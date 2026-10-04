---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "Window Functions"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 14
---
# Window Functions

⬅ [[057 Subqueries & CTEs]] · [[_Index - SQL & Databases|SQL & Databases]] · [[059 String, Date & Advanced Functions]] ➡

> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. CTE (WITH Clause)]]
2. [[#2. Multiple CTEs]]
3. [[#3. Recursive CTE]]
4. [[#4. ROW_NUMBER()]]
5. [[#5. RANK() vs DENSE_RANK()]]
6. [[#6. NTILE(n)]]
7. [[#7. LAG() & LEAD()]]
8. [[#8. FIRST_VALUE / LAST_VALUE]]
9. [[#9. Running Total]]
10. [[#10. Moving Average]]
11. [[#11. Percent of Total]]
12. [[#12. SCM Window Example]]
13. [[#13. ⭐ Advanced: ABC Analysis with Cumulative Percentage]]
14. [[#14. ⭐ Advanced: Gaps and Islands, Sessionisation and YoY]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Window functions and CTEs are now standard on every major engine
> **MySQL 8.0 reached end of life on 30 April 2026.** Window functions and CTEs arrived in MySQL 8.0; with 8.0's extended support over, MySQL 8.4 is the recommended LTS, and older 5.7-era code without these features is firmly legacy. ([OpenLogic](https://www.openlogic.com/blog/mysql-8-end-of-life))
>
> **PostgreSQL leads the 2025 Stack Overflow Developer Survey** (**55.6%** of all respondents, **58.2%** of professionals; MySQL **40.5%**, SQLite **37.5%**, SQL Server **30.1%**). PostgreSQL has had full window-function and recursive-CTE support for years. ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
>
> **PostgreSQL 18 (25 Sep 2025)** adds an asynchronous I/O subsystem (reported gains up to about 3x in some scenarios) and skip-scan on multicolumn B-tree indexes: relevant because window queries sort and scan large partitions. ([LWN](https://lwn.net/Articles/1039483/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. CTE (WITH Clause)
> 🔴 Tier 1 · _Tracker hint:_ WITH cte AS (SELECT ...) SELECT * FROM cte; improves readability

### Definition
A **Common Table Expression (CTE)** is a named temporary result defined with `WITH` and visible only to the statement that follows. It reads top-down, like naming steps of an analysis.

```sql
WITH dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_sal
    FROM   emp
    GROUP  BY dept_id
)
SELECT e.name, e.salary, d.avg_sal
FROM   emp e
JOIN   dept_avg d ON d.dept_id = e.dept_id
WHERE  e.salary > d.avg_sal;
```
Benefits: readability, reuse within the statement, an alternative to nested subqueries, and the only way (besides loops) to write recursive queries. A CTE is **not** automatically faster: in PostgreSQL 12+ a CTE referenced once is inlined; in MySQL 8 it is merged or materialised by the optimiser. Supported in MySQL 8.0+, PostgreSQL 8.4+, SQL Server 2005+, SQLite 3.8.3+. A CTE can also be used in `INSERT/UPDATE/DELETE` (PostgreSQL even allows data-modifying CTEs).

### Example
Instead of a derived table nested inside a WHERE, name the step `dept_avg`. Dept 10 average = 60k, dept 20 average = 80k; the final SELECT compares each employee's salary to the right average. Anyone reviewing the query reads the logic top to bottom.

### In the news
See news box. CTEs and window functions only became available in MySQL with 8.0, so any shop on 8.0 or later (now 8.4) can use them.

### Interview angle
> [!question] How it is asked
> "What is a CTE? How is it different from a subquery or temp table?"

> [!tip] Strong answer includes
> - Named, statement-scoped result; readability
> - Not guaranteed to be faster; engine-dependent
> - Difference from temp table (not stored) and view (not persistent)
> - Mention of recursion as unique capability

---

## 2. Multiple CTEs
> 🔴 Tier 1 · _Tracker hint:_ WITH cte1 AS (...), cte2 AS (...) SELECT * FROM cte1 JOIN cte2

### Definition
Define several CTEs after a **single** `WITH`, separated by commas; later CTEs can reference earlier ones. This builds a readable pipeline: clean, aggregate, then join.

```sql
WITH monthly AS (
    SELECT cust_id, DATE_FORMAT(order_date,'%Y-%m') AS ym, SUM(amount) AS rev
    FROM   orders GROUP BY cust_id, DATE_FORMAT(order_date,'%Y-%m')
),
ranked AS (
    SELECT *, RANK() OVER (PARTITION BY ym ORDER BY rev DESC) AS rnk
    FROM   monthly
)
SELECT * FROM ranked WHERE rnk <= 3;
```
Rules: one `WITH` keyword; no comma before the final SELECT; each CTE name must be unique; a CTE can only see CTEs defined **above** it (except in recursive definitions). Using the same CTE several times may recompute it in some engines, so check EXPLAIN. Common pattern: CTE 1 = filtered base data, CTE 2 = metric calculation, CTE 3 = ranking/flags, final query = presentation.

### Example
Step 1 `monthly`: customer revenue per month (e.g. C1, Sep = 5,000). Step 2 `ranked`: ranks customers within each month. Final: top 3 per month. Three small steps replace one unreadable triple-nested subquery.

### In the news
See news box. The "stepwise CTE pipeline" style is now the norm in analytics code reviews across MySQL 8.4 and PostgreSQL.

### Interview angle
> [!question] How it is asked
> "Write a query with two CTEs: monthly revenue and then the top 3 customers per month."

> [!tip] Strong answer includes
> - Single WITH, comma-separated CTEs
> - Later CTEs referencing earlier ones
> - Clear naming per step
> - Awareness of possible re-evaluation, and use of EXPLAIN

---

## 3. Recursive CTE
> 🔴 Tier 1 · _Tracker hint:_ WITH RECURSIVE — for org hierarchy, BOM explosion, sequence generation

### Definition
A **recursive CTE** has an **anchor** member (starting rows) and a **recursive** member that references the CTE itself, combined with `UNION ALL`. It repeats until the recursive step returns no new rows.

```sql
-- org hierarchy: everyone under manager 1, with depth
WITH RECURSIVE org AS (
    SELECT id, name, manager_id, 1 AS lvl
    FROM   emp WHERE id = 1                     -- anchor
    UNION ALL
    SELECT e.id, e.name, e.manager_id, o.lvl + 1
    FROM   emp e JOIN org o ON e.manager_id = o.id   -- recursive step
)
SELECT * FROM org;

-- number sequence 1..5
WITH RECURSIVE n AS (SELECT 1 AS i UNION ALL SELECT i + 1 FROM n WHERE i < 5)
SELECT * FROM n;
```
Syntax: `WITH RECURSIVE` in MySQL 8+ and PostgreSQL; SQL Server omits the word RECURSIVE. Always include a **termination condition**; MySQL stops at `cte_max_recursion_depth` (default 1000); SQL Server has `OPTION (MAXRECURSION n)` (default 100). Guard against cycles by tracking visited ids or a depth limit.

### Example
BOM: Bike needs 1 Frame and 2 Wheels; each Wheel needs 36 Spokes and 1 Rim. Recursive explosion for 1 bike: Wheels 2, Spokes = 2 x 36 = **72**, Rims 2 x 1 = 2, Frame 1. The quantity is multiplied at each level (`o.qty * b.qty`).

### In the news
See news box. Recursive CTEs arrived in MySQL only with 8.0, so hierarchy queries that needed stored procedures in 5.7 are now plain SQL on 8.4.

### Interview angle
> [!question] How it is asked
> "Print the reporting chain for an employee." "Explode a bill of materials." "Generate dates between two dates."

> [!tip] Strong answer includes
> - Anchor + recursive member + UNION ALL
> - Termination and cycle protection
> - Level counter and quantity multiplication for BOMs
> - Dialect notes (RECURSIVE keyword, recursion limits)

---

## 4. ROW_NUMBER()
> 🔴 Tier 1 · _Tracker hint:_ ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) — unique rank

### Definition
A **window function** computes a value for each row using a set of related rows (its **window**) **without collapsing rows** (unlike GROUP BY). Syntax:

`function() OVER (PARTITION BY ... ORDER BY ... [frame])`

`ROW_NUMBER()` assigns a unique sequential number 1, 2, 3... within each partition, **even for ties** (tie order is arbitrary unless you add a tie-breaker).

```sql
SELECT name, dept, salary,
       ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC, id) AS rn
FROM   emp;

-- top earner per department
SELECT * FROM (
    SELECT e.*, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC, id) AS rn
    FROM emp e) t
WHERE rn = 1;
```
Window functions run after WHERE/GROUP BY/HAVING and before ORDER BY, so you **cannot filter on them directly**: wrap in a subquery/CTE. Classic uses: top-N per group, **deduplication** (keep `rn = 1` per key, delete the rest), pagination, numbering rows.

### Example
Dept A salaries 90k, 90k, 70k: `ROW_NUMBER()` gives 1, 2, 3. Two people tie at 90k but get different numbers, so `rn = 1` returns exactly one of them. Deduplicating customers: `ROW_NUMBER() OVER (PARTITION BY email ORDER BY created_at DESC)` and keeping `rn = 1` retains the latest record per email.

### In the news
See news box. ROW_NUMBER-based deduplication is a daily task in data-cleaning pipelines on both leading engines.

### Interview angle
> [!question] How it is asked
> "Get the highest-paid employee per department." "Remove duplicate rows keeping the latest."

> [!tip] Strong answer includes
> - PARTITION BY (groups) and ORDER BY (sequence) explained
> - Unique numbering even on ties; add tie-breaker
> - Wrap in subquery/CTE to filter rn
> - Dedup and top-N patterns

---

## 5. RANK() vs DENSE_RANK()
> 🔴 Tier 1 · _Tracker hint:_ RANK skips numbers on ties (1,1,3); DENSE_RANK doesn't (1,1,2)

### Definition
| Function | Ties | Example for 90, 90, 80, 70 |
|---|---|---|
| `ROW_NUMBER()` | different numbers | 1, 2, 3, 4 |
| `RANK()` | same rank, **gaps** after ties | 1, 1, 3, 4 |
| `DENSE_RANK()` | same rank, **no gaps** | 1, 1, 2, 3 |

```sql
SELECT name, salary,
       RANK()       OVER (ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS drnk
FROM   emp;

-- Nth highest salary (handles ties): N = 3
SELECT DISTINCT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS d FROM emp) t
WHERE d = 3;
```
Choose **DENSE_RANK** for "Nth highest value", **RANK** for sports-style ranking (1, 1, 3) and for "top N including ties" (`rnk <= N`), and ROW_NUMBER when exactly one row per group is needed. Related: `PERCENT_RANK()` and `CUME_DIST()` give relative position (0 to 1).

### Example
Salaries 90, 90, 80, 70. Third highest **distinct** salary: DENSE_RANK = 3 gives **70**. With RANK the value 70 has rank 4 and nobody has rank 3, so `rank = 3` returns nothing, a classic mistake.

### In the news
See news box. These ranking functions appear in MySQL 8.0+ and PostgreSQL alike, so one query pattern works on both.

### Interview angle
> [!question] How it is asked
> "Difference between RANK, DENSE_RANK and ROW_NUMBER?" "Find the 3rd highest salary."

> [!tip] Strong answer includes
> - The (1,1,3) vs (1,1,2) vs (1,2,3) illustration
> - Chooses DENSE_RANK for Nth highest
> - Top N with ties via RANK
> - Notes tie-breakers matter for ROW_NUMBER only

---

## 6. NTILE(n)
> 🔴 Tier 1 · _Tracker hint:_ NTILE(4) divides rows into quartiles; useful for ABC classification

### Definition
`NTILE(n)` splits the ordered rows of a partition into **n buckets** of (nearly) equal row count and returns the bucket number 1..n. If rows do not divide evenly, the first buckets get one extra row.

```sql
SELECT sku, revenue,
       NTILE(4) OVER (ORDER BY revenue DESC) AS quartile
FROM   sku_sales;
```
Uses: quartiles/deciles, customer segmentation (top 20% = `NTILE(5)` bucket 1), rough ABC grouping. **Caveat:** NTILE splits by **row count**, not by cumulative value, so true ABC (A = items producing 80% of revenue) needs a cumulative-percentage window (see Advanced section). NTILE also ignores ties (identical values can land in different buckets), so use PERCENT_RANK if ties must stay together.

### Example
10 SKUs, `NTILE(4)`: bucket sizes are 10 / 4 = 2 remainder 2, so the first two buckets get 3 rows and the last two get 2: sizes 3, 3, 2, 2. With 8 SKUs, each bucket has exactly 2.

### In the news
See news box. NTILE exists on all leading engines, but does not replace value-weighted Pareto logic for inventory classification.

### Interview angle
> [!question] How it is asked
> "Split customers into 4 spend quartiles." "Is NTILE the right tool for ABC analysis?"

> [!tip] Strong answer includes
> - Equal row-count buckets and remainder rule
> - Example of quartile or decile segmentation
> - Knows the limitation versus cumulative-value ABC
> - Handles ties and small groups

---

## 7. LAG() & LEAD()
> 🔴 Tier 1 · _Tracker hint:_ LAG(sales,1) gets previous row value; LEAD gets next — trend analysis

### Definition
`LAG(col, n, default)` returns the value from **n rows before** the current row in the window order; `LEAD(col, n, default)` looks **n rows ahead**. The first (or last) row has no neighbour, so you get NULL unless a default is supplied.

```sql
SELECT month, sales,
       LAG(sales, 1)  OVER (ORDER BY month)                         AS prev_sales,
       sales - LAG(sales, 1) OVER (ORDER BY month)                  AS change,
       ROUND(100.0 * (sales - LAG(sales) OVER (ORDER BY month))
                   / LAG(sales) OVER (ORDER BY month), 1)           AS mom_pct,
       LEAD(sales, 1, 0) OVER (ORDER BY month)                      AS next_sales
FROM   monthly_sales;
```
Add `PARTITION BY` to restart per group (e.g. per product). Typical uses: month-on-month and year-on-year growth (`LAG(x, 12)`), days between consecutive orders (`order_date - LAG(order_date)`), detecting status changes, replacing self-joins. Guard against division by zero with `NULLIF`.

### Example
Sales: Jan 100, Feb 120, Mar 90. LAG gives NULL, 100, 120. MoM: Feb = (120 - 100)/100 = **+20%**; Mar = (90 - 120)/120 = **-25%**. LEAD for Jan = 120, for Mar = NULL (or default 0).

### In the news
See news box. Trend and growth calculations using LAG are core for demand-planning dashboards, now writable in plain SQL on any 2025-era engine.

### Interview angle
> [!question] How it is asked
> "Calculate month-over-month growth." "Find customers whose gap between consecutive orders exceeds 30 days."

> [!tip] Strong answer includes
> - LAG = previous, LEAD = next, with offset and default
> - PARTITION BY for per-entity trends
> - Percentage change formula with NULLIF
> - Contrasts with self join (simpler, faster)

---

## 8. FIRST_VALUE / LAST_VALUE
> 🔴 Tier 1 · _Tracker hint:_ Returns first/last value in window; use with ROWS BETWEEN frame

### Definition
`FIRST_VALUE(col)` returns the first value in the window frame, `LAST_VALUE(col)` the last; `NTH_VALUE(col, n)` the nth.

**Frame trap:** when a window has `ORDER BY` but no explicit frame, the default frame is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. So `LAST_VALUE` returns the **current row's** value, not the partition's last. Specify the full frame:

```sql
SELECT sku, month, price,
       FIRST_VALUE(price) OVER (PARTITION BY sku ORDER BY month)            AS first_price,
       LAST_VALUE(price)  OVER (PARTITION BY sku ORDER BY month
            ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)       AS last_price
FROM   price_hist;
```
Frame clause syntax: `ROWS BETWEEN <start> AND <end>` with `UNBOUNDED PRECEDING`, `n PRECEDING`, `CURRENT ROW`, `n FOLLOWING`, `UNBOUNDED FOLLOWING`. `ROWS` counts physical rows; `RANGE` groups peer rows with equal ORDER BY values. Use cases: compare each price to the launch price, to the latest price, first purchase date per customer.

### Example
SKU prices Jan 50, Feb 55, Mar 60. FIRST_VALUE = 50 on every row. LAST_VALUE with the default frame returns 50, 55, 60 (current row); with `UNBOUNDED FOLLOWING` it returns 60 on every row. Price vs launch: Mar = (60 - 50)/50 = +20%.

### In the news
See news box. This default-frame behaviour is standard SQL and the same in MySQL 8.4 and PostgreSQL 18, so the trap is portable.

### Interview angle
> [!question] How it is asked
> "Why does LAST_VALUE return the current row?" "Show each product's price relative to its first price."

> [!tip] Strong answer includes
> - Explains the default frame and its consequence
> - Gives the explicit ROWS BETWEEN fix
> - ROWS vs RANGE difference
> - Alternative: FIRST_VALUE with reversed ORDER BY

---

## 9. Running Total
> 🔴 Tier 1 · _Tracker hint:_ SUM(amount) OVER (PARTITION BY cust ORDER BY date ROWS UNBOUNDED PRECEDING)

### Definition
A **running (cumulative) total** is a SUM window ordered by time, with a frame from the first row to the current row.

```sql
SELECT cust_id, order_date, amount,
       SUM(amount) OVER (PARTITION BY cust_id
                         ORDER BY order_date, order_id
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM   orders;
```
`ROWS UNBOUNDED PRECEDING` is shorthand for the same frame. Prefer **ROWS** over the default **RANGE**: with RANGE, rows with the same `order_date` are peers and get the **same** cumulative value (the total includes all peers), which is rarely intended; add a unique tie-breaker (`order_id`) to ORDER BY. Uses: cumulative sales vs target, stock-ledger balance (receipts minus issues), cash balance, cumulative % for Pareto charts. Stock balance: `SUM(qty_in - qty_out) OVER (PARTITION BY sku ORDER BY txn_date, txn_id)`.

### Example
Orders for one customer: 100, 120, 90, 140. Running totals: **100, 220, 310, 450**. Stock ledger: opening 0, +500, -200, -150 gives balances 500, 300, 150, so the report shows the balance after every movement.

### In the news
See news box. Running balances in ledger-style SQL are the basis of inventory and finance reports in ERP data marts.

### Interview angle
> [!question] How it is asked
> "Compute cumulative revenue per customer by date." "Show inventory balance after each transaction."

> [!tip] Strong answer includes
> - SUM() OVER with ORDER BY and ROWS frame
> - Why ROWS beats RANGE on duplicate dates
> - PARTITION BY to restart per group
> - Unique tie-breaker in ORDER BY

---

## 10. Moving Average
> 🔴 Tier 1 · _Tracker hint:_ AVG(sales) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)

### Definition
A **moving average** smooths noisy series by averaging a sliding window, e.g. a 3-month moving average (3MMA):

$$MA_t = \frac{1}{k}\sum_{i=0}^{k-1} x_{t-i}$$

```sql
SELECT month, sales,
       AVG(sales) OVER (ORDER BY month
                        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS ma3,
       COUNT(*)   OVER (ORDER BY month
                        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS n_in_window
FROM   monthly_sales;
```
The first rows have fewer than k observations, so the "average" is over fewer points; use `n_in_window` or wrap in `CASE WHEN n = 3 THEN ... END` to blank partial windows. This is a **trailing** average (uses past data only): suitable for naive forecasting of the next period; centred windows use `1 PRECEDING AND 1 FOLLOWING`. For irregular dates (missing months) ROWS counts rows, not calendar months, so first fill gaps with a calendar table or use a RANGE interval frame (PostgreSQL).

### Example
Sales: 100, 120, 90, 140. Month 3 MA = (100 + 120 + 90)/3 = **103.33**. Month 4 MA = (120 + 90 + 140)/3 = **116.67**. Month 1 (only itself) = 100 and month 2 = (100 + 120)/2 = 110, partial windows.

### In the news
See news box. Moving averages are the simplest demand-forecast baseline, and writing one in SQL avoids exporting data to Excel.

### Interview angle
> [!question] How it is asked
> "Calculate a 3-month moving average of sales." "How do you handle the first two months?"

> [!tip] Strong answer includes
> - Frame `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`
> - Partial window handling
> - Trailing vs centred
> - Missing-period caveat for ROWS-based frames

---

## 11. Percent of Total
> 🔴 Tier 1 · _Tracker hint:_ SUM(amount) OVER (PARTITION BY region) — denominator for % share

### Definition
Use a window SUM **without ORDER BY** as the denominator, so every row sees the total of its partition and the detail rows survive.

```sql
SELECT region, product, amount,
       ROUND(100.0 * amount / SUM(amount) OVER (PARTITION BY region), 1) AS pct_of_region,
       ROUND(100.0 * amount / SUM(amount) OVER (), 1)                    AS pct_of_total
FROM   sales;
```
`OVER ()` = whole result set; `PARTITION BY region` = within region. Without a window you would need a subquery or self join to get the denominator. Remember `100.0 *` (or CAST) to avoid integer division, and guard divisions with `NULLIF(denominator, 0)`. Also: cumulative % (running total / grand total) for **Pareto/ABC**; share of customer in revenue; contribution to variance.

### Example
North: A = 200, B = 300; South: A = 500. Grand total = 1,000. `pct_of_total`: 20%, 30%, 50%. `pct_of_region`: North A = 200/500 = **40%**, North B = 300/500 = **60%**, South A = 500/500 = **100%**.

### In the news
See news box. Share-of-total columns are the building block for dashboard tiles and Pareto views in BI tools.

### Interview angle
> [!question] How it is asked
> "Show each product's share of its category's sales." "What percent of revenue does each customer contribute?"

> [!tip] Strong answer includes
> - SUM() OVER (PARTITION BY ...) without ORDER BY as denominator
> - Avoiding integer division and zero denominators
> - Difference between share of partition and share of grand total
> - Extending to cumulative % for Pareto

---

## 12. SCM Window Example
> 🔴 Tier 1 · _Tracker hint:_ Rank suppliers by delivery performance per category using RANK() OVER (PARTITION BY category ORDER BY otd DESC)

### Definition
Combine aggregation (CTE) with window ranking to produce a supplier league table per category.

```sql
WITH perf AS (
    SELECT s.category, s.supplier_name,
           COUNT(*) AS n_pos,
           100.0 * SUM(CASE WHEN r.receipt_date <= p.promised_date THEN 1 ELSE 0 END) / COUNT(*) AS otd
    FROM   purchase_orders p
    JOIN   receipts  r ON r.po_id = p.po_id
    JOIN   suppliers s ON s.id = p.supplier_id
    GROUP  BY s.category, s.supplier_name
    HAVING COUNT(*) >= 10                      -- minimum sample
)
SELECT category, supplier_name, otd,
       RANK() OVER (PARTITION BY category ORDER BY otd DESC) AS rnk,
       otd - AVG(otd) OVER (PARTITION BY category)           AS vs_category_avg
FROM   perf;
```
Variations: `LAG(otd)` by quarter for supplier trend, `NTILE(4)` for performance quartiles, running spend share for Pareto, `ROW_NUMBER()` to pick the latest PO per supplier.

### Example
Category "Packaging": Supplier A OTD 96%, B 92%, C 92%, D 85%. RANK: A = 1, B = 2, C = 2, D = 4. Category average = (96 + 92 + 92 + 85)/4 = **91.25%**; A is +4.75 pts, D is -6.25 pts. D is the candidate for a corrective-action plan or second-source qualification.

### In the news
See news box. Supplier scorecards built with window functions run directly on ERP extracts in warehouses, with no export to spreadsheet tools needed.

### Interview angle
> [!question] How it is asked
> "Rank suppliers within each category by on-time delivery." "Which supplier's performance deteriorated the most quarter over quarter?"

> [!tip] Strong answer includes
> - Aggregate in a CTE first, then rank in the outer query
> - RANK vs DENSE_RANK vs ROW_NUMBER choice with ties
> - Minimum-sample HAVING filter
> - Business action tied to the ranking (review, dual source)

---

## 13. ⭐ Advanced: ABC Analysis with Cumulative Percentage
> ⭐ Advanced · _Added beyond the tracker_

### Definition
True **ABC (Pareto) classification** ranks SKUs by revenue (or consumption value), computes the **cumulative share** of the total, and cuts at thresholds (commonly A up to 80%, B up to 95%, C the rest). It is value-weighted, unlike NTILE.

```sql
WITH s AS (
    SELECT sku, SUM(qty * price) AS rev FROM sales GROUP BY sku
),
c AS (
    SELECT sku, rev,
           100.0 * SUM(rev) OVER (ORDER BY rev DESC, sku
                                  ROWS UNBOUNDED PRECEDING) / SUM(rev) OVER () AS cum_pct
    FROM   s
)
SELECT sku, rev, ROUND(cum_pct,1) AS cum_pct,
       CASE WHEN cum_pct <= 80 THEN 'A'
            WHEN cum_pct <= 95 THEN 'B'
            ELSE 'C' END AS abc_class
FROM   c;
```
Use `cum_pct - 100.0*rev/total <= 80` (cumulative share *before* the item) if you want the SKU that crosses the threshold included in class A. Policy follows: A items get tight control and frequent review, high service level; C items get simple rules and low review effort. Link with XYZ (demand variability) for a 9-box policy.

### Example
SKU revenues: S1 500, S2 300, S3 100, S4 60, S5 40; total 1,000. Cumulative: 50%, 80%, 90%, 96%, 100%. Classes: S1 = A, S2 = A (80%), S3 = B (90%), S4 = C (96% > 95), S5 = C. So 2 of 5 SKUs (40%) produce 80% of revenue.

### In the news
See news box. Inventory teams commonly run this analysis directly in SQL on ERP exports, since cumulative windows on PostgreSQL 18 or MySQL 8.4 handle millions of SKUs.

### Interview angle
> [!question] How it is asked
> "How would you classify 10,000 SKUs into A, B, C using SQL?"

> [!tip] Strong answer includes
> - Aggregate revenue, order desc, running SUM divided by total SUM
> - Thresholds (80/95) and boundary handling
> - Contrast with NTILE (row-based)
> - Link to policy: service levels, review frequency, safety stock

---

## 14. ⭐ Advanced: Gaps and Islands, Sessionisation and YoY
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Classic window-function puzzles used in senior analytics interviews.

**Gaps and islands:** find consecutive runs. Subtracting `ROW_NUMBER()` from a sequential key gives a constant per island.

```sql
-- consecutive-day login streaks
WITH d AS (
    SELECT DISTINCT user_id, login_date FROM logins
),
g AS (
    SELECT user_id, login_date,
           login_date - INTERVAL ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) DAY AS grp  -- MySQL
    FROM d
)
SELECT user_id, MIN(login_date) AS start_dt, MAX(login_date) AS end_dt, COUNT(*) AS streak_days
FROM g GROUP BY user_id, grp;
```
PostgreSQL: `login_date - (ROW_NUMBER() OVER (...))::int AS grp`.

**Gap detection:** `LEAD(date) OVER (...) - date > 1` flags missing days. **Sessionisation:** start a new session when `date - LAG(date) > 30 min`, then cumulative-sum the flags. **YoY:** `LAG(revenue, 12) OVER (ORDER BY month)`.

### Example
Login dates 1, 2, 3, 5, 6 Oct. Row numbers 1..5; date minus row number gives constants 0 (for 1-3) and 1 (for 5, 6) in day offsets, so two islands: 1-3 Oct (streak 3) and 5-6 Oct (streak 2). The gap on 4 Oct is detected by a LEAD difference of 2 days.

### In the news
See news box. Streak and session logic like this drives retention analytics in consumer apps and runs on any modern engine with window support.

### Interview angle
> [!question] How it is asked
> "Find the longest consecutive-day streak per user." "Identify missing dates in a sequence."

> [!tip] Strong answer includes
> - The ROW_NUMBER subtraction trick and why it works
> - Dedupe first (DISTINCT) so duplicates do not break the sequence
> - Alternative with LAG and a cumulative flag
> - Dialect-correct date arithmetic

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
