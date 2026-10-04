---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "SQL for SCM & Business Analytics"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 12
---
# SQL for SCM & Business Analytics

⬅ [[060 Query Optimization & Indexing]] · [[_Index - SQL & Databases|SQL & Databases]] · [[181 SQL Interview Problem Bank]] ➡
> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Inventory Aging Query]]
2. [[#2. Supplier Scorecard Query]]
3. [[#3. OTIF Calculation]]
4. [[#4. ABC Classification in SQL]]
5. [[#5. Month-over-Month Growth]]
6. [[#6. Cohort Retention Analysis]]
7. [[#7. Running Inventory Balance]]
8. [[#8. Top N per Category]]
9. [[#9. Duplicate Detection]]
10. [[#10. Date Spine for Gaps]]
11. [[#11. ⭐ Advanced: Inventory Turnover, Days of Inventory and Stock-out Days in SQL]]
12. [[#12. ⭐ Advanced: Forecast Accuracy (MAPE, Bias, WMAPE) and Moving Averages in SQL]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): when a quick-commerce leader takes inventory onto its own books, SQL on stock data becomes a P&L tool
> **Blinkit moves to an inventory-led model (Sept 2025).** Per Logistics Insider's explainer, Blinkit shifted from a marketplace (sellers listed products and paid for warehouse storage) to buying inventory directly from sellers and brands: sellers had until 30 Jul 2025 to opt in, inventory transferred to Blinkit's books by 31 Aug 2025 and the full transition began on 1 Sep 2025. Eternal's CFO was quoted saying that, assuming 100% inventory ownership in FY25, Blinkit would need less than ₹1,000 crore of working capital, about 3-4% of its gross order value (₹28,274 crore). Once you own the stock, ageing, dead stock, stock-outs and running balances (the queries below) hit working capital and margins directly. ([Logistics Insider](https://www.logisticsinsider.in/explained-blinkits-new-inventory-led-model/))
>
> **MySQL 8.0 reaches end of life (April 2026).** The release notes state "As of April 2026, with version 8.0.46, MySQL 8.0 reaches End of Life (EoL)" and point users to MySQL 8.4 LTS. Window functions (`LAG`, `NTILE`, `ROW_NUMBER`) and recursive CTEs used in this note were introduced in MySQL 8.0, so they carry over to 8.4. ([MySQL release notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Inventory Aging Query
> 🔴 Tier 1 · _Tracker hint:_ SELECT product, days_in_stock, CASE WHEN days>90 THEN 'Dead' ... END FROM inventory

### Definition
**Inventory ageing** buckets stock by how long it has sat unsold (days since receipt, or since last movement). It exposes slow-moving and obsolete stock tying up cash and warehouse space. Compute days with `DATEDIFF`, bucket with `CASE`, and aggregate value per bucket. In MySQL you cannot reuse a SELECT alias in the same SELECT, so compute days in a subquery or CTE.

```sql
WITH aged AS (
  SELECT sku, warehouse, qty, unit_cost,
         DATEDIFF(CURDATE(), last_receipt_date) AS days_in_stock
  FROM inventory
  WHERE qty > 0
)
SELECT CASE WHEN days_in_stock <= 30  THEN '0-30 Fresh'
            WHEN days_in_stock <= 90  THEN '31-90 Normal'
            WHEN days_in_stock <= 180 THEN '91-180 Slow'
            ELSE '180+ Dead' END          AS age_bucket,
       COUNT(*)                           AS sku_locations,
       SUM(qty * unit_cost)               AS stock_value
FROM aged
GROUP BY age_bucket
ORDER BY MIN(days_in_stock);
```
Better ageing uses **FIFO layers** (receipt batches) or **last sale date**: an item received last week but never sold is not "fresh" demand-wise. Thresholds depend on the product (perishables: days; spares: years). Output feeds provisioning, liquidation and promotions.

### Example
A warehouse holds 200 units at ₹500 aged 220 days: dead stock value = 200 x 500 = ₹1,00,000. If the total stock is ₹10,00,000, then 10% (1,00,000 / 10,00,000) is in the 180+ bucket. At an annual carrying cost of 20%, that pocket costs ₹20,000 a year before any write-down.

### In the news
See news box. With Blinkit owning inventory from Sept 2025, every aged unit sits on its balance sheet, so ageing reports become a working-capital control rather than a seller's problem.

### Interview angle
> [!question] How it is asked
> "Write a query to identify dead stock" or "How would you reduce excess inventory in this warehouse?"

> [!tip] Strong answer includes
> - Days since receipt or last sale, bucketed with CASE; value-weighted not just counts
> - Business thresholds justified per category
> - Actions: liquidation, returns to vendor, stop re-ordering, review safety stock
> - Note limits: batch/expiry-level data gives truer ageing than a single date

---

## 2. Supplier Scorecard Query
> 🔴 Tier 1 · _Tracker hint:_ SELECT supplier, AVG(lead_time), SUM(defects)/SUM(qty)*100 AS defect_rate GROUP BY supplier

### Definition
A **supplier scorecard** summarises delivery, quality and cost performance per supplier. Typical metrics: average and variability of lead time, on-time delivery %, defect rate (PPM or %), fill/short-shipment rate, price variance.

```sql
SELECT s.supplier_name,
       COUNT(*)                                          AS receipts,
       AVG(DATEDIFF(r.received_date, r.po_date))         AS avg_lead_days,
       STDDEV_SAMP(DATEDIFF(r.received_date, r.po_date)) AS lead_sd,
       SUM(r.defect_qty) / SUM(r.received_qty) * 100     AS defect_rate_pct,
       SUM(r.defect_qty) / SUM(r.received_qty) * 1000000 AS defect_ppm,
       100 * AVG(r.received_date <= r.promised_date)     AS on_time_pct
FROM receipts r JOIN suppliers s ON s.supplier_id = r.supplier_id
WHERE r.received_date >= '2025-04-01'
GROUP BY s.supplier_name
ORDER BY defect_rate_pct DESC;
```
Key point: compute a **weighted** defect rate as `SUM(defects)/SUM(qty)`, not `AVG(defects/qty)`, which over-weights tiny shipments. In MySQL a boolean comparison is 1/0, so `AVG(cond)` gives a proportion (in PostgreSQL use `AVG((cond)::int)`). Lead-time **variability** (standard deviation) matters as much as the mean because safety stock depends on it ($SS = Z \sqrt{L\sigma_d^2 + d^2\sigma_L^2}$). Combine metrics into a weighted score only after normalising scales, and require a minimum volume per supplier.

### Example
Supplier A: shipments of 1,000 units with 10 defects, and 100 units with 5 defects. Weighted defect rate = (10 + 5) / (1,000 + 100) = 15/1,100 = 1.36%. Average of ratios = (1.0% + 5.0%) / 2 = 3.0%, which exaggerates the small shipment. In PPM, 1.36% is 13,636 PPM (0.01364 x 1,000,000).

### In the news
See news box. As retailers take stock ownership (Blinkit, Sept 2025), supplier quality and lead-time reliability flow straight into their own inventory risk, which makes scorecards a commercial negotiation tool.

### Interview angle
> [!question] How it is asked
> "How would you rank suppliers using SQL?" or "Supplier A has a lower defect rate on average but we still have quality issues. Why?"

> [!tip] Strong answer includes
> - Weighted ratios (sum over sum) not averages of ratios
> - Lead-time mean and variability, on-time %, defect %, and cost
> - Minimum-volume filters and time window
> - Turn the output into actions: corrective action plans, dual sourcing, share-of-business shifts

---

## 3. OTIF Calculation
> 🔴 Tier 1 · _Tracker hint:_ SELECT COUNT(CASE WHEN on_time=1 AND in_full=1 THEN 1 END)/COUNT(*) AS otif FROM deliveries

### Definition
**OTIF (On-Time In-Full)** = orders (or lines) delivered both on or before the promised date AND with the full ordered quantity, divided by total orders. It is the headline customer-service KPI in FMCG and retail supply chains.

```sql
SELECT customer,
       COUNT(*)                                                       AS orders,
       100.0 * COUNT(CASE WHEN delivered_date <= promised_date
                           AND delivered_qty  >= ordered_qty THEN 1 END) / COUNT(*) AS otif_pct,
       100.0 * AVG(delivered_date <= promised_date)                   AS on_time_pct,   -- MySQL boolean avg
       100.0 * AVG(delivered_qty  >= ordered_qty)                     AS in_full_pct
FROM deliveries
WHERE delivered_date IS NOT NULL
GROUP BY customer;
```
`COUNT(CASE WHEN cond THEN 1 END)` counts only rows where cond holds (the CASE gives NULL otherwise, and COUNT ignores NULL). Pitfalls: integer division in PostgreSQL/SQL Server (multiply by `100.0` or cast first); undelivered orders (NULL dates) silently dropped; whether OTIF is measured at order, line or case level (line-level is stricter or more granular); tolerance windows (e.g., delivered within promised date plus/minus 0 days; in-full within 100% vs 98%). OTIF is **multiplicative-ish**: it is at most the lower of on-time % and in-full %.

### Example
1,000 orders: 940 on time, 900 in full, and 860 both on time and in full. OTIF = 860 / 1,000 = **86%**. Even though each leg looks above 90%, OTIF is 86%. If failures were independent, expected OTIF would be 0.94 x 0.90 = 84.6%, so 86% shows the failures overlap a little (the same orders fail both tests).

### In the news
See news box. With inventory on its own books, a quick-commerce player's in-full rate to customers depends directly on its own replenishment, which is why OTIF is split into supplier OTIF (inbound) and customer OTIF (outbound).

### Interview angle
> [!question] How it is asked
> "Calculate OTIF from a deliveries table" or "OTIF is 82%. How do you find out why?"

> [!tip] Strong answer includes
> - Correct CASE-count formula and decimal division
> - Decompose into on-time % and in-full % and cut by customer, lane, SKU, warehouse, supplier
> - State the definition (order vs line, tolerance, promised vs requested date)
> - Root causes and levers: forecast, safety stock, carrier performance, pick accuracy

---

## 4. ABC Classification in SQL
> 🔴 Tier 1 · _Tracker hint:_ NTILE(3) OVER (ORDER BY revenue DESC) to classify A/B/C items

### Definition
**ABC analysis** (Pareto) ranks items by annual revenue or consumption value: typically **A** = top items making about 80% of value, **B** = next 15%, **C** = last 5%. It sets control intensity (tight control and frequent review for A, simple rules for C).

The tracker's shortcut, `NTILE(3)`, splits items into three **equal-sized groups by rank** (each a third of the SKUs), which is not the same as 80/15/5 by value:
```sql
SELECT sku, revenue,
       CASE NTILE(3) OVER (ORDER BY revenue DESC) WHEN 1 THEN 'A' WHEN 2 THEN 'B' ELSE 'C' END AS abc
FROM sku_revenue;
```
The **correct, value-based** approach uses cumulative share:
```sql
WITH t AS (
  SELECT sku, revenue,
         SUM(revenue) OVER (ORDER BY revenue DESC, sku
                            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_rev,
         SUM(revenue) OVER ()                                                   AS total_rev
  FROM sku_revenue
)
SELECT sku, revenue, ROUND(100 * cum_rev / total_rev, 1) AS cum_pct,
       CASE WHEN cum_rev / total_rev <= 0.80 THEN 'A'
            WHEN cum_rev / total_rev <= 0.95 THEN 'B'
            ELSE 'C' END AS abc
FROM t;
```
Use an explicit `ROWS` frame (the default `RANGE` frame treats ties together). Often an item that crosses the 80% line is kept in A (use cum_rev minus own revenue). Extend with **XYZ** (demand variability by coefficient of variation) for a 9-box.

### Example
Five SKUs, revenues 500, 300, 100, 60, 40 (total 1,000). Cumulative: 500 (50%), 800 (80%), 900 (90%), 960 (96%), 1,000 (100%). Value-based: SKU1 A, SKU2 A, SKU3 B, SKU4 C, SKU5 C. NTILE(3) over 5 rows makes groups of 2, 2, 1: SKU1-2 A, SKU3-4 B, SKU5 C, so SKU4 (6% of revenue) is wrongly called B.

### In the news
See news box. For a quick-commerce firm carrying owned stock, ABC drives which of thousands of SKUs deserve dark-store space and frequent replenishment, and which can be demand-driven or dropped.

### Interview angle
> [!question] How it is asked
> "Classify products into A, B and C using SQL" or "What is wrong with using NTILE(3) for ABC?"

> [!tip] Strong answer includes
> - Cumulative-percentage method with window functions and explicit frame
> - Explicit warning that NTILE gives equal counts, not 80/15/5 of value
> - Policy differences by class (review frequency, service level, safety stock)
> - Extension to XYZ, and refresh periodically

---

## 5. Month-over-Month Growth
> 🔴 Tier 1 · _Tracker hint:_ LAG(revenue,1) OVER (ORDER BY month) to calculate MoM % change

### Definition
**MoM growth %** = (current month - previous month) / previous month x 100. `LAG(col, n)` reads the value from `n` rows earlier in the window order, avoiding self-joins.

```sql
WITH m AS (
  SELECT DATE_FORMAT(order_date, '%Y-%m') AS ym, SUM(amount) AS revenue
  FROM orders GROUP BY DATE_FORMAT(order_date, '%Y-%m')
)
SELECT ym, revenue,
       LAG(revenue, 1) OVER (ORDER BY ym)                        AS prev_rev,
       ROUND(100 * (revenue - LAG(revenue, 1) OVER (ORDER BY ym))
             / NULLIF(LAG(revenue, 1) OVER (ORDER BY ym), 0), 1) AS mom_pct
FROM m;
```
The first month has no previous row, so `LAG` returns NULL (or give a default: `LAG(revenue,1,0)`). `NULLIF(...,0)` avoids divide-by-zero. Pitfalls: **missing months** (a gap makes LAG compare with the wrong month; fix with a date spine, see sub-topic 10); partition by product/region with `PARTITION BY`; seasonality (compare year-over-year with `LAG(revenue, 12)`). Equivalent forward-looking function: `LEAD`.

### Example
Revenue: Jan 200, Feb 230, Mar 207. Feb MoM = (230 - 200) / 200 = +15%. Mar MoM = (207 - 230) / 230 = -10%. Note +15% then -10% does not return to 200: 230 x 0.90 = 207, which is 3.5% above January.

### In the news
See news box. Fast-growing models (Blinkit's GOV of ₹28,274 crore in FY25) are tracked on monthly growth, but MoM alone misleads where seasonality exists, so pair with YoY.

### Interview angle
> [!question] How it is asked
> "Calculate month-over-month revenue growth per category."

> [!tip] Strong answer includes
> - `LAG` with `ORDER BY` (and `PARTITION BY` for categories)
> - NULL for the first period and divide-by-zero guard
> - Handling missing months with a calendar table
> - MoM vs YoY and seasonality commentary

---

## 6. Cohort Retention Analysis
> 🔴 Tier 1 · _Tracker hint:_ JOIN on first_purchase_month vs subsequent months; group by cohort

### Definition
A **cohort** groups customers by their first-purchase month. **Retention** at month *n* = share of the cohort that purchases again *n* months later. It tells a PM or consultant whether growth is real loyalty or constant acquisition.

```sql
WITH first_order AS (
  SELECT customer_id,
         DATE_FORMAT(MIN(order_date), '%Y-%m-01') AS cohort_month
  FROM orders GROUP BY customer_id
),
activity AS (
  SELECT DISTINCT customer_id, DATE_FORMAT(order_date, '%Y-%m-01') AS active_month
  FROM orders
),
joined AS (
  SELECT f.cohort_month,
         TIMESTAMPDIFF(MONTH, f.cohort_month, a.active_month) AS month_n,
         a.customer_id
  FROM first_order f JOIN activity a ON a.customer_id = f.customer_id
)
SELECT cohort_month, month_n,
       COUNT(DISTINCT customer_id) AS active_customers,
       ROUND(100 * COUNT(DISTINCT customer_id) /
             MAX(COUNT(DISTINCT customer_id)) OVER (PARTITION BY cohort_month), 1) AS retention_pct
FROM joined
GROUP BY cohort_month, month_n
ORDER BY cohort_month, month_n;
```
The month 0 row is the cohort size (every customer is active in their first month), so `MAX(...) OVER (PARTITION BY cohort)` picks it as the denominator. Use `DISTINCT` so a customer with many orders in a month counts once. Variants: revenue retention, rolling retention, weekly cohorts for apps. Right-censoring: recent cohorts have fewer observable months.

### Example
Jan cohort has 200 customers (month 0). In month 1, 50 of them order again: retention = 50 / 200 = 25%. Month 2: 36 active = 18%. A flattening curve (say settling near 15%) signals a loyal core; a curve falling toward zero signals a discount-driven, leaky base.

### In the news
See news box. Quick-commerce economics depend on repeat orders from the same neighbourhoods, which is why cohort retention is a core investor and operations metric for these players.

### Interview angle
> [!question] How it is asked
> "Write a query to measure monthly customer retention" or "How would you know if our new-user growth is healthy?"

> [!tip] Strong answer includes
> - First-purchase cohort definition and month offset logic
> - Denominator = cohort size (month 0); use `COUNT(DISTINCT customer_id)`
> - Triangle layout and right-censoring of recent cohorts
> - Interpretation: curve flattening, revenue vs logo retention, link to CAC/LTV

---

## 7. Running Inventory Balance
> 🔴 Tier 1 · _Tracker hint:_ SUM(qty_in - qty_out) OVER (ORDER BY date) as running_balance

### Definition
A **running (cumulative) balance** is the stock on hand after each transaction: opening balance plus cumulative receipts minus cumulative issues. Use `SUM() OVER` with an explicit frame, partitioned per SKU/warehouse.

```sql
SELECT sku, txn_date, txn_id, qty_in, qty_out,
       SUM(qty_in - qty_out) OVER (
            PARTITION BY sku
            ORDER BY txn_date, txn_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_balance
FROM stock_movements
ORDER BY sku, txn_date, txn_id;
```
Notes: add a unique tie-breaker (`txn_id`) to `ORDER BY`, because with the default `RANGE` frame rows sharing the same date would all show the same cumulative total. If there is an **opening balance**, add it as a first row or `+ opening_qty` via a join. Use the series to detect **negative balances** (data errors or unrecorded receipts: `WHERE running_balance < 0`), compute **days of stock-out**, and reconcile to system stock. For large tables, consider a periodic snapshot table instead of recomputing from history each time.

### Example
SKU A1 movements: +100 (receipt), -30, -20, +50. Running balance: 100, then 100 - 30 = 70, then 70 - 20 = 50, then 50 + 50 = 100. If a later issue of 120 is booked, the balance goes to -20, which flags a missing receipt or a posting error.

### In the news
See news box. When a firm owns inventory (Blinkit from Sept 2025), the stock ledger becomes a financial record, so accuracy of the running balance affects the accounts.

### Interview angle
> [!question] How it is asked
> "Compute the daily closing stock for each SKU from receipts and issues."

> [!tip] Strong answer includes
> - Window `SUM` with `PARTITION BY sku ORDER BY date` and explicit frame
> - Tie-breaker for same-day rows and opening balance
> - Negative-balance check as data quality control
> - Mention reconciliation with physical counts (cycle counts)

---

## 8. Top N per Category
> 🔴 Tier 1 · _Tracker hint:_ ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC) then WHERE rn <= 3

### Definition
You cannot filter on a window function in the same `WHERE`, so compute the rank in a CTE or subquery and filter outside.

```sql
WITH ranked AS (
  SELECT category, product, SUM(sales) AS sales,
         ROW_NUMBER() OVER (PARTITION BY category ORDER BY SUM(sales) DESC) AS rn
  FROM order_lines
  GROUP BY category, product
)
SELECT category, product, sales
FROM ranked
WHERE rn <= 3;
```
Which function: **`ROW_NUMBER`** gives unique ranks 1,2,3 (ties broken arbitrarily unless you add a tie-breaker in `ORDER BY`); **`RANK`** gives ties the same rank and skips (1,2,2,4); **`DENSE_RANK`** ties share a rank without gaps (1,2,2,3). Use `RANK`/`DENSE_RANK` if all tied items should be included. A window function can be applied over an aggregate (`SUM(sales)` inside `OVER (...)` after `GROUP BY`) as above, because window functions run after grouping. Other uses: latest record per key (`ROW_NUMBER() ... ORDER BY updated_at DESC`, keep rn = 1), top supplier per category, worst-performing warehouse per region.

### Example
Category Snacks sales: Chips 500, Namkeen 400, Biscuits 400, Nuts 100. `ROW_NUMBER`: 1,2,3,4 (Namkeen and Biscuits get 2 and 3 in arbitrary order); top 3 = Chips, Namkeen, Biscuits, but with a top 2 cut-off one tied item would be dropped arbitrarily. `RANK`: 1,2,2,4, so `rank <= 3` gives Chips, Namkeen, Biscuits. `DENSE_RANK`: 1,2,2,3, so `<= 3` gives Nuts too (4 rows).

### In the news
See news box. Per-store or per-category "top sellers" lists decide which SKUs get dark-store space for firms now owning stock (Blinkit, Sept 2025).

### Interview angle
> [!question] How it is asked
> "Get the top 3 products by sales in each category" or "Latest order per customer."

> [!tip] Strong answer includes
> - `PARTITION BY` category with `ORDER BY` sales DESC, filtered in an outer query
> - Choice of `ROW_NUMBER` vs `RANK` vs `DENSE_RANK` and tie behaviour
> - Deterministic tie-breaker
> - Alternative approaches (correlated subquery or `LIMIT` per group via lateral join) and why windows are cleaner

---

## 9. Duplicate Detection
> 🔴 Tier 1 · _Tracker hint:_ GROUP BY key_cols HAVING COUNT(*) > 1 — data quality checks

### Definition
Duplicates inflate revenue, stock and customer counts. Detect with `GROUP BY` the business key and `HAVING COUNT(*) > 1`:

```sql
-- Which keys are duplicated, and how often?
SELECT supplier_id, invoice_no, COUNT(*) AS n
FROM invoices
GROUP BY supplier_id, invoice_no
HAVING COUNT(*) > 1;

-- See the actual duplicate rows, keep the first
SELECT * FROM (
  SELECT i.*, ROW_NUMBER() OVER (PARTITION BY supplier_id, invoice_no ORDER BY invoice_id) AS rn
  FROM invoices i
) x WHERE rn > 1;

-- Delete duplicates keeping the lowest invoice_id (MySQL)
DELETE i FROM invoices i
JOIN (SELECT MIN(invoice_id) AS keep_id, supplier_id, invoice_no
      FROM invoices GROUP BY supplier_id, invoice_no HAVING COUNT(*) > 1) d
  ON i.supplier_id = d.supplier_id AND i.invoice_no = d.invoice_no AND i.invoice_id <> d.keep_id;
```
`HAVING` filters groups after aggregation (`WHERE` filters rows before). Check near-duplicates too (case, spaces, spelling: normalise with `UPPER(TRIM())`). Prevent recurrence with a `UNIQUE` constraint on the business key. In SCM, classic duplicates: the same invoice paid twice (duplicate payment risk), duplicate vendor masters, repeated EDI or PO lines, double-posted goods receipts. Always back up or run the SELECT first before deleting.

### Example
Invoices table: (S1, INV-9) appears 2 times for ₹80,000 each. Duplicate query returns n = 2. Overpayment risk = 1 extra x 80,000 = ₹80,000. Of 10,000 rows, if 150 are surplus duplicates, 1.5% of rows (150 / 10,000) are redundant.

### In the news
See news box. As owners of stock and payables, firms such as Blinkit need clean vendor and invoice masters, since a duplicated receipt overstates inventory and a duplicated invoice leaks cash.

### Interview angle
> [!question] How it is asked
> "How do you find and remove duplicate records?" or "How would you check data quality in a supplier invoice table?"

> [!tip] Strong answer includes
> - `GROUP BY ... HAVING COUNT(*) > 1` with the business key
> - `ROW_NUMBER()` approach to keep one and delete the rest
> - Normalise before comparing; near-duplicates and fuzzy matching
> - Prevent: unique constraints, validation at entry, plus SCM impact (duplicate payments)

---

## 10. Date Spine for Gaps
> 🔴 Tier 1 · _Tracker hint:_ Generate all dates, LEFT JOIN actual data to find missing dates/periods

### Definition
Real tables only contain dates where something happened, so days with zero sales or stock-outs are **missing rows**, not zeros. A **date spine** (calendar table) lists every date; `LEFT JOIN` the facts to it to expose gaps, fill zeros, and make `LAG`/moving averages correct.

```sql
-- MySQL 8: generate dates with a recursive CTE (default limit 1000 iterations)
WITH RECURSIVE spine AS (
  SELECT DATE '2025-01-01' AS d
  UNION ALL
  SELECT d + INTERVAL 1 DAY FROM spine WHERE d < '2025-01-31'
)
SELECT sp.d, COALESCE(SUM(s.qty), 0) AS units_sold
FROM spine sp
LEFT JOIN daily_sales s ON s.sale_date = sp.d AND s.sku = 'A1'
GROUP BY sp.d
ORDER BY sp.d;

-- Only the missing days:
--   ... HAVING COUNT(s.sale_date) = 0
-- PostgreSQL: FROM generate_series('2025-01-01'::date, '2025-01-31', '1 day') AS sp(d)
```
Put the filter on the right table (`sku = 'A1'`) in the `ON` clause, not in `WHERE`, otherwise the LEFT JOIN turns into an inner join and gaps vanish. For multiple SKUs, `CROSS JOIN` spine with the SKU list first. Best practice: a permanent **date dimension** table (with fiscal year, week, holiday). Uses: stock-out days, missing-feed detection, fill rate by day, continuous time series for forecasting.

### Example
SKU A1 has sales rows on 1, 2, 4 and 5 January only. Spine of 5 days minus 4 present = 1 gap: 3 January had zero sales (or no data). If that was a stock-out, lost-sales days = 1 of 5 = 20% availability loss. Without the spine, a 'daily average' would be over 4 days, not 5.

### In the news
See news box. For dark stores that own their stock, "days with zero availability" per SKU is a lost-revenue metric that only a date spine can compute.

### Interview angle
> [!question] How it is asked
> "Find days when there were no orders" or "Our daily report skips days with zero sales. Fix it."

> [!tip] Strong answer includes
> - Calendar/spine generation (recursive CTE or `generate_series`)
> - `LEFT JOIN` with conditions in `ON`; `COALESCE` for zeros
> - Cross join with SKU/store list for panel data
> - Business uses: stock-out days, SLA misses, missing data feeds

---

## 11. ⭐ Advanced: Inventory Turnover, Days of Inventory and Stock-out Days in SQL
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Operations and consulting cases ask for efficiency KPIs straight from data.

- **Inventory turnover** = COGS / average inventory, where average inventory = (opening + closing) / 2 (or the average of month-end balances).
- **Days of inventory (DIO)** = 365 / turnover = average inventory / COGS x 365.
- **Days of supply** = on-hand / average daily demand.
- **Stock-out rate** = days with zero stock / days in period (use the date spine and running balance).

```sql
WITH bal AS (   -- month-end stock value per SKU
  SELECT sku, DATE_FORMAT(snapshot_date,'%Y-%m') AS ym, AVG(stock_value) AS avg_stock_value
  FROM inventory_snapshots GROUP BY sku, DATE_FORMAT(snapshot_date,'%Y-%m')
), c AS (
  SELECT sku, SUM(cogs) AS cogs_12m FROM sales_cogs WHERE sale_date >= CURDATE() - INTERVAL 12 MONTH GROUP BY sku
)
SELECT c.sku, c.cogs_12m, AVG(b.avg_stock_value) AS avg_inv,
       c.cogs_12m / NULLIF(AVG(b.avg_stock_value),0)       AS turns,
       365 * AVG(b.avg_stock_value) / NULLIF(c.cogs_12m,0) AS dio
FROM c JOIN bal b ON b.sku = c.sku
GROUP BY c.sku, c.cogs_12m;
```
Use **cumulative** definitions consistently: annual COGS with average inventory over the same period. Compare turns across categories only within a category (perishables turn far faster than spares). Link to cash: cash-to-cash = DIO + DSO - DPO.

### Example
Annual COGS ₹36 crore, average inventory ₹4.5 crore. Turns = 36 / 4.5 = 8.0. DIO = 365 / 8 = 45.6 days. If DSO = 10 and DPO = 30, cash-to-cash = 45.6 + 10 - 30 = 25.6 days. Cutting inventory to ₹3.6 crore gives turns 10 and DIO 36.5 days, freeing ₹0.9 crore of cash.

### In the news
See news box. Blinkit's CFO framing of working capital as roughly 3-4% of GOV is exactly this type of turnover logic expressed in percentage-of-sales terms.

### Interview angle
> [!question] How it is asked
> "How would you measure whether this warehouse's inventory is efficient?" or "Write SQL for inventory turns."

> [!tip] Strong answer includes
> - Formula with consistent time period and average (not closing) inventory
> - Convert to days and to cash-to-cash
> - Segment by category and ABC class before comparing
> - Pair with service level so cutting stock does not hurt availability

---

## 12. ⭐ Advanced: Forecast Accuracy (MAPE, Bias, WMAPE) and Moving Averages in SQL
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Planners and consultants judge forecasts using error metrics, computed easily with window functions.

- **Bias (mean error)** = average of (forecast - actual): positive = over-forecasting.
- **MAPE** = average of |forecast - actual| / actual x 100 (breaks when actual = 0 and over-weights small items).
- **WMAPE** = SUM(|forecast - actual|) / SUM(actual): weighted by volume, preferred for SKU portfolios. Forecast accuracy is often reported as 1 - WMAPE.
- **Moving average** forecast: average of the last *k* periods.

```sql
SELECT sku,
       100 * SUM(ABS(forecast_qty - actual_qty)) / NULLIF(SUM(actual_qty),0) AS wmape_pct,
       100 * (SUM(forecast_qty) - SUM(actual_qty)) / NULLIF(SUM(actual_qty),0) AS bias_pct
FROM demand_vs_forecast
WHERE month >= '2025-04-01'
GROUP BY sku;

-- 3-month moving average per SKU
SELECT sku, month, actual_qty,
       AVG(actual_qty) OVER (PARTITION BY sku ORDER BY month
                             ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS ma3
FROM demand_monthly;
```
Compute error at the level where decisions are made (SKU-location-week), and measure at the planning lag (forecast made 4 weeks before). Persistent bias is an easier fix than random error.

### Example
Three months, actuals 100, 120, 80 (sum 300); forecasts 110, 100, 90. Absolute errors 10, 20, 10 = 40, so WMAPE = 40 / 300 = 13.3% (accuracy 86.7%). Bias = (300 - 300) / 300 = 0%: forecasts are unbiased overall despite 13.3% error. Moving average for month 3 = (100 + 120 + 80) / 3 = 100.

### In the news
See news box. A retailer that buys stock outright (Blinkit's inventory-led shift) lives or dies by forecast bias, since over-forecast creates dead stock and under-forecast creates lost sales.

### Interview angle
> [!question] How it is asked
> "How would you measure forecast accuracy for 10,000 SKUs?" or "Write SQL for a 3-month moving average."

> [!tip] Strong answer includes
> - WMAPE vs MAPE and why, plus bias to show direction
> - Window frame `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`
> - Measure at decision granularity and the right forecast lag
> - Actions: fix bias first, segment by ABC/XYZ, add safety stock for residual error

---

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
