---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Procurement & Strategic Sourcing"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 17
---
# Procurement & Strategic Sourcing

⬅ [[001 SCM Introduction & Fundamentals]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[003 Inventory Management]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Strategic Sourcing]]
2. [[#2. Make vs Buy Decision]]
3. [[#3. Vendor Selection Process]]
4. [[#4. RFQ / RFP / RFI]]
5. [[#5. Supplier Evaluation & Scorecard]]
6. [[#6. Supplier Relationship Management]]
7. [[#7. Contract Types]]
8. [[#8. Category Management]]
9. [[#9. Global Sourcing]]
10. [[#10. Procurement Cycle]]
11. [[#11. e-Procurement & P2P]]
12. [[#12. Total Cost of Ownership (TCO)]]
13. [[#13. Ethical & Sustainable Procurement]]
14. [[#14. Procurement KPIs]]
15. [[#15. Negotiation Strategies]]
16. [[#16. ⭐ Advanced: Should-Cost Modelling (Cost Breakdown Analysis)]]
17. [[#17. ⭐ Advanced: Supplier Risk Management & Multi-Sourcing]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): when a cheap, single-sourced input stops a factory
> **Nexperia chip crisis (Oct 2025).** Nexperia, a Netherlands-headquartered, Chinese-owned chipmaker, became the source of an auto-chip shortage amid US–China trade tensions and Chinese export rules on Nexperia products made in China. Honda cut output at US and Canadian plants and halted its Celaya plant in Mexico (over 190,000 vehicles produced the previous year, mainly HR-V SUVs for North America). Nissan began surveying its parts makers. ([Japan Times](https://www.japantimes.co.jp/business/2025/10/30/companies/honda-mexico-production-halt/))
> 
> **China rare-earth magnet curbs (Apr–Jun 2025).** After China suspended exports of a wide range of rare earths and related magnets in April 2025, Suzuki halted production of its Swift model at the Sagara plant in Japan (June 2025), reported as the first Japanese automaker hit; the report gave no volume figures. ([Deccan Herald / Reuters](https://www.deccanherald.com/business/companies/suzuki-motor-halted-swift-car-production-due-to-chinas-rare-earth-curbs-sources-say-3572312))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Strategic Sourcing
> 🔴 Tier 1 · _Tracker hint:_ Spend analysis, supplier market analysis, sourcing strategy

### Definition
**Strategic sourcing** is the structured, data-driven process of reducing total cost and risk by aligning what the firm buys with what the supply market can offer, rather than buying reactively item by item. A common 7-step cycle:
1. **Spend analysis**: classify all spend by category, supplier, business unit, price (the "spend cube"); find fragmentation and maverick spend.
2. **Category/requirement profiling**: demand, specifications, internal stakeholders.
3. **Supply market analysis**: number of suppliers, entry barriers, capacity, price drivers, Porter's five forces on the supply side.
4. **Sourcing strategy**: single vs multiple, local vs global, contract type, make vs buy.
5. **Supplier selection / negotiation** (RFx, auctions).
6. **Implementation / contracting**.
7. **Performance management and continuous improvement.**

Typical pattern in spend data: the **Pareto rule**: ~80% of spend sits in ~20% of suppliers, so effort goes to those.

### Example
A manufacturer's spend cube shows ₹500 cr annual spend across 1,200 suppliers; 60 suppliers hold ₹400 cr (80%). It also finds 14 suppliers selling the same packaging film at 5 different prices. Consolidating that category to 3 suppliers on a volume contract at the lowest price tier is a classic first-wave strategic-sourcing saving.

### In the news
See news box. Both disruptions were sourcing-strategy failures at the sub-tier: cheap, single-sourced inputs (a chip, magnets) that spend analysis alone did not flag as critical. Strategic sourcing must combine **spend** with **supply risk**.

### Interview angle
> [!question] How it is asked
> "How would you reduce procurement cost for a company spending ₹500 cr a year?" or "What is strategic sourcing and how is it different from purchasing?"

> [!tip] Strong answer includes
> - Spend analysis first (Pareto, category cube, price variance, maverick spend)
> - Supply market analysis and Kraljic segmentation before choosing levers
> - Levers: volume consolidation, specification standardisation, competitive bidding, TCO, demand management
> - Savings must be validated by Finance (baseline vs realised) and sustained via supplier management

---

## 2. Make vs Buy Decision
> 🔴 Tier 1 · _Tracker hint:_ TCO, core competency analysis, outsourcing risks

### Definition
Decision whether to produce an item or service in-house or procure it externally.

**Quantitative:** compare total relevant cost. If make has fixed cost $F$ and variable cost $v_m$ per unit, and buy costs $p$ per unit, break-even volume is

$$Q^* = \frac{F}{p - v_m}$$

Above $Q^*$ make is cheaper; below it, buy.

**Qualitative:** core competence (Prahalad & Hamel), strategic importance, IP protection, quality control, capacity availability, supplier capability, flexibility, lead time, regulatory needs.

**Outsourcing risks:** loss of know-how, supplier lock-in, hold-up, quality issues, hidden coordination cost, supplier becoming competitor. Transaction cost economics (Williamson): high **asset specificity** and uncertainty favour making.

### Example
Make: fixed ₹2,00,000 per year (tooling) + ₹40 per unit. Buy: ₹60 per unit. $Q^* = 2{,}00{,}000 / (60-40) = 10{,}000$ units. At 15,000 units: make = 2,00,000 + 6,00,000 = ₹8,00,000; buy = ₹9,00,000, so make saves ₹1,00,000. At 6,000 units buy is cheaper (₹3.6 lakh vs ₹4.4 lakh).

### In the news
See news box. Apple-style "outsource assembly, keep design" works until the outsourced chain has a hidden single point of failure; make-or-buy must include *where* the supplier's own inputs come from.

### Interview angle
> [!question] How it is asked
> "Should an auto-component firm make or buy a part?" or "Why did Boeing/Apple outsource, and when does it backfire?"

> [!tip] Strong answer includes
> - Break-even maths and what the fixed costs include (capex, people, capacity opportunity cost)
> - Core vs non-core, and asset specificity
> - Risk factors: lock-in, IP, supplier capability, capacity flexibility
> - Hybrid options: dual (make + buy), joint venture, long-term contract

---

## 3. Vendor Selection Process
> 🔴 Tier 1 · _Tracker hint:_ Criteria: cost, quality, delivery, capacity, reliability

### Definition
A funnel from many potential suppliers to a short list and a final award.
1. Define requirements and criteria (specs, volumes, service).
2. Identify long list (market research, referrals, directories, RFI).
3. Pre-qualify (financial health, certifications such as ISO 9001/IATF 16949, capacity, compliance).
4. Issue RFQ/RFP; collect bids.
5. Evaluate with a weighted scoring model; site audit; samples/trial lots.
6. Negotiate and award; sign contract and onboard.

Core criteria: **Quality, Cost (TCO not just price), Delivery/lead time, Capacity and flexibility, Reliability/financial stability, Technology/innovation, Service, Risk and ESG compliance.** Methods: weighted point method, categorical method, AHP, cost-ratio method.

### Example
Criteria weights: price 30%, quality 30%, delivery 20%, financial stability 10%, ESG 10%. Vendor X scores (out of 10): 8, 9, 7, 6, 7 gives 2.4 + 2.7 + 1.4 + 0.6 + 0.7 = **7.8**. Vendor Y scores 9, 6, 8, 8, 6 gives 2.7 + 1.8 + 1.6 + 0.8 + 0.6 = **7.5**. X wins despite higher price.

### In the news
See news box. After Nexperia and rare earths, "sub-tier visibility" and geographic concentration have become explicit selection criteria.

### Interview angle
> [!question] How it is asked
> "How would you select a supplier for a critical component?"

> [!tip] Strong answer includes
> - Staged process (long list → pre-qualify → RFQ → audit → award)
> - Weighted criteria with weights chosen from the item's criticality (Kraljic)
> - TCO and risk, not only price
> - Pilot order or trial before full award; dual-source for critical items

---

## 4. RFQ / RFP / RFI
> 🔴 Tier 1 · _Tracker hint:_ Definitions, when to use each, evaluation scoring

### Definition
| Document | Purpose | When to use | Evaluation |
|---|---|---|---|
| **RFI** (Request for Information) | Learn what suppliers can do; build long list | Early, unfamiliar market, unclear solution | Not scored for award; screening |
| **RFQ** (Request for Quotation) | Get price and terms for a **clearly specified** item | Standardised, well-defined needs | Mainly price, delivery, terms (lowest compliant bid) |
| **RFP** (Request for Proposal) | Get a **solution** plus price for complex needs | Services, systems, custom solutions | Weighted scoring: technical (e.g. 60-70%) and commercial (30-40%) |

(RFT/tender is the formal public-sector variant; India's GeM portal and CPPP use it.) Good practice: clear scope and SLAs, same information to all bidders, fixed deadline, Q&A round, transparent scoring criteria, two-envelope (technical then commercial) bidding.

### Example
RFP for a warehouse management system: technical score weight 70%, commercial 30%. Bidder A technical 85, price score 70 gives 0.7×85 + 0.3×70 = 59.5 + 21 = **80.5**. Bidder B technical 75, price score 95 gives 52.5 + 28.5 = **81.0**. B wins narrowly; a 5-point swing in weighting would change that, so weights must be fixed before opening bids. (Price score often = lowest price / bidder price × 100.)

### In the news
See news box. Firms restarting sourcing for alternative chips/magnets typically begin with RFIs to discover who can qualify quickly, then RFQs for approved parts.

### Interview angle
> [!question] How it is asked
> "What is the difference between RFQ, RFP and RFI, and when do you use each?"

> [!tip] Strong answer includes
> - One-line distinction: information vs price for a spec vs solution + price
> - Weighted scoring with weights set before bids open
> - Two-envelope technical/commercial approach
> - Ensuring fair, auditable process (important in PSUs and GeM)

---

## 5. Supplier Evaluation & Scorecard
> 🔴 Tier 1 · _Tracker hint:_ Weighted scoring, KPIs: lead time, defect rate, OTD

### Definition
A **supplier scorecard** measures actual performance periodically (monthly/quarterly) against agreed targets, and feeds reviews, business allocation and development.

Typical KPIs and formulas:
- **On-time delivery (OTD)** = orders delivered on or before promised date / total orders.
- **Quality / defect rate** = defective units / units received; often in **PPM** = defects / units × 10⁶.
- **Lead time** (average and variability).
- **Cost**: price variance, cost-reduction delivered.
- **Responsiveness, corrective-action closure time, compliance.**

Composite score = $\sum w_i \times s_i$ with $\sum w_i = 1$. Typical bands: preferred, approved, conditional/probation, disqualified.

### Example
Weights: cost 30%, quality 25%, delivery 25%, service 20%. Supplier A scores 8, 7, 9, 6: 2.4 + 1.75 + 2.25 + 1.2 = **7.6**. Supplier B scores 9, 6, 7, 8: 2.7 + 1.5 + 1.75 + 1.6 = **7.55**. Nearly equal; but if quality is a gate (minimum score 7), B fails on quality despite a similar total.

### In the news
See news box. Scorecards measure what is visible; the Nexperia shortage came from a risk dimension (ownership, geography, sub-tier) that most scorecards omit. Add a risk score.

### Interview angle
> [!question] How it is asked
> "How do you measure supplier performance?" or "A supplier's OTD fell to 80%. What do you do?"

> [!tip] Strong answer includes
> - KPIs across quality, cost, delivery, service (plus risk/ESG)
> - Weights tied to category importance; minimum thresholds on critical KPIs
> - Review cadence and action ladder (corrective action, probation, share shifting)
> - Root-cause on the OTD drop (lead time, capacity, our own forecast changes) before blaming the supplier

---

## 6. Supplier Relationship Management
> 🔴 Tier 1 · _Tracker hint:_ SRM tiers, partnership models, development programs

### Definition
SRM is the discipline of managing interactions with suppliers to extract more value than a transaction would. Segment suppliers (often by Kraljic quadrant and spend/risk) and match the relationship:

| Tier | Relationship | Typical |
|---|---|---|
| Strategic partner | Joint planning, co-development, shared KPIs, long-term contracts | Few; critical, hard to replace |
| Preferred | Regular reviews, volume commitments | Leverage-category key suppliers |
| Approved / transactional | Competitive bids, e-catalogues | Non-critical items |

Partnership models: arm's-length, long-term contract, preferred-supplier, strategic alliance, JV, **keiretsu** (Toyota-style). **Supplier development** programs: training, joint kaizen, quality support, financing (supply-chain finance). Risks: dependence, complacency, information leakage.

### Example
Toyota's supplier associations and joint improvement teams trained suppliers in the Toyota Production System; Indian OEMs and tier-1s run similar vendor-development programs. A retailer running a supply-chain-finance programme lets small suppliers get paid early at the retailer's lower borrowing rate while the retailer extends payment terms.

### In the news
See news box. Honda/Suzuki cases show relationship depth matters in a shortage: suppliers allocate scarce chips and magnets to customers they treat as strategic.

### Interview angle
> [!question] How it is asked
> "How would you build a closer relationship with your top 5 suppliers?"

> [!tip] Strong answer includes
> - Segmentation first, then differentiate effort
> - Mechanisms: joint business plans, shared forecasts, supplier development, executive sponsorship
> - Governance: QBRs, scorecards, escalation path
> - Hedge dependence: second source, contract clauses, inventory

---

## 7. Contract Types
> 🔴 Tier 1 · _Tracker hint:_ Fixed price, cost-plus, time-and-material, frame agreements

### Definition
| Contract | Price basis | Risk bearer | Use |
|---|---|---|---|
| **Fixed price (lump sum)** | Agreed total or unit price | Supplier (cost overruns) | Well-defined scope, stable specs |
| **Cost-plus** (cost + fee or % margin) | Actual cost + margin | Buyer | Uncertain scope, R&D, defence; needs audit; weak cost incentive |
| **Time & Material (T&M)** | Hourly/daily rates × effort + materials | Buyer | IT services, maintenance; scope unclear |
| **Frame / blanket / rate contract** | Pre-agreed price and terms, call-offs by releases | Shared | Repeat purchases; volume commitments |
| **Incentive / gain-share** | Target cost with sharing of savings/overruns | Shared | Align incentives |

Also: take-or-pay, index-linked price (steel, crude), SLA-based, performance-based. Key clauses: price revision, liquidated damages, force majeure, IP, termination, audit.

### Example
Frame agreement: 12-month rate contract for 1,20,000 packaging cartons at ₹18 each with monthly releases of 10,000 and price indexed to kraft paper above ±5%. Cost-plus: actual cost ₹1 cr + 10% fee = ₹1.10 cr; weakness: supplier earns more as cost rises (fee as % of cost), so many buyers prefer fixed fee.

### In the news
See news box. In a shortage, contracts with firm capacity reservation or allocation clauses are worth far more than price discounts.

### Interview angle
> [!question] How it is asked
> "Which contract type would you use for a new product where the scope is unclear?"

> [!tip] Strong answer includes
> - Match contract to uncertainty: fixed for known scope, T&M/cost-plus for unknown, incentive for shared risk
> - Who bears risk and what behaviour each induces
> - Frame agreements for repeat items, with volume bands and price indexation
> - Protective clauses (SLA, penalty, exit)

---

## 8. Category Management
> 🔴 Tier 1 · _Tracker hint:_ Spend categorization, kraljic matrix (leverage/strategic/bottleneck/non-critical)

### Definition
Category management groups similar spend into **categories** managed by a dedicated team with its own strategy. **Kraljic matrix (1983)** positions items on **supply risk** (x) vs **profit impact / spend** (y):

| | Low supply risk | High supply risk |
|---|---|---|
| **High profit impact** | **Leverage**: competitive bidding, volume consolidation, switch suppliers | **Strategic**: partnerships, long-term contracts, joint development, dual-source if possible |
| **Low profit impact** | **Non-critical (routine)**: automate, e-catalogue, reduce transactions, P-card | **Bottleneck**: secure supply, safety stock, find substitutes, supplier development |

Process: classify spend, build category strategy, set targets, execute, review. The retail version (shelf, assortment, planogram) is a related use of the term.

### Example
For an EV maker: battery cells and rare-earth magnets = **strategic**; steel sheets, packaging = **leverage**; office stationery, housekeeping = **non-critical**; a single-source specialty sensor or a spare for an old press = **bottleneck**.

### In the news
See news box. Nexperia chips and rare-earth magnets looked low-value (low profit impact) but behaved as **bottleneck** items: high supply risk, plant-stopping consequences.

### Interview angle
> [!question] How it is asked
> "Explain the Kraljic matrix with examples" or "How would you segment 10,000 suppliers?"

> [!tip] Strong answer includes
> - Axes correctly labelled and four quadrants with strategies
> - Examples from the company's own context
> - Caveat: cheap items can be bottleneck items; re-classify as markets move
> - Link to resources: spend management effort proportional to impact

---

## 9. Global Sourcing
> 🔴 Tier 1 · _Tracker hint:_ Advantages, risks (currency, geopolitics), near-shoring

### Definition
Buying from suppliers across borders to gain cost, capability, capacity or access to technology.

**Advantages:** lower unit price, scale, specialised capability, supplier competition.
**Risks:** currency, longer lead times and higher safety stock, transport cost and disruption, tariffs/duties, geopolitics, IP, quality, language/culture, ESG compliance.

**Landed cost** = FOB price + freight + insurance + customs duty + clearing/handling + inventory carrying cost (+ non-recoverable taxes). Strategies: **near-shoring** (neighbouring/regional countries), **re-shoring**, **friend-shoring**, **China+1**, dual sourcing, local-for-local.

### Example
Imported part: FOB $10, freight and insurance $1, so CIF = $11; duty 10% of CIF = $1.10; landed = $12.10. At ₹84/$, **₹1,016.40** against a domestic quote of ₹1,050. But add 8 weeks extra transit: if holding cost is 20% a year, 8 weeks on ₹1,016 is about ₹31 more, leaving a thin advantage; a 5% rupee fall would flip it.

### In the news
See news box. Concentration of rare-earth magnets and chips in China is the textbook risk of global sourcing; many firms now run China+1.

### Interview angle
> [!question] How it is asked
> "Should the company source from China or India? Evaluate."

> [!tip] Strong answer includes
> - Landed cost, not price; include lead-time inventory and duty
> - Risk list: FX, geopolitical, disruption, quality, compliance
> - Mitigation: dual sourcing, near-shoring, hedging, safety stock, local partner
> - Decision tied to item type (strategic vs commodity)

---

## 10. Procurement Cycle
> 🔴 Tier 1 · _Tracker hint:_ Need identification → PR → PO → GRN → Invoice → Payment

### Definition
The operational flow of one purchase:
1. **Need identification** (MRP or user demand) and specification.
2. **Purchase Requisition (PR)**: internal request, approved by budget holder.
3. Source determination: RFQ, quotation comparison, supplier selection.
4. **Purchase Order (PO)**: legal commitment to supplier.
5. Order confirmation, expediting.
6. **Goods Receipt Note (GRN)**: quantity and quality check at receipt (and inspection).
7. **Invoice verification**: **three-way match** of PO, GRN and invoice.
8. **Payment** per terms (e.g. net 45), then reconciliation and records.

Controls: segregation of duties, approval limits, tolerance limits for the match. A **two-way match** compares PO and invoice only (used for services).

### Example
PO: 100 units at ₹50 = ₹5,000. GRN: 98 units accepted (2 rejected). Invoice: 100 units at ₹50 = ₹5,000. Three-way match fails on quantity; payment is limited to 98 × 50 = **₹4,900** and a debit note raised for the ₹100 difference.

### In the news
See news box. Under shortages, expediting and PO re-prioritisation become the daily work of procurement teams; clean PO data and supplier confirmations give early warning.

### Interview angle
> [!question] How it is asked
> "Walk me through the procure-to-pay process" or "What are the controls to prevent fraud in purchasing?"

> [!tip] Strong answer includes
> - Correct order: PR → PO → GRN → invoice → payment
> - Three-way match and why
> - Controls: approvals, segregation of duties, vendor master hygiene
> - Where it is slow and how e-procurement shortens PO cycle time

---

## 11. e-Procurement & P2P
> 🔴 Tier 1 · _Tracker hint:_ SAP MM, reverse auctions, e-catalogues, purchase-to-pay

### Definition
**e-Procurement** uses digital platforms for sourcing and buying: e-tendering, **reverse auctions** (suppliers bid prices down in real time), **e-catalogues** (pre-negotiated items ordered online), supplier portals, e-invoicing. **P2P (Purchase-to-Pay)** covers the whole flow from requisition to payment. Benefits: speed, compliance (less maverick spend), transparency, data for analysis, lower transaction cost. Risks: reverse auctions damage relationships and can squeeze quality; only suitable for commodity-like, well-specified items. India: **GeM** (Government e-Marketplace) for public buying.

**SAP MM T-codes (classic ECC / S/4):**
```
ME51N  Create purchase requisition      ME21N  Create purchase order
ME41   Create RFQ                       ME47   Maintain quotation
ME49   Price comparison                 ME23N  Display purchase order
MIGO   Goods receipt / movement         MIRO   Enter incoming invoice
MM01   Create material master           ME2N   PO list by document number
```
In S/4HANA vendors are maintained as Business Partners (T-code **BP**); older ECC used XK01/MK01.

### Example
A reverse auction for 50,000 kg of packaging film: opening bid ₹100/kg, final winning bid ₹88/kg, i.e. 12% reduction, worth ₹6 lakh on that volume (12 × 50,000). Caveat: if quality specs were loose, the saving may leak back as defects.

### In the news
See news box. Digital P2P data (open POs by sub-supplier) is how firms trace exposure to a Nexperia-type shock; those without it spent days calling suppliers.

### Interview angle
> [!question] How it is asked
> "What is a reverse auction and when would you not use it?" or "Which SAP modules/T-codes do you know for procurement?"

> [!tip] Strong answer includes
> - e-sourcing vs e-ordering vs full P2P
> - Reverse auction pros and cons; best for commodities with clear specs
> - T-codes: ME51N, ME21N, MIGO, MIRO (as above) and three-way match
> - Impact metrics: PO cycle time, % spend under contract, touchless invoices

---

## 12. Total Cost of Ownership (TCO)
> 🔴 Tier 1 · _Tracker hint:_ Price + transport + inventory + quality + risk costs

### Definition
TCO captures all costs of acquiring, owning and using an item, not just price:

$$TCO = \text{Price} + \text{Acquisition (ordering, transport, duty)} + \text{Ownership (inventory, handling, quality, warranty, downtime)} + \text{Post-use (disposal)} + \text{Risk cost}$$

Techniques: cost-ratio method, total-landed-cost model, life-cycle costing (for capital goods, include energy and maintenance, and discount to NPV). The *iceberg* picture: price is the visible tip. TCO helps in make-vs-buy, supplier selection, and local-vs-global sourcing.

### Example
Per unit: Supplier A: price 100, transport 3, quality cost 1, inventory carrying 2 = **106**. Supplier B (lower price): price 92, transport 6 (far), quality cost 4 (more rework), inventory 5 (longer lead time) = **107**. B looks 8% cheaper on price but is 1 unit costlier on TCO.

### In the news
See news box. A "risk cost" line (expected loss from stoppage = probability × impact) is exactly what was missing for single-sourced chips and magnets.

### Interview angle
> [!question] How it is asked
> "Supplier A is 10% cheaper. Should we switch?"

> [!tip] Strong answer includes
> - Ask for full cost elements: freight, duty, inventory, quality, payment terms, risk
> - Compute TCO with numbers, show the crossover
> - Include qualitative factors (capacity, relationship)
> - Recommend a pilot or dual-sourcing if uncertain

---

## 13. Ethical & Sustainable Procurement
> 🔴 Tier 1 · _Tracker hint:_ ESG criteria, code of conduct, conflict minerals

### Definition
Buying in a way that considers human rights, labour conditions, environment and governance across the supply base. Tools: **Supplier Code of Conduct**, ESG questionnaires and audits (SA8000, ISO 14001, SMETA), risk screening, traceability, supplier development, and exit for severe breaches.

**Conflict minerals** = the 3TG: tin, tantalum, tungsten and gold from conflict-affected areas (e.g. DRC and neighbours); US Dodd-Frank Act Section 1502 requires reporting by listed US firms; the EU has its own regulation. Other topics: child/forced labour, modern slavery, deforestation (palm oil), Scope 3 emissions (purchased goods are often the largest part of a firm's footprint). In India, SEBI's **BRSR** reporting pushes listed companies to disclose value-chain sustainability information.

### Example
An Indian apparel exporter must show EU buyers that its cotton and its sub-contracted units meet labour and chemical standards; a failed audit can end the account. A consumer-electronics firm maps tantalum capacitors back to smelters to certify conflict-free sourcing.

### In the news
See news box. Resilience and ethics converge: concentrated, opaque sub-tier supply is both an ESG and a continuity risk. (No separate statistic is cited here.)

### Interview angle
> [!question] How it is asked
> "How do you ensure your suppliers are ethical?" or "What are conflict minerals?"

> [!tip] Strong answer includes
> - Code of conduct plus audits plus corrective-action plans (not just paperwork)
> - Risk-based approach: audit high-risk categories/geographies first
> - Traceability to sub-tier; certification
> - Trade-off with cost and how to price it (TCO/risk)

---

## 14. Procurement KPIs
> 🔴 Tier 1 · _Tracker hint:_ Cost savings %, supplier OTD%, PO cycle time, maverick spend%

### Definition
| KPI | Formula / meaning |
|---|---|
| **Cost savings %** | (Baseline price − new price) × volume / baseline spend |
| **Spend under management** | Spend with contracts or managed categories / total spend |
| **Supplier OTD %** | On-time deliveries / total deliveries |
| **PO cycle time** | PR approval to PO issue (or PO to receipt) |
| **Maverick (off-contract) spend %** | Spend outside approved contracts or processes / total spend |
| **Supplier quality PPM** | Defects per million received |
| **Procurement ROI** | Savings / procurement operating cost |
| **Days Payable Outstanding (DPO)** | Payables / COGS × 365 |

Distinguish **hard savings** (price reduction, visible in P&L), **cost avoidance** (prevented increase) and **soft savings**.

### Example
Baseline price ₹100, negotiated ₹94, volume 10,000 units: saving = 6 × 10,000 = ₹60,000 on baseline spend of ₹10,00,000 = **6%**. Maverick spend: ₹12 cr of total ₹80 cr outside contracts = **15%**.

### In the news
See news box. After shortages, KPIs like "% critical parts with qualified second source" and "supplier lead-time variability" are being added to dashboards (as a practice, not a sourced statistic).

### Interview angle
> [!question] How it is asked
> "What KPIs would you set for a procurement team?"

> [!tip] Strong answer includes
> - Balanced set: cost, quality, delivery, process efficiency, compliance, risk
> - Define baselines and distinguish hard vs soft savings
> - Beware gaming (cheapest price hurting quality)
> - Link to business outcomes (working capital, service level)

---

## 15. Negotiation Strategies
> 🔴 Tier 1 · _Tracker hint:_ BATNA, ZOPA, win-win vs win-lose, anchoring

### Definition
- **BATNA** (Best Alternative To a Negotiated Agreement, Fisher & Ury): your walk-away option; the stronger it is, the more power you have.
- **Reservation price**: worst acceptable deal. **ZOPA** (Zone of Possible Agreement): overlap between buyer's maximum and seller's minimum; no overlap, no deal.
- **Distributive (win-lose)** negotiation divides a fixed pie; **integrative (win-win)** expands it by trading across issues (price vs volume vs payment terms vs lead time).
- **Anchoring**: first number sets the reference; make the first offer when you have good information. Other tactics: concessions in decreasing size, packaging issues, silence, good-cop/bad-cop (recognise, don't fall for).

Preparation: know your BATNA and theirs, costs (should-cost), interests, and concessions.

### Example
Buyer's maximum price ₹110; seller's minimum ₹95. ZOPA = ₹95-110. If the buyer opens at ₹90 (anchor below), settlement likely lands around ₹100. Integrative trade: buyer accepts ₹102 but offers a 12-month volume commitment and payment in 30 days instead of 60, valuable to the seller.

### In the news
See news box. Buyers with no alternative source (weak BATNA) had no leverage when suppliers allocated scarce chips and magnets; BATNA building (second source) is a prerequisite to negotiation.

### Interview angle
> [!question] How it is asked
> "How would you negotiate a 10% price cut with a key supplier?"

> [!tip] Strong answer includes
> - Preparation: BATNA, should-cost, supplier's interests
> - Mix of levers: volume, term, payment, specification, shared savings
> - Win-win framing for strategic partners; competitive tension for leverage items
> - Know when to walk away

---

## 16. ⭐ Advanced: Should-Cost Modelling (Cost Breakdown Analysis)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Should-cost analysis** builds a bottom-up estimate of what an item *should* cost given materials, process, labour, overhead and a fair margin, rather than relying on supplier quotes or market prices. Elements:
- Material (weight × price + scrap/yield loss)
- Conversion: machine hours × machine rate + labour hours × labour rate
- Overheads, tooling amortisation, logistics, SG&A
- Supplier margin (benchmark e.g. 8-12%)

Uses: negotiation fact base, challenging cost-plus claims, **index-linked pricing** (price tied to steel/aluminium index), and design-to-cost with engineering (VA/VE: value analysis and engineering). Used heavily by auto OEMs and consulting cost-transformation work.

### Example
Machined bracket: material ₹40 (including scrap), labour ₹8, machine and overheads ₹12, subtotal ₹60; margin 10% = ₹6; **should-cost = ₹66**. Supplier's quote ₹78; the gap is ₹12 (about 15.4% of the quote). Negotiation agenda: challenge scrap rate, machine rate and margin line by line, not just ask for a "10% discount".

### In the news
See news box. As input prices (rare-earths, chips) became volatile, buyers moved to index-linked contracts and should-cost transparency to agree fair pass-through. (General practice; no statistic cited.)

### Interview angle
> [!question] How it is asked
> "A supplier quotes ₹78. How do you know whether that is fair?"

> [!tip] Strong answer includes
> - Build cost model: material, conversion, overhead, margin
> - Benchmark rates and yield; use commodity indices
> - Use model to structure negotiation and spot design-to-cost levers
> - Caveat: validate assumptions with engineering and, where possible, open-book costing

---

## 17. ⭐ Advanced: Supplier Risk Management & Multi-Sourcing
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Systematically identify, assess and mitigate supply risk. Steps:
1. **Map** the network to tier-2/3 (who makes the inputs to your supplier).
2. **Assess** risk = probability × impact; rank by a risk-criticality matrix (impact on revenue, recovery time / **time-to-recover (TTR)** vs **time-to-survive (TTS)**).
3. **Mitigate**: dual/multi-sourcing, qualified alternates, safety stock for bottleneck items, long-term capacity reservation, design flexibility (common parts), geographic diversification (China+1), supplier financial monitoring, insurance.
4. **Monitor** with early-warning signals (news, financial health, port congestion).

**Single vs dual sourcing trade-off:** single gives volume leverage and partnership; dual gives resilience and competition. Typical split for critical parts: 70/30 or 80/20, with the second source kept "warm" by regular orders.

### Example
A firm loses ₹4 crore a day when a line stops. A buffer of 20 days' stock costs: ₹10 cr inventory × 12% holding = ₹1.2 cr a year. If the supplier risk is 5% a year of a 15-day outage = 0.05 × 15 × ₹4 cr = ₹3 cr expected loss, buffer/second source is justified.

### In the news
See news box. Both Nexperia and rare-earth events exposed single-point dependencies and sparked sub-tier mapping and strategic stock programmes.

### Interview angle
> [!question] How it is asked
> "How would you make our supply base more resilient without doubling costs?"

> [!tip] Strong answer includes
> - Segment first: protect critical (bottleneck/strategic) items only
> - Visibility to tier-2/3; TTR vs TTS logic
> - Mix of levers: dual source, buffer, design standardisation, contracts
> - Quantify expected loss vs cost of mitigation

---
## 🔗 Go deeper: expansion notes
- [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)|Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]
- [[122 Spend Analysis, Savings & Procurement Maturity|Spend Analysis, Savings & Procurement Maturity]]
- [[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms|Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]
- [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies|Outsourcing, Supplier Partnerships & Kraljic Strategies]]
