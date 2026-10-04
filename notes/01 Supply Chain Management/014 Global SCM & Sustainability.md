---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Global SCM & Sustainability"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Global SCM & Sustainability

⬅ [[013 ERP & Enterprise Systems (SAP-Oracle)]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[015 Supply Chain Risk & Resilience]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Green Supply Chain]]
2. [[#2. Circular Economy in SCM]]
3. [[#3. ESG in Supply Chain]]
4. [[#4. Sustainable Procurement]]
5. [[#5. Carbon Footprint Calculation]]
6. [[#6. Near-shoring & Friend-shoring]]
7. [[#7. Trade Regulations & Tariffs]]
8. [[#8. Currency & Geopolitical Risk]]
9. [[#9. Ethical Sourcing]]
10. [[#10. UN SDG Alignment]]
11. [[#11. Scope 3 Emissions]]
12. [[#12. Sustainability KPIs]]
13. [[#13. ⭐ Advanced: CBAM & Carbon Border Adjustments]]
14. [[#14. ⭐ Advanced: Supply Chain Due Diligence & Traceability]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Carbon borders, ESG disclosure and tariff shocks
> **EU CBAM bites Indian steel (Jan–Jun 2026).** The EU fully implemented its Carbon Border Adjustment Mechanism in **January 2026** (covering iron and steel, aluminium, cement, fertilisers, hydrogen and electricity). An ICRIER study reported by Business Standard (26 Jun 2026) projected India's steel exports to the EU could fall **24%**, and noted that India's iron and steel exports to the region had already dropped **13% in the four months to April 2026**. ICRIER also estimated CBAM would cut global steel-sector emissions by only about 1%. ([Business Standard](https://www.business-standard.com/amp/economy/news/india-s-steel-exports-to-eu-may-fall-24-due-to-cbam-says-icrier-study-126062601055_1.html))
>
> **SEBI's BRSR value-chain rules (circular dated 28 Mar 2025).** For the **top 250 listed companies**, value-chain partners to be disclosed are now those individually accounting for **2% or more** of purchases or sales by value (the earlier test was partners covering 75% cumulatively), with the option to limit to 75% cumulative. Value-chain ESG disclosures need limited assurance/assessment from **FY2025-26**, and the term "assurance" was changed to "assessment" to widen the pool of reviewers. ([Vinod Kothari](https://vinodkothari.com/2025/04/brsr-disclosures-for-value-chain-partners-eased-by-sebi/))
>
> **US tariffs on India (2025 to Feb 2026).** As summarised by ClearTax (single source, treat figures with care): a 25% US tariff on Indian goods took effect on **1 Aug 2025**, with an additional 25% from **27 Aug 2025**, bringing it to **50%**; pharmaceuticals, semiconductors, energy and critical minerals were exempt. India's exports to the US were about **$87 bn a year (about 2.5% of GDP)**. A bilateral deal on **2 Feb 2026** reportedly cut the rate to **18%**. ([ClearTax](https://cleartax.in/s/us-tariff-on-india))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Green Supply Chain
> 🟠 Tier 2 · _Tracker hint:_ Carbon footprint reduction, reverse logistics, eco-packaging

### Definition
A **green supply chain** integrates environmental thinking into sourcing, production, distribution, use and end-of-life. Levers:
- **Transport:** mode shift (road to rail or coastal), load consolidation, route optimisation, fuel efficiency, EVs and alternative fuels.
- **Network and warehousing:** fewer empty miles, energy-efficient and solar-powered DCs.
- **Packaging:** right-sizing, recycled or reusable materials, eco-packaging.
- **Production:** energy efficiency, renewable power, waste reduction (see lean).
- **Reverse logistics:** returns, refurbishment, recycling.

Emissions from freight: $E = \text{tonne-km} \times \text{emission factor (kg CO}_2\text{e per tonne-km)}$. Mode factors differ widely: road is the highest per tonne-km among land modes, rail much lower, with waterways lower still (use a published factor set, such as GLEC/GHG Protocol, for real work).

### Example
Illustrative factors (assumed, not official): road 0.07, rail 0.025 kg CO2e per tonne-km. A 100-tonne shipment over 1,000 km = 100,000 tonne-km. Road: 100,000 x 0.07 = 7,000 kg = **7.0 t CO2e**. Rail: 100,000 x 0.025 = 2,500 kg = **2.5 t**. Saving 4.5 t, or **64%**, at the price of slower and less flexible service.

### In the news
See news box. CBAM and BRSR disclosure both push exporters and large listed firms to measure and cut supply-chain emissions, turning green logistics from CSR into a commercial requirement.

### Interview angle
> [!question] How it is asked
> "How would you reduce the carbon footprint of a distribution network without hurting service?"

> [!tip] Strong answer includes
> - Measure first: tonne-km and emissions by mode and lane
> - Levers in order of impact: mode shift, consolidation, network redesign, packaging
> - Cost-service-carbon trade-off with a number
> - Stakeholders: customers and regulators who now ask for emissions data

---

## 2. Circular Economy in SCM
> 🟠 Tier 2 · _Tracker hint:_ Closed-loop supply chains; product as a service; remanufacturing

### Definition
The **circular economy** replaces take-make-dispose with loops that keep products and materials in use. Ellen MacArthur's principles: design out waste and pollution, keep products and materials in use, regenerate natural systems. Loops in order of value retention: **reuse/share → repair/maintain → refurbish/remanufacture → recycle** (recycling last, as it destroys form and embodied energy).

**Closed-loop supply chain** = forward chain plus reverse chain (collection, inspection, sorting, remanufacture, resale). Business models: **product-as-a-service** (the firm keeps ownership and sells outcomes, for example tyres per kilometre or lighting as a service), take-back schemes, remanufacturing, secondary-material markets. Design issues: modularity, standardised parts, durability, and take-back logistics cost. Indian context: Extended Producer Responsibility (EPR) rules for plastic packaging, e-waste and batteries.

### Example
Caterpillar's remanufacturing programme (Cat Reman) returns used components, rebuilds them to specification and resells them with warranty. Illustrative numbers: a new part costs ₹100; a remanufactured one costs ₹60 to produce (core collected, cleaned, rebuilt) and sells at ₹75, a margin of ₹15 (25% on cost). A new part selling at ₹120 earns ₹20 (20% on cost). The remanufactured part gives a higher return on cost, saves raw materials and gives customers a lower price.

### In the news
See news box. EPR obligations and CBAM-type border measures reward producers who keep materials in loops, which cut embedded emissions.

### Interview angle
> [!question] How it is asked
> "How can a durable goods manufacturer make its supply chain circular?"

> [!tip] Strong answer includes
> - Hierarchy of loops (reuse, repair, remanufacture, recycle)
> - Reverse-logistics design: collection, grading, remanufacturing capacity
> - Business models (PaaS, take-back) and economics with a number
> - Barriers: design for disassembly, reverse-flow cost, quality perception, regulation (EPR)

---

## 3. ESG in Supply Chain
> 🟠 Tier 2 · _Tracker hint:_ Environmental, Social, Governance metrics; GRI reporting

### Definition
**ESG** covers **Environmental** (emissions, energy, water, waste, biodiversity), **Social** (labour practices, health and safety, human rights, community, diversity) and **Governance** (ethics, anti-corruption, transparency, board oversight). In supply chains most ESG risk sits **upstream** with suppliers.

Reporting frameworks: **GRI** (impact-based sustainability reporting standards), **SASB/ISSB (IFRS S1/S2)** (investor-focused, climate), **CDP**, **TCFD** (now folded into ISSB), the EU's **CSRD/ESRS**, and in India **SEBI's BRSR** (Business Responsibility and Sustainability Report) with **BRSR Core**, a subset of KPIs on nine ESG attributes that requires assurance, phased by market-cap tier of listed companies. Supply chain ESG programme: map suppliers, risk-rate by country and category, set a code of conduct, audit (SMETA, EcoVadis, SA8000), train, track corrective actions, and tie awards to performance.

### Example
A listed FMCG firm in the top 250 must report value-chain partners that are at least 2% of purchases or sales (see news box). Say it has 6 such suppliers covering 38% of purchases: it collects energy, emissions and labour-practice data from them, gets a limited assessment from a third party and reports year-on-year improvement.

### In the news
See news box. SEBI's March 2025 change cut the vendor count to be reported (from "partners covering 75% cumulatively" to those at or above 2% individually) while keeping an assessment requirement from FY2025-26.

### Interview angle
> [!question] How it is asked
> "How would you integrate ESG into supplier management?"

> [!tip] Strong answer includes
> - E, S, G split and where supply-chain risk concentrates
> - Frameworks: BRSR/BRSR Core, GRI, ISSB, CSRD (and which applies to whom)
> - Programme: mapping, risk rating, code of conduct, audits, corrective action, incentives
> - Data quality: supplier readiness and capability building, especially MSMEs

---

## 4. Sustainable Procurement
> 🟠 Tier 2 · _Tracker hint:_ Supplier ESG audits, fair trade, renewable sourcing

### Definition
Buying goods and services so that social, environmental and economic impacts over the **whole life** are considered, not only price. Tools:
- **Supplier code of conduct** and **ESG questionnaire/rating** (EcoVadis, CDP supply chain programme).
- **On-site audits** (SMETA, SA8000, ISO 14001/45001 certifications) and risk-based sampling.
- **Total cost of ownership** including energy, waste, end-of-life, and an **internal carbon price**.
- **Preferred sourcing:** renewable energy (PPAs, green power), recycled content, certified materials (FSC, Fairtrade, RSPO).
- **Supplier development** (not just exit) for MSMEs; inclusive sourcing (local, women-owned).

Weigh ESG in supplier scorecards (for example price 40, quality 25, delivery 20, ESG 15).

### Example
Internal carbon price ₹5,000 per tonne CO2e (= ₹5 per kg). Supplier A: ₹100 per unit, 0.5 kg CO2e per unit; Supplier B: ₹101, 0.2 kg. Carbon-adjusted cost: A = 100 + 0.5 x 5 = **₹102.5**; B = 101 + 0.2 x 5 = **₹102.0**. B wins once carbon is priced, despite the higher quote.

### In the news
See news box. BRSR's value-chain disclosures and CBAM both make suppliers' emissions a procurement criterion for Indian buyers and exporters.

### Interview angle
> [!question] How it is asked
> "Your lowest-cost supplier fails an ESG audit. What do you do?"

> [!tip] Strong answer includes
> - Severity of the finding (child labour vs documentation gap) and immediate action
> - Corrective action plan with timeline, re-audit and a stop-work trigger for critical breaches
> - TCO view with ESG and carbon-adjusted cost
> - Balance of exit vs development, given supply risk and MSME impact

---

## 5. Carbon Footprint Calculation
> 🟠 Tier 2 · _Tracker hint:_ Scope 1/2/3 emissions; LCA; emission factors

### Definition
The **GHG Protocol** classifies emissions:
- **Scope 1:** direct (fuel burned in own boilers, vehicles, process emissions).
- **Scope 2:** indirect from purchased electricity, steam, heat. Reported **location-based** (grid average) and **market-based** (contractual instruments, green power).
- **Scope 3:** all other indirect emissions across the value chain (see section 11).

Basic calculation:

$$\text{Emissions (kg CO}_2\text{e)} = \text{Activity data} \times \text{Emission factor}$$

Gases are converted to CO2-equivalent using global warming potentials (GWP). **Life Cycle Assessment (LCA)** (ISO 14040/14044) quantifies the impacts of a product from cradle to grave (or cradle to gate) with defined functional unit and system boundary. Sources of factors: DEFRA, IPCC, national grid factors (India's CEA publishes a grid emission factor), ecoinvent.

### Example
Diesel burned: 10,000 litres x about 2.68 kg CO2 per litre = **26.8 t** (Scope 1). Electricity: 1,000,000 kWh at an assumed grid factor of 0.7 kg CO2 per kWh (illustrative; use the current CEA figure) = **700 t** (Scope 2 location-based). Total Scope 1 + 2 = 726.8 t. If the factory buys 400,000 kWh of green power, market-based Scope 2 = 600,000 x 0.7 = 420 t.

### In the news
See news box. CBAM requires exporters to calculate embedded emissions of goods using prescribed methods, making these calculations a trade-compliance skill.

### Interview angle
> [!question] How it is asked
> "How would you estimate the carbon footprint of a product or a company?"

> [!tip] Strong answer includes
> - Scope 1/2/3 definitions and boundaries
> - Activity data x emission factor with a worked example
> - Location vs market-based Scope 2, LCA basics
> - Data quality hierarchy: supplier-specific over spend-based estimates

---

## 6. Near-shoring & Friend-shoring
> 🟠 Tier 2 · _Tracker hint:_ Supply chain resilience post-COVID; TCO recalculation

### Definition
- **Offshoring:** moving production far away, mainly for low cost.
- **Near-shoring:** moving closer to the demand market (for example Mexico for the US, Eastern Europe for Western Europe).
- **Friend-shoring:** relocating to politically aligned countries to reduce geopolitical risk.
- **China+1:** adding a second country base beside China.
- **Reshoring/on-shoring:** back to the home country.

Drivers: COVID disruptions, tariffs and export controls, geopolitical risk, logistics volatility, customer demand for short lead times. Decision tool is **total cost of ownership (TCO)** or **total landed cost**: price + freight + duties + inventory carrying (pipeline and safety stock) + quality cost + risk/disruption cost + compliance. Non-cost factors: supplier ecosystem, skills, infrastructure, ease of doing business, incentives (India's PLI schemes).

### Example
Offshore: price 80 + freight 6 + duty 4 + pipeline inventory (60 days x 80 x 20% / 365 = 2.63) + risk allowance 3 = **95.63**. Near-shore: price 90 + freight 2 + duty 0 + inventory (15 days x 90 x 20% / 365 = 0.74) + risk allowance 1 = **93.74**. The nearer source, with a 12.5% higher price, wins on total landed cost by about 2%.

### In the news
See news box. US tariffs of up to 50% on Indian goods in 2025 (cut to a reported 18% in Feb 2026) show how fast duty assumptions move, and why TCO models must be scenario-based. In contrast, India has also benefited from China+1 flows (see the Supply Chain Introduction note's news box).

### Interview angle
> [!question] How it is asked
> "A US apparel brand is considering moving 30% of its sourcing out of China. Where and how would you advise?"

> [!tip] Strong answer includes
> - TCO or landed-cost model across 2–3 countries, with tariff scenarios
> - Non-cost factors: capacity, skills, infrastructure, compliance and political risk
> - Phased approach: dual sourcing, pilot, not a big-bang shift
> - Mention for India: ecosystem, PLI, FTA access, but also constraints (logistics, scale)

---

## 7. Trade Regulations & Tariffs
> 🟠 Tier 2 · _Tracker hint:_ Import duties, anti-dumping, FTAs, rules of origin

### Definition
- **Customs duty** in India: Basic Customs Duty (BCD), Social Welfare Surcharge (SWS, 10% of BCD, where applicable), and **IGST** on imports (on the value including duty). Classification uses **HS codes**; valuation on **CIF**.
- **Anti-dumping duty:** imposed to offset dumped imports; India's DGTR investigates and recommends, and the Finance Ministry notifies. **Countervailing duty** for subsidised imports; **safeguard duty** for import surges.
- **Non-tariff measures:** quotas, licences, BIS standards (QCOs), sanitary rules.
- **FTAs/CEPAs:** preferential duty if the goods satisfy **rules of origin (RoO)**: wholly obtained, **change in tariff heading (CTH)**, or **regional value content (RVC)** thresholds (for example 35% in some agreements), proved via a certificate of origin.
- **Incoterms** decide who pays freight, duty and risk (for example FOB, CIF, DDP).
- **Duty drawback and schemes:** Advance Authorisation, EPCG, RoDTEP help exporters.

### Example
CIF value ₹100. BCD 10% = 10. SWS 10% of BCD = 1. Assessable base for IGST = 100 + 10 + 1 = 111. IGST 18% = **19.98**. Total taxes = 10 + 1 + 19.98 = **₹30.98**, so landed cost before freight within India = ₹130.98 (IGST is typically creditable). An FTA reducing BCD to 0 would cut taxes by the BCD and SWS (and the IGST on them): total = 100 x 18% = ₹18.

### In the news
See news box. Tariff levels on Indian exports swung from 25% to 50% and then to 18% within a year (ClearTax summary); exporters needed scenario pricing and flexible origin options.

### Interview angle
> [!question] How it is asked
> "How would a tariff increase of 25% affect an exporter and how should it respond?"

> [!tip] Strong answer includes
> - Who bears the tariff (price elasticity and contract terms: DDP vs FOB)
> - Calculation of landed-cost effect and margin impact
> - Responses: re-routing, assembly in a lower-tariff country (watch rules of origin), FTA use, cost-sharing, price increases
> - Compliance risk: misclassification, origin fraud (transshipment)

---

## 8. Currency & Geopolitical Risk
> 🟠 Tier 2 · _Tracker hint:_ Hedging, dual-sourcing, inventory buffers

### Definition
**Currency (FX) risk:** exchange-rate moves change the home-currency value of cash flows. Types: **transaction** (receivables/payables), **translation** (consolidation) and **economic** exposure (competitiveness). Hedges: **forward contracts** (lock a rate), options (protection with premium), natural hedges (match currency of revenue and cost, local sourcing), invoicing in rupees, and netting. RBI rules govern authorised-dealer forward cover for Indian firms.

**Geopolitical risk:** wars, sanctions, export controls, chokepoint closures, tariffs. Responses: **dual/multi-sourcing**, regional diversification, **buffer inventory** at critical nodes, flexible contracts, route alternatives, supply-risk mapping to tier-N, scenario planning and business-continuity plans, insurance. Each has a cost, so risk-rank by probability, impact and substitutability (Kraljic matrix in the procurement notes).

### Example
An Indian importer owes $1 million in 3 months. Spot ₹85, 3-month forward ₹86. Hedged cost: ₹8.6 crore, fixed. If unhedged and spot becomes ₹88, cost = ₹8.8 crore, **₹20 lakh more** than the hedge; if spot is ₹84, cost = ₹8.4 crore, **₹20 lakh less**. The hedge removes the uncertainty at a known cost (the 1-rupee forward premium, ₹10 lakh versus today's spot).

### In the news
See news box. Tariff changes, such as the 25% to 50% to 18% path for India-US goods, are a geopolitical risk that works like an FX move on landed cost; both are managed by scenarios and flexible sourcing.

### Interview angle
> [!question] How it is asked
> "How should a company protect itself against rupee depreciation and a supplier-country shock?"

> [!tip] Strong answer includes
> - Identify exposure (net, by currency and horizon) before hedging
> - Financial hedges (forwards, options) and natural hedges
> - Operational hedges: dual sourcing, buffer stock, regional plants
> - Costs of each and a risk-ranking to decide where to spend

---

## 9. Ethical Sourcing
> 🟠 Tier 2 · _Tracker hint:_ Child labor, conflict minerals, SA8000 standard

### Definition
**Ethical sourcing** ensures that the people and places behind products are treated fairly: no child or forced labour, safe conditions, fair wages and hours, freedom of association, no discrimination, responsible mineral and raw-material sourcing.

- **Standards and codes:** ILO core conventions, **SA8000** (certifiable social accountability standard), SMETA/Sedex audits, BSCI, Fair Trade, RBA code (electronics).
- **Conflict minerals:** tin, tantalum, tungsten and gold (3TG) from conflict-affected areas; US Dodd-Frank Section 1502 requires reporting for listed US firms; OECD due-diligence guidance. Cobalt in batteries is a related concern.
- **Child labour** in India is regulated by the Child and Adolescent Labour (Prohibition and Regulation) Act, 1986 (as amended in 2016).
- Tools: supplier mapping and traceability, unannounced audits, worker grievance channels, remediation (not just termination), and responsible exit.

### Example
An audit of a garment supplier finds underage workers (apparent age below 14) in a sub-contracted unit. Strong response: immediately remove the children from work in a safe way with support (schooling, income replacement for the family) rather than just dismissing them, require disclosure of sub-contractors, re-audit, and tie future orders to remediation.

### In the news
See news box. Disclosure rules such as BRSR's value-chain assessment mean social incidents at suppliers now have to be reported and assessed.

### Interview angle
> [!question] How it is asked
> "You discover forced or child labour at a tier-2 supplier. What do you do?"

> [!tip] Strong answer includes
> - Stop and protect: immediate action for affected workers, remediation not mere termination
> - Investigate scope and root causes (sub-contracting, recruitment fees, pressure on price and lead time)
> - Standards (SA8000, ILO), audits, traceability
> - Our own buying practices: unrealistic prices and deadlines are part of the cause

---

## 10. UN SDG Alignment
> 🟠 Tier 2 · _Tracker hint:_ Goals 12, 13, 17 in SCM context; corporate reporting

### Definition
The 17 **UN Sustainable Development Goals (2015–2030)** are a shared framework many firms use for sustainability strategy and reporting (GRI and BRSR both reference SDGs). Supply chain relevance:

| SDG | Supply chain link |
|---|---|
| **12 Responsible consumption and production** | Sustainable sourcing, waste reduction, circularity, food loss (target 12.3: halve per-capita food waste at retail and consumer level and reduce food losses along production and supply chains by 2030) |
| **13 Climate action** | Scope 1-3 reduction, green logistics, renewable energy |
| **17 Partnerships for the goals** | Supplier collaboration, industry initiatives, finance and capacity building for MSMEs |
| 8 Decent work | Labour standards, ethical sourcing |
| 9 Industry, innovation, infrastructure | Resilient infrastructure, technology |
| 6, 7 Water, energy | Water stewardship, clean energy |

Practice: map material topics to SDGs, set targets with KPIs, report progress; avoid **SDG-washing** (claiming alignment without measurable contribution).

### Example
A food company maps its cold-chain upgrade to SDG 12.3 (target: cut post-harvest loss from 12% to 8% of volume for supplied produce) and SDG 13 (lower emissions per tonne delivered with efficient refrigeration), with supplier training under SDG 17. Volume: 100,000 t supplied; loss reduction of 4 points saves **4,000 t** of produce.

### In the news
See news box. SEBI's BRSR format itself links disclosures to national guidelines on responsible business; CBAM relates to SDG 13.

### Interview angle
> [!question] How it is asked
> "Which SDGs are most relevant to supply chains and how would you operationalise them?"

> [!tip] Strong answer includes
> - SDG 12, 13, 17 plus 8 and 9 with a concrete link each
> - Translate to measurable KPIs and targets
> - Embed in procurement criteria and supplier programmes
> - Avoid vague claims; use verified metrics and reporting

---

## 11. Scope 3 Emissions
> 🟠 Tier 2 · _Tracker hint:_ Supplier emissions, product use, end-of-life; disclosure requirements

### Definition
**Scope 3** = all indirect emissions in the value chain not in Scope 2. GHG Protocol defines **15 categories**.

**Upstream:** 1 Purchased goods and services; 2 Capital goods; 3 Fuel- and energy-related activities; 4 Upstream transportation and distribution; 5 Waste generated in operations; 6 Business travel; 7 Employee commuting; 8 Upstream leased assets.
**Downstream:** 9 Downstream transportation; 10 Processing of sold products; 11 **Use of sold products**; 12 **End-of-life treatment**; 13 Downstream leased assets; 14 Franchises; 15 Investments.

For many companies Scope 3 is the **largest share** of the footprint, yet hardest to measure. Methods (in rising accuracy): **spend-based** (spend x EEIO factor), **average-data** (physical quantity x average factor), **supplier-specific** (primary supplier data). Hotspot analysis first, then collect data where it matters. Reductions rely on supplier engagement, design changes and customers' behaviour.

### Example
Spend-based Category 1: ₹10 crore of purchased steel parts x an assumed factor of 0.4 kg CO2e per ₹100 spent: ₹10 crore = 10^8 rupees; 10^8/100 x 0.4 = 400,000 kg = **400 t CO2e**. Switching to supplier-specific data (for example, a supplier using scrap-based EAF steel with lower intensity) may lower the figure and reward the better supplier.

### In the news
See news box. India's BRSR value-chain requirements push Scope 3-type data collection; CBAM forces embedded-emissions data for specific goods. (Check current rules in other jurisdictions such as the EU and California before quoting dates.)

### Interview angle
> [!question] How it is asked
> "Why is Scope 3 hard, and how would you start measuring it for a consumer goods company?"

> [!tip] Strong answer includes
> - The 15 categories grouped upstream and downstream, naming the big ones (1, 4, 11, 12)
> - Methods hierarchy: spend-based, average-data, supplier-specific
> - Hotspot-first approach and supplier engagement
> - Disclosure context and assurance expectations

---

## 12. Sustainability KPIs
> 🟠 Tier 2 · _Tracker hint:_ Carbon intensity, water usage, waste diversion%, renewable energy%

### Definition
| KPI | Formula | Note |
|---|---|---|
| **Carbon intensity** | tCO2e / ₹ crore revenue (or per tonne of product) | Intensity can fall while absolute emissions rise |
| **Absolute emissions** | Total tCO2e by scope | Needed for science-based targets |
| **Water intensity** | kL water withdrawn / tonne product (or per ₹ crore) | Add water recycled % and stress-area use |
| **Waste diversion %** | Waste diverted from landfill / total waste x 100 | Reuse, recycle, recover |
| **Renewable energy %** | Renewable kWh / total kWh x 100 | Separate on-site and purchased |
| **Energy intensity** | GJ per tonne or ₹ crore | BRSR Core attribute |
| **Supplier ESG coverage %** | Spend with assessed suppliers / total spend | |
| **LTIFR** | Lost-time injuries x 1,000,000 / hours worked | Safety |

Set a baseline year, a boundary, targets (for example aligned to SBTi), and review with assurance. Beware metric gaming: link intensity and absolute figures together.

### Example
Revenue ₹500 crore, emissions 12,500 tCO2e: carbon intensity = 12,500/500 = **25 tCO2e per ₹ crore**. Waste: 800 t generated, 560 t recycled or reused: diversion = 560/800 = **70%**. Energy: 8 million kWh used, 2 million from renewables: **25%**. Water: 120,000 kL for 40,000 t product = **3 kL/t**.

### In the news
See news box. BRSR Core's standardised, assurable indicators are meant to make such KPIs comparable across companies and across the value chain.

### Interview angle
> [!question] How it is asked
> "Which sustainability KPIs would you put on a supply chain scorecard?"

> [!tip] Strong answer includes
> - A short, balanced set across E, S and G (carbon, water, waste, renewable %, safety, supplier ESG coverage)
> - Intensity and absolute measures, with baselines and targets
> - Data owners, assurance and reporting cadence
> - Link to cost and risk (energy cost, CBAM exposure), not only compliance

---

## 13. ⭐ Advanced: CBAM & Carbon Border Adjustments
> ⭐ Advanced · _Added beyond the tracker_

### Definition
The EU's **Carbon Border Adjustment Mechanism** puts a carbon price on imports of selected carbon-intensive goods (iron and steel, aluminium, cement, fertilisers, electricity, hydrogen) so that they face a cost comparable to EU producers under the **EU ETS** and to prevent **carbon leakage**.

Phases: a **transitional phase (Oct 2023–Dec 2025)** with reporting only; the **definitive phase from January 2026**, when EU importers must be authorised declarants and surrender **CBAM certificates** priced off the EU ETS allowance price, for embedded emissions, with the obligation phased in as EU free allocation is phased out.

Simplified formula:

$$\text{CBAM cost} \approx \text{Embedded emissions (tCO}_2\text{e per t)} \times (\text{EU ETS price} - \text{carbon price paid in origin}) \times \text{tonnes}$$

(ignoring the free-allocation adjustment). Exporters need **verified embedded-emissions data** (direct, and indirect for some goods). Responses: decarbonise (scrap-based EAF, green power, hydrogen DRI), supplier data systems, shift trade flows, lobby via FTA, domestic carbon market (India's Carbon Credit Trading Scheme).

### Example
Illustrative: 1 t of steel with 2.2 tCO2e embedded, EU ETS price €70/t, carbon price paid in India = 0. Gross CBAM cost = 2.2 x 70 = **€154 per tonne**, which must be compared with the price of steel and the free-allocation phase-in. If a supplier cuts intensity to 1.6 tCO2e/t: 1.6 x 70 = €112, saving **€42 per tonne (27%)**.

### In the news
See news box. ICRIER projected a 24% fall in India's steel exports to the EU, and the sector's exports had already fallen 13% in the four months to April 2026.

### Interview angle
> [!question] How it is asked
> "How should an Indian steel exporter respond to CBAM?"

> [!tip] Strong answer includes
> - What CBAM is, which sectors, and the 2026 definitive phase
> - Cost calculation with embedded emissions and ETS price, noting the free-allocation phase-in
> - Operational levers: decarbonisation, data systems, market diversification
> - Strategic: customer pass-through, FTA and policy engagement

---

## 14. ⭐ Advanced: Supply Chain Due Diligence & Traceability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Regulators increasingly require firms to **know and prove** what happens in their supply chains: the US **Uyghur Forced Labor Prevention Act (UFLPA)** (in force from June 2022) presumes goods linked to Xinjiang are made with forced labour unless the importer proves otherwise; the **EU CSDDD** (adopted in 2024; scope and timing have been under revision, so check the latest position) obliges large firms to identify and mitigate human-rights and environmental harm in their chains; other examples include German and French supply-chain due-diligence laws.

Capability build: **multi-tier mapping** (tier-1 to raw material), risk-scoring by country and commodity, **traceability** (batch or lot IDs, blockchain/serialisation, mass-balance vs segregated chains), supplier contracts with audit rights, grievance mechanisms, and evidence files for customs and auditors. Key measures: % of spend mapped to tier-2/3, % of high-risk suppliers audited, time to trace a lot (hours).

### Example
A firm can name 120 tier-1 suppliers but only 15 of their sub-suppliers. A customs authority detains a shipment and requires proof of origin of cotton. Time to prove origin: 6 weeks (unmapped), with demurrage of, say, ₹40,000 per day: 42 days x ₹40,000 = **₹16.8 lakh**. A traceability system that retrieves lot-level records in 2 days would reduce this to ₹0.8 lakh.

### In the news
See news box. SEBI's BRSR value-chain disclosure and CBAM's embedded-emissions data both reward firms with tier-level traceability.

### Interview angle
> [!question] How it is asked
> "How would you build visibility beyond tier-1 suppliers?"

> [!tip] Strong answer includes
> - Start with a risk-based approach: highest-risk commodities and countries first
> - Mapping methods: supplier questionnaires, bills of material, data providers, serialisation
> - Contract levers: audit rights, flow-down clauses, penalties and incentives
> - KPIs: % spend mapped, audit coverage, time-to-trace; and the legal context (UFLPA, CSDDD, BRSR)

---
## 🔗 Go deeper: expansion notes
- [[135 Reverse Logistics, Remanufacturing & EPR in India|Reverse Logistics, Remanufacturing & EPR in India]]
- [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP|India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]
- [[140 Packaging, Unitisation & Load Optimisation|Packaging, Unitisation & Load Optimisation]]
