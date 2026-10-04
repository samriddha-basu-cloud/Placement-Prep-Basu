---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Bullwhip Effect, Beer Game & Information Sharing"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Bullwhip Effect, Beer Game & Information Sharing

⬅ [[113 Network Design & Facility Location Modelling]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. The Bullwhip (Forrester) Effect: Definition and Measurement]]
2. [[#2. The Four Causes (Lee, Padmanabhan and Whang, 1997)]]
3. [[#3. Quantifying Demand-Signal Processing: Lead Time and Smoothing]]
4. [[#4. Multi-Stage Amplification: A Step in Demand Through Four Stages]]
5. [[#5. Price Promotions, Forward Buying and Order Batching: Numbers]]
6. [[#6. Rationing, Shortage Gaming and Panic Ordering]]
7. [[#7. The Beer Distribution Game and Misperception of Feedback]]
8. [[#8. Information Sharing: POS Data, VMI and CPFR]]
9. [[#9. Countermeasures Mapped to Causes]]
10. [[#10. Cases: P&G Pampers, HP Printers, Barilla]]
11. [[#11. Post-COVID Bullwhips: Chips, Containers, Toilet Paper and the Stock Hangover]]
12. [[#12. Measuring and Dashboarding Bullwhip in Real Data]]
13. [[#13. ⭐ Advanced: When Amplification Is Rational and the Information-Sharing Value Trade-off]]

## 📰 News box
> [!news] Shared news hook for this topic (2020–2026): panic ordering, double ordering and the hangover
> **Chip shortage: scarcity, cancellations and long lead times (2021).** Wikipedia's summary of the 2020-2023 chip shortage records that carmakers first "incorrectly predicted that sales would drop, canceled chip orders", then could not meet demand; chip lead times reached **15 weeks in February 2021** (the longest since 2017) and Broadcom's reached **22.2 weeks in April 2021, up from 12.2 weeks in February 2020**. The shortage was expected to cost the auto industry about **$210 billion** in revenue in 2021 (an estimate reported there). Order cancellations followed by scramble buying is a textbook bullwhip pattern. ([Wikipedia: 2020-2023 global chip shortage](https://en.wikipedia.org/wiki/2020%E2%80%932023_global_chip_shortage))
>
> **The hangover: dead stock after the surge (reported 1 October 2026).** In a Netstock survey of 150+ small-business customers, **dead stock as a share of excess inventory rose from 12% (2024) to 17% (2025) to 24% (2026)**; 93% had an active excess-inventory reduction strategy but only 7% met all four of Netstock's health measures, and supplier lead times ranged from 21 to 79 days on average. The survey reports the trend; linking it to earlier over-buying is this note's interpretation, not the survey's claim. ([Supply Chain Dive](https://www.supplychaindive.com/news/beyond-tariffs-a-storm-of-pressures-is-hampering-smb-supply-chains/831880/))
>
> **Pandemic demand spikes and the classic evidence.** Wikipedia's bullwhip entry traces the effect to Jay Forrester (1961, *Industrial Dynamics*) and to the 1997 Lee-Padmanabhan-Whang study of four causes, repeats the often-quoted claim that a **5% change in point-of-sale demand can be read as a change of up to 40% upstream**, and cites COVID-19 panic buying (masks, ventilators, toilet paper, eggs) and post-pandemic container shortages that provoked over-ordering. In the original *Sloan Management Review* article, Procter & Gamble (Pampers) and Hewlett-Packard (printers) are the lead examples: end-customer sales were fairly smooth while orders swung much more upstream. ([Wikipedia: Bullwhip effect](https://en.wikipedia.org/wiki/Bullwhip_effect); [MIT Sloan Management Review](https://sloanreview.mit.edu/article/the-bullwhip-effect-in-supply-chains/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The Bullwhip (Forrester) Effect: Definition and Measurement
> 🔴 Tier 1 · _Key points:_ variance of orders > variance of demand; ratio and CV measures; upstream amplification

### Definition
The **bullwhip effect** (also the **Forrester effect**, after Jay Forrester's 1961 *Industrial Dynamics*) is the increase in the variability of orders as one moves upstream from retailer to wholesaler, manufacturer and supplier, even when end-customer demand is relatively stable. Standard measure:

$$BW = \frac{\text{Var}(\text{orders placed by a stage})}{\text{Var}(\text{demand it receives})} \quad (BW>1 \Rightarrow \text{amplification}),\qquad \text{or CV ratio}=\frac{CV_{orders}}{CV_{demand}}$$

Use the **coefficient of variation** ($\sigma/\mu$) when volumes differ across stages. Costs of bullwhip (Lee et al.): excess inventory, poor service, lost revenue, mis-planned capacity, expedited transport, reduced quality and production schedule disruptions. Basic summary of the topic is in [[001 SCM Introduction & Fundamentals]]; this note adds the mathematics, the game and the countermeasure design.

### Example
Retail sales of a detergent average 1,000 units a week with s.d. 100 (CV 0.10). The distributor orders the same average 1,000 a week with s.d. 180 (CV 0.18) and the factory receives orders averaging 1,000 with s.d. 330 (CV 0.33). $BW$ (variance basis): distributor $(180/100)^2 = 3.24$; factory relative to retail $(330/100)^2 = 10.9$. The factory plans capacity and raw material for demand that is 3.3x as variable as what consumers actually buy.

### In the news
See news box. The post-surge dead-stock numbers (12% to 24% of excess inventory) are the cost side of amplified orders.

### Interview angle
> [!question] How it is asked
> "What is the bullwhip effect and how would you measure it for a client?"

> [!tip] Strong answer includes
> - Definition (orders more variable than demand, growing upstream) with the Forrester origin
> - Ratio of order variance to demand variance by stage, or CV ratio
> - Measure from shipment and order data over at least 52 weeks, deseasonalised
> - Consequences in cost terms: inventory, capacity, expediting, service

---

## 2. The Four Causes (Lee, Padmanabhan and Whang, 1997)
> 🔴 Tier 1 · _Key points:_ demand signal processing, order batching, price fluctuation, rationing and shortage gaming

### Definition
Lee, Padmanabhan and Whang (Sloan Management Review, 1997) showed that bullwhip arises from **rational** local decisions, not only from poor management:

| Cause | Mechanism | Typical symptom |
|---|---|---|
| **1. Demand signal processing** | Each stage forecasts from the *orders* of the stage below and sets safety stock as a multiple of forecast error, so a small rise raises the target stock | Orders overshoot after a small demand uptick |
| **2. Order batching** | Periodic (weekly/monthly) ordering or full-truck/lot sizes concentrate demand into spikes | Month-end spikes, empty weeks |
| **3. Price fluctuations** | Promotions, trade discounts and forward buying decouple purchases from consumption | Spike at the promotion, trough after |
| **4. Rationing and shortage gaming** | When supply is short and allocated pro rata to orders, buyers inflate orders; when supply recovers, orders collapse | Phantom demand, cancellations |

Other contributors from behavioural research: **misperception of feedback** (ignoring orders already in the pipeline), long information and material delays, and incentives (sales targets, quarter-end pushes). See the four-cause summary in [[001 SCM Introduction & Fundamentals]] and the demand side in [[004 Demand Forecasting & Planning]].

### Example
A beverage distributor receives a promotion scheme (₹5 off per case for 2 weeks). Retailers buy 3 months of stock; the distributor reads the spike as demand and orders the bottler up; two weeks later there are no orders. Consumer demand never changed (price fluctuation + signal processing).

### In the news
See news box. Panic ordering in the 2021 chip shortage is cause 4; the 2021-2026 excess-stock hangover is cause 4 reversing.

### Interview angle
> [!question] How it is asked
> "Why does bullwhip arise even when every player is rational?"

> [!tip] Strong answer includes
> - The four causes with one-line mechanism and a symptom for each
> - Each cause paired with a counter (see sub-topic 9)
> - Behavioural overlay: pipeline neglect and incentives
> - A real example (P&G Pampers, HP printers, a promotion)

---

## 3. Quantifying Demand-Signal Processing: Lead Time and Smoothing
> 🔴 Tier 1 · _Key points:_ $1+2L/p+2L^2/p^2$ for moving average; $(1+L\alpha)^2+\dots$ for exponential smoothing

### Definition
Let a stage use an **order-up-to** policy with lead time $L$ (periods of cover, including the review period) and forecast the mean demand from the demand it observes. For iid demand with variance $\sigma^2$, order variance divided by demand variance is:

**Moving average of $p$ periods** (Chen, Drezner, Ryan and Simchi-Levi, 2000):
$$\frac{\text{Var}(q)}{\text{Var}(D)} = 1 + \frac{2L}{p} + \frac{2L^2}{p^2}$$

**Exponential smoothing with parameter $\alpha$** (derivation of the same logic: $q_t = D_{t-1}+L\alpha(D_{t-1}-\hat\mu_{t-1})$, with $\text{Var}(\hat\mu)=\sigma^2\alpha/(2-\alpha)$):
$$\frac{\text{Var}(q)}{\text{Var}(D)} = (1+L\alpha)^2 + (L\alpha)^2\,\frac{\alpha}{2-\alpha}$$

Both exceed 1 and rise with **lead time $L$** and with **responsiveness of the forecast** (small $p$ or large $\alpha$): a short, jumpy forecast and a long lead time multiply the swings. (This ignores the $z\hat\sigma$ safety-stock term, which adds more amplification when the safety factor depends on a forecast error estimate.) Chen et al. state the moving-average result as a lower bound, because the safety-stock term adds further amplification; the exponential-smoothing line is derived here under the same logic and checked by simulation.

### Example
Moving average, $p=5$, $L=2$: $1 + 0.8 + 0.32 =$ **2.12**; $L=4$: $1+1.6+1.28 =$ **3.88**; $p=10$, $L=4$: **2.12**. Doubling the averaging window offsets a doubled lead time. Smoothing with $\alpha = 0.2$, $L=2$: $(1.4)^2 + (0.4)^2 \times 0.111 = 1.96 + 0.0178 =$ **1.978**; $\alpha=0.5$, $L=4$: $9 + 4\times0.333 =$ **10.33**. (Checked against a 300,000-period simulation: 2.12, 3.88, 1.98 and 10.34.) Reading: with $p=5$ and $L=2$ the standard deviation of orders is $\sqrt{2.12}=1.46$ times the s.d. of demand.

### In the news
See news box. Long chip lead times (15 to 22 weeks) are a large $L$; forecasts reacting to scarce signals push the ratio up.

### Interview angle
> [!question] How it is asked
> "What drives the size of the bullwhip? How would a shorter lead time help?"

> [!tip] Strong answer includes
> - The formula (at least the moving-average one) and what $L$ and $p$ do
> - Numerical illustration: $p=5$, $L=2$ gives about 2.1x variance
> - Levers: reduce $L$, lengthen the forecast window (smoother forecasts), share demand data
> - Trade-off: a smoother forecast reacts more slowly to real shifts

---

## 4. Multi-Stage Amplification: A Step in Demand Through Four Stages
> 🔴 Tier 1 · _Key points:_ amplification compounds; overshoot then undershoot; decentralised vs centralised information

### Definition
With each stage forecasting from the orders it receives, the ratios **multiply** (decentralised information), so a four-stage chain with stage ratio 2.12 has about $2.12^4 \approx 20.2$ variance amplification at the top. If every stage sees **end-customer demand** (centralised information), the bound (Chen et al.) becomes

$$\frac{\text{Var}(q^{(k)})}{\text{Var}(D)} \ge 1+\frac{2\sum L_i}{p}+\frac{2(\sum L_i)^2}{p^2}$$

which for $k=4$ stages, each $L=2$, $p=5$ gives $1 + 3.2 + 5.12 =$ **9.32**, versus 20.2: information sharing removes about **54%** of the amplification but not all, because lead times still add.

### Example
Excel illustration. Customer demand: 100 for five weeks, then a step to 110 (+10%). Each stage uses MA(4) and $L=2$: order $q_t = D_t + L\,(\bar D_t - \bar D_{t-1})$ where $\bar D_t$ is the average of the last four demands it saw. Excel for cell `C8`: `=B8+$F$1*(AVERAGE(B5:B8)-AVERAGE(B4:B7))` (demand in column B, $L$ in F1), copied down; the next stage reads this column as its demand.

| Week | Customer | Retailer order | Wholesaler | Distributor | Factory |
|---|---|---|---|---|---|
| 5 | 100 | 100 | 100 | 100 | 100 |
| 6 | 110 | 115.0 | 122.5 | 133.8 | **150.6** |
| 7-9 | 110 | 115.0 | 122.5 | 133.8 | 150.6 |
| 10 on | 110 | 110 | 107.5 | 100.0 | **83.1** |

A permanent 10% rise at the customer becomes a **51% spike** at the factory (150.6 vs 100 baseline) for four weeks, then a **17% undershoot** (83.1) when the forecast windows catch up. Capacity and stock plans built on the distorted order stream are wrong twice: too big in the spike, too small in the dip.

### In the news
See news box. The sequence "cancel, scramble, glut" (chips 2020-23, then excess stock) is the same overshoot-undershoot shape.

### Interview angle
> [!question] How it is asked
> "A 10% demand rise at retail: what happens to factory orders?"

> [!tip] Strong answer includes
> - Compounding of amplification across stages (multiply, not add)
> - Numeric illustration of overshoot and the later undershoot
> - Centralised information bound and its limit (lead times still add)
> - Operations impact: capacity, overtime, then idle time and inventory write-offs

---

## 5. Price Promotions, Forward Buying and Order Batching: Numbers
> 🔴 Tier 1 · _Key points:_ forward-buy quantity, promotion spikes, EDLP; batching and order frequency

### Definition
**Forward buying**: a retailer buys more than needed at a temporary discount. For a one-off special price $\delta$ below the regular price, with regular lot $Q_0=\sqrt{2DS/h}$ and holding cost $h$ per unit per period, the cost-minimising special order is approximately

$$Q_{special} = Q_0 + \frac{\delta D}{h}$$

The more the discount per unit and the lower the holding cost, the larger the forward buy; orders then drop to zero for months. **Order batching**: ordering weekly, monthly or in full pallets/trucks makes orders lumpy: a supplier faces a spike every month even if consumption is smooth. Both are **rational** at the buyer, yet raise upstream variance and inventory.

### Example
Retailer demand $D=1{,}000$ units a month, price ₹100, order cost $S=₹2{,}000$, holding $h=₹2$ per unit per month. $Q_0=\sqrt{2\times1000\times2000/2}=$ **1,414**, i.e. an order every 1.4 months. The manufacturer offers ₹5 off for one purchase: $Q_{special} = 1{,}414 + 5\times1{,}000/2 =$ **3,914** (3.9 months of cover). Savings versus buying normally for the same 3.9 months (incl. ordering and holding) are about **₹13,300**: the retailer wins. The manufacturer sees one order **2.8x** the normal lot (3,914 vs 1,414), followed by about 4 months of near-zero orders against steady consumption of 1,000 a month. Everyday low pricing (EDLP) removes the incentive: $\delta=0$ gives $Q=Q_0$.

### In the news
See news box. Anticipation of a price or policy change (tariff front-loading, shortage allocation) works like a promotion and pulls demand forward; the aftermath is the dead-stock rise noted in the news box.

### Interview angle
> [!question] How it is asked
> "Does trade promotion cause bullwhip? What would you do as a FMCG supply chain head?"

> [!tip] Strong answer includes
> - Forward buying and promotion spikes: buyer rational, chain irrational
> - Remedies: EDLP or smaller, scheduled promotions, pay-for-performance/scan-based trading, limit forward buy, share promotion calendars (CPFR)
> - Quantify the spike and the trough after the promotion
> - Include batching: lower ordering cost with e-ordering, consolidate multi-product loads, see [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]

---

## 6. Rationing, Shortage Gaming and Panic Ordering
> 🔴 Tier 1 · _Key points:_ proportional allocation, phantom orders, cancellations, post-shortage collapse

### Definition
When supply is short and the supplier **allocates in proportion to orders** (e.g. 50% of whatever each customer asks), customers **inflate** orders to get a bigger share; the supplier reads inflated orders as demand and expands capacity; when supply recovers, customers cancel or cut orders and the supplier is left with overcapacity and stock. Variants: **panic buying** at consumer level (toilet paper, masks, eggs), **double ordering** with several suppliers, **order cancellation** in downturns.

**Allocation based on past sales** (not current orders) removes the incentive to exaggerate.

### Example
Five dealers each genuinely need 100 units (500 in all); the supplier can make 250 and allocates **pro rata to orders**. If all order honestly (100), each gets 50. If one dealer inflates to 200 while the other four stay honest, total orders are 600, so each unit ordered gets 250/600 = 41.7%: the inflater receives **83.3** and each honest dealer **41.7**. Gaming pays, so every dealer inflates: all five order 200, total orders 1,000, each gets 25% of 200 = 50, which is exactly what honesty would have delivered, but the supplier now believes demand is 1,000, twice the truth. If it adds capacity of 500 and the shortage ends, genuine demand of 500 uses only half the new capacity: 50% idle. Under **allocation based on past sales** (each sold 100 last quarter) every dealer gets 50 whatever it orders, so exaggeration earns nothing.

### In the news
See news box. The chip-market sequence of cancellations then double-ordering is the case study; the later dead-stock growth is the cost.

### Interview angle
> [!question] How it is asked
> "A key component is on allocation. How do you prevent customers from gaming it?"

> [!tip] Strong answer includes
> - Mechanism: allocation proportional to orders rewards exaggeration
> - Fix: allocate by historical sales or share, require orders to be non-cancellable, capacity reservation contracts, order-to-delivery visibility
> - Judge real demand with sell-through data, not orders
> - Caution about capacity investments based on shortage orders

---

## 7. The Beer Distribution Game and Misperception of Feedback
> 🔴 Tier 1 · _Key points:_ four-stage chain, delays, Sterman (1989), supply-line neglect

### Definition
The **Beer Distribution Game** (MIT Sloan, Jay Forrester's group; analysed by John Sterman, 1989) is a role-play of a single-product chain: **Retailer, Wholesaler, Distributor, Factory** (brewery). Each team member sees only their neighbours' orders, places an order each week, and faces **order and shipment delays** (about two weeks each). Customer demand is **constant (4 cases a week) and then steps up once (to 8)** at a pre-set week. Costs: holding (typically $0.50 per case per week) and backlog (typically $1.00): the aim is to minimise team cost.

Typical outcome: huge oscillations, inventory first collapses into backlog, then massive overstocks, and orders upstream swing by large multiples. **Not caused by external randomness**: the structure (delays, no shared information) plus player decision rules produce it. Sterman's analysis: players follow an **anchoring-and-adjustment** rule (order = expected demand + adjustment to correct stock) but **under-weight the supply line** (orders already placed), so they keep ordering while the pipeline is full: "misperception of feedback". (Check the paper for the estimated weight on the supply line before quoting a figure.)

### Example
Step demand 4 to 8 at week 5. The retailer sees stock fall, orders 12, then 16; deliveries arrive two weeks late; the retailer panics and orders more; weeks later large deliveries arrive when demand is still 8 and the retailer cancels orders to zero; the wholesaler, distributor and factory see even larger swings with longer delays. In a typical run the factory's peak order can be several times the consumer's 8 cases. In class, the **cure**: allow all players to see the real consumer demand every week; amplification collapses.

### In the news
See news box. Real-world double-ordering (chips, containers, eggs) is the Beer Game, played for billions.

### Interview angle
> [!question] How it is asked
> "What are the lessons of the Beer Game?"

> [!tip] Strong answer includes
> - Structure causes behaviour: delays + local decisions + no shared data
> - Players ignore the pipeline (supply line); correct by ordering to a target *inventory position* (stock + on order)
> - Remedy demonstrated in class: share end-demand, reduce delays, coordinate
> - Link to systems thinking and S&OP: see [[005 Production & Operations Planning]]

---

## 8. Information Sharing: POS Data, VMI and CPFR
> 🔴 Tier 1 · _Key points:_ sell-through data, VMI, CPFR, quantified benefit, conditions

### Definition
Information-sharing approaches:
- **POS / sell-through data sharing**: upstream stages see consumer demand rather than downstream orders: removes cause 1 (signal processing). Benefit is larger when demand is **autocorrelated** and when **lead time** is long (Lee, So and Tang, 2000).
- **Vendor-managed inventory (VMI)**: supplier owns replenishment decisions for the buyer's stock using the buyer's data (see [[003 Inventory Management]]); suppliers can smooth and consolidate shipments.
- **CPFR (Collaborative Planning, Forecasting and Replenishment)**: joint business plan, shared forecast, exception handling, shared promotions calendar.
- **Advance demand information, shared capacity and inventory visibility, control towers** ([[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]).

Limits: information alone does not fix lead time, batching or incentives; confidentiality and trust, data quality ([[175 Data Quality, Master Data & Data Governance]]), and benefits that accrue upstream while costs are downstream (alignment needs a contract; see [[137 Supply Chain Contracts & Game Theory]]).

### Example
From the four-stage model, centralised POS information cuts amplification from about 20.2x to 9.32x (-54%). A manufacturer receiving daily POS from a retailer for 300 SKUs uses it to cut forecast error (WAPE) on promotions from 38% to 27% and to reduce safety stock in proportion: $SS\propto\sigma_{error}$, and $27/38 = 0.71$, so about $-29\%$ stock; on ₹40 cr of safety stock that is about **₹11.6 cr** of inventory, or ₹2.3 cr a year of carrying cost at 20%. (Illustrative figures.)

### In the news
See news box. P&G and Walmart's data-sharing and VMI are the textbook response to the Pampers pattern described in the Sloan Management Review article.

### Interview angle
> [!question] How it is asked
> "A retailer won't share POS data. How do you reduce bullwhip anyway?"

> [!tip] Strong answer includes
> - Business case for the retailer: fewer stock-outs, lower inventory, better promotions
> - Start narrow: top SKUs, weekly sell-through, one category
> - Non-data levers: smaller order batches, shorter lead time, allocation on sales history
> - Contracts that share benefits (gain share, scan-based trading)

---

## 9. Countermeasures Mapped to Causes
> 🔴 Tier 1 · _Key points:_ cause-to-fix table; operational, informational and incentive levers

### Definition
| Cause | Information fix | Operational fix | Incentive / commercial fix |
|---|---|---|---|
| Demand signal processing | POS sharing, CPFR, centralised demand data | Shorter lead time ($L$), longer forecast window or smoother $\alpha$, order-up-to based on sell-through | Reward forecast quality at partners |
| Order batching | EDI and e-ordering to cut order cost | Smaller, more frequent orders, mixed-pallet loads, third-party consolidation, milk runs | Freight and handling pricing by frequency rather than lot size |
| Price fluctuations | Share promotion calendars | Smaller scheduled promotions, forward-buy limits | **EDLP**, scan-based trading, pay-for-sell-through, cap on promotion quantities |
| Rationing and gaming | Share inventory and capacity data | Allocation on sales history, capacity reservations, flexible capacity | Non-cancellable orders, penalties for cancellations |

Smoothing orders is not free: lower order variability means more stock variability or lower service, so set it by the cost trade-off (production smoothing vs inventory). Compare VMI in [[003 Inventory Management]] and S&OP in [[120 Integrated Business Planning (IBP) & S&OP Maturity]].

### Example
FMCG distributor: monthly orders from sub-distributors spike at month end because of sales-target incentives. Fixes: (1) weekly ordering with order-up-to targets (cuts batching), (2) cap month-end schemes at 110% of the trailing average (cuts price/target distortion), (3) share secondary-sales data with the manufacturer weekly (cuts signal processing). Measured result in the trial region: coefficient of variation of weekly orders falls from 0.42 to 0.28; the order-to-sales variance ratio falls from 3.1 to 1.5 (illustrative values for the design of a KPI).

### In the news
See news box. After the shortage-and-glut episode, firms moved to visibility and flexible-capacity clauses; evidence of how widely is not established in these sources.

### Interview angle
> [!question] How it is asked
> "Give me five ways to reduce bullwhip in this FMCG chain."

> [!tip] Strong answer includes
> - Cause-to-fix table, with at least one of each type (information, operational, incentive)
> - Quantify: target BW ratio, CV of orders, lead time
> - Sequence: quick wins (promotion calendar, order frequency), then structural (VMI, lead time)
> - Trade-offs and metrics so the fix does not simply move the problem

---

## 10. Cases: P&G Pampers, HP Printers, Barilla
> 🔴 Tier 1 · _Key points:_ what was observed, cause, remedy

### Definition
- **Procter & Gamble, Pampers (Lee et al. 1997):** consumer purchases of diapers were fairly smooth, but orders from distributors to P&G and from P&G to its materials suppliers (3M is named in the article) swung much more. Causes: batching, promotions, forecasting from orders. Response: continuous replenishment and shared data with retailers (Walmart is the standard example), EDLP and the **Efficient Consumer Response** movement.
- **Hewlett-Packard, printers:** reseller sales swung moderately but their orders swung more, and orders from the printer division to the integrated-circuit division swung even more. Causes: forecasting from orders, long lead times, promotions. Response: reduce order lead time, share channel sell-through data.
- **Barilla (HBS case, Hammond):** the Italian pasta maker's delivery requests from distributors were very spiky because of promotions and batching; **Just-in-Time Distribution (JITD)** has Barilla decide shipments from distributors' sell-through data. (Case summary from the Harvard Business School teaching case; check the case text before citing details.)
- **Campbell Soup** is named in the Lee article as an early participant in the Efficient Consumer Response initiative.

### Example
Describe a case in **STAR-style cause-effect-fix** form: "Observation: consumers use 1,000 diapers a day; distributors' orders to the plant range 400 to 2,200; Cause: promotions and weekly batching; Fix: daily POS sharing and VMI plus EDLP; Result: order CV falls, DC stock falls." Use only numbers you can source; the Pampers case article gives the pattern, not a set of values for each stage.

### In the news
See news box (the Sloan Management Review article, source for P&G and HP).

### Interview angle
> [!question] How it is asked
> "Name a company that dealt with bullwhip and what it did."

> [!tip] Strong answer includes
> - Company, observed pattern, diagnosed cause, remedy, effect
> - Honesty about numbers: pattern known, specifics unquoted
> - Link between the remedy and the four causes
> - A current example: chips, post-COVID stock

---

## 11. Post-COVID Bullwhips: Chips, Containers, Toilet Paper and the Stock Hangover
> 🔴 Tier 1 · _Key points:_ panic buying, double ordering, long lead times, glut after shortage

### Definition
2020-2023 provided several textbook bullwhip cycles:
- **Consumer panic buying** (toilet paper, masks, eggs): retail sales spike above consumption; retailers order extra; manufacturers add shifts; demand normalises and shelves overflow.
- **Semiconductors:** carmakers cut orders expecting a slump, then could not meet the rebound; chip lead times lengthened to 15 to 22 weeks (see news box); buyers commonly responded with larger or duplicate orders (the standard shortage-gaming pattern); by 2023 the shortage had mostly subsided as growth slowed.
- **Containers and ports:** congested ports lengthened lead times, importers ordered earlier and in larger quantities, then carried stock when demand weakened.
- **Tariffs and policy shocks (2025-26):** front-loading before tariff changes is a pull-forward that tends to be followed by weaker orders; separately, the news-box survey reports dead stock rising as a share of small firms' excess inventory.

Common mechanisms: long and rising lead time $L$ (formula in sub-topic 3), cause 4 gaming, and pull-forward followed by hangover. The right response is visibility, tiered safety stock for critical parts ([[015 Supply Chain Risk & Resilience]]), flexible contracts, and not treating orders as demand.

### Example
A tier-2 auto supplier sees orders double for six weeks. Before investing in capacity: (1) compare orders with the OEM's vehicle build schedule (sell-through), (2) test for double ordering with duplicate part numbers or multiple suppliers, (3) estimate real demand at, say, +20% not +100%, (4) offer **flex capacity** (overtime and a shift) rather than capex. If true demand is +20% and orders are +100%, building capacity for +100% leaves 40% of the new capacity idle: $1 - 1.2/2.0 = 0.40$.

### In the news
See news box. The Netstock survey figures (dead stock 24% of excess inventory in 2026) quantify the hangover; the chip lead times quantify $L$.

### Interview angle
> [!question] How it is asked
> "Orders for our product have doubled. Should we build capacity?"

> [!tip] Strong answer includes
> - First test whether orders equal demand (sell-through, double-ordering, allocation gaming)
> - Estimate true demand range, then flex capacity before fixed capacity
> - Contract protection: take-or-pay, cancellation windows, capacity reservation fees
> - Plan for the downside: what happens to stock and capacity when orders normalise

---

## 12. Measuring and Dashboarding Bullwhip in Real Data
> 🔴 Tier 1 · _Key points:_ order vs demand variance by node, deseasonalise, shipments vs orders, periodicity

### Definition
Practical measurement steps:
1. Define the **node** (distributor, DC, plant), the **demand** it sees (outbound shipments/sales) and the **orders** it places (purchase orders or production orders) in the same time bucket (week or month).
2. **Remove seasonality and trend** (use residuals or a deseasonalised series): otherwise the ratio reflects planned seasonality. Cachon, Randall and Schmidt (2007) is a known empirical study that found amplification mainly at some levels of US industry data and not at others, so measure your own chain rather than assuming bullwhip.
3. Compute $BW=\text{Var}(orders)/\text{Var}(demand)$ per SKU group, then **volume-weight**. Also compute CV by stage and the **peak-to-average** ratio.
4. Segment by SKU class (ABC-XYZ), by customer, by promotional vs non-promotional weeks.
5. Track alongside **forecast accuracy**, service level and inventory days (see [[012 Supply Chain Analytics & KPIs]]).

```python
import pandas as pd
df = pd.read_csv("weekly_flow.csv")        # columns: sku, week, shipments, orders_placed
g = df.groupby("sku")
bw = (g["orders_placed"].var() / g["shipments"].var()).rename("BW")
cv = (g["orders_placed"].std()/g["orders_placed"].mean()) / (g["shipments"].std()/g["shipments"].mean())
print(pd.concat([bw, cv.rename("CV_ratio")], axis=1).sort_values("BW", ascending=False).head(10))
```

### Example
A distributor's weekly shipments (demand) have s.d. 420 units (mean 2,000, CV 0.21) and its purchase orders s.d. 780 (mean 2,000, CV 0.39). $BW=(780/420)^2=$ **3.45**; CV ratio **1.86**. Splitting the data: in promo weeks BW is 5.1, in non-promo weeks 1.4 (illustrative), so the issue is promotion-driven. Action: promotion calendar sharing and a cap on forward buy in the trade scheme. See also [[064 Pandas — Data Manipulation]] and [[045 SQL for Operations Analytics]].

### In the news
See news box. After the hangover, boards ask for early-warning dashboards; a bullwhip ratio by supplier belongs next to OTIF and days of cover.

### Interview angle
> [!question] How it is asked
> "How would you check whether the client has a bullwhip problem?"

> [!tip] Strong answer includes
> - Order variance vs demand variance at each node, over a long window and deseasonalised
> - Split by SKU class and promotional vs non-promotional
> - Compare with a benchmark or with upstream nodes, not a single number
> - Link to root causes and propose targeted fixes

---

## 13. ⭐ Advanced: When Amplification Is Rational and the Information-Sharing Value Trade-off
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Two cautions beyond the textbook. (1) **Production smoothing vs bullwhip:** if the production cost is convex (overtime, setup), a plant *wants* to smooth production relative to demand, which reduces the bullwhip; if there are fixed ordering costs or stock-out costs, it may amplify. Order variance above demand variance is not always a mistake: it can be the **cost-minimising** response to batching and seasonality. Empirical studies (e.g. Cachon, Randall and Schmidt, 2007) report mixed evidence across industries, so diagnose the cause before prescribing a fix. (2) **Value of information sharing** is not uniform: it is larger when lead times are long, demand is autocorrelated and the supplier has little slack capacity, and smaller when the retailer's orders are already near-optimal. Quantify with the multi-stage formula and the cost of the sharing infrastructure.

Decision rule for investing in sharing: benefit $\approx$ (reduction in safety stock + reduction in expediting + service gain) minus (IT, integration and governance cost).

### Example
Manufacturer with safety stock ₹40 cr, carrying cost 20% and expediting cost ₹3 cr a year. Sharing POS data cuts the amplification at its stage from 2.12 to 1.35, so the s.d. of orders relative to demand falls from $\sqrt{2.12}=1.46$ to $\sqrt{1.35}=1.16$ (-20%). If safety stock scales with that s.d.: ₹40 cr x 20% = **₹8 cr** less stock, worth ₹1.6 cr a year in carrying cost; expediting down by a third saves ₹1.0 cr. Benefit **₹2.6 cr** a year. Cost: a one-off ₹1.5 cr integration spread over 3 years (₹0.5 cr) plus ₹0.4 cr a year of run and governance = ₹0.9 cr. Net about **₹1.7 cr** a year: positive but modest, so start with the highest-variance SKUs where benefit per rupee is greatest. (Illustrative inputs.)

### In the news
See news box. Tariff and shortage cycles make demand autocorrelated and lead times long, conditions in which sharing pays off most.

### Interview angle
> [!question] How it is asked
> "Is bullwhip always bad? How would you build the business case for a data-sharing platform?"

> [!tip] Strong answer includes
> - Nuance: some amplification is cost-optimal; diagnose causes
> - Value of sharing depends on lead time, correlation and capacity slack
> - Benefit in stock, expediting and service minus platform cost, with sensitivity
> - Pilot first with high-variability SKUs; review with partners
