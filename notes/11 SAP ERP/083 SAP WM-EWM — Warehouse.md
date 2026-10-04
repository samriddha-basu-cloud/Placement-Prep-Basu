---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP WM/EWM — Warehouse"
tier: Tier 2
roles: Operations
status: complete
subtopics: 12
---
# SAP WM/EWM — Warehouse

⬅ [[082 SAP SD — Sales & Distribution]] · [[_Index - SAP ERP|SAP ERP]] · [[084 SAP QM & PM]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. WM vs EWM]]
2. [[#2. WM Organizational Structure]]
3. [[#3. Transfer Order (LT01/LT0A)]]
4. [[#4. Transfer Requirement]]
5. [[#5. Inventory in WM]]
6. [[#6. Putaway Strategies]]
7. [[#7. Picking Strategies]]
8. [[#8. EWM Warehouse Order]]
9. [[#9. Cross Docking in EWM]]
10. [[#10. Labor Management in EWM]]
11. [[#11. ⭐ Advanced: Slotting, ABC-Velocity Zoning & Warehouse KPIs]]
12. [[#12. ⭐ Advanced: Embedded vs Decentralised EWM & Warehouse Automation (MFS)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): warehouse systems ride the S/4HANA migration wave
> **ECC clock is ticking (Gartner figures, end-2024).** Mainstream maintenance for SAP ERP 6.0 (ECC, EHP 6–8) ends on **31 Dec 2027**, extended maintenance to **31 Dec 2030**. Gartner estimated only **39% of SAP's ~35,000 ECC customers (~14,000)** had bought S/4HANA transition licences by end-2024. For ECC users on classic WM, the migration forces a decision between staying on WM (compatibility scope) and moving to EWM. ([SoftwareSeni summary](https://www.softwareseni.com/what-sap-ecc-end-of-support-actually-means-and-why-17000-companies-are-not-ready/); secondary source quoting Gartner. The WM/EWM implication is the note author's analysis, not stated in that source.)
> 
> **GAIL goes live on RISE with SAP (formal launch 25 Jun 2025).** GAIL described itself as the first Maharatna PSU to move from legacy ECC to S/4HANA on cloud ("Navodaya"), delivered within one year. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
> 
> **SAP Q4 2025 (29 Jan 2026).** Current cloud backlog +25% constant currency (+16% reported); 2026 guidance 23–25% cloud revenue growth; Business AI in about two-thirds of Q4 cloud orders. ([Constellation Research](https://www.constellationr.com/insights/news/saps-q4-cloud-backlog-spurs-concerns))
> 
> Sub-topics that say **"See news box"** reuse these items. Related: [[080 SAP MM — Materials Management]], [[082 SAP SD — Sales & Distribution]].

---
## 1. WM vs EWM
> 🟠 Tier 2 · _Tracker hint:_ WM = classic warehouse mgmt; EWM = extended, more features, decentralized option

### Definition
**WM (Warehouse Management)** is the classic SAP warehouse module embedded in ERP (ECC and the S/4HANA compatibility scope). It manages stock by **storage bin** within a warehouse number, using transfer orders and requirements.

**EWM (Extended Warehouse Management)** is the advanced warehouse application, originally a separate SCM component, now available **embedded in S/4HANA** (basic and advanced) or as a **decentralised** system on its own server connected to ERP/S/4HANA.

| | WM | EWM |
|---|---|---|
| Work document | Transfer order (TO) | Warehouse task (WT) and warehouse order (WO) |
| Inbound/outbound docs | Delivery in SD/MM | Inbound / outbound delivery with warehouse requests |
| Storage control | Basic | Process- and layout-oriented storage control |
| Features | Putaway, picking, cycle counting | Wave management, labour management, yard management, slotting, cross-docking, RF framework, material flow system (MFS) for automation, value-added services |
| Strategy | Compatibility scope; SAP has extended its availability window, check SAP Note 2269324 for the current date | Strategic warehouse product |

Rule of thumb: WM for simple, low-complexity warehouses; EWM for high volumes, automation, 3PLs and complex processes.

### Example
A small plant warehouse with 500 bins and manual forklifts uses WM. A national FMCG distribution centre with 50,000 bins, RF devices, waves and AGVs uses EWM. A 3PL serving several clients may need EWM for multi-client handling and value-added services (labelling).

### In the news
See news box. For ECC customers using classic WM, the S/4HANA move triggers the WM-to-EWM decision; embedded EWM reduces integration effort compared with a separate system.

### Interview angle
> [!question] How it is asked
> "When would you choose EWM over WM?" or "What is the difference between embedded and decentralised EWM?"

> [!tip] Strong answer includes
> - Capabilities difference: waves, labour, yard, automation (MFS)
> - Embedded (shared database, simpler) vs decentralised (separate system, scalability, decoupled uptime)
> - Decision criteria: complexity, volumes, automation, 3PL needs, TCO
> - Awareness of SAP's roadmap, with the caveat to check current notes

---

## 2. WM Organizational Structure
> 🟠 Tier 2 · _Tracker hint:_ Warehouse Number → Storage Type → Storage Section → Storage Bin

### Definition
WM org units form a hierarchy below the plant/storage location:

| Level | Meaning |
|---|---|
| **Warehouse number** | Complete warehouse complex; assigned to plant + storage location combination (`OX09`, `OMKV`) |
| **Storage type** | Physical or logical area with its own rules, e.g. high-rack, bulk, fixed-bin picking, goods receipt area (001), goods issue (916) |
| **Storage section** | Subdivision of a storage type (e.g. fast movers) used for strategies |
| **Storage bin** | Smallest addressable location (e.g. 05-12-03) with capacity and bin type |
| **Quant** | Quantity of material in a bin; the unit where stock is kept in WM |
| **Interim storage types** | Goods receipt area, goods issue area, differences |
| **Staging area, door** | Support for picking and shipping |

Link to IM (inventory management): stock quantity per storage location in IM equals the sum of quants in WM for the warehouse number. T-codes: `LS01N` create bin, `LS03N` display bin, `LX02` stock per bin, `LX03` bin status report, `LS24` stock per material.

### Example
Warehouse 100 (plant 1100, sloc 0001): storage types 001 GR zone, 010 high-rack, 020 fixed-bin picking, 916 GI zone. In 010 section "A" holds pallets, bins 01-02-03 etc. 1,000 kg of resin is held as 2 quants: 600 kg in bin 01-02-03 and 400 kg in 01-02-04.

### In the news
See news box. In migration projects warehouse structure and bin master data must be mapped carefully to the target (WM or EWM).

### Interview angle
> [!question] How it is asked
> "Explain the WM structure from warehouse number to bin" or "What is a quant?"

> [!tip] Strong answer includes
> - Warehouse number, storage type, section, bin, quant in order
> - Role of interim storage types (GR/GI zones)
> - Assignment to plant and storage location
> - Example of how stock is split into quants

---

## 3. Transfer Order (LT01/LT0A)
> 🟠 Tier 2 · _Tracker hint:_ Physical document for warehouse movement; TO = pick/put-away instruction

### Definition
A **transfer order (TO)** is the WM document instructing warehouse staff to move material from a **source** bin to a **destination** bin (put-away, picking, stock transfer, replenishment). It includes material, quantity, source and destination storage types and bins, and is processed as a pick/putaway list.

Creation:
- `LT01` create TO manually (for a movement type without prior requirement).
- From a **transfer requirement** (`LT03` by TR) or from a delivery (`LT04`); TO creation can be automatic or from collective lists.
- The tracker lists `LT0A`; check your system for exact transaction names, because variants differ by release.

Processing: **TO confirmation** (`LT12`, single; `LT25` list) confirms physical movement and updates quants, and may be required or not depending on storage type settings. Without confirmation the TO remains open and stock is "in transit" between bins. Cancel with `LT15`; display `LT21`. TO status: open, confirmed, partially confirmed, cancelled.

Posting change notice: TO confirmation completes the WM part; IM is updated by the goods movement (GR/GI), which may be done before or after.

### Example
Put-away of 20 pallets of resin: TO 0000001234, source 001 GR zone (bin 'GR-ZONE'), destination 010 (bin 01-02-03). The stacker driver prints the TO, moves the pallets and confirms in `LT12`. If 2 pallets are damaged, the TO is confirmed for 18 and a difference is posted for 2 into the differences storage type.

### In the news
See news box. Real-time RF-based confirmations reduce the lag between physical and system stock; EWM replaces TOs by warehouse tasks.

### Interview angle
> [!question] How it is asked
> "What is a transfer order and how is it different from a transfer requirement?"

> [!tip] Strong answer includes
> - TO as the actual movement instruction with source and destination
> - Creation sources: manual, TR, delivery
> - Confirmation and what it updates (quants)
> - Handling of differences (partial confirmation)

---

## 4. Transfer Requirement
> 🟠 Tier 2 · _Tracker hint:_ Created by goods movement; triggers TO creation; auto or manual

### Definition
A **transfer requirement (TR)** is a request to the warehouse to move material, generated by another application and **not** a movement itself. Sources: **goods receipt** from MM (101 creates a TR to put goods away from the GR zone), **goods issue** requirements from PP (components to a production supply area), and **inventory management** transfers.

TR properties: material, quantity, requirement type, **movement type**, **required date**, **storage type of source/destination**, plant. A TR remains open until it is covered by one or more TOs. Display and process: `LB10` (TRs for storage location), `LB11` (display TR), `LB01` (create TR manually), `LT03` (create TO for TR).

Settings: the warehouse can be configured so TO creation happens **automatically** (immediately after the TR) or **in background / collective** (`LT04`, `LB10` lists), depending on the storage type and process. TR vs TO: TR = "what is needed", TO = "how it is moved". TRs help planners group demand and **release work** to the floor.

### Example
A GR of 20 pallets posts a TR to put the pallets from the GR zone. If the setup is "TO created immediately", the warehouse supervisor finds a TO ready. If it is "collective", TRs accumulate until `LB10` is run at 4 pm to build TOs for the night shift.

### In the news
See news box. In EWM the equivalent concept is the warehouse request/delivery document, which creates warehouse tasks.

### Interview angle
> [!question] How it is asked
> "How is a TO generated in WM?" or "TR vs TO?"

> [!tip] Strong answer includes
> - TR is the demand signal, TO the executable document
> - Sources of TR: GR, GI/production supply, manual
> - Immediate vs collective TO creation
> - How this controls workload release

---

## 5. Inventory in WM
> 🟠 Tier 2 · _Tracker hint:_ Cycle counting (LX26); annual inventory; bin-level inventory management

### Definition
WM offers inventory methods operating at **bin (quant) level**:
- **Periodic (annual/year-end) inventory:** physical count of all stock on one date (stock frozen); count documents, entry and difference posting.
- **Continuous inventory:** counts spread over the year per storage bin.
- **Cycle counting:** materials classified into **cycle-counting indicators A/B/C** with different frequencies (e.g. A items 4 times a year, B twice, C once); `LICC` (cycle counting) creates inventory records for due materials.
- **Inventory on demand / zero-stock check:** count when a bin is emptied or when a stock check triggers a difference.
- **Inventory sampling** (for statistical estimation).

Process: block bins (optionally) → **create inventory record** (`LI01N`/`LICC`) → print count document → **enter count** (`LI11N`) → **recount** if tolerance exceeded → **post differences** (`LI20`) with the difference then synchronised with IM (movement types 701/702). `LX25` and the tracker's `LX26` provide inventory status reports.

Benefit of cycle counting: accuracy without shutting the warehouse; focus on high-value items.

### Example
10,000 SKUs: A 1,000 items (counted 4×) = 4,000 counts, B 3,000 (2×) = 6,000, C 6,000 (1×) = 6,000 counts per year, totalling **16,000 counts** (roughly 64 per working day over 250 days). Compare with a once-a-year full count of 10,000 SKUs requiring warehouse shutdown.

### In the news
See news box. Drones and RFID are being used to speed counts but the SAP posting process stays the same.

### Interview angle
> [!question] How it is asked
> "How would you improve inventory accuracy in a warehouse?"

> [!tip] Strong answer includes
> - Cycle counting by ABC class (frequency rationale)
> - Root causes: receiving errors, mis-picks, unrecorded scrap, master data
> - SAP steps: record, count, recount, post difference
> - KPI: inventory record accuracy, shrinkage

---

## 6. Putaway Strategies
> 🟠 Tier 2 · _Tracker hint:_ Fixed bin, open storage, addition to existing stock, next empty bin, FIFO

### Definition
A **putaway strategy** decides the destination bin for incoming stock; it is set per **storage type** (and overridable per material).

| Strategy | How it works | Typical use |
|---|---|---|
| Fixed bin | Material has a dedicated bin | Fast-moving picking areas |
| Open storage | Any free area/bin of the storage type | Bulk, floor storage |
| Addition to existing stock | Adds to bin already containing the same material (and batch), subject to capacity | Space-efficient, same-SKU consolidation |
| Next empty bin | Uses the next free bin by search sequence | Rack storage, discrete pallets |
| Near picking bin / bulk storage by bin type | Considers capacity and storage unit type (pallet, box) | Pallet racking with different bin sizes |

Constraint checks: **capacity**, **storage type search**, **storage section search**, **hazardous material**, **FIFO** or batch separation. Putaway is first determined on the TO creation, then confirmed by the operator; SAP can also optimise by **bin capacity (weight, volume, number of pallets)**.

A well-designed strategy balances **space use**, **travel time** and **pick accuracy**.

### Example
Incoming 10 pallets of detergent (A-class). Strategy for high-rack: "addition to existing stock" fills a half-empty bin (capacity 4 pallets, currently 2, so 2 more) and uses next empty bins for the remaining 8, minimising partial bins. For a fast mover with a fixed pick bin, replenish the bin from reserve.

### In the news
See news box. Slotting optimisation using AI is a growing add-on in EWM-based warehouses.

### Interview angle
> [!question] How it is asked
> "How would you decide where to store incoming goods?"

> [!tip] Strong answer includes
> - Strategy options with when each fits
> - ABC/velocity-based zoning (fast movers close to dock)
> - Capacity and compatibility constraints
> - Impact on travel distance and pick productivity

---

## 7. Picking Strategies
> 🟠 Tier 2 · _Tracker hint:_ FIFO, FEFO (expiry), partial pallet, fixed bin; configured per storage type

### Definition
**Stock removal (picking) strategies** determine which quant is picked, set per storage type:
- **FIFO** (first in, first out): oldest goods-receipt date first. Standard.
- **LIFO:** last in, first out (bulk piles).
- **FEFO** (first expired, first out): earliest **shelf-life expiry date** first, essential in food, pharma.
- **Partial pallet first:** picks incomplete pallets to clear loose stock; avoids many partials.
- **Fixed bin / pick bin:** picks from the fixed picking bin; replenished from bulk.
- **Large/small quantity strategy:** full pallets for large orders, picking from pick area for small ones.

Picking methods: **discrete, batch, zone, wave**, or **cluster picking**. Picking productivity: $\text{Lines per hour} = \frac{\text{order lines picked}}{\text{labour hours}}$; $\text{Pick accuracy} = \frac{\text{correct lines}}{\text{lines picked}}$.

Pick strategies tie into delivery: TO for delivery picks according to the strategy, then **PGI** (movement 601).

### Example
Warehouse holds yoghurt batch A (expiry 10 Nov, 40 cases), batch B (expiry 5 Nov, 30 cases). Order for 50 cases under FEFO: pick 30 from B and 20 from A. FIFO by receipt date could have picked the later-expiring batch first and left B to expire (loss ≈ 30 cases × ₹360 = ₹10,800).

### In the news
See news box. In perishables and pharma, expiry-based picking (FEFO) is a compliance and waste-reduction lever, and S/4HANA batch management supports it.

### Interview angle
> [!question] How it is asked
> "FIFO or FEFO, which do you choose and why?"

> [!tip] Strong answer includes
> - Strategy definitions and when each applies
> - Shelf-life and regulation as the deciding factor
> - Picking method (zone, wave) vs strategy distinction
> - KPIs: pick accuracy, lines per hour, write-offs due to expiry

---

## 8. EWM Warehouse Order
> 🟠 Tier 2 · _Tracker hint:_ Groups transfer orders; optimized for labor; wave management

### Definition
In EWM the executable unit is the **warehouse task (WT)** (equivalent of a TO item). A **warehouse order (WO)** groups several WTs into a work package for one worker or resource, built using **warehouse order creation rules (WOCR)** that consider **activity area, route, queue, capacity limits, maximum weight/volume, number of items**.

**Wave management:** **waves** group outbound delivery items (by carrier cut-off, route or priority) so picking is released in a controlled batch. Wave creation: manual or automatic with a **wave template**. Benefits: **balanced labour, shorter travel, aligned dock schedule**.

Typical flow: outbound delivery order → **wave** → warehouse tasks → **warehouse orders** assigned to queues → RF confirmation → packing → goods issue. Monitor: `/SCWM/MON` (warehouse management monitor), RF transactions via ITS or Fiori.

Compared with WM TOs: more **optimisation** (grouping, sorting by travel path), **resource management** (assign WOs to users by qualification), integrated **yard** and **loading**.

### Example
Outbound for 1,200 order lines due 6 pm. Waves: wave 1 (12:00 cut-off, 400 lines), wave 2 (14:00, 500 lines), wave 3 (16:00, 300 lines). Each WO limited to 30 lines or 500 kg, so wave 1 produces about 14 WOs (400 / 30 = 13.3 → 14).

### In the news
See news box. Fulfilment centres for e-commerce and quick commerce rely on this wave-and-order logic to keep pick productivity high.

### Interview angle
> [!question] How it is asked
> "How does EWM organise work for pickers and how do waves help?"

> [!tip] Strong answer includes
> - WT vs WO and how WOs are created from rules
> - Wave concept and cut-off alignment
> - Labour balance and travel minimisation
> - Monitoring and exception handling

---

## 9. Cross Docking in EWM
> 🟠 Tier 2 · _Tracker hint:_ Planned cross docking; opportunistic; direct flow without storage

### Definition
**Cross-docking** moves goods from inbound to outbound with little or no storage in between, saving putaway and picking effort and reducing inventory.

In EWM:
- **Planned cross-docking (PCD):** inbound and outbound documents are linked **in advance** (e.g. by a **transportation cross-docking** or merchandise distribution method), so receipt is directed to the outbound door/staging area. Typical in retail distribution (**merchandise distribution cross-docking**, MDCD, where goods are allocated to stores) or when inbound ASN matches known outbound orders.
- **Opportunistic cross-docking (OCD):** the system **detects at goods receipt** that the received product is needed by a waiting outbound delivery and redirects it, even if not planned.
- **Direct flow** (no storage): goods go straight from inbound dock to outbound dock, in contrast to storage-based flow.

Requirements: reliable ASNs, a matching **time window**, a **staging area**, and tight coordination with transport. Metrics: **dock-to-dock time**, **cross-dock share**, **dwell time**.

### Example
A retailer receives 2,000 cartons of soft drinks from the plant at 8 am, to supply 20 stores by 2 pm. Planned cross-docking allocates 100 cartons per store; trucks are loaded in the same shift: dwell time 3 hours instead of 1.5 days, avoiding 2,000 putaway and pick moves.

### In the news
See news box. Faster retail replenishment (quick commerce, modern trade) pushes more cross-dock flows.

### Interview angle
> [!question] How it is asked
> "When is cross-docking appropriate and how does EWM support it?"

> [!tip] Strong answer includes
> - Definition and benefits: less inventory, faster flow
> - Planned vs opportunistic cross-docking
> - Prerequisites: accurate ASN, predictable demand, synchronised transport
> - Risks: delays cascade, no buffer

---

## 10. Labor Management in EWM
> 🟠 Tier 2 · _Tracker hint:_ Queue-based work assignment; performance benchmarking; incentive wages

### Definition
**Labour management (LM)** in EWM plans, monitors and evaluates warehouse employee workload using **engineered labour standards**.
- **Planned times** per activity (e.g. pick a carton = 12 s, travel 1.2 m/s) from **calculation profiles** and formulas using quantity, weight, distance.
- **Indirect labour** tasks (cleaning, breaks) handled with **indirect-labour tasks**.
- **Queue-based work assignment:** WOs assigned to queues and resources; RF users **log on to a queue** and receive the next WO.
- **Performance measurement:** actual vs planned time gives **performance %**: $\text{Performance} = \frac{\text{planned time}}{\text{actual time}} \times 100$.
- **Incentive wages:** performance data passed to HR/payroll to compute productivity pay.
- **Workload forecasting:** compare predicted load (from deliveries) with available labour to plan shifts.

Benefits: labour productivity, fair incentive pay, transparency. Risks: perverse incentives (speed vs accuracy), worker pushback, so pair with quality KPIs.

### Example
Planned time for a pick task: 90 s; actual: 120 s → performance = 90/120 = **75%**. An operator completing 100 tasks planned at 150 min of work in 120 min of actual time performs at 125%, which could qualify for an incentive tier (company policy-defined).

### In the news
See news box. Labour is the largest warehouse operating cost and tightening labour markets in logistics make productivity tools more important.

### Interview angle
> [!question] How it is asked
> "How would you improve warehouse labour productivity?"

> [!tip] Strong answer includes
> - Engineered standards and measurement (planned vs actual)
> - Queue/RF-based task assignment and workload forecast
> - Incentives with balancing quality metrics
> - Change management with labour representatives

---

## 11. ⭐ Advanced: Slotting, ABC-Velocity Zoning & Warehouse KPIs
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Slotting** assigns SKUs to bin locations based on **velocity (ABC), cube, weight, affinity (items ordered together)** to minimise travel and handling. Common design: **A items** (about 20% of SKUs, ~80% of picks) in the **golden zone** (waist-high, near dock); C items on high levels or deep storage. **Re-slotting** is periodic as demand shifts.

Core KPIs:
- **Dock-to-stock time** = time from receipt to put-away complete.
- **Order picking accuracy** = correct lines / total lines.
- **Order cycle time** = order release to ship.
- **Inventory record accuracy** = bins counted correct / bins counted.
- **Warehouse space utilisation** = used space / available space.
- **Cost per order line** = total warehouse cost / lines.
- **Productivity** = lines (or units) per labour hour.

EWM supports **slotting** via storage-bin sorting, storage-type search and **ABC indicator** to guide putaway. Layout principle: **Pareto**, **cube-per-order index (COI)** = space required / orders per period; lower COI nearer the dock.

### Example
Warehouse with 2,000 SKUs; top 400 SKUs (20%) account for 80% of 50,000 monthly pick lines (40,000 lines). Moving them from the far end to a zone 30 m closer saves around 30 m × 2 (round trip) per pick cluster; at 40,000 lines and a cluster of 10 lines, that is 4,000 trips × 60 m = **240 km saved a month**.

### In the news
See news box. Quick-commerce dark stores depend on slotting discipline (small footprint, high SKU velocity) to meet 10-minute delivery promises.

### Interview angle
> [!question] How it is asked
> "A warehouse's pick productivity has dropped 20%. What do you do?"

> [!tip] Strong answer includes
> - Diagnosis with data: pick path, travel time, SKU velocity, congestion
> - Slotting/ABC and re-slotting; batch or zone picking
> - KPI set to track
> - Process fixes plus systems fixes (RF, EWM labour management)

---

## 12. ⭐ Advanced: Embedded vs Decentralised EWM & Warehouse Automation (MFS)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Embedded EWM** runs in the same S/4HANA instance as ERP, sharing the database and master data (Business Partner, product). Simpler landscape, no replication via CIF/core interface, lower TCO and comes in a **basic** and an **advanced** variant (check SAP's current licensing and scope documentation).

**Decentralised EWM** runs on a separate system (own database) connected via integration (queues, qRFC). Advantages: warehouse uptime independent from ERP, scaling for very high volumes, can serve several ERPs. Costs: master-data distribution and more interfaces.

**Material Flow System (MFS):** EWM's interface to automated equipment (conveyors, shuttles, AS/RS) through **PLC / warehouse control system (WCS)** telegrams; EWM sends tasks and receives status and events. **Process-oriented storage control** (POSC) and **layout-oriented storage control** route handling units through steps (decon, pack, stage).

Robotics (AGVs, AMRs) typically integrate through the same MFS or a warehouse control system layer.

### Example
A pharma 3PL with 4 ERP clients chooses decentralised EWM so one warehouse can serve all, keeping running even when a client's ERP is down. A single-plant manufacturer on S/4HANA picks embedded EWM to avoid an additional system.

### In the news
See news box. As companies move to S/4HANA, embedded EWM is often the default choice unless scale or multi-ERP needs justify decentralisation.

### Interview angle
> [!question] How it is asked
> "Embedded or decentralised EWM for this client? And how would you integrate an automated storage system?"

> [!tip] Strong answer includes
> - Differences in database, integration, uptime, scale, cost
> - Decision criteria with explicit assumptions
> - MFS and WCS/PLC integration basics
> - Risk management: cut-over, performance testing, fall-back processes

---
## 🔗 Go deeper: expansion notes
- [[197 SAP EWM Deep Dive - Process-Oriented Warehousing|SAP EWM Deep Dive - Process-Oriented Warehousing]]
- [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)|SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]]
