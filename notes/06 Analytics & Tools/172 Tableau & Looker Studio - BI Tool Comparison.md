---
tags: [analytics-tools, tier2]
area: Analytics & Tools
topic: "Tableau & Looker Studio - BI Tool Comparison"
tier: Tier 2
roles: Operations / PM / Consulting
status: complete
subtopics: 13
---
# Tableau & Looker Studio - BI Tool Comparison

⬅ [[047 MIS & Dashboard Design]] · [[_Index - Analytics & Tools|Analytics & Tools]] · [[173 Process Mining & Operations Intelligence]] ➡

> **Area:** Analytics & Tools · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / PM / Consulting

## Sub-topics in this note
1. [[#1. Tableau Architecture, Products and Data Connection]]
2. [[#2. Dimensions, Measures and Field Types]]
3. [[#3. Calculated Fields and Parameters]]
4. [[#4. Level of Detail (LOD) Expressions]]
5. [[#5. Table Calculations]]
6. [[#6. Dashboards, Actions and Interactivity]]
7. [[#7. Looker Studio (Data Studio) Basics]]
8. [[#8. Looker Studio Blends, Joins and Limits]]
9. [[#9. Decision Grid: Power BI vs Tableau vs Looker Studio vs Excel]]
10. [[#10. Choosing the Right Chart for Operations KPIs]]
11. [[#11. Interview-Style Dashboard Questions and KPI Traps]]
12. [[#12. Performance, Security and Governance Tips]]
13. [[#13. ⭐ Advanced: Semantic Layers, Looker (LookML) and AI-Assisted Analytics]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): BI tools are renaming, repricing and adding AI agents
> **Looker Studio is now "Data Studio" again (16 April 2026).** Google's release notes record that Looker Studio was rebranded as Data Studio on 16 April 2026, with a new home page that also reaches BigQuery conversational agents and Colab data apps; "Gemini in Looker" became "Gemini in Data Studio". The same notes list 40+ new partner connectors between March and September 2026 (Facebook Ads, Salesforce, Shopify, LinkedIn Ads and others) and Pro-only security features (customer-managed encryption keys, data residency) from 11 June 2026. Google describes the core product as no-cost, with a paid Pro tier. This note uses "Looker Studio" because most interview material and job descriptions still do. ([Google Cloud release notes](https://docs.cloud.google.com/data-studio/release-notes), [overview](https://docs.cloud.google.com/data-studio/welcome))
>
> **Power BI price rise (1 April 2025).** Microsoft raised Power BI Pro to **$14 per user per month** and Premium Per User to **$24**, the first change in nearly 10 years, applying to new commercial customers at once and to existing customers at renewal. ([Microsoft Fabric community blog](https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/important-update-to-microsoft-power-bi-pricing/5174341))
>
> **Tableau Next (15 April 2025).** Salesforce announced Tableau Next, an agentic analytics platform built on the Salesforce Platform and Data Cloud, with a semantic layer (Tableau Semantics), a natural-language "Concierge" and an anomaly-watching "Inspector". The Tableau Cloud price page checked in this session listed **Standard at $15 and Enterprise at $35 per user per month** (billed annually), with Creator, Explorer and Viewer license types. Prices and edition names change, so verify before quoting. ([Salesforce](https://www.salesforce.com/news/stories/tableau-next-announcement/), [Tableau pricing](https://www.tableau.com/pricing/teams-orgs))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Tableau Architecture, Products and Data Connection
> 🟠 Tier 2 · _Key points:_ Desktop, Prep, Cloud/Server, Public; live vs extract; relationships vs joins vs blends

### Definition
**Tableau** is a visual analytics platform (owned by Salesforce) built on drag-and-drop VizQL: dragging fields to shelves generates queries and marks. Main products:
- **Tableau Desktop** (authoring) and web authoring in the browser.
- **Tableau Prep Builder** (cleaning, joining, pivoting flows).
- **Tableau Cloud** (hosted) and **Tableau Server** (self-hosted) for publishing, permissions, subscriptions and alerts.
- **Tableau Public** (free, public sharing only) for portfolios.
- **Tableau Pulse** and **Tableau Next** for AI-driven metrics and agents.

**Connection modes:**

| Mode | What happens | Use when |
|---|---|---|
| **Live** | Every interaction queries the source | Fresh data, strong database, small result sets |
| **Extract (.hyper)** | Compressed columnar snapshot on a refresh schedule | Slow sources, big data, offline use; usually much faster |

**Combining data:** **relationships** (logical layer: tables stay separate and are joined at query time based on the fields in the view, avoiding duplicated measures), **joins** (physical layer, row-level; inner, left, right, full outer), **unions** (stack same-structure files) and legacy **data blending** (primary and secondary sources linked on a field, aggregated before combining). Prefer relationships for different grain tables (orders and returns); use joins when you need a single flat table.

Tableau vs the rest of the Tableau family in an interview: Desktop creates, Prep prepares, Server/Cloud governs and shares.

### Example
An operations team connects three CSV extracts: Orders (one row per order line), Shipments (one row per shipment), Returns (one row per return). A join on Order ID would duplicate order lines wherever an order has several shipments and inflate sales. With relationships on Order ID, Tableau aggregates each table at the right grain and the sales total stays correct. The workbook uses an extract refreshed every night at 2 a.m., so planners get instant filters during the day.

### In the news
See news box. Tableau's move to Tableau Next with a semantic layer shows that the real battle is moving from drawing charts to governing consistent metric definitions.

### Interview angle
> [!question] How it is asked
> "What is the difference between live and extract connections in Tableau, and when would you use each?"

> [!tip] Strong answer includes
> - Live for freshness and powerful databases; extract (Hyper) for speed and offline use with scheduled refresh
> - Relationships vs joins vs blends, with the "fan-out duplicates measures" risk
> - Desktop to Cloud/Server publishing path with permissions
> - Cost of extracts: staleness and refresh windows

---
## 2. Dimensions, Measures and Field Types
> 🟠 Tier 2 · _Key points:_ Dimension vs measure, discrete (blue) vs continuous (green), aggregation, data roles

### Definition
- **Dimension:** qualitative field that slices data (Region, Warehouse, Product, Date as a category). Creates headers when placed on Rows/Columns.
- **Measure:** quantitative field that is aggregated (Sales, Units, Lead time). Creates axes.
- **Discrete (blue pill):** distinct individual values, draws headers. **Continuous (green pill):** unbroken range, draws an axis. Dates can be either: **discrete month** gives separate month labels; **continuous month** gives a continuous timeline.
- **Aggregation:** SUM, AVG, MEDIAN, COUNTD (distinct count), MIN, MAX. Disaggregating (Analysis menu) shows one mark per row.
- **Data types:** string, number, date, date-time, boolean, geographic role.
- **Sets, groups, bins, hierarchies and parameters:** sets (in or out of a condition), groups (combine members), bins (fixed-size buckets of a measure such as lead time in 2-day bins), hierarchies (drill-down), parameters (user-controlled values).

A common point of confusion: a number can be a dimension (Store ID) and a text field cannot be a measure (except via COUNT).

### Example
Lead-time analysis: drag **Warehouse** (dimension) to Rows and **AVG(Lead Time Days)** (measure) to Columns for a bar chart. Convert Order Date to **continuous month** to get a line of average lead time across months. Create bins of Lead Time of size 2 and drag **COUNT(Order ID)** to see a histogram. A parameter "Target Days" feeds a reference line.

### In the news
See news box. Both Tableau Pulse and Gemini in Data Studio rely on the metric (measure) definitions you set up; poor dimension and measure hygiene gives poor AI answers too.

### Interview angle
> [!question] How it is asked
> "What are dimensions and measures, and what do blue and green pills mean?"

> [!tip] Strong answer includes
> - Dimension slices; measure is aggregated; discrete makes headers; continuous makes axes
> - Example with date discrete vs continuous
> - Mentions COUNTD for distinct counts and bins for histograms
> - Notes that a numeric field can be a dimension

---
## 3. Calculated Fields and Parameters
> 🟠 Tier 2 · _Key points:_ Row-level vs aggregate calcs; IF/CASE; DATEDIFF; ratio of sums; parameters

### Definition
A **calculated field** is a formula built on existing fields. Types:
- **Row-level** (evaluated for every row): `DATEDIFF('day',[Order Date],[Ship Date])`, `IF [Delivered Date] > [Promised Date] THEN 1 ELSE 0 END`.
- **Aggregate** (evaluated after aggregation): `SUM([On Time]) / SUM([Orders])`.
- **Table calculations** (on the aggregated result in the view; see the table calculation sub-topic).
- **LOD expressions** (aggregate at a defined level; see the next sub-topic).

Function families: logical (IF, IIF, CASE, ISNULL, ZN), string (LEFT, CONTAINS, SPLIT), date (DATEADD, DATETRUNC, DATEDIFF, TODAY), number (ROUND, ABS), type conversion (STR, FLOAT, DATE), aggregate (SUM, AVG, COUNTD, ATTR), user (USERNAME(), ISMEMBEROF() for security).

A **parameter** is a workbook variable that the viewer controls (list, range, free text) and calculations read: "Select KPI" (swap the measure), "Top N" and "Target %".

**Order of operations** (important for filters): extract filters, data-source filters, context filters, **FIXED LOD**, dimension filters, INCLUDE/EXCLUDE LOD, measure filters, table calcs. Dimension filters do not affect a FIXED LOD unless converted to context filters.

**Golden rule for KPIs:** use a **ratio of sums**, not an average of row ratios.

### Example
Three warehouses with orders and on-time orders: WH1 1,000 orders, 900 on time (90%); WH2 200, 140 (70%); WH3 100, 60 (60%). The correct network on-time rate = (900 + 140 + 60) / (1,000 + 200 + 100) = 1,100 / 1,300 = **84.6%**. Averaging the three percentages gives (90 + 70 + 60) / 3 = **73.3%**, a 11.3 point error that understates a network dominated by the strongest warehouse. In Tableau: `OTIF % = SUM([On Time]) / SUM([Orders])` (aggregate calculation), formatted as a percentage.

### In the news
See news box. The AI layers (Tableau Pulse, Gemini in Data Studio) generate calculated fields from natural language, but a reviewer still needs to catch an average-of-ratios error like the one above.

### Interview angle
> [!question] How it is asked
> "Your OTIF dashboard shows 73% but finance says 85%. What could be wrong?"

> [!tip] Strong answer includes
> - Average of ratios vs ratio of sums; weighting by volume
> - Filter or join duplication, grain mismatch, different definitions of "on time"
> - Reconciling to source with a pivot, then fixing the calculation and documenting the KPI definition
> - Order of operations as another source of surprise

---
## 4. Level of Detail (LOD) Expressions
> 🟠 Tier 2 · _Key points:_ FIXED, INCLUDE, EXCLUDE; syntax; cohort, percent-of-total, customer-level averages

### Definition
**LOD expressions** compute an aggregate at a level different from the view's level of detail. Syntax (as in Tableau's documentation):

`{[FIXED | INCLUDE | EXCLUDE] <dimension declaration> : <aggregate expression>}`

- **FIXED:** uses only the dimensions listed, regardless of the view. `{ FIXED [Region] : SUM([Sales]) }`.
- **INCLUDE:** the listed dimensions in addition to the view's. `{ INCLUDE [Customer Name] : SUM([Sales]) }`.
- **EXCLUDE:** removes listed dimensions from the view's level. `{ EXCLUDE [Region] : SUM([Sales]) }`.

A `FIXED` expression with no dimension (`{ SUM([Sales]) }`) returns the grand total. FIXED calculations are computed before dimension filters (unless those are context filters); INCLUDE and EXCLUDE respect them. LODs can be used inside other calculations and as dimensions (FIXED results can be used as a dimension, for instance to bin customers by lifetime sales).

Typical uses: **percent of total**, **cohort analysis** (`{ FIXED [Customer] : MIN([Order Date]) }` for first order date), **customer-level metrics inside a region view**, comparing a value with a group average, and "customers with only one order".

### Example
Data (₹ lakh): North C1 40, C1 20, C2 50, C3 30; South C4 60, C4 10, C5 30; West C6 45, C7 25. Total = 310. In a view with Region and Customer:
- `{ FIXED [Region] : SUM([Sales]) }` = North 140, South 100, West 70, repeated against every customer of the region.
- **Share of region total** per customer: `SUM([Sales]) / SUM({ FIXED [Region] : SUM([Sales]) })`. C1 = 60 / 140 = 42.9%.
- **Region share of the whole**: `SUM({ FIXED [Region] : SUM([Sales]) }) / SUM({ FIXED : SUM([Sales]) })`; North = 140 / 310 = 45.2%, South 32.3%, West 22.6%.
- **Average sales per customer in each region** (view = Region only): `AVG({ INCLUDE [Customer] : SUM([Sales]) })` gives North 46.7, South 50.0, West 35.0. The plain `AVG([Sales])` per row gives 35.0, 33.3 and 35.0: different because it averages order lines, not customers.
- **First purchase month for cohorts:** `{ FIXED [Customer] : MIN([Order Date]) }`.

Choosing: FIXED when the level must not change with the view (most common and easiest to reason about), INCLUDE to get a finer level than the view then re-aggregate, EXCLUDE to ignore a view dimension (percent of total).

### In the news
See news box. Semantic layers in Tableau Next and Looker model such metrics once; LOD expressions are the workbook-level way to express the same "metric at a fixed grain" logic.

### Interview angle
> [!question] How it is asked
> "Write an LOD to show each customer's share of their region's sales" or "When would you use INCLUDE versus FIXED?"

> [!tip] Strong answer includes
> - The three types with syntax; FIXED independent of view
> - Order of operations: FIXED before dimension filters, so context filters are needed
> - A concrete example with numbers (share of region, first purchase date)
> - Alternatives: table calculations or a joined, pre-aggregated table

---
## 5. Table Calculations
> 🟠 Tier 2 · _Key points:_ Compute using; running total, rank, window average, percent of total, difference from previous

### Definition
**Table calculations** operate on the **aggregated results in the view** (after filters and aggregation), so they depend on the layout and need an **addressing/partitioning** choice ("Compute using": table across, table down, pane, or specific dimensions). They are done locally in Tableau rather than in the database. Common functions:
- `RUNNING_SUM(SUM([Sales]))`, `RUNNING_AVG`
- `WINDOW_AVG(SUM([Sales]), -2, 0)` moving average over current and previous 2 periods
- `RANK(SUM([Sales]))`, `RANK_DENSE`, `INDEX()`, `SIZE()`
- `LOOKUP(SUM([Sales]), -1)` previous value; `PREVIOUS_VALUE`
- `TOTAL(SUM([Sales]))` for percent of total
- Quick table calculations: running total, difference, percent difference, percent of total, moving average, year-to-date total, compound growth rate.

**Table calculation vs LOD:** a table calc changes with the view and sees only marks in the view; an LOD is computed in the data source at a stated level, independent of the view layout (for FIXED).

### Example
Monthly shipments (thousand units): 100, 120, 90, 150.
- Running sum: 100, 220, 310, 460.
- Moving average over three months `WINDOW_AVG(SUM([Units]), -2, 0)`: 100, 110, 103.3, 120.
- Percent difference from previous month `(SUM([Units]) - LOOKUP(SUM([Units]), -1)) / ABS(LOOKUP(SUM([Units]), -1))`: n/a, +20%, -25%, +66.7%.
- Rank of regions by sales: North 140 (1), South 100 (2), West 70 (3).
Setting "Compute using" to the wrong dimension (for example Region instead of Month) is the usual mistake and gives nonsense running totals.

### In the news
See news box. The newer "Concierge" and "Pulse" experiences return period-over-period changes automatically, yet analysts still need to understand the moving-average and difference logic to trust and challenge them.

### Interview angle
> [!question] How it is asked
> "What is a table calculation and how is it different from an LOD?"

> [!tip] Strong answer includes
> - Works on the aggregated view; depends on addressing and partitioning
> - Examples: running total, rank, moving average, percent of total
> - Contrast with LOD (database-level, independent of the view)
> - Pitfall: changing the layout changes the result

---
## 6. Dashboards, Actions and Interactivity
> 🟠 Tier 2 · _Key points:_ Layout containers, filter/highlight/URL/sheet/parameter/set actions, device layouts, storytelling

### Definition
A **dashboard** combines worksheets, filters, legends, text, images and web content in tiled or floating **layout containers** (horizontal and vertical). Design for the audience: a one-screen summary at top (KPIs), trends and breakdowns below, detail on demand. Set a fixed size or range for consistency and create **device layouts** for phone or tablet.

**Dashboard actions** (Tableau documentation lists six types):
1. **Filter:** use a selection in one view to filter another.
2. **Highlight:** dim all marks except related ones.
3. **Go to URL:** link to an external page or file.
4. **Go to Sheet:** navigate to another sheet, dashboard or story.
5. **Change Parameter:** set a parameter from a mark selection.
6. **Change Set Values:** update a set from a mark selection.

Related: **dashboard filters** (apply to selected sheets), **tooltips as viz-in-tooltip**, **dynamic zone visibility**, **stories** (sequence of sheets), **navigation buttons**, and **Pulse metrics** for subscription-style monitoring.

Design principles (see [[047 MIS & Dashboard Design]]): purpose first, five to seven KPIs, consistent colours, avoid dual-axes confusion, show targets and thresholds, label clearly, and test with real users.

### Example
A control-tower dashboard for a 3PL: top row KPI cards (OTIF 84.6%, average dock-to-stock hours, backlog); left a map of warehouses coloured by OTIF; right a bar of late orders by cause; below a trend line. A **filter action** on the map filters the bar and trend to the selected warehouse; a **parameter action** switches the trend between OTIF and fill rate; a **go to sheet** action opens a table of late orders for root-cause drill-down. Mobile layout shows KPI cards and the map only.

### In the news
See news box. Gemini in Data Studio and Tableau agents now offer "ask the dashboard", but the interaction design (what filters what) is still the author's job.

### Interview angle
> [!question] How it is asked
> "Design a dashboard for the head of operations." or "What interactivity would you add and why?"

> [!tip] Strong answer includes
> - Audience, decisions and KPIs first, charts second
> - Summary to detail layout; actions for drill-down; targets shown
> - Mention of performance (marks, filters) and mobile layout
> - A short walkthrough of how a manager would use it to find a problem

---
## 7. Looker Studio (Data Studio) Basics
> 🟠 Tier 2 · _Key points:_ Free web BI; connectors; data sources; calculated fields; sharing; Pro tier

### Definition
**Looker Studio** (originally Google Data Studio, renamed Looker Studio in 2022, and renamed Data Studio again on 16 April 2026 per Google's release notes) is Google's free, browser-based tool to build dashboards and reports from many data sources, with collaborative sharing like Google Docs.

Core concepts:
- **Data sources** (the connection plus field definitions) feed **reports** (pages of charts, tables, controls).
- **Connectors:** Google connectors (BigQuery, Google Sheets, Google Analytics, Google Ads, Search Console, YouTube, Cloud Storage, Cloud SQL), database connectors (MySQL, PostgreSQL, SQL Server, Redshift, Spanner), file upload (CSV), and **partner and community connectors** for third-party systems; Google's notes record 40+ new partner connectors added in 2026.
- **Fields:** dimensions and metrics with types; **calculated fields** at the data-source or chart level, using functions such as `CASE`, `IF`, `SUM`, `COUNT_DISTINCT`, `TODATE`, `REGEXP_EXTRACT`.
- **Controls:** filters, date-range selector, drop-downs; **parameters**; **data freshness** settings and caching; **extracted data** for speed.
- **Sharing:** link sharing, scheduled email delivery, embedding; **owner's credentials vs viewer's credentials** on a data source controls what the viewer can see.
- **Pro tier:** team workspaces, enhanced permissions, hourly scheduled delivery and alerts, audit logs, customer-managed encryption keys.

Strengths: no licence cost for basic use, instant sharing, tight with Google Marketing and BigQuery data. Limits: lighter modelling, weaker complex calculations and governance than Tableau or Power BI, performance tied to the source.

### Example
A D2C brand's marketing and operations review uses Google Sheets (daily returns log), BigQuery (order data) and Google Ads. The ops lead builds a one-page report: filter bar (date range, warehouse), scorecards (orders, return rate, delivery delay), time-series of orders vs delayed orders, and a table of cities by return rate with conditional colours. The data source for BigQuery uses **owner's credentials** so viewers need no BigQuery access; the report is shared with the leadership group as view-only and scheduled as a PDF every Monday.

### In the news
See news box. The rebrand to Data Studio and the addition of conversational analytics agents point to Google folding free reporting and BigQuery-based AI analysis into one product.

### Interview angle
> [!question] How it is asked
> "When would you choose Looker Studio over Power BI?"

> [!tip] Strong answer includes
> - Free, quick, web-based, Google-stack data (BigQuery, Sheets, GA); easy sharing
> - Limits: complex modelling, row-level governance, performance on large data
> - Connector options (Google, partner, community) and credentials model
> - Names the Pro tier and the 2026 name change correctly

---
## 8. Looker Studio Blends, Joins and Limits
> 🟠 Tier 2 · _Key points:_ Blend up to five sources; five join types; equality keys; aggregation pitfalls

### Definition
A **blend** combines data from several data sources into a single chart-level table. From Google's documentation (checked in this session): you can blend **up to five data sources**; supported join operators are **inner, left outer, right outer, full outer and cross**; join conditions support **equality only** between fields (the fields do not need the same name, only matching values). Rules of thumb:
- Choose a **join key** with unique values in each source to avoid row multiplication; aggregate before blending if sources have different grain.
- Metrics from a blend are aggregated at the chart's dimension level; use **left outer** to keep all rows from the primary table.
- A blend lives in the chart, so it is repeated for each chart that needs it; a **BigQuery view or a pre-joined table** is cleaner for reuse and performance.
- Compared with **Tableau relationships** (join at query time with aggregation at each table's own grain) and **Power BI data model relationships** (star schema; see [[044 Power BI & DAX]]), Looker Studio blends are simpler but less robust.

### Example
Join daily **orders** (BigQuery, key = Date + City) with **delivery delays** (Google Sheets, key = Date + City). Left outer blend with Orders on the left: every order row remains; delay minutes appear where the sheet has a match and blank elsewhere. If the sheet contains two rows for one Date and City, the join duplicates the order metric; fix by aggregating the sheet to one row per key first or by using a unique key column. For equality only, a join on "delay date between order date and order date + 3" is not possible: precompute the join in BigQuery.

### In the news
See news box. Google continues to add partner connectors (more than 40 in 2026), which makes blends tempting; the limits above explain why heavy blending is replaced by modelled views in the warehouse.

### Interview angle
> [!question] How it is asked
> "How do you combine two data sources in Looker Studio and what can go wrong?"

> [!tip] Strong answer includes
> - Blends: up to five sources, five join types, equality-only keys
> - Duplicate-key fan-out and grain mismatch; choosing the left table
> - Better alternative: pre-join in BigQuery or use a data model
> - Understanding aggregation level of metrics in blends

---
## 9. Decision Grid: Power BI vs Tableau vs Looker Studio vs Excel
> 🟠 Tier 2 · _Key points:_ Fit by data size, skills, governance, cost, ecosystem

### Definition
No tool wins everywhere; pick by decision criteria. Related notes: [[044 Power BI & DAX]], [[043 Advanced Excel (Pivot, Solver, Forecasting)]], [[047 MIS & Dashboard Design]].

| Criterion | Excel | Power BI | Tableau | Looker Studio |
|---|---|---|---|---|
| Typical user | Analyst, finance, ops | Business and IT teams, Microsoft shops | Analysts, data visualisation specialists | Marketing, small teams, Google-stack |
| Data volume | Up to roughly a million rows per sheet (more via the data model) | Millions to billions with import, DirectQuery, Fabric | Large with extracts and live connections | Depends on source (BigQuery scales) |
| Data modelling | Basic (Power Pivot) | Strong (star schema, DAX, Power Query) | Good (relationships, LOD, Prep) | Light (blends, calculated fields) |
| Visual flexibility | Medium | High | Very high (viz craft) | Medium |
| Self-service governance | Weak (file sprawl) | Strong (workspaces, RLS, sensitivity labels) | Strong (projects, permissions, certified sources) | Basic, stronger in Pro |
| AI assist | Copilot in Excel (licence) | Copilot | Pulse, Tableau Next agents | Gemini in Data Studio |
| Price signal (checked) | Part of Microsoft 365 | Pro $14 and PPU $24 per user per month from April 2025; Desktop free | Standard $15 and Enterprise $35 per user per month (Cloud page checked); Public free | Free; Pro paid |
| Best when | Ad hoc analysis, one-off models, final formatting | Enterprise reporting in a Microsoft environment | Exploratory analysis and rich dashboards across sources | Quick, cheap, shareable reports on Google data |

Decision shortcuts: Microsoft 365 company with SAP or Azure data and a need for RLS: **Power BI**. Exploration with many visual forms or multi-cloud: **Tableau**. Marketing analytics on GA and Ads, zero budget: **Looker Studio**. One-off analysis with data under 100,000 rows or a final board pack: **Excel**. Many companies run two (Power BI for enterprise metrics, Excel for ad hoc).

### Example
A 3PL with 12 warehouses, SAP S/4HANA data in a warehouse (Azure Synapse) and a Microsoft 365 licence base. Needs: daily OTIF and dock-to-stock KPIs, row-level security so each warehouse sees only its data, 200 viewers. Recommendation: **Power BI** (existing licences, RLS, scheduled refresh); the marketing team uses **Looker Studio** for GA and Ads; the commercial team uses **Excel** for pricing what-ifs. License cost for 200 viewers at $14 for Pro: 200 × 14 = $2,800 per month, versus capacity-based licensing, which can remove per-viewer fees for larger audiences; the team should model both and check current terms. See [[012 Supply Chain Analytics & KPIs]] for the KPI set.

### In the news
See news box. Power BI Pro's 2025 price rise and Tableau's reshaped editions mean the decision grid should be rechecked yearly; AI features (Copilot, Tableau agents, Gemini) are now part of the comparison.

### Interview angle
> [!question] How it is asked
> "Which BI tool would you choose for our company and why?"

> [!tip] Strong answer includes
> - Criteria first: users, data volume and source, governance, skills, cost, ecosystem
> - A clear recommendation tied to the company's stack, plus a fallback
> - Costs with a note that they change and must be checked
> - Mention of hybrid use (Excel for ad hoc, BI for governed KPIs)

---
## 10. Choosing the Right Chart for Operations KPIs
> 🟠 Tier 2 · _Key points:_ Comparison, trend, distribution, composition, relationship, target and variation charts

### Definition
Choose the chart by the question. Mapping:

| Question | Chart | Operations example |
|---|---|---|
| Compare categories | Sorted bar | Late orders by warehouse |
| Trend over time | Line | Daily OTIF, weekly inventory days |
| Actual vs target | Bullet chart or bar with reference line | OTIF vs 95% target |
| Variation and stability | Control chart (run chart with limits) | Daily picking errors (see [[091 Statistical Quality Control (SQC)]]) |
| Distribution | Histogram or box plot | Lead-time distribution, outliers |
| Prioritise causes | Pareto (bars + cumulative line) | Top delay causes |
| Part-to-whole | Stacked bar, treemap (pie only for 2-3 slices) | Spend by category |
| Relationship | Scatter | Order size vs delivery time |
| Pattern across two dimensions | Heat map | Dock congestion by hour and day |
| Flow or stage loss | Funnel or Sankey | Order-to-delivery stages |
| Change decomposition | Waterfall | Inventory bridge from opening to closing |
| Geography | Filled or symbol map | Delivery performance by pin-code region |

Rules: start axes at zero for bars, avoid 3D, limit colours, sort by value, label directly, use colour for meaning (red only for breaches), and annotate. Interview shorthand: **one message per chart, one chart per question.**

### Example
Delay causes for 500 late orders: carrier delay 190, stock-out 120, address error 75, packing error 60, weather 35, other 20. Percentages: 38%, 24%, 15%, 12%, 7%, 4%; cumulative: 38, 62, 77, 89, 96, 100. A **Pareto chart** shows that the first two causes explain 62% of lateness, so the team targets carrier SLAs and safety stock. A pie would not rank them; a table would not show the cumulative. In Tableau the Pareto uses a bar plus `RUNNING_SUM(SUM([Orders])) / TOTAL(SUM([Orders]))` on a second axis.

### In the news
See news box. AI "suggest a visual" features exist in Pulse and Data Studio, but they choose by data type, not by business question; the question-to-chart mapping remains your judgement.

### Interview angle
> [!question] How it is asked
> "Which chart would you use to show warehouse OTIF against target across 12 sites and over time?"

> [!tip] Strong answer includes
> - Link of chart to the question: bullet or bar vs target for sites, line for trend (small multiples)
> - Sorting, thresholds, colour used sparingly
> - Pareto for causes, control chart for stability, heat map for time patterns
> - Why not pie or 3D

---
## 11. Interview-Style Dashboard Questions and KPI Traps
> 🟠 Tier 2 · _Key points:_ KPI selection, definitions, ratio traps, validation, stakeholder questions

### Definition
Dashboard questions test business thinking more than tool clicks. A reusable structure: **(1) purpose and audience, (2) decisions and KPIs, (3) data sources and definitions, (4) layout and interactivity, (5) validation and refresh, (6) adoption.** Frequent traps:
- **Ratio of sums vs average of ratios** (see calculated fields).
- **Denominator drift:** OTIF defined differently across regions.
- **Aggregating non-additive measures** (inventory days summed across months, unique customers by month summed to a year).
- **Time-grain mismatch** (daily data vs monthly target).
- **Survivorship and filter traps:** filter excludes cancelled orders without saying so.
- **Too many KPIs and no thresholds**, or green dashboards with no action rule.
- **Stale or unreliable data** with no "last refreshed" stamp.

Practice questions: "How would you validate a dashboard before release?" (reconcile three totals to source, test edge cases, check filters, peer review). "Sales dropped 8% last week: what does the dashboard need to show?" (drill by region, product, channel, price, stock-out, then check data issues first).

### Example
Prompt: "Design the KPI page for a regional distribution manager." Answer: audience is a manager making daily dispatch decisions; KPIs: OTIF, order backlog in hours, vehicle fill rate, cost per drop; each with definition, owner, target and refresh. Layout: scorecards, trend, bullet vs target by depot, table of at-risk orders. Validation: compare Monday's OTIF with the ERP report (difference below 0.5 points) and test with a depot that has zero orders. Adoption: 15-minute training, daily stand-up use, quarterly KPI review. See [[012 Supply Chain Analytics & KPIs]].

### In the news
See news box. As vendors add conversational analytics, wrong or ambiguous definitions will be answered quickly but wrongly: governance of the metric dictionary matters more, not less.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would build a dashboard from a business request to go-live."

> [!tip] Strong answer includes
> - Clarify the decision and user, then KPI definitions with owners and targets
> - Data sources, model grain and refresh; reconciliation to a trusted source
> - Design: summary, trend, drill-down, thresholds; mobile if needed
> - Testing, documentation, training and measuring adoption

---
## 12. Performance, Security and Governance Tips
> 🟠 Tier 2 · _Key points:_ Extracts, fewer marks, filter design, row-level security, certified data, lifecycle

### Definition
**Performance (Tableau):** use **extracts** instead of heavy live queries; filter early (extract and data-source filters), use **context filters** sparingly; minimise marks (aggregate instead of showing millions of points); avoid too many quick filters ("only relevant values" runs queries); prefer fewer, simpler dashboards; avoid heavy string calculations and nested LODs on large data; use the **Performance Recording** feature to find slow queries; remove unused fields; use Boolean or integer calcs in place of strings. **Looker Studio:** use BigQuery with partitioned tables or a pre-aggregated view, limit the number of charts per page, use **extracted data** or caching and set data freshness appropriately, and avoid blends with large sources. **Power BI:** star schema, reduce cardinality, incremental refresh (see [[044 Power BI & DAX]]).

**Security and governance:** role-based **permissions** (project, workbook, data source); **row-level security** (user filters, `USERNAME()` mappings in Tableau, viewer credentials or filtered views in Looker Studio, RLS roles in Power BI); **certified data sources** with a metric dictionary; naming standards; version control and promotion from dev to prod; sensitive-data masking; usage monitoring and retirement of unused workbooks; **data freshness labels** and an ownership matrix. Link to data quality and master data practices in [[175 Data Quality, Master Data & Data Governance]].

### Example
A dashboard with 5 million order rows takes 40 seconds to load on a live connection. Fixes: switch to an extract with an aggregated dataset at day-warehouse-SKU grain (reduces rows to around 400,000), add a data-source filter for the last 24 months, replace 12 quick filters with 4 and an action filter, and show a map of 40 depots instead of 5 million points. Load time falls to about 4 seconds (illustrative), a tenfold improvement. Security: a user filter calculation `[Warehouse Owner] = USERNAME()` lets each manager see only their warehouse; admins see all by group membership.

### In the news
See news box. Google's Pro-only CMEK and data-residency features (June 2026) and Tableau's Advanced Management tier show that governance is increasingly what the paid tiers sell.

### Interview angle
> [!question] How it is asked
> "A dashboard is slow and users complain. How do you diagnose and fix it?"

> [!tip] Strong answer includes
> - Measure first (performance recording, query times), then reduce data, marks and filters
> - Extracts or aggregated tables; warehouse-side optimisation
> - Governance: security, certified sources, definitions, lifecycle
> - Trade-off between freshness and speed

---
## 13. ⭐ Advanced: Semantic Layers, Looker (LookML) and AI-Assisted Analytics
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **semantic layer** defines business metrics and relationships once (revenue, OTIF, active customers) so every dashboard and AI agent uses the same logic. Examples: **Tableau Semantics** (part of Tableau Next), **Looker's LookML** (code-defined dimensions, measures, explores in version control), **Power BI semantic models** (formerly datasets), dbt metrics layers and **Cube-type** headless BI.

**Looker vs Looker Studio:** **Looker** is Google Cloud's enterprise BI platform with the LookML modelling layer and governed exploration; **Looker Studio** (Data Studio) is the free report builder. Do not mix them up in an interview.

**AI-assisted analytics:** natural language to chart, calculated-field generation (Gemini in Data Studio), proactive anomaly alerts (Tableau Inspector, Pulse), Copilot in Power BI. Risks: hallucinated joins and metrics, access control leakage, confident wrong answers, unclear lineage. Controls: grounded semantic layer, verified answers, access policies, human review of key figures, audit logs.

**Operating model:** data product owners, certified metrics, usage analytics, cost control (query cost on BigQuery or Snowflake), and a request-to-release pipeline with testing.

### Example
Two teams report different OTIF values (84.6% vs 86.1%) because one counts partial shipments as on time. The fix is not another dashboard: the data team defines `OTIF = orders delivered in full and on or before promised date ÷ orders due` once in the semantic layer, retires the conflicting calculations, and points both dashboards and the AI assistant to the certified metric. Disagreements are then resolved by definition change requests, not by arguing over charts.

### In the news
See news box. Tableau Semantics in Tableau Next and Google's push for conversational analytics on BigQuery agents both start from the same premise: governed definitions come first, and AI sits on top.

### Interview angle
> [!question] How it is asked
> "How would you make sure everyone in the company gets the same number for revenue or OTIF?"

> [!tip] Strong answer includes
> - A single owned metric definition in a semantic layer, versioned and tested
> - Certified data sources and deprecating duplicates
> - How AI assistants are grounded in the same layer
> - Governance cadence: definition change requests, owners, audits
