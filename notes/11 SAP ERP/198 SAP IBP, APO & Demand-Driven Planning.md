---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP IBP, APO & Demand-Driven Planning"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 13
---
# SAP IBP, APO & Demand-Driven Planning

⬅ [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]] · [[_Index - SAP ERP|SAP ERP]] · [[199 SAP Ariba, SRM & Business Network]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. SAP Planning Landscape: ECC, APO, S/4HANA and IBP]]
2. [[#2. IBP Modules and Architecture]]
3. [[#3. Planning Areas, Time Profiles and Key Figures]]
4. [[#4. Statistical Forecasting in IBP]]
5. [[#5. Demand Sensing and Short-Term Signals]]
6. [[#6. Supply Planning: Heuristics, Constrained Optimiser and Response]]
7. [[#7. Inventory Optimisation (Multi-Echelon)]]
8. [[#8. S&OP and Collaboration in IBP]]
9. [[#9. Response Planning and Control Tower]]
10. [[#10. SAP APO History and Sunset]]
11. [[#11. Embedded PP/DS in S/4HANA and Integration (CPI-DS, SDI)]]
12. [[#12. IBP vs Kinaxis, o9 and Other Planning Platforms]]
13. [[#13. ⭐ Advanced: Demand-Driven Replenishment (DDMRP) in IBP]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): SAP pushes IBP towards AI-assisted, order-based and time-series planning in one planning area
> **IBP product updates announced at SAP Connect (7 October 2025).** SAP listed a harmonised planning area that supports both time-series and order-based planning, unified scenario simulations showing the effect of alerts and risks across planning horizons, characteristic-based planning for industries such as fashion retail, high tech and life sciences, a configurable Planner Workspace with Joule guidance, and embedded AI for forecasting and inventory management. The AI capabilities were in beta with general availability planned for Q2 2026; three Joule supply-chain agents were also announced (production planning and operations, GA planned Q1 2026; change record management, Q2 2026; supplier onboarding, available). ([SAP News Center, 7 Oct 2025](https://news.sap.com/2025/10/sap-connect-innovative-updates-supply-chain-management/))
>
> **SAP IBP review-platform ratings (24 November 2025).** SAP reported (data snapshot 5 November 2025) Gartner Peer Insights 4.8/5 on 51 reviews, TrustRadius 8.4/10 on 107 reviews and G2 4.3/5 on 251 reviews for IBP, and called it the leader among customers in supply chain planning. This is a vendor-published summary of customer reviews, so treat it as marketing evidence, not independent benchmarking. ([SAP News Center, 24 Nov 2025](https://news.sap.com/2025/11/sap-ibp-customer-choice-software-review-platforms/))
>
> **Competitor snapshot: Kinaxis 2025.** Wikipedia (citing company filings) reports Kinaxis 2025 revenue of US$548 million, 400+ customers, the Maestro concurrent planning platform with AI agents from 2025, and a new CEO (Razat Gaurav) from January 2026. ([Wikipedia: Kinaxis](https://en.wikipedia.org/wiki/Kinaxis))
>
> Sub-topics that say **"See news box"** reuse these items. Related notes: [[120 Integrated Business Planning (IBP) & S&OP Maturity]] (concepts), [[119 Supply Planning, DRP & Available-to-Promise]], [[117 Demand-Driven MRP (DDMRP) & Buffer Management]].

---
## 1. SAP Planning Landscape: ECC, APO, S/4HANA and IBP
> 🟠 Tier 2 · _Key points:_ ERP execution vs planning layer; APO (on-premise) to IBP (cloud); embedded planning in S/4HANA

### Definition
SAP's planning stack has three layers:
- **ERP planning (execution-level):** MRP in ECC/S/4HANA (see [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]]) plus PP in [[081 SAP PP — Production Planning]]. Net requirements, lot sizing, purchase requisitions and planned orders, based on a single plant view.
- **Advanced planning (network-level):** **SAP APO** (Advanced Planner and Optimizer), part of **SAP SCM**, a separate server linked to ECC by the **Core Interface (CIF)**. Modules: **DP** (demand planning), **SNP** (supply network planning, with heuristic, capacity levelling and optimiser), **PP/DS** (production planning and detailed scheduling), **GATP** (global ATP), **TP/VS** (transportation planning and vehicle scheduling).
- **Cloud planning:** **SAP Integrated Business Planning (IBP)** on SAP HANA, delivered as SaaS with Excel and web (Fiori) UI. IBP replaces APO's functionality, using key figures and planning areas in place of APO's planning books and macros. In S/4HANA, **embedded PP/DS** (no separate SCM server or CIF) and **aATP** cover short-term production scheduling and availability, while IBP covers tactical and strategic planning.

Typical target architecture: **S/4HANA (execution) + embedded PP/DS (detailed scheduling, optional) + IBP (demand, supply, inventory, S&OP) + EWM/TM (execution)**.

### Example
A Pune FMCG company runs ECC with APO DP/SNP. At S/4HANA migration it replaces APO DP with IBP for Demand, APO SNP with IBP for Supply (heuristics, optimiser), keeps MRP for plant-level planning, and uses embedded PP/DS for the packing lines, thus retiring the SCM server and the CIF queues. See [[200 SAP S-4HANA Migration, Data Migration & Testing]] for the migration view.

### In the news
See news box. The October 2025 update stresses one harmonised planning area in IBP, the direction of travel for combining tactical (time-series) and operational (order-based) planning.

### Interview angle
> [!question] How it is asked
> "What are the differences between MRP, APO and IBP, and where would each be used?"

> [!tip] Strong answer includes
> - Layered view: ERP execution, advanced planning, cloud IBP
> - Module mapping from APO (DP, SNP, PP/DS, GATP, TP/VS) to IBP and S/4HANA (Demand, Supply, Response, aATP, TM)
> - Why constrained, network-wide planning needs more than single-plant MRP
> - Awareness of the migration drivers (APO lifecycle, S/4HANA, cloud)

---
## 2. IBP Modules and Architecture
> 🟠 Tier 2 · _Key points:_ Demand, Supply, Inventory, S&OP, Response, Control Tower; SaaS on HANA; Excel add-in and Fiori

### Definition
SAP's IBP product page lists these capability areas: **Forecasting and Demand Management** (demand planning, demand sensing, statistical models), **Response and Supply Planning** (multilevel supply planning, rough-cut planning, response management), **Sales and Operations Planning** (real-time planning, scenarios, collaboration), **Inventory Planning** (including demand-driven replenishment and inventory optimisation) and **Supply Chain Control Tower** (visibility and analytics). SAP claims 1,000+ companies use the platform (vendor figure from the product page).

| Module | Purpose | Planning style |
|---|---|---|
| IBP for Demand | Statistical forecasting, sensing, demand collaboration | Time series |
| IBP for Inventory | Multi-echelon safety stock optimisation, DDMRP-style replenishment | Time series |
| IBP for Supply | Constrained or unconstrained network supply plan: heuristics, optimiser | Time series |
| IBP for Response and Supply | Order-level, finite planning, what-if, allocation | Order-based (OBP) |
| IBP for S&OP | Consensus planning, scenarios, KPIs | Time series |
| Control Tower | Alerts and dashboards across modules | Both |

Architecture: **SaaS on HANA** with tenant per customer; users work through **Excel add-in**, **Fiori planner workspace**, jobs (**application jobs**) run statistical forecast, supply heuristics, optimiser, copy operations and alerts. Data enters through integration (see sub-topic 11).

### Example
S&OP cycle in IBP: Demand planner runs statistical forecast (Monday); sales overrides in the Excel add-in (Tuesday); supply planner runs supply heuristic or optimiser (Wednesday); S&OP meeting reviews scenarios and the executive approves the consensus (Thursday); the plan is released to S/4HANA as planned independent requirements (PIRs) for MRP.

### In the news
See news box. SAP's 2025 product statement puts embedded AI into forecasting and inventory management, so planners get recommendations rather than only running models.

### Interview angle
> [!question] How it is asked
> "Name the IBP modules and say which would solve a client's high forecast error and high safety stock."

> [!tip] Strong answer includes
> - Right module for the problem: Demand for forecast error, Inventory for stock levels, Supply for constraints
> - Time-series vs order-based planning
> - Cloud delivery, Excel and Fiori UI, integration with S/4HANA
> - Benefits quantified (forecast accuracy, stock cut) rather than only features

---
## 3. Planning Areas, Time Profiles and Key Figures
> 🟠 Tier 2 · _Key points:_ Master data types, attributes, planning level, time profile, key figure types, calculation; versions and scenarios

### Definition
IBP's data model:
- **Master data types:** product, location, customer, resource, and others. Each has **attributes** (e.g. product group, location region).
- **Planning area:** the container that defines which **key figures**, **attributes** and **time profile** are available and what **planning levels** can be used. A **sample planning area** can be copied and extended.
- **Planning level:** a combination of attributes at which a key figure is stored and calculated, for example product × customer × week for sales, or product family × month for S&OP. Aggregation and disaggregation between levels follow defined rules.
- **Time profile:** the hierarchy of time buckets (for example day, week, month, quarter, year) and the horizon; planning in IBP can use different levels per process (monthly S&OP, weekly supply).
- **Key figure (KF):** a measure with a type (stored, calculated, helper), unit, aggregation (sum, average) and calculation; examples **Statistical Forecast Quantity**, **Consensus Demand**, **Actual Sales**, **Safety Stock**, **Constrained Supply**.
- **Versions and scenarios:** the base version stores the official plan; **scenarios** are what-if copies that planners simulate and compare; approved scenarios are promoted to the base version.

Rule of thumb: design the planning area from the process backwards: what decisions, at what level, with which key figures and horizon.

### Example
For a snack company: planning area with product (SKU, brand), location (DC, plant) and customer (channel) attributes. Key figures: Actual Sales (history), Stat Forecast, Sales Input, Marketing Input, Consensus Demand. Levels: SKU × DC × week for operational demand planning (24-month horizon: 104 weeks), brand × month for the S&OP executive review. Disaggregation proportional to history splits brand forecast down to SKUs.

### In the news
See news box. The harmonised time-series and order-based planning area announced in October 2025 reduces the need to maintain separate planning areas for tactical and operational planning.

### Interview angle
> [!question] How it is asked
> "How would you design the IBP data model for a company with 10,000 SKUs, 3 plants and 25 DCs?"

> [!tip] Strong answer includes
> - Attributes, planning levels, time profile and key figures defined from the decisions needed
> - Aggregation and disaggregation logic, versions and scenarios
> - Volume and performance control (not planning at the lowest level without reason)
> - Governance of master data, linked to [[175 Data Quality, Master Data & Data Governance]]

---
## 4. Statistical Forecasting in IBP
> 🟠 Tier 2 · _Key points:_ Model families, automatic model selection, ensembles, error measures (MAPE, bias), forecast value added

### Definition
IBP Demand provides **statistical forecast** algorithms for time series: **moving average**, **single, double and triple exponential smoothing (Holt-Winters)**, **Croston** for intermittent demand, **regression and causal** models with external drivers, and **automatic model selection** that tests several models on a hold-out window and chooses by error measure. **Machine-learning forecast** (for example gradient boosting) can use many drivers such as promotions and prices. Theory for these methods is in [[066 Demand Forecasting & Time Series]], [[004 Demand Forecasting & Planning]] and [[218 Forecasting with ML & Foundation Models]].

Error measures (computed by the **forecast error calculation** operator): MAE, MAPE, WMAPE, bias.
$$\text{MAPE} = \frac{100}{n}\sum \frac{|A_t - F_t|}{A_t} \qquad \text{Bias} = \frac{1}{n}\sum (F_t - A_t)$$

**Forecast value added (FVA)** compares the accuracy of consensus overrides with the statistical baseline; negative FVA means human adjustments hurt.

### Example
Eight weeks of sales for an SKU: 120, 132, 128, 141, 150, 147, 160, 158. Simple exponential smoothing with $\alpha = 0.3$ and the first forecast set to 120 gives forecasts for weeks 2 to 8 of 120.0, 123.6, 124.9, 129.7, 135.8, 139.2, 145.4, and a week-9 forecast of **149.2**. MAE = **13.9**, MAPE = **9.4%** and bias = **−13.9** (forecast consistently below actuals: the trend is missed). A Holt model with $\alpha = 0.4$, $\beta = 0.2$ captures the trend and forecasts about **172.8** for week 9, so IBP's automatic model selection would favour a trend model here.

### In the news
See news box. AI forecasting in IBP was in beta in October 2025, with general availability planned for Q2 2026 (SAP statement).

### Interview angle
> [!question] How it is asked
> "Forecast error is 30% at SKU-week level. What do you do?"

> [!tip] Strong answer includes
> - Segment first (ABC/XYZ), choose models per demand pattern (smooth, intermittent, seasonal, new product)
> - Measure with MAPE/WMAPE and bias at the right level and lag
> - Aggregation: error falls at higher levels, so measure the decision level
> - FVA of overrides and promotions governance; see [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]]

---
## 5. Demand Sensing and Short-Term Signals
> 🟠 Tier 2 · _Key points:_ Short horizon, near-term orders and POS, ML on recent signals, lag-based accuracy

### Definition
**Demand sensing** improves the **short-term forecast** (typically the next few weeks) by learning from recent signals such as **latest orders, shipments, POS data, weather, promotions and web traffic**, compared with the statistical forecast that uses long history. In IBP Demand the sensing algorithm uses machine learning (for example gradient boosting on recent patterns) and outputs a **sensed demand** key figure that replaces the forecast in the near term, fading into the baseline further out. The conceptual background is in [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]].

Measuring: compare accuracy at the **lag** used by supply (e.g. forecast made 2 weeks ahead for week t), and track **forecast accuracy by lag** and **bias**. Sensing mainly helps with fast-moving, promotion-driven and channel-based products; it adds little for slow, stable items and requires clean daily or weekly data feeds.

### Example
Baseline forecast for next week: 1,000 units. Orders received in the last 3 days run 18% above the same days' pattern and a promotion is confirmed. Sensing raises next week to 1,160 and week 3 to 1,060, fading to 1,000 in week 5. Supply planning releases an extra 160 units to the DC this week to avoid out-of-stocks.

### In the news
See news box. SAP's 2025 roadmap emphasises embedded AI and scenario simulation across horizons, in line with moving signals into planning faster.

### Interview angle
> [!question] How it is asked
> "How is demand sensing different from statistical forecasting?"

> [!tip] Strong answer includes
> - Horizon (days to weeks versus months), data inputs and algorithm
> - Needs: granular data, integration frequency, process to act on the signal
> - Measurement at relevant lag and net benefit (stock-outs and inventory)
> - Limits: not for long-term strategy, and noise risk

---
## 6. Supply Planning: Heuristics, Constrained Optimiser and Response
> 🟠 Tier 2 · _Key points:_ Unconstrained heuristic, capacity levelling, optimiser (LP), order-based planning; cost vs service trade-off

### Definition
**IBP for Supply** creates a network plan from demand and constraints:
- **Heuristic (unconstrained):** pushes demand through the supply chain network using sourcing rules (quota arrangement, lead times) and shows resource overload.
- **Capacity levelling / constrained heuristic:** moves or shifts production to resolve overloads within limits.
- **Optimiser (constrained):** a **linear programming model** that minimises total cost (production, transport, storage, **penalties for late or unmet demand**, and inventory) subject to capacity, material and lot-size constraints; it can be run on **time-series** planning, with the objective set by cost parameters (see [[146 Operations Research - Linear Programming]] for the maths).
- **Response and Supply (order-based planning):** plans at **order level** with finite capacity and time-sensitive reaction to changes, with allocation and what-if; it works as the successor of APO PP/DS/SNP combined for tactical response.

Output is a **constrained supply plan** that goes to S/4HANA as planned orders or purchase requisitions, or as PIRs for MRP.

### Example
Demand 1,000 units next month. Plant A: capacity 600, cost ₹50 plus ₹6 transport = ₹56 per unit; Plant B: capacity 500, cost ₹58 plus ₹3 transport = ₹61 per unit; unmet demand penalty ₹200 per unit. Optimiser: A 600, B 400, total **₹58,000** (600 × 56 + 400 × 61 = 33,600 + 24,400). If Plant A loses capacity (maintenance) and can only make 450: A 450 (₹25,200), B 500 (₹30,500) and 50 units unmet (₹10,000 penalty), total **₹65,700**; the planner then evaluates a scenario using overtime or outsourcing for the 50 units at less than ₹200 per unit.

### In the news
See news box. The 2025 announcement of unified scenario simulation across horizons applies directly to this step: what-if runs of optimiser vs heuristic.

### Interview angle
> [!question] How it is asked
> "When would you use an optimiser rather than a heuristic in supply planning?"

> [!tip] Strong answer includes
> - Heuristic: fast, transparent, good for ranking decisions; optimiser: cost trade-offs across network
> - Objective with explicit costs and penalties, constraints, and sensitivity
> - Data needs and change management (planners trust)
> - Release to S/4HANA and exception handling

---
## 7. Inventory Optimisation (Multi-Echelon)
> 🟠 Tier 2 · _Key points:_ MEIO, service-level targets, guaranteed service times, safety stock by stage; DDMRP alternative

### Definition
**IBP for Inventory** computes **safety stocks** across a multi-stage network (**MEIO: multi-echelon inventory optimisation**). Inputs: demand variability and forecast error, supply lead-time variability, service-level targets (cycle service level or fill rate), costs, and the network structure with **service times** between stages. A common model is **guaranteed service time**: each stage quotes a service time $S$ to its customer and has net replenishment time $\tau = SI + LT - S$ where $SI$ is the inbound service time and $LT$ the lead time. Safety stock per stage:
$$SS = z \cdot \sigma_d \cdot \sqrt{\tau}$$
The optimiser chooses service times to minimise total holding cost, often pushing stock to where it is cheapest (upstream, semi-finished) or where it pools best. Complements: simple formula in [[003 Inventory Management]] and [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]].

### Example
Weekly demand sigma = 100 units, $z = 1.645$ (95%). Plant lead time 4 weeks, DC lead time 1 week, customer service time 0. Value per unit: ₹80 at the plant (semi-finished), ₹100 at the DC. **Plant quotes service 0** to DC: plant τ = 4, DC τ = 1: SS = 329 at plant + 164.5 at DC = 493.5 units, value ₹42,770. **Plant quotes service 4 weeks** (makes to order): plant τ = 0, DC inbound SI = 4 so DC τ = 5: SS = 367.8 at DC, value ₹36,783. **Plant quotes service 1**: 284.9 + 232.6 = 517.6 units, value ₹46,058. The second option has the lowest stock value, at the price of a slower replenishment loop that the planners must manage. Pooling: four DCs each with demand sigma 40 per week, lead time 2 weeks: separate safety stock 4 × 1.645 × 40 × $\sqrt{2}$ = 372 units; one central DC with sigma $40\sqrt{4}$ = 80 gives 186 units, a **50% cut**.

### In the news
See news box. Embedded AI for inventory management is part of SAP's October 2025 IBP announcements (beta at the time).

### Interview angle
> [!question] How it is asked
> "Why does multi-echelon optimisation beat setting safety stock at each location independently?"

> [!tip] Strong answer includes
> - Interdependence of stages through service times and lead times
> - Square-root pooling and cost-weighted placement
> - Inputs: forecast error, lead-time variability, service targets
> - Limits and practicalities: data quality, planner acceptance, review cadence

---
## 8. S&OP and Collaboration in IBP
> 🟠 Tier 2 · _Key points:_ Process steps, consensus demand, scenarios, KPIs, alerts, job scheduling

### Definition
**S&OP in IBP** operationalises the monthly cycle: **(1) data and performance review, (2) demand review (statistical + sales/marketing input), (3) supply review (constraints and scenarios), (4) pre-S&OP gap resolution, (5) executive S&OP and decisions**. IBP supports this with **scenario simulation**, alerts (for example demand over supply), **Planner Workspace dashboards**, collaboration (comments and tasks), and **what-if** on the financial view (revenue, margin, inventory value). Planning results are exposed in key figures such as **Consensus Demand**, **Supply Plan**, **Gap**, **Inventory Value**.

Maturity and governance of S&OP (stages, roles, KPIs) is in [[120 Integrated Business Planning (IBP) & S&OP Maturity]]; this note is about tool mechanics.

### Example
Executive meeting: scenario A (base): revenue ₹520 crore, gross margin 26%, inventory ₹95 crore. Scenario B (promote product X with 8% price cut): revenue ₹545 crore, margin 24.5%, inventory ₹104 crore. Margin in rupees: A = 0.26 × 520 = ₹135.2 crore; B = 0.245 × 545 = ₹133.5 crore. B adds revenue but reduces gross margin by ₹1.7 crore and raises inventory by ₹9 crore, so the executive team chooses A unless service gains justify B.

### In the news
See news box. Unified scenario simulation across planning horizons (SAP 2025 announcement) targets this exact decision step.

### Interview angle
> [!question] How it is asked
> "How would you set up the monthly S&OP cycle in IBP and measure its success?"

> [!tip] Strong answer includes
> - Calendar and roles: who inputs, who approves, what the decision is
> - Scenarios with financial view and risk, a single version of the truth
> - KPIs: forecast accuracy, bias, service level, inventory days, plan adherence
> - Link to finance (budget) and execution (MRP, procurement)

---
## 9. Response Planning and Control Tower
> 🟠 Tier 2 · _Key points:_ Order-based planning, allocation, what-if, alerts, control tower, supply chain orchestration

### Definition
**IBP for Response** (order-based planning) plans **at order level** with finite capacity, supports **allocation of constrained supply to customer orders**, and quickly re-plans after disruptions. It reads sales orders, stock, production and purchase orders from S/4HANA, and returns planned orders and confirmations. Planners use **Supply Chain Control Tower** dashboards: alerts, custom KPIs, maps and drill-down to resolve exceptions.

SAP also announced **SAP Supply Chain Orchestration** (H1 2026 availability) as an AI-centred solution for disruption detection and response on top of Business Network data, and integrates Business Network with ERP and planning ([[199 SAP Ariba, SRM & Business Network]]).

### Example
A fire stops a supplier for 10 days. Control Tower alert shows 12 production orders at risk; response planning re-sequences orders by margin and customer priority. Of 200 affected customer orders, 150 keep their dates, 30 are delayed by up to 3 days and 20 are re-sourced from another plant, so only 15% of the orders slip instead of all of them (illustrative figures).

### In the news
See news box. SAP announced the Orchestration product and Joule agents for supply chain to connect planning and execution signals (October 2025).

### Interview angle
> [!question] How it is asked
> "How would a control tower help during a supplier disruption?"

> [!tip] Strong answer includes
> - Detect (alerts), diagnose (drill-down), decide (scenarios), act (re-plan, release)
> - Prioritisation rules for allocation
> - Data latency and integration reliability
> - Examples from [[015 Supply Chain Risk & Resilience]]

---
## 10. SAP APO History and Sunset
> 🟠 Tier 2 · _Key points:_ APO as SCM component of Business Suite 7; CIF; end-of-maintenance link to Business Suite; migration paths

### Definition
**APO** was released around the early 2000s as part of **SAP SCM** (Supply Chain Management) and became SAP's standard advanced planning engine, using **liveCache** (an in-memory object store) and the **CIF** to exchange master and transaction data with ECC. Modules: DP, SNP, PP/DS, GATP, TP/VS.

Sunset logic: APO belongs to the **SAP Business Suite 7** generation. SAP's maintenance commitments for SAP SCM follow the Business Suite 7 timetable and SAP's publicised ECC dates (mainstream maintenance to 31 December 2027, extended maintenance to 31 December 2030, as quoted in the news box of [[080 SAP MM — Materials Management]], based on Gartner and secondary sources). The exact end-of-maintenance date for SAP SCM/APO releases should be confirmed in the SAP Product Availability Matrix and SAP's maintenance strategy before quoting in a client meeting (not verified for this note), and it is not part of S/4HANA. APO in an S/4HANA landscape is supported only in a limited, time-bound way; the strategic target is IBP plus embedded S/4HANA components.

Migration paths: **DP → IBP Demand**, **SNP → IBP Supply/Response**, **PP/DS → embedded PP/DS in S/4HANA or IBP order-based**, **GATP → aATP in S/4HANA**, **TP/VS → SAP TM** (see [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]]). Realistic effort: redesign, not lift-and-shift, because APO macros and CIF models do not move 1:1.

### Example
Client with 400 APO DP macros and 12 SNP planning books. Programme: inventory the macros, cut redundant ones (many are redundant after years of change), map the rest to IBP key figures and operators, parallel-run forecasts for 3 cycles, compare MAPE and bias between APO and IBP before cut-over.

### In the news
See news box. IBP, not APO, receives SAP's AI and scenario-simulation investment.

### Interview angle
> [!question] How it is asked
> "A client uses APO and plans S/4HANA. What is your recommendation for planning?"

> [!tip] Strong answer includes
> - APO mapped module by module to IBP, embedded PP/DS, aATP, TM
> - Timeline logic tied to Business Suite maintenance, with dates checked at the source
> - Parallel run, KPI baseline and macro rationalisation
> - Risks: custom code, planner adoption, data model redesign

---
## 11. Embedded PP/DS in S/4HANA and Integration (CPI-DS, SDI)
> 🟠 Tier 2 · _Key points:_ Embedded PP/DS; planning board; IBP integration via CPI-DS, SDI, SAP Cloud Integration; master data and transaction data

### Definition
**Embedded PP/DS** is detailed scheduling that runs inside S/4HANA (no SCM server, no CIF, shared data): **planning board**, heuristics, **sequence-dependent set-up**, finite capacity, and interactive rescheduling for plants with complex lines (licensing and scope should be confirmed with SAP). It is complemented by MRP Live for net requirements.

**IBP integration** with ECC/S/4HANA:
- **SAP Cloud Integration for data services (CPI-DS)** loads master data and time-series data (history, PIRs) on schedule through a **Data Services Agent**; widely used, batch-oriented.
- **SAP HANA smart data integration (SDI)** with a **Data Provisioning Agent** supports real-time or frequent replication for some objects.
- **Order-based planning integration** uses real-time or near-real-time interfaces for orders and stock from S/4HANA, and returns planned orders.
- **Data quality**: planning output is only as good as units of measure, calendars, BOMs, lead times and master data (see [[175 Data Quality, Master Data & Data Governance]]).

### Example
Integration design: nightly CPI-DS jobs load 36 months of sales history and open orders to IBP; IBP returns the consensus forecast as PIRs to S/4HANA every Thursday; MRP Live then runs on Friday; embedded PP/DS sequences the packing lines. Monitoring: job failure alerts, record-count reconciliation between S/4HANA and IBP.

### In the news
See news box. The October 2025 announcement of order-based and time-series planning in one planning area reduces the number of integration objects customers must maintain.

### Interview angle
> [!question] How it is asked
> "How does data flow between S/4HANA and IBP, and what could break it?"

> [!tip] Strong answer includes
> - Master data, history, orders and stock inbound; PIRs and planned orders outbound
> - Tools (CPI-DS, SDI, cloud integration) and scheduling
> - Reconciliation checks and error handling
> - Roles: who owns master data and planning parameters

---
## 12. IBP vs Kinaxis, o9 and Other Planning Platforms
> 🟠 Tier 2 · _Key points:_ Concurrent planning, knowledge graph, SAP-centric integration, total cost, best-of-breed vs suite

### Definition
Planning vendors differ in architecture and fit:
- **SAP IBP:** modular, strongest where the ERP is SAP (S/4HANA integration, shared master data); broad scope (demand, inventory, supply, S&OP, response); SAP reports 1,000+ companies on the platform (product page) and strong review-platform ratings (news box, vendor-published).
- **Kinaxis (Maestro, formerly RapidResponse):** **concurrent planning** on shared data so demand, supply and inventory change propagate in real time; 400+ customers and 2025 revenue of US$548 million (Wikipedia); AI agents introduced from 2025.
- **o9 Solutions:** a platform with an enterprise knowledge graph and a broad planning scope (qualitative; figures not verified here).
- **Others:** Blue Yonder, Oracle SCM planning, Anaplan (financial and S&OP), Coupa supply chain design, John Galt, ToolsGroup, RELEX (retail), Logility.

Selection criteria: ERP fit and integration cost, planning depth (finite scheduling, MEIO), speed of what-if, implementation partner ecosystem, total cost, planner usability, and vendor roadmap. Market maps appear in [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]].

### Example
A pharma group on S/4HANA with multi-site finite scheduling needs: scorecard weights ERP integration 30%, planning depth 25%, usability 15%, cost 15%, partner availability 15%. IBP 8, 7, 6, 7, 8 → 2.4 + 1.75 + 0.9 + 1.05 + 1.2 = **7.30**; best-of-breed alternative 7, 8, 8, 6, 6 → 2.1 + 2.0 + 1.2 + 0.9 + 0.9 = **7.10** (illustrative scores). Close, so a proof of value on the client's data decides.

### In the news
See news box for SAP's ratings claims and the Kinaxis 2025 snapshot; neither replaces a proof of concept.

### Interview angle
> [!question] How it is asked
> "Why would you recommend IBP and not Kinaxis or o9 for this client?"

> [!tip] Strong answer includes
> - Criteria and weights first, not vendor preference
> - Fit with ERP landscape and existing skills
> - Proof-of-value and reference checks, TCO over 5 years
> - Fair strengths of each vendor

---
## 13. ⭐ Advanced: Demand-Driven Replenishment (DDMRP) in IBP
> ⭐ Advanced · _Added beyond the tracker_

### Definition
The SAP IBP product page lists **demand-driven replenishment** within inventory planning. **DDMRP** (see [[117 Demand-Driven MRP (DDMRP) & Buffer Management]]) positions **decoupling points** and sizes **buffers** with three zones:
$$\text{Red zone} = \text{red base} + \text{red safety}, \quad \text{Yellow} = ADU \times DLT, \quad \text{Green} = \max(\text{MOQ},\ ADU \times DLT \times LTF,\ \text{order cycle} \times ADU)$$
where ADU is average daily usage, DLT the decoupled lead time and LTF the lead-time factor. **Net flow position** = on-hand + on-order − qualified demand; an order is proposed when net flow falls into the yellow zone or below, and its size brings the position to the top of green. In IBP, buffer parameters are key figures that are recalculated periodically, and the system generates **replenishment proposals** and priority views (buffer penetration).

### Example
ADU 100 units/day, DLT 10 days, lead-time factor 0.5, variability factor 0.5, MOQ 200. Yellow = 100 × 10 = 1,000. Red base = ADU × DLT × LTF = 100 × 10 × 0.5 = 500; red safety = red base × variability = 250; red = 750. Green = max(200, 500, order cycle 5 days × 100 = 500) = 500. Top of green = 750 + 1,000 + 500 = **2,250**. If net flow position is 1,400 (inside yellow, below top of yellow 1,750), the order quantity = 2,250 − 1,400 = **850** units.

### In the news
See news box. IBP's October 2025 inventory and AI updates sit alongside demand-driven features as complementary methods to MEIO.

### Interview angle
> [!question] How it is asked
> "When would DDMRP beat classical MRP or MEIO, and how does IBP support it?"

> [!tip] Strong answer includes
> - Decoupling, buffers and net flow position with a worked example
> - Suitable situations: volatile demand, long and variable lead times, complex BOMs
> - Parameter governance: ADU, variability and lead-time factors reviewed regularly
> - Pitfalls: poor decoupling points, buffers set once and forgotten
