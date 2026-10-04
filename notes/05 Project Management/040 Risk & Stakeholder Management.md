---
tags: [project-management, tier1]
area: Project Management
topic: "Risk & Stakeholder Management"
tier: Tier 1
roles: Project Mgmt
status: complete
subtopics: 12
---
# Risk & Stakeholder Management

⬅ [[039 Scheduling Tools (CPM-PERT-Gantt)]] · [[_Index - Project Management|Project Management]] · [[041 Agile Project Management]] ➡

> **Area:** Project Management · **Priority:** 🔴 Tier 1 · **Target roles:** Project Mgmt

## Sub-topics in this note
1. [[#1. Risk Identification Techniques]]
2. [[#2. Qualitative Risk Analysis]]
3. [[#3. Quantitative Risk Analysis]]
4. [[#4. Risk Response Strategies]]
5. [[#5. Risk Register]]
6. [[#6. Contingency Reserve]]
7. [[#7. Stakeholder Register]]
8. [[#8. Power-Interest Grid]]
9. [[#9. Stakeholder Engagement Assessment Matrix]]
10. [[#10. Communications Plan]]
11. [[#11. ⭐ Advanced: Risk Appetite, Thresholds and Risk Burn-down]]
12. [[#12. ⭐ Advanced: Stakeholder Salience Model and RACI]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): CrowdStrike outage and India's project overruns
> **CrowdStrike outage (19 July 2024).** A faulty configuration update to CrowdStrike's Falcon Sensor ("Channel File 291") caused an out-of-bounds memory read and crashed about **8.5 million Windows systems** worldwide. Estimated losses: about **$5.4 bn for the top 500 US companies** (only roughly $540 m to $1.08 bn insured) and about **$550 m for Delta Air Lines**, which cancelled over 7,000 flights across five days. A single untested change in one vendor's software became a global operational risk. ([Wikipedia summary of sources](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages))
>
> **India's central infrastructure overruns (MoSPI report for July 2026, published 27 Aug 2026).** Of **1,775 central projects costing Rs 150 crore or more**, the cumulative cost overrun was **Rs 3,40,504 crore** (original cost Rs 33.70 lakh crore vs revised Rs 37.11 lakh crore, about 10%). Transport and logistics projects were 70% of the total. ([Swarajya](https://swarajyamag.com/news-brief/indias-1775-central-infrastructure-projects-face-rs-34-lakh-crore-cost-overrun))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Risk Identification Techniques
> 🔴 Tier 1 · _Tracker hint:_ Brainstorming, Delphi, SWOT for risk, checklist, interviews

### Definition
A **risk** is an uncertain event or condition that, if it occurs, has a positive (opportunity) or negative (threat) effect on project objectives. **Identification** is the iterative process of finding and documenting individual risks and sources of overall project risk. It is done early and repeated at every phase gate and review.

Main techniques:
- **Brainstorming:** a facilitated group generates many risks without criticism, then clusters them.
- **Delphi technique:** experts answer anonymous questionnaires in rounds; a facilitator shares the summarised answers until consensus. Anonymity removes the influence of seniority.
- **SWOT analysis:** Strengths/Weaknesses (internal) and Opportunities/Threats (external) are mined for risks.
- **Checklists:** lists built from past projects and lessons learned. Quick but never exhaustive.
- **Interviews and expert judgment:** one-to-one sessions with SMEs, vendors, operations staff.
- **Root cause analysis, assumption and constraint analysis, document review, Ishikawa diagrams.**
- **Risk Breakdown Structure (RBS):** categories (technical, external, organisational, PM) to prompt coverage.

Output: initial entries in the **risk register** (see [[#5. Risk Register]]) written in the form "Because of <cause>, <event> may occur, leading to <effect>".

### Example
A warehouse automation project for a 3PL in Pune. Brainstorming with the ops team lists: conveyor vendor slippage, software integration with the WMS, monsoon flooding of the dock, key-person dependency on one IT lead. A checklist from a previous project adds "statutory approvals (fire NOC) delayed". Writing the cause-event-effect form: "Because the WMS vendor has one integration engineer, he may become unavailable, delaying go-live by 4 weeks."

### In the news
See news box. CrowdStrike is a case of a risk that most affected firms never listed: dependency on one security vendor's update pipeline. A good identification workshop would ask "which single vendors can stop us?".

### Interview angle
> [!question] How it is asked
> "How do you identify risks at the start of a project?" or "Tell me about a risk you spotted early."

> [!tip] Strong answer includes
> - Several techniques, matched to context (Delphi for expert-heavy, brainstorming for team, checklists for repeat projects)
> - Cause-event-effect wording rather than vague worries
> - Repeating identification throughout the project, not once
> - Capturing opportunities as well as threats
> - Result lands in the register with an owner

---

## 2. Qualitative Risk Analysis
> 🔴 Tier 1 · _Tracker hint:_ Probability × Impact matrix; prioritization; risk urgency

### Definition
**Qualitative analysis** ranks identified risks quickly by assessing **probability** (likelihood of occurrence) and **impact** (effect on scope, schedule, cost, quality). No simulation is needed, so it is cheap and always done.

**Risk score** = Probability × Impact, on ordinal scales (for example 1 to 5 each, giving 1 to 25). A **probability-impact (P-I) matrix** colours the cells red, amber, green according to the organisation's risk thresholds.

| Score | Rating | Typical action |
|---|---|---|
| 15 to 25 | High (red) | Active response plan, senior review |
| 6 to 14 | Medium (amber) | Response plan, monitor |
| 1 to 5 | Low (green) | Watch list |

Other attributes used for prioritising: **urgency** (how soon the response must be acted on), **proximity** (how soon the risk could hit), **detectability**, **manageability**, **dormancy**, and **risk data quality assessment** (are the ratings based on facts or hunches?). Risks can also be categorised by RBS to find hot spots.

### Example
Scale 1 to 5. Monsoon flood at the dock: P = 4, I = 4, score = 16 (red). Vendor delay: P = 3, I = 5, score = 15 (red). Fire NOC delay: P = 2, I = 3, score = 6 (amber). IT lead leaves: P = 2, I = 4, score = 8 (amber). Ranking: flood, vendor, IT lead, NOC. If the flood is expected in two months but the vendor delay in two weeks, the vendor risk is more **urgent** though lower scored.

### In the news
See news box. The Rs 3.4 lakh crore overrun figure shows what happens when probability of delay is routinely rated "medium" but impact is never priced; qualitative rank without follow-up quantification understates large-project exposure.

### Interview angle
> [!question] How it is asked
> "How would you prioritise 40 risks?" or "What is a probability-impact matrix and what are its limits?"

> [!tip] Strong answer includes
> - Score = P × I with defined scales and thresholds agreed in advance
> - Urgency and proximity as a second filter
> - Limits: ordinal scales, subjectivity, equal scores for very different risks
> - Moving the top risks to quantitative analysis

---

## 3. Quantitative Risk Analysis
> 🔴 Tier 1 · _Tracker hint:_ Monte Carlo simulation; EMV = Probability × Impact ($)

### Definition
**Quantitative analysis** gives numerical effect of risks on overall objectives, used for the highest-priority risks and for overall schedule/cost exposure.

**Expected Monetary Value:**
$$EMV = P \times I$$
with threats as negative values and opportunities as positive. Project EMV is the sum of the risk EMVs and often sizes the **contingency reserve**.

**Decision tree analysis** takes the EMV of each branch, net of the cost of the option.

**Monte Carlo simulation** replaces single-point estimates with distributions (for example triangular or PERT: $E=\frac{O+4M+P}{6}$, $\sigma=\frac{P-O}{6}$). The model is run thousands of times, giving a probability curve (S-curve) of total cost or finish date. Output reads like "80% chance of finishing by day X". It also gives a **sensitivity (tornado) chart** showing which risk drives variance most. Tools: @RISK, Crystal Ball, Primavera Risk Analysis, or Excel with `RAND()`.

### Example
Threat: supplier strike, P = 30%, impact Rs 50 lakh, EMV = 0.30 × (-50) = **-15 lakh**. Opportunity: bulk-discount, P = 20%, benefit Rs 30 lakh, EMV = 0.20 × 30 = **+6 lakh**. Net EMV = -15 + 6 = **-9 lakh**, so about Rs 9 lakh of reserve is justified for these two alone.
Monte Carlo: three tasks with PERT mean 10, 12, 8 days = 30 days; the simulation may show P50 = 31 days and P80 = 35 days, so the committed date should be about 35 days for 80% confidence.

### In the news
See news box. Delta's roughly $550 m loss is the kind of low-probability, very high-impact tail that EMV averages hide; Monte Carlo and scenario analysis expose it better than a single expected value.

### Interview angle
> [!question] How it is asked
> "What is EMV?" "How would you decide the contingency for this project?" "Why is Monte Carlo better than a three-point estimate?"

> [!tip] Strong answer includes
> - EMV formula, with sign convention and a worked number
> - Monte Carlo yields a distribution and confidence levels (P50, P80), not a single date
> - Used only on top risks because data and effort are needed
> - Caveat: garbage in, garbage out; correlation between risks needs modelling

---

## 4. Risk Response Strategies
> 🔴 Tier 1 · _Tracker hint:_ Threats: Avoid, Transfer, Mitigate, Accept; Opportunities: Exploit, Share, Enhance, Accept

### Definition
A response is chosen for each prioritised risk so that overall exposure falls within appetite, at a cost proportional to the risk.

| Threat strategy | Meaning | Example |
|---|---|---|
| **Avoid** | Remove the cause or change the plan | Drop an unproven technology |
| **Transfer** | Shift impact (not removal) to a third party | Insurance, fixed-price contract, warranty |
| **Mitigate** | Reduce probability and/or impact | Second supplier, prototype, extra testing |
| **Accept** | Do nothing, active (contingency) or passive | Hold a reserve, or deal with it if it occurs |
| **Escalate** | Beyond the project's authority | Send to programme/sponsor |

| Opportunity strategy | Meaning |
|---|---|
| **Exploit** | Make sure it happens |
| **Share** | Give ownership to a partner best able to capture it |
| **Enhance** | Raise probability or benefit |
| **Accept** | Take it if it comes |

Plus a **fallback plan** (if the response fails) and **contingency plan** (triggered when a risk event occurs). **Secondary risks** (created by the response) and **residual risks** (left after the response) must be recorded.

### Example
Threat: monsoon flooding at the dock. Avoid: relocate the staging area to higher ground. Mitigate: raise pallets, flood barriers. Transfer: stock-in-transit insurance. Accept: hold Rs 5 lakh contingency. Opportunity: a client may expand scope, and Exploit means assigning the best planners to win it; Share means partnering with a larger integrator.

### In the news
See news box. After CrowdStrike, firms used **mitigate** (staged rollouts, canary groups, offline recovery images) and **transfer** (cyber insurance, contractual SLAs), showing that transfer covers only part of the loss because reputation stays with you.

### Interview angle
> [!question] How it is asked
> "What are the four responses to a negative risk? Give an example of each." "When would you accept a risk?"

> [!tip] Strong answer includes
> - All four threat and four opportunity strategies, correctly named
> - Cost-benefit logic: do not spend more on a response than the EMV it removes
> - Residual and secondary risks
> - Owner and trigger for the response

---

## 5. Risk Register
> 🔴 Tier 1 · _Tracker hint:_ Risk, probability, impact, response, owner, residual risk

### Definition
The **risk register** is the living log of every identified risk and its analysis and response. It is created in identification and updated through qualitative/quantitative analysis, response planning, implementation and monitoring.

Typical columns: ID, description (cause-event-effect), category (RBS), probability, impact, score, **urgency/proximity**, **response strategy and actions**, **owner**, **triggers/warning signs**, **contingency/fallback plan and cost**, **residual risk** score, **secondary risks**, status (open, closed, occurred), date raised and last reviewed.

Good practice: single named owner, reviewed at every status meeting, closed risks retained for lessons learned. Related reports: **risk report** (overall exposure and top risks for sponsors) and a **risk burn-down chart** (see the advanced section).

### Example
| ID | Risk | P | I | Score | Response | Owner | Residual |
|---|---|---|---|---|---|---|---|
| R1 | WMS vendor engineer unavailable, go-live slips 4 wks | 3 | 5 | 15 | Mitigate: cross-train second engineer | IT lead | 2×5 = 10 |
| R2 | Dock flooding | 4 | 4 | 16 | Avoid: relocate staging | Site manager | 1×4 = 4 |
Residual risk falls after the response is applied, which proves the response is worth its cost.

### In the news
See news box. After a large outage, regulators and boards asked for evidence that third-party software risk was on the register with a named owner; "not in the register" meant "not managed".

### Interview angle
> [!question] How it is asked
> "What goes into a risk register?" "How do you keep it from becoming shelfware?"

> [!tip] Strong answer includes
> - The fields: description, P, I, response, owner, triggers, residual risk
> - Regular review cadence and ownership
> - Link to the contingency reserve and lessons learned
> - Concise, cause-event-effect wording

---

## 6. Contingency Reserve
> 🔴 Tier 1 · _Tracker hint:_ For known-unknown risks; use triggers; vs management reserve

### Definition
**Contingency reserve** is the time/budget allowance, **included in the baseline**, to cover **identified risks** that are accepted or for which responses are planned ("known unknowns"). It is released by the project manager when a **trigger** (warning sign, risk event) occurs.

**Management reserve** is held **outside the cost baseline** (but within the project budget) for **unidentified risks** ("unknown unknowns"). Use needs senior management approval and a change to the baseline.

| | Contingency reserve | Management reserve |
|---|---|---|
| Covers | Identified (known-unknown) risks | Unforeseen (unknown-unknown) |
| In cost baseline? | Yes | No |
| Authority | Project manager | Sponsor / management |
| Sized by | EMV, Monte Carlo | Policy, percentage, judgment |

$$\text{Project budget} = \text{Cost baseline} + \text{Management reserve}$$
$$\text{Cost baseline} = \text{Work package estimates} + \text{Control-account contingency}$$

### Example
Work packages Rs 10 crore; contingency (from risk EMVs) Rs 1 crore; so baseline Rs 11 crore. Management reserve Rs 0.5 crore; project budget Rs 11.5 crore. A flood occurs (trigger), PM draws Rs 0.2 crore of contingency without approval. A new regulation nobody foresaw needs Rs 0.3 crore, so the PM asks for MR and the baseline is re-approved.

### In the news
See news box. Large public projects with revised costs about 10% over the original (Rs 3.4 lakh crore on Rs 33.7 lakh crore) show why unpriced contingency becomes a sunk-cost conversation later.

### Interview angle
> [!question] How it is asked
> "What is the difference between contingency and management reserve?" "How would you size contingency?"

> [!tip] Strong answer includes
> - Known vs unknown unknowns; inside vs outside baseline
> - Who can release it
> - Sizing from EMV or a P80 simulation
> - Reserve burn-down as a health indicator

---

## 7. Stakeholder Register
> 🔴 Tier 1 · _Tracker hint:_ Name, role, interest, influence, engagement strategy

### Definition
A **stakeholder** is any person, group or organisation that can affect, be affected by, or perceive itself to be affected by the project. The **stakeholder register** is the document of the *Identify Stakeholders* process (PMBOK Planning/Initiating).

Fields: **identification** (name, position, location, role, contact), **assessment** (major requirements, expectations, potential influence, phase of most interest), **classification** (internal/external, supporter/neutral/resistor, power/interest) and **engagement strategy**.

Sources: project charter, procurement documents, organisational charts, interviews, stakeholder analysis. It is a living document updated at each phase and when the team or environment changes. It feeds the stakeholder engagement plan and the communications plan. **Sensitive information** (for example "resistant") should be restricted.

### Example
Metro rail depot project. Sponsor (Director, high power, high interest, supporter): weekly steering update. Local residents' association (low power, high interest, resistor to noise): consultation meetings. Pollution control board (high power, low interest): compliance filings. Contractor foremen (low power, high interest): daily toolbox meeting.

### In the news
See news box. Delta and other airlines' stakeholders (passengers, crew, regulators) bore the outage consequences; teams that had them listed with channel and contact responded faster.

### Interview angle
> [!question] How it is asked
> "How do you identify and track stakeholders?" "Who would you list for an ERP rollout?"

> [!tip] Strong answer includes
> - Broad definition including external and indirect stakeholders
> - Register fields, including interest, influence, expectations and strategy
> - Update cadence and confidentiality
> - Leads to engagement and communications plans

---

## 8. Power-Interest Grid
> 🔴 Tier 1 · _Tracker hint:_ High power/high interest = manage closely; low/low = monitor

### Definition
The **Power-Interest grid** (Mendelow) plots stakeholders by **power** (authority/ability to influence) against **interest** (concern about outcomes) to decide the engagement effort. Related grids: power-influence, influence-impact.

| | Low interest | High interest |
|---|---|---|
| **High power** | **Keep satisfied** | **Manage closely** |
| **Low power** | **Monitor** (minimum effort) | **Keep informed** |

Stakeholders move between cells over time (for example a regulator becomes high-interest after an incident), so the grid is re-run. Limits: ignores attitude (supporter or opponent), legitimacy and urgency (see Salience model).

### Example
ERP rollout at a manufacturer: CFO and COO (high/high, manage closely: weekly steering), IT security head (high power, low interest: keep satisfied with a compliance brief), plant operators (low power, high interest: keep informed with training and newsletters), peripheral vendors (low/low: monitor, quarterly update).

### In the news
See news box. After CrowdStrike, regulators and boards, once low-interest on third-party software, moved to high power/high interest; the grid should be refreshed whenever the external context shifts.

### Interview angle
> [!question] How it is asked
> "How do you prioritise stakeholders?" or "Draw a power-interest grid for this project and tell me the plan for each quadrant."

> [!tip] Strong answer includes
> - Four quadrants and the action for each
> - Examples from the case, naming individuals
> - Mention that positions change and add attitude (supporter or resistor)
> - Effort allocation: most time on the top-right quadrant, without ignoring the top-left

---

## 9. Stakeholder Engagement Assessment Matrix
> 🔴 Tier 1 · _Tracker hint:_ Current vs desired engagement level; gap strategies

### Definition
The **Stakeholder Engagement Assessment Matrix** compares each stakeholder's **current (C)** engagement level against the **desired (D)** level the project needs. Levels (PMBOK): **Unaware, Resistant, Neutral, Supportive, Leading**.

| Stakeholder | Unaware | Resistant | Neutral | Supportive | Leading |
|---|---|---|---|---|---|
| Sponsor | | | C | D | |
| Union leader | | C | D | | |
| Plant head | | | | C, D | |

A **gap** between C and D requires an action: for each gap, define an engagement action (more communication, involvement in design, addressing concerns, pairing with a champion). If C = D, maintain. It supports the **Plan Stakeholder Engagement** and is updated at each review (Monitor Stakeholder Engagement).

### Example
Rollout of a new WMS. Warehouse supervisors are currently **Resistant** (fear of job loss) and the desired level is **Supportive**: a two-level gap. Actions: involve two supervisors in design, publish a no-layoff reskilling plan, give a floor-level pilot, review after 4 weeks.

### In the news
See news box. In public projects, local resistance is often the factor behind delays; the matrix makes "resistant, desired neutral" explicit and gives it an owner and date.

### Interview angle
> [!question] How it is asked
> "How would you handle a resistant stakeholder?" "What is the difference between a stakeholder register and an engagement assessment matrix?"

> [!tip] Strong answer includes
> - The five levels and the current-vs-desired logic
> - A specific action per gap, with owner and date
> - Listen for the root concern (job loss, workload, ownership)
> - Re-assess regularly

---

## 10. Communications Plan
> 🔴 Tier 1 · _Tracker hint:_ Who gets what info, when, how, from whom

### Definition
The **communications management plan** defines **who** needs **what** information, **when**, in **what format and channel**, **from whom**, with what **frequency** and **feedback** mechanism, and the **escalation path**. It is derived from the stakeholder register and the engagement plan.

Number of communication channels in a group of n people:
$$\text{Channels} = \frac{n(n-1)}{2}$$

Communication types: push (email), pull (portal), interactive (meetings). Models: sender-encode-medium-decode-receiver with noise and feedback. Common outputs: status report, dashboard, steering-committee pack, RAID log extract. Include language and time-zone needs.

### Example
10 people: 10×9/2 = **45 channels**; adding 5 people (15) gives 15×14/2 = **105 channels**, so a 50% increase in staff nearly doubles the paths (+133%). Plan excerpt: Sponsor, weekly, 1-page RAG dashboard, PM; Operators, daily, 10-minute huddle, shift lead; Regulator, monthly, formal letter, PMO.

### In the news
See news box. During outages the winners were firms with a pre-agreed communication tree and a status page, and the losers improvised through email that was itself down. Include an out-of-band channel in the plan.

### Interview angle
> [!question] How it is asked
> "How do you keep a large project stakeholder group informed?" "What would you put in a communications plan?"

> [!tip] Strong answer includes
> - Who, what, when, how, who from; plus feedback and escalation
> - Channel formula and why larger teams need structure
> - Tailor to the audience (executives: one page, RAG)
> - Out-of-band channel and a crisis protocol

---

## 11. ⭐ Advanced: Risk Appetite, Thresholds and Risk Burn-down
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Risk appetite** is the degree of uncertainty an organisation is willing to accept in pursuit of value; **risk tolerance** is the acceptable variation around an objective (for example +/-10% cost); **risk threshold** is the exposure level at which a specific response is triggered (for example any risk with score above 15 is escalated). Appetite differs by stakeholder (a start-up vs a bank) and drives the P-I matrix colours.

**Risk exposure** = sum of the EMVs of open risks. A **risk burn-down chart** plots total exposure (or count of high risks) over time; a healthy project shows exposure falling as responses are implemented and risks retire. Flat or rising exposure at the project's later stages is a warning. Related: **Risk-adjusted contingency drawdown** (reserve used vs reserve remaining against the plan), and **Risk Management Maturity Models**.

### Example
Week 1: top-10 exposure Rs 80 lakh. Week 6: after vendor cross-training and flood mitigation, exposure Rs 35 lakh; contingency Rs 40 lakh is still unused. Reduction = (80 - 35)/80 = 56%. If tolerance is cost +/-10% on Rs 11 crore (Rs 1.1 crore), exposure well inside tolerance.

### In the news
See news box. CrowdStrike pushed boards to restate appetite for third-party dependency; some firms set a threshold such as "no single vendor update may reach all endpoints at once".

### Interview angle
> [!question] How it is asked
> "How do you know whether your project risk is going down?" "What is the difference between risk appetite and risk tolerance?"

> [!tip] Strong answer includes
> - Definitions of appetite, tolerance and threshold, with a numeric example
> - Exposure as the sum of EMVs, tracked over time (burn-down)
> - Escalation when thresholds are breached
> - Link to reserve usage

---

## 12. ⭐ Advanced: Stakeholder Salience Model and RACI
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Salience model** (Mitchell, Agle and Wood, 1997) classes stakeholders by three attributes: **power**, **legitimacy** and **urgency**. One attribute: latent (dormant, discretionary, demanding). Two: expectant (dominant, dangerous, dependent). All three: **definitive**, who gets top priority. It complements the power-interest grid by adding urgency and legitimacy.

**RACI matrix** assigns each task or deliverable one role per person: **R**esponsible (does the work), **A**ccountable (one person who signs off), **C**onsulted (two-way input), **I**nformed (one-way). Rules: exactly one A per row, at least one R, avoid too many Cs. A **RASCI** adds Support. The matrix prevents orphaned tasks and duplicated effort and is part of the resource and communications plans.

### Example
Deliverable "WMS go-live". Project manager: A. IT lead: R. Operations head: C. Finance: I. Warehouse supervisors: C (design) and I (schedule). A union rep who is angry (urgency), has legitimate claim, and the power to strike is **definitive** and moves to the top of the engagement list.

### In the news
See news box. In the infrastructure overrun data, ministries such as Road Transport and Railways own 1,183 of 1,775 projects (993 + 190), so a single accountable owner (RACI "A") per milestone is the lever for accountability.

### Interview angle
> [!question] How it is asked
> "Who is responsible and who is accountable?" "How do you avoid ambiguity in a cross-functional project?"

> [!tip] Strong answer includes
> - RACI definitions and the one-A rule
> - Salience attributes and the idea of a definitive stakeholder
> - Use RACI to resolve ownership disputes early
> - Keep it short and reviewed with the people named

---
## 🔗 Go deeper: expansion notes
- [[169 Project Team Leadership, Conflict & Team Development|Project Team Leadership, Conflict & Team Development]]
- [[170 Programme, Portfolio & PMO Management|Programme, Portfolio & PMO Management]]
