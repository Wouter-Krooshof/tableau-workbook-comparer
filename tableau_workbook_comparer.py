"""Tableau Workbook Comparer.

Tool to parse and compare two Tableau Workbook (.twb) XML files.
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any, List


def parse_workbook(file_path: Path) -> Dict[str, Any]:
    """Parse a Tableau Workbook (.twb) XML file and extract key components."""
    tree = ET.parse(file_path)
    root = tree.getroot()

    datasources = []
    for ds in root.findall(".//datasource"):
        ds_name = ds.get("name", "")
        caption = ds.get("caption", ds_name)
        if ds_name:
            datasources.append({"name": ds_name, "caption": caption})

    worksheets = []
    for ws in root.findall(".//worksheet"):
        ws_name = ws.get("name", "")
        if ws_name:
            worksheets.append(ws_name)

    dashboards = []
    for db in root.findall(".//dashboard"):
        db_name = db.get("name", "")
        if db_name:
            dashboards.append(db_name)

    return {
        "datasources": datasources,
        "worksheets": worksheets,
        "dashboards": dashboards,
    }


def compare_workbooks(wb1_data: Dict[str, Any], wb2_data: Dict[str, Any]) -> Dict[str, Any]:
    """Compare two parsed workbook data structures."""
    ws1 = set(wb1_data["worksheets"])
    ws2 = set(wb2_data["worksheets"])

    db1 = set(wb1_data["dashboards"])
    db2 = set(wb2_data["dashboards"])

    return {
        "worksheets": {
            "added": sorted(list(ws2 - ws1)),
            "removed": sorted(list(ws1 - ws2)),
            "common": sorted(list(ws1 & ws2)),
        },
        "dashboards": {
            "added": sorted(list(db2 - db1)),
            "removed": sorted(list(db1 - db2)),
            "common": sorted(list(db1 & db2)),
        },
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python tableau_workbook_comparer.py <file1.twb> <file2.twb>")
        sys.exit(1)

    file1 = Path(sys.argv[1])
    file2 = Path(sys.argv[2])

    if not file1.exists() or not file2.exists():
        print("Error: One or both workbook files do not exist.")
        sys.exit(1)

    print(f"Comparing '{file1.name}' and '{file2.name}'...")
    wb1 = parse_workbook(file1)
    wb2 = parse_workbook(file2)

    diff = compare_workbooks(wb1, wb2)

    print("\n--- Worksheets ---")
    print(f"Added: {diff['worksheets']['added']}")
    print(f"Removed: {diff['worksheets']['removed']}")

    print("\n--- Dashboards ---")
    print(f"Added: {diff['dashboards']['added']}")
    print(f"Removed: {diff['dashboards']['removed']}")


if __name__ == "__main__":
    main()
