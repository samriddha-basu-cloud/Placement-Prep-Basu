---
tags: [product-management, tier2]
area: Product Management
topic: "PRDs, Stakeholder Management & Product Operations"
tier: Tier 2
roles: Product Manager
status: complete
subtopics: 13
---
# PRDs, Stakeholder Management & Product Operations

⬅ [[166 AI Product Management - LLM Products, Evals & Economics]] · [[_Index - Product Management|Product Management]]

> **Area:** Product Management · **Priority:** 🟠 Tier 2 · **Target roles:** Product Manager

## Sub-topics in this note
1. [[#1. PRD Purpose and Structure]]
2. [[#2. Worked PRD Example: One-Tap Reorder for a B2B Retailer App]]
3. [[#3. Writing Requirements: User Stories, Acceptance Criteria and Edge Cases]]
4. [[#4. Working with Engineering]]
5. [[#5. Working with Design]]
6. [[#6. Roadmap Communication: Now-Next-Later and Outcome Roadmaps]]
7. [[#7. Saying No and Handling Competing Requests]]
8. [[#8. Managing Executives and Stakeholders]]
9. [[#9. Launch Readiness Checklist and Release Management]]
10. [[#10. Post-Launch Review]]
11. [[#11. OKR Cascade: From Company Objectives to Product Key Results]]
12. [[#12. Product Operations (Product Ops)]]
13. [[#13. ⭐ Advanced: Decision Records, PR-FAQs and Documentation Templates]]

## 📰 News box
> [!news] Why this matters now (2024–2026): PM craft meets new compliance clocks
> **India's DPDP Rules, 2025 add privacy items to every launch checklist.** The Government's press release says the Digital Personal Data Protection Rules, 2025 operationalise the DPDP Act, 2023 with an **18-month phased compliance timeline**, breach notification to affected individuals, **verifiable parental consent** for children's data and rights to access, correct and erase personal data, with a digital Data Protection Board. Reported commencement dates: 13 November 2025, 13 November 2026 and 13 May 2027. The Act's Schedule caps penalties at **₹250 crore** for failing to keep reasonable security safeguards and **₹200 crore** for failing to notify a breach. For PMs this means consent, data-minimisation, retention and incident-response lines belong in the PRD's requirements and the launch-readiness checklist, not in a late legal review. ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014), [MeitY text of the Act](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf))
>
> **Roadmaps moved from dates to horizons.** Janna Bastow, who created the **Now-Next-Later** roadmap around 2012, argues that date-based roadmaps force deadlines on teams and crowd out discovery; the format replaces dates with three confidence horizons. ([ProdPad](https://www.prodpad.com/blog/invented-now-next-later-roadmap/))
>
> **OKRs remain the dominant goal system in tech.** The framework traces to Andy Grove at Intel (documented in *High Output Management*, 1983), reached Google around 1999 through John Doerr, and is typically scored 0.0-1.0 with about 0.7 considered a healthy result for aspirational key results. ([Wikipedia: OKRs](https://en.wikipedia.org/wiki/Objectives_and_key_results))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. PRD Purpose and Structure
> 🟠 Tier 2 · _Key points:_ Problem first; goals and non-goals; requirements; metrics; risks; living document

### Definition
A **Product Requirements Document (PRD)** aligns the team on **what** is being built, **for whom**, **why**, and **how success is judged**, leaving the **how** (implementation) to engineering and design. Its real job is shared understanding and decisions on scope, not paperwork. Atlassian's guide lists typical components: project specifics (people, status, target date), goals and business objectives, background and strategic fit, assumptions, user stories, user interaction and design, open questions and out-of-scope items.

A practical structure:

| Section | Contents |
|---|---|
| **Header** | Title, owner (PM), contributors, status, version, last updated, links |
| **1. Problem and context** | Who has the problem, evidence (research, data), why now, cost of doing nothing |
| **2. Goals** | Business and user goals; the outcome metric to move |
| **3. Non-goals** | What this release will not do (protects scope) |
| **4. Users and use cases** | Personas/segments, key jobs-to-be-done, scenarios |
| **5. Solution overview** | Concept, flows, link to designs |
| **6. Requirements** | Prioritised functional requirements (must/should/could), non-functional requirements, edge cases, acceptance criteria |
| **7. Success metrics** | Primary metric, secondary metrics, guardrails, targets, measurement plan |
| **8. Assumptions, dependencies, risks** | Technical, legal, operational; mitigations |
| **9. Rollout and launch plan** | Phases, flags, communication, support readiness |
| **10. Open questions and decisions log** | Owner and due date for each |

Good PRDs are **short** (1-4 pages for most features), written in plain language, versioned, and treated as a conversation: engineers and designers comment before it is "final". A PRD is different from a **one-pager/PR-FAQ** (pitch), a **spec** (technical design), and **user stories** (backlog items): see [[032 Agile & Scrum Framework]] and [[035 Technical Understanding (APIs, SDLC)]].

### Example
A weak problem statement: "Add a Reorder button." A strong one: "Kirana retailers who ordered at least 3 times in 60 days take a median of 90 seconds and 14 taps to reorder their usual items, and 38% abandon before checkout; the target is to cut median reorder time to under 30 seconds." The second names the user, the pain, the metric and the goal, and leaves the solution open.

### In the news
See news box. Privacy and security requirements under the DPDP Rules are now standard rows in section 6 and section 8 of a PRD for any feature touching personal data.

### Interview angle
> [!question] How it is asked
> "What goes into a PRD? Write one for [feature] in the next five minutes."

> [!tip] Strong answer includes
> - Problem, evidence, goals, non-goals, requirements, metrics, risks, rollout
> - Distinguishes what/why (PRD) from how (design, tech spec)
> - Treats the PRD as a living, collaborative document
> - Measurable success criteria and guardrails

---

## 2. Worked PRD Example: One-Tap Reorder for a B2B Retailer App
> 🟠 Tier 2 · _Key points:_ A compact end-to-end PRD with problem, goals/non-goals, requirements, metrics and risks

### Definition
Below is a compact PRD for a **fictional** B2B grocery ordering app serving kirana stores (illustrative numbers). Use it as a template.

**Problem.** 62% of weekly orders repeat at least 70% of the previous basket, yet reordering takes a median 90 seconds and 14 taps; 38% of reorder sessions end before checkout; support receives 25 reorder-related tickets per 1,000 orders. Interviews with 12 retailers (see [[164 Product Discovery & User Research]]) show they reorder at the shop counter on a phone with weak connectivity.

**Goals.** (1) Increase weekly reorder rate (retailers with a reorder in a week ÷ active retailers) from 30% to 40% in two quarters. (2) Reduce median time to reorder from 90 s to 30 s.

**Non-goals.** No price or credit-limit changes; no voice ordering (next-horizon); no new payment methods; no changes to the delivery promise.

**Requirements** (MoSCoW, see [[034 Prioritization Frameworks]]):

| ID | Requirement | Priority | Acceptance criterion |
|---|---|---|---|
| R1 | "Reorder last order" button on home for retailers with 2+ prior orders | Must | Tap shows the cart prefilled with last order's items and current prices |
| R2 | Out-of-stock and price-change flags per line | Must | Unavailable items marked; changed prices highlighted; total recalculated |
| R3 | Edit quantity/remove items before checkout | Must | Changes persist; minimum order value check shown |
| R4 | Works on 2G/3G; offline draft | Should | Cart builds in under 3 s on a 300 kbps throttle |
| R5 | "Usual items" suggestions | Could | Show up to 5 frequently bought items not in last order |
| NFR | Page load p95 under 2 s; accessibility labels; Hindi/Marathi/English text | Must | Tested on target devices |
| Privacy | Purchase history used only for ordering features; erasure supported (DPDP) | Must | Legal sign-off recorded |

**Metrics.** Primary: weekly reorder rate (30% → 40%). Secondary: time to reorder (median), reorder-session completion rate (62% → 80%). **Guardrails:** order cancellation rate (not above 3%), support tickets per 1,000 orders (not above 25), average order value (not below −3%).

**Risks and mitigations.** Stale prices shown → fetch live price at load, show change flags. Wrong auto-filled quantities increase returns → require confirmation of quantity edits above 2× usual. Cannibalisation of larger planned orders → monitor AOV guardrail. Dependency: inventory API latency → cache with 5-minute TTL.

**Rollout.** Feature flag; 5% of retailers for one week, 25% for one week, then 100%, with go/no-go checks at each step.

### Example
A/B sample size for the primary metric: baseline weekly reorder rate 20% in the tested cohort, target lift to 22% (+2 percentage points), 5% significance, 80% power:
$$n = \frac{(z_{\alpha/2}+z_{\beta})^2\,[p_1(1-p_1)+p_2(1-p_2)]}{(p_2-p_1)^2} = \frac{(1.96+0.8416)^2 \times (0.16 + 0.1716)}{0.0004} \approx 6{,}507 \text{ per arm}$$
So about 13,014 retailers are needed in total; with 20,000 eligible retailers all exposed, one week of data suffices statistically, but run at least two weeks to cover weekly ordering cycles. If only 4,000 retailers are eligible, either accept a larger minimum detectable effect or use a longer, non-A/B design. See [[092 Sampling & Experimental Design]], [[089 Hypothesis Testing]] and [[214 Causal Inference & Experimentation Beyond A-B Tests]].

### In the news
See news box. The privacy row above is the kind of requirement that the DPDP Rules turn from optional to mandatory.

### Interview angle
> [!question] How it is asked
> "Pick a feature of an app you use, and write its PRD's goals, non-goals, requirements and metrics."

> [!tip] Strong answer includes
> - Evidence-based problem statement with baseline numbers
> - Clear non-goals and prioritised requirements with acceptance criteria
> - One primary metric, secondary metrics and guardrails
> - Risks, dependencies and staged rollout

---

## 3. Writing Requirements: User Stories, Acceptance Criteria and Edge Cases
> 🟠 Tier 2 · _Key points:_ INVEST; Given-When-Then; states and edge cases; non-functional requirements

### Definition
- **User story:** "As a [user], I want [capability] so that [benefit]." Good stories follow **INVEST**: Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **Acceptance criteria:** testable conditions, often as **Given / When / Then**: *Given a retailer with two prior orders, when they tap "Reorder", then the cart shows the last order's items at current prices.*
- **Edge cases and states:** empty, loading, error, partial success, permissions, timeouts, slow networks, concurrent edits, localisation (languages, ₹ formatting, GST invoice fields), accessibility, and data errors.
- **Non-functional requirements (NFRs):** performance (p95 latency), availability/SLOs, security, privacy, scalability, observability (events to track), compliance, support and operability.
- **Analytics spec:** define events and properties up front (event name, trigger, attributes) so the success metric can be measured on day 1; see [[031 Product Metrics & Analytics]].
- **Prioritisation inside the PRD:** MoSCoW or Kano for requirements; RICE or value/effort for features across the roadmap.
- **Definition of Ready / Definition of Done:** the story is ready when it has acceptance criteria, designs and dependencies resolved; done when tested, deployed behind a flag, instrumented and documented.

Anti-patterns: prescribing the solution when you can state the problem; ambiguous words ("fast", "easy", "robust"); no non-goals; requirements that cannot be tested; omitting error states.

### Example
Ambiguous: "The page should load fast." Testable: "p95 server response under 800 ms and cart rendered under 2 s on a 300 kbps connection, measured on a mid-range Android device." Edge case list for reorder: item discontinued; price changed; pack size changed; minimum order value not met; credit limit exceeded; two devices reorder simultaneously; user partially edits then loses connectivity; store holiday and delivery slot closed.

### In the news
See news box. Consent, retention and erasure acceptance criteria (for example "erasure request removes purchase history from the recommendation index within a defined window") are now a normal part of NFR lists.

### Interview angle
> [!question] How it is asked
> "Write acceptance criteria for a 'forgot password' flow. What edge cases would you cover?"

> [!tip] Strong answer includes
> - Given-When-Then criteria that are testable
> - Error, empty, abuse and security cases (rate limits, token expiry, account enumeration)
> - NFRs and analytics events
> - Clear separation of must-have and later iterations

---

## 4. Working with Engineering
> 🟠 Tier 2 · _Key points:_ Early involvement, estimates and ranges, technical debt, trade-off conversations, respect for focus

### Definition
Effective PM-engineering partnership:

- **Involve engineers early** (discovery, not hand-off): they spot feasibility and cost cliffs; see the product-trio idea in [[164 Product Discovery & User Research]].
- **Share the problem, not the solution**; agree the outcome and let the team propose options (including a cheaper "80/20" version).
- **Estimates are ranges with confidence**, not promises; use t-shirt sizes early and story points in sprints; ask "what would make this estimate wrong?"; avoid negotiating estimates downward.
- **Respect capacity:** capacity = people × days × focus factor. 6 engineers × 10 days × 0.7 focus = 42 engineer-days; commit to about 80% (about 34) to leave buffer for bugs, support and surprises.
- **Technical debt and platform work:** reserve a fixed share of capacity (commonly 15-25%) for reliability, debt and enablers; explain the business value (incident rate, delivery speed) to executives.
- **Decisions:** agree who decides what (DACI or RACI), e.g. product decides scope and priority, engineering decides architecture and estimates, design decides interaction.
- **Rituals:** backlog refinement, sprint planning, demos, retrospectives (see [[032 Agile & Scrum Framework]], [[041 Agile Project Management]]); keep meetings useful and protect focus time.
- **Quality and incident culture:** blameless post-mortems, clear definition of done, test and monitoring expectations; PMs own the user impact and communication during incidents.
- **Technical literacy:** understand APIs, data flows, environments and trade-offs (see [[035 Technical Understanding (APIs, SDLC)]]).

### Example
Planning: the team has 42 engineer-days in the sprint (6 × 10 × 0.7). Commitment 34 days (80%). Backlog candidates: reorder button (12 days), price-change flags (8), edit quantities (6), offline draft (14). The first three total 26 days; adding offline draft (14) would reach 40 days, beyond the 34-day commitment, so it is deferred to the next sprint and the PRD marks it "Should". The PM explains the trade-off to stakeholders as scope sequencing rather than "engineering is slow".

### In the news
See news box. New compliance obligations compete for the same engineering capacity: DPDP work (consent flows, deletion pipelines) needs explicit capacity in planning, not hidden "extras".

### Interview angle
> [!question] How it is asked
> "Engineering says your feature will take 3 months; you need it in 1. What do you do?"

> [!tip] Strong answer includes
> - Asks what drives the estimate and for options (cut scope, phase, reuse, buy)
> - Aligns on the outcome and deadline's real cause (is it fixed?)
> - Offers trade-offs, not pressure; escalates only with data
> - Documents the decision and revisits after delivery

---

## 5. Working with Design
> 🟠 Tier 2 · _Key points:_ Shared problem framing, critiques, design system, research partnership, handoff

### Definition
- **Co-own the problem:** the designer joins discovery and problem framing; the PM brings business context and constraints, the designer brings user and interaction insight (see [[033 Design Thinking & UX]]).
- **Critique, not approval:** structured crits ("what problem does this solve, what are we trading off?") rather than "I don't like it". Give feedback on outcomes against goals.
- **Prototype before building:** low-fidelity first; test with 5 users per round ([[164 Product Discovery & User Research]]).
- **Design systems:** reuse components for consistency, speed and accessibility; know the cost of custom UI.
- **Hand-off as collaboration:** annotated flows, states (empty, error, loading), responsive behaviour, content and localisation; engineers review designs early; use design QA before release.
- **Metrics and craft:** pair quantitative (funnels, task success) with qualitative; avoid optimising a metric at the cost of trust (dark patterns).
- **Conflict patterns:** scope creep from pixel-perfect polish vs deadlines: agree a quality bar per release (must-fix vs later).

### Example
Reorder screen debate: design proposes a rich carousel of "usual items" (3 weeks of work); PM and engineering want a simple prefilled list (4 days). Resolution: ship the list first (R1-R3), instrument "usual item" taps, and prototype the carousel with 5 retailers in parallel; build it only if prototype tests show a measurable gain over the list. Everyone's concern is addressed by evidence.

### In the news
See news box. Accessibility and privacy notices are design requirements now; plan time for consent UI and clear notices in the design sprint.

### Interview angle
> [!question] How it is asked
> "How do you handle a disagreement with your designer?"

> [!tip] Strong answer includes
> - Returns to user evidence and goal metrics, not authority
> - Tests the disagreement with a prototype or experiment
> - Agrees decision rights and a quality bar up front
> - Preserves the relationship: credit and shared ownership

---

## 6. Roadmap Communication: Now-Next-Later and Outcome Roadmaps
> 🟠 Tier 2 · _Key points:_ Horizons, themes and outcomes, confidence, dates only for commitments; RICE for ordering

### Definition
A **roadmap** communicates direction and priorities, not a delivery contract. Types:

| Format | Features | Best for |
|---|---|---|
| **Timeline / Gantt** | Dates for each item | Fixed-date commitments (regulatory deadlines, contractual launches) |
| **Now-Next-Later** | Three horizons by confidence, not by date | Agile teams, uncertainty, external sharing |
| **Outcome / theme roadmap** | Problems and goals per quarter, not features | Aligning with strategy and OKRs |
| **Release roadmap** | Planned releases with scope | Delivery coordination, B2B customers |

Best practices: lead with **strategy and outcomes** ("reduce time to reorder"), show **confidence levels**, keep **different versions per audience** (leadership: themes and outcomes; sales: what is committed vs exploratory; engineering: detailed next quarter), state assumptions and dependencies, and **update it on a cadence**. Put **dates only on genuine commitments** (regulatory deadlines such as DPDP milestones, contractual launches). Maintain a visible **"not doing"** list.

**RICE scoring** orders candidates:
$$\text{RICE} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$$
Reach = users per period; Impact on a 0.25-3 scale; Confidence as a percentage; Effort in person-months. See [[034 Prioritization Frameworks]].

### Example
Candidates for the retailer app (Reach per quarter; Impact; Confidence; Effort in person-months):

| Item | Reach | Impact | Confidence | Effort | RICE |
|---|---|---|---|---|---|
| One-tap reorder | 8,000 | 2 | 80% | 3 | 8,000×2×0.8/3 = **4,267** |
| Invoice download | 6,000 | 0.5 | 100% | 1 | **3,000** |
| Credit-limit display | 5,000 | 1 | 80% | 1.5 | **2,667** |
| Voice ordering | 3,000 | 3 | 50% | 6 | **750** |

Now: one-tap reorder; Next: invoice download, credit-limit display; Later: voice ordering (needs discovery). Communicated to sales as "Now/Next/Later with confidence", not as month commitments, except a statutory compliance change that has a fixed legal date.

### In the news
See news box for the Now-Next-Later origin: date-based roadmaps invite deadline negotiations and crowd out discovery.

### Interview angle
> [!question] How it is asked
> "Sales wants a date for a feature on the roadmap. How do you respond?"

> [!tip] Strong answer includes
> - Explains the horizon model and confidence, separate from commitments
> - Offers a date only with explicit assumptions and ranges, or a smaller scoped commitment
> - Understands the customer need behind the date request
> - Uses RICE or similar to explain priority, not authority

---

## 7. Saying No and Handling Competing Requests
> 🟠 Tier 2 · _Key points:_ Say no to the request, yes to the problem; transparent criteria; trade-offs; parking lot

### Definition
A PM's value comes largely from **what they decline**. Method:

1. **Understand the underlying problem** behind the request ("What are you trying to achieve? What happens today?"); stakeholders often propose solutions.
2. **Check against goals, strategy and capacity**: does it move the current outcome? What is the opportunity cost?
3. **Decide with transparent criteria** (RICE, strategic fit, revenue at risk, customer count, effort); share the scoring.
4. **Respond with respect and options**: "Not now, because X; here is what we are doing instead; here is what would change my mind." Offer alternatives: a workaround, a smaller version, a later date, or a different team.
5. **Close the loop**: record in a parking lot or backlog with the reason, and revisit on a cadence; tell stakeholders when circumstances change.
6. **Trade-offs, not refusals** with executives: "To add this, we remove one of these; which do you prefer?" (see [[040 Risk & Stakeholder Management]]).
7. **Avoid**: a silent no, a vague "maybe" that becomes a commitment, over-promising, and surprising a stakeholder in a meeting.

### Example
A large distributor threatens to churn unless a custom report is built (3 person-months). Analysis: ₹1.8 crore annual contract (about 2% of revenue); 2 other customers asked similar things; the report is 80% achievable via the existing export plus a template (3 days). Response: provide the template now, add the report to Next with a discovery interview for the shared need, and commit to a review in 6 weeks. The PM says no to custom work and yes to the problem, with evidence from the RICE table and customer count.

### In the news
See news box. Compliance deadlines are the main "non-negotiable" category in prioritisation; a transparent rubric should place them above optional features.

### Interview angle
> [!question] How it is asked
> "The CEO asks you to add a feature that is off-strategy. What do you do?"

> [!tip] Strong answer includes
> - Seeks the underlying goal and reasons; maps to strategy and metrics
> - Presents trade-offs and cost of delay with data
> - Offers options (smaller test, later date, alternative)
> - Commits to a decision, documents it and follows up

---

## 8. Managing Executives and Stakeholders
> 🟠 Tier 2 · _Key points:_ Stakeholder map; pre-wiring; single-page updates; bad news early; RACI/DACI

### Definition
- **Map stakeholders** by influence and interest (see [[040 Risk & Stakeholder Management]]): manage closely (high/high), keep satisfied, keep informed, monitor.
- **Understand each stakeholder's goals and constraints** (sales: quota and deals; finance: budget and ROI; legal: risk; support: ticket volume).
- **Pre-wire decisions:** meet key people one-on-one before the big review so no one is surprised; the meeting confirms rather than debates.
- **Communicate in the executive's frame:** answer first (the decision or ask), then evidence; 1-page summaries; metrics tied to business goals; clear asks and deadlines (see [[162 Structured Communication - SCQA, Storylines & Case Delivery]]).
- **Cadence:** weekly status for the team, monthly business review, quarterly roadmap and OKR reviews; escalate **early** with options.
- **Bad news early:** state facts, impact, options and your recommendation.
- **Decision frameworks:** **RACI** (Responsible, Accountable, Consulted, Informed) for tasks; **DACI** (Driver, Approver, Contributors, Informed) for decisions, with a single approver.
- **Influence without authority:** use data, customer evidence, small pilots, credit sharing, and trust built through delivery.
- **Handling HiPPO** (highest paid person's opinion): convert opinions to testable hypotheses.

### Example
Status update to an executive in five lines: (1) Decision needed by Friday: delay the offline-draft feature by one sprint. (2) Why: edge-case testing found stale-price risk affecting about 4% of orders. (3) Impact: reorder launch moves from 14 to 21 October; target metric unaffected. (4) Options: ship without offline draft (recommended) or delay all. (5) Risk if no decision: team idle 2 days. This format makes the decision easy and builds credibility.

### In the news
See news box. Compliance dates are a rare topic where executives respond to external clocks rather than preferences; use them to secure capacity.

### Interview angle
> [!question] How it is asked
> "Tell me about a time you had to influence a senior stakeholder who disagreed with you."

> [!tip] Strong answer includes
> - Understanding their goals and constraints before arguing
> - Using data and a small experiment to resolve disagreement
> - Pre-wiring and clear asks
> - Outcome, measured result and relationship afterwards (see [[049 STAR Stories — Leadership & Conflict]])

---

## 9. Launch Readiness Checklist and Release Management
> 🟠 Tier 2 · _Key points:_ Go/no-go criteria, feature flags, staged rollout, rollback, comms and support readiness

### Definition
**Launch readiness** confirms that the product, the business and the company are ready. Checklist areas:

| Area | Examples of checks |
|---|---|
| **Product and quality** | Acceptance criteria met; test coverage; no open P0/P1 bugs; performance and load tests; accessibility; device/browser matrix |
| **Data and analytics** | Events instrumented and validated; dashboards live; experiment configured; baselines captured |
| **Reliability** | Monitoring and alerts; rollback plan; feature flags; on-call; runbook; capacity |
| **Security and privacy** | Security review; DPDP consent, notices, retention, deletion and breach process; vendor/contract checks |
| **Legal and compliance** | Terms, claims, regulatory approvals (RBI, GST, sector rules) |
| **Go-to-market** | Positioning, pricing, sales and support training, help-centre articles, FAQ, communication plan (see [[036 Go-To-Market Strategy]]) |
| **Support and operations** | Ticket categories, escalation paths, SLAs, ops capacity |
| **Decision** | Go/no-go meeting with named approvers and explicit criteria |

**Release strategies:** **feature flags**, **staged rollout** (1% → 5% → 25% → 100%), **canary releases**, **dark launches**, **beta/early access**, **blue-green deployments**, and **kill switches**. Each stage has **exit criteria** (guardrail metrics within thresholds, no severe incidents) and a **rollback trigger**. Reliability targets use **SLOs**: a 99.9% monthly availability SLO allows an error budget of $30 \times 24 \times 60 \times 0.001 = 43.2$ minutes of downtime.

**Release management:** release calendar and freeze windows (festival season sales in India), change approvals, release notes, versioning, dependency coordination across teams, hotfix process. For project-style launches see [[042 Cost & Budget Management]] and [[038 PMBOK Knowledge Areas]] for change control.

### Example
Staged rollout for the reorder feature with 200,000 daily active retailers: Stage 1 at 1% = 2,000 retailers for 3 days; exit criteria: crash rate not above baseline +0.1pp, cancellation rate not above 3%, p95 latency under 2 s. Stage 2 at 5% = 10,000 for 1 week with the A/B test; Stage 3 at 25% for 1 week; Stage 4 at 100%. A trigger: if cancellation rate exceeds 3.5% for two consecutive hours, flip the flag off automatically and page the on-call. Go/no-go scorecard before Stage 1: 18 of 20 checklist items done, the two open items (help-centre article, one low-priority bug) accepted by named owners.

### In the news
See news box. The DPDP penalty for failing to notify a breach (₹200 crore) makes an incident and breach-notification runbook a launch-blocking item for features that handle personal data.

### Interview angle
> [!question] How it is asked
> "What would be on your launch checklist for a payments feature?"

> [!tip] Strong answer includes
> - Quality, data, reliability, security/privacy, legal, GTM, support and decision criteria
> - Staged rollout with metrics-based exit and rollback criteria
> - Named owners for each item and a go/no-go meeting
> - Post-launch monitoring plan and communication

---

## 10. Post-Launch Review
> 🟠 Tier 2 · _Key points:_ Compare forecast vs actual; learnings; follow-ups; closing the loop

### Definition
A **post-launch review** (30/60/90 days) checks whether the product delivered the intended outcome and captures learning:

1. **Outcome vs target:** primary metric vs the PRD target; secondary metrics; guardrails.
2. **Adoption and engagement:** exposure, activation, repeat use, segments (new vs existing, region, device).
3. **Business impact:** revenue, cost, retention, support load, ops cost; an incremental view using the experiment or holdout.
4. **Quality and reliability:** incidents, bugs, performance, support tickets and qualitative feedback.
5. **Forecast accuracy:** what we expected vs actual, and why the gap (assumptions that failed).
6. **Process review (retrospective):** what went well/poorly in discovery, estimation, collaboration, rollout.
7. **Decisions:** iterate, scale, fix, sunset; update roadmap and OKRs; communicate results (including failures) to stakeholders.
8. **Archive learning** in a searchable repository (product ops can run this).

Avoid: declaring success from vanity metrics, no baseline, skipping the review once the team moves on, blaming individuals.

### Example
Forecast: weekly reorder rate 30% → 40%. Actual at 60 days: 34%, i.e. $(34-40)/40 = -15\%$ vs forecast, but +4 points over baseline. Analysis: adoption among retailers with 2+ prior orders reached 55%, but only 12% of retailers with weak connectivity used it (R4 offline draft was deferred). Median reorder time fell from 90 s to 41 s (target 30 s). Guardrails: cancellations 2.6% (OK), tickets 21 per 1,000 (improved). Decision: scale to 100%, prioritise offline draft in Next, and re-forecast target to 38%.

### In the news
See news box. A DPDP-relevant review item: confirm consent and deletion flows worked in production and that no personal data was logged unnecessarily.

### Interview angle
> [!question] How it is asked
> "A feature you launched did not hit its target. What do you do?"

> [!tip] Strong answer includes
> - Segment analysis and funnel diagnostics before concluding
> - Separates execution issues (bugs, reach) from hypothesis failures
> - Decides: iterate, pivot or sunset, with evidence
> - Shares learnings openly and updates forecasting assumptions

---

## 11. OKR Cascade: From Company Objectives to Product Key Results
> 🟠 Tier 2 · _Key points:_ Objective plus 3-5 measurable KRs; alignment not cascade-by-copy; scoring 0-1; outcomes not outputs

### Definition
**OKRs** pair a qualitative, inspiring **objective** with 3-5 measurable **key results**. Origin: Grove at Intel; popularised by Doerr at Google. Rules: KRs measure **outcomes** (numbers moved), not tasks; set ambitious targets (aspirational KRs scored around 0.7 are healthy; committed KRs target 1.0); review weekly or monthly, score at quarter end; separate OKRs from compensation. **Cascade** means **alignment** (each team's OKRs contribute to higher-level ones, with ownership negotiated top-down and bottom-up), not copying: product OKRs link to company OKRs through a driver tree. Compare with balanced scorecards in [[225 Budgeting, Variance Analysis & Balanced Scorecard]] and metrics trees in [[031 Product Metrics & Analytics]].

Score for a KR with start $s$, target $t$, actual $a$:
$$\text{Score} = \frac{a - s}{t - s}$$

### Example
Company objective: "Become the default ordering channel for neighbourhood retailers". Company KR: weekly active ordering retailers from 40,000 to 60,000. Product-team objective: "Make reordering effortless". KRs: (1) Weekly reorder rate 30% → 40%; (2) Median time to reorder 90 s → 30 s; (3) Reorder-related tickets per 1,000 orders 25 → 15. Quarter-end actuals: 36%, 50 s, 19.

| KR | Start | Target | Actual | Score |
|---|---|---|---|---|
| Weekly reorder rate | 30% | 40% | 36% | (36−30)/(40−30) = **0.60** |
| Median time to reorder | 90 s | 30 s | 50 s | (50−90)/(30−90) = **0.67** |
| Tickets per 1,000 orders | 25 | 15 | 19 | (19−25)/(15−25) = **0.60** |

Objective score = mean = **0.62**, near the aspirational norm of 0.6-0.7. The review asks which learnings to apply next quarter (offline draft), not whether people "failed". Link the product KR (reorder rate) to the company KR via the driver tree: active retailers = retailers ordering weekly; more reorders raise weekly activity.

### In the news
See news box for the OKR history (Intel, Google) and the 0.7 convention.

### Interview angle
> [!question] How it is asked
> "Write OKRs for the search team of an e-commerce app."

> [!tip] Strong answer includes
> - Inspiring objective, 3-4 outcome-based KRs with baselines and targets
> - Alignment to company goals through a metrics tree
> - Guardrails and balanced metrics (quality, cost)
> - Scoring and review cadence, and the output-vs-outcome distinction

---

## 12. Product Operations (Product Ops)
> 🟠 Tier 2 · _Key points:_ Process, data/insights, tooling, enablement; scales PM effectiveness

### Definition
**Product operations** is a function that helps product teams work effectively at scale by owning the **systems and rhythms** around product, not the product decisions themselves. Typical remit:

- **Data and insights:** analytics tooling, shared dashboards, experimentation platform, research repository, customer feedback aggregation.
- **Process and planning:** roadmap and OKR cadence, planning templates, intake of requests, launch process and checklists, release calendars.
- **Tooling and enablement:** product stack (backlog, roadmap, feedback tools, docs), onboarding for new PMs, playbooks and templates, training.
- **Cross-functional alignment:** liaison between product, sales, support, marketing, finance and legal; launch coordination and enablement.
- **Governance and quality:** PRD and decision-record standards, post-launch reviews, product health scorecards, dependency tracking, portfolio view.
- **When it pays off:** more than about 5-8 PMs or teams, multiple product lines, heavy coordination or reporting overhead; small teams can run lightweight "ops" within PM.
- **Metrics:** PM time spent on admin, launch quality (incidents, delays), planning cycle time, adoption of tools, stakeholder satisfaction, experiment velocity.

Compare with project/programme management ([[170 Programme, Portfolio & PMO Management]]) and data/BI teams ([[047 MIS & Dashboard Design]]); product ops is closer to **enablement** for product teams.

### Example
A 25-PM product organisation spends roughly 6 hours per PM per week on status reporting and ad-hoc data requests. Product ops builds a single product-health dashboard, a quarterly planning template and a request-intake form; PM admin time falls to 3 hours. Savings: 25 PMs × 3 hours × 48 weeks = **3,600 hours** a year, about 2 FTE of PM capacity (assuming 1,800 hours per FTE-year). Compared with the cost of 1-2 product ops hires, the investment pays back mainly through better launches and faster planning rather than the hours alone.

### In the news
See news box. As privacy, AI and accessibility checks multiply, product ops increasingly owns the launch-readiness checklist and the compliance evidence trail.

### Interview angle
> [!question] How it is asked
> "Does a 12-person product team need a product operations function?"

> [!tip] Strong answer includes
> - Defines product ops as systems, data, process and enablement, not decision-making
> - Triggers (scale, coordination pain) and the metrics of success
> - Starts lightweight (one owner, templates, dashboards) and grows with need
> - Distinguishes from PMO and from data teams

---

## 13. ⭐ Advanced: Decision Records, PR-FAQs and Documentation Templates
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Documentation is a tool for **faster, better decisions**, not a bureaucracy. Common templates:

| Template | Purpose | Key sections |
|---|---|---|
| **One-pager / opportunity brief** | Pitch an idea, decide whether to invest | Problem, evidence, size of opportunity, proposed approach, effort, risks |
| **PR-FAQ (Amazon "working backwards")** | Define the product from the customer's end, before building | Draft press release (customer, problem, solution, quote), customer FAQ, internal FAQ (cost, risks, metrics) |
| **PRD** | Align on scope for a build | See sub-topics 1-2 |
| **Design doc / RFC** | Engineering proposes architecture and invites review | Context, goals, options and trade-offs, decision, rollout |
| **ADR (architecture decision record)** | Record a decision and why | Status, context, decision, consequences |
| **DACI decision doc** | Make a cross-functional decision | Driver, Approver, Contributors, Informed; options; recommendation; deadline |
| **Experiment brief** | Pre-register an experiment | Hypothesis, metric, threshold, sample, duration, decision rule |
| **Launch brief / readiness doc** | Align go-to-market and operations | Audience, message, checklist, owners |
| **Post-mortem / post-launch review** | Learn from outcomes | Timeline, impact, root causes, actions |
| **Weekly update / strategy memo** | Keep stakeholders aligned | Status, risks, asks, next steps |

Principles: write for the reader and the decision; make the **ask explicit**; keep docs short and linked; version and date them; assign owners; use **comments for async review** before meetings; store in a searchable place with a consistent template (product ops). **Narrative memos** (Amazon-style six-pagers read silently at the start of a meeting) force clearer thinking than slides. **Decision logs** reduce re-litigation and onboarding time.

### Example
DACI for "Should we launch offline draft in this release?" Driver: PM. Approver: Head of Product. Contributors: engineering lead, design lead, support lead, data analyst. Informed: sales and customer success. Options: (A) ship now without offline draft; (B) delay 2 weeks; (C) ship with a limited offline mode. Recommendation: A, because only 12% of retailers are on weak connectivity, and the delay costs two weeks of 40,000 weekly retailers' reorder-time savings. Decision recorded on Friday with the reason and revisit date. Six months later a new PM reads the log and does not reopen the debate. For consulting-style structuring see [[162 Structured Communication - SCQA, Storylines & Case Delivery]]; for interviews see [[163 PM Interview Types & Answer Frameworks]].

### In the news
See news box. AI features and privacy obligations are pushing teams to add "risk and compliance" sections to PRDs and experiment briefs (see [[166 AI Product Management - LLM Products, Evals & Economics]]).

### Interview angle
> [!question] How it is asked
> "How do you make sure your team's decisions are documented and not repeatedly relitigated?"

> [!tip] Strong answer includes
> - Lightweight templates: DACI, decision log, ADR, PRD, experiment brief
> - Clear driver and single approver with deadlines
> - Records of options considered and why one was chosen
> - Reviews and revisit dates so decisions can change when evidence does
