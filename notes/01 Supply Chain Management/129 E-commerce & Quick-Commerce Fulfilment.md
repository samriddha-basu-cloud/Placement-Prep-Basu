---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "E-commerce & Quick-Commerce Fulfilment"
tier: Tier 1
roles: Operations / PM / Consulting
status: complete
subtopics: 14
---
# E-commerce & Quick-Commerce Fulfilment

⬅ [[128 Warehouse Labour, WES-WCS & Yard Management]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[130 FMCG & Retail Distribution - India Route-to-Market]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / PM / Consulting

## Sub-topics in this note
1. [[#1. E-commerce Fulfilment Models: Inventory-Led, Marketplace and Hybrid]]
2. [[#2. Platform-Fulfilled vs Seller-Fulfilled (FBA-Type Programmes)]]
3. [[#3. Fulfilment Centre Flow and Network Structure]]
4. [[#4. Sortation and Hub Operations]]
5. [[#5. Order Promising and Delivery SLAs]]
6. [[#6. COD, RTO Economics and Prepaid Nudges]]
7. [[#7. Returns and Reverse Logistics in E-commerce]]
8. [[#8. Dark-Store Model for Quick Commerce]]
9. [[#9. Unit Economics per Order and Dark-Store Break-Even]]
10. [[#10. Assortment and Replenishment for 10-Minute Delivery]]
11. [[#11. Rider Logistics and Last-Mile Economics]]
12. [[#12. ONDC and Open-Network Commerce]]
13. [[#13. Peak Sale Events and Capacity Planning]]
14. [[#14. ⭐ Advanced: Dark-Store Network Design and Cannibalisation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Quick commerce becomes a core retail channel
> **Q-commerce already dominates online grocery (Bain, 2024 data).** Bain & Company's India online-shopping report says that in 2024 more than **two-thirds of e-grocery orders** and about **one-tenth of e-retail spend** happened on quick-commerce platforms; it projects growth above **40% a year through 2030**, notes that **15-20% of quick-commerce GMV** now comes from non-grocery items (general merchandise, electronics, phones, apparel), and lists new entrants such as Flipkart Minutes, Myntra's M-now, BigBasket's BB Now and Amazon's quick offering. ([Bain & Company](https://www.bain.com/insights/how-india-shops-online-2025/))
>
> **Market-size and reach data points (IBEF, Wikipedia; treat as indicative).** IBEF's e-commerce page cites a quick-commerce market of **US$7-8 billion in FY25**, forecast at **US$65-70 billion by 2030**; its FMCG page says quick commerce is **70-75% of e-grocery orders**. Wikipedia reports Blinkit in **153 cities (Mar 2025)** and Blinkit's transaction value overtaking Zomato's core food delivery (Jul 2025); Swiggy Instamart in **127 cities (Jul 2025)**; and Zepto raising **US$450 million at a US$7 billion valuation (Oct 2025)**. ([IBEF e-commerce](https://www.ibef.org/industry/ecommerce), [IBEF FMCG](https://www.ibef.org/industry/fmcg), [Wikipedia: Blinkit](https://en.wikipedia.org/wiki/Blinkit), [Wikipedia: Swiggy](https://en.wikipedia.org/wiki/Swiggy), [Wikipedia: Zepto](https://en.wikipedia.org/wiki/Zepto_(company)))
>
> **ONDC scale-up (2022-Oct 2024).** The Open Network for Digital Commerce piloted in five cities on 29 Apr 2022 and, per Wikipedia, reached about **14 million monthly transactions in Oct 2024** (including about 8.4 million non-mobility orders) and about 370,000 active vendors across 800+ cities by May 2024. ([Wikipedia: ONDC](https://en.wikipedia.org/wiki/Open_Network_for_Digital_Commerce))
>
> Sub-topics that say **"See news box"** reuse these items. Private-company metrics change every quarter; confirm the latest shareholder letters before quoting figures in an interview.

---
## 1. E-commerce Fulfilment Models: Inventory-Led, Marketplace and Hybrid
> 🔴 Tier 1 · _Key points:_ Inventory model vs marketplace, who owns stock, FDI rules, control vs asset-light

### Definition
- **Inventory-led (first-party/1P):** the platform buys stock, owns it, sets price and fulfils (Amazon's own retail arm, and quick-commerce dark stores that buy and own stock). Control over assortment, availability and experience; high working capital and obsolescence risk.
- **Marketplace (3P):** independent sellers list and own inventory; the platform provides traffic, payments, logistics and tools and earns **commission, fixed fees, shipping fees and ad income**. Asset-light, wide assortment, less control over quality.
- **Hybrid:** a mix, with the platform fulfilling for sellers (see sub-topic 2) and running its own 1P category.

Regulatory context in India: **100% FDI is permitted in the marketplace model and in B2B e-commerce, but not in inventory-based B2C e-commerce by foreign-owned firms** (IBEF notes the FDI position); marketplace rules also limit the platform's control over sellers (for example, restrictions on sellers in which the platform has equity and on concentration of sales from one seller; check current policy text). Domestic-owned platforms may hold inventory. These constraints shaped the Indian structure of "marketplace plus affiliated logistics".

| Dimension | 1P inventory | 3P marketplace |
|---|---|---|
| Working capital | Platform | Seller |
| Assortment | Curated, narrower | Very wide |
| Quality control | High | Variable |
| Margin source | Trading margin plus ads | Commission plus fees plus ads |
| Fulfilment control | Full | Via platform services or seller |

### Example
A platform sells 10 lakh units a month at an average price of ₹500. As 1P with 22% gross margin, revenue is ₹50 crore and gross profit ₹11 crore, but it carries 30 days of stock at cost (₹50 crore x 0.78 = ₹39 crore) at, say, 11% p.a. cost of capital, which is **₹0.36 crore a month of carrying cost**. As 3P with a 12% blended take rate on ₹50 crore of GMV, revenue is ₹6 crore with no inventory cost, but the platform now depends on sellers' stock accuracy and packing quality.

### In the news
See news box. Quick commerce in India is largely inventory-led in dark stores (Bain describes a 30-minute-or-less promise moving to under 15 minutes for select products), which puts working capital and wastage squarely on the platform.

### Interview angle
> [!question] How it is asked
> "Should a new D2C-adjacent platform go inventory-led or marketplace? What are the supply-chain implications?"

> [!tip] Strong answer includes
> - Compares control, capital, assortment and regulation (FDI)
> - Connects the model to fulfilment: 1P means demand forecasting and replenishment, 3P means seller onboarding and quality
> - Mentions hybrid and a staged approach
> - Quantifies working capital or take-rate economics

---
## 2. Platform-Fulfilled vs Seller-Fulfilled (FBA-Type Programmes)
> 🔴 Tier 1 · _Key points:_ FBA-type, seller-fulfilled, easy-ship, fee structure, storage

### Definition
- **Platform-fulfilled (FBA-type, e.g., Fulfilled by Amazon, Flipkart Smart Fulfilment/Assured):** sellers send stock to the platform's fulfilment centres (FCs); the platform stores, picks, packs, ships, handles customer service and often returns. Benefits: faster delivery promise, a fulfilment badge, better conversion; costs: inbound shipping, storage fees (including long-term storage penalty), pick-pack-ship fees, removal and return fees.
- **Seller-fulfilled:** the seller ships from its own warehouse using its courier partners; flexible, but delivery promise and ratings depend on the seller.
- **Hybrid (seller flex, easy-ship style):** the seller stores, the platform's logistics partner picks up and delivers.

Seller decision: compare **landed fulfilment cost per order** and **conversion uplift** across the options.

$$\text{Cost per order} = \text{Inbound} + \text{Storage} + \text{Pick-pack} + \text{Outbound shipping} + \text{Returns allowance}$$

### Example
A seller with ₹800 AOV and 5,000 orders per month. Self-fulfilled: packing and labour ₹28, courier ₹62, returns allowance ₹16 = ₹106 per order, with a 4-day average delivery. Platform-fulfilled: pick-pack ₹30, shipping ₹55, storage and inbound ₹9, returns ₹14 = ₹108 per order, but the fulfilment badge lifts conversion 15% and cuts delivery to 2 days. If the seller's contribution margin before fulfilment is ₹260 per order, then self-fulfilled yields ₹154 x 5,000 = ₹7.7 lakh. Platform-fulfilled yields ₹152 x 5,750 orders (15% higher volume) = **₹8.74 lakh**, which is 13.5% higher despite a marginally higher cost per order. The decision therefore turns on conversion and service level, not only unit cost.

### In the news
See news box. As platforms add quick-commerce channels for non-grocery (15-20% of Q-commerce GMV per Bain), sellers face a new fulfilment option: dark-store inventory with 10-30 minute promises.

### Interview angle
> [!question] How it is asked
> "A mid-size seller asks whether to join the platform's fulfilment programme. What would you advise?"

> [!tip] Strong answer includes
> - A cost-per-order comparison plus conversion and delivery-speed uplift
> - Inventory placement risk (stock stuck in FCs, long-term storage fees)
> - Control and customer data considerations; multi-channel inventory
> - Recommends a pilot on the fastest-moving SKUs

---
## 3. Fulfilment Centre Flow and Network Structure
> 🔴 Tier 1 · _Key points:_ FC, mother hub, sort centre, delivery hub, last mile

### Definition
E-commerce networks have four layers: **supplier/seller → fulfilment centre (FC) or warehouse → sortation centre/hub → delivery hub (last-mile station) → customer**, with reverse flows. Inside a typical FC:

**Inbound** (appointment, receipt, QC) → **put-away** (random/chaotic storage with barcodes, since e-commerce inventory is mixed) → **pick** (batch, zone, goods-to-person) → **pack** (right-sized boxes, label) → **sort by destination** → **dispatch** by line-haul truck.

Network design choices: number and location of FCs (balance transport and inventory; see [[113 Network Design & Facility Location Modelling]]), regional FCs versus a central FC, **inventory placement** (fast movers deep and forward, slow movers central), and zoning for fragile/hazmat/large items. Network KPIs: order-to-ship time, FC cost per order, inventory accuracy, **fill rate** and **first-attempt delivery rate**. See [[010 Warehouse Management]] and [[127 Warehouse Engineering - Racking, Sizing & Material Handling]].

**Chaotic (random) storage** puts items wherever space is available, with the WMS tracking location; it raises space use but needs excellent scanning discipline.

### Example
A national e-commerce firm serves eastern India from a single FC in Bhiwandi (Maharashtra), roughly 1,900 km away, with a 5-day average delivery. A regional FC in Kolkata holding the top 3,000 SKUs would serve about 70% of the region's 40,000 daily orders, or 28,000 orders, cutting line-haul to about 150 km and delivery to 2 days. At a transport saving of ₹14 per order (assumed) the saving is 28,000 x 14 = ₹3.92 lakh a day, about **₹1.18 crore a month**. The extra inventory of ₹6 crore at 11% p.a. costs about **₹0.055 crore a month**. The net is roughly **₹1.1 crore a month**, before counting the conversion benefit of a faster promise and the cost of running a second site (rent, staff) which must be subtracted.

```python
orders, save, extra_inv = 40000*0.70, 14, 6e7
print(orders*save*30/1e7, extra_inv*0.11/12/1e7)  # 1.18 crore saving vs 0.055 crore carrying, per month
```

### In the news
See news box. The shift from a few mega-FCs to many nearby nodes (dark stores for the 10-30 minute segment) is the structural change in Indian e-commerce networks.

### Interview angle
> [!question] How it is asked
> "A marketplace's east-India deliveries take 5 days. Redesign the network."

> [!tip] Strong answer includes
> - Diagnoses where the days are lost (FC dwell, line-haul, hub, last mile)
> - Proposes forward inventory for fast movers; quantifies transport saving vs inventory cost
> - Mentions sortation hubs and surface-to-air mix for premium promises
> - Notes service-level segmentation (express vs economy)

---
## 4. Sortation and Hub Operations
> 🔴 Tier 1 · _Key points:_ Sort centre, cut-offs, line-haul, hub-and-spoke, sorter types

### Definition
**Sortation** groups parcels by destination pincode or route. Levels: **FC sort** (to destination hub), **mother hub/gateway** (to regional hubs), **delivery centre sort** (to rider/route). Methods: **manual sort with pigeon-holes**, **cross-belt, tilt-tray and sliding-shoe sorters**, **put-to-light walls**, and **robotic sorters**. A hub-and-spoke or a **mesh** of hubs reduces the number of lanes: with $n$ origins and $n$ destinations, direct lanes number $n^2$, while a single hub needs only $2n$.

$$\text{Direct lanes} = n(n-1),\qquad \text{Hub-and-spoke lanes} = 2n$$

Operating levers: **truck cut-off times** (the last time a parcel can enter a sort and still make the line-haul), **sorter capacity** (items per hour), **load factor** of line-haul trucks (consolidated by lane), and **mode choice** (surface for economy, air for express metro-to-metro; rail in specific lanes).

### Example
With 20 cities, direct lanes = 20 x 19 = 380; a single hub needs 40 lanes, but adds distance (a Pune-Mumbai parcel routed via Delhi is absurd). So networks use regional hubs: 4 regional hubs with 5 cities each gives 20 x 2 spokes (40) + 12 hub-to-hub lanes = 52 lanes. A sorter handling 9,000 items per hour (illustrative) runs 16 hours a day = 144,000 parcels; a hub needing 500,000 a day in peak would require 3.5 sorters or a mix of manual and automatic sort, which is why peak planning is central.

### In the news
See news box. As Q-commerce expands into non-grocery items, hubs must support multiple promise tiers (10 minute, same day, next day) at once.

### Interview angle
> [!question] How it is asked
> "Why do e-commerce networks use hubs rather than shipping direct from FC to each city?"

> [!tip] Strong answer includes
> - Lane count maths, consolidation and load factor
> - Trade-off: extra handling and transit time vs cost
> - Cut-off timings and the sorter capacity constraint
> - Mention of regional hubs and air/surface mix

---
## 5. Order Promising and Delivery SLAs
> 🔴 Tier 1 · _Key points:_ Promise date, ATP, lane SLA, on-time, service-level maths

### Definition
**Order promising** commits a delivery date or time when the customer checks out. The promise must reflect **stock availability (available-to-promise, [[119 Supply Planning, DRP & Available-to-Promise]])**, **FC processing time**, **cut-off**, **carrier transit time distribution by lane** and **capacity**. A good promise is a **service-level choice**: set the promised days at a chosen percentile of the lead-time distribution.

$$\text{Promise} = \text{Cut-off handling} + \mu_T + z\,\sigma_T$$

where $\mu_T$ and $\sigma_T$ are the mean and standard deviation of end-to-end transit (days) and $z$ is the service factor (1.28 for 90%, 1.645 for 95%). KPIs: **on-time delivery (OTD)**, **first-attempt delivery rate (FADR)**, **order cycle time**, **cancellation rate** (stock-outs after the order), **NDR** (non-delivery reports), and **cost of promise** (speed costs more). Customer metrics: conversion and repeat rate by promise tier.

### Example
A lane has mean transit 3.0 days and standard deviation 0.8 days. For a 90% on-time promise: 3.0 + 1.28 x 0.8 = **4.0 days**. For 95%: 3.0 + 1.645 x 0.8 = **4.3 days**, so promise 5 days (about 99% on time) or 4 days (about 90%). Suppose 1 lakh orders a day and each late delivery costs ₹60 in support and goodwill. The 4-day promise has about 10% late orders: 10,000 x ₹60 = **₹6 lakh a day**; the 5-day promise has about 1% late: **₹0.6 lakh a day**. The 5-day promise saves ₹5.4 lakh a day in service cost but may reduce conversion, so the right promise is found by testing the conversion loss against that saving.

### In the news
See news box. Q-commerce reset expectations: Bain describes the promise moving from 30 minutes toward 15 minutes for select products and one hour for a wider assortment.

### Interview angle
> [!question] How it is asked
> "Should we promise 2-day delivery everywhere? How do you decide on delivery SLAs?"

> [!tip] Strong answer includes
> - Lane-wise distributions, percentile-based promise and cost of speed
> - Segmentation by customer and product (Prime-type members, high AOV)
> - On-time vs conversion trade-off; A/B test
> - Linking to inventory placement and ATP

---
## 6. COD, RTO Economics and Prepaid Nudges
> 🔴 Tier 1 · _Key points:_ COD, RTO rate, forward and reverse shipping, prepaid incentives

### Definition
**Cash on delivery (COD)** is common in Indian e-commerce because of trust and payment access, but it brings higher **RTO (return to origin)**: shipments that are refused, not available or undeliverable and go back to the seller. An RTO order incurs **forward freight, return freight, packaging and handling, and possible damage or resale loss**, and earns nothing. COD also adds **cash handling fees and remittance delay**.

Expected contribution per order (delivered share $1-r$):

$$E = (1-r)\,(GM - F - P - C) - r\,(F + R + P)$$

with $GM$ gross margin per order, $F$ forward shipping, $R$ return shipping, $P$ packaging, $C$ COD fee, and $r$ the RTO rate. RTO levers: **pincode serviceability and risk scoring**, **address verification and confirmation calls/WhatsApp**, **prepaid incentives**, **COD fees or limits on high-risk orders**, **NDR management with re-attempts** and **better delivery-slot selection**.

### Example
Order value ₹1,200, gross margin 30% = ₹360; forward shipping ₹70, return ₹60, packaging ₹15, COD fee ₹30 (assumed figures). With **COD at 25% RTO** (assumed): E = 0.75 x (360 − 70 − 15 − 30) − 0.25 x (70 + 60 + 15) = 0.75 x 245 − 0.25 x 145 = 183.8 − 36.3 = **₹147.5**. **Prepaid at 8% RTO**: 0.92 x (360 − 70 − 15) − 0.08 x 145 = 253 − 11.6 = **₹241.4**. For a 60:40 COD:prepaid mix the blended contribution is **₹185.1**. Shifting 20 points of the mix to prepaid (40:60) lifts it to **₹203.8**, **+₹18.8 per order**; at 1 lakh orders per day that is about **₹5.6 crore a month**. Break-even: a COD order loses money once RTO exceeds 245/(245+145) = **62.8%**, but one RTO erases the profit of 0.59 delivered COD orders, so even moderate RTO matters.

### In the news
See news box. As UPI-enabled payments penetrate, quick-commerce platforms run largely on prepaid orders at the door, a structural advantage over multi-day COD delivery.

### Interview angle
> [!question] How it is asked
> "A D2C brand has 30% RTO on COD orders. What do you do, and how do you size the benefit?"

> [!tip] Strong answer includes
> - The contribution formula with RTO and the cost of a failed order
> - Root causes: address quality, delivery attempts, slow delivery, fake orders, pincode risk
> - Levers: prepaid incentive, order confirmation, risk scoring, NDR re-attempts
> - Quantifies benefit and checks conversion impact of limiting COD

---
## 7. Returns and Reverse Logistics in E-commerce
> 🔴 Tier 1 · _Key points:_ Return rate, reason codes, grading, refurbish/resell, fraud

### Definition
Returns arise from **fit and size (fashion), defects/damage, wrong item, change of mind, and fraud or abuse**. Fashion return rates can be very high compared with electronics or grocery; check category-specific benchmarks. The reverse flow: **return request → pickup (or drop) → inbound at returns centre → inspection and grading (A resale, B refurbish, C liquidation, D scrap) → restock, refurbish, vendor return or liquidate**, plus refund and claims handling. Metrics: **return rate, return cost per unit, time-to-refund, recovery value (% of original price recovered), restock time and fraud rate**. Design levers: better size guides and content, packaging, quality checks before dispatch, partner-courier QC at pickup, return reason analytics and dynamic policies by user risk. See [[135 Reverse Logistics, Remanufacturing & EPR in India]].

### Example
An apparel order of ₹1,500 with 30% margin (₹450). Return rate 25%. Each return costs ₹120 (reverse pickup, handling, repack) and 15% of returned items cannot be resold at full price, with a 40% loss on those: loss = ₹1,500 x 0.15 x 0.40 = ₹90 per returned order. Expected returns cost per order = 0.25 x (120 + 90) = **₹52.5**, and a returned order also forgoes the margin. If the return rate falls to 20% through better size guidance: cost falls to 0.20 x 210 = ₹42, saving ₹10.5 per order, or ₹1.05 crore a month on 10 lakh orders. Recovering more value (resale at full price rising from 85% to 92% of returned units) cuts the ₹90 loss to ₹48.

### In the news
See news box. Quick commerce handles returns differently: perishables are refunded on the spot and non-returnable, while non-grocery categories raise return handling at the dark store.

### Interview angle
> [!question] How it is asked
> "A fashion marketplace has a 30% return rate. How do you reduce the cost without hurting conversion?"

> [!tip] Strong answer includes
> - Splits returns by reason and category to target the largest cause
> - Sizing, content and QC levers; policy by customer risk
> - Reverse-flow redesign: grading, resale channels, vendor chargebacks
> - Quantifies the saving per order and at scale

---
## 8. Dark-Store Model for Quick Commerce
> 🔴 Tier 1 · _Key points:_ Dark store, mother hub, SKU range, catchment, 10-minute promise

### Definition
A **dark store** is a small, picking-only fulfilment node inside a dense neighbourhood, with no walk-in customers. Typical features (indicative; they vary by company and city): roughly **2,000-5,000 sq ft** footprint, **a few thousand to over ten thousand SKUs**, a **catchment radius of about 2-3 km** (so that the ride takes about 5-8 minutes), **pickers organised by zone**, an app that sequences picks to minimise time, chiller/frozen units for dairy and fresh, and **replenishment several times a day** from a larger **mother hub or warehouse**.

A quick-commerce order flows: **order placed → system assigns to the nearest store with stock → pick (target 1.5-3 min) → pack → rider handover → delivery**. The model works only with **density of demand**, **high throughput per sq ft**, and **tight operational control**. Players: Blinkit (Eternal), Zepto, Swiggy Instamart, plus BigBasket (BB Now), Flipkart Minutes and Amazon's quick offering.

Dark-store dynamics differ from traditional retail: the **assortment is limited to what fits and sells**, wastage control for fresh and dairy is central, and **store-level service is measured in minutes**. See [[010 Warehouse Management]] for slotting and picking, [[227 GST & Indirect Tax for Supply Chains]] for GST on stock transfers from mother hubs.

### Example
Catchment radius 2 km gives an area of π x 2² = **12.6 km²**. At 15,000 households per km² (illustrative dense urban figure), that is **188,500 households**. If 8% order monthly (15,080 users) at 2.4 orders a month, volume is **36,191 orders a month, about 1,206 per day**. At the peak hour (assume 12% of the day's orders, about 145 orders) and 2 minutes of picking per order, the store needs 145 x 2 / 60 = **4.8 picker-hours per hour**, so 5-6 pickers at peak, plus packers and a replenishment crew.

### In the news
See news box. Blinkit operated in 153 cities by March 2025, Instamart in 127 cities by July 2025, and Zepto raised US$450 million at a US$7 billion valuation in Oct 2025 (Wikipedia, indicative); the expansion is a dark-store roll-out problem more than a technology problem.

### Interview angle
> [!question] How it is asked
> "How would you decide where to open the next dark store in Bengaluru?"

> [!tip] Strong answer includes
> - Catchment and demand-density analysis: households, income, order history, competitor presence
> - Ride-time based radius rather than distance; cannibalisation of nearby stores
> - Minimum viable orders per day (break-even), rent and real-estate constraints
> - Mother-hub supply and ability to replenish multiple times a day

---
## 9. Unit Economics per Order and Dark-Store Break-Even
> 🔴 Tier 1 · _Key points:_ AOV, take rate, contribution margin, orders per store per day, break-even

### Definition
**Unit economics per order** shows whether each order makes or loses money before central costs:

$$\text{Contribution per order} = \text{AOV}\times\text{Take rate} - \text{Last-mile} - \text{Variable store cost} - \frac{\text{Fixed store cost}}{\text{Orders per month}}$$

where **take rate** is net revenue (margin on goods, commission, advertising, delivery and handling fees, less discounts) as a share of order value (GOV). Other terms: **AOV** (average order value), **GOV/GMV**, **contribution margin (CM)**, **adjusted EBITDA** (after central tech, marketing and corporate costs), and **orders per store per day (OPD)**. Fixed store costs (rent, core staff, utilities, equipment) are spread over OPD, so utilisation is the first driver; AOV and ad income are the second; rider cost per order is the third.

### Example
Illustrative numbers (assumed, not company data): AOV ₹650, take rate 19% = **₹123.5**; rider cost ₹42; variable costs (packaging, payment, wastage) ₹17; store fixed cost ₹12 lakh a month.

| Orders per day | Fixed cost per order | Contribution per order | CM % of AOV |
|---|---|---|---|
| 500 | ₹80.0 | -₹15.5 | -2.4% |
| 800 | ₹50.0 | ₹14.5 | 2.2% |
| 1,000 | ₹40.0 | ₹24.5 | 3.8% |
| 1,200 | ₹33.3 | ₹31.2 | 4.8% |
| 1,500 | ₹26.7 | ₹37.8 | 5.8% |

**Break-even orders per day** = 12,00,000 / (30 x (123.5 − 42 − 17)) = **620**. If central costs (tech, marketing, support) are ₹20 per order, the store needs about **900 orders per day** to cover them; at 1,200 orders, 31.2 − 20 = ₹11.2 per order. Levers: raise AOV (add-on items, larger baskets), ad income and fees, reduce rider cost (batching), reduce wastage and raise OPD by densifying demand (more users per store through assortment and reliability).

```python
aov, take, rider, var, fixed = 650, 0.19, 42, 17, 1_200_000
rev = aov*take
for opd in (500, 800, 1000, 1200, 1500):
    cm = rev - rider - var - fixed/(30*opd)
    print(opd, round(cm,1), round(cm/aov*100,1))
print("break-even OPD", fixed/(30*(rev-rider-var)))
```

### In the news
See news box. IBEF and Bain describe fast growth (above 40% a year to 2030) but the question for each player is store-level contribution; interviewers expect candidates to separate store-level profitability from company-level adjusted EBITDA.

### Interview angle
> [!question] How it is asked
> "Is quick commerce a sustainable business? Walk me through the unit economics of one order and one dark store."

> [!tip] Strong answer includes
> - Per-order build: take rate (margin, ads, fees), rider, packaging and wastage, store cost per order
> - Break-even OPD and the sensitivity to AOV and utilisation
> - Contribution vs adjusted EBITDA (central costs, marketing)
> - Levers: AOV, ads, batching, wastage, private labels, density

---
## 10. Assortment and Replenishment for 10-Minute Delivery
> 🔴 Tier 1 · _Key points:_ SKU range, fast movers, FEFO, min-max, multiple replenishments

### Definition
A dark store has to **win on availability** from a limited range. **Assortment** decisions: core daily needs (milk, bread, eggs, vegetables) for frequency, high-margin categories (personal care, snacks, home care, electronics accessories) for take rate, and long-tail items for a few stores only. Use sales velocity, margin, substitutability and basket affinity; review each store's mix by local preference.

**Replenishment**: periodic review, order-up-to policy per SKU per store with several delivery waves per day from the mother hub: 

$$S = d\,(R + L) + z\,\sigma_d\sqrt{R+L}$$

where $d$ is mean daily demand, $\sigma_d$ the daily standard deviation, $R$ review period and $L$ lead time in days (see [[003 Inventory Management]] and [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]). Perishables use **FEFO** with markdowns and wastage targets; **forecasting at store-SKU-day level** ([[004 Demand Forecasting & Planning]], [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]]) captures weather, events and promotions.

### Example
A SKU sells 12 units a day with a daily standard deviation of 4. With one replenishment a day (R = 1 day) and lead time 0.5 day, $S$ = 12 x 1.5 + 1.65 x 4 x $\sqrt{1.5}$ = 18 + 8.1 = **26.1 units**. With two replenishments a day (R = 0.5 day) and a shorter hub lead time (L = 0.25 day), R + L = 0.75 and S = 12 x 0.75 + 1.65 x 4 x $\sqrt{0.75}$ = 9 + 5.7 = **14.7 units**. Shelf stock falls by 44% for the same availability, which matters when a store has a few thousand SKUs, limited space and perishable stock; but each extra replenishment wave adds transport and handling cost at the mother hub.

### In the news
See news box. As Q-commerce moves into electronics and apparel (15-20% of GMV per Bain), the assortment problem changes from fast-turn perishables to long-tail items with different forecasting needs.

### Interview angle
> [!question] How it is asked
> "A dark store has 8% stock-outs on top 500 items and 4% wastage on fresh. How do you fix both?"

> [!tip] Strong answer includes
> - Splits the problem: forecasting accuracy, replenishment frequency and shelf discipline
> - Applies safety-stock and review-period logic with numbers
> - FEFO, markdown and assortment pruning to cut wastage
> - Considers the trade-off with mother-hub delivery cost

---
## 11. Rider Logistics and Last-Mile Economics
> 🔴 Tier 1 · _Key points:_ Orders per rider-hour, utilisation, batching, payout, gig workforce

### Definition
Last-mile in quick commerce and food/e-commerce uses **gig riders** (two-wheelers, increasingly EVs) assigned by an algorithm. Core metrics: **delivery time**, **orders per rider per hour (OPRH)**, **rider utilisation**, **distance per order**, **batching rate**, **payout per order**, **idle time** and **rider supply by hour**. The trip cycle is wait at store + ride out + handover + ride back:

$$\text{OPRH} = \frac{60}{\text{Cycle time (min)}}\times\text{Utilisation}$$

Levers: **stacked orders** (two close orders on one trip), **smaller catchments**, **faster picking** (shorter wait), **rider slots and incentives for peak hours**, **EV charging** and **safe-driving policies**. Rider welfare and regulation (social security for platform workers in the labour codes, safety expectations) are now part of the cost model. 3PL and courier networks use **route optimisation** for scheduled e-commerce delivery; see [[125 Transportation Management Deep Dive]] and [[009 Logistics & Distribution]].

### Example
Average delivery distance 2.0 km at 18 km/h gives 6.7 minutes each way. Cycle = 2 min wait + 6.7 out + 2 handover + 5.0 return (a shorter return as the rider is often reassigned en route) = **15.7 minutes**, so a fully used rider could do 3.8 orders per hour. At 70% utilisation, OPRH = **2.68**. With a payout of ₹42 per order, the rider earns about **₹113 per hour**. If utilisation is only 50% (low demand), OPRH falls to 1.9 and the platform must pay a minimum guarantee or lose riders; this is why density and slots matter. If a quarter of trips carry two orders, orders per trip rise to 1.25 (+25%); where riders are paid per trip, rider cost per order falls by 20%.

### In the news
See news box. Wikipedia's Blinkit page records the April 2023 delivery-partner strike in Delhi NCR over reduced payouts, a reminder that rider economics are fragile and a reputational risk.

### Interview angle
> [!question] How it is asked
> "Rider cost per order has risen 15% and delivery time is up. What would you check?"

> [!tip] Strong answer includes
> - Splits cycle time into wait, ride, handover and return; finds the bloated step
> - Supply-demand balance by hour and slot; batching potential
> - Payout structure vs productivity, incentives and rider retention
> - Safety, welfare and regulatory implications

---
## 12. ONDC and Open-Network Commerce
> 🔴 Tier 1 · _Key points:_ Unbundled commerce, buyer and seller apps, protocol, logistics interoperability

### Definition
The **Open Network for Digital Commerce (ONDC)** is a government-backed, protocol-based network that unbundles the e-commerce stack so that any **buyer app** can discover products from any **seller app** and use any compliant **logistics provider**, instead of each platform controlling the whole chain. It targets **small retailers and sellers** (reducing dependence on platform fees and algorithms) and **city-level commerce** across food, grocery, mobility and general merchandise. For supply chains this means: (1) **logistics interoperability** with multiple 3PLs in one order flow; (2) **hyperlocal fulfilment** from neighbourhood stores; (3) **standardised catalogues and order states**, but variable service quality.

Constraints: **uneven quality and delivery performance** across sellers and logistics partners, **reconciliation and dispute handling** across parties, thin margins for participants, and the need for discount-funded growth. Compared with platform-led quick commerce, ONDC trades scale economies for openness.

### Example
A kirana store in a Tier-2 city lists 1,500 SKUs on a seller app. A customer places a 10-item order of ₹420. The seller app assigns a hyperlocal delivery partner at ₹35. The kirana earns a retail margin of about 12% (₹50) and a lower platform fee (say 3% = ₹12.6, assumed), so contribution is ₹50.4 − ₹35 − ₹12.6 = **₹2.8**, which leaves almost nothing for packing or returns; the economics work only with batching, a customer-paid delivery fee or larger baskets. This is why density and order batching are central to the open-network model too.

### In the news
See news box. ONDC's Wikipedia page lists about 14 million monthly transactions by Oct 2024 (including 8.4 million non-mobility orders) against the much higher scale of platform quick commerce, showing both the promise and the scale gap. Compare with [[165 Platform & Marketplace Product Strategy]].

### Interview angle
> [!question] How it is asked
> "Will ONDC disrupt Amazon and Flipkart? What are the supply-chain obstacles?"

> [!tip] Strong answer includes
> - Explains unbundling: buyer apps, seller apps, logistics and protocol
> - Obstacles: service quality, reconciliation, density, unit economics, customer habit
> - Where it can win: hyperlocal, mobility, category-specific and B2B niches
> - Offers a measured view with data (volumes vs incumbents)

---
## 13. Peak Sale Events and Capacity Planning
> 🔴 Tier 1 · _Key points:_ Festival peaks, forecast, surge capacity, pre-positioning, war-room

### Definition
Large events (festive sales around Diwali, end-of-season sales and flash sales) create volume spikes of several times normal levels in a few days. Planning cycle: **forecast by SKU-region** (use event history, marketing plan and price-promotion elasticity; see [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]]); **pre-position inventory** (push fast-moving stock to regional FCs and dark stores); **capacity plan** for FC pick-pack, sorters, line-haul and last-mile; **temporary labour and training** ([[128 Warehouse Labour, WES-WCS & Yard Management]]); **carrier capacity commitments**; **order caps and slot-based promises** if capacity is tight; **war-room** with hourly dashboards; **post-peak returns** capacity. Risks: stock-outs on deals, SLA breaches, carrier collapse, and customer service overload. See [[015 Supply Chain Risk & Resilience]].

### Example
Normal volume 1 lakh orders a day; the sale week averages 3.2 lakh a day with a peak day of 4.5 lakh. FC capacity is 2.0 lakh. Gap at peak = 2.5 lakh orders. Options: temp labour and extra shifts (+0.8 lakh), a pre-built temporary FC (+0.7 lakh), pre-positioned stock in dark stores and regional nodes taking 0.5 lakh, and order throttling on low-priority sellers: 0.5 lakh deferred. If the late deliveries cost ₹60 each and 10% of peak orders slip (45,000 orders), cost = ₹27 lakh for the day, which justifies a ₹10-15 lakh investment in extra capacity. A rule: peak capacity should be set at about the 90-95th percentile of the forecast, with a defined shedding plan above that.

### In the news
See news box. Quick commerce adds a new type of peak: weather and cricket-match spikes and festival gifting, handled at store level with hourly re-forecasting.

### Interview angle
> [!question] How it is asked
> "Plan the supply chain for a 5-day sale where volumes triple."

> [!tip] Strong answer includes
> - Forecast, pre-positioning, capacity by node, temp labour and carrier plan
> - Capacity-constraint logic: where the first bottleneck appears and how to shed or smooth demand
> - War-room metrics and escalation rules
> - Cost of failure versus cost of buffer capacity

---
## 14. ⭐ Advanced: Dark-Store Network Design and Cannibalisation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
City-level dark-store network design is a **facility location problem** with coverage constraints ([[113 Network Design & Facility Location Modelling]]): choose store sites to cover demand within a ride-time limit while keeping each store above its break-even orders per day. Considerations: **demand density by micro-market**, **ride-time isochrones** (not straight-line distance), **cannibalisation** (a new store takes orders from neighbouring stores while raising total share), **rent and availability of real estate**, **store size by SKU range**, **mother-hub location**, and **stage-wise rollout**. A simple p-median or maximal-coverage model can be solved in Python or Excel Solver ([[068 Operations-Specific Python (PuLP, SimPy)]]).

Marginal analysis: opening a new store is worth it if the **incremental orders per day** (new customers served plus higher share) exceed its break-even OPD after cannibalisation.

### Example
Using the earlier unit-economics model (take ₹123.5, rider ₹42, variable ₹17, store fixed ₹12 lakh a month), two existing stores each do 1,100 orders a day, a contribution of ₹28.1 per order, or **₹61,900 a day** in total. A third store opens between them and does 900 orders a day, of which 300 are cannibalised (150 from each neighbour), so incremental demand is 600 orders. The old stores fall to 950 orders (₹22.4 per order) and the new store earns ₹20.1 per order: total contribution = 2 x 950 x 22.4 + 900 x 20.1 = **₹60,600 a day**, which is **₹1,300 a day (₹39,000 a month) lower** despite 600 extra orders, because a third fixed cost is carried. The new store pays off only if it reaches about 930 orders with the same cannibalisation (630 incremental), or if faster delivery lifts frequency and retention. This is why cannibalisation must be modelled before opening stores.

### In the news
See news box. As players expand from metros into 100+ cities (153 for Blinkit, 127 for Instamart per Wikipedia), the quality of site selection and cannibalisation modelling separates profitable expansion from burn.

### Interview angle
> [!question] How it is asked
> "A quick-commerce company wants to double its stores in Mumbai. What should it check first?"

> [!tip] Strong answer includes
> - Demand density and ride-time coverage, existing store utilisation and cannibalisation
> - Break-even OPD and incremental economics of the new store
> - Real estate and mother-hub capacity, rider supply
> - Phased roll-out with clear stop-loss criteria
