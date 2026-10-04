---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Food, Agri & Perishables Supply Chain - India"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Food, Agri & Perishables Supply Chain - India

⬅ [[132 Pharma & Healthcare Supply Chain]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[134 Electronics & Semiconductor Supply Chain]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Farm-to-Fork Chain & Where the Rupee Goes]]
2. [[#2. APMC Mandis & e-NAM]]
3. [[#3. Post-Harvest Losses & How to Measure Them]]
4. [[#4. Cold Chain Infrastructure & the Gap (PMKSY, NCCD)]]
5. [[#5. Shelf Life, FEFO & Quality Management]]
6. [[#6. Amul & the Cooperative Dairy Model]]
7. [[#7. Contract Farming & Direct Procurement]]
8. [[#8. FPOs & Aggregation]]
9. [[#9. Agri-Tech Models: DeHaat, Ninjacart & Peers]]
10. [[#10. MSP, Procurement & Agri Price Policy]]
11. [[#11. Perishable Inventory: Newsvendor & Markdown Logic]]
12. [[#12. Food Safety, FSSAI, HACCP & Traceability]]
13. [[#13. Worked Case: A Loss-Reduction Business Case]]
14. [[#14. ⭐ Advanced: Price Volatility, Trade Policy & Network Design for Fresh]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India grows enough food but still loses 30-40% of it before it is eaten
> **Post-harvest loss and the irradiation debate (May 2026).** A Business Standard report put losses between harvest and consumption at 30-40% of India's production. India made 357.73 million tonnes of foodgrain in FY2024-25, and mango output was 22.8 million tonnes, but mango exports were only about 29,938 tonnes. India has just 19 food-irradiation plants and only 4 are USDA-certified for exports; the government earmarked ₹1,000 crore under Pradhan Mantri Kisan Sampada Yojana (PMKSY) for 50 multi-product irradiation units. ([Business Standard, 11 May 2026](https://www.business-standard.com/economy/news/food-irradiation-india-mango-exports-post-harvest-losses-commercial-viability-126051100088_1.html))
>
> **Amul crosses ₹1 trillion (FY2025-26).** Amul reported turnover above ₹1 trillion (about 11% growth); GCMMF's own turnover was ₹73,450 crore versus ₹65,911 crore in FY25 (+11.4%). In May 2026 GCMMF raised milk prices by ₹2 a litre and member unions raised the farmer procurement price by ₹30 per kg of fat (+3.7% over May 2025), citing cattle-feed, packaging-film and fuel costs. ([Business Standard, 5 April 2026](https://www.business-standard.com/companies/news/amul-turnover-crosses-rs-1-trillion-fy26-gcmmf-growth-126040500200_1.html), [Business Standard, 13 May 2026](https://www.business-standard.com/companies/news/amul-hikes-milk-prices-by-rs-2-litre-across-india-effective-may-14-126051301395_1.html))
>
> **Agri-tech reset: Ninjacart (December 2025).** Ninjacart reported FY25 operating revenue of ₹1,634 crore (down from ₹2,007 crore) and a loss of ₹256 crore after exiting low-margin, non-core lines; its core businesses were growing over 100% in FY26 and management targets overall profitability in 2026-27. ([Business Standard, 26 December 2025](https://www.business-standard.com/companies/news/ninjacart-posts-rs-256-cr-loss-in-fy25-revenue-drops-to-rs-1-634-cr-125122600743_1.html))
>
> **e-NAM keeps widening its basket (February 2025).** The Agriculture Ministry added 10 commodities (including dried tulsi leaves, besan, wheat flour, asafoetida, baby corn and dragon fruit), taking e-NAM's tradable items to 231, with value-added FPO products in focus. ([Business Standard, 6 February 2025](https://www.business-standard.com/industry/agriculture/govt-adds-10-additional-commodities-to-e-nam-platform-for-trading-125020601719_1.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Farm-to-Fork Chain & Where the Rupee Goes
> 🟠 Tier 2 · _Key points:_ aggregator, mandi, wholesaler, retailer, price spread, farmer share

### Definition
A typical Indian fresh-produce chain: **farmer** → village **aggregator/trader** → **APMC mandi** (commission agent, auctions) → **wholesaler/semi-wholesaler** → **retailer** (thela, kirana, modern retail) → consumer. Variants: farmer → FPO → processor; farmer → company collection centre (ITC, Reliance, Amul, PepsiCo) → plant; farmer → agri-tech aggregator (Ninjacart, DeHaat) → retailer or quick-commerce dark store ([[129 E-commerce & Quick-Commerce Fulfilment]]).

Why the chain is long: fragmented small holdings (average holding about 1 hectare), thin local storage, seasonal gluts, credit from the trader, and many handling steps (each adding loss, cost and margin). Concepts: **price spread** = consumer price − farm-gate price; **farmer's share** = farm-gate/consumer price; **marketing margin** and **marketing cost** (transport, loading/unloading (hamali), commission, spoilage).

### Example
An illustrative tomato chain (per kg sold, prices ₹): farm-gate **12.00**. Aggregator adds transport and loading ₹1.50 → ₹13.50; mandi charges (commission, hamali, weighing) ₹1.00 → **₹14.50 cost to the wholesaler**. The wholesaler loses 8% of the weight to spoilage and wants a 10% margin: selling price = 14.50 ÷ 0.92 × 1.10 = **₹17.34**. The retailer loses 10% and wants a 15% margin: price = 17.34 ÷ 0.90 × 1.15 = **₹22.15**. Farmer's share = 12/22.15 = **54%**. If spoilage were halved at both stages (4% and 5%), the consumer price would fall to 14.50 ÷ 0.96 × 1.10 = ₹16.62, then 16.62 ÷ 0.95 × 1.15 = **₹20.11**: a 9% price cut or, if split, better farm-gate prices and margins at no extra cost.

### In the news
See news box. The 30-40% post-harvest loss estimate is the spoilage term in this arithmetic; every point shaved there flows into price, margin or farmer income.

### Interview angle
> [!question] How it is asked
> "A tomato farmer gets ₹12 a kg and the consumer pays ₹30. Where does the difference go and how would you reduce it?"

> [!tip] Strong answer includes
> - A stage-by-stage price build-up: transport, mandi charges, spoilage, margins
> - Separating **cost** (fixed by physics and handling) from **margin** (market power)
> - Levers: aggregation, direct procurement, crates and cold chain, storage to smooth gluts, digital price discovery
> - Awareness that cutting stages may shift, not remove, functions (storage, credit, risk) ([[009 Logistics & Distribution]])

---
## 2. APMC Mandis & e-NAM
> 🟠 Tier 2 · _Key points:_ APMC Act, commission agents, auction, e-NAM, price discovery, reform limits

### Definition
State **APMC** (Agricultural Produce Market Committee) Acts require notified produce to be sold in regulated **mandis**, licensing traders and commission agents (arhtiyas), levying a **market fee** and commission. Aim: protect farmers from exploitation; side effects: cartelised traders, high cumulative charges, and monopoly of the notified market.

**e-NAM** (National Agriculture Market) launched 14 April 2016 as a pan-India electronic trading portal **networking existing APMC mandis** for online bidding, with e-payment, weighing and assaying at the mandi. It began with a first batch of mandis and, by the time of the figures Wikipedia records, linked over 1,000 mandis in 18 states and 2 UTs; the listed items reached **231 commodities** by February 2025. Challenges: thin online bidding in many mandis (still physical lots), lack of assaying labs, inter-state movement barriers and license rules, and farmers' need for immediate cash. Complementary moves: **warehouse-based sale** (WDRA-registered warehouse receipts, with a gateway for post-harvest finance launched in March 2024 per Business Standard) and the **Model APMC Act 2017** (private markets, direct purchase).

### Example
A commission agent charges 2% and the market fee is 1.5% of ₹2,000 per quintal, plus ₹40 for hamali and ₹30 for weighing and sorting: charges = 40 + 30 + 40 + 30 = **₹140 (7%)** per quintal. If an e-NAM trade with quality assaying fetches ₹2,100 per quintal because buyers from another state can bid, the farmer's net = 2,100 − (42 + 31.5 + 40 + 30) = **₹1,956.5**, against 2,000 − 140 = ₹1,860 in the local auction: +5.2%. The gain comes from more bidders (price); the charges stay similar unless fees are reformed.

### In the news
See news box. The February 2025 expansion to value-added products (flours, spices, processed items) shows e-NAM moving from raw commodity trade toward FPO-made products.

### Interview angle
> [!question] How it is asked
> "e-NAM has been live since 2016, yet most farmers still sell locally. Why, and what would you change?"

> [!tip] Strong answer includes
> - What e-NAM is (online trading layer on APMC mandis) and what it is not (not a logistics or storage solution)
> - Barriers: assaying, trust, payment timing, transport, small lots
> - Fixes: grading standards, FPO aggregation, warehouse receipts and finance, last-mile logistics
> - Honest limits: a platform cannot remove physical constraints

---
## 3. Post-Harvest Losses & How to Measure Them
> 🟠 Tier 2 · _Key points:_ harvest, handling, storage, transport, loss %, food loss index, causes

### Definition
**Post-harvest loss** is physical loss (weight) and quality loss (grade, price) between harvest and the consumer. Stages and causes: **harvest** (maturity errors, mechanical damage), **handling** (loose bags, rough loading), **storage** (heat, humidity, pests, no cold chain), **transport** (overloading, long hours, heat), **market** (waiting, unsold produce) and **retail** (overstocking, poor display). Fruit and vegetables lose the most, followed by dairy, fish and meat. Business Standard (May 2026) cites 30-40% losses for India's produce; study figures differ by crop and by method, so state the source and definition when quoting.

Measuring: **Food Loss Percentage** = $\dfrac{\text{quantity lost}}{\text{quantity entering the stage}} \times 100$ at each stage, and the cumulative chain loss: $1-\prod(1-L_i)$. The FAO's **Food Loss Index** tracks loss from farm gate to (not including) retail, and SDG 12.3 aims to halve per-capita food waste at retail and consumer level and cut food losses by 2030. Methods: weighing at stage entry/exit, sampling, surveys, and now sensor/IoT data and photo grading. Quality loss (price discount for lower grade) is converted into **value loss**.

### Example
Mango pulp supply: harvest-to-pack loss 4%, transport 6%, storage 5%, retail 8%. Surviving fraction = 0.96 × 0.94 × 0.95 × 0.92 = **0.789**, a cumulative loss of **21.1%**, slightly below the simple sum of the four rates (23%) because each stage applies to a shrinking base. Cutting transport loss to 3% by switching to ventilated crates gives 0.96 × 0.97 × 0.95 × 0.92 = 0.814, a cumulative loss of 18.6%: a 2.5-point gain from one stage. At 100,000 tonnes handled and ₹40,000 per tonne, that is 2,500 tonnes = **₹10 crore** a year.

### In the news
See news box. At 30-40% loss, irradiation and cold chain are only part of the answer; much of the loss occurs before and during first-mile transport.

### Interview angle
> [!question] How it is asked
> "How would you measure and reduce post-harvest loss for a fresh-produce company?"

> [!tip] Strong answer includes
> - Stage-wise measurement with consistent definitions (weight and value)
> - Pareto of causes by stage to pick the biggest levers
> - Targeted fixes: crates, pre-cooling, grading at source, refrigerated transport, shorter chain
> - Business case (₹ saved vs cost) and a monitoring KPI

---
## 4. Cold Chain Infrastructure & the Gap (PMKSY, NCCD)
> 🟠 Tier 2 · _Key points:_ cold storage, pack house, reefer, ripening chamber, integrated cold chain, utilisation

### Definition
A fresh-produce cold chain: **pack house** (sorting, grading, pre-cooling) → **reefer transport** → **cold storage** (long-term bulk, e.g. potatoes at 2-4°C) or **distribution centre** → **ripening chamber** (bananas, mangoes) → **retail refrigeration**. Types: **bulk cold stores** (mostly potato in UP and West Bengal), **multi-commodity and multi-temperature** stores, **controlled-atmosphere** (apples), and **integrated cold chain** projects.

Government support: the **Integrated Cold Chain and Value Addition Infrastructure** component of **PMKSY** (grants for pack houses, reefers, cold stores, irradiation) and **MIDH/NHB** subsidies for storage. The **National Centre for Cold-Chain Development (NCCD)** is revising technical guidelines and building a digital mobile app for cold-chain data (Business Standard, May 2024). The sector is estimated at about ₹2 lakh crore turnover growing over 10% a year, with a projection of ₹5 lakh crore by 2030-32 (Business Standard, May 2024).

The "gap" is not just capacity but **mismatch and utilisation**: a large share of cold storage capacity is single-commodity (potato) in a few states, while the shortage is in pack houses, reefer vehicles and storage near production clusters for fruit, vegetables, dairy and fish. Low utilisation outside the potato season makes economics hard.

### Example
A potato cold store of 5,000 tonnes charges ₹2.5 per kg per season (assumption), so full-capacity revenue is 5,000,000 kg × 2.5 = ₹125 lakh. Assume fixed cost (interest, depreciation, staff) of ₹60 lakh a year and variable cost (power, handling) of ₹0.8 per kg stored. Profit at utilisation $u$ = 125u − 40u − 60 = 85u − 60 (₹ lakh). At 100% use: **₹25 lakh**; at 85%: 72.25 − 60 = **₹12.25 lakh**; breakeven $u = 60/85 = $ **70.6%**. A store that fills only for the potato season but has 50% use the rest of the year loses money, so multi-commodity or off-season use (apples, chillies, pulses) is the route to viability; hence the policy push for multi-temperature stores.

### In the news
See news box. The irradiation initiative and NCCD guidelines show policy moving from simply funding capacity to funding the right type of capacity.

### Interview angle
> [!question] How it is asked
> "India has plenty of cold storage by tonnage yet fruits and vegetables still rot. Explain and recommend."

> [!tip] Strong answer includes
> - Capacity vs fit: location, commodity, temperature, utilisation
> - Missing links: first-mile pre-cooling, reefer transport, ripening and retail
> - Business model: multi-commodity use, anchor customers, power cost and financing
> - Policy: PMKSY and standards via NCCD; role of FPOs and private logistics ([[132 Pharma & Healthcare Supply Chain]] for similar temperature-control principles)

---
## 5. Shelf Life, FEFO & Quality Management
> 🟠 Tier 2 · _Key points:_ shelf life, FEFO/FIFO, remaining shelf life, markdowns, ripening

### Definition
**Shelf life** is the time a product stays within quality limits under specified storage; it depends on temperature, humidity, handling and packaging. **FEFO** issues by the earliest expiry or best-before date; **FIFO** by earliest receipt, which suffices if shelf life is the same across lots. **Minimum remaining shelf life (MRSL)** is a customer requirement: for example, a modern-trade chain may refuse a dairy lot with less than two-thirds of life left.

Practical tools: **temperature-time indicators**, **FEFO bin location in WMS** ([[010 Warehouse Management]]), **ageing reports** with markdown triggers (e.g. 30% price cut when 25% life remains), **ripening schedules** for fruit, and **transfer between stores** to match demand. The **quality-adjusted value** of inventory declines with age: that is why inventory cover for perishables is days, not weeks.

### Example
A dairy sells curd with 21 days of shelf life and its retailers insist on at least 14 days remaining at delivery, so the product must be no more than **7 days old** when it reaches the store. Budget: packing and cooling at the plant 1 day, plant-to-depot transit 1 day, depot-to-store transit 1 day; leaving **3 days** for depot dwell (7 − 1 − 1 − 1). A depot holding 6 days of cover will, at the tail of its stock, deliver 10-day-old curd, which the retailer rejects. Fixes: cut depot cover to 3 days or less by replenishing daily instead of twice a week, issue strictly FEFO, and push slower-selling pack sizes to shorter-lead routes. Each rejected pallet is a full write-off of product and freight.

### In the news
See news box. Milk price changes of ₹2 per litre at Amul show how strongly the dairy chain depends on a daily flow where products cannot wait.

### Interview angle
> [!question] How it is asked
> "How do you manage a product with a 7-day shelf life across a depot network?"

> [!tip] Strong answer includes
> - Shelf-life budget by stage (plant, transit, depot, store)
> - FEFO discipline, short cycles, small lots, daily replenishment
> - Markdown and redistribution rules; waste KPI
> - Demand forecasting at SKU-store level to reduce overstock ([[004 Demand Forecasting & Planning]])

---
## 6. Amul & the Cooperative Dairy Model
> 🟠 Tier 2 · _Key points:_ three-tier cooperative, village society, daily procurement, chilling, GCMMF, farmer share

### Definition
Amul's **three-tier cooperative**: village **Dairy Cooperative Societies (DCS)** collect milk twice daily, test fat/SNF (solids-not-fat) and pay farmers by quality; **District Cooperative Milk Producers' Unions** (such as Kaira) chill, process and transport; the state **federation (GCMMF)** markets under the Amul brand. Founded in 1946 (Anand), Amul spread through **Operation Flood** (launched 1970) and now involves about 3.6 million milk producers. It supplies a daily-fresh, tightly cold-chained product: village bulk milk coolers (chill to about 4°C within hours), insulated tankers, plants for pasteurised milk, curd, butter, ghee and ice cream, and a distributor network of retailers and parlours.

Why it works as a supply chain: **assured procurement** (farmer sells every day), **transparent price formula** based on fat and SNF, **extension and inputs** (cattle feed, artificial insemination, veterinary), **vertical integration** to branded value-added products, and **scale in distribution** (a long-run share of the retail rupee returned to farmers, which Amul states is around 80% of consumer milk spend, as the company describes it). FY2025-26 numbers are in the news box.

### Example
Illustrative: a district union collects 20 lakh litres a day. Milk with 4.5% fat contains about 0.0464 kg of fat per litre (1 litre weighs about 1.03 kg). The May 2026 report says a ₹30 per kg-fat rise was 3.7%, which implies a base of about ₹811 per kg of fat (30 ÷ 0.037). So the rise adds 0.0464 × 30 = **₹1.39 per litre**; on 20 lakh litres that is ₹27.8 lakh a day, or about **₹101 crore a year**. A retail increase of ₹2 per litre on liquid milk sold (say all 20 lakh litres) brings ₹40 lakh a day, which covers the procurement rise and leaves ₹12 lakh a day towards higher feed, film and fuel costs, consistent with GCMMF's explanation. In practice not all milk is sold as liquid milk; value-added products carry different margins.

### In the news
See news box. Crossing ₹1 trillion shows how a cooperative with a daily-perishable chain scaled by combining procurement, processing and branding.

### Interview angle
> [!question] How it is asked
> "Why did Amul succeed where other agri-supply chains failed, and can the model be replicated for other crops?"

> [!tip] Strong answer includes
> - The three-tier structure with assured procurement and quality-based payment
> - Supply-chain enablers: chilling at source, daily flows, short chain, branded downstream
> - Replication limits: milk is a daily, uniform, storable-after-processing product with steady cash flow; fruit and vegetables vary by season and grade
> - Governance risks: politics, dilution of farmer control, cost pass-through

---
## 7. Contract Farming & Direct Procurement
> 🟠 Tier 2 · _Key points:_ buy-back, assured price, input support, ITC e-Choupal, risk sharing, side-selling

### Definition
**Contract farming** is an agreement between a buyer (processor, retailer, exporter) and farmers to produce to specified quality, quantity and often price, with the buyer providing seeds, inputs, credit and advice, and committing to buy. Models: **procurement only**, **centralised** (company with many contract farmers), **nucleus-estate**, **intermediary (FPO/aggregator)** and **multi-party**. India's **Model Contract Farming Act 2018** and the later Farmers (Empowerment and Protection) Agreement Act 2020 (the central farm laws were repealed in 2021) shaped the debate. Examples: **PepsiCo** potatoes for chips, **ITC e-Choupal** direct sourcing, tea and spice estates, and poultry integration.

Supply-chain benefits: consistent quality, traceable origin, planned volumes (lower buffer), and farmer income stability. Risks: **side-selling** (farmer sells to a higher spot bidder), **default** by the buyer when market prices fall (rejecting on quality grounds), unequal bargaining, and counterparty credit.

### Example
A processor contracts 2,000 tonnes of potatoes at a fixed ₹18 per kg while the spot price ranges ₹12-26. If spot rises to ₹26, a farmer who side-sells gains ₹8 per kg: on 10 tonnes, ₹80,000, so a fixed-price contract is fragile. A better design: contract price = spot price clipped to a band of ₹14 (floor) to ₹25 (cap), **plus a ₹1.5 per kg loyalty bonus** paid on delivery, with input credit deducted at delivery. At a spot of ₹26 the contract pays 25 + 1.5 = ₹26.5, above spot, so there is no reason to side-sell; at ₹12 the farmer still receives 14 + 1.5 = ₹15.5. The buyer's cost is bounded at ₹26.5 per kg, and its exposure is the bonus (₹1.5 on 2,000 tonnes = **₹30 lakh**).

### In the news
See news box. As Amul raised the procurement price by ₹30 per kg of fat for farmers, it also shows a procurement relationship working by price signalling rather than coercion.

### Interview angle
> [!question] How it is asked
> "Design a contract-farming programme for a potato chip maker and say how you prevent side-selling."

> [!tip] Strong answer includes
> - Terms: grades, delivery windows, price formula (floor, cap, index), input credit and extension
> - Risk sharing: price band, insurance, quality testing at neutral labs
> - Enforcement: relationship, bonus, aggregation through FPO, digital records
> - Fairness and compliance (state APMC and contract laws)

---
## 8. FPOs & Aggregation
> 🟠 Tier 2 · _Key points:_ FPO/FPC, 10,000 FPO scheme, aggregation, shared storage, credit

### Definition
A **Farmer Producer Organisation (FPO)** (usually a Farmer Producer Company under the Companies Act) pools small farmers to buy inputs, aggregate and grade produce, add storage and basic processing, and sell in bulk. The central scheme for **Formation and Promotion of 10,000 FPOs** (launched 2020, implemented through SFAC, NABARD and NCDC, with a budget of about ₹6,865 crore) supports handholding and equity grants. Value for supply chain: **aggregated volumes** attract institutional buyers; **shared assets** (grading, crates, cold rooms) lower unit cost; **collective credit** (warehouse receipt finance) lets farmers wait for better prices. FPOs are also named as beneficiaries of e-NAM's new value-added commodities.

Constraints: governance and skills, working capital, quality consistency, and demand linkage. The success pattern: **anchor buyer + professional CEO + one or two commodities + shared infrastructure**.

### Example
An FPO has 800 farmers with 1 hectare of vegetables each. Individually each sells 3 tonnes at ₹10 per kg through a trader taking a 15% effective cut. By aggregating 2,400 tonnes, the FPO sells to a retail chain at ₹13 per kg with a 5% FPO fee and ₹1.20 per kg for grading, crates and transport: net to farmer = 13 × 0.95 − 1.20 = **₹11.15 per kg** against 10 × 0.85 = ₹8.50: +31%. For a 3-tonne farmer, +₹7,950 per season. The FPO's own income = 5% × 13 × 2,400,000 kg = **₹15.6 lakh**, covering a manager and a clerk but not a cold room without grants.

### In the news
See news box. e-NAM's addition of FPO products such as flours and spices (February 2025) shows policy linking FPOs to digital markets.

### Interview angle
> [!question] How it is asked
> "Why do most FPOs fail to become profitable, and what supply chain linkages would help?"

> [!tip] Strong answer includes
> - Scale and working capital, not just formation, as the bottleneck
> - Anchor buyers, grading standards, and contracts
> - Shared logistics and storage; link to credit (warehouse receipts) and e-NAM
> - Professional management and clear unit economics

---
## 9. Agri-Tech Models: DeHaat, Ninjacart & Peers
> 🟠 Tier 2 · _Key points:_ full-stack, B2B fresh supply, asset-light, input marketplace, unit economics

### Definition
Indian agri-tech splits into: **input and advisory platforms** (DeHaat: seeds, fertiliser, advisory, output marketing through village-level entrepreneurs), **farm-to-business fresh supply** (Ninjacart, WayCool, Jumbotail for FMCG), **farm-to-consumer** (direct fruit and vegetable sellers), **farm-tech and fintech** (credit, crop insurance, satellite data) and **cold-chain and storage platforms**. Operating model: collect at farm-gate or village hubs, grade and crate, deliver to retailers, restaurants and quick-commerce stores with next-morning or same-day delivery.

Unit economics: gross margin per kg (sell price − buy price − wastage) must exceed **cost per kg** of collection, sorting, transport and last mile. Scale economies come from **route density** and **data on demand and price**. Many models struggle with perishable wastage (6-10% typical), thin margins and heavy working capital; asset-light variants lean on partners for storage and trucks.

### Example
A B2B fresh supplier buys vegetables at ₹20/kg and sells at ₹26/kg. Wastage 7% of buy volume (sold quantity = 0.93 of bought). Per kg bought: revenue = 0.93 × 26 = ₹24.18; cost of goods = ₹20; gross margin = **₹4.18** (17.3% of revenue). Operating costs (collection ₹1.0, sorting ₹0.6, crates ₹0.5, last-mile ₹1.4, tech and overhead ₹0.9) = ₹4.4 per kg. Net = **−₹0.22 per kg bought**: a small loss. Cutting wastage to 4% lifts revenue to 0.96 × 26 = ₹24.96, gross margin ₹4.96, net +₹0.56 per kg; at 100 tonnes a day (100,000 kg) that is ₹56,000 a day (₹16.8 lakh a month at 30 days): a thin business in which wastage control decides profit or loss.

### In the news
See news box. Ninjacart's FY25 numbers (revenue down 19% to ₹1,634 crore with a ₹256 crore loss after dropping low-margin lines) show the discipline sector players now need: shed volume that does not earn its cost.

### Interview angle
> [!question] How it is asked
> "Evaluate the unit economics of a fresh-produce B2B platform and say what it needs to break even."

> [!tip] Strong answer includes
> - Per-kg waterfall: buy, wastage, sell, logistics, overhead
> - Sensitivity: wastage, fill rate of trucks, price spread
> - Moats: farmer network, data, working-capital finance, anchor customers
> - Asset-light vs asset-heavy choice and risk of price volatility

---
## 10. MSP, Procurement & Agri Price Policy
> 🟠 Tier 2 · _Key points:_ MSP, CACP, FCI procurement, cost concepts, price volatility, stock limits

### Definition
**Minimum Support Price (MSP)** is the price at which the government stands ready to purchase listed crops; it is announced on the recommendation of the **Commission for Agricultural Costs and Prices (CACP)**, with 23 commodities covered (cereals, pulses, oilseeds and commercial crops such as cotton; sugarcane has a separate FRP). The 2018 policy set MSP at least **1.5 times the cost of production** (cost defined as **A2+FL**: paid-out costs plus imputed family labour). Procurement through **FCI** and state agencies is concentrated in wheat and paddy in a few states, so effective support for most crops and farmers is limited (a common estimate in the literature is that only a fifth to a quarter of wheat and paddy output is sold at MSP, according to Wikipedia's summary of that literature).

For supply chains MSP matters as: (a) a floor for raw-material cost for processors (cotton, pulses, edible oil), (b) a driver of cropping pattern and thus of where mills and stocks sit, (c) an input to **stock-limit, export-ban and import-duty** decisions to control consumer inflation, which add policy risk for traders and processors ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]).

### Example
A crop has A2+FL cost of ₹1,500 per quintal: MSP at 1.5× = **₹2,250**. If the mandi price falls to ₹2,000, farmers with access to procurement sell at ₹2,250 (+12.5%); the government's economic cost per quintal = MSP + handling − realised price. If handling and storage are ₹250 and the open-market sale realises ₹2,300, net cost = 2,250 + 250 − 2,300 = **₹200 per quintal**. Procuring 100 lakh quintals costs ₹200 crore net. For processors, a price floor reduces downside but raises cost when prices are high: a buyer of cotton or pulses must model MSP as a likely floor.

### In the news
See news box. e-NAM and the post-harvest finance gateway (March 2024) were built so farmers can sell above MSP-linked benchmarks by timing sales.

### Interview angle
> [!question] How it is asked
> "How does MSP affect a food processor's supply chain and what risks arise from government stock limits and export bans?"

> [!tip] Strong answer includes
> - What MSP is and its reach (few crops, few states)
> - Procurement and storage implications; policy risk (stock limits, export bans) on trade and inventory decisions
> - Hedging and contracts (formula pricing, forward sourcing, diversification of origins)
> - Alternatives: price deficiency payment, direct benefit transfer

---
## 11. Perishable Inventory: Newsvendor & Markdown Logic
> 🟠 Tier 2 · _Key points:_ underage cost, overage cost, critical ratio, service level, salvage

### Definition
For a product that expires or loses most of its value after one selling period (daily vegetables, fresh milk, bread, flowers), the **newsvendor model** picks an order quantity $Q$ to balance **underage cost** $C_u$ (profit lost per unit short = price − cost) and **overage cost** $C_o$ (loss per unit left over = cost − salvage). The optimum meets the **critical ratio**:

$$F(Q^*) = \frac{C_u}{C_u + C_o}$$

For normal demand $Q^* = \mu + z\sigma$ where $z=\Phi^{-1}(CR)$. Expected lost sales = $\sigma\,L(z)$ with the standard normal loss function $L(z)=\varphi(z)-z[1-\Phi(z)]$; expected sales = $\mu - \sigma L(z)$; expected leftover = $Q - $ expected sales. See also the derivation in [[003 Inventory Management]]. Extensions: **multiple-period perishables** (FEFO with age categories), **markdown optimisation**, **fixed shelf life with order-up-to** and **dynamic pricing** by age.

### Example
A dark store sells tomatoes: cost ₹20/kg, price ₹35/kg, salvage ₹8/kg (end-of-day discount or composting). Demand ~ Normal(mean 200 kg, sd 40 kg). $C_u = 15$, $C_o = 12$, CR = 15/27 = **0.5556**, z = 0.1397, $Q^* = 200 + 0.1397 \times 40 = $ **205.6 kg**. Expected lost sales = 40 × L(0.14) = 13.3 kg; expected sales = 186.7 kg; expected leftover = 18.9 kg; expected profit = 35 × 186.7 + 8 × 18.9 − 20 × 205.6 = **₹2,573**/day. Ordering the mean (200 kg) earns ₹2,569; ordering 180 kg earns ₹2,486; 220 kg earns ₹2,546 (differences are small near the optimum because the profit curve is flat, but the service level differs: expected fill rate at 205.6 kg is 93.3%).

### In the news
See news box. The daily milk price and procurement moves for Amul reflect a newsvendor-type tension: over-procure and you carry surplus to powder and butter; under-procure and shelves go empty.

### Interview angle
> [!question] How it is asked
> "A shop buys 200 kg of a vegetable daily at ₹20 and sells at ₹35 with salvage of ₹8. How much should it buy?"

> [!tip] Strong answer includes
> - Cu, Co, critical ratio, and z-value calculation
> - Interpretation: stock more when margin is high and salvage is high
> - Practical checks: demand distribution, shelf-life carryover, substitution
> - Link to markdown pricing and forecast improvements as ways to lift profit

---
## 12. Food Safety, FSSAI, HACCP & Traceability
> 🟠 Tier 2 · _Key points:_ FSSAI licence, HACCP, FSMS, cold chain compliance, traceability, recall

### Definition
**FSSAI** (Food Safety and Standards Authority of India) regulates under the **Food Safety and Standards Act 2006**: licensing and registration of food businesses (including warehouses, transporters and retailers), labelling, standards and testing, import clearance, and recalls. **HACCP** (Hazard Analysis and Critical Control Points) is a preventive system: identify hazards (biological, chemical, physical), set **critical control points (CCPs)** such as cooking temperature or chill-room temperature, set **critical limits**, monitor, define corrective actions, verify and keep records. Global standards: **ISO 22000**, **FSSC 22000**, **BRCGS**. FSSAI also authorises recycled content use: it granted authorisation to 17 food-grade r-PET plants (about 300,000 tonnes of capacity) in March 2026.

**Traceability**: one step back, one step forward; batch/lot codes linking raw material, process and dispatch so a recall can isolate the exact batch. Technologies: QR codes, ERP batch records, blockchain pilots, IoT temperature loggers. Cold chain compliance (for dairy, meat, seafood) includes vehicle temperature, hygiene and personnel.

### Example
A dairy plant pasteurises at 72°C for 15 seconds (critical limit) with a flow-diversion valve if temperature drops. A logger shows 70.8°C for 40 seconds on one batch of 12,000 litres: CCP deviation. Action: divert/hold the batch, retest, rework or discard; cost of discard at ₹55 per litre = **₹6.6 lakh**. Prevention (calibrated sensor, alarm) costs far less; traceability limits any recall to that one batch, not all of the week's 800,000 litres (1.5% of that week's volume).

### In the news
See news box. FSSAI's r-PET authorisations show food-safety regulation interacting with sustainability mandates (recycled content in packaging, see [[135 Reverse Logistics, Remanufacturing & EPR in India]]).

### Interview angle
> [!question] How it is asked
> "What is HACCP and how would you build traceability for a fresh-produce exporter?"

> [!tip] Strong answer includes
> - The seven HACCP principles in short; CCP and critical limit examples
> - Traceability from farm lot to shipment; digital records
> - Cold chain and hygiene compliance, audits, recall drills
> - Export standards (residue limits, GlobalG.A.P.) and the cost of rejection

---
## 13. Worked Case: A Loss-Reduction Business Case
> 🟠 Tier 2 · _Key points:_ baseline, interventions, cost-benefit, payback, KPI

### Definition
A structured method for a loss-reduction project: (1) **baseline** loss by stage (weight, value) using sampling; (2) **Pareto** of causes; (3) **intervention** options with cost and expected reduction; (4) **business case**: annual benefit = tonnes saved × net realisation per tonne; compare with annualised cost; (5) **pilot**, then scale; (6) **KPI**: loss %, quality grade mix, cost per kg, farmer price.

Typical interventions: plastic crates replacing gunny bags, **pre-cooling**, **refrigerated or insulated trucks**, **grading at source** and **direct-to-store delivery**, which skips the wholesale market.

### Example
A distributor handles 1,000 tonnes per day (300 days) of vegetables valued at ₹20 per kg at purchase cost. Baseline loss is 18%. The plan: plastic crates (assume 4 percentage points of loss reduction) and pre-cooling plus insulated vans (2 points), a total of 6 points to 12%. Annual benefit = 1,000 × 0.06 × 300 = 18,000 tonnes × ₹20 = **₹36 crore**. Costs (assumed): crates 100,000 × ₹250 = ₹2.5 crore capital, depreciated over 5 years (₹0.5 crore a year), cleaning ₹3 per crate-trip × 50,000 trips a day × 300 = ₹4.5 crore, pre-cooling and vans ₹4 crore a year: ₹9 crore a year in total. Net = **₹27 crore** a year; benefit/cost = 4.0. A sensible plan would pilot at one city, track by weighing at receipt and delivery, and only count savings after a 10% haircut (benefit ₹32.4 crore) because losses are measured imperfectly.

### In the news
See news box. At the national level, a 30-40% loss estimate means even modest reductions give large value; the example above is a single distributor's version of that.

### Interview angle
> [!question] How it is asked
> "Your client loses 18% of produce between farm and store. Build the case to cut it to 12%."

> [!tip] Strong answer includes
> - Baseline by stage, causes, and an assumptions list
> - Costed interventions with expected impact and payback
> - Sensitivity (what if only half the benefit arrives?) and pilot plan
> - Metrics and governance so benefits are actually captured ([[026 Case Interview — Operations Cases]])

---
## 14. ⭐ Advanced: Price Volatility, Trade Policy & Network Design for Fresh
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Fresh-produce prices swing sharply (onion, tomato, potato) because supply is seasonal, demand is inelastic and storage is limited; the government responds with **stock limits, export bans or duties, buffer-stock releases and import-duty cuts**. For a processor, retailer or exporter the decisions are: **how much to contract versus buy spot**, **where to store**, and **where to place consolidation hubs**.

A fresh-produce network usually has **village collection points** → **cluster hubs with pre-cooling and grading** → **city DCs/dark stores**. Tools: **facility-location** and **vehicle routing** models ([[113 Network Design & Facility Location Modelling]], [[125 Transportation Management Deep Dive]]) with time-window constraints (maximum hours from harvest to cooling), shelf-life constraints and seasonality. A key trade-off is **transport cost vs spoilage cost**: more hubs lower transport time but raise fixed cost.

### Example
Two hub options for a 200-tonne/day vegetable flow (6,000 tonnes a month, value ₹20 per kg). **Option A**: one hub 120 km from farms, transit 4 hours, loss 6%, transport ₹1.40 per kg, fixed cost ₹25 lakh a month. **Option B**: three hubs averaging 40 km, transit 1.5 hours, loss 3%, transport ₹0.70 per kg, fixed cost ₹60 lakh a month. A: spoilage 6,000,000 × 6% × 20 = ₹72 lakh; transport ₹84 lakh; fixed ₹25 lakh: total **₹181 lakh**. B: spoilage ₹36 lakh; transport ₹42 lakh; fixed ₹60 lakh: total **₹138 lakh**. B saves ₹43 lakh a month: the combined spoilage and transport saving (₹36 + ₹42 = ₹78 lakh) exceeds the extra fixed cost (₹35 lakh). If volume halves, savings fall to ₹39 lakh against ₹35 lakh of extra fixed cost, so B barely breaks even: hub count should follow volume.

### In the news
See news box. Policy-driven shocks to farm-gate and mandi prices (stock limits, export curbs, duty changes) are a reminder that network and contract design must tolerate sudden rule changes; the milk-price and procurement-price moves in the news box show cost pass-through under a similar pressure.

### Interview angle
> [!question] How it is asked
> "The government has banned onion exports. As head of supply chain at an exporter, what do you do?"

> [!tip] Strong answer includes
> - Immediate: protect committed orders, redirect to domestic or processed channels, renegotiate
> - Medium term: diversify products and markets, contract with farmers on flexible terms, storage and processing
> - Scenario planning with rule-change probability; policy engagement
> - Cost-of-capital trade-offs in holding stock versus selling
