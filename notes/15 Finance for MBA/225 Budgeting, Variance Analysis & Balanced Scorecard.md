---
tags: [finance-for-mba, tier2]
area: Finance for MBA
topic: "Budgeting, Variance Analysis & Balanced Scorecard"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Budgeting, Variance Analysis & Balanced Scorecard

⬅ [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]] · [[_Index - Finance for MBA|Finance for MBA]] · [[226 Corporate Finance Essentials - Capital Structure & Cost of Capital]] ➡

> **Area:** Finance for MBA · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Purpose of Budgeting and the Master Budget]]
2. [[#2. Budget Types: Static, Flexible, Zero-Based, Rolling, Incremental, Activity-Based]]
3. [[#3. Operating Budgets: Sales, Production and Material Purchase Chain]]
4. [[#4. Cash Budget and Capital Expenditure Budget]]
5. [[#5. Responsibility Accounting: Cost, Revenue, Profit and Investment Centres]]
6. [[#6. Static vs Flexible Budgets: The First Variance Cut]]
7. [[#7. Sales Variances: Price, Volume, Mix and Quantity]]
8. [[#8. Material and Labour Variances]]
9. [[#9. Overhead Variances and the Full Variance Tree]]
10. [[#10. Interpreting Variances: Investigate, Interrelate, Decide]]
11. [[#11. ROI, Residual Income and EVA]]
12. [[#12. The Balanced Scorecard and Strategy Maps]]
13. [[#13. KPI Cascading, OKRs and Linking Pay to the Scorecard]]
14. [[#14. Budgeting Pitfalls, Behavioural Effects and Beyond Budgeting]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Budgets at national scale, and what happens when cost discipline overrides everything else
> **Union Budget 2026-27 (presented February 2026).** The Centre budgeted capital expenditure of **₹12.2 lakh crore** for 2026-27 (about ₹11 lakh crore revised estimate for 2025-26), a **fiscal deficit of 4.3% of GDP** (4.4% revised for 2025-26), total expenditure of **₹53.5 lakh crore** and gross market borrowing of **₹17.2 lakh crore**. A national budget is a static plan with revised estimates (RE) published a year later, which is the same budget-versus-actual loop a plant manager faces every month. ([PIB: Highlights of Union Budget 2026-27](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2221455&lang=1&reg=3))
>
> **Kraft Heinz and zero-based budgeting (2015-2025).** 3G Capital's model required executives to justify every expense from scratch. After the roughly **$50 billion** Kraft-Heinz merger closed in July 2015, thousands of jobs were cut and marketing and innovation spend was squeezed; in **February 2019** the company announced a **$15.4 billion write-down** on the Kraft and Oscar Mayer brands and the stock fell **27% in one day**. A September 2025 commentary reports the company announcing a demerger and describes organic growth turning negative after the budget cuts. The cautionary lesson is that cost budgets without brand and capability investment can destroy value. ([PitchBook](https://pitchbook.com/news/articles/how-3g-capital-and-a-50b-buyout-turned-kraft-heinz-upside-down); [The Elevator Pitch](https://elevatorpitch.substack.com/p/kraft-heinz-demerger-3g-failure))
>
> **ZBB adoption is minority practice (2026 industry guide).** One analytics-vendor guide reports traditional incremental budgeting at "roughly 55-60%" of companies versus ZBB at "15-20%" (25-35% in large enterprises); these are the vendor's estimates, not audited survey data, so quote them as indicative. ([Polestar Analytics](https://www.polestaranalytics.com/blog/zero-based-budgeting-in-2026))
>
> Sub-topics that say **"See news box"** reuse these items. All company numbers in worked examples below are illustrative, not drawn from any real firm.

---
## 1. Purpose of Budgeting and the Master Budget
> 🟠 Tier 2 · _Key points:_ planning, coordination, authorisation, motivation, control; master budget = operating + financial budgets

### Definition
A **budget** is a quantified plan for a defined period, expressed in money (and often units). It serves six purposes: **planning** (turn strategy into numbers), **coordination** (sales, production, purchasing and finance work to one plan), **resource authorisation**, **communication**, **motivation** (targets) and **control** (compare actual with plan, then act). The **master budget** is the integrated set:

| Layer | Contents |
|---|---|
| Operating budgets | Sales, production, direct material usage and purchases, direct labour, factory overhead, ending inventory, COGS, selling & admin |
| Financial budgets | Capex budget, cash budget, budgeted income statement, budgeted balance sheet |

The **principal budget factor** (limiting factor) is the constraint that sets the starting point: usually sales demand, but it can be machine capacity, a scarce material or labour. Budgeting is **top-down** (imposed, fast, low buy-in), **bottom-up/participative** (better information and commitment, but invites slack) or a negotiated blend. Budgets feed performance management ([[042 Cost & Budget Management]] covers project budgets; this note covers the operating-company view) and cost behaviour from [[110 Cost Accounting for Operations]].

### Example
A Nashik auto-component plant starts from the sales forecast (see [[004 Demand Forecasting & Planning]]) of 10,000 housings, then derives a production plan, material purchases, labour hours, overhead and cash needs. If the foundry supplying castings can deliver only 36,000 kg a month, material becomes the **principal budget factor** and sales are capped at 9,000 housings (4 kg each) no matter what the sales team promises.

### In the news
See news box. The Union Budget is a master budget in miniature: receipts (sales), expenditure (costs), capex and a borrowing (financing) plan, followed by revised estimates.

### Interview angle
> [!question] How it is asked
> "How would you build next year's budget for a manufacturing business, and where do you start?"

> [!tip] Strong answer includes
> - Start with the limiting factor, usually the demand forecast, then derive production, purchases, labour and cash
> - Distinguish operating budgets from financial budgets
> - Name the S&OP link: the budget is the annual financial view of the operating plan ([[120 Integrated Business Planning (IBP) & S&OP Maturity]])
> - Mention participation vs imposed targets and the risk of slack

---
## 2. Budget Types: Static, Flexible, Zero-Based, Rolling, Incremental, Activity-Based
> 🟠 Tier 2 · _Key points:_ static vs flexible; incremental vs ZBB; rolling; ABB; when to use each

### Definition
| Type | How it works | Best for | Weakness |
|---|---|---|---|
| **Static (fixed)** | Built once for one planned activity level; not changed | Stable discretionary costs, fixed-cost centres | Useless for judging variable costs when volume differs |
| **Flexible** | Costs restated for the **actual activity level** (fixed stay fixed, variable move with volume) | Manufacturing and service cost control | Needs reliable cost-behaviour split |
| **Incremental** | Last year + a % adjustment | Simple, fast | Perpetuates waste, rewards inflated bases |
| **Zero-based (ZBB)** | Every activity justified from zero as "decision packages", ranked by benefit | Overhead and support functions, turnarounds | Time-consuming; short-term bias; can cut capability |
| **Rolling (continuous)** | Always N future quarters; one is added as one expires | Volatile markets, fast-changing demand | Review fatigue; targets keep moving |
| **Activity-based (ABB)** | Budget resources from planned cost-driver volumes (see ABC in [[110 Cost Accounting for Operations]]) | Overhead-heavy firms | Needs good driver data |

Related: **driver-based planning** (sales volume, headcount or tonnes drive cost lines automatically) and **beyond budgeting** (replace fixed annual targets with relative targets and rolling forecasts; see sub-topic 14).

### Example
A warehouse spends ₹60 lakh a year on admin. Incremental: +5% → ₹63 lakh. ZBB: each activity (inventory audit, vendor payments, reporting) is costed from zero; the team finds a ₹9 lakh reporting package duplicated by the ERP and keeps ₹51 lakh. A rolling 4-quarter forecast then restates the plan every quarter as volumes change.

### In the news
See news box. Kraft Heinz is the standard ZBB cautionary tale; the 15-20% ZBB adoption estimate shows it remains a minority method, usually applied to overheads rather than whole businesses.

### Interview angle
> [!question] How it is asked
> "Would you use zero-based budgeting to cut costs in this company?"

> [!tip] Strong answer includes
> - ZBB suits discretionary overhead, not capacity-building or brand spend
> - Cost of doing it every year vs a periodic reset
> - Pair ZBB savings with protected investment lines
> - Alternatives: flexible budgets for variable cost, rolling forecasts for volatile demand

---
## 3. Operating Budgets: Sales, Production and Material Purchase Chain
> 🟠 Tier 2 · _Key points:_ production = sales + closing FG − opening FG; purchases = usage + closing RM − opening RM

### Definition
$$\text{Production units}=\text{Sales units}+\text{Closing FG}-\text{Opening FG}$$
$$\text{Purchases}=\text{Material used}+\text{Closing RM}-\text{Opening RM}$$
Direct labour hours = production × standard hours/unit; overhead = variable rate × activity + fixed budget. Inventory policy (days or % of next period's sales) is the lever that converts a demand plan into a production plan; it links directly to [[003 Inventory Management]] and [[005 Production & Operations Planning]].

### Example
Quarterly sales (units) 20,000 / 24,000 / 30,000 / 26,000 and next-year Q1 forecast 22,000. Policy: closing finished goods = **20% of next quarter's sales**; opening stock 4,000; 4 kg material per unit.

| Quarter | Sales | Closing FG | Opening FG | Production | Material (kg) |
|---|---|---|---|---|---|
| Q1 | 20,000 | 4,800 | 4,000 | 20,800 | 83,200 |
| Q2 | 24,000 | 6,000 | 4,800 | 25,200 | 100,800 |
| Q3 | 30,000 | 5,200 | 6,000 | 29,200 | 116,800 |
| Q4 | 26,000 | 4,400 | 5,200 | 25,200 | 100,800 |

Production is smoother than sales (peak 29,200 against 30,000 sales) because stock absorbs part of the Q3 peak. Total production 100,400 vs total sales 100,000 (closing 4,400 minus opening 4,000).

### In the news
See news box. At national level the equivalent chain is receipts, expenditure and borrowing: gross borrowing of ₹17.2 lakh crore finances the roughly ₹17 lakh crore gap between ₹53.5 lakh crore of spending and ₹36.5 lakh crore of non-debt receipts (gross borrowing also covers repayments).

### Interview angle
> [!question] How it is asked
> "Sales are forecast at 1 lakh units; opening stock is 10,000 and you want 15,000 at close. How many do you produce?"

> [!tip] Strong answer includes
> - Production = sales + closing − opening (here 1,05,000)
> - State assumptions on safety stock or stock-days
> - Check capacity (OEE, shifts) before accepting the production budget ([[018 Capacity Management & OEE]])
> - Notice that seasonality can be levelled by stock at a holding cost

---
## 4. Cash Budget and Capital Expenditure Budget
> 🟠 Tier 2 · _Key points:_ cash timing, not profit; collections lag, payment lag; capex approved separately via NPV/IRR

### Definition
A **cash budget** forecasts receipts and payments by period to show the closing balance, any shortfall to be financed (overdraft, working-capital limit) or surplus to be invested. It uses **cash timing**, not accrual: depreciation is excluded, sales are cash only when collected, purchases are cash only when paid.
$$\text{Closing cash}=\text{Opening cash}+\text{Receipts}-\text{Payments}$$
The **capex budget** lists approved long-term projects, phased by spend, each justified by discounted cash flow ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]], [[109 Valuation Basics (NPV, IRR, DCF)]]); its cash outflows then flow into the cash budget and its depreciation into the P&L budget. Working capital sizing links to [[136 Supply Chain Finance & Working Capital]].

### Example
Sales (₹ lakh): Feb 100, Mar 120, Apr 110, May 130. Terms: 40% cash, 60% collected the next month. Purchases (₹ lakh): Feb 60, Mar 70, Apr 65, paid the next month. Cash operating costs 25 per month; capex of 40 in April; opening cash on 1 March 20.

| Month | Collections | Supplier payments | Opex | Capex | Net | Closing |
|---|---|---|---|---|---|---|
| Mar | 0.4×120 + 0.6×100 = 108 | 60 | 25 | 0 | +23 | 43 |
| Apr | 0.4×110 + 0.6×120 = 116 | 70 | 25 | 40 | −19 | 24 |
| May | 0.4×130 + 0.6×110 = 118 | 65 | 25 | 0 | +28 | 52 |

April is the pinch point even though the business is profitable: the capex and the receivable lag cut cash by ₹19 lakh. If the minimum operating balance were 30, a ₹6 lakh short-term borrowing would be needed in April.

### In the news
See news box. The Centre's ₹12.2 lakh crore capex budget is the national capex budget; its timing across quarters is a cash-planning issue in the same way.

### Interview angle
> [!question] How it is asked
> "The company reports a profit but keeps running out of cash. Why?"

> [!tip] Strong answer includes
> - Receivable and inventory build, capex and debt repayment consume cash but are not expenses
> - Walk through a monthly cash budget with collection and payment lags
> - Remedies: faster collections, supplier terms, supply chain finance, phasing capex
> - Distinguish profit, cash flow and funding

---
## 5. Responsibility Accounting: Cost, Revenue, Profit and Investment Centres
> 🟠 Tier 2 · _Key points:_ controllability principle; centre types; performance measure per centre

### Definition
**Responsibility accounting** assigns costs and revenues to the manager who can influence them and judges that manager only on **controllable** items (the controllability principle).

| Centre | Manager controls | Typical measure |
|---|---|---|
| **Cost centre** (standard: production line, warehouse, HR) | Costs only | Cost vs flexed budget, cost per unit/pick, variances |
| **Revenue centre** (sales region) | Revenue | Sales vs budget, price/volume/mix |
| **Profit centre** (business unit, plant with transfer prices) | Revenue and costs | Segment margin, profit vs budget |
| **Investment centre** (division with capital authority) | Profit and capital employed | ROI, residual income, EVA |

Design points: separate controllable from allocated costs; use **transfer prices** where profit centres trade internally ([[110 Cost Accounting for Operations]]); beware that treating a logistics cost centre only on cost per pallet can push it to under-serve customers.

### Example
A distribution centre (DC) is a **cost centre** with budget ₹2.4 crore. The regional sales head is a **revenue centre**. The state business unit combining both is a **profit centre**. A DC manager is not accountable for the freight surcharge triggered by a customer's last-minute order change (uncontrollable by DC; controllable by the sales team), so it is booked to sales or reported as a separate line.

### In the news
See news box. Union Budget heads are effectively responsibility centres: each ministry owns its allocation and is reviewed against the revised estimate.

### Interview angle
> [!question] How it is asked
> "How would you evaluate the performance of a plant manager vs a regional sales head?"

> [!tip] Strong answer includes
> - Match the measure to the decision rights: cost, revenue, profit or capital
> - Controllable vs uncontrollable; allocated costs shown below the line
> - Risk of sub-optimisation (each centre hitting its number at the firm's expense)
> - Add non-financial measures (see Balanced Scorecard)

---
## 6. Static vs Flexible Budgets: The First Variance Cut
> 🟠 Tier 2 · _Key points:_ flex the budget to actual volume; separate volume effect from efficiency/price effects

### Definition
A static budget compared with actual results mixes **volume** effects with **spending/efficiency** effects. The **flexible budget** restates the budget to actual output so each variance is clean:
- **Sales volume variance** = flexed budget − static budget (effect of selling more or less than planned)
- **Flexible-budget variance** = actual − flexed budget (price, cost and efficiency effects)

### Example (used for sub-topics 7-9)
Pump housing: budget 10,000 units at ₹1,500. Standard unit cost: material 4 kg × ₹120 = ₹480; labour 2.5 h × ₹160 = ₹400; variable overhead 2.5 h × ₹40 = ₹100; fixed overhead budget ₹20,00,000, absorbed at ₹80 per labour hour (₹200/unit at 10,000 units). Standard cost ₹1,180; standard profit ₹320/unit; **budgeted profit ₹32,00,000**.

Actual: sold and produced 9,200 units at ₹1,540; material 38,000 kg at ₹126; labour 24,000 h at ₹158; variable overhead ₹9,90,000; fixed overhead ₹20,80,000. **Actual profit = ₹25,18,000** (revenue 1,41,68,000 − costs 1,16,50,000).

| Line | Static | Flexed (9,200 units) | Actual |
|---|---|---|---|
| Revenue | 1,50,00,000 | 1,38,00,000 | 1,41,68,000 |
| Variable cost | 98,00,000 | 90,16,000 | 95,70,000 |
| Fixed overhead | 20,00,000 | 20,00,000 | 20,80,000 |
| Profit | 32,00,000 | 27,84,000 | 25,18,000 |

Volume variance = ₹4,16,000 A (static vs flexed); flexible-budget variance = ₹2,66,000 A (flexed vs actual). Total ₹6,82,000 A. Check: 32,00,000 − 25,18,000 = 6,82,000.

### In the news
See news box. A national RE is a "flexed" view: revenues and spending are restated to what actually happened before judging the plan.

### Interview angle
> [!question] How it is asked
> "Plant costs are 8% over budget. Is that bad?"

> [!tip] Strong answer includes
> - Ask whether volume was higher; flex the budget before judging
> - Separate volume from price/efficiency variances
> - Fixed costs do not flex; per-unit fixed cost rises with lower volume
> - Conclude with actions, not just numbers

---
## 7. Sales Variances: Price, Volume, Mix and Quantity
> 🟠 Tier 2 · _Key points:_ price = (AP − SP) × AQ; volume at standard margin; mix and quantity split

### Definition
$$\text{Sales price}=(AP-SP)\times AQ,\qquad \text{Sales volume (profit)}=(AQ-BQ)\times \text{Std margin}$$
For several products, the **volume variance splits into quantity and mix**:
$$\text{Quantity}=(\text{Total actual units}-\text{Total budget units})\times \text{Budget mix}_i\times \text{Std margin}_i$$
$$\text{Mix}=(\text{Actual units}_i-\text{Total actual units}\times \text{Budget mix}_i)\times \text{Std margin}_i$$
Mix is favourable when the sales shift toward higher-margin products. Use margin (not revenue) so the variance explains profit.

### Example
Single product (the pump housing): price = (1,540 − 1,500) × 9,200 = **₹3,68,000 F**; volume = (9,200 − 10,000) × 320 = **₹2,56,000 A**.

Two products: budget A 6,000 units (price ₹100, std cost ₹60, margin ₹40) and B 4,000 (₹200, ₹150, margin ₹50); budgeted profit ₹4,40,000. Actual A 4,500 at ₹98; B 5,000 at ₹205.

| Product | Price variance | Quantity | Mix |
|---|---|---|---|
| A | (98 − 100) × 4,500 = 9,000 A | (9,500 − 10,000) × 0.6 × 40 = 12,000 A | (4,500 − 5,700) × 40 = 48,000 A |
| B | (205 − 200) × 5,000 = 25,000 F | (9,500 − 10,000) × 0.4 × 50 = 10,000 A | (5,000 − 3,800) × 50 = 60,000 F |
| Total | **16,000 F** | **22,000 A** | **12,000 F** |

Check: 4,40,000 − 22,000 + 12,000 + 16,000 = **₹4,46,000** = actual units at standard margin plus price variances. Interpretation: total volume fell 5% (quantity adverse) but the shift toward B (higher margin) earned a favourable mix; B's price premium more than offset A's discount.

### In the news
See news box. When marketing is cut under a cost budget, the damage shows up later as volume and mix variances, as the Kraft Heinz case (organic growth turning negative after budgets were gutted) illustrates.

### Interview angle
> [!question] How it is asked
> "Revenue is flat but profit fell. Which variances would you compute?"

> [!tip] Strong answer includes
> - Price, volume, mix; mix measured on margin
> - Check whether discounts bought volume that was not worth it
> - Decompose by customer or channel using the same logic
> - Link to the profitability framework in [[025 Case Interview — Profitability]]

---
## 8. Material and Labour Variances
> 🟠 Tier 2 · _Key points:_ price/rate vs usage/efficiency; material mix and yield; idle time

### Definition
| Variance | Formula | Usual owner |
|---|---|---|
| Material price | (SP − AP) × AQ purchased | Purchasing |
| Material usage | (SQ for actual output − AQ) × SP | Production |
| Labour rate | (SR − AR) × actual hours paid | HR/Production planning |
| Labour efficiency | (Std hours for actual output − Actual hours) × SR | Production |
| Idle time | Idle hours × SR (adverse) | Planning/maintenance |

Positive = favourable (F), negative = adverse (A). **Usage splits into mix and yield** when several materials can be blended: **mix** = (actual quantity in standard proportions − actual quantity) × SP (is the blend cheaper or dearer than standard?); **yield** = (standard input for actual output − total actual input) × average standard price (did the process produce less than it should?).

### Example (pump housing)
- Standard kg for 9,200 units = 36,800; actual 38,000 kg at ₹126.
- Material price = (120 − 126) × 38,000 = **₹2,28,000 A**; usage = (36,800 − 38,000) × 120 = **₹1,44,000 A**; total ₹3,72,000 A.
- Standard hours = 9,200 × 2.5 = 23,000; actual 24,000 h at ₹158.
- Labour rate = (160 − 158) × 24,000 = **₹48,000 F**; efficiency = (23,000 − 24,000) × 160 = **₹1,60,000 A**; total ₹1,12,000 A.

Mix and yield illustration: standard 1 unit = 3 kg X at ₹50 + 2 kg Y at ₹100 (5 kg, ₹350; average ₹70/kg). For 1,000 units the plant used 3,300 kg X and 1,900 kg Y (5,200 kg). Usage = (3,000 − 3,300) × 50 + (2,000 − 1,900) × 100 = −15,000 + 10,000 = **₹5,000 A**. Mix = (3,120 − 3,300) × 50 + (2,080 − 1,900) × 100 = −9,000 + 18,000 = **₹9,000 F** (the dearer material Y was under-used relative to the standard blend); yield = (5,000 − 5,200) × 70 = **₹14,000 A**. Mix + yield = 9,000 − 14,000 = −5,000 ✓.

### In the news
See news box. A supply base squeezed by cost cutting often produces favourable price variances and adverse usage/quality variances: the price variance is booked by purchasing, the usage cost lands on the shop floor.

### Interview angle
> [!question] How it is asked
> "Material price variance is favourable but the plant is losing money. Why?"

> [!tip] Strong answer includes
> - Cheaper material may raise scrap, rework or downtime (usage and efficiency adverse)
> - Interdependence: one cause, several variances; total cost matters
> - Price variance at purchase point (isolate early) vs usage at production
> - Quality link: [[008 Six Sigma & Quality Tools]], [[011 Quality Management (TQM)]]

---
## 9. Overhead Variances and the Full Variance Tree
> 🟠 Tier 2 · _Key points:_ variable OH expenditure and efficiency; fixed OH expenditure and volume (capacity, efficiency); reconcile to profit

### Definition
| Variance | Formula |
|---|---|
| Variable OH expenditure | (Actual hours × std rate) − actual variable OH |
| Variable OH efficiency | (Std hours for actual output − Actual hours) × std rate |
| Fixed OH expenditure | Budgeted fixed OH − Actual fixed OH |
| Fixed OH volume | Absorbed fixed OH (std hours × rate) − Budgeted fixed OH |
| – capacity | (Actual hours − Budgeted hours) × rate |
| – efficiency | (Std hours for actual output − Actual hours) × rate |

**Variance tree:** Budget profit → sales price, sales volume → material price, usage (mix, yield) → labour rate, idle, efficiency → variable OH expenditure, efficiency → fixed OH expenditure, volume (capacity, efficiency) → actual profit.

### Example (pump housing, absorption costing)
Fixed rate = ₹20,00,000 / 25,000 budget hours = ₹80/h.
- Variable OH expenditure = 24,000 × 40 − 9,90,000 = **₹30,000 A**; efficiency = (23,000 − 24,000) × 40 = **₹40,000 A**.
- Fixed OH expenditure = 20,00,000 − 20,80,000 = **₹80,000 A**; volume = 23,000 × 80 − 20,00,000 = **₹1,60,000 A**, which splits into capacity (24,000 − 25,000) × 80 = ₹80,000 A and efficiency (23,000 − 24,000) × 80 = ₹80,000 A.

**Reconciliation (₹):**

| Item | Amount |
|---|---|
| Budgeted profit | 32,00,000 |
| Sales price | +3,68,000 |
| Sales volume | −2,56,000 |
| Material price / usage | −2,28,000 / −1,44,000 |
| Labour rate / efficiency | +48,000 / −1,60,000 |
| Variable OH expenditure / efficiency | −30,000 / −40,000 |
| Fixed OH expenditure / volume | −80,000 / −1,60,000 |
| **Actual profit** | **25,18,000** |

Check: 32,00,000 + 3,68,000 − 2,56,000 − 3,72,000 − 1,12,000 − 70,000 − 2,40,000 = 25,18,000 ✓. Note that the sales volume (₹2,56,000) plus fixed OH volume (₹1,60,000) equals the ₹4,16,000 volume variance in sub-topic 6, because absorption costing splits one economic effect in two.

### In the news
See news box. Fixed-overhead under-absorption is exactly what a lower-volume year looks like in a plant P&L; at a national level the equivalent is a fixed-cost expenditure base (salaries, interest) that does not flex with receipts.

### Interview angle
> [!question] How it is asked
> "Walk me through why actual profit was ₹7 lakh below budget."

> [!tip] Strong answer includes
> - Present the tree: revenue side first, then material, labour, overhead
> - Separate controllable variances from volume-driven under-absorption
> - Identify the two or three largest items and root causes
> - Recommend an action per variance owner with a time frame

---
## 10. Interpreting Variances: Investigate, Interrelate, Decide
> 🟠 Tier 2 · _Key points:_ materiality thresholds; controllability; interdependence; standards review; planning vs operational variance

### Definition
A variance is a prompt to ask a question, not a verdict. Investigate when it is **material** (a rupee or percentage threshold, or a trend over several periods), **controllable**, and **cost-effective to chase**. Common cautions:
- **Interdependence:** buying cheaper material (price F) may raise scrap and rework (usage A, efficiency A); a rush order (labour overtime rate A) may win a customer (sales price/volume F).
- **Planning vs operating variances:** if the standard price was set before a commodity spike, part of the adverse price variance is a **planning** error, not a purchasing failure.
- **Standards drift:** revise standards for learning curves ([[152 Learning Curves, Work Measurement & Productivity]]), new suppliers and yield changes.
- **Statistical control:** treat variances inside normal random variation as noise ([[091 Statistical Quality Control (SQC)]]).
- **Behaviour:** variance reports can push managers to hit one favourable number (e.g., cutting maintenance) at the firm's expense.

### Example
The ₹2,28,000 A material price variance on 38,000 kg: if the market price of the casting alloy rose from ₹120 to ₹124 after standards were set, ₹1,52,000 (4 × 38,000) is a planning variance and only ₹76,000 (2 × 38,000) an operating variance attributable to purchasing. The ₹1,44,000 A usage variance (1,200 kg over, about 3.3% of the 36,800 kg standard) came from a worn die producing scrap, after die maintenance had been deferred to protect machine hours. A good report states these causes and an owner for each.

### In the news
See news box. Kraft Heinz is an extreme case: one commentary reports cost cuts lifting margins to about 30% while organic growth turned negative; non-financial indicators (brand health, volume trends) would have flagged the problem earlier than the cost variances did.

### Interview angle
> [!question] How it is asked
> "The purchasing head says the adverse price variance is not his fault. How would you decide?"

> [!tip] Strong answer includes
> - Split planning (standard) from operating variance
> - Check market indices and contract terms vs actual price paid
> - Consider the full cost, including usage and quality effects
> - Agree materiality limits and owners; do not chase noise

---
## 11. ROI, Residual Income and EVA
> 🟠 Tier 2 · _Key points:_ ROI = profit/investment; RI = profit − charge; EVA = NOPAT − WACC × capital; goal congruence

### Definition
$$ROI=\frac{\text{Operating profit}}{\text{Capital employed}},\qquad RI=\text{Operating profit}-r\times\text{Capital employed}$$
$$EVA=NOPAT-WACC\times\text{Invested capital}=(ROIC-WACC)\times\text{Invested capital},\qquad NOPAT=EBIT\,(1-t)$$
ROI favours percentage returns and can make managers reject projects that beat the cost of capital but dilute the division's average. **RI** and **EVA** charge for capital in absolute terms, so any project with return above the cost of capital raises the measure. EVA (Stern Stewart) adds accounting adjustments (capitalise R&D, add back one-off charges) to approximate economic profit. WACC is built in [[226 Corporate Finance Essentials - Capital Structure & Cost of Capital]]; return ratios are in [[108 Financial Statements & Ratios]].

### Example
Division: capital ₹50 crore, operating profit ₹9 crore, cost of capital 12%. ROI = 18%; RI = 9 − 0.12 × 50 = **₹3 crore**. A project needs ₹10 crore and earns 15% (₹1.5 crore). ROI after the project = 10.5 / 60 = **17.5%** (below 18%, so an ROI-judged manager rejects it); RI = 10.5 − 7.2 = **₹3.3 crore** (up ₹0.3 crore; an RI-judged manager accepts it, which is also what the firm wants).

EVA: EBIT ₹120 crore, tax 25.17%, invested capital ₹700 crore, WACC 11%. NOPAT = 120 × (1 − 0.2517) = **₹89.8 crore**; capital charge = ₹77 crore; **EVA = ₹12.8 crore**; ROIC 12.83% vs WACC 11% (spread 1.83 points).

### In the news
See news box. Public capex of ₹12.2 lakh crore is justified on returns above the cost of public funds; the same RI logic prefers projects clearing a hurdle over those that maximise percentage return.

### Interview angle
> [!question] How it is asked
> "Why might ROI-based incentives cause a good manager to turn down a good project?"

> [!tip] Strong answer includes
> - The average-vs-marginal return problem
> - RI/EVA with an explicit capital charge fix it
> - Weaknesses: accounting distortions, short-termism, needs a defensible WACC
> - Tie to capital allocation across divisions

---
## 12. The Balanced Scorecard and Strategy Maps
> 🟠 Tier 2 · _Key points:_ four perspectives; cause-and-effect strategy map; lead vs lag measures; targets and initiatives

### Definition
The **Balanced Scorecard** (Kaplan and Norton, 1992) translates strategy into measures across four perspectives:

| Perspective | Question | Example measures |
|---|---|---|
| Financial | How do we look to shareholders? | EVA, ROCE, revenue growth, cost-to-serve |
| Customer | How do customers see us? | OTIF, perfect order rate, NPS, share of wallet |
| Internal process | What must we excel at? | Cycle time, OEE, defect PPM, order-to-cash days |
| Learning and growth | Can we sustain improvement? | Training hours, skills coverage, system uptime |

Each objective has a **measure, target and initiative**. A **strategy map** links objectives in a cause-and-effect chain: *skilled people → better processes → reliable service → loyal customers → revenue and margin*. A good scorecard mixes **lag** (outcome) and **lead** (driver) measures, has 15-25 measures at most, and is owned at each level. Supply chain KPIs sit mainly in customer and process perspectives ([[012 Supply Chain Analytics & KPIs]], [[047 MIS & Dashboard Design]]).

### Example
Strategy map for a 3PL (third-party logistics) provider:
1. **Learning and growth:** WMS-trained supervisors (85% certified) → lower pick errors.
2. **Process:** pick accuracy 99.8%, dock-to-stock 4 hours → higher on-time dispatch.
3. **Customer:** OTIF 97%, damage claims below 0.2% → retention of key accounts.
4. **Financial:** revenue per sq ft up 8%; EVA positive.
An **initiative** (WMS rollout) is attached to each process objective; a **target** (OTIF from 94% to 97% by March) with a named owner makes it actionable. A useful test: if an objective in the map has no lead measure explaining how it will be achieved, it is a wish.

### In the news
See news box. Kraft Heinz tracked margin (financial perspective) tightly while customer and brand measures lagged; a four-perspective scorecard would have surfaced the imbalance. Indian large-company BSC use is documented in academic case studies, for instance the Tata Steel case in *Accounting Education* (2009) ([Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/09639280802436731)); the abstract page was reviewed, not the full text.

### Interview angle
> [!question] How it is asked
> "Design a scorecard for a quick-commerce dark store network."

> [!tip] Strong answer includes
> - Four perspectives with 2-3 measures each, lead and lag mixed
> - A strategy map showing causal links, e.g., picking accuracy → delivery time → repeat orders
> - Targets, owners and initiatives; fewer measures, not more
> - Warn against vanity metrics and measure conflicts (speed vs cost)

---
## 13. KPI Cascading, OKRs and Linking Pay to the Scorecard
> 🟠 Tier 2 · _Key points:_ cascade from corporate to individual; KPI tree; line of sight; OKRs vs KPIs vs MBO; Hoshin link

### Definition
**KPI cascading** decomposes a top-level objective into measures each lower level can influence, so every manager has a line of sight to the corporate goal. Methods:
- **KPI tree:** ROCE = margin × asset turnover; margin splits into price, material, labour; asset turnover splits into inventory days, receivable days.
- **Strategy deployment (Hoshin Kanri):** catchball negotiation between levels ([[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]]).
- **OKRs:** ambitious objectives with measurable key results, reset quarterly, scored 0-1 and often kept separate from pay; **KPIs** track steady-state health; **MBO** ties targets to appraisal and bonus.

Rules: cascade **outcomes down, not formulas down**; keep a few measures per role; no measure should be controllable by nobody; avoid measures that conflict between functions (procurement cost vs production availability); link bonuses to a balanced set (not just one number) and to team as well as individual results.

### Example
Corporate goal: raise operating margin from 9% to 11% on ₹2,000 crore revenue, i.e., ₹40 crore more profit. Cascade: supply chain owns ₹16 crore (freight −₹6 crore through load optimisation; inventory carrying cost −₹4 crore, from cutting inventory by ₹22 crore at an 18% annual carrying cost = ₹3.96 crore; procurement savings ₹6 crore). A DC manager's KPIs: cost per order (tied to freight and labour), inventory accuracy 99.5%, OTIF 98%. Check: the three supply chain lines add to 6 + 4 + 6 = ₹16 crore, 40% of the margin goal.

### In the news
See news box. The Union Budget cascades national targets (fiscal deficit 4.3% of GDP) into ministry-level allocations and monitored outcomes.

### Interview angle
> [!question] How it is asked
> "How would you cascade a 2-point margin improvement target across functions?"

> [!tip] Strong answer includes
> - Decompose the margin by driver (price, mix, material, conversion, logistics, overhead)
> - Assign owners and lead KPIs per driver with realistic sizing
> - Resolve conflicts between KPIs through joint targets
> - Mention review cadence and pay linkage with balanced measures

---
## 14. Budgeting Pitfalls, Behavioural Effects and Beyond Budgeting
> 🟠 Tier 2 · _Key points:_ slack, sandbagging, use-it-or-lose-it, ratchet effect, gaming; remedies; rolling forecasts and relative targets

### Definition
Common pitfalls:
- **Budgetary slack/sandbagging:** padding costs or understating sales to make targets easy.
- **Use-it-or-lose-it:** unspent budget is cut next year, so year-end spending spikes.
- **Ratchet effect:** this year's outperformance becomes next year's floor, discouraging stretch.
- **Annual calendar rigidity:** the plan is stale by month three in a volatile market.
- **Incremental bias, politics and time cost:** budgeting can absorb a large share of finance effort for little decision value.
- **Short-termism:** cutting R&D, training, maintenance or marketing to reach a number.
- **Control vs planning conflict:** the same number is used for forecasting and for judging people, which discourages honest forecasts.
Remedies: separate **forecast** from **target**; use **rolling forecasts** and **driver-based** models; set **relative targets** (vs peers, vs prior year) as the **beyond-budgeting** model proposes; use **flexible budgets**; protect strategic investment lines; add non-financial measures; reward accuracy of forecasts, not only attainment. Link: [[188 Financial Modelling in Excel]] for building driver-based models and [[190 SAP FI-CO Essentials for Operations Professionals]] for how budgets and actuals are held in an ERP.

### Example
A DC manager's annual transport budget is ₹5 crore, and unspent money is clawed back. In Q4 he books ₹60 lakh of trailers for the next year's contracts and prepays a vendor, creating no value. A rolling-forecast alternative sets a transport cost per tonne-km target adjusting to volume, reviewed quarterly, and rewards the **cost per tonne-km improvement** instead of "spend by year end". Savings are shared with the team instead of being removed.

### In the news
See news box. Kraft Heinz shows short-termism at scale, and a vendor guide cites ZBB use at only 15-20% of companies, signalling that even firms trying to fix budget bloat rarely adopt the full method.

### Interview angle
> [!question] How it is asked
> "Why do budgets often fail, and what would you change?"

> [!tip] Strong answer includes
> - Behavioural failures (slack, ratchet, year-end spend) with a specific example
> - Fixes: rolling forecasts, flexible budgets, relative targets, decoupling forecast from bonus
> - Preserve discipline: ZBB for overhead, capex gating for investment
> - Acknowledge that budgets remain useful for coordination and authorisation
