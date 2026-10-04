---
tags: [project-management, tier1]
area: Project Management
topic: "Project Management Interview Questions & Numericals"
tier: Tier 1
roles: Project Manager
status: complete
subtopics: 14
---
# Project Management Interview Questions & Numericals

⬅ [[170 Programme, Portfolio & PMO Management]] · [[_Index - Project Management|Project Management]]

> **Area:** Project Management · **Priority:** 🔴 Tier 1 · **Target roles:** Project Manager

## Sub-topics in this note
1. [[#1. Scope and Requirements Questions (Q1 to Q7)]]
2. [[#2. Schedule Questions (Q8 to Q14)]]
3. [[#3. Cost and Budget Questions (Q15 to Q21)]]
4. [[#4. Risk Management Questions (Q22 to Q28)]]
5. [[#5. Stakeholder and Communication Questions (Q29 to Q34)]]
6. [[#6. Agile and Hybrid Questions (Q35 to Q41)]]
7. [[#7. Behavioural Questions (Q42 to Q47)]]
8. [[#8. Scenario Questions]]
9. [[#9. Numericals: CPM, Float and Lags (N1 to N3)]]
10. [[#10. Numericals: Crashing and Optimal Duration (N4 to N5)]]
11. [[#11. Numericals: PERT and Three-Point Estimates (N6 to N9)]]
12. [[#12. Numericals: Earned Value and Forecasting (N10 to N13)]]
13. [[#13. Numericals: Risk, EMV and Decision Trees (N14 to N15)]]
14. [[#14. ⭐ Advanced: Formula Sheet, Answer Frameworks and Timing Tricks]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Overruns and business acumen keep PM interviews practical
> **India's central project overruns (MoSPI report for July 2026, published 27 August 2026).** Of **1,775 central projects of Rs 150 crore and above**, original cost was Rs 33,70,138 crore and revised cost Rs 37,10,642 crore, a cumulative overrun of **Rs 3,40,504 crore** (about 10%). Expenditure was 51.91% of revised cost, and 675 projects (38%) had crossed 80% physical completion. Interviewers in infrastructure, EPC and consulting use exactly this kind of data to ask "why do projects overrun and how would you control it?" ([Swarajya, citing MoSPI](https://swarajyamag.com/news-brief/indias-1775-central-infrastructure-projects-face-rs-34-lakh-crore-cost-overrun))
>
> **Business acumen (PMI Pulse of the Profession 2025).** PMI reported 66% of project professionals with moderate business acumen, 18% high and 16% low, and called business acumen the critical differentiator for delivering project success. Expect questions that link a project to profit, benefits and strategy, not only to schedule and cost. ([PMI](https://www.pmi.org/learning/thought-leadership/boosting-business-acumen))
>
> **PMBOK Guide 8th edition (November 2025).** Reported as restructured into 6 principles and 7 performance domains (Governance, Scope, Schedule, Finance, Stakeholders, Resources, Risk), keeping the classic tools (CPM, EVM, risk analysis) while stressing value, accountable leadership and empowered teams. ([BrainBOK comparison](https://www.brainbok.com/blog/pmp/pmbok-guide-7th-vs-8th-edition-what-has-changed), [Learning Tree summary](https://www.learningtree.com/blog/pmbok-guide-8th-edition-whats-new/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Scope and Requirements Questions (Q1 to Q7)
> 🔴 Tier 1 · _Key points:_ WBS, baseline, creep, change control, validation, MoSCoW

### Definition
Scope questions test whether the candidate defines "done" before building and controls change without being rigid. The reference tools are in [[037 PM Fundamentals & Lifecycle]] and [[038 PMBOK Knowledge Areas]]. Answer structure: **definition, tool, example, pitfall**. Keep each answer to 30 to 45 seconds.

### Example
**Q1. What is the difference between product scope and project scope?** Product scope is the features and functions of the deliverable (a WMS with 5 modules); project scope is the work needed to deliver it (analysis, build, test, training, migration).

**Q2. What is a WBS, and how do you know it is good?** A hierarchical decomposition of total scope into deliverable-oriented work packages. Good WBS follows the **100% rule** (every level covers all the work of its parent, nothing extra), has mutually exclusive elements, and ends in packages that can be estimated, assigned and tracked (often 8 to 80 hours or a few weeks, as a rule of thumb).

**Q3. What is scope creep and how do you prevent it?** Uncontrolled additions without adjusting time, cost or resources. Prevent it by a signed scope baseline (scope statement + WBS + WBS dictionary), a change control process (request, impact analysis, CCB decision, baseline update), and a habit of answering "yes, and here is the impact" instead of "no".

**Q4. Scope creep versus gold plating?** Creep is added by the customer or stakeholders; gold plating is added by the team beyond requirements, without approval. Both break the baseline; gold plating adds cost and risk without value.

**Q5. How do you prioritise requirements when everything is "high priority"?** Use **MoSCoW** (must, should, could, won't), score by value versus effort or RICE/WSJF ([[034 Prioritization Frameworks]]), tie each requirement to a business objective, and ask the sponsor to trade: "to add this, which moves out?".

**Q6. What is a requirements traceability matrix?** A table linking each requirement to its source, design element, test case and deliverable, so that nothing is missed and the impact of a change can be found quickly.

**Q7. Validate Scope versus Control Quality?** Control Quality checks that deliverables meet specifications (internal, by the team). Validate Scope is formal acceptance by the customer or sponsor. A deliverable can pass quality and still be rejected if it solves the wrong problem.

### In the news
See news box. Many Indian public-project overruns trace to scope changes after award (utility shifting, design revisions), which is why scope baselines and change control are the first thing interviewers probe.

### Interview angle
> [!question] How it is asked
> "A client keeps asking for small additions every week. What do you do?"

> [!tip] Strong answer includes
> - Acknowledge value, log every request, run an impact analysis (time, cost, risk, resources)
> - Route through change control with the sponsor, never silently absorb
> - Offer options: swap scope, add budget or time, defer to phase 2
> - Prevention: clear baseline, acceptance criteria, regular scope reviews

---
## 2. Schedule Questions (Q8 to Q14)
> 🔴 Tier 1 · _Key points:_ Critical path, float, compression, leveling, estimation, critical chain

### Definition
Schedule questions mix definitions with decision-making under deadline pressure. Always mention the **critical path** and the **trade-off** (cost, risk, quality) of any recovery action. Background: [[039 Scheduling Tools (CPM-PERT-Gantt)]].

### Example
**Q8. What is the critical path and can it change?** The longest path through the network; it sets the minimum project duration and has zero (or the lowest) total float. It can shift when other paths slip, when durations are re-estimated or when logic changes, so recompute at every update.

**Q9. Total float vs free float?** Total float is the delay an activity can have without delaying the project end ($LS - ES$). Free float is the delay without delaying any successor's early start. Total float is shared along a path; free float belongs to the activity.

**Q10. Crashing vs fast tracking?** Crashing adds resources to critical activities to shorten duration (cost up). Fast tracking overlaps activities that were sequential (risk and rework up). Crash lowest cost-slope activities first; fast track only where dependencies are soft. Neither reduces scope.

**Q11. Resource levelling vs smoothing?** Levelling resolves over-allocation and may extend the finish date; smoothing adjusts activities only within their float so the finish date is unchanged.

**Q12. How do you estimate durations when you have no history?** Three-point (PERT) estimates $\frac{O+4M+P}{6}$ from SMEs, analogous estimates from similar projects, bottom-up by work package, parametric (for example metres of pipe per crew-day), with a documented range and assumptions; refine with rolling-wave planning.

**Q13. What is critical chain?** Goldratt's method that removes padding from task estimates, protects the chain with a **project buffer** and **feeding buffers**, and limits multitasking. It targets student syndrome and Parkinson's law (work expands to fill time).

**Q14. A project is 3 weeks behind on a 6-month plan. What do you do?** Check whether the delay is on the critical path, find root cause, re-forecast with the real velocity, evaluate compression (crash, fast track, scope trade) with costs and risks, present options to the sponsor and re-baseline only with approval.

### In the news
See news box. Schedule slips drive the MoSPI cost overrun; time-related delay and cost are linked, which is why PMs compute cost of delay and not only days late.

### Interview angle
> [!question] How it is asked
> "The client moves the go-live 4 weeks earlier. Can you do it?"

> [!tip] Strong answer includes
> - Do not say "yes" or "no" immediately; check critical path and options
> - Crash and fast-track options with cost and risk quantified
> - Scope, quality or resource trade-offs offered
> - Risk of burnout and defects; get approval in writing

---
## 3. Cost and Budget Questions (Q15 to Q21)
> 🔴 Tier 1 · _Key points:_ Estimation accuracy, baseline, contingency vs management reserve, EVM, contracts

### Definition
Cost answers need formulas plus judgement. Reference: [[042 Cost & Budget Management]] and contract types in [[168 Project Procurement, Contracts & EPC Delivery]].

### Example
**Q15. Contingency reserve vs management reserve?** Contingency covers identified risks (known unknowns), is in the cost baseline and is controlled by the PM. Management reserve covers unidentified work (unknown unknowns), sits outside the baseline in the project budget, and needs management approval.

**Q16. How accurate are estimates, and how does it change?** Rough order of magnitude early (PMBOK range about -25% to +75%), budget estimates (about -10% to +25%), definitive (about -5% to +10%); accuracy improves as scope is defined. Always state the range.

**Q17. Explain CPI and SPI with a one-line interpretation.** $CPI = EV/AC$: value earned per rupee spent. $SPI = EV/PV$: value earned per rupee of work planned. Below 1 is bad for both.

**Q18. How do you forecast EAC?** If the past will continue: $BAC/CPI$. If variance was a one-off: $AC + (BAC-EV)$. If cost and schedule both drive remaining cost: $AC + \frac{BAC-EV}{CPI \times SPI}$. If the estimate was flawed: $AC +$ bottom-up ETC.

**Q19. What is TCPI?** The efficiency needed for the remaining work to hit a target: $TCPI = \frac{BAC-EV}{BAC-AC}$. Above about 1.1 the target is unrealistic.

**Q20. Fixed-price vs time-and-materials vs cost-plus?** Fixed-price puts cost risk on the seller (good for clear scope); T&M for unclear scope with a cap; cost-plus reimburses cost plus fee, used where scope is uncertain (some defence and R&D); incentives (target cost with share ratio) align both sides.

**Q21. You are 15% over budget at the midpoint. What do you do?** Analyse root causes (rework, price escalation, scope), compute EAC under realistic assumptions, identify recovery levers (scope, rate, vendors), tell the sponsor early with options, and never hide the variance by re-baselining without approval.

### In the news
See news box. A 10% average overrun in India's central project portfolio is a reminder that "contingency of 5%" is rarely enough for infrastructure; interviewers test whether you size reserves from risk (EMV) rather than a habit.

### Interview angle
> [!question] How it is asked
> "Your CPI is 0.85. What does it mean and what do you do?"

> [!tip] Strong answer includes
> - Interpretation in rupee terms: each ₹1 spent earns ₹0.85 of planned value
> - EAC calculation with a stated assumption
> - Root cause (productivity, scope, vendor price) and corrective action
> - Early escalation with options and TCPI check

---
## 4. Risk Management Questions (Q22 to Q28)
> 🔴 Tier 1 · _Key points:_ Risk vs issue, P-I, EMV, responses, reserves, residual and secondary risk

### Definition
Risk answers should show a **process** (identify, analyse, plan response, monitor) and a **number** (EMV or P × I). Reference: [[040 Risk & Stakeholder Management]] and [[150 Decision Analysis & Simulation]].

### Example
**Q22. Risk vs issue?** A risk is a future uncertain event; an issue is a risk that has occurred (or a current problem). Risks are managed by plans and reserves, issues by action and escalation.

**Q23. How do you prioritise risks?** Probability × impact on defined scales, then urgency and proximity; top risks go to quantitative analysis (EMV, Monte Carlo).

**Q24. Compute EMV of a risk.** $EMV = P \times I$. Supplier strike: 30% × (-₹50 lakh) = -₹15 lakh. Opportunities are positive. Sum to size contingency.

**Q25. List the response strategies.** Threats: avoid, transfer, mitigate, accept (active or passive), escalate. Opportunities: exploit, share, enhance, accept, escalate.

**Q26. Residual vs secondary risk?** Residual risk remains after a response; secondary risk is new risk created by the response (for example outsourcing a task creates vendor-dependency risk).

**Q27. Contingency plan vs fallback plan vs workaround?** Contingency plan is a pre-planned response when a trigger occurs; fallback is the plan B if the response fails; a workaround is an unplanned response to a risk that has occurred.

**Q28. How would you handle a risk the team keeps ignoring?** Assign an owner, set a trigger and a date, show EMV in rupees, escalate to the sponsor if exposure exceeds threshold, and track it on the risk burn-down.

### In the news
See news box. Overruns of about 10% across 1,775 projects show systemic under-pricing of risk; reference-class forecasting (use outcomes of similar past projects) is the interview-ready way to correct optimism bias.

### Interview angle
> [!question] How it is asked
> "What are the top three risks on your last project and what did you do?"

> [!tip] Strong answer includes
> - Risks stated in cause-event-effect form with P, I and owner
> - Response chosen by cost versus exposure
> - Reserve tied to EMV, tracked and drawn down transparently
> - Actual outcome and lesson

---
## 5. Stakeholder and Communication Questions (Q29 to Q34)
> 🔴 Tier 1 · _Key points:_ Power-interest grid, engagement, channels, escalation, RACI

### Definition
Stakeholder answers should show diagnosis (who, power, interest, attitude), a plan (engagement and frequency) and a feedback loop. See [[040 Risk & Stakeholder Management]], [[167 PRDs, Stakeholder Management & Product Operations]] and [[169 Project Team Leadership, Conflict & Team Development]].

### Example
**Q29. How do you manage a senior stakeholder who is hostile to the project?** Meet one-to-one to find interests and fears, involve them in decisions that affect them, share early wins and data, agree a communication rhythm, and use the sponsor only if direct engagement fails.

**Q30. Power-interest grid, four strategies?** High power, high interest: manage closely; high power, low interest: keep satisfied; low power, high interest: keep informed; low power, low interest: monitor.

**Q31. How many communication channels in a team of 10?** $\frac{n(n-1)}{2} = \frac{10 \times 9}{2} = 45$. Use it to argue for structure, a communication plan and smaller teams.

**Q32. What does a communication plan contain?** Audience, information, purpose, format, frequency, owner and escalation path; the plan is reviewed when stakeholders change.

**Q33. RACI in one line?** Responsible (does), Accountable (one owner), Consulted (two-way), Informed (one-way); exactly one A per task.

**Q34. How do you deliver bad news to a sponsor?** Early, with facts, impact, options and your recommendation, in person or by call before email; never surprise the sponsor in a steering committee.

### In the news
See news box. PMI's finding that business acumen differentiates success implies that explaining projects in business terms (value, risk, benefits) is a stakeholder skill, not just a technical one.

### Interview angle
> [!question] How it is asked
> "Two stakeholders want opposite things. How do you decide?"

> [!tip] Strong answer includes
> - Interests behind positions; link both to the project objective
> - Decision criteria agreed with the sponsor; escalation where authority sits
> - Document the decision and communicate the reasoning
> - Relationship repair afterwards

---
## 6. Agile and Hybrid Questions (Q35 to Q41)
> 🔴 Tier 1 · _Key points:_ Scrum roles, velocity, DoD, hybrid, when agile fails, PM role in agile

### Definition
Show that you understand when each approach fits and how a project manager adds value in an agile setting. See [[041 Agile Project Management]] and [[032 Agile & Scrum Framework]].

### Example
**Q35. Agile vs waterfall, when to use which?** Waterfall for stable scope and regulated, physical work (plant construction); agile for uncertain requirements and fast feedback (software). Most real projects are hybrid: predictive for the physical or contractual frame, agile for software components.

**Q36. Scrum roles and events?** Roles: Product Owner (value, backlog), Scrum Master (process, impediments), Developers. Events: sprint, sprint planning, daily scrum, review, retrospective.

**Q37. Velocity: forecast the finish.** Backlog 210 points, last three sprints 28, 32, 30 (mean 30). Forecast $210/30 = 7$ sprints (14 weeks for 2-week sprints); give a range using the lowest and highest velocities (28 to 32: 6.6 to 7.5 sprints).

**Q38. Definition of Done vs acceptance criteria?** DoD is the team-wide quality standard for every item (tested, reviewed, documented). Acceptance criteria are specific to a story.

**Q39. What does a project manager do in a Scrum team?** Not a Scrum role, but the PM handles budget, vendors, cross-team dependencies, risk, stakeholder reporting and release coordination; a PM who commands the team undermines self-organisation.

**Q40. How do you handle scope change mid-sprint?** Do not change the sprint goal; the PO may cancel the sprint in extreme cases; new items go to the backlog and are prioritised for the next sprint.

**Q41. Kanban vs Scrum?** Kanban is flow-based with WIP limits and no fixed iteration; Scrum is timeboxed with commitments. Use Kanban for support or operations work with continuous arrival.

### In the news
See news box. PMBOK 8's empowered-team principle and PMI's hybrid findings (see [[041 Agile Project Management]]) mean interviewers expect hybrid fluency rather than methodology loyalty.

### Interview angle
> [!question] How it is asked
> "Can agile work for a fixed-price, fixed-deadline contract?"

> [!tip] Strong answer includes
> - Yes with adaptation: fix the outcome and date, flex scope within the backlog by priority
> - Contract with change mechanisms and agreed definition of done
> - Early visible increments, regular demos, transparent burn-up
> - Honest about the risk when scope is also fixed

---
## 7. Behavioural Questions (Q42 to Q47)
> 🔴 Tier 1 · _Key points:_ STAR, conflict, failure, pressure, influence, ethics

### Definition
Use **STAR** (situation, task, action, result) with a number in the result and one lesson. Prepare 5 stories reusable across questions (see [[049 STAR Stories — Leadership & Conflict]], [[052 Strengths, Weaknesses, Failures]] and [[163 PM Interview Types & Answer Frameworks]]). Below, each item gives the model answer's skeleton.

### Example
**Q42. Tell me about a project that failed or missed its target.** Skeleton: context and goal; your role; what went wrong and your share of the cause; the action you took (re-plan, escalation); outcome (for example 3 weeks late, 8% over); concrete change you made afterwards.

**Q43. Describe a conflict in your team.** Skeleton: facts, interests of each side, private conversations, collaborative solution, result and relationship after.

**Q44. Tell me about working under a tight deadline.** Skeleton: prioritised by critical path and value, cut non-essential scope with sponsor approval, daily check-ins, protected quality, delivered on time with a measured outcome.

**Q45. A time you influenced without authority.** Skeleton: understood the other party's goals, used data and a small pilot, built allies, won commitment; result in numbers.

**Q46. An ethical dilemma.** Skeleton: the pressure (for example to report green status), the principle (transparency, accuracy), the action (raised it with the sponsor with a recovery plan), the result.

**Q47. Why project management?** Link ability to structure ambiguity, deliver across stakeholders and accountability for outcomes with evidence from your internship or projects (see [[050 Why Consulting - PM - Operations-]]).

### In the news
See news box. With overruns of about 10% on average in India's central projects, stories that show how you spotted a slip early and corrected it are more convincing than stories of heroic late-night finishes.

### Interview angle
> [!question] How it is asked
> "Tell me about a time you had to deliver bad news."

> [!tip] Strong answer includes
> - One specific story, 90 seconds, with numbers
> - Your own action (use "I", not "we" throughout)
> - Honest account of what went wrong
> - A lesson that you actually changed in later work

---
## 8. Scenario Questions
> 🔴 Tier 1 · _Key points:_ Diagnose, quantify, options, recommend, communicate

### Definition
Scenario answers follow: **(1) clarify, (2) quantify, (3) options with trade-offs, (4) recommend, (5) communicate and follow up.** Always compute an index or EMV if numbers are given.

### Example
**Q48. After 4 months, 40% of the budget is spent and 20% of the work is done.** $CPI = EV/AC = 20/40 = 0.5$. If this continues, $EAC = BAC/CPI = 100/0.5 = 200$ (double). If the cause was a one-off, $EAC = AC + (BAC-EV) = 40 + 80 = 120$. $TCPI = (100-20)/(100-40) = 1.33$ (unrealistic). Recommendation: find the cause in a week, present both EACs to the sponsor, ask for a decision to re-scope, add funding or stop.

**Q49. The key vendor fails 6 weeks before go-live.** Assess critical path impact, invoke contract remedies, activate fallback (second vendor, in-house build for core features), phased release, inform the client with a recovery plan.

**Q50. Testing finds a critical defect one week before go-live.** Severity and impact analysis, fix or workaround, go/no-go criteria agreed with the sponsor, limited rollout (pilot site), rollback plan; never ship silently.

**Q51. The sponsor wants a 3-week earlier date.** Ask why, show critical path, offer: crash (extra team at ₹X lakh), fast track (rework risk), reduce scope (MoSCoW), phase release; decision by sponsor with risk accepted in writing.

**Q52. A statutory approval (fire NOC or pollution consent) is delayed.** Identify the dependency owner, escalate through channels, re-sequence non-dependent work, use float, add the delay to the risk register, and inform the client under contract relief (extension of time).

**Q53. Two projects need the same key engineer.** Check each project's priority and critical path with the portfolio owner, quantify cost of delay for each, reallocate or hire, document the decision (see [[170 Programme, Portfolio & PMO Management]] for capacity management).

**Q54. The team is demotivated after a failed release.** Run a blameless retrospective, recognise effort, simplify the next goal, remove blockers, check workload and engagement (see [[169 Project Team Leadership, Conflict & Team Development]]).

### In the news
See news box. In the MoSPI portfolio, the 675 projects beyond 80% physical completion can still be over budget; scenario questions like Q48 train you to read cost and progress together.

### Interview angle
> [!question] How it is asked
> "You join a project that is red on every metric. What do you do in your first two weeks?"

> [!tip] Strong answer includes
> - Listen first, gather facts, validate baseline and data
> - Rank problems by impact (critical path, EAC, top risks)
> - Quick wins and a recovery plan with options and owners
> - Re-set expectations with the sponsor and report weekly

---
## 9. Numericals: CPM, Float and Lags (N1 to N3)
> 🔴 Tier 1 · _Key points:_ Forward pass, backward pass, float, SS lag

### Definition
**Forward pass:** $ES = \max(EF_{pred})$, $EF = ES + d$. **Backward pass:** $LF = \min(LS_{succ})$, $LS = LF - d$. **Total float** $= LS - ES$; **free float** $= \min(ES_{succ}) - EF$. Critical path: zero total float. Method in [[039 Scheduling Tools (CPM-PERT-Gantt)]].

### Example
**N1. Network (durations in days):** A 3 (start), B 4 (after A), C 2 (after A), D 5 (after B), E 4 (after B and C), F 3 (after D), G 6 (after D and E), H 2 (after F and G). Find project duration and critical path.

| Act | d | ES | EF | LS | LF | TF | FF |
|---|---|---|---|---|---|---|---|
| A | 3 | 0 | 3 | 0 | 3 | 0 | 0 |
| B | 4 | 3 | 7 | 3 | 7 | 0 | 0 |
| C | 2 | 3 | 5 | 6 | 8 | 3 | 2 |
| D | 5 | 7 | 12 | 7 | 12 | 0 | 0 |
| E | 4 | 7 | 11 | 8 | 12 | 1 | 1 |
| F | 3 | 12 | 15 | 15 | 18 | 3 | 3 |
| G | 6 | 12 | 18 | 12 | 18 | 0 | 0 |
| H | 2 | 18 | 20 | 18 | 20 | 0 | 0 |

Project duration **20 days**; critical path **A-B-D-G-H** (3+4+5+6+2 = 20). Near-critical: A-B-E-G-H = 19 days; A-B-D-F-H = 17; A-C-E-G-H = 17.

**N2. Using N1: how late can C finish without delaying the project, and what happens if it slips 3 days?** Total float of C = 3 (LS 6 - ES 3). Free float = 2 (E can start at day 7, C ends at day 5). If C slips 3 days, it ends at day 8, E starts at 8 (1 day late; E's own float of 1 absorbs it) and the project still ends at day 20. If C slips 4 days, the project ends at day 21. Message: float consumed by one activity is not available to its successors.

**N3. Precedence with lag.** A (5 days). B (6 days) can start 2 days after A starts (SS+2). C (4 days) starts after A finishes (FS). D (3 days) starts after both B and C finish.
Forward: A 0 to 5; B ES = 0 + 2 = 2, EF 8; C ES 5, EF 9; D ES = max(8, 9) = 9, EF 12. Project = **12 days**. Backward: D LS 9; C LS 5 (float 0); B LF 9, LS 3 (float 1); A LS 0. Critical path **A-C-D**; B has float 1.

### In the news
See news box. Float analysis is how a PM judges whether a delay in land handover or utility shifting threatens the end date or is absorbed.

### Interview angle
> [!question] How it is asked
> "Here is a network. What is the critical path and which activity can slip the most?"

> [!tip] Strong answer includes
> - Forward then backward pass in a table; state duration and critical path
> - Total and free float with the meaning of each
> - Near-critical paths flagged as risk
> - Takeaway: where to focus management attention

---
## 10. Numericals: Crashing and Optimal Duration (N4 to N5)
> 🔴 Tier 1 · _Key points:_ Cost slope, crash step by step, direct plus indirect cost

### Definition
$$\text{Cost slope} = \frac{\text{Crash cost} - \text{Normal cost}}{\text{Normal duration} - \text{Crash duration}}$$

Procedure: crash the **cheapest-slope critical activity** with remaining capacity by one day, recompute all path lengths, repeat; when several paths are critical, shorten all of them (a common activity, or the cheapest combination). Total cost = direct (normal plus crash cost) + indirect (overhead per day × duration) (+ penalty). Background: [[039 Scheduling Tools (CPM-PERT-Gantt)]] (crashing sub-topic).

### Example
**N4. Crash the N1 network.** Data (₹ thousand; normal duration, crash duration, normal cost, crash cost): A 3/2, 30/36; B 4/3, 40/52; C 2/1, 10/14; D 5/3, 60/90; E 4/3, 32/38; F 3/2, 24/30; G 6/4, 70/94; H 2/1, 20/30. Slopes (₹k/day): A 6, B 12, C 4, D 15, E 6, F 6, G 12, H 10. Normal cost = 286.

| Step | Crash | Slope | Duration | Total direct cost |
|---|---|---|---|---|
| 0 | none | - | 20 | 286 |
| 1 | A by 1 | 6 | 19 | 292 |
| 2 | H by 1 | 10 | 18 | 302 |
| 3 | B by 1 | 12 | 17 | 314 |
| 4 | G by 1 | 12 | 16 | 326 |
| 5 | G by 1 | 12 | 15 | 338 |
| 6 | D by 1 | 15 | 14 | 353 |
| 7 | D by 1 and E by 1 | 15 + 6 = 21 | 13 | 374 |

Reading the steps: at step 1 only A-B-D-G-H is critical and A has the lowest slope on it (6). At step 2 A is at its crash limit, so H (10) beats B (12), G (12) and D (15). At step 3 B and G tie at 12 (B chosen; G gives the same cost). Step 7: both A-B-D-G-H and A-B-E-G-H are 14 days, so D and E must both be crashed (21). The minimum possible duration is **13 days** at ₹374k, confirmed by checking all combinations.

**N5. Optimal duration with indirect cost ₹14k/day.** Total cost = direct + 14 × duration:

| Duration | 20 | 19 | 18 | 17 | 16 | 15 | 14 | 13 |
|---|---|---|---|---|---|---|---|---|
| Direct | 286 | 292 | 302 | 314 | 326 | 338 | 353 | 374 |
| Indirect | 280 | 266 | 252 | 238 | 224 | 210 | 196 | 182 |
| **Total** | 566 | 558 | 554 | 552 | 550 | **548** | 549 | 556 |

Minimum total cost = **₹548k at 15 days**: crashing further adds more direct cost than it saves in overhead. A penalty or a bonus for early completion would add a term to this table and can move the optimum.

### In the news
See news box. Crashing only works where more resources can actually shorten work; large public projects delayed by land and approvals cannot be crashed back, which is why the cost of delay must be weighed against crash cost.

### Interview angle
> [!question] How it is asked
> "Reduce the project by 4 days at minimum cost. Which activities do you crash and what does it cost?"

> [!tip] Strong answer includes
> - Slopes computed first; crash critical path only, cheapest first, check limits
> - Recompute paths after each step; shorten all critical paths together
> - Total cost curve with indirect cost and the optimum
> - Mention alternatives: fast tracking, scope trade, adding shift

---
## 11. Numericals: PERT and Three-Point Estimates (N6 to N9)
> 🔴 Tier 1 · _Key points:_ Expected time, variance, Z probability, merge bias, cost at confidence

### Definition
$$t_e = \frac{O + 4M + P}{6}, \qquad \sigma^2 = \left(\frac{P - O}{6}\right)^2, \qquad Z = \frac{T - \mu_{path}}{\sigma_{path}}$$

Path mean = sum of $t_e$; path variance = sum of variances (independent activities). Probability from the standard normal ([[087 Probability Fundamentals]], [[088 Probability Distributions]]). Useful $Z$ values: 1.28 for 90%, 1.645 for 95%.

### Example
**N6. Critical path with O, M, P (days):** Design (4, 6, 14), Procure (8, 10, 18), Install (6, 8, 10), Test (2, 4, 6), Train (3, 4, 11).

| Activity | $t_e$ | Variance |
|---|---|---|
| Design | (4+24+14)/6 = 7.0 | (10/6)² = 2.78 |
| Procure | (8+40+18)/6 = 11.0 | (10/6)² = 2.78 |
| Install | (6+32+10)/6 = 8.0 | (4/6)² = 0.44 |
| Test | (2+16+6)/6 = 4.0 | (4/6)² = 0.44 |
| Train | (3+16+11)/6 = 5.0 | (8/6)² = 1.78 |

Mean = **35 days**, variance = 8.22, $\sigma = 2.87$.

**N7. Probability of finishing in 38 days; date for 90% confidence.** $Z = (38-35)/2.87 = 1.05$, so $P \approx 85\%$. For 32 days $Z = -1.05$, $P \approx 15\%$. For 90%: $35 + 1.28 \times 2.87 = 38.7$ days, about **39 days**. A committed date of 35 days has only a 50% chance.

**N8. Merge bias.** Two parallel paths: Path 1 mean 30, $\sigma$ 3; Path 2 mean 29, $\sigma$ 4. Probability each finishes within 33 days: $\Phi(1) = 84.1\%$ and $\Phi(1) = 84.1\%$. Probability the project (both) finishes in 33 days = $0.841 \times 0.841 = 70.8\%$ (independence assumed). Analysing only the longest path overstates confidence; Monte Carlo handles this.

**N9. Cost at confidence (₹ lakh).** Work packages (O, M, P): Civil (90, 100, 130), Racking (40, 48, 70), Electrical (25, 30, 41), IT (30, 36, 60). Expected: 103.33 + 50.33 + 31.00 + 39.00 = **223.67**. Variance: 44.44 + 25.00 + 7.11 + 25.00 = 101.56, $\sigma = 10.08$. Sum of most-likely values = 214, so the "most likely" total is optimistic by 9.67. Budget at 90% = $223.67 + 1.28 \times 10.08 = 236.6$ lakh; at 95% = $223.67 + 1.645 \times 10.08 = 240.2$ lakh. Contingency at 90% above the expected value = about ₹12.9 lakh.

### In the news
See news box. The 90% budget in N9 sits 10.5% above the sum of most-likely values (and 5.8% above the expected value), similar in size to MoSPI's roughly 10% average overrun: honest three-point ranges produce budgets close to what projects actually cost.

### Interview angle
> [!question] How it is asked
> "What is the probability this project finishes in 38 days?" or "What date would you commit to?"

> [!tip] Strong answer includes
> - Expected time and variance per activity; add along the path
> - Z-score and probability with correct reading of the table
> - Commit at a chosen confidence (P80 or P90), not the mean
> - Limitations: independence assumption, merge bias, beta approximation

---
## 12. Numericals: Earned Value and Forecasting (N10 to N13)
> 🔴 Tier 1 · _Key points:_ CPI, SPI, EAC variants, TCPI, WBS roll-up, earned schedule

### Definition
$$CV = EV - AC, \quad SV = EV - PV, \quad CPI = \frac{EV}{AC}, \quad SPI = \frac{EV}{PV}$$
$$EAC_1 = \frac{BAC}{CPI}, \quad EAC_2 = AC + (BAC - EV), \quad EAC_3 = AC + \frac{BAC - EV}{CPI \times SPI}, \quad TCPI = \frac{BAC - EV}{BAC - AC}$$
Interpretation and when to use each EAC: [[042 Cost & Budget Management]].

### Example
**N10. BAC ₹500 lakh, PV 250, EV 200, AC 230.** $CV = -30$, $SV = -50$, $CPI = 200/230 = 0.870$, $SPI = 200/250 = 0.80$. The project is over budget and behind schedule.

**N11. EAC variants for N10.**
- $EAC_1 = 500 / 0.8696 = ₹575$ lakh, $ETC = 345$, $VAC = -75$.
- $EAC_2 = 230 + (500 - 200) = ₹530$ lakh, $ETC = 300$, $VAC = -30$ (variance was a one-off).
- $EAC_3 = 230 + 300 / (0.8696 \times 0.8) = 230 + 431.25 = ₹661.25$ lakh, $VAC = -161.25$ (both indices keep applying; typically the pessimistic view).
- $TCPI_{BAC} = 300 / 270 = 1.11$: remaining work must run at 11% better efficiency than planned to finish at BAC. Reaching $EAC_2$ would need $TCPI = 300/300 = 1.0$.

**N12. WBS roll-up (₹ lakh).** Budget (BAC), planned %, actual % complete, AC: Civil 120, 100%, 90%, 115; Racking 80, 75%, 60%, 52; Electrical 60, 50%, 30%, 20; Software 90, 20%, 25%, 25.
PV = 120 + 60 + 30 + 18 = 228. EV = 108 + 48 + 18 + 22.5 = 196.5. AC = 212. BAC = 350.
$CPI = 196.5/212 = 0.927$, $SPI = 196.5/228 = 0.862$, $EAC = 350/0.927 = ₹377.6$ lakh. Insight: only Software is ahead of schedule (SPI = 1.25) while Electrical is the laggard (SPI = 0.60); the aggregate hides this, so analyse by package. EVM also assumes credible %-complete reporting (use 0/100 or 50/50 rules to limit optimism).

**N13. Earned schedule.** Project BAC ₹600 lakh over 6 months; planned cumulative PV at month ends: 50, 120, 220, 350, 480, 600. At month 4 (AT = 4), EV = 300. EV 300 is reached between month 3 (PV 220) and month 4 (PV 350): $ES = 3 + (300-220)/(350-220) = 3.615$ months. $SV(t) = 3.615 - 4 = -0.38$ months; $SPI(t) = 3.615/4 = 0.904$. Classic $SPI = EV/PV = 300/350 = 0.857$. Both show lateness, but earned schedule is expressed in time and stays valid near the end of the project, where classic SPI drifts to 1.

### In the news
See news box. The overrun picture in the MoSPI data is the aggregate negative VAC across 1,775 projects; the same logic as N10 to N12 applied portfolio-wide (see [[170 Programme, Portfolio & PMO Management]]).

### Interview angle
> [!question] How it is asked
> "EV is 200, AC 230, PV 250, BAC 500. Tell me everything about this project and what you will do."

> [!tip] Strong answer includes
> - Indices with plain-language meaning (₹0.87 value per ₹1; 80% of planned progress)
> - Two or three EAC views and the assumption behind each; TCPI sanity check
> - Corrective actions linked to cause; sponsor decision needed
> - Caveat: EVM depends on honest progress measurement

---
## 13. Numericals: Risk, EMV and Decision Trees (N14 to N15)
> 🔴 Tier 1 · _Key points:_ EMV sum, contingency sizing, decision tree, value of information

### Definition
$$EMV = \sum_i P_i \times I_i$$
Decision trees: evaluate from the leaves back to the root; at chance nodes take the probability-weighted mean; at decision nodes choose the best option; subtract option costs. See [[150 Decision Analysis & Simulation]] and [[040 Risk & Stakeholder Management]].

### Example
**N14. Risk register (₹ lakh).** Vendor delay (30%, -40), monsoon flooding (20%, -25), key engineer leaves (10%, -30), bulk discount (25%, +12), early client approval (15%, +8). EMVs: -12, -5, -3, +3, +1.2. Threat EMV = **-20**; opportunity EMV = **+4.2**; **net EMV = -15.8 lakh**. Contingency recommendation: about ₹16 lakh (net) up to ₹20 lakh (threats only, if opportunities are uncertain). Do not forget that EMV is an average; the vendor delay alone could cost ₹40 lakh, so reserve and response plans differ.

**N15. Pilot vs direct roll-out (₹ crore).** Full roll-out costs ₹10 crore and returns ₹30 crore if it succeeds (net +20) or ₹4 crore if it fails (net -6). Without a pilot, P(success) = 0.45. A pilot costs ₹1.5 crore; it succeeds with probability 0.5, and after a successful pilot the roll-out succeeds with probability 0.9; after a failed pilot the project is stopped (consistent with 0.5 × 0.9 = 0.45).
- Direct: $0.45 \times 20 + 0.55 \times (-6) = 9 - 3.3 = $ **+5.7**.
- After a positive pilot: $0.9 \times 20 + 0.1 \times (-6) = 17.4$. Pilot route: $0.5 \times 17.4 + 0.5 \times 0 - 1.5 = $ **+7.2**.
Decision: **run the pilot** (value +7.2 vs +5.7). The pilot's information is worth 3.0 crore (8.7 with the pilot before its cost, less 5.7 direct): it removes average failure losses of 0.55 × 6 = 3.3 and leaves only 0.5 × 0.1 × 6 = 0.3. It costs 1.5, so the net gain is 1.5.

### In the news
See news box. Staged funding with pilots is the practical way to avoid the cost overruns seen in large projects: spend a little to learn before committing the large amount.

### Interview angle
> [!question] How it is asked
> "Would you pilot first or go full-scale? Show me the numbers."

> [!tip] Strong answer includes
> - Tree with probabilities and payoffs, solved from the right
> - Option cost included; comparison with the no-pilot EMV
> - Value of information concept; sensitivity to the pilot's predictive power
> - Non-financial factors: speed, competitors, reputational risk

---
## 14. ⭐ Advanced: Formula Sheet, Answer Frameworks and Timing Tricks
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Formula sheet (memorise):**

| Topic | Formula |
|---|---|
| Float | $TF = LS - ES$; $FF = \min(ES_{succ}) - EF$ |
| PERT | $t_e = (O+4M+P)/6$; $\sigma = (P-O)/6$; $Z = (T-\mu)/\sigma$ |
| Crash slope | (Crash cost - Normal cost) / (Normal time - Crash time) |
| EVM | $CPI = EV/AC$; $SPI = EV/PV$; $EAC = BAC/CPI$; $TCPI = (BAC-EV)/(BAC-AC)$ |
| EMV | $P \times I$, sum for contingency |
| Channels | $n(n-1)/2$ |
| NPV / PI | $\sum CF_t/(1+r)^t$; $PI = NPV/\text{investment}$ |

**Frameworks:** (1) *Definition, tool, example, pitfall* for concept questions; (2) *Clarify, quantify, options, recommend, communicate* for scenarios; (3) STAR with a number for behavioural; (4) *Index, interpretation, forecast, action* for EVM.

**Timing tricks:** state the answer first, then reasoning; round sensibly (2 decimals for indices); label units (₹ lakh vs ₹ crore); say assumptions aloud; for numericals show the table, not only the answer; check reasonableness (CPI below 1 must give EAC above BAC).

### Example
Rapid check: BAC ₹80 crore, 50% complete (EV 40), AC 44. $CPI = 0.909$; $EAC = 80/0.909 = 88$; $VAC = -8$; $TCPI = 40/36 = 1.11$. In 30 seconds: "We are paying ₹1.10 for each rupee of planned value; if this continues we finish at ₹88 crore, ₹8 crore over; to hold budget we need 11% better efficiency, which is a stretch; I would investigate rework and price escalation this week and take options to the sponsor."

### In the news
See news box. Interviewers in infrastructure and consulting often start from a public number such as the 10% aggregate overrun and ask you to reason from it: practise turning a headline number into an index, a forecast and an action.

### Interview angle
> [!question] How it is asked
> "Walk me through your approach if I give you project data in the interview."

> [!tip] Strong answer includes
> - Restate data, pick the formula, compute neatly, interpret in business language
> - Highlight the assumption behind each forecast
> - Recommend an action and the decision needed from the sponsor
> - Cross-check with a second method (EAC variant, path length) where time allows
