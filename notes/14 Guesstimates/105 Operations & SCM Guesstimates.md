---
tags: [guesstimates, tier1]
area: Guesstimates
topic: "Operations & SCM Guesstimates"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 10
---
# Operations & SCM Guesstimates

⬅ [[104 Classic Guesstimate Types & Templates]] · [[_Index - Guesstimates|Guesstimates]] · [[106 Product & Tech Guesstimates]] ➡

> **Area:** Guesstimates · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. How many trucks cross Mumbai-Pune highway daily?]]
2. [[#2. Warehouse size needed for Amazon India fulfillment]]
3. [[#3. Inventory for a D-Mart store]]
4. [[#4. Number of delivery executives Zomato has in Mumbai]]
5. [[#5. How many cold storage facilities in India?]]
6. [[#6. Fleet size for Reliance Retail supply chain]]
7. [[#7. Lead time estimation for imported goods]]
8. [[#8. Daily production capacity of a mid-size FMCG plant]]
9. [[#9. ⭐ Advanced: Little's Law and utilisation for capacity guesstimates]]
10. [[#10. ⭐ Advanced: Top-down vs bottom-up triangulation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Dense retail and quick-commerce networks give you real numbers to sanity-check guesstimates
> **D-Mart (Avenue Supermarts), Q2 FY26 (quarter ended 30 Sep 2025).** Consolidated revenue rose 15% YoY to **₹16,676 crore**, EBITDA was **₹1,230 crore** (margin 7.3% vs 7.6% a year earlier) and the chain had **432 stores**, after adding 8 in the quarter. That is roughly ₹38–39 crore of revenue per store per quarter, a useful anchor for any store-inventory or store-trucking estimate. ([Torus Digital](https://www.torusdigital.com/toruscope/quarterly-results/avenue-supermarts-q2-fy26-results-dmarts-profit-rises-4-yoy-revenue-up-15/))
> 
> **Eternal (Zomato + Blinkit), Q2 FY26 (reported Oct 2025).** Revenue was **₹13,590 crore (+183% YoY)**, of which Blinkit contributed **₹9,891 crore**; about **80% of Blinkit's order value now comes from inventory it owns** (a shift from marketplace to inventory-led). Profit after tax was only ₹65 crore and adjusted EBITDA margin 1.75%. The dark-store network is a node-and-arc operation where every guesstimate on orders per rider or per store matters. ([INDmoney](https://www.indmoney.com/blog/stocks/eternal-zomato-q2-results))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. How many trucks cross Mumbai-Pune highway daily?
> 🔴 Tier 1 · _Tracker hint:_ FMCG + industrial goods for ~25M pop Pune; daily consumption estimate → truck capacity 10 tons → ~8,000-10,000 trucks

### Definition
This is a **flow (demand-driven) guesstimate**: estimate the tonnage that must move along a corridor, then divide by truck payload.

$$\text{Trucks/day} = \frac{\text{Tonnes/day on corridor}}{\text{Payload per truck} \times \text{Load factor}}$$

Structure: (1) define the catchment (Pune metro and its industrial belt such as Chakan and Ranjangaon); (2) estimate goods consumed per person per day (food, FMCG, fuel, building materials, industrial inputs); (3) apply the **share that arrives from the Mumbai side** (port, import DCs, FMCG national DCs); (4) add **outbound** flows (auto parts, exports to JNPT); (5) divide by payload, then add empty or part-loaded return trips because a crossing is a crossing whether loaded or not. Always state the direction convention (both directions, 24 hours).

### Example
Assume catchment 8M people × 5 kg/day (all goods incl. industry) = 40,000 t/day. Say 25% comes via the Mumbai side = 10,000 t inbound and a similar 10,000 t outbound = 20,000 t/day. At 10 t per truck, loaded trips = 2,000/day. Add ~25% empty or part-loaded crossings: ≈ **2,500 trucks/day**.
The tracker's 8,000–10,000 comes from a ~25M catchment: 2,500 × 25/8 ≈ 7,800. The two answers differ only in the catchment assumption, which is exactly what you should say aloud. Cross-check against toll-plaza counts (I have not verified a published figure).

### In the news
See news box. D-Mart's 432 stores and Blinkit's inventory-led network are the demand end of precisely these truck flows; more dense retail points means more, smaller replenishment trips.

### Interview angle
> [!question] How it is asked
> "Estimate the number of trucks crossing the Mumbai-Pune highway every day." Often inside a logistics-consulting or road-freight case.

> [!tip] Strong answer includes
> - Clear catchment definition and a two-way, 24-hour convention
> - Tonnes first, trucks second (payload, load factor, empty returns)
> - Mention of segments: FMCG, perishables, industrial, construction
> - A sanity check (toll data, vehicles per lane per hour) and honest range

---

## 2. Warehouse size needed for Amazon India fulfillment
> 🔴 Tier 1 · _Tracker hint:_ Orders/day × avg package size × dwell time × buffer → sq ft; consider pick face vs storage

### Definition
Warehouse space is driven by **inventory on hand** (cube) and **throughput** (process areas). Steps:

$$\text{Units in stock} = \text{Units/day} \times \text{Days on hand}$$
$$\text{Storage area} = \frac{\text{Units} \times \text{Volume/unit}}{\text{Rack height} \times \text{Cube utilisation}}$$

Then add non-storage area (receiving, sortation, pack stations, returns, docks, aisles), typically as much again as storage. Separate **reserve storage** (dense racking) from **pick faces** (forward area, low density, high touch) as pick faces are space-hungry for fast movers. Note the dwell time is the lever: fast movers 7–10 days, long tail 60+ days.

### Example
Assume (illustrative, not company data): 1M orders/day nationally × 1.5 units = 1.5M units/day; 20 days on hand = 30M units; 5 litres (0.005 m³) per unit = 150,000 m³. Rack height 6 m, cube utilisation 30%: 150,000 / (6 × 0.3) = 83,333 m² ≈ 9 lakh sq ft (×10.764). Double for process space: **~18 lakh sq ft network-wide**, to be split across dozens of fulfilment centres by region.

### In the news
See news box. Eternal's shift to owning ~80% of Blinkit's order value as inventory means it must carry stock in dark stores, which is the same dwell-time-times-volume maths at small scale.

### Interview angle
> [!question] How it is asked
> "How much warehouse space does Amazon need in India?" or "How would you size a new fulfilment centre?"

> [!tip] Strong answer includes
> - Inventory-driven vs throughput-driven sizing, and why both are checked
> - Days on hand as the key lever, split by ABC class
> - Cube utilisation and rack height instead of naive floor-area logic
> - Network view: many regional FCs, not one giant warehouse (see [[001 SCM Introduction & Fundamentals]] on network design)

---

## 3. Inventory for a D-Mart store
> 🔴 Tier 1 · _Tracker hint:_ ~5,000 SKUs; avg 5 units each; avg price ₹200 → ₹50L in inventory; turnover 25x/year

### Definition
Store inventory value = **SKUs × average units on hand per SKU × cost per unit**. Cross-check with the turnover identity:

$$\text{Inventory} = \frac{\text{COGS per year}}{\text{Inventory turns}}$$

Two independent routes (bottom-up from shelves, top-down from sales) should roughly agree. State whether you value at cost (correct for inventory) or at retail price (overstates by the margin).

### Example
Tracker route: 5,000 × 5 × ₹200 = ₹50,00,000 = **₹50 lakh**. That fits a small-format store.
Top-down for a real D-Mart: revenue per store ≈ ₹16,676 cr / 432 stores × 4 ≈ **₹154 crore/year**. At an assumed ~85% COGS = ₹131 crore; at 25 turns the inventory is ≈ **₹5 crore**. The gap (10x) tells you a D-Mart box stocks far more SKUs and depth (typically >10,000 SKUs), so your SKU count assumption was too low. This reconciliation is the real insight.

### In the news
See news box. Use the Q2 FY26 revenue and store count as your sanity anchor, and mention the margin squeeze (EBITDA 7.3% vs 7.6%) as a reason inventory efficiency matters.

### Interview angle
> [!question] How it is asked
> "Estimate the value of inventory in a D-Mart store." Often followed by "how would you reduce it?"

> [!tip] Strong answer includes
> - Bottom-up and top-down estimates, then reconciliation
> - Value at cost, not selling price
> - Category mix: grocery turns faster than apparel/general merchandise
> - Link to turns, days of inventory and working capital

---

## 4. Number of delivery executives Zomato has in Mumbai
> 🔴 Tier 1 · _Tracker hint:_ ~1.5L orders/day in Mumbai; avg delivery time 30 min; 8 hr shift = 16 deliveries/person → ~9,400 executives

### Definition
A **capacity-matching** guesstimate: riders needed = orders ÷ orders one rider can do.

$$\text{Riders} = \frac{\text{Orders/day}}{\text{Orders per rider per day}}, \quad \text{Orders/rider} = \frac{\text{Productive hours}}{\text{Cycle time per order}}$$

Refinements: demand is **peaky** (lunch and dinner, about 60% of orders in 4 hours), riders **batch** orders, a rider has idle time between orders, and many are part-time. So estimate to peak, then adjust for shift pattern.

### Example
Tracker: 8 h shift / 0.5 h per order = 16 orders; 150,000 / 16 = **9,375 ≈ 9,400 riders** (if each rider works every day).
Peak check: 60% of orders in 4 hours = 90,000 orders; one rider does 8 per 4 hours (cycle 30 min) → 11,250 riders simultaneously. Part-timers and weekly offs mean the registered pool is higher than the 9,400 estimate. Mention both.

### In the news
See news box. Eternal is investing heavily in Blinkit's fleet and dark stores; quick commerce has short cycle times (far below 30 minutes), so each rider completes more orders per hour, but it needs dense rider supply near every dark store.

### Interview angle
> [!question] How it is asked
> "How many delivery partners does Zomato or Swiggy have in Bengaluru or Mumbai?"

> [!tip] Strong answer includes
> - Orders/day first, then orders per rider
> - Peak-hour thinking, not just daily averages
> - Distinction between active, registered and simultaneous riders
> - Sanity check against known company disclosures

---

## 5. How many cold storage facilities in India?
> 🔴 Tier 1 · _Tracker hint:_ Horticultural output ~300M tons; 10% needs cold storage; avg facility 5,000 tons → ~6,000 facilities (actual ~8,000)

### Definition
A **supply-side capacity** guesstimate: total tonnage requiring storage ÷ capacity per facility. Segment by product: potato (the biggest user), fruits and vegetables, dairy, meat and fish, pharma and vaccines, ready-to-eat. Adjust for **turnover** (potato stores fill once a season; a dairy chilling store turns weekly) and for geography (Uttar Pradesh, West Bengal, Gujarat, Punjab dominate).

$$\text{Facilities} = \frac{\text{Output} \times \text{Share needing cold chain}}{\text{Avg capacity} \times \text{Annual turns}}$$

### Example
300M t × 10% = 30M t; ÷ 5,000 t = **6,000 facilities**. With one fill per year that is the answer; the tracker notes the reported figure is about 8,000 (not verified here), implying either a higher share needing storage or smaller average capacity. Say the gap is within a 1.3x error band and explain which assumption to flex.

### In the news
See news box. Blinkit and D-Mart style high-frequency retail increases demand for temperature-controlled last-mile, not only bulk potato stores.

### Interview angle
> [!question] How it is asked
> "How many cold storage units are there in India?" or "Is there a gap in cold chain capacity?"

> [!tip] Strong answer includes
> - Segmentation by product and by storage type (bulk vs distribution vs reefer)
> - Turnover assumption stated
> - Reconciliation to a known figure
> - A so-what: wastage and the investment opportunity

---

## 6. Fleet size for Reliance Retail supply chain
> 🔴 Tier 1 · _Tracker hint:_ ~2,000 stores; avg 5 trucks/store/day; shared routes → estimate 3,000-4,000 trucks

### Definition
Fleet size comes from **total tonne-trips ÷ trips per truck per day**, then divided by availability.

$$\text{Fleet} = \frac{\text{Truck-trips/day}}{\text{Trips per truck/day}\times \text{Availability}}$$

Split into **primary** (vendor to DC) and **secondary** (DC to store) legs. Use milk-run routes (one truck serving 3 to 4 stores) to avoid the naive "5 trucks per store" overcount. Note that the 2,000-store figure is the tracker's problem input; Reliance Retail's actual store count is far larger, so say the assumption explicitly.

### Example
2,000 stores × 6 t/day inbound = 12,000 t/day. Secondary: 8 t effective load per truck, one dispatch/day → 1,500 trucks. Primary leg roughly equal tonnage → 1,500. Total 3,000 truck-days; at 85% availability: 3,000 / 0.85 ≈ **3,500 trucks**, inside the 3,000–4,000 band. Note that Reliance would mostly hire from 3PLs, so "fleet" means contracted capacity.

### In the news
See news box. Dense dark-store and big-box growth increase delivery frequency; the more stores, the more milk-run optimisation matters.

### Interview angle
> [!question] How it is asked
> "How many trucks does a large retailer need to supply its stores?"

> [!tip] Strong answer includes
> - Tonnage-based logic, not trucks per store
> - Primary vs secondary legs and milk runs
> - Availability and own-vs-hired fleet
> - Cost link: ₹/tonne-km and fill rate

---

## 7. Lead time estimation for imported goods
> 🔴 Tier 1 · _Tracker hint:_ Supplier lead time + transit (sea 30-45 days) + customs (5-7 days) + last mile = 60-75 days total

### Definition
Lead time is the **sum of sequential stages** (not the maximum), each with its own variability:

$$LT = T_{\text{production}} + T_{\text{origin handling}} + T_{\text{sea}} + T_{\text{customs}} + T_{\text{inland}}$$

Estimate the mean for each stage and a **standard deviation**, because safety stock depends on variability: for independent stages $\sigma_{LT} = \sqrt{\sum \sigma_i^2}$. Sea transit is the largest but customs and port dwell cause most of the variance. Distinguish **lead time** (order to receipt) from **transit time** (departure to arrival).

### Example
Supplier ready 14 days + origin inland and port 4 + sea 35 + customs 6 + inland to DC 5 = **64 days**, inside the 60–75 band. If sea transit swings ±5 days and customs ±3 days, then $\sigma = \sqrt{25+9} \approx 5.8$ days, and a 95% service level needs about 1.65 × 5.8 ≈ 9.6 days of extra cover.

### In the news
See news box. For import-dependent retailers, a longer or less reliable lead time forces higher safety stock, which shows up as the inventory days that D-Mart and Blinkit-style players try to cut.

### Interview angle
> [!question] How it is asked
> "How long does it take for goods to reach India from China, and what does it mean for inventory?"

> [!tip] Strong answer includes
> - Stage-wise build-up, ranges rather than a point
> - Variability and safety stock link
> - Levers: air vs sea, bonded warehouses, advance customs filing
> - Cost of time: pipeline inventory = demand × lead time

---

## 8. Daily production capacity of a mid-size FMCG plant
> 🔴 Tier 1 · _Tracker hint:_ Identify bottleneck line speed (e.g. 500 units/min); available time 20 hrs/day = 600,000 units/day

### Definition
Capacity is set by the **bottleneck** (theory of constraints), not the average machine.

$$\text{Capacity} = \text{Rate}_{\text{bottleneck}} \times \text{Available time}$$
$$\text{Effective output} = \text{Capacity} \times \text{OEE}, \quad OEE = A \times P \times Q$$

where $A$ = availability, $P$ = performance, $Q$ = quality. Plants rarely hit design capacity: changeovers, cleaning, breakdowns and rejects cut output. Scale by number of lines and days per year (about 300 working days).

### Example
500 units/min × 60 × 20 h = **600,000 units/day** (design). With OEE of 75% (e.g. A 90% × P 90% × Q 93% ≈ 75%): **450,000 units/day**. Annual: 450,000 × 300 = 135M units. For biscuits at 50 g, that is about 6,750 tonnes/year (check: 135M × 0.05 kg = 6.75M kg).

### In the news
See news box. As D-Mart grows (432 stores), FMCG plants supplying it face rising volumes; the capacity question becomes "can the bottleneck line keep pace?"

### Interview angle
> [!question] How it is asked
> "Estimate production capacity of a Parle or Britannia plant." Or: "Where would you add capacity?"

> [!tip] Strong answer includes
> - Bottleneck identification, stated rate and hours
> - OEE to move from design to effective capacity
> - Changeovers and SKU mix
> - Utilisation implications for debottlenecking vs new line

---

## 9. ⭐ Advanced: Little's Law and utilisation for capacity guesstimates
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Little's Law**: $L = \lambda W$, where $L$ = average items in the system, $\lambda$ = arrival (throughput) rate, $W$ = average time in the system. It holds for any stable system and lets you size queues, pickers or riders without simulating. Staffing rule: required servers = $\lambda \times \text{service time} / \text{target utilisation}$. Queues explode as utilisation approaches 100%, so plan at 80–85%.

### Example
A dark store receives 1,000 orders/hour; each is in the store (pick-pack) for 6 minutes (0.1 h). Orders in process $L = 1000 \times 0.1 = 100$. A picker handles one order per 4 min = 15/hour; 1000/15 = 66.7 pickers at 100% utilisation; at 85%: 66.7 / 0.85 ≈ **79 pickers**.

### In the news
See news box. Blinkit-style stores live on this maths: promise time $W$ is fixed at about 10 minutes, so the only levers are throughput and headcount.

### Interview angle
> [!question] How it is asked
> "A warehouse ships 20,000 orders a day, each spends 8 hours in the building. How many orders are in the building at any time?" (answer: 20,000/24 × 8 ≈ 6,667)

> [!tip] Strong answer includes
> - $L = \lambda W$ with consistent units
> - Target utilisation (not 100%)
> - Peak vs average arrival
> - Use as a cross-check in guesstimates

---

## 10. ⭐ Advanced: Top-down vs bottom-up triangulation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Top-down** starts from a large known base (population, households, GDP) and applies filters. **Bottom-up** builds from unit capacity (one rider, one store, one truck) and multiplies. **Triangulation** runs both and compares: if they agree within about 30%, confidence is high; if not, find the assumption that diverges. Consultants prefer this because it exposes a bad assumption early and shows rigour.

### Example
Zomato orders in Mumbai. Bottom-up from the tracker: 9,400 riders × 16 orders = about 1.5L orders/day. Top-down: ~5M households × 8% ordering on a given day = 4L orders; Zomato share ~40% = **1.6L orders/day**. The two agree within ~7%, so use ~1.5L as the working number.

### In the news
See news box. The Eternal results give you reported scale (order value, revenue) to benchmark a third, company-disclosed route.

### Interview angle
> [!question] How it is asked
> "Can you check that another way?" (typical interviewer nudge after your first answer)

> [!tip] Strong answer includes
> - A genuinely independent second route (different assumptions)
> - A tolerance for agreement, and a reconciliation
> - Not changing the first answer just to match
> - Stating which route you trust more and why

---
## 🔗 Go deeper: expansion notes
- [[223 Logistics, Manufacturing & Industry Data Points - India|Logistics, Manufacturing & Industry Data Points - India]]
