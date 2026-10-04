---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Network Design & Facility Location Modelling"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 13
---
# Network Design & Facility Location Modelling

⬅ [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[114 Bullwhip Effect, Beer Game & Information Sharing]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. Network Design Decisions and Scope]]
2. [[#2. Warehouse Count vs Cost vs Service]]
3. [[#3. Square-Root Law of Inventory Consolidation]]
4. [[#4. Centre-of-Gravity Method]]
5. [[#5. Weighted Scoring and Factor Rating]]
6. [[#6. The p-Median Problem]]
7. [[#7. Capacitated Facility Location (MILP)]]
8. [[#8. Hub-and-Spoke vs Point-to-Point]]
9. [[#9. DC Consolidation: Cost, Service and GST in India]]
10. [[#10. Coverage and Service-Constrained Design]]
11. [[#11. Tools, Data and Modelling Workflow]]
12. [[#12. Case: Redesigning a Pan-India Distribution Network]]
13. [[#13. ⭐ Advanced: Robust, Multi-Echelon and Dynamic Network Design]]

## 📰 News box
> [!news] Shared news hook for this topic (2017–2026): tax and tariff rules redraw warehouse maps
> **GST and the end of "a warehouse in every state" (from 1 July 2017).** GST replaced a stack of state-level taxes (including octroi and check-post regimes) with one national tax; Wikipedia's summary of government claims is that removing interstate checkposts cut truck travel time on interstate movement by about **20%**, and the e-way bill became mandatory for interstate consignments above ₹50,000 from **1 June 2018** (validity one day per 200 km). Firms that had kept a depot in each state to avoid inter-state sales tax could consolidate into fewer, larger regional hubs. ([Wikipedia: GST India](https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)); the 20% figure is a government claim, not an independent measurement)
>
> **GST rate rationalisation (announced 3 September 2025, effective 22 September 2025).** The six-slab structure was simplified to **5%** and **18%**, plus **40%** on a short list of luxury and sin goods, with the 12% and 28% slabs removed; the government projected a net revenue loss of about ₹480 billion. Rate changes alter landed-cost comparisons for products that were taxed differently, so network cost models need refreshing. ([Wikipedia: GST India](https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)))
>
> **Lead times differ sharply even within one segment (Netstock survey, reported 1 October 2026).** In a survey of 150+ small-business customers, supplier lead-time swings were the top inventory-planning pressure (29%), with 77% citing lead-time challenges in some form; average lead times ran from **21 days** for the fastest-moving businesses to **79 days** for the slowest. Long, variable inbound lead times push networks toward more buffer stock and more nodes. ([Supply Chain Dive](https://www.supplychaindive.com/news/beyond-tariffs-a-storm-of-pressures-is-hampering-smb-supply-chains/831880/))
>
> **Gartner Top 25 (17 June 2026).** Gartner's summary of what distinguishes leaders includes "investing in network-centric strategies". ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-06-17-gartner-announces-2026-rankings-of-the-global-supply-chain-top-25))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Network Design Decisions and Scope
> 🔴 Tier 1 · _Key points:_ how many, where, what size, what role; strategic vs tactical; cost-service trade-off

### Definition
**Supply chain network design** decides the structure of the physical chain: the **number, location, capacity and role** of plants, warehouses/DCs, cross-docks and ports, which **products and customers** each serves, and the **transport modes and lanes** between them. It is a **strategic** (multi-year, expensive to reverse) decision, revisited when demand, costs, regulation or strategy shifts.

Decisions: (1) facility role (production, regional DC, forward stocking point, cross-dock, returns centre); (2) location; (3) capacity allocation (what each site makes or stocks); (4) market and supplier allocation (which customer is served from where); (5) ownership (own, 3PL, public warehouse). Objective: **minimise total cost** (fixed facility + inventory + transport + handling + duties/taxes) **subject to a service constraint** (e.g. 95% of demand within 24 hours), or maximise profit. Cost items move in opposite directions as the number of facilities grows: transport and customer delivery time fall; facility, inventory and inbound costs rise (see [[009 Logistics & Distribution]], [[019 Facility Layout & Location]] for micro-location).

### Example
A consumer-durables firm in India runs 14 state-level warehouses. Network design asks: how many hubs after GST? Which plants should feed which hubs? Which 200 SKUs deserve forward stock near metros and which ones sit centrally? Which customers are served from outside their own state?

### In the news
See news box. GST removed a major driver of state-wise depots; the 2025 rate change and tariff shifts are reminders to re-run the model.

### Interview angle
> [!question] How it is asked
> "A client has 14 warehouses. How would you decide the right number and locations?"

> [!tip] Strong answer includes
> - Objective (total landed cost subject to service) and decision variables (open/close, assign)
> - Data needed: demand by location, lanes and rates, facility costs, lead times, tax effects
> - Scenarios and sensitivity (growth, fuel, tax, service level)
> - Qualitative factors and implementation (transition cost, contracts, people)

---

## 2. Warehouse Count vs Cost vs Service
> 🔴 Tier 1 · _Key points:_ U-shaped total cost; facility cost up, transport down, inventory up with square root

### Definition
As the number of warehouses $n$ rises: **facility cost** rises about linearly ($\propto n$), **inventory (safety stock)** rises with $\sqrt{n}$, **outbound transport** falls (roughly $\propto 1/\sqrt{n}$ for uniformly spread demand), and **inbound** transport rises slightly (smaller consignments). A stylised total:

$$TC(n) = a\,n + b\sqrt{n} + \frac{c}{\sqrt{n}}$$

Total cost is **U-shaped** and **flat near the minimum**, so service and risk, not the last rupee, decide the final choice. The optimum satisfies $a + \tfrac{b}{2\sqrt n} - \tfrac{c}{2 n^{3/2}} = 0$.

### Example
Illustrative annual figures (₹ crore): $a = 2.0$ (rent, staff and extra inbound per node), $b = 2.0$ (inventory), $c = 30$ (outbound).

| n | Facility | Inventory | Outbound | Total |
|---|---|---|---|---|
| 1 | 2.0 | 2.0 | 30.0 | 34.0 |
| 2 | 4.0 | 2.8 | 21.2 | 28.0 |
| 3 | 6.0 | 3.5 | 17.3 | **26.8** |
| 4 | 8.0 | 4.0 | 15.0 | 27.0 |
| 5 | 10.0 | 4.5 | 13.4 | 27.9 |
| 6 | 12.0 | 4.9 | 12.2 | 29.1 |
| 9 | 18.0 | 6.0 | 10.0 | 34.0 |

The continuous optimum is $n\approx 3.25$; integers 3 or 4 are within 1% (26.8 vs 27.0). Going from 4 to 9 DCs to promise next-day delivery adds about ₹7 cr a year (34.0 vs 27.0), so ask whether the service uplift earns more than that margin.

### In the news
See news box. Long, variable inbound lead times (21 to 79 days in the Netstock survey) raise the $b$ term (more buffer), while GST lowered $a$ for large consolidated hubs.

### Interview angle
> [!question] How it is asked
> "If we open more warehouses, will costs go down?"

> [!tip] Strong answer includes
> - Names the opposing cost curves and the U-shaped total
> - States that inventory scales with $\sqrt{n}$ not $n$ (next sub-topic)
> - Notes the flat optimum and the role of service targets
> - Suggests running the model with real data and scenarios

---

## 3. Square-Root Law of Inventory Consolidation
> 🔴 Tier 1 · _Key points:_ $SS \propto \sqrt n$; correlation weakens pooling; limits (lead time, product value)

### Definition
For $n$ locations with independent, identical demands (s.d. $\sigma$ each) and the same lead time $L$ and service $z$:

$$SS_{\text{decentralised}} = n\,z\,\sigma\sqrt{L},\qquad SS_{\text{centralised}} = z\,\sigma\sqrt{n}\sqrt{L}\quad\Rightarrow\quad \frac{SS_{central}}{SS_{decentral}} = \frac{1}{\sqrt n}$$

Moving inventory from $n_1$ to $n_2$ locations scales safety stock by $\sqrt{n_2/n_1}$ (the Maister square-root rule; applies to safety stock, and roughly to total inventory when cycle stock is small). With correlation $\rho$ between locations, the pooled s.d. is $\sigma\sqrt{n + n(n-1)\rho}$, so benefit shrinks as demands move together. Also assumes unchanged lead time and service; centralising lengthens outbound delivery.

### Example
Five regional DCs, weekly demand s.d. 200 units each, lead time 2 weeks, $z = 1.65$. Decentralised SS = $5 \times 1.65 \times 200\sqrt2 =$ **2,333 units**. Central: $1.65 \times 200\sqrt5\sqrt2 =$ **1,044 units**, a **55%** reduction ($1-1/\sqrt5$). With $\rho = 0.3$, pooled s.d. = $200\sqrt{5+20\times0.3} = 663$, SS = 1,548 (only 34% saved); with $\rho = 0.6$ the saving falls to about 18%. At ₹8,000 a unit and 22% carrying cost, the independent-demand case frees $1{,}290\times8{,}000\approx$ ₹1.03 cr of stock and ₹23 lakh a year of carrying cost.

### In the news
See news box. Consolidation after GST is the real-world version of this law; the risk is that one hub becomes a single point of failure.

### Interview angle
> [!question] How it is asked
> "We want to go from 8 warehouses to 3. By how much will inventory fall?"

> [!tip] Strong answer includes
> - Square-root law with the ratio $\sqrt{3/8}\approx 0.61$ (about 39% lower safety stock)
> - Conditions: independent demand, same lead time and service
> - Counter-forces: longer delivery, higher outbound cost, concentration risk
> - Related ideas: postponement, [[003 Inventory Management]] risk pooling

---

## 4. Centre-of-Gravity Method
> 🔴 Tier 1 · _Key points:_ weighted-average coordinates, ignores road network and fixed costs, starting point only

### Definition
For demand points $j$ with coordinates $(x_j, y_j)$ and volumes (or volume x rate) $V_j$, the **centre of gravity** is

$$\bar x = \frac{\sum_j V_j x_j}{\sum_j V_j},\qquad \bar y = \frac{\sum_j V_j y_j}{\sum_j V_j}$$

It minimises the weighted **squared** straight-line distance, which is close to, but not the same as, minimising weighted distance (the true minimum-transport-cost point is the **Weber point** found iteratively, e.g. by the Weiszfeld algorithm). Limitations: straight-line distances; a single facility; no fixed costs, capacity or road network; the answer may fall in a lake or a state border: use it as a **region** to search, then apply feasible-site and scoring analysis.

### Example
Plant-to-market outbound volumes (tonnes/month) and coordinates in km (east, north) from Mumbai: Mumbai (0, 0) 500; Ahmedabad (−33, 436) 200; Pune (105, −61) 150; Bengaluru (505, −675) 250; Hyderabad (600, −187) 200. Total 1,300.
$\bar x = (0 - 6{,}600 + 15{,}750 + 126{,}250 + 120{,}000)/1{,}300 \approx$ **196 km**; $\bar y = (0 + 87{,}200 - 9{,}150 - 168{,}750 - 37{,}400)/1{,}300 \approx$ **−99 km**: about 18.2 N, 74.7 E, the Satara belt south of Pune. At ₹5 per tonne-km (straight-line, illustrative): monthly transport = Mumbai ₹22.1 lakh; Pune ₹22.5 lakh; **centre of gravity ₹24.4 lakh**. The Weiszfeld iteration converges to **Mumbai**, because that node's weight (500) outweighs the combined pull of the others. Lesson: the centre of gravity is a screening tool and can be 10% worse than a demand node; real road distances (about 1.3x straight-line) and rates change the picture.

### In the news
See news box. After GST, firms could place a hub by logistics geography rather than state boundaries, which makes a centre-of-gravity screen more meaningful.

### Interview angle
> [!question] How it is asked
> "Where would you put a single warehouse to serve these five cities?" with volumes and distances.

> [!tip] Strong answer includes
> - Formula, calculation and a sanity check against feasible nearby sites
> - Caveats: straight-line distances, one site, no fixed costs, squared vs linear distance
> - Follow-up with weighted scoring and total landed cost for 2-3 shortlisted sites
> - Mention that coordinates can be replaced by drive times

---

## 5. Weighted Scoring and Factor Rating
> 🔴 Tier 1 · _Key points:_ quantitative plus qualitative criteria, weights, sensitivity, tie-breaking

### Definition
**Factor rating** (weighted scoring) scores each candidate site (1-5 or 1-10) on criteria, multiplies by weights summing to 1 and ranks totals: $\text{Score}_k = \sum_i w_i s_{ik}$. Typical criteria: landed cost, service reach, labour availability, infrastructure and connectivity (highways, rail, port), regulatory and tax regime, incentives, land and rent, **risk** (flood, power, political). Use for the **qualitative** layer after the quantitative model shortlists. Control the biases: set weights *before* scoring, test **sensitivity** to weights, and examine **knock-out criteria** (a site that fails a must-have gets zero).

### Example
Weights: cost 0.30, service 0.25, labour 0.15, infrastructure 0.15, risk 0.15. Scores (1-5): Bhiwandi [4, 5, 4, 5, 2], Nagpur [4, 3, 3, 3, 4], Indore [3, 4, 3, 4, 4], Hosur [5, 4, 4, 4, 3]. Totals: Bhiwandi **4.10**, Hosur **4.15**, Indore **3.55**, Nagpur **3.45**. The top two are separated by 0.05, so test weights: with cost 0.15 and service 0.40 (others unchanged) Bhiwandi gets 4.25 and Hosur 4.00, a flip. The recommendation therefore depends on the strategic priority, which must be stated: it is a **priority conversation**, not a computation.

### In the news
See news box. Risk and tax factors in the scoring have changed since 2017 and 2025; a stale scorecard embeds old assumptions.

### Interview angle
> [!question] How it is asked
> "How would you choose between these three candidate cities for a new plant?"

> [!tip] Strong answer includes
> - Quantitative model first (landed cost), qualitative scoring second
> - Weights agreed before scoring; sensitivity analysis
> - Knock-out criteria and risk factors
> - Reference: the same logic as supplier selection in [[002 Procurement & Strategic Sourcing]]

---

## 6. The p-Median Problem
> 🔴 Tier 1 · _Key points:_ open exactly $p$ facilities, minimise demand-weighted distance, binary assignment

### Definition
Choose exactly $p$ of $m$ candidate sites to minimise the total demand-weighted distance (or cost) from each customer to its nearest open site. With $y_i = 1$ if site $i$ is open and $z_{ij} = 1$ if customer $j$ is served by site $i$:

$$\min \sum_i \sum_j w_j d_{ij} z_{ij}\quad\text{s.t.}\quad \sum_i z_{ij}=1\ \forall j,\;\; z_{ij}\le y_i,\;\; \sum_i y_i = p,\;\; y_i, z_{ij}\in\{0,1\}$$

No capacities and no fixed costs: only $p$ and distance. It is NP-hard in general but solves quickly for modest sizes with a MILP solver. Related models: **p-centre** (minimise the *maximum* distance, for emergency services) and **set covering / maximal covering** (every customer within a radius with the fewest sites).

### Example
Using the five-city data above (candidate sites = the five cities, weights = tonnes), the best sites and total weighted distance (tonne-km a month): $p=1$: Mumbai, **442,108**; $p=2$: Mumbai and Bengaluru, **205,097** (-54%); $p=3$: Mumbai, Bengaluru and Hyderabad, **105,664** (-48%). Diminishing returns are visible: each added site cuts less. At ₹5 per tonne-km, $p=2$ to $p=3$ saves $(205{,}097-105{,}664)\times5\times12\approx$ ₹60 lakh a year of straight-line transport: compare against the cost of the third site.

### In the news
See news box. Gartner's "network-centric" language is a statement about choosing $p$ and locations jointly with flows.

### Interview angle
> [!question] How it is asked
> "Formulate the problem of choosing 3 DC locations out of 10 candidates to minimise distance."

> [!tip] Strong answer includes
> - Binary location and assignment variables, the "serve from open site only" constraint, the cardinality constraint
> - Objective: weighted distance (or cost x distance)
> - Contrast with centre of gravity (continuous, one site) and capacitated version
> - Heuristics for large problems (greedy add, interchange) if asked

---

## 7. Capacitated Facility Location (MILP)
> 🔴 Tier 1 · _Key points:_ fixed charges, capacities, flows; binary open/close with continuous flow; solved with PuLP or Solver

### Definition
**Capacitated fixed-charge facility location** (CFLP) chooses which sites to open and how much to ship from each to each customer to minimise fixed plus transport cost under capacity:

$$\min \sum_i f_i y_i + \sum_i\sum_j c_{ij} x_{ij}$$
$$\text{s.t.}\ \sum_i x_{ij} = d_j\ (\forall j),\qquad \sum_j x_{ij} \le K_i\,y_i\ (\forall i),\qquad x_{ij}\le d_j\,y_i,\qquad y_i\in\{0,1\},\ x_{ij}\ge 0$$

$f_i$ = annual fixed cost of site $i$, $K_i$ = capacity, $c_{ij}$ = unit cost from $i$ to $j$, $d_j$ = demand. The constraint $x_{ij}\le d_j y_i$ is redundant logically but **tightens the LP relaxation**, so the solver converges faster. Extensions: single sourcing ($x_{ij}$ binary share), multi-product, multi-echelon (plant to DC to customer), service-time constraints (set $x_{ij}=0$ if time exceeds the limit), duties and taxes in $c_{ij}$, budget and facility count limits. Mathematics of LP/MILP in [[146 Operations Research - Linear Programming]] and [[148 Operations Research - Network Models & Integer Programming]]; the transport sub-problem is in [[147 Operations Research - Transportation, Assignment & Transshipment]].

### Example
Same five cities as candidates, ₹5 per tonne-km on straight-line distance, flows annualised (tonnes/month x 12). Fixed cost (₹ cr/year): Mumbai 1.8, Ahmedabad 1.2, Pune 1.4, Bengaluru 1.5, Hyderabad 1.3. Capacity (tonnes/month): Mumbai 700, Ahmedabad 400, Pune 500, Bengaluru 500, Hyderabad 500. Solving the MILP (verified by enumerating all site sets with an LP for flows): open **Mumbai, Ahmedabad and Hyderabad**: fixed ₹4.30 cr + transport ₹0.86 cr = **₹5.16 cr**. Flows: Mumbai serves Mumbai (500) and Pune (150); Ahmedabad serves itself (200); Hyderabad serves Hyderabad (200) and Bengaluru (250). Opening Bengaluru as well costs ₹5.91 cr (transport falls to ₹0.11 cr but fixed rises by ₹1.5 cr); opening all five costs ₹7.20 cr. A single site is infeasible: capacity 700 < demand 1,300.

```python
import pulp
m = pulp.LpProblem("cflp", pulp.LpMinimize)
y = pulp.LpVariable.dicts("y", sites, cat="Binary")
x = pulp.LpVariable.dicts("x", [(i, j) for i in sites for j in cust], lowBound=0)
m += pulp.lpSum(f[i]*y[i] for i in sites) + pulp.lpSum(c[i, j]*x[i, j] for i in sites for j in cust)
for j in cust: m += pulp.lpSum(x[i, j] for i in sites) == d[j]
for i in sites: m += pulp.lpSum(x[i, j] for j in cust) <= K[i]*y[i]
m.solve(pulp.PULP_CBC_CMD(msg=0))
```

### In the news
See news box. With GST, state tax is no longer a hard constraint on $x_{ij}$, so the optimiser can ship across state lines; a pre-2017 model had to add inter-state tax in $c_{ij}$.

### Interview angle
> [!question] How it is asked
> "Write the MILP for opening warehouses with capacity limits. How would you solve it in Excel?"

> [!tip] Strong answer includes
> - Variables, objective, three constraint families, binary vs continuous
> - Excel Solver: binary cells for open/close, flows as continuous (GRG not needed: use Simplex LP with integer constraints), [[077 Solver, Goal Seek & What-If Analysis]]
> - Python PuLP or OR-Tools for larger models, see [[068 Operations-Specific Python (PuLP, SimPy)]]
> - Sensitivity: change fixed cost, fuel, demand and re-solve; check robustness

---

## 8. Hub-and-Spoke vs Point-to-Point
> 🔴 Tier 1 · _Key points:_ consolidation, route count $n+m$ vs $n\times m$, handling and transit penalty

### Definition
**Point-to-point (P2P)** ships directly from each origin to each destination: $n\times m$ lanes, no extra handling, shortest transit, but thin flows and partial trucks. **Hub-and-spoke** routes everything through a hub (or hubs): $n + m$ lanes, higher fill and frequency, economies of scale, but double handling, extra distance and one more day. Related: **cross-docking**, **milk run** (multi-pickup route), **multi-hub** and **hybrid** (direct for heavy lanes, hub for thin ones). The break-even is on flow per lane: if a lane can fill a truck on its own, go direct.

### Example
5 plants, 8 markets; every lane carries 3 tonnes/day; trucks carry 10 tonnes. **P2P**: 40 lanes dispatch daily at about 30% fill; average 600 km at ₹50,000 per trip: 40 x 50,000 = **₹20.0 lakh/day** for 120 t = ₹16,667/t. **Hub**: each plant sends 24 t/day to the hub, 3 trucks (rounded up) = 15 trucks; the hub sends 15 t/day to each market, 2 trucks = 16 trucks; 31 trucks at 300 km legs of ₹25,000 = ₹7.75 lakh, plus hub handling ₹400/t x 120 t = ₹0.48 lakh: **₹8.23 lakh/day** (₹6,858/t), **59% lower**, for roughly +1 day transit. If lane flows were 10 t/day, direct trucks would be full and P2P would win.

### In the news
See news box. Faster e-way-bill and no state check posts reduced the delay penalty of the extra hub leg after GST.

### Interview angle
> [!question] How it is asked
> "When would you use a hub-and-spoke network over direct shipping?"

> [!tip] Strong answer includes
> - Lane-count arithmetic and consolidation benefits
> - Costs: handling, extra transit, hub congestion and single point of failure
> - Break-even on lane volume and service promise
> - Hybrid design, cross-dock, milk run: see [[125 Transportation Management Deep Dive]]

---

## 9. DC Consolidation: Cost, Service and GST in India
> 🔴 Tier 1 · _Key points:_ inventory pooling, fixed cost, outbound cost, tax and compliance, transition

### Definition
**Consolidation** merges nodes to gain scale and pooling. Cost model for a merge from $n_1$ to $n_2$: saving = fixed cost + inventory carrying cost saved + handling saved; penalty = extra outbound transport + lost service + one-off transition (exit, severance, relocation, system re-mapping). **India context**: before GST (July 2017), inter-state sales attracted CST and entry taxes, and tax credit did not flow freely, so firms held **depots in each state**. After GST, **input tax credit** flows across states, so a hub can serve several states, though the supply is inter-state (IGST), and **place-of-supply and e-way bill** compliance apply. Remaining reasons for state-level nodes: delivery time promise, state-specific regulation (liquor, pharma licences, excise), large market size, perishables and customer contracts. Also check registration: a warehouse in a new state typically needs a separate GST registration for that state (an additional place of business covers extra sites within a state), so consolidation across states also reduces compliance workload. Confirm treatment with a tax adviser.

### Example
Eight state warehouses with weekly demand s.d. (300, 250, 200, 250, 180, 220, 150, 100) units, lead time 2 weeks, $z = 1.65$. Safety stock now: $1.65 \sqrt2 \sum\sigma_j =$ **3,850 units**. One central hub: $1.65\sqrt2\sqrt{\sum\sigma_j^2} =$ **1,416** (-63%). Three regional hubs (groups of 3, 3 and 2 states): **2,328** (-40%, near the $\sqrt{3/8}$ prediction of 39%). For a durable at ₹8,000 a unit and 22% carrying cost, 8 to 3 hubs releases 1,522 units: ₹1.22 cr of stock and about **₹27 lakh a year** of carrying cost, before warehouse rent and manpower savings. Offset: outbound freight rises (longer lanes) and delivery moves from same-day to 1-2 days in some states: set that against the saving, and keep forward stock only for fast-moving SKUs in metros.

### In the news
See news box. GST (2017) opened consolidation; the 2025 rate changes affect product-level landed costs and invite a refresh of the business case.

### Interview angle
> [!question] How it is asked
> "Should the company reduce its 18 state-level depots after GST?"

> [!tip] Strong answer includes
> - Model total cost: fixed, inventory pooling ($\sqrt{n}$), outbound, service-level impact
> - India specifics: IGST and credit flows, e-way bill, state-specific regulations, GST registration per state
> - Segment: consolidate slow movers, keep fast movers forward
> - Transition plan, contracts with 3PLs, pilot in one region first

---

## 10. Coverage and Service-Constrained Design
> 🔴 Tier 1 · _Key points:_ set covering, maximal covering, delivery-time zones, service as constraint or objective

### Definition
Service is often expressed as **coverage**: share of customers or demand within $T$ hours of a facility. **Set covering**: minimise the number of sites so that every demand point is within radius $R$. **Maximal covering**: with $p$ sites, maximise the demand covered. Let $a_{ij}=1$ if site $i$ is within $R$ of customer $j$:

$$\min \sum_i y_i\ \text{ s.t. } \sum_i a_{ij} y_i \ge 1\ \forall j\quad(\text{set cover}),\qquad \max \sum_j d_j u_j\ \text{ s.t. } u_j \le \sum_i a_{ij}y_i,\ \sum_i y_i = p$$

Link service with cost: plot the **cost-service curve** (cost vs % demand within 1 day) and look for the knee. The last 5% of coverage often costs more than the first 80%.

### Example
With the five-city data and a 450 km radius (about one day by road for a night-loaded truck), straight-line distances are: Mumbai to Pune 121 km, to Ahmedabad 437 km, to Hyderabad 628 km, to Bengaluru 843 km; Hyderabad to Bengaluru 497 km. Mumbai alone covers Mumbai, Pune and Ahmedabad: (500 + 150 + 200)/1,300 = **65%** of demand. Adding Hyderabad covers itself (200 t): **81%**. Bengaluru is 497 km from Hyderabad, outside the radius, so full coverage needs a third site there: **100%**. Compare with the cost-minimising CFLP design (Mumbai, Ahmedabad, Hyderabad; ₹5.16 cr), which leaves Bengaluru's 19% of demand beyond one day. Opening Bengaluru as a fourth site costs ₹0.75 cr more a year (₹5.91 cr): the decision is whether 19 points of one-day coverage earn more than ₹0.75 cr.

### In the news
See news box. Quick-commerce and e-commerce push promises toward same-day, which makes coverage the binding constraint; see [[129 E-commerce & Quick-Commerce Fulfilment]].

### Interview angle
> [!question] How it is asked
> "The CEO wants next-day delivery to 95% of customers. How many warehouses do we need?"

> [!tip] Strong answer includes
> - Convert the promise to a coverage radius or time zone
> - Coverage curve and the cost of each additional percentage point
> - Segment by SKU: forward-stock the fast movers only
> - Test with data: customer location file and drive-time matrix

---

## 11. Tools, Data and Modelling Workflow
> 🔴 Tier 1 · _Key points:_ baseline, validation, scenarios; Solver, PuLP, anyLogistix, Coupa, Optilogic

### Definition
**Data**: demand by customer-location-product (12-36 months), cost curves (facility fixed and variable, handling), lane rates and transit times (by mode and weight break), inventory parameters (lead time, variability, service targets), tax and duty, capacity and constraints. **Workflow**: (1) **baseline model** replicating current costs within 1-3% of actuals (validation: if it cannot reproduce today, no scenario is credible); (2) **cleanse and aggregate** demand (customer clusters by pin-code or district), (3) **scenarios** (fewer sites, different sites, growth, tax change, fuel +20%), (4) **sensitivity and robustness** (which decisions are the same across scenarios), (5) **business case** (savings, one-time costs, payback), (6) **implementation roadmap**. **Tools**: Excel Solver for small cases (see [[043 Advanced Excel (Pivot, Solver, Forecasting)]]), Python PuLP/OR-Tools, and commercial network-design platforms such as **anyLogistix** (simulation + optimisation), **Coupa Supply Chain Design** (formerly LLamasoft, Supply Chain Guru), **Optilogic**, and planning suites with design modules. Tool names change owners often; verify the current vendor in an interview.

### Example
Baseline for a 3PL's 12-DC network: model total cost ₹412 cr against actual ₹418 cr (1.4% gap): acceptable. Scenario "9 DCs": -₹19 cr annual cost, +4 points of next-day coverage lost; scenario "9 DCs + 3 forward nodes for top 300 SKUs": -₹13 cr and coverage retained. One-time transition ₹22 cr; payback = 22 / 13 = **1.7 years**.

### In the news
See news box. Gartner's emphasis on network-centric planning corresponds to the "design to operations" loop in modern platforms.

### Interview angle
> [!question] How it is asked
> "Walk me through the steps and data needed for a network design study."

> [!tip] Strong answer includes
> - Baseline validation before scenarios
> - Data hygiene and aggregation choices
> - Scenario list and sensitivity, not a single "optimal" answer
> - Payback and implementation risk, and who must buy in (sales for service, finance for capex)

---

## 12. Case: Redesigning a Pan-India Distribution Network
> 🔴 Tier 1 · _Key points:_ structure, numbers, recommendation, risks

### Definition
A repeatable structure for a network-redesign case: (1) **clarify** objectives (cost, service, growth, resilience) and constraints (capex, existing leases); (2) **baseline** (volumes, nodes, cost per unit by node); (3) **options** (status quo, consolidate to hubs, add forward nodes, outsource to 3PL); (4) **evaluate** (cost, service, inventory, risk, flexibility); (5) **recommend** with phasing; (6) **risks and mitigations**. Quantify with the building blocks above: $\sqrt{n}$ pooling, $TC(n)$ curve, hub-and-spoke consolidation.

### Example
FMCG company: 18 state depots, ₹1,200 cr revenue distributed, logistics cost 9.5% of revenue (₹114 cr). Option A: 6 regional hubs. Inventory: safety stock scales by $\sqrt{6/18}=0.577$, so stock falls 42%; if safety stock is ₹60 cr, savings ₹25 cr stock, carrying at 20% = **₹5 cr**/yr. Facilities: 12 fewer leases saves ₹8 cr. Outbound freight rises 6% of ₹70 cr = ₹4.2 cr. Net run-rate saving about 5.0 + 8.0 - 4.2 = **₹8.8 cr** a year, 0.7% of revenue. One-time costs ₹14 cr: payback **1.6 years**. Risk: service at distant-state outlets; mitigate by forward stock for top 100 SKUs and a 2-day SLA. Recommendation: phase two regions first.

### In the news
See news box. Post-GST consolidation is the most common real-world version of this case in India; post-2025 rate changes require a refreshed landed-cost view.

### Interview angle
> [!question] How it is asked
> "A client with 18 depots asks if it should consolidate. What do you do?"

> [!tip] Strong answer includes
> - Structured issue tree (cost, service, risk) and a hypothesis
> - Numbers using pooling, facility and freight changes
> - Net saving, payback and phasing
> - Risks: service dips, 3PL capacity, tax compliance, change management; tie to [[026 Case Interview — Operations Cases]]

---

## 13. ⭐ Advanced: Robust, Multi-Echelon and Dynamic Network Design
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Real networks face **uncertainty** (demand, cost, disruption), **multiple echelons** (suppliers, plants, DCs, stores) and **time** (phasing). Techniques: **scenario-based (stochastic) design** minimises expected cost across scenarios or minimises **regret** (the worst gap to each scenario's best); **robust design** keeps decisions that perform acceptably under most scenarios; **multi-period** design adds open/close timing and capex; **multi-echelon inventory optimisation** sets stocks jointly for all echelons; **resilience** adds redundancy (dual sourcing, backup sites). Cost of a regret-minimising choice:

$$\text{Regret}(d,s)=C(d,s)-\min_{d'}C(d',s),\qquad \min_d \max_s \text{Regret}(d,s)$$

### Example
Two designs, three scenarios (₹ cr cost): Design A (3 hubs): base 100, fuel+30% 118, disruption at main hub 160. Design B (4 hubs): 106, 120, 125. Best per scenario: base 100 (A), fuel 118 (A), disruption 125 (B). Regret of A: 0, 0, 35; of B: 6, 2, 0. Max regret: A = 35, B = 6. A minimax-regret planner picks **B** (four hubs): it pays 6 cr extra in the base case to avoid a 35 cr loss. With scenario probabilities 0.6, 0.3, 0.1, expected cost A = 0.6 x 100 + 0.3 x 118 + 0.1 x 160 = **111.4**; B = 0.6 x 106 + 0.3 x 120 + 0.1 x 125 = **112.1**; A is slightly cheaper in expectation, so the choice depends on risk appetite.

### In the news
See news box. A 21-day versus 79-day lead-time spread (Netstock survey) is the kind of input variability a robust design must absorb.

### Interview angle
> [!question] How it is asked
> "How would you make the network resilient without paying for redundancy everywhere?"

> [!tip] Strong answer includes
> - Scenario analysis with probabilities and regret
> - Selective redundancy (critical SKUs, bottleneck nodes)
> - Value-of-resilience logic: expected loss avoided vs cost, see [[015 Supply Chain Risk & Resilience]]
> - Flexibility options (3PL overflow, contract capacity)
