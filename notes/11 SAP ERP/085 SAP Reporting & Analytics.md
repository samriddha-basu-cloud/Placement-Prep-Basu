---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP Reporting & Analytics"
tier: Tier 1
roles: Operations
status: complete
subtopics: 11
---
# SAP Reporting & Analytics

⬅ [[084 SAP QM & PM]] · [[_Index - SAP ERP|SAP ERP]] · [[190 SAP FI-CO Essentials for Operations Professionals]] ➡
> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Standard SAP Reports]]
2. [[#2. SAP List Viewer (ALV)]]
3. [[#3. Information System (LIS)]]
4. [[#4. SAP BW/BI]]
5. [[#5. SAP Analytics Cloud (SAC)]]
6. [[#6. Fiori Analytical Apps]]
7. [[#7. ABAP Query (SQ01/SQ02)]]
8. [[#8. SAP Report to Excel]]
9. [[#9. Key SCM T-codes Summary]]
10. [[#10. ⭐ Advanced: CDS Views and Embedded Analytics in S/4HANA]]
11. [[#11. ⭐ Advanced: Designing a Supply Chain KPI Dashboard from SAP Data]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): SAP bundles BW, Datasphere and Analytics Cloud into Business Data Cloud
> **SAP Business Data Cloud (launched 13 Feb 2025; general availability planned April 2025).** The platform combines SAP Datasphere, SAP Analytics Cloud (SAC), SAP BW / BW/4HANA Private Cloud Edition and managed SAP Databricks, plus "Intelligent Applications". SAP's FAQ states BW 7.5 PCE contracts can run until the **end of 2030** and BW/4HANA PCE carries a commitment **until at least 2040**. Message to customers: keep BW investments, but new analytics is moving to a cloud data-product model. ([SAP Community FAQ](https://community.sap.com/t5/technology-blog-posts-by-sap/sap-business-data-cloud-faqs/ba-p/14022781))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Standard SAP Reports
> 🔴 Tier 1 · _Tracker hint:_ T-codes starting with MB (inventory), ME (purchasing), CO (controlling); ALV grid

### Definition
Every SAP module ships with **standard reports** run by **transaction codes (T-codes)**. A planner's daily toolkit:

| Area | T-code | Report |
|---|---|---|
| Inventory | MB52 | Warehouse stocks of material (by plant/storage location) |
| Inventory | MMBE | Stock overview for one material |
| Inventory | MB51 | Material document list (movements) |
| Inventory | MB5B | Stocks on posting date (historical) |
| Purchasing | ME2M | POs by material |
| Purchasing | ME2N | POs by PO number; ME2L by vendor |
| Purchasing | ME5A | Purchase requisition list |
| Planning | MD04 | Stock/requirements list |
| Controlling | KSB1 | Cost centre line items |
| Production | COOIS | Production order information system |

Prefixes help memory: **MB** material/inventory, **ME** purchasing, **MD** MRP, **CO** production/controlling orders, **VA/VL** sales and delivery. Most output uses the **ALV grid** (next sub-topic). In S/4HANA many are replaced or complemented by Fiori apps, but the T-codes still run.

### Example
A buyer asks "what is open on material 100234?" Run ME2M with the material and open-items scope; ALV lists each PO, delivery date and open quantity. Then MD04 to see if the delay causes a shortage.

### In the news
See news box. Whatever the platform, daily operational questions are still answered by these transaction-level reports; BDC is aimed at cross-system analytics.

### Interview angle
> [!question] How it is asked
> "Which SAP reports would you use to find open POs, current stock and expected shortages?" 

> [!tip] Strong answer includes
> - 4–6 correct T-codes tied to a business question (not a memorised list)
> - Difference between transactional (live) and analytical reports
> - Awareness that S/4HANA offers Fiori equivalents
> - Honest statement of exposure level (user/consultant)

---

## 2. SAP List Viewer (ALV)
> 🔴 Tier 1 · _Tracker hint:_ Sort, filter, download; display variant; export to Excel

### Definition
The **ABAP List Viewer (ALV) grid** is the standard interactive table control for report output. Features: **sort** (ascending/descending), **filter**, **subtotals and totals**, **column choice and order**, **layout/display variants** (save your column set as a variant, set as default), **drill-down** by double-click, and **export** (spreadsheet, local file, PDF, mail).

Typical workflow: run report → right-click column → set filter → *Layout > Change* to hide columns → *Save layout* (user-specific or global with /prefix) → export. Selection-screen variants (save entered selection values) are different from ALV layout variants; many candidates confuse them.

### Example
After MB52, the grid has 20 columns. You filter plant = 1000, sort by value descending, add subtotal on material group, and save layout `/OBS_STOCK`. Next week one click shows slow movers in the same format.

### In the news
See news box. Even SAC and Fiori dashboards are fed by the same data; ALV remains the quick ad-hoc view.

### Interview angle
> [!question] How it is asked
> "A manager wants a weekly stock report by plant with value. How would you produce it quickly in SAP?"

> [!tip] Strong answer includes
> - Run the right report, apply selection variant, adjust ALV layout, export
> - Distinction between selection variant and layout
> - Automation: background job and email with the variant
> - Caveat: Excel copy loses live link; document the data timestamp

---

## 3. Information System (LIS)
> 🔴 Tier 1 · _Tracker hint:_ Logistics Information System; standard analyses; flexible analyses

### Definition
The **Logistics Information System (LIS)** collects transactional data (sales, purchasing, inventory, production, plant maintenance, quality) into **information structures** (S-tables, such as S001 for customers and S012 for purchasing). **Updating** is driven by update rules, and data is read in:
- **Standard analyses**: ready-made views (for example purchasing analysis by vendor/material/period) with drill-down and graphics.
- **Flexible analyses**: user-defined key figures and characteristics, comparisons across periods.

Sub-systems include SIS (Sales), PURCHIS (Purchasing), INVCO (Inventory Controlling), SFIS (Shop floor) and PMIS (Plant Maintenance). LIS data also feeds BW through **LO extractors** (set up in LBWE). In S/4HANA, LIS is largely legacy: real-time **CDS-view-based** analytics and Fiori are preferred, though many companies still use it.

### Example
Purchasing head wants "value of POs by vendor by month for 12 months" without building a custom report: standard purchasing analysis gives it with drill-down to material level, based on pre-aggregated structure data so it runs fast.

### In the news
See news box. BW and LIS data structures are exactly what SAP's customers are being nudged to expose via cloud data products.

### Interview angle
> [!question] How it is asked
> "What is LIS and why is it different from a normal report?"

> [!tip] Strong answer includes
> - Pre-aggregated information structures updated from transactions
> - Standard vs flexible analyses
> - Role as BW data source and why it is being replaced by CDS
> - Limitation: update lag/inconsistency if update rules are mis-set

---

## 4. SAP BW/BI
> 🔴 Tier 1 · _Tracker hint:_ Business Warehouse; InfoCubes, DSO; queries in BEx Analyzer; predecessor to SAP Analytics Cloud

### Definition
**SAP BW (Business Warehouse, earlier called BI)** is SAP's data warehouse. Flow: **source systems** (ERP, files) → **extractors** (for example LO) → **PSA** (staging) → **transformations** → **DataStore Object (DSO)** (detail, with change log) → **InfoCube** (star schema for multidimensional queries) → **BEx query** → front end (**BEx Analyzer** in Excel, now largely replaced by Analysis for Office, Web, SAC).

Key objects: **InfoObjects** (characteristics and key figures), **InfoProviders**, **MultiProviders**. **BW/4HANA** simplifies this to a few objects (advanced DSO, CompositeProvider) and runs only on HANA. Benefits: historical consolidation across systems, harmonised master data, large volumes, delta loads; drawback: latency and IT dependence.

### Example
A tyre maker loads sales orders, deliveries and billing into BW overnight. An InfoCube with customer, material, plant and month answers "revenue and fill rate by region by quarter" which no single ERP report can.

### In the news
See news box. SAP committed to supporting BW 7.5 PCE to 2030 and BW/4HANA to at least 2040, so BW knowledge remains employable while SAC grows.

### Interview angle
> [!question] How it is asked
> "What is the difference between ERP reporting and a data warehouse?"

> [!tip] Strong answer includes
> - OLTP vs OLAP, history and integration
> - Extract-transform-load flow with DSO and InfoCube
> - BEx/AO as front ends and the move to SAC
> - When you would not use it: real-time operational needs

---

## 5. SAP Analytics Cloud (SAC)
> 🔴 Tier 1 · _Tracker hint:_ Cloud BI + planning; predictive; integrates with S/4HANA directly

### Definition
**SAP Analytics Cloud** is a single SaaS product for **BI (dashboards, stories), planning (budget, forecast, S&OP-style what-if) and predictive analytics (smart insights, time-series forecasts, classification)**. Data access modes:
- **Live connection**: queries run in source (S/4HANA via CDS views, BW, Datasphere); no data copy, always fresh.
- **Acquired (import) data**: copied into SAC, faster but stale until refreshed.

Features: stories with charts, geo maps, calculations, **Just Ask / smart discovery** (natural-language features), integration with Excel and the SAP Business Technology Platform. Compared with BEx, SAC is browser-based, role-friendly and includes planning. SAC is a core component of Business Data Cloud.

### Example
Supply chain head builds a story with live S/4HANA connection: OTIF by plant, inventory days and a forecast of next quarter's demand using SAC's time-series forecast; planners adjust a safety-stock assumption and see cost impact in the same screen.

### In the news
See news box. SAC is one of the four named components in SAP Business Data Cloud.

### Interview angle
> [!question] How it is asked
> "How would you build a dashboard for the COO from SAP data?"

> [!tip] Strong answer includes
> - Choose KPIs first, then data source (live vs import)
> - Mention governance: one version of truth, roles, refresh
> - Planning vs reporting capability of SAC
> - Comparison with Power BI/Tableau without bashing

---

## 6. Fiori Analytical Apps
> 🔴 Tier 1 · _Tracker hint:_ Role-based analytical tiles; real-time HANA queries; mobile ready

### Definition
**SAP Fiori** is the role-based UX for S/4HANA. Types of apps: **transactional**, **fact sheets**, and **analytical** (KPI tiles, smart business cards, **Overview Pages**). They run on **CDS views** (core data services) over HANA, so numbers are **live**, not extracted. Examples in supply chain: *Monitor Material Coverage*, *Manage Purchase Orders*, *Stock – Multiple Materials*, *Monitor Purchase Order Items*. The **Fiori Launchpad** shows tiles with live counts or KPI semantic colours (red/green) and drill into the underlying app. Responsive layout works on mobile. Concept: **embedded analytics** (analysis directly in the transactional system).

### Example
A procurement manager's launchpad has a tile "Overdue PO items: 37" in red. One tap opens the list, filtered by vendor; she exports to Excel and calls the three worst vendors, which would otherwise need ME2N, a variant and a download.

### In the news
See news box. Embedded Fiori analytics covers real-time operations; BDC/SAC covers cross-domain and planning.

### Interview angle
> [!question] How it is asked
> "What has changed in SAP reporting with S/4HANA?"

> [!tip] Strong answer includes
> - CDS views and HANA enabling live analytics
> - Role-based tiles, KPI cards, mobile readiness
> - Distinction: embedded analytics vs BW vs SAC
> - A concrete supply chain app example

---

## 7. ABAP Query (SQ01/SQ02)
> 🔴 Tier 1 · _Tracker hint:_ User-defined reports; no coding needed; field groups and queries

### Definition
**SAP Query** lets power users build reports without ABAP coding. Components and T-codes:
1. **SQ03 User groups**: who may use which queries.
2. **SQ02 InfoSets**: define the data source (table join, logical database, or table) and group fields into **field groups**.
3. **SQ01 Query**: select fields, set selection criteria, list layout (basic list, statistics, ranked list), output as ALV.

Users must be assigned to a user group and have authorisation. Queries can be run from the menu, SQVI (quick viewer, single-user), or added to a user menu. Limitations: simple joins only, performance on big tables, not transported easily in some setups; in S/4HANA, custom CDS views and Fiori **Custom Analytical Queries** are the strategic route.

### Example
Plant head wants a list of material, storage location and stock for a custom attribute not in MB52. Admin builds an InfoSet on MARA/MARD (SQ02), assigns a field group; the key user builds the query in SQ01 and runs it with plant as selection.

### In the news
See news box. Self-service reporting is the same aspiration as SAC and Datasphere, but with governed data products.

### Interview angle
> [!question] How it is asked
> "What do you do when the standard report does not give the view the business needs?"

> [!tip] Strong answer includes
> - Ladder: variant/layout → SQVI/SQ01 → custom report/CDS → BW/SAC
> - Know InfoSet/user group/query roles
> - Mention authorisations and data governance
> - Weigh cost/benefit of building vs using standard

---

## 8. SAP Report to Excel
> 🔴 Tier 1 · _Tracker hint:_ System → List → Save → Local File; or use Export button in ALV; SAP BW to Excel

### Definition
Three routes:
1. **Classic list**: *System > List > Save > Local File* and choose format (unconverted text, spreadsheet, rich text, HTML).
2. **ALV grid**: *List > Export > Spreadsheet* (or the export icon, Ctrl+Shift+F7) and choose Excel/ Excel in-place; the layout (columns, order, filters) is exported.
3. **BW / SAC**: *Analysis for Office* (live Excel add-in connected to queries) or export from BEx/SAC.

Good practice: export with a saved layout, keep units/currency columns, **never overwrite** the source, document report name, selection and timestamp; avoid scientific-notation and leading-zero loss on material numbers (format text columns). Typical clean-up in Excel: Text-to-Columns, TRIM, VLOOKUP/XLOOKUP, pivot table.

### Example
Export MB52 with 5,000 rows; pivot by plant and material group to value; add XLOOKUP to ABC class; chart the top 20 SKUs by stock value. Results go to the S&OP meeting as a one-page view.

### In the news
See news box. Governance concerns about "Excel as the data layer" are one of the arguments for live connections (Analysis for Office, SAC).

### Interview angle
> [!question] How it is asked
> "Have you worked with SAP data in Excel? How do you make it reliable?"

> [!tip] Strong answer includes
> - Right route (ALV export vs Analysis for Office live)
> - Data hygiene issues: leading zeros, units, duplicates
> - Reproducibility: saved layout/variant, timestamp, steps
> - Excel skills applied (pivot, lookup) to produce a decision

---

## 9. Key SCM T-codes Summary
> 🔴 Tier 1 · _Tracker hint:_ MB52 stock, ME2M PO by material, MD04 stock/reqmts list, CO26 order info system

### Definition
Cheat sheet of supply-chain T-codes (check the exact system, as menus and availability vary with S/4HANA vs ECC):

| Process | T-code | Use |
|---|---|---|
| Stock | MB52, MMBE, MB5B, MB51 | Stock by location, overview, history, movements |
| Purchasing | ME21N / ME22N / ME23N | Create / change / display PO |
| Purchasing | ME2M, ME2N, ME2L | PO lists by material / PO number / vendor |
| Receipt/Invoice | MIGO, MIRO | Goods movement, invoice verification |
| Planning | MD04, MD07, MD01/MD02 | Stock/requirements list, collective, MRP run |
| Production | CO01, CO02, CO03, COOIS, CO26 | Create/change/display production order, order information, standard analyses |
| Sales/delivery | VA01, VA05, VL01N, VL06O | Order create, order list, delivery, outbound delivery monitor |
| Master | MM01, MM03, XK01 (ECC) | Material master, vendor (S/4 uses BP) |
| Query | SQ01, SE16N | Query and table display (authorised use only) |

### Example
Diagnosing a stock-out: MMBE (is stock really zero?) → ME2M (is a PO open, when due?) → MD04 (what is the demand and the planned receipts?) → COOIS (is the production order delayed?). Four T-codes give the root cause.

### In the news
See news box. The T-code layer persists while analytics layers evolve.

### Interview angle
> [!question] How it is asked
> "Name the SAP transactions you would use to investigate a delayed customer order."

> [!tip] Strong answer includes
> - Follow the flow: sales order → stock → purchasing → production
> - Accurate codes with purpose; admit gaps instead of guessing
> - Use of ALV variants to share the result
> - Link to the KPI (OTIF, fill rate) that frames the investigation

---

## 10. ⭐ Advanced: CDS Views and Embedded Analytics in S/4HANA
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Core Data Services (CDS) views** define data models on HANA tables with semantics and annotations (`@Analytics`, `@UI`). Cube-type CDS views (analytical data models) and query views power Fiori analytical apps and SAC **live** connections without a separate warehouse. Benefits: **no data replication**, real-time numbers, reuse of authorisations. Extensibility: custom fields and **custom analytical queries** (app *Custom Analytical Queries*) built by key users.

```abap
@AbapCatalog.sqlViewName: 'ZVSTOCK'
@Analytics.dataCategory: #CUBE
define view Z_StockCube as select from mard {
  key matnr, key werks, key lgort, labst }
```
(Illustrative only; production views should use released SAP views.)

### Example
Demand planner wants stock coverage by plant live. Rather than loading stock to BW nightly, a CDS-based query view feeds a SAC story over a live connection; figures match MMBE at all times.

### In the news
See news box. SAP's cloud direction keeps embedded analytics for operations and uses Datasphere/BDC for cross-source data.

### Interview angle
> [!question] How it is asked
> "When would you use embedded analytics versus a data warehouse?"

> [!tip] Strong answer includes
> - Embedded for real-time, single-system, operational questions
> - Warehouse/data cloud for history, multi-source, heavy transformation
> - Performance and governance trade-offs
> - Reuse of authorisations and semantic layer

---

## 11. ⭐ Advanced: Designing a Supply Chain KPI Dashboard from SAP Data
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Dashboards fail when they start from data rather than decisions. Method: (1) **decision first** (who decides what, how often); (2) pick 5–8 KPIs from SCOR attributes (OTIF, fill rate, inventory days, forecast accuracy, perfect order, cash-to-cash); (3) **define each KPI precisely** (numerator, denominator, source table, exclusions); (4) choose a **refresh** (live or nightly); (5) **targets and thresholds** (traffic lights); (6) **drill path** from KPI to exception list.

$$\text{OTIF \%} = \frac{\text{order lines delivered on time and in full}}{\text{total order lines}} \times 100$$

Source mapping: deliveries (LIKP/LIPS), sales orders (VBAK/VBAP), stock (MARD), POs (EKKO/EKPO).

### Example
OTIF: 4,200 lines shipped in a month; 3,570 on time and in full → 3,570/4,200 = **85%**. Drill by customer shows two customers account for 60% of misses, so action targets them.

### In the news
See news box. As platforms consolidate, the quality of KPI definitions matters more than the tool.

### Interview angle
> [!question] How it is asked
> "Design a control tower or KPI dashboard for a distribution network."

> [!tip] Strong answer includes
> - Decision-driven KPI selection and clear definitions
> - Data lineage from SAP tables to KPI
> - Thresholds and exception drill-down
> - Adoption: owner, review cadence, data-quality checks

---

---
## 🔗 Go deeper: expansion notes
- [[198 SAP IBP, APO & Demand-Driven Planning|SAP IBP, APO & Demand-Driven Planning]]
- [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows|SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]
