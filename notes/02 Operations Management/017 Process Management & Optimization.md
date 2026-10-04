---
tags: [operations-management, tier1]
area: Operations Management
topic: "Process Management & Optimization"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Process Management & Optimization

[[_Index - Operations Management|Operations Management]] · [[018 Capacity Management & OEE]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Process Mapping & BPMN]]
2. [[#2. Value-Added vs Non-Value-Added]]
3. [[#3. Bottleneck Identification]]
4. [[#4. Throughput & Little's Law]]
5. [[#5. Cycle Time Analysis]]
6. [[#6. Lead Time Reduction]]
7. [[#7. Process Flow Analysis]]
8. [[#8. Work Study & Time-Motion]]
9. [[#9. Ergonomics]]
10. [[#10. Standard Operating Procedures]]
11. [[#11. Process Simulation]]
12. [[#12. Business Process Reengineering]]
13. [[#13. ⭐ Advanced: Lean Six Sigma DMAIC and Process Capability]]
14. [[#14. ⭐ Advanced: Queueing Theory and Service Process Design]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): process redesign at industrial scale
> **Amazon's warehouse flow redesign (Jul 2025).** Amazon announced its 1 millionth warehouse robot and **DeepFleet**, an AI model that coordinates robot traffic; reporting says it makes the fleet about **10% faster**, and about **75% of Amazon's global deliveries** involve robotic assistance. Cutting travel time and congestion inside a fulfilment centre is a pure process-flow problem: shorter paths, fewer queues, less waiting. ([TechCrunch](https://techcrunch.com/2025/07/01/amazon-deploys-its-1-millionth-robot-releases-generative-ai-model/))
> 
> **Maruti Suzuki Hansalpur (reported 30 Jul 2026).** Production started at Plant D of Maruti Suzuki's Hansalpur (Gujarat) facility, lifting its capacity from 750,000 to **1 million units a year**, India's largest single-location passenger-vehicle plant; Maruti's total capacity reaches **2.9 million units a year**, with cumulative investment at Hansalpur of about ₹25,288.7 crore. ([Evo India](https://www.evoindia.com/news/car-news/maruti-suzuki-hansalpur-reaches-1-million-capacity-587590))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Process Mapping & BPMN
> 🔴 Tier 1 · _Tracker hint:_ Swimlane diagrams, BPMN notation, as-is vs to-be

### Definition
A **process map** shows the steps, decisions, inputs/outputs and owners of a process. Common forms: **SIPOC** (Supplier, Input, Process, Output, Customer: a high-level scope map), **flowchart**, **swimlane (cross-functional) diagram** (rows = roles/departments, so hand-offs are visible), and **BPMN** (Business Process Model and Notation, an OMG standard).

BPMN core elements: **events** (circles: start, intermediate, end), **activities/tasks** (rounded rectangles), **gateways** (diamonds: exclusive XOR, parallel AND, inclusive OR), **sequence flows** (solid arrows), **message flows** (dashed, between pools), **pools and lanes**.

Method: **As-Is** map (how work really happens, built by walking the process), find pain points (delays, rework, hand-offs), design **To-Be** map, then implement and control.

### Example
Purchase-to-pay as-is: request raised on email, approvals by 3 managers in series, PO created manually, invoice matched manually. The swimlane shows 9 hand-offs between 4 departments. To-be: single e-requisition, parallel approvals above thresholds only, auto three-way match: hand-offs fall from 9 to 4.

### In the news
See news box. Amazon's fulfilment redesign starts with mapping the physical flow and its queues before optimising it.

### Interview angle
> [!question] How it is asked
> "How would you approach improving a process you know nothing about?"

> [!tip] Strong answer includes
> - Scope with SIPOC, then walk the process (gemba) to build the as-is map
> - Swimlanes to expose hand-offs and waiting
> - Measure time and defects at each step
> - Design to-be, pilot, standardise (SOP) and monitor

---

## 2. Value-Added vs Non-Value-Added
> 🔴 Tier 1 · _Tracker hint:_ Customer-defined value; waste identification

### Definition
An activity is **value-added (VA)** if the customer would pay for it, it changes the product/service form, fit or function, and it is done right the first time. **Non-value-added (NVA)** activities consume resources without adding value (waiting, rework, inspection, extra movement). **Necessary but non-value-added (NNVA / business-value-added)**: required by regulation or current technology (e.g., statutory documentation, safety checks).

Lean's **eight wastes (TIMWOODS):** Transport, Inventory, Motion, Waiting, Over-production, Over-processing, Defects, Skills (under-used talent).

$$\text{Process Cycle Efficiency (PCE)} = \frac{\text{Value-added time}}{\text{Total lead time}}$$
Un-improved office and job-shop processes often have PCE below 10%; a commonly quoted lean benchmark is 25% or more.

### Example
A loan approval takes 5 working days (40 working hours) end to end, but only 2 hours are actual assessment work. PCE $= 2/40 = 5\%$. Waiting in queues is 95% of the time, so the lever is queue removal, not working faster.

### In the news
See news box. Amazon's robots remove walking (motion/transport waste); Maruti's plants are designed for flow with minimal waiting.

### Interview angle
> [!question] How it is asked
> "Identify waste in this process" or "What is VA vs NVA?"

> [!tip] Strong answer includes
> - Customer-defined value
> - Three-way split: VA, NNVA, NVA
> - TIMWOODS naming with examples
> - PCE number and its implication

---

## 3. Bottleneck Identification
> 🔴 Tier 1 · _Tracker hint:_ Utilization-based identification; Theory of Constraints

### Definition
The **bottleneck** is the resource with the lowest effective capacity relative to demand (highest utilisation). It sets the throughput of the whole process: an hour lost at the bottleneck is an hour lost for the system, whereas an hour saved at a non-bottleneck is a mirage.

Identify it by: (i) highest utilisation ($\text{Demand} \times \text{processing time} / \text{available time}$); (ii) longest queue **in front of** it with idle stations after it; (iii) lowest capacity.

**Theory of Constraints (Goldratt)**, five focusing steps: **Identify** the constraint → **Exploit** it (squeeze max from it) → **Subordinate** everything else → **Elevate** it (add capacity) → **Repeat** (the constraint moves). See also [[018 Capacity Management & OEE]].

### Example
Line: A = 60 units/hr, B = 45/hr, C = 50/hr. Bottleneck = B; system throughput = 45/hr. Utilisation: A $=45/60 = 75\%$, C $=45/50 = 90\%$, B = 100%. Adding 5 units/hr to A achieves nothing; adding 5/hr to B lifts output to 50/hr (now limited by C).

### In the news
See news box. Plant expansion at Maruti is capacity added where the constraint (final assembly/paint) limits volume, and Amazon's DeepFleet targets traffic congestion as a throughput constraint.

### Interview angle
> [!question] How it is asked
> "Output is low although machines look busy. How do you find the problem?"

> [!tip] Strong answer includes
> - Utilisation and queue evidence for the bottleneck
> - Five focusing steps
> - Do not add capacity elsewhere; protect and keep the bottleneck running (no breaks, buffer in front)
> - Mention that the constraint moves after elevation

---

## 4. Throughput & Little's Law
> 🔴 Tier 1 · _Tracker hint:_ Throughput = WIP / Cycle Time; applications

### Definition
**Little's Law** (steady-state, any stable system):
$$WIP = TH \times CT \quad\Longleftrightarrow\quad TH = \frac{WIP}{CT}$$
where $WIP$ = average items in the system, $TH$ = throughput (items per unit time), $CT$ = average time an item spends in the system (flow time). It requires consistent units and long-run averages, and no assumption about distribution.

Applications: set WIP caps (CONWIP/kanban), estimate lead time from WIP and throughput, size queues (customers in a bank), hospital beds, ticket backlogs in IT. To cut lead time at the same throughput, **cut WIP**.

### Example
A plant has 60 jobs in process and ships 12 jobs/day. $CT = 60/12 = 5$ days. Reducing WIP to 36 with the same throughput gives $CT = 36/12 = 3$ days, a 40% drop in lead time. Another: a helpdesk holds 150 open tickets and closes 30/day, so average ticket age = 5 days.

### In the news
See news box. With a fleet-wide throughput gain of about 10%, the same WIP would mean about 9% shorter flow time (WIP fixed: $CT = WIP/TH$, $1/1.10 \approx 0.91$); this is an application of the law, not a reported figure.

### Interview angle
> [!question] How it is asked
> "Orders take 10 days to deliver and 200 are in progress. What is the throughput? How do you halve lead time?"

> [!tip] Strong answer includes
> - $TH = 200/10 = 20$ per day
> - Halve lead time by halving WIP (at same throughput) or increasing throughput
> - Assumptions: steady state, same units
> - Practical tools: WIP cap, kanban, bottleneck relief

---

## 5. Cycle Time Analysis
> 🔴 Tier 1 · _Tracker hint:_ Process vs lead time; reduction strategies

### Definition
Terms are used differently across firms, so define them:
- **Process (touch) time:** time actually working on the item.
- **Cycle time:** time between completion of successive units at a station (capacity view), or time to complete a unit at the process.
- **Lead time:** total elapsed time from order to delivery, including queues and waiting. 
- **Takt time** $= \dfrac{\text{Available time}}{\text{Customer demand}}$: the pace demanded by the customer.

**Process cycle efficiency** $= \text{value-added time}/\text{lead time}$. 

In a serial process, the **bottleneck cycle time** sets the output rate; a line with stations of 40, 55 and 50 seconds produces one unit every 55 seconds. Reduction levers: remove NVA steps, parallelise, balance, reduce setup, cut batch size, and eliminate queues.

### Example
Order-to-delivery lead time is 10 working days (80 hours) and touch time is 6 hours: PCE $= 6/80 = 7.5\%$. Takt: 450 minutes/shift and demand 225 units → takt = 2 min; if the bottleneck takes 2.5 min, shortfall is 20% (output 180 vs 225).

### In the news
See news box. A plant adding capacity (Hansalpur) is an attempt to bring cycle time below takt at higher volume.

### Interview angle
> [!question] How it is asked
> "How would you reduce cycle time in this process?"

> [!tip] Strong answer includes
> - Distinguish touch time, cycle time, lead time, takt
> - Measure first, find where time is spent
> - Levers: eliminate, combine, parallelise, automate
> - Confirm cycle time vs takt for the bottleneck

---

## 6. Lead Time Reduction
> 🔴 Tier 1 · _Tracker hint:_ Parallel activities, setup reduction, queue elimination

### Definition
Lead time $= \text{processing} + \text{setup} + \text{queue} + \text{move} + \text{inspection}$. In most plants **queue (waiting) is 80–90% of lead time**, so the best lever is flow, not speed of work.

Levers:
- **Parallel activities** (do tasks concurrently: simultaneous engineering, parallel approvals).
- **Setup reduction (SMED, Shigeo Shingo):** convert internal setup (machine stopped) to external (machine running); allows small batches.
- **Smaller batches / one-piece flow:** a batch of $n$ waits $(n-1)$ unit-times.
- **Queue elimination:** WIP caps, pull systems, level loading (Little's Law).
- Layout and cellular design to cut moves; first-time-right to avoid rework.

### Example
A process has 3 sequential stages with 1 min per unit each. If the whole batch of 100 moves stage by stage, the batch is complete at $3 \times 100 = 300$ min. With transfer batches of 10, stage 1 still takes 100 min, and the last transfer batch then needs $2 \times 10$ min more at stages 2 and 3, so the order completes at $100 + 20 = 120$ min. Lead time falls by 60%.

### In the news
See news box. Faster, more predictable flow inside the warehouse is how e-commerce shortens delivery promises.

### Interview angle
> [!question] How it is asked
> "A customer complains of long delivery times. How do you shorten them?"

> [!tip] Strong answer includes
> - Break lead time into components with data (value stream map)
> - Queue as the main culprit
> - SMED, small batches, parallelisation, pull
> - Quantified before/after

---

## 7. Process Flow Analysis
> 🔴 Tier 1 · _Tracker hint:_ Flow diagrams, spaghetti diagrams, simulation

### Definition
Process flow analysis studies how material, people and information move to find delay, distance and complexity. Tools:
- **Flow process chart** (ASME symbols: operation, transport, inspection, delay, storage) with time and distance per step.
- **Spaghetti diagram:** a floor-plan trace of an item's or person's path; reveals backtracking and distance. 
- **Value stream map (VSM):** includes information flow, inventory triangles, and a timeline of VA vs lead time.
- **Flow ratio / PCE** and capacity analysis at each step.
- **Simulation** for variability and "what if" (see sub-topic 11).

Output: ranked list of waste, to-be flow with shorter distances and fewer hand-offs.

### Example
A hospital pharmacy tech walks 1.8 km per shift between 6 locations, shown by a spaghetti diagram. Re-locating the two most visited cabinets next to the dispensing counter cuts walking to 0.7 km, a 61% reduction ($1 - 0.7/1.8 = 0.611$).

### In the news
See news box. DeepFleet-style optimisation is essentially an automated spaghetti-diagram fix: shortest conflict-free paths for robots.

### Interview angle
> [!question] How it is asked
> "How would you analyse the flow in a warehouse or an outpatient department?"

> [!tip] Strong answer includes
> - Observe and record: flow chart, spaghetti diagram, time study
> - Metrics: distance, hand-offs, waiting time, PCE
> - Redesign layout and sequence
> - Test via simulation or pilot

---

## 8. Work Study & Time-Motion
> 🔴 Tier 1 · _Tracker hint:_ Standard time, method study, work sampling, MTM

### Definition
**Work study** = **method study** (find the best way: record, examine, develop, install) + **work measurement** (find the time).

Standard time:
$$\text{Normal time} = \text{Observed time} \times \frac{\text{Rating}}{100}, \qquad \text{Standard time} = \text{Normal time} \times (1 + \text{Allowance})$$
Allowances: personal, fatigue, delay (typically 10–20% in total).

Techniques: **stopwatch time study**, **work sampling** (random observations to estimate % of time on activities; sample size $n = Z^2 p(1-p)/e^2$), **predetermined motion time systems** such as **MTM** (1 TMU = 0.00001 hour = 0.036 second) and MOST, and the **Gilbreth therbligs** for motion analysis.

### Example
Observed average 1.0 min, performance rating 110%, allowance 15%: normal time $= 1.0 \times 1.10 = 1.10$ min; standard time $= 1.10 \times 1.15 = 1.265$ min per unit. Work sampling: to estimate idle time near 30% within ±5% at 95% confidence, $n = 1.96^2 \times 0.3 \times 0.7 / 0.05^2 = 3.8416 \times 0.21 / 0.0025 \approx 323$ observations.

### In the news
See news box. Standard times and takt underpin the capacity planning of new plants like Hansalpur Plant D.

### Interview angle
> [!question] How it is asked
> "How would you set a labour standard for a new task?" or "Compute the standard time."

> [!tip] Strong answer includes
> - Distinguish normal and standard time
> - Method study before time study
> - Rating and allowances explained
> - Work sampling for non-repetitive work; MTM for new designs before the job exists

---

## 9. Ergonomics
> 🔴 Tier 1 · _Tracker hint:_ Workstation design, RULA/REBA assessment, fatigue reduction

### Definition
Ergonomics (human factors) fits work to the person to cut injury risk and fatigue and raise productivity and quality. Issues: posture, force, repetition, reach, lifting, vibration, lighting, noise, heat.

Assessment tools: **RULA** (Rapid Upper Limb Assessment, scores 1–7; 5+ needs investigation soon, 7 = change now), **REBA** (Rapid Entire Body Assessment, scores 1–15, higher = more risk), **NIOSH lifting equation** (recommended weight limit), OWAS. 

Design rules: work between knee and shoulder height, neutral wrist, reach within the **normal work area**, adjustable benches, anti-fatigue mats, lifting aids, job rotation. Benefits: fewer musculoskeletal disorders, lower absenteeism, less error.

### Example
An assembler lifts 12-kg boxes from floor level 80 times a shift: high REBA score. Fix: raise the pallet with a lift table to waist height and use a tilt stand: expected REBA falls from, say, 9 to 4 (illustrative), cutting bending and injury risk.

### In the news
See news box. Robots taking over heavy-travel and carrying tasks is partly an ergonomic and safety argument; cobots in assembly follow similar logic.

### Interview angle
> [!question] How it is asked
> "How would you improve productivity at a workstation without increasing workload?"

> [!tip] Strong answer includes
> - Observe posture, reach, force and repetition
> - RULA/REBA to quantify
> - Engineering fixes first (layout, tools), then admin (rotation)
> - Link to productivity, quality and safety KPIs

---

## 10. Standard Operating Procedures
> 🔴 Tier 1 · _Tracker hint:_ SOP writing, visual work instructions, one-point lessons

### Definition
A **Standard Operating Procedure (SOP)** documents the best-known way to do a task so that outcome is repeatable regardless of who does it. Good SOPs: define purpose and scope, roles, safety, step-by-step actions with key points and quality checks, tools and materials, and a revision/ownership record.

Formats: **visual work instructions** (photos, diagrams, colour codes: faster to read on the shop floor), **one-point lessons (OPL)** (one-page TPM/Lean lessons on a single topic), **checklists**, **job breakdown sheets** (TWI: steps, key points, reasons). SOPs are the baseline for **kaizen**: no standard, no improvement. Keep them short, owned by the operators, version-controlled and audited (also needed for ISO 9001/GMP).

### Example
An SOP for a changeover on a packing machine: 14 steps, each with a photo, a time target and a quality check; after training and standardising, changeover time falls from 45 to 30 minutes and first-pass errors fall (illustrative targets).

### In the news
See news box. Scaling a plant to a million units needs rigid standard work so that new lines reproduce established quality.

### Interview angle
> [!question] How it is asked
> "How do you make sure a process improvement sticks?"

> [!tip] Strong answer includes
> - Standardise: SOP/visual instructions created with the operators
> - Train and certify; audit regularly
> - Visual management and review cadence
> - Continuous improvement loop updates the standard

---

## 11. Process Simulation
> 🔴 Tier 1 · _Tracker hint:_ Arena, Simul8, FlexSim basics; Monte Carlo in process design

### Definition
Simulation builds a computer model of a process to test changes without disturbing the real system, particularly when **variability and queues** make spreadsheets misleading. **Discrete-event simulation (DES):** entities (jobs/patients) flow through resources and queues, with random arrival and service times. Tools: **Arena, Simul8, FlexSim**, AnyLogic.

Steps: define the question, collect data, fit distributions (e.g., exponential interarrival), build and **validate** the model, run many **replications**, compare scenarios with confidence intervals.

**Monte Carlo simulation** samples random inputs repeatedly to get a distribution of outcomes (e.g., project completion time or demand during lead time).

Queueing benchmark (M/M/1): utilisation $\rho = \lambda/\mu$; average wait in queue $W_q = \dfrac{\rho}{\mu - \lambda}$. Waiting explodes as $\rho \to 1$.

### Example
M/M/1 counter: arrivals 9 per hour, service 10 per hour, $\rho = 0.9$, $W_q = 0.9/(10-9) = 0.9$ hr = 54 min. At 8 arrivals/hr: $\rho = 0.8$, $W_q = 0.8/2 = 0.4$ hr = 24 min. A 10% drop in load more than halves the wait.

### In the news
See news box. Large fleet coordination like DeepFleet and plant ramp-ups are typically tested in simulation before rollout (the typical industry practice; the sources do not describe the method).

### Interview angle
> [!question] How it is asked
> "When would you use simulation instead of a spreadsheet?"

> [!tip] Strong answer includes
> - Variability, queues, interdependence
> - DES vs Monte Carlo
> - Validation, replications, scenario comparison
> - The nonlinear effect of utilisation on waiting

---

## 12. Business Process Reengineering
> 🔴 Tier 1 · _Tracker hint:_ Radical redesign vs incremental; Hammer & Champy

### Definition
**BPR** (Hammer & Champy, *Reengineering the Corporation*, 1993) is "the fundamental rethinking and **radical redesign** of business processes to achieve **dramatic** improvements in cost, quality, service and speed". It starts from a clean sheet ("if we were starting today, how would we do this?"), is process-centred (end-to-end, not departmental), and usually uses IT as an enabler.

| | Kaizen (incremental) | BPR (radical) |
|---|---|---|
| Change | Small, continuous | Big, one-time |
| Risk | Low | High (many BPR projects failed) |
| Involvement | Everyone | Top-down, cross-functional |
| Gain | Small steps, cumulative | Step change (large targets) |

Principles: organise around outcomes not tasks; let those who use the output do the work; capture information once at source; treat dispersed resources as centralised. Failure causes: no top-management support, ignoring people, poor scope, cost-cutting disguised as BPR.

### Example
Ford's accounts payable (a classic case from Hammer): matching PO, receiving document and invoice by clerks replaced by "invoiceless processing" — pay on receipt of goods against the PO — cutting accounts-payable headcount drastically.

### In the news
See news box. Moving from picker-walks-to-shelf to robot-brings-shelf is a BPR-type redesign of the fulfilment process rather than a tweak.

### Interview angle
> [!question] How it is asked
> "When would you choose reengineering over continuous improvement?"

> [!tip] Strong answer includes
> - Radical vs incremental trade-off
> - Use BPR when the process is fundamentally broken or technology enables a step change
> - Change-management and risk
> - Combine: BPR to redesign, kaizen to sustain

---

## 13. ⭐ Advanced: Lean Six Sigma DMAIC and Process Capability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**DMAIC** structures data-driven improvement: **Define** (problem, scope, CTQs) → **Measure** (baseline, MSA) → **Analyse** (root causes: fishbone, 5 Whys, Pareto, regression) → **Improve** (solutions, pilot) → **Control** (SOPs, control charts, ownership).

**Process capability** compares process spread to specification limits:
$$C_p = \frac{USL - LSL}{6\sigma}, \qquad C_{pk} = \min\!\left(\frac{USL-\mu}{3\sigma},\ \frac{\mu - LSL}{3\sigma}\right)$$
$C_{pk} \ge 1.33$ is a common target. **Sigma level** relates to defects per million opportunities (DPMO): 6σ ≈ 3.4 DPMO (with the usual 1.5σ shift), 3σ ≈ 66,807.

### Example
Spec 10.0 ± 0.3 mm, so USL = 10.3, LSL = 9.7; process mean 10.05, σ = 0.08. $C_p = 0.6/0.48 = 1.25$. $C_{pk} = \min\big((10.3-10.05)/0.24,\ (10.05-9.7)/0.24\big) = \min(1.04,\ 1.46) = 1.04$. The process is off-centre; centring it lifts $C_{pk}$ toward 1.25.

### In the news
See news box. Plant ramp-ups need capable processes ($C_{pk}$) so that quality holds at 1 million units a year.

### Interview angle
> [!question] How it is asked
> "Walk me through a DMAIC project" or "What is Cpk?"

> [!tip] Strong answer includes
> - Phases with a tool for each
> - Cp vs Cpk (centring)
> - A data-based example with numbers
> - Control phase: how gains are sustained

---

## 14. ⭐ Advanced: Queueing Theory and Service Process Design
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Service processes (banks, hospitals, call centres, branches) have random arrivals and service, so queues form even when average capacity exceeds demand. Core models use Kendall notation **A/S/c** (arrival/service/servers). For **M/M/1**: $\rho = \lambda/\mu$, $L_q = \dfrac{\rho^2}{1-\rho}$, $W_q = \dfrac{\rho}{\mu-\lambda}$, and by Little's Law $L_q = \lambda W_q$.

Design levers: add servers, **pool** queues into one line (reduces average wait), reduce service variability (standardise), triage/segment (express lanes), manage arrivals (appointments), and cap utilisation to leave slack (typically 70–85%).

### Example
$\lambda = 9/\text{hr}$, $\mu = 10/\text{hr}$: $\rho = 0.9$, $L_q = 0.81/0.1 = 8.1$ customers waiting; $W_q = 0.9$ hr, and $L_q = \lambda W_q = 9 \times 0.9 = 8.1$ ✓. Raising $\mu$ to 12 (faster service): $\rho = 0.75$, $L_q = 0.5625/0.25 = 2.25$.

### In the news
See news box. Robot congestion in warehouses is a queueing problem: AI traffic control is a way to cut waiting for shared aisles.

### Interview angle
> [!question] How it is asked
> "A bank branch has long queues though tellers are idle part of the day. Why, and what would you do?"

> [!tip] Strong answer includes
> - Randomness plus high utilisation means long queues
> - Nonlinearity of waiting versus utilisation
> - Pooling, scheduling, staggering shifts to match arrivals
> - Measure: arrival pattern by hour, service-time distribution

---
## 🔗 Go deeper: expansion notes
- [[149 Queueing Theory & Waiting-Line Analysis|Queueing Theory & Waiting-Line Analysis]]
- [[152 Learning Curves, Work Measurement & Productivity|Learning Curves, Work Measurement & Productivity]]
- [[173 Process Mining & Operations Intelligence|Process Mining & Operations Intelligence]]
