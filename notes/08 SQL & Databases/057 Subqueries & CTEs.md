---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "Subqueries & CTEs"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Subqueries & CTEs

⬅ [[056 JOINs — All Types]] · [[_Index - SQL & Databases|SQL & Databases]] · [[058 Window Functions]] ➡

> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Scalar Subquery]]
2. [[#2. IN Subquery]]
3. [[#3. EXISTS Subquery]]
4. [[#4. Correlated Subquery]]
5. [[#5. Subquery in FROM (Derived Table)]]
6. [[#6. Subquery vs JOIN]]
7. [[#7. NOT IN vs NOT EXISTS]]
8. [[#8. Subquery for Ranking]]
9. [[#9. ANY / ALL Operators]]
10. [[#10. Nested Subqueries]]
11. [[#11. ⭐ Advanced: Lateral Joins and Top-N per Group]]
12. [[#12. ⭐ Advanced: Common Table Expressions vs Temp Tables vs Views]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Query engines keep getting better at optimising subqueries
> **PostgreSQL 18 (25 Sep 2025).** New release with an asynchronous I/O subsystem (reported gains up to about 3x in some scenarios), skip-scan lookups on multicolumn B-tree indexes and virtual generated columns. Faster scans and smarter index use reduce the cost of subquery-heavy analytics. ([LWN](https://lwn.net/Articles/1039483/))
>
> **PostgreSQL is the most-used database in the 2025 Stack Overflow survey** (**55.6%** of all respondents, **58.2%** of professionals; MySQL **40.5%**, SQLite **37.5%**, SQL Server **30.1%**). It is also the most-desired for the third year running. ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
>
> **MySQL 8.0 end of life (30 Apr 2026).** Extended support ended on 30 April 2026; MySQL 8.4 is the recommended LTS. Teams upgrading re-test queries whose plans depend on optimiser behaviour, including subqueries and CTEs. ([OpenLogic](https://www.openlogic.com/blog/mysql-8-end-of-life))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Scalar Subquery
> 🔴 Tier 1 · _Tracker hint:_ SELECT name, (SELECT MAX(salary) FROM emp) AS max_sal FROM emp

### Definition
A **scalar subquery** returns exactly **one row and one column**, so it can be used anywhere a single value is allowed: SELECT list, WHERE, HAVING, SET in UPDATE.

```sql
SELECT name, salary,
       (SELECT MAX(salary) FROM emp)               AS max_sal,
       salary - (SELECT AVG(salary) FROM emp)      AS diff_from_avg
FROM   emp
WHERE  salary > (SELECT AVG(salary) FROM emp);
```
If it returns more than one row you get an error ("subquery returns more than 1 row"); if it returns zero rows the value is NULL. An uncorrelated scalar subquery is executed once and its value reused. Typical uses: compare each row to a global benchmark (average, maximum, latest date) without a join. A window function (`AVG(salary) OVER ()`) is the modern alternative when you also need per-row context ([[058 Window Functions]]).

### Example
Salaries: 40k, 50k, 90k. Average = 180k / 3 = **60k**. `WHERE salary > (SELECT AVG(salary) FROM emp)` returns only the 90k row. The subquery runs once, not three times.

### In the news
See news box. Both MySQL 8.4 and PostgreSQL 18 evaluate an uncorrelated scalar subquery once, so it is cheap even on big tables.

### Interview angle
> [!question] How it is asked
> "List employees earning more than the company average." "Show each order with the overall maximum order value."

> [!tip] Strong answer includes
> - One row and one column requirement and the error otherwise
> - Evaluated once if uncorrelated
> - Use in WHERE and SELECT
> - Mentions window function alternative

---

## 2. IN Subquery
> 🔴 Tier 1 · _Tracker hint:_ WHERE dept_id IN (SELECT id FROM dept WHERE region='South')

### Definition
`col IN (subquery)` keeps rows whose value appears in the **set** returned by the subquery (single column, many rows).

```sql
SELECT * FROM emp
WHERE  dept_id IN (SELECT id FROM dept WHERE region = 'South');
```
Equivalent to a **semi-join**: each outer row appears once even if the value occurs multiple times in the subquery (unlike a JOIN, which would duplicate rows). Modern optimisers convert IN-subqueries to semi-joins, so performance is usually similar to EXISTS or JOIN. `NOT IN` is dangerous with NULLs (see sub-topic 7). The subquery must return a single column; multi-column IN is possible in some dialects: `WHERE (a, b) IN (SELECT a, b ...)`. Use IN when you want to filter by a list derived from another table and do not need columns from that table.

### Example
dept ids in South: {1, 4}. Employees: Ravi (dept 1), Asha (dept 2), Meera (dept 4), Kiran (dept 1). IN-subquery returns Ravi, Meera, Kiran. A JOIN returns the same here, but if `dept` had two rows with id 1 (data error), the JOIN would duplicate Ravi and Kiran while IN would not.

### In the news
See news box. Because PostgreSQL and MySQL 8.4 rewrite IN to semi-joins, readability is the main reason to choose it.

### Interview angle
> [!question] How it is asked
> "Find employees who work in departments located in the South region." "IN versus JOIN?"

> [!tip] Strong answer includes
> - Set membership, one column returned
> - No duplication versus JOIN
> - Equivalent semi-join in the optimiser
> - Warns about NOT IN and NULLs

---

## 3. EXISTS Subquery
> 🔴 Tier 1 · _Tracker hint:_ WHERE EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id)

### Definition
`EXISTS (subquery)` is TRUE if the subquery returns **at least one row**; the selected columns are irrelevant (`SELECT 1` is convention), and evaluation can **stop at the first match**.

```sql
SELECT c.id, c.name
FROM   customers c
WHERE  EXISTS (SELECT 1 FROM orders o
               WHERE o.cust_id = c.id AND o.order_date >= '2026-01-01');
```
It is usually written as a **correlated** subquery (links to the outer row), which the optimiser turns into a semi-join. EXISTS returns TRUE/FALSE only, never UNKNOWN, so it is **NULL-safe**, unlike IN. Choose EXISTS over IN when the subquery table is large or when NULLs are possible, and for "has at least one related record" logic. `NOT EXISTS` is the safe anti-join.

### Example
Customers {1, 2, 3}; orders exist for customers 1 and 3 in 2026. `EXISTS` returns customers 1 and 3. `NOT EXISTS` returns customer 2: the customers who have not ordered this year, a typical churn list.

### In the news
See news box. The EXISTS pattern is the same in every engine in the survey top five, which makes it portable.

### Interview angle
> [!question] How it is asked
> "Customers with at least one order in 2026." "EXISTS versus IN?"

> [!tip] Strong answer includes
> - Boolean test, stops at first match, SELECT 1 convention
> - NULL-safe
> - Semi-join, no duplicates
> - When it beats IN (large inner set, NULLs) and equivalence in modern optimisers

---

## 4. Correlated Subquery
> 🔴 Tier 1 · _Tracker hint:_ References outer query column; runs once per outer row; slower

### Definition
A **correlated subquery** references a column from the outer query, so it cannot run on its own and is conceptually executed **once per outer row**.

```sql
-- employees earning more than the average of THEIR department
SELECT e.name, e.dept_id, e.salary
FROM   emp e
WHERE  e.salary > (SELECT AVG(x.salary)
                   FROM   emp x
                   WHERE  x.dept_id = e.dept_id);
```
Cost: with n outer rows, up to n subquery executions, roughly O(n x m) without an index on the correlation column. Optimisers often **decorrelate** the query into a join, but not always. Faster alternatives: pre-aggregate in a derived table/CTE and join, or use a window function (`AVG(salary) OVER (PARTITION BY dept_id)`). Index the correlation column (`dept_id`).

### Example
Dept A: 40k, 60k (avg 50k). Dept B: 70k, 90k (avg 80k). Correlated filter returns 60k (above A's 50k) and 90k (above B's 80k). A global average (65k) would wrongly return 70k and 90k and miss the 60k person.

### In the news
See news box. Upgrading from MySQL 8.0 to 8.4 can change plans for correlated subqueries, so re-check with EXPLAIN on production-size data.

### Interview angle
> [!question] How it is asked
> "Employees earning above their department average." "Why is my correlated subquery slow?"

> [!tip] Strong answer includes
> - Definition: references outer column, runs per outer row
> - Shows a rewrite with a join to an aggregate or a window function
> - Index on the correlation column
> - Uses EXPLAIN to confirm decorrelation

---

## 5. Subquery in FROM (Derived Table)
> 🔴 Tier 1 · _Tracker hint:_ SELECT * FROM (SELECT dept, AVG(sal) AS avg_sal FROM emp GROUP BY dept) t WHERE t.avg_sal > 60000

### Definition
A subquery in the FROM clause is a **derived table** (inline view): it produces a temporary result set you can filter, join or aggregate again. An **alias is mandatory** in MySQL and SQL Server (and in PostgreSQL before version 16); always add one for portability.

```sql
SELECT t.dept, t.avg_sal
FROM  (SELECT dept, AVG(salary) AS avg_sal
       FROM   emp GROUP BY dept) AS t
WHERE  t.avg_sal > 60000;

-- two-level aggregation: average of department totals
SELECT AVG(dept_total) FROM
 (SELECT dept, SUM(salary) AS dept_total FROM emp GROUP BY dept) d;
```
Uses: aggregate-then-join (avoids fan-out), aggregate of aggregates, filtering on a window function result (you cannot put a window function in WHERE, so wrap it: `SELECT * FROM (SELECT ..., ROW_NUMBER() OVER (...) rn FROM t) x WHERE rn = 1`). CTEs express the same thing with better readability.

### Example
Dept totals: A = 100k, B = 200k, C = 300k. Average of department totals = 600k / 3 = **200k**. This needs two levels: first SUM per dept, then AVG over those sums; `AVG(SUM(salary))` is not allowed in one step.

### In the news
See news box. Since PostgreSQL 12 and MySQL 8, simple derived tables and non-recursive CTEs are inlined into the main query, so there is little performance penalty versus joins.

### Interview angle
> [!question] How it is asked
> "Average of per-department totals." "Latest order per customer without window functions."

> [!tip] Strong answer includes
> - Alias requirement
> - Aggregate-then-join and two-level aggregation
> - Wrapping window functions to filter on them
> - Offers the CTE rewrite for readability

---

## 6. Subquery vs JOIN
> 🔴 Tier 1 · _Tracker hint:_ JOINs usually faster; subqueries more readable for complex logic

### Definition
Many questions can be answered either way. Differences:

| | JOIN | Subquery |
|---|---|---|
| Columns from the second table | Yes | Not directly (only IN/EXISTS filter) |
| Duplicates | Multiplies rows on one-to-many | IN/EXISTS do not duplicate |
| NULL behaviour | NULL keys do not match | NOT IN has the NULL trap |
| Readability | Good for combining columns | Good for "filter by" and stepwise logic |
| Performance | Predictable, indexable | Modern optimisers rewrite many to joins; correlated ones can be slow |

Rule of thumb: **need columns from both tables, use a JOIN; only need to filter by existence, use EXISTS/IN**. Correlated scalar subqueries in SELECT are often better as a join to a pre-aggregated table. Do not rely on folklore ("joins are always faster"): compare `EXPLAIN` plans and timings on real data.

### Example
"Customers with at least one order." JOIN version returns a customer once per order (duplicates; needs DISTINCT). EXISTS version returns each customer once, no DISTINCT, and stops at the first match. For "customer name with order amount" you need the JOIN because the amount is a column of orders.

### In the news
See news box. As planners improve (PostgreSQL 18, MySQL 8.4), the readable form is increasingly the right default, with performance verified by EXPLAIN.

### Interview angle
> [!question] How it is asked
> "Is a JOIN faster than a subquery?" "Rewrite this subquery using a JOIN."

> [!tip] Strong answer includes
> - Depends on the optimiser; verify with EXPLAIN
> - When each is natural (columns needed versus existence check)
> - Duplication and NULL differences
> - Offers CTE/window alternatives for complex logic

---

## 7. NOT IN vs NOT EXISTS
> 🔴 Tier 1 · _Tracker hint:_ NOT IN fails with NULLs; prefer NOT EXISTS for safety

### Definition
`x NOT IN (a, b, NULL)` expands to `x <> a AND x <> b AND x <> NULL`. The last term is UNKNOWN, so the whole condition is never TRUE and **no rows are returned** if the list contains any NULL. `NOT EXISTS` tests row existence and is unaffected by NULLs.

```sql
-- BROKEN if blocked_suppliers.sup_id can be NULL
SELECT * FROM suppliers
WHERE  id NOT IN (SELECT sup_id FROM blocked_suppliers);

-- SAFE
SELECT * FROM suppliers s
WHERE  NOT EXISTS (SELECT 1 FROM blocked_suppliers b WHERE b.sup_id = s.id);

-- also safe: anti-join
SELECT s.* FROM suppliers s
LEFT JOIN blocked_suppliers b ON b.sup_id = s.id
WHERE b.sup_id IS NULL;
```
A NOT IN is acceptable only when the subquery column is declared NOT NULL or filtered with `IS NOT NULL`. Also note that `NOT IN` with a literal list that includes NULL fails the same way.

### Example
Suppliers {1, 2, 3}; blocked table has sup_id {2, NULL}. NOT IN returns **0 rows** (expected 1 and 3). NOT EXISTS returns suppliers 1 and 3 as intended.

### In the news
See news box. This NULL semantics is part of the SQL standard and identical in MySQL, PostgreSQL and SQL Server, so the pitfall does not go away on migration.

### Interview angle
> [!question] How it is asked
> "Why does NOT IN return an empty result?" (a favourite trap question)

> [!tip] Strong answer includes
> - Three-valued logic explanation with the expansion
> - NOT EXISTS or LEFT JOIN ... IS NULL as fixes
> - Filtering NULLs inside the subquery
> - Notes NOT NULL constraints make NOT IN safe

---

## 8. Subquery for Ranking
> 🔴 Tier 1 · _Tracker hint:_ WHERE salary = (SELECT MAX(salary) FROM emp WHERE dept = e.dept)

### Definition
Before window functions, "top per group" and "Nth highest" were solved with subqueries.

```sql
-- highest-paid employee in each department (ties all returned)
SELECT e.*
FROM   emp e
WHERE  e.salary = (SELECT MAX(salary) FROM emp WHERE dept = e.dept);

-- second highest salary overall
SELECT MAX(salary) FROM emp
WHERE  salary < (SELECT MAX(salary) FROM emp);

-- Nth highest via LIMIT/OFFSET (N = 3)
SELECT DISTINCT salary FROM emp ORDER BY salary DESC LIMIT 1 OFFSET 2;

-- Nth highest via correlated count (N = 3)
SELECT DISTINCT e1.salary FROM emp e1
WHERE (SELECT COUNT(DISTINCT e2.salary) FROM emp e2 WHERE e2.salary > e1.salary) = 2;
```
The Nth highest uses N-1 as the count of strictly higher distinct values. Modern equivalent: `DENSE_RANK() OVER (ORDER BY salary DESC) = N` ([[058 Window Functions]]). If fewer than N distinct salaries exist the result is empty/NULL, so state how you handle it.

### Example
Salaries: 90, 80, 80, 70. Second highest overall = MAX of salaries below 90 = **80**. Third highest distinct = 70 (distinct values 90, 80, 70). Per department, a tie at the top returns both employees, which may or may not be intended.

### In the news
See news box. Both leading engines support window functions, so ranking subqueries now appear mainly in interviews and legacy code.

### Interview angle
> [!question] How it is asked
> "Find the second (or Nth) highest salary." "Top earner per department."

> [!tip] Strong answer includes
> - At least two methods (MAX with `<`, OFFSET, or DENSE_RANK)
> - Handles ties and duplicates (DISTINCT, DENSE_RANK)
> - Handles N larger than available values (returns NULL)
> - Prefers window functions in production

---

## 9. ANY / ALL Operators
> 🔴 Tier 1 · _Tracker hint:_ WHERE salary > ALL (SELECT salary FROM emp WHERE dept='HR')

### Definition
Compare a value with **every** or **some** value returned by a subquery.
- `x > ANY (subq)` (or `SOME`): true if x is greater than **at least one** value, i.e. `x > MIN(subq)`.
- `x > ALL (subq)`: true if x is greater than **every** value, i.e. `x > MAX(subq)`.
- `x = ANY (subq)` is the same as `x IN (subq)`; `x <> ALL (subq)` is the same as `x NOT IN (subq)` (and inherits the NULL trap).

```sql
SELECT name, salary FROM emp
WHERE  salary > ALL (SELECT salary FROM emp WHERE dept = 'HR');   -- beats every HR salary

SELECT name FROM emp
WHERE  salary > ANY (SELECT salary FROM emp WHERE dept = 'HR');   -- beats at least one HR salary
```
Edge cases: `> ALL` over an **empty** set is TRUE; `> ANY` over an empty set is FALSE. NULLs in the subquery make ALL comparisons UNKNOWN. SQL Server and MySQL support ANY/ALL; MIN/MAX rewrites are often clearer and faster.

### Example
HR salaries: 40k, 50k, 60k. `> ALL` means salary > 60k (the maximum): 70k passes, 55k does not. `> ANY` means salary > 40k (the minimum): 55k and 70k both pass.

### In the news
See news box. PostgreSQL also offers `= ANY(array)` for arrays, a form common in application code.

### Interview angle
> [!question] How it is asked
> "Employees earning more than everyone in HR." "Difference between ANY and ALL?"

> [!tip] Strong answer includes
> - ANY ~ at least one (MIN), ALL ~ every (MAX)
> - Equivalence of `= ANY` with IN
> - Empty-set and NULL edge cases
> - Simpler MIN/MAX rewrite

---

## 10. Nested Subqueries
> 🔴 Tier 1 · _Tracker hint:_ Subquery within a subquery; limit to 2-3 levels for readability

### Definition
A subquery can contain another subquery. Execution works from the innermost outwards (for uncorrelated ones).

```sql
-- employees in departments whose location is in the highest-revenue region
SELECT name FROM emp
WHERE dept_id IN (
    SELECT id FROM dept
    WHERE  region = (
        SELECT region FROM sales
        GROUP  BY region
        ORDER  BY SUM(amount) DESC
        LIMIT  1));
```
Beyond two or three levels, readability, debugging and maintainability collapse. Refactor into **CTEs** that name each step (`WITH top_region AS (...), depts AS (...) SELECT ...`), temporary tables or views. Check that every level returns the shape its parent expects (scalar versus set). Name aliases clearly and indent consistently.

### Example
Region revenue: South 500, West 300. Innermost query returns 'South'. The middle returns department ids in South, say {1, 4}. The outer returns the employees of departments 1 and 4. Rewriting the three layers as three named CTEs gives identical results but can be tested step by step.

### In the news
See news box. Both PostgreSQL and MySQL 8+ support CTEs, so deep nesting is no longer needed for portability.

### Interview angle
> [!question] How it is asked
> "Walk me through this nested query." or "Refactor this query to be readable."

> [!tip] Strong answer includes
> - Inside-out evaluation explanation
> - Recommends CTEs for 3+ levels
> - Checks scalar vs set at each level
> - Validates each step independently with sample output

---

## 11. ⭐ Advanced: Lateral Joins and Top-N per Group
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **LATERAL** subquery (PostgreSQL, MySQL 8.0.14+; `CROSS APPLY`/`OUTER APPLY` in SQL Server) in the FROM clause may reference columns from tables to its left, so it runs per outer row **and can return multiple rows**. This solves "top N per group" elegantly.

```sql
-- latest 3 orders for every customer
SELECT c.id, c.name, o.order_id, o.order_date
FROM   customers c
CROSS JOIN LATERAL (                 -- PostgreSQL; MySQL: JOIN LATERAL (...) ON TRUE
    SELECT order_id, order_date
    FROM   orders
    WHERE  cust_id = c.id
    ORDER  BY order_date DESC
    LIMIT  3) o;
```
Alternatives for top-N per group: `ROW_NUMBER() OVER (PARTITION BY cust_id ORDER BY order_date DESC) <= 3` in a derived table (the most common), or a correlated count. LATERAL shines when an index on (cust_id, order_date) makes each probe cheap, and when the per-group logic is complex (calls to table functions, unnesting).

### Example
Customer 1 has orders on 1, 5, 9, 12 Oct. Top 3 latest: 12, 9, 5 Oct. The LATERAL subquery runs once per customer, sorts that customer's orders using the index and returns only 3 rows, versus ranking every order in the table with a window function.

### In the news
See news box. LATERAL support in MySQL 8.0.14+ (and thus 8.4) closes a long-standing gap with PostgreSQL for top-N per group queries.

### Interview angle
> [!question] How it is asked
> "Show the 3 most recent orders for each customer." "Top 2 products per category."

> [!tip] Strong answer includes
> - ROW_NUMBER partition solution first (most expected)
> - LATERAL/APPLY as the per-row alternative
> - Index to support the per-group probe
> - Tie handling (RANK vs ROW_NUMBER)

---

## 12. ⭐ Advanced: Common Table Expressions vs Temp Tables vs Views
> ⭐ Advanced · _Added beyond the tracker_

### Definition
All three name an intermediate result, with different lifetimes.

| | CTE (`WITH`) | Temp table | View |
|---|---|---|---|
| Lifetime | One statement | Session | Permanent definition |
| Stores data? | No (logical) | Yes, physically | No (stored query) |
| Indexable | No | Yes | Only underlying tables (or materialised view) |
| Best for | Readability, recursion, stepwise logic | Reusing a heavy result many times, large intermediate sets | Reusable business logic, security (hide columns) |

```sql
WITH recent AS (SELECT * FROM orders WHERE order_date >= '2026-09-01')
SELECT cust_id, SUM(amount) FROM recent GROUP BY cust_id;

CREATE TEMPORARY TABLE recent AS SELECT * FROM orders WHERE order_date >= '2026-09-01';
CREATE VIEW v_recent_orders AS SELECT * FROM orders WHERE order_date >= '2026-09-01';
```
Optimiser behaviour: PostgreSQL (12+) inlines a non-recursive CTE referenced once; with `WITH x AS MATERIALIZED (...)` it is computed once. If a CTE is referenced several times, check whether it is recomputed. A **materialised view** stores results and needs refresh (`REFRESH MATERIALIZED VIEW` in PostgreSQL).

### Example
A report uses a heavy 20-million-row filtered set three times. Writing it as a CTE referenced three times may recompute it (engine-dependent). Writing it once into an indexed temp table and querying it three times avoids repeating the 20-million-row scan.

### In the news
See news box. PostgreSQL's controls (MATERIALIZED / NOT MATERIALIZED) show how the leading engine lets you choose between readability and a computed-once result.

### Interview angle
> [!question] How it is asked
> "CTE vs temp table vs view: when do you use which?" "Is a CTE faster than a subquery?"

> [!tip] Strong answer includes
> - Lifetimes and storage differences
> - CTE is mainly readability and recursion, not a guaranteed speed-up
> - Temp table when reused multiple times or needing indexes
> - Views for reuse and access control; materialised views for caching

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
