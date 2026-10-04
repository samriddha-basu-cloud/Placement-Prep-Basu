---
tags: [operations-management, tier2]
area: Operations Management
topic: "Maintenance Management (TPM/RCM)"
tier: Tier 2
roles: Operations
status: complete
subtopics: 10
---
# Maintenance Management (TPM/RCM)

⬅ [[021 Scheduling & Sequencing]] · [[_Index - Operations Management|Operations Management]] · [[146 Operations Research - Linear Programming]] ➡
> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Types of Maintenance]]
2. [[#2. Total Productive Maintenance (TPM)]]
3. [[#3. Reliability-Centered Maintenance (RCM)]]
4. [[#4. MTBF & MTTR]]
5. [[#5. Condition-Based Monitoring]]
6. [[#6. Predictive Maintenance (PdM)]]
7. [[#7. OEE and Maintenance Link]]
8. [[#8. Spare Parts Management]]
9. [[#9. ⭐ Advanced: Reliability Mathematics (Bathtub Curve, Weibull, Series-Parallel)]]
10. [[#10. ⭐ Advanced: Maintenance KPIs and Cost Optimisation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI-driven predictive maintenance reaches steel and railways
> **Indian Railways (reported 8 Dec 2025).** Railways is piloting AI-driven predictive maintenance for signalling systems at selected stations, has adopted the **Online Monitoring of Rolling Stock System (OMRS)** and **Wheel Impact Load Detector (WILD)**, and signed an MoU (July 2025) with the Dedicated Freight Corridor Corporation for a **wayside machine-vision inspection system** that detects hanging or missing train components. A second MoU with Delhi Metro covers automatic wheel-profile measurement giving real-time wheel wear data. The stated focus is "standardised failure-prediction logic and automated alert mechanisms". ([Construction World](https://www.constructionworld.in/transport-infrastructure/metro-rail-and-railways-infrastructure/railways-expand-ai-based-predictive-maintenance-systems/82809))
>
> **Tata Steel x Google Cloud (reported Sept 2025).** Tata Steel partnered with Google Cloud on IoT-sensor and ML-based predictive maintenance, monitoring temperature, vibration and energy use, with the reported sites being European operations (Netherlands, UK). The source reports improved reliability and fewer unplanned outages but gives **no quantified savings**, so treat the benefit as qualitative. ([WebProNews](https://www.webpronews.com/tata-steel-teams-up-with-google-cloud-for-ai-driven-predictive-maintenance/), a secondary report)
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Types of Maintenance
> 🟠 Tier 2 · _Tracker hint:_ Corrective, Preventive, Predictive, Proactive

### Definition
| Type | Trigger | Idea | Best for |
|---|---|---|---|
| **Corrective / breakdown** | Failure occurred | Run to failure, then repair | Non-critical, cheap, redundant assets |
| **Preventive (PM)** | Calendar or usage interval | Service before failure at fixed intervals | Wear-out failures with predictable life |
| **Predictive (PdM / CBM)** | Measured condition | Act when a condition indicator crosses a threshold | Critical, costly assets with detectable degradation |
| **Proactive** | Root cause | Remove the cause (alignment, balancing, contamination control, redesign) to extend life | Chronic repeat failures |

Corrective is *reactive* and often the most expensive when downtime is included; preventive risks over-maintaining (replacing parts with life left) and **infant-mortality** errors introduced by maintenance itself. Predictive uses the **P-F interval** (time between a detectable potential failure P and functional failure F). A healthy plant targets mostly planned work (a common benchmark is 80% planned vs 20% reactive; treat figures as rule-of-thumb). Also: *design-out maintenance* and *opportunistic maintenance*.

### Example
A 20 kW conveyor motor (cheap, spare in stock, redundant line): run-to-failure is rational. A main kiln drive gearbox (₹40 lakh, 6 weeks lead time, shuts the plant): vibration and oil monitoring (predictive) plus alignment and filtration (proactive). Total cost = repair + downtime: if failure costs ₹2 lakh per hour of downtime and a breakdown lasts 12 hours, downtime alone is ₹24 lakh, dwarfing a planned 4-hour stop (₹8 lakh) done at a weekend shutdown.

### In the news
See news box. Indian Railways' shift from fixed-interval inspection to sensor-triggered checks (WILD, OMRS) is a move from preventive to predictive maintenance.

### Interview angle
> [!question] How it is asked
> "What maintenance strategy would you use for a bottleneck machine versus a non-critical one?"

> [!tip] Strong answer includes
> - Four types, with trigger and trade-off for each
> - Criticality-based selection (not one strategy for everything)
> - Total cost view: repair + downtime + safety
> - Direction of travel: reactive to preventive to predictive/proactive

---

## 2. Total Productive Maintenance (TPM)
> 🟠 Tier 2 · _Tracker hint:_ 8 pillars; autonomous maintenance; planned maintenance

### Definition
**TPM** (Japan, Nippon Denso/Seiichi Nakajima, JIPM) makes *everyone*, operators included, responsible for equipment effectiveness, targeting **zero breakdowns, zero defects, zero accidents**. It attacks the **six big losses** (breakdowns, setup/adjustment, minor stops, reduced speed, process defects, start-up yield) which sum to OEE.

**Eight pillars:**
1. **Autonomous Maintenance (Jishu Hozen)**: operators clean, lubricate, inspect (CLI), via a 7-step programme from initial cleaning to full self-management.
2. **Focused Improvement (Kobetsu Kaizen)**: project teams attack the big losses.
3. **Planned Maintenance**: scheduled and predictive work by the maintenance department.
4. **Quality Maintenance (Hinshitsu Hozen)**: keep equipment conditions that give zero defects.
5. **Early Equipment / Product Management**: design for maintainability.
6. **Training and Education**: skills for operators and technicians.
7. **Safety, Health and Environment**.
8. **TPM in Administration (Office TPM)**.
(JIPM later versions group these slightly differently; the eight above is the most common exam list.)

Foundation: 5S. Metric: OEE.

### Example
A packaging line at 62% OEE. Operators start autonomous maintenance (clean sensors, tighten, lubricate per 15-minute checklists), planned maintenance replaces wear parts on a calendar, and a kaizen team fixes the top minor-stop cause (a misaligned feeder). Over a year minor stops drop and OEE moves to ~75% (illustrative). Many Indian auto and tyre plants run TPM; Maruti Suzuki and Tata Motors suppliers often pursue the JIPM TPM Award.

### In the news
See news box. Sensor-based monitoring complements TPM: operators' daily checks catch visible issues, and sensors catch hidden ones.

### Interview angle
> [!question] How it is asked
> "What is TPM and how does it differ from preventive maintenance?" or "Name the 8 pillars."

> [!tip] Strong answer includes
> - Operators share ownership; not only the maintenance department
> - Pillars named, with autonomous maintenance in more detail
> - Link to OEE and the six big losses
> - Implementation traps: no management support, treating it as a cleaning drive

---

## 3. Reliability-Centered Maintenance (RCM)
> 🟠 Tier 2 · _Tracker hint:_ Failure modes, consequences, maintenance strategy selection

### Definition
**RCM** (Nowlan & Heap, United Airlines, 1978; standard SAE JA1011) is a structured way of deciding what maintenance each asset needs, based on **function, failure and consequence**, not on habit. Seven questions:
1. Functions and performance standards?
2. How can it fail (functional failures)?
3. What causes each failure (failure modes)?
4. What happens when it fails (effects)?
5. How much does it matter (consequences: safety, environmental, operational, non-operational)?
6. What can be done to predict or prevent it?
7. What if nothing suitable can be found (default actions)?

Decision logic: if a **scheduled on-condition** task is technically feasible and worth doing, use it; else **scheduled restoration/discard**; else **failure-finding** for hidden functions; else redesign or run-to-failure when consequences are small. FMEA supports it: $RPN = S\times O\times D$ (severity, occurrence, detection, each 1–10).

### Example
Pump with failure mode "bearing seizure": S = 8, O = 5, D = 6, so RPN = 240 (high). Detection improves with vibration monitoring (D 6 to 2): RPN = 8 × 5 × 2 = 80. Strategy chosen: on-condition vibration monitoring because failure shows warning (P-F interval of weeks). For a redundant standby lamp, the strategy is run to failure.

### In the news
See news box. Aviation and railways are RCM's home ground; Railways' standardised failure-prediction logic is an RCM-type consequence-based approach.

### Interview angle
> [!question] How it is asked
> "How would you decide the maintenance plan for 500 assets in a new plant?"

> [!tip] Strong answer includes
> - Criticality ranking first (focus RCM on critical assets)
> - Function, failure mode, effect, consequence logic
> - Strategy selection hierarchy
> - RPN and data from CMMS/history; review periodically

---

## 4. MTBF & MTTR
> 🟠 Tier 2 · _Tracker hint:_ Mean Time Between Failures; Mean Time To Repair; availability formula

### Definition
$$MTBF=\frac{\text{total operating (up) time}}{\text{number of failures}},\qquad MTTR=\frac{\text{total repair (down) time}}{\text{number of repairs}}$$

**Inherent availability** $A=\dfrac{MTBF}{MTBF+MTTR}$. Failure rate $\lambda = 1/MTBF$ (constant-rate/exponential assumption), reliability $R(t)=e^{-t/MTBF}$. For non-repairable items use **MTTF** (mean time to failure). Related: **MTTA** (to acknowledge), **MTBM** (between maintenance).

Improving MTBF = better reliability (design, proactive actions, PM); improving MTTR = maintainability (spares, tooling, skills, modular design, diagnostics). Operational availability also includes logistics and administrative delay, so it is lower than inherent availability.

### Example
A press ran 700 hours in a month, with 5 breakdowns totalling 20 hours of repair.
- MTBF = 700 / 5 = **140 h**; MTTR = 20 / 5 = **4 h**.
- Availability = 140 / (140 + 4) = **97.2%**.
Halving MTTR to 2 h gives 140/142 = 98.6%; doubling MTBF to 280 h with MTTR 4 gives 280/284 = 98.6%. Equal gains by either route.

### In the news
See news box. Wayside monitoring systems aim at both levers: earlier detection lengthens MTBF by avoiding failures, and faster diagnosis reduces MTTR.

### Interview angle
> [!question] How it is asked
> "A machine has MTBF of 100 h and MTTR of 5 h. What is its availability, and how do you improve it?"

> [!tip] Strong answer includes
> - Correct formulas and units, availability $=100/105=95.2\%$
> - Separate levers: reliability (MTBF) vs maintainability (MTTR)
> - Assumption of constant failure rate
> - Link to OEE availability and spare-part strategy

---

## 5. Condition-Based Monitoring
> 🟠 Tier 2 · _Tracker hint:_ Vibration, thermal, oil analysis, ultrasonic — techniques

### Definition
**Condition-based maintenance (CBM)** performs maintenance when measurements show degradation, exploiting the **P-F curve**: a detectable symptom appears at P, well before functional failure at F, and the inspection interval should be about half the P-F interval.

| Technique | Detects | Typical assets |
|---|---|---|
| **Vibration analysis** (FFT spectra, ISO 20816 severity) | Imbalance, misalignment, bearing/gear faults, looseness | Motors, pumps, fans, gearboxes |
| **Infrared thermography** | Hot spots from friction, loose electrical joints, insulation | Switchgear, motors, bearings, steam lines |
| **Oil analysis** (viscosity, particle count, wear metals, water) | Wear, contamination, lubricant degradation | Gearboxes, hydraulics, engines |
| **Ultrasonic testing** | Leaks (air, steam, vacuum), early bearing friction, electrical discharge | Compressed-air lines, valves |
| **Motor current signature analysis**, **acoustic emission**, **eddy current**, **NDT** | Rotor bar, cracks, corrosion | Motors, pressure parts |

Triggering requires **alert and alarm thresholds** set against baselines.

### Example
A gearbox oil sample shows iron at 120 ppm versus a baseline of 40 ppm and rising, with a particle count over limit. P is detected; the plant schedules replacement at the next weekend shutdown rather than losing a week to a seizure. If the P-F interval is 6 weeks, inspect roughly every 3 weeks.

### In the news
See news box. Railway wheel-impact detectors and machine-vision systems are CBM techniques; Tata Steel's temperature and vibration monitoring is the vibration and thermal case.

### Interview angle
> [!question] How it is asked
> "Which condition monitoring technique for an electric motor? For compressed air?"

> [!tip] Strong answer includes
> - Match technique to failure mode
> - P-F interval and inspection frequency
> - Baselines and thresholds; cost-benefit by criticality
> - Skills needed: trained analysts or vendor contract

---

## 6. Predictive Maintenance (PdM)
> 🟠 Tier 2 · _Tracker hint:_ IoT sensors, ML models, anomaly detection

### Definition
**PdM** uses data from sensors (vibration, temperature, current, pressure, acoustic) plus operating and maintenance history to forecast failures, giving a **Remaining Useful Life (RUL)** estimate or a failure probability within a horizon.

Pipeline: sensors, edge gateway, historian or cloud, **feature engineering** (RMS, kurtosis, FFT bands, rolling stats), model, alert, work order in the CMMS/EAM (e.g. SAP PM). Model types:
- **Anomaly detection** (unsupervised): Isolation Forest, autoencoders, statistical control limits. Needs only healthy data; good when failures are rare.
- **Classification** (will it fail within N days?): random forest, gradient boosting; needs labelled failures; class imbalance is the main problem.
- **Regression / survival models** for RUL: Weibull, LSTM.
Evaluate on **precision/recall and lead time**, not accuracy; false alarms erode trust. Pitfalls: scarce failure labels, sensor drift, change in operating regime, no action path.

### Example
Illustrative: 1,000 monitored pumps, 20 real failures per year. A model with 80% recall catches 16 failures, avoiding 16 × 8 hours × ₹1.5 lakh/hour = ₹192 lakh in downtime, if it also raises 40 false alarms each costing a ₹20,000 inspection = ₹8 lakh. Net benefit ~₹184 lakh before the system cost. (Numbers are assumptions to show the method.)

### In the news
See news box. Both Tata Steel and Indian Railways describe sensor plus analytics approaches; Tata Steel's benefit is only qualitatively reported in the source.

### Interview angle
> [!question] How it is asked
> "How would you launch a predictive maintenance pilot?" or "Why do PdM projects fail?"

> [!tip] Strong answer includes
> - Start with critical assets with known failure modes, not "all assets"
> - Data readiness, failure labelling, domain input from technicians
> - Business case: avoided downtime vs false alarm cost
> - Integrate with work-order flow so predictions trigger action

---

## 7. OEE and Maintenance Link
> 🟠 Tier 2 · _Tracker hint:_ Availability pillar improvement through reduced downtime

### Definition
$$OEE = Availability\times Performance\times Quality$$
$$Availability=\frac{\text{planned production time}-\text{downtime}}{\text{planned production time}}$$
Performance = (ideal cycle time × total count) / run time; Quality = good count / total count. World-class benchmark: ~85% OEE (availability 90%, performance 95%, quality 99%, giving 0.90 × 0.95 × 0.99 = 84.6%).

Maintenance owns the **availability** pillar: breakdowns and, partly, setups and changeovers. It also touches performance (worn machines run slower, minor stops) and quality (drift, leaks). Metrics to couple: MTBF/MTTR, planned-maintenance percentage, PM compliance, backlog, **TEEP** (OEE × utilisation of calendar time).

### Example
Shift 480 minutes planned, 60 minutes breakdown/changeover downtime; performance 90%, quality 98%.
- Availability = (480 − 60)/480 = 87.5%; OEE = 0.875 × 0.90 × 0.98 = **77.2%**.
After a TPM programme cuts downtime to 30 minutes: A = 450/480 = 93.75%; OEE = 0.9375 × 0.90 × 0.98 = **82.7%**, a 5.5 point gain from maintenance alone.

### In the news
See news box. Predictive and condition-based tools target exactly the unplanned-downtime term in availability.

### Interview angle
> [!question] How it is asked
> "OEE at the plant is 60%. Where do you start?" or "How does maintenance affect OEE?"

> [!tip] Strong answer includes
> - OEE formula and compute availability from data
> - Pareto of downtime reasons (breakdown, setup, waiting)
> - Maintenance levers: PM, autonomous maintenance, spares, faster repair
> - Mention to avoid gaming OEE (planned time definition)

---

## 8. Spare Parts Management
> 🟠 Tier 2 · _Tracker hint:_ VED analysis, min-max, critical spares strategy

### Definition
Spares are different from production inventory: demand is sporadic (lumpy), costs of stock-outs can be huge, and items can be obsolete. Classification tools:
- **VED**: **V**ital (out of stock stops production), **E**ssential (causes disruption but workarounds exist), **D**esirable (little impact). Often combined with **ABC** (by value) in a matrix: vital items get high service level even if cheap or low-moving.
- **FSN** (fast, slow, non-moving) and **HML**.

**Min-max / reorder-point policy:**
$$ROP = d\times L + SS,\quad Max = ROP + Q$$
Demand rate $d$, lead time $L$. For critical, slow-moving spares, use Poisson-demand-based stocking or *insurance spares* with a service level over the lead time; consider pooling across plants, vendor-managed consignment, repairable rotables, and reverse engineering/3D printing of obsolete parts.

### Example
Bearing: use 2 per month (0.0667/day), lead time 30 days, safety stock 2: $ROP = 0.0667 \times 30 + 2 = 4$. Order quantity 3, max = 7. A vital imported gearbox, used once in 5 years at ₹30 lakh with a 20-day shutdown cost of ₹2 crore per day risk: hold one spare regardless of usage, because expected downtime cost far exceeds holding cost.

### In the news
See news box. Predictive signals let planners buy spares *before* failure, replacing "just in case" stock with "just in time for the predicted failure" for non-vital items.

### Interview angle
> [!question] How it is asked
> "How would you reduce spare-part inventory without raising downtime risk?"

> [!tip] Strong answer includes
> - Classify first: ABC-VED matrix
> - Different policy per class: vital = keep; desirable = reduce or vendor-managed
> - Cleanse obsolete and duplicate part codes; share across sites
> - Measure service level, stock-out downtime and inventory turns

---

## 9. ⭐ Advanced: Reliability Mathematics (Bathtub Curve, Weibull, Series-Parallel)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
The **bathtub curve** has three phases: infant mortality (decreasing failure rate), useful life (constant rate, random failures) and wear-out (increasing). The **Weibull** distribution captures them with the shape parameter $\beta$: $\beta<1$ infant mortality, $\beta\approx1$ random (exponential), $\beta>1$ wear-out. Reliability: $R(t)=e^{-(t/\eta)^\beta}$.

**System reliability:** series $R_s=\prod R_i$ (all must work); parallel/redundant $R_p=1-\prod(1-R_i)$. Implications: time-based PM helps only when $\beta>1$ (wear-out); for random failures ($\beta\approx1$) preventive replacement does not improve reliability and can hurt.

### Example
Exponential: MTBF 500 h, mission 100 h: $R=e^{-0.2}=0.819$. Series of three components 0.95, 0.90, 0.98: $0.95\times0.90\times0.98=0.838$. Two identical 0.90 units in parallel: $1-0.1\times0.1=0.99$, which is why critical pumps are installed in duty-standby pairs.

### In the news
See news box. Condition-based approaches suit wear-out failures with a measurable symptom; failure data needed to fit Weibull models is what PdM platforms collect.

### Interview angle
> [!question] How it is asked
> "When is preventive maintenance a waste of money?"

> [!tip] Strong answer includes
> - Bathtub curve and failure-pattern logic
> - PM works for wear-out ($\beta>1$), not random failures
> - Series vs parallel system effect and redundancy cost
> - Use data (CMMS history) to confirm patterns

---

## 10. ⭐ Advanced: Maintenance KPIs and Cost Optimisation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Key indicators: **planned maintenance percentage** (planned hours / total maintenance hours), **PM compliance** (PMs completed on time / scheduled), **schedule compliance**, **backlog** (weeks of work outstanding), **wrench time** (hands-on time / paid time; 25–35% is common in poor shops, 55%+ in good ones; benchmark figures are rough), **maintenance cost as % of replacement asset value** (often 2–3% as a rule of thumb), **MTBF, MTTR, availability**, **emergency work ratio**. Optimisation: find the **economic PM interval** where the sum of PM cost and expected failure cost is minimised; $\text{Cost rate}(T)=\dfrac{C_p R(T)+C_f(1-R(T))}{\text{expected cycle length}}$ in age-replacement models.

### Example
Plant has 1,000 maintenance hours in a month, 600 planned: planned % = 60%; 120 PM tasks scheduled and 102 done on time: PM compliance = 85%. Target: planned > 80%, compliance > 90%; fix by planner/scheduler roles, kitting parts before jobs, and shutdown planning (raises wrench time).

### In the news
See news box. Data from sensors feeds these KPIs automatically, replacing manual logs.

### Interview angle
> [!question] How it is asked
> "How would you measure whether the maintenance function is performing well?"

> [!tip] Strong answer includes
> - Leading indicators (planned %, PM compliance) and lagging ones (downtime, MTBF)
> - Cost per unit output, not only absolute spend
> - Resist cutting maintenance budget blindly (deferred maintenance cost)
> - Link to OEE and safety incidents

---
## 🔗 Go deeper: expansion notes
- [[155 Reliability Engineering & Maintenance Optimisation|Reliability Engineering & Maintenance Optimisation]]
- [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies|SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]]
