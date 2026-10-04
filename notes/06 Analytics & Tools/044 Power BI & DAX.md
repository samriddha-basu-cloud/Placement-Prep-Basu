---
tags: [analytics-tools, tier1]
area: Analytics & Tools
topic: "Power BI & DAX"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 11
---
# Power BI & DAX

⬅ [[043 Advanced Excel (Pivot, Solver, Forecasting)]] · [[_Index - Analytics & Tools|Analytics & Tools]] · [[045 SQL for Operations Analytics]] ➡

> **Area:** Analytics & Tools · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Power BI Architecture]]
2. [[#2. Power Query (M Language)]]
3. [[#3. Data Modeling]]
4. [[#4. DAX Basics]]
5. [[#5. DAX Time Intelligence]]
6. [[#6. DAX Filter Functions]]
7. [[#7. KPI Visuals]]
8. [[#8. Slicers & Interactions]]
9. [[#9. Row-Level Security (RLS)]]
10. [[#10. Power BI Service & Workspaces]]
11. [[#11. ⭐ Advanced: Performance Tuning, Calculation Groups and Incremental Refresh]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Power BI folds into Microsoft Fabric
> **Fabric app development opens to Power BI users (29 Sep 2026).** The Register reports Microsoft is extending Fabric app-development capabilities to Power BI Pro and Premium Per User licensees at no extra cost, with an open-source SDK called Rayfin to build data apps with AI coding agents (preview "in the coming weeks"). Figures quoted: about **425,000 Power BI customers**, **35 million+ monthly Power BI business users** and **40,000 Fabric customers**; each app gets a 1 GB Fabric SQL database. ([The Register](https://www.theregister.com/applications/2026/09/29/redmond-to-millions-of-power-bi-users-youre-fabric-app-devs-now/5299552))
>
> Read this as: Power BI is no longer just a report tool; it is the front end of a wider data platform (Fabric), so semantic-model, governance and workspace design skills matter more than chart skills.
>
> Sub-topics that say **"See news box"** reuse this item.

---
## 1. Power BI Architecture
> 🔴 Tier 1 · _Tracker hint:_ Data source → Power Query → Data Model → Report → Service

### Definition
Power BI's flow:
1. **Data sources:** Excel, CSV, SQL Server, SAP HANA/BW, SharePoint, APIs, cloud (Azure, Snowflake), 100+ connectors.
2. **Power Query (Get Data / Transform):** extract and shape; steps recorded in the **M language**.
3. **Data Model (VertiPaq in-memory columnar engine):** tables, relationships, **DAX** measures; compressed for speed.
4. **Report (Power BI Desktop):** visuals, slicers, pages, bookmarks.
5. **Power BI Service (app.powerbi.com):** publish to workspaces, dashboards, apps, scheduled refresh, sharing, RLS, subscriptions; **gateway** to reach on-premises data. **Mobile** app for consumption.

**Storage modes:** **Import** (data loaded into the model: fastest, scheduled refresh), **DirectQuery** (queries sent to the source live: fresh but slower, limited DAX), **Live Connection** (to an existing semantic model / Analysis Services), **Composite** (mix) and **Direct Lake** in Fabric. Terminology: "dataset" is now called a **semantic model**.

Components: Desktop (author, free), Service (share, license: Pro, Premium Per User, Fabric capacity), Report Server (on-premises). A **report** has pages of visuals; a **dashboard** (Service only) pins tiles from many reports.

### Example
A 3PL loads shipment data from SQL Server (Import), cleans dates in Power Query, relates shipments to a Date table and Customer table, writes measures (OTIF %), builds a 3-page report, publishes to a "Logistics Ops" workspace, and schedules refresh at 06:00 IST through an on-premises gateway.

### In the news
See news box. Power BI's architecture is now part of Fabric: the same semantic model can feed reports, notebooks and apps, so model quality is the leverage point.

### Interview angle
> [!question] How it is asked
> "Explain the Power BI workflow end to end." "Import vs DirectQuery: when would you use which?"

> [!tip] Strong answer includes
> - The five-step flow and what is done where (Desktop vs Service)
> - Import (default, fast) vs DirectQuery (real-time, big data) trade-off
> - Gateway for on-premises refresh
> - Report vs dashboard vs app vs semantic model

---

## 2. Power Query (M Language)
> 🔴 Tier 1 · _Tracker hint:_ Data transformation: merge, append, pivot, unpivot, clean

### Definition
**Power Query Editor** (Home, Transform Data) records each transformation as an **Applied Step** written in **M**. Steps are repeated at every refresh, so the cleaning is reproducible.

Common transformations:
- **Clean:** remove duplicates/blank rows/errors, trim, fix types, replace values, split and extract text, fill down.
- **Merge Queries** = join (Left Outer, Inner, Full Outer, Anti), **Append Queries** = stack tables (UNION ALL).
- **Pivot** (rows to columns) and **Unpivot** (columns to rows; turn "Jan, Feb, Mar" columns into Month and Value).
- **Group By**, add custom/conditional/index columns, parameters, functions, folder-combine.
- **Query folding:** when steps are translated to SQL and run at the source (faster); order steps so foldable ones come first.

M basics:
```
let
    Source  = Csv.Document(File.Contents("C:\data\orders.csv"), [Delimiter=",", Encoding=65001]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed   = Table.TransformColumnTypes(Promoted, {{"Qty", Int64.Type}, {"Date", type date}}),
    Filtered = Table.SelectRows(Typed, each [Qty] > 0)
in
    Filtered
```
M is case sensitive; the last expression after `in` is the output.

### Example
Plant sends a sheet with columns "Jan-26, Feb-26, Mar-26" of demand per SKU. Select the SKU column, right-click, **Unpivot Other Columns**: you get SKU, Month, Demand (long format), ready for a pivot and for time intelligence. Append the three plant files from a folder, then Merge with the SKU master (Left Outer on SKU) to bring in category.

### In the news
See news box. Power Query skills transfer: the same engine runs in Excel, Power BI and Fabric dataflows.

### Interview angle
> [!question] How it is asked
> "How would you consolidate 12 monthly files with inconsistent columns?" "Merge vs Append?"

> [!tip] Strong answer includes
> - Merge = join (columns), Append = union (rows)
> - Unpivot to get tidy data for analysis
> - Do cleaning in Power Query, measures in DAX
> - Query folding and keeping steps minimal and named

---

## 3. Data Modeling
> 🔴 Tier 1 · _Tracker hint:_ Star schema, snowflake; relationships; cardinality; bi-directional

### Definition
A good model is a **star schema**: one central **fact table** (transactions with measures and foreign keys: Sales, Shipments) surrounded by **dimension tables** (Date, Product, Customer, Location) that describe and filter. A **snowflake** normalises dimensions further (Product to Subcategory to Category): more joins, smaller storage, slower and harder for users. Power BI favours star.

**Relationships:** one-to-many (dimension to fact, filter flows from "one" side to "many" side), many-to-one, one-to-one, many-to-many (use sparingly; bridge table). **Cross-filter direction:** single (default) or **both** (bi-directional); bi-directional can cause ambiguity and slow queries, so use only when needed (for example slicers on a dimension filtered by another dimension, or with RLS). One **active** relationship between two tables; others inactive, activated by `USERELATIONSHIP` in DAX (for example Order Date vs Ship Date).

Best practices: a **dedicated Date table** (marked as date table), unique keys, hide foreign keys, avoid wide flat tables, avoid calculated columns when a measure will do, set data types and formats.

### Example
Fact_Shipments (ShipID, DateKey, ProductKey, CustomerKey, Qty, Freight) linked many-to-one to Dim_Date, Dim_Product, Dim_Customer. Ship Date and Delivery Date both link to Dim_Date: one active (Ship Date), one inactive; the measure `Delivered Qty = CALCULATE(SUM(Fact_Shipments[Qty]), USERELATIONSHIP(Fact_Shipments[DeliveryDateKey], Dim_Date[DateKey]))` uses the second.

### In the news
See news box. As semantic models become shared assets across Fabric apps, a clean star schema with one date table is the difference between a model people trust and one nobody can reuse.

### Interview angle
> [!question] How it is asked
> "What is a star schema and why does Power BI prefer it?" "When would you use a bi-directional relationship?"

> [!tip] Strong answer includes
> - Fact vs dimension; one-to-many filter flow
> - Star vs snowflake trade-off
> - Role-playing dates with inactive relationships and USERELATIONSHIP
> - Bi-directional only with care; avoid many-to-many

---

## 4. DAX Basics
> 🔴 Tier 1 · _Tracker hint:_ Calculated columns vs measures; SUM, COUNT, AVERAGE, IF

### Definition
**DAX** (Data Analysis Expressions) is the formula language of the model.

| | Calculated column | Measure |
|---|---|---|
| Evaluated | Row by row at refresh (**row context**) | On the fly, per visual cell (**filter context**) |
| Stored | Yes (uses memory) | No |
| Use for | Slicing/grouping attributes, relationships | Aggregations, KPIs, ratios |

```
Total Sales = SUM(Sales[Amount])
Orders = COUNTROWS(Sales)
Distinct Customers = DISTINCTCOUNT(Sales[CustomerID])
Avg Order Value = DIVIDE([Total Sales], [Orders])            -- safe divide, no #DIV/0
Margin % = DIVIDE([Total Sales] - [Total Cost], [Total Sales])
Stock Status = IF(Inventory[OnHand] < Inventory[ReorderPoint], "Reorder", "OK")   -- calculated column
```
Iterators (`SUMX`, `AVERAGEX`) calculate row-wise then aggregate: `Revenue = SUMX(Sales, Sales[Qty] * Sales[Price])`. Variables improve readability and speed: `VAR x = ... RETURN ...`. **Filter context** (slicers, rows, columns, filters) determines what a measure sees; **row context** exists in calculated columns and iterators; `CALCULATE` converts row context to filter context (context transition).

### Example
A matrix with Region in rows shows `[Total Sales]` per region without writing separate formulas: the same measure re-evaluates in each region's filter context. If Sales has 1,000 orders and Total Sales = Rs 5,00,000, `Avg Order Value` = 500; the measure at Region = West might be 24 orders and Rs 15,600, so 650.

### In the news
See news box. Measures live in the semantic model and are reused by every report and app built on it; define them once and certify the model.

### Interview angle
> [!question] How it is asked
> "Calculated column vs measure?" "Write a measure for on-time delivery percentage."

> [!tip] Strong answer includes
> - Row context vs filter context
> - Prefer measures; calculated columns only for slicing attributes
> - DIVIDE, variables, iterators (SUMX)
> - Example measure: `OTD % = DIVIDE(CALCULATE(COUNTROWS(Orders), Orders[OnTime] = TRUE()), COUNTROWS(Orders))`

---

## 5. DAX Time Intelligence
> 🔴 Tier 1 · _Tracker hint:_ TOTALYTD, SAMEPERIODLASTYEAR, DATEADD, DATESYTD

### Definition
Time intelligence needs a **contiguous Date table** (every date, no gaps) related to the fact and **marked as a date table**.

```
Sales YTD       = TOTALYTD([Total Sales], 'Date'[Date])
Sales FY YTD    = TOTALYTD([Total Sales], 'Date'[Date], "3/31")        -- Indian FY ending 31 March
Sales YTD (alt) = CALCULATE([Total Sales], DATESYTD('Date'[Date]))
Sales LY        = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
Sales PM        = CALCULATE([Total Sales], DATEADD('Date'[Date], -1, MONTH))
YoY %           = DIVIDE([Total Sales] - [Sales LY], [Sales LY])
Rolling 3M      = CALCULATE([Total Sales], DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -3, MONTH))
```
Other functions: `TOTALMTD`, `TOTALQTD`, `DATESBETWEEN`, `PARALLELPERIOD`, `PREVIOUSMONTH`, `ENDOFMONTH`. Create the Date table with `CALENDAR` or `CALENDARAUTO`, add Year, Quarter, Month, FY columns. Use the same Date table for all facts. Sort Month Name by Month Number.

### Example
Monthly sales: Mar 2025 = Rs 80 lakh, Mar 2026 = Rs 92 lakh. `Sales LY` in Mar 2026 = 80; YoY % = (92 - 80)/80 = **15%**. FY YTD with year-end "3/31": in Oct 2026 it sums 1 Apr 2026 to 31 Oct 2026, matching how Indian companies report.

### In the news
See news box. Time-intelligence logic is a reason to centralise the date table in a shared model instead of each app re-inventing fiscal calendars.

### Interview angle
> [!question] How it is asked
> "How do you calculate YoY growth in Power BI?" "Why does SAMEPERIODLASTYEAR give blanks?"

> [!tip] Strong answer includes
> - Dedicated, complete, marked Date table
> - The function set and the Indian fiscal year parameter
> - Blanks arise from gaps in the Date table or using the fact table's date column
> - Compute growth with DIVIDE and handle blank prior year

---

## 6. DAX Filter Functions
> 🔴 Tier 1 · _Tracker hint:_ CALCULATE, ALL, ALLEXCEPT, FILTER, VALUES, EARLIER

### Definition
**CALCULATE(expression, filter1, filter2, ...)** evaluates an expression in a **modified filter context**. It is the most important DAX function.

```
Sales North     = CALCULATE([Total Sales], Sales[Region] = "North")
Sales All Reg   = CALCULATE([Total Sales], ALL(Sales[Region]))            -- remove region filter
% of Total      = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Sales)))
% of Region     = DIVIDE([Total Sales], CALCULATE([Total Sales], ALLEXCEPT(Sales, Sales[Region])))
Big Orders      = CALCULATE([Total Sales], FILTER(Sales, Sales[Amount] > 100000))
Selected Region = IF(HASONEVALUE(Sales[Region]), VALUES(Sales[Region]), "Multiple")
```
- **ALL** removes filters; **ALLEXCEPT** removes all except named columns; **ALLSELECTED** respects slicer selection but removes visual-level filters.
- **FILTER(table, condition)** is an iterator returning a filtered table (more flexible, slower than a simple Boolean filter).
- **VALUES** returns the distinct values currently in context (a one-column table); **SELECTEDVALUE** gets a single value.
- **EARLIER** refers to an outer row context in nested calculated columns (for example rank); modern DAX prefers variables: `VAR cur = Sales[Amount] RETURN COUNTROWS(FILTER(Sales, Sales[Amount] > cur)) + 1`.
- `KEEPFILTERS`, `REMOVEFILTERS` (clearer alias for ALL inside CALCULATE).

### Example
A matrix has Region rows. Total Sales: North 40, South 30, East 20, West 10 (Rs lakh), total 100. `% of Total` = North 40/100 = **40%**, South 30%, East 20%, West 10%; all rows share the denominator because `ALL(Sales)` removes the region filter. If a Region slicer selects North and South only, `ALLSELECTED` would give North 40/70 = 57.1%.

### In the news
See news box. These filter-context skills decide whether a shared model's KPIs, such as share of total and rolling comparison, stay correct under any slicer a user picks.

### Interview angle
> [!question] How it is asked
> "Explain CALCULATE and filter context." "How do you compute percent of total?"

> [!tip] Strong answer includes
> - CALCULATE modifies filter context; ALL/ALLEXCEPT/ALLSELECTED differences
> - Percent-of-total measure with the denominator logic
> - Row context vs filter context; context transition
> - EARLIER is legacy; use VAR

---

## 7. KPI Visuals
> 🔴 Tier 1 · _Tracker hint:_ Card, gauge, KPI indicator; conditional formatting; RAG status

### Definition
- **Card / multi-row card:** a single number (Total Sales, OTIF %).
- **KPI visual:** value, trend axis (time) and **target**, with good/bad colouring and a goal comparison.
- **Gauge:** progress to a target (min, max, target); use sparingly: space-hungry, hard to compare.
- **Others:** bar and line for trend, matrix with conditional-formatting data bars, icons, **sparklines** in tables, waterfall for bridges, decomposition tree, scatter for ABC/XYZ.
- **Conditional formatting** (background colour, font colour, data bars, icons) by rules, colour scales, or by a **field value** from a DAX measure that returns a hex colour. 
- **RAG status** (Red/Amber/Green) from thresholds:
```
OTIF RAG = SWITCH(TRUE(), [OTIF %] >= 0.95, "Green", [OTIF %] >= 0.90, "Amber", "Red")
```
Design: show value, target, variance, and trend; consistent number formats; colour-blind-safe palettes (not red-green only: add icons/arrows); limit KPIs to the few that drive decisions.

### Example
Warehouse page: cards for OTIF % (target 95%), Order Cycle Time, Inventory Days; KPI visual for monthly OTIF versus target; table of depots with a data bar for backlog and an icon for RAG. A depot at 92% OTIF shows Amber, since 90% <= 92% < 95%.

### In the news
See news box. As reports become interfaces for apps and agents, clear KPI definitions (one certified measure per KPI) matter more than decoration.

### Interview angle
> [!question] How it is asked
> "How would you design an operations KPI dashboard in Power BI?"

> [!tip] Strong answer includes
> - Audience and decisions first; 4 to 6 headline KPIs with targets
> - KPI visual vs card vs gauge (and why gauges are weak)
> - RAG logic from a measure; accessibility beyond colour
> - Drill path from KPI to cause (region, SKU, lane)

---

## 8. Slicers & Interactions
> 🔴 Tier 1 · _Tracker hint:_ Sync slicers, cross-filter vs cross-highlight; drill-through

### Definition
- **Slicers:** on-canvas filters (list, dropdown, between, relative date). **Sync slicers** (View, Sync slicers) apply one slicer across selected pages.
- **Visual interactions** (Format, Edit interactions): a selection in one visual can **cross-filter** (other visuals show only the selected data), **cross-highlight** (others show the full data with the selection highlighted, so you see share), or have **no impact**.
- **Drill-down/up** moves through a hierarchy within a visual (Year, Quarter, Month); **drill-through** sends the user to a detail page filtered to the selected item (right-click); **tooltips pages** show a mini-visual on hover; **bookmarks** and buttons save view states for navigation; **field parameters** let the user switch measures/dimensions.
- **Filter pane** levels: visual, page, report; filters can be locked/hidden. Slicers on a many-to-one dimension filter facts, not the other way, unless the relationship is bi-directional.

### Example
A supply-chain report has a Region slicer synced across Overview and Supplier pages. Clicking "Pune" in a bar chart cross-filters the table to Pune only while a donut uses cross-highlight to show Pune's share of total. Right-click a supplier, **Drill through** to a "Supplier Detail" page showing its OTIF trend and late POs.

### In the news
See news box. As apps built on Power BI models spread, interaction design (clear defaults, a reset button, limited slicers) is part of governance.

### Interview angle
> [!question] How it is asked
> "Cross-filter vs cross-highlight?" "How would you let a manager drill from a KPI to the underlying orders?"

> [!tip] Strong answer includes
> - Definitions with an example for each
> - Sync slicers vs page-level filters
> - Drill-through and tooltips for detail without clutter
> - Performance: too many slicers/visuals slow reports

---

## 9. Row-Level Security (RLS)
> 🔴 Tier 1 · _Tracker hint:_ Static vs dynamic RLS; role assignment in Power BI Service

### Definition
**RLS** restricts the data rows a user can see, based on roles with **DAX filter expressions** on tables. It works on Import and DirectQuery models.

- **Static RLS:** one role per fixed filter, e.g. role "North" with `[Region] = "North"` on the Region table; users are added to the matching role. Simple, but many roles to maintain.
- **Dynamic RLS:** one role; filter uses the logged-in user: `[ManagerEmail] = USERPRINCIPALNAME()` on a security table related to the data (or `USERNAME()`). Scales to hundreds of users via a mapping table.

Steps: Desktop, Modeling, Manage roles, define the DAX filter, **View as** to test; publish; in the Service open the semantic model, **Security**, add users or groups to roles. Notes: RLS applies to Viewers, not to workspace Admin/Member/Contributor roles who can edit content (they bypass it); RLS is not applied in Desktop to the author; **Object-level security (OLS)** hides tables/columns; use security groups and test with a non-owner account.

### Example
Table `Security(Email, Region)`. Role "RegionalManagers" on Security: `[Email] = USERPRINCIPALNAME()`, with a relationship from Security[Region] to Region[Region] so the filter reaches Sales (enable "Apply security filter in both directions" on that relationship if it must flow the other way). Priya@company.in sees only West data; the Pune and Mumbai depots are West, so her totals show only those. Add one row to the mapping table when a manager changes; no new role needed.

### In the news
See news box. As more apps are built on the same semantic model, access control must live in the model (RLS) and the workspace, so one rule governs every report and app.

### Interview angle
> [!question] How it is asked
> "How would you make sure each regional manager sees only their own region?"

> [!tip] Strong answer includes
> - Dynamic RLS with a mapping table and USERPRINCIPALNAME()
> - Role assignment in the Service and testing with View as
> - Workspace role bypass caveat (Admin/Member/Contributor)
> - Alternatives: separate reports (poor scale), OLS for columns

---

## 10. Power BI Service & Workspaces
> 🔴 Tier 1 · _Tracker hint:_ Publishing, sharing, scheduled refresh, apps, gateways

### Definition
The **Power BI Service** is the cloud site for sharing and governing content.
- **Workspaces:** collaboration containers for semantic models, reports, dashboards. **Roles:** Admin, Member, Contributor, Viewer. Typical pattern: Dev, Test, Prod workspaces with **deployment pipelines**.
- **Publish** from Desktop to a workspace; **Apps** package content for wide audiences (read-only, one link, audience groups). Sharing options: direct share link, app, embed, email subscriptions, Teams/SharePoint embedding. Licences: **Free**, **Pro** (per user; both sharer and consumer need Pro unless content is in Premium/Fabric capacity), **Premium Per User**, **Fabric/Premium capacity** (free viewers on higher SKUs).
- **Scheduled refresh** (Import models): up to 8 times a day on Pro and 48 on Premium (check current limits); needs credentials; **gateway** (on-premises data gateway, standard mode; personal mode is for one user) for on-premises sources; **incremental refresh** loads only new/changed partitions.
- **Governance:** sensitivity labels, endorsement (certified, promoted), lineage view, usage metrics, data alerts on dashboard tiles, row-level security, tenant settings.

### Example
A team builds the logistics report in Desktop, publishes to "Logistics-Prod", connects the semantic model to an on-premises SQL Server via a gateway, sets refresh at 06:00 and 14:00 IST, and publishes an **app** for regional heads with RLS, rather than sharing individual reports to 200 people.

### In the news
See news box. With Power BI sitting inside Fabric (425,000 customers, 35 million+ monthly users per the report), workspace roles, capacity and endorsements are central to how large organisations manage this scale.

### Interview angle
> [!question] How it is asked
> "How do you share a report with 200 users and keep it refreshed from on-prem data?"

> [!tip] Strong answer includes
> - Workspace and app model; roles and licences
> - Gateway plus scheduled/incremental refresh
> - Dev/Test/Prod deployment, certified datasets, RLS
> - Monitoring refresh failures and usage

---

## 11. ⭐ Advanced: Performance Tuning, Calculation Groups and Incremental Refresh
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Performance:** reduce model size and visual count; remove unused columns, avoid high-cardinality columns (timestamps to separate date and time), prefer measures, replace bi-directional filters and many-to-many, use variables in DAX, aggregate tables, and **Import** over DirectQuery unless needed. Tools: **Performance Analyzer** (Desktop), **DAX Studio**, **Tabular Editor**, VertiPaq Analyzer. Query folding in Power Query pushes work to the source.

**Calculation groups** (Tabular Editor) apply the same logic (YTD, LY, YoY) to many measures without duplicating DAX. **Incremental refresh** partitions a large fact table by date using `RangeStart`/`RangeEnd` parameters, refreshing only recent partitions. **Aggregations** pre-summarise huge DirectQuery tables. **Field parameters** let users choose a measure. **Deployment pipelines** and Git integration for version control. **Semantic model best practice:** one certified model, many thin reports.

### Example
A 50-million-row shipment table takes 40 minutes to refresh. Set `RangeStart/RangeEnd`, keep 3 years, refresh only the last 7 days: refresh drops to a few minutes. Replacing a datetime column (millions of unique values) with Date plus a separate Time-of-day (1,440 values) cuts memory sharply (columnar compression depends on cardinality).

### In the news
See news box. As the semantic model becomes the shared backbone for reports and apps in Fabric, a slow or inconsistent model hurts every consumer at once.

### Interview angle
> [!question] How it is asked
> "A report is slow. How do you diagnose and fix it?"

> [!tip] Strong answer includes
> - Performance Analyzer to find the slow visual and DAX Studio for the query
> - Model fixes (cardinality, star schema, remove columns), DAX fixes (variables, avoid FILTER over big tables)
> - Incremental refresh and aggregations for scale
> - Governance: one certified model, thin reports

---
## 🔗 Go deeper: expansion notes
- [[172 Tableau & Looker Studio - BI Tool Comparison|Tableau & Looker Studio - BI Tool Comparison]]
