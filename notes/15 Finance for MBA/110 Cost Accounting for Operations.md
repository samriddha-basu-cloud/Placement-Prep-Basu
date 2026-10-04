---
tags: [finance-for-mba, tier2]
area: Finance for MBA
topic: "Cost Accounting for Operations"
tier: Tier 2
roles: Consulting / Operations
status: complete
subtopics: 12
---
# Cost Accounting for Operations

⬅ [[109 Valuation Basics (NPV, IRR, DCF)]] · [[_Index - Finance for MBA|Finance for MBA]] · [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]] ➡
> **Area:** Finance for MBA · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. Cost Classification]]
2. [[#2. Contribution Margin]]
3. [[#3. Absorption Costing vs Marginal Costing]]
4. [[#4. Standard Costing & Variances]]
5. [[#5. Activity-Based Costing (ABC)]]
6. [[#6. Transfer Pricing]]
7. [[#7. Make vs Buy Decision]]
8. [[#8. Target Costing]]
9. [[#9. Life Cycle Costing]]
10. [[#10. Relevant Costs for Decisions]]
11. [[#11. ⭐ Advanced: Throughput accounting and the bottleneck]]
12. [[#12. ⭐ Advanced: Time-driven ABC for logistics and service operations]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Cost structure decides who wins in low-margin Indian retail
> **D-Mart (Avenue Supermarts), Q2 FY26 (quarter ended 30 Sep 2025).** Revenue grew 15% YoY to **₹16,676 crore** but EBITDA rose only 11.3% to **₹1,230 crore**; EBITDA margin slipped to **7.3% from 7.6%** and PAT margin to **4.1% from 4.6%**, which the source attributes to "cost pressures in operations". The company added 8 stores (432 in total). When margins are this thin, a 0.3-point cost slip is worth about ₹50 crore a quarter (0.3% of ₹16,676 crore). ([Torus Digital](https://www.torusdigital.com/toruscope/quarterly-results/avenue-supermarts-q2-fy26-results-dmarts-profit-rises-4-yoy-revenue-up-15/))
> 
> **Eternal / Blinkit, Q2 FY26 (reported Oct 2025).** About **80% of Blinkit's order value** now comes from inventory the company owns; revenue was **₹13,590 crore (+183%)** but adjusted EBITDA margin fell to **1.75%** from 6.4%. Moving from marketplace to inventory-led changes the cost structure (cost of goods enters COGS, holding and wastage costs appear), a live make-versus-buy style decision. ([INDmoney](https://www.indmoney.com/blog/stocks/eternal-zomato-q2-results))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Cost Classification
> 🟠 Tier 2 · _Tracker hint:_ Fixed vs Variable; Direct vs Indirect; Product vs Period costs

### Definition
Costs are classified by purpose:

| Basis | Categories | Example (bakery) |
|---|---|---|
| Behaviour | **Fixed** (constant in total within a range), **Variable** (change with volume), **Semi-variable/mixed**, **Step** | Rent (fixed), flour (variable), electricity (mixed) |
| Traceability | **Direct** (traceable to a product) vs **Indirect/overhead** | Flour vs factory supervisor |
| Function | **Product** (inventoriable: DM, DL, factory OH) vs **Period** (expensed when incurred: selling, admin) | Oven depreciation (product) vs advertising (period) |
| Decision | Relevant vs sunk, avoidable, controllable | See later sub-topics |

Per-unit fixed cost falls as volume rises; per-unit variable cost is constant. The classification drives cost-volume-profit, absorption vs marginal costing and make-or-buy decisions.

### Example
Plant makes 10,000 units. Rent ₹2,00,000 (fixed): ₹20/unit; at 20,000 units, ₹10/unit. Materials ₹40/unit stay ₹40 at any volume. Total cost at 10,000 units = 2,00,000 + 4,00,000 = ₹6,00,000 (₹60/unit); at 20,000 units = 2,00,000 + 8,00,000 = ₹10,00,000 (₹50/unit).

### In the news
See news box. D-Mart's store rents and staff are largely fixed, so higher sales per store lowers cost per rupee of sales; the margin slip points to cost lines that did not scale.

### Interview angle
> [!question] How it is asked
> "Which of the costs in this plant are fixed vs variable, and why does it matter?"

> [!tip] Strong answer includes
> - Behaviour (fixed/variable/mixed), traceability, function split
> - Per-unit vs total behaviour
> - Mention of relevant range and step costs
> - Link to break-even and pricing decisions

---

## 2. Contribution Margin
> 🟠 Tier 2 · _Tracker hint:_ CM = Revenue – Variable Costs; CM ratio = CM/Revenue; higher = more scalable

### Definition
$$CM = \text{Revenue} - \text{Variable costs}, \quad CM\ ratio = \frac{CM}{\text{Revenue}}$$

CM is what each sale contributes to cover fixed costs and then profit. **Profit = CM − Fixed costs.** Per unit: $P - V$. It supports break-even ($FC / CM_{unit}$), product-mix decisions (rank by CM per scarce resource, e.g. per machine hour), pricing floors and operating leverage (**DOL = CM/Profit**). A high CM ratio with high fixed cost means high operating leverage: profit grows fast with volume but falls fast too.

### Example
Price ₹100; variable cost ₹60 → CM ₹40; CM ratio **40%**. 5,000 units: CM = ₹2,00,000; fixed cost ₹1,50,000 → profit ₹50,000; DOL = 2,00,000/50,000 = **4**. A 10% rise in volume lifts profit about 40% (check: 5,500 × 40 = 2,20,000 − 1,50,000 = 70,000 = +40%).

### In the news
See news box. For D-Mart, EBITDA margin of ~7% sits on a CM of perhaps 15% of sales (gross margin level, not reported here); the gap is fixed store cost, so same-store volume growth matters.

### Interview angle
> [!question] How it is asked
> "Product A has 50% margin, B has 30%; which should we push?" (answer: depends on CM per constraint)

> [!tip] Strong answer includes
> - CM vs gross margin distinction (variable vs COGS)
> - Per-constraint ranking, not just ratio
> - Operating leverage and risk
> - Use in pricing floors and promotions

---

## 3. Absorption Costing vs Marginal Costing
> 🟠 Tier 2 · _Tracker hint:_ Absorption: fixed OH absorbed in product; Marginal: only variable costs in product cost

### Definition
- **Absorption (full) costing:** product cost = direct materials + direct labour + variable OH + **fixed manufacturing OH**. Required for external reporting (Ind AS 2 inventories).
- **Marginal (variable) costing:** product cost = variable costs only; fixed manufacturing OH is a **period cost**. Used for internal decisions.

Profit differs when production ≠ sales:
$$\text{Absorption profit} - \text{Marginal profit} = (\text{Closing stock} - \text{Opening stock units}) \times \text{Fixed OH per unit}$$

Production > sales → absorption profit is higher (fixed cost deferred into stock). Over a long period both give the same total profit. Absorption can tempt managers to overproduce to show profit.

### Example
Price ₹100; variable cost ₹60; fixed OH ₹2,00,000 (budgeted ₹20 per unit on 10,000 units); production 10,000, sales 8,000.
- Marginal: CM = 8,000 × 40 = 3,20,000 − 2,00,000 = **₹1,20,000**; closing stock 2,000 × 60 = ₹1,20,000.
- Absorption: 8,000 × (100 − 80) = **₹1,60,000**; closing stock 2,000 × 80 = ₹1,60,000.
Difference = ₹40,000 = 2,000 × ₹20 ✓.

### In the news
See news box. Under Eternal's inventory-led model, unsold stock sits on the balance sheet; how costs are absorbed into inventory affects reported profit.

### Interview angle
> [!question] How it is asked
> "Why does profit differ under the two methods, and which would you use for decisions?"

> [!tip] Strong answer includes
> - Treatment of fixed OH and the difference formula
> - Direction of the difference (production vs sales)
> - Marginal for decisions; absorption for external reporting
> - The risk of overproduction incentives

---

## 4. Standard Costing & Variances
> 🟠 Tier 2 · _Tracker hint:_ Material price & usage variance; Labor rate & efficiency variance; OH variance

### Definition
Standard costing sets **predetermined costs** per unit and analyses differences (variances) from actual results. Convention: **F** (favourable, profit up) or **A** (adverse).

| Variance | Formula |
|---|---|
| Material price | (Std price − Actual price) × Actual quantity purchased/used |
| Material usage | (Std quantity for actual output − Actual quantity) × Std price |
| Labour rate | (Std rate − Actual rate) × Actual hours |
| Labour efficiency | (Std hours for actual output − Actual hours) × Std rate |
| Variable OH spending / efficiency | Same logic on OH rate and hours |
| Fixed OH | Budget − Actual (expenditure); Absorbed − Budget (volume) |

Price variances usually trace to purchasing; usage and efficiency to production. Investigate material variances by cause, not blame.

### Example
Output 1,000 units. Material: standard 2 kg at ₹50; actual 2,200 kg at ₹52. Price = (50 − 52) × 2,200 = **₹4,400 A**; usage = (2,000 − 2,200) × 50 = **₹10,000 A**; total ₹14,400 A (check: 2,200 × 52 = 1,14,400 vs standard 1,00,000 ✓).
Labour: standard 3 h at ₹200; actual 3,100 h at ₹195. Rate = (200 − 195) × 3,100 = **₹15,500 F**; efficiency = (3,000 − 3,100) × 200 = **₹20,000 A**; net ₹4,500 A (check: 3,100 × 195 = 6,04,500 vs 6,00,000 ✓).

### In the news
See news box. D-Mart's operating-cost slippage is a "variance" at group level; each store's staffing hours and utilities would be tracked against standard.

### Interview angle
> [!question] How it is asked
> "Material cost is 8% above budget. Diagnose the variance."

> [!tip] Strong answer includes
> - Split into price vs usage (and rate vs efficiency)
> - Interdependence: cheaper material may raise usage
> - Root causes and owners
> - Management by exception (investigate only material variances)

---

## 5. Activity-Based Costing (ABC)
> 🟠 Tier 2 · _Tracker hint:_ Assigns costs to activities → to products based on actual usage; reduces cross-subsidization

### Definition
Traditional costing spreads overhead using a volume base (labour hours, units), which **over-costs high-volume simple products and under-costs low-volume complex ones**. ABC: (1) identify activities (setups, inspections, order handling); (2) pool costs by activity; (3) choose a **cost driver** (number of setups); (4) compute the rate = pool cost ÷ driver volume; (5) assign to products by their driver consumption.

$$\text{Product OH} = \sum_{\text{activities}} \text{Rate}_a \times \text{Driver usage}_a$$

Benefits: accurate product and customer profitability, better pricing and portfolio decisions. Costs: data and effort; **time-driven ABC** simplifies this. Useful in distribution and logistics (cost per order line, per delivery, per SKU).

### Example
Setup overhead ₹6,00,000. Product A: 10,000 units, 20 setups; Product B: 1,000 units, 40 setups. Rate = 6,00,000/60 = ₹10,000 per setup. A: 2,00,000 → **₹20/unit**; B: 4,00,000 → **₹400/unit**. Traditional unit-based allocation: 6,00,000/11,000 = ₹54.55/unit to both: A over-costed (54.55 vs 20), B hugely under-costed (54.55 vs 400): cross-subsidy.

### In the news
See news box. Quick-commerce players must cost each order by activity (pick, pack, rider, returns, wastage); an average cost per order hides which stores or baskets lose money.

### Interview angle
> [!question] How it is asked
> "Why do some products look profitable but destroy value?" or "Product A is our bestseller, but should we keep the long tail of SKUs?"

> [!tip] Strong answer includes
> - Cost pools and drivers; the cross-subsidy problem
> - Numeric illustration
> - Decision use: pricing, SKU rationalisation, customer profitability
> - Limitations (data, cost) and time-driven ABC

---

## 6. Transfer Pricing
> 🟠 Tier 2 · _Tracker hint:_ Price charged between divisions; market price, cost-based, or negotiated

### Definition
The internal price at which one division sells to another. Goals: goal congruence (decisions that maximise firm profit), divisional autonomy, performance evaluation. Methods:
- **Market-based:** best when there is a competitive external market.
- **Cost-based:** variable cost, full cost, or cost-plus; simple but can pass on inefficiency.
- **Negotiated:** within the range set below.

General rule: **minimum transfer price = variable cost + opportunity cost** (lost contribution from external sales if capacity is full); **maximum = lower of buyer's external purchase price and net marginal revenue**. The tax angle: cross-border transfer pricing is regulated (arm's-length principle, Indian Income Tax rules).

### Example
Division A: variable cost ₹40, full cost ₹55, market price ₹70. Division B can buy outside at ₹65.
- **Spare capacity in A:** minimum ₹40; maximum ₹65 → any price in **₹40–65** benefits the firm.
- **A at full capacity (could sell all at ₹70):** minimum = 40 + (70 − 40) = ₹70 > ₹65, so B should **buy outside**; forcing an internal transfer would lose ₹5 per unit.

### In the news
See news box. In integrated groups (Reliance, Tata, Eternal's Hyperpure supply to Zomato and Blinkit) internal prices decide which unit reports profit, so fair transfer pricing matters for both incentives and tax.

### Interview angle
> [!question] How it is asked
> "Division A has spare capacity; B wants a lower price. What price should they agree?"

> [!tip] Strong answer includes
> - The min/max range logic
> - Opportunity cost under full vs spare capacity
> - Behavioural effects: autonomy and fairness
> - Tax and arm's-length compliance for cross-border cases

---

## 7. Make vs Buy Decision
> 🟠 Tier 2 · _Tracker hint:_ Relevant costs only; ignore sunk costs; include opportunity cost

### Definition
Compare the **relevant (incremental, avoidable) cost** of making in-house against the purchase price, plus **opportunity cost** of capacity.

$$\text{Relevant cost of making} = DM + DL + \text{Variable OH} + \text{Avoidable fixed cost} + \text{Opportunity cost of capacity}$$

Allocated fixed overhead that continues if you buy is **not relevant**. Qualitative factors: quality, supply risk, IP, flexibility, supplier dependence (see strategic sourcing in [[002 Procurement & Strategic Sourcing]]), lead time, learning. Also consider long-term capacity and exit costs.

### Example
Component: 10,000 units/year. Supplier price **₹90**. In-house per unit: DM 40, DL 20, variable OH 10, allocated fixed OH 30 (of which only ₹5 avoidable).
Relevant make cost = 40 + 20 + 10 + 5 = **₹75** < ₹90, so **make** (saves ₹15 × 10,000 = ₹1,50,000).
If buying frees capacity that earns ₹2,00,000 contribution elsewhere (₹20/unit), make cost = 75 + 20 = **₹95 > ₹90**, so **buy**.

### In the news
See news box. Eternal's shift to owning inventory at Blinkit is a "make vs buy" in the sourcing sense: take on stock risk and capture margin, or leave it to sellers and earn a commission.

### Interview angle
> [!question] How it is asked
> "Should we manufacture this component or outsource it?"

> [!tip] Strong answer includes
> - Relevant-cost logic: avoidable costs only, capacity opportunity cost
> - Numeric comparison
> - Strategic and risk factors (core competence, supplier risk)
> - Reversibility and contract structure

---

## 8. Target Costing
> 🟠 Tier 2 · _Tracker hint:_ Market price – desired profit = target cost; reverse-engineer cost from price

### Definition
Instead of cost-plus pricing, start with the **customer's price**:

$$\text{Target cost} = \text{Target selling price} - \text{Target profit}$$

If the current cost exceeds the target, the **cost gap** must be closed through value engineering (redesign, cheaper materials, fewer parts), supplier negotiation (supplier co-design), process improvement and DFMA, before launch. Associated with Toyota and Japanese manufacturers; in India, seen in Tata Nano-type low-price products and consumer durables. Key: involve cross-functional teams early because ~70–80% of the cost is locked in at the design stage.

### Example
Market price ₹1,200; required margin 20% on price → profit ₹240 → **target cost ₹960**. Current estimate ₹1,050 → gap **₹90** (8.6% of current cost). Plan: material redesign saves ₹40, supplier renegotiation ₹30, process change ₹20 = ₹90, gap closed.

### In the news
See news box. With D-Mart's margin edging down, "everyday low price" retail effectively runs target costing: price set by the market, costs must follow.

### Interview angle
> [!question] How it is asked
> "A competitor launched a product at 20% lower price. How would you respond on cost?"

> [!tip] Strong answer includes
> - Price-minus logic
> - Cost gap and levers (design, supplier, process)
> - Cross-functional early involvement
> - Distinguish from cost-plus pricing

---

## 9. Life Cycle Costing
> 🟠 Tier 2 · _Tracker hint:_ Total cost over product/asset life: acquisition + operating + maintenance + disposal

### Definition
Life-cycle cost (LCC) captures the **total cost of ownership** over the asset's life:

$$LCC = \text{Acquisition} + PV(\text{Operating}) + PV(\text{Maintenance}) + PV(\text{Disposal}) - PV(\text{Salvage})$$

Use discounting to compare options with different timing. For manufacturers, LCC also includes R&D, design and decommissioning costs (product life cycle costing). Important in fleet, plant and equipment choices where the **cheapest purchase is often not the cheapest to own**. Related to total cost of ownership (TCO) in procurement.

### Example
Machine A: price ₹10 lakh, operating ₹2 lakh/yr, maintenance ₹0.5 lakh/yr, salvage ₹1 lakh; 5 years; 10%. Annual 2.5 × 3.7908 = 9.477; salvage PV = 1 × 0.6209 = 0.621. **LCC = 10 + 9.477 − 0.621 = ₹18.86 lakh**.
Machine B: price ₹7 lakh, operating ₹3.5 lakh/yr, maintenance ₹1 lakh/yr, salvage ₹0.5 lakh. Annual 4.5 × 3.7908 = 17.059; salvage PV 0.310. **LCC = 7 + 17.059 − 0.310 = ₹23.75 lakh**. A is cheaper over life despite the higher price.

### In the news
See news box. Fleet choices for delivery (EV vs petrol two-wheelers) depend on LCC; riders and operators weigh purchase price against running cost over many years.

### Interview angle
> [!question] How it is asked
> "Which truck should we buy: the cheaper one or the efficient one?"

> [!tip] Strong answer includes
> - All cost phases and discounting
> - A numeric comparison
> - Non-cost factors: downtime, resale, reliability
> - Sensitivity to fuel/usage assumptions

---

## 10. Relevant Costs for Decisions
> 🟠 Tier 2 · _Tracker hint:_ Sunk cost = ignore; Opportunity cost = include; Incremental cash flows only

### Definition
A cost is **relevant** only if it is **future, cash and different between alternatives**. Therefore:
- **Sunk costs** (already spent): ignore.
- **Committed/non-cash/allocated costs** (depreciation, allocated overhead that does not change): ignore.
- **Opportunity costs** (benefit forgone by choosing one use of a resource): include.
- **Incremental revenues and costs**: include.

Standard applications: special orders, make vs buy, shutdown, further processing (joint product costs are sunk at the split-off point), scarce-resource usage. For material in stock: relevant cost is the replacement cost if it will be replaced, or the best alternative use (resale value) if not.

### Example
Special order: 1,000 units at ₹80. Variable cost ₹60; allocated fixed OH ₹30/unit (full cost ₹90); spare capacity. Relevant: revenue 80 − variable 60 = ₹20/unit → **+₹20,000, accept** even though price < full cost. ₹5 lakh already spent on market research is sunk. If capacity is full and displaced sales earn ₹25/unit contribution, the order loses ₹5/unit, so reject.

### In the news
See news box. For D-Mart opening a store, land and fit-out already paid are sunk; the decision to keep a weak store open should use future incremental cash flows only.

### Interview angle
> [!question] How it is asked
> "We have spent ₹10 crore on this plant; should we continue?" (sunk cost test)

> [!tip] Strong answer includes
> - Future, cash, differential test
> - Explicit treatment of sunk costs and opportunity costs
> - Spare vs full capacity distinction
> - Qualitative factors: reputation, long-term pricing

---

## 11. ⭐ Advanced: Throughput accounting and the bottleneck
> ⭐ Advanced · _Added beyond the tracker_

### Definition
From the Theory of Constraints: **Throughput** = Revenue − Totally variable costs (usually materials). Labour and overhead are treated as fixed in the short run. Rank products by **throughput per unit of bottleneck time**, not by margin %.

$$\text{Throughput per bottleneck minute} = \frac{\text{Price} - \text{Material cost}}{\text{Minutes on bottleneck}}$$

Key metrics: Throughput (T), Inventory (I, investment), Operating expense (OE). Net profit = T − OE. Improve by exploiting the bottleneck (never starve it), subordinating other processes, then elevating capacity.

### Example
Bottleneck available 480 min/day. Product X: price ₹100, material ₹40 → T = ₹60; 2 min → **₹30/min**. Product Y: price ₹90, material ₹30 → T = ₹60; 1.5 min → **₹40/min**. Y wins: make 480/1.5 = 320 units × 60 = **₹19,200** vs X: 240 units × 60 = **₹14,400**, even though both earn ₹60 per unit.

### In the news
See news box. In dark stores the bottleneck is often picker capacity or rider availability; contribution should be judged per constrained resource-hour.

### Interview angle
> [!question] How it is asked
> "You have a bottleneck machine and two products; which to prioritise?"

> [!tip] Strong answer includes
> - Throughput per bottleneck minute (not margin %)
> - Identify the constraint, protect it
> - Numeric comparison
> - Link to OEE and capacity planning ([[105 Operations & SCM Guesstimates]])

---

## 12. ⭐ Advanced: Time-driven ABC for logistics and service operations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Time-driven ABC (TDABC)** (Kaplan and Anderson) simplifies ABC by using two estimates only: the **capacity cost rate** and the **time required** for each activity.

$$\text{Capacity cost rate} = \frac{\text{Cost of resource pool}}{\text{Practical capacity (minutes)}}$$
$$\text{Cost of activity} = \text{Rate} \times \text{Minutes per occurrence}$$

Practical capacity is typically 80–85% of theoretical. Unused capacity is shown explicitly, which highlights idle resources. Ideal for order processing, warehouses, customer service and returns.

### Example
Order-processing team costs ₹12,00,000/month; 10 staff × 20 days × 420 min = 84,000 minutes. Rate = 12,00,000/84,000 = **₹14.29/min**. A standard order takes 5 minutes = **₹71.4**; a returns order 18 minutes = **₹257**. If 60,000 minutes are used, utilisation = 71% and the cost of unused capacity = 24,000 × 14.29 = ₹3.43 lakh/month.

### In the news
See news box. Costing each order's handling time makes the economics of small baskets in quick commerce visible and shows where margin is lost.

### Interview angle
> [!question] How it is asked
> "How would you find out which customers are unprofitable to serve?"

> [!tip] Strong answer includes
> - Two parameters: rate and time
> - Cost of unused capacity
> - Using it to price (minimum order value, delivery fee)
> - Contrast with classic ABC

---
## 🔗 Go deeper: expansion notes
- [[225 Budgeting, Variance Analysis & Balanced Scorecard|Budgeting, Variance Analysis & Balanced Scorecard]]
- [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement|Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]
- [[227 GST & Indirect Tax for Supply Chains|GST & Indirect Tax for Supply Chains]]
