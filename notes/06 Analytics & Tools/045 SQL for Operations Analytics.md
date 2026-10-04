---
tags: [analytics-tools, tier1]
area: Analytics & Tools
topic: "SQL for Operations Analytics"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 11
---
# SQL for Operations Analytics

⬅ [[044 Power BI & DAX]] · [[_Index - Analytics & Tools|Analytics & Tools]] · [[046 Python for Operations]] ➡

> **Area:** Analytics & Tools · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. SELECT & Filtering]]
2. [[#2. Aggregations]]
3. [[#3. JOINs]]
4. [[#4. Subqueries]]
5. [[#5. Window Functions]]
6. [[#6. CTEs (Common Table Expressions)]]
7. [[#7. String & Date Functions]]
8. [[#8. CASE Statements]]
9. [[#9. Indexes & Query Optimization]]
10. [[#10. SQL for SCM Use Cases]]
11. [[#11. ⭐ Advanced: Gaps and Islands, Cohorts, Pivoting and Data Quality Checks]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): SQL remains a top-tier skill despite AI
> **Stack Overflow Developer Survey 2025 (released 29 Jul 2025).** From **49,000+ respondents in 177 countries**, SQL was used by about **59%** (JavaScript 66%, HTML/CSS 62%), Python jumped **7 percentage points** year on year, and **PostgreSQL** was again the most admired/desired database (about 66% of those who used it this year want to keep using it, for the third year running). SQL is still among the most used languages while AI tools write more of the first draft. ([Stack Overflow press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/))
>
> The practical takeaway: AI can draft a query in seconds, but the analyst who can read, test and fix it (joins that duplicate rows, NULL traps, wrong grain) is the one who gets trusted with the number.
>
> Sub-topics that say **"See news box"** reuse this item.

---
> Dialect note: examples use standard SQL that runs on PostgreSQL and MySQL 8; differences are flagged. Sample tables: `orders(order_id, customer_id, order_date, status)`, `order_lines(order_id, sku, qty_ordered, qty_shipped, unit_price)`, `products(sku, name, category, supplier_id)`, `suppliers(supplier_id, name, city)`, `purchase_orders(po_id, supplier_id, promised_date, received_date)`, `inventory(sku, warehouse, qty, received_date)`.

## 1. SELECT & Filtering
> 🔴 Tier 1 · _Tracker hint:_ SELECT, WHERE, AND/OR, IN, BETWEEN, LIKE, IS NULL

### Definition
Logical order of evaluation: `FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`. So a column alias defined in SELECT cannot be used in WHERE (in most dialects).

```sql
SELECT order_id, customer_id, order_date
FROM   orders
WHERE  status IN ('SHIPPED', 'DELIVERED')
  AND  order_date BETWEEN '2026-04-01' AND '2026-09-30'   -- inclusive both ends
  AND  customer_id IS NOT NULL
  AND  (region = 'West' OR region = 'South')              -- parentheses control AND/OR precedence
ORDER BY order_date DESC
LIMIT 10;                                                  -- SQL Server: SELECT TOP 10
```
`LIKE 'MH-%'` (starts with), `'%_X'` (`%` any string, `_` one character). **NULL** is unknown: `= NULL` never matches; use `IS NULL`; `NULL <> 'x'` is also unknown, so such rows are dropped by WHERE; `NOT IN` with a NULL in the list returns nothing, a notorious trap. Use `DISTINCT` to remove duplicates, `COALESCE(col, 0)` to default NULLs. `AND` binds tighter than `OR`. Avoid `SELECT *` in production.

### Example
Find late-payment risk: open orders from April 2026 onwards for SKUs that begin with 'MH' and have no promised date.
```sql
SELECT order_id, sku
FROM   order_lines
WHERE  sku LIKE 'MH%' AND promised_date IS NULL;
```
Operator precedence trap: `WHERE region='West' OR region='South' AND status='OPEN'` is read as `West OR (South AND OPEN)`, returning all West rows regardless of status.

### In the news
See news box. SQL's 59% usage in the survey is why a basic WHERE/NULL error is still the most common interview failure: AI drafts do not remove the need to check logic.

### Interview angle
> [!question] How it is asked
> "Write a query to list orders in the last 30 days that were not delivered." or "Why does `WHERE col = NULL` return nothing?"

> [!tip] Strong answer includes
> - Clause order of evaluation and why aliases fail in WHERE
> - NULL handling: IS NULL, COALESCE, the NOT IN trap
> - Parentheses for AND/OR; BETWEEN is inclusive
> - Restate the grain: one row per what?

---

## 2. Aggregations
> 🔴 Tier 1 · _Tracker hint:_ COUNT, SUM, AVG, MIN, MAX; GROUP BY; HAVING vs WHERE

### Definition
Aggregates collapse many rows into one per group: `COUNT(*)` (all rows), `COUNT(col)` (non-NULL values), `COUNT(DISTINCT col)`, `SUM`, `AVG` (ignores NULLs), `MIN`, `MAX`.

```sql
SELECT   warehouse,
         COUNT(*)                 AS lines,
         SUM(qty_ordered)         AS units,
         ROUND(AVG(unit_price),2) AS avg_price
FROM     order_lines
WHERE    order_date >= '2026-04-01'     -- filters ROWS before grouping
GROUP BY warehouse
HAVING   SUM(qty_ordered) > 1000        -- filters GROUPS after aggregation
ORDER BY units DESC;
```
**WHERE** filters rows before aggregation (cannot use aggregates); **HAVING** filters groups after (can use aggregates). Every non-aggregated column in SELECT must appear in GROUP BY (strict dialects). `AVG` ignores NULLs, so `AVG(x)` may differ from `SUM(x)/COUNT(*)`. To get a rate: `SUM(CASE WHEN ... THEN 1 ELSE 0 END) * 1.0 / COUNT(*)`; multiply by 1.0 to avoid **integer division** (in PostgreSQL `3/4 = 0`).

### Example
`order_lines` per warehouse: Pune 1,500 units over 300 lines, Nashik 800 units over 200 lines. Query above with HAVING > 1000 returns only Pune. Average units per line for Pune = 1,500/300 = 5; for Nashik = 4 (not shown, filtered out by HAVING).

### In the news
See news box. Aggregations are the analyst's daily tool; a GROUP BY at the wrong grain double counts, so many wrong dashboards trace back to a join before an aggregate.

### Interview angle
> [!question] How it is asked
> "What is the difference between WHERE and HAVING?" "Find customers with more than 5 orders."

> [!tip] Strong answer includes
> - Row filter vs group filter, with the order of execution
> - COUNT(*) vs COUNT(col) vs COUNT(DISTINCT col)
> - Integer division and NULL behaviour in AVG
> - Example: `SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id HAVING COUNT(*) > 5`

---

## 3. JOINs
> 🔴 Tier 1 · _Tracker hint:_ INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF — with SCM examples

### Definition
A join combines rows from two tables on a condition.

| Join | Returns | SCM use |
|---|---|---|
| **INNER** | Only matching rows | Orders that have a shipment |
| **LEFT (OUTER)** | All left rows + matches (NULL if none) | All SKUs, with stock if any; find SKUs **with no sales** (`WHERE r.sku IS NULL`) |
| **RIGHT** | Mirror of LEFT | Rare; rewrite as LEFT |
| **FULL OUTER** | All rows from both | Reconcile PO vs GRN vs invoice (3-way match) |
| **CROSS** | Cartesian product (m × n rows) | All SKU × warehouse combinations; date scaffolds |
| **SELF** | Table joined to itself via alias | Employee-manager; BOM parent-child; route legs |

```sql
-- SKUs that never sold (anti-join)
SELECT p.sku, p.name
FROM   products p
LEFT JOIN order_lines ol ON ol.sku = p.sku
WHERE  ol.sku IS NULL;

-- Reconcile PO and goods receipt
SELECT COALESCE(po.po_id, gr.po_id) AS po_id, po.qty AS ordered, gr.qty AS received
FROM   po_lines po
FULL OUTER JOIN goods_receipts gr ON gr.po_id = po.po_id;   -- MySQL has no FULL JOIN: UNION of LEFT and RIGHT
```
Pitfalls: **row explosion** when joining on a non-unique key (a many-to-many join multiplies rows and inflates SUMs); conditions on the right table of a LEFT JOIN belong in `ON`, not `WHERE` (else it turns into an inner join).

### Example
`products` has 3 SKUs (A, B, C); `order_lines` has A twice and B once. INNER JOIN returns 3 rows (A, A, B); LEFT JOIN returns 4 (A, A, B, C with NULLs); CROSS JOIN of 3 SKUs × 2 warehouses returns 6 rows. If `SUM(qty)` is taken after joining a header with two shipment rows, header qty is counted twice: aggregate each side first (CTE) then join.

### In the news
See news box. "Why does my total not match?" is the most frequent real-world SQL bug, and the answer is almost always a join that changed the grain.

### Interview angle
> [!question] How it is asked
> "Find customers who never ordered." "Difference between INNER and LEFT join?" "What happens if the join key is not unique?"

> [!tip] Strong answer includes
> - All six join types with one SCM use each
> - Anti-join with LEFT JOIN ... IS NULL (or NOT EXISTS)
> - ON vs WHERE for outer joins
> - Grain check: count rows before and after the join

---

## 4. Subqueries
> 🔴 Tier 1 · _Tracker hint:_ Correlated vs non-correlated; IN, EXISTS, scalar subquery

### Definition
A **subquery** is a query nested inside another (in `WHERE`, `FROM` (derived table), `SELECT`).
- **Non-correlated:** runs once, independent of the outer query.
- **Correlated:** references the outer row, so logically runs per outer row (optimisers often rewrite it into a join).
- **Scalar subquery:** returns one value (one row, one column).
- **IN / NOT IN, EXISTS / NOT EXISTS, ANY/ALL.**

```sql
-- non-correlated, scalar: orders above overall average value
SELECT order_id, total
FROM   order_totals
WHERE  total > (SELECT AVG(total) FROM order_totals);

-- correlated: each SKU's line price above that SKU's own average
SELECT ol.order_id, ol.sku, ol.unit_price
FROM   order_lines ol
WHERE  ol.unit_price > (SELECT AVG(x.unit_price) FROM order_lines x WHERE x.sku = ol.sku);

-- EXISTS: customers with at least one open order (stops at the first match)
SELECT c.customer_id
FROM   customers c
WHERE  EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id AND o.status = 'OPEN');
```
`EXISTS` vs `IN`: `EXISTS` is NULL-safe and good for large inner sets; `NOT IN` returns no rows if the inner list contains NULL, so prefer `NOT EXISTS`. A derived table must have an alias. Where readability matters, a CTE is clearer.

### Example
Average order total is 5,000. Orders of 4,000, 5,500, 7,000 and 3,000 give average = 19,500/4 = 4,875; the scalar subquery returns 4,875, so the query returns the 5,500 and 7,000 orders. Using `NOT IN (SELECT customer_id ...)` where one `customer_id` is NULL returns zero rows; `NOT EXISTS` returns the correct customers.

### In the news
See news box. Because AI tools often generate nested subqueries, you should be able to spot a correlated one and judge whether a join or window would be cheaper.

### Interview angle
> [!question] How it is asked
> "Second highest order value?" "Correlated vs non-correlated subquery?" "IN vs EXISTS?"

> [!tip] Strong answer includes
> - Definitions with a one-line example each
> - NULL trap in NOT IN
> - When to rewrite as a join/CTE/window for speed and readability
> - Second highest: `SELECT MAX(total) FROM t WHERE total < (SELECT MAX(total) FROM t)`, or DENSE_RANK

---

## 5. Window Functions
> 🔴 Tier 1 · _Tracker hint:_ ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG, LEAD, RUNNING totals

### Definition
A **window function** computes across a set of rows related to the current row **without collapsing them** (unlike GROUP BY). Syntax:
```
function() OVER (PARTITION BY cols ORDER BY cols [ROWS BETWEEN ... AND ...])
```
- **Ranking:** `ROW_NUMBER()` (unique 1,2,3), `RANK()` (ties share rank, gaps after), `DENSE_RANK()` (ties share, no gaps), `NTILE(n)` (n equal buckets, e.g. quartiles).
- **Offset:** `LAG(col, n)` previous row, `LEAD(col, n)` next row.
- **Aggregates as windows:** `SUM() OVER`, `AVG() OVER` (running and moving).
- `FIRST_VALUE`, `LAST_VALUE`, `PERCENT_RANK`, `CUME_DIST`.

```sql
SELECT sku, sale_date, qty,
       SUM(qty) OVER (PARTITION BY sku ORDER BY sale_date
                      ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_qty,
       AVG(qty) OVER (PARTITION BY sku ORDER BY sale_date
                      ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)          AS moving_avg_7d,
       LAG(qty, 1) OVER (PARTITION BY sku ORDER BY sale_date)            AS prev_day_qty
FROM   daily_sales;

-- top 3 SKUs by revenue in each category
SELECT * FROM (
  SELECT category, sku, revenue,
         DENSE_RANK() OVER (PARTITION BY category ORDER BY revenue DESC) AS rnk
  FROM   sku_revenue) t
WHERE rnk <= 3;
```
Windows cannot be used in WHERE; wrap in a subquery/CTE. With `ORDER BY` and no frame, the default frame is `RANGE ... CURRENT ROW` (ties included).

### Example
Revenue values 100, 100, 90 in one partition: `ROW_NUMBER` = 1, 2, 3; `RANK` = 1, 1, 3; `DENSE_RANK` = 1, 1, 2. Daily qty 10, 20, 30: `running_qty` = 10, 30, 60; `LAG(qty)` = NULL, 10, 20; day-on-day change = qty - LAG = NULL, 10, 10. `NTILE(4)` over 8 SKUs sorted by revenue puts 2 SKUs in each quartile (a basis for ABC grouping).

### In the news
See news box. Window functions are the dividing line between basic and "analyst-grade" SQL, so they are a frequent differentiator in technical screens.

### Interview angle
> [!question] How it is asked
> "Top 3 products per category." "Running total of sales by day." "Compare each month to the previous month."

> [!tip] Strong answer includes
> - PARTITION BY (reset) vs ORDER BY (sequence) and the frame clause
> - ROW_NUMBER vs RANK vs DENSE_RANK on ties
> - LAG/LEAD for period-on-period change
> - Filter on a window result via a subquery or CTE

---

## 6. CTEs (Common Table Expressions)
> 🔴 Tier 1 · _Tracker hint:_ WITH clause; recursive CTEs; readability vs subquery

### Definition
A **CTE** is a named temporary result set defined with `WITH` and used in the following statement. It breaks a long query into readable steps and can be referenced several times.

```sql
WITH shipped AS (
    SELECT order_id, SUM(qty_shipped) AS shipped_qty FROM order_lines GROUP BY order_id
),
ordered AS (
    SELECT order_id, SUM(qty_ordered) AS ordered_qty FROM order_lines GROUP BY order_id
)
SELECT o.order_id, o.ordered_qty, s.shipped_qty,
       s.shipped_qty * 1.0 / o.ordered_qty AS fill_rate
FROM   ordered o JOIN shipped s ON s.order_id = o.order_id;
```
**Recursive CTE:** an anchor query UNIONed with a recursive part that references the CTE; used for hierarchies (BOM explosion, org charts, route legs) and number/date series.
```sql
WITH RECURSIVE bom_tree AS (          -- SQL Server and Oracle omit the word RECURSIVE
    SELECT parent_sku, child_sku, qty, 1 AS level
    FROM   bom WHERE parent_sku = 'BIKE'
    UNION ALL
    SELECT b.parent_sku, b.child_sku, b.qty * t.qty, t.level + 1
    FROM   bom b JOIN bom_tree t ON b.parent_sku = t.child_sku
)
SELECT * FROM bom_tree;
```
CTE vs subquery: mostly readability and reuse; performance is usually the same (PostgreSQL 12+ inlines non-recursive CTEs by default). CTE vs temp table: a temp table persists for the session and can be indexed. Guard recursion against cycles (depth limit).

### Example
BOM: BIKE needs 2 WHEEL; WHEEL needs 36 SPOKE. Anchor: (BIKE, WHEEL, 2, level 1). Recursive step: (WHEEL, SPOKE, 36 × 2 = 72, level 2). So a bike needs 72 spokes. A date series: `WITH RECURSIVE d(dt) AS (SELECT DATE '2026-10-01' UNION ALL SELECT dt + 1 FROM d WHERE dt < DATE '2026-10-31') SELECT * FROM d;` (PostgreSQL date arithmetic).

### In the news
See news box. As AI-generated SQL tends to produce long nested statements, CTEs are how you make them reviewable.

### Interview angle
> [!question] How it is asked
> "Explain a CTE and when you'd use a recursive one." "CTE vs subquery vs temp table?"

> [!tip] Strong answer includes
> - Readability, reuse and step-by-step logic
> - Recursive structure: anchor + UNION ALL + termination
> - BOM/org-chart/series examples
> - Performance caveats; temp tables for reuse and indexing

---

## 7. String & Date Functions
> 🔴 Tier 1 · _Tracker hint:_ CONCAT, SUBSTRING, DATEDIFF, DATE_FORMAT, EXTRACT

### Definition
Functions differ by dialect; know the idea and the main variants.

| Task | MySQL | PostgreSQL | SQL Server |
|---|---|---|---|
| Join text | `CONCAT(a,' ',b)` | `CONCAT(a,' ',b)` (or the double-pipe operator) | `CONCAT(a,' ',b)` |
| Substring | `SUBSTRING(s, 1, 3)` | `SUBSTRING(s FROM 1 FOR 3)` or `SUBSTR` | `SUBSTRING(s,1,3)` |
| Length / trim | `LENGTH`, `TRIM`, `UPPER` | same | `LEN`, `TRIM` |
| Date difference (days) | `DATEDIFF(end, start)` | `end::date - start::date` | `DATEDIFF(day, start, end)` |
| Format date | `DATE_FORMAT(d, '%Y-%m')` | `TO_CHAR(d, 'YYYY-MM')` | `FORMAT(d, 'yyyy-MM')` |
| Part of date | `EXTRACT(MONTH FROM d)` | `EXTRACT(MONTH FROM d)` | `DATEPART(month, d)` |
| Truncate to month | `DATE_FORMAT(d,'%Y-%m-01')` | `DATE_TRUNC('month', d)` | `DATETRUNC(month, d)` (2022+) |
| Add interval | `DATE_ADD(d, INTERVAL 7 DAY)` | `d + INTERVAL '7 days'` | `DATEADD(day, 7, d)` |

Also `REPLACE`, `LEFT/RIGHT`, `POSITION`, `COALESCE`, `CAST(x AS DATE)`, `CURRENT_DATE`. Keep dates as DATE types; avoid string comparison on date text. For range filters use `d >= '2026-04-01' AND d < '2026-05-01'` (half-open) rather than wrapping the column in a function (keeps indexes usable).

### Example
PO promised 2026-10-05, received 2026-10-09: lateness = 4 days (`DATEDIFF('2026-10-09','2026-10-05')` in MySQL; `received_date - promised_date` in PostgreSQL). Monthly roll-up in PostgreSQL: `SELECT TO_CHAR(order_date,'YYYY-MM') AS month, COUNT(*) FROM orders GROUP BY 1 ORDER BY 1;`. SKU code 'MH-NSK-00123': `SUBSTRING(sku, 4, 3)` = 'NSK'.

### In the news
See news box. Date logic (time zones, month ends, half-open ranges) is where AI-written queries most often slip, so always verify with a hand-checked sample.

### Interview angle
> [!question] How it is asked
> "Orders per month for the last year." "Average delivery lead time in days."

> [!tip] Strong answer includes
> - Know dialect differences and state which one you assume
> - Half-open date ranges and avoiding functions on indexed columns
> - Group by month with DATE_TRUNC/DATE_FORMAT
> - Handle NULL dates (undelivered) explicitly

---

## 8. CASE Statements
> 🔴 Tier 1 · _Tracker hint:_ Conditional logic; bucketing; pivot-style aggregation

### Definition
`CASE` is SQL's if-then-else, evaluated top to bottom; the first true branch wins; no ELSE yields NULL.
```sql
CASE WHEN cond1 THEN v1 WHEN cond2 THEN v2 ELSE v3 END      -- searched
CASE col WHEN 'A' THEN 1 WHEN 'B' THEN 2 END                -- simple
```
Uses:
- **Bucketing:** `CASE WHEN days_late = 0 THEN 'On time' WHEN days_late <= 3 THEN '1-3 days' ELSE '>3 days' END`.
- **Conditional aggregation / pivot:** count or sum only some rows per column.
```sql
SELECT warehouse,
       COUNT(*)                                          AS orders,
       SUM(CASE WHEN status = 'DELIVERED' THEN 1 ELSE 0 END) AS delivered,
       SUM(CASE WHEN status = 'RETURNED'  THEN 1 ELSE 0 END) AS returned,
       AVG(CASE WHEN status='DELIVERED' THEN lead_days END)  AS avg_lead_days   -- AVG ignores NULLs
FROM   orders
GROUP BY warehouse;
```
Also inside `ORDER BY` for custom sort order, and in `UPDATE` for conditional changes. Make ranges non-overlapping and ordered; put the most specific test first.

### Example
Warehouse W1 has 200 orders: 180 delivered, 12 returned, 8 open. Query returns orders = 200, delivered = 180, returned = 12; delivery % = 180/200 = 90%; return rate = 12/200 = 6%. Pivot-style output (one column per status) needs no PIVOT keyword: each CASE builds one column.

### In the news
See news box. Conditional aggregation is how analysts build the same KPI tables that BI tools show, which makes dashboards reproducible from the database.

### Interview angle
> [!question] How it is asked
> "Show delivered, returned and open orders as separate columns per warehouse." "Bucket customers into High/Medium/Low."

> [!tip] Strong answer includes
> - Searched CASE with an ELSE and ordered conditions
> - SUM(CASE ...) for pivoting and conditional rates
> - Know that AVG(CASE ... END) ignores NULLs (a feature)
> - Division by zero guard: NULLIF(denominator, 0)

---

## 9. Indexes & Query Optimization
> 🔴 Tier 1 · _Tracker hint:_ Index types; EXPLAIN plan; avoid SELECT *

### Definition
An **index** is a sorted data structure (usually **B-tree**) that lets the database find rows without scanning the whole table, at the cost of extra storage and slower writes.

Types: **B-tree** (default; equality and range), **hash** (equality only), **composite** (multi-column; follows the **leftmost-prefix rule**), **unique**, **clustered** (defines physical row order, one per table, e.g. SQL Server/InnoDB primary key) vs **non-clustered/secondary**, **covering index** (contains all needed columns; no table lookup), partial and full-text indexes.

```sql
CREATE INDEX idx_orders_cust_date ON orders (customer_id, order_date);
EXPLAIN SELECT * FROM orders WHERE customer_id = 42 AND order_date >= '2026-09-01';
EXPLAIN ANALYZE SELECT ...;    -- PostgreSQL / MySQL 8: actually runs and shows real timings
```
Read the plan: **Seq/Full Scan** vs **Index Scan/Seek**, estimated vs actual rows, join methods (nested loop, hash, merge), sort cost.

Optimisation habits: select only needed columns (no `SELECT *`), filter early, **sargable** predicates (`order_date >= X`, not `YEAR(order_date) = 2026`; no leading wildcard `LIKE '%abc'`), index join and filter columns, avoid implicit type conversion, prefer `EXISTS` over `IN` on big inner sets, pre-aggregate before joining, use `LIMIT`, update statistics, partition large tables, avoid correlated subqueries on huge tables.

### Example
`orders` has 10 million rows. `WHERE customer_id = 42` without an index scans all 10 million rows; with a B-tree index it descends about 3 to 4 levels and reads the few matching rows. For `WHERE YEAR(order_date) = 2026` the index on `order_date` is ignored; rewrite as `order_date >= '2026-01-01' AND order_date < '2027-01-01'`. A composite index on (customer_id, order_date) serves both columns, but a query filtering only on `order_date` cannot use it efficiently (leftmost-prefix rule).

### In the news
See news box. As AI generates more queries, running EXPLAIN on them before production use is the safeguard against a plausible-looking query that scans a 10-million-row table.

### Interview angle
> [!question] How it is asked
> "A report query is slow. What do you do?" "What is a covering index?" "Why can't the index be used here?"

> [!tip] Strong answer includes
> - EXPLAIN first, find the scan/sort/join cost
> - Index on filter and join columns, order in a composite index, sargability
> - Trade-off: faster reads, slower writes and more storage
> - Avoid SELECT *, push filters early, pre-aggregate

---

## 10. SQL for SCM Use Cases
> 🔴 Tier 1 · _Tracker hint:_ Inventory aging, supplier performance, order fill rate queries

### Definition
Three staples, each combining aggregations, CASE and joins.

**Inventory ageing** (buckets by days in stock):
```sql
SELECT sku, warehouse,
       SUM(CASE WHEN CURRENT_DATE - received_date <= 30 THEN qty ELSE 0 END) AS d0_30,
       SUM(CASE WHEN CURRENT_DATE - received_date BETWEEN 31 AND 60 THEN qty ELSE 0 END) AS d31_60,
       SUM(CASE WHEN CURRENT_DATE - received_date BETWEEN 61 AND 90 THEN qty ELSE 0 END) AS d61_90,
       SUM(CASE WHEN CURRENT_DATE - received_date > 90 THEN qty ELSE 0 END) AS d90_plus
FROM   inventory GROUP BY sku, warehouse;      -- PostgreSQL date subtraction; MySQL use DATEDIFF
```
**Supplier performance** (on-time delivery %, average delay):
```sql
SELECT s.name,
       COUNT(*) AS pos,
       100.0 * SUM(CASE WHEN po.received_date <= po.promised_date THEN 1 ELSE 0 END) / COUNT(*) AS otd_pct,
       AVG(GREATEST(po.received_date - po.promised_date, 0)) AS avg_days_late
FROM   purchase_orders po JOIN suppliers s ON s.supplier_id = po.supplier_id
WHERE  po.received_date IS NOT NULL
GROUP BY s.name ORDER BY otd_pct;
```
**Order fill rate** (line and unit):
```sql
SELECT 100.0 * SUM(qty_shipped) / NULLIF(SUM(qty_ordered), 0)                       AS unit_fill_pct,
       100.0 * SUM(CASE WHEN qty_shipped >= qty_ordered THEN 1 ELSE 0 END) / COUNT(*) AS line_fill_pct
FROM   order_lines;
```
Others: **ABC classification** (cumulative revenue % by SKU using `SUM() OVER` and a CASE on 80/95%), stock-out days, days of inventory (stock / average daily demand), OTIF, 3-way match, lead-time percentiles (`PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY lead_days)` in PostgreSQL).

### Example
Supplier A: 10 POs, 8 on time: OTD = 100 × 8/10 = **80%**. Order lines: ordered 1,000 units, shipped 920: unit fill = **92%**; if 4 of 5 lines were fully shipped, line fill = **80%** (line fill is stricter). Inventory: 500 units received 20 days ago (0 to 30 bucket), 300 received 75 days ago (61 to 90 bucket), 200 received 120 days ago (90+): 20% of stock is older than 90 days, a write-off risk.

### In the news
See news box. These are the metrics ops managers ask for first; being able to produce them from raw tables in a screen test shows readiness for Operations and Consulting analyst roles.

### Interview angle
> [!question] How it is asked
> "Write a query for supplier on-time delivery." "Show inventory ageing by bucket." "Fill rate by customer."

> [!tip] Strong answer includes
> - Define the metric and grain first (line vs order vs unit)
> - CASE-based conditional aggregation; NULLIF for division
> - Handle undelivered/NULL dates and returns explicitly
> - Sanity check totals against a source figure; mention indexes if the table is large

---

## 11. ⭐ Advanced: Gaps and Islands, Cohorts, Pivoting and Data Quality Checks
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Interview-level patterns beyond the tracker:
- **Deduplication:** `ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1` keeps the latest record.
- **Consecutive-day streaks (gaps and islands):** subtract `ROW_NUMBER()` from the date to create a group key; consecutive days share the same key.
- **Period-over-period:** `LAG` with `(cur - prev) / NULLIF(prev, 0)`.
- **Cohort/repeat-rate:** first order date per customer via `MIN() OVER`, then month index.
- **Pareto/ABC:** cumulative share = `SUM(rev) OVER (ORDER BY rev DESC) / SUM(rev) OVER ()`.
- **Median/percentile:** `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY x)` (PostgreSQL, Oracle, SQL Server as window), MySQL has no built-in median.
- **Set operations:** `UNION` (distinct) vs `UNION ALL` (keeps duplicates, faster), `INTERSECT`, `EXCEPT`.
- **Data-quality checks:** duplicates (`GROUP BY ... HAVING COUNT(*) > 1`), orphan keys (anti-join), NULL rates, reconciling counts and sums to source.
- **Transactions/ACID, normalisation (1NF to 3NF)**, and star-schema thinking for analytics.

### Example
Dedup: two rows for order 101 (updated 9 Oct and 12 Oct): `ROW_NUMBER` = 1 for 12 Oct, so a filter `rn = 1` keeps it. ABC: SKU revenues 500, 300, 100, 60, 40 (total 1,000): cumulative share = 50%, 80%, 90%, 96%, 100%. Class A = SKUs up to 80% (2 SKUs, 40% of items), B up to 95% (1 SKU), C the rest (2 SKUs).

### In the news
See news box. Reconciliation and data-quality queries are the unglamorous checks that keep AI-written analysis honest.

### Interview angle
> [!question] How it is asked
> "Remove duplicates keeping the latest record." "Find customers who ordered 3 months in a row." "Classify SKUs into A, B, C."

> [!tip] Strong answer includes
> - ROW_NUMBER for dedupe and the gaps-and-islands trick
> - Cumulative-share window for ABC
> - UNION vs UNION ALL
> - Always propose a reconciliation check to the source total

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
