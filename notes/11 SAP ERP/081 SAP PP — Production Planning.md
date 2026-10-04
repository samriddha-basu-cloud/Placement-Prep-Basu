---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP PP — Production Planning"
tier: Tier 1
roles: Operations
status: complete
subtopics: 15
---
# SAP PP — Production Planning

⬅ [[080 SAP MM — Materials Management]] · [[_Index - SAP ERP|SAP ERP]] · [[082 SAP SD — Sales & Distribution]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. PP Organizational Structure]]
2. [[#2. Bill of Materials (CS01/CS03)]]
3. [[#3. Work Center (CR01)]]
4. [[#4. Routing (CA01)]]
5. [[#5. Demand Management (MD61/MD62)]]
6. [[#6. MRP Run (MD01N)]]
7. [[#7. Production Order (CO01/CO11N)]]
8. [[#8. Capacity Planning (CM01)]]
9. [[#9. Shop Floor Control]]
10. [[#10. KANBAN in SAP (PK01)]]
11. [[#11. PP-PI (Process Industries)]]
12. [[#12. Repetitive Manufacturing]]
13. [[#13. MRP Key Parameters]]
14. [[#14. ⭐ Advanced: Make-to-Order & Variant Configuration]]
15. [[#15. ⭐ Advanced: MRP Live, Demand-Driven MRP (DDMRP) & PP/DS]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): manufacturers face the ECC deadline and move planning to S/4HANA
> **ECC clock is ticking (Gartner figures, end-2024).** Mainstream maintenance for SAP ERP 6.0 (ECC, EHP 6–8) ends on **31 Dec 2027**, extended maintenance runs to **31 Dec 2030**. Gartner estimated only **39% of SAP's ~35,000 ECC customers (~14,000)** had bought S/4HANA transition licences by end-2024; a Horváth study of 200 SAP companies found only **8% of migrations finished on schedule**, with projects running **30% longer** than planned. ([SoftwareSeni summary](https://www.softwareseni.com/what-sap-ecc-end-of-support-actually-means-and-why-17000-companies-are-not-ready/); secondary source quoting Gartner and Horváth)
> 
> **GAIL goes live on RISE with SAP (formal launch 25 Jun 2025).** GAIL, a gas-processing and petrochemicals major, described itself as the first Maharatna PSU to move from legacy ECC to S/4HANA on cloud ("Navodaya"), delivered within one year. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
> 
> **SAP Q4 2025 (29 Jan 2026).** Current cloud backlog +25% in constant currency (+16% reported); 2026 guidance 23–25% cloud revenue growth; Business AI in about two-thirds of Q4 cloud orders. ([Constellation Research](https://www.constellationr.com/insights/news/saps-q4-cloud-backlog-spurs-concerns))
> 
> Sub-topics that say **"See news box"** reuse these items. Related: [[080 SAP MM — Materials Management]].

---
## 1. PP Organizational Structure
> 🔴 Tier 1 · _Tracker hint:_ Plant → Work Centers → Routings; Production Versions; Plant capacity

### Definition
PP is plant-centred. Key org and master-data structure:
- **Plant** (production site, MRP and planning level) with **storage locations**, **MRP areas** (optional), **planner groups** and **production scheduler groups** (responsible for order execution).
- **Work centres** (where work is done) assigned to the plant; **task lists** (routings, master recipes) list operations performed on work centres.
- **Production version** (`C223` or in material master MRP 4): links a BOM alternative and a routing alternative for a given validity and lot-size range. One material can have several versions (e.g. line A vs line B).
- **Plant calendar** and **factory calendar**, **shift sequences**, and **capacity categories** (machine, labour).

Organisational hierarchy: Client → Company Code → Plant → Storage Location; PP-specific: **MRP controller**, **production scheduler**, **planner group** (task list), **capacity planner group**.

Production type choices: discrete (make-to-stock, make-to-order), repetitive, process (PP-PI), Kanban.

### Example
Plant 1100 Pune makes e-scooter controllers. Work centres: SMT-01 (surface mount line), WAVE-01, TEST-01. Material C-100 has two production versions: 0001 using BOM alt 1 and routing group G1 (line SMT-01) for lots of 500–5,000, and 0002 using BOM alt 2 and routing G2 for lots up to 499 on a manual line.

### In the news
See news box. Manufacturing is the largest S/4HANA migration pool; PP structures (work centres, routings) often get simplified in the process.

### Interview angle
> [!question] How it is asked
> "How is a plant set up for production in SAP?" or "What links BOM and routing?"

> [!tip] Strong answer includes
> - Plant, work centre, routing, BOM as the four building blocks
> - Production version as the link between BOM and routing
> - MRP controller and scheduler responsibilities
> - Choice of manufacturing type by product (discrete, repetitive, process)

---

## 2. Bill of Materials (CS01/CS03)
> 🔴 Tier 1 · _Tracker hint:_ Header material + components + qty; BOM usage; BOM explosion in MRP

### Definition
A **BOM** lists the components and quantities needed to make one base quantity of a header material. Structure: **header** (material, plant, BOM usage, alternative, base quantity, validity) and **items** (component, quantity, unit, **item category** such as L stock item, N non-stock, T text, D document).

Important concepts:
- **BOM usage:** 1 production, 2 engineering/design, 3 universal, 5 sales and distribution. MRP uses the production BOM.
- **Alternative BOMs:** same material made in different ways (e.g. different lot size or plant).
- **Change management:** engineering change numbers (`CC01`) with validity dates.
- **Phantom assemblies** (special procurement key 50): not stocked; exploded through during MRP.
- **Multi-level BOM:** assemblies contain sub-assemblies; **BOM explosion** in MRP goes level by level using low-level codes.
- **Variant BOM** (super BOM) combines options.

T-codes: `CS01` create, `CS02` change, `CS03` display, `CS11` level-by-level explosion, `CS12` multi-level explosion, `CS15` where-used, `CSC1` BOM copy.

Component requirement (with scrap): $\text{Requirement} = \frac{\text{order qty}}{\text{base qty}} \times \text{component qty} \times (1 + \text{scrap\%})$.

### Example
BOM for 1 bicycle (base qty 1 PC): frame 1, wheel 2, handlebar 1, chain 1, bolt 12 (component scrap 2%). Order for 500 bicycles → wheels 1,000, bolts = 500 × 12 × 1.02 = **6,120**. If the wheel is itself a sub-assembly (rim 1, tyre 1, spokes 36), MRP explodes it too: 1,000 wheels need 36,000 spokes.

### In the news
See news box. Accurate BOMs are a pre-condition for MRP Live in S/4HANA; BOM errors are among the most common causes of production shortages in migrated plants.

### Interview angle
> [!question] How it is asked
> "What is a BOM and how does MRP use it?" or "How do you handle engineering changes in BOMs?"

> [!tip] Strong answer includes
> - Header/items and BOM usage
> - Multi-level explosion with quantity arithmetic including scrap
> - Alternatives, phantom assemblies, change numbers
> - Link to MRP, costing and production order component list

---

## 3. Work Center (CR01)
> 🔴 Tier 1 · _Tracker hint:_ Machine/labor resource; capacity; scheduling formulas; shift schedules

### Definition
A **work centre** is a location (machine, line, group of workers) where operations are performed. It stores **default values and control data**:
- **Basic data:** plant, category (machine, labour, process line), usage (which task lists may use it), standard value key (what times are entered: setup, machine, labour).
- **Capacity data:** capacity category, **operating time**, **number of individual capacities**, **capacity utilisation rate**, shift sequence (from factory calendar).
- **Scheduling:** formulas for lead time scheduling and capacity requirements, e.g. $\text{Capacity requirement} = \text{setup time} + \text{operation qty} \times \text{machine time per unit}$.
- **Costing:** link to a **cost centre** and **activity types**, giving the cost rate (e.g. machine hour ₹600) for product costing.

Available capacity per day: $\text{Operating time} \times \text{utilisation} \times \text{number of individual capacities}$.

T-codes: `CR01` create, `CR02` change, `CR03` display, `CR05` where-used (work centre list), `CRC1` resources (PP-PI).

### Example
Work centre MACH-01: shift 8 h with 0.5 h break = 7.5 h operating time, utilisation 90%, 2 machines. Available capacity = 7.5 × 0.9 × 2 = **13.5 hours per day**. A 200-unit operation with setup 30 min and 2 min/unit needs 30 + 400 = 430 min = **7.17 hours**, so about 53% of the day's capacity.

### In the news
See news box. Machine data from IoT and MES feed work-centre confirmations in modern smart-factory integrations with S/4HANA.

### Interview angle
> [!question] How it is asked
> "What is stored in a work centre, and how is capacity defined?"

> [!tip] Strong answer includes
> - Work centre as the link between routing, capacity and cost centre
> - Capacity formula with utilisation and number of capacities
> - Standard value key and scheduling formulas
> - Costing relevance (activity price)

---

## 4. Routing (CA01)
> 🔴 Tier 1 · _Tracker hint:_ Sequence of operations; work centers; standard values (machine time, labor time)

### Definition
A **routing** (task list type N) is the ordered **sequence of operations** needed to produce a material, with the work centre and **standard values** for each operation (setup time, machine time per base quantity, labour time, teardown). It also holds **component allocation** (which BOM items are consumed at which operation), **inspection characteristics** (QM), **production resource/tools (PRT)** and **control keys** (e.g. confirmation required, costing relevant).

Lead time scheduling uses routing times: $\text{Operation lead time} = \text{queue} + \text{setup} + \text{processing} + \text{teardown} + \text{wait} + \text{move}$. Scheduling types: **forward** (from start date), **backward** (from finish date, standard), **today**.

Routing structure: **Group** and **group counter** (alternative sequences), **operation** (10, 20, 30...), **sub-operations** and **sequences** for parallel or alternative paths. T-codes: `CA01` create, `CA02` change, `CA03` display; `CA85` mass replace of work centre.

Linking: the material is assigned to a routing in the routing header or via the **production version** (so MRP-produced planned orders pick the right routing and BOM).

### Example
Routing for a metal bracket (base 1 piece): Op 10 Cutting (setup 20 min, 1 min/pc), Op 20 Drilling (setup 10, 0.5), Op 30 Painting (setup 0, 0.3). For a 100-piece lot: process times 100, 50, 30 min; setups 20, 10, 0 min. Total = 100 + 50 + 30 + 30 = **210 min** of in-operation time (before queue and move times).

### In the news
See news box. Consultants are often asked to rationalise routings during migration, since decades of duplicated task lists inflate data volumes.

### Interview angle
> [!question] How it is asked
> "What's the difference between a BOM and a routing?" or "How is production lead time calculated in SAP?"

> [!tip] Strong answer includes
> - BOM = what to make with; routing = how and where to make it
> - Standard values and where they feed (scheduling, capacity, costing)
> - Lead-time elements and backward scheduling
> - Production version linkage

---

## 5. Demand Management (MD61/MD62)
> 🔴 Tier 1 · _Tracker hint:_ Planned Independent Requirements (PIR); strategy group; consumption mode

### Definition
**Demand management** captures expected demand for finished goods (and key sub-assemblies) so MRP can plan them before customer orders arrive. Demand is stored as **Planned Independent Requirements (PIR)**, entered in `MD61` (create), `MD62` (change), `MD63` (display), or transferred from SOP/forecast (`MC74`).

Key control: **planning strategy** (determined by the **strategy group** in MRP 3 view). Examples:
| Strategy | Name | Idea |
|---|---|---|
| 10 | Make-to-stock | Plan on PIR; sales orders consume PIR |
| 40 | Planning with final assembly | Plan sub-assemblies on PIR; final assembly when order arrives, consumption by orders |
| 50 | Planning without final assembly | Plan components only; no final assembly planned |
| 20 | Make-to-order | No PIR; production per sales order |
| 25 | Make-to-order for configurable material | Used with variant configuration |

**Consumption mode** and **consumption periods** (backward/forward) define how real sales orders reduce PIR so demand is not double counted (PIR 100, order 30 → remaining PIR 70).

### Example
A bike maker enters PIR for 1,000 units in October (weekly 250). By week 2 customer orders of 180 arrive; with consumption backward 1 week, forward 1 week, orders consume PIR so the net requirement is the larger of the remaining PIR and orders, avoiding a 1,180 total.

### In the news
See news box. Planners increasingly link demand management with SAP IBP forecasts instead of manual PIRs.

### Interview angle
> [!question] How it is asked
> "What is a PIR and how does consumption work?" or "Difference between strategy 10 and 40?"

> [!tip] Strong answer includes
> - PIR as forecast-driven, order consumption to avoid double counting
> - Strategy group and common strategies (10, 40, 50, 20)
> - Make-to-stock vs make-to-order link to decoupling point
> - Source of PIRs: sales forecast, SOP/IBP

---

## 6. MRP Run (MD01N)
> 🔴 Tier 1 · _Tracker hint:_ Net requirements calc; planned orders; planned order → production order conversion

### Definition
An **MRP run** evaluates demand (PIR, sales orders, dependent requirements, reservations) against supply (stock, open production orders, POs, PRs, planned orders) and creates **procurement proposals**: **planned orders** (in-house) or **PRs/schedule lines** (external). In S/4HANA, `MD01N` (MRP Live) executes the logic in the HANA database. Processing keys: **NETCH** (net change in the planning horizon), **NETPL** (net change), **NEUPL** (regenerative).

Steps:
1. Determine planning scope and horizon (plant, materials, MRP controller).
2. **BOM explosion**, level by level by low-level code (finished goods first).
3. **Net requirement calculation:** $\text{Net} = \text{requirements} + \text{safety stock} - \text{stock} - \text{receipts}$.
4. **Lot sizing**, then **lead-time scheduling** (backward from requirement date using routing or planned delivery time).
5. Create planned order or PR; **conversion** of planned order to production order via `MD04` (convert) or `CO41`/`COHV` mass conversion.

Display tools: `MD04` stock/requirements list, `MD05` MRP list, `MD07` current stock requirement list. Planned orders can be **firmed** to protect them from automatic change.

### Example
Material FERT-100: demand 400 (week 10), stock 80, safety stock 40, firmed planned order 100 due week 9. Net = 400 + 40 − 80 − 100 = **260**. With lot size EX, a planned order for 260 is created and later converted to a production order (CO01 or `MD04` conversion) at release.

### In the news
See news box. MRP Live improves runtime so planners can run MRP multiple times a day, rather than overnight only.

### Interview angle
> [!question] How it is asked
> "Explain the MRP logic and what MRP creates for in-house vs external procurement."

> [!tip] Strong answer includes
> - Inputs, netting formula, outputs
> - Planned order for make, PR for buy; conversion to production order
> - Processing keys, MRP Live in HANA
> - Common problems: wrong lead time, missing BOM or master data, firmed orders

---

## 7. Production Order (CO01/CO11N)
> 🔴 Tier 1 · _Tracker hint:_ Released, confirmed, TECO; goods issue from production order; goods receipt

### Definition
A **production order** is the document that authorises and tracks manufacture of a quantity of a material on given dates, with **components** (from BOM) and **operations** (from routing). Created via `CO01` (or by converting a planned order), changed `CO02`, displayed `CO03`; mass processing `COHV`; list `COOIS`.

**Status flow:** CRTD (created) → REL (released) → PCNF/CNF (partially/fully confirmed) → **DLV** (delivered) → **TECO** (technically completed) → **CLSD** (closed after settlement). Typical order of events:
1. **Availability check** of components, capacity, PRT.
2. **Release** (`CO05N`) and print shop papers.
3. **Goods issue** of components: movement 261 (manual or backflush).
4. **Confirmations** in `CO11N` (single), `CO15` (production order confirmation) record yield, scrap, activity times; they update capacity and status.
5. **Goods receipt** from production with movement 101.
6. **TECO** (`CO02`) and **settlement** (`KO88`) of variances at period close to inventory or CO accounts.

Costs: planned (from BOM and routing) vs actual (material issues, activity postings, overhead). Variances: usage, price, lot-size, input.

### Example
Order for 1,000 pieces of C-100: components issued (261) worth ₹3,00,000, activity ₹60,000, so actual cost ₹3,60,000. GR 1,000 pieces at standard ₹350 = ₹3,50,000. Variance ₹10,000 is settled to variance accounts at TECO.

### In the news
See news box. Real-time confirmation data is feeding AI-driven scheduling and predictive maintenance in modern SAP stacks.

### Interview angle
> [!question] How it is asked
> "Walk me through a production order from creation to settlement."

> [!tip] Strong answer includes
> - Status flow: created, released, confirmed, delivered, TECO, closed
> - Movements 261 (issue) and 101 (receipt) and the accounting effect
> - Confirmation and variance calculation
> - Link to MRP conversion and costing

---

## 8. Capacity Planning (CM01)
> 🔴 Tier 1 · _Tracker hint:_ Load vs capacity; capacity leveling; overload alerts; finite scheduling

### Definition
**Capacity planning** compares the **capacity requirements** generated by planned and production orders with the **available capacity** of each work centre, and resolves overloads.
- **Capacity evaluation** (`CM01` by work centre; `CM02` by order/work centre; `CM03` work-centre view) shows the **load**, e.g. 125% in week 12.
- **Capacity levelling** via the **planning table** (`CM21`, `CM25`) or the leveling transaction: reschedule, split orders, shift to alternative work centre, add shifts or overtime, outsource.
- **Finite scheduling** (in PP/DS or via capacity levelling) enforces limits; ordinary MRP is **infinite** (it ignores capacity).

Utilisation: $\text{Load \%} = \frac{\text{capacity requirement}}{\text{available capacity}} \times 100$. Typical rule: sustained load above 85–90% starts to hurt lead times (queueing). Capacity requirements are generated when orders are saved, using routing standard values.

PP/DS (Production Planning and Detailed Scheduling) is the advanced finite-planning option, available embedded in S/4HANA.

### Example
Work centre MACH-01 has 13.5 h/day, so 67.5 h for a 5-day week. Orders load 81 h: load = 81 / 67.5 = **120%**. Action: move 13.5 h of work to MACH-02 or run Saturday overtime (e.g. +8 h × 2 machines = 16 h), returning load to about 97% (81 / 83.5 with overtime).

### In the news
See news box. As demand volatility rose in 2024–25, planners relied on faster re-planning cycles; MRP Live and PP/DS help shorten the loop.

### Interview angle
> [!question] How it is asked
> "MRP shows you can't meet demand because the plant is overloaded. What do you do?"

> [!tip] Strong answer includes
> - Capacity load calculation and evaluation tools (CM01)
> - MRP is infinite-capacity; need levelling
> - Levers: alternative work centres, overtime, splitting, outsourcing, re-prioritise
> - Bottleneck thinking (Theory of Constraints)

---

## 9. Shop Floor Control
> 🔴 Tier 1 · _Tracker hint:_ Confirmations (CO11N); yield, scrap, rework reporting; goods receipt

### Definition
**Shop floor control** executes and monitors orders on the plant floor:
- **Release and shop papers** (order, operation lists, pick lists, tags).
- **Component staging and issue** (261, backflush or manual).
- **Confirmation** (`CO11N` operation timeticket, `CO15`, `CORK` for process orders): record **yield**, **scrap**, **rework quantity**, actual setup/machine/labour time, **reason for variance**, final confirmation flag.
- **Work-in-process (WIP)** valuation, shown in order costs.
- **Goods receipt** from the order (101) at the last operation, optionally automatic ("GR at final confirmation").
- **Order monitoring:** `COOIS` information system, `COHV` for mass operations.

KPIs: yield $= \frac{\text{good units}}{\text{units started}}$, scrap rate, schedule adherence, OEE (availability × performance × quality). MES (shop floor systems) integrate via **SAP Digital Manufacturing**.

### Example
Order for 1,000 pieces: Op 10 starts 1,000; confirm 970 yield, 20 scrap, 10 rework. Yield = 970/1,000 = **97%**. Final confirmation books GR of 970 pieces; scrap 20 posted to scrap cost; rework 10 is re-run in a rework operation (cost reassigned).

### In the news
See news box. Plants linking shop-floor data to ERP in real time can detect yield loss in the same shift rather than at month end.

### Interview angle
> [!question] How it is asked
> "How do you track production progress and losses in SAP?" or "What is a confirmation?"

> [!tip] Strong answer includes
> - Confirmation types and data (yield, scrap, rework, times)
> - Automatic effects: capacity relief, status change, optional backflush and GR
> - KPIs: yield, OEE, schedule adherence
> - Role of MES and data accuracy discipline

---

## 10. KANBAN in SAP (PK01)
> 🔴 Tier 1 · _Tracker hint:_ Kanban cards; replenishment triggers; classical vs event-driven kanban

### Definition
**Kanban** is a pull system: replenishment is triggered by consumption rather than by MRP forecast. In SAP, a **control cycle** (`PK01` create, `PK02` change, `PK03` display) links a supply area (production storage location) with a source (in-house production, external vendor, stock transfer) and holds the number of kanbans and quantity per container.

- **Classical (card-based) kanban:** each container has a card/status (empty, full, in transit). Setting a kanban to **empty** (`PK13N` kanban board, or by scanning) triggers replenishment via a PR, production order, stock transfer or scheduling-agreement release.
- **Event-driven kanban:** replenishment is triggered by an event or requirement (for example a dependent requirement or a signal from the line) rather than by a card scan; kanban sizing can be recalculated with the kanban calculation (`PKBC`).

Number of kanbans: $N = \frac{D \times (L + S)}{C}$, where D = daily demand, L = replenishment lead time (days), S = safety time (days), C = container quantity (rounded up).

Material master requires MRP type **PD** with replenishment strategy "Kanban" (indicator on MRP 4 view, and MRP type with kanban relevant).

### Example
Demand D = 200 units/day, replenishment lead time 0.5 day, safety factor 10% on lead time (S = 0.05 day), container C = 25. N = 200 × (0.5 + 0.05) / 25 = 110 / 25 = 4.4 → **5 kanbans**. Total circulating stock = 5 × 25 = 125 units.

### In the news
See news box. Toyota-style pull replenishment is being combined with demand-sensing in S/4HANA PP, but kanban remains the simplest way to run stable, repetitive consumption.

### Interview angle
> [!question] How it is asked
> "How would you reduce shop-floor inventory in SAP?" or "How many kanbans do you need?"

> [!tip] Strong answer includes
> - Pull vs push and where kanban fits (stable, repetitive)
> - SAP control cycle design and replenishment strategies
> - Kanban count formula with arithmetic
> - Limits: high variability, long lead time

---

## 11. PP-PI (Process Industries)
> 🔴 Tier 1 · _Tracker hint:_ Process orders; process instructions; batch management; pharma/chemical focus

### Definition
**PP-PI** serves continuous or batch process industries (chemicals, pharma, food). Differences from discrete PP:

| Discrete | Process |
|---|---|
| BOM + routing | **Master recipe** (phases, operations, resources, formulas) |
| Production order (`CO01`) | **Process order** (`COR1`) |
| Work centre | **Resource** (`CRC1`) |
| Piece quantities | Quantities with variable batch sizes, yield, co-/by-products |

Features: **process instructions** and **control recipes** (instructions to operators/DCS), **batch management** with classification and shelf-life (`MSC1N` create batch), co-products and by-products, **recipe approval**, GMP-validated electronic signatures. Process order confirmation: `CORK`; master recipe: `C201` (create), `C202`, `C203`. **Batch determination** picks batches by strategy (FEFO/FIFO) at goods issue.

Material quantity calculation uses formulas on the recipe (e.g. active ingredient quantity depends on potency).

### Example
Paracetamol tablet batch: recipe for 500 kg granulate: 330 kg API (corrected for 98% potency: 330 / 0.98 ≈ 336.7 kg), excipients 170 kg. Process order 1,000 kg doubles quantities; each lot is batch managed (batch 2025A017), with expiry date set at GR (e.g. 36 months).

### In the news
See news box. Pharma and chemical firms migrating to S/4HANA also adopt cloud batch traceability (serialisation) for compliance, which sits on the batch concept shown here.

### Interview angle
> [!question] How it is asked
> "How does production planning in a pharma plant differ from an automobile assembly line?"

> [!tip] Strong answer includes
> - Recipe vs BOM and routing; process order vs production order
> - Batch management and traceability (regulated industries)
> - Co-products, yield and potency adjustment
> - Compliance: GMP, audit trail, electronic signature

---

## 12. Repetitive Manufacturing
> 🔴 Tier 1 · _Tracker hint:_ Rate-based planning; backflushing; production versions; automotive/FMCG focus

### Definition
**Repetitive manufacturing (REM)** suits high-volume, stable, flow-line production (automotive, FMCG, consumer electronics) where the same product is made continuously. Instead of discrete orders, it plans by **rate** (e.g. 500 units/hour) on a **production line** over a period.

Features:
- Planning at **product cost collector** level (costs collected per material, plant and production version, not per order), reducing order-management effort.
- **Rate-based planning** using a **line rate** and **line loading** (planning table `MF50`).
- **Backflushing** (`MFBF`) at the reporting point: the system automatically consumes components (261) and receives finished goods (101) based on quantity produced.
- **Production versions** specify the BOM and routing (rate routing).
- Variances computed at the cost collector, settled at period end.

Benefits: minimal transactions, low administrative effort, accurate component consumption. Limitation: low flexibility for customised or engineer-to-order items.

### Example
FMCG line makes 6,000 packs/hour; shift 8 h. Backflush at line end 40,000 packs: system consumes 40,000 × film consumption (0.04 kg) = **1,600 kg** film and posts GR of 40,000 packs, with no shop papers. Compare with discrete: 40 orders and 40 confirmations.

### In the news
See news box. Automotive and FMCG manufacturers with fast cycle times use REM with S/4HANA to keep transaction volumes manageable.

### Interview angle
> [!question] How it is asked
> "When would you choose repetitive manufacturing over discrete production orders?"

> [!tip] Strong answer includes
> - Repetitive, high-volume, stable flows; rate-based planning
> - Backflush and cost collector explained
> - Trade-offs: low flexibility, less order-level costing
> - Example from automotive or FMCG

---

## 13. MRP Key Parameters
> 🔴 Tier 1 · _Tracker hint:_ MRP type (MRP, reorder point, consumption); lot size procedure; safety stock in material master

### Definition
Parameters in the **material master (MRP 1–4 views)** govern how each item is planned.

| Parameter | Values / meaning |
|---|---|
| **MRP type** | **PD** deterministic MRP; **VB** manual reorder point; **VM** automatic reorder point (with forecast); **VV** forecast-based planning; **ND** no planning |
| **MRP controller** | Planner responsible |
| **Lot-size procedure** | **EX** lot-for-lot; **FX** fixed lot; **HB** replenish to maximum stock; **WB/MB/TB** weekly / monthly / daily grouping; optimum procedures such as Part-period balancing |
| **Safety stock** | Buffer against variability; deducted in net requirement |
| **Reorder point** | Trigger level in reorder point planning |
| **Planned delivery time / GR processing time / in-house production time** | Lead-time elements for scheduling |
| **Procurement type** | E in-house, F external, X both |
| **Special procurement** | e.g. 30 subcontracting, 50 phantom |
| **Planning time fence / rounding value** | Frozen horizon; rounding to pallet size |

Reorder point: $ROP = d \times L + SS$, safety stock $SS = z \times \sigma_d \times \sqrt{L}$ for demand variability (z = 1.65 for 95%).

### Example
Daily demand d = 40 units, σ = 10, lead time 9 days, 95% service. $SS = 1.65 \times 10 \times 3 = 49.5 \approx 50$. ROP = 40 × 9 + 50 = **410 units**. Lot-size HB with maximum 1,000: when stock hits 410, order 1,000 − 410 = 590 units.

### In the news
See news box. Many migrations include a clean-up of MRP parameters because stale safety stocks and lead times accumulate over years and inflate working capital.

### Interview angle
> [!question] How it is asked
> "A planner complains MRP creates too many small orders. What parameters do you check?"

> [!tip] Strong answer includes
> - MRP type PD vs reorder point; when to use which
> - Lot-size procedure (EX vs FX vs HB) with the trade-off between ordering cost and holding cost
> - Safety stock and lead-time parameters; formula for ROP
> - Data hygiene: periodic review of planned delivery time and safety stock

---

## 14. ⭐ Advanced: Make-to-Order & Variant Configuration
> ⭐ Advanced · _Added beyond the tracker_

### Definition
For customer-specific products (machinery, lifts, switchgear) PP uses **make-to-order (MTO)** strategies: strategy 20 (MTO with sales order stock, **special stock E**), strategy 25 (MTO for configurable materials), and **engineer-to-order** with project stock (Q) via PS. Demand and stock are tied to the sales order item: production for order X can be used only for order X.

**Variant configuration (VC)** lets a **configurable material** (e.g. a pump) have **characteristics** (motor power, material of construction) and **values**, chosen by the user at sales order entry. The configuration drives a **super BOM** (components selected by **selection conditions**) and a **super routing** (operations selected by dependencies), plus pricing via **variant conditions** (VA00). Tools: `CT04` characteristic, `CL02` class, `CU41` configuration profile, `CU50` configuration simulation.

Benefit: mass customisation with controlled data volume (one super BOM instead of thousands of BOMs). Risk: complex dependencies to maintain.

### Example
Industrial pump P-700: characteristics Motor (5, 7.5, 10 kW) and Casing (cast iron, stainless). That is 3 × 2 = **6 variants** from one super BOM; 6 separate BOMs would need maintenance in 6 places. A sales order for 10 kW stainless creates an MTO production order and prices the stainless premium via variant condition.

### In the news
See news box. Capital goods makers on SAP are using configuration to quote faster as part of digital selling.

### Interview angle
> [!question] How it is asked
> "How would you plan production for products that are customised per order?"

> [!tip] Strong answer includes
> - MTO vs MTS and the decoupling point idea
> - Variant configuration structure (characteristics, super BOM, dependencies)
> - Special stock concept tying production to customer order
> - Trade-offs: flexibility vs lead time and data complexity

---

## 15. ⭐ Advanced: MRP Live, Demand-Driven MRP (DDMRP) & PP/DS
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**MRP Live** (`MD01N`) is HANA-optimised, uses set-based processing and parallelism, and is available in S/4HANA only; classic `MD01` is retained for compatibility.

**DDMRP** (Demand Driven Material Requirements Planning, Ptak and Smith) replaces forecast-driven netting with **strategic decoupled buffers** at positions in the BOM. Buffer zones: **green** (order size), **yellow** (average demand during decoupled lead time, DLT), **red** (safety, split by lead-time and variability factors). Net flow position = on-hand + on-order − qualified demand; when it falls into the yellow zone, order up to the top of green. Demand-driven planning is supported in S/4HANA via the DDMRP functionality, with buffer positioning and adjustments.

**PP/DS** (embedded in S/4HANA) adds finite, detailed scheduling with heuristics and optimisation, with planning table and constraints, for complex lines with sequencing needs.

Selection logic: stable demand: classic MRP; volatile demand and long chains: DDMRP; tight capacity and sequence-dependent changeovers: PP/DS.

### Example
Component with average daily usage 100, DLT 10 days, variability factor 0.5, lead-time factor 0.5. Yellow = 100 × 10 = 1,000. Red base = 1,000 × 0.5 = 500 plus red safety = 500 × 0.5 = 250, so red = 750. Green = e.g. 500 (order cycle). Top of green = 750 + 1,000 + 500 = **2,250**. If net flow position is 1,600 (below top of yellow = 1,750), order 2,250 − 1,600 = **650**.

### In the news
See news box. After supply shocks, planners are revisiting buffers in positions with high variability; DDMRP gives a structured way to hold and review them.

### Interview angle
> [!question] How it is asked
> "How would you reduce bullwhip and stock-outs in a manufacturing plant with volatile demand?"

> [!tip] Strong answer includes
> - Limits of forecast-based MRP under volatility
> - DDMRP buffer positioning, zones and net flow position
> - MRP Live and PP/DS where capacity is the constraint
> - Metrics to prove improvement: inventory days, service level, expedite count

---
## 🔗 Go deeper: expansion notes
- [[193 SAP MRP Deep Dive - Planning Strategies & Parameters|SAP MRP Deep Dive - Planning Strategies & Parameters]]
- [[194 SAP Production Execution, Confirmation & Product Costing|SAP Production Execution, Confirmation & Product Costing]]
- [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows|SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]
