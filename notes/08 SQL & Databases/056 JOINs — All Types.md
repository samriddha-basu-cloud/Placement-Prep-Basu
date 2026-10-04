---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "JOINs — All Types"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# JOINs — All Types

⬅ [[055 Aggregations & GROUP BY]] · [[_Index - SQL & Databases|SQL & Databases]] · [[057 Subqueries & CTEs]] ➡

> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. INNER JOIN]]
2. [[#2. LEFT JOIN (LEFT OUTER)]]
3. [[#3. RIGHT JOIN]]
4. [[#4. FULL OUTER JOIN]]
5. [[#5. CROSS JOIN]]
6. [[#6. SELF JOIN]]
7. [[#7. Multi-table JOIN]]
8. [[#8. JOIN on Multiple Conditions]]
9. [[#9. Non-equi JOIN]]
10. [[#10. SCM JOIN Example]]
11. [[#11. ⭐ Advanced: Semi-joins, Anti-joins and the ON vs WHERE Trap]]
12. [[#12. ⭐ Advanced: Join Algorithms and Performance]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Join-heavy workloads and the engines that run them
> **PostgreSQL 18 (25 Sep 2025).** The release adds an asynchronous I/O subsystem (reported gains up to about 3x in some scenarios, covering sequential scans, bitmap heap scans and vacuum) and skip-scan lookups on multicolumn B-tree indexes. Joins on large tables are dominated by scan and index cost, so these changes matter for join-heavy reporting. ([LWN](https://lwn.net/Articles/1039483/))
>
> **PostgreSQL leads the 2025 Stack Overflow survey** with **55.6%** of all respondents (**58.2%** of professionals), versus MySQL **40.5%** and SQL Server **30.1%**. PostgreSQL supports `FULL OUTER JOIN` natively; MySQL does not and needs a UNION workaround. ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
>
> **MySQL 8.0 end of life (30 Apr 2026).** Extended support ended on 30 April 2026, with MySQL 8.4 as the recommended LTS, so join queries and optimiser behaviour should be re-tested on upgrade. ([OpenLogic](https://www.openlogic.com/blog/mysql-8-end-of-life))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. INNER JOIN
> 🔴 Tier 1 · _Tracker hint:_ Returns rows with match in BOTH tables — most common join

### Definition
`INNER JOIN` (or just `JOIN`) returns only rows where the join condition is true in **both** tables; unmatched rows from either side are dropped.

```sql
SELECT o.order_id, c.name, o.amount
FROM   orders o
INNER JOIN customers c ON c.id = o.cust_id;
```
Row count: for a one-to-many join the result has one row per matching "many" row; for many-to-many it multiplies ($m \times n$ rows per key). NULL keys never match (NULL = NULL is UNKNOWN). Think of the Venn diagram as the **intersection**. Older comma syntax (`FROM a, b WHERE a.id = b.id`) is equivalent but error-prone because forgetting WHERE silently makes a cross join.

Use INNER JOIN when you only care about entities that exist on both sides (orders that have a valid customer). Be aware that an inner join can silently hide data problems, such as orders with missing customers.

### Example
`customers` ids {1, 2, 3}; `orders` has cust_id values {2, 2, 3, 4}. Inner join returns 3 rows: two for customer 2, one for customer 3. Customer 1 (no orders) and the order for cust_id 4 (no such customer) are dropped.

### In the news
See news box. INNER JOIN semantics are identical across MySQL, PostgreSQL and SQL Server, so the skill transfers whichever database leads the market.

### Interview angle
> [!question] How it is asked
> "What does an INNER JOIN return?" "Join orders and customers and show the customer name per order."

> [!tip] Strong answer includes
> - Matching rows only; intersection
> - One-to-many produces repeated left rows
> - NULL keys never match
> - Mentions explicit JOIN syntax over comma joins

---

## 2. LEFT JOIN (LEFT OUTER)
> 🔴 Tier 1 · _Tracker hint:_ All rows from left table + matching from right; NULLs where no match

### Definition
`LEFT JOIN` keeps **every row of the left table**; right-table columns are NULL when there is no match.

```sql
-- customers with their orders, including customers who never ordered
SELECT c.id, c.name, o.order_id
FROM   customers c
LEFT JOIN orders o ON o.cust_id = c.id;

-- anti-join: customers with NO orders
SELECT c.id, c.name
FROM   customers c
LEFT JOIN orders o ON o.cust_id = c.id
WHERE  o.order_id IS NULL;
```
**Critical rule:** a filter on the right table placed in `WHERE` (e.g. `WHERE o.status = 'SHIPPED'`) removes the NULL rows and turns the join into an inner join. Put right-table filters in the `ON` clause to preserve unmatched left rows. For counts use `COUNT(o.order_id)`, not `COUNT(*)`, so customers with zero orders count 0 rather than 1.

### Example
customers {1, 2, 3}; orders for customers 2 (two orders) and 3 (one). LEFT JOIN returns 4 rows: (1, NULL), (2, o1), (2, o2), (3, o3). Customer 1 is kept with NULLs, which the anti-join pattern isolates: it returns customer 1 only.

### In the news
See news box. A migration test for MySQL 8.0 to 8.4 should compare LEFT JOIN row counts, since a changed filter placement alters results silently.

### Interview angle
> [!question] How it is asked
> "Find customers who have never placed an order." "Why did my LEFT JOIN behave like an INNER JOIN?"

> [!tip] Strong answer includes
> - All left rows kept, NULLs on the right
> - Anti-join using IS NULL on a right-side key
> - ON vs WHERE for right-table filters
> - COUNT(right_col) rather than COUNT(*)

---

## 3. RIGHT JOIN
> 🔴 Tier 1 · _Tracker hint:_ All rows from right table + matching from left; less common, use LEFT instead

### Definition
`RIGHT JOIN` keeps every row of the **right** table and fills left columns with NULL where no match exists. It is the mirror image of LEFT JOIN: `A RIGHT JOIN B` equals `B LEFT JOIN A`.

```sql
SELECT c.name, o.order_id
FROM   customers c
RIGHT JOIN orders o ON o.cust_id = c.id;   -- all orders, even with unknown customer
```
Most teams standardise on LEFT JOIN because reading a query "from the main table outward" is easier and mixing LEFT and RIGHT in one query is confusing. Just swap table order. Right joins are mainly useful to find **orphan records** (orders whose customer is missing: `WHERE c.id IS NULL`), which usually signals a referential-integrity problem.

### Example
customers {1, 2, 3}; orders cust_id {2, 2, 3, 4}. `customers RIGHT JOIN orders` returns 4 rows: two for customer 2, one for 3, and (NULL, order for 4). The NULL-customer row exposes an orphan order.

### In the news
See news box. Both PostgreSQL and MySQL support RIGHT JOIN, so the rewrite to LEFT JOIN is a style choice, not a portability fix.

### Interview angle
> [!question] How it is asked
> "What is the difference between LEFT and RIGHT JOIN?" "Rewrite this RIGHT JOIN as a LEFT JOIN."

> [!tip] Strong answer includes
> - Mirror relationship with LEFT JOIN
> - Practical convention: use LEFT, reorder tables
> - Orphan-record detection use
> - Same ON/WHERE caveats as LEFT JOIN

---

## 4. FULL OUTER JOIN
> 🔴 Tier 1 · _Tracker hint:_ All rows from both tables; NULLs where no match on either side

### Definition
`FULL OUTER JOIN` returns all rows from both tables: matches combined, plus unmatched left rows (right NULL) and unmatched right rows (left NULL).

```sql
-- PostgreSQL, SQL Server, Oracle
SELECT a.id AS a_id, b.id AS b_id
FROM   a FULL OUTER JOIN b ON a.id = b.id;

-- MySQL (no FULL OUTER JOIN): UNION of LEFT and RIGHT
SELECT a.id AS a_id, b.id AS b_id FROM a LEFT  JOIN b ON a.id = b.id
UNION
SELECT a.id AS a_id, b.id AS b_id FROM a RIGHT JOIN b ON a.id = b.id;
```
Main use: **reconciliation**: compare two sources (system A vs system B) and see what is only in A, only in B or in both. Rows with a NULL on one side are exceptions. Row count: matches + unmatched left + unmatched right. `UNION` removes duplicate rows, so use `UNION ALL` plus an anti-join on the second query if true duplicates matter.

### Example
A = {1, 2, 3}, B = {2, 3, 4}. FULL OUTER JOIN gives (1, NULL), (2, 2), (3, 3), (NULL, 4): **4 rows**. Inner join would give 2, left join 3, right join 3.

### In the news
See news box. This is a concrete dialect gap: PostgreSQL (the leading database in 2025) supports FULL OUTER JOIN while MySQL needs the UNION emulation.

### Interview angle
> [!question] How it is asked
> "Reconcile inventory in the WMS and ERP: show items missing in either system." "Does MySQL support FULL JOIN?"

> [!tip] Strong answer includes
> - All rows from both sides, NULLs for gaps
> - MySQL workaround with LEFT UNION RIGHT
> - Reconciliation use case with a status column (CASE WHEN a.id IS NULL THEN 'only in B' ...)
> - Handles duplicates (UNION vs UNION ALL)

---

## 5. CROSS JOIN
> 🔴 Tier 1 · _Tracker hint:_ Cartesian product — every row × every row; use with care (n×m rows)

### Definition
`CROSS JOIN` pairs **every** row of one table with every row of the other, with no join condition. Result size = $n \times m$.

```sql
SELECT s.store_id, p.sku
FROM   stores s
CROSS JOIN products p;       -- every store-product combination
```
Legitimate uses: generate **all combinations** (store x SKU x month) to build a complete grid, then LEFT JOIN actual sales so missing combinations show as zero; build calendar or number tables; scenario analysis. Dangerous when accidental: an INNER JOIN with a missing or wrong ON clause (or a forgotten WHERE in a comma join) explodes row counts: 1 million x 1 million = $10^{12}$ rows. In MySQL, `JOIN` without `ON` behaves as a cross join.

### Example
50 stores and 200 SKUs: `CROSS JOIN` creates 50 x 200 = **10,000** store-SKU rows. LEFT JOIN weekly sales onto this grid and `COALESCE(qty, 0)` to find SKUs with zero sales in a store (candidate for delisting or a stock-out check).

### In the news
See news box. Large accidental Cartesian products are the classic way a join-heavy query exhausts memory, which faster I/O alone does not fix.

### Interview angle
> [!question] How it is asked
> "What is a Cartesian product and when is it useful?" "Create a report showing zero for missing store-month combinations."

> [!tip] Strong answer includes
> - n x m rows definition
> - Grid-building use plus LEFT JOIN to fill gaps
> - Danger of missing ON conditions
> - Sanity-check row counts after joins

---

## 6. SELF JOIN
> 🔴 Tier 1 · _Tracker hint:_ Table joined to itself; useful for org hierarchy, comparing rows in same table

### Definition
A **self join** joins a table to itself using two different aliases; it is not a special keyword, just a normal join where both sides are the same table.

```sql
-- employee and manager
SELECT e.name AS employee, m.name AS manager
FROM   emp e
LEFT JOIN emp m ON e.manager_id = m.id;     -- LEFT keeps the CEO (no manager)

-- pairs of products in the same category, each pair once
SELECT a.sku, b.sku
FROM   products a
JOIN   products b ON a.category = b.category AND a.sku < b.sku;
```
Uses: hierarchies (one level; deeper levels need a recursive CTE, see [[058 Window Functions]]), comparing a row to another row (previous day's price, duplicates), finding pairs. The `a.sku < b.sku` trick removes mirrored duplicates and self-pairs. For "compare with previous row", `LAG()` is usually cleaner and faster.

### Example
emp: (1, Asha, manager NULL), (2, Ravi, 1), (3, Meera, 1). The self join gives (Asha, NULL), (Ravi, Asha), (Meera, Asha). Using INNER JOIN would drop Asha.

### In the news
See news box. Hierarchical queries on org or BOM data are a typical reason to move beyond plain self joins to recursive CTEs, supported by both MySQL 8+ and PostgreSQL.

### Interview angle
> [!question] How it is asked
> "List each employee with their manager's name." "Find employees earning more than their manager."

> [!tip] Strong answer includes
> - Two aliases of the same table
> - LEFT JOIN to keep the top of the hierarchy
> - Salary comparison: `e.salary > m.salary`
> - When to use recursive CTE or window functions instead

---

## 7. Multi-table JOIN
> 🔴 Tier 1 · _Tracker hint:_ JOIN 3+ tables; order matters for performance; alias every table

### Definition
Chain joins left to right; each ON clause links the new table to something already joined.

```sql
SELECT o.order_id, c.name, p.product_name, s.supplier_name
FROM   orders o
JOIN   customers c   ON c.id = o.cust_id
JOIN   order_items i ON i.order_id = o.order_id
JOIN   products p    ON p.id = i.product_id
JOIN   suppliers s   ON s.id = p.supplier_id;
```
Logical join order is left to right, but for **inner joins** the optimiser freely reorders them using statistics, so written order rarely matters; it matters for outer joins (LEFT JOIN is not associative with inner joins) and when hints are used. Good practice: alias every table, qualify every column, join on indexed keys, filter early, select only needed columns, and mind **fan-out** when mixing one-to-many joins (sums inflate; see [[055 Aggregations & GROUP BY]]).

### Example
Orders: 1,000. Each has 3 items on average, so after joining `order_items` there are 3,000 rows. Joining `products` (many-to-one) keeps 3,000 rows. Summing `o.amount` now counts each order three times, so total = 3 x true revenue unless aggregated first.

### In the news
See news box. Five-table joins on tens of millions of rows are where PostgreSQL 18's I/O improvements and good indexes show up in run time.

### Interview angle
> [!question] How it is asked
> "Write a query joining orders, products and suppliers." "Why did my totals multiply after adding a join?"

> [!tip] Strong answer includes
> - Clean chaining with aliases
> - Index on join keys
> - Fan-out awareness and pre-aggregation
> - Mixing inner and outer joins carefully (order and WHERE effects)

---

## 8. JOIN on Multiple Conditions
> 🔴 Tier 1 · _Tracker hint:_ ON t1.id = t2.id AND t1.date = t2.date — compound join condition

### Definition
The ON clause can combine several predicates with AND (and OR). It is needed when the **natural key is composite** or when you must restrict the match.

```sql
-- composite key
SELECT s.sku, s.wh_id, s.qty, p.price
FROM   stock s
JOIN   price_list p ON p.sku = s.sku AND p.region = s.region;

-- date-effective match
JOIN fx f ON f.currency = o.currency AND f.rate_date = o.order_date
```
Rules: omitting one part of a composite key creates duplicate matches (fan-out). With **outer joins**, extra conditions on the optional table belong in ON (not WHERE). `OR` conditions in ON often kill index use and slow down joins; rewrite as two joins or a UNION. Compare data types of both sides (VARCHAR vs INT) to avoid implicit conversion.

### Example
`stock` has SKU A in warehouses W1 and W2. `price_list` has SKU A priced per region: North and South. Joining on `sku` alone yields 2 x 2 = 4 rows; joining on `sku AND region` yields 2 correct rows. The missing second condition doubles the stock.

### In the news
See news box. Composite-key joins benefit from composite indexes, and PostgreSQL 18 skip-scan can make an index on (sku, region) usable even when only region is supplied.

### Interview angle
> [!question] How it is asked
> "Join two tables on a composite key." "Join orders to the exchange rate for that day."

> [!tip] Strong answer includes
> - AND of key parts in ON
> - Notices duplication when a key part is missing
> - ON vs WHERE for outer joins
> - Avoids OR in ON, and ensures matching data types

---

## 9. Non-equi JOIN
> 🔴 Tier 1 · _Tracker hint:_ ON t1.salary BETWEEN t2.low AND t2.high — range-based joins

### Definition
A **non-equi join** uses an operator other than `=` in ON: `<`, `>`, `<=`, `>=`, `BETWEEN`, `<>`. It matches rows by **range or inequality**.

```sql
-- salary grade lookup
SELECT e.name, e.salary, g.grade
FROM   emp e
JOIN   salary_grade g ON e.salary BETWEEN g.low AND g.high;

-- price valid on order date (slowly changing price table)
JOIN price_hist p ON p.sku = o.sku
                 AND o.order_date >= p.valid_from AND o.order_date < p.valid_to
```
Typical uses: banding (age, salary, discount slabs), effective-dated lookups, matching events to time windows, running totals via self join (`b.date <= a.date`). Non-equi joins cannot use hash joins, so they run as nested loops/range scans and can be slow; ensure the ranges do not overlap, or one row will match multiple bands.

### Example
Grades: A 0-39,999; B 40,000-79,999; C 80,000-1,50,000. Employee with salary 55,000 satisfies only B, so exactly one row. If bands overlapped (B starting at 39,000), 39,500 would match both and the employee would appear twice.

### In the news
See news box. Effective-dated price and rate joins are standard for finance reports and carry over unchanged between database engines.

### Interview angle
> [!question] How it is asked
> "Assign each employee a salary grade using a grade table." "Join a transaction to the price valid on that date."

> [!tip] Strong answer includes
> - Range condition in ON
> - Half-open date intervals to avoid boundary double matches
> - Overlap risk
> - Performance caveat versus equi-joins

---

## 10. SCM JOIN Example
> 🔴 Tier 1 · _Tracker hint:_ orders JOIN products ON orders.prod_id = products.id JOIN suppliers ON products.sup_id = suppliers.id

### Definition
Supply-chain questions usually span fact tables (orders, receipts, inventory) and dimensions (products, suppliers, warehouses). Join facts to dimensions on keys, then aggregate.

```sql
-- Spend and open quantity by supplier
SELECT s.supplier_name,
       COUNT(DISTINCT o.order_id)        AS n_orders,
       SUM(o.qty * p.unit_cost)          AS spend
FROM   orders o
JOIN   products  p ON o.prod_id = p.id
JOIN   suppliers s ON p.sup_id  = s.id
WHERE  o.order_date >= '2026-04-01'
GROUP  BY s.supplier_name
ORDER  BY spend DESC;

-- Products with no orders in the last 90 days (dead stock candidates)
SELECT p.sku
FROM   products p
LEFT JOIN orders o ON o.prod_id = p.id AND o.order_date >= CURRENT_DATE - INTERVAL 90 DAY
WHERE  o.order_id IS NULL;
```
Note the ON-clause date filter preserving unmatched products, and `INTERVAL 90 DAY` (MySQL; PostgreSQL uses `INTERVAL '90 days'`).

### Example
Supplier S1 supplies products P1 (cost 50) and P2 (cost 20). Orders: P1 x 100, P2 x 200. Spend = 100 x 50 + 200 x 20 = 5,000 + 4,000 = **9,000** for S1. A product with no orders appears only in the LEFT JOIN anti-join list.

### In the news
See news box. Large ERP extracts (orders, products, suppliers) are exactly the multi-table joins where indexes on foreign keys and fast scans decide whether a report takes seconds or minutes.

### Interview angle
> [!question] How it is asked
> "Which suppliers account for 80% of spend?" "List products with no sales in 90 days."

> [!tip] Strong answer includes
> - Fact-to-dimension join pattern with correct keys
> - Pre-filtering by date and selecting needed columns only
> - Anti-join with LEFT JOIN for dead stock
> - Business reading: spend concentration and supplier risk (Pareto)

---

## 11. ⭐ Advanced: Semi-joins, Anti-joins and the ON vs WHERE Trap
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Semi-join:** return rows from A that **have** a match in B, without duplicating A for multiple matches. Write as `WHERE EXISTS (SELECT 1 FROM b WHERE b.a_id = a.id)` or `IN (subquery)`.
- **Anti-join:** rows in A with **no** match in B: `NOT EXISTS`, or `LEFT JOIN ... WHERE b.id IS NULL`. Prefer these over `NOT IN` because of the NULL trap ([[057 Subqueries & CTEs]]).

```sql
-- customers with at least one order (no duplicates, unlike a plain join)
SELECT c.* FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.cust_id = c.id);
```
**ON vs WHERE in outer joins:** ON decides *how rows are matched*; WHERE filters the *result afterwards*. For `A LEFT JOIN B ON ... WHERE B.col = x`, unmatched rows (B.col NULL) are removed: it is effectively an inner join. To keep all A rows but only match B rows with `col = x`, write `LEFT JOIN B ON ... AND B.col = x`.

### Example
customers {1, 2}; orders: customer 1 has two orders, customer 2 has none. `JOIN` returns customer 1 twice. `WHERE EXISTS` returns customer 1 **once**. `NOT EXISTS` returns customer 2. With a LEFT JOIN and `WHERE o.status='NEW'`, customer 2 vanishes; with the condition in ON, customer 2 stays with NULLs.

### In the news
See news box. Query optimisers in PostgreSQL and MySQL 8.4 both turn EXISTS and IN into semi-joins internally, so the choice is about clarity and NULL safety.

### Interview angle
> [!question] How it is asked
> "Customers who ordered at least once, without duplicates." "Why did my LEFT JOIN lose rows after I added a WHERE?"

> [!tip] Strong answer includes
> - Semi- vs anti-join definitions and the EXISTS patterns
> - ON versus WHERE explanation for outer joins
> - NOT EXISTS over NOT IN
> - Verifies with row counts

---

## 12. ⭐ Advanced: Join Algorithms and Performance
> ⭐ Advanced · _Added beyond the tracker_

### Definition
The optimiser picks a physical join algorithm:

| Algorithm | How it works | Best when |
|---|---|---|
| Nested loop | For each outer row, probe the inner table (via index) | Small outer set, indexed inner key |
| Hash join | Build an in-memory hash table on the smaller input, probe with the larger | Large unsorted inputs, equi-joins, no useful index |
| Merge (sort-merge) join | Sort both inputs on the key and merge | Inputs already sorted or indexed on the key |

PostgreSQL implements all three; MySQL used only nested loop until it added hash joins in 8.0.18. Performance checklist: index foreign keys, join on same data types, filter before joining, avoid `SELECT *`, avoid functions on join columns, keep statistics fresh (`ANALYZE`), and read `EXPLAIN` for the join type and estimated vs actual rows.

### Example
Joining 1 million orders to 10,000 customers: a hash join builds a hash table of 10,000 customers (small) and streams 1 million orders through it: about 1,010,000 operations. A naive nested loop without an index on `customers.id` would do up to 1,000,000 x 10,000 = $10^{10}$ comparisons.

### In the news
See news box. MySQL 8.4 and PostgreSQL 18 both rely on hash joins for large equi-joins, and PostgreSQL 18's async I/O reduces time spent waiting on disk during the scans feeding them.

### Interview angle
> [!question] How it is asked
> "A join query is slow. How do you diagnose it?"

> [!tip] Strong answer includes
> - EXPLAIN to see algorithm and row estimates
> - Index on join keys, matching data types
> - Name nested loop, hash, merge with when each wins
> - Reduce rows before the join, fresh statistics

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
