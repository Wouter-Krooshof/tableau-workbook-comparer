# Tableau Workbook Comparer

A tool to parse, compare, and diff Tableau Workbooks (`.twb` and `.twbx` files) to identify differences in datasources, calculated fields, worksheets, dashboards, parameters, and filters.

## Features

- **XML & Workbook Parsing**: Extract metadata and structure from Tableau Workbook XML.
- **Calculated Fields Diffing**: Compare formulas and definitions across workbook versions.
- **Datasource & Connection Comparison**: Identify changes in tables, joins, and custom SQL queries.
- **Worksheet & Dashboard Tracking**: Detect added, removed, or modified visual components.

## Usage

```bash
python tableau_workbook_comparer.py path/to/workbook1.twb path/to/workbook2.twb
```

## Setup

```bash
pip install -r requirements.txt
```
