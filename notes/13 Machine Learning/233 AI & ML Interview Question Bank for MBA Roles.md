---
tags: [machine-learning, tier1, ai, question-bank]
area: Machine Learning
topic: "AI & ML Interview Question Bank for MBA Roles"
tier: Tier 1
roles: All roles
status: complete
subtopics: 12
---
# AI & ML Interview Question Bank for MBA Roles

⬅ [[232 AI Productivity Toolkit for MBA Work - Excel, SQL, Decks & Research]] · [[_Index - Machine Learning|Machine Learning]]

> **Area:** Machine Learning · **Priority:** 🔴 Tier 1 · **Target roles:** All roles

**How to use:** this is the Machine Learning area's equivalent of [[143 SCM Interview Question Bank]] and [[215 Statistics Interview Question Bank & Numericals]]. Do the numericals with a timer (3 minutes each) and answer the rapid-fire questions aloud in 30-45 seconds each. Worked numbers were computed in Python. Links point to the note that teaches each concept.

## Sub-topics in this note
1. [[#1. How AI and ML Questions Are Asked in MBA Interviews]]
2. [[#2. Rapid-Fire I: Core Machine-Learning Concepts]]
3. [[#3. Rapid-Fire II: Generative AI and LLMs]]
4. [[#4. Numericals I: Classification Metrics and Cost-Sensitive Thresholds]]
5. [[#5. Numericals II: Forecast Error, Regression and Lift]]
6. [[#6. Numericals III: A/B Tests, AI Unit Economics and ROI]]
7. [[#7. Mini-Cases: AI in Operations and Supply Chain]]
8. [[#8. Product and AI-PM Questions]]
9. [[#9. Consulting and Strategy Opinion Questions]]
10. [[#10. Ethics, Risk and Regulation Questions]]
11. [[#11. Grilling on Your Own AI/ML Projects]]
12. [[#12. ⭐ Advanced: Explain-It Drills and Questions to Ask the Interviewer]]

## 📰 News box
> [!news] Shared news hook for this topic (2025–2026): the facts most likely to be dropped into an AI question
> - **Adoption vs value:** 88% of organisations use AI; about 6% are high performers earning ≥5% of EBIT from it (McKinsey, 5 Nov 2025). ([McKinsey](https://www.mckinsey.com/featured-insights/artificial-intelligence/the-state-of-ai-2025))
> - **Pilots:** about 95% of corporate GenAI pilots showed no measurable P&L impact (MIT NANDA, 2025). ([Computing](https://computing.co.uk/news/2025/ai/mit-report-95pc-corporate-generative-ai-pilots-fail))
> - **Agents:** Gartner (June 2025) expects over 40% of agentic AI projects to be cancelled by end-2027. ([Outlook Business](https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner))
> - **India:** AI Governance Guidelines (5 Nov 2025), DPDP Rules (14 Nov 2025), AI Impact Summit and New Delhi Declaration (Feb 2026), IndiaAI compute portal over 38,000 GPUs (Mar 2026); details in [[231 AI Industry Landscape, Economics & India AI Ecosystem]].
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. How AI and ML Questions Are Asked in MBA Interviews
> 🔴 Tier 1 · _Key points:_ Five question types; role-wise emphasis; the "concept → example → business implication → caveat" answer formula

### Definition
| Type | Example | Most common in |
|---|---|---|
| Concept check | "What is overfitting?" | analytics, PM, ops |
| Numerical | "Compute precision and recall from this table" | analytics, consulting tests, PM |
| Application | "Where would you use ML in our plant?" | operations, consulting |
| Opinion / current affairs | "Will AI replace planners?" | all, GDs |
| Project grilling | "Explain your churn model" | anyone with ML on the CV |

**Answer formula (45-60 seconds):** concept in one plain sentence → example from operations or the company's industry → business implication with a number → one caveat or risk. This mirrors the "fact, so-what, caveat" method in [[180 Current Affairs & Economy Briefing for MBA Interviews (2025-26)]].

### Example
Q: "What is overfitting?" A: "When a model learns noise in the training data, so it performs well on past data and poorly on new data. For example, a demand model with 50 features trained on one year might perfectly fit last Diwali but miss this year's shift in festival dates. The business impact is false confidence: planners trust a forecast that will be wrong. I'd guard against it with time-based validation and simpler models first ([[094 ML Fundamentals & Workflow]])."

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> Any of the five types, often mixed within one answer ("define it, then apply it to us").

> [!tip] Strong answer includes
> - Plain language first, jargon second
> - An example from their industry
> - A number and a caveat

---
## 2. Rapid-Fire I: Core Machine-Learning Concepts
> 🔴 Tier 1 · _Key points:_ 15 questions, one-line answers; expand using the linked notes

### Definition
1. **Supervised vs unsupervised?** Supervised learns from labelled outcomes (predict demand, default); unsupervised finds structure without labels (customer segments). [[094 ML Fundamentals & Workflow]]
2. **Classification vs regression?** Category output (late/on-time) vs numeric output (lead time in days).
3. **Bias-variance trade-off?** Simple models underfit (high bias); complex models overfit (high variance); choose complexity by validation error.
4. **Why a test set?** To estimate performance on unseen data honestly; never tune on it.
5. **Cross-validation?** Rotate training and validation folds to use data efficiently; for time series use rolling-origin, not random folds.
6. **Data leakage?** Information from the future or from the target sneaks into features (e.g., "days delayed" when predicting "late"), inflating accuracy.
7. **Feature engineering example in ops?** Lags, rolling averages, promotion flags, festival calendar, supplier on-time history.
8. **Random forest vs gradient boosting?** Forest averages many independent trees (robust, less tuning); boosting builds trees sequentially to fix errors (often more accurate, needs tuning). [[096 Classification Algorithms]]
9. **Why logistic regression is still used?** Interpretable, fast, well-calibrated probabilities; regulators and managers can follow it.
10. **K-means use case?** Segment SKUs or customers by volume, variability and margin; pick k with elbow/silhouette and business sense. [[097 Unsupervised Learning]]
11. **PCA?** Compresses correlated variables into fewer components; useful for visualisation and noise reduction. [[207 Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis]]
12. **Regularisation?** Penalises large coefficients (L1 lasso can zero them out; L2 ridge shrinks them) to reduce overfitting. [[095 Regression Algorithms]]
13. **SHAP?** Attributes each prediction to features additively; explains why the model flagged a supplier as risky. [[098 Model Selection & Optimization]]
14. **Model drift?** Input or relationship changes over time (new products, price shocks); monitor PSI and accuracy, retrain on triggers. [[220 Responsible AI, Explainability & Model Governance]]
15. **Reinforcement learning in ops?** Learns policies by trial and reward, e.g., inventory replenishment or dynamic pricing in simulation; rarely deployed raw in production. [[099 ML for Operations & SCM]]

### Example
Practice drill: set a 30-second timer per question; record yourself; mark any answer with jargon you could not explain. Re-do the weak ones after reading the linked note.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> Several in quick succession in analytics, PM and consulting-tech interviews.

> [!tip] Strong answer includes
> - One-sentence answers with an ops example
> - Honest "I'd check" for things you don't know well

---
## 3. Rapid-Fire II: Generative AI and LLMs
> 🔴 Tier 1 · _Key points:_ 15 questions; manager-level depth; see [[228 Generative AI & LLM Foundations for Managers]]

### Definition
1. **How does an LLM work?** Predicts the next token based on patterns learned from huge text; scale gives broad abilities.
2. **What is a token?** A word piece; about 0.75 English words; pricing and context limits are in tokens.
3. **Context window?** Maximum tokens the model can consider at once (prompt + answer).
4. **Hallucination and fixes?** Fluent false output; fix with grounding (RAG), citations, tools, abstention, human review.
5. **What is RAG?** Retrieve relevant documents at query time and give them to the model so answers are grounded and current. [[219 NLP, Embeddings & LLM Applications for Analysts]]
6. **Embeddings?** Numeric vectors capturing meaning; enable semantic search ("late delivery" finds "shipment delayed").
7. **Fine-tuning vs RAG?** Fine-tune for style/format or narrow tasks; RAG for changing knowledge; start with prompting and RAG.
8. **Temperature?** Randomness of output; low for extraction, higher for ideation.
9. **Reasoning models?** Spend more computation thinking before answering; better at multi-step problems; slower and dearer.
10. **Agent vs chatbot?** Agent plans and takes actions through tools; chatbot only converses. [[229 Agentic AI & Intelligent Automation in Operations]]
11. **MCP?** Open standard for connecting AI models to tools and data; donated to a Linux Foundation-hosted foundation in Dec 2025.
12. **Open-weight vs closed models?** Downloadable weights (control, residency) vs API-only (capability, convenience).
13. **How to evaluate an LLM feature?** Golden test set, task-specific metrics (accuracy, groundedness), LLM-as-judge with human calibration, online metrics. [[166 AI Product Management - LLM Products, Evals & Economics]]
14. **Prompt injection?** Malicious instructions hidden in content the model reads; defend with permissions, separation and approvals.
15. **Why do GenAI pilots fail?** Not integrated into workflows, no owner, no measurement, no feedback loop. [[230 AI Strategy, Use-Case Prioritisation & ROI]]

### Example
Follow-up chain an interviewer may run: "What is RAG?" → "When would RAG fail?" (bad retrieval, poor document quality, questions needing reasoning across many docs) → "How would you measure retrieval quality?" (recall@k on a labelled question set; groundedness of answers).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> PM and consulting interviews, increasingly operations roles too.

> [!tip] Strong answer includes
> - Clear definitions, no buzzword stacking
> - Business use and limits for each

---
## 4. Numericals I: Classification Metrics and Cost-Sensitive Thresholds
> 🔴 Tier 1 · _Key points:_ Accuracy paradox; precision/recall/F1; expected cost; threshold = C_FP / (C_FP + C_FN)

### Definition
From the confusion matrix ([[096 Classification Algorithms]]): precision = TP/(TP+FP); recall = TP/(TP+FN); F1 = 2PR/(P+R); accuracy = (TP+TN)/N. With calibrated probabilities, flag a case when $p > \dfrac{C_{FP}}{C_{FP}+C_{FN}}$ (the cost-minimising threshold).

### Example
**Q1.** A predictive-maintenance model covers 1,000 machine-weeks; 50 actual failures. It flags 80 machine-weeks, of which 40 fail.
- TP = 40, FP = 40, FN = 10, TN = 910.
- Precision = 40/80 = **0.50**; recall = 40/50 = **0.80**; F1 = 2 × 0.5 × 0.8 / 1.3 = **0.615**; accuracy = 950/1000 = **95%**.
- Trap: a model that predicts "no failure" always also scores 95% accuracy. Accuracy is useless here.

**Q2.** Each missed failure costs ₹5,00,000 (downtime, repair); each false alarm costs ₹20,000 (inspection). Expected cost with model = 40 × 20,000 + 10 × 5,00,000 = ₹8 lakh + ₹50 lakh = **₹58 lakh**; without model (all failures missed) = 50 × ₹5 lakh = **₹250 lakh**. Saving **₹192 lakh**.

**Q3.** Optimal probability threshold = 20,000 / (20,000 + 5,00,000) = **0.038**. Flag any machine with predicted failure probability above about 4%; false alarms are cheap relative to misses, so be aggressive.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "The model has 95% accuracy; should we deploy it?" with a confusion matrix.

> [!tip] Strong answer includes
> - Base rate check (accuracy paradox)
> - Precision/recall in business terms (false alarms vs misses)
> - Threshold from costs, and an expected-cost comparison

---
## 5. Numericals II: Forecast Error, Regression and Lift
> 🔴 Tier 1 · _Key points:_ MAPE vs WAPE vs bias; coefficient interpretation; R²; lift and gains

### Definition
- MAPE = mean of |A − F| / A; WAPE = Σ|A − F| / ΣA (volume-weighted, preferred in supply chain); bias = (ΣF − ΣA) / ΣA ([[012 Supply Chain Analytics & KPIs]], [[218 Forecasting with ML & Foundation Models]]).
- Linear regression coefficient = change in Y for a one-unit change in X, holding others constant; R² = share of variance explained ([[090 Regression Analysis]]).
- **Lift** in decile $d$ = (positive rate in decile) / (overall positive rate).

### Example
**Q4.** Actuals 100, 200, 50; forecasts 90, 230, 40.
- MAPE = (10% + 15% + 20%) / 3 = **15.0%**
- WAPE = (10 + 30 + 10) / 350 = **14.3%**
- Bias = (360 − 350) / 350 = **+2.9%** (slight over-forecast)
Note how MAPE over-weights the small item (50 units, 20% error).

**Q5.** Regression: Weekly sales = 1,200 + 35 × (promo spend in ₹'000) − 80 × (price in ₹), R² = 0.62. Interpretation: each extra ₹1,000 of promotion adds 35 units, holding price constant; each ₹1 price increase loses 80 units; 62% of week-to-week variation is explained. Caveat: correlation, not proof of causation; promotions may coincide with festivals ([[214 Causal Inference & Experimentation Beyond A-B Tests]]).

**Q6.** Churn base rate is 10%. The top decile of a churn model's scores contains 35% churners. Lift = 35% / 10% = **3.5**. If retention offers cost ₹200 and save 30% of targeted churners worth ₹3,000 margin each, value per 1,000 top-decile customers = 1,000 × 0.35 × 0.30 × 3,000 − 1,000 × 200 = ₹3,15,000 − ₹2,00,000 = **₹1.15 lakh**; at the 10% base rate the same campaign would lose money (1,000 × 0.10 × 0.30 × 3,000 = ₹90,000 < ₹2 lakh).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> Data-interpretation tables in consulting tests; forecasting questions in ops interviews; targeting questions in PM/marketing.

> [!tip] Strong answer includes
> - Correct formula and the arithmetic shown
> - The business interpretation (which error matters, who to target)
> - A caveat (MAPE distortion, causality)

---
## 6. Numericals III: A/B Tests, AI Unit Economics and ROI
> 🔴 Tier 1 · _Key points:_ Two-proportion z-test; power and sample size; token cost; payback

### Definition
Two-proportion z-test: $z = (p_2 - p_1)/\sqrt{\bar p(1-\bar p)(2/n)}$ for equal arm sizes $n$ ([[089 Hypothesis Testing]]). Model cost = volume × (tokens in × price in + tokens out × price out) / 10⁶ ([[228 Generative AI & LLM Foundations for Managers]]). Payback = one-time cost / net annual benefit.

### Example
**Q7.** An AI recommendation widget: control conversion 4.0%, treatment 4.4%, 20,000 users per arm. Pooled p = 4.2%; standard error = √(0.042 × 0.958 × 2/20,000) ≈ 0.00201; z = 0.004 / 0.00201 ≈ **1.99**; two-sided p ≈ **0.046**, significant at 5%. But the sample needed for 80% power to detect this 10% relative lift is about **39,500 per arm**, so this test was under-powered and the effect estimate is fragile; extend the test or replicate before full launch.

**Q8.** Support chatbot: 50,000 conversations/month, 3,000 input and 500 output tokens each, at \$2 / \$10 per million tokens. Cost = 150 M × \$2 + 25 M × \$10 = \$300 + \$250 = **\$550/month** ≈ ₹52,800 at ₹96/\$. If it deflects 40% of conversations from humans at ₹45 each: 20,000 × ₹45 = ₹9 lakh/month saving. Model cost is about 6% of the saving; integration and quality control dominate.

**Q9.** An AP agent costs ₹60 lakh to implement and ₹43 lakh a year to run; it saves ₹2.28 crore a year. Net annual benefit = ₹1.85 crore; payback = 60 / 185 × 12 ≈ **3.9 months** ([[229 Agentic AI & Intelligent Automation in Operations]], sub-topic 6).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> PM: "Your A/B test shows a lift; ship it?" Consulting: "Is this AI worth it?"

> [!tip] Strong answer includes
> - Significance and power, not only the p-value
> - Unit economics with assumptions stated
> - Sensitivity on the key driver (deflection rate, automation rate)

---
## 7. Mini-Cases: AI in Operations and Supply Chain
> 🔴 Tier 1 · _Key points:_ Four 5-minute cases with answer skeletons

### Definition
Use the structure: objective and baseline → options (AI and non-AI) → data and feasibility → KPIs and pilot → risks ([[230 AI Strategy, Use-Case Prioritisation & ROI]], sub-topic 12).

### Example
**Case A: "Forecast accuracy is 60% at SKU-week level for a paint company. Can ML help?"** Clarify metric (WAPE? bias?) and level; check data (sell-in vs sell-out, dealer stock, weather, construction season, price changes); baseline with exponential smoothing; global gradient-boosting model with weather and price features ([[218 Forecasting with ML & Foundation Models]]); measure forecast value added; also fix process (S&OP, consensus overrides). KPI: WAPE and bias at SKU-depot-week; inventory days; fill rate.

**Case B: "Use GenAI in procurement for a pharma company."** Spend classification; contract clause extraction and compliance; RFQ drafting and bid comparison; supplier risk monitoring from news and regulatory alerts (USFDA warning letters). Controls: GxP documentation, validation, human sign-off ([[132 Pharma & Healthcare Supply Chain]]).

**Case C: "A 3PL wants to cut empty truck miles with AI."** Baseline empty-km share; levers: backhaul matching via load-board data, route optimisation (OR solver), ML prediction of return-load availability by lane and day; pilot on top 20 lanes; KPI: empty-km %, cost per tonne-km, utilisation ([[125 Transportation Management Deep Dive]]).

**Case D: "Quality escapes rose at an auto-component plant. Would computer vision help?"** Pareto of defect types; check if defects are visually detectable at line speed; lighting and camera feasibility; label data from past rejects; pilot on one line; KPI: escape rate (ppm), false-reject rate, OEE impact; combine with root-cause work (8D, SPC) ([[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]], [[091 Statistical Quality Control (SQC)]]).

### In the news
See news box. Interviewers favour answers that combine AI with operations fundamentals rather than replacing them.

### Interview angle
> [!question] How it is asked
> As a 10-minute mini-case in operations and consulting interviews.

> [!tip] Strong answer includes
> - Baseline and root cause before technology
> - A data and feasibility check
> - KPIs, a pilot and non-AI levers

---
## 8. Product and AI-PM Questions
> 🟠 Tier 2 · _Key points:_ Design, metrics, evaluation, trade-offs; see [[166 AI Product Management - LLM Products, Evals & Economics]] and [[163 PM Interview Types & Answer Frameworks]]

### Definition
Common prompts and the skeleton:
1. **"Design an AI feature for [app]."** Users and pain → AI vs non-AI solution → MVP → evaluation → metrics → risks → roadmap.
2. **"How would you measure success of an AI assistant?"** North star (task completion), quality (accuracy, groundedness), engagement (repeat use), efficiency (time saved), guardrails (complaints, escalation, harmful outputs), cost per task.
3. **"Your AI feature's usage dropped after launch. Why?"** Segment by user, platform, query type; check quality regressions (model or prompt change), latency, cost-driven throttling, UX changes, novelty decay.
4. **"Build or buy the model?"** Differentiation, data, cost at scale, latency, privacy, vendor risk.
5. **"How do you prioritise AI ideas?"** RICE with an evaluation-readiness factor; value × feasibility.

### Example
"Design an AI feature for a quick-commerce app." Users: busy urban households. Pain: building a weekly basket is tedious. Feature: "Smart basket": predicts replenishment items from purchase history and suggests a one-tap basket; GenAI turns a recipe or a typed list ("dal tadka for 4, breakfast for the week") into a basket. Metrics: basket adoption rate, items accepted per suggested basket, AOV change, repeat use, wrong-item complaints. Risks: privacy, out-of-stock suggestions, pushy upselling. MVP: replenishment predictions first (classic ML), then the GenAI list-to-basket feature ([[129 E-commerce & Quick-Commerce Fulfilment]]).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> PM interviews at e-commerce, fintech, SaaS and GCC product teams.

> [!tip] Strong answer includes
> - User problem first, AI second
> - Evaluation plan and guardrail metrics
> - Staged roadmap with the cheapest validating MVP

---
## 9. Consulting and Strategy Opinion Questions
> 🟠 Tier 2 · _Key points:_ Balanced, data-backed opinions; structure; a clear stance

### Definition
Common opinion prompts with a one-line stance to build on (expand with [[231 AI Industry Landscape, Economics & India AI Ecosystem]]):
1. **"Will AI replace consultants?"** It automates research, analysis and drafting; it raises the bar on judgement, client relationships and implementation; pyramid structures will thin at the bottom.
2. **"Will AI replace supply chain planners?"** It shifts planners from data wrangling to exception management and scenario decisions; fewer planners per SKU, higher skill.
3. **"Should every company have an AI strategy?"** Every company needs a business strategy that uses AI where it creates measurable value; a standalone "AI strategy" often becomes technology theatre.
4. **"Is India ahead or behind in AI?"** Strong in talent, adoption, digital public infrastructure and GCCs; behind in frontier models, chips and compute, though IndiaAI and sovereign models are narrowing gaps.
5. **"AI bubble?"** Valuations may correct; the technology and adoption are real (sub-topic 12 of [[231 AI Industry Landscape, Economics & India AI Ecosystem]]).

### Example
"Will AI replace supply chain planners?" in 45 seconds: "Not replace, but reshape. Today planners spend maybe half their time gathering and cleaning data. AI and agents will take most of that, and ML forecasts already beat manual ones for stable items. What stays human is judgement on exceptions, trade-offs between cost and service, and aligning sales, finance and plants in S&OP. So teams will be smaller per SKU and more senior. The risk is that companies cut people before the tools are reliable; I'd scale headcount changes only after measured forecast value added."

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> Partner rounds, GDs, "what do you think about…" questions.

> [!tip] Strong answer includes
> - A clear stance in the first sentence
> - Two reasons with evidence
> - One caveat and an implication for the company

---
## 10. Ethics, Risk and Regulation Questions
> 🟠 Tier 2 · _Key points:_ Use the six-step responsible-AI frame from [[220 Responsible AI, Explainability & Model Governance]]

### Definition
Common questions:
1. **"Is it ethical to use AI in hiring?"** Depends on design and controls: bias audits, explanation, human decision, appeal, regulatory duties.
2. **"How would you make sure our model isn't biased?"** Define protected groups and fairness metric; test subgroup performance; check proxies; monitor; document.
3. **"What does India's DPDP Act mean for our AI project?"** Consent and purpose limitation, data minimisation, rights of data principals, breach notification, phased timelines from Nov 2025 Rules.
4. **"EU AI Act relevance for an Indian company?"** Applies if you place AI systems on the EU market or outputs are used there; high-risk categories have strict obligations; transparency duties for chatbots from Aug 2026.
5. **"Who is accountable when an AI makes a mistake?"** The deploying company; name a business owner; keep logs; human oversight by risk tier.

### Example
"A bank wants AI to approve small business loans automatically." Answer: stakes high (livelihoods), regulated sector; risks: bias by region or gender via proxies, opaque decisions, drift as economy changes; controls: interpretable model or explanations, fairness audits, human review of declines and mid-band scores, appeals, monitoring; recommendation: automate approvals of clearly strong applications, keep humans on declines; review quarterly.

### In the news
See news box. India's AI Governance Guidelines rely on existing laws plus principles, so accountability sits with deployers under sector regulators.

### Interview angle
> [!question] How it is asked
> Increasingly in consulting, BFSI and HR-tech interviews; also as GD topics.

> [!tip] Strong answer includes
> - Stakes and stakeholders, risks, controls, law, decision
> - Not absolutist; conditions for responsible use

---
## 11. Grilling on Your Own AI/ML Projects
> 🔴 Tier 1 · _Key points:_ Anything on your CV is fair game; prepare the 12 standard probes

### Definition
For every ML or AI project on your resume, prepare answers to:
1. What business problem, and who used the output?
2. What data, how much, from where, and what cleaning?
3. Why this model? What baseline did you beat, and by how much?
4. How did you validate (split, cross-validation, time-aware)?
5. Which metric and why (not just accuracy)?
6. What were the most important features, and did they make business sense?
7. What went wrong or surprised you?
8. Was there any leakage risk?
9. How would you deploy and monitor it?
10. What was the business impact (or estimated impact)?
11. What would you do with more time or data?
12. If GenAI: how did you evaluate outputs, what did it cost, and how did you handle hallucinations?

### Example
CV line: "Built XGBoost model to predict supplier delivery delays (AUC 0.81)." Probe: "AUC 0.81 against what baseline?" Good: "A logistic regression with the same features gave 0.74 and the buyer's rule-of-thumb (past 3-month OTD below 85%) gave 0.66. At our chosen threshold the model caught 70% of late deliveries with 45% precision, which let buyers expedite about 30 POs a week. Biggest lesson: our first version had 0.93 AUC because it used the GRN posting date, which leaks the outcome."

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "Walk me through this project" followed by three levels of "why".

> [!tip] Strong answer includes
> - Numbers you can defend, baselines and the metric choice
> - A mistake you found and fixed
> - Business use and next steps

---
## 12. ⭐ Advanced: Explain-It Drills and Questions to Ask the Interviewer
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Explain-it drills:** practise explaining the same concept at three levels in under 45 seconds each: (a) to a 10-year-old, (b) to a plant head, (c) to a data scientist. Concepts to drill: machine learning, overfitting, precision vs recall, RAG, AI agent, A/B test, model drift.

**Smart questions to ask** (choose ones that fit the role):
- "Which AI or analytics initiatives in your function have moved from pilot to production, and what made them work?"
- "How do planners/buyers/consultants here use AI tools day to day?"
- "What data foundations are you investing in this year?"
- "How do you measure value from AI projects here?"
- "What would make a new associate stand out in using these tools responsibly?"

### Example
"Precision vs recall" three ways:
- *10-year-old:* "If you're catching mangoes falling from a tree, recall is how many falling mangoes you catch; precision is how many things you caught are actually mangoes and not leaves."
- *Plant head:* "Recall: of all machine failures, how many the system warned us about. Precision: of all warnings, how many were real. We can catch more failures if we accept more false alarms."
- *Data scientist:* "TP/(TP+FN) vs TP/(TP+FP); we'll choose the threshold by the cost ratio of misses to false alarms, roughly 25:1 here."

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "Explain X to me as if I were [non-technical person]" and "Do you have any questions for us?"

> [!tip] Strong answer includes
> - Analogy matched to the listener
> - Accuracy preserved under simplification
> - Questions that show research and genuine interest
