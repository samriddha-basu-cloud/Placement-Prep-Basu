---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems

⬅ [[114 Bullwhip Effect, Beer Game & Information Sharing]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[116 Inventory Valuation, Cycle Counting & Inventory Governance]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. EPQ / EMQ: Finite Production Rate]]
2. [[#2. Planned Backorders Model]]
3. [[#3. All-Units Quantity Discounts]]
4. [[#4. Incremental (Marginal) Quantity Discounts]]
5. [[#5. Continuous Review: (s, Q) and (s, S) Policies]]
6. [[#6. Periodic Review: (R, S), (R, s, S) and Base Stock]]
7. [[#7. Service Levels: Type 1 vs Type 2, Loss Function and Table]]
8. [[#8. Fixing (s, Q) for a Fill-Rate Target]]
9. [[#9. Safety Stock under Lead-Time Variability and Review Period]]
10. [[#10. Joint Replenishment and Coordinated Ordering]]
11. [[#11. Multi-Item Budget Constraint (Lagrange Multiplier)]]
12. [[#12. Slow-Moving and Intermittent Items]]
13. [[#13. ⭐ Advanced: Base Stock as Newsvendor, Optimising Q and s Together]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): lead-time swings and excess stock put policy parameters back under the microscope
> **Lead-time volatility is now the top planning pressure for small firms (reported 1 October 2026).** In a Netstock survey of 150+ small-business customers, **supplier lead-time swings (29%)** were the single most-cited inventory-planning pressure, followed by raw-material costs (23%), freight costs (23%) and demand shifts (21%); across all factors, 77% cited lead-time challenges. Average supplier lead times ran from **21 days** (fastest-moving businesses) to **79 days** (slowest). Only 53% held service levels above 90%. Lead-time variance enters safety stock directly: see sub-topic 9. ([Supply Chain Dive](https://www.supplychaindive.com/news/beyond-tariffs-a-storm-of-pressures-is-hampering-smb-supply-chains/831880/))
>
> **Excess and dead stock keep climbing.** The same survey reports dead stock as a share of excess inventory rising from **12% in 2024 to 17% in 2025 to 24% in 2026**; 93% of respondents had an active excess-inventory reduction strategy, but only 7% met all four of Netstock's scorecard measures. Order quantities and reorder points set too high for slow-moving items are one way this builds up. ([Supply Chain Dive](https://www.supplychaindive.com/news/beyond-tariffs-a-storm-of-pressures-is-hampering-smb-supply-chains/831880/); the link to policy settings is this note's interpretation)
>
> **Inventory is scored in Gartner's Top 25 (17 June 2026).** Inventory as a percentage of revenue carries a **10%** weight in Gartner's methodology (peer opinion 25%, Gartner expert opinion 25%, ESG 20%, change in return on productive assets 10%, revenue growth 5%, gross-margin change 5%); Schneider Electric ranked first with a score of 7.05. ([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-06-17-gartner-announces-2026-rankings-of-the-global-supply-chain-top-25))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. EPQ / EMQ: Finite Production Rate
> 🔴 Tier 1 · _Key points:_ replenishment spread over production time; $Q^*=\sqrt{2DS/(H(1-d/p))}$

### Definition
The **Economic Production Quantity (EPQ)**, also called **EMQ** (economic manufacturing quantity), modifies the EOQ ([[003 Inventory Management]]) for items made in-house at a production rate $P$ greater than the demand rate $D$ (same time unit). Stock builds at $P-D$ during the run and falls at $D$ afterwards, so the peak inventory is less than the lot size:

$$I_{max}=Q\left(1-\frac{D}{P}\right),\qquad TC(Q)=\frac{D}{Q}S+\frac{I_{max}}{2}H,\qquad Q^*=\sqrt{\frac{2DS}{H\,(1-D/P)}},\qquad TC^*=\sqrt{2DSH(1-D/P)}$$

$S$ = setup cost per run, $H$ = holding cost per unit per year. As $P\to\infty$ the EPQ tends to EOQ. EPQ is **larger** than EOQ because holding cost per unit is lower. Run length $=Q/P$; cycle $=Q/D$. Reduce $S$ (SMED, see [[007 Lean Manufacturing]]) to shrink batches.

### Example
Annual demand $D=24{,}000$, production capacity $P=96{,}000$ a year, setup ₹3,000, $H=₹30$. $D/P=0.25$. EOQ $=\sqrt{2\times24000\times3000/30}=2{,}191$. **EPQ** $=\sqrt{2\times24000\times3000/(30\times0.75)}=$ **2,530**. Peak stock $=2{,}530\times0.75=1{,}897$; average 949. $TC^*=\sqrt{2\times24000\times3000\times30\times0.75}=$ **₹56,921** a year. Using the EOQ of 2,191 in the same model costs ₹57,511 (+1.0%), so the cost curve is flat. Production run $=2{,}530/96{,}000\times365\approx$ **9.6 days** every **38.5 days**; about 9.5 runs a year.

### In the news
See news box. In the Netstock survey, lead times of up to 79 days make long production runs of slow-moving items risky; setup-cost reduction is the lever that shrinks $Q^*$.

### Interview angle
> [!question] How it is asked
> "How is EPQ different from EOQ, and what happens as production speed rises?"

> [!tip] Strong answer includes
> - Formula with the $(1-D/P)$ factor and its meaning (stock builds during the run)
> - EPQ > EOQ; as $P\to\infty$ the two coincide
> - Worked numbers and a flat cost curve comment
> - Practical constraints: shared capacity across SKUs, changeover time, shelf life

---

## 2. Planned Backorders Model
> 🔴 Tier 1 · _Key points:_ allow shortages with cost $B$; $Q^*=\sqrt{\tfrac{2DS}{H}\tfrac{H+B}{B}}$; max backorder

### Definition
If customers wait and the shortage cost is a per-unit-per-year backorder cost $B$, planned backorders can be cheaper than holding stock. Let $b$ be the maximum backorder and $Q-b$ the maximum stock:

$$TC=\frac{D}{Q}S+\frac{(Q-b)^2}{2Q}H+\frac{b^2}{2Q}B,\qquad Q^*=\sqrt{\frac{2DS}{H}\cdot\frac{H+B}{B}},\quad b^*=Q^*\frac{H}{H+B},\quad TC^*=\sqrt{2DSH\,\frac{B}{H+B}}$$

As $B\to\infty$ it becomes the EOQ. Use only when backorders are tolerated and the cost (lost goodwill, expediting, penalties) is known: unreliable for customers who would buy elsewhere (lost sales) and for critical items.

### Example
$D=12{,}000$, $S=₹500$, $H=₹20$ per unit-year, $B=₹60$. EOQ $=775$ and $TC=₹15{,}492$. With backorders: $Q^*=\sqrt{2\times12000\times500/20\times80/60}=$ **894**; maximum backorder $b^*=894\times20/80=$ **224**; maximum stock $=670.8\approx671$; $TC^*=\sqrt{2\times12000\times500\times20\times60/80}=$ **₹13,416**, i.e. **13.4% lower** than the EOQ policy. In each cycle the firm is in backorder for $b^*/Q^*=H/(H+B)=25\%$ of the time. That is acceptable only if customers truly wait.

### In the news
See news box. Where lead times are volatile, deliberately planned backorders are rarely tolerated by customers; unplanned backorders are better treated by service-level safety stock (sub-topics 7-9).

### Interview angle
> [!question] How it is asked
> "Is it ever optimal to run out of stock on purpose?"

> [!tip] Strong answer includes
> - Backorders vs lost sales and the shortage cost $B$
> - The $\sqrt{(H+B)/B}$ factor and the fraction of the cycle in backorder $H/(H+B)$
> - A worked comparison with EOQ
> - Judgement: B2B contract with penalties vs retail where customers walk away

---

## 3. All-Units Quantity Discounts
> 🔴 Tier 1 · _Key points:_ price applies to the whole order; check each tier's feasible EOQ; compare total costs

### Definition
In an **all-units discount** the lower price applies to **every unit** in the order once the order reaches a break quantity. Procedure (price breaks $q_1<q_2<\dots$ with unit prices $c_1>c_2>\dots$, $h_k=i\cdot c_k$):
1. For each tier $k$ compute $EOQ_k=\sqrt{2DS/h_k}$.
2. If $EOQ_k$ is below the tier's break quantity, use the break quantity $q_k$ (the lowest feasible quantity at that price); if above the tier's upper limit the tier is infeasible.
3. Compute total annual cost $TC_k=Dc_k+\frac{D}{Q_k}S+\frac{Q_k}{2}ic_k$.
4. Choose the lowest $TC_k$.

Holding cost depends on the price: $H=ic$. Beyond the pure cost view, consider storage and cash constraints, shelf life, supplier lock-in and whether the discount induces forward buying (bullwhip: [[114 Bullwhip Effect, Beer Game & Information Sharing]]).

### Example
$D=10{,}000$, $S=₹400$, $i=20\%$. Price ₹50 for $Q<1{,}000$; ₹48 for $1{,}000\le Q<2{,}500$; ₹46.50 for $Q\ge2{,}500$.
- Tier 1 (₹50): $EOQ=\sqrt{2\times10000\times400/10}=894$ (feasible): $TC=500{,}000+4{,}472+4{,}472=$ **₹508,944**.
- Tier 2 (₹48): $EOQ=913<1{,}000$, so $Q=1{,}000$: $480{,}000+4{,}000+4{,}800=$ **₹488,800**.
- Tier 3 (₹46.50): EOQ 927 $<2{,}500$, so $Q=2{,}500$: $465{,}000+1{,}600+11{,}625=$ **₹478,225**.
Best: **order 2,500**, saving ₹30,719 (6.0%) versus the plain EOQ of 894, mostly from the lower unit price. Check capacity: average stock is 1,250 units (₹58k of stock at ₹46.50).

### In the news
See news box. Discounts raise cycle stock and, in a slow-moving or volatile segment, dead stock: the survey's rise in dead stock reminds that a cheaper unit is not cheaper if it does not sell.

### Interview angle
> [!question] How it is asked
> "A supplier offers 4% off for an order of 2,500 instead of 900. Should we accept?"

> [!tip] Strong answer includes
> - The procedure (EOQ per tier, feasibility, total cost including purchase cost)
> - Explicit total-cost comparison, not "cheaper price wins"
> - Non-cost factors: shelf life, cash, space, obsolescence risk, supplier dependence
> - Negotiation angle: ask for staggered deliveries at the discounted price (scheduled call-offs)

---

## 4. Incremental (Marginal) Quantity Discounts
> 🔴 Tier 1 · _Key points:_ each price applies only to units in its band; effective average price; closed-form per band

### Definition
With **incremental discounts**, the lower price applies only to **units above** each break. The cost of an order $Q$ in band $k$ is $K_k+c_kQ$, where $K_k$ is the **fixed intercept** (the amount by which the total is above $c_kQ$). Average unit cost is $K_k/Q+c_k$. The annual cost is

$$TC(Q)=D\left(\frac{K_k}{Q}+c_k\right)+\frac{D}{Q}S+\frac{Q}{2}\,i\left(\frac{K_k}{Q}+c_k\right),\qquad Q_k^*=\sqrt{\frac{2D(S+K_k)}{i\,c_k}}$$

Compute $Q_k^*$ for each band; keep it if it lies inside the band; otherwise use the nearest band boundary; compare the candidates' total cost.

### Example
Same $D=10{,}000$, $S=400$, $i=20\%$. Price ₹50 for units 1-1,000; ₹48 for 1,001-2,500; ₹46.50 for units above 2,500. Intercepts: band 1 $K=0$; band 2: an order of $Q$ costs $1000\times50+(Q-1000)\times48=48Q+2{,}000$, so $K=2{,}000$; band 3: $1000\times50+1500\times48+(Q-2500)\times46.5=46.5Q+5{,}750$, so $K=5{,}750$.
- Band 1: $Q^*=\sqrt{2\times10000\times400/(0.2\times50)}=894$; $TC=$ **₹508,944**.
- Band 2: $Q^*=\sqrt{2\times10000\times(400+2000)/(0.2\times48)}=2{,}236$ (in band): average cost $=48.894$; $TC=$ **₹501,666**.
- Band 3: $Q^*=\sqrt{2\times10000\times(400+5750)/(0.2\times46.5)}=3{,}637$ (in band): average cost $=48.081$; $TC=$ **₹499,397**.
Best: **order about 3,637**, with an average price of ₹48.08, saving ₹9.5k (1.9%) versus ₹50. Incremental schemes give **smaller savings** than all-units schemes for the same price list, so buyers rarely over-order as much.

### In the news
See news box. Tiered freight and 3PL rate cards (more discounted per pallet above thresholds) are incremental discounts; the same logic applies to logistics contracts.

### Interview angle
> [!question] How it is asked
> "What is the difference between all-units and incremental discounts, and how does it change order quantity?"

> [!tip] Strong answer includes
> - Definitions: whole-order price vs band price
> - Procedure and the intercept $K$
> - Result: all-units produce sharper incentives (and bigger forward buys)
> - Supplier view: all-units discounts coordinate the chain but encourage batching

---

## 5. Continuous Review: (s, Q) and (s, S) Policies
> 🔴 Tier 1 · _Key points:_ inventory position, reorder point, fixed order quantity vs order-up-to level

### Definition
In **continuous review** the stock is monitored after every transaction. The trigger uses the **inventory position** $IP=\text{on hand}+\text{on order}-\text{backorders}$:
- **(s, Q)** (also "(Q, R)" or "(R, Q)" in some texts): when $IP\le s$, order a **fixed quantity $Q$**.
- **(s, S)**: when $IP\le s$, order **up to $S$**, i.e. order $S-IP$. With unit-sized demands, $IP$ hits $s$ exactly and $S=s+Q$, so the two policies are identical; with **lumpy demand** (an order can jump $IP$ well below $s$) (s, S) restores the position to $S$ while (s, Q) may leave it too low.
- **(S-1, S)** (one-for-one or base stock): order whenever one unit is consumed; used for expensive, slow-moving or critical items.

Reorder point $s=\mu_L+SS$ where $\mu_L=d\bar L$. $Q$ is set by EOQ or EPQ; $SS$ by the service criterion (sub-topics 7-9). A simple procedure: set $Q$ from EOQ, then $s$ from the service target; refine by iterating (Hadley-Whitin) when service is cost-based.

### Example
Daily demand 40 (s.d. 12), lead time 9 days, $Q=300$, reorder point $s=396$ (sub-topic 8), so for (s, S) the level is $S=s+Q=696$. Stock on hand 250 and 150 on order: $IP=400>396$, no order. After a sale of 10, $IP=390\le396$: **(s, Q)** orders 300 (position 690); **(s, S)** orders $696-390=306$ (position 696): almost the same, because demand arrives in small units. Now a customer takes 80 units at once when $IP=400$: $IP=320$. **(s, Q)** orders 300 and the position is 620, still well below 696; **(s, S)** orders $696-320=376$ and restores 696. If a single order of 450 arrived, $IP=-50$: (s, Q) orders 300 and is still below $s$, so it must order again; (s, S) orders 746 in one step. Lumpy B2B demand is the case for (s, S).

### In the news
See news box. System parameters ($s$ and $Q$) must be refreshed when lead times move; static ERP reorder points are a major source of both stock-outs and excess.

### Interview angle
> [!question] How it is asked
> "Explain (s, Q) versus (s, S) versus base stock, and when you would use each."

> [!tip] Strong answer includes
> - Inventory position (not on hand) as the trigger
> - Fixed quantity vs order-up-to, and why (s, S) handles lumpy demand
> - Base stock for slow, expensive, critical items; $(s,Q)$ for fast items with fixed order cost
> - SAP view: reorder point planning vs forecast-based planning, see [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]]

---

## 6. Periodic Review: (R, S), (R, s, S) and Base Stock
> 🔴 Tier 1 · _Key points:_ protection interval $R+L$; order-up-to level; safety stock penalty vs continuous review

### Definition
In **periodic review** the stock is checked every $R$ periods.
- **(R, S)**: at each review, order $S-IP$ (order-up-to). Protection interval is $R+L$:
$$S=\mu_{R+L}+z\,\sigma_{R+L},\quad \mu_{R+L}=d(R+L),\ \ \sigma_{R+L}=\sigma_d\sqrt{R+L}$$
- **(R, s, S)**: at each review, order up to $S$ only if $IP\le s$; avoids small orders when ordering cost is high. Under fixed cost it is the (near-)optimal policy for periodic review (Scarf's result for $(s,S)$ in the periodic setting).
- **Base stock (R = 1 period, order each period)**: the order each period equals the last period's demand.

Periodic review needs **more safety stock** than continuous review at equal service because the protection interval is $R+L$, not $L$. Its advantages: coordination of orders (many items from one supplier on a fixed day), fewer transactions, predictable workload, and routes and milk runs. Cost-optimal base stock with backorders: $P(D_{R+L}\le S)=\dfrac{b}{b+h}$ (a newsvendor rule, see sub-topic 13).

### Example
Daily demand 40, s.d. 12, $L=9$, **continuous review** SS at 95% Type 1: $1.645\times12\sqrt9=59$. **Weekly review** ($R=7$): $\sigma_{16}=12\sqrt{16}=48$; $SS=1.645\times48=$ **79** (+33%, the ratio $\sqrt{16/9}$); $S=40\times16+79=$ **719**. If at review the position is 520, order $719-520=199$. With **daily** review ($R=1$), $\sigma_{10}=12\sqrt{10}=37.9$ and $SS=1.645\times37.9=$ **62**, only 3 above continuous review: moving from weekly to daily review releases 17 units of safety stock (79 to 62) at the cost of six extra reviews a week.

### In the news
See news box. Longer and more variable lead times raise $L$ and $\sigma_L$: a periodic system's protection interval is $R+L$ so it is hit twice.

### Interview angle
> [!question] How it is asked
> "We review every Monday. How do we set order-up-to levels, and why do we need more safety stock than with continuous review?"

> [!tip] Strong answer includes
> - Protection interval $R+L$ and the formula for $S$
> - Quantify the penalty $\sqrt{(R+L)/L}$
> - Cases where periodic is better (supplier day, joint ordering, low-tech)
> - $(R,s,S)$ for items with high order cost

---

## 7. Service Levels: Type 1 vs Type 2, Loss Function and Table
> 🔴 Tier 1 · _Key points:_ cycle service (stock-out probability) vs fill rate (units); $L(z)$; unit normal loss table

### Definition
- **Type 1 (cycle service level, CSL)**: probability of no stock-out in a replenishment cycle: $P(D_L\le s)=\Phi(z)$; $SS=z\sigma_L$.
- **Type 2 (fill rate, $\beta$)**: share of demand filled from stock. Expected shortage per cycle $E[\text{shortage}]=\sigma_L\,G(z)$ where $G(z)=L(z)$ is the **unit normal loss function**:

$$G(z)=\varphi(z)-z\,[1-\Phi(z)],\qquad \beta = 1-\frac{\sigma_L\,G(z)}{Q}\ \ \Rightarrow\ \ G(z)=\frac{Q(1-\beta)}{\sigma_L}$$

Excel: `=NORM.S.DIST(z,FALSE)-z*(1-NORM.S.DIST(z,TRUE))`, solve for $z$ with Goal Seek or look up the table.

| $z$ | $\Phi(z)$ | $G(z)$ | $z$ | $\Phi(z)$ | $G(z)$ |
|---|---|---|---|---|---|
| 0.00 | 0.5000 | 0.3989 | 1.50 | 0.9332 | 0.0293 |
| 0.25 | 0.5987 | 0.2863 | 1.75 | 0.9599 | 0.0162 |
| 0.50 | 0.6915 | 0.1978 | 2.00 | 0.9772 | 0.0085 |
| 0.75 | 0.7734 | 0.1312 | 2.25 | 0.9878 | 0.0042 |
| 1.00 | 0.8413 | 0.0833 | 2.50 | 0.9938 | 0.0020 |
| 1.25 | 0.8944 | 0.0506 | 3.00 | 0.9987 | 0.0004 |

Key insight: fill rate depends on **$Q$** (a large $Q$ means few exposure cycles per year), cycle service does not. Related KPIs in [[012 Supply Chain Analytics & KPIs]].

### Example
Daily demand 40, s.d. 12, $L=9$: $\mu_L=360$, $\sigma_L=36$, $Q=300$. A **95% CSL** needs $z=1.645$, $SS=59$. The implied fill rate is $1-36\times G(1.645)/300=1-36\times0.0206/300=$ **99.75%**. If management asks for "95% service" meaning **fill rate** instead, $G=300\times0.05/36=0.417$, which corresponds to $z\approx-0.04$ (essentially **zero** safety stock): the difference between about 59 units and none is caused by the **definition** alone. Always ask which service level is meant.

### In the news
See news box. In the Netstock scorecard, "service levels above 90%" is a headline measure and only 53% met it: definitions (fill rate vs cycle service) matter for what that number means.

### Interview angle
> [!question] How it is asked
> "What is the difference between a 95% service level and a 95% fill rate? Which needs more safety stock?"

> [!tip] Strong answer includes
> - Define CSL (probability of no stock-out) and fill rate (fraction of demand)
> - Loss function formula and its use: $G(z)=Q(1-\beta)/\sigma_L$
> - Fill rate target usually needs *less* safety stock than the same-number CSL when $Q$ is large
> - Ask the client which they mean, and which the contract penalises

---

## 8. Fixing (s, Q) for a Fill-Rate Target
> 🔴 Tier 1 · _Key points:_ solve $G(z)=Q(1-\beta)/\sigma_L$; $s=\mu_L+z\sigma_L$; effect of $Q$

### Definition
Procedure for an **(s, Q) system with a Type 2 target $\beta$** under normal lead-time demand:
1. $\mu_L=d\bar L$, $\sigma_L=\sigma_d\sqrt{\bar L}$ (add lead-time variance if needed, sub-topic 9).
2. Choose $Q$ (EOQ, adjusted for pack size or MOQ).
3. Compute $G^*=Q(1-\beta)/\sigma_L$; read $z$ from the loss table (or solve).
4. $s=\mu_L+z\sigma_L$, $SS=z\sigma_L$.
5. Check cost: if a shortage cost $\pi$ per unit short is known, the cost-optimal reorder point satisfies $P(D_L>s)=\dfrac{hQ}{\pi D}$ (classical $(Q,r)$ condition with backorders).

Increasing $Q$ lets you cut safety stock for the same fill rate: a higher $Q$ means fewer stock-out exposures a year.

### Example
$\mu_L=360$, $\sigma_L=36$, $D=14{,}600$ a year, $S=₹500$, $H=₹20$ per unit-year. **Target $\beta=99\%$, $Q=300$:** $G=300\times0.01/36=0.0833\Rightarrow z=1.00$, so $SS=36$ and **$s=396$** (cycle service only 84%). **Target 99.5%:** $G=0.0417$, $z=1.34$, $SS=48$, $s=408$. Raise $Q$ to the EOQ of 854 (for $\beta=99.5\%$): $G=0.1186\Rightarrow z=0.81$, $SS=29$. Relevant annual cost (ordering plus holding of cycle and safety stock): at $Q=300$, $SS=48$: $24{,}333+(150+48)\times20=$ **₹28,300**; at $Q=854$, $SS=29$: $8{,}544+(427+29)\times20=$ **₹17,669**, a 38% reduction. Fewer cycles a year means fewer stock-out exposures, so a larger lot also needs less safety stock for the same fill rate: set $Q$ and $s$ together.

### In the news
See news box. Gartner's 10% weight on inventory-to-revenue rewards the discipline of fixing both $Q$ and $s$ instead of dumping stock to hit service.

### Interview angle
> [!question] How it is asked
> "Set the reorder point and safety stock for a 98% fill rate on this SKU."

> [!tip] Strong answer includes
> - Compute $\mu_L$ and $\sigma_L$; identify the order quantity
> - Use the loss function: $G(z)=Q(1-\beta)/\sigma_L$, find $z$
> - State the resulting $s$ and cycle service for sanity
> - Note that $Q$ and $s$ interact and should be set together

---

## 9. Safety Stock under Lead-Time Variability and Review Period
> 🔴 Tier 1 · _Key points:_ $\sigma_{DLT}^2=\bar L\sigma_d^2+\bar d^2\sigma_L^2$; reduce lead-time variance; add review period

### Definition
With random demand per period (mean $d$, s.d. $\sigma_d$) and a random lead time (mean $\bar L$, s.d. $\sigma_L$ in the same units, independent of demand):

$$\sigma_{DLT}=\sqrt{\bar L\,\sigma_d^2+d^2\,\sigma_L^2},\qquad SS=z\,\sigma_{DLT}$$

For a periodic review replace $\bar L$ by $R+\bar L$. The second term (lead-time variance) is multiplied by the **square of demand**, so for high-volume items it dominates. Remedies: improve supplier reliability, agree delivery windows, use closer or dual suppliers, expedite via a dedicated carrier, hold vendor-managed stock, or manage by **demand-during-lead-time distribution** from history (empirical quantile). Also check demand and lead time are independent; storm or festival weeks can correlate them.

### Example
$d=40$, $\sigma_d=12$, $\bar L=9$ days, 95% CSL ($z=1.65$).
- $\sigma_L=0$: $SS=1.65\times12\times3=$ **59**.
- $\sigma_L=1$ day: $\sqrt{9\times144+1600\times1}=\sqrt{2896}=53.8$; $SS=$ **89** (+50%).
- $\sigma_L=2$ days: $\sqrt{1296+6400}=87.7$; $SS=$ **145** (2.4x).
- $\sigma_L=3$ days: $SS=$ **207** (3.5x).
If lead-time s.d. is cut from 2 to 1 day through a supplier delivery-window agreement, safety stock falls by 56 units; at ₹500 a unit and 22% carrying cost that is ₹6,200 a year per SKU: multiplied across 500 SKUs, ₹31 lakh.

### In the news
See news box. The Netstock survey's lead-time dispersion (21 to 79 days on average, and "swings" the top pressure at 29%) is exactly the $\sigma_L$ term.

### Interview angle
> [!question] How it is asked
> "Lead time is 9 days on average but ranges 5 to 15. How do you set safety stock?"

> [!tip] Strong answer includes
> - The combined variance formula and why lead-time variance can dominate
> - Numerical sensitivity (halving $\sigma_L$)
> - Use history to estimate $\sigma_L$, not supplier promises; segment suppliers by reliability
> - Levers: supplier performance management ([[002 Procurement & Strategic Sourcing]]) over stock

---

## 10. Joint Replenishment and Coordinated Ordering
> 🔴 Tier 1 · _Key points:_ major (shared) order cost $S$, minor item costs $s_i$, cycle $T$ and multiples $k_i$

### Definition
When several items share a supplier, truck or production line, each order incurs a **major (joint) setup cost $S$** plus **minor costs $s_i$** per item included. Ordering each item independently pays $S$ every time. **Joint replenishment (JRP)** orders on a base cycle $T$ and includes item $i$ every $k_i$ cycles ($k_i$ integers $\ge1$):

$$TC(T,\mathbf k)=\frac{S+\sum_i s_i/k_i}{T}+\frac{T}{2}\sum_i k_i D_i h_i,\qquad T^*=\sqrt{\frac{2\,(S+\sum_i s_i/k_i)}{\sum_i k_iD_ih_i}}$$

Practical solution (Silver's iterative method or enumeration): start with all $k_i=1$, compute $T$, update $k_i=\mathrm{round}\sqrt{2s_i/(T^2D_ih_i)}$, repeat to convergence. Applications: purchasing from one vendor, container/truck loading, one production line with a common setup, joint orders in procurement ([[002 Procurement & Strategic Sourcing]], [[125 Transportation Management Deep Dive]]).

### Example
Three items: $D=(12000, 8000, 1000)$, $h=(20,15,25)$, $s=(100,150,300)$, major $S=₹800$.
- **Independent EOQs** (each pays $S+s_i$): lots 1,039, 1,007, 297: total cost **₹43,300** a year.
- **Joint**: enumeration gives $k=(1,1,2)$, $T=0.0765$ years = **27.9 days**, order quantities 918, 612 and 153 (the third item every second cycle), total **₹31,369**: **27.6% cheaper**. With all items every cycle ($k=1$): $T=30.6$ days, ₹32,241.
The saving comes from sharing the major cost; item 3 (high $s_i$ relative to its holding-cost rate) drops out of alternate cycles.

### In the news
See news box. Fewer, fuller shipments are a cost lever; but with volatile lead times (news box) the joint cycle needs safety stock for the review period $T+L$, see sub-topic 6.

### Interview angle
> [!question] How it is asked
> "We buy 40 SKUs from one supplier and order each separately. How would you reduce ordering cost?"

> [!tip] Strong answer includes
> - Major vs minor ordering costs and the base-cycle idea
> - Formula sketch and iteration (or "group by supplier and fixed review day")
> - Numerical saving versus independent EOQs
> - Practical constraints: truck capacity, supplier minimums, shelf life, safety stock for $T+L$

---

## 11. Multi-Item Budget Constraint (Lagrange Multiplier)
> 🔴 Tier 1 · _Key points:_ common multiplier $\lambda$ shrinks all lots; shadow price of capital; Solver check

### Definition
With a budget (or space) limit on the combined order values, the EOQs may violate the constraint. Minimise total cost subject to $\sum_i c_iQ_i\le B$. Lagrangian: $\sum_i\left(\frac{D_iS_i}{Q_i}+\frac{i\,c_iQ_i}{2}\right)+\lambda\left(\sum_i c_iQ_i-B\right)$. Setting the derivative to zero:

$$Q_i(\lambda)=\sqrt{\frac{2D_iS_i}{c_i\,(i+2\lambda)}}=\frac{EOQ_i}{\sqrt{1+2\lambda/i}}$$

Find $\lambda\ge0$ (by bisection or Goal Seek) so that $\sum c_iQ_i=B$. All lots shrink by **the same factor** $\sqrt{1+2\lambda/i}$ (for the same $i$): the multiplier acts like an increase in the carrying-cost rate. $\lambda$ is the **shadow price**: the annual cost saved per extra rupee of budget. For a **space or pallet** constraint replace $c_i$ by space per unit $w_i$ in the constraint. Excel Solver ([[077 Solver, Goal Seek & What-If Analysis]]) or PuLP/SciPy reproduce the result.

### Example
Carrying rate $i=25\%$. Items: A $D=20{,}000$, $S=300$, $c=₹100$; B $D=10{,}000$, $S=200$, $c=₹400$; C $D=6{,}000$, $S=250$, $c=₹800$. Unconstrained EOQs: **693, 200, 122**; order values $c_iQ_i$: ₹69,300 + ₹80,000 + ₹98,000 = ₹247,262 (the sum with unrounded Qs). Total annual cost ₹61,815. Budget limit **₹150,000** per cycle value: solve $\lambda=0.2147$; lots **420, 121, 74** (all scaled by $1/\sqrt{1+2\times0.2147/0.25}=0.606$); order values ₹42,030 + ₹48,532 + ₹59,439 = ₹150,000. Total cost **₹69,699** (+12.8%). Marginal value of budget: raising it to ₹151,000 lowers cost by about ₹212 a year ($\approx 0.2124$ per rupee, close to $\lambda$).

### In the news
See news box. Gartner's inventory-to-revenue metric and rising capital costs make "inventory under a budget" a normal planning constraint; the shadow price tells which items to cut last.

### Interview angle
> [!question] How it is asked
> "The CFO caps inventory investment at ₹1.5 crore. How do you set order quantities across SKUs?"

> [!tip] Strong answer includes
> - Lagrange multiplier approach and the common scaling factor
> - Shadow price meaning (value of relaxing the budget by ₹1)
> - Practical heuristic: scale all EOQs by one factor and round
> - Better: focus the cut on low-value-of-service items (ABC) rather than uniform cuts

---

## 12. Slow-Moving and Intermittent Items
> 🔴 Tier 1 · _Key points:_ Poisson demand, (S-1, S) policy, Croston and SBA forecasting, normal approximation fails

### Definition
**Slow-moving** items have low volume; **intermittent** items have many zero-demand periods and irregular sizes. Normal-demand formulae break down: safety-stock normal approximations give fractional or negative stock and mis-state risk. Methods:
- **Poisson demand with base stock $(S-1,S)$:** with mean demand $\lambda L$ in the lead time, **fill rate** $=P(D_L\le S-1)$ and the **ready rate** (stock available) $=P(D_L\le S-1)$ for backorder policies. Choose the smallest $S$ that reaches the target.
- **Croston's method** forecasts the demand size $z$ and the interval $p$ between demands separately (both smoothed with $\alpha$ only when demand occurs): forecast per period $=z/p$. **SBA** (Syntetos-Boylan Approximation) multiplies by $(1-\alpha/2)$ to remove Croston's upward bias.
- **Classification:** ADI (average demand interval) and $CV^2$ of sizes (Syntetos-Boylan cut-offs about ADI 1.32, $CV^2$ 0.49) separate smooth, erratic, intermittent and lumpy demand.
- **Policy options:** hold nothing, make-to-order, central stock, or stock one unit; consider supplier lead time, cost of a stock-out and obsolescence (FSN and dead stock in [[003 Inventory Management]]).

### Example
**Poisson:** a spare part sells 12 a year; lead time 1 month, so $\lambda L=1.0$. Fill rate by $S$: $S=2$: $P(D\le1)=73.6\%$; $S=3$: $P(D\le2)=92.0\%$; **$S=4$: $P(D\le3)=98.1\%$**; $S=5$: 99.6%. Choose $S=4$ for a 98% target (3 units of "safety" for a mean demand of 1). **Croston:** demands over 20 periods: 5, 8, 4, 6 and 5 in periods 3, 7, 10, 15, 20 (zeros otherwise); true average 1.4 a period. With $\alpha=0.1$: smoothed size $\hat z=5.23$, interval $\hat p=3.45$: Croston forecast $5.23/3.45=1.51$ per period; SBA: $0.95\times1.51=1.44$. The true average is 1.4: Croston overstates slightly (1.51) and SBA corrects most of it (1.44).

### In the news
See news box. As dead stock rises (24% of excess inventory in 2026), slow movers deserve a $(S-1,S)$ or make-to-order policy rather than a "min/max" copied from fast items.

### Interview angle
> [!question] How it is asked
> "How would you manage the inventory of 5,000 spare parts that sell a few units a year?"

> [!tip] Strong answer includes
> - Segment (ADI/CV², value, criticality-VED) and choose policy per segment
> - Poisson-based base stock rather than normal safety stock
> - Croston/SBA for forecasting; reviews for obsolescence and return-to-vendor options
> - Pooling (central stock), consignments and supplier lead-time agreements

---

## 13. ⭐ Advanced: Base Stock as Newsvendor, Optimising Q and s Together
> ⭐ Advanced · _Added beyond the tracker_

### Definition
For a **base-stock policy** with backorder cost $b$ per unit short and holding cost $h$ per unit per period over the protection interval $R+L$, the optimal order-up-to level satisfies the newsvendor critical ratio

$$P(D_{R+L}\le S^*)=\frac{b}{b+h}$$

so $S^*=\mu_{R+L}+z\sigma_{R+L}$ with $z=\Phi^{-1}(b/(b+h))$. The (s, Q) system is optimised jointly by the Hadley-Whitin iteration: (1) start with $Q_0=EOQ$; (2) find $s$ from the shortage condition $P(D_L>s)=\dfrac{hQ}{\pi D}$; (3) recompute $Q=\sqrt{\dfrac{2D\,[S+\pi\,\sigma_LG(z)]}{h}}$ (the order cost is augmented by the expected shortage cost per cycle); repeat to convergence. For a given service target, an approximate shortcut is to set $Q$ by EOQ then $s$ by the loss function (sub-topic 8): usually within 1-2% of the optimum. Also: (s, S) is the optimal structure under fixed order cost (K-convexity, Scarf 1960), which is why ERP min-max systems are not arbitrary.

### Example
Weekly review, lead time 2 weeks, weekly demand 100 (s.d. 30), $R=1$, so $R+L=3$ weeks: $\mu_3=300$, $\sigma_3=30\sqrt3=52$. Holding ₹1 per unit-week; backorder cost ₹19: ratio $19/20=0.95$, $z=1.645$, $S^*=300+1.645\times52=$ **386**. If backorder cost rises to ₹49: ratio 0.98, $z=2.05$, $S^*=407$ (+21 units). The cost parameters, not an arbitrary "95% service", determine the level; if shortage cost is hard to quantify, use the implied ratio as a sanity check: a 95% target implies a backorder cost 19 times the weekly holding cost.

### In the news
See news box. Boards judge inventory by turns and service; the base-stock ratio makes the trade-off explicit in rupees.

### Interview angle
> [!question] How it is asked
> "What shortage cost is implied by a 98% service target?"

> [!tip] Strong answer includes
> - Newsvendor ratio for base stock: $b/(b+h)=$ service target
> - Implied cost: $b=h\times\text{CR}/(1-\text{CR})$ (98% gives 49x the holding cost per period)
> - Joint optimisation of $Q$ and $s$ (iteration) and its closeness to the shortcut
> - Use in SAP/IBP service-level optimisation: see [[198 SAP IBP, APO & Demand-Driven Planning]] and [[117 Demand-Driven MRP (DDMRP) & Buffer Management]]
