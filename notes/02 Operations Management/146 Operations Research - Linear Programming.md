---
tags: [operations-management, tier1]
area: Operations Management
topic: "Operations Research - Linear Programming"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Operations Research - Linear Programming

⬅ [[022 Maintenance Management (TPM-RCM)]] · [[_Index - Operations Management|Operations Management]] · [[147 Operations Research - Transportation, Assignment & Transshipment]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. What LP Is: Assumptions and Formulation Steps]]
2. [[#2. Product-Mix Formulation]]
3. [[#3. Blending and Diet Problems]]
4. [[#4. Graphical Method]]
5. [[#5. Special Cases: Infeasible, Unbounded, Alternate Optima, Degenerate, Redundant]]
6. [[#6. Simplex Method: Standard Form and Tableau Logic]]
7. [[#7. Simplex Worked Iterations (Pump Problem)]]
8. [[#8. Big-M, Two-Phase Method and Minimisation Problems]]
9. [[#9. Duality]]
10. [[#10. Shadow Prices and Reduced Costs]]
11. [[#11. Sensitivity Analysis and Ranging]]
12. [[#12. LP in Excel Solver and Python (PuLP)]]
13. [[#13. Interpreting and Communicating LP Results to Managers]]
14. [[#14. ⭐ Advanced: Interior-Point Methods, Complexity and LP Relaxations]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): The 1947 simplex method gets a new theoretical guarantee
> **Optimal smoothed analysis of the simplex method (preprint April 2025; presented at FOCS in December 2025).** Sophie Huiberts and Eleon Bach tightened the Spielman–Teng (2001) "smoothed analysis" result, which had explained why the simplex method, invented by George Dantzig in the 1940s, is fast in practice despite exponential worst cases. Quanta Magazine reports that the 2001 polynomial bounds carried exponents as high as 30, and that the new work gives much tighter guarantees and proves that, within this analysis model, the bound cannot be improved. ([Quanta Magazine, 13 Oct 2025](https://www.quantamagazine.org/researchers-discover-the-optimal-way-to-optimize-20251013/))
>
> **"By-the-book" analysis (arXiv, October 2025; v2 June 2026).** Bach, Black, Huiberts and Kafer model what real solvers actually do (input scaling, feasibility tolerances, bound perturbation) and prove an expected polynomial number of pivots for a two-phase simplex under those assumptions, narrowing the gap between theory and the practice of commercial LP codes. ([arXiv 2510.21613](https://arxiv.org/pdf/2510.21613))
>
> **Reliance exits Russian crude (20 November 2025).** India's largest private refiner stopped Russian-origin imports at Jamnagar ahead of tighter US and EU sanctions; its long-term Rosneft contract had supplied nearly 500,000 barrels per day, and it bought about 1 million barrels of Kuwaiti crude as a replacement. A crude-slate change of this kind is a textbook refinery LP re-run: feed prices, yields and product-price vectors change, and the plan re-optimises. ([OilPrice](https://oilprice.com/Latest-Energy-News/World-News/Indias-Reliance-Industries-Officially-Shuts-the-Door-on-Russian-Crude-Ahead-of.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. What LP Is: Assumptions and Formulation Steps
> 🔴 Tier 1 · _Key points:_ Decision variables, objective, constraints, non-negativity; four assumptions

### Definition
**Linear programming (LP)** chooses values of continuous **decision variables** to maximise or minimise a **linear objective** subject to **linear constraints** (≤, ≥, =) and non-negativity. General form:

$$\max\ Z = c^{T}x \quad \text{s.t.}\quad Ax \le b,\ x \ge 0$$

Formulation recipe (the part interviewers actually test): (1) define the decision variables with units (e.g., $x_1$ = units of pump P1 per week); (2) write the objective in ₹ (usually contribution margin, not profit, since fixed costs do not change with the plan: see [[110 Cost Accounting for Operations]]); (3) list every scarce resource as a constraint (machine hours, labour, material, demand cap, storage, policy); (4) add non-negativity; (5) check units on every row.

Four assumptions, each worth naming in an interview:

| Assumption | Meaning | Where it breaks |
|---|---|---|
| Proportionality | Contribution and resource use scale linearly | Volume discounts, setup times, learning curves |
| Additivity | Totals are sums of individual contributions | Product cannibalisation, shared set-ups |
| Divisibility | Fractional values allowed | Trucks, machines, people (need integer programming: [[148 Operations Research - Network Models & Integer Programming]]) |
| Certainty | Coefficients are known constants | Demand, yield, price volatility (use sensitivity analysis, scenarios or stochastic programming) |

LP is the workhorse behind [[005 Production & Operations Planning]], aggregate planning ([[153 Aggregate Planning Models & Workforce Strategy]]), blending, network design ([[113 Network Design & Facility Location Modelling]]) and the transportation family ([[147 Operations Research - Transportation, Assignment & Transshipment]]).

### Example
Spotting the formulation error: a manager writes "maximise profit = 300 x₁ + 200 x₂ − ₹50,000 rent". The ₹50,000 is a constant, so it shifts $Z$ but never changes which plan is optimal. Drop it from the objective and subtract it afterwards. Another classic error: constraining *percentages* directly. "Protein at least 20% of the batch" becomes the linear row $0.08M + 0.45S \ge 0.20(M+S)$, or equivalently $0.08M+0.45S \ge 200$ when the batch is fixed at 1,000 kg.

### In the news
See news box. LP is a 1940s technique, yet 2025's research on why the simplex method is fast shows that it is still the engine inside commercial solvers. Reliance's crude-slate change is the same formulation pattern: crude grades as variables, distillation capacity and product specifications as constraints, margin as objective.

### Interview angle
> [!question] How it is asked
> "A plant makes three products on shared machines. How would you decide the weekly production plan, and what would you need to know first?"

> [!tip] Strong answer includes
> - Variables, objective (contribution margin per unit), constraints (each scarce resource), non-negativity
> - Data needed: unit margins, resource usage per unit, capacities, market limits
> - State the assumptions and say which one is most doubtful in this plant
> - Mention that the *solution* (shadow prices, ranging) matters more than the plan itself

---
## 2. Product-Mix Formulation
> 🔴 Tier 1 · _Key points:_ Max contribution; machine hours, assembly, finishing

### Definition
The **product-mix problem** decides how much of each product to make when products compete for limited resources. It is the standard first LP and the template for most plant-planning cases.

Running example used through this note (all figures weekly): a Pune pump maker produces **P1** (contribution ₹300 per unit) and **P2** (₹200 per unit). Resource use per unit and availability:

| Resource | P1 | P2 | Available |
|---|---|---|---|
| Machining (hours) | 2 | 1 | 100 |
| Assembly (hours) | 1 | 1 | 80 |
| Finishing (hours) | 1 | 0 | 40 |

$$\max\ Z = 300x_1 + 200x_2$$
$$2x_1 + x_2 \le 100,\quad x_1 + x_2 \le 80,\quad x_1 \le 40,\quad x_1, x_2 \ge 0$$

Each row has a clear interpretation: row 1 is the machining-hour budget; row 3 happens to involve only P1 because only P1 needs the finishing bay. Adding **demand caps** ($x_2 \le D_2$), **minimum commitments** ($x_1 \ge 10$ for a key customer) or **policy rows** (P2 share of volume at least 30%) uses the same pattern.

### Example
Solved (graphically in sub-topic 4, by simplex in sub-topic 7, verified with PuLP in sub-topic 12): **make 20 of P1 and 60 of P2, for $Z$ = ₹18,000 per week.** Machining: $2(20)+60 = 100$ (fully used), assembly: $20+60 = 80$ (fully used), finishing: $20 \le 40$ (20 hours idle). The bottlenecks are therefore machining and assembly; adding finishing capacity would be wasted money, and that insight is worth more than the plan.

### In the news
See news box. Refinery planners solve a product-mix LP of this exact shape every day, with crude grades as the resource side and gasoline/diesel/ATF/petcoke yields as the product side. When Reliance switched crude sources in November 2025, the "resource" coefficients changed while the structure stayed the same.

### Interview angle
> [!question] How it is asked
> "You have a product-mix LP solution that leaves one resource unused. What does that tell you, and what would you do?"

> [!tip] Strong answer includes
> - Slack on a constraint means it is not binding: more of that resource has zero marginal value (shadow price 0)
> - Focus capex or overtime on the binding constraints; quantify using shadow prices
> - Flag that unused capacity may be a result of the product-mix, so re-check if demand or margins shift
> - Link to Theory of Constraints thinking about bottlenecks ([[018 Capacity Management & OEE]])

---
## 3. Blending and Diet Problems
> 🔴 Tier 1 · _Key points:_ Minimise cost subject to quality specs; ≥ constraints

### Definition
**Blending (and diet) problems** minimise the cost of mixing ingredients so that the mix meets minimum or maximum quality specifications. Because specs are ratios, convert them to linear form using a fixed batch size or by moving terms to one side. Typical uses: cattle feed, fertiliser grades, cement/steel/oil blending, ration planning, packaged-food recipes.

**Cattle-feed example.** Make a 1,000 kg batch from maize (₹22/kg; 8% protein; 3% fibre) and soya meal (₹48/kg; 45% protein; 6% fibre). The batch needs at least 20% protein (200 kg) and at most 5% fibre (50 kg):

$$\min\ 22M + 48S \quad \text{s.t. } M+S=1000,\ 0.08M+0.45S \ge 200,\ 0.03M+0.06S \le 50$$

Substituting $M = 1000 - S$: protein gives $80 + 0.37S \ge 200 \Rightarrow S \ge 324.3$; fibre gives $30 + 0.03S \le 50 \Rightarrow S \le 666.7$. Cost rises with $S$, so choose the smallest: $S = 324.32$ kg, $M = 675.68$ kg, **cost ₹30,432** (₹30.43/kg). Protein is binding, fibre has slack (actual fibre 4.0%). The protein row's shadow price is about **₹70.27 per extra kg of protein** required.

**Diet example (per person per day, quantities in 100 g units).** Rice: ₹5, 7 g protein, 350 kcal. Dal: ₹12, 22 g protein, 340 kcal. Requirement: protein ≥ 55 g, energy ≥ 2,000 kcal:

$$\min\ 5r + 12d \quad \text{s.t. } 7r+22d \ge 55,\ 350r+340d \ge 2000$$

Both constraints bind: $r = 4.756$ (476 g rice), $d = 0.987$ (99 g dal), **cost ₹35.62** per day. Shadow prices: ₹0.470 per extra gram of protein and ₹0.0049 per extra kcal. Real diet LPs add fibre, fat and micronutrient rows plus palatability caps (e.g., no more than 150 g of dal), which the pure-cost optimum otherwise ignores.

### Example
Sensitivity read-out for managers: if the protein spec rises from 20% to 21% (210 kg), cost rises by about $10 \times 70.27 = ₹703$, i.e., ₹0.70 per kg of feed. If soya meal's price rises from ₹48 to ₹60, the optimal *mix* does not change (the protein spec fixes the soya quantity at its minimum) but cost rises by $324.32 \times 12 = ₹3,892$. With a fixed batch size the mix would change only if soya became cheaper per kg than maize (below ₹22), because then the optimiser would use as much of it as the fibre limit allows.

### In the news
See news box. Crude blending in refining is the industrial version of this problem: blend components must meet density, sulphur and octane specs, and the slate changes when sanctions or prices change. (Non-linear blending, such as octane with interactions, needs non-linear or successive-LP methods.)

### Interview angle
> [!question] How it is asked
> "A feed company wants the cheapest feed that meets protein and fibre norms. How would you formulate and solve it, and what happens when the soya price spikes?"

> [!tip] Strong answer includes
> - Variables as kg of each ingredient; specs expressed as linear rows (fix batch size or use ratio constraints)
> - Minimisation with ≥ rows: needs Big-M or two-phase in simplex, or just use Solver
> - Shadow price of the protein spec and ranging of ingredient prices
> - Practical caveats: ingredient availability caps, minimum inclusion rates, batch-to-batch variability

---
## 4. Graphical Method
> 🔴 Tier 1 · _Key points:_ Feasible region, corner points, iso-profit line

### Definition
With two decision variables, an LP can be solved on a plane. Steps: (1) plot each constraint as a line, shade the feasible side; (2) the intersection of all half-planes is the **feasible region** (a convex polygon); (3) the **Fundamental Theorem of LP**: if an optimum exists, it occurs at a **corner (extreme) point**; (4) evaluate $Z$ at each corner, or slide an **iso-profit line** $300x_1+200x_2 = k$ outward until it last touches the region.

### Example
Corner points of the pump problem (axes plus constraint intersections that satisfy every row):

| Corner | $x_1$ | $x_2$ | $Z = 300x_1+200x_2$ |
|---|---|---|---|
| O | 0 | 0 | 0 |
| A | 40 | 0 | 12,000 |
| B (finishing ∩ machining) | 40 | 20 | 16,000 |
| **C (machining ∩ assembly)** | **20** | **60** | **18,000** |
| D | 0 | 80 | 16,000 |

**Optimum = C: (20, 60), Z = ₹18,000.** The iso-profit line has slope $-300/200 = -1.5$, which lies between the slopes of the machining line ($-2$) and the assembly line ($-1$); that is exactly why C is optimal and why $c_1/c_2$ may range from 1 to 2 before the optimum jumps to B or D (see sub-topic 11). Simplex is the algebraic version of walking O → A → B → C along the edges.

Graph tip for exams: if the iso-profit line is parallel to a binding constraint, the problem has **alternate optima** (sub-topic 5).

### In the news
See news box. Graphs only handle two variables, but they explain what solvers do in thousands of dimensions: simplex moves along edges of a polyhedron, and the 2025 results are about how long such walks take on realistic, slightly noisy data.

### Interview angle
> [!question] How it is asked
> "Solve this two-variable LP graphically and tell me the optimum, then tell me what happens if the profit of P1 doubles."

> [!tip] Strong answer includes
> - Plot constraints, mark feasible region, list all corner points, evaluate $Z$
> - State the optimum and which constraints bind
> - For the "what if", compare the iso-profit slope with constraint slopes: ratio $c_1/c_2 = 600/200 = 3$ is outside [1, 2], so the optimum shifts to B (compute: at B, Z = 600·40+200·20 = 28,000 vs C = 24,000 and A = 24,000)
> - Note that graphical method is for intuition; real problems use Solver or code

---
## 5. Special Cases: Infeasible, Unbounded, Alternate Optima, Degenerate, Redundant
> 🔴 Tier 1 · _Key points:_ How each looks graphically and in a tableau

### Definition
| Case | Graph | Simplex tableau signal | Business meaning |
|---|---|---|---|
| **Infeasible** | No point satisfies all constraints | Artificial variable stays positive at the end of Phase 1 | Requirements conflict (e.g., minimum output exceeds capacity) |
| **Unbounded** | Feasible region open in the improving direction | Entering column has no positive entry (ratio test fails) | Missing constraint: a modelling error, since no real system earns infinite profit |
| **Alternate optima** | Iso-profit line parallel to a binding edge | A non-basic variable has reduced cost exactly 0 in the optimal tableau | Several plans with equal value; pick by secondary criteria |
| **Degenerate** | More constraints meet at a vertex than needed | A basic variable equals 0; ratio-test tie | Can cause stalling or cycling in simplex (rare in practice) |
| **Redundant constraint** | Constraint does not touch the feasible region | Never binds | Can be dropped without changing the answer |

### Example
- **Infeasible:** $x_1+x_2 \le 4$ and $x_1+x_2 \ge 6$ cannot both hold (solver status: infeasible).
- **Unbounded:** $\max x_1+x_2$ s.t. $x_1 - x_2 \le 1$: increasing both variables together is unlimited (solver status: unbounded).
- **Alternate optima:** change pump contributions to ₹200 and ₹200. The objective line is now parallel to the assembly constraint $x_1+x_2=80$, and every point on the edge from (0, 80) to (20, 60) gives $Z$ = ₹16,000. A solver returns one corner; the planner should look at neighbours using the zero reduced cost as a clue.
- **Degenerate:** add a constraint $x_1+2x_2 \le 140$ to the pump problem. At (20, 60) it also binds ($20+120=140$), so three lines pass through one vertex. The solution and Z = ₹18,000 are unchanged, but the basis contains a variable at zero level.

### In the news
See news box. Degeneracy and cycling are why textbook simplex has exponential worst cases, and why practical codes perturb bounds randomly; the 2025 "by-the-book" paper explicitly models such perturbation.

### Interview angle
> [!question] How it is asked
> "Your solver says 'unbounded' for a production plan. What went wrong?"

> [!tip] Strong answer includes
> - Unbounded means a missing or wrongly signed constraint (e.g., forgot capacity, or sign error in a ≤)
> - For "infeasible": find the conflicting rows, relax with slack and penalty to see which constraint is the binding conflict
> - Alternate optima: more than one plan with equal value; use a tie-breaker (stability, lower inventory)
> - Degeneracy: solution is fine; shadow prices may not be unique

---
## 6. Simplex Method: Standard Form and Tableau Logic
> 🔴 Tier 1 · _Key points:_ Slack variables, basic feasible solution, entering/leaving variable

### Definition
The **simplex method** (Dantzig, 1947) moves from one vertex of the feasible polyhedron to an adjacent one with a better objective until none is better. Algebraically:

1. **Standard form:** convert ≤ rows to equalities with **slack** variables ($s \ge 0$), ≥ rows with **surplus** variables (and an artificial variable), keep all RHS ≥ 0.
2. **Basic feasible solution (BFS):** with $m$ equations, set $n-m$ variables to zero (non-basic) and solve for the $m$ basic variables; vertices correspond to BFS.
3. **Entering variable:** the non-basic variable with the most negative entry in the $Z$-row (for a max problem written as $Z - c^Tx = 0$), i.e., the best reduced-cost improvement per unit.
4. **Leaving variable (min-ratio test):** among rows with positive entering-column entry, choose the smallest $\text{RHS}/\text{entry}$, which is the first constraint that becomes tight.
5. **Pivot:** row-reduce so the entering column becomes a unit vector. Repeat until the $Z$-row has no negative entries: optimal.

$$\theta = \min_i \left\{\frac{b_i}{a_{ik}} : a_{ik} > 0\right\}$$

Optimality reading: in the final tableau, the **Z-row entries under slack variables are the shadow prices**, and the entries under non-basic decision variables are reduced costs.

### Example
Pump problem in standard form (slacks $s_1,s_2,s_3$): $2x_1+x_2+s_1=100$, $x_1+x_2+s_2=80$, $x_1+s_3=40$, $Z-300x_1-200x_2=0$. Starting BFS: $x_1=x_2=0$ (the origin), slacks equal the RHS, $Z=0$. The $Z$-row has −300 and −200, so $x_1$ enters (steepest). Ratios: $100/2=50$, $80/1=80$, $40/1=40$, so $s_3$ leaves: we move from O to A (40, 0). Dantzig's "most negative" rule is only a heuristic: other pricing rules (steepest edge) reduce pivots in practice.

### In the news
See news box. The theory of why simplex runs fast, in spite of Klee–Minty cubes where it can visit exponentially many vertices, was the open puzzle behind the 2001 and 2025 smoothed-analysis papers.

### Interview angle
> [!question] How it is asked
> "Explain in plain language how simplex works, and why it never needs to check every corner."

> [!tip] Strong answer includes
> - Moves along edges to better neighbouring vertices; stops when no improving neighbour exists (convexity makes local = global)
> - Names entering variable (largest improvement), leaving variable (min-ratio keeps feasibility)
> - Uses slack variables to turn inequalities into equalities and gives the origin as the starting BFS
> - Mentions worst case is exponential but typical performance is polynomial-like in practice

---
## 7. Simplex Worked Iterations (Pump Problem)
> 🔴 Tier 1 · _Key points:_ Three pivots from the origin to ₹18,000

### Definition
A simplex tableau lists, for each constraint row, the coefficients of all variables and the RHS; the bottom row is the $Z$-row. Basic variables have unit columns. Below, columns are $x_1, x_2, s_1, s_2, s_3 \mid$ RHS (all values computed and checked with Python/SciPy).

### Example
**Tableau 0 (origin, Z = 0):**

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | RHS |
|---|---|---|---|---|---|---|
| $s_1$ | 2 | 1 | 1 | 0 | 0 | 100 |
| $s_2$ | 1 | 1 | 0 | 1 | 0 | 80 |
| $s_3$ | 1 | 0 | 0 | 0 | 1 | 40 |
| $Z$ | −300 | −200 | 0 | 0 | 0 | 0 |

Enter $x_1$; ratios 50, 80, **40** → $s_3$ leaves; pivot on the 1 in row 3.

**Tableau 1 (A: x₁ = 40, Z = 12,000):**

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | RHS |
|---|---|---|---|---|---|---|
| $s_1$ | 0 | 1 | 1 | 0 | −2 | 20 |
| $s_2$ | 0 | 1 | 0 | 1 | −1 | 40 |
| $x_1$ | 1 | 0 | 0 | 0 | 1 | 40 |
| $Z$ | 0 | −200 | 0 | 0 | 300 | 12,000 |

Enter $x_2$; ratios 20, 40, (none) → $s_1$ leaves.

**Tableau 2 (B: x₁ = 40, x₂ = 20, Z = 16,000):** the $Z$-row becomes (0, 0, 200, 0, −100 | 16,000); $s_3$ has −100, so it enters; ratios (none), 20, 40 → $s_2$ leaves.

**Tableau 3 (C, optimal):**

| Basis | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | RHS |
|---|---|---|---|---|---|---|
| $x_2$ | 0 | 1 | −1 | 2 | 0 | 60 |
| $s_3$ | 0 | 0 | −1 | 1 | 1 | 20 |
| $x_1$ | 1 | 0 | 1 | −1 | 0 | 20 |
| $Z$ | 0 | 0 | **100** | **100** | 0 | **18,000** |

No negative entries: optimal. $x_1=20$, $x_2=60$, $s_3=20$ (idle finishing hours), $Z = ₹18{,}000$. The Z-row under $s_1, s_2$ reads **shadow prices ₹100 per machining hour and ₹100 per assembly hour**; the slack column for finishing shows 0. This path O → A → B → C visits exactly the corners in the graphical table.

### In the news
See news box. Real LP codes (CPLEX, Gurobi, HiGHS, CBC) are sophisticated implementations of this very tableau logic, working on a "revised simplex" form with sparse matrices; the "by-the-book" paper analyses the tolerances and perturbations they use.

### Interview angle
> [!question] How it is asked
> "Walk me through one simplex iteration and read off the answer from the final tableau."

> [!tip] Strong answer includes
> - Identify entering column (most negative Z-row), run the ratio test, pivot, update Z
> - Read solution: basic variables take the RHS, non-basic are zero
> - Read shadow prices off slack columns in the Z-row
> - State optimality test (no negatives in Z-row for a max problem) and be able to say what a tie in the ratio test means (degeneracy)

---
## 8. Big-M, Two-Phase Method and Minimisation Problems
> 🔴 Tier 1 · _Key points:_ Artificial variables for ≥ and = rows

### Definition
When a row is "≥" or "=", slack variables cannot provide an initial identity basis. Add an **artificial variable** $a_i \ge 0$ and remove it by penalty or by a first phase:

- **Big-M:** add $M a_i$ to a minimisation objective (subtract for max), with $M$ a huge positive number; artificial variables are driven out if the problem is feasible.
- **Two-phase:** Phase 1 minimises $\sum a_i$; if the minimum is 0, drop the artificials and run Phase 2 with the real objective; if > 0, the LP is **infeasible**. Two-phase avoids the numerical trouble of an enormous $M$, which is why solvers use it.

A minimisation problem can be handled directly (choose the most *positive* $Z$-row entry) or by maximising $-Z$.

### Example
$$\min\ Z = 4x_1 + x_2 \quad \text{s.t. } 3x_1+x_2 = 3,\ 4x_1+3x_2 \ge 6,\ x_1+2x_2 \le 4$$

Standard form: $3x_1+x_2+a_1 = 3$; $4x_1+3x_2 - s_2 + a_2 = 6$; $x_1+2x_2+s_3 = 4$. Big-M objective: $\min Z' = 4x_1+x_2+Ma_1+Ma_2$. Eliminating the artificials from the objective row gives the starting row: $x_1$: $4-7M$; $x_2$: $1-4M$; $s_2$: $+M$; RHS $-9M$. The most attractive entering variable is $x_1$ (largest negative coefficient $-7M+4$); the ratio test picks row 1 ($3/3=1$ against $6/4=1.5$). Further pivots lead to the optimum **$x_1 = 0.4,\ x_2 = 1.8,\ Z = 3.4$** (checked by Python): the equality is met ($1.2+1.8=3$), the ≥ row is met ($1.6+5.4=7 \ge 6$, surplus 1), and the ≤ row is met with $0.4+3.6=4$ (binding).

### In the news
See news box. Feasibility detection, the heart of Phase 1, is still the first thing every solver does: if a refinery plan "cannot meet the demand with the allowed crude slate", Phase 1 is the machinery that tells the planner that the requirements conflict.

### Interview angle
> [!question] How it is asked
> "How does simplex start when the origin is not feasible?"

> [!tip] Strong answer includes
> - Artificial variables create an initial basis; Big-M penalises them, two-phase first minimises their sum
> - If artificials remain positive at the optimum of Phase 1, the model is infeasible
> - Mentions numerical issues of Big-M (choose M too large and rounding errors arise); Solver does this internally
> - Be able to convert min ↔ max and ≥ ↔ ≤ without error

---
## 9. Duality
> 🔴 Tier 1 · _Key points:_ Primal-dual pairs, weak/strong duality, complementary slackness

### Definition
Every LP (the **primal**) has a companion **dual** LP. For a max primal with ≤ constraints:

$$\text{Primal: } \max\ c^Tx\ \text{s.t. } Ax\le b,\ x\ge0 \qquad \text{Dual: } \min\ b^Ty\ \text{s.t. } A^Ty\ge c,\ y\ge0$$

Translation rules: each primal constraint gets a dual variable $y_i$; each primal variable gives a dual constraint; max ↔ min; RHS ↔ objective coefficients; ≤ ↔ ≥ (sign conventions flip for equality or free variables: an equality row gives a *free* dual variable).

Key theorems:
- **Weak duality:** any feasible primal value ≤ any feasible dual value (for max primal).
- **Strong duality:** if one has an optimum, so does the other, and the optimal values are **equal**.
- **Complementary slackness:** $y_i^*\,(b_i - a_i x^*) = 0$ and $x_j^*\,(a_j^T y^* - c_j) = 0$. If a resource has slack, its price is zero; if a variable is positive, its dual constraint is tight.

Economic reading: the dual asks "what is the lowest total price at which an outsider could buy all my resources, such that no product's resource-value falls below its margin?" Dual variables are **imputed resource prices**.

### Example
Pump dual: $\min\ 100y_1 + 80y_2 + 40y_3$ s.t. $2y_1+y_2+y_3 \ge 300$ (P1), $y_1+y_2 \ge 200$ (P2), $y_i \ge 0$. Solve: because $x_1, x_2 > 0$, both dual constraints are tight, and since finishing has slack ($s_3 = 20$), $y_3 = 0$. Then $2y_1+y_2=300$ and $y_1+y_2=200$ give $y_1 = 100$, $y_2 = 100$. Dual objective: $100(100)+80(100)+40(0) = 10{,}000+8{,}000 = ₹18{,}000$ = primal optimum (strong duality). Simplex solves both at once: the final tableau's Z-row under the slacks is the dual solution.

Why use the dual in practice: a model with many constraints and few variables is cheaper to solve in the dual; and duals give the price information needed for decisions (below).

### In the news
See news box. Dual values drive pricing and trading decisions in energy: a refinery's LP shadow price on distillation capacity or on a sulphur spec is exactly the number that tells it how much to pay for a better crude or an extra barrel of capacity.

### Interview angle
> [!question] How it is asked
> "What is the dual of a product-mix LP and what do the dual variables mean?"

> [!tip] Strong answer includes
> - Write the dual in two lines; name the correspondence (constraints ↔ variables, max ↔ min)
> - Strong duality: optimal values equal (₹18,000 in the example)
> - Complementary slackness explains why non-binding constraints have zero price
> - Dual variables as opportunity cost of resources: the maximum a manager should pay per extra unit

---
## 10. Shadow Prices and Reduced Costs
> 🔴 Tier 1 · _Key points:_ Marginal value of a resource; cost of forcing a product in

### Definition
- **Shadow price (dual value)** of a constraint = change in the optimal objective per unit increase of its RHS, *within the allowable range*. For a max problem with ≤ rows it is ≥ 0; for a ≥ row in a min problem it is the marginal cost of tightening the requirement.
- **Reduced cost** of a decision variable = how much the objective deteriorates per unit if the variable is forced into the plan from zero (equivalently, how far its coefficient must improve before it enters the plan). Variables in the optimal basis have reduced cost 0.

$$\text{reduced cost}_j = c_j - \sum_i y_i a_{ij}$$

A shadow price is the **maximum price worth paying** for one more unit of a scarce resource; if overtime costs less than the shadow price, buy it; if more, don't.

### Example
Pump plan: machining shadow price ₹100 per hour. If overtime costs ₹70 per machining hour, buying 10 more hours (within the range 80 to 120, see sub-topic 11) adds $10 \times 100 = ₹1{,}000$ revenue-contribution at a ₹700 cost: net gain ₹300. At ₹130/hour it would lose ₹300. Finishing's shadow price is 0, so extra finishing hours are worthless today.

Reduced-cost illustration: suppose a third product P3 earns ₹250 and needs 2 machining + 2 assembly hours. Its imputed cost is $100(2)+100(2) = ₹400 > ₹250, so reduced cost = $250 - 400 = -150$ (unattractive; do not make it). If P3 needed only 1 machining + 1 assembly hour, imputed cost ₹200 < ₹250, and it would enter the plan.

### In the news
See news box. For a refiner the same logic prices a crude switch: if a Kuwaiti barrel's margin beats the imputed cost of its resource usage at the optimum, it enters the crude slate; if not, it stays out.

### Interview angle
> [!question] How it is asked
> "Your LP says the shadow price of machine hours is ₹100. A supplier offers extra hours at ₹120. What do you do?"

> [!tip] Strong answer includes
> - Shadow price is marginal value only within the allowable RHS range (give the range)
> - ₹100 < ₹120: do not buy at ₹120 (each hour loses ₹20); consider negotiating below ₹100
> - Re-solve after a big change because the basis may change and the price with it
> - Shadow prices are opportunity costs, not accounting costs

---
## 11. Sensitivity Analysis and Ranging
> 🔴 Tier 1 · _Key points:_ Objective-coefficient ranges, RHS ranges, 100% rule

### Definition
**Sensitivity (post-optimality) analysis** asks how far the data can change before the optimal *basis* changes.

- **Objective coefficient ranging:** the interval for $c_j$ over which the current optimal plan stays optimal (the value of $Z$ changes, the plan does not).
- **RHS ranging:** the interval for $b_i$ over which the shadow price stays valid (the basis stays feasible).
- **100% rule:** when several coefficients (or RHS values) change together, the current solution stays optimal if the sum of (change ÷ allowable change in that direction) is ≤ 100%. It is sufficient, not necessary.

### Example
Pump problem (computed from the optimal tableau and verified by re-solving):

| Item | Current | Allowable decrease | Allowable increase | Range |
|---|---|---|---|---|
| $c_1$ (P1 margin) | 300 | 100 | 100 | 200 to 400 |
| $c_2$ (P2 margin) | 200 | 50 | 100 | 150 to 300 |
| Machining RHS | 100 | 20 | 20 | 80 to 120 |
| Assembly RHS | 80 | 20 | 20 | 60 to 100 |
| Finishing RHS | 40 | 20 | no limit | 20 to ∞ |

How to get them: the optimum at C stays optimal while the iso-profit slope stays between the machining and assembly slopes: $1 \le c_1/c_2 \le 2$. So $c_1 \in [200, 400]$ at $c_2 = 200$, and $c_2 \in [150, 300]$ at $c_1 = 300$. For machining RHS $b_1$: $x_1 = b_1 - 80$, $x_2 = 160 - b_1$, $s_3 = 120 - b_1$; non-negativity gives $80 \le b_1 \le 120$. Within that range $Z = 18{,}000 + 100(b_1-100)$.

100% rule check: P1 margin falls ₹60 (60/100 = 60% of its allowable decrease) and P2 margin rises ₹40 (40/100 = 40% of its allowable increase): total 100%, the edge of validity.

### In the news
See news box. Sensitivity ranges are how a refinery planner answers "how far can the Brent–Dubai spread move before we change the crude slate": the question is about basis change, not about the optimal value.

### Interview angle
> [!question] How it is asked
> "Here is a Solver sensitivity report. What does it tell the manager, and which numbers would you worry about?"

> [!tip] Strong answer includes
> - Distinguish *range of optimality* (objective coefficient) from *range of feasibility* (RHS) and say what happens outside (basis changes, re-solve)
> - Point to small allowable increases/decreases as the fragile assumptions
> - Use the 100% rule for simultaneous changes
> - Translate into action: "plan is robust unless P1 margin falls below ₹200 or machining hours fall below 80"

---
## 12. LP in Excel Solver and Python (PuLP)
> 🔴 Tier 1 · _Key points:_ Model layout, SUMPRODUCT, sensitivity report; pulp code

### Definition
**Excel Solver** (setup and options in [[077 Solver, Goal Seek & What-If Analysis]] and [[043 Advanced Excel (Pivot, Solver, Forecasting)]]): lay out decision cells (changing variable cells), an objective cell with `=SUMPRODUCT(margins, quantities)`, constraint left-hand sides with `SUMPRODUCT(usage_row, quantities)` and RHS cells. In the Solver dialog: set objective (Max/Min), by changing the decision cells, add constraints, tick **Make Unconstrained Variables Non-Negative**, choose **Simplex LP** (not GRG Nonlinear), solve, and request the **Answer** and **Sensitivity** reports. The Sensitivity report shows *Final Value, Reduced Cost, Objective Coefficient, Allowable Increase/Decrease* for variables, and *Final Value, Shadow Price, Constraint R.H. Side, Allowable Increase/Decrease* for constraints. A caution on signs: Solver's reduced cost and shadow price follow a "change in objective" convention; read the sign against what you know.

**Python (PuLP)** (see [[068 Operations-Specific Python (PuLP, SimPy)]] and [[046 Python for Operations]]):

```python
import pulp

m = pulp.LpProblem("pump_mix", pulp.LpMaximize)
x1 = pulp.LpVariable("P1", lowBound=0)
x2 = pulp.LpVariable("P2", lowBound=0)

m += 300 * x1 + 200 * x2                      # objective
m += 2 * x1 + x2 <= 100, "machining"
m += x1 + x2 <= 80,      "assembly"
m += x1 <= 40,           "finishing"

m.solve(pulp.PULP_CBC_CMD(msg=0))
print(pulp.LpStatus[m.status], x1.value(), x2.value(), pulp.value(m.objective))
for name, c in m.constraints.items():
    print(name, "shadow price:", c.pi, "slack:", c.slack)
```

### Example
Running this code (PuLP 3.3 with the CBC solver) prints `Optimal 20.0 60.0 18000.0`, shadow prices `machining 100.0`, `assembly 100.0`, `finishing 0.0` with slack 20, which agrees with the tableau and the graph. For a model with 50 plants and 200 SKUs, the same code scales by building variables with `LpVariable.dicts` and constraints with `lpSum` loops; the model is data-driven, the solver is a commodity. A 3-minute interview deliverable: show the layout, name the three Solver settings that matter (Simplex LP, non-negative, report type), and interpret shadow prices.

### In the news
See news box. Open-source solvers such as CBC and HiGHS, which implement simplex and interior-point methods, are what make LP accessible to analysts and start-ups; the research cited in the news box concerns exactly this class of algorithm.

### Interview angle
> [!question] How it is asked
> "Build this in Excel Solver, or show me code: how would you set up and check it?"

> [!tip] Strong answer includes
> - Clean separation of data, decision cells, calculations, and constraints; named ranges help auditing
> - Right solving method (Simplex LP for linear models) and non-negativity box
> - Check: status optimal, constraints binding as expected, shadow prices in sensible range
> - Mention checking with a small hand case before scaling up

---
## 13. Interpreting and Communicating LP Results to Managers
> 🔴 Tier 1 · _Key points:_ Plan, bottleneck, prices, robustness, limits

### Definition
Manager-ready reading of an LP in five lines: (1) **the plan** (what to make/buy/ship); (2) **the value** (₹ contribution vs the current plan); (3) **the bottlenecks** (binding constraints and their shadow prices); (4) **the slack** (idle capacity or unused budget); (5) **the robustness** (ranges and which assumptions are fragile). Add a one-line "what to do": invest in the bottleneck, drop unprofitable SKUs, renegotiate the scarce input.

When LP is the wrong tool: integer decisions (use IP: [[148 Operations Research - Network Models & Integer Programming]]); non-linear costs (economies of scale); randomness (simulation, stochastic programming: [[150 Decision Analysis & Simulation]]); multiple objectives (goal programming). Multi-period extensions add inventory-balance equations $I_t = I_{t-1} + P_t - D_t$, giving the aggregate plans in [[153 Aggregate Planning Models & Workforce Strategy]].

### Example
Pump plant summary for the CFO: "Optimal plan: 20 P1 + 60 P2 per week = ₹18,000. Machining and assembly are the bottlenecks, worth ₹100 per hour each; 20 finishing hours sit idle, so do not expand finishing. Every extra machining hour is worth ₹100 up to +20 hours. The plan holds while P1's margin stays within ₹200 to ₹400. Versus the current rule-of-thumb plan of 30 P1 + 40 P2 (₹17,000: check, $9{,}000+8{,}000$), optimisation adds ₹1,000 a week, roughly ₹52,000 per year." (Check: 30 P1 uses 60+40 = 100 machining hours and 30+40 = 70 assembly hours, so it is feasible but leaves 10 assembly hours unused.)

### In the news
See news box. The simplex-method headline of 2025 is a reminder that "optimisation" in a company is an algorithm plus a story: the algorithm is old and trusted; the story (bottlenecks, prices, robustness) is what the manager buys.

### Interview angle
> [!question] How it is asked
> "You have run the model: how would you present the result to a sceptical plant head?"

> [!tip] Strong answer includes
> - Start with the decision and ₹ impact, then bottlenecks and what to do
> - Use shadow prices and ranges as the "why" and "how long it stays true"
> - Say what the model ignores (set-ups, integrality, demand uncertainty) and how you will check it (pilot, scenarios)
> - Offer a sanity check against the current plan so the plant head can recognise the result

---
## 14. ⭐ Advanced: Interior-Point Methods, Complexity and LP Relaxations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Complexity.** Klee and Minty (1972) built cubes on which Dantzig's rule visits all $2^n$ vertices, so simplex is exponential in the worst case. Khachiyan's ellipsoid method (1979) and Karmarkar's interior-point method (1984) are polynomial. **Interior-point (barrier) methods** move through the interior along a central path; they excel on very large sparse LPs, while simplex tends to win on warm starts (re-solves after small changes), which is why both are offered in commercial solvers.
- **Smoothed analysis** (Spielman–Teng 2001) shows that after small random perturbation of the data, simplex needs expected polynomial pivots; **Bach–Huiberts (2025)** give a tight bound within that model. "By-the-book" analysis (Bach, Black, Huiberts, Kafer) goes further and models solver tolerances.
- **LP relaxation.** Drop integrality from an integer program: the LP optimum is a bound (upper for max) used in branch-and-bound and for gap measurement: $\text{gap} = \dfrac{Z_{LP} - Z_{IP}}{Z_{IP}}$.
- **Robust and stochastic LP.** Uncertain $c$, $A$, $b$: robust LP protects against worst case in an uncertainty set; two-stage stochastic LP chooses first-stage decisions, then recourse after demand is revealed.

### Example
Relaxation bound: suppose the pump plant could only make whole batches of 15 units. LP says 20 P1 and 60 P2 (₹18,000), but that is not batch-compatible. The best batch-compatible plan (enumerated by Python) is 15 P1 and 60 P2: machining 90, assembly 75, $Z = 4{,}500+12{,}000 = ₹16{,}500$. The LP bound of ₹18,000 says no integer plan can exceed that, so the gap is $(18{,}000 - 16{,}500)/16{,}500 \approx 9.1\%$: the price of the batch rule. For the simplex theory result: in 2001 the proved bound had exponents up to 30; the 2025 result is reported to be optimal within that analysis model, a rare "closing" of a 25-year-old gap.

### In the news
See news box. These are the three 2025 research items on the oldest algorithm in business analytics.

### Interview angle
> [!question] How it is asked
> "Is the simplex method polynomial? Why do people still use it over interior-point methods?"

> [!tip] Strong answer includes
> - Worst case exponential (Klee–Minty), practically fast; interior-point is polynomial and good for huge LPs
> - Simplex is better for warm starts, gives vertex solutions with clear basis and shadow prices for sensitivity
> - Smoothed analysis explains the gap between worst-case and practice
> - LP relaxation as a bound for integer problems ([[148 Operations Research - Network Models & Integer Programming]])
