---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP PM Deep Dive - Maintenance Orders, Plans & Strategies"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP PM Deep Dive - Maintenance Orders, Plans & Strategies

⬅ [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]] · [[_Index - SAP ERP|SAP ERP]]

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. PM Process and the Technical-Object Model]]
2. [[#2. Functional Locations and Equipment Masters]]
3. [[#3. Maintenance BOMs and Task Lists]]
4. [[#4. Maintenance Notifications]]
5. [[#5. Maintenance Order Types and Order Structure]]
6. [[#6. Order Lifecycle: Create, Plan, Release, Confirm, TECO, Settle]]
7. [[#7. Spare Parts: Reservations, Procurement, Stocking and Cost]]
8. [[#8. Preventive Maintenance Plans: Single Cycle, Strategy, Performance-Based]]
9. [[#9. Measuring Points, Counters and Condition-Based Triggers]]
10. [[#10. Maintenance KPIs from SAP: MTBF, MTTR, PM Compliance, Backlog]]
11. [[#11. Costs, Settlement and Integration with MM, FI/CO, QM and PS]]
12. [[#12. S/4HANA Asset Management, Fiori and Intelligent Asset Management]]
13. [[#13. Worked Breakdown Flow: From Alarm to Settlement]]
14. [[#14. ⭐ Advanced: Maintenance Strategy Optimisation, RCM and Shutdown Management]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Asset management moves from work orders to condition-based, AI-assisted maintenance
> **Equinor targets condition-based maintenance with SAP Asset Performance Management (SAP News Center, 26 Aug 2024).** After running a monitoring centre for 8–9 years on manual processes and home-grown dashboards, Equinor started rolling out SAP's asset performance management software, with the goal of **proactive maintenance for 40% of its equipment** and lower maintenance cost and downtime. The article stresses integration with existing SAP systems (no duplicate data entry), real-time sensor ingestion, and automatic task pre-assignment from asset strategies and failure modes. ([SAP News Center](https://news.sap.com/2024/08/equinor-condition-based-maintenance-sap-asset-performance-management/))
>
> **Petrobras at the Buzios field (SAP News Center, 1 Mar 2024).** Proof of concept in **2020**; by **end-2023** SAP Intelligent Asset Management covered **10 critical systems** (gas compression, production gathering, fire and gas detection, firefighting, power generation, offloading, water/oil treatment, injection pumping) at Buzios, which represents nearly **16%** of Petrobras' oil and gas production. Machine-learning anomaly detection and failure prediction were activated; Petrobras cites higher machine availability and fewer failures (no figures given). ([SAP News Center](https://news.sap.com/2024/03/petrobras-sap-intelligent-asset-management-maintenance/))
>
> **SAP's product direction (SAP News Center, 13 Dec 2024).** SAP positions Intelligent Asset Management around a unified asset data thread, closed loops between IoT sensors and manual inspections, mobile work management (SAP Service and Asset Manager, with offline use), and IoT partnerships (Cumulocity); SAP cites an IDC 2024 SaaS EAM customer-satisfaction award. ([SAP News Center](https://news.sap.com/2024/12/sap-intelligent-asset-management-future-asset-excellence/))
>
> **ECC deadline (SAP, 4 Feb 2025).** On-premise ECC mainstream maintenance ends 2027 and extended maintenance 2030; the paid transition option (buy from 2028, use 2031–2033) is a cloud subscription, not a maintenance prolongation. ([SAP News Center](https://news.sap.com/2025/02/sap-erp-private-edition-transition-option-navigate-complex-rise-with-sap-transformations/))
>
> Sub-topics that say **"See news box"** reuse these items. Basics in [[084 SAP QM & PM]]; maintenance theory in [[022 Maintenance Management (TPM-RCM)]] and [[155 Reliability Engineering & Maintenance Optimisation]].

---
## 1. PM Process and the Technical-Object Model
> 🟠 Tier 2 · _Key points:_ Notify, plan, execute, complete, settle, analyse; location, equipment, assembly

### Definition
**SAP PM (Plant Maintenance)**, also called Enterprise Asset Management, manages technical assets and the work done on them. The closed loop:
1. **Notify:** a problem or request is recorded (notification).
2. **Plan:** work is planned in a maintenance order (operations, components, costs); preventive tasks come from maintenance plans.
3. **Schedule and release:** capacity, materials and permits are checked; the order is released.
4. **Execute and confirm:** work is done, time and parts are confirmed.
5. **Complete:** technical completion (TECO) and history entry.
6. **Settle and analyse:** costs settle to the receiver; KPIs and failure analysis feed the next plan.

**Technical objects:** **functional location** (place or function in a plant structure), **equipment** (the physical object), **assembly** and **material** (spares in the BOM), plus **linear assets** for pipelines and roads. Everything else (notifications, orders, plans) hangs on these objects; the quality of that master data decides whether reports mean anything.

### Example
A cement plant structure: plant 1100 → kiln line 1 → preheater → ID fan. Functional location `CMT-K1-PH-IDFAN`; equipment `E-10045` is "ID fan motor, 1,500 kW" installed there; spare parts in the equipment BOM; a monthly vibration check plan; and a breakdown history linked to equipment. If the motor is swapped, the location history stays and the motor's own history moves with it.

### In the news
See news box. Both Equinor and Petrobras describe attaching sensor data and strategy to the same asset hierarchy; asset data quality is therefore the base layer of any AI programme.

### Interview angle
> [!question] How it is asked
> "Describe the end-to-end process of maintenance in SAP PM."

> [!tip] Strong answer includes
> - The loop from notification to settlement, with the document at each step
> - Role of functional locations and equipment as anchors
> - Preventive vs corrective sources of orders
> - Reports and KPIs that come back from the loop

---
## 2. Functional Locations and Equipment Masters
> 🟠 Tier 2 · _Key points:_ Structure indicator, installation, categories, classification, warranty

### Definition
- **Functional location** (`IL01` create, `IL02` change, `IL03` display; structure `IH01`): a hierarchical key built from a **structure indicator** and **edit mask** (for example `PLANT-LINE-STATION`), with a category, **superior functional location**, cost centre, work centre, **ABC indicator** (criticality), authorisation group, classification and **partners** (responsible persons).
- **Equipment** (`IE01` create, `IE02`, `IE03`; list `IH08`): an individual object with a number, **equipment category** (machine, vehicle, test equipment, production resource/tool), manufacturer, model, serial number, acquisition date and value, **warranty** (vendor and customer), **installation location** (functional location) and **superior equipment** for sub-equipment. **Installation and dismantling** (`IE4N`) record movement; **equipment BOM** (`IB01`) lists spares.
- **Classification and characteristics** (class type 002 for equipment, 003 for functional locations) store technical data (power, capacity, pressure) and support search.
- **Fleet and linear objects** use separate categories and master data.
- Tables: `IFLOT` (functional locations), `EQUI` (equipment), `ILOA` (location and account assignment data), `EQKT`/`IFLOTX` texts.
- **Data quality rule:** every equipment installed at a location, every notification against equipment or location, every task list at a structure level.

### Example
Functional location `PUN-PKG-L2-FILL` (Pune, packaging, line 2, filler) has ABC indicator A (critical). Equipment `E-20318` "Filler pump P-204" is installed with serial 7712 and warranty ending 31 Mar 2027; when the pump fails under warranty the notification flags the vendor. Replacing the pump with `E-20999` dismantles the old one (history stays with E-20318) and installs the new one (a new history), while the location history shows both.

### In the news
See news box. Petrobras started with a limited pilot and extended to all critical systems; the equipment master is what makes such scaling possible.

### Interview angle
> [!question] How it is asked
> "What is the difference between a functional location and equipment, and why does it matter for MTBF?"

> [!tip] Strong answer includes
> - Location = place/function; equipment = physical object that can move
> - Structure indicator, hierarchy, ABC indicator
> - Installation and dismantling and how history behaves
> - Reporting by location vs by equipment for reliability analysis

---
## 3. Maintenance BOMs and Task Lists
> 🟠 Tier 2 · _Key points:_ Equipment BOM, material BOM, general task lists, equipment task lists, reuse

### Definition
- **Maintenance BOM** (`IB01` equipment BOM; also functional location BOM and material BOM): a structured list of the spare parts that make up an asset. Items have categories: **L (stock item)**, **N (non-stock item)**, **T (text)**, **D (document)**. Item category L supports reservation and issue; N drives purchase requisition; T carries instructions.
- **Task list** (`IA05` general task list, `IA01` equipment task list, `IA11` functional location task list): a reusable list of **operations** (work centre, standard text, duration), **components** (from the BOM or entered), **tools** (production resources/tools such as test equipment), and **maintenance packages** for strategy plans. **Reference** the task list from the maintenance plan or order so that planners do not retype work every time.
- **Assignment** of a task list to equipment, location, or material.
- **Permits and safety:** work clearance management (WCM) for hazardous work, linked to orders.

### Example
General task list "Lubricate gearbox, 6-monthly": 3 operations (drain 0.5 h, flush 0.5 h, refill and test 0.5 h), 1 component (oil 20 l, stock item), 2 technicians. When used for 40 gearboxes it is created once; the plan quantity and standard cost are then consistent across all 40 orders.

### In the news
See news box. Equinor's "task pre-assignment from asset strategies" is the same idea at scale: tasks follow from the asset strategy and failure mode rather than being retyped.

### Interview angle
> [!question] How it is asked
> "How do you ensure that spare parts and tasks are available when a maintenance order is created?"

> [!tip] Strong answer includes
> - Equipment BOMs with stock and non-stock items; reservation vs PR
> - Task list reuse, packages, production resources and tools
> - Standard text, durations, and cost implications
> - Governance: who maintains BOMs and task lists after repairs

---
## 4. Maintenance Notifications
> 🟠 Tier 2 · _Key points:_ M1, M2, M3, catalogs, breakdown indicator, priority, conversion to order

### Definition
A **maintenance notification** (`IW21` create, `IW22` change, `IW23` display; lists `IW28`/`IW29`; table `QMEL`) records a problem, request or activity before work is planned. Standard types: **M1 maintenance request** (a request from operations), **M2 malfunction report** (failure, with breakdown indicator and malfunction start and end), **M3 activity report** (work done without a request). Key fields:
- **Reference object:** equipment and/or functional location, assembly.
- **Breakdown indicator** and **malfunction start/end** date and time: the basis for downtime and MTTR.
- **Priority** (for example 1 very high, 2 high, 3 medium, 4 low) with **required start and end**.
- **Catalog coding:** object part, **damage code**, **cause code** (and activity). Standard catalog profiles from the equipment category propose valid codes.
- **Reporter, planner group, work centre** and **long text**.
- **Notification status** (outstanding, in process, order assigned, postponed, completed) and the **order link**: a notification is converted to an order (button "Create order") so work and costs are tracked.
- **Task and activity** lines inside notifications can plan simple work without an order.

### Example
At 14:10 an operator raises M2 for pump P-204: damage code "Leakage", object part "Mechanical seal", malfunction start 14:10, breakdown indicator ticked, priority 2. The planner sets cause code "Wear" on completion and records malfunction end at 20:10. Downtime = 6 h, which feeds MTTR and availability. Without the end time the downtime cannot be calculated.

### In the news
See news box. Failure-mode and damage codes are the structured data that SAP's predictive features (anomaly detection, failure prediction) need to learn from.

### Interview angle
> [!question] How it is asked
> "What fields on the notification are critical for later reliability analysis?"

> [!tip] Strong answer includes
> - Reference object, breakdown flag, malfunction start/end
> - Damage and cause codes, priority
> - Discipline: complete codes at closure
> - Notification vs order separation and why

---
## 5. Maintenance Order Types and Order Structure
> 🟠 Tier 2 · _Key points:_ PM01/PM02/PM03, operations, components, control keys, planning data

### Definition
Order types are configured per company; the standard examples are **PM01** (maintenance order, typically corrective or general), **PM02** (planned/preventive order, generated from a maintenance plan) and **PM03** (refurbishment of spare parts). **Maintenance activity types** classify the work (inspection, preventive, repair, calibration) and **priorities** control scheduling. An order (`IW31` create, `IW32` change, `IW33` display; list `IW38`/`IW39`; header table `AFIH`, order master `AUFK`) contains:
- **Header:** order type, description, reference object, planner group, main work centre, priority, basic dates, **maintenance activity type**, **settlement rule**.
- **Operations:** work centre, control key (**PM01 internal processing**, **PM02 external processing**), work duration, number of people, activity type for costing, optional **sub-operations**.
- **Components:** spare parts as stock (L), non-stock (N, creates a purchase requisition), text; reservations are created when the order is saved or released.
- **Costs:** **planned costs** from operations (rate times hours) and components; **actual costs** from confirmations and goods issues; external services via PO or service entry sheet.
- **Objects:** the technical objects the order serves, and **permits** where needed.

### Example
Order type PM01 for the filler pump: operation 0010 internal (2 people, 6 h planned, activity type "labour" at ₹450 per hour), operation 0020 external welding service (control key PM02, ₹6,500 outsourced), components: 2 bearings (stock item, ₹3,700 each). Planned cost: labour 2 × 6 × 450 = 5,400, material 7,400, external 6,500: **₹19,300**.

### In the news
See news box. As condition-based triggers (Equinor, Petrobras) create more orders automatically, standard order structures and task lists are what stop planning workloads from exploding.

### Interview angle
> [!question] How it is asked
> "What are the elements of a maintenance order and how are costs captured on it?"

> [!tip] Strong answer includes
> - Operations, components, costs and settlement rule
> - Internal vs external processing and how each posts
> - Planned vs actual cost; how an order type's settings steer behaviour
> - Notification as input and history as output

---
## 6. Order Lifecycle: Create, Plan, Release, Confirm, TECO, Settle
> 🟠 Tier 2 · _Key points:_ Statuses, goods issue, confirmation, technical completion, business completion

### Definition
| Step | Action (T-code) | System effect |
|---|---|---|
| 1 Create | `IW31` or from notification | Status CRTD (created); planned costs calculated |
| 2 Plan | Operations, components, permits, capacity | Reservations for stock components; PRs for non-stock |
| 3 Schedule | Dates and capacity check; scheduling board | Basic and scheduled dates |
| 4 Release | `IW32` change status to REL | Printing, goods issue, confirmation allowed; availability check per config |
| 5 Issue parts | `MIGO` 261 against reservation | Material cost posts to the order (Dr order/cost, Cr Inventory) |
| 6 Execute and confirm | `IW41` (single), `IW44` (collective) | Actual hours; status PCNF then CNF with the final confirmation flag; labour cost via activity allocation |
| 7 Document | History entries, measurement readings, damage/cause | Equipment history updated |
| 8 TECO | `IW32` technical completion | Work done; no more confirmations or issues; reservations released; history locked in |
| 9 Settle | `KO88` (single), `KO8G` (collective) | Actual costs credited to the order, debited to receiver (cost centre, asset, other) |
| 10 Business complete | Close order | Status CLSD; archiving possible |

Notes: cost on the order is a **collector**, not a final expense, until settled. **Variance** between planned and actual is analysed on the order before it is settled. Orders can be reopened only before closure or by reversing statuses where permitted.

### Example
Order cost: planned ₹19,300. Actual: labour 2 × 6.5 h × ₹450 = ₹5,850; bearings issued 2 × ₹3,700 = ₹7,400; external welding ₹6,500 (invoice posts to the order through the PO). Total actual ₹19,750; variance +₹450 (2.3% over). After TECO, `KO88` settles ₹19,750 to cost centre `CC-PKG-L2` as maintenance expense.

### In the news
See news box. Closed-loop approaches (Equinor, Petrobras) depend on orders being confirmed and closed with correct readings; open or untidy orders break the data loop.

### Interview angle
> [!question] How it is asked
> "Walk me through the life cycle of a maintenance order and what accounting happens when."

> [!tip] Strong answer includes
> - Statuses and the action that triggers each
> - Material issue, labour confirmation, external service postings
> - TECO vs closing; settlement to receiver
> - Discipline items: final confirmation, accurate hours, history coding

---
## 7. Spare Parts: Reservations, Procurement, Stocking and Cost
> 🟠 Tier 2 · _Key points:_ Stock vs non-stock, reservations, criticality, min-max, ABC/VED, cost to order

### Definition
- **Stock items (L):** reserved on save/release; `MIGO` goods issue 261 consumes the reservation; MRP can replenish them (reorder point or MRP).
- **Non-stock items (N):** a purchase requisition is created automatically; on goods receipt the item posts directly to the order (account assignment "order"), no inventory.
- **Services:** external services via service PO and service entry sheet ([[192 SAP Sourcing & Procurement Deep Dive]]).
- **Strategic spares:** insurance spares for critical equipment (slow-moving, high cost). Policies use **criticality** and **ABC/VED** analysis. **VED** (vital, essential, desirable) is widely used in Indian public-sector and process plants: stock vital items regardless of consumption rate, stock essential items on consumption basis, buy desirable items on demand. See [[003 Inventory Management]] and [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]].
- **Quantity and cost:** reservations show planned demand early; `MB25`/`MB21` handle reservations; `MB51` shows consumption by movement 261; `MB52` stock; MRP uses reservations in planning.
- **Repairable spares:** refurbishment order (PM03) to repair and return to stock, with the cost of repair settled to stock.

### Example
A critical gearbox (cost ₹3,20,000, lead time 16 weeks, expected failure once in 6 years) is "vital": policy is to hold one spare. Cost of holding at 20% a year: ₹64,000 per year. A failure without a spare costs 16 weeks of downtime; if downtime costs ₹18,000 per hour, even 3 days (72 h) costs ₹12,96,000, far above the carrying cost. A low-cost gasket (₹150, used 40 a year) is stock-managed with a reorder point.

### In the news
See news box. Predictive maintenance reduces emergency purchases and improves planning of parts, because failure forecasts give lead time to procure.

### Interview angle
> [!question] How it is asked
> "How should critical spares be stocked and how does SAP support it?"

> [!tip] Strong answer includes
> - Stock vs non-stock logic with reservation/PR
> - Criticality analysis (ABC/VED), min/max for consumables, insurance spares for critical items
> - Cost comparison of holding vs downtime
> - Repairable spares and refurbishment orders

---
## 8. Preventive Maintenance Plans: Single Cycle, Strategy, Performance-Based
> 🟠 Tier 2 · _Key points:_ Plan types, maintenance items, scheduling parameters, call horizon, shift factor, packages

### Definition
A **maintenance plan** schedules recurring work for one or more **maintenance items** (technical object plus task list). Types:
- **Single cycle plan** (`IP41`): one cycle, for example every 90 days, or every 500 operating hours.
- **Strategy plan** (`IP42`): a **maintenance strategy** (`IP11`) defines **packages** (1M, 3M, 6M, 12M) in a **hierarchy** so that on common dates only the highest package executes and it includes lower-level tasks.
- **Multiple counter plan** (`IP43`): several counters; the plan is due when any counter's cycle is reached.
- **Basis types:** **time-based**, **performance-based** (counter readings such as running hours, km, cycles) and **condition-based** (measurement document with a valuation code).

Plan creation (`IP01`) and scheduling (`IP10` start; `IP30` deadline monitoring; scheduling overview `IP19`). A **call object** is generated at the call date: a **maintenance order**, a **notification** or a service entry sheet. Scheduling parameters:
- **Call horizon (%):** how early the call object is created (percentage of the cycle).
- **Scheduling period:** how far ahead the plan is scheduled.
- **Completion requirement:** whether the next date depends on the completion of the previous call.
- **Shift factor (late/early completion):** how much of a late or early completion shifts the next date (0% fixed dates, 100% full shift to the completion date); applies only outside the **tolerance**.
- **Tolerance (+/−)** around the planned date; **factory calendar**; **start of cycle**.

### Example
**Time-based single cycle:** 90-day cycle starting 1 Jan 2026. Planned date 1 Apr 2026. With a 80% call horizon the order is created 72 days after start, on **14 Mar 2026** (18 days before due). Late tolerance 10% (9 days). Case 1: work completed 6 Apr (5 days late, inside tolerance): no shift, next planned date 30 Jun 2026 (1 Apr + 90 days). Case 2: completed 16 Apr (15 days late, outside tolerance): shift factor 100% re-bases to the completion date, next 15 Jul 2026; with a 50% shift factor the next date moves by about 7.5 days to about 7 Jul 2026.

**Performance-based:** pump cycle 500 running hours, usage 16 h/day: due every 31.25 days; with a 90% call horizon the order is created after 450 hours, about 28 days.

**Strategy plan with packages:** 1M, 3M, 6M and 12M over 12 months generate 12 calls: 1M × 8 (months 1, 2, 4, 5, 7, 8, 10, 11), 3M × 2 (months 3, 9), 6M × 1 (month 6), 12M × 1 (month 12).

### In the news
See news box. Condition-based programmes (Equinor, Petrobras) aim to replace fixed-interval plans on critical assets with data-triggered tasks, while strategy and time-based plans continue for low-risk assets.

### Interview angle
> [!question] How it is asked
> "Explain call horizon and shift factor with an example, and when would you choose a strategy plan?"

> [!tip] Strong answer includes
> - Plan types and when each is used (time, performance, condition; single vs strategy)
> - Call horizon, tolerance and shift factor explained with dates
> - Package hierarchy to avoid duplicate tasks
> - Review of intervals using failure data, not habit

---
## 9. Measuring Points, Counters and Condition-Based Triggers
> 🟠 Tier 2 · _Key points:_ Measuring points, counters, documents, valuation codes, automatic notifications

### Definition
- **Measuring point** (`IK01` create): a place on equipment or location where a value is measured (temperature, vibration, pressure) with a **characteristic** (unit, decimals), **measurement range** and **valuation codes** (for example normal, warning, alarm).
- **Counter:** a measuring point of counter type that accumulates (running hours, km, cycles) with **counter overflow** and **annual estimate** used for scheduling.
- **Measurement document** (`IK11` create, `IK12` change, `IK13` display; table `IMRG`) records a reading. **Collective entry** supports rounds.
- **Triggers:** a reading outside limits (valuation code) can create a **notification** or **order** automatically. A **measurement-based maintenance plan** uses counter readings to schedule performance-based calls.
- **Interfaces:** sensor and SCADA data can post measurement documents through IoT platforms; condition-based plans react when thresholds are crossed.
- **Calibration:** test equipment with measuring points and plans produces calibration inspections ([[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]]).

### Example
Bearing temperature measuring point on motor M-11: limits 40–80 °C, alarm at 85 °C. Reading on 3 Jun = 88 °C: the valuation code "alarm" creates an M2 notification automatically with priority 2; planner converts it into an order for 4 June, avoiding a breakdown. Counter for running hours: reading 4,980 h versus due 5,000 h means a lubrication call is due within a day at 16 h/day.

### In the news
See news box. Equinor's rollout is an example of ingesting real-time sensor data into the asset system and acting on it through predefined asset strategies.

### Interview angle
> [!question] How it is asked
> "How can SAP PM trigger maintenance from machine condition rather than from the calendar?"

> [!tip] Strong answer includes
> - Measuring points, documents and valuation codes
> - Counters for performance-based plans
> - IoT/APM integration for scale
> - Governance: right thresholds, avoid alarm fatigue, review false positives

---
## 10. Maintenance KPIs from SAP: MTBF, MTTR, PM Compliance, Backlog
> 🟠 Tier 2 · _Key points:_ Data sources, formulas, planned vs reactive ratio, backlog in weeks

### Definition
Core formulas (see also [[155 Reliability Engineering & Maintenance Optimisation]] and [[018 Capacity Management & OEE]]):
$$MTBF = \frac{\text{operating time}}{\text{number of failures}}, \quad MTTR = \frac{\text{total repair time}}{\text{number of repairs}}, \quad A = \frac{MTBF}{MTBF + MTTR}$$
$$\text{PM compliance} = \frac{\text{PM orders completed within window}}{\text{PM orders scheduled}}, \quad \text{Backlog (weeks)} = \frac{\text{open planned work hours}}{\text{crew hours per week}}$$
Other KPIs: **planned vs reactive ratio** (PM:CM), **schedule compliance**, **wrench time** (hands-on-tool time), **maintenance cost per replacement asset value**, **spare-part service level**, and **repeat failures**.

**SAP sources:** M2 notifications (breakdown indicator, malfunction start/end) via `IW28`/`IW29`; orders via `IW38`/`IW39` with planned and actual hours and costs; confirmations; measurement documents; the **Plant Maintenance Information System** (a logistics information system) and BI. Data quality is the limit: if breakdown times, damage and cause codes or final confirmations are missing, the KPI is wrong.

### Example
Equipment ran 8,000 h in the year with 7 failures and 42 h total repair time: MTBF = 8,000/7 = **1,142.9 h**, MTTR = 42/7 = **6.0 h**, availability = 1,142.9/(1,142.9 + 6.0) = **99.48%**. PM compliance: 132 of 150 scheduled PM orders completed in the window = **88%**. Backlog: 1,800 open planned hours; six technicians at 40 h/week and 75% wrench time = 180 productive hours a week, so backlog = **10 weeks** (a common target is 2–4 weeks; the right level depends on the plant).

### In the news
See news box. Petrobras cites availability and failure reductions, and Equinor a 40% proactive-maintenance goal; both are KPIs that rely on the data fields above.

### Interview angle
> [!question] How it is asked
> "How would you measure and improve maintenance performance in a plant using SAP data?"

> [!tip] Strong answer includes
> - KPI definitions and where each number comes from in SAP
> - Data-quality checks before analysis (missing end times, final confirmation)
> - Pareto by equipment and cause to target effort
> - Levers: PM plan optimisation, spares, training, design-out of repeat failures

---
## 11. Costs, Settlement and Integration with MM, FI/CO, QM and PS
> 🟠 Tier 2 · _Key points:_ Cost flow, settlement rules, budgets, links to modules

### Definition
**Cost flow:** parts issued (MM, 261) debit the order and credit inventory; labour is allocated from the work centre's cost centre and activity type (CO); external services post via PO/invoice to the order; overheads can be applied by costing sheet. **Settlement** (`KO88`/`KO8G`) transfers actual cost to the **receiver** in the settlement rule: **cost centre** (routine maintenance), **asset under construction or fixed asset** (capitalised improvements, investment orders), **internal order**, **WBS element**. Settlement profile and allocation structure decide which cost elements go where.

**Integration map:**
| Module | Integration |
|---|---|
| MM | Reservations, PRs for non-stock, service procurement, stock; see [[080 SAP MM — Materials Management]] |
| FI/CO | Cost centre/activity types, settlement, asset accounting, budget availability; see [[190 SAP FI-CO Essentials for Operations Professionals]] |
| QM | Calibration, inspection of test equipment, quality notifications ([[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]]) |
| PS | Shutdown and turnaround projects, capital projects ([[170 Programme, Portfolio & PMO Management]]) |
| HR | Qualifications and time confirmation |
| PP | Production resources and tools, availability of machines for planning |

**Maintenance vs capital rule (accounting judgement):** maintenance that restores the original condition is expense; improvements that increase capacity or life are capitalised, via investment order to asset. Confirm local accounting policy and Ind AS treatment.

### Example
Planned ₹19,300; actual ₹19,750 settled to cost centre as expense. A different order, "pump upgrade to higher capacity", costs ₹4,80,000 and is settled to asset under construction `AUC-PKG-L2` then capitalised on completion, with depreciation from the capitalisation date. Cost centre maintenance budget for the year ₹60 lakh; at month 6 actual ₹34 lakh is 56.7% of budget at 50% of the year (over-run signal).

### In the news
See news box. Closed-loop asset management is as much a finance story as a technical one: the savings Equinor and Petrobras seek show up as lower unplanned cost and higher availability.

### Interview angle
> [!question] How it is asked
> "Where do maintenance costs end up in SAP, and how do you separate repair expense from capital improvements?"

> [!tip] Strong answer includes
> - Order as cost collector; settlement rule and receivers
> - Material, labour and service flows
> - Capital vs revenue distinction via investment orders
> - Cost-centre budget monitoring and variance review

---
## 12. S/4HANA Asset Management, Fiori and Intelligent Asset Management
> 🟠 Tier 2 · _Key points:_ Fiori apps, mobile execution, APM, AIN, IoT, S/4HANA differences

### Definition
In **S/4HANA**, PM continues as **Asset Management / Enterprise Asset Management** with the same objects and orders but modern UIs, embedded analytics, and cloud extensions. Typical elements:
- **Fiori apps** for notification creation, order planning and scheduling, and analytical lists (app names and availability vary by release; use SAP's Fiori apps reference library for the current list).
- **Mobile and field execution:** **SAP Service and Asset Manager** offers real-time access to work orders and asset data on phones and tablets, including offline use in remote locations (per SAP's Dec 2024 article).
- **SAP Intelligent Asset Management** brings together **SAP Asset Performance Management** (condition monitoring, failure modes, strategies, predictive models), the **Asset Intelligence Network** (manufacturer-to-operator asset data sharing) and related services, with IoT connectivity (for example Cumulocity).
- **Business Partner** replaces some legacy partner handling, **Product Master** concepts apply to spares, and **MATDOC** changes how material issues are stored; see [[200 SAP S-4HANA Migration, Data Migration & Testing]].
- **Extensibility:** custom fields and logic via key-user tools; avoid modifying standard PM transactions to stay clean-core.

### Example
A technician on a Nashik line uses a tablet app offline in a basement to view the assigned order, scan the equipment QR code, record readings and time, and complete the order; the data syncs when the device reconnects, and the planner sees confirmed hours and a closing note the same day instead of next week from paper.

### In the news
See news box. SAP's Dec 2024 positioning (mobile, AI, closed loop with IoT) and customer references (Equinor, Petrobras) show where S/4HANA-era asset management is heading.

### Interview angle
> [!question] How it is asked
> "How does SAP S/4HANA change plant maintenance compared with ECC PM?"

> [!tip] Strong answer includes
> - Same core objects; new UI, mobile, analytics and APM integration
> - Predictive/condition-based layer attached to the same master data
> - Technical changes (BP, MATDOC, MRP Live) that affect migration
> - Clean-core extensions and phased adoption

---
## 13. Worked Breakdown Flow: From Alarm to Settlement
> 🟠 Tier 2 · _Key points:_ M2, order, parts, confirmation, TECO, settlement, analysis

### Definition
Step-by-step with T-codes and numbers (illustrative):
1. **Failure:** the filler pump P-204 stops at 14:10; operator raises an **M2 notification** (`IW21`) with breakdown indicator, damage "Leakage".
2. **Planner:** converts it into **order PM01** (`IW31`): operation 0010 internal (2 people, 6 h), 0020 external welding (₹6,500), components 2 bearings (₹3,700 each). Planned cost ₹19,300.
3. **Release** (`IW32`); reservations are visible to stores; permit issued.
4. **Issue parts** (`MIGO` 261): ₹7,400 posted to the order.
5. **Execute and confirm** (`IW41`): 2 technicians, 6.5 h each, final confirmation. Labour = 2 × 6.5 × 450 = ₹5,850.
6. **External service** invoice ₹6,500 posts to the order.
7. **Close notification:** malfunction end 20:10 (downtime 6 h), cause "Bearing wear".
8. **TECO** and settle (`KO88`): actual ₹19,750 to cost centre.
9. **Analyse:** failure history shows the third bearing failure in 12 months; planner proposes a vibration measuring point and a quarterly bearing plan.

**Economics:** downtime cost 6 h × ₹18,000 = **₹1,08,000** is not in the order but in lost output; failure cost = ₹19,750 + ₹1,08,000 = **₹1,27,750**. A quarterly PM plan costing ₹2,200 per visit = ₹8,800/year pays for itself if it prevents at least 8,800/1,27,750 = **0.069 failures a year** (about one failure every 14.5 years); with three failures last year the case is strong.

### Example
Reading the order together with its notification: planned ₹19,300 vs actual ₹19,750: +₹450; time estimated 12 labour-hours vs actual 13 (8.3% over). Total cycle time notification to completion: 6 h (14:10 to 20:10). The priority-2 target was 8 h, so SLA was met.

### In the news
See news box. Cases like Petrobras at Buzios show scaled deployment: begin with a few critical systems, prove failure reduction, then extend.

### Interview angle
> [!question] How it is asked
> "A critical pump failed three times in a year. What would you do in SAP to stop it?"

> [!tip] Strong answer includes
> - Pull history by equipment (notifications, damage/cause, orders, costs)
> - Pareto of causes and cost of failure including downtime
> - New plan or measuring point with threshold, spare strategy
> - Verify with MTBF/availability after change

---
## 14. ⭐ Advanced: Maintenance Strategy Optimisation, RCM and Shutdown Management
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Criticality and RCM:** rank assets by consequence of failure (safety, production, cost). RCM selects per failure mode: run-to-failure, time-based, condition-based or redesign ([[022 Maintenance Management (TPM-RCM)]]). SAP holds ABC indicators on objects and strategies in plans; SAP APM adds failure-mode libraries.
- **Optimal PM interval:** with failure cost $C_f$, planned replacement cost $C_p$ and an increasing failure rate, an age-replacement policy minimises cost per unit time; choose the interval by minimising $\frac{C_p \cdot R(T) + C_f \cdot (1-R(T))}{\int_0^T R(t)\,dt}$ (see [[155 Reliability Engineering & Maintenance Optimisation]]).
- **Shutdown/turnaround management:** large planned stoppages for refineries, steel, cement, power. Work is bundled as a **project** (PS network or work breakdown structure) with hundreds of orders, scheduling tools, permits (WCM), contractor management, spare pre-staging, and a critical-path plan ([[039 Scheduling Tools (CPM-PERT-Gantt)]]). KPIs: schedule adherence, cost vs budget, scope growth, safety incidents.
- **Condition-based roadmap:** start with criticality, instrument only the assets that merit it, standardise failure codes, pilot, prove KPI improvement, scale (the pattern reported by Petrobras).

### Example
Age-replacement example: a bearing with planned replacement cost $C_p$ = ₹8,000, unplanned failure cost $C_f$ = ₹1,27,750 (repair plus downtime) and Weibull wear-out life (shape 2.5, scale 3,000 h; mean life about 2,662 h). Minimising the cost-rate formula numerically gives an optimal interval of about **870 h**, at which only about 4.4% of bearings would have failed first; expected cost is about **₹15.5 per hour**. Replacing at the scale life of 3,000 h costs about ₹35.7 per hour, and running to failure about ₹48 per hour (127,750 / 2,662). Policy: replace at the interval or on a vibration alarm, whichever comes first, and re-fit the Weibull parameters from PM history yearly. The inputs are illustrative.

### In the news
See news box. Equinor's aim of proactive maintenance on 40% of equipment illustrates that strategy is about selecting where condition-based logic pays, not about instrumenting everything.

### Interview angle
> [!question] How it is asked
> "You have 500 machines and limited budget. How do you prioritise maintenance strategies?"

> [!tip] Strong answer includes
> - Criticality ranking first (consequence times likelihood)
> - Matching strategy to failure pattern and cost of failure
> - Pilot, measure, scale; data readiness first
> - Shutdown planning basics for big-ticket work

Related: [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]], [[016 Digital Supply Chain & Industry 4.0]].
