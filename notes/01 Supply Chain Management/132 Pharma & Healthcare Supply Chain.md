---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Pharma & Healthcare Supply Chain"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Pharma & Healthcare Supply Chain

⬅ [[131 Automotive Supply Chain - JIT, Tiers & EVs]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[133 Food, Agri & Perishables Supply Chain - India]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Pharma Value Chain: API to Patient]]
2. [[#2. GMP, GDP & the Regulatory Architecture]]
3. [[#3. Cold Chain (2-8°C) Design]]
4. [[#4. Temperature Excursions, MKT & Lane Qualification]]
5. [[#5. Serialisation & Track-and-Trace (DSCSA, EU, India QR)]]
6. [[#6. Recall Management]]
7. [[#7. FEFO, Expiry & Short-Dated Stock]]
8. [[#8. Drug Pricing: NPPA, DPCO & Trade Margins]]
9. [[#9. Generics, API Dependence on China & India's Response]]
10. [[#10. Vaccine Supply Chain: UIP, Cold-Chain Network & U-WIN]]
11. [[#11. Hospital Inventory, Implants & Consignment]]
12. [[#12. Jan Aushadhi, Public Procurement & Generic Access]]
13. [[#13. Regulatory Risk, Counterfeits & Compliance Playbook]]
14. [[#14. ⭐ Advanced: Drug Shortage Risk & Resilience Scoring]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): a metal-price spike and a data rule show how fragile and regulated the medicine chain is
> **Platinum spike triggers a 50% price hike on cancer drugs (June 2026).** NPPA, using the extraordinary powers in Para 19 of the Drugs (Prices Control) Order, allowed cisplatin 1 mg/ml injection to rise from ₹7.26 to ₹10.89 per ml and carboplatin 10 mg/ml from ₹60.49 to ₹90.74 per ml (+50% each), plus a 50% rise for anti-tetanus immunoglobulins and 20.6% for some vaccines (BCG, measles-rubella, measles). The cause was an "almost 250 per cent rise in platinum prices" that disrupted production. ([Business Standard, 12 June 2026](https://www.business-standard.com/industry/news/govt-allows-50-price-hike-for-key-cancer-drugs-amid-supply-concerns-126061201253_1.html))
>
> **NPPA wants quarterly supply data (June 2026).** Manufacturers of scheduled formulations (928 medicines whose ingredients are in the First Schedule of DPCO 2013) must file Form 3 production and sales returns through IPDMS 2.0 each quarter and clear pending quarters at once; non-filing can attract action under DPCO and the Essential Commodities Act, 1955. The stated aim is better shortage monitoring. ([Business Standard, 24 June 2026](https://www.business-standard.com/industry/news/nppa-asks-drugmakers-to-submit-quarterly-data-on-essential-medicines-126062401120_1.html))
>
> **Annual price-cap indexation (March 2026).** NPPA allowed a 0.64% increase in MRP of scheduled essential drugs in line with the wholesale price index. ([Business Standard, 25 March 2026](https://www.business-standard.com/industry/news/nppa-allows-0-64-percent-hike-in-essential-drug-prices-126032501290_1.html))
>
> **PLI for pharmaceuticals.** The pharma PLI runs 2020-21 to 2028-29 with about ₹15,000 crore (US$2 billion) of incentives, aimed at cutting import dependence; as of 2016-17 China supplied about 66% of India's API raw-material imports by volume. ([Wikipedia, Pharmaceutical industry in India](https://en.wikipedia.org/wiki/Pharmaceutical_industry_in_India); the 66% figure is dated, so treat it as indicative)
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Pharma Value Chain: API to Patient
> 🟠 Tier 2 · _Key points:_ API, formulation, CFA, stockist, retailer, hospital, margins

### Definition
The medicine chain has five links:
1. **Intermediates and API** (active pharmaceutical ingredient): chemical or biological synthesis; long lead time (months), high regulatory burden, concentrated in China and India.
2. **Formulation** (tablets, injectables, syrups): API + excipients + packaging in a GMP plant; batch-based production with a batch number, manufacturing and expiry dates.
3. **Primary distribution**: manufacturer → **C&F agent (CFA)** or depot → **super-stockist** → **stockist/distributor** (state wise licensed).
4. **Secondary distribution**: stockist → chemist/retail pharmacy or **hospital**/institutional buyer; **government tenders** buy directly.
5. **Dispensing**: pharmacy, hospital, Jan Aushadhi Kendra, e-pharmacy.

India is the third-largest producer of medicines by volume (about 20% of global generic demand, nearly half of US generic prescriptions by volume per Wikipedia's summary). Trade margins are regulated indirectly: for price-controlled drugs the retailer margin is fixed (16% of price to retailer), and wholesaler margin is typically about 8-10% (industry practice).

### Example
A strip of tablets sold at an MRP of ₹100 (excluding GST, illustrative): retailer margin 20% on PTR means PTR = 100/1.20 = ₹83.33; if stockist margin is 10% of the price to stockist (PTS), PTS = 83.33/1.10 = ₹75.76. If the company's cost of goods is ₹18 and field-force, marketing and trade promotion cost another ₹30, then 75.76 − 18 − 30 = ₹27.76 (about 37% of PTS) is left for overheads, R&D and profit. Distribution takes about 24% of MRP, which is why companies look for leaner channels (direct-to-retailer, e-B2B ordering) and why chemist associations resist deep discounting.

### In the news
See news box. The platinum episode started at the very first link (a raw material), but it was visible only at the last (a shortage of chemotherapy at hospitals).

### Interview angle
> [!question] How it is asked
> "Draw the Indian pharma supply chain and tell me where the biggest risks and margins sit."

> [!tip] Strong answer includes
> - The five links with the Indian terms (CFA, super-stockist, retailer, tender)
> - Margin waterfall from MRP to company realisation
> - Risk map: API concentration, cold-chain breaks, expiry, regulatory price cuts
> - Link to channel design ([[009 Logistics & Distribution]], [[130 FMCG & Retail Distribution - India Route-to-Market]])

---
## 2. GMP, GDP & the Regulatory Architecture
> 🟠 Tier 2 · _Key points:_ CDSCO, state licensing, Schedule M, WHO-GMP, GDP, USFDA

### Definition
**GMP** (good manufacturing practice) governs how a drug is made: facility design, validated processes, documentation, change control, deviation and CAPA, quality-control release by batch. **GDP** (good distribution practice) governs storage and transport: licensed premises, temperature control, traceability, segregation of rejected and expired goods, vehicle qualification, complaint and recall handling, and anti-counterfeit controls. **GxP** adds good laboratory, clinical and pharmacy practice.

India's regime: the **Drugs and Cosmetics Act, 1940** and Rules, with central regulator **CDSCO** (approvals, imports, standards) and **state licensing authorities** (manufacturing and sale licences). **Schedule M** sets GMP rules; a revised Schedule M, aligned with WHO-GMP, was notified in late 2023, with larger firms given a shorter deadline and MSME manufacturers a later one (check the current extension status). Export manufacturers also face inspections by the US FDA, EU, MHRA and WHO prequalification; an FDA warning letter or import alert at a plant can stop US shipments from it.

Principles that matter for operations: **batch traceability**, **quality agreements** with CMOs and 3PLs, **data integrity** (ALCOA+: attributable, legible, contemporaneous, original, accurate), and **qualified person / responsible person** release. This overlaps with [[011 Quality Management (TQM)]] and [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]].

### Example
A distributor's GDP audit finds a pallet of a 2-8°C product in a 25°C dispatch bay for 40 minutes with no excursion record. Correct reaction: quarantine the stock, retrieve data-logger or door-open data, compare against stability data for allowable excursions (see section 4), decide release or reject by quality head (QA), open a deviation, root cause (no cold-staging area), and CAPA (dedicated 2-8°C dock, alarm). Product is not "fine unless proven bad": it is **held until proven fit**.

### In the news
See news box. NPPA's quarterly data call is a regulatory move on availability; revised Schedule M and QR/serialisation rules are quality-side moves, and both raise compliance cost for smaller firms.

### Interview angle
> [!question] How it is asked
> "What is the difference between GMP and GDP? Who is responsible for a quality failure in distribution?"

> [!tip] Strong answer includes
> - GMP = making, GDP = storing and moving; both under quality agreements
> - Indian regulators (CDSCO and state licensing) and export regulators (US FDA, EU)
> - Concepts: deviation, CAPA, batch release, data integrity
> - Responsibility: marketing-authorisation holder is accountable; 3PL is contractually responsible for the activities it performs

---
## 3. Cold Chain (2-8°C) Design
> 🟠 Tier 2 · _Key points:_ 2-8°C, CRT, frozen, active vs passive, last mile, validation

### Definition
Temperature classes used in pharma: **frozen** (−25 to −10°C or colder; some mRNA vaccines −70°C), **refrigerated 2-8°C** (most vaccines, insulin, biologics, many injectables), **controlled room temperature (CRT)** 15-25°C (many oral solids; labelled "store below 25°C" or "30°C" in warm climates), and **ambient**. Biologics are stability-sensitive: some vaccines are damaged by **freezing** as well as by heat, so the cold chain has a lower limit too.

Design elements:
- **Storage**: validated cold rooms and pharma refrigerators with redundant compressors, backup generator, calibrated sensors and mapping of hot/cold spots.
- **Transport**: **active** (reefer vans with controlled units), **passive** (insulated boxes with gel packs or phase-change material, rated for 24-120 hours), or hybrid.
- **Monitoring**: data loggers or IoT sensors with alarms, calibrated annually; dashboards for excursion events.
- **Handoffs**: the most risky points are airport tarmac, customs, cross-docks and last-mile delivery; a **time-out-of-refrigeration (TOR)** budget is allocated per hand-off.

Cold chain adds cost: cold-chain logistics is commonly cited as costing a multiple of ambient (often quoted as roughly 2-4 times), and packaging can be a large part of it. This is why firms segment: only products that need 2-8°C go that way.

### Example
A biologic is flown from Hyderabad to Guwahati (door to door 36 hours planned). A passive shipper is rated for 96 hours at the qualified summer profile. Margin of safety = 96/(36 × 1.5 delay factor) = 96/54 = **1.78**, comfortable. If the same shipper is used for a lane with 72-hour expected duration and 1.2 delay factor, margin = 96/86.4 = **1.11**: acceptable only with a tracking alert and a recovery plan; many companies require ≥1.25.

### In the news
See news box. Many of the vaccines and immunoglobulins in the NPPA price action are cold-chain products: price caps, shortages and temperature control interact.

### Interview angle
> [!question] How it is asked
> "How would you design cold chain logistics for a biologic launch across India?"

> [!tip] Strong answer includes
> - Segmentation by temperature class and by lane
> - Choice of active/passive packaging and rated duration vs lane transit
> - Monitoring, alarms and TOR budget; backup power and redundancy
> - Cost-to-serve trade-offs and where to place regional depots ([[113 Network Design & Facility Location Modelling]])

---
## 4. Temperature Excursions, MKT & Lane Qualification
> 🟠 Tier 2 · _Key points:_ excursion, mean kinetic temperature, stability data, lane qualification, deviation

### Definition
An **excursion** is any time the product leaves its labelled temperature range. It is not automatically a reject: stability data from the manufacturer may support a limited time outside (for example, a defined number of hours at up to 25°C). Decision tools:
- **Mean kinetic temperature (MKT)**: the single isothermal temperature that would cause the same degradation as the actual varying profile. It weights hot peaks more than the arithmetic mean because degradation is exponential in temperature (Arrhenius):

$$MKT = \frac{\Delta H/R}{-\ln\left(\frac{1}{n}\sum_{i=1}^{n} e^{-\Delta H/(R\,T_i)}\right)}$$

with temperatures $T_i$ in kelvin and the common default $\Delta H/R \approx 10{,}000$ K ($\Delta H \approx 83.14$ kJ/mol).
- **Lane qualification**: before using a route for a product, run **operational qualification** (the packaging against design summer/winter profiles in a chamber) and **performance qualification** (real shipments with loggers over several seasons) to prove that the lane stays within limits, including delays at hubs.

### Example
A hypothetical vaccine shipment logged these 12 two-hourly temperatures in °C: 5, 5, 6, 7, 12, 18, 25, 31, 31, 24, 8, 5. Arithmetic mean = **14.75°C**; computing the MKT with $\Delta H/R = 10{,}000$ K gives **20.3°C**, noticeably higher because of the 31°C peaks. Any 2-8°C label is already violated by readings 5-10, so this lot would be quarantined and the manufacturer's stability team asked for a disposition. The MKT is useful for CRT products (to judge long storage with swings), but for strict 2-8°C biologics it is **not** a pass signal; the excursion budget from stability data governs.

### In the news
See news box. When drugs are in short supply, as with the chemotherapy and vaccine cases, the pressure to release marginal stock rises: a documented decision framework prevents ad hoc choices.

### Interview angle
> [!question] How it is asked
> "A shipment of insulin shows 4 hours at 12°C. What do you do?"

> [!tip] Strong answer includes
> - Quarantine first, then decide using manufacturer stability data and logger data, not intuition
> - MKT and why it weights peaks; its limits for biologics
> - Root cause (lane, packaging, hand-off) and CAPA
> - Lane qualification across seasons as the preventive measure

---
## 5. Serialisation & Track-and-Trace (DSCSA, EU, India QR)
> 🟠 Tier 2 · _Key points:_ GTIN, serial number, aggregation, DSCSA, India QR code on APIs and top-300 brands

### Definition
**Serialisation** gives every saleable pack a unique identity (a 2D barcode carrying **GTIN, serial number, lot, expiry**). **Aggregation** links each item to its case and pallet in a parent-child hierarchy, so one scan of a pallet reveals the contents. **Track-and-trace** records each ownership change and lets regulators and trading partners verify a pack. Purposes: fight counterfeits, enable precise recalls, and detect diversion.

Regimes:
- **US DSCSA** (enacted 27 November 2013): requires an interoperable electronic system to identify and trace prescription drugs at package level; the final stage was due 27 November 2023, then the FDA gave staged enforcement discretion and exemptions into 2024-26 (check current dates for each trade-partner type, as dispensers got longer).
- **EU FMD** (since 2019): verification at dispensing against a central repository (EMVS).
- **India**: amendments to the Drugs Rules brought **QR/barcode requirements** for APIs and for the Schedule H2 list of top-300 drug brands by turnover, with compliance dates extended more than once; the intent is a traceable chain from API to pack and later to a central database. Check the current status of each phase before quoting a date in an interview.

Operational burden: printing and vision-checking on packaging lines, serial-number management, EPCIS data exchange with partners, and handling returns and rework (decommissioning and re-commissioning serial numbers).

### Example
One packing line runs at 300 packs per minute for 8 hours: 300 × 60 × 8 = **144,000 packs** per shift each needing a unique serial, printed, camera-verified and aggregated into cases (say 100 packs per case) → 1,440 case records and, for 40 cases per pallet, 36 pallet records. A 99.5% first-pass vision-read rate still means 720 rejected packs per shift to be re-printed or scrapped, so ink, camera quality and line speed are tuned together.

### In the news
See news box. NPPA's push to see quarterly production and sales data is the price-and-availability side of the same trend: regulators want pack-level and batch-level visibility.

### Interview angle
> [!question] How it is asked
> "What is serialisation and what operational changes does it require in a pharma plant and distribution network?"

> [!tip] Strong answer includes
> - Definition (GTIN, serial, lot, expiry, aggregation) and objectives (counterfeit, recall, diversion)
> - Regimes (DSCSA, EU FMD, India QR), with an honest note on changing deadlines
> - Operational impact: line speed, rework, EPCIS, master data ([[175 Data Quality, Master Data & Data Governance]])
> - Benefits beyond compliance: faster recalls, returns validation, demand visibility

---
## 6. Recall Management
> 🟠 Tier 2 · _Key points:_ Class I/II/III, batch trace, quarantine, depth of recall, mock recall

### Definition
A **recall** removes a defective or unsafe batch from the market. Classes (US convention): **Class I** (reasonable probability of serious harm or death), **Class II** (temporary or reversible harm), **Class III** (unlikely to cause harm). Depth: to wholesaler, retailer or consumer level.

Process: detect (complaint, test failure, regulator alert) → assess health hazard → decide class and depth → notify authorities and trade → **quarantine** stock → trace distribution by batch → retrieve and **reconcile** quantity → disposal or rework → root cause and CAPA → effectiveness check. The test of readiness is a **mock recall**: can the company locate 100% of a batch within hours? Link to inventory records by batch ([[116 Inventory Valuation, Cycle Counting & Inventory Governance]]) and to SAP batch traceability ([[191 SAP MM Advanced - Inventory, Batches & Special Stocks]]).

India context: state regulators draw samples and declare "Not of Standard Quality" (NSQ) or spurious; companies then recall batches. Contaminated-syrup episodes in 2022-25 (Gambia, Uzbekistan and India) made batch traceability, raw-material testing (especially excipients such as glycerin and propylene glycol) and export testing a regulatory priority.

### Example
Batch of 400,000 strips, COGS ₹45 per strip, found NSQ after 70% shipped, and 80% of shipped units are recovered: units shipped = 280,000; recovered = 224,000. Costs: write-off 224,000 × 45 = **₹100.8 lakh**; reverse freight ₹6 per strip = ₹13.44 lakh; destruction ₹2 per strip = ₹4.48 lakh; plus the unshipped 120,000 strips held for investigation = ₹54 lakh of blocked stock. Direct cost ≈ ₹118.7 lakh (and ₹54 lakh of stock is blocked while the investigation runs) before lost sales, regulatory fines and brand damage: a small cost of prevention (better testing and supplier audit) would have been far cheaper.

### In the news
See news box. A shortage after a recall or a raw-material shock raises the risk that stock of uncertain quality is pulled into the market; this is why traceability and availability data go together.

### Interview angle
> [!question] How it is asked
> "A batch of a paediatric syrup fails an impurity test after distribution. Walk me through the first 48 hours."

> [!tip] Strong answer includes
> - Immediate hold, notify, class and depth of recall
> - Batch-level trace to every consignee, with reconciliation target
> - Communication (regulator, trade, doctors) and disposal
> - CAPA on supplier qualification and incoming testing, and mock-recall metrics

---
## 7. FEFO, Expiry & Short-Dated Stock
> 🟠 Tier 2 · _Key points:_ FEFO, minimum remaining shelf life, near-expiry, returns, write-offs

### Definition
**FEFO** (first-expired, first-out) issues the batch with the nearest expiry, not the oldest receipt (FIFO). Pharma needs it because batches of the same SKU have different expiry dates and a unit is worthless after expiry. Key rules:
- **Minimum remaining shelf life (MRSL)** at receipt and at dispatch (e.g. receive ≥70% of life; dispatch to retailer ≥ 50-60%), standard in tenders and distributor contracts.
- **Near-expiry** management: monitor stock by expiry buckets (<3, 3-6, 6-12 months), push to fast channels, return to manufacturer (expiry returns schemes of 3-5% of sales are normal), or destroy and write off.
- Forecast accuracy and batch-size choice matter: large batch sizes can create expiry risk for slow SKUs ([[004 Demand Forecasting & Planning]], [[003 Inventory Management]]).

Retail-level loss often comes from mismatch between purchase pack and consumption, and from stockists keeping slow SKUs "in case" a doctor prescribes.

### Example
A hospital pharmacy holds two batches of a ₹80 drug: Batch A, 20,000 units expiring in 3 months, and Batch B, 30,000 units expiring in 9 months. Use is 8,000 units a month. **FEFO** issues Batch A first: 24,000 units are used in 3 months, so all 20,000 of Batch A are consumed (plus 4,000 from B) and the remaining 26,000 of B are used within the next 3.25 months: **zero expiry loss**. If staff wrongly issue the newest batch first (B), in 3 months only 24,000 of B's 30,000 are used and all 20,000 units of A expire: 20,000 × ₹80 = **₹16 lakh** lost. At portfolio level, a 3% annual expiry write-off on ₹40 lakh of inventory is ₹1.2 lakh, a figure to compare against holding cost and fill-rate targets.

### In the news
See news box. In periods of shortage (platinum-related chemotherapy shortage), stock allocation by expiry and by patient priority becomes important to avoid waste.

### Interview angle
> [!question] How it is asked
> "A distributor has 8% of inventory near expiry. What do you do and how do you prevent it?"

> [!tip] Strong answer includes
> - Short-term: bucket by expiry, redeploy, return, discount, donate where allowed
> - Root causes: batch sizes, forecast bias, long cover, poor FEFO discipline, MRSL gaps
> - System: FEFO picking in WMS ([[010 Warehouse Management]]), expiry alerts, SLOB reviews
> - Quantify: expiry loss as % of sales and trend

---
## 8. Drug Pricing: NPPA, DPCO & Trade Margins
> 🟠 Tier 2 · _Key points:_ NLEM, ceiling price, market-based pricing, 10% rule, para 19, trade margin rationalisation

### Definition
**NPPA** (National Pharmaceutical Pricing Authority) implements the **Drugs (Prices Control) Order, 2013** under the Essential Commodities Act. Structure:
- **NLEM** (National List of Essential Medicines, latest 2022, 384 medicines): drugs on the list are **scheduled**; **ceiling prices** apply (928 scheduled formulations count different strengths and forms, per NPPA's 2026 data call).
- **Ceiling price (market-based method)** = simple average of **price to retailer (PTR)** of all brands with at least 1% market share in that formulation, plus the **retailer margin of 16%**, GST extra.
- **Annual revision** of ceiling prices by the change in the **wholesale price index (WPI)**; the 0.64% change in March 2026 is an example.
- **Non-scheduled drugs**: manufacturers may raise MRP by at most **10% in a 12-month period** (checks by NPPA).
- **Para 19**: in extraordinary circumstances, NPPA can fix or revise the price of any drug in the public interest (invoked in June 2026 for the cancer drugs and vaccines).
- Separate **device price caps**: coronary stents (Feb 2017, about ₹7,260 for bare-metal and ₹29,600 for drug-eluting, indexed since) and knee implants.
Trade-margin rationalisation (capping margin on selected cancer drugs, 2019) sits on top.

### Example
Five brands each with at least 1% share have PTRs per strip of ₹22.00, ₹24.50, ₹26.00, ₹21.00 and ₹25.00 (illustrative). Simple average = ₹23.70. Ceiling price (excl. GST) = 23.70 × 1.16 = **₹27.49**. A brand with MRP ₹31 must cut to ₹27.49 + GST; a brand at ₹25 may stay. Economic effects: low-priced brands are not forced to rise, high-priced brands lose margin, and if input costs rise (as for platinum) an unviable ceiling price causes supply withdrawal, which is why Para 19 relief was needed.

### In the news
See news box. This is live evidence for the topic: three NPPA actions in about three months (indexation in March, a data call and a Para 19 price rise in June), the last one raising a cap to protect supply.

### Interview angle
> [!question] How it is asked
> "Price caps help patients but can cause shortages. How would you design the policy and handle the trade-off?"

> [!tip] Strong answer includes
> - Mechanism: NLEM, market-based ceiling, WPI indexation, 10% rule, Para 19
> - Evidence: price cuts saved patients money (govt estimate of ₹3,788 crore a year for 2022 list), but viability risk for low-margin generics
> - Mitigation: monitoring (quarterly data), targeted relief, procurement of API, manufacturer incentives
> - For a company: pricing, portfolio and supply decisions under controlled prices

---
## 9. Generics, API Dependence on China & India's Response
> 🟠 Tier 2 · _Key points:_ KSM, API, single-source, PLI, bulk-drug parks, dual sourcing

### Definition
Indian generics makers are global volume leaders but depend on imported **key starting materials (KSMs)**, intermediates and APIs, historically 60-70% from China for many categories (66% by volume in 2016-17 in the Wikipedia figure above; share varies by molecule and has moved since). Dependence is highest in antibiotics (penicillin, cephalosporin chain), vitamins, paracetamol and some cardio drugs.

Government response: **PLI for bulk drugs** (₹6,940 crore for 41 products, 2020) and **bulk drug parks**, the broader **pharma PLI** (₹15,000 crore) and the PRIP research scheme; plus company moves: **China+1 and backward integration**, dual sourcing, and long-term contracts. Risks: price war from Chinese suppliers, environmental compliance cost in India, and the time to qualify a new API source (regulatory filings in the US/EU require a change-notification, so switching can take 6-18 months). This is a Kraljic **strategic/bottleneck** category ([[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]], [[002 Procurement & Strategic Sourcing]]).

### Example
A formulation has API at 30% of COGS. If the imported API price rises 20%, COGS rises 6% (0.30 × 0.20). With a COGS-to-price ratio of 40% and a price cap, margin falls by 0.06 × 40% = 2.4 percentage points of price, i.e. a company with a 20% EBITDA margin loses 12% of EBITDA. Dual sourcing at 20% of volume from India at a 10% higher price raises blended API cost by only 2% yet limits exposure if the Chinese supply is cut.

### In the news
See news box. The pharma PLI and the NPPA platinum action are the same story told from two ends: policy supports API depth, and pricing rules decide whether manufacturers can bear input shocks.

### Interview angle
> [!question] How it is asked
> "India is the 'pharmacy of the world' but imports most of its API. How would you reduce this risk for a mid-size generics company?"

> [!tip] Strong answer includes
> - Quantify exposure: % API/KSM by value and by country, single-source items
> - Options: dual-source, regulatory filing of second source, backward integration, buffer stock for critical KSMs
> - Policy levers: PLI, bulk-drug parks, tariffs and anti-dumping
> - Total cost: price premium vs risk reduction ([[015 Supply Chain Risk & Resilience]], [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]])

---
## 10. Vaccine Supply Chain: UIP, Cold-Chain Network & U-WIN
> 🟠 Tier 2 · _Key points:_ UIP, ILR, vaccine vial monitor, eVIN, U-WIN, forecasting

### Definition
India's **Universal Immunisation Programme (UIP)**, launched in 1985, covers vaccines against 12 diseases and reaches about 27 million children a year (per Wikipedia summary); the programme also covers pregnant women. The supply chain is government-run, multi-tier: manufacturer or procurement agency → **national store** → **state vaccine stores** → **district stores** → **cold chain points** at PHCs/CHCs → **session sites** (outreach with vaccine carriers).

Equipment: **walk-in coolers/freezers** at state and regional stores, **ice-lined refrigerators (ILR)** and deep freezers at cold chain points, **cold boxes/vaccine carriers** with conditioned ice packs, **vaccine vial monitors (VVM)** on vials, data loggers. **eVIN** (electronic vaccine intelligence network) digitises vaccine stock and temperature at cold chain points; **U-WIN** is the digital platform for registering and tracking immunisation of pregnant women and children (a Co-WIN-like record). Rules: **multi-dose vial policy**, **shake test** for freeze damage, **open-vial policy**, first-expiry-first-out.

Supply challenges: wastage in multi-dose vials (planned wastage factor), forecasting of demand by session, last-mile transport in hilly or flood-prone districts, power outages, and freezing of freeze-sensitive vaccines (the commonest cold-chain failure).

### Example
A district expects 4,000 children to need a 10-dose-vial vaccine in a month. With 25% planned wastage the factor is 1/(1 − 0.25) = 1.333: doses required = 4,000 × 1.333 = 5,333, i.e. 533.3 vials, so **534 vials**. Cutting wastage to 15% (factor 1.176) gives 4,706 doses = 470.6 vials, so **471 vials**: **63 vials (about 12%) saved** a month by better session planning (fewer, larger sessions and open-vial policy), before adding any safety stock.

### In the news
See news box. NPPA's price move for BCG and measles vaccines shows that public-programme vaccines also sit under price regulation, and that sustaining supply is a pricing and sourcing issue as much as a cold-chain one.

### Interview angle
> [!question] How it is asked
> "How would you reduce vaccine wastage and stock-outs in a large Indian state?"

> [!tip] Strong answer includes
> - Network: state store → district → cold chain point → session site
> - Data: eVIN stock and temperature visibility; U-WIN for demand and defaulter tracking
> - Operations: session planning, multi-dose vial rules, replenishment cycles, redundancy in power
> - Quantify wastage factors and safety stock as above

---
## 11. Hospital Inventory, Implants & Consignment
> 🟠 Tier 2 · _Key points:_ ABC/VED, par levels, consignment implants, central pharmacy, stock-outs

### Definition
A hospital manages thousands of SKUs: drugs, consumables (syringes, sutures), implants (stents, joints), reagents, and equipment spares. Typical tools: **ABC by value**, **VED by clinical criticality** (a "vital" item such as oxygen or anti-venom gets near-100% availability regardless of cost), **par levels** with periodic review at wards, a **central store** with **ward sub-stores**, and **unit-dose or automated dispensing cabinets**. Implants are often kept on **consignment** or loaner sets from the supplier, billed on use; reps attend surgeries, with traceability by implant serial.

Procurement: **rate contracts and tenders** (public hospitals), **group purchasing** (private chains), and **price caps** on items such as stents which change vendor economics. Risks: expiry in slow-moving specials, leakage and pilferage, emergency purchases at high prices, and tight service levels for life-saving items ([[003 Inventory Management]] for ABC/VED/FSN).

### Example
A 400-bed hospital uses 600 SKUs of surgical consumables. Applying ABC: top 12% of SKUs account for 70% of spend (A items: weekly review, tight min/max); next 25% give 20% (B: fortnightly), remaining 63% give 10% (C: monthly, large order quantities). Moving the stents and orthopaedic implants to consignment with a ₹1.2 crore average stock at 11% cost of capital removes ₹13.2 lakh a year of carrying cost from the hospital; the vendor's offsetting request is a 3-4% price premium, so the net gain is for the party with the lowest cost of capital and best forecast.

### In the news
See news box. Hospitals felt the platinum-related chemotherapy shortage as stock-outs of oncology injectables; essential-medicine data collection by NPPA aims to give an early warning.

### Interview angle
> [!question] How it is asked
> "Design an inventory policy for a hospital's pharmacy with 5,000 SKUs."

> [!tip] Strong answer includes
> - Segmentation by value (ABC), criticality (VED) and demand pattern
> - Min/max and par levels with service targets by class
> - FEFO, expiry controls, consignment for implants, emergency buy protocol
> - Metrics: stock-out rate for vital items, expiry %, inventory days

---
## 12. Jan Aushadhi, Public Procurement & Generic Access
> 🟠 Tier 2 · _Key points:_ PMBJP, Kendras, central warehouse, tenders, TNMSC model

### Definition
**Pradhan Mantri Bhartiya Janaushadhi Pariyojana (PMBJP)** sells quality-tested generic medicines through dedicated **Jan Aushadhi Kendras** at prices that the government says are typically 50-80% below branded equivalents. Supply chain: **PMBI** (Pharmaceuticals & Medical Devices Bureau of India) procures through tenders (suppliers must hold WHO-GMP certification and pass batch testing at NABL labs), stores in central warehouse (Gurugram) and regional depots, and ships to Kendras run by entrepreneurs, NGOs and institutions; revenue comes from a trade margin for the Kendra owner and incentives. Scale: the network crossed about 15,000 Kendras by 2025 with a target of 25,000 (from ministry statements; verify the latest count before quoting).

Other public models: **Tamil Nadu Medical Services Corporation (TNMSC)**, a benchmark for centralised tender, computerised stock and quality testing; **Rajasthan's free medicine scheme**; **state drug logistics corporations**; and **PM-JAY** empanelled hospitals. Typical challenges: stock-outs of high-demand SKUs at Kendras, small range for chronic-care brands, doctors' prescribing behaviour, and distribution to rural areas.

### Example
A diabetic pays ₹1,200 a month for branded drugs. If the Jan Aushadhi generic costs 35% of the branded price: ₹420, a saving of ₹780 per month (65%) and **₹9,360 a year**. For a Kendra selling ₹3 lakh of medicines a month at a 20% margin, gross margin = ₹60,000 monthly before rent, pharmacist salary, power and wastage, so footfall and product availability decide viability.

### In the news
See news box. Price control (NPPA) and generic access (PMBJP) both aim at affordability; the first regulates brands, the second changes the channel.

### Interview angle
> [!question] How it is asked
> "How would you scale Jan Aushadhi from 15,000 to 25,000 outlets without stock-outs?"

> [!tip] Strong answer includes
> - Demand-led assortment (top 200 SKUs by demand per Kendra cluster), regional depots, replenishment frequency
> - Supplier base and quality testing capacity
> - Kendra economics and training; digital ordering and visibility
> - Prescribing and awareness levers, not only supply

---
## 13. Regulatory Risk, Counterfeits & Compliance Playbook
> 🟠 Tier 2 · _Key points:_ NSQ, spurious drugs, import alerts, price risk, contract manufacturing

### Definition
Pharma supply chains face four recurring regulatory risks:
1. **Quality/enforcement**: NSQ and spurious drug findings, licence cancellations, FDA warning letters and import alerts, product bans (fixed-dose combinations).
2. **Price control**: NPPA ceiling prices, trade-margin caps, device price caps; unilateral changes may make an SKU loss-making.
3. **Track-and-trace/serialisation** and data-integrity compliance, including late deadlines and changing rules.
4. **Trade and tariff**: US tariff or Section 232 measures on pharmaceuticals, EU rules, export controls on APIs.

Counterfeit and substandard medicines enter through weak points: unlicensed wholesale, online sellers, repackaging and returns. Controls: authorised-distributor lists, serialisation and verification at dispensing, tamper-evident packs, vendor qualification (including **audits of CMOs and 3PLs**), complaint analytics, and board-level quality KPIs. A **regulatory risk register** with owner, trigger and action per risk keeps the supply chain ahead of rule changes ([[015 Supply Chain Risk & Resilience]]).

### Example
A company sells 20 million packs a year at ₹40 realisation per pack for a drug under a ceiling price. A 5% ceiling cut (₹2 per pack) reduces revenue by ₹4 crore; with a contribution margin of 35% (₹14) and no cost reduction, contribution falls from ₹28 crore to ₹24 crore (−14.3%). Mitigations: API savings (3%), pack-size mix, dropping the lowest-margin SKU if the company is allowed to discontinue (with regulator notice), or shifting volume to non-scheduled products.

### In the news
See news box. NPPA's three actions within about three months (indexation, data call, Para 19) show regulatory risk running both ways: sometimes it cuts price, sometimes it lifts the cap to protect supply.

### Interview angle
> [!question] How it is asked
> "Rank the biggest regulatory risks to a pharma supply chain and say how you would manage each."

> [!tip] Strong answer includes
> - A structured list: quality, price, track-and-trace, trade
> - Impact estimate per risk (₹ or % margin) and early-warning indicators
> - Preventive controls and contingency plans (second source, buffer, regulatory affairs liaison)
> - Governance: owner and reporting cadence

---
## 14. ⭐ Advanced: Drug Shortage Risk & Resilience Scoring
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Drug shortages arise from low-margin sterile injectables and old generics (little incentive to invest), single-site or single-API supply, quality shutdowns, demand surges and input shocks (platinum, heparin, solvents). A **shortage risk score** for each SKU can combine:
- **Concentration**: number of qualified API and finished-dose sources and sites.
- **Margin headroom**: price relative to ceiling and cost of goods.
- **Criticality**: clinical severity if absent (VED).
- **Recovery time**: time to qualify an alternative plus time to rebuild stock.
- **Buffer**: weeks of cover in the chain.

$$\text{Risk score} = \text{Concentration} \times \text{Criticality} \times \frac{\text{Recovery time}}{\text{Buffer cover}}$$

(a relative index for ranking, not a probability). High scores trigger action: safety stock of API or finished goods, second-source qualification, long-term contracts, or regulatory dialogue on pricing.

### Example
Two SKUs. Cisplatin injection: 2 qualified sources (concentration scored 2 on a 1-3 scale where 1 = many sources and 3 = single source), criticality 3, recovery 16 weeks, buffer 4 weeks: score = 2 × 3 × 16/4 = **24**. Paracetamol tablets: 3 (many sources → concentration 1), criticality 1, recovery 6 weeks, buffer 8 weeks: 1 × 1 × 6/8 = **0.75**. The 32-fold difference shows where buffers belong. If cisplatin buffer is raised from 4 to 8 weeks: 2 × 3 × 16/8 = 12; cost of an extra 4 weeks of stock at 12 lakh a week and 11% carrying cost is 48 lakh × 11% ≈ ₹5.3 lakh a year per SKU.

### In the news
See news box. In June 2026 the platinum-driven problem was handled through price relief; a shortage score that tracks input-price indices and source counts is the kind of tool that can flag such SKUs earlier.

### Interview angle
> [!question] How it is asked
> "How would you build an early-warning system for medicine shortages at a distributor or a state procurement agency?"

> [!tip] Strong answer includes
> - Data: stock cover, sales trend, source count, price vs ceiling, input price indices
> - A simple scoring approach and thresholds for escalation
> - Playbook: allocation, substitution, import via emergency channels, price relief request
> - Governance: weekly shortage review and cross-functional ownership with [[012 Supply Chain Analytics & KPIs]]-style dashboards
