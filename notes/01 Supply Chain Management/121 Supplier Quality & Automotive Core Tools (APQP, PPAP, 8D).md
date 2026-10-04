---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)

⬅ [[120 Integrated Business Planning (IBP) & S&OP Maturity]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[122 Spend Analysis, Savings & Procurement Maturity]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. IATF 16949 & the Automotive Quality Ecosystem]]
2. [[#2. APQP: Advanced Product Quality Planning (Five Phases)]]
3. [[#3. PPAP: The 18 Elements and Five Submission Levels]]
4. [[#4. FMEA (Design and Process) and the Link to Control Plans]]
5. [[#5. Control Plan and Process Flow]]
6. [[#6. MSA and SPC: Measurement and Process Capability]]
7. [[#7. Incoming Inspection, AQL Sampling and Quality Gates]]
8. [[#8. 8D Problem Solving and the SCAR]]
9. [[#9. Supplier Audits: System, Process (VDA 6.3) and Product]]
10. [[#10. Supplier Rating: PPM, Delivery, Responsiveness and Consequences]]
11. [[#11. Supplier Development, New-Part Launch and SQE Role]]
12. [[#12. India Auto Clusters and Tyre-Industry Quality (CEAT, JBM Context)]]
13. [[#13. ⭐ Advanced: Cost of Poor Supplier Quality, Chargebacks and Sub-Tier Control]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's component base keeps growing while one cheap part can still stop a line
> **India's auto-component industry (FY25 and FY26).** ACMA reported FY25 turnover of **₹6.73 lakh crore (US$80.2 billion), up 9.6%**, with exports of US$22.9 billion; OEM supplies were ₹5.70 lakh crore and the aftermarket ₹99,948 crore. A July 2026 industry-review report put FY2025-26 turnover at **₹7.60 lakh crore (US$85.9 billion), up 12.7%**, with exports of about US$24 billion. More tier-1 and tier-2 volume means more suppliers that OEMs must qualify, audit and rate. ([ACMA press release FY25](https://www.acma.in/uploads/press-release/Press%20Release%20FY25.pdf); [AutoGuide India on the FY2025-26 review](https://www.autoguideindia.com/reports/acma-indian-auto-component-industry-fy2025-26-growth-report/))
>
> **Nexperia chip crisis (Sep-Oct 2025).** The Dutch government took control of Nexperia on 30 September 2025, and China imposed export controls on its Chinese factories on 4 October. Nexperia sells about 60% of its output to the auto industry (US$2.06 billion revenue in 2024); industry groups warned stocks might last only a few weeks. A basic, low-cost discrete chip sitting in the sub-tier became the single point of failure for car lines worldwide. ([Yahoo Finance explainer](https://finance.yahoo.com/news/nexperia-chip-crisis-know-062732843.html))
>
> **Recalls as the cost of escapes.** Maruti Suzuki recalled **16,041 vehicles (Baleno 11,851 and Wagon R 4,190) on 25 March 2024** over a suspected defect in the fuel pump motor, built July-November 2019. Globally, iSeeCars data from NHTSA showed **Ford with 153 recalls in 2025**, the most of any automaker (study published 8 April 2026). ([S&P Global Mobility](https://autotechinsight.spglobal.com/news/5274950/maruti-suzuki-india-recalls-16041-vehicles-over-fuel-pump-motor-defect); [CBS Detroit](https://www.cbsnews.com/detroit/news/ford-leads-automakers-153-recalls-2025/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. IATF 16949 & the Automotive Quality Ecosystem
> 🔴 Tier 1 · _Key points:_ ISO 9001 + automotive extras, customer-specific requirements, 3-year certificate, core tools

### Definition
**IATF 16949:2016** is the automotive quality management standard maintained by the International Automotive Task Force (OEMs plus trade bodies). It does not stand alone: it is an add-on to **ISO 9001:2015** and replaced **ISO/TS 16949** in October 2016. Certificates are issued by IATF-recognised certification bodies for **manufacturing sites** that do value-adding work on automotive parts, last **three years**, and are confirmed by annual surveillance audits. Beyond ISO 9001 it adds requirements on:
- **Product safety, embedded software, and traceability** (including sub-tier control).
- **Risk-based thinking, contingency plans** (a plan for supply failure, utility loss, labour issues).
- **Customer-specific requirements (CSRs)**: each OEM (Tata Motors, Mahindra, Maruti Suzuki, Hyundai, global OEMs) layers its own rules on top, for example PPAP level, escalation levels, or special approvals.
- **Use of the five core tools**: **APQP** (planning), **PPAP** (approval), **FMEA** (risk), **MSA** (measurement), **SPC** (process control), plus the control plan.
- **Supplier management**: second-party audits, supplier performance monitoring, development of suppliers with poor performance.

Core-tool owners: AIAG (US) with VDA (Germany) publish the manuals. **VDA 6.3** is the German process audit; **ISO 9001** is the base; **ISO 14001** and **ISO 45001** are commonly asked for alongside.

### Example
A Pune sheet-metal supplier wants a new bracket order from an OEM. Gate sequence: (1) IATF 16949 certificate or documented plan to obtain it; (2) OEM-specific supplier assessment (VDA 6.3 or its own checklist); (3) APQP on the part; (4) PPAP approval; (5) series supply under a scorecard. Skipping a gate shifts risk to the OEM line, where a stoppage costs far more than the audit.

### In the news
See news box. As ACMA's turnover climbs past ₹7 lakh crore, an OEM's supplier base grows more tiers deep; IATF 16949, CSRs and sub-tier traceability are the tools that keep that depth visible.

### Interview angle
> [!question] How it is asked
> "What is IATF 16949 and how is it different from ISO 9001?" or "What would you check before onboarding a new auto-component supplier?"

> [!tip] Strong answer includes
> - IATF 16949 = ISO 9001 plus automotive requirements, with customer-specific requirements on top
> - Five core tools named and one line on each (APQP, PPAP, FMEA, MSA, SPC)
> - Certification is site-specific, 3-year cycle with surveillance
> - Links to the broader [[011 Quality Management (TQM)|quality management note]] and the [[131 Automotive Supply Chain - JIT, Tiers & EVs|automotive supply chain note]]

---
## 2. APQP: Advanced Product Quality Planning (Five Phases)
> 🔴 Tier 1 · _Key points:_ Plan and define, product design, process design, validation, launch and feedback

### Definition
**APQP** is a structured method to plan a new part so that quality is designed in before the first production run. It was created in the late 1980s-90s by Ford, GM and Chrysler working with ASQC, and is run as a cross-functional team using timing charts. Five phases:

| Phase | Name | Typical outputs |
|---|---|---|
| 1 | **Plan and define** the programme | Voice of customer, design goals, reliability and quality goals, preliminary bill of materials, process flow, special product and process characteristics, management support |
| 2 | **Product design and development** (verification) | DFMEA, design for manufacturing and assembly, design verification, prototype control plan, drawings and specifications, new equipment and gauge requirements |
| 3 | **Process design and development** (verification) | Packaging standards, process flow chart, floor-plan layout, **PFMEA**, pre-launch control plan, work instructions, MSA plan, preliminary process capability plan |
| 4 | **Product and process validation** | Significant production run, **MSA**, process capability study, **PPAP** submission, production validation testing, packaging evaluation, **production control plan**, quality planning sign-off |
| 5 | **Launch, assessment and corrective action** | Reduced variation, improved customer satisfaction, delivery and service, lessons learned |

Each phase ends with a **gate review**. The five core tools sit inside the phases: DFMEA in 2, PFMEA and control plan in 3, MSA and SPC and PPAP in 4. The long-standing reference is AIAG's **APQP (2nd edition, 2008)**; AIAG and VDA have since worked on joint APQP/control-plan guidance, so confirm the edition the customer specifies.

### Example
A tyre-valve or wheel-rim supplier takes a new part for a hatchback launch. Phase 1: customer drawing, annual volume 600,000, special characteristic = leak rate. Phase 2: DFMEA on seal geometry. Phase 3: PFMEA on the machining and leak-test step, pre-launch control plan. Phase 4: 300-piece run, Cpk study on the critical diameter, PPAP. Phase 5: feedback after launch, with a 90-day early-production containment. If a critical characteristic fails capability in Phase 4, launch moves or a 100% inspection is added until it is fixed.

### In the news
See news box. Rising component volumes and EV platform launches mean more new part numbers; each one passes through this five-phase gate path.

### Interview angle
> [!question] How it is asked
> "Walk me through how a supplier launches a new component for an OEM." or "What is APQP?"

> [!tip] Strong answer includes
> - Five phases in order with a deliverable per phase
> - Where DFMEA, PFMEA, control plan, MSA, SPC and PPAP fall
> - Cross-functional team and gate reviews, not a quality-department activity
> - Links to [[154 Product & Service Design - QFD, DFMA & Value Engineering|QFD and DFMA]] for the design phases

---
## 3. PPAP: The 18 Elements and Five Submission Levels
> 🔴 Tier 1 · _Key points:_ Evidence that the process can make conforming parts at rate; PSW; levels 1 to 5

### Definition
The **Production Part Approval Process (PPAP, AIAG 4th edition, 2006)** is the supplier's evidence package that it understands all customer requirements and can consistently meet them in a real production run. It is approved by the customer before volume shipments.

**18 elements:** 1 Design records; 2 Engineering change documents; 3 Customer engineering approval; 4 Design FMEA; 5 Process flow diagram; 6 Process FMEA; 7 Control plan; 8 MSA studies; 9 Dimensional results; 10 Material and performance test results; 11 Initial process studies; 12 Qualified laboratory documentation; 13 Appearance approval report (AAR); 14 Sample production parts; 15 Master sample; 16 Checking aids; 17 Customer-specific requirement records; 18 **Part Submission Warrant (PSW)**.

**Submission levels** (customer specifies; default is Level 3):

| Level | What is submitted |
|---|---|
| 1 | PSW only (appearance report if required) |
| 2 | PSW with product samples and limited supporting data |
| 3 | PSW with product samples and **complete** supporting data (default) |
| 4 | PSW and other items as defined by the customer |
| 5 | PSW with samples and complete data, **reviewed at the supplier's site** |

**Significant production run:** typically 1 to 8 hours of production, at least **300 consecutive parts**, made with production tooling, gauges, process, operators and rate. **Initial process study acceptance (Cpk/Ppk):** above 1.67 acceptable; 1.33 to 1.67 may be acceptable with customer review; below 1.33 not acceptable. **Dispositions:** Approved, Interim approval (limited time or quantity while issues are closed), Rejected. **Resubmission triggers:** new part, engineering change, tooling change or refurbishment, new location or sub-supplier, process change, long tooling inactivity, and correction of a significant quality problem.

### Example
Supplier submits Level 3 for a bracket. Dimensional results show 300 pieces and a critical hole position with Ppk 1.45. Customer disposition: **interim approval** for 3 months or 50,000 pieces with 100% check on that characteristic until Ppk reaches 1.67. If the supplier then moves the press to a second plant, a **fresh PPAP** is needed because the location changed.

### In the news
See news box. The Nexperia episode illustrates the risk PPAP resubmission rules target: a change in a sub-tier source, location or material (here forced by export controls) must be declared and re-approved, not discovered at the line.

### Interview angle
> [!question] How it is asked
> "What is PPAP and when would a supplier have to resubmit?"

> [!tip] Strong answer includes
> - Purpose: evidence of capability at rate, not a paper exercise
> - The PSW as the signed summary; level 3 as default
> - 300-piece run and Cpk/Ppk thresholds (1.67, 1.33)
> - Resubmission triggers and interim approval as a controlled risk
> - Mention that PPAP packages are usually exchanged through customer supplier portals, with inspection results tracked in [[084 SAP QM & PM|SAP QM]]

---
## 4. FMEA (Design and Process) and the Link to Control Plans
> 🔴 Tier 1 · _Key points:_ DFMEA vs PFMEA, AIAG-VDA 7 steps, Action Priority, severity first

### Definition
**FMEA** identifies how a design (DFMEA) or process (PFMEA) can fail, what the effect would be, and what controls exist. The 2019 **AIAG-VDA FMEA handbook** uses a **7-step approach**: (1) planning and preparation, (2) structure analysis, (3) function analysis, (4) failure analysis (failure mode, effect, cause chain), (5) risk analysis, (6) optimisation, (7) results documentation. It replaces the classic $RPN = S \times O \times D$ ranking by **Action Priority (AP: High, Medium, Low)**, because RPN treats unequal risks as equal. The detailed scales and an RPN example are in [[008 Six Sigma & Quality Tools]]; this note focuses on the supplier-quality use.

**How FMEA drives the rest of the tool chain:**
- DFMEA flags **special characteristics** (safety, regulatory, fit and function) and design verification tests.
- PFMEA turns each failure mode into a **prevention control** (poka-yoke, tooling) and **detection control** (gauge, vision, torque monitoring) written into the **control plan**.
- Escapes found in the field or at the customer feed back into the FMEA (a "living document").
- A supplier's FMEA is checked in **PPAP** (elements 4 and 6) and in the **VDA 6.3** process audit (element P3).

### Example
Process: welding a nut onto a bracket. Failure mode: nut missing. Effect: assembly line stops (S = 8 at supplier level, safety not involved). Cause: operator skips pick. O = 4; current control: visual check, D = 5; RPN = 8 × 4 × 5 = **160**. Action: add a nut-presence sensor interlock (poka-yoke): D falls to 2, RPN = 8 × 4 × 2 = **64**. The same action goes into the control plan as the detection method with a reaction plan "stop and quarantine since last good check".

### In the news
See news box. A recall such as Maruti's 2024 fuel-pump-motor action is the cost of a failure mode that reached the customer; FMEA plus a capable control plan is the planning route to catching such modes earlier (the public notice does not state the root cause).

### Interview angle
> [!question] How it is asked
> "How do FMEA and the control plan relate?" or "How would you reduce the risk of a recurring defect?"

> [!tip] Strong answer includes
> - DFMEA vs PFMEA and who owns each
> - AIAG-VDA 2019 steps and Action Priority replacing RPN
> - FMEA outputs feed control plan, inspection frequency and gauge selection
> - Severity-led prioritisation and re-scoring after actions

---
## 5. Control Plan and Process Flow
> 🔴 Tier 1 · _Key points:_ Prototype, pre-launch, production; characteristics, methods, reaction plan

### Definition
A **control plan** is the written summary of how a part will be controlled at each process step. Three phases: **prototype**, **pre-launch** (extra checks during ramp-up) and **production**. Each line lists: process step, machine, **product and process characteristic** (flag special characteristics), specification and tolerance, **evaluation method** (gauge, sample size, frequency), **control method** (SPC, poka-yoke, first-off approval), and a **reaction plan** (what to do and who decides when a check fails).

It is built from the **process flow diagram** and PFMEA; any change to process, gauge or inspection frequency should update all three. A control plan is not an inspection plan alone: it covers prevention (maintenance, set-up approval, tool life) as well as detection.

### Example
Process step "bead-wire grommet fitting" at a tyre-component supplier, characteristic "inner diameter 1.00 ± 0.05 mm". Method: air gauge (MSA-approved), sample 5 pieces every hour, X-bar and R chart; reaction plan: if a point is out of control, stop the cell, segregate and 100% sort everything since the last good check, escalate to the production head. During pre-launch the sample is 5 every 15 minutes; once Ppk exceeds 1.67 for 3 consecutive months the frequency can be relaxed (agreed with the customer).

### In the news
See news box. Where a supplier changes a sub-tier part source quietly, the control plan's incoming-material control and traceability columns are what show whether the change would have been noticed.

### Interview angle
> [!question] How it is asked
> "What goes into a control plan and when do you update it?"

> [!tip] Strong answer includes
> - Columns: characteristic, method, frequency, reaction plan
> - Derived from PFMEA and process flow; updated on any change or escape
> - Prototype / pre-launch / production phases
> - Reaction plan with containment and responsibility

---
## 6. MSA and SPC: Measurement and Process Capability
> 🔴 Tier 1 · _Key points:_ Gauge R&R <10% good, ndc >= 5, Cpk/Ppk thresholds, control charts

### Definition
You cannot control what you cannot measure reliably. **MSA (AIAG MSA, 4th edition)** studies the gauge: **bias, linearity, stability** (location) and **repeatability and reproducibility (GR&R)** (spread). Acceptance rules of thumb:

| %GRR (of total variation) | Verdict |
|---|---|
| < 10% | Acceptable |
| 10% to 30% | Conditionally acceptable (cost, criticality, customer approval) |
| > 30% | Unacceptable, improve the measurement system |

and the number of distinct categories $ndc = 1.41 \times PV/GRR \ge 5$. Details and Python in [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]].

**SPC** monitors the process with control charts (X-bar and R, individuals, p and c charts) to separate common from special causes; see [[091 Statistical Quality Control (SQC)]]. **Capability:**

$$C_p = \frac{USL - LSL}{6\sigma}, \qquad C_{pk} = \min\left(\frac{USL-\mu}{3\sigma}, \frac{\mu - LSL}{3\sigma}\right)$$

$P_p$ and $P_{pk}$ use the overall (long-term) standard deviation and are what PPAP's initial process study reports; $C_{pk}$ uses within-subgroup variation and is used for ongoing control.

### Example
Bead-wire diameter 1.00 ± 0.05 mm (LSL 0.95, USL 1.05): mean 1.012, $\sigma$ = 0.011. $C_p = 0.10/0.066 = 1.52$; $C_{pk} = (1.05 - 1.012)/(0.033) = $ **1.15** (fails the 1.33 minimum; about 276 PPM out of spec on the upper side). Centre the process at 1.001 and reduce $\sigma$ to 0.0075: $C_{pk} = 2.18$, effectively zero defects. Gauge: GRR standard deviation 0.0021 against total variation 0.0150 gives **%GRR = 14%** (conditional), $ndc \approx 10$; as a share of the 0.10 mm tolerance, $6 \times 0.0021 / 0.10 = 12.6\%$.

### In the news
See news box. Fewer escapes need both a capable process and a gauge that can see the difference; recalls usually trace to one of the two.

### Interview angle
> [!question] How it is asked
> "A supplier shows Cpk of 1.8 on your part but you still get rejections. Why?"

> [!tip] Strong answer includes
> - Check the **measurement system**: a poor gauge can hide variation
> - Distinguish Cp (potential) and Cpk (centering), Pp/Ppk vs Cpk (long vs short term)
> - Short-run sampling (300 parts in one run) may not see tool wear or batch changes
> - Non-normal data, special causes, or a different characteristic failing

---
## 7. Incoming Inspection, AQL Sampling and Quality Gates
> 🔴 Tier 1 · _Key points:_ ISO 2859-1, code letter, Ac/Re, OC curve, skip-lot, ship-to-stock

### Definition
**Incoming (receiving) inspection** verifies that purchased parts meet specification before they reach the line. Methods: 100% inspection (critical or very small lots), **sampling by attributes** (ISO 2859-1 / ANSI Z1.4, tables by lot size and AQL), **sampling by variables** (ISO 3951), certificate-of-conformance checks, and **skip-lot / dock-to-stock** (no inspection for suppliers with proven history).

Reading the **AQL table** (General inspection level II, single sampling, normal): lot size gives a **code letter**, the letter gives sample size $n$, AQL gives **acceptance number** $Ac$ and **rejection number** $Re$. Switching rules: normal to **tightened** after 2 of 5 lots rejected; to **reduced** after 10 accepted lots with low defects and steady production; back to normal on a rejected lot. AQL is an agreed inspection reference, **not** a guarantee that delivered lots are at that quality; the protection against bad lots is the OC curve.

Probability of accepting a lot with true defect rate $p$ under plan $(n, c)$: $P_a = \sum_{k=0}^{c}\binom{n}{k}p^k(1-p)^{n-k}$.

### Example
Lot of 1,000 pieces: code letter J, $n = 80$, AQL 1.0%: $Ac = 2$, $Re = 3$. Accept if 2 or fewer defectives are found.

| True defect rate $p$ | $P_a$ |
|---|---|
| 0.5% | 99.2% |
| 1.0% | 95.3% |
| 2.0% | 78.4% |
| 4.0% | 37.5% |
| 6.5% | 10.1% |

A lot with 4% defects (40 bad pieces) still passes about 3 times in 8, which is why chronic defect suppliers need **supplier-side process control** (Cpk, PPM targets) rather than relying on receiving inspection. Receiving gates also include material tests: for a tyre plant, **Mooney viscosity and cure-curve checks** on rubber, tensile and coating tests on steel cord, ash and moisture tests on carbon black.

### In the news
See news box. A recall or line-stop traces back to escapes that passed sampling; a lot-by-lot sampling plan has limited power against a rare but severe defect.

### Interview angle
> [!question] How it is asked
> "Should we increase incoming inspection on a supplier with rising defects?"

> [!tip] Strong answer includes
> - Inspection does not build quality; use temporarily as containment (tightened inspection, 100% sort) while root cause is fixed
> - Understands AQL, OC curve and the risk to buyer and seller
> - Shift to process-based control: PPM, SCAR, audit, capability
> - Cost trade-off: inspection cost vs cost of escape to the line

---
## 8. 8D Problem Solving and the SCAR
> 🔴 Tier 1 · _Key points:_ D0 to D8, containment, root cause and escape point, permanent corrective action

### Definition
**8D** is a team-based corrective-action method from Ford (1987 "Team Oriented Problem Solving" manual). A **SCAR (Supplier Corrective Action Request)** is the formal request that asks the supplier to complete an 8D report within a deadline.

| Step | Purpose |
|---|---|
| **D0** | Plan, emergency response, decide whether 8D is needed |
| **D1** | Form a cross-functional team |
| **D2** | Describe the problem (5W2H, is / is-not, quantified) |
| **D3** | **Interim containment**: sort stock at supplier, in transit, at customer; certified-stock marking |
| **D4** | Root cause **and escape point** (why it was made and why detection failed): 5 Whys, fishbone, fault tree |
| **D5** | Choose and verify permanent corrective actions |
| **D6** | Implement and validate |
| **D7** | **Prevent recurrence**: update FMEA, control plan, work instructions, horizontal deployment to similar parts |
| **D8** | Recognise the team, close |

**Typical SCAR clock (illustrative, set by customer):** containment in 24 hours, initial analysis in 3 to 5 days, final report in 10 to 30 days. Quality of 8D is judged on the proof of root cause, effectiveness check, and updates to the FMEA and control plan (not just retraining).

### Example
At an OEM line, 12 welded brackets of a 18,000-piece lot have a missing weld nut; the line stopped for 40 minutes at 45 vehicles per hour (**30 vehicles** lost, illustrative contribution ₹1 lakh each = ₹30 lakh of margin at risk). D3: sort all stock: 18,000 pieces at 600 per inspector-hour is **30 inspector-hours**. D4: **why made**: the operator skipped the nut pick (no presence sensor); **why escaped**: the visual check sampled 5 per hour. D6: poka-yoke sensor and 100% automatic check; D7: PFMEA and control plan updated, same fix rolled to two sister lines.

### In the news
See news box. After a large recall such as 16,041 vehicles for a fuel-pump motor, the formal 8D/SCAR trail is how the OEM allocates cost and verifies that the supplier fix is permanent.

### Interview angle
> [!question] How it is asked
> "A supplier's part has a field failure. How do you run the response?" or "Walk through 8D."

> [!tip] Strong answer includes
> - Containment first (customer protected), then root cause
> - Both **occurrence** and **escape** root causes
> - Verification of corrective action and horizontal deployment
> - Link to [[008 Six Sigma & Quality Tools|root cause tools]] and cost-of-quality logic

---
## 9. Supplier Audits: System, Process (VDA 6.3) and Product
> 🔴 Tier 1 · _Key points:_ Three audit types, P1 to P7, 0/4/6/8/10 scoring, A/B/C grades, downgrade rule

### Definition
Second-party (customer) audits come in three types: **system audit** (QMS against ISO 9001 or IATF 16949 or VDA 6.1), **process audit** (does a specific process deliver conforming output; **VDA 6.3**), and **product audit** (finished-part check against drawing and customer requirements). **VDA 6.3** has seven process elements:

| Element | Focus |
|---|---|
| P1 | Potential analysis |
| P2 | Project management |
| P3 | Planning of product and process development (FMEA, control plan) |
| P4 | Realisation: sampling and series launch |
| P5 | Supplier management |
| P6 | Process analysis / production (turtle diagram per process step) |
| P7 | Customer care, service, customer satisfaction |

Each question is scored **10, 8, 6, 4 or 0**. Fulfilment degree $E = \dfrac{\text{points achieved}}{\text{points possible}} \times 100\%$. Common grading: **A: 90% or more** (quality capable), **B: 80% to under 90%** (conditionally capable), **C: below 80%** (not capable). A **zero on a starred question downgrades** the result regardless of the average (specific thresholds and starred questions depend on edition, 2016 or 2023, and customer). Findings carry action plans, deadlines and re-audit.

### Example
A plastics supplier is audited on 20 P6 questions: 9 score 10, 5 score 8, 3 score 6, 2 score 4, and 1 scores 0. Points = 90 + 40 + 18 + 8 + 0 = 156 out of 200: $E = $ **78%**, which is **grade C** even though 14 of 20 questions were strong. The single zero (say, no containment for nonconforming material) is a stop-ship type finding: the OEM puts the supplier on **new business hold** until a re-audit lifts it above 80%.

### In the news
See news box. The Nexperia case shows why VDA 6.3 element P5 (supplier management) matters: it tests whether a supplier knows and controls its own sub-tier sources.

### Interview angle
> [!question] How it is asked
> "How would you audit a supplier's process, and what makes a supplier fail?"

> [!tip] Strong answer includes
> - System vs process vs product audit
> - VDA 6.3 structure and scoring with the A/B/C idea
> - Downgrade logic on critical questions and an action-plan follow-up
> - Risk-based audit plan: frequency by supplier performance and criticality

---
## 10. Supplier Rating: PPM, Delivery, Responsiveness and Consequences
> 🔴 Tier 1 · _Key points:_ PPM formula, OTD, SCAR closure, weighted rating, business allocation

### Definition
Auto OEM scorecards typically combine **quality**, **delivery**, **responsiveness/cost**, with explicit **escalation levels**. Core measures:

$$PPM = \frac{\text{rejected parts}}{\text{parts received}} \times 10^6, \qquad OTD\% = \frac{\text{lines delivered in the agreed window}}{\text{lines due}} \times 100$$

Others: **line-stoppage hours** caused, **SCAR closure time**, **premium freight** caused, **PPAP on-time approval**, **cost savings delivered**. Weighted rating: $R = \sum w_i s_i$ (quality often 40-50% weight). Consequences: **bonus-malus** on business share (high rating gets new parts), **controlled shipping** (CS1: supplier adds extra sort; CS2: third-party sort at supplier's cost), **new business hold**, probation, and exit. Compare with the generic scorecard in [[002 Procurement & Strategic Sourcing]]; the automotive version is quality-gated and PPM-driven.

### Example
Supplier ships 250,000 parts in a month and 37 are rejected: **PPM = 148**. Rating weights: quality 40%, delivery 30%, responsiveness 15%, cost 15%. Supplier A scores 92, 88, 80, 85: $0.4(92) + 0.3(88) + 0.15(80) + 0.15(85) = $ **87.95**. Supplier B scores 70, 95, 90, 96: **84.4**. Despite high delivery and cost, B ranks lower because quality carries the highest weight; and if the OEM's gate is "quality score at least 75", B is also put on a quality improvement plan. Delivery: 188 on-time lines of 200 = **94% OTD**.

### In the news
See news box. With an industry of ₹6.73 lakh crore (FY25) and ₹7.60 lakh crore (FY26) turnover across many tiers, a numeric rating is the practical way for an OEM to compare thousands of suppliers and decide where to intervene.

### Interview angle
> [!question] How it is asked
> "Design a supplier rating system for an automotive OEM." or "A supplier has PPM of 600 against a target of 100. What do you do?"

> [!tip] Strong answer includes
> - PPM, OTD, responsiveness, cost, risk; weights that favour quality for safety parts
> - Escalation ladder and business-share consequences
> - Look at *own* causes too (drawing issue, late forecast changes)
> - Joint improvement plan with dates and a recovery criterion

---
## 11. Supplier Development, New-Part Launch and SQE Role
> 🔴 Tier 1 · _Key points:_ Supplier quality engineer, launch readiness, early production containment, joint kaizen

### Definition
**Supplier development** is investing OEM or buyer effort (engineers, training, tooling, finance) to raise a supplier's capability, usually for strategic or bottleneck categories (see [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]]). Typical programme: **diagnose** (VDA 6.3 gap, process walk), **prioritise** (Pareto on defects), **joint projects** (kaizen, SMED, poka-yoke, capability studies), **review** (monthly KPIs), **exit or reward**.

The **Supplier Quality Engineer (SQE)** (a typical entry job for operations graduates in auto OEMs) owns: PPAP review, audits, 8D follow-up, incoming inspection feedback, launch readiness reviews and the supplier's rating. **Launch controls** reduce risk in the first months: **safe launch / early production containment** (extra inspection for a fixed period or volume), run-at-rate (a supplier produces for several hours at the quoted line rate), and part-by-part sign-off of **special characteristics**. Lean tools support this (see [[007 Lean Manufacturing]] and [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]]).

### Example
A Chennai tier-2 casting supplier has a scrap rate of 3.2% (32,000 PPM) and an OEM-assigned PPM target of 500 on delivered parts. SQE plan: 100% X-ray on the critical wall thickness (containment), a **run-at-rate** of 8 hours at 1,200 pieces per hour, PFMEA revision to add die-temperature control (prevention), then a 6-month review with Cpk > 1.33 as the exit criterion for the extra inspection. If scrap drops to 1.0% (10,000 PPM internally) while shipped PPM stays below 500, extra inspection is lifted.

### In the news
See news box. Growth from ₹6.73 lakh crore to ₹7.60 lakh crore in a year means many new part numbers and new suppliers, which is the workload that supplier-development and launch-readiness teams carry.

### Interview angle
> [!question] How it is asked
> "A critical supplier is chronically late and poor in quality. Fix it or exit it?"

> [!tip] Strong answer includes
> - Segment first: strategic or bottleneck supplier (develop) vs leverage (re-source)
> - Diagnose with data (audit, Pareto), not opinion
> - Joint plan with dates; resources from both sides; clear exit criterion
> - Dual-source or qualify an alternative in parallel (risk hedge)

---
## 12. India Auto Clusters and Tyre-Industry Quality (CEAT, JBM Context)
> 🔴 Tier 1 · _Key points:_ Pune, Chennai, NCR-Gurugram clusters; tyre quality specifics; sheet-metal and tooling suppliers

### Definition
India's component supply base is clustered around OEM plants:
- **Pune-Chakan-Pimpri:** passenger-vehicle and commercial-vehicle OEMs and a dense tier-1/tier-2 base of forgings, machining and sheet metal.
- **Chennai-Oragadam-Hosur:** car, truck and export hub with strong engine, transmission and tyre-linked ecosystems.
- **Gurugram-Manesar-Faridabad-Neemrana:** two-wheeler and small-car OEM clusters with sheet-metal, tooling and electronics suppliers (JBM-type sheet-metal and welded-assembly suppliers sit in this belt).

Cluster advantages: **short lead times, milk-run feasibility, joint problem-solving at the OEM line**; risks: single-region exposure (floods, labour unrest, local power).

**Tyre makers (CEAT, MRF, Apollo, JK Tyre) as both customer and supplier:** they buy natural rubber, synthetic rubber, carbon black, steel cord and bead wire, and sell to OEMs under OEM PPAP and IATF 16949 requirements. Typical quality gates: **cure-rheometer and Mooney checks** on rubber compound; **bead-wire and steel-cord tensile and brass-coating adhesion** tests; in-process **tyre uniformity and balance** (force variation) testing; X-ray and bead inspection; and batch traceability from compound to tyre code (DOT code).

### Example
A tyre plant buys steel cord from two suppliers. Supplier 1 (illustrative figures): 4 lots rejected for coating adhesion in a quarter out of 40 lots (10% lot rejection). Plant response: SCAR, tightened sampling, a joint process review of the brass-plating line, and a 60-day shift of 20% of volume to Supplier 2. Result tracked as **PPM, lot-acceptance rate and 8D closure time**; the cost of a single field tyre recall (rubber, labour, logistics, brand) is a multiple of the cord price difference, which is why the plant keeps both suppliers qualified instead of single-sourcing for a few rupees per kg.

### In the news
See news box. CEAT Specialty's integration of the CAMSO business (Ambernath plant at 105 tonnes per day and 90-95% utilisation, September 2026 report) shows how acquisitions bring a second quality system and supplier base to reconcile. ([Autocar Professional](https://www.autocarpro.in/feature/how-camso-is-reshaping-ceats-specialty-tyre-business-134873))

### Interview angle
> [!question] How it is asked
> "Describe a supplier quality problem you saw during your internship and how you handled it."

> [!tip] Strong answer includes
> - A concrete STAR story using the tools (PPM, 8D, containment, root cause)
> - Cluster logic: why proximity helps
> - Numbers: defect rate before/after, cost avoided, closure time
> - Honest role clarity: what you owned vs what the team did (link: [[051 Internship Learnings & Projects]])

---
## 13. ⭐ Advanced: Cost of Poor Supplier Quality, Chargebacks and Sub-Tier Control
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Cost of poor supplier quality (COPSQ)** includes: receiving inspection and sorting, rework, scrap, line stoppages, premium freight, engineering time, warranty and recall, and brand damage. It follows the standard **cost of poor quality** pyramid ([[011 Quality Management (TQM)|COPQ in TQM]]): failure cost rises steeply the later the defect is found (supplier plant, receiving, OEM line, customer field). OEM contracts therefore allow **chargebacks** (sorting and rework at pre-agreed rates), **line-stop recovery**, and shared **warranty** terms.

**Sub-tier control** extends the same tools down the chain: tier-1 must flow down IATF/PPAP requirements, maintain **supplier lists with sub-tier approvals**, approve changes in sub-tier source, location or process, and keep **traceability** by lot to the customer shipment. For electronics, **semiconductor and software content** needs **mapping of critical parts to their wafer fab and back-end plants** (see [[134 Electronics & Semiconductor Supply Chain]]). The risk side is covered in [[015 Supply Chain Risk & Resilience]].

### Example
A defective lot reaches the OEM line. Costs (illustrative): supplier sorting 30 inspector-hours at ₹400 = ₹12,000; OEM line stoppage of 30 vehicles at ₹1 lakh contribution = ₹30 lakh; premium freight for replacement parts ₹60,000; engineering time ₹40,000. Total = ₹12,000 + ₹30,00,000 + ₹60,000 + ₹40,000 = **₹31.12 lakh**, against an incoming-inspection saving of ₹12,000 per lot that tempts purchasing to skip checks. **Sorting is under 0.4% of the total**: the real cost is the line stop, so the sensible controls are prevention in the supplier plant and containment at the OEM.

### In the news
See news box. Nexperia showed that exposure can sit beyond the tier-1 contract, in a low-value chip from a single group; this is the case for mapping critical parts to their source sites before a disruption, not after.

### Interview angle
> [!question] How it is asked
> "How would you justify investing in supplier development when the supplier is just 2% of our spend?"

> [!tip] Strong answer includes
> - Spend is not the same as risk; compute the cost of a line stop or recall
> - Failure cost ladder: supplier, receiving, line, field
> - Contract tools: chargebacks, escalation, flow-down, sub-tier approval
> - Prevention and visibility investment vs inspection

---
