---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP Fundamentals & Architecture"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP Fundamentals & Architecture

[[_Index - SAP ERP|SAP ERP]] · [[080 SAP MM — Materials Management]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. What is SAP?]]
2. [[#2. SAP Architecture]]
3. [[#3. SAP Client Concept]]
4. [[#4. SAP Navigation]]
5. [[#5. SAP Organizational Structure]]
6. [[#6. Master Data vs Transactional Data]]
7. [[#7. SAP Document Principle]]
8. [[#8. SAP Roles & Authorization]]
9. [[#9. SAP Fiori]]
10. [[#10. SAP HANA]]
11. [[#11. SAP ECC vs S/4HANA]]
12. [[#12. SAP S/4HANA Key Changes]]
13. [[#13. ⭐ Advanced: SAP Activate & Implementation Approach (Fit-to-Standard)]]
14. [[#14. ⭐ Advanced: Clean Core, SAP BTP & RISE with SAP]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the ECC-to-S/4HANA deadline and cloud-first ERP
> **ECC clock is ticking (Gartner figures, end-2024).** Mainstream maintenance for SAP ERP 6.0 (ECC, EHP 6–8) ends on **31 Dec 2027**, with extended maintenance to **31 Dec 2030**. Gartner estimated only **39% of SAP's ~35,000 ECC customers (~14,000)** had bought S/4HANA transition licences by end-2024, projecting ~17,000 holdouts by 2027. A Horváth study of 200 SAP companies found only **8% of migrations finished on schedule**. ([SoftwareSeni summary](https://www.softwareseni.com/what-sap-ecc-end-of-support-actually-means-and-why-17000-companies-are-not-ready/); secondary source quoting Gartner and Horváth)
> 
> **SAP Q4 2025 results (29 Jan 2026).** Current cloud backlog grew **25% in constant currency (16% reported)**, which analysts saw as short of CEO Klein's earlier "at least 25%" remark, and SAP guided **2026 cloud revenue growth of 23–25%**. SAP said Business AI featured in about two-thirds of Q4 cloud orders. ([Constellation Research](https://www.constellationr.com/insights/news/saps-q4-cloud-backlog-spurs-concerns))
> 
> **GAIL goes live on RISE with SAP (formal launch 25 Jun 2025).** GAIL (India) described itself as the first Maharatna PSU to move from legacy ECC to S/4HANA on cloud, under an initiative called "Navodaya", completed within one year. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. What is SAP?
> 🔴 Tier 1 · _Tracker hint:_ Systems, Applications & Products in Data Processing; German ERP leader; ABAP programming language

### Definition
**SAP** (founded 1972 in Walldorf, Germany by former IBM engineers; German original "Systeme, Anwendungen, Produkte in der Datenverarbeitung") is the world's leading **ERP** vendor. An ERP system is one integrated database and application suite in which finance, procurement, production, sales, warehousing, HR and so on share the same master data and post to each other in real time.

Evolution: R/1 → R/2 (mainframe) → **R/3** (1992, client-server) → **ECC 6.0** (2006) → **S/4HANA** (2015, built only for the HANA database). SAP's own language is **ABAP** (Advanced Business Application Programming), used for reports, enhancements, interfaces, forms and conversions (the "RICEFW" objects consultants talk about). Modern extensions use SAP BTP (Business Technology Platform) and Fiori/UI5.

Key module families:
- **Logistics:** MM (materials), PP (production), SD (sales), WM/EWM (warehouse), QM, PM, LE.
- **Finance:** FI, CO. **HR:** HCM / SuccessFactors.

Why it matters: a transaction in one module (a goods receipt in MM) automatically creates the accounting entry in FI, so the "single version of truth" replaces siloed spreadsheets.

### Example
Tata Motors, Mahindra, Asian Paints, ITC and many PSUs run SAP. In an auto plant, a sales order in SD creates demand, MRP in PP/MM plans the parts, MM buys them, WM stores them, and FI posts every movement. A consultant's job is often to map the client's process to these standard modules (fit-to-standard) and configure the gaps.

### In the news
See news box. GAIL's cloud ECC-to-S/4HANA move shows that Indian PSUs, not only private firms, are replatforming ERP.

### Interview angle
> [!question] How it is asked
> "What is SAP and why do companies use it?" or "Which SAP modules have you worked with, and how do they integrate?"

> [!tip] Strong answer includes
> - ERP definition: one database, integrated modules, real-time postings
> - Module names and one integration example (GR in MM posts to FI)
> - Honest scope: say you know the process and navigation from coursework or training, without claiming project experience you do not have
> - Awareness of the current direction: S/4HANA, cloud (RISE), Fiori

---

## 2. SAP Architecture
> 🔴 Tier 1 · _Tracker hint:_ 3-tier: Presentation (SAP GUI/Fiori) → Application (SAP server) → Database (HANA/Oracle)

### Definition
Classic SAP is a **three-tier client-server architecture**:

| Tier | What runs here | Examples |
|---|---|---|
| Presentation | User interface | SAP GUI, SAP Fiori launchpad in a browser, mobile apps |
| Application | Business logic, executed by ABAP application servers | Dispatcher, work processes (dialog, update, background, enqueue, spool), message server |
| Database | Persistent data | SAP HANA (mandatory for S/4HANA); Oracle, DB2, SQL Server, MaxDB for ECC |

The **dispatcher** queues user requests and hands them to free **work processes**; the **enqueue** process manages locks so that two users cannot change the same document at once. Several application servers can be added to scale horizontally while a single database holds the data. In S/4HANA the Fiori front-end server is often embedded in the same stack.

Typical landscape: **DEV → QAS (test) → PRD**, each a separate system, linked by a transport route.

### Example
You run a stock report in MB52. Your PC (presentation) sends the request to the application server; a dialog work process executes the ABAP, queries the database for stock tables, and returns the result list. If 500 users do this at the same time, adding application servers spreads the load; the database must still be sized to cope.

### In the news
See news box. "RISE with SAP" bundles the application, database (HANA) and infrastructure as a managed cloud service, so customers like GAIL no longer run the lower two tiers themselves.

### Interview angle
> [!question] How it is asked
> "Explain SAP's three-tier architecture" or "What changes in architecture with S/4HANA?"

> [!tip] Strong answer includes
> - The three tiers with named technologies
> - Role of dispatcher and work processes in one sentence
> - DEV-QAS-PRD landscape and why change goes through it
> - S/4HANA: HANA only, Fiori as default UI

---

## 3. SAP Client Concept
> 🔴 Tier 1 · _Tracker hint:_ Client = independent data environment; prod/test/dev clients; client-dependent vs independent data

### Definition
A **client** is the highest organisational unit in an SAP system: a self-contained environment with its own master data, transaction data, user master records and customising. It is identified by a **three-digit number** (e.g. 100, 200, 300) that users enter at logon. Standard clients delivered by SAP include 000 (SAP reference client) and 001; 066 is used by SAP EarlyWatch services.

- **Client-dependent data:** business data and most customising (material masters, vendors, POs, user records, org units). Different in each client.
- **Client-independent data:** shared across all clients in a system: ABAP programs, data dictionary and table definitions, cross-client customising, repository objects.

Client settings are maintained in **SCC4** (role such as production, test, customising; protection against overwrite or comparison), and client copy is **SCCL / SCC1 / SCC9**. Typical use: DEV has a customising client (e.g. 100) and a unit-test client (e.g. 110); QAS has an integration test client; PRD has one live client. A production client is normally locked from direct customising changes.

### Example
In a training system, Client 100 holds the SIOM sample company with plant 1000. If you create material RM-001 in client 100, it does not exist in client 200 of the same system, but both clients run the same ABAP program for MIGO because programs are client-independent.

### In the news
See news box. In a brownfield S/4HANA conversion, the client structure and the clients to be converted are among the first design decisions.

### Interview angle
> [!question] How it is asked
> "What is a client in SAP?" "Is a PO client-dependent or independent?"

> [!tip] Strong answer includes
> - Client = top-level, legally and technically independent business entity inside one system
> - Dependent vs independent examples
> - How clients are used across DEV/QAS/PRD
> - SCC4 and client copy as the tools

---

## 4. SAP Navigation
> 🔴 Tier 1 · _Tracker hint:_ Transaction codes (T-codes); menu path vs T-code; Favorites; SAP Easy Access Menu

### Definition
Users reach a function either by **menu path** in the **SAP Easy Access Menu** (e.g. Logistics → Materials Management → Purchasing → Purchase Order → Create) or by typing a **transaction code (T-code)** in the command field (e.g. `ME21N`). **Favorites** store frequently used transactions.

Command field prefixes:

| Entry | Effect |
|---|---|
| `/nME21N` | Ends the current transaction and opens ME21N |
| `/oME21N` | Opens ME21N in a new session (window) |
| `/n` | Returns to Easy Access |
| `/nex` | Logs off without a prompt |
| `/i` | Deletes the current session |

Useful technical T-codes: `SE16N` (table browser), `SE11` (data dictionary), `SE38` (ABAP editor), `SU53` (last failed authority check), `SM37` (background jobs), `SU01` (users), `SM04` (user list). Press **F4** for input help, **F1** for field help (technical information shows table and field names). Tip: in the S/4HANA Fiori launchpad, apps are found by search tiles rather than by menu.

### Example
Procurement clerk workflow with T-codes only: `MM03` display material, `ME51N` raise PR, `ME21N` create PO, `MIGO` receive goods, `MIRO` post invoice, `MB52` check stock. Memorising about 20 of these makes you quick in any SAP demo or case.

### In the news
See news box. As companies move to S/4HANA, many users shift from T-codes to Fiori tiles, but consultants and key users still rely on T-codes for support work.

### Interview angle
> [!question] How it is asked
> "Name five T-codes you know and what they do" or "How do you find a table behind a field?"

> [!tip] Strong answer includes
> - T-codes grouped by process (P2P, O2C, PP) rather than a random list
> - /n and /o prefixes
> - F1 then technical information, then SE16N for the table
> - Mention that Fiori apps map to the same underlying functions

---

## 5. SAP Organizational Structure
> 🔴 Tier 1 · _Tracker hint:_ Client → Company Code → Plant → Storage Location → Purchasing Org → Purchasing Group

### Definition
The **enterprise structure** mirrors the legal and operational structure of the business. Each unit is created in configuration and assigned to others.

| Unit | Meaning | Key assignment |
|---|---|---|
| Client | Highest level, whole group | Contains everything |
| Company code | Legal entity with its own balance sheet | Needed for FI postings |
| Plant | Manufacturing site, distribution centre or branch | Assigned to exactly one company code |
| Storage location | Place within a plant where stock is kept | Belongs to one plant; stock is managed per plant and sloc |
| Purchasing organisation | Negotiates conditions with vendors, legally responsible for POs | Assigned to a company code (company-code-specific) or plant, may serve many plants |
| Purchasing group | Buyer or buyer team | Not assigned to the org structure; used for reporting and responsibility |

Related: **Controlling area** (CO), **Business area** (legacy), **Sales area** (sales org + distribution channel + division) in SD, **Shipping point**, **Warehouse number** in WM. Rule of thumb: financial stock value is held at plant (valuation area) level; quantity is split by storage location.

### Example
Company: Ruchi Foods Pvt Ltd (client 100) → company code 1000 (Mumbai entity) → plants 1100 (Pune factory) and 1200 (Nashik factory) → storage locations 0001 raw materials, 0002 finished goods in each plant → purchasing org 1000 serving both plants → purchasing groups 001 packaging, 002 ingredients.

### In the news
See news box. In greenfield implementations such as large PSU rollouts, getting the enterprise structure right is the first design deliverable because changing it later is costly.

### Interview angle
> [!question] How it is asked
> "Explain the SAP organisational structure for procurement" or "Can one plant belong to two company codes?"

> [!tip] Strong answer includes
> - Hierarchy in correct order with a one-line purpose for each
> - One plant maps to one company code; one purchasing org can serve many plants
> - Purchasing group is a buyer, not an org unit in the legal sense
> - A short example with names

---

## 6. Master Data vs Transactional Data
> 🔴 Tier 1 · _Tracker hint:_ Master: Material Master, Vendor Master, Customer Master; Transaction: PO, Sales Order, Production Order

### Definition
**Master data** is relatively stable data about business objects, created once and reused by many transactions. **Transactional data** records business events and changes constantly, copying defaults from master data.

| | Master data | Transactional data |
|---|---|---|
| Examples | Material master (MM01), vendor master, customer master, BOM, routing, work centre, info record | Purchase requisition, PO, goods receipt, sales order, delivery, invoice, production order |
| Change frequency | Low | High |
| Lifecycle | Long-lived, versioned or blocked | Open → closed, documented |
| Risk | Bad master data propagates everywhere (garbage in, garbage out) | Errors affect single documents |

Data quality is therefore a governance task (MDM, approval workflows, duplicate checks). In S/4HANA, customer and vendor are unified under the **Business Partner (BP)** with roles.

### Example
Material master 10000123 "M8 Bolt" has base unit of measure PC and a standard price. When a PO is created for it, the item automatically defaults the unit, plant data, tax code and price. If the master has the wrong lead time (say 30 days instead of 3), MRP will place orders 27 days too early on every run, blowing up inventory.

### In the news
See news box. Migration programs (like GAIL's) spend a large share of effort on cleansing and loading master data.

### Interview angle
> [!question] How it is asked
> "Difference between master data and transactional data?" or "What happens if material master data is wrong?"

> [!tip] Strong answer includes
> - Crisp definition plus three examples of each
> - Impact example (wrong lead time or price)
> - Data governance: ownership, workflows, validation rules
> - S/4HANA Business Partner as a point of difference

---

## 7. SAP Document Principle
> 🔴 Tier 1 · _Tracker hint:_ Every transaction creates a document with unique number; document flow; audit trail

### Definition
In SAP every business event is stored as a **document**: a header (date, user, type) with items, assigned a **unique number** from a number range (often combined with the fiscal year). Documents are **never overwritten or physically deleted** in normal operation; corrections are done by reversal or cancellation documents (e.g. movement type 102 reverses 101), which preserves the **audit trail**.

Document types you meet constantly:
- **Material document** (movement in MM) and **accounting document** (posting in FI), created together from one GR.
- **Purchasing documents:** PR, RFQ, PO, scheduling agreement.
- **Sales documents:** inquiry, quotation, order, delivery, invoice.

**Document flow** links successive documents (e.g. sales order → delivery → invoice → accounting document) and is shown in the order's menu (Environment → Document Flow). Change history sits in change documents (e.g. `ME23N` item changes, field-level `CDHDR/CDPOS` tables).

### Example
GR for PO 4500012345 creates material document 5000000789 (2025) and accounting document 5000001234 (company code 1000, FY 2025). Reversing it via MIGO with movement type 102 creates a new material document that references the original; both stay in the system and the net effect is zero.

### In the news
See news box. Compliance and e-invoicing regimes make immutable, traceable documents more important in cloud ERP.

### Interview angle
> [!question] How it is asked
> "What is the document principle in SAP?" or "A GR was posted wrongly. How do you fix it?"

> [!tip] Strong answer includes
> - Every transaction leaves a numbered, dated, user-stamped document
> - Reversal not deletion, with movement type 102 as an example
> - Document flow as the tool to trace a sales order to invoice
> - Link to audit and statutory compliance

---

## 8. SAP Roles & Authorization
> 🔴 Tier 1 · _Tracker hint:_ Role-based access; T-code SU01 for user management; authorization objects

### Definition
SAP security is **role-based access control (RBAC)**.
- **User master record** (`SU01`): logon ID, password rules, user type, assigned roles.
- **Role** (`PFCG`): a collection of **menu entries** (T-codes, Fiori apps) and **authorizations**. Roles are generated into **profiles** and assigned to users.
- **Authorization object:** a group of **fields** that together protect an action, e.g. `M_BEST_BSA` (PO document type), `M_BEST_EKO` (purchasing org), `M_BEST_WRK` (plant), each with an **activity** field (`ACTVT`: 01 create, 02 change, 03 display).
- **Authorization:** the specific field values granted, e.g. plant 1100, activity 03.

When a user gets "You are not authorized", `SU53` shows the last failed check, which a basis or security consultant uses to fix the role. **Segregation of duties (SoD)** ensures the person who creates a PO cannot also approve the payment; tools like SAP GRC check this.

### Example
A store clerk role: display material (`MM03`), post GR (`MIGO`, activity 01 with movement type 101, plant 1100 only), no `ME21N` change rights. A buyer role: create PO for purchasing org 1000 and plants 1100/1200, but not post invoices in `MIRO`.

### In the news
See news box. During S/4HANA migrations, roles must be redesigned because T-codes are replaced by Fiori apps and catalogs, a typical source of delays.

### Interview angle
> [!question] How it is asked
> "How is access controlled in SAP?" or "A user cannot post a GR. How do you debug it?"

> [!tip] Strong answer includes
> - User, role, authorization object, field value chain
> - SU01, PFCG, SU53
> - Segregation of duties example (PO vs invoice approval)
> - Principle of least privilege

---

## 9. SAP Fiori
> 🔴 Tier 1 · _Tracker hint:_ Modern web/mobile UI; tile-based; role-specific apps; replaces traditional SAP GUI

### Definition
**SAP Fiori** is SAP's user-experience layer built on **SAPUI5/HTML5**: responsive, browser- and mobile-based, with a **launchpad** of **tiles** assigned by role (via catalogs and groups/spaces). Design principles: role-based, adaptive, simple, coherent, delightful.

App types: **transactional** (create PO, post goods movement), **analytical** (KPI tiles with embedded HANA analytics), and **fact sheets** (object overviews with drill-down, search). The **Fiori Apps Reference Library** lists apps with prerequisites. **Fiori elements** generates standard UI from OData services and annotations, reducing custom UI code.

SAP GUI is not obsolete (many T-codes still exist and are used by power users), but new innovations in S/4HANA are delivered as Fiori apps first. Example mappings: `ME21N` → "Create Purchase Order" app; `MIGO` → "Post Goods Movement" app; `VA01` → "Create Sales Order" app.

### Example
A plant manager's launchpad has tiles for "Stock - Multiple Materials" (like MMBE), "Monitor Purchase Order Items" and "Production Order Overview", each with a live count (e.g. 14 overdue POs) that opens the list on click. Previously, they would need three T-codes and a custom report.

### In the news
See news box. SAP's cloud and AI push (Business AI in about two-thirds of Q4 2025 cloud orders) is delivered through the Fiori interface, for example Joule assistants inside apps.

### Interview angle
> [!question] How it is asked
> "What is Fiori and how is it different from SAP GUI?"

> [!tip] Strong answer includes
> - Browser/mobile, tile-based, role-specific, built on SAPUI5
> - Three app types
> - It complements, not entirely replaces, GUI today
> - User-adoption impact: fewer clicks, less training

---

## 10. SAP HANA
> 🔴 Tier 1 · _Tracker hint:_ In-memory database; real-time analytics; column-store; powers SAP S/4HANA

### Definition
**SAP HANA** (High-performance ANalytic Appliance, first released 2010–11) is an **in-memory, column-oriented** relational database that also supports row storage, so OLTP (transactions) and OLAP (analytics) run on the same data copy.

Key technical ideas:
- **In-memory:** data resides in RAM; disk is for persistence and recovery.
- **Column store:** each column is stored contiguously, giving high **compression** and fast aggregation over a few columns.
- **Insert-only / no aggregates:** totals are calculated on the fly instead of maintaining redundant aggregate and index tables, which simplifies the S/4HANA data model.
- **Parallel processing** on multi-core CPUs.
- **Embedded engines:** predictive, spatial, graph, text analytics; **Core Data Services (CDS) views** expose business models.

Why it matters for MM/PP: MRP can be executed in the database (**MRP Live**, `MD01N`), running in minutes what used to take hours in classic ECC MRP (`MD01`).

### Example
A retailer's stock position per material across 5,000 stores: in a row-store system with aggregate tables, the report reads pre-built totals and may be hours out of date; in HANA it can sum the column on demand in seconds, so a planner sees the live number when negotiating a replenishment.

### In the news
See news box. SAP's 2027 ECC deadline is effectively a "move to HANA" deadline, because S/4HANA runs only on HANA.

### Interview angle
> [!question] How it is asked
> "What is SAP HANA and why is it faster?"

> [!tip] Strong answer includes
> - In-memory plus column-store plus compression plus parallelism
> - OLTP and OLAP on one platform
> - Removal of aggregates and the simplified data model
> - A business benefit: MRP Live or real-time reporting

---

## 11. SAP ECC vs S/4HANA
> 🔴 Tier 1 · _Tracker hint:_ ECC = legacy; S/4HANA = simplified tables, HANA-only, new processes; migration journey

### Definition
**ECC 6.0** (2006) runs on any supported database and is a suite of separate components with many redundant tables. **S/4HANA** (4th generation business suite on HANA, 2015) is rebuilt on HANA with a simplified data model and Fiori as the main UI.

| Aspect | ECC | S/4HANA |
|---|---|---|
| Database | Oracle, DB2, SQL Server, HANA | HANA only |
| Finance data | Several tables (FI, CO, asset, ML) | **Universal Journal** `ACDOCA` |
| Material documents | `MKPF` + `MSEG` | `MATDOC` |
| Customer / vendor | Separate masters | Business Partner (BP) |
| Material number | 18 characters | up to 40 |
| MRP | Classic `MD01` | MRP Live `MD01N` |
| UI | SAP GUI | Fiori first |
| Deployment | On-premise | On-premise, private cloud, public cloud |

**Migration paths:** **Greenfield** (new implementation, clean-slate processes), **Brownfield** (system conversion via SUM/DMO, keeping history and customisations), **Selective data transition / bluefield** (hybrid, e.g. company-code or history selection). Prepare using the **Readiness Check** and **Simplification Item Catalog**.

### Example
A manufacturer with 20 years of custom ABAP chooses brownfield to keep history but spends the project cleaning up custom code that touches old tables like `MSEG`. A smaller firm with weak process discipline chooses greenfield, adopts standard processes ("clean core") and migrates only open items and master data.

### In the news
See news box. The ECC deadline (31 Dec 2027 mainstream, 2030 extended) and Gartner's estimate that only 39% of ECC customers had bought S/4HANA licences make this a live consulting market. GAIL's cloud move is a PSU example.

### Interview angle
> [!question] How it is asked
> "A client is on ECC. How would you decide between greenfield and brownfield?"

> [!tip] Strong answer includes
> - Differences: HANA only, universal journal, BP, Fiori, MRP Live
> - Three migration approaches and when to choose each
> - Decision criteria: process maturity, custom code, data volume, downtime, budget
> - The deadline, with the caveat that you checked current dates

---

## 12. SAP S/4HANA Key Changes
> 🔴 Tier 1 · _Tracker hint:_ Simplified material document; single source of truth; embedded analytics; Fiori-first

### Definition
Main functional and data model changes that matter for logistics users:
1. **Simplified material document:** `MATDOC` replaces `MKPF` and `MSEG`, and many aggregate stock tables (e.g. `MARC` history, `MARD` totals) are replaced by calculating from documents. Fewer locks, faster posting.
2. **Single source of truth:** the **Universal Journal** (`ACDOCA`) holds FI, CO, asset and material ledger line items in one table.
3. **Business Partner** replaces separate customer and vendor masters (CVI integration).
4. **Material Ledger and actual costing** are mandatory (price determination).
5. **MRP Live** (`MD01N`) runs in HANA; planning and available-to-promise improvements (advanced ATP).
6. **Embedded analytics:** CDS-based real-time reports within the transactional system; no separate data warehouse needed for operational reports.
7. **Fiori-first UX** and the "**clean core**" principle (extend via side-by-side BTP or in-app key-user extensibility, avoid modifying standard).
8. Optional **embedded EWM and TM**, simplified Credit Management (SAP Credit Management replaces classic SD credit check), and new Product Master length (40 characters).

### Example
Before: month-end reconciliation between FI and CO and the material ledger consumed days because three tables disagreed. After: a single line in `ACDOCA` carries the cost centre, profit centre, material and account, so a plant controller sees stock value and cost impact of a goods movement in one report.

### In the news
See news box. SAP's "Business AI" push (about two-thirds of Q4 2025 cloud orders) sits on top of this unified data model; GAIL is an example of a large Indian enterprise adopting it.

### Interview angle
> [!question] How it is asked
> "What has changed in S/4HANA compared to ECC?"

> [!tip] Strong answer includes
> - Three headline changes: HANA-only, universal journal / simplified data model, Fiori
> - MATDOC, BP, MRP Live as concrete examples
> - Clean-core principle and why it eases upgrades
> - Business impact: faster close, real-time reporting, fewer reconciliations

---

## 13. ⭐ Advanced: SAP Activate & Implementation Approach (Fit-to-Standard)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**SAP Activate** is SAP's implementation methodology combining best practices, tools and content. Phases: **Discover → Prepare → Explore → Realize → Deploy → Run**. In **Explore**, teams run **Fit-to-Standard workshops**: demonstrate the pre-configured standard (SAP Best Practices) to business users and record only the gaps, instead of writing detailed blueprints from scratch as in classic ASAP.

Core principles: configure before customise, **clean core**, agile sprints in Realize, **RICEFW** inventory (Reports, Interfaces, Conversions, Enhancements, Forms, Workflows) managed to stay small, and cut-over planning (data loads, freeze, mock runs) before go-live. Testing layers: unit, integration (SIT), user acceptance (UAT), regression, performance. Change management and training are workstreams in their own right; poor adoption is a common reason for failure.

Consulting metrics: number of gaps vs standard, defect leakage, data quality scores, cut-over duration, hypercare ticket volume.

### Example
A packaging company on RISE: in Explore, 120 scenarios are shown; 95 fit as standard, 18 need configuration, 7 become RICEFW items (e.g. a custom label form and a legacy-MES interface). Keeping the 7 items small keeps upgrade effort low.

### In the news
See news box. Horváth's 8% on-schedule figure is a reminder that scope and data readiness, not technology, decide project outcomes. GAIL reported delivering its S/4HANA cloud go-live within one year.

### Interview angle
> [!question] How it is asked
> "How would you run an ERP implementation?" or "Why do ERP projects fail?"

> [!tip] Strong answer includes
> - Activate phases and fit-to-standard idea
> - Governance: steering committee, scope control, RICEFW budget
> - Data migration, cut-over and testing as critical-path items
> - Change management and super-users; failure causes with a mitigation each

---

## 14. ⭐ Advanced: Clean Core, SAP BTP & RISE with SAP
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Clean core** means keeping the standard ERP free of modifications so upgrades are quick, putting extensions in decoupled layers. Extension options: **in-app (key-user) extensibility** (custom fields, logic), **developer extensibility** (ABAP Cloud, released APIs only) and **side-by-side extensions on SAP BTP** (Business Technology Platform) via events and APIs.

**RISE with SAP** is a commercial bundle: S/4HANA Cloud (private edition) or public edition, infrastructure, technical managed services, BTP credits and process-transformation tools, billed as a subscription. **GROW with SAP** is the equivalent aimed at public-cloud adopters.

Trade-offs: subscription (OPEX) vs perpetual licence plus maintenance (CAPEX); less customisation freedom vs faster upgrades; lock-in to SAP's release cadence vs lower infrastructure burden.

### Example
A company needs a supplier-onboarding portal with approval steps. Instead of modifying standard vendor creation, it builds a BTP app using released business-partner APIs and sends events on approval. After an S/4HANA upgrade the standard code is untouched and the app keeps working.

### In the news
See news box. SAP's cloud backlog and 2026 guidance (cloud revenue growth 23–25% in constant currency) show customers moving to subscription models; GAIL's RISE go-live is the Indian example.

### Interview angle
> [!question] How it is asked
> "What is clean core and why does SAP promote it?" or "Should this client choose RISE or on-premise S/4HANA?"

> [!tip] Strong answer includes
> - Definition of clean core and three extension types
> - Commercial and operational differences between RISE and on-premise
> - Decision criteria: customisation need, regulatory constraints, IT capability, TCO horizon
> - A balanced recommendation with the assumption stated

---
## 🔗 Go deeper: expansion notes
- [[200 SAP S-4HANA Migration, Data Migration & Testing|SAP S-4HANA Migration, Data Migration & Testing]]
- [[201 SAP Landscape, Transports, Security & GRC Basics|SAP Landscape, Transports, Security & GRC Basics]]
- [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows|SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]
