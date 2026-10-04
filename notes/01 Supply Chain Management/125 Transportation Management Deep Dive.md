---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Transportation Management Deep Dive"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Transportation Management Deep Dive

⬅ [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[126 International Trade Documentation, Customs & Trade Finance]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Mode Selection: Cost, Speed, Reliability, Capacity and Inventory]]
2. [[#2. FTL, LTL, Part-Load and Parcel: Service Types and Decision Rules]]
3. [[#3. Freight Rate Structures: Per km, per Tonne, per Pallet and Zone Matrices]]
4. [[#4. Cost per Tonne-km: Building the Truck Economics]]
5. [[#5. Load Building, Weight-Cube Utilisation and Pallet Planning]]
6. [[#6. Vehicle Routing, Milk-Run and the Savings Algorithm]]
7. [[#7. Intermodal, Rail and Dedicated Freight Corridors]]
8. [[#8. Carrier Management and Freight Tendering]]
9. [[#9. TMS Functions: Planning, Tendering, Tracking and Freight Audit and Payment]]
10. [[#10. India Trucking Ecosystem: Fleet Owners, Brokers and Aggregators]]
11. [[#11. Indian Compliance: E-way Bill, FASTag, Axle Load, Detention]]
12. [[#12. Transport KPIs and Control-Tower Metrics]]
13. [[#13. ⭐ Advanced: Fuel Surcharges, Spot vs Contract and Freight Cost Escalation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's freight rail corridors complete while fuel and freight volatility persist
> **Western Dedicated Freight Corridor completed (March-September 2026).** Per Wikipedia's page on the corridor, the **1,506 km** Western DFC (Dadri to Jawaharlal Nehru Port, Navi Mumbai) reached completion with a trial run on the last electrified double-line stretch (JNPT to Vaitarna) on **31 March 2026** and was formally dedicated by the Prime Minister on **8 September 2026**. It carries **double-stack containers on standard flat cars (up to about 400 containers a train)**, trains up to 1,500 m long, speeds above 100 km/h, and 25 t axle load on track (32.5 t on bridges). The Eastern DFC was reported fully operational from April 2024. ([Wikipedia: Western DFC](https://en.wikipedia.org/wiki/Western_Dedicated_Freight_Corridor); [Wikipedia: Eastern DFC](https://en.wikipedia.org/wiki/Eastern_Dedicated_Freight_Corridor))
>
> **India's modal cost gap (NCAER, FY2023-24).** NCAER put logistics cost at **7.97% of GDP (about ₹24 trillion)** and average cost per tonne-km at **rail ₹1.96, coastal ₹1.80, inland waterways ₹3.30, road ₹3.78 and air ₹72**. Indian Railways carried **1,588.06 million tonnes** of freight in 2023-24 on an average of 11,724 freight trains a day. ([ITLN](https://www.itln.in/logistics/indian-logistics-costs-at-797-of-gdp-new-study-reveals-1356654); [Wikipedia: Indian Railways](https://en.wikipedia.org/wiki/Indian_Railways))
>
> **Diesel and freight pressure (October 2026).** Brent crude traded at about **$98.15 a barrel on 1 October 2026** after a roughly **14% gain in September**, a direct driver of diesel and fuel-surcharge clauses. In a Netstock survey of 150+ SMBs (published 1 October 2026), **72% cited freight pressures** among their leading issues and freight and shipping costs were the top primary challenge for 23%. ([Business Standard](https://www.business-standard.com/markets/commodities/oil-prices-steady-as-investors-assess-us-iran-peace-talks-supply-outlook-126100100084_1.html); [Supply Chain Dive](https://www.supplychaindive.com/news/beyond-tariffs-a-storm-of-pressures-is-hampering-smb-supply-chains/831880/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Mode Selection: Cost, Speed, Reliability, Capacity and Inventory
> 🔴 Tier 1 · _Key points:_ Total logistics cost = freight + inventory in transit + service risk; break-even cargo value

### Definition
Mode choice (road, rail, coastal/inland waterways, air, pipeline) is a **trade-off on freight cost, transit time, reliability (variance of transit), capacity/shipment size, flexibility, damage risk, emissions and the cargo's value density**. The basic profiles are in [[009 Logistics & Distribution]]; the decision logic here is **total logistics cost**:

$$TLC = \text{Freight} + \text{First/last-mile} + \underbrace{V \cdot i \cdot \frac{t}{365}}_{\text{in-transit inventory carrying}} + \text{Safety stock effect} + \text{Cost of service failure}$$

with $V$ = cargo value, $i$ = annual carrying cost rate, $t$ = transit days. Slower modes win on low value density, bulk, and stable demand; faster modes win when carrying cost, stock-out cost or shelf life dominate. Tools: a **weighted scoring matrix** (cost, time, reliability, capacity, damage) for qualitative choice; **TLC comparison** for quantitative. Rail's variance and wagon availability, and road's dependence on diesel, are reliability and cost-risk factors.

### Example
Mumbai to Delhi, 1,400 km, 20 t consignment (cargo value ₹60 lakh). Using NCAER averages: road = 20 × 1,400 × ₹3.78 = **₹1,05,840**; rail = 20 × 1,400 × ₹1.96 = ₹54,880 plus first/last-mile road legs of ₹18,000 = ₹72,880. Rail adds 3 days in transit: carrying cost = ₹60 lakh × 18% × 3/365 = ₹8,877, so rail TLC = **₹81,757**, **22.8% cheaper**. Break-even: rail stops winning when the extra carrying cost equals the freight saving of ₹32,960, i.e. cargo value of 32,960 × 365 / (0.18 × 3) = **₹2.23 crore per 20 t load (about ₹11.1 lakh per tonne)**. For ₹4 crore of electronics, rail carrying cost is ₹59,178 and TLC ₹1,32,058, so road wins.

### In the news
See news box. NCAER's ₹3.78 vs ₹1.96 per tonne-km gap, and the freshly completed Western DFC, widen the cases where rail or intermodal beats road; diesel volatility strengthens that case further.

### Interview angle
> [!question] How it is asked
> "A client ships 500 tonnes a week from Mumbai to Delhi by road. Should it shift to rail?"

> [!tip] Strong answer includes
> - Total logistics cost, not freight rate alone; break-even cargo value
> - Reliability and transit variance, terminal handling, first/last mile
> - Segment: bulk and low-value to rail/DFC, urgent and high-value on road or air
> - Pilot lane, service-level commitments, and contract with the railway or a container operator

---
## 2. FTL, LTL, Part-Load and Parcel: Service Types and Decision Rules
> 🔴 Tier 1 · _Key points:_ Shipment size bands, hub-and-spoke, part-load, courier; when each wins

### Definition
- **FTL (full truck load):** one shipper, one vehicle, point to point; priced per trip or per km; fastest for large consignments (roughly above 8 to 10 tonnes or 60-70% of truck volume).
- **LTL / part-load (PTL):** several shippers share a vehicle; carriers consolidate through **hubs** (**hub-and-spoke**) or operate **direct multi-drop** lanes; priced per kg, per pallet or per CFT/CBM with minimum charges; transit longer, handling damage higher.
- **Parcel / courier / express:** small shipments (under about 30 to 50 kg), pricing by **zone and weight slab**, **volumetric weight** rule, COD surcharges, tracking by AWB.
- **Dedicated / contract fleet** and **milk-run** for repeated flows.
Decision rule: choose by **shipment weight/volume, frequency, service level and damage sensitivity**; consolidate shipments when possible to move from parcel to LTL and LTL to FTL. The FTL vs LTL break-even formula is in [[009 Logistics & Distribution]]; below we add **zone/volumetric** logic.

### Example
A consignment of 12 cartons, each 60 × 40 × 40 cm weighing 14 kg. Actual weight = 168 kg. Volume = 12 × 0.096 m³ = 1.152 m³. Using an illustrative surface volumetric rule of 1 m³ = 250 kg, volumetric weight = 288 kg, so **chargeable weight = 288 kg** (the larger). At ₹14 per kg (LTL, one zone pair) the freight is 288 × 14 = **₹4,032**, versus ₹2,352 on actual weight (the volumetric rule adds 71%). Switching to 50 × 35 × 35 cm cartons (0.06125 m³ each) gives a volumetric weight of 12 × 0.06125 × 250 = 184 kg, close to the actual 168 kg, so freight falls to about **₹2,573 (−36%)**: right-sizing packaging attacks the volumetric penalty directly.

### In the news
See news box. Freight cost is the top pressure for 23% of SMBs surveyed and 72% listed it among their leading issues; small shippers are the ones paying LTL and parcel slab rates, so consolidation matters most for them.

### Interview angle
> [!question] How it is asked
> "When should a company move from LTL to FTL, or from courier to LTL?"

> [!tip] Strong answer includes
> - Weight/volume bands and frequency; chargeable weight (volumetric)
> - Consolidation, pooling and dispatch-day scheduling
> - Service trade-offs: transit time, damage, tracking
> - Numerical break-even and sensitivity to fuel surcharge

---
## 3. Freight Rate Structures: Per km, per Tonne, per Pallet and Zone Matrices
> 🔴 Tier 1 · _Key points:_ Lane rate, per-km, per-tonne-km, per-pallet, zone matrix, surcharges and accessorials

### Definition
Common structures:
- **Per trip (lane rate) / per km:** FTL price for a vehicle type on a lane (e.g. ₹58 per km for a 32-ft multi-axle truck, illustrative), often negotiated annually by lane.
- **Per tonne / per tonne-km:** bulk and rail; per-tonne rates with minimum guaranteed tonnage.
- **Per pallet / per CBM / per kg:** LTL and shared services.
- **Zone matrix (origin zone x destination zone):** rate cards by weight slab; used by LTL, parcel and courier carriers.
- **Cost-plus / open book** for dedicated fleets: fixed monthly rate plus per-km above a committed distance.
Add-ons (**accessorials**): fuel surcharge (indexed to diesel), loading and unloading, **detention** beyond free time, multi-point pickup/delivery, toll and entry charges, ODC (over-dimensional cargo), return/RTO, insurance, GST. India: GST on road freight depends on the carrier type and mechanism (reverse charge vs forward); see [[227 GST & Indirect Tax for Supply Chains]]. **Return-load (backhaul) pricing** matters: one-way lanes carry the empty return in the price.

### Example
A 32-ft truck quoted ₹58 per km on a 1,000 km lane carrying 16 t: trip price **₹58,000**; **₹3.63 per tonne-km** (58,000 / (16 × 1,000)); with 20 pallets, ₹2,900 per pallet. If the truck cubes out at 10.8 t (dense cartons), cost per tonne rises to 58,000 / 10.8 = ₹5,370, versus ₹4,143 per tonne at 14 t. Zone matrix example (₹ per kg, 100 to 500 kg slab):

| Origin \ Destination | North | West | South | East |
|---|---|---|---|---|
| North | 6 | 11 | 15 | 14 |
| West | 11 | 6 | 12 | 16 |
| South | 15 | 12 | 6 | 15 |

A West-to-South 300 kg consignment costs 300 × ₹12 = ₹3,600 plus fuel surcharge of 10% (₹360) = **₹3,960**.

### In the news
See news box. With Brent at about $98 and up 14% in a month, fuel-surcharge schedules (typically a table linking diesel price bands to a percentage add-on) are where the volatility passes to shippers.

### Interview angle
> [!question] How it is asked
> "How would you structure a freight contract with a transporter for 40 lanes?"

> [!tip] Strong answer includes
> - Lane-wise per-trip/per-km rates, vehicle types, volume bands
> - Fuel surcharge linked to a published diesel price with a base and band
> - Accessorials and detention rules, free time, load/unload obligations
> - Performance KPIs (OTD, claims) and review cycle

---
## 4. Cost per Tonne-km: Building the Truck Economics
> 🔴 Tier 1 · _Key points:_ Per-km cost stack; loaded-km share; load factor; diesel sensitivity

### Definition
Cost per tonne-km (loaded) is the key unit:

$$\text{Cost per tonne-km} = \frac{\text{Total cost per km}}{\text{Loaded-km share} \times \text{Load factor} \times \text{Payload (t)}}$$

Cost per km includes **variable** (fuel, tyres, maintenance, tolls, driver trip allowances) and **fixed** (driver salary, insurance, permit/tax, depreciation, interest, overhead) costs divided by annual km. Drivers of the unit cost: **annual kilometres** (utilisation, fixed-cost spread), **loaded-km share** (backhaul availability), **load factor** (weight and cube fill), **fuel economy**, **driving time lost** (detention, queues, restrictions) and **toll/route** choice.

### Example
Illustrative 16-t payload truck, 1,00,000 km a year:

| Item | ₹ per km |
|---|---|
| Fuel (₹92/litre at 4.5 km/l) | 20.44 |
| Tyres | 2.80 |
| Maintenance | 3.20 |
| Driver (₹40,000/month = ₹4.8 lakh a year) | 4.80 |
| Tolls (FASTag) | 4.50 |
| Insurance, permits, taxes (₹1.8 lakh) | 1.80 |
| Finance and depreciation (10% interest on ₹15 lakh average balance + ₹3 lakh depreciation) | 4.50 |
| **Subtotal** | **42.04** |
| Overhead and margin (5%) | 2.10 |
| **Total** | **44.15** |

Annual cost ₹44.15 lakh. With **80% loaded km** and **85% load factor** (13.6 t average load): cost per loaded tonne-km = 44.15 / (0.80 × 0.85 × 16) = **₹4.06**. A return load that lifts loaded-km share to 95% gives ₹3.42 (−16%); load factor to 95% gives ₹3.63 (−11%). Fuel is 48.6% of the subtotal, so a 10% diesel rise lifts cost per km by about **4.9%**. The result is in the same range as NCAER's national road average of ₹3.78.

### In the news
See news box. NCAER's ₹3.78 road average is a useful reasonableness check for a bottom-up build, and Brent's 14% September gain shows why the fuel row needs a separate escalation clause.

### Interview angle
> [!question] How it is asked
> "What is the cost per tonne-km for a truck and how would you reduce it?"

> [!tip] Strong answer includes
> - Per-km cost stack and annual-km assumption
> - Formula with loaded-km share and load factor
> - Levers ranked by impact: backhaul, load factor, turnaround, fuel, route and tolls
> - Check against benchmarks (NCAER, internal data)

---
## 5. Load Building, Weight-Cube Utilisation and Pallet Planning
> 🔴 Tier 1 · _Key points:_ Weight vs cube constraints, stackability, loading sequence, multi-drop, packaging link

### Definition
**Load building** decides which orders ride on which vehicle to maximise utilisation within constraints: **weight** (payload, axle load), **cube** (usable volume), **pallet positions**, **stackability and compatibility** (no food with chemicals), **delivery sequence** (LIFO for multi-drop), **time windows**, **fragility**, and **legal limits** (see axle load). **Cube-out vs weight-out:** products with low density fill the volume before weight; heavy products reach the payload limit first. Utilisation lens: $U = \max(\text{weight util.}, \text{cube util.})$ (the binding constraint). Improving utilisation: **packaging redesign**, **pallet height optimisation**, **nesting/knock-down shipments**, **order consolidation** with minimum drop sizes and order cut-offs, **mixed pallets**, and **cross-docking**; see [[140 Packaging, Unitisation & Load Optimisation]]. Algorithmic approach: **bin-packing and vehicle-loading heuristics** in TMS ([[148 Operations Research - Network Models & Integer Programming]] for formulation).

### Example
A 32-ft truck: payload 14 t, usable 60 m³. Product density 180 kg/m³: it cubes out at 60 × 0.18 = **10.8 t (77% of payload)**. At ₹58,000 per trip, the cost per tonne is ₹5,370, against ₹4,143 per tonne if the truck could be loaded to 14 t. Fix: raise pallet height from 1.2 m to 1.5 m (stackable cartons) and compress the cartons so density rises to 230 kg/m³: cube-out at 13.8 t (99% of payload), cost per tonne = 58,000 / 13.8 = **₹4,203 (−22%)**. Annual effect: moving 32,400 t a year (3,000 loads of 10.8 t) costs 3,000 × ₹58,000 = ₹17.4 crore today; at 13.8 t a load the same tonnage needs 2,348 trips and costs about ₹13.62 crore, a saving of **₹3.78 crore a year** (cost per tonne falls by ₹1,167).

### In the news
See news box. When freight and diesel costs climb, utilisation (kg per rupee of freight) becomes the cheapest lever, ahead of renegotiating rates.

### Interview angle
> [!question] How it is asked
> "A client's trucks leave only 70% full. What would you do?"

> [!tip] Strong answer includes
> - Diagnose weight vs cube constraint; measure by lane
> - Order consolidation, packaging and pallet design, dispatch rules
> - Multi-drop sequencing and time windows
> - Quantify gains and customer-service trade-offs

---
## 6. Vehicle Routing, Milk-Run and the Savings Algorithm
> 🔴 Tier 1 · _Key points:_ VRP constraints; milk-run for inbound; Clarke-Wright savings; time windows

### Definition
The **Vehicle Routing Problem (VRP)** assigns customers to routes and sequences stops to minimise distance, time or cost subject to capacity, time windows, driver hours and vehicle types. Variants: capacitated VRP (CVRP), VRP with time windows (VRPTW), pickup-and-delivery, multi-depot. **Milk-run** (a fixed route that collects from several suppliers, or delivers to several customers, in one loop) is standard in auto and FMCG inbound logistics (JIT). The **Clarke-Wright savings** heuristic starts with one route per customer and merges them in order of

$$s_{ij} = d_{0i} + d_{0j} - d_{ij}$$

(distance saved by serving $i$ and $j$ together rather than separately from depot 0), subject to capacity. Optimisation models and solvers (LP/MIP; see [[147 Operations Research - Transportation, Assignment & Transshipment]] and [[068 Operations-Specific Python (PuLP, SimPy)]]) refine the heuristic route. More on route optimisation is in [[009 Logistics & Distribution]].

### Example
Plant P with suppliers A, B, C: distances P-A 40, P-B 30, P-C 35 km; A-B 25, A-C 50, B-C 15. Pickups: A 4 t, B 5 t, C 4 t (truck 16 t). Separate trips: 2 × (40 + 30 + 35) = **210 km**. Savings: $s_{BC} = 30 + 35 - 15 = 50$, $s_{AB} = 40 + 30 - 25 = 45$, $s_{AC} = 40 + 35 - 50 = 25$. Merge B-C (route P-B-C-P = 80 km), then add A next to B: route P-A-B-C-P = 40 + 25 + 15 + 35 = **115 km** (13 t, within capacity): 45% shorter. At ₹42 per km, 210 km = ₹8,820 versus 115 km = ₹4,830 per cycle (saving ₹3,990).

### In the news
See news box. Higher diesel prices (Brent up about 14% in September 2026) make every kilometre removed from a route more valuable.

### Interview angle
> [!question] How it is asked
> "Design a milk-run for 12 suppliers feeding one plant in Pune."

> [!tip] Strong answer includes
> - Clustering by geography, volume and pickup windows
> - Fixed schedule, loading discipline, returnable containers
> - Route cost vs direct deliveries; buffer for variability
> - Software and KPI tracking (route adherence, fill rate, TAT)

---
## 7. Intermodal, Rail and Dedicated Freight Corridors
> 🔴 Tier 1 · _Key points:_ Container rail, double-stack, first/last-mile, terminals; DFC advantages and limits

### Definition
**Intermodal transport** moves a unit load (a container) through multiple modes (truck, rail, ship) without handling the cargo; **multimodal** means one contract and one liable operator. In India, rail freight runs through Indian Railways wagons, **CONCOR** and private container train operators, and **DFCs** designed for higher speed, longer and heavier trains. The Western DFC supports **double-stack container trains** on standard flat cars, increasing container capacity per train and cutting cost per container-km on the Mumbai-Gujarat-NCR trunk. Key elements: **inland container depots (ICDs)**, **private freight terminals (PFTs)**, **gati shakti cargo terminals**, **first/last-mile drayage**, **terminal dwell time**, **wagon allocation** and **transit reliability**. Rail's strengths: bulk, low cost per tonne-km, low emissions; weaknesses: terminal handling, rake size minimums, lower flexibility and variable transit time (policy: [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]).

### Example
A consumer-durables firm moves 40 containers a week from a NCR ICD to JNPT. Road per container: ₹58,000; rail (with drayage at both ends ₹14,000 per container): ₹36,000 + ₹14,000 = ₹50,000. Savings ₹8,000 per container, **₹3.2 lakh a week = ₹1.66 crore a year** (52 weeks). Transit time rises from 3 to 5 days; extra pipeline inventory = 40 containers × 2 more days of the weekly flow ≈ about 11.4 containers' worth of stock (80 / 7); at ₹25 lakh a container and 18% carrying cost, the extra stock costs 11.4 × 25 lakh × 18% = ₹51 lakh a year. Net saving ≈ **₹1.15 crore a year**; reliability and dwell time can erode it.

### In the news
See news box. The Western DFC's completion (trial run on 31 March 2026, dedication on 8 September 2026) and double-stack capacity raise the share of long-haul containerised freight that can shift, subject to terminal and drayage readiness.

### Interview angle
> [!question] How it is asked
> "Would you move container traffic from road to rail after the Western DFC is ready?"

> [!tip] Strong answer includes
> - Cost per container including drayage and terminal handling
> - Transit reliability and dwell time at terminals
> - Which lanes and volumes suit rail; contract options
> - Inventory impact and customer service effects

---
## 8. Carrier Management and Freight Tendering
> 🔴 Tier 1 · _Key points:_ Lane tender, primary/backup allocation, scorecards, contract vs spot, carrier onboarding

### Definition
**Carrier management** covers sourcing, contracting, allocation, performance monitoring and development of transporters. **Freight tendering** has two meanings: (1) the **annual lane bid (RFQ/RFP)** to set contract rates and allocation; (2) the **daily load tender** (a shipment is offered to the primary carrier first and **waterfalls** to the backup or spot market if declined within a time limit). Elements: **lane-by-lane bid** with volume forecast and vehicle type; **carrier qualification** (fleet, financials, insurance, GPS, compliance, safety); **allocation strategy** (e.g. 60/30/10 primary-secondary-tertiary) balancing price and reliability; **bid optimisation** (scenario analysis with capacity limits); **contract vs spot mix** (e.g. 80/20); **scorecards** (OTD, acceptance rate, claims, documentation, TAT), **freight index/diesel** clauses, and **carrier development** (fleet quality, drivers). Related: [[002 Procurement & Strategic Sourcing|sourcing methods]] and [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies|partnership models]].

### Example
Lane Mumbai-Delhi, 50 loads a month. Bids: Carrier 1 ₹48,000, Carrier 2 ₹50,500, Carrier 3 ₹53,000; spot market ₹56,000. Allocation 60/30/10: weighted rate = 0.6 × 48,000 + 0.3 × 50,500 + 0.1 × 53,000 = **₹49,250**, monthly cost = 50 × 49,250 = ₹24.63 lakh, ₹0.63 lakh above an all-to-Carrier-1 plan (₹24 lakh). If Carrier 1 rejects 15% of tenders and those loads go to spot: expected rate = 0.85 × 48,000 + 0.15 × 56,000 = **₹49,200**, nearly identical to the multi-carrier allocation, but with better service reliability and less last-minute spot scrambling. Acceptance rate and OTD should therefore decide allocation, not only price.

### In the news
See news box. With diesel moving sharply, a contract with a clear fuel-escalation formula protects both carrier viability and shipper budget; rate quotes without it tend to be withdrawn in a spike.

### Interview angle
> [!question] How it is asked
> "How would you run a freight tender for 200 lanes and 30 carriers?"

> [!tip] Strong answer includes
> - Data prep: lane volumes, vehicle types, seasonality, service requirements
> - Evaluation: price, capacity, acceptance, compliance; optimisation of allocation
> - Primary/secondary structure and spot-share rules
> - Governance: quarterly review, scorecard, fuel clause, exit

---
## 9. TMS Functions: Planning, Tendering, Tracking and Freight Audit and Payment
> 🔴 Tier 1 · _Key points:_ Plan-execute-settle loop; control tower; integration with ERP and WMS

### Definition
A **Transportation Management System (TMS)** covers four loops:
1. **Planning and optimisation:** load consolidation, mode and carrier selection, route and cost optimisation, appointment scheduling.
2. **Execution and tendering:** load tendering (waterfall), dispatch, e-way bill and documentation, carrier communications, appointment and gate integration with yard systems ([[128 Warehouse Labour, WES-WCS & Yard Management]]).
3. **Visibility and tracking:** GPS/telematics, ETAs, exception alerts (route deviation, delay, tampering), proof of delivery (e-POD), control tower views.
4. **Freight audit and payment (FAP):** match invoice against contracted rate, weight, accessorials and POD; accrue cost; pay; analyse leakage.
Plus **analytics** (cost to serve, carrier performance, lane analysis) and **integration** with ERP, WMS, order management and carrier portals. Examples: SAP TM ([[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]]), Oracle OTM, Blue Yonder, plus Indian TMS platforms. The wider technology landscape is in [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]].

### Example
Freight spend ₹100 crore a year. An audit shows 3% leakage: wrong weights, detention billed without gate-in proof, rate-card mismatches, duplicate invoices. Recovery = ₹3 crore. A TMS with automated three-way match (rate, POD, accessorial) costing ₹0.6 crore a year yields a net benefit of ₹2.4 crore. Additional gains: load consolidation of 2% (₹2 crore) and 5% fewer expedited loads. Benefits table for the business case: leakage ₹3.0 crore, consolidation ₹2.0 crore, lower detention ₹0.5 crore, cost of the system ₹(0.6) crore; net ≈ ₹4.9 crore.

### In the news
See news box. A tracked, rate-compliant contract-freight system limits the exposure to the spot market whenever fuel and rate spikes arrive.

### Interview angle
> [!question] How it is asked
> "What would a TMS implementation give a manufacturer with 500 trucks a day?"

> [!tip] Strong answer includes
> - The four loops and their value levers
> - Business case with leakage, consolidation, and productivity
> - Data and integration challenges (master data, carrier onboarding, GPS quality)
> - Change management with transporters and plants

---
## 10. India Trucking Ecosystem: Fleet Owners, Brokers and Aggregators
> 🔴 Tier 1 · _Key points:_ Fragmented small operators, broker layers, digital freight platforms, driver supply

### Definition
Indian road freight is **highly fragmented**: a large share of trucks is owned by small operators with a handful of vehicles (industry commentary commonly cites that most owners have one to five trucks; treat as indicative). Layers: **shipper → transport contractor / fleet operator / 3PL → broker or commission agent → fleet owner/owner-driver → driver**. Brokers provide **market access and load matching** (and take a commission), while **aggregator and digital freight platforms** (marketplaces, app-based matching, GPS tracking, instant payment) reduce search time and empty running. Implications: **quality and compliance vary**, documents and payments are manual, **advance and balance payment practices** (cash at loading and on delivery with the rest) drive behaviour, **driver shortage and fatigue**, **detention** with little compensation, and **weak telematics**. Strategic options for a large shipper: contract with **organised fleet operators or 3PLs**, run **dedicated fleets** with leasing, create **preferred-transporter programmes**, use **digital freight platforms** for the tail, enforce compliance (KYC, insurance, GPS). See [[009 Logistics & Distribution]] and [[223 Logistics, Manufacturing & Industry Data Points - India]].

### Example
Shipper buys 2,000 loads a month through a transport contractor at ₹50,000 per load. The contractor pays the fleet owner ₹46,000 and keeps a margin of ₹4,000 (8%). Moving 40% of loads to direct contracts with 15 vetted fleet owners at ₹47,500 saves ₹2,500 on 800 loads = **₹20 lakh a month = ₹2.4 crore a year**, but adds ₹0.4 crore a year of internal management and compliance cost: net **₹2.0 crore**. Risk: less spot flexibility during peaks; keep the contractor for 60% as back-up capacity.

### In the news
See news box. Fuel volatility hits small fleet owners hardest (thin cash buffers), so escalation clauses and prompt payment improve carrier reliability; the DFC adds an organised alternative on trunk lanes.

### Interview angle
> [!question] How it is asked
> "Why is Indian trucking inefficient, and what would you change as a large shipper?"

> [!tip] Strong answer includes
> - Fragmentation, broker layers, low trip utilisation, detention, manual documents
> - Levers: aggregation, contract fleets, telematics, payment discipline, load pooling
> - Rail and DFC as parallel capacity; policy context (ULIP, NLP)
> - Realism about change and compliance risks

---
## 11. Indian Compliance: E-way Bill, FASTag, Axle Load, Detention
> 🔴 Tier 1 · _Key points:_ E-way bill thresholds and validity; FASTag; load limits; detention economics

### Definition
- **E-way bill (GST):** an electronic permit for goods above **₹50,000** in value moved in a conveyance (inter-state movement beyond about 10 km, with intra-state rules phased in by states from April-May 2018); **Part A** (consignment details) and **Part B** (vehicle details). Validity: **one day for every 200 km or part thereof**, extendable before expiry. A truck without a valid e-way bill risks detention and penalty; plants build e-way bill generation into dispatch (SAP: see [[195 SAP SD Advanced - Pricing, Output & Document Flow|SD output]] and [[227 GST & Indirect Tax for Supply Chains]]).
- **FASTag:** RFID-based electronic toll payment, piloted in 2014 and made mandatory at toll plazas in early 2021 (the 1 January 2021 deadline was postponed to 15 February 2021); cuts queues and gives toll data for cost control. Toll is a per-km cost line for trucks.
- **Axle-load and weight norms:** the permitted laden weight by axle configuration is set under the Central Motor Vehicles Rules and was raised in 2018 (by roughly 20-25% on many configurations); check the current table before quoting; overloading triggers fines at weigh-in-motion points, damages roads and raises safety risk; over-dimensional cargo needs permits.
- **Detention:** carriers charge for truck time beyond a free period (commonly 24 hours; contract-specific) because idle trucks lose revenue; waiting at plants, ports and unloading points is the largest hidden productivity loss.
- Other: **driver hours and compliance**, **GPS and speed**, **state entry/permit rules**, **vehicle fitness**.

### Example
Lane of 1,000 km: transit 2.5 days one way, return 2.5 days, loading 1 day, unloading 1 day: **cycle 7 days**. At 330 operating days: 47.1 trips a year; at ₹58,000 revenue per round trip = **₹27.3 lakh**. If detention adds one day at each end (loading and unloading take 2 days each), cycle = 9 days, 36.7 trips, **₹21.3 lakh**: a loss of ₹6.1 lakh a year per truck (22%). A carrier prices this loss into the rate unless the shipper compensates it through detention charges or fixes dock performance. E-way bill: a 1,000 km consignment needs validity of 1,000/200 = **5 days**; transit of 2.5 days leaves buffer, but a breakdown can exhaust it: extend before expiry.

### In the news
See news box. Wikipedia's e-way bill summary gives the ₹50,000 threshold and one-day-per-200-km validity; FASTag's mandatory status since 2021 means toll data are available for audit.

### Interview angle
> [!question] How it is asked
> "How do detention and waiting time affect transport cost and what would you do?"

> [!tip] Strong answer includes
> - Truck cycle-time arithmetic and revenue lost per day
> - Dock scheduling, appointment systems, yard management, gate-to-gate TAT KPI
> - Detention clauses with free time, both sides' accountability
> - Statutory points: e-way bill, FASTag, axle load, with note to verify current rules

---
## 12. Transport KPIs and Control-Tower Metrics
> 🔴 Tier 1 · _Key points:_ Cost, utilisation, service, productivity; definitions and targets

### Definition
| KPI | Formula / meaning |
|---|---|
| **Freight cost as % of sales** | Freight spend / net sales |
| **Cost per tonne-km** (or per case, per pallet) | Freight cost / (tonnes × km) |
| **Load factor (vehicle fill)** | Actual weight / payload, and cube utilisation |
| **Empty running %** | Empty km / total km |
| **On-time delivery / OTIF** | Deliveries on time (and in full) / total |
| **Vehicle turnaround time (TAT)** | Gate-in to gate-out at plant or DC |
| **Detention days / cost** | Hours beyond free time |
| **Carrier acceptance rate** | Tendered loads accepted / tendered |
| **Rate compliance** | Loads at contract rate / loads |
| **Claims ratio** | Value of damage and loss / freight value |
| **Spot share** | Spot loads / all loads |
| **Freight audit variance** | Invoiced vs contract |
| **Emissions per tonne-km** | CO₂e / tonne-km |
Dashboards combine KPIs by lane, carrier, plant, and customer; see [[012 Supply Chain Analytics & KPIs]] and [[138 Order Management, Customer Service & Cost-to-Serve]] for cost-to-serve. KPIs should balance cost and service (OTIF) and be actionable (owner and trigger).

### Example
Monthly data for one 1,000 km lane (illustrative): 1,200 loads, 15,000 tonnes, freight cost ₹6.96 crore. Tonne-km = 15,000 t × 1,000 km = 1.5 crore, so cost per tonne-km = 6.96 / 1.5 = **₹4.64**. Average load = 15,000 / 1,200 = 12.5 t (78% of a 16 t payload); on-time deliveries 1,104 of 1,200 = **92%**; primary carriers accepted 1,056 of 1,200 tendered loads (**88%**), so 12% went to spot; average gate-to-gate TAT 11.5 hours against a 6-hour target. Improvement priorities: load factor (cost lever), then TAT (cycle lever).

### In the news
See news box. NCAER's ₹3.78 national road average against this lane's ₹4.64 signals where to look (small loads, empty returns, detention), though lane mix matters.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track to manage a transport operation, and which would you act on first?"

> [!tip] Strong answer includes
> - Cost, utilisation, service, productivity, compliance KPIs
> - Formulas and a benchmark; link to targets
> - Root-cause on the biggest gap and a prioritised action plan
> - Owners and review cadence

---
## 13. ⭐ Advanced: Fuel Surcharges, Spot vs Contract and Freight Cost Escalation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **fuel surcharge** passes diesel moves into freight price. A common design: contract rate stated at a **base diesel price**; each band of change adjusts the rate by an agreed percentage, reflecting fuel's share of the carrier's cost:

$$\text{Rate}_t = \text{Rate}_0\Big[1 + \phi\,\frac{D_t - D_0}{D_0}\Big]$$

where $\phi$ is fuel's share of cost (about 0.45 to 0.50 for long-haul trucking in the example above) and $D$ is diesel price. **Spot vs contract:** spot rates move with market tightness (festive peaks, harvest, month-end, monsoon) and usually carry a premium at peaks and a discount in troughs; **contract** rates give capacity assurance at the cost of paying above spot in slack periods. A balanced portfolio (for example 80% contract, 20% spot) with an index-linked review limits both price and service risk. Link to commodity-linked clauses in [[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]] and to carbon accounting through emissions per tonne-km.

### Example
Lane rate ₹58,000 at base diesel ₹92 per litre, $\phi = 0.486$ (from the cost build). Diesel rises 10% to ₹101.2: rate = 58,000 × (1 + 0.486 × 0.10) = **₹60,819** (+₹2,819, +4.9%). On 600 loads a month that is **₹16.9 lakh more a month**, ₹2.03 crore a year. A buyer that fixed the rate for 12 months without a fuel clause is protected, but the carrier may accept loads selectively when diesel jumps (acceptance rate falls), a hidden cost. Spot vs contract: if peak-season spot is 18% above contract on 20% of the loads for 3 months, extra cost on 600 loads a month = 600 × 0.20 × 3 × ₹58,000 × 18% = ₹37.6 lakh, which a reserved contract capacity buffer may cheaply avoid.

### In the news
See news box. A roughly 14% monthly jump in Brent (to about $98 on 1 October 2026) is the scenario this formula is built for; shippers with clear surcharge tables avoid disputes and capacity withdrawal.

### Interview angle
> [!question] How it is asked
> "Diesel is up 10%. How should transporter rates and customer prices change?"

> [!tip] Strong answer includes
> - Fuel share of cost, formula, and band-based surcharge
> - Pass-through downstream (customer freight terms), timing, and caps
> - Spot vs contract exposure and carrier acceptance risk
> - Mitigations: modal shift to rail, load factor, route changes, telematics-based fuel efficiency
