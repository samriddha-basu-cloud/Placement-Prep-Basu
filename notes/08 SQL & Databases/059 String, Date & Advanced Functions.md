---
tags: [sql-databases, tier2]
area: SQL & Databases
topic: "String, Date & Advanced Functions"
tier: Tier 2
roles: All Roles
status: complete
subtopics: 11
---
# String, Date & Advanced Functions

⬅ [[058 Window Functions]] · [[_Index - SQL & Databases|SQL & Databases]] · [[060 Query Optimization & Indexing]] ➡

> **Area:** SQL & Databases · **Priority:** 🟠 Tier 2 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. String Functions]]
2. [[#2. Date Functions]]
3. [[#3. EXTRACT / DATE_PART]]
4. [[#4. Type Casting]]
5. [[#5. Math Functions]]
6. [[#6. COALESCE vs IFNULL vs NVL]]
7. [[#7. String Splitting]]
8. [[#8. Pivoting with CASE]]
9. [[#9. JSON Functions (MySQL 8+)]]
10. [[#10. Regular Expressions]]
11. [[#11. ⭐ Advanced: Window-friendly Date Bucketing (DATE_TRUNC, week and fiscal periods)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the SQL dialect you learnt is moving under your feet
> **MySQL 8.0 reaches end of life (April 2026).** The official MySQL 8.0 release notes state: "As of April 2026, with version 8.0.46, MySQL 8.0 reaches End of Life (EoL). MySQL 8.0 users are encouraged to upgrade to the latest MySQL 8.4 LTS or MySQL Innovation release." Many Indian analytics teams still run 8.0, so JSON, regex and window functions (all 8.0 features) now sit on a version that no longer gets fixes. ([MySQL release notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/))
>
> **PostgreSQL 18 released (25 Sep 2025).** Adds a `casefold()` text function and a `PG_UNICODE_FAST` collation for better text processing, virtual generated columns (computed at query time), `uuidv7()` and `OLD`/`NEW` values in `RETURNING`. ([PostgreSQL announcement](https://www.postgresql.org/about/news/postgresql-18-released-3142/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. String Functions
> 🟠 Tier 2 · _Tracker hint:_ UPPER, LOWER, LENGTH, SUBSTRING(str,start,len), TRIM, REPLACE, CONCAT, INSTR

### Definition
String functions clean and reshape text columns, which is the first step in almost every real analytics job (SKU codes, vendor names, addresses are messy). MySQL syntax (positions are **1-based**):

```sql
SELECT UPPER('nashik')               AS u,   -- 'NASHIK'
       LOWER('SIOM')                 AS l,   -- 'siom'
       LENGTH('SKU-001')             AS len, -- 7 (bytes in MySQL; CHAR_LENGTH counts characters)
       SUBSTRING('SKU-001', 5, 3)    AS part,-- '001'
       TRIM('  vendor  ')            AS t,   -- 'vendor'
       REPLACE('A-B-C','-','/')      AS r,   -- 'A/B/C'
       CONCAT('PO-', 2024, '-', 17)  AS po,  -- 'PO-2024-17'
       INSTR('SKU-001','-')          AS pos; -- 4 (0 if not found)
```

Notes: `CONCAT` returns NULL if any argument is NULL; use `CONCAT_WS(sep, a, b, ...)` which skips NULLs. `||` is concatenation in PostgreSQL/Oracle but a logical OR in default MySQL. `LEFT(s,n)`, `RIGHT(s,n)`, `LPAD(s,n,pad)` are also common. Functions on a column in `WHERE` can block index use (see [[060 Query Optimization & Indexing]]).

### Example
Standardise vendor names so that ' tata steel ' and 'TATA STEEL' group together:
```sql
SELECT UPPER(TRIM(vendor_name)) AS vendor, SUM(po_value) AS spend
FROM purchase_orders
GROUP BY UPPER(TRIM(vendor_name));
```
`SUBSTRING('SKU-001', 5, 3)`: start at character 5, take 3 characters, giving '001'.

### In the news
See news box. PostgreSQL 18 adds `casefold()` for case-insensitive comparison, the modern alternative to wrapping both sides in `LOWER()`.

### Interview angle
> [!question] How it is asked
> "You have a vendor table with inconsistent names. How would you clean it before computing spend per vendor?" or "What is the difference between LENGTH and CHAR_LENGTH?"

> [!tip] Strong answer includes
> - TRIM plus UPPER/LOWER normalisation before GROUP BY or JOIN
> - Knowing 1-based positions and the NULL behaviour of CONCAT vs CONCAT_WS
> - Mention of dialect differences (`||`, `SUBSTR`, `LEN` in SQL Server)
> - Warning that functions on indexed columns hurt performance, so clean data once at load time

---

## 2. Date Functions
> 🟠 Tier 2 · _Tracker hint:_ NOW(), CURDATE(), DATE_ADD(date, INTERVAL 7 DAY), DATEDIFF(d1,d2), DATE_FORMAT(date,'%Y-%m')

### Definition
Date functions drive lead-time, ageing, SLA and trend analysis. MySQL:

```sql
SELECT NOW(),                                   -- current date and time
       CURDATE(),                               -- current date
       DATE_ADD('2025-01-25', INTERVAL 7 DAY),  -- 2025-02-01
       DATE_SUB('2025-03-01', INTERVAL 1 MONTH),-- 2025-02-01
       DATEDIFF('2025-03-01','2025-02-01'),     -- 28  (d1 - d2, in days)
       DATE_FORMAT('2025-03-09','%Y-%m');       -- '2025-03'
```

Key points: `DATEDIFF(d1, d2)` = d1 minus d2 (sign matters, argument order is a classic mistake). `TIMESTAMPDIFF(unit, start, end)` gives differences in months, hours etc. (start first!). `DATE_FORMAT` codes: `%Y` 4-digit year, `%m` month 01-12, `%d` day, `%b` month name. Other dialects: PostgreSQL uses `date1 - date2`, `date + INTERVAL '7 days'`, `TO_CHAR(d,'YYYY-MM')`, `DATE_TRUNC('month', d)`; SQL Server uses `DATEDIFF(day, start, end)` (start first) and `DATEADD`.

### Example
Supplier lead time = receipt date minus PO date:
```sql
SELECT supplier, AVG(DATEDIFF(received_date, po_date)) AS avg_lead_days
FROM purchase_orders GROUP BY supplier;
```
PO on 10 Jan, received 24 Jan: `DATEDIFF('2025-01-24','2025-01-10') = 14` days. Monthly roll-up: `GROUP BY DATE_FORMAT(order_date,'%Y-%m')`.

### In the news
See news box. Dialect drift (MySQL vs PostgreSQL date syntax) is a practical reason to know the logic, not just one vendor's function names.

### Interview angle
> [!question] How it is asked
> "Write a query for average delivery time per month" or "Find orders delayed more than 5 days past promised date."

> [!tip] Strong answer includes
> - Correct `DATEDIFF` argument order and unit (days)
> - `DATE_FORMAT` or `DATE_TRUNC` for monthly grouping
> - Handling NULL (undelivered) dates explicitly
> - Awareness of time zones and `DATE` vs `DATETIME` when filtering with `BETWEEN` (end-of-day trap)

---

## 3. EXTRACT / DATE_PART
> 🟠 Tier 2 · _Tracker hint:_ EXTRACT(YEAR FROM order_date); MONTH, DAY, HOUR, WEEKDAY

### Definition
`EXTRACT(unit FROM date)` is the ANSI-standard way to pull a component out of a date or timestamp, and works in MySQL, PostgreSQL and Oracle.

```sql
SELECT EXTRACT(YEAR  FROM order_date) AS yr,
       EXTRACT(MONTH FROM order_date) AS mth,
       EXTRACT(HOUR  FROM order_ts)   AS hr
FROM orders;
```
MySQL shortcuts: `YEAR(d)`, `MONTH(d)`, `DAY(d)`, `HOUR(t)`, `QUARTER(d)`, `WEEK(d)`, `DAYNAME(d)`. Weekday: MySQL `WEEKDAY(d)` returns **0 = Monday ... 6 = Sunday**, whereas `DAYOFWEEK(d)` returns **1 = Sunday ... 7 = Saturday**. PostgreSQL: `DATE_PART('dow', d)` gives 0 = Sunday, and `EXTRACT(ISODOW FROM d)` gives 1 = Monday.

Caveat: `GROUP BY MONTH(d)` merges January 2024 and January 2025. Group by year and month together, or by `DATE_FORMAT(d,'%Y-%m')`.

### Example
Peak-hour analysis for a quick-commerce store: `SELECT EXTRACT(HOUR FROM order_ts) AS hr, COUNT(*) AS orders FROM orders GROUP BY hr ORDER BY orders DESC LIMIT 3;` tells you when to schedule pickers and riders. Weekend vs weekday: `CASE WHEN WEEKDAY(order_date) >= 5 THEN 'Weekend' ELSE 'Weekday' END` (5 = Saturday, 6 = Sunday in MySQL).

### In the news
See news box. The 2025 Postgres release keeps `EXTRACT` and `DATE_PART` unchanged, a reminder that ANSI-standard functions travel best across engines.

### Interview angle
> [!question] How it is asked
> "Find the busiest day of week and hour for orders" or "Why does my monthly total look inflated?"

> [!tip] Strong answer includes
> - `EXTRACT` plus the weekday numbering convention for the dialect
> - Group by year AND month to avoid merging years
> - Preference for range filters over `YEAR(col) = 2024` on large tables (index use)
> - Business interpretation: staffing, capacity or promotion timing

---

## 4. Type Casting
> 🟠 Tier 2 · _Tracker hint:_ CAST(col AS INT); CONVERT(col, DECIMAL(10,2)); STR_TO_DATE

### Definition
Casting converts a value from one data type to another, needed when numbers or dates arrive as text (CSV imports, Excel exports).

```sql
SELECT CAST('123' AS SIGNED)            AS i,   -- MySQL integer cast: SIGNED or UNSIGNED, not INT
       CAST('12.5' AS DECIMAL(10,2))    AS d,
       CONVERT('12.5', DECIMAL(10,2))   AS d2,  -- MySQL syntax CONVERT(expr, type)
       STR_TO_DATE('15-08-2025','%d-%m-%Y') AS dt, -- 2025-08-15
       CAST('2025-08-15' AS DATE)       AS dt2;
```
Points: `CAST(x AS INT)` (the tracker's form) works in PostgreSQL, SQL Server and Oracle, but MySQL's `CAST` expects `SIGNED`/`UNSIGNED` for integers; PostgreSQL uses `x::INT` or `CAST(x AS INTEGER)`; SQL Server `CONVERT(type, expr)` has the type first. Integer division trap: `5/2` is 2.5 in MySQL (decimal) but 2 in PostgreSQL/SQL Server with integer operands, so cast one side to decimal when computing ratios (`CAST(a AS DECIMAL(10,4))/b`). Implicit casting (comparing a text column to a number) can disable indexes and give silent wrong matches. `STR_TO_DATE` is the reverse of `DATE_FORMAT`: it needs a format string matching the text exactly; failures return NULL.

### Example
A CSV loaded all columns as text. Revenue per unit: `SELECT CAST(revenue AS DECIMAL(12,2)) / CAST(units AS SIGNED) FROM raw_sales;` Without the casts, text sorts as '100' < '20' because comparison is alphabetical.

### In the news
See news box. PostgreSQL 18 virtual generated columns can embed a cast once in the table definition, so every query reads clean typed values.

### Interview angle
> [!question] How it is asked
> "A numeric column was imported as text and sorts wrongly. How do you fix it?" or "Why does 5/2 return 2 in some databases?"

> [!tip] Strong answer includes
> - Explicit CAST/CONVERT and the correct target type (DECIMAL for money, not FLOAT)
> - Integer-division pitfall and fix
> - `STR_TO_DATE` with matching format for non-ISO dates
> - Better long-term fix: correct the schema or ETL step

---

## 5. Math Functions
> 🟠 Tier 2 · _Tracker hint:_ ROUND(x,2), FLOOR, CEIL, ABS, MOD, POWER, SQRT, RAND()

### Definition
```sql
SELECT ROUND(12.3456, 2)  AS r,   -- 12.35
       ROUND(1234.5, -2)  AS r2,  -- 1200 (hundreds)
       FLOOR(-2.5)        AS f,   -- -3  (towards minus infinity)
       CEIL(-2.5)         AS c,   -- -2
       ABS(-7)            AS a,   -- 7
       MOD(17, 5)         AS m,   -- 2   (same as 17 % 5)
       POWER(2, 10)       AS p,   -- 1024
       SQRT(144)          AS s,   -- 12
       RAND()             AS rnd; -- random in [0,1)
```
Useful applications: `CEIL(demand / pack_size) * pack_size` rounds an order up to whole packs; `SQRT` appears in EOQ ($EOQ = \sqrt{2DS/H}$) and safety-stock formulas ($SS = Z\sigma\sqrt{L}$); `MOD` to find odd/even or to bucket rows; `ORDER BY RAND() LIMIT 100` takes a random sample (slow on big tables). `ROUND` in MySQL rounds .5 away from zero for exact values, while some engines use banker's rounding; round only at the final step, not midway.

### Example
Demand 1,000 units per year, ordering cost 500 per order, holding cost 20 per unit per year: `SELECT ROUND(SQRT(2*1000*500/20), 1);` gives $\sqrt{50000} = 223.6$ units. Pack rounding: need 230 units, packs of 12: `CEIL(230/12)*12 = 20*12 = 240` ($230/12 = 19.17$, ceiling 20).

### In the news
See news box. Not directly affected; the point for interviews is that arithmetic functions are stable across versions, unlike text and date functions.

### Interview angle
> [!question] How it is asked
> "Round order quantities up to full cartons" or "Compute EOQ in SQL for each SKU."

> [!tip] Strong answer includes
> - FLOOR vs CEIL behaviour on negatives, ROUND with negative digits
> - Rounding only at the end and using DECIMAL
> - A business use (pack-size rounding, EOQ, safety stock)
> - Awareness that `RAND()` sampling is non-reproducible without a seed

---

## 6. COALESCE vs IFNULL vs NVL
> 🟠 Tier 2 · _Tracker hint:_ COALESCE(a,b,c) returns first non-null; IFNULL(a,b) MySQL-specific

### Definition
All three replace NULLs with a default.
| Function | Args | Engine |
|---|---|---|
| `COALESCE(a,b,c,...)` | Any number, returns the first non-NULL | ANSI standard: MySQL, PostgreSQL, SQL Server, Oracle |
| `IFNULL(a,b)` | Exactly two | MySQL (SQLite too) |
| `NVL(a,b)` | Exactly two | Oracle |
| `ISNULL(a,b)` | Two | SQL Server (different meaning in MySQL: tests NULL) |

`NULLIF(a,b)` returns NULL if a = b, which prevents division by zero: `revenue / NULLIF(units,0)`. Remember NULL semantics: `NULL = NULL` is unknown, so use `IS NULL`; aggregates such as `SUM`, `AVG` ignore NULLs (`AVG` of 10, NULL, 20 is 15, not 10), and `COUNT(col)` skips NULLs while `COUNT(*)` does not. Replacing NULL by 0 before `AVG` changes the answer, so decide deliberately.

### Example
```sql
SELECT item, COALESCE(promised_date, requested_date, order_date) AS due_date,
       COALESCE(on_hand,0) + COALESCE(on_order,0) AS inventory_position
FROM stock;
```
If on_hand = 40 and on_order is NULL, inventory position = 40 + 0 = 40; without COALESCE, 40 + NULL = NULL and the row disappears from reports.

### In the news
See news box. Because MySQL 8.0 EOL pushes migrations, prefer `COALESCE` over `IFNULL`/`NVL` so queries port across engines.

### Interview angle
> [!question] How it is asked
> "What is the difference between COALESCE and IFNULL?" or "Why is my total NULL when one column is missing?"

> [!tip] Strong answer includes
> - Portability: COALESCE is ANSI and takes many arguments
> - NULL arithmetic (any operation with NULL gives NULL)
> - `NULLIF` for divide-by-zero
> - Effect of NULLs on AVG and COUNT

---

## 7. String Splitting
> 🟠 Tier 2 · _Tracker hint:_ SUBSTRING_INDEX(email,'@',1) to extract username from email

### Definition
`SUBSTRING_INDEX(str, delim, count)` (MySQL) returns the part of the string before the `count`-th delimiter; a **negative** count counts from the right.

```sql
SELECT SUBSTRING_INDEX('rahul.k@siom.in','@', 1)  AS user_name, -- 'rahul.k'
       SUBSTRING_INDEX('rahul.k@siom.in','@',-1)  AS domain,    -- 'siom.in'
       SUBSTRING_INDEX(SUBSTRING_INDEX('a/b/c','/',2),'/',-1) AS second_part; -- 'b'
```
Nesting gives the n-th token: first take everything up to the n-th delimiter, then take the last piece. Other engines: PostgreSQL `SPLIT_PART('a/b/c','/',2)` returns 'b', and `STRING_TO_ARRAY`; SQL Server `STRING_SPLIT` (returns rows); BigQuery `SPLIT`. Alternative in MySQL: `SUBSTRING(email, 1, INSTR(email,'@')-1)`. If the delimiter is absent, `SUBSTRING_INDEX` returns the whole string. Storing delimited lists in one column violates 1NF, so splitting is a clean-up, not a design.

### Example
Group customers by email domain to spot corporate buyers:
```sql
SELECT SUBSTRING_INDEX(email,'@',-1) AS domain, COUNT(*) AS customers
FROM customers GROUP BY domain ORDER BY customers DESC;
```
Warehouse bin code 'MUM-A-12-03': `SUBSTRING_INDEX(bin_code,'-',1)` gives the site 'MUM'.

### In the news
See news box. Different engines split strings differently (`SPLIT_PART` vs `SUBSTRING_INDEX`), so state the dialect in interviews.

### Interview angle
> [!question] How it is asked
> "Extract the domain from an email" or "A column stores 'city-state-pin'. Split it into three columns."

> [!tip] Strong answer includes
> - Positive vs negative count in `SUBSTRING_INDEX`
> - Nesting to get the middle token
> - Dialect equivalents (`SPLIT_PART`, `STRING_SPLIT`)
> - Remark that multi-valued columns should be normalised (1NF)

---

## 8. Pivoting with CASE
> 🟠 Tier 2 · _Tracker hint:_ SELECT SUM(CASE WHEN month=1 THEN sales END) AS Jan, SUM(CASE WHEN month=2 THEN sales END) AS Feb

### Definition
Standard SQL has no universal `PIVOT` (SQL Server and Oracle do), so analysts use **conditional aggregation**: one `SUM(CASE ...)` per output column, with `GROUP BY` on the row key.

```sql
SELECT region,
       SUM(CASE WHEN MONTH(order_date)=1 THEN sales END) AS Jan,
       SUM(CASE WHEN MONTH(order_date)=2 THEN sales END) AS Feb,
       SUM(CASE WHEN MONTH(order_date)=3 THEN sales END) AS Mar,
       SUM(sales)                                        AS Total
FROM orders
WHERE order_date >= '2025-01-01' AND order_date < '2025-04-01'
GROUP BY region;
```
`CASE` without `ELSE` yields NULL, which `SUM` ignores; use `COUNT(CASE WHEN cond THEN 1 END)` for counts (note `COUNT(CASE ... ELSE 0 END)` would count everything). The same trick builds KPI flags such as `SUM(CASE WHEN on_time=1 THEN 1 ELSE 0 END)`. Limitation: column list is fixed in the query; dynamic pivots need prepared statements or BI tools. The reverse (unpivot) uses `UNION ALL`.

### Example
Region data: North Jan 100, Feb 120; South Jan 80, Feb 70. Output: North row Jan 100, Feb 120, Total 220; South row Jan 80, Feb 70, Total 150. Wrapping `SUM(...)` around `CASE` over the full table, with `GROUP BY region`, produces the Excel-style matrix with one query.

### In the news
See news box. Window functions and JSON features in MySQL 8 reduced the need for some pivots, but conditional aggregation remains the portable answer.

### Interview angle
> [!question] How it is asked
> "Turn rows of monthly sales into columns, one per month, without PIVOT."

> [!tip] Strong answer includes
> - `SUM(CASE WHEN ... THEN ... END)` with `GROUP BY`
> - NULL handling and `COUNT` vs `SUM` flag variants
> - Limitation: static columns; mention dynamic SQL or BI tool alternative
> - Filtering date range with a sargable condition first

---

## 9. JSON Functions (MySQL 8+)
> 🟠 Tier 2 · _Tracker hint:_ JSON_EXTRACT, JSON_OBJECT, JSON_ARRAY — for semi-structured data

### Definition
MySQL has a native `JSON` data type (5.7+) with validation and functions for semi-structured payloads such as API responses, clickstream or IoT events.

```sql
-- Sample column: attrs = '{"colour":"red","dims":{"w":10,"h":20},"tags":["fragile","cold"]}'
SELECT JSON_EXTRACT(attrs, '$.colour')       AS c1,  -- "red" (with quotes)
       attrs->'$.colour'                     AS c2,  -- same as JSON_EXTRACT
       attrs->>'$.colour'                    AS c3,  -- red (unquoted text)
       JSON_UNQUOTE(JSON_EXTRACT(attrs,'$.dims.w')) AS w,
       JSON_EXTRACT(attrs,'$.tags[0]')       AS t0;  -- "fragile" (arrays are 0-indexed)

SELECT JSON_OBJECT('sku','A1','qty',5) AS o,  -- {"sku": "A1", "qty": 5}
       JSON_ARRAY(1,2,3)               AS a;  -- [1, 2, 3]
```
Also `JSON_SET`, `JSON_CONTAINS`, `JSON_LENGTH`, and `JSON_TABLE` (8.0) to turn arrays into rows. Querying inside JSON cannot use a normal index; create a **generated column** over the JSON path and index that. PostgreSQL uses `jsonb` with `->`, `->>` and GIN indexes. Use JSON for flexible attributes; keep core, frequently filtered fields as proper columns.

### Example
A supplier-portal sends `{"po":"P77","lines":[{"sku":"A1","qty":5},{"sku":"B2","qty":3}]}`. `JSON_LENGTH(payload,'$.lines')` returns 2 lines, and `JSON_EXTRACT(payload,'$.lines[1].qty')` returns 3.

### In the news
See news box. These JSON features are MySQL 5.7/8.0 era; with 8.0 at end of life in April 2026, check them against 8.4 LTS before migrating.

### Interview angle
> [!question] How it is asked
> "How would you query event data stored as JSON?" or "When would you store JSON in a relational table?"

> [!tip] Strong answer includes
> - `->>` or `JSON_UNQUOTE` to get clean text
> - Indexing via generated columns
> - Trade-off: flexibility vs integrity, performance and 1NF
> - Alternative: normalise the stable fields, keep JSON for the variable part

---

## 10. Regular Expressions
> 🟠 Tier 2 · _Tracker hint:_ REGEXP_LIKE, REGEXP_REPLACE — pattern matching beyond LIKE

### Definition
`LIKE` supports only `%` (any string) and `_` (one character). Regular expressions allow classes, repetition and anchors. MySQL 8 (ICU-based):

```sql
SELECT * FROM customers WHERE REGEXP_LIKE(phone, '^[6-9][0-9]{9}$');       -- Indian mobile: 10 digits starting 6-9
SELECT * FROM customers WHERE email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$';
SELECT REGEXP_REPLACE('Ph: +91-98765 43210', '[^0-9]', '') AS digits;       -- '919876543210'
SELECT REGEXP_SUBSTR('PO-2025-0042', '[0-9]{4}$')          AS seq;          -- '0042'
SELECT REGEXP_INSTR('abc123', '[0-9]')                     AS pos;          -- 4
```
Tokens: `^` start, `$` end, `[]` set, `{n}` exactly n, `+` one or more, `.` any char, `\\d` digit (backslash escaped in MySQL strings). PostgreSQL uses `~` and `~*` operators and `REGEXP_REPLACE(str, pattern, repl, 'g')` (flag `g` for global); Oracle has `REGEXP_LIKE`. Regex scans cannot use ordinary indexes and are slow on very large tables, so use them for cleaning and validation, not hot query paths. Validate pin codes with `^[1-9][0-9]{5}$` (6 digits, not starting 0).

### Example
Data-quality check: count invalid GSTINs. A GSTIN is 15 characters (state code, PAN, entity, Z, check). A simple structural test is `REGEXP_LIKE(gstin, '^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$')` and the query `SELECT COUNT(*) FROM vendors WHERE NOT REGEXP_LIKE(gstin, ...)` shows how many vendor records need fixing before GST reconciliation.

### In the news
See news box. PostgreSQL 18 text-processing additions and MySQL's ICU regex engine both show text handling is still evolving; test regex behaviour after any version upgrade.

### Interview angle
> [!question] How it is asked
> "Validate phone numbers or pin codes in SQL" or "Strip non-numeric characters from a column."

> [!tip] Strong answer includes
> - When LIKE is not enough and a regex is
> - Correct anchors (`^ $`) and quantifiers
> - Performance caveat (no index use) and dialect differences
> - Using it for data-quality audits before analysis

---

## 11. ⭐ Advanced: Window-friendly Date Bucketing (DATE_TRUNC, week and fiscal periods)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Business reporting rarely follows calendar months. Indian companies use a **fiscal year April–March** (FY2025-26 = 1 Apr 2025 to 31 Mar 2026), so SQL needs fiscal mapping and week bucketing.

```sql
-- MySQL: fiscal year and quarter (Apr start)
SELECT order_date,
       CASE WHEN MONTH(order_date) >= 4 THEN YEAR(order_date)+1 ELSE YEAR(order_date) END AS fy_end_year,
       MOD(MONTH(order_date) + 8, 12) DIV 3 + 1 AS fiscal_qtr   -- Apr-Jun=1, Jul-Sep=2, Oct-Dec=3, Jan-Mar=4
FROM orders;

-- Week start (Monday) in MySQL
SELECT DATE_SUB(order_date, INTERVAL WEEKDAY(order_date) DAY) AS week_start FROM orders;

-- PostgreSQL
SELECT DATE_TRUNC('month', order_date) AS m, DATE_TRUNC('week', order_date) AS w FROM orders;
```
Check the fiscal quarter arithmetic: April gives MOD(4+8,12)=0, 0 DIV 3 = 0, plus 1 = Q1; January gives MOD(9,12)=9, 9 DIV 3 = 3, plus 1 = Q4. A shared **date dimension** table (one row per date with fiscal year, quarter, week, holiday flag) is better than repeating this logic in every query.

### Example
Order dated 15 Feb 2026: month 2 < 4, so fiscal year ends 2026 (FY2025-26); quarter = MOD(10,12) DIV 3 + 1 = 3 + 1 = 4, i.e. Q4. An order on 5 Apr 2026 is FY2026-27 Q1.

### In the news
See news box. Postgres and MySQL are both moving versions, so putting date logic in a reusable date dimension insulates reports from syntax changes.

### Interview angle
> [!question] How it is asked
> "Report sales by Indian fiscal quarter" or "How do you build weekly numbers when weeks start on Monday?"

> [!tip] Strong answer includes
> - Fiscal mapping (April start) done with CASE or a date dimension
> - Sargable range filters instead of functions on the column
> - Week definition (ISO vs Sunday start) stated explicitly
> - Idea of a calendar table, which also supports gap analysis (see [[061 SQL for SCM & Business Analytics]])

---

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
