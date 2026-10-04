---
tags: [product-management, tier1]
area: Product Management
topic: "PM Interview Types & Answer Frameworks"
tier: Tier 1
roles: Product Manager
status: complete
subtopics: 13
---
# PM Interview Types & Answer Frameworks

⬅ [[036 Go-To-Market Strategy]] · [[_Index - Product Management|Product Management]] · [[164 Product Discovery & User Research]] ➡

> **Area:** Product Management · **Priority:** 🔴 Tier 1 · **Target roles:** Product Manager

## Sub-topics in this note
1. [[#1. The Map of PM Interview Types]]
2. [[#2. Product Sense and Design: CIRCLES and User–Segment–Need–Solution]]
3. [[#3. Product Improvement]]
4. [[#4. Root-Cause Analysis: Metric Drop and the Diagnostic Tree]]
5. [[#5. Success Metrics]]
6. [[#6. Execution and Prioritisation]]
7. [[#7. Strategy and Market Entry]]
8. [[#8. Estimation Questions for PMs]]
9. [[#9. Technical Questions for PMs]]
10. [[#10. Behavioural Questions for PMs]]
11. [[#11. AI-Product Questions]]
12. [[#12. Answer Delivery and Common Mistakes Across Types]]
13. [[#13. ⭐ Advanced: Company-Style Prompt Bank and Scoring Rubric]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the Indian consumer-internet and AI products that PM interviewers use as prompts
> **UPI at scale, with a market-share cap.** Wikipedia's UPI page records about **20 billion transactions worth ₹25 trillion in August 2025** (roughly 7,500 a second) and the NPCI **30% market-share cap** on any single payment app, with the compliance deadline extended from December 2023 to **31 December 2024** (it has been extended more than once, so check the latest NPCI circular). ([Wikipedia: UPI](https://en.wikipedia.org/wiki/Unified_Payments_Interface)) **PhonePe** converted to a public company in April 2025 and filed confidentially for an IPO in September 2025 (reported target size about $1.5 billion; about 600 million registered users). ([Wikipedia: PhonePe](https://en.wikipedia.org/wiki/PhonePe)) **Paytm Payments Bank** was ordered by the RBI on 31 January 2024 to stop most activities from 29 February (later extended to 15 March 2024); Zomato bought Paytm's ticketing business for about ₹2,048 crore in August 2024. ([Wikipedia: Paytm](https://en.wikipedia.org/wiki/Paytm))
>
> **Quick commerce reaches break-even.** Blinkit's Q3 FY26 results (21 January 2026): operating revenue **₹12,256 crore (+24% quarter on quarter)**, **adjusted EBITDA of ₹4 crore (margin 0.03%) against a ₹156 crore loss the previous quarter**, **2,027 dark stores**, and about 90% of net order value on its own inventory. ([Inc42](https://inc42.com/buzz/eternal-q3-blinkit-hyperpure-achieve-adjusted-ebitda-profitability/)) **Swiggy** listed in November 2024 at ₹390 a share (about $11.3 billion), had Instamart in 127 cities and third in share behind Blinkit and Zepto by July 2025, and shut down its **Genie** hyperlocal delivery service in May 2025, a real product-prioritisation decision. ([Wikipedia: Swiggy](https://en.wikipedia.org/wiki/Swiggy))
>
> **AI products priced for India.** OpenAI launched **ChatGPT Go in India at ₹399 a month in August 2025, with UPI payment support**, and the ChatGPT page reports **900 million weekly active users in February 2026**. ([Wikipedia: ChatGPT](https://en.wikipedia.org/wiki/ChatGPT))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The Map of PM Interview Types
> 🔴 Tier 1 · _Key points:_ Product sense, improvement, metrics, execution, strategy, estimation, technical, behavioural, AI

### Definition
PM interviews rotate through a small set of question types. Each tests a different muscle; recognise the type in the first 10 seconds and use its framework.

| Type | Typical prompt | What is tested | Core framework |
|---|---|---|---|
| **Product sense / design** | "Design a product for X" | User empathy, creativity, prioritisation | CIRCLES or user–segment–need–solution |
| **Product improvement** | "How would you improve Y?" | Diagnosis of pain points, trade-offs | Journey, pain points, fixes, metrics |
| **Root cause / metric drop** | "Orders dropped 8%. Why?" | Structured analytical thinking | Diagnostic tree: define, data, internal vs external, segment, funnel |
| **Success metrics** | "How do you measure Z?" | Metric design, goals vs guardrails | Goal, funnel, north star, inputs, guardrails |
| **Execution / prioritisation** | "You have 5 features and 2 engineers" | Trade-offs, stakeholder judgment | RICE, impact-effort, opportunity cost |
| **Strategy / market entry** | "Should company A enter B?" | Business judgment, competitive thinking | 3C, build-buy-partner, economics, risks |
| **Estimation** | "How many X in India?" | Structured numeracy | Top-down and bottom-up ([[028 Guesstimates & Market Sizing]]) |
| **Technical** | "How does UPI work?" | Technical literacy and trade-offs | Components, flow, failure modes ([[035 Technical Understanding (APIs, SDLC)]]) |
| **Behavioural** | "Tell me about a conflict" | Leadership, ownership, learning | STAR ([[049 STAR Stories — Leadership & Conflict]]) |
| **AI product** | "Design an AI assistant for..." | Judgment on accuracy, cost, safety | Value, evals, cost, fallback ([[166 AI Product Management - LLM Products, Evals & Economics]]) |

Round structure at Indian product companies (Swiggy, Flipkart, PhonePe, CRED, Paytm and others) typically combines several types in 45–60 minute rounds; the exact mix varies by company and level, so ask your recruiter. Fundamentals behind all of them: [[030 Product Fundamentals & Strategy]], [[031 Product Metrics & Analytics]], [[034 Prioritization Frameworks]].

### Example
Prompt: "Swiggy's order volume dipped. What do you do?" It is a **metric drop** question, not a strategy question: start by clarifying the metric and time window, not by proposing features. Mis-typing the question is the commonest early error.

### In the news
See news box. Each news item suggests a type: Blinkit's break-even (metrics, unit economics), Swiggy's Genie shutdown (execution and prioritisation), PhonePe and UPI cap (strategy and technical), ChatGPT Go in India (AI product and pricing).

### Interview angle
> [!question] How it is asked
> "How do you prepare for PM interviews?" (and the first move in every round is to classify the question)

> [!tip] Strong answer includes
> - Names the question type and the framework before answering
> - Clarifies, structures, and states a hypothesis early
> - Quantifies where possible; summarises at the end
> - Mixes frameworks with product judgment instead of reciting them

---
## 2. Product Sense and Design: CIRCLES and User–Segment–Need–Solution
> 🔴 Tier 1 · _Key points:_ Clarify, pick a user segment, rank needs, 3 solutions, choose one, define success

### Definition
**What is tested:** empathy, structured creativity, prioritisation, and the ability to commit. **Frameworks:**

- **CIRCLES** (popularised by Lewis C. Lin): **C**omprehend the situation, **I**dentify the customer, **R**eport customer needs, **C**ut through prioritisation, **L**ist solutions, **E**valuate trade-offs, **S**ummarise.
- **User–segment–need–solution:** goals, users and segments (pick one), pain points and needs (rank), 3 solutions (prioritise one), success metrics and risks. It is simpler and fits a 30-minute answer.

Spend about 20% of time on clarifying and the user, 30% on needs, 30% on solutions, and 20% on metrics and risks. Link to research and design methods: [[033 Design Thinking & UX]], [[164 Product Discovery & User Research]].

**Common mistakes:** jumping to a solution; picking "everyone" as the user; a feature list with no prioritisation; no success metric; ignoring business constraints and feasibility; copying a competitor's feature without a user need.

### Example
**Prompt:** "Design a savings product for delivery partners on PhonePe."
1. **Clarify:** goal is to drive engagement and deposit balances; assume UPI app and regulated partner (mutual fund or bank) for the money; India.
2. **Segments:** delivery partners, cab drivers, freelancers; pick **delivery partners**: irregular daily income, high UPI use (daily payouts), often no savings buffer, low financial literacy.
3. **Needs (ranked):** (a) a cushion for income dips and emergencies; (b) saving without effort; (c) quick access when needed; (d) trust: no lock-in surprises.
4. **Solutions:** (A) auto-save a chosen % (say 5%) of each payout into a goal wallet; (B) round-up on every UPI spend; (C) a savings group with a nudge. **Choose A**: it removes effort, matches income timing and has the strongest effect on the top need; add a free emergency withdrawal to address (c).
5. **Metrics:** north star = monthly net savings per active saver; funnel = opt-in rate, retention at 3 months, withdrawal rate; guardrails = complaint rate, payout-app engagement, fraud. Illustrative size: 1 lakh workers saving 5% of ₹18,000 a month = ₹9 crore of monthly inflow (1,00,000 × 18,000 × 0.05).
6. **Risks:** regulatory limits on deposit-like features, partner dependency, low trust; mitigate with a regulated partner and transparent terms.

### In the news
See news box. UPI's scale (about 20 billion transactions in August 2025) is what makes payout-triggered, effortless features possible; the NPCI 30% cap is a platform constraint every payment-app PM must design around.

### Interview angle
> [!question] How it is asked
> "Design a product for senior citizens to pay bills." or "Design a feature to increase credit-card repayment on time."

> [!tip] Strong answer includes
> - Clarifying questions and a stated goal
> - One chosen segment with a reason; ranked needs
> - Three distinct solutions, one picked with trade-offs
> - Success metrics, guardrails and risks

---
## 3. Product Improvement
> 🔴 Tier 1 · _Key points:_ Journey, pain points, root cause, 2–3 fixes, pick one, metrics

### Definition
**What is tested:** diagnosing a real problem before fixing it; trade-offs; data sense. **Framework:** (1) clarify the product, goal and user; (2) map the **journey** (discover, decide, transact, receive, support); (3) find **pain points** with evidence (reviews, drop-off data, support tickets, research); (4) choose the **highest-impact** problem (frequency × severity × business value); (5) propose **2–3 fixes** and pick one; (6) metrics, experiment and risks.

Differences from design: the product exists, so use **data and journeys**; improvement should be specific (a step in a flow) not a new product. Compare options with [[034 Prioritization Frameworks]].

**Common mistakes:** "add AI" as the answer; improving something users do not care about; ignoring operational and cost implications; no baseline or measure of improvement.

### Example
**Prompt:** "How would you improve returns on Flipkart?" (a marketplace-style problem)
1. **Goal:** reduce friction and cost while protecting trust. **Users:** buyers returning damaged, wrong or unfit items (fashion size returns are common).
2. **Journey:** initiate return, schedule pickup, hand over, wait for refund, resolution. **Pain points (hypotheses to validate):** unclear pickup windows, missed pickups, refund delay (the biggest anxiety: "where is my money?"), and size mismatch causing repeat returns.
3. **Pick:** refund speed after pickup (high frequency and high emotional impact; also reduces support contacts).
4. **Solutions:** (A) refund to wallet or UPI as soon as the courier scans the item (instant, with risk controls for high-risk cases); (B) live pickup tracking; (C) pre-purchase size prediction to avoid the return. **Choose A first** because it fixes the biggest emotion, with C as the long-term cost lever.
5. **Metrics:** refund time (median and P90), support contacts per return, repeat purchase after return; guardrails = fraud and abuse rate, cost of refund-before-receipt exposure, seller disputes.
6. **Experiment:** staged rollout to low-risk customers, with a holdout.

### In the news
See news box. Swiggy's Instamart competes in speed and reliability: improvements there mean fulfilment and substitution, not only app screens, which is a reason to tie product answers to operations ([[129 E-commerce & Quick-Commerce Fulfilment]]).

### Interview angle
> [!question] How it is asked
> "How would you improve Google Maps for Indian two-wheeler riders?" or "How would you improve the checkout of a food-delivery app?"

> [!tip] Strong answer includes
> - A journey with evidence-based pain points
> - Prioritised problem choice with a reason
> - Two or three fixes compared; one chosen
> - Metrics, baseline and experiment plan; guardrails

---
## 4. Root-Cause Analysis: Metric Drop and the Diagnostic Tree
> 🔴 Tier 1 · _Key points:_ Define, verify data, internal vs external, segment, funnel, then hypothesise

### Definition
**What is tested:** structured analytical reasoning under ambiguity. **Diagnostic tree:**

1. **Clarify the metric:** definition, time window, magnitude, sudden or gradual, all segments or some.
2. **Check data and measurement:** tracking bug, logging change, dashboard error, delayed data.
3. **External factors:** seasonality, holidays, weather, competitor moves, regulation, macro shocks.
4. **Internal changes:** releases, experiments, pricing, promotions, marketing spend, supply and operations changes, outages.
5. **Segment:** platform (Android, iOS, web), version, geography, user cohort (new vs existing), channel, category.
6. **Funnel decomposition:** $\text{Orders}=\text{Sessions}\times\text{Cart rate}\times\text{Checkout-start rate}\times\text{Payment success}$ find the step that moved.
7. **Hypothesis, validation and action:** the likely cause, the data that would confirm it, the fix and a monitor.

**Common mistakes:** listing causes without a structure; ignoring data quality; not segmenting; guessing a single cause; not proposing the next step. See [[031 Product Metrics & Analytics]] (funnels and metric trees) and [[045 SQL for Operations Analytics]] for the queries.

### Example
**Prompt:** "Weekly orders on a food-delivery app fell 8% (1.00 million to 0.92 million). Why?"
- **Clarify:** week-on-week, all cities, all categories? No known release? The interviewer says: sudden, across cities, started Tuesday.
- **Data check:** orders are down in two independent systems, so not a tracking bug.
- **Decompose:** sessions 5.0M to 4.9M (−2%); session-to-cart rate flat at 40%; cart-to-order fell from 50% to 47%: orders = 4.9 × 0.40 × 0.47 = 0.92M ✓ versus 5.0 × 0.40 × 0.50 = 1.00M. **The drop is in cart-to-order, not in traffic.**
- **Split cart-to-order** = checkout-start rate × payment success: 0.532 × 0.94 = 0.50 before, 0.534 × 0.88 = 0.47 after. **Checkout-start unchanged; payment success fell from 94% to 88%** (payment failures doubled from 6% to 12%).
- **Segment:** Android UPI-intent flows on one bank app, started with a release on Tuesday.
- **Impact:** restoring payment success to 94% would bring orders to about 0.98M, recovering about 63,000 of the roughly 79,000 lost; the remaining ~2% is the session decline (marketing or seasonality).
- **Action:** roll back or hotfix the payment flow, add a UPI retry and payment-method fallback, alert on payment success per bank and platform, and compensate affected users.

### In the news
See news box. Paytm's 2024 RBI restrictions are an external-regulatory cause that would show up as a metric drop in payments products; the same decomposition (users × frequency × success rate) applies.

### Interview angle
> [!question] How it is asked
> "DAU dropped 10% yesterday. What do you do?" or "UPI success rate for our app fell. Why?"

> [!tip] Strong answer includes
> - Clarifies the metric and checks data quality first
> - Separates external from internal causes; segments and decomposes the funnel
> - Quantifies each step to localise the drop
> - Ends with the likely cause, confirming evidence, fix and a monitor

---
## 5. Success Metrics
> 🔴 Tier 1 · _Key points:_ Goal, user value, north star, input metrics, guardrails; unit economics

### Definition
**What is tested:** whether you can define success precisely and avoid vanity or gameable metrics. **Framework:**

1. **Goal:** the business and user objective of the product.
2. **User and value:** who gets value, and what action signals it?
3. **North star:** one metric capturing delivered value (e.g. weekly orders per active user, successful payments, listening hours).
4. **Input metrics:** the levers that move it (acquisition, activation, frequency, conversion).
5. **Health metrics / guardrails:** quality, cost, latency, complaints, abuse, long-term retention.
6. **Counter-metrics:** the thing the target might harm (growth versus margin; speed versus accidents).
7. **Targets and time frame;** how to measure (instrumentation, experiment).

Use the AARRR funnel and cohorts ([[031 Product Metrics & Analytics]]) and the north-star discussion in [[030 Product Fundamentals & Strategy]]. **Common mistakes:** a single vanity metric; no guardrails; ignoring unit economics; unmeasurable metrics; mixing outputs and inputs.

### Example
**Prompt:** "How would you measure the success of a 10-minute grocery delivery product?"
- **Goal:** build a repeat habit profitably. **North star:** orders per active user per month (habit), subject to contribution margin ≥ 0.
- **Inputs:** new-user conversion, assortment fill rate, delivery time (median, P90), availability at peak hours, repeat rate at 30/60 days.
- **Guardrails:** delivery safety incidents, rider earnings and attrition, complaint and refund rate, wastage.
- **Unit economics (illustrative):** AOV ₹600; gross margin plus fees 22% = ₹132; ad income 3% = ₹18; delivery cost ₹45; packaging and wastage ₹12; discounts ₹20 → contribution = 132 + 18 − 45 − 12 − 20 = **₹73 per order (12.2% of AOV)**. If a dark store's fixed daily cost is ₹60,000, break-even = 60,000 / 73 ≈ **822 orders a day**. Metric implication: store-level orders per day against 822 is a leading indicator of whether a store is profitable.

### In the news
See news box. Blinkit reported adjusted EBITDA of ₹4 crore (0.03% margin) on ₹12,256 crore revenue after moving about 90% of net order value to an inventory-led model: the interview-ready lesson is that the north star (orders) must be paired with a margin metric.

### Interview angle
> [!question] How it is asked
> "How would you know if UPI Autopay is successful?" or "What metrics would you track for a new subscription?"

> [!tip] Strong answer includes
> - A clear goal and one north-star metric with a reason
> - Input and guardrail metrics; counter-metric
> - Unit economics or a link to revenue and cost
> - How to measure it and what target or time frame

---
## 6. Execution and Prioritisation
> 🔴 Tier 1 · _Key points:_ Goals, RICE or impact-effort, dependencies, trade-offs, stakeholders

### Definition
**What is tested:** judgment about what to do and not do, and how to align people. **Framework:** (1) confirm the goal and constraints (engineering capacity, deadline, compliance); (2) list options with **impact, effort, confidence, reach**; (3) score with **RICE** (Reach × Impact × Confidence ÷ Effort) or an impact-effort grid; (4) consider **dependencies, risk and strategic fit** (moats, platform needs); (5) decide, say what you are **not** doing, and plan communication; (6) define success metrics and check-in points. See [[034 Prioritization Frameworks]] for the methods.

$$RICE=\frac{\text{Reach}\times\text{Impact}\times\text{Confidence}}{\text{Effort}}$$

**Common mistakes:** treating scores as truth (they are a conversation aid); ignoring dependencies and compliance; saying yes to everything; not naming the trade-off; skipping stakeholder alignment ([[167 PRDs, Stakeholder Management & Product Operations]]).

### Example
**Prompt:** "Quarter planning: one squad (2 engineers), four candidate features on a food-delivery app. What do you build?"

| Feature | Reach (users/quarter) | Impact (0.25–3) | Confidence | Effort (person-months) | RICE |
|---|---|---|---|---|---|
| A. UPI retry and fallback on failure | 300,000 | 2 | 80% | 1 | 300,000 × 2 × 0.8 / 1 = **480,000** |
| B. Voice search | 120,000 | 1 | 50% | 3 | 20,000 |
| C. One-tap reorder shortcut | 250,000 | 1 | 80% | 0.5 | **400,000** |
| D. Gift cards | 100,000 | 2 | 50% | 4 | 25,000 |

Build **A and C** first (1.5 person-months of effort, well within the squad's capacity); defer B and D unless strategic. Caveats: A's reach and impact tie directly to the payment-success finding in sub-topic 4, so confidence is high; validate C's impact by an experiment; communicate to the stakeholder who wanted gift cards what data would change the decision (for example a partner commitment).

### In the news
See news box. Swiggy's May 2025 shutdown of Genie, the hyperlocal delivery service, is a real stop decision (interpretation: it concentrates effort on food delivery and quick commerce). The interview version: "What would you stop, and why?"

### Interview angle
> [!question] How it is asked
> "You have capacity for two of these five features. Which do you choose?" or "How do you say no to a senior stakeholder?"

> [!tip] Strong answer includes
> - A stated goal and decision criteria before scoring
> - A transparent score with assumptions; sanity-checks the ranking
> - Names what is deprioritised and why; dependencies and risk
> - Stakeholder communication and a measurement plan

---
## 7. Strategy and Market Entry
> 🔴 Tier 1 · _Key points:_ Market, customer, competition, capabilities; build-buy-partner; economics; risks

### Definition
**What is tested:** business judgment and competitive reasoning at product level. **Framework (3C plus economics):**

1. **Market:** size, growth, structure, regulation, economics ([[027 Case Interview — Market Entry]] for the market-entry skeleton).
2. **Customer:** segments, unmet needs, willingness to pay.
3. **Competition:** incumbents, substitutes, entry barriers, likely reactions.
4. **Company:** capabilities, assets, advantages (data, distribution, brand, supply).
5. **Options:** build, buy, partner; sequencing and pilot.
6. **Economics:** revenue model, unit economics, investment, break-even.
7. **Risks and recommendation:** go, no-go or test, with kill criteria.

Platform and marketplace strategies are covered in [[165 Platform & Marketplace Product Strategy]]; go-to-market is in [[036 Go-To-Market Strategy]].

**Common mistakes:** a generic 3C recitation with no recommendation; ignoring company-specific advantages; no economics; ignoring regulation (essential in fintech and health).

### Example
**Prompt:** "Should a large e-commerce marketplace launch a 10-minute delivery service?"
- **Market and customer:** high-frequency urban demand; but the value is concentrated in dense neighbourhoods with high incomes.
- **Competition:** incumbents scaling dark stores with density advantages; the news shows Blinkit with 2,027 stores and only just break-even.
- **Company:** strengths (existing customers, brand, logistics know-how) versus the need for a dense dark-store network and inventory management.
- **Economics:** contribution per order of about ₹73 in the illustrative model; break-even at about 822 orders per dark store per day; so the plan needs enough density to reach that in each store.
- **Options:** (1) build in 2–3 dense pincodes as a pilot; (2) partner with local retailers; (3) acquire a smaller player.
- **Recommendation:** go with a limited pilot in the top 2–3 dense areas, with explicit kill criteria: if stores do not reach about 60% of break-even orders within six months or contribution per order stays negative, stop. Note what is not known: real costs and competitor reactions.

### In the news
See news box. Blinkit's first break-even came after a shift to an inventory-led model at about 90% of net order value, which shows how much the model, not just the demand, drives the economics; Swiggy ranks third in quick commerce share (per Wikipedia) and shut a non-core service.

### Interview angle
> [!question] How it is asked
> "Should PhonePe launch a credit product?" or "Should CRED enter UPI payments?"

> [!tip] Strong answer includes
> - Structure plus a clear recommendation, not a list
> - Company-specific advantages and constraints (regulation, data, trust)
> - Rough economics and break-even; pilot and kill criteria
> - Competitive reaction and risks

---
## 8. Estimation Questions for PMs
> 🔴 Tier 1 · _Key points:_ Top-down and bottom-up; state assumptions; cross-check; connect to the decision

### Definition
**What is tested:** structured numeracy and sensible assumptions; PM estimation often ends in a **decision** ("is it worth building?"). **Approach:** clarify scope; choose a method (top-down from population, bottom-up from units; see [[028 Guesstimates & Market Sizing]], [[102 Guesstimate Framework]], [[103 Key India Data Points to Memorize]]); segment; calculate; **sanity-check against a second method**; state the "so what".

**Common mistakes:** unsegmented single rates; unstated assumptions; false precision; no cross-check; an estimate disconnected from the decision.

### Example
**Prompt:** "Estimate UPI transactions in India per day."
- **Bottom-up (assumptions):** adults ≈ 1.0 billion; smartphone-using adults ≈ 650 million; share who use UPI at least monthly ≈ 45% → ≈ 290 million UPI users; average transactions per active user per day ≈ 2.2 (many pay daily for groceries, transport, food, P2P). Total ≈ 290 million × 2.2 ≈ **640 million transactions a day**.
- **Cross-check:** the reported figure for August 2025 was about 20 billion a month (Wikipedia), i.e. 20 billion / 31 = **645 million a day**, so the estimate is close. Reported average ticket ≈ ₹25 trillion / 20 billion = ₹1,250 per transaction.
- **So what:** at 2.2 transactions per active user per day and a cap of 30% share per app, a single app can have at most about 190 million transactions a day: the cap binds large apps and is a product constraint (engagement per user, not only user count).

### In the news
See news box. The UPI figure (about 20 billion transactions in August 2025) is a ready anchor for payment-related estimates; verify the latest NPCI data before an interview.

### Interview angle
> [!question] How it is asked
> "How many food deliveries happen in Bengaluru per day?" or "Estimate the revenue potential of a new feature."

> [!tip] Strong answer includes
> - Clear segmentation and stated assumptions
> - Sensible numbers, rounded, with a cross-check
> - A sensitivity (what if one assumption is off by 2x)
> - A conclusion that informs the product decision

---
## 9. Technical Questions for PMs
> 🔴 Tier 1 · _Key points:_ Components, request flow, failure modes, trade-offs; speak at PM depth

### Definition
**What is tested:** whether you can work credibly with engineers: understanding of APIs, data flows, latency, reliability, security and trade-offs. **Framework:** (1) restate the user-visible behaviour; (2) draw the **components and the request flow**; (3) identify **failure points and states** (timeouts, retries, idempotency); (4) discuss **trade-offs** (latency vs cost vs consistency vs security); (5) say what you would ask engineering; (6) tie back to user impact and metrics. Background: [[035 Technical Understanding (APIs, SDLC)]], [[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses]].

**Common mistakes:** too deep or too shallow; no failure modes; unsupported claims about how a specific company's system works (say "typically").

### Example
**Prompt:** "A user's UPI payment shows 'pending'. What is happening, and what should the product do?"
- **Typical flow (simplified):** payer's app sends a payment request via its PSP bank to the NPCI switch; the switch routes it to the payer's bank (debit) and the payee's bank (credit), and the result returns to both apps.
- **Pending state:** the response is delayed or lost (timeout) so the app does not know whether the debit or credit happened.
- **Product response:** show an honest "pending" with a clear time expectation; check status through the **status-enquiry (reconciliation) call** rather than retrying blindly; protect against double charges with **idempotency**; auto-refund or confirm within a stated time; notify the user; track the pending rate as a metric.
- **Metrics:** payment success rate, pending rate and median resolution time, support contacts per pending payment; compare by bank and by app version (links back to the root-cause example in sub-topic 4).

### In the news
See news box. As UPI volume reaches about 20 billion transactions a month and the market-share cap applies, reliability and failure handling in the payment flow become differentiators.

### Interview angle
> [!question] How it is asked
> "What happens when you tap 'Pay' in a food-delivery app?" or "What is an API, and what happens if it times out?"

> [!tip] Strong answer includes
> - A clear simplified flow with the main components
> - Failure states and how the product handles them (retries, idempotency, status checks)
> - Trade-offs and what to ask engineers
> - Link to user impact and metrics

---
## 10. Behavioural Questions for PMs
> 🔴 Tier 1 · _Key points:_ STAR; ownership; influence without authority; decisions with incomplete data; failure and learning

### Definition
**What is tested:** ownership, influence without authority, decision-making, collaboration, resilience and self-awareness. **Frameworks:** STAR (Situation, Task, Action, Result) with a reflection ([[049 STAR Stories — Leadership & Conflict]]); build a bank of 6–8 stories mapped to competencies ([[176 Company-Specific Behavioural Rounds & Leadership Principles]], [[048 Tell Me About Yourself]]).

Typical PM themes: a **decision with incomplete data**, **disagreement with engineering or design**, **saying no**, **a failure**, **launching something**, **influencing a senior stakeholder**, **prioritising under pressure**. For students: use internship, project, club or operations stories ([[051 Internship Learnings & Projects]]).

**Common mistakes:** "we" instead of "I"; no measurable result; blaming others; no learning; telling the story chronologically.

### Example
**Prompt:** "Tell me about a time you made a decision with incomplete data." **Model answer (illustrative story structure):** "(**Situation**) In my internship at a manufacturer I had to choose between two vendors for a packaging line two weeks before a launch, with only a three-month trial from each. (**Task**) I owned the recommendation to the plant head. (**Action**) I listed what I knew and did not know, built a simple scorecard (cost, defect rate, delivery reliability) weighted with the plant head, pulled defect data for the 400 trial lots, and checked the biggest unknown, delivery reliability, with two other customers by phone. Vendor B was 4% cheaper but had a 2.1% defect rate against 1.2%; I recommended Vendor A with a clause to renegotiate price after six months. (**Result**) Defect-related rework stayed under 1.5% in the first quarter and the price was reduced 2% at review. (**Learning**) I now write down the single assumption that would flip a decision and test it first." (Replace with your real story and numbers; do not invent results.)

### In the news
See news box. Genie's closure and Paytm's regulatory episode are the sort of decisions about which PM interviewers ask "what would you have done?"; prepare a view that shows judgment on trade-offs, not hindsight.

### Interview angle
> [!question] How it is asked
> "Tell me about a time you disagreed with your engineering lead." or "Describe your biggest failure."

> [!tip] Strong answer includes
> - A specific story with your role, actions and a measurable result
> - Shows influence without authority and respect for the other side
> - Honest about what went wrong and the learning
> - Short (2–3 minutes), structured, ends with the result

---
## 11. AI-Product Questions
> 🔴 Tier 1 · _Key points:_ Value and use case, accuracy and evals, cost per task, latency, safety and fallback, metrics

### Definition
**What is tested:** whether you understand what makes AI products different: probabilistic outputs, evaluation, cost per use, safety and human fallback. **Framework:**

1. **User problem and why AI:** a task where AI beats rules (language, summarisation, personalisation).
2. **Quality definition and evals:** what is a good answer? Offline test sets, human review, online metrics ([[166 AI Product Management - LLM Products, Evals & Economics]]).
3. **Cost and latency:** cost per task = tokens × price; response-time budget.
4. **Risk and safety:** hallucination, privacy, bias, abuse, regulatory limits ([[220 Responsible AI, Explainability & Model Governance]]).
5. **Human fallback and UX:** confidence thresholds, escalation, user control.
6. **Metrics:** resolution rate, escalation rate, customer satisfaction, cost per resolved ticket, error rate on critical cases.
7. **Rollout:** shadow mode, small cohort, monitoring.

For technical depth see [[219 NLP, Embeddings & LLM Applications for Analysts]] and [[100 ML for Product Management]].

**Common mistakes:** "use AI" with no problem; ignoring cost per query; no evaluation plan; no fallback; overpromising accuracy.

### Example
**Prompt:** "Design an AI assistant for a quick-commerce app's customer support."
- **Use case:** order status, missing items, refunds: high-volume, repetitive.
- **Quality:** the assistant must be correct on policy and amounts; evaluate on a test set of 1,000 historical tickets, with an expert-labelled "correct resolution" and a hard-fail list (wrong refund amounts).
- **Cost model (illustrative prices):** an average conversation of 6 turns with 2,000 input tokens and 300 output tokens each = 12,000 input and 1,800 output tokens; at ₹0.25 per 1,000 input tokens and ₹1.00 per 1,000 output tokens, cost = 12 × 0.25 + 1.8 × 1.00 = **₹4.8 per conversation**. A human agent ticket costs ₹40 (assumed). For 1,00,000 tickets a month: baseline ₹40 lakh. If the AI touches all tickets and fully resolves 40%, cost = 1,00,000 × 4.8 + 60,000 × 40 = ₹4.8 lakh + ₹24 lakh = **₹28.8 lakh, a 28% saving (₹11.2 lakh)**. Break-even resolution rate = 4.8 / 40 = **12%**; at 20% resolution saving is 8%, at 60% it is 48%.
- **Safety and fallback:** auto-escalate when confidence is low, when the refund exceeds a threshold, or the user asks for a human; log every conversation for audit.
- **Metrics:** resolution rate without human, CSAT versus human baseline, escalation rate, cost per resolved ticket, refund-error rate (guardrail).
- **Rollout:** shadow mode, then 5% of traffic, then scale if error rates stay below the threshold.

### In the news
See news box. ChatGPT Go at ₹399 a month with UPI support (August 2025) shows pricing and payment methods being adapted for India, and 900 million weekly users (February 2026) indicates the scale of expectation users bring to AI assistants.

### Interview angle
> [!question] How it is asked
> "How would you build an AI shopping assistant for Flipkart?" or "How would you price an AI feature in India?"

> [!tip] Strong answer includes
> - A real user problem and a quality definition with evals
> - Cost per task and break-even economics
> - Safety, privacy and human fallback
> - Rollout plan with guardrail metrics

---
## 12. Answer Delivery and Common Mistakes Across Types
> 🔴 Tier 1 · _Key points:_ Structure, pacing, thinking aloud, commitment, summaries; the five most common mistakes

### Definition
Across all types, interviewers score **structure, insight, communication, product judgment and collaboration** (the exact rubric varies by company).

**Delivery rules:**
1. **Clarify and restate** the problem; confirm assumptions in one or two questions.
2. **State the structure** at the start ("I will cover three things...") and **signpost** as you go.
3. **Think aloud;** pause openly for 10–20 seconds when needed.
4. **Commit** to a choice and give a reason; do not list endlessly.
5. **Quantify** where you can; state assumptions.
6. **Summarise** in 30 seconds at the end: recommendation, why, risk, next step ([[162 Structured Communication - SCQA, Storylines & Case Delivery]]).
7. **Collaborate:** treat hints and objections as part of the work.

**Mistakes by type (quick reference):**

| Type | Frequent mistake | Fix |
|---|---|---|
| Product sense | Solution before user | Pick and justify one segment first |
| Improvement | Generic fixes | Evidence-based pain points |
| Metric drop | One guess | Decompose the funnel, then hypothesise |
| Metrics | Vanity metric only | North star plus guardrails and unit economics |
| Execution | Score worship | State trade-offs and what is not done |
| Strategy | Framework recital | Recommendation with economics and kill criteria |
| Estimation | No cross-check | Second method, sensitivity |
| Technical | Shallow or wrong | Flow, failure modes, ask engineers |
| Behavioural | "We" stories | Your actions, measured result, learning |
| AI | "Add AI" | Problem, evals, cost, fallback |

### Example
A 30-second wrap for the payment-drop case: "Orders fell 8% mainly because payment success dropped from 94% to 88% on Android UPI flows after Tuesday's release; traffic explains only about 2 points. I recommend a hotfix and a retry fallback, which should recover about 63,000 of the 79,000 lost orders a week. Risk: the fix may not cover all banks, so I would monitor payment success by bank daily. Next step: confirm with the payments team which bank and app version are affected."

### In the news
See news box. Interviewers in Indian consumer-internet companies often use live products and recent events as prompts; refer to numbers from the news with caution (state source and date) and avoid presenting guesses as fact.

### Interview angle
> [!question] How it is asked
> "What do you think went well in that answer, and what would you improve?" (a mock-interview debrief question)

> [!tip] Strong answer includes
> - Names specific strengths and weaknesses (structure, quantification, commitment)
> - Recognises the question type and the framework used
> - States one change for the next attempt
> - Shows openness to feedback

---
## 13. ⭐ Advanced: Company-Style Prompt Bank and Scoring Rubric
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Use company-style prompts to practise; the type follows the company's business model. Prompts below are practice prompts, not claims about what any company actually asks.

| Company (context) | Practice prompt | Type | What to bring |
|---|---|---|---|
| **Swiggy** (food and quick commerce) | "Delivery times are slipping at dinner peak. Diagnose and fix." | Root cause + execution | Funnel and supply-demand decomposition; rider capacity |
| **Swiggy / Blinkit** | "Which categories should a dark store add?" | Strategy + metrics | Contribution per order; break-even orders per store |
| **Paytm** (payments and financial services) | "Merchant payments volumes fell after a regulatory action. What do you do?" | Metric drop + strategy | Regulation, partner banks, merchant retention |
| **PhonePe** (UPI and financial services) | "Design a feature to make UPI payments more reliable." | Product sense + technical | Failure modes, success rate by bank, trust |
| **CRED** (credit card bill payments and rewards for creditworthy users) | "How would you increase engagement for members who pay bills once a month?" | Improvement + metrics | Habit loop, rewards economics, retention cohorts |
| **Flipkart** (marketplace) | "Return rates are rising in fashion. What would you do?" | Root cause + improvement | Size fit, seller quality, reverse logistics cost |
| **Any** | "Design an AI feature for X with cost limits." | AI product | Cost per task, evals, fallback |

**Scoring rubric (self or peer, 1–5 each):** (1) clarification and framing; (2) structure; (3) user and product insight; (4) quantification and data sense; (5) trade-offs and prioritisation; (6) communication and synthesis; (7) collaboration and adaptability. A target of 4 or above on structure and quantification matters most in Indian PM rounds with an analytical bent. Keep an error log by type and re-attempt weak types after 48 hours.

### Example
Self-review of a mock root-cause answer: framing 4, structure 4, insight 3, quantification 2 (no decomposition numbers), trade-offs 3, communication 3, collaboration 4. Plan: run three more metric-drop drills using the funnel formula and compute the lost orders per step before proposing a cause; re-score.

### In the news
See news box. For current prompts, read the latest quarterly results and product announcements of your target company the week before the interview ([[180 Current Affairs & Economy Briefing for MBA Interviews (2025-26)]]) and prepare one sharp insight and one metric per company.

### Interview angle
> [!question] How it is asked
> "Why do you want to be a PM at our company, and what would you improve in our product?"

> [!tip] Strong answer includes
> - Specific knowledge of the product and its recent changes
> - A clear user problem, a prioritised idea, and metrics
> - Honest awareness of constraints (regulation, cost, trust)
> - Fit between your background (operations, analytics) and the company's challenges
