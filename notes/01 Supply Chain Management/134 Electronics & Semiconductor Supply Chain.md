---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Electronics & Semiconductor Supply Chain"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Electronics & Semiconductor Supply Chain

⬅ [[133 Food, Agri & Perishables Supply Chain - India]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[135 Reverse Logistics, Remanufacturing & EPR in India]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Semiconductor Value Chain: Design to Distribution]]
2. [[#2. Why Lead Times Are 12-26 Weeks (and What They Do to Safety Stock)]]
3. [[#3. Concentration Risk: TSMC, ASML & Geography]]
4. [[#4. The 2020-23 Shortage as a Bullwhip Case]]
5. [[#5. Nexperia-Type Events: Policy, Ownership & Packaging Single Points]]
6. [[#6. Allocation, Long-Term Agreements & Buying Strategies for Chips]]
7. [[#7. EMS & ODM: Foxconn, Dixon and the Contract-Manufacturing Model]]
8. [[#8. India Semiconductor Mission & Electronics Incentive Schemes]]
9. [[#9. Apple's China+1 Shift to India]]
10. [[#10. Component Obsolescence, Last-Time Buy & Lifecycle Management]]
11. [[#11. Counterfeit Parts & Gray-Market Risk]]
12. [[#12. Rare Earths, Critical Minerals & Electronics Inputs]]
13. [[#13. Product Lifecycle & Demand Volatility in Electronics]]
14. [[#14. ⭐ Advanced: A Resilient Electronics Sourcing Strategy (BOM Risk Scoring)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): chips are a geopolitical asset, and India is trying to move from assembling phones to making components
> **Nexperia dispute (October-November 2025).** The Dutch government took control of Nexperia's governance on national-security grounds (Goods Availability Act), China then banned Nexperia from exporting locally packaged products, and automakers scrambled for simple chips (switches, logic, LED-headlight drivers, battery-management parts). Honda halted its Celaya plant in Mexico and cut output in the US and Canada; Nissan warned of a possible large-scale problem. The Dutch government suspended its control on 19 November 2025, but Wingtech continued to challenge it in court. Nexperia makes about 100 billion units a year (2022 figure) and holds only about 5% of the automotive discrete market by revenue, yet far more by volume. ([Wikipedia: Nexperia](https://en.wikipedia.org/wiki/Nexperia), [WTOP/AP](https://wtop.com/europe/2025/11/a-crisis-at-chipmaker-nexperia-sent-automakers-scrambling-heres-what-to-know/), [Japan Times](https://www.japantimes.co.jp/business/2025/10/30/companies/honda-mexico-production-halt/))
>
> **iPhone exports hit ₹2 trillion (FY2025-26).** iPhones were over 75% of India's ₹2.6 trillion smartphone exports in FY26, up from about ₹1.5 trillion in FY25, in the final year of the large-scale electronics PLI; Tata Electronics ($26.3 billion of iPhone exports, FY22-FY26) edged past Foxconn ($25.6 billion) after buying Wistron's India operation (November 2023) and a 60% stake in Pegatron's (2024). ([Business Standard, 29 April 2026](https://www.business-standard.com/companies/news/iphone-exports-hit-record-2-trillion-in-final-year-of-smartphone-pli-126042901178_1.html), [Business Standard, 2 July 2026](https://www.business-standard.com/technology/tech-news/tata-electronics-pips-foxconn-in-india-iphone-exports-worth-26-3-billion-126070201178_1.html))
>
> **India Semiconductor Mission moves toward fabs (September 2026).** ASML began India operations in September 2026. Tata Electronics' Dholera fab, India's first 300 mm fab, is planned at 50,000 wafers a month with launch scheduled for 2028; a "Semicon 2.0" scheme of ₹1.27 lakh crore was reported. A separate analysis found India holding only 0.6% of global semiconductor funding in 2026 and a chip trade deficit of $34 billion in 2025-26 (against $6.8 billion in 2017-18). ([Business Standard, 20 September 2026](https://www.business-standard.com/technology/tech-news/asml-begins-india-operations-plans-to-hire-young-engineering-graduates-126092000591_1.html), [Business Standard, 27 September 2026](https://www.business-standard.com/industry/news/statsguru-india-s-chip-aspirations-face-funding-gap-despite-policy-push-126092700857_1.html))
>
> **Foxconn doubles down in Tamil Nadu (October 2025).** Foxconn announced a ₹15,000 crore investment in Tamil Nadu with about 14,000 engineering jobs. ([Business Standard, 13 October 2025](https://www.business-standard.com/companies/news/foxconn-rs-15000-crore-investment-tamil-nadu-ai-manufacturing-jobs-125101300504_1.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Semiconductor Value Chain: Design to Distribution
> 🟠 Tier 2 · _Key points:_ fabless, foundry, IDM, OSAT, EMS, distributors, equipment, materials

### Definition
The chip chain has distinct layers, each concentrated in a few firms:
1. **Design**: **fabless** companies (Qualcomm, Nvidia, MediaTek) and in-house design at **IDMs** (Intel, Samsung, TI, Infineon, NXP); tools from **EDA** vendors (Synopsys, Cadence) and IP such as Arm.
2. **Equipment and materials**: lithography (ASML), deposition and etch (Applied Materials, Lam, Tokyo Electron), silicon wafers, photoresists and specialty gases (Japan has high shares).
3. **Fabrication (front end)**: wafers processed in **foundries** (TSMC, Samsung, GlobalFoundries, UMC, SMIC) or IDM fabs; 400-1,000+ process steps over roughly 2-4 months of cycle time.
4. **Assembly, test and packaging (back end)**: **OSAT** firms (ASE, Amkor, JCET); India's first projects are here (Micron's ATMP in Sanand, Tata's Assam OSAT, Kaynes, CG Power).
5. **Distribution**: franchised distributors (Arrow, Avnet, Digi-Key, Mouser) and independent brokers.
6. **Board and product assembly**: **EMS** (electronics manufacturing services: Foxconn, Flex, Jabil, Dixon) and **ODM** (original design manufacturers) for the brand owner (Apple, Samsung, automakers).

Semiconductors are the cheapest (by value) but most critical part of many products; categories: logic, memory (DRAM, NAND), analogue and power, discretes, and sensors. The industry is cyclical, capital-intensive (a leading fab costs tens of billions of dollars) and demand-driven by phones, PCs, cars, industrial and, recently, AI servers (see the Foxconn items in [[016 Digital Supply Chain & Industry 4.0]] for the technology side).

### Example
A smartphone's bill of materials (BOM) of ₹20,000 might include chips worth ₹7,000 and display, battery and mechanicals worth the rest. The chips pass through design (royalty and margin), wafer fab, OSAT, distributor and EMS, and each stage adds a margin and 4-12 weeks of lead time. Because the fab and the lithography tool owner capture the highest value, a country that only does final assembly (EMS) captures a small share of product value; the policy pivot is therefore toward components, OSAT and fabs.

### In the news
See news box. The ASML arrival, the Tata fab plan and the 0.6% funding share capture both the ambition and the distance to travel in India.

### Interview angle
> [!question] How it is asked
> "Walk me through the semiconductor supply chain and tell me where the bottlenecks are."

> [!tip] Strong answer includes
> - The layers (design, equipment, fab, OSAT, distribution, EMS) with examples
> - Concentration points: leading-edge foundry, EUV lithography, specialty materials
> - Long lead times and capital intensity as structural features
> - Where India participates (OSAT, EMS, design) and where it does not yet (leading-edge fab)

---
## 2. Why Lead Times Are 12-26 Weeks (and What They Do to Safety Stock)
> 🟠 Tier 2 · _Key points:_ cycle time, capacity planning, product mix, buffer, safety stock grows with square root of L

### Definition
Chip order-to-delivery lead times typically run **12-26 weeks** and peaked beyond that in the shortage. Components of the lead time:
- **Fab cycle time**: hundreds of steps, queueing at bottleneck tools, and "hot lots" that cut the queue but consume capacity.
- **Wafer start planning**: foundries plan capacity quarters ahead and allocate wafer starts by product, customer and node.
- **Back end**: assembly, test and packaging, with substrate (ABF) and test-capacity constraints.
- **Logistics and distribution**: air freight, customs, consolidation.
- **Capacity addition**: a new fab takes 2-4 years and a very large investment; so supply cannot respond within a year.

Effect on planning: forecast horizon must exceed lead time. Safety stock for a lead-time demand: $SS = z\sigma_d\sqrt{L}$ where $L$ is lead time in the same units as $\sigma_d$ (assuming constant lead time; see [[003 Inventory Management]]); with variable lead time, $SS = z\sqrt{L\sigma_d^2 + \mu_d^2\sigma_L^2}$.

### Example
Weekly demand for a microcontroller: mean 10,000 units, standard deviation 2,000. At 95% service ($z=1.65$): with $L=12$ weeks, $SS = 1.65 \times 2000 \times \sqrt{12} \approx$ **11,432** units; with $L=26$ weeks, $SS = 1.65 \times 2000 \times \sqrt{26} \approx$ **16,827**: +47% more safety stock. Add pipeline stock (mean demand × L): 120,000 vs 260,000 units, a rise of 140,000. A buyer who cuts the planned lead time by doing VMI at the distributor, or stocking through a hub, avoids carrying that extra inventory at its own balance sheet.

### In the news
See news box. Honda's Celaya halt shows that with 12-26 week upstream lead times, a few days' disruption at a Chinese packaging site cannot be recovered by re-ordering: the buffer must exist before the event.

### Interview angle
> [!question] How it is asked
> "Why can't chip makers just ramp up production when demand spikes? What does that imply for a buyer?"

> [!tip] Strong answer includes
> - Cycle time, capacity cadence and 2-4 year capex lead time
> - Quantified lead-time effect on safety and pipeline stock
> - Buyer actions: earlier forecasts, LTAs, strategic buffer on high-risk parts, design flexibility
> - Why forecast accuracy matters more than inventory alone ([[004 Demand Forecasting & Planning]])

---
## 3. Concentration Risk: TSMC, ASML & Geography
> 🟠 Tier 2 · _Key points:_ leading-edge share, EUV monopoly, Taiwan, single points of failure, specialty chemicals

### Definition
Different layers show different degrees of concentration: roughly two-thirds of global **foundry revenue** and the large majority of **leading-edge (below 7 nm)** logic is made by TSMC in Taiwan (industry-tracker estimates, which move quarter to quarter); **ASML** is the only supplier of **EUV lithography** machines (described in the business press as a monopoly in advanced lithography); advanced memory is dominated by three firms (Samsung, SK Hynix, Micron); advanced packaging and substrates have their own bottlenecks; and Japan supplies a large share of photoresist and wafer materials. For **mature-node chips (28 nm and above)**, which cars, appliances and industrials use, China is expanding rapidly, creating both price pressure and geopolitical exposure.

Risk framing: **single point of failure** (one fab or one tool vendor), **geopolitical risk** (Taiwan Strait, export controls on advanced chips and tools, China's controls on critical minerals), **natural hazard** (earthquake, drought, power outage), and **policy risk** (tariffs, local-content rules). A mitigation path combines **geographic diversification** (TSMC Arizona/Japan/Germany, Intel, Samsung US, India's Dholera and Sanand), **dual sourcing at design stage**, and inventory of the highest-impact parts ([[015 Supply Chain Risk & Resilience]]).

### Example
A company sources a power-management chip from a single fab. Probability of a month-long outage in a year = 4%; impact (lost contribution) = ₹250 crore per month of outage. Expected loss = 0.04 × 250 = **₹10 crore a year**. Mitigation: qualify a second source that can cover 70% of needs during an outage, and keep it "warm" with 20% of normal volume. Cost: ₹6 crore one-time (≈ ₹1.5 crore a year over 4 years) plus a 3% price premium on that 20% of volume (₹0.6 crore on ₹100 crore of chip spend) = about **₹2.1 crore a year**. Expected loss falls to 0.04 × 250 × 0.3 = ₹3 crore, a saving of ₹7 crore, so the net benefit is about 7 − 2.1 = **₹4.9 crore** a year in expectation. The numbers are assumptions; the structure (expected loss avoided vs cost of mitigation) is the point.

### In the news
See news box. The Nexperia episode concentrated risk differently: a Dutch-owned, China-owned and China-packaged supply loop had a single policy failure point even though the chips were commodity discretes.

### Interview angle
> [!question] How it is asked
> "Is concentration in Taiwan the biggest semiconductor risk? What else worries you?"

> [!tip] Strong answer includes
> - Layers: foundry, EUV tools, memory, materials, packaging, mature-node China
> - The probability x impact logic and mitigation cost comparison
> - Policy risks: export controls, rare earth/critical mineral controls, tariffs
> - Responses: diversification (including India), dual sources, buffers, and design for substitution

---
## 4. The 2020-23 Shortage as a Bullwhip Case
> 🟠 Tier 2 · _Key points:_ cancellation, reallocation, double ordering, amplification, glut after

### Definition
Sequence: (1) Early 2020: car demand falls, automakers cut chip orders; (2) foundries reassign capacity to booming PC, phone and gaming demand; (3) auto demand returns in H2 2020 faster than expected; (4) chip lead times stretch, buyers panic-order and **double-order** to hold a place in queue (phantom demand); (5) shortages worsen through 2021 with fabrication constraints, Malaysian COVID lockdowns and plant incidents; (6) by 2023, inventory builds and orders get cancelled, and memory and consumer chips go into a glut: the classic **bullwhip** cycle ([[114 Bullwhip Effect, Beer Game & Information Sharing]]). AlixPartners estimated in September 2021 that the shortage would cost automakers **$210 billion of revenue** and **7.7 million vehicles** in 2021 (vs $110 billion and 3.9 million in May 2021).

Amplification of order variability in an order-up-to system with moving-average forecasting over $p$ periods and lead time $L$:

$$\frac{\text{Var(orders)}}{\text{Var(demand)}} \geq 1 + \frac{2L}{p} + \frac{2L^2}{p^2}$$

Each tier multiplies this factor.

### Example
Take $L=3$ months and $p=6$ months: factor = 1 + 2(3)/6 + 2(9)/36 = 1 + 1 + 0.5 = **2.5** for one tier; across three tiers (OEM to Tier 1 to chip distributor to chip maker) the amplification is about 2.5³ = **15.6**, and for four tiers 39. A 5% swing in car demand therefore appears as a very large swing at the foundry. Order inflation magnifies it: suppose supply is 70 units against true needs of A 50, B 30, C 20 (total 100). Pro-rata on true needs gives A 35, B 21, C 14. If A doubles its order to 100 (total 150), pro-rata on orders gives A **46.7**, B **14.0**, C **9.3**: gaming the allocation gains A 11.7 units at others' expense, which is why suppliers move to history-based allocation and non-cancellable orders.

### In the news
See news box. In 2025 the trigger was different (a corporate-control and export-ban dispute), but the same panic-buying and re-allocation pattern reappeared.

### Interview angle
> [!question] How it is asked
> "Was the chip shortage a supply problem or a demand-planning problem?"

> [!tip] Strong answer includes
> - Both: demand collapse and recovery plus constrained capacity and inelastic supply
> - Bullwhip mechanics: order batching, shortage gaming, price fluctuation, lead time
> - Quantification (amplification factor or allocation example)
> - Fixes: share real end-demand data, commitments with flexibility bands, and cut lead times

---
## 5. Nexperia-Type Events: Policy, Ownership & Packaging Single Points
> 🟠 Tier 2 · _Key points:_ discrete chips, ownership, wafer-to-package loop, export bans, 2025 timeline

### Definition
A **Nexperia-type event** is a supply break caused not by capacity but by **ownership, legal or export-control action** on a node in the chain. In 2025: Wingtech (China) owned Nexperia (Netherlands), after buying it in 2018 for about $3.6 billion; the US had put Wingtech on its entity list; the Dutch ministry took over governance in October 2025; wafer shipments from Nexperia's German fab to its Chinese packaging plant in Dongguan stopped; China banned export of locally packaged Nexperia products; carmakers (Honda, Nissan, Ford, GM, VW and others cited) feared shutdowns. The Dutch government suspended its order on 19 November 2025, and chip sales resumed in part, while litigation continued (Wikipedia's timeline mentions further court steps into 2026).

Lessons: (1) **Low-value discrete chips** are single points of failure; (2) the **front-end/back-end split** across countries makes the product vulnerable to either country's controls; (3) OEMs had **no visibility** beyond Tier 1; (4) **qualification time** for substitute parts (AEC-Q101 and customer validation) is months; (5) the event cost much more than the parts' price.

### Example
A Tier-1 uses 12 Nexperia-type diodes in each module at ₹6 each (₹72 per module) in a product with ₹3,000 BOM sold for ₹4,500. Daily production is 8,000 modules. Chip spend per day = 8,000 × 72 = ₹5.76 lakh. A line stop costs the contribution margin, say ₹500 per module = ₹40 lakh per day: **7 times the chip spend**. A buffer of 30 days of the chip stock at ₹5.76 lakh per day = ₹1.73 crore, which at 12% a year costs ₹20.7 lakh annually (₹1.73 crore × 12%), equal to half a day of a line stop. Qualifying a pin-compatible alternate, even at a 20% premium on the part (₹1.15 lakh a day extra at full volume), is cheap compared with a multi-week stop.

### In the news
See news box. Honda's Celaya plant built over 190,000 vehicles in the previous year, so a halt of weeks represents tens of thousands of vehicles.

### Interview angle
> [!question] How it is asked
> "A Tier-2 chip supplier is caught in a political dispute and you have 3 weeks of stock. What do you do this week?"

> [!tip] Strong answer includes
> - Triage: exposure by part and by plant, days of cover, alternates, spot-market and broker options with counterfeit controls
> - Contact: supplier, distributor, regulators; allocate scarce parts to highest-margin or highest-contract-penalty lines
> - Medium term: second source, design change, buffer stock and tier-N mapping
> - Communication to customers and impact estimation

---
## 6. Allocation, Long-Term Agreements & Buying Strategies for Chips
> 🟠 Tier 2 · _Key points:_ NCNR, LTA, prepayment, allocation rules, distributors vs direct, consignment hubs

### Definition
In shortage, suppliers **allocate** capacity: priority to strategic customers, long-term-agreement (LTA) holders and those with committed forecasts. Tools:
- **LTA/capacity reservation**: volume commitment over 1-3 years, sometimes with **prepayment** or **take-or-pay** clauses; price may be indexed or fixed.
- **NCNR** (non-cancellable, non-returnable) orders, which shift risk to buyers.
- **Frame contracts with call-offs**, **VMI/consignment hubs** near EMS plants.
- **Direct vs distributor**: large OEMs deal direct; mid-size firms depend on franchised distributors and risk broker markets.
- **Flexibility bands** (±20% on a rolling forecast), **last-time-buy** rights, **price-adjustment** formulae.

Buyer considerations: commit to volumes you will use (avoid becoming the buyer of obsolete stock), keep multiple qualified alternates, and use a **should-cost** view of price. Procurement categories fall in Kraljic's bottleneck/strategic quadrants ([[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]], [[002 Procurement & Strategic Sourcing]]).

### Example
An OEM needs 1.2 million chips a year. Spot price ₹40; LTA price ₹46 with 80% take-or-pay (960,000 units minimum). If demand falls 30% to 840,000 units, it pays the shortfall of 120,000 × ₹46 = ₹55.2 lakh (take-or-pay on the minimum). Total cost = (840,000 + 120,000) × 46 = ₹4.416 crore for 840,000 useful chips = **₹52.6 per usable chip**, above the ₹40 spot price. If shortage returns and spot hits ₹120, the LTA saves 840,000 × (120 − 46) = ₹6.2 crore: the LTA is insurance, and the premium pays off only if shortage probability is high enough. If the probability of a shortage year is 30%: expected spot cost = 0.3 × 120 + 0.7 × 40 = ₹64 per chip, above the LTA's ₹46 (or ₹52.6 effective if volume falls 30%).

### In the news
See news box. After the 2021 episode and Nexperia 2025 many OEMs moved to direct contracts with chipmakers, bypassing Tier 1 intermediation for critical parts.

### Interview angle
> [!question] How it is asked
> "Should we sign a 3-year take-or-pay agreement for a critical chip?"

> [!tip] Strong answer includes
> - Expected-cost comparison under shortage/no-shortage scenarios
> - Contract terms: flexibility band, price indexation, termination, last-time-buy
> - Supplier health and dual sourcing in parallel
> - Governance: forecasting discipline and cross-functional approval

---
## 7. EMS & ODM: Foxconn, Dixon and the Contract-Manufacturing Model
> 🟠 Tier 2 · _Key points:_ EMS vs ODM, margins, BOM pass-through, scale, customer concentration, PLI

### Definition
**EMS** (electronics manufacturing services) assembles products for brand owners using the customer's design and often the customer's BOM (components bought by the customer or EMS with pass-through). **ODM** (original design manufacturing) also designs the product, owns IP and sells under the customer's brand. Large players: Foxconn (Hon Hai), Pegatron, Wistron, Flex, Jabil; in India Dixon, Tata Electronics, Kaynes, Amber, and the bigger EMS in Chennai and Noida. **Dixon** (founded 1993, IPO 2017) makes TVs, washing machines, smartphones, LED bulbs and security systems for brands including Samsung, Xiaomi, Panasonic, Philips, Motorola and Google, reported FY2025 revenue of about ₹38,880 crore, and formed a joint venture with Vivo in December 2024 (per Wikipedia's summary).

Economics: EMS earns **low single-digit EBITDA margins on a large pass-through revenue base**, so returns come from scale, utilisation, **working-capital turns** and yield; ODM earns more through design and component sourcing. Risks: customer concentration, component allocation, price-downs, and **inventory risk** if BOM is bought on the EMS balance sheet. Typical metrics: **yield**, **OEE**, **line changeover**, **inventory turns**, **cash conversion cycle** ([[018 Capacity Management & OEE]], [[136 Supply Chain Finance & Working Capital]]).

### Example
An EMS earns revenue of ₹1,000 on a phone where ₹850 is pass-through BOM and ₹150 is its own value-add; its cost of conversion and overhead is ₹120, so EBITDA = ₹30 (3.0% of revenue, 20% of value-add). Government incentive of 5% of incremental sales adds ₹50 on ₹1,000 and turns EBITDA to ₹80 (8%). A 1 percentage-point yield loss on ₹1,000 of production costs about ₹10: a third of the base EBITDA, so yield and scrap discipline are central. If BOM inventory days are 30 and the EMS buys BOM at 850, BOM inventory of 30 days ties up 850 × 30/365 = ₹69.9 per ₹1,000 of annual revenue, which at 10% cost of capital is ₹7 and matters against EBITDA of ₹30.

### In the news
See news box. Tata Electronics overtaking Foxconn in cumulative iPhone exports (FY22-FY26) and Foxconn's ₹15,000 crore Tamil Nadu plan show the large EMS players scaling inside India.

### Interview angle
> [!question] How it is asked
> "How does an EMS company make money on thin margins and what are its main supply chain risks?"

> [!tip] Strong answer includes
> - EMS vs ODM and pass-through revenue concept
> - Margin levers: yield, utilisation, working capital, incentive income, move to ODM and component manufacturing
> - Risks: customer concentration, allocation, forex, inventory write-offs
> - India context: PLI-enabled scale and the shift to component localisation

---
## 8. India Semiconductor Mission & Electronics Incentive Schemes
> 🟠 Tier 2 · _Key points:_ ISM, ATMP/OSAT, fab, PLI LSEM, ECMS, design-linked incentive, DVA

### Definition
India's policy stack: the **India Semiconductor Mission (ISM)**, announced in December 2021 with an outlay of about ₹76,000 crore, supports fabs, display fabs, compound semiconductors and **OSAT/ATMP** with fiscal support (up to 50% of project cost for eligible projects); the **Design-Linked Incentive**; the **PLI for large-scale electronics manufacturing (LSEM)** (mobile phones, IT hardware) from FY2021-22 (the final year was FY26 per Business Standard); and the **Electronics Component Manufacturing Scheme (ECMS)** (2025) to deepen component and sub-assembly localisation. Approved projects per Wikipedia's summary: **Tata-Powerchip fab at Dholera** (about ₹91,000 crore, 28 nm, 50,000 wafer starts a month); **Micron ATMP at Sanand** ($2.75 billion); **Tata OSAT in Assam** (₹27,000 crore); **CG Power-Renesas-Stars OSAT**; **Kaynes OSAT** (₹3,307 crore); and an HCL-Foxconn display-driver chip plant. Business Standard reported in September 2026 that a "Semicon 2.0" scheme of ₹1.27 lakh crore has been reported for the next phase.

Supply-chain implications: fabs need **ultra-pure water, stable power, specialty gases and chemicals**, equipment vendors' presence (ASML opened India operations in September 2026), vendor parks (about 450 vendors, 363 vendor parks under construction at Dholera per the report), and skilled engineers. Domestic demand (autos, phones, appliances, telecom, defence) is the anchor; export competitiveness is the challenge.

### Example
Suppose a government gives 50% fiscal support on a ₹10,000 crore OSAT plant (₹5,000 crore) with state matching of 20% of project cost (₹2,000 crore): company equity and debt required = 10,000 − 7,000 = **₹3,000 crore**. If the plant earns ₹1,800 crore of revenue a year at a 25% EBITDA margin (₹450 crore), payback on its own capital is 3,000/450 = **6.7 years**; without incentives it would be 10,000/450 = 22 years. This is why such plants only exist under incentive schemes in early years; sustainable returns depend on utilisation and customer commitments (anchor customers).

### In the news
See news box. India's 0.6% share of semiconductor funding in 2026 and a $34 billion chip trade deficit indicate that capital deployment, not just announcements, is the gap.

### Interview angle
> [!question] How it is asked
> "Is India's semiconductor mission realistic? What would you prioritise?"

> [!tip] Strong answer includes
> - Segments: OSAT first, mature-node fab next, design and components
> - Requirements: anchor demand, utilities, vendor ecosystem, talent, equipment supply
> - Economics: incentive share, payback, utilisation risk
> - Linkage to electronics PLI/ECMS and auto/EV demand ([[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]])

---
## 9. Apple's China+1 Shift to India
> 🟠 Tier 2 · _Key points:_ iPhone exports, PLI, Tata/Foxconn, vendor base, localisation, tariffs

### Definition
**China+1** means adding a second production base while retaining China. Apple's drivers: geopolitical and tariff risk, COVID-era lockdowns (Zhengzhou 2022), and Indian PLI incentives. India's path: Foxconn began iPhone assembly in 2019; PLI began in FY2021-22; Wistron and Pegatron India units were taken over by Tata Electronics (100% of Wistron in November 2023; 60% of Pegatron in 2024). Results: iPhone exports of ₹9,351.6 crore (FY22), ₹44,269.5 crore (FY23), ₹85,013.5 crore (FY24), about ₹1.5 trillion (FY25) and about ₹2 trillion (FY26, 11 months), with iPhones over 75% of smartphone exports; around 250,000 people are employed across Apple's Indian ecosystem including 40+ component suppliers, with a majority-female workforce at the assembly plants (per Business Standard).

Constraints: India still imports most high-value components (displays, chips, camera modules), so **domestic value addition** is modest; tariffs and policy shifts (US tariff changes in 2025-26) affect the economics; labour and logistics (air freight to the US, customs time) matter; and Chinese export restrictions on equipment or engineers can slow ramp-up.

### Example
Exports grew from ₹85,013.5 crore (FY24) to ₹1.5 trillion (FY25), a 76% rise, and to ₹2 trillion in FY26 (+33%). Compound growth FY22 to FY26: (200,000/9,351.6)^(1/4) − 1 = about **2.15 times a year**, that is roughly 115% a year. If domestic value addition on an iPhone is 15% of the ex-factory price (an assumption for illustration), ₹2 trillion of exports corresponds to about ₹30,000 crore of India-made value, about ₹1.7 lakh crore of imported content; the policy goal is to raise that 15% through component localisation.

### In the news
See news box. The ₹2 trillion export figure makes Apple India's largest single branded export and signals the scale of the China+1 shift.

### Interview angle
> [!question] How it is asked
> "Why has Apple shifted production to India, and what must happen for India to capture more value?"

> [!tip] Strong answer includes
> - Drivers: risk diversification, PLI, tariffs, scale of Indian talent
> - Measures: export growth, share, employment
> - Value capture: component localisation, supplier parks, logistics and power
> - Risks: dependency on one anchor customer, policy and tariff swings

---
## 10. Component Obsolescence, Last-Time Buy & Lifecycle Management
> 🟠 Tier 2 · _Key points:_ PCN, EOL, LTB, DMSMS, redesign, lifecycle mismatch

### Definition
Electronic parts have lifecycles of 5-10 years or less, while industrial, medical, automotive and defence products last 10-30 years: the **lifecycle mismatch**. Suppliers issue **product change notifications (PCN)** and **end-of-life (EOL)** notices; buyers get a window (often 6-12 months) for a **last-time buy (LTB)**. Alternatives: **redesign** with a new part, **form-fit-function (FFF) alternate**, **aftermarket sources/re-manufacturing**, or stock **buffer**. Tools: BOM health tools (SiliconExpert, Z2Data, etc.), obsolescence forecasting, and **DMSMS** (diminishing manufacturing sources and material shortages) programmes in defence. Obsolescence management is part of design: prefer parts with long-life commitments, second sources, and standard footprints.

LTB sizing: buy enough to cover the remaining production and service demand until redesign or end of support, balanced against holding costs and risk of overbuy.

### Example
A controller needs a chip that goes EOL. Annual demand 12,000 units for 8 years of remaining service life = 96,000 chips at ₹120 = ₹1.152 crore. Average stock is half the LTB (₹57.6 lakh), holding cost at 12% a year for 8 years = ₹55.3 lakh. Total = 115.2 + 55.3 = ₹170.5 lakh, i.e. ₹177.6 per chip held to use. A redesign with a new chip costs ₹90 lakh in engineering and re-qualification plus ₹100 per chip purchases (96,000 × 100 = ₹96 lakh): total **₹186 lakh**: nearly equal, so the decision depends on risk: if demand turns out 25% lower, LTB leaves unused stock of 24,000 × ₹120 = **₹28.8 lakh** written off, but redesign has no such exposure, so a partial LTB covering 3-4 years plus redesign may beat either extreme.

### In the news
See news box. After a shock, companies add alternates and review BOM risk; the 2025 events accelerated "design for substitution" in discrete parts.

### Interview angle
> [!question] How it is asked
> "A supplier announces end of life for a critical part used in a 15-year product. What are your options?"

> [!tip] Strong answer includes
> - Options: LTB, alternate, redesign, aftermarket or reclaimed supply
> - LTB sizing with demand uncertainty and holding cost
> - Cost comparison and risk-based decision
> - Preventive: lifecycle checks at design stage, BOM health monitoring, long-life supplier agreements

---
## 11. Counterfeit Parts & Gray-Market Risk
> 🟠 Tier 2 · _Key points:_ brokers, remarked parts, testing, authorised channels, standards

### Definition
During shortages, buyers turn to **independent distributors and brokers**, where **counterfeit** (fake, remarked or recycled) parts appear: used chips with sanded and re-marked tops, parts relabelled to a higher grade, cloned components, or reject parts. Consequences: failures in vehicles, medical devices and aircraft, recalls, liability and brand damage.

Controls: **buy from OEM or authorised distributors**; require **certificates of conformance** and traceability to the manufacturer; define a **counterfeit-avoidance policy** (SAE AS5553 for avoidance and AS6081 for distributors, and industry standards such as IDEA-STD-1010); inspect (visual and microscope, **X-ray, decapsulation, electrical and functional tests**); sample testing; and have a quarantine process. Price anomalies (a part at far below market or at 10x), long unexplained lead times and anonymous sellers are red flags.

### Example
A buyer needs 5,000 chips at a list price of ₹200 and cannot get them from authorised channels for 20 weeks. A broker offers them at ₹900 each (₹45 lakh). Screening costs: 10% sampling (500 units) at ₹300 per unit = ₹1.5 lakh. Probability of a defective lot without testing = 15%; consequence ₹3 crore in field failure and recall. Expected loss without testing = 0.15 × 3 crore = ₹45 lakh; with testing, assuming it catches 90% of bad lots, expected loss = 0.015 × 3 crore = ₹4.5 lakh plus ₹1.5 lakh testing. Testing saves about ₹39 lakh in expectation, and the **price premium (₹35 lakh)** is itself the cost of the shortage.

### In the news
See news box. Shortage pushes buyers toward grey-market channels; the Nexperia event made brokers' stock valuable overnight.

### Interview angle
> [!question] How it is asked
> "Your production is stopped for a chip and a broker has stock at 5x price. Do you buy?"

> [!tip] Strong answer includes
> - Authorised channels and manufacturer escalation first
> - If broker: vet the broker, test lots, use the highest-testing tier for critical products, and quarantine
> - Quantify the expected cost of counterfeit failure vs premium and stop cost
> - Standards and a documented policy

---
## 12. Rare Earths, Critical Minerals & Electronics Inputs
> 🟠 Tier 2 · _Key points:_ neodymium magnets, gallium, germanium, export controls, recycling, India's position

### Definition
Electronics and EVs depend on **critical minerals**: **rare earths** (neodymium, dysprosium, praseodymium) for permanent magnets in motors, speakers, haptics and hard drives; **gallium and germanium** for power electronics and optics; **tungsten, tantalum, cobalt, lithium, graphite**. China controls roughly 90% of global rare-earth **processing** (Al Jazeera, August 2025) and has used export licensing as policy: it imposed rare-earth export restrictions on 4 April 2025 and eased them for India after talks around 19 August 2025. India's own rare-earth production is under 1% of global output.

Supply-chain responses: **stockpiles and strategic reserves**, **diversified sourcing** (Australia, Africa, the US), **recycling and urban mining** (e-waste as source, see [[135 Reverse Logistics, Remanufacturing & EPR in India]]), **material substitution** (ferrite or induction motors, lower-dysprosium magnets), long-term offtakes and **price-risk** hedges ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]). India's National Critical Mineral Mission (2025) and magnet-manufacturing incentives aim to build capacity, though results will take years.

### Example
A scooter maker uses 0.35 kg of magnet per motor (assumption) and builds 30,000 units a month, so it needs 10.5 tonnes of magnets a month. Suppose supply is cut to 40% (4.2 tonnes a month) from month 1 and stock on hand is one month (10.5 tonnes). Month 1: 14.7 tonnes available, 10.5 used, 4.2 left over. Month 2: 4.2 + 4.2 = 8.4 tonnes, enough for 24,000 units (80%). Month 3: stock exhausted, 4.2 tonnes gives 12,000 units: a **60% shortfall**. With three months of buffer (31.5 tonnes) the same disruption would be absorbed for about 4 months; the buffer costs 31.5 tonnes of working capital but protects the entire output. Bajaj Auto's Chetak output in July 2025 (10,824 units, down about 47% from 20,384 a year earlier) shows what the end of the buffer looks like.

### In the news
See news box. Both automotive and electronics were hit; Nexperia (chips) and rare earths (magnets) show that different materials produce the same failure type.

### Interview angle
> [!question] How it is asked
> "How would you build resilience for a product that depends on Chinese rare-earth magnets?"

> [!tip] Strong answer includes
> - Dependence map by tier, with stock cover and licensing lead time
> - Options: buffer, alternate suppliers, motor redesign, recycling, offtake contracts
> - Quantify the stock needed for a plausible disruption window
> - Government and industry-level actions (reserves, magnet capacity)

---
## 13. Product Lifecycle & Demand Volatility in Electronics
> 🟠 Tier 2 · _Key points:_ short life cycles, NPI ramp, price erosion, memory cycle, inventory write-down

### Definition
Consumer electronics have **12-24 month product lifecycles**, rapid **price erosion** (a component's price may fall 20-50% over its life), launch-day demand spikes, and heavy promotions. Supply planning problems: **new-product introduction (NPI)** ramps with low yield at first; **forecast error** large at the SKU/colour/storage level; the **cost of obsolescence** and **inventory price protection** (distributors reimburse buyers for price drops); **memory and display cycles** that swing prices by multiples. Strategies: **postponement** (configure late: colour, storage, regional packaging), **modular design**, **component commonality**, **shorter lead times via regional hubs**, **make-to-order for configurations** and **cash discipline** (low inventory days). See [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]] and [[118 New-Product Forecasting, Demand Sensing & Demand Shaping]].

### Example
A phone maker holds 8 weeks of component inventory valued at ₹400 crore when the price of memory falls 20% in the quarter; exposure = ₹400 crore × 20% = **₹80 crore** loss in value if uncovered by price protection or hedges. Cutting stock to 4 weeks halves it to ₹40 crore. Demand error: forecast 1.0 million launch units across 12 SKUs; with an SKU-level MAPE of 35% and aggregate error of 8%, the company can postpone final configuration to the last 3 days to use the better aggregate forecast: expected over/under-stock on postponed components falls from about 35% to about 8% of volume.

### In the news
See news box. AI-server demand is a new source of volatility: Business Standard reported in July 2026 that [Foxconn's sales surged 40% on AI-server demand](https://www.business-standard.com/world-news/nvidia-supplier-foxconn-s-sales-surge-40-on-robust-ai-server-demand-126070500386_1.html), the kind of demand shift that competes with consumer devices for scarce packaging and memory capacity.

### Interview angle
> [!question] How it is asked
> "Design a supply chain for a smartphone launch with a 12-month life."

> [!tip] Strong answer includes
> - Phases: pre-launch build, ramp, peak, decline; buffer logic by phase
> - Postponement and commonality; allocation by region and channel
> - Component price risk and price protection; end-of-life run-out plan
> - KPIs: forecast accuracy, inventory days, obsolescence %, launch-day fill rate

---
## 14. ⭐ Advanced: A Resilient Electronics Sourcing Strategy (BOM Risk Scoring)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Rank every BOM line by **risk score** and apply different policies:
- **Exposure** = spend or production impact (stopped output per day).
- **Supply risk** = single-source, long lead time, geopolitical origin, financial health of supplier, past allocation.
- **Substitutability** = existing qualified alternates, cost and time to qualify.

A practical quadrant: **high impact + low substitutability** (e.g. microcontroller on a certified board): buffer plus LTA and second source in qualification; **high impact + high substitutability** (standard discretes): approve alternates, minimal buffer; **low impact + low substitutability**: monitor; **low + high**: commodity. Linking to [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]] for risk-monitoring tools and to [[015 Supply Chain Risk & Resilience]] for the framework.

Quantify with **time-to-recover (TTR)** and **time-to-survive (TTS)** (how long you can operate without the part): risk exists where TTR > TTS. Mitigation spend should rise with $(\text{TTR} - \text{TTS}) \times \text{daily stop cost}$.

### Example
Three parts and a daily stop cost of ₹40 lakh: (a) MCU: TTR 20 weeks, TTS 4 weeks, gap 16 weeks (112 days) → exposure ₹40 lakh × 112 = **₹44.8 crore**; (b) diode: TTR 6 weeks (42 days), TTS 5 weeks (35 days), gap 7 days → ₹2.8 crore; (c) resistor: TTR 3 weeks, TTS 6 weeks, no gap → 0. Priority is clear: the MCU gets an LTA, a second-source qualification and 8 extra weeks of buffer (12 weeks of cover in total; the extra stock is 8 weeks × ₹6 lakh a week of chip purchases = ₹48 lakh, with carrying cost ≈ ₹5.8 lakh a year at 12%), against ₹44.8 crore of potential loss.

### In the news
See news box. Nexperia and rare-earth episodes showed that the part with gap > 0 might be a one-rupee discrete or a magnet, not necessarily the expensive chip.

### Interview angle
> [!question] How it is asked
> "You have 3,000 BOM lines. Where do you spend your resilience budget?"

> [!tip] Strong answer includes
> - Filtering by exposure and risk, not by spend alone
> - TTR vs TTS gap analysis and expected-loss ranking
> - Differentiated policies: LTA, buffer, alternates, redesign, monitoring
> - Cost of buffers vs expected loss and a review cadence
