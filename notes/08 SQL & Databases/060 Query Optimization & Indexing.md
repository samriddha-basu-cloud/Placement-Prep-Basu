---
tags: [sql-databases, tier2]
area: SQL & Databases
topic: "Query Optimization & Indexing"
tier: Tier 2
roles: All Roles
status: complete
subtopics: 12
---
# Query Optimization & Indexing

⬅ [[059 String, Date & Advanced Functions]] · [[_Index - SQL & Databases|SQL & Databases]] · [[061 SQL for SCM & Business Analytics]] ➡

> **Area:** SQL & Databases · **Priority:** 🟠 Tier 2 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. EXPLAIN / EXPLAIN ANALYZE]]
2. [[#2. Index Types]]
3. [[#3. When to Index]]
4. [[#4. Avoid SELECT *]]
5. [[#5. Avoid Functions on Indexed Columns]]
6. [[#6. Query Rewriting]]
7. [[#7. Partitioning]]
8. [[#8. Normalization (1NF/2NF/3NF)]]
9. [[#9. Denormalization for Analytics]]
10. [[#10. Transactions & ACID]]
11. [[#11. ⭐ Advanced: Composite Index Design and Reading Plans (ESR rule, selectivity, covering)]]
12. [[#12. ⭐ Advanced: Isolation Levels, Locking and Deadlocks]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): database engines are baking optimisation into the planner
> **PostgreSQL 18 released (25 Sep 2025).** The release announcement lists an asynchronous I/O subsystem with "up to 3x" faster reads from storage for some workloads (sequential scans, bitmap heap scans, vacuum), **skip scan** lookups on multicolumn B-tree indexes, index use for `WHERE ... OR ...` conditions, hash-join improvements, and planner statistics that now carry over during major-version upgrades. ([PostgreSQL announcement](https://www.postgresql.org/about/news/postgresql-18-released-3142/))
>
> **MySQL 8.0 end of life (April 2026).** The MySQL 8.0 release notes say that "As of April 2026, with version 8.0.46, MySQL 8.0 reaches End of Life (EoL)" and recommend moving to MySQL 8.4 LTS or an Innovation release, so execution-plan behaviour must be re-tested on upgrade. ([MySQL release notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. EXPLAIN / EXPLAIN ANALYZE
> 🟠 Tier 2 · _Tracker hint:_ Shows query execution plan; look for full table scans vs index scans

### Definition
`EXPLAIN` shows the **execution plan** the optimiser chose for a query without running it: join order, access method, which index (if any) and estimated rows. `EXPLAIN ANALYZE` (PostgreSQL; MySQL 8.0.18+) actually **executes** the query and adds real timings and row counts, so you can compare *estimated vs actual* rows. A big gap means stale statistics (`ANALYZE TABLE` in MySQL, `ANALYZE` in PostgreSQL).

```sql
EXPLAIN SELECT * FROM orders WHERE customer_id = 42;
EXPLAIN ANALYZE SELECT o.order_id FROM orders o JOIN customers c ON c.id = o.customer_id WHERE c.city = 'Nashik';
```
MySQL `EXPLAIN` columns to read: `type` (best to worst: `const`, `eq_ref`, `ref`, `range`, `index`, `ALL`), `key` (index used), `rows` (estimated rows examined), `Extra` (`Using index` = covering; `Using filesort` and `Using temporary` are warning signs). In PostgreSQL look for `Seq Scan` vs `Index Scan`/`Index Only Scan`/`Bitmap Heap Scan`, and join types (Nested Loop, Hash Join, Merge Join). A full scan is not always bad: on small tables, or when the query returns a large fraction of rows, a scan is cheaper than an index. Caution: `EXPLAIN ANALYZE` on `INSERT/UPDATE/DELETE` really modifies data; wrap in a transaction and roll back.

### Example
`SELECT * FROM orders WHERE customer_id = 42` on 10 million rows with no index shows `type = ALL, rows = ~10,000,000`. After `CREATE INDEX idx_cust ON orders(customer_id)` the plan shows `type = ref, key = idx_cust, rows = ~25` (if each customer has about 25 orders): 400,000 times fewer rows examined (10,000,000 / 25).

### In the news
See news box. PostgreSQL 18 added skip scans and OR-condition index use, so plans that showed a sequential scan on an older version may change after upgrade; re-check with `EXPLAIN`.

### Interview angle
> [!question] How it is asked
> "A query is slow. What do you do first?" or "How do you read an EXPLAIN output?"

> [!tip] Strong answer includes
> - Run EXPLAIN (ANALYZE) first, before guessing; read access type, key, rows
> - Compare estimated vs actual rows and refresh statistics if far apart
> - Know that a scan can be correct for small tables or low-selectivity filters
> - Then act: add/adjust index, rewrite query, reduce columns; re-measure

---

## 2. Index Types
> 🟠 Tier 2 · _Tracker hint:_ B-tree (default), Hash, Full-text, Composite, Covering index

### Definition
An **index** is a separate sorted structure that lets the database find rows without scanning the table, at the cost of extra storage and slower writes.

| Type | Best for | Notes |
|---|---|---|
| **B-tree** (default) | Equality, ranges (`<`, `BETWEEN`), `ORDER BY`, prefix `LIKE 'abc%'` | Balanced tree, lookup cost is logarithmic |
| **Hash** | Equality only (`=`) | No range or sort; PostgreSQL `USING HASH`, MySQL MEMORY engine (InnoDB uses an internal adaptive hash) |
| **Full-text** | Word search in text (`MATCH ... AGAINST` in MySQL) | Handles stop-words and ranking, unlike `LIKE '%word%'` |
| **Composite** | Multiple columns in one index | Follows the **leftmost-prefix rule**: index (a,b,c) serves filters on a; a,b; a,b,c but not b alone |
| **Covering** | Query answered from the index alone | All selected and filtered columns are in the index (`Using index`); no table lookup |
| **Unique / Primary** | Enforce uniqueness | In InnoDB the primary key is the clustered index (rows stored in its order) |

```sql
CREATE INDEX idx_cust_date ON orders (customer_id, order_date);   -- composite
CREATE UNIQUE INDEX uq_sku ON products (sku);
CREATE FULLTEXT INDEX ft_desc ON products (description);
```
Other families: BRIN (huge time-ordered tables), GIN/GiST (PostgreSQL arrays, JSON, text).

### Example
Query `SELECT order_date, amount FROM orders WHERE customer_id = 42` with index (customer_id, order_date, amount) is **covering**: both returned columns and the filter live in the index, so no table read is needed. B-tree depth: with about 500 keys per page, 10 million rows need $\lceil \log_{500}(10^7) \rceil = \lceil 2.59 \rceil = 3$ page reads to find a key.

### In the news
See news box. PostgreSQL 18's **skip scan** loosens the leftmost-prefix rule for multicolumn B-tree indexes in some cases (when the leading column has few distinct values), but design indexes by the rule, not by hoping for skip scans.

### Interview angle
> [!question] How it is asked
> "What types of indexes do you know?" or "You have an index on (a,b). Will `WHERE b = 5` use it?"

> [!tip] Strong answer includes
> - B-tree as default and why (ranges, sorting)
> - Leftmost-prefix rule with an example
> - Covering index and the saving of a table lookup
> - Cost side: write overhead and storage, so index selectively

---

## 3. When to Index
> 🟠 Tier 2 · _Tracker hint:_ Columns in WHERE, JOIN ON, ORDER BY, GROUP BY — high cardinality columns

### Definition
Index the columns the database repeatedly uses to *find, join or sort* rows:
- `WHERE` filters, **foreign keys / `JOIN ... ON`** columns, `ORDER BY` and `GROUP BY` columns (an index can avoid a sort).
- Prefer **high cardinality / high selectivity** columns: selectivity = distinct values / total rows. A flag with 2 values (selectivity near 0) is a poor index alone; an order ID (selectivity 1) is ideal.
- In composite indexes put equality columns first, then the range column, with the most selective of the equals first.

Do **not** index: small tables, columns rarely queried, low-cardinality columns on their own, or tables with heavy writes and few reads. Every index must be updated on every `INSERT/UPDATE/DELETE` and takes disk and memory. Find unused indexes (MySQL `sys.schema_unused_indexes`, PostgreSQL `pg_stat_user_indexes`) and drop them. Index foreign keys: otherwise deleting a parent row scans the child table.

### Example
Table `shipments` (50 million rows): column `status` has 4 values (selectivity $4/50{,}000{,}000 \approx 0$), `shipment_id` has 50 million. An index on `status` returns about 12.5 million rows per value, so the optimiser will likely ignore it. A composite index (`status`, `created_at`) works for `WHERE status='DELAYED' AND created_at >= '2025-01-01'` because the date narrows the result.

### In the news
See news box. Newer planners (PostgreSQL 18 OR-condition support) make fewer indexes necessary, but the principle of indexing the access path still stands.

### Interview angle
> [!question] How it is asked
> "Which columns would you index in an orders table?" or "Why not index every column?"

> [!tip] Strong answer includes
> - WHERE, JOIN, ORDER BY, GROUP BY columns, and foreign keys
> - Selectivity/cardinality reasoning
> - Write-cost and storage trade-off
> - Validate with EXPLAIN and workload, and remove unused indexes

---

## 4. Avoid SELECT *
> 🟠 Tier 2 · _Tracker hint:_ Fetch only needed columns; reduces I/O and memory usage

### Definition
`SELECT *` returns every column, including wide ones (text, JSON, blobs) that the query never uses. Costs: more disk I/O, more memory and network transfer, **no covering-index possibility** (the engine must go back to the table), larger sort and temp-table sizes, and fragility when columns are added or reordered (an app or a view `SELECT *` breaks silently). In a join it also returns duplicate column names.

```sql
-- Bad
SELECT * FROM orders WHERE customer_id = 42;
-- Better
SELECT order_id, order_date, amount FROM orders WHERE customer_id = 42;
```
Columnar warehouses (BigQuery, Snowflake, Redshift) charge or scale by columns scanned, so `SELECT *` there is a direct cost. Exceptions: quick exploration with `LIMIT`, and `EXISTS (SELECT 1 ...)` where the select list is ignored.

### Example
A table has 40 columns averaging 1,000 bytes per row; the report needs 3 columns of about 40 bytes. For 1 million rows: `SELECT *` moves about 1 GB (1,000 bytes x 1,000,000), the narrow query about 40 MB, a 25x reduction (1,000 / 40). With a covering index the table is not read at all.

### In the news
See news box. Not tied to one headline; but PostgreSQL 18's async I/O makes reads faster, not free, so fewer columns still wins.

### Interview angle
> [!question] How it is asked
> "Why is SELECT * considered bad practice?"

> [!tip] Strong answer includes
> - I/O, memory, network cost and loss of covering indexes
> - Fragility to schema change
> - Pay-per-scan warehouses make it a billing issue
> - The acceptable exceptions (ad-hoc exploration, `EXISTS`)

---

## 5. Avoid Functions on Indexed Columns
> 🟠 Tier 2 · _Tracker hint:_ WHERE YEAR(date)=2024 prevents index use; use range instead

### Definition
A predicate is **sargable** (Search ARGument ABLE) when the engine can use an index seek on it. Wrapping the indexed column in a function, arithmetic or an implicit cast makes the engine compute the expression for every row, forcing a scan.

| Non-sargable | Sargable rewrite |
|---|---|
| `WHERE YEAR(order_date) = 2024` | `WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'` |
| `WHERE DATE(created_at) = '2025-03-01'` | `WHERE created_at >= '2025-03-01' AND created_at < '2025-03-02'` |
| `WHERE amount * 1.18 > 1000` | `WHERE amount > 1000 / 1.18` |
| `WHERE UPPER(name) = 'TATA'` | Use a case-insensitive collation, or a functional index |
| `WHERE phone = 9876543210` (phone is VARCHAR) | `WHERE phone = '9876543210'` (avoid implicit cast) |
| `WHERE name LIKE '%steel'` | Leading wildcard cannot use B-tree; use full-text or reverse index |

Use a half-open range (`>= start AND < next_start`) instead of `BETWEEN ... '2024-12-31'` to avoid missing time-of-day rows. If the function is unavoidable, create a **functional index** (MySQL 8.0.13+: `CREATE INDEX i ON t ((UPPER(name)))`; PostgreSQL: `CREATE INDEX i ON t (UPPER(name))`).

### Example
Table of 100 million orders with an index on `order_date`. `WHERE YEAR(order_date)=2024` scans all 100 million rows; the range version seeks to the first 2024 entry and reads about one year of data, say 12 million rows if volumes are even over ~8 years (100M / 8.33). That is roughly 8x fewer rows even before counting the cost of the function on every row.

### In the news
See news box. PostgreSQL 18's OR-condition index support helps with some patterns, but it does not make wrapped columns sargable.

### Interview angle
> [!question] How it is asked
> "This query on a date-indexed table is slow: `WHERE YEAR(order_date)=2024`. Fix it."

> [!tip] Strong answer includes
> - Explains sargability and why a function defeats the index
> - Rewrites as a half-open date range
> - Mentions implicit type conversion and leading-wildcard LIKE
> - Offers functional index as the fallback

---

## 6. Query Rewriting
> 🟠 Tier 2 · _Tracker hint:_ Subquery → JOIN; NOT IN → NOT EXISTS; OR → UNION ALL

### Definition
The same result can be written several ways, and the form can change the plan. Modern optimisers rewrite many cases themselves (MySQL 8 and PostgreSQL both flatten many `IN` subqueries into semi-joins), so always compare with `EXPLAIN`.

1. **Correlated subquery to JOIN** (or window function): avoid running the inner query per outer row.
2. **`NOT IN` to `NOT EXISTS` / `LEFT JOIN ... IS NULL`:** `NOT IN` returns *no rows at all* if the subquery yields any NULL (three-valued logic), and is often slower. `NOT EXISTS` handles NULLs correctly.
3. **`OR` to `UNION ALL`:** when each branch can use a different index (use `UNION ALL` only if branches cannot overlap; otherwise `UNION` removes duplicates at extra cost).
4. **`EXISTS` instead of `COUNT(*) > 0`**, and `LIMIT`/pagination by key (`WHERE id > last_id`) instead of large `OFFSET`.
5. Filter early: push `WHERE` before joins and aggregate before joining when possible.

```sql
-- Customers with no orders
SELECT c.id FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);
```

### Example
`SELECT * FROM t WHERE a = 5 OR b = 7` with separate indexes on a and b may scan the table; `SELECT ... WHERE a = 5 UNION ALL SELECT ... WHERE b = 7 AND a <> 5` uses both indexes (the `a <> 5` stops double counting; add `OR a IS NULL` handling if a can be NULL). `NOT IN` trap: `WHERE id NOT IN (1, 2, NULL)` returns 0 rows, because `id <> NULL` is unknown.

### In the news
See news box. PostgreSQL 18 now handles `OR` conditions with indexes in more cases, which narrows the benefit of manual `UNION ALL` rewrites on that engine; test instead of assuming.

### Interview angle
> [!question] How it is asked
> "Find customers who never ordered. Which query pattern and why?" or "Why did NOT IN return nothing?"

> [!tip] Strong answer includes
> - `NOT EXISTS` over `NOT IN` and the NULL explanation
> - Correlated subquery vs join and window alternatives
> - `OR` to `UNION ALL` with the duplicate caveat
> - Verification with EXPLAIN since optimisers differ

---

## 7. Partitioning
> 🟠 Tier 2 · _Tracker hint:_ Range, List, Hash partitioning — improves query performance on large tables

### Definition
**Partitioning** splits one logical table into smaller physical pieces by a **partition key**. The optimiser can skip partitions that cannot match the filter (**partition pruning**), and old data can be dropped instantly (`ALTER TABLE ... DROP PARTITION`) instead of a slow `DELETE`.

| Type | Rule | Typical use |
|---|---|---|
| **Range** | Value ranges | Orders by month or year (time series) |
| **List** | Explicit value lists | Region or country codes |
| **Hash** | `hash(key) mod N` | Even spread, avoid hot spots |
| Composite | Range then hash | Large event tables |

```sql
CREATE TABLE orders (
  order_id BIGINT, order_date DATE NOT NULL, amount DECIMAL(12,2),
  PRIMARY KEY (order_id, order_date)
) PARTITION BY RANGE (YEAR(order_date)) (
  PARTITION p2023 VALUES LESS THAN (2024),
  PARTITION p2024 VALUES LESS THAN (2025),
  PARTITION pmax  VALUES LESS THAN MAXVALUE);
```
MySQL rule: the partition key must be part of every unique key (including the primary key). Partitioning helps only when queries filter on the partition key; it is not a substitute for indexes. Do not confuse with **sharding** (splitting across servers).

### Example
Orders table has 8 yearly partitions of equal size (100M rows total, 12.5M each). `WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'` scans only partition p2024: 12.5M rows rather than 100M, an 8x cut. Purging 2016 data = dropping one partition (instant) vs deleting 12.5M rows with log and lock overhead.

### In the news
See news box. Planner improvements (PostgreSQL 18) and version upgrades (MySQL 8.0 to 8.4) change partition-pruning details, so re-verify pruning with `EXPLAIN` (MySQL: `partitions` column).

### Interview angle
> [!question] How it is asked
> "A 500-million-row orders table is slow; how would you restructure it?"

> [!tip] Strong answer includes
> - Partition by date (range) when queries are time-bound; pruning explained
> - Archival and fast drop of old partitions
> - Hash/list alternatives, and the unique-key constraint
> - Distinguish from indexing and sharding; measure before and after

---

## 8. Normalization (1NF/2NF/3NF)
> 🟠 Tier 2 · _Tracker hint:_ Remove redundancy; 3NF = no transitive dependency on non-key attributes

### Definition
**Normalisation** organises tables to remove redundancy and **update, insert and delete anomalies**.

- **1NF:** each cell holds one atomic value; no repeating groups (no "phone1, phone2" or comma lists); rows uniquely identifiable.
- **2NF:** 1NF plus no **partial dependency**: every non-key attribute depends on the *whole* composite key. (Only matters when the key is composite.)
- **3NF:** 2NF plus no **transitive dependency**: non-key attributes depend only on the key, not on other non-key attributes ("the key, the whole key, and nothing but the key").
- **BCNF:** stricter 3NF where every determinant is a candidate key.

Example violation: `Orders(order_id, product_id, product_name, customer_id, customer_city, pin_code, city)`. `product_name` depends only on `product_id` (partial, breaks 2NF if the key is (order_id, product_id)). `city` depends on `pin_code`, which depends on the key (transitive, breaks 3NF).

Fix: `Orders(order_id, customer_id, date)`, `OrderLines(order_id, product_id, qty)`, `Products(product_id, name)`, `Customers(customer_id, name, pin_code)`, `PinCodes(pin_code, city)`. Benefit: change a product name in one place. Cost: more joins.

### Example
Single table with a row per order line stores the supplier phone each time. If supplier S1 has 5,000 rows and changes phone, you must update 5,000 rows (update anomaly), and a missed row leaves inconsistent data. After normalisation, one row in `Suppliers` is updated: 5,000 updates reduced to 1.

### In the news
See news box. Version upgrades and migrations (MySQL 8.0 EOL) are far easier on a clean, normalised schema than on one with hidden redundancy.

### Interview angle
> [!question] How it is asked
> "Explain 1NF, 2NF, 3NF with an example" or "Normalise this table."

> [!tip] Strong answer includes
> - Plain definitions and the "key, whole key, nothing but the key" phrase
> - Identify the specific partial and transitive dependencies in the given table
> - Benefits (no anomalies) and cost (joins)
> - Know when to denormalise (analytics, see next section)

---

## 9. Denormalization for Analytics
> 🟠 Tier 2 · _Tracker hint:_ Star/snowflake schema; trading storage for query speed in BI

### Definition
**Denormalisation** deliberately adds redundancy to cut joins and speed up reads. OLTP systems (order entry) stay normalised for write integrity; **OLAP/BI** systems use dimensional models:

- **Star schema:** a central **fact table** (measures such as quantity, revenue, at a stated grain: one row per order line) surrounded by denormalised **dimension tables** (Date, Product, Customer, Store/Warehouse, Supplier). Few joins, simple SQL, fast aggregation.
- **Snowflake schema:** dimensions further normalised (Product to Category to Department). Less storage and redundancy but more joins.
- Other tools: summary/aggregate tables, materialised views, pre-computed columns.

Trade-offs: faster reads, simpler queries for analysts vs. more storage, harder updates, risk of inconsistency (handled by ETL, **slowly changing dimensions**: Type 1 overwrite, Type 2 add a new row with validity dates). Always declare the grain first.

### Example
Retail star schema: `fact_sales(date_key, product_key, store_key, units, revenue)` with `dim_date`, `dim_product(sku, brand, category)`, `dim_store(city, state)`. "Revenue by category by state by month" needs 3 joins from the fact table. In a fully normalised OLTP schema the same question may need 6 to 8 joins (order, line, product, brand, category, store, city, state).

### In the news
See news box. Faster scan engines (PostgreSQL 18 async I/O) reduce, but do not remove, the case for dimensional models in BI.

### Interview angle
> [!question] How it is asked
> "Design a data model for sales analytics" or "Star vs snowflake?"

> [!tip] Strong answer includes
> - OLTP (normalised) vs OLAP (denormalised) purpose
> - Fact table, grain and dimensions named for the case
> - Star vs snowflake trade-off
> - SCD handling and ETL ownership of consistency

---

## 10. Transactions & ACID
> 🟠 Tier 2 · _Tracker hint:_ Atomicity, Consistency, Isolation, Durability; COMMIT, ROLLBACK, SAVEPOINT

### Definition
A **transaction** is a unit of work that either fully happens or not at all.

- **Atomicity:** all statements succeed or all are undone (all-or-nothing).
- **Consistency:** the database moves from one valid state to another; constraints (keys, checks) hold.
- **Isolation:** concurrent transactions do not see each other's uncommitted changes (degree set by isolation level).
- **Durability:** once committed, data survives a crash (write-ahead/redo log).

```sql
START TRANSACTION;                      -- BEGIN in PostgreSQL
UPDATE stock SET qty = qty - 10 WHERE sku = 'A1' AND wh = 'MUM';
UPDATE stock SET qty = qty + 10 WHERE sku = 'A1' AND wh = 'PUN';
SAVEPOINT after_transfer;
INSERT INTO transfer_log (sku, qty) VALUES ('A1', 10);
ROLLBACK TO after_transfer;             -- undo only the log insert
COMMIT;                                 -- make the transfers permanent (ROLLBACK would undo everything)
```
InnoDB (MySQL) and PostgreSQL are ACID-compliant; MyISAM is not transactional. MySQL default is `autocommit = 1`, so each statement commits alone unless you open a transaction.

### Example
Stock transfer of 10 units Mumbai to Pune: without a transaction, a crash after the first update loses 10 units (Mumbai 90, Pune unchanged). With atomicity, the crash rolls back both: Mumbai stays at 100. Durable commit means after `COMMIT` returns, a power cut cannot undo the move.

### In the news
See news box. Upgrades (MySQL 8.0 to 8.4, PostgreSQL 18) add `RETURNING OLD/NEW` and other features, but ACID guarantees remain the baseline reason relational databases run order and inventory systems.

### Interview angle
> [!question] How it is asked
> "What is ACID? Give a banking or inventory example." or "What does ROLLBACK do?"

> [!tip] Strong answer includes
> - Each property in one line with a transfer example
> - COMMIT, ROLLBACK, SAVEPOINT behaviour
> - Autocommit awareness
> - Link to concurrency: isolation levels and the cost of locking

---

## 11. ⭐ Advanced: Composite Index Design and Reading Plans (ESR rule, selectivity, covering)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Interviewers for analytics-engineering and PM roles ask "how would you make this query fast?" A systematic method:

1. Capture the slow query and its frequency (frequency x cost decides priority).
2. `EXPLAIN ANALYZE`; note scan type, rows examined vs rows returned.
3. Design one **composite index** by the **Equality, Sort, Range** order: equality columns first, then the `ORDER BY` columns, then the range column. For `WHERE status='OPEN' AND region='W' AND created_at >= X ORDER BY priority` consider (status, region, priority, created_at) or (status, region, created_at) depending on which avoids the sort for the dominant query. (Once a range column is used, later index columns cannot be used for ordering/seeking in MySQL.)
4. Add selected columns to make it **covering** only if the query is hot; PostgreSQL `INCLUDE (col)` stores extras without sorting on them.
5. Check redundancy: an index on (a) is redundant if (a,b) exists.
6. Re-run EXPLAIN, compare latency and write overhead.

Rows examined / rows returned close to 1 means an efficient access path.

### Example
Hot query: `WHERE warehouse_id = 7 AND status = 'PENDING' ORDER BY created_at LIMIT 50` on 20 million rows. Index (warehouse_id, status, created_at): equality, equality, then sort column, so the first 50 rows are read directly in order, no filesort, about 50 index entries read vs up to 20 million scanned (400,000x fewer: 20,000,000 / 50).

### In the news
See news box. PostgreSQL 18 skip scan means a (status, created_at) index may serve queries that omit `status` when it has few distinct values, a nuance worth mentioning but not designing around.

### Interview angle
> [!question] How it is asked
> "Design the right index for this query" or "Why is my composite index not used for ORDER BY?"

> [!tip] Strong answer includes
> - Equality, then sort, then range column ordering, with reasoning
> - Leftmost-prefix and the effect of a range in the middle
> - Covering index and write-overhead trade-off
> - Evidence-based: before/after EXPLAIN and rows examined

---

## 12. ⭐ Advanced: Isolation Levels, Locking and Deadlocks
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Isolation (the I in ACID) is tunable. The SQL standard defines four levels by which anomalies they allow:

| Level | Dirty read | Non-repeatable read | Phantom read |
|---|---|---|---|
| READ UNCOMMITTED | Possible | Possible | Possible |
| READ COMMITTED | Prevented | Possible | Possible |
| REPEATABLE READ | Prevented | Prevented | Possible (largely prevented in InnoDB) |
| SERIALIZABLE | Prevented | Prevented | Prevented |

Defaults: MySQL InnoDB uses REPEATABLE READ; PostgreSQL uses READ COMMITTED. Both implement **MVCC** (multi-version concurrency control): readers see a snapshot and do not block writers. Higher isolation = more safety but more locking, retries or lower throughput.

Pessimistic locking: `SELECT ... FOR UPDATE` locks the rows you will modify (use to stop two pickers claiming the same stock). A **deadlock** arises when two transactions each wait for a lock the other holds; the engine kills one (the "victim"), and the application must retry. Prevent by accessing tables and rows in a consistent order and keeping transactions short.

### Example
Two order-allocation jobs both read `qty = 5` for SKU A1 and each sells 4: without locking, final qty becomes 1 (both write 5 - 4) instead of -3, an oversell of 3 units. `SELECT qty FROM stock WHERE sku='A1' FOR UPDATE;` makes the second job wait until the first commits, then it sees qty = 1 and rejects the sale.

### In the news
See news box. Both engines in the news box use MVCC, and PostgreSQL 18's changes are about I/O and planning, not changing these isolation semantics.

### Interview angle
> [!question] How it is asked
> "What isolation levels exist?" or "How do you prevent two users from booking the last unit?"

> [!tip] Strong answer includes
> - The four levels and anomalies each prevents
> - MVCC and engine defaults
> - `FOR UPDATE` or optimistic version check for inventory contention
> - Deadlock cause and prevention (order of access, short transactions, retry)

---

---
## 🔗 Go deeper: expansion notes
- [[181 SQL Interview Problem Bank|SQL Interview Problem Bank]]
- [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses|Data Modelling for Analytics - Star Schema, SCD & Warehouses]]
- [[183 Views, Stored Procedures, Triggers & Temporary Tables|Views, Stored Procedures, Triggers & Temporary Tables]]
