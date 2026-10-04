---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Logistics & Distribution"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 15
---
# Logistics & Distribution

⬅ [[008 Six Sigma & Quality Tools]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[010 Warehouse Management]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Transportation Modes]]
2. [[#2. Incoterms 2020]]
3. [[#3. Freight Costing]]
4. [[#4. Warehouse Management System (WMS)]]
5. [[#5. Cross Docking]]
6. [[#6. Last Mile Delivery]]
7. [[#7. Cold Chain Logistics]]
8. [[#8. Reverse Logistics]]
9. [[#9. 3PL / 4PL Models]]
10. [[#10. Route Optimization]]
11. [[#11. Network Optimization]]
12. [[#12. Port & Customs Operations]]
13. [[#13. Distribution KPIs]]
14. [[#14. ⭐ Advanced: Total Landed Cost]]
15. [[#15. ⭐ Advanced: India's Logistics Ecosystem and Reform Levers]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's logistics cost resets to ~8% of GDP, while the Red Sea reroutes world shipping
> **NCAER puts India's logistics cost at 7.97% of GDP (FY2023-24; published 2025).** The National Council of Applied Economic Research's "Assessment of Logistics Cost in India" (hybrid of user/provider surveys and government data) estimates total logistics cost at **7.97% of GDP, about ₹24.01 lakh crore**, far below the "13–14% of GDP" figure commonly cited from external studies (Commerce Minister Piyush Goyal's framing). Average cost per tonne-km: rail **₹1.96**, air **₹72**. ([ITLN](https://www.itln.in/logistics/indian-logistics-costs-at-797-of-gdp-new-study-reveals-1356654))
>
> **Red Sea / Suez rerouting (from late 2023, through 2024).** Per Maersk (July 2024), Suez crossings fell about **66%** (the canal normally carries ~12% of global trade), the Cape route lengthened average cargo travel distance by about **9%**, and available shipping capacity fell **15–20% in Q2 2024**; effects included higher fuel use and freight rates, port congestion and equipment shortages. ([Maersk](https://www.maersk.com/insights/resilience/2024/07/09/effects-of-red-sea-shipping))
>
> **Quick commerce densifies the last mile (Dec 2024 – FY26).** HSBC Global Research expected India's quick-commerce chains to reach **5,000–5,500 dark stores by FY2025-26** (Blinkit 1,000+ in the Dec-2024 quarter, Zepto ~850, Swiggy Instamart heading to 1,000), with gross order value of **$35–40 bn by FY2027-28**. ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/indias-quick-commerce-landscape-to-transform-with-5000/486062))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Transportation Modes
> 🔴 Tier 1 · _Tracker hint:_ Road, rail, air, sea, pipeline — cost/speed/capacity trade-offs

### Definition
Five modes, each with a distinct cost-speed-capacity-reliability profile:

| Mode | Cost per tonne-km | Speed | Capacity | Flexibility | Best for |
|---|---|---|---|---|---|
| **Road** | Medium | Medium | Low-medium | Highest (door-to-door) | Short/medium haul, FMCG, last mile |
| **Rail** | Low | Slow-medium | High | Low (fixed lines, terminals) | Bulk, containers, long haul |
| **Sea (waterways)** | Lowest | Slowest | Very high | Low (ports) | International trade, bulk, containers |
| **Air** | Highest | Fastest | Low | Medium (airports) | High-value, urgent, perishable |
| **Pipeline** | Very low (once built) | Slow, continuous | Fixed | None | Crude oil, gas, products |

**Intermodal** (containers moved by several modes without handling the cargo) combines strengths (rail for the long haul, road for first/last mile). Selection criteria: value density, urgency, volume, shelf life, reliability, damage risk, carbon footprint (emissions per tonne-km: air $\gg$ road $>$ rail $>$ sea). The **cost vs inventory trade-off**: a faster mode raises freight but lowers in-transit inventory and safety stock.

### Example
Using NCAER's national averages (rail ₹1.96, air ₹72 per tonne-km), moving 10 tonnes over 1,400 km: rail $= 10 \times 1{,}400 \times 1.96 = ₹27{,}440$; air $= 10 \times 1{,}400 \times 72 = ₹10{,}08{,}000$, about 37 times as much. Air makes sense only if the goods' value or the cost of a stock-out justifies it (e.g. ₹5 crore of electronics with a launch deadline).

### In the news
See news box. NCAER's rail-vs-air gap per tonne-km illustrates why India's policy pushes freight from road to rail and waterways; the Red Sea shows a sea route's weakness: reliability.

### Interview angle
> [!question] How it is asked
> "Which mode would you use to ship X from Mumbai to Delhi?" or "How do you choose between sea and air for a time-sensitive consignment?"

> [!tip] Strong answer includes
> - Decision criteria: value, urgency, volume, distance, reliability, shelf life
> - Cost vs inventory trade-off (faster mode cuts pipeline stock)
> - Intermodal option and a numeric comparison
> - India context: road dominates, rail/DFC share is policy-targeted

---

## 2. Incoterms 2020
> 🔴 Tier 1 · _Tracker hint:_ EXW, FOB, CIF, DDP, DAP — risk & cost transfer points

### Definition
**Incoterms** (ICC) are standard trade terms that fix **who pays for what** (freight, insurance, duties) and **where risk transfers** from seller to buyer. Incoterms 2020 has **11 terms**:

| Any mode | Sea/inland waterway only |
|---|---|
| **EXW** Ex Works, **FCA** Free Carrier, **CPT** Carriage Paid To, **CIP** Carriage and Insurance Paid To, **DAP** Delivered at Place, **DPU** Delivered at Place Unloaded (replaced DAT), **DDP** Delivered Duty Paid | **FAS** Free Alongside Ship, **FOB** Free On Board, **CFR** Cost and Freight, **CIF** Cost, Insurance and Freight |

Key points:
- **EXW**: minimum seller duty; buyer bears nearly everything from the seller's door.
- **FOB**: seller delivers goods **on board** the vessel at the named port; risk passes on loading; buyer pays main freight.
- **CIF**: seller pays freight and minimum insurance to the destination port, but **risk still passes at loading** (cost and risk points differ). In 2020, CIP requires higher cover (Institute Cargo Clauses A) while CIF stays at Clause C.
- **DAP**: seller delivers to named destination, ready for unloading; buyer clears import.
- **DDP**: maximum seller duty, including import duty and clearance.
Incoterms do not cover transfer of title, payment terms or contract law.

### Example
Indian exporter: EXW price ₹100. FOB Mumbai $= 100 + 4$ (inland haulage) $+ 1$ (export clearance) $+ 3$ (terminal/loading) $= 108$. CIF Rotterdam $= 108 + 10$ (ocean freight) $+ 1$ (insurance) $= 119$. Under FOB, the buyer carries risk from the moment the goods are on board; under CIF the seller pays for the insurance, but the buyer still bears the transit risk (and claims on the policy).

### In the news
See news box. When ships diverted around the Cape, FOB/CIF buyers and sellers disputed who pays for extra freight and delay; contracts with CIF/CFR leave the freight risk with the seller but the loss risk with the buyer.

### Interview angle
> [!question] How it is asked
> "What is the difference between FOB and CIF?" or "Which Incoterm would you choose as an exporter/importer?"

> [!tip] Strong answer includes
> - The 11 terms in two groups; risk vs cost transfer points
> - FOB vs CIF distinction (risk at loading in both)
> - Choose by control: buyers wanting control prefer FOB/FCA; sellers wanting simplicity may quote DAP/DDP but take customs risk
> - Note: use FCA for containers (risk passes at the terminal, not on board)

---

## 3. Freight Costing
> 🔴 Tier 1 · _Tracker hint:_ LTL vs FTL, freight rate components, fuel surcharges

### Definition
**FTL (full truckload)** dedicates a whole vehicle to one shipper: price per trip (₹/km or lane rate), regardless of load. **LTL (less than truckload)** shares space: price per kg/pallet/CBM, plus hub handling; slower and more handling damage, but economical for small volumes. Also **part-load** (common in India), parcel/courier, and **FCL vs LCL** for sea containers.

**Rate components:** base line-haul (distance/weight/volume, **chargeable weight** $= \max$(actual, volumetric)), fuel surcharge (often indexed to diesel), accessorials (detention, loading/unloading, tolls, handling, ODA charges), insurance/risk, taxes (GST on freight), peak-season surcharges. Air chargeable weight: volumetric $= \dfrac{L \times W \times H\ (\text{cm})}{6000}$ kg.

**Break-even load** between FTL and LTL: $Q^* = \dfrac{FTL\ rate}{LTL\ rate\ per\ tonne}$.

### Example
FTL ₹30,000 for a 20-tonne truck; LTL ₹1,800 per tonne. $Q^* = 30{,}000 / 1{,}800 = 16.7$ t (83% of capacity); above that ship FTL. With an 8% fuel surcharge the FTL becomes $30{,}000 \times 1.08 = ₹32{,}400$ and break-even shifts to $32{,}400/1{,}800 = 18$ t if the surcharge applies only to FTL.

### In the news
See news box. Longer Red Sea routings pushed up fuel use and rates; fuel-linked surcharges are how carriers pass diesel and route costs to shippers.

### Interview angle
> [!question] How it is asked
> "When should a company move from LTL to FTL?" or "A client's freight cost per kg is rising. Diagnose."

> [!tip] Strong answer includes
> - Rate components and chargeable weight (volumetric vs actual)
> - Break-even calculation and consolidation (milk run, pooling)
> - Drivers of cost increase: load factor, lane mix, surcharges, detention
> - Levers: consolidate, multi-modal, renegotiate with lane-wise tenders

---

## 4. Warehouse Management System (WMS)
> 🔴 Tier 1 · _Tracker hint:_ Receiving, putaway, picking, packing, shipping modules

### Definition
A **WMS** is software that directs and records warehouse operations in real time and holds the inventory by **location, lot/batch, serial, status**. Core flow:
1. **Receiving**: ASN/PO match, quality check, GRN.
2. **Putaway**: system-directed location by rules (velocity/ABC, size, temperature, FEFO for perishables).
3. **Storage and replenishment**: bin management, cycle counting, slotting.
4. **Picking**: discrete, batch, zone, wave, cluster picking; RF/voice/pick-to-light; pick path optimisation.
5. **Packing**: verification, cartonisation, labelling.
6. **Shipping**: loading, documents, carrier integration, yard management.
Plus **returns, labour management, cross-docking, 3PL billing**, integration with ERP/TMS/OMS. Types: standalone, ERP module, cloud, with automation (AS/RS, AMR) via WES.

KPIs: dock-to-stock time, pick accuracy ($\text{correct lines}/\text{total lines}$), lines per labour hour, order cycle time, inventory accuracy, space utilisation.

### Example
A DC picks 20,000 lines a day. Moving from paper picking (98.5% accuracy) to RF scan with a WMS (99.9%): errors fall from $300$ to $20$ lines a day. At ₹400 per error (re-pick, return, credit), saving $= 280 \times 400 = ₹1.12$ lakh a day.

### In the news
See news box. Quick-commerce dark stores run on WMS logic (slotting, directed picks, minutes-level SLAs) at small scale.

### Interview angle
> [!question] How it is asked
> "What does a WMS do?" or "How would you reduce picking errors and cycle time in a DC?"

> [!tip] Strong answer includes
> - The six process blocks with the logic of each
> - Directed putaway, slotting by velocity, picking strategy
> - KPIs and a quantified benefit
> - Integration (ERP, TMS) and when automation is justified

---

## 5. Cross Docking
> 🔴 Tier 1 · _Tracker hint:_ Direct transfer without storage; JIT supply, perishables

### Definition
**Cross-docking** moves inbound goods directly to outbound vehicles with little or no storage, typically **under 24 hours**. The facility is a **flow-through terminal**, not a warehouse.

Types: **Pre-distribution** (goods pre-allocated to stores by the supplier: ready to move) and **post-distribution** (allocation decided at the dock). Variants: continuous, consolidation (many suppliers to one customer), deconsolidation, opportunistic.

Enablers: accurate ASN/advance information, synchronised arrivals/departures, labelling/barcodes, suitable dock layout. Benefits: lower inventory, handling and storage cost, faster delivery, fresher perishables, higher truck fill. Limits: needs reliable suppliers and information, tight scheduling, and sufficient volume; no buffer against variability.

### Example
A hub handles 1,000 pallets a day. With a conventional warehouse dwell of 5 days, on-hand $= 1{,}000 \times 5 = 5{,}000$ pallets (Little's Law). With cross-docking, dwell 0.5 day: $500$ pallets, 90% less space and inventory. Walmart's use of cross-docking is the standard case.

### In the news
See news box. Higher uncertainty in lead times (Red Sea) makes pure cross-docking riskier, so networks keep some buffer stock alongside flow-through operations.

### Interview angle
> [!question] How it is asked
> "Why would a grocery retailer use cross-docking? What are the risks?"

> [!tip] Strong answer includes
> - Definition (no storage, less than 24 h), and pre- vs post-distribution
> - Where it fits: high-volume, predictable, perishable
> - Conditions: information sharing, synchronisation
> - Risks: variability, missed connections, dock congestion

---

## 6. Last Mile Delivery
> 🔴 Tier 1 · _Tracker hint:_ Cost structures, route optimization, BOPIS, micro-fulfillment

### Definition
**Last mile** is the final leg from a local hub or store to the customer; it is the **most expensive and least efficient** part of delivery, often cited at roughly 40–50% of total delivery cost (a rule of thumb, varying by market).

**Cost drivers:** drop density (stops per route), failed deliveries, time windows, traffic, vehicle type (bike, van, EV), labour (gig vs employed), returns, speed promise. Cost per drop $= \dfrac{\text{route cost}}{\text{successful drops}}$.

**Models:** hub-and-spoke from a sorting centre; **BOPIS/click-and-collect** (customer picks up, trading convenience for cost); **parcel lockers/pick-up points**; **ship-from-store**; **dark stores / micro-fulfilment centres (MFC)** for 10–30 minute delivery; crowd-sourced/gig riders; drones/robots (pilots). Tools: route optimisation, slot management, delivery-time prediction, proof of delivery, NDR (non-delivery report) workflows.

### Example
A van route costs ₹1,200. With 40 drops: ₹30 per drop; with 60 drops (better clustering, delivery slots): ₹20, a 33% saving. A first-attempt failure rate of 10% adds re-delivery: for 40 planned drops, 4 re-attempts at ₹30 = ₹120 extra a route (+10%).

### In the news
> [!news] Dark stores and the 10-minute promise (Dec 2024 – FY28 outlook)
> HSBC Global Research (as reported by Entrepreneur India) expected **5,000–5,500 dark stores by FY2025-26** across Blinkit (1,000+ in the Dec-2024 quarter), Zepto (~850) and Swiggy Instamart (heading to 1,000), and gross order value of **$35–40 bn by FY2027-28**, after which players move from expansion to optimising capacity. Dense micro-nodes are how these firms cut last-mile distance. ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/indias-quick-commerce-landscape-to-transform-with-5000/486062))

### Interview angle
> [!question] How it is asked
> "How would you reduce last-mile cost for an e-commerce company?" or "Is quick commerce sustainable?"

> [!tip] Strong answer includes
> - Cost drivers framed as drop density, first-attempt success, speed promise
> - Levers: clustering and routing, slots, pick-up points/BOPIS, micro-fulfilment, return-to-origin policy
> - Unit economics: cost per order vs average basket value
> - Trade-off between speed and cost; service tiers

---

## 7. Cold Chain Logistics
> 🔴 Tier 1 · _Tracker hint:_ Temperature-controlled, pharma & food applications, break-of-cold

### Definition
A **cold chain** is an unbroken, temperature-controlled supply chain from producer to consumer: pre-cooling, cold storage, reefer transport, cold-room hubs, last-mile insulated delivery. Typical ranges: **chilled 0–8°C** (dairy, fruit, vegetables), **vaccines 2–8°C**, **frozen about −18°C** (meat, ice cream), **ultra-cold −60°C or below** (some mRNA vaccines, biologics), and **controlled room temperature 15–25°C** for many pharmaceuticals.

**Break of cold** (temperature excursion) occurs when the product leaves its range, such as at hand-offs (loading dock, airport tarmac, customs holds, door-open stops). Controls: pre-cooled reefers, data loggers/IoT sensors with alerts, validated packaging (PCM gel packs, dry ice), qualified lanes, SOPs and **GDP (Good Distribution Practice)** compliance, backup power, **FEFO** inventory.

Cost is typically several times that of ambient logistics because of equipment, energy and monitoring. Metrics: excursion rate, shelf-life remaining on delivery, wastage %, reefer utilisation.

### Example
Illustrative: a vaccine consignment worth ₹2 crore with an excursion rate of 1% of shipments and total loss on affected shipments loses ₹2 lakh per ₹2 crore moved, i.e. $0.01 \times 2$ crore $= ₹2$ lakh. A ₹1 lakh IoT logging and rerouting programme that halves excursions pays back ($0.5 \times 2$ lakh $= ₹1$ lakh a year per ₹2 crore flow) in one year.

### In the news
See news box. Rerouting and delays on long sea voyages are most damaging to perishables and temperature-sensitive cargo, where extra transit days reduce remaining shelf life and increase excursion risk.

### Interview angle
> [!question] How it is asked
> "Design the cold chain for a vaccine/fresh-produce distributor in India."

> [!tip] Strong answer includes
> - Temperature ranges per product and the full chain (pre-cooling to last mile)
> - Break-of-cold points and monitoring
> - Cost-risk trade-off, wastage and compliance (GDP)
> - India issues: power reliability, fragmented infrastructure, high post-harvest loss

---

## 8. Reverse Logistics
> 🔴 Tier 1 · _Tracker hint:_ Returns management, remanufacturing, recycling, WEEE

### Definition
**Reverse logistics** moves goods from the customer back upstream for return, repair, reuse, remanufacturing, recycling or disposal. Drivers: e-commerce returns, warranty, recalls, end-of-life regulation, circular economy, recovery of value.

Process: **return authorisation (RMA)** → collection → receiving and **grading/inspection** → **disposition** (restock, refurbish, repair, remanufacture, resell via liquidation or secondary market, recycle, scrap) → financial settlement. Hierarchy of value recovery: reuse > repair > refurbish/remanufacture > recycle > landfill.

**WEEE** (Waste Electrical and Electronic Equipment) rules require producers to take responsibility for e-waste (Extended Producer Responsibility, EPR); India's E-Waste (Management) Rules, 2022 (effective April 2023) set EPR targets for producers. Challenges: forecasting returns, reverse flows are small and scattered, fraud/abuse, grading speed, high handling cost.

### Example
10,000 online fashion orders, 20% returned: 2,000 returns. Handling and two-way shipping cost ₹250 each $= ₹5$ lakh. If 80% can be resold at full margin and 20% only at a ₹300 loss: loss $= 400 \times 300 = ₹1.2$ lakh, plus ₹5 lakh cost, so about ₹6.2 lakh, or ₹62 per order shipped. Cutting the return rate to 15% saves $500 \times 250 = ₹1.25$ lakh in handling alone.

### In the news
See news box. Quick commerce and e-commerce returns pressure dark-store and fulfilment-centre economics: every return reuses the same expensive last-mile network.

### Interview angle
> [!question] How it is asked
> "How would you reduce returns and recover value for an online electronics retailer?"

> [!tip] Strong answer includes
> - Root causes of returns (size/fit, damage, wrong item) and prevention
> - Disposition tree and recovery hierarchy
> - Economics: cost of return, resale value, speed of processing
> - EPR/WEEE compliance and circular-economy angle

---

## 9. 3PL / 4PL Models
> 🔴 Tier 1 · _Tracker hint:_ 3PL = outsourced execution; 4PL = managed services/orchestration

### Definition
- **1PL**: shipper does its own logistics. **2PL**: asset-based carrier (truck, ship, airline).
- **3PL (third-party logistics)**: outsources execution (transport, warehousing, freight forwarding, value-added services) to a provider; contracts can be dedicated, shared, or on a cost-plus/transactional basis.
- **4PL (fourth-party / lead logistics provider)**: an integrator that **designs, manages and orchestrates** multiple 3PLs, technology and the whole supply chain for the client, usually non-asset-based, with gain-share contracts.
- **5PL**: platform/e-marketplace aggregating logistics (concept in digital marketplaces).

Make-or-buy: outsource when logistics is non-core, volume is variable, capital or expertise is lacking, or geographic reach is needed. Risks: loss of control, dependence, hidden costs, data/IP, service failure. Governance: SLAs/KPIs (OTIF, damage, dwell), QBRs, open-book costing, exit clauses.

### Example
In-house: fixed ₹60 lakh a year plus ₹100 per shipment. 3PL: ₹250 per shipment. Break-even $= 60{,}00{,}000 / (250 - 100) = 40{,}000$ shipments a year. Below that, outsource; above, in-house is cheaper (before service and risk considerations).

### In the news
See news box. NCAER's lower, better-measured logistics cost figure and Red Sea disruptions both raise the value of providers that can offer multi-modal options, visibility and re-planning.

### Interview angle
> [!question] How it is asked
> "Should a mid-size FMCG company outsource its logistics?" or "3PL vs 4PL?"

> [!tip] Strong answer includes
> - Definitions with who owns assets and decisions
> - Make-or-buy economics with a break-even and non-cost criteria
> - Contract and KPI governance, gain-share
> - Risks and mitigations (dual providers, exit plan, data access)

---

## 10. Route Optimization
> 🔴 Tier 1 · _Tracker hint:_ TSP, VRP, Clarke-Wright algorithm, real-time re-routing

### Definition
- **TSP (travelling salesman problem)**: shortest tour visiting each stop once and returning to start. NP-hard.
- **VRP (vehicle routing problem)**: serve customers from a depot with a fleet minimising total cost. Variants: **CVRP** (capacity), **VRPTW** (time windows), pickup-delivery, multi-depot, heterogeneous fleet.
- **Clarke-Wright savings algorithm** (constructive heuristic):
  1. Start with each customer served by its own route (depot-$i$-depot).
  2. Compute savings $s_{ij} = d_{0i} + d_{0j} - d_{ij}$ for every pair.
  3. Sort savings descending; merge routes in that order when capacity and time constraints allow, and $i$, $j$ are route ends.
- Other heuristics/metaheuristics: nearest neighbour, sweep, 2-opt, tabu search, genetic algorithms, OR-tools solvers.
- **Real-time re-routing** uses live traffic, order insertion, ETAs, and dynamic dispatch.

Objectives: distance, time, cost, emissions, fairness of workloads, SLA adherence.

### Example
Depot 0, customers A, B, C: $d_{0A} = 10$, $d_{0B} = 12$, $d_{0C} = 8$; $d_{AB} = 5$, $d_{AC} = 9$, $d_{BC} = 11$. Separate routes: $2 \times (10 + 12 + 8) = 60$. Savings: $s_{AB} = 10 + 12 - 5 = 17$; $s_{BC} = 12 + 8 - 11 = 9$; $s_{AC} = 10 + 8 - 9 = 9$. Merge A-B first: route $0\text{-}A\text{-}B\text{-}0 = 27$. Add C via $s_{BC}$ (capacity permitting): $0\text{-}A\text{-}B\text{-}C\text{-}0 = 10 + 5 + 11 + 8 = 34$, saving $60 - 34 = 26 = 17 + 9$.

### In the news
See news box. Dark-store and delivery fleets rely on dynamic dispatch and re-routing at minute-level; at sea, carriers re-routed whole services around the Cape.

### Interview angle
> [!question] How it is asked
> "A delivery company has 200 drops a day and 15 vehicles. How would you plan routes?"

> [!tip] Strong answer includes
> - TSP vs VRP and constraints (capacity, time windows)
> - Clarke-Wright savings logic with a small numeric illustration
> - Beyond distance: time windows, driver hours, service times
> - Dynamic re-routing and data needs (GPS, traffic, order data)

---

## 11. Network Optimization
> 🔴 Tier 1 · _Tracker hint:_ Hub location, spoke design, multi-echelon distribution

### Definition
Choosing the **number, location and role** of plants, DCs, hubs and cross-docks, and assigning customers, to minimise total cost for a service level.

Methods:
- **Centre of gravity**: $x^* = \dfrac{\sum w_i x_i}{\sum w_i}$, $y^* = \dfrac{\sum w_i y_i}{\sum w_i}$ (weights = volumes), a first-cut location.
- **Facility location MIP** (fixed charge): minimise $\sum f_j y_j + \sum c_{ij} x_{ij}$ with demand and capacity constraints.
- **Hub-and-spoke vs point-to-point**: hubs consolidate flows (fewer links, higher load factor, extra handling/distance).
- **Multi-echelon**: plant → central warehouse → regional DC → store; inventory placed at the right echelon; the **square-root law**: safety stock $\propto \sqrt{n}$ for $n$ locations.
Trade-offs: more nodes mean lower transport and faster service but higher fixed and inventory cost. Include tax (GST), customs, risk and resilience. See [[001 SCM Introduction & Fundamentals]].

### Example
Demand points: A (0, 0) 100 t; B (10, 0) 200 t; C (0, 10) 100 t. $x^* = (0 \cdot 100 + 10 \cdot 200 + 0 \cdot 100)/400 = 5$; $y^* = (0 + 0 + 10 \cdot 100)/400 = 2.5$. Candidate hub at (5, 2.5). Consolidating 4 regional DCs into 1 cuts safety stock by about 50% ($1/\sqrt{4}$) but lengthens outbound distance.

### In the news
See news box. The shift of electronics assembly toward India and the Red Sea disruption both forced network redesign: new nodes, alternative corridors and more buffer stock.

### Interview angle
> [!question] How it is asked
> "Where should we build a new warehouse for pan-India distribution?" or "How many DCs do we need?"

> [!tip] Strong answer includes
> - Data request: demand by location, costs, service targets
> - Cost trade-off curve (transport vs inventory vs facilities) and the square-root law
> - Centre of gravity then optimisation model; scenario tests (growth, disruption)
> - Non-cost: GST/state taxes, land, labour, risk

---

## 12. Port & Customs Operations
> 🔴 Tier 1 · _Tracker hint:_ Bill of lading, customs clearance, HS codes, duties

### Definition
**Bill of Lading (B/L)**: issued by the carrier; it is (1) a **receipt** for goods, (2) **evidence of the contract of carriage**, and (3) a **document of title** (if negotiable "to order"), enabling transfer of goods and use in letters of credit. Types: straight, order, **telex/electronic**, house vs master. Air equivalent: Air Waybill (non-negotiable).

**Customs clearance (India):** importer files a **Bill of Entry** (exports: **Shipping Bill**) electronically (ICEGATE); assessment (self-assessed), duty payment, examination if selected by risk management, then **out-of-charge**. Documents: commercial invoice, packing list, B/L/AWB, certificate of origin, licences.

**HS code** (Harmonized System, 6-digit international, India uses 8-digit ITC-HS) classifies goods and determines duty rates and regulations. Duties: Basic Customs Duty (BCD), Social Welfare Surcharge (SWS), **IGST** on the assessable value plus duties; anti-dumping, safeguard duties where notified. Port operations: vessel berthing, discharge, **container freight stations (CFS)**, **ICDs**, dwell time, demurrage and detention charges. Programmes: AEO (Authorised Economic Operator) for faster clearance.

### Example
Illustrative rates: CIF value ₹10,00,000; BCD 10% $= ₹1{,}00{,}000$; SWS 10% of BCD $= ₹10{,}000$; IGST 18% on $(10{,}00{,}000 + 1{,}00{,}000 + 10{,}000) = 11{,}10{,}000$ gives $₹1{,}99{,}800$. Total duty $= 1{,}00{,}000 + 10{,}000 + 1{,}99{,}800 = ₹3{,}09{,}800$, i.e. 31% of CIF. Misclassifying the HS code changes the BCD rate, and so the whole landed cost. (Actual rates vary by HS code and notifications.)

### In the news
See news box. Port and canal disruptions bring congestion, container imbalances and detention costs; faster customs and port dwell times are a stated pillar of India's logistics-cost reduction effort.

### Interview angle
> [!question] How it is asked
> "What documents are needed to import goods? What does a Bill of Lading do?"

> [!tip] Strong answer includes
> - B/L's three functions and its role in finance
> - Import steps: Bill of Entry, assessment, duty, examination, out-of-charge
> - HS classification and duty-stack arithmetic
> - Hidden costs: demurrage, detention, CFS charges, and how to cut dwell time

---

## 13. Distribution KPIs
> 🔴 Tier 1 · _Tracker hint:_ OTIF, delivery accuracy%, cost per shipment, load factor%

### Definition
| KPI | Formula |
|---|---|
| **OTIF** | Orders delivered on time and in full / total orders |
| **On-time delivery %** | Deliveries by promised time / total deliveries |
| **Delivery accuracy %** | Orders with the right item, quantity and place / total orders |
| **Fill rate** | Units shipped from stock / units ordered |
| **Cost per shipment / per tonne-km** | Total transport cost / shipments (or tonne-km) |
| **Load factor %** | Actual load / vehicle capacity (weight or volume) |
| **Vehicle utilisation** | Productive hours (or km) / available |
| **Order cycle time** | Order to delivery |
| **Damage / claims %** | Damaged orders / total |
| **Perfect order** | On time x in full x damage-free x correct documents |
| **Logistics cost % of sales** | Logistics cost / revenue |

OTIF is stringent: an order counts only if it is both on time and in full, so OTIF is never higher than either rate alone. Balance **cost** and **service** KPIs and measure by lane/customer/carrier to find the issue.

### Example
1,000 orders: 920 on time; of those 880 also in full. $OTIF = 880/1000 = 88\%$ (on-time 92%). A truck carries 14 t on a 20 t vehicle: load factor 70%; filling to 18 t raises it to 90% and cuts cost per tonne by $1 - 14/18 = 22\%$ on the same trip cost. If trip cost is ₹30,000: ₹2,143 per tonne vs ₹1,667.

### In the news
See news box. Retail and FMCG customers' OTIF fines, and the sharp fall in schedule reliability from Red Sea diversions, put these KPIs on the boardroom agenda.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track for a distribution network?" or "OTIF has fallen to 85%. What do you do?"

> [!tip] Strong answer includes
> - A balanced scorecard: service (OTIF, accuracy), cost (per shipment, % of sales), asset (load factor, utilisation)
> - Split OTIF into on-time and in-full, by lane, DC, carrier, SKU
> - Root-cause path: forecast, stock-outs, dock scheduling, carrier performance
> - Targets, owners, review cadence

---

## 14. ⭐ Advanced: Total Landed Cost
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Total landed cost (TLC)** is the full cost to get a product into your warehouse (or to the customer), not just the invoice price:

$$TLC = \text{Product price} + \text{Freight} + \text{Insurance} + \text{Duties and taxes} + \text{Handling and clearance} + \text{Inventory carrying cost} + \text{Other (risk, quality, FX)}$$

**Inventory carrying cost** of the extra in-transit/safety stock $= \text{Value} \times \text{holding rate} \times \dfrac{\text{lead time (days)}}{365}$ (for pipeline stock), plus safety stock buffers for longer, less reliable lanes. Hidden items: demurrage, rejects, expedite costs, minimum order quantities, payment terms (financing).

Use TLC for **sourcing and network decisions** (near-shoring vs offshoring), mode choice and make-vs-buy. Sensitivity analysis: oil price, freight volatility, exchange rate, duty changes.

### Example
Per unit: Supplier X (nearby): price ₹100, freight 8, insurance 1, duty 10, handling 3, carrying 4 $= ₹126$. Supplier Y (far, cheaper): price ₹92, freight 20, insurance 2, duty 10, handling 3, carrying 9 $= ₹136$. The "cheaper" supplier is 8% costlier landed ($136/126 = 1.079$) and also less reliable.

### In the news
See news box. After the Red Sea reroutes added transit distance and capacity pressure, landed cost comparisons shifted toward nearer sources for many importers.

### Interview angle
> [!question] How it is asked
> "Supplier A is 8% cheaper than supplier B. Would you switch?"

> [!tip] Strong answer includes
> - TLC components beyond price
> - Quantified comparison (as above) and sensitivity to freight and lead time
> - Risk and quality costs; supplier reliability
> - Decision: choose lowest TLC at acceptable risk, not lowest price

---

## 15. ⭐ Advanced: India's Logistics Ecosystem and Reform Levers
> ⭐ Advanced · _Added beyond the tracker_

### Definition
India-specific building blocks that frequently appear in consulting and operations cases:
- **GST and e-way bill**: GST removed most state-border check posts and shifted warehousing decisions from tax-driven to cost-driven (hub consolidation). The **e-way bill** is required for movement of goods above a threshold value (₹50,000 for most consignments).
- **FASTag**: electronic toll collection (mandatory for four-wheelers and above since 2021) cutting toll waiting time.
- **Dedicated Freight Corridors (DFC)**: Eastern and Western corridors for faster, higher-capacity freight trains.
- **PM Gati Shakti** (launched 2021) and the **National Logistics Policy** (September 2022): integrated planning of infrastructure, and the target of bringing logistics cost down to global benchmarks; the **Unified Logistics Interface Platform (ULIP)** integrates government data.
- **Modal mix**: road carries the majority of freight in India; policy aims to raise rail and coastal/waterway shares.
- **Multimodal logistics parks**, warehousing standards, and the move from fragmented operators to organised 3PLs.
Measurement matters: NCAER's 7.97% of GDP (FY2023-24) corrects older 13–14% estimates, so always cite the source and definition.

### Example
A beverage company with 22 state-wise warehouses (pre-GST pattern) consolidates to 8 regional DCs. Safety stock falls to about $\sqrt{8/22} = 60\%$ of the earlier level (a 40% cut), assuming equal demand per node. Outbound distances rise, so check the service level, and use rail for the middle mile.

### In the news
See news box. NCAER's 7.97% figure is the most recent official-style benchmark; the Red Sea disruption is a reminder that India's external corridors are as important as domestic ones.

### Interview angle
> [!question] How it is asked
> "India's logistics cost is high relative to GDP. What would you do about it?" (a typical policy or market-entry case)

> [!tip] Strong answer includes
> - Cost drivers: modal mix, fragmentation, dwell time, empty running, documentation
> - Levers: DFC/rail share, multimodal hubs, digitisation (e-way bill, FASTag, ULIP), warehouse consolidation, 3PL organisation
> - Mention the measurement debate (7.97% vs 13–14%) to show rigour
> - Prioritise by impact and time-to-implement

---
## 🔗 Go deeper: expansion notes
- [[125 Transportation Management Deep Dive|Transportation Management Deep Dive]]
- [[126 International Trade Documentation, Customs & Trade Finance|International Trade Documentation, Customs & Trade Finance]]
- [[129 E-commerce & Quick-Commerce Fulfilment|E-commerce & Quick-Commerce Fulfilment]]
- [[130 FMCG & Retail Distribution - India Route-to-Market|FMCG & Retail Distribution - India Route-to-Market]]
- [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP|India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]
