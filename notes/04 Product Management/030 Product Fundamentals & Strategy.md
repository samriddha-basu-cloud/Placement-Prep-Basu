---
tags: [product-management, tier1]
area: Product Management
topic: "Product Fundamentals & Strategy"
tier: Tier 1
roles: PM
status: complete
subtopics: 14
---
# Product Fundamentals & Strategy

[[_Index - Product Management|Product Management]] · [[031 Product Metrics & Analytics]] ➡

> **Area:** Product Management · **Priority:** 🔴 Tier 1 · **Target roles:** PM

## Sub-topics in this note
1. [[#1. Product Lifecycle (PLC)]]
2. [[#2. MVP (Minimum Viable Product)]]
3. [[#3. Product-Market Fit]]
4. [[#4. User Persona Development]]
5. [[#5. User Journey Mapping]]
6. [[#6. Product Roadmap]]
7. [[#7. North Star Metric]]
8. [[#8. Product Strategy]]
9. [[#9. Jobs To Be Done (JTBD)]]
10. [[#10. Competitor Analysis for PM]]
11. [[#11. Product Positioning]]
12. [[#12. Product Vision & Mission]]
13. [[#13. ⭐ Advanced: Product-Led Growth and Moats]]
14. [[#14. ⭐ Advanced: Prioritisation Frameworks and Product Trade-offs]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): ChatGPT's growth to 800 million weekly users
> At OpenAI's DevDay on **6 October 2025**, Sam Altman said ChatGPT had reached **800 million weekly active users**, up from about **700 million in August 2025** and **500 million at the end of March 2025**; he also said about **4 million developers** had built with OpenAI and that the API was processing over **6 billion tokens per minute**. A single product moved from launch (Nov 2022) to a mass-market platform with an ecosystem around it. ([TechCrunch](https://techcrunch.com/2025/10/06/sam-altman-says-chatgpt-has-hit-800m-weekly-active-users/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Product Lifecycle (PLC)
> 🔴 Tier 1 · _Tracker hint:_ Introduction, Growth, Maturity, Decline — strategy per stage

### Definition
The **product lifecycle** describes sales and profit over a product's life in four stages.

| Stage | Sales / profit | Customers | Strategy focus |
|---|---|---|---|
| Introduction | Low sales, losses | Innovators | Awareness, trial, build distribution, validate value |
| Growth | Rapid sales, profit turns positive | Early adopters, early majority | Scale, features, widen segments, build brand |
| Maturity | Sales peak and flatten, highest profit | Majority | Defend share, differentiate, cut costs, extend line |
| Decline | Sales and profit fall | Laggards | Harvest, reposition, or divest/sunset |

PM actions per stage: Introduction = find product-market fit; Growth = scale infrastructure, retention, monetisation; Maturity = efficiency, adjacent features, price tiers, new segments or geographies; Decline = migrate users, reduce support, or reinvent (a "second curve"). Limits: not every product follows the curve; categories (not just brands) have lifecycles; managers can extend it by innovation.

### Example
Smartphones in India: feature phones in decline; basic smartphones mature; 5G and foldables in introduction or early growth. Kodak film is the classic decline case; Netflix moved from DVD-by-mail (decline) to streaming (growth).

### In the news
See news box. ChatGPT is a growth-stage product: weekly users rose from 500 million to 800 million in about six months, so priorities shift from "does anyone want it" to capacity, reliability and monetisation.

### Interview angle
> [!question] How it is asked
> "Where is product X in its lifecycle and what would you do?" or "How do you extend a mature product?"

> [!tip] Strong answer includes
> - Identifies the stage with evidence (growth rate, margin, competition)
> - Stage-appropriate strategy and metrics
> - Mentions extension tactics (new segments, features, pricing)
> - Notes the limits of the model

---

## 2. MVP (Minimum Viable Product)
> 🔴 Tier 1 · _Tracker hint:_ Lean startup; build-measure-learn; MVP types

### Definition
An **MVP** is the smallest version of a product that lets you test the riskiest assumption with real users and learn, with the least effort (Eric Ries, *The Lean Startup*). The loop is **Build → Measure → Learn**, driven by *validated learning*, not feature count. Then **pivot** or **persevere**.

Common MVP types:
- **Concierge:** deliver the service manually to a few customers.
- **Wizard of Oz:** looks automated, humans do the work behind the scenes.
- **Landing page / smoke test:** measure sign-ups before building.
- **Explainer video** (Dropbox).
- **Single-feature MVP** and **piecemeal** (assemble existing tools).
- **Pre-order / crowdfunding.**

"Minimum" means minimum to learn, "viable" means it must still deliver value. Define the hypothesis, metric and success threshold *before* building.

### Example
Zappos' founder photographed shoes at local stores and posted them online, buying only after an order, to test whether people would buy shoes online. Flipkart started with books. Dropbox used a demo video before the product was complete (widely reported to have multiplied its waiting list).

### In the news
See news box. ChatGPT launched as a "research preview" in Nov 2022, a low-polish release that learned from massive user feedback.

### Interview angle
> [!question] How it is asked
> "How would you validate this idea with minimal investment?" or "What would your MVP be for X?"

> [!tip] Strong answer includes
> - The riskiest assumption stated first
> - A specific MVP type with a reason
> - Success metric and threshold
> - What decision follows (pivot, persevere, kill)

---

## 3. Product-Market Fit
> 🔴 Tier 1 · _Tracker hint:_ Retention, NPS, Sean Ellis test; how to measure

### Definition
**Product-market fit (PMF)** (Marc Andreessen): being in a good market with a product that satisfies it. Signs: organic growth, strong retention, customers complaining when it is down.

How to measure:
- **Sean Ellis test:** ask "How would you feel if you could no longer use the product?" PMF is signalled when **40% or more** answer "very disappointed".
- **Retention curve** that flattens (a plateau) rather than decaying to zero; cohort retention by day/week/month.
- **NPS** (Net Promoter Score), see [[031 Product Metrics & Analytics]].
- **Organic share** of acquisition, word-of-mouth, referral rate.
- **Usage frequency** and engagement versus the natural frequency of the problem.
- Unit economics: LTV/CAC.

Pre-PMF: iterate on the product. Post-PMF: scale go-to-market.

### Example
A fintech app sees 100% of users on day 0, 40% on day 7, 22% day 30, flattening near 20% after day 60: a plateau suggests fit within a core segment. If the curve keeps falling to 3%, there is no fit yet; adding marketing spend would only buy churn.

### In the news
See news box. For ChatGPT, weekly active user growth with high organic acquisition is the quantitative PMF signal at scale.

### Interview angle
> [!question] How it is asked
> "How do you know if your product has product-market fit?"

> [!tip] Strong answer includes
> - Sean Ellis 40% rule plus the flattening retention curve
> - Quantitative and qualitative evidence
> - Segment-level PMF (who loves it)
> - What you would do if it is absent

---

## 4. User Persona Development
> 🔴 Tier 1 · _Tracker hint:_ Demographic, psychographic, pain points, jobs-to-be-done

### Definition
A **persona** is a research-based archetype of a user segment. It should come from interviews, surveys and data, not imagination.

Typical fields: name and photo (fictional), **demographics** (age, city, income, occupation), **psychographics** (values, attitudes), **behaviours** (devices, tools, frequency), **goals / jobs to be done**, **pain points**, **motivations and triggers**, **barriers**, and a representative quote. Include a *key scenario*.

Process: collect data, cluster by behaviour and needs (not just demographics), draft 2–4 primary personas, validate with real users, and keep them alive in prioritisation ("Would Asha need this?"). Also define **anti-personas** (users you do not design for).

### Example
Persona for a UPI-based bill-splitting app: "Rohan, 24, Bengaluru software analyst, shares a flat with 3 friends; pays rent, Wi-Fi and groceries; pain: chasing friends for money; goal: settle quickly without awkwardness; tools: UPI, WhatsApp." (Illustrative, not real data.)

### In the news
See news box. At 800 million weekly users, ChatGPT serves very different personas (students, coders, writers); each uses a different job, so one persona is insufficient.

### Interview angle
> [!question] How it is asked
> "Who is your target user for this product?" or "Create a persona for a rural education app."

> [!tip] Strong answer includes
> - Behaviour-based segmentation backed by research
> - Concrete pain points and goals
> - One primary persona chosen with reasons
> - How the persona changes a product decision

---

## 5. User Journey Mapping
> 🔴 Tier 1 · _Tracker hint:_ Awareness → acquisition → activation → retention → referral

### Definition
A **user journey map** shows a persona's steps, actions, thoughts and emotions across stages, exposing pain points and opportunities. Stages (AARRR-style): **Awareness** (discover), **Acquisition** (sign up/install), **Activation** (first value, the "aha moment"), **Retention** (repeat use), **Referral** (recommend), often plus Revenue.

Map rows: stage, user actions, touchpoints/channels, thoughts, **emotion curve**, pain points, opportunities, owner/metric. Method: pick persona and scenario, list steps from research, mark moments of truth and drop-off points, prioritise fixes by impact. Link each stage to a metric (conversion, time to first value, D30 retention).

### Example
Food-delivery first order: sees ad → installs → registers with OTP → browses → adds to cart → fails at payment (pain point) → delivery late (low emotion) → rates app. Fixing payment failure at step 6 can be worth more than more ads.

### In the news
See news box. For AI assistants, the activation moment is a first useful answer; shaving friction at sign-up is part of the journey of reaching hundreds of millions weekly users.

### Interview angle
> [!question] How it is asked
> "Walk me through the user journey for booking a cab and where you'd improve it."

> [!tip] Strong answer includes
> - Persona and scenario stated first
> - Stages with actions, emotions and pain points
> - Drop-off data or hypotheses with metrics
> - Prioritised improvements

---

## 6. Product Roadmap
> 🔴 Tier 1 · _Tracker hint:_ Vision, strategy, goals, initiatives, features; quarterly OKRs

### Definition
A **roadmap** is a strategic communication of *where the product is going and why*, not a promise of dates. Hierarchy: **Vision → Strategy → Goals/OKRs → Initiatives/themes → Features**.

Formats: **Now-Next-Later** (avoids false dates), theme-based, outcome-based, timeline. **OKRs:** Objective (qualitative, inspiring) + 3–5 measurable Key Results per quarter, e.g. "O: Make onboarding effortless; KR1: raise activation 35% → 50%; KR2: cut time-to-first-order to under 3 minutes."

Prioritisation inputs: RICE $=\frac{\text{Reach}\times\text{Impact}\times\text{Confidence}}{\text{Effort}}$, MoSCoW, Kano, value vs effort. Keep audiences in mind: executives (outcomes), engineering (detail), sales (customer-facing, no firm dates).

### Example
RICE: Feature A reach 10,000 users/quarter, impact 2, confidence 80%, effort 4 person-months: $10{,}000\times2\times0.8/4=4{,}000$. Feature B: reach 2,000, impact 3, confidence 100%, effort 1: $2{,}000\times3\times1/1=6{,}000$. B ranks higher.

### In the news
See news box. Fast-moving products publish roadmaps as themes (new models, tools, enterprise features) rather than fixed dates; expectation-setting matters.

### Interview angle
> [!question] How it is asked
> "How would you build and prioritise a roadmap?" or "Stakeholders want 10 features; how do you decide?"

> [!tip] Strong answer includes
> - Roadmap tied to strategy and measurable goals
> - A prioritisation method with numbers
> - Handling stakeholders and trade-offs
> - Flexibility: now-next-later, review cadence

---

## 7. North Star Metric
> 🔴 Tier 1 · _Tracker hint:_ Single metric that best captures product value delivered

### Definition
The **North Star Metric (NSM)** is the one metric that best reflects the core value customers receive and predicts long-term revenue. Good NSMs: measure value delivered (not vanity), are a **leading** indicator of revenue, are actionable by teams, and are understandable. It is supported by **input metrics** (breadth, depth, frequency, efficiency) that teams can move.

Examples: Airbnb = nights booked; Spotify = time spent listening; Swiggy/Zomato = orders per active user or GMV; WhatsApp = messages sent; a SaaS tool = weekly active teams. Avoid: revenue alone (lagging), sign-ups (vanity), downloads.

Test: if this metric rises and nothing else is gamed, are customers better off *and* is the business healthier?

### Example
Food delivery app NSM: "orders per monthly active user". Inputs: new users (breadth), orders per user per month (frequency), average basket (depth), delivery success rate (quality). A team raising restaurant selection moves breadth; a faster-delivery squad moves frequency.

### In the news
See news box. For ChatGPT, weekly active users is a candidate headline metric, but a deeper NSM might be "weekly users who get a task done" (depth).

### Interview angle
> [!question] How it is asked
> "What would be the North Star metric for Instagram / Zepto / a learning app?"

> [!tip] Strong answer includes
> - A metric tied to value delivered, with justification
> - Input metrics that decompose it
> - Rejects vanity and lagging alternatives
> - Guardrail metrics (quality, trust) to prevent gaming

---

## 8. Product Strategy
> 🔴 Tier 1 · _Tracker hint:_ Differentiation, focus, cost leadership for products

### Definition
**Product strategy** is a set of choices on *whom you serve, what problem you solve, and how you win*. Porter's generic strategies applied to products:

- **Cost leadership:** lowest cost via scale and efficiency (Reliance Jio's low-priced data plans at launch).
- **Differentiation:** unique features, UX or brand worth a premium (Apple).
- **Focus (niche):** serve a narrow segment better (cost focus or differentiation focus).

Other pieces: target market, value proposition, moats (network effects, switching costs, data, brand, scale), business model, and sequencing (wedge → expand). A **strategy kernel** (Rumelt): diagnosis, guiding policy, coherent actions. "Stuck in the middle" is the risk of doing none well. Strategy also means *what not to build*.

### Example
CRED focuses on high-credit-score users with rewards and premium UX (differentiation + focus). Zerodha uses cost leadership via flat brokerage fees and a technology-driven low-cost model.

### In the news
See news box. OpenAI's strategy of a consumer-first product that pulls developers onto a platform is a wedge-and-expand strategy.

### Interview angle
> [!question] How it is asked
> "What should be Spotify India's product strategy?" or "How would you compete against a bigger incumbent?"

> [!tip] Strong answer includes
> - Target segment and value proposition
> - Choice among cost, differentiation, focus with reasons
> - Moat and what you will not do
> - Sequencing: wedge, then expansion

---

## 9. Jobs To Be Done (JTBD)
> 🔴 Tier 1 · _Tracker hint:_ Customers hire products to do a job; outcome-based thinking

### Definition
**JTBD** (Clayton Christensen; Tony Ulwick's outcome-driven innovation): customers "hire" a product to make progress in a particular circumstance. Focus on the **job**, not the demographic.

Job statement: "When **[situation]**, I want to **[motivation]**, so I can **[expected outcome]**." Jobs have **functional**, **emotional** and **social** dimensions. Competition is whoever does the job (a milkshake competes with a banana and boredom).

Ulwick's **opportunity score** = importance + (importance − satisfaction) with both rated 1–10 (satisfaction capped so the gap is non-negative): high importance with low satisfaction = opportunity. Research method: "switch interviews" asking why customers switched and what triggered it.

### Example
Christensen's milkshake: morning commuters hired milkshakes to make a long boring drive more interesting and to fill the stomach, so a thicker shake and dispensers for speed worked better than new flavours. Indian example: a customer "hires" a quick-commerce app to avoid a store run when guests arrive unexpectedly.

### In the news
See news box. Students "hire" ChatGPT to understand a topic fast, professionals to draft; different jobs, different measures of success.

### Interview angle
> [!question] How it is asked
> "What job does a user hire LinkedIn / Zepto / a gym app for?"

> [!tip] Strong answer includes
> - A job statement with situation, motivation, outcome
> - Functional, emotional and social dimensions
> - Non-obvious competitors (alternative ways of doing the job)
> - How the job changes the product decision

---

## 10. Competitor Analysis for PM
> 🔴 Tier 1 · _Tracker hint:_ Feature matrix, pricing, positioning, gaps to exploit

### Definition
Systematic comparison to find where to win. Steps: (1) identify **direct, indirect and substitute** competitors, (2) pick dimensions that matter to the customer, (3) collect evidence (product trial, reviews, pricing pages, job posts, filings, app-store data), (4) build a **feature matrix** and a **positioning map** (two axes, e.g. price vs breadth), (5) find **gaps** and unmet needs, (6) decide response.

Frameworks: SWOT, Porter's Five Forces, perceptual maps, "table stakes vs differentiators vs delighters" (Kano). Useful items: pricing and packaging, target segment, messaging, distribution, ratings and complaint themes, funding and pace of shipping.

Pitfall: copying features. Match table stakes, differentiate where customers value and you can sustain.

### Example
Feature matrix for three expense apps: columns = auto SMS reading, UPI integration, split bills, budgets, free tier. If all have auto-reading and budgets (table stakes) but none supports shared household accounts well, "family accounts" is a candidate differentiator, checked against reviews that complain about it.

### In the news
See news box. Rapid releases by AI-assistant competitors show that feature parity is temporary; speed of learning and distribution matter more.

### Interview angle
> [!question] How it is asked
> "How would you analyse competitors before launching a new product?"

> [!tip] Strong answer includes
> - Direct, indirect and substitute competitors
> - Customer-relevant comparison dimensions
> - Table stakes vs differentiators and gaps
> - Action: positioning decision, not just a table

---

## 11. Product Positioning
> 🔴 Tier 1 · _Tracker hint:_ Category, target audience, differentiation, proof points

### Definition
**Positioning** is the place a product occupies in the target customer's mind relative to alternatives. A classic statement (Geoffrey Moore):

*For [target customer] who [need], [product] is a [category] that [key benefit]. Unlike [alternative], our product [differentiator].*

Components (April Dunford's *Obviously Awesome*): **competitive alternatives**, **unique attributes**, **value** those attributes bring, **target customers** who care most, and the **market category** that frames it. **Proof points** (data, testimonials, certifications, benchmarks) make it credible. Sequence: alternatives → differentiators → value → who cares → category.

Re-positioning means changing the frame (e.g., from "feature phone replacement" to "premium camera"). Positioning drives messaging, pricing, channels and the roadmap.

### Example
"For urban young investors who find stock trading complex, Groww is a simple investing app that makes first-time investing easy. Unlike traditional brokers with heavy interfaces, it offers clean UX and low friction." (Illustrative paraphrase of public positioning.)

### In the news
See news box. As AI assistants multiply, positioning on trust, task coverage and ecosystem becomes the differentiator once raw capability converges.

### Interview angle
> [!question] How it is asked
> "How would you position a new health-tracking wearable in India?"

> [!tip] Strong answer includes
> - Target segment, category and competitive alternatives
> - A one-line positioning statement
> - Differentiators supported by proof points
> - Consistent messaging, pricing and channel implications

---

## 12. Product Vision & Mission
> 🔴 Tier 1 · _Tracker hint:_ Inspirational long-term direction; team alignment

### Definition
- **Vision:** the future you want to create; inspiring, long-term (5–10 years), ambitious, "where we are going".
- **Mission:** what the product does today, for whom and why; "why we exist and how".
- **Strategy:** how you will get there; **roadmap** and **OKRs** turn it into action.

A good product vision is customer-centred, concise (one or two sentences), emotionally clear, and falsifiable enough to guide choices (it tells you what to say no to). Craft with stakeholders, test with customers, and communicate repeatedly. Product vision board (Roman Pichler): vision, target group, needs, product, business goals.

Common failures: vague slogans, revenue-only statements, not tied to decisions.

### Example
Google's mission: "to organize the world's information and make it universally accessible and useful." Amazon's long-time vision: be Earth's most customer-centric company. For a student's hypothetical app: "Every learner in a small town gets a top-tier teacher in their pocket."

### In the news
See news box. At OpenAI scale, mission statements about broad benefit become operational constraints on product, safety and access choices.

### Interview angle
> [!question] How it is asked
> "What's the vision for this product?" or "How do you align the team behind a vision?"

> [!tip] Strong answer includes
> - Vision vs mission vs strategy clarity
> - Customer-centred, concise, inspiring vision
> - Translation to goals, OKRs and trade-off decisions
> - How you communicate and test it with the team

---

## 13. ⭐ Advanced: Product-Led Growth and Moats
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Product-led growth (PLG)** uses the product itself as the main driver of acquisition, conversion and expansion: free tier or trial, self-serve onboarding, fast time-to-value, in-product virality, usage-based upgrade. Examples: Slack, Zoom, Canva, Notion, Dropbox.

Key mechanics: **activation** (time to "aha"), **viral coefficient** $k = i \times c$ (invites per user × conversion per invite; $k>1$ is self-sustaining), **freemium conversion**, **expansion revenue**. **Moats** that keep growth defensible: network effects, switching costs and data, scale and brand, integrations/ecosystem. PLG works best when the product is easy to try, valuable on its own, and has a low-friction price; it struggles with complex enterprise sales unless paired with sales-assist (PLS).

### Example
Each user invites 4 colleagues and 20% of them join: $k=4\times0.2=0.8$. Starting with 1,000 users, total reach converges to $1000/(1-0.8)=5{,}000$ (geometric sum), so virality alone multiplies reach 5x but doesn't run away; to get $k>1$, raise invites or conversion.

### In the news
See news box. ChatGPT's consumer reach fed a developer ecosystem (about 4 million developers), the platform stage of a PLG-style flywheel.

### Interview angle
> [!question] How it is asked
> "How would you grow a B2B SaaS tool without a big sales team?"

> [!tip] Strong answer includes
> - Self-serve loop: acquire, activate, convert, expand
> - Virality and activation maths
> - Moat choice and why it holds
> - When PLG is the wrong choice

---

## 14. ⭐ Advanced: Prioritisation Frameworks and Product Trade-offs
> ⭐ Advanced · _Added beyond the tracker_

### Definition
PMs rank many requests with limited capacity. Common tools:

- **RICE:** $(\text{Reach}\times\text{Impact}\times\text{Confidence})/\text{Effort}$.
- **ICE:** Impact × Confidence × Ease.
- **MoSCoW:** Must, Should, Could, Won't (this release).
- **Kano:** basic, performance, delighters; basics are expected, absence hurts.
- **Value vs effort 2x2:** quick wins first, avoid money pits.
- **Weighted scoring:** score against strategy-aligned criteria with weights.
- **Cost of delay / WSJF:** $\frac{\text{Cost of delay}}{\text{Job size}}$.

Decide with data and strategy: tie to the north star and OKRs; separate **discovery** (is it valuable?) from **delivery** (can we build it?). Communicate *why not*.

### Example
WSJF: Item X cost of delay Rs 30 lakh per month, size 2 months → 15. Item Y cost of delay Rs 50 lakh per month, size 5 months → 10. Do X first, even though Y's delay cost is higher in absolute terms.

### In the news
See news box. In hyper-growth, capacity and reliability work often outranks new features; cost-of-delay thinking helps defend that call.

### Interview angle
> [!question] How it is asked
> "You have 10 requests and capacity for 3. How do you choose?"

> [!tip] Strong answer includes
> - A named framework with scoring example
> - Linkage to strategy and metrics
> - Discovery vs delivery separation
> - Stakeholder communication of trade-offs

---
## 🔗 Go deeper: expansion notes
- [[164 Product Discovery & User Research|Product Discovery & User Research]]
- [[165 Platform & Marketplace Product Strategy|Platform & Marketplace Product Strategy]]
