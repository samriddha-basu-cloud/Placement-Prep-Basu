---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Supply Chain Analytics & KPIs"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 16
---
# Supply Chain Analytics & KPIs

⬅ [[011 Quality Management (TQM)]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[013 ERP & Enterprise Systems (SAP-Oracle)]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. OTIF (On Time In Full)]]
2. [[#2. Fill Rate]]
3. [[#3. Perfect Order Rate]]
4. [[#4. Forecast Accuracy & Bias]]
5. [[#5. Inventory Turns]]
6. [[#6. Days Inventory Outstanding (DIO)]]
7. [[#7. Cash-to-Cash Cycle Time]]
8. [[#8. Supplier OTD %]]
9. [[#9. Order Cycle Time]]
10. [[#10. Demand Forecast Error Tracking]]
11. [[#11. KPI Dashboard Design]]
12. [[#12. Power BI for SCM]]
13. [[#13. SQL for SCM Analytics]]
14. [[#14. Scenario & Sensitivity Analysis]]
15. [[#15. ⭐ Advanced: KPI Trees & the Diagnostic Case Approach]]
16. [[#16. ⭐ Advanced: ABC-XYZ Segmentation & Forecastability]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Measuring supply chains, from India's logistics benchmark to Gartner's Top 25
> **India's first systematic logistics-cost benchmark (Sep 2025).** The DPIIT-NCAER study measured logistics cost at **7.97% of GDP for FY2023-24 (about ₹24.01 lakh crore)**, versus the older "13–14%" perception. It reported per-tonne-km costs of **₹1.96 (rail), ₹1.80 (coastal), ₹3.78 (road) and ₹72 (air)**, and small firms spending **16.9% of output** on logistics against **7.6%** for large firms. The study used primary surveys of 500+ industry users and 3,000 service providers. ([Logistics Insider](https://www.logisticsinsider.in/indias-logistics-cost-at-7-9-of-gdp-report/))
>
> **Gartner Global Supply Chain Top 25 (20 Jun 2025).** Schneider Electric ranked #1 for the third year running, NVIDIA rose to #2, and Amazon, Apple, P&G and Unilever kept "Masters" status. Gartner's analyst said leaders differentiate through AI, autonomous operations and resource (water) stewardship. The ranking uses composite financial and non-financial scores; the article fetched does not detail the formula. ([Supply Chain Digital](https://supplychaindigital.com/articles/gartners-top-25-global-supply-chain-2025))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. OTIF (On Time In Full)
> 🔴 Tier 1 · _Tracker hint:_ Primary delivery KPI; formula, target benchmarks, root cause drill

### Definition
**OTIF** measures the share of orders (or lines) delivered **both** on time **and** in full against the customer's request or agreed date:

$$OTIF\% = \frac{\text{Orders delivered on time AND in full}}{\text{Total orders due}} \times 100$$

Definitions must be agreed: *on time* (exact date, or a window such as -1/+0 days), *in full* (100% of ordered quantity, or within a tolerance), and the *unit* (order, line or case). Large retailers set OTIF targets in the high-90s and apply penalties, so suppliers need precise definitions.

Because it needs both conditions, OTIF is stricter than either on-time % or in-full %. Root-cause drill: split into **OT failures** (late) and **IF failures** (short), then Pareto by supplier/plant/lane/SKU/customer and by cause code (stock-out, production miss, picking error, transport delay, customer-side rejection, system error).

### Example
1,000 orders: 920 on time, 950 in full, and 880 both. OTIF = 880/1000 = **88%**. Note that 0.92 x 0.95 = 87.4%, close to 88%, but OTIF is the *actual joint* count, not the product, unless failures are independent. Breakdown: on time but short = 920-880 = 40; in full but late = 950-880 = 70; both late and short = 1000-880-40-70 = 10.

### In the news
See news box. NCAER's 7.97% benchmark shows India's logistics cost is improving; OTIF is the customer-facing counterpart that tells whether the lower cost is also reliable service.

### Interview angle
> [!question] How it is asked
> "OTIF has dropped from 95% to 85%. How would you diagnose it?"

> [!tip] Strong answer includes
> - Clarify the definition (window, tolerance, unit) first
> - Split into on-time vs in-full and drill by customer, SKU, DC, lane, supplier
> - Pareto causes, then separate internal (stock, picking) from external (carrier, customer)
> - Corrective actions with owners, and a leading indicator (for example inventory availability, pick accuracy)

---

## 2. Fill Rate
> 🔴 Tier 1 · _Tracker hint:_ Order fill rate vs line fill rate vs unit fill rate

### Definition
Fill rate measures how much of demand is met **from stock, without delay or backorder**. Three levels:

- **Order fill rate** = complete orders shipped / orders received (strictest).
- **Line fill rate** = order lines shipped complete / lines ordered.
- **Unit (item) fill rate** = units shipped / units ordered (most lenient).

Unit fill rate is always at least line fill rate, which is at least order fill rate. Fill rate links to safety stock via the **service level**: cycle service level (probability of no stock-out per cycle, from $z$) differs from fill rate (fraction of demand met), computed from the expected shortage per cycle: $\text{Fill rate} = 1 - \frac{ESC}{Q}$, where ESC is expected shortage per replenishment cycle and $Q$ is the order quantity.

### Example
4 orders. A: 3 lines (100, 50, 20 units), shipped 100, 50, 10. B: 2 lines (40, 40), shipped 40, 40. C: 1 line (30), shipped 0. D: 4 lines (10 each), shipped all.
- Order fill = complete orders B and D = 2/4 = **50%**.
- Line fill: complete lines = A 2 + B 2 + C 0 + D 4 = 8 of 10 lines = **80%**.
- Unit fill: ordered 170+80+30+40 = 320, shipped 160+80+0+40 = 280, so 280/320 = **87.5%**.

### In the news
See news box. Gartner's leaders pair high service with low inventory; fill rate is the service half of that balance.

### Interview angle
> [!question] How it is asked
> "What is the difference between fill rate and service level?" or "Which fill rate would you report to the board?"

> [!tip] Strong answer includes
> - Three levels with formulas and the ordering of strictness
> - Cycle service level vs fill rate distinction
> - Choose by customer expectation (retail replenishment: line; B2B project orders: order fill)
> - Trade-off with inventory, and segment SKUs by importance

---

## 3. Perfect Order Rate
> 🔴 Tier 1 · _Tracker hint:_ % orders with no errors across delivery, quality, docs, invoicing

### Definition
**Perfect Order Rate (POR)** is the percentage of orders delivered with **no error at any stage**: on time, in full, damage-free, with correct documentation and invoice (a SCOR reliability metric).

$$POR = \%\text{On-time} \times \%\text{In-full} \times \%\text{Damage-free} \times \%\text{Correct docs/invoice}$$

(multiply when the errors are independent; otherwise count orders with all conditions met). Because the conditions compound, a chain with four 95% steps has POR $= 0.95^4 = 81.5\%$. Best used with a **defect (error) tree** by category to pin the weakest link. POR is the metric that best captures the customer experience, and drives costs through credit notes, re-deliveries and disputes.

### Example
On-time 96%, in-full 97%, damage-free 99%, correct documents 98%: POR = 0.96 x 0.97 x 0.99 x 0.98 = **90.3%**. Even with every component at 96% or above, one order in ten has some error. Raising only on-time from 96% to 99% lifts POR to 0.99 x 0.97 x 0.99 x 0.98 = 93.2%.

### In the news
See news box. Top-ranked chains in Gartner's list are those that combine reliability with efficiency; POR is the operational measure of that reliability.

### Interview angle
> [!question] How it is asked
> "Why is the perfect order rate much lower than each of its components?"

> [!tip] Strong answer includes
> - The four or five components and the multiplication logic
> - The compounding example ($0.95^4$)
> - Cost of imperfect orders (returns, credit notes, disputes)
> - Improvement via root-cause by component and process automation of documents

---

## 4. Forecast Accuracy & Bias
> 🔴 Tier 1 · _Tracker hint:_ 1 - MAPE; positive vs negative bias; consequences

### Definition
For actual $A_t$ and forecast $F_t$:

$$MAPE = \frac{1}{n}\sum \frac{|A_t - F_t|}{A_t}, \qquad \text{Accuracy} = 1 - MAPE$$

$$WMAPE = \frac{\sum |A_t - F_t|}{\sum A_t}, \qquad \text{Bias} = \frac{\sum (F_t - A_t)}{\sum A_t}$$

- MAPE explodes when actuals are near zero; **WMAPE** (volume-weighted) is preferred for intermittent items.
- **Bias** shows direction: positive = over-forecasting (excess inventory, obsolescence), negative = under-forecasting (stock-outs, expediting). Error can be small in MAPE but biased; bias is systematic and fixable.
- **Tracking signal** = RSFE / MAD (running sum of forecast errors over mean absolute deviation); outside about ±4 signals bias.

### Example
Actual: 100, 120, 80, 100. Forecast: 110, 100, 90, 110. Errors F-A: +10, -20, +10, +10. Absolute % errors: 10%, 16.7%, 12.5%, 10% → MAPE = 49.17/4 = **12.3%**, accuracy 87.7%. WMAPE = 50/400 = 12.5%. Bias = +10/400 = **+2.5%** (over-forecast). MAD = 50/4 = 12.5; RSFE = +10; tracking signal = 10/12.5 = **0.8** (within limits).

### In the news
See news box. The leading chains in Gartner's ranking invest in AI and analytics; better forecast accuracy and lower bias are a prime use case.

### Interview angle
> [!question] How it is asked
> "Forecast accuracy is 85% but we still have stock-outs and excess. How come?"

> [!tip] Strong answer includes
> - Accuracy aggregated vs SKU-location level; level matters
> - Bias vs error; mix of over- and under-forecast in different SKUs
> - Weighted metrics and forecast value added
> - Action: segment (ABC-XYZ), consensus process, remove sales-target inflation

---

## 5. Inventory Turns
> 🔴 Tier 1 · _Tracker hint:_ COGS/Avg inventory; industry benchmarks; impact on working capital

### Definition
$$\text{Inventory turns} = \frac{\text{COGS}}{\text{Average inventory}}$$

(use COGS, not sales, so numerator and denominator are both at cost; average inventory = (opening + closing)/2 or a monthly average). Higher turns mean faster conversion to sales and lower holding cost, unless stocks are so lean that service suffers. Benchmarks differ by industry: grocery and fast-fashion retail turn many times a year, heavy machinery and aerospace turn only a few, so compare with peers, not across industries. Turns improve with shorter lead times, better forecasting, SKU rationalisation and lower batch sizes. Inventory carrying cost (capital, storage, insurance, obsolescence) commonly runs about 20-30% a year of inventory value as a rule of thumb.

### Example
COGS ₹600 crore, average inventory ₹100 crore: turns = **6.0**. Raise turns to 8: inventory = 600/8 = ₹75 crore, releasing **₹25 crore** of cash. At a 10% cost of capital the saving is ₹2.5 crore a year, before storage and obsolescence savings.

### In the news
See news box. NCAER found small firms bear much higher logistics costs; inventory held to buffer unreliable logistics is a part of that burden.

### Interview angle
> [!question] How it is asked
> "Inventory turns have fallen from 8 to 6. What could be happening and what do you do?"

> [!tip] Strong answer includes
> - Formula and why COGS is used
> - Hypotheses: demand drop, slow movers, over-buying, longer lead times, mix change
> - Segment-level analysis (ABC, ageing, DIO by category)
> - Link to cash released and service level trade-off

---

## 6. Days Inventory Outstanding (DIO)
> 🔴 Tier 1 · _Tracker hint:_ Avg inventory/(COGS/365); cash cycle link

### Definition
$$DIO = \frac{\text{Average inventory}}{\text{COGS}/365} = \frac{365}{\text{Inventory turns}}$$

DIO states how many days of cost of sales sit in inventory. It is the first leg of the cash-to-cash cycle. Disaggregate by raw material, WIP and finished goods to find where days accumulate. Use days of supply on a forward-looking basis (stock divided by forecast daily demand) for planning, since DIO is backward-looking.

### Example
Average inventory ₹100 crore, COGS ₹600 crore: COGS per day = 600/365 = ₹1.644 crore; DIO = 100/1.644 = **60.8 days** (= 365/6). Reducing DIO by 10 days releases about 10 x 1.644 = **₹16.4 crore** of cash.

### In the news
See news box. Gartner's Top 25 ranking is a composite of financial and non-financial measures (the exact weightings were not in the article read); DIO is the sort of efficiency measure peers are compared on.

### Interview angle
> [!question] How it is asked
> "How would you cut DIO by 15 days without hurting service?"

> [!tip] Strong answer includes
> - Formula and relation to turns
> - Break down by RM/WIP/FG and by ABC class
> - Levers: safety-stock policy, lead-time cuts, batch sizes, SKU pruning, VMI/consignment
> - Quantify the cash released and monitor fill rate

---

## 7. Cash-to-Cash Cycle Time
> 🔴 Tier 1 · _Tracker hint:_ DIO + DSO - DPO; working capital optimization

### Definition
$$C2C = DIO + DSO - DPO$$

- **DSO** (days sales outstanding) = Average receivables / (Sales/365)
- **DPO** (days payables outstanding) = Average payables / (COGS/365)

It measures the days between paying suppliers and collecting from customers. A shorter or negative cycle (as in some retailers and e-commerce marketplaces) means suppliers finance the business. Levers: reduce DIO (inventory), reduce DSO (invoicing accuracy, collections, early-pay discounts), increase DPO (terms negotiation, supply chain finance, but without damaging supplier health; India's MSME payment rule requires payment within 45 days of acceptance for MSE suppliers (Section 43B(h) of the Income-tax Act)).

### Example
DIO 61, DSO 45, DPO 50: C2C = 61 + 45 - 50 = **56 days**. With COGS ₹600 crore (₹1.644 crore per day), cutting DIO by 10 days and DSO by 5 days: C2C = 41 days; working capital released about 15 x 1.644 = **₹24.7 crore** (approximating all days at COGS).

### In the news
See news box. Resilient leaders also protect supplier liquidity; stretching DPO aggressively can backfire in a disruption.

### Interview angle
> [!question] How it is asked
> "A company's C2C cycle is 90 days versus 60 for the peer. How do you close the gap?"

> [!tip] Strong answer includes
> - The three components and what drives each
> - Benchmarking and finding which component explains the gap
> - Levers by component, and trade-offs (service, supplier relationships, MSME 45-day rule)
> - Cash impact quantified

---

## 8. Supplier OTD %
> 🔴 Tier 1 · _Tracker hint:_ On-time delivery from suppliers; scorecarding

### Definition
$$\text{Supplier OTD}\% = \frac{\text{PO lines received on or before the promised date (within window)}}{\text{PO lines due}} \times 100$$

Define the reference date (supplier's confirmed date vs requested date) and window (for example -2/+0 days), and whether early deliveries count as on time (early can also hurt: space and cash). Combine with **in-full**, quality (PPM defects, rejection %), cost (price variance), responsiveness and risk in a **supplier scorecard** with weights; use for tiering, business awards, performance reviews and development plans (see the procurement and sourcing notes).

### Example
200 PO lines due; 170 received within the window: OTD = **85%**. Scorecard weights: quality 40%, delivery 30%, cost 20%, service 10%. Scores: 95, 85, 80, 90. Weighted score = 0.4 x 95 + 0.3 x 85 + 0.2 x 80 + 0.1 x 90 = 38 + 25.5 + 16 + 9 = **88.5**.

### In the news
See news box. Gartner's Top 25 leaders manage supplier risk with data; a supplier scorecard is the basic version of that transparency.

### Interview angle
> [!question] How it is asked
> "How would you build a supplier scorecard and what would you do about a supplier at 70% OTD?"

> [!tip] Strong answer includes
> - Definition with window and the early-delivery rule
> - Balanced criteria and weights tied to strategy
> - Diagnose root cause (supplier capacity vs our late POs vs transport)
> - Actions: joint improvement plan, safety stock, dual-sourcing, escalation path

---

## 9. Order Cycle Time
> 🔴 Tier 1 · _Tracker hint:_ Order placement to delivery; customer experience KPI

### Definition
**Order cycle time (OCT)** = time from customer order placement to receipt of goods. Components: order entry and credit check → order processing and allocation → picking, packing → dispatch wait (cut-off) → transit → delivery and unloading. Report **mean, median and a percentile (P90/P95)** and the **variability**: customers feel reliability, not only the average. Compare with promised lead time and measure **order-to-ship** (internal) and **ship-to-deliver** (carrier) separately. For e-commerce and quick-commerce, minutes and hours matter; for B2B, days. Shorter cycle time reduces safety stock held downstream because of a shorter forecasting horizon.

### Example
Order processing 4 h + picking and packing 8 h + wait for dispatch cut-off 12 h + transit 48 h = **72 hours (3 days)**. Removing the 12-hour wait by adding a second dispatch run cuts OCT by 17% (12/72). If P90 is 5 days while the mean is 3, reliability needs work.

### In the news
See news box. India's improving logistics performance (7.97% of GDP) and quick-commerce growth push customers' expectations of delivery time down.

### Interview angle
> [!question] How it is asked
> "Customers complain about delivery time. How would you analyse the order cycle?"

> [!tip] Strong answer includes
> - Break the cycle into stages and measure each (value-added vs waiting)
> - Use percentiles and variance, not just averages
> - Quick wins: cut-off times, parallel processing, forward stocking
> - Linking to customer satisfaction and cost trade-off

---

## 10. Demand Forecast Error Tracking
> 🔴 Tier 1 · _Tracker hint:_ MAPE trending, root cause, corrective action

### Definition
Tracking is a **routine process**, not a one-time statistic:
1. Measure error at the right level and lag (for example SKU-DC-month at the **lead-time lag**, not the lag-0 forecast).
2. Trend MAPE/WMAPE and **bias** (rolling 3 and 12 months), with a **tracking signal** alert at ±4.
3. Compute **Forecast Value Added (FVA)**: compare the error of each step (naive, statistical, planner override, sales input) to see which adds value:  $FVA = Error_{previous\ step} - Error_{this\ step}$.
4. Root cause by category: promotions not planned, new items, stock-outs censoring sales, data errors, market shocks.
5. Corrective action: model changes, demand sensing, collaboration with sales, master-data fixes; assign owners and review in S&OP.

### Example
Monthly MAPE: naive forecast 20%, statistical forecast 15%, after planner overrides 17%. FVA of statistical vs naive = +5 points (good); FVA of override = 15-17 = **-2 points** (override destroys value). Action: restrict manual overrides to promotions and new products and track hit rates.

### In the news
See news box. Gartner highlights AI and autonomous operations at top chains, which includes automated forecast monitoring and exception alerts.

### Interview angle
> [!question] How it is asked
> "How would you set up a process to improve forecast accuracy over six months?"

> [!tip] Strong answer includes
> - Metrics (WMAPE, bias, FVA) and the lag at which they are measured
> - Segmentation (ABC-XYZ) with different targets
> - Root-cause logs and monthly S&OP review with accountability
> - Reduce bias first: it is the cheapest accuracy gain

---

## 11. KPI Dashboard Design
> 🔴 Tier 1 · _Tracker hint:_ Balanced scorecard, traffic light indicators, drill-down hierarchy

### Definition
A good dashboard answers "Are we on track, why not, what do I do?" within seconds.

**Principles:**
- **Few, linked KPIs** per audience: executive (6–10), functional, operational. Balance with the **Balanced Scorecard** (financial, customer, internal process, learning and growth) or **SCOR** attributes (reliability, responsiveness, agility, cost, assets).
- **Target, trend and status:** show actual vs target, a sparkline of the last 12 periods, and a **traffic light** with explicit thresholds (green at or above target, amber within an agreed band, red below).
- **Drill-down hierarchy:** network → region → DC → customer/SKU, using a **KPI tree** (for example OTIF → on-time, in-full → causes).
- **Data definitions and owners:** a KPI dictionary, refresh time, single source of truth.
- Mix **leading** (inventory availability, supplier confirmation) and **lagging** (OTIF, cost) indicators; avoid chart junk and too many colours; colour-blind-safe palettes.

### Example
OTIF target 95%: green at 95% or above, amber 92–95%, red below 92%. A reading of 93.4% shows amber; the user drills to region (South 89% red), then to DC and cause (carrier delays on two lanes), then to the action owner.

### In the news
See news box. NCAER's work shows measurement itself is a policy tool: what was not measured (logistics cost) was misjudged for years.

### Interview angle
> [!question] How it is asked
> "Design a KPI dashboard for the COO of a FMCG distributor."

> [!tip] Strong answer includes
> - Start with decisions and audience, then KPIs (service, cost, inventory, cash, quality)
> - Targets, thresholds, trends and drill-down paths
> - Data governance: definitions, owners, refresh cadence
> - Avoid vanity metrics; link each KPI to an action

---

## 12. Power BI for SCM
> 🔴 Tier 1 · _Tracker hint:_ DAX measures, slicers, drill-through, time intelligence

### Definition
Power BI model: a **star schema** with fact tables (Orders, Shipments, Inventory) and dimensions (Date, Product, Customer, Supplier, Location). Key features:
- **Measures (DAX)** are calculated on the fly in the filter context; **calculated columns** are stored per row.
- **Slicers** filter pages; **drill-through** jumps from a summary to a detail page for the selected item; **hierarchies** enable drill-down.
- **Time intelligence** needs a marked **Date table**.

```dax
Orders = COUNTROWS ( Orders )

OTIF Orders =
CALCULATE (
    COUNTROWS ( Orders ),
    Orders[OnTime] = TRUE (),
    Orders[InFull] = TRUE ()
)

OTIF % = DIVIDE ( [OTIF Orders], [Orders] )

Sales YTD = TOTALYTD ( SUM ( Sales[Amount] ), 'Date'[Date] )

Sales LY = CALCULATE ( SUM ( Sales[Amount] ), SAMEPERIODLASTYEAR ( 'Date'[Date] ) )

Sales YoY % = DIVIDE ( SUM ( Sales[Amount] ) - [Sales LY], [Sales LY] )
```

Use `DIVIDE` to avoid divide-by-zero errors; use conditional formatting for traffic lights; use Row-Level Security so regional managers see their data.

### Example
A DC dashboard: slicers for month and region; cards for OTIF %, fill rate, DIO; a line chart of OTIF % by month vs target; a matrix by customer; right-click a red customer to **drill through** to a page listing late and short orders with cause codes.

### In the news
See news box. As Gartner's leaders push AI-enabled analytics, BI tools with natural-language and AI features (such as Copilot in Power BI) are becoming the interface layer for such KPIs.

### Interview angle
> [!question] How it is asked
> "Have you used Power BI? Write a DAX measure for OTIF% or YoY growth."

> [!tip] Strong answer includes
> - Star-schema model, measures vs calculated columns
> - Correct DAX using `CALCULATE`, `DIVIDE`, `TOTALYTD` or `SAMEPERIODLASTYEAR`
> - Interactivity: slicers, drill-through, tooltips, RLS
> - Do not claim hands-on experience you lack; describe a small project honestly

---

## 13. SQL for SCM Analytics
> 🔴 Tier 1 · _Tracker hint:_ Joins for order-inventory-supplier data; window functions for trends

### Definition
Typical tables: `orders`, `order_lines`, `shipments`, `inventory`, `po_lines`, `receipts`, `suppliers`. Use **joins** to combine them, **aggregates** with `GROUP BY` for KPIs, and **window functions** for trends, ranks and running totals.

```sql
-- Supplier on-time delivery %
SELECT s.supplier_name,
       COUNT(*) AS lines_received,
       ROUND(100.0 * SUM(CASE WHEN r.receipt_date <= p.promised_date THEN 1 ELSE 0 END)
             / COUNT(*), 1) AS otd_pct
FROM po_lines p
JOIN suppliers s ON s.supplier_id = p.supplier_id
JOIN receipts  r ON r.po_line_id  = p.po_line_id
GROUP BY s.supplier_name
ORDER BY otd_pct;

-- Monthly OTIF with 3-month moving average and month-on-month change
WITH m AS (
  SELECT DATE_TRUNC('month', order_date) AS month,
         100.0 * AVG(CASE WHEN on_time AND in_full THEN 1 ELSE 0 END) AS otif
  FROM orders
  GROUP BY 1
)
SELECT month, otif,
       AVG(otif) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS otif_ma3,
       otif - LAG(otif) OVER (ORDER BY month) AS mom_change
FROM m;
```

Use `LEFT JOIN` when you must keep orders without shipments (otherwise they vanish from the KPI). `RANK() OVER (PARTITION BY region ORDER BY late_cnt DESC)` ranks within groups. `DATE_TRUNC` is PostgreSQL; use `DATEFROMPARTS` / `EOMONTH` style in SQL Server.

### Example
Find the top 3 late-delivering suppliers per plant: compute late counts in a CTE, then `ROW_NUMBER() OVER (PARTITION BY plant ORDER BY late_cnt DESC)` and filter `rn <= 3`. Stock cover per SKU: join `inventory` to a 28-day average of `order_lines` and divide.

### In the news
See news box. Gartner's leaders use data platforms at scale; SQL on the warehouse is the common denominator across the BI, forecasting and analytics tools.

### Interview angle
> [!question] How it is asked
> "Write a query to compute on-time delivery by supplier" or "Explain INNER vs LEFT JOIN and a window function use case."

> [!tip] Strong answer includes
> - Correct join type with reason (keeping unmatched rows)
> - `GROUP BY` with `CASE WHEN` to compute rates
> - Window function for trend or rank (`LAG`, moving average, `ROW_NUMBER`)
> - Check for duplicates (join fan-out) and nulls before trusting numbers

---

## 14. Scenario & Sensitivity Analysis
> 🔴 Tier 1 · _Tracker hint:_ What-if modeling in Excel; Monte Carlo basics

### Definition
- **Sensitivity analysis:** change one input at a time (demand, lead time, price, cost) and see the output; shown as a tornado chart or a **Data Table** (What-If Analysis > Data Table).
- **Scenario analysis:** change several inputs together to define coherent cases (base, optimistic, disruption); Excel **Scenario Manager**, or a scenario switch cell with `CHOOSE`/`INDEX`.
- **Goal Seek:** find the input that gives a target output.
- **Monte Carlo simulation:** draw inputs from probability distributions many times and study the distribution of outcomes. In Excel: `=NORM.INV(RAND(), mean, sd)` for a normal demand; repeat over 1,000+ rows; compute mean, percentiles, and probability of shortfall. Add-ins and Python/NumPy also work.

Use to set safety stock, size capacity, test network designs or compare supplier risk.

### Example
Demand per week ~ Normal(mean 1,000, sd 200); capacity 1,100. Probability of exceeding capacity = $1-\Phi\left(\frac{1100-1000}{200}\right) = 1-\Phi(0.5) = 1 - 0.6915 = $ **30.9%**. To cover 95% of demand: 1,000 + 1.645 x 200 = **1,329**, which is the capacity or inventory position needed. A Monte Carlo of 1,000 draws would give about the same 31% exceedance, plus the full distribution of unmet demand.

### In the news
See news box. Resilience planning rests on scenario work: Gartner's leaders attribute performance to analytics and autonomous operations; scenario models are how planners test disruptions before they happen.

### Interview angle
> [!question] How it is asked
> "How would you test whether our network plan survives a port closure or a 30% demand spike?"

> [!tip] Strong answer includes
> - Distinguish sensitivity (one variable), scenario (combination) and simulation (distributions)
> - Name Excel tools: Data Table, Scenario Manager, Goal Seek, `NORM.INV(RAND(), ...)`
> - Interpret outputs as probabilities and ranges, not a single number
> - Link to decisions: safety stock, capacity buffers, dual sourcing

---

## 15. ⭐ Advanced: KPI Trees & the Diagnostic Case Approach
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **KPI tree** decomposes a headline metric into drivers so that analysis is MECE and actions have owners.

```
OTIF
├─ On-time
│  ├─ Order processing delay
│  ├─ Pick/pack delay
│  └─ Transit delay (carrier, lane)
└─ In-full
   ├─ Stock-out at order release (forecast, replenishment)
   ├─ Pick/ship errors
   └─ Supplier short supply
```

Consulting approach for "KPI X has dropped": (1) clarify definition and period, (2) segment (product, customer, geography, time), (3) find where the gap is concentrated (Pareto), (4) test hypotheses for causes, (5) quantify impact, (6) recommend actions and track leading indicators. A **DuPont-style tree** links operational KPIs to financial outcomes (for example inventory turns → ROCE).

### Example
OTIF fell from 95% to 88%. Splitting: on-time fell by 2 points, in-full by 6 points. In-full drop is concentrated in the Western DC (in-full 78%) and in 12 SKUs (a new pack size). Hypothesis: replenishment parameters not updated for a new pack. Action: reset min/max, expedite stock, and monitor stock availability weekly.

### In the news
See news box. NCAER-style decomposition (by mode, firm size, warehousing) is exactly the kind of tree that turned "13-14%" folklore into a measured 7.97%.

### Interview angle
> [!question] How it is asked
> "On-time deliveries fell 7 points last quarter. Structure your approach."

> [!tip] Strong answer includes
> - Clarify metric definition, then a MECE tree
> - Segment by customer, region, SKU, time to locate the problem
> - Hypotheses ranked by likely impact, with the data to test each
> - Recommendation with a number, an owner and a leading indicator

---

## 16. ⭐ Advanced: ABC-XYZ Segmentation & Forecastability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**ABC** ranks SKUs by value or volume (for example A = top 80% of sales); **XYZ** ranks by demand variability using the **coefficient of variation**:

$$CV = \frac{\sigma}{\mu}$$

A common (convention-based, adjustable) rule: X when CV < 0.5, Y when 0.5 to 1.0, Z when CV > 1.0. The 3 x 3 matrix drives policy: **AX** (high value, stable) get tight forecasts and low safety stock, automatic replenishment; **AZ** (high value, erratic) need collaboration, buffer or make-to-order; **CZ** candidates for delisting or make-to-order. Targets for accuracy and service level differ by segment; one KPI target for all SKUs wastes effort.

### Example
SKU 1: monthly demand mean 200, sd 50: CV = 0.25 → X. SKU 2: mean 100, sd 120: CV = 1.2 → Z. If SKU 1 is also in the top 80% of sales it is **AX**. Safety stock $= z \sigma_L$: for service 98% ($z = 2.05$) and lead time of one month, SKU 1 needs 2.05 x 50 = **103 units**; for SKU 2 at a lower 90% service ($z = 1.28$): 1.28 x 120 = **154 units**, so a more erratic item needs more buffer even at lower service, which is why Z-items are often managed differently (make-to-order or consolidation).

### In the news
See news box. Gartner's emphasis on autonomous operations assumes policies differentiated by segment; automated planning engines apply segment rules at scale.

### Interview angle
> [!question] How it is asked
> "How would you rationalise 20,000 SKUs and set service levels?"

> [!tip] Strong answer includes
> - ABC by value/volume and XYZ by CV, with the matrix
> - Policy per cell: forecast method, safety stock, service targets, ordering
> - Delisting or MTO for CZ; collaboration for AZ
> - Review segmentation periodically as the demand pattern changes

---
## 🔗 Go deeper: expansion notes
- [[138 Order Management, Customer Service & Cost-to-Serve|Order Management, Customer Service & Cost-to-Serve]]
- [[136 Supply Chain Finance & Working Capital|Supply Chain Finance & Working Capital]]
- [[143 SCM Interview Question Bank|SCM Interview Question Bank]]
