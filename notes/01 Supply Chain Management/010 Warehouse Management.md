---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Warehouse Management"
tier: Tier 2
roles: Operations
status: complete
subtopics: 14
---
# Warehouse Management

⬅ [[009 Logistics & Distribution]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[011 Quality Management (TQM)]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Warehouse Layout Types]]
2. [[#2. Slotting Optimization]]
3. [[#3. Picking Methods]]
4. [[#4. Put-Away Strategies]]
5. [[#5. Automated Storage & Retrieval (ASRS)]]
6. [[#6. RFID & Barcode Systems]]
7. [[#7. Inventory Accuracy]]
8. [[#8. Warehouse KPIs]]
9. [[#9. Returns Processing]]
10. [[#10. Goods Receipt Process]]
11. [[#11. Value-Added Services in Warehouse]]
12. [[#12. Safety & Compliance]]
13. [[#13. ⭐ Advanced: Cross-Docking & Dock Scheduling]]
14. [[#14. ⭐ Advanced: Automation Business Case (AMR, Goods-to-Person, ASRS)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Robots in the warehouse and India's first logistics-cost benchmark
> **Amazon's one-millionth warehouse robot (Jul 2025).** Amazon said it had deployed 1 million robots across its fulfilment network, with the millionth unit delivered to a facility in Japan, and launched "DeepFleet", a generative-AI model that coordinates robot traffic and was reported to make the robot fleet about **10% faster**. Its next-generation fulfilment centres are described as having about **10x as many robots** as current sites, working alongside human staff. ([TechCrunch](https://techcrunch.com/2025/07/01/amazon-deploys-its-1-millionth-robot-releases-generative-ai-model/))
>
> **India's logistics cost at 7.97% of GDP (Sep 2025).** The DPIIT-NCAER study put India's logistics cost at **7.97% of GDP in FY2023-24 (about ₹24.01 lakh crore)**, far below the earlier "13–14%" perception. It found warehousing averaging **₹30 per sq ft per month**, with cold storage at about **₹58.5**, and that small firms spend **16.9% of output** on logistics versus **7.6%** for large firms. ([Logistics Insider](https://www.logisticsinsider.in/indias-logistics-cost-at-7-9-of-gdp-report/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Warehouse Layout Types
> 🟠 Tier 2 · _Tracker hint:_ U-flow, I-flow, L-flow; receiving vs dispatch zoning

### Definition
Layout decides how goods **flow** through the building, from inbound docks to storage, picking, packing and outbound docks. The flow shape sets travel distance, dock utilisation and room for expansion.

| Flow | Receiving and dispatch | Strengths | Weaknesses |
|---|---|---|---|
| **I-flow (straight-through)** | Opposite walls | Simple, one-way, high throughput, easy to separate inbound and outbound traffic | Needs two building faces; long walk if goods are stored and retrieved across the full length; docks cannot be shared |
| **U-flow** | Same wall, side by side | Shared dock equipment and staff, short path for cross-docking, three free walls for expansion, good security (one access side) | Dock congestion at peak; inbound and outbound can interfere |
| **L-flow** | Adjacent walls | Suits plots with a corner access; good when inbound and outbound volumes differ | Fewer standard reference designs; some cross-aisle travel |

**Zoning principles:** keep receiving, quality hold, bulk storage, forward pick area, packing and dispatch staging as distinct zones; put the highest-velocity SKUs closest to the dispatch end; separate hazardous, cold and high-value zones; size staging by peak-hour volume.

### Example
Illustrative: a plot allows a 120 m by 60 m shed. With I-flow, a pallet received at one end and shipped from the other end travels about 120 m through the storage area. With U-flow, receiving and dispatch sit on the same 60 m wall; a pallet that is cross-docked travels roughly 20–30 m and the same 10 dock doors serve both inbound in the morning and outbound in the evening (good dock utilisation when volumes are time-separated).

### In the news
See news box. As robots and goods-to-person systems spread (Amazon), the layout is being designed around robot lanes and station placement, not only forklift aisles.

### Interview angle
> [!question] How it is asked
> "Which warehouse layout would you choose for an e-commerce DC versus a cross-dock for an FMCG distributor?"

> [!tip] Strong answer includes
> - Names the three flows and where docks sit in each
> - Links the choice to volume profile (cross-dock heavy favours U; high-throughput steady flow favours I)
> - Mentions expansion, security and dock sharing as secondary criteria
> - Mentions zoning (receiving, QC hold, reserve, forward pick, pack, dispatch) and velocity-based placement

---

## 2. Slotting Optimization
> 🟠 Tier 2 · _Tracker hint:_ Fast movers near dispatch; ABC-based slotting; velocity analysis

### Definition
**Slotting** assigns each SKU to a storage location to minimise picker travel and handling while respecting weight, cube, safety and compatibility rules.

Steps: (1) **velocity analysis**: rank SKUs by picks (lines) per period, not just units; (2) **ABC classes**: A = about 20% of SKUs giving about 80% of picks, placed in the **golden zone** (waist-to-shoulder height, nearest the pack/dispatch end); (3) apply constraints: heavy items low, fragile in protected spots, hazmat segregated; (4) **re-slot** periodically as seasonality changes demand.

A classic rule is the **Cube-per-Order Index (COI)**:

$$COI = \frac{\text{Storage cube required for the SKU}}{\text{Number of picks (orders) per period}}$$

Lowest COI goes closest to dispatch. Slotting by popularity alone ignores bulky items; COI balances both.

### Example
SKU A needs 0.50 m³ and is picked 1,000 times a month: COI = 0.50/1000 = **0.0005**. SKU B needs 0.20 m³ and is picked 100 times: COI = 0.20/100 = **0.0020**. A is slotted closer, even though B takes less space. If the A pick face is 20 m closer to dispatch, saving is 1,000 picks x 20 m x 2 (round trip) = 40,000 m a month, about 40 km of walking avoided.

### In the news
See news box. India's warehouse rents (about ₹30 per sq ft per month on average) make every unnecessary square foot costly, so slotting and density matter.

### Interview angle
> [!question] How it is asked
> "Pickers walk too much in our warehouse. What would you do?"

> [!tip] Strong answer includes
> - Start with data: pick-line frequency by SKU, SKU cube, order profiles
> - ABC placement plus COI, and affinity slotting (items ordered together placed near each other)
> - Golden zone ergonomics and heavy-low rule
> - Seasonal re-slotting and measuring the gain (travel distance, lines per hour)

---

## 3. Picking Methods
> 🟠 Tier 2 · _Tracker hint:_ Order picking, batch picking, zone picking, wave picking

### Definition
Order picking is typically **50–60% of warehouse operating cost**, the largest labour component (a widely quoted textbook figure), so method choice matters.

| Method | How it works | Best for |
|---|---|---|
| **Discrete (order) picking** | One picker picks one order start to finish | Few lines per order, low volume |
| **Batch picking** | Picker collects several orders' items in one trip, sorted later (or into cartons while picking) | Many small orders, overlapping SKUs |
| **Zone picking** | Each picker stays in a zone; orders pass zone to zone (pick-and-pass) or are consolidated | Large facilities, many SKUs |
| **Wave picking** | Orders released in timed waves, for example by carrier cut-off or priority | Scheduled dispatch, shared dock capacity |

Enablers: pick-to-light, voice, RF scanners, goods-to-person and robot-assisted picking. Trade-off: batching cuts travel but adds a sorting step and error risk.

### Example
Illustrative: 10 orders, each one line. Discrete: 10 trips x 200 m = 2,000 m. Batch picking of 5 orders per trip with a longer trip of 260 m: 2 trips x 260 m = 520 m, a **74% reduction** in travel ((2000-520)/2000 = 74%), at the cost of sorting 5 orders after the trip.

### In the news
See news box. Amazon's robots bring shelves to stations (goods-to-person), eliminating the pickers' walking altogether; DeepFleet aims at faster robot routing.

### Interview angle
> [!question] How it is asked
> "Which picking method for a grocery e-commerce DC with 8 lines per order and cut-off at 4 pm?"

> [!tip] Strong answer includes
> - Defines methods and picks a hybrid (zone plus batch plus wave)
> - Reasoning from order profile: lines per order, SKU count, cut-off times
> - Notes error and sorting trade-offs
> - Names the KPI to track: lines picked per hour, travel per pick, accuracy

---

## 4. Put-Away Strategies
> 🟠 Tier 2 · _Tracker hint:_ Fixed location, random location, closest open slot

### Definition
**Put-away** moves received goods from the dock to a storage location and records it.

- **Fixed (dedicated) location:** each SKU has its own slot. Easy to learn and pick, but space is sized for each SKU's *maximum* stock, so utilisation is low.
- **Random (floating) location:** any SKU goes to any free slot, tracked by WMS. Higher space utilisation, needs accurate system data, may increase picker travel.
- **Closest open location:** the first free slot nearest the dock; fast put-away but fast and slow movers mix.
- **Class-based (zoned):** the ABC class has a zone, and random within it; the usual compromise.
- Other rules: **directed put-away** by WMS using weight, size, FEFO/batch, hazard class and pick-face replenishment need.

### Example
Illustrative: 10 SKUs, each with maximum stock of 100 pallets, but never all at peak together; the aggregate peak is 600 pallets. Fixed slots need 10 x 100 = **1,000 positions**; random needs about **600** (plus a buffer). That is a 40% saving in positions, bought with a WMS and location discipline.

### In the news
See news box. At Amazon-style sites, "chaotic storage" (random, WMS-tracked bin placement) is standard because robots and software, not people, remember locations.

### Interview angle
> [!question] How it is asked
> "Fixed or random storage for 50,000 SKUs? What are the risks?"

> [!tip] Strong answer includes
> - Defines fixed vs random vs closest-open vs class-based
> - Utilisation vs travel and data-accuracy trade-off
> - Notes WMS dependency and inventory-accuracy risk
> - Recommends class-based with directed put-away, with a reason

---

## 5. Automated Storage & Retrieval (ASRS)
> 🟠 Tier 2 · _Tracker hint:_ Vertical carousels, mini-load, unit-load, shuttle systems

### Definition
**AS/RS** uses computer-controlled machines to store and retrieve loads from defined locations.

| Type | Load | Typical use |
|---|---|---|
| **Unit-load** | Pallets (up to about 1 tonne or more), crane in aisle | Bulk, high-bay, cold stores |
| **Mini-load** | Totes/cartons, small crane | Spare parts, e-commerce |
| **Shuttle** | Shuttle moves within each rack level; lifts handle vertical | High throughput, flexible |
| **Vertical lift module / vertical carousel** | Trays in an enclosed column | Small parts, saves floor space, ergonomics |
| **Horizontal carousel** | Rotating bins | Order picking in small zones |

Benefits: space (high-bay), accuracy, labour saving, safety. Costs: high capex, lower flexibility, single-point-of-failure risk, need for stable SKU profiles.

Crane throughput (moves per hour) = 3600 / cycle time in seconds. A dual-command cycle (store and retrieve in one trip) improves productivity.

### Example
Illustrative: a unit-load crane does a single-command cycle in 60 s: 3600/60 = **60 moves/hour**. A dual-command cycle of 90 s completes 2 moves: 3600/90 x 2 = **80 moves/hour**, a 33% gain.

### In the news
See news box. Automation is accelerating globally (1 million robots at Amazon), but India's low labour and rent cost per sq ft means the ROI case must be built carefully (see the advanced section on automation business cases).

### Interview angle
> [!question] How it is asked
> "Would you recommend an ASRS for this 3PL warehouse?"

> [!tip] Strong answer includes
> - Names ASRS types and which fits the load
> - Conditions that justify it: high volume, stable SKU profile, expensive space, labour shortage, accuracy needs
> - Quantifies payback with capex, labour and space saved
> - Mentions downtime risk, maintenance and scalability

---

## 6. RFID & Barcode Systems
> 🟠 Tier 2 · _Tracker hint:_ Real-time tracking, scan-on-receive, cycle counting

### Definition
- **Barcode** (1D linear, 2D such as QR/Data Matrix, with GS1 standards like GTIN, SSCC): optical, needs line of sight, scans one item at a time, very cheap.
- **RFID** (UHF tags in the 860–960 MHz band, EPC Gen2): reads many tags without line of sight, can write data, higher tag cost, affected by metals and liquids.

Uses in a warehouse: **scan-on-receive** (match ASN/PO, create GRN), put-away confirmation by location scan, pick verification, packing and dispatch scan, **cycle counting** and real-time stock visibility. The **SSCC** (18-digit) identifies a pallet or carton for ASN-based receiving.

Choice: barcode when volumes are high and unit value low; RFID when item value, count speed or visibility justify the tag cost (apparel, pharma, returnable assets).

### Example
Counting 10,000 items. Barcode at 5 s per item: 50,000 s = **13.9 hours**. RFID reader at an assumed 600 tags per minute: 10,000/600 = **about 17 minutes**. Inditex (Zara) is well known for tagging garments with RFID to gain item-level store and stock visibility.

### In the news
See news box. Robot fleets depend on accurate bin and item identification; the data layer (barcode/RFID) is what lets chaotic storage work.

### Interview angle
> [!question] How it is asked
> "Barcode or RFID for a pharma distributor? Justify."

> [!tip] Strong answer includes
> - Technical difference (line of sight, bulk read, cost)
> - Business benefit: speed, accuracy, traceability (batch/expiry)
> - Cost-benefit: tag cost vs shrinkage and labour saved
> - Process integration: scan-on-receive, put-away, cycle count

---

## 7. Inventory Accuracy
> 🟠 Tier 2 · _Tracker hint:_ Cycle counting vs physical count; LIFO/FIFO/FEFO

### Definition
**Inventory record accuracy (IRA)** = locations (or SKUs) where system quantity equals physical quantity / locations counted. Best-in-class DCs aim for 98–99.9%.

- **Physical (wall-to-wall) count:** all stock counted at once, usually at year end; operations stop, error-prone.
- **Cycle counting:** counting a subset daily so that every item is counted at a planned frequency; ABC-based (A items counted more often); finds root causes early, no shutdown.

**Issue and valuation rules:** **FIFO** (first in, first out: oldest stock issued first), **FEFO** (first expired, first out: for perishables, pharma, FMCG with batch expiry), **LIFO** (last in first out). Note that LIFO is **not permitted for inventory valuation under Ind AS 2** (and IFRS); FIFO and weighted average are used.

### Example
IRA: 480 of 500 locations counted match the system: 480/500 = **96%**. Cycle count plan: 500 A-items counted 4 times a year = 2,000 counts; over 250 working days = **8 counts a day**.

### In the news
See news box. Accurate inventory records are the precondition for robots and WMS to find stock; without them automation only moves errors faster.

### Interview angle
> [!question] How it is asked
> "System shows stock but pickers find none. How do you improve inventory accuracy?"

> [!tip] Strong answer includes
> - Cycle count vs physical count, with ABC frequency
> - Root causes: receiving errors, mis-picks, location errors, theft, unit-of-measure errors
> - Process controls: scan-on-receive, location verification, adjustments approval
> - FIFO/FEFO for expiry-bound goods, and that LIFO is not allowed under Ind AS 2

---

## 8. Warehouse KPIs
> 🟠 Tier 2 · _Tracker hint:_ Order fill rate, pick accuracy%, lines picked/hr, cost/order

### Definition
| KPI | Formula |
|---|---|
| Order fill rate | Orders shipped complete / orders received |
| Pick accuracy % | (Lines picked - lines with errors) / lines picked |
| Lines picked per hour | Lines picked / picker labour hours |
| Cost per order | Total warehouse cost / orders shipped |
| Dock-to-stock time | Time from truck arrival or GRN to available stock |
| On-time dispatch % | Orders dispatched before cut-off / total |
| Inventory accuracy | Matching locations / counted |
| Space utilisation | Used positions / available positions |

Use a balanced view (service, quality, productivity, cost) and watch trade-offs: pushing lines per hour can lower accuracy. Pick accuracy is often quoted in parts per million (PPM) errors for high-performance sites.

### Example
10,000 orders shipped in a month; 9,700 shipped complete: fill rate = **97%**. 12 wrong lines out of 4,000 picked: accuracy = (4000-12)/4000 = **99.7%**. 4,000 lines by 8 pickers x 8 hours = 64 labour hours: 4000/64 = **62.5 lines per hour**. Cost ₹3,00,000 for 10,000 orders: **₹30 per order**.

### In the news
See news box. NCAER found that small firms spend 16.9% of output on logistics versus 7.6% for large ones, showing scale and process discipline are cost levers.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track for a new DC and what are the targets?"

> [!tip] Strong answer includes
> - A balanced set: service, quality, productivity, cost, inventory
> - Exact formulas and definitions (what is an in-full line?)
> - The trade-off between productivity and accuracy
> - Dashboards with owners, thresholds and root-cause drill-down

---

## 9. Returns Processing
> 🟠 Tier 2 · _Tracker hint:_ Triage, restocking, liquidation, disposal workflow

### Definition
**Reverse logistics** handles returned goods. Workflow: **receive and log** (RMA match) → **inspect and grade** (A like-new, B refurbishable, C damaged, D scrap) → **disposition**: restock, refurbish/repack, return to vendor (RTV), liquidate (B2B resale, outlet), donate, recycle or dispose → **update** inventory and financial credit.

Principles: speed (value decays with time), clear grading rules, root-cause capture (wrong size, defect, fraud), separate returns area, hazard/e-waste compliance. Returns are structurally high in online fashion (about 20–30%, as noted in Topic 001) and in COD orders (RTO, return to origin).

**Recovery rate** = value recovered / original cost of returned goods.

### Example
100 returned units, cost ₹800 each (₹80,000). 60 restocked at full cost value = ₹48,000. 25 refurbished and recovered at 50% = ₹10,000. 15 liquidated at 20% = ₹2,400. Recovery = 60,400/80,000 = **75.5%**.

### In the news
See news box. High-volume e-commerce DCs now need dedicated returns lanes and fast grading; robots and automated sorters are being applied to the returns flow too.

### Interview angle
> [!question] How it is asked
> "Return rate for our online apparel business is 30%. How do you cut the cost of returns?"

> [!tip] Strong answer includes
> - Splits the problem: prevent returns (size guides, QC) vs process returns faster/cheaper
> - Triage and disposition tree with timelines
> - Recovery-rate maths and channel choice (liquidators, outlets)
> - Data feedback loop to merchandising and suppliers

---

## 10. Goods Receipt Process
> 🟠 Tier 2 · _Tracker hint:_ PO match, quality inspection, GRN, system update

### Definition
Steps: **advance notice (ASN) and dock appointment** → **unloading and visual check** (seals, damage) → **identify and count** against the PO or delivery note → **quality inspection** (sampling, see [[011 Quality Management (TQM)]]) → **GRN (Goods Receipt Note)**: record accepted, rejected, short and excess quantities → **system update**: stock increases, PO is updated, accrual (GR/IR) is posted → **put-away** → **three-way match** of PO, GRN and supplier invoice before payment.

In SAP, goods receipt against a purchase order is done in **MIGO** with movement type **101**; quality-managed items go to quality-inspection stock. Tolerances for over and under-delivery are defined on the PO line.

### Example
PO for 1,000 units. Truck brings 1,000; inspection rejects 20; GRN accepts 980 and records 20 rejected. Payment is made only for 980 units (invoice for 1,000 is blocked or credit-noted). Dock-to-stock time is measured from truck arrival to the 980 units being available.

### In the news
See news box. Fast, accurate receiving at the dock is where inventory accuracy starts; every error here propagates into pick failures later.

### Interview angle
> [!question] How it is asked
> "Walk me through what happens when a supplier truck arrives."

> [!tip] Strong answer includes
> - The full sequence from appointment to put-away
> - Controls: PO match, tolerance, quality sampling, GRN
> - System impact (inventory, accrual, three-way match)
> - KPIs: dock-to-stock time, receiving accuracy, supplier ASN compliance

---

## 11. Value-Added Services in Warehouse
> 🟠 Tier 2 · _Tracker hint:_ Kitting, labeling, light assembly, postponement

### Definition
VAS are activities done in the warehouse beyond store-and-ship: **kitting** (bundling components into one SKU), **labelling and re-labelling** (MRP stickers, language, barcode), **light assembly and packaging**, **gift-wrap, personalisation, quality checks, repair/refurbish** and **postponement**, delaying final customisation (packaging, labelling, configuration) until the actual order is known.

Benefits: pooled inventory of generic (undifferentiated) product lowers safety stock; faster response; revenue for 3PLs. Risks: labour complexity, space, regulatory compliance (for example Legal Metrology labelling rules for packaged goods in India).

Postponement works because pooling reduces variability: safety stock of the common item scales with the square root of the number of variants pooled.

### Example
HP's DeskJet printers for different countries differed only by power supply and manual; shipping generic printers and finishing locally at the regional DC (the classic postponement case) reduced inventory and stock-outs. Numeric toy: 4 country variants each with safety stock 500 units; one generic stock pooled needs about 500 x sqrt(4) = **1,000 units** vs **2,000** before.

### In the news
See news box. NCAER's finding that small firms carry heavy logistics cost supports outsourcing VAS to 3PLs that spread them over scale.

### Interview angle
> [!question] How it is asked
> "How can a 3PL create more value than storage and transport?"

> [!tip] Strong answer includes
> - Lists VAS with a business reason for each
> - Explains postponement and risk pooling with a number
> - Mentions pricing models (per unit or per hour) and compliance
> - Notes capacity and quality risks

---

## 12. Safety & Compliance
> 🟠 Tier 2 · _Tracker hint:_ Fire, racking standards, load limits, ergonomics

### Definition
Key areas:
- **Fire:** sprinkler design for storage class and rack height, fire exits, extinguishers, hydrant system, emergency drills; in India, building fire norms in the **National Building Code (NBC 2016)** and a local Fire NOC.
- **Racking:** installed to manufacturer design; **load plates** show beam capacity (per level and per bay), pallets in good condition, regular inspection for damage (forklift impact), anchoring, no overloading.
- **Material handling:** forklift licensing, speed limits, pedestrian segregation, battery charging safety, dock restraints.
- **Ergonomics:** limit manual lifting. The NIOSH recommended weight limit starts from a **load constant of 23 kg** and is reduced by factors for height, distance, twist and frequency.
- **Law:** in India workplace safety is governed by the Factories Act, 1948 and the OSH Code 2020 (which consolidates several labour laws); a good answer names the principle without over-claiming section numbers.
- Hazmat segregation, safety signage, near-miss reporting and **lost-time injury rate**: $\frac{\text{lost-time injuries} \times 200{,}000}{\text{hours worked}}$ (OSHA-style incident rate).

### Example
A beam level is rated at 2,000 kg per pair. Three pallets of 800 kg each give 3 x 800 = 2,400 kg, which is **20% over** capacity (400/2000), so a pallet must be removed or moved to a heavier-rated level.

### In the news
See news box. As humans and robots share floors (Amazon's next-generation sites), zoning, speed limits and safety interlocks become central safety design issues.

### Interview angle
> [!question] How it is asked
> "You find overloaded racks and blocked fire exits during your first week as warehouse manager. What do you do?"

> [!tip] Strong answer includes
> - Immediate risk containment (unload, cordon, clear exits), then root cause
> - Regular inspections, load plates, audits and training
> - Compliance awareness (NBC, Factories Act/OSH Code)
> - Safety KPIs and a culture of near-miss reporting

---

## 13. ⭐ Advanced: Cross-Docking & Dock Scheduling
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Cross-docking** moves inbound goods to outbound vehicles with little or no storage (typically under 24 hours). Types: **pre-allocated** (each inbound carton already assigned to a store), **post-allocated** (allocation after arrival), **continuous** (for perishables) and **consolidation/deconsolidation**. It suits predictable flows, high-velocity items and reliable suppliers, and needs ASN data, barcode labels per destination and synchronised dock doors.

**Dock scheduling** assigns appointment slots to trucks to avoid congestion; the number of dock doors needed is approximately

$$N = \frac{\text{trucks per peak hour} \times \text{average service time (hours)}}{\text{target door utilisation}}$$

Poor scheduling creates detention charges and long truck turnaround time (TAT).

### Example
Peak of 12 trucks an hour, average 45 minutes (0.75 h) unloading, target utilisation 80%: N = 12 x 0.75 / 0.8 = 9/0.8 = **11.25, so 12 doors**. Cutting service time to 30 minutes gives 12 x 0.5/0.8 = 7.5, so 8 doors.

### In the news
See news box. NCAER's work shows logistics performance is a national competitiveness issue; truck turnaround at docks is a visible lever that firms control.

### Interview angle
> [!question] How it is asked
> "Our DC trucks wait 6 hours at the gate. How do you fix it?"

> [!tip] Strong answer includes
> - Measure first: gate-in to gate-out, queue time, door utilisation
> - Appointment system, door allocation, pre-advice (ASN) and staging
> - Capacity calculation like the one above
> - Cross-dock where flows are predictable, with supplier compliance on labelling

---

## 14. ⭐ Advanced: Automation Business Case (AMR, Goods-to-Person, ASRS)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Automation options range from **conveyors and sorters**, to **AMRs (autonomous mobile robots)** that assist pickers, **goods-to-person (GTP)** stations and **ASRS** (see section 5). The business case compares **capex plus operating cost** against labour, space and accuracy gains:

$$\text{Payback (years)} = \frac{\text{Capex}}{\text{Annual savings}}$$

Evaluate **NPV**, scalability (modular AMRs vs fixed ASRS), peak handling, implementation risk, integration with WMS, uptime guarantee and flexibility to SKU changes. In India, where labour is cheaper than in the US or Europe, payback rests more on throughput, accuracy, space and peak-season labour availability than on headcount alone.

### Example
Illustrative: AMR system capex ₹6 crore. Labour saved: 40 pickers x ₹3,00,000 a year = ₹1.2 crore; accuracy and throughput gains ₹0.4 crore; less annual maintenance ₹0.3 crore. Net savings = 1.2 + 0.4 - 0.3 = ₹1.3 crore. Payback = 6/1.3 = **4.6 years**. If volumes double without adding staff, savings rise and payback shortens; if volumes fall, it lengthens.

### In the news
See news box. Amazon's DeepFleet reportedly raises fleet speed about 10%, a software-only improvement that raises ROI on the same hardware: a reminder to include software upgrade potential in the business case.

### Interview angle
> [!question] How it is asked
> "Should this 3PL invest in warehouse automation?"

> [!tip] Strong answer includes
> - Payback and NPV with explicit assumptions
> - Contract tenure and customer volume visibility (3PL risk)
> - Phased, modular approach before full automation
> - Non-financial benefits: safety, accuracy, ability to win clients, and risks: downtime, vendor lock-in

---
## 🔗 Go deeper: expansion notes
- [[127 Warehouse Engineering - Racking, Sizing & Material Handling|Warehouse Engineering - Racking, Sizing & Material Handling]]
- [[128 Warehouse Labour, WES-WCS & Yard Management|Warehouse Labour, WES-WCS & Yard Management]]
- [[197 SAP EWM Deep Dive - Process-Oriented Warehousing|SAP EWM Deep Dive - Process-Oriented Warehousing]]
