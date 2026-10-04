---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Supply Planning, DRP & Available-to-Promise"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Supply Planning, DRP & Available-to-Promise

⬅ [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[120 Integrated Business Planning (IBP) & S&OP Maturity]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. The Supply Planning Process and Where It Sits]]
2. [[#2. Distribution Requirements Planning (DRP): Logic and Worked Table]]
3. [[#3. Constrained vs Unconstrained Planning]]
4. [[#4. Supply Network Planning: Heuristics vs Optimiser]]
5. [[#5. Deployment and Fair-Share Allocation]]
6. [[#6. Replenishment Rules: Lot-for-Lot, Fixed Lot and Min-Max]]
7. [[#7. Time Fences: Demand, Planning and Frozen Horizon]]
8. [[#8. Available-to-Promise (ATP) and Order Promising]]
9. [[#9. Capable-to-Promise (CTP) and Global Promising]]
10. [[#10. Supplier Scheduling and Release Planning]]
11. [[#11. S&OE: Sales and Operations Execution]]
12. [[#12. SAP and APS Tie-Ins: IBP, S/4HANA, PP/DS]]
13. [[#13. ⭐ Advanced: Plan Stability, Nervousness and Supply Planning KPIs]]

## 📰 News box
> [!news] Shared news hook for this topic (2026): planning platforms are being bought on "visibility and real-time response"
> **Ansaldo Energia selects Kinaxis Maestro (25 August 2026).** The 170-year-old Italian power-generation technology company chose Kinaxis Maestro for supply chain planning and orchestration after evaluating several leading platforms, citing end-to-end visibility, real-time synchronisation and AI-powered orchestration; PwC leads the implementation. No financial terms were disclosed. ([Kinaxis press release](https://www.kinaxis.com/en/news/press-releases/2026/ansaldo-energia-selects-kinaxis-power-future-global-energy-infrastructure))
>
> **Sterlite Technologies (STL) selects Kinaxis Planning One (12 August 2026).** The Indian optical and digital networking company picked the planning solution to improve visibility, respond faster to market changes and strengthen cross-functional coordination; Kinaxis said it was its first customer win through Google Marketplace's mid-market initiative. STL's CEO said the aim is a supply chain "built to sense and respond in real time". ([Kinaxis press release](https://www.kinaxis.com/en/news/press-releases/2026/sterlite-technologies-limited-selects-kinaxis-strengthen-supply-chain))
>
> **SAP IBP positioning.** SAP says more than 1,000 companies worldwide use SAP Integrated Business Planning, and describes its supply planning as constrained or unconstrained, heuristic-based or optimisation-based, with a separate response and supply module for feasible order-level plans. ([SAP IBP overview](https://www.sap.com/products/scm/integrated-business-planning.html); [IBP features](https://www.sap.com/products/scm/integrated-business-planning/features.html))
>
> Sub-topics that say **"See news box"** reuse these items. All items are vendor statements.

---
## 1. The Supply Planning Process and Where It Sits
> 🔴 Tier 1 · _Key points:_ Consensus demand in, feasible supply plan out, released to execution

### Definition
**Supply planning** turns the consensus demand plan into a feasible plan for production, procurement and distribution that meets service and cost targets within capacity and material limits. Sequence:
1. **Inputs**: consensus demand (see [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]], [[120 Integrated Business Planning (IBP) & S&OP Maturity]]), inventory and open orders, bills of materials and routings, lead times, capacities, supplier and transport constraints, policy parameters (safety stock, lot sizes).
2. **Netting** at each node: requirements less stock and scheduled receipts.
3. **Planning proposals**: planned production, purchase and transfer orders.
4. **Constraint check**: capacity, material, storage, transport, budget; resolve gaps by levelling, overtime, outsourcing, shifting, allocation.
5. **Release** to execution: MRP/PO/STO or schedule releases, then S&OE (sub-topic 11).
Planning layers by horizon: strategic network ([[113 Network Design & Facility Location Modelling]]), tactical **supply network planning (SNP)** at 3-24 months, operational **MRP/DRP and production scheduling** (see [[005 Production & Operations Planning]], [[021 Scheduling & Sequencing]]), execution. Inputs from [[003 Inventory Management]] policies decide how inventory targets feed the plan.

### Example
Consensus demand for next month is 12,000 units; opening stock 2,000 and target closing stock 3,000, scheduled receipts 1,500. Net requirement = 12,000 + 3,000 − 2,000 − 1,500 = **11,500 units**. Plant capacity is 10,500 units: a 1,000-unit gap goes to the constraint step (overtime, a co-packer, pull-in from the previous month, or demand shaping).

### In the news
See news box. Ansaldo's and STL's platform choices are about linking these layers, from S&OP down to order-level response, in a single model.

### Interview angle
> [!question] How it is asked
> "Walk me through how a supply plan is built from the demand forecast."

> [!tip] Strong answer includes
> - Inputs, netting, proposals, constraint check, release
> - Distinguishes tactical (SNP) from operational (MRP/DRP) planning
> - States how gaps are resolved, with trade-offs
> - Feedback loop to S&OP and execution

---
## 2. Distribution Requirements Planning (DRP): Logic and Worked Table
> 🔴 Tier 1 · _Key points:_ Time-phased netting by stocking location; planned releases back-schedule by lead time

### Definition
**DRP** extends MRP logic to the distribution network: for each DC or depot, time-phased forecast demand is netted against projected on-hand to create **planned receipts**, which are back-scheduled by transit lead time into **planned order releases** that become requirements (dependent demand) on the supplying node. For each period:

$$POH_t = POH_{t-1} + \text{Receipts}_t - \text{Gross requirements}_t$$

A planned receipt is created whenever projected on-hand would fall below **safety stock**; the quantity is a lot size multiple. Releases roll up the network: the DC's release is the plant's or the central warehouse's gross requirement, giving the plant a time-phased, actual-use view that avoids the amplification of ordering independently. DRP complements reorder-point replenishment by looking forward, handling promotions, seasonality and lumpy lot sizes. See [[010 Warehouse Management]] and [[009 Logistics & Distribution]].

### Example
DC with opening on-hand 130, safety stock 20, lead time 2 weeks, lot size 150. Gross requirements (weeks 1-8): 40, 50, 60, 50, 70, 60, 80, 70.

| Week | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Gross req. | 40 | 50 | 60 | 50 | 70 | 60 | 80 | 70 |
| Planned receipt | 0 | 0 | 150 | 0 | 150 | 0 | 0 | 150 |
| Projected on-hand | 90 | 40 | 130 | 80 | 160 | 100 | 20 | 100 |
| Planned release (2 wk earlier) | 150 | 0 | 150 | 0 | 0 | 150 | 0 | 0 |

Week 3: 40 − 60 = −20 is below safety stock 20, so a 150 lot is received (on-hand 130). The first release (150) falls in week 1, i.e. it must be placed now; had it fallen before week 1 it would be past due and flagged for expediting. The three releases (1, 3, 6) are the plant's gross requirements.

### In the news
See news box. DRP-style netting across nodes underlies the "end-to-end visibility" both Kinaxis customers cite.

### Interview angle
> [!question] How it is asked
> "How is DRP different from reorder-point replenishment, and when would you use it?"

> [!tip] Strong answer includes
> - Time-phased forecast netting vs statistical trigger at a fixed level
> - Back-scheduling by transit time; roll-up to the plant
> - Use when demand is lumpy/seasonal and lead times are long
> - Weakness: depends on forecast quality; mitigated by DDMRP buffers ([[117 Demand-Driven MRP (DDMRP) & Buffer Management]])

---
## 3. Constrained vs Unconstrained Planning
> 🔴 Tier 1 · _Key points:_ Unconstrained shows need; constrained shows what is feasible; gap drives decisions

### Definition
An **unconstrained** (infinite-capacity) plan ignores capacity and material limits and shows the **requirement**; a **constrained** (finite) plan respects limits and shows what is **feasible**. The *gap* between them is the decision list. MRP is typically unconstrained with a later capacity check (CRP/RCCP, see [[005 Production & Operations Planning]]); APS and SNP optimisers are constrained. Practical sequence: run unconstrained to expose the gap, then constrain with rules or optimisation, and agree actions in the supply review of S&OP. Constraint types: production capacity, labour, tooling, supplier capacity, storage, transport, shelf-life, shared components, financial limits.

### Example
Monthly demand 1,200, 1,300 and 1,500 units (total 4,000); capacity 1,300 a month (3,900). The unconstrained plan needs 1,500 in month 3 against capacity of 1,300, a 200-unit gap in that month; month 1 has 100 spare units of capacity, so total demand exceeds total capacity by 100 units (4,000 vs 3,900). Options: pre-build 100 in month 1 and hold for 2 months at ₹100 a unit-month = **₹20,000**; or overtime in month 3 at ₹800 extra per unit = **₹80,000** for 100 units. The pre-build is cheapest for the first 100 units; the remaining 100-unit gap needs overtime, outsourcing or a revised promise date, so the constrained plan carries an explicit **100-unit shortfall** to be decided in S&OP.

### In the news
See news box. SAP's IBP page describes both constrained and unconstrained heuristic or optimisation supply planning, treating the choice as a configuration of the same model.

### Interview angle
> [!question] How it is asked
> "Demand exceeds capacity for the next two quarters. What do you do?"

> [!tip] Strong answer includes
> - Quantify the gap (units, ₹, timing) from the unconstrained plan
> - Option ladder: pre-build, shift, overtime, outsource, allocate, demand-shape
> - Compare cost and service impact per option
> - Decision forum: S&OP supply review and executive S&OP

---
## 4. Supply Network Planning: Heuristics vs Optimiser
> 🔴 Tier 1 · _Key points:_ Rule-based fast vs cost-minimising LP; transparency vs optimality

### Definition
- **Heuristics**: rule-based, level by level (top-down), such as demand netting then capacity levelling then deployment. Fast, transparent and predictable; may be sub-optimal and sequential decisions cannot trade off across nodes.
- **Optimiser (LP/MIP)**: minimise total cost (production + transport + holding + penalties for late or unmet demand) subject to balance, capacity and policy constraints; see [[146 Operations Research - Linear Programming]], [[147 Operations Research - Transportation, Assignment & Transshipment]] and [[148 Operations Research - Network Models & Integer Programming]]. Better when many trade-offs interact (multi-plant sourcing, shelf-life), but needs clean cost data and planners to trust it; results are less obviously "explainable".
$$\min \sum_{i,j} c_{ij}x_{ij} \quad \text{s.t.} \quad \sum_j x_{ij}\le Cap_i,\;\; \sum_i x_{ij} = D_j,\;\; x_{ij}\ge 0$$
Typical practice: heuristics for stable parts and routine runs; optimiser for allocation, sourcing and what-if.

### Example
Plant P1 (capacity 500) and P2 (capacity 400); DC1 demand 450, DC2 demand 350. Landed cost per unit (₹): P1→DC1 46, P1→DC2 48, P2→DC1 55, P2→DC2 50.
**Greedy rule** (serve DC2 first from the cheapest plant): P1→DC2 350 (₹16,800), then DC1 gets P1's remaining 150 (₹6,900) and 300 from P2 (₹16,500): total **₹40,200**.
**Optimiser** (solved as an LP): P1→DC1 450 (₹20,700), P1→DC2 50 (₹2,400), P2→DC2 300 (₹15,000): total **₹38,100**, saving **₹2,100** (5.2%) on one run, by serving the DC where the plant advantage is greatest.

### In the news
See news box. SAP offers both heuristic and optimisation planning in IBP; the choice is configured per use case.

### Interview angle
> [!question] How it is asked
> "When would you use an optimiser rather than a heuristic for supply planning?"

> [!tip] Strong answer includes
> - Compare transparency vs optimality, speed vs data needs
> - A small numerical example showing greedy vs optimum
> - Use optimisers where interactions are strong (multi-sourcing, constraints)
> - Governance: planners can override and understand the result

---
## 5. Deployment and Fair-Share Allocation
> 🔴 Tier 1 · _Key points:_ Push vs pull deployment; allocate scarce supply by cover, not by loudness

### Definition
**Deployment** decides how available supply at a source node (plant or central warehouse) is distributed to destination nodes (DCs) in the short term. If supply exceeds requirements, **push** the surplus per rules (target days of supply). If supply is short, a **fair-share** rule allocates scarce stock. Two common rules: (a) **proportional to demand** and (b) **equalise cover** (days of supply) after allowing for each node's current stock:

$$\text{Alloc}_j = \Big(\frac{S + \sum_k OH_k}{\sum_k D_k}\Big) D_j - OH_j$$

(b) avoids giving more to a node that already holds stock. Other tie-breakers: customer priority, service commitments, shelf-life, transport load building (full trucks). Fair share is the supply-side counterpart of product allocation in order promising (sub-topic 8).

### Example
Supply 1,000 units; demand (next cycle) A 600, B 500, C 400; on-hand A 100, B 50, C 150.
- Proportional: A 400, B 333, C 267 → resulting cover (stock after allocation / demand) = 83%, 77%, **104%**: C ends with more than it needs while B is short.
- Equalise cover: target cover = (1,000 + 300)/1,500 = 86.7%; allocations **A 420, B 383, C 197** (sum 1,000), all nodes at 86.7% cover.
Equalising cover is fairer on service; proportional allocation is simpler to explain. Round to full-truck or case multiples afterwards.

### In the news
See news box. "Sense and respond in real time" (STL) is what fair-share logic provides when a disruption hits and deployment must be re-run daily.

### Interview angle
> [!question] How it is asked
> "We have 1,000 units and three regions want 1,500. How do you allocate?"

> [!tip] Strong answer includes
> - Fair-share method with cover equalisation and arithmetic
> - Overlay of customer priority, margin, contractual obligations
> - Re-run frequently; communicate the allocation transparently
> - Fix the root cause: capacity, supplier, forecast bias

---
## 6. Replenishment Rules: Lot-for-Lot, Fixed Lot and Min-Max
> 🔴 Tier 1 · _Key points:_ Match rule to item; avoid system defaults

### Definition
- **Lot-for-lot (L4L)**: order exactly the net requirement each period. No excess, maximum orders; suits high-value, low-setup, or make-to-order items.
- **Fixed order quantity / EOQ**: order a fixed lot when needed; suits stable demand with high setup cost.
- **Period order quantity (POQ)**: cover a fixed number of periods.
- **Min-max (s, S)**: when inventory position falls to or below **min** (s), order up to **max** (S); the order size varies; suits many low-value items with continuous review ([[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]).
- **Reorder point (Q, R)** and **two-bin/kanban** for C items.
Lot-sizing trade-offs and MRP algorithms (Wagner-Whitin, Silver-Meal, part-period) are in [[005 Production & Operations Planning]]. Apply by item class: A items L4L or short POQ; C items min-max with bulk; perishable items small frequent lots.

### Example
Item with min 100, max 300. Inventory position 90 triggers an order of 300 − 90 = **210**; position 140 does not. Lead-time demand 40/day for 3 days, review each day: min must cover 120 plus safety stock, so with a safety stock of 40 units min = 120 + 40 = 160; max = min + EOQ-like quantity (say 200) = 360. Missing this arithmetic is the common cause of stock-outs on min-max items: the min was set too low when lead time rose.

### In the news
See news box. Platforms from SAP and Kinaxis expose these rules as parameters, so planners can set them per segment instead of globally.

### Interview angle
> [!question] How it is asked
> "When would you use lot-for-lot versus min-max replenishment?"

> [!tip] Strong answer includes
> - Definitions with order size logic
> - Choose by cost of setup vs holding, value, demand pattern
> - Min must cover lead-time demand plus safety stock
> - Review lot sizes when lead times or demand change

---
## 7. Time Fences: Demand, Planning and Frozen Horizon
> 🔴 Tier 1 · _Key points:_ Control change near the present; protect stability

### Definition
Time fences stabilise plans:
- **Demand time fence (DTF)**: inside it, the forecast is ignored and only customer orders drive demand (the near term is "known").
- **Planning time fence (PTF)**: inside it, the system does not auto-create, move or delete orders; changes need planner approval, and capacity/material are committed.
- **Frozen horizon**: the span where nothing is changed (schedule is locked for production execution).
Beyond the PTF the system can re-plan freely, within **liquid** (flexible) zones. Fences trade **stability** (fewer schedule changes, lower nervousness, supplier trust) against **flexibility** (ability to respond). Typical settings are tied to the cumulative lead time for critical components: the DTF to the shortest time in which production can respond to a new order, the PTF to the component or supplier lead time.

### Example
Product with DTF = 2 weeks, PTF = 6 weeks, forecast 100 a week. Week 1 orders 120 and week 2 orders 90: demand inside DTF = 120 and 90 (forecast ignored). Week 3 orders 40: demand = max(100, 40) = 100 (forecast consumption). A rush order for 80 units arriving in week 3 with free capacity of 50 is inside the PTF: the planner must decide, e.g. approve overtime or allocate 50 and promise 30 next week; the system will not silently move other work.

### In the news
See news box. As planning tools shorten response times (real-time re-planning), firms must still choose fences so that suppliers receive stable schedules.

### Interview angle
> [!question] How it is asked
> "The plan changes every day and the shop floor ignores it. What would you do?"

> [!tip] Strong answer includes
> - Time fences (DTF, PTF, frozen) with rules for each
> - Plan stability KPI and review of change reasons
> - Trade-off flexibility vs stability; link to S&OE
> - Supplier schedule firm/forecast split

---
## 8. Available-to-Promise (ATP) and Order Promising
> 🔴 Tier 1 · _Key points:_ Uncommitted supply; cumulative ATP; allocation and checking rules

### Definition
**ATP** is the quantity of an item uncommitted and available to promise to new customer orders. In an MPS-based (discrete) ATP, each time a master-schedule receipt occurs, compute for that period:

$$ATP = (\text{On-hand, first period only}) + MPS_t - \sum \text{Customer orders until the next MPS receipt}$$

and the **cumulative ATP** is the running sum used for promising. A new order is promised in the earliest period where cumulative ATP covers it, else a later date or a partial. Modern order promising adds **checking rules** (stock, receipts, planned production, supply across plants: *global ATP*), **product allocation** (reserve quantities by customer or channel), **backorder processing** (re-run to reprioritise after shortages), substitution and alternative-location rules. In SAP S/4HANA the engine is **advanced ATP (aATP)** with product allocation (PAL) and backorder processing (BOP); see [[195 SAP SD Advanced - Pricing, Output & Document Flow]] and [[082 SAP SD — Sales & Distribution]], and order-management practice in [[138 Order Management, Customer Service & Cost-to-Serve]].

### Example
On-hand 50. MPS receipts of 100 in weeks 2, 4 and 6. Booked orders weeks 1-6: 30, 40, 20, 50, 10, 40.

| Receipt week | Periods covered | ATP calculation | ATP | Cumulative |
|---|---|---|---|---|
| 1 (on-hand) | wk 1 | 50 − 30 | 20 | 20 |
| 2 | wk 2-3 | 100 − (40 + 20) | 40 | 60 |
| 4 | wk 4-5 | 100 − (50 + 10) | 40 | 100 |
| 6 | wk 6 | 100 − 40 | 60 | 160 |

A new order for 70 units due week 4: cumulative ATP at week 4 is 100, so it can be promised for week 4 (after which cumulative ATP in week 4 falls to 30). An order of 120 for week 4 is promised 100 in week 4 and 20 from week 6 (cumulative ATP 160) or by an expedite.

### In the news
See news box. Real-time synchronisation across the network (Ansaldo) is exactly what allows promise dates to reflect stock, supply and capacity.

### Interview angle
> [!question] How it is asked
> "A key customer wants 120 units next week. How do you decide what to promise?"

> [!tip] Strong answer includes
> - ATP logic with cumulative ATP and allocation rules
> - Priority customers: product allocation and backorder re-prioritisation
> - Partial vs split shipments; communication of reliable dates
> - Link: ATP accuracy depends on inventory record accuracy ([[116 Inventory Valuation, Cycle Counting & Inventory Governance]])

---
## 9. Capable-to-Promise (CTP) and Global Promising
> 🔴 Tier 1 · _Key points:_ ATP plus uncommitted capacity and material

### Definition
**CTP** extends ATP by checking **unused capacity and component availability** to produce new supply, not only existing supply. The promised date is the earlier of when stock is available and when the item can be built given the lead time, slots, and material. CTP needs a finite-capacity view and is typical of make-to-order and configure-to-order (ETO partially). **Global ATP/CTP** looks across plants and DCs, choosing the source by rules (cost, date, service). Compare with **ATD/profitable-to-promise (PTP)**, which prioritises orders by margin when supply is scarce. CTP depends on a trustworthy lead time, so set the **promise lead time** realistically rather than as the best case.

### Example
Item built in 1 day on a line with weekly capacity 120 units and 90 already committed: free capacity 30. Material for 40 units is on hand. A customer asks for 50: CTP is limited by capacity (30) and material (40), so **30 units can be promised for this week**; the next 20 depend on next week's capacity and a material receipt. Contrast with ATP, which would have said zero (no finished stock).

### In the news
See news box. In 2026, Ansaldo's emphasis on "complete visibility across operations" reflects the data prerequisites for credible CTP.

### Interview angle
> [!question] How it is asked
> "What is the difference between ATP and CTP and when does CTP matter?"

> [!tip] Strong answer includes
> - ATP uses existing/planned supply; CTP adds capacity and material
> - Relevance for make-to-order and shortages
> - Data needs: finite capacity, BOM, lead times, availability
> - Risk: over-promising when the capacity model is inaccurate

---
## 10. Supplier Scheduling and Release Planning
> 🔴 Tier 1 · _Key points:_ Scheduling agreements, firm vs forecast zones, supplier visibility

### Definition
For repetitive purchased parts, replacing individual purchase orders with a **scheduling agreement** (blanket contract plus periodic delivery schedule) gives suppliers visibility. The schedule has a **firm** zone (committed, short term), a **trade-off** zone (changes allowed within limits), and a **forecast** zone (indicative, for supplier planning); changes within the fixed horizon cost money. Delivery schedules can be released weekly, daily, or as JIT calls ([[131 Automotive Supply Chain - JIT, Tiers & EVs]]). Combine with VMI or consignment for C parts ([[003 Inventory Management]]), supplier portals, and scorecards for schedule adherence. In SAP, scheduling agreements and release documentation sit in the procurement module; see [[192 SAP Sourcing & Procurement Deep Dive]] and [[199 SAP Ariba, SRM & Business Network]]. Supplier schedule stability links with time fences (sub-topic 7).

### Example
A bearing supplier receives a 13-week schedule at about 3,000 a week. Weeks 1-2 are firm (3,000 each); weeks 3-4 are flexible within ±20% (2,400-3,600 a week); weeks 5-13 are forecast only. If the OEM raises week 3 to 3,800, the supplier is obliged to deliver only up to 3,600 and the extra 200 is best effort; if the OEM cuts week 2 (firm) to 2,500, it compensates the supplier for the 500-unit shortfall at the contract rate (for example ₹150 per bearing for committed material, or ₹75,000). Risk is allocated transparently by zone.

### In the news
See news box. Kinaxis, SAP and others advertise supplier collaboration as part of end-to-end planning; the schedule is what is actually shared.

### Interview angle
> [!question] How it is asked
> "How do you give a supplier a stable plan when your demand is volatile?"

> [!tip] Strong answer includes
> - Scheduling agreement with firm/flexible/forecast zones
> - Frozen horizon and flex limits; cost of changes
> - Share forecast and inventory visibility; VMI where suitable
> - KPIs: schedule adherence, OTIF, schedule stability

---
## 11. S&OE: Sales and Operations Execution
> 🔴 Tier 1 · _Key points:_ Weekly or daily response layer below S&OP

### Definition
**S&OE** manages **near-term** (days to ~4 weeks) deviations from plan: shortages, expediting, reallocations, order promising, transport changes, late deliveries. It sits below the monthly S&OP/IBP cycle and uses fresh signals (stock, orders, shipments, supplier updates, [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]] sensed demand). Typical format: a **daily or weekly meeting** supported by a control tower with exception alerts ranked by value and date; decisions are bounded by tactical guardrails from S&OP (allocation rules, spend limits). Link: [[120 Integrated Business Planning (IBP) & S&OP Maturity]]. Metrics: OTIF, backlog, expedite cost, schedule adherence, plan stability, time to decide.

### Example
A line failure cuts tomorrow's output by 2,000 units, 40% of the planned. S&OE huddle within 2 hours: re-run deployment with fair share, allocate to top-10 customers by contract priority, shift 500 units from another plant at ₹14 per unit extra freight (₹7,000), and promise revised dates for the rest. The tactical effect (lost quarter volume) is moved to the next S&OP supply review.

### In the news
See news box. "Sense and respond in real time" (STL) is the S&OE promise; the underlying data feed matters most.

### Interview angle
> [!question] How it is asked
> "What is the difference between S&OP and S&OE?"

> [!tip] Strong answer includes
> - Horizon (months vs days-weeks), purpose (align vs respond)
> - Frequency, participants, decision rights
> - Guardrails flowing from S&OP to S&OE and feedback back
> - Metrics and tools (control tower, alerts)

---
## 12. SAP and APS Tie-Ins: IBP, S/4HANA, PP/DS
> 🔴 Tier 1 · _Key points:_ Which tool plans what and at which horizon

### Definition
| Layer | SAP component | What it does |
|---|---|---|
| Strategic / tactical | **SAP IBP** (supply planning, S&OP, scenario planning) | Network supply plan, heuristics or optimiser, what-if |
| Order-level response | **IBP response and supply** | Feasible order-based plans, short horizon |
| Operational planning | **S/4HANA MRP (MRP Live)**, **PP/DS** | Material and capacity planning, finite scheduling |
| Replenishment | **Demand-driven replenishment (DDR)** | Buffer-based replenishment (see [[117 Demand-Driven MRP (DDMRP) & Buffer Management]]) |
| Order promising | **aATP** | ATP/product allocation/backorder processing |
| Execution | MM/SD/EWM | POs, deliveries, warehouse tasks |
In legacy SAP APO (being replaced), **SNP** provided heuristic and optimiser runs plus deployment and TLB (transport load builder); see [[198 SAP IBP, APO & Demand-Driven Planning]], [[081 SAP PP — Production Planning]], [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]] and the technology landscape in [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]. Non-SAP: Kinaxis Maestro, o9, Blue Yonder, Oracle SCM, Anaplan. Key design question: where to cut planning between tactical network optimisation and operational execution, and how plans flow back.

### Example
A consumer products company: IBP for a monthly constrained network plan, S/4HANA MRP Live for material plans, PP/DS for line scheduling, aATP for order promising, EWM for the warehouse. A mapping workshop assigns each decision (monthly production volume, weekly line schedule, daily allocation) to a tool, avoiding the commonest failure: two tools planning the same decision with different results.

### In the news
See news box. SAP's claim of over 1,000 IBP customers and Kinaxis's wins at STL and Ansaldo show the market is moving to cloud planning suites over legacy APS.

### Interview angle
> [!question] How it is asked
> "A client runs MRP in SAP ECC. What would you recommend to improve supply planning?"

> [!tip] Strong answer includes
> - Clarify pain points first (service, inventory, expedites, plan stability)
> - Map decisions to tools by horizon; avoid duplicating logic
> - Data prerequisites: master data, lead times, capacity
> - Phased roll-out and change management

---
## 13. ⭐ Advanced: Plan Stability, Nervousness and Supply Planning KPIs
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Nervousness** is plan instability in response to small demand or supply changes: orders move, resize and cancel repeatedly, and suppliers and shop floors lose trust. Controls: time fences (sub-topic 7), **change thresholds** (re-plan only if the change exceeds X%), **lot sizing with firming**, planning at the right aggregation level, buffers at decoupling points ([[117 Demand-Driven MRP (DDMRP) & Buffer Management]]), and exception-based review. KPIs for supply planning:
- **Plan attainment / schedule adherence** = actual output on plan ÷ planned output.
- **Plan stability** = share of planned orders in the frozen horizon unchanged at execution.
- **Supply plan feasibility**: constrained vs unconstrained gap.
- **Service**: OTIF, fill rate, backlog; **inventory**: days of cover vs target.
- **Expedite and premium freight cost** per ₹ of sales ([[012 Supply Chain Analytics & KPIs]], [[009 Logistics & Distribution]]).

### Example
Frozen horizon of 4 weeks holds 80 planned production orders. At execution 62 are unchanged: **stability = 62/80 = 77.5%**; target 90%. Root cause analysis shows 11 changes from demand updates, 5 from supplier delay, 2 from machine breakdowns. Fix: widen DTF by a week for A items and agree supplier schedule rules, targeting 90% within a quarter. Plan attainment: 9,400 of 10,000 planned units produced on time = 94%.

### In the news
See news box. IDC's finding (in its AI study) that 12% of leaders have governance fully embedded applies to planning too: automated re-planning without stability rules creates noise faster.

### Interview angle
> [!question] How it is asked
> "How do you know whether your supply planning process is working?"

> [!tip] Strong answer includes
> - Output KPIs (OTIF, inventory days) and process KPIs (stability, attainment, gap)
> - Root-cause analysis of plan changes
> - Targets and cadence; link to S&OP review
> - Avoid single-metric gaming (inventory without service)
