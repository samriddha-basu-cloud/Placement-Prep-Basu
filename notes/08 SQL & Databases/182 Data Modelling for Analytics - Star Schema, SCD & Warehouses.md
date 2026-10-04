---
tags: [sql-databases, tier2]
area: SQL & Databases
topic: "Data Modelling for Analytics - Star Schema, SCD & Warehouses"
tier: Tier 2
roles: Analytics / Operations
status: complete
subtopics: 12
---
# Data Modelling for Analytics - Star Schema, SCD & Warehouses

⬅ [[181 SQL Interview Problem Bank]] · [[_Index - SQL & Databases|SQL & Databases]] · [[183 Views, Stored Procedures, Triggers & Temporary Tables]] ➡

> **Area:** SQL & Databases · **Priority:** 🟠 Tier 2 · **Target roles:** Analytics / Operations

## Sub-topics in this note
1. [[#1. OLTP vs OLAP and the Analytics Stack]]
2. [[#2. Dimensional Modelling: Business Process, Grain, Dimensions, Facts]]
3. [[#3. Fact Table Types and Additivity]]
4. [[#4. Star, Snowflake and Constellation Schemas; Conformed Dimensions]]
5. [[#5. Keys and Special Dimensions: Surrogate Keys, Degenerate, Role-Playing and the Date Dimension]]
6. [[#6. Slowly Changing Dimensions: Types 0, 1, 2 and 3]]
7. [[#7. SCD Types 4, 5, 6, 7 and Implementing Type 2 in SQL]]
8. [[#8. Modelling a Supply-Chain Warehouse: Inventory Snapshot, Shipment and PO Facts]]
9. [[#9. Data Vault, Inmon vs Kimball and One-Big-Table Designs]]
10. [[#10. ETL vs ELT, Layered Pipelines and Change Data Capture]]
11. [[#11. Data Lake, Warehouse and Lakehouse; Open Table Formats]]
12. [[#12. ⭐ Advanced: Metrics and Semantic Layers, and a Modelling Case]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the analytics stack is converging on open table formats, ELT-style transformation and shared metric definitions
> **Fivetran and dbt Labs complete their merger (1 June 2026).** The combined "Fivetran + dbt Labs" company pairs data movement (ingestion) with dbt's SQL transformation standard, serves over 100,000 data teams per the company, and is open-sourcing the dbt Fusion engine runtime in dbt Core v2.0 (alpha, Apache 2.0). Its announcement also describes an open "Agents Schema" that stores semantic models and business documentation in plain SQL tables. The deal is a marker of how normal ELT (load first, transform in the warehouse with SQL) has become. ([Fivetran](https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents))
>
> **Snowflake doubles down on Apache Iceberg and open source (8 April 2026).** Snowflake said it plans production-ready support for Iceberg V3 (the spec released in June 2025, adding semi-structured data, row-level change data capture, geospatial data and nanosecond timestamps), and is building or joining pg_lake (a PostgreSQL extension open-sourced in November 2025), Apache Polaris Catalog, OpenLineage and an Open Semantic Interchange for semantic modelling. ([TechTarget](https://www.techtarget.com/searchdatamanagement/news/366641473/Snowflake-broadens-open-source-embrace-ups-Iceberg-support))
>
> **Databricks adds managed Iceberg tables (12 June 2025, public preview).** Unity Catalog can write Iceberg tables that any Iceberg client can read through the Iceberg REST Catalog API, and can federate Iceberg tables managed by external catalogs such as AWS Glue and Snowflake Horizon. Together with the Snowflake item, this is the evidence behind the "lakehouse with open table formats" pattern. ([Databricks](https://www.databricks.com/blog/announcing-full-apache-iceberg-support-databricks))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. OLTP vs OLAP and the Analytics Stack
> 🟠 Tier 2 · _Key points:_ transactional vs analytical workloads, normalised vs denormalised, row vs columnar, where each system sits

### Definition
**OLTP (online transaction processing)** systems run the business: place an order, post a goods receipt, update stock. They handle many short read-write transactions on current data, use **normalised** schemas (third normal form) to avoid anomalies, and are optimised for single-row access by key. **OLAP (online analytical processing)** systems answer questions about the business: revenue by region and month, OTIF by carrier. They scan and aggregate millions of rows of historical data, use **denormalised dimensional** models, and are optimised for read throughput, usually with **columnar storage** (only the needed columns are read, and similar values compress well).

| Aspect | OLTP | OLAP / data warehouse |
|---|---|---|
| Purpose | Run operations | Analyse and report |
| Typical operation | Insert, update, read one record | Scan, join, aggregate many records |
| Data | Current, detailed | Historical, integrated, often summarised |
| Schema | Normalised (3NF) | Dimensional (star), sometimes wide tables |
| Storage | Row store | Column store (common) |
| Latency target | Milliseconds per transaction | Seconds to minutes per query |
| Examples | SAP S/4HANA, PostgreSQL or MySQL behind an app | Snowflake, BigQuery, Redshift, Microsoft Fabric, Databricks SQL |
| Users | Clerks, applications | Analysts, managers, BI tools |

The usual flow is source systems (ERP, WMS, TMS, e-commerce) feed an **integration layer** (ETL or ELT), then a **warehouse or lakehouse** with dimensional marts, then BI tools and data science. **HTAP** (hybrid transactional-analytical) engines blur the line but do not remove the modelling choices below. ERP context: [[013 ERP & Enterprise Systems (SAP-Oracle)]] and [[085 SAP Reporting & Analytics]]; the SQL skills assumed are in [[053 SQL Foundations & Data Types]] and [[058 Window Functions]].

### Example
The same fact looks different in the two worlds. In the OLTP schema a shipment touches five normalised tables (`shipment`, `shipment_line`, `product`, `address`, `carrier`). A manager asking for "freight cost per unit by carrier by month" would need a five-table join over millions of rows on a system that is busy taking orders. In the warehouse one **fact table** holds one row per shipment line with foreign keys to small, pre-joined **dimension tables**, so the same question is one join per dimension and one `GROUP BY`, run on a separate system without slowing operations. This is the core argument for a dimensional model.

### In the news
See news box. The Fivetran and dbt merger and the Iceberg announcements all concern moving data out of OLTP systems into analytical storage and transforming it there.

### Interview angle
> [!question] How it is asked
> "What is the difference between OLTP and OLAP? Why not report directly from the transactional database?"

> [!tip] Strong answer includes
> - Workload contrast: many small writes vs few large reads
> - Normalised vs dimensional design and row vs columnar storage
> - Why reporting on OLTP hurts performance and gives unstable history
> - Where each sits in the stack (ERP vs warehouse) with an example
> - Mentions that the warehouse integrates several sources and keeps history

---
## 2. Dimensional Modelling: Business Process, Grain, Dimensions, Facts
> 🟠 Tier 2 · _Key points:_ Kimball four-step design, declaring the grain, facts vs dimensions, descriptive attributes

### Definition
**Dimensional modelling** (Ralph Kimball's approach) organises analytics data into **facts** (numeric measurements of a business event) and **dimensions** (the descriptive context: who, what, where, when, how). The design process has four steps:

1. **Choose the business process** (order fulfilment, inventory, procurement, shipping).
2. **Declare the grain**: exactly what one fact-table row represents (for example "one row per shipment line", "one row per product per location per day"). Declaring grain first prevents mixed-grain tables, the most damaging modelling error.
3. **Identify the dimensions** that describe the event at that grain (date, product, location, carrier, supplier).
4. **Identify the facts**: the numeric measures at that grain (quantity, cost, value). Prefer additive facts, store components not ratios (store `delivered_qty` and `ordered_qty`, derive fill rate).

Dimensions are wide and denormalised, with many descriptive attributes (product name, brand, category, pack size) used for filtering, grouping and labelling. A good dimension is the "user interface" of the warehouse: analysts slice by its attributes. Contrast with Inmon's top-down approach (a normalised enterprise warehouse first, marts after) in sub-topic 9. The foundation SQL is in [[055 Aggregations & GROUP BY]] and [[056 JOINs — All Types]].

### Example
Process: outbound shipping. Grain: one row per shipment line (one product on one shipment). Dimensions: ship date, promised date, delivery date (the date dimension used three times), product, origin location, destination location, carrier. Facts: `qty_ordered`, `qty_delivered`, `freight_cost`. Degenerate dimension: `shipment_id` (kept in the fact table because it has no attributes of its own). Derived KPIs at query time: on-time (delivery date at or before the promised date), in-full (delivered at least ordered), freight per unit (sum of freight over sum of units, **not** the average of per-row ratios). The full DDL and queries are in sub-topic 8.

### In the news
See news box. dbt-style transformation projects usually name models by grain (for example a shipment-line fact), which is the same discipline in code.

### Interview angle
> [!question] How it is asked
> "Walk me through designing a data model for order fulfilment. What is the grain and why does it matter?"

> [!tip] Strong answer includes
> - The four steps in order, starting from business process and grain
> - Grain stated in one sentence, with consequences (no mixed grains, correct counts)
> - Facts additive where possible, ratios derived in queries
> - Dimension attributes chosen for how users will filter and group
> - Example from a supply-chain process (shipment, PO, inventory)

---
## 3. Fact Table Types and Additivity
> 🟠 Tier 2 · _Key points:_ transaction, periodic snapshot, accumulating snapshot, factless; additive, semi-additive, non-additive

### Definition
**Fact table types:**
- **Transaction fact:** one row per event (a shipment line, a goods issue). The most detailed, flexible and common.
- **Periodic snapshot:** one row per entity per period (inventory per product per location per day) regardless of activity. Fits **balances** that are not events.
- **Accumulating snapshot:** one row per process instance, **updated** as it passes milestones (a PO: ordered, confirmed, received, invoiced), with several date keys and lag measures. Fits pipelines and lead times.
- **Factless fact:** rows with keys but no measures, recording that something happened or was possible (a promotion covering a product-store pair, supplier-item authorisation).

**Additivity of facts:**
- **Additive:** sum over any dimension (units shipped, freight cost).
- **Semi-additive:** sum over some dimensions but **not time** (inventory on hand, account balance). Sum across products and locations for one date, but across dates use average, minimum, maximum or the end-of-period value.
- **Non-additive:** ratios, percentages, unit prices; store numerator and denominator and compute the ratio after summing.

### Example
Daily inventory snapshots for two products in two warehouses (Pune, Nashik) over three days, loaded into `fact_inventory_snapshot` (the DDL and rows are in sub-topic 8; units on hand and value at unit cost 40 for the cable P1 and 150 for the charger P2). Totals per date are legitimate sums across product and location:

| Date | Units | Value |
|---|---|---|
| 2025-04-01 | 190 | 13,100 |
| 2025-04-02 | 175 | 11,950 |
| 2025-04-03 | 150 | 9,850 |

Adding these three dates together (190 + 175 + 150 = 515 units) is meaningless: the same stock would be counted three times. The correct "average inventory value" over the period is the average of the daily totals, (13,100 + 11,950 + 9,850) / 3 = 11,633.33. This is the denominator of inventory turnover ([[003 Inventory Management]]); the common mistake is averaging at row level (here that would give 2,908.33, the average value per product-location-day, a different number).

### In the news
See news box. Open table formats such as Iceberg add snapshot and time-travel features at the storage level, but the modelling decision of periodic snapshot vs transaction fact remains yours.

### Interview angle
> [!question] How it is asked
> "What are the types of fact tables? What is a semi-additive measure? How would you model daily inventory?"

> [!tip] Strong answer includes
> - Names transaction, periodic snapshot, accumulating snapshot and factless facts with one example each
> - Semi-additive explained with inventory balances: sum across locations, average across time
> - Non-additive measures stored as components
> - Chooses a snapshot for balances and a transaction fact for events
> - Mentions storage growth of daily snapshots and strategies (partitioning, weekly after N days)

---
## 4. Star, Snowflake and Constellation Schemas; Conformed Dimensions
> 🟠 Tier 2 · _Key points:_ star vs snowflake trade-offs, galaxy of facts, conformed dimensions, bus matrix, outriggers and bridges

### Definition
A **star schema** has one central fact table joined directly to denormalised dimension tables, so every query is fact-to-dimension with one join per dimension. A **snowflake schema** normalises dimensions into sub-tables (product to category to department), saving a little storage and easing maintenance of hierarchies but adding joins and complexity. In modern columnar warehouses storage is cheap and joins cost time, so **stars are the default**; snowflake only where a sub-dimension is large and shared (an **outrigger**). A **constellation (galaxy) schema** has several fact tables sharing dimensions.

**Conformed dimensions** have identical keys, attributes and meaning across fact tables (the same `dim_product` and `dim_date` for sales, inventory and shipments). They enable **drill-across**: query two facts at the same grain of a shared dimension and combine the results (for example units sold vs units in stock by product and week). A **bus matrix** lists business processes down the side and dimensions across the top and marks which processes use which dimensions; it is the planning tool for conformance.

| Process | Date | Product | Location | Supplier | Carrier | Customer |
|---|---|---|---|---|---|---|
| Sales orders | X | X | X | | | X |
| Inventory snapshot | X | X | X | | | |
| Purchase order lines | X | X | X | X | | |
| Shipments | X | X | X | | X | X |

Other structures: **bridge tables** resolve many-to-many relationships (a product with several approved suppliers, with weighting factors); **role-playing dimensions** reuse one dimension for several roles (order date, ship date, delivery date); **junk dimensions** combine low-cardinality flags (rush flag, gift flag, payment mode) into one small dimension.

### Example
Snowflaking `dim_product`: `product` to `category` to `department` means three tables and two extra joins to answer "revenue by department". The star version stores `category` and `department` as columns in `dim_product`, repeating the text on every product row; with 100,000 products and 40 categories the repetition costs a few megabytes, trivial next to the speed and simplicity gained. A conformed `dim_location` shared by the inventory snapshot and the shipment fact lets a single report show "units shipped from Pune" next to "units in stock at Pune" without any reconciliation step.

### In the news
See news box. Semantic-layer efforts such as the Open Semantic Interchange that Snowflake mentions aim to share exactly these conformed definitions (what is a "product", a "location", an "active customer") across tools.

### Interview angle
> [!question] How it is asked
> "Star vs snowflake schema? What is a conformed dimension and why does it matter?"

> [!tip] Strong answer includes
> - Star: denormalised, fewer joins, easiest for BI; snowflake: normalised, more joins, saves space
> - Default to star in columnar warehouses, snowflake selectively
> - Conformed dimensions enable drill-across and one version of the truth
> - Bus matrix as the planning artefact
> - Role-playing, junk, bridge and outrigger structures as follow-ups

---
## 5. Keys and Special Dimensions: Surrogate Keys, Degenerate, Role-Playing and the Date Dimension
> 🟠 Tier 2 · _Key points:_ surrogate vs natural vs business key, unknown member, date dimension with Indian fiscal year, late-arriving data

### Definition
- **Natural (business) key:** the identifier from the source system (SKU, supplier code, GSTIN). It can change, be reused, collide across systems, or arrive in different formats.
- **Surrogate key:** a meaningless integer (or hash) generated by the warehouse. Benefits: insulates the warehouse from source-key changes, lets one entity have **multiple versions** (slowly changing dimensions), integrates multiple source systems, joins faster than long text keys, and permits a reserved **unknown member** (for example key -1) so facts with a missing dimension still load and inner joins do not silently drop them.
- **Degenerate dimension:** an identifier kept in the fact table with no dimension table (shipment id, PO number, invoice number).
- **Late-arriving dimension:** a fact arrives before its dimension row; load an **inferred member** placeholder and update it when the real row arrives.
- **Date dimension:** one row per calendar day with attributes (month, quarter, weekday, weekend flag, holiday flag, fiscal period). It is generated, not extracted. For India the **fiscal year runs April to March**, so a date dimension should carry both calendar and fiscal attributes, for example 31 March 2025 falls in FY2024-25 and 1 April 2025 in FY2025-26 (April to June is fiscal Q1).

### Example
Generate a date dimension for 2025 with the Indian fiscal year in PostgreSQL (tested on PostgreSQL 16):
```sql
CREATE TABLE dim_date AS
SELECT TO_CHAR(d, 'YYYYMMDD')::int AS date_key, d::date AS full_date,
       EXTRACT(YEAR FROM d)::int AS cal_year, EXTRACT(MONTH FROM d)::int AS month_no, TO_CHAR(d, 'Mon') AS month_name,
       EXTRACT(ISODOW FROM d)::int AS iso_dow, (EXTRACT(ISODOW FROM d) >= 6) AS is_weekend,
       'FY' || CASE WHEN EXTRACT(MONTH FROM d) >= 4 THEN EXTRACT(YEAR FROM d)::int ELSE EXTRACT(YEAR FROM d)::int - 1 END
            || '-' || RIGHT((CASE WHEN EXTRACT(MONTH FROM d) >= 4 THEN EXTRACT(YEAR FROM d)::int + 1
                                  ELSE EXTRACT(YEAR FROM d)::int END)::text, 2) AS fiscal_year,
       ((EXTRACT(MONTH FROM d)::int + 8) % 12) / 3 + 1 AS fiscal_quarter
FROM generate_series('2025-01-01'::date, '2025-12-31'::date, interval '1 day') AS g(d);
ALTER TABLE dim_date ADD PRIMARY KEY (date_key);

SELECT full_date, fiscal_year, fiscal_quarter FROM dim_date
WHERE full_date IN ('2025-03-31', '2025-04-01', '2025-07-01', '2025-10-01', '2025-12-31') ORDER BY 1;
-- 2025-03-31 FY2024-25 Q4 | 2025-04-01 FY2025-26 Q1 | 2025-07-01 FY2025-26 Q2 | 2025-10-01 FY2025-26 Q3 | 2025-12-31 FY2025-26 Q3
```
The table has 365 rows (2025 is not a leap year). The integer `date_key` in `YYYYMMDD` form is readable and sortable, and is the one case where a meaningful surrogate is conventional.

### In the news
See news box. dbt-style projects typically generate surrogate keys by hashing business keys (for example MD5 or SHA over key columns) so that models can be built in parallel without a central sequence, a pattern shared with data vault.

### Interview angle
> [!question] How it is asked
> "Why use surrogate keys instead of natural keys? What is a degenerate dimension? How do you design a date dimension?"

> [!tip] Strong answer includes
> - Surrogate keys: stability, versioning for SCD, multi-source integration, performance, unknown member
> - Degenerate dimension with an example (PO number in the fact)
> - Date dimension generated in advance with calendar and fiscal attributes (April to March for India)
> - Late-arriving dimensions handled with inferred members
> - Notes that surrogate keys must be resolved during the fact load (lookup by natural key and effective date)

---
## 6. Slowly Changing Dimensions: Types 0, 1, 2 and 3
> 🟠 Tier 2 · _Key points:_ Type 0 fixed, Type 1 overwrite, Type 2 new row with validity dates, Type 3 previous-value column

### Definition
Dimension attributes change over time (a supplier is re-rated, a customer moves city, a SKU is reclassified). **Slowly changing dimension (SCD)** types define how the warehouse records the change:

| Type | Treatment | History kept? | Use when |
|---|---|---|---|
| 0 | Retain original; never update | Original only | Facts about origin (first purchase date, original credit score) |
| 1 | Overwrite the old value | No | Corrections, attributes where history is irrelevant (typo fix) |
| 2 | Add a new row with validity dates and a current flag | Full | History matters for analysis (supplier rating at time of order) |
| 3 | Add a column holding the previous value | One prior value | A single "old vs new" comparison (before and after a sales-region reorganisation) |

A **Type 2** row has: surrogate key, natural key, tracked attributes, `valid_from`, `valid_to` (a high date such as 9999-12-31 for the current row) and `is_current`. Facts reference the surrogate key valid **at the event date**, so history is preserved in reports. Enforce "only one current row per natural key" with a partial unique index.

### Example
Type 2 supplier dimension plus Type 1 and Type 3 examples (PostgreSQL 16, tested). Sahyadri Components is initially rated tier B; a Type 1 fix corrects a name later and a Type 3 column tracks a sales-region change:
```sql
CREATE TABLE dim_product (
  product_sk INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, product_id TEXT NOT NULL UNIQUE,
  product_name TEXT, category TEXT, unit_cost NUMERIC(10,2));
INSERT INTO dim_product (product_id, product_name, category, unit_cost)
VALUES ('P1','USB Cable','Electronics',40), ('P2','Charger','Electronics',150);

CREATE TABLE dim_supplier (
  supplier_sk INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, supplier_id TEXT NOT NULL, supplier_name TEXT,
  city TEXT, rating_tier TEXT,
  valid_from DATE NOT NULL, valid_to DATE NOT NULL DEFAULT '9999-12-31', is_current BOOLEAN NOT NULL DEFAULT TRUE);
CREATE UNIQUE INDEX one_current_row ON dim_supplier (supplier_id) WHERE is_current;
INSERT INTO dim_supplier (supplier_id, supplier_name, city, rating_tier, valid_from)
VALUES ('S01','Sahyadri Components','Pune','B','2024-01-01'), ('S03','Metro Traders','Mumbai','A','2024-01-01');

-- Type 3: keep one previous value (sales-region reorganisation)
CREATE TABLE dim_customer (
  customer_sk INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, customer_id TEXT UNIQUE, customer_name TEXT,
  sales_region TEXT, prev_sales_region TEXT);
INSERT INTO dim_customer (customer_id, customer_name, sales_region) VALUES ('C001','Asha Retail','West'), ('C002','Ravi Traders','South');
UPDATE dim_customer SET prev_sales_region = sales_region, sales_region = 'West-1' WHERE customer_id = 'C001';
SELECT customer_id, sales_region, prev_sales_region FROM dim_customer ORDER BY 1;
-- C001 West-1 (was West) | C002 South (no previous value)
```
Type 1 is a plain `UPDATE` (for example `UPDATE dim_supplier SET supplier_name = 'Sahyadri Components Pvt Ltd' WHERE supplier_id = 'S01'`); it rewrites every version of that supplier, so reports for past periods change too. Type 0 is simply "never update this column" (enforce with permissions or by excluding the column from the update step of the load).

### In the news
See news box. In dbt, Type 2 history is commonly implemented with snapshots that detect changes and maintain validity columns, so these concepts translate directly into the tools used in practice.

### Interview angle
> [!question] How it is asked
> "Explain slowly changing dimensions. A supplier's rating changed; how do you keep history so old purchase orders show the old rating?"

> [!tip] Strong answer includes
> - Types 0, 1, 2, 3 defined with one supply-chain example each
> - Type 2 mechanics: new row, validity dates, current flag, surrogate key resolved by event date
> - Trade-offs: Type 2 grows the dimension and complicates joins; Type 1 loses history silently
> - Chooses the type per attribute, not per table
> - Mentions a partial unique index or constraint to guarantee one current row

---
## 7. SCD Types 4, 5, 6, 7 and Implementing Type 2 in SQL
> 🟠 Tier 2 · _Key points:_ mini-dimensions, hybrid Type 6, Type 7 dual keys, two-step Type 2 load, as-of surrogate key lookup

### Definition
Advanced types combine the basics:
- **Type 4 (mini-dimension):** move rapidly changing attributes (customer age band, spend band) into a small separate dimension; the fact table carries both the customer key and the mini-dimension key. (Some texts use "Type 4" for a separate **history table** that holds old rows while the main table keeps only current data.)
- **Type 5:** a mini-dimension plus a Type 1 outrigger on the base dimension pointing to the current profile.
- **Type 6 (hybrid 1+2+3):** Type 2 rows plus an extra column holding the **current** value of the tracked attribute on every row (updated Type 1 style), so you can report by "rating at the time" or "rating today".
- **Type 7:** the fact carries both the as-of surrogate key and the durable natural key; a "current" view of the dimension then supports both views of history without a Type 6 column.

**Implementing Type 2** from a staging table of today's source data is a two-step, set-based pattern inside one transaction: (1) **close** the current row where any tracked attribute differs (`valid_to` = effective date minus one day, `is_current` false); (2) **insert** a new current row for changed and new natural keys. (A single `MERGE` cannot update and insert for the same source row, which is why the two-step form, or a `MERGE` over a union of "changed" and "new" rows, is used.) Compare tuples with `IS DISTINCT FROM` so NULLs are handled. When loading facts, look up the surrogate key where the event date falls between `valid_from` and `valid_to`.

### Example
Staging holds today's supplier master: S01 is now rated A (changed), S02 is new, S03 is unchanged. Effective date 1 April 2025. This continues the tables of sub-topic 6:
```sql
CREATE TABLE stg_supplier (supplier_id TEXT, supplier_name TEXT, city TEXT, rating_tier TEXT);
INSERT INTO stg_supplier VALUES
 ('S01','Sahyadri Components','Pune','A'), ('S02','Delta Packaging','Nashik','B'), ('S03','Metro Traders','Mumbai','A');

BEGIN;
UPDATE dim_supplier d SET valid_to = DATE '2025-04-01' - 1, is_current = FALSE         -- 1) close changed rows
FROM stg_supplier s
WHERE d.supplier_id = s.supplier_id AND d.is_current
  AND (d.city, d.rating_tier) IS DISTINCT FROM (s.city, s.rating_tier);

INSERT INTO dim_supplier (supplier_id, supplier_name, city, rating_tier, valid_from)    -- 2) open new current rows
SELECT s.supplier_id, s.supplier_name, s.city, s.rating_tier, DATE '2025-04-01'
FROM stg_supplier s
LEFT JOIN dim_supplier d ON d.supplier_id = s.supplier_id AND d.is_current
WHERE d.supplier_id IS NULL;
COMMIT;

SELECT supplier_sk, supplier_id, rating_tier, valid_from, valid_to, is_current FROM dim_supplier ORDER BY supplier_id, valid_from;
-- 1 S01 B 2024-01-01 2025-03-31 f | 3 S01 A 2025-04-01 9999-12-31 t | 4 S02 B 2025-04-01 9999-12-31 t | 2 S03 A 2024-01-01 9999-12-31 t
```
S03 is untouched; S01 now has two versions (keys 1 and 3). Run the load again and nothing changes: after the first run no current row differs from staging, so both statements affect zero rows, which makes the job **idempotent**.

Type 4 mini-dimension and Type 7 current view:
```sql
-- Type 4: rapidly changing customer profile held in a small separate dimension
CREATE TABLE dim_customer_profile (profile_sk INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, spend_band TEXT, order_freq_band TEXT);
-- fact rows carry customer_sk AND profile_sk (profile as of the transaction)

-- Type 7: the as-of key lives in the fact; durable key + current view gives "today's attributes"
CREATE VIEW dim_supplier_current AS SELECT * FROM dim_supplier WHERE is_current;
```

### In the news
See news box. dbt snapshots, Delta Lake and Iceberg `MERGE` support and warehouse-native change tracking make Type 2 loads routine, but hand-written SQL like this remains the common interview question.

### Interview angle
> [!question] How it is asked
> "Write the SQL to maintain a Type 2 dimension from a staging table." / "What is a Type 6 dimension? When would you use a mini-dimension?"

> [!tip] Strong answer includes
> - Two-step close-then-insert in one transaction, with `IS DISTINCT FROM` for NULL-safe comparison
> - Idempotent load (rerun produces no change) and one-current-row constraint
> - Fact load resolves the surrogate key by effective date
> - Type 6 or 7 to support "as-was" and "as-is" reporting
> - Mini-dimension for fast-changing attributes so the main dimension does not explode

---
## 8. Modelling a Supply-Chain Warehouse: Inventory Snapshot, Shipment and PO Facts
> 🟠 Tier 2 · _Key points:_ three fact types in one bus, conformed dimensions, KPI queries (inventory, OTIF, lead time), spend by supplier rating at PO time

### Definition
A supply-chain mart usually has three core facts around shared dimensions (date, product, location, supplier, carrier):
- **`fact_inventory_snapshot`** (periodic snapshot; grain: product x location x day). Measures: on-hand quantity, inventory value. Semi-additive.
- **`fact_shipment`** (transaction; grain: shipment line). Measures: quantity ordered and delivered, freight cost. Three role-played dates (ship, promised, delivery). On-time and in-full are derived.
- **`fact_po_line`** (accumulating snapshot; grain: PO line). Dates for PO, promised receipt and actual receipt (NULL until received), ordered and received quantity, PO value, supplier key as of the PO date.

KPI definitions used here: OTIF at shipment level (delivered by the promised date **and** delivered quantity at least the ordered quantity), fill rate (received / ordered), lead time (receipt date minus PO date), freight per unit (total freight / total units delivered). More KPI context is in [[012 Supply Chain Analytics & KPIs]], [[061 SQL for SCM & Business Analytics]] and the SAP-side sources in [[085 SAP Reporting & Analytics]].

### Example
Continue from the dimension tables above (dates from sub-topic 5, products and suppliers from sub-topics 6 and 7). Add locations, carriers and the three facts, then run KPI queries. All SQL was executed on PostgreSQL 16.
```sql
CREATE TABLE dim_location (location_sk INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, location_id TEXT NOT NULL UNIQUE,
  location_name TEXT, city TEXT, state TEXT, location_type TEXT);
CREATE TABLE dim_carrier (carrier_sk INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY, carrier_id TEXT UNIQUE, carrier_name TEXT, mode TEXT);
INSERT INTO dim_location (location_id, location_name, city, state, location_type) VALUES
 ('W-PUNE','Pune DC','Pune','Maharashtra','WAREHOUSE'), ('W-NSK','Nashik DC','Nashik','Maharashtra','WAREHOUSE'),
 ('S-MUM','Mumbai Store','Mumbai','Maharashtra','STORE');
INSERT INTO dim_carrier (carrier_id, carrier_name, mode) VALUES ('C1','BlueLine Roadways','ROAD'), ('C2','RailFreight Co','RAIL');

CREATE TABLE fact_inventory_snapshot (
  date_key INT REFERENCES dim_date, product_sk INT REFERENCES dim_product, location_sk INT REFERENCES dim_location,
  on_hand_qty INT NOT NULL, inventory_value NUMERIC(14,2) NOT NULL, PRIMARY KEY (date_key, product_sk, location_sk));
INSERT INTO fact_inventory_snapshot
SELECT d.date_key, p.product_sk, l.location_sk, v.q, v.q * p.unit_cost
FROM (VALUES
 ('2025-04-01','P1','W-PUNE',100), ('2025-04-01','P1','W-NSK',40), ('2025-04-01','P2','W-PUNE',30), ('2025-04-01','P2','W-NSK',20),
 ('2025-04-02','P1','W-PUNE',90),  ('2025-04-02','P1','W-NSK',40), ('2025-04-02','P2','W-PUNE',25), ('2025-04-02','P2','W-NSK',20),
 ('2025-04-03','P1','W-PUNE',80),  ('2025-04-03','P1','W-NSK',35), ('2025-04-03','P2','W-PUNE',25), ('2025-04-03','P2','W-NSK',10)
) AS v(d, pid, lid, q)
JOIN dim_date d ON d.full_date = v.d::date JOIN dim_product p ON p.product_id = v.pid JOIN dim_location l ON l.location_id = v.lid;

-- Semi-additive: sum across product and location for a date, then AVERAGE across dates
SELECT d.full_date, SUM(f.on_hand_qty) AS units, SUM(f.inventory_value) AS value
FROM fact_inventory_snapshot f JOIN dim_date d USING (date_key) GROUP BY d.full_date ORDER BY d.full_date;
-- 190 13100.00 | 175 11950.00 | 150 9850.00
SELECT ROUND(AVG(daily_value), 2) AS avg_inventory_value
FROM (SELECT date_key, SUM(inventory_value) AS daily_value FROM fact_inventory_snapshot GROUP BY date_key) t;   -- 11633.33
```
Shipment transaction fact and OTIF by carrier:
```sql
CREATE TABLE fact_shipment (
  shipment_id TEXT PRIMARY KEY, ship_date_key INT REFERENCES dim_date, promised_date_key INT REFERENCES dim_date,
  delivery_date_key INT REFERENCES dim_date, product_sk INT REFERENCES dim_product, origin_sk INT REFERENCES dim_location,
  dest_sk INT REFERENCES dim_location, carrier_sk INT REFERENCES dim_carrier, qty_ordered INT, qty_delivered INT, freight_cost NUMERIC(10,2));
INSERT INTO fact_shipment
SELECT v.sid, ds.date_key, dp.date_key, dd.date_key, p.product_sk, o.location_sk, t.location_sk, c.carrier_sk, v.qo, v.qd, v.fc
FROM (VALUES
 ('SH-001','2025-04-02','2025-04-04','2025-04-04','P1','W-PUNE','S-MUM','C1',50,50,3000),
 ('SH-002','2025-04-02','2025-04-04','2025-04-05','P2','W-PUNE','S-MUM','C1',20,20,1800),
 ('SH-003','2025-04-03','2025-04-06','2025-04-05','P1','W-NSK','S-MUM','C2',40,36,2100),
 ('SH-004','2025-04-05','2025-04-08','2025-04-08','P2','W-NSK','S-MUM','C1',10,10,1500),
 ('SH-005','2025-04-07','2025-04-09','2025-04-10','P1','W-PUNE','S-MUM','C2',60,60,2400),
 ('SH-006','2025-04-08','2025-04-11','2025-04-10','P2','W-PUNE','S-MUM','C1',15,15,1650)
) AS v(sid, sd, pd, dd, pid, oid, tid, cid, qo, qd, fc)
JOIN dim_date ds ON ds.full_date = v.sd::date JOIN dim_date dp ON dp.full_date = v.pd::date JOIN dim_date dd ON dd.full_date = v.dd::date
JOIN dim_product p ON p.product_id = v.pid JOIN dim_location o ON o.location_id = v.oid
JOIN dim_location t ON t.location_id = v.tid JOIN dim_carrier c ON c.carrier_id = v.cid;

SELECT c.carrier_name, COUNT(*) AS shipments,
       SUM((f.delivery_date_key <= f.promised_date_key)::int) AS on_time,
       SUM((f.qty_delivered >= f.qty_ordered)::int) AS in_full,
       SUM((f.delivery_date_key <= f.promised_date_key AND f.qty_delivered >= f.qty_ordered)::int) AS otif,
       ROUND(100.0 * SUM((f.delivery_date_key <= f.promised_date_key AND f.qty_delivered >= f.qty_ordered)::int) / COUNT(*), 1) AS otif_pct,
       SUM(f.freight_cost) AS freight, SUM(f.qty_delivered) AS units,
       ROUND(SUM(f.freight_cost) / SUM(f.qty_delivered), 2) AS freight_per_unit
FROM fact_shipment f JOIN dim_carrier c USING (carrier_sk) GROUP BY c.carrier_name ORDER BY c.carrier_name;
-- BlueLine Roadways: 4 shipments, 3 on time, 4 in full, 3 OTIF (75.0%), freight 7950, 95 units, 83.68 per unit
-- RailFreight Co:    2 shipments, 1 on time, 1 in full, 0 OTIF (0.0%),  freight 4500, 96 units, 46.88 per unit
```
Reading the result: rail is cheaper per unit but had no OTIF shipment (one late, one short), a trade-off a carrier review would discuss. Comparing `date_key` integers works because `YYYYMMDD` keys sort like dates.

PO accumulating snapshot, with the supplier version resolved as of the PO date (this is the Type 2 payoff):
```sql
CREATE TABLE fact_po_line (
  po_number TEXT, line_no INT, supplier_sk INT REFERENCES dim_supplier, product_sk INT REFERENCES dim_product,
  po_date_key INT REFERENCES dim_date, promised_date_key INT REFERENCES dim_date, received_date_key INT REFERENCES dim_date,
  ordered_qty INT, received_qty INT, po_value NUMERIC(14,2), PRIMARY KEY (po_number, line_no));
INSERT INTO fact_po_line
SELECT v.po, 1, s.supplier_sk, p.product_sk, dpo.date_key, dpr.date_key, drc.date_key, v.oq, v.rq, v.val
FROM (VALUES
 ('PO-501','S01','P1','2025-03-20','2025-03-27','2025-03-27',500,500,20000),
 ('PO-502','S01','P2','2025-04-10','2025-04-17','2025-04-19',100,90,15000),
 ('PO-503','S02','P1','2025-04-12','2025-04-19',NULL,300,NULL,12000),
 ('PO-504','S03','P2','2025-04-15','2025-04-22','2025-04-22',80,80,12000)
) AS v(po, sid, pid, pod, prd, rcd, oq, rq, val)
JOIN dim_supplier s ON s.supplier_id = v.sid AND v.pod::date BETWEEN s.valid_from AND s.valid_to   -- as-of lookup
JOIN dim_product p ON p.product_id = v.pid
JOIN dim_date dpo ON dpo.full_date = v.pod::date JOIN dim_date dpr ON dpr.full_date = v.prd::date
LEFT JOIN dim_date drc ON drc.full_date = v.rcd::date;

-- Spend by the rating the supplier had when the PO was placed
SELECT s.rating_tier, SUM(f.po_value) AS spend FROM fact_po_line f JOIN dim_supplier s USING (supplier_sk) GROUP BY s.rating_tier ORDER BY 1;
-- A 27000 (PO-502 15000 + PO-504 12000) | B 32000 (PO-501 20000 + PO-503 12000)
-- If ratings had been overwritten (Type 1): S01 would count as A on both POs, giving A 47000 and B 12000, a wrong history.

-- Accumulating snapshot: PO-503 is open (no received date); it gets updated when goods arrive
SELECT po_number FROM fact_po_line WHERE received_date_key IS NULL;                      -- PO-503
UPDATE fact_po_line SET received_date_key = 20250420, received_qty = 280 WHERE po_number = 'PO-503';

SELECT s.supplier_id, COUNT(*) AS pos, ROUND(AVG(dr.full_date - dp.full_date), 1) AS avg_lead_days,
       ROUND(100.0 * SUM(f.received_qty) / SUM(f.ordered_qty), 1) AS fill_pct
FROM fact_po_line f JOIN dim_supplier s USING (supplier_sk)
JOIN dim_date dp ON dp.date_key = f.po_date_key JOIN dim_date dr ON dr.date_key = f.received_date_key
GROUP BY s.supplier_id ORDER BY 1;
-- S01 2 POs, 8.0 days, 98.3% | S02 1 PO, 8.0 days, 93.3% | S03 1 PO, 7.0 days, 100.0%
```
S01 lead time: PO-501 is 7 days (20 to 27 March) and PO-502 is 9 days (10 to 19 April), average 8.0; fill (500 + 90) / (500 + 100) = 98.3%. Open POs have no receipt date yet, so the inner joins to the receipt date drop them from the lead-time average until the goods arrive.

### In the news
See news box. These three facts are the typical targets of ELT jobs from ERP and WMS extracts; open table formats let them sit in a lakehouse and still be queried with warehouse-style SQL.

### Interview angle
> [!question] How it is asked
> "Design a data warehouse for a supply chain: inventory, shipments and purchase orders. What are the facts, dimensions and grain? How do you handle a supplier's rating changing?"

> [!tip] Strong answer includes
> - Three fact types matched to the process: periodic snapshot (inventory), transaction (shipment), accumulating snapshot (PO)
> - Grain declared for each; conformed date, product and location dimensions
> - Semi-additive handling of inventory (sum across space, average across time)
> - Type 2 supplier dimension with as-of key lookup so history is correct
> - KPI formulas at the right grain (OTIF per shipment, weighted fill rate and freight per unit)

---
## 9. Data Vault, Inmon vs Kimball and One-Big-Table Designs
> 🟠 Tier 2 · _Key points:_ hubs, links, satellites, auditability, raw vs business vault, when to choose

### Definition
**Data Vault** (Dan Linstedt) is a modelling pattern for the integration layer of an enterprise warehouse, built for auditability, change tolerance and parallel loading:
- **Hub:** one row per unique business key (supplier number, product SKU), with a hash key, load timestamp and record source. Hubs hold no descriptive data.
- **Link:** one row per relationship between hubs (supplier supplies product; PO line connects PO, product and supplier). Links make many-to-many the default.
- **Satellite:** descriptive attributes of a hub or link, **insert-only with history** (a new row per change, keyed by hub key and load time), so every version and its source are preserved.

A **raw vault** stores source data unaltered; a **business vault** adds derived rules; **information marts** (usually star schemas) are built on top for reporting. Strengths: full lineage and history, easy to add sources, loads parallelise. Costs: many more tables and joins, steeper learning curve, a mart layer is still needed. It suits large regulated enterprises with many source systems; it is overkill for a single-team analytics project.

**Other styles:** **Inmon** builds a normalised enterprise warehouse first and derives marts (top-down); **Kimball** builds conformed dimensional marts directly (bottom-up, the bus); a **one big table (OBT)** denormalises everything into one wide table for a BI tool, trading flexibility and storage for query simplicity. Modern ELT teams often use a layered pattern: staging, intermediate models, then star-schema marts (see sub-topic 10).

### Example
A minimal vault for suppliers (PostgreSQL 16, tested). The satellite keeps every version; the "current view" takes the latest row per hub key:
```sql
CREATE TABLE hub_supplier (supplier_hk CHAR(32) PRIMARY KEY, supplier_bk TEXT NOT NULL UNIQUE, load_dts TIMESTAMP NOT NULL, record_source TEXT NOT NULL);
CREATE TABLE sat_supplier_details (
  supplier_hk CHAR(32) REFERENCES hub_supplier, load_dts TIMESTAMP NOT NULL, city TEXT, rating_tier TEXT, record_source TEXT NOT NULL,
  PRIMARY KEY (supplier_hk, load_dts));
CREATE TABLE link_po_supplier (link_hk CHAR(32) PRIMARY KEY, po_bk TEXT NOT NULL, supplier_hk CHAR(32) REFERENCES hub_supplier,
  load_dts TIMESTAMP NOT NULL, record_source TEXT NOT NULL);

INSERT INTO hub_supplier VALUES (MD5('S01'), 'S01', '2024-01-01', 'ERP');
INSERT INTO sat_supplier_details VALUES
 (MD5('S01'), '2024-01-01', 'Pune', 'B', 'ERP'),
 (MD5('S01'), '2025-04-01', 'Pune', 'A', 'ERP');
INSERT INTO link_po_supplier VALUES (MD5('PO-501|S01'), 'PO-501', MD5('S01'), '2025-03-20', 'ERP');

SELECT h.supplier_bk, s.city, s.rating_tier, s.load_dts
FROM hub_supplier h
JOIN LATERAL (SELECT * FROM sat_supplier_details x WHERE x.supplier_hk = h.supplier_hk ORDER BY x.load_dts DESC LIMIT 1) s ON TRUE;
-- S01 Pune A 2025-04-01 (the older B row is retained in the satellite)
```
The hash of the business key (`MD5('S01')`) lets hubs, links and satellites load independently and in parallel, without lookups.

### In the news
See news box. Snowflake's mention of Open Semantic Interchange and the Fivetran and dbt "Agents Schema" show the industry moving the semantic (business meaning) layer into open formats; the vault answers a different question (auditable raw integration) but sits in the same stack.

### Interview angle
> [!question] How it is asked
> "What is a data vault? How does it differ from a star schema? Inmon vs Kimball?"

> [!tip] Strong answer includes
> - Hubs (business keys), links (relationships), satellites (history) with the purpose of each
> - Vault is an integration and audit layer; stars are the presentation layer
> - Trade-offs: flexibility and lineage vs more tables and joins
> - Inmon top-down normalised vs Kimball bottom-up dimensional, and that many firms mix them
> - Picks based on scale, regulation and number of sources

---
## 10. ETL vs ELT, Layered Pipelines and Change Data Capture
> 🟠 Tier 2 · _Key points:_ transform before vs after load, bronze-silver-gold, incremental loads, CDC, idempotency, orchestration

### Definition
**ETL** extracts data from sources, **transforms** it on a separate processing server, then loads the finished tables into the warehouse. **ELT** loads raw data into the warehouse or lakehouse first and transforms it **inside** the platform with SQL, using its scalable compute. ELT became the default with cloud warehouses because storage is cheap, transformations are version-controlled SQL (dbt), raw data stays available for reprocessing, and analysts can contribute. ETL still fits sensitive data that must be masked before landing, legacy tools, and streaming or heavy non-SQL processing.

**Layered (medallion) design:** **bronze** (raw, as received, append-only), **silver** (cleaned, de-duplicated, typed, conformed keys), **gold** (business-ready star schemas and aggregates). Other vocabularies: staging, intermediate, marts.

**Loading patterns:** full refresh (small tables), **incremental** (only new or changed rows, using a high-water mark such as `updated_at`) and **change data capture (CDC)** (reading the source's transaction log to capture inserts, updates and deletes). Good pipelines are **idempotent** (a rerun yields the same result), handle late-arriving data, validate quality at each layer (row counts, uniqueness, not-null, referential integrity) and are scheduled and monitored by an orchestrator (Airflow, Dagster, Azure Data Factory, dbt Cloud). Data quality rules: [[175 Data Quality, Master Data & Data Governance]]; the SAP side of extraction: [[085 SAP Reporting & Analytics]].

### Example
A bronze-to-silver step in SQL: keep the latest record per order line from an append-only landing table and cast types (tested on PostgreSQL 16):
```sql
CREATE TABLE bronze_shipments (shipment_id TEXT, qty TEXT, status TEXT, updated_at TIMESTAMP, loaded_at TIMESTAMP DEFAULT now());
INSERT INTO bronze_shipments (shipment_id, qty, status, updated_at) VALUES
 ('SH-9','40','CREATED','2025-04-01 09:00'), ('SH-9','40','DISPATCHED','2025-04-02 11:00'),
 ('SH-10','25','CREATED','2025-04-02 10:00'), ('SH-9','38','DELIVERED','2025-04-04 16:30');

CREATE TABLE silver_shipments AS
SELECT shipment_id, qty::int AS qty, status, updated_at
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY shipment_id ORDER BY updated_at DESC) AS rn FROM bronze_shipments) t
WHERE rn = 1;

SELECT * FROM silver_shipments ORDER BY shipment_id;
-- SH-10 25 CREATED 2025-04-02 10:00 | SH-9 38 DELIVERED 2025-04-04 16:30
```
Four raw rows become two current rows, and the bronze table still holds the full history, so the silver layer can be rebuilt after a rule change. The ranking idiom is the one drilled in [[181 SQL Interview Problem Bank]].

### In the news
See news box. The Fivetran and dbt Labs merger (completed 1 June 2026) joins the "EL" and the "T" of ELT in one company, and the dbt Core v2.0 alpha open-sources the Fusion runtime that compiles and runs this kind of SQL.

### Interview angle
> [!question] How it is asked
> "ETL vs ELT: which would you use and why? How do you load a large table incrementally? What is CDC?"

> [!tip] Strong answer includes
> - Where transformation happens and why ELT suits cloud warehouses
> - Raw layer retained for replay; layered bronze-silver-gold or staging-intermediate-marts
> - Incremental vs full refresh, high-water marks, CDC for deletes, idempotent reruns
> - Data-quality tests between layers and monitoring
> - Cases where ETL is still right (masking before landing, legacy, streaming)

---
## 11. Data Lake, Warehouse and Lakehouse; Open Table Formats
> 🟠 Tier 2 · _Key points:_ schema-on-read vs schema-on-write, lake risks, ACID on object storage, Delta, Iceberg, Hudi, choosing

### Definition
- **Data warehouse:** structured, modelled data with **schema-on-write**, strong governance and fast SQL; proprietary or managed storage; best for BI and reporting.
- **Data lake:** cheap object storage (S3, ADLS, GCS) holding raw files in any format (CSV, JSON, Parquet, images, logs) with **schema-on-read**; flexible and cheap for data science, but without table-level guarantees it can degrade into a "data swamp" (no schema enforcement, no ACID, unclear ownership).
- **Lakehouse:** lake storage plus a **table-format layer** that adds warehouse features: ACID transactions, schema enforcement and evolution, time travel, upserts and deletes (`MERGE`), and engine-neutral SQL. The main **open table formats** are **Delta Lake**, **Apache Iceberg** and **Apache Hudi**; data files are usually **Parquet**. A **catalog** (Unity Catalog, Polaris, AWS Glue, Hive Metastore) tracks tables and permissions.

How to choose: a small team with mostly structured BI needs picks a managed warehouse; heavy ML or unstructured data points to a lakehouse; multi-engine or multi-vendor strategies favour open formats such as Iceberg to avoid lock-in. In practice firms run a lakehouse with star-schema gold tables for BI, which is the dimensional model of sub-topics 2 to 8 on open storage. Related: [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]] and [[172 Tableau & Looker Studio - BI Tool Comparison]].

### Example
Illustrative Spark SQL on an Iceberg table (reference syntax, not executed here), showing why a table format matters: a plain Parquet folder cannot do a safe row-level update, but an Iceberg table can:
```spark-sql
CREATE TABLE gold.fact_shipment (shipment_id STRING, ship_date DATE, qty_delivered INT, freight_cost DECIMAL(10,2))
USING iceberg PARTITIONED BY (months(ship_date));

MERGE INTO gold.fact_shipment t USING silver.shipment_updates s ON t.shipment_id = s.shipment_id
WHEN MATCHED THEN UPDATE SET t.qty_delivered = s.qty_delivered
WHEN NOT MATCHED THEN INSERT *;

SELECT * FROM gold.fact_shipment TIMESTAMP AS OF '2025-04-05 00:00:00';   -- time travel to an earlier snapshot
```
The partition expression `months(ship_date)` is Iceberg's hidden partitioning: queries filter on `ship_date` and the engine prunes partitions without the analyst knowing the layout.

### In the news
See news box. Snowflake (8 April 2026) and Databricks (12 June 2025) both expanded Iceberg support, so an Iceberg table written by one engine can increasingly be read by the other, the practical meaning of "open lakehouse".

### Interview angle
> [!question] How it is asked
> "Data lake vs data warehouse vs lakehouse? Why do companies adopt Iceberg or Delta?"

> [!tip] Strong answer includes
> - Schema-on-write vs schema-on-read and the swamp risk
> - What a table format adds: ACID, schema evolution, time travel, merge, partition evolution
> - Open formats reduce vendor lock-in and allow several engines on one copy of data
> - A pragmatic architecture: raw and silver on the lake, gold star schemas for BI
> - Cost, governance and skills as selection factors

---
## 12. ⭐ Advanced: Metrics and Semantic Layers, and a Modelling Case
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **metrics (semantic) layer** defines business metrics once (OTIF, fill rate, inventory turns, active customers), with their grain, filters and dimensions, and serves them to every tool (BI dashboards, notebooks, spreadsheets, AI assistants). Without it, the same KPI is re-implemented in each report and the numbers disagree. Implementations: dbt's semantic layer (MetricFlow), Cube, LookML, Power BI semantic models and DAX measures ([[044 Power BI & DAX]]), Tableau and Looker Studio data sources ([[172 Tableau & Looker Studio - BI Tool Comparison]]), and warehouse-native semantic views. Snowflake's April 2026 mention of an Open Semantic Interchange and the "Agents Schema" in the dbt and Fivetran announcement show a push to make semantic definitions portable, including for AI agents that generate SQL.

Design principles: define metrics at the **right grain** (OTIF per shipment, not per line, unless that is the agreed definition), store **numerators and denominators**, name the **time dimension** (ship date or delivery date?), document filters (exclude cancelled), assign an owner, and version changes. A simple, tool-neutral way to enforce a single definition is a **view** over the star schema that every report reads. Dashboards and MIS: [[047 MIS & Dashboard Design]].

### Example
One governed definition of OTIF by carrier and month, as a view over the shipment star (PostgreSQL 16, tested). Every dashboard queries the view instead of re-deriving the logic:
```sql
CREATE VIEW metric_otif_by_carrier_month AS
SELECT c.carrier_name, d.cal_year, d.month_no,
       COUNT(*) AS shipments,
       SUM((f.delivery_date_key <= f.promised_date_key AND f.qty_delivered >= f.qty_ordered)::int) AS otif_shipments,
       ROUND(100.0 * SUM((f.delivery_date_key <= f.promised_date_key AND f.qty_delivered >= f.qty_ordered)::int) / COUNT(*), 1) AS otif_pct
FROM fact_shipment f
JOIN dim_carrier c USING (carrier_sk)
JOIN dim_date d ON d.date_key = f.ship_date_key        -- metric is dated by SHIP date (a documented choice)
GROUP BY c.carrier_name, d.cal_year, d.month_no;

SELECT * FROM metric_otif_by_carrier_month ORDER BY carrier_name;
-- BlueLine Roadways 2025 4 | 4 shipments | 3 OTIF | 75.0     RailFreight Co 2025 4 | 2 shipments | 0 OTIF | 0.0
```
Because the percentage is computed from counts inside the view, consumers who aggregate further should re-sum `otif_shipments` and `shipments` rather than average `otif_pct`.

**Modelling case to rehearse (30 seconds each):** "Design a warehouse for a quick-commerce company." Process: order fulfilment. Grain: one row per order line (a transaction fact), plus a daily inventory snapshot per dark store and SKU and an accumulating snapshot for order lifecycle (placed, picked, dispatched, delivered). Dimensions: date (and time of day), customer, product, store, rider, promotion. Type 2 on store attributes and product category, Type 1 on typo fixes. Metrics layer: order fill rate, delivery time (minutes), picking accuracy, stock-out rate. Mention the Blinkit inventory-led shift described in [[061 SQL for SCM & Business Analytics]] as the reason inventory snapshots now sit on the company's own books. Then state the ELT flow (raw events to silver, gold star) and the tests you would run.

### In the news
See news box. Semantic and metrics layers are where warehouse modelling meets AI: agents that write SQL need governed definitions, which is why vendors are publishing open semantic specifications.

### Interview angle
> [!question] How it is asked
> "Different dashboards show different OTIF numbers. How do you fix that?" / "Design the data model for a quick-commerce or supply-chain analytics team."

> [!tip] Strong answer includes
> - Diagnoses causes: different grain, date field, filters or cancellation rules
> - One governed definition in a metrics layer or a shared view, with owner and version
> - Stores numerators and denominators; documents the time dimension and exclusions
> - Walks the case: process, grain, dimensions, facts, SCD choices, loading pattern, tests
> - Links the model to the SQL and KPIs the team will use ([[045 SQL for Operations Analytics]], [[183 Views, Stored Procedures, Triggers & Temporary Tables]])
