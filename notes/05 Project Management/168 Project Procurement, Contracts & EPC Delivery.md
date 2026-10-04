---
tags: [project-management, tier2]
area: Project Management
topic: "Project Procurement, Contracts & EPC Delivery"
tier: Tier 2
roles: Project Manager / Operations
status: complete
subtopics: 14
---
# Project Procurement, Contracts & EPC Delivery

⬅ [[042 Cost & Budget Management]] · [[_Index - Project Management|Project Management]] · [[169 Project Team Leadership, Conflict & Team Development]] ➡

> **Area:** Project Management · **Priority:** 🟠 Tier 2 · **Target roles:** Project Manager / Operations

## Sub-topics in this note
1. [[#1. Procurement Management Process and Make-or-Buy]]
2. [[#2. Procurement Planning: SOW, Solicitation Documents and Selection Criteria]]
3. [[#3. Fixed-Price Contracts: FFP, FPIF and Economic Price Adjustment]]
4. [[#4. Cost-Reimbursable and Time & Materials Contracts]]
5. [[#5. Delivery Models: Design-Bid-Build, Design-Build, EPC/Turnkey, EPCM and PMC]]
6. [[#6. PPP in Indian Infrastructure: BOT, HAM, TOT and Concessions]]
7. [[#7. FIDIC Contract Basics]]
8. [[#8. Bid Evaluation and Source Selection]]
9. [[#9. Risk Allocation and Incentive Design in Contracts]]
10. [[#10. Claims, Variation Orders, Extension of Time and Liquidated Damages]]
11. [[#11. Vendor and Contractor Performance Management]]
12. [[#12. Procurement Closure and Lessons Learned]]
13. [[#13. Lessons from Megaprojects: Cost-Overrun Statistics and Their Causes]]
14. [[#14. ⭐ Advanced: Alliancing, Reference Classes and Claims Avoidance]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's central projects and the price of weak contracting
> **MoSPI infrastructure report (July 2026 data).** Across **1,775 central-sector projects costing ₹150 crore or more**, the cumulative cost overrun was **₹3,40,504 crore**: original cost ₹33,70,138 crore against revised cost ₹37,10,642 crore, about **10.1%** above plan (calculated: 340,504 / 3,370,138). Spending to date was ₹19.26 lakh crore, or 51.91% of revised cost. Transport and logistics accounted for 1,246 projects (70% of the total, ₹19.81 lakh crore); the Ministry of Road Transport and Highways alone had 993 projects worth ₹9.62 lakh crore, and Railways 190 projects worth ₹6.38 lakh crore. 675 projects (38%) had crossed 80% physical completion. The report did not say how many individual projects overran or give time-overrun detail. ([Swarajya](https://swarajyamag.com/news-brief/indias-1775-central-infrastructure-projects-face-rs-34-lakh-crore-cost-overrun))
>
> **Megaproject benchmark (Flyvbjerg).** Using a database of about **16,000 projects**, Bent Flyvbjerg reports that only around **0.5%** deliver on budget, on schedule and with the promised benefits, the basis of his "iron law of megaprojects" (over budget, over time, under benefits, over and over again), popularised in *How Big Things Get Done* (2023). ([Wikipedia: Bent Flyvbjerg](https://en.wikipedia.org/wiki/Bent_Flyvbjerg))
>
> **FIDIC contract suite.** FIDIC's Red, Yellow and Silver books (employer-designed works, design-build, and EPC/turnkey) were revised in **second editions in 2017**; the Silver Book is the standard for EPC/turnkey. ([Wikipedia: FIDIC](https://en.wikipedia.org/wiki/FIDIC))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Procurement Management Process and Make-or-Buy
> 🟠 Tier 2 · _Key points:_ Plan, conduct, control, close; make-or-buy break-even; sourcing strategy

### Definition
Project procurement management covers acquiring goods, services and results from outside the team. PMBOK-style processes: **plan procurement** (what to buy, make-or-buy, strategy, documents, selection criteria), **conduct procurement** (solicit, evaluate, award), **control procurement** (administer contracts, monitor performance, manage changes and claims) and **close procurement** (final acceptance, settle claims, records). See [[038 PMBOK Knowledge Areas]] and [[037 PM Fundamentals & Lifecycle]].

**Make-or-buy analysis** compares internal production with external purchase on cost, capability, capacity, quality, risk, control, intellectual property, strategic importance and time. Break-even volume where internal fixed cost $F$ and variable cost $v$ equal the supplier price $b$ per unit:

$$Q^{*} = \frac{F}{b - v}$$

Beyond $Q^{*}$ making is cheaper (if $b > v$). Qualitative factors can override: keep **core competencies** in-house, buy commodities; consider flexibility, supplier risk and learning curve (see [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]] and [[002 Procurement & Strategic Sourcing]]). Outputs: procurement management plan, make-or-buy decisions, procurement strategy (delivery method, contract type, phasing), bid documents, source selection criteria, independent cost estimates.

### Example
Precast concrete units for a warehouse project: in-house casting yard needs ₹12,00,000 fixed set-up and ₹180 per unit variable; a supplier quotes ₹260 per unit. Break-even $Q^{*} = 12{,}00{,}000/(260-180) = 15{,}000$ units. At 10,000 units: make ₹30,00,000 vs buy ₹26,00,000, so buy; at 20,000 units: make ₹48,00,000 vs buy ₹52,00,000, so make saves ₹4,00,000. If the project needs only 10,000 units, buy, unless supplier reliability or quality is a concern.

### In the news
See news box. With overruns averaging about 10% on central projects, procurement choices (who carries which risk) are among the biggest controllable drivers.

### Interview angle
> [!question] How it is asked
> "How do you decide whether to do work in-house or outsource it on a project?"

> [!tip] Strong answer includes
> - Break-even calculation with fixed and variable costs
> - Qualitative criteria: core competency, risk, control, capacity, time
> - Links to contract type and risk allocation
> - Supplier market readiness and fallback plan

---

## 2. Procurement Planning: SOW, Solicitation Documents and Selection Criteria
> 🟠 Tier 2 · _Key points:_ SOW, RFI/RFQ/RFP/EOI, prequalification, evaluation criteria set before bids open

### Definition
- **Statement of Work (SOW) / scope of supply:** a clear, complete description of what is to be delivered (deliverables, specifications, standards, interfaces, acceptance criteria). For works: **drawings, technical specifications, Bill of Quantities (BoQ)**. Ambiguity here is the main source of later claims.
- **Solicitation documents:** **RFI** (request for information, market sounding), **EOI / prequalification** (shortlist capable bidders), **RFQ** (price for well-defined items), **RFP** (proposal with technical and commercial offer for complex scope), **tender / bid documents** with instructions to bidders, general and special conditions, specifications, forms and bid security.
- **Source selection criteria** (decided before bids open): technical capability and experience, financial strength, past performance, schedule, price, HSE, local content, compliance. Evaluate **technical first**, then price, and keep them in separate envelopes (**two-bid system**).
- **Independent cost estimate (ICE)** as a benchmark for evaluating price and spotting abnormally low or high bids.
- **Procurement schedule** aligned with the project schedule: long-lead items (transformers, turbines, structural steel) start early; see [[039 Scheduling Tools (CPM-PERT-Gantt)]].
- **Contract packaging:** one EPC package vs multiple packages (civil, mechanical, electrical): fewer interfaces vs more competition and flexibility.
- **Public procurement in India:** the General Financial Rules 2017, Manual for Procurement of Works (Department of Expenditure), Central Vigilance Commission guidelines, **GeM** (Government e-Marketplace) for goods and services, e-tendering portals, and Make in India preference orders. Principles: transparency, competition, fairness, accountability. (Details and thresholds change; check the current manual.)

### Example
Package plan for a ₹300 crore cold-chain hub: Package A civil and structure (EPC, ₹140 crore), Package B refrigeration plant (supply-install, ₹95 crore), Package C racking and automation (₹45 crore), Package D electrical and utilities (₹20 crore). The refrigeration compressors have a 36-week lead time, so Package B is tendered first; with a 60-week project, award by week 8 keeps delivery on the critical path. Splitting adds interface risk (a coordination cost that an EPC wrap would have shifted to one contractor at a premium of, say, 4-6%).

### In the news
See news box. A cleaner, more complete scope at tender is a direct lever against variation orders, a major source of cost growth.

### Interview angle
> [!question] How it is asked
> "What is the difference between RFI, RFQ and RFP, and when would you use each?"

> [!tip] Strong answer includes
> - Correct definitions and purpose of each document
> - Prequalification and two-envelope evaluation, criteria fixed before opening bids
> - Scope clarity as the root of claim avoidance
> - Package and sequencing logic with lead times

---

## 3. Fixed-Price Contracts: FFP, FPIF and Economic Price Adjustment
> 🟠 Tier 2 · _Key points:_ Firm fixed price, fixed price incentive with share ratio, ceiling and point of total assumption, EPA

### Definition
**Fixed-price (lump-sum) contracts** set a price for a defined scope; the **seller bears cost risk**, the buyer bears scope-definition risk (changes cost extra).

- **Firm Fixed Price (FFP):** price fixed regardless of actual cost. Simple; best when scope is well defined and stable.
- **Fixed Price Incentive Fee (FPIF):** a target cost, target profit (fee), **sharing ratio** (buyer:seller) for under-/overruns, and a **ceiling price**. The **Point of Total Assumption (PTA)** is the cost beyond which the seller bears 100% of overruns:
$$\text{PTA} = \frac{\text{Ceiling price} - \text{Target price}}{\text{Buyer's share}} + \text{Target cost}$$
- **Fixed Price with Economic Price Adjustment (FP-EPA):** price adjusts for specified index movements (steel, cement, diesel, labour, forex) for long contracts; in India price-variation clauses commonly reference **WPI or CPI indices** for components. See [[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]].
- **Purchase order** for simple items.

Use when scope and design are mature; the seller's price includes a **risk premium**, and the temptation to cut quality or chase variations rises as the contract becomes unprofitable.

### Example
FPIF (all in ₹ crore): target cost 100, target fee 10, target price 110, ceiling price 125, sharing ratio **80/20** (buyer 80%, seller 20%).

| Actual cost | Cost over/(under) target | Seller's fee | Price paid | Note |
|---|---|---|---|---|
| 90 | −10 | 10 + 0.2×10 = **12.0** | 102.0 | seller shares savings |
| 100 | 0 | 10.0 | 110.0 | target |
| 115 | +15 | 10 − 0.2×15 = **7.0** | 122.0 | seller shares overrun |
| 118.75 | +18.75 | 6.25 | **125.0** | = ceiling, PTA reached |
| 125 | +25 | would be 5.0 → price 130, capped | 125.0 | seller fee zero |
| 130 | +30 | | 125.0 | seller loses **5** |

PTA = (125 − 110)/0.8 + 100 = **118.75**. Beyond that cost, the seller carries every extra rupee. An FFP at ₹110 crore with actual cost ₹115 crore would leave the seller with a ₹5 crore loss and none of this sharing.

### In the news
See news box. Fixed-price EPC with unclear scope or ground conditions is where overruns turn into disputes and abandoned sites.

### Interview angle
> [!question] How it is asked
> "Explain FPIF with an example. What is the point of total assumption?"

> [!tip] Strong answer includes
> - Target cost, target fee, share ratio, ceiling
> - Computes price and fee for an under- and an overrun
> - PTA formula with value
> - When fixed price is appropriate (defined scope) and risks (risk premium, quality cutting)

---

## 4. Cost-Reimbursable and Time & Materials Contracts
> 🟠 Tier 2 · _Key points:_ CPFF, CPIF, CPPC (avoid), T&M with not-to-exceed; buyer bears cost risk; controls

### Definition
**Cost-reimbursable contracts** pay the seller's allowable actual costs plus a fee; the **buyer bears cost risk**. Used when scope is uncertain, urgent, R&D-heavy or emergency.

| Type | Fee | Incentive effect |
|---|---|---|
| **Cost Plus Fixed Fee (CPFF)** | Fixed amount set at award (based on estimated cost) | Fee does not move with cost; mild cost incentive |
| **Cost Plus Incentive Fee (CPIF)** | Target fee plus share of under/overrun, usually with min and max fee | Seller shares savings and overruns; best incentive among cost-plus |
| **Cost Plus Award Fee (CPAF)** | Base fee plus discretionary award for performance | Subjective; needs clear criteria |
| **Cost Plus Percentage of Cost (CPPC)** | Fee = % of cost | **Perverse incentive**: higher cost, higher fee; banned for US federal contracts and generally avoided |

**Time & Materials (T&M):** pay agreed **rates** for hours and materials actually used, often with a **not-to-exceed (NTE) cap**. Open-ended without a cap; fast to start; common in IT, consulting and maintenance. Controls: approved rate card, timesheets, change approvals, caps, audit rights, definition of allowable costs and **target-cost reviews**. In India cost-plus and "item-rate with variations" structures appear in some public works (item-rate/BoQ re-measurement contracts are measured on actual quantities).

### Example
Continue the ₹100 crore target-cost job with fee mechanics, in ₹ crore:

| Contract | Actual cost 90 | Actual cost 115 | Seller's view |
|---|---|---|---|
| **CPFF** (fixed fee 8) | pay 98 (cost + 8) | pay 123 | Fee unchanged, no incentive to save |
| **CPIF** 80/20, target fee 10, fee between 0 and 20 | fee 12, pay **102** | fee 7, pay **122** | Shares both sides |
| **CPPC** 10% of cost | pay 99 (fee 9) | pay 126.5 (fee 11.5) | Overruns raise the fee: avoid |
| **FFP** 110 | pay 110 (profit 20) | pay 110 (loss 5) | Seller bears all |

At an actual cost of 160 the CPIF fee would formula to −2, so it floors at the minimum fee of 0 and the buyer pays 160. A T&M example: 5,000 hours at ₹1,200 per hour = ₹60 lakh; if the hours reach 6,500 the bill is ₹78 lakh; a NTE cap of ₹70 lakh limits exposure (needs a formal change to go higher).

### In the news
See news box. Cost-reimbursable arrangements shift overrun risk onto the public exchequer, so they demand stronger owner-side controls than fixed-price contracts.

### Interview angle
> [!question] How it is asked
> "Which contract type would you choose for a project with high scope uncertainty, and how would you protect the buyer?"

> [!tip] Strong answer includes
> - Cost-reimbursable with incentive (CPIF) or phased: study/prototype under T&M then fixed-price
> - Computes fee under under- and overrun
> - Controls: caps, audits, allowable-cost definitions, approvals
> - Why CPPC is avoided

---

## 5. Delivery Models: Design-Bid-Build, Design-Build, EPC/Turnkey, EPCM and PMC
> 🟠 Tier 2 · _Key points:_ Single-point responsibility; risk allocation; EPC lump-sum turnkey; EPCM; PMC

### Definition
| Model | Design by | Construction by | Risk and control |
|---|---|---|---|
| **Design-Bid-Build (DBB, "item-rate")** | Owner's consultant | Contractor selected after design | Owner controls design and bears design risk and interface; competitive pricing on completed design; slower |
| **Design-Build (DB)** | Contractor | Same contractor | Single responsibility, faster, owner gives less design control |
| **EPC (Engineering-Procurement-Construction), lump-sum turnkey (LSTK)** | Contractor | Contractor (procure and build) | Contractor takes most design, procurement and construction risk for a fixed price and date; owner defines performance requirements; higher price for risk transfer |
| **EPCM** | Engineer designs and manages | Multiple contractors under owner | Owner bears more cost risk; EPCM is a fee-based management service |
| **PMC (Project Management Consultancy)** | Independent | Supervises owner's contracts | Advisory/supervision role for the owner |
| **Construction Management at Risk** | Designer separate | CM guarantees maximum price | Early contractor input |
| **Alliance / Integrated Project Delivery (IPD)** | Joint | Shared | Shared risk and reward, open books |

**EPC / turnkey** is common in Indian infrastructure (roads, power plants, water, metro civil packages, solar parks, refineries). In **EPC mode on highways**, the government (NHAI/MoRTH) finances the entire cost and the contractor builds and hands over; in contrast to BOT and HAM (next sub-topic). Features: **performance guarantees** (output, efficiency), **delay and performance liquidated damages**, **caps on liability** (often 100% of contract price or less), **performance bank guarantee** (commonly 3-10% of contract value in Indian practice, check the specific bid), **retention money**, **advance payment with bank guarantee**, **milestone-based payment**, **interface management**, **testing and commissioning**, and **defects liability period (DLP)**. FIDIC's Silver Book is the model for EPC/turnkey (see below).

Selecting model: scope maturity, owner expertise, schedule pressure, risk appetite, financing and market capacity. Integration with cost control: [[042 Cost & Budget Management]]; schedule: [[039 Scheduling Tools (CPM-PERT-Gantt)]].

### Example
A ₹400 crore solar-plus-storage plant: owner chooses **EPC lump-sum** with milestones: advance 10% (against bank guarantee), 60% on equipment delivery milestones, 20% on mechanical completion, 5% on commissioning and 5% retention released after a 12-month DLP. Guarantees: capacity utilisation factor, performance ratio 80%; LDs: delay 0.5% of contract price per week capped at 10% (₹40 crore) and performance LD for shortfall. Compared with DBB, price is perhaps 5-8% higher (risk premium, an assumption), but schedule certainty and a single point of responsibility are worth it if the owner lacks interface-management capacity.

### In the news
See news box. MoRTH leads project count (993 central projects); the delivery mode chosen (EPC, HAM, BOT) shapes who funds overruns.

### Interview angle
> [!question] How it is asked
> "What are the advantages and disadvantages of EPC lump-sum turnkey contracts for the owner?"

> [!tip] Strong answer includes
> - Single-point responsibility, schedule and price certainty, risk transfer
> - Higher price, less owner control, claims over scope and changes, contractor financial strength risk
> - Safeguards: guarantees, LDs, retention, step-in rights, independent supervision
> - Comparison to DBB and EPCM

---

## 6. PPP in Indian Infrastructure: BOT, HAM, TOT and Concessions
> 🟠 Tier 2 · _Key points:_ BOT toll, BOT annuity, HAM, TOT, VGF; risk sharing; model concession agreements

### Definition
**Public-private partnerships (PPPs)** use private capital and capability to build and operate public infrastructure under a **concession**: the private party designs, builds, finances, operates and transfers an asset (BOT and variants such as BOOT, DBFOT) and recovers costs through user fees or government payments. BOT allocates substantial construction, financing, operation and demand risk to the private party.

| Model | Who funds construction | Who bears traffic/revenue risk | Payments to developer |
|---|---|---|---|
| **EPC (public funds)** | Government | Government | Milestone payments |
| **BOT Toll** | Developer (equity plus debt), sometimes with VGF | Developer | Toll collected by developer over concession |
| **BOT Annuity** | Developer | Government (fixed annuities) | Semi-annual annuities |
| **HAM (Hybrid Annuity Model)** | Government about **40%** during construction; developer about 60% | Government (toll collected by the authority) | Construction support plus annuities with interest, plus O&M payments |
| **TOT (Toll-Operate-Transfer)** | Existing asset | Developer | Upfront payment by developer to authority for toll rights |
| **InvIT/monetisation** | Recycles operating assets into funds | Investors | Capital recycling |

The HAM structure above is the standard NHAI design as generally described (confirm against the current Model Concession Agreement before quoting): developer is paid by the authority; the developer bears construction, financing and O&M performance risk, but not traffic risk, which helped attract bidders after weaker BOT-toll experience. **Viability Gap Funding (VGF)** gives capital grants (the PPP framework cites up to 20% of project cost) to make economically sound but financially marginal projects bankable. As of November 2020, India reported 1,103 PPP projects with committed investment of about US$275 billion, roads being 60% by count (source: Wikipedia summary; dated). Model concession agreements and the **Kelkar Committee** (2015) recommended better risk allocation, renegotiation frameworks and stronger arbitration.

### Example
Illustrative HAM economics for a ₹1,000 crore road project: construction support = 40% × 1,000 = **₹400 crore** (paid in milestones); developer funds ₹600 crore (say 30% equity ₹180 crore, 70% debt ₹420 crore). The ₹600 crore plus interest is repaid via 30 semi-annual annuities. Assuming interest at 9.5% a year (illustrative; actual rate is set as bank rate plus a spread in the concession): semi-annual rate 4.75%, annuity = 600 × 0.0475 / (1 − 1.0475^−30) ≈ **₹37.9 crore each half-year**, about ₹75.9 crore a year, so total annuities ₹1,137.8 crore over 15 years, with O&M payments extra. The developer's equity IRR depends on cost control and on penalties for lane availability failures. Capital-budgeting tools are in [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]] and [[109 Valuation Basics (NPV, IRR, DCF)]].

### In the news
See news box. Road projects dominate the central pipeline (993 projects, ₹9.62 lakh crore), so the choice of EPC vs HAM vs BOT directly affects fiscal exposure to overruns. Related policy: [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].

### Interview angle
> [!question] How it is asked
> "Why did India move from BOT toll to HAM on highways, and what are the trade-offs?"

> [!tip] Strong answer includes
> - BOT toll shifted traffic risk to developers, which strained bidders and lenders when traffic fell short
> - HAM shares funding (about 40% government) and removes traffic risk from the developer
> - Trade-off: government retains revenue risk and longer-term annuity liabilities
> - Mentions VGF, concession agreements, dispute resolution, and lender protections

---

## 7. FIDIC Contract Basics
> 🟠 Tier 2 · _Key points:_ Red, Yellow, Silver books; Engineer; claims notice; DAAB; risk allocation by book

### Definition
**FIDIC** (International Federation of Consulting Engineers) publishes standard forms used internationally and widely for India's externally funded and private projects. The core suite (second editions 2017):

| Book | Used for | Design responsibility | Pricing and risk |
|---|---|---|---|
| **Red Book** (Construction) | Employer-designed works | Employer | Re-measurement (BoQ); employer carries more risk (ground, design) |
| **Yellow Book** (Plant & Design-Build) | Contractor-designed plant and works | Contractor | Lump sum with adjustments; shared risk |
| **Silver Book** (EPC/Turnkey) | Turnkey with fixed price and date | Contractor, nearly all | Lump sum; contractor carries most risk (including ground), employer's requirements define scope |
| **Green Book** | Short-form, small works | Either | Simple |

Key mechanisms (2017 editions): the **Engineer** (Red/Yellow) determines claims and certificates fairly (Silver uses an Employer's Representative); **time for completion**, **Notice of Claim** (contractor must notify within **28 days** of becoming aware of an event giving rise to a claim, with detailed particulars later; late notice can bar the claim, so check the specific clause), **extension of time**, **variations** (instruction or request for proposal) and valuation, **payment certificates**, **Taking-Over** certificate, **Defects Notification Period**, **termination** rights, and **dispute avoidance/adjudication boards (DAAB)** followed by arbitration. Contracts operate through **General Conditions plus Particular Conditions**, where parties tailor risk allocation; heavy amendments can unbalance the form. Indian public works often use **government-specific standards** (such as CPWD or MoRTH/NHAI templates, **GCC**) rather than FIDIC; know both.

### Example
Under a Red Book contract an unexpected rock layer is found at 4 m depth. Contractor gives notice within 28 days, supplies records; the Engineer assesses whether conditions were "unforeseeable" (physical conditions clause), grants EOT of 15 days and cost of ₹1.2 crore. Under a Silver Book, the same event is typically at contractor's risk unless the Particular Conditions or Employer's Requirements say otherwise; the contractor should therefore have priced additional ground investigation and contingency at bid time.

### In the news
See news box. The 2017 second editions strengthened notice, claims and dispute-avoidance mechanisms; the practice lesson is timely notice and contemporaneous records.

### Interview angle
> [!question] How it is asked
> "What is the difference between FIDIC Red, Yellow and Silver books?"

> [!tip] Strong answer includes
> - Design responsibility and risk allocation for each book
> - Re-measurement vs lump-sum pricing
> - Claims notice discipline and dispute avoidance boards
> - Awareness that Particular Conditions modify risk, and that Indian public contracts often use their own GCC

---

## 8. Bid Evaluation and Source Selection
> 🟠 Tier 2 · _Key points:_ Prequalification, technical responsiveness, L1 vs QCBS, weighted scoring, abnormally low bids

### Definition
Stages: **responsiveness check** (compliance with documents), **technical evaluation** (qualifying criteria and scoring), **price evaluation**, **clarifications and negotiation** (limited, rules-bound in public procurement), **award**, **contract signing** with performance security.

- **L1 (lowest evaluated bidder):** among technically qualified bids, lowest price wins. Standard for most public works and goods in India; transparent but encourages **lowballing** and may ignore quality.
- **QCBS (Quality-and-Cost Based Selection):** weighted score
$$\text{Combined score} = w_t \times S_t + w_f \times S_f, \qquad S_f = 100 \times \frac{\text{Lowest price}}{\text{Bid price}}$$
Common for consultancy; in public works its use is limited and conditions apply; check the current Ministry of Finance procurement manuals.
- **Weighted scoring models** for private projects: criteria weights (technical, financial, experience, schedule, HSE, references).
- **Total cost of ownership (TCO) / life-cycle cost** (CAPEX plus operating and maintenance) instead of purchase price only.
- **Abnormally low bids:** compare against the independent estimate and the average of bids; ask for a rate analysis; require higher performance security.
- **Ethics and vigilance:** conflict of interest declarations, integrity pacts, no post-bid changes outside rules, documented evaluation committee decisions, audit trail.

### Example
Three technically qualified bidders for a ₹100 crore package (technical score out of 100; price in ₹ crore). Weights 70:30.

| Bidder | Tech score | Price | Financial score | Combined |
|---|---|---|---|---|
| A | 82 | 95 | 100 × 88/95 = 92.63 | 0.7×82 + 0.3×92.63 = **85.19** |
| B | 90 | 100 | 88.00 | 0.7×90 + 0.3×88 = **89.40** |
| C | 75 | 88 | 100.00 | 0.7×75 + 0.3×100 = **82.50** |

L1 selects C (₹88 crore); QCBS selects B (₹100 crore, highest technical). The ₹12 crore gap buys technical strength. For an unmanageably complex plant that is sensible; for a standard road section it is not, which is why L1 with strict qualification is used there. Abnormal-bid check: bids 100, 105, 110 and 72 have mean 96.75; 72 is 74% of mean; demand justification and extra security.

### In the news
See news box. Under-priced awards followed by variations and claims are a plausible contributor to systematic overruns; this is a hypothesis in the sources read, not a finding they report.

### Interview angle
> [!question] How it is asked
> "L1 or quality-based selection: how would you choose a contractor for a complex project?"

> [!tip] Strong answer includes
> - Matches method to complexity: L1 for well-defined works, QCBS or weighted for complex scope
> - Prequalification thresholds and technical gating
> - Abnormally low bid analysis and performance security
> - Total cost of ownership and transparent, documented scoring

---

## 9. Risk Allocation and Incentive Design in Contracts
> 🟠 Tier 2 · _Key points:_ Allocate risk to the party best able to manage it; pain/gain share; bonuses; guarantees

### Definition
Principle: allocate each risk to the party that can **control** it, **bear** it at lowest cost and has the incentive to manage it (see [[040 Risk & Stakeholder Management]], [[137 Supply Chain Contracts & Game Theory]]).

| Risk | Typically better borne by |
|---|---|
| Design errors in owner-supplied design | Owner |
| Means and methods, productivity, workmanship | Contractor |
| Geotechnical (unforeseeable) | Shared / owner under Red Book; contractor under Silver |
| Land acquisition, statutory clearances, right-of-way | **Owner/authority** (a major source of delay in Indian projects) |
| Price inflation of inputs | Shared by index adjustment, or contractor for short fixed-price jobs |
| Force majeure, change in law | Shared (time relief; cost for change in law) |
| Traffic or demand | Authority (annuity/HAM) or developer (toll BOT) |
| Interface among packages | Whoever holds the interface role: EPC wrap or owner/PMC |

**Incentive tools:** pain/gain share (FPIF/CPIF), early-completion bonus, milestone payments, retention and performance guarantees, LDs for delay and performance, quality bonuses, KPI-linked fees, alliance models. **Balance:** very harsh terms raise bid prices, produce claims-based behaviour and abandonment; an unbalanced risk allocation is a leading cause of disputes. Mitigations: contingency allocation (see [[042 Cost & Budget Management]]), insurance (CAR, third-party liability), bonds (bid, performance, advance), step-in rights.

### Example
Early-completion bonus: a 24-month ₹200 crore contract, delay LD at 0.5% of price per week capped at 10%, and a bonus of ₹0.5 crore per week early capped at ₹4 crore. The owner's benefit from early opening is ₹1.5 crore a week (toll or operating revenue). The bonus costs ₹0.5 crore per week and yields ₹1.5 crore of owner benefit: net +₹1 crore per week; contractor is motivated to accelerate. Without a bonus, the contractor has no reason to finish early. The LD rate of ₹1 crore per week (0.5% × 200) is below the owner's loss of ₹1.5 crore a week, so the **LD must be a genuine pre-estimate of loss** (see next sub-topic) and may be justified up to its cap only if documented.

### In the news
See news box. Land and clearance delays, not just contractor performance, drive many Indian project delays, which is why risk allocation should place them with the authority and why contracts need relief mechanisms.

### Interview angle
> [!question] How it is asked
> "How would you structure a contract to align incentives of a contractor with the owner's schedule and cost goals?"

> [!tip] Strong answer includes
> - Principle: risk to the party who can control it
> - Pain/gain share, early completion bonus and balanced LDs with caps
> - Guarantees, retention, insurance and step-in rights
> - Avoiding unbalanced terms that inflate bids or breed disputes

---

## 10. Claims, Variation Orders, Extension of Time and Liquidated Damages
> 🟠 Tier 2 · _Key points:_ Notice, records, EOT vs cost, concurrent delay, LD cap, dispute escalation

### Definition
- **Variation order (VO) / change order:** a formal change to scope, quantity, specification or schedule, priced by contract rates, derived rates or agreed lump sums; requires approval authority and documentation. See change control in [[038 PMBOK Knowledge Areas]].
- **Claim:** a request by a party for time and/or money based on contract rights (employer-caused delay, differing site conditions, change in law, force majeure). Contractor claims need **timely notice, contemporaneous records, causation analysis and quantification**.
- **Extension of time (EOT)** relieves the contractor from delay LDs; **cost compensation** (prolongation costs, disruption, loss of productivity) needs separate entitlement. **Concurrent delay** (both parties) often gives time but not money.
- **Delay analysis methods:** as-planned vs as-built, impacted as-planned, time-impact analysis, windows analysis (see [[039 Scheduling Tools (CPM-PERT-Gantt)]]).
- **Liquidated damages (LDs):** pre-agreed sum for delay or performance shortfall, typically a percentage of contract price per week or day, capped (commonly around 5-10%). Enforceable if a **genuine pre-estimate** of loss, not a penalty; under Indian law (Section 74 of the Indian Contract Act) courts award reasonable compensation up to the stated amount and the claimant must usually prove loss in many cases (verify current case law). LDs are normally the **exclusive remedy** for delay.
- **Dispute resolution:** negotiation, engineer's determination, dispute boards/DAAB, mediation, arbitration (Arbitration and Conciliation Act 1996 as amended), courts. Government contracts often include departmental committees; settlement schemes have been used for old arbitration awards.

### Example
₹200 crore contract; delay LD 0.5% of price per week, capped at 10%. The contractor finishes 20 weeks late, but 8 weeks are employer-caused (late site handover), approved as EOT. Net culpable delay = 12 weeks. LD = 0.5% × 200 × 12 = **₹12 crore** (cap ₹20 crore not reached). Prolongation costs for the 8 weeks of EOT at ₹35 lakh per week of site overheads = 8 × 0.35 = **₹2.8 crore** claimed. Net effect: owner deducts ₹12 crore LD and owes ₹2.8 crore if entitlement is accepted. Variation orders: +₹6.5 crore (added drainage), +₹3.2 crore (changed paving spec), −₹1.4 crore (omitted landscaping) = net +₹8.3 crore, so revised contract value ₹208.3 crore, a 4.15% increase: well inside normal limits (many public contracts cap variations, for example at 10-25%; check the specific contract).

### In the news
See news box. A 10% aggregate overrun on central projects is of the order of change orders and delay costs that careful contract administration aims to bound.

### Interview angle
> [!question] How it is asked
> "The contractor claims EOT and money for delay caused by late land handover. How do you handle it?"

> [!tip] Strong answer includes
> - Checks contractual notice and records, causation and critical path (time-impact analysis)
> - Separates EOT (relief from LDs) from cost entitlement
> - Concurrent delay treatment and mitigation duties
> - Preserves relationship: negotiation, then dispute board/arbitration

---

## 11. Vendor and Contractor Performance Management
> 🟠 Tier 2 · _Key points:_ KPIs and scorecards, reviews, audits, corrective actions, relationship tiers, consequence management

### Definition
**Control procurement** is the day-to-day management of seller performance:

- **KPIs:** quality (first-pass yield, NCRs, defects, rework), delivery (on-time-in-full, schedule performance), cost (invoice accuracy, variation ratio, price vs index), HSE (incidents, LTIFR), responsiveness, compliance and documentation, sustainability.
- **Scorecard:** weighted composite across KPIs, reviewed monthly or quarterly with the vendor.
- **Governance:** kick-off, progress meetings, inspections and hold points, factory acceptance tests, audits, interface meetings, invoice verification against milestones, payments linked to certified progress.
- **Remedies:** corrective action requests, cure notices, withholding payments, LDs, step-in, termination for default, blacklisting under rules.
- **Relationship segmentation:** strategic, leverage, bottleneck, non-critical (Kraljic; see [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]]); invest in joint improvement with strategic vendors.
- **Supplier quality tools:** audits, APQP/PPAP in manufacturing supply chains ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]), SPC; ERP/SRM support in [[192 SAP Sourcing & Procurement Deep Dive]] and [[199 SAP Ariba, SRM & Business Network]].
- **Data and analytics:** spend and performance visibility ([[122 Spend Analysis, Savings & Procurement Maturity]]).

### Example
Weighted scorecard for an MEP contractor: quality 35%, delivery 30%, cost 20%, HSE 15%. Scores: quality 88, delivery 72, cost 80, HSE 95. Composite = 0.35×88 + 0.30×72 + 0.20×80 + 0.15×95 = 30.8 + 21.6 + 16.0 + 14.25 = **82.65**. With a threshold of 85, the contractor is placed on a performance improvement plan: the weakest KPI is delivery (72), so action items include a recovery schedule, weekly look-ahead meetings and partial payment hold of 2% until the schedule is recovered. Next review in 6 weeks.

### In the news
See news box. Only about 38% of the central projects tracked had passed 80% physical completion; systematic performance management is how owners spot slippage early rather than at completion.

### Interview angle
> [!question] How it is asked
> "How do you manage an underperforming contractor on a live project?"

> [!tip] Strong answer includes
> - Fact-based review using KPIs and records; root cause (resources, design, payments, interfaces)
> - Escalating tools: corrective plan, resource commitments, payment holds, LDs, step-in
> - Protects schedule and quality; contingency options (alternate vendors)
> - Documents every step for potential disputes

---

## 12. Procurement Closure and Lessons Learned
> 🟠 Tier 2 · _Key points:_ Final acceptance, settle claims, retention release, records, lessons learned

### Definition
**Close procurement** formally completes each contract:

1. **Verify delivery and acceptance:** all deliverables accepted; testing, commissioning, punch list cleared; **Taking-Over / completion certificates**.
2. **Defects liability / notification period:** monitor and rectify defects; release of **retention money** and **performance guarantee** after DLP.
3. **Final account and claims settlement:** reconcile quantities, variations, LDs, price adjustments and backcharges; resolve open claims or dispute procedures; obtain **no-claim/discharge** certificates where appropriate.
4. **Records:** as-built drawings, O&M manuals, warranties, test certificates, training, spares, IP and software licences transferred; audit file for public contracts.
5. **Supplier performance rating** recorded in the vendor database.
6. **Lessons learned:** what worked and failed in specification, bidding, contract terms, risk allocation, administration; shared to improve templates and estimating.
7. **Contract closure in systems:** purchase orders closed in ERP, accruals reversed, open commitments released (see [[190 SAP FI-CO Essentials for Operations Professionals]]).

Early termination follows a similar route with settlement of work done, return of advances, and handling of guarantees.

### Example
₹200 crore contract at final account (₹ crore): certified work value after variations 208.3; less delay LD 12.0, so entitlement = 208.3 − 12.0 = 196.3. Payments already made (net of advance recovery) are assumed to be 183.0. Retention of 5% of certified value = 0.05 × 208.3 = 10.415 stays withheld until the 12-month defects liability period ends. Balance payable now = 196.3 − 183.0 − 10.415 = **2.885**; after the DLP, the 10.415 is released if defects are rectified. If the contractor had already received 190, the same arithmetic gives 196.3 − 190 − 10.415 = −4.115, an over-payment to be recovered or offset against retention. This is why closure reconciliation matters: milestone and advance payments running ahead of certified progress are only caught at final account.

### In the news
See news box. The MoSPI database reports both cost and physical progress, a reminder that a project is not closed until money, scope and records reconcile.

### Interview angle
> [!question] How it is asked
> "What do you check before closing out a contract and releasing the final payment and guarantee?"

> [!tip] Strong answer includes
> - Acceptance and testing complete, defects cleared, DLP over
> - Final account reconciliation including variations, LDs and advances
> - Records, as-built and warranties handed over
> - Lessons learned and vendor rating recorded

---

## 13. Lessons from Megaprojects: Cost-Overrun Statistics and Their Causes
> 🟠 Tier 2 · _Key points:_ Iron law of megaprojects; optimism bias and strategic misrepresentation; reference-class forecasting; India stats

### Definition
Evidence on large projects:

- **Flyvbjerg's database** (about 16,000 projects): only about **0.5%** meet budget, schedule and benefit promises; many sectors show **average overruns well above zero** and "fat tails" (a few projects overrun by multiples), especially nuclear, IT and Olympic projects. The "iron law": over budget, over time, under benefits, over and over again. (Treat exact sector means as quoted from his work, not verified here.)
- **India (MoSPI, July 2026):** for 1,775 central projects of ₹150 crore or more, cost overrun ₹3.4 lakh crore, about 10.1% of original cost, in aggregate (not per project; the source does not report individual project overrun shares or time overrun).
- **Causes:** optimism bias and **strategic misrepresentation** (underestimating to win approval); weak front-end definition and design maturity; **land acquisition and clearances**; scope creep and late changes; unrealistic bids and weak contractor capability; poor risk allocation and interface management; supply chain and commodity price shocks; inadequate governance and skills; escalation and financing delays.
- **Remedies:** **reference-class forecasting** (adjust estimates using the distribution of outcomes of similar past projects), **independent reviews at stage gates**, higher front-end investment (planning), **modularisation and smaller delivery units**, early contractor involvement, realistic contingency based on risk analysis (P50/P80), data-driven monitoring ([[042 Cost & Budget Management]]), strong owner capability, and balanced contracts.

### Example
Reference-class adjustment: a rail project budget is ₹10,000 crore; the reference class of 100 similar projects shows an average overrun of 40% with 80th-percentile overrun of 70%. Uplift for P80 funding: ₹10,000 crore × 1.70 = **₹17,000 crore**; for P50 (say 35% median) ₹13,500 crore. The sponsor funds at P80 and sets a P50 as target budget, holding the difference as a **management reserve**. In the Indian aggregate, a 10.1% overrun on ₹33.7 lakh crore of original cost is ₹3.4 lakh crore, equal to about ₹340 crore for every ₹3,370 crore planned. Note the contrast: a 10% average can hide a few very large overruns, so portfolio-level averages are not a substitute for project-level review.

### In the news
See news box for MoSPI and Flyvbjerg data.

### Interview angle
> [!question] How it is asked
> "Why do large infrastructure projects almost always overrun, and what would you do about it?"

> [!tip] Strong answer includes
> - Cites causes: optimism bias, scope definition, land/clearances, contract risk allocation
> - Mentions reference-class forecasting and stage-gate reviews
> - Uses evidence (MoSPI 10.1% aggregate; the 0.5% on-time-on-budget statistic) with correct caveats
> - Concrete measures for the project at hand: contingency, packaging, governance

---

## 14. ⭐ Advanced: Alliancing, Reference Classes and Claims Avoidance
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Alliancing and IPD:** owner and key contractors share a single risk-reward pool: target outturn cost, open books, **pain/gain sharing** (for example 50/50 above and below target), limited liability and joint decision-making. Strong for high-uncertainty, complex projects; heavy on trust and governance; value-for-money test needed in public procurement.
- **Early Contractor Involvement (ECI):** contractor contributes to design and buildability under a development agreement, then a target-price contract.
- **Claims avoidance:** clear scope and risk register, joint site investigations, **contemporaneous records**, early warning notices, rapid change decisions, dispute boards from day one, and reasonable LD caps.
- **Quantitative contingency:** build a **risk-adjusted cost estimate** (Monte Carlo on cost and schedule), report P50 and P80 (see [[150 Decision Analysis & Simulation]] and [[068 Operations-Specific Python (PuLP, SimPy)]]).
- **Procurement analytics:** bid pattern analysis to detect collusion, abnormal bid dispersion; use data from [[122 Spend Analysis, Savings & Procurement Maturity]].
- **Interview case use:** treat procurement strategy as a decision tree: scope maturity (high/low) × risk allocation (owner/contractor/shared) × market capacity → contract type and delivery model; combine with schedule and cost effects (see [[171 Project Management Interview Questions & Numericals]]).

### Example
Target outturn cost (TOC) alliance: TOC ₹500 crore; pain/gain share 50/50 between owner and the alliance, with the alliance's profit at risk up to 100% of its fee (₹40 crore) and limited above that. Actual cost ₹470 crore: gain ₹30 crore, shared ₹15 crore each, so the alliance receives fee ₹40 crore + ₹15 crore = ₹55 crore. Actual ₹540 crore: pain ₹40 crore, shared ₹20 crore each, so the alliance's fee is ₹40 − ₹20 = ₹20 crore. Actual ₹600 crore: pain ₹100 crore, half ₹50 crore exceeds the ₹40 crore fee, so fee falls to zero and the alliance's loss is capped, the owner pays the rest. A Monte Carlo cost model for the owner gives P50 ₹520 crore and P80 ₹570 crore, so the owner sets its funding at P80 while the TOC is negotiated at about P50 to keep stretch.

### In the news
See news box. The shape of overruns (a few very large ones) is why probabilistic budgeting (P80) is replacing single-point estimates.

### Interview angle
> [!question] How it is asked
> "When would you choose an alliance contract over a fixed-price EPC?"

> [!tip] Strong answer includes
> - High uncertainty, complex interfaces and strong owner-contractor trust
> - Open book TOC and pain/gain sharing with caps; governance and value-for-money tests
> - Trade-offs: less price certainty than fixed price
> - Contingency set with probabilistic analysis (P50/P80)
