"""Tableau Workbook Comparer.

A comprehensive tool to parse, peel off layer-by-layer, and compare two Tableau Workbook
(.twb or .twbx) XML files. It extracts and diffs metadata, parameters, datasources,
custom SQL, calculated fields, worksheets, dashboards, layout zones, and actions.
"""

import sys
import os
import zipfile
import json
import argparse
import difflib
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple, Set


class WorkbookLoader:
    """Handles loading and XML extraction for .twb and .twbx files."""

    @staticmethod
    def load_xml_root(file_path: Path) -> ET.Element:
        """Loads the XML root from a .twb or .twbx file."""
        if not file_path.exists():
            raise FileNotFoundError(f"Workbook file not found: {file_path}")

        if file_path.suffix.lower() == ".twbx":
            return WorkbookLoader._extract_twbx_xml(file_path)
        elif file_path.suffix.lower() == ".twb":
            return ET.parse(file_path).getroot()
        else:
            # Fallback attempt parsing as XML
            try:
                return ET.parse(file_path).getroot()
            except Exception as e:
                raise ValueError(f"Unsupported file format or unparseable XML in {file_path}: {e}")

    @staticmethod
    def _extract_twbx_xml(twbx_path: Path) -> ET.Element:
        """Extracts the main .twb file from a packaged .twbx ZIP archive."""
        with zipfile.ZipFile(twbx_path, "r") as z:
            twb_files = [f for f in z.namelist() if f.endswith(".twb") and not f.startswith("__MACOSX")]
            if not twb_files:
                raise ValueError(f"No .twb file found inside {twbx_path}")
            # Pick the root twb file
            main_twb = sorted(twb_files, key=lambda x: x.count('/'))[0]
            with z.open(main_twb) as f:
                return ET.parse(f).getroot()


class TableauXMLPeeler:
    """Peels off a Tableau Workbook XML layer by layer into structured representations."""

    def __init__(self, root: ET.Element):
        self.root = root

    def peel_all(self) -> Dict[str, Any]:
        """Runs full layer-by-layer peeling of the XML document."""
        return {
            "metadata": self.peel_metadata(),
            "parameters": self.peel_parameters(),
            "datasources": self.peel_datasources(),
            "worksheets": self.peel_worksheets(),
            "dashboards": self.peel_dashboards(),
            "actions": self.peel_actions(),
        }

    def peel_metadata(self) -> Dict[str, Any]:
        """Layer 1: Root attributes, document properties, and preferences."""
        attribs = dict(self.root.attrib)
        version = attribs.get("version", "unknown")
        source_build = attribs.get("source-build", "unknown")
        tableau_version = attribs.get("tableau-version", attribs.get("original-version", "unknown"))

        doc_props = {}
        for prop in self.root.findall("./document-properties/*"):
            doc_props[prop.tag] = prop.text or prop.get("value", "")

        preferences = {}
        for pref in self.root.findall("./preferences/preference"):
            p_name = pref.get("name", "")
            if p_name:
                preferences[p_name] = pref.get("value", "")

        return {
            "version": version,
            "source_build": source_build,
            "tableau_version": tableau_version,
            "document_properties": doc_props,
            "preferences": preferences,
        }

    def peel_parameters(self) -> Dict[str, Dict[str, Any]]:
        """Layer 2: Extract Parameters (stored under special datasource 'Parameters')."""
        parameters = {}
        for ds in self.root.findall("./datasources/datasource"):
            ds_name = ds.get("name", "")
            if ds_name == "Parameters" or ds.get("caption") == "Parameters":
                for col in ds.findall("./column"):
                    p_name = col.get("name", "")
                    caption = col.get("caption", p_name)
                    datatype = col.get("datatype", "")
                    value = col.get("value", "")
                    param_type = col.get("param-domain-type", "all")

                    # Formula/Calculation if present
                    calc_elem = col.find("./calculation")
                    formula = calc_elem.get("formula", "") if calc_elem is not None else ""

                    # Range / allowable values
                    members = []
                    for m in col.findall("./members/member"):
                        members.append(m.get("value", ""))

                    parameters[p_name] = {
                        "name": p_name,
                        "caption": caption,
                        "datatype": datatype,
                        "current_value": value,
                        "domain_type": param_type,
                        "formula": formula,
                        "allowable_values": members,
                    }
        return parameters

    def peel_datasources(self) -> Dict[str, Dict[str, Any]]:
        """Layer 3: Extract Datasources, Connections, Custom SQL, Relations, Fields, Calc Fields."""
        datasources = {}
        for ds in self.root.findall("./datasources/datasource"):
            ds_name = ds.get("name", "")
            if not ds_name or ds_name == "Parameters":
                continue

            caption = ds.get("caption", ds_name)
            inline = ds.get("inline", "true")
            has_extract = ds.find("./extract") is not None

            connections = []
            custom_sql_list = []
            tables = []
            joins = []

            # Parse Connection & Relations
            for conn in ds.findall(".//connection"):
                conn_class = conn.get("class", "")
                server = conn.get("server", "")
                dbname = conn.get("dbname", "")
                schema = conn.get("schema", "")
                if conn_class and conn_class != "federated":
                    connections.append({
                        "class": conn_class,
                        "server": server,
                        "dbname": dbname,
                        "schema": schema,
                    })

            # Parse Relations (Tables, Custom SQL, Joins)
            for rel in ds.findall(".//relation"):
                rel_type = rel.get("type", "")
                rel_name = rel.get("name", rel.get("table", ""))
                if rel_type == "text":  # Custom SQL
                    sql_text = rel.text.strip() if rel.text else ""
                    custom_sql_list.append({
                        "name": rel_name,
                        "sql": sql_text,
                    })
                elif rel_type == "table":
                    tables.append(rel.get("table", rel_name))
                elif rel_type == "join":
                    join_type = rel.get("join", "")
                    clause_keys = []
                    for clause in rel.findall(".//clause"):
                        for expression in clause.findall(".//expression"):
                            clause_keys.append(expression.get("op", ""))
                    joins.append({
                        "type": join_type,
                        "clauses": clause_keys,
                    })

            # Parse Columns & Calculated Fields
            calc_fields = {}
            regular_columns = {}
            for col in ds.findall("./column"):
                c_name = col.get("name", "")
                if not c_name:
                    continue
                c_caption = col.get("caption", c_name)
                c_datatype = col.get("datatype", "")
                c_role = col.get("role", "")
                c_type = col.get("type", "")

                calc_elem = col.find("./calculation")
                if calc_elem is not None:
                    calc_fields[c_name] = {
                        "name": c_name,
                        "caption": c_caption,
                        "datatype": c_datatype,
                        "role": c_role,
                        "formula": calc_elem.get("formula", "").strip(),
                    }
                else:
                    regular_columns[c_name] = {
                        "name": c_name,
                        "caption": c_caption,
                        "datatype": c_datatype,
                        "role": c_role,
                        "type": c_type,
                    }

            # Parse Folders
            folders = []
            for folder in ds.findall("./folder-model/folder"):
                f_name = folder.get("name", "")
                f_cols = [c.get("name", "") for c in folder.findall("./folder-item")]
                folders.append({"name": f_name, "columns": f_cols})

            datasources[ds_name] = {
                "name": ds_name,
                "caption": caption,
                "inline": inline,
                "has_extract": has_extract,
                "connections": connections,
                "custom_sql": custom_sql_list,
                "tables": sorted(list(set(tables))),
                "joins": joins,
                "calculated_fields": calc_fields,
                "regular_columns": regular_columns,
                "folders": folders,
            }

        return datasources

    def peel_worksheets(self) -> Dict[str, Dict[str, Any]]:
        """Layer 4: Extract Worksheets, Shelves, Marks card encodings, and Filters."""
        worksheets = {}
        for ws in self.root.findall("./worksheets/worksheet"):
            ws_name = ws.get("name", "")
            if not ws_name:
                continue

            # Rows and Cols shelves
            rows_elem = ws.find(".//table/rows")
            cols_elem = ws.find(".//table/cols")
            rows = rows_elem.text.strip() if rows_elem is not None and rows_elem.text else ""
            cols = cols_elem.text.strip() if cols_elem is not None and cols_elem.text else ""

            # Marks card encodings
            mark_class = ""
            mark_encodings = []
            for pane in ws.findall(".//table/panes/pane"):
                m_elem = pane.find("./mark")
                if m_elem is not None:
                    mark_class = m_elem.get("class", "")
                for enc in pane.findall(".//encoding"):
                    attr = enc.get("attr", "")
                    field = enc.get("field", "")
                    if attr and field:
                        mark_encodings.append(f"{attr}:{field}")

            # Filters / Slices
            filters = []
            for slice_elem in ws.findall(".//table/slices/slice"):
                f_field = slice_elem.text.strip() if slice_elem.text else ""
                filters.append(f_field)

            worksheets[ws_name] = {
                "name": ws_name,
                "rows": rows,
                "cols": cols,
                "mark_class": mark_class,
                "mark_encodings": sorted(list(set(mark_encodings))),
                "filters": sorted(filters),
            }

        return worksheets

    def peel_dashboards(self) -> Dict[str, Dict[str, Any]]:
        """Layer 5: Extract Dashboards, Size settings, Embedded worksheets, and Zones."""
        dashboards = {}
        for db in self.root.findall("./dashboards/dashboard"):
            db_name = db.get("name", "")
            if not db_name:
                continue

            size_elem = db.find("./size")
            db_size = {}
            if size_elem is not None:
                db_size = {
                    "preset": size_elem.get("preset", ""),
                    "maxwidth": size_elem.get("maxwidth", ""),
                    "maxheight": size_elem.get("maxheight", ""),
                    "minwidth": size_elem.get("minwidth", ""),
                    "minheight": size_elem.get("minheight", ""),
                }

            # Extracted worksheets in zones
            contained_worksheets = []
            zones = []
            for zone in db.findall(".//zone"):
                zone_type = zone.get("type-HP", zone.get("type", ""))
                ws_ref = zone.get("name", "")
                if ws_ref:
                    contained_worksheets.append(ws_ref)
                if zone_type:
                    zones.append({"type": zone_type, "name": ws_ref})

            # Unique contained worksheets
            unique_worksheets = sorted(list(set([w for w in contained_worksheets if w])))

            dashboards[db_name] = {
                "name": db_name,
                "size": db_size,
                "worksheets": unique_worksheets,
                "zone_count": len(zones),
            }

        return dashboards

    def peel_actions(self) -> Dict[str, Dict[str, Any]]:
        """Layer 6: Extract Dashboard Actions (filter, highlight, url, parameter, set)."""
        actions = {}
        for act in self.root.findall("./actions/action"):
            act_name = act.get("caption", act.get("name", ""))
            if not act_name:
                continue

            # Determine Action type
            act_type = "unknown"
            sources = []
            targets = []

            activation = act.find("./activation")
            trigger = activation.get("type", "") if activation is not None else ""

            # Check action child type elements
            for child in act:
                if child.tag.endswith("action"):
                    act_type = child.tag.replace("-action", "")
                    for src in child.findall(".//source"):
                        if src.get("worksheet"):
                            sources.append(src.get("worksheet"))
                        if src.get("dashboard"):
                            sources.append(src.get("dashboard"))
                    for tgt in child.findall(".//target"):
                        if tgt.get("worksheet"):
                            targets.append(tgt.get("worksheet"))
                        if tgt.get("dashboard"):
                            targets.append(tgt.get("dashboard"))

            actions[act_name] = {
                "name": act_name,
                "type": act_type,
                "trigger": trigger,
                "sources": sorted(list(set(sources))),
                "targets": sorted(list(set(targets))),
            }

        return actions


class WorkbookComparer:
    """Compares two peeled Tableau workbook data dictionaries and produces detailed diffs."""

    def __init__(self, wb1_data: Dict[str, Any], wb2_data: Dict[str, Any]):
        self.wb1 = wb1_data
        self.wb2 = wb2_data

    def compare(self) -> Dict[str, Any]:
        """Runs comparisons across all layers."""
        return {
            "metadata": self._compare_metadata(),
            "parameters": self._compare_parameters(),
            "datasources": self._compare_datasources(),
            "worksheets": self._compare_worksheets(),
            "dashboards": self._compare_dashboards(),
            "actions": self._compare_actions(),
            "summary": {},  # Will be populated
        }

    def _compare_metadata(self) -> Dict[str, Any]:
        m1, m2 = self.wb1["metadata"], self.wb2["metadata"]
        return {
            "version_changed": m1["version"] != m2["version"],
            "v1_version": m1["version"],
            "v2_version": m2["version"],
            "v1_build": m1["source_build"],
            "v2_build": m2["source_build"],
        }

    def _compare_parameters(self) -> Dict[str, Any]:
        p1, p2 = self.wb1["parameters"], self.wb2["parameters"]
        keys1, keys2 = set(p1.keys()), set(p2.keys())

        added = [p2[k] for k in sorted(list(keys2 - keys1))]
        removed = [p1[k] for k in sorted(list(keys1 - keys2))]
        modified = []

        for k in sorted(list(keys1 & keys2)):
            item1, item2 = p1[k], p2[k]
            diffs = []
            if item1["current_value"] != item2["current_value"]:
                diffs.append(f"Value: '{item1['current_value']}' -> '{item2['current_value']}'")
            if item1["formula"] != item2["formula"]:
                formula_diff = self._generate_diff(item1["formula"], item2["formula"])
                diffs.append(f"Formula modified:\n{formula_diff}")
            if item1["allowable_values"] != item2["allowable_values"]:
                diffs.append(f"Allowable values modified: {item1['allowable_values']} -> {item2['allowable_values']}")

            if diffs:
                modified.append({
                    "name": k,
                    "caption": item2["caption"],
                    "diffs": diffs
                })

        return {
            "added": added,
            "removed": removed,
            "modified": modified,
            "unchanged_count": len(keys1 & keys2) - len(modified)
        }

    def _compare_datasources(self) -> Dict[str, Any]:
        ds1, ds2 = self.wb1["datasources"], self.wb2["datasources"]
        keys1, keys2 = set(ds1.keys()), set(ds2.keys())

        added = [ds2[k] for k in sorted(list(keys2 - keys1))]
        removed = [ds1[k] for k in sorted(list(keys1 - keys2))]
        modified = []

        for k in sorted(list(keys1 & keys2)):
            d1, d2 = ds1[k], ds2[k]
            diffs = []

            # Custom SQL Diffs
            sql1 = {s["name"]: s["sql"] for s in d1["custom_sql"]}
            sql2 = {s["name"]: s["sql"] for s in d2["custom_sql"]}
            for sql_name in sorted(list(set(sql1.keys()) | set(sql2.keys()))):
                if sql_name in sql1 and sql_name not in sql2:
                    diffs.append(f"Custom SQL Removed: [{sql_name}]")
                elif sql_name in sql2 and sql_name not in sql1:
                    diffs.append(f"Custom SQL Added: [{sql_name}]\nSQL:\n{sql2[sql_name]}")
                elif sql1[sql_name] != sql2[sql_name]:
                    s_diff = self._generate_diff(sql1[sql_name], sql2[sql_name])
                    diffs.append(f"Custom SQL Modified: [{sql_name}]\n{s_diff}")

            # Calculated Fields Diffs
            cf1, cf2 = d1["calculated_fields"], d2["calculated_fields"]
            cf_keys1, cf_keys2 = set(cf1.keys()), set(cf2.keys())
            for c_key in sorted(list(cf_keys2 - cf_keys1)):
                diffs.append(f"Calculated Field Added: [{cf2[c_key]['caption']}] ({cf2[c_key]['formula']})")
            for c_key in sorted(list(cf_keys1 - cf_keys2)):
                diffs.append(f"Calculated Field Removed: [{cf1[c_key]['caption']}]")
            for c_key in sorted(list(cf_keys1 & cf_keys2)):
                c1, c2 = cf1[c_key], cf2[c_key]
                if c1["formula"] != c2["formula"]:
                    f_diff = self._generate_diff(c1["formula"], c2["formula"])
                    diffs.append(f"Calculated Field Formula Modified: [{c2['caption']}]\n{f_diff}")

            # Tables Diffs
            t1, t2 = set(d1["tables"]), set(d2["tables"])
            if t1 != t2:
                if t2 - t1:
                    diffs.append(f"Tables Added: {sorted(list(t2 - t1))}")
                if t1 - t2:
                    diffs.append(f"Tables Removed: {sorted(list(t1 - t2))}")

            if diffs:
                modified.append({
                    "name": k,
                    "caption": d2["caption"],
                    "diffs": diffs
                })

        return {
            "added": added,
            "removed": removed,
            "modified": modified,
            "unchanged_count": len(keys1 & keys2) - len(modified)
        }

    def _compare_worksheets(self) -> Dict[str, Any]:
        ws1, ws2 = self.wb1["worksheets"], self.wb2["worksheets"]
        keys1, keys2 = set(ws1.keys()), set(ws2.keys())

        added = [ws2[k] for k in sorted(list(keys2 - keys1))]
        removed = [ws1[k] for k in sorted(list(keys1 - keys2))]
        modified = []

        for k in sorted(list(keys1 & keys2)):
            w1, w2 = ws1[k], ws2[k]
            diffs = []
            if w1["rows"] != w2["rows"]:
                diffs.append(f"Rows shelf modified:\n  Old: {w1['rows']}\n  New: {w2['rows']}")
            if w1["cols"] != w2["cols"]:
                diffs.append(f"Cols shelf modified:\n  Old: {w1['cols']}\n  New: {w2['cols']}")
            if w1["mark_class"] != w2["mark_class"]:
                diffs.append(f"Mark type changed: {w1['mark_class']} -> {w2['mark_class']}")
            if w1["filters"] != w2["filters"]:
                diffs.append(f"Filters modified:\n  Old: {w1['filters']}\n  New: {w2['filters']}")

            if diffs:
                modified.append({
                    "name": k,
                    "diffs": diffs
                })

        return {
            "added": added,
            "removed": removed,
            "modified": modified,
            "unchanged_count": len(keys1 & keys2) - len(modified)
        }

    def _compare_dashboards(self) -> Dict[str, Any]:
        db1, db2 = self.wb1["dashboards"], self.wb2["dashboards"]
        keys1, keys2 = set(db1.keys()), set(db2.keys())

        added = [db2[k] for k in sorted(list(keys2 - keys1))]
        removed = [db1[k] for k in sorted(list(keys1 - keys2))]
        modified = []

        for k in sorted(list(keys1 & keys2)):
            d1, d2 = db1[k], db2[k]
            diffs = []
            if d1["worksheets"] != d2["worksheets"]:
                diffs.append(f"Contained worksheets modified:\n  Old: {d1['worksheets']}\n  New: {d2['worksheets']}")
            if d1["size"] != d2["size"]:
                diffs.append(f"Dashboard sizing changed:\n  Old: {d1['size']}\n  New: {d2['size']}")

            if diffs:
                modified.append({
                    "name": k,
                    "diffs": diffs
                })

        return {
            "added": added,
            "removed": removed,
            "modified": modified,
            "unchanged_count": len(keys1 & keys2) - len(modified)
        }

    def _compare_actions(self) -> Dict[str, Any]:
        a1, a2 = self.wb1["actions"], self.wb2["actions"]
        keys1, keys2 = set(a1.keys()), set(a2.keys())

        added = [a2[k] for k in sorted(list(keys2 - keys1))]
        removed = [a1[k] for k in sorted(list(keys1 - keys2))]
        modified = []

        for k in sorted(list(keys1 & keys2)):
            item1, item2 = a1[k], a2[k]
            diffs = []
            if item1["sources"] != item2["sources"]:
                diffs.append(f"Sources modified: {item1['sources']} -> {item2['sources']}")
            if item1["targets"] != item2["targets"]:
                diffs.append(f"Targets modified: {item1['targets']} -> {item2['targets']}")

            if diffs:
                modified.append({
                    "name": k,
                    "diffs": diffs
                })

        return {
            "added": added,
            "removed": removed,
            "modified": modified,
            "unchanged_count": len(keys1 & keys2) - len(modified)
        }

    @staticmethod
    def _generate_diff(text1: str, text2: str) -> str:
        """Generates a clean line-by-line diff string between two text blocks."""
        lines1 = text1.splitlines()
        lines2 = text2.splitlines()
        diff = difflib.unified_diff(lines1, lines2, lineterm="")
        return "\n".join(list(diff)[2:])  # strip header lines


class ReportGenerator:
    """Generates console, markdown, and JSON report representations."""

    @staticmethod
    def generate_console_summary(comparison: Dict[str, Any], file1: str, file2: str) -> str:
        lines = []
        lines.append("================================================================================")
        lines.append("                      TABLEAU WORKBOOK COMPARISON REPORT                        ")
        lines.append("================================================================================")
        lines.append(f" Base Workbook  (V1): {file1}")
        lines.append(f" Target Workbook(V2): {file2}")
        lines.append("================================================================================\n")

        # Layer 1: Metadata
        meta = comparison["metadata"]
        lines.append("--- LAYER 1: WORKBOOK METADATA ---")
        if meta["version_changed"]:
            lines.append(f" [!] Version changed from {meta['v1_version']} to {meta['v2_version']}")
        else:
            lines.append(f" [=] Version: {meta['v1_version']} (Unchanged)")
        lines.append("")

        # Layer 2: Parameters
        params = comparison["parameters"]
        lines.append(f"--- LAYER 2: PARAMETERS (Added: {len(params['added'])}, Removed: {len(params['removed'])}, Modified: {len(params['modified'])}) ---")
        for p in params["added"]:
            lines.append(f" [+] ADDED: Parameter [{p['caption']}] ({p['datatype']}) = '{p['current_value']}'")
        for p in params["removed"]:
            lines.append(f" [-] REMOVED: Parameter [{p['caption']}]")
        for p in params["modified"]:
            lines.append(f" [*] MODIFIED: Parameter [{p['caption']}]")
            for d in p["diffs"]:
                lines.append(f"     {d}")
        lines.append("")

        # Layer 3: Datasources
        ds = comparison["datasources"]
        lines.append(f"--- LAYER 3: DATASOURCES & CALCULATIONS (Added: {len(ds['added'])}, Removed: {len(ds['removed'])}, Modified: {len(ds['modified'])}) ---")
        for item in ds["added"]:
            lines.append(f" [+] ADDED DATASOURCE: [{item['caption']}]")
        for item in ds["removed"]:
            lines.append(f" [-] REMOVED DATASOURCE: [{item['caption']}]")
        for item in ds["modified"]:
            lines.append(f" [*] MODIFIED DATASOURCE: [{item['caption']}]")
            for d in item["diffs"]:
                indented = "\n".join(["     " + l for l in d.splitlines()])
                lines.append(indented)
        lines.append("")

        # Layer 4: Worksheets
        ws = comparison["worksheets"]
        lines.append(f"--- LAYER 4: WORKSHEETS (Added: {len(ws['added'])}, Removed: {len(ws['removed'])}, Modified: {len(ws['modified'])}) ---")
        for w in ws["added"]:
            lines.append(f" [+] ADDED WORKSHEET: [{w['name']}]")
        for w in ws["removed"]:
            lines.append(f" [-] REMOVED WORKSHEET: [{w['name']}]")
        for w in ws["modified"]:
            lines.append(f" [*] MODIFIED WORKSHEET: [{w['name']}]")
            for d in w["diffs"]:
                indented = "\n".join(["     " + l for l in d.splitlines()])
                lines.append(indented)
        lines.append("")

        # Layer 5: Dashboards
        db = comparison["dashboards"]
        lines.append(f"--- LAYER 5: DASHBOARDS (Added: {len(db['added'])}, Removed: {len(db['removed'])}, Modified: {len(db['modified'])}) ---")
        for d in db["added"]:
            lines.append(f" [+] ADDED DASHBOARD: [{d['name']}]")
        for d in db["removed"]:
            lines.append(f" [-] REMOVED DASHBOARD: [{d['name']}]")
        for d in db["modified"]:
            lines.append(f" [*] MODIFIED DASHBOARD: [{d['name']}]")
            for diff_item in d["diffs"]:
                indented = "\n".join(["     " + l for l in diff_item.splitlines()])
                lines.append(indented)
        lines.append("")

        # Layer 6: Actions
        act = comparison["actions"]
        lines.append(f"--- LAYER 6: DASHBOARD ACTIONS (Added: {len(act['added'])}, Removed: {len(act['removed'])}, Modified: {len(act['modified'])}) ---")
        for a in act["added"]:
            lines.append(f" [+] ADDED ACTION: [{a['name']}] ({a['type']})")
        for a in act["removed"]:
            lines.append(f" [-] REMOVED ACTION: [{a['name']}]")
        for a in act["modified"]:
            lines.append(f" [*] MODIFIED ACTION: [{a['name']}]")
            for d in a["diffs"]:
                lines.append(f"     {d}")
        lines.append("\n================================================================================")
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Tableau Workbook XML Layer-by-Layer Comparer")
    parser.add_argument("file1", type=Path, help="Path to first workbook (.twb or .twbx)")
    parser.add_argument("file2", type=Path, help="Path to second workbook (.twb or .twbx)")
    parser.add_argument("--json", type=Path, help="Export comparison report as JSON file")
    parser.add_argument("--markdown", type=Path, help="Export comparison report as Markdown file")

    args = parser.parse_args()

    # Load XML roots
    root1 = WorkbookLoader.load_xml_root(args.file1)
    root2 = WorkbookLoader.load_xml_root(args.file2)

    # Peel XML layer by layer
    peeler1 = TableauXMLPeeler(root1)
    peeler2 = TableauXMLPeeler(root2)

    wb1_data = peeler1.peel_all()
    wb2_data = peeler2.peel_all()

    # Run comparisons
    comparer = WorkbookComparer(wb1_data, wb2_data)
    result = comparer.compare()

    # Print Console Summary
    report_text = ReportGenerator.generate_console_summary(result, str(args.file1), str(args.file2))
    print(report_text)

    # Optional JSON Export
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)
        print(f"\n[+] Report exported to JSON: {args.json}")

    # Optional Markdown Export
    if args.markdown:
        with open(args.markdown, "w", encoding="utf-8") as f:
            f.write(f"# Tableau Workbook Comparison Report\n\n```text\n{report_text}\n```\n")
        print(f"[+] Report exported to Markdown: {args.markdown}")


if __name__ == "__main__":
    main()
