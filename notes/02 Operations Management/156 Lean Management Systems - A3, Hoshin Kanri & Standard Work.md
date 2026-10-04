---
tags: [operations-management, tier1]
area: Operations Management
topic: "Lean Management Systems - A3, Hoshin Kanri & Standard Work"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Lean Management Systems - A3, Hoshin Kanri & Standard Work

⬅ [[155 Reliability Engineering & Maintenance Optimisation]] · [[_Index - Operations Management|Operations Management]] · [[157 Business Excellence Models & Quality Awards]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Lean as a Management System, Not a Toolbox]]
2. [[#2. A3 Thinking and the A3 Report]]
3. [[#3. Hoshin Kanri, X-Matrix and Catchball]]
4. [[#4. Standard Work, Takt Time and the Work Combination Sheet]]
5. [[#5. Training Within Industry (TWI)]]
6. [[#6. Visual Management, Andon and the Obeya]]
7. [[#7. Leader Standard Work and Gemba Walks]]
8. [[#8. Lean Daily Management and Tiered Meetings]]
9. [[#9. Lean Accounting and Value-Stream Costing]]
10. [[#10. Lean in Services, Healthcare and Offices]]
11. [[#11. Toyota Kata: Improvement Kata and Coaching Kata]]
12. [[#12. Sustaining Lean and Why Lean Programmes Fail]]
13. [[#13. ⭐ Advanced: Designing a Lean Management System Rollout (a Consulting View)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the lean management system meets AI, and shows what happens when its disciplines lapse
> **Toyota gives shop-floor staff AI tools for kaizen (published 19 Nov 2025).** Toyota built an in-house platform on Google Cloud (Kubernetes Engine, Cloud Workstations, web apps) so factory workers can create and deploy machine-learning models with drag-and-drop tools and no coding. Reported figures: **1,200+ workers across 10 plants**, **10,000+ models built by workers**, **10,000+ man-hours saved a year** and about **20% faster model creation**. The source frames it as amplifying kaizen and respect for people: the improvement system stays the same while the problem-solvers get better tools. The figures are as reported by the trade article, not audited. ([Lean Tomatoes](https://leantomatoes.com/2025/11/19/toyota-using-ai-to-reinvent-kaizen-and-boost-productivity/))
>
> **Boeing 737-9 door plug: NTSB findings (report released 10 Jul 2025).** Four critical bolts were missing after rework at Boeing's Renton plant: workers opened the plug with no removal record, closed it without securing the hardware, and no quality-assurance inspection was done. The NTSB also found Boeing had not fully implemented the safety management system it started in 2016. In Sept 2025 the FAA proposed **$3.1 million** in penalties over hundreds of quality-system violations at Boeing and Spirit AeroSystems 737 factories (Sept 2023 to Feb 2024), including an allegation that a Boeing employee pressured a member of its Organization Designation Authorization (ODA) unit to sign off an aircraft to meet a delivery schedule. A case study in what standard work, stop-the-line authority and leader discipline exist to prevent. ([Manufacturing Dive](https://www.manufacturingdive.com/news/boeing-faa-inadequate-training-oversight-737-max-doorplug-blowout-ntsb/752872/); [NPR](https://www.npr.org/2025/09/13/nx-s1-5540728/boeing-faa-safety-fines-door-plug-blowout))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Lean as a Management System, Not a Toolbox
> 🔴 Tier 1 · _Key points:_ tools vs system; principles, PDCA, respect for people; the lean "house"

### Definition
Tools such as 5S, kanban, SMED and VSM (covered in [[007 Lean Manufacturing]]) deliver one-off gains. A **lean management system (LMS)** is the set of routines that makes improvement permanent and everyone's job: it connects **strategy** to daily work, defines **how people solve problems**, and defines **what leaders do**. A common way to organise it:

| Layer | Question it answers | Typical mechanism |
|---|---|---|
| Direction | Where are we going? | Hoshin Kanri, true-north metrics (safety, quality, delivery, cost, people) |
| Standards | What is the best known way now? | Standard work, visual standards, TWI |
| Detecting | Is reality different from the standard? | Visual management, andon, tiered daily meetings |
| Problem solving | Why, and what next? | A3, PDCA, kata |
| Leadership | Who sustains it? | Leader standard work, gemba walks, coaching |
| Capability | Can people do all this? | TWI, kata, job rotation |

The two pillars of the Toyota Way are **continuous improvement** and **respect for people**; the engine is **PDCA** (plan, do, check, act) at every level. Taiichi Ohno's phrase is that without a standard there can be no kaizen: improvement is a change *from* a baseline. Contrast with a "tools programme" run by a central lean team, which is usually the first sign of a lean failure (sub-topic 12). Related systems: [[011 Quality Management (TQM)]], [[017 Process Management & Optimization]], [[008 Six Sigma & Quality Tools]].

### Example
Plant X ran SMED on 6 presses and cut changeovers from 48 to 28 minutes. Nobody owned the new standard, the changeover cart was reused for other jobs, and within a year the average drifted back to 41 minutes. Plant Y did the same, then put the changeover in a **standard work** sheet, tracked it on a **daily tier-1 board**, asked the supervisor to audit it weekly in **leader standard work**, and escalated misses above 35 minutes to the A3 queue. Same tools; the management system made the gain stick.

### In the news
See news box. Toyota's AI-for-kaizen platform is a tool upgrade inside an unchanged system: front-line staff still find and solve their own problems, only faster.

### Interview angle
> [!question] How it is asked
> "You implemented 5S and kanban but results faded after six months. What was missing?"

> [!tip] Strong answer includes
> - Tools without a management system: no standard, no audit, no leader routine
> - Layers: direction, standards, detection, problem solving, leadership, capability
> - Ownership by line managers rather than a central lean cell
> - A concrete example of a metric board, a tiered meeting and an escalation rule

---
## 2. A3 Thinking and the A3 Report
> 🔴 Tier 1 · _Key points:_ one sheet; PDCA storyline; coaching tool; root cause before countermeasure

### Definition
An **A3** is a problem-solving and communication method on a single A3 sheet (about 297 x 420 mm, the paper size that fitted a fax). Its value is the thinking discipline: the author must reduce a problem to one logical page that a sponsor can read, challenge and approve. The usual layout follows PDCA, left side for the problem, right side for the solution:

1. **Title and theme**: the problem or opportunity, owner, date.
2. **Background**: why it matters to the business (link to hoshin objective).
3. **Current condition**: facts at the gemba, process map or data, a **quantified gap**.
4. **Goal / target condition**: measurable, time-bound.
5. **Root-cause analysis**: 5 Whys, Pareto, fishbone, supported by data.
6. **Countermeasures**: what, who, by when, linked to each root cause (not "solutions in search of a problem").
7. **Implementation plan**: tasks, owners, dates.
8. **Follow-up / check**: how and when results are verified, and what is standardised or learned.

A3 types: problem-solving (most common), proposal, and status report. Common faults: jumping to countermeasures before root cause, vague goals, no data, a poster of text. The A3 is a **conversation** between author and mentor (often called *nemawashi*: building consensus), not a form to fill in.

### Example
Late deliveries from a machining line (on-time-in-full 82%, target 95%).
- **Current condition:** Pareto of 18% late orders over 6 weeks: 55% were caused by changeover overrun on three presses, 25% by material shortage, 20% other. Changeovers take 48 min, six a day = 288 min of 900 available (32% of the day).
- **Goal:** OTIF 95% in 90 days; changeover under 28 min.
- **Root cause (5 Whys):** overrun, because tools are searched for; because no standard kit; because each setter packs differently; because there is no standard changeover sheet.
- **Countermeasures:** SMED with external/internal split, shadow board, standard changeover work. Saving: $6\times(48-28)=120$ min a day, recovering $120/900=13\%$ of capacity.
- **Check:** weekly changeover time on the tier-1 board; OTIF tracked monthly; replicate to other presses.
Total time saved is a calculated target, to be proved at the check step.

### In the news
See news box. Toyota's AI tools are meant to feed the same cycle: the model finds a pattern, the worker still writes the problem and countermeasure.

### Interview angle
> [!question] How it is asked
> "Walk me through an A3 you have used or would use to reduce customer complaints."

> [!tip] Strong answer includes
> - Structure: background, current condition, goal, root cause, countermeasures, plan, follow-up
> - Quantified gap and Pareto before analysis
> - Countermeasures mapped one-to-one to root causes
> - The A3 as a coaching conversation and a record of learning

---
## 3. Hoshin Kanri, X-Matrix and Catchball
> 🔴 Tier 1 · _Key points:_ policy deployment; vital few; catchball; monthly review

### Definition
**Hoshin Kanri** (policy or "compass" management, developed in post-war Japan with Deming and Juran influences) turns top-level strategy into a small number of **breakthrough objectives** that are cascaded through the organisation to daily work and reviewed in PDCA cycles. Key elements:

- **Vital few:** 3 to 5 annual objectives; everything else is "daily management" (running the base business).
- **X-matrix:** one page with four quadrants: long-term objectives, annual objectives, **priorities/improvement projects**, and **metrics** (targets to improve), with correlations marked at the edges and owners on the right-hand side.
- **Catchball:** two-way negotiation of targets and means. A superior throws a target, the lower level examines feasibility and resources and throws back a revised plan, repeated until aligned; this builds ownership and surfaces constraints.
- **Cascade:** corporate X-matrix to plant to department to team, each level's objective supporting the one above.
- **Review:** monthly (or quarterly) hoshin reviews of progress against plan, with countermeasures (A3s) for deviations, and an annual review that feeds the next cycle.
Compared with MBO and the balanced scorecard ([[225 Budgeting, Variance Analysis & Balanced Scorecard]]), Hoshin emphasises *means* (how to achieve) and *catchball* as much as targets. Strategic context: [[020 Operations Strategy]], [[023 Business Fundamentals & Strategy]].

### Example
Corporate objective: cut order-to-delivery lead time by 30% (10 days to 7 days) and raise EBITDA margin 1.5 points. Plant level: reduce plant lead time 10 to 7 days through supermarket kanban and changeover reduction; department: changeover under 28 min on 6 presses. During catchball the maintenance head says two of the presses lack spare tooling; the plant manager adds a tooling-spares project and delays one target by a quarter in return for a firm budget. Monthly review: lead time 9.1 days against a plan of 9.0, a yellow status with an A3 on a raw-material delay.

### In the news
See news box. The Boeing case is a strategy-execution gap: stated priorities (quality, safety) and daily reality (delivery pressure) were not aligned, which hoshin and catchball try to surface early.

### Interview angle
> [!question] How it is asked
> "How do you make sure the plant's daily priorities match the company's strategy?"

> [!tip] Strong answer includes
> - Few objectives, cascaded with measures and owners
> - Catchball for realism and ownership
> - Regular review with countermeasures, not only reporting
> - Difference from MBO/KPI lists: alignment of means and daily management

---
## 4. Standard Work, Takt Time and the Work Combination Sheet
> 🔴 Tier 1 · _Key points:_ takt, sequence, standard WIP; baseline for kaizen; not a straitjacket

### Definition
**Standard work** is the currently best-known method for doing a job, documented so any trained operator can do it safely with the same quality and time. It rests on three elements:

1. **Takt time** $=\dfrac{\text{available production time}}{\text{customer demand}}$ (pace of demand).
2. **Work sequence** of each operator (manual work, walk, machine time).
3. **Standard work-in-process** needed to keep the sequence flowing (minimum stock in the cell).

Documents: the **process capacity table** (machine capacities, tool-change times), the **standardised work combination table (work combination sheet)** showing for each element the manual time, auto (machine) time and walk time on a time axis against takt, and the **standardised work chart** (layout, sequence, safety and quality points, standard WIP). Number of operators $=\dfrac{\text{total work content}}{\text{takt time}}$ rounded up, then balanced. Standard work is *not* fixed forever: it is the baseline against which operators and supervisors improve, and it must be written *with* the people who do the job. See also [[152 Learning Curves, Work Measurement & Productivity]] for time study and [[019 Facility Layout & Location]] for cells.

### Example
Demand 480 units a day, two shifts of 7.5 productive hours: takt $=2\times7.5\times3600/480=\mathbf{112.5\ s}$. A cell has five operations of 40, 35, 50, 45 and 30 s manual content (total 200 s). Operators needed $=200/112.5=1.78$, so 2. In a U-shaped cell, operator A runs operations 1, 2 and 5 (105 s, 93% of takt) and operator B runs 3 and 4 (95 s, 84%). Combination sheet check for one machined step: manual load 80 s, walk 10 s, machine auto time 60 s while the operator works elsewhere. The operator's own cycle is 90 s, so the step fits within takt of 112.5 s. If demand rises 20%, takt falls to $112.5/1.2=93.75$ s, operator B's 95 s now exceeds takt and the sequence must be rebalanced.

### In the news
See news box. Missing work records and a closed door plug without hardware are the exact failures standard work (with defined sequence and hold points) is designed to prevent.

### Interview angle
> [!question] How it is asked
> "Demand is 480 units a day and you have 15 working hours. How many operators and how would you document the job?"

> [!tip] Strong answer includes
> - Takt time computation and operators $=$ work content / takt
> - Three elements of standard work and the combination sheet
> - Standard work as the baseline for kaizen, created with the operators
> - Re-balance when demand changes; link to cell design

---
## 5. Training Within Industry (TWI)
> 🔴 Tier 1 · _Key points:_ JI, JM, JR; 4-step method; "if the worker hasn't learned, the instructor hasn't taught"

### Definition
**TWI** was a US wartime programme (1940 to 1945) that trained supervisors to expand output quickly with unskilled labour; by the end of the war over 1.6 million workers in about 16,500 plants had been certified. Three core 10-hour programmes, plus Program Development for trainers:

| Programme | Purpose | Core method |
|---|---|---|
| **Job Instruction (JI)** | Train people quickly and correctly | Four steps: **prepare** the worker, **present** the operation (key points, reasons), **try out** performance, **follow up** |
| **Job Methods (JM)** | Improve the way jobs are done with existing resources | Break down the job, question each detail, develop a new method (eliminate, combine, rearrange, simplify), apply it |
| **Job Relations (JR)** | Handle people problems before they grow | Get the facts, weigh and decide, take action, check results; treat people as individuals |

TWI strongly shaped Japanese industry and the Toyota Production System. Modern uses: **standard work** is the content, **JI** is how it is passed on (with job breakdown sheets listing *important steps*, *key points* and *reasons*), **JM** is the quick kaizen method, and **JR** supports supervisors in lean transformations.

### Example
Teaching a new operator to torque a wheel hub. Job breakdown: important step "position socket"; key point "square to face, 2 hands" (safety/quality); reason "avoids cross-threading and slip". Instruction: prepare (put at ease, state the job, find out what they know), present (do it slowly, explain key points), try out (the learner does it and explains key points back), follow up (check frequently, taper off). Certification time depends on the job, so quote no benchmark without data. Failure of training shows up as a quality escape, which is why key points are tied to the control plan ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

### In the news
See news box. Boeing's NTSB report cites a lack of specialised technicians and training and oversight gaps for door-plug work, the kind of failure structured job instruction targets.

### Interview angle
> [!question] How it is asked
> "How would you train 40 new operators on a line in two weeks without a drop in quality?"

> [!tip] Strong answer includes
> - Standard work and job breakdown first, then four-step JI with trainer certification
> - Skills matrix and cross-training plan, certification before solo work
> - JR for supervisors on the line, JM for continuous improvement
> - Quality check of early output and a feedback loop to the standard

---
## 6. Visual Management, Andon and the Obeya
> 🔴 Tier 1 · _Key points:_ see abnormality in seconds; andon pull; boards; obeya for projects

### Definition
**Visual management** displays standards and status so that anyone can see, within seconds and without a report, whether work is normal. Tools: floor markings and shadow boards (5S), kanban cards, heijunka boxes, performance boards (plan vs actual per hour), **andon** lights and signals, quality boards, takt boards.

- **Andon:** a signal (cord, button, light, sound) that allows any operator to **stop the line or call help** when an abnormality occurs; part of **jidoka** (build quality in). Success depends on the response: the supervisor must arrive in about a minute, and stops must not be punished.
- **Hourly production board:** target per hour, actual, variance, and reason for gaps; a gap of more than a set tolerance triggers a note and support.
- **Obeya** ("big room"): a dedicated room with the project or programme's plans, metrics, risks and A3s on the walls, used for weekly cross-functional meetings. Toyota used it for chief-engineer-led product development; common in new-product and transformation programmes.
Digital andon and MES dashboards extend the same ideas ([[047 MIS & Dashboard Design]], [[173 Process Mining & Operations Intelligence]]).

### Example
A cell has a target of 60 units/hour. The hourly board shows 60, 60, 52, 58 and the reason for the 52 ("changeover 9 min overrun"). The team leader sees the red cell within one minute and starts the escalation. After a month the board shows that 70% of lost output comes from two reasons, which become A3 topics. Where the board is a 12 m walk from the line or updated at end of shift, it is a report, not visual management.

### In the news
See news box. A functioning andon culture is the opposite of the alleged schedule-pressure behaviour in the FAA proposal; stopping the line must be rewarded.

### Interview angle
> [!question] How it is asked
> "How would you set up visual management in a plant that mostly relies on weekly Excel reports?"

> [!tip] Strong answer includes
> - Real-time or hourly, at the point of work, showing target/actual/reason
> - Andon with clear response times and no blame for pulling it
> - Escalation rules and daily review; boards driving action, not decoration
> - Obeya for cross-functional programmes with visible risks and A3s

---
## 7. Leader Standard Work and Gemba Walks
> 🔴 Tier 1 · _Key points:_ standard routine for managers; verify standards; coach, not fix

### Definition
**Leader standard work (LSW)** documents the repeating routine of team leaders, supervisors and managers: what to check, when and where, and what to do with abnormalities. It shifts leaders from firefighting to verifying and improving standards. Typical content by level: team leader checks start-up, hourly boards, andon response; supervisor checks standard work adherence, audits (5S, safety, quality gates), problem escalation; manager does gemba walks, reviews A3s, coaches; a plant head attends tier meetings and reviews hoshin KPIs.

**Gemba walk:** going to the place where work happens to observe, ask and learn, not to inspect. Good walks have a theme (e.g., safety), ask "why" and "show me", look for deviations from standard, and end with agreed follow-ups. The routine is usually split into fixed time-slots on an LSW card, with a visible "checks done" tick, and a first-line leader should spend most of the shift on the floor rather than at a desk. Related: [[169 Project Team Leadership, Conflict & Team Development]] for coaching style.

### Example
A supervisor's daily LSW: 06:00 start-up check (5 items), 06:30 tier-1 meeting, 09:00 audit of one standard-work sheet, 11:00 andon-response review, 14:00 problem escalation to the A3 queue, 15:00 handover. Three weeks of audits show 70% of line-side cards are out of date; the supervisor revises them with operators and the audit pass rate rises from 62% to 91% (illustrative figures). Without the LSW card these checks are the first to be dropped when the line has a breakdown.

### In the news
See news box. NTSB's finding that Boeing's safety management system was not fully implemented suggests leadership routines did not reach the factory floor.

### Interview angle
> [!question] How it is asked
> "As a new plant manager, what does your week look like and how do you avoid being dragged into firefighting?"

> [!tip] Strong answer includes
> - Fixed routine: gemba, tier meetings, A3 reviews, coaching time
> - Verifying standards rather than doing the work
> - Questions that develop people, not instructions
> - Visible checks and respect for the team's time

---
## 8. Lean Daily Management and Tiered Meetings
> 🔴 Tier 1 · _Key points:_ short stand-ups; tier 1-4 escalation; SQDCP boards

### Definition
**Lean daily management (LDM)** or tiered accountability is a cascade of short stand-up meetings in front of boards covering **SQDCP** (Safety, Quality, Delivery, Cost, People) with a clear escalation path:

| Tier | Who | Typical time (guide) | Focus |
|---|---|---|---|
| 1 | Team members and team leader | 10 to 15 min at shift start | Yesterday's result, today's plan, abnormalities |
| 2 | Supervisors, support (maintenance, quality, logistics) | 15 min | Issues team could not fix, cross-team support |
| 3 | Department managers | 15 to 20 min | Systemic problems, resources |
| 4 | Plant head and function heads | 20 to 30 min | Trends, hoshin progress, investment |

Rules: standing, same time and place, boards updated by owners, **escalate by time limit** (issues unsolved in 24 hours move up), problem owners and dates, and a closed loop (feedback goes back down). Link to MES/OEE data ([[018 Capacity Management & OEE]]) and to the tracking of A3 countermeasures. Without escalation limits, boards turn into reporting rituals.

### Example
A packaging line misses its output target by 6% for two days: tier 1 records "no film feeding, 14 min stops". Tier 2 the same morning assigns maintenance to check the unwinder; tier 3 two days later learns that the supplier's film tolerance is the cause and takes it to purchasing; tier 4 sees a plant-wide film defect trend and sets up a supplier A3. Five stand-ups of 15 minutes cost about $5\times15=75$ minutes of a manager's day at most, yet move a problem up in days rather than waiting for a monthly review.

### In the news
See news box. Toyota's AI tools are designed to give workers data to act on at tier 1; the system still depends on the daily meeting to turn data into action.

### Interview angle
> [!question] How it is asked
> "How do you make daily performance reviews useful instead of a time-wasting ritual?"

> [!tip] Strong answer includes
> - SQDCP and short standing meetings with defined agenda
> - Escalation rules with time limits and owners
> - Closed-loop feedback and A3s for recurring issues
> - Metrics that the team can influence; no blaming

---
## 9. Lean Accounting and Value-Stream Costing
> 🔴 Tier 1 · _Key points:_ costs by value stream; box score; no inventory-building profit

### Definition
Traditional standard costing rewards producing more: fixed overhead is absorbed into inventory, so reported profit rises when stock is built. Lean accounting aligns the numbers with flow: **value-stream costing** collects direct and overhead costs for a whole value stream (people, machines, materials, facility) on a weekly or monthly basis, avoiding allocation by labour hour; the **box score** shows operational measures (dock-to-dock days, first-pass yield, sales per person, on-time delivery), capacity (productive, non-productive, available) and financial results on a single page. Other features: simple weekly reporting, **pull** based inventory measures, target-cost design, and use of throughput logic ([[110 Cost Accounting for Operations]]). Inventory is treated as a risk and cash cost, not an asset to be maximised ([[136 Supply Chain Finance & Working Capital]]).

### Example
Price ₹1,000, variable cost ₹600, fixed overhead ₹2,00,000 a month, capacity 1,000 units, sales 800 units.
- Absorption costing, produce 1,000: overhead rate ₹200 a unit; profit $=800\times(1000-600-200)=\mathbf{₹1.60}$ lakh.
- Produce only 800: overhead rate ₹250; profit $=800\times(1000-600-250)=₹1.20$ lakh.
- Actual economic result in both cases: $800\times400-200{,}000=₹1.20$ lakh. Building 200 extra units created ₹40,000 of **paper** profit ($200\times200$) and consumed cash.
Box-score illustration: a value stream with ₹4 crore monthly sales, ₹2.2 crore materials and ₹1 crore stream costs shows ₹0.8 crore stream profit (20%); with 50 people that is ₹8 lakh of sales per person per month. After lean improvements, the inventory falls, and reporting avoids the "profit dip" trap by showing why profit fell.

### In the news
See news box. The Boeing penalty is an example of costs of poor quality surfacing as regulatory, rework and growth-cap costs that standard cost reports rarely show.

### Interview angle
> [!question] How it is asked
> "After your lean programme inventory fell and the finance team reported lower profit. How do you explain it?"

> [!tip] Strong answer includes
> - Absorption costing releases overhead when inventory falls, so profit dips temporarily; cash improves
> - Value-stream costing and box score as better management information
> - Example numbers like the 200 units x ₹200 above
> - Align the CFO before starting the programme

---
## 10. Lean in Services, Healthcare and Offices
> 🔴 Tier 1 · _Key points:_ information and patients as the flow; PCE; same wastes

### Definition
In services and offices the "material" is information, a patient or a customer, and waste shows up as **waiting, rework, handoffs, searching, over-processing and inventory of unprocessed work**. Tools adapt directly: value-stream maps with **process cycle efficiency** $PCE=\dfrac{\text{value-added time}}{\text{lead time}}$, standard work for transactions, queues managed with takt or pull signals, 5S for files and desktops, visual boards for work in progress (kanban boards), A3s for service problems, andon for escalating a stuck case. Differences from the factory: **variable arrival and process times** (see [[149 Queueing Theory & Waiting-Line Analysis]], [[151 Service Operations Management]]), the customer participates in the process, and quality is harder to measure. Healthcare examples are well known: reduced door-to-doctor time in emergency departments, standard order sets, pull-based stock of supplies; the risk is treating patients as units on a line, so patient safety and clinician time are measured as well.

### Example
Order-to-cash in an Indian distributor: invoice dispute takes 15 days elapsed, but hands-on touch time is 2.4 days (check, correct, approve). $PCE=2.4/15=16\%$. Wait time is 12.6 days. Root causes: batching approvals once a week, lost emails, three signatures. Countermeasures: daily approval, a shared tracker (kanban board), and a rule that errors are fixed at source. If lead time falls to 6 days and touch time stays 2.4 days, PCE is 40% and the days of receivables outstanding fall, releasing working capital.

### In the news
See news box. Toyota's workers building their own AI models for process problems is a sign that lean thinking is now applied to information flows, not only machines.

### Interview angle
> [!question] How it is asked
> "Can lean be applied to a bank's loan-processing back office? How would you start?"

> [!tip] Strong answer includes
> - Map the flow of the application, measure lead time and touch time (PCE)
> - Waste types in offices: waiting for approvals, rework from incomplete forms, handoffs
> - Pull, standard work and visual boards; first-time-right at intake
> - Caution about variability, customer and employee fatigue; link to queueing

---
## 11. Toyota Kata: Improvement Kata and Coaching Kata
> 🔴 Tier 1 · _Key points:_ vision, current condition, target condition, experiments; five coaching questions

### Definition
**Toyota Kata** (Mike Rother, 2009) describes the routines behind Toyota's improvement and coaching, proposing that capability is built by **practising routines** (kata) until they become habit. It treats management as the systematic pursuit of desired conditions.

**Improvement Kata (four steps):**
1. Understand the direction or challenge (**vision**).
2. Grasp the **current condition** with data.
3. Establish the next **target condition** (a measurable state a few weeks away).
4. **Experiment** toward it with rapid PDCA cycles, discovering obstacles one at a time.

**Coaching Kata:** the coach (typically the learner's manager) asks five questions about each cycle: What is the target condition? What is the actual condition? What obstacles are preventing you from reaching the target, and which one are you addressing now? What is your next step (the next experiment) and what do you expect? When can we go and see what we have learned? The learner records experiments on a storyboard. Compared with an A3, a kata focuses on **learning through experiments** where the path is unknown, whereas an A3 documents a problem with a known gap and countermeasures. The kata ideas influenced agile and DevOps practice ([[032 Agile & Scrum Framework]]).

### Example
Challenge: halve packaging-line changeover within a year. Current condition: average 48 min, standard deviation 9 min. Target condition for the next 4 weeks: 40 min with fewer than 3 tool searches. Obstacle 1: tools are not at point of use. Experiment: a changeover cart with tools; expectation: 4 min saved. Result: 3 min saved (45 min), learning: the labeller adjustment wastes 5 min, so the next experiment targets that. After 10 cycles of one-week experiments, the line reaches 31 min (illustrative). The coach asked the five questions at each 15-minute daily session instead of providing the answers.

### In the news
See news box. Workers training and deploying their own models is an experiment-driven approach consistent with kata: small, fast learning cycles by those closest to the problem.

### Interview angle
> [!question] How it is asked
> "How is Toyota Kata different from an A3 or a kaizen event?"

> [!tip] Strong answer includes
> - Improvement kata four steps and coaching kata five questions
> - Experiment-based approach for unknown paths vs A3 for defined problems
> - Daily practice and coaching drive capability, not a one-off event
> - Metric target conditions and visual storyboards

---
## 12. Sustaining Lean and Why Lean Programmes Fail
> 🔴 Tier 1 · _Key points:_ leadership, tools-first, drift; India examples; assessment

### Definition
Frequent causes of failed or faded lean efforts:

| Cause | Symptom | Countermeasure |
|---|---|---|
| Tools without system | Great kaizen events, results fade | Standard work, tier meetings, audits |
| Leaders delegate | "Lean cell" owns it, line managers do not | Leader standard work, gemba, hoshin objectives for line leaders |
| Cost-cutting focus | Headcount cut after kaizen; workers hide improvements | Employment security pledge, redeploy gains to growth |
| No quality-first | Speed pushed over defect-free work | Stop-the-line authority, jidoka |
| Wrong metrics | Local efficiency rises, WIP and cash worsen | Flow metrics, value-stream costing |
| Weak problem solving | Quick fixes recur | A3 and kata discipline |
| Slow culture change | Training only | Coaching, role-modelling, multi-year view |
Diagnostics: lean maturity assessments (ask whether standards exist, are visible and are checked), observation of tier meetings and the share of problems closed on time. A "lean transformation" typically takes years; fast gains are possible but sustaining them is the test.

**Indian context.** Toyota Kirloskar Motor (a joint venture set up in 1997, with Toyota Motor Corporation holding 89% and the Kirloskar Group 11% according to Wikipedia as checked in Oct 2026) and Maruti Suzuki are the best-known TPS-lineage employers; many Indian engineering and auto-component firms pursue TPM, TQM and Shingo or Deming-type recognition ([[157 Business Excellence Models & Quality Awards]]). In interviews, cite a case you have actually read about and only figures you can source.

### Example
A pharma plant reports ₹1.2 crore savings from 30 kaizen events in a year, but a year later the finance team can show only ₹0.4 crore in the P&L. Investigation: savings were counted as "hours saved", not as cost removed or capacity sold; 8 events' improvements were not standardised and reverted. Correction: finance co-signs savings; each event closes with a standard-work update and a 90-day audit; savings are classed as **hard** (cost out), **soft** (capacity freed) and **avoidance**. Realised value rises to ₹0.9 crore the next year (illustrative).

### In the news
See news box. Boeing's SMS and factory-quality gaps show how an organisation with detailed processes can still drift when leaders prioritise schedule; Toyota's reinvestment in kaizen tooling shows the opposite behaviour.

### Interview angle
> [!question] How it is asked
> "Why do most lean transformations fail and how would you make yours stick?"

> [!tip] Strong answer includes
> - Leadership behaviour and daily routines, not only tools
> - No-layoff or redeployment principle to retain trust
> - Standard work, audits, tier meetings and A3/kata discipline
> - Savings validated by finance; leading and lagging indicators

---
## 13. ⭐ Advanced: Designing a Lean Management System Rollout (a Consulting View)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A consulting-style roll-out of an LMS is staged. A common structure (a synthesis rather than a standard):

1. **Diagnose:** gemba observation, value-stream maps, a baseline of SQDCP KPIs, leadership interviews, an assessment against the six layers in sub-topic 1.
2. **Align:** hoshin objectives and a charter; choose a **model line** or value stream where results will be visible within 8 to 12 weeks.
3. **Build the basics:** 5S, standard work, visual boards, tier 1 meetings, escalation.
4. **Embed leadership routines:** leader standard work, coaching, A3 review rhythm.
5. **Expand:** replicate to other lines and functions; use kata for capability building; adapt tiers.
6. **Sustain:** audits, finance verification, hoshin integration, leader succession.
Quantify benefit by driver, e.g.: capacity (OEE, [[018 Capacity Management & OEE]]) gain valued at contribution margin only when there is demand; inventory days reduction valued at carrying cost; quality cost avoided; labour redeployed, not removed. Typical risks: change fatigue, supervisor overload, union issues, and demand volatility. For consulting cases, [[026 Case Interview — Operations Cases]] covers the structure.

### Example
Plant with ₹400 crore annual sales, OEE 62%, inventory 55 days of COGS ₹280 crore.
- Model line target: OEE +8 points on a bottleneck line that is sold out: if the line contributes ₹120 crore sales at 30% contribution, $8/62\approx13\%$ more output = ₹15.5 crore sales, ₹4.6 crore contribution (only if the market takes it).
- Inventory from 55 to 45 days: reduction $=280\times10/365=₹7.7$ crore cash; at 10% carrying cost, ₹0.77 crore a year.
Program cost: external coaching and internal time, say ₹1.5 crore. Payback is under a year only if the OEE gain is monetised through demand; otherwise the cash benefit alone gives a payback of about two years. Highlighting this dependency is what a strong consultant answer does.

### In the news
See news box. Both items are reminders that the benefit case depends on discipline sustained over time, not on a single event.

### Interview angle
> [!question] How it is asked
> "A client wants a lean transformation across 12 plants. How would you structure the first 100 days?"

> [!tip] Strong answer includes
> - Diagnose, pick a model line, show results fast, then scale
> - Leadership routines and capability building, not just tool deployment
> - Business case by driver, with demand and cash caveats
> - Risks: change fatigue, labour trust, KPI gaming, and a sustaining plan
