---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "Aggregations & GROUP BY"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Aggregations & GROUP BY

⬅ [[054 Filtering, Sorting & CASE]] · [[_Index - SQL & Databases|SQL & Databases]] · [[056 JOINs — All Types]] ➡

> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Aggregate Functions]]
2. [[#2. GROUP BY]]
3. [[#3. HAVING Clause]]
4. [[#4. COUNT vs COUNT(*)]]
5. [[#5. GROUP BY Multiple Columns]]
6. [[#6. ROLLUP & CUBE]]
7. [[#7. GROUPING SETS]]
8. [[#8. Conditional Aggregation]]
9. [[#9. String Aggregation]]
10. [[#10. SCM Use Case]]
11. [[#11. ⭐ Advanced: Aggregation Pitfalls — Fan-out and Double Counting]]
12. [[#12. ⭐ Advanced: Percentiles, Median and Approximate Aggregates]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Aggregation engines and dialect gaps
> **PostgreSQL is the most-used database in the 2025 Stack Overflow survey** (**55.6%** of all respondents, **58.2%** of professionals; MySQL **40.5%**, SQL Server **30.1%**). PostgreSQL supports `ROLLUP`, `CUBE` and `GROUPING SETS` natively, while MySQL offers only `WITH ROLLUP`, so portable aggregation skills matter. ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
>
> **PostgreSQL 18 (25 Sep 2025)** introduced an asynchronous I/O subsystem; the release reports gains up to about 3x in some scenarios, with support for sequential scans, bitmap heap scans and vacuum, the scan-heavy operations that aggregate queries rely on. ([LWN](https://lwn.net/Articles/1039483/))
>
> **MySQL 8.0 end of life (30 Apr 2026).** Extended support ended on 30 April 2026; MySQL 8.4 is the recommended LTS. Reporting queries need re-validation on the new version. ([OpenLogic](https://www.openlogic.com/blog/mysql-8-end-of-life))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Aggregate Functions
> 🔴 Tier 1 · _Tracker hint:_ COUNT(*), COUNT(col), SUM(col), AVG(col), MIN(col), MAX(col)

### Definition
An **aggregate function** collapses many rows into one value.

| Function | Returns | NULL handling |
|---|---|---|
| `COUNT(*)` | number of rows | counts all rows |
| `COUNT(col)` | non-NULL values | ignores NULL |
| `SUM(col)` | total | ignores NULL; all-NULL gives NULL |
| `AVG(col)` | mean = SUM / COUNT(col) | ignores NULL in both numerator and denominator |
| `MIN`, `MAX` | smallest, largest (numbers, dates, text) | ignores NULL |

```sql
SELECT COUNT(*) AS n_orders,
       SUM(amount) AS revenue,
       AVG(amount) AS aov,          -- average order value
       MIN(order_date) AS first_order,
       MAX(order_date) AS last_order
FROM orders;
```
Without GROUP BY, the whole table is one group and you get **one row**. Aggregates cannot appear in WHERE (use HAVING). Also: `COUNT(DISTINCT col)`, `STDDEV`, `VARIANCE`. Integer division caution: in PostgreSQL and SQL Server `SUM(a)/COUNT(*)` on integers truncates; cast to DECIMAL.

### Example
Order amounts: 200, 300, NULL, 500. `COUNT(*)` = 4, `COUNT(amount)` = 3, `SUM` = 1,000, `AVG` = 1,000 / 3 = **333.33** (not 250), because the NULL row is excluded from both sum and count.

### In the news
See news box. Basic aggregates behave the same on MySQL 8.4 and PostgreSQL 18, which is why they are the safest building blocks for KPI queries.

### Interview angle
> [!question] How it is asked
> "What does AVG do with NULLs?" "Find total revenue and average order value."

> [!tip] Strong answer includes
> - NULLs ignored by all aggregates except COUNT(*)
> - AVG denominator is non-NULL count
> - One row returned when no GROUP BY
> - Casting to avoid integer truncation

---

## 2. GROUP BY
> 🔴 Tier 1 · _Tracker hint:_ SELECT dept, COUNT(*) FROM emp GROUP BY dept — groups rows by unique values

### Definition
`GROUP BY` partitions rows into groups that share the same values in the listed columns and returns **one row per group**, with aggregates computed per group.

```sql
SELECT dept, COUNT(*) AS headcount, SUM(salary) AS payroll
FROM   emp
GROUP  BY dept
ORDER  BY payroll DESC;
```
**Rule:** every column in SELECT must either be in GROUP BY or be inside an aggregate. MySQL's default `ONLY_FULL_GROUP_BY` mode enforces this (older MySQL silently picked an arbitrary value). NULLs form their own group. Logical order: FROM, WHERE, **GROUP BY**, HAVING, SELECT, ORDER BY, so you may sort by aggregates and filter rows (WHERE) before grouping. Grouping by an expression is allowed: `GROUP BY DATE_FORMAT(order_date,'%Y-%m')` in MySQL or `DATE_TRUNC('month', order_date)` in PostgreSQL.

### Example
`emp`: Sales has 3 people (salaries 40k, 50k, 60k); Ops has 2 (45k, 55k). Result: Sales, 3, 150k; Ops, 2, 100k. Two output rows from five input rows.

### In the news
See news box. The ONLY_FULL_GROUP_BY discipline is already the PostgreSQL norm, so writing strict GROUP BY queries keeps them portable.

### Interview angle
> [!question] How it is asked
> "Write a query for headcount and average salary per department." "Why do I get 'not in GROUP BY' error?"

> [!tip] Strong answer includes
> - One row per group
> - Select-list rule for non-aggregated columns
> - Filtering rows with WHERE before grouping
> - Group by expressions (month) for time-series summaries

---

## 3. HAVING Clause
> 🔴 Tier 1 · _Tracker hint:_ SELECT dept, AVG(salary) FROM emp GROUP BY dept HAVING AVG(salary) > 50000

### Definition
`HAVING` filters **groups** after aggregation, so it can use aggregate functions; `WHERE` cannot.

```sql
SELECT dept, AVG(salary) AS avg_sal
FROM   emp
GROUP  BY dept
HAVING AVG(salary) > 50000 AND COUNT(*) >= 3;
```
Best practice: put non-aggregate conditions in WHERE (they shrink the data before grouping) and keep only aggregate conditions in HAVING. Repeating the aggregate expression in HAVING is portable; using the alias (`HAVING avg_sal > 50000`) works in MySQL but not in PostgreSQL or SQL Server. See [[054 Filtering, Sorting & CASE]] for WHERE vs HAVING.

### Example
Order counts per customer: C1 = 12, C2 = 3, C3 = 7. `HAVING COUNT(*) > 5` returns C1 and C3. "Repeat customers" for a retention KPI are those with 2 or more orders: `HAVING COUNT(*) >= 2`.

### In the news
See news box. HAVING on large fact tables is where PostgreSQL 18's faster scans pay off, since the filter runs only after the full aggregate is built.

### Interview angle
> [!question] How it is asked
> "List departments with more than 5 employees." "Customers with total spend above 50,000."

> [!tip] Strong answer includes
> - HAVING after GROUP BY, aggregates allowed
> - Row filters belong in WHERE for speed
> - Portable form (repeat expression, not alias)
> - Combines multiple aggregate conditions

---

## 4. COUNT vs COUNT(*)
> 🔴 Tier 1 · _Tracker hint:_ COUNT(*) counts all rows incl. NULL; COUNT(col) excludes NULLs

### Definition
- `COUNT(*)` and `COUNT(1)` count **rows**, regardless of NULLs (they perform identically in modern optimisers).
- `COUNT(col)` counts rows where `col IS NOT NULL`.
- `COUNT(DISTINCT col)` counts distinct non-NULL values.

Useful identities: **missing values** = `COUNT(*) - COUNT(col)`; **completeness %** = $\frac{COUNT(col)}{COUNT(*)} \times 100$.

```sql
SELECT COUNT(*)                 AS total_rows,
       COUNT(email)             AS with_email,
       COUNT(*) - COUNT(email)  AS missing_email,
       COUNT(DISTINCT city)     AS distinct_cities
FROM customers;
```
After a LEFT JOIN, `COUNT(*)` counts unmatched left rows as 1 each, while `COUNT(right.id)` counts only real matches. Use the latter to avoid inflated counts (see [[056 JOINs — All Types]]).

### Example
`customers` has 1,000 rows; 850 have an email. `COUNT(*)` = 1,000, `COUNT(email)` = 850, missing = 150, completeness = 850 / 1,000 = **85%**.

### In the news
See news box. Data-quality checks like completeness are standard when migrating databases (for example MySQL 8.0 to 8.4) to confirm no rows were lost.

### Interview angle
> [!question] How it is asked
> "Difference between COUNT(*), COUNT(1) and COUNT(column)?"

> [!tip] Strong answer includes
> - Rows versus non-NULL values
> - COUNT(1) = COUNT(*)
> - Use to quantify missing data
> - Pitfall after LEFT JOIN

---

## 5. GROUP BY Multiple Columns
> 🔴 Tier 1 · _Tracker hint:_ GROUP BY dept, year — creates unique group per combination

### Definition
Listing several columns creates one group per **distinct combination** of values. Order of columns in GROUP BY does not change the groups (only the default sort in some engines).

```sql
SELECT dept, YEAR(hire_date) AS yr, COUNT(*) AS hires
FROM   emp
GROUP  BY dept, YEAR(hire_date)
ORDER  BY dept, yr;
```
The number of groups is at most the product of the distinct counts. More grouping columns mean finer detail and fewer rows per group, so aggregates may become noisy or sparse. **Missing combinations** (a dept with no hires in some year) do not appear in the output; to show zeros, build a calendar or dimension table and LEFT JOIN to it.

### Example
Sales: (North, 2025, 100), (North, 2025, 50), (North, 2026, 80), (South, 2025, 70). `GROUP BY region, year` with SUM gives: North 2025 = 150, North 2026 = 80, South 2025 = 70. South 2026 is absent, not zero.

### In the news
See news box. Multi-dimensional grouping is the foundation of the ROLLUP/CUBE reports described next, which PostgreSQL supports fully.

### Interview angle
> [!question] How it is asked
> "Revenue by region and month." "Why is a month missing from my report?"

> [!tip] Strong answer includes
> - One group per combination
> - Explains missing combinations and the calendar-table fix
> - Controls output order with ORDER BY
> - Sensible granularity (not so fine that groups are tiny)

---

## 6. ROLLUP & CUBE
> 🔴 Tier 1 · _Tracker hint:_ WITH ROLLUP adds subtotals; CUBE adds all combinations (advanced analytics)

### Definition
- **ROLLUP(a, b)** produces groups for (a, b), (a), and the grand total (): hierarchical subtotals, right to left.
- **CUBE(a, b)** produces all combinations: (a, b), (a), (b) and (): cross-tab subtotals.
- Subtotal rows show NULL in the rolled-up column; use `GROUPING(col)` (returns 1 for a subtotal NULL) to label them.

```sql
-- PostgreSQL / SQL Server / Oracle
SELECT region, product, SUM(amount) AS rev
FROM   sales
GROUP  BY ROLLUP (region, product);

-- MySQL (8.0 and 8.4): only ROLLUP, no CUBE
SELECT region, product, SUM(amount) AS rev
FROM   sales
GROUP  BY region, product WITH ROLLUP;
-- label subtotal rows: COALESCE(region, 'ALL REGIONS') or CASE WHEN GROUPING(region)=1 THEN ...
```
Number of grouping sets: ROLLUP over n columns gives n+1 levels; CUBE gives $2^n$ combinations.

### Example
Sales: North-A 100, North-B 50, South-A 70. `ROLLUP(region, product)` returns: North-A 100; North-B 50; **North-NULL 150**; South-A 70; **South-NULL 70**; **NULL-NULL 220** (grand total). CUBE would additionally add product subtotals: A = 170, B = 50.

### In the news
See news box. MySQL's lack of CUBE and GROUPING SETS versus PostgreSQL's full support is a concrete reason analysts moving across the top two open-source databases must check dialect support.

### Interview angle
> [!question] How it is asked
> "How do you get subtotals and a grand total in a single query?"

> [!tip] Strong answer includes
> - ROLLUP (hierarchical) versus CUBE (all combinations)
> - NULL meaning subtotal; GROUPING() to distinguish from real NULLs
> - Dialect: MySQL WITH ROLLUP only
> - Count of grouping sets (n+1 versus 2^n)

---

## 7. GROUPING SETS
> 🔴 Tier 1 · _Tracker hint:_ GROUPING SETS((dept),(year),()) — flexible multi-level aggregation

### Definition
`GROUPING SETS` lets you list **exactly** which groupings you want in one pass, equivalent to a `UNION ALL` of several GROUP BY queries but scanning the table once. `ROLLUP` and `CUBE` are shorthand for particular grouping sets.

```sql
SELECT dept, year, SUM(amount) AS total
FROM   sales
GROUP  BY GROUPING SETS ((dept), (year), ());
-- same as: dept totals + year totals + grand total
```
Equivalences: `ROLLUP(a,b)` = `GROUPING SETS((a,b),(a),())`; `CUBE(a,b)` = `GROUPING SETS((a,b),(a),(b),())`. Columns not in a set appear as NULL; use `GROUPING(col)` to tell subtotal NULLs from data NULLs. Supported in PostgreSQL, SQL Server, Oracle; **not in MySQL**, where you emulate with UNION ALL.

### Example
Sales by dept: A = 100, B = 200; by year: 2025 = 150, 2026 = 150. `GROUPING SETS((dept),(year),())` returns 2 + 2 + 1 = **5 rows**: A 100, B 200, 2025 150, 2026 150 and the grand total 300.

### In the news
See news box. As PostgreSQL's usage share leads the 2025 survey, GROUPING SETS fluency is increasingly useful for reporting queries.

### Interview angle
> [!question] How it is asked
> "Produce totals by department, by year and overall in one query."

> [!tip] Strong answer includes
> - Single scan versus multiple UNION ALL queries
> - Relationship to ROLLUP/CUBE
> - GROUPING() function
> - Knows MySQL fallback (UNION ALL)

---

## 8. Conditional Aggregation
> 🔴 Tier 1 · _Tracker hint:_ SUM(CASE WHEN status='shipped' THEN amount ELSE 0 END) AS shipped_rev

### Definition
Put a `CASE` expression inside an aggregate to compute several filtered metrics in a single pass; this is also the portable way to **pivot** rows into columns.

```sql
SELECT region,
       SUM(CASE WHEN status = 'SHIPPED'   THEN amount ELSE 0 END) AS shipped_rev,
       SUM(CASE WHEN status = 'CANCELLED' THEN amount ELSE 0 END) AS cancelled_rev,
       COUNT(CASE WHEN status = 'SHIPPED' THEN 1 END)             AS shipped_orders,   -- COUNT ignores NULL
       AVG(CASE WHEN status = 'SHIPPED' THEN amount END)          AS shipped_aov
FROM   orders
GROUP  BY region;

-- PostgreSQL: SUM(amount) FILTER (WHERE status = 'SHIPPED')
```
For COUNT, omit ELSE so non-matching rows become NULL and are not counted; with `ELSE 0`, COUNT would count every row. For AVG, `ELSE 0` would drag the average down, so omit ELSE.

### Example
Orders: SHIPPED 100, SHIPPED 300, CANCELLED 200. `SUM(CASE ... SHIPPED ... ELSE 0)` = 400. `AVG(CASE ... SHIPPED THEN amount END)` = 200 (ignores the NULL). With `ELSE 0` the average would be 400/3 = 133.33, which is wrong.

### In the news
See news box. PostgreSQL's `FILTER (WHERE ...)` clause is a cleaner alternative and shows how the leading dialect improves on CASE-inside-aggregate.

### Interview angle
> [!question] How it is asked
> "Show shipped and cancelled revenue as separate columns per region." "Compute on-time delivery rate per supplier."

> [!tip] Strong answer includes
> - SUM(CASE) pattern and the COUNT(CASE ... END) pattern without ELSE
> - Pivot use
> - Rate formula: SUM(CASE ... 1 ELSE 0 END) / COUNT(*)
> - ELSE 0 pitfall in AVG

---

## 9. String Aggregation
> 🔴 Tier 1 · _Tracker hint:_ GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') in MySQL

### Definition
String aggregation joins values from many rows into one string per group.

| Dialect | Syntax |
|---|---|
| MySQL | `GROUP_CONCAT(name ORDER BY name SEPARATOR ', ')` |
| PostgreSQL | `STRING_AGG(name, ', ' ORDER BY name)` |
| SQL Server 2017+ | `STRING_AGG(name, ', ') WITHIN GROUP (ORDER BY name)` |
| Oracle | `LISTAGG(name, ', ') WITHIN GROUP (ORDER BY name)` |

```sql
SELECT dept,
       GROUP_CONCAT(DISTINCT name ORDER BY name SEPARATOR ', ') AS team
FROM   emp
GROUP  BY dept;
```
MySQL caution: `group_concat_max_len` defaults to 1024 characters and silently truncates longer results; raise it with `SET SESSION group_concat_max_len = 100000;`. NULL values are skipped. Typical uses: list of SKUs per order, suppliers per category, flattening tags for reports.

### Example
Order 501 has items Pen, Book, Bag. `GROUP_CONCAT(item ORDER BY item SEPARATOR ', ')` returns **'Bag, Book, Pen'** for that order: three rows become one.

### In the news
See news box. The syntax split across MySQL, PostgreSQL and SQL Server is a good example of why interviews ask which dialect you know.

### Interview angle
> [!question] How it is asked
> "Show each customer with all their order ids in one column."

> [!tip] Strong answer includes
> - Right function for the dialect
> - Ordering and separator options
> - The MySQL truncation limit
> - Where it is used (reports) and where not (feeding further computation; use arrays or normalised rows)

---

## 10. SCM Use Case
> 🔴 Tier 1 · _Tracker hint:_ Supplier performance: SELECT supplier, AVG(lead_time), COUNT(orders) GROUP BY supplier

### Definition
Supplier scorecards are aggregation queries: group purchase-order lines by supplier and compute lead time, on-time delivery, defect rate and spend.

```sql
SELECT s.supplier_name,
       COUNT(*)                                         AS n_pos,
       AVG(DATEDIFF(r.receipt_date, p.order_date))      AS avg_lead_days,   -- MySQL; PostgreSQL: receipt_date - order_date
       SUM(CASE WHEN r.receipt_date <= p.promised_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS otd_pct,
       SUM(p.qty * p.unit_price)                        AS spend
FROM   purchase_orders p
JOIN   receipts r  ON r.po_id = p.po_id
JOIN   suppliers s ON s.supplier_id = p.supplier_id
GROUP  BY s.supplier_name
HAVING COUNT(*) >= 5
ORDER  BY otd_pct DESC;
```
Also useful: `STDDEV(lead_days)` for **lead-time variability**, which drives safety stock more than the mean does.

### Example
Supplier A: 3 POs with lead times 5, 7, 6 days, 2 of 3 on time. Supplier B: 2 POs with 10 and 12 days, 1 of 2 on time. A: avg = 18/3 = **6 days**, OTD = 2/3 = **66.7%**. B: avg = 22/2 = **11 days**, OTD = 50%. With few POs, apply HAVING to ignore unreliable samples.

### In the news
See news box. Faster scans in PostgreSQL 18 help when scorecards aggregate tens of millions of PO lines; the logic stays the same across engines.

### Interview angle
> [!question] How it is asked
> "Write a query to rank suppliers by on-time delivery." "Which suppliers have the highest lead-time variability?"

> [!tip] Strong answer includes
> - GROUP BY supplier with AVG lead time, COUNT of POs, OTD via conditional aggregation
> - HAVING for minimum sample size
> - Mentions variability (STDDEV), not just mean
> - Ties to action: dual sourcing or safety stock for volatile suppliers

---

## 11. ⭐ Advanced: Aggregation Pitfalls — Fan-out and Double Counting
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Fan-out** happens when you join a table at a coarser grain to one at a finer grain and then SUM a coarse-grain measure: each coarse row is repeated once per matching fine row, so totals inflate.

Rules of thumb:
1. State the **grain** (what one row represents) of every table before joining.
2. **Aggregate before joining** (pre-aggregate in a subquery or CTE to the join key), then join one-to-one.
3. After a join, check `COUNT(*)` against the expected row count.
4. `COUNT(DISTINCT id)` fixes counts but **not sums**; sums need pre-aggregation.

```sql
-- wrong: order amount repeated for each line item
SELECT SUM(o.amount) FROM orders o JOIN order_items i ON i.order_id = o.id;

-- right: aggregate the fine table first
WITH it AS (SELECT order_id, SUM(qty) AS units FROM order_items GROUP BY order_id)
SELECT SUM(o.amount), SUM(it.units)
FROM orders o JOIN it ON it.order_id = o.id;
```

### Example
Order 1 has amount 1,000 and 3 line items. Joining and summing `o.amount` gives 3 x 1,000 = **3,000** for this one order. If total revenue should be 1,000, the report is overstated by 200%. Pre-aggregating items gives one row per order and the correct 1,000.

### In the news
See news box. Reconciling totals before and after a database migration (MySQL 8.0 to 8.4) is the practical check for this kind of silent error.

### Interview angle
> [!question] How it is asked
> "My revenue total doubled after adding a join. What happened?"

> [!tip] Strong answer includes
> - Names fan-out and grain
> - Pre-aggregate in a CTE or subquery
> - Reconciles against a control total
> - Distinguishes COUNT DISTINCT fix from SUM fix

---

## 12. ⭐ Advanced: Percentiles, Median and Approximate Aggregates
> ⭐ Advanced · _Added beyond the tracker_

### Definition
AVG is distorted by outliers (one Rs 10 lakh order); **median** (50th percentile) is robust. Support differs by dialect:

```sql
-- PostgreSQL / Oracle: ordered-set aggregates
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_amt,
       PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY amount) AS p90
FROM orders;

-- MySQL: no built-in median; use window functions
SELECT AVG(amount) AS median_amt FROM (
  SELECT amount,
         ROW_NUMBER() OVER (ORDER BY amount) AS rn,
         COUNT(*)     OVER ()                AS cnt
  FROM orders) t
WHERE rn IN (FLOOR((cnt+1)/2), CEIL((cnt+1)/2));
```
`PERCENTILE_CONT` interpolates; `PERCENTILE_DISC` returns an actual value. Warehouses offer approximate versions (`APPROX_COUNT_DISTINCT`, `APPROX_PERCENTILE`) that trade a small error for speed on billions of rows. Delivery SLAs are often stated as **P90/P95 lead time**.

### Example
Order values: 100, 120, 130, 140, 1,000,000. Mean = 1,000,490 / 5 = **200,098**, which describes no real order. Median = **130**. Reporting the median (and P90) gives a true picture of a typical order.

### In the news
See news box. MySQL needs a window-function workaround for the median while PostgreSQL has it built in, another practical dialect gap.

### Interview angle
> [!question] How it is asked
> "Why use median over average?" "Find the median salary in SQL."

> [!tip] Strong answer includes
> - Outlier robustness and skewed distributions
> - Median via PERCENTILE_CONT or ROW_NUMBER trick
> - P90/P95 for SLAs and lead times
> - Approximate aggregates for scale

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
