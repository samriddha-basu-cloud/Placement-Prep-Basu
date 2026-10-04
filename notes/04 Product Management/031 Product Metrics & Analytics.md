---
tags: [product-management, tier1]
area: Product Management
topic: "Product Metrics & Analytics"
tier: Tier 1
roles: PM / Consulting
status: complete
subtopics: 14
---
# Product Metrics & Analytics

⬅ [[030 Product Fundamentals & Strategy]] · [[_Index - Product Management|Product Management]] · [[032 Agile & Scrum Framework]] ➡

> **Area:** Product Management · **Priority:** 🔴 Tier 1 · **Target roles:** PM / Consulting

## Sub-topics in this note
1. [[#1. DAU / MAU / WAU]]
2. [[#2. User Retention]]
3. [[#3. Churn Rate]]
4. [[#4. CAC (Customer Acquisition Cost)]]
5. [[#5. LTV (Lifetime Value)]]
6. [[#6. Conversion Funnel Metrics]]
7. [[#7. Net Promoter Score (NPS)]]
8. [[#8. A/B Testing]]
9. [[#9. Feature Adoption Rate]]
10. [[#10. Session Duration & Depth]]
11. [[#11. Revenue Metrics]]
12. [[#12. Pirate Metrics (AARRR)]]
13. [[#13. ⭐ Advanced: Cohort, Retention Curves and Unit Economics Together]]
14. [[#14. ⭐ Advanced: Experiment Pitfalls, Metric Trees and Guardrails]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Duolingo's Q2 2025 engagement metrics
> In its Q2 2025 shareholder letter (6 August 2025) Duolingo reported **47.7 million daily active users (DAUs), up 40% year on year** (34.1 million in Q2 2024), **128.3 million monthly active users (MAUs), up 24%** (103.6 million), and **10.9 million paid subscribers, up 37%** (8.0 million). DAUs grew much faster than MAUs, so stickiness (DAU/MAU) rose to about **37%** (47.7 / 128.3). Paid subscribers of 10.9 million are about 8.5% of MAUs (10.9 / 128.3), my calculation. ([Duolingo Q2 2025 shareholder letter, SEC](https://www.sec.gov/Archives/edgar/data/1562088/000156208825000165/q2fy25duolingo6-30x25share.htm))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. DAU / MAU / WAU
> 🔴 Tier 1 · _Tracker hint:_ Daily/Weekly/Monthly Active Users; stickiness = DAU/MAU

### Definition
**Active users** count unique users who perform a defined *qualifying action* in a window: DAU (day), WAU (week), MAU (month). The definition of "active" matters (opening the app vs completing a core action such as a lesson, an order or a message).

$$\text{Stickiness}=\frac{\text{DAU}}{\text{MAU}}$$

Interpretation: DAU/MAU of 20% means the average monthly user is active about 6 days a month ($0.20\times30$). Benchmarks: social and messaging apps often above 50%; games, utilities and e-commerce much lower; the right target depends on the *natural frequency* of the need (a travel app is rarely daily). WAU/MAU is a better stickiness measure for weekly-use products.

Cautions: DAU is a vanity metric if unpaired with retention and revenue; watch for bots, multi-device double counting, and one-off spikes from notifications or promotions.

### Example
Product with 200,000 MAU and 50,000 average DAU: stickiness = 25%, i.e. users show up about 7.5 days a month. If a new feature lifts DAU to 60,000 with MAU flat at 200,000, stickiness is 30%.

### In the news
See news box. Duolingo's DAU/MAU of about 37% (47.7 / 128.3), and DAUs growing 40% against 24% for MAUs, shows deepening habit, not only a bigger user base.

### Interview angle
> [!question] How it is asked
> "DAU is flat but MAU is growing. What is happening?" or "Which engagement metric would you track for a food-delivery app?"

> [!tip] Strong answer includes
> - Defines "active" with a core action
> - Computes stickiness and links to natural frequency
> - Segments by cohort, platform, geography
> - Pairs with retention and revenue to avoid vanity conclusions

---

## 2. User Retention
> 🔴 Tier 1 · _Tracker hint:_ Day 1/7/30 retention; cohort analysis; churn reasons

### Definition
**Retention** is the share of users from a starting cohort who return after a period.

$$\text{Day-N retention}=\frac{\text{users active on day }N}{\text{users who joined (day 0)}}$$

Types: **classic (N-day)** retention, **unbounded** (returned on or after day N) and **bracket** retention. A **cohort table** groups users by sign-up week/month and tracks each cohort over time, revealing whether newer cohorts retain better after product changes. The **retention curve** should flatten into a plateau; a curve falling to zero means no product-market fit. Typical mobile-app benchmarks: roughly 25–40% on D1, 10–20% on D7, 5–10% on D30 (indicative and category dependent).

Churn reasons: poor onboarding (never reached the "aha"), missing value, bugs/performance, better alternatives, price, life change. Levers: onboarding, habit loops (notifications, streaks), content freshness, customer success.

### Example
Cohort of 10,000 installs: D1 4,000 (40%), D7 2,000 (20%), D30 1,000 (10%). A new onboarding variant gives D30 of 1,300, a lift of 3 percentage points, or 30% relative.

### In the news
See news box. Duolingo's rising DAU against slower MAU growth is a retention story: existing learners returning daily (streak mechanics) is what grows DAU fastest.

### Interview angle
> [!question] How it is asked
> "D7 retention fell from 22% to 17%. How would you investigate?"

> [!tip] Strong answer includes
> - Cohort and segment cuts (channel, version, geography, device)
> - Checks for data/tracking changes and seasonality
> - Hypotheses along the journey (onboarding, release, competitor)
> - Proposes experiments and a leading indicator

---

## 3. Churn Rate
> 🔴 Tier 1 · _Tracker hint:_ Monthly churn = lost customers / start-of-month customers

### Definition
$$\text{Churn rate}=\frac{\text{customers lost in period}}{\text{customers at start of period}}\times100$$

Related: **retention rate** $=1-$ churn; **average customer lifetime** $=1/\text{churn}$; **revenue churn** (MRR lost / starting MRR), which can differ from logo churn; **net revenue churn** can be negative when expansion exceeds losses. **Voluntary** churn (cancel) vs **involuntary** (failed payments).

Compounding: 5% monthly churn is not 60% a year; annual retention $=0.95^{12}\approx54\%$ so annual churn is about **46%**. Do not count new customers acquired in the month in the denominator.

Diagnose by cohort, plan, tenure, reason codes and exit surveys. Fixes: onboarding, usage nudges, win-back offers, dunning for failed payments, annual plans.

### Example
Start of month 2,000 subscribers; lost 100; gained 150. Churn = 100/2,000 = **5%**. Expected lifetime = 1/0.05 = 20 months. Ending customers 2,050.

### In the news
See news box. With paid subscribers growing 37% at Duolingo, small changes in monthly churn on a larger base compound quickly into revenue.

### Interview angle
> [!question] How it is asked
> "Churn went from 3% to 5% in a quarter. What do you do?"

> [!tip] Strong answer includes
> - Right formula and denominator, logo vs revenue churn
> - Voluntary vs involuntary
> - Segment analysis to localise the cause
> - Retention initiatives and how to size the prize

---

## 4. CAC (Customer Acquisition Cost)
> 🔴 Tier 1 · _Tracker hint:_ Total sales+marketing / new customers acquired

### Definition
$$\text{CAC}=\frac{\text{Total sales and marketing cost in period}}{\text{New customers acquired in period}}$$

Include salaries of sales/marketing, ad spend, tools, agency fees and commissions (fully loaded). **Blended CAC** includes organic customers; **paid CAC** counts only paid-channel customers and paid spend; compute by channel. **CAC payback (months)** $=\frac{\text{CAC}}{\text{ARPU}\times\text{gross margin}}$; SaaS targets are often under 12 months. Pair with LTV (next sub-topic): LTV:CAC above about 3 is a common benchmark.

Pitfalls: lag between spend and conversion, ignoring attribution overlap, mixing organic with paid, or optimising CAC while attracting low-quality users who churn.

### Example
Quarter spend: ads Rs 30 lakh + sales team Rs 15 lakh + tools Rs 5 lakh = Rs 50 lakh; new customers 1,000. CAC = Rs 5,000. ARPU Rs 600/month, gross margin 70% → monthly gross profit Rs 420; payback = 5,000/420 ≈ **11.9 months**.

### In the news
See news box. Strong organic daily habit (as with Duolingo) lowers blended CAC because retained users and word of mouth do part of the acquisition.

### Interview angle
> [!question] How it is asked
> "CAC doubled while conversion stayed flat. What could be going on?"

> [!tip] Strong answer includes
> - Full-cost formula and channel-level view
> - Link to LTV and payback
> - Causes: auction costs, saturation, targeting, funnel leaks
> - Mix shift toward cheaper/organic channels and referrals

---

## 5. LTV (Lifetime Value)
> 🔴 Tier 1 · _Tracker hint:_ Avg revenue per user × avg lifespan; LTV:CAC ratio (>3x target)

### Definition
**Customer lifetime value** is the total gross profit expected from a customer over their relationship.

$$\text{LTV}=\text{ARPU}\times\text{Gross margin}\times\text{Lifetime}=\frac{\text{ARPU}\times\text{GM}}{\text{churn rate}}$$

(with ARPU and churn on the same period). Use gross margin (not revenue), and discount future cash flows for long lifetimes. Rule of thumb: **LTV:CAC > 3x** and payback < 12 months; below 1x destroys value, very high (>5x) may mean under-investing in growth. Segment LTV by cohort/plan/channel; early data is predictive (use retention curves rather than assuming constant churn).

### Example
ARPU Rs 300/month, gross margin 70%, monthly churn 5%: LTV = 300 × 0.7 / 0.05 = **Rs 4,200**. CAC Rs 1,200 → LTV:CAC = **3.5x**, healthy. If churn rises to 8%: LTV = 210/0.08 = Rs 2,625 → 2.2x, below target.

### In the news
See news box. Duolingo's growth in paid subscribers (+37%) from a free user base is a freemium LTV model: a minority of users pay, so total LTV is subscription profit across all users.

### Interview angle
> [!question] How it is asked
> "How would you calculate LTV for a new subscription app and when would you stop acquiring users?"

> [!tip] Strong answer includes
> - Formula with gross margin and churn
> - LTV:CAC and payback benchmarks
> - Cohort-based, discounted estimate when data is limited
> - Levers: raise ARPU, cut churn, lower CAC

---

## 6. Conversion Funnel Metrics
> 🔴 Tier 1 · _Tracker hint:_ Impression → click → signup → activation → paid conversion

### Definition
A **funnel** shows how many users move through successive steps and where they drop. Typical stages: **Impression → Click (CTR) → Visit → Sign-up → Activation → Paid / Purchase → Repeat**.

$$\text{Step conversion}=\frac{\text{users at step } n+1}{\text{users at step } n},\qquad \text{Overall conversion}=\prod \text{step conversions}$$

CTR $=\text{clicks}/\text{impressions}$. Analyse: largest absolute drop, step with the biggest improvement potential, differences by channel/device/cohort, and time-to-convert. Improving the narrowest step by a relative 10% lifts the final result by 10%, regardless of position, so prioritise by effort and size of the opportunity. Cart abandonment, payment failure and form friction are classic leaks.

### Example
1,000,000 impressions; CTR 2% → 20,000 clicks; sign-up 10% → 2,000; activation 50% → 1,000; paid 10% → 100. Overall = 100/1,000,000 = 0.01%. Ad cost Rs 2 lakh → cost per paying customer = Rs 2,000. Raising activation from 50% to 60% gives 120 paying customers (+20%).

### In the news
See news box. For freemium products like Duolingo, a few percent of the big free base converting to paid drives growth, so funnel steps near activation are high leverage.

### Interview angle
> [!question] How it is asked
> "Sign-ups are up but paid conversions are flat. Diagnose."

> [!tip] Strong answer includes
> - Maps the funnel with step conversions and absolute numbers
> - Finds the biggest leak and segments it
> - Hypotheses (traffic quality, onboarding, pricing, bugs)
> - A/B tests to fix and a success metric

---

## 7. Net Promoter Score (NPS)
> 🔴 Tier 1 · _Tracker hint:_ % Promoters - % Detractors; follow-up qualitative

### Definition
Ask: "How likely are you to recommend us to a friend or colleague?" (0–10). **Promoters** 9–10, **Passives** 7–8, **Detractors** 0–6.

$$\text{NPS}=\%\text{Promoters}-\%\text{Detractors}\quad(\text{range } -100 \text{ to } +100)$$

Always add an open-text "why?" and close the loop with detractors. Use **transactional NPS** (after an interaction) and **relationship NPS** (periodic). Cautions: sample bias and response rate, cultural scoring differences, benchmark within the industry, and NPS is a lagging, attitudinal metric; pair with behaviour (retention, referral). Related: CSAT (satisfaction with a specific interaction), CES (effort).

### Example
200 responses: 100 promoters (50%), 60 passives (30%), 40 detractors (20%). NPS = 50 − 20 = **+30**. Moving 20 detractors to passives gives detractors 10%, NPS = 50 − 10 = +40.

### In the news
See news box. Fast-growing products still track NPS alongside usage; growth in DAU does not prove users would recommend, especially if engagement is driven by streak anxiety or notifications.

### Interview angle
> [!question] How it is asked
> "NPS is 20. Is that good and what would you do next?"

> [!tip] Strong answer includes
> - Correct calculation and scale
> - Benchmarks vs same industry and trend
> - Follow-up qualitative analysis and closing the loop
> - Links to behavioural metrics (retention, referrals)

---

## 8. A/B Testing
> 🔴 Tier 1 · _Tracker hint:_ Null hypothesis, statistical significance, sample size, p-value

### Definition
An **A/B test** randomly assigns users to control (A) and variant (B) and compares a pre-defined metric.

- **Null hypothesis (H0):** no difference between A and B. **Alternative (H1):** there is a difference.
- **p-value:** probability of seeing a difference at least this large if H0 were true. If $p<\alpha$ (usually 0.05) the result is *statistically significant*.
- **Power** (usually 80%) is the chance of detecting a real effect of a given size; **MDE** is the minimum detectable effect.
- **Sample size per group** (rule of thumb, 95% confidence, 80% power, proportions): $n\approx\frac{16\,p(1-p)}{\delta^2}$ where $\delta$ is the absolute lift to detect.
- Two-proportion z-test: $z=\frac{p_B-p_A}{\sqrt{\hat p(1-\hat p)(2/n)}}$.

Good practice: one primary metric plus guardrails, fix sample size/duration in advance (no peeking), run whole weeks, randomise at the right unit, check sample ratio mismatch, and correct for multiple comparisons. Statistical vs *practical* significance.

### Example
Baseline conversion 10%; detect +1 point: $n\approx16\times0.1\times0.9/0.01^2=14{,}400$ per group. Result: A 1,000/10,000 (10%), B 1,100/10,000 (11%). Pooled $\hat p=0.105$, $SE=\sqrt{0.105\times0.895\times0.0002}\approx0.00434$, $z=0.01/0.00434\approx2.31$, two-sided $p\approx0.02<0.05$: significant. Check guardrails (refund rate, revenue per user) before shipping.

### In the news
See news box. Companies running consumer apps at Duolingo scale test thousands of variations (notifications, streak mechanics); the discipline is choosing metrics that grow retention, not just clicks.

### Interview angle
> [!question] How it is asked
> "How would you test a new checkout page, and how do you know the result is real?"

> [!tip] Strong answer includes
> - Hypothesis, primary metric, guardrails, randomisation unit
> - Sample size and duration set in advance
> - p-value interpretation without misstatement
> - Pitfalls: peeking, novelty effect, multiple tests, network effects

---

## 9. Feature Adoption Rate
> 🔴 Tier 1 · _Tracker hint:_ Users using feature / total users × 100

### Definition
$$\text{Feature adoption}=\frac{\text{users who used the feature in the period}}{\text{total (or eligible) active users}}\times100$$

Choose the denominator carefully: *eligible* users (those who could see it) gives a truer rate. Complementary metrics: **time to first use**, **repeat usage / frequency**, **feature stickiness** (feature DAU/MAU), **retention of feature users vs non-users** (watch selection bias), and **depth** (share who complete the key action). Distinguish **awareness** (saw it), **trial** (used once) and **adoption** (habitual use). Low adoption causes: discoverability, poor onboarding, wrong problem, friction.

### Example
App with 8,000 monthly active users; 2,400 used "saved lists" at least once → 30% adoption. Of these, 900 used it in 3 of 4 weeks → habitual adoption = 900/8,000 = 11.25%. Feature users retained at 70% vs 45% for non-users, but heavy users self-select, so run an experiment to confirm causality.

### In the news
See news box. As Duolingo added features around its core streak and lessons, adoption among DAUs, not total installs, decides whether a feature earns its place.

### Interview angle
> [!question] How it is asked
> "A new feature has 5% adoption. Is that good? What would you do?"

> [!tip] Strong answer includes
> - Defines adoption for eligible users and a time window
> - Benchmarks vs expected usage frequency
> - Diagnoses awareness, usability, value
> - Experiments to test impact on retention or revenue

---

## 10. Session Duration & Depth
> 🔴 Tier 1 · _Tracker hint:_ Engagement signals; pages per session, scroll depth

### Definition
Engagement metrics describe *how* users use the product in a visit.

- **Session duration** $=\text{total time}/\text{number of sessions}$; **sessions per user** per day/week.
- **Depth:** pages/screens per session, scroll depth, actions per session, completion of a key flow.
- **Bounce rate:** single-page sessions.
- **Time spent** per DAU.

Higher is not always better: a checkout or support flow should be short; a streaming or content app benefits from longer sessions. Prefer *value-weighted* engagement (tasks completed, orders, lessons finished) and pair with satisfaction. Beware of confusing slow, frustrating experiences with engagement. Report median, not just mean, because sessions are skewed.

### Example
10,000 sessions with total time 1,200,000 seconds → average 120 seconds (2 min). After a redesign, the average is 90 seconds but completed orders per session rise from 0.12 to 0.18. Engagement quality improved (+50% orders per session) even though time fell.

### In the news
See news box. Duolingo's daily-habit design shows that short, frequent sessions can matter more than long ones.

### Interview angle
> [!question] How it is asked
> "Average session time fell 15%. Is that bad?"

> [!tip] Strong answer includes
> - Context: is longer better for this product?
> - Pairs time with outcome metrics
> - Segments (new vs returning, device)
> - Checks performance issues or tracking changes

---

## 11. Revenue Metrics
> 🔴 Tier 1 · _Tracker hint:_ MRR, ARR, ARPU, expansion MRR, churn MRR

### Definition
Subscription revenue metrics:

- **MRR** (monthly recurring revenue) = sum of monthly subscription values; **ARR** $=\text{MRR}\times12$.
- **New MRR, Expansion MRR** (upgrades, upsell), **Contraction MRR** (downgrades), **Churned MRR** (cancellations).
- Net new MRR $=\text{New}+\text{Expansion}-\text{Contraction}-\text{Churned}$.
- **ARPU** $=\text{Revenue}/\text{active users}$; **ARPPU** per *paying* user.
- **Net revenue retention (NRR)** $=\frac{\text{Start MRR}+\text{Expansion}-\text{Contraction}-\text{Churned}}{\text{Start MRR}}$ (excludes new customers); NRR above 100% means existing customers grow on their own. **Gross revenue retention** excludes expansion (max 100%).
- Also GMV vs net revenue (take rate) for marketplaces.

### Example
Start MRR Rs 10 lakh; new 1.5; expansion 0.5; contraction 0.1; churned 0.6 (all lakh). Ending MRR = 10 + 1.5 + 0.5 − 0.1 − 0.6 = **Rs 11.3 lakh**; ARR = Rs 135.6 lakh. NRR = (10 + 0.5 − 0.1 − 0.6)/10 = **98%**; GRR = (10 − 0.1 − 0.6)/10 = 93%.

### In the news
See news box. Duolingo's 10.9 million paid subscribers against 128.3 million MAUs shows a low-conversion, high-scale freemium model: ARPU across all users is low, ARPPU much higher.

### Interview angle
> [!question] How it is asked
> "MRR grew 8% but NRR is below 100%. Is the business healthy?"

> [!tip] Strong answer includes
> - Decomposes MRR into new, expansion, contraction, churn
> - Interprets NRR/GRR correctly
> - Notes growth is acquisition-dependent when NRR under 100%
> - Proposes expansion and retention levers

---

## 12. Pirate Metrics (AARRR)
> 🔴 Tier 1 · _Tracker hint:_ Acquisition, Activation, Retention, Referral, Revenue

### Definition
Dave McClure's **AARRR** framework covers the customer lifecycle:

| Stage | Question | Example metrics |
|---|---|---|
| Acquisition | How do users find us? | Visitors, installs, CAC by channel |
| Activation | Do they have a great first experience? | % reaching "aha", time to first value |
| Retention | Do they come back? | D1/D7/D30, churn, DAU/MAU |
| Referral | Do they tell others? | Invites per user, viral coefficient, NPS |
| Revenue | Do we make money? | ARPU, conversion to paid, LTV |

Use it to find the **weakest stage** (the bottleneck) and prioritise: fixing leaky retention before pouring money into acquisition. Order varies (some products monetise earlier). Pair with a North Star ([[030 Product Fundamentals & Strategy]]).

### Example
Mobile game: 100,000 installs (acquisition), 60% complete tutorial (activation), D7 retention 8% (retention, the leak), 3% invite friends (referral), 2% pay (revenue). Priority: improve D7 (onboarding, daily rewards) before buying more installs, since each installed user is lost quickly.

### In the news
See news box. Duolingo's results span the stack: acquisition (MAU +24%), retention/engagement (DAU +40%), revenue (paid subscribers +37%).

### Interview angle
> [!question] How it is asked
> "Use AARRR to diagnose why a fintech app isn't growing."

> [!tip] Strong answer includes
> - All five stages with a metric each
> - Finds the bottleneck using data
> - Prioritises by impact and effort
> - Tailors the framework to the product's model

---

## 13. ⭐ Advanced: Cohort, Retention Curves and Unit Economics Together
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A unified view links retention to money. Build a **cohort revenue table** (cohort × month), compute the cohort's cumulative gross profit per user, and compare with CAC to find the **payback month**.

With retention $r_t$ (share of cohort still active in month $t$), ARPU $a$ and gross margin $m$:

$$\text{Cumulative profit per acquired user}=\sum_{t=0}^{T} a\,m\,r_t$$

If retention plateaus at $r_\infty>0$, LTV keeps growing; with geometric churn $c$, $\text{LTV}=am/c$. Also check **cohort quality by channel** (CAC may be low but retention poor) and **contribution margin** after variable costs. Real businesses have *improving or worsening cohorts*, so do not extrapolate a single average.

### Example
a = Rs 300, m = 70%, so profit per active user-month = Rs 210. Retention months 0–5: 100%, 60%, 45%, 38%, 34%, 32%. Cumulative profit: 210 × (1 + 0.6 + 0.45 + 0.38 + 0.34 + 0.32) = 210 × 3.09 = Rs 649. With CAC Rs 800, payback is not reached in 6 months; if retention plateaus at 30%, each extra month adds Rs 63, so payback in about (800 − 649)/63 ≈ 2.4 more months, around month 8–9.

### In the news
See news box. Strong public-company disclosures of DAU, MAU and subscribers let outsiders approximate cohort economics; internal teams have the cohort detail.

### Interview angle
> [!question] How it is asked
> "How would you decide if a user-acquisition channel is worth scaling?"

> [!tip] Strong answer includes
> - Cohort-based LTV by channel versus its CAC
> - Payback and plateau considerations
> - Sensitivity to retention assumptions
> - Scale only if marginal CAC stays below marginal LTV

---

## 14. ⭐ Advanced: Experiment Pitfalls, Metric Trees and Guardrails
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Metric tree:** decompose the goal into drivers, e.g. Revenue = Users × Conversion × ARPU, and Users = New + Returning. Teams own inputs. **Guardrail metrics** (latency, refunds, unsubscribes, NPS) protect against local wins that hurt the system.

Experiment pitfalls:
- **Peeking** and stopping early inflates false positives.
- **Multiple comparisons:** testing 20 metrics at $\alpha=0.05$ gives about one false positive on average; use a Bonferroni correction ($\alpha/k$) or pre-register the primary metric.
- **Novelty and primacy effects**, **Simpson's paradox** across segments, **sample ratio mismatch**.
- **Network effects / interference** in marketplaces and social products: randomise by cluster or geography.
- **Underpowered tests:** a "no difference" result may be inconclusive.
- **Metric gaming** (Goodhart's law).
When not to A/B test: tiny traffic, one-way-door decisions, ethical issues.

### Example
10 secondary metrics tested at $\alpha=0.05$: chance of at least one false positive $=1-0.95^{10}\approx40\%$. Bonferroni threshold: 0.05/10 = **0.005** per metric.

### In the news
See news box. Large consumer apps rely on guardrails (user trust, wellbeing) so that engagement gains from nudges do not erode long-term retention.

### Interview angle
> [!question] How it is asked
> "Your A/B test shows +3% on the primary metric but -1% on retention. Ship it?"

> [!tip] Strong answer includes
> - Looks at guardrails and long-term effects before shipping
> - Checks significance, power and segment effects
> - Considers a holdout or longer run
> - Makes an explicit trade-off decision with stakeholders

---
## 🔗 Go deeper: expansion notes
- [[214 Causal Inference & Experimentation Beyond A-B Tests|Causal Inference & Experimentation Beyond A-B Tests]]
- [[166 AI Product Management - LLM Products, Evals & Economics|AI Product Management - LLM Products, Evals & Economics]]
