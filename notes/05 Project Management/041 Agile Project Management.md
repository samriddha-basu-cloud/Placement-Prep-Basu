---
tags: [project-management, tier1]
area: Project Management
topic: "Agile Project Management"
tier: Tier 1
roles: Project Mgmt / PM
status: complete
subtopics: 9
---
# Agile Project Management

⬅ [[040 Risk & Stakeholder Management]] · [[_Index - Project Management|Project Management]] · [[042 Cost & Budget Management]] ➡

> **Area:** Project Management · **Priority:** 🔴 Tier 1 · **Target roles:** Project Mgmt / PM

## Sub-topics in this note
1. [[#1. Agile vs Waterfall]]
2. [[#2. Hybrid PM]]
3. [[#3. Scrum for Projects]]
4. [[#4. Agile Metrics]]
5. [[#5. Change Management in Agile]]
6. [[#6. Agile Risk Management]]
7. [[#7. Distributed Agile Teams]]
8. [[#8. Kanban for Operations Projects]]
9. [[#9. ⭐ Advanced: Scaling Agile (SAFe), Estimation and Earned Value in Agile]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Hybrid approaches rise; delivery discipline still a gap
> **Hybrid is mainstream (PMI, Feb 2024).** PMI's Pulse of the Profession research reported hybrid project management adoption rising from **20% in 2020 to 31.5% in 2023**, a 57.5% increase in three years, and said hybrid done well performs comparably to purely agile or predictive approaches. ([PMI](https://www.pmi.org/blog/project-management-embraces-the-fit-for-purpose-approach))
>
> **Delivery discipline (PMI Pulse of the Profession 2025).** Projects led by professionals with high business acumen showed schedule adherence of **63% vs 59%**, budget adherence of **73% vs 68%** and failure rates of **8% vs 11%** compared with others; only 18% of the 2,254 professionals surveyed rated as high business acumen. The point for agile: method choice matters less than commercial judgment and delivery control. ([PMI Pulse 2025 PDF](https://www.pmi.org/-/media/pmi/documents/public/pdf/learning/thought-leadership/pulse/pulse_of_the_profession_2025-1.pdf))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Agile vs Waterfall
> 🔴 Tier 1 · _Tracker hint:_ Flexibility vs predictability; uncertainty handling; change cost

### Definition
**Waterfall (predictive):** requirements, design, build, test and deploy run in sequence with sign-off gates; scope is fixed early, and cost and schedule are estimated. Strong when requirements are stable and well understood and regulation demands documentation (construction, plant installation).

**Agile (adaptive):** work is delivered in short **iterations** (1 to 4 weeks) producing a usable increment; requirements evolve through a prioritised backlog and frequent customer feedback. Strong when requirements are uncertain or change quickly (software, product development).

| Dimension | Waterfall | Agile |
|---|---|---|
| Scope | Fixed, time and cost estimated | Variable; time and cost fixed (timebox) |
| Planning | Up-front, detailed | Rolling, just-in-time |
| Customer involvement | At milestones | Continuous |
| Cost of change | Rises steeply later in the lifecycle | Kept low and flat by short feedback loops |
| Risk exposure | Discovered late (integration, test) | Discovered early each sprint |
| Value delivery | At the end | Incrementally |

The classic **cost-of-change curve** is the argument: the later a change, the more rework. Agile attacks the curve with short cycles, automated testing and continuous integration.

### Example
Building a new fulfilment centre (civil work, racking, fire clearance): waterfall; scope is known and rework is costly. Building the picker's mobile app inside it, where users keep changing their mind: Agile, with a 2-week sprint and demos to supervisors.

### In the news
See news box. The shift to hybrid acknowledges that neither pure approach fits every project.

### Interview angle
> [!question] How it is asked
> "When would you choose Agile over Waterfall?" "Can you use Agile for a physical infrastructure project?"

> [!tip] Strong answer includes
> - Decision criteria: uncertainty, cost of change, regulation, customer availability
> - Cost-of-change curve
> - Not a religion: most real projects are hybrid
> - A real example for each

---

## 2. Hybrid PM
> 🔴 Tier 1 · _Tracker hint:_ Agile for design, waterfall for compliance phases; gate reviews

### Definition
**Hybrid project management** combines predictive and adaptive practices within one project: for example a predictive overall plan, milestones and **stage gates** (budget, regulation, procurement) with agile execution in the uncertain parts (design, software, configuration). Patterns:
- **Phase-based:** waterfall for requirements/approvals and deployment, Agile sprints for build.
- **Component-based:** hardware or civil work predictive; software agile.
- **Agile inside a stage-gate (Agile-Stage-Gate):** each gate reviews the increments delivered, not documents.

Success factors: a clear interface between the two (who owns the integrated plan), a common **definition of done**, a shared risk log, and budgeting at a release/phase level rather than per task. Pitfall: "Wagile", where gates and documentation add bureaucracy while sprints add no real flexibility.

### Example
A pharma ERP rollout: GxP validation, audit trail and regulatory sign-off are waterfall gates (fixed documentation), while the planning-screen design and mobile-scanner user interface are built in 2-week sprints with plant users. Gate 3 reviews working software demos plus validation documents.

### In the news
See news box: hybrid use rose from 20% (2020) to 31.5% (2023), which is the market catching up with exactly this reality.

### Interview angle
> [!question] How it is asked
> "How would you manage a project with fixed regulatory deadlines but changing requirements?"

> [!tip] Strong answer includes
> - Split by uncertainty: what is fixed (compliance, hardware, contracts) vs what is fluid
> - Gate reviews tied to increments and evidence
> - A single integrated roadmap and a shared definition of done
> - Awareness of the "Wagile" failure mode

---

## 3. Scrum for Projects
> 🔴 Tier 1 · _Tracker hint:_ Sprint = mini-project; rolling wave planning; adaptive roadmap

### Definition
**Scrum** is a lightweight framework. **Roles:** Product Owner (value, backlog order), Scrum Master (process, removes impediments), Developers (self-managing team). **Events:** Sprint (timebox of 1 to 4 weeks, itself a mini-project with a goal), Sprint Planning, Daily Scrum (15 min), Sprint Review (inspect increment with stakeholders), Sprint Retrospective (improve the way of working). **Artifacts:** Product Backlog, Sprint Backlog, Increment, each with a commitment (Product Goal, Sprint Goal, Definition of Done).

For project-style use: the **roadmap** is adaptive (themes and releases, not fixed tasks); the near term is detailed (**rolling wave planning**: plan the next 1 to 2 sprints in detail, later work in outline); budgets and dates are managed by **release planning** using velocity.

Estimation: story points, planning poker, relative sizing. Scaling: SAFe, LeSS, Scrum of Scrums.

### Example
A 6-month "returns-processing portal" project for an e-commerce firm: 12 sprints of 2 weeks. Release 1 (sprint 6) delivers the minimum portal for a pilot warehouse; backlog for sprints 7 to 12 is reprioritised after pilot feedback. The sponsor sees a working increment every 2 weeks instead of a status report.

### In the news
See news box. Delivery discipline still matters: Scrum events do not replace budget and schedule control, the weakness PMI's 2025 data highlights (59% to 63% schedule adherence).

### Interview angle
> [!question] How it is asked
> "Explain Scrum." "How do you plan a 6-month project in Scrum?"

> [!tip] Strong answer includes
> - Roles, events, artifacts in a crisp line each
> - Sprint as timeboxed mini-project with a goal and a usable increment
> - Rolling-wave plan and release planning from velocity
> - What it does not cover (budget, contracts), where hybrid practices help

---

## 4. Agile Metrics
> 🔴 Tier 1 · _Tracker hint:_ Velocity, burndown chart, burnup chart, cycle time, lead time

### Definition
- **Velocity:** story points completed per sprint (done items only). Used for forecasting, not for comparing teams.
- **Burndown chart:** remaining work (y) vs time (x), for sprint or release. Falling line vs ideal line.
- **Burnup chart:** completed work and total scope on the same chart; shows **scope change** clearly, which burndown hides.
- **Lead time:** from request/commit to delivery (customer's wait). **Cycle time:** from work start to done (team's process time). Lead time = queue time + cycle time.
- **Throughput:** items finished per unit time.
- **Little's Law:** $WIP = \text{Throughput} \times \text{Cycle time}$.
- Others: escaped defects, sprint goal success rate, cumulative flow diagram (CFD), predictability.

Forecast: sprints remaining = remaining points / average velocity.

### Example
Last three sprints: 28, 32, 30 points, so average velocity = (28+32+30)/3 = **30**. Remaining backlog = 150 points, so forecast = 150/30 = **5 sprints** (10 weeks). A kanban board with 12 items in progress and throughput of 3 items/day has average cycle time = 12/3 = **4 days**. If items wait 6 days before work begins, lead time = 6 + 4 = 10 days.

### In the news
See news box. Metrics help the "schedule adherence" gap: burn-up charts make scope creep visible instead of letting it silently erase schedule predictability.

### Interview angle
> [!question] How it is asked
> "What is the difference between cycle time and lead time?" "Your burndown is flat. What do you check?"

> [!tip] Strong answer includes
> - Precise definitions and Little's Law
> - Burnup vs burndown: scope visibility
> - A flat burndown might mean blocked items, big stories, or scope added; check the board
> - Velocity is a planning tool, not a performance target (Goodhart's Law)

---

## 5. Change Management in Agile
> 🔴 Tier 1 · _Tracker hint:_ Embracing change; product backlog as change vehicle

### Definition
The Agile Manifesto: "Responding to change over following a plan" and "welcome changing requirements, even late in development". Change is absorbed through the **product backlog**: new or changed requirements are added as items, estimated, and **reprioritised by the Product Owner** by value, risk and cost. Because the sprint is timeboxed, the sprint scope is **protected** (changes go in the next sprint, unless the Product Owner cancels the sprint).

Compared with formal change control in waterfall (change request, impact analysis, CCB approval), Agile has a lightweight, continuous process; yet governance is still needed for **scope trade-offs** (fixed-time/cost: to add one item, drop or defer another), contracts (fixed price, variable scope), and dependencies on other teams. For **organisational change** (people adopting new ways of working) use frameworks such as ADKAR or Kotter alongside Agile.

### Example
Mid-project, a retailer requires GST e-invoice integration. Product Owner estimates 20 points, ranks it above 25 points of low-value dashboard work, and pushes the dashboard to the next release. Release date unchanged; scope swapped.

### In the news
See news box. High-business-acumen managers' better budget adherence (73% vs 68%) suggests that managing the trade-off of change against baseline is a commercial skill, not just a process.

### Interview angle
> [!question] How it is asked
> "A client keeps adding requirements every sprint. What do you do?"

> [!tip] Strong answer includes
> - Backlog as single vehicle; PO prioritises by value
> - Protect the sprint; changes enter next sprint
> - Swap, not stack: scope vs time vs cost trade-off made visible
> - Use burnup chart to show the effect of scope growth to the client

---

## 6. Agile Risk Management
> 🔴 Tier 1 · _Tracker hint:_ Short sprints reduce risk exposure; retrospective-based learning

### Definition
Agile reduces risk structurally: short **iterations** limit the amount of work at stake in any cycle (risk exposure = probability × impact is bounded), working software exposes technical and integration risk early, the highest-value/highest-risk items are done first (**risk-based prioritisation**, "fail fast"), frequent customer feedback reduces requirement and market risk, and the team's transparency (daily scrum, boards) raises problems early.

Practices: **risk-adjusted backlog** (add risk items as spikes), **spikes** (timeboxed research), **impediment log**, **retrospectives** (inspect and adapt), **definition of done** (quality gates), **automated testing/CI**, **risk burn-down** chart. Remaining risks: scope creep, dependency on external teams, technical debt, product-owner availability, and distributed team issues.

### Example
A route-optimisation tool depends on an untested third-party maps API. The team runs a 3-day **spike** in sprint 1; it shows rate limits would break the plan. Switching vendor in week 2 cost 3 days; discovering it at integration test in month 5 could cost weeks.

### In the news
See news box. CrowdStrike (see [[040 Risk & Stakeholder Management]]) is a counter-example of one-shot, all-at-once release; staged rollouts are agile's risk logic applied to deployment.

### Interview angle
> [!question] How it is asked
> "How does Agile reduce project risk?" "Where does Agile increase risk?"

> [!tip] Strong answer includes
> - Short feedback loops, early working increments, value/risk-ordered backlog
> - Spikes and definition of done
> - Honest limits: unclear budget, dependencies, scope creep, technical debt
> - Retrospective actions tracked to closure

---

## 7. Distributed Agile Teams
> 🔴 Tier 1 · _Tracker hint:_ Remote collaboration; time zones; async tools (Confluence, Slack)

### Definition
Distributed (remote/offshore) teams add friction in communication, trust, and tools. Principles:
- **Overlap hours:** protect 2 to 4 hours of common time for ceremonies (planning, demos); do the rest asynchronously.
- **Written-first culture:** decisions, acceptance criteria and designs in a shared wiki (Confluence, Notion), tickets in Jira/Azure DevOps, chat in Slack/Teams, recorded demos.
- **Explicit working agreements:** response times, meeting etiquette, definition of done, code review rules.
- **Follow-the-sun handoffs** with clear handover notes.
- **Visibility tools:** online boards, dashboards, CI status.
- **Trust and cohesion:** a kick-off in person, rotating meeting times so one site doesn't always bear the late hour, video on, social rituals.
- **Challenges:** time-zone lag, cultural/communication styles, tool sprawl, onboarding.

India angle: many projects run with India-US or India-Europe time offsets (US East is 9.5 to 10.5 hours behind IST), so sprint events cluster in the Indian late afternoon/evening.

### Example
Team across Pune, Bengaluru and London. Daily scrum is replaced by a 10-minute async stand-up post in Slack by 10:00 IST; a live 30-minute meeting at 14:30 IST (09:00 London in winter, 10:00 in summer) handles blockers. Sprint review is recorded for the US sponsor.

### In the news
See news box. As hybrid work becomes normal, distributed Agile practice is a baseline skill; the PMI data also shows only a minority of professionals strong on business acumen, so communication and commercial clarity are differentiators.

### Interview angle
> [!question] How it is asked
> "How would you run a sprint with team members across three time zones?"

> [!tip] Strong answer includes
> - Overlap hours for live events; async for the rest
> - Working agreements and single source of truth
> - Rotate inconvenient timings; build trust
> - Tools named, but principle first

---

## 8. Kanban for Operations Projects
> 🔴 Tier 1 · _Tracker hint:_ WIP limits, flow metrics, queue theory

### Definition
**Kanban** visualises work on a board (columns = workflow states), **limits work in progress (WIP)**, manages flow, and improves continuously. It has no fixed iterations, which suits **operations and support work** (maintenance requests, procurement tickets, audits) with continuous, unpredictable arrivals.

Core practices: visualise, limit WIP, manage flow, make policies explicit, feedback loops, improve collaboratively.

Flow metrics: throughput, cycle time, lead time, WIP, **cumulative flow diagram**, blocked time. **Little's Law:** $\text{Cycle time} = WIP / \text{Throughput}$. Reducing WIP reduces cycle time without needing faster workers. **Queueing theory** (Kingman's formula) says wait time grows non-linearly as utilisation approaches 100%, so some slack (for example 80 to 85% utilisation) keeps flow quick and handles variability.

Kanban vs Scrum: no sprints/roles required, change anytime, pull based, best for flow; Scrum for product increments in timeboxes. **Scrumban** merges them.

### Example
A plant maintenance team has 24 open work orders and finishes 6 per week: average cycle time = 24/6 = **4 weeks**. Cut WIP limit to 12 with the same throughput: cycle time = 12/6 = **2 weeks**; urgent breakdowns use an "expedite" lane with its own limit of 1.

### In the news
See news box. The lack of schedule adherence in PMI's data (59% to 63%) is a flow problem as much as a planning problem; WIP limits are the cheapest remedy.

### Interview angle
> [!question] How it is asked
> "How is Kanban different from Scrum?" "Your team has 40 tickets in progress and nothing finishes. Fix it."

> [!tip] Strong answer includes
> - WIP limits and Little's Law with a number
> - Stop starting, start finishing; pull, don't push
> - Why high utilisation causes queues (queueing theory)
> - Classes of service/expedite lane and policies

---

## 9. ⭐ Advanced: Scaling Agile (SAFe), Estimation and Earned Value in Agile
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Large programmes need coordination across teams. **SAFe** (Scaled Agile Framework) organises teams into an **Agile Release Train (ART)** of 5 to 12 teams that plan together in a **Program Increment (PI)** of about 8 to 12 weeks, with **PI Planning**, a shared backlog, and **Inspect and Adapt** workshops. Alternatives: LeSS, Nexus, Spotify model.

**Story point estimation** uses relative sizing (Fibonacci 1, 2, 3, 5, 8, 13), planning poker, and reference stories. **Earned value in Agile:** with release budget BAC and total points $S$, each point has planned value $BAC/S$; **EV = points done × BAC/S**, PV = points planned by now × BAC/S, AC = money spent. Then CPI = EV/AC, SPI = EV/PV (see [[042 Cost & Budget Management]]). **Definition of Ready and Done**, **MVP** and **WSJF** (Weighted Shortest Job First = cost of delay / job size) are used for prioritisation.

### Example
Release: 400 points, budget Rs 2 crore, so Rs 50,000 per point. After 5 sprints: 120 points done (EV = 120 × 50,000 = Rs 60 lakh), 150 planned (PV = Rs 75 lakh), spent Rs 70 lakh. CPI = 60/70 = 0.86, SPI = 60/75 = 0.80: over budget and behind. Forecast sprints needed at velocity 24 per sprint: (400-120)/24 = 11.7, so about 12 more sprints.

### In the news
See news box. Large Indian programmes are mostly hybrid; EVM-in-Agile gives the sponsor the same CPI/SPI language even though the team plans in points.

### Interview angle
> [!question] How it is asked
> "How do you report progress to a CFO when the team uses story points?" "How would you coordinate 8 Agile teams?"

> [!tip] Strong answer includes
> - Convert points to value (EV) so CPI and SPI work
> - Release-level baseline, with sprint-level flexibility
> - PI planning/ARTs, dependency mapping, shared cadence
> - WSJF or cost-of-delay prioritisation

---
## 🔗 Go deeper: expansion notes
- [[169 Project Team Leadership, Conflict & Team Development|Project Team Leadership, Conflict & Team Development]]
