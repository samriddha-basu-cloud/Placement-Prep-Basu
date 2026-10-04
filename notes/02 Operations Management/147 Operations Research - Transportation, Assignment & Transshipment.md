---
tags: [operations-management, tier1]
area: Operations Management
topic: "Operations Research - Transportation, Assignment & Transshipment"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Operations Research - Transportation, Assignment & Transshipment

⬅ [[146 Operations Research - Linear Programming]] · [[_Index - Operations Management|Operations Management]] · [[148 Operations Research - Network Models & Integer Programming]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. The Transportation Problem: Formulation and Balance]]
2. [[#2. Northwest Corner Method]]
3. [[#3. Least-Cost (Matrix-Minimum) Method]]
4. [[#4. Vogel's Approximation Method (VAM)]]
5. [[#5. Optimality Test: MODI (u–v) Method, Full Worked Example]]
6. [[#6. Stepping-Stone Method and Degeneracy]]
7. [[#7. Unbalanced, Prohibited-Route and Maximisation Variants]]
8. [[#8. The Assignment Problem and the Hungarian Method]]
9. [[#9. Assignment Variants and Related Problems]]
10. [[#10. Transshipment Problems]]
11. [[#11. Applications: Network Design, Allocation and Sourcing]]
12. [[#12. Solver and Python Formulation]]
13. [[#13. ⭐ Advanced: Duality, Min-Cost Flow Generality and Network Simplex]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Amazon India re-cuts its fulfilment network, and flow algorithms get near-linear
> **Amazon India's biggest network expansion (14 September 2026).** Amazon India announced 20 new fulfilment centres, 6 new sort centres and 150 new last-mile delivery stations ahead of the festive season, backed by an investment of over ₹2,800 crore. Storage capacity rises about 50% (to 64 million cubic feet) and sortation area about 25% (2.4 to 3 million sq ft); seven of the new fulfilment centres and all six sort centres are in non-metro cities, including first facilities in Raipur, Ranchi and Varanasi. Deciding which node serves which pin code at minimum landed cost is a transportation/assignment problem solved at network scale. ([Amazon India](https://www.aboutamazon.in/news/operations/amazon-india-operations-network-expansion-biggest))
>
> **Min-cost flow in almost-linear time (arXiv March 2022, FOCS 2022).** Chen, Kyng, Liu, Peng, Probst Gutenberg and Sachdeva gave an algorithm computing exact maximum and minimum-cost flows in time $m^{1+o(1)}$ on a graph with $m$ edges (polynomially bounded capacities and costs). Transportation, assignment and transshipment are special cases of min-cost flow, so the result is the theoretical ceiling for this whole note; the paper lists optimal transport and matrix scaling among its applications. ([arXiv 2203.00671](https://arxiv.org/pdf/2203.00671v1))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The Transportation Problem: Formulation and Balance
> 🔴 Tier 1 · _Key points:_ Sources, destinations, cost matrix, balanced vs unbalanced

### Definition
The **transportation problem** ships a single homogeneous product from $m$ sources (plants, warehouses) with supplies $s_i$ to $n$ destinations (DCs, customers) with demands $d_j$, at unit cost $c_{ij}$, to minimise total shipping cost.

$$\min\ Z=\sum_{i=1}^{m}\sum_{j=1}^{n} c_{ij}x_{ij}\quad\text{s.t.}\ \sum_j x_{ij}=s_i,\ \ \sum_i x_{ij}=d_j,\ \ x_{ij}\ge 0$$

It is an LP with $mn$ variables and $m+n$ constraints, but only $m+n-1$ of them are independent when total supply equals total demand (**balanced**), so every basic feasible solution has exactly $m+n-1$ allocated (basic) cells. Special structure means the tableau of the full simplex is unnecessary: transportation-specific methods (this note) are lighter, and **integer supplies and demands always give integer optimal flows** (the integrality property, because the constraint matrix is totally unimodular).

Working example for the whole note (supply and demand in hundreds of units; costs in ₹ per unit):

| | D1 | D2 | D3 | D4 | Supply |
|---|---|---|---|---|---|
| Nashik (P1) | 8 | 6 | 10 | 9 | 100 |
| Pune (P2) | 9 | 12 | 13 | 7 | 120 |
| Nagpur (P3) | 14 | 9 | 16 | 5 | 80 |
| Demand | 70 | 80 | 90 | 60 | 300 |

Total supply 300 = total demand 300, so it is balanced. Process: (1) find an initial basic feasible solution; (2) test optimality; (3) improve until optimal.

### Example
The two checks to run first: balance (add a dummy row or column if not, sub-topic 7) and degeneracy (an initial solution with fewer than $m+n-1 = 6$ occupied cells, sub-topic 6). Here $3+4-1 = 6$, so a non-degenerate solution has six allocations. Costs are per unit, so total cost = Σ (units × cost) × 100: a final answer of 2,520 means ₹2.52 lakh per cycle.

### In the news
See news box. Amazon's Sept 2026 expansion changes both sides of the cost matrix at once: more sources (fulfilment centres, sort centres) and more destinations (delivery stations), so the network is re-solved rather than patched.

### Interview angle
> [!question] How it is asked
> "A company has 3 plants and 4 warehouses. How would you decide how much to ship from each plant to each warehouse?"

> [!tip] Strong answer includes
> - Identify supply, demand, unit cost and the objective; check balance
> - Name the method: initial solution (VAM) then optimality test (MODI) or just LP/Solver
> - Mention constraints that break the textbook model: capacity on lanes, minimum truckloads, service-level and transit-time limits
> - Link to network design ([[113 Network Design & Facility Location Modelling]]) and transportation management ([[125 Transportation Management Deep Dive]])

---
## 2. Northwest Corner Method
> 🔴 Tier 1 · _Key points:_ Fast, ignores cost; starting point only

### Definition
**Northwest Corner (NWC):** start at the top-left cell, allocate $\min(s_i, d_j)$, cross out the exhausted row or column, move right (if a column is satisfied) or down (if a row is exhausted), repeat. It is purely positional: costs are not consulted, so the starting solution is usually poor, but it is quick and always yields a BFS.

### Example
Working example, step by step:

| Cell | Allocation | Remaining |
|---|---|---|
| (P1,D1) | min(100,70) = 70 | S1 = 30, D1 done |
| (P1,D2) | min(30,80) = 30 | S1 done, D2 = 50 |
| (P2,D2) | min(120,50) = 50 | S2 = 70, D2 done |
| (P2,D3) | min(70,90) = 70 | S2 done, D3 = 20 |
| (P3,D3) | min(80,20) = 20 | S3 = 60, D3 done |
| (P3,D4) | min(60,60) = 60 | all done |

Cost: $70(8)+30(6)+50(12)+70(13)+20(16)+60(5) = 560+180+600+910+320+300 = 2{,}870$. Six occupied cells = $m+n-1$, so non-degenerate. The true optimum is 2,520, so NWC is 13.9% above optimal ($350/2520$). This is the starting point used for the MODI walk-through in sub-topic 5.

### In the news
See news box. Real network solvers never start from a positional rule; the NWC method matters as a teaching device and for generating a quick feasible plan.

### Interview angle
> [!question] How it is asked
> "Find an initial feasible solution using the northwest corner rule and tell me its cost."

> [!tip] Strong answer includes
> - Clean allocation table with remaining supply/demand at each step
> - Count occupied cells and compare with $m+n-1$ (spot degeneracy)
> - State clearly that NWC ignores cost and is not optimal in general
> - Compare cost with later methods to show the value of better starting heuristics

---
## 3. Least-Cost (Matrix-Minimum) Method
> 🔴 Tier 1 · _Key points:_ Allocate greedily to cheapest cells

### Definition
**Least-Cost Method (LCM):** repeatedly pick the cell with the lowest unit cost (break ties by largest possible allocation or arbitrarily), allocate $\min(s_i,d_j)$, cross out the exhausted row/column. It uses cost information, so the start is usually better than NWC, but the greedy choice can force expensive cells at the end.

### Example
Working example, cheapest first: (P3,D4) cost 5 → min(80,60) = 60; next lowest: (P1,D2) cost 6 → min(100,80) = 80; (P2,D4) cost 7 is gone (D4 done); (P1,D1) cost 8 → min(20,70) = 20; (P2,D1) cost 9 → min(120,50) = 50; (P3,D2) cost 9 is gone (D2 done); (P1,D4) gone; (P1,D3) gone (S1 exhausted); (P2,D3) cost 13 → min(70,90) = 70; (P3,D3) cost 16 → 20.

Allocation: (P1,D1)=20, (P1,D2)=80, (P2,D1)=50, (P2,D3)=70, (P3,D3)=20, (P3,D4)=60. Cost: $20(8)+80(6)+50(9)+70(13)+20(16)+60(5)=160+480+450+910+320+300=2{,}620$, which is 4.0% above the optimum, versus NWC's 13.9%.

### In the news
See news box. Nearest-source allocation is the intuitive rule for order routing; the lesson of LCM (greedy is a decent start, but gets locked into bad late choices) is why a network of Amazon's size is planned with exact optimisation rather than rules of thumb.

### Interview angle
> [!question] How it is asked
> "Why not just ship from the cheapest source to each destination?"

> [!tip] Strong answer includes
> - Greedy ignores the opportunity cost: using a cheap lane for one destination can force a very expensive lane elsewhere
> - Shows LCM start (2,620) improving on NWC (2,870) but still not optimal (2,520)
> - Explains that capacity limits make "nearest" infeasible for everyone at once
> - Names VAM as a smarter heuristic using regret

---
## 4. Vogel's Approximation Method (VAM)
> 🔴 Tier 1 · _Key points:_ Penalty = difference between two lowest costs

### Definition
**VAM** allocates where the *regret* of not choosing the cheapest cell is greatest. For each remaining row and column, the **penalty** is the difference between the two smallest costs. Pick the row/column with the largest penalty, allocate as much as possible to its cheapest cell, cross out the satisfied row or column, recompute, repeat. Ties in penalty: choose the row/column whose cheapest cell allows the largest allocation. VAM typically gives a start that is optimal or within a few per cent, so it is the method examiners and practitioners prefer.

### Example
Working example:

| Step | Penalties (rows P1-P3, then cols D1-D4) | Largest | Allocation |
|---|---|---|---|
| 1 | 2, 2, 4 \| 1, 3, 3, 2 | Row P3 (4) | (P3,D4) cost 5: 60; D4 done |
| 2 | 2, 3, 5 \| 1, 3, 3 | Row P3 (5) | (P3,D2) cost 9: 20; P3 done |
| 3 | 2, 3 \| 1, 6, 3 | Col D2 (6) | (P1,D2) cost 6: 60; D2 done |
| 4 | 2, 4 \| 1, 3 | Row P2 (4) | (P2,D1) cost 9: 70; D1 done |
| 5 | only column D3 left | n/a | (P2,D3) 50, (P1,D3) 40 |

VAM solution: (P1,D2)=60, (P1,D3)=40, (P2,D1)=70, (P2,D3)=50, (P3,D2)=20, (P3,D4)=60; six cells. Cost: $360+400+630+650+180+300 = 2{,}520$. This equals the LP optimum (verified by SciPy and PuLP), so MODI will confirm optimality immediately. VAM is *not* guaranteed optimal: it usually is on small textbook cases.

### In the news
See news box. The VAM idea (give priority to the destination that would lose most if denied its cheapest source) is the intuition behind why a network planner does not simply send every order to the nearest FC.

### Interview angle
> [!question] How it is asked
> "Use VAM to get an initial solution. Why is it better than NWC and least cost?"

> [!tip] Strong answer includes
> - Penalty definition (second-lowest minus lowest) and why it measures regret
> - Correct bookkeeping when a row or column is crossed out (recompute penalties)
> - Compare costs: NWC 2,870 → LCM 2,620 → VAM 2,520 (optimal)
> - State it is a heuristic: confirm with the optimality test

---
## 5. Optimality Test: MODI (u–v) Method, Full Worked Example
> 🔴 Tier 1 · _Key points:_ u + v = c on basic cells; opportunity cost on empty cells; loop; θ

### Definition
**MODI (Modified Distribution) method** tests a basic feasible solution:
1. Assign potentials $u_i$ (rows) and $v_j$ (columns) so that $u_i+v_j=c_{ij}$ for every **basic** (allocated) cell; set one potential (usually $u_1$) to 0.
2. For every **non-basic** cell compute the **opportunity cost** $\Delta_{ij}=c_{ij}-u_i-v_j$ (the cost change per unit if that cell is brought into the plan).
3. If all $\Delta_{ij}\ge 0$ the solution is optimal (for a minimisation). Otherwise pick the most negative cell, trace the **closed loop** (alternate + and − corners through basic cells), set $\theta=$ minimum allocation on the − corners, add θ at + corners and subtract at − corners; one basic cell goes to zero and leaves.
4. Repeat. Each iteration cost change is $\theta\times\Delta_{ij}$.

The $u_i$ and $v_j$ are the **dual variables** of the transportation LP (sub-topic 13).

### Example
Start from the NWC solution (cost 2,870): basic cells (1,1)=70, (1,2)=30, (2,2)=50, (2,3)=70, (3,3)=20, (3,4)=60.

**Iteration 0.** With $u_1=0$: $v_1=8$, $v_2=6$; $u_2=12-6=6$; $v_3=13-6=7$; $u_3=16-7=9$; $v_4=5-9=-4$. Opportunity costs for empty cells: (1,3)=10−0−7=**3**; (1,4)=9−0+4=13; (2,1)=9−6−8=**−5**; (2,4)=7−6+4=5; (3,1)=14−9−8=**−3**; (3,2)=9−9−6=**−6**. Most negative: (3,2) = −6. Loop: (3,2)+ → (3,3)− → (2,3)+ → (2,2)−. θ = min(20, 50) = 20. Cost change $20\times(-6)=-120$: **2,750**.

**Iteration 1.** Allocation: (1,1)=70, (1,2)=30, (2,2)=30, (2,3)=90, (3,2)=20, (3,4)=60. Recompute: $u=(0,6,3)$, $v=(8,6,7,2)$. Opportunity costs: (1,3)=3; (1,4)=7; (2,1)=9−6−8=**−5**; (2,4)=7−6−2=−1; (3,1)=3; (3,3)=6. Enter (2,1): loop (2,1)+ → (2,2)− → (1,2)+ → (1,1)−; θ = min(30, 70) = 30; change $30\times(-5)=-150$: **2,600**.

**Iteration 2.** Allocation: (1,1)=40, (1,2)=60, (2,1)=30, (2,3)=90, (3,2)=20, (3,4)=60. $u=(0,1,3)$, $v=(8,6,12,2)$. Opportunity costs: (1,3)=10−12=**−2**; (1,4)=7; (2,2)=5; (2,4)=4; (3,1)=3; (3,3)=1. Enter (1,3): loop (1,3)+ → (1,1)− → (2,1)+ → (2,3)−; θ = min(40, 90) = 40; change $40\times(-2)=-80$: **2,520**.

**Iteration 3 (test).** Allocation: (1,2)=60, (1,3)=40, (2,1)=70, (2,3)=50, (3,2)=20, (3,4)=60. $u=(0,3,3)$, $v=(6,6,10,2)$. Opportunity costs of empty cells: (1,1)=2, (1,4)=7, (2,2)=3, (2,4)=2, (3,1)=5, (3,3)=3, all positive: **optimal, cost ₹2,520 (hundreds)**, all costs positive so the optimum is unique. Dual check: $\sum s_iu_i+\sum d_jv_j = 100(0)+120(3)+80(3)+70(6)+80(6)+90(10)+60(2) = 600+1{,}920 = 2{,}520$ ✓.

Reading the answer: Nashik sends 60 to D2 and 40 to D3; Pune sends 70 to D1 and 50 to D3; Nagpur sends 20 to D2 and 60 to D4. Every iteration was computed and verified in Python; the path 2,870 → 2,750 → 2,600 → 2,520 matches the sum of θ × Δ.

### In the news
See news box. MODI's $u,v$ numbers are the dual prices that large network models report: the "price" of supply at a node. Almost-linear-time min-cost flow algorithms replace this pivoting for huge graphs, but the economics (reduced cost = cost minus potentials) are identical.

### Interview angle
> [!question] How it is asked
> "Here is a feasible shipping plan. How do you know whether it is optimal, and what do you do if it is not?"

> [!tip] Strong answer includes
> - Compute $u,v$ on basic cells, opportunity cost on empty cells, apply the sign rule (all ≥ 0 means optimal for min)
> - Trace the loop, θ rule, update; show the cost drop = θ × Δ
> - Interpret $u,v$ as shadow prices of supply/demand
> - Note a zero opportunity cost on an empty cell signals alternate optimal plans

---
## 6. Stepping-Stone Method and Degeneracy
> 🔴 Tier 1 · _Key points:_ Loop-by-loop evaluation; add ε when occupied cells < m+n−1

### Definition
**Stepping-stone** evaluates each empty cell by tracing its loop and adding the signed costs around it (+, −, +, − at corners). The net is exactly the opportunity cost that MODI gets from $u,v$. Stepping-stone is conceptually simple but laborious; MODI computes all of them from potentials, so use MODI in exams for more than a 3×3.

**Degeneracy** in transportation: fewer than $m+n-1$ occupied cells. It arises (a) in the initial solution when a row and a column are exhausted by the same allocation, or (b) mid-iteration when two or more − corners tie for the minimum θ. Fix: put an infinitesimally small **ε** (treated as 0 in the final answer) in an unoccupied cell so that the occupied cells remain a spanning tree (no closed loop among them); then continue as normal. Degeneracy does not change the optimal cost; it only prevents $u,v$ from being solved for all rows and columns.

### Example
**Stepping-stone check.** Take the NWC solution and evaluate empty cell (3,2): loop (3,2)+9, (3,3)−16, (2,3)+13, (2,2)−12: net = 9−16+13−12 = **−6**: moving one unit onto this cell saves ₹6, the same as the MODI value computed in sub-topic 5.

**Degeneracy case.** Supplies (40, 60), demands (40, 30, 30). NWC: (1,1) = min(40,40) = 40 exhausts both S1 and D1 simultaneously. Only 3 cells get filled ((1,1)=40, (2,2)=30, (2,3)=30), but $m+n-1=4$. Add ε at (1,2) or (2,1), whichever keeps the occupied cells loop-free, then proceed. If the ε sits at a − corner, θ = ε and the cell leaves with no change in cost (a degenerate pivot).

### In the news
See news box. In practice network LPs are highly degenerate (many ties), and modern network-simplex codes handle it with perturbation, which is the same ε idea.

### Interview angle
> [!question] How it is asked
> "What is degeneracy in a transportation problem and how do you resolve it?"

> [!tip] Strong answer includes
> - Definition: occupied cells < m+n−1; causes: simultaneous exhaustion of row and column, tie in θ
> - Fix with ε allocation placed so that no closed loop is formed among occupied cells
> - Final cost unaffected; ε is dropped from the reported plan
> - Be able to state that MODI cannot find all $u,v$ without it

---
## 7. Unbalanced, Prohibited-Route and Maximisation Variants
> 🔴 Tier 1 · _Key points:_ Dummy row/column, big-M, convert max to min

### Definition
- **Unbalanced (supply ≠ demand):** if supply > demand add a **dummy destination** absorbing the excess at cost 0 (or at storage/holding cost); if demand > supply add a **dummy source** at cost 0 (or at a shortage penalty, such as lost-sales cost). Dummy flows are idle capacity or unmet demand.
- **Prohibited route** (strike, road closure, regulation): give that cell a very large cost $M$ so it is never chosen.
- **Maximisation** (profit or revenue matrix): either subtract every entry from the largest entry and minimise, or apply the optimality test with reversed signs.
- **Capacitated lanes / minimum quantities:** need LP/min-cost-flow formulation, not the basic transportation tableau.

### Example
**Unbalanced.** Keep supplies (100, 120, 80) = 300 but let demands be (70, 80, 60, 60) = 270: add a dummy destination D5 with demand 30 and zero costs. Optimum (LP check): total cost **₹2,130 (hundreds)**; Nashik: 60 to D2 and 40 to D3; Pune: 70 to D1, 20 to D3 and **30 to the dummy** (30 units of Pune capacity stay idle); Nagpur: 20 to D2 and 60 to D4. Dropping 30 units of demand at D3 saved ₹390 versus the balanced case, and the dummy flow tells the planner where the cheapest place to leave capacity idle is (here Pune).

**Unmet demand with a penalty.** If demand exceeds supply by 30 and each unmet unit costs ₹20 in lost margin, add a dummy source (supply 30) with cost 20 to every destination; then the optimiser decides which destination goes short.

**Maximisation.** A 2×2 profit matrix [[40, 25], [30, 35]]: subtract each from 40 to get [[0, 15], [10, 5]]; the minimum assignment is the diagonal (0+5 = 5), so maximum profit = 2×40 − 5 = **75** (40 + 35). The off-diagonal plan earns 25 + 30 = 55.

### In the news
See news box. Adding 20 fulfilment centres raises capacity by roughly 50%; whenever capacity in a region exceeds demand, a model needs the dummy-destination logic (idle capacity), and in peak sale weeks, when demand exceeds capacity, a shortage penalty for late or lost orders matters.

### Interview angle
> [!question] How it is asked
> "Supply is 300 units but demand is only 270. How would you model it?"

> [!tip] Strong answer includes
> - Add a dummy destination with demand 30 at zero (or holding) cost; interpret flows to the dummy as unused capacity
> - For shortages, dummy source with a penalty cost reflecting lost sales
> - Prohibited lanes via big-M; maximisation by converting to minimisation
> - Mention that ties in dummy allocations indicate flexibility

---
## 8. The Assignment Problem and the Hungarian Method
> 🔴 Tier 1 · _Key points:_ One-to-one matching; row/column reduction; cover zeros with minimum lines

### Definition
The **assignment problem** matches $n$ agents to $n$ tasks one-to-one at minimum total cost (time, ₹ or distance). It is a transportation problem with all supplies and demands equal to 1, but is so degenerate that a specialised algorithm is better: the **Hungarian method** (Kuhn, 1955, based on Kőnig and Egerváry). Steps:

1. **Row reduction:** subtract each row's minimum from that row.
2. **Column reduction:** subtract each column's minimum from that column.
3. **Cover** all zeros with the **minimum number of horizontal/vertical lines**. If the number of lines = $n$, an optimal assignment exists among the zeros: choose a set of $n$ zeros with exactly one in every row and column.
4. Otherwise let $\theta$ = smallest uncovered entry: subtract it from uncovered entries, add it to entries covered twice (line intersections), leave singly-covered entries; go to step 3.

Why it works: subtracting a constant from a row or column changes every complete assignment's cost by the same amount, so the optimal assignment is unchanged; once a zero-cost complete assignment exists on the reduced matrix, it is optimal because costs cannot be negative.

### Example
Assign four delivery partners (rows A–D) to four routes (columns 1–4); entries are minutes:

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| A | 15 | 26 | 25 | 12 |
| B | 19 | 27 | 23 | 28 |
| C | 26 | 10 | 27 | 8 |
| D | 23 | 16 | 25 | 15 |

**Row reduction** (subtract 12, 19, 8, 15): rows become (3, 14, 13, 0), (0, 8, 4, 9), (18, 2, 19, 0), (8, 1, 10, 0). **Column reduction** (column minima 0, 1, 4, 0): matrix

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| A | 3 | 13 | 9 | 0 |
| B | 0 | 7 | 0 | 9 |
| C | 18 | 1 | 15 | 0 |
| D | 8 | 0 | 6 | 0 |

Minimum lines to cover all zeros: column R4, row B, and column R2 or row D: **3 lines < 4**, so adjust. Take lines on column R4, row B and column R2. Smallest uncovered entry: 3 (A–R1). Subtract 3 from uncovered entries (rows A, C, D × columns R1, R3), add 3 at the intersections (B–R2 and B–R4), leave others:

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| A | 0 | 13 | 6 | 0 |
| B | 0 | 10 | 0 | 12 |
| C | 15 | 1 | 12 | 0 |
| D | 5 | 0 | 3 | 0 |

Now 4 lines are needed (cover column R1, column R4, then B–R3 and D–R2 still need covering), so a complete zero assignment exists: **A–R1 (15), B–R3 (23), C–R4 (8), D–R2 (16) = 62 minutes** (verified with SciPy and brute-force over all 24 permutations). Selecting zeros: C has zeros only at R4, forcing C–R4; then D's remaining zero is R2; B's remaining zero is R3; A takes R1.

### In the news
See news box. Matching gig workers, riders or drivers to tasks in batches is an assignment problem on a bipartite graph; and the 2022 almost-linear min-cost-flow result is the theoretical engine for solving such matchings at massive scale.

### Interview angle
> [!question] How it is asked
> "Five analysts, five projects, a time matrix: who goes where? Explain the Hungarian method and what happens if lines < n."

> [!tip] Strong answer includes
> - Row then column reduction; minimum line cover; check lines = n
> - If not, subtract the smallest uncovered entry from uncovered cells, add it at intersections
> - Final answer must be one zero per row and column; read the cost from the original matrix
> - Know variants: maximisation, unbalanced (add dummy row/column), prohibited assignment (big-M)

---
## 9. Assignment Variants and Related Problems
> 🔴 Tier 1 · _Key points:_ Max, unbalanced, restricted, multiple optima; scheduling and TSP link

### Definition
- **Maximisation:** convert profit matrix to opportunity-loss matrix by subtracting every entry from the largest entry in the matrix (or row-wise, same result), then run Hungarian as a minimisation.
- **Unbalanced** ($m \ne n$): add dummy rows or columns of zeros (or of idle/shortage costs) until square. Assigning an agent to a dummy task means the agent is left idle.
- **Prohibited assignments:** big-M or very large cost.
- **Multiple optimal solutions:** when after the final adjustment there are several ways to choose zeros; choose by secondary criteria (skills, continuity, fairness).
- **One agent, several tasks / one task, several agents:** replicate the agent or task into copies (e.g., a driver who can do two routes becomes two rows).
- **Link to other models:** assigning jobs to machines is a scheduling problem ([[021 Scheduling & Sequencing]]); the TSP is an assignment problem plus the requirement that the result be a single tour (subtour elimination: [[148 Operations Research - Network Models & Integer Programming]]).

### Example
Five tasks, four workers, minimise time: add a dummy worker whose cost is 0 for every task, making the matrix 5×5. The task matched to the dummy is the one left unstaffed (or outsourced), and the algorithm picks the task whose absence hurts total time least. The final answer has the form "four real assignments plus one task to the dummy".

**Maximisation example (Python-verified).** Profit matrix [[40, 25], [30, 35]] (₹ thousand per day for partner–city pairs). Row/col conversion gives [[0, 15], [10, 5]]; optimal assignment is the diagonal with total profit 75 (the other plan gives 55).

**Counting check.** For $n=4$ there are $4! = 24$ possible assignments; for $n=15$ there are $15! \approx 1.3\times 10^{12}$. The Hungarian method solves any $n$ in $O(n^3)$ time, so enumeration is never the answer.

### In the news
See news box. Matching problems grow from 4×4 in a classroom to very large instances in a real network, which is where the near-linear-time flow algorithms in the news box matter.

### Interview angle
> [!question] How it is asked
> "You have 6 sales reps and 5 territories with a revenue matrix. How do you assign?"

> [!tip] Strong answer includes
> - Add a dummy territory (zero revenue) to square the matrix; maximisation converted to minimisation
> - The rep matched to the dummy is the one left without a territory (or redeployed)
> - Mention constraints that break pure assignment (skill gaps, travel, continuity with clients), solved by adding restricted cells with big-M
> - Time complexity $O(n^3)$ versus $n!$ enumeration

---
## 10. Transshipment Problems
> 🔴 Tier 1 · _Key points:_ Intermediate nodes; node-balance constraints; buffer-stock trick

### Definition
In a **transshipment problem**, goods may pass through intermediate nodes (cross-docks, hubs, ports, transhipment warehouses) before reaching destinations. Model it as a **minimum-cost network flow**:

$$\min \sum_{(i,j)} c_{ij}x_{ij} \quad\text{s.t.}\ \underbrace{\sum_j x_{ij}-\sum_k x_{ki}}_{\text{net outflow}} = \begin{cases} s_i & \text{source}\\ -d_i & \text{destination}\\ 0 & \text{transshipment node}\end{cases}$$

(or "≤ $s_i$" for sources when supply exceeds demand). Textbook trick: convert to an ordinary transportation problem by making every node both a source and a destination with a **buffer** $B$ equal to the total supply (or total demand): each node gets supply = its own supply + $B$ and demand = its own demand + $B$; shipping from a node to itself costs 0.

### Example
Plants: Pune (supply 150), Nagpur (100). Hubs: Hyderabad, Bhopal. Customers: C1 (80), C2 (90), C3 (80). Unit costs (₹): Pune→Hyd 6, Pune→Bhopal 9, Nagpur→Hyd 8, Nagpur→Bhopal 4; Hyd→C1/C2/C3 = 5/7/9; Bhopal→C1/C2/C3 = 8/4/5; direct plant→customer: Pune 14/16/18, Nagpur 17/15/12.

- **Direct shipping only:** optimum 3,500 (Pune: 80 to C1, 70 to C2; Nagpur: 20 to C2, 80 to C3).
- **With hubs allowed:** optimum **2,670**: Pune→Hyd 80, Pune→Bhopal 70, Nagpur→Bhopal 100, Hyd→C1 80, Bhopal→C2 90, Bhopal→C3 80. Check: $480+630+400+400+360+400 = 2{,}670$.
- **Saving:** 830 (23.7%) from using consolidation hubs, because the cheapest customer legs run via hubs. A second plan, Pune→Hyd 150 and Nagpur→Bhopal 100 with Hyd→C1 80, Hyd→C2 70, Bhopal→C2 20, Bhopal→C3 80, also costs 2,670: alternate optima.

(All values from a Python/PuLP min-cost-flow model.) The buffer formulation yields the same answer from an enlarged transportation table in which all seven nodes appear as both sources and destinations.

### In the news
See news box. Sort centres and delivery stations can be modelled as the transshipment nodes between fulfilment centres and customers: Amazon's addition of six sort centres and 150 delivery stations adds exactly this hub layer to the network, where consolidation can lower the per-unit linehaul cost.

### Interview angle
> [!question] How it is asked
> "Would it be cheaper to ship directly from plants to customers or through a hub? How would you decide?"

> [!tip] Strong answer includes
> - Formulate as min-cost flow with node balance (net outflow) constraints
> - Compare direct vs hub networks numerically (here ₹3,500 vs ₹2,670)
> - Mention hub costs not in the model: handling, dwell time, inventory pooling, extra transit time and damages
> - Link to cross-docking and network design ([[009 Logistics & Distribution]], [[113 Network Design & Facility Location Modelling]])

---
## 11. Applications: Network Design, Allocation and Sourcing
> 🔴 Tier 1 · _Key points:_ Plant–DC–customer flows, order allocation, workforce matching

### Definition
Where these models are used:
- **Distribution planning:** monthly plant-to-DC and DC-to-market flows, with lane capacities, minimum loads, and service constraints.
- **Network design:** evaluate scenarios (open/close a warehouse, add a plant) by solving a transportation model per scenario, then compare total cost. Choosing *which* facilities to open is a binary/MIP extension ([[148 Operations Research - Network Models & Integer Programming]]).
- **Sourcing / order allocation:** suppliers as sources, plants as destinations, with unit cost including freight and duty (landed cost: [[002 Procurement & Strategic Sourcing]]).
- **Assignment uses:** drivers to routes, engineers to service calls, staff to shifts, machines to jobs, sales reps to territories, bids to contractors.
- **Limits:** single product, linear cost, no economies of scale, no inventory or time dimension; multi-product and multi-period variants use LP/MIP.

### Example
Scenario analysis with the working example (base optimum 2,520). **Scenario A:** move 20 units of capacity from Nagpur to Nashik (supplies 120, 120, 60). Re-solving gives **2,460**, a saving of 60 = 20 × 3, which equals the difference of the potentials $u_3-u_1=3$ from the MODI table. **Scenario B:** move the same 20 units from Nagpur to Pune (100, 140, 60): cost stays **2,520**, because $u_3-u_2=0$. So the potentials already tell the planner where extra capacity is worth building: Nashik, not Pune.

**Lane thresholds.** An unused lane enters the plan only if its cost falls by more than its opportunity cost. Nashik→D1 has $\Delta=2$: at a cost of 6 it is indifferent (cost stays 2,520), at 5 it enters and carries 40 units (total 2,480). Pune→D4 also has $\Delta=2$: at cost 4 it carries 50 units (total 2,470). All figures verified by re-solving the LP.

### In the news
See news box. Amazon's ₹2,800 crore investment is an exercise in network design: more capacity at non-metro nodes shortens the "last leg" and shifts the optimal flows away from metro hubs. Expect a case-interview question on whether adding a node in Raipur/Ranchi/Varanasi lowers total cost, which one answers by comparing network costs with and without the node, plus service-level gains.

### Interview angle
> [!question] How it is asked
> "Should we open a new DC in the East? How would you quantify the benefit?"

> [!tip] Strong answer includes
> - Build a cost model for with/without the DC: transport (transportation LP), facility fixed cost, inventory, service level
> - Report both cost delta and service impact (delivery time, coverage within X hours)
> - Flag assumptions: demand allocation, lane rates, cost linearity
> - Use scenario/sensitivity analysis rather than a point estimate

---
## 12. Solver and Python Formulation
> 🔴 Tier 1 · _Key points:_ SUMPRODUCT layout; flow variables; ≤ supply, ≥ demand

### Definition
**Excel Solver** (see [[077 Solver, Goal Seek & What-If Analysis]]): lay out a shipment grid (decision cells, initially 0), row totals, column totals, and a cost grid. Objective cell: `=SUMPRODUCT(CostGrid, ShipGrid)`. Constraints: row total `<=` supply (or `=` when balanced), column total `>=` demand (or `=`). Settings: Simplex LP, non-negative. For assignment, make the grid binary (each row sum = 1, each column sum = 1), which Solver handles as LP because the constraint matrix is totally unimodular, so integer constraints are optional but harmless.

**Python (PuLP)** (see [[068 Operations-Specific Python (PuLP, SimPy)]]):

```python
import pulp
plants = ["Nashik", "Pune", "Nagpur"]; dcs = ["D1", "D2", "D3", "D4"]
supply = dict(zip(plants, [100, 120, 80])); demand = dict(zip(dcs, [70, 80, 90, 60]))
cost = {"Nashik": [8, 6, 10, 9], "Pune": [9, 12, 13, 7], "Nagpur": [14, 9, 16, 5]}
c = {(p, d): cost[p][j] for p in plants for j, d in enumerate(dcs)}

m = pulp.LpProblem("transport", pulp.LpMinimize)
x = pulp.LpVariable.dicts("ship", c.keys(), lowBound=0)
m += pulp.lpSum(c[k] * x[k] for k in c)
for p in plants: m += pulp.lpSum(x[p, d] for d in dcs) <= supply[p]
for d in dcs:    m += pulp.lpSum(x[p, d] for p in plants) >= demand[d]
m.solve(pulp.PULP_CBC_CMD(msg=0))
print(pulp.LpStatus[m.status], pulp.value(m.objective))   # Optimal 2520.0
```

### Example
Running the code prints `Optimal 2520.0` with flows Nashik→D2 60, Nashik→D3 40, Pune→D1 70, Pune→D3 50, Nagpur→D2 20, Nagpur→D4 60, matching MODI. For assignment problems use `scipy.optimize.linear_sum_assignment(cost_matrix)` (pass `maximize=True` for profit): on the 4×4 delivery matrix of sub-topic 8 it returns A–R1, B–R3, C–R4, D–R2 with total 62. Practical pitfalls: forgetting to balance (infeasible when supply < demand with `=` constraints), mixing units, and not rounding results.

### In the news
See news box. Open-source solvers and libraries now give an analyst at a start-up the same transportation engine large networks use; scale (millions of lanes) is where the specialised network-simplex and almost-linear algorithms matter.

### Interview angle
> [!question] How it is asked
> "Set up a transportation problem in Excel Solver: how do you do it, and how do you check the result?"

> [!tip] Strong answer includes
> - Grid layout, SUMPRODUCT objective, row/column constraint formulas, non-negativity, Simplex LP
> - Use `<=` for supply and `>=` for demand when unbalanced; `=` when balanced
> - Check totals, integer flows, binding constraints, and compare with VAM/MODI on a small case
> - Mention sensitivity: dual values per node as the value of extra capacity or the cost of extra demand

---
## 13. ⭐ Advanced: Duality, Min-Cost Flow Generality and Network Simplex
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Dual of the transportation problem:** $\max \sum_i s_iu_i + \sum_j d_jv_j$ subject to $u_i+v_j \le c_{ij}$ (with signs as per the convention used for the supply/demand rows). The MODI potentials are exactly these dual variables, and the opportunity cost $c_{ij}-u_i-v_j$ is the dual slack. Complementary slackness: basic cells have zero opportunity cost.
- **Dual price interpretation:** $v_j-u_i$ is the maximum price difference the network would accept between destination $j$ and source $i$; if the actual price gap exceeds the lane cost, there is an arbitrage incentive to expand that lane.
- **Generalisation:** transportation ⊂ transshipment ⊂ **min-cost network flow** ⊃ shortest path, max flow, assignment. Add arc capacities and you get the **capacitated transportation problem**. Specialised **network simplex** exploits the spanning-tree structure of basic solutions and is much faster than general simplex.
- **Totally unimodular matrices:** integer supply/demand data mean extreme points are integral, which is why LP relaxations of transportation and assignment problems are already integral (no branch-and-bound needed).
- **Beyond:** multi-commodity flow (products share lane capacity) loses integrality; fixed-charge flows (open/close lanes) become MIPs.

### Example
Dual verification in the working example: potentials $u=(0,3,3)$, $v=(6,6,10,2)$ satisfy $u_i+v_j \le c_{ij}$ for all cells (the smallest slack is 2) and give dual objective $100(0)+120(3)+80(3)+70(6)+80(6)+90(10)+60(2) = 2{,}520$, equal to the primal cost, which proves optimality without trusting the pivoting. Reading the potentials (differences matter, since the balanced problem fixes them only up to a constant): $v_3-v_2=4$, so shifting one unit of demand from D2 to D3 raises the optimal cost by ₹4 (re-solving gives 2,524); $u_2-u_1=3$, so moving one unit of supply from Nashik to Pune raises cost by ₹3 (re-solving gives 2,523).

### In the news
See news box. The $m^{1+o(1)}$ min-cost flow result is the theoretical foundation for every item in this note; practical solvers (network simplex, cost scaling) are what Amazon-style network optimisers run.

### Interview angle
> [!question] How it is asked
> "Is the transportation problem an LP? Why do you always get integer answers, and what changes when lane capacities or fixed costs enter?"

> [!tip] Strong answer includes
> - It is an LP with a network (totally unimodular) structure, so integer data give integer vertices
> - Duals are node prices $u_i, v_j$; MODI is simplex specialised for this structure
> - Fixed charges, minimum lot sizes and multi-commodity flows break integrality: use MIP
> - Cite the family: shortest path, max flow, assignment, transshipment are all special cases of min-cost flow ([[148 Operations Research - Network Models & Integer Programming]])
