---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "SQL Foundations & Data Types"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# SQL Foundations & Data Types

[[_Index - SQL & Databases|SQL & Databases]] · [[054 Filtering, Sorting & CASE]] ➡

> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. What is SQL & Why It Matters]]
2. [[#2. Database Concepts]]
3. [[#3. Data Types]]
4. [[#4. DDL — CREATE TABLE]]
5. [[#5. DDL — ALTER & DROP]]
6. [[#6. Constraints]]
7. [[#7. INSERT / UPDATE / DELETE]]
8. [[#8. SELECT Basics]]
9. [[#9. Aliases]]
10. [[#10. NULL Handling]]
11. [[#11. ⭐ Advanced: Normalization (1NF to 3NF) vs Denormalization]]
12. [[#12. ⭐ Advanced: Indexes & Reading EXPLAIN]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Which SQL database is actually used, and what changed in 2025–26
> **PostgreSQL is the most-used database (Stack Overflow Developer Survey 2025).** Among all respondents PostgreSQL is used by **55.6%**, MySQL **40.5%**, SQLite **37.5%**, Microsoft SQL Server **30.1%** and MongoDB **24%**; among professional developers PostgreSQL is **58.2%**. The survey notes PostgreSQL is both the most-used and most-desired database for the third year running. ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
>
> **PostgreSQL 18 released (25 Sep 2025).** Headline features: an asynchronous I/O subsystem (benchmarks show gains up to about 3x in some scenarios), skip-scan lookups on multicolumn B-tree indexes, virtual generated columns and OAuth authentication. ([LWN](https://lwn.net/Articles/1039483/))
>
> **MySQL 8.0 reached end of life (30 Apr 2026).** Extended support stopped on 30 April 2026; MySQL 8.4 is the recommended long-term-support (LTS) upgrade path. ([OpenLogic](https://www.openlogic.com/blog/mysql-8-end-of-life))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. What is SQL & Why It Matters
> 🔴 Tier 1 · _Tracker hint:_ Structured Query Language; RDBMS vs NoSQL; SQL dialects (MySQL, PostgreSQL, SQL Server, SQLite)

### Definition
**SQL (Structured Query Language)** is the standard, declarative language for defining, querying and changing data held in a **relational database management system (RDBMS)**. *Declarative* means you state **what** result you want, not **how** to fetch it; the database optimiser chooses the execution plan.

SQL statements fall into families:

| Family | Purpose | Examples |
|---|---|---|
| DDL (Data Definition) | Define structure | CREATE, ALTER, DROP, TRUNCATE |
| DML (Data Manipulation) | Change data | INSERT, UPDATE, DELETE |
| DQL (Query) | Read data | SELECT |
| DCL (Control) | Permissions | GRANT, REVOKE |
| TCL (Transaction) | Commit control | COMMIT, ROLLBACK |

**RDBMS vs NoSQL:** an RDBMS stores data in tables with a fixed schema, relationships via keys and **ACID** guarantees (Atomicity, Consistency, Isolation, Durability). NoSQL stores (MongoDB documents, Redis key-value, Cassandra wide-column) trade rigid schema and joins for horizontal scale and flexible structure. **Dialects** share a core (ANSI SQL) but differ in details: MySQL uses `LIMIT`, SQL Server uses `TOP`, PostgreSQL has `ILIKE` and `FETCH FIRST`, SQLite is a serverless embedded file database.

Why it matters for business roles: ERP, CRM, e-commerce and WMS data sits in relational tables, so SQL is the fastest way to answer "what happened and why" without waiting for an analyst.

### Example
A Flipkart-style analyst needs "orders per city last month". In Excel, 20 million rows will not open. In SQL: `SELECT city, COUNT(*) FROM orders WHERE order_date >= '2026-09-01' AND order_date < '2026-10-01' GROUP BY city;` returns a few dozen rows in seconds because the database does the filtering and counting where the data lives.

### In the news
See news box. PostgreSQL leading the 2025 survey at 55.6% is the strongest argument for learning the standard core of SQL rather than one vendor's quirks.

### Interview angle
> [!question] How it is asked
> "What is SQL and how is it different from NoSQL?" or "Have you used SQL? Which dialect?" (often followed by a live query).

> [!tip] Strong answer includes
> - Declarative language, the DDL/DML/DQL split
> - RDBMS = tables + keys + ACID; NoSQL = flexible schema, scale-out, used when data is unstructured or write-heavy
> - Honest dialect statement ("core ANSI SQL; I know the MySQL and PostgreSQL differences for LIMIT, date functions")
> - A business example of a question SQL answers quickly

---

## 2. Database Concepts
> 🔴 Tier 1 · _Tracker hint:_ Table, row, column, schema, primary key, foreign key, index, constraint

### Definition
- **Table (relation):** a set of rows sharing the same columns, e.g. `orders`.
- **Row (record/tuple):** one entity instance; **column (field/attribute):** one property with a data type.
- **Schema:** the logical container and blueprint (tables, views, relationships). In MySQL, schema is a synonym for database; in PostgreSQL and SQL Server it is a namespace inside a database.
- **Primary key (PK):** column(s) that uniquely identify a row; cannot be NULL, only one per table.
- **Foreign key (FK):** column that references a PK in another table, enforcing **referential integrity** (you cannot create an order for a customer who does not exist).
- **Index:** a separate sorted structure (usually a B-tree) that speeds up lookups and joins at the cost of slower writes and extra storage.
- **Constraint:** a rule the database enforces automatically (NOT NULL, UNIQUE, CHECK...).

A **candidate key** is any column set that could be a PK; a **composite key** uses two or more columns (e.g. `order_id, line_no`); a **surrogate key** is a system-generated id (auto-increment) with no business meaning.

### Example
`customers(cust_id PK, name, city)` and `orders(order_id PK, cust_id FK, amount)`. One customer has many orders (1:N). Deleting customer 7 while orders exist either fails or cascades depending on the FK rule (`ON DELETE RESTRICT` or `CASCADE`).

### In the news
See news box. PostgreSQL 18's virtual generated columns are a column-level feature: the value is computed when read, so no extra storage is used.

### Interview angle
> [!question] How it is asked
> "Difference between primary key and foreign key?" "Can a table have two primary keys?" "What is an index and when would you not add one?"

> [!tip] Strong answer includes
> - PK: unique and not null, one per table; FK: references a PK, may repeat and (usually) may be NULL
> - A composite PK is still one primary key
> - Index: faster reads, slower writes; avoid on tiny or frequently updated low-cardinality columns
> - Concrete customer-orders example

---

## 3. Data Types
> 🔴 Tier 1 · _Tracker hint:_ INT, BIGINT, VARCHAR, CHAR, TEXT, DATE, DATETIME, TIMESTAMP, BOOLEAN, DECIMAL, FLOAT

### Definition
A data type fixes what values a column may hold and how much storage it uses. Picking the right one affects correctness, speed and size.

| Type | Use | Note |
|---|---|---|
| INT | Whole numbers up to about 2.1 billion | 4 bytes |
| BIGINT | Very large ids/counts | 8 bytes |
| DECIMAL(p,s) | Exact money, quantities | p total digits, s after the point |
| FLOAT / DOUBLE | Approximate scientific values | Rounding error; never for money |
| CHAR(n) | Fixed length codes (state code) | Padded with spaces |
| VARCHAR(n) | Variable text up to n | Names, SKUs |
| TEXT | Long free text | Limited indexing |
| DATE | Calendar date | `2026-10-02` |
| DATETIME / TIMESTAMP | Date plus time | In MySQL, TIMESTAMP is stored in UTC and has a narrower range (1970 to 2038) |
| BOOLEAN | True/false | MySQL stores it as TINYINT(1) |

`DECIMAL(10,2)` holds up to 8 digits before the decimal point and 2 after, so the maximum is 99,999,999.99.

### Example
Storing a price of 0.1 + 0.2 in FLOAT gives 0.30000000000000004 in many systems, while `DECIMAL(10,2)` gives exactly 0.30. That is why invoices, GST amounts and inventory valuation use DECIMAL, and sensor readings or ML scores may use FLOAT.

### In the news
See news box. MySQL 8.0 going end of life in April 2026 is a reminder to check type behaviour (for example implicit conversions and TIMESTAMP limits) when upgrading to 8.4.

### Interview angle
> [!question] How it is asked
> "Why not use FLOAT for money?" "Difference between CHAR and VARCHAR?" "DATETIME vs TIMESTAMP?"

> [!tip] Strong answer includes
> - DECIMAL for exact arithmetic, FLOAT for approximate
> - CHAR fixed length (faster for fixed codes), VARCHAR variable
> - TIMESTAMP time-zone aware and range-limited in MySQL; DATETIME wider range, no conversion
> - Choose the smallest type that fits (INT vs BIGINT) for index and memory efficiency

---

## 4. DDL — CREATE TABLE
> 🔴 Tier 1 · _Tracker hint:_ CREATE TABLE orders (id INT PRIMARY KEY, cust_id INT, amount DECIMAL(10,2), order_date DATE)

### Definition
**CREATE TABLE** defines a new table with its columns, types and constraints. DDL statements usually auto-commit in MySQL (they cannot be rolled back); PostgreSQL allows transactional DDL.

```sql
CREATE TABLE orders (
    id          INT PRIMARY KEY AUTO_INCREMENT,   -- PostgreSQL: SERIAL or GENERATED ... AS IDENTITY
    cust_id     INT NOT NULL,
    amount      DECIMAL(10,2) DEFAULT 0.00,
    order_date  DATE NOT NULL,
    status      VARCHAR(20) DEFAULT 'NEW',
    CONSTRAINT fk_cust FOREIGN KEY (cust_id) REFERENCES customers(id)
);

-- Create from a query result
CREATE TABLE orders_2026 AS
SELECT * FROM orders WHERE order_date >= '2026-01-01';
```

Good practice: name constraints, always define a PK, use `IF NOT EXISTS` in scripts, and create parent tables before child tables.

### Example
A warehouse team creates `stock(sku VARCHAR(20), wh_id INT, qty INT, PRIMARY KEY (sku, wh_id))`. The composite PK means each SKU appears once per warehouse, which matches the business rule exactly.

### In the news
See news box. Skip-scan in PostgreSQL 18 makes composite indexes such as (sku, wh_id) useful even when a query filters only on the second column.

### Interview angle
> [!question] How it is asked
> "Write the DDL for an orders table." or "Design tables for a simple order system."

> [!tip] Strong answer includes
> - Correct types (DECIMAL for amount, DATE for date)
> - PK, FK and NOT NULL stated deliberately
> - Parent-before-child creation order
> - Mentions that CREATE TABLE ... AS copies data but not constraints or indexes

---

## 5. DDL — ALTER & DROP
> 🔴 Tier 1 · _Tracker hint:_ ALTER TABLE ADD/DROP/MODIFY column; DROP TABLE; TRUNCATE vs DELETE

### Definition
```sql
ALTER TABLE orders ADD COLUMN region VARCHAR(30);
ALTER TABLE orders MODIFY COLUMN amount DECIMAL(12,2);   -- MySQL
ALTER TABLE orders ALTER COLUMN amount TYPE NUMERIC(12,2); -- PostgreSQL
ALTER TABLE orders DROP COLUMN region;
ALTER TABLE orders RENAME COLUMN status TO order_status;
DROP TABLE orders;           -- removes structure AND data
TRUNCATE TABLE orders;       -- removes all rows, keeps structure
DELETE FROM orders WHERE order_date < '2024-01-01';
```

| | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| Type | DML | DDL | DDL |
| Removes | Chosen rows | All rows | Table itself |
| WHERE allowed | Yes | No | No |
| Rollback | Yes (in a transaction) | Usually no in MySQL; yes in PostgreSQL | Usually no |
| Speed | Slower (row by row, logged) | Fast | Fast |
| Resets AUTO_INCREMENT | No | Yes (MySQL) | n/a |

### Example
Monthly staging table `stg_sales` is reloaded every night: `TRUNCATE TABLE stg_sales;` then bulk insert. Using `DELETE FROM stg_sales;` on 50 million rows would be far slower and bloat the transaction log.

### In the news
See news box. With MySQL 8.0 retired, teams migrating to 8.4 run ALTER scripts on production tables, where online DDL and testing on a copy first matter.

### Interview angle
> [!question] How it is asked
> "Difference between DELETE, TRUNCATE and DROP?" (one of the most common SQL screening questions)

> [!tip] Strong answer includes
> - DML vs DDL, WHERE support, rollback and speed
> - Identity reset behaviour
> - Safety habit: run a SELECT with the same WHERE first, and take a backup before DROP
> - Triggers fire on DELETE but not on TRUNCATE

---

## 6. Constraints
> 🔴 Tier 1 · _Tracker hint:_ NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT — usage and purpose

### Definition
Constraints push business rules into the database so bad data cannot get in, regardless of which application writes it.

| Constraint | Purpose | Allows NULL? |
|---|---|---|
| NOT NULL | Value required | No |
| UNIQUE | No duplicates | Yes (MySQL/PostgreSQL allow multiple NULLs) |
| PRIMARY KEY | Unique + not null identifier | No |
| FOREIGN KEY | Must match a parent key | Yes unless NOT NULL |
| CHECK | Custom condition | Passes if condition is NULL |
| DEFAULT | Value used when omitted | n/a |

```sql
CREATE TABLE products (
    sku       VARCHAR(20) PRIMARY KEY,
    name      VARCHAR(100) NOT NULL,
    barcode   VARCHAR(20) UNIQUE,
    price     DECIMAL(10,2) CHECK (price > 0),
    uom       VARCHAR(5) DEFAULT 'EA',
    sup_id    INT,
    FOREIGN KEY (sup_id) REFERENCES suppliers(id) ON DELETE SET NULL
);
```
CHECK is enforced in MySQL from version 8.0.16; earlier versions parsed and ignored it.

### Example
Without `CHECK (qty >= 0)` a bug in a returns module could push stock to -40, which would silently distort inventory valuation. With the constraint the insert fails loudly and the bug is found on day one.

### In the news
See news box. As PostgreSQL adoption grows, its strict constraint enforcement (and transactional DDL) is often cited as a reason teams choose it for data-integrity-critical systems.

### Interview angle
> [!question] How it is asked
> "What constraints do you know? Difference between UNIQUE and PRIMARY KEY?"

> [!tip] Strong answer includes
> - All six with a one-line purpose
> - PK = UNIQUE + NOT NULL, one per table; UNIQUE can be many and allow NULL
> - FK actions: CASCADE, SET NULL, RESTRICT
> - Why constraints beat application-only validation

---

## 7. INSERT / UPDATE / DELETE
> 🔴 Tier 1 · _Tracker hint:_ DML statements; WHERE clause in UPDATE/DELETE; bulk insert

### Definition
```sql
-- single and multi-row insert
INSERT INTO orders (cust_id, amount, order_date)
VALUES (101, 2500.00, '2026-10-01'),
       (102,  899.50, '2026-10-01');

-- insert from a query
INSERT INTO orders_archive SELECT * FROM orders WHERE order_date < '2024-01-01';

UPDATE orders SET status = 'SHIPPED', amount = amount * 1.05
WHERE id = 5001;

DELETE FROM orders WHERE status = 'CANCELLED';

-- bulk load (MySQL)
LOAD DATA INFILE '/data/orders.csv' INTO TABLE orders
FIELDS TERMINATED BY ',' IGNORE 1 ROWS;
```
**Golden rule:** an UPDATE or DELETE without WHERE changes **every row**. Wrap risky changes in a transaction (`START TRANSACTION; ... ROLLBACK/COMMIT;`) and preview with SELECT. Multi-row INSERT and bulk loaders are far faster than one INSERT per row because of fewer round trips and commits.

### Example
A price revision of +5% for the "Beverages" category: first `SELECT COUNT(*) FROM products WHERE category='Beverages';` returns 120. Then `UPDATE products SET price = ROUND(price*1.05,2) WHERE category='Beverages';` reports 120 rows affected, matching expectation. A mismatch would signal a wrong filter.

### In the news
See news box. PostgreSQL 18's async I/O targets exactly bulk read and vacuum workloads, which is where large batch DML pain shows up.

### Interview angle
> [!question] How it is asked
> "What happens if you run UPDATE without WHERE?" "How would you safely delete 10 million rows?"

> [!tip] Strong answer includes
> - Every row is affected; use transactions and a preview SELECT
> - Delete in batches (e.g. LIMIT 10000 loops) to avoid long locks and log growth
> - Bulk load tools rather than row-by-row inserts
> - Mention backups or soft-delete flags in production

---

## 8. SELECT Basics
> 🔴 Tier 1 · _Tracker hint:_ SELECT col1, col2 FROM table WHERE condition ORDER BY col LIMIT n

### Definition
```sql
SELECT order_id, cust_id, amount
FROM   orders
WHERE  amount > 1000
ORDER  BY amount DESC
LIMIT  10;
```
**Written order:** SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT.
**Logical execution order:** FROM (and JOINs) → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT. This explains why a column alias defined in SELECT cannot be used in WHERE (but can be used in ORDER BY), and why WHERE cannot contain aggregates.

Avoid `SELECT *` in production queries: it reads unneeded columns, defeats covering indexes and breaks when the schema changes.

### Example
"Top 5 largest orders this month": `SELECT order_id, amount FROM orders WHERE order_date >= '2026-10-01' ORDER BY amount DESC LIMIT 5;` The engine filters to October rows first, sorts only those, then returns 5.

### In the news
See news box. PostgreSQL 18 skip-scan helps queries whose WHERE clause skips the leading column of a composite index.

### Interview angle
> [!question] How it is asked
> "What is the order of execution of a SQL query?" or a basic top-N query on a whiteboard.

> [!tip] Strong answer includes
> - Written vs logical order, with the alias consequence
> - Why SELECT * is discouraged
> - Deterministic ORDER BY before LIMIT
> - Names columns explicitly and formats the query cleanly

---

## 9. Aliases
> 🔴 Tier 1 · _Tracker hint:_ SELECT col AS alias, table AS t; improves readability in joins

### Definition
An **alias** is a temporary name for a column or table within one query. `AS` is optional but recommended.

```sql
SELECT o.order_id,
       o.amount * 1.18 AS amount_with_gst,
       c.name          AS customer
FROM   orders AS o
JOIN   customers AS c ON c.id = o.cust_id;
```
- **Column alias:** renames output and names computed expressions. It cannot be used in WHERE (not yet evaluated) but can be used in ORDER BY (and in GROUP BY in MySQL/PostgreSQL).
- **Table alias:** shortens names and is **mandatory** for self-joins and derived tables (subqueries in FROM).
- Use quotes for aliases with spaces: `AS "Total Sales"` (PostgreSQL/standard) or backticks in MySQL.

### Example
Self-join for employees and managers: `FROM emp e JOIN emp m ON e.mgr_id = m.id`. Without distinct aliases `e` and `m`, the query is ambiguous and fails.

### In the news
See news box. Readable aliasing matters more as teams share SQL in code review across MySQL and PostgreSQL stacks.

### Interview angle
> [!question] How it is asked
> "Why can't I use my column alias in the WHERE clause?" or "When are table aliases mandatory?"

> [!tip] Strong answer includes
> - Logical execution order explains the WHERE restriction
> - Mandatory for self-joins and derived tables
> - Short but meaningful alias names (`o`, `c`), consistent across the query
> - Prefix every column with its alias in multi-table queries

---

## 10. NULL Handling
> 🔴 Tier 1 · _Tracker hint:_ IS NULL, IS NOT NULL, COALESCE(col, default), NULLIF(a,b), IFNULL

### Definition
**NULL means unknown or missing, not zero and not an empty string.** SQL uses **three-valued logic** (TRUE, FALSE, UNKNOWN). Any comparison with NULL yields UNKNOWN, and WHERE keeps only TRUE rows, so `col = NULL` never matches; use `IS NULL`.

```sql
SELECT * FROM orders WHERE ship_date IS NULL;
SELECT COALESCE(discount, 0)    AS disc  FROM orders;  -- first non-NULL argument (standard)
SELECT IFNULL(discount, 0)      AS disc  FROM orders;  -- MySQL, two arguments
SELECT amount / NULLIF(qty, 0)  AS unit_price FROM orders; -- NULLIF returns NULL if equal; avoids divide-by-zero
```
Behaviour to remember: `NULL + 5 = NULL`; aggregates (SUM, AVG, COUNT(col)) ignore NULLs, but COUNT(*) counts them; `NULL = NULL` is UNKNOWN; NULLs group together in GROUP BY and DISTINCT; `x NOT IN (..., NULL)` returns no rows.

### Example
Discount column values: 10, NULL, 20. `AVG(discount)` = (10+20)/2 = **15** (NULL ignored). `AVG(COALESCE(discount,0))` = (10+0+20)/3 = **10**. Which is right depends on whether NULL means "not applicable" or "zero discount", so state the assumption.

### In the news
See news box. As SQL becomes standard analyst equipment, NULL mishandling remains the most common silent cause of wrong dashboards.

### Interview angle
> [!question] How it is asked
> "What is the difference between NULL and 0?" "Why does `WHERE col = NULL` return nothing?" "How do aggregates treat NULL?"

> [!tip] Strong answer includes
> - NULL = unknown; three-valued logic; IS NULL syntax
> - COALESCE vs IFNULL (standard vs MySQL) and NULLIF for divide-by-zero
> - COUNT(*) vs COUNT(col), AVG ignoring NULLs, with the 15 vs 10 example
> - The NOT IN with NULL trap (link: [[057 Subqueries & CTEs]])

---

## 11. ⭐ Advanced: Normalization (1NF to 3NF) vs Denormalization
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Normalization** organises tables to remove redundancy and update anomalies (insert, update, delete).
- **1NF:** atomic values, no repeating groups (no "A,B,C" in one cell).
- **2NF:** 1NF plus no **partial dependency**: every non-key column depends on the *whole* composite key.
- **3NF:** 2NF plus no **transitive dependency**: non-key columns depend only on the key ("the key, the whole key, and nothing but the key").
- **BCNF** is a stricter 3NF.

**Denormalization** deliberately duplicates data (pre-joined or summary tables, star schemas) to speed up reads in analytics, at the cost of storage and update complexity. OLTP systems (order entry) are normalised; OLAP/data warehouses are often denormalised into **fact** and **dimension** tables.

### Example
`orders(order_id, cust_id, cust_name, cust_city)` repeats customer details on every order; changing a customer's city means updating many rows. Splitting into `customers(cust_id, name, city)` and `orders(order_id, cust_id)` stores the city once (3NF), because `cust_name` depended on `cust_id`, not on `order_id` (transitive dependency).

### In the news
See news box. Postgres and MySQL both remain core OLTP engines; warehouse-style denormalised models are built on top of them or on cloud warehouses.

### Interview angle
> [!question] How it is asked
> "What is normalization? Explain 1NF, 2NF, 3NF." or "When would you denormalize?"

> [!tip] Strong answer includes
> - Each form defined in one line with a tiny example
> - Anomalies it prevents
> - Trade-off: fewer anomalies versus more joins
> - Denormalise for read-heavy reporting, not for transaction tables

---

## 12. ⭐ Advanced: Indexes & Reading EXPLAIN
> ⭐ Advanced · _Added beyond the tracker_

### Definition
An **index** (typically a B-tree) lets the engine find rows without scanning the whole table: lookup cost goes from O(n) to about O(log n). Types: single-column, **composite** (column order matters: the **leftmost-prefix rule**), unique, covering (index contains every column the query needs), clustered (table rows stored in index order; InnoDB clusters on the PK).

```sql
CREATE INDEX idx_orders_cust_date ON orders (cust_id, order_date);
EXPLAIN SELECT * FROM orders WHERE cust_id = 101 AND order_date >= '2026-09-01';
-- PostgreSQL: EXPLAIN ANALYZE shows actual timings
```
In EXPLAIN look for a full table scan (`type = ALL` in MySQL, `Seq Scan` in PostgreSQL), the index chosen, and estimated vs actual rows. Indexes become useless when you wrap the column in a function (`WHERE YEAR(order_date)=2026`) or use a leading wildcard (`LIKE '%abc'`). Every extra index slows INSERT/UPDATE.

### Example
A table of 10 million orders: a full scan reads all 10,000,000 rows to find one customer. A B-tree with fan-out of about 100 needs roughly $\log_{100}(10^7)$ = 3.5, so about 4 page reads. That is the difference between seconds and milliseconds.

### In the news
See news box. PostgreSQL 18's skip-scan lets a composite index on (a, b) serve queries that filter only on b in some cases, easing the classic leftmost-prefix limitation.

### Interview angle
> [!question] How it is asked
> "A query on a 10-million-row table is slow. How do you speed it up?"

> [!tip] Strong answer includes
> - Run EXPLAIN first; identify full scan versus index use
> - Composite index design, leftmost-prefix rule, avoiding functions on indexed columns
> - Covering index and selecting only needed columns
> - Costs: write overhead and storage, so index selectively

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
