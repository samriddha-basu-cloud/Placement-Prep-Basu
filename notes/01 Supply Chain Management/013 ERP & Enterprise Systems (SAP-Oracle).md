---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "ERP & Enterprise Systems (SAP/Oracle)"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 15
---
# ERP & Enterprise Systems (SAP/Oracle)

⬅ [[012 Supply Chain Analytics & KPIs]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[014 Global SCM & Sustainability]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. ERP Basics]]
2. [[#2. SAP MM (Materials Management)]]
3. [[#3. SAP PP (Production Planning)]]
4. [[#4. SAP SD (Sales & Distribution)]]
5. [[#5. SAP WM/EWM]]
6. [[#6. SAP QM (Quality Management)]]
7. [[#7. Oracle SCM Cloud]]
8. [[#8. ERP Integration Points]]
9. [[#9. Master Data in ERP]]
10. [[#10. Transaction Flows in SAP]]
11. [[#11. ERP Implementation Phases]]
12. [[#12. Change Management in ERP]]
13. [[#13. Analytics from ERP]]
14. [[#14. ⭐ Advanced: S/4HANA vs ECC and "Clean Core"]]
15. [[#15. ⭐ Advanced: ERP Selection, Fit-Gap and TCO]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): The SAP ECC deadline and the S/4HANA migration wave
> **SAP ECC 6 end of mainstream maintenance.** As reported by Rimini Street (a third-party support vendor, so read with that bias in mind), SAP has repeatedly said ECC 6 EHP 0–5 mainstream maintenance ended on **31 Dec 2025**, while EHP 6–8 mainstream maintenance ends **31 Dec 2027**, with extended maintenance available at about two percentage points extra (roughly 9% more cost) through **31 Dec 2030**. In Q1 2025 SAP added an "ERP, private edition, transition option" under RISE for select customers needing support beyond 2030, conditional on moving to HANA by end-2030. ([Rimini Street](https://www.riministreet.com/blog/no-extension-to-ecc-support-2027-deadline/))
>
> **A live implementation (Aug 2025).** Wipro announced it had delivered **RISE with SAP S/4HANA Cloud Private Edition** for Victoria's AusNet energy network within an **18-month** schedule, coordinating **1,600+ users** and **50+ energy retailers** during cutover, with geospatial and mobile field-asset capability. A concrete example of a big-bang style cutover with heavy change management. ([Wipro](https://www.wipro.com/newsroom/press-releases/2025/ausnet-and-wipro-deliver-landmark-energy-sector-transformation-with-sap-s4hana-cloud-implementation/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. ERP Basics
> 🔴 Tier 1 · _Tracker hint:_ Integrated modules, real-time data, single source of truth

### Definition
**Enterprise Resource Planning (ERP)** is an integrated software suite that runs core business processes (finance, procurement, inventory, production, sales, HR) on **one shared database**, so a transaction entered once is visible everywhere (**single source of truth**). Benefits: integration, real-time visibility, standard processes, audit trail and control, reduced duplicate entry. Evolution: MRP → MRP II → ERP → ERP II (extended with SCM and CRM) → cloud/SaaS and in-memory platforms (SAP S/4HANA, Oracle Fusion Cloud).

Architecture: **modules** (MM, SD, PP, FI/CO, QM, WM) share **master data** and **org structure** (client, company code, plant, storage location). Deployment: on-premise, private cloud, public cloud (SaaS). Typical risks: customisation creep, poor data quality, resistance to change, cost and time overruns. Major vendors: SAP, Oracle, Microsoft Dynamics, Infor; Indian mid-market: Tally, Ramco, plus SAP Business One and NetSuite.

### Example
A customer order in SAP SD reserves stock (MM), creates a delivery, reduces inventory on goods issue, posts COGS and revenue automatically to finance (FI), and updates demand signals for planning (PP/MRP), all without re-keying.

### In the news
See news box. The ECC deadline shows that ERP is a long-lived platform decision: companies who bought in the 2000s now face a forced re-platforming.

### Interview angle
> [!question] How it is asked
> "What is ERP and why do companies implement it?" or "What are the risks?"

> [!tip] Strong answer includes
> - Integrated modules on a single database, real-time data
> - Business benefits with a measurable example (order-to-cash cycle, inventory visibility)
> - Risks: cost, customisation, change resistance, data quality
> - Awareness of cloud vs on-premise choices

---

## 2. SAP MM (Materials Management)
> 🔴 Tier 1 · _Tracker hint:_ Purchase requisition, PO, GR/GI, invoice verification, stock mgmt

### Definition
MM covers procurement and inventory. Process (Procure-to-Pay core):

| Step | Typical T-code | Notes |
|---|---|---|
| Purchase requisition (PR) | **ME51N** | Internal demand, can be auto-created by MRP |
| Request for quotation / source determination | ME41, ME47 | Vendor selection, source list, info record ME11 |
| Purchase order (PO) | **ME21N** | Output to vendor; release strategy for approvals |
| Goods receipt (GR) | **MIGO** (movement type 101) | Updates stock and posts accounting |
| Invoice verification (IV) | **MIRO** | Three-way match PO, GR, invoice |
| Stock overview | **MMBE**, MB52 | Material document list: MB51 |
| Goods issue (GI) | MIGO (261 to production order, 201 to cost centre) | Reduces stock |

Material valuation: moving average price (**V**) or standard price (**S**). Accounting entries are automatic through account determination (transaction **OBYC**): GR posts Dr Inventory / Cr GR/IR clearing; IV posts Dr GR/IR / Cr Vendor.

### Example
PO for 100 units at ₹50. GR: Dr Inventory ₹5,000, Cr GR/IR ₹5,000. Invoice with 18% GST: Dr GR/IR ₹5,000, Dr Input GST ₹900, Cr Vendor ₹5,900. Price difference between PO and invoice goes to a price-difference account (for S-priced materials) or adjusts the moving average price.

### In the news
See news box. ECC-to-S/4 projects redesign MM processes too: in S/4HANA the vendor master moves to **Business Partner**, and material documents sit in a simplified table (MATDOC).

### Interview angle
> [!question] How it is asked
> "Walk me through the procure-to-pay process in SAP and what happens in accounting."

> [!tip] Strong answer includes
> - PR → PO → GR → IV → payment with T-codes and documents created
> - Accounting entries (inventory, GR/IR, vendor)
> - Three-way match and tolerances; release strategies
> - Valuation methods (standard vs moving average) and their effect

---

## 3. SAP PP (Production Planning)
> 🔴 Tier 1 · _Tracker hint:_ Demand management, MRP run, production orders, shop floor

### Definition
PP plans and executes manufacturing.

1. **Demand management:** planned independent requirements (**MD61**) from sales forecast, plus customer orders.
2. **MRP run** (**MD01** total planning, MD02 single-item multi-level): explodes demand through the **BOM**, nets against stock and receipts, and creates **planned orders** (in-house) or purchase requisitions (external).
3. **Evaluate:** **MD04** stock/requirements list; convert planned order to **production order** (**CO01**, CO02 change).
4. **Shop floor:** release, reserve and issue components (movement 261), **confirm** operations (**CO11N**), goods receipt of finished goods (101), costs settled in CO.

Net requirement logic:

$$\text{Net} = \text{Gross requirement} - \text{Stock} - \text{Scheduled receipts} + \text{Safety stock}$$

Master data: BOM, routing, work centre, MRP views on the material master (MRP type, lot-size procedure, lead times). Variants: repetitive manufacturing, process industries (PP-PI), and in S/4HANA embedded planning with MRP Live.

### Example
Gross requirement 500, stock 120, scheduled receipts 80, safety stock 50: net = 500 - 120 - 80 + 50 = **350**. With a fixed lot size of 100, MRP creates planned orders for **400** (4 x 100). If each unit needs 2 components at 5% scrap: component requirement = 400 x 2 x 1.05 = **840**.

### In the news
See news box. Planning moves in S/4HANA toward real-time MRP (MRP Live), cutting batch windows, which strengthens the case for migration.

### Interview angle
> [!question] How it is asked
> "Explain how an MRP run works and what it needs to give correct results."

> [!tip] Strong answer includes
> - Inputs: demand, BOM, inventory, lead times, lot-size rules
> - The netting formula and explosion with a numeric example
> - Output: planned orders and purchase requisitions, exception messages in MD04
> - Data quality as the main failure cause (wrong lead times, BOMs)

---

## 4. SAP SD (Sales & Distribution)
> 🔴 Tier 1 · _Tracker hint:_ Sales order, delivery, billing, credit management

### Definition
SD runs order-to-cash.

| Step | T-code | What happens |
|---|---|---|
| Inquiry / quotation | VA11, VA21 | Optional pre-sales documents |
| Sales order | **VA01** | Pricing (condition technique), availability check (ATP), credit check |
| Delivery | **VL01N** | Picking, packing, shipment |
| Post goods issue (PGI) | **VL02N** | Movement type 601: reduces stock, posts COGS |
| Billing | **VF01** | Creates invoice, posts revenue and receivable to FI |
| Payment | F-28 | Customer payment clears receivable |

Key concepts: **pricing procedure** (condition types such as PR00 price, discounts, taxes), **document flow**, **partner functions** (sold-to, ship-to, bill-to, payer), **ATP**, **credit management** (classic **FD32**; in S/4HANA, SAP Credit Management via the business partner), output determination, **third-party and intercompany sales**. GST in India is handled via tax condition types and HSN/SAC codes.

### Example
Order of 200 units at ₹300 with a 5% discount: net price per unit ₹285; value ₹57,000; 18% GST = ₹10,260; invoice ₹67,260. PGI posts Dr COGS / Cr Inventory (at cost, say ₹200 per unit = ₹40,000); billing posts Dr Customer ₹67,260 / Cr Revenue ₹57,000 / Cr Output GST ₹10,260.

### In the news
See news box. Large cutovers (as at AusNet, with 50+ retailers interfacing) show how SD-style external processes (billing and settlement with partners) drive cutover planning.

### Interview angle
> [!question] How it is asked
> "Walk me through order-to-cash in SAP and where credit blocks occur."

> [!tip] Strong answer includes
> - Document chain: order → delivery → PGI → billing → payment
> - Where stock and revenue are posted (PGI vs billing)
> - Pricing, ATP and credit check at order or delivery
> - Typical exceptions: credit block, partial delivery, returns, billing blocks

---

## 5. SAP WM/EWM
> 🔴 Tier 1 · _Tracker hint:_ Warehouse structure, transfer orders, put-away strategies in SAP

### Definition
**WM (Warehouse Management)** gives bin-level management inside a storage location. Structure: **Warehouse number → storage type → storage section → storage bin**. Movements are done with **transfer orders (TO)** created from transfer requirements or posting changes (**LT01** create TO, **LT12** confirm TO, **LS01N** create bin). **Put-away strategies** (fixed bin, open storage, next empty bin, addition to existing stock, bulk storage, near picking bin) and **picking strategies** (FIFO, LIFO, shortest path, FEFO via shelf-life) are set per storage type.

**EWM (Extended Warehouse Management)** is the successor: embedded in S/4HANA or decentralised. It uses **warehouse tasks and warehouse orders**, handles inbound/outbound deliveries, wave management, RF/mobile execution, yard management, labour and resource management, with the monitor via **/SCWM/MON**. SAP has positioned EWM, not classic WM, as the strategic solution for S/4HANA.

### Example
Goods receipt for 40 pallets. Put-away strategy for the "high-rack" storage type is "next empty bin": the system proposes 40 empty bins, creates TOs, and the operator confirms each (LT12). At confirmation, the stock moves from the GR interim storage type to the final bin, giving bin-level accuracy.

### In the news
See news box. In S/4HANA migrations, companies must decide whether to keep classic WM or move to EWM (check SAP's current support statements for WM in S/4HANA), a typical scoping question.

### Interview angle
> [!question] How it is asked
> "How does SAP manage put-away and picking in a warehouse? What is the difference between WM and EWM?"

> [!tip] Strong answer includes
> - Warehouse structure and TO concept with T-codes
> - Put-away and picking strategies and when to use each
> - EWM improvements: WT/WO, wave, yard, labour, deeper automation integration
> - Link to inventory accuracy and KPIs (see [[010 Warehouse Management]])

---

## 6. SAP QM (Quality Management)
> 🔴 Tier 1 · _Tracker hint:_ Inspection lots, usage decisions, QM integration with MM/PP

### Definition
QM manages inspection and quality records. Flow: **inspection plan** (**QP01**, with master inspection characteristics **QS21**) → **inspection lot** created automatically on an event (goods receipt, production order release/confirmation, delivery, or manually with **QA01**) → **results recording** (**QE51N**) → **usage decision (UD)** (**QA11**; accept, reject or accept with deviation) → **stock posting** from quality inspection stock to unrestricted or blocked, with follow-up such as a **quality notification** (**QM01**) and a corrective action.

Integration: **MM**: the QM view in the material master activates inspection type 01 (GR); stock in "quality inspection" status is not available for use. **PP**: in-process inspection at operations and a final inspection before GR of finished goods. **SD**: inspection at delivery or certificates (quality certificates). Sampling procedures and dynamic modification (skip rules) tighten or relax inspection depending on past results (see [[011 Quality Management (TQM)]]).

### Example
100 units are received; an inspection lot with a sample of 8 is created. Two defects found; the acceptance number is 1 → reject. UD "rejected": stock moves from QI stock to blocked stock and a return-to-vendor with a quality notification is raised, so the supplier's quality score drops.

### In the news
See news box. In the Boeing audit story (see the Quality note), the issue was missing process documentation that would have triggered inspection, a reminder that system-triggered inspection plans, like those in QM, exist to remove that human-memory dependence.

### Interview angle
> [!question] How it is asked
> "How is quality inspection integrated with procurement in SAP?"

> [!tip] Strong answer includes
> - Inspection plan → lot → results → usage decision → stock posting
> - Triggers (GR, production, delivery) and QI stock
> - Quality notifications and vendor evaluation
> - Dynamic modification rules, and the link to supplier scorecards

---

## 7. Oracle SCM Cloud
> 🔴 Tier 1 · _Tracker hint:_ Order management, inventory, procurement, manufacturing modules

### Definition
**Oracle Fusion Cloud SCM** is Oracle's SaaS suite for supply chain, updated on a regular quarterly release cycle. Main areas:
- **Order Management:** order capture, orchestration, pricing, **Global Order Promising** (availability and promise dates), fulfilment and returns.
- **Inventory Management:** on-hand, subinventories, lot/serial control, cycle counts, costing.
- **Procurement:** requisitions, purchasing, supplier qualification and portal, sourcing, contracts.
- **Manufacturing:** work definitions, work orders, shop-floor execution, quality.
- **Supply Chain Planning:** demand and supply planning, S&OP.
- **Logistics:** warehouse management and transportation management.
- **Product Lifecycle Management** and **Maintenance**.

Differences vs SAP: SaaS-first and a single data model, with configuration through setup tasks and extensibility via a platform; SAP historically stronger in discrete and process manufacturing depth and large on-premise installed base; Oracle's strength in integrated cloud finance and a single-cloud model. Selection depends on industry fit, existing estate and TCO.

### Example
A distributor on Oracle: a customer order enters Order Management, Global Order Promising selects the best warehouse, Inventory ships it, and receivables is updated; low stock triggers a requisition in Procurement, converted to a purchase order to the supplier through the portal.

### In the news
See news box. The ECC deadline has also made Oracle and others bid for SAP customers deciding whether to re-platform rather than upgrade; the market commentary is mixed and no figure is claimed here.

### Interview angle
> [!question] How it is asked
> "Compare SAP and Oracle for a mid-size manufacturer. How would you decide?"

> [!tip] Strong answer includes
> - Module coverage in each (order management, inventory, procurement, manufacturing, planning)
> - Selection criteria: industry fit, TCO, integration, talent, vendor roadmap
> - Cloud vs on-premise and customisation impact
> - Fit-gap and proof of concept before deciding

---

## 8. ERP Integration Points
> 🔴 Tier 1 · _Tracker hint:_ MM↔PP↔SD↔FI integration; data flows and dependency

### Definition
Integration means one event updates several modules automatically.

| Event | MM / PP / SD | FI/CO effect |
|---|---|---|
| Goods receipt on PO | MM stock up | Dr Inventory, Cr GR/IR |
| Invoice verification | MM | Dr GR/IR, Cr Vendor |
| Goods issue to production order | PP/MM stock down | Dr WIP, Cr Inventory |
| Goods receipt of finished goods | PP stock up | Dr FG inventory, Cr WIP (via order settlement) |
| Post goods issue to customer | SD/MM stock down | Dr COGS, Cr Inventory |
| Billing | SD | Dr Customer, Cr Revenue |

Dependencies: SD availability check reads PP/MM stock and planned receipts; MRP converts SD demand to PP and MM supply; **account determination** (OBYC for MM, VKOA for SD) ties every movement to ledger accounts; master data errors (missing account assignment) stop postings. Integration with external systems: EDI, APIs, middleware (SAP Integration Suite), and WMS/TMS/CRM.

### Example
A customer order of 100 units with zero stock: SD ATP checks planned orders from MRP; if production order completes tomorrow, a confirmed date is given. Once produced, the finished goods receipt (PP) feeds stock, delivery and PGI (SD) reduce stock and post COGS (FI): four modules, one chain.

### In the news
See news box. At AusNet the project integrated field-service and asset systems, as well as 50+ external retailers, during cutover; integration scope is typically what extends ERP timelines.

### Interview angle
> [!question] How it is asked
> "A goods issue posted but finance shows no COGS. Where do you look?"

> [!tip] Strong answer includes
> - Understand the integration chain and account determination (OBYC, VKOA)
> - Check movement type, valuation class, material master accounting view
> - Check blocked postings, period closing, error logs
> - Explain a clear example of cross-module flow with entries

---

## 9. Master Data in ERP
> 🔴 Tier 1 · _Tracker hint:_ Material master, vendor master, customer master, BOM, routing

### Definition
**Master data** is the slowly changing reference data used by every transaction; poor master data is the biggest root cause of ERP problems ("garbage in, garbage out").

| Object | Purpose | T-code (ECC) |
|---|---|---|
| **Material master** | Views by function (basic, purchasing, MRP, sales, storage, quality, accounting) and org level | MM01/MM02/MM03 |
| **Vendor master** | Vendor general, company-code and purchasing data (banking, payment terms) | XK01 (S/4: Business Partner, BP) |
| **Customer master** | General, company code (reconciliation account), sales area data (pricing, shipping) | XD01 (S/4: BP) |
| **BOM** | Components per parent with quantities | CS01 |
| **Routing** | Operations, work centres, times | CA01 |
| **Work centre** | Capacity and cost | CR01 |
| **Info record** | Vendor-material price and lead time | ME11 |

Governance: data owners, creation and change workflows, mandatory fields, duplicate check, naming standards, regular cleansing, and metrics (completeness, accuracy, duplicates).

### Example
A material with a planned delivery time of 3 days instead of the real 21 days will make MRP release orders too late, producing shortages, even though MRP itself is functioning perfectly. Fixing the lead time in the MRP view corrects planned order dates.

### In the news
See news box. Migration to S/4HANA triggers data cleansing: companies archive obsolete materials and merge duplicate vendors before moving; the data work is often the critical path.

### Interview angle
> [!question] How it is asked
> "Why does master data governance matter in ERP?"

> [!tip] Strong answer includes
> - Names key objects and what each controls
> - Examples of master-data errors and their effects
> - Governance: ownership, workflow, duplicate checks, KPIs
> - Link to migration and analytics quality

---

## 10. Transaction Flows in SAP
> 🔴 Tier 1 · _Tracker hint:_ Procure-to-Pay, Order-to-Cash, Plan-to-Produce — end-to-end

### Definition
Three end-to-end flows:

**Procure-to-Pay (P2P):** requirement (PR, ME51N) → PO (ME21N) → GR (MIGO, 101) → invoice verification (MIRO) → payment run (F110) → vendor ledger cleared.

**Order-to-Cash (O2C):** sales order (VA01) → availability check → delivery (VL01N) → pick/pack → PGI (VL02N, 601) → billing (VF01) → customer payment (F-28) → receivable cleared.

**Plan-to-Produce (P2Pr):** forecast or PIR (MD61) → MRP (MD01) → planned order → production order (CO01) → component issue (261) → confirmation (CO11N) → GR of finished goods (101) → order settlement (CO88) to inventory.

Each flow creates a **document chain** viewable by document flow; each step has controls (approvals, tolerances, blocks) and financial postings. Measuring flow KPIs: PO cycle time, GR/IR ageing, DSO, order-to-delivery time, schedule adherence.

### Example
Make-to-stock product: MRP triggers production order for 400 units (CO01); components issued; confirmation posts labour/machine cost; GR of 400 FG at standard cost ₹200 = ₹80,000 inventory. Customer orders 150: VA01 → VL01N → PGI posts COGS ₹30,000 → VF01 invoices ₹300 x 150 = ₹45,000 plus GST.

### In the news
See news box. Wipro's AusNet delivery is an end-to-end transformation including order-to-cash style processes for retailers; process-first design underlies successful programs.

### Interview angle
> [!question] How it is asked
> "Describe O2C in SAP step by step and name documents and T-codes."

> [!tip] Strong answer includes
> - Sequence with documents and T-codes
> - Financial postings at each stage
> - Controls and typical exceptions (blocks, tolerances)
> - KPIs per flow (DSO, cycle time, GR/IR ageing)

---

## 11. ERP Implementation Phases
> 🔴 Tier 1 · _Tracker hint:_ Blueprint, realization, final prep, go-live, support

### Definition
Classic **ASAP methodology** (5 phases):
1. **Project preparation:** scope, team, governance, plan, landscape.
2. **Business blueprint:** requirements and process design workshops, fit-gap, blueprint sign-off.
3. **Realization:** configuration, development (RICEFW: Reports, Interfaces, Conversions, Enhancements, Forms, Workflows), unit and integration testing.
4. **Final preparation:** user acceptance testing (UAT), data migration mock loads, cutover plan, end-user training, go/no-go decision.
5. **Go-live and support:** cutover, hypercare (typically 4–8 weeks), stabilisation, handover.

Modern **SAP Activate** uses six phases: Discover, Prepare, Explore, Realize, Deploy, Run, with a fit-to-standard approach and agile sprints. Approaches: **greenfield** (new implementation), **brownfield** (system conversion), **bluefield/selective data transition**. Go-live styles: big bang, phased (by plant/module), parallel. Typical success factors: executive sponsorship, scope control, data quality, testing discipline, change management; typical failure causes: scope creep, under-resourced business teams, late data migration.

### Example
A 1,000-user manufacturing rollout: blueprint 3 months, realization 6, final prep 3, go-live in month 12, hypercare 2 months. Scope cut (fit-to-standard instead of custom) reduces RICEFW count and shortens realization.

### In the news
See news box. Wipro delivered AusNet in 18 months (as announced); with the ECC deadline of 2027, many programs are compressed, raising the risk of weak testing and training.

### Interview angle
> [!question] How it is asked
> "What are the phases of an ERP implementation and where do projects fail?"

> [!tip] Strong answer includes
> - The five ASAP phases (or SAP Activate) with deliverables
> - Greenfield vs brownfield, big-bang vs phased go-live
> - Failure points: scope creep, data, testing, training
> - Governance: steering committee, risk log, go/no-go criteria

---

## 12. Change Management in ERP
> 🔴 Tier 1 · _Tracker hint:_ User training, data migration, cutover planning

### Definition
ERP is a business change programme, not an IT install. Components:
- **Stakeholder and impact analysis:** who changes what, by role.
- **Communication and sponsorship:** consistent message from leadership; change champions and **super-users**.
- **Training:** role-based, hands-on, in a training client with realistic data; train-the-trainer; just-in-time before go-live.
- **Data migration:** extract, clean, transform, load (ETL), with **mock loads** (usually 2–3), reconciliation (counts, values) and business sign-off.
- **Cutover planning:** detailed hour-by-hour runbook (freeze, final loads, open-item balances, interfaces on, validation), rollback criteria, **go/no-go**.
- **Hypercare** and support desk; adoption KPIs (login rates, ticket trends, error rates).
- Frameworks: **Kotter's 8 steps**, **ADKAR** (Awareness, Desire, Knowledge, Ability, Reinforcement).

Resistance is natural; address it with involvement, reasons, training, and quick wins.

### Example
Inventory migration reconciliation: legacy stock value ₹52.40 crore across 18,000 materials; loaded value ₹52.38 crore across 18,000 materials after mock 2: the ₹2 lakh difference is investigated (rounding on 14 items and 2 wrong units of measure) and fixed before mock 3.

### In the news
See news box. AusNet's cutover involved 1,600+ users and 50+ retailers; at that scale a rehearsed cutover and communications plan is what limits business disruption.

### Interview angle
> [!question] How it is asked
> "Users resist the new ERP two weeks before go-live. What do you do?"

> [!tip] Strong answer includes
> - Diagnose the resistance (training gaps, fear, process fit)
> - Super-users, targeted training, floor-walkers, quick fixes
> - Go/no-go criteria and a contingency plan, including a possible go-live deferral
> - A structured framework (ADKAR or Kotter) and adoption metrics

---

## 13. Analytics from ERP
> 🔴 Tier 1 · _Tracker hint:_ Standard reports, ABAP queries, BI integration (SAP BW)

### Definition
Layers of reporting from ERP:
1. **Standard (operational) reports:** ME2N (POs), MB51 (material documents), MMBE (stock), VA05 (sales orders), MD04 (stock/requirements). Real-time but transaction-level.
2. **Ad-hoc tools:** **SQVI** (quick viewer), **SQ01** (ABAP query), **SE16N** (table display, read-only with authorisation), ALV list layouts for export.
3. **Embedded analytics in S/4HANA:** **CDS views** and **Fiori** analytical apps run on live data.
4. **Data warehouse and BI:** **SAP BW / BW/4HANA** (extractors, InfoProviders, planning), **SAP Datasphere** and **SAP Analytics Cloud**; connectors to Power BI/Tableau.

Why separate analytics: avoid loading the transaction system, combine ERP with external data, history and planning. Good practice: certified data models, data-quality checks, and role-based access. Key SCM reports: OTIF from delivery documents, inventory ageing (DIO), vendor evaluation (ME61), open PO ageing, GR/IR clearing.

### Example
Compute DIO: pull closing stock value by material (MB52 or table MARD with valuation prices) and COGS from billing/FI; DIO = average inventory / (COGS/365). Doing this in BW once, with a consistent definition, avoids each plant producing different numbers in Excel.

### In the news
See news box. S/4HANA with embedded analytics reduces the need for separate extract jobs for some reports, one of the selling points in the migration push.

### Interview angle
> [!question] How it is asked
> "How would you build a procurement dashboard on top of SAP data?"

> [!tip] Strong answer includes
> - Source tables or standard extractors, and the data model (PO, GR, invoice, vendor)
> - Operational reports vs BW/BI for history and combination
> - KPIs: spend by category, PO cycle time, OTD, price variance, GR/IR ageing
> - Data governance: single definition per KPI, refresh cadence, access control

---

## 14. ⭐ Advanced: S/4HANA vs ECC and "Clean Core"
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**SAP S/4HANA** (launched 2015) runs on the **SAP HANA** in-memory database and simplifies the data model.

| Area | ECC (classic) | S/4HANA |
|---|---|---|
| Database | Any supported DB | HANA only |
| Finance | Separate FI and CO tables | **Universal Journal (ACDOCA)**, one line-item table |
| Material documents | MKPF/MSEG, aggregates | MATDOC, fewer aggregates |
| Customers/vendors | Separate masters | **Business Partner** (single concept) |
| MRP | Batch | **MRP Live** (HANA-optimised) |
| UX | SAP GUI | **Fiori** apps |
| Advanced ATP, EWM, credit | Add-ons | Embedded options |

**Deployment:** on-premise, **RISE with SAP** (private edition), **public cloud (GROW with SAP)**. **Clean core** means keeping custom code outside the standard core (side-by-side extensions on BTP, in-app key-user extensibility) so upgrades stay easy. Migration paths: greenfield, brownfield (system conversion with SUM/DMO and Readiness Check), selective data transition.

### Example
A firm with 3,000 custom (Z) objects runs the custom-code analysis: 1,200 are unused (retire), 900 are replaced by standard functions in S/4, 900 are rebuilt as extensions. Only 900 of 3,000 (30%) need rebuilding, and retiring the 1,200 unused objects (40%) removes them from testing scope entirely.

### In the news
See news box. The 2027 mainstream-maintenance date for ECC 6 EHP 6–8 and its 2030 extended support limit are the immediate drivers for brownfield vs greenfield decisions.

### Interview angle
> [!question] How it is asked
> "What are the main differences between ECC and S/4HANA and how would you advise a client on migration?"

> [!tip] Strong answer includes
> - Technical changes: HANA, Universal Journal, Business Partner, MATDOC, Fiori
> - Migration paths and how to choose (customisation, data history, appetite for process change)
> - Clean-core principle and extensions
> - Business case: deadline risk, TCO, process benefits and not only the technology

---

## 15. ⭐ Advanced: ERP Selection, Fit-Gap and TCO
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Selecting an ERP is a structured decision.
1. **Requirements:** processes by priority (must/should/nice-to-have), regulatory needs (GST e-invoicing, e-way bill), integration, scale.
2. **Long-list to short-list:** RFI, then RFP with scripted demos on the company's own scenarios.
3. **Fit-gap analysis:** for each requirement, rate **Fit** (standard), **Configure**, **Extend/Customise**, **Gap**; each gap gets effort and risk.
4. **TCO over 5–7 years:** licences or subscription, implementation partner, infrastructure, internal team, training, support/AMC, upgrades, integration, change cost.
5. **Scoring:** weighted scorecard on fit, TCO, vendor viability, ecosystem/talent, risk, roadmap.
6. **Reference checks and proof of concept.**

$$TCO = \sum_{t=0}^{T} \frac{\text{Licence/subscription}_t + \text{Implementation}_t + \text{Run cost}_t + \text{Internal cost}_t}{(1+r)^t}$$

Cloud shifts spend from capex to opex but does not make it cheaper automatically; subscription costs compound over time.

### Example
Option A (on-premise): ₹10 crore upfront plus ₹2 crore a year run cost for 5 years = 10 + 10 = ₹20 crore (undiscounted). Option B (cloud): ₹4 crore implementation plus ₹3.2 crore a year subscription for 5 years = 4 + 16 = ₹20 crore (undiscounted). Equal at 5 years; B costs less upfront and is cheaper if the horizon is shorter, while A is cheaper beyond year 5. Include discounting and the hidden costs (data migration, change, integration) before concluding.

### In the news
See news box. For SAP ECC users, the choice is no longer "ERP or not" but which S/4HANA route and when: a TCO and risk question given the 2027 and 2030 dates.

### Interview angle
> [!question] How it is asked
> "A mid-size manufacturer wants a new ERP. How do you run the selection?"

> [!tip] Strong answer includes
> - Requirements prioritised by process and compliance (GST e-invoicing)
> - Fit-gap, weighted scorecard and scripted demos
> - Five to seven year TCO, including hidden costs
> - Risk, vendor viability, partner ecosystem and change-readiness

---
## 🔗 Go deeper: expansion notes
- [[190 SAP FI-CO Essentials for Operations Professionals|SAP FI-CO Essentials for Operations Professionals]]
- [[191 SAP MM Advanced - Inventory, Batches & Special Stocks|SAP MM Advanced - Inventory, Batches & Special Stocks]]
- [[192 SAP Sourcing & Procurement Deep Dive|SAP Sourcing & Procurement Deep Dive]]
- [[193 SAP MRP Deep Dive - Planning Strategies & Parameters|SAP MRP Deep Dive - Planning Strategies & Parameters]]
- [[195 SAP SD Advanced - Pricing, Output & Document Flow|SAP SD Advanced - Pricing, Output & Document Flow]]
- [[200 SAP S-4HANA Migration, Data Migration & Testing|SAP S-4HANA Migration, Data Migration & Testing]]
- [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows|SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]
