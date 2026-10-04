---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP EWM Deep Dive - Process-Oriented Warehousing"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP EWM Deep Dive - Process-Oriented Warehousing

⬅ [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]] · [[_Index - SAP ERP|SAP ERP]] · [[198 SAP IBP, APO & Demand-Driven Planning]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. EWM Positioning: Embedded, Decentralised, WM and Logistics Management]]
2. [[#2. EWM Organisational Structure]]
3. [[#3. Product, Packaging and Handling-Unit Master Data]]
4. [[#4. Warehouse Process Types and Storage Control]]
5. [[#5. Warehouse Tasks, Orders, Queues and Resources]]
6. [[#6. Inbound Process: ASN, Goods Receipt and Putaway]]
7. [[#7. Outbound Process: Delivery, Picking, Packing, Loading and Goods Issue]]
8. [[#8. Wave Management]]
9. [[#9. RF Framework and Mobile Execution]]
10. [[#10. Physical Inventory and Cycle Counting]]
11. [[#11. Slotting and Yard Management]]
12. [[#12. Warehouse Automation, Robotics and Material Flow System]]
13. [[#13. ⭐ Advanced: End-to-End Inbound-to-Outbound Walkthrough and KPIs]]
14. [[#14. ⭐ Advanced: WM-to-EWM Migration and Cut-over Considerations]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): SAP EWM becomes the context layer for warehouse robots and AI
> **SAP reports a 12th consecutive Gartner Magic Quadrant Leader placement for Warehouse Management Systems (4 May 2026).** In its own announcement SAP cites EWM capabilities such as APIs for robotics integration, predictive labour demand planning, AI-assisted slotting optimisation, embedded Joule natural-language interaction, "customers across 24 industries", support for SAP and non-SAP ERP environments, and a portfolio split between **SAP EWM** (complex operations) and **SAP Logistics Management** (launched February 2026, for local, satellite and mid-scale sites). (Vendor-published report of the analyst result: [SAP News Center, 4 May 2026](https://news.sap.com/2026/05/sap-leader-2026-gartner-magic-quadrant-warehouse-management-systems/))
>
> **Humanoid and robotic pilots driven by EWM (5 November 2025).** SAP described nine pilots in which EWM or SAP Logistics Management supplies tasks and business context to robots: Bosch (humanoid picking, deployed in 10 working days), Vodafone Procure & Connect (warehouse inspection in Duisburg), Mahindra & Mahindra (visual identifier checks, potential up to 3x throughput and 67% less manual verification), Martur Fompak (up to 5x throughput), Tetra Pak (inbound verification, projected 10–20% accuracy gain), Arçelik-LG, BITZER and Sartorius. The throughput figures are described as potential or pilot results, not audited benefits. ([SAP News Center, 5 Nov 2025](https://news.sap.com/2025/11/sap-physical-ai-partnerships-new-robotics-pilots/))
>
> **EWM in the SAP logistics suite (April 2025).** SAP's report on its 11th consecutive Leader placement in the Gartner Magic Quadrant for Transportation Management Systems lists an integrated set of SAP Transportation Management, SAP Extended Warehouse Management, SAP Yard Logistics and SAP Business Network for Logistics, with shipping and receiving orchestration between TM and EWM. ([SAP News Center, 1 Apr 2025](https://news.sap.com/2025/04/sap-a-leader-gartner-magic-quadrant-transportation-management-systems/))
>
> Sub-topics that say **"See news box"** reuse these items. Basics of WM vs EWM are in [[083 SAP WM-EWM — Warehouse]]; engineering context is in [[010 Warehouse Management]] and [[128 Warehouse Labour, WES-WCS & Yard Management]].

---
## 1. EWM Positioning: Embedded, Decentralised, WM and Logistics Management
> 🟠 Tier 2 · _Key points:_ Embedded vs decentralised EWM; basic vs advanced; WM compatibility; Logistics Management for mid-scale sites

### Definition
**SAP Extended Warehouse Management (EWM)** is SAP's process-oriented warehouse application. Deployment choices:
- **Embedded EWM** in S/4HANA: same system and database as ERP, shared product and business partner master data, no master data distribution or core interface; simplest landscape. SAP offers a basic and an advanced scope with different licensing (check SAP's current licence terms before promising features).
- **Decentralised EWM:** a separate system (own database) connected to ERP by queued RFC or integration; independent uptime and scaling, one EWM can serve several ERPs, costs more interfaces and duplicated master data.
- **Classic WM (compatibility scope):** the transfer-order-based module in ECC and S/4HANA; the availability date is governed by SAP Note 2269324 (check the current date, as SAP has extended it before).
- **SAP Logistics Management:** per the May 2026 SAP announcement (news box), a newer offering for local, satellite and mid-scale operations, with EWM for complex ones.

Decision factors: volume and complexity, automation (conveyors, shuttles, robots), multi-client 3PL needs, ERP landscape, integration effort, and total cost. Concepts of WM/EWM contrast are covered in [[083 SAP WM-EWM — Warehouse]].

### Example
Three sites: a 3PL with 6 client ERPs (decentralised EWM), an automotive plant on S/4HANA with a high-bay and 40 RF users (embedded EWM, advanced scope), and a regional depot with 800 bins and manual handling (stay on WM or choose the lighter offering). Rule: one warehouse number maps to one EWM system.

### In the news
See news box. SAP's portfolio statement signals that EWM is for complex operations, while a lighter product covers satellites.

### Interview angle
> [!question] How it is asked
> "Embedded or decentralised EWM for a client with five plants and one ERP?"

> [!tip] Strong answer includes
> - Embedded as default for a single S/4HANA landscape; decentralised for multi-ERP, high scale or independent uptime
> - Licensing and scope caveats, and the alternatives (WM, lighter product)
> - Criteria, assumptions, and a TCO view
> - Awareness that SAP dates must be checked at the source

---
## 2. EWM Organisational Structure
> 🟠 Tier 2 · _Key points:_ Warehouse number, storage type, storage section, storage bin, activity area, work centre, staging area, door, yard

### Definition
Hierarchy (largest to smallest):
- **Warehouse number:** the top organisational unit, a complete warehouse with its own configuration; assigned to the ERP plant and storage location (a plant/storage location pair maps to one warehouse number).
- **Storage type:** a physical or logical area with common behaviour (high-rack, floor block, picking area, goods-receipt zone, shipping zone), with its own putaway and removal strategies, capacity check and role (for example "storage type role: standard storage type, identification point, pick point").
- **Storage section:** subdivision of a storage type (fast movers, heavy items).
- **Storage bin:** the smallest location, with a **bin type** (dimension and load limit) and a **coordinate** for travel distance.
- **Activity area:** a group of bins (possibly across storage types) used for work: **picking area, putaway area, inventory area**. Warehouse orders are built within one activity area, so it is the main lever for worker routes and zones.
- **Work centre:** a special location with specific functions (packing, deconsolidation, quality inspection, value-added service).
- **Staging area/group, door, and yard** (checkpoint, yard bin) for goods receipt and issue.
- **Quant:** stock of a product in a bin (product, batch, quantity, owner, stock type, handling unit).

Stock is held by **ownership and stock type** inside EWM and is reconciled to ERP through a stock-integrity process.

### Example
Warehouse number 1100 (Bhiwandi DC): storage types 0010 (goods receipt), 0020 (reserve pallets, high rack), 0030 (carton flow pick), 0040 (packing), 0050 (goods issue). Activity areas: A-PICK (0030 aisles 1 to 6), B-PICK (aisles 7 to 12), so two pickers can work in parallel. Quant: 40 cartons of product SKU-77, batch B12, in bin 0030-03-05-02.

### In the news
See news box. Robot pilots select tasks from EWM, which relies on this structure for bins, task priorities and storage locations.

### Interview angle
> [!question] How it is asked
> "Explain the EWM organisational structure and what an activity area does."

> [!tip] Strong answer includes
> - Order of the hierarchy and a physical example
> - Activity area for work grouping, versus storage type for stock strategy
> - Work centres and staging for packing and shipping
> - Link to plant and storage location in ERP

---
## 3. Product, Packaging and Handling-Unit Master Data
> 🟠 Tier 2 · _Key points:_ Warehouse product data, packaging specification, handling units, serial and batch, storage bin types

### Definition
- **Product master** (same as ERP material or product; in embedded EWM shared) extended by **warehouse data**: storage type indicators, putaway control indicator, stock removal control indicator, unit of measure for handling (**alternative UoM**), shelf life and **batch** handling, hazardous goods.
- **Packaging specification:** defines how products are packed into **handling units (HU)** with maximum quantity per carton or per pallet, packaging material and packing instructions; used in pack stations to propose content.
- **Handling unit (HU):** a physical unit (pallet, carton, container) with an ID (SSCC) that holds products and moves as one object; tracked in the system, often with nested HU. HU-based processes reduce scans and errors.
- **Storage bin type and putaway rules** decide which bin accepts which HU, and **capacity** constraints (weight, volume, number of HUs).

Master-data quality (dimensions, weights, units, pack data) drives slotting, putaway, load planning and picking accuracy (see [[175 Data Quality, Master Data & Data Governance]] and [[140 Packaging, Unitisation & Load Optimisation]]).

### Example
Product SKU-77: 12 units per carton, 60 cartons per pallet (EUR pallet, SSCC-labelled), carton 5 kg and 0.02 m³. Pallet = 720 units, 300 kg net, 1.2 m³. A bin type for pallets allows one HU up to 1,000 kg. A wrong carton weight of 0.5 kg in master data would let the system plan 10 times as many cartons into a pick WO as the picker can carry.

### In the news
See news box. Robotic picking pilots depend on accurate product dimensions and HU structures from the system.

### Interview angle
> [!question] How it is asked
> "Why do handling units matter in EWM, and what master data does packing rely on?"

> [!tip] Strong answer includes
> - HU as the unit of movement and tracking
> - Packaging specification and capacity limits
> - Impact of wrong dimensions or weights downstream
> - Governance: validation at product creation

---
## 4. Warehouse Process Types and Storage Control
> 🟠 Tier 2 · _Key points:_ Warehouse process type, activity, layout-oriented and process-oriented storage control, WT per step

### Definition
A **warehouse process type (WPT)** is the control object for any movement: it determines the **activity** (putaway, picking, posting change, replenishment, physical inventory), confirmation settings (whether a confirmation is required, HU confirmation, differences), and **WT creation** behaviour. In SAP standard examples include 1010 for putaway and 2010 for picking; companies define their own per movement type.

**Storage control** defines the path of goods through several steps:
- **Layout-oriented storage control:** the route follows the physical layout, through intermediate storage types (for example goods receipt zone → conveyor → identification point → high rack), with a **WT for each step**.
- **Process-oriented storage control:** the route follows **process steps** such as unload, count, quality inspection, deconsolidate, pack, stage, load; each step is a **work centre** or location and has its own WT or task. It can add steps depending on product, HU type or delivery.
- **Determination:** WPT, storage control and strategies come from **determination tables** based on warehouse number, movement type, product group, and so on.

Outbound steps: pick → pack at a work centre → stage → load → goods issue. Inbound steps: unload → GR → deconsolidate/inspect → putaway.

### Example
Chilled food DC: inbound WPT 1010 with process-oriented storage control: Unload at dock door → temperature check at work centre QC01 → deconsolidate mixed pallets at DECON → putaway to cold storage type 0020. Outbound WPT 2010 → pick from bin → pack at PACK → stage in zone ST1 → load into truck. Each segment has a separate WT, so the progress is visible and each user receives only their step.

### In the news
See news box. Pilots with Tetra Pak and Arçelik-LG describe inbound steps (verification, storing) that map to these process steps.

### Interview angle
> [!question] How it is asked
> "What is storage control in EWM and why is it more flexible than WM?"

> [!tip] Strong answer includes
> - WPT as the central control object
> - Layout-oriented versus process-oriented control with examples
> - WT per step and visibility
> - Configuration choices and testing of determination logic

---
## 5. Warehouse Tasks, Orders, Queues and Resources
> 🟠 Tier 2 · _Key points:_ WT, WO, WOCR, queue, resource management, priorities; the executable unit of work

### Definition
- **Warehouse task (WT):** the instruction to move a quantity (or HU) from a source bin to a destination bin; carries product, quantity, process type, priority and the process step.
- **Warehouse order (WO):** a group of WTs executed by one resource in one trip; created by **warehouse order creation rules (WOCR)**, using filters and limits such as activity area, queue, **maximum number of items, weight or volume**, route, and sorting by bin coordinates for shortest path.
- **Queue:** WOs are assigned to queues (picking, putaway, replenishment, specific equipment); queue determination is based on source/destination activity area and process type. Resources log on to **queues** matching their qualification.
- **Resource management:** resources (people, forklifts) belong to **resource groups** and **resource types**; the system assigns the next WO via **RF dialogue** or **monitor** (`/SCWM/MON`). Priority and **latest start/finish** drive sequencing.
- **Confirmation:** WT confirmation posts the stock movement; **differences** and **exceptions** (bin empty, damaged goods) are handled in the monitor or by RF exception codes.

### Example
Wave with 30 delivery items, 960 cartons at 12 kg each = 11,520 kg. WOCR limits per WO: max 12 items and max 400 kg. Item rule needs 3 WOs; weight rule needs 11,520 / 400 = 28.8 → **29** WOs. The binding constraint is weight, so the system creates 29 WOs (an average of 397 kg each). Lighter limits or pallet-picking logic would reduce the count.

### In the news
See news box. SAP's EWM announcement mentions predictive labour demand planning, which works from WT and WO volumes by queue.

### Interview angle
> [!question] How it is asked
> "How does EWM turn a delivery into work for pickers, and what controls the size of each pick trip?"

> [!tip] Strong answer includes
> - Hierarchy: delivery → WT → WO → queue → resource
> - WOCR limits (items, weight, volume), activity area, sorting
> - Resource management and priorities
> - Monitoring and exception handling

---
## 6. Inbound Process: ASN, Goods Receipt and Putaway
> 🟠 Tier 2 · _Key points:_ Purchase order, ASN, inbound delivery, unloading, GR posting, putaway strategies, quality inspection

### Definition
1. **PO and ASN:** ERP PO; supplier sends **ASN** (advanced shipping notification, EDI or via a network such as [[199 SAP Ariba, SRM & Business Network]]), creating an **inbound delivery** in ERP.
2. **Replication:** the inbound delivery (or notification) is transferred to EWM as an **inbound delivery notification**, which becomes the **EWM inbound delivery**; packaging data and HUs are created from ASN or on receipt.
3. **Yard and dock:** truck check-in, door assignment (optional yard process), unloading.
4. **Goods receipt:** posting GR in EWM updates stock and triggers the **ERP goods movement** (movement type 101, see [[080 SAP MM — Materials Management]]); GR can be blocked pending QA.
5. **Putaway:** WT created by **putaway strategy**: fixed bin, open storage, addition to existing stock, empty bin, near picking bin, pallet-specific; destination bin chosen by storage type search sequence; confirmation (RF) completes the movement.
6. **Quality inspection:** optional inspection at a work centre (see [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]]).

Control points: ASN accuracy, tolerance on delivered quantity, and HU label (SSCC) readability.

### Example
ASN for 6,000 cartons; 60 cartons per pallet gives **100 pallets**. Two doors each unload 10 pallets an hour: **5 hours**. Putaway to high-rack storage type with 120 bins: after putaway, 100 of 120 bins are used (**83.3%** utilisation); 20 spare bins remain for the next inbound. KPI: dock-to-stock time target 4 hours from GR posting.

### In the news
See news box. Tetra Pak's pilot uses robot-assisted verification at the inbound stage, then records results in EWM.

### Interview angle
> [!question] How it is asked
> "Walk through inbound in EWM from ASN to stored stock, and name the controls."

> [!tip] Strong answer includes
> - Documents: PO, ASN, inbound delivery, GR, WT
> - Putaway strategies and capacity checks
> - Quality hold, discrepancies and returns
> - KPI example: dock-to-stock time, putaway accuracy

---
## 7. Outbound Process: Delivery, Picking, Packing, Loading and Goods Issue
> 🟠 Tier 2 · _Key points:_ ERP outbound delivery, ODR/ODO, wave, picking, packing, staging, loading, goods issue

### Definition
1. **Sales order and delivery** in ERP ([[082 SAP SD — Sales & Distribution]], [[195 SAP SD Advanced - Pricing, Output & Document Flow]]); the **outbound delivery** is transferred to EWM as an **outbound delivery request (ODR)**, followed by the **outbound delivery order (ODO)** with warehouse-specific data.
2. **Wave/release:** items are grouped and released (see sub-topic 8); **stock removal strategies** (FIFO, strict FIFO, shelf-life-based, partial quantity, large/small quantity) choose source bins; WTs are created.
3. **Pick:** WOs executed by RF; pick-by-HU or by line; consolidation at staging.
4. **Pack:** at a packing work centre; the system proposes packaging by packaging specification; HU labels and documents print.
5. **Stage and load:** HUs staged in zone, assigned to a door and **load onto a transport unit**; loading confirmation.
6. **Goods issue:** GI posting in EWM triggers ERP movement 601, COGS and the billing flow; transport booking and shipment are in [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]].

Exceptions: short pick (stock missing) → replenishment or re-allocation; deliveries on hold (credit block); damaged HU.

### Example
Order from a retail chain: 8 stores, 960 cartons in 30 delivery items. Release in two waves (cut-off 14:00 and 17:00). Wave 1 takes 18 items = 576 cartons at 12 kg = 6,912 kg, WO weight limit 400 kg gives **18 WOs** (6,912 / 400 = 17.3). At 120 cartons per picker-hour, wave 1 needs 4.8 picker-hours; with 3 pickers it finishes in about 1.6 hours.

### In the news
See news box. Bosch's humanoid picking pilot is driven by EWM task data, using exactly this WT-WO flow.

### Interview angle
> [!question] How it is asked
> "Describe outbound in EWM and where goods issue posts to the ERP."

> [!tip] Strong answer includes
> - Delivery replication, wave release, strategies, picking, packing, loading, GI
> - Documents created at each step and their ERP effect
> - Exception paths (short pick, hold)
> - Metrics: lines per hour, accuracy, on-time dispatch

---
## 8. Wave Management
> 🟠 Tier 2 · _Key points:_ Wave templates, criteria, release, cut-offs, balancing workload, wave vs waveless

### Definition
A **wave** is a group of delivery items released together for picking. A **wave template** defines selection criteria (route, carrier, priority, **cut-off time**, ship-to, product group), wave size limits (items, weight, volume) and release behaviour (manual or automatic **wave release** creating WTs). Waves are monitored in the warehouse monitor; waves can be split, merged or reprocessed.

Why waves: align picking with **carrier departures**, balance **pick workload** across the shift, group items for consolidation, and avoid overloading packing and staging. **Waveless** (continuous) processing creates WTs as deliveries arrive, suited to e-commerce with short cycle time; mixed designs are common (see [[129 E-commerce & Quick-Commerce Fulfilment]]).

Design variables: wave interval, size, cut-off buffer, priority orders (express) as dedicated mini-waves, replenishment before the wave (ensure pick bins stocked).

### Example
Carrier trucks depart at 18:00 and 21:00, with 2 hours for load and dispatch (labour and travel). Waves released at 12:00 for the 18:00 truck and 15:00 for the 21:00 truck. Wave 1 total 4.8 picker-hours (above); if only 2 pickers are available, the wave takes 2.4 hours and finishes at 14:24, still 3.6 hours before the truck.

### In the news
See news box. AI-assisted slotting and labour forecasting from SAP's 2026 EWM statement support wave design.

### Interview angle
> [!question] How it is asked
> "When would you use waves and when waveless picking?"

> [!tip] Strong answer includes
> - Wave template criteria and cut-offs
> - Waves for scheduled carriers and balanced labour; waveless for fast e-commerce
> - Interaction with replenishment and packing capacity
> - KPIs: on-time wave completion, idle time, travel distance

---
## 9. RF Framework and Mobile Execution
> 🟠 Tier 2 · _Key points:_ Radio-frequency devices, logical transactions, scan-driven confirmation, voice and wearables

### Definition
The **RF framework** presents warehouse transactions on handheld devices with small screens. Users **log on** to the resource, scan the **HU or bin label**, receive a **WO** and confirm each WT by scanning source bin, product/HU and destination bin; the system validates that scanned values match the WT (verification fields). **Logical transactions** such as putaway, picking by HU, picking by WO, **physical inventory counting**, **ad-hoc movements**, and **replenishment** are assembled from **screen flows** with navigation and function keys. Menu design is per **warehouse number and user profile**. The RF UI runs through `/SCWM/RFUI` (screen types for scanner devices), and customers extend with voice picking, wearables and vehicle-mounted terminals, or integrate robots through APIs (news box).

Quality of RF design decides productivity: fewer screens per task, error messages that say what to do, scan-first approach.

### Example
Picker logs on, receives WO 4500001234 with 12 WTs sorted by bin coordinates. At each step: scan bin 0030-03-05-02, scan SKU-77 label, key quantity 10, confirm. With 12 picks at 25 seconds each (300 seconds) plus 3 minutes of travel, a WO takes about 8 minutes, so a picker completes 7.5 WOs an hour = **90 lines per hour**.

### In the news
See news box. SAP lists APIs for robotics integration; robots and humans alike take WOs through the same task interface.

### Interview angle
> [!question] How it is asked
> "How do pickers confirm tasks in EWM and how do you prevent wrong picks?"

> [!tip] Strong answer includes
> - RF logon, WO assignment, scan verification, confirmation, exception codes
> - Screen design principles (few clicks, clear errors)
> - Training, device management, offline plan
> - Metrics: error rate, lines per hour

---
## 10. Physical Inventory and Cycle Counting
> 🟠 Tier 2 · _Key points:_ Periodic, cycle, continuous and zero-stock check; inventory documents, count, difference posting; ABC

### Definition
EWM supports these **physical inventory procedures**: **periodic** (full count of an area on a date), **cycle counting** (each product counted at a frequency based on its **cycle counting indicator**, typically ABC), **continuous** (counting during normal operations, triggered by events such as **low stock** or **putaway/picking events** and **zero stock check** when a bin empties), and **storage-bin-specific** counts. Steps: create **inventory document** for a physical inventory area or bin selection, **count** by RF or on paper (blind count, no system quantity shown), **differences** are recounted if beyond tolerance, then **posting differences** with reasons; ERP postings follow stock integrity rules.

Governance: tolerance by value, second-count rule, segregation of duties, and root-cause analysis. See [[116 Inventory Valuation, Cycle Counting & Inventory Governance]] for finance and policy.

### Example
SKUs: 500 A items (3 counts a year), 1,500 B items (2 counts), 3,000 C items (1 count): **7,500 counts a year**, or **30 counts per working day** (250 days). With a counter handling 15 counts an hour, this needs two counter-hours a day. Zero stock check at the pick bin catches phantom stock: the picker confirms empty bin and the system triggers a recount.

### In the news
See news box. Robotics pilots (Vodafone Procure & Connect, Duisburg) use inspections to detect damaged items and obstructions and feed findings back, which supports inventory accuracy.

### Interview angle
> [!question] How it is asked
> "How would you design a cycle counting programme in EWM, and how do you handle differences?"

> [!tip] Strong answer includes
> - Procedures: periodic, cycle, continuous, zero-stock check
> - ABC frequency, blind count, recount rules, tolerance, approval
> - Root-cause for repeat differences
> - Link to audit, valuation and ERP reconciliation

---
## 11. Slotting and Yard Management
> 🟠 Tier 2 · _Key points:_ Slotting rules, velocity classes, travel reduction; yard bins, check-in, door assignment

### Definition
**Slotting** determines the best storage type, section and bin for each product from **demand velocity (ABC), dimensions, weight, HU type and handling constraints**. EWM supports **slotting rules** and a slotting run that calculates result and **putaway control** proposals; **AI-assisted slotting** is among the capabilities SAP names (news box). Principles: place fast movers near dock and at ergonomic heights, keep heavy items low, co-locate items that are ordered together, and re-slot seasonally.

**Yard management:** controls trucks on site. **Check-in** at the gate creates a transportation unit (TU), the TU is moved to a **yard bin** or assigned a **door**, unloaded or loaded, and **checked out**. Gate and door scheduling reduce truck waiting (**detention**) and are linked to transportation (see [[125 Transportation Management Deep Dive]]). SAP Yard Logistics is listed in SAP's logistics suite (news box).

### Example
1,000 picks a day; average travel per pick 120 m before slotting and 80 m after moving the top 20% fastest SKUs to the golden zone. Saving 40 m × 1,000 = **40,000 m a day**; at 1 m/s walking speed that is **11.1 hours** of walking a day (about 1.4 shifts of picker time).

### In the news
See news box. SAP's EWM announcement names AI-assisted slotting and predictive labour planning.

### Interview angle
> [!question] How it is asked
> "A DC has high picker travel time. What would you change?"

> [!tip] Strong answer includes
> - ABC slotting, golden zone, pick-bin replenishment, zone picking
> - Quantify the saving (distance × picks)
> - Yard and dock scheduling for waiting time
> - Trade-offs: re-slotting effort and disruption

---
## 12. Warehouse Automation, Robotics and Material Flow System
> 🟠 Tier 2 · _Key points:_ MFS, PLC/WCS, AS/RS, AGV/AMR; EWM as task source for robots; APIs

### Definition
EWM's **Material Flow System (MFS)** is the interface layer to automation: EWM sends **telegrams** to a **PLC** or a **warehouse control system** (WCS) controlling conveyors, shuttles and AS/RS, and receives status and events; **communication points**, **conveyor segments** and **MFS resources** are modelled in EWM. **Robotics:** AGVs/AMRs and humanoid robots take **warehouse tasks** from EWM through APIs, executing picking, moving or inspection; the November 2025 SAP announcement describes pilots in which EWM provides the business context (inventory, task priorities, storage locations) and the robot returns confirmation and exceptions (news box). Business justification depends on labour cost, space, throughput and accuracy.

### Example
Automated shuttle system (6 aisles, 20,000 pallet positions) at a pharma DC. Throughput goal 120 pallets an hour in and out. Manual operation needs 14 forklifts and 20 operators across shifts; automation needs 4 operators for exceptions. If annual saving is ₹2.4 crore on labour and the investment is ₹18 crore, simple payback = 18 / 2.4 = **7.5 years**, so the case depends also on space saving, accuracy and growth, see [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]].

### In the news
See news box. SAP's physical-AI announcement lists 13 robotics companies and 10+ enablement partners; the pilot benefits reported are potential, not independent measurements.

### Interview angle
> [!question] How it is asked
> "How would you integrate automated storage or robots with EWM and justify the investment?"

> [!tip] Strong answer includes
> - MFS/PLC/WCS integration pattern, fallback to manual
> - Task-source role of EWM, APIs and exception handling
> - Business case with payback, sensitivity and non-financial benefits
> - Pilot first, then scale

---
## 13. ⭐ Advanced: End-to-End Inbound-to-Outbound Walkthrough and KPIs
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Walkthrough for a Pune-based FMCG distribution centre:
1. **PO** 4500012345 for 6,000 cartons; **ASN** → inbound delivery 180001234 → replicated to EWM.
2. **Yard**: truck check-in, door 3. **Unload** and **GR** posted at 10:20 (ERP 101 movement; stock in unrestricted EWM stock).
3. **Putaway**: 100 HU, WTs created with putaway strategy "empty bin", confirmed by RF within 4 hours.
4. **Sales orders** from 8 stores, deliveries replicated as ODR → ODO; **wave** released at 12:00; WTs and WOs are created, pickers confirm by RF.
5. **Pack, stage, load**; GI posted at 17:30, ERP 601; invoice by SD; shipment by TM.
6. **Physical inventory**: cycle count for A items weekly.

KPI set:
$$\text{Dock-to-stock} = t_{\text{putaway confirmed}} - t_{\text{GR}} \qquad \text{Pick accuracy} = 1 - \frac{\text{lines with errors}}{\text{lines picked}}$$
$$\text{Space utilisation} = \frac{\text{bins occupied}}{\text{bins available}} \qquad \text{Inventory record accuracy} = \frac{\text{bins counted correctly}}{\text{bins counted}}$$

### Example
Day results: 960 cartons shipped on 30 lines; 2 lines had picking errors, so line accuracy = 1 − 2/30 = **93.3%** (low versus a typical target above 99%); 100 pallets stored, 83.3% utilisation; dock-to-stock average 3.6 hours; 120 bins counted, 117 correct: record accuracy **97.5%**. Interpretation: process works but picking accuracy needs RF verification and pack-station checks.

### In the news
See news box for robotics, AI slotting and labour planning in EWM.

### Interview angle
> [!question] How it is asked
> "Walk us through an end-to-end warehouse flow in EWM and say what you would measure."

> [!tip] Strong answer includes
> - Clear sequence of documents and events with ERP touchpoints
> - KPI formulas with example numbers
> - Identification of improvement levers (RF, slotting, waves)
> - Link to the end-to-end flows in [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]

---
## 14. ⭐ Advanced: WM-to-EWM Migration and Cut-over Considerations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Migration from classic WM (transfer orders, storage types, quants) to EWM is a **redesign**, not a conversion: concepts differ (activity areas, storage control, WT/WO, HUs). Typical steps: (1) fit-gap and design workshops, (2) decide embedded versus decentralised and licence scope, (3) map organisational structure and master data (bin types, packaging specification), (4) design process types, storage control and WOCR, (5) build RF screens, labels and printers, (6) integration tests with ERP, TM, QM and automation, (7) **cut-over**: freeze, count, load stock as quants per bin and HU with reconciliation to ERP, (8) hypercare with floor support. Risks: performance at peak, label and scanner readiness, and under-trained users. Migration wave planning for S/4HANA is in [[200 SAP S-4HANA Migration, Data Migration & Testing]].

### Example
Cut-over weekend: stop movements Friday 20:00; wall-to-wall count completed 02:00; load 1,20,000 quants, reconcile ERP stock to EWM by product and batch (tolerance zero for value, ±0 for quantity); go-live Sunday 18:00. A mismatch of 12 quants (0.01%) is resolved by recount before release. Fall-back: manual transfer order paper process kept for 2 days.

### In the news
See news box. SAP's 12th Leader placement and its Logistics Management launch show that SAP expects customers to choose between EWM and lighter options during migration.

### Interview angle
> [!question] How it is asked
> "What are the biggest risks when moving a busy DC from WM to EWM?"

> [!tip] Strong answer includes
> - Redesign, not lift-and-shift; process and organisation changes
> - Cut-over reconciliation, performance testing and fall-back plan
> - Hypercare with floor-walkers and daily KPIs
> - Phased go-live by warehouse or process
