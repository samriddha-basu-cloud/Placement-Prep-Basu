---
tags: [operations-management, tier2]
area: Operations Management
topic: "Aggregate Planning Models & Workforce Strategy"
tier: Tier 2
roles: Operations
status: complete
subtopics: 13
---
# Aggregate Planning Models & Workforce Strategy

⬅ [[152 Learning Curves, Work Measurement & Productivity]] · [[_Index - Operations Management|Operations Management]] · [[154 Product & Service Design - QFD, DFMA & Value Engineering]] ➡

> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Aggregate Planning: Purpose, Inputs and Cost Structure]]
2. [[#2. Pure Strategies: Level, Chase and Hybrid (Mixed)]]
3. [[#3. Worked Cost Tables: Chase vs Level vs Hybrid]]
4. [[#4. Sensitivity: When the Answer Flips, and the Fire-and-Rehire Break-even]]
5. [[#5. The Transportation Method for Aggregate Planning]]
6. [[#6. Linear Programming Formulation]]
7. [[#7. Linear Decision Rule and Other Analytical Models]]
8. [[#8. Disaggregation to the MPS, Rolling Horizon and Time Fences]]
9. [[#9. Workforce Flexibility: Part-time, Shifts, Temps, Cross-training and Outsourcing]]
10. [[#10. Demand-Management Levers and Level-Strategy Support]]
11. [[#11. India: Labour Law Constraints on Workforce Strategy]]
12. [[#12. Aggregate Planning in Services: Staffing, Relief Factors and Variants]]
13. [[#13. ⭐ Advanced: Aggregate Planning in S&OP/IBP, Uncertainty and Practical Heuristics]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's labour codes and a crew-rostering failure change the workforce-planning rulebook
> **India's four Labour Codes came into force on 21 November 2025.** They subsume **29 central labour enactments** and cover wages, industrial relations, social security, and occupational safety, health and working conditions; the reforms also extend provident fund, insurance and gratuity-type benefits to gig and platform workers. In the Industrial Relations Code the threshold above which layoff, retrenchment and closure need prior government permission rises from **100 to 300 workers**, and workers must give **14 days' notice** (not exceeding 60 days) before a strike. These figures matter directly to hire-fire cost assumptions in aggregate plans. ([Wikipedia: Labour law in India](https://en.wikipedia.org/wiki/Labour_law_in_India); [Wikipedia: Industrial Relations Code, 2020](https://en.wikipedia.org/wiki/Industrial_Relations_Code,_2020)) Rule-level details (fixed-term employment, contract labour, re-skilling fund) are not confirmed by these sources; verify them against the notified rules before quoting.
>
> **IndiGo, December 2025: workforce plan with no slack.** DGCA's order on the 3-5 December disruption (2,507 flights cancelled, 1,852 delayed, over 3 lakh passengers affected) cited over-maximised use of crew, aircraft and network, rosters with minimal recovery margins and heavy dead-heading, and poor implementation of revised flight-duty-time limits. Penalty: **₹22.20 crore**. An aggregate workforce plan that ignores a changing rule on duty hours and keeps no buffer is a plan that breaks. ([The Tribune](https://www.tribuneindia.com/news/airline-operations/dgca-imposes-rs-22-20-crore-penalty-on-indigo-over-december-2025-flight-disruption))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Aggregate Planning: Purpose, Inputs and Cost Structure
> 🟠 Tier 2 · _Key points:_ Medium-term (3-18 months); family-level plan; costs of capacity changes

### Definition
**Aggregate planning (APP)** sets, for 3 to 18 months ahead, the production rate, workforce size, inventory and subcontracting that meet forecast demand at minimum cost, planning at the level of a **product family** (units, standard hours or rupees) rather than SKUs. It sits between long-range capacity decisions and the short-range master production schedule (see [[005 Production & Operations Planning]] and [[020 Operations Strategy]]); in modern companies it is the supply half of S&OP/IBP (see [[120 Integrated Business Planning (IBP) & S&OP Maturity]]).

**Inputs:** aggregate demand forecast (see [[004 Demand Forecasting & Planning]]), current workforce and inventory, capacity (regular, overtime, subcontract), policies (service level, layoffs), and a cost structure:
- **Regular-time cost** (wages and fixed benefits per period), **overtime** (premium, 1.5x to 2x), **subcontracting** (price plus quality and control risk).
- **Hiring and training cost**, **layoff/severance cost**.
- **Inventory holding cost** (capital, storage, obsolescence), **backorder or lost-sales cost** (penalty, goodwill).
- Cost of changing production rate (overtime, idle time, setup disruption).

Decision variables per period $t$: workforce $W_t$, hires $H_t$, layoffs $F_t$, regular production $P_t$, overtime $O_t$, subcontract $S_t$, inventory $I_t$, backlog $B_t$.

### Example
Running case for this note: a 6-month plan, demand 900, 1,000, 1,100, 1,500, 1,900, 1,600 (total 8,000 units). Working days 22, 19, 21, 21, 22, 20 (125 days). Each unit needs 2 labour-hours; a worker works 8 hours and is paid ₹400 an hour, so a worker produces $4 \times \text{days}$ units a month: 88, 76, 84, 84, 88, 80. Costs: regular labour effectively ₹800 per unit when fully used; overtime ₹1,200 per unit (limit 20% of regular capacity); subcontract ₹1,300 per unit; hire ₹30,000 per worker; layoff ₹40,000 per worker; holding ₹40 per unit per month; no backorders allowed; opening workforce 18, opening and closing inventory 0. Material cost is the same under every plan, so it is left out.

### In the news
See news box. The labour-code changes alter the layoff and retrenchment components of the cost structure; the IndiGo order shows the hidden cost of designing a plan with no recovery margin.

### Interview angle
> [!question] How it is asked
> "What is aggregate planning, and what trade-offs does it manage?"

> [!tip] Strong answer includes
> - Medium-term, family-level planning between strategy and MPS
> - The cost list: regular, overtime, subcontract, hire, layoff, holding, backorder
> - The core trade-off: workforce and rate stability vs inventory vs service level
> - Place in S&OP: supply plan matched to the demand plan

---

## 2. Pure Strategies: Level, Chase and Hybrid (Mixed)
> 🟠 Tier 2 · _Key points:_ Level = constant output, inventory absorbs; chase = output follows demand; mixed

### Definition
- **Level strategy:** constant production rate and workforce; inventory (or backlog) absorbs the demand swings. Good when holding cost is low, products are storable, and stable employment matters.
- **Chase strategy:** production in each period equals demand; workforce, overtime, shifts or subcontracting flex. Good when holding cost is high or products are perishable, customised or made-to-order, and workers are easy to hire and release.
- **Hybrid (mixed) strategy:** stable core workforce at a base level, plus overtime, temporary labour, subcontracting and some inventory for peaks. The usual real-world choice.

**Reactive levers (supply):** hire/fire, overtime/undertime, part-time and temps, subcontracting, inventory, backlog. **Demand levers:** price, promotion, advertising, complementary products and counter-seasonal items (see sub-topic 10). In services, inventory is not available, so chase and demand management dominate (sub-topic 12).

### Example
Using the running case, the strategies to compare are: (i) **chase**, hire/fire to exactly the monthly requirement; (ii) **level**, constant 16 workers that produce 8,000 units over six months; (iii) **hybrid**, 15 workers plus overtime; (iv) **retain 18** workers (no layoffs). Detailed numbers are in sub-topic 3. A quick qualitative preview: chase pays the most in hiring and layoffs, level pays in holding, hybrid pays overtime premium but holds less stock, and retaining everyone pays idle wages.

### In the news
See news box. Larger layoff thresholds under the Industrial Relations Code make a chase strategy easier on paper for big employers, but contract and statutory obligations still apply (sub-topic 11).

### Interview angle
> [!question] How it is asked
> "Would you use a level or chase strategy for a seasonal packaged-food manufacturer?"

> [!tip] Strong answer includes
> - Product shelf-life, holding cost and demand predictability decide the mix
> - Cost comparison framework, not a slogan
> - Core workforce plus temps and a pre-season build (hybrid)
> - Capacity, labour-market and policy constraints

---

## 3. Worked Cost Tables: Chase vs Level vs Hybrid
> 🟠 Tier 2 · _Key points:_ Month-by-month table; total cost; compare strategies

### Definition
A **cost table** lists, for each month, demand, production, workforce changes and the cost components, then totals them. Steps: (1) convert demand to workers needed ($\lceil D_t/\text{units per worker}_t \rceil$); (2) compute hire/layoff counts from the opening workforce; (3) compute labour, overtime and subcontract costs; (4) roll forward inventory $I_t = I_{t-1} + P_t - D_t$ and cost it. Always check that opening and closing balances reconcile, and state assumptions.

### Example
Running case. Units per worker per month 88, 76, 84, 84, 88, 80; monthly pay per worker ₹70,400, 60,800, 67,200, 67,200, 70,400, 64,000.

**Chase:** workers needed = ceil(demand / units per worker) = 11, 14, 14, 18, 22, 20. Changes from the opening 18: −7, +3, 0, +4, +4, −2, so **11 hires and 9 layoffs**. Labour $= ₹66,04,800$; hiring $11 \times 30{,}000 = ₹3{,}30{,}000$; layoffs $9 \times 40{,}000 = ₹3{,}60{,}000$. Total **₹72,94,800**, no inventory.

**Level (16 workers):** production 1,408, 1,216, 1,344, 1,344, 1,408, 1,280 (8,000 total). Month-end inventory: 508, 724, 968, 812, 320, 0. Holding $= (508 + 724 + 968 + 812 + 320) \times 40 = 3{,}332 \times 40 = ₹1{,}33{,}280$. Labour: a worker's six-month pay is $70{,}400 + 60{,}800 + 67{,}200 + 67{,}200 + 70{,}400 + 64{,}000 = ₹4{,}00{,}000$, so $16 \times 4{,}00{,}000 = ₹64{,}00{,}000$; layoff of 2 workers $= ₹80{,}000$. Total **₹66,13,280**.

**Hybrid (15 workers + overtime):** production 1,320, 1,140, 1,260, 1,260, 1,320, 1,200 on regular time, plus overtime of 260 units in May and 240 in June (500 units at ₹1,200). Labour $= ₹60{,}00{,}000$; layoffs of 3 $= ₹1{,}20{,}000$; overtime $= 500 \times 1{,}200 = ₹6{,}00{,}000$; holding (420 + 560 + 720 + 480 + 160 = 2,340 unit-months) $= ₹93{,}600$. Total **₹68,13,600**.

**Retain 18 workers:** labour ₹72,00,000, holding ₹46,080, total **₹72,46,080**.

| Strategy | Labour | Hire/layoff | Subcontract/OT | Holding | Total (₹) |
|---|---|---|---|---|---|
| Chase | 66,04,800 | 6,90,000 | 0 | 0 | 72,94,800 |
| Level 16 | 64,00,000 | 80,000 | 0 | 1,33,280 | 66,13,280 |
| Hybrid 15 + overtime | 60,00,000 | 1,20,000 | 6,00,000 | 93,600 | 68,13,600 |
| Retain 18 | 72,00,000 | 0 | 0 | 46,080 | 72,46,080 |

In this data the **level plan is cheapest (₹66.13 lakh)**, 9% below chase. Reason: hiring and layoff cost (₹70,000 per cycle) is high compared with holding at ₹40 per unit-month. The free LP optimum (integer workers, overtime and subcontracting allowed) is the same level-16 plan: ₹66,13,280. The cheapest hybrid with a constant 15 workers costs ₹68.14 lakh, and with 14 workers (overtime plus 256 subcontracted units) ₹70.52 lakh: shrinking the core below 16 does not pay at these prices.

### In the news
See news box. In 2025-26 labour-code rollout, a chase plan's layoff costs must be re-checked for compliance (notice, compensation, re-skilling), so hire-fire costs in the model need an update.

### Interview angle
> [!question] How it is asked
> "Given this demand and cost data, compare chase and level strategies and recommend one."

> [!tip] Strong answer includes
> - A clean table with every cost line and a reconciled inventory
> - The reason one wins (cost structure), plus the sensitivities
> - Non-cost factors: service level, morale, skill retention, capacity ceilings
> - A hybrid recommendation when pure strategies leave gaps

---

## 4. Sensitivity: When the Answer Flips, and the Fire-and-Rehire Break-even
> 🟠 Tier 2 · _Key points:_ Holding cost vs hire-fire cost; break-even idle time; shadow price

### Definition
Aggregate plans are decisions about **cost ratios**. Two useful rules of thumb:
- **Fire-and-rehire break-even:** if a trough in demand would leave a worker idle for $k$ months, laying off and rehiring pays only when
$$k \times \text{monthly wage} > \text{layoff cost} + \text{hiring cost}$$
- **Inventory vs capacity:** building stock early pays if holding cost over the months stored is less than the cost of the extra capacity (overtime premium, subcontract premium, or hire-fire) it avoids.
Run the model at several parameter values (holding, subcontract price, overtime premium) and watch when the optimal workforce path changes. A large drop in holding cost (e.g. cheaper warehouse space) favours level; short shelf-life, fashion risk, or high capital cost favours chase.

### Example
Average monthly wage per worker in the case $= ₹64{,}00{,}000/16/6 = ₹66{,}667$. Hire plus layoff $= 30{,}000 + 40{,}000 = ₹70{,}000$, so the break-even is $70{,}000/66{,}667 = 1.05$ months: lay off only if the trough lasts more than about a month (and legally can).

Re-running the optimisation with higher holding cost (everything else the same):

| Holding cost (₹/unit-month) | Optimal total (₹) | Workforce path (6 months) | Overtime (units) |
|---|---|---|---|
| 40 | 66,13,280 | 16 constant | 0 |
| 150 | 69,40,200 | 13, 13, 13, 17, 20, 20 | 0 |
| 300 | 70,03,200 | 12, 12, 12, 19, 20, 20 | 68 |
| 600 | 70,48,800 | 12, 12, 13, 18, 20, 20 | 136 |

As holding cost rises 15 times, the plan moves from a flat 16 workers to a strong seasonal ramp (12 to 20), but the cost never reaches the pure chase plan (₹72.95 lakh), because the optimiser still avoids needless hiring and layoffs and uses a little overtime. This is the typical result: **the optimum is a hybrid whose shape depends on cost ratios**.

### In the news
See news box. Changes in retrenchment cost (compensation, notice, re-skilling contributions) increase the "layoff" parameter; the table shows what that does to the workforce path.

### Interview angle
> [!question] How it is asked
> "Under what cost conditions would you switch from level to chase?"

> [!tip] Strong answer includes
> - Break-even logic between hire-fire and idle wages, with a number
> - Cost ratio explanation (holding vs rate-change cost)
> - A sensitivity table or two scenarios, not only a base case
> - Non-cost: skill loss, quality, labour relations

---

## 5. The Transportation Method for Aggregate Planning
> 🟠 Tier 2 · _Key points:_ Sources = capacity by period/mode; destinations = demand; cost matrix includes holding

### Definition
When costs are linear and workforce is fixed, aggregate planning becomes a **transportation problem** (see [[147 Operations Research - Transportation, Assignment & Transshipment]]). Rows (sources) are capacity types by production period (regular, overtime, subcontract), columns (destinations) are demand periods, and each cell cost equals the unit production cost plus holding cost for every month the unit is carried: $c_{ij} = c_i + h\,(j - t_i)$ for $j \ge t_i$. Add a dummy column for unused capacity (cost 0). Backorder cells can be added with penalty cost for $j < t_i$. The solution (e.g. by Vogel's method plus MODI, or Solver) gives the optimal production and inventory path.

### Example
Three months, demand 500, 700, 950. Per month: regular capacity 600 at ₹800, overtime capacity 100 at ₹1,200, subcontract 150 at ₹1,300; holding ₹40 per unit-month; no backorders. Cost matrix for a month-1 unit: delivered in M1: regular 800 (OT 1,200; sub 1,300); delivered in M2: 840 (OT 1,240; sub 1,340); in M3: 880 (1,280; 1,380).

Optimal allocation (verified by LP):

| Source | To M1 | To M2 | To M3 |
|---|---|---|---|
| Regular M1 | 500 | 100 | |
| Overtime M1 | | 100 | |
| Regular M2 | | 400 | 200 |
| Overtime M2 | | 100 | |
| Regular M3 | | | 600 |
| Overtime M3 | | | 100 |
| Subcontract M3 | | | 50 |

Cost $= 500(800) + 100(840) + 100(1240) + 400(800) + 200(840) + 100(1200) + 600(800) + 100(1200) + 50(1300) = ₹18{,}81{,}000$. Demand check: M1 = 500; M2 = 100 + 100 + 400 + 100 = 700; M3 = 200 + 600 + 100 + 50 = 950. Logic: regular capacity is fully used every month and carried forward at ₹40 per month when it is cheaper than overtime in the later month; subcontracting is the last resort, only 50 units in M3.

### In the news
See news box. This formulation is how a shop floor would test a legal constraint such as an overtime cap: reduce the overtime-capacity entries and re-solve.

### Interview angle
> [!question] How it is asked
> "Set up the transportation tableau for a 3-month aggregate plan and explain the cell costs."

> [!tip] Strong answer includes
> - Rows, columns, dummy column and cost $=$ production $+$ holding $\times$ months carried
> - Infeasible cells (no producing for past demand unless backorder)
> - Method (VAM/MODI or Solver) and a sanity check on supply and demand balance
> - Limits: fixed workforce, linear costs, no hire/fire decisions

---

## 6. Linear Programming Formulation
> 🟠 Tier 2 · _Key points:_ Objective, balance constraints, capacity constraints, hire/layoff flow

### Definition
The general LP (extending the transportation form to hiring and layoffs; see [[146 Operations Research - Linear Programming]]) for $T$ periods:

$$\min \sum_{t=1}^{T} \left( w_t W_t + h\,H_t + f\,F_t + c_o O_t + c_s S_t + i\, I_t + b\, B_t \right)$$
subject to:
$$W_t = W_{t-1} + H_t - F_t, \qquad P_t \le u_t W_t, \qquad O_t \le \alpha\, u_t W_t$$
$$I_t - B_t = I_{t-1} - B_{t-1} + P_t + O_t + S_t - D_t$$
with $W_t, H_t, F_t \ge 0$ (integers if workers are counted as whole persons), $B_T = 0$, and $I_0, B_0, W_0$ given. Use $\alpha$ for the overtime limit, $u_t$ for units per worker in month $t$, $w_t$ for monthly pay per worker. Policy constraints (minimum workforce, maximum change per month, safety stock) are added as extra inequalities. The same model can be solved with Excel Solver ([[077 Solver, Goal Seek & What-If Analysis]]) or PuLP ([[068 Operations-Specific Python (PuLP, SimPy)]]).

### Example
Python (PuLP) skeleton for the running case:

```python
import pulp
D=[900,1000,1100,1500,1900,1600]; days=[22,19,21,21,22,20]
u=[4*d for d in days]; pay=[3200*d for d in days]   # Rs 400/hr x 8 h
m=pulp.LpProblem("aggregate", pulp.LpMinimize); T=range(6)
W=pulp.LpVariable.dicts("W",T,0,cat="Integer"); H=pulp.LpVariable.dicts("H",T,0,cat="Integer")
F=pulp.LpVariable.dicts("F",T,0,cat="Integer"); P=pulp.LpVariable.dicts("P",T,0)
O=pulp.LpVariable.dicts("O",T,0); S=pulp.LpVariable.dicts("S",T,0); I=pulp.LpVariable.dicts("I",T,0)
m += pulp.lpSum(pay[t]*W[t]+30000*H[t]+40000*F[t]+1200*O[t]+1300*S[t]+40*I[t] for t in T)
for t in T:
    m += W[t] == (18 if t==0 else W[t-1]) + H[t] - F[t]
    m += P[t] <= u[t]*W[t]; m += O[t] <= 0.2*u[t]*W[t]
    m += I[t] == (0 if t==0 else I[t-1]) + P[t]+O[t]+S[t]-D[t]
m += I[5] == 0
m.solve(pulp.PULP_CBC_CMD(msg=0)); print(pulp.value(m.objective))
```
With subcontracting costed at ₹1,300 (as in the transportation example) the optimum for the running case with ₹40 holding is the level-16 plan at ₹66.13 lakh: the solver confirms the hand table's winner. Integer workers cause tiny differences from a fractional LP.

### In the news
See news box. LP/MILP workforce models underpin airline crew rostering; the IndiGo case reflects a rostering model that did not include the new duty-time rule and lacked recovery slack.

### Interview angle
> [!question] How it is asked
> "Formulate aggregate planning as an LP. What are the decision variables, objective and constraints?"

> [!tip] Strong answer includes
> - Decision variables and the three balance constraints (workforce, capacity, inventory)
> - Objective with all cost terms and the integrality remark
> - Extra policy constraints (overtime cap, workforce change limits)
> - Tools (Solver, PuLP) and sensitivity analysis on cost parameters

---

## 7. Linear Decision Rule and Other Analytical Models
> 🟠 Tier 2 · _Key points:_ HMMS (1960); quadratic cost; management coefficients; search rules

### Definition
Holt, Modigliani, Muth and Simon (HMMS, 1960) modelled a paint-factory plan with **quadratic cost functions** (hiring/layoff, overtime, inventory), which makes the optimal decisions **linear** in demand forecasts and current state: this is the **Linear Decision Rule (LDR)**.

$$P_t = \sum_{k=0}^{N} a_k\, D_{t+k} + b\, W_{t-1} + c\, I_{t-1} + d, \qquad W_t = e\,W_{t-1} + \sum_{k} g_k\, D_{t+k} + \dots$$
Production responds to the weighted sum of present and future forecasts (weights decline with horizon), to the workforce already in place and to inventory (stock above target reduces output). Features: smooth rates, easy to compute once the coefficients are known, but relies on a quadratic cost fit and a single product.

Other approaches:
- **Management coefficients model** (Bowman, 1963): regress past managers' decisions on demand, workforce and inventory to capture good judgment.
- **Search decision rules** and **simulation** for non-linear costs.
- **Stochastic programming / robust optimisation** when demand is uncertain, with scenarios and recourse (hire later, overtime, subcontract).
- **Heuristics and spreadsheet "what-if"** remain most common in practice.

### Example
Illustrative (non-HMMS) rule of the same form: $P_t = 0.6\,D_t + 0.3\,D_{t+1} + 0.1\,D_{t+2} + 0.5\,(I^* - I_{t-1})$ with target inventory $I^* = 300$. If $D_t, D_{t+1}, D_{t+2} = 1{,}000, 1{,}200, 1{,}500$ and $I_{t-1} = 200$: $P_t = 600 + 360 + 150 + 50 = 1{,}160$. Production leans towards the future (1,160 vs 1,000 this month's demand), smoothing the ramp. The coefficients here are assumed for illustration; HMMS derives them from cost parameters.

### In the news
No dedicated news hook; LDR is a classical result. See news box for the modern pressures (labour rules, rostering) that such a smooth-rate model would have to include as constraints.

### Interview angle
> [!question] How it is asked
> "What is the linear decision rule and why is it rarely used in practice?"

> [!tip] Strong answer includes
> - HMMS quadratic costs lead to linear rules for production and workforce
> - What the rule responds to: forecasts, workforce, inventory
> - Why not used: single product, quadratic cost fit, coefficient estimation, no integer/policy constraints
> - What is used today: LP/MILP, simulation and S&OP processes

---

## 8. Disaggregation to the MPS, Rolling Horizon and Time Fences
> 🟠 Tier 2 · _Key points:_ Family to SKU; run-out time; rolling plan; freeze windows

### Definition
The aggregate plan is **disaggregated** into the **master production schedule (MPS)** by item, week and line (see [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]], [[081 SAP PP — Production Planning]] and [[119 Supply Planning, DRP & Available-to-Promise]]). Methods:
- **Percentage/mix splits** from historical shares.
- **Run-out time method:** allocate the family quantity so that every item has the same run-out time (months of supply), preventing stock-outs of fast movers.
- **Cut-and-fit** and optimisation with changeover and lot-size constraints.

The plan is revised on a **rolling horizon**: each month, update forecasts and actuals, commit the near months, re-plan the rest. **Time fences** (demand, planning, freeze) regulate how much change is allowed near-term: the closer to execution, the costlier a change. The capacity check at this level is **rough-cut capacity planning (RCCP)** against bottleneck resources, before detailed MRP/CRP.

### Example
Family production this month: 1,400 units. On-hand: A 400, B 150, C 90 (total 640); monthly demand: A 700, B 420, C 280 (1,400). Family run-out time $= (640 + 1{,}400)/1{,}400 = 1.457$ months. Allocate $p_i = 1.457 \times d_i - I_i$:

| Item | On hand | Demand | Run-out target | Production |
|---|---|---|---|---|
| A | 400 | 700 | 1.457 | 620 |
| B | 150 | 420 | 1.457 | 462 |
| C | 90 | 280 | 1.457 | 318 |

Total 1,400 ✓. A plain 50/30/20 mix split would produce 700, 420 and 280, leaving end stocks of 400, 150 and 90 units, i.e. 0.57, 0.36 and 0.32 months of supply, so C is most likely to stock out. The run-out method leaves 320, 192 and 128 units, equal to 0.457 months for every item.

### In the news
See news box. After a rule or demand shock, rolling re-planning with freeze windows is how plants absorb change without whiplash (compare the bullwhip discussion in [[114 Bullwhip Effect, Beer Game & Information Sharing]]).

### Interview angle
> [!question] How it is asked
> "How do you convert an aggregate plan into a master schedule?"

> [!tip] Strong answer includes
> - Disaggregation methods, with run-out time as a numeric example
> - RCCP validation against the bottleneck
> - Rolling horizon and time fences to control nervousness
> - Feedback to S&OP if the disaggregated plan is infeasible

---

## 9. Workforce Flexibility: Part-time, Shifts, Temps, Cross-training and Outsourcing
> 🟠 Tier 2 · _Key points:_ Numerical vs functional flexibility; core-periphery; cost vs commitment

### Definition
**Numerical flexibility:** change headcount or hours quickly: part-time, temporary and contract workers, **annualised hours**, **flexi-shifts** (extra shift, weekend shift), overtime banks, outsourcing, and **gig/platform labour**. **Functional flexibility:** cross-trained multi-skilled workers who can move between tasks, boosting capacity at bottlenecks (see [[007 Lean Manufacturing]], [[006 Manufacturing Systems]]). **Financial flexibility:** pay linked to output or profit.

Design as **core-periphery**: a stable core for skills and knowledge, a flexible periphery for peaks. Trade-offs: temps and contract labour cost less in commitment but have a learning curve (see [[152 Learning Curves, Work Measurement & Productivity]]), higher error rates and legal exposure; outsourcing transfers capacity risk but adds supplier risk (see [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]]); overtime is fast but raises fatigue and accident risk and has statutory caps. Compare options on **cost per productive hour** including training, supervision and quality cost.

### Example
Peak requirement: 2,000 extra labour-hours over two months. Option A, overtime at 1.5x on ₹400: ₹600 per hour, with a 15% productivity loss from fatigue, so effective ₹706 per productive hour: ₹14.1 lakh. Option B, temporary workers at ₹350 per hour plus 100 hours of training and supervision at ₹400 per hour (₹40,000) and 20% lower productivity in the first month (average 10% over two months): $2{,}000 \times 350/0.9 + 40{,}000 = ₹8.18$ lakh. Option C, subcontract at ₹520 per hour: ₹10.4 lakh. Temps are cheapest here, but quality and ramp-up risk must be priced; overtime is the quick option.

### In the news
See news box. The Code on Social Security's extension of benefits to gig and platform workers changes the cost of the "gig" lever; fixed-term and contract rules need to be checked before building a plan around them (sub-topic 11).

### Interview angle
> [!question] How it is asked
> "Peak demand in Q3 is 30% above normal. What workforce options do you consider, and how do you choose?"

> [!tip] Strong answer includes
> - Numerical vs functional flexibility, core-periphery model
> - Cost per productive hour, including training, quality and legal obligations
> - Lead time for each option and ability to scale back
> - Retention of core skills and avoiding overtime fatigue

---

## 10. Demand-Management Levers and Level-Strategy Support
> 🟠 Tier 2 · _Key points:_ Price, promotion, backlog, counter-seasonal products, reservations

### Definition
Aggregate planning is not only about capacity: demand can be reshaped to fit.
- **Pricing and promotion:** off-peak discounts, festive-season pricing, advance-booking incentives.
- **Backlog and lead-time quotation:** quote longer delivery in peak periods (acceptable for customised goods).
- **Counter-seasonal products and complementary lines:** fans and heaters, ice-cream and soup, gas and electric water-heaters.
- **Reservation and appointment systems** in services; **dynamic pricing** (see [[151 Service Operations Management]]).
- **Order promising (ATP/CTP)** to protect capacity for priority customers (see [[119 Supply Planning, DRP & Available-to-Promise]]).
- **Make-to-order vs make-to-stock** positioning to decide where the demand-supply buffer sits ([[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]).

The logic: a rupee of discount to move 1 unit of demand from a peak to a trough is worth it if it saves more than a rupee of capacity cost (overtime premium, holding cost) per unit moved.

### Example
Peak month demand 1,900 against regular capacity 1,760 (20 workers). Overtime for 140 units costs a premium of $140 \times 400 = ₹56{,}000$. A pre-booking discount of ₹100 on 140 units shifted to the previous month costs ₹14,000 plus holding 140 units for one month at ₹40 = ₹5,600: ₹19,600 in total, saving about ₹36,400. If the discount must apply to 600 units to move 140 units (as in most promotions), cost $= 600 \times 100 = ₹60{,}000$ and the lever is not worth it: promotions must be targeted at price-sensitive demand.

### In the news
See news box. IRCTC's Tatkal rules (Aadhaar OTP, agent window) are demand management of a different kind: they ration access to scarce capacity (see the news box in [[151 Service Operations Management]]).

### Interview angle
> [!question] How it is asked
> "Capacity is 20% short in festival season. Besides hiring, what else can you do?"

> [!tip] Strong answer includes
> - Demand shaping (price, advance booking, lead-time quote) and product-mix levers
> - Compare lever cost vs capacity cost, and the cannibalisation risk
> - Segment customers (priority vs deferrable)
> - Measure results and adjust the next plan

---

## 11. India: Labour Law Constraints on Workforce Strategy
> 🟠 Tier 2 · _Key points:_ ID Act retrenchment; contract labour; fixed-term; new codes from 21 Nov 2025

### Definition
Hiring and firing in India are shaped by statute. Pre-code framework (Industrial Disputes Act, 1947): **retrenchment** (Section 25F) requires one month's notice (or pay in lieu), compensation of **15 days' average pay for every completed year of service**, and notice to the government; **Chapter V-B** required prior government permission for layoff, retrenchment or closure in establishments with 100 or more workers; the **Contract Labour (Regulation and Abolition) Act, 1970** restricted contract labour in core, perennial work in covered establishments. The **Factories Act, 1948** set daily and weekly hour limits and overtime at double rate.

**Labour codes (in force 21 November 2025):** the Industrial Relations Code raises the permission threshold from 100 to **300 workers** (verified in sources cited in the news box) and requires 14 days' strike notice. Features usually cited from the codes as enacted, to be verified against the final notified rules before quoting: recognition of **fixed-term employment** with pro-rata benefits (gratuity after one year under the Social Security Code), a **worker re-skilling fund** funded by the employer on retrenchment, applicability of contract-labour provisions only to establishments above a higher worker threshold (50 under the OSH Code), and a general prohibition on contract labour in core activities with listed exceptions. State rules and wage-ceiling details matter, so a plan must carry a compliance check per state and per establishment size.

Implication for aggregate planning: the **layoff parameter in the cost model is not a pure cost, it is also a constraint and a time delay**; for large units, a chase strategy has legal and reputational friction, so most Indian manufacturers use hybrid plans with a stable permanent core and contract or fixed-term labour for peaks, subject to the codes.

### Example
Cost model update. A plant with 250 workers (above the old 100-worker permission threshold, below the new 300) wants to lay off 25 workers (10%) after a demand fall. Average monthly pay ₹30,000 (daily ₹1,000 on a 30-day basis): statutory retrenchment compensation (15 days per year) for an average 8 years of service $= 8 \times 15 \times 1{,}000 = ₹1{,}20{,}000$ per worker, plus one month's notice pay ₹30,000: ₹1.5 lakh. For 25 workers, ₹37.5 lakh. The aggregate-plan layoff parameter should therefore be about ₹1.5 lakh per worker (not ₹40,000), which changes the break-even in sub-topic 4: $1.5 \text{ lakh} + \text{hiring} 30{,}000 = ₹1.8$ lakh vs monthly wage 30,000: break-even idleness is 6 months. Under that cost, and with notice and union processes on top, the plan will nearly always keep workers and use overtime, temps or subcontracting. (Illustrative figures, not company data.)

### In the news
See news box for the 21 November 2025 date and the 300-worker threshold; confirm all other numbers with the current text and state rules.

### Interview angle
> [!question] How it is asked
> "Your plant must cut capacity by 15% for six months. Why can't you simply retrench, and what options do you have?"

> [!tip] Strong answer includes
> - Retrenchment rules (notice, compensation, permission threshold, now 300 workers) and union relations
> - Alternatives: stop overtime and temps first, redeploy and cross-train, shorten the week, voluntary retirement scheme, inventory build
> - Cost-model adjustment: layoff cost as a high parameter
> - A verification step: current state rules and the status of codes

---

## 12. Aggregate Planning in Services: Staffing, Relief Factors and Variants
> 🟠 Tier 2 · _Key points:_ No inventory; chase with part-time; shift scheduling; relief factor

### Definition
Services cannot hold finished inventory, so APP turns into **staffing and capacity planning**: decide the workforce level and mix (full-time, part-time, flex) and the shift pattern against forecast hourly or daily demand (call centres, hospitals, airlines, retail). Tools:
- **Workload to headcount conversion:** required staff $=$ workload (hours) / productive hours per person.
- **Relief factor (coverage ratio):** converts "posts" into staff when leave, weekly offs and absence exist.
- **Shift scheduling and rostering:** cyclic roster, split shifts, annualised hours, weekly-off rotation; heuristics or integer programming (see [[021 Scheduling & Sequencing]]).
- **Demand levers:** appointments, reservations, price and capacity pooling.
- **Yield management** for perishable capacity (see [[151 Service Operations Management]]).
The stakes are asymmetric: understaffing creates queues and abandonment (see [[149 Queueing Theory & Waiting-Line Analysis]]), overstaffing wastes wages, and rosters must respect duty-time and rest rules (the IndiGo lesson).

### Example
A ward needs one post staffed 24x7 at a 1:6 nurse-patient ratio. Census by shift: 40, 52, 66 patients $\to$ 7, 9 and 11 nurses (ceil of patients/6). Coverage: a 24x7 post needs 168 hours a week; a nurse works 40 hours, so one post needs $168/40 = 4.2$ nurses; with 15% leave and absence the relief factor gives $4.2/0.85 = 4.94$ nurses per post. For the 9-nurse day shift: $9 \times 4.94 \approx 44$ nurses on the roster if every shift is staffed equally. Part-time nurses covering evening peaks change the mix and cost.

### In the news
See news box. IndiGo's roster, designed with minimal recovery margins and dead-heading, is a services-workforce plan with a missing coverage buffer; the regulator's order effectively imposed one.

### Interview angle
> [!question] How it is asked
> "How would you plan staffing for a 24x7 customer support centre with a peak at 6 pm?"

> [!tip] Strong answer includes
> - Convert call volume to workload (Erlang-type sizing), then to headcount with shrinkage
> - Relief factor, shift pattern and part-timers for the peak
> - Cross-training and overflow routing; metrics: service level, occupancy, abandonment
> - Compliance with rest rules and fatigue limits

---

## 13. ⭐ Advanced: Aggregate Planning in S&OP/IBP, Uncertainty and Practical Heuristics
> ⭐ Advanced · _Added beyond the tracker_

### Definition
In practice the aggregate plan is a **monthly S&OP/IBP cycle** step: demand review, supply review (capacity, constraints, scenarios), financial reconciliation, executive decision (see [[120 Integrated Business Planning (IBP) & S&OP Maturity]], [[198 SAP IBP, APO & Demand-Driven Planning]]). Advanced considerations:
- **Uncertainty:** plan against **scenarios** (base, high, low); commit a core capacity and **option contracts** (flexible labour, subcontract capacity, reservation fees) for upside. Use **chance constraints** (service probability) or **robust** models; protect with safety capacity rather than only safety stock.
- **Bottleneck-based planning:** use the theory of constraints; plan aggregate capacity at the bottleneck (see [[018 Capacity Management & OEE]]).
- **Multi-site and network:** allocate volume across plants (see [[113 Network Design & Facility Location Modelling]]).
- **Learning and ramp-up:** new-line capacity should follow the learning curve, not nameplate.
- **KPIs:** plan adherence, forecast bias, schedule stability (frozen-window changes), overtime %, labour utilisation, capacity utilisation, cost per unit and OTIF.

### Example
A plant faces demand scenarios in Q3 of 1,500 (low), 1,800 (base), 2,100 (high) units a month, probabilities 25%, 50%, 25%. Plan A: core capacity 1,800, with 300 units of subcontract options at ₹1,300. Plan B: capacity 2,100 at ₹800 regular cost, with idle cost for unused units at ₹300. Expected extra cost over the cost of producing the actual demand at regular rates: Plan A pays the subcontract premium only in the high case, $0.25 \times 300 \times (1{,}300 - 800) = ₹37{,}500$, and carries 300 idle units in the low case, $0.25 \times 300 \times 300 = ₹22{,}500$: total ₹60,000. Plan B carries idle capacity of 600 units in the low case ($0.25 \times 600 \times 300 = ₹45{,}000$) and 300 in the base case ($0.5 \times 300 \times 300 = ₹45{,}000$): ₹90,000. Plan A (core plus options) is cheaper by ₹30,000; the advantage grows as the idle cost rises or the high-demand probability falls.

### In the news
See news box. The two 2025 developments, a rule change in India's labour framework and the DGCA's finding on buffers, point to the same advanced message: build rule-change and disruption scenarios into the plan, and keep a deliberate capacity cushion.

### Interview angle
> [!question] How it is asked
> "How would you plan capacity when demand is uncertain and labour is hard to flex?"

> [!tip] Strong answer includes
> - Scenario planning with a core-plus-flex capacity structure
> - Option value arithmetic (premium paid only in the high case)
> - Bottleneck focus and S&OP governance
> - KPIs and trigger points for activating flex capacity
