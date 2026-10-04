---
tags: [product-management, tier1]
area: Product Management
topic: "Prioritization Frameworks"
tier: Tier 1
roles: PM / Consulting
status: complete
subtopics: 10
---
# Prioritization Frameworks

⬅ [[033 Design Thinking & UX]] · [[_Index - Product Management|Product Management]] · [[035 Technical Understanding (APIs, SDLC)]] ➡

> **Area:** Product Management · **Priority:** 🔴 Tier 1 · **Target roles:** PM / Consulting

## Sub-topics in this note
1. [[#1. RICE Framework]]
2. [[#2. MoSCoW Method]]
3. [[#3. Kano Model]]
4. [[#4. ICE Scoring]]
5. [[#5. Value vs Effort Matrix]]
6. [[#6. OKRs (Objectives & Key Results)]]
7. [[#7. Priority Poker]]
8. [[#8. Feature Flagging]]
9. [[#9. ⭐ Advanced: WSJF and Cost of Delay]]
10. [[#10. ⭐ Advanced: Opportunity Scoring (Importance vs Satisfaction)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): CrowdStrike's faulty update shows why gradual rollout and kill switches matter (Jul 2024)
> **CrowdStrike outage (19 Jul 2024).** A faulty configuration ("channel file 291") for the Falcon sensor, pushed automatically as a rapid-response content update, crashed about **8.5 million Windows devices** (under 1% of Windows machines, but many in airlines, banks and hospitals). The Content Validator failed to catch a mismatch between 21 expected and 20 supplied input fields. A fix was deployed within **79 minutes**, yet about 99% of sensors were back only by 29 Jul. Afterwards CrowdStrike moved to a **"concentric rings" staged rollout** with customer control (early adopter, general availability, or delay) and tested content updates like code releases. ([TechTarget](https://www.techtarget.com/whatis/feature/Explaining-the-largest-IT-outage-in-history-and-whats-next))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. RICE Framework
> 🔴 Tier 1 · _Tracker hint:_ Reach × Impact × Confidence / Effort; scoring and ranking

### Definition
**RICE** (popularised by Intercom) gives each backlog item a numeric score so very different ideas can be compared on one scale:

$$\text{RICE} = \frac{\text{Reach} \times \text{Impact} \times \text{Confidence}}{\text{Effort}}$$

| Input | Meaning | Typical scale |
|---|---|---|
| **Reach** | How many users/events are affected in a period (e.g. per quarter) | Actual count |
| **Impact** | Effect per user on the goal | 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal |
| **Confidence** | How sure you are about the Reach and Impact estimates | 100% / 80% / 50% |
| **Effort** | Total team time | Person-months |

Confidence is the "honesty discount": a flashy idea backed only by opinion gets penalised. Score is relative, not absolute: use it to **rank**, then sanity-check with strategy, dependencies and risk. Weaknesses: estimates can be gamed, Reach ignores strategic value, and it undervalues platform or tech-debt work.

### Example
| Feature | Reach/qtr | Impact | Confidence | Effort (person-months) | RICE |
|---|---|---|---|---|---|
| A: UPI autopay reminder | 2,000 | 2 | 80% | 4 | 2000×2×0.8/4 = **800** |
| B: One-tap reorder | 500 | 3 | 100% | 1 | 500×3×1/1 = **1,500** |
| C: New home-screen theme | 10,000 | 0.5 | 50% | 5 | 10000×0.5×0.5/5 = **500** |

Ranking: B, A, C. C has the biggest reach but low impact and low confidence.

### In the news
See news box. CrowdStrike's rapid-response updates were high Reach (millions of devices) with a catastrophic downside; a RICE score has no "risk" term, so risky high-reach changes need an explicit risk check next to the score.

### Interview angle
> [!question] How it is asked
> "You have 10 feature requests and one team. How do you prioritise?" or "Walk me through RICE and when it fails."

> [!tip] Strong answer includes
> - The formula and units of each input (Reach per period, Impact scale, Confidence %, Effort in person-months)
> - A quick worked calculation with two or three items
> - Where it breaks: gaming, no strategic or risk dimension, tech debt
> - Pairing with a goal (OKR) and stakeholder discussion, not blindly following the number

---

## 2. MoSCoW Method
> 🔴 Tier 1 · _Tracker hint:_ Must have, Should have, Could have, Won't have — for sprints

### Definition
**MoSCoW** (from the DSDM agile method, Dai Clegg) sorts requirements for a fixed time-box into four buckets:
- **Must have:** without it the release has no value or is illegal/unsafe. If one Must is missing, the release fails.
- **Should have:** important, painful to leave out, but a workaround exists.
- **Could have:** desirable; first to be dropped if time runs short.
- **Won't have (this time):** explicitly agreed to be out of scope now (not "never"), which manages expectations.

Rule of thumb in DSDM: Musts should be about 60% of effort, Shoulds and Coulds fill the remainder, leaving a contingency buffer. Test for a true Must: "What happens if we ship without it?" If the answer is "we are fine", it is not a Must.

### Example
A bank app MVP for a UPI-style payment launch: **Must** = send/receive money, PIN authentication, transaction history. **Should** = UPI QR scan. **Could** = dark mode. **Won't (this release)** = credit-line on UPI. The team protects the Musts and cuts Coulds when the sprint slips.

### In the news
See news box. CrowdStrike's content-validation step arguably was a Must for every release, yet the rapid-response channel treated content updates as lighter than code releases; a Must-have test gate applies to every change, not just big ones.

### Interview angle
> [!question] How it is asked
> "The deadline is fixed and scope is too big. What do you cut?"

> [!tip] Strong answer includes
> - Four buckets with the Won't = "not now" nuance
> - A test for Must (ship-without test), with a cap on Musts
> - Fixed time and cost, flexible scope: where MoSCoW fits
> - Stakeholder alignment workshop to agree buckets, plus its weakness (no ranking inside a bucket)

---

## 3. Kano Model
> 🔴 Tier 1 · _Tracker hint:_ Basic, Performance, Delight (excitement) features — satisfaction curve

### Definition
Noriaki Kano's model (1984) classifies features by how they affect satisfaction versus how well they are implemented:

| Category | If absent | If present | Behaviour |
|---|---|---|---|
| **Basic (must-be)** | Strong dissatisfaction | Neutral (expected) | Hygiene factors |
| **Performance (one-dimensional)** | Dissatisfied | Satisfied, proportional to quality | More is better (speed, battery) |
| **Delight (attractive)** | Neutral (nobody expects it) | Very satisfied | Differentiators |
| **Indifferent / Reverse** | No effect / some users dislike it | | Avoid building |

Data is gathered with a **paired survey**: a *functional* question ("How would you feel if the app had X?") and a *dysfunctional* one ("...if it did not have X?"), answered on Like / Expect / Neutral / Tolerate / Dislike, then mapped to a category via the Kano evaluation table. Key insight: **today's delighter becomes tomorrow's basic** (expectations drift), so product strategy must keep inventing delighters.

### Example
Illustrative for a food-delivery app: accurate order status = Basic; faster delivery time = Performance; live rider tracking was once a Delight and is now widely expected, i.e. it migrated toward Basic. A surprise freebie in the bag is a Delight with little cost.

### In the news
See news box. Reliability is a Basic: nobody praises an endpoint-security tool for running, but everyone punishes it for crashing 8.5 million machines.

### Interview angle
> [!question] How it is asked
> "How do you decide between fixing bugs, improving speed and adding a wow feature?"

> [!tip] Strong answer includes
> - The three categories plus indifferent/reverse, with the satisfaction curve described
> - Survey method (functional and dysfunctional questions)
> - Time decay: delighter to basic
> - Using it with RICE: Kano says what kind of value, RICE says what order

---

## 4. ICE Scoring
> 🔴 Tier 1 · _Tracker hint:_ Impact, Confidence, Ease — simpler version of RICE

### Definition
**ICE** (popularised by Sean Ellis for growth experiments) scores each idea 1–10 on:
- **Impact:** how much it moves the target metric if it works.
- **Confidence:** how sure you are that it will work (evidence, past tests).
- **Ease:** how easy to implement (inverse of effort).

$$\text{ICE} = I \times C \times E \quad(\text{some teams use the average } (I+C+E)/3)$$

It drops **Reach**, so it is fast for experiment backlogs (growth, marketing) but gives weaker discrimination when ideas affect very different numbers of users. Scores are subjective: calibrate the scale as a team, and rescore after each experiment because Confidence should rise or fall with evidence.

### Example
Two growth experiments: (1) referral banner: I = 8, C = 6, E = 5, ICE = 8×6×5 = **240**; (2) WhatsApp order-status message: I = 6, C = 9, E = 8, ICE = 6×9×8 = **432**. Run (2) first, even though (1) has more upside, because it is more certain and cheap.

### In the news
See news box. Staged-rollout experiments are the ICE world: ship small, learn, raise Confidence before expanding.

### Interview angle
> [!question] How it is asked
> "How is ICE different from RICE and when would you use each?"

> [!tip] Strong answer includes
> - Formula and the 1–10 scales
> - Difference: no Reach, Ease instead of Effort (higher is better)
> - Use ICE for quick experiment triage, RICE when audience size varies and data exists
> - Limitation: subjectivity, so use shared scoring rubrics

---

## 5. Value vs Effort Matrix
> 🔴 Tier 1 · _Tracker hint:_ 2×2 quadrant; quick wins vs big bets vs avoid

### Definition
Plot each item with **Effort** on one axis and **Value** (business/customer impact) on the other:

| | Low effort | High effort |
|---|---|---|
| **High value** | **Quick wins:** do first | **Big bets:** plan, de-risk, staged delivery |
| **Low value** | **Fill-ins:** do if spare capacity | **Money pits / avoid:** drop |

It is a visual workshop tool, good for aligning a mixed group (engineers, sales, design) in 30 minutes, because the debate is about placement not a spreadsheet. Weaknesses: no quantification, easy to bias toward quick wins forever and starve the big bets that create strategic moats. Combine with a defined value metric (revenue, retention) so "value" is not just opinion.

### Example
A fintech PM places: autofill of IFSC code (quick win), KYC re-verification redesign (big bet: high value, high effort due to compliance), animated splash screen (money pit). Roadmap: quick win this sprint, big bet scoped into phases, splash dropped.

### In the news
See news box. A staged rollout is how you de-risk a "big bet" quadrant item: start with a small ring, widen as metrics hold.

### Interview angle
> [!question] How it is asked
> "Use any framework to prioritise these six initiatives for the next quarter."

> [!tip] Strong answer includes
> - Draw the 2×2 and name the four quadrants
> - Define the axes with metrics (value = incremental revenue or retention, effort = person-weeks)
> - Balanced portfolio: quick wins plus at least one big bet
> - Caveat on subjectivity; validate the top items with data

---

## 6. OKRs (Objectives & Key Results)
> 🔴 Tier 1 · _Tracker hint:_ Objective = qualitative goal; KR = measurable outcome

### Definition
**OKRs** link strategy to execution. Created by Andy Grove at Intel and brought to Google by John Doerr (1999).
- **Objective:** a qualitative, inspiring, time-bound goal (what).
- **Key Results:** 2–5 measurable outcomes proving the objective is met (how we know). They measure **outcomes, not tasks** ("increase D30 retention from 18% to 25%", not "launch onboarding revamp").
- **Cadence:** quarterly (company/team) with weekly check-ins; scoring 0.0–1.0, where ~0.7 on **stretch** ("aspirational") OKRs is considered healthy; **committed** OKRs should hit 1.0.

OKRs are not a prioritisation formula but a **filter**: initiatives that do not move a Key Result drop down the list. Common mistakes: too many OKRs, KRs that are really tasks, tying them directly to compensation (kills ambition), and no alignment across levels.

### Example
Objective: *Make our grocery app the default weekly shop for urban families.*
- KR1: Raise weekly-active orderers from 40,000 to 60,000.
- KR2: Cut median delivery time from 32 to 25 minutes.
- KR3: Lift 4-week repeat rate from 35% to 45%.
Mid-quarter, KR1 is at 52,000: progress = (52,000 − 40,000)/(60,000 − 40,000) = **60%**.

### In the news
See news box. After the outage, CrowdStrike committed to staged rollout and customer control (per the news box); a team in that position would turn "reliability" into a measurable Key Result (for example, percentage of updates shipped through staged rings) rather than a vague value.

### Interview angle
> [!question] How it is asked
> "What is the difference between OKRs and KPIs?" or "Write OKRs for a food-delivery PM."

> [!tip] Strong answer includes
> - Objective qualitative vs KR quantitative outcome
> - KPIs monitor health continuously; OKRs drive change in a period
> - A crisp example with baseline and target numbers
> - Pitfalls: output-as-KR, too many, comp-linking

---

## 7. Priority Poker
> 🔴 Tier 1 · _Tracker hint:_ Team-based prioritization; relative ranking

### Definition
Priority Poker is a **collaborative, game-style prioritisation** technique in the planning-poker family: participants privately choose a card (often Fibonacci-style values) for how important a story is, reveal at once, then discuss outliers and converge on a **relative ranking**. The simultaneous reveal avoids anchoring on the senior person's opinion, and the discussion surfaces hidden assumptions. Related techniques: **Planning Poker** (estimates effort/story points, not priority), the **$100 test** (each person spreads 100 points across items) and **Buy-a-Feature** (limited play money to "buy" features).

Steps: list items with acceptance criteria, each participant votes, discuss highest/lowest voters, revote (max 2 rounds), record the agreed order. Works best with 5–9 people from different functions.

### Example
Eight backlog items, 6 participants using the $100 test: Search filters get 180 points total, Dark mode 40, Invoice export 220, others share 160... The group sees Invoice export and Search filters as top; the three engineers who voted dark mode high explain a tech-debt win, which gets merged into the ranking discussion.

### In the news
See news box. Team-based review before release (a "second pair of eyes" on risky changes) is the organisational version of the same idea: do not let one voice decide.

### Interview angle
> [!question] How it is asked
> "Your stakeholders each say their feature is top priority. How do you get alignment?"

> [!tip] Strong answer includes
> - A structured, facilitated technique (poker, $100 test, MoSCoW workshop) rather than "I decide"
> - Simultaneous reveal to avoid anchoring, and discussion of outliers
> - Link to data and goals to settle ties
> - The PM owns the final call and communicates the trade-offs

---

## 8. Feature Flagging
> 🔴 Tier 1 · _Tracker hint:_ Gradual rollout; kill switch; A/B test enabler

### Definition
A **feature flag (toggle)** is a runtime condition in code that turns a feature on or off without redeploying. It separates **deploy** (code in production) from **release** (users see it). Types:
- **Release flags:** hide unfinished work; enable trunk-based development.
- **Experiment flags:** route users to variants for A/B tests.
- **Ops flags / kill switches:** instantly disable a risky feature or heavy dependency.
- **Permission flags:** enable for a plan, tenant or beta group.

Typical rollout: internal staff, 1%, 5%, 25%, 100%, watching error rate, latency and business metrics at each ring. Percentage rollout hashes the user ID so a given user stays consistently in or out.

```python
def is_enabled(flag, user_id, rollout_pct):
    bucket = hash(f"{flag}:{user_id}") % 100   # stable per user
    return bucket < rollout_pct

if is_enabled("new_checkout", user.id, rollout_pct=5):
    show_new_checkout()
else:
    show_old_checkout()
```

Costs: flag debt (remove stale flags), testing combinations, and a dependency on the flag service. Tools: LaunchDarkly, Unleash, Flagsmith, or in-house config.

### Example
A PM launches a redesigned checkout to 5% of users; conversion at 5% shows +2% with no error spike, so it moves to 25%, then 100%. Had payment errors risen, the kill switch reverts everyone to the old flow in seconds, no hotfix deploy needed.

### In the news
See news box. CrowdStrike's change to **rings and customer-controlled deployment** is feature flagging's logic applied to content updates: small blast radius first, widen on evidence, keep the ability to stop.

### Interview angle
> [!question] How it is asked
> "How would you release a risky change to 10 million users?" or "What is a kill switch?"

> [!tip] Strong answer includes
> - Deploy vs release separation
> - Staged ring rollout with defined guardrail metrics and stop conditions
> - Kill switch and A/B testing as enabled use cases
> - Housekeeping: flag ownership, expiry, cleanup

---

## 9. ⭐ Advanced: WSJF and Cost of Delay
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**WSJF (Weighted Shortest Job First)** from SAFe and Don Reinertsen's lean product economics sequences work to maximise economic value over time:

$$\text{WSJF} = \frac{\text{Cost of Delay}}{\text{Job Duration (or size)}}$$

In SAFe, **Cost of Delay = User/Business Value + Time Criticality + Risk Reduction/Opportunity Enablement**, each scored on a relative (Fibonacci) scale. Items with high delay cost and short duration go first. Intuition: if two jobs lose ₹ per week while waiting, do the shorter one first, because it frees capacity sooner. Unlike RICE, it explicitly captures **time-criticality** (a regulatory deadline, a seasonal window).

### Example
| Item | Value | Time criticality | Risk reduction | CoD (sum) | Size | WSJF |
|---|---|---|---|---|---|---|
| GST e-invoice change | 8 | 13 | 5 | 26 | 5 | **5.2** |
| New dashboard | 13 | 3 | 2 | 18 | 8 | **2.25** |
| Tech-debt cleanup | 3 | 2 | 13 | 18 | 3 | **6.0** |

Order: tech-debt cleanup (6.0), GST e-invoice (5.2), dashboard (2.25). The compliance item scores high because of the deadline.

### In the news
See news box. Risk reduction is a legitimate scoring term: the cost of not hardening a rollout process showed up as a global outage.

### Interview angle
> [!question] How it is asked
> "How do you prioritise between a revenue feature and a regulatory deadline or tech debt?"

> [!tip] Strong answer includes
> - Cost of Delay concept and the divide-by-duration logic
> - The three CoD components
> - Contrast with RICE (no explicit time or risk term)
> - Caveat: relative scoring is still subjective

---

## 10. ⭐ Advanced: Opportunity Scoring (Importance vs Satisfaction)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
From Tony Ulwick's **Outcome-Driven Innovation**: survey customers on how **important** each job-to-be-done outcome is and how **satisfied** they are with current solutions (both rated 1–10). Then:

$$\text{Opportunity} = \text{Importance} + \max(\text{Importance} - \text{Satisfaction},\ 0)$$

High importance and low satisfaction = **underserved** (opportunity); high importance and high satisfaction = **table stakes** to maintain; low importance and high satisfaction = **overserved** (risk of over-engineering or room to cut cost). It grounds prioritisation in customer data instead of internal opinion, and complements Kano.

### Example
Outcome "minimise time to reconcile invoices": Importance 9.2, Satisfaction 4.5 → Opportunity = 9.2 + (9.2 − 4.5) = **13.9**. Outcome "customise report colours": Importance 3.0, Satisfaction 7.0 → 3.0 + max(−4.0, 0) = **3.0**. Invest in reconciliation, not colours.

### In the news
See news box. Customers of security software rated availability as paramount; the outage showed an overserved feature set can still fail the one outcome that matters.

### Interview angle
> [!question] How it is asked
> "How would you use customer research to decide what to build next?"

> [!tip] Strong answer includes
> - Jobs-to-be-done outcomes rather than feature wishes
> - The importance-satisfaction gap and the formula
> - Segmenting by customer type before averaging
> - Cross-check with usage data and effort (so it feeds RICE or Value vs Effort)

---
## 🔗 Go deeper: expansion notes
- [[164 Product Discovery & User Research|Product Discovery & User Research]]
- [[167 PRDs, Stakeholder Management & Product Operations|PRDs, Stakeholder Management & Product Operations]]
