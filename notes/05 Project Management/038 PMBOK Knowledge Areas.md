---
tags: [project-management, tier1]
area: Project Management
topic: "PMBOK Knowledge Areas"
tier: Tier 1
roles: Project Mgmt
status: complete
subtopics: 12
---
# PMBOK Knowledge Areas

⬅ [[037 PM Fundamentals & Lifecycle]] · [[_Index - Project Management|Project Management]] · [[039 Scheduling Tools (CPM-PERT-Gantt)]] ➡

> **Area:** Project Management · **Priority:** 🔴 Tier 1 · **Target roles:** Project Mgmt

## Sub-topics in this note
1. [[#1. Integration Management]]
2. [[#2. Scope Management]]
3. [[#3. Schedule Management]]
4. [[#4. Cost Management]]
5. [[#5. Quality Management]]
6. [[#6. Resource Management]]
7. [[#7. Communications Management]]
8. [[#8. Risk Management]]
9. [[#9. Procurement Management]]
10. [[#10. Stakeholder Management]]
11. [[#11. ⭐ Advanced: Quantitative Risk (EMV, Decision Trees, Monte Carlo)]]
12. [[#12. ⭐ Advanced: Change Control Board and Baselines]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): PMBOK 8th edition retires the ten Knowledge Areas; Navi Mumbai Airport is a live case
> **PMBOK Guide 8th edition (Nov 2025).** According to a PMP-prep summary (secondary source; confirm on pmi.org), the 8th edition was published in **Nov 2025**, is organised around **6 principles, 7 performance domains** (governance, scope, schedule, finance, stakeholders, resources, risk), 5 focus areas and **40 processes**, and "distils" the earlier **ten Knowledge Areas** into the domains; a revised PMP exam is reported for **9 Jul 2026**. The ten Knowledge Areas below remain the standard way to learn the content (they are the 6th edition's structure). ([PM Study Circle](https://pmstudycircle.com/pmbok-guide-8th-edition/))
> 
> **Navi Mumbai International Airport (opened 8 Oct 2025).** Proposed Nov 1997, approved Aug 2007, groundbreaking Feb 2018, construction start Aug 2021, Phase 1 inaugurated 8 Oct 2025 (reported cost **₹19,650 crore**; **20 million passengers a year** capacity); delays came from resettling **2,786 households across ten villages** and a developer change from GVK (2017) to Adani (2021). Commercial operations were reported for **25 Dec 2025**. ([All India Radio](https://www.newsonair.gov.in/pm-modi-unveils-%E2%82%B919650-cr-navi-mumbai-airport-a-new-milestone-in-indias-aviation-sector), [Wikipedia](https://en.wikipedia.org/wiki/Navi_Mumbai_International_Airport))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Integration Management
> 🔴 Tier 1 · _Tracker hint:_ Develop charter, project plan, direct work, manage changes, close

### Definition
**Integration Management** coordinates all other areas into a unified whole. PMBOK 6 processes:
1. **Develop Project Charter** (Initiating)
2. **Develop Project Management Plan** (Planning): integrates subsidiary plans and baselines.
3. **Direct and Manage Project Work** (Executing): produces deliverables, implements approved changes.
4. **Manage Project Knowledge** (Executing)
5. **Monitor and Control Project Work** (M&C)
6. **Perform Integrated Change Control** (M&C): the **Change Control Board (CCB)** reviews change requests, analysing impact on all constraints.
7. **Close Project or Phase** (Closing)

Key artefacts: charter, project management plan, change log, issue log, work performance data → information → reports. Tools: expert judgement, change control tools, configuration management. Integration is the PM's **core role**: trade-offs among competing objectives.

### Example
A supplier-delay triggers a change request to reorder sequence: PM assesses impact (schedule +2 weeks, cost +₹4 lakh, risk of quality), submits to the CCB, and if approved updates the schedule baseline and risk register, communicates to stakeholders. That cross-area handling is integration.

### In the news
See news box. In PMBOK 8 integration is not a stand-alone domain; its ideas (holistic view principle) are spread through the guide. Navi Mumbai's developer change and land-resettlement shows integration across legal, civil and commercial threads.

### Interview angle
> [!question] How it is asked
> "What is integrated change control?" or "How do you keep a multi-team project aligned?"

> [!tip] Strong answer includes
> - Seven processes in lifecycle order
> - Change process steps: request, analyse impact, CCB decision, update baselines, communicate
> - Plan integrates subsidiary plans and baselines
> - Give an example of a cross-area trade-off

---

## 2. Scope Management
> 🔴 Tier 1 · _Tracker hint:_ Collect requirements, define scope, WBS, validate, control scope

### Definition
Ensures the project includes **all and only** the work required. Processes:
1. **Plan Scope Management**
2. **Collect Requirements:** interviews, workshops, surveys, prototypes, user stories; output: requirements documentation and **Requirements Traceability Matrix (RTM)**.
3. **Define Scope:** the **project scope statement** (deliverables, exclusions, acceptance criteria, assumptions).
4. **Create WBS:** scope baseline = scope statement + WBS + WBS dictionary.
5. **Validate Scope:** customer **formally accepts** deliverables (done in Monitoring; contrast with Control Quality, which checks correctness internally).
6. **Control Scope:** monitor status vs baseline, manage changes, prevent creep.

**Product scope** (features and functions) vs **project scope** (work to deliver). Use MoSCoW for requirement priority (see [[034 Prioritization Frameworks]]).

### Example
For a new distribution centre: out-of-scope list explicitly excludes the transport fleet; validation: customer walks through the racking and WMS test results and signs the acceptance form; a request for cold storage later is treated as a change request.

### In the news
See news box. Scope survives as a "scope" performance domain in PMBOK 8; Navi Mumbai's phased approach (Phase 1 first) is scope management in practice: define what opens first.

### Interview angle
> [!question] How it is asked
> "Difference between Validate Scope and Control Quality?" or "How do you manage scope on a project with vague requirements?"

> [!tip] Strong answer includes
> - Six processes, scope baseline components
> - Validate (customer acceptance) vs Control Quality (internal correctness)
> - RTM and change control
> - Product vs project scope

---

## 3. Schedule Management
> 🔴 Tier 1 · _Tracker hint:_ Define activities, sequence, estimate, develop schedule, control

### Definition
Processes: **Plan Schedule Management**, **Define Activities** (from work packages), **Sequence Activities** (dependencies: FS, SS, FF, SF; leads and lags), **Estimate Activity Durations** (analogous, parametric, three-point/PERT, bottom-up), **Develop Schedule** (CPM, resource optimisation, schedule compression), **Control Schedule** (variance analysis, performance reviews, EVM's SPI).

Dependency types: mandatory (hard logic), discretionary (soft), external, internal. Output: **schedule baseline**, Gantt, milestone chart, network diagram. Detail on techniques: [[039 Scheduling Tools (CPM-PERT-Gantt)]]. Key formulas: $\text{SV} = EV - PV$; $\text{SPI} = EV/PV$; $\text{Float} = LS - ES$.

### Example
Activities: A (3 days) then B (4) and C (2) in parallel, both then D (1). Paths: A-B-D = 8 days, A-C-D = 6 days. The project is 8 days; C has 2 days of float.

### In the news
See news box. Navi Mumbai's mid-2020 target and Oct 2025 opening, with construction starting in Aug 2021, shows how schedule baselines break when the predecessor logic (land, permits, developer) isn't resolved.

### Interview angle
> [!question] How it is asked
> "The project is 3 weeks behind. What do you do?"

> [!tip] Strong answer includes
> - Root cause first: variance analysis on critical path
> - Options: crashing, fast tracking, scope cut; with risk/cost of each
> - Use SPI and trend to forecast completion
> - Re-baseline only with approved change

---

## 4. Cost Management
> 🔴 Tier 1 · _Tracker hint:_ Estimate, budget, control; Earned Value Management (EVM)

### Definition
Processes: **Plan Cost Management**, **Estimate Costs** (analogous, parametric, bottom-up, three-point; accuracy improves from ROM −25/+75% to definitive −5/+10%), **Determine Budget** (cost baseline + **contingency reserve** inside baseline, **management reserve** outside), **Control Costs** (EVM).

**EVM formulas:**
| Measure | Formula |
|---|---|
| PV (planned value), EV (earned value), AC (actual cost) | EV = % complete × BAC |
| CV (cost variance) | EV − AC |
| SV (schedule variance) | EV − PV |
| CPI | EV / AC |
| SPI | EV / PV |
| EAC (typical variance continues) | BAC / CPI |
| EAC (atypical) | AC + (BAC − EV) |
| ETC | EAC − AC |
| VAC | BAC − EAC |
| TCPI (to BAC) | (BAC − EV)/(BAC − AC) |

CPI < 1 = over budget; SPI < 1 = behind schedule.

### Example
BAC = ₹10,00,000; planned 50% done (PV = ₹5,00,000); actually 40% (EV = ₹4,00,000); AC = ₹4,50,000.
CV = 4.0 − 4.5 = **−₹50,000**; SV = 4.0 − 5.0 = **−₹1,00,000**; CPI = 4.0/4.5 = **0.889**; SPI = 4.0/5.0 = **0.80**.
EAC = 10,00,000/0.889 = **₹11,25,000**; ETC = 11,25,000 − 4,50,000 = **₹6,75,000**; VAC = **−₹1,25,000**; TCPI = 6.0/5.5 = **1.09**.

### In the news
See news box. Cost figures for Navi Mumbai Airport differ across sources (₹19,650 crore reported at inauguration; a ₹167 billion overall estimate on Wikipedia), a good reminder to state the **scope and baseline** behind any cost number.

### Interview angle
> [!question] How it is asked
> "A project is 40% complete, spent 45% of budget. What is the status and forecast?"

> [!tip] Strong answer includes
> - Compute CPI, SPI and EAC with correct formulas
> - Interpret: over cost, behind schedule; typical vs atypical variance
> - Corrective options and TCPI feasibility
> - Contingency vs management reserve

---

## 5. Quality Management
> 🔴 Tier 1 · _Tracker hint:_ Plan, manage, control quality; QA vs QC in projects

### Definition
Processes: **Plan Quality Management** (standards, metrics, cost of quality), **Manage Quality** (≈ Quality Assurance: process audits, process improvement), **Control Quality** (≈ Quality Control: inspect deliverables, measure against acceptance criteria).

| | QA (Manage Quality) | QC (Control Quality) |
|---|---|---|
| Focus | Processes, prevention | Product, detection |
| When | Throughout | On deliverables |
| Tools | Audits, process analysis, root-cause | Inspection, testing, control charts, Pareto, histograms |

**Cost of Quality** = cost of conformance (prevention, appraisal) + cost of non-conformance (internal and external failure). **Quality vs grade:** low grade can be acceptable, low quality never. Other tools: fishbone (Ishikawa), control charts (±3σ, "rule of seven"), Pareto 80/20, cause-effect, design of experiments, benchmarking, Six Sigma, PDCA.

### Example
Construction: QA = auditing the concrete-mixing process and calibration; QC = testing the poured slab's compressive strength. If 3 of 40 test cubes fail (7.5%), root cause analysis finds a faulty batching plant; the **Pareto chart** shows 80% of defects came from one supplier.

### In the news
See news box. PMBOK 8 lists quality as a principle ("embed quality") rather than a stand-alone knowledge area, consistent with treating it as everyone's responsibility.

### Interview angle
> [!question] How it is asked
> "Difference between QA and QC?"

> [!tip] Strong answer includes
> - Process (preventive) vs product (detective)
> - Cost of quality and why prevention is cheaper
> - Tools: control chart, Pareto, fishbone
> - Quality vs grade; linking to acceptance criteria

---

## 6. Resource Management
> 🔴 Tier 1 · _Tracker hint:_ Identify, acquire, develop, manage team; RACI matrix

### Definition
Processes: **Plan Resource Management** (roles, org charts, RAM/**RACI**, resource management plan), **Estimate Activity Resources**, **Acquire Resources** (negotiation, pre-assignment, virtual teams), **Develop Team** (training, co-location, recognition; Tuckman stages: forming, storming, norming, performing, adjourning), **Manage Team** (conflict management, performance appraisals), **Control Resources**.

**RACI matrix:** **R**esponsible (does the work), **A**ccountable (one owner who signs off), **C**onsulted (two-way input), **I**nformed (one-way update). Rule: exactly **one A per task**. Conflict-resolution modes: collaborate/problem-solve (best), compromise, smooth, force, withdraw. Motivation theories: Maslow, Herzberg, McGregor X/Y, Tuckman. **Resource optimisation:** leveling and smoothing (see [[039 Scheduling Tools (CPM-PERT-Gantt)]]).

### Example
| Task | PM | Tech lead | QA | Sponsor |
|---|---|---|---|---|
| Approve design | C | R | I | A |
| Run UAT | A | C | R | I |

Each row has exactly one A. A missing "A" is a classic cause of dropped tasks.

### In the news
See news box. In PMBOK 8 "resources" is a performance domain. At megaprojects like Navi Mumbai the resource question includes land, labour and contractor capacity (for example the Larsen & Toubro construction role noted by Wikipedia), not just people.

### Interview angle
> [!question] How it is asked
> "How do you manage conflict in your team?" or "What is a RACI matrix?"

> [!tip] Strong answer includes
> - RACI definitions and one-A rule
> - Team development stages and the PM's role in each
> - Preferred conflict approach (collaborate), with a STAR example from the student's own experience
> - Handling resource constraints

---

## 7. Communications Management
> 🔴 Tier 1 · _Tracker hint:_ Plan, manage, monitor communications; stakeholder info needs

### Definition
Processes: **Plan Communications Management** (who needs what, when, how, who sends), **Manage Communications**, **Monitor Communications**. PMs spend about 90% of their time communicating (commonly quoted rule of thumb).

**Communication channels** $= \dfrac{n(n-1)}{2}$. Adding people increases complexity sharply.

Models: sender, encode, medium, decode, receiver, feedback, noise. Methods: **interactive** (meetings, calls), **push** (email, reports), **pull** (intranet, dashboards). Communication plan: stakeholder, information, format, frequency, owner. Skills: active listening, clarity, tailoring. Barriers: noise, culture, language, time zones. Reports: status, forecast, dashboard, RAG indicators. **Escalation** triggers should be pre-agreed.

### Example
A 7-member team plus the PM = 8 people: 8×7/2 = **28 channels**. Adding 2 members → 10 people: 10×9/2 = **45 channels** (+17), so formal structure (weekly stand-up, single status report, shared tracker) becomes necessary.

### In the news
See news box. Navi Mumbai: affected communities in ten villages required sustained engagement and resettlement communication; PMBOK 8 treats stakeholders as a core domain, not a side task.

### Interview angle
> [!question] How it is asked
> "How do you report bad news to a sponsor?" or "How many communication channels in a team of 10?"

> [!tip] Strong answer includes
> - Formula and the complexity insight
> - Plan by stakeholder: information, channel, frequency
> - Push/pull/interactive methods
> - Bad news early, with facts, impact, options and recommendation

---

## 8. Risk Management
> 🔴 Tier 1 · _Tracker hint:_ Identify, analyze (qual/quant), plan response, implement, monitor

### Definition
Risk = uncertain event with positive (opportunity) or negative (threat) effect. Processes (6th ed.): **Plan Risk Management**, **Identify Risks** (brainstorming, Delphi, SWOT, checklists; output **risk register**), **Perform Qualitative Analysis** (probability-impact matrix, rank), **Perform Quantitative Analysis** (EMV, decision trees, Monte Carlo, sensitivity/tornado), **Plan Risk Responses**, **Implement Risk Responses**, **Monitor Risks**.

**Responses to threats:** avoid, transfer (insurance, fixed-price contract), mitigate, accept (active/passive). **Opportunities:** exploit, share, enhance, accept. **Contingency plan** (planned fallback) vs **fallback plan**; **residual** and **secondary** risks.

$$\text{EMV} = \text{Probability} \times \text{Impact}$$

### Example
Risk: port strike delays imported equipment. P = 30%, impact ₹20 lakh → EMV = 0.30 × 20 = **₹6 lakh**. Mitigation: pre-book alternate shipping for ₹2 lakh, which reduces P to 10% → new EMV = ₹2 lakh. Benefit = 6 − 2 = 4 lakh for 2 lakh cost → worth doing (net +₹2 lakh).

### In the news
See news box. Navi Mumbai's delay causes (land acquisition, opposition, developer change) were identifiable early risks; the lesson is to rank them by probability and impact at initiation and assign owners. PMBOK 8 makes "risk" a performance domain.

### Interview angle
> [!question] How it is asked
> "How do you manage risk on a project?" or "What would you do if a risk you identified materialises?"

> [!tip] Strong answer includes
> - Process flow from identify to monitor
> - Qualitative scoring then quantitative where needed (EMV)
> - Four threat responses, owners and triggers
> - Contingency reserve; risk register reviewed regularly

---

## 9. Procurement Management
> 🔴 Tier 1 · _Tracker hint:_ Plan, conduct, control, close procurements; contract types

### Definition
Processes: **Plan Procurement Management** (make-or-buy analysis, procurement strategy, source selection criteria), **Conduct Procurements** (RFQ/RFP/RFI bids, bidder conference, evaluation, award), **Control Procurements** (administer contract, monitor performance, manage changes and claims), **Close Procurements**.

**Contract types:**
| Type | Who bears cost risk | Notes |
|---|---|---|
| **Fixed price (FFP)** | Seller | Best when scope well-defined; FPIF, FP-EPA variants |
| **Cost reimbursable (CPFF, CPIF, CPAF)** | Buyer | Scope uncertain; buyer pays costs plus fee |
| **Time and Material (T&M)** | Shared | Quick start, open-ended; cap with not-to-exceed |

Procurement documents: RFI (information), RFQ (price), RFP (proposal with solution), SOW. Evaluate with weighted criteria. Relates to Indian practice: tender/e-procurement, L1 (lowest bidder) selection risk, performance guarantees.

### Example
Make-or-buy: building an in-house yard system costs ₹80 lakh (capex) with ₹10 lakh/year support; buying costs ₹4 lakh/month = ₹48 lakh/year. Over 3 years: make = 80 + 30 = ₹110 lakh; buy = ₹144 lakh; but buy has faster deployment and lower risk, so decision uses risk and timing, not only cost.

### In the news
See news box. Navi Mumbai's developer shift (GVK to Adani) and L&T construction role illustrate procurement decisions at the strategic level; the contract and partner choice shaped delivery from 2021 onward.

### Interview angle
> [!question] How it is asked
> "Which contract type would you use for an ERP implementation?"

> [!tip] Strong answer includes
> - Match contract type to scope certainty and risk transfer
> - Make-or-buy analysis with TCO
> - Source selection criteria beyond price (capability, references, risk)
> - Vendor management, claims and closing

---

## 10. Stakeholder Management
> 🔴 Tier 1 · _Tracker hint:_ Identify, plan engagement, manage, monitor engagement

### Definition
Processes: **Identify Stakeholders** (stakeholder register, analysis; Initiating), **Plan Stakeholder Engagement**, **Manage Stakeholder Engagement**, **Monitor Stakeholder Engagement**.

Engagement levels: **Unaware, Resistant, Neutral, Supportive, Leading**: record **current (C)** and **desired (D)** level in the assessment matrix and act on the gaps. Tools: power-interest grid (see [[037 PM Fundamentals & Lifecycle]]), salience model, interviews, surveys, communication plan, issue log, negotiation, ground rules. Keys: **early** identification, continuous dialogue, expectation management, acting on issues quickly, ethical conduct.

In PMBOK 8, "stakeholders" is a performance domain, and 7th edition has the principle "engage with stakeholders proactively".

### Example
Stakeholder matrix for a new WMS: Warehouse head: current = Resistant, desired = Supportive. Plan: involve in design workshops, pilot in his DC with his KPIs, weekly 1:1. After 6 weeks re-score: Neutral → Supportive.

### In the news
See news box. Navi Mumbai's resettlement of 2,786 households and recorded local opposition (Wikipedia) show stakeholder management as schedule-critical.

### Interview angle
> [!question] How it is asked
> "A key stakeholder is resistant to your project. What do you do?"

> [!tip] Strong answer includes
> - Understand concerns, map power and interest
> - Gap between current and desired engagement
> - Concrete actions (involve, communicate, address issues), sponsor's help
> - Monitor and adapt; keep a record

---

## 11. ⭐ Advanced: Quantitative Risk (EMV, Decision Trees, Monte Carlo)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Expected Monetary Value (EMV)** sums probability-weighted outcomes; a **decision tree** compares options by EMV, including costs of each branch. **Monte Carlo simulation** runs thousands of iterations drawing activity durations/costs from distributions to produce a probability curve (S-curve) of completion date or cost, e.g. "P80 finish date". **Sensitivity (tornado) analysis** ranks the risks with the largest effect on the objective.

For a decision tree: $\text{EMV(option)} = \sum p_i \times \text{outcome}_i - \text{cost}$. Choose the highest EMV (for a risk-neutral decision-maker). Report **P50/P80** and set contingency as the gap between baseline and the chosen confidence level (P80 minus P50). Limitation: inputs are estimates (garbage-in, garbage-out); correlation among risks is often ignored.

### Example
Option 1: build in-house: 60% chance profit ₹50 lakh, 40% chance loss ₹10 lakh: EMV = 0.6×50 + 0.4×(−10) = 30 − 4 = **₹26 lakh**. Option 2: outsource: certain profit ₹20 lakh. Choose in-house on EMV, but if ₹10 lakh loss is unacceptable the sponsor may choose outsourcing (risk appetite).

### In the news
See news box. Large infrastructure uses probabilistic schedule/cost estimates; the Navi Mumbai span from a mid-2020 target to Oct 2025 opening shows a distribution of outcomes far wider than a point estimate.

### Interview angle
> [!question] How it is asked
> "How would you decide between two options with uncertain payoffs?"

> [!tip] Strong answer includes
> - EMV with a worked tree
> - Risk appetite beyond EMV
> - Monte Carlo output (P50/P80) and contingency
> - Assumptions and limitations

---

## 12. ⭐ Advanced: Change Control Board and Baselines
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **baseline** is the approved version of scope, schedule or cost against which performance is measured; the **performance measurement baseline (PMB)** integrates the three. Baselines change only through **Integrated Change Control**: request, log, impact assessment (scope, schedule, cost, quality, resources, risk), **CCB** decision (approve, reject, defer), update plans and baselines, communicate. **Emergency changes** have pre-agreed fast paths. **Configuration management** tracks versions of items and documents.

Differentiate: **corrective action** (bring performance back to plan), **preventive action** (reduce probability of future deviation), **defect repair**, **change request** (formal). Common mistake: re-baselining to hide poor performance; re-baseline only for approved scope/funding changes, keeping the original for audit and learning.

### Example
Sponsor requests an extra module costing ₹15 lakh and 3 weeks. PM logs the change, assesses impact (critical path +2 weeks, risk of resource clash), CCB approves with budget from management reserve; new cost baseline = old + 15 lakh; the change log records approval, date and rationale.

### In the news
See news box. Where cost numbers differ between sources (Navi Mumbai), disciplined baselines and change logs are how to explain exactly what changed between estimates.

### Interview angle
> [!question] How it is asked
> "How do you handle change requests after the baseline is approved?"

> [!tip] Strong answer includes
> - Baseline concept and PMB
> - Change workflow and CCB roles
> - Corrective vs preventive action vs defect repair
> - Don't re-baseline to hide variance; keep audit trail

---
## 🔗 Go deeper: expansion notes
- [[168 Project Procurement, Contracts & EPC Delivery|Project Procurement, Contracts & EPC Delivery]]
- [[170 Programme, Portfolio & PMO Management|Programme, Portfolio & PMO Management]]
