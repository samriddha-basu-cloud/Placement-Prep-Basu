---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Production & Operations Planning"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 15
---
# Production & Operations Planning

⬅ [[004 Demand Forecasting & Planning]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[006 Manufacturing Systems]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Aggregate Planning]]
2. [[#2. Capacity Planning]]
3. [[#3. Line Balancing]]
4. [[#4. Master Production Schedule (MPS)]]
5. [[#5. Material Requirements Planning (MRP)]]
6. [[#6. MRP II]]
7. [[#7. ERP in Production]]
8. [[#8. Production Scheduling]]
9. [[#9. Job Sequencing Rules]]
10. [[#10. Bottleneck Analysis]]
11. [[#11. Theory of Constraints (TOC)]]
12. [[#12. Shop Floor Control]]
13. [[#13. Rough-Cut Capacity Planning (RCCP)]]
14. [[#14. ⭐ Advanced: Lot-Sizing Techniques in MRP]]
15. [[#15. ⭐ Advanced: OEE & Finite-Capacity Scheduling (APS)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): when one missing component rewrites the production plan
> **Honda and the Nexperia shortage (Oct 2025).** Honda reduced output at its US and Canadian plants and halted its Celaya, Mexico plant (over 190,000 vehicles produced last year, mainly HR-V SUVs for North America) because of a chip shortage linked to Nexperia amid US-China trade tensions and Chinese export rules. Honda said it was "making arrangements to resume operations" with timing unclear; Nissan was surveying its parts makers. ([Japan Times](https://www.japantimes.co.jp/business/2025/10/30/companies/honda-mexico-production-halt/))
> 
> **Suzuki Swift halt (Jun 2025).** After China suspended exports of a wide range of rare earths and related magnets in April 2025, Suzuki halted Swift production at its Sagara plant, reported as the first Japanese automaker affected. The Swift Sport variant was unaffected, a reminder that shortages are SKU-specific and plans must be re-sequenced by variant. ([Deccan Herald / Reuters](https://www.deccanherald.com/business/companies/suzuki-motor-halted-swift-car-production-due-to-chinas-rare-earth-curbs-sources-say-3572312))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Aggregate Planning
> 🔴 Tier 1 · _Tracker hint:_ Chase, Level, Mixed strategies; trade-offs in workforce & inventory

### Definition
Aggregate planning sets, for a medium horizon (6-18 months), the **production rate, workforce size, overtime, subcontracting and inventory** for an aggregated product family, to meet forecast demand at minimum cost. Inputs: demand forecast, capacity, costs (regular and overtime labour, hiring/firing, holding, backorder/stock-out, subcontracting).

| Strategy | Idea | Pros | Cons |
|---|---|---|---|
| **Chase** | Production = demand each period; vary workforce/overtime | Low inventory | Hiring/firing cost, morale, training |
| **Level** | Constant output; inventory absorbs swings | Stable workforce | High holding cost, risk of stock-outs/obsolescence |
| **Mixed (hybrid)** | Level base plus overtime/subcontracting/part-time | Balanced | Complex |

Methods: spreadsheet trial-and-error, linear programming / transportation method, heuristics. Output feeds the **MPS** (disaggregation).

### Example
Monthly demand: Jan 800, Feb 1,000, Mar 1,200, Apr 1,000 (total 4,000; opening stock 0). **Level plan** = 1,000/month. End inventories: Jan +200, Feb +200, Mar 0 (1,000 − 1,200 = −200, using the 200), Apr 0. Unit-months held = 400; at ₹10 per unit-month = **₹4,000**. **Chase** holds zero stock but must vary output 800 → 1,200, incurring hire/fire or overtime: if changing 200 units of output costs ₹15,000 each time (three changes: +200, +200, −200) = ₹45,000, level is cheaper here.

### In the news
See news box. Plan changes after component outages are aggregate-plan reworks: re-allocate output across plants and variants and rebuild the plan when the missing part returns (catch-up via overtime).

### Interview angle
> [!question] How it is asked
> "A seasonal demand business: would you chase or level production?"

> [!tip] Strong answer includes
> - Definitions of chase, level, mixed with cost trade-offs
> - Cost elements and which dominates (inventory cost, labour flexibility, perishability)
> - Practical levers: overtime, subcontracting, temporary labour, pre-build
> - Link to S&OP and MPS

---

## 2. Capacity Planning
> 🔴 Tier 1 · _Tracker hint:_ Design capacity, effective capacity, utilization, efficiency

### Definition
- **Design capacity**: maximum possible output under ideal conditions.
- **Effective capacity**: achievable output given product mix, maintenance, scheduling, breaks (always ≤ design).
- **Actual output**: what is produced after breakdowns, scrap, absenteeism.

$$\text{Utilisation} = \frac{\text{Actual output}}{\text{Design capacity}}, \qquad \text{Efficiency} = \frac{\text{Actual output}}{\text{Effective capacity}}$$

Capacity strategies: **lead** (build ahead of demand), **lag** (add after demand proves), **match**. Options: add shifts/overtime, subcontract, capex, flexible workforce. Long-range capacity planning (facilities), medium (workforce, shifts), short (scheduling). Capacity cushion = 100% − average utilisation. Rule: running near 100% utilisation raises queues and lead time non-linearly (Kingman/queuing logic).

### Example
Design capacity 100 units/shift, effective 80, actual 68. Utilisation = 68/100 = **68%**; efficiency = 68/80 = **85%**. To meet a demand of 6,800 units over 100 shifts the plant is fine; for demand of 9,000 units, capacity needed = 9,000/(80 × 0.85) = 132 shifts, i.e. add 32 shifts or a second line.

### In the news
See news box. Plants with high utilisation have no slack to recover from a stoppage; Honda's restart involves catching up under capacity constraints.

### Interview angle
> [!question] How it is asked
> "A plant runs at 90% utilisation and customers complain about late deliveries. Why?"

> [!tip] Strong answer includes
> - Distinguish design, effective, actual; utilisation vs efficiency
> - High utilisation increases queues and lead time (variability)
> - Options: bottleneck relief, shifts, subcontracting, demand shaping
> - Lead/lag/match strategy with capex risk

---

## 3. Line Balancing
> 🔴 Tier 1 · _Tracker hint:_ Cycle time, workstation assignment, precedence diagram, idle time%

### Definition
Assigning tasks to workstations on an assembly line so each station's workload is as equal as possible given the **precedence diagram**.

$$CT = \frac{\text{Available time per period}}{\text{Required output}}, \quad N_{min} = \left\lceil \frac{\sum t_i}{CT} \right\rceil$$
$$\text{Efficiency} = \frac{\sum t_i}{N_{actual}\times CT}, \quad \text{Idle time \%} = 1 - \text{Efficiency}, \quad \text{Balance delay} = \text{idle \%}$$

Heuristics: **Largest Candidate Rule**, **Ranked Positional Weight (RPW)**, Kilbridge-Wester, and COMSOAL; assign tasks to the current station in order while time ≤ CT and precedence is satisfied. Takt time = available time / customer demand.

### Example
Shift 7.5 hours = 27,000 s; demand 450 units: $CT = 27{,}000/450 = 60$ s. Total task time = 240 s: $N_{min} = 240/60 = 4$ stations. If the best feasible assignment needs 5 stations: efficiency = 240/(5 × 60) = **80%**, idle = **20%**. If CT is cut to 50 s: $N_{min} = \lceil 4.8 \rceil = 5$, efficiency = 240/(5 × 50) = 96%.

### In the news
See news box. Variant-specific shortages (Swift vs Swift Sport) change the mix on a mixed-model line, forcing re-balancing and re-sequencing.

### Interview angle
> [!question] How it is asked
> "Compute the cycle time and minimum number of stations; what is the efficiency?"

> [!tip] Strong answer includes
> - CT and N_min formulas with numbers
> - Precedence constraints and heuristic (RPW)
> - Efficiency / idle time interpretation
> - Practical: variability, ergonomics, multi-skilled operators, mixed-model lines

---

## 4. Master Production Schedule (MPS)
> 🔴 Tier 1 · _Tracker hint:_ Disaggregated from aggregate plan; time-phased

### Definition
The **MPS** is a time-phased plan of **what end items to produce, how many and when** (typically weekly buckets), disaggregated from the aggregate plan and driven by forecast and **customer orders**. It is the main input to MRP. Elements: **forecast, customer orders (backlog), projected on-hand, MPS quantity, ATP (available-to-promise)**. Time fences: **demand time fence** (inside it, orders rule; firm), **planning time fence** (changes need approval).

$$\text{Projected OH}_t = \text{OH}_{t-1} + \text{MPS}_t - \max(\text{Forecast}_t,\ \text{Customer orders}_t)$$

Plan an MPS lot when projected OH would go negative. **ATP** for the first period = OH + MPS − committed orders until the next MPS.

### Example
Opening on-hand 50, lot size 70. Forecast (wk1-4): 30, 30, 40, 40; customer orders: 35, 28, 20, 10. Week 1: use max(30,35) = 35: OH = 15, no MPS. Week 2: 15 − 30 = −15 → MPS 70, OH = 15 + 70 − 30 = 55. Week 3: 55 − 40 = 15. Week 4: 15 − 40 = −25 → MPS 70, OH = 15 + 70 − 40 = 45. **MPS = 0, 70, 0, 70.**

### In the news
See news box. Shortages trigger MPS re-planning: swap to variants whose parts are available, freeze near-term, and reschedule others.

### Interview angle
> [!question] How it is asked
> "What is the difference between aggregate plan, MPS and MRP?"

> [!tip] Strong answer includes
> - Hierarchy: family (aggregate) → end item (MPS) → components (MRP)
> - Time fences and ATP
> - Role of the MPS in making delivery promises
> - RCCP check before releasing

---

## 5. Material Requirements Planning (MRP)
> 🔴 Tier 1 · _Tracker hint:_ BOM, gross vs net requirements, planned order releases

### Definition
MRP is a **dependent-demand** logic that, from the MPS, **BOM** and **inventory records**, calculates what components to order and when.

Steps: **explode** the BOM (level by level) → gross requirement → subtract on-hand and scheduled receipts → **net requirement** → apply **lot sizing** → **offset by lead time** → **planned order receipts** and **planned order releases**.

$$\text{Net req} = \text{Gross req} - \text{On hand} - \text{Scheduled receipts} + \text{Safety stock}$$

Inputs: MPS, BOM, inventory status (records accuracy ≥ 95%+ needed), lead times, lot-size rules. Outputs: planned orders, reschedule messages, exception reports. Weakness: infinite-capacity assumption, nervousness, garbage-in-garbage-out.

### Example
Product A needs 2 units of B (BOM: A → 2B). Demand for A is 100 in week 5; on-hand A 20; lead time of A assembly 1 week; B on hand 30; B lead time 2 weeks; lot-for-lot. A: net = 100 − 20 = 80; **release 80 A in week 4**. B: gross = 80 × 2 = 160; net = 160 − 30 = 130; **release 130 B in week 2** (4 − 2).

### In the news
See news box. MRP exposes shortages as exception messages; with a missing chip, MRP shows which end items are not buildable (pegging) so planners can reprioritise.

### Interview angle
> [!question] How it is asked
> "Given this BOM and inventory, compute the planned order releases."

> [!tip] Strong answer includes
> - Explosion, netting, lot sizing, lead-time offsetting in order
> - Inputs and accuracy needs (BOM, inventory records)
> - Gross vs net, scheduled receipts
> - Limitations (no capacity check) and MRP II/APS fixes

---

## 6. MRP II
> 🔴 Tier 1 · _Tracker hint:_ Extended to capacity, finance, HR; closed-loop MRP

### Definition
**Closed-loop MRP** adds feedback: after MRP generates plans, **capacity requirements planning (CRP)** checks feasibility; shop-floor and purchasing execution report back so plans are revised. **MRP II (Manufacturing Resource Planning)** extends this to the whole business: sales and operations planning, MPS, RCCP, MRP, CRP, shop-floor control, purchasing, plus **financial planning** (costing, budgets, cash flow), **distribution (DRP)** and simulation of "what-if". Name introduced by Oliver Wight (1980s). ERP later added HR, finance, CRM and all modules on one database.

Evolution: MRP (materials) → closed-loop MRP (capacity + feedback) → MRP II (business resources) → ERP (enterprise) → APS/IBP (optimised, constraint-based).

### Example
Closed loop: MRP releases 130 B in week 2; CRP finds the machining centre needs 120 hours but has 100. Planner shifts 20 hours to week 1 or adds overtime. MRP II converts the plan into rupees: purchases of ₹X crore feed the cash-flow forecast so finance can arrange working capital.

### In the news
See news box. Plan feasibility under shocks (capacity AND material) is why firms invest in constraint-based planning beyond classic MRP.

### Interview angle
> [!question] How it is asked
> "How is MRP II different from MRP and ERP?"

> [!tip] Strong answer includes
> - MRP = materials; closed-loop adds capacity and feedback; MRP II adds finance, S&OP, DRP
> - ERP extends to HR, CRM, supply chain on one database
> - Why each step emerged (infinite capacity problem)
> - Today: APS/IBP

---

## 7. ERP in Production
> 🔴 Tier 1 · _Tracker hint:_ SAP PP module: routing, work centers, production orders

### Definition
In **SAP PP (Production Planning)** the master data are: **Material master** (MM01), **BOM** (CS01), **Work center** (CR01: capacity, cost centre, formulas), and **Routing** (CA01: sequence of operations with times, work centers, components). Execution:

```
CS01   Create BOM                     CA01   Create routing
CR01   Create work center             MM01   Create material master
MD61   Create planned independent requirements (PIR)
MD01   MRP run - total planning       MD04   Stock/requirements list
MD02   MRP run - single item, multi-level
CO01   Create production order       CO02   Change order     CO03  Display order
CO11N  Time-ticket confirmation       COOIS  Order information system
```

Flow: PIR/sales order → MRP → **planned order** → convert to **production order** (CO01 or via MD04) → **release** → material staging, goods issue (MIGO movement 261) → operation **confirmation** (CO11N) → goods receipt (movement 101) → **settlement** of order costs. Repetitive manufacturing, process orders (PP-PI) and Kanban are variants. In S/4HANA, MRP Live (MD01N) is the faster run.

### Example
A bike assembler: BOM for Bike X has frame, 2 wheels, handlebar; routing has 3 operations (weld at WC-WELD, 20 min; assemble at WC-ASSY, 15 min; test at WC-TEST, 5 min). A production order for 100 bikes schedules 100 × 40 = 4,000 min of work across the three work centers; confirming each operation back-flushes components if configured.

### In the news
See news box. Planners used ERP/MRP exception lists to see which production orders were short of the missing component and re-sequence them (general practice).

### Interview angle
> [!question] How it is asked
> "Walk me through the production process in SAP, from planned order to goods receipt."

> [!tip] Strong answer includes
> - Master data: material, BOM, work center, routing
> - Process flow with T-codes and goods movement types (261 issue, 101 receipt)
> - How MRP creates planned orders and how they convert
> - Integration with MM (procurement), SD (demand) and CO (costing)

---

## 8. Production Scheduling
> 🔴 Tier 1 · _Tracker hint:_ Forward vs backward scheduling; Gantt chart

### Definition
Scheduling assigns specific jobs to machines and times.
- **Forward scheduling:** start from today/release date, schedule operations as early as possible; gives the earliest completion date; builds inventory/WIP if finished early.
- **Backward scheduling:** start from the due date and schedule operations as late as possible; minimises WIP and inventory; risk if any delay (no slack).
- **Finite vs infinite capacity** loading; **Gantt chart** shows jobs against time and resources (Henry Gantt); a load chart shows machine utilisation.

Concepts: lead time = queue + setup + run + wait + move; queue time usually 80-90% of lead time in job shops. Advanced: APS, constraint-based finite scheduling, genetic algorithms. Aim: meet due dates, minimise setups, flow time, WIP.

### Example
Order due on day 20; operations take 5, 4, 3 days (total 12), no queues. **Backward:** op3 days 18-20, op2 days 14-18, op1 days 9-14, so **start day 8 (latest)**. **Forward** from day 0 finishes at day 12, giving 8 days of slack/early inventory. Choose forward if capacity is tight and delay is costly; backward for JIT.

### In the news
See news box. After a stoppage, plants reschedule forward to recover fastest, using finite-capacity logic to see what can actually be built when parts return.

### Interview angle
> [!question] How it is asked
> "Forward versus backward scheduling: when would you use each?"

> [!tip] Strong answer includes
> - Definitions and consequence (inventory vs lateness risk)
> - Calculation with slack
> - Finite-capacity and bottleneck focus
> - Gantt chart and use in project/shop floor

---

## 9. Job Sequencing Rules
> 🔴 Tier 1 · _Tracker hint:_ FCFS, SPT, LPT, EDD, CR — definitions and applications

### Definition
Priority (dispatching) rules for sequencing jobs at one machine:
- **FCFS**: first come, first served; fair, poor performance.
- **SPT** (shortest processing time): minimises **average flow time** and WIP; may starve long jobs.
- **LPT**: longest processing time first; used for load balancing (parallel machines, makespan).
- **EDD** (earliest due date): minimises **maximum lateness/tardiness**.
- **CR** (critical ratio) = (due date − today) / remaining processing time; CR < 1 behind schedule, = 1 on time, > 1 ahead; dynamic.
- Others: slack time, **Johnson's rule** (two-machine flow shop makespan), WSPT.

Measures: flow time, lateness (completion − due), tardiness = max(0, lateness), makespan, utilisation, WIP.

### Example
Jobs (processing days, due day): A (3, 5), B (2, 6), C (4, 7), D (1, 8). **SPT:** D, B, A, C; completion 1, 3, 6, 10; average flow = 20/4 = **5.0**; tardiness: A = 1, C = 3, others 0, average 1.0, max 3. **EDD/FCFS:** A, B, C, D; completion 3, 5, 9, 10; average flow = 27/4 = **6.75**; tardiness C = 2, D = 2, average 1.0, **max 2**. SPT has the lowest flow time; EDD has the lowest maximum tardiness.

### In the news
See news box. When scarce chips or magnets limit builds, priority rules decide which orders or variants get the scarce parts first (customer priority, margin, due date), often a CR/EDD-type rule.

### Interview angle
> [!question] How it is asked
> "Sequence these 5 jobs by SPT and EDD and compare."

> [!tip] Strong answer includes
> - Definitions and the metric each rule optimises
> - Worked comparison table
> - Trade-offs (starvation of long jobs under SPT)
> - Which rule for which context: SPT for throughput, EDD for delivery, CR for dynamic shops

---

## 10. Bottleneck Analysis
> 🔴 Tier 1 · _Tracker hint:_ Identification using utilization%, impact on throughput

### Definition
A **bottleneck** is the resource whose capacity limits system output; **throughput of the line = capacity of the bottleneck**. Identification: highest utilisation (load/capacity), longest queue in front, starved downstream stations, longest processing time per unit, WIP piling up before it. Capacity of a station = units per hour = 1/processing time (× machines). **Utilisation** = demand rate / capacity.

Effects: one hour lost at the bottleneck = one hour lost for the whole system; an hour saved elsewhere is a mirage. **Improvement levers:** protect with buffer, never starve it, reduce its setups, add shift/overtime, offload to non-bottleneck, add machine, improve yield before it, remove inspection from it. Beware **moving bottlenecks** after you fix one.

### Example
Process: Cut 10 units/hr, Weld 6/hr, Paint 8/hr; market demand 8/hr. Utilisation at demand: Cut 80%, Weld 8/6 = **133% (bottleneck)**, Paint 100%. Throughput = 6/hr (capacity of Weld). Adding a second paint booth gives nothing; adding a welder (12/hr) moves the bottleneck to Paint (8/hr) and throughput to 8/hr.

### In the news
See news box. A missing component is a *material* bottleneck: the constraint moved from machine capacity to part supply, and plants without alternates had to idle.

### Interview angle
> [!question] How it is asked
> "Throughput at the plant is below target. How do you find and fix the bottleneck?"

> [!tip] Strong answer includes
> - Identify with utilisation, queue and starvation, not opinion
> - Quantify throughput impact; protect and exploit it
> - Elevate (capex) only after exploiting
> - Re-check as the bottleneck moves

---

## 11. Theory of Constraints (TOC)
> 🔴 Tier 1 · _Tracker hint:_ Goldratt's 5 steps; Drum-Buffer-Rope; throughput accounting

### Definition
Eliyahu Goldratt (*The Goal*, 1984): every system has at least one constraint limiting its goal (making money). **Five focusing steps:**
1. **Identify** the constraint.
2. **Exploit** it (squeeze maximum from existing capacity).
3. **Subordinate** everything else to the constraint.
4. **Elevate** the constraint (invest to increase capacity).
5. **Repeat**; avoid inertia (the constraint moves).

**Drum-Buffer-Rope (DBR):** the **drum** is the constraint's schedule (sets the pace); the **buffer** is time/stock protecting the constraint from starvation; the **rope** is the signal that releases material at the pace of the drum.

**Throughput accounting:** Throughput $T$ = sales − truly variable costs (TVC, mainly materials); Inventory $I$ = money invested; Operating expense $OE$. $NP = T - OE$; $ROI = NP/I$. Rank products by **throughput per constraint minute**, not by margin per unit.

### Example
Product P: price ₹100, TVC ₹40, T = ₹60, uses 5 min on the constraint: ₹12 per constraint minute. Product Q: price ₹130, TVC ₹50, T = ₹80, uses 8 min: **₹10** per constraint minute. P is better for the constrained resource despite lower T per unit. In 600 constraint-minutes: P gives 120 units × 60 = ₹7,200; Q gives 75 units × 80 = ₹6,000.

### In the news
See news box. In a component shortage the scarce part *is* the constraint: TOC says allocate it to the products with the highest throughput per unit of the scarce part.

### Interview angle
> [!question] How it is asked
> "Which product should the company make when the machine is the limiting factor?"

> [!tip] Strong answer includes
> - Five steps stated in order and illustrated
> - Throughput per constraint unit calculation
> - DBR: drum, buffer, rope
> - Contrast: local efficiency vs system throughput

---

## 12. Shop Floor Control
> 🔴 Tier 1 · _Tracker hint:_ Dispatching, progress reporting, expediting, variance analysis

### Definition
Execution-level control that makes the plan happen:
- **Order release and dispatching**: release production orders, daily dispatch list by priority (rules in section 9).
- **Progress reporting / data collection**: confirmations, barcode/RFID, MES, operator time tickets, scrap and downtime reasons.
- **Expediting**: chase late orders, materials, tooling.
- **Input-output control**: monitor planned vs actual input/output at work centres to control queues and lead time.
- **Variance analysis**: schedule variance (planned vs actual dates), efficiency variance (standard vs actual hours), usage variance (material), rate variance, yield/scrap.
- **Feedback loop** to MRP/planning.

Tools: **MES** (Manufacturing Execution System), OEE dashboards, andon, daily management meetings (Gemba). OEE = Availability × Performance × Quality.

### Example
Standard 100 hours for a batch, actual 112: efficiency variance = 12 hours adverse (12%). If the standard labour rate is ₹300/hr, cost variance = 12 × 300 = **₹3,600** unfavourable. Input-output: planned input to a work centre 200 hrs/wk vs actual 240 and output 200: queue grows by 40 hrs a week, so lead time is rising.

### In the news
See news box. Restarting after a halt depends on shop-floor control: re-sequencing, kitting scarce parts, and tracking recovery hour by hour.

### Interview angle
> [!question] How it is asked
> "How do you ensure the production plan is actually executed on the floor?"

> [!tip] Strong answer includes
> - Dispatching, confirmations, expediting, escalation
> - Key variances and OEE
> - Daily management meeting and visual boards
> - Feedback to planning (reschedule) and root-cause problem solving

---

## 13. Rough-Cut Capacity Planning (RCCP)
> 🔴 Tier 1 · _Tracker hint:_ Resource profile method; load vs capacity comparison

### Definition
RCCP checks whether the **MPS** is feasible against **key (critical) resources** before MRP runs, to avoid releasing impossible plans. Methods:
1. **Capacity Planning using Overall Factors (CPOF)**: historical total hours per unit allocated by resource share.
2. **Bill of labour/resources approach**.
3. **Resource profile (resource bill)**: for each product, hours per unit at each critical resource (with lead-time offsets).

$$\text{Load}_{r,t} = \sum_{p} \text{MPS}_{p,t}\times \text{hours}_{p,r}$$

Compare load to available capacity (effective). Overloads → shift production, add overtime/subcontract, or revise MPS. **RCCP** is rough (key resources, no queues); **CRP** is detailed (all work centres, from MRP planned orders, with routing and lead times).

### Example
MPS week 3: Product X 60 units, Product Y 40 units. Hours per unit on the assembly line: X 2.0, Y 1.5. Load = 60×2 + 40×1.5 = 120 + 60 = **180 hours**. Available: 4 workers × 40 hr × 90% efficiency = 144 hours. **Overload 36 hours (125% load)**. Options: 36 hours of overtime, move 18 units of X to week 2 (18 × 2 = 36 hr), or subcontract.

### In the news
See news box. Resource-profile checks tell you whether catch-up output after a restart is physically feasible, or if shifts must be added.

### Interview angle
> [!question] How it is asked
> "How do you check if the master schedule can be achieved with current capacity?"

> [!tip] Strong answer includes
> - RCCP vs CRP and when each applies
> - Resource profile formula with numbers
> - Resolve overload: shift, overtime, subcontract, revise MPS
> - Put RCCP before MRP in the planning cascade

---

## 14. ⭐ Advanced: Lot-Sizing Techniques in MRP
> ⭐ Advanced · _Added beyond the tracker_

### Definition
MRP needs a rule to convert net requirements into order quantities:
- **Lot-for-lot (L4L)**: order exactly net requirement; zero holding, many setups.
- **Fixed order quantity / EOQ**: see [[003 Inventory Management]]; best for steady demand, poor for lumpy.
- **Periodic order quantity (POQ)**: order enough to cover a fixed number of periods; $POQ = EOQ/\bar d$ (EOQ in periods of demand).
- **Part-period balancing / Silver-Meal**: add periods until average cost per period starts rising.
- **Wagner-Whitin**: dynamic programming optimum for time-varying demand.

Total cost = setup cost + holding cost (usually on end-of-period stock).

### Example
Net requirements weeks 1-4: 40, 60, 0, 80. Setup S = ₹100, holding H = ₹1 per unit-week. **L4L:** 3 orders (40, 60, 80) = ₹300 setup, 0 holding = **₹300**. **2-period POQ:** order 100 in week 1 (covers weeks 1-2): holds 60 for one week = ₹60; week 3 has no requirement; order 80 in week 4. Setups 2 × 100 = ₹200, holding ₹60, total **₹260**, cheaper than L4L.

### In the news
See news box. After disruptions, planners shift to smaller lots or lot-for-lot for scarce components to avoid tying up parts in one product, while changing lot rules for stable parts.

### Interview angle
> [!question] How it is asked
> "Which lot-sizing rule would you choose, and what are the cost components?"

> [!tip] Strong answer includes
> - Names and logic of L4L, POQ, EOQ, Silver-Meal, Wagner-Whitin
> - Cost arithmetic on a small example
> - Match rule to demand pattern and setup cost
> - Note: reducing setup cost (SMED) makes small lots economical

---

## 15. ⭐ Advanced: OEE & Finite-Capacity Scheduling (APS)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**OEE (Overall Equipment Effectiveness)** = Availability × Performance × Quality:
- Availability = run time / planned production time (losses: breakdowns, changeovers)
- Performance = (ideal cycle time × total count) / run time (losses: slow cycles, minor stops)
- Quality = good count / total count

World-class benchmark often quoted ≈ 85% (a rule of thumb). Use OEE on the bottleneck to prioritise improvement (six big losses). **TEEP** includes unscheduled time.

**APS (Advanced Planning & Scheduling)** replaces MRP's infinite-capacity assumption with **finite, constraint-based** planning (material, machine, labour, tools) using heuristics/optimisation; tools: SAP PP/DS (in S/4HANA), SAP IBP, o9, Kinaxis, Siemens Opcenter. Handles sequence-dependent setups, what-if scenarios and re-planning after disruptions.

### Example
Planned time 480 min; downtime 48 min → run time 432; availability = 432/480 = **90%**. Ideal cycle 1 min, produced 410 units in 432 min: performance = 410/432 = **94.9%** (≈95%). Good units 402: quality = 402/410 = **98.0%**. OEE = 0.90 × 0.949 × 0.98 ≈ **83.7%**. Raising availability by 5 points (to 95%) lifts OEE to about 88.3%.

### In the news
See news box. Planners using APS can re-run schedules around a missing component within hours, while spreadsheet planning takes days: a practical resilience capability (general statement).

### Interview angle
> [!question] How it is asked
> "How would you improve the output of a plant without buying a new machine?"

> [!tip] Strong answer includes
> - OEE decomposition and loss tree; focus on the bottleneck
> - SMED, preventive maintenance (TPM), quality at source
> - Finite-capacity scheduling to cut changeovers and waiting
> - Quantify: each OEE point on the bottleneck equals X units/₹

---
## 🔗 Go deeper: expansion notes
- [[117 Demand-Driven MRP (DDMRP) & Buffer Management|Demand-Driven MRP (DDMRP) & Buffer Management]]
- [[119 Supply Planning, DRP & Available-to-Promise|Supply Planning, DRP & Available-to-Promise]]
- [[153 Aggregate Planning Models & Workforce Strategy|Aggregate Planning Models & Workforce Strategy]]
- [[193 SAP MRP Deep Dive - Planning Strategies & Parameters|SAP MRP Deep Dive - Planning Strategies & Parameters]]
