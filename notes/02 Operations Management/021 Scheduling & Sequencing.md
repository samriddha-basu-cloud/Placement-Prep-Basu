---
tags: [operations-management, tier1]
area: Operations Management
topic: "Scheduling & Sequencing"
tier: Tier 1
roles: Operations
status: complete
subtopics: 12
---
# Scheduling & Sequencing

⬅ [[020 Operations Strategy]] · [[_Index - Operations Management|Operations Management]] · [[022 Maintenance Management (TPM-RCM)]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Forward vs Backward Scheduling]]
2. [[#2. Priority Dispatching Rules]]
3. [[#3. Johnson's Algorithm]]
4. [[#4. Gantt Charts]]
5. [[#5. Single Machine Scheduling]]
6. [[#6. Flow Shop Scheduling]]
7. [[#7. Job Shop Scheduling]]
8. [[#8. Advanced Planning & Scheduling (APS)]]
9. [[#9. Constraint-Based Scheduling]]
10. [[#10. Workforce Scheduling]]
11. [[#11. ⭐ Advanced: Moore-Hodgson, Weighted Rules and Why Many Problems Are NP-Hard]]
12. [[#12. ⭐ Advanced: Robust Scheduling and Disruption Recovery]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): IndiGo's December 2025 rostering meltdown
> **IndiGo scheduling crisis (2–9 Dec 2025).** New DGCA Flight Duty Time Limitation (FDTL) norms, phased in from July 2025, cut permitted night landings per crew from six to two per week. IndiGo, which held about **64.2% of India's domestic market in Aug 2025**, had built a rotation-and-roster plan around high pilot utilisation. Result: roughly **4,500 flights cancelled over ten days**, a peak of about **1,600 cancellations on 5 Dec**, and over **10 lakh passengers affected**. DGCA fined IndiGo **₹22.2 crore** (its highest ever), asked for a **₹50 crore** bank guarantee, ordered a **10% flight cut**, and granted temporary FDTL exemptions to 10 Feb 2026. ([Wikipedia summary](https://en.wikipedia.org/wiki/2025_IndiGo_scheduling_crisis))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Forward vs Backward Scheduling
> 🔴 Tier 1 · _Tracker hint:_ From current date vs from due date; applications

### Definition
**Forward scheduling** starts from the *release date* (today or material availability) and schedules each operation as early as possible, producing the **earliest completion date**. **Backward scheduling** starts from the *due date* and works back, placing each operation as late as possible, producing the **latest start date**.

| | Forward | Backward |
|---|---|---|
| Start point | Today / release date | Customer due date |
| Output | Earliest finish | Latest start |
| Inventory/WIP | Higher (work waits finished) | Lower (just-in-time) |
| Risk | Early finish, holding cost | No slack: any delay makes the job late |
| Typical use | Make-to-stock, job shops quoting a promise date | Make-to-order, JIT, MRP lead-time offsetting |

**Slack** = latest start − earliest start = due date − (release date + total processing time + queue/move time). Positive slack means the job can be delayed without lateness; negative slack means the due date is infeasible. MRP uses backward scheduling for planned order release; **Available-to-Promise** quoting uses forward scheduling. Finite-capacity tools often combine both: backward to find the ideal start, forward if capacity forces a later start.

### Example
A job has 3 operations of 5, 4 and 3 days (12 days total, ignoring queues). Due date is day 20; today is day 0.
- Forward: finishes day 0 + 12 = **day 12**, 8 days early (8 days of slack, plus finished-goods holding).
- Backward: latest start = 20 − 12 = **day 8**; operation 3 runs day 17–20, operation 2 day 13–17, operation 1 day 8–13.
If today were day 10 instead, backward scheduling would give a latest start of day 8 (already passed), so slack = −2 days: the job needs expediting or a revised promise date.

### In the news
See news box. IndiGo's rosters were effectively scheduled to the legal limit with almost no slack; when the rule changed, there was no buffer to absorb it. Backward-scheduled, zero-slack plans fail abruptly.

### Interview angle
> [!question] How it is asked
> "A customer wants delivery in 3 weeks. How do you decide when to start production?" or "Forward or backward scheduling: which would you use and why?"

> [!tip] Strong answer includes
> - Define both and state which result each gives (earliest finish vs latest start)
> - Slack calculation and what negative slack triggers (expedite, overtime, renegotiate date)
> - Trade-off: backward cuts inventory but is fragile; add a time buffer
> - Name where each is used: MRP offsetting (backward), order promising (forward)

---

## 2. Priority Dispatching Rules
> 🔴 Tier 1 · _Tracker hint:_ FCFS, SPT (minimize avg completion), LPT, EDD (minimize lateness), CR

### Definition
When several jobs wait at a work centre, a **dispatching rule** picks the next one. Notation: $p_j$ processing time, $d_j$ due date, $C_j$ completion time, $L_j = C_j - d_j$ lateness, $T_j=\max(0,L_j)$ tardiness.

| Rule | Sequence by | Best at |
|---|---|---|
| **FCFS** | Arrival time | Perceived fairness; poor on all metrics |
| **SPT** | Smallest $p_j$ first | Minimises mean flow time / mean completion time, and WIP; starves long jobs |
| **LPT** | Largest $p_j$ first | Balances load on parallel machines (minimises makespan heuristically) |
| **EDD** | Earliest $d_j$ | Minimises **maximum lateness** $L_{max}$ on one machine |
| **Slack (STR)** | $d_j - t - $ remaining time | Urgency |
| **Critical Ratio** | $CR = \dfrac{d_j - t}{\text{remaining processing time}}$ | CR < 1 behind schedule, CR = 1 on time, CR > 1 ahead; sort ascending |

SPT and EDD are provably optimal for their single-machine metrics; no rule is best on everything, and SPT's drawback is long-job starvation (use aging or a cap).

### Example
Four jobs (hours, due date): A (3, due 6), B (5, due 12), C (2, due 4), D (6, due 15).
- FCFS A-B-C-D: completions 3, 8, 10, 16; mean = 37/4 = **9.25**.
- SPT C-A-B-D: completions 2, 5, 10, 16; mean = 33/4 = **8.25**.
- LPT D-B-A-C: 6, 11, 14, 16; mean = 47/4 = 11.75.
- EDD (due 4, 6, 12, 15 gives C-A-B-D, same as SPT): lateness −2, −1, −2, +1, so $L_{max}=1$, one tardy job.
CR check: at day 3, job B has 12−3 = 9 days left and 5 hours of work: CR = 9/5 = 1.8 (comfortable).

### In the news
See news box. Crew pairing was the "dispatch" problem in IndiGo's crisis: with too few legal pilots, deciding which flights to cancel is a priority rule (protect long-haul, protect high-load routes, protect the earliest-due connections).

### Interview angle
> [!question] How it is asked
> "Which sequencing rule would you use in a job shop and why?" or a small numeric: "Sequence these 5 jobs to minimise average completion time."

> [!tip] Strong answer includes
> - SPT for mean flow time, EDD for max lateness, CR for dynamic urgency; say what each optimises
> - Do the arithmetic cleanly in a table (job, p, C, due, lateness)
> - Weakness of SPT (starvation) and fix
> - Say that in practice you combine rules and respect customer priority/changeover

---

## 3. Johnson's Algorithm
> 🔴 Tier 1 · _Tracker hint:_ Two-machine flow shop; minimize makespan

### Definition
Johnson's rule (1954) gives the **optimal permutation sequence** minimising makespan $C_{max}$ for $n$ jobs through **two machines in series** ($F2||C_{max}$); all jobs go M1 then M2.

**Steps**
1. List processing times $(a_j, b_j)$ on M1 and M2.
2. Find the smallest time among all entries.
3. If it is on **M1**, place that job as early as possible (next free slot from the front); if on **M2**, place it as late as possible (next free slot from the back).
4. Remove the job; repeat. Ties may be broken arbitrarily.

Equivalent form: jobs with $a_j \le b_j$ go first in ascending $a_j$; the rest go last in descending $b_j$.

Makespan = time M2 finishes the last job. Lower bound: $\max(\sum a_j + \min b_j,\ \min a_j + \sum b_j)$. It extends to 3 machines only when M2 is dominated ($\min a \ge \max b$ or $\min c \ge \max b$), by treating $(a+b,\ b+c)$ as two virtual machines.

### Example
Jobs (M1, M2): A (4, 5), B (4, 1), C (10, 4), D (6, 10), E (2, 3).
Smallest is 1 (B on M2) → B last. Then 2 (E on M1) → E first. Then 4 (A on M1, tie with C on M2) → A second. Then C on M2 (4) → C fourth. D is left in the middle.
Sequence: **E-A-D-C-B**.
- M1: E 0–2, A 2–6, D 6–12, C 12–22, B 22–26.
- M2: E 2–5, A 6–11, D 12–22, C 22–26, B 26–27.
Makespan = **27**. Lower bound = ΣM1 + min M2 = 26 + 1 = 27, so it is optimal.

### In the news
See news box. Johnson's rule is for a clean two-stage line; the IndiGo case is a far more constrained problem (crew pairing, aircraft rotation, rest rules), but the lesson is the same: the sequence and the constraints, not just total capacity, set the output.

### Interview angle
> [!question] How it is asked
> "Given these 5 jobs on two machines, find the sequence that minimises total time and compute the makespan."

> [!tip] Strong answer includes
> - State the rule, build the sequence step by step
> - Draw the Gantt (or timetable) and read the makespan, including idle time on M2
> - Sanity-check using the lower bound
> - Note the limits: 2 machines (or special 3-machine case), same job order on both

---

## 4. Gantt Charts
> 🔴 Tier 1 · _Tracker hint:_ Activity vs machine Gantt; manual and MS Project

### Definition
A **Gantt chart** plots time on the x-axis and tasks or resources on the y-axis, with bars showing start, duration and finish.
- **Activity (project) Gantt:** one row per task, with dependencies (finish-to-start, start-to-start, etc.), milestones and the critical path. Used in project management.
- **Machine (load/schedule) Gantt:** one row per machine or work centre, bars are jobs. Used in production scheduling to see sequence, idle time, overlap and **utilisation** = busy time / available time.

**Building one manually:** list tasks and durations, set dependencies, place bars at earliest start, mark the critical path, then add resource levelling. **In MS Project:** enter tasks, durations and predecessors; set task type (fixed duration/work/units), calendars and resources; use *Resource Usage* and *Level Resources* to remove overloads; set a **baseline** and track % complete. The critical path is shown by Format > Critical Tasks.

Limits: Gantt charts do not show uncertainty or optimise a schedule; they communicate one.

### Example
Two machines, three jobs: M1 runs J1 (0–4), J2 (4–7), J3 (7–10); M2 runs J1 (4–9), J2 (9–11), J3 (11–15). Horizon 15 hours. M1 utilisation = 10/15 = 66.7%; M2 busy = 5 + 2 + 4 = 11 hours, utilisation 11/15 = 73.3% (idle 0–4). The chart immediately shows M2 waiting 4 hours at the start, which a table hides.

### In the news
See news box. During the IndiGo crisis, rosters and aircraft rotations were effectively Gantt views of crew and tail-number time; the visual gaps (a crew timed out, a plane without crew) were the cancellations.

### Interview angle
> [!question] How it is asked
> "How would you track the plan for a 6-month plant commissioning?" or "Draw the schedule for these jobs and show where the bottleneck is."

> [!tip] Strong answer includes
> - Distinguish project vs machine Gantt
> - Dependencies, critical path, baseline vs actual
> - Resource levelling and utilisation reading
> - Honest limits (static; pair with CPM/PERT for uncertainty)

---

## 5. Single Machine Scheduling
> 🔴 Tier 1 · _Tracker hint:_ Performance metrics: Cmax, Lmax, ΣCj, ΣTj

### Definition
One machine, $n$ jobs, no preemption. Standard objectives and the rule that solves each:

| Metric | Meaning | Optimal / good rule |
|---|---|---|
| $C_{max}$ (makespan) | Time last job finishes | Same for any sequence if no setups/release dates ($=\sum p_j$) |
| $\sum C_j$ | Total (mean) completion time | **SPT** |
| $\sum w_jC_j$ | Weighted completion | **WSPT**: ascending $p_j/w_j$ |
| $L_{max}$ | Maximum lateness | **EDD** (Jackson's rule) |
| $\sum U_j$ | Number of tardy jobs | **Moore-Hodgson** algorithm |
| $\sum T_j$ | Total tardiness | NP-hard (weakly); heuristics, DP, SPT/EDD bounds |

Lateness can be negative, tardiness cannot: $T_j=\max(0,C_j-d_j)$. Optimising total tardiness and many due-date metrics with release dates or setups is **NP-hard**, which is why industry uses heuristics and solvers.

### Example
Jobs (p, due): J1 (4, 5), J2 (2, 3), J3 (6, 12).
EDD order J2-J1-J3: C = 2, 6, 12; L = −1, +1, 0; $L_{max}=1$; T = 0, 1, 0, so $\sum T_j=1$; $\sum C_j=20$; $C_{max}=12$.
SPT order is the same here (2, 4, 6), so one sequence is optimal for both. If J3 had due date 11, EDD order stays J2-J1-J3 and J3 is 1 late (T=1) as well; $\sum T_j=2$.

### In the news
See news box. A ground-handling or cleaning crew at an airport gate is a single-resource sequencing problem; when cancellations pile up, minimising total tardiness (not average completion) protects passenger experience.

### Interview angle
> [!question] How it is asked
> "Which rule minimises average completion time? Maximum lateness? Number of late jobs?"

> [!tip] Strong answer includes
> - Match metric to rule: SPT, EDD, Moore-Hodgson, WSPT
> - Define lateness vs tardiness
> - Compute a small example
> - Mention that total tardiness is NP-hard so heuristics are used in practice

---

## 6. Flow Shop Scheduling
> 🔴 Tier 1 · _Tracker hint:_ n-jobs, m-machines; heuristics (NEH algorithm)

### Definition
A **flow shop** has $m$ machines in series and every job visits them in the same order. In a **permutation flow shop** the job order is the same on all machines, giving $n!$ candidate sequences; minimising makespan for $m\ge3$ is **NP-hard**. Bottleneck machine sets throughput.

Heuristics: **CDS** (Campbell-Dudek-Smith, builds $m-1$ virtual two-machine problems and applies Johnson), **Palmer's slope index**, and the **NEH** algorithm (Nawaz-Enscore-Ham, 1983), widely regarded as the best constructive heuristic:
1. Compute total processing time of each job; sort jobs in **descending** total time.
2. Take the first two jobs, try both orders, keep the better makespan.
3. For each next job in the list, insert it in every possible position of the current partial sequence; keep the position with the lowest makespan.
4. Repeat until all jobs are placed.
Complexity about $O(n^2 m)$ with Taillard's speed-up. Metaheuristics (iterated greedy, genetic algorithms) improve further.

### Example
Two machines, jobs J1 (4, 5), J2 (6, 2), J3 (3, 3). Totals: 9, 8, 6, so list J1, J2, J3.
- J2-J1: M1 0–6, 6–10; M2 J2 6–8, J1 10–15 → 15. J1-J2: M1 0–4, 4–10; M2 J1 4–9, J2 10–12 → **12**. Keep J1-J2.
- Insert J3: J3-J1-J2 gives 15; J1-J3-J2 gives 15; J1-J2-J3 gives 16. Best = **15** (J3-J1-J2).
Johnson's rule also gives 15 here, so NEH matched the optimum.

### In the news
See news box. A multi-stage line is only as fast as its constraint; IndiGo's constrained resource was legally available crew hours, not aircraft.

### Interview angle
> [!question] How it is asked
> "How would you schedule 20 jobs through a 5-stage line?" (open-ended, expects heuristics) or "Explain NEH."

> [!tip] Strong answer includes
> - Permutation flow shop, $n!$ growth, NP-hard
> - NEH steps in one breath
> - Practical drivers: bottleneck, setups, buffers/blocking
> - Mention solvers/metaheuristics and when a simple rule is enough

---

## 7. Job Shop Scheduling
> 🔴 Tier 1 · _Tracker hint:_ Complexity; shifting bottleneck; simulation-based

### Definition
In a **job shop** each job has its own routing across machines (possibly revisiting some). The number of operation sequences is $(n!)^m$ for $n$ jobs and $m$ machines: 10 jobs on 10 machines gives about $(3.6\times10^6)^{10}\approx4\times10^{65}$. Minimising makespan ($J||C_{max}$) is **strongly NP-hard** (the classic 10x10 benchmark known as MT10 resisted exact solution for decades).

Approaches:
- **Dispatching rules** inside a simulation (SPT, EDD, CR, FOR/MWKR) and **discrete-event simulation** to compare them under variability.
- **Disjunctive graph** model: nodes = operations, conjunctive arcs = routing, disjunctive arcs = machine conflicts; choose orientation to minimise the longest path.
- **Shifting Bottleneck Procedure** (Adams, Balas, Zawack 1988): solve single-machine problems, pick the machine that is the worst bottleneck, fix its sequence, re-optimise earlier machines, repeat.
- **Constraint programming, MILP, tabu search, genetic algorithms** for modern solvers.
Practical complexity drivers: sequence-dependent setups, rework, breakdowns, material availability.

### Example
A tool-room with 6 jobs and 4 machines: the number of sequences is $(6!)^4 = 720^4 \approx 2.7\times10^{11}$. Enumeration is impossible; a planner simulates SPT, EDD and CR, compares mean tardiness and WIP, and picks the best, perhaps with a bottleneck-first override on the heat-treatment furnace.

### In the news
See news box. IndiGo's network (hundreds of aircraft, thousands of daily flights, each crew with a different duty pattern) is a job shop at massive scale; small rule changes (night landings 6 to 2) ripple through every pairing, which is why simple patches failed.

### Interview angle
> [!question] How it is asked
> "Why is job shop scheduling so hard? How do real plants schedule it?"

> [!tip] Strong answer includes
> - Combinatorial explosion with the $(n!)^m$ number
> - Dispatching rules + simulation as the pragmatic route
> - Shifting bottleneck idea (schedule the constraint first)
> - Real constraints: setups, maintenance, material, operator skills

---

## 8. Advanced Planning & Scheduling (APS)
> 🔴 Tier 1 · _Tracker hint:_ APS software; finite capacity scheduling; SAP APO

### Definition
**APS** software plans and schedules production and supply **simultaneously considering material and capacity constraints**, in contrast to classic MRP II, which assumes **infinite capacity** and fixed lead times. Modules: demand planning, supply network planning, production planning/detailed scheduling (PP/DS), available-to-promise, and transport planning.

**Finite capacity scheduling (FCS):** loads work to a resource only up to its available capacity, reports load vs capacity, and moves or splits jobs; it uses optimisation (LP/heuristics/constraint programming) and rules. Key benefits: realistic promise dates, fewer expedites, shorter lead times, what-if simulation.

Capacity load check: $\text{Load \%} = \dfrac{\text{scheduled hours}}{\text{available hours}}\times100$. Vendors: **SAP APO** (legacy; SAP now steers customers to **SAP IBP** and PP/DS in S/4HANA), Oracle, **Kinaxis RapidResponse**, **o9 Solutions**, Siemens Opcenter APS, Preactor.

### Example
MRP plans 120 hours of work on a machine for a week with 80 available hours (two shifts × 5 days × 8 h): load = 120/80 = **150%**; MRP releases it anyway, causing backlog. An APS shows the overload, shifts 25 h to an alternate machine, adds 15 h of overtime on the third shift, and defers 10 h to next week, giving credible dates.

### In the news
See news box. Airlines rely on crew-optimisation systems (APS analogues). The IndiGo crisis shows even an optimised plan is only as good as the constraints encoded: the rule change effectively invalidated the model's assumptions.

### Interview angle
> [!question] How it is asked
> "Why is MRP not enough? What does APS add?" or "Would you invest in an APS system for this plant?"

> [!tip] Strong answer includes
> - Infinite vs finite capacity distinction
> - Modules and data needed (accurate BOM, routings, capacity, master data)
> - Benefits quantified (promise-date reliability, WIP, OTIF)
> - Cautions: data quality, change management, link to S&OP

---

## 9. Constraint-Based Scheduling
> 🔴 Tier 1 · _Tracker hint:_ Theory of Constraints; drum-buffer-rope scheduling

### Definition
**Theory of Constraints** (Goldratt, *The Goal*, 1984): every system has one dominant constraint that limits throughput; improving non-constraints is an illusion. Five focusing steps: **Identify, Exploit, Subordinate, Elevate, Repeat**.

**Drum-Buffer-Rope (DBR)** is TOC's scheduling method:
- **Drum:** the bottleneck's schedule, which sets the pace of the plant.
- **Buffer:** a *time buffer* ahead of the constraint (and shipping) so it never starves; typically sized as a fraction of lead time, then tuned by buffer management (green/yellow/red zones).
- **Rope:** a release signal tying raw-material release to the drum's pace, preventing excess WIP.

A hour lost at the bottleneck is an hour lost for the whole system; an hour saved at a non-bottleneck is a mirage. **Constraint programming** (CP) is a separate but related term: scheduling as variables + constraints solved by CP solvers.

### Example
Line: cutting 80 units/h, welding 50 units/h, painting 70 units/h. Welding is the constraint. Plant output = 50 × 16 h = **800 units/day**. Releasing material at 80/h would build 30 units of WIP per hour before welding (480 per 16-hour day) with no extra output. DBR releases at 50/h, holds a 2-hour time buffer before welding, and cuts WIP. Adding 10% capacity to painting adds nothing; a 10% gain at welding (55/h) adds 80 units/day.

### In the news
See news box. IndiGo's binding constraint was legal pilot hours at night; adding aircraft or schedule would not have helped. A TOC reading says protect and plan around the constraint first, then subordinate the rest.

### Interview angle
> [!question] How it is asked
> "Your plant has idle machines but orders are late. What is happening?" (looking for the constraint)

> [!tip] Strong answer includes
> - Identify the bottleneck from utilisation/queue data
> - Five steps; exploit before elevating (cheap before capex)
> - DBR explained simply
> - Throughput accounting mindset (throughput, inventory, operating expense)

---

## 10. Workforce Scheduling
> 🔴 Tier 1 · _Tracker hint:_ Shift planning, rostering, skill matching, labor laws

### Definition
**Workforce scheduling** assigns people to shifts and tasks to meet demand at minimum cost, respecting skills, preferences and **labour rules**. Stages: forecast demand per interval, compute requirements, build **shift patterns**, produce **rosters** (who works when), then daily adjustment.

Staffing arithmetic: required headcount per shift = (workload ÷ productive hours per person) ÷ (1 − shrinkage), where shrinkage covers leave, absence, training. Call-centre style demand uses **Erlang C** for staffing to a service level. Approaches: heuristics, set-covering integer programs, and **cyclic rosters** (rotating patterns). Skill matching ensures each shift has the required certification mix.

Constraints in India: the **Factories Act 1948** limits adult workers to 48 hours per week and 9 hours per day, with overtime paid at double the ordinary rate and mandatory weekly rest; state Shops and Establishments Acts, and the new labour codes, add rules, so always confirm current norms. In aviation, FDTL rules cap duty and flight hours and mandate rest.

### Example
A warehouse needs 12 pickers on duty at peak, 7 days a week, and each person works 6 days. Coverage headcount = 12 × 7 / 6 = 14. With 25% shrinkage (leave, absence), staff to roster = 14 ÷ (1 − 0.25) ≈ 18.7, so about **19 people**. (Ignoring the rest-day rule, shrinkage alone would give 12 ÷ 0.75 = 16.) Always state the assumptions.

### In the news
See news box. The IndiGo crisis is the textbook Indian workforce-scheduling failure: regulation changed rest and night-landing limits, yet the roster and pilot pool were not resized in time.

### Interview angle
> [!question] How it is asked
> "How would you plan shifts for a 24x7 hub with variable demand?" or "How many people do we need?"

> [!tip] Strong answer includes
> - Demand forecast by interval, then headcount formula with shrinkage
> - Legal limits and fatigue risk; fairness and preferences
> - Buffer capacity (reserve crew, cross-training, flexible staff)
> - Plan for rule changes: compliance lead time

---

## 11. ⭐ Advanced: Moore-Hodgson, Weighted Rules and Why Many Problems Are NP-Hard
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Moore-Hodgson** minimises the **number of tardy jobs** ($1||\sum U_j$): sequence by EDD; the first time a job becomes late, remove the job with the largest processing time among those scheduled so far (including the late one) and put it at the end; continue. **WSPT** (Smith's rule) minimises $\sum w_jC_j$ by ordering by $p_j/w_j$ ascending. Problems like $1||\sum T_j$, $J||C_{max}$ and $F_m||C_{max}$ ($m\ge3$) are NP-hard: no known polynomial algorithm, so interviewers expect "heuristic + bound" answers, not brute force.

### Example
Jobs (p, due): A (4, 4), B (3, 5), C (2, 6), D (5, 11). EDD: A done at 4 (on time), B at 7 (due 5: late). Remove the longest among A, B: A (4). Remaining sequence B, C, D: B 3 (due 5 ok), C 5 (ok), D 10 (due 11 ok); A goes last at 14, late. Number tardy = 1 (minimum possible). WSPT check: p/w for job (p=4, w=2) is 2 and for (p=3, w=1) is 3, so the first goes first.

### In the news
See news box. Airlines minimise *cancelled or late flights* weighted by passengers affected (a weighted-tardiness objective), which is why recovery planners prioritise flights by load and connections.

### Interview angle
> [!question] How it is asked
> "Which sequence gives the fewest late orders?" or "Why not just check every sequence?"

> [!tip] Strong answer includes
> - Name the algorithm for the objective
> - Show the arithmetic
> - Explain the combinatorial explosion in one line ($20!\approx2.4\times10^{18}$)

---

## 12. ⭐ Advanced: Robust Scheduling and Disruption Recovery
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Real schedules break. **Predictive-reactive scheduling** builds a baseline and reschedules on events (breakdown, rush order, absence). **Robust scheduling** inserts slack or buffer where disruptions are likely, trading a little efficiency for stability. Metrics: **schedule stability** (changes versus baseline), **schedule robustness** (tolerance to variation) and **schedule efficiency**. Policies: *rolling horizon* (re-plan every shift or day with a frozen window), *right-shift* (delay everything), *match-up* (rejoin the original plan at a defined point), and *reserve capacity* (spare crew, standby aircraft). In airlines, recovery orders: aircraft first, then crew, then passengers.

### Example
A plant with 95% planned utilisation and random breakdowns has queues growing without limit; lowering planned utilisation to 85% by adding a 10% time buffer cuts expected queueing delay sharply (in an M/M/1 view, waiting time scales with $\rho/(1-\rho)$: 0.95/0.05 = 19 vs 0.85/0.15 = 5.7, about 70% lower).

### In the news
See news box. IndiGo ran lean on crew buffer; the penalty (₹22.2 crore fine, mandated 10% cut, mass cancellations) far exceeded the cost of a standby pool.

### Interview angle
> [!question] How it is asked
> "How would you make this schedule resilient to disruption?"

> [!tip] Strong answer includes
> - Buffer placement at the bottleneck and critical resources
> - Rolling horizon with a frozen window
> - Cost of slack vs cost of failure, quantified
> - Monitoring: schedule adherence and re-plan frequency

---
## 🔗 Go deeper: expansion notes
- [[148 Operations Research - Network Models & Integer Programming|Operations Research - Network Models & Integer Programming]]
- [[150 Decision Analysis & Simulation|Decision Analysis & Simulation]]
