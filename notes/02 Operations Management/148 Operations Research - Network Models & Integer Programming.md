---
tags: [operations-management, tier2]
area: Operations Management
topic: "Operations Research - Network Models & Integer Programming"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Operations Research - Network Models & Integer Programming

⬅ [[147 Operations Research - Transportation, Assignment & Transshipment]] · [[_Index - Operations Management|Operations Management]] · [[149 Queueing Theory & Waiting-Line Analysis]] ➡

> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Network Basics and the Shortest-Path Problem (Dijkstra)]]
2. [[#2. Shortest-Path Variants and Other Algorithms]]
3. [[#3. Minimum Spanning Tree (Kruskal and Prim)]]
4. [[#4. Maximum Flow and the Max-Flow Min-Cut Theorem]]
5. [[#5. Minimum-Cost Flow]]
6. [[#6. Travelling Salesman Problem and Tour Heuristics]]
7. [[#7. Vehicle Routing and the Clarke–Wright Savings Algorithm]]
8. [[#8. Integer and Binary Programming: Formulation and Why LP Rounding Fails]]
9. [[#9. Branch and Bound (Worked Example)]]
10. [[#10. Knapsack and Capital-Budgeting Problems]]
11. [[#11. Facility Location with Binary Variables]]
12. [[#12. Set Covering, Location Covering and Logical Constraints]]
13. [[#13. Goal Programming and Multi-Objective Trade-offs]]
14. [[#14. ⭐ Advanced: Complexity, Metaheuristics and Solver Practice]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Dijkstra's 1956 shortest-path algorithm is beaten in theory, and route optimisation pays at scale
> **"Breaking the sorting barrier" for shortest paths (STOC 2025 Best Paper; announced 29 April 2025).** A team led by Xinkai Shu (Max Planck Institute for Informatics) with Ran Duan, Jiayi Mao, Longhui Yin (Tsinghua University) and Xiao Mao (Stanford) won the Best Paper Award at the ACM Symposium on Theory of Computing, presented 23 June 2025 in Prague. Their directed single-source shortest-path algorithm shrinks the "frontier" recursively using a hybrid of Dijkstra and Bellman–Ford ideas, avoiding the sorting overhead (the log n factor per operation) that limits Dijkstra's algorithm, which dates from 1956. It is an asymptotic result for theory; road-routing engines still lean on preprocessing tricks. ([Max Planck Institute for Informatics](https://www.mpi-inf.mpg.de/news/detail/stoc-best-paper-award-how-to-find-the-shortest-path-faster))
>
> **UPS "dynamic ORION" (full rollout by July 2021).** UPS's route-optimisation system, tested since 2003, was upgraded to re-plan routes during the day; Supply Chain Dive reported it saves 2–4 miles per driver per day on top of the roughly 8-mile reduction achieved by the original ORION, with 97% of the ORION van fleet covered at the time. Pick-up requests arriving mid-day are inserted into the best route automatically: a live vehicle-routing problem. ([Supply Chain Dive](https://www.supplychaindive.com/news/ups-orion-route-planning-analytics-data-logistics/601673/))
>
> **Amazon India expands its network (14 September 2026).** 20 new fulfilment centres, 6 sort centres and 150 last-mile delivery stations, investment above ₹2,800 crore; seven new fulfilment centres and all six sort centres are in non-metro cities, with first facilities in Raipur, Ranchi and Varanasi. Every such node is a facility-location and network-flow decision. ([Amazon India](https://www.aboutamazon.in/news/operations/amazon-india-operations-network-expansion-biggest))
>
> **Max flow and min-cost flow in almost-linear time (arXiv 2022, FOCS 2022).** Chen, Kyng, Liu, Peng, Probst Gutenberg and Sachdeva compute exact maximum and minimum-cost flows in $m^{1+o(1)}$ time on a graph with $m$ edges. ([arXiv 2203.00671](https://arxiv.org/pdf/2203.00671v1))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Network Basics and the Shortest-Path Problem (Dijkstra)
> 🟠 Tier 2 · _Key points:_ Nodes, arcs, weights; Dijkstra's greedy settling; non-negative weights

### Definition
A **network** (graph) has **nodes** (cities, depots, tasks) and **arcs/edges** (roads, lanes, precedence links) with attributes: length, cost, time or capacity. The **shortest-path problem** finds a minimum-total-weight route between a source and a destination (or from the source to all nodes).

**Dijkstra's algorithm** (weights ≥ 0): keep a tentative distance $d(v)$ for each node (0 for the source, ∞ for others); repeatedly *settle* the unsettled node with the smallest $d$, then relax its neighbours: $d(v)\leftarrow\min\{d(v),\ d(u)+w_{uv}\}$. A settled label is final because no later path can be shorter when all weights are non-negative. With a binary heap the running time is $O((m+n)\log n)$.

### Example
Illustrative hub network (distances in km): A–B 4, A–C 2, B–C 1, B–D 5, C–D 8, C–E 10, D–E 2, D–F 6, E–F 7, A–F 12. Source A.

| Step | Settle | Updated labels |
|---|---|---|
| 0 | A (0) | B 4, C 2, F 12 |
| 1 | C (2) | B 3 (via C), D 10, E 12 |
| 2 | B (3) | D 8 (via B) |
| 3 | D (8) | E 10, F stays 12 (8+6 = 14 is worse) |
| 4 | E (10) | F stays 12 (10+7 = 17) |
| 5 | F (12) | done |

Shortest distances from A: C 2, B 3, D 8, E 10, F 12. Routes: A–C–B–D–E for E (length 2+1+5+2 = 10), and the *direct* A–F link for F (12), not the longer path through D (14). The shortest-path tree has total weight 2+1+5+2+12 = 22 (checked with NetworkX). Read the route by backtracking predecessors from the destination.

### In the news
See news box. The STOC 2025 paper is a reminder that even this textbook algorithm has theoretical room to improve; in practice, Dijkstra with preprocessing (contraction hierarchies, A\* with landmarks) drives routing.

### Interview angle
> [!question] How it is asked
> "Find the shortest route from the plant to every warehouse. Walk me through Dijkstra on this network, and tell me when it fails."

> [!tip] Strong answer includes
> - Maintain tentative labels, settle the smallest, relax neighbours; show a table
> - State the non-negative-weights requirement and why it matters (settled labels are final)
> - Name Bellman–Ford for negative weights and Floyd–Warshall for all pairs
> - Link to practical routing: travel *time* edge weights that change with traffic, not just distance

---
## 2. Shortest-Path Variants and Other Algorithms
> 🟠 Tier 2 · _Key points:_ Bellman–Ford, Floyd–Warshall, A*, critical path as longest path

### Definition
| Algorithm | Handles | Idea | Complexity |
|---|---|---|---|
| Dijkstra | Non-negative weights, single source | Greedy settling | $O((m+n)\log n)$ |
| Bellman–Ford | Negative weights; detects negative cycles | Relax all edges $n-1$ times | $O(nm)$ |
| Floyd–Warshall | All pairs; negative weights without negative cycles | DP: allow intermediate nodes $1..k$ | $O(n^3)$ |
| A* | Single pair with a heuristic | Dijkstra guided by an admissible estimate (e.g., straight-line distance) | Often far fewer nodes |
| DAG shortest/longest path | Acyclic graphs | Process in topological order | $O(n+m)$ |

**Project networks:** the critical path is the *longest* path in a precedence DAG ([[039 Scheduling Tools (CPM-PERT-Gantt)]]); longest path is easy on a DAG but NP-hard in general graphs. **Applications:** route and ETA computation, network-latency routing, currency arbitrage detection (negative cycle in log-rates), minimum-cost replacement schedules, supply-chain lead-time minimisation.

### Example
Floyd–Warshall recursion: $d^{(k)}_{ij}=\min\{d^{(k-1)}_{ij},\ d^{(k-1)}_{ik}+d^{(k-1)}_{kj}\}$. On the Dijkstra network, allowing C as an intermediate improves A→B from 4 to 3 (A–C–B) and creates an A→D path of length 10 (A–C–D) where none existed with no intermediates; once B is also allowed, A→D improves to 8 (A–C–B–D). Arbitrage example: convert currencies at rates $r_{ij}$; use weights $-\log r_{ij}$; a negative cycle means a profitable loop, which Bellman–Ford detects.

### In the news
See news box. Almost every logistics API call (ETA, nearest hub) is a shortest-path query; the 2025 STOC result improves the worst-case theory for sparse directed graphs, while production systems answer queries in microseconds via precomputation.

### Interview angle
> [!question] How it is asked
> "A ride-hailing app has to compute ETAs for millions of queries a day. How would you structure the shortest-path computation?"

> [!tip] Strong answer includes
> - Don't run Dijkstra from scratch per query: preprocess (contraction hierarchies, landmarks) and cache
> - Use time-dependent travel-time weights and live traffic updates
> - Mention A* with admissible heuristics for single-pair queries
> - Know the algorithm families and their assumptions (negative weights, all-pairs)

---
## 3. Minimum Spanning Tree (Kruskal and Prim)
> 🟠 Tier 2 · _Key points:_ Connect all nodes at minimum total length; no cycles; n−1 edges

### Definition
A **spanning tree** connects all $n$ nodes with $n-1$ edges and no cycle; the **minimum spanning tree (MST)** has least total weight. Uses: designing cable, pipeline or road networks, connecting plants to a utility grid, clustering (single-linkage), network backbones.

- **Kruskal:** sort edges by weight; add the next edge unless it forms a cycle (check with union–find); stop at $n-1$ edges. $O(m\log m)$.
- **Prim:** grow a tree from any node; repeatedly add the cheapest edge connecting the tree to a new node. $O(m\log n)$ with a heap.
- **Cut property:** the cheapest edge crossing any partition of the nodes belongs to some MST; **cycle property:** the heaviest edge on any cycle is not needed (for distinct weights).

### Example
Same network. **Kruskal:** sorted edges: B–C 1 ✓, A–C 2 ✓, D–E 2 ✓, A–B 4 ✗ (cycle A–C–B), B–D 5 ✓ (joins {A,B,C} with {D,E}), D–F 6 ✓ (adds F), E–F 7 ✗, A–F 12 ✗, C–D 8 ✗, C–E 10 ✗. Five edges, **MST length = 1+2+2+5+6 = 16**.

**Prim from A:** A–C 2; C–B 1; B–D 5; D–E 2; D–F 6: total 16, the same tree as Kruskal. Compare with the shortest-path tree from A (total 22, uses A–F 12): the MST minimises *total network length*, the shortest-path tree minimises *each node's distance from the source*: they differ in general, and conflating them is a classic interview slip.

### In the news
See news box. Network build-out (new sort centres, delivery stations) is a connectivity-versus-cost problem: MST gives the minimum-length backbone, but real logistics networks add redundancy and capacity beyond a tree.

### Interview angle
> [!question] How it is asked
> "Which algorithm would you use to connect 10 villages with the least cable, and how does it differ from shortest path?"

> [!tip] Strong answer includes
> - MST (Kruskal or Prim), with the cycle-avoidance step explained and total length computed
> - Difference: MST minimises total length; shortest-path tree minimises distances from the source
> - Caveat: a tree has no redundancy; add edges for reliability (a cost-vs-resilience trade-off)
> - Mention Steiner trees (extra junction points) can beat the MST

---
## 4. Maximum Flow and the Max-Flow Min-Cut Theorem
> 🟠 Tier 2 · _Key points:_ Augmenting paths, residual graph, min cut = max flow

### Definition
Given a directed network with arc capacities $u_{ij}$, a source $s$ and sink $t$, the **maximum-flow problem** sends as much flow as possible subject to capacity and conservation at intermediate nodes. **Ford–Fulkerson:** repeatedly find an augmenting path in the **residual graph** (forward residual = capacity − flow; backward residual = flow that can be cancelled), push the bottleneck, and stop when no path exists. Choosing the shortest augmenting path each time is **Edmonds–Karp** ($O(nm^2)$). An **$s$–$t$ cut** $(S,T)$ splits the nodes with $s\in S$, $t\in T$; its capacity is the sum of capacities of arcs from $S$ to $T$.

$$\text{Max-flow Min-cut theorem: }\ \max\text{ flow value}=\min\text{ cut capacity}$$

Integer capacities give integer flows; max flow is also a special LP whose dual is the min cut.

### Example
Network: s→a 10, s→b 8, a→b 5, a→c 7, b→d 10, c→d 4, c→t 8, d→t 10.
1. Path s–a–c–t: bottleneck min(10, 7, 8) = 7. Flow 7.
2. Path s–b–d–t: bottleneck min(8, 10, 10) = 8. Flow 15.
3. Residual path s–a–b–d–t: s→a has 3 left, a→b 5, b→d 2 left (10−8), d→t 2 left (10−8): bottleneck 2. Flow **17**.
4. From s the reachable set is {s, a, b} (b→d and a→c are saturated); no path to t.

**Min cut:** $S=\{s,a,b\}$, $T=\{c,d,t\}$; arcs from $S$ to $T$: a→c (7) and b→d (10) = **17 = max flow** (verified with NetworkX). The network has more than one minimum cut (for example a→c plus d→t is also 17), so adding capacity pays only where *every* minimum cut is relieved: raising a→c from 7 to 8 lifts the max flow to 18, whereas raising b→d, d→t, c→t or a→b alone changes nothing (all re-solved with NetworkX).

### In the news
See news box. The 2022 almost-linear-time algorithm for max flow and min-cost flow is the headline theory result in this area; in practice, push-relabel and dinic-style codes run on huge graphs.

### Interview angle
> [!question] How it is asked
> "What is the maximum number of containers per day we can move from the port to the inland terminal through this rail and road network, and where is the bottleneck?"

> [!tip] Strong answer includes
> - Model as max flow with capacities; find augmenting paths until none remain
> - Identify the min cut: the bottleneck set of links that limit throughput
> - Explain what to do: add capacity on cut arcs; capacity elsewhere is wasted
> - State the theorem and link to LP duality

---
## 5. Minimum-Cost Flow
> 🟠 Tier 2 · _Key points:_ Supplies, demands, costs and capacities; generalises transportation

### Definition
The **minimum-cost flow problem** sends flow through a network with node supplies/demands $b_i$ (net outflow), arc capacities $u_{ij}$ and unit costs $c_{ij}$ at least cost:

$$\min\sum_{(i,j)}c_{ij}x_{ij}\ \ \text{s.t.}\ \sum_j x_{ij}-\sum_k x_{ki}=b_i,\ \ 0\le x_{ij}\le u_{ij}$$

It generalises transportation, assignment, transshipment ([[147 Operations Research - Transportation, Assignment & Transshipment]]), shortest path (send one unit) and max flow. **Successive shortest path:** repeatedly send flow along the cheapest residual path. **Network simplex** is the standard practical algorithm.

### Example
Send 10 units from S to T: arcs S→A (cap 6, cost 2), S→B (cap 8, cost 5), A→B (cap 3, cost 1), A→T (cap 5, cost 6), B→T (cap 9, cost 3).
- Cheapest path S–A–B–T costs 2+1+3 = 6 per unit, limited by A→B to 3 units: cost 18.
- Next S–A–T costs 8 per unit; S→A has 3 spare units, A→T has room: 3 units, cost 24.
- Then S–B–T costs 8 per unit: 4 units, cost 32.

Total **74** for 10 units (3+3+4). Flows: S→A 6, S→B 4, A→B 3, A→T 3, B→T 7: cost $12+20+3+18+21=74$ (verified with NetworkX). The path costs 6, 8, 8 are the *marginal costs* of the 1st–3rd, 4th–6th, 7th–10th units, so total cost is convex in the amount shipped: each extra unit costs the same or more as cheap capacity is exhausted.

### In the news
See news box. Network-design models for fulfilment networks like Amazon's are min-cost flow models with fixed costs layered on top; the near-linear-time result is the theoretical ceiling for solving the flow part.

### Interview angle
> [!question] How it is asked
> "How does a min-cost flow model differ from a transportation model, and where would you use it?"

> [!tip] Strong answer includes
> - Node balance with transshipment nodes, arc capacities, unit costs
> - Special cases: transportation, assignment, shortest path, max flow
> - Marginal-cost reading: each extra unit uses the next cheapest residual path
> - Practical: add fixed charges or lot sizes and it becomes a MIP

---
## 6. Travelling Salesman Problem and Tour Heuristics
> 🟠 Tier 2 · _Key points:_ NP-hard; nearest neighbour; 2-opt; bounds

### Definition
The **Travelling Salesman Problem (TSP)** finds the shortest closed tour visiting each node exactly once. It is NP-hard: for $n$ cities there are $(n-1)!/2$ distinct tours (symmetric case); 20 cities already give about $6\times10^{16}$. Methods: exact (branch-and-cut, dynamic programming in $O(n^22^n)$), constructive heuristics, and improvement heuristics.

- **Nearest neighbour:** start at the depot, always go to the nearest unvisited node, return home. Simple; typically 20–25% above optimal on random Euclidean instances, but can be much worse.
- **Cheapest/farthest insertion, Christofides:** better constructions (Christofides guarantees ≤ 1.5× optimal for metric TSP).
- **2-opt / Or-opt:** remove two edges and reconnect to uncross the tour, repeat until no improvement.
- **MST lower bound:** a tour minus one edge is a spanning tree, so the optimal tour length ≥ MST length.

### Example
Depot 0 and five customers with distances to the depot (12, 10, 15, 8, 14 for customers 1 to 5) and between customers: 1–2 6, 1–3 20, 1–4 15, 1–5 22, 2–3 14, 2–4 11, 2–5 17, 3–4 21, 3–5 9, 4–5 12.

**Nearest neighbour:** 0→4 (8), 4→2 (11), 2→1 (6), 1→3 (20), 3→5 (9), 5→0 (14): **68**. **Optimal (by enumeration of all 120 tours):** 0→1→2→3→5→4→0 = 12+6+14+9+12+8 = **61**. The heuristic is 11.5% above the optimum, caused by the forced 20-km link 1→3 late in the tour: the classic "greedy ends badly" pattern, and 2-opt would fix it.

### In the news
See news box. UPS's ORION solves a huge, constrained version of this problem per driver per day; the general lesson is that near-optimal routes found fast, and re-planned as conditions change, are worth more than optimal routes found too slowly.

### Interview angle
> [!question] How it is asked
> "A delivery executive has 12 stops. Is it realistic to find the best route by trying all of them? What would you do instead?"

> [!tip] Strong answer includes
> - 11!/2 ≈ 2 crore routes for 12 stops is feasible for a computer but not for 25+ stops: growth is factorial
> - Heuristics: nearest neighbour then 2-opt; or use a solver (OR-Tools)
> - Quality bound: compare to the MST lower bound
> - Real constraints: time windows, traffic, capacity: that's VRP

---
## 7. Vehicle Routing and the Clarke–Wright Savings Algorithm
> 🟠 Tier 2 · _Key points:_ Savings = d0i + d0j − dij; merge routes within capacity

### Definition
The **Vehicle Routing Problem (VRP)** generalises TSP: several vehicles with capacity $Q$ serve customers with demands $q_i$ from a depot, minimising total distance/cost. Variants: time windows (VRPTW), pickup–delivery, heterogeneous fleet, multi-depot, split deliveries.

**Clarke–Wright savings (1964):**
1. Start with one dedicated route per customer (depot–$i$–depot).
2. Compute savings for each pair: $s_{ij}=d_{0i}+d_{0j}-d_{ij}$ (distance saved by serving $i$ and $j$ on one route).
3. Sort savings in descending order. For each pair, merge the two routes if $i$ and $j$ are **end points** of different routes (adjacent to the depot) and the combined load $\le Q$.
4. Stop when no feasible merge remains.

### Example
Use the TSP data and demands $q=(4,3,5,6,4)$, vehicle capacity **15**. Savings: (3,5) = 15+14−9 = **20**; (1,2) = 12+10−6 = **16**; (2,3) = 10+15−14 = 11; (4,5) = 8+14−12 = **10**; (2,5) = 7; (2,4) = 7; (1,3) = 7; (1,4) = 5; (1,5) = 4; (3,4) = 2.

| Pair (saving) | Decision |
|---|---|
| (3,5) 20 | Merge: route [3,5], load 9 |
| (1,2) 16 | Merge: route [1,2], load 7 |
| (2,3) 11 | Reject: load 16 > 15 |
| (4,5) 10 | Merge: [4,5,3] → route 4–5–3, load 15 |
| (2,5), (1,3), (2,4), (1,4), (1,5), (3,4) | 2 and 5 are now interior (or load would exceed 15): skip or reject |

Result: Route A 0–1–2–0 = 12+6+10 = 28; Route B 0–4–5–3–0 = 8+12+9+15 = 44; **total 72**, versus 118 for five single-customer trips (saving 46 = 20+16+10). Brute-force enumeration over all splits gives an optimum of 72, so the savings heuristic is optimal here (not guaranteed in general). Sweep and cluster-first/route-second methods are alternatives; modern solvers use metaheuristics (tabu search, adaptive large neighbourhood search).

### In the news
See news box. UPS's dynamic ORION is an industrial VRP/TSP engine, and last-mile networks like Amazon's 150 new delivery stations create thousands of such route problems every day.

### Interview angle
> [!question] How it is asked
> "You have 30 deliveries and 4 vans: how would you plan routes by hand, and when would you use software?"

> [!tip] Strong answer includes
> - Savings algorithm steps, with a worked example or at least the savings formula
> - Constraints to flag: capacity, time windows, driver hours, vehicle type, return-to-depot
> - Heuristics give good, fast answers; exact methods don't scale; metaheuristics are the production standard
> - Link to transport management and cost-to-serve ([[125 Transportation Management Deep Dive]], [[009 Logistics & Distribution]])

---
## 8. Integer and Binary Programming: Formulation and Why LP Rounding Fails
> 🟠 Tier 2 · _Key points:_ Pure, mixed, binary; LP relaxation; modelling logic with 0/1 variables

### Definition
An **integer program (IP)** is an LP with some or all variables required to be integers. Types: **pure IP**, **mixed-integer (MIP)** (some continuous), **binary/0-1** (decisions: open/close, select/reject). The **LP relaxation** drops integrality; for maximisation, $Z_{LP}\ge Z_{IP}$ (a bound), and rounding the LP optimum may be infeasible or poor.

**Standard binary modelling devices:**
- Select at most $k$ of $n$: $\sum x_i\le k$; exactly one: $\sum x_i=1$.
- If A then B (prerequisite): $x_A\le x_B$.
- Fixed charge: cost $F\,y+c\,x$ with $x\le M y$ ($y=1$ if activity is used).
- Either-or constraints: $a x\le b+M(1-y)$ and $a' x\le b'+My$.
- Contingent or mutually exclusive projects: $x_1+x_2\le 1$.

Unlike LP, IP has no simple optimality test; solvers use **branch-and-bound/cut/price**.

### Example
$$\max\ 5x_1+4x_2\ \ \text{s.t.}\ 6x_1+4x_2\le 24,\ x_1+2x_2\le 6,\ x_1,x_2\ge0\text{ integer}$$

LP relaxation optimum: $x=(3,\ 1.5)$, $Z=21$. Rounding down gives (3, 1) with $Z=19$; the true integer optimum is **(4, 0) with $Z=20$** (check: $6\cdot4=24\le24$, $4\le6$). So rounding left value on the table and gave a point that was not optimal. Rounding *up* (3, 2) violates $x_1+2x_2\le6$ (3+4 = 7). Integer solutions are generally *not* near the rounded LP point, especially in 0/1 problems.

### In the news
See news box. Network and facility decisions (which of Amazon's 20 new fulfilment centres to build where) are binary variables: IP is the formal language of "open or not".

### Interview angle
> [!question] How it is asked
> "Why can't you just round the LP solution for an integer problem?"

> [!tip] Strong answer includes
> - Rounding can break feasibility or give a poor solution; give a small example (3, 1.5 → 4, 0)
> - LP relaxation gives a bound; gap measures how good the incumbent is
> - Binary variables model decisions and logical conditions
> - Name branch-and-bound and what MIP solvers do

---
## 9. Branch and Bound (Worked Example)
> 🟠 Tier 2 · _Key points:_ Branch on fractional variable; bound with LP; prune

### Definition
**Branch-and-bound** searches a tree of LP relaxations. At each node: solve the LP; if infeasible, **prune**; if its value is no better than the best known integer solution (the **incumbent**), prune by **bound**; if the solution is integral, update the incumbent; otherwise **branch** on a fractional variable $x_j=f$: create the subproblems $x_j\le\lfloor f\rfloor$ and $x_j\ge\lceil f\rceil$. Stop when no open nodes remain. Variants: best-first vs depth-first search, strong branching, cutting planes (branch-and-cut).

### Example
Continue the problem from sub-topic 8.
- **Root:** LP gives $(3,\,1.5)$, $Z=21$. Branch on $x_2$.
- **Node 1 ($x_2\le1$):** LP gives $(3.33,\,1)$, $Z=20.67$. Branch on $x_1$.
  - **Node 1a ($x_1\le3$):** $(3,1)$, $Z=19$: integral: incumbent 19.
  - **Node 1b ($x_1\ge4$):** $(4,0)$, $Z=20$: integral: **new incumbent 20**.
- **Node 2 ($x_2\ge2$):** LP gives $(2,2)$, $Z=18$ (integral, but) **bound 18 < 20**, prune.

All nodes closed: **optimal $x=(4,0)$, $Z=20$**, proved without enumerating the integer grid. Because LP values are valid upper bounds, once the best open bound ≤ incumbent, the incumbent is optimal. Gap = (best bound − incumbent)/incumbent: right after incumbent 20 was found, the best bound among open nodes was still the root value 21 (Node 2 unsolved), a gap of $(21-20)/20=5\%$. (All LPs solved with SciPy.)

### In the news
See news box. Commercial MIP solvers (CPLEX, Gurobi, CBC, HiGHS, OR-Tools) are branch-and-cut engines with powerful presolve and heuristics; network-design models of the scale of an Amazon expansion are MIPs solved with such tools.

### Interview angle
> [!question] How it is asked
> "Explain branch-and-bound using a small integer program, and how you know when to stop."

> [!tip] Strong answer includes
> - Solve relaxation, branch on a fractional variable, bound and prune
> - Show the tree and the incumbent updating
> - Stopping rule: all nodes pruned, or the gap is small enough for the business (e.g., under 1%)
> - Practical advice: set a time limit and accept the best incumbent with its gap

---
## 10. Knapsack and Capital-Budgeting Problems
> 🟠 Tier 2 · _Key points:_ 0/1 knapsack; value density; LP relaxation; dynamic programming

### Definition
The **0/1 knapsack** chooses a subset of items to maximise value subject to one capacity: $\max\sum v_ix_i$ s.t. $\sum w_ix_i\le W$, $x_i\in\{0,1\}$. Business forms: **capital budgeting** (projects with costs and NPVs within a budget: [[109 Valuation Basics (NPV, IRR, DCF)]], [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]), cargo loading, shelf-space allocation, selecting SKUs for a limited warehouse.

- **Greedy by value density** $v_i/w_i$ is optimal for the *fractional* knapsack (that is the LP relaxation) but not for 0/1.
- **Dynamic programming:** $f(k)=\max\{f(k),\ f(k-w_i)+v_i\}$ over $k=W..w_i$, in $O(nW)$ pseudo-polynomial time.
- Packing generalisations: bin packing, multiple knapsack (loading trucks: [[140 Packaging, Unitisation & Load Optimisation]]).

### Example
Budget ₹80 lakh. Projects (cost, NPV in ₹ lakh): P1 (45, 8), P2 (30, 6), P3 (50, 9), P4 (20, 4), P5 (10, 3).

Density: P5 0.30, P2 0.20, P4 0.20, P3 0.18, P1 0.178. **LP relaxation:** take P5, P2, P4 (cost 60, NPV 13) and 40% of P3 (cost 20, NPV 3.6): bound **16.6**. **Integer optimum (enumeration and DP agree):** P3 + P4 + P5, cost 50+20+10 = 80, NPV 9+4+3 = **16**. Greedy by density would take P5, P2, P4 (NPV 13, ₹20 lakh unused, and neither P1 nor P3 fits), a 19% shortfall: so density is a heuristic, not an optimiser. Gap between bound and optimum: $(16.6-16)/16 = 3.75\%$.

### In the news
See news box. Choosing which sites to build within a fixed capex envelope (Amazon's announced ₹2,800 crore for 2026) is a budgeting knapsack: rank candidates by value density, then solve the 0/1 version to use the budget well.

### Interview angle
> [!question] How it is asked
> "You have a ₹80 lakh budget and five candidate projects. How do you choose, and is picking the highest NPV-per-rupee projects optimal?"

> [!tip] Strong answer includes
> - Binary formulation with one budget constraint (and logical rules if projects are linked)
> - Density ranking is a heuristic; 0/1 integrality can beat it (₹16 lakh vs ₹13 lakh in the example)
> - Mention the LP bound and DP for small instances
> - Add real-world complications: multiple periods, risk, dependencies, strategic must-haves

---
## 11. Facility Location with Binary Variables
> 🟠 Tier 2 · _Key points:_ Fixed-charge models; y (open) and x (assign); uncapacitated vs capacitated

### Definition
**Uncapacitated fixed-charge facility location (UFL):** choose which candidate sites $i$ to open ($y_i\in\{0,1\}$) and assign customers $j$ ($x_{ij}$ = fraction of $j$'s demand served from $i$) to minimise fixed plus service cost:

$$\min\sum_i F_iy_i+\sum_i\sum_j c_{ij}x_{ij}\quad\text{s.t.}\ \sum_i x_{ij}=1\ \forall j,\ \ x_{ij}\le y_i,\ \ y_i\in\{0,1\}$$

The linking constraint $x_{ij}\le y_i$ stops service from a closed site. Extensions: **capacitated** ($\sum_j d_jx_{ij}\le K_iy_i$), **$p$-median** (open exactly $p$ sites to minimise demand-weighted distance), **$p$-centre** (minimise the maximum distance), **covering** location (sub-topic 12). Related heuristic methods (centre of gravity, load-distance) are in [[019 Facility Layout & Location]] and [[113 Network Design & Facility Location Modelling]].

### Example
Three candidate warehouses with annual fixed costs (₹ lakh) 30, 32, 25 and four customer regions. Service cost (₹ lakh per year) from site to region:

| | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| W1 | 10 | 40 | 50 | 34 |
| W2 | 45 | 12 | 36 | 48 |
| W3 | 50 | 46 | 10 | 12 |

Evaluate every subset (each region served by its cheapest open site): W3 alone = 25+118 = 143; W1 alone = 30+134 = 164; W2 alone = 32+141 = 173; W1+W2 = 62+92 = 154; W2+W3 = 57+79 = 136; W1+W3 = 55+72 = **127**; all three = 87+44 = 131. **Open W1 and W3: total ₹127 lakh; R1, R2 from W1 and R3, R4 from W3.** Opening W2 as well would add 32 of fixed cost but save only 28 of service cost (R2 would move from W1's 40 to W2's 12), so it is not worth it. The binary model solved with PuLP/CBC agrees: cost 127, $y=(1,0,1)$; here the LP relaxation is already integral (also 127), which is common but not guaranteed.

### In the news
See news box. Amazon's September 2026 network expansion (20 FCs, 6 sort centres, 150 delivery stations, ₹2,800 crore) is a large facility-location decision: fixed costs of capacity versus the transport and speed gains from placing nodes close to demand, especially in non-metro cities.

### Interview angle
> [!question] How it is asked
> "A retailer wants to add warehouses. How would you decide how many and where?"

> [!tip] Strong answer includes
> - Fixed-charge trade-off: fixed cost per site versus transport/service savings, with binary open/close variables
> - Data: demand by region, lane costs, site costs, capacity, service time targets
> - Evaluate multiple scenarios (3, 4, 5 sites) and show the cost curve, not a single answer
> - Include non-cost criteria: service level, risk, talent, regulations (GST state structure: [[227 GST & Indirect Tax for Supply Chains]])

---
## 12. Set Covering, Location Covering and Logical Constraints
> 🟠 Tier 2 · _Key points:_ Cover every demand point with minimum sites; greedy heuristic

### Definition
**Set covering:** choose the cheapest collection of sets (candidate depots, service centres, shifts) so that every element (demand zone, time slot) is covered at least once.

$$\min\sum c_jx_j\quad\text{s.t.}\ \sum_{j:\,i\in S_j}x_j\ge1\ \ \forall i,\ \ x_j\in\{0,1\}$$

Related: **set packing** (each element at most once), **set partitioning** (exactly once; crew pairing in airlines, cutting-stock patterns). **Maximal covering location** picks $p$ sites to cover as much demand as possible within a service radius. NP-hard; the **greedy heuristic** (pick the set covering the most uncovered elements) guarantees a $\ln n$-factor approximation.

### Example
Zones 1–6. Candidate service depots and the zones each covers within the response-time limit: D1 {1,2,3}, D2 {2,4}, D3 {3,4,5}, D4 {1,5,6}, D5 {2,5,6}. Each depot costs the same, so minimise their number.

Two depots cannot cover six zones here (the largest covers three; the best pair D1+D3 covers {1,2,3,4,5} and misses 6; D1+D4 misses 4). Enumeration over all subsets shows the minimum is **3 depots**, with six optimal triples such as {D1, D3, D4} or {D2, D3, D4}. Greedy: pick D1 (covers 3 new zones), then D3 (covers 4 and 5), then D4 (covers 6): {D1, D3, D4}: optimal in this instance, though greedy is not optimal in general. With unequal depot costs, the objective becomes cost-weighted and the best set can change.

### In the news
See news box. Delivery stations in non-metro cities (Amazon's 150 new stations) are classic covering decisions: every pin code must be reachable within a promised delivery time, and the model asks for the cheapest set of sites that does so.

### Interview angle
> [!question] How it is asked
> "We want same-day delivery to every pin code in a city: how do you choose the minimum number of delivery stations?"

> [!tip] Strong answer includes
> - Covering formulation with coverage sets defined by a drive-time threshold
> - Binary variables per candidate site; objective = number of sites or total cost
> - Heuristic (greedy) for quick estimates, MIP for the final design
> - Trade-off curve: coverage % versus number of sites (diminishing returns)

---
## 13. Goal Programming and Multi-Objective Trade-offs
> 🟠 Tier 2 · _Key points:_ Deviation variables d−, d+; preemptive priorities; weights

### Definition
**Goal programming (GP)** handles several, possibly conflicting goals by turning each into a soft constraint with **deviation variables**: $a_jx+d_j^--d_j^+=g_j$, where $d^-\ge0$ is under-achievement and $d^+\ge0$ is over-achievement of goal $g_j$. The objective minimises unwanted deviations only (e.g., $d^-$ for a minimum-profit goal, $d^+$ for a cost ceiling).

- **Preemptive (lexicographic) GP:** goals are ranked $P_1\succ P_2\succ\dots$; optimise $P_1$, then $P_2$ without worsening $P_1$, etc.
- **Weighted GP:** minimise $\sum w_jd_j$, with weights reflecting importance and scaled by goal units.
- **Hard constraints** (capacity, safety, legal limits) remain strict; goals are the wish-list.

Contrast with LP (one objective) and with other multi-criteria approaches such as AHP and Pareto frontiers.

### Example
Pump plant ([[146 Operations Research - Linear Programming]] constraints: machining $2x_1+x_2\le100$, assembly $x_1+x_2\le80$, finishing $x_1\le40$). Goals in priority order: **G1:** profit $300x_1+200x_2\ge17{,}000$; **G2:** P2 output $x_2\ge70$ (a customer commitment); **G3:** P1 output $x_1\ge30$.

- **Priority 1:** minimise $d_1^-$: achievable to 0 (for example (30, 40) earns 9,000+8,000 = 17,000).
- **Priority 2:** keep $d_1^-=0$, minimise $d_2^-$: achievable to 0 with **(10, 70)**: profit 3,000+14,000 = 17,000, machining 90 ≤ 100, assembly 80 ≤ 80.
- **Priority 3:** with G1 and G2 met, minimise $d_3^-$: the best is still $x_1=10$, a shortfall of **20 units** against the P1 goal.

Final plan (10, 70): meets the profit and P2 goals, misses the P1 goal by 20. The pure-profit LP optimum (20, 60) earns ₹18,000 but misses G2 by 10 units: GP makes the value judgement explicit by giving up ₹1,000 of profit to honour a customer commitment (all steps solved with SciPy).

### In the news
See news box. Large-network planning rarely has one objective: Amazon-style expansions trade cost, speed (same-day coverage), resilience and workforce goals, which GP or weighted-sum / Pareto-frontier models formalise.

### Interview angle
> [!question] How it is asked
> "Cost, service level and carbon all matter. How do you optimise a network with multiple objectives?"

> [!tip] Strong answer includes
> - Options: weighted sum, lexicographic/goal programming, ε-constraint (optimise one, bound the others), Pareto frontier
> - Show the trade-off curve to executives, not a single "optimal" point
> - Handle units with normalisation and make priorities explicit
> - Keep hard constraints (safety, law) separate from goals

---
## 14. ⭐ Advanced: Complexity, Metaheuristics and Solver Practice
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Complexity classes.** Shortest path, MST, max flow, min-cost flow and assignment are **polynomial** (the "easy" network problems); TSP, VRP, general IP, set covering and facility location are **NP-hard**. The 2022 almost-linear flow algorithms and the 2025 STOC shortest-path result move the polynomial frontier; they do not change NP-hardness.
- **Approximation guarantees:** Christofides (1.5 for metric TSP), greedy set cover ($\ln n$), 2-approximation MST-doubling for TSP. In practice, heuristics routinely beat their worst-case guarantees.
- **Metaheuristics:** simulated annealing, tabu search, genetic algorithms and adaptive large neighbourhood search; they scale to thousands of stops and support messy constraints but give no optimality proof.
- **Cuts and strong formulations:** tighter formulations (e.g., aggregated vs disaggregated linking constraints in facility location) shrink the LP gap dramatically; solvers add valid inequalities automatically (branch-and-cut).
- **Decomposition:** Benders (split binary location from continuous flows), column generation (VRP and crew pairing), Lagrangian relaxation.
- **Practice:** Google OR-Tools (routing and CP-SAT), PuLP/Pyomo with CBC or HiGHS, commercial Gurobi/CPLEX/Xpress ([[068 Operations-Specific Python (PuLP, SimPy)]]); set a MIP gap (e.g., 1%) and time limit; always compare against a simple baseline.

### Example
MIP gap reporting: a solver reports incumbent ₹127 lakh and best bound ₹120 lakh: gap $(127-120)/127=5.5\%$ (on the incumbent), meaning the true optimum lies between ₹120 and ₹127 lakh; if the business needs ≤ 2%, either run longer, strengthen the formulation, or accept ₹127 lakh. For the 5-customer VRP above, there are $5!=120$ orderings and up to 16 ways to split each, so enumeration gave optimum 72 instantly; at 50 customers the count exceeds $10^{64}$ orderings, so heuristics are mandatory.

### In the news
See news box. The headline algorithms there are from the "easy" polynomial side of the divide; the commercial value (UPS, Amazon) comes from handling the NP-hard side well enough, fast enough.

### Interview angle
> [!question] How it is asked
> "Why is routing 'hard' while shortest path is 'easy', and what do you do when the exact method is too slow?"

> [!tip] Strong answer includes
> - Polynomial vs NP-hard with an example of each; combinatorial explosion in tour counts
> - Practical stack: good heuristic (savings, nearest neighbour) + local search + solver with a time limit
> - Use bounds and gaps to judge quality
> - State that a quick, robust, explainable solution that drivers accept beats a fragile theoretical optimum
