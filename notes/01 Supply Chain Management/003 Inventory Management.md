---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Inventory Management"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 16
---
# Inventory Management

⬅ [[002 Procurement & Strategic Sourcing]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[004 Demand Forecasting & Planning]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Types of Inventory]]
2. [[#2. EOQ Model]]
3. [[#3. Reorder Point (ROP)]]
4. [[#4. Safety Stock Calculation]]
5. [[#5. ABC Analysis]]
6. [[#6. FSN Analysis]]
7. [[#7. VED Analysis]]
8. [[#8. HML Analysis]]
9. [[#9. JIT Inventory]]
10. [[#10. Cycle Stock vs Buffer Stock]]
11. [[#11. Dead Stock & Obsolescence]]
12. [[#12. Inventory Turnover Ratio]]
13. [[#13. Consignment & VMI]]
14. [[#14. Inventory KPIs]]
15. [[#15. ⭐ Advanced: Newsvendor Model & Critical Ratio]]
16. [[#16. ⭐ Advanced: Risk Pooling, Postponement & Multi-Echelon Inventory]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): tariffs and chip shortages turned inventory into a strategic decision
> **Tariff front-loading (early 2025).** The NRF / Hackett Associates Global Port Tracker reported loaded US import volumes up **13.4% year on year in January 2025** and projected **+6.1% in February and +10.8% in March** as retailers imported "as much merchandise ... ahead of rising tariffs as possible" (20% tariffs on Chinese goods already in force, reciprocal tariffs scheduled for 2 April). It projected the first year-on-year decline since September 2023 for June-July. ([Supply Chain Dive](https://www.supplychaindive.com/news/loaded-import-volume-forecast-national-retail-federation-tariffs-trump/742071/))
> 
> **Nexperia and thin buffers (Oct 2025).** Honda cut output at US and Canadian plants and halted its Celaya plant in Mexico (over 190,000 vehicles built the previous year) because of a Nexperia chip shortage; Nissan surveyed its parts makers. Lean, just-in-time stocks of a cheap component left almost no cushion. ([Japan Times](https://www.japantimes.co.jp/business/2025/10/30/companies/honda-mexico-production-halt/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Types of Inventory
> 🔴 Tier 1 · _Tracker hint:_ Raw material, WIP, FG, MRO, transit, safety stock

### Definition
Inventory is stock held to decouple supply from demand. Classification by **form**: **Raw materials**, **Work-in-process (WIP)**, **Finished goods (FG)**, **MRO** (maintenance, repair, operating supplies: spares, lubricants, tools), **packaging**. By **function**:
- **Cycle stock**: from batch ordering/production.
- **Safety (buffer) stock**: protects against demand/lead-time uncertainty.
- **Pipeline / in-transit stock**: goods on the move; pipeline inventory = demand per day × transit days.
- **Anticipation (seasonal) stock**: built ahead of a peak or price rise.
- **Decoupling stock**: between stages of different speeds.
- **Speculative / hedge stock**.

Why hold: scale economies, uncertainty, lead time, price hedging, service level. Why not: holding cost (capital, storage, insurance, obsolescence ≈ 15-30% of value per year) and hiding problems (Lean's "inventory is waste").

### Example
A cement firm in Nashik: clinker and gypsum (raw), semi-processed in kilns (WIP), cement bags (FG), spare bearings and refractory bricks (MRO). Goods on a train to a depot, 6 days away, with 200 tonnes a day: pipeline stock = 200 × 6 = **1,200 tonnes**.

### In the news
See news box. Anticipation stock appeared in tariff front-loading; pipeline stock ballooned when shipping routes lengthened.

### Interview angle
> [!question] How it is asked
> "What types of inventory does a manufacturer hold and why?"

> [!tip] Strong answer includes
> - Both classifications (form and function)
> - Purpose of each type, with a one-line example
> - Costs of holding vs of not holding
> - Where to cut: WIP and pipeline are usually the most reducible

---

## 2. EOQ Model
> 🔴 Tier 1 · _Tracker hint:_ EOQ = √(2DS/H); assumptions, limitations

### Definition
The **Economic Order Quantity** minimises the sum of annual ordering and holding cost:

$$TC(Q) = \frac{D}{Q}S + \frac{Q}{2}H, \qquad EOQ = Q^* = \sqrt{\frac{2DS}{H}}$$

where $D$ = annual demand, $S$ = cost per order, $H$ = annual holding cost per unit ($= i \times c$). At the optimum, ordering cost = holding cost, and $TC^* = \sqrt{2DSH}$. Orders per year = $D/Q^*$; cycle time = $Q^*/D$.

**Assumptions:** constant, known demand; instantaneous replenishment; constant lead time; no quantity discounts; no stock-outs; single item; fixed S and H. **Limitations:** real demand varies; lead times vary; discounts; capacity or shelf-life limits. The cost curve is flat near $Q^*$, so ±10-20% error costs little. Extensions: EPQ (finite production rate), quantity discounts, backorders.

### Example
$D = 12{,}000$ units/yr, $S$ = ₹500, $H$ = ₹20/unit/yr.
$Q^* = \sqrt{2 \times 12000 \times 500 / 20} = \sqrt{600{,}000} \approx 775$ units.
Orders/yr = 12,000/775 ≈ 15.5. Ordering cost ≈ 15.5 × 500 = ₹7,746; holding = (775/2) × 20 = ₹7,746 (equal, as theory predicts). $TC^* = \sqrt{2 \times 12000 \times 500 \times 20} = \sqrt{240{,}000{,}000} \approx$ **₹15,492**.

### In the news
See news box. Front-loading ahead of tariffs shows when EOQ's assumptions break: a known future price jump changes the optimal order size (forward buying), which EOQ ignores.

### Interview angle
> [!question] How it is asked
> "Derive or calculate the EOQ. What happens if ordering cost halves?"

> [!tip] Strong answer includes
> - Formula, variables and the equality of the two costs at optimum
> - Sensitivity: EOQ scales with √S, so halving S reduces Q* by about 29% ($1/\sqrt2$)
> - Assumptions and why they fail in practice
> - Link: reducing setup cost (SMED, e-procurement) is the route to smaller lots

---

## 3. Reorder Point (ROP)
> 🔴 Tier 1 · _Tracker hint:_ ROP = (Avg daily demand × Lead Time) + Safety Stock

### Definition
In a **continuous review (Q, R)** system, place an order of size $Q$ when the inventory position (on hand + on order − backorders) falls to the **reorder point**:

$$ROP = d \times L + SS$$

$d$ = average demand per period, $L$ = replenishment lead time in the same units, $SS$ = safety stock. The first term is expected demand during lead time (DDLT); safety stock covers variation. Use inventory *position* (not on-hand) to avoid double ordering. Contrast the **periodic review (R, S)** system: review every $R$ days and order up to $S$; needs protection over $R + L$.

**Two-bin and kanban** are visual forms of ROP. SAP: reorder-point planning uses MRP type VB (manual reorder point) or VM (automatic reorder point, ROP computed from forecast); the MRP run is MD01 (total) / MD03 (single item).

### Example
Daily demand 40 units, lead time 6 days, safety stock 60. ROP = 40 × 6 + 60 = **300 units**. If current stock is 280 and 100 units are already on order, inventory position is 380 > 300, so no new order.

### In the news
See news box. When lead times lengthen (reroutes, tariff-driven rush), $L$ rises and ROP rises mechanically, which is how disruptions inflate inventory.

### Interview angle
> [!question] How it is asked
> "Lead time has gone from 6 to 9 days. How does your reorder point change?"

> [!tip] Strong answer includes
> - Formula and meaning of each term
> - Use of inventory position vs on-hand
> - Both mean and variance of lead time matter
> - Continuous vs periodic review trade-off

---

## 4. Safety Stock Calculation
> 🔴 Tier 1 · _Tracker hint:_ Z × σ_LT × √LT; service level Z-values

### Definition
Safety stock buffers uncertainty during the lead time. With normal demand and **fixed** lead time $L$:

$$SS = Z \times \sigma_d \times \sqrt{L}$$

($\sigma_d$ = standard deviation of demand per period, so $\sigma_{DLT} = \sigma_d\sqrt{L}$; the tracker's "σ_LT × √LT" is loosely written: the standard deviation *over the lead time* already includes the √L.) With **variable** lead time (mean $\bar L$, s.d. $\sigma_L$):

$$SS = Z\sqrt{\bar L\,\sigma_d^2 + \bar d^2\,\sigma_L^2}$$

| Cycle service level | Z |
|---|---|
| 90% | 1.28 |
| 95% | 1.65 |
| 97.5% | 1.96 |
| 99% | 2.33 |
| 99.9% | 3.09 |

Cycle service level = probability of no stock-out in a cycle; it is **not** the fill rate. Higher service levels cost increasingly more stock (diminishing returns).

### Example
$\sigma_d = 10$ units/day, $L = 9$ days, 95% service (Z = 1.65): $\sigma_{DLT} = 10\sqrt{9} = 30$; $SS = 1.65 \times 30 = 49.5 \approx$ **50 units**. Raising to 99%: 2.33 × 30 = 70 units (+41%) for 4 extra points of service.

### In the news
See news box. Honda's Nexperia exposure is a safety-stock story: stock set for normal variability did not cover a supply-side outage, which needs a different tool (strategic buffer for critical parts).

### Interview angle
> [!question] How it is asked
> "How much safety stock should we hold for this SKU?" with demand mean/s.d. and lead time given.

> [!tip] Strong answer includes
> - Correct formula, √L logic, Z from service level
> - Handles lead-time variability
> - Distinguishes cycle service level from fill rate
> - Practical caveats: non-normal demand, intermittent items, risk pooling, review period (add $R$ to $L$)

---

## 5. ABC Analysis
> 🔴 Tier 1 · _Tracker hint:_ A=high value/low vol; B=mid; C=low value/high vol; 80-20 rule

### Definition
ABC classifies items by **annual consumption value** (annual usage × unit cost) using Pareto logic. Typical cut-offs:

| Class | % of items | % of annual value | Control |
|---|---|---|---|
| **A** | ~10-20% | ~70-80% | Tight: frequent review, accurate records, low safety stock, close supplier follow-up |
| **B** | ~30% | ~15-20% | Moderate |
| **C** | ~50-60% | ~5-10% | Loose: bulk orders, two-bin, higher safety stock, simple controls |

Steps: compute value per item, sort descending, compute cumulative %, cut at thresholds. Limitation: ignores criticality (a cheap vital part may be class C) so combine with **VED**.

### Example
Annual values (₹ lakh): P 500, Q 300, R 100, S 60, T 40 (total 1,000). Cumulative: P 50%, Q 80%, R 90%, S 96%, T 100%. **A** = P and Q (2 of 5 items = 40% of items, 80% of value); **B** = R; **C** = S and T. (With 1,000 real SKUs the A group is typically far smaller.)

### In the news
See news box. In tariff-driven front-loading, retailers prioritised A items (high-value, high-turn) to pull forward, while C items were left to normal replenishment.

### Interview angle
> [!question] How it is asked
> "How would you reduce inventory in a warehouse with 20,000 SKUs?"

> [!tip] Strong answer includes
> - ABC as first cut with cumulative value table
> - Different policies by class (service level, review frequency)
> - Combine with XYZ (demand variability) and VED (criticality)
> - Quantify: eg A items 15% of SKUs, 75% of value -> focus there

---

## 6. FSN Analysis
> 🔴 Tier 1 · _Tracker hint:_ Fast/Slow/Non-moving; application in warehouse slotting

### Definition
**FSN** classifies items by **movement frequency** (issues or picks per period) or time since last movement, not by value:
- **F (Fast-moving)**: frequent consumption; keep near dispatch, high availability.
- **S (Slow-moving)**: infrequent; stock minimal, review replenishment.
- **N (Non-moving)**: no issue for a defined period (e.g. 12-24 months); candidate for disposal or write-down.

Criteria are set per business (eg F: movements > 12 per year; S: 1-12; N: 0). Uses: **warehouse slotting** (fast items at golden zone near docks, shorter pick paths), reducing obsolescence, setting differentiated safety stock, identifying dead stock. Often combined: **ABC-FSN matrix** (e.g. A-F: tight control; C-N: dispose).

### Example
Hardware distributor: SKU 101 picked 480 times/yr (F), SKU 202 picked 6 times (S), SKU 303 not picked in 18 months (N). Moving 101 to the pick face nearest the packing area saves walking: if each pick saves 10 metres and a picker walks at 1 m/s, 480 picks save 4,800 m, about **80 minutes** a year for one SKU; multiplied across hundreds of fast SKUs the saving is large.

### In the news
See news box. Post-tariff, retailers sitting on front-loaded goods that slowed down needed FSN to find which SKUs became slow-moving and mark them down.

### Interview angle
> [!question] How it is asked
> "How would you arrange a warehouse for an e-commerce firm?"

> [!tip] Strong answer includes
> - FSN definition with thresholds
> - Slotting logic: fast near dock, heavy items low, correlated items together
> - Combine FSN with ABC (value) and cube (size)
> - Dynamic re-slotting with seasonality

---

## 7. VED Analysis
> 🔴 Tier 1 · _Tracker hint:_ Vital/Essential/Desirable; used in spare parts & healthcare SCM

### Definition
**VED** ranks items by **criticality** of stock-out:
- **Vital**: stock-out stops production or endangers life; zero tolerance, high service level (98-99%+).
- **Essential**: stock-out causes disruption but workable for a short time; moderate service level.
- **Desirable**: stock-out has little impact; lowest level.

Used for spares (MRO), hospitals/pharmacy (life-saving drugs, vaccines), defence and public health supply chains. **ABC-VED matrix**: category I (AV, AE, BV, CV): tight control; category II (BE, CE, AD, BD ...); category III (CD): minimal. VED prevents the ABC mistake of neglecting cheap but critical parts. Criticality is a management judgement, so use a committee and review annually.

### Example
Hospital: adrenaline injection (cheap, class C by value) is **Vital**: hold 99% availability; a luxury hospital-room item is **Desirable**. A power plant: a ₹800 relay that shuts down a turbine (vital) is stocked even though annual value is low.

### In the news
See news box. A Nexperia chip costing a few rupees was "vital" in VED terms; the shortage shows that value-based ABC alone mis-prioritised it.

### Interview angle
> [!question] How it is asked
> "How would you manage inventory of spare parts or medicines?"

> [!tip] Strong answer includes
> - VED defined by consequence of stock-out
> - ABC-VED matrix to set control levels
> - Service-level targets by class
> - Governance: criticality committee, regular re-classification

---

## 8. HML Analysis
> 🔴 Tier 1 · _Tracker hint:_ High/Medium/Low unit cost; financial control focus

### Definition
**HML** classifies items by **unit price** (not annual value): **H** high-cost units, **M** medium, **L** low. Cut-offs are set by the firm (eg H above ₹10,000, M ₹1,000-10,000, L below ₹1,000). Purpose: financial control and **security**: H items (e.g. electronic modules, precious tools) need locked storage, authorisation, frequent counts and close approval of issues; L items can be left in open bins with simple controls and bulk ordering.

Compare: ABC = value × volume; HML = unit cost only; FSN = movement; VED = criticality; **SDE** (scarcity: Scarce/Difficult/Easy to procure) and **GOLF** (Government/Ordinary/Local/Foreign sources) address availability. Together they form a multi-criteria classification.

### Example
A store has a ₹45,000 PLC card (H, 2 units, locked, cycle-counted monthly), ₹2,500 contactors (M), and ₹15 fasteners (L, 50,000 units in open bins). Annual value may make fasteners class C and PLC cards class B, but HML determines how they are physically secured.

### In the news
See news box. High-value electronics held as safety stock (H class) require careful control: tying capital and inviting shrinkage or obsolescence.

### Interview angle
> [!question] How it is asked
> "Name different inventory classification techniques and when you'd use each."

> [!tip] Strong answer includes
> - HML basis and use (unit cost, control and security)
> - Contrast with ABC, FSN, VED
> - Multi-criteria approach to avoid blind spots
> - Practical example from stores/MRO

---

## 9. JIT Inventory
> 🔴 Tier 1 · _Tracker hint:_ Zero inventory goal, pull system, supplier proximity requirements

### Definition
**Just-in-Time** (Toyota Production System, Taiichi Ohno) delivers *only what is needed, when needed, in the quantity needed*. Pillars: **pull** (kanban cards), **takt time**, small lot sizes (SMED to cut setup), level scheduling (**heijunka**), quality at source (jidoka), **supplier integration** (frequent small deliveries, milk runs, supplier parks), continuous improvement. Goal: cut inventory, which hides problems like a high water level hides rocks.

Prerequisites: stable, levelled demand; reliable short lead times; very high quality; close suppliers; strong trust. **Risks**: no buffer for disruptions (Japan 2011 earthquake, Nexperia 2025), supplier fragility, transport delays. Modern view: **JIT + resilience** (strategic buffers for critical or single-sourced parts, "just-in-case" selectively).

### Example
Toyota's kanban: a container of 20 bolts is emptied on the line; its card signals the supplier to deliver exactly one container. Dell assembles after the order, holding components for only days. Kanban count: $k = \dfrac{d \times (w + p)(1+\alpha)}{c}$; with $d$ = 120/hr, lead time (wait + process) 0.5 hr, container size 20, safety factor 10%: $k = 120 \times 0.5 \times 1.1 / 20 = 3.3 \to$ **4 cards**.

### In the news
See news box. Honda's plant halts under the Nexperia shortage are a live case of JIT fragility: thin buffers turned a component outage into a vehicle-line stoppage within days.

### Interview angle
> [!question] How it is asked
> "Is JIT still relevant after COVID and chip shortages?"

> [!tip] Strong answer includes
> - JIT principles (pull, small lots, quality, supplier proximity)
> - Prerequisites and risk when they are absent
> - Hybrid: JIT for stable, local, multi-sourced parts; buffers for critical/long-lead items
> - Indian context: poor logistics and monsoon variability make blind JIT risky

---

## 10. Cycle Stock vs Buffer Stock
> 🔴 Tier 1 · _Tracker hint:_ Cycle = regular replenishment; Buffer = uncertainty hedge

### Definition
| | Cycle stock | Buffer (safety) stock |
|---|---|---|
| Purpose | Meet demand between replenishments | Hedge demand/lead-time uncertainty |
| Driver | Lot size $Q$ | Variability and service level |
| Average level | $Q/2$ | $SS$ (all the time) |
| Reduce by | Lower ordering/setup cost, smaller lots | Reduce variability, shorten lead time, pool, improve forecasts |

Average inventory = $Q/2 + SS$. Cycle stock falls with smaller lots (EOQ); buffer stock falls with better information and shorter lead time. Cycle stock is "planned"; buffer is "insurance".

### Example
EOQ 775 units, safety stock 50: average inventory = 775/2 + 50 = **437.5 units**. If setup cost halves, EOQ becomes 548 (775/√2); cycle stock falls from 387.5 to 274, average inventory to 324 (-26%) while buffer is unchanged.

### In the news
See news box. In 2025 firms raised **buffer** stock (tariff and shortage hedging); cycle stock logic is separate and unaffected by uncertainty.

### Interview angle
> [!question] How it is asked
> "What drives cycle stock and what drives safety stock? How would you reduce each?"

> [!tip] Strong answer includes
> - Q/2 vs SS and their drivers
> - Levers to reduce each
> - Link to EOQ and service level
> - Total average inventory formula

---

## 11. Dead Stock & Obsolescence
> 🔴 Tier 1 · _Tracker hint:_ Identification, disposal, prevention strategies

### Definition
**Dead stock**: inventory with no demand for an extended period (e.g. 12-24 months) and little chance of selling at full value; **obsolete stock**: outdated by technology, design change or expiry; **excess**: above forecast needs (e.g. more than 12 months' cover).

**Identification:** aging report, FSN (N class), days of cover vs shelf life, expiry date reports, slow-turn report. **Disposal:** discount/liquidation, bundling, return to vendor, transfer to another channel/region, cannibalise for spares, donate (tax benefit), scrap/recycle; write-down per accounting standards (Ind AS 2: lower of cost and net realisable value). **Prevention:** better forecasts, lower MOQs, postponement, end-of-life planning, first-expired-first-out (FEFO), vendor buy-back clauses, SKU rationalisation, ABC/FSN reviews.

### Example
₹2 crore of electronics stock has had no movement for 24 months; net realisable value is estimated at ₹60 lakh. Write-down = ₹2.0 cr − ₹0.6 cr = **₹1.4 cr** hit to profit. Compare with the holding cost avoided had it been prevented: ~20% × ₹2 cr = ₹40 lakh a year.

### In the news
See news box. A front-loaded tariff build-up risks a hangover: Port Tracker forecast the first import decline since September 2023 for June-July 2025, consistent with retailers working off pulled-forward stock.

### Interview angle
> [!question] How it is asked
> "A company has 15% obsolete stock. What would you do?"

> [!tip] Strong answer includes
> - Quantify and age the stock first
> - Disposal ladder (return, rework, liquidate, scrap) with finance involvement
> - Root cause: forecast bias, MOQ, product-change management
> - Preventive KPIs: aged stock %, excess days of cover

---

## 12. Inventory Turnover Ratio
> 🔴 Tier 1 · _Tracker hint:_ COGS / Avg Inventory; higher = leaner, Days Inventory Outstanding

### Definition
$$ITR = \frac{COGS}{\text{Average inventory}}, \qquad DIO = \frac{365}{ITR} = \frac{\text{Avg inventory}}{COGS}\times 365$$

Average inventory = (opening + closing)/2. Higher turns mean leaner stock and lower holding cost, but too high may signal stock-outs. Compare within industry (grocery 20+ turns, auto OEM 10-20, capital goods 3-5 are indicative bands, not benchmarks to quote as facts). Linked to the **cash-to-cash cycle** = DIO + DSO − DPO. Also **GMROI** = gross margin / average inventory at cost, used in retail.

### Example
COGS ₹600 cr; opening inventory ₹90 cr, closing ₹110 cr, average ₹100 cr. ITR = 600/100 = **6.0**; DIO = 365/6 ≈ **61 days**. If management raises turns to 8: average inventory = 600/8 = ₹75 cr, releasing ₹25 cr of cash; at 10% cost of capital, ₹2.5 cr a year.

### In the news
See news box. Tariff front-loading pushes ITR down temporarily (inventory up, COGS later); analysts read turnover and DIO in earnings to see whether the stock will be worked off.

### Interview angle
> [!question] How it is asked
> "Inventory turns fell from 8 to 6. What could be the reasons?"

> [!tip] Strong answer includes
> - Formula and DIO conversion; cash release arithmetic
> - Diagnose: sales slowdown vs inventory build, mix, front-loading, forecast error
> - Benchmark vs industry
> - Warn about over-optimising (stock-outs)

---

## 13. Consignment & VMI
> 🔴 Tier 1 · _Tracker hint:_ Vendor-managed inventory; ownership transfer point

### Definition
- **Consignment stock:** the supplier owns goods held at the customer's site; **title transfers on consumption** (when used or sold), and the customer pays then. Customer saves working capital; supplier carries inventory cost.
- **VMI (Vendor-Managed Inventory):** the supplier monitors the customer's stock (via EDI/POS data) and decides when and how much to replenish within min/max limits. VMI can be **with or without consignment**: ownership may transfer on receipt or on consumption.
- **Benefits:** lower stock-outs, reduced bullwhip, fewer orders, shared forecast; **risks:** data trust, supplier burden, dependency, disputes about ownership and obsolescence.

Mechanics in SAP: consignment uses special stock indicator **K**; the liability is settled with **MRKO**; goods movement via MIGO. Related: CPFR (see [[004 Demand Forecasting & Planning]]).

### Example
Walmart and Procter & Gamble (late 1980s) pioneered VMI: P&G monitored Walmart's DC stock of Pampers and shipped on its own, improving in-stock and cutting inventory. Hospitals use consignment for implants/stents: the vendor places a stock at the hospital, billed only for items used.

### In the news
See news box. Buyers hit by shortages sought consignment/hub arrangements with chip suppliers to hold stock near the plant without carrying the cost (a general practice response, not a sourced statistic).

### Interview angle
> [!question] How it is asked
> "When would you recommend VMI or consignment?"

> [!tip] Strong answer includes
> - Definitions and ownership transfer point
> - Who benefits/bears cost; what data must be shared
> - Conditions: high volume, stable items, trusted partners, IT integration
> - Risks and contract terms (min/max, obsolescence, audit)

---

## 14. Inventory KPIs
> 🔴 Tier 1 · _Tracker hint:_ Fill rate, stock-out rate, holding cost%, ITR, shrinkage%

### Definition
| KPI | Formula |
|---|---|
| **Fill rate** | Units shipped from stock / units demanded (line fill rate by order lines) |
| **Stock-out rate** | Stock-out occasions / demand occasions (or SKU-days out of stock / SKU-days) |
| **Holding (carrying) cost %** | Annual holding cost / average inventory value (capital + storage + service + risk, ~15-30%) |
| **Inventory turnover / DIO** | COGS / avg inventory; 365 / ITR |
| **Shrinkage %** | (Book stock − physical stock) / book stock or sales |
| **Inventory accuracy** | Locations counted correct / locations counted |
| **GMROI** | Gross margin / avg inventory at cost |
| **Days of cover, aged stock %** | Stock / average daily demand; value older than X days / total |

Balance service KPIs (fill rate, OTIF) against financial KPIs (turns, holding cost); optimising only one distorts behaviour.

### Example
Demand in a month 10,000 units; shipped from stock 9,400: fill rate = **94%**. Book stock ₹5.00 cr, physical ₹4.90 cr: shrinkage = ₹10 lakh = **2%** of book. Holding: ₹20 cr average inventory × 22% = ₹4.4 cr/yr.

### In the news
See news box. Tariff-driven import swings forced retailers to watch days of cover and aged stock weekly instead of monthly.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track for an inventory control tower?"

> [!tip] Strong answer includes
> - Mix of service, financial and accuracy metrics
> - Formulas and definitions (fill rate vs cycle service level)
> - Segment by ABC/XYZ
> - Targets, owners, and review cadence

---

## 15. ⭐ Advanced: Newsvendor Model & Critical Ratio
> ⭐ Advanced · _Added beyond the tracker_

### Definition
For a **single-period** decision (fashion, festive, perishables) with uncertain demand $D$: order $Q$ before demand is known. Let **underage cost** $C_u$ = lost margin per unit short = price − cost; **overage cost** $C_o$ = cost − salvage per unit left. The optimal order satisfies the **critical ratio**:

$$F(Q^*) = P(D \le Q^*) = \frac{C_u}{C_u + C_o}$$

For normal demand $Q^* = \mu + z\sigma$ where $z = \Phi^{-1}(CR)$. Higher margin or lower salvage loss pushes the order up. Applications: seasonal garments, newspaper, Diwali sweets, airline overbooking, fresh produce.

### Example
Cost ₹60, price ₹100, salvage ₹40: $C_u = 40$, $C_o = 20$, $CR = 40/60 = 0.667$, so $z \approx 0.43$. Demand ~ N(100, 20): $Q^* = 100 + 0.43 \times 20 =$ **≈ 109 units** (above the mean because the miss costs more than the leftover).

### In the news
See news box. Front-loading ahead of tariffs was a newsvendor choice with an uncertain "demand" (policy outcome): overage cost of carrying goods versus underage cost of tariffs.

### Interview angle
> [!question] How it is asked
> "A retailer must order winter jackets 6 months ahead. How many should it order?"

> [!tip] Strong answer includes
> - Underage and overage costs, critical ratio
> - Order above or below mean depending on margin vs salvage
> - Tools to improve: quick response, postponement, reorders, markdown planning
> - Sensitivity to demand uncertainty

---

## 16. ⭐ Advanced: Risk Pooling, Postponement & Multi-Echelon Inventory
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Risk pooling**: aggregating demand across locations reduces relative variability. With $n$ identical, independent locations each with demand s.d. $\sigma$, pooled s.d. is $\sigma\sqrt n$ (not $n\sigma$), so safety stock falls to $1/\sqrt n$ of the decentralised total (the **square-root law**). Correlation weakens the benefit. Related pooling tools: centralised DC, **postponement** (delay differentiation, e.g. packaging or colouring at the last stage), component commonality, transshipment, universal designs.

**Multi-echelon inventory optimisation (MEIO)** sets stock levels jointly across plant, regional DCs and stores (rather than each node alone) to hit a service target at the lowest total investment; software: SAP IBP, o9, Blue Yonder, Kinaxis.

### Example
Four DCs each with demand s.d. 100/week, lead time 4 weeks, Z = 1.65. Each: SS = 1.65 × 100 × 2 = 330; total 1,320. One central DC: s.d. = 100 × √4 = 200; SS = 1.65 × 200 × 2 = 660. Saves **660 units (50%)**, at the cost of longer outbound delivery.

### In the news
See news box. Post-shock networks are balancing pooled central stock (cheaper) against regional resilience; the trade-off the square-root law quantifies.

### Interview angle
> [!question] How it is asked
> "We want to cut inventory by 20% without hurting service. What would you do?"

> [!tip] Strong answer includes
> - Risk pooling with the square-root law and numbers
> - Postponement/commonality to reduce variety-driven stock
> - Segmentation (ABC/XYZ) and service differentiation
> - Trade-offs: delivery time and transport cost rise when centralising

---
## 🔗 Go deeper: expansion notes
- [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems|Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]
- [[116 Inventory Valuation, Cycle Counting & Inventory Governance|Inventory Valuation, Cycle Counting & Inventory Governance]]
- [[117 Demand-Driven MRP (DDMRP) & Buffer Management|Demand-Driven MRP (DDMRP) & Buffer Management]]
- [[114 Bullwhip Effect, Beer Game & Information Sharing|Bullwhip Effect, Beer Game & Information Sharing]]
