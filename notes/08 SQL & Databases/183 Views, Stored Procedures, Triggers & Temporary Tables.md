---
tags: [sql-databases, tier3]
area: SQL & Databases
topic: "Views, Stored Procedures, Triggers & Temporary Tables"
tier: Tier 3
roles: Analytics / Operations
status: complete
subtopics: 12
---
# Views, Stored Procedures, Triggers & Temporary Tables

⬅ [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses]] · [[_Index - SQL & Databases|SQL & Databases]]

> **Area:** SQL & Databases · **Priority:** 🟡 Tier 3 · **Target roles:** Analytics / Operations

## Sub-topics in this note
1. [[#1. Views]]
2. [[#2. Materialised Views]]
3. [[#3. CTE vs Temporary Table vs View vs Subquery]]
4. [[#4. Temporary Tables and Table Variables Across Engines]]
5. [[#5. Stored Procedures and Functions]]
6. [[#6. User-Defined Functions: Scalar, Table-Valued and Performance]]
7. [[#7. Triggers and Audit Logging]]
8. [[#8. Transactions, Locking and Error Handling in Procedures]]
9. [[#9. Worked Example: Inventory Issue, Receipt and Transfer Procedures]]
10. [[#10. Dynamic SQL and SQL Injection Cautions]]
11. [[#11. Security: GRANT, Views and Row-Level Security]]
12. [[#12. ⭐ Advanced: Indexed Views, Performance and Cross-Engine Differences]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): server-side SQL logic keeps getting richer, and the risks around it keep ranking high
> **PostgreSQL 18 released (25 Sep 2025).** Per the official release notes, version 18 adds **virtual generated columns** (computed on read, now the default), **`OLD` and `NEW` support in `RETURNING`** for `INSERT`, `UPDATE`, `DELETE` and `MERGE` (so one statement can return both the before and after image, which simplifies audit-style logic), temporal constraints, `uuidv7()`, an asynchronous I/O subsystem and skip-scan on multicolumn B-tree indexes. ([PostgreSQL docs](https://www.postgresql.org/docs/release/18.0/))
>
> **MySQL 8.0 reached end of life (April 2026).** The release notes say that with version 8.0.46 (released 2026-04-21) MySQL 8.0 reaches EoL and recommend moving to MySQL 8.4 LTS, so stored procedure, trigger and view code written for 8.0 should be tested on 8.4. ([MySQL release notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/))
>
> **SQL Server 2025 reached general availability (announced at Microsoft Ignite).** Microsoft's announcement lists a native vector type, native JSON and regular-expression functions among the headline features; the exact GA date was not confirmed from the page, so check Microsoft's documentation. ([Microsoft Tech Community](https://techcommunity.microsoft.com/blog/sqlserver/sql-server-2025-is-now-generally-available/4470570))
>
> **OWASP Top 10:2025 ranks Injection fifth (A05:2025)**, behind Broken Access Control (A01), Security Misconfiguration (A02), Software Supply Chain Failures (A03) and Cryptographic Failures (A04). Dynamic SQL built by string concatenation and over-broad database privileges are the database-side faces of A05 and A01. ([OWASP](https://owasp.org/Top10/2025/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Views
> 🟡 Tier 3 · _Key points:_ CREATE VIEW, abstraction and security, updatable views, WITH CHECK OPTION, security_invoker

### Definition
A **view** is a stored, named `SELECT`. It holds **no data of its own** (an ordinary view is re-evaluated every time it is queried); the optimiser expands the view definition into the calling query. Uses: hide join complexity behind one name (a "semantic layer" for analysts), expose only some columns or rows (a security layer), keep business rules (such as the definition of "low stock") in one place, and keep old queries working after a table is refactored.

Simple one-table views are **updatable**: an `INSERT`/`UPDATE`/`DELETE` on the view changes the base table. Views with `GROUP BY`, `DISTINCT`, set operators or aggregates are not automatically updatable. `WITH CHECK OPTION` rejects changes that would make a row disappear from the view. Standard ANSI SQL; syntax is almost identical in PostgreSQL, MySQL and SQL Server (`CREATE OR REPLACE VIEW` in PostgreSQL and MySQL, `CREATE OR ALTER VIEW` in SQL Server 2016 SP1+). Nested views (a view on a view on a view) hide cost and are hard to debug; keep the stack shallow. This note assumes [[056 JOINs — All Types]] and [[057 Subqueries & CTEs]].

### Example
The running schema is a small inventory database (all code in the PostgreSQL-flavoured sections of this note was executed on PostgreSQL 16).

```sql
CREATE TABLE stock (
  sku TEXT NOT NULL, warehouse TEXT NOT NULL,
  on_hand INT NOT NULL CHECK (on_hand >= 0), reorder_point INT NOT NULL, unit_cost NUMERIC(10,2) NOT NULL,
  PRIMARY KEY (sku, warehouse));
CREATE TABLE stock_movement (
  mv_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, sku TEXT NOT NULL, warehouse TEXT NOT NULL,
  qty INT NOT NULL, reason TEXT, moved_at TIMESTAMP NOT NULL DEFAULT now(), moved_by TEXT NOT NULL DEFAULT current_user);
CREATE TABLE stock_audit (
  audit_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, sku TEXT, warehouse TEXT,
  old_on_hand INT, new_on_hand INT, changed_at TIMESTAMP DEFAULT now(), changed_by TEXT DEFAULT current_user);
INSERT INTO stock VALUES
 ('SKU-A','PUNE',120,50,40.00), ('SKU-A','NASHIK',30,50,40.00),
 ('SKU-B','PUNE',15,20,150.00), ('SKU-B','NASHIK',80,20,150.00), ('SKU-C','PUNE',0,10,600.00);

-- One shared definition of "low stock"
CREATE VIEW v_low_stock AS
SELECT sku, warehouse, on_hand, reorder_point, reorder_point - on_hand AS shortfall
FROM stock WHERE on_hand <= reorder_point;

SELECT * FROM v_low_stock ORDER BY sku, warehouse;
-- SKU-A NASHIK 30 50 20 | SKU-B PUNE 15 20 5 | SKU-C PUNE 0 10 10

-- A row-restricted, updatable view that refuses out-of-scope rows
CREATE VIEW v_pune_stock AS SELECT * FROM stock WHERE warehouse = 'PUNE' WITH CHECK OPTION;
DO $t$ BEGIN
  INSERT INTO v_pune_stock VALUES ('SKU-Z','NASHIK',5,1,10.00);       -- violates the view's WHERE
EXCEPTION WHEN with_check_option_violation THEN RAISE NOTICE 'Rejected by WITH CHECK OPTION'; END $t$;
```
Everything else in this note builds on these three tables.

### In the news
See news box. PostgreSQL 18's virtual generated columns are a table-level cousin of a view column: a value computed on read rather than stored, which is exactly what a view expression does.

### Interview angle
> [!question] How it is asked
> "What is a view? Does it store data? Can you update through a view? Why use one?"

> [!tip] Strong answer includes
> - A view is a saved query, not stored data; it is expanded at query time
> - Benefits: abstraction, one definition of a metric, restricting rows or columns, backward compatibility
> - Updatable only for simple single-table views; `WITH CHECK OPTION` protects the filter
> - Cost: nested views hide complexity and can slow queries; no performance gain by itself
> - Contrasts with a materialised view (stored result) and a CTE (statement-scoped)

---
## 2. Materialised Views
> 🟡 Tier 3 · _Key points:_ stored query result, REFRESH, CONCURRENTLY needs a unique index, staleness, per-engine support

### Definition
A **materialised view** stores the **result** of its query on disk and must be refreshed to pick up changes. It trades freshness for speed, so it suits expensive aggregates that dashboards hit repeatedly (daily issue summaries, ABC tables, KPI marts). Support differs:

- **PostgreSQL:** `CREATE MATERIALIZED VIEW ... [WITH NO DATA]`, `REFRESH MATERIALIZED VIEW [CONCURRENTLY]`. A plain refresh locks readers out; `CONCURRENTLY` keeps the view readable but needs the view to be already populated and to have a **unique index** covering all rows. Indexes can be created on a materialised view.
- **Oracle:** native, with fast refresh and refresh-on-commit options.
- **SQL Server:** no `MATERIALIZED VIEW` keyword; an **indexed view** (see sub-topic 12) is the equivalent and is maintained automatically.
- **MySQL:** none. Emulate with a summary table refreshed by a scheduled `EVENT`, an `INSERT ... ON DUPLICATE KEY UPDATE`, or an ETL job.

Refreshing is a design decision: how stale may it be, who triggers the refresh (cron, scheduler, end of ETL), and does the refresh fit in the window? For analytics layers built outside the database see [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses]].

### Example
Summarise stock by SKU (units and value) once, then show that changes stay invisible until the refresh. The demo update is reversed at the end so the later numbers in this note still hold.
```sql
CREATE MATERIALIZED VIEW mv_stock_by_sku AS
SELECT sku, SUM(on_hand) AS units, SUM(on_hand * unit_cost) AS stock_value FROM stock GROUP BY sku;

CREATE UNIQUE INDEX mv_stock_by_sku_pk ON mv_stock_by_sku (sku);   -- required for CONCURRENTLY, also speeds lookups
SELECT sku, units, stock_value FROM mv_stock_by_sku ORDER BY sku;
-- SKU-A 150 6000.00 | SKU-B 95 14250.00 | SKU-C 0 0.00

UPDATE stock SET on_hand = 10 WHERE sku = 'SKU-C' AND warehouse = 'PUNE';          -- goods received
SELECT units, stock_value FROM mv_stock_by_sku WHERE sku = 'SKU-C';                -- still 0 and 0.00 (stale)
REFRESH MATERIALIZED VIEW CONCURRENTLY mv_stock_by_sku;
SELECT units, stock_value FROM mv_stock_by_sku WHERE sku = 'SKU-C';                -- now 10 and 6000.00 (10 x 600)

UPDATE stock SET on_hand = 0 WHERE sku = 'SKU-C' AND warehouse = 'PUNE';           -- undo the demo change
REFRESH MATERIALIZED VIEW mv_stock_by_sku;
```
In sub-topic 12 the same idea is applied to a daily issue summary over the movement log.

### In the news
See news box. Virtual generated columns in PostgreSQL 18 are computed on read, so they never go stale; a materialised view is the opposite design choice (stored, fast, possibly stale).

### Interview angle
> [!question] How it is asked
> "What is the difference between a view and a materialised view? When would you use each?"

> [!tip] Strong answer includes
> - View: no storage, always fresh, cost paid on each query; materialised view: stored, fast reads, stale until refreshed
> - Refresh strategy (schedule, on-demand, incremental where supported) and acceptable staleness
> - `CONCURRENTLY` plus a unique index in PostgreSQL; indexed views in SQL Server; summary tables in MySQL
> - Indexing a materialised view like a table
> - A concrete use: dashboard aggregates over a large movement table

---
## 3. CTE vs Temporary Table vs View vs Subquery
> 🟡 Tier 3 · _Key points:_ scope, persistence, indexes and statistics, materialisation, when to use which

### Definition
All four name an intermediate result; they differ in **scope, storage and optimiser behaviour**.

| Construct | Scope / lifetime | Stored? | Indexable | Best for |
|---|---|---|---|---|
| Subquery / derived table | One statement | No | No | Small inline steps |
| CTE (`WITH`) | One statement | Usually no (inlined) | No | Readable multi-step logic, recursion |
| View | Permanent object | No | No (the base tables are) | Reusable definition, security |
| Materialised view | Permanent object | Yes | Yes | Expensive repeated aggregates |
| Temporary table | Session (or transaction) | Yes | Yes, can `ANALYZE` | Large intermediate results reused several times, debugging |
| Table variable (SQL Server) | Batch or procedure | Yes (tempdb) | Limited | Small row sets |

Optimiser notes: in **PostgreSQL 12+**, a non-recursive CTE referenced once is inlined into the main query (it behaves like a subquery), and you can force behaviour with `WITH x AS MATERIALIZED (...)` or `NOT MATERIALIZED`. In **MySQL 8**, the optimiser merges or materialises CTEs and derived tables. **SQL Server** treats CTEs as inline macros (they are not materialised, so a CTE referenced twice is evaluated twice). A **temporary table** has real statistics and indexes, which is why splitting one monster query into temp-table steps can be faster; the cost is extra writes. See also [[057 Subqueries & CTEs]] and [[060 Query Optimization & Indexing]].

### Example
Inventory exposure by SKU, written first with a CTE and then with a temp table when the intermediate result is reused:
```sql
-- CTE: readable, one statement
WITH value_by_sku AS (
  SELECT sku, SUM(on_hand * unit_cost) AS stock_value FROM stock GROUP BY sku)
SELECT sku, stock_value FROM value_by_sku WHERE stock_value > 5000 ORDER BY sku;
-- SKU-A 6000 | SKU-B 14250

-- Force PostgreSQL to compute the CTE once (useful if it is expensive and referenced twice)
WITH value_by_sku AS MATERIALIZED (
  SELECT sku, SUM(on_hand * unit_cost) AS stock_value FROM stock GROUP BY sku)
SELECT sku, stock_value, ROUND(100.0 * stock_value / SUM(stock_value) OVER (), 1) AS pct FROM value_by_sku ORDER BY sku;

-- Temp table: lives for the transaction here, can be indexed and analysed, then vanishes at COMMIT
BEGIN;
CREATE TEMP TABLE tmp_value ON COMMIT DROP AS
  SELECT sku, SUM(on_hand * unit_cost) AS stock_value FROM stock GROUP BY sku;
CREATE INDEX ON tmp_value (stock_value);
ANALYZE tmp_value;
SELECT sku FROM tmp_value WHERE stock_value > 5000 ORDER BY sku;   -- SKU-A, SKU-B
COMMIT;
```
Check: SKU-A is (120 + 30) x 40 = 6,000; SKU-B is (15 + 80) x 150 = 14,250; SKU-C has no stock, so its value is 0.

### In the news
See news box. PostgreSQL 18 and MySQL 8.4 both keep the CTE behaviours described here, but MySQL 8.0 code relying on 8.0 optimiser quirks should be re-tested after the April 2026 end of life.

### Interview angle
> [!question] How it is asked
> "CTE vs temp table vs view: what is the difference and when do you use each?"

> [!tip] Strong answer includes
> - Scope and persistence: statement vs session vs permanent
> - A CTE is a readability tool and is not automatically materialised; a temp table is physically stored and can be indexed
> - Engine specifics: PostgreSQL 12 inlining and `MATERIALIZED` hint; SQL Server CTEs re-evaluated per reference
> - Chooses a temp table for large reused intermediates or when statistics matter
> - Mentions that none of these is "faster by default"; check `EXPLAIN`

---
## 4. Temporary Tables and Table Variables Across Engines
> 🟡 Tier 3 · _Key points:_ session scope, ON COMMIT, #temp and @table in SQL Server, cleanup, concurrency

### Definition
A **temporary table** is a real table visible only to its creating session (or connection) and dropped automatically at the end of the session or, if specified, of the transaction. Different sessions can use the same temp-table name without clashing, which makes them safe for ETL steps and report staging. Typical uses: staging bulk loads, breaking up complex queries, holding keys for a join, and intermediate results in a stored procedure.

Per engine:
- **PostgreSQL:** `CREATE TEMP TABLE t (...)` or `CREATE TEMP TABLE t AS SELECT ...`; `ON COMMIT PRESERVE ROWS` (default), `DELETE ROWS` or `DROP`. Stored in the session's temporary schema.
- **MySQL:** `CREATE TEMPORARY TABLE t ...`; dropped at session end; cannot be referenced twice in the same query (a long-standing restriction).
- **SQL Server:** `#local` (session) and `##global` temp tables live in `tempdb`; `@table_variable` is scoped to the batch or procedure, has no statistics (cardinality estimate is low on older compatibility levels), and is not affected by rollback of the surrounding transaction.

Pitfalls: heavy temp-table use inside a high-concurrency transactional system can bloat `tempdb` or temp files; forgetting to index a large temp table; and relying on a temp table that a connection pool may hand to a different session.

### Example
Stage the SKUs to reorder, enrich them, and read them back. The temp table disappears at the end of the session.
```sql
CREATE TEMP TABLE tmp_reorder AS
SELECT sku, warehouse, reorder_point - on_hand AS shortfall FROM stock WHERE on_hand <= reorder_point;

ALTER TABLE tmp_reorder ADD COLUMN est_cost NUMERIC(12,2);
UPDATE tmp_reorder r SET est_cost = r.shortfall * s.unit_cost
FROM stock s WHERE s.sku = r.sku AND s.warehouse = r.warehouse;

SELECT sku, warehouse, shortfall, est_cost FROM tmp_reorder ORDER BY sku, warehouse;
-- SKU-A NASHIK 20 800.00 | SKU-B PUNE 5 750.00 | SKU-C PUNE 10 6000.00
DROP TABLE tmp_reorder;
```
The estimated replenishment spend is 800 + 750 + 6,000 = 7,550 in cost units (for example rupees).

### In the news
See news box. Temp tables and table variables are one of the first places SQL Server and PostgreSQL differ; with SQL Server 2025 now generally available, check the documentation of your target version for tempdb behaviours rather than relying on older advice.

### Interview angle
> [!question] How it is asked
> "What is a temporary table? Difference between #temp and @table variable? When would you use one in a stored procedure?"

> [!tip] Strong answer includes
> - Session-scoped real table; auto-dropped; isolated per session
> - SQL Server: `#temp` has statistics and indexes, `@table` variable is lighter but with weaker estimates
> - Uses a temp table to stage, index and reuse a large intermediate result
> - Cleans up explicitly or with `ON COMMIT DROP`
> - Mentions MySQL's single-reference limitation

---
## 5. Stored Procedures and Functions
> 🟡 Tier 3 · _Key points:_ parameters (IN/OUT), CALL vs SELECT, procedure vs function, benefits and drawbacks

### Definition
A **stored procedure** is a named block of SQL and procedural code stored in the database and run with `CALL` (or `EXEC` in SQL Server). It can take input and output parameters, run several statements, and (in most engines) control transactions. A **function** returns a value (scalar) or a row set (table-valued) and is used inside queries.

| Aspect | Procedure | Function |
|---|---|---|
| Invoked by | `CALL` / `EXEC` | Inside `SELECT`, `WHERE`, `JOIN` |
| Returns | Nothing, OUT parameters or result sets | A value or table |
| Side effects | Typically allowed (DML, DDL) | Restricted in some engines (SQL Server forbids data modification in scalar functions) |
| Transaction control | Allowed (PostgreSQL 11+ `COMMIT`/`ROLLBACK`, MySQL, SQL Server) | Not allowed in PostgreSQL functions |

Benefits: logic close to the data (fewer round trips), one tested implementation shared by all applications, parameterised and plan-cached execution, permission control (grant `EXECUTE` without table access). Drawbacks: business logic hidden in the database, harder version control and testing, vendor lock-in (PL/pgSQL, T-SQL and MySQL's procedural SQL differ), and debugging difficulty. Modern teams keep the database layer thin and put most logic in application code or transformation tools, using procedures for atomic data operations.

### Example
A table-returning function (reusable inside queries) and a scalar function:
```sql
CREATE FUNCTION fn_stock_value(p_sku TEXT) RETURNS NUMERIC LANGUAGE sql STABLE AS $fn$
  SELECT COALESCE(SUM(on_hand * unit_cost), 0) FROM stock WHERE sku = p_sku
$fn$;
SELECT fn_stock_value('SKU-A') AS value_a;         -- (120 + 30) x 40 = 6000

CREATE FUNCTION fn_below_reorder(p_warehouse TEXT)
RETURNS TABLE (sku TEXT, on_hand INT, reorder_point INT) LANGUAGE sql STABLE AS $fn$
  SELECT s.sku, s.on_hand, s.reorder_point FROM stock s
  WHERE s.warehouse = p_warehouse AND s.on_hand <= s.reorder_point
$fn$;
SELECT * FROM fn_below_reorder('PUNE') ORDER BY sku;   -- SKU-B 15 20 | SKU-C 0 10
```
Procedures with parameters appear in sub-topic 9. The three-engine equivalents of a procedure header are:
```mysql
-- MySQL 8 (client command DELIMITER is needed in the mysql shell)
DELIMITER //
CREATE PROCEDURE sp_issue_stock(IN p_sku VARCHAR(30), IN p_wh VARCHAR(20), IN p_qty INT) BEGIN ... END //
DELIMITER ;
CALL sp_issue_stock('SKU-A', 'PUNE', 20);
```
```tsql
-- SQL Server
CREATE OR ALTER PROCEDURE dbo.sp_issue_stock @sku NVARCHAR(30), @wh NVARCHAR(20), @qty INT AS BEGIN ... END;
EXEC dbo.sp_issue_stock @sku = N'SKU-A', @wh = N'PUNE', @qty = 20;
```
(The MySQL and SQL Server snippets are syntax reference, not executed here; the PostgreSQL code in this note was run on PostgreSQL 16.)

### In the news
See news box. PostgreSQL's `CALL` and in-procedure transaction control date from version 11; PostgreSQL 18 adds `OLD`/`NEW` in `RETURNING`, which lets a procedure return before and after values from one `UPDATE`.

### Interview angle
> [!question] How it is asked
> "Difference between a stored procedure and a function? Advantages and disadvantages of stored procedures?"

> [!tip] Strong answer includes
> - Function returns a value and is usable in queries; procedure performs actions, is called with `CALL`/`EXEC`, and can control transactions
> - IN, OUT and INOUT parameters; default values
> - Advantages: atomic multi-step operations, fewer round trips, security via `EXECUTE` grants
> - Drawbacks: hidden logic, lock-in, testing and version control
> - Mentions keeping DDL for procedures in source control and migrations

---
## 6. User-Defined Functions: Scalar, Table-Valued and Performance
> 🟡 Tier 3 · _Key points:_ volatility, inlining, scalar UDF cost, set-based thinking, determinism

### Definition
A **user-defined function (UDF)** packages reusable logic. Kinds: **scalar** (one value), **table-valued** (a set of rows, inline or multi-statement), and **aggregate** (custom aggregates). Performance rule: the optimiser reasons well about **set-based** SQL, but treats a procedural scalar function as a black box called **once per row**. Consequences: a scalar UDF in a `WHERE` or `SELECT` over millions of rows can be orders of magnitude slower than the equivalent expression; it may block parallelism; and it hides cost from `EXPLAIN`.

Mitigations: prefer **inline** table-valued functions (SQL Server) or `LANGUAGE sql` functions that the planner can inline (PostgreSQL); mark volatility correctly in PostgreSQL (`IMMUTABLE` for pure functions, `STABLE` for read-only within a statement, `VOLATILE` default) because the planner can cache and index on `IMMUTABLE` results; in MySQL declare `DETERMINISTIC` only when true. SQL Server 2019 added scalar UDF inlining for many functions, which narrows the gap but does not remove it. For analytics, a view or a derived expression is usually simpler and faster than a UDF.

### Example
Same logic as a function and as an inline expression. The inline version is what the planner can optimise:
```sql
CREATE FUNCTION fn_margin_pct(p_cost NUMERIC, p_price NUMERIC) RETURNS NUMERIC
LANGUAGE sql IMMUTABLE AS $fn$
  SELECT CASE WHEN p_price = 0 THEN NULL ELSE ROUND(100.0 * (p_price - p_cost) / p_price, 1) END
$fn$;

SELECT fn_margin_pct(150, 250) AS margin_pct;                -- (250 - 150) / 250 = 40.0
SELECT ROUND(100.0 * (250 - 150) / 250, 1) AS margin_inline;  -- 40.0, same result written inline
```
Because the function is `LANGUAGE sql` and `IMMUTABLE`, PostgreSQL can inline it into the calling query, so you keep reuse without the per-row call overhead. A `LANGUAGE plpgsql` version would not be inlined.

### In the news
See news box. Functions keep gaining vendor-specific powers (SQL Server 2025 regex and JSON functions, PostgreSQL 18 `uuidv7()`), but the performance guidance (set-based, inlinable, correct volatility) is stable across versions.

### Interview angle
> [!question] How it is asked
> "Why can a scalar UDF be slow? How would you speed up a query that calls one?"

> [!tip] Strong answer includes
> - Row-by-row invocation and an opaque optimiser estimate
> - Fixes: inline the logic, use inline table-valued functions or a join, or rewrite as set-based SQL
> - Correct volatility or determinism markers
> - Awareness of SQL Server 2019 scalar UDF inlining and its limits
> - Prefers views or expressions when no procedural logic is needed

---
## 7. Triggers and Audit Logging
> 🟡 Tier 3 · _Key points:_ BEFORE/AFTER, row vs statement, OLD/NEW, inserted/deleted, audit trail, pitfalls

### Definition
A **trigger** runs automatically when a table is modified. Components: **event** (`INSERT`, `UPDATE`, `DELETE`), **timing** (`BEFORE`, `AFTER`, `INSTEAD OF` for views) and **level** (per row or per statement). Inside a row trigger, `OLD` and `NEW` hold the before and after images (PostgreSQL, MySQL, Oracle); SQL Server triggers are statement-level and expose the pseudo-tables `inserted` and `deleted`. Typical uses: **audit logging**, enforcing rules that a `CHECK` constraint cannot express, maintaining denormalised totals, and populating history tables.

Pitfalls: triggers are invisible to developers reading application code; they add cost to every write; chains of triggers (one firing another) become hard to reason about and can recurse; they can fail the user's transaction; bulk loads may fire them millions of times; and they should never contain business logic that can be expressed with a constraint. Prefer constraints and explicit procedures; use triggers for audit and integrity safety nets.

### Example
Audit every change to `stock.on_hand` (old value, new value, user, time) in PostgreSQL. The trigger fires only when the quantity actually changes:
```sql
CREATE FUNCTION trg_stock_audit() RETURNS trigger LANGUAGE plpgsql AS $fn$
BEGIN
  IF NEW.on_hand IS DISTINCT FROM OLD.on_hand THEN
    INSERT INTO stock_audit (sku, warehouse, old_on_hand, new_on_hand)
    VALUES (OLD.sku, OLD.warehouse, OLD.on_hand, NEW.on_hand);
  END IF;
  RETURN NEW;
END $fn$;

CREATE TRIGGER stock_audit_trg
AFTER UPDATE OF on_hand ON stock
FOR EACH ROW EXECUTE FUNCTION trg_stock_audit();
```
After the procedure scenarios of sub-topic 9 (run in order), `stock_audit` holds one row per quantity change, for example `SKU-A | PUNE | 120 | 100` after issuing 20 units. The equivalents elsewhere are:
```mysql
-- MySQL: row-level AFTER UPDATE trigger; <=> is the NULL-safe equality operator
CREATE TRIGGER stock_audit_trg AFTER UPDATE ON stock FOR EACH ROW
BEGIN
  IF NOT (NEW.on_hand <=> OLD.on_hand) THEN
    INSERT INTO stock_audit (sku, warehouse, old_on_hand, new_on_hand) VALUES (OLD.sku, OLD.warehouse, OLD.on_hand, NEW.on_hand);
  END IF;
END;
```
```tsql
-- SQL Server: statement-level, set-based, uses the inserted/deleted pseudo-tables
CREATE TRIGGER dbo.trg_stock_audit ON dbo.stock AFTER UPDATE AS
BEGIN
  SET NOCOUNT ON;
  INSERT dbo.stock_audit (sku, warehouse, old_on_hand, new_on_hand)
  SELECT d.sku, d.warehouse, d.on_hand, i.on_hand
  FROM deleted d JOIN inserted i ON i.sku = d.sku AND i.warehouse = d.warehouse
  WHERE d.on_hand <> i.on_hand;
END;
```
(MySQL and SQL Server snippets are syntax reference and were not executed here.) A SQL Server trigger must handle **multi-row** statements; writing it as if only one row changed is the classic bug.

### In the news
See news box. PostgreSQL 18's `OLD`/`NEW` in `RETURNING` lets an application capture before and after values without a trigger, a lighter alternative for some audit needs; MySQL 8.4 and SQL Server 2025 triggers behave as before.

### Interview angle
> [!question] How it is asked
> "What is a trigger? Write one that logs changes to a table. What are the drawbacks?"

> [!tip] Strong answer includes
> - Event, timing and level explained with a concrete audit example
> - `OLD`/`NEW` (PostgreSQL, MySQL) or `inserted`/`deleted` (SQL Server) and why SQL Server needs set-based code
> - Fires only on real change (`IS DISTINCT FROM`) to avoid noise
> - Drawbacks: hidden logic, write overhead, cascading and recursion, bulk-load cost
> - Alternatives: constraints, procedures, temporal tables or change-data-capture for heavy audit needs

---
## 8. Transactions, Locking and Error Handling in Procedures
> 🟡 Tier 3 · _Key points:_ ACID, atomic multi-step update, FOR UPDATE, savepoints and exception blocks, TRY/CATCH, COMMIT in procedures

### Definition
A **transaction** groups statements into one all-or-nothing unit (**ACID**: atomicity, consistency, isolation, durability). In a stored procedure the usual pattern is: validate inputs, lock the rows you will change, perform the changes, write the log row, and let any error roll the whole unit back.

- **Locking:** `SELECT ... FOR UPDATE` locks the selected rows until the transaction ends, so two sessions cannot both read "10 in stock" and both issue 8 units. SQL Server uses `WITH (UPDLOCK, ROWLOCK)` hints.
- **Isolation level:** the default is `READ COMMITTED` in PostgreSQL and SQL Server and `REPEATABLE READ` in MySQL InnoDB; stricter levels cost concurrency.
- **Error handling:** PostgreSQL PL/pgSQL uses `BEGIN ... EXCEPTION WHEN ... THEN ...`, and a block with an `EXCEPTION` clause behaves like a **savepoint** (its changes are rolled back if the handler runs). MySQL uses `DECLARE ... HANDLER` with `SIGNAL`/`RESIGNAL`. SQL Server uses `BEGIN TRY ... END TRY BEGIN CATCH ... END CATCH`, `THROW`, and `SET XACT_ABORT ON`.
- **Transaction control inside procedures:** a PostgreSQL procedure called with `CALL` from the top level may `COMMIT` and `ROLLBACK` itself (version 11+); functions cannot. This enables batch jobs that commit in chunks.
- **Deadlocks:** two sessions locking the same rows in different order. Fix by locking in a consistent order and keeping transactions short; the database aborts one victim, so callers should retry.

### Example
A wrapper that attempts an issue and, on failure, rolls back the issue but still records the failure. The `EXCEPTION` block rolls back everything done inside the block; the log insert in the handler survives:
```sql
CREATE TABLE issue_error_log (
  log_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, sku TEXT, warehouse TEXT, qty INT,
  error_message TEXT, logged_at TIMESTAMP DEFAULT now());

CREATE PROCEDURE sp_issue_or_log(p_sku TEXT, p_wh TEXT, p_qty INT)
LANGUAGE plpgsql AS $fn$
BEGIN
  CALL sp_issue_stock(p_sku, p_wh, p_qty, 'SALE');
EXCEPTION WHEN OTHERS THEN
  INSERT INTO issue_error_log (sku, warehouse, qty, error_message) VALUES (p_sku, p_wh, p_qty, SQLERRM);
END $fn$;
```
(`sp_issue_stock` is defined in sub-topic 9, so call this wrapper after that sub-topic.) For `SKU-C` in Pune there is no stock to issue, so nothing changes in `stock`, and `issue_error_log` receives the message "Insufficient stock for SKU-C/PUNE: have 0, need 3" (the call is part of the test scenario in sub-topic 9).

A batch job that commits per warehouse, so a failure at the third warehouse keeps the first two:
```sql
CREATE TABLE stock_snapshot_daily (snap_date DATE, warehouse TEXT, sku_count INT, units BIGINT, value NUMERIC(14,2));

CREATE PROCEDURE sp_close_day(p_date DATE) LANGUAGE plpgsql AS $fn$
DECLARE r RECORD;
BEGIN
  FOR r IN SELECT DISTINCT warehouse FROM stock ORDER BY warehouse LOOP
    INSERT INTO stock_snapshot_daily
    SELECT p_date, r.warehouse, COUNT(*), SUM(on_hand), SUM(on_hand * unit_cost) FROM stock WHERE warehouse = r.warehouse;
    COMMIT;                                   -- allowed in a procedure called from the top level
  END LOOP;
END $fn$;

CALL sp_close_day(DATE '2025-03-31');
SELECT warehouse, sku_count, units, value FROM stock_snapshot_daily ORDER BY warehouse;
-- NASHIK 2 110 13200.00 | PUNE 3 135 7050.00     (NASHIK: 30 + 80 units; 30 x 40 + 80 x 150. PUNE: 120 + 15 + 0 units)
```

### In the news
See news box. MySQL 8.4 keeps InnoDB's `REPEATABLE READ` default and handler-based error handling; PostgreSQL 18 changes none of these semantics, so transaction patterns learned today remain valid.

### Interview angle
> [!question] How it is asked
> "How do you make a multi-step stock update safe under concurrency? How do you handle errors in a stored procedure?"

> [!tip] Strong answer includes
> - Atomic unit (all steps commit or none), with the ACID properties named
> - Row lock (`FOR UPDATE` or `UPDLOCK`) before reading a balance that will be changed
> - Engine-appropriate error handling: `EXCEPTION`, `HANDLER`, `TRY/CATCH` with a re-raise so callers see the failure
> - Keeps transactions short and orders lock acquisition consistently to avoid deadlocks
> - Mentions retry on deadlock or serialisation failure

---
## 9. Worked Example: Inventory Issue, Receipt and Transfer Procedures
> 🟡 Tier 3 · _Key points:_ validation, lock, update, movement log, trigger audit, atomic transfer, test scenarios

### Definition
Goal: a safe way to **issue** stock (sale or production consumption), **receive** stock, and **transfer** between warehouses so that (1) on-hand never goes negative, (2) every change is logged in `stock_movement`, (3) the audit trigger records the before/after quantity, and (4) a failed transfer leaves both warehouses unchanged. Design rules: validate parameters first; lock the row with `FOR UPDATE`; check the business rule; update; log; raise a clear error message otherwise. The transfer procedure simply calls issue and receive, so both run in the caller's single transaction. Inventory concepts (balance, reorder point, safety stock) are in [[003 Inventory Management]]; SAP's equivalent goods-movement logic is in [[080 SAP MM — Materials Management]].

### Example
```sql
CREATE PROCEDURE sp_issue_stock(p_sku TEXT, p_wh TEXT, p_qty INT, p_reason TEXT DEFAULT 'SALE')
LANGUAGE plpgsql AS $fn$
DECLARE v_on_hand INT;
BEGIN
  IF p_qty IS NULL OR p_qty <= 0 THEN
    RAISE EXCEPTION 'Quantity must be positive, got %', p_qty USING ERRCODE = '22023';
  END IF;
  SELECT on_hand INTO v_on_hand FROM stock WHERE sku = p_sku AND warehouse = p_wh FOR UPDATE;   -- row lock
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Unknown SKU/warehouse: %/%', p_sku, p_wh;
  END IF;
  IF v_on_hand < p_qty THEN
    RAISE EXCEPTION 'Insufficient stock for %/%: have %, need %', p_sku, p_wh, v_on_hand, p_qty;
  END IF;
  UPDATE stock SET on_hand = on_hand - p_qty WHERE sku = p_sku AND warehouse = p_wh;            -- audit trigger fires here
  INSERT INTO stock_movement (sku, warehouse, qty, reason) VALUES (p_sku, p_wh, -p_qty, p_reason);
END $fn$;

CREATE PROCEDURE sp_receive_stock(p_sku TEXT, p_wh TEXT, p_qty INT, p_reason TEXT DEFAULT 'PO_RECEIPT')
LANGUAGE plpgsql AS $fn$
BEGIN
  IF p_qty IS NULL OR p_qty <= 0 THEN
    RAISE EXCEPTION 'Quantity must be positive, got %', p_qty USING ERRCODE = '22023';
  END IF;
  UPDATE stock SET on_hand = on_hand + p_qty WHERE sku = p_sku AND warehouse = p_wh;
  IF NOT FOUND THEN
    RAISE EXCEPTION 'Unknown SKU/warehouse: %/%', p_sku, p_wh;
  END IF;
  INSERT INTO stock_movement (sku, warehouse, qty, reason) VALUES (p_sku, p_wh, p_qty, p_reason);
END $fn$;

CREATE PROCEDURE sp_transfer_stock(p_sku TEXT, p_from TEXT, p_to TEXT, p_qty INT) LANGUAGE plpgsql AS $fn$
BEGIN
  CALL sp_issue_stock(p_sku, p_from, p_qty, 'TRANSFER_OUT');
  CALL sp_receive_stock(p_sku, p_to, p_qty, 'TRANSFER_IN');
END $fn$;
```
Test scenario with expected results (starting stock: SKU-A PUNE 120, SKU-B PUNE 15, SKU-B NASHIK 80):
```sql
CALL sp_issue_stock('SKU-A', 'PUNE', 20, 'SALE');                       -- SKU-A PUNE 120 -> 100
DO $t$ BEGIN CALL sp_issue_stock('SKU-B', 'PUNE', 25);                  -- only 15 on hand
EXCEPTION WHEN OTHERS THEN RAISE NOTICE 'Rejected: %', SQLERRM; END $t$; -- Insufficient stock for SKU-B/PUNE: have 15, need 25
CALL sp_transfer_stock('SKU-B', 'NASHIK', 'PUNE', 40);                  -- NASHIK 80 -> 40, PUNE 15 -> 55
DO $t$ BEGIN CALL sp_transfer_stock('SKU-B', 'NASHIK', 'PUNE', 500);    -- fails at the issue step
EXCEPTION WHEN OTHERS THEN RAISE NOTICE 'Transfer rejected: %', SQLERRM; END $t$;

CALL sp_issue_or_log('SKU-C', 'PUNE', 3);                               -- nothing to issue: the error is logged, not raised
SELECT error_message FROM issue_error_log;                              -- Insufficient stock for SKU-C/PUNE: have 0, need 3

SELECT sku, warehouse, on_hand FROM stock ORDER BY sku, warehouse;
-- SKU-A NASHIK 30 | SKU-A PUNE 100 | SKU-B NASHIK 40 | SKU-B PUNE 55 | SKU-C PUNE 0
SELECT sku, warehouse, qty, reason FROM stock_movement ORDER BY mv_id;
-- SKU-A PUNE -20 SALE | SKU-B NASHIK -40 TRANSFER_OUT | SKU-B PUNE 40 TRANSFER_IN
SELECT sku, warehouse, old_on_hand, new_on_hand FROM stock_audit ORDER BY audit_id;
-- SKU-A PUNE 120->100 | SKU-B NASHIK 80->40 | SKU-B PUNE 15->55
```
Three facts to verify by hand: total SKU-B stock is 95 before and after the transfer (40 + 55); the failed 500-unit transfer wrote nothing to `stock_movement` or `stock_audit`; and the `CHECK (on_hand >= 0)` constraint is a second line of defence if someone updates the table directly.

Why `FOR UPDATE`: without it, two concurrent sessions could both read 15 and both issue 10, leaving a wrong balance (or a constraint failure). The lock makes the second session wait, then re-read the updated quantity. The SQL Server equivalent uses `BEGIN TRY ... BEGIN TRAN ... WITH (UPDLOCK, ROWLOCK) ... COMMIT ... END TRY BEGIN CATCH IF @@TRANCOUNT > 0 ROLLBACK; THROW; END CATCH` with `SET XACT_ABORT ON`. In MySQL use `START TRANSACTION`, `SELECT ... FOR UPDATE`, a `DECLARE EXIT HANDLER FOR SQLEXCEPTION` that does `ROLLBACK; RESIGNAL;`, and `SIGNAL SQLSTATE '45000'` to raise business errors.

### In the news
See news box. PostgreSQL 18's `RETURNING OLD, NEW` could let `sp_issue_stock` return the before and after balances from a single `UPDATE` instead of relying on the audit trigger alone.

### Interview angle
> [!question] How it is asked
> "Write a stored procedure that issues stock and prevents negative inventory." / "How do you make a warehouse-to-warehouse transfer atomic?"

> [!tip] Strong answer includes
> - Validates parameters, locks the row, checks the rule, updates, logs, raises a specific error
> - Explains why the lock is needed (lost-update race) and why a `CHECK` constraint is still valuable
> - Builds transfer from two calls inside one transaction so failure undoes both
> - Mentions the audit trail (trigger or movement table) and idempotency or retry handling
> - Gives the SQL Server or MySQL equivalent constructs on request

---
## 10. Dynamic SQL and SQL Injection Cautions
> 🟡 Tier 3 · _Key points:_ EXECUTE format, quoting identifiers and literals, bind parameters, sp_executesql, least privilege

### Definition
**Dynamic SQL** builds and runs a statement from a string at run time (`EXECUTE` in PostgreSQL, `PREPARE`/`EXECUTE` in MySQL, `sp_executesql` or `EXEC (@sql)` in SQL Server). It is needed when table or column names, or the number of pivot columns, are not known in advance. The danger is **SQL injection**: concatenating user-supplied text into the string lets the attacker change the statement's meaning (injection ranks fifth in the OWASP Top 10:2025).

Rules: (1) **values** go through bind parameters (`EXECUTE ... USING`, `sp_executesql` with parameter list, MySQL `?` placeholders), never concatenation; (2) **identifiers** (table or column names) cannot be bound, so quote them with the engine's quoting function (`format('%I', ...)` or `quote_ident` in PostgreSQL, `QUOTENAME` in SQL Server) or validate against an allow-list from the catalog; (3) run the code with the **least privilege** needed; (4) log executed statements for debugging; (5) prefer static SQL whenever possible, since dynamic SQL defeats compile-time checks and may prevent plan reuse.

### Example
A safe row-count function: the table name is quoted as an identifier, the filter value is bound as a parameter.
```sql
CREATE FUNCTION fn_count_rows(p_table TEXT, p_wh TEXT DEFAULT NULL) RETURNS BIGINT LANGUAGE plpgsql AS $fn$
DECLARE n BIGINT;
BEGIN
  IF p_wh IS NULL THEN
    EXECUTE format('SELECT count(*) FROM %I', p_table) INTO n;
  ELSE
    EXECUTE format('SELECT count(*) FROM %I WHERE warehouse = $1', p_table) INTO n USING p_wh;
  END IF;
  RETURN n;
END $fn$;

SELECT fn_count_rows('stock') AS all_rows, fn_count_rows('stock', 'PUNE') AS pune_rows;   -- 5 | 3

-- Injection attempt: %I turns the whole string into one (non-existent) identifier, so nothing is dropped
DO $t$ BEGIN PERFORM fn_count_rows('stock; DROP TABLE stock');
EXCEPTION WHEN undefined_table THEN RAISE NOTICE 'Injection attempt failed safely'; END $t$;
```
The unsafe version, `EXECUTE 'SELECT count(*) FROM ' || p_table`, would run the attacker's `DROP TABLE` if the role had the right to drop it. SQL Server equivalent: `SET @sql = N'SELECT COUNT(*) FROM ' + QUOTENAME(@tbl); EXEC sp_executesql @sql;`, with values passed through `@params` rather than concatenated.

### In the news
See news box. OWASP Top 10:2025 places Injection fifth and Broken Access Control first; least-privilege grants (sub-topic 11) limit the damage of any injection that does slip through.

### Interview angle
> [!question] How it is asked
> "What is dynamic SQL? What are the risks and how do you mitigate them?"

> [!tip] Strong answer includes
> - Use cases: variable table or column names, dynamic pivots, generic admin procedures
> - Injection explained with an example and parameter binding for values
> - Identifier quoting (`%I`, `QUOTENAME`) or allow-listing for names
> - Least privilege for the executing role; avoid dynamic SQL when static will do
> - Notes the plan-cache and testing drawbacks

---
## 11. Security: GRANT, Views and Row-Level Security
> 🟡 Tier 3 · _Key points:_ GRANT/REVOKE, roles, views as column filters, security_invoker, row-level security policies, least privilege

### Definition
Database security follows **least privilege**: give each role only what it needs. `GRANT SELECT, INSERT ON t TO role` adds a privilege, `REVOKE` removes it; **roles** (groups) simplify management. Techniques:

- **Views and procedures as gatekeepers:** grant access to a view or `EXECUTE` on a procedure instead of the underlying table. In PostgreSQL a view runs with the **view owner's** rights by default; since PostgreSQL 15 `WITH (security_invoker = true)` makes it use the caller's rights. SQL Server uses ownership chaining; MySQL has `SQL SECURITY DEFINER | INVOKER` on views and routines.
- **Row-level security (RLS):** the engine adds a predicate to every query by role. PostgreSQL: `ALTER TABLE ... ENABLE ROW LEVEL SECURITY` plus `CREATE POLICY ... USING (...)`; table owners and superusers bypass it unless `FORCE ROW LEVEL SECURITY`. SQL Server has security policies with predicate functions. MySQL has no native RLS (use views filtered by `CURRENT_USER()`).
- **Column-level control:** `GRANT SELECT (col1, col2) ON t TO role`, or a view that omits sensitive columns.
- **`SECURITY DEFINER` routines** run with the owner's rights; set a safe `search_path` and keep them tiny, since a vulnerable one is a privilege-escalation route.
- Governance context: [[175 Data Quality, Master Data & Data Governance]] and India's personal-data law, whose rules were notified in November 2025 with an 18-month phased compliance period ([[180 Current Affairs & Economy Briefing for MBA Interviews (2025-26)]]), push teams towards demonstrable access control.

### Example
An analyst role that can read the low-stock view but not the base table, and a warehouse manager who sees only Pune rows:
```sql
CREATE ROLE analyst NOLOGIN;
GRANT SELECT ON v_low_stock TO analyst;                  -- view only, no access to table stock
SET ROLE analyst;
SELECT COUNT(*) AS low_rows FROM v_low_stock;            -- works (the view runs with its owner's rights): 2
DO $t$ BEGIN PERFORM COUNT(*) FROM stock;
EXCEPTION WHEN insufficient_privilege THEN RAISE NOTICE 'analyst cannot read the base table'; END $t$;
RESET ROLE;

CREATE ROLE wh_pune_mgr NOLOGIN;
GRANT SELECT ON stock TO wh_pune_mgr;
ALTER TABLE stock ENABLE ROW LEVEL SECURITY;
CREATE POLICY pune_only ON stock FOR SELECT TO wh_pune_mgr USING (warehouse = 'PUNE');

SET ROLE wh_pune_mgr;
SELECT sku, warehouse, on_hand FROM stock ORDER BY sku;   -- only PUNE rows: SKU-A, SKU-B, SKU-C
RESET ROLE;
SELECT COUNT(*) FROM stock;                               -- owner still sees all 5 rows (owners bypass RLS)
```
After the sub-topic 9 scenario only SKU-A in Nashik (30 against a reorder point of 50) and SKU-C in Pune (0 against 10) are low, so the view returns 2 rows; with the starting data it returned 3.

### In the news
See news box. OWASP lists Broken Access Control as the number one web-application risk in 2025; database-level least privilege and row-level policies are the data-tier answer.

### Interview angle
> [!question] How it is asked
> "How would you let a regional manager see only their region's data? How do GRANT and views help secure a database?"

> [!tip] Strong answer includes
> - Least privilege with roles; grant on views or procedures, not base tables
> - Row-level security policy (PostgreSQL, SQL Server) or filtered views (MySQL)
> - Distinguishes definer vs invoker rights and the `SECURITY DEFINER` risk
> - Mentions column-level grants and masking for sensitive fields
> - Links to auditing (triggers, logs) and data-protection law obligations

---
## 12. ⭐ Advanced: Indexed Views, Performance and Cross-Engine Differences
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Indexing views.** A plain view has no index of its own; the optimiser uses the base-table indexes after expanding it. To store and index the result:
- **SQL Server indexed view:** create the view `WITH SCHEMABINDING` (two-part names, deterministic expressions, no outer joins or `DISTINCT` and, with `GROUP BY`, a `COUNT_BIG(*)` column), then `CREATE UNIQUE CLUSTERED INDEX`. The engine maintains it on every write and can use it even when queries do not mention it (on Enterprise-type editions); the write cost is the price.
- **PostgreSQL materialised view:** index it like a table; refresh explicitly (sub-topic 2).
- **MySQL:** index a summary table you maintain.

**Performance checklist** for server-side code: keep procedures set-based (avoid row-by-row cursors or loops), index join and filter keys ([[060 Query Optimization & Indexing]]), keep transactions short, avoid triggers on high-volume loading tables (or disable them during bulk loads where policy allows), read plans with `EXPLAIN (ANALYZE, BUFFERS)`, and avoid scalar UDFs in large scans.

**Engineering discipline:** store view, procedure and trigger definitions in source control; deploy through migration scripts; write tests (insert fixtures, call, assert rows); and document dependencies so a column rename does not silently break a view.

| Feature | PostgreSQL | MySQL 8.4 | SQL Server |
|---|---|---|---|
| Call a procedure | `CALL p(...)` | `CALL p(...)` | `EXEC p ...` |
| Procedural language | PL/pgSQL (also SQL, Python, etc.) | MySQL stored program syntax | T-SQL |
| Raise an error | `RAISE EXCEPTION` | `SIGNAL SQLSTATE '45000'` | `THROW` / `RAISERROR` |
| Catch an error | `EXCEPTION WHEN ...` | `DECLARE HANDLER` | `TRY ... CATCH` |
| Trigger images | `OLD` / `NEW` | `OLD` / `NEW` | `deleted` / `inserted` (set-based) |
| Temp table | `CREATE TEMP TABLE` | `CREATE TEMPORARY TABLE` | `#t`, `##t`, `@t` |
| Materialised view | Native | None | Indexed view |
| Row-level security | `CREATE POLICY` | None native | Security policy with predicate function |
| Recursive CTE keyword | `WITH RECURSIVE` | `WITH RECURSIVE` | `WITH` |
| String identifier quoting | double quotes | backticks | square brackets |

### Example
Summarise units issued per day and SKU from the movement log, then compare the plans for the base query and the stored result. With the few rows in this note the difference is invisible; on a movement table with tens of millions of rows, the second plan is an index lookup on a few hundred rows instead of a scan and aggregation of the whole table. After the sub-topic 9 scenario the summary shows SKU-A 20 and SKU-B 40 issued on the day it was run.
```sql
CREATE MATERIALIZED VIEW mv_daily_issues AS
SELECT moved_at::date AS day, sku, SUM(-qty) AS units_issued, COUNT(*) AS movements
FROM stock_movement WHERE qty < 0 GROUP BY 1, 2;
CREATE UNIQUE INDEX mv_daily_issues_pk ON mv_daily_issues (day, sku);
SELECT sku, units_issued FROM mv_daily_issues ORDER BY sku;                                              -- SKU-A 20 | SKU-B 40

EXPLAIN SELECT moved_at::date AS day, sku, SUM(-qty) FROM stock_movement WHERE qty < 0 GROUP BY 1, 2;   -- aggregates the base table
EXPLAIN SELECT sku, units_issued FROM mv_daily_issues WHERE day = CURRENT_DATE;                          -- reads the stored result
```
SQL Server indexed view skeleton (reference only, not executed here):
```tsql
CREATE VIEW dbo.v_issue_summary WITH SCHEMABINDING AS
SELECT sku, COUNT_BIG(*) AS movements, SUM(qty) AS net_qty   -- SUM over a NOT NULL column; COUNT_BIG(*) is mandatory
FROM dbo.stock_movement GROUP BY sku;
GO
CREATE UNIQUE CLUSTERED INDEX ix_v_issue_summary ON dbo.v_issue_summary (sku);
```

### In the news
See news box. With MySQL 8.0 retired and SQL Server 2025 and PostgreSQL 18 current, a good interview answer names the version it assumes, because defaults and features (generated columns, `RETURNING OLD/NEW`, regex, JSON) differ across them.

### Interview angle
> [!question] How it is asked
> "How would you speed up a slow dashboard query on a huge movement table?" / "Compare stored procedure syntax in MySQL, PostgreSQL and SQL Server."

> [!tip] Strong answer includes
> - Considers an index, a pre-aggregated summary (materialised or indexed view) and the freshness trade-off
> - Knows the SQL Server indexed-view restrictions (`SCHEMABINDING`, `COUNT_BIG`) and the write-cost trade-off
> - Compares error handling and trigger models across the three engines
> - Reads the execution plan before changing anything
> - Mentions source control, migrations and tests for database code; links to [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses]] for the analytics layer
