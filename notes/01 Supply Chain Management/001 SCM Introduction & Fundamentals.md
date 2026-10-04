---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "SCM Introduction & Fundamentals"
tier: Tier 1
roles: Operations / Consulting
status: sample
subtopics: 12
---
# SCM Introduction & Fundamentals

[[_Index - Supply Chain Management|Supply Chain Management]] · [[002 Procurement & Strategic Sourcing]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Supply Chain vs Logistics]]
2. [[#2. Supply Chain Drivers]]
3. [[#3. Push vs Pull Systems]]
4. [[#4. Bullwhip Effect]]
5. [[#5. Value Chain Analysis]]
6. [[#6. Supply Chain Network Design]]
7. [[#7. Supply Chain Performance Metrics]]
8. [[#8. Supply Chain Integration]]
9. [[#9. Supply Chain Strategy]]
10. [[#10. Omnichannel SCM]]
11. [[#11. Trade-offs in SCM]]
12. [[#12. Supply Chain Collaboration]]

## 📰 News box
> [!news] Shared news hook for this whole topic: three recent shocks that tested supply chains (2023–2025)
> **Red Sea / Suez rerouting (from late 2023, hitting hardest through 2024).** Carriers diverted ships around the Cape of Good Hope. Maersk reports the longer route added about **9% to average cargo travel distance**, Suez crossings fell by about **66%** (the canal normally carries ~12% of global trade), and effective container capacity was estimated **15–20% lower in Q2 2024** because ships were tied up on longer voyages. ([Maersk](https://www.maersk.com/insights/resilience/2024/07/09/effects-of-red-sea-shipping))
>
> **Tariffs and the China+1 shift (2025).** Apple assembled ~**23.9 million iPhones in India in H1 2025** (+53% YoY); India's share of US smartphone imports rose to **44% in Q2 2025 from 13%**, while China's fell to 25% from 61%. India's FY2025 iPhone exports were reported at **$17.4 bn** (+76%). ([SCW Mag](https://scw-mag.com/news/apples-supply-shift-to-india-speeds-up-to-44-surpassing-china-for-the-first-time/))
>
> **Nexperia chip crisis (Oct 2025).** After the Dutch government seized control of chipmaker Nexperia from its Chinese parent Wingtech (early Oct 2025), Nexperia suspended wafer supply to its Dongguan plant on 29 Oct; by 31 Oct suppliers such as ZF were cutting shifts and Nissan said its chip stock lasted only "until the first week of November". A cheap, single-sourced component halted car lines. ([Tom's Hardware](https://www.tomshardware.com/tech-industry/nexperia-conflict-spills-overseas-as-it-halts-exports-to-china-german-automotive-manufacturers-slow-production-due-to-semiconductor-shortages-from-dutch-chipmaker))
>
> Sub-topics below that say **"See news box"** reuse these items; their *Interview angle* still tells you how to apply them.

---

## 1. Supply Chain vs Logistics
> 🔴 Tier 1 · _Tracker hint:_ Scope difference, flows (material/info/finance), SC objectives

### Definition
A **supply chain** is the network of organisations, activities, information and resources that moves a product from raw material to the end customer *and back* (returns). It manages **three flows**: material (forward), information (both ways) and finance (backward, as payments).

**Logistics** is the *subset* that plans, implements and controls the efficient forward and reverse movement and storage of goods, services and information between origin and consumption (CSCMP's wording). It covers transport, warehousing, inventory handling, packaging and order fulfilment.

| | Supply Chain Management | Logistics |
|---|---|---|
| Scope | End to end, across firms | Mostly within / between a firm's nodes |
| Focus | Value creation, relationships, strategy | Movement and storage efficiency |
| Includes | Sourcing, make, deliver, return, planning, partners | Transport, warehousing, inventory, packaging |
| Typical KPI | Cash-to-cash cycle, perfect order rate | Cost per tonne-km, on-time delivery |

Objective: maximise **supply chain surplus** = customer value − supply chain cost, not minimise any single cost.

### Example
Tata Steel sourcing coking coal from Australia is *logistics* when you ask "which ship, which port, how many days at the yard?" It is *supply chain management* when you ask "should we contract a second supplier in Mozambique, invest in a rail siding, and share demand forecasts with auto customers to level production?"

### In the news
See news box. Red Sea rerouting is a *logistics* problem (route, transit time) that became a *supply chain* problem (safety stock, supplier choice, contract terms).

### Interview angle
> [!question] How it is asked
> "What is the difference between supply chain and logistics?" or "Is logistics part of supply chain or the other way round?"

> [!tip] Strong answer includes
> - One-line hierarchy: logistics ⊂ supply chain ⊂ (arguably) the firm's overall strategy
> - Three flows (material, information, finance)
> - A short example showing the same event viewed at both levels
> - Closing with the objective: maximising surplus, not minimising logistics cost

---

## 2. Supply Chain Drivers
> 🔴 Tier 1 · _Tracker hint:_ Facilities, Inventory, Transportation, Information, Sourcing, Pricing

### Definition
Chopra & Meindl's six **drivers** are the levers a manager actually pulls to move along the *efficiency ↔ responsiveness* frontier.

| Driver | Responsiveness lever | Efficiency lever |
|---|---|---|
| **Facilities** | Many, flexible, close to customers | Few, centralised, scale economies |
| **Inventory** | High stock, wide variety | Low stock, cycle/safety stock trimmed |
| **Transportation** | Fast modes (air, express) | Slow, full-load modes (sea, rail) |
| **Information** | Real-time visibility, sharing | Fewer, cheaper systems |
| **Sourcing** | Flexible, multiple suppliers | Low-cost, consolidated suppliers |
| **Pricing** | Dynamic, differentiated by lead time | Everyday-low, stable pricing |

The first three are *physical*, the last three *cross-functional*. Information is the glue.

### Example
Amazon India: many fulfilment centres near metros (facilities), deep inventory of fast movers (inventory), own delivery fleet (transportation), real-time tracking (information), marketplace sellers (sourcing), Prime-vs-standard delivery pricing (pricing). IKEA sits at the other end: few huge warehouses, flat-pack to cut transport cost.

### In the news
See news box. Red Sea: transportation driver forced a shift; companies raised inventory (inventory driver) to compensate for the longer, less reliable lead time.

### Interview angle
> [!question] How it is asked
> "What are the drivers of supply chain performance?" or "Walk me through how you'd make this retailer's supply chain more responsive."

> [!tip] Strong answer includes
> - All six drivers named, grouped physical vs cross-functional
> - For each, which way it moves for responsiveness vs efficiency
> - Recognition that drivers interact (more facilities → lower transport cost but higher inventory)
> - Pick the 2–3 that matter most for the case instead of listing everything

---

## 3. Push vs Pull Systems
> 🔴 Tier 1 · _Tracker hint:_ Push = forecast-driven; Pull = demand-driven; Push-Pull boundary

### Definition
- **Push:** production and replenishment are planned from **forecasts**. Good for stable demand and big scale economies; risk is excess or stock-outs.
- **Pull:** execution is triggered by **actual demand** (customer order, kanban signal). Low inventory, high responsiveness; needs short lead times and flexibility.
- **Push–pull boundary (decoupling point):** the stage up to which the chain runs on forecasts (push) and after which it runs on orders (pull). Moving it *downstream* (closer to customer) means more make-to-stock; moving it *upstream* means more make-to-order.

Related: **Customer Order Decoupling Point (CODP)**: make-to-stock → assemble-to-order → make-to-order → engineer-to-order.

### Example
Dell's build-to-order model: components are bought and stocked on forecast (push), but the PC is assembled only after the order (pull), so the boundary sits at assembly. Toyota's kanban pulls parts from upstream only as the line consumes them.

### In the news
See news box. After the Nexperia shock, carmakers revisited how much buffer stock of low-cost chips to hold: a push-side decision (stock on forecast) forced by pull-side fragility.

### Interview angle
> [!question] How it is asked
> "Is Zara a push or pull supply chain?" "Where would you put the decoupling point for a laptop maker?"

> [!tip] Strong answer includes
> - Clear definitions, and that most real chains are **hybrid**
> - The decoupling point concept with a real company
> - Criteria for choice: demand uncertainty, lead time, variety, value of the product
> - Trade-off: moving the boundary changes inventory risk vs delivery time

---

## 4. Bullwhip Effect
> 🔴 Tier 1 · _Tracker hint:_ Demand amplification upstream, causes (order batching, price fluctuations), remedies

### Definition
The **bullwhip effect** is the increase in the variability of orders as you move upstream from retailer → wholesaler → manufacturer → supplier, even when end-customer demand is fairly stable.

**Measure:** Bullwhip ratio = Var(orders placed) / Var(demand received). A ratio > 1 means amplification.

For a retailer using a *p*-period moving-average forecast with lead time *L* (Chen, Drezner, Ryan, Simchi-Levi, 2000):

$$\frac{Var(Q)}{Var(D)} \ge 1 + \frac{2L}{p} + \frac{2L^2}{p^2}$$

Longer lead time and shorter forecast window both increase amplification.

**Four classic causes (Lee, Padmanabhan & Whang, 1997):**
1. **Demand signal processing**: each tier forecasts from the *orders* of the tier below, not end demand.
2. **Order batching**: periodic or lot-size ordering.
3. **Price fluctuations**: promotions and forward buying.
4. **Rationing and shortage gaming**: customers over-order when supply is short.

**Remedies:** share point-of-sale data, shorten lead times, smaller/more frequent orders, everyday-low pricing, allocation based on past sales (not orders), VMI/CPFR (see [[#8. Supply Chain Integration]]).

### Example
Procter & Gamble noticed that Pampers' retail sales were steady, yet orders to P&G and then to its suppliers of materials swung widely. Fix: data sharing and VMI with Walmart. Numeric toy example: retail demand varies ±5 units around 100; wholesaler orders ±15; manufacturer ±40, a ratio of 8× in variance at the top tier.

### In the news
> [!news] Capacity swings and front-loading (2024–2025)
> The Red Sea diversions cut effective container capacity by an estimated 15–20% in Q2 2024 (see news box). Shippers responded with earlier, larger orders and extra buffer stock, exactly the rationing-gaming and batching behaviour that amplifies upstream swings. Use it as a *current illustration*; the numeric capacity figure is sourced, the behavioural link is the analytical reading.

### Interview angle
> [!question] How it is asked
> "What is the bullwhip effect and how would you reduce it?" often inside a case about a FMCG distributor with erratic factory orders.

> [!tip] Strong answer includes
> - Definition with the order-variance idea and the retailer-to-supplier picture
> - At least three of the four causes, each paired with its remedy
> - Real company (P&G, HP printers, Barilla)
> - Distinguishes information fixes (POS sharing, CPFR) from operational fixes (lead time, batch size) and incentive fixes (pricing, allocation)

---

## 5. Value Chain Analysis
> 🔴 Tier 1 · _Tracker hint:_ Porter's Value Chain: Primary + Support Activities

### Definition
Michael Porter's **value chain** (1985) breaks a firm into activities that create value and cost.
- **Primary:** inbound logistics → operations → outbound logistics → marketing & sales → service.
- **Support:** firm infrastructure, human resource management, technology development, procurement.

**Margin** = total value created − total cost of performing the activities. Advantage comes from performing activities at lower cost (cost leadership) or in ways that raise buyer value (differentiation). Don't confuse with *supply chain* (inter-firm) or *value stream map* (lean, process-level).

### Example
Zara: design-to-shelf in about 2–3 weeks. Its edge sits in operations (in-house manufacturing of fashion-sensitive items), outbound logistics (twice-weekly store replenishment) and technology (store feedback to designers), not marketing (it spends little on advertising).

### In the news
See news box. Apple's India shift is a value-chain choice: moving *operations* (final assembly) while keeping design, software and branding in-house.

### Interview angle
> [!question] How it is asked
> "Where does this company create value?" or "Where in the value chain is the profit leak?"

> [!tip] Strong answer includes
> - Primary vs support activities, correctly named
> - Identify which 1–2 activities drive the firm's advantage
> - Link cost drivers to the case's profitability problem
> - Mention outsourcing candidates (non-core activities)

---

## 6. Supply Chain Network Design
> 🔴 Tier 1 · _Tracker hint:_ Node/arc model, facility location, hub-and-spoke vs direct

### Definition
Deciding the **number, location, capacity and role** of plants, warehouses and cross-docks, and the **flows** between them, to minimise total landed cost subject to a service level.

**Total cost** = fixed facility costs + inventory holding + transportation + handling. Adding warehouses: transportation (outbound) falls, but facility and inventory costs rise. Inventory consolidation follows the **square-root law**: safety stock scales with √(number of locations), so going from 4 DCs to 1 cuts safety stock by about 50% ($\sqrt{4}=2$).

Network models: node-arc (flow optimisation / LP), centre-of-gravity location, **hub-and-spoke** (consolidation, shorter lines) vs **direct/point-to-point** (speed, no handling). Evaluate also: tax, duties, labour, risk, and lead time to customers.

### Example
A FMCG firm has 4 regional DCs, each holding safety stock of 1,000 units. Consolidating to 1 central DC: required safety stock ≈ 1,000 × √4 = 2,000 units vs 4,000 before (assuming independent, equal demand). Saving of 2,000 units × holding cost, against higher outbound transport and slower delivery.

### In the news
See news box. Apple/Foxconn/Tata building capacity in India is network redesign (**China+1**). The Red Sea closure showed networks that depended on one corridor had no fast alternative route.

### Interview angle
> [!question] How it is asked
> "A company wants to close two warehouses. How do you decide?" or "Where would you set up a new plant for the Indian market?"

> [!tip] Strong answer includes
> - The cost trade-off (facility, inventory, transport) plus service level
> - Square-root law for inventory consolidation, with the numeric intuition
> - Non-cost factors: risk, tax (GST implications in India), proximity to suppliers
> - A clear data request: demand by pin code, current costs, lead-time targets

---

## 7. Supply Chain Performance Metrics
> 🔴 Tier 1 · _Tracker hint:_ SCOR model, Perfect Order Rate, OTIF, Cycle Time, Fill Rate

### Definition
**SCOR (Supply Chain Operations Reference)**: process model (Plan, Source, Make, Deliver, Return; Enable in SCOR 12) with attributes: **Reliability, Responsiveness, Agility, Costs, Asset Management**.

Core formulas:
- **Perfect Order Rate** = (orders on-time × in-full × damage-free × correct documentation) / total orders. Because the conditions multiply, four 95% steps give $0.95^4 \approx 81\%$.
- **OTIF** = orders delivered on time and in full / total orders.
- **Fill rate** = units shipped immediately from stock / units demanded.
- **Order cycle time** = order placed → delivered.
- **Cash-to-Cash cycle** = DIO + DSO − DPO.
- **Inventory turns** = COGS / average inventory.

### Example
Retail chain: 1,000 orders, 940 on time, of those 900 complete, of those 880 damage-free and correctly invoiced. Perfect order rate = 880/1000 = **88%**, OTIF = 90%. If DIO = 45, DSO = 30, DPO = 40: cash-to-cash = 45 + 30 − 40 = **35 days**.

### In the news
See news box. After Red Sea disruptions, reliability metrics (schedule reliability, OTIF) became board-level KPIs because transit times were no longer predictable.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track for this distribution network?" or "OTIF has dropped to 85%. Diagnose."

> [!tip] Strong answer includes
> - Balanced set across SCOR attributes (not only cost)
> - The multiplicative nature of perfect order
> - Link to cash (cash-to-cash) and customer (fill rate/OTIF)
> - For a diagnosis: split OTIF into on-time vs in-full, by supplier/lane/SKU

---

## 8. Supply Chain Integration
> 🔴 Tier 1 · _Tracker hint:_ Horizontal vs Vertical; CPFR; VMI; Information sharing

### Definition
Aligning partners' plans, data and incentives so the chain behaves like one system.
- **Vertical integration:** owning more stages (backward: suppliers; forward: distribution). **Horizontal:** merging/pooling at the same stage (shared warehouses, logistics alliances).
- **VMI (Vendor-Managed Inventory):** supplier owns replenishment decisions at the customer's stock location.
- **CPFR (Collaborative Planning, Forecasting & Replenishment):** joint business plan, shared forecast and exception management.
- Degree of integration: internal → supplier/customer → full network.

### Example
Walmart–P&G VMI (1980s) cut Walmart's stock-outs and P&G's volatility. Reliance Retail sharing demand data with FMCG suppliers is a modern equivalent.

### In the news
See news box. Nexperia showed the limit of visibility: most carmakers did not know their tier-2 and tier-3 exposure to one chipmaker until supply stopped.

### Interview angle
> [!question] How it is asked
> "Should the company vertically integrate its supplier?"

> [!tip] Strong answer includes
> - Control vs flexibility/capital trade-off
> - Criteria: asset specificity, risk, scale, capability
> - Alternatives short of ownership: long-term contracts, JVs, VMI
> - What data must be shared and how incentives are aligned

---

## 9. Supply Chain Strategy
> 🔴 Tier 1 · _Tracker hint:_ Efficient vs Responsive SC; Lean vs Agile; Fisher's framework

### Definition
**Fisher (1997):** match the chain to the product.
| Product | Demand | Margin | Right chain |
|---|---|---|---|
| Functional (staples) | Predictable | Low | **Efficient**: cost, utilisation, low inventory |
| Innovative (fashion, tech) | Unpredictable | High | **Responsive**: buffer capacity, speed, flexibility |

**Lean vs Agile:** lean eliminates waste for stable demand; agile responds to volatility. **Leagile** combines them around a decoupling point. Strategy must fit competitive strategy (cost leadership vs differentiation): the *strategic fit* concept (Chopra & Meindl).

### Example
Maggi/ Parle-G (functional): efficient. Zara fast fashion (innovative): responsive, with local sourcing for volatile lines and low-cost sourcing for basics.

### In the news
See news box. Companies are moving from pure efficiency ("just-in-time") to **resilience** ("just-in-case"), which Fisher's framework misses.

### Interview angle
> [!question] How it is asked
> "What supply chain strategy fits a premium smartphone vs a staple like salt?"

> [!tip] Strong answer includes
> - Fisher matrix and justification by demand uncertainty
> - Strategic fit with competitive strategy
> - Flag when a firm is mismatched (efficient chain for innovative product → stock-outs)
> - Modern addition: resilience

---

## 10. Omnichannel SCM
> 🔴 Tier 1 · _Tracker hint:_ Click-and-collect, unified inventory, last-mile, returns

### Definition
Serving customers seamlessly across store, web, app and marketplace using **one view of inventory** and flexible fulfilment (ship-from-store, BOPIS/click-and-collect, pick-up points, home delivery) and a managed **reverse flow** (returns, which can be 20–30% in online fashion).

Key challenges: inventory visibility, order orchestration, last-mile cost (often ~40–50% of delivery cost), returns handling, and conflict between channels (pricing, margins).

### Example
Reliance Retail's JioMart fulfils online grocery orders from nearby stores; Walmart US popularised store-as-warehouse for pick-up. Blinkit-style dark stores serve a 2–3 km radius in ~10 minutes.

### In the news
> [!news] Quick commerce and dark stores (Dec 2024 – FY26)
> HSBC Global Research expected India's quick-commerce chains to reach **5,000–5,500 dark stores by FY2025-26**: Blinkit had 1,000+ stores in the Dec-2024 quarter (216 added in one quarter), Zepto ~850, Swiggy Instamart heading to 1,000. HSBC projected gross order value of **$35–40 bn by FY2027-28**, with players then shifting from expansion to optimising capacity. A textbook case of pushing inventory to a dense local node network. ([Entrepreneur India](https://india.entrepreneur.com/news-and-trends/indias-quick-commerce-landscape-to-transform-with-5000/486062))

### Interview angle
> [!question] How it is asked
> "How would an apparel retailer integrate online and offline inventory?"

> [!tip] Strong answer includes
> - Single inventory view and order management
> - Fulfilment options and the trade-off of each
> - Returns policy and economics
> - KPIs: fulfilment cost per order, delivery time, return rate, availability

---

## 11. Trade-offs in SCM
> 🔴 Tier 1 · _Tracker hint:_ Cost vs service level; centralization vs decentralization

### Definition
Every decision trades one objective for another. The **efficient frontier** of cost vs responsiveness: a firm either moves along it (accepting more cost for service) or shifts it (better technology, information).

Typical trade-offs: more inventory ↔ fewer stock-outs; centralise ↔ lower inventory but longer lead time; fast transport ↔ cost; flexibility ↔ utilisation; low-cost supplier ↔ risk concentration. Quantify with **total cost of ownership** and **service level targets**.

### Example
Reducing the service level target from 98% to 95% lowers the safety-stock Z-value from 2.05 to 1.65, cutting safety stock by about 20% ($1 - 1.65/2.05 \approx 19.5\%$) at the price of 3 pp more stock-outs.

### In the news
See news box. Many firms accepted higher cost (extra supplier, dual sourcing) for resilience after 2024–25 shocks.

### Interview angle
> [!question] How it is asked
> "The CEO wants both lower cost and higher service level. What do you say?"

> [!tip] Strong answer includes
> - Acknowledge the frontier, then show how to *shift* it (information sharing, postponement, better forecasting)
> - Quantify an example
> - Segment SKUs/customers (not every item deserves the same service level)

---

## 12. Supply Chain Collaboration
> 🔴 Tier 1 · _Tracker hint:_ Joint planning, shared KPIs, cross-docking, co-manufacturing

### Definition
Partners jointly plan and share risks and rewards. Forms: joint planning (S&OP with customers/suppliers), shared KPIs and gain-share contracts, **cross-docking** (inbound goods moved to outbound with no storage), **co-manufacturing/contract manufacturing**, 3PL/4PL partnerships. Success factors: trust, data transparency, aligned incentives, governance. Failure causes: opportunism, asymmetric power, IT incompatibility.

### Example
Retailer–supplier cross-docking at Walmart: goods arrive and leave in under 24 hours with minimal storage. Co-manufacturing: a large FMCG firm hires a contract bottler to cover peak seasons.

### In the news
See news box. Companies pushing deeper supplier visibility programmes after Nexperia is collaboration as risk-management.

### Interview angle
> [!question] How it is asked
> "How would you build a closer relationship with your top 5 suppliers?"

> [!tip] Strong answer includes
> - Segment partners by criticality ([[002 Procurement & Strategic Sourcing]] Kraljic)
> - Mechanisms: shared forecasts, joint improvement, gain-sharing
> - Governance and KPIs
> - Risks of dependence and how to hedge

---
## 🔗 Go deeper: expansion notes
- [[111 SCOR Model & Supply Chain Process Frameworks|SCOR Model & Supply Chain Process Frameworks]]
- [[112 Supply Chain Strategy - Fit, Segmentation & Maturity|Supply Chain Strategy - Fit, Segmentation & Maturity]]
- [[114 Bullwhip Effect, Beer Game & Information Sharing|Bullwhip Effect, Beer Game & Information Sharing]]
- [[141 Supply Chain Disruption Case Library (2011-2026)|Supply Chain Disruption Case Library (2011-2026)]]
- [[142 Company Supply Chain Case Library|Company Supply Chain Case Library]]
- [[143 SCM Interview Question Bank|SCM Interview Question Bank]]
