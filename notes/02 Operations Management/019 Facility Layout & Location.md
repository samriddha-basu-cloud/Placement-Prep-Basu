---
tags: [operations-management, tier2]
area: Operations Management
topic: "Facility Layout & Location"
tier: Tier 2
roles: Operations
status: complete
subtopics: 10
---
# Facility Layout & Location

⬅ [[018 Capacity Management & OEE]] · [[_Index - Operations Management|Operations Management]] · [[020 Operations Strategy]] ➡

> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Layout Types]]
2. [[#2. Product Layout]]
3. [[#3. Process Layout]]
4. [[#4. Facility Location Decisions]]
5. [[#5. Transportation Method (LP)]]
6. [[#6. Material Handling Equipment]]
7. [[#7. Space Planning & Utilization]]
8. [[#8. Plant Layout Diagrams]]
9. [[#9. ⭐ Advanced: Systematic Layout Planning (SLP) and Relationship Charts]]
10. [[#10. ⭐ Advanced: Cellular Manufacturing and Group Technology]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): where India is putting its new plants
> **Micron's Sanand plant starts production (inaugurated 28 Feb 2026).** Prime Minister Modi inaugurated Micron's ATMP (assembly, testing, marking and packaging) plant at Sanand, Gujarat, India's first semiconductor chip facility to begin commercial production. Total investment is **$2.7 billion** (including central and state incentives), the plant is expected to create about **5,000 direct and 15,000 indirect jobs**, and it was the first project approved under India's **₹76,000 crore** Semiconductor Mission; by Feb 2026 the government had approved **10 projects with ₹1.60 lakh crore** of investment. ([Business Standard](https://www.business-standard.com/amp/industry/news/pm-modi-inaugurates-micron-atmp-unit-sanand-plant-starts-production-126022801029_1.html))
> 
> **Maruti Suzuki Hansalpur Plant D (reported 30 Jul 2026).** Capacity of the Hansalpur (Gujarat) facility rose from 750,000 to **1 million vehicles a year**, India's largest single-location passenger-vehicle plant; Maruti's total capacity is **2.9 million units a year**, cumulative Hansalpur investment about **₹25,288.7 crore**, and the site handles about **47% of Maruti's export shipments**. ([Evo India](https://www.evoindia.com/news/car-news/maruti-suzuki-hansalpur-reaches-1-million-capacity-587590))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Layout Types
> 🟠 Tier 2 · _Tracker hint:_ Product (line), Process (functional), Fixed-position, Cellular

### Definition
Layout decides how departments, machines and flows are arranged to minimise handling and delay.

| Layout | Arrangement | Volume / variety | Strength | Weakness |
|---|---|---|---|---|
| **Product (line)** | Stations in order of operations | High volume, low variety | Low unit cost, simple control | Inflexible; one breakdown stops the line |
| **Process (functional)** | Similar machines grouped (turning, milling) | Low volume, high variety | Flexible, general-purpose machines | Long flows, high WIP, complex scheduling |
| **Fixed-position** | Product stays; resources come to it | One-off, very large (ships, bridges, buildings) | Avoids moving the product | Coordination of resources |
| **Cellular (group technology)** | Machines grouped by part family | Medium volume / medium variety | Shorter flow, less WIP, team ownership | Needs stable part families; cell balance |

Also **hybrid** layouts (e.g., fabrication in process layout, assembly in a line) and **retail/service layouts** (warehouse, store).

### Example
Maruti's car plant: press shop, body shop, paint and final assembly arranged as a product layout (the line) because volumes are very high. A custom-machine job shop uses a process layout. Shipbuilding uses fixed-position.

### In the news
See news box. Large plants like Hansalpur are product-layout (line) facilities; Micron's ATMP plant is a process flow of assembly and test steps.

### Interview angle
> [!question] How it is asked
> "Which layout would you choose for X and why?"

> [!tip] Strong answer includes
> - Match to volume and variety
> - Pros/cons of each
> - Cellular as the compromise
> - Consider flexibility needs and future product changes

---

## 2. Product Layout
> 🟠 Tier 2 · _Tracker hint:_ Assembly lines; balancing; takt time alignment

### Definition
In a product layout the work is split into **tasks** assigned to **workstations** along a line. **Line balancing** aims to equalise work content across stations to meet demand.

$$\text{Takt time} = \frac{\text{Available time per period}}{\text{Demand per period}}, \qquad \text{Min. stations} = \left\lceil \frac{\sum t_i}{\text{Takt (cycle time)}} \right\rceil$$
$$\text{Balance efficiency} = \frac{\sum t_i}{N \times CT}, \qquad \text{Balance delay} = 1 - \text{Efficiency}$$
Method (e.g., **Ranked positional weight / largest candidate rule**): list tasks and precedence; compute takt; assign tasks to a station in order until its time would exceed $CT$; open a new station; repeat. Constraints: precedence, zoning, task time ≤ takt.

### Example
Available time 450 min/shift, demand 225 units → takt = 2 min. Total task time = 11 min → minimum stations $= \lceil 11/2 \rceil = \lceil 5.5 \rceil = 6$. If balancing achieves 6 stations: efficiency $= 11/(6 \times 2) = 91.7\%$; balance delay 8.3%. If demand rises to 300/shift: takt = 1.5 min → $\lceil 11/1.5 \rceil = \lceil 7.33 \rceil = 8$ stations.

### In the news
See news box. Plants running at a million vehicles a year need balanced lines tuned to takt for each model mix.

### Interview angle
> [!question] How it is asked
> "Calculate takt time and the minimum number of workstations."

> [!tip] Strong answer includes
> - Takt from demand, not from what the line can do
> - Minimum stations with rounding up
> - Efficiency and balance delay
> - Handling mixed models and variability (buffers, floaters)

---

## 3. Process Layout
> 🟠 Tier 2 · _Tracker hint:_ Departmental grouping; material handling distance minimization

### Definition
In a process (functional) layout, similar processes are grouped into departments, and different jobs follow different routes. The design goal is to **minimise total material-handling cost**, usually modelled as **load-distance**:
$$\text{Cost} = \sum_{i}\sum_{j} f_{ij} \times d_{ij} \times c$$
where $f_{ij}$ is flow (trips/loads) between departments $i$ and $j$, $d_{ij}$ the distance and $c$ the cost per load-distance. Heavy-flow pairs should be adjacent. Methods: **from-to (flow) matrix**, trial and error swaps, **CRAFT** (computerised swaps), **Systematic Layout Planning** (see the advanced section below).

### Example
Three departments A, B, C in a row with unit spacing. Flows: A-B = 50, B-C = 10, A-C = 100 loads. Layout A-B-C: distances AB = 1, BC = 1, AC = 2 → load-distance $= 50 + 10 + 200 = 260$. Layout A-C-B: AC = 1, CB = 1, AB = 2 → $100 + 10 + 100 = 210$. Better: put the heavy A-C pair adjacent.

### In the news
See news box. Semiconductor ATMP and similar plants group by process step (wafer handling, assembly, test), a functional logic with strict cleanliness zones.

### Interview angle
> [!question] How it is asked
> "How would you reduce movement in a job shop?"

> [!tip] Strong answer includes
> - Flow matrix and load-distance metric
> - Place high-flow departments adjacent
> - Move toward cells for part families
> - Consider non-quantitative factors (noise, safety, expansion)

---

## 4. Facility Location Decisions
> 🟠 Tier 2 · _Tracker hint:_ Factor rating, centroid method, break-even analysis

### Definition
Location decisions combine cost and non-cost factors (labour, power, land, taxes, incentives, logistics, suppliers, markets, risk).

1. **Factor rating (weighted scoring):** score each site 1–10 or 0–100 per factor, weight by importance (weights sum to 1); total $= \sum w_i s_i$.
2. **Centre-of-gravity (centroid) method:**
$$\bar{x} = \frac{\sum V_i x_i}{\sum V_i},\qquad \bar{y} = \frac{\sum V_i y_i}{\sum V_i}$$
with $V_i$ = volume to/from point $i$ and $(x_i, y_i)$ its coordinates. A starting point, ignoring road networks.
3. **Break-even (cost-volume) analysis:** total cost $TC = F + vQ$; compare sites; the volume where two sites cost the same is $Q^* = \dfrac{F_B - F_A}{v_A - v_B}$.

### Example
**Centroid:** points (10,20) volume 100; (30,10) volume 200; (50,40) volume 100. $\bar{x} = (1000 + 6000 + 5000)/400 = 30$, $\bar{y} = (2000 + 2000 + 4000)/400 = 20$ → (30, 20).
**Break-even:** Site A: F = ₹5,00,000, v = ₹30/unit. Site B: F = ₹8,00,000, v = ₹20/unit. $Q^* = (800{,}000 - 500{,}000)/(30 - 20) = 30{,}000$ units. Below 30,000 choose A; above, B.

### In the news
See news box. Micron chose Sanand (Gujarat) and Maruti scaled at Hansalpur (also Gujarat); state incentives and an existing industrial cluster are typical weights in a factor rating (the sources do not state the firms' decision criteria).

### Interview angle
> [!question] How it is asked
> "Where would you locate a new plant/warehouse?"

> [!tip] Strong answer includes
> - Quantitative (cost model, centroid) plus qualitative (factor rating)
> - Fixed vs variable cost and break-even volume
> - India factors: state incentives, GST implications, industrial corridors, port access, labour availability
> - Risk and flexibility; clarify demand and supplier locations first

---

## 5. Transportation Method (LP)
> 🟠 Tier 2 · _Tracker hint:_ Minimizing transport cost; northwest corner, MODI

### Definition
The **transportation problem** ships goods from $m$ sources (supply $s_i$) to $n$ destinations (demand $d_j$) at unit cost $c_{ij}$ to minimise total cost:
$$\min \sum_i\sum_j c_{ij}x_{ij}\quad \text{s.t.}\quad \sum_j x_{ij} \le s_i,\ \sum_i x_{ij} \ge d_j,\ x_{ij}\ge 0$$
Balanced when $\sum s = \sum d$ (else add a dummy). Steps: (1) **initial feasible solution** (Northwest Corner, Least Cost, Vogel's Approximation); (2) test optimality with **MODI (u-v method)**: for basic cells $u_i + v_j = c_{ij}$; for non-basic cells the opportunity cost $c_{ij} - (u_i + v_j)$ must be $\ge 0$ for optimality; (3) if negative, enter that cell via a closed loop and repeat. Basic cells must equal $m + n - 1$.

### Example
Plants P1 (supply 30), P2 (40); warehouses W1 (25), W2 (25), W3 (20). Costs: P1: 4, 6, 8; P2: 5, 3, 7.
NW corner: P1→W1 25, P1→W2 5, P2→W2 20, P2→W3 20: cost $= 100 + 30 + 60 + 140 = ₹330$.
MODI: improve by moving 5 units (P1→W3 and P2→W2 up, P1→W2 and P2→W3 down): change $= +40 + 15 - 30 - 35 = -10$ → **₹320**: P1→W1 25, P1→W3 5, P2→W2 25, P2→W3 15. Check: $u_1 = 0$, $v_1 = 4$, $v_3 = 8$, $u_2 = -1$, $v_2 = 4$; opportunity costs P1W2 $= 6 - 4 = 2$, P2W1 $= 5 - 3 = 2$, both $\ge 0$ → optimal.

### In the news
See news box. Multi-plant, multi-market networks (Maruti's exports from Hansalpur) are choices of "which source serves which market" at minimum landed cost.

### Interview angle
> [!question] How it is asked
> "Solve this transportation problem" or "How would you allocate production across plants to minimise cost?"

> [!tip] Strong answer includes
> - Balance supply and demand (dummy if needed)
> - Initial solution then optimality test (MODI or solver)
> - Mention degeneracy and capacity limits
> - In practice use Excel Solver/LP, and add non-cost constraints (service, risk)

---

## 6. Material Handling Equipment
> 🟠 Tier 2 · _Tracker hint:_ Forklifts, conveyors, AGVs, cranes — selection criteria

### Definition
Material handling is the movement, protection, storage and control of materials. Principles: minimise distance, avoid double handling, use gravity, unit loads, and standardise. Equipment classes:

| Equipment | Best for | Considerations |
|---|---|---|
| **Forklifts / pallet trucks** | Flexible pallet movement, loading | Aisle width, labour, safety |
| **Conveyors (belt, roller, overhead)** | Continuous, fixed-path flows | Low flexibility, high capex |
| **AGVs / AMRs** | Repeating (AGV) or flexible (AMR) transport | Navigation, traffic, floor condition |
| **Cranes and hoists** | Heavy, large loads | Span, capacity, safety |
| **ASRS / shuttles** | High-density storage and retrieval | High capex, throughput design |

Selection criteria: load size/weight, flow volume and distance, path fixed or variable, flexibility, space, safety, capex vs opex, integration with WMS, and life-cycle cost.

### Example
Moving 40 pallets/hour over 200 m: a manual forklift handles about 15 pallets per hour for that trip; you would need 3 forklifts and operators. A conveyor handles that flow continuously with one loader but costs more upfront; choose by comparing annual labour saved vs annualised capex.

### In the news
See news box. Large fabs and ATMP plants and high-volume auto plants rely on automated handling; Amazon-type AMR scale is covered in [[016 Digital Supply Chain & Industry 4.0]].

### Interview angle
> [!question] How it is asked
> "How would you choose handling equipment for a new warehouse?"

> [!tip] Strong answer includes
> - Flow, load, distance, flexibility as selection criteria
> - Fixed-path vs flexible equipment
> - Life-cycle cost and safety
> - Future volume growth and WMS integration

---

## 7. Space Planning & Utilization
> 🟠 Tier 2 · _Tracker hint:_ Aisle width, storage density, cubic utilization

### Definition
Space planning balances **storage density** (how much you store per square metre) against **accessibility and throughput**.
- **Floor-space utilisation** $= \dfrac{\text{Area used for storage}}{\text{Total floor area}}$; typically 20-40% of a warehouse is aisles, docks and offices.
- **Cubic utilisation** $= \dfrac{\text{Volume of stored goods}}{\text{Usable cubic volume}}$; building height, racking and forklift reach decide it. 
- **Aisle width:** narrow aisles raise density but need specialised trucks (VNA); wider aisles ease counterbalance trucks.
- Storage types: block stacking, selective racking, drive-in, push-back, flow racks, mezzanines, ASRS.
- **Slotting:** place fast movers (ABC analysis) near the dock at golden-zone heights.
Total pallet positions $= \text{rack bays} \times \text{levels} \times \text{pallets per bay}$.

### Example
Warehouse 10,000 m² floor, 8 m clear height. Racking occupies 5,000 m²; so floor utilisation of storage = 50%. Racks use 6 m of 8 m height on average: cubic utilisation (ignoring density) $\approx 50\% \times 75\% = 37.5\%$. Moving to narrower aisles can raise rack area to 6,500 m² (65%) and cubic utilisation to $65\% \times 75\% = 48.75\%$, about 30% more storage.

### In the news
See news box. Land and building costs are a core part of plant economics; large integrated sites aim for high utilisation of built space.

### Interview angle
> [!question] How it is asked
> "How would you increase warehouse capacity without a new building?"

> [!tip] Strong answer includes
> - Floor vs cubic utilisation
> - Narrow aisles, higher racking, mezzanines, slotting
> - Trade-off: density vs picking speed and safety
> - Quantify pallet positions and cost per position

---

## 8. Plant Layout Diagrams
> 🟠 Tier 2 · _Tracker hint:_ Block layout, detailed layout, 2D/3D CAD basics

### Definition
Layout design runs from broad to detailed:
1. **Block layout:** departments as blocks sized by area, arranged using flow/relationship data (from-to chart, REL chart).
2. **Detailed layout:** exact positions of machines, aisles, utilities, storage, safety zones, fire exits, drainage.
3. **Visualisation and validation:** 2D CAD (AutoCAD) drawings; **3D models and digital factory tools** (e.g., Tecnomatix, FlexSim, Revit) for clash checks, walk-throughs and simulation of flows.

Design inputs: product and volume forecast, process flow, equipment footprints, handling methods, utilities, safety and statutory norms (e.g., Factories Act), future expansion space. Steps end with evaluation (distance, cost, flexibility), approval and implementation.

### Example
Block layout for a packaging unit: Receiving → Raw store → Printing → Converting → Packing → Dispatch placed in a U-shape so that receiving and dispatch share the docks (saving gate staff and yard), with a 20% expansion strip left beside Converting.

### In the news
See news box. Hansalpur grew by adding a fourth plant (Plant D) within one site, showing the value of reserving expansion space early.

### Interview angle
> [!question] How it is asked
> "What are the steps in designing a plant layout?"

> [!tip] Strong answer includes
> - Block then detailed layout
> - Inputs and constraints (flow, safety, utilities)
> - Use of CAD/3D and simulation to test
> - Expansion and flexibility built in

---

## 9. ⭐ Advanced: Systematic Layout Planning (SLP) and Relationship Charts
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**SLP (Muther)** handles layouts where flow is not the only concern. Steps: collect P-Q-R-S-T data (Product, Quantity, Routing, Supporting services, Time) → analyse **flow** (from-to chart) and **activity relationships** (REL chart) → combine into a relationship diagram → add **space requirements** → generate alternatives → evaluate against modifying considerations (safety, handling, expansion) → select.

**REL chart** closeness codes: **A** absolutely necessary, **E** especially important, **I** important, **O** ordinary, **U** unimportant, **X** undesirable (e.g., paint next to welding sparks), with reason codes. Convert to numeric weights (e.g., A = 6, E = 5, I = 4, O = 3, U = 2, X = 1... conventions vary) for scoring layouts.

### Example
Departments: Paint (P), Welding (W), Assembly (A). REL: A-P = A, A-W = E, P-W = X. Keep Assembly between Welding and Paint: W-A-P in a row. Closeness is high for the two A/E pairs while the X pair (P-W) is separated by Assembly, at distance 2.

### In the news
See news box. Semiconductor ATMP plants have strict "undesirable adjacency" logic (cleanliness, vibration), a real-life use of X ratings (generally true of such plants; not a claim from the source).

### Interview angle
> [!question] How it is asked
> "How do you lay out a facility when both flow and non-flow factors matter?"

> [!tip] Strong answer includes
> - SLP steps and P-Q-R-S-T data
> - REL chart with A/E/I/O/U/X
> - Combining quantitative flow and qualitative closeness
> - Evaluate alternatives with weighted criteria

---

## 10. ⭐ Advanced: Cellular Manufacturing and Group Technology
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Group technology (GT)** classifies parts into **families** with similar shapes or processing steps. **Cellular manufacturing** dedicates a cell of machines to a family, giving near-flow-line performance for medium volume and variety. Cell formation methods: **production flow analysis** and **rank order clustering (ROC)** on a part-machine incidence matrix, which sorts rows and columns by binary weights to reveal blocks.

Benefits: shorter lead time, less WIP, fewer setups, better quality ownership. Limits: needs stable families; exceptional parts requiring machines in several cells; reduced machine utilisation.

### Example
Part-machine matrix (1 = part uses machine): P1 uses M1, M2; P2 uses M1, M2; P3 uses M3, M4; P4 uses M3, M4. After clustering: Cell 1 = {M1, M2} makes P1, P2; Cell 2 = {M3, M4} makes P3, P4. No inter-cell moves. If a part P5 needs M2 and M3, it is an **exceptional element**; options: duplicate a machine or subcontract.

### In the news
See news box. The sources do not describe cell layouts; the link is that high-volume plants use line layouts, while medium-volume, high-mix shops are where cells pay off.

### Interview angle
> [!question] How it is asked
> "Your job shop has long lead times and high WIP. What layout change would you consider?"

> [!tip] Strong answer includes
> - Part-family analysis (GT) first
> - Cells for stable families; benefits quantified
> - Cost: duplicate machines, lower utilisation
> - Transition plan with pilot cell

---
## 🔗 Go deeper: expansion notes
- [[113 Network Design & Facility Location Modelling|Network Design & Facility Location Modelling]]
- [[147 Operations Research - Transportation, Assignment & Transshipment|Operations Research - Transportation, Assignment & Transshipment]]
