---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Outsourcing, Supplier Partnerships & Kraljic Strategies"
tier: Tier 2
roles: Consulting / Operations
status: complete
subtopics: 13
---
# Outsourcing, Supplier Partnerships & Kraljic Strategies

⬅ [[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[125 Transportation Management Deep Dive]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. Kraljic Matrix: Scoring, Quadrant Strategies and Pitfalls]]
2. [[#2. The Supplier Relationship Spectrum: Transactional to Alliance to Vertical Integration]]
3. [[#3. Outsourcing Decision Frameworks: What to Make, What to Buy]]
4. [[#4. Contract Manufacturing, EMS, OEM, ODM and CDMO Models]]
5. [[#5. Vested Outsourcing and Outcome-Based Contracts]]
6. [[#6. Supplier Tiers, Keiretsu and Strategic Alliances]]
7. [[#7. Offshoring and the Total Cost of Offshoring]]
8. [[#8. Supplier Development and Co-Location]]
9. [[#9. Outsourcing Risks: Hollowing Out, IP Leakage, Dependency and Quality]]
10. [[#10. Relationship Governance: Structure, KPIs and Cadence]]
11. [[#11. SLAs, Service Credits and Incentive Design]]
12. [[#12. Exit Planning, Insourcing and Reshoring]]
13. [[#13. ⭐ Advanced: Transaction Cost Economics, Hold-Up and Relationship-Specific Investment]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Indian contract manufacturers scale up while global brands outsource whole networks
> **Dixon Technologies, India's contract-manufacturing bellwether.** Per its Wikipedia profile (figures as published there; checked October 2026), Dixon operates as an **EMS and ODM** company with **FY25 revenue of ₹38,880 crore** (about US$4.0 billion), 17 manufacturing units and over 15,000 employees. It makes products for brands such as Samsung, Xiaomi, Panasonic, Philips, Motorola and Google (Pixel phones for US and European markets), and formed a joint venture with **Vivo in December 2024** for devices and smartphones, plus a telecom-equipment line for Bharti Airtel under the PLI scheme. ([Wikipedia: Dixon Technologies](https://en.wikipedia.org/wiki/Dixon_Technologies))
>
> **Puma hands its North American distribution network to Maersk (announced 24 September 2026).** Maersk contract logistics will manage fulfilment and inventory across three US distribution centres (about 2.3 million sq ft: Torrance, Phoenix, Whitestown), with Maersk's first multi-client AutoStore deployment at Torrance (about 20 million units a year of capacity from 2027). The deal expands an existing relationship that already covered ocean, air, customs and inland transport. Contract length was not disclosed. ([Supply Chain Dive](https://www.supplychaindive.com/news/puma-taps-maersk-to-manage-north-america-distribution-network/831623/))
>
> **Where outsourcing goes wrong.** Reference summaries of contract manufacturing list the standard risks: loss of intellectual property when formulas and designs are shared, dependency and loss of control, and the manufacturer prioritising other clients, against benefits of cost, specialised skills and scale. ([Wikipedia: Contract manufacturer](https://en.wikipedia.org/wiki/Contract_manufacturer))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Kraljic Matrix: Scoring, Quadrant Strategies and Pitfalls
> 🟠 Tier 2 · _Key points:_ Supply risk vs profit impact; scoring method; moving items over time; what the matrix cannot do

### Definition
The **Kraljic matrix** (Peter Kraljic, "Purchasing Must Become Supply Management", Harvard Business Review, 1983) segments purchased **categories** on two axes: **profit impact** (vertical; volume, share of cost, effect on quality and product) and **supply risk / market complexity** (horizontal; number of suppliers, entry barriers, substitution, logistics, monopoly power). The quadrants and their standard actions are tabulated in [[002 Procurement & Strategic Sourcing]]; this note works through how to **score**, **act**, and **avoid misuse**.

**Scoring method:** list categories; score each criterion 1 to 5 (profit impact: % of spend, effect on product cost and quality; supply risk: number of qualified suppliers, switching time, import share, single-source status); weight and average; classify high at about 3.5 and above.

| Quadrant | Posture | Typical actions |
|---|---|---|
| Strategic (high impact, high risk) | **Partner** | Long-term agreements, early supplier involvement, joint development, capacity reservation, dual-source where possible, open-book costing |
| Leverage (high impact, low risk) | **Exploit** | Competitive bids, volume consolidation, reverse auctions, index-based pricing, switching |
| Bottleneck (low impact, high risk) | **Secure** | Safety stock, substitution, spec flexibility, supplier development, longer contracts for continuity |
| Non-critical (low impact, low risk) | **Simplify** | Catalogues, P-cards, standardisation, tail-spend automation |

**Common misuses:** classifying suppliers instead of categories, treating it as static, and using spend as a proxy for profit impact.

### Example
Scores (profit impact, supply risk) for an EV two-wheeler maker: battery cells (5, 5) strategic; sheet steel (5, 2) leverage; a single-source motor-controller chip (2, 5) bottleneck; stationery (1, 1) non-critical; wiring harness (4, 3) leverage; rubber compound for tyres (4, 4) strategic. Actions: long-term, co-developed contract with capacity reservation for cells; index-linked annual tenders for steel; safety stock plus a second-source qualification for the chip; e-catalogue for stationery. When a trade or export event raises supply risk for steel from 2 to 4, steel migrates to strategic and the sourcing posture must change.

### In the news
See news box. A multi-brand EMS such as Dixon sits at the **strategic** end of its customers' portfolios (high impact, scarce capacity), while Puma's distribution network is an example of a category being moved from internal management to a partner.

### Interview angle
> [!question] How it is asked
> "Apply the Kraljic matrix to this company's purchases and tell me what you would do differently for each quadrant."

> [!tip] Strong answer includes
> - Axes named correctly and scoring criteria stated
> - Categories, not suppliers; examples from the client's context
> - Different actions per quadrant, and a note that items migrate
> - Criticism: static snapshot, spend bias, ignores supplier power and relationship

---
## 2. The Supplier Relationship Spectrum: Transactional to Alliance to Vertical Integration
> 🟠 Tier 2 · _Key points:_ Arm's length, preferred, strategic alliance, JV, ownership; matching depth to value

### Definition
Buyer-supplier relationships lie on a spectrum:

| Form | Commitment | Information sharing | Typical use |
|---|---|---|---|
| **Arm's-length / transactional** | Per order | Price and specification | Leverage and non-critical items |
| **Preferred supplier / framework agreement** | 1-3 years, volume intent | Forecasts, performance | Repeat buys with performance tracking |
| **Strategic partnership / alliance** | 3-10 years, joint targets | Cost data, roadmaps, joint planning | Strategic items, co-development |
| **Joint venture / equity stake** | Shared ownership | Deep | Capacity, technology or market access |
| **Vertical integration (make)** | Full control | Internal | Core, proprietary, risky-to-outsource |

Greater commitment brings **lower cost over time, innovation and supply assurance**, but also **higher switching costs, dependence and monitoring needs**. Partner only where the item is strategic and the supplier is capable and trustworthy; use competition elsewhere. Detailed supplier relationship management concepts (segmentation, scorecards) are in [[002 Procurement & Strategic Sourcing]]; the focus here is partnership design.

### Example
A bus-body builder moves chassis components from annual tenders to a five-year partnership with a tier-1: shared 3-year volume forecast, agreed annual price-down of 2% against jointly identified savings, supplier parks near the plant and joint kaizen. If the plan delivers 2% a year on ₹200 crore, the savings are ₹4 crore in year 1 and ₹7.92 crore cumulative by year 2 (₹4 crore + 2% of the then-reduced base: 196 × 2% = ₹3.92 crore). The price-down only holds if volume is committed: a volume shortfall is the main way partnerships fail.

### In the news
See news box. Dixon's Vivo joint venture (December 2024) is an example of moving from contract to equity-linked partnership as capability and market access become interdependent.

### Interview angle
> [!question] How it is asked
> "When would you move from competitive bidding to a strategic partnership?"

> [!tip] Strong answer includes
> - Criteria: strategic importance, supply risk, supplier capability, trust
> - What each side commits (volume, information, investment)
> - Governance, exit clauses and cost-benefit sharing
> - Risks: lock-in, complacency, over-reliance

---
## 3. Outsourcing Decision Frameworks: What to Make, What to Buy
> 🟠 Tier 2 · _Key points:_ Core vs non-core, capability fit, transaction costs, strategic importance

### Definition
Beyond the cost-based make-or-buy comparison in [[002 Procurement & Strategic Sourcing]], outsourcing decisions use frameworks that look at **strategic** fit:
- **Core competency test** (Prahalad and Hamel): keep activities that give competitive advantage, are hard to imitate and span products; outsource commodity activities.
- **Strategic importance x relative capability matrix:** high importance and high capability: keep and invest; high importance, low capability: build or ally; low importance, high capability: sell or share; low importance, low capability: outsource.
- **Transaction cost economics** (Williamson): outsource when markets are competitive and **asset specificity** (dedicated tooling, know-how), **uncertainty** and frequency are low; integrate or form close partnerships when specificity is high (hold-up risk).
- **Quinn and Hilmer:** outsource where the supplier has superior scale or expertise, but avoid ceding activities that create critical knowledge.
- **Scorecard:** cost, quality, flexibility, risk, IP sensitivity, control, regulatory implications, capacity.

Financial test: compare **TCO** of in-house vs outsource, including transition and governance costs, rather than the quoted price alone.

### Example
Make or buy a plastic housing: in-house needs ₹6 crore of fixed cost (tooling, moulding capacity) and ₹700 variable per unit; the contract manufacturer quotes ₹820 per unit with no fixed cost. Break-even volume = 6,00,00,000 / (820 − 700) = **5,00,000 units**. Above 5 lakh units a year, in-house is cheaper; below it, outsource. At 3 lakh units: in-house cost = ₹6 crore + 3 lakh × ₹700 = ₹8.1 crore; outsource = 3 lakh × ₹820 = ₹2.46 crore, so outsourcing saves **₹5.64 crore**. Add hidden costs of oversight, quality and logistics (say 5% of ₹2.46 crore = ₹12 lakh) and run an IP-sensitivity check before deciding; the saving is large enough to survive them.

### In the news
See news box. Puma's decision to outsource network management to Maersk follows the same logic: logistics is a non-core activity for a sports brand where a partner brings automation and scale.

### Interview angle
> [!question] How it is asked
> "Should a mid-size manufacturer outsource its warehouse or its machining?"

> [!tip] Strong answer includes
> - Strategic vs cost criteria; core competency and IP sensitivity
> - Break-even volumes and TCO with hidden costs
> - Capability of the supplier market and switching costs
> - Phased pilot and exit route

---
## 4. Contract Manufacturing, EMS, OEM, ODM and CDMO Models
> 🟠 Tier 2 · _Key points:_ Who designs, who owns IP, who sources; India EMS and PLI

### Definition
| Model | Who designs | Who owns IP | Typical sectors | Example roles |
|---|---|---|---|---|
| **OEM** (original equipment manufacturer) | Brand owner | Brand | Autos, appliances, many industrial goods | Builds to the brand's specification |
| **Contract manufacturer (CM)** | Brand | Brand | FMCG, apparel, pharma, consumer goods | Produces under the brand's name |
| **EMS** (electronics manufacturing services) | Brand | Brand | Electronics: PCB assembly, box build | Assembly, test, supply chain management |
| **ODM** (original design manufacturer) | Manufacturer | Manufacturer or shared | Consumer electronics, white-label | Designs and builds; brand rebadges |
| **CDMO / CMO** | Client or CDMO | Client (process knowledge shared) | Pharma, biotech | Process development plus manufacturing |

Key decisions: **who buys the components** (turnkey vs consigned), **tooling ownership**, **IP and know-how protection**, **capacity commitment**, **quality system** (IATF 16949, ISO 13485, GMP), **pricing** (cost-plus, per-unit with material pass-through), and **minimum volumes**. In India, **PLI schemes** for electronics, pharma and autos ([[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]) encourage domestic contract manufacturing; sector detail in [[134 Electronics & Semiconductor Supply Chain]] and [[132 Pharma & Healthcare Supply Chain]].

### Example
A phone brand uses an EMS partner for assembly (turnkey, the EMS buys components at ₹7,200 per unit and charges ₹400 for conversion and ₹300 margin: ₹7,900), versus an ODM model where the manufacturer also designs the phone (₹8,300 per unit including design amortisation, but time to market falls by about six months). Choice: if design differentiation is the brand's edge, EMS; if speed and breadth of range matter, ODM.

### In the news
See news box. Dixon's FY25 revenue of ₹38,880 crore, with customers spanning Samsung to Google, shows EMS and ODM scale, while contract-manufacturing summaries flag IP and dependency risks.

### Interview angle
> [!question] How it is asked
> "Contract manufacturer or own plant for a new product line?"

> [!tip] Strong answer includes
> - Distinguish OEM/EMS/ODM/CDMO
> - Component sourcing and tooling ownership
> - IP protection, dual-sourcing the contract manufacturer, quality audits
> - Volume and capex trade-off; role of PLI and policy

---
## 5. Vested Outsourcing and Outcome-Based Contracts
> 🟠 Tier 2 · _Key points:_ Buy outcomes not transactions; five rules; gainshare; relational contracting

### Definition
**Vested outsourcing** (University of Tennessee, Kate Vitasek) is a hybrid, relational-contract approach in which buyer and provider are both vested in each other's success, built on relational contract theory (Macneil, Macaulay). Its five rules:
1. **Outcome-based, not transaction-based:** pay for results.
2. **Focus on the "what", not the "how":** let the provider choose the method.
3. **Clearly defined, measurable desired outcomes.**
4. **Pricing model with incentives** that reward outcomes and share gains (and pains).
5. **Insight over oversight:** governance through transparency and data.
Reported adopters include P&G, Microsoft, Dell and FedEx (per the vested-outsourcing literature, as summarised in public references). Compare with **transactional** (price per unit, SLAs, penalties) and **relational** models. Needs trust, data transparency, a long horizon and honest baselines.

### Example
A 3PL runs a plant's inbound logistics. Baseline cost ₹120 per tonne; vested agreement targets ₹108 within two years, sharing savings 50:50. Savings = ₹12 per tonne; the provider earns ₹6 per tonne gain share (plus the management fee). If volume is 4 lakh tonnes, buyer saves ₹24 lakh and provider earns ₹24 lakh in incentive in addition to a fixed fee. Guardrails: a **baseline** audited by both sides, service floors (OTIF at least 97%), and a cap or floor on gains to prevent gaming.

### In the news
See news box. Puma-Maersk shows an existing multi-service partnership widened to run whole facilities; the reported terms do not say whether pricing is outcome-based, but arrangements of this scale are where gain-share and shared-capacity rules would be negotiated.

### Interview angle
> [!question] How it is asked
> "How would you structure a contract with a 3PL so that it keeps improving instead of only meeting an SLA?"

> [!tip] Strong answer includes
> - Outcome definitions, gainshare/painshare, baselines
> - Insight-based governance and open data
> - Clear exit and benchmarking provisions
> - Preconditions: trust, time horizon, honest baseline

---
## 6. Supplier Tiers, Keiretsu and Strategic Alliances
> 🟠 Tier 2 · _Key points:_ Tier-1/2/3 structure; vertical keiretsu; supplier associations; alliances

### Definition
Auto and electronics supply chains are **tiered**: **tier-1** suppliers deliver systems or modules to the OEM and manage **tier-2** (components) and **tier-3** (materials) suppliers. The OEM controls tier-1 directly and tier-2 indirectly. The Japanese **vertical keiretsu** links a parent (Toyota, Nissan) to tiered suppliers through long relationships, shared planning, supplier associations and often small equity stakes. **Horizontal keiretsu** (the Mitsubishi, Mitsui, Sumitomo groups) are bank-centred cross-shareholding groups; cross-shareholdings weakened after the 1990s and Japan's 2015 governance code pushed disclosure. Features that other firms copy without ownership: **long-term commitment, joint cost-down targets, supplier associations, supplier parks, open information, shared development roles**. Alliances (looser than keiretsu) include co-development, joint procurement and technology licensing. In India, Tata, Mahindra, Maruti Suzuki and Hero MotoCorp use supplier clusters and tiers; see [[131 Automotive Supply Chain - JIT, Tiers & EVs]].

**Risks of tiering:** low visibility into tier-2 and tier-3 (Nexperia-type events), lower flexibility, bargaining dependence. Mitigation: map sub-tier critical parts, flow down quality and compliance requirements ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

### Example
An OEM sources a wiring harness (tier-1) which uses copper wire (tier-2) from a drawer, which buys copper rod (tier-3). Cost split of the harness at ₹1,000: copper 45% (₹450), labour and conversion 25% (₹250), connectors and other parts 15% (₹150), overhead and margin 15% (₹150). An OEM wanting to cap price risk negotiates a copper index clause **at the tier-1** while the tier-1 passes the same index to its tier-2: the OEM's visibility into the 45% share allows a fair price adjustment instead of a flat premium.

### In the news
See news box. Brands such as Samsung and Google using Dixon show a brand-to-EMS tier relationship; the weak spot is almost always visibility of the tier below.

### Interview angle
> [!question] How it is asked
> "What can Indian OEMs learn from the keiretsu system?"

> [!tip] Strong answer includes
> - Vertical vs horizontal keiretsu and the features that work (commitment, joint kaizen, shared forecasts)
> - Limits: rigidity, inbreeding, cross-shareholding unwinding
> - Tier visibility and cascade of requirements
> - Indian context: clusters, supplier parks, tier-1 consolidation

---
## 7. Offshoring and the Total Cost of Offshoring
> 🟠 Tier 2 · _Key points:_ Headline price vs landed and risk-adjusted cost; duty, freight, inventory, quality, FX

### Definition
**Offshoring** moves production or services abroad (to one's own captive site or to a third party). The headline gain is a lower unit price; the true comparison is **total landed cost** plus risk costs (see [[009 Logistics & Distribution|total landed cost in the logistics note]] and the TCO idea in [[002 Procurement & Strategic Sourcing]]). Hidden items: **freight and insurance**, **customs duty and taxes** (including GST credit mechanics), **port and inland handling**, **pipeline and safety inventory** from longer lead time (carrying cost 15-25% a year), **quality and rework**, **FX hedging cost or exposure**, **supplier oversight and travel**, **IP risk**, **order flexibility** (larger MOQs), and **disruption risk**. Counter-trends: **nearshoring, friend-shoring and China+1**, driven by tariffs, geopolitics and resilience.

### Example
A domestic part costs ₹1,000 per piece. An overseas supplier quotes ₹780 ex-works (22% cheaper):

| Item | ₹ per piece |
|---|---|
| Ex-works price | 780.00 |
| Freight and insurance (4%) | 31.20 |
| Customs duty (assumed 10% of CIF ₹811.20) | 81.12 |
| Port and inland handling (2%) | 15.60 |
| Pipeline inventory carrying (18% a year, 60 extra days) | 23.08 |
| Extra safety stock (20 days) | 7.69 |
| Quality and rework (1.5%) | 11.70 |
| FX hedging cost (1%) | 7.80 |
| Oversight and travel (1%) | 7.80 |
| **Total landed cost** | **965.99** |

Real saving = 1,000 − 966 = **₹34 (3.4%)**, not 22%. On 4,00,000 pieces: ₹1.36 crore. If duty were 20% instead of 10%, landed cost becomes ₹1,047 and the offshore option is **4.7% dearer**. Duty rate, extra inventory days and quality cost decide the answer, so run sensitivity.

### In the news
See news box. The items there do not quote duty rates; the 10% vs 20% duty sensitivity in the example shows why any change in trade policy forces a re-run of offshoring TCO.

### Interview angle
> [!question] How it is asked
> "Supplier in China is 20% cheaper. Should we switch?"

> [!tip] Strong answer includes
> - Total landed cost build-up with numbers
> - Sensitivity on duty, lead time, FX, quality
> - Strategic factors: IP, resilience, speed, flexibility, regulation (BIS or import curbs)
> - Alternatives: domestic supplier cost-down, partial dual sourcing

---
## 8. Supplier Development and Co-Location
> 🟠 Tier 2 · _Key points:_ Develop vs switch; supplier parks; resident engineers; joint kaizen; investment sharing

### Definition
**Supplier development** is the buyer's investment of time, knowledge or money to raise a supplier's performance (quality, cost, delivery, safety, technology). Forms: **assessment and feedback**, **training** (lean, TPM, quality tools), **resident engineers** at the supplier, **joint improvement projects** (kaizen, VSM, SMED), **capital support** (tooling, equipment, loans, early payment), **technology transfer**, and **co-location** (supplier parks or in-plant satellite units next to the OEM, enabling JIT sequencing, shared logistics and fast problem solving). Quality-specific mechanics (audits, SCAR, 8D, PPAP) are in [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]; this section covers the strategic decision.

**Decision logic:** develop if the supplier is strategic or bottleneck, has willingness and capability gaps that are fixable, and benefits exceed the buyer's investment; otherwise re-source. Benefits: lower defect cost, shorter lead times, innovation, lower risk. Risks: free-riding by competitors who share the supplier, dependency, unrecovered investment.

### Example
Development plan for a bottleneck stamping supplier: buyer invests ₹40 lakh in engineer time, training and a gauge; the supplier cuts rejection from 3% to 1.2% on a supply of ₹25 crore a year. Rejection cost avoided (at cost of poor quality equal to the part value): (3% − 1.2%) × ₹25 crore = **₹45 lakh a year**. Payback = 40 / 45 = **0.89 years (about 11 months)**. A co-located satellite unit cuts transport and inventory: if pipeline inventory falls from 5 days to 1 day on ₹25 crore of annual purchases, inventory falls by ₹25 crore × 4/365 = **₹27.4 lakh**, worth about ₹5 lakh a year at 18% carrying cost.

### In the news
See news box. Large EMS and ODM networks (Dixon: 17 plants, over 15,000 staff) are the kind of supplier that is worth developing jointly rather than only auditing.

### Interview angle
> [!question] How it is asked
> "Would you invest in a weak supplier or replace it?"

> [!tip] Strong answer includes
> - Segment first (Kraljic); develop strategic or bottleneck suppliers
> - Evidence on capability gap and supplier commitment
> - Payback arithmetic and shared investment
> - Fallback: parallel qualification of an alternative

---
## 9. Outsourcing Risks: Hollowing Out, IP Leakage, Dependency and Quality
> 🟠 Tier 2 · _Key points:_ Hollow corporation, hold-up, IP, concentration, mitigation toolkit

### Definition
Key outsourcing risks:
- **Hollowing out:** the firm gradually loses skills (design, process know-how) and ends up dependent on suppliers, who may become competitors (a supplier moving into the brand's market).
- **IP and know-how leakage:** formulas, drawings, process parameters; risk rises with sharing and with the supplier serving competitors.
- **Dependency and hold-up:** switching costs and specific assets let the supplier renegotiate price after commitment.
- **Quality and brand risk** (ethical sourcing, safety failures at the supplier).
- **Capacity prioritisation:** the supplier favours bigger clients in a shortage.
- **Concentration and sub-tier opacity** (see [[015 Supply Chain Risk & Resilience]]).
- **Regulatory and sustainability exposure** (labour, environment; see [[014 Global SCM & Sustainability]]).

**Mitigation toolkit:** retain **critical know-how and design authority**; **NDAs and IP clauses**; split critical processes; **tooling ownership** and drawings escrow; **dual sourcing** or step-in rights; **audits** and quality gates; **capacity reservation**; **financial health monitoring**; **exit and transition plans**; internal capability to judge supplier performance (**intelligent buyer** capability).

### Example
A brand outsources final assembly and also shares full process parameters. A risk register entry: IP leakage, probability 10% a year, impact estimated at ₹30 crore loss of advantage: expected loss ₹3 crore a year. Mitigations: split the know-how (the supplier only receives parameters for its step; the brand keeps calibration software), contractual penalties and audit rights, and a second source for the 20% of volume with the most sensitive step. If mitigation cuts probability to 3% and costs ₹0.5 crore a year, net benefit = (10% − 3%) × 30 − 0.5 = **₹1.6 crore a year**.

### In the news
See news box. Contract-manufacturing references list IP loss and dependency among the main risks, the same ones brands manage when scaling EMS and ODM partners.

### Interview angle
> [!question] How it is asked
> "What are the risks of outsourcing and how would you protect the company?"

> [!tip] Strong answer includes
> - List of risks with examples (hollowing out, IP, hold-up)
> - Mitigation toolkit that matches each risk
> - Retaining a core capability even if production is outsourced
> - Quantify expected loss and mitigation cost

---
## 10. Relationship Governance: Structure, KPIs and Cadence
> 🟠 Tier 2 · _Key points:_ Three-tier governance; QBR; joint steering; escalation; relationship health

### Definition
**Governance** is how the parties direct and control the relationship after the contract is signed. A common three-tier structure:
1. **Strategic (executive) tier:** joint steering committee (twice yearly or yearly): strategy, roadmap, investments, big disputes.
2. **Tactical (management) tier:** quarterly business review (QBR) on KPIs, improvement projects, risks, commercial adjustments.
3. **Operational tier:** weekly or daily, handling orders, issues, escalation, with defined **RACI** and escalation paths.
Instruments: **balanced scorecard** (cost, quality, delivery, innovation, risk, relationship), **governance calendar**, **single point of contact**, **joint improvement plan**, **dispute resolution ladder**, **benchmarking clause**, and a **relationship health survey** (trust, communication). Governance effort should be proportional: strategic suppliers get all three tiers; leverage items get operational monitoring only. Link to supplier KPI design in [[012 Supply Chain Analytics & KPIs]].

### Example
A 3PL contract has these KPIs: OTIF 97%, damage rate below 0.2%, inventory accuracy 99.5%, and cost per case within budget. Governance calendar: daily huddle, weekly ops review, monthly KPI pack, quarterly QBR and an annual steering committee. A relationship health score (1 to 5) is collected every six months; a drop from 4.2 to 3.4 triggers an executive meeting even if KPIs are green, because trust problems show up before performance falls.

### In the news
See news box. Large multi-site arrangements such as Puma-Maersk (three DCs, a shared automation platform) need governance across sites and clients, including priority rules when capacity is shared.

### Interview angle
> [!question] How it is asked
> "How would you govern a critical outsourcing relationship?"

> [!tip] Strong answer includes
> - Three tiers with forums and cadence
> - KPIs and scorecards, benchmarking and joint improvement
> - Escalation ladder and dispute resolution
> - Relationship health beyond KPIs

---
## 11. SLAs, Service Credits and Incentive Design
> 🟠 Tier 2 · _Key points:_ Measurable service levels; credits, caps, bonus; gaming risks

### Definition
A **service-level agreement (SLA)** specifies measurable service levels, measurement method, reporting, remedies and review. Elements: **metric definition** (e.g. OTIF measured at the customer's dock), **target and minimum**, **measurement period and data owner**, **service credits** (penalty) for misses, **earn-back and bonus** for exceeding, **caps**, **exclusions** (force majeure, customer-caused), **root-cause and corrective-action duty**, and **continuous improvement targets**. Design cautions: too many KPIs dilute focus; penalties without cause analysis cause friction; incentives can be **gamed** (e.g. closing tickets early, manipulating cut-off times); a mix of **penalties and gain-share** is stronger than penalties alone. Link to contract types in [[002 Procurement & Strategic Sourcing]] and to risk allocation in [[137 Supply Chain Contracts & Game Theory]].

### Example
Monthly fee ₹50 lakh; OTIF target 95%; service credit 2% of fee per percentage point below target, capped at 10% of fee. Actual OTIF is 91%: shortfall = 4 points, credit = 4 × 2% × ₹50 lakh = **₹4 lakh** (below the ₹5 lakh cap). If actual were 88%: 7 points would imply ₹7 lakh, but the cap limits the credit to **₹5 lakh**. For reaching 98% or better, a bonus of 1% of fee (₹50,000) may apply, so over a year the provider's incentive is ₹6 lakh against credits at risk of ₹60 lakh.

### In the news
See news box. In any outsourced distribution network, OTIF and inventory accuracy SLAs, with credits and shared-capacity rules, are the working tools behind a headline partnership announcement.

### Interview angle
> [!question] How it is asked
> "A 3PL meets SLAs on paper but customers are unhappy. What went wrong?"

> [!tip] Strong answer includes
> - Check metric definition and measurement point (SLA vs customer experience)
> - Gaming and exclusions; unbalanced penalties
> - Align KPIs with customer-facing outcomes; add gain-share
> - Review cadence and a joint improvement plan

---
## 12. Exit Planning, Insourcing and Reshoring
> 🟠 Tier 2 · _Key points:_ Exit clauses, transition plan, step-in rights, switching costs, bringing work back

### Definition
Every outsourcing contract should be signed **with the exit in mind**. Exit planning covers: **termination triggers** (performance, insolvency, change of control, convenience with notice), **transition assistance** period and cost, **step-in rights** (buyer takes over operations temporarily), **data, tooling, documentation and IP return**, **inventory and WIP buy-back**, **knowledge transfer**, **non-solicitation** of key staff, **parallel running** and **cut-over plan**, **dual-source readiness**, and **cost of exit** estimates. **Insourcing or reshoring** (bringing work back) is considered when the supplier fails, strategic value rises, or total cost, risk or policy (tariffs, PLI) favours home production; it needs capacity, skills and investment, so treat it like a new make-vs-buy decision.

### Example
Exit cost estimate for moving an EMS assembly line to another provider: tooling and fixture transfer ₹1.5 crore, requalification (PPAP or equivalent, test, audits) ₹0.8 crore, buffer stock build for a 3-month transition (₹4 crore at 18% a year for 4 months = ₹24 lakh), parallel running 2 months at 10% premium on ₹3 crore monthly spend = ₹60 lakh, and project team ₹0.4 crore. Total = 1.5 + 0.8 + 0.24 + 0.60 + 0.4 = **₹3.54 crore** and 6 to 9 months. A supplier who knows the exit cost can demand a price rise up to the annualised exit cost (₹3.54 crore spread over a 3-year horizon = about ₹1.18 crore a year): that is the **hold-up ceiling**, which is why exit options must be created in advance.

### In the news
See news box. When a brand like Puma hands a network to a partner, the reverse path (re-taking operations or switching providers) rests on contract terms for data, systems and transition support that are agreed up front.

### Interview angle
> [!question] How it is asked
> "What clauses and plans would you put in place so you can leave an outsourcing contract?"

> [!tip] Strong answer includes
> - Termination triggers and transition assistance
> - Ownership of tooling, data, IP; step-in rights
> - Second source or internal fallback capability
> - Estimated exit cost and how it shapes bargaining power

---
## 13. ⭐ Advanced: Transaction Cost Economics, Hold-Up and Relationship-Specific Investment
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Transaction cost economics (Williamson)** explains why firms make instead of buy: markets are efficient unless transactions are plagued by **asset specificity** (investments valuable only in this relationship), **uncertainty**, and **frequency**. When a supplier invests in a dedicated tool, the buyer can **hold it up** after the investment (renegotiate price), and the supplier anticipates this, underinvesting or charging a premium. Solutions: **long-term contracts**, **buyer-financed or buyer-owned tooling**, **minimum volume guarantees**, **mutual dependence** (hostages: both invest), **reputation and repeated dealing** (keiretsu logic), **equity links**, or **vertical integration**.

A simple test: the supplier will invest only if the contract term (or guaranteed volume) pays back the specific investment:

$$\text{Payback (years)} = \frac{\text{Specific investment}}{\text{Annual contribution from the contract}}$$

If the contract is shorter than the payback, the supplier either refuses, asks for an up-front payment or prices in a premium.

### Example
Supplier must invest ₹5 crore in dedicated tooling; contribution margin ₹40 per unit on 5,00,000 units a year = ₹2 crore a year; payback = 5 / 2 = **2.5 years**. A 2-year contract is too short, so the supplier would add a premium. Options for the buyer: sign a 3-year contract with a volume floor, or **own the tooling** (₹5 crore capex, recovered in piece price over three years at roughly ₹33 per unit plus interest) so that the supplier is not locked in and can be replaced. Weigh against the risk that the supplier's capacity cannot be shared with other customers.

### In the news
See news box. Large EMS and ODM relationships involve exactly this: dedicated lines, tooling and test equipment tied to a customer's product, which is why long-term commitment, joint ventures (Dixon-Vivo, December 2024) and volume guarantees accompany them.

### Interview angle
> [!question] How it is asked
> "Why do auto OEMs often own the tooling used by suppliers?"

> [!tip] Strong answer includes
> - Asset specificity and hold-up logic
> - Payback and contract length arithmetic
> - Alternatives: volume floors, equity, long-term contracts, tooling ownership
> - Trade-off: control vs supplier flexibility and capital use
