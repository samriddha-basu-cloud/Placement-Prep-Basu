---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Six Sigma & Quality Tools"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 16
---
# Six Sigma & Quality Tools

⬅ [[007 Lean Manufacturing]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[009 Logistics & Distribution]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. DMAIC Framework]]
2. [[#2. DMADV / DFSS]]
3. [[#3. SIPOC Diagram]]
4. [[#4. Fishbone (Ishikawa) Diagram]]
5. [[#5. Pareto Analysis (80/20)]]
6. [[#6. Statistical Process Control (SPC)]]
7. [[#7. Process Capability (Cp/Cpk)]]
8. [[#8. Hypothesis Testing Basics]]
9. [[#9. Regression in Six Sigma]]
10. [[#10. FMEA (Failure Mode Effect Analysis)]]
11. [[#11. Root Cause Analysis (RCA)]]
12. [[#12. Design of Experiments (DOE)]]
13. [[#13. Measurement System Analysis (MSA)]]
14. [[#14. Six Sigma Levels]]
15. [[#15. ⭐ Advanced: Cost of Poor Quality (COPQ)]]
16. [[#16. ⭐ Advanced: Control Chart Rules and Short-term vs Long-term Capability]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): when quality systems fail in public
> **Boeing 737 MAX: a quality lapse caps production (Jan 2024 to Oct 2025).** After a door-sized panel detached from an Alaska Airlines 737 MAX in January 2024, which exposed "production lapses" at the Renton factory, the FAA capped output at **38 aircraft per month**. Boeing reached 38 in May 2025; on **17 Oct 2025** the FAA allowed a rise to **42 per month**. Boeing's Q2 2025 net loss was **$612 million** (vs $1.4 billion a year earlier). ([Spokesman-Review](https://www.spokesman.com/stories/2025/oct/17/after-months-of-limits-faa-allows-boeing-to-increa/))
>
> **Japan's automaker certification scandal (June 2024).** Japan's transport ministry found falsified or improper certification test data (emissions, noise, braking, crash/pedestrian-protection tests) at **Toyota, Mazda, Honda, Suzuki and Yamaha** across a survey of 68 companies. Toyota and Mazda temporarily halted shipments of some models (e.g. Toyota's Yaris Cross); Toyota chairman Akio Toyoda said vehicles were "produced and sold without going through the correct certification process". A failure of measurement and process integrity, not only of manufacturing. ([Drive](https://www.drive.com.au/news/toyota-mazda-honda-suzuki-scandal/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. DMAIC Framework
> 🔴 Tier 1 · _Tracker hint:_ Define→Measure→Analyze→Improve→Control; tollgate reviews

### Definition
**DMAIC** is Six Sigma's structured, data-driven method for improving an **existing** process:

| Phase | Purpose | Typical tools |
|---|---|---|
| **Define** | Problem, scope, customer CTQs, goal, charter | Project charter, SIPOC, VOC, CTQ tree |
| **Measure** | Baseline performance, validate measurement | Data plan, MSA, process map, baseline sigma, Cp/Cpk |
| **Analyze** | Find root causes | Fishbone, Pareto, hypothesis tests, regression, 5 Whys |
| **Improve** | Develop, test and implement solutions | DOE, FMEA, pilot, poka-yoke |
| **Control** | Hold the gains | Control charts, control plan, SOPs, response plan |

**Tollgate reviews** at the end of each phase decide whether to proceed. Roles: Champion, Master Black Belt, **Black Belt**, Green Belt, Yellow Belt. Success metric: **Y = f(X)**, the output (Y) improves by controlling the vital few inputs (Xs). Projects are usually 3–6 months and tied to a financial benefit.

### Example
An accounts-payable team processes 10,000 invoices per month with an 8% error rate, each error costing ₹500 to fix: ₹4 lakh a month. Root cause (Analyze): missing PO numbers. After Improve (mandatory PO field) and Control (weekly p-chart), errors fall to 2%: $10{,}000 \times 2\% \times 500 = ₹1$ lakh. Saving $= ₹3$ lakh a month $= ₹36$ lakh a year.

### In the news
See news box. Boeing's recovery under FAA oversight is a Control-phase problem at scale: the rate increase to 42 was granted only after demonstrating that the improved process held.

### Interview angle
> [!question] How it is asked
> "Walk me through a DMAIC project" or "Where would you use DMAIC vs a quick fix?"

> [!tip] Strong answer includes
> - Five phases with the key output of each and the tollgate logic
> - A concrete example with baseline, root cause, solution, control and rupee benefit
> - Emphasis on data and CTQs, plus Y = f(X)
> - Control phase is where most projects fail, so name the control plan and owner
> - (For HR-style use: structure with STAR; use placeholders for your own project)

---

## 2. DMADV / DFSS
> 🔴 Tier 1 · _Tracker hint:_ Design for Six Sigma; new product/process design

### Definition
**DMADV** is the Six Sigma method for **designing a new product or process** (or when an existing one is so broken that incremental improvement will not do). It is the best-known form of **DFSS (Design for Six Sigma)**.

| Phase | Purpose |
|---|---|
| **Define** | Project goals, customers, market need |
| **Measure** | Identify **CTQs** (critical to quality): VOC, benchmarks, QFD (House of Quality), risk |
| **Analyze** | Develop design alternatives, select the best (Pugh matrix, simulation) |
| **Design** | Detailed design, **FMEA**, tolerance design, DOE, pilot plan |
| **Verify** | Pilot, validate that the design meets CTQs, hand over to the process owner with a control plan |

Variants: **IDOV** (Identify, Design, Optimise, Validate), **DMADOV**. DMAIC vs DMADV: DMAIC improves what exists; DMADV builds what does not exist yet. Designing quality in early is much cheaper than fixing it later (cost of change rises steeply with each stage).

### Example
A bank designs a new digital loan-approval process. VOC says customers want a decision in under 10 minutes (CTQ). Design uses a rules engine and automated KYC; Verify runs a pilot on a sample of live applications. If the measured 95th-percentile decision time is 8.5 minutes and the process capability against USL = 10 min is $C_{pk} \ge 1.33$, the design passes verification.

### In the news
See news box. Japan's certification scandal shows what happens when verification (the "V") is falsified rather than genuinely tested.

### Interview angle
> [!question] How it is asked
> "What is the difference between DMAIC and DMADV?"

> [!tip] Strong answer includes
> - Improve existing vs design new, with the phase list
> - CTQs, QFD and FMEA as design tools
> - Why design-stage quality is cheaper than downstream fixes
> - Example: new product or service launch, with a verification gate

---

## 3. SIPOC Diagram
> 🔴 Tier 1 · _Tracker hint:_ Suppliers-Inputs-Process-Outputs-Customers; process scoping tool

### Definition
**SIPOC** is a one-page, high-level map used in **Define** to scope a process and align the team: **S**uppliers, **I**nputs, **P**rocess (4–7 high-level steps), **O**utputs, **C**ustomers. Build it right-to-left (customers and outputs first) so that the process serves a stated requirement. It sets start and stop points, finds missing stakeholders, and lists CTQ requirements for outputs and inputs.

| S | I | P | O | C |
|---|---|---|---|---|
| Who provides | What they provide | Key steps | What is produced | Who receives it |

Use it before detailed process mapping or VSM, and when team members disagree about what the process is.

### Example
Online food delivery order: **Suppliers**: restaurant, rider fleet, payment gateway; **Inputs**: order, menu data, rider availability; **Process**: Order placed, Restaurant accepts, Food prepared, Rider assigned, Pick-up, Delivery; **Outputs**: delivered meal, invoice, tracking updates; **Customers**: diner, restaurant (payout). Scope decision: the project covers "Rider assigned to Delivery", not menu management.

### In the news
See news box. For the automaker scandal, a SIPOC of "certification testing" would have shown the regulator and test-lab as suppliers/customers of the data, exposing where verification sits.

### Interview angle
> [!question] How it is asked
> "How would you scope a process-improvement project?" or "Draw a SIPOC for order-to-cash."

> [!tip] Strong answer includes
> - Five columns, built from customer back to supplier
> - 4–7 process steps, with clear start/end boundaries
> - Use: scoping, aligning stakeholders, bridging to detailed maps
> - Link to VOC and CTQs

---

## 4. Fishbone (Ishikawa) Diagram
> 🔴 Tier 1 · _Tracker hint:_ 6M causes: Machine, Method, Man, Material, Measurement, Mother Nature

### Definition
The **cause-and-effect (fishbone/Ishikawa) diagram** organises possible causes of a problem (the "head") along major "bones". Manufacturing's **6M**: **Machine, Method, Man (people), Material, Measurement, Mother Nature (environment)**. Services use **8P** (Product, Price, Place, Promotion, People, Process, Physical evidence, Productivity) or 4S.

Steps: state the effect precisely (with data), draw the spine, add categories, brainstorm causes in each (ask "Why does this happen?" repeatedly to add sub-causes), then **prioritise** (vote, Pareto, multi-voting) and **verify with data**. A fishbone lists *possible* causes only: it does not prove them. Combine with 5 Whys and hypothesis tests.

### Example
Effect: "12% of shipments are late". Machine: forklifts breakdown; Method: no dock scheduling; Man: untrained loaders; Material: pallets not available; Measurement: cut-off time not defined; Mother Nature: monsoon flooding. Data check shows 55% of delays occurred at dock without appointments, so Method is investigated first.

### In the news
See news box. Boeing's investigation of the door-panel incident and Japan's certification findings were both root-cause exercises across people, method and measurement categories (analytical reading).

### Interview angle
> [!question] How it is asked
> "Deliveries are late. How do you structure the possible causes?"

> [!tip] Strong answer includes
> - The 6M structure (or 8P for services), applied to the case
> - Move from brainstorm to data: Pareto, stratification, hypothesis tests
> - Distinguish symptoms from root causes
> - Mention 5 Whys and the limit of fishbones (hypotheses only)

---

## 5. Pareto Analysis (80/20)
> 🔴 Tier 1 · _Tracker hint:_ Frequency chart, cumulative%, vital few vs trivial many

### Definition
The **Pareto principle** (Vilfredo Pareto; Juran applied it to quality) states that roughly **80% of effects come from 20% of causes** (the "vital few vs useful many"). The **Pareto chart** is a bar chart of categories in descending order of frequency (or cost) with a cumulative-percentage line.

Steps: define categories, collect data over a fixed period, sort descending, compute percent and **cumulative %**, draw bars and the cumulative line, focus on categories up to about 80%. Use *cost* or *impact*, not just count, when severity differs. 80/20 is a heuristic, not a law. Repeat after fixes (the chart changes). Use before a fishbone to choose where to dig.

### Example
250 defects:

| Defect | Count | % | Cumulative % |
|---|---|---|---|
| Scratches | 120 | 48% | 48% |
| Dents | 60 | 24% | 72% |
| Misalignment | 40 | 16% | 88% |
| Paint | 20 | 8% | 96% |
| Other | 10 | 4% | 100% |

Two categories (Scratches, Dents) give 72% of defects; three give 88%. Attack scratches first: eliminating them removes 48% of defects.

### In the news
See news box. Regulators' findings after quality scandals show a Pareto of failure types (testing, documentation, process), and firms prioritise fixes accordingly.

### Interview angle
> [!question] How it is asked
> "Customer complaints are rising. How would you decide what to fix first?"

> [!tip] Strong answer includes
> - Pareto of complaints by type, weighted by cost or customer impact
> - Cumulative percentage and the vital-few focus
> - Caution: count vs cost, and re-run after improvement
> - Follow with root-cause tools on the top bar

---

## 6. Statistical Process Control (SPC)
> 🔴 Tier 1 · _Tracker hint:_ Control charts (X-bar, R, P, C charts); UCL/LCL; control limits

### Definition
**SPC** (Shewhart) monitors a process over time to separate **common-cause** (inherent, random) from **special-cause** (assignable) variation. **Control limits** are set at $\pm 3\sigma$ of the plotted statistic; they are **not** specification limits.

| Chart | Data | Use |
|---|---|---|
| **X-bar and R** | Variable, subgroups (n 2–10) | Mean and range of a measurement |
| **I-MR** | Variable, individuals | Single measurements |
| **p chart** | Attribute, proportion defective, variable n | Fraction defective |
| **np chart** | Number defective, constant n | |
| **c chart** | Count of defects per unit (constant area) | |
| **u chart** | Defects per unit, variable area | |

Formulas: X-bar limits $= \bar{\bar{X}} \pm A_2 \bar{R}$; R chart $UCL = D_4\bar{R}$, $LCL = D_3 \bar{R}$; p chart $= \bar{p} \pm 3\sqrt{\bar{p}(1-\bar{p})/n}$; c chart $= \bar{c} \pm 3\sqrt{\bar{c}}$ (LCL floored at 0). Constants for $n=5$: $A_2 = 0.577$, $D_3 = 0$, $D_4 = 2.114$. A point outside limits, or non-random patterns (runs, trends), signals special cause.

### Example
X-bar chart, $n = 5$, $\bar{\bar{X}} = 50$, $\bar{R} = 4$: UCL $= 50 + 0.577 \times 4 = 52.31$, LCL $= 47.69$; R chart UCL $= 2.114 \times 4 = 8.46$. p chart: $\bar{p} = 0.04$, $n = 200$: $\sigma = \sqrt{0.04 \times 0.96 / 200} = 0.0139$, UCL $= 0.0816$, LCL $= 0.04 - 0.0416 < 0 \to 0$. c chart: $\bar{c} = 9$: UCL $= 9 + 3 \times 3 = 18$, LCL $= 0$.

### In the news
See news box. Control charts are the early-warning system that makes lapses visible before shipment, when they are cheap to fix.

### Interview angle
> [!question] How it is asked
> "What is a control chart and how is it different from specification limits?" or "Which chart for defects per unit?"

> [!tip] Strong answer includes
> - Common vs special cause and the 3-sigma logic
> - Chart selection by data type
> - Control limits come from the process; spec limits come from the customer
> - What to do when a point is out: stop, investigate, find the assignable cause, do not tamper otherwise

---

## 7. Process Capability (Cp/Cpk)
> 🔴 Tier 1 · _Tracker hint:_ Cp = (USL-LSL)/(6σ); Cpk = min[(USL-μ),(μ-LSL)]/(3σ)

### Definition
**Process capability** compares the process's natural variation to the specification width, assuming a stable (in-control), approximately normal process.

$$C_p = \frac{USL - LSL}{6\sigma} \qquad C_{pk} = \min\left[\frac{USL-\mu}{3\sigma},\ \frac{\mu - LSL}{3\sigma}\right]$$

- $C_p$ ignores centring (potential capability); $C_{pk}$ includes it (actual capability). $C_{pk} \le C_p$, equal when centred.
- Rule of thumb: $C_{pk} \ge 1.33$ acceptable; $\ge 1.67$ for critical characteristics; $< 1$ not capable.
- $Z$ (sigma level) $\approx 3 \times C_{pk}$ for the nearer limit.
- **Pp/Ppk** use overall (long-term) standard deviation; **Cp/Cpk** use within-subgroup (short-term).

### Example
Shaft diameter spec 9.5–10.5 mm, $\mu = 10.1$, $\sigma = 0.1$. $C_p = 1.0 / 0.6 = 1.667$. $C_{pk} = \min(0.4, 0.6) / 0.3 = 1.333$. The mean is off-centre toward the upper limit, which sits $0.4/0.1 = 4\sigma$ away: about 32 ppm above USL (normal tail beyond $z = 4$ is $3.17 \times 10^{-5}$). Re-centring to 10.0 gives $C_{pk} = 1.667$ and ppm $\approx 0.57$ in total.

### In the news
See news box. Capability studies only mean something if the measurement system and test data are honest (see MSA); falsified data defeats the whole exercise.

### Interview angle
> [!question] How it is asked
> "A supplier says Cp = 1.8 but you have rejections. What might be wrong?"

> [!tip] Strong answer includes
> - Cp vs Cpk formulas; Cpk penalises off-centre means (Cp 1.8 with a shifted mean can give a low Cpk)
> - Prerequisites: in-control process, normality, valid MSA
> - Thresholds (1.33, 1.67) and the link to sigma level
> - Actions: centre the process first, then reduce variation

---

## 8. Hypothesis Testing Basics
> 🔴 Tier 1 · _Tracker hint:_ Null/alternate hypothesis; p-value; type I/II error

### Definition
Hypothesis testing uses sample data to judge a claim about a process.
- **$H_0$** (null): no effect/no difference (status quo). **$H_1$** (alternate): there is an effect.
- **Test statistic** (z, t, F, $\chi^2$) and **p-value**: the probability of getting results at least as extreme as observed *if $H_0$ is true*. If $p < \alpha$ (usually 0.05), reject $H_0$.
- **Type I error ($\alpha$)**: reject a true $H_0$ (false alarm, producer's risk). **Type II error ($\beta$)**: fail to reject a false $H_0$ (miss, consumer's risk). **Power** $= 1 - \beta$ (rises with sample size and effect size).

| Data | Test |
|---|---|
| Mean vs target, $\sigma$ known | 1-sample z; unknown: 1-sample t |
| Two means | 2-sample t; paired t |
| 3+ means | One-way ANOVA |
| Variances | F-test, Levene |
| Proportions | z for proportions, chi-square |

Failing to reject $H_0$ is **not** proof it is true. Statistical significance is not practical significance.

### Example
A filling line should deliver 100 g. A sample of $n = 36$ has $\bar{x} = 98.8$ g; assume $\sigma = 3$ g. $z = (98.8 - 100)/(3/\sqrt{36}) = -1.2/0.5 = -2.4$. Two-sided $p = 2 \times 0.0082 = 0.0164 < 0.05$, so reject $H_0$: the mean fill differs from 100 g. Action: investigate the filler's setting.

### In the news
See news box. Regulators effectively run hypothesis tests on firms' compliance data; fabricated samples make every p-value meaningless.

### Interview angle
> [!question] How it is asked
> "What does a p-value of 0.03 mean?" or "How would you test whether the new supplier's parts differ from the old one?"

> [!tip] Strong answer includes
> - $H_0$/$H_1$ stated clearly; p-value interpreted correctly (not "probability $H_0$ is true")
> - Type I vs II errors with business meanings, and power/sample size
> - Choose the test by data type (t, ANOVA, chi-square)
> - Check assumptions (normality, independence), and distinguish statistical from practical significance

---

## 9. Regression in Six Sigma
> 🔴 Tier 1 · _Tracker hint:_ Y=f(X); correlation; residual analysis; DOE link

### Definition
**Regression** quantifies how the output **Y** depends on inputs **X**: the **Y = f(X)** logic of Six Sigma. Simple linear: $Y = \beta_0 + \beta_1 X + \varepsilon$, with least-squares $b_1 = S_{xy}/S_{xx}$, $b_0 = \bar{y} - b_1\bar{x}$.

- **Correlation $r$** ($-1$ to $+1$) measures linear association; $R^2 = r^2$ is the share of variation in Y explained. Correlation is not causation.
- **Multiple regression** handles several Xs; check **multicollinearity** (VIF), use adjusted $R^2$.
- **Residual analysis** validates the model: residuals should be random, roughly normal, constant variance, independent. Patterns (curves, funnel shapes) indicate a wrong model.
- Regression on **observational** data finds associations; **DOE** (designed experiments) establishes causation by controlling Xs.
Use in Analyze (find vital Xs) and Improve (set optimal levels, predict Y).

### Example
Oven temperature (X) vs defects (Y) at points (1,2), (2,4), (3,5), (4,4), (5,5) (X scaled). $\bar{x} = 3$, $\bar{y} = 4$; $S_{xy} = 6$, $S_{xx} = 10$: $b_1 = 0.6$, $b_0 = 4 - 0.6 \times 3 = 2.2$. Prediction at $x = 6$: $2.2 + 3.6 = 5.8$. $SSR = 0.36 \times 10 = 3.6$, $SST = 6$, so $R^2 = 0.6$ (60% explained).

### In the news
See news box. Analytics teams use regression-type models on plant data (Toyota's worker-built ML models are an extension) to predict defects from process variables.

### Interview angle
> [!question] How it is asked
> "How would you find which process variables drive defects?"

> [!tip] Strong answer includes
> - Y = f(X), regression on candidate Xs after screening with Pareto/fishbone
> - $R^2$, p-values of coefficients, residual diagnostics
> - Correlation vs causation, confirm with a DOE or pilot
> - Beware of extrapolation and multicollinearity

---

## 10. FMEA (Failure Mode Effect Analysis)
> 🔴 Tier 1 · _Tracker hint:_ RPN = Severity × Occurrence × Detection; risk prioritization

### Definition
**FMEA** is a proactive method to find how a product (DFMEA) or process (PFMEA) can fail, the effect, the cause, and the controls, then rank the risks and act.

Steps: list process steps, **failure modes**, **effects**, **causes**, current controls; score each on 1–10:
- **Severity (S)**: how bad the effect is.
- **Occurrence (O)**: how often the cause occurs.
- **Detection (D)**: how likely the control is to *miss* it (10 = cannot detect).

$$RPN = S \times O \times D \quad (\text{max } 1000)$$

Prioritise high RPN, but also **any high severity** (S of 9–10) regardless of RPN. Recommended action, owner, then re-score. The 2019 AIAG-VDA handbook replaces RPN with **Action Priority (AP)** tables because RPN can mislead (different S/O/D combinations give the same product).

### Example
Failure mode: a label is applied to the wrong bottle. S = 8, O = 4, D = 5: $RPN = 160$. Add barcode verification (poka-yoke): D falls to 2, so $RPN = 8 \times 4 \times 2 = 64$ (60% lower). Further action to cut O to 2 gives $32$.

### In the news
See news box. Both the Boeing and Japanese certification cases are failures in detection controls: effects were severe, and the controls that should have caught them did not.

### Interview angle
> [!question] How it is asked
> "How do you prioritise risks in a new process launch?" or "Compute the RPN and say what you would do."

> [!tip] Strong answer includes
> - S, O, D scales and the RPN formula
> - Severity-first override and the move to Action Priority
> - Actions that reduce O or D (poka-yoke, control plan), then re-score
> - FMEA as a living document, linked to the control plan

---

## 11. Root Cause Analysis (RCA)
> 🔴 Tier 1 · _Tracker hint:_ 5 Whys, fault tree analysis, current reality tree

### Definition
**RCA** finds the underlying cause so a problem does not recur, instead of treating symptoms.
- **5 Whys**: ask "why?" repeatedly (about five times) until a process or system cause appears. Simple, but results depend on who asks; verify with data.
- **Fault tree analysis (FTA)**: top-down, logic tree (AND/OR gates) from an undesired event to basic causes; can compute event probabilities (AND: multiply; OR: $1 - \prod(1 - p_i)$).
- **Current reality tree (TOC)**: links observed undesirable effects to core causes via cause-effect logic.
- Others: fishbone, Pareto, **8D** (Eight Disciplines) problem solving, **is / is-not** analysis, change analysis.

Good RCA distinguishes **direct cause**, **root cause** and **contributing factors**; fixes the system, not the person; confirms the cause by data or a test and verifies the effect after the fix.

### Example
5 Whys: A machine stopped. (1) Fuse blown; (2) bearing overloaded; (3) bearing lacked lubrication; (4) pump failed to circulate oil; (5) pump shaft worn, no strainer (root cause). Fix: add strainer, lubrication checks. FTA numbers: two independent redundant sensors each fail with $p = 0.05$; both must fail (AND): $0.05^2 = 0.0025$.

### In the news
See news box. Public investigations of the Boeing and Japanese cases look for system causes (culture, oversight, process) beyond the individual error.

### Interview angle
> [!question] How it is asked
> "A customer complaint repeated three times. How do you stop it happening again?"

> [!tip] Strong answer includes
> - 5 Whys with a worked example, and why one chain is not enough (branch if needed)
> - Verify with data, then corrective and preventive action (CAPA)
> - Systemic, not blame-based, causes
> - Follow-up check that the problem is gone

---

## 12. Design of Experiments (DOE)
> 🔴 Tier 1 · _Tracker hint:_ Factorial experiments, interaction effects, Taguchi method

### Definition
**DOE** varies several factors **simultaneously** in a planned way to find their effects on a response with minimum runs, instead of changing one factor at a time (OFAT), which misses **interactions**.

- **Full factorial** $2^k$: $k$ factors at two levels (low/high), $2^k$ runs. Main effect of A $=$ average response at A high $-$ average at A low. Interaction AB = difference in A's effect between levels of B.
- **Fractional factorial**: fewer runs by confounding higher-order interactions (screening).
- Principles: **randomisation, replication, blocking**.
- **Response surface** methods find the optimum; **Taguchi** uses orthogonal arrays and **signal-to-noise ratios** (larger-the-better $-10\log_{10}[\frac{1}{n}\sum 1/y^2]$) to make a process *robust* to noise factors.

### Example
$2^2$ experiment on yield: (A−,B−) = 20; (A+,B−) = 30; (A−,B+) = 25; (A+,B+) = 45.
- Effect A $= \frac{(30+45)-(20+25)}{2} = 15$
- Effect B $= \frac{(25+45)-(20+30)}{2} = 10$
- Interaction AB $= \frac{(20+45)-(30+25)}{2} = 5$
Best setting: both high (45). OFAT would have missed that A's effect is larger when B is high: A's effect is $30-20 = 10$ at B− but $45-25 = 20$ at B+.

### In the news
See news box. Digital twins and simulation let firms run virtual DOEs before physical trials, as in Foxconn's virtual factory validation (see [[006 Manufacturing Systems]]).

### Interview angle
> [!question] How it is asked
> "How would you find the best settings for a process with five variables?"

> [!tip] Strong answer includes
> - Why DOE beats OFAT (efficiency, interactions)
> - Screening fractional factorial, then full factorial or response surface
> - Randomisation, replication; analyse with ANOVA and effect plots
> - Taguchi for robustness; confirm with a verification run

---

## 13. Measurement System Analysis (MSA)
> 🔴 Tier 1 · _Tracker hint:_ Gauge R&R; repeatability vs reproducibility

### Definition
**MSA** checks that the measurement system is good enough before you trust data. Observed variance $= $ process variance $+$ measurement variance.

**Gauge R&R** components:
- **Repeatability (equipment variation, EV)**: same operator, same part, same gauge, repeated.
- **Reproducibility (appraiser variation, AV)**: different operators, same part.
- $\sigma_{GRR} = \sqrt{EV^2 + AV^2}$; $\%GRR = \sigma_{GRR}/\sigma_{total}$ (or vs tolerance).
Acceptance (AIAG): $<10\%$ good; $10$–$30\%$ marginal; $>30\%$ unacceptable. Also **number of distinct categories** ($ndc \ge 5$).

Other aspects: **bias** (accuracy vs reference), **linearity**, **stability** over time, **resolution** (discrimination: at least 1/10 of tolerance). For attribute data: **attribute agreement analysis** (Kappa). Typical study: 10 parts, 3 operators, 2–3 trials, randomised.

### Example
$EV = 0.3$, $AV = 0.4$: $\sigma_{GRR} = \sqrt{0.09 + 0.16} = 0.5$. Part-to-part $\sigma_P = 2.0$: $\sigma_{total} = \sqrt{4 + 0.25} = 2.06$. $\%GRR = 0.5/2.06 = 24.3\%$: marginal; improve (training, fixture, better gauge) before running capability or SPC.

### In the news
See news box. Japan's scandal is a measurement-integrity failure: tests were improperly conducted or recorded, so reported measurements did not reflect the product.

### Interview angle
> [!question] How it is asked
> "Inspectors disagree on defects. How do you fix it?" or "Why do MSA before Cpk?"

> [!tip] Strong answer includes
> - Repeatability vs reproducibility with %GRR thresholds
> - Order: MSA first (Measure phase), then baseline and capability
> - Sources: operator, fixture, gauge resolution, environment; calibrations
> - Attribute data: Kappa, operational definitions and standards

---

## 14. Six Sigma Levels
> 🔴 Tier 1 · _Tracker hint:_ DPMO, sigma level table; 3.4 DPMO at 6σ

### Definition
**Sigma level** expresses process capability as how many standard deviations fit between the mean and the nearest spec limit. Defect metrics:

$$DPU = \frac{\text{defects}}{\text{units}} \quad DPO = \frac{\text{defects}}{\text{units} \times \text{opportunities}} \quad DPMO = DPO \times 10^6$$

By convention the table includes a **1.5σ long-term shift** of the mean:

| Sigma level | DPMO | Yield |
|---|---|---|
| 2 | 308,538 | 69.1% |
| 3 | 66,807 | 93.3% |
| 4 | 6,210 | 99.38% |
| 5 | 233 | 99.977% |
| 6 | **3.4** | 99.99966% |

Without the shift, six sigma would be about 0.002 DPMO; the 1.5σ shift is empirical (Motorola) and debated. **Rolled throughput yield** $= \prod$ step yields: 10 steps at 99% gives $0.99^{10} = 90.4\%$, so high step quality is needed for complex processes.

### Example
500 invoices, 5 opportunities for error each, 60 defects found: $DPMO = 60/(500 \times 5) \times 10^6 = 24{,}000$, i.e. about 3.5σ (22,750 DPMO is 3.5σ). To reach 4σ (6,210 DPMO) defects would need to fall to about 16 for the same volume ($6{,}210 \times 2{,}500 / 10^6 \approx 15.5$).

### In the news
See news box. Aerospace and auto lines need very high sigma levels: Boeing's rate cap is a regulator's way of limiting output until the process proves it can hold quality at volume.

### Interview angle
> [!question] How it is asked
> "What does six sigma mean? Calculate DPMO for this data." or "Is Six Sigma relevant now that firms use agile and AI?"

> [!tip] Strong answer includes
> - Sigma level table, DPMO formula and the 1.5σ shift caveat
> - Opportunities defined carefully (they can be gamed)
> - RTY across steps (multiplicative)
> - Balanced view: Lean Six Sigma, data-based, still relevant with analytics

---

## 15. ⭐ Advanced: Cost of Poor Quality (COPQ)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**COPQ** (cost of quality, Juran/Feigenbaum) is the money lost because processes are not right the first time. Categories (PAF model):
- **Prevention**: training, design reviews, poka-yoke, FMEA, planning.
- **Appraisal**: inspection, testing, audits, calibration.
- **Internal failure**: scrap, rework, re-inspection, downtime (found before delivery).
- **External failure**: warranty, returns, recalls, complaints, lost customers, litigation (found after delivery).

Classic insight: spending more on prevention lowers total cost: failure costs rise steeply with each stage the defect passes (the **1-10-100 rule** is a rule of thumb: ₹1 to prevent, ₹10 to fix in-house, ₹100 after reaching the customer). Many firms lose **10–30% of sales** to COPQ (a widely quoted range); the "iceberg": visible failures (scrap, warranty) are small relative to hidden ones (lost time, expediting, lost sales). COPQ is used to **select and justify Six Sigma projects**.

### Example
Sales ₹500 crore. Prevention ₹3 crore, appraisal ₹7 crore, internal failure ₹30 crore, external failure ₹25 crore: COPQ $= 65$ crore $= 13\%$ of sales. Spending an extra ₹5 crore on prevention that cuts failure costs by 30% ($0.3 \times 55 = ₹16.5$ crore) nets $+₹11.5$ crore a year.

### In the news
See news box. Boeing's Q2 2025 loss of $612 million and Toyota's temporary shipment halts show external-failure costs (regulatory, reputational, lost output) dwarf prevention budgets.

### Interview angle
> [!question] How it is asked
> "How would you build a business case for a quality improvement programme?"

> [!tip] Strong answer includes
> - PAF categories and visible vs hidden costs
> - Quantify current COPQ, then the saving from fixing the top Pareto items
> - Prevention-first logic with the 1-10-100 intuition
> - Present as ROI and payback, with a pilot

---

## 16. ⭐ Advanced: Control Chart Rules and Short-term vs Long-term Capability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A single point beyond $3\sigma$ is not the only out-of-control signal. **Western Electric / Nelson rules** (zones A, B, C = 3, 2, 1 sigma from the centre line) flag:
1. One point beyond 3σ.
2. Two of three consecutive points beyond 2σ (same side).
3. Four of five consecutive points beyond 1σ (same side).
4. Eight (or nine) consecutive points on one side of the centre line.
5. Six points in a row steadily rising or falling (trend).
6. Fourteen points alternating up and down (overcontrol/two streams).
Too many rules raise the **false alarm rate**: with 3σ limits alone the in-control false alarm probability per point is about 0.27% (average run length ~370); extra rules shorten it.

**Short-term vs long-term:** $C_p/C_{pk}$ use within-subgroup $\sigma$ (potential), $P_p/P_{pk}$ use overall $\sigma$ (what the customer experiences). A big gap ($C_{pk} \gg P_{pk}$) means the mean drifts between subgroups: a centring/stability problem, not a spread problem.

### Example
Eight consecutive points above the centre line on an X-bar chart, none beyond limits: rule 4 signals a shift (probability of 8 in a row on one side by chance $= 0.5^8 \approx 0.4\%$). Investigate a tool-wear or material-lot change. Capability: $C_{pk} = 1.5$ but $P_{pk} = 0.9$ means between-subgroup drift dominates, so fix stability before reducing common-cause variation.

### In the news
See news box. Early-warning rules matter most when a process is run near its limit, as when a factory ramps up toward a higher production rate under scrutiny.

### Interview angle
> [!question] How it is asked
> "All points are inside the limits. Is the process in control?"

> [!tip] Strong answer includes
> - Run rules and trends, not only points outside limits
> - Trade-off between sensitivity and false alarms
> - Cp/Cpk vs Pp/Ppk and what the gap tells you
> - Action: investigate the special cause, don't adjust when only common cause is present

---
## 🔗 Go deeper: expansion notes
- [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)|Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]
- [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)|Acceptance Sampling & Measurement System Analysis (Gauge R&R)]]
- [[213 Design of Experiments - Factorial, Fractional & Taguchi|Design of Experiments - Factorial, Fractional & Taguchi]]
