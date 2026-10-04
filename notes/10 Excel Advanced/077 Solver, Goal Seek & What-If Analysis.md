---
tags: [excel-advanced, tier2]
area: Excel Advanced
topic: "Solver, Goal Seek & What-If Analysis"
tier: Tier 2
roles: All Roles
status: complete
subtopics: 12
---
# Solver, Goal Seek & What-If Analysis

⬅ [[076 Charts, Dashboards & Form Controls]] · [[_Index - Excel Advanced|Excel Advanced]] · [[078 Excel for Operations & SCM]] ➡

> **Area:** Excel Advanced · **Priority:** 🟠 Tier 2 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Goal Seek]]
2. [[#2. Scenario Manager]]
3. [[#3. Data Table (1-variable)]]
4. [[#4. Data Table (2-variable)]]
5. [[#5. Solver Add-in]]
6. [[#6. Solver for EOQ]]
7. [[#7. Solver for Transportation]]
8. [[#8. Monte Carlo in Excel]]
9. [[#9. Break-Even Analysis]]
10. [[#10. NPV / IRR in Excel]]
11. [[#11. ⭐ Advanced: Sensitivity Reports, Shadow Prices and Tornado Charts]]
12. [[#12. ⭐ Advanced: Building a Defensible Decision Model]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Excel adds Python and AI agents next to classic what-if tools
> **Python in Excel (GA Sep 2024).** The Register reported on 18 Sep 2024 that Python in Excel was generally available for Windows users with Microsoft 365 Business or Enterprise on the Current Channel, built with Anaconda. It makes heavier simulation (e.g. NumPy-style Monte Carlo) possible inside a workbook; premium compute was priced at $24 per user per month. ([The Register](https://www.theregister.com/2024/09/18/python_in_excel_general_release/))
> 
> **Agent Mode (Dec 2025 to Jan 2026).** Microsoft announced general availability of Agent Mode in Excel on the web on 9 Dec 2025 and on Windows on 27 Jan 2026. It can build models from plain-language goals, but sensitivity checks, constraints and assumptions (what Goal Seek, Solver and Data Tables test) still need to be set and challenged by the analyst. I did not find a source specific to Solver or Goal Seek updates, so no figures are claimed for them. ([Excel for web](https://techcommunity.microsoft.com/blog/excelblog/agent-mode-in-excel-is-now-generally-available-on-excel-for-web/4476092), [Desktop](https://techcommunity.microsoft.com/blog/excelblog/agent-mode-in-excel-is-now-generally-available-on-desktop/4457408))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Goal Seek
> 🟠 Tier 2 · _Tracker hint:_ Data → What-If Analysis → Goal Seek; set cell = value by changing cell

### Definition
**Goal Seek** finds the value of **one input cell** that makes a **formula cell** reach a target. Path: **Data > What-If Analysis > Goal Seek**; fields: *Set cell* (must contain a formula), *To value* (a number you type), *By changing cell* (a constant input, not a formula). It uses iterative numerical search (Newton-type), so it gives an approximate answer to a tolerance and may fail on non-monotonic or discontinuous models. Limitations: one variable, one target, no constraints, and the answer is static (re-run when inputs change). Typical uses: break-even volume, the interest rate that gives a required EMI, the price that gives a target margin, the demand needed to fill capacity. If you need many variables or constraints use Solver. Make sure the model is not circular and starts with a reasonable initial value.

### Example
Profit = (Price - Variable cost) x Quantity - Fixed cost, with Price 50, VC 30, FC 40,000. Quantity 1,500 gives profit = 20 x 1,500 - 40,000 = -10,000. Goal Seek: set Profit cell to 0 by changing Quantity returns 2,000 (20 x 2,000 = 40,000). Setting the target to 20,000 returns 3,000 units.

### In the news
See news box. Agents can build models quickly; Goal Seek remains the fast manual check of "what has to be true" for a target.

### Interview angle
> [!question] How it is asked
> "How would you find the sales volume needed to hit a profit target in Excel?"

> [!tip] Strong answer includes
> - Set cell, To value, By changing cell, and that the changing cell must be an input
> - One variable only, no constraints, approximate result
> - Break-even example with numbers
> - Know when to move to Solver

---

## 2. Scenario Manager
> 🟠 Tier 2 · _Tracker hint:_ Data → What-If → Scenario Manager; define Best/Base/Worst; summary report

### Definition
**Scenario Manager** stores named sets of input values (scenarios) for up to 32 changing cells and lets you switch between them. Path: **Data > What-If Analysis > Scenario Manager > Add**; name the scenario (Best, Base, Worst), choose *Changing cells*, enter values. **Show** applies a scenario to the sheet. **Summary** creates a report (Scenario Summary or PivotTable) showing chosen *Result cells* under every scenario side by side, with current values in a column. Tips: use **named cells** so the summary is readable; keep the live sheet on Base; scenarios are stored in the sheet and can be merged. Limitations: static values (not linked to external data), clumsy for many scenarios; a modern alternative is a **scenario selector** (dropdown or form control plus `CHOOSE`/`INDEX` into a scenario table), which is transparent and shareable.

### Example
Inputs: Demand growth, Price change, Cost inflation. Best: 12%, +3%, 4%; Base: 8%, 0%, 6%; Worst: 2%, -4%, 9%. Result cells: Revenue and EBITDA. The Summary report shows three columns of EBITDA so management sees the range at once. Selector equivalent: `=INDEX(ScenarioTable, ScenarioNo, 2)` with `ScenarioNo` linked to a combo box.

### In the news
See news box. Scenario thinking is unchanged by new tooling; the value is in choosing assumptions defensibly.

### Interview angle
> [!question] How it is asked
> "How do you present best, base and worst cases for a plan in Excel?"

> [!tip] Strong answer includes
> - Scenario Manager with Summary report
> - Selector with INDEX/CHOOSE as the more transparent alternative
> - How to choose scenario assumptions (drivers, probabilities)
> - Don't forget to restore the base case before sharing

---

## 3. Data Table (1-variable)
> 🟠 Tier 2 · _Tracker hint:_ One-way: vary one input; see impact on output — sensitivity table

### Definition
A **one-variable Data Table** recomputes a model for a list of values of **one input** and records the result(s). Layout (column-oriented): list the input values down a column (e.g. A3:A7); in the cell **one row above and one column to the right** (B2) enter a formula that links to the output (`=Profit`). Select A2:B7 > **Data > What-If Analysis > Data Table**; *Column input cell* = the model's input cell. Excel fills the grid with the array `{=TABLE(,input)}`. Add more output formulas across row 2 for multiple outputs. Rules: the input cell must be on the **same sheet** as the table; Data Tables recalc slowly (set calculation to **Automatic except for Data Tables** if needed). Use for sensitivity (price, demand, lead time, interest rate) and to chart the response curve.

### Example
Using the profit model (Price 50, VC 30, FC 40,000), volumes 1,000, 2,000, 3,000 in column A with B2 `=Profit`: results -20,000, 0, 20,000 (20 x 1,000 - 40,000 = -20,000; 20 x 2,000 - 40,000 = 0; 20 x 3,000 - 40,000 = 20,000). Plot it to see the break-even crossing at 2,000.

### In the news
See news box. Data Tables remain the classic native tool for sensitivity grids that agents or analysts then chart.

### Interview angle
> [!question] How it is asked
> "How would you show how profit changes as volume varies?"

> [!tip] Strong answer includes
> - Layout: input list, formula one cell above/right, Column input cell
> - Same-sheet restriction and calculation setting
> - Chart the result for the insight
> - Mention limits vs full simulation

---

## 4. Data Table (2-variable)
> 🟠 Tier 2 · _Tracker hint:_ Two-way: vary 2 inputs simultaneously; pricing × volume matrix

### Definition
A **two-variable Data Table** varies **two inputs** and shows one output in a matrix. Layout: put the output formula in the **top-left corner cell**; row input values across the top row; column input values down the left column. Select the whole block > **Data Table**; *Row input cell* = the input whose values run across the top; *Column input cell* = the input whose values run down the side. Mixing them up is the most common mistake. Only **one output** per two-way table. Use for price x volume, discount x margin, demand x lead time, WACC x growth (valuation). Add conditional formatting (red for losses) so the matrix reads like a heat map. Combine with Goal Seek lines (the zero-profit boundary).

### Example
Profit = (P - 30) x Q - 40,000. Prices 45, 50, 55 down; volumes 2,000, 2,500 across:

| Price \ Volume | 2,000 | 2,500 |
|---|---|---|
| 45 | -10,000 | -2,500 |
| 50 | 0 | 10,000 |
| 55 | 10,000 | 22,500 |

Check one cell: P = 55, Q = 2,500: 25 x 2,500 = 62,500; minus 40,000 = 22,500.

### In the news
See news box. Sensitivity matrices are a staple when AI-built models need stress-testing before decisions.

### Interview angle
> [!question] How it is asked
> "How would you show profit sensitivity to both price and volume?"

> [!tip] Strong answer includes
> - Corner cell holds the formula; row vs column input cells
> - Only one output per two-way table
> - Colour-code and interpret (break-even frontier)
> - Mention tornado chart for ranking many drivers

---

## 5. Solver Add-in
> 🟠 Tier 2 · _Tracker hint:_ Max/min/target objective; subject to constraints; LP, integer, non-linear modes

### Definition
**Solver** optimises an **objective cell** by changing **decision variable cells** subject to **constraints**. Enable it: **File > Options > Add-ins > Manage: Excel Add-ins > Go > tick Solver Add-in**; then **Data > Solver**. Parameters: *Set Objective* (Max, Min or Value Of), *By Changing Variable Cells*, *Subject to the Constraints* (<=, >=, =, int, bin, dif), tick *Make Unconstrained Variables Non-Negative*. Choose the **solving method**:

| Method | Use when |
|---|---|
| Simplex LP | Linear objective and constraints; gives global optimum, sensitivity reports |
| GRG Nonlinear | Smooth non-linear models (EOQ, pricing curves) |
| Evolutionary | Non-smooth, discontinuous models (IF, lookups); heuristic |

Reports: **Answer, Sensitivity** (shadow prices, reduced costs, for LP) and **Limits**. Formulating correctly (variables, objective, constraints) matters more than clicking. Add **Integer** constraints for whole units; this turns LP into integer programming, which may be slower.

### Example
Product mix: A earns 40 per unit using 2 machine-hours; B earns 30 using 1 hour; 100 hours available, demand caps A at 40 and B at 60. Maximise 40A + 30B s.t. 2A + B <= 100, A <= 40, B <= 60. Try A = 20, B = 60: hours = 40 + 60 = 100 OK. Profit = 800 + 1,800 = 2,600. Compare A = 40, B = 20: hours 80 + 20 = 100; profit 1,600 + 600 = 2,200. B earns 30 per machine-hour and A only 20, so fill B first (B = 60, using 60 hours), then use the remaining 40 hours for A (A = 20). That gives 2,600, the optimum.

### In the news
See news box. Agent Mode may suggest optimisation but does not replace explicit objective, variable and constraint design that Solver forces you to write.

### Interview angle
> [!question] How it is asked
> "Have you used Solver? Formulate a product-mix problem."

> [!tip] Strong answer includes
> - Objective, decision variables, constraints
> - Method choice (Simplex vs GRG vs Evolutionary)
> - Integer and non-negativity settings
> - Interpret sensitivity (shadow price) and check feasibility

---

## 6. Solver for EOQ
> 🟠 Tier 2 · _Tracker hint:_ Minimize total cost = ordering + holding cost; constraint: qty ≥ safety stock

### Definition
EOQ minimises annual total inventory cost:

$$TC(Q)=\frac{D}{Q}S+\frac{Q}{2}H,\qquad Q^*=\sqrt{\frac{2DS}{H}}$$

with D annual demand, S cost per order, H annual holding cost per unit. In Excel: input cells D, S, H; **decision cell** Q; objective cell `=D/Q*S + Q/2*H`. In Solver: Set Objective = TC, **Min**, changing cell = Q, constraints `Q >= SafetyStock` (or minimum order quantity) and `Q <= MaxStorage`, method **GRG Nonlinear** (the objective is non-linear in Q), start with a positive Q (not zero, to avoid division by zero). Check against the formula `=SQRT(2*D*S/H)`. Solver adds value when real constraints exist (MOQ, pallet multiples via integer, budget, storage) or when quantity discounts break the formula. Total cost is flat near the optimum, so rounding to a practical lot size costs little.

### Example
D = 12,000, S = ₹500, H = ₹10. $Q^*=\sqrt{2\times12000\times500/10}=\sqrt{1{,}200{,}000}\approx1095$. Ordering = 12,000/1,095.4 x 500 = ₹5,477; holding = 1,095.4/2 x 10 = ₹5,477; TC = ₹10,954. Using 1,200: ordering 5,000 + holding 6,000 = 11,000, only 0.4% higher. With MOQ constraint Q >= 1,500: TC = 4,000 + 7,500 = 11,500 (5% higher), the cost of the MOQ.

### In the news
See news box. Python in Excel can run optimisers, but a Solver EOQ model is the transparent first step that interviewers expect.

### Interview angle
> [!question] How it is asked
> "Use Excel to find the optimal order quantity with a minimum order constraint."

> [!tip] Strong answer includes
> - TC formula, EOQ formula, and equal ordering and holding costs at the optimum
> - Solver setup: GRG Nonlinear, minimise, constraints
> - Sensitivity: flat cost curve near Q*
> - Mention safety stock is separate from EOQ

---

## 7. Solver for Transportation
> 🟠 Tier 2 · _Tracker hint:_ Minimize cost subject to supply/demand constraints; integer variables

### Definition
The **transportation problem** ships goods from m sources to n destinations at minimum total cost:

$$\min \sum_{i}\sum_{j} c_{ij}x_{ij}\quad \text{s.t. } \sum_j x_{ij}\le s_i,\ \ \sum_i x_{ij}\ge d_j,\ \ x_{ij}\ge0$$

Excel layout: cost matrix; a matching matrix of **decision cells** x (initially 0 or 1); row totals (shipped from each source) compared to supply; column totals compared to demand; objective `=SUMPRODUCT(costs, x)`. Solver: minimise objective, by changing the x matrix, constraints row total <= supply, column total >= demand (or =), non-negative, method **Simplex LP**. If supply equals demand (balanced) use "=". If unbalanced add a dummy destination/source. LP gives integer solutions automatically for integer supply and demand (network structure), but add `int` if you impose extra constraints. Extensions: transshipment, fixed charges (binary variables), capacity limits.

### Example
Supplies: P1 = 30, P2 = 40. Demands: D1 = 20, D2 = 30, D3 = 20 (balanced at 70). Costs per unit: P1 to D1/D2/D3 = 4/6/8; P2 = 5/3/7. Optimal: P1 sends 20 to D1 and 10 to D3; P2 sends 30 to D2 and 10 to D3. Cost = 20x4 + 10x8 + 30x3 + 10x7 = 80 + 80 + 90 + 70 = 320. An alternative plan (P1: 20 to D1, 10 to D2; P2: 20 to D2, 20 to D3) costs 80 + 60 + 60 + 140 = 340, worse.

### In the news
See news box. Network optimisation is the same logic behind modern logistics planning tools; Solver shows the mechanics.

### Interview angle
> [!question] How it is asked
> "How would you minimise freight cost from 3 plants to 5 warehouses using Excel?"

> [!tip] Strong answer includes
> - Decision matrix, SUMPRODUCT objective, supply and demand constraints
> - Simplex LP; balanced vs unbalanced (dummy node)
> - Interpreting shadow prices and which lanes are used
> - Mention capacity or fixed-charge extensions needing binary variables

---

## 8. Monte Carlo in Excel
> 🟠 Tier 2 · _Tracker hint:_ =norm.inv(RAND(), mean, std); press F9 to re-simulate; data table for 1000 iterations

### Definition
**Monte Carlo simulation** replaces fixed assumptions with **random draws** from probability distributions, runs the model many times, and studies the distribution of outcomes. Excel tools:

```excel
=NORM.INV(RAND(), mean, std)       -- normal draw
=RANDBETWEEN(low, high)             -- uniform integer
=MIN + RAND()*(MAX-MIN)             -- uniform
=-LN(1-RAND())*mean                 -- exponential draw
```
`RAND()` is volatile, so each F9 press produces a new trial. To run 1,000 trials: put trial numbers 1 to 1,000 in a column, link the top cell to the output, and use a **one-variable Data Table** with any blank cell as the *Column input cell*. Then summarise: `AVERAGE`, `STDEV.S`, `PERCENTILE.INC(range,0.05)`, `COUNTIF(range,"<0")/1000` for probability of loss, and a histogram. Standard error shrinks as $1/\sqrt{n}$. Use `RAND()` fixes (paste values) to freeze results, and respect correlations between variables. Assumed distributions must be justified.

### Example
Demand ~ Normal(mean 100, sd 20); order quantity 120. Probability demand exceeds 120 = P(Z > 1) = 1 - 0.8413 = 15.9%. A 1,000-trial simulation with `=NORM.INV(RAND(),100,20)` and `COUNTIF(range,">120")/1000` returns roughly 0.16 (e.g. 0.14 to 0.18 across runs), matching theory.

### In the news
See news box. Python in Excel brings NumPy-style simulation into workbooks, but the Data Table method is still the no-code standard.

### Interview angle
> [!question] How it is asked
> "How would you estimate the probability that project cost overruns the budget?"

> [!tip] Strong answer includes
> - Replace point estimates with distributions and run many trials
> - NORM.INV(RAND()) and Data Table for iterations
> - Report mean, percentiles, probability of exceeding a threshold
> - Caveats: assumptions, correlations, volatile recalculation

---

## 9. Break-Even Analysis
> 🟠 Tier 2 · _Tracker hint:_ Goal Seek: set profit=0, change quantity; build sensitivity table for price/cost

### Definition
**Break-even** is the volume where total revenue equals total cost (profit = 0).

$$Q_{BE}=\frac{FC}{P-VC},\qquad \text{Break-even revenue}=\frac{FC}{CM\%}$$

Contribution margin per unit = P - VC; CM% = (P - VC)/P. **Margin of safety** = (Actual - BE)/Actual. **Degree of operating leverage** = Contribution / Profit. For a target profit: $Q=(FC+\text{Target})/(P-VC)$. In Excel: compute with the formula, verify using **Goal Seek** (set profit to 0 by changing quantity), and build a **Data Table** over price and variable cost to see how the break-even moves. Chart revenue and total cost lines against volume; the crossing is the break-even point. Assumes linear costs and a single product (for mix, use weighted-average contribution).

### Example
P = 50, VC = 30, FC = 40,000. CM = 20, CM% = 40%. $Q_{BE}=40{,}000/20=2{,}000$ units; BE revenue = 2,000 x 50 = ₹100,000 (also 40,000/0.4 = 100,000). If actual sales are 3,000: margin of safety = (3,000 - 2,000)/3,000 = 33.3%. Profit = 20,000; DOL = contribution 60,000 / profit 20,000 = 3, so a 10% volume rise lifts profit 30%.

### In the news
See news box. Whatever tool builds the model, the break-even logic is a first sanity check on any business case.

### Interview angle
> [!question] How it is asked
> "A new product has fixed cost 40,000 and unit contribution 20. How many units to break even, and what if price falls 10%?"

> [!tip] Strong answer includes
> - Formula, contribution margin and margin of safety
> - Sensitivity: price 45 gives CM 15 and BE = 2,667 units (40,000/15 = 2,666.7)
> - Goal Seek and Data Table as Excel methods
> - Limits (linear, single product, ignores time value)

---

## 10. NPV / IRR in Excel
> 🟠 Tier 2 · _Tracker hint:_ =NPV(rate, cf1:cfn); =IRR(cf_range); =xnpv for irregular dates

### Definition
$$NPV=\sum_{t=0}^{n}\frac{CF_t}{(1+r)^t},\qquad IRR: NPV=0$$

```excel
=NPV(rate, cf1:cfn) + CF0         -- NPV() assumes the first value is at the END of period 1, so add CF0 separately
=IRR(range, [guess])              -- annual return for periodic flows; first value is time 0
=XNPV(rate, values, dates)        -- irregular dates; first date is the base date (time 0)
=XIRR(values, dates)
=MIRR(values, finance_rate, reinvest_rate)
```
Decision rule: accept if NPV > 0 or IRR > hurdle rate (WACC). IRR can mislead with non-conventional flows (multiple IRRs) or when ranking mutually exclusive projects of different scale; NPV is preferred. The most common error is including the time-0 outflow inside `NPV()`. Payback ignores time value; discounted payback does not. Use a **Data Table** to show NPV vs discount rate (NPV profile), and Goal Seek on the rate for IRR.

### Example
Invest ₹1,000 now; receive ₹400 at the end of years 1, 2, 3. At 10%: PV of inflows = 400 x (0.9091 + 0.8264 + 0.7513) = 400 x 2.4869 = 994.7; NPV = 994.7 - 1,000 = -5.3. Excel: `=NPV(10%,400,400,400)-1000` = -5.26. IRR solves 400 x annuity factor = 1,000 (factor 2.5), giving about 9.7%, below the 10% hurdle, so reject.

### In the news
See news box. AI generated cash-flow models make timing errors (time-0 inside NPV); knowing the convention is the check.

### Interview angle
> [!question] How it is asked
> "Should we invest in this machine? Evaluate in Excel" or "Why can NPV() give the wrong answer?"

> [!tip] Strong answer includes
> - NPV formula and the time-0 convention in Excel
> - IRR vs hurdle rate, limits of IRR, NPV preference
> - XNPV/XIRR for dated flows
> - Sensitivity on discount rate and cash flows

---

## 11. ⭐ Advanced: Sensitivity Reports, Shadow Prices and Tornado Charts
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Solver's **Sensitivity Report** (LP only) is where the managerial insight lies:
- **Shadow price** (dual value): the change in the objective per one-unit increase in a constraint's right-hand side, valid within the allowable range (e.g. one extra machine-hour worth ₹x).
- **Reduced cost**: how much a non-basic variable's objective coefficient must improve before it enters the plan.
- **Allowable increase/decrease**: range over which the shadow price or current plan stays valid.

A **tornado chart** ranks drivers: change each input by plus or minus 10% (one at a time), record the output swing, sort by size, and plot as a horizontal bar chart; the top bars are the drivers worth managing. Together these answer "what is the value of relaxing a constraint?" and "which assumption matters most?", which consultants prefer to a bare optimum.

### Example
In the product-mix example (A: 40, B: 30, hours 100, A <= 40, B <= 60): at the optimum A = 20, B = 60, hours is the binding constraint. One extra hour lets A rise by 0.5 (2 hours per A), adding 0.5 x 40 = ₹20, so the shadow price of machine-hours is ₹20 per hour, so overtime costing less than ₹20 per hour is worth buying. Check: A = 20.5, B = 60 uses 41 + 60 = 101 hours; profit = 820 + 1,800 = 2,620, up ₹20.

### In the news
See news box. AI can run an optimiser; explaining a shadow price to decision makers is the human contribution.

### Interview angle
> [!question] How it is asked
> "What does the shadow price tell the plant manager?" or "Which assumption drives your model the most?"

> [!tip] Strong answer includes
> - Shadow price as the value of one more unit of a scarce resource, with validity range
> - Binding vs non-binding constraints
> - Tornado chart procedure
> - Action: buy capacity if cost < shadow price

---

## 12. ⭐ Advanced: Building a Defensible Decision Model
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A consulting-quality what-if model has structure: **Inputs** (blue font, one sheet, with source and units), **Calculations** (no hardcodes, formulas consistent across rows), **Outputs** (KPIs, charts) and **Checks** (balance and sum checks). Techniques:
- Use a **scenario selector** (dropdown + `CHOOSE`/`INDEX`) rather than overwriting inputs.
- Add **Data Tables** for the two or three key drivers and a **tornado** for the rest.
- Use **Goal Seek** to answer reverse questions ("what price do we need?").
- Run **Solver** for constrained decisions and save its model on the sheet.
- Run **Monte Carlo** where uncertainty is wide, reporting percentiles.
- Document assumptions, version, and owner; test extremes (zero demand) and unit consistency.
- Tell the story: recommendation, key sensitivity, risk, next step.

### Example
Capacity expansion decision: inputs (demand growth, price, capex ₹5 cr), outputs NPV and IRR. The scenario selector shows NPV: Best +₹2.1 cr, Base +₹0.6 cr, Worst -₹0.9 cr (illustrative numbers). Goal Seek finds the minimum price for which NPV = 0; the Data Table on demand growth x price shows the zone of acceptable outcomes; recommendation: proceed with a phased capex because the worst case is negative.

### In the news
See news box. As model generation gets automated, model governance and defensible assumptions differentiate analysts and consultants.

### Interview angle
> [!question] How it is asked
> "You are asked to evaluate a plant expansion. How would you structure the Excel model?"

> [!tip] Strong answer includes
> - Inputs-calcs-outputs-checks structure
> - Which what-if tool answers which question
> - Risk framing with scenarios or simulation
> - A recommendation with the key sensitivity

---
## 🔗 Go deeper: expansion notes
- [[187 Excel Interview Problem Bank & Case Exercises|Excel Interview Problem Bank & Case Exercises]]
- [[188 Financial Modelling in Excel|Financial Modelling in Excel]]
- [[189 VBA, Macros & Office Scripts Basics|VBA, Macros & Office Scripts Basics]]
