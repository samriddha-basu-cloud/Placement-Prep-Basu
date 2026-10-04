---
tags: [operations-management, tier2]
area: Operations Management
topic: "Reliability Engineering & Maintenance Optimisation"
tier: Tier 2
roles: Operations
status: complete
subtopics: 14
---
# Reliability Engineering & Maintenance Optimisation

⬅ [[154 Product & Service Design - QFD, DFMA & Value Engineering]] · [[_Index - Operations Management|Operations Management]] · [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]] ➡

> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Reliability Function, Hazard Rate and Failure Metrics]]
2. [[#2. Exponential Model and the Bathtub Curve]]
3. [[#3. Weibull Distribution and Parameter Interpretation]]
4. [[#4. Series Systems and Reliability Block Diagrams]]
5. [[#5. Parallel, k-out-of-n and Standby Redundancy]]
6. [[#6. Availability: Inherent, Achieved and Operational]]
7. [[#7. FMEA and FMECA]]
8. [[#8. Fault Tree Analysis and Cut Sets]]
9. [[#9. Age vs Block Replacement and the Optimal PM Interval]]
10. [[#10. Spare Parts Provisioning with the Poisson Model]]
11. [[#11. Condition Monitoring and the P-F Interval]]
12. [[#12. Warranty Cost Models]]
13. [[#13. RCM Decision Logic and the Failure Patterns]]
14. [[#14. ⭐ Advanced: Hidden Failures, Failure-Finding Intervals and Common-Cause Failure]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the price of unreliability, and a failure of the maintenance system itself
> **Siemens "True Cost of Downtime 2024" (Senseye report).** The survey puts unplanned downtime at about **$1.4 trillion a year for the Fortune Global 500, equal to 11% of revenues**, a fall of 6% since 2022. Automotive plants lose about **$2.3 million per hour** (roughly double the 2019 level), against about **$36,000 per hour in FMCG**. Plants average **25 unplanned incidents and 27 lost hours a month** (down from 42 and 39 in 2019), yet the average recovery takes **81 minutes** (up from 49). Almost half of firms now run predictive-maintenance teams, twice the 2019 share, and nine in ten do some condition monitoring. The figures are survey-based estimates, not audited costs. ([Siemens / Senseye report PDF](https://assets.new.siemens.com/siemens/assets/api/uuid:1b43afb5-2d07-47f7-9eb7-893fe7d0bc59/tcod-2024_original.pdf))
>
> **Alaska Airlines 737-9 door-plug blowout, NTSB findings (report released 10 Jul 2025).** On 5 Jan 2024 a door plug left the aircraft in flight. The NTSB found four critical bolts were missing: employees had opened the plug during rework at Boeing's Renton plant with no removal record, closed it without securing the hardware, and no quality-assurance inspection caught it. It also found Boeing had not fully implemented the safety management system it began in 2016. ([Manufacturing Dive](https://www.manufacturingdive.com/news/boeing-faa-inadequate-training-oversight-737-max-doorplug-blowout-ntsb/752872/)) In Sept 2025 the FAA proposed **$3.1 million** in civil penalties for hundreds of quality-system violations at Boeing's and Spirit AeroSystems' 737 factories between Sept 2023 and Feb 2024 ([NPR](https://www.npr.org/2025/09/13/nx-s1-5540728/boeing-faa-safety-fines-door-plug-blowout)). A textbook case of a *detection* control that did not exist.
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Reliability Function, Hazard Rate and Failure Metrics
> 🟠 Tier 2 · _Key points:_ R(t), F(t), f(t), h(t), MTTF; conditional reliability

### Definition
Let $T$ be the (random) time to failure of an item.

- **Unreliability** $F(t)=P(T\le t)$ and **reliability** $R(t)=P(T>t)=1-F(t)$.
- **Density** $f(t)=dF/dt$.
- **Hazard (failure) rate** $h(t)$: the instantaneous failure rate of items that have survived to $t$.

$$h(t)=\frac{f(t)}{R(t)},\qquad R(t)=\exp\!\left(-\int_0^t h(u)\,du\right),\qquad MTTF=\int_0^\infty R(t)\,dt$$

The **conditional reliability** of an item that has already survived to age $t_0$ for a further mission $x$ is $R(x\mid t_0)=R(t_0+x)/R(t_0)$. This is the quantity a maintenance planner needs ("it has run 600 h, will it last another 200 h?"). **MTTF** is for non-repairable items; **MTBF** (see [[022 Maintenance Management (TPM-RCM)|maintenance management]]) is for repairable ones. Hazard rate is a *rate* (per hour), not a probability, and can exceed 1 per unit time. Distinguish it from the failure *density*, which is unconditional.

The **B-life** notation: $B_{10}$ is the age by which 10% of units have failed (bearing makers quote $L_{10}$ life this way). Median life is $B_{50}$.

### Example
A fleet of 200 new motors is observed. After 1,000 h, 20 have failed, so empirical $\hat F(1000)=0.10$, $\hat R(1000)=0.90$. In the next 100 h, 6 of the remaining 180 fail: the empirical hazard over that interval is $6/(180\times100)=3.3\times10^{-4}$ per hour (one failure per 3,000 unit-hours), whereas the unconditional density is $6/(200\times100)=3\times10^{-4}$. The two differ because the hazard divides by survivors, not by the original population.

### In the news
See news box. Siemens' "27 lost hours per plant per month" is an aggregate of exactly these failure and repair times; reliability maths turns that average into a distribution that can be planned for.

### Interview angle
> [!question] How it is asked
> "What is the difference between reliability, hazard rate and MTBF? Does a high MTBF mean the item rarely fails in early life?"

> [!tip] Strong answer includes
> - $R(t)$ as a survival probability, $h(t)=f/R$ as a rate conditional on survival
> - MTBF is a mean, not a guaranteed life: with exponential life only **36.8%** of items survive to MTBF
> - Conditional reliability for items already in service
> - Link to survival analysis ([[211 Reliability & Survival Analysis]]) and distributions ([[088 Probability Distributions]])

---
## 2. Exponential Model and the Bathtub Curve
> 🟠 Tier 2 · _Key points:_ constant hazard; memoryless; bathtub; limits

### Definition
With a **constant hazard** $\lambda$ the life is exponential:

$$R(t)=e^{-\lambda t},\qquad MTTF=\frac1\lambda,\qquad R(\text{MTTF})=e^{-1}\approx0.368$$

It is **memoryless**: $R(x\mid t_0)=R(x)$, so an old item is as good as new. That is realistic for electronic parts, shock/overload events and externally caused failures, and unrealistic for wear-out. Preventive replacement of an exponential item gives **no** reliability benefit (and adds infant-mortality risk from the intervention).

The **bathtub curve** has three zones: *infant mortality* (decreasing hazard: defects, installation errors, commissioning), *useful life* (roughly constant hazard) and *wear-out* (increasing hazard: fatigue, corrosion, abrasion). Burn-in screening attacks the first zone; age-based replacement attacks the third. Nowlan and Heap's airline study found that the bathtub is rare: for United Airlines items, only about **4%** followed the classic bathtub (pattern A) and **2%** pure wear-out (pattern B), while patterns with no wear-out zone (D, E, F) covered about **89%**, with 68% showing infant mortality then random failures. These percentages come from aircraft data and are not an industry norm, so test your own plant's history.

### Example
A VFD controller has MTBF 2,000 h ($\lambda=0.0005$/h).
- $R(500)=e^{-0.25}=\mathbf{0.779}$; $R(2000)=0.368$.
- Time for 90% reliability: $t=-\ln(0.9)\times2000=\mathbf{210.7\ h}$.
- Having already run 1,000 h, the chance of surviving another 500 h is still 0.779 (memoryless).

### In the news
See news box. Siemens reports 25 incidents a month per plant; a stable monthly count across hundreds of independent assets behaves like a constant-hazard (Poisson) process at plant level even when each machine wears out.

### Interview angle
> [!question] How it is asked
> "Your PM team replaces a PLC card every 12 months, yet failures continue. Why?"

> [!tip] Strong answer includes
> - Constant hazard means age-based replacement cannot help; failures are random or infant-mortality
> - Check maintenance-induced failures (re-installation after PM)
> - Use condition monitoring, redundancy or spares instead of calendar replacement
> - Cite the six failure patterns and say they must be verified with plant data

---
## 3. Weibull Distribution and Parameter Interpretation
> 🟠 Tier 2 · _Key points:_ shape β, scale η, B10, MTTF with Gamma; 63.2%

### Definition
$$R(t)=\exp\!\left[-\left(\frac t\eta\right)^{\beta}\right],\qquad h(t)=\frac\beta\eta\left(\frac t\eta\right)^{\beta-1},\qquad MTTF=\eta\,\Gamma\!\left(1+\frac1\beta\right)$$

- **Shape $\beta$:** $\beta<1$ decreasing hazard (infant mortality); $\beta=1$ constant (exponential, with $\eta$ = MTTF); $\beta>1$ increasing hazard (wear-out; $\beta\approx2$ to 4 for fatigue/bearings/corrosion, higher for brittle, tightly-clustered lives). Roughly $\beta\approx3.5$ gives a near-symmetric life.
- **Scale (characteristic life) $\eta$:** the age by which **63.2%** have failed whatever $\beta$ is, since $R(\eta)=e^{-1}$.
- Percentile life: $t_p=\eta[-\ln(1-p)]^{1/\beta}$, so $B_{10}=\eta(0.1054)^{1/\beta}$.
- A third parameter $\gamma$ (failure-free location) is sometimes added.

Fitting: plot $\ln\ln\frac{1}{1-F}$ against $\ln t$ (Weibull probability paper); the slope is $\beta$. Software: Excel `WEIBULL.DIST`, Python `reliability`/`lifelines`/`scipy.stats.weibull_min`; handle **censored** data (units still running) with maximum likelihood, not by dropping them ([[211 Reliability & Survival Analysis]]).

### Example
Pump seals follow Weibull $\beta=2.5$, $\eta=1{,}000$ h (computed in Python).

| Quantity | Value |
|---|---|
| $R(600)$ | $\exp[-(0.6)^{2.5}]=0.757$ |
| $h(600)$ | $0.00116$ per hour |
| MTTF | $1000\,\Gamma(1.4)=1000\times0.8873=887.3$ h |
| Median ($B_{50}$) | 863.6 h |
| $B_{10}$ | 406.5 h |
| $R(800\mid600)$ | $R(800)/R(600)=0.5642/0.7566=0.746$ |

Here $R(800)=\exp[-(0.8)^{2.5}]=\exp(-0.5724)=0.5642$: a seal that has already survived 600 h has a 74.6% chance of surviving another 200 h, lower than a new seal's $R(200)=0.982$ because wear has accumulated.

Reading: with $\beta=2.5$ failures cluster around 700 to 1,100 h and a calendar interval near $B_{10}$ (about 400 h) is worth testing in the age-replacement model of sub-topic 9. If $\beta$ were 1.0, the same data would argue *against* planned replacement.

### In the news
See news box. Automotive's $2.3 million per hour downtime cost explains why bearing and drive makers publish $B_{10}$/$L_{10}$ lives and why OEMs demand Weibull plots from suppliers.

### Interview angle
> [!question] How it is asked
> "A supplier's gearbox has Weibull shape 0.8. Would you replace it on a schedule?"

> [!tip] Strong answer includes
> - $\beta<1$ means hazard falls with age: scheduled replacement makes things worse; fix quality, installation and run-in
> - $\eta$ as 63.2% life; B10 as a conservative planning life
> - Need enough failures and correct treatment of censored data
> - Pair with cost: the replacement interval depends on $C_f/C_p$ (sub-topic 9)

---
## 4. Series Systems and Reliability Block Diagrams
> 🟠 Tier 2 · _Key points:_ product rule; weakest link; many components erode reliability

### Definition
In a **series** system every component must work. With independent components:

$$R_s(t)=\prod_{i=1}^{n}R_i(t),\qquad \lambda_s=\sum_i\lambda_i\ \text{(exponential)},\qquad MTTF_s=\frac1{\sum\lambda_i}$$

$R_s\le\min R_i$: the system is never better than its weakest link, and reliability decays quickly as parts are added. A **reliability block diagram (RBD)** shows how functional success flows through blocks (series = one path, parallel = alternatives); more complex networks use path or cut-set methods. A production line with no buffers is a series system, which links to the throughput logic of [[018 Capacity Management & OEE|capacity and OEE]] and the line-balance ideas of [[006 Manufacturing Systems]].

### Example
A filling line has four machines with reliabilities (over a shift) of 0.98, 0.95, 0.99, 0.97.
$R_s=0.98\times0.95\times0.99\times0.97=\mathbf{0.894}$. The weakest machine (0.95) is the best target: raising it to 0.99 gives $0.98\times0.99\times0.99\times0.97=0.932$.
Scale effect: 10 components at 0.99 each give $0.99^{10}=0.904$; 50 give $0.605$; 100 components at 0.999 give $0.905$. Complexity must be paid for with component quality.
Rates add: components with MTBFs of 10,000 h, 5,000 h and 20,000 h give $\lambda_s=10^{-4}+2\times10^{-4}+0.5\times10^{-4}=3.5\times10^{-4}$, so $MTTF_s=2{,}857$ h.

### In the news
See news box. The door-plug case is a series-logic failure: each of design, rework, inspection and records had to hold, and one missing link (no record, no inspection) was enough.

### Interview angle
> [!question] How it is asked
> "A line has 10 stations each 98% reliable and no buffers. What is line reliability and what would you do?"

> [!tip] Strong answer includes
> - $0.98^{10}=81.7\%$ and the product rule
> - Improve the weakest or highest-consequence element first (Pareto)
> - Add buffers or parallel/redundant paths at bottleneck stations
> - Independence assumption: say when it fails (shared power, shared operator)

---
## 5. Parallel, k-out-of-n and Standby Redundancy
> 🟠 Tier 2 · _Key points:_ redundancy formulas; k-of-n binomial; standby vs active

### Definition
**Active parallel** (any one suffices): $R_p=1-\prod_i(1-R_i)$.
**k-out-of-n** (identical, independent, each $R$): the system works if at least $k$ of $n$ work:

$$R_{k/n}=\sum_{i=k}^{n}\binom{n}{i}R^{i}(1-R)^{n-i}$$

Series is $n/n$ and parallel is $1/n$. **Standby** redundancy keeps the spare unpowered until needed; with perfect switching and exponential identical units, $R(t)=e^{-\lambda t}(1+\lambda t)$ and $MTTF=2/\lambda$ for one standby (versus $1.5/\lambda$ for active parallel pair). Imperfect switch reliability and spare dormancy failures reduce this. Redundancy adds cost, weight and maintenance, and is limited by **common-cause failure** (sub-topic 13). Mixed networks are solved by collapsing parallel groups into single equivalent blocks.

### Example
- Two parallel pumps at 0.90: $1-0.1^2=0.99$; three: 0.999.
- Series-parallel: stage A (0.95) then two parallel B units (0.90 each) then C (0.98): $0.95\times0.99\times0.98=\mathbf{0.9217}$.
- A 2-out-of-3 sensor vote with each sensor 0.90: $3(0.9)^2(0.1)+0.9^3=0.243+0.729=\mathbf{0.972}$; a 3-out-of-4 arrangement at 0.90 gives 0.948.
- Standby vs active, two units with MTTF 1,000 h over a 500 h mission: single unit 0.607; active pair $2e^{-0.5}-e^{-1}=0.845$; standby $e^{-0.5}(1.5)=\mathbf{0.910}$. Mean lives: 1,500 h active pair, 2,000 h standby.

### In the news
See news box. Aviation certifies redundancy (hydraulics, flight computers) precisely because single-point failures cost so much; the news item on downtime cost per hour is the economic case for redundancy on critical plant utilities (compressors, cooling water).

### Interview angle
> [!question] How it is asked
> "Is a second standby compressor worth buying? How would you justify it?"

> [!tip] Strong answer includes
> - Compute system reliability/availability with and without the spare ($1-(1-A)^2$)
> - Compare incremental capex and carrying cost with expected downtime cost avoided (hours saved x cost per hour), possibly via [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]
> - Mention common-cause failure and switching reliability
> - Alternatives: spares inventory, faster repair, load sharing

---
## 6. Availability: Inherent, Achieved and Operational
> 🟠 Tier 2 · _Key points:_ A_i, A_a, A_o; MTBM, MDT; system availability

### Definition
Availability is the probability that a repairable item is working when needed. Definitions used in reliability practice:

$$A_i=\frac{MTBF}{MTBF+MTTR},\qquad A_a=\frac{MTBM}{MTBM+\bar M},\qquad A_o=\frac{MTBM}{MTBM+MDT}$$

- **Inherent** $A_i$: design-level, corrective repair only, ideal support (no logistics or admin delay).
- **Achieved** $A_a$: includes preventive as well as corrective maintenance time ($\bar M$ = mean active maintenance time), still excluding delays.
- **Operational** $A_o$: real-world, with mean downtime $MDT$ including logistic delay (waiting for spares) and administrative delay (permits, approvals).

Series systems multiply availabilities; parallel systems use $1-\prod(1-A_i)$ (assuming independent repair crews). Availability lets an operations manager trade reliability against maintainability: for target $A$ and given MTBF the allowable repair time is $MTTR=MTBF(1-A)/A$. Contrast with **OEE availability**, which is a *time-based plant metric* excluding planned stops (see [[018 Capacity Management & OEE]]).

### Example
A press has MTBF 140 h and MTTR 4 h: $A_i=140/144=97.2\%$. In practice the mean time between maintenance is 200 h (including PM) and each stop averages 4 h active repair + 4 h waiting for a spare + 2 h approvals = 10 h MDT, so $A_o=200/210=\mathbf{95.2\%}$. Two thirds of downtime is not repair: a spares and process fix is worth more than faster fitters.
Target 98% with MTBF 400 h needs $MTTR=400\times0.02/0.98=8.2$ h. Three machines with availabilities 0.95, 0.97 and 0.99 in series give $0.912$; two parallel 90% units give 0.99.

### In the news
See news box. Siemens notes that average recovery time per incident *rose* from 49 to 81 minutes between 2019 and 2024: operational availability is being eroded by repair and logistic delays even as failure counts fall.

### Interview angle
> [!question] How it is asked
> "MTBF is 400 h and MTTR 8 h. Availability? And what do you do to reach 98.5%?"

> [!tip] Strong answer includes
> - $400/408=98.0\%$ and the formula, with the exponential/steady-state assumption
> - Differentiate inherent vs operational availability and MDT components
> - Levers: reliability (design, proactive) and maintainability (spares, tools, skills, diagnostics)
> - SAP link: breakdown data in [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]] gives MTBF/MTTR

---
## 7. FMEA and FMECA
> 🟠 Tier 2 · _Key points:_ S, O, D; RPN limits; AIAG-VDA Action Priority

### Definition
**Failure Mode and Effects Analysis (FMEA)** is a structured, bottom-up review of how each element of a design (DFMEA), process (PFMEA) or asset could fail, what the effect is, and how it is controlled. **FMECA** adds *criticality* ranking. Columns: function, failure mode, effect, severity (S), cause, occurrence (O), current controls, detection (D), then actions and re-scored values.

$$RPN=S\times O\times D\quad(\text{each }1\text{ to }10,\ \text{range }1\text{ to }1000)$$

Weaknesses of RPN: different S/O/D combinations give the same number, scales are ordinal (not arithmetic), and a safety-critical mode with low occurrence can score low. The **AIAG & VDA FMEA Handbook (2019)** therefore replaced RPN with **Action Priority (AP)**, rated High / Medium / Low, which weighs severity first, then occurrence, then detection across all 1,000 S-O-D combinations, and it introduced a seven-step approach (planning, structure analysis, function analysis, failure analysis, risk analysis, optimisation, results documentation). IEC 60812 is the generic standard. In APQP FMEAs feed control plans ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

### Example
| Failure mode | S | O | D | RPN |
|---|---|---|---|---|
| A: gearbox guard missing, operator contact | 9 | 2 | 3 | 54 |
| B: label misprint | 4 | 7 | 8 | 224 |
| C: bearing seizure (pump) | 8 | 5 | 6 | 240 |

RPN ranks C > B > A, but A is a safety hazard and must be addressed regardless. After adding vibration monitoring to C, $D$ falls from 6 to 2: $RPN=8\times5\times2=80$. Re-scoring must reflect a *real* control, not a hoped-for one.

### In the news
See news box. In the door-plug case, a rework step with no record and no inspection corresponds to a very high detection score (D close to 10), with a catastrophic severity.

### Interview angle
> [!question] How it is asked
> "What are the drawbacks of RPN and how would you prioritise FMEA actions?"

> [!tip] Strong answer includes
> - S, O, D definitions and the multiplication
> - Weaknesses: equal weighting, ordinal scales, duplicates
> - Severity-first prioritisation or AIAG-VDA Action Priority; always act on S 9-10
> - Link FMEA to control plan, maintenance plan and [[008 Six Sigma & Quality Tools]]

---
## 8. Fault Tree Analysis and Cut Sets
> 🟠 Tier 2 · _Key points:_ top-down; AND/OR gates; minimal cut sets; single points of failure

### Definition
**Fault tree analysis (FTA, IEC 61025)** works top-down from an undesired **top event** and uses logic gates (AND, OR) to decompose it into basic events. It is the complement of FMEA (bottom-up). For independent basic events with probabilities $p_i$:

$$P_{AND}=\prod p_i,\qquad P_{OR}=1-\prod(1-p_i)\approx\sum p_i\ (\text{rare events})$$

A **cut set** is a set of basic events that together cause the top event; a **minimal cut set** has none removable. Single-event cut sets are **single points of failure**; the number of events in a cut set shows redundancy depth. Use FTA for safety and root cause (plant incidents, recalls); use FMEA to enumerate modes. 5-Why and Ishikawa are lighter alternatives, and an FTA is the formal form of root-cause logic in 8D.

### Example
Top event: loss of cooling flow to a reactor. Logic: (Pump 1 fails AND Pump 2 fails) OR (Controller fails). Probabilities over the mission: each pump 0.05, controller 0.004.
- Pump branch: $0.05\times0.05=0.0025$.
- Top event: $1-(1-0.0025)(1-0.004)=\mathbf{0.00649}$ (0.65%).
- Minimal cut sets: {P1, P2} and {C}. The controller is a single point of failure carrying 62% of the risk ($0.004/0.00649$). Duplicating the controller (both must fail, $0.004^2=1.6\times10^{-5}$) gives $1-(0.9975)(1-1.6\times10^{-5})=0.00252$, a 61% cut in risk.

### In the news
See news box. Investigators' causal chain for the door plug (no work record, no rework inspection, weak safety management) is an AND of independent lapses: each barrier that would have broken the chain was absent or ineffective.

### Interview angle
> [!question] How it is asked
> "A conveyor system stops 3 times a month. How would you find the root cause and which tool would you use?"

> [!tip] Strong answer includes
> - Stop and breakdown data first (Pareto of downtime from MES/CMMS)
> - FTA for top-down logic or Ishikawa/5-Why for a single recurring event; FMEA for a design review
> - AND/OR gates and cut sets, with identification of single points of failure
> - Action hierarchy: eliminate, then detect, then respond

---
## 9. Age vs Block Replacement and the Optimal PM Interval
> 🟠 Tier 2 · _Key points:_ C_p vs C_f; cost rate; only for β>1

### Definition
Planned replacement is worth considering only when the hazard **rises** and failure costs more than planned replacement: $C_f>C_p$. Let $C_p$ = cost of a planned (preventive) replacement and $C_f$ = cost of a failure replacement (including downtime).

**Age replacement:** replace on failure or at age $T$, whichever comes first. Long-run cost per unit time:

$$C(T)=\frac{C_p\,R(T)+C_f\,[1-R(T)]}{\int_0^{T}R(t)\,dt}$$

**Block replacement:** replace at fixed calendar times $T,2T,\dots$ regardless of age, plus failure replacements in between ($M(T)$ = expected number of failures in $[0,T]$, from the renewal function):

$$C_b(T)=\frac{C_p+C_f\,M(T)}{T}$$

Block replacement is simpler to schedule (a shutdown every $T$) but wastes life of young parts. Compare both against run-to-failure cost $C_f/MTTF$. For exponential life no $T$ beats run-to-failure. Solve $C(T)$ numerically (Excel Solver or Python).

### Example
Seal set: Weibull $\beta=2.5$, $\eta=1{,}000$ h, $C_p=₹5{,}000$, $C_f=₹30{,}000$ (including lost output). All computed numerically in Python.

| Interval $T$ (h) | Age replacement cost (₹/h) | Block replacement cost (₹/h) |
|---|---|---|
| 300 | 20.97 | 21.50 |
| 400 | 19.05 | 19.79 |
| 450 | **18.87** (minimum) | 19.69 (minimum is 19.68 at about 438) |
| 500 | 19.02 | 19.88 |
| 700 | 21.39 | 22.14 |
| 1,000 | 26.63 | 26.07 |
| Run to failure | 33.81 | 33.81 |

Age replacement at about **450 h** costs ₹18.9/h versus ₹33.8/h for run-to-failure, a **44% saving**. The curve is flat near the optimum, so a practical 400 to 500 h interval aligned to a shutdown costs little. Block replacement is about 4% dearer at its best, the price of administrative simplicity. If $C_f/C_p$ were 1.5 rather than 6, the optimum moves much further out and the saving shrinks; a ratio below about 1.0 means never replace early.

### In the news
See news box. At the per-hour downtime costs reported by Siemens, $C_f$ is dominated by lost output, so the ratio $C_f/C_p$ is large and interval-based replacement of wear-out parts pays; for FMCG-type low downtime costs, run-to-failure on cheap parts is often the right call.

### Interview angle
> [!question] How it is asked
> "A machine part costs ₹5,000 to replace in a planned stop and ₹30,000 to replace after a breakdown. How would you decide the replacement interval?"

> [!tip] Strong answer includes
> - Need failure data and a shape parameter $\beta>1$; otherwise no PM benefit
> - Cost-rate formula, optimisation, and flatness of the curve near the optimum
> - Age vs block replacement trade-off (waste of life vs simplicity), opportunistic replacement at shutdowns
> - Sensitivity to $C_f/C_p$; link to replacement economics in [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]

---
## 10. Spare Parts Provisioning with the Poisson Model
> 🟠 Tier 2 · _Key points:_ demand over lead time ~ Poisson; critical ratio; service level

### Definition
For a spare that is used only when its parent fails and is repaired or replenished after a lead time $L$, demand during $L$ is approximately **Poisson** with mean $\mu=N\lambda L$ ($N$ identical installed units, failure rate $\lambda$):

$$P(D=x)=\frac{\mu^x e^{-\mu}}{x!},\qquad \text{Fill probability}=P(D\le s)=\sum_{x=0}^{s}\frac{\mu^xe^{-\mu}}{x!}$$

Choose stock $s$ as the smallest value meeting a target service level, or use the **cost trade-off** (newsvendor-style critical ratio): stock up to the smallest $s$ with $P(D\le s)\ge \dfrac{C_u}{C_u+C_o}$, where $C_u$ = cost of one stock-out and $C_o$ = holding cost of one extra spare over the period. Constant failure rate is assumed (Poisson fails for wear-out parts: use the [[211 Reliability & Survival Analysis|renewal]] logic instead, or schedule replacement). Insurance spares, rotables, and pooling across plants cut stock needs; see [[003 Inventory Management]], [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]] and spares in [[022 Maintenance Management (TPM-RCM)|maintenance management]].

### Example
**(a) Lead-time stock.** 40 identical bearings run, each with MTBF 8,000 h; replacement lead time is 3 months (2,190 h). $\mu=40\times2190/8000=10.95$. Smallest $s$ for 90% fill: $P(D\le14)=0.858$, $P(D\le15)=0.910$, so **$s=15$**; for 95%, $P(D\le16)=0.946$, $P(D\le17)=0.969$, so $s=17$. The last two units buy 6 points of service.
**(b) Cost-based.** A critical gearbox spare: demand $\mu=1.8$ per year; stock-out cost (plant stoppage) $C_u=₹1{,}50{,}000$; holding cost per spare per year $C_o=₹12{,}000$. Critical ratio $=150{,}000/162{,}000=0.926$. $P(D\le3)=0.891<0.926$ and $P(D\le4)=0.964$, so hold **4** spares. Holding 4 spares costs $4\times12{,}000=₹48{,}000$ a year, against an expected stop cost far higher with 0 to 2 spares.

### In the news
See news box. With average recovery time lengthening (49 to 81 minutes in the Siemens data), waiting for parts is a leading delay and spares policy is part of availability.

### Interview angle
> [!question] How it is asked
> "How many spare motors should the plant keep for 40 installed motors?"

> [!tip] Strong answer includes
> - Poisson demand over the lead time, with $\mu=N\lambda L$
> - Service-level or critical-ratio logic with explicit stock-out cost
> - Criticality segmentation (VED analysis), shared/pooled and repairable spares
> - Assumption check: wear-out parts need scheduled replacement forecast, not Poisson

---
## 11. Condition Monitoring and the P-F Interval
> 🟠 Tier 2 · _Key points:_ P-F curve; inspect at half P-F; inspection economics

### Definition
Many failures give warning. On the **P-F curve** the **potential failure P** is the earliest point at which degradation is detectable (vibration, temperature, oil particles, current signature, ultrasound) and **functional failure F** is when the asset can no longer do its job. The time between them is the **P-F interval**.

- To detect P reliably, inspect at an interval of **at most the P-F interval**; the common rule is **about half the P-F interval**, so there is time between detection and F to plan the repair (net P-F interval).
- If inspection interval $I\le PF$, an event is caught (with a perfect technique). With a longer interval, the chance of catching it before F is about $PF/I$.
- Condition-based tasks are valid only where degradation is detectable and the P-F interval is longer than the lead time to act. Compare technique costs with the cost of failure. For techniques see [[022 Maintenance Management (TPM-RCM)|condition-based monitoring and predictive maintenance]]; for SAP measuring points see [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]].

### Example
A fan bearing shows vibration at P about 6 weeks before seizure ($PF=6$ weeks).
- Required inspection interval: 6 weeks at most; 3 weeks (half the P-F) leaves a net window of at least 3 weeks for ordering parts and planning a shutdown.
- A monthly (4-week) route still catches every event in this model, but the worst-case notice is only 2 weeks.
- A quarterly (12-week) route catches only about $6/12=50\%$ of events before failure.
- Economics of a 3-weekly route: about 17 visits at ₹800 = ₹13,600 a year, against 1.5 failures a year at ₹1.2 lakh each = ₹1.8 lakh. If monitoring prevents 80% of failures, the saving is $0.8\times1.8-0.136=₹1.30$ lakh a year.

### In the news
See news box. Siemens' finding that nine in ten firms do some condition monitoring, and about half have PdM teams, shows monitoring has become mainstream but gains depend on correct intervals and follow-through.

### Interview angle
> [!question] How it is asked
> "Vibration analysis finds a fault 2 weeks before failure. How often should you monitor?"

> [!tip] Strong answer includes
> - P-F interval concept and inspection at about half of it
> - Detection must leave enough time to plan the intervention (spares, shutdown)
> - Cost of monitoring vs cost of failure; applicability only to detectable degradation
> - Track false alarms and missed events, and tie to a work-order trigger

---
## 12. Warranty Cost Models
> 🟠 Tier 2 · _Key points:_ FRW, pro-rata, non-renewing; reliability to cost link

### Definition
Warranty is a promise to repair, replace or refund if the product fails within warranty period $W$. The expected cost per unit is driven directly by reliability:

- **Free replacement/repair warranty (FRW):** the seller bears the full cost $c$ of each failure within $W$. With **minimal repair** (item restored to its pre-failure state), the expected number of failures in $[0,W]$ is the cumulative hazard $H(W)=\int_0^W h(t)\,dt$; cost per unit $=c\,H(W)$. For Weibull, $H(W)=(W/\eta)^\beta$.
- **Pro-rata warranty (PRW):** the refund or credit falls with age at failure, e.g. $P(1-t/W)$ for failure at age $t<W$.
- **Non-renewing:** a replacement carries only the *remaining* warranty. **Renewing:** each replacement restarts the full warranty (costlier to the seller).
- Other forms: combination FRW/PRW (tyres, batteries), two-dimensional warranty (age and usage, e.g. 3 years or 60,000 km in automobiles), and extended warranties priced as insurance. Provisions are booked as warranty expense under accrual accounting ([[108 Financial Statements & Ratios]]).

### Example
**(a) FRW with Weibull life.** An appliance has $\beta=1.8$, $\eta=6$ years; warranty $W=2$ years; each repair costs ₹3,500.
$F(2)=1-\exp[-(2/6)^{1.8}]=12.9\%$ of units fail at least once. Expected repairs per unit (minimal repair) $=(1/3)^{1.8}=0.138$, so warranty cost is $0.138\times3{,}500=\mathbf{₹484}$ per unit, about 1.2% of a ₹40,000 selling price.
**(b) Exponential life and pro-rata.** Failure rate 0.15 per year, price ₹4,000, $W=2$ years.
- FRW replacement cost ₹2,800: expected cost of the first failure $=2800\times(1-e^{-0.3})=₹726$.
- Pro-rata refund $4000(1-t/2)$: expected refund $=₹544$, about 25% cheaper for the seller, because late failures cost less. Tail effects (later repeated failures) are excluded in both.
If a design fix raises $\eta$ from 6 to 8 years, $H(2)$ falls to $0.082$ and cost to ₹289 per unit, a 40% cut: reliability investment pays back through warranty cost.

### In the news
See news box. Siemens' doubling of automotive downtime cost shows how field and plant failures translate into money; Indian OEMs and consumer-durable makers set warranty reserves against this kind of failure data, and a rising failure rate is an early signal to the quality function.

### Interview angle
> [!question] How it is asked
> "A competitor offers 5-year warranty. How do you decide whether to match it?"

> [!tip] Strong answer includes
> - Expected warranty cost $=c\,H(W)$ from the failure distribution, not a flat percentage
> - Compare with price premium, brand and sales gains; consider pro-rata or two-dimensional limits
> - Reliability growth or supplier cost-sharing as ways to reduce exposure
> - Tie field data back to [[008 Six Sigma & Quality Tools]] and [[011 Quality Management (TQM)]]

---
## 13. RCM Decision Logic and the Failure Patterns
> 🟠 Tier 2 · _Key points:_ consequences first; task selection; hidden functions

### Definition
**Reliability-centred maintenance (RCM)** selects maintenance tasks by function and consequence, not by habit. Developed by Nowlan and Heap (United Airlines, 1978) and codified in **SAE JA1011**, which sets seven questions that any process must answer: functions and standards, functional failures, failure modes, effects, consequences, preventive tasks, and default actions if no task fits. Overview in [[022 Maintenance Management (TPM-RCM)|maintenance management]].

**Decision logic (simplified):**
1. **Consequence?** safety/environmental, operational (output, quality, cost), or non-operational (repair cost only), or **hidden** (a protective function whose failure shows only when needed).
2. **Is a predictive (on-condition) task technically feasible and worth doing?** (detectable P, long enough P-F) then do it.
3. **Is scheduled restoration or discard feasible and cost-effective?** (a clear wear-out age, $\beta>1$, most units survive to it) then do it.
4. **Hidden function?** a failure-finding task (functional test) at a computed interval (sub-topic 14).
5. If nothing is effective: redesign (mandatory for safety) or run to failure (acceptable only when consequences are small).

The percentages of items with no wear-out zone (see sub-topic 2) explain why RCM replaced blanket time-based overhauls: much calendar-based PM adds cost and infant-mortality risk without benefit. In practice, rank assets by criticality (consequence x likelihood) first and apply full RCM only to the top slice; use FMEA (sub-topic 7) as the analysis engine and a CMMS to hold the resulting tasks ([[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]]).

### Example
Boiler feed pump (single, critical): FMEA shows bearing seizure (S=8). P-F interval about 5 weeks, vibration route fortnightly: **on-condition task**. Mechanical seal wears out around 12,000 h ($\beta\approx3$): **scheduled replacement** at the annual shutdown. Standby pump auto-start fails silently: **failure-finding test** monthly. Instrument-air dryer on a redundant train: **run to failure**. Four assets, four different strategies, and total PM labour typically falls once calendar tasks with no technical basis are deleted.

### In the news
See news box. Aviation, the home of RCM, relies on maintenance programmes built on this logic; the door-plug findings show that even a strong programme fails if work records and inspection steps are not enforced.

### Interview angle
> [!question] How it is asked
> "How do you decide the maintenance strategy for a new plant with 500 assets?"

> [!tip] Strong answer includes
> - Criticality screening, then RCM on the critical slice
> - Consequence-driven task hierarchy: predict, restore, find hidden failures, redesign, run to failure
> - Data: failure history, Weibull $\beta$, P-F intervals, cost of failure
> - Continuous review through KPIs (MTBF, planned-work %, backlog) and feedback to design

---
## 14. ⭐ Advanced: Hidden Failures, Failure-Finding Intervals and Common-Cause Failure
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **hidden (dormant) function** (relief valve, fire pump, standby generator, trip circuit) fails undetected and matters only when demanded. Its failure rate $\lambda$ is not the issue; its **unavailability** is. With periodic functional tests at interval $T$ (perfect testing, failures found at the next test):

$$U(T)\approx\frac{\lambda T}{2}\ \ (\lambda T\ll1),\qquad T=\frac{2U}{\lambda}$$

A **multiple failure** needs the demand (rate $\lambda_d$ of the protected device failing) to occur while the protection is down: rate $\approx\lambda_d\,U$. RCM sets the failure-finding interval so that the multiple-failure risk meets a target.

**Common-cause failure (CCF):** redundant units fail together through a shared cause (design flaw, maintenance error, power, environment). The **beta-factor model** assumes a fraction $\beta_c$ of each unit's failure probability is common to all units. For two parallel units with unit unreliability $q$: system unreliability $=1-(1-\beta_c q)\big(1-[(1-\beta_c)q]^2\big)$, dominated by the $\beta_c q$ term once $\beta_c$ is non-trivial. Do not confuse $\beta_c$ with Weibull $\beta$. Defence: diversity, separation, staggered maintenance (so one error cannot hit both trains).

### Example
**Failure-finding.** Relief valve failure rate $\lambda=0.04$ per year; annual test gives $U=0.04\times1/2=2\%$. To hold unavailability to 0.5%: $T=2\times0.005/0.04=0.25$ years, i.e. test **quarterly**. If the process upset rate is 0.2 per year, multiple-failure rate $=0.2\times0.005=0.001$ per year (one per 1,000 years).
**CCF.** Two parallel pumps, unit failure probability over 1,000 h $q=1-e^{-0.1}=0.0952$.

| $\beta_c$ | System failure probability | Reliability |
|---|---|---|
| 0 (ideal independence) | 0.00906 | 0.9909 |
| 0.05 | 0.01289 | 0.9871 |
| 0.10 | 0.01678 | 0.9832 |
| 0.20 | 0.02472 | 0.9753 |

A modest 10% common cause nearly **doubles** system unreliability (x1.85) relative to the independent calculation, which is why redundancy claims need a CCF review.

### In the news
See news box. The door-plug failure is a dormant-defect story: missing bolts did not announce themselves until the plug moved in service, an argument for functional verification and records at every intrusive maintenance step.

### Interview angle
> [!question] How it is asked
> "You have two redundant pumps and the plant still tripped. What could have gone wrong?"

> [!tip] Strong answer includes
> - Common-cause modes: same maintenance error, shared power/control, same batch, same environment
> - Hidden failure: standby not tested (auto-start, valve position), failure-finding interval too long
> - Fixes: test regime based on $U=\lambda T/2$, diversity, staggered maintenance, post-maintenance verification
> - Quantify with a beta-factor and a fault tree rather than "add another spare"
