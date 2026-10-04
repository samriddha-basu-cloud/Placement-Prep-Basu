---
tags: [sql-databases, tier1]
area: SQL & Databases
topic: "SQL Interview Problem Bank"
tier: Tier 1
roles: Analytics / Operations / PM
status: complete
subtopics: 12
---
# SQL Interview Problem Bank

⬅ [[061 SQL for SCM & Business Analytics]] · [[_Index - SQL & Databases|SQL & Databases]] · [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses]] ➡

> **Area:** SQL & Databases · **Priority:** 🔴 Tier 1 · **Target roles:** Analytics / Operations / PM

## Sub-topics in this note
1. [[#1. How to Use This Bank: Schema, Seed Data and Method]]
2. [[#2. Ranking and Nth-Value Problems]]
3. [[#3. Duplicates and "Latest Record" Problems]]
4. [[#4. Anti-Joins, Self-Joins, Hierarchies and Division]]
5. [[#5. Running Totals, Moving Averages and Percent of Total]]
6. [[#6. Consecutive Days, Gaps and Islands]]
7. [[#7. Time Comparisons: MoM, YoY and Time Between Events]]
8. [[#8. Retention, Cohorts and Repeat Purchase]]
9. [[#9. Pivot, Unpivot and Conditional Aggregation]]
10. [[#10. Operations Metrics: OTIF, Supplier Scorecard, ABC, Dead Stock and Days of Cover]]
11. [[#11. Common Mistakes and Debugging Checklist]]
12. [[#12. ⭐ Advanced: Dialect Translation, Problem Index and Answer Delivery]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): SQL is still the most-tested analytics skill, and PostgreSQL-style SQL is now the common denominator
> **Stack Overflow Developer Survey 2025.** Of 26,083 respondents, SQL was used by **58.6%**; PostgreSQL led database usage at **55.6%** of all respondents (**58.2%** of professional developers), ahead of MySQL (40.5%), SQLite (37.5%) and Microsoft SQL Server (30.1%). Interview SQL is therefore best practised in PostgreSQL-flavoured ANSI SQL, with a mental translation table for MySQL and SQL Server (given in sub-topic 12). ([Stack Overflow](https://survey.stackoverflow.co/2025/technology))
>
> **PostgreSQL 18 released (25 Sep 2025).** Highlights per the official release notes: an asynchronous I/O subsystem, skip-scan lookups on multicolumn B-tree indexes, virtual generated columns, `OLD`/`NEW` in `RETURNING`, and the timestamp-ordered `uuidv7()` function. The window, CTE and aggregate-filter features used in this bank have been stable for many releases. ([PostgreSQL docs](https://www.postgresql.org/docs/release/18.0/))
>
> **MySQL 8.0 reached end of life (April 2026).** The release notes state that with version 8.0.46 (released 2026-04-21) MySQL 8.0 reaches EoL and point users to MySQL 8.4 LTS. Window functions and recursive CTEs arrived in 8.0, so they remain available on 8.4. ([MySQL release notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/))
>
> **SQL Server 2025 reached general availability (announced at Microsoft Ignite).** Microsoft's announcement lists a native vector type, native JSON capabilities and regular-expression functions among the headline features (exact GA date not confirmed from the page; check Microsoft's documentation). ([Microsoft Tech Community](https://techcommunity.microsoft.com/blog/sqlserver/sql-server-2025-is-now-generally-available/4470570))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. How to Use This Bank: Schema, Seed Data and Method
> 🔴 Tier 1 · _Key points:_ one shared schema, 38 numbered problems (plus variants), tested in PostgreSQL 16, difficulty tags [E] [M] [H]

### Definition
This bank holds **38 numbered classic SQL interview problems** (with variants, over 45 distinct queries) on one small e-commerce and operations schema so that every query can be checked by hand. Each problem has a difficulty tag (**[E]** easy, **[M]** medium, **[H]** hard), a tested solution and the trap interviewers look for. Every query below was executed on **PostgreSQL 16** against the seed data in this sub-topic; the printed results are the real outputs. Features used: `FILTER (WHERE ...)` on aggregates, `DATE_TRUNC`, `generate_series`, `percentile_cont ... WITHIN GROUP`, `DISTINCT ON`, `BOOL_AND`, `CROSS JOIN LATERAL (VALUES ...)`, date subtraction (`date - date` gives an integer number of days), `::` casts and `WITH RECURSIVE`. Sub-topic 12 translates each to MySQL 8 and SQL Server. Foundations are in [[053 SQL Foundations & Data Types]], [[056 JOINs — All Types]], [[057 Subqueries & CTEs]] and [[058 Window Functions]]; this note is the drill.

**Five-step method for any problem (say it aloud in the interview):**
1. Restate the output: columns, and the **grain** (one row per what?).
2. Identify the source tables and the join keys; ask about NULLs, duplicates and cancelled rows.
3. Pick the pattern: aggregate, window, anti-join, self-join, recursive, gaps and islands, conditional aggregation.
4. Build in small CTE steps and sanity-check each step on the sample data.
5. State edge cases: ties, empty groups, NULL, divide by zero, time zones, performance on large tables.

### Example
Run the DDL and seed data once; every later problem uses it. Dates run from Jan 2024 to Mar 2025. Order ids skip 1013 and 1020-1021 on purpose (for the gap problem), order 1010 is cancelled, customer 8 never ordered, product 303 was never sold, and customer 1 has a duplicate login row on 2025-03-02.

```sql
CREATE TABLE customers (customer_id INT PRIMARY KEY, name TEXT NOT NULL, city TEXT, segment TEXT, signup_date DATE);
CREATE TABLE products (product_id INT PRIMARY KEY, name TEXT NOT NULL, category TEXT, unit_cost NUMERIC(10,2), unit_price NUMERIC(10,2));
CREATE TABLE orders (order_id INT PRIMARY KEY, customer_id INT REFERENCES customers, order_date DATE NOT NULL,
  promised_date DATE, delivered_date DATE, status TEXT NOT NULL);
CREATE TABLE order_items (order_id INT REFERENCES orders, product_id INT REFERENCES products,
  qty INT NOT NULL, unit_price NUMERIC(10,2) NOT NULL, shipped_qty INT NOT NULL, PRIMARY KEY (order_id, product_id));
CREATE TABLE employees (emp_id INT PRIMARY KEY, name TEXT, manager_id INT REFERENCES employees, dept TEXT, salary INT);
CREATE TABLE logins (customer_id INT REFERENCES customers, login_date DATE NOT NULL);
CREATE TABLE inventory_txn (txn_id INT PRIMARY KEY, product_id INT REFERENCES products, txn_date DATE NOT NULL, qty INT NOT NULL);
CREATE TABLE stock_snapshot (product_id INT REFERENCES products, snap_date DATE, on_hand INT, PRIMARY KEY (product_id, snap_date));
CREATE TABLE suppliers (supplier_id INT PRIMARY KEY, name TEXT, city TEXT);
CREATE TABLE purchase_orders (po_id INT PRIMARY KEY, supplier_id INT REFERENCES suppliers, product_id INT REFERENCES products,
  po_date DATE, promised_date DATE, received_date DATE, ordered_qty INT, received_qty INT);
CREATE TABLE leads (lead_id INT PRIMARY KEY, email TEXT, source TEXT, created_at DATE);
CREATE TABLE bom (parent_item TEXT, component TEXT, qty_per INT);
CREATE TABLE sales_target (category TEXT PRIMARY KEY, q1 INT, q2 INT, q3 INT, q4 INT);

INSERT INTO customers VALUES
 (1,'Asha Mehta','Pune','Retail','2024-01-05'),(2,'Ravi Iyer','Mumbai','Retail','2024-01-20'),
 (3,'Neha Joshi','Nashik','Corporate','2024-02-10'),(4,'Karan Shah','Pune','Retail','2024-02-25'),
 (5,'Meera Nair','Bengaluru','Corporate','2024-03-15'),(6,'Imran Khan','Delhi','Retail','2024-04-02'),
 (7,'Sunita Rao','Mumbai','Retail','2024-05-18'),(8,'Vikram Das','Nashik','Corporate','2025-01-10');

INSERT INTO products VALUES
 (101,'USB Cable','Electronics',40,60),(102,'Charger','Electronics',150,250),(103,'Earbuds','Electronics',600,1000),
 (201,'Notebook','Stationery',20,35),(202,'Pen Pack','Stationery',30,50),
 (301,'Rice 5kg','Grocery',200,260),(302,'Cooking Oil 1L','Grocery',110,140),(303,'Tea 250g','Grocery',90,120);

INSERT INTO orders VALUES
 (1001,1,'2024-01-08','2024-01-12','2024-01-11','DELIVERED'),(1002,2,'2024-01-22','2024-01-26','2024-01-27','DELIVERED'),
 (1003,3,'2024-02-12','2024-02-16','2024-02-15','DELIVERED'),(1004,1,'2024-02-20','2024-02-24','2024-02-24','DELIVERED'),
 (1005,4,'2024-03-01','2024-03-05','2024-03-04','DELIVERED'),(1006,5,'2024-03-18','2024-03-22','2024-03-25','DELIVERED'),
 (1007,2,'2024-04-05','2024-04-09','2024-04-08','DELIVERED'),(1008,6,'2024-04-10','2024-04-14','2024-04-14','DELIVERED'),
 (1009,1,'2024-05-02','2024-05-06','2024-05-05','DELIVERED'),(1010,7,'2024-05-20','2024-05-24',NULL,'CANCELLED'),
 (1011,3,'2024-06-11','2024-06-15','2024-06-14','DELIVERED'),(1012,4,'2024-07-03','2024-07-07','2024-07-09','DELIVERED'),
 (1014,5,'2024-08-14','2024-08-18','2024-08-17','DELIVERED'),(1015,6,'2024-09-09','2024-09-13','2024-09-12','DELIVERED'),
 (1016,1,'2024-10-15','2024-10-19','2024-10-18','DELIVERED'),(1017,2,'2024-11-04','2024-11-08','2024-11-08','DELIVERED'),
 (1018,7,'2024-12-12','2024-12-16','2024-12-15','DELIVERED'),(1019,3,'2025-01-09','2025-01-13','2025-01-12','DELIVERED'),
 (1022,1,'2025-01-27','2025-01-31','2025-02-02','DELIVERED'),(1023,5,'2025-02-06','2025-02-10','2025-02-09','DELIVERED'),
 (1024,2,'2025-02-18','2025-02-22','2025-02-21','DELIVERED'),(1025,4,'2025-03-04','2025-03-08','2025-03-07','DELIVERED'),
 (1026,6,'2025-03-17','2025-03-21','2025-03-21','DELIVERED'),(1027,1,'2025-03-25','2025-03-29','2025-03-28','DELIVERED');

-- order_id, product_id, qty, unit_price, shipped_qty
INSERT INTO order_items VALUES
 (1001,101,10,60,10),(1001,201,20,35,20),(1002,103,2,1000,2),(1002,102,1,250,1),
 (1003,301,4,260,4),(1003,302,6,140,6),(1004,102,3,250,3),(1004,202,10,50,10),
 (1005,201,15,35,15),(1005,301,2,260,2),(1006,103,3,1000,2),(1006,101,5,60,5),
 (1007,302,10,140,10),(1007,201,5,35,5),(1008,102,2,250,2),(1008,201,10,35,10),
 (1009,103,1,1000,1),(1009,202,8,50,8),(1010,301,3,260,0),
 (1011,301,6,260,6),(1011,101,12,60,12),(1012,103,2,1000,2),(1012,302,4,140,3),
 (1014,102,4,250,4),(1014,202,6,50,6),(1015,301,5,260,5),(1015,201,25,35,25),
 (1016,103,2,1000,2),(1016,101,8,60,8),(1017,302,12,140,12),(1017,201,10,35,10),
 (1018,102,2,250,2),(1019,103,1,1000,1),(1019,301,3,260,3),
 (1022,103,3,1000,3),(1022,202,12,50,12),(1023,102,5,250,5),(1023,101,10,60,10),
 (1024,301,8,260,8),(1024,302,5,140,5),(1025,103,2,1000,2),(1025,201,20,35,18),
 (1026,102,3,250,3),(1026,202,10,50,10),(1027,103,1,1000,1),(1027,301,4,260,4);

INSERT INTO employees VALUES
 (1,'Anil Kulkarni',NULL,'Exec',200000),(2,'Bhavna Rao',1,'Ops',200000),(3,'Chetan Patil',1,'Tech',150000),
 (4,'Divya Menon',2,'Ops',90000),(5,'Esha Kapoor',2,'Ops',120000),(6,'Farhan Ali',3,'Tech',130000),
 (7,'Gita Sharma',3,'Tech',90000),(8,'Harsh Vora',4,'Ops',95000),(9,'Isha Bose',5,'Ops',70000),
 (10,'Jay Thakur',6,'Tech',140000);

INSERT INTO logins VALUES
 (1,'2025-03-01'),(1,'2025-03-02'),(1,'2025-03-02'),(1,'2025-03-03'),(1,'2025-03-05'),(1,'2025-03-06'),
 (1,'2025-03-07'),(1,'2025-03-08'),(1,'2025-03-12'),(2,'2025-03-01'),(2,'2025-03-03'),(2,'2025-03-04'),
 (3,'2025-03-02'),(3,'2025-03-03'),(3,'2025-03-04'),(3,'2025-03-05'),(5,'2025-03-10');

INSERT INTO inventory_txn VALUES
 (1,102,'2025-01-02',100),(2,102,'2025-01-05',-30),(3,102,'2025-01-09',-25),(4,102,'2025-01-15',60),
 (5,102,'2025-01-20',-40),(6,102,'2025-01-28',-35),(7,103,'2025-01-03',50),(8,103,'2025-01-10',-20),
 (9,103,'2025-01-22',-15),(10,103,'2025-02-04',-10);

INSERT INTO stock_snapshot VALUES
 (101,'2025-03-01',50),(101,'2025-03-02',40),(101,'2025-03-03',30),(101,'2025-03-04',0),(101,'2025-03-05',0),
 (101,'2025-03-06',0),(101,'2025-03-07',25),(101,'2025-03-08',15),(101,'2025-03-09',0),(101,'2025-03-10',0),
 (101,'2025-03-11',10),(101,'2025-03-12',5);

INSERT INTO suppliers VALUES (1,'Sahyadri Components','Pune'),(2,'Delta Packaging','Nashik'),(3,'Metro Traders','Mumbai');
INSERT INTO purchase_orders VALUES
 (9001,1,101,'2025-01-02','2025-01-09','2025-01-08',500,500),(9002,1,102,'2025-01-05','2025-01-12','2025-01-14',200,180),
 (9003,2,201,'2025-01-07','2025-01-14','2025-01-14',1000,1000),(9004,2,202,'2025-01-10','2025-01-17','2025-01-20',800,640),
 (9005,3,301,'2025-01-12','2025-01-19','2025-01-18',300,300),(9006,3,302,'2025-01-15','2025-01-22','2025-01-22',400,400),
 (9007,1,103,'2025-01-20','2025-01-27','2025-01-27',100,100),(9008,3,303,'2025-01-25','2025-02-01','2025-02-04',250,250);

INSERT INTO leads VALUES
 (1,'asha@example.com','web','2025-01-03'),(2,'ravi@example.com','referral','2025-01-04'),
 (3,'asha@example.com','event','2025-01-10'),(4,'neha@example.com','web','2025-01-11'),
 (5,'ravi@example.com','web','2025-01-12'),(6,'asha@example.com','web','2025-02-01'),
 (7,'karan@example.com','event','2025-02-02');

INSERT INTO bom VALUES ('Bike','Frame',1),('Bike','Wheel',2),('Wheel','Rim',1),('Wheel','Spoke',36),('Frame','Tube',4);
INSERT INTO sales_target VALUES ('Electronics',500,550,600,700),('Stationery',100,110,120,150),('Grocery',300,320,340,400);
```
Order revenue is `SUM(qty * unit_price)` over `order_items`. Unless a problem says otherwise, revenue counts only `status = 'DELIVERED'` orders (23 of the 24 orders). Total delivered revenue is 44,175; the three largest products are Earbuds (17,000), Rice 5kg (8,320) and Cooking Oil 1L (5,180).

### In the news
See news box. PostgreSQL is the most-used database in the 2025 survey, and MySQL 8.0 going end-of-life means interview databases are now MySQL 8.4 or PostgreSQL; all features used here exist on both (translations in sub-topic 12).

### Interview angle
> [!question] How it is asked
> "Here is a schema on the whiteboard. Write a query for X. Walk me through your thinking before you type."

> [!tip] Strong answer includes
> - States the grain of the output and of each source table before writing SQL
> - Builds the query in named CTE steps and checks each on a few rows
> - Calls out ties, NULLs, duplicates and cancelled or partial records unprompted
> - Names the dialect and mentions the portable alternative if a function is vendor-specific
> - Closes with one line on performance (indexes on join and filter keys, pre-aggregate before joining)

---
## 2. Ranking and Nth-Value Problems
> 🔴 Tier 1 · _Key points:_ second highest salary, Nth per group, top-N per category, ties, median

### Definition
Ranking problems ask for the **Nth value**, the **top N per group** or a **median**. Three window functions cover them and differ only in tie handling: `ROW_NUMBER()` (always unique, ties broken arbitrarily), `RANK()` (ties share a rank, then a gap) and `DENSE_RANK()` (ties share a rank, no gap). "Second highest salary" almost always means the second highest **distinct** value, so `DENSE_RANK() = 2` or `DISTINCT ... OFFSET 1` is correct and a naive `ORDER BY ... OFFSET 1` is wrong when the top value is tied. Details of window syntax are in [[058 Window Functions]].

### Example
**P1 [E] Second highest salary.** Salaries 200000 (two people), 150000, 140000 ... so the answer is 150000.
```sql
-- (a) DISTINCT + OFFSET; wrapped in a scalar subquery it returns NULL instead of "no rows"
SELECT (SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1) AS second_highest;  -- 150000
-- (b) Without window functions (works on any engine)
SELECT MAX(salary) AS second_highest FROM employees WHERE salary < (SELECT MAX(salary) FROM employees); -- 150000
-- (c) DENSE_RANK; generalises to the Nth value
SELECT DISTINCT salary FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rk FROM employees) t WHERE rk = 2;
-- WRONG when the top salary is tied: returns 200000, the second ROW, not the second value
SELECT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;
```

**P2 [M] Second highest salary in each department.** Ops: Esha 120000 (after Bhavna 200000); Tech: Jay 140000; Exec has only one salary, so no row.
```sql
SELECT dept, name, salary
FROM (SELECT dept, name, salary, DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rk FROM employees) t
WHERE rk = 2 ORDER BY dept;
-- Ops | Esha Kapoor | 120000      Tech | Jay Thakur | 140000
```

**P3 [M] Top 2 products by revenue within each category** (delivered orders only).
```sql
WITH rev AS (
  SELECT p.category, p.name, SUM(oi.qty * oi.unit_price) AS revenue
  FROM order_items oi JOIN products p USING (product_id) JOIN orders o USING (order_id)
  WHERE o.status = 'DELIVERED' GROUP BY p.category, p.name),
ranked AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY revenue DESC) AS rn FROM rev)
SELECT category, name, revenue FROM ranked WHERE rn <= 2 ORDER BY category, rn;
-- Electronics: Earbuds 17000, Charger 5000 | Grocery: Rice 8320, Cooking Oil 5180 | Stationery: Notebook 3675, Pen Pack 2300
```
Use `RANK()` instead of `ROW_NUMBER()` if the business wants **all** products tied at the cut-off.

**P4 [M] Highest-paid employee(s) per department, keeping ties.**
```sql
SELECT dept, name, salary
FROM (SELECT *, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rk FROM employees) t
WHERE rk = 1 ORDER BY dept, name;
-- Exec Anil 200000 | Ops Bhavna 200000 | Tech Chetan 150000
```

**P5 [M] Median salary, and median order value.** Salaries sorted: 70, 90, 90, 95, 120, 130, 140, 150, 200, 200 (thousand); the median is the mean of the 5th and 6th values, (120000 + 130000) / 2 = 125000.
```sql
-- PostgreSQL / SQL Server (as window): ordered-set aggregate
SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary FROM employees;   -- 125000
-- Portable (MySQL 8 too): pick the middle one or two rows
WITH r AS (SELECT salary, ROW_NUMBER() OVER (ORDER BY salary) AS rn, COUNT(*) OVER () AS n FROM employees)
SELECT AVG(salary) AS median_salary FROM r WHERE rn IN ((n + 1) / 2, (n + 2) / 2);              -- 125000
-- Median vs mean of delivered order values (23 orders): median 1880, mean 1920.65
WITH ov AS (SELECT o.order_id, SUM(oi.qty * oi.unit_price) AS v
            FROM order_items oi JOIN orders o USING (order_id) WHERE o.status = 'DELIVERED' GROUP BY o.order_id)
SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY v) AS median_value, ROUND(AVG(v), 2) AS mean_value FROM ov;
```
`(n+1)/2` and `(n+2)/2` use integer division: for n = 10 they give 5 and 6; for n = 9 both give 5.

### In the news
See news box. Ranking and median queries are plain ANSI/PostgreSQL features, so they behave the same on PostgreSQL 18 and MySQL 8.4; only `percentile_cont` needs the portable fallback on MySQL.

### Interview angle
> [!question] How it is asked
> "Find the second highest salary without using LIMIT." / "Top 3 products per category." / "What is the difference between RANK, DENSE_RANK and ROW_NUMBER?"

> [!tip] Strong answer includes
> - Asks whether "second highest" means the second distinct value, and handles ties explicitly
> - Gives the subquery (`MAX ... WHERE <`) answer and the `DENSE_RANK` answer, and says which generalises
> - Uses `ROW_NUMBER` for "exactly N rows" and `RANK` for "all ties at the cut-off"
> - Returns NULL, not an empty set, when the Nth value does not exist, if the caller needs it
> - Mentions the median needs `percentile_cont` or the two-middle-rows trick

---
## 3. Duplicates and "Latest Record" Problems
> 🔴 Tier 1 · _Key points:_ find duplicates, delete keeping one, latest row per entity, DISTINCT ON

### Definition
**Duplicate detection** groups by the business key and keeps groups with `COUNT(*) > 1`. **De-duplication** numbers rows inside each key with `ROW_NUMBER() OVER (PARTITION BY key ORDER BY <which one to keep>)` and removes `rn > 1`. The same numbering pattern answers "latest record per customer". Always decide, and say, **which duplicate survives** (latest, earliest, most complete). Data-quality context is in [[175 Data Quality, Master Data & Data Governance]].

### Example
**P6 [E] Emails that appear more than once in `leads`.**
```sql
SELECT email, COUNT(*) AS n FROM leads GROUP BY email HAVING COUNT(*) > 1 ORDER BY email;
-- asha@example.com 3 | ravi@example.com 2
```

**P7 [M] Delete duplicate leads, keeping the most recent row per email.** Seven rows become four.
```sql
BEGIN;
DELETE FROM leads
WHERE lead_id IN (
  SELECT lead_id FROM (
    SELECT lead_id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY created_at DESC, lead_id DESC) AS rn
    FROM leads) t
  WHERE rn > 1);                      -- DELETE 3
SELECT * FROM leads ORDER BY lead_id; -- keeps lead_id 4 (neha), 5 (ravi), 6 (asha), 7 (karan)
ROLLBACK;                             -- use COMMIT once the row count is as expected
```
Add the tie-breaker (`lead_id DESC`) so the survivor is deterministic. In production, take a backup or use a staging table; then add a `UNIQUE (email)` constraint so the problem cannot return.

**P8 [M] Latest order per customer.**
```sql
-- PostgreSQL-only shortcut
SELECT DISTINCT ON (customer_id) customer_id, order_id, order_date
FROM orders ORDER BY customer_id, order_date DESC, order_id DESC;
-- Portable
SELECT customer_id, order_id, order_date
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC, order_id DESC) AS rn FROM orders) t
WHERE rn = 1 ORDER BY customer_id;
-- 1:1027  2:1024  3:1019  4:1025  5:1023  6:1026  7:1018
```
Customer 7's latest order (1018) is a delivered one; their earlier order 1010 was cancelled. If the question is "latest **delivered** order", filter before numbering.

### In the news
See news box. `DISTINCT ON` is PostgreSQL-specific, which is why the portable `ROW_NUMBER()` form is worth memorising for MySQL 8.4 and SQL Server panels.

### Interview angle
> [!question] How it is asked
> "Delete duplicate rows from a table, keeping one." / "Get each customer's most recent order." / "How do you find duplicate emails?"

> [!tip] Strong answer includes
> - `GROUP BY ... HAVING COUNT(*) > 1` to find, `ROW_NUMBER` to delete
> - States which row survives and adds a deterministic tie-breaker
> - Runs the delete inside a transaction and checks the affected-row count
> - Prevents recurrence with a unique constraint or an upsert (`INSERT ... ON CONFLICT`)
> - Knows `DISTINCT ON` is PostgreSQL-only

---
## 4. Anti-Joins, Self-Joins, Hierarchies and Division
> 🔴 Tier 1 · _Key points:_ NOT EXISTS vs NOT IN, employees earning more than manager, recursive org tree, BOM explosion, "bought all"

### Definition
An **anti-join** returns rows with **no match** in another table: `NOT EXISTS` (safest), `LEFT JOIN ... WHERE right.key IS NULL`, or `NOT IN` (dangerous with NULLs: `1 NOT IN (2, NULL)` is never true, so the whole query returns no rows). A **self-join** joins a table to itself under two aliases (employee to manager). A **recursive CTE** walks a hierarchy of unknown depth: an anchor row set plus a recursive step joined back to the CTE. **Relational division** ("customers who bought **all** Electronics products") is solved by counting distinct matches and comparing with the total. See [[056 JOINs — All Types]] and [[057 Subqueries & CTEs]].

### Example
**P9 [E] Customers who never placed an order** (answer: Vikram Das, id 8).
```sql
SELECT c.customer_id, c.name FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);
-- Equivalent
SELECT c.customer_id, c.name FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id WHERE o.order_id IS NULL;
-- Products never sold (answer: Tea 250g, id 303: bought from suppliers in PO 9008 but no sale: dead stock)
SELECT p.product_id, p.name FROM products p
WHERE NOT EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id);
```

**P10 [M] Employees who earn more than their manager** (Harsh 95000 vs Divya 90000; Jay 140000 vs Farhan 130000).
```sql
SELECT e.name AS employee, e.salary, m.name AS manager, m.salary AS mgr_salary
FROM employees e JOIN employees m ON m.emp_id = e.manager_id
WHERE e.salary > m.salary;
```
The CEO has `manager_id` NULL and drops out of the inner join, which is the desired behaviour here.

**P11 [M] Full reporting chain, level and path for every employee; and each manager's total team size.**
```sql
WITH RECURSIVE org AS (
  SELECT emp_id, name, manager_id, 1 AS lvl, name::text AS path
  FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.emp_id, e.name, e.manager_id, o.lvl + 1, o.path || ' > ' || e.name
  FROM employees e JOIN org o ON e.manager_id = o.emp_id)
SELECT lvl, path FROM org ORDER BY path;
-- e.g. 4 | Anil Kulkarni > Bhavna Rao > Divya Menon > Harsh Vora   (10 rows, max level 4)

-- Total (direct + indirect) reports per person: Anil 9, Bhavna 4, Chetan 3, Divya 1
WITH RECURSIVE tree AS (
  SELECT emp_id AS root, emp_id FROM employees
  UNION ALL
  SELECT t.root, e.emp_id FROM tree t JOIN employees e ON e.manager_id = t.emp_id)
SELECT e.name, COUNT(*) - 1 AS reports_total
FROM tree t JOIN employees e ON e.emp_id = t.root GROUP BY e.name, e.emp_id
ORDER BY reports_total DESC, e.name LIMIT 4;
```

**P12 [M] Bill of materials explosion: components needed for one Bike.** Wheels 2, Spokes 2 x 36 = 72, Rims 2 x 1 = 2, Frame 1, Tubes 1 x 4 = 4.
```sql
WITH RECURSIVE x AS (
  SELECT component, qty_per::int AS qty, 1 AS lvl FROM bom WHERE parent_item = 'Bike'
  UNION ALL
  SELECT b.component, x.qty * b.qty_per, x.lvl + 1 FROM x JOIN bom b ON b.parent_item = x.component)
SELECT component, qty, lvl FROM x ORDER BY lvl, component;
-- Frame 1 L1 | Wheel 2 L1 | Rim 2 L2 | Spoke 72 L2 | Tube 4 L2
```
Quantities **multiply** down the tree. A cycle in the data (A needs B, B needs A) would loop forever; add a depth limit (`WHERE lvl < 10`) or track a path array.

**P13 [H] Customers who bought every Electronics product** (relational division; answer customers 1 and 5).
```sql
SELECT o.customer_id
FROM orders o JOIN order_items oi USING (order_id) JOIN products p USING (product_id)
WHERE o.status = 'DELIVERED' AND p.category = 'Electronics'
GROUP BY o.customer_id
HAVING COUNT(DISTINCT p.product_id) = (SELECT COUNT(*) FROM products WHERE category = 'Electronics')
ORDER BY 1;
```

### In the news
See news box. Recursive CTEs only arrived in MySQL with 8.0 and are retained in 8.4; SQL Server omits the `RECURSIVE` keyword, a one-word translation to mention if the interview database is not PostgreSQL.

### Interview angle
> [!question] How it is asked
> "Find customers with no orders." / "Employees earning more than their managers." / "Print the org chart." / "Customers who bought all products in a category."

> [!tip] Strong answer includes
> - Prefers `NOT EXISTS` and can explain the `NOT IN` plus NULL trap
> - Names the self-join aliases clearly (`e`, `m`) and explains why the CEO disappears
> - Writes anchor plus recursive member with a termination or cycle guard
> - Solves "all of" with `COUNT(DISTINCT) = total` rather than multiple joins
> - Relates BOM explosion to MRP requirement calculation (see [[061 SQL for SCM & Business Analytics]])

---
## 5. Running Totals, Moving Averages and Percent of Total
> 🔴 Tier 1 · _Key points:_ SUM() OVER, frame clauses, ROWS vs RANGE, calendar spine, above-average rows

### Definition
A **running total** is `SUM(x) OVER (PARTITION BY ... ORDER BY ...)`. A **moving average** adds a frame: `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`. **Percent of total** divides by `SUM(x) OVER ()`. Two traps: with only `ORDER BY`, the default frame is `RANGE ... CURRENT ROW`, so tied rows get the same running value (use `ROWS` for row-by-row); and a row-based moving average silently spans a wider period if some months are missing, so join to a **calendar spine** first (`generate_series`). Compare-to-group-average problems use `AVG() OVER (PARTITION BY ...)`.

### Example
**P14 [E] Running stock balance per product** (receipts positive, issues negative). Product 102 goes 100, 70, 45, 105, 65, 30; product 103 goes 50, 30, 15, 5.
```sql
SELECT product_id, txn_date, qty,
       SUM(qty) OVER (PARTITION BY product_id ORDER BY txn_date, txn_id) AS on_hand
FROM inventory_txn ORDER BY product_id, txn_date, txn_id;
```
Adding `txn_id` to the `ORDER BY` makes same-day transactions deterministic.

**P15 [M] Monthly delivered revenue, cumulative revenue and share of total.**
```sql
WITH m AS (
  SELECT DATE_TRUNC('month', o.order_date)::date AS month, SUM(oi.qty * oi.unit_price) AS revenue
  FROM orders o JOIN order_items oi USING (order_id) WHERE o.status = 'DELIVERED' GROUP BY 1)
SELECT month, revenue,
       SUM(revenue) OVER (ORDER BY month) AS cum_revenue,
       ROUND(100.0 * revenue / SUM(revenue) OVER (), 1) AS pct_of_total
FROM m ORDER BY month;
-- 2024-01 3550 (cum 3550, 8.0%) ... 2025-03 5990 (cum 44175, 13.6%); the 15 months total 44175
```

**P16 [M] 3-month moving average on a complete calendar.**
```sql
WITH months AS (SELECT generate_series('2024-01-01'::date, '2025-03-01'::date, interval '1 month')::date AS month),
rev AS (SELECT DATE_TRUNC('month', o.order_date)::date AS month, SUM(oi.qty * oi.unit_price) AS revenue
        FROM orders o JOIN order_items oi USING (order_id) WHERE o.status = 'DELIVERED' GROUP BY 1),
f AS (SELECT m.month, COALESCE(r.revenue, 0) AS revenue FROM months m LEFT JOIN rev r USING (month))
SELECT month, revenue,
       ROUND(AVG(revenue) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 0) AS ma3,
       COUNT(*) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS months_in_window
FROM f ORDER BY month;
-- 2024-03: (3550+3130+4345)/3 = 3675 | 2025-03: (4630+5380+5990)/3 = 5333
```
The first two rows have fewer than 3 months in the window (`months_in_window` shows 1 and 2); decide whether to show or suppress them.

**P17 [M] Orders larger than the same customer's average order, and employees paid above their department average.**
```sql
WITH ov AS (SELECT o.order_id, o.customer_id, SUM(oi.qty * oi.unit_price) AS value
            FROM orders o JOIN order_items oi USING (order_id) WHERE o.status = 'DELIVERED' GROUP BY 1, 2),
w AS (SELECT *, AVG(value) OVER (PARTITION BY customer_id) AS cust_avg FROM ov)
SELECT order_id, customer_id, value, ROUND(cust_avg, 1) AS cust_avg FROM w WHERE value > cust_avg ORDER BY customer_id, order_id;
-- 10 orders, e.g. 1022 (customer 1) 3600 vs average 2011.7

SELECT name, dept, salary
FROM (SELECT *, AVG(salary) OVER (PARTITION BY dept) AS a FROM employees) t
WHERE salary > a ORDER BY dept, salary DESC;
-- Bhavna 200000 (Ops avg 115000), Esha 120000, Chetan 150000 (Tech avg 127500), Jay 140000, Farhan 130000
```

### In the news
See news box. Window frames behave the same in PostgreSQL 18, MySQL 8.4 and SQL Server 2025, which is why running-total questions are the safest bet for any panel.

### Interview angle
> [!question] How it is asked
> "Compute a running balance of inventory." / "Show each month's share of annual revenue." / "Give a 3-month moving average." / "Rows above their group average."

> [!tip] Strong answer includes
> - Chooses `ROWS` over the default `RANGE` frame and explains the tie behaviour (with values 10, 20 on the same date, `RANGE` shows 30 and 30, `ROWS` shows 10 and 30)
> - Uses a calendar spine so missing months do not distort a moving average
> - Aggregates to the right grain (order, then customer) **before** applying the window
> - Adds a deterministic secondary sort key
> - Links to stock-balance logic used in [[003 Inventory Management]] and [[061 SQL for SCM & Business Analytics]]

---
## 6. Consecutive Days, Gaps and Islands
> 🔴 Tier 1 · _Key points:_ date minus row_number trick, LEAD/LAG, missing ids, stock-out spells, no-activity days

### Definition
**Gaps and islands**: an *island* is a run of consecutive values (days, ids); a *gap* is what is missing between islands. The classic trick: for consecutive dates, `date - ROW_NUMBER()` is **constant within a run**, so grouping by it yields each island's start, end and length. Always `DISTINCT` the dates first, otherwise duplicate rows break the arithmetic. For gaps, compare each value with `LEAD(value)` and keep rows where the difference is more than 1. For "days with nothing", left-join a generated calendar to the facts.

### Example
**P18 [M] Longest login streak per customer.** Customer 1 logged in on 1-3 March, 5-8 March and 12 March (with a duplicate row on 2 March), so the longest streak is 4 days.
```sql
WITH d AS (SELECT DISTINCT customer_id, login_date FROM logins),              -- remove duplicate days first
g AS (SELECT customer_id, login_date,
             login_date - (ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY login_date))::int AS grp FROM d),
s AS (SELECT customer_id, MIN(login_date) AS streak_start, MAX(login_date) AS streak_end, COUNT(*) AS days
      FROM g GROUP BY customer_id, grp),
r AS (SELECT *, RANK() OVER (PARTITION BY customer_id ORDER BY days DESC) AS rk FROM s)
SELECT customer_id, streak_start, streak_end, days FROM r WHERE rk = 1 ORDER BY customer_id;
-- 1: 2025-03-05..03-08 (4) | 2: 03-03..03-04 (2) | 3: 03-02..03-05 (4) | 5: 03-10 (1)
```
Select from `s` instead of `r` to list **every** streak (customer 1 has three: 3, 4 and 1 days).

**P19 [M] Customers who logged in on at least 3 consecutive days** (answer: 1 and 3), using `LEAD` instead of islands.
```sql
WITH d AS (SELECT DISTINCT customer_id, login_date FROM logins),
x AS (SELECT customer_id, login_date,
             LEAD(login_date, 1) OVER w AS d1, LEAD(login_date, 2) OVER w AS d2
      FROM d WINDOW w AS (PARTITION BY customer_id ORDER BY login_date))
SELECT DISTINCT customer_id FROM x WHERE d1 = login_date + 1 AND d2 = login_date + 2 ORDER BY 1;
```
This is quicker to write for a fixed length of 3; the island method handles any length.

**P20 [M] Missing order numbers (gaps in a sequence).** Order ids jump from 1012 to 1014 and from 1019 to 1022.
```sql
SELECT order_id + 1 AS gap_start, next_id - 1 AS gap_end
FROM (SELECT order_id, LEAD(order_id) OVER (ORDER BY order_id) AS next_id FROM orders) t
WHERE next_id - order_id > 1;
-- 1013..1013 and 1020..1021
```

**P21 [H] Stock-out spells: consecutive days at zero stock.** Product 101 was out of stock 4-6 March (3 days) and 9-10 March (2 days).
```sql
WITH z AS (SELECT product_id, snap_date,
                  snap_date - (ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY snap_date))::int AS grp
           FROM stock_snapshot WHERE on_hand = 0)
SELECT product_id, MIN(snap_date) AS stockout_from, MAX(snap_date) AS stockout_to, COUNT(*) AS days_out
FROM z GROUP BY product_id, grp ORDER BY stockout_from;
```
Filtering `on_hand = 0` **before** numbering is what makes the two spells land in different groups: the rows in between (7-8 March) are gone, so the date minus row number jumps.

**P22 [M] Calendar days in March 2025 with no orders** (28 of 31 days; orders were placed on the 4th, 17th and 25th only).
```sql
SELECT d::date AS day
FROM generate_series('2025-03-01'::date, '2025-03-31'::date, '1 day') AS d
LEFT JOIN orders o ON o.order_date = d::date
WHERE o.order_id IS NULL ORDER BY 1;
```
On engines without `generate_series`, build the calendar with a recursive CTE (see [[058 Window Functions]]) or a permanent date dimension table.

### In the news
See news box. `generate_series` is a PostgreSQL feature; MySQL 8.4 needs a recursive CTE for the same calendar, and SQL Server 2022 added `GENERATE_SERIES` as well.

### Interview angle
> [!question] How it is asked
> "Find users who logged in 3 days in a row." / "Longest streak per user." / "Find missing invoice numbers." / "How long was each product out of stock?"

> [!tip] Strong answer includes
> - Removes duplicate days first and explains why
> - Explains why `date - row_number` is constant inside a streak
> - Uses `LEAD`/`LAG` for fixed-length or gap questions and islands for variable length
> - Uses a calendar spine for "days with no activity"
> - Ties the stock-out query to service level and lost sales (see [[012 Supply Chain Analytics & KPIs]])

---
## 7. Time Comparisons: MoM, YoY and Time Between Events
> 🔴 Tier 1 · _Key points:_ LAG, same month last year, base effect, first-to-second order gap

### Definition
**Month-over-month (MoM)** compares with the previous period using `LAG(revenue) OVER (ORDER BY month)`. **Year-over-year (YoY)** compares with the same period a year earlier: either a **self-join** on `month = month - INTERVAL '1 year'` or `LAG(revenue, 12)` on a **gap-free** monthly series. Growth is `(current - previous) / previous`; guard the denominator with `NULLIF(previous, 0)`. Small bases produce huge percentages (base effect), so show the absolute values too. Time-between-events problems number each customer's orders and subtract dates.

### Example
**P23 [M] Month-over-month revenue growth.**
```sql
WITH m AS (
  SELECT DATE_TRUNC('month', o.order_date)::date AS month, SUM(oi.qty * oi.unit_price) AS revenue
  FROM orders o JOIN order_items oi USING (order_id) WHERE o.status = 'DELIVERED' GROUP BY 1)
SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
             / NULLIF(LAG(revenue) OVER (ORDER BY month), 0), 1) AS mom_pct
FROM m ORDER BY month;
-- 2024-02: 3130 vs 3550 = -11.8% | 2024-03: +38.8% | 2024-12: 500 vs 2030 = -75.4% | 2025-01: 5380 vs 500 = +976.0% (base effect)
```

**P24 [M] Year-over-year growth for each month that has a prior-year month.**
```sql
WITH m AS (
  SELECT DATE_TRUNC('month', o.order_date)::date AS month, SUM(oi.qty * oi.unit_price) AS revenue
  FROM orders o JOIN order_items oi USING (order_id) WHERE o.status = 'DELIVERED' GROUP BY 1)
SELECT cur.month, cur.revenue, prev.revenue AS same_month_last_year,
       ROUND(100.0 * (cur.revenue - prev.revenue) / prev.revenue, 1) AS yoy_pct
FROM m cur JOIN m prev ON prev.month = cur.month - INTERVAL '1 year'
ORDER BY cur.month;
-- 2025-01: 5380 vs 3550 = +51.5% | 2025-02: 4630 vs 3130 = +47.9% | 2025-03: 5990 vs 4345 = +37.9%
```
The self-join is robust to missing months (they simply produce no row); `LAG(revenue, 12)` is only correct if every month exists, which is why the calendar spine from P16 matters.

**P25 [M] Days between each customer's first and second delivered order.**
```sql
WITH o AS (
  SELECT customer_id, order_date,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn,
         LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_date
  FROM orders WHERE status = 'DELIVERED')
SELECT customer_id, prev_date AS first_order, order_date AS second_order, order_date - prev_date AS days_between
FROM o WHERE rn = 2 ORDER BY customer_id;
-- 1: 43 days | 2: 74 | 3: 120 | 4: 124 | 5: 149 | 6: 152   (customer 7 has only one delivered order)
```
Without the status filter, customer 7 would appear with a cancelled order as the "first" order: another reason to state the filter.

### In the news
See news box. Date arithmetic is where dialects differ most (PostgreSQL `date - date`, MySQL `DATEDIFF(a, b)`, SQL Server `DATEDIFF(day, b, a)`), so state the dialect before writing date logic.

### Interview angle
> [!question] How it is asked
> "Calculate MoM growth." / "YoY revenue by month." / "Average time between a customer's first and second purchase."

> [!tip] Strong answer includes
> - `LAG` with `NULLIF` to avoid divide-by-zero and shows absolute values beside percentages
> - Explains the base effect (+976% from a tiny December)
> - Chooses self-join or `LAG(12)` knowing the gap-free assumption
> - Filters cancelled orders before ranking events
> - Relates MoM and YoY to seasonality in demand planning ([[004 Demand Forecasting & Planning]])

---
## 8. Retention, Cohorts and Repeat Purchase
> 🔴 Tier 1 · _Key points:_ cohort month, month index, FILTER counts, new vs returning, consecutive-month activity

### Definition
A **cohort** groups customers by the month of their first order. **Retention** at month k is the share of the cohort still ordering k months later. Recipe: (1) cohort month per customer, (2) distinct customer-month activity, (3) join and compute `month_no`, (4) pivot with conditional counts and divide by cohort size. **Repeat rate** = customers with 2+ orders / customers with 1+ orders. **New vs returning** compares each order month with the customer's first-order month.

### Example
**P26 [H] Monthly cohort retention table.** January 2024 cohort: customers 1 and 2; only customer 1 ordered again in the next month (50% month-1 retention).
```sql
WITH first_o AS (
  SELECT customer_id, DATE_TRUNC('month', MIN(order_date))::date AS cohort
  FROM orders WHERE status = 'DELIVERED' GROUP BY 1),
act AS (SELECT DISTINCT customer_id, DATE_TRUNC('month', order_date)::date AS m
        FROM orders WHERE status = 'DELIVERED'),
j AS (SELECT f.cohort,
             (EXTRACT(YEAR FROM a.m) * 12 + EXTRACT(MONTH FROM a.m)
              - EXTRACT(YEAR FROM f.cohort) * 12 - EXTRACT(MONTH FROM f.cohort))::int AS month_no,
             a.customer_id
      FROM first_o f JOIN act a USING (customer_id))
SELECT cohort,
       COUNT(DISTINCT customer_id) FILTER (WHERE month_no = 0) AS m0,
       COUNT(DISTINCT customer_id) FILTER (WHERE month_no = 1) AS m1,
       COUNT(DISTINCT customer_id) FILTER (WHERE month_no BETWEEN 1 AND 3) AS within_3m
FROM j GROUP BY cohort ORDER BY cohort;
-- 2024-01: 2,1,2 | 2024-02: 1,0,0 | 2024-03: 2,0,0 | 2024-04: 1,0,0 | 2024-12: 1,0,0
```
Divide `m1` by `m0` for the retention rate. With only seven buyers the sample is tiny; the structure is what matters.

**P27 [M] Repeat purchase rate** (6 of 7 buyers ordered at least twice = 85.7%).
```sql
SELECT COUNT(*) FILTER (WHERE n >= 2) AS repeat_customers, COUNT(*) AS buyers,
       ROUND(100.0 * COUNT(*) FILTER (WHERE n >= 2) / COUNT(*), 1) AS repeat_rate_pct
FROM (SELECT customer_id, COUNT(*) AS n FROM orders WHERE status = 'DELIVERED' GROUP BY customer_id) t;
```

**P28 [M] New vs returning customers per month.**
```sql
WITH o AS (SELECT customer_id, DATE_TRUNC('month', order_date)::date AS m,
                  MIN(order_date) OVER (PARTITION BY customer_id) AS first_date
           FROM orders WHERE status = 'DELIVERED')
SELECT m AS month,
       COUNT(DISTINCT customer_id) FILTER (WHERE DATE_TRUNC('month', first_date) = m) AS new_customers,
       COUNT(DISTINCT customer_id) FILTER (WHERE DATE_TRUNC('month', first_date) < m) AS returning_customers
FROM o GROUP BY m ORDER BY m;
-- 2024-01: 2 new, 0 returning | 2024-02: 1, 1 | 2025-03: 0 new, 3 returning
```

**P29 [M] Customers who ordered in two consecutive calendar months** (answer: customer 1, who ordered in both January and February 2024).
```sql
WITH m AS (SELECT DISTINCT customer_id, DATE_TRUNC('month', order_date)::date AS mth
           FROM orders WHERE status = 'DELIVERED')
SELECT DISTINCT a.customer_id
FROM m a JOIN m b ON b.customer_id = a.customer_id AND b.mth = (a.mth + INTERVAL '1 month')::date
ORDER BY 1;
```

### In the news
See news box. Cohort tables are the standard output of product analytics; the same pattern is used for retention in PM interviews (see [[031 Product Metrics & Analytics]]).

### Interview angle
> [!question] How it is asked
> "Write a query for month-1 retention by signup cohort." / "What percentage of customers buy again?" / "Split monthly buyers into new and returning."

> [!tip] Strong answer includes
> - Defines the cohort and the activity event before writing SQL
> - Uses distinct customer-month activity so multiple orders do not inflate counts
> - Pivots with `FILTER` or `CASE` and divides by cohort size
> - Notes small cohorts make percentages noisy and that the latest month is incomplete
> - Distinguishes the retention definition (active in month k) from "returned within k months"

---
## 9. Pivot, Unpivot and Conditional Aggregation
> 🔴 Tier 1 · _Key points:_ FILTER vs CASE, quarter columns, wide-to-long, HAVING, product pairs

### Definition
**Pivot** turns row values into columns using conditional aggregation: `SUM(x) FILTER (WHERE cond)` (PostgreSQL) or `SUM(CASE WHEN cond THEN x END)` (portable; add `COALESCE(...,0)` if you need zeros instead of NULL). **Unpivot** turns columns into rows with `UNION ALL` or `CROSS JOIN LATERAL (VALUES ...)`. `WHERE` filters rows **before** grouping; `HAVING` filters groups **after** aggregation. A self-join on `order_items` with `a.product_id < b.product_id` counts product pairs bought together (market basket) without double counting. Excel analogue: [[075 Pivot Tables & Power Query]].

### Example
**P30 [M] 2024 delivered revenue by category and quarter.**
```sql
SELECT p.category,
  SUM(oi.qty * oi.unit_price) FILTER (WHERE EXTRACT(QUARTER FROM o.order_date) = 1) AS q1,
  SUM(oi.qty * oi.unit_price) FILTER (WHERE EXTRACT(QUARTER FROM o.order_date) = 2) AS q2,
  SUM(oi.qty * oi.unit_price) FILTER (WHERE EXTRACT(QUARTER FROM o.order_date) = 3) AS q3,
  SUM(oi.qty * oi.unit_price) FILTER (WHERE EXTRACT(QUARTER FROM o.order_date) = 4) AS q4
FROM order_items oi JOIN orders o USING (order_id) JOIN products p USING (product_id)
WHERE o.status = 'DELIVERED' AND EXTRACT(YEAR FROM o.order_date) = 2024
GROUP BY p.category ORDER BY p.category;
-- Electronics 6900 | 2220 | 3000 | 2980    Grocery 2400 | 2960 | 1860 | 1680    Stationery 1725 | 925 | 1175 | 350
-- Portable form of one column:
--   COALESCE(SUM(CASE WHEN EXTRACT(QUARTER FROM o.order_date) = 1 THEN oi.qty * oi.unit_price END), 0) AS q1
```

**P31 [M] Unpivot the quarterly target table into one row per category and quarter.**
```sql
SELECT t.category, v.quarter, v.target
FROM sales_target t
CROSS JOIN LATERAL (VALUES ('Q1', t.q1), ('Q2', t.q2), ('Q3', t.q3), ('Q4', t.q4)) AS v(quarter, target)
ORDER BY t.category, v.quarter;           -- 12 rows, e.g. Electronics Q1 500, Electronics Q2 550
-- Portable: one SELECT per quarter joined by UNION ALL (SELECT category, 'Q1' AS quarter, q1 AS target FROM sales_target UNION ALL SELECT category, 'Q2', q2 FROM sales_target and so on)
```

**P32 [E] Customers whose total delivered spend exceeds 5,000** (HAVING; customers 1, 2, 5, 4, 3 with 12070, 8635, 6450, 6305, 5940).
```sql
SELECT o.customer_id, SUM(oi.qty * oi.unit_price) AS total
FROM orders o JOIN order_items oi USING (order_id)
WHERE o.status = 'DELIVERED'
GROUP BY o.customer_id HAVING SUM(oi.qty * oi.unit_price) > 5000 ORDER BY total DESC;
```

**P33 [M] Which two products are most often bought together?** Charger (102) and Pen Pack (202) appear together in 3 orders.
```sql
SELECT a.product_id AS p1, b.product_id AS p2, COUNT(*) AS orders_together
FROM order_items a JOIN order_items b ON a.order_id = b.order_id AND a.product_id < b.product_id
GROUP BY 1, 2 ORDER BY orders_together DESC, p1, p2 LIMIT 4;
-- 102+202: 3 | 101+103: 2 | 103+202: 2 | 103+301: 2
```
(All orders, including the cancelled 1010, are counted here; add the `orders` join and status filter if cancelled orders must be excluded; order 1010 has only one item so it forms no pair anyway.)

### In the news
See news box. `FILTER` is PostgreSQL syntax (also SQLite); MySQL 8.4 and SQL Server need the `CASE` form, which is the portable answer to keep in your head. SQL Server also has a `PIVOT` operator.

### Interview angle
> [!question] How it is asked
> "Show sales by category as columns per quarter." / "Convert wide data to long format." / "Which products are bought together?" / "What is the difference between WHERE and HAVING?"

> [!tip] Strong answer includes
> - Knows the `CASE` pattern is portable and `FILTER` is shorter on PostgreSQL
> - Understands pivots need a fixed list of columns (dynamic pivots need dynamic SQL, see [[183 Views, Stored Procedures, Triggers & Temporary Tables]])
> - Uses `a.id < b.id` in the pair self-join to avoid duplicates and self-pairs
> - Separates row filters (`WHERE`) from group filters (`HAVING`)
> - Mentions that the output is easy to feed to a pivot-table or BI tool ([[047 MIS & Dashboard Design]])

---
## 10. Operations Metrics: OTIF, Supplier Scorecard, ABC, Dead Stock and Days of Cover
> 🔴 Tier 1 · _Key points:_ order-level OTIF, on-time vs in-full, fill rate, ABC cut-offs, days since last sale, cover

### Definition
**OTIF (On Time In Full)** = orders delivered on or before the promised date **and** with every line shipped in full, divided by delivered orders. It is computed at **order** level: one late or short line fails the whole order. **On-time %** and **fill rate** (received / ordered quantity) are separate supplier KPIs, and **lead time** is receipt date minus PO date. **ABC classification** ranks items by revenue and labels the cumulative 80% as A, the next 15% as B and the rest as C (Pareto). **Dead stock** is stock with no recent movement. **Days of cover** = stock on hand / average daily demand. Definitions and benchmarks: [[012 Supply Chain Analytics & KPIs]], [[003 Inventory Management]] and [[061 SQL for SCM & Business Analytics]].

### Example
**P34 [M] OTIF %, with the failing orders listed and OTIF by quarter.** 23 delivered orders: 19 on time, 20 in full, 18 both, so OTIF = 18 / 23 = 78.3%.
```sql
WITH line AS (
  SELECT o.order_id, o.promised_date, o.delivered_date,
         BOOL_AND(oi.shipped_qty >= oi.qty) AS in_full
  FROM orders o JOIN order_items oi USING (order_id)
  WHERE o.status = 'DELIVERED' GROUP BY o.order_id, o.promised_date, o.delivered_date)
SELECT COUNT(*) AS orders,
       COUNT(*) FILTER (WHERE delivered_date <= promised_date) AS on_time,
       COUNT(*) FILTER (WHERE in_full) AS in_full,
       COUNT(*) FILTER (WHERE delivered_date <= promised_date AND in_full) AS otif,
       ROUND(100.0 * COUNT(*) FILTER (WHERE delivered_date <= promised_date AND in_full) / COUNT(*), 1) AS otif_pct
FROM line;                                 -- 23 | 19 | 20 | 18 | 78.3

-- Which orders fail, and why (5 orders)
WITH line AS (
  SELECT o.order_id, (o.delivered_date <= o.promised_date) AS on_time, BOOL_AND(oi.shipped_qty >= oi.qty) AS in_full
  FROM orders o JOIN order_items oi USING (order_id)
  WHERE o.status = 'DELIVERED' GROUP BY o.order_id, o.delivered_date, o.promised_date)
SELECT order_id, on_time, in_full FROM line WHERE NOT (on_time AND in_full) ORDER BY order_id;
-- 1002 late | 1006 late and short | 1012 late and short | 1022 late | 1025 short only

-- OTIF by quarter
WITH line AS (
  SELECT o.order_id, DATE_TRUNC('quarter', o.order_date)::date AS qtr,
         (o.delivered_date <= o.promised_date AND BOOL_AND(oi.shipped_qty >= oi.qty)) AS otif
  FROM orders o JOIN order_items oi USING (order_id)
  WHERE o.status = 'DELIVERED' GROUP BY o.order_id, o.order_date, o.delivered_date, o.promised_date)
SELECT qtr, COUNT(*) AS orders, SUM(otif::int) AS otif_orders, ROUND(100.0 * AVG(otif::int), 1) AS otif_pct
FROM line GROUP BY qtr ORDER BY qtr;
-- 2024-Q1 66.7 | 2024-Q2 100.0 | 2024-Q3 66.7 | 2024-Q4 100.0 | 2025-Q1 71.4
```
`BOOL_AND` is PostgreSQL; elsewhere use `MIN(CASE WHEN shipped_qty >= qty THEN 1 ELSE 0 END) = 1`.

**P35 [M] Supplier scorecard: on-time %, fill rate, average lead time (days).**
```sql
SELECT s.name, COUNT(*) AS pos,
       ROUND(100.0 * AVG((po.received_date <= po.promised_date)::int), 1) AS on_time_pct,
       ROUND(100.0 * SUM(po.received_qty) / SUM(po.ordered_qty), 1) AS fill_rate_pct,
       ROUND(AVG(po.received_date - po.po_date), 1) AS avg_lead_days
FROM purchase_orders po JOIN suppliers s USING (supplier_id)
GROUP BY s.name ORDER BY on_time_pct DESC, s.name;
-- Metro Traders 3 | 66.7 | 100.0 | 7.7    Sahyadri Components 3 | 66.7 | 97.5 | 7.3    Delta Packaging 2 | 50.0 | 91.1 | 8.5
```
Fill rate is **weighted** (sum received over sum ordered); averaging per-PO percentages would overweight small POs. Delta's fill rate: (1000 + 640) / (1000 + 800) = 91.1%.

**P36 [M] ABC classification by revenue.**
```sql
WITH rev AS (
  SELECT p.product_id, p.name, SUM(oi.qty * oi.unit_price) AS revenue
  FROM order_items oi JOIN orders o USING (order_id) JOIN products p USING (product_id)
  WHERE o.status = 'DELIVERED' GROUP BY 1, 2),
c AS (SELECT *, SUM(revenue) OVER (ORDER BY revenue DESC, product_id) AS cum_rev, SUM(revenue) OVER () AS total FROM rev)
SELECT name, revenue, ROUND(100.0 * cum_rev / total, 1) AS cum_pct,
       CASE WHEN cum_rev - revenue < 0.80 * total THEN 'A'
            WHEN cum_rev - revenue < 0.95 * total THEN 'B' ELSE 'C' END AS abc_class
FROM c ORDER BY revenue DESC, product_id;
-- Earbuds 17000 38.5% A | Rice 8320 57.3% A | Cooking Oil 5180 69.0% A | Charger 5000 80.4% A
-- Notebook 3675 88.7% B | USB Cable 2700 94.8% B | Pen Pack 2300 100.0% B
```
This version assigns an item to the class in which its **start** (cumulative before it) falls, so the item that crosses 80% (Charger, 80.4%) stays in A. The stricter variant `cum_rev / total <= 0.80` pushes Charger to B and Pen Pack to C. Both conventions exist; state yours. With only 7 SKUs the Pareto shape is mild, whereas real catalogues are far more skewed.

**P37 [M] Days since last sale per product (as of 2025-03-31), including products never sold.**
```sql
SELECT p.name, MAX(o.order_date) AS last_sale, DATE '2025-03-31' - MAX(o.order_date) AS days_since_sale
FROM products p
LEFT JOIN order_items oi USING (product_id)
LEFT JOIN orders o ON o.order_id = oi.order_id AND o.status = 'DELIVERED'
GROUP BY p.name ORDER BY days_since_sale DESC NULLS FIRST, p.name;
-- Tea 250g NULL (never sold) | USB Cable 2025-02-06, 53 days | Cooking Oil 41 | Notebook 27 | Charger 14 | Pen Pack 14 | Earbuds 6 | Rice 6
```
The status condition sits in the `ON` clause, not in `WHERE`, so products with no delivered sales are kept (a `WHERE` filter would turn the left join into an inner join).

**P38 [M] Days of cover for each product from January 2025 movements.** Product 102: closing stock 30, issues of 130 units over 31 days = 4.19 per day, so about 7.2 days of cover; product 103: stock 15, issues 35, so 1.13 per day and 13.3 days.
```sql
WITH j AS (
  SELECT product_id, SUM(qty) AS on_hand_end, -SUM(qty) FILTER (WHERE qty < 0) AS issued, 31 AS days
  FROM inventory_txn WHERE txn_date BETWEEN '2025-01-01' AND '2025-01-31' GROUP BY product_id)
SELECT product_id, on_hand_end, issued,
       ROUND(issued::numeric / days, 2) AS daily_demand,
       ROUND(on_hand_end / (issued::numeric / days), 1) AS days_of_cover
FROM j ORDER BY product_id;
-- 102 | 30 | 130 | 4.19 | 7.2     103 | 15 | 35 | 1.13 | 13.3
```
Product 103's February issue (10 units on 4 Feb) is outside the January window, so its closing stock here is 15, not 5. A reorder-point check compares days of cover with supplier lead time (about 7 to 8 days in P35).

### In the news
See news box. OTIF and supplier scorecards are exactly the queries run daily in warehouse and procurement dashboards; correctness at the order grain is what separates a credible KPI from a flattering one.

### Interview angle
> [!question] How it is asked
> "Calculate OTIF." / "Build a supplier scorecard." / "Classify SKUs into A, B, C." / "Which products have not sold in 90 days?" / "How many days of stock do we have?"

> [!tip] Strong answer includes
> - Computes OTIF at **order** level and shows on-time and in-full separately for diagnosis
> - Uses weighted fill rate and defines lead time clearly
> - States the ABC cut-off convention and that thresholds are a policy choice
> - Keeps `LEFT JOIN` conditions in `ON` so zero-sale products survive
> - Links cover to reorder point and safety stock ([[003 Inventory Management]]) and flags the as-of date

---
## 11. Common Mistakes and Debugging Checklist
> 🔴 Tier 1 · _Key points:_ NULL logic, join fan-out, integer division, COUNT variants, WHERE vs ON, window defaults

### Definition
Most wrong interview answers fail on one of a dozen traps, not on syntax. Check these before saying "done":

| Mistake | Symptom | Fix |
|---|---|---|
| `NOT IN` on a column with NULLs | Query returns no rows | Use `NOT EXISTS` |
| Filtering the right table of a `LEFT JOIN` in `WHERE` | Left join behaves as inner join; zero-activity rows vanish | Move the condition to `ON` |
| Join **fan-out**: joining orders to items then summing an order-level column | Totals inflated | Aggregate to the right grain first, then join |
| `COUNT(*)` vs `COUNT(col)` vs `COUNT(DISTINCT col)` | Counts include NULLs or duplicates | `COUNT(col)` skips NULLs; pick deliberately |
| Integer division (`100 * 3 / 7` gives 42) | Percentages truncated | Use `100.0 * a / b` or cast to `numeric` |
| Dividing by zero | Error or NULL surprises | `NULLIF(denominator, 0)` |
| `LIMIT` or `OFFSET` without `ORDER BY` | Non-deterministic rows | Always order, with a tie-breaker |
| Default window frame with ties | Equal running totals for tied rows | `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` |
| `LAST_VALUE` with the default frame | Returns the current row | Extend the frame to `UNBOUNDED FOLLOWING` |
| Duplicate dates before an islands query | Wrong streak lengths | `SELECT DISTINCT` first |
| `BETWEEN` on timestamps | Last day excluded or double counted | Use `>= start AND < next_start` |
| Filtering cancelled or test rows inconsistently | KPIs do not reconcile | Put the status rule in one CTE |
| `SELECT DISTINCT` used to hide a join bug | Slow and still wrong | Find the cause of the duplicates |

### Example
Two verified illustrations. First, **fan-out and grain**: the average of `qty * unit_price` over `order_items` is the average **line** value (977.28), whereas the average **order** value over delivered orders is 1920.65: the question "average order value" needs the order-level CTE from P5. Second, the **`ROWS` vs `RANGE`** difference on tied sort keys:
```sql
SELECT d, x,
       SUM(x) OVER (ORDER BY d) AS range_sum,                                              -- default frame
       SUM(x) OVER (ORDER BY d ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS rows_sum
FROM (VALUES (1, 10), (1, 20), (2, 5)) AS t(d, x);
-- (1,10): range 30, rows 10 | (1,20): range 30, rows 30 | (2,5): range 35, rows 35

SELECT 7 / 2 AS int_div, 7 / 2.0 AS num_div, 100 * 3 / 7 AS int_pct, ROUND(100.0 * 3 / 7, 1) AS num_pct;
-- 3 | 3.5 | 42 | 42.9

SELECT 'row' WHERE 1 NOT IN (2, NULL);       -- returns no rows: NULL makes NOT IN unknown
SELECT COUNT(*) AS all_rows, COUNT(delivered_date) AS non_null FROM orders;   -- 24 vs 23 (cancelled order has NULL)
```
And the `LEFT JOIN` trap: customer 8 appears with count 0 when the status test is in `ON`, and vanishes when it is in `WHERE`.

### In the news
See news box. These traps are engine-independent, which is why interviewers use them to separate memorised syntax from understanding; the same NULL and grain discipline underpins data-quality work ([[175 Data Quality, Master Data & Data Governance]]).

### Interview angle
> [!question] How it is asked
> "Your query returns different totals from the finance report. How do you debug it?" / "Why does this NOT IN return nothing?" / "Why is my running total the same for two rows?"

> [!tip] Strong answer includes
> - Reconciles at each step: row counts per CTE, then a total checked against a known figure
> - Names the grain of each table and spots fan-out
> - Explains NULL three-valued logic in one sentence
> - Mentions `EXPLAIN` and indexes on join keys when asked about performance ([[060 Query Optimization & Indexing]])
> - Treats edge cases (ties, empty groups, cancelled rows) as part of the answer, not an afterthought

---
## 12. ⭐ Advanced: Dialect Translation, Problem Index and Answer Delivery
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Panels use PostgreSQL, MySQL 8 or SQL Server (or an online editor you do not choose). Know the equivalents of the PostgreSQL features used above and the index of all problems for revision.

| Need | PostgreSQL (used here) | MySQL 8.x | SQL Server |
|---|---|---|---|
| Limit rows | `LIMIT n OFFSET k` | `LIMIT n OFFSET k` | `OFFSET k ROWS FETCH NEXT n ROWS ONLY` or `TOP n` |
| Truncate to month | `DATE_TRUNC('month', d)` | `DATE_FORMAT(d, '%Y-%m-01')` | `DATEFROMPARTS(YEAR(d), MONTH(d), 1)` |
| Days between | `d2 - d1` | `DATEDIFF(d2, d1)` | `DATEDIFF(day, d1, d2)` |
| Add a month | `d + INTERVAL '1 month'` | `DATE_ADD(d, INTERVAL 1 MONTH)` | `DATEADD(month, 1, d)` |
| Conditional aggregate | `SUM(x) FILTER (WHERE c)` | `SUM(CASE WHEN c THEN x END)` | `SUM(CASE WHEN c THEN x END)` |
| Median | `percentile_cont(0.5) WITHIN GROUP (...)` | two-middle-rows with `ROW_NUMBER` | `PERCENTILE_CONT(0.5) WITHIN GROUP (...) OVER (...)` |
| First row per group | `DISTINCT ON (k)` or `ROW_NUMBER` | `ROW_NUMBER` | `ROW_NUMBER` |
| Calendar | `generate_series` | recursive CTE | recursive CTE or `GENERATE_SERIES` (2022+) |
| Boolean AND per group | `BOOL_AND(cond)` | `MIN(cond) = 1` | `MIN(CASE WHEN cond THEN 1 ELSE 0 END) = 1` |
| Recursive CTE keyword | `WITH RECURSIVE` | `WITH RECURSIVE` | `WITH` (no keyword) |
| Concatenate | text `\|\|` operator | `CONCAT(a, b)` | `CONCAT(a, b)` or `+` |
| Cast | `x::int` or `CAST` | `CAST` | `CAST` or `CONVERT` |

### Example
**Problem index for revision** (tag = difficulty; pattern = what to say first):

| Q | Tag | Problem | Pattern |
|---|---|---|---|
| P1 | E | Second highest salary | `DENSE_RANK`, distinct, ties |
| P2 | M | Second highest per department | `DENSE_RANK` partition |
| P3 | M | Top 2 products per category | `ROW_NUMBER` partition |
| P4 | M | Highest paid per department with ties | `RANK = 1` |
| P5 | M | Median salary and order value | `percentile_cont`, middle rows |
| P6 | E | Duplicate emails | `GROUP BY HAVING` |
| P7 | M | Delete duplicates keep latest | `ROW_NUMBER`, transaction |
| P8 | M | Latest order per customer | `DISTINCT ON`, `ROW_NUMBER` |
| P9 | E | Customers with no orders, products never sold | `NOT EXISTS` anti-join |
| P10 | M | Earns more than manager | self-join |
| P11 | M | Org chart, team sizes | recursive CTE |
| P12 | M | BOM explosion | recursive CTE with multiplication |
| P13 | H | Bought all Electronics | relational division |
| P14 | E | Running stock balance | `SUM() OVER` |
| P15 | M | Cumulative revenue, percent of total | window, `SUM() OVER ()` |
| P16 | M | 3-month moving average | frame, calendar spine |
| P17 | M | Above own average | `AVG() OVER (PARTITION BY)` |
| P18 | M | Longest login streak | islands |
| P19 | M | 3 consecutive days | `LEAD` |
| P20 | M | Missing order numbers | gap with `LEAD` |
| P21 | H | Stock-out spells | islands on filtered rows |
| P22 | M | Days with no orders | `generate_series` left join |
| P23 | M | MoM growth | `LAG`, `NULLIF` |
| P24 | M | YoY growth | self-join on month - 1 year |
| P25 | M | Days between first and second order | `ROW_NUMBER`, `LAG` |
| P26 | H | Cohort retention | cohort, month index, `FILTER` |
| P27 | M | Repeat purchase rate | nested aggregate |
| P28 | M | New vs returning by month | window `MIN` per customer |
| P29 | M | Orders in consecutive months | self-join on month + 1 |
| P30 | M | Category by quarter | pivot |
| P31 | M | Wide to long targets | unpivot with `LATERAL VALUES` |
| P32 | E | Spend above 5,000 | `HAVING` |
| P33 | M | Products bought together | self-join `a < b` |
| P34 | M | OTIF | order-level boolean aggregate |
| P35 | M | Supplier scorecard | weighted fill rate |
| P36 | M | ABC classification | cumulative share |
| P37 | M | Days since last sale | left join, `ON` filter |
| P38 | M | Days of cover | issues per day |

Several problems carry extra variants (P1 has four solutions, P3 to P5, P8, P31 and P34 have alternatives), so the bank holds well over 45 distinct tested queries.

**Delivering the answer (60-second pattern):** restate the grain; name the pattern; write CTE 1 and say what it returns; write the final select; run through one example row; mention one edge case and one performance point. Practise the pivot, cohort and OTIF problems aloud, since they carry the most follow-ups.

### In the news
See news box. With SQL Server 2025 adding native regex and JSON, and PostgreSQL 18 adding `uuidv7()` and virtual generated columns, vendor-specific shortcuts keep growing; the portable core in this bank stays valid across all three engines.

### Interview angle
> [!question] How it is asked
> "Which SQL dialect are you most comfortable with? Rewrite this query for MySQL." / "How would you approach an unfamiliar schema in a timed test?"

> [!tip] Strong answer includes
> - Names the dialect up front and translates `FILTER`, `DISTINCT ON`, date functions and `generate_series` on request
> - Falls back to the portable form (`CASE`, `ROW_NUMBER`, recursive CTE) when unsure of vendor syntax
> - Uses a repeatable delivery script: grain, pattern, CTE steps, example row, edge case, performance
> - Points to follow-up reading: [[045 SQL for Operations Analytics]], [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses]], [[143 SCM Interview Question Bank]]
