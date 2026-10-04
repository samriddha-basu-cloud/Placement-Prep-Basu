---
tags: [analytics-tools, tier1]
area: Analytics & Tools
topic: "MIS & Dashboard Design"
tier: Tier 1
roles: Operations
status: complete
subtopics: 10
---
# MIS & Dashboard Design

⬅ [[046 Python for Operations]] · [[_Index - Analytics & Tools|Analytics & Tools]] · [[172 Tableau & Looker Studio - BI Tool Comparison]] ➡
> **Area:** Analytics & Tools · **Priority:** 🔴 Tier 1 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. MIS Definition & Purpose]]
2. [[#2. Dashboard Hierarchy]]
3. [[#3. KPI Selection]]
4. [[#4. Data Source Integration]]
5. [[#5. Report Automation]]
6. [[#6. Data Validation & Governance]]
7. [[#7. Storytelling with Data]]
8. [[#8. Excel-based MIS]]
9. [[#9. ⭐ Advanced: Operations KPI Definitions (OTIF, OEE, Fill Rate)]]
10. [[#10. ⭐ Advanced: Control Tower and Real-Time Operations Dashboards]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): BI platforms are adding AI assistants and governance
> **Power BI November 2025 feature summary.** Microsoft announced a standalone Copilot that now auto-selects data sources, "Verified Answers" that carry slicer and field-parameter state (filter limit raised from 3 to 10), a remote Power BI Model Context Protocol server (preview) so custom agents can query semantic models, and Semantic Model Version History (generally available, auto-captures up to 5 versions with restore). The card visual also became generally available. Theme: more self-service and AI on top of governed models, with audit and versioning. ([Source](https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-November-2025-Feature-Summary/ba-p/5173992))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. MIS Definition & Purpose
> 🔴 Tier 1 · _Tracker hint:_ Management Information System; operational vs strategic MIS

### Definition
A **Management Information System (MIS)** is an organised system of people, processes and technology that collects, processes, stores and distributes information so managers can plan, control and decide. Good MIS output is **relevant, accurate, timely, complete and actionable** (the right information to the right person at the right time).

| Level | Users | Decisions | Typical output |
|---|---|---|---|
| Operational MIS | Supervisors, planners | Daily, structured | Shift production, dispatches, stock-outs |
| Tactical MIS | Plant/regional managers | Weekly or monthly | OTIF, cost variance, capacity utilisation |
| Strategic MIS | Senior leadership | Quarterly or yearly, unstructured | Market share, ROCE, network design KPIs |

Modern stacks combine transaction processing systems (TPS), MIS reports, decision-support and executive dashboards. An MIS is a means; the test is whether a decision changes because of it.

### Example
A tyre plant's MIS shows: operational (hourly output and downtime per press), tactical (weekly OEE and scrap by line), strategic (monthly cost per tyre vs competitors and capacity-expansion case). Each layer uses the same underlying data at different granularity.

### In the news
See news box. AI assistants and verified answers speed up access to MIS data, but only if the underlying definitions are governed.

### Interview angle
> [!question] How it is asked
> "What is an MIS and how is it different from a dashboard?"

> [!tip] Strong answer includes
> - Definition and the five qualities of good information
> - Levels: operational, tactical, strategic
> - A dashboard is one presentation layer of an MIS
> - A concrete example linking information to a decision

---

## 2. Dashboard Hierarchy
> 🔴 Tier 1 · _Tracker hint:_ Strategic (C-suite) → Tactical (managers) → Operational (floor)

### Definition
Dashboards should match the viewer's decision horizon.

| Tier | Audience | Refresh | Content | Design |
|---|---|---|---|---|
| Strategic | CEO, COO, CFO | Monthly or quarterly | 5 to 8 headline KPIs, trend vs target and benchmark | Sparse, exception-focused |
| Tactical | Plant, regional, category managers | Daily or weekly | KPIs with drill-down by site, product, customer | Filters, variance analysis |
| Operational | Supervisors, floor, control tower | Real time or hourly | Live queues, alerts, task status | Big numbers, traffic lights, minimal text |

Principles: numbers must **reconcile** across tiers (the top-level figure is the sum of lower-level data); allow **drill-down** from strategic to operational; show variance against target not raw values; and avoid giving everyone the same all-in-one dashboard.

### Example
A logistics firm's CEO view shows OTIF 94% vs 96% target. A regional manager drills in to see Lane X at 85%. A depot supervisor sees today's 12 delayed trucks, each with reason code. One number, three views.

### In the news
See news box. Version history and certified models support consistent numbers across all three tiers.

### Interview angle
> [!question] How it is asked
> "Design a dashboard for a plant head vs a CEO."

> [!tip] Strong answer includes
> - Clarify the user, decision and frequency first
> - Fewer KPIs at the top, more detail at the bottom
> - Drill-down and reconciliation
> - Alerts for the floor, trends for leadership

---

## 3. KPI Selection
> 🔴 Tier 1 · _Tracker hint:_ SMART criteria; leading vs lagging; balanced scorecard perspective

### Definition
A **KPI** is a metric tied to an objective, with an owner, target and action. Select KPIs with:

- **SMART**: Specific, Measurable, Achievable, Relevant, Time-bound.
- **Leading vs lagging**: lagging indicators report outcomes (revenue, OTIF, defect rate); leading indicators predict them (supplier lead-time variance, open-order ageing, maintenance backlog). Use both.
- **Balanced scorecard (Kaplan and Norton)** perspectives: Financial, Customer, Internal process, Learning and growth.

Rules of thumb: fewer is better (5 to 8 per dashboard); each KPI has a clear definition, formula, data source and owner; avoid vanity metrics; beware that targets distort behaviour (Goodhart's law: a measure that becomes a target ceases to be a good measure).

### Example
Warehouse goal: faster dispatch. Lagging KPI: order-to-dispatch hours (target under 24, monthly). Leading KPIs: percentage of orders picked within 4 hours of release; putaway backlog. Balanced scorecard mapping: Financial = cost per order; Customer = OTIF; Internal = pick accuracy; Learning = training hours.

### In the news
See news box. AI assistants answer questions on whatever metrics exist, which makes careful KPI definitions even more important.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track for a warehouse / a procurement team?"

> [!tip] Strong answer includes
> - Start from objective, not from available data
> - Mix leading and lagging; balance cost, service, quality
> - Definition, owner, target, frequency for each
> - Warns about gaming and too many KPIs

---

## 4. Data Source Integration
> 🔴 Tier 1 · _Tracker hint:_ ERP → ETL → Data Warehouse → BI Tool pipeline

### Definition
Typical pipeline: **sources** (ERP such as SAP, WMS, TMS, CRM, Excel, IoT) → **ETL/ELT** (extract, transform, load) → **data warehouse or lakehouse** (a modelled, historical store, often star schema with fact and dimension tables) → **semantic layer** (shared metric definitions) → **BI tool** (Power BI, Tableau, Looker, Qlik).

Key concepts: **ETL** transforms before loading, **ELT** loads raw data then transforms in the warehouse; **incremental loads** (only new or changed rows) vs full loads; **master data** (SKU, customer, location) must be conformed across systems; **latency** (batch nightly vs near real time).

```sql
-- fact table joined to dimensions (star schema)
SELECT d.month, p.category, SUM(f.qty) AS units
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
JOIN dim_product p ON f.sku_key = p.sku_key
GROUP BY d.month, p.category;
```

### Example
A manufacturer pulls production orders from SAP, downtime from a plant historian and dispatches from a TMS. ETL nightly maps all three to a common `plant_id` and `sku_id`, loads a warehouse, and the plant-performance dashboard reads from one semantic model.

### In the news
See news box. Microsoft's push for a semantic model that agents and Copilot query shows the semantic layer is becoming central.

### Interview angle
> [!question] How it is asked
> "How would you build a dashboard when data is in five different systems?"

> [!tip] Strong answer includes
> - Pipeline stages in order
> - Master-data harmonisation and a single source of truth
> - Refresh frequency vs business need
> - Data quality checks at the load step

---

## 5. Report Automation
> 🔴 Tier 1 · _Tracker hint:_ Scheduled reports; trigger-based alerts; email distribution

### Definition
Automation removes manual compilation and gets the right information out on time. Three patterns:

- **Scheduled refresh and distribution:** report refreshes at a set time (e.g. 6 a.m.) and is emailed or posted to Teams.
- **Trigger-based alerts:** when a threshold is crossed (stock below ROP, OTIF under 90%, temperature out of range) a notification fires. Manage by exception.
- **Self-service portals:** users pull data via governed datasets.

Tools: Power BI subscriptions and data alerts, Power Automate, Excel with VBA/Power Query, Python scripts with cron, Airflow. Controls: owner, failure alerts, access control, change log, and a manual fallback. Avoid alert fatigue: tune thresholds so alerts are rare and actionable.

### Example
A 4-hour Monday MIS compile for 6 plants is replaced by a Sunday-night refresh and a 7 a.m. email. Saving $4 \times 52 = 208$ hours a year per analyst. An alert fires if any plant's scrap exceeds 3%.

### In the news
See news box. Power BI's version history and AI features reduce risk when many people maintain automated reports.

### Interview angle
> [!question] How it is asked
> "How did you reduce reporting effort?" / "How would you automate weekly reports?"

> [!tip] Strong answer includes
> - Baseline effort and result in hours or percent
> - Schedule plus exception alerts
> - Failure monitoring and ownership
> - Avoid claiming figures you cannot support

---

## 6. Data Validation & Governance
> 🔴 Tier 1 · _Tracker hint:_ Source of truth; data quality rules; audit trail

### Definition
**Data governance** is the policies, roles and controls that keep data trustworthy and secure. Pillars:

- **Single source of truth:** one agreed system and definition for each metric (e.g. "OTIF" defined once).
- **Data quality dimensions:** accuracy, completeness, consistency, timeliness, uniqueness, validity.
- **Validation rules:** range checks, mandatory fields, referential integrity, reconciliation totals against ERP/finance, duplicate checks.
- **Audit trail and lineage:** who changed what and when; where each number came from.
- **Roles:** data owner (accountable), steward (maintains quality), consumer.
- **Access control** and compliance (India's Digital Personal Data Protection Act 2023 for personal data).

Rule: a dashboard with one wrong number loses trust faster than a dashboard with a missing one.

### Example
Sales MIS and finance report different revenue. Root cause: one uses invoice date, the other uses dispatch date. Fix: a data-dictionary entry fixing the definition, an automated reconciliation check, and a named owner.

### In the news
See news box. Semantic Model Version History is an audit-trail control in practice.

### Interview angle
> [!question] How it is asked
> "What do you do if two reports show different numbers?"

> [!tip] Strong answer includes
> - Trace lineage, compare definitions and filters, reconcile
> - Establish single source of truth and owner
> - Preventive controls: validation rules, reconciliation, access
> - Communicates transparently to stakeholders

---

## 7. Storytelling with Data
> 🔴 Tier 1 · _Tracker hint:_ Pyramid principle; chart selection; reducing clutter (Cole Nussbaumer)

### Definition
Insight must be communicated, not just displayed.

- **Pyramid principle (Barbara Minto):** answer first, then supporting arguments, then data.
- **Cole Nussbaumer Knaflic's approach:** understand context (who, what, how), choose an effective visual, **eliminate clutter**, **focus attention** (colour, size, position), think like a designer, tell a story (beginning, middle, end).
- **Chart selection:** line for trend; bar for comparison; scatter for relationship; table for exact values; avoid pies beyond 2 to 3 slices, 3-D and dual axes without need.
- **Declutter:** remove gridlines, borders, redundant labels; direct-label lines; one highlight colour; action title ("OTIF fell 6 points in Q3 due to carrier X").

### Example
Slide title "Rework cost is 4% of revenue, concentrated in Line 3" followed by a bar chart with Line 3 in orange and others grey, beats a slide titled "Rework analysis" with a dense multi-colour table.

### In the news
See news box. As AI generates charts automatically, human judgement on message and framing becomes the differentiator.

### Interview angle
> [!question] How it is asked
> "How would you present this analysis to the CEO?"

> [!tip] Strong answer includes
> - Lead with the recommendation (pyramid)
> - One message per chart; action titles
> - Remove clutter, highlight the point
> - Tailor depth to the audience

---

## 8. Excel-based MIS
> 🔴 Tier 1 · _Tracker hint:_ Dynamic dashboards; form controls; VBA basics for automation

### Definition
Excel remains the most common MIS tool in Indian operations. Building blocks:

- **Data model:** raw data in an Excel Table (`Ctrl+T`), Power Query for refreshable cleaning, optional Power Pivot.
- **Formulas:** `SUMIFS`, `COUNTIFS`, `XLOOKUP` (or `INDEX/MATCH`), `IFERROR`, dynamic arrays (`FILTER`, `UNIQUE`, `SORT`).
- **Dynamic dashboards:** PivotTables + PivotCharts + **Slicers**/Timelines; named ranges; conditional formatting; sparklines.
- **Form controls:** drop-downs (Data Validation list), combo boxes, option buttons linked to a cell that drives formulas.
- **VBA basics:** macros to refresh and export.

```vba
Sub RefreshAndExport()
    ThisWorkbook.RefreshAll
    ThisWorkbook.Sheets("Dashboard").ExportAsFixedFormat Type:=xlTypePDF, _
        Filename:=ThisWorkbook.Path & "\MIS.pdf"
End Sub
```

Limits: row limits (about 1.05 million), version control, multi-user risk, manual errors; move to BI/database when scale or governance demands it.

### Example
A plant MIS workbook: Power Query loads daily production CSVs, a table feeds PivotTables with a Plant slicer, a drop-down selects the month, `SUMIFS` computes OEE inputs, and a macro exports a PDF each morning.

### In the news
See news box. Many firms use Excel for prototyping and Power BI for governed distribution.

### Interview angle
> [!question] How it is asked
> "Walk me through how you built an MIS in Excel" or "When would you move from Excel to Power BI?"

> [!tip] Strong answer includes
> - Structured data, Power Query, PivotTables, slicers
> - Automation with VBA or refresh
> - Awareness of limits and move-to-BI triggers
> - Accuracy checks (reconciliation, locked cells)

---

## 9. ⭐ Advanced: Operations KPI Definitions (OTIF, OEE, Fill Rate)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Precisely defined KPIs are the heart of any MIS.

- **OTIF** $=\dfrac{\text{orders delivered on time and in full}}{\text{total orders}}\times100$ (define the on-time window and the tolerance for in-full).
- **Fill rate** $=\dfrac{\text{units shipped}}{\text{units ordered}}$.
- **OEE** $=\text{Availability}\times\text{Performance}\times\text{Quality}$ where Availability = run time / planned time, Performance = actual output / ideal output at run time, Quality = good units / total units.
- **Inventory turns** $=\dfrac{COGS}{\text{average inventory}}$.

World-class OEE is often cited around 85%, but benchmarks vary by industry.

### Example
Planned time 480 min, downtime 48 min: Availability $=432/480=90\%$. Output 3,800 vs ideal 4,000 in run time: Performance $=95\%$. Good units 3,724 of 3,800: Quality $=98\%$. $OEE=0.90\times0.95\times0.98=83.8\%$.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "How is OEE calculated and what would you do if it is 60%?"

> [!tip] Strong answer includes
> - Formula with all three factors
> - Decompose to find the biggest loss
> - Data capture reliability
> - Action link (SMED, preventive maintenance, quality at source)

---

## 10. ⭐ Advanced: Control Tower and Real-Time Operations Dashboards
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **control tower** gives end-to-end visibility across orders, inventory and shipments, with exception management. Features: live data feeds (GPS, WMS, IoT), rules engine for alerts, root-cause tags, escalation paths and a daily review cadence. Design rules: show only what needs action, rank exceptions by business impact (value at risk, customer priority), give the owner and next step, and measure response time to alerts as a KPI.

Benefits: faster reaction, fewer expedites, shared view between functions. Pitfalls: data latency, too many alerts, no clear owner.

### Example
A dashboard flags 12 trucks predicted to miss delivery windows, sorts them by order value, and lets the dispatcher call the driver or re-route. Metric: average time from alert to action falls from 90 to 30 minutes.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "How would you design a control tower for a distribution network?"

> [!tip] Strong answer includes
> - Data sources and latency
> - Exception rules and prioritisation by impact
> - Ownership and escalation
> - Measuring the tower's own effectiveness

---
## 🔗 Go deeper: expansion notes
- [[172 Tableau & Looker Studio - BI Tool Comparison|Tableau & Looker Studio - BI Tool Comparison]]
- [[175 Data Quality, Master Data & Data Governance|Data Quality, Master Data & Data Governance]]
