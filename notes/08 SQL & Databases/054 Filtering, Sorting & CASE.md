---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "Filtering, Sorting & CASE"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Filtering, Sorting & CASE

⬅ [[053 SQL Foundations & Data Types]] · [[_Index - SQL & Databases|SQL & Databases]] · [[055 Aggregations & GROUP BY]] ➡

> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. WHERE Clause]]
2. [[#2. IN / NOT IN]]
3. [[#3. BETWEEN]]
4. [[#4. LIKE & Pattern Matching]]
5. [[#5. CASE WHEN]]
6. [[#6. ORDER BY]]
7. [[#7. LIMIT / TOP / FETCH]]
8. [[#8. DISTINCT]]
9. [[#9. WHERE vs HAVING]]
10. [[#10. Wildcards & REGEXP]]
11. [[#11. ⭐ Advanced: Sargable Predicates & Date Filtering]]
12. [[#12. ⭐ Advanced: Pivoting with CASE and NULL-safe Comparisons]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Dialect differences matter because the database market is shifting
> **PostgreSQL leads the 2025 Stack Overflow Developer Survey.** Used by **55.6%** of all respondents (**58.2%** of professionals), ahead of MySQL (**40.5%**), SQLite (**37.5%**) and SQL Server (**30.1%**); it is the most-used and most-desired database for the third year running. ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
>
> **MySQL 8.0 end of life (30 Apr 2026).** Extended support ended on 30 April 2026 and MySQL 8.4 LTS is the recommended path, so queries written for older MySQL need a re-check on 8.4. ([OpenLogic](https://www.openlogic.com/blog/mysql-8-end-of-life))
>
> **PostgreSQL 18 (25 Sep 2025).** Adds asynchronous I/O (up to about 3x gains in some benchmarks) and skip-scan on multicolumn B-tree indexes, which can make filter-heavy queries faster without rewriting them. ([LWN](https://lwn.net/Articles/1039483/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. WHERE Clause
> 🔴 Tier 1 · _Tracker hint:_ =, !=, >, <, >=, <=; and, or, not; operator precedence

### Definition
**WHERE** filters rows *before* grouping. Comparison operators: `=`, `<>` or `!=`, `>`, `<`, `>=`, `<=`. Combine with `AND`, `OR`, `NOT`.

**Precedence:** comparison operators first, then `NOT`, then `AND`, then `OR`. So `a OR b AND c` means `a OR (b AND c)`. Always add parentheses to make intent explicit.

```sql
SELECT * FROM orders
WHERE status = 'SHIPPED'
  AND (region = 'South' OR region = 'West')
  AND NOT amount < 500;
```
A row passes only if the condition evaluates to TRUE; rows where it is FALSE or UNKNOWN (NULL involved) are dropped. Compare dates as `'2026-10-01'` literals and use half-open ranges (`>= start AND < next_start`) for datetimes.

### Example
`WHERE region='South' OR region='West' AND amount>1000` returns **all South rows of any amount** plus West rows above 1000, because AND binds first. The intended filter "South or West, and above 1000" needs `(region='South' OR region='West') AND amount>1000`.

### In the news
See news box. A query that ran correctly on MySQL 8.0 should still be regression-tested on 8.4 and on PostgreSQL if you migrate, since implicit type conversions in comparisons can differ.

### Interview angle
> [!question] How it is asked
> "What does this query return?" with a mixed AND/OR WHERE, or "Why did my filter return too many rows?"

> [!tip] Strong answer includes
> - NOT > AND > OR precedence
> - Use of parentheses
> - NULL rows dropped by comparisons
> - Sargable filters (no function wrapped around the column) for index use

---

## 2. IN / NOT IN
> 🔴 Tier 1 · _Tracker hint:_ WHERE city IN ('Mumbai','Delhi','Bangalore'); vs subquery with IN

### Definition
`col IN (v1, v2, v3)` is shorthand for `col = v1 OR col = v2 OR col = v3`. `NOT IN` is the negation. The list can also come from a **subquery**.

```sql
SELECT * FROM customers WHERE city IN ('Mumbai','Delhi','Bangalore');

SELECT * FROM orders
WHERE  cust_id IN (SELECT id FROM customers WHERE tier = 'Gold');
```
**NULL trap:** if the list or subquery contains a NULL, `x NOT IN (...)` yields UNKNOWN for every row and returns **nothing**. Use `NOT EXISTS` or filter `WHERE col IS NOT NULL` inside the subquery (see [[057 Subqueries & CTEs]]). `IN (subquery)` is fine with NULLs for positive matches. Huge literal lists are better replaced by a join to a lookup table.

### Example
Supplier ids in `blocked_suppliers` = {7, 9, NULL}. `SELECT * FROM suppliers WHERE id NOT IN (SELECT sup_id FROM blocked_suppliers);` returns **0 rows** even though 100 suppliers are not blocked, because `id <> NULL` is UNKNOWN. Adding `WHERE sup_id IS NOT NULL` inside the subquery fixes it.

### In the news
See news box. PostgreSQL's optimiser handles `IN`/`EXISTS` semi-joins well; the NULL semantics are identical across the major dialects.

### Interview angle
> [!question] How it is asked
> "Why does NOT IN return no rows?" or "IN vs EXISTS vs JOIN?"

> [!tip] Strong answer includes
> - IN as a compact OR list
> - The NOT IN with NULL pitfall and two fixes
> - IN (subquery) versus a join for large data
> - Mention that duplicates in the subquery do not duplicate output rows (unlike a join)

---

## 3. BETWEEN
> 🔴 Tier 1 · _Tracker hint:_ WHERE amount BETWEEN 1000 AND 5000; inclusive on both ends

### Definition
`x BETWEEN a AND b` is equivalent to `x >= a AND x <= b`: **both ends inclusive**. Works for numbers, dates and strings. Put the smaller value first, since `BETWEEN 5000 AND 1000` returns nothing. `NOT BETWEEN` excludes the range.

**Date trap:** for DATETIME columns `BETWEEN '2026-10-01' AND '2026-10-31'` treats the end as `2026-10-31 00:00:00`, silently dropping orders placed later on 31 October. Prefer:
```sql
WHERE order_ts >= '2026-10-01' AND order_ts < '2026-11-01'
```
String ranges use collation order: `BETWEEN 'A' AND 'C'` includes 'C' exactly but not 'Cat'.

### Example
Amounts: 999, 1000, 3000, 5000, 5001. `BETWEEN 1000 AND 5000` returns 1000, 3000, 5000 (three rows). 999 and 5001 are excluded.

### In the news
See news box. Date-range correctness is behaviour that does not change across dialects, so it is a safe skill to carry from MySQL to PostgreSQL.

### Interview angle
> [!question] How it is asked
> "Is BETWEEN inclusive?" and "How do you filter all of last month's orders correctly?"

> [!tip] Strong answer includes
> - Inclusive on both ends
> - The DATETIME end-of-day trap and the half-open range fix
> - Lower bound first
> - Use of date functions only when index use is not needed, otherwise range predicates

---

## 4. LIKE & Pattern Matching
> 🔴 Tier 1 · _Tracker hint:_ LIKE 'A%' (starts with A), '%co%' (contains), '_a%' (second char a)

### Definition
`LIKE` matches text with two wildcards: `%` (any number of characters, including zero) and `_` (exactly one character).

| Pattern | Meaning |
|---|---|
| `'A%'` | starts with A |
| `'%son'` | ends with son |
| `'%co%'` | contains co |
| `'_a%'` | second character is a |
| `'____'` | exactly four characters |

Case sensitivity depends on collation: MySQL's default is case-insensitive; PostgreSQL's `LIKE` is case-sensitive (use `ILIKE`). Escape literal wildcards with `ESCAPE '\'`, for example `LIKE '50\%' `. Performance: `LIKE 'abc%'` can use an index; `LIKE '%abc'` cannot (leading wildcard forces a scan), so use full-text search or trigram indexes for contains-searches on big tables.

### Example
Customer names: Amit, Ramesh, Sarita, Kamal, Anu. `LIKE '_a%'` matches Ramesh, Sarita, Kamal (second letter a), not Amit or Anu. `LIKE 'A%'` matches Amit and Anu.

### In the news
See news box. PostgreSQL's strong text-search and trigram options are one reason it is chosen for search-heavy apps.

### Interview angle
> [!question] How it is asked
> "Find all customers whose names start with A and end with n." or "Why is my LIKE '%x%' slow?"

> [!tip] Strong answer includes
> - % versus _ with examples
> - Case sensitivity by dialect (ILIKE)
> - Leading wildcard prevents index use
> - Alternatives: full-text index, REGEXP

---

## 5. CASE WHEN
> 🔴 Tier 1 · _Tracker hint:_ CASE WHEN score>=90 THEN 'A' WHEN score>=75 THEN 'B' ELSE 'C' END AS grade

### Definition
**CASE** is SQL's if-then-else expression. Conditions are evaluated top to bottom and the **first TRUE** branch wins; without ELSE, unmatched rows return NULL.

```sql
SELECT student, score,
       CASE WHEN score >= 90 THEN 'A'
            WHEN score >= 75 THEN 'B'
            ELSE 'C' END AS grade
FROM results;

-- simple form: compare one expression to values
CASE status WHEN 'D' THEN 'Delivered' WHEN 'S' THEN 'Shipped' ELSE 'Other' END
```
CASE works in SELECT, WHERE, ORDER BY, GROUP BY and inside aggregates (**conditional aggregation**, see [[055 Aggregations & GROUP BY]]). Order of branches matters: put the most restrictive condition first. All branches must return compatible types.

### Example
ABC tagging of SKUs by annual revenue: `CASE WHEN rev >= 1000000 THEN 'A' WHEN rev >= 200000 THEN 'B' ELSE 'C' END`. A SKU with revenue 500,000 fails the first test, passes the second, and is tagged B. If the branches were reversed, every SKU of 200,000 or more would be tagged B and no A would exist.

### In the news
See news box. Standard CASE syntax is identical across MySQL, PostgreSQL and SQL Server, so it is portable analytic logic.

### Interview angle
> [!question] How it is asked
> "Categorise customers into High/Medium/Low spend." or "Pivot rows to columns without PIVOT."

> [!tip] Strong answer includes
> - First-match-wins and branch ordering
> - ELSE to avoid unintended NULLs
> - Use inside SUM/COUNT for pivoting
> - Searched versus simple CASE

---

## 6. ORDER BY
> 🔴 Tier 1 · _Tracker hint:_ ORDER BY col1 ASC, col2 DESC; NULL ordering (NULLS LAST)

### Definition
`ORDER BY` sorts the result; without it, row order is **not guaranteed**. Default is `ASC`. You can sort by several columns, by alias, by expression or by column position (`ORDER BY 2`, discouraged).

```sql
SELECT dept, name, salary FROM emp
ORDER BY dept ASC, salary DESC;

-- NULL placement
ORDER BY bonus DESC NULLS LAST;           -- PostgreSQL, Oracle, SQLite 3.30+
ORDER BY (bonus IS NULL), bonus DESC;      -- MySQL / SQL Server workaround
```
Default NULL position differs: MySQL and SQL Server treat NULL as the lowest value (first in ASC); PostgreSQL treats NULL as the highest (last in ASC). ORDER BY is the last logical step before LIMIT, so it can use SELECT aliases. Add a tie-breaker column (e.g. a unique id) for deterministic pagination.

### Example
Salaries in dept A: 90k, 90k, NULL, 70k. `ORDER BY salary DESC` in PostgreSQL gives NULL, 90k, 90k, 70k (NULL treated as highest) but in MySQL gives 90k, 90k, 70k, NULL. Adding `NULLS LAST` (or the IS NULL trick) makes both consistent.

### In the news
See news box. Moving from MySQL to the market-leading PostgreSQL changes default NULL ordering, a classic silent behaviour difference.

### Interview angle
> [!question] How it is asked
> "How do you sort by department then by salary descending?" "Where do NULLs appear?"

> [!tip] Strong answer includes
> - Multi-column sorting with mixed directions
> - NULL ordering differences and NULLS LAST
> - Sorting is only guaranteed with ORDER BY
> - Tie-breaker for stable top-N and pagination

---

## 7. LIMIT / TOP / FETCH
> 🔴 Tier 1 · _Tracker hint:_ MySQL: LIMIT n OFFSET m; SQL Server: TOP n; Standard: FETCH FIRST n ROWS

### Definition
Three syntaxes for "first n rows":

```sql
-- MySQL, PostgreSQL, SQLite
SELECT * FROM orders ORDER BY amount DESC LIMIT 10 OFFSET 20;

-- SQL Server
SELECT TOP 10 * FROM orders ORDER BY amount DESC;
SELECT * FROM orders ORDER BY amount DESC
OFFSET 20 ROWS FETCH NEXT 10 ROWS ONLY;      -- SQL Server 2012+

-- ANSI standard (PostgreSQL, Oracle 12c+, Db2)
SELECT * FROM orders ORDER BY amount DESC
FETCH FIRST 10 ROWS ONLY;
```
Always pair with ORDER BY, else the "top n" is arbitrary. `OFFSET m` skips m rows, so page p of size s uses `OFFSET (p-1)*s`. Deep OFFSET is slow because skipped rows are still read; **keyset pagination** (`WHERE id > last_id ORDER BY id LIMIT s`) is faster. `FETCH FIRST ... WITH TIES` includes ties for the last place.

### Example
Page 3 with 25 rows per page: `LIMIT 25 OFFSET 50` (skip (3-1)*25 = 50). For "top 3 salaries including ties" use `FETCH FIRST 3 ROWS WITH TIES` or a window function ([[058 Window Functions]]).

### In the news
See news box. PostgreSQL's growing share means the standard `FETCH FIRST` form and `LIMIT` both deserve to be in your toolkit.

### Interview angle
> [!question] How it is asked
> "Write the top 5 customers by revenue in SQL Server and in MySQL." "How do you paginate?"

> [!tip] Strong answer includes
> - The three dialect forms
> - ORDER BY dependence
> - OFFSET formula and its performance problem; keyset alternative
> - Ties handling (WITH TIES, DENSE_RANK)

---

## 8. DISTINCT
> 🔴 Tier 1 · _Tracker hint:_ SELECT DISTINCT city FROM customers; removes duplicates

### Definition
`DISTINCT` removes duplicate **rows** from the result (compares the whole selected row, not one column). NULLs are treated as equal for this purpose, so one NULL row remains.

```sql
SELECT DISTINCT city FROM customers;
SELECT DISTINCT city, tier FROM customers;      -- unique (city, tier) pairs
SELECT COUNT(DISTINCT cust_id) FROM orders;     -- number of unique buyers
```
`DISTINCT` is **not** a function: `SELECT DISTINCT(a), b` still dedupes the pair (a, b). It requires a sort or hash step, so it is costly on big results; if you are using DISTINCT to hide duplicates caused by a bad join, fix the join instead. `UNION` removes duplicates, `UNION ALL` does not. PostgreSQL also has `DISTINCT ON (col)` to keep the first row per group.

### Example
`orders` has 1,000 rows from 240 unique customers. `COUNT(cust_id)` = 1,000 (rows), `COUNT(DISTINCT cust_id)` = 240 (customers). Average orders per customer = 1,000 / 240 = 4.17.

### In the news
See news box. Large-scale DISTINCT counts benefit from PostgreSQL 18's improved I/O, but approximate distinct counts are common in analytics warehouses.

### Interview angle
> [!question] How it is asked
> "How do you count unique customers?" "Does DISTINCT apply to one column?"

> [!tip] Strong answer includes
> - Applies to the whole row
> - COUNT(DISTINCT col) for unique counts
> - Warns against using it to paper over join duplication
> - UNION vs UNION ALL link

---

## 9. WHERE vs HAVING
> 🔴 Tier 1 · _Tracker hint:_ WHERE filters rows before GROUP BY; HAVING filters after aggregation

### Definition
| | WHERE | HAVING |
|---|---|---|
| Filters | Individual rows | Groups |
| Runs | Before GROUP BY | After GROUP BY |
| Can use aggregates | No | Yes |
| Can use SELECT alias | No (standard) | MySQL yes, PostgreSQL no |

```sql
SELECT dept, AVG(salary) AS avg_sal
FROM   emp
WHERE  status = 'ACTIVE'          -- row filter first (cheap, reduces work)
GROUP  BY dept
HAVING AVG(salary) > 50000;       -- group filter after
```
Put any condition that does not need an aggregate in WHERE: it discards rows before grouping and can use indexes. HAVING without GROUP BY treats the whole table as one group.

### Example
Employees: dept A has salaries 40k, 60k (avg 50k), dept B has 55k, 65k (avg 60k). `HAVING AVG(salary) > 50000` returns only B. If you also want to ignore salaries below 45k, that is a WHERE: `WHERE salary >= 45000` makes dept A just 60k (avg 60k), so now A also qualifies. The two filters answer different questions.

### In the news
See news box. This is one of the most portable SQL concepts across all dialects in the 2025 survey top five.

### Interview angle
> [!question] How it is asked
> "Difference between WHERE and HAVING?" (near-certain screening question)

> [!tip] Strong answer includes
> - Row versus group filter and execution order
> - Aggregates only in HAVING
> - Performance: filter early with WHERE
> - A one-query example using both

---

## 10. Wildcards & REGEXP
> 🔴 Tier 1 · _Tracker hint:_ REGEXP '^[A-Z]'; useful for string pattern filtering in analytics

### Definition
When `LIKE` is too limited, use **regular expressions**.

| Dialect | Syntax |
|---|---|
| MySQL | `col REGEXP '^[A-Z]'`, `REGEXP_LIKE(col, pattern)` (8.0+) |
| PostgreSQL | `col ~ '^[A-Z]'` (case-sensitive), `~*` (insensitive), `!~` (not match) |
| SQL Server | no native regex; use LIKE with `[A-Z]` ranges, or CLR |

Common tokens: `^` start, `$` end, `.` any char, `*` zero or more, `+` one or more, `[abc]` set, `[0-9]` range, `|` alternation, `{n}` repeat.

```sql
-- MySQL: valid 6-digit Indian PIN code (first digit 1-9)
SELECT * FROM customers WHERE pin REGEXP '^[1-9][0-9]{5}$';
-- Names starting with a vowel
SELECT * FROM customers WHERE name REGEXP '^[AEIOUaeiou]';
```
Regex cannot use ordinary B-tree indexes, so use it for cleaning and validation, not on hot paths.

### Example
Checking PIN codes: '411005' matches `^[1-9][0-9]{5}$`; '041005' fails (starts with 0); '41100' fails (only five digits). This quickly flags bad address data in a delivery database.

### In the news
See news box. Because regex syntax differs between MySQL and PostgreSQL, dialect awareness shows up in migration checklists.

### Interview angle
> [!question] How it is asked
> "How would you validate email or PIN formats in SQL?" or "Find names that start with a vowel."

> [!tip] Strong answer includes
> - LIKE for simple, REGEXP for complex patterns
> - Anchors ^ and $, character classes, quantifiers
> - Dialect operators (REGEXP, ~)
> - Performance caveat and use for data-quality checks

---

## 11. ⭐ Advanced: Sargable Predicates & Date Filtering
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A predicate is **sargable** (Search ARGument ABLE) if the engine can use an index to evaluate it. Wrapping the column in a function or arithmetic usually breaks this.

| Not sargable | Sargable rewrite |
|---|---|
| `WHERE YEAR(order_date) = 2026` | `WHERE order_date >= '2026-01-01' AND order_date < '2027-01-01'` |
| `WHERE amount * 1.18 > 1000` | `WHERE amount > 1000/1.18` |
| `WHERE name LIKE '%ram'` | full-text or trigram index |
| `WHERE UPPER(city) = 'PUNE'` | case-insensitive collation or functional index |
| `WHERE col + 0 = 5` | `WHERE col = 5` |

Also: implicit type conversion (comparing a VARCHAR column to a number) can disable the index; `OR` across different columns may prevent index use; `LEFT(col, 3) = 'ABC'` can be written `col LIKE 'ABC%'`.

### Example
Table of 50 million orders with an index on `order_date`. `WHERE YEAR(order_date)=2026` computes YEAR on all 50 million rows (full scan). The range form walks the index to the first 2026 row and stops at the first 2027 row, reading only the rows needed.

### In the news
See news box. PostgreSQL 18's skip scan widens the cases where a composite index helps, but function-wrapped columns remain non-sargable unless you create an expression index.

### Interview angle
> [!question] How it is asked
> "This query is slow although the column is indexed. Why?"

> [!tip] Strong answer includes
> - Defines sargable and gives the YEAR() example
> - Rewrites to range predicates
> - Mentions functional/expression indexes as the alternative
> - Verifies with EXPLAIN before and after

---

## 12. ⭐ Advanced: Pivoting with CASE and NULL-safe Comparisons
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Two interview favourites that combine this topic's tools.

**1. Pivot with CASE** (rows to columns, portable across dialects):
```sql
SELECT product,
       SUM(CASE WHEN month = 'Jan' THEN qty ELSE 0 END) AS jan,
       SUM(CASE WHEN month = 'Feb' THEN qty ELSE 0 END) AS feb
FROM   sales
GROUP  BY product;
```
**2. NULL-safe equality:** `a = b` is UNKNOWN when either is NULL. Use `a <=> b` (MySQL) or `a IS NOT DISTINCT FROM b` (standard, PostgreSQL) when you want two NULLs to count as equal, for example when comparing a staging table to a master table. For one-sided checks write `(a = b OR (a IS NULL AND b IS NULL))`.

Also useful: `COALESCE` inside filters (`WHERE COALESCE(status,'NEW') = 'NEW'`) to treat NULL as a default value, noting that wrapping the column may reduce index use.

### Example
Sales: (Pen, Jan, 10), (Pen, Feb, 5), (Pen, Jan, 4). The pivot returns one row: Pen, jan = 10 + 4 = 14, feb = 5. Without GROUP BY and SUM, CASE alone would return three rows with zeros filling the other month's column.

### In the news
See news box. Standard `IS NOT DISTINCT FROM` works on PostgreSQL, while MySQL uses its `<=>` operator, another place where the top two open-source databases differ.

### Interview angle
> [!question] How it is asked
> "Convert monthly rows into columns without PIVOT." "Compare two tables where some values are NULL."

> [!tip] Strong answer includes
> - SUM(CASE...) with GROUP BY pivot pattern
> - Awareness that PIVOT keyword is SQL Server/Oracle only
> - NULL-safe comparison operators by dialect
> - Check the result row counts against the source totals

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
