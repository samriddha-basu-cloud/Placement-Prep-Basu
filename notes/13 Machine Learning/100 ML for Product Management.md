---
tags: [machine-learning, tier2]
area: Machine Learning
topic: "ML for Product Management"
tier: Tier 2
roles: PM
status: complete
subtopics: 10
---
# ML for Product Management

⬅ [[099 ML for Operations & SCM]] · [[_Index - Machine Learning|Machine Learning]] · [[101 Deep Learning Basics]] ➡

> **Area:** Machine Learning · **Priority:** 🟠 Tier 2 · **Target roles:** PM

## Sub-topics in this note
1. [[#1. Churn Prediction Model]]
2. [[#2. Recommendation Systems]]
3. [[#3. A/B Test Analysis with Stats]]
4. [[#4. Personalization with ML]]
5. [[#5. NLP for Product]]
6. [[#6. Search & Ranking]]
7. [[#7. Fraud Detection]]
8. [[#8. Customer Lifetime Value (CLV) Prediction]]
9. [[#9. ⭐ Advanced: Uplift Modelling and Causal Inference for PMs]]
10. [[#10. ⭐ Advanced: Experiment Metrics, Guardrails and Metric Design]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): ML-driven fraud control and scale at UPI
> **UPI at 10 years (2026).** PIB reports UPI processed **24,161.69 crore transactions worth ₹314 lakh crore in FY2025-26** (vs 2 crore transactions in FY2016-17), with a daily average of ~66 crore transactions in 2025, 703 banks live by March 2026 and a peak month of 2,264 crore transactions (March 2026). At this scale fraud/risk models must score payments in real time. ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2257087&reg=3&lang=2))
> 
> **RBI's MuleHunter.AI.** Built by the Reserve Bank Innovation Hub, it uses AI/ML to flag mule accounts used to move fraud proceeds; an industry write-up (Sept 2026) says it is live across **31 banks**. ([RMA India](https://rmaindia.org/mulehunter-ai-rbis-ai-fraud-detection-system-now-live-across-31-banks/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Churn Prediction Model
> 🟠 Tier 2 · _Tracker hint:_ Features: usage, recency, support tickets; XGBoost; output = churn probability

### Definition
**Churn** = a customer stops using or paying for the product within a defined window. A churn model estimates $P(\text{churn in next } k \text{ days})$ per user, so the team can intervene.

Design steps: (1) define churn precisely (subscription cancel, or no activity for 30 days), (2) choose an **observation window** (features) and a **prediction window** (label) with no overlap to avoid leakage, (3) engineer features: RFM (recency, frequency, monetary), usage trend, feature adoption, support tickets, NPS, payment failures, tenure, (4) train logistic regression (baseline) or XGBoost, (5) evaluate with AUC, precision/recall at top-k, and **lift** (churners captured in the top decile vs random), (6) act: target the retention offer to users with high churn probability and high value.

Key point for PMs: predicting churn is not enough; you need **uplift** (who responds to the intervention) and a cost-benefit rule: intervene if $P(\text{churn})\times\text{value saved}\times\text{success rate} > \text{offer cost}$.

```python
import xgboost as xgb
m = xgb.XGBClassifier(n_estimators=300, max_depth=4, learning_rate=0.05,
                      scale_pos_weight=neg/pos)
m.fit(X_train, y_train)
p = m.predict_proba(X_test)[:, 1]
```

### Example
10,000 subscribers, baseline monthly churn 5% = 500 churners. The model's top decile (1,000 users) contains 200 churners: precision 20%, **lift = 20%/5% = 4×**. A ₹100 offer to these 1,000 users costs ₹1,00,000; if it saves 25% of the 200 (50 users) worth ₹1,200 each = ₹60,000. Not worth it at that value; targeting needs higher value or a cheaper offer.

### In the news
See news box. UPI has 703 live banks and ~66 crore daily transactions, so payment apps compete on repeat usage; scoring each user's likelihood of lapsing is how they decide whom to retain (the application is analytical, not from the source).

### Interview angle
> [!question] How it is asked
> "Users are churning. How would you use data and ML to reduce churn?" or "Design a churn prediction feature for a SaaS product."

> [!tip] Strong answer includes
> - Churn definition, windows, leakage avoidance
> - Features and model choice, metrics beyond accuracy (lift, precision at k)
> - Intervention design and uplift; cost-benefit
> - Experiment to prove retention offers work (A/B)
> - Root-cause (qualitative) work alongside the model

---

## 2. Recommendation Systems
> 🟠 Tier 2 · _Tracker hint:_ Collaborative filtering (user-item matrix); content-based; hybrid; matrix factorization

### Definition
Recommenders rank items for each user.

- **Collaborative filtering (CF):** uses behaviour only. *User-based* (similar users liked it), *item-based* (similar items to what you liked). Similarity: cosine $\cos(a,b)=\frac{a\cdot b}{\|a\|\|b\|}$.
- **Content-based:** match item attributes (genre, category, text embeddings) to a user profile.
- **Matrix factorization:** approximate the user-item matrix $R\approx UV^T$ with latent factors; predicted rating $\hat r_{ui}=p_u\cdot q_i$ (+ biases), learned by ALS/SGD.
- **Hybrid / deep two-tower models:** combine both, handle cold start.
- **Pipeline:** candidate generation → ranking → re-ranking (diversity, business rules).

Problems: **cold start** (new users/items), sparsity, popularity bias, feedback loops, filter bubbles. Metrics offline: precision@k, recall@k, NDCG, MAP; online: CTR, conversion, watch time, retention, via A/B tests.

### Example
User A rated items (5, 3, 0), User B (4, 3, 1). Cosine = (5×4 + 3×3 + 0×1) / (√34 × √26) = 29 / (5.83 × 5.10) = 29/29.73 = **0.975**, so very similar; item 3 liked by B (1) is a weak signal, but what A has not seen and B rated high would be recommended to A.

### In the news
See news box. High-volume Indian consumer platforms (payments, food, e-commerce) rely on such ranking and risk models operating in real time; the UPI scale figures show the data volume available for training.

### Interview angle
> [!question] How it is asked
> "How would you design recommendations for a food delivery app?" or "How do you solve cold start?"

> [!tip] Strong answer includes
> - CF vs content-based vs hybrid, with trade-offs
> - Cold-start strategies (popularity, onboarding, content features)
> - Success metric and A/B testing, plus guardrails (diversity, latency)
> - Two-stage architecture (retrieval then ranking)
> - Product risks: filter bubble, fairness, explainability

---

## 3. A/B Test Analysis with Stats
> 🟠 Tier 2 · _Tracker hint:_ Two-proportion z-test; sample size; minimum detectable effect; avoid peeking

### Definition
An A/B test randomly assigns users to control (A) and variant (B) to measure causal impact.

**Two-proportion z-test:** with conversion $\hat p_A,\hat p_B$ and pooled $\hat p=\frac{x_A+x_B}{n_A+n_B}$:
$$z=\frac{\hat p_B-\hat p_A}{\sqrt{\hat p(1-\hat p)\left(\frac1{n_A}+\frac1{n_B}\right)}}$$
Two-sided 5% significance: reject $H_0$ if $|z|>1.96$.

**Sample size per arm** (power 80%, α=5%): 
$$n\approx\frac{2\,(1.96+0.84)^2\,p(1-p)}{\delta^2}\approx\frac{15.7\,p(1-p)}{\delta^2}$$
where $\delta$ is the **minimum detectable effect (MDE)** in absolute terms.

Pitfalls: **peeking** (checking early and stopping at the first p<0.05 inflates false positives; use fixed horizon, sequential tests or alpha-spending), multiple metrics/variants (Bonferroni), novelty effect, sample-ratio mismatch, network interference, running for full weekly cycles. Report confidence interval and practical significance, not just p-value.

### Example
Baseline conversion p = 10%, want to detect +1 pp (δ = 0.01). n ≈ 15.7 × 0.10 × 0.90 / 0.0001 = 15.7 × 0.09 / 0.0001 = **14,130 per arm**. Test result: A 1,000/10,000 = 10%, B 1,100/10,000 = 11%. Pooled p = 0.105; SE = √(0.105×0.895×(2/10,000)) = √(0.0000188) ≈ 0.00434; z = 0.01/0.00434 ≈ **2.30**, p ≈ 0.02, significant. (Note that n=10,000 is below 14,130, so the test was slightly underpowered for a 1 pp MDE; the result is significant but still verify.)

### In the news
See news box. Large platforms with tens of crores of daily events can detect tiny effects; at that scale statistical significance is easy, so practical significance and guardrails matter more.

### Interview angle
> [!question] How it is asked
> "We ran an A/B test and conversion went up 2%. Should we ship?" or "How long should we run this test?"

> [!tip] Strong answer includes
> - Hypothesis, primary metric, guardrail metrics, randomisation unit
> - Sample size from baseline, MDE, power, α; duration in full weeks
> - No peeking/or proper sequential method; multiple-testing caution
> - Statistical vs practical significance and cost to ship
> - Check for sample-ratio mismatch and segment effects

---

## 4. Personalization with ML
> 🟠 Tier 2 · _Tracker hint:_ Segment-of-one; contextual bandits; explore-exploit tradeoff

### Definition
Personalization tailors content, offers or ranking to each user ("segment of one"), using user history, context (time, device, location) and item features.

**Explore-exploit tradeoff:** *exploit* what looks best now, *explore* alternatives to learn. **Multi-armed bandits** balance this online:
- **ε-greedy:** with probability ε pick random.
- **UCB:** pick the arm with highest $\bar x_a+\sqrt{2\ln t/n_a}$.
- **Thompson sampling:** sample from each arm's posterior, pick the max.
- **Contextual bandits:** the best arm depends on context features $x$ (e.g., which banner to show this user now). Regret is minimised faster than classic A/B tests which waste traffic on losing variants.

Challenges: cold start, delayed rewards, off-policy evaluation, privacy (DPDP Act 2023 in India: consent and purpose limitation), filter bubbles, and avoiding creepiness.

### Example
Two banners: A with true CTR 5%, B 8%. A/B test at 50/50 for 10,000 users: 5,000 see A (250 clicks) and 5,000 see B (400 clicks) = 650 clicks. A bandit that shifts to ~90% B after learning: ≈ 1,000 on A (~50 clicks) + 9,000 on B (720 clicks) = **~770 clicks**, about 18% more, since less traffic is wasted on the loser.

### In the news
See news box. The consent and data-use limits on personalising financial offers matter more for payments apps given UPI's scale.

### Interview angle
> [!question] How it is asked
> "How would you personalise the home screen of our app?"

> [!tip] Strong answer includes
> - Level of personalisation: rules → segments → ML ranking → bandit
> - Explore-exploit explained plainly with an example
> - Metrics and holdout group measuring true incremental lift
> - Privacy/consent and cold start
> - Start simple; ML only when the value of personalisation is proven

---

## 5. NLP for Product
> 🟠 Tier 2 · _Tracker hint:_ Sentiment analysis on reviews; topic modeling on support tickets; intent classification for chatbots

### Definition
NLP converts text feedback into product insight.

- **Sentiment analysis:** classify reviews as positive/negative/neutral (lexicon, logistic regression on TF-IDF, or fine-tuned BERT). Aspect-based sentiment links sentiment to features ("battery: negative").
- **Topic modelling:** LDA or embedding clustering (BERTopic) to find themes in support tickets.
- **Intent classification and slot filling** for chatbots; **named-entity recognition** to extract order IDs.
- **LLMs** can summarise feedback and classify at scale with prompts; validate on a labelled sample.

TF-IDF: $w_{t,d}=tf_{t,d}\times\log\frac{N}{df_t}$. Metrics: F1, confusion matrix, inter-annotator agreement. Indian context: code-mixed text (Hinglish) and regional languages reduce accuracy; need multilingual models.

### Example
1,000 tickets: topic model finds 4 themes: delivery delay 38%, payment failure 27%, app crash 20%, refund 15%. A PM prioritises payment failure plus delays (65% of volume). If fixing delays removes half of its tickets, that cuts 190 tickets, i.e. **19% of total volume**.

### In the news
See news box. MuleHunter.AI shows regulators embracing pattern-detecting models; consumer apps similarly mine support text for fraud and failure signals.

### Interview angle
> [!question] How it is asked
> "We have 50,000 app reviews. How would you extract insights?"

> [!tip] Strong answer includes
> - Pipeline: clean → classify sentiment/topic → quantify and prioritise
> - Validation on a human-labelled sample
> - Link themes to metrics (churn, CSAT) and roadmap decisions
> - Language and code-mixing limitations

---

## 6. Search & Ranking
> 🟠 Tier 2 · _Tracker hint:_ Learning to Rank (LTR); BM25 for text search; neural ranking; click-through rate optimization

### Definition
Search = **retrieve** candidates, then **rank**.

- **BM25** (lexical): score $=\sum_{t\in q}IDF(t)\frac{f(t,d)(k_1+1)}{f(t,d)+k_1(1-b+b\frac{|d|}{avgdl})}$; typical $k_1\approx1.2$–2, $b=0.75$.
- **Semantic/dense retrieval:** embedding similarity (vector search) handles synonyms.
- **Learning to Rank:** pointwise, pairwise (RankNet), listwise (LambdaMART) models using features: text match, price, popularity, CTR, conversion, freshness, personalisation.
- **CTR optimisation:** model predicted click/conversion probability; blend with business value (margin, ads). Beware **position bias** (top results get clicks regardless of relevance); correct via randomisation or inverse propensity weighting.

Metrics: NDCG@k, MRR, precision@k; online: CTR, zero-result rate, conversion, time-to-first-click.

$$DCG@k=\sum_{i=1}^k\frac{2^{rel_i}-1}{\log_2(i+1)}$$

### Example
Results with relevance (3, 2, 0): DCG = (2³−1)/log₂2 + (2²−1)/log₂3 + 0 = 7/1 + 3/1.585 = 7 + 1.893 = **8.893**. Ideal order (3, 2, 0) is the same, so NDCG = 1. If shown as (2, 3, 0): DCG = 3/1 + 7/1.585 = 3 + 4.416 = 7.416; NDCG = 7.416/8.893 = **0.834**.

### In the news
See news box. For high-volume Indian marketplaces, ranking decisions affect millions of daily sessions; the product lens is to pair relevance gains with guardrail metrics.

### Interview angle
> [!question] How it is asked
> "Search conversion on our app is low. How do you improve it?" or "How would you rank products on a marketplace?"

> [!tip] Strong answer includes
> - Separate retrieval vs ranking; lexical + semantic hybrid
> - Metrics (NDCG, zero-result rate, conversion) and A/B tests
> - Features and position bias
> - Query understanding: spelling, synonyms, vernacular queries

---

## 7. Fraud Detection
> 🟠 Tier 2 · _Tracker hint:_ Supervised (labeled fraud data) or unsupervised (anomaly); imbalanced class handling critical

### Definition
Fraud models score each transaction/account for risk in milliseconds.

- **Supervised** (labelled chargebacks/confirmed fraud): logistic regression, gradient boosting.
- **Unsupervised/anomaly** (no labels or new patterns): Isolation Forest, autoencoders, graph methods (rings of linked accounts, device sharing).
- **Imbalance:** fraud may be 0.1% of data. Handle with class weights, under/over-sampling (SMOTE with caution), anomaly framing, and metrics like **precision, recall, PR-AUC**; accuracy is useless (99.9% by predicting "no fraud").
- **Decision layer:** score → thresholds → approve / step-up authentication / manual review / block. Cost matrix: false positive = lost customer and friction; false negative = fraud loss.
- **Adversarial drift:** fraudsters adapt, so retrain frequently and keep rules plus ML.

### Example
10 lakh transactions, 0.1% fraud = 1,000. Model flags 2,000; of those 700 are fraud. Precision = 700/2,000 = **35%**, recall = 700/1,000 = **70%**. Average fraud ₹5,000 prevented = ₹35 lakh; review cost ₹20 × 2,000 = ₹40,000. Net ≈ ₹34.6 lakh benefit.

### In the news
See news box. RBI's MuleHunter.AI (31 banks) and UPI's 66 crore daily transactions illustrate imbalanced, high-throughput fraud detection in India.

### Interview angle
> [!question] How it is asked
> "Design a fraud detection system for a UPI-like payments app."

> [!tip] Strong answer includes
> - Real-time scoring with rules + ML; latency budget
> - Imbalance handling and the right metrics
> - Threshold by cost; friction-based responses (step-up) instead of only blocking
> - Feedback loop, drift, graph features for mule networks
> - Customer experience and regulatory compliance

---

## 8. Customer Lifetime Value (CLV) Prediction
> 🟠 Tier 2 · _Tracker hint:_ Regression or survival analysis; Pareto/NBD model; BG/NBD for non-contractual

### Definition
**CLV** = present value of the margin a customer will generate.

**Simple formula (contractual):**
$$CLV=\sum_{t=1}^{T}\frac{m\cdot r^{t-1}}{(1+d)^{t}}\;\approx\;\frac{m}{1+d-r}\ (T\to\infty)$$
with margin $m$ per period (received at period end), retention rate $r$, discount rate $d$. Ignoring discounting, the common shortcut is $CLV=m\times\frac{1}{1-r}$.

**Non-contractual settings** (retail, e-commerce: you do not observe churn): **BG/NBD** (Beta-Geometric/NBD) models purchase counts while "alive" and dropout probability; **Pareto/NBD** is the continuous-dropout version. Inputs are just **frequency, recency, age (T)**. Add **Gamma-Gamma** for monetary value. ML alternative: regress future 12-month spend on RFM and behaviour features. **Survival analysis** (Kaplan-Meier, Cox) suits subscriptions.

Use: set acquisition budgets (**CAC < CLV/3** rule of thumb), segment VIPs, decide retention spend.

### Example
Customer margin ₹300 per year, retention 80%, ignoring discounting: CLV = 300/(1−0.8) = **₹1,500**. With discount 10% using $m/(1+d-r)$ = 300/(1.1−0.8) = **₹1,000**. If CAC is ₹400, CLV/CAC = 2.5 (below the 3× rule, so improve retention or margin).

### In the news
See news box. In payments, lifetime value is driven by repeat usage; UPI's ~66 crore daily transactions show how heavily frequency drives monetisation for apps.

### Interview angle
> [!question] How it is asked
> "How would you calculate CLV, and how would you use it for marketing spend?"

> [!tip] Strong answer includes
> - Formula with margin, retention, discount; contractual vs non-contractual
> - BG/NBD + Gamma-Gamma named with required inputs (recency, frequency, T, monetary)
> - Use for CAC limits and segment-specific offers
> - Cohort validation, and caution about predicted vs realised values

---

## 9. ⭐ Advanced: Uplift Modelling and Causal Inference for PMs
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Standard models predict *who will churn or buy*; **uplift models** predict *who will change behaviour because of our action*. Customer types: persuadables (target), sure things (waste), lost causes (waste), sleeping dogs (harm).

$$Uplift(x)=P(Y=1\mid T=1,x)-P(Y=1\mid T=0,x)$$

Methods: two-model approach, S-/T-/X-learners, uplift trees; requires randomised data. When A/B is impossible: **difference-in-differences**, regression discontinuity, matching, synthetic control. **CUPED** reduces A/B variance by using pre-experiment covariates: $Y' = Y-\theta(X-\bar X)$.

### Example
Offer sent to 1,000 treated and 1,000 control users. Purchase rates: treated 12%, control 9%. Uplift = 3 pp; 30 incremental purchases. If margin per purchase is ₹500 → ₹15,000 incremental margin; offer cost ₹10 × 1,000 = ₹10,000; net **₹5,000**. A targeted send to only high-uplift users would cut cost.

### In the news
See news box. Fraud and risk teams also use "who should we step-up" decisions where the intervention changes outcomes, not just predictions.

### Interview angle
> [!question] How it is asked
> "How do you know your retention campaign actually worked?"

> [!tip] Strong answer includes
> - Control/holdout group for incrementality
> - Correlation vs causation; selection bias
> - Uplift vs propensity targeting
> - Cost-benefit with incremental margin

---

## 10. ⭐ Advanced: Experiment Metrics, Guardrails and Metric Design
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Good experimentation needs good metrics.

- **North Star** (long-term value) → **driver metrics** (activation, frequency) → **guardrails** (latency, crash rate, refunds, complaints) → **counter-metrics** (to catch gaming).
- **Ratio metrics** (CTR = clicks/impressions) need the **delta method** or bootstrap for variance because numerator and denominator are correlated.
- **Heterogeneous effects:** check by segment but correct for multiple comparisons.
- **Long-term effects:** use holdouts and surrogates; short-term lifts can hurt retention.
- **Decision rule:** pre-register hypothesis, MDE, duration and ship/no-ship thresholds.

### Example
New checkout lifts conversion by 2% relative (5.0% → 5.1%) but payment-failure rate rises from 1.0% to 1.5%. On 1,00,000 sessions that is about +100 orders (5,000 → 5,100) but failed payments rise from 1,000 to 1,500 (+500). The guardrail breach (+50% relative failure rate) triggers investigation instead of an automatic ship.

### In the news
See news box. Fraud tools balance fraud caught against false declines (a guardrail), the same two-sided metric logic.

### Interview angle
> [!question] How it is asked
> "Which metrics would you track for a new feature, and what would make you roll it back?"

> [!tip] Strong answer includes
> - Primary, secondary, guardrail and counter-metrics
> - Pre-defined success/rollback thresholds
> - Segment cuts and long-term holdout
> - Statistical care for ratio metrics

---
## 🔗 Go deeper: expansion notes
- [[214 Causal Inference & Experimentation Beyond A-B Tests|Causal Inference & Experimentation Beyond A-B Tests]]
- [[219 NLP, Embeddings & LLM Applications for Analysts|NLP, Embeddings & LLM Applications for Analysts]]
