# Tableau Workbook Comparison Report

```text
================================================================================
                      TABLEAU WORKBOOK COMPARISON REPORT                        
================================================================================
 Base Workbook  (V1): Daily Group Sales_7.twb
 Target Workbook(V2): Daily Group Sales_13.twb
================================================================================

--- LAYER 1: WORKBOOK METADATA ---
 [=] Version: 18.1 (Unchanged)

--- LAYER 2: PARAMETERS (Added: 0, Removed: 0, Modified: 1) ---
 [*] MODIFIED: Parameter [pm_date]
     Value: '#2026-09-24#' -> '#2026-09-23#'
     Formula modified:
@@ -1 +1 @@
-#2026-09-24#
+#2026-09-23#

--- LAYER 3: DATASOURCES & CALCULATIONS (Added: 1, Removed: 1, Modified: 0) ---
 [+] ADDED DATASOURCE: [Daily Group Sales 3.0]
 [-] REMOVED DATASOURCE: [Grouped External Sales 2.0 new]

--- LAYER 4: WORKSHEETS (Added: 1, Removed: 1, Modified: 43) ---
 [+] ADDED WORKSHEET: [map - TO delta% vs budget 2.0]
 [-] REMOVED WORKSHEET: [map - TO Δ% vs budget]
 [*] MODIFIED WORKSHEET: [FX]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:csbuCountry_Reporting:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:csbu_country_reporting:nk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [FX measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [FX trend]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[Multiple Values]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[Multiple Values]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [Full Month]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names] / [Grouped External Sales 2.0 (local copy) (copy)].[yr:InvoiceDate:ok])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names] / [federated.07pdzlx0k2seif18uh2zd1jwbeij].[yr:invoice_date:ok])
 [*] MODIFIED WORKSHEET: [LC business type]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[none:Business_Type_Group_2:nk] / [Grouped External Sales 2.0 (local copy) (copy)].[none:Businesstype:nk])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:business_type_group_2:nk] / [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:business_type:nk])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [TO LC measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [TO measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [TO measures (2)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [TO measures (3)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [TO measures (4)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [Table: Business type vs. Industry]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[none:Business Type Group 2 (copy)_1386545745140359168:nk] / [Grouped External Sales 2.0 (local copy) (copy)].[none:Businesstype:nk])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:Business Type Group 2 (copy)_1386545745140359168:nk] / [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:business_type:nk])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:Industry:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:industry:nk]
 [*] MODIFIED WORKSHEET: [Table: Business type vs. Industry Perspective 2]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[none:Business Type Group 2 (copy)_1386545745140359168:nk] / [Grouped External Sales 2.0 (local copy) (copy)].[none:Businesstype:nk])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:Business Type Group 2 (copy)_1386545745140359168:nk] / [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:business_type:nk])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:Calculation_2686115737618796548:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:product_category:nk]
 [*] MODIFIED WORKSHEET: [Volume measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [Volume measures (2)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [Volume measures (3)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [daily bars day (2)]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[sum:Turnover (copy)_1754433544814776320:qk] + ([Grouped External Sales 2.0 (local copy) (copy)].[sum:TurnoverEuro:qk] + ([Grouped External Sales 2.0 (local copy) (copy)].[cum:sum:Turnover (copy)_1754433544814776320:qk] + [Grouped External Sales 2.0 (local copy) (copy)].[usr:Calculation_3836222468677021698:qk])))
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:Turnover (copy)_1754433544814776320:qk] + ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:turnover_euro:qk] + ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[cum:sum:Turnover (copy)_1754433544814776320:qk] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[usr:Calculation_3836222468677021698:qk])))
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[dy:InvoiceDate:ok]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[dy:invoice_date:ok]
 [*] MODIFIED WORKSHEET: [detail absolute]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:per what 3a (copy)_1173469180404498434:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:per what 3a (copy)_1173469180404498434:nk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [detail table]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[none:Calculation_413205315849248770:ok] / ([Grouped External Sales 2.0 (local copy) (copy)].[none:Calculation_413205315869618191:ok] / [Grouped External Sales 2.0 (local copy) (copy)].[none:Calculation_2771402638455300096:ok]))
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:Calculation_413205315849248770:ok] / ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:Calculation_413205315869618191:ok] / [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:Calculation_2771402638455300096:ok]))
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [detail table (2)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[dy:InvoiceDate:ok]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[dy:invoice_date:ok]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [highlight table 1 CSBU prod cat]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:Calculation_2686115737618796548:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:product_category:nk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [highlight table 1 CSBU segment]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:Industry:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:industry:nk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [highlight table 2 CSBU Business Type]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[none:Business Type Group 2 (copy)_1386545745140359168:nk] / [Grouped External Sales 2.0 (local copy) (copy)].[none:Businesstype:nk])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:Business Type Group 2 (copy)_1386545745140359168:nk] / [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:business_type:nk])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [highlight table CSBU]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[none:Cluster:nk] / [Grouped External Sales 2.0 (local copy) (copy)].[none:csbuCountryJoin:nk])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:cluster:nk] / [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:csbu_country_join:nk])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [inv days]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:csbuCountry_Reporting:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:csbu_country_reporting:nk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [lc TO measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [lc Volume measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [lc margin measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [lc prod cat]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:Calculation_2686115737618796548:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:product_category:nk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [lc segment]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[none:Industry:nk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:industry:nk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [lc trend OL]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[sum:Calculation_1456914503679799305:qk] + [Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Calculation_1456914503679799305:qk:4])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:Calculation_1456914503679799305:qk] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:Calculation_1456914503679799305:qk:4])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [lc trend TO]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[sum:Turnover:qk] + [Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Turnover:qk:4])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:turnover:qk] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:turnover:qk:4])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [lc trend margin %]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[usr:Margin % lc LY (copy)_413205315887923229:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[usr:Margin % lc LY (copy)_413205315887923229:qk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [map]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[Latitude (generated)]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[Latitude (generated)]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[Longitude (generated)]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[Longitude (generated)]
 [*] MODIFIED WORKSHEET: [map - margin Δ% vs budget]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[Latitude (generated)]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[Latitude (generated)]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[Longitude (generated)]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[Longitude (generated)]
 [*] MODIFIED WORKSHEET: [margin measures]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [margin measures (2)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [margin measures (3)]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[:Measure Names]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[:Measure Names]
 [*] MODIFIED WORKSHEET: [small multiples]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Calculation_1813824758949527643:qk:2] + ([Grouped External Sales 2.0 (local copy) (copy)].[usr:Calculation_1410752630613745666:qk:2] + ([Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Calculation_1372190548022374405:qk:6] + [Grouped External Sales 2.0 (local copy) (copy)].[usr:Margin % CY (copy)_411516457497165824:qk])))
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:Calculation_1813824758949527643:qk:2] + ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[usr:Calculation_1410752630613745666:qk:2] + ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:Calculation_1372190548022374405:qk:6] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[usr:Margin % CY (copy)_411516457497165824:qk])))
     Cols shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[none:per what filter segment (copy)_280630594442031106:nk] * [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[none:per what filter segment (copy)_280630594442031106:nk] * [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk])
 [*] MODIFIED WORKSHEET: [trend OL]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[sum:Calculation_1456914503679799305:qk] + [Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Calculation_1456914503679799305:qk:4])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:Calculation_1456914503679799305:qk] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:Calculation_1456914503679799305:qk:4])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [trend TO]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[sum:Calculation_1813824758949527643:qk] + [Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Calculation_1813824758949527643:qk:4])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:Calculation_1813824758949527643:qk] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:Calculation_1813824758949527643:qk:4])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [trend TO (2)]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[sum:Calculation_1813824758949527643:qk] + [Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Calculation_1813824758949527643:qk:4])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:Calculation_1813824758949527643:qk] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:Calculation_1813824758949527643:qk:4])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [trend TO LC]
     Rows shelf modified:
       Old: ([Grouped External Sales 2.0 (local copy) (copy)].[sum:Turnover:qk] + [Grouped External Sales 2.0 (local copy) (copy)].[win:sum:Turnover:qk:4])
       New: ([federated.07pdzlx0k2seif18uh2zd1jwbeij].[sum:turnover:qk] + [federated.07pdzlx0k2seif18uh2zd1jwbeij].[win:sum:turnover:qk:2])
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]
 [*] MODIFIED WORKSHEET: [trend margin %]
     Rows shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[usr:Margin % CY (copy)_245164742006915078:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[usr:Margin % CY (copy)_245164742006915078:qk]
     Cols shelf modified:
       Old: [Grouped External Sales 2.0 (local copy) (copy)].[tmn:InvoiceDate:qk]
       New: [federated.07pdzlx0k2seif18uh2zd1jwbeij].[tmn:invoice_date:qk]

--- LAYER 5: DASHBOARDS (Added: 0, Removed: 0, Modified: 1) ---
 [*] MODIFIED DASHBOARD: [Landing Page]
     Contained worksheets modified:
       Old: ['OL vs budget', 'TO daily vs LY ', 'TO measures (4)', 'TO vs LY', 'TO vs budget', 'Volume measures (3)', '__LastDataUpdate (2)', 'commerce score', 'daily OL vs ly', 'map - TO Δ% vs budget', 'map - margin Δ% vs budget', 'margin measures (3)', 'margin% vs LY', 'margin% vs budget', 'time labels (2)']
       New: ['OL vs budget', 'TO daily vs LY ', 'TO measures (4)', 'TO vs LY', 'TO vs budget', 'Volume measures (3)', '__LastDataUpdate (2)', 'commerce score', 'daily OL vs ly', 'map - TO delta% vs budget 2.0', 'map - margin Δ% vs budget', 'margin measures (3)', 'margin% vs LY', 'margin% vs budget', 'time labels (2)']

--- LAYER 6: DASHBOARD ACTIONS (Added: 0, Removed: 0, Modified: 0) ---

================================================================================
```
