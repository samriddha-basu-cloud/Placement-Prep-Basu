---
tags: [project-management, tier1]
area: Project Management
topic: "Scheduling Tools (CPM/PERT/Gantt)"
tier: Tier 1
roles: Project Mgmt
status: complete
subtopics: 12
---
# Scheduling Tools (CPM/PERT/Gantt)

⬅ [[038 PMBOK Knowledge Areas]] · [[_Index - Project Management|Project Management]] · [[040 Risk & Stakeholder Management]] ➡

> **Area:** Project Management · **Priority:** 🔴 Tier 1 · **Target roles:** Project Mgmt

## Sub-topics in this note
1. [[#1. Gantt Chart]]
2. [[#2. Critical Path Method (CPM)]]
3. [[#3. Network Diagram (AON/AOA)]]
4. [[#4. PERT (Program Evaluation Review Technique)]]
5. [[#5. Forward & Backward Pass]]
6. [[#6. Resource Leveling]]
7. [[#7. Resource Smoothing]]
8. [[#8. Fast Tracking]]
9. [[#9. Crashing]]
10. [[#10. Schedule Compression]]
11. [[#11. ⭐ Advanced: Critical Chain Project Management (CCPM)]]
12. [[#12. ⭐ Advanced: Monte Carlo Schedule Risk Analysis]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): a 28-year schedule, Navi Mumbai International Airport
> **Navi Mumbai Airport (inaugurated 8 Oct 2025).** The airport was **proposed in Nov 1997**, **approved Aug 2007**, targeted to open around **mid-2020**, groundbroken in **Feb 2018** but with actual construction starting only in **Aug 2021** (Larsen & Toubro as contractor) after a developer change from GVK (won bid 2017) to Adani (2021) and the **resettlement of 2,786 households across ten villages**. Phase 1 was inaugurated on **8 Oct 2025** (reported cost **₹19,650 crore**, capacity **20 million passengers a year**), with commercial operations reported for **25 Dec 2025**. A textbook case of a critical path dominated by non-construction activities (land, approvals, ownership). ([All India Radio](https://www.newsonair.gov.in/pm-modi-unveils-%E2%82%B919650-cr-navi-mumbai-airport-a-new-milestone-in-indias-aviation-sector), [Wikipedia](https://en.wikipedia.org/wiki/Navi_Mumbai_International_Airport))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Gantt Chart
> 🔴 Tier 1 · _Tracker hint:_ Bar chart of tasks over time; dependencies; progress tracking

### Definition
A **Gantt chart** shows activities as horizontal bars on a time axis: bar start and length = start date and duration; arrows show dependencies; shading shows % complete; a vertical **"today" line** shows status; **milestones** are diamonds (zero duration). Popularised by Henry Gantt in the 1910s. Tools: MS Project, Excel, Smartsheet, Jira timeline, Asana.

**Strengths:** simple, intuitive for stakeholders, shows overlaps, progress and resource loading. **Weaknesses:** doesn't show dependency logic clearly in large projects, no float calculation unless linked to CPM, becomes cluttered; a Gantt is a **presentation** of a schedule, whereas the network diagram and CPM are the **calculation**. Baseline vs actual bars show slippage. Combine with milestone charts for executives and a **critical-path** highlight in red.

### Example
Website launch (days): Requirements (1–5), Design (6–12), Development (13–27), Testing (28–35), Go-live (36, milestone). By the end of day 20, 8 of Development's 15 planned days (days 13–20) have elapsed, so the plan says about 53% complete; if the bar is shaded only 40%, the Gantt shows it visibly behind.

### In the news
See news box. Public megaproject schedules are commonly shown on Gantt/milestone charts; the Navi Mumbai timeline (1997 proposal, 2007 approval, 2018 groundbreaking, 2021 construction start, 2025 inauguration) is effectively a milestone Gantt whose earliest bars were stretched by land and ownership issues.

### Interview angle
> [!question] How it is asked
> "How would you present the project schedule to the steering committee?" or "Gantt vs network diagram?"

> [!tip] Strong answer includes
> - What the bars, arrows, milestones and today-line show
> - Gantt = communication; network diagram/CPM = logic and float
> - Baseline vs actual and critical-path highlighting
> - Tool awareness (MS Project, Excel) and the right level of detail for each audience

---

## 2. Critical Path Method (CPM)
> 🔴 Tier 1 · _Tracker hint:_ Longest path; float = LS-ES; critical activity = zero float

### Definition
**CPM** (developed in 1957 by DuPont and Remington Rand: Kelley and Walker) uses a **deterministic** network to find the **critical path**: the **longest** path from start to finish, which sets the **shortest possible project duration**. Activities on it have **zero total float**; delay one by *x* days and the project slips by *x* days (unless compressed).

**Total float (slack)** $= LS - ES = LF - EF$. **Free float** $= ES_{\text{successor}} - EF_{\text{activity}}$ (minimum over successors). **Project float** is the delay allowed to the project end date. There can be **multiple critical paths**, and **near-critical** paths (small float) are also risky. Critical path is dynamic: it changes as activities slip or are crashed. Steps: list activities and durations, set dependencies, forward pass, backward pass, compute float, identify critical path, then compress or optimise resources.

### Example
Activities: A(3), B(4, after A), C(2, after A), D(5, after B), E(3, after C), F(2, after D and E).
Paths: A-B-D-F = 3+4+5+2 = **14**; A-C-E-F = 3+2+3+2 = **10**. Critical path = **A-B-D-F, 14 days**; path float for A-C-E-F = 14 − 10 = **4 days**.

### In the news
See news box. The airport's critical path was driven by non-construction predecessors (land acquisition and resettlement of 2,786 households, developer transition), the reason CPM must include approvals, land and funding activities, not only civil work.

### Interview angle
> [!question] How it is asked
> "Find the critical path and project duration for this network" or "What happens if a non-critical activity is delayed?"

> [!tip] Strong answer includes
> - Critical path = longest path, zero total float, minimum duration
> - Float formulas (LS−ES) and free vs total float
> - Multiple/near-critical paths and dynamic changes
> - Use: focus management attention and resources on critical activities

---

## 3. Network Diagram (AON/AOA)
> 🔴 Tier 1 · _Tracker hint:_ Activity-on-node vs activity-on-arrow; precedence logic

### Definition
A **network diagram** shows activities and their logical dependencies.
- **AON / PDM (Precedence Diagramming Method):** activities are **nodes** (boxes) and arrows show dependencies. Standard in modern tools (MS Project); supports **four dependency types** plus lead and lag, and needs no dummy activities.
- **AOA / ADM (Arrow Diagramming Method):** activities are **arrows**, nodes are events; supports only **finish-to-start** and needs **dummy activities** (dashed zero-duration arrows) to represent some logic. Used in classic PERT/CPM.

**Dependency types:** FS (finish-to-start, most common), SS (start-to-start), FF (finish-to-finish), SF (start-to-finish, rare). **Lead** = overlap (negative lag), **lag** = delay (e.g. concrete curing 7 days). **Dependency kinds:** mandatory (hard logic), discretionary (preferred logic), external, internal. Checks: one start, one end, no loops, no dangling activities.

### Example
In AON: node D "Install equipment" has predecessor B "Foundation" (FS) and a lag of 7 days for curing. If activity F "Testing" can start when "Install" starts (SS + 2-day lag) because testing preparation overlaps, SS captures it; AOA would need dummies and cannot express SS.

### In the news
See news box. Land acquisition/resettlement was a mandatory external dependency for the airport's construction, an example of logic that belongs in the network from day one.

### Interview angle
> [!question] How it is asked
> "Draw the network for this project" or "What is a dummy activity?"

> [!tip] Strong answer includes
> - AON vs AOA with differences (dependency types, dummies)
> - Four dependency types with examples; lead and lag
> - Mandatory vs discretionary vs external
> - Validity checks on the network

---

## 4. PERT (Program Evaluation Review Technique)
> 🔴 Tier 1 · _Tracker hint:_ 3-point estimate: (O + 4M + P) / 6; beta distribution

### Definition
**PERT** (US Navy Polaris programme, 1958) handles **uncertain** durations using three estimates: **Optimistic (O)**, **Most likely (M)**, **Pessimistic (P)**, assuming a **beta distribution**.

$$t_e = \frac{O + 4M + P}{6}, \qquad \sigma = \frac{P - O}{6}, \qquad \text{Variance} = \sigma^2$$

(The **triangular** distribution uses (O + M + P)/3.) Along the critical path: expected duration = Σ $t_e$; variance = Σ variances (assuming independence); $\sigma_{path} = \sqrt{\Sigma \sigma^2}$. Probability of finishing by a target date $T$: $Z = (T - \mu)/\sigma_{path}$, read from normal tables (Z = 1 → 84.1%, Z = 2 → 97.7%).

Limitations: assumes independent activities, ignores that other near-critical paths may become critical (**merge bias** underestimates project duration), estimates are subjective. CPM = deterministic; PERT = probabilistic.

### Example
Activity: O = 2, M = 5, P = 14 days. $t_e$ = (2 + 20 + 14)/6 = 36/6 = **6 days**; σ = (14 − 2)/6 = **2**; variance **4**.
Critical path of 5 such activities: μ = 40 days, total variance 25 → σ = 5. P(finish ≤ 45 days): Z = (45 − 40)/5 = 1 → **84%**. P(finish ≤ 50): Z = 2 → **97.7%**.

### In the news
See news box. The Navi Mumbai timeline (mid-2020 target vs Oct 2025 opening) is far outside any reasonable three-point range for civil work, showing that PERT must include the tail risks (land, litigation, ownership), not just the technical uncertainty.

### Interview angle
> [!question] How it is asked
> "A task has estimates 4, 6 and 14 days. What is the expected duration and the probability of finishing in 10 days?" (answer: te = (4 + 24 + 14)/6 = 7, σ = 10/6 ≈ 1.67)

> [!tip] Strong answer includes
> - Formulas for te and σ, and where beta distribution assumed
> - Path variance addition and Z-score probability
> - PERT vs CPM: probabilistic vs deterministic
> - Limitations (independence, merge bias, subjective estimates)

---

## 5. Forward & Backward Pass
> 🔴 Tier 1 · _Tracker hint:_ ES/EF/LS/LF calculations; total float; free float

### Definition
**Forward pass** (start → end): $ES$ = max of predecessors' $EF$ (project start = 0); $EF = ES + \text{duration}$. The largest EF at the end = project duration. **Backward pass** (end → start): $LF$ = min of successors' $LS$ (end activity LF = project duration); $LS = LF - \text{duration}$.

$$\text{Total float} = LS - ES = LF - EF,\qquad \text{Free float} = \min(ES_{succ}) - EF$$

(Convention: the "day 0" start and finish-of-day inclusive conventions vary; the "ES = predecessor EF" convention is used here.) Critical activities: total float = 0. Free float ≤ total float.

### Example
Same network as the CPM sub-topic (durations A3, B4, C2, D5, E3, F2):
| Act | ES | EF | LS | LF | Total float | Free float |
|---|---|---|---|---|---|---|
| A | 0 | 3 | 0 | 3 | 0 | 0 |
| B | 3 | 7 | 3 | 7 | 0 | 0 |
| C | 3 | 5 | 7 | 9 | 4 | 0 |
| D | 7 | 12 | 7 | 12 | 0 | 0 |
| E | 5 | 8 | 9 | 12 | 4 | 4 |
| F | 12 | 14 | 12 | 14 | 0 | n/a |
F: ES = max(EF_D = 12, EF_E = 8) = 12. C: LF = LS_E = 9, so LS = 7. Free float of C = ES_E − EF_C = 5 − 5 = 0 (delaying C delays E's earliest start), while E has free float 4.

### In the news
See news box. Float is the allowance that hides slippage until it is consumed: Navi Mumbai's multi-year slips mean any float in the original plan was long exhausted by the time the construction start moved to Aug 2021.

### Interview angle
> [!question] How it is asked
> "Compute ES, EF, LS, LF and float for these activities" or "Difference between free and total float?"

> [!tip] Strong answer includes
> - Forward pass uses max of predecessors, backward pass uses min of successors
> - Float formula and zero-float critical activities
> - Free float: delay without affecting any successor's early start; total float: without affecting project end
> - Check: sum along the critical path equals project duration

---

## 6. Resource Leveling
> 🔴 Tier 1 · _Tracker hint:_ Adjust schedule to resolve resource overallocation; extend duration

### Definition
**Resource leveling** (a resource optimisation technique) adjusts start and finish dates to resolve **over-allocation** or limited resource availability, balancing demand against supply. It **may change the critical path and often extends the project duration**, since it delays activities until resources are available, and uses float as well as pushing activities beyond it. Applied after the CPM schedule when resources are fixed or scarce (specialist engineers, cranes). Outputs: levelled schedule, resource histogram with reduced peaks.

Trade-offs: longer duration and possibly higher indirect costs; but smoother resource use, reduced burnout, avoided premium rates. **Resource-constrained scheduling** (limited resources) vs **time-constrained** (fixed end date). Software leveling (MS Project) uses priority rules; verify output manually.

### Example
Two parallel activities each need the same 2 welders, but only 2 are available (demand 4 for 5 days). Leveling sequences them one after another: Activity X days 1–5, Y days 6–10 instead of both days 1–5. Project finish moves from day 12 to day 17 because Y was on the critical path: duration extends by 5 days but welders are no longer overallocated.

### In the news
See news box. Resource constraints (contractor capacity, workforce availability) are typical for megaprojects; levelling is how plans reflect that real capacity rather than assuming unlimited resources.

### Interview angle
> [!question] How it is asked
> "You have more tasks than people. What do you do?" or "Resource leveling vs smoothing?"

> [!tip] Strong answer includes
> - Leveling changes dates to meet resource limits and may extend duration and change the critical path
> - Use when resources are the binding constraint
> - Alternatives: add resources, outsource, reduce scope
> - Quantify the impact on end date and cost

---

## 7. Resource Smoothing
> 🔴 Tier 1 · _Tracker hint:_ Adjust resources within float; critical path unchanged

### Definition
**Resource smoothing** adjusts activities **only within their available float**, so the **critical path and end date do not change**. It aims at reducing peaks and valleys in resource demand without adding time. Compared with leveling: smoothing is limited to float, leveling can exceed it.

| | Leveling | Smoothing |
|---|---|---|
| Constraint | Resources are limited | Time is fixed |
| Uses float? | Yes, and beyond | Within float only |
| End date | May extend | Unchanged |
| Critical path | May change | Unchanged |
| Result | May still not fully resolve overallocation | May leave some peaks |

### Example
In the CPM network, activity C has 4 days total float and E 4 days. If a scarce tester is overloaded in days 3–5, move C to start at day 4 (still before its late start of 7); the 14-day completion is unchanged, but the peak demand in days 3–5 reduces.

### In the news
See news box. For a project with a hard commissioning date, smoothing is the preferred first tool; the Navi Mumbai opening events (inauguration 8 Oct, operations later) illustrate fixed external dates.

### Interview angle
> [!question] How it is asked
> "Difference between resource leveling and resource smoothing?"

> [!tip] Strong answer includes
> - Critical path and duration change: leveling yes (possibly), smoothing no
> - Float is the "budget" for smoothing
> - Which one fits a fixed-deadline vs a fixed-resource project
> - A small example showing the shift of non-critical activities

---

## 8. Fast Tracking
> 🔴 Tier 1 · _Tracker hint:_ Parallel activities; increases risk; used when behind schedule

### Definition
**Fast tracking** is a **schedule compression** technique in which activities or phases normally done in **sequence** are performed **in parallel** (overlapped) for at least part of their duration. It shortens duration with **little or no added cost**, but **increases risk** (rework, coordination problems, quality issues) because later work starts without final inputs. Only applies where dependencies are **discretionary** (soft logic) and only on the **critical path** (otherwise no gain). Typical: start construction before design is 100% complete; begin testing modules while others are developed.

Mitigation: clear interfaces, frequent communication, risk review, early prototypes, buffers for rework. Evaluate overlap with a lead in the network (negative lag), and always re-run the critical-path calculation, since another path may now be critical.

### Example
Critical path: Design (10 days) then Build (15 days) = 25. If Build starts at day 7 of Design (lead of 3 days), the duration is 22 days: a 3-day saving at ~zero direct cost, with the risk that late design changes force rework on early build work.

### In the news
See news box. Public projects often start site works while approvals and land issues are pending (the airport's Feb 2018 groundbreaking preceded Aug 2021 actual construction), a reminder that "starting early" without resolving the dependency does not shorten the project.

### Interview angle
> [!question] How it is asked
> "The project is behind by 3 weeks. What can you do?"

> [!tip] Strong answer includes
> - Parallelise discretionary dependencies on the critical path
> - Cost low, risk high: say what rework risk and how to control it
> - Compare with crashing (cost up)
> - Recalculate the critical path after the change

---

## 9. Crashing
> 🔴 Tier 1 · _Tracker hint:_ Add resources to critical path; cost-time trade-off

### Definition
**Crashing** shortens the duration by **adding resources** (overtime, extra staff, faster equipment) to **critical-path** activities, at **increased cost**; it works only if added resources actually reduce duration (Brooks' law: adding people to a late software project may make it later). Choose activities with the **lowest cost slope**:

$$\text{Crash cost per day} = \frac{\text{Crash cost} - \text{Normal cost}}{\text{Normal duration} - \text{Crash duration}}$$

Procedure: (1) identify the critical path; (2) pick the critical activity with the lowest slope and remaining crash capacity; (3) crash by 1 day (or to its limit); (4) recompute the network, since a parallel path may become critical (then crash both); (5) stop at the target date or when crash cost exceeds benefit (e.g. liquidated damages avoided or delay penalty). The **time-cost trade-off curve** shows total cost as crashing proceeds; direct cost rises while indirect cost falls, giving an optimum.

### Example
Activity X normal 10 days at ₹100,000; crash 7 days at ₹160,000: slope = (160,000 − 100,000)/(10 − 7) = **₹20,000/day**. Activity Y: normal 8 days ₹80,000; crash 6 days ₹130,000: slope = 50,000/2 = ₹25,000/day. If both are critical and 2 days must be saved, crash X by 2 days: +₹40,000. If the delay penalty is ₹30,000/day (₹60,000 for 2 days), crashing is worthwhile.

### In the news
See news box. Where delays have already consumed years (the airport's multi-year slip), crashing cannot recover time lost to land and approvals; it only works where added resources actually shorten the critical activity.

### Interview angle
> [!question] How it is asked
> "How would you pull the schedule in by 2 weeks if the sponsor will pay?"

> [!tip] Strong answer includes
> - Crash critical activities only, lowest slope first
> - Recompute the critical path after each step
> - Compare crash cost against penalty or benefit
> - Limits: diminishing returns, Brooks' law, safety and quality

---

## 10. Schedule Compression
> 🔴 Tier 1 · _Tracker hint:_ Fast track + crash; impact on scope and quality

### Definition
**Schedule compression** shortens the schedule **without reducing project scope**, to meet constraints or imposed dates. Two techniques: **crashing** (cost up, risk modest) and **fast tracking** (risk up, cost modest). Both apply to **critical-path** activities. Other levers: reduce scope (not "compression" per PMI, but a legitimate option), improve productivity, remove waste, better resource skill, parallel procurement, pre-fabrication. Sequence of decision: fast track first when cost is the issue; crash when risk is the issue; combine when both are acceptable.

**Impact:** cost (crashing), risk and rework (fast tracking), potential **quality** shortfalls if testing is squeezed, and team stress. The PM must present the options to the sponsor with impacts on the triple constraint (see [[037 PM Fundamentals & Lifecycle]]), then update baselines through change control.

### Example
Original duration 14 days (critical A-B-D-F). Options: (a) Fast-track B and D (start D after 3 of B's 4 days): −1 day at no cost; (b) crash D by 2 days at ₹20,000/day: −2 days, +₹40,000. Combined: 14 − 3 = 11 days if the parallel path (10 days) stays below: A-C-E-F at 10 days becomes near critical (1 day float), so risk increases.

### In the news
See news box. Compression has limits where the binding constraint is external (land, approvals, ownership), which is why the first question is always "what is actually on the critical path?".

### Interview angle
> [!question] How it is asked
> "Compare crashing and fast tracking; which would you choose and why?"

> [!tip] Strong answer includes
> - Definitions and which constraint each trades (cost vs risk)
> - Applies only to critical activities, recompute after each change
> - Quality and scope impacts; presenting options to the sponsor
> - Re-baseline through change control

---

## 11. ⭐ Advanced: Critical Chain Project Management (CCPM)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Eliyahu Goldratt's **CCPM** (*Critical Chain*, 1997, applying the Theory of Constraints) argues that individual task estimates contain hidden safety that is wasted through **Parkinson's law** (work expands to fill time), the **student syndrome** (start late) and multitasking. CCPM:
- Cuts task estimates to about 50% (aggressive but achievable) and moves the removed safety into **buffers**.
- **Critical chain** = longest path considering **both task and resource dependencies** (not only logic).
- **Project buffer** at the end of the chain (protects delivery date), **feeding buffers** where non-critical chains join, and **resource buffers** (alerts).
- Manage by **buffer consumption** (green/yellow/red zones): act when a red zone is reached, not on every task slip. No task due dates; relay-race behaviour (start immediately, pass quickly).

Benefits: shorter overall durations (often cited as 25% shorter), fewer multitasking losses. Limitations: culture change and tooling, less fit for highly uncertain agile work.

### Example
Chain of 4 tasks each estimated at 10 days = 40 days with hidden 50% safety. CCPM estimates 5 days each = 20 days and adds a project buffer of half the chain = 10 days: planned finish 30 days with a visible buffer instead of 40 hidden days. If the chain has consumed 6 of the 10 buffer days at 50% completion, the buffer is yellow: plan recovery actions.

### In the news
See news box. A multi-year slip, as in Navi Mumbai, would have consumed any task-level safety long ago; buffers only help if their consumption is monitored and acted upon at project level.

### Interview angle
> [!question] How it is asked
> "How is critical chain different from critical path?"

> [!tip] Strong answer includes
> - Resource dependency and buffers as the main differences
> - Parkinson's law and student syndrome as the problems solved
> - Buffer management zones (green/yellow/red)
> - Applicability limits

---

## 12. ⭐ Advanced: Monte Carlo Schedule Risk Analysis
> ⭐ Advanced · _Added beyond the tracker_

### Definition
PERT's closed-form analysis uses only the critical path. **Monte Carlo simulation** (via tools like @RISK, Primavera Risk Analysis or Excel) samples each activity duration from a distribution (triangular or beta defined by O, M, P) thousands of times, recomputes the CPM each time, and records the project finish. Output: a **cumulative probability curve** (e.g. P50 = 52 days, P80 = 58 days) and a **criticality index** (the % of runs where an activity was on the critical path) and sensitivity (tornado) chart. It captures **merge bias**: where several parallel paths of similar length make the project's expected finish later than the single critical path suggests.

**Contingency (schedule reserve)** = target-confidence date minus the deterministic baseline date, e.g. P80 − baseline. Interpretation guides: if your plan date is the deterministic CPM finish, the probability of hitting it is often well below 50% for networks with parallel paths.

### Example
Two parallel paths each take 20 days if everything is on time, with ±3-day uncertainty each. The deterministic finish is 20 days. The project finishes at max(path1, path2). The chance that both paths end by 20 days is about 25% (0.5 × 0.5 assuming symmetric independent paths), not 50%, so a plan date of 20 days is risky; a P80 date of roughly 22 days is a better commitment.

### In the news
See news box. The wide gap between promised and actual dates for large infrastructure is what probabilistic schedules are meant to expose early; the Navi Mumbai timeline (targeted mid-2020, opened Oct 2025) is the type of outcome a P80 view warns about.

### Interview angle
> [!question] How it is asked
> "How confident are you in the delivery date?"

> [!tip] Strong answer includes
> - Replace single-point date with P50/P80 from simulation
> - Merge bias explained simply
> - Criticality index to focus management
> - Use results to set schedule contingency and communicate risk to the sponsor

---
## 🔗 Go deeper: expansion notes
- [[171 Project Management Interview Questions & Numericals|Project Management Interview Questions & Numericals]]
