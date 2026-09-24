# Tableau Workbook Comparison Report

```text
================================================================================
                      TABLEAU WORKBOOK COMPARISON REPORT                        
================================================================================
 Base Workbook  (V1): tests/sample_v1_old.twb
 Target Workbook(V2): tests/sample_v2_recent.twb
================================================================================

--- LAYER 1: WORKBOOK METADATA ---
 [!] Version changed from 18.1 to 18.2

--- LAYER 2: PARAMETERS (Added: 1, Removed: 0, Modified: 1) ---
 [+] ADDED: Parameter [Discount Rate Threshold] (real) = '0.15'
 [*] MODIFIED: Parameter [Region Parameter]
     Value: '"EMEA"' -> '"GLOBAL"'
     Allowable values modified: ['"EMEA"', '"AMER"', '"APAC"'] -> ['"EMEA"', '"AMER"', '"APAC"', '"GLOBAL"']

--- LAYER 3: DATASOURCES & CALCULATIONS (Added: 0, Removed: 0, Modified: 1) ---
 [*] MODIFIED DATASOURCE: [Sales Orders DB]
     Custom SQL Modified: [Custom SQL Query]
     @@ -1,3 +1,3 @@
     -SELECT order_id, customer_id, order_date, sales, profit
     +SELECT order_id, customer_id, order_date, sales, profit, discount_amount
                FROM presentation.fact_sales_orders
                WHERE order_date >= '2023-01-01'
     Calculated Field Added: [Customer CLV] (SUM([sales]) * 1.25)
     Calculated Field Formula Modified: [Profit Margin]
     @@ -1 +1 @@
     -SUM([profit]) / SUM([sales])
     +IF SUM([sales]) > 0 THEN SUM([profit]) / SUM([sales]) ELSE 0 END

--- LAYER 4: WORKSHEETS (Added: 1, Removed: 1, Modified: 1) ---
 [+] ADDED WORKSHEET: [Customer Retention Analysis]
 [-] REMOVED WORKSHEET: [Deprecated Regional Sheet]
 [*] MODIFIED WORKSHEET: [Sales Overview]
     Mark type changed: bar -> line

--- LAYER 5: DASHBOARDS (Added: 0, Removed: 0, Modified: 1) ---
 [*] MODIFIED DASHBOARD: [Executive Sales Dashboard]
     Contained worksheets modified:
       Old: ['Sales Overview']
       New: ['Customer Retention Analysis', 'Sales Overview']
     Dashboard sizing changed:
       Old: {'preset': 'automatic', 'maxwidth': '1200', 'maxheight': '800', 'minwidth': '', 'minheight': ''}
       New: {'preset': 'fixed', 'maxwidth': '1400', 'maxheight': '900', 'minwidth': '', 'minheight': ''}

--- LAYER 6: DASHBOARD ACTIONS (Added: 0, Removed: 0, Modified: 1) ---
 [*] MODIFIED ACTION: [Filter to Customer]
     Targets modified: ['Executive Sales Dashboard'] -> ['Customer Retention Analysis']

================================================================================
```
