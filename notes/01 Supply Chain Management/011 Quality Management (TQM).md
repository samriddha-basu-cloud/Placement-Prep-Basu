---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Quality Management (TQM)"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 12
---
# Quality Management (TQM)

⬅ [[010 Warehouse Management]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[012 Supply Chain Analytics & KPIs]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. TQM Philosophy]]
2. [[#2. ISO 9001:2015]]
3. [[#3. Quality Control vs Quality Assurance]]
4. [[#4. PDCA Cycle]]
5. [[#5. Cost of Quality (CoQ)]]
6. [[#6. Acceptance Sampling]]
7. [[#7. Deming's 14 Points]]
8. [[#8. Juran's Quality Trilogy]]
9. [[#9. Zero Defects Philosophy]]
10. [[#10. Quality Audits]]
11. [[#11. ⭐ Advanced: Process Capability & Statistical Process Control]]
12. [[#12. ⭐ Advanced: Six Sigma DMAIC & FMEA]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Boeing's 737-9 door-plug failure as a quality-system case
> **FAA audit (Mar 2024).** After a door plug panel detached from an Alaska Airlines 737-9 on **5 January 2024**, an FAA six-week audit of Boeing's Renton plant and supplier Spirit AeroSystems' Wichita plant found "multiple instances" where the companies failed to comply with quality-control requirements, in areas such as **manufacturing process control, parts handling and storage, and product control**. Boeing was given 90 days to produce a corrective-action plan. ([NPR](https://www.npr.org/2024/03/04/1235826355/faa-audit-boeing-737-max-8-9-quality-control-failures))
>
> **NTSB probable cause (Jun 2025).** The NTSB said the accident (Flight 1282, 14,830 ft, 174 uninjured and 8 with minor injuries) was caused by Boeing's failure to provide **adequate training, guidance and oversight** to factory workers. All four securing bolts were missing; the plug was opened on 18 Sep 2023 for rivet repair **without the required documentation**, so no quality inspection of the closure took place. The NTSB also criticised the FAA's oversight of "repetitive and systemic" nonconformance. ([NTSB](https://www.ntsb.gov/news/press-releases/Pages/NR20250624.aspx))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. TQM Philosophy
> 🔴 Tier 1 · _Tracker hint:_ Customer focus, continuous improvement, fact-based decisions, people involvement

### Definition
**Total Quality Management (TQM)** is a management approach where *every* function and employee is responsible for quality, aiming at long-term customer satisfaction and organisational success. Core elements:

1. **Customer focus:** quality is defined by the customer (internal customers too).
2. **Total involvement of people:** empowerment, training, quality circles.
3. **Process approach:** manage activities as processes, fix the process not the person.
4. **Continuous improvement (Kaizen):** small, ongoing gains via PDCA.
5. **Fact-based decision making:** data, SPC, root-cause tools.
6. **Leadership and constancy of purpose.**
7. **Supplier partnership:** quality built in upstream.

Quality dimensions (Garvin): performance, features, reliability, conformance, durability, serviceability, aesthetics, perceived quality. Gurus: Deming, Juran, Crosby, Ishikawa, Feigenbaum, Taguchi. TQM differs from inspection-based quality, which only detects defects after the fact.

### Example
Tata Steel won the Deming Application Prize (2008), awarded for company-wide TQM practice, an Indian showcase of leadership-led quality. At shop-floor level, a Toyota-style *andon* cord lets any worker stop the line when a defect appears: people involvement plus fact-based problem solving.

### In the news
See news box. Boeing is a case of what happens when quality ownership is not embedded: the NTSB blamed inadequate training, guidance and oversight rather than a single person's slip.

### Interview angle
> [!question] How it is asked
> "What is TQM and how is it different from simply inspecting products?"

> [!tip] Strong answer includes
> - Definition with 4–5 principles (customer, people, process, improvement, facts)
> - Contrast: prevention and everyone's responsibility vs end-of-line inspection
> - A concrete example (andon, quality circles, Deming Prize winners)
> - Pitfalls: TQM as a slogan, no leadership commitment, no measurement

---

## 2. ISO 9001:2015
> 🔴 Tier 1 · _Tracker hint:_ Plan-Do-Check-Act, risk-based thinking, context of organization

### Definition
**ISO 9001:2015** is the international standard for a **Quality Management System (QMS)**. It is certifiable (third-party audit, usually a three-year cycle with surveillance audits). It is built on **seven quality management principles**: customer focus, leadership, engagement of people, process approach, improvement, evidence-based decision making, relationship management.

Structure (Annex SL high-level structure), clauses **4 to 10**:
| Clause | Theme |
|---|---|
| 4 | Context of the organization (issues, interested parties, scope) |
| 5 | Leadership (policy, roles, customer focus) |
| 6 | Planning (**risks and opportunities**, quality objectives) |
| 7 | Support (resources, competence, documented information) |
| 8 | Operation (design, purchasing, production, release) |
| 9 | Performance evaluation (monitoring, internal audit, management review) |
| 10 | Improvement (nonconformity, corrective action) |

Key changes vs 2008: **risk-based thinking** replaced "preventive action", and the standard explicitly follows **PDCA**. Certification shows a *system*, not that every product is excellent.

### Example
A Pune auto-component supplier is ISO 9001 certified (often required by OEM customers). Its internal audits, control plans and corrective-action records are what the certification body checks; OEM-specific standards such as IATF 16949 sit on top of ISO 9001 for automotive.

### In the news
See news box. Boeing held process documents, yet the plug was opened without the required paperwork: a QMS works only when its procedures are followed and audited in practice.

### Interview angle
> [!question] How it is asked
> "What does ISO 9001 certification mean for a supplier and what does it not guarantee?"

> [!tip] Strong answer includes
> - QMS standard, clauses 4–10, PDCA, risk-based thinking
> - Certification by independent body, surveillance audits
> - Limitation: certifies system and consistency, not product excellence
> - Value to buyers: supplier qualification and reduced audit burden

---

## 3. Quality Control vs Quality Assurance
> 🔴 Tier 1 · _Tracker hint:_ QC = product inspection; QA = process prevention

### Definition
| | Quality Control (QC) | Quality Assurance (QA) |
|---|---|---|
| Focus | The **product** | The **process and system** |
| Nature | Detection, reactive | Prevention, proactive |
| Activities | Inspection, testing, sampling, SPC | Procedures, audits, training, supplier approval |
| Timing | During or after production | Before and throughout |
| Who | Inspectors and lab | Everyone, led by QA function |
| Question | "Is this unit good?" | "Will our process produce good units?" |

Quality Control is a part of the quality-management system, and QA gives confidence that requirements will be met. A third idea, **quality planning**, sets objectives before work starts. Cost logic: it is cheaper to prevent than to detect and far cheaper than a customer complaint (the 1-10-100 rule of thumb).

### Example
A pharma plant: QC lab tests every batch (assay, dissolution); QA reviews batch records, validates the process and audits GMP compliance, and decides batch release. A change to a process is QA's domain; testing the batch is QC's.

### In the news
See news box. At Boeing, the QC step (inspection of the door closure) could not occur because documentation that triggers inspection was missing, a QA/system failure, not only a QC one.

### Interview angle
> [!question] How it is asked
> "Difference between QA and QC? Give an example."

> [!tip] Strong answer includes
> - The product vs process distinction and detect vs prevent
> - A clean example (batch testing vs GMP/process validation)
> - That both are needed, and prevention is cheaper
> - Link to cost of quality

---

## 4. PDCA Cycle
> 🔴 Tier 1 · _Tracker hint:_ Plan→Do→Check→Act; Deming's wheel; link to Kaizen

### Definition
**PDCA** (Shewhart cycle, popularised by Deming as the Deming wheel) is the iterative loop of improvement:
- **Plan:** define the problem, collect data, find root cause, set target and countermeasures.
- **Do:** implement on a small scale (pilot).
- **Check (Study):** compare results with target, using data.
- **Act:** standardise if successful (update SOP), otherwise revise the plan and repeat.

**Kaizen** is the culture of many small continuous improvements; PDCA is its operating method. Related: **SDCA** (standardise-do-check-act) holds the gains; **DMAIC** is the Six Sigma version; the **A3 report** documents PDCA on a page. ISO 9001 is built on PDCA.

### Example
Dispatch damage at a distribution centre is 4% of cartons. Plan: Pareto shows 70% of damage is from top-heavy stacking; target 1.5%. Do: pilot new stacking pattern and corner boards on one dock. Check: damage drops to 1.4%. Act: update the SOP for all docks and begin a new cycle on the next biggest cause.

### In the news
See news box. NTSB's corrective view for Boeing is effectively a failed "Act": nonconformance had been repeated and recorded but not durably corrected, which the NTSB called "repetitive and systemic".

### Interview angle
> [!question] How it is asked
> "Explain PDCA with an example from your experience or a case."

> [!tip] Strong answer includes
> - Four stages with the content of each
> - A quantified before/after example
> - Standardisation step (Act) to hold gains
> - Link to Kaizen and Six Sigma DMAIC

---

## 5. Cost of Quality (CoQ)
> 🔴 Tier 1 · _Tracker hint:_ Prevention + Appraisal + Internal Failure + External Failure costs

### Definition
**Cost of Quality** = Cost of Good Quality (conformance) + Cost of Poor Quality (non-conformance):

$$CoQ = \text{Prevention} + \text{Appraisal} + \text{Internal failure} + \text{External failure}$$

| Category | Examples |
|---|---|
| Prevention | Training, quality planning, supplier development, process design |
| Appraisal | Inspection, testing, audits, calibration |
| Internal failure | Scrap, rework, re-inspection, downtime (found before shipping) |
| External failure | Returns, warranty, recalls, complaints, lost customers, liability |

Principle: investing more in prevention lowers failure costs by more than it adds; **external failure** is the most expensive (hidden: reputation). Typical manufacturing CoQ ranges widely; many firms are surprised it is a **double-digit % of sales**.

### Example
Sales ₹100 crore. Prevention ₹2 cr, appraisal ₹3 cr, internal failure ₹4 cr, external failure ₹6 cr. CoQ = 2+3+4+6 = **₹15 crore = 15% of sales**; poor-quality cost = 4+6 = ₹10 crore. If ₹1 crore more is spent on prevention and it cuts failure cost by ₹3 crore, CoQ falls to 15+1-3 = ₹13 crore.

### In the news
See news box. Boeing's quality problems carried huge external-failure costs (grounded aircraft, production caps, investigations), far beyond what prevention (documentation discipline, training) would have cost. The figures are not given here; the point is directional.

### Interview angle
> [!question] How it is asked
> "How would you convince the CFO to spend more on quality?"

> [!tip] Strong answer includes
> - The four CoQ categories with examples
> - Show current CoQ (as % of sales) and the failure split
> - Prevention ROI example with numbers
> - Include hidden costs (lost customers, brand)

---

## 6. Acceptance Sampling
> 🔴 Tier 1 · _Tracker hint:_ AQL, OC curves, sampling plans (single, double, sequential)

### Definition
**Acceptance sampling** decides whether to accept or reject a **lot** by inspecting a sample, used when testing is destructive or 100% inspection is costly (and imperfect).

- **AQL (Acceptable Quality Level):** the worst quality level considered acceptable as a process average (for example 1% defective). **LTPD/RQL** is the level the consumer wants rejected.
- **Single sampling plan (n, c):** take n units, accept the lot if defectives ≤ c.
- **Double sampling:** a smaller first sample, with a second sample if inconclusive; **sequential** samples unit by unit until a decision.
- **OC (Operating Characteristic) curve:** plots probability of acceptance $P_a$ against the lot defective rate p. Larger n and smaller c make the curve steeper.
- **Producer's risk** α (rejecting a good lot at AQL), **consumer's risk** β (accepting a bad lot at LTPD).
- Standards: ANSI/ASQ Z1.4 (MIL-STD-105E) and ISO 2859.

Using the Poisson approximation: $P_a = \sum_{k=0}^{c} \frac{e^{-np}(np)^k}{k!}$.

### Example
Plan n = 50, c = 2. At p = 1%: λ = 0.5, $P_a = e^{-0.5}(1+0.5+0.125) = 0.6065 \times 1.625 = 0.986$. At p = 5%: λ = 2.5, $P_a = e^{-2.5}(1+2.5+3.125) = 0.0821 \times 6.625 = 0.544$. So good lots are nearly always accepted, but a 5%-defective lot still passes about 54% of the time: a weak plan against bad lots. Increase n to tighten.

### In the news
See news box. Sampling does not help if the defect is a *process omission* (missing bolts); every unit needed verification of a critical characteristic, so 100% inspection or error-proofing was warranted.

### Interview angle
> [!question] How it is asked
> "What is AQL and how do you choose a sampling plan for incoming components?"

> [!tip] Strong answer includes
> - AQL, n and c, producer and consumer risk
> - OC curve intuition with a number
> - When sampling is inappropriate (critical defects, safety-critical items)
> - Alternatives: supplier certification and SPC, skip-lot, 100% automated inspection

---

## 7. Deming's 14 Points
> 🔴 Tier 1 · _Tracker hint:_ Key principles for transformation; constancy of purpose

### Definition
W. Edwards Deming's 14 points for management ("Out of the Crisis", 1982):
1. Create **constancy of purpose** for improvement.
2. Adopt the new philosophy; refuse delay and mistakes.
3. **Cease dependence on inspection** to achieve quality.
4. End awarding business on **price tag alone**; use single suppliers with trust.
5. Improve constantly and forever the system of production and service.
6. Institute training on the job.
7. Institute leadership.
8. **Drive out fear.**
9. Break down barriers between departments.
10. Eliminate slogans and exhortations.
11. Eliminate numerical quotas and management by objectives (numbers only).
12. Remove barriers to pride of workmanship.
13. Institute education and self-improvement.
14. Put everybody in the company to work on the transformation.

Deming also stressed the **System of Profound Knowledge** (appreciation of a system, variation, theory of knowledge, psychology) and that about 94% of problems belong to the *system* (management), not workers (a figure often attributed to Deming).

### Example
Point 4 in action: Toyota-style long-term supplier partnerships, rather than annual lowest-bid awards; point 3: building error-proofing (poka-yoke) into the line so inspection is not the main safeguard.

### In the news
See news box. Point 8 (drive out fear) and 12 matter: where staff cannot raise concerns, defects escape. Boeing's NTSB finding on training, guidance and oversight maps to points 6, 7 and 3.

### Interview angle
> [!question] How it is asked
> "Name some of Deming's 14 points and say which you would apply in a distribution company."

> [!tip] Strong answer includes
> - Naming 5–6 points accurately, not reciting all
> - Grouping them: leadership, system, people, suppliers
> - Applying selectively with an example (point 4 supplier partnerships, point 11 quotas and gaming)
> - Mentioning common-cause vs special-cause variation

---

## 8. Juran's Quality Trilogy
> 🔴 Tier 1 · _Tracker hint:_ Quality planning, control, improvement

### Definition
Joseph Juran defined quality as **fitness for use** and structured quality management in a trilogy (like financial management: budgeting, control, improvement):

| Process | Purpose | Key activities |
|---|---|---|
| **Quality planning** | Design processes that meet customer needs | Identify customers, needs, product features, process design, transfer to operations |
| **Quality control** | Hold the process at the planned level | Monitor performance, compare with goals, act on the difference (fix sporadic spikes) |
| **Quality improvement** | Break through to a new, better level | Chronic problems, project-by-project, **Pareto principle** (vital few vs trivial many) |

The **Juran trilogy diagram** shows performance with a sporadic spike (fixed by control) and a chronic level of waste (reduced by improvement projects). Juran also stressed management's role: he said most quality problems are management-controllable.

### Example
A dairy has chronic 3% packet leakage (chronic waste) and occasional spikes to 8% when a sealing jaw wears (sporadic). Control: SPC and maintenance fix the spikes. Improvement: a project on film quality and sealing temperature cuts the chronic level to 1%. Planning: the next packaging line is designed with those specs from day one.

### In the news
See news box. The FAA found repeated nonconformances at Boeing and its supplier; a chronic problem that control alone had not solved, calling for improvement projects and planning at the process level.

### Interview angle
> [!question] How it is asked
> "What are the three parts of Juran's trilogy and how do they differ?"

> [!tip] Strong answer includes
> - Planning, control, improvement defined
> - Sporadic vs chronic problems
> - Pareto principle and fitness for use
> - Contrast with Crosby (zero defects) or Deming (system and variation)

---

## 9. Zero Defects Philosophy
> 🔴 Tier 1 · _Tracker hint:_ Crosby; conformance to requirements; cost of non-conformance

### Definition
Philip Crosby's "Quality is Free" (1979). **Four absolutes of quality:**
1. Quality means **conformance to requirements** (not goodness or luxury).
2. Quality comes from **prevention**, not appraisal.
3. The performance standard is **zero defects**: "do it right the first time", not "acceptable" error levels.
4. The measure of quality is the **price of non-conformance** (cost of poor quality).

Crosby's 14-step programme and Quality Management Maturity Grid support it. "Quality is free" means the money spent on prevention is repaid by avoided failure costs. Criticism: zero defects can be read as a slogan; Deming criticised slogans. Six Sigma gives a measurable form: **3.4 defects per million opportunities (DPMO)** at 6σ (with the standard 1.5σ shift).

### Example
A "99% good" process sounds fine, but 1% = **10,000 DPMO**. If an airline handles 1 million bags, 1% mishandled means 10,000 bags every period. At 3.4 DPMO the figure would be 3.4 bags.

### In the news
See news box. For a safety-critical product such as an aircraft door closure, a "zero defects" requirement is non-negotiable: four missing bolts is a conformance failure on a critical characteristic.

### Interview angle
> [!question] How it is asked
> "Is zero defects realistic? How does it relate to Six Sigma?"

> [!tip] Strong answer includes
> - Crosby's four absolutes
> - Zero defects as a standard and mindset; Six Sigma as the measurable approach (3.4 DPMO)
> - Nuance: cost-benefit for non-critical features, no tolerance for safety-critical ones
> - "Quality is free" with a cost-of-quality link

---

## 10. Quality Audits
> 🔴 Tier 1 · _Tracker hint:_ Internal, external, supplier audits; audit checklist; corrective action

### Definition
A **quality audit** is a systematic, independent, documented examination of whether activities and results comply with planned arrangements (ISO 19011 gives audit guidance).

| Type | Who audits | Purpose |
|---|---|---|
| First-party (internal) | Own trained auditors | Check QMS compliance and prepare for external audits |
| Second-party (supplier) | The customer audits its supplier | Qualify and monitor suppliers (process, product, system audits) |
| Third-party (external) | Certification body or regulator | Certification (ISO 9001), regulatory approval |

**Audit process:** plan and scope → checklist from standard and procedures → opening meeting → evidence (documents, observation, interviews, sampling) → findings classified (**major nonconformity**, **minor nonconformity**, observation) → closing meeting → report → **corrective action (CAPA)** with root cause (5-Why, fishbone), correction, due date and **verification of effectiveness**.

### Example
A supplier audit by an OEM finds: (a) calibration of a torque wrench overdue, minor; (b) no control on a critical weld parameter, major. The supplier must submit a root-cause analysis, containment and corrective action within, say, 30 days, and the OEM verifies the effectiveness at a follow-up audit.

### In the news
See news box. The FAA audit of Boeing and Spirit AeroSystems is a real second-/third-party audit with 90 days for a corrective-action plan, and the NTSB later judged the FAA's own oversight of repeated nonconformance to be inadequate.

### Interview angle
> [!question] How it is asked
> "How would you audit a new supplier before awarding a contract?"

> [!tip] Strong answer includes
> - Types of audit and the process steps
> - Checklist areas: QMS, process control, calibration, traceability, capacity, ESG
> - Classification of findings and CAPA with verification
> - Risk-based frequency and supplier scorecards

---

## 11. ⭐ Advanced: Process Capability & Statistical Process Control
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**SPC** monitors process variation with **control charts**: the centre line is the process mean, limits are at ±3σ. Points beyond limits or non-random patterns signal **special-cause** variation. For an X-bar chart with subgroup size n: $UCL/LCL = \bar{\bar{X}} \pm A_2 \bar{R}$ (for n = 5, $A_2 = 0.577$).

**Process capability** compares process spread with specification limits:

$$C_p = \frac{USL - LSL}{6\sigma}, \qquad C_{pk} = \min\left(\frac{USL-\mu}{3\sigma}, \frac{\mu-LSL}{3\sigma}\right)$$

$C_{pk} \ge 1.33$ is a common minimum (many auto customers ask for 1.67). Control limits come from the process; specification limits come from the customer: never mix them.

### Example
Shaft diameter spec 10.0 ± 0.6 mm (LSL 9.4, USL 10.6), σ = 0.15, mean μ = 10.1. $C_p = 1.2/0.9 = 1.33$. $C_{pk} = \min((10.6-10.1)/0.45,\ (10.1-9.4)/0.45) = \min(1.11, 1.56) = 1.11$. The process is capable in spread but off-centre; centring to 10.0 gives $C_{pk} = 1.33$. X-bar chart: grand mean 50, $\bar{R}$ = 4, n = 5: limits = 50 ± 0.577 x 4 = 50 ± 2.31, so **47.69 to 52.31**.

### In the news
See news box. SPC would not catch a process step that never happened (missing bolts), but it is the mainstream tool for variation-based defects and a supplier-quality staple; the lesson is to match the control method to the failure mode.

### Interview angle
> [!question] How it is asked
> "What is the difference between Cp and Cpk?" or "The process is in control but we still get rejections. Why?"

> [!tip] Strong answer includes
> - Control limits vs specification limits
> - Cp (potential) vs Cpk (actual, includes centring) with a calculation
> - In control but not capable: reduce variation or recentre
> - Common vs special causes and how Deming's view applies

---

## 12. ⭐ Advanced: Six Sigma DMAIC & FMEA
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Six Sigma** is a data-driven programme to cut variation and defects, with belts (Yellow, Green, Black, Master Black Belt). **DMAIC:** **D**efine (problem, CTQ, project charter), **M**easure (baseline, measurement-system analysis), **A**nalyse (root cause: fishbone, 5-Why, Pareto, hypothesis tests), **I**mprove (solutions, pilot, DOE), **C**ontrol (control plan, SPC, SOPs). Metrics: DPMO, sigma level, yield, rolled throughput yield $RTY = \prod y_i$.

**FMEA (Failure Mode and Effects Analysis)** ranks risks before they occur: 

$$RPN = Severity \times Occurrence \times Detection$$

each scored 1–10 (detection 10 = hardest to detect). Prioritise high RPN (and high severity regardless of RPN) for corrective actions.

### Example
FMEA of a fastener step: failure "bolt not installed", severity 9, occurrence 3, detection 8 (no check): RPN = 9 x 3 x 8 = **216**. Add a torque-confirmation gate that alerts if torque is not recorded: detection improves to 2, RPN = 9 x 3 x 2 = **54**. RTY example: 3 steps with yields 98%, 96% and 95%: RTY = 0.98 x 0.96 x 0.95 = **89.4%**.

### In the news
See news box. A properly run FMEA would score "fastener not installed during rework with no documentation" as high severity, and error-proofing or a hard-stop check would be the response.

### Interview angle
> [!question] How it is asked
> "Walk me through a DMAIC project to reduce order errors in a warehouse."

> [!tip] Strong answer includes
> - Each DMAIC phase with the tool used
> - A quantified baseline and target (DPMO or error %)
> - FMEA/RPN to prioritise risks, and poka-yoke as a fix
> - Control phase to sustain the gains: SOP, SPC, audits

---
## 🔗 Go deeper: expansion notes
- [[157 Business Excellence Models & Quality Awards|Business Excellence Models & Quality Awards]]
- [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)|Acceptance Sampling & Measurement System Analysis (Gauge R&R)]]
- [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)|Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]
