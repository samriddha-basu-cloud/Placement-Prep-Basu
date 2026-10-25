---
tags: [machine-learning, tier1, ai, consulting]
area: Machine Learning
topic: "AI Strategy, Use-Case Prioritisation & ROI"
tier: Tier 1
roles: Consulting / Operations / PM
status: complete
subtopics: 12
---
# AI Strategy, Use-Case Prioritisation & ROI

⬅ [[229 Agentic AI & Intelligent Automation in Operations]] · [[_Index - Machine Learning|Machine Learning]] · [[231 AI Industry Landscape, Economics & India AI Ecosystem]] ➡

> **Area:** Machine Learning · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations / PM

**Why this matters for placements:** "AI transformation" is now one of the largest consulting service lines, and AI cases appear in consulting, product and operations interviews. The questions are rarely about algorithms; they are about **where to play, how to prioritise, how to prove value and how to scale**. Pair this note with [[024 Consulting Frameworks]] and [[162 Structured Communication - SCQA, Storylines & Case Delivery]].

## Sub-topics in this note
1. [[#1. AI Value Levers: Revenue, Cost, Capital, Risk and Experience]]
2. [[#2. Use-Case Discovery: Process Walk, Pain Points and Value at Stake]]
3. [[#3. Prioritisation: Value × Feasibility Matrix and Scoring]]
4. [[#4. Data Readiness Assessment]]
5. [[#5. Building the Business Case: NPV, Payback and Sensitivity]]
6. [[#6. Build, Buy or Partner]]
7. [[#7. Proving Value: Baselines, Controls and Attribution]]
8. [[#8. From Pilot to Scale: Crossing the "GenAI Divide"]]
9. [[#9. Operating Model: AI CoE, Hub-and-Spoke and Roles]]
10. [[#10. Change Management and Adoption]]
11. [[#11. AI Maturity Models and Roadmaps]]
12. [[#12. ⭐ Advanced: Solving an AI Strategy Case End to End]]

## 📰 News box
> [!news] Shared news hook for this topic (2025–2026): value concentrates in few firms; pilots stall; capex keeps rising
> **Most firms use AI; few make money from it.** McKinsey's *State of AI 2025* (5 Nov 2025): 88% use AI in at least one function; about one-third have begun scaling enterprise-wide; 39% see any EBIT impact; about 6% are "high performers" (≥5% of EBIT from AI). 32% of respondents expect AI to reduce their workforce by 3% or more in the next year. ([McKinsey](https://www.mckinsey.com/featured-insights/artificial-intelligence/the-state-of-ai-2025))
>
> **95% of GenAI pilots show no P&L impact** in MIT NANDA's *GenAI Divide* report (2025); bought tools succeeded about twice as often as internal builds, and more than half of budgets went to sales and marketing even though back-office uses returned more. ([Computing](https://computing.co.uk/news/2025/ai/mit-report-95pc-corporate-generative-ai-pilots-fail))
>
> **Spend keeps climbing.** The four largest US hyperscalers (Amazon, Microsoft, Alphabet, Meta) guided to roughly \$730 billion of combined 2026 capex by late July 2026, versus about \$410 billion in 2025, much of it for AI data centres. ([Analysis Atlas](https://analysis-atlas.com/research/hyperscaler-ai-capex-2026/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. AI Value Levers: Revenue, Cost, Capital, Risk and Experience
> 🔴 Tier 1 · _Key points:_ Tie every use case to a P&L, balance-sheet or risk line; MECE lever tree

### Definition
An **AI value-lever tree** (MECE, [[024 Consulting Frameworks]]):
- **Revenue:** better pricing and promotions, personalisation and cross-sell, fewer lost sales from stock-outs, faster quote turnaround, new AI-enabled products.
- **Cost:** labour productivity (drafting, processing, support), procurement savings (spend analytics, negotiation prep), quality (fewer defects), logistics (routing, load building), energy.
- **Capital (working capital and capex):** lower inventory from better forecasts, faster collections, higher asset utilisation from predictive maintenance ([[018 Capacity Management & OEE]]).
- **Risk:** fraud detection, compliance monitoring, supplier risk ([[015 Supply Chain Risk & Resilience]]).
- **Experience:** customer satisfaction, employee experience, speed.

Rule: a use case without a lever and a metric is a demo, not a business case.

### Example
For a cement company: **revenue**: dealer-level price recommendations; **cost**: kiln fuel-mix optimisation with ML (energy is a large share of cost), GenAI for dispatch-desk queries; **capital**: predictive maintenance on mills to cut unplanned downtime; **risk**: anomaly detection on diesel consumption by trucks. Each mapped to one P&L line and one KPI.

### In the news
See news box. McKinsey's high performers are distinguished by pursuing growth and innovation goals as well as cost.

### Interview angle
> [!question] How it is asked
> "How can AI create value for a steel / FMCG / logistics company?"

> [!tip] Strong answer includes
> - A lever tree before examples (structure first)
> - Industry-specific examples tied to cost structure
> - Prioritisation by size of the cost or revenue pool

---
## 2. Use-Case Discovery: Process Walk, Pain Points and Value at Stake
> 🔴 Tier 1 · _Key points:_ Start from processes and pain, not technology; quantify the pool before the solution

### Definition
Discovery steps:
1. **Walk the value chain** (plan-source-make-deliver-return, [[111 SCOR Model & Supply Chain Process Frameworks]]; or the customer journey).
2. **Find pain points:** where effort, errors, delays, leakage or lost revenue concentrate. Interview process owners; use process mining and data.
3. **Size the pool (value at stake):** cost or revenue affected × plausible improvement %.
4. **Map AI patterns** to each pain: predict, optimise, generate, extract, converse, act ([[228 Generative AI & LLM Foundations for Managers]]).
5. **Long-list** 20-40 ideas, then prioritise.

Value at stake = addressable base × improvement %. Keep it a range, with the assumptions written down.

### Example
Mid-size pharma distributor, revenue ₹3,000 crore:
| Pain point | Addressable base | Improvement | Value at stake |
|---|---|---|---|
| Near-expiry write-offs | ₹45 crore/yr | 20-30% | ₹9-13.5 crore |
| Order-desk effort (WhatsApp/phone orders) | 120 staff × ₹4.5 lakh = ₹5.4 crore | 30-40% | ₹1.6-2.2 crore |
| Collections delays (DSO 62 days) | receivables ≈ ₹510 crore | 5 days lower DSO | ≈ ₹41 crore cash released one-time |

Near-expiry and DSO dominate; order-desk automation is smaller but quick.

### In the news
See news box. Firms that start from technology ("we need a chatbot") are over-represented in the 95% of stalled pilots.

### Interview angle
> [!question] How it is asked
> "You have two weeks to identify AI opportunities for a client. How do you go about it?"

> [!tip] Strong answer includes
> - Process-led discovery with interviews and data
> - Value-at-stake sizing with ranges
> - A long list narrowed by explicit criteria

---
## 3. Prioritisation: Value × Feasibility Matrix and Scoring
> 🔴 Tier 1 · _Key points:_ 2×2 of value vs feasibility; weighted scoring; quick wins, big bets, fill-ins, money pits

### Definition
Plot use cases on **value** (value at stake, strategic fit) and **feasibility** (data readiness, technical maturity, integration effort, risk, change effort). Quadrants:
- **Quick wins:** high value, high feasibility, do now.
- **Big bets:** high value, low feasibility, invest in foundations (data, platforms) and stage them.
- **Fill-ins:** low value, high feasibility, do if cheap or as capability builders.
- **Money pits:** low value, low feasibility, avoid.

Weighted scoring (like RICE in product, [[034 Prioritization Frameworks]]): Score = Σ weight × rating, with weights agreed with leadership. Also check **dependencies** (a forecast model may be needed before a replenishment agent) and **sequencing** to build reusable capabilities.

### Example
Weights: value 40%, data readiness 20%, technical feasibility 15%, risk 10% (higher = lower risk), time-to-value 15%. Ratings 1-5:

| Use case | Value | Data | Tech | Risk | Speed | **Score** |
|---|---|---|---|---|---|---|
| Near-expiry prediction & redistribution | 5 | 4 | 4 | 4 | 3 | **4.25** |
| Collections prioritisation (DSO) | 4 | 4 | 5 | 4 | 4 | **4.15** |
| Order-desk GenAI assistant | 3 | 3 | 4 | 3 | 5 | **3.45** |
| Fully autonomous procurement agent | 4 | 2 | 2 | 1 | 1 | **2.55** |

(For the first row: 0.4×5 + 0.2×4 + 0.15×4 + 0.1×4 + 0.15×3 = 2.0 + 0.8 + 0.6 + 0.4 + 0.45 = 4.25.)

### In the news
See news box. Gartner's prediction that over 40% of agentic projects will be cancelled is largely about "money pit" choices made without a feasibility screen ([[229 Agentic AI & Intelligent Automation in Operations]]).

### Interview angle
> [!question] How it is asked
> "The client has 30 AI ideas and budget for 3. How do you choose?"

> [!tip] Strong answer includes
> - Value × feasibility with explicit sub-criteria and weights
> - Dependencies and sequencing (foundations first)
> - Portfolio balance: quick wins to fund and prove, one big bet for strategy

---
## 4. Data Readiness Assessment
> 🔴 Tier 1 · _Key points:_ Availability, quality, granularity, history, access rights, labels, latency; data is the usual bottleneck

### Definition
Questions to score data readiness for each use case:
1. **Availability:** does the data exist in a system (ERP, WMS, CRM) or in spreadsheets and emails?
2. **Quality:** completeness, accuracy, consistency of master data ([[175 Data Quality, Master Data & Data Governance]]).
3. **Granularity and history:** SKU-location-day for forecasting; 2-3 years with seasonality ([[218 Forecasting with ML & Foundation Models]]).
4. **Labels:** for supervised ML, do we know the outcomes (fraud yes/no, failure dates)?
5. **Access and rights:** consent and purpose under the DPDP Act, contracts, data residency ([[220 Responsible AI, Explainability & Model Governance]]).
6. **Latency:** batch is fine for weekly planning; real-time needed for fraud or routing.
7. **Unstructured data:** documents and emails are now usable by GenAI, which widens what is feasible.

### Example
Predictive maintenance on 40 crushers: sensor data exists only for 12 machines (installed last year), failure logs are free-text in the CMMS with inconsistent codes, and no labels link sensor patterns to failures. Readiness score 2/5. Recommendation: start with GenAI to structure 5 years of maintenance logs into failure modes (feasible now), install sensors on the critical 15 machines, and revisit the ML model in 9-12 months ([[155 Reliability Engineering & Maintenance Optimisation]]).

### In the news
See news box. Most of the "learning gap" MIT describes is about tools not connected to company data and workflows.

### Interview angle
> [!question] How it is asked
> "What do you need before you can build an AI model for X?"

> [!tip] Strong answer includes
> - A data checklist applied to the case
> - Interim value (what can be done with today's data)
> - Data foundation steps with a timeline

---
## 5. Building the Business Case: NPV, Payback and Sensitivity
> 🔴 Tier 1 · _Key points:_ Separate one-time cash (working capital) from recurring savings; avoid double counting; ramp-up; sensitivity reveals what really drives value

### Definition
AI business case = incremental cash flows over 3-5 years, discounted ([[109 Valuation Basics (NPV, IRR, DCF)]], [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]):
- **Benefits:** labour hours actually redeployed or avoided, cost savings, margin from extra revenue (not revenue itself), working-capital release (one-time cash), risk reduction (expected loss avoided).
- **Costs:** build/licence, integration, data work, cloud and model usage, run team, change management, model monitoring and retraining.
- **Ramp-up:** benefits rarely reach 100% in year 1.
- **Pitfalls:** counting revenue instead of contribution; counting both the cash release of inventory **and** the capital cost on that inventory; assuming freed hours become savings without a headcount or growth plan.

### Example
**AI demand-sensing for an FMCG firm** (₹ crore, illustrative). Inventory ₹600 crore, of which safety stock ≈ ₹240 crore. Forecast error (WAPE) falls from 35% to 28%, so safety stock falls about 20% (it scales with error, [[003 Inventory Management]]): **₹48 crore released**, half in year 1 and half in year 2. Non-capital holding cost (storage, obsolescence) saved at 8% = ₹3.84 crore/yr. Fewer stock-outs save ₹15 crore revenue at 30% contribution = ₹4.5 crore/yr. Run cost ₹3 crore/yr; build ₹8 crore. Ramp 50%, 100%, 100%. Discount rate 12%.

| Year | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Cash flow incl. inventory release | −8.00 | 25.17 | 29.34 | 5.34 |
| Cash flow, operating only | −8.00 | 1.17 | 5.34 | 5.34 |

NPV including inventory release ≈ **₹41.7 crore**; operating-only NPV ≈ **₹1.1 crore**; if lost-sales benefit is only half, operating NPV ≈ **−₹3.3 crore**. Message to the CFO: the case **is** the working-capital release, so make inventory policy changes (lowering safety-stock parameters in ERP) part of the project scope, or the benefit never materialises.

### In the news
See news box. The small share of firms reporting EBIT impact reflects benefits that were never converted into P&L or balance-sheet changes.

### Interview angle
> [!question] How it is asked
> "Is this AI investment worth it?" with a data table.

> [!tip] Strong answer includes
> - Clear separation of one-time and recurring flows; contribution not revenue
> - NPV/payback with a ramp
> - Sensitivity that identifies the decisive assumption and how to secure it

---
## 6. Build, Buy or Partner
> 🟠 Tier 2 · _Key points:_ Buy for commodity capability, build for differentiation and proprietary data, partner for speed plus customisation

### Definition
| Option | When | Watch-outs |
|---|---|---|
| **Buy (SaaS, embedded AI in ERP/CRM)** | common processes (AP, service desk, spend analytics); speed matters | lock-in, fit to process, data rights |
| **Build (in-house team on cloud/model APIs)** | proprietary data or process is the advantage (pricing, network optimisation) | talent, time, maintenance burden |
| **Partner (consultancy/SI, start-up co-development)** | need speed and customisation; building internal capability | knowledge transfer, IP terms |

Decision factors: strategic differentiation, data uniqueness, time-to-value, total cost of ownership (5 years), internal skills, vendor maturity, and exit options. See also [[166 AI Product Management - LLM Products, Evals & Economics]] (build vs buy vs fine-tune).

### Example
A retailer: buys an AI service-desk tool for HR and IT queries (commodity), builds its own markdown-pricing model on proprietary sell-through data (differentiating), and partners with a start-up for computer-vision shelf audits (specialised, fast-moving tech) with a clause giving it rights to its labelled image data.

### In the news
See news box. MIT's finding that purchased tools succeeded about twice as often as internal builds is a strong prior for "buy" outside core differentiators.

### Interview angle
> [!question] How it is asked
> "Should the client build its own AI or buy a vendor product?"

> [!tip] Strong answer includes
> - Criteria table and a recommendation per use case, not one answer for all
> - TCO over several years, not licence price alone
> - Data ownership and exit terms

---
## 7. Proving Value: Baselines, Controls and Attribution
> 🟠 Tier 2 · _Key points:_ Measure before; control group or staggered rollout; financial sign-off; avoid vanity metrics

### Definition
- **Baseline:** current KPI level over a representative period (seasonality!).
- **Counterfactual:** A/B test, holdout regions/stores/SKUs, staggered (stepped-wedge) rollout, or difference-in-differences ([[214 Causal Inference & Experimentation Beyond A-B Tests]]).
- **Leading vs lagging metrics:** adoption and accuracy (leading) vs cost, margin, inventory (lagging).
- **Finance sign-off:** agree the benefit methodology with the CFO's team before the pilot.
- **Vanity metrics to avoid:** number of prompts, "hours saved" self-reported, number of use cases launched.

### Example
Route-optimisation pilot in 10 of 40 depots. Fuel cost per delivered tonne-km fell 9% in pilot depots and 3% in the other 30 (diesel prices fell). Difference-in-differences attributes **6 percentage points** to the tool, not 9. At ₹40 crore annual fuel spend across all depots, scaled value ≈ ₹2.4 crore a year, not ₹3.6 crore.

### In the news
See news box. Only 39% of McKinsey respondents could attribute any EBIT impact to AI, a sign that measurement design is often missing.

### Interview angle
> [!question] How it is asked
> "The pilot saved 9%. Should we roll out?"

> [!tip] Strong answer includes
> - Ask about the control group and external factors
> - Difference-in-differences logic in one line
> - Scale decision with the attributed, not raw, benefit

---
## 8. From Pilot to Scale: Crossing the "GenAI Divide"
> 🔴 Tier 1 · _Key points:_ Pilots fail on workflow fit, integration, ownership and learning; design pilots to scale

### Definition
Why pilots stall ("pilot purgatory"):
1. Built as a demo outside the real workflow and systems.
2. No business owner accountable for the KPI.
3. No integration budget; manual copy-paste kills adoption.
4. No feedback loop, so the tool does not improve.
5. Success criteria undefined, so there is no decision.
6. Risk, legal and IT reviews start only after the pilot.

**Scale-ready pilot design:** real users, real data, in the actual system; owner with a target; integration in scope; risk review in parallel; go/fix/stop gates; a scale plan (sites, cost, team) written before the pilot starts.

### Example
A bank's GenAI credit-memo drafting pilot impressed users but stalled: it ran in a separate web tool, analysts pasted data in by hand, and model risk management saw it only in month 4. The relaunch embedded drafting inside the loan-origination system, pulled financials via API, involved model risk from week 1, and targeted a 30% cut in memo turnaround. It scaled to all branches in two quarters.

### In the news
See news box. MIT's report frames the divide as a "learning gap": tools that do not adapt to workflows or learn from feedback.

### Interview angle
> [!question] How it is asked
> "Why do most AI pilots fail, and how would you avoid that?"

> [!tip] Strong answer includes
> - Three or four specific causes, not "lack of data" alone
> - Pilot design principles that anticipate scale
> - Ownership and measurement

---
## 9. Operating Model: AI CoE, Hub-and-Spoke and Roles
> 🟠 Tier 2 · _Key points:_ Centralised vs federated vs hub-and-spoke; key roles; governance forums

### Definition
- **Centralised CoE (centre of excellence):** one team builds everything; good for early stages and scarce talent; risks becoming a bottleneck far from business needs.
- **Federated:** each business unit has its own teams; fast and close to the business; duplication and inconsistent standards.
- **Hub-and-spoke (most common at scale):** the hub owns platforms, standards, governance, reusable components and talent development; spokes in business units own use cases and adoption.

Roles: business product owner, data/ML engineers, AI/ML scientists, AI product manager ([[166 AI Product Management - LLM Products, Evals & Economics]]), MLOps/platform engineers, data stewards, risk/compliance, change managers and "AI translators" (business people who frame problems, often an MBA role). Governance: an AI steering committee for portfolio and funding; a risk forum for high-risk use cases ([[220 Responsible AI, Explainability & Model Governance]]).

### Example
A conglomerate sets up a group AI hub of 40 people (platform, governance, top talent) and spokes in cement, retail and financial services, each with an AI product owner and 5-10 builders. The hub provides an approved model gateway, prompt and evaluation tooling, and a use-case registry; spokes are measured on business KPIs.

### In the news
See news box. In India, many multinationals run these hubs from global capability centres ([[231 AI Industry Landscape, Economics & India AI Ecosystem]]).

### Interview angle
> [!question] How it is asked
> "How should a company organise for AI?"

> [!tip] Strong answer includes
> - Three models with trade-offs, then a recommendation by maturity
> - Roles including business ownership and translators
> - Governance forums and funding mechanism

---
## 10. Change Management and Adoption
> 🔴 Tier 1 · _Key points:_ Adoption is the bottleneck; ADKAR; redesign roles and incentives; trust through transparency

### Definition
AI changes jobs, so adoption needs deliberate change management ([[169 Project Team Leadership, Conflict & Team Development]]). **ADKAR** (Awareness, Desire, Knowledge, Ability, Reinforcement) is a practical checklist:
- **Awareness:** why change, what it means for each role.
- **Desire:** address fears (job loss, blame for AI errors); show what people gain (less drudgery, new skills).
- **Knowledge and Ability:** training on the tool and on judgement (when to override).
- **Reinforcement:** KPIs and incentives updated; leaders use the tool visibly; success stories.

Also: **job redesign** (what tasks move to AI, what new tasks appear), **workforce planning** (redeployment, natural attrition vs layoffs), union and works-council consultation where relevant, and an honest communication line.

### Example
Planners ignored a new ML forecast and kept overriding it, so forecast value added was negative ([[099 ML for Operations & SCM]]). Fixes: show the drivers behind each forecast, track override accuracy publicly (planner overrides improved accuracy only 38% of the time), allow overrides only with a reason code, and change the planner KPI from "forecast accuracy" to "forecast value added". Overrides fell by half within a quarter and accuracy improved.

### In the news
See news box. With a third of firms expecting workforce reductions, employees' fears are reasonable; change plans have to address them directly.

### Interview angle
> [!question] How it is asked
> "The model is accurate but nobody uses it. What do you do?"

> [!tip] Strong answer includes
> - Diagnose: trust, workflow fit, incentives, skills
> - Specific interventions (explainability, KPI change, training, leadership use)
> - Measure adoption and value added

---
## 11. AI Maturity Models and Roadmaps
> 🟠 Tier 2 · _Key points:_ Five stages; foundations vs use cases; 3-horizon roadmap

### Definition
A generic **AI maturity ladder**:
1. **Exploring:** ad-hoc experiments, shadow AI use by employees.
2. **Piloting:** a few funded pilots, little reuse.
3. **Scaling:** platforms, governance, several use cases in production with KPIs.
4. **Embedded:** AI in core processes across functions; data products; operating model in place.
5. **AI-native:** products and business model built around AI; continuous learning loops.

**Roadmap in three horizons:** H1 (0-6 months) quick wins and governance basics; H2 (6-18 months) data foundations, platform, scaling 3-5 use cases; H3 (18-36 months) big bets and business-model changes. Similar to supply-chain maturity frameworks ([[112 Supply Chain Strategy - Fit, Segmentation & Maturity]]).

### Example
A mid-size auto-component group at stage 2 (three disconnected pilots). Roadmap: H1, an AI policy and approved tools for all staff, plus two P2P quick wins; H2, a data platform with clean material and supplier masters, predictive maintenance on bottleneck lines, a demand-sensing pilot with the top OEM customer; H3, an AI-assisted quoting system for new parts (RFQ to quote in days instead of weeks).

### In the news
See news box. About one-third of firms report starting enterprise-wide scaling, i.e. moving from stage 2 to stage 3.

### Interview angle
> [!question] How it is asked
> "Draw an AI roadmap for our company for the next three years."

> [!tip] Strong answer includes
> - Current-state assessment first
> - Horizons mixing quick wins, foundations and big bets
> - Governance and people work alongside technology

---
## 12. ⭐ Advanced: Solving an AI Strategy Case End to End
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A case structure for "Should client X invest in AI for Y?" (adapts the profitability/investment frameworks in [[025 Case Interview — Profitability]] and [[026 Case Interview — Operations Cases]]):
1. **Clarify objective:** cost, growth, service, risk? Time frame? Budget?
2. **Understand the process and baseline:** volumes, costs, KPIs, pain points.
3. **Generate options:** AI and non-AI (process fix, rules, outsourcing). Interviewers reward considering the non-AI option.
4. **Evaluate:** value at stake, feasibility (data, tech, people), risk, cost.
5. **Recommend:** with pilot design, KPIs, gates and risks.

### Example
**Case prompt:** "A national cold-chain logistics company with 600 reefer trucks loses 2.5% of pharma and food loads to temperature excursions. It wants to use AI. What should it do?"
- *Clarify:* objective is to cut excursion losses and claims; value of goods carried ₹2,400 crore/yr; losses and claims ≈ 2.5% = ₹60 crore.
- *Baseline:* excursions cluster at loading docks (40%), door openings during multi-drop (35%), equipment failure (25%).
- *Options:* (a) ML predictive maintenance on reefer units using telematics (targets 25% cause); (b) real-time anomaly alerts with driver instructions (targets door-opening and dock causes); (c) process fixes: pre-cooling SOPs, dock scheduling ([[133 Food, Agri & Perishables Supply Chain - India]], [[132 Pharma & Healthcare Supply Chain]]).
- *Evaluate:* telematics data exists for 70% of fleet; process fixes cheap and fast; alerts need a control-room workflow.
- *Recommend:* immediate SOP fixes (est. 30% of dock-related losses, ₹7 crore), anomaly-alert pilot on 100 trucks (target 40% cut in door-opening excursions), predictive maintenance after 6 months of clean sensor data. Total addressable ≈ ₹20-25 crore/yr against ₹6-8 crore investment; stop the alert pilot if excursion rate on pilot trucks does not fall 25% vs control trucks in 12 weeks.

### In the news
See news box. Interviewers increasingly test whether candidates can resist "AI for everything" and combine AI with process and operations fundamentals.

### Interview angle
> [!question] How it is asked
> The full case above, or "Our competitor announced an AI initiative. Should we respond?"

> [!tip] Strong answer includes
> - Clarifying the objective and the baseline with numbers
> - AI and non-AI options, evaluated on value and feasibility
> - A staged recommendation with KPIs, controls and a stop rule
