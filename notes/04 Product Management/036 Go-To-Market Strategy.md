---
tags: [product-management, tier2]
area: Product Management
topic: "Go-To-Market Strategy"
tier: Tier 2
roles: PM / Consulting
status: complete
subtopics: 10
---
# Go-To-Market Strategy

⬅ [[035 Technical Understanding (APIs, SDLC)]] · [[_Index - Product Management|Product Management]] · [[163 PM Interview Types & Answer Frameworks]] ➡
> **Area:** Product Management · **Priority:** 🟠 Tier 2 · **Target roles:** PM / Consulting

## Sub-topics in this note
1. [[#1. GTM Framework]]
2. [[#2. Product Launch Plan]]
3. [[#3. Pricing Strategies]]
4. [[#4. Channel Strategy]]
5. [[#5. Customer Segmentation]]
6. [[#6. Sales Enablement]]
7. [[#7. Product-Led Growth (PLG)]]
8. [[#8. Launch Metrics]]
9. [[#9. ⭐ Advanced: Positioning and Messaging]]
10. [[#10. ⭐ Advanced: Unit Economics (CAC, LTV, Payback)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): OpenAI gives ChatGPT Go free for a year in India (Oct–Nov 2025)
> On 27 Oct 2025 OpenAI announced that **ChatGPT Go**, normally priced at **under $5 per month**, would be **free for 12 months for all users in India from 4 Nov 2025** (existing Go subscribers also qualify). The plan offers about **10x more usage** than the free tier for responses, image generation and file uploads, plus better memory. TechCrunch reported India as OpenAI's second-largest market, with **29 million ChatGPT app downloads in the 90 days before Aug 2025** but only about **$3.6 million in in-app purchases**, so the free year is a bet on adoption first and monetisation later. OpenAI opened a New Delhi office in Aug 2025 and held a developer event in Bengaluru on 4 Nov. ([TechCrunch](https://techcrunch.com/2025/10/27/openai-offers-free-chatgpt-go-for-one-year-to-all-users-in-india))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. GTM Framework
> 🟠 Tier 2 · _Tracker hint:_ Target segment → value proposition → channels → pricing → launch

### Definition
A **go-to-market (GTM) strategy** is the plan for delivering a product to a target customer and winning in the market. Core building blocks:
1. **Target segment / ICP:** who exactly buys, and why now.
2. **Value proposition and positioning:** the problem solved, the differentiated benefit, and the competitive alternative.
3. **Pricing and packaging:** how value is captured.
4. **Channels and sales motion:** how customers find, try and buy (self-serve, inside sales, field sales, partners).
5. **Marketing and demand generation:** messaging, content, performance, events.
6. **Launch plan and metrics:** timeline, owners, success measures.

A useful sizing step is **TAM, SAM, SOM** (total, serviceable, obtainable market). GTM is cross-functional: Product, Marketing, Sales, Customer Success, Finance and Ops. The PM's role is to be the "CEO of the launch": own the narrative and the readiness checklist, not to do everyone's job.

### Example
A B2B logistics-SaaS for Indian SMEs: ICP = D2C brands shipping 500–5,000 parcels/month; value prop = 20% fewer RTOs via address-verification; channel = self-serve free trial plus inside sales for >2,000 parcels; pricing = per-shipment fee; launch metric = 50 paying brands in 90 days.

### In the news
See news box. OpenAI's India move shows all blocks at once: a mass segment (students, young professionals), a value proposition (more usage), a price (free for a year), distribution (app and partners) and a launch moment (4 Nov event).

### Interview angle
> [!question] How it is asked
> "How would you launch [product] in India?" or "Design a GTM for a new fintech app."

> [!tip] Strong answer includes
> - Segment first, then value proposition, pricing, channels, launch and metrics, in that order
> - A sharp ICP, not "everyone"
> - Sizing (TAM/SAM/SOM) and a target for the first 90 days
> - Risks and the cross-functional owners

---

## 2. Product Launch Plan
> 🟠 Tier 2 · _Tracker hint:_ Alpha, beta, GA; launch checklist; press release

### Definition
Launch phases: **Alpha** (internal users, find major defects), **Closed beta** (invited customers, validate value and usability), **Open beta** (broader load and feedback), **GA (General Availability)** (public release, full support and SLA). Further: soft launch in one city/segment before national, **staged rollout** by percentage.

**Launch checklist:** product readiness (quality, performance, security sign-off, rollback plan), legal/compliance, pricing and billing, documentation and help-centre, support training and macros, sales enablement, marketing assets (landing page, press release, demo video, FAQs), analytics instrumentation, success metrics and a **war-room** for launch day. Use **Amazon's "working backwards" press release**: write the customer-facing announcement and FAQ first to test whether the value is crisp. Classify launches by tier (Tier 1: major, full campaign; Tier 3: changelog entry) to size effort.

### Example
A new health-insurance comparison feature: alpha with 50 employees, closed beta with 500 invited users in Pune, GA after beta NPS exceeded the team's threshold and p95 latency met the target; launch-day war-room monitors conversion and error rate with a kill switch.

### In the news
See news box. A free year is a launch-plan decision (when, where, for whom). Separately, CrowdStrike's July 2024 outage and its adoption of ring-based staged rollouts is a reminder that GA to everyone at once is the riskiest launch design; see [[034 Prioritization Frameworks]] on feature flags.

### Interview angle
> [!question] How it is asked
> "Walk me through how you'd launch a new feature end to end" or "What would you do on launch day if conversion drops 30%?"

> [!tip] Strong answer includes
> - Alpha, beta, GA with entry and exit criteria for each
> - Launch tiering and a cross-functional checklist
> - Success metrics set in advance; staged rollout and kill switch
> - Post-launch review at day 7, 30 and 90

---

## 3. Pricing Strategies
> 🟠 Tier 2 · _Tracker hint:_ Cost-plus, value-based, freemium, subscription, usage-based

### Definition
| Strategy | How price is set | Best when |
|---|---|---|
| **Cost-plus** | Unit cost + markup | Commodities, B2B contracts, transparent costs |
| **Competitor/market-based** | Anchor to rivals | Mature, comparable products |
| **Value-based** | Share of customer's economic value | Differentiated B2B products |
| **Penetration** | Low price to gain share | Network effects, scale economies |
| **Skimming** | High initial price, then reduce | New technology, early adopters |
| **Freemium** | Free tier plus paid upgrade | Low marginal cost, viral/PLG |
| **Subscription** | Recurring fee | Ongoing value (SaaS, OTT) |
| **Usage-based** | Pay per unit consumed | Variable use (cloud, APIs, payments) |

Key ideas: **willingness to pay**, price anchoring, tiered "good-better-best" packaging, psychological pricing (₹499 vs ₹500), price elasticity of demand $E = \%\Delta Q / \%\Delta P$, and **price sensitivity in India** (low ARPU, high volume, UPI and prepaid norms). Methods to find WTP: Van Westendorp survey, conjoint analysis, A/B price tests.

### Example
Cost-plus: unit cost ₹600, 25% markup → price ₹750. Freemium: 100,000 free users × 3% conversion × ₹800/month = 3,000 payers × ₹800 = **₹24 lakh MRR**. Value-based: software saves a client ₹10 lakh a year; pricing at about 20% of value captured = ₹2 lakh a year still leaves the customer an 8 lakh net benefit.

### In the news
See news box. OpenAI priced ChatGPT Go at under $5 a month, then set it to zero for a year in India, a **penetration/freemium-style** decision justified by India's large user base but low in-app spending.

### Interview angle
> [!question] How it is asked
> "How would you price a new SaaS product?" or "Should we make our product free?"

> [!tip] Strong answer includes
> - Three anchors: cost (floor), competition (reference), value (ceiling)
> - Pricing model fit (subscription vs usage) to how value scales
> - Tiering and packaging; testing via experiments or surveys
> - Unit economics check (CAC, LTV, margin) and a plan if free users do not convert

---

## 4. Channel Strategy
> 🟠 Tier 2 · _Tracker hint:_ Direct vs indirect; digital vs offline; partnership channels

### Definition
A **channel** is the route by which a product reaches customers. **Direct** (own website/app, own sales force): control over experience, price and data; higher fixed cost. **Indirect** (distributors, retailers, resellers, marketplaces, system integrators): reach and speed; margin sharing and less control. **Digital** (performance marketing, SEO, app stores, marketplaces) vs **offline** (retail, field sales, events) vs **partnership** (bundles with telcos, banks, OEM pre-installs, co-marketing).

Choose by **customer buying behaviour**, deal size, cost-to-serve, and **channel conflict** risk. Economics: $\text{CAC by channel} = \text{channel spend} / \text{customers acquired}$; compare with LTV. Indian context: marketplace dominance (Amazon, Flipkart), quick-commerce, distributor networks for FMCG reaching small kiranas, UPI-based fintech partnerships, vernacular and WhatsApp commerce.

### Example
A new packaged-snack brand: starts on quick-commerce and marketplaces (fast, trackable), builds modern-trade presence in 3 metros, and only then hires distributors for general trade. A SaaS company selling to enterprises uses a direct sales team for large deals and a reseller programme for SMEs.

### In the news
See news box. The reported channel was OpenAI's own app and sign-up flow (direct, digital); the article does not mention telco or other partners, so treat partnership distribution as the open question a PM would ask: when the price is zero, distribution matters as much as the product.

### Interview angle
> [!question] How it is asked
> "Which channels would you use to launch an Indian D2C brand?" or "Should we go direct or through distributors?"

> [!tip] Strong answer includes
> - Matching channel to customer behaviour and deal size
> - Channel economics: margin, CAC, cost-to-serve
> - Conflict management (pricing parity, territories)
> - Sequencing: test in a few channels, then scale the winners

---

## 5. Customer Segmentation
> 🟠 Tier 2 · _Tracker hint:_ B2B vs B2C; firmographic, demographic, behavioral segments

### Definition
**Segmentation** divides a market into groups with similar needs, followed by **targeting** and **positioning** (STP).

| Basis | B2C examples | B2B examples |
|---|---|---|
| **Demographic / Firmographic** | Age, income, city tier | Industry, company size, revenue, geography |
| **Behavioural** | Usage frequency, loyalty, purchase occasion | Product usage, buying process, tech stack |
| **Psychographic** | Lifestyle, values | Culture, risk appetite |
| **Needs-based / Jobs-to-be-done** | Problem being solved | Pain point and trigger event |

A good segment is **measurable, substantial, accessible, differentiable and actionable**. For B2B define an **ICP (Ideal Customer Profile)** and personas for buyer, user and economic decision-maker (the buying committee). Choose a **beachhead segment** where you can win first. Segment attractiveness = size × growth × ability to serve × competitive intensity.

### Example
An Indian invoicing/accounting SaaS: segments by size: kirana/freelancers (price-sensitive, mobile-first, UPI-linked), SMEs (GST filing, multi-user) and mid-market (ERP integrations). Beachhead: SMEs with 10–50 employees filing monthly GST, because pain is high and decision-making is fast.

### In the news
See news box. OpenAI's offer is aimed at the whole Indian consumer base, but TechCrunch's numbers (29 million downloads, only $3.6 million in-app revenue) show the segment is big but monetises poorly: segment size is not segment value.

### Interview angle
> [!question] How it is asked
> "How would you segment the market for a new credit card?" or "Who is your ideal customer?"

> [!tip] Strong answer includes
> - STP flow and sensible segmentation bases for B2C vs B2B
> - Criteria for choosing a segment (size, growth, fit, accessibility)
> - A beachhead with reasons and a way to validate (interviews, data)
> - Differentiating buyer, user and payer in B2B

---

## 6. Sales Enablement
> 🟠 Tier 2 · _Tracker hint:_ Battle cards, demo scripts, ROI calculators for sales team

### Definition
**Sales enablement** equips salespeople with the content, training and tools to sell the product effectively. Assets: **battle cards** (one-page competitor comparison: strengths, weaknesses, landmines, rebuttals), **demo scripts** (tell-show-tell storyline tied to pain points), **ROI/TCO calculators**, pitch decks, one-pagers, case studies, objection-handling guides, pricing and discount rules, and a **sales playbook** (ICP, qualification such as BANT/MEDDICC, stages). Process: product training before launch, certification, call coaching, win/loss reviews, feedback loops to product.

Metrics: ramp time for new reps, win rate, average deal size, sales-cycle length, content usage. $\text{Payback of enablement} = \Delta\text{win-rate} \times \text{pipeline} \times \text{ACV}$.

### Example
A B2B payroll product: ROI calculator input = 200 employees, 3 days of HR time per month at ₹800/hour saved. Hours saved = 3 days × 8 h × 12 = 288 h/year; saving = 288 × ₹800 = **₹2.30 lakh/year**; if the annual price is ₹1.0 lakh, ROI = (2.30 − 1.0)/1.0 = **130%** and payback ≈ 5.2 months (1.0/2.30 × 12).

### In the news
See news box. For a free-for-a-year consumer plan sales enablement is light; but for enterprise AI products the same launch needs battle cards that address data-privacy and pricing questions.

### Interview angle
> [!question] How it is asked
> "Sales says they can't sell the new product. What do you do?"

> [!tip] Strong answer includes
> - Diagnose first: lead quality, pitch, pricing, competition, training
> - Concrete assets: battle card, demo script, ROI calculator
> - Feedback loop with win/loss analysis and field calls
> - Metrics: ramp time, win rate, cycle time

---

## 7. Product-Led Growth (PLG)
> 🟠 Tier 2 · _Tracker hint:_ Free trial, viral loops, in-product conversion; Slack/Notion examples

### Definition
**PLG** uses the product itself as the main driver of acquisition, conversion and expansion. Features: free tier or trial, **self-serve onboarding**, a fast **"aha moment"**, in-product upgrade prompts, virality (invites, shared docs), and **product-qualified leads (PQLs)** handed to sales as accounts grow. Contrast **sales-led** (demos, field sales, long cycles).

**Viral coefficient** $K = i \times c$ (invites per user × conversion of invites); K > 1 means self-sustaining growth. Funnel: visitor → signup → activation → habit → paid → expansion. **Net revenue retention** above 100% shows expansion beats churn. Works best when time-to-value is short, the product is easy to adopt bottom-up, and marginal cost per free user is low.

### Example
**Slack:** teams invite colleagues; Stewart Butterfield has said that teams that exchange about 2,000 messages almost always keep using it (widely cited activation threshold). **Notion:** free personal plan and shareable templates seed team adoption. **Dropbox:** referral storage rewards; widely cited as growing from 100,000 to 4 million users in about 15 months. **Freshworks and Zoho** also lean on free trials in India.

### In the news
See news box. ChatGPT Go free for a year is PLG at national scale: remove price friction, let usage build habit, and convert later to paid tiers.

### Interview angle
> [!question] How it is asked
> "Is PLG right for our enterprise software?" or "How would you design a viral loop?"

> [!tip] Strong answer includes
> - PLG defined with the funnel and the aha moment
> - Viral coefficient maths and why K > 1 is rare
> - Where it fails: complex enterprise, high security review, long cycles (hybrid PLG plus sales)
> - Metrics: activation, PQLs, free-to-paid conversion, NRR

---

## 8. Launch Metrics
> 🟠 Tier 2 · _Tracker hint:_ Signups, activation rate, early NPS, day-7 retention

### Definition
Measure the funnel from awareness to habit:
- **Signups / installs:** top of funnel (and CAC).
- **Activation rate** = users reaching the "aha" action / signups. Define the action precisely (first order placed, first project created).
- **Day-N retention** = users active on day N / users who joined (cohort-based). **Day-7 retention** is the key early signal of product-market fit.
- **Early NPS** = %Promoters (9–10) − %Detractors (0–6).
- Also: time-to-first-value, conversion to paid, error and crash rate, support tickets per 1,000 users, ratings.

Use **cohort tables**, compare against pre-set targets, and separate vanity metrics (downloads) from outcome metrics (retained, paying users). Use guardrail metrics (crash rate, refunds) alongside growth ones.

### Example
Launch cohort: 10,000 signups; 4,000 complete first order → activation **40%**; 2,500 are active on day 7 → D7 retention **25%** of signups; survey of 200: 100 promoters, 60 passives, 40 detractors → NPS = (100 − 40)/200 = **+30**. Target was D7 ≥ 30%, so the team investigates onboarding drop-off before scaling spend.

### In the news
See news box. In OpenAI's India case, the $3.6 million in-app purchase figure against 29 million downloads (about $0.12 per download, my arithmetic) is exactly the kind of gap between installs and revenue that activation and retention metrics are meant to expose.

### Interview angle
> [!question] How it is asked
> "How will you measure the success of the launch?" or "D7 retention is 12%. What do you do?"

> [!tip] Strong answer includes
> - A funnel with targets set before launch
> - Precise definitions (activation, cohort retention, NPS formula)
> - Leading metrics (activation, D7) vs lagging (revenue, D90)
> - A diagnosis plan: segment by channel, cohort and onboarding step

---

## 9. ⭐ Advanced: Positioning and Messaging
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Positioning** defines how your product is understood relative to alternatives. April Dunford's framework (*Obviously Awesome*) sequence: (1) competitive alternatives (what customers do today, including "nothing"/Excel), (2) unique attributes, (3) the value those attributes enable, (4) the customers who care most, (5) the market category that makes the value obvious. **Messaging** then translates it into headline, proof points and calls to action for each persona. A classic template: *For [target] who [need], [product] is a [category] that [key benefit]. Unlike [alternative], it [differentiator].*

Test messaging by A/B landing pages, five-second tests, and sales-call feedback. Bad positioning shows up as long sales cycles, price pressure and prospects asking "how are you different?" Positioning guides product, pricing and channel, not only ads.

### Example
A new expense-management tool for Indian startups: alternatives = Excel and reimbursement emails; unique attribute = UPI-linked corporate cards with auto-receipt capture; value = month-end close in 1 day, not 5; best-fit customers = 50–500 person startups with finance teams of 1–3; category = "spend management", not "accounting software".

### In the news
See news box. "Free for 12 months" is a pricing message; the positioning question for any AI assistant in India is what job it replaces (search, tutor, writing aid), which decides who adopts it.

### Interview angle
> [!question] How it is asked
> "How would you position a new entrant against a strong incumbent?"

> [!tip] Strong answer includes
> - Start from the customer's alternatives, not features
> - Pick a niche where you are clearly better, and a category frame
> - Distinct messages per persona with proof points
> - Test and iterate with data

---

## 10. ⭐ Advanced: Unit Economics (CAC, LTV, Payback)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
$$\text{CAC} = \frac{\text{Sales and marketing spend}}{\text{New customers}}$$

$$\text{LTV} = \frac{\text{ARPA} \times \text{Gross margin}}{\text{Churn rate}}$$

(ARPA and churn on the same period, e.g. monthly.) **CAC payback (months)** $= \text{CAC} / (\text{ARPA} \times \text{GM})$. Rule-of-thumb health: **LTV:CAC ≥ 3** and payback under about 12 months (B2B SaaS norms vary; consumer apps often target faster). Blended vs paid CAC, contribution margin after delivery and support costs, and cohort-based LTV are more reliable than simple formulas. Free-user programmes add a **cost-to-serve** that must be funded by conversion.

### Example
ARPA ₹2,000/month, gross margin 70%, monthly churn 4%: LTV = 2,000 × 0.7 / 0.04 = **₹35,000**. CAC = ₹10,500 → LTV:CAC = **3.33**; payback = 10,500 / (2,000 × 0.7) = 10,500/1,400 = **7.5 months**. If churn rose to 6%, LTV falls to ₹23,333 and LTV:CAC to 2.2, a warning.

### In the news
See news box. A free year means 12 months of serving costs without revenue; the economics only work if later conversion, ads/ecosystem value or strategic gains exceed that cost-to-serve. The article does not disclose OpenAI's unit economics, so this is the question to ask, not an answer.

### Interview angle
> [!question] How it is asked
> "Is this growth strategy profitable?" or "Calculate LTV and say if the business is healthy."

> [!tip] Strong answer includes
> - Formulas with consistent time units and gross margin, not revenue
> - LTV:CAC and payback, with benchmarks stated as rules of thumb
> - Sensitivity to churn and discounting
> - Levers: reduce CAC, raise ARPA, cut churn, improve margin

---
## 🔗 Go deeper: expansion notes
- [[165 Platform & Marketplace Product Strategy|Platform & Marketplace Product Strategy]]
