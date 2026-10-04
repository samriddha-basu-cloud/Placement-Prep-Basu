---
tags: [excel-advanced, tier1]
area: Excel Advanced
topic: "Excel for Operations & SCM"
tier: Tier 1
roles: Operations
status: complete
subtopics: 12
---
# Excel for Operations & SCM

⬅ [[077 Solver, Goal Seek & What-If Analysis]] · [[_Index - Excel Advanced|Excel Advanced]] · [[187 Excel Interview Problem Bank & Case Exercises]] ➡
> **Area:** Excel Advanced · **Priority:** 🔴 Tier 1 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Inventory Tracker Template]]
2. [[#2. Production Schedule in Excel]]
3. [[#3. OEE Calculator]]
4. [[#4. Supplier Scorecard]]
5. [[#5. Demand Forecast Model]]
6. [[#6. ABC Analysis in Excel]]
7. [[#7. MIS Dashboard Structure]]
8. [[#8. Variance Analysis Template]]
9. [[#9. Pareto Chart]]
10. [[#10. Cost Model in Excel]]
11. [[#11. ⭐ Advanced: Safety Stock, Service Level and Reorder Engine]]
12. [[#12. ⭐ Advanced: Automating Ops Reports with Power Query and ERP Exports]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Excel stays the operations analyst's tool as Python and AI agents arrive
> **Python in Excel (GA Sep 2024).** The Register reported on 18 Sep 2024 that Python in Excel became generally available for Windows users with Microsoft 365 Business or Enterprise on the Current Channel, letting analysts run forecasting and statistics inside workbooks (built with Anaconda; premium compute $24 per user per month). ([The Register](https://www.theregister.com/2024/09/18/python_in_excel_general_release/))
> 
> **Agent Mode in Excel (Dec 2025 to Jan 2026).** Microsoft announced general availability of Agent Mode on Excel for the web on 9 Dec 2025 (commercial Microsoft 365 Copilot users) and on Windows on 27 Jan 2026. For operations teams this means first-draft trackers, scorecards and dashboards can be generated from a prompt, while checking the logic (reorder points, OEE definitions, weights) remains the planner's job. I did not verify any operations-specific adoption numbers, so none are quoted. ([Excel for web](https://techcommunity.microsoft.com/blog/excelblog/agent-mode-in-excel-is-now-generally-available-on-excel-for-web/4476092), [Desktop](https://techcommunity.microsoft.com/blog/excelblog/agent-mode-in-excel-is-now-generally-available-on-desktop/4457408))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Inventory Tracker Template
> 🔴 Tier 1 · _Tracker hint:_ Columns: SKU, Description, Opening, In, Out, Closing, ROP, EOQ; conditional formatting on stock alerts

### Definition
A reusable stock ledger built as an Excel **Table** with columns: SKU, Description, UoM, Opening, In (receipts), Out (issues), Closing, Daily demand, Lead time, Safety stock, ROP, EOQ, Status.

```excel
Closing = Opening + In - Out
ROP     = Daily demand * Lead time + Safety stock
EOQ     = SQRT(2 * Annual demand * Order cost / Holding cost)
Status  = IF(Closing <= ROP, "REORDER", IF(Closing <= ROP*1.2, "WATCH", "OK"))
```
Transactions are better kept in a separate **Transactions** sheet (Date, SKU, Type, Qty) with the tracker using `SUMIFS`: `Closing = Opening + SUMIFS(Qty, SKU, A2, Type, "IN") - SUMIFS(Qty, SKU, A2, Type, "OUT")`. Add data validation (SKU dropdown, positive quantities), conditional formatting (red when `=$G2<=$K2`), and a pivot for stock value (Closing x unit cost). Protect formulas; log changes; reconcile to the ERP periodically (e.g. SAP MB52 stock report).

### Example
SKU 1001: opening 500, in 200, out 350, so closing = 500 + 200 - 350 = 350. Daily demand 20, lead time 7 days, safety stock 40: ROP = 20 x 7 + 40 = 180; closing 350 > 180 and above 1.2 x 180 = 216, so status OK. After a further 140 units issued, closing = 210: still above ROP but below 216, so WATCH. Annual demand 7,300, S = ₹400, H = ₹20: EOQ = sqrt(2 x 7,300 x 400 / 20) = sqrt(292,000) = 540.

### In the news
See news box. Agent Mode can draft a tracker, but you must confirm ROP and status logic before relying on its alerts.

### Interview angle
> [!question] How it is asked
> "Design an inventory tracker in Excel that alerts when to reorder."

> [!tip] Strong answer includes
> - Columns and the closing, ROP and EOQ formulas
> - Transactions sheet plus SUMIFS rather than manual overwriting
> - Conditional-format alerts and data validation
> - Reconciliation to ERP and limits of Excel (multi-user, audit trail)

---

## 2. Production Schedule in Excel
> 🔴 Tier 1 · _Tracker hint:_ Gantt using conditional formatting or stacked bar; resource loading

### Definition
A production schedule lists jobs with start, duration, end, line/resource and status, and visualises them as a **Gantt chart**. Two methods:

1. **Conditional-formatting Gantt**: dates across the top (D4:AH4); a job row with Start in B and End in C; apply to the grid the formula rule `=AND(D$4>=$B5, D$4<=$C5)` with a fill colour. Add a "today" line with `=D$4=TODAY()`.
2. **Stacked bar Gantt**: bar chart with Start date as an invisible first series and Duration as the visible second series; reverse the category axis.

Formulas: End = `WORKDAY(Start, Duration-1, Holidays)`; Duration = Quantity / Rate. **Resource loading**: for each day or week, `=SUMIFS(HoursPerDay, Line, X, Start, "<="&date, End, ">="&date)` versus capacity, with a rule highlighting overload (> 100%). Link to dependencies (Start = previous End + 1) for sequencing, and to changeover time. Excel is fine for short-term finite scheduling on a handful of lines; at scale use APS tools.

### Example
Job J1: 1,200 units at 400 units/day = 3 days; starting Monday 5-Oct-2026 on a five-day week: End = WORKDAY(5-Oct, 3-1) = Wednesday 7-Oct. J2 follows from 8-Oct for 2 days, ending Fri 9-Oct. Line capacity 8 hours/day; J1 uses 8 h/day, so load = 100%; if J3 is added on the same line on 6-Oct, load = 16 h / 8 h = 200%, shown in red.

### In the news
See news box. AI agents can draw a Gantt, but capacity and sequencing logic must be checked by the planner.

### Interview angle
> [!question] How it is asked
> "How would you build a production plan and visual schedule in Excel?"

> [!tip] Strong answer includes
> - Inputs (rate, quantity, holidays) and WORKDAY for end dates
> - Gantt method (conditional formatting or stacked bar)
> - Resource-load check vs capacity
> - Limits: finite capacity, changeovers; when to move to ERP/APS

---

## 3. OEE Calculator
> 🔴 Tier 1 · _Tracker hint:_ Availability × Performance × Quality; auto-trend chart; MTTR/MTBF log

### Definition
**Overall Equipment Effectiveness** measures how well planned production time is used.

$$OEE=A\times P\times Q$$

- Availability A = Run time / Planned production time (run time = planned time minus stops)
- Performance P = (Ideal cycle time x Total count) / Run time
- Quality Q = Good count / Total count

World-class benchmark is often quoted as about 85%. Excel build: input sheet (date, shift, line, planned minutes, downtime minutes, ideal cycle time, total units, rejects), calculation columns, a **trend chart** (line of daily OEE vs target) and a **loss waterfall** (availability, performance and quality losses). Add a downtime log with reason codes; summarise with a pivot (Pareto of downtime). Reliability metrics: **MTBF** = operating time / number of failures; **MTTR** = total repair time / number of failures; Availability = MTBF / (MTBF + MTTR). Use SUMIFS across shifts and weight by time, not an average of daily percentages.

### Example
Shift 480 min planned; 60 min stops; ideal cycle 1 min/unit; produced 350; rejects 14. Run time = 420. A = 420/480 = 87.5%. P = (1 x 350)/420 = 83.3%. Good = 336; Q = 336/350 = 96%. OEE = 0.875 x 0.8333 x 0.96 = 70.0% (check: good units x ideal time / planned time = 336/480 = 70%). With 3 failures: MTBF = 420/3 = 140 min, MTTR = 60/3 = 20 min, A = 140/160 = 87.5%.

### In the news
See news box. Python in Excel can extend OEE analytics, but the Excel calculator remains how most shop floors and ops reviews work.

### Interview angle
> [!question] How it is asked
> "How is OEE calculated, and how would you track and improve it in Excel?"

> [!tip] Strong answer includes
> - A x P x Q with definitions and a worked example
> - The six big losses grouped into the three factors
> - Time-weighted aggregation, trend chart, downtime Pareto
> - MTBF/MTTR and improvement actions (SMED, TPM)

---

## 4. Supplier Scorecard
> 🔴 Tier 1 · _Tracker hint:_ Weighted scoring: OTD 40% + Quality 30% + Lead Time 20% + Cost 10%; radar chart

### Definition
A **weighted scorecard** converts several supplier metrics into one comparable score.

$$\text{Score}=\sum_i w_i s_i,\qquad \sum_i w_i=1$$

Steps: (1) choose KPIs: on-time delivery (OTD), quality (PPM or acceptance rate), lead time, cost/price competitiveness (optionally responsiveness, compliance); (2) **normalise** each to a 0 to 100 scale (e.g. OTD % as is; quality = 100 - defect %, cost = lowest price / supplier price x 100; lead time = best lead time / supplier lead time x 100); (3) set weights summing to 100% in input cells; (4) compute `=SUMPRODUCT(weights, scores)`; (5) rank with `RANK.EQ`/`SORTBY`; (6) rating bands (e.g. >=85 Preferred, 70 to 84 Approved, <70 Probation); (7) **radar chart** to compare profiles. Pull data from PO/GRN with SUMIFS. Weights should reflect strategy, and ranking should be tested for sensitivity to weights.

### Example
Supplier X: OTD 90, Quality 80, Lead time 70, Cost 60. Score = 0.40 x 90 + 0.30 x 80 + 0.20 x 70 + 0.10 x 60 = 36 + 24 + 14 + 6 = 80. Supplier Y: 80, 90, 75, 85 gives 32 + 27 + 15 + 8.5 = 82.5; Y ranks higher despite X's better delivery. If OTD weight rises to 50% (quality 20%): X = 45 + 16 + 14 + 6 = 81; Y = 40 + 18 + 15 + 8.5 = 81.5, still Y but the gap narrows, which is a sensitivity insight.

### In the news
See news box. Whether built by hand or agent, the weights embody sourcing strategy and need sign-off.

### Interview angle
> [!question] How it is asked
> "How would you evaluate and rank suppliers objectively?"

> [!tip] Strong answer includes
> - KPI choice, normalisation, weights, SUMPRODUCT
> - Rating bands and a radar chart
> - Sensitivity of rank to weights
> - Link to total cost of ownership and risk, and corrective-action process

---

## 5. Demand Forecast Model
> 🔴 Tier 1 · _Tracker hint:_ Historical data + FORECAST.ETS(); seasonality; error tracking (MAPE)

### Definition
Excel offers built-in forecasting functions:

```excel
=FORECAST.ETS(target_date, values, timeline, [seasonality], [data_completion], [aggregation])
=FORECAST.ETS.SEASONALITY(values, timeline)
=FORECAST.ETS.CONFINT(target_date, values, timeline, [confidence_level])
=FORECAST.LINEAR(x, known_y, known_x)
```
**FORECAST.ETS** uses the AAA version of exponential triple smoothing (level, trend and seasonality); the timeline must have consistent steps (daily, monthly). Seasonality is auto-detected (1) or set (e.g. 12 for monthly data). The **Forecast Sheet** (Data > Forecast Sheet) builds table and chart with confidence bounds. Track accuracy:

$$MAPE=\frac{1}{n}\sum\frac{|A_t-F_t|}{A_t},\quad MAD=\frac{1}{n}\sum|A_t-F_t|,\quad Bias=\frac{\sum(F_t-A_t)}{n}$$

Excel: `=SUMPRODUCT(ABS((A2:A13-B2:B13)/A2:A13))/COUNT(A2:A13)`. Compare against a naive or moving-average baseline; hold out recent periods to test. MAPE breaks down with zeros and low volumes (use WAPE). Forecast at the right aggregation level.

### Example
Actuals 100, 200, 50; forecasts 110, 170, 55. APEs: |100-110|/100 = 10%; |200-170|/200 = 15%; |50-55|/50 = 10%. MAPE = (10 + 15 + 10)/3 = 11.67%. MAD = (10 + 30 + 5)/3 = 15 units. Bias = (10 - 30 + 5)/3 = -5, so on average it under-forecasts by 5 units.

### In the news
See news box. Python in Excel opens richer forecasting libraries, yet FORECAST.ETS plus MAPE is the standard Excel-only answer.

### Interview angle
> [!question] How it is asked
> "How would you forecast demand in Excel and measure accuracy?"

> [!tip] Strong answer includes
> - FORECAST.ETS with seasonality, timeline requirements
> - MAPE, MAD and bias with formulas
> - Baseline comparison and holdout
> - Limitations (promotions, new products, MAPE with zeros)

---

## 6. ABC Analysis in Excel
> 🔴 Tier 1 · _Tracker hint:_ Sort by revenue descending; cumulative %; IF/IFS for A/B/C classification

### Definition
**ABC analysis** ranks items by annual consumption value (usage x unit cost) to focus control: **A** items (about 70 to 80% of value, ~10 to 20% of items), **B** (next ~15 to 20%), **C** (last ~5%, ~50% of items). Excel steps:

1. Annual value = Qty x Cost.
2. Sort descending: `=SORTBY(A2:C100, C2:C100, -1)` (or Data > Sort).
3. Share % = value / total; cumulative % = running sum: `=SUM($C$2:C2)/SUM($C$2:$C$100)`.
4. Classify: `=IFS(D2<=0.8,"A", D2<=0.95,"B", TRUE,"C")`.
5. Summarise by class with a pivot (items count and value %) and chart (Pareto).

Nuance: the item that crosses a threshold can be classified using the cumulative % **before** it is added (`D2-C2/total`) so that the first item is always A. Thresholds are policy choices. Extend to **XYZ** (demand variability by coefficient of variation) for a 9-box policy. Policy: A = tight control, frequent review, low safety stock; C = simple rules, bulk ordering.

### Example
Revenue (₹ lakh): 500, 250, 100, 80, 40, 20, 10 (total 1,000). Cumulative %: 50, 75, 85, 93, 97, 99, 100. With 80% and 95% cut-offs: items 1 and 2 are A (75% of value from 2 of 7 items, 29%); items 3 and 4 are B (cum 85%, 93%); items 5 to 7 are C. Item 5 at 97% exceeds 95%, so C.

### In the news
See news box. Classification logic is simple enough for an agent to draft; the cut-offs are business policy you must justify.

### Interview angle
> [!question] How it is asked
> "How would you classify 5,000 SKUs for inventory control in Excel?"

> [!tip] Strong answer includes
> - Annual consumption value, sort, cumulative %, IFS thresholds
> - Policy differences between A, B and C
> - XYZ overlay for demand variability
> - Caveat: value is not criticality (add VED)

---

## 7. MIS Dashboard Structure
> 🔴 Tier 1 · _Tracker hint:_ Summary sheet (KPIs) + detail sheets (raw data) + chart sheets; hyperlinks

### Definition
An **MIS (Management Information System) report** gives managers a regular, consistent view of performance. A robust workbook structure:

| Sheet | Purpose |
|---|---|
| README / Index | Purpose, KPI definitions, owner, refresh steps, hyperlinks |
| Summary | KPI tiles, RAG status, key charts (the only sheet management reads) |
| Calc | Pivots / SUMIFS feeding the summary |
| Data sheets | Raw monthly/transaction data as Tables (one per source) |
| Charts | Detail trends if needed |
| Lists / Settings | Dropdown lists, targets, thresholds, as-of date |

Navigation: `=HYPERLINK("#'Summary'!A1","Go to Summary")`, and a back-link on each sheet. Keep one-way flow (data to calc to summary), colour-code tabs, and put reconciliation checks on the summary. Use named ranges and consistent formats; protect formulas; use Power Query for refreshes. Typical operations KPIs: OTIF, inventory days, OEE, cost per unit, backlog, fill rate, downtime. Publish as PDF for senior leaders.

### Example
Monthly plant MIS: Data sheets hold production, dispatch and quality tables (maybe 20,000 rows). Calc sheet pivots feed the Summary: OTIF 94% (target 95%, amber), OEE 72% (target 75%, amber), Inventory days 38 (target 40, green: lower is better). A checks cell compares dispatch units on the Summary to the data table total; mismatch shows "CHECK".

### In the news
See news box. Agent Mode can assemble sheets, but a clear architecture and README are what keep an MIS trustworthy for the next analyst.

### Interview angle
> [!question] How it is asked
> "How would you structure a monthly MIS workbook for a plant head?"

> [!tip] Strong answer includes
> - Layered structure (data, calc, summary) and one-way flow
> - KPI definitions, targets, RAG
> - Navigation, checks, protection, refresh method
> - Mention Power Query/Power BI for scale

---

## 8. Variance Analysis Template
> 🔴 Tier 1 · _Tracker hint:_ Actual vs Budget vs Prior Year; absolute & % variance; traffic lights

### Definition
**Variance analysis** compares actual performance with a benchmark (budget/plan, forecast, prior year) and explains the differences.

```excel
Absolute variance = Actual - Budget
% variance        = (Actual - Budget) / ABS(Budget)
```
Sign convention: for **revenue/profit**, positive = favourable; for **costs**, positive (actual > budget) = **adverse**. Use `=IF(Budget=0,"n/a",(Actual-Budget)/ABS(Budget))` to avoid division errors. Add traffic lights with conditional formatting or an icon set (e.g. green if favourable, amber within 5% adverse, red beyond). Columns: Line item, Actual, Budget, Var, Var %, Prior year, YoY Var, YoY %, Comment/Root cause, Action owner. Decompose operations variances: **price variance** = (Actual price - Std price) x Actual qty; **usage/volume variance** = (Actual qty - Std qty) x Std price. Use YTD and month views; link commentary to a driver, not a restatement of numbers. A **waterfall** from budget to actual makes the story clear.

### Example
Sales: Actual 110, Budget 100, Prior year 95. Variance vs budget = +10 (+10%); vs PY = +15 (+15.8% = 15/95). Raw-material cost: budget ₹500 (100 units at 5), actual 520 (110 units at 4.727). Price variance = (4.727 - 5) x 110 = -30 (favourable); usage/volume variance = (110 - 100) x 5 = +50 (adverse); net = +20 (adverse), matching 520 - 500. Check: -30 + 50 = 20 ✓ (volume rose with sales, so flex the budget before judging).

### In the news
See news box. AI can calculate variances instantly; the value is in the root-cause comment and the action.

### Interview angle
> [!question] How it is asked
> "Costs are 8% over budget this month. How do you analyse it?"

> [!tip] Strong answer includes
> - Variance formulas, sign convention for cost vs revenue
> - Price vs volume (usage) decomposition and flexing budget
> - Traffic-light thresholds and comment column
> - Action owners and follow-up

---

## 9. Pareto Chart
> 🔴 Tier 1 · _Tracker hint:_ Sort by frequency desc; cumulative %; dual axis combo chart; 80/20 line

### Definition
A **Pareto chart** shows causes ranked by frequency (columns, descending) with a cumulative % line on a secondary axis (0 to 100%), identifying the "vital few" causes. Based on the Pareto principle (roughly 80% of effects from 20% of causes; not an exact law). Build in Excel:

1. Tabulate causes and counts (pivot or `COUNTIF`); sort descending (put "Other" last).
2. Cumulative % = running sum / total: `=SUM($B$2:B2)/SUM($B$2:$B$7)`.
3. Select data > **Insert > Recommended Charts / Combo**; counts as clustered columns, cumulative % as line with markers on the **secondary axis**; set secondary axis max to 100%.
4. Add an **80% reference line** (a constant series) and reduce gap width to 0 to 10%.
Excel 2016+ also offers **Insert > Statistic Chart > Pareto** that sorts automatically. Use in quality (defects), maintenance (downtime causes), customer complaints. Weight by cost or time, not just count, when severity differs.

### Example
Defects: Scratch 50, Dent 30, Crack 10, Misprint 6, Other 4 (total 100). Cumulative %: 50%, 80%, 90%, 96%, 100%. Scratch and Dent (2 of 5 categories) cause 80% of defects, so improvement effort goes there first. Fixing both with 70% effectiveness cuts defects by 0.7 x 80 = 56 units, 56%.

### In the news
See news box. Whatever tool draws the chart, the managerial step (what to fix first) is unchanged.

### Interview angle
> [!question] How it is asked
> "Plant has 5 defect types. How do you decide what to tackle first, and how would you show it in Excel?"

> [!tip] Strong answer includes
> - Sort, cumulative %, combo chart with secondary axis
> - 80/20 interpretation and caveats (severity, cost-weighting)
> - Use in Six Sigma/problem solving (DMAIC Analyse phase)
> - Follow-up: root cause (5 Whys, fishbone) and re-check the Pareto after action

---

## 10. Cost Model in Excel
> 🔴 Tier 1 · _Tracker hint:_ Fixed vs variable cost breakdown; unit cost; contribution margin; break-even

### Definition
A **cost model** separates **fixed** costs (rent, salaries, depreciation; constant in the relevant range) from **variable** costs (materials, direct labour, freight; proportional to volume) and derives unit economics.

Total cost = FC + VC x Q. Average (unit) cost = FC/Q + VC. Contribution per unit = P - VC; CM% = (P - VC)/P. Break-even Q = FC/(P - VC). Operating profit = CM x Q - FC. Build with inputs (price, VC per unit, FC, volume) in blue, calculations and outputs, a **Data Table** for volume sensitivity, and a chart (cost and revenue lines). **Semi-variable** costs (power, maintenance) split using the high-low method: VC/unit = (Cost_high - Cost_low)/(Q_high - Q_low). Add **activity-based** drivers where overhead depends on batches or setups. Remember costs are only fixed within a relevant range; step costs appear when capacity is added.

### Example
Price ₹100, VC ₹60/unit, FC ₹200,000/month, volume 10,000. Revenue 1,000,000; VC 600,000; contribution 400,000 (CM% 40%); profit 200,000. Unit cost = (200,000 + 600,000)/10,000 = ₹80. Break-even = 200,000/40 = 5,000 units. At 6,000 units: unit cost = 200,000/6,000 + 60 = 93.33. High-low: power ₹90,000 at 8,000 units and ₹70,000 at 4,000 units gives VC = 20,000/4,000 = ₹5 per unit and fixed power = 90,000 - 40,000 = ₹50,000.

### In the news
See news box. Cost-model outputs drive pricing and make-or-buy; the model's assumptions deserve scrutiny whoever built it.

### Interview angle
> [!question] How it is asked
> "Build a cost model for a new product line and tell me the break-even and the unit cost at different volumes."

> [!tip] Strong answer includes
> - Fixed vs variable vs semi-variable and the relevant range
> - Unit cost falls with volume; contribution margin and break-even
> - Sensitivity table on volume and price
> - Link to pricing, make-or-buy and capacity decisions

---

## 11. ⭐ Advanced: Safety Stock, Service Level and Reorder Engine
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Upgrade the inventory tracker with statistically based safety stock.

$$SS=z\cdot\sigma_d\sqrt{L}\ \ (\text{demand variability only}),\qquad SS=z\sqrt{L\sigma_d^2+d^2\sigma_L^2}$$

$$ROP=dL+SS$$

where d = average daily demand, $\sigma_d$ = std dev of daily demand, L = lead time (days), $\sigma_L$ = std dev of lead time, and z = `NORM.S.INV(service level)`.

```excel
=NORM.S.INV(0.95)                          -- 1.645
=NORM.S.INV(0.95) * STDEV.S(D2:D91) * SQRT(L)
```
Compute demand statistics from history with `AVERAGE` and `STDEV.S` per SKU (pivot/`AVERAGEIFS`; array `STDEV.S(FILTER(...))`). Combine with ABC: higher service level for A items, lower for C. Provide a data table of service level vs safety stock vs holding cost to show the cost of an extra point of service. Cycle service level is not fill rate; they differ.

### Example
Daily demand mean 20, sd 10; lead time 9 days; service level 95% (z = 1.645). SS = 1.645 x 10 x sqrt(9) = 1.645 x 10 x 3 = 49.35, so about 50. ROP = 20 x 9 + 49.35 = 229.35, so reorder at about 230. Raising service to 99% (z = 2.326) gives SS = 69.8 (about 70), 41% more safety stock for 4 more points of service.

### In the news
See news box. Probability-based buffers matter again after recent supply disruptions; the Excel engine shows the cost of resilience.

### Interview angle
> [!question] How it is asked
> "How do you set safety stock for an item with variable demand and lead time?"

> [!tip] Strong answer includes
> - SS formula, z for the service level, ROP = dL + SS
> - Both demand and lead-time variability
> - Differentiate service by ABC class; cost of higher service
> - Distinguish cycle service level from fill rate

---

## 12. ⭐ Advanced: Automating Ops Reports with Power Query and ERP Exports
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Most operations reports begin with ERP extracts (SAP, Oracle, Tally) in Excel or CSV. A repeatable pipeline:

1. **Export** standard reports (e.g. SAP MB52 for stock by plant and storage location, ME2M for POs by material, MB51 for material documents; confirm the report names in your ERP).
2. **Power Query**: Data > Get Data > From Folder; promote headers, set types, trim and clean, filter, remove totals rows, unpivot if needed, merge with master data (material, vendor).
3. **Data Model/Calc sheet**: pivot or SUMIFS; **KPIs** (OTIF, stock cover, ageing buckets, backlog).
4. **Refresh All** weekly; checks reconcile totals to the ERP screen.
5. **Distribution**: PDF/Power BI/e-mail; Office Scripts or Power Automate for scheduling.

Controls: version stamp, as-of date, parameterised folder path, error handling for missing files, audit trail of changes. Typical KPIs: **stock cover (days)** = Stock / Average daily consumption; **ageing** buckets by `TODAY() - receipt date`; **OTIF** = on-time-in-full lines / total lines.

### Example
Weekly stock report: the SAP export has 25,000 rows. Query removes blank and total rows, converts quantity to numbers, merges with ABC class. Stock cover for SKU 1001 = 350 units / 20 per day = 17.5 days; with lead time 7 days it has ample cover. The whole refresh takes about a click instead of an hour of manual clean-up (qualitative, not a measured figure).

### In the news
See news box. Automation of recurring reports, whether through Power Query or agents, frees time for analysis if outputs are validated.

### Interview angle
> [!question] How it is asked
> "You get a weekly ERP stock extract and need a management report. How do you make it repeatable and error-free?"

> [!tip] Strong answer includes
> - Folder-based Power Query with parameters and typed columns
> - Reconciliation of totals to the ERP source
> - KPI definitions (stock cover, OTIF, ageing)
> - Scheduling and ownership, and when to move to Power BI

---
## 🔗 Go deeper: expansion notes
- [[187 Excel Interview Problem Bank & Case Exercises|Excel Interview Problem Bank & Case Exercises]]
- [[188 Financial Modelling in Excel|Financial Modelling in Excel]]
- [[189 VBA, Macros & Office Scripts Basics|VBA, Macros & Office Scripts Basics]]
