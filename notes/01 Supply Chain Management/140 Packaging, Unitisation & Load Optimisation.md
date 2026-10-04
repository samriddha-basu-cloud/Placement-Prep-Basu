---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Packaging, Unitisation & Load Optimisation"
tier: Tier 2
roles: Operations
status: complete
subtopics: 14
---
# Packaging, Unitisation & Load Optimisation

⬅ [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[141 Supply Chain Disruption Case Library (2011-2026)]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Packaging Levels: Primary, Secondary and Tertiary]]
2. [[#2. Unitisation and the Unit Load Concept]]
3. [[#3. Pallet Types and Standards: EUR, GMA and the India 1200 × 1000]]
4. [[#4. Pallet Patterns and Stacking Limits]]
5. [[#5. Container Loading: 20 ft, 40 ft and 40 ft High Cube]]
6. [[#6. Cubing, Dimensional Weight and Volumetric Weight]]
7. [[#7. Packaging Cost vs Damage: Finding the Economic Level]]
8. [[#8. Packaging Testing: ISTA, Drop, Vibration and Compression]]
9. [[#9. Returnable Packaging and Reusable Transit Items]]
10. [[#10. Sustainable Packaging and EPR in India]]
11. [[#11. 3D Load-Planning Software and Optimisation]]
12. [[#12. Air Cargo ULDs: Unit Load Devices]]
13. [[#13. ⭐ Advanced: E-commerce Packaging, Right-Sizing and Returns]]
14. [[#14. ⭐ Advanced: Load Securing, Weight Distribution and Verified Gross Mass]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): less virgin plastic, more reuse, and higher freight and parcel surcharges
> **Nestlé sets a virgin-plastic path to 2030 (Sept 2026).** Packaging Dive reported Nestlé's plan to cut virgin plastic use by **12-17% by 2030 against a 2018 baseline**. Recycled content was **21% in 2025**; the plan relies on recycled content for roughly half to 60% of the improvement, on reduction and elimination for 30-40% and on alternative materials and reuse for 10-15%; reusable packaging was only **0.51%** of the total in 2025. ([Packaging Dive](https://www.packagingdive.com/news/nestle-plastic-reduction-strategy-2030/831243/))
>
> **Reuse services scale (Sept 2026).** Circular Services (a Closed Loop Partners subsidiary) acquired Re:Dish, a New York reusable-dishware operator that handles collection, washing and tracking and says it has diverted more than **9 million** single-use items; the buyer plans to bundle reuse with its existing recycling services. ([Packaging Dive](https://www.packagingdive.com/news/circular-services-acquires-redish/831012/))
>
> **Surcharges and container rates.** Supply Chain Dive reported (25 Sept 2026) that USPS, FedEx, UPS and Amazon were adding peak-season fees from September to January, which raise the value of shrinking parcel size and weight ([Supply Chain Dive](https://www.supplychaindive.com/news/carrier-diversity-key-to-holiday-success-in-a-high-cost-environment/831027/)). On ocean freight, Drewry's World Container Index stood at **$2,712 per 40ft container on 21 May 2026, up 6% week on week**, with Shanghai-Rotterdam up 15% to $2,773 (the latest snapshot available to this note; check the live index). ([Drewry](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Packaging Levels: Primary, Secondary and Tertiary
> 🟠 Tier 2 · _Key points:_ Product contact, grouping, transport; functions and trade-offs

### Definition
Packaging is organised in levels, each with a different job:

| Level | What it is | Main functions | Examples |
|---|---|---|---|
| **Primary** | In direct contact with the product, the "sales unit" | Protect, contain, preserve (barrier, shelf life), inform, sell | Bottle, sachet, blister, can, pouch |
| **Secondary** | Groups primary packs into a shelf-ready or distribution unit | Group, protect, display, ease handling | Corrugated carton of 12, shrink-wrapped tray, display carton |
| **Tertiary** | Unitises secondary packs for storage and transport | Unit load, stability, handling by forklift, identification | Pallet with stretch wrap, strapping, corner boards, roll cage |

Some texts add **quaternary** packaging (shipping container, ULD). Packaging performs four broad functions: **protection**, **containment/unitisation**, **information** (labels, GS1 barcodes, SSCC pallet labels, batch and expiry) and **convenience/marketing**. Design must balance **product protection** (shelf life, damage), **cost**, **cube efficiency** (see [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]), **machinability** (filling lines) and **sustainability** (EPR). Packaging is typically 5-15% of the cost of goods in FMCG, higher in low-value, high-volume goods; confirm for each category.

### Example
A Pune biscuit maker: primary = 200 g laminate pack; secondary = corrugated case of 24 packs (about 5.5 kg); tertiary = 1200 × 1000 mm pallet with 60 cases (10 per layer, 6 layers) = 1,440 packs and about 330 kg. A change from 24 to 30 packs per case lifts cube efficiency but needs stronger boards and affects shelf-restocking time at the retailer: packaging decisions affect three stakeholders at once.

### In the news
See news box. Nestlé's reduce-recycle-reuse plan targets primary packaging materials; the freight surcharges bite at the secondary and tertiary level through cube and weight.

### Interview angle
> [!question] How it is asked
> "Explain primary, secondary and tertiary packaging and how supply chain decisions affect each."

> [!tip] Strong answer includes
> - Level definitions with an example each, and the functions of packaging
> - How each level interacts with logistics: cube, pallet pattern, damage, labelling
> - Trade-offs: protection vs cost vs sustainability vs line speed
> - Who bears the cost and who gets the benefit (often different functions)

---
## 2. Unitisation and the Unit Load Concept
> 🟠 Tier 2 · _Key points:_ Combining items into one handled unit; pallets, roll cages, slip sheets, containers, ULDs

### Definition
**Unitisation** combines multiple items or cartons into a single **unit load** that is handled, stored and moved as one, so that handling cost per item falls, throughput rises and damage and pilferage drop. Unit-load formats: **pallets** (wood, plastic, metal, paper), **slip sheets**, **roll cages and trolleys** (retail, parcels), **bulk containers/IBCs** (liquids), **drums**, **intermodal containers** and **air ULDs**. A good unit load is **stable** (will not collapse or tilt), **compatible** with equipment (forklift entry, racking beam spans, vehicle floor), **identifiable** (SSCC label, barcodes), and **efficient** (cube and weight utilisation). Principle: **move as few handling units as possible for as long as possible**, and keep the same unit from factory to store, a major driver of labour productivity in warehouses ([[010 Warehouse Management]], [[127 Warehouse Engineering - Racking, Sizing & Material Handling]], [[009 Logistics & Distribution]]).

Stabilisation: stretch wrap (pre-stretch, containment force), strapping, corner boards, adhesive between layers, shrink hoods; protection against moisture and dust.

### Example
Loading 1,440 cartons manually into a truck at 2 cartons a minute takes 12 hours of labour; a single forklift loads 24 pallets of 60 cartons in about 40 minutes (about 100 seconds per pallet). Labour per carton falls roughly 18×; with pallets also stored in racking, put-away and picking productivity improve and carton damage drops because cartons are no longer touched individually.

### In the news
See news box. Reuse services (washing, tracking, returns) depend on unitised, trackable, returnable formats, extending the unit load concept to reverse flows.

### Interview angle
> [!question] How it is asked
> "Why do companies unitise loads and what can go wrong?"

> [!tip] Strong answer includes
> - Productivity (handling), protection, security and traceability benefits
> - Dependence on standardised pallet sizes and compatible racking and vehicles
> - Failure modes: unstable pallets, overhang, poor wrap, over-stacking, mixed SKUs
> - Link to cost: unitised flow reduces touches, the main driver of handling cost

---
## 3. Pallet Types and Standards: EUR, GMA and the India 1200 × 1000
> 🟠 Tier 2 · _Key points:_ 1200×800, 48×40 in, 1200×1000, wood vs plastic, ISPM 15, pooling

### Definition
Standard pallet footprints (ISO 6780 lists six sizes ranging from 800 × 1,200 mm to 1,165 × 1,165 mm):

| Pallet | Size | Where used |
|---|---|---|
| **EUR / EPAL (EUR 1)** | 1,200 × 800 mm | Europe; four-way entry; pooled and exchanged |
| **GMA** | 48 × 40 in (1,219 × 1,016 mm) | North America (a large share of new wood pallets in the US) |
| **ISO 1200 × 1000** | 1,200 × 1,000 mm | Widely used in India and in Asia and international trade; often the default for Indian FMCG, pharma and industrial plants (check customer-specific standards) |
| Others | 1,100 × 1,100, 1,140 × 1,140, 1,165 × 1,165 mm | Asia-Pacific (Australia's square pallet) |

Materials: **wood** (most common, cheap, repairable; stringer or block construction; block pallets give four-way entry), **plastic** (HDPE or recycled; durable, hygienic, no ISPM 15 treatment, but costlier), **metal** (heavy loads) and **paper/pressed wood** (light, one-way export). **ISPM 15** requires heat treatment (HT) or methyl bromide fumigation (MB) marking for wooden packaging in international trade. Specifications to look at: static, dynamic and racking load ratings, entry type (two-way vs four-way), deck board gaps, hygiene (food and pharma prefer plastic) and fork pocket height.

Pallet ownership: **one-way** (expendable, export), **owned/returnable** and **pooled/rental** (CHEP, LPR in Europe and other pool providers). Pooling reduces capital and transfers but needs pallet-exchange discipline.

### Example
Same carton volume shipped on 1200 × 800 EUR pallets versus 1200 × 1000: with a 400 × 300 mm carton the **EUR pallet takes 8 cartons per layer (0.96 m² fully tiled)** and the **1200 × 1000 pallet takes 10 per layer (1.2 m², also fully tiled)**. A plant standardising on 1200 × 1000 but supplying a European retailer on EUR pallets must re-palletise at the port or at an exchange hub, adding a touch and ₹ cost per pallet; for an Indian exporter, pallet size should be negotiated with the buyer before packaging design.

### In the news
See news box. Plastic pallets and reuse systems tie into sustainability goals and EPR conversations; wood needs ISPM 15 compliance for export.

### Interview angle
> [!question] How it is asked
> "Which pallet size would you standardise on in India and what happens when you export?"

> [!tip] Strong answer includes
> - Know the standard sizes (EUR 1200 × 800, GMA 48 × 40 in, ISO 1200 × 1000)
> - Fit-to-product and fit-to-container logic; customer and port standards
> - Material trade-offs (wood vs plastic vs pooled), ISPM 15 for export
> - Cost and handling: re-palletising, exchange systems, damage and loss

---
## 4. Pallet Patterns and Stacking Limits
> 🟠 Tier 2 · _Key points:_ Column vs interlocked vs pinwheel, area utilisation, box compression strength, stack height

### Definition
**Pallet pattern**: arrangement of cartons in each layer. **Column stacking** (cartons directly above each other) uses the full compression strength of corrugated boxes but gives poor load stability; **interlocking (brick or pinwheel) patterns** improve stability but typically cut box strength by about 30-40% (rule-of-thumb figures from packaging engineering guidance). Goals: **area utilisation** (layer area covered ÷ pallet area), **no or minimal overhang** (overhang can reduce compression strength sharply and invites damage), uniform layers and stability.

Stacking limit from **box compression test (BCT)**: the allowable stacking load on the bottom box is $BCT / SF$, where $SF$ is a safety factor (higher with humid conditions, long storage, rough handling, interlocked patterns; typical guidance ranges from about 3 to 6). Number of cartons that can sit above the bottom one = allowable load ÷ carton weight. Also consider racking beam capacity, forklift mast height, vehicle height and the pallet's own load rating.

### Example
Carton 400 × 300 × 250 mm, weight 6 kg. Pallet 1200 × 1000 mm.

- **Layer pattern:** split the pallet into a 1200 × 400 strip (4 cartons, 300 mm side along the length) and a 1200 × 600 area (2 rows of 3 cartons with 400 mm along the length) = **10 per layer**, utilisation 1,200/1,200 = **100%**, no overhang.
- **BCT 120 kg-force**, safety factor 4: allowable load on the bottom carton = **30 kg**, i.e. 5 cartons above it, so **6 layers** = 60 cartons per pallet.
- Upgrade to a stronger board (BCT 170 kg-force): allowable 42.5 kg = 7 cartons above, so 8 layers; the 8-layer limit equals the vehicle height limit (240 cm container: 8 × 25 cm = 200 cm plus a 15 cm pallet = 215 cm). Pallet loads 80 cartons (480 kg) instead of 60: **+33% cartons per pallet**, which cuts pallet-handling and transport cost per carton by 25%, against a board cost rise that must stay below those savings.

### In the news
See news box. Lighter, thinner boards meet sustainability goals but reduce BCT, so lighter packaging often means fewer layers unless the design is tested (see the ISTA sub-topic below).

### Interview angle
> [!question] How it is asked
> "How would you decide how many cartons to stack on a pallet and what limits you?"

> [!tip] Strong answer includes
> - Layer pattern for area utilisation and stability (column vs interlock trade-off)
> - Stack limit from BCT with a safety factor, plus vehicle, racking and forklift limits
> - Overhang, humidity and storage time as strength reducers
> - Value of testing and of pattern software over trial and error

---
## 5. Container Loading: 20 ft, 40 ft and 40 ft High Cube
> 🟠 Tier 2 · _Key points:_ Capacity, payload, floor pallets, cube-out vs weigh-out, utilisation

### Definition
ISO containers (typical values; check the carrier's specification for the actual unit):

| Container | Internal volume | Typical max payload | Tare |
|---|---|---|---|
| **20 ft** | about 33.1 m³ | about 28,280 kg | about 2,200 kg |
| **40 ft** | about 67.5 m³ | about 26,680 kg | about 3,800 kg |
| **40 ft High Cube** | about 75.3 m³ | about 26,545 kg | about 3,935 kg |

Internal dimensions are approximately 5.90 × 2.35 × 2.39 m (20 ft), 12.03 × 2.35 × 2.39 m (40 ft) and 12.03 × 2.35 × 2.69 m (40 ft HC). Floor positions for pallets: EUR pallets, **11 (20 ft) and 25 (40 ft)**; 1200 × 1000 pallets roughly **9-10 in a 20 ft and 20-22 in a 40 ft** depending on pattern and tolerance (planners use the conservative figure); **pallet-wide containers** take more EUR pallets (15 in a 20 ft, 30 in a 40 ft). Also: reefers (temperature controlled), open-top, flat-rack and tank containers.

**Cube-out vs weigh-out:** the container is full by volume (cube-out) for light cargo and by weight (weigh-out) for dense cargo. The **break-even density** is payload ÷ volume: about **395 kg/m³ for a 40 ft** and **854 kg/m³ for a 20 ft**. Utilisation = loaded volume ÷ internal volume and loaded weight ÷ payload. Legal and road limits (weight on Indian roads, axle loads) can bind before the container's payload ([[125 Transportation Management Deep Dive]], [[126 International Trade Documentation, Customs & Trade Finance]]).

### Example
40 ft container, 20 pallets of 1200 × 1000; carton 400 × 300 × 250 mm (0.03 m³), 10 per layer, 8 layers = 80 cartons per pallet; pallet tare 25 kg.

- **Light product (6 kg per carton):** 1,600 cartons = 48 m³ and 10,100 kg. Cube utilisation = 48/67.5 = **71%**; weight use 10,100/26,680 = 38%: **cube-limited**.
- **Dense product (18 kg per carton):** weight limit = (26,680 − 500)/18 = **1,454 cartons** (91% of the 1,600 that would fit by space): **weight-limited**, and cube use only 43.6/67.5 = **65%**.
- If stacking is limited to 6 layers (BCT problem above), 20 pallets × 60 = 1,200 cartons = 36 m³ = **53%** cube utilisation. Moving to 8 layers adds 400 cartons per container (+33%), about 25% less sea freight per carton at the same box rate.

### In the news
See news box. With a 40 ft rate at $2,712 (21 May 2026) a one-point change in cube utilisation is worth about $27 per container; at 71% versus 53% utilisation, freight per carton differs by roughly one-third.

### Interview angle
> [!question] How it is asked
> "Calculate how many cartons fit in a 40 ft container and tell me whether volume or weight is binding."

> [!tip] Strong answer includes
> - Container volume and payload; pallet positions; layers from internal height
> - Compute both volume-based and weight-based limits; the lower governs
> - Break-even density (about 395 kg/m³ for a 40 ft)
> - Practical losses: dunnage, door clearance, mixed pallets, tolerances

---
## 6. Cubing, Dimensional Weight and Volumetric Weight
> 🟠 Tier 2 · _Key points:_ Cube (L×W×H), chargeable weight = max(actual, volumetric), divisors 5,000 and 6,000

### Definition
**Cubing** is measuring and recording length, width, height and weight of each SKU and case (often with automatic dimensioners, for example in-line cubing and weighing systems); accurate item master data feeds slotting, pallet and container planning, carrier invoicing and WMS rules ([[175 Data Quality, Master Data & Data Governance]], [[010 Warehouse Management]]).

**Dimensional (volumetric) weight** prices space on a carrier's vehicle or aircraft:

$$\text{Volumetric weight (kg)} = \frac{L \times W \times H \text{ (cm)}}{\text{divisor}}$$

$$\text{Chargeable weight} = \max(\text{actual weight},\ \text{volumetric weight})$$

Common divisors: **6,000 cm³ per kg for IATA air cargo** (one cubic metre = 166.7 kg) and **5,000 cm³ per kg for many express and courier services**; in inches, 139 or 166 in³ per lb depending on service. Carriers publish their own divisor and rounding, and Indian surface and rail carriers and e-commerce logistics providers use their own factors, so always read the rate card. Ocean LCL uses a **weight-or-measurement** rule (1 m³ is treated as 1,000 kg; the greater is charged, or "W/M"). The **density** of the shipment decides whether it is charged on weight or volume.

### Example
Carton 60 × 40 × 30 cm, actual weight 8 kg.

- Volume = 72,000 cm³. IATA volumetric weight = 72,000/6,000 = **12 kg**; courier at 5,000 gives **14.4 kg**.
- Chargeable weight = **12 kg** (air), 50% above the actual 8 kg.
- Redesign to 50 × 35 × 25 cm = 43,750 cm³: volumetric = 7.29 kg, so chargeable = actual **8 kg** (a third less).
- At an illustrative ₹120 per chargeable kg, saving = 4 kg × ₹120 = ₹480 per carton; for 5,000 cartons = **₹24 lakh**. Break-even density for air at 6,000: 166.7 kg/m³.

### In the news
See news box. Peak-season fees and parcel surcharges stack on top of dimensional weight, increasing the value of right-sized boxes.

### Interview angle
> [!question] How it is asked
> "Why is the freight bill for our light but bulky product so high and what can we do?"

> [!tip] Strong answer includes
> - Dimensional weight: chargeable = max(actual, volumetric), divisor 5,000 or 6,000
> - Reduce volume: right-size cartons, remove void, compress or flat-pack, nest
> - Negotiate divisor and rounding in carrier contracts; consolidate shipments
> - Maintain SKU cubing data so billing can be audited

---
## 7. Packaging Cost vs Damage: Finding the Economic Level
> 🟠 Tier 2 · _Key points:_ Total cost = packaging + expected damage cost; over- and under-packaging

### Definition
Packaging should minimise **total landed cost**, not packaging cost:

$$\text{Cost per unit shipped} = \text{Packaging cost} + P(\text{damage}) \times \text{Cost per damaged unit}$$

Cost per damaged unit includes the product value (or write-down), reverse freight, handling, replacement shipment, customer-service cost, and the **lost-customer** effect. **Under-packaging** shows in damage, claims and returns; **over-packaging** shows in material cost, cube and weight, waste and EPR fees. The optimum is found by testing alternatives (see ISTA below) and measuring damage rates in the field ([[110 Cost Accounting for Operations]], [[138 Order Management, Customer Service & Cost-to-Serve]]). Product-side measures to reduce damage: fragility analysis (the G-level the product can survive), cushioning curves, and design changes (see [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]).

### Example
Product value ₹1,200; each damaged unit costs ₹1,200 (write-off) + ₹250 (handling, return freight, support) = **₹1,450**.

| Option | Packaging cost | Damage rate | Expected damage cost | Total per unit |
|---|---|---|---|---|
| A: basic carton | ₹18 | 3.0% | ₹43.5 | **₹61.5** |
| B: moulded-pulp insert | ₹26 | 0.8% | ₹11.6 | **₹37.6** |
| C: foam-in-place, double wall | ₹35 | 0.5% | ₹7.3 | **₹42.3** |

Option B is the cheapest in total. B versus A saves ₹23.9 per unit, or **₹2.39 crore on 10 lakh units a year**, even though packaging cost is 44% higher. C protects better but costs more than it saves. If the cost of a damaged unit includes customer churn (for example ₹2,000), the optimum may shift toward C.

### In the news
See news box. As sustainability goals push for lighter and mono-material packs, damage rates must be measured so that material cuts do not backfire on returns.

### Interview angle
> [!question] How it is asked
> "The packaging team wants a cheaper carton; the customer-service team reports more damage. How do you decide?"

> [!tip] Strong answer includes
> - Total-cost formula (packaging plus expected damage cost)
> - Data: damage rate by lane and carrier, claims and returns, cost per damage
> - Test alternatives (lab and field), then pilot
> - Include sustainability and cube effects, not just unit material cost

---
## 8. Packaging Testing: ISTA, Drop, Vibration and Compression
> 🟠 Tier 2 · _Key points:_ Transit simulation, ISTA 1/2/3/6/7 series, ASTM D4169, field validation

### Definition
Packaging is validated by **laboratory simulation of the distribution environment**: shock (drop, incline-impact), vibration (random, sine; simulating truck and air), compression (static or dynamic stacking), climatic and thermal tests, and special tests (pressure change, water exposure). **ISTA** (International Safe Transit Association) publishes standard test procedures grouped in series:

- **Series 1**: non-simulation integrity tests (basic drop and vibration)
- **Series 2**: partial simulation
- **Series 3**: general simulation of the distribution environment, such as **3A** for individual packaged products shipped by parcel delivery systems (packages up to about 70 kg or 150 lb) and **3E** for unitised loads of similar packaged products
- **Series 6**: member-specific or retailer-specific protocols (for example ISTA 6-Amazon.com tests for e-commerce shipping)
- **Series 7**: thermal-controlled and temperature-sensitive shipments

Other standards: **ASTM D4169** (performance testing of shipping containers), ISO 4180, ASTM D642 and TAPPI methods for compression and BCT. Process: define the distribution environment, pick the protocol, test the package with the product (or a dummy of equal mass), assess damage, redesign, then **validate in the field with tracked shipments**. Test results are a screening tool, not a guarantee: the real chain has variability (carrier, route, climate).

### Example
An e-commerce seller ships a ₹4,500 appliance. Current packaging fails the ISTA 3A drop sequence (a corner crush on a drop onto a corner). A redesign adds corner cushions (₹6 more per unit) and passes. Field data: damage rate in the previous 6 months = 2.4% on 80,000 shipments = 1,920 claims at ₹4,900 (value plus handling) = **₹94 lakh**; after redesign 0.7% = 560 claims = **₹27.4 lakh**; saving ₹66.6 lakh against added packaging cost of ₹6 × 80,000 = ₹4.8 lakh.

### In the news
See news box. Retailer and marketplace packaging rules (such as parcel testing programmes) and lighter-weight targets increase the amount of testing needed before packaging changes go live.

### Interview angle
> [!question] How it is asked
> "How do you prove a new, lighter package will survive distribution?"

> [!tip] Strong answer includes
> - Define the distribution environment and select ISTA/ASTM protocols
> - Lab testing followed by field trials with damage tracking
> - Fragility of the product (G-level) and cushioning design
> - Decision rule: pass criteria plus cost per damage vs saving from material cuts

---
## 9. Returnable Packaging and Reusable Transit Items
> 🟠 Tier 2 · _Key points:_ RTI economics, break-even trips, loss rate, pooling, reverse logistics

### Definition
**Returnable transport packaging (RTI)**: plastic crates and totes, roll cages, pallets, collapsible bulk bins, kegs, racks and dunnage that circulate between supplier and customer many times. Used in auto components (JIT, [[131 Automotive Supply Chain - JIT, Tiers & EVs]]), retail fresh food, dairy and beverages, e-commerce totes and pooled pallets. Benefits: lower cost per trip, less waste, better protection, ergonomics, standard sizes, fewer EPR obligations. Costs and risks: capital, **empty return freight**, washing and repair, tracking and loss, pool management, and the need for agreed ownership, deposit or rental mechanisms ([[135 Reverse Logistics, Remanufacturing & EPR in India]], [[014 Global SCM & Sustainability]]).

**Break-even number of trips**: per-trip cost of RTI $= \frac{\text{Purchase price}}{N} + \text{washing} + \text{empty return} + \text{pool management}$ compared with the per-trip cost of expendable packaging. Loss and damage rates reduce the effective $N$.

### Example
Expendable corrugated pack: ₹180 per trip. RTI crate: ₹2,400 purchase, washing ₹30, empty return freight ₹45, tracking and pool management ₹10 per trip (₹85 in total per trip excluding capital).

- Per-trip cost at life $N$: 2,400/$N$ + 85.
- Break-even: 2,400/$N$ + 85 = 180, so $N = 2{,}400/95 =$ **25.3 trips**.
- If the crate really completes 40 trips: ₹60 + ₹85 = ₹145 per trip, saving ₹35 (19%); at 1.2 lakh trips a year = **₹42 lakh**.
- If losses cut life to 20 trips: ₹120 + ₹85 = ₹205, ₹25 worse than expendable. Control of loss (tracking, deposits, pool agreements) decides success.

### In the news
See news box. Re:Dish's model (collection, washing and tracking as a service) and Nestlé's reuse share of only 0.51% show how far reuse still has to scale and where the operational challenge lies.

### Interview angle
> [!question] How it is asked
> "Should we replace cardboard cartons with returnable crates for our dealer network?"

> [!tip] Strong answer includes
> - Break-even trips formula with loss rate and reverse logistics costs
> - Closed-loop vs open-loop vs pooled models, and who owns the asset
> - Operational readiness: tracking, washing, repair, return flow, standard sizes
> - Sustainability and EPR benefits, but financial case must hold first

---
## 10. Sustainable Packaging and EPR in India
> 🟠 Tier 2 · _Key points:_ Reduce, redesign, recycle, reuse; EPR obligations for PIBOs; right-sizing; mono-material

### Definition
Sustainable packaging principles: **reduce** material (lightweighting, right-sizing, fewer layers), **redesign** for recyclability (mono-material, easily separable components, avoidance of problem materials), **use recycled content**, **reuse** (RTI, refill) and **responsibly source** (certified paper). Business logic: material cost, freight cost (weight and cube), regulation and retailer demands, brand.

India's regulatory frame is **Extended Producer Responsibility (EPR)**: under the **Plastic Waste Management Rules, 2016 and later amendments (including the 2022 EPR guidelines)**, producers, importers and brand owners (PIBOs) must register on the CPCB EPR portal and meet targets for collection, recycling and recycled-content use for plastic packaging across categories (rigid, flexible, multi-layered, compostable); single-use plastic items were banned from 1 July 2022. Separate EPR regimes exist for **e-waste** and **batteries** ([[135 Reverse Logistics, Remanufacturing & EPR in India]], [[014 Global SCM & Sustainability]]). Targets, categories and fee structures change; **check the current CPCB and MoEFCC notifications** before quoting numbers. Packaging engineers and supply chain teams must also address: tracking of packaging weight by category (EPR data), supplier declarations, recycler contracts and certificates, and avoid "greenwash" claims.

### Example
A beverage firm sells 20 crore bottles a year with a 24 g PET bottle. Redesign cuts weight to 21 g (−12.5%): PET saved = 3 g × 20 crore = 600 tonnes. At ₹110 per kg PET (illustrative) = **₹6.6 crore** a year material saving; a lighter bottle also lowers freight weight (but because beverages are heavy, the effect is small) and lowers EPR obligation quantities. Check top-load strength (stacking!) and filling-line speed before approving; fewer grams can mean more damage unless the bottle is tested.

### In the news
See news box. Nestlé's virgin-plastic path (recycled content, reduction, reuse) is a typical corporate structure for EPR-era packaging strategy.

### Interview angle
> [!question] How it is asked
> "How would EPR rules change your packaging and supply chain strategy?"

> [!tip] Strong answer includes
> - Register, measure and report packaging weights by category; meet collection and recycling targets via PROs or recyclers
> - Redesign levers: lightweighting, mono-material, recycled content, reuse systems
> - Cost trade-offs: EPR fees vs redesign capex vs freight savings
> - Check current rules since targets change; caution about greenwashing

---
## 11. 3D Load-Planning Software and Optimisation
> 🟠 Tier 2 · _Key points:_ 3D bin packing, constraints, heuristics, load plans and sequence, axle loads

### Definition
The **container loading problem** is a **three-dimensional bin-packing** problem (NP-hard): choose where to place each box so that volume is used well subject to constraints. Real constraints: weight and axle-load limits and centre of gravity, **stacking and fragility** (what can go on top of what), orientation ("this side up"), **loading and unloading sequence (LIFO)** for multi-drop routes, unit load integrity, compatibility (food vs chemicals), door and floor load limits, and securing. Methods: constructive heuristics (layer building, wall building, extreme-point and guillotine approaches), local search and metaheuristics, and mixed-integer models for small cases. Commercial tools (cargo and container loading planners, WMS/TMS modules, pallet-building software, tools in packaging design suites) take SKU cube data, orders and vehicle types, and output a **visual 3D loading plan**, utilisation, weights, and step-by-step loading instructions.

Benefits: higher utilisation (often several percentage points of cube), fewer trips or containers, fewer damages (stable loads), faster loading with clear instructions, and better quotation and capacity planning. Prerequisites: reliable cubing and weight data, discipline in following the plan, and realistic "packing efficiency" parameters. Integration: TMS ([[125 Transportation Management Deep Dive]]), WMS/EWM ([[197 SAP EWM Deep Dive - Process-Oriented Warehousing]]), SAP load building ([[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]]). The pallet-building variant ("mixed-case palletising") is solved with similar algorithms and underlies robotic palletisers ([[068 Operations-Specific Python (PuLP, SimPy)]] for optimisation tooling).

### Example
An exporter ships 14 container loads a month at 66% average cube utilisation and ₹2.8 lakh per 40 ft. Load-planning software and better palletisation raise utilisation to 74% on the same cargo (+8 points), which means 66/74 = 89.2% of the containers are needed: 14 × 0.892 = 12.5 containers.

- Saving ≈ 1.5 containers a month × ₹2.8 lakh = **₹4.2 lakh a month ≈ ₹50 lakh a year**, less software cost and any extra loading time.
- Weight limits: if a mixed load reaches the payload limit first (weight-limited), the plan should instead mix dense and light SKUs (density balancing) to use both limits.

### In the news
See news box. At higher container and surcharge levels, each percentage point of utilisation is worth more, which strengthens the business case for load planning.

### Interview angle
> [!question] How it is asked
> "How would you increase container utilisation without changing the product or the carrier?"

> [!tip] Strong answer includes
> - Fix the data: accurate cube and weight, packaging dimensions and stacking limits
> - Optimise pallets first, then container plan; consider mixing dense and light SKUs
> - Use load-planning software with real constraints (sequence, axle load, fragility)
> - Measure utilisation (cube and weight), track variance between plan and actual loads

---
## 12. Air Cargo ULDs: Unit Load Devices
> 🟠 Tier 2 · _Key points:_ AKE (LD3), PMC pallets, contours, volume, build-up, chargeable weight

### Definition
**Unit load devices (ULDs)** are the pallets and containers used to load air cargo and baggage into aircraft holds. They have shapes that fit aircraft contours, so the usable volume and weight differ by aircraft type and hold position. Common types:

- **AKE (LD3)**: half-width contoured container, about 4.5 m³ internal volume; used on widebody aircraft from Airbus and Boeing (confirm the compatible aircraft list for the exact type).
- **PMC (LD7-type pallet)**: 2,438 × 3,175 mm (96 × 125 in) pallet, around 14 m³ when built up with a net; requires larger doors.
- **AAP (LD9)**: full-width container, around 10.8 m³.
- **Temperature-controlled ULDs** (insulated, active) for pharma and perishables ([[132 Pharma & Healthcare Supply Chain]]).

Materials are aluminium frames with polycarbonate panels, with certified structural strength. Capacity is measured in **positions** and by **maximum gross weight** (indicative figures: about 1,588 kg for an AKE and about 6,800 kg for a PMC; confirm for the exact ULD and aircraft). **Build-up** (loading cargo onto pallets or into containers at the forwarder or airline cargo terminal) follows rules on weight distribution, height contour and securing nets and straps. The airline charges on **chargeable weight** (actual vs volumetric at 6,000 cm³ per kg) ([[009 Logistics & Distribution]]). **ULD handling** issues: damage, ULD shortages, repositioning of empties, and tracking.

### Example
An AKE (4.5 m³).

- Volumetric (chargeable) equivalent = 4.5 m³ × 166.7 kg/m³ = **750 kg**.
- Light cargo at 120 kg/m³ fills the container at 540 kg actual: **chargeable 750 kg**, so the shipper pays for 210 kg of air.
- Dense cargo at 250 kg/m³ would give 1,125 kg actual in the same 4.5 m³, so **actual weight governs**; check that the ULD's maximum gross weight (about 1,588 kg including tare) is not exceeded.
- Break-even density = 166.7 kg/m³. At 120 kg/m³ the shipper pays for 39% more weight than it ships (166.7/120 = 1.39); at 160 kg/m³ the premium is only 4%, which is why compressing or consolidating light cargo cuts cost per actual kg.

### In the news
See news box. Parcel dimensional-weight surcharges and container rate changes show the same density economics that govern air cargo ULD pricing.

### Interview angle
> [!question] How it is asked
> "What is a ULD and how does density affect air-freight cost?"

> [!tip] Strong answer includes
> - ULD types (AKE/LD3, PMC) with volumes and why contour matters
> - Chargeable weight with the 6,000 divisor and the 166.7 kg/m³ break-even
> - Packaging and consolidation levers (compress, right-size, bundle)
> - Operational points: build-up rules, ULD tracking, special handling cargo

---
## 13. ⭐ Advanced: E-commerce Packaging, Right-Sizing and Returns
> ⭐ Advanced · _Added beyond the tracker_

### Definition
E-commerce parcels are packed at item level and travel through parcel networks with many touches, so packaging must resist drops and compression while avoiding excess size. Key levers: **right-sizing** (a range of box sizes, or on-demand box-making machines), **ships-in-own-container (SIOC)** designs that need no overbox, **void-fill reduction** (inflated air, paper), poly-mailers for soft goods, **dimensional-weight reduction**, and **returns-friendly** design (reusable mailers, easy-reseal tapes). Trade-offs: protection vs size; automation capex vs material saving; customer experience; sustainability messaging. Link to [[129 E-commerce & Quick-Commerce Fulfilment]] for pick-pack-ship flow and [[135 Reverse Logistics, Remanufacturing & EPR in India]] for returns. Data inputs: cubing of SKUs, order combinations, box-selection algorithms and carrier divisors.

### Example
A seller ships 10 lakh parcels a year in a ₹14 corrugated box of 40 × 30 × 20 cm (24,000 cm³; volumetric at 5,000 = 4.8 kg) with 1.5 kg actual weight. A three-size box set cuts average volume to 12,000 cm³ (2.4 kg volumetric, still above actual 1.5 kg).

- Chargeable weight falls from 4.8 to 2.4 kg per parcel. At an illustrative ₹16 per kg of chargeable weight above the first slab, saving ≈ 2.4 × ₹16 = **₹38 per parcel**, or ₹3.8 crore a year on 10 lakh parcels.
- Right-sized boxes cost ₹11 on average (−₹3) from less board: another ₹30 lakh.
- Cost: sizing machine or extra SKUs of boxes and slightly more complex packing station time (assume ₹2 per parcel = ₹20 lakh). Net ≈ **₹3.9 crore a year**.

### In the news
See news box. Peak-season surcharges increase the value of every kilo of volumetric weight removed.

### Interview angle
> [!question] How it is asked
> "How would you cut the shipping cost of an e-commerce business without changing carriers?"

> [!tip] Strong answer includes
> - Dimensional-weight analysis by SKU and order; box-size optimisation
> - Packaging redesign (SIOC, poly mailers, void-fill reduction) with ISTA 6-type testing
> - Returns packaging and reuse, and sustainability angle
> - Quantified savings net of automation and labour cost

---
## 14. ⭐ Advanced: Load Securing, Weight Distribution and Verified Gross Mass
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A load that shifts or collapses endangers people and cargo. Principles of load securing: **block** (against bulkheads, dunnage, void fillers), **lash** (straps, chains, nets), **friction** (anti-slip mats) and **top-over lashing**; keep the **centre of gravity low and central**, distribute weight evenly (heavy at the bottom, close to the axle area, not all at the door or the nose), avoid concentrated floor loads, and respect axle-load limits for trucks (axle load norms in India were revised upwards by the transport ministry in 2018, so check current figures). In containers, voids are filled with dunnage or air bags and desiccants are used where condensation is a risk. International references: the IMO/ILO/UNECE **CTU Code** (Code of Practice for Packing of Cargo Transport Units) and **EN 12195** (load restraint on road vehicles).

**VGM (verified gross mass):** under the SOLAS amendment effective **1 July 2016**, the shipper must provide a verified gross mass for every packed export container before it can be loaded on a ship, either by weighing the packed container or by weighing contents plus tare. Wrong or missing VGM leads to refused loading and fines, and misdeclared weights cause stack collapses and accidents ([[126 International Trade Documentation, Customs & Trade Finance]]).

### Example
A 20 ft container, tare 2,200 kg: contents 18,400 kg cargo + 300 kg pallets + 120 kg dunnage = 18,820 kg. **VGM = 18,820 + 2,200 = 21,020 kg**, well inside the 30,480 kg maximum gross mass on a typical 20 ft (confirm on the CSC plate). If the cargo were declared as 16,000 kg, the VGM would be understated by 2,820 kg (13%) and the load could be refused or fined at the port and could distort ship stability calculations.

Weight distribution check: if 80% of the 18,820 kg is loaded in the front half of the container (15,056 kg) the rear half carries only 3,764 kg; standard guidance limits imbalance (for example, no more than about 60% of weight in one half). Re-plan by interleaving heavy and light pallets.

### In the news
See news box. High freight rates and tight schedules raise the cost of a rolled or rejected container, so verified weights and secure loading matter more.

### Interview angle
> [!question] How it is asked
> "What is VGM and what are the main rules of good container stuffing?"

> [!tip] Strong answer includes
> - VGM requirement (SOLAS, since 1 July 2016) and the two methods
> - Weight distribution, centre of gravity, blocking and bracing, dunnage
> - Axle and payload limits and the consequence of misdeclaration
> - Documentation and responsibilities of shipper, packer and forwarder
