---
tags: [product-management, tier1]
area: Product Management
topic: "Agile & Scrum Framework"
tier: Tier 1
roles: PM / Project Mgmt
status: complete
subtopics: 14
---
# Agile & Scrum Framework

⬅ [[031 Product Metrics & Analytics]] · [[_Index - Product Management|Product Management]] · [[033 Design Thinking & UX]] ➡

> **Area:** Product Management · **Priority:** 🔴 Tier 1 · **Target roles:** PM / Project Mgmt

## Sub-topics in this note
1. [[#1. Agile Manifesto]]
2. [[#2. Scrum Roles]]
3. [[#3. Sprint Cycle]]
4. [[#4. Product Backlog]]
5. [[#5. Sprint Backlog]]
6. [[#6. User Story Format]]
7. [[#7. Story Points & Velocity]]
8. [[#8. Kanban vs Scrum]]
9. [[#9. Definition of Done (DoD)]]
10. [[#10. Sprint Retrospective]]
11. [[#11. Jira for Agile]]
12. [[#12. Scaled Agile (SAFe basics)]]
13. [[#13. ⭐ Advanced: Flow Metrics, Little's Law and Probabilistic Forecasting]]
14. [[#14. ⭐ Advanced: Agile in Non-Software Contexts and Hybrid Project Management]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Digital.ai's 18th State of Agile report (Oct 2025)
> Released on **28 October 2025**, Digital.ai's 18th State of Agile report (nearly **350 respondents**, mainly Agile coaches and consultants in enterprises of 20,000+ employees) found: **84% of respondents use AI** in their work (up from **68%** the year before), but only **49%** have governance guardrails; **76%** feel more pressure to prove Agile's business impact; **79%** say teams are doing more with fewer resources; and **74%** use hybrid, blended or custom Agile approaches rather than one pure framework. ([Digital.ai press release](https://digital.ai/press-releases/digital-ais-18th-state-of-agile-report-marks-the-start-of-the-fourth-wave-of-software-delivery/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Agile Manifesto
> 🔴 Tier 1 · _Tracker hint:_ 4 values, 12 principles; mindset over methodology

### Definition
The **Agile Manifesto** (2001, Snowbird, Utah; 17 authors) states four values: "We value ... *more* ..."

1. **Individuals and interactions** over processes and tools
2. **Working software** over comprehensive documentation
3. **Customer collaboration** over contract negotiation
4. **Responding to change** over following a plan

"While there is value in the items on the right, we value the items on the left more." The **12 principles** include: satisfy the customer through early and continuous delivery; welcome changing requirements; deliver working software frequently (weeks, not months); business people and developers work together daily; build around motivated individuals; face-to-face conversation; working software is the primary measure of progress; sustainable pace; technical excellence; simplicity (maximising work not done); self-organising teams; regular reflection and adaptation.

Agile is a **mindset** (iterative, incremental, feedback-driven), implemented by frameworks such as Scrum, Kanban, XP. It contrasts with **waterfall**: sequential phases, heavy upfront planning, changes costly. Agile is not "no planning or no documentation".

### Example
A retail bank builds a mobile loan feature: waterfall delivers after 12 months and discovers customers hate the KYC step; Agile ships a basic version in 6 weeks, learns from users, then iterates sprint by sprint.

### In the news
See news box. 74% blending approaches shows that the mindset (values and principles) outlasts any one framework.

### Interview angle
> [!question] How it is asked
> "What is Agile and how is it different from waterfall?" or "Do you need Scrum to be Agile?"

> [!tip] Strong answer includes
> - The four values correctly with the "over" trade-off
> - Mindset vs framework distinction
> - Where Agile fits (uncertain requirements) and where waterfall still does (fixed scope, regulated, hardware)
> - A concrete example

---

## 2. Scrum Roles
> 🔴 Tier 1 · _Tracker hint:_ Product Owner, Scrum Master, Development Team — responsibilities

### Definition
The Scrum Guide (2020) defines one **Scrum Team** with three accountabilities (typically about 10 or fewer people):

| Role | Accountable for |
|---|---|
| **Product Owner (PO)** | Maximising product value; owns and orders the Product Backlog; single voice for stakeholders; defines the Product Goal |
| **Scrum Master (SM)** | Team effectiveness; coaches Scrum; removes impediments; facilitates events; a servant-leader, not a project manager |
| **Developers** | Creating a usable Increment each Sprint; plan the Sprint; self-managing, cross-functional (dev, test, design, data) |

The earlier term "Development Team" (2017 and before) became "Developers" in 2020. No hierarchy within the team; no "team lead". Stakeholders and managers are outside the team. Common anti-patterns: PO as a proxy with no decision power, SM as a task assigner, a PO who is not available.

### Example
In a quick-commerce app team: PO decides to prioritise "reorder in one tap" over "referral banners" based on data; Developers (2 backend, 2 mobile, 1 QA, 1 designer) estimate and build; SM resolves a blocker with the payments API vendor and coaches the team on stand-ups.

### In the news
See news box. With 79% doing more with fewer resources, a strong PO who says "no" and orders the backlog by value is critical.

### Interview angle
> [!question] How it is asked
> "What is the difference between a Scrum Master and a Project Manager?" or "As a PO, how do you handle conflicting stakeholder demands?"

> [!tip] Strong answer includes
> - The three accountabilities and their distinct outputs
> - SM as servant-leader, not command-and-control
> - PO's prioritisation logic (value, risk, dependencies)
> - A realistic anti-pattern and fix

---

## 3. Sprint Cycle
> 🔴 Tier 1 · _Tracker hint:_ Sprint planning → Daily standup → Sprint review → Sprint retrospective

### Definition
A **Sprint** is a fixed timebox of one month or less (commonly 1–2 weeks) that produces a potentially releasable **Increment**. The five Scrum events:

| Event | Purpose | Max timebox (1-month sprint) |
|---|---|---|
| Sprint | Container for all events | 1 month |
| **Sprint Planning** | Why (Sprint Goal), what (backlog items), how (plan) | 8 hours |
| **Daily Scrum** | Inspect progress to the Sprint Goal, adapt the plan | 15 minutes |
| **Sprint Review** | Show the Increment to stakeholders, gather feedback, adapt backlog | 4 hours |
| **Sprint Retrospective** | Improve how the team works | 3 hours |

Timeboxes are proportionally shorter for shorter sprints. The Sprint Goal does not change during the sprint; scope may be clarified. The PO can cancel a sprint only if the Sprint Goal becomes obsolete. Scrum pillars: **transparency, inspection, adaptation**; values: commitment, focus, openness, respect, courage.

### Example
2-week sprint: Mon (Day 1) planning (about 4 hours); daily scrum at 10:00 for 15 minutes; backlog refinement mid-sprint (not a formal event); final Thursday review with stakeholders; retro the same afternoon; next sprint starts the next day with no gap.

### In the news
See news box. Many teams adapt cadence (shorter sprints or flow) when AI tooling accelerates coding; the events remain inspect-and-adapt checkpoints.

### Interview angle
> [!question] How it is asked
> "Walk me through a sprint." "What if the team cannot finish the sprint scope?"

> [!tip] Strong answer includes
> - Five events with purpose and timebox
> - Sprint Goal and Increment concepts
> - Handling unfinished work (back to the backlog, re-estimate; do not extend the sprint)
> - Inspect-and-adapt as the rationale

---

## 4. Product Backlog
> 🔴 Tier 1 · _Tracker hint:_ User stories, epics, themes; backlog grooming / refinement

### Definition
The **Product Backlog** is the single, ordered list of everything that might be needed in the product, owned by the PO. It is **emergent** and never complete; its commitment is the **Product Goal**.

Hierarchy: **Theme** (strategic grouping) → **Epic** (large body of work, spans many sprints) → **User story** (a sprint-sized slice of value) → **Task** (technical steps, in the sprint backlog).

**Refinement** (formerly *grooming*) is the ongoing activity of breaking down, clarifying, estimating and ordering items so that the top items are *ready* (small enough for one sprint, clear acceptance criteria, understood dependencies). Typical effort cap about 10% of capacity. Ordering considers value, risk, dependencies, cost of delay and effort. Qualities of a good backlog (**DEEP**): Detailed appropriately, Estimated, Emergent, Prioritised.

### Example
Theme: "Faster checkout" → Epic: "UPI one-tap pay" → Stories: "As a returning user, I want to pay with my saved UPI ID so that I skip entering details" and "As a user, I want a failed-payment retry". Items near the top are refined to be ready; items at the bottom stay vague epics.

### In the news
See news box. As teams add AI-assisted coding, backlog quality and clear acceptance criteria become the constraint, not coding speed.

### Interview angle
> [!question] How it is asked
> "How do you prioritise a backlog?" or "What is backlog refinement and who does it?"

> [!tip] Strong answer includes
> - PO owns ordering; team collaborates in refinement
> - Epic/story/task breakdown with example
> - Prioritisation techniques (value vs effort, RICE, MoSCoW, cost of delay)
> - Ready criteria and the DEEP qualities

---

## 5. Sprint Backlog
> 🔴 Tier 1 · _Tracker hint:_ Committed items for sprint; sprint goal alignment

### Definition
The **Sprint Backlog** = the **Sprint Goal** (why) + the selected Product Backlog items (what) + an actionable plan to deliver the Increment (how). It is owned by the Developers, made visible in real time (board), and updated daily as more is learned.

Sprint Planning inputs: the ordered Product Backlog, the latest Increment, projected capacity and **velocity** (past throughput), and the **Definition of Done**. Developers forecast what they can complete; it is a *forecast, not a promise* in Scrum 2020. The Sprint Goal gives coherence and flexibility: if the plan changes, scope is renegotiated with the PO while protecting the goal. Avoid mid-sprint scope additions that break the goal. Capacity planning: $\text{Capacity}=\text{people}\times\text{days}\times\text{focus factor}$ minus leave.

### Example
Sprint Goal: "Users can pay with saved UPI IDs in the checkout." Sprint Backlog: 5 stories (21 points), tasks such as API integration, UI, tests and monitoring. Capacity: 6 developers × 9 working days × 0.7 focus = 37.8 person-days; velocity of last three sprints (20, 22, 21) suggests ~21 points.

### In the news
See news box. Sprint goals help teams under resource pressure choose what *not* to do.

### Interview angle
> [!question] How it is asked
> "How do you decide how much work to take into a sprint?" or "Mid-sprint, the CEO asks for a new feature. What do you do?"

> [!tip] Strong answer includes
> - Capacity plus velocity plus Sprint Goal
> - Developers own the forecast; PO provides priorities
> - Protect the goal; negotiate trade-offs, swap not add
> - Uses the Definition of Done to count completed work

---

## 6. User Story Format
> 🔴 Tier 1 · _Tracker hint:_ 'As a [user], I want [goal] so that [benefit]'; acceptance criteria

### Definition
A **user story** is a short description of a feature from the user's perspective:

> *As a* **[type of user]**, *I want* **[goal]** *so that* **[benefit]**.

Qualities (**INVEST**, Bill Wake): **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable. Stories follow the **3 Cs**: Card (the text), Conversation (details), Confirmation (acceptance criteria).

**Acceptance criteria** define when the story meets requirements, often in **Given-When-Then** (Gherkin) style:

```gherkin
Given I am a logged-in user with a saved UPI ID
When I tap "Pay now" on the checkout page
Then the payment is initiated and I see a confirmation within 5 seconds
```

Splitting large stories: by workflow step, data variation, user role, happy path vs exceptions, or "walking skeleton" first. Avoid technical-task stories with no user value.

### Example
"As a first-time borrower, I want to upload my PAN and Aadhaar-based eKYC so that my loan application is processed without visiting a branch." Acceptance criteria: eKYC success shows a green tick; mismatched name shows an error with a retry; the process completes in under 2 minutes at P90 (illustrative).

### In the news
See news box. AI tools can draft stories quickly, but testable acceptance criteria and the "so that" benefit still need human product judgement.

### Interview angle
> [!question] How it is asked
> "Write a user story and acceptance criteria for [feature]." or "How do you split a big story?"

> [!tip] Strong answer includes
> - Correct format with a real benefit
> - INVEST check and Given-When-Then criteria
> - Splitting strategy
> - Non-functional criteria (performance, security) when relevant

---

## 7. Story Points & Velocity
> 🔴 Tier 1 · _Tracker hint:_ Relative estimation; planning poker; velocity trend

### Definition
**Story points** are a unit of *relative* size that combine effort, complexity and uncertainty, not hours. Teams usually use a modified Fibonacci scale: 1, 2, 3, 5, 8, 13, 21. Estimate by comparison to reference stories ("this is about twice that one").

**Planning poker:** each Developer privately picks a card, all reveal at once, high and low estimators explain, repeat until converged. It avoids anchoring.

**Velocity** = story points of *Done* items completed per sprint; use the average of the last 3–5 sprints to forecast.

$$\text{Sprints remaining}=\frac{\text{Remaining backlog points}}{\text{Average velocity}}$$

Cautions: velocity is team-specific (do not compare teams or use as a performance target, because points inflate), count only fully Done stories, and recalibrate when the team changes. Alternatives: #NoEstimates, throughput and cycle time, T-shirt sizing.

### Example
Last five sprints' velocity: 18, 22, 20, 19, 21 → average 20. Remaining backlog 140 points → 140/20 = **7 sprints**. With a range (min 18, max 22): 6.4 to 7.8 sprints, so forecast 7–8 sprints.

### In the news
See news box. Leaders under pressure to demonstrate Agile ROI (76%) may be tempted to use velocity as a target; it is a planning tool, and outcome metrics (value delivered, lead time) are better.

### Interview angle
> [!question] How it is asked
> "Why not estimate in hours?" or "Velocity dropped 30% this sprint. What do you do?"

> [!tip] Strong answer includes
> - Relative estimation rationale and Fibonacci scale
> - Planning poker mechanics
> - Velocity for forecasting, not for comparing teams
> - Investigates causes of drops (leave, tech debt, unplanned work, team changes)

---

## 8. Kanban vs Scrum
> 🔴 Tier 1 · _Tracker hint:_ Scrum = sprints; Kanban = continuous flow; hybrid Scrumban

### Definition
| | Scrum | Kanban |
|---|---|---|
| Cadence | Fixed-length sprints | Continuous flow |
| Roles | PO, SM, Developers | None prescribed |
| Commitment | Sprint Goal / forecast | WIP limits, pull when capacity frees |
| Change | Protected during sprint | Anytime |
| Metrics | Velocity, burndown | Cycle time, lead time, throughput, WIP |
| Best for | Product development with planned increments | Support, ops, maintenance, unpredictable inflow |

**Kanban** principles: visualise work on a board (To do, Doing, Done), **limit WIP**, manage flow, make policies explicit, improve continuously. **Little's Law:** $\text{Avg cycle time}=\frac{\text{WIP}}{\text{Throughput}}$.

**Scrumban** blends the two: Scrum events with a Kanban board and WIP limits, or sprints replaced by on-demand planning. Choose by nature of work: planned deliverables and cross-functional collaboration (Scrum) vs interrupt-driven flow (Kanban).

### Example
An IT support team receives 20 tickets a day with variable urgency: Kanban with WIP limit of 6 and a cycle-time target of 2 days. Throughput 3 tickets a day with WIP 6 gives cycle time = 6/3 = 2 days. A product squad building a new payment feature uses 2-week Scrum sprints.

### In the news
See news box. The 74% hybrid or custom approaches include Scrumban-type blends.

### Interview angle
> [!question] How it is asked
> "When would you choose Kanban over Scrum?"

> [!tip] Strong answer includes
> - Fixed iteration vs continuous flow
> - WIP limits and flow metrics
> - Context-based choice with an example
> - Scrumban and when hybrid helps

---

## 9. Definition of Done (DoD)
> 🔴 Tier 1 · _Tracker hint:_ Agreed completion criteria; quality gates

### Definition
The **Definition of Done** is a formal, shared description of the state of an Increment when it meets the quality needed for the product. Work that does not meet the DoD cannot be released or even shown at review as "Done"; it returns to the backlog. In Scrum 2020 it is the commitment for the Increment.

Typical items: code reviewed and merged, unit and integration tests passing, acceptance criteria met, security and performance checks, documentation updated, deployed to staging, product owner accepted, no critical bugs, monitoring in place.

Contrast: **Acceptance criteria** are story-specific; DoD applies to all stories. **Definition of Ready** governs entry to the sprint. Teams evolve DoD over time (adding automation, accessibility checks). A weak DoD leads to **technical debt** and fake velocity.

### Example
DoD for a fintech team: code peer-reviewed; 80% unit test coverage on new code; no critical Sonar issues; passes regression suite; PCI/security checklist; feature flag configured; release notes written. A story whose code works but has no tests is **not Done** and its points are not counted in velocity.

### In the news
See news box. With 84% using AI, teams are adding AI-specific checks (review of generated code, licensing and security scans) to their DoD, consistent with only 49% having governance.

### Interview angle
> [!question] How it is asked
> "What is the difference between acceptance criteria and Definition of Done?"

> [!tip] Strong answer includes
> - Team-wide quality standard vs story-specific conditions
> - Examples and relation to technical debt
> - Evolving the DoD through retrospectives
> - Handling incomplete work and velocity counting

---

## 10. Sprint Retrospective
> 🔴 Tier 1 · _Tracker hint:_ What went well, what to improve, action items

### Definition
The **Sprint Retrospective** closes the sprint; the team inspects how it worked (people, interactions, processes, tools, DoD) and plans improvements. Timebox: up to 3 hours for a 1-month sprint. Attendees: the Scrum Team.

Common formats: **Start-Stop-Continue**; **Mad-Sad-Glad**; **4Ls** (Liked, Learned, Lacked, Longed for); **Sailboat** (wind, anchors, rocks); **5 Whys** for root causes. Flow: set the stage (psychological safety) → gather data → generate insights → decide **a few** actions → close. Output: 1–3 concrete, owned, time-bound improvements added to the next Sprint Backlog.

Good retros: blameless, follow up on past actions, vary the format, include data (cycle time, defects). Failure modes: complaints without actions, only the loudest voices, management attending and silencing the team.

### Example
Retro finding: three stories slipped due to late QA handoff. Action: "QA joins refinement and writes acceptance tests before development; owner Priya; check cycle-time of QA phase next retro." Result tracked as a measurable item next sprint.

### In the news
See news box. The pressure to prove Agile's impact (76%) makes retros useful: improvements should be tied to measurable outcomes.

### Interview angle
> [!question] How it is asked
> "How do you run a retrospective, and what if the team is silent or negative?"

> [!tip] Strong answer includes
> - A structure and varied formats
> - Psychological safety and blameless tone
> - Concrete actions with owners and follow-up
> - Using data and tracking whether improvements worked

---

## 11. Jira for Agile
> 🔴 Tier 1 · _Tracker hint:_ Boards, backlog, sprint management, reports, velocity chart

### Definition
**Jira** (Atlassian) is the most widely used tool for Agile work tracking.

- **Issue types:** Epic, Story, Task, Bug, Sub-task; fields: assignee, priority, story points, labels, components, fix version.
- **Boards:** **Scrum board** (active sprint with columns To Do, In Progress, Done) and **Kanban board** (continuous flow with WIP limits). Columns map to workflow statuses.
- **Backlog view:** order issues, create sprints, drag into a sprint, estimate.
- **Sprint management:** start/complete sprint, sprint goal, move unfinished issues.
- **Reports:** **Burndown chart** (remaining work vs time), **Burnup**, **Velocity chart** (committed vs completed per sprint), **Sprint report**, **Cumulative flow diagram**, **Control chart** (cycle time).
- **JQL** (Jira Query Language):

```
project = PAY AND sprint in openSprints() AND status != Done ORDER BY priority DESC
assignee = currentUser() AND issuetype = Bug AND created >= -7d
```

- Workflows, automation rules, roadmaps (timeline), dashboards and integrations (Confluence, GitHub, Slack).

### Example
Create Epic "UPI one-tap pay", add Stories with 3/5/8 points to the backlog, create "Sprint 14", move stories in, **Start sprint** (set duration and goal). Daily, developers drag cards; at the end, **Complete sprint**; the velocity chart shows committed 21 vs completed 19 points. Unfinished stories return to the backlog.

### In the news
See news box. AI adoption is reported by 84% of teams while governance (49%) lags, so how a team configures its Jira workflow and DoD for AI-assisted work is a live question.

### Interview angle
> [!question] How it is asked
> "How have you used Jira?" or "Which Jira reports help you track sprint health?"

> [!tip] Strong answer includes
> - Boards, backlog, sprint workflow and issue hierarchy
> - Burndown vs velocity vs cumulative flow
> - A JQL query example
> - Tool is secondary to practices (don't let metrics become targets)

---

## 12. Scaled Agile (SAFe basics)
> 🔴 Tier 1 · _Tracker hint:_ Agile Release Train; Program Increment; PI Planning

### Definition
**SAFe (Scaled Agile Framework)** coordinates many Agile teams in large enterprises.

- **Agile Release Train (ART):** a long-lived team of Agile teams (about 50–125 people) that plans, commits and delivers together, aligned to a value stream.
- **Program Increment (PI):** a fixed timebox, typically 8–12 weeks (commonly 10: four 2-week iterations plus an Innovation and Planning iteration).
- **PI Planning:** a two-day face-to-face (or virtual) event where all ART teams plan the next PI, identify dependencies and risks, set **PI Objectives**, and produce a **program board**; confidence vote (fist of five).
- Roles: **Release Train Engineer (RTE)**, **Product Management**, **System Architect**, **Business Owners**.
- **Portfolio level:** Lean Portfolio Management, Epics, strategic themes, and **WSJF** prioritisation $=\frac{\text{Cost of delay}}{\text{Job size}}$.
- Competencies: team and technical agility, DevOps, business agility; alternatives: LeSS, Nexus, Scrum@Scale, Spotify model.

Criticism: can feel heavy and process-driven versus the original Agile values.

### Example
A large Indian bank's digital division has 8 Scrum teams (about 80 people) forming one ART. Every 10 weeks they hold PI Planning, agree on objectives like "launch the digital loan journey", map dependencies (core banking, risk, security teams) and commit to PI Objectives with business value scores.

### In the news
See news box. 79% doing more with fewer resources and 76% needing to show impact are the pressures that push large organisations toward scaled frameworks and portfolio-level metrics.

### Interview angle
> [!question] How it is asked
> "How do you coordinate multiple Agile teams with dependencies?"

> [!tip] Strong answer includes
> - ART, PI, PI Planning and roles
> - Dependency and risk management (program board)
> - Pros and cons versus lighter approaches
> - When not to scale (single team, small organisation)

---

## 13. ⭐ Advanced: Flow Metrics, Little's Law and Probabilistic Forecasting
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Modern Agile teams complement velocity with **flow metrics**:

- **Lead time:** request to delivery; **Cycle time:** start of work to done; **Throughput:** items completed per period; **WIP:** items in progress; **Flow efficiency** = active time / total elapsed time.
- **Little's Law:** $\text{WIP}=\text{Throughput}\times\text{Cycle time}$ (stable system). Reducing WIP shortens cycle time without working harder.
- **Cumulative flow diagram (CFD):** band widths show WIP; widening bands signal bottlenecks.
- **Probabilistic forecasting:** run Monte Carlo simulation over historical throughput to give "85% chance we finish 30 items by date X" rather than a single date.

Percentile-based **Service Level Expectations**: "85% of items finish within 8 days." Metrics should drive learning, not rankings.

### Example
Team throughput is 5 items per week with 20 items in progress: cycle time = 20/5 = 4 weeks. Cutting WIP to 10 (same throughput) gives cycle time = 10/5 = **2 weeks**, so customers get items twice as fast.

### In the news
See news box. Pressure to prove Agile's business impact (76%) is pushing teams toward outcome and flow measures such as lead time rather than velocity alone.

### Interview angle
> [!question] How it is asked
> "How would you reduce delivery time without adding people?"

> [!tip] Strong answer includes
> - Little's Law and WIP limits
> - Finds bottlenecks with a CFD and flow efficiency
> - Percentile-based forecasts
> - Cautions against gaming metrics

---

## 14. ⭐ Advanced: Agile in Non-Software Contexts and Hybrid Project Management
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Agile is used beyond software: marketing, HR, operations, supply chain and hardware. **Hybrid** approaches combine **waterfall** (stage gates, fixed baseline for regulated or physical work) with **Agile** (iterative delivery inside stages). **PMI's PMBOK 7** and the **PMI-ACP** certification recognise adaptive and predictive methods.

Choose by **uncertainty and cost of change**: high requirements uncertainty and cheap change → Agile; stable scope, high cost of change (construction, plant commissioning) → predictive; mixed → hybrid (e.g., fixed hardware design milestones with Agile software and sprint reviews). Key adaptations: time-boxed iterations, visual boards, regular reviews with the customer, and backlog of deliverables. Agile **earned value** variants track burn-up against scope.

Pitfalls: "Agile in name only" (stand-ups with command-and-control), ignoring contracts and governance (use fixed price per sprint, change-friendly contracts), and lacking a decision-making PO.

### Example
A plant expansion project: civil works use a Gantt baseline (waterfall); the MES (manufacturing execution system) software runs in 2-week sprints with plant users in the review; both feed a monthly steering committee with a combined milestone plan.

### In the news
See news box. 74% hybrid or custom approaches show that mixed models are now the norm, not the exception.

### Interview angle
> [!question] How it is asked
> "How would you manage a project with both fixed deadlines and uncertain requirements?"

> [!tip] Strong answer includes
> - Criteria for choosing predictive, Agile or hybrid
> - Governance and contracting that tolerate change
> - Metrics for both schedule and value
> - A concrete example and risk of "fake Agile"

---
## 🔗 Go deeper: expansion notes
- [[167 PRDs, Stakeholder Management & Product Operations|PRDs, Stakeholder Management & Product Operations]]
