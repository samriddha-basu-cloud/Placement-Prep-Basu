---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Automotive Supply Chain - JIT, Tiers & EVs"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Automotive Supply Chain - JIT, Tiers & EVs

⬅ [[130 FMCG & Retail Distribution - India Route-to-Market]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[132 Pharma & Healthcare Supply Chain]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. OEM-Tier Structure & Why Autos Are the Textbook Supply Chain]]
2. [[#2. JIT Pull, Kanban & Takt Time]]
3. [[#3. JIT vs JIS (Just-in-Sequence)]]
4. [[#4. Inbound Logistics: Milk Run & Cross-Dock to the Line]]
5. [[#5. Kitting, Line-Side Delivery & Supermarkets]]
6. [[#6. VMI, Consignment & Supplier Hubs at the OEM]]
7. [[#7. Build-to-Order vs Stock Vehicles & Dealer Inventory]]
8. [[#8. Aftermarket & Spare Parts Logistics]]
9. [[#9. EV Supply Chain: Cells, Rare Earths, Localisation, PLI-Auto & ACC]]
10. [[#10. Semiconductor Shortage 2021-23 & the Nexperia Lesson]]
11. [[#11. Tyre Supply Chain]]
12. [[#12. India's Auto Clusters & Manufacturing Geography]]
13. [[#13. Vehicle Outbound Logistics: Car Carriers, RoRo & Rail]]
14. [[#14. ⭐ Advanced: Automotive KPIs & a Resilience Scorecard]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): a ₹40 chip or a magnet can stop a ₹8 lakh car
> **Nexperia chip shock (October-November 2025).** After the Dutch government took control of Nexperia and the company stopped wafer shipments to its Chinese plant, automakers scrambled: Honda halted its Celaya plant in Mexico (it built over 190,000 vehicles the previous year, mostly HR-V SUVs for North America) and cut output at US and Canadian plants, while Nissan said the problem "may become a large-scale problem". Nexperia makes simple discrete chips (switches, logic, LED-headlight drivers, battery-management and braking-system parts) and holds only about 5% of the automotive discrete market by revenue, but far more by chip volume. ([Japan Times](https://www.japantimes.co.jp/business/2025/10/30/companies/honda-mexico-production-halt/), [WTOP/AP explainer](https://wtop.com/europe/2025/11/a-crisis-at-chipmaker-nexperia-sent-automakers-scrambling-heres-what-to-know/))
>
> **Rare-earth magnets hit Indian EV makers (2025).** China imposed rare-earth export restrictions on 4 April 2025 and eased them for India after talks around 19 August 2025. In between, Bajaj Auto's Chetak electric scooter output fell to 10,824 units in July 2025 from 20,384 in July 2024 (about -47%). China controls roughly 90% of global rare-earth processing. ([Al Jazeera](https://www.aljazeera.com/economy/2025/8/28/how-rare-earth-shortages-are-stalling-indias-burgeoning-ev-sector))
>
> **PLI-Auto and ACC progress (2025-26).** The PLI-Auto scheme (₹25,938 crore, approved September 2021, minimum 50% domestic value addition) had attracted ₹44,326 crore of investment and 67,820 jobs by 31 March 2026. As of 31 December 2025, ₹2,321.94 crore of incentive had been disbursed and over 13.6 lakh EVs produced under it (about 10.4 lakh electric two-wheelers). By contrast, the ₹18,100 crore ACC battery PLI (50 GWh allotted in 2022) had delivered only about 1.4 GWh (2.8%) by October 2025 according to IEEFA. ([PIB, PLI-Auto, March 2026](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2290691&reg=48&lang=2), [PIB, Dec 2025](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2210127&reg=3&lang=1), [PIB, ACC allotment](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1809037&reg=3&lang=2), [IEEFA](https://ieefa.org/articles/only-28-target-capacity-delivered-yet-under-indias-battery-manufacturing-incentive-scheme))
>
> **India's auto volumes (FY2025-26).** SIAM reported domestic sales of 46.43 lakh passenger vehicles (+7.9%), 2.17 crore two-wheelers (+10.7%), 10.80 lakh commercial vehicles (+12.6%) and total production of 3.47 crore units, with passenger-vehicle exports of 9.05 lakh (+17.5%). ([SIAM](https://www.siam.in/news-&-updates/press-releases/auto-industry-performance-of-q4-jan--march-2026-fy-2025-26/605))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. OEM-Tier Structure & Why Autos Are the Textbook Supply Chain
> 🔴 Tier 1 · _Key points:_ OEM, Tier 1/2/3, bought-in content, platform sharing, power asymmetry

### Definition
An **OEM** (original equipment manufacturer: Maruti Suzuki, Tata Motors, Mahindra, Hyundai, Hero, Bajaj) designs the vehicle, assembles it and owns the brand and the dealer network. Most of the vehicle is **bought in**: industry estimates put purchased parts and materials at roughly 65-80% of vehicle cost, so the OEM's performance is largely its suppliers' performance.

The supply base is a pyramid:
- **Tier 1**: sells directly to the OEM, usually system or module integrators (seats, cockpits, wiring harnesses, axles, braking systems). Examples: Bosch, Motherson, Uno Minda, Bharat Forge, Sona Comstar.
- **Tier 2**: supplies Tier 1 with sub-components (castings, stampings, fasteners, plastic mouldings, ECUs).
- **Tier 3 and below**: raw materials and commodity processing (steel, aluminium, rubber, resin, copper).
- **Lateral players**: tooling and die makers, logistics providers (3PLs), and "directed-buy" suppliers whose price is negotiated by the OEM although the part is shipped via a Tier 1.

Structural features: very high volumes with low unit margins, long model lifecycles (5-8 years with a mid-cycle facelift), part numbers in the thousands (a car has several thousand parts; an Indian small car around 2,000-3,000 depending on definition), shared **platforms** to spread tooling cost, and heavy **buyer power** (annual price-downs, capacity commitments, tooling ownership). Quality gates such as APQP and PPAP govern entry (see [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

### Example
A hatchback with ₹6.5 lakh ex-factory price and 72% bought-in content means ₹4.68 lakh flows to the supply base. A 2% annual price-down demanded from suppliers is worth about ₹9,360 per car; at 10 lakh cars a year that is ₹936 crore, which explains why Tier-1s fight for volume and "localise" Tier-2 sourcing to protect margin.

### In the news
See news box. Both the Nexperia and rare-earth episodes were Tier-3/Tier-4 problems: OEMs did not buy the chip or the magnet directly, yet their lines stopped.

### Interview angle
> [!question] How it is asked
> "Draw the structure of an automotive supply chain and tell me where the OEM's risk sits."

> [!tip] Strong answer includes
> - OEM, Tier 1/2/3 with one Indian example each, and the 65-80% bought-in point
> - Information flow: schedule and call-offs go down, quality and capacity signals go up, with the bullwhip risk between ([[114 Bullwhip Effect, Beer Game & Information Sharing]])
> - The visibility gap: OEMs contract Tier 1 only, so Tier-N risk is hidden
> - Link to supplier strategy ([[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]])

---
## 2. JIT Pull, Kanban & Takt Time
> 🔴 Tier 1 · _Key points:_ Toyota Production System, kanban sizing, heijunka, takt

### Definition
**Just-in-time (JIT)** delivers the right part, in the right quantity, at the moment the line needs it, so inventory shrinks to a few hours. It grew out of the Toyota Production System (see [[007 Lean Manufacturing]]). Three controls make it work:
- **Takt time** = available production time ÷ customer demand; the beat of the line.
- **Kanban**: a card or e-signal that authorises replenishment of a container; downstream consumption pulls upstream production.
- **Heijunka** (level scheduling): smooths mix and volume so suppliers see a stable pull instead of spikes.

Number of kanban containers:

$$N = \frac{D \times L \times (1+\alpha)}{C}$$

where $D$ = demand per day, $L$ = replenishment lead time in days (transit + processing + waiting), $\alpha$ = safety factor, $C$ = container capacity.

### Example
A plant runs 2 shifts of 7.5 hours (15 hours = 54,000 s) and must build 1,080 cars a day: takt = 54,000 / 1,080 = **50 seconds** (72 cars per hour).
A bracket is used at 960 per day. Replenishment lead time 0.5 day, safety factor 10%, container holds 40: $N = 960 \times 0.5 \times 1.1 / 40 = 13.2$, so **14 kanbans**. Halving lead time to 0.25 day cuts it to 6.6, i.e. **7 kanbans**: shrinking lead time halves the inventory without touching service.

### In the news
See news box. Honda's Celaya stoppage shows the other side of JIT: with hours (not weeks) of stock on a low-cost part, a single upstream interruption stops the whole plant.

### Interview angle
> [!question] How it is asked
> "What is the difference between JIT and holding safety stock, and when does JIT fail?"

> [!tip] Strong answer includes
> - JIT as a system (takt, pull, levelling, quality at source), not just "low inventory"
> - Kanban formula and the lever: reduce lead time or container size, not add cards
> - Failure modes: single-source, long-distance parts, volatile demand, geopolitical shocks
> - The modern compromise: JIT for stable commodity parts, strategic buffers for critical/long-lead items ([[015 Supply Chain Risk & Resilience]])

---
## 3. JIT vs JIS (Just-in-Sequence)
> 🔴 Tier 1 · _Key points:_ sequence call-off, high-variety parts, supplier proximity, buffer in minutes

### Definition
**Just-in-sequence (JIS)** goes one step beyond JIT: the supplier delivers each part not only on time but **in the exact order of vehicles on the assembly line**, so the fitter takes the next item without choosing. It suits parts that are bulky and highly variant (colour, trim, engine type): seats, bumpers, cockpits, door panels, wheels and tyres, exhaust systems.

Mechanics: the OEM freezes the vehicle sequence at a **sequence point** (often after the paint shop, the point where the order of vehicles is fixed). It sends the sequence electronically (an EDI/ASN call-off); the supplier builds or picks in that order and ships, typically within a window of 90 to 240 minutes. The supplier's plant is therefore usually within a few kilometres of the OEM, or inside a **supplier park**.

| Feature | JIT | JIS |
|---|---|---|
| Delivery trigger | Consumption signal (kanban / schedule) | Sequence of vehicles on the line |
| Order of parts | Any order within the container | Exact order |
| Typical parts | Fasteners, brackets, electrical | Seats, cockpits, bumpers, wheels |
| Supplier distance | Can be regional | Minutes to a couple of hours |
| Risk if wrong | Shortage of a part | Wrong variant on a car, rework or line stop |

### Example
A car line produces a vehicle every 50 s with 6 seat variants. A seat supplier located 8 km away receives the sequence 140 minutes ahead (≈168 vehicles). It builds 168 seat sets in that order, loads trolleys in reverse unloading order and delivers. If the OEM re-sequences cars after the sequence point (for example, a paint defect pulls a car out), the supplier's seat set no longer matches: this "sequence break" is the main JIS cost driver and is managed by freezing the sequence late and keeping a small resequencing buffer.

### In the news
See news box. JIS parts are the most exposed to interruption because a missing or wrong module cannot be substituted from stock; commodity chips can be buffered, sequenced modules cannot.

### Interview angle
> [!question] How it is asked
> "What is just-in-sequence, and why would an OEM insist that a seat supplier locates next to its plant?"

> [!tip] Strong answer includes
> - The definition (right order, not only right time) with seats/cockpits as examples
> - Sequence point and freeze window; sequence-break cost
> - Trade-off: tiny inventory and no line-side variant picking vs supplier concentration and location rigidity
> - Where JIS pays: high variant count and high part volume per car

---
## 4. Inbound Logistics: Milk Run & Cross-Dock to the Line
> 🔴 Tier 1 · _Key points:_ milk run, cross-dock, consolidation hubs, frequency vs fill

### Definition
**Milk run**: one truck follows a fixed route and timetable collecting small quantities from several suppliers, then delivers to the plant (the OEM controls and pays for the route; the opposite of every supplier shipping its own partly empty truck). It turns many LTL shipments into one near-full truck and supports small-lot, frequent delivery, which JIT needs.

**Cross-dock**: inbound consignments from many suppliers are received at a consolidation hub near the plant, re-sorted by line-side location and shipped on to the line within hours with no put-away. Long-distance suppliers send full trucks to the hub; the hub supplies the plant with a short, frequent shuttle ([[010 Warehouse Management]], [[009 Logistics & Distribution]]).

Design variables: route length, pickup time windows, loading sequence (last in, first out at the plant gate), returnable packaging (the empty-container loop), and frequency (more trips lower inventory but raise transport cost).

### Example
Five Chakan-area suppliers each send a truck to the plant daily; each truck runs a 80 km round trip at ₹28/km: 5 × 80 × 28 = **₹11,200 per day**, at about 20% truck fill. A single milk-run loop of 120 km at ₹32/km (larger vehicle) costs 120 × 32 = **₹3,840 per day**, a saving of ₹7,360 a day (65.7%), about ₹22 lakh a year on 300 working days. Offsets: milk-run adds pickup waiting time and needs a planner; if one supplier misses its slot the whole loop is delayed, so time-window discipline and a buffer of a few hours at the plant are essential.

### In the news
See news box. Hubs and short loops cut inventory, but the Nexperia event showed that a shorter loop does not help when the upstream chip, not the truck, is missing.

### Interview angle
> [!question] How it is asked
> "A plant gets daily deliveries from 12 suppliers in one industrial belt, with half-empty trucks. What do you propose?"

> [!tip] Strong answer includes
> - Diagnose: truck fill, distance, delivery frequency, dock congestion
> - Milk run for nearby suppliers, cross-dock/consolidation hub for far ones
> - A simple cost calculation (trips × km × rate) and the inventory vs transport trade-off
> - Risks: slot discipline, returnable packaging, single carrier dependency

---
## 5. Kitting, Line-Side Delivery & Supermarkets
> 🔴 Tier 1 · _Key points:_ kits, supermarket, sub-assembly, line-side space, picking errors

### Definition
**Kitting** is picking all components for one vehicle (or one work station) into a container or trolley in advance, so the fitter handles one box. **Line-side supermarkets** are small stores near the line holding about 2-8 hours of components, replenished by tugger trains on fixed routes ("water spider" in lean terms).

Choice of delivery mode by part type:
- **Continuous supply** (bulk, standard, high volume): bins at the line (fasteners, clips).
- **Kitting** (many small variant parts): a kit per vehicle or per station.
- **Sequencing** (large, variant parts): see JIS.

Benefits: less line-side space, fewer fitting errors, shorter fitter walking time. Costs: extra handling and a kitting area; picking accuracy becomes critical (a wrong kit stops the station).

### Example
A model has 60 variant parts at a station. Line-side bins need 60 locations. With kitting, one kit holds a vehicle's 60 parts; if a picker makes errors on 0.2% of lines, a kit of 60 lines has a probability of at least one error of $1-(0.998)^{60} \approx 11.3\%$. Without error-proofing (barcode scan, pick-to-light), 1 in 9 kits would be wrong, a strong argument for pick-to-light plus a scanner check.

### In the news
See news box. Kits and supermarkets carry only hours of stock, so any upstream chip or magnet gap shows up on the line within a shift.

### Interview angle
> [!question] How it is asked
> "When would you kit parts instead of using line-side bins?"

> [!tip] Strong answer includes
> - Criteria: variant count, part size, line-side space, error cost
> - Quantified benefit: space, handling time, error rate
> - Error-proofing (poka-yoke) so picking errors do not stop the line
> - Link to warehouse picking technology ([[127 Warehouse Engineering - Racking, Sizing & Material Handling]])

---
## 6. VMI, Consignment & Supplier Hubs at the OEM
> 🔴 Tier 1 · _Key points:_ ownership transfer at consumption, min/max, supplier warehouse

### Definition
In **VMI** (vendor-managed inventory) the supplier monitors the OEM's stock of its parts and replenishes within agreed min-max limits. In **consignment**, stock sits at the OEM (or its hub) but remains owned by the supplier until it is **withdrawn into production**; only then is it invoiced. Auto OEMs often combine both with a **supplier hub** (supplier-run warehouse near the plant, often operated by a 3PL) so that the supplier can ship large batches cheaply and still deliver in small lots.

Effect on the OEM: lower inventory on its balance sheet and less administrative load. Effect on the supplier: it carries the inventory cost and demand risk, so price must recognise this. In SAP, consignment stock is handled as special stock "K" with settlement on consumption (see [[080 SAP MM — Materials Management]] and [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]]).

### Example
OEM uses ₹90 crore of components a year with an average ₹6 crore of that stock bought outright. Under consignment the ₹6 crore of stock sits on the supplier's books. At the OEM's 10% cost of capital the OEM saves ₹60 lakh a year. The supplier now carries the stock at, say, 12% cost of capital: ₹72 lakh a year, or 0.8% of the ₹90 crore of sales. If it can pool stock across several customers and hold less than ₹6 crore, the whole chain gains; if not, it will ask for a price rise of about 0.8% and the OEM's gain shrinks to roughly zero. The negotiation is therefore about who can hold inventory more cheaply and more safely.

### In the news
See news box. Consignment shifts financial exposure, not the physical shortage: when supply stopped, both parties lost, which is why OEMs started asking for visibility of chip stocks deep in the chain.

### Interview angle
> [!question] How it is asked
> "What is the difference between VMI and consignment, and who wins?"

> [!tip] Strong answer includes
> - Definitions: VMI is who plans replenishment, consignment is who owns the stock
> - Cash-flow effect for both parties, with a rough cost-of-capital calculation
> - Controls: min/max, consumption reporting, audit counts, liability if stock is damaged
> - Link to [[003 Inventory Management]] and [[136 Supply Chain Finance & Working Capital]]

---
## 7. Build-to-Order vs Stock Vehicles & Dealer Inventory
> 🔴 Tier 1 · _Key points:_ build-to-stock, build-to-order, wholesale vs retail, dealer days of stock

### Definition
Three customer-order models:
- **Build-to-stock (BTS)**: vehicles are built to a forecast, pushed to dealers, and customers buy from dealer stock. This is typical in India, where buyers want delivery in days.
- **Build-to-order (BTO)**: vehicle built after a customer order (typical for premium vehicles in Europe, special configurations and fleet orders). It needs a short, predictable lead time.
- **Hybrid** (postponement): common platforms and options built to stock, final configuration or accessories fitted after the order ([[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]).

India's **wholesale** (OEM dispatch to dealers) and **retail** (dealer to customer) numbers differ; when wholesale exceeds retail the difference piles up as dealer stock, financed by the dealer on a floor-plan loan. FADA flagged **about 50 days** of passenger-vehicle inventory at the end of FY2024-25 against a healthy norm of roughly 21-30 days (industry rule of thumb), and recorded record FY2024-25 retail registrations of 25,955,366 units (+10%).

### Example
A dealer sells 60 cars a month. At 50 days of stock he holds 60/30 × 50 = **100 cars**, at ₹8 lakh dealer cost = ₹8 crore; at 10% interest the carrying cost is **₹80 lakh a year**. At 35 days, stock is 70 cars (₹5.6 crore) and carrying cost ₹56 lakh: freeing ₹2.4 crore and saving **₹24 lakh a year**, before counting discounts and ageing stock. If the OEM pushes cars to hit its monthly wholesale target, the dealer's cash gets stuck, which feeds heavy end-of-month discounts and disputes.

### In the news
See news box. SIAM's FY26 data show wholesale growth of 7.9% in passenger vehicles; the supply-chain question is whether wholesale tracks real retail demand or builds stock.

### Interview angle
> [!question] How it is asked
> "Dealers hold 55 days of stock when the norm is 30. How would you fix it as the OEM's supply chain head?"

> [!tip] Strong answer includes
> - Cause: wholesale pushed above retail, wrong variant mix, slow models
> - Levers: align wholesale to retail (daily retail data), variant rationalisation, regional balancing (dealer-to-dealer transfers), BTO for slow variants
> - Quantify: days of stock → ₹ locked → carrying cost
> - S&OP link ([[120 Integrated Business Planning (IBP) & S&OP Maturity]])

---
## 8. Aftermarket & Spare Parts Logistics
> 🔴 Tier 1 · _Key points:_ service parts, fill rate, ABC/VED, hub-and-spoke, genuine vs independent aftermarket

### Definition
The **aftermarket** supplies replacement parts, accessories and consumables (batteries, tyres, filters, brake pads, body panels) over a vehicle's 10-15 year life. It is high-margin, steady, and demand follows the installed vehicle base (the "car parc") and age profile. Channels: OEM genuine parts through dealers and parts depots, **independent aftermarket** (IAM) through distributors and retailers, and increasingly online.

Spare-parts supply chain design: a central parts depot (CPD), regional distribution centres, dealer stock, with a **service level target** of ~95%+ for fast movers and an emergency order channel. Inventory classes: **ABC** by value, **FSN** by movement, **VED** by criticality (a "vehicle off-road" or VOR part gets a higher service level regardless of price). Obsolescence: when a model ends, OEMs must support spares for about 10 years or more, so end-of-production planning uses a last-time-buy ([[003 Inventory Management]], [[155 Reliability Engineering & Maintenance Optimisation]]).

Key measures: **fill rate** (lines or units shipped complete from stock), **VOR resolution time**, parts availability at dealer, and inventory turns.

### Example
A parts depot has 40,000 SKUs. Fast movers (6,000 SKUs) deliver 80% of demand at 98% fill, the remaining 34,000 SKUs are slow with 85% fill. If daily orders are 50,000 lines, lines filled = 0.8 × 50,000 × 0.98 + 0.2 × 50,000 × 0.85 = 39,200 + 8,500 = 47,700, an overall line fill of **95.4%**. Raising the slow-mover fill by pooling stock centrally to 90% adds 0.2 × 50,000 × 0.05 = 500 lines per day: the biggest gain per rupee comes from the long tail, but each extra point costs disproportionately more.

### In the news
See news box. The EV transition changes the aftermarket: fewer engine and exhaust parts, more battery and electronics parts; independent garages depend on OEM access to software and battery data.

### Interview angle
> [!question] How it is asked
> "How would you set stocking levels for a 50,000-SKU spare-parts network?"

> [!tip] Strong answer includes
> - Segmentation (ABC/FSN/VED) with differentiated service levels
> - Central vs regional stocking (risk pooling) for slow movers
> - VOR/emergency channel and end-of-life support rules
> - Metrics: fill rate, VOR days, obsolescence %

---
## 9. EV Supply Chain: Cells, Rare Earths, Localisation, PLI-Auto & ACC
> 🔴 Tier 1 · _Key points:_ battery cell cost share, magnets, DVA, PLI-Auto, PLI-ACC, import dependence

### Definition
An EV replaces the engine and gearbox (several hundred moving parts) with a **battery pack, motor and power electronics**. The new critical chain is: lithium, nickel, cobalt, manganese, graphite → cathode and anode materials → **cells** → pack (cells + BMS + cooling) → vehicle. The pack is the single costliest item, commonly estimated at about a quarter to 40% of an EV's cost depending on segment and chemistry (an estimate, not a fixed figure). Drive motors often use **permanent magnets with rare earths** (neodymium, dysprosium); China dominates processing.

India's policy stack:
- **PLI-Auto** (₹25,938 crore, approved 2021): sales-linked incentive on "advanced automotive technology" products with at least **50% domestic value addition (DVA)**; the scheme runs to FY2027-28.
- **PLI-ACC** (₹18,100 crore): 50 GWh of cell capacity allotted in 2022 to Ola Electric (20 GWh), Hyundai Global Motors (20 GWh), Reliance New Energy (5 GWh) and Rajesh Exports (5 GWh); incentive paid on batteries sold, with plants due within two years.
- Other levers: PM E-DRIVE, customs-duty design, the 2024 scheme to promote manufacturing of electric passenger cars in India (SPMEPCI) and state EV policies. See [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].

Strategic issue: India assembles packs from imported cells, so **localisation is shallow** (pack assembly is local, cells and magnets are not). Rare-earth shocks, battery chemistry shifts (LFP vs NMC) and cell-plant execution risk are the three big uncertainties.

### Example
Assumed (illustrative) numbers: 30 kWh pack, imported cell cost ₹7,500/kWh → cells ₹2.25 lakh = **25%** of a ₹9 lakh vehicle. If the rupee depreciates 5% against the dollar, cell cost rises ₹11,250 per car (+1.25% of vehicle price) with no change in volume; a pass-through price hike of 1.25% is then needed to hold margin.
For scale: the ACC scheme's allotted 50 GWh would have supplied about 1.67 million 30 kWh packs a year, whereas only 1.4 GWh (about 47,000 packs) was commissioned by October 2025 (2.8% of target).

### In the news
See news box. The ACC shortfall, PLI-Auto's 13.6 lakh EVs (mostly two-wheelers) and the magnet crisis together show the Indian EV story: assembly is scaling, cell and magnet depth is not yet.

### Interview angle
> [!question] How it is asked
> "India wants to localise EV batteries. What are the supply chain risks, and how would you de-risk a two-wheeler EV launch?"

> [!tip] Strong answer includes
> - Map the chain (minerals, cells, pack, motor, magnets) and the chokepoints (China processing)
> - Policy: PLI-Auto 50% DVA; PLI-ACC performance (2.8% delivered) as a caution on execution risk
> - Mitigation: multi-source cells (LFP/NMC), ferrite/rare-earth-free motor designs, buffer stock of magnets, long-term contracts, battery swapping and recycling ([[135 Reverse Logistics, Remanufacturing & EPR in India]])
> - Commodity price hedging ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]])

---
## 10. Semiconductor Shortage 2021-23 & the Nexperia Lesson
> 🔴 Tier 1 · _Key points:_ cancellation, allocation, bullwhip, long lead time, tier-N visibility

### Definition
In 2020 automakers cut chip orders as demand collapsed; foundries reassigned capacity to consumer electronics (laptops, phones) that boomed. When car demand returned in 2021, chip lead times were long (fabs plan 12-26+ weeks and cannot add capacity overnight), and auto, a small buyer of older-node chips, went to the back of the queue. AlixPartners estimated in September 2021 that the shortage would cost the global industry **$210 billion of revenue** in 2021 and **7.7 million vehicles** of lost production (versus $110 billion and 3.9 million estimated in May 2021).

Root causes: order cancellation and loss of priority, JIT with tiny chip buffers, single-source and high design-in switching cost (a chip change needs re-validation, often months), and lack of visibility beyond Tier 1. Responses: direct contracts and long-term agreements with chipmakers, partial stocking of critical chips (strategic buffer), design for multi-source, and sharing demand forecasts earlier. Related electronics supply chain issues are covered in [[134 Electronics & Semiconductor Supply Chain]].

### Example
At takt 50 s, 72 cars leave the line per hour. If each car sells for ₹8 lakh, one hour of line stoppage means ₹5.76 crore of delayed revenue; an 8-hour shift is about ₹46 crore. A chip that costs ₹40 per car (₹2,880 per hour at 72 cars) has therefore a stoppage cost ratio of 20,000:1, which is why a buffer of, say, 2 weeks of stock of such a chip is cheap insurance: at 1,080 cars/day × 14 days × ₹40 = ₹6.05 lakh of stock held, against crores per hour at stake.

### In the news
See news box. Nexperia 2025 repeated the pattern with a different trigger (government control and export controls, not capacity), and on a part category (simple discrete chips) that OEMs had assumed was abundant.

### Interview angle
> [!question] How it is asked
> "What did the automotive industry learn from the chip shortage, and what would you change in sourcing?"

> [!tip] Strong answer includes
> - Sequence of causes: demand cut, cancellation, reallocation, JIT with thin buffer, tier-N blindness
> - Quantification: stoppage cost per hour vs cost of buffer
> - Actions: criticality classification of electronic parts, buffers on high-risk parts, multi-sourcing/design flexibility, direct supply agreements, tier-N mapping
> - Balance: do not buffer everything; this is a risk-weighted decision ([[015 Supply Chain Risk & Resilience]], [[141 Supply Chain Disruption Case Library (2011-2026)]])

---
## 11. Tyre Supply Chain
> 🔴 Tier 1 · _Key points:_ natural rubber, OE vs replacement, dealers, imports, exports, retreading

### Definition
Tyres are a raw-material-heavy, working-capital-heavy product: natural rubber (NR), synthetic rubber, carbon black, steel cord, fabric and chemicals. Two markets: **OE** (supplied to vehicle makers in JIT/JIS-style schedules, low margin, brand building) and **replacement** (the larger share of demand in most markets, sold through multi-tier dealer networks, higher margin). Truck-and-bus radialisation, farm and off-highway tyres, and exports shape the mix.

Indian facts (ATMA / IBEF, FY2025): industry turnover about ₹99,942 crore; exports ₹25,051 crore (+9%) to 170+ countries; farm and off-the-road tyres are nearly 60% of export value; natural rubber is about 60% of rubber consumption (higher than the global norm), and **imports cover around 40%** of the industry's NR needs; ₹27,000 crore of expansion invested over four years. NR is grown mainly in Kerala (smallholders), so raw-material price and import-duty swings pass directly into tyre margins. Retreading and recycling close the loop ([[135 Reverse Logistics, Remanufacturing & EPR in India]]).

### Example
A truck-tyre plant makes 10,000 tyres a day with an assumed 19 kg of natural rubber each: 190 tonnes of NR a day. A ₹10 per kg rise in NR price costs 190,000 × 10 = ₹19 lakh a day, or ₹62.7 crore over 330 production days. Unless contract pricing passes this on with a lag, margin falls; this is why tyre makers use price-linked formulas, buy forward and hold raw-material stock of 30-60 days ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]).

### In the news
> [!news] Tyre makers squeezed by rubber prices (2026)
> Business Standard reported (24 August 2026) that natural rubber, nearly half of the industry's raw-material cost, averaged about ₹220/kg in FY26 but reached ₹275/kg in June 2026 (about +25%); the raw-material basket rose 16-20% sequentially in Q1 FY27, operating margins were projected to fall from about 14.2% to 11.5-12% in FY27, and CEAT, Apollo and JK had taken cumulative price hikes of roughly 9-11% against a needed 15-16%. Six large makers plan about ₹18,000 crore of capex over FY27-28. Separately, tyre exports hit a record ₹27,312 crore in FY26 (+9%); the US, the largest market (15%, ₹4,082 crore), saw tariffs rise from 25% to 50% in August 2025 and fall to 18% in February 2026, per the same newspaper. ([Business Standard, Aug 2026](https://www.business-standard.com/industry/news/tyre-makers-capex-expansion-margins-natural-rubber-prices-126082400607_1.html), [Business Standard, Jun 2026](https://www.business-standard.com/industry/news/indian-tyre-exports-hit-record-high-in-fy26-despite-global-challenges-126060301000_1.html))

Tyres and wheels for new vehicles are often sequenced to the line like seats, so the same JIT discipline applies on the OE side.

### Interview angle
> [!question] How it is asked
> "A tyre maker's margin has fallen 3 points. How do you analyse the supply chain?"

> [!tip] Strong answer includes
> - Cost structure: NR/SR/carbon black share, price vs contract lag, forex
> - Channel mix: OE vs replacement, dealer inventory and credit days
> - Fixes: formula pricing, import mix, retreading, mix shift to higher-margin radials/OTR
> - Working capital: raw-material days and finished-goods days

---
## 12. India's Auto Clusters & Manufacturing Geography
> 🔴 Tier 1 · _Key points:_ Chennai, Pune-Chakan, NCR, Gujarat, Bengaluru-Hosur, supplier parks

### Definition
Auto assembly clusters form where OEMs, Tier-1s, ports and skilled labour co-locate, so milk runs and JIS become feasible:
- **Chennai-Sriperumbudur-Hosur**: Hyundai, Renault-Nissan, BMW, Daimler, Ashok Leyland, TVS, plus deep-water ports (Chennai, Kattupalli, Ennore) for exports.
- **Pune-Chakan-Pimpri (and Aurangabad/Waluj)**: Tata Motors, Mahindra, Bajaj, Mercedes-Benz, VW group; large Tier-1 base. Closest to the Nashik region of the SIOM campus.
- **NCR (Gurugram-Manesar-Neemrana-Kharkhoda)**: Maruti Suzuki, Hero MotoCorp, Honda 2W and the largest component base in north India.
- **Gujarat (Sanand-Hansalpur)**: Tata (including EV), Suzuki Motor Gujarat (Maruti's Gujarat plant); near Mundra/Pipavav ports.
- **Bengaluru-Bidadi**: Toyota Kirloskar; **Jamshedpur** and **Pantnagar**: commercial vehicles.

Advantages: shared suppliers, short lead times, shared infrastructure. Disadvantages: concentrated risk (floods in Chennai 2015, 2023), labour pressure on wages, and need for **supplier parks** (inside or adjacent to OEM land) to host JIS suppliers. Government logistic schemes such as Gati Shakti and the National Logistics Policy aim to reduce logistics cost ([[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]], [[223 Logistics, Manufacturing & Industry Data Points - India]]).

### Example
For a new EV plant with 60% of bought-in parts by value from suppliers: if 40 Tier-1s would each need a JIS-capable location, the OEM can compare a **cluster site** (existing suppliers, say average 40 km, 3-hour delivery window) against a **greenfield site** (average 400 km, 1-day transit plus 3-day pipeline stock). With 2,000 vehicles a day and ₹3.2 lakh of bought-in parts per vehicle on JIS/JIT, adding 3 days of pipeline stock = 2,000 × 3 × 3.2 lakh = ₹192 crore of extra stock; at 10% cost of capital, ₹19.2 crore a year, before extra freight: a major reason why cluster presence outweighs a cheaper land offer.

### In the news
See news box. State incentive competition (Gujarat, Tamil Nadu, Maharashtra) for EV and battery plants builds on the PLI schemes; clusters decide where cell and pack plants go.

### Interview angle
> [!question] How it is asked
> "Where would you set up a new EV plant in India and why?"

> [!tip] Strong answer includes
> - Criteria: supplier base, port access, labour, power, state incentives, land
> - Quantify pipeline stock and freight difference between sites
> - Risk: flood or political concentration; second-source location
> - Link with national policy (PLI, Gati Shakti) and talent

---
## 13. Vehicle Outbound Logistics: Car Carriers, RoRo & Rail
> 🔴 Tier 1 · _Key points:_ car carrier trailers, rail auto rakes, RoRo, coastal, yard management, transit damage

### Definition
Finished vehicles go from the plant yard to **stockyards**, then to dealers (domestic) or to ports (exports). Modes:
- **Road car carriers**: multi-deck trailers carrying 6-10 cars; flexible for short and regional runs; transit damage and overloading rules are the main issues.
- **Rail**: dedicated auto-carrier wagons, run as full rakes between plant sidings and hubs; cheaper and lower CO2 on long distances.
- **RoRo (roll-on/roll-off) ships** for exports and coastal movement; vehicles are driven on and off, which lowers handling time and damage.
- **Yard and PDI** (pre-delivery inspection) management: sequencing loads, damage inspection, ageing stock.

Data: in 2024-25 India moved about **1.25 million cars by rail out of 5.06 million** moved across all modes, a rail share of about **24.5%**, up from 1.5% in 2013-14 and 14.7% four years earlier; rail "cut the road's share in half" on routes over 600 km. Maruti Suzuki dispatched 496,600 vehicles by rail in 2024 (up from 422,300 in 2023) and targets 35% of dispatches by rail by 2030-31; Hyundai Motor India sent 156,724 vehicles by rail in 2024, about 26% of its domestic wholesale volume ([[125 Transportation Management Deep Dive]], [[009 Logistics & Distribution]]).

### Example
A plant ships 1,000 cars a week to a destination 1,600 km away. Assume (illustrative) road costs ₹30,000 per car and rail ₹22,000, so rail saves ₹8,000 per car: **₹80 lakh a week**. Rail needs about 1.5 extra days of transit, which adds a pipeline of 1,000/7 × 1.5 ≈ 214 cars. At ₹7 lakh a car and 10% annual carrying cost, that extra stock costs 214 × 7 lakh × 10% ≈ ₹1.5 crore a year, or about **₹2.9 lakh a week**. Net benefit ≈ ₹77 lakh a week, so rail wins clearly when lane volume fills rakes, pickup is predictable and the plant has a siding. Road keeps the small-drop, last-mile and urgent flows.

### In the news
See news box. Rail's rising share and the target of 35% for Maruti are the outbound counterpart to export growth (PV exports 9.05 lakh in FY26).

### Interview angle
> [!question] How it is asked
> "Should Maruti move more cars by rail? What is the trade-off?"

> [!tip] Strong answer includes
> - Cost per car-km, transit time, damage, flexibility, carbon
> - Rail works at lane volume (full rake), road at small drops and last mile
> - Pipeline inventory cost of longer transit vs freight saving
> - Enablers: plant sidings, rake planning, terminals, Gati Shakti

---
## 14. ⭐ Advanced: Automotive KPIs & a Resilience Scorecard
> ⭐ Advanced · _Added beyond the tracker_

### Definition
KPI tree for an OEM supply chain (compare with [[012 Supply Chain Analytics & KPIs]], [[018 Capacity Management & OEE]]):
- **Supplier delivery**: OTIF %, premium (expedited) freight as % of freight, line stoppages caused by supply (minutes).
- **Quality**: supplier PPM = defective parts / parts delivered × $10^6$; first-time-right at PPAP; warranty cost per vehicle.
- **Inventory**: days of inventory by tier (raw, WIP, FG); **dealer stock days**; ageing stock > 90 days.
- **Production**: OEE, takt adherence, schedule attainment (planned vs actual by variant).
- **Aftermarket**: fill rate, VOR hours.
- **Cost and ESG**: logistics cost per vehicle, CO2 per vehicle shipped, rail share.
- **Resilience**: % of critical parts single-sourced, time-to-recover (TTR) and time-to-survive (TTS) by part, tier-N visibility %.

Resilience scoring: rank parts by $\text{risk} = \text{probability} \times \text{impact}$, where impact = line stoppage cost per hour × TTR hours not covered by buffer. Buffer where the ratio is highest.

### Example
A supplier delivered 1.2 million parts last quarter with 37 defective: PPM = 37 / 1,200,000 × 10⁶ = **30.8 PPM**. If OTIF is 97% of lines on time and 99% in full, and the two are independent, combined OTIF is 0.97 × 0.99 = **96.0%**. At 500 supplier lines per day, 20 lines (4%) are failures each day: each is a potential stoppage or expedited truck.
Resilience: a chip with TTR 10 weeks, stock cover 2 weeks and stoppage cost ₹46 crore per shift is a top-risk item; a bracket with 3 alternative sources and 1-week TTR is low risk despite larger volume.

### In the news
See news box. After 2021 and 2025, many OEMs added tier-N visibility and critical-part buffers to their KPI sets.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track to run an auto plant's supply chain, and how would you prioritise resilience investments?"

> [!tip] Strong answer includes
> - A balanced set: delivery, quality, inventory, cost, resilience, with definitions
> - PPM and OTIF calculations done correctly
> - Risk-weighted prioritisation, not buffering everything
> - How the KPIs are used (supplier scorecards, QBR, sourcing decisions) and the link to [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]
