---
tags: [project-management, tier2]
area: Project Management
topic: "Cost & Budget Management"
tier: Tier 2
roles: Project Mgmt
status: complete
subtopics: 7
---
# Cost & Budget Management

⬅ [[041 Agile Project Management]] · [[_Index - Project Management|Project Management]] · [[168 Project Procurement, Contracts & EPC Delivery]] ➡
> **Area:** Project Management · **Priority:** 🟠 Tier 2 · **Target roles:** Project Mgmt

## Sub-topics in this note
1. [[#1. Cost Estimation Methods]]
2. [[#2. Cost Baseline]]
3. [[#3. Earned Value Management (EVM)]]
4. [[#4. Budget at Completion (BAC)]]
5. [[#5. CPI & SPI Interpretation]]
6. [[#6. Forecasting EAC]]
7. [[#7. ⭐ Advanced: Earned Schedule, Cost Escalation and Reserve Analysis]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's central projects and the cost of overruns
> **MoSPI infrastructure report (July 2026 data, published 27 Aug 2026).** Of **1,775 central sector projects costing Rs 150 crore or more**, the cumulative cost overrun was **Rs 3,40,504 crore**: original cost **Rs 33,70,138 crore** vs revised cost **Rs 37,10,642 crore** (about +10.1%). Cumulative expenditure was Rs 19.26 lakh crore, or **51.91% of revised cost**. Road Transport and Highways (993 projects, Rs 9.62 lakh crore), Railways (190) and Coal (121) lead by count. The source report did not say how many individual projects overran. ([Swarajya](https://swarajyamag.com/news-brief/indias-1775-central-infrastructure-projects-face-rs-34-lakh-crore-cost-overrun))
>
> **Business acumen and budget adherence (PMI Pulse of the Profession 2025).** Budget adherence was **73% for high-business-acumen project professionals vs 68% for others**, and failure rates 8% vs 11%. ([PMI](https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/pulse_of_the_profession_2025-1.pdf))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Cost Estimation Methods
> 🟠 Tier 2 · _Tracker hint:_ Analogous, parametric, bottom-up, three-point

### Definition
Estimating predicts the cost of resources for each activity. Accuracy improves as the project definition improves (rough order of magnitude -25% to +75% early, definitive -5% to +10% late).

| Method | How | Accuracy / use |
|---|---|---|
| **Analogous (top-down)** | Scale the actual cost of a similar past project | Fast, rough, early stage |
| **Parametric** | Unit cost × quantity from a statistical relationship (Rs/sq m, Rs/km, hours/line of code) | Good when history is reliable and scalable |
| **Bottom-up** | Estimate each work package and roll up | Most accurate, most effort |
| **Three-point (PERT)** | $E = \frac{O + 4M + P}{6}$, $\sigma = \frac{P - O}{6}$ | Reflects uncertainty |
| Triangular | $E = \frac{O + M + P}{3}$ | Simpler |
| Others | Expert judgment, vendor bid analysis, reserve analysis, cost of quality, group decision techniques | |

Estimates should state assumptions, basis, range and confidence; add contingency separately.

### Example
Parametric: a 4,000 sq m warehouse at Rs 30,000 per sq m = 4,000 × 30,000 = Rs 12 crore. Three-point for racking install: O = 10, M = 14, P = 24 (Rs lakh): PERT = (10 + 4×14 + 24)/6 = 90/6 = **Rs 15 lakh**; $\sigma$ = (24 - 10)/6 = 2.33 lakh; so about 68% range is 12.7 to 17.3 lakh. Triangular would give (10+14+24)/3 = 16 lakh.

### In the news
See news box. Overruns of about 10% on Rs 33.7 lakh crore of projects suggest early analogous estimates are routinely optimistic; use bottom-up and reference-class data as the project matures.

### Interview angle
> [!question] How it is asked
> "How would you estimate the cost of a new plant?" "What is the difference between analogous and parametric estimating?"

> [!tip] Strong answer includes
> - Match the method to project stage and data available
> - PERT formula with a worked number
> - State assumptions, range and confidence; keep reserve separate
> - Cross-check top-down against bottom-up

---

## 2. Cost Baseline
> 🟠 Tier 2 · _Tracker hint:_ Time-phased budget; S-curve; performance measurement baseline

### Definition
The **cost baseline** is the approved, **time-phased** budget used to measure, monitor and control cost performance. It is the **performance measurement baseline (PMB)** for earned value (together with scope and schedule baselines). It is built by aggregating activity estimates into work packages and control accounts, adding **contingency reserves**, and spreading them across time. Plotted cumulatively it forms an **S-curve** (slow start, steep middle, flat finish).

$$\text{Cost baseline} = \text{Work package estimates} + \text{Contingency reserves}$$
$$\text{Project budget} = \text{Cost baseline} + \text{Management reserve}$$

Management reserve is outside the baseline. Any change to the baseline needs formal change control. **Funding limit reconciliation** ensures planned spend matches funding availability.

### Example
Budget Rs 12 crore over 6 months. Monthly plan (Rs crore): 1.0, 2.0, 3.0, 3.0, 2.0, 1.0. Cumulative PV: 1.0, 3.0, 6.0, 9.0, 11.0, 12.0 (the S-curve). At end of month 3 the PV is Rs 6 crore; this is the benchmark against which EV and AC are compared.

### In the news
See news box. Revised cost of Rs 37.1 lakh crore versus original Rs 33.7 lakh crore means baselines are being re-set; each rebaseline hides the true overrun against the original, so track both.

### Interview angle
> [!question] How it is asked
> "What is a cost baseline and how is it different from a budget?"

> [!tip] Strong answer includes
> - Time-phased, approved, includes contingency, excludes management reserve
> - Drawing the S-curve and what PV means on it
> - Baseline changes only through change control
> - Keep original baseline for reporting overrun

---

## 3. Earned Value Management (EVM)
> 🟠 Tier 2 · _Tracker hint:_ PV, EV, AC; CPI=EV/AC; SPI=EV/PV; VAC, EAC, ETC

### Definition
EVM integrates scope, schedule and cost.
- **PV (Planned Value)** = budgeted cost of work scheduled.
- **EV (Earned Value)** = budgeted cost of work performed = % complete × BAC.
- **AC (Actual Cost)** = actual cost of work performed.

| Metric | Formula | Read |
|---|---|---|
| Cost variance | $CV = EV - AC$ | negative = over budget |
| Schedule variance | $SV = EV - PV$ | negative = behind |
| CPI | $EV / AC$ | below 1 = over budget |
| SPI | $EV / PV$ | below 1 = behind |
| EAC | $BAC / CPI$ | forecast total |
| ETC | $EAC - AC$ | remaining spend |
| VAC | $BAC - EAC$ | final variance |
| TCPI | $\frac{BAC - EV}{BAC - AC}$ | efficiency needed |

Remember: **EV is the anchor**; variances are EV minus something.

### Example
BAC Rs 1,000 lakh. At month 5: planned 50% complete, actual 40% complete, spent 450. PV = 500, EV = 0.40 × 1,000 = 400, AC = 450.
CV = 400 - 450 = **-50**; SV = 400 - 500 = **-100**; CPI = 400/450 = **0.889**; SPI = 400/500 = **0.80**.
EAC = 1,000/0.889 = **1,125**; ETC = 1,125 - 450 = **675**; VAC = 1,000 - 1,125 = **-125**.

### In the news
See news box. Public-sector overrun reporting is the macro version of CV: revised cost minus original cost = Rs 3.4 lakh crore.

### Interview angle
> [!question] How it is asked
> "A project is 40% complete, you've spent 45% of the budget. What does it tell you?" Often with numbers to compute on the spot.

> [!tip] Strong answer includes
> - Definitions PV, EV, AC and all formulas correctly
> - Calculation done aloud and the interpretation in words
> - Next step: root cause, corrective action, forecast and revised baseline if needed
> - Limits: EV depends on honest % complete (use 0/100 or 50/50 rules for work packages)

---

## 4. Budget at Completion (BAC)
> 🟠 Tier 2 · _Tracker hint:_ Original approved budget; vs EAC (forecast at completion)

### Definition
**BAC** is the sum of all budgets established for the work to be performed, i.e. the total planned value at the end of the project. It equals the cost baseline (excluding management reserve). It is **fixed** unless a formal change is approved, so it is the yardstick.

**EAC (Estimate at Completion)** is the expected total cost given performance to date; it changes with each status period. 

$$VAC = BAC - EAC$$

Positive VAC = under budget; negative = overrun. **Budget** is what you plan, **EAC** is what you now expect, and **AC** is what you have spent. A typical error: updating BAC to match EAC to "get green" again; this hides the overrun. BAC changes only with scope changes or approved rebaseline.

### Example
BAC = Rs 8 crore. At 50% earned (EV = 4 crore) with AC = 4.4 crore: CPI = 4/4.4 = 0.909; EAC = 8/0.909 = Rs 8.8 crore; VAC = 8 - 8.8 = -0.8 crore. BAC stays at 8; the sponsor must decide whether to fund the 0.8 crore, cut scope, or tap management reserve.

### In the news
See news box. In the MoSPI data, original cost (BAC analogue) Rs 33.70 lakh crore vs revised Rs 37.11 lakh crore (EAC analogue); the Rs 3.4 lakh crore gap is the aggregate negative VAC.

### Interview angle
> [!question] How it is asked
> "What is BAC and how is it different from EAC?"

> [!tip] Strong answer includes
> - BAC fixed and approved; EAC is a forecast
> - VAC = BAC - EAC with sign interpretation
> - Never quietly rebaseline BAC
> - Who approves changes (sponsor, CCB)

---

## 5. CPI & SPI Interpretation
> 🟠 Tier 2 · _Tracker hint:_ CPI<1 = over budget; SPI<1 = behind schedule; trend analysis

### Definition
- **CPI > 1:** under budget (each rupee spent earns more than a rupee of planned work); **CPI = 1:** on budget; **CPI < 1:** over budget.
- **SPI > 1:** ahead; **= 1:** on plan; **< 1:** behind. SPI approaches 1 at project end by mathematics (EV converges on PV), so late SPI is weak; use **earned schedule** (ES) or critical path analysis.

| CPI | SPI | Reading |
|---|---|---|
| < 1 | < 1 | Over budget and late: serious |
| < 1 | > 1 | Ahead but expensive (overtime/crashing) |
| > 1 | < 1 | Cheap but late (under-resourced) |
| > 1 | > 1 | Good, check quality and scope |

**Trend analysis:** plot CPI and SPI over periods; a **cumulative CPI** stabilises after about 20% completion and rarely improves by more than about 10% afterwards (an often-cited rule of thumb from US defence studies; treat as indicative). Use thresholds, for example green 0.95 to 1.05, amber 0.90 to 0.95, red below 0.90.

### Example
Month-by-month CPI: 0.97, 0.93, 0.90, 0.88 with SPI 1.0, 0.95, 0.90, 0.85. Falling trend: the project is deteriorating on both axes; do not wait until CPI is 0.80. Action: root cause (rework? vendor rate?), re-forecast EAC and ask for corrective action plan.

### In the news
See news box. A 10% aggregate overrun equals a portfolio CPI of about 0.91 (33.70/37.11, assuming overrun is the only variance and measured at completion cost); good for a sense of scale.

### Interview angle
> [!question] How it is asked
> "CPI is 0.85 and SPI is 1.1. Explain."

> [!tip] Strong answer includes
> - Plain-language reading, both indices together
> - Trend, not a snapshot
> - A cause hypothesis (overtime, crashing, price escalation) and checks
> - Caveat: SPI becomes meaningless near the end; use earned schedule

---

## 6. Forecasting EAC
> 🟠 Tier 2 · _Tracker hint:_ EAC = BAC/CPI (typical); EAC = AC + ETC (re-estimate)

### Definition
Choose the formula by what you believe about the future:

| Situation | Formula |
|---|---|
| Past performance **will continue** (typical variance) | $EAC = BAC / CPI$ |
| Past variance was **one-off** (atypical) | $EAC = AC + (BAC - EV)$ |
| Both cost and schedule performance affect the remaining work | $EAC = AC + \frac{BAC - EV}{CPI \times SPI}$ |
| Original estimate was fundamentally flawed | $EAC = AC + \text{Bottom-up ETC}$ |

$$ETC = EAC - AC \quad (\text{or the re-estimate})$$
$$TCPI_{BAC} = \frac{BAC - EV}{BAC - AC}, \quad TCPI_{EAC} = \frac{BAC - EV}{EAC - AC}$$

TCPI above 1 means future work must be done more efficiently than so far; above about 1.1 the target is generally unrealistic.

### Example
BAC 1,000, EV 400, AC 450, CPI 0.889, SPI 0.80.
- Typical: 1,000/0.889 = **1,125**
- Atypical: 450 + (1,000 - 400) = **1,050**
- CPI×SPI: 450 + 600/(0.889×0.80) = 450 + 600/0.711 = **1,294**
- TCPI to hit BAC = 600/550 = **1.09** (need 9% better efficiency than the plan from now on).

### In the news
See news box. Public projects with revised cost 10% above original and only 51.91% of the revised cost spent imply further EAC risk as more work remains to be executed.

### Interview angle
> [!question] How it is asked
> "How do you forecast the final cost of a project?" "When would you use AC + (BAC - EV)?"

> [!tip] Strong answer includes
> - Three or four formulas and when each applies
> - Compute a range (best, typical, worst) not a single number
> - TCPI as reality check on the sponsor's target
> - Bottom-up re-estimate when the baseline is unreliable

---

## 7. ⭐ Advanced: Earned Schedule, Cost Escalation and Reserve Analysis
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Earned Schedule (ES)** fixes SPI's late-project distortion: ES is the time at which the current EV *should* have been earned on the baseline. $SV(t) = ES - AT$ (actual time) and $SPI(t) = ES / AT$. It stays meaningful up to completion and gives a time forecast: $IEAC(t) = PD / SPI(t)$ (PD = planned duration).

**Cost escalation** (inflation, steel and fuel price rises) is modelled in the estimate: $C_t = C_0 (1 + e)^t$. **Cost of delay**: each month late costs overheads + financing + lost revenue. **Reserve analysis** compares remaining contingency with remaining risk EMV (see [[040 Risk & Stakeholder Management]]); if reserve falls below remaining exposure, escalate.

Also: **Cost of quality** (prevention + appraisal vs failure) and **life-cycle costing** (capex + operating + disposal), key in operations investments.

### Example
Planned duration 10 months, EV at month 6 equals the PV planned for month 4.5. ES = 4.5, AT = 6, so SPI(t) = 4.5/6 = 0.75, forecast = 10/0.75 = 13.3 months. Escalation: Rs 100 crore steel-heavy cost at 6% for 2 years = 100 × 1.06² = Rs 112.36 crore.

### In the news
See news box. The source did not break the Rs 3.4 lakh crore overrun into causes (I did not verify any); in interviews, say you would split it into escalation, delay and scope change, and track an escalation clause explicitly.

### Interview angle
> [!question] How it is asked
> "A project is 90% through its schedule and SPI shows 0.98 but the team says it'll be late. What's going on?"

> [!tip] Strong answer includes
> - SPI is cost-based so converges to 1; use earned schedule or critical path
> - Time forecast formula
> - Include escalation and cost of delay in forecast
> - Reserve vs remaining exposure

---
## 🔗 Go deeper: expansion notes
- [[225 Budgeting, Variance Analysis & Balanced Scorecard|Budgeting, Variance Analysis & Balanced Scorecard]]
- [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement|Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]
