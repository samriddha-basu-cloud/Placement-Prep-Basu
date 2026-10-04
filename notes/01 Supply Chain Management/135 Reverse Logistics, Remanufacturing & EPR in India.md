---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Reverse Logistics, Remanufacturing & EPR in India"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Reverse Logistics, Remanufacturing & EPR in India

⬅ [[134 Electronics & Semiconductor Supply Chain]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[136 Supply Chain Finance & Working Capital]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Reverse Flows: Returns, Recalls, End-of-Life]]
2. [[#2. Returns Flow Design, RMA & Grading]]
3. [[#3. The Disposition Decision: Restock, Refurbish, Remanufacture, Recycle, Liquidate]]
4. [[#4. Recovery Value Economics: A Worked Example]]
5. [[#5. Closed-Loop Supply Chains & the Circular Economy]]
6. [[#6. Remanufacturing & Retreading: Auto Parts, Tyres, Electronics]]
7. [[#7. Reverse Logistics Network Design & 3PLs]]
8. [[#8. E-commerce Returns & Returns Fraud]]
9. [[#9. Refurbished Marketplaces & Re-commerce]]
10. [[#10. India's EPR Architecture: E-Waste Rules 2022 & Battery Waste Rules 2022]]
11. [[#11. Plastic Packaging EPR, rPET Mandate & Tyre EPR]]
12. [[#12. Vehicle Scrapping Policy & RVSFs]]
13. [[#13. Reverse Logistics KPIs & Cost Accounting]]
14. [[#14. ⭐ Advanced: EPR Make-vs-Buy and Reverse-Network Modelling]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's waste rules now force companies to run a reverse supply chain
> **E-waste is up 72% in five years (reported December 2024).** Government data given to the Rajya Sabha showed India's e-waste generation rising from 10.14 lakh tonnes in 2019-20 to 17.51 lakh tonnes in 2023-24 (about 72%). The E-Waste (Management) Rules, 2022 came into effect on 1 April 2023, replacing the 2016 Rules. ([Business Standard, 16 December 2024](https://www.business-standard.com/india-news/india-sees-72-rise-in-electrical-electronic-waste-in-5-years-govt-124121601342_1.html))
>
> **Recycled-content mandate for PET packaging (2025-26).** Under the Plastic Waste Management Rules, rigid packaging (including beverage bottles) must contain 30% recycled food-grade PET from 1 April 2025, rising by 10 percentage points a year to 60% by 2028-29. In February 2025 beverage makers (Coca-Cola, PepsiCo, Bisleri, Parle Agro were cited) argued that only five FSSAI-approved plants then met about 15% of demand; by March 2026 FSSAI had authorised 17 r-PET plants adding about 300,000 tonnes of capacity. ([Business Standard, 26 February 2025](https://www.business-standard.com/industry/news/beverage-giants-oppose-india-rpet-bottle-mandate-april-2025-125022600258_1.html), [Business Standard, 16 March 2026](https://www.business-standard.com/industry/news/fssai-grants-authorisation-to-17-r-pet-plants-adds-3-mt-capacity-126031601276_1.html))
>
> **Scrapping infrastructure (August 2024).** The Ministry of Road Transport reported 60+ registered vehicle scrapping facilities (RVSFs) in 17 States/UTs and 75+ automated testing stations in 12; passenger-vehicle buyers get a discount of 1.5% of the ex-showroom price or ₹20,000, whichever is less, on a new car when they scrap an old one within six months. ([PIB, 28 August 2024](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2049367&reg=48&lang=2))
>
> **A formal e-waste recycling market is forming (August 2026).** One market report projects India's e-waste recycling market growing from $1.7 billion (2025) to $3 billion by 2034 (6.34% CAGR), while flagging the large informal sector and high compliance cost for small recyclers. ([Business Standard, 25 August 2026](https://www.business-standard.com/technology/tech-news/india-e-waste-recycling-market-growth-2034-126082500824_1.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Reverse Flows: Returns, Recalls, End-of-Life
> 🟠 Tier 2 · _Key points:_ forward vs reverse, sources of returns, uncertainty, value decay

### Definition
**Reverse logistics** is the movement of goods from the point of consumption back toward the point of origin to recapture value or ensure proper disposal. Sources of reverse flow:
- **Customer returns** (change of mind, wrong size, defective, damaged in transit).
- **Commercial returns** (unsold stock returned by retailers, expiry returns, overstock, seasonal).
- **Warranty and repair returns**.
- **Recalls** (safety or quality).
- **End-of-use / end-of-life** (old phone, battery, tyre, scrapped vehicle).
- **Packaging and reusables** (crates, pallets, gas cylinders, bottles).

Differences from forward logistics: **uncertain timing, quantity and quality**; many-to-one flows; unclear product condition; **value decays quickly** (a returned phone loses value each week it sits); and few systems built for it. Reverse logistics is a **profit and ESG lever**, not just a cost: the Wikipedia overview cites a global reverse logistics market of about $993 billion in 2023, e-commerce return rates near 20% (against 8-10% in-store) and return costs of up to 7% of gross enterprise sales (as a general industry range). See also [[129 E-commerce & Quick-Commerce Fulfilment]] and [[009 Logistics & Distribution]].

### Example
An online fashion seller with ₹100 crore of sales and a 20% return rate processes ₹20 crore worth of returned goods. At ₹250 per returned order (reverse pickup, QC, repack, restock) and an average order of ₹1,500: returns = 100 crore/1,500 × 20% ≈ 133,333 orders; processing cost = 133,333 × 250 = **₹3.33 crore**, plus lost margin on goods that cannot be resold at full price (assume 15% markdown on 30% of returned goods: ₹20 crore × 30% × 15% = **₹0.9 crore**). Total ≈ ₹4.2 crore, or about 4.2% of sales, which is why a small drop in return rate is worth far more than a small drop in freight rate.

### In the news
See news box. The e-waste growth figure and the mandatory recycling targets are the end-of-life side of the same reverse flow.

### Interview angle
> [!question] How it is asked
> "How is reverse logistics different from forward logistics and why do companies neglect it?"

> [!tip] Strong answer includes
> - Sources of reverse flow and the uncertainty in timing, quantity and quality
> - Value decay with time and handling steps
> - Cost size (processing, markdown) vs the value recoverable
> - Strategic role: customer experience, margin recovery, compliance and sustainability

---
## 2. Returns Flow Design, RMA & Grading
> 🟠 Tier 2 · _Key points:_ RMA, returns centre, gatekeeping, grading A/B/C/D, speed to disposition

### Definition
A returns process: **authorisation (RMA)** → **collection** (reverse pickup, drop-off, courier or store) → **receiving and inspection** → **grading** → **disposition** → **financial settlement** (refund, credit note, vendor chargeback). Design principles:
- **Gatekeeping**: screen at the start (return reason, warranty, eligibility window, serial or IMEI check) to block ineligible returns.
- **Centralised returns centre** for expertise and scale vs **decentralised** handling for speed.
- **Grading**: standard criteria (functional and cosmetic) with photo/scan evidence; typical grades: **A** (like new/open box), **B** (minor cosmetic), **C** (needs repair/refurb), **D** (non-repairable, parts or scrap).
- **Speed**: days in the loop translate directly to lost value; use **cross-docking** for returns with obvious destination (return to vendor, restock).
- **Data**: capture return reason codes, SKU, supplier, batch to feed root-cause (quality, size chart, packaging).

Linkages with inventory accounting: returned stock carries a **valuation** (lower of cost and net realisable value; see [[116 Inventory Valuation, Cycle Counting & Inventory Governance]]) and in ERP is held in blocked or returns stock until graded ([[082 SAP SD — Sales & Distribution]] covers returns orders and credit memos).

### Example
A returns centre processes 1,000 returned phones a day with 60 graders each doing 20 units a day (1,200 capacity). Average time from receipt to grade is 1.5 days. If the average value loss from ageing is 0.3% of value per day on ₹20,000 phones (₹60 a day), cutting dwell from 1.5 to 0.5 days saves ₹60 per phone, or ₹60,000 a day = **₹18 lakh a month** on 1,000 phones a day (30 days), without adding any grader. Reduced time to disposition is worth as much as any improved grade.

### In the news
See news box. As recycling becomes regulated, graded and documented returns (with serials and weights) become evidence for EPR reporting.

### Interview angle
> [!question] How it is asked
> "Design a returns process for an online electronics retailer."

> [!tip] Strong answer includes
> - End-to-end flow: RMA, pickup, QC, grading, disposition, refund
> - Gatekeeping and fraud checks at source
> - Hub design: central returns centre vs regional, with SLAs
> - Data: reasons, SKU, supplier, root cause feedback to merchandising and quality

---
## 3. The Disposition Decision: Restock, Refurbish, Remanufacture, Recycle, Liquidate
> 🟠 Tier 2 · _Key points:_ disposition options, value hierarchy, decision rule, secondary markets

### Definition
After grading, each unit goes to the **highest net-recovery option** (the "value-recovery hierarchy"):
1. **Return to vendor (RTV)**: defective or contractual returns; credit from supplier.
2. **Restock / resell as new or open-box**: good condition; fastest, highest value.
3. **Refurbish**: cosmetic/functional repair, then sell as "refurbished" in a secondary channel.
4. **Remanufacture**: dismantle, rebuild to like-new specification with warranty (engines, alternators, copiers).
5. **Cannibalise / harvest parts**: for spares inventory.
6. **Liquidate**: sell to bulk buyers or auction in lots (jobbers, B-stock sites).
7. **Recycle**: material recovery through authorised recyclers (compulsory for e-waste, batteries).
8. **Dispose** (compliant landfill or incineration), last resort.

Decision rule per unit: $\text{Net recovery}_j = \text{Resale value}_j - \text{Processing cost}_j - \text{Reverse freight} - \text{Holding cost}$; choose $j$ with the highest value, subject to **channel conflicts** (refurbished sold at deep discount must not cannibalise new sales; brand protection) and **regulation** (safety certification, warranty).

### Example
See section 4 for a full computation. In short: a Grade-C phone can be repaired (net ₹5,950) or liquidated in bulk (net ₹5,900): almost equal, so a small change in repair failure rate flips the decision. The refurbish option for Grade B phones (net ₹11,350) is far above the bulk liquidation of ₹5,900.

### In the news
See news box. The regulated options (recycling for e-waste, scrapping through RVSFs) show that disposition is partly a compliance decision.

### Interview angle
> [!question] How it is asked
> "A retailer has 10,000 returned units in mixed condition. How do you decide what to do with them?"

> [!tip] Strong answer includes
> - Grade first, then compute net recovery per option
> - Hierarchy and exceptions (brand, regulation, safety)
> - Speed and holding cost; channel conflict
> - Feedback to prevent returns and recover from suppliers

---
## 4. Recovery Value Economics: A Worked Example
> 🟠 Tier 2 · _Key points:_ net recovery, recovery rate, liquidate-all vs graded disposition

### Definition
**Recovery rate** = total value recovered ÷ original value of returned goods. Net recovery per unit = resale price − processing/repair cost − reverse freight. The point of grading is that blended recovery from **graded, differentiated** disposition exceeds bulk liquidation of the whole lot, after covering grading costs. Related economics include **net realisable value (NRV)** for accounting ([[110 Cost Accounting for Operations]]).

### Example
1,000 returned smartphones, original selling price ₹20,000. Reverse freight ₹250 per unit. Grade mix and chosen routes (assumed figures):

| Grade | Share | Units | Route | Resale (₹) | Process cost (₹) | Net per unit (₹) | Total (₹ lakh) |
|---|---|---|---|---|---|---|---|
| A | 25% | 250 | Open-box restock | 16,000 | 300 | 15,450 | 38.63 |
| B | 35% | 350 | Refurbish and sell | 12,500 | 900 | 11,350 | 39.73 |
| C | 25% | 250 | Repair and sell | 9,000 | 2,800 | 5,950 | 14.88 |
| D | 15% | 150 | Parts/recycle | 1,500 | 200 | 1,050 | 1.58 |

Total net recovery = ₹94.8 lakh, i.e. ₹9,480 per unit, **47.4%** of original value. Alternative: sell all 1,000 units as a mixed lot to a bulk buyer at ₹6,000 each less ₹100 freight per unit: ₹59.0 lakh (**29.5%**). Graded disposition is better by ₹35.8 lakh, even before counting that Grade A and B units protect brand value. Grading costs (say ₹150 a unit = ₹1.5 lakh) are small in comparison. Note that C-grade repair (₹5,950) is barely better than liquidation (₹5,900): a 5% failure on repair removes the advantage.

### In the news
See news box. Under EPR, Grade D units flow to authorised recyclers and the recycling certificate counts toward the producer's target.

### Interview angle
> [!question] How it is asked
> "How would you evaluate whether to invest in a refurbishment centre for returned products?"

> [!tip] Strong answer includes
> - Grade mix data, route economics per grade, recovery rate
> - Capacity and fixed costs (tools, trained technicians, space) vs volume
> - Sensitivity to resale prices and repair yield
> - Channel conflict, warranty and compliance risks

---
## 5. Closed-Loop Supply Chains & the Circular Economy
> 🟠 Tier 2 · _Key points:_ open vs closed loop, take-back, design for disassembly, product-as-a-service

### Definition
A **closed-loop supply chain** integrates forward and reverse flows so used products or materials return to the same maker to be reused, remanufactured or recycled into new product; an **open-loop** system recovers material for use in other products (e.g. PET bottles to polyester fibre). The **circular economy** extends this: design out waste, keep products in use, regenerate materials.

Enablers: **take-back** programmes (buy-back, trade-in, deposit-refund), **design for disassembly** and modularity ([[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]), standardised **materials** and **labelling**, **product-as-a-service** (leasing, subscriptions, pay-per-use), and **digital product passports** (traceability of battery/part history). Barriers: collection logistics and cost, uncertain return quality, price of virgin materials, regulatory definition of waste, and consumer attitudes to refurbished goods.

### Example
A beverage firm uses returnable glass bottles in a deposit scheme: a glass bottle costs ₹14, with 25 trips in its life, handling and washing ₹1.5 per trip, and return loop transport ₹0.6 per trip. Cost per trip = 14/25 + 1.5 + 0.6 = **₹2.66**. A single-use PET bottle costs an assumed ₹6 per fill (plus end-of-life burden). Breakeven number of trips: 14/n + 2.1 = 6 gives n = 3.6, so the returnable system wins above about 4 trips. If only 70% of bottles come back each cycle, the expected life falls to about 1/0.3 = 3.3 trips and the returnable system loses its advantage: the return rate is the economic driver.

### In the news
See news box. The rPET mandate (30% recycled content from April 2025) is a closed-loop requirement for bottles, with recycling capacity now the constraint.

### Interview angle
> [!question] How it is asked
> "Is a closed-loop model viable for consumer electronics in India?"

> [!tip] Strong answer includes
> - Definitions and examples; enabling design (modularity, labelling)
> - Economics: collection cost, recovery rate and value of recovered material
> - Regulation (EPR) as a forcing function, and channels (trade-in, dealers)
> - Barriers: informal sector competition, consumer trust, data security

---
## 6. Remanufacturing & Retreading: Auto Parts, Tyres, Electronics
> 🟠 Tier 2 · _Key points:_ core, reman vs refurbish, retread, warranty, core deposit

### Definition
**Remanufacturing** restores used products (**cores**) to like-new performance, with a warranty equal to new, via disassembly, cleaning, inspection, replacement of worn components and testing. It differs from **refurbishing** (cosmetic, minimal rework, lower warranty) and **repair** (fix the specific fault). Typical sectors: auto engines, transmissions, alternators, starters, diesel injectors, aerospace parts, copiers and printers, medical imaging equipment, and increasingly EV batteries (second-life).

Operational issues: the **core supply** (uncertain quantity and quality; offered via **core deposit** or trade-in), **dismantling yield** (share of core components reused), **testing**, **spare parts** availability, and **demand** for reman parts alongside new parts ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]] applies to quality of the rebuilt part). **Tyre retreading** replaces the worn tread on a sound **casing** (hot or cold process); it is widely used for truck and bus tyres and aircraft, and for fleets reduces cost per km significantly. India's tyre chain is discussed in [[131 Automotive Supply Chain - JIT, Tiers & EVs]].

### Example
Assumed values: a new truck tyre costs ₹22,000 and lasts 80,000 km; a retread costs ₹7,000 and lasts 60,000 km on a sound casing. Cost per km: new = 22,000/80,000 = **₹0.275**; retread = 7,000/60,000 = **₹0.117** (casing cost already sunk in the first life), a saving of **58%** per km. A fleet of 1,000 tyres retreaded once saves (22,000 − 7,000) × 1,000 = **₹1.5 crore** of purchases against a new tyre, before lower resale value, with the condition that casings pass inspection (typically 70-85% of casings qualify; assumption). Business risks: casing quality, retread blow-outs (brand, safety), and customer acceptance.

### In the news
See news box. Natural-rubber supply risk and recycling/EPR targets for tyres favour retreading and tyre recycling; chemical or pyrolysis recycling is in early stages.

### Interview angle
> [!question] How it is asked
> "A truck fleet owner asks if retreading is worth it. How do you answer?"

> [!tip] Strong answer includes
> - Cost per km comparison and casing quality criteria
> - Safety and warranty, supplier selection (certified retreaders)
> - Impact on inventory, spares and tyre-management policy (pressure, rotation)
> - Environmental and EPR benefits

---
## 7. Reverse Logistics Network Design & 3PLs
> 🟠 Tier 2 · _Key points:_ centralised returns hub, consolidation, RTV, 3PL, reverse pickup, ERP

### Definition
Design decisions: **where to process** (centralised, regional or at stores), **what to consolidate** (milk-run reverse pickups, cross-dock with forward return legs), **who runs it** (in-house vs **3PL returns specialists**, repair partners and authorised service centres), **capacity** (peak seasons: festive sales and post-sale returns), and **information systems** (returns management, RMA in WMS/ERP, serial and IMEI tracking). Typical trade-off: fewer, larger centres lower fixed cost and give expertise but lengthen transport and time; more centres do the opposite ([[113 Network Design & Facility Location Modelling]]).

Outsourcing criteria: volume variability, specialised repair skills, geography, compliance (authorised recyclers need authorisation under the EPR rules), and data security (wiping devices). Metrics: **time to disposition**, **cost per return**, **recovery rate**, **backlog**. In India, quick-commerce and e-commerce players run reverse pickup via their delivery fleets and **return-to-origin (RTO)** flows for failed deliveries ([[129 E-commerce & Quick-Commerce Fulfilment]]).

### Example
Two options for 600,000 returns a year: **Central hub** (one site, fixed cost ₹8 crore a year, handling ₹120 per return, transport to hub ₹110 per return) = 8 + 600,000 × 230/1e7 = 8 + 13.8 = **₹21.8 crore**. **Three regional hubs** (fixed ₹15 crore a year, handling ₹130 per return due to lower scale, transport ₹60 per return) = 15 + 600,000 × 190/1e7 = 15 + 11.4 = **₹26.4 crore**. The central hub wins by ₹4.6 crore unless the three-hub model reduces time to disposition enough to save value: at 0.5 days faster and ₹60 a day value loss (₹30 per return) that is 600,000 × 30 = ₹1.8 crore, still short. Thus central unless speed value per day is above about ₹153 per return-day (4.6 crore ÷ 600,000 ÷ 0.5).

### In the news
See news box. Producers must route end-of-life goods only to authorised recyclers, which constrains a network to licensed nodes.

### Interview angle
> [!question] How it is asked
> "Should we centralise returns processing for our e-commerce business, or do regional centres?"

> [!tip] Strong answer includes
> - Cost model (fixed, handling, transport) plus value of speed
> - Customer promise (refund timing) and service levels
> - 3PL vs in-house: capability, control, data security
> - Peaks and scalability; KPIs

---
## 8. E-commerce Returns & Returns Fraud
> 🟠 Tier 2 · _Key points:_ RTO, wardrobing, empty-box and swapped-item fraud, controls, policy design

### Definition
Indian e-commerce faces high **return rates** (fashion and electronics) and **RTO** (return to origin) on failed cash-on-delivery orders. **Return fraud** types: **wardrobing** (using and returning), **empty-box or wrong-item return**, **swapped item** (returning a fake or older unit), **claiming non-receipt**, **serial returners**, **refund abuse** with coupons, and **organised rings**. Controls:
- **Policy design**: return windows, exchange-only for high-risk categories, restocking fees, **try-and-buy** only for trusted customers.
- **Verification**: **IMEI/serial match**, tamper-evident packaging, **video at pickup**, QC at pick-up point, weight checks.
- **Analytics**: risk scoring on customer, pincode, category, return history ([[094 ML Fundamentals & Workflow]], [[096 Classification Algorithms]]).
- **Differentiated service**: faster refunds for low-risk customers, held refunds for high-risk.
- **Reduce reasons for return**: size guides, better photos, accurate descriptions, packaging.

### Example
An electronics seller has 100,000 orders a month, a 20% return rate (20,000 returns) and 2% of returns fraudulent (400 cases). Average value lost per fraud case = ₹9,000 (the item is unsaleable or substituted), so loss = 400 × 9,000 = **₹36 lakh a month**. Pickup QC with IMEI check and video costs ₹40 per return = 20,000 × 40 = ₹8 lakh a month and catches 75% of fraud: loss avoided = ₹27 lakh; net gain **₹19 lakh a month**. A risk-score-based targeted QC (checking only the top 30% riskiest returns, catching 65% of fraud) costs 6,000 × 40 = ₹2.4 lakh and avoids ₹23.4 lakh: net **₹21 lakh a month**: better and less friction for honest customers.

### In the news
See news box. Verified returns data (serial numbers, grading records) also supports EPR and warranty accounting.

### Interview angle
> [!question] How it is asked
> "Return rates at your marketplace have jumped to 25%. How do you reduce them without hurting customers?"

> [!tip] Strong answer includes
> - Split returns by reason: genuine defect, size/fit, fraud, change of mind
> - Fix root causes (listing quality, packaging, sizing) and target fraud with scoring, not blanket restrictions
> - Policy and operations: windows, pickup QC, refund timing for risky segments
> - Financial and customer-experience trade-offs

---
## 9. Refurbished Marketplaces & Re-commerce
> 🟠 Tier 2 · _Key points:_ re-commerce, grading standards, warranty, trust, supply of used devices

### Definition
**Re-commerce** is the resale of used or refurbished goods: phones, laptops, appliances, furniture, fashion. Models: **trade-in and buy-back** (OEM or retailer buys old devices to subsidise new ones), **refurbished marketplaces** with warranty, **certified pre-owned programmes** (cars, premium devices), **peer-to-peer** platforms, and **B2B liquidation** sites. In India this includes refurbished smartphones through online platforms and retail partners, and OEM-certified programmes.

Success factors: **supply** (acquiring used units at the right price via trade-in), **grading and testing** at scale, **warranty and returns** that build trust, **spare parts and refurbishment capacity**, data wiping, and sales channels with price transparency. Supply-chain issues: grading consistency, parts availability for old models, fraud risk (stolen devices, IMEI blacklists), and brand-protection concerns.

### Example
A platform buys used phones at ₹9,000 average, refurbishes (₹1,200 parts and labour, ₹400 logistics, ₹300 QC and packaging) and sells at ₹14,500 with a 6-month warranty. Warranty claims average 6% of units, costing ₹2,500 each. Per unit: revenue 14,500 − cost of purchase 9,000 − refurb 1,200 − logistics 400 − QC 300 − warranty (0.06 × 2,500 = 150) = **₹3,450**, a **23.8%** margin on revenue, before platform overhead and marketing. If the failure rate doubles to 12%, warranty cost rises to ₹300 and margin falls by ₹150 (to ₹3,300): small relative to purchase price, so the major risk lies in paying too much for used units, not warranty.

### In the news
See news box. As e-waste rules push producers and recyclers to formalise, a formal channel for refurbished devices also reduces leakage to the informal sector.

### Interview angle
> [!question] How it is asked
> "How would you build a refurbished-phone business in India and where does the supply chain break?"

> [!tip] Strong answer includes
> - Sourcing of used devices (trade-in, partnerships, corporate fleets)
> - Grading, refurbishment capacity, parts, and warranty design
> - Unit economics and price risk (new-model launches depress old phone prices)
> - Regulation (EPR, data wiping, stolen-device checks)

---
## 10. India's EPR Architecture: E-Waste Rules 2022 & Battery Waste Rules 2022
> 🟠 Tier 2 · _Key points:_ EPR, producer, authorised recycler, EPR certificates, portal, targets

### Definition
**Extended Producer Responsibility (EPR)** makes the producer responsible for the whole life cycle, including take-back and environmentally sound disposal. In India EPR is operated through **online portals** run by the **CPCB** where producers register, report sales, buy **EPR certificates** from authorised recyclers, and file returns. The mechanism creates a **market for EPR certificates** (a tradable instrument resembling carbon credits, as the Wikipedia summary of EPR notes).

**E-Waste (Management) Rules, 2022** (effective 1 April 2023): cover a larger list of electrical and electronic equipment than the 2016 rules (which notified 21 items); require producers, importers and brand owners to register, set **EPR targets** as a percentage of the weight sold in earlier years (the schedule steps up over years; check the current schedule), allow **refurbishers** to be registered, and require recyclers to be authorised. Certificates are generated by recyclers on proof of recycling.

**Battery Waste Management Rules, 2022** (notified 2022; operational from 2023): cover portable, automotive, industrial and EV batteries, require **EPR** from producers, and prescribe **recovery or recycled-content** obligations (details differ by chemistry and year: verify before quoting numbers). Important for EV supply chain ([[131 Automotive Supply Chain - JIT, Tiers & EVs]]) as Li-ion packs reach end of life.

Operational implications: producer's **reverse logistics network**, partnerships with authorised recyclers, **take-back at dealers and service centres**, **record keeping** (weights, serials), and penalties or **environmental compensation** for non-compliance.

### Example
A laptop maker sells 100,000 units a year at 2.2 kg average: 220 tonnes. Suppose the EPR target is 60% of that weight (assumed percentage for illustration) = **132 tonnes** to be certified through authorised recyclers. If the certificate price (assumption) is ₹60 per kg, the compliance cost = 132,000 kg × 60 = **₹79.2 lakh** a year (about ₹79 per laptop sold, which is 0.13% of a ₹60,000 laptop's price). Taking back through its own service network could reduce cost if collection cost per kg is below ₹60 and quality is verified, but it must still end in an authorised recycler.

### In the news
See news box. The 72% jump in e-waste in five years and the rules effective April 2023 explain the compliance push.

### Interview angle
> [!question] How it is asked
> "What is EPR and how would a consumer-electronics company set up compliance in India?"

> [!tip] Strong answer includes
> - EPR definition, portals, certificates, targets, and recyclers
> - Operational set-up: registration, data systems, take-back, authorised partners
> - Cost estimate and make-vs-buy of collection
> - Risk: informal-sector leakage, certificate fraud, changing rules

---
## 11. Plastic Packaging EPR, rPET Mandate & Tyre EPR
> 🟠 Tier 2 · _Key points:_ categories 1-4, recycled content, certificates, deposit-refund, waste tyres

### Definition
**Plastic Packaging EPR**: under the Plastic Waste Management (Amendment) Rules, 2022 (notified February 2022), brand owners, producers and importers (PIBOs) must meet **EPR targets** across categories: **Category 1** rigid, **2** flexible single layer, **3** multilayer or laminated, **4** compostable. Targets include collection and recycling obligations and, increasingly, **recycled-content** requirements. Compliance is through **EPR certificates** via the CPCB portal. The 2025-26 **rPET mandate**: 30% recycled food-grade PET in rigid packaging from 1 April 2025, 40% targeted for 2026-27 and rising 10 points a year to 60% by 2028-29 (Business Standard); recycling capacity and **FSSAI authorisation** for food-grade r-PET are bottlenecks, and bottling cost rises were estimated by industry at nearly 30%. Some states introduced **deposit-refund** schemes (Himachal Pradesh, 2025).

**Tyre EPR**: waste tyres are covered under the hazardous and other waste rules, with EPR for tyre producers and importers for recycling or reuse through authorised recyclers (pyrolysis, crumb rubber, reclaim rubber) and retreading as a recovery route; check the current notified targets before quoting numbers.

For the supply chain: PIBOs must **track packaging weights by category**, contract with certified recyclers, and redesign packaging (mono-material, lighter) to lower EPR cost ([[140 Packaging, Unitisation & Load Optimisation]]).

### Example
A snacks company places 8,000 tonnes of multilayer packaging (Category 3) in a year. Assume an EPR target of 50% (illustrative), so 4,000 tonnes must be certified; at an assumed certificate cost of ₹9,000 per tonne the cost is 4,000 × 9,000 = **₹3.6 crore**. Now assume it redesigns 30% of volume (2,400 tonnes) into a recyclable mono-material whose assumed compliance cost is ₹5,000 per tonne. Remaining multilayer: 5,600 × 50% × 9,000 = ₹2.52 crore; redesigned: 2,400 × 50% × 5,000 = ₹0.60 crore; total **₹3.12 crore**, a saving of ₹0.48 crore a year. Redesign pays only if the extra material and conversion cost on the 2,400 tonnes is below ₹0.48 crore ÷ 2,400 t = **₹2,000 per tonne**.

### In the news
See news box. The beverage industry's objections show how recycled-content targets can run ahead of available recycling capacity.

### Interview angle
> [!question] How it is asked
> "A beverage company must reach 30% recycled PET by April 2025 and 60% later. How would you build the supply chain?"

> [!tip] Strong answer includes
> - Capacity gap: authorised food-grade r-PET suppliers and take-back flows
> - Contracts and prices for r-PET, multiple suppliers, quality spec (FSSAI)
> - Collection systems: deposit-refund, kabadiwalas, partnerships; light-weighting and design
> - Cost impact and pass-through, scenario planning for rule changes

---
## 12. Vehicle Scrapping Policy & RVSFs
> 🟠 Tier 2 · _Key points:_ Voluntary Vehicle-Fleet Modernisation, fitness test, RVSF, ATS, scrapping certificate, incentives

### Definition
India's **Vehicle Scrapping Policy** (Voluntary Vehicle-Fleet Modernisation Programme, launched August 2021) aims to phase out old, polluting, unfit vehicles and to create a formal recycling industry. Elements: **fitness tests at Automated Testing Stations (ATS)**; vehicles that fail (or are not renewed) become **end-of-life vehicles**; owners deliver them to a **Registered Vehicle Scrapping Facility (RVSF)** that issues a **Certificate of Deposit**; the owner gets **scrap value, a scrapping-certificate discount** on a new vehicle (manufacturers' discount; the PIB figures in the news box), and potential **road-tax and registration concessions** by states. Commercial vehicles get a 3% (above 3.5 t GVW) or 1.5% (below) discount on direct scrapping; certificate trading carries 2.75% and 1.25%.

As of the August 2024 PIB note: 60+ RVSFs across 17 States/UTs and 75+ ATSs across 12; 11 passenger-vehicle and 7 commercial-vehicle manufacturers participated. RVSF operations: dismantling (fluids, battery, tyres, airbags, catalytic converter), **parts recovery** for resale (where rules permit), **material recovery** (steel, aluminium, copper, plastics) and **ELV waste** handling, with traceability through the **Vahan** system. The policy links to auto OEM EPR for vehicles and to the aftermarket (reman parts) ([[131 Automotive Supply Chain - JIT, Tiers & EVs]]).

### Example
A passenger car with ₹8 lakh ex-showroom price: incentive = min(1.5% × 800,000 = ₹12,000, ₹20,000) = **₹12,000**; at ₹15 lakh, 1.5% would be ₹22,500, capped at **₹20,000**. For an old 1,100 kg car, assume 85% is recoverable metal at ₹30 per kg: 1,100 × 0.85 × 30 = **₹28,050** of material value. If the RVSF pays the owner ₹25,000-30,000 for it, the owner's total benefit is about ₹37,000-50,000 with the incentive, against a resale value that may be only ₹60,000-90,000 for an old petrol car: the policy works mainly for cars at the end of their economic life, which is one reason uptake is modest. RVSF economics: a plant scrapping 2,000 cars a year earns about ₹28,050 of material value plus ₹8,000 of parts resale per car (assumption) = ₹36,050 × 2,000 = **₹7.2 crore**; paying owners ₹30,000 each costs ₹6.0 crore, leaving ₹1.2 crore (₹6,050 per car) for labour, compliance and capital recovery, so volume and parts monetisation decide viability.

### In the news
See news box. The RVSF and ATS counts show the infrastructure phase of the policy; [Business Standard reported in September 2024](https://www.business-standard.com/industry/auto/govt-studies-linking-vehicle-scrapping-policy-to-pollution-levels-not-age-124091001083_1.html) that the government was studying a link between scrapping and pollution levels rather than age alone.

### Interview angle
> [!question] How it is asked
> "Why has India's vehicle scrapping policy had modest uptake and what would you change?"

> [!tip] Strong answer includes
> - Owner economics (scrap value + incentive vs resale value), convenience of RVSF access
> - Supply-side: RVSF capacity, parts monetisation, feedstock volume, regulation
> - Incentive design (state road tax rebate, manufacturer discounts, age vs pollution-based tests)
> - Sustainability and supply chain benefits: material recovery, formalisation of ELV sector

---
## 13. Reverse Logistics KPIs & Cost Accounting
> 🟠 Tier 2 · _Key points:_ return rate, recovery rate, time to disposition, cost per return, EPR compliance %

### Definition
KPIs ([[012 Supply Chain Analytics & KPIs]]):
- **Return rate** = units returned ÷ units sold (by reason, SKU, channel).
- **Time to disposition** = days from receipt to final route; **dock-to-stock** for restock.
- **Recovery rate** = value recovered ÷ original value (or ÷ cost).
- **Cost per return** = reverse freight + handling + processing + admin.
- **Net recovery per unit** (see section 4).
- **Grade accuracy** (audit misgrading), **repair yield** and **warranty failure rate** for refurbished goods.
- **Fraud rate** and **recovery from vendors** (RTV credit recovered %).
- **EPR compliance %** = certified quantity ÷ obligation; **collection rate** for take-back; **recycled content %**.
- **Carbon and landfill diversion**.

Cost accounting: track reverse logistics as a **separate cost centre** with all components; allocate by driver; compute **total cost of returns** as % of sales; include **inventory write-down** from unsellable returns.

### Example
A company sells 5,00,000 units a year with a 12% return rate (60,000 returns). Cost per return is ₹320 (freight ₹140, handling ₹100, processing ₹80). Average return value ₹2,400; recovery rate 55%. Value recovered = 60,000 × 2,400 × 0.55 = ₹7.92 crore; value lost = 60,000 × 2,400 × 0.45 = ₹6.48 crore; cost = 60,000 × 320 = ₹1.92 crore. Total net cost of returns = 6.48 + 1.92 = **₹8.4 crore**. Lifting recovery to 65% reduces lost value by ₹1.44 crore (60,000 × 2,400 × 10%); cutting return rate from 12% to 10% reduces both categories by one-sixth, saving 8.4 crore × (1/6) = **₹1.4 crore**: about equal gains, from very different levers.

### In the news
See news box. EPR compliance % and RVSF-supplied scrap volumes are new reverse-logistics KPIs created by regulation.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you put on a returns dashboard and how would you use them?"

> [!tip] Strong answer includes
> - A balanced set: rate, speed, value, cost, quality, compliance
> - Reason-code analytics feeding upstream fixes
> - Cost-to-recover vs value recovered by route and grade
> - Targets and owners; link to finance (provisioning)

---
## 14. ⭐ Advanced: EPR Make-vs-Buy and Reverse-Network Modelling
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Producers face a **make-vs-buy** choice for EPR: **buy certificates** from recyclers (variable cost, little control) or **build own take-back** (collection points, reverse pickups, partnerships) with a fixed cost and **learning**. Decision model:

$$\text{Cost}_{own} = F + c_{coll} \cdot Q_{own} + c_{rec}\cdot Q_{own}, \qquad \text{Cost}_{buy} = p \cdot Q_{total}$$

where $F$ = fixed cost of the programme, $c_{coll}$ = collection cost per kg, $c_{rec}$ = recycling fee per kg, $p$ = certificate price per kg and $Q$ = quantity. Own-collection is attractive when $Q_{own}$ is large enough that $F/Q_{own} + c_{coll} + c_{rec} < p$ and when collection also yields **resale value or customer loyalty** (trade-in credits). Reverse-network design may include **mixed-integer location** models to choose collection nodes and routes ([[148 Operations Research - Network Models & Integer Programming]]), with a closed-loop objective that includes forward and reverse flows.

### Example
Obligation 132 tonnes (from section 10). Buy: ₹60 per kg × 132,000 = **₹79.2 lakh**. Own: F = ₹25 lakh, c_coll = ₹22/kg, c_rec = ₹18/kg on a collected 132,000 kg: 25 lakh + 132,000 × 40 = 25 lakh + 52.8 lakh = **₹77.8 lakh**: slightly cheaper and gives control and goodwill; if only 100,000 kg can be collected (the remaining 32,000 kg bought at ₹60): own = 25 + 40 lakh + 19.2 lakh = **₹84.2 lakh**, more expensive than buying everything. The breakeven collected quantity (with the shortfall bought at ₹60) is where own cost equals buy cost: ₹25 lakh + 40Q + 60(132,000 − Q) = ₹79.2 lakh, which simplifies to 25 lakh = 20Q, so Q = 125,000 kg. Therefore own-collection wins only above 125 tonnes of actual collection, i.e. a **95% collection yield**: collection performance, not unit costs, drives the decision.

### In the news
See news box. As certificate markets mature and recycling capacity grows, certificate prices will move, so the make-vs-buy balance should be reviewed annually.

### Interview angle
> [!question] How it is asked
> "Should a company buy EPR certificates or build its own take-back network?"

> [!tip] Strong answer includes
> - Cost model with fixed and variable parts, and the breakeven quantity
> - Yield risk (collection shortfalls) and the fallback of buying
> - Non-cost benefits: brand, trade-in, data, supply of cores for refurbishing
> - Regulatory and price risk in certificate markets
