---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Integrated Business Planning (IBP) & S&OP Maturity"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 14
---
# Integrated Business Planning (IBP) & S&OP Maturity

⬅ [[119 Supply Planning, DRP & Available-to-Promise]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. From S&OP to IBP: What and Why]]
2. [[#2. The Five-Step Monthly Cycle]]
3. [[#3. Data Gathering and the Demand Review]]
4. [[#4. The Supply Review: Constraints, Gaps and Options]]
5. [[#5. Pre-S&OP: Reconciliation, Financials and Recommendations]]
6. [[#6. Executive S&OP and Governance]]
7. [[#7. Financial Integration of the Plan]]
8. [[#8. Scenario Planning and What-If Analysis]]
9. [[#9. S&OP Maturity: Oliver Wight Class A and a Five-Stage Ladder]]
10. [[#10. S&OP vs S&OE vs MPS: Aligning Horizons]]
11. [[#11. KPIs and Scorecard for S&OP]]
12. [[#12. S&OP Failure Modes and Remedies]]
13. [[#13. Tools: SAP IBP, o9, Kinaxis, Anaplan and Others]]
14. [[#14. ⭐ Advanced: Running an S&OP Design in a Consulting Case]]

## 📰 News box
> [!news] Shared news hook for this topic (2026): IBP has become the planning "system of record", and governance is the gap
> **Oliver Wight's IBP definition and maturity tool.** Oliver Wight describes integrated business planning as a decision-making process that aligns strategy, portfolio, demand, supply and resulting financials through a "focused and exception-driven monthly re-planning process", yielding one operating plan of **24+ months**. It offers a self-assessment of IBP maturity across four dimensions: executive decision-making, interpersonal behaviours, process design and supporting information systems. Its Class A Standard for Business Excellence is now in its **Seventh Edition** and was first created over 40 years ago. ([Oliver Wight: IBP](https://www.oliverwight-americas.com/services/integrated-business-planning-advanced-sales-operations-planning/); [Class A Standard](https://www.oliverwight-americas.com/services/class-a-standard-for-business-excellence/))
>
> **Kinaxis named Gartner Leader for the 11th year (23 March 2026).** Kinaxis said it was named a Leader in the 2026 Gartner Magic Quadrant for Supply Chain Planning Solutions for Discrete Industries and for Process Industries; its Maestro platform covers S&OP, demand planning, supply planning, inventory, production planning and scheduling. Vendor-reported. ([Kinaxis press release](https://www.kinaxis.com/en/news/press-releases/2026/kinaxis-recognized-leader-2026-gartnerr-magic-quadranttm-reports-supply))
>
> **Governance lags adoption (IDC, August 2026).** In an IDC survey of over 2,000 supply chain leaders (sponsored by Kinaxis), 98% had some AI capability but only **12%** had governance fully embedded; **67%** said accountability for AI outcomes will need significant governance changes. ([Kinaxis press release](https://www.kinaxis.com/en/news/press-releases/2026/kinaxis-sponsored-study-identifies-supply-chain-ai-accountability-gap))
>
> **SAP IBP footprint.** SAP says more than 1,000 companies use IBP, with modules for demand sensing, demand planning, supply planning, S&OP, response and supply planning, and scenario planning ("what-if analyses on demand or supply changes"). ([SAP IBP overview](https://www.sap.com/products/scm/integrated-business-planning.html); [IBP features](https://www.sap.com/products/scm/integrated-business-planning/features.html))
>
> Sub-topics that say **"See news box"** reuse these items. Vendor and sponsor statements are not independent evidence.

---
## 1. From S&OP to IBP: What and Why
> 🔴 Tier 1 · _Key points:_ One plan across demand, supply, finance; monthly, exception-driven

### Definition
**Sales and Operations Planning (S&OP)** is a monthly cross-functional process that reconciles demand and supply into one agreed operating plan, approved by executives. **Integrated Business Planning (IBP)** is the extended form: a longer horizon (24+ months), added **portfolio/product** and **strategy** inputs, explicit **financial integration** (revenue, margin, working capital, cash), scenario planning and risk, all in a single plan the leadership team owns. Typical objectives: balance demand and supply at the volume and mix level, align operational plans with the budget and strategy, surface risks early, and make trade-offs (service, cost, inventory, cash) explicit.

Why S&OP exists: functions optimise locally (sales maximise volume, manufacturing minimise cost, finance protect cash, supply chain protect service). S&OP forces the trade-off into the open and fixes it with one set of numbers. It sits between strategic planning and weekly scheduling, and feeds MPS and supply planning ([[005 Production & Operations Planning]], [[119 Supply Planning, DRP & Available-to-Promise]]). Core textbook coverage also appears in [[004 Demand Forecasting & Planning]] and [[153 Aggregate Planning Models & Workforce Strategy]].

### Example
A company's sales team commits to ₹66 crore a month, the statistical demand plan reads ₹60 crore, and manufacturing can supply ₹58 crore. Without S&OP each function plans to its own number: marketing builds for ₹66 crore, factory for ₹58 crore, finance budgets ₹66 crore. With S&OP there is one consensus (say ₹62 crore), a gap to supply of ₹4 crore handled by overtime and outsourcing, and a gap to budget of ₹4 crore flagged to executives.

### In the news
See news box. Oliver Wight's wording ("exception-driven", "24+ months", financials aligned) is the standard definition of IBP.

### Interview angle
> [!question] How it is asked
> "What is S&OP and how is IBP different?"

> [!tip] Strong answer includes
> - One plan, cross-functional, monthly, approved by executives
> - IBP: longer horizon, portfolio, financial integration, scenarios
> - Examples of conflicts it resolves (volume vs cost vs cash vs service)
> - Limits: S&OP is tactical; S&OE handles the short term

---
## 2. The Five-Step Monthly Cycle
> 🔴 Tier 1 · _Key points:_ Data, demand review, supply review, pre-S&OP, executive S&OP

### Definition
The standard APICS-style cycle has five steps over roughly 2-3 weeks:
1. **Data gathering**: actuals, forecast accuracy, inventory, backlog, capacity, financials, last month's decisions.
2. **Demand planning / demand review**: statistical baseline plus sales, marketing, finance input; assumptions (price, promotions, launches); a single **consensus demand plan** ([[118 New-Product Forecasting, Demand Sensing & Demand Shaping]]).
3. **Supply planning / supply review**: constrained supply plan against the demand plan; capacity, material, supplier and inventory targets; identify gaps and options ([[119 Supply Planning, DRP & Available-to-Promise]]).
4. **Pre-S&OP (reconciliation) meeting**: cross-functional team resolves gaps, prices scenarios, reconciles with the financial plan, prepares recommendations and unresolved decisions.
5. **Executive S&OP**: leadership reviews, decides trade-offs and approves the plan, sets guidance for the next cycle.
Outputs: signed-off demand, supply and financial plans, risks, action log. Meeting hygiene: fixed calendar, standard pack, pre-reads, decisions recorded, owners and dates.

### Example
Working-day calendar for the monthly cycle: days 1-3 data and statistical forecast; days 4-5 demand review; days 6-8 supply review; days 9-11 pre-S&OP; day 12-13 executive S&OP; day 14 plan published to ERP/APS and S&OE. Each step has a cut-off: late data does not stop the cycle; the plan is published with a flagged assumption. Output of the five steps is the one-page "plan on a page": volume, revenue, margin, inventory, service, and top 5 risks.

### In the news
See news box. IBP tools aim to keep the five steps in one data model so each meeting reads the same numbers.

### Interview angle
> [!question] How it is asked
> "Describe the S&OP process step by step. Who attends each step?"

> [!tip] Strong answer includes
> - The five steps in order with purpose and output
> - Roles: demand planner, sales/marketing, supply planner, finance, exec sponsor
> - Cadence, pre-reads, decision rights
> - What is decided where (pre-S&OP recommends, exec S&OP decides)

---
## 3. Data Gathering and the Demand Review
> 🔴 Tier 1 · _Key points:_ Baseline plus overrides, assumptions, accuracy and bias

### Definition
The **demand review** converts data into the consensus demand plan: (a) statistical forecast by product family and location; (b) overlays for promotions, launches, price moves, competitor actions, customer plans, phase-outs; (c) a review of last month's **accuracy and bias** at the planning level (WMAPE, bias, forecast value added); (d) a list of **assumptions** and **risks and opportunities**; (e) unconstrained consensus demand that is not capped by supply. Rules: the demand plan is owned by Sales/Commercial; it is not set to match supply or budget; each override has an owner and reason; the plan is expressed in units and in ₹. See [[004 Demand Forecasting & Planning]] for methods and FVA, and [[218 Forecasting with ML & Foundation Models]] for ML options.

### Example
Statistical forecast for a snacks family: 8,000 tonnes in March. Overlays: festival promotion +6% (+480), new variant launch +150, competitor price cut −3% (−240). Consensus = 8,000 + 480 + 150 − 240 = **8,390 tonnes**. Last month's accuracy: WMAPE 18%, bias +5% (over-forecast), so the planner proposes lowering the promotion uplift assumption from 6% to 4% (−160 tonnes), giving **8,230 tonnes**, and logs the reason.

### In the news
See news box. IDC's data-quality finding (62% of leaders want better data quality and integration) is the first barrier in this step.

### Interview angle
> [!question] How it is asked
> "How do you get sales and operations to agree on the demand number?"

> [!tip] Strong answer includes
> - Single consensus plan with assumptions, owner, logs
> - Use bias and FVA to challenge overrides
> - Separate forecast from target and budget
> - Escalation path for unresolved differences

---
## 4. The Supply Review: Constraints, Gaps and Options
> 🔴 Tier 1 · _Key points:_ Constrained supply plan, gap list, options with cost

### Definition
The **supply review** tests whether the consensus demand can be met: plants, suppliers, logistics, inventory targets and cash. It shows a **rough-cut capacity** view by bottleneck, material availability, inventory projection (days of cover vs target), service impact and financial effect. Output: a feasible supply plan and a **gap list** (demand not covered, capacity shortfalls, inventory excess) with options and costs. Option ladder: shift production, pre-build, overtime, extra shift, co-packer, expedite materials, alternate sourcing, demand shaping, allocation, change promise dates. Tools: RCCP and APS ([[005 Production & Operations Planning]], [[018 Capacity Management & OEE]], [[119 Supply Planning, DRP & Available-to-Promise]]).

### Example
Demand plan 105,000 units for next month; line A capacity 100,000 (OEE-adjusted); inventory 8,000 above the policy level. Gap = 5,000 units, but excess stock of 8,000 can cover it. Plan: consume 5,000 from the excess stock and produce 100,000; the excess falls from 8,000 to 3,000 units, so inventory moves towards target without extra capacity. Alternatively, a co-packer would cost ₹18 per unit more (₹90,000 for 5,000), not needed. If demand was 112,000 the stock would not cover 12,000 and the choice would be overtime (₹60 per unit extra) versus lost sales.

### In the news
See news box. Ansaldo's emphasis on end-to-end visibility is what makes such supply reviews credible rather than spreadsheet guesses.

### Interview angle
> [!question] How it is asked
> "Demand is 10% above capacity next quarter. What do you present at the supply review?"

> [!tip] Strong answer includes
> - Quantified gap by time, product and bottleneck
> - Options with cost, service and risk; recommendation
> - Inventory and cash effects
> - Which decisions need executive approval

---
## 5. Pre-S&OP: Reconciliation, Financials and Recommendations
> 🔴 Tier 1 · _Key points:_ Close gaps, link to budget, frame decisions

### Definition
The **pre-S&OP** is the mid-level meeting where the integrated reconciliation happens: confirm demand and supply plans, translate to revenue, margin and working capital, compare with the **budget/annual operating plan**, resolve what can be resolved, and frame the decisions and **scenarios** the executives must make. Standard inputs: demand and supply plans, gap list, financial reconciliation (plan vs budget), inventory and service forecast, risks and opportunities, new product status. Outputs: recommended plan, 2-3 scenarios, decisions needed, KPIs for review. Preparation matters: executives should see an agreed set of numbers, not a debate. Link: [[225 Budgeting, Variance Analysis & Balanced Scorecard]] for plan vs budget variance.

### Example
Plan vs budget (₹ crore, quarter): revenue plan 186 vs budget 198 (gap 12, −6.1%); gross margin plan 29.2% vs 30.0%; inventory projected 124 vs target 110. Recommendations: (1) accept a −₹12 crore revenue gap and recalibrate budget; (2) accelerate liquidation of aged stock (₹9 crore) to meet inventory target; (3) pursue pricing action on two SKUs with high elasticity (see [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]]) to recover ₹3 crore. The executive meeting then decides between options rather than debating basics.

### In the news
See news box. Oliver Wight cites a Marzetti CFO who says monthly reviews give visibility of gaps and how to close them within 90 minutes, which is the target for the executive session.

### Interview angle
> [!question] How it is asked
> "What happens in the pre-S&OP and why is it needed?"

> [!tip] Strong answer includes
> - Reconciliation of demand, supply, financials
> - Gap to budget and scenarios
> - Recommendation and decisions needed
> - Prevents the executive meeting becoming a working session

---
## 6. Executive S&OP and Governance
> 🔴 Tier 1 · _Key points:_ Decisions, accountability, RACI, rules of the game

### Definition
The **executive S&OP** (management business review) is a 60-90 minute decision meeting chaired by the CEO or business-unit head, attended by sales, marketing, finance, operations, supply chain, R&D/product, HR as needed. Agenda: performance vs last month, the recommended plan and scenarios, decisions, risks, and approval. Governance elements: **charter** (scope, horizon, frequency), **calendar**, **RACI**, **rules** (frozen window, change approval, escalation), **KPI scorecard**, **action log**, and the principle that the plan approved is the plan everyone executes.

| Role | Responsibility |
|---|---|
| CEO / BU head | Chairs, decides trade-offs, holds functions accountable |
| Sales / Commercial head | Owns demand plan and commitments |
| Operations / Supply head | Owns supply plan feasibility |
| Finance | Owns financial reconciliation and budget linkage |
| S&OP / IBP leader | Runs process, data and calendar, challenges assumptions |
| Planners | Prepare data, scenarios, execute decisions |
Executive absence and delegating to juniors are the main reasons S&OP degrades into a reporting meeting. Link to programme governance: [[170 Programme, Portfolio & PMO Management]].

### Example
The executive meeting reviews two scenarios: A (fund overtime, serve 100% of demand, cost ₹0.4 crore) versus B (cap supply at 95%, no overtime). The CEO selects A because the lost contribution under B (₹0.9 crore) exceeds cost; an action log records owners, dates, and a review in the next cycle. A plan change after approval needs sign-off from the same body or a defined delegate.

### In the news
See news box. IDC's 12% figure for embedded governance reflects that process rules, not tools, decide whether the cycle produces decisions.

### Interview angle
> [!question] How it is asked
> "Why do many S&OP processes fail even with good software?"

> [!tip] Strong answer includes
> - Executive ownership and decision rights
> - Calendar discipline and one set of numbers
> - Accountability for commitments and tracked actions
> - Process before technology

---
## 7. Financial Integration of the Plan
> 🔴 Tier 1 · _Key points:_ Translate units to revenue, margin, inventory, cash

### Definition
IBP's differentiator is that the operational plan is valued in money. Standard translations:
- **Revenue** = units × net price (after trade spend); **gross margin** = revenue − standard/actual cost of goods.
- **Inventory value** = projected units × cost; days of cover; **working capital** and cash impact ([[136 Supply Chain Finance & Working Capital]]).
- **Capacity and cost**: overtime, expedite, co-packing, obsolescence provisions ([[116 Inventory Valuation, Cycle Counting & Inventory Governance]]).
- **Variance to budget** and forecast of the P&L.
Finance co-owns the reconciliation; differences between volume plan and budget are explained by price, mix, volume. Link: [[108 Financial Statements & Ratios]] and [[110 Cost Accounting for Operations]]. Output: a plan that supports both the operational and board-level story.

### Example
Plan: 100,000 units a month at ₹500, variable cost ₹320, so revenue ₹5.00 crore and contribution ₹1.80 crore (₹180 per unit). Inventory at standard cost ₹320: 20,000 units of stock = ₹64 lakh. If demand falls to 90,000 and production is not cut, stock rises by 10,000 units = **₹32 lakh**, and at a 22% annual carrying cost = about **₹0.59 lakh a month**; contribution falls ₹18 lakh. These figures let finance and operations discuss a production cut versus building stock.

### In the news
See news box. Both SAP's S&OP module ("integrate financial and operational planning in one S&OP process") and Oliver Wight emphasise this link.

### Interview angle
> [!question] How it is asked
> "How does S&OP connect to finance?"

> [!tip] Strong answer includes
> - Volume to revenue, margin, inventory and cash, with one example
> - Reconciliation of plan to budget; variance categories
> - Finance as co-owner in pre-S&OP
> - Working capital and risk consequences

---
## 8. Scenario Planning and What-If Analysis
> 🔴 Tier 1 · _Key points:_ Evaluate options with numbers before deciding

### Definition
**Scenario planning** tests alternative futures or decisions on the same model: demand up/down, supplier disruption, price change, capacity addition, tariff, new product. Each scenario shows volume, service, inventory, cost and cash. A good set has a **base case**, one **upside**, one **downside**, and **decision options** (rather than many random cases); each is tied to triggers and agreed responses. Link to risk planning ([[015 Supply Chain Risk & Resilience]]) and what-if tools in Excel ([[077 Solver, Goal Seek & What-If Analysis]]). Scenario results feed the executive meeting as a comparison table and a recommended path.

### Example
Capacity 105,000 units a month; price ₹500, variable cost ₹320 (contribution ₹180).

| Scenario (₹ crore a month) | Units sold | Revenue | Contribution | Stock effect |
|---|---|---|---|---|
| Base: demand 100,000, produce 100,000 | 100,000 | 5.00 | 1.80 | none |
| Upside demand 115,000, cap at 105,000 | 105,000 | 5.25 | 1.89 | none |
| Upside, add 10,000 by overtime (extra ₹60) | 115,000 | 5.75 | 2.01 | none |
| Downside demand 90,000, production held | 90,000 | 4.50 | 1.62 | +₹32 lakh stock |

Overtime adds ₹0.12 crore (10,000 × (180 − 60)) over the capped case. Trigger rule: if orders for the first two weeks exceed plan by 8%, approve overtime for the next two weeks; if below by 8%, cut production by one shift.

### In the news
See news box. SAP IBP's scenario planning is described as running what-if analyses on demand or supply changes and comparing scenarios.

### Interview angle
> [!question] How it is asked
> "A key supplier may be disrupted next quarter. How would you use scenario planning?"

> [!tip] Strong answer includes
> - Base/upside/downside plus response options
> - Quantify service, cost, inventory, cash for each
> - Triggers and pre-agreed actions
> - Decision made by executives; revisit monthly

---
## 9. S&OP Maturity: Oliver Wight Class A and a Five-Stage Ladder
> 🔴 Tier 1 · _Key points:_ Class D to A; process, behaviour, data, technology

### Definition
Maturity models describe how an organisation's planning evolves. **Oliver Wight** classifies business-planning excellence using the **ABCD Checklist** (Class D to Class A) and the Class A Standard (now in its seventh edition per Oliver Wight's site); in popular description Class D is informal, mostly reactive planning, Class C is a basic functional process, Class B is an integrated planning process supported by management, and **Class A** is a company-wide process embedded in strategy and continuous improvement, delivering sustainable results. Oliver Wight's IBP maturity self-assessment looks at four dimensions: executive decision-making, behaviours, process design, information systems.

Practitioners often use a **five-stage ladder** (names vary by author and vendor; the labels here are a teaching version):
| Stage | Name | Hallmarks |
|---|---|---|
| 1 | Reactive | Spreadsheets, firefighting, functional silos, forecasts by sales only |
| 2 | Standard | Monthly meeting, statistical forecast, supply responds to demand |
| 3 | Integrated | Consensus demand, constrained supply, financial reconciliation, exec sign-off |
| 4 | Collaborative | Extended to customers and suppliers, scenarios, portfolio and strategy in the cycle |
| 5 | Orchestrated | Real-time, analytics and AI-assisted, automated exception handling, outcome-based governance |
Moving up needs process discipline, behaviours (trust, accountability), data and tools, in that order. Do not skip stages: tools cannot compensate for missing governance.

### Example
Diagnostic on a mid-size manufacturer: (1) monthly meeting exists but CEO attends 30% of the time, (2) forecast accuracy and bias not measured, (3) finance sees plan after approval, (4) separate spreadsheets for supply. Rating: Stage 2 with elements of Stage 1. 12-month roadmap: M1-3 set calendar and KPIs (accuracy, bias); M4-6 introduce constrained supply and finance reconciliation; M7-12 scenarios and tool selection. Success criteria are measured with KPIs (sub-topic 11), not by a score alone.

### In the news
See news box. Oliver Wight's own maturity tool and Kinaxis's September 2026 vision of "operational orchestration with agentic AI" ([Kinaxis newsroom](https://www.kinaxis.com/en/newsroom)) both sit at the top of this ladder; the IDC data show few firms are there.

### Interview angle
> [!question] How it is asked
> "How would you assess the maturity of a client's S&OP and what would you recommend?"

> [!tip] Strong answer includes
> - Diagnostic dimensions: executive behaviour, process, data, technology, KPIs
> - Maturity ladder with Class A as target and typical characteristics
> - Phased roadmap with quick wins and measurable benefits
> - Caveat: models are heuristics; business context decides the right target

---
## 10. S&OP vs S&OE vs MPS: Aligning Horizons
> 🔴 Tier 1 · _Key points:_ Months vs weeks vs days; guardrails flow down

### Definition
| Layer | Horizon | Frequency | Output | Owner |
|---|---|---|---|---|
| Strategic planning | 3-10 years | Annual | Network, capacity, portfolio | Board/CEO |
| S&OP / IBP | 3-24 months | Monthly | Aggregate demand/supply/financial plan | Executive team |
| MPS / supply planning | 1-6 months | Weekly | Item-level production and purchase plan | Planning |
| S&OE | Days to ~4 weeks | Daily/weekly | Allocation, expedite, re-promise decisions | Supply chain/Sales ops |
| Execution | Real time | Continuous | Shop-floor and logistics operations | Operations |
S&OP sets **guardrails** (volume targets, allocation rules, authorised cost of recovery, inventory limits) that S&OE uses; S&OE feeds back deviations to the next S&OP. Without S&OE, S&OP gets overloaded with short-term firefighting; without S&OP, S&OE has no direction. See [[119 Supply Planning, DRP & Available-to-Promise]] for S&OE and [[153 Aggregate Planning Models & Workforce Strategy]] for aggregate planning methods.

### Example
S&OP approves 100,000 units a month with a rule: expedite cost up to ₹3 lakh a month without escalation; allocate shortages to A customers first. During week 2, a supplier delay cuts material for 4,000 units: S&OE spends ₹1.1 lakh on air freight, allocates remaining stock by the rule and re-promises dates. The cumulative effect (4,000 units late) is reported to the next S&OP.

### In the news
See news box. Kinaxis, SAP and others market single models spanning S&OP to S&OE to keep guardrails and execution in step.

### Interview angle
> [!question] How it is asked
> "How is S&OE different from S&OP?"

> [!tip] Strong answer includes
> - Horizon, frequency, decisions and participants
> - Guardrails and feedback loop
> - Where each fits in the planning stack
> - Example of a decision at each level

---
## 11. KPIs and Scorecard for S&OP
> 🔴 Tier 1 · _Key points:_ Process, plan and outcome measures

### Definition
Measure three levels:
- **Process health**: meeting held on schedule, attendance (executive attendance), data cut-off adherence, decisions made and closed, plan changes after freeze.
- **Plan quality**: forecast accuracy (WMAPE) and **bias**, forecast value added, supply plan attainment, plan stability, gap to budget (demand, supply and financial reconciliation).
- **Business outcomes**: OTIF/fill rate, inventory days and value, expedite cost, obsolescence write-off, revenue and margin vs plan, cash-to-cash ([[012 Supply Chain Analytics & KPIs]], [[136 Supply Chain Finance & Working Capital]]).
Rules: few KPIs, owned by named people, trended, and linked to targets; avoid manufacturing "accuracy" by sandbagging (hence bias and FVA). Use a one-page scorecard in the executive pack ([[225 Budgeting, Variance Analysis & Balanced Scorecard]]).

### Example
Scorecard for a month: WMAPE (family level) 14% against target 12%; bias +4% (target ±3%); supply plan attainment 96%; OTIF 93% (target 95%); inventory days 91 (target 85); gap-to-budget revenue −3.5%; executive attendance 4 of 6. Actions: investigate +4% bias (promotion overrides), review stock days: reducing from 91 to 85 on COGS of ₹2,800 crore releases 2,800 × 6/365 = **₹46 crore** of cash.

### In the news
See news box. IDC notes 51% want clear ROI and time to value from AI, making outcome KPIs the evidence needed to keep funding.

### Interview angle
> [!question] How it is asked
> "What KPIs would you put on an S&OP dashboard?"

> [!tip] Strong answer includes
> - Process, plan, outcome KPIs
> - Bias and FVA, not only MAPE
> - Targets, owners, cadence
> - Link to money (cash released, margin protected)

---
## 12. S&OP Failure Modes and Remedies
> 🔴 Tier 1 · _Key points:_ Most failures are behavioural, not technical

### Definition
| Failure mode | Symptom | Remedy |
|---|---|---|
| No executive ownership | Delegates attend, no decisions | Exec sponsor, decision rights, attendance KPI |
| Forecast gaming | Sandbagging, optimism, "hockey stick" | Separate forecast from target, track bias, FVA |
| Supply constraints hidden | Plan is infeasible, firefighting follows | Constrained supply review with capacity data |
| Meeting without decisions | Review of past, no trade-offs | Decision-oriented agenda, scenarios, action log |
| Finance outside the loop | Plan vs budget conflict at the end | Finance co-owns reconciliation |
| Too much detail | Item-level debates | Plan at family level; exceptions only |
| Tool-first | Software without process | Fix process and data first |
| No S&OE link | Plan overridden daily | Guardrails, S&OE cadence, stability rules |
| Poor data | Arguments about numbers | Data governance ([[175 Data Quality, Master Data & Data Governance]]) |
| No continuous improvement | Same issues each month | KPIs, root cause, maturity roadmap |
Link with change management and stakeholder topics: [[040 Risk & Stakeholder Management]].

### Example
A food company's S&OP has run 18 months. Symptoms: forecast bias +11%, inventory days 98 (target 80), CEO attended 2 of 12 meetings. Diagnosis: sales forecasts inflated to secure supply, so factory builds stock; no consequence for bias. Remedy: bias in sales KPIs, exec attendance, monthly aged stock review. After 6 months: bias +3%, inventory days 86; the 12-day fall on COGS ₹1,800 crore releases 1,800 × 12/365 = **₹59 crore** (illustrative).

### In the news
See news box. IDC's finding that few firms have governance fully embedded is the contemporary version of "no executive ownership".

### Interview angle
> [!question] How it is asked
> "S&OP at this company is just a monthly meeting. What would you fix first?"

> [!tip] Strong answer includes
> - Diagnosis from symptoms: attendance, bias, decisions
> - Fix governance and behaviour before technology
> - Quick win, measurable KPI improvement
> - Sustain with calendar and accountability

---
## 13. Tools: SAP IBP, o9, Kinaxis, Anaplan and Others
> 🔴 Tier 1 · _Key points:_ Capabilities, selection criteria, implementation approach

### Definition
IBP platforms provide demand planning, supply planning, inventory optimisation, S&OP workflow, scenario simulation and integrated financial planning. Examples: **SAP IBP** (modules for demand sensing, demand planning, supply planning, S&OP, response and supply, scenario planning; see [[198 SAP IBP, APO & Demand-Driven Planning]]), **Kinaxis Maestro** (concurrent planning, scenario simulation), **o9 Solutions**, **Anaplan** (connected planning, strong in finance modelling), **Blue Yonder**, **Oracle SCM**. Selection criteria: fit to process, integration to ERP (SAP, Oracle), scalability and speed, scenario engine, financial integration, usability, total cost of ownership, vendor viability, local implementation partners. Implementation approach: design process first, pilot on a business unit, data governance, change management, adoption KPIs; tool landscape in [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]] and ERP context in [[013 ERP & Enterprise Systems (SAP-Oracle)]].

### Example
A mid-size Indian manufacturer compares three options on a weighted scorecard: process fit (30%), integration with existing ERP (20%), scenario capability (20%), cost (15%), partner availability (15%). Scores out of 5: Tool A 4/3/4/2/3, Tool B 3/5/3/4/4, Tool C 5/3/5/2/3. Weighted: A = 1.2 + 0.6 + 0.8 + 0.3 + 0.45 = **3.35**; B = 0.9 + 1.0 + 0.6 + 0.6 + 0.6 = **3.70**; C = 1.5 + 0.6 + 1.0 + 0.3 + 0.45 = **3.85**. C leads on capability but is costly; sensitivity at 25% cost weight may flip the order. STL's choice of Kinaxis Planning One via the Google Marketplace mid-market route (August 2026) shows the market's move to lighter cloud deployment.

### In the news
See news box. Gartner Leader status (11 years for Kinaxis) and SAP's 1,000+ IBP customers are vendor claims: verify with references and demos.

### Interview angle
> [!question] How it is asked
> "Which planning tool would you recommend to a mid-sized manufacturer and why?"

> [!tip] Strong answer includes
> - Process requirements first, then tool criteria
> - Integration with existing ERP
> - Pilot/phased approach with measurable benefits
> - Total cost, change management, vendor and partner capability

---
## 14. ⭐ Advanced: Running an S&OP Design in a Consulting Case
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A typical case: "Our forecast is poor, inventory is high and service is low. Fix planning." A structure that works:
1. **Clarify**: scope, KPIs, horizon, what is measured now (service, inventory days, accuracy, bias).
2. **Diagnose** with data: segment SKUs (ABC-XYZ), forecast bias by product and customer, inventory by type and age, service by channel; map the current planning process and who owns what; identify gaps against the five steps and a maturity ladder.
3. **Design** the future process: calendar, roles/RACI, demand review rules, supply review inputs, financial integration, KPIs, S&OE interface; tool requirements.
4. **Quantify the prize**: inventory days, cash, service, lost sales, expedite cost.
5. **Roadmap and risks**: pilot, governance, change management, quick wins in 90 days.
6. **Recommendation** in one page with sequencing. Use the structuring tools in [[024 Consulting Frameworks]], [[026 Case Interview — Operations Cases]] and [[162 Structured Communication - SCQA, Storylines & Case Delivery]].

### Example
FMCG company: revenue ₹4,000 crore, COGS ₹2,800 crore, inventory ₹700 crore (DIO 91 days), OTIF 88%, forecast bias +12%. Hypothesis: sales over-forecast to protect supply; factory builds stock but wrong mix. Prize: cut stock by 10% (₹70 crore) at 22% carrying cost = **₹15.4 crore a year**, plus OTIF +5 points protects revenue. Plan: (0-3 months) calendar, KPIs, bias dashboard, SKU segmentation; (3-6 months) constrained supply review, financial integration; (6-12 months) scenario tool, S&OE huddle. Risks: executive time, data, sales resistance; mitigation: sponsor, incentive tied to bias, pilot on one category first.

### In the news
See news box. Oliver Wight and IDC both place governance and behaviour ahead of technology, which supports the sequencing in this answer.

### Interview angle
> [!question] How it is asked
> "How would you set up S&OP at a company that has none?"

> [!tip] Strong answer includes
> - Diagnose, design, quantify, roadmap, risks
> - Start small: one category, simple calendar, few KPIs
> - Exec sponsorship and incentives
> - Tool selection after process design
