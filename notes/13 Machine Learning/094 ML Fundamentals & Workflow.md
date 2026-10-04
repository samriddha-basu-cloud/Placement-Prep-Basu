---
tags: [machine-learning, tier1]
area: Machine Learning
topic: "ML Fundamentals & Workflow"
tier: Tier 1
roles: PM / Operations
status: complete
subtopics: 14
---
# ML Fundamentals & Workflow

[[_Index - Machine Learning|Machine Learning]] · [[095 Regression Algorithms]] ➡

> **Area:** Machine Learning · **Priority:** 🔴 Tier 1 · **Target roles:** PM / Operations

## Sub-topics in this note
1. [[#1. What is Machine Learning?]]
2. [[#2. Supervised Learning]]
3. [[#3. Unsupervised Learning]]
4. [[#4. Reinforcement Learning]]
5. [[#5. ML Workflow (CRISP-DM)]]
6. [[#6. Bias-Variance Tradeoff]]
7. [[#7. Train-Validation-Test Split]]
8. [[#8. Cross Validation (k-fold)]]
9. [[#9. Feature Engineering]]
10. [[#10. Data Preprocessing]]
11. [[#11. Overfitting Prevention]]
12. [[#12. ML Evaluation Metrics Overview]]
13. [[#13. ⭐ Advanced: Data Leakage and Time-Aware Validation]]
14. [[#14. ⭐ Advanced: Framing ML Problems for the Business (PM lens)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): ML goes mainstream in business, and in Indian banking
> **Stanford AI Index 2025 (April 2025).** 78% of organisations reported using AI in 2024, up from 55% a year earlier. The inference cost of a system performing at GPT-3.5 level fell over 280-fold between Nov 2022 and Oct 2024. US private AI investment in 2024 was $109.1 bn (about 12x China's $9.3 bn). ([Business Wire summary of the Stanford HAI report](https://www.businesswire.com/news/home/20250407539812/en/Stanford-HAIs-2025-AI-Index-Reveals-Record-Growth-in-AI-Capabilities-Investment-and-Regulation))
>
> **RBI's MuleHunter.AI (Dec 2024 to Dec 2025).** The Reserve Bank Innovation Hub announced an ML-based tool in Dec 2024 to spot "mule" accounts used to move illicit funds, built after studying 19 behaviour patterns; it was piloted with two public sector banks and, per an RTI reply reported in Dec 2025, 23 banks had implemented it. RBI declined to disclose how many mule accounts were found. ([Business Standard](https://www.business-standard.com/finance/personal-finance/explained-rbi-has-a-new-ai-tool-mulehunter-ai-to-reduce-digital-frauds-124120900250_1.html), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. What is Machine Learning?
> 🔴 Tier 1 · _Tracker hint:_ System learns from data without explicit programming; pattern recognition; 3 types

### Definition
**Machine learning (ML)** is a branch of AI in which a system improves its performance on a task from data rather than from hand-written rules. Tom Mitchell's formal definition: a program learns from experience *E* with respect to task *T* and performance measure *P* if its performance on *T*, measured by *P*, improves with *E*.

Traditional programming: **rules + data → answers**. ML: **data + answers → rules (the model)**, which are then applied to new data.

| Type | Data | Goal | Typical use |
|---|---|---|---|
| Supervised | Labelled (X, y) | Predict y for new X | Demand forecast, churn, credit default |
| Unsupervised | Unlabelled X | Find structure | Customer segments, anomalies |
| Reinforcement | Rewards from an environment | Learn a policy | Robotics, dynamic pricing, routing |

ML is not magic: it finds statistical patterns, so it is only as good as the data and only valid where the future resembles the past.

### Example
A rule-based spam filter says "if subject contains 'lottery' then spam". An ML filter is shown 100,000 emails labelled spam/not-spam and learns which words, senders and patterns predict spam, including patterns no human wrote down.

### In the news
See news box. The Stanford numbers show ML is now routine business infrastructure (78% of organisations using AI), so interviewers expect candidates to speak about it fluently even for non-technical roles.

### Interview angle
> [!question] How it is asked
> "Explain machine learning to a non-technical manager." or "How is ML different from traditional programming or from statistics?"

> [!tip] Strong answer includes
> - The rules-versus-data inversion in one sentence
> - The three types with one business example each
> - A caveat: needs enough good data, can fail when the world changes
> - A concrete operations example such as demand forecasting or ETA prediction

---

## 2. Supervised Learning
> 🔴 Tier 1 · _Tracker hint:_ Input-output pairs; learn mapping f(X)=Y; classification, regression

### Definition
In **supervised learning** each training example has inputs (features) $X$ and a known label $y$. The algorithm learns a function $\hat y = f(X)$ that minimises a **loss** on the training data and generalises to unseen data.

- **Regression:** $y$ is continuous (sales, price, delivery time). Loss: squared error.
- **Classification:** $y$ is a category (churn / no churn). Loss: log-loss (cross-entropy).

$$\min_f \; \frac{1}{n}\sum_{i=1}^{n} L\big(y_i, f(x_i)\big) + \lambda\,\Omega(f)$$

where $\Omega$ is a regulariser that penalises complexity. Common algorithms: linear and logistic regression, trees, random forests, gradient boosting, SVM, neural networks. The main cost is **labels**: someone must collect and verify them.

### Example
A quick-commerce firm has 2 years of history: features (day, weather, festival flag, price) and label (units sold). Fitting a gradient-boosted regressor to predict next-day units per SKU is supervised regression. Predicting whether an order will be cancelled (yes/no) is supervised classification.

### In the news
See news box. MuleHunter.AI-type fraud tools are supervised problems in spirit: past accounts labelled "mule" or "genuine" teach the model which behaviour patterns matter (the sources describe ML on transaction data but do not state the exact algorithm).

### Interview angle
> [!question] How it is asked
> "What is supervised learning? Give a business example of regression and classification."

> [!tip] Strong answer includes
> - Labelled data and mapping X to y
> - Regression versus classification and the matching metric
> - The label cost and label quality issue
> - One example from operations, e.g. ETA (regression) and late-delivery flag (classification)

---

## 3. Unsupervised Learning
> 🔴 Tier 1 · _Tracker hint:_ No labels; find hidden structure; clustering, dimensionality reduction, association rules

### Definition
**Unsupervised learning** works on data with no target variable; the algorithm discovers structure on its own.

| Family | Question answered | Methods |
|---|---|---|
| Clustering | Which records are similar? | K-Means, hierarchical, DBSCAN |
| Dimensionality reduction | Can I summarise many features by a few? | PCA, t-SNE, autoencoders |
| Association rules | What occurs together? | Apriori, FP-Growth |
| Anomaly detection | What is unusual? | Isolation Forest |

There is no single "correct" answer to score against, so evaluation is harder (silhouette score, business usefulness, stability). Output must be **interpreted and named by humans**. Details in [[097 Unsupervised Learning]].

### Example
A retailer clusters 2 million loyalty-card customers on spend, frequency and category mix and finds a "weekend bulk-buyer" group nobody had defined. Marketing then designs an offer for that group.

### In the news
See news box. Detecting unusual behaviour across accounts without relying only on fixed rules is the motivation the RBI gave for ML-based mule detection.

### Interview angle
> [!question] How it is asked
> "How would you segment customers when you have no labels?" or "Supervised vs unsupervised?"

> [!tip] Strong answer includes
> - No target variable; structure discovery
> - Name two families with an example each
> - How to validate: silhouette, stability, and business actionability
> - Admit that segments need human naming and action

---

## 4. Reinforcement Learning
> 🔴 Tier 1 · _Tracker hint:_ Agent learns from rewards/penalties; environment interaction; used in robotics, games

### Definition
In **reinforcement learning (RL)** an **agent** takes **actions** in an **environment**, observes a new **state** and receives a **reward**. It learns a **policy** $\pi(a\mid s)$ that maximises expected cumulative discounted reward:

$$G_t = \sum_{k=0}^{\infty} \gamma^k\, r_{t+k+1}, \quad 0\le\gamma<1$$

Key ideas: exploration versus exploitation, delayed reward, trial and error. Methods: Q-learning, policy gradients, deep RL. Unlike supervised learning there is no "right answer" per step, only a reward signal, so training needs a simulator or safe live experiments.

Operations uses: dynamic pricing, warehouse robot routing, inventory replenishment policies, ad bidding. Bandit algorithms (a simple RL case) drive A/B-style online experiments.

### Example
A warehouse robot gets +1 for each parcel delivered to the right bin and -0.01 per second of travel. After many simulated runs it learns shorter routes without anyone coding the routes. In pricing, the agent raises a price slightly, observes sales and profit (reward), and adjusts.

### In the news
See news box. The falling inference cost (280-fold) is part of why running many simulated or live decisions with learned policies is becoming economically viable.

### Interview angle
> [!question] How it is asked
> "What is reinforcement learning and where could it be used in a supply chain?"

> [!tip] Strong answer includes
> - Agent, environment, state, action, reward vocabulary
> - Exploration versus exploitation
> - A supply chain use: replenishment or routing
> - Limits: needs simulation, reward design is hard, risk in live use

---

## 5. ML Workflow (CRISP-DM)
> 🔴 Tier 1 · _Tracker hint:_ Business understanding → Data understanding → Preparation → Modeling → Evaluation → Deployment

### Definition
**CRISP-DM** (Cross-Industry Standard Process for Data Mining) is the standard lifecycle, and it is **iterative**, not linear:

1. **Business understanding:** define the decision, success metric and cost of errors.
2. **Data understanding:** collect, profile, find quality issues.
3. **Data preparation:** clean, join, engineer features (usually 60–80% of the effort).
4. **Modeling:** choose algorithms, tune.
5. **Evaluation:** check against the *business* goal, not just accuracy.
6. **Deployment:** integrate, monitor, retrain.

Modern practice extends step 6 into **MLOps** ([[098 Model Selection & Optimization]]). Many ML projects fail at steps 1 and 6, not at modelling.

### Example
Goal: reduce stock-outs at 500 pharmacies. Business: target fill rate 98%. Data: 3 years of sales, promotions, weather. Preparation: handle returns, new stores. Modeling: gradient boosting versus a seasonal baseline. Evaluation: weekly forecast error and simulated fill rate. Deployment: nightly batch forecast feeding the replenishment system, with drift alerts.

### In the news
See news box. MuleHunter.AI went through the full path: problem framing with banks (19 patterns), a two-bank pilot, then rollout to 23 banks by Dec 2025.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would run an ML project end to end." (very common for PM and consultant cases)

> [!tip] Strong answer includes
> - Starts from the business decision and metric, not the algorithm
> - All six phases, and that it loops back
> - Baseline model first, then complexity
> - Deployment and monitoring as part of "done"

---

## 6. Bias-Variance Tradeoff
> 🔴 Tier 1 · _Tracker hint:_ High bias = underfitting (too simple); High variance = overfitting (memorizes noise)

### Definition
Expected prediction error on new data decomposes as:

$$E[(y-\hat f(x))^2] = \underbrace{\text{Bias}^2}_{\text{wrong assumptions}} + \underbrace{\text{Variance}}_{\text{sensitivity to training sample}} + \underbrace{\sigma^2}_{\text{irreducible noise}}$$

| | High bias | High variance |
|---|---|---|
| Symptom | Train and test error both high | Train error low, test error high |
| Cause | Model too simple | Model too complex, too little data |
| Fix | More features, complex model | More data, regularise, simplify, ensemble |

Increasing complexity lowers bias but raises variance; the best model sits at the minimum of total test error. Learning curves help diagnose which side you are on ([[098 Model Selection & Optimization]]).

### Example
Predict house price from area. A straight line may give train RMSE 9 lakh and test RMSE 10 lakh (high bias). A degree-15 polynomial gives train RMSE 1 lakh and test RMSE 15 lakh (high variance, memorised noise). A degree-2 curve with 4 and 5 lakh is the sweet spot. (Illustrative numbers.)

### In the news
See news box. Cheaper inference and abundant data make high-capacity models easy to deploy, which makes disciplined validation against variance more, not less, important.

### Interview angle
> [!question] How it is asked
> "Explain bias-variance tradeoff." or "Your model has 99% train and 70% test accuracy. What is wrong?"

> [!tip] Strong answer includes
> - The two failure modes with train/test error symptoms
> - The decomposition (bias squared + variance + noise)
> - At least three remedies for each side
> - Mention of validation or cross-validation to detect it

---

## 7. Train-Validation-Test Split
> 🔴 Tier 1 · _Tracker hint:_ 80-10-10 or 70-15-15; train=fit, val=tune, test=evaluate; never touch test early

### Definition
Data is split into three parts with different jobs:

- **Training set:** model parameters are fitted here.
- **Validation set:** compare models and tune hyperparameters.
- **Test set:** one final, unbiased estimate of real-world performance; used **once**.

Typical ratios 70-15-15 or 80-10-10; with huge data a 1% test set can suffice. Rules: split **before** any preprocessing that learns from data (scalers, imputers) to avoid leakage; use **stratified** splits for imbalanced classes; for time-ordered data split **chronologically**, never randomly.

```python
from sklearn.model_selection import train_test_split
X_tmp, X_test, y_tmp, y_test = train_test_split(X, y, test_size=0.15, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_tmp, y_tmp, test_size=0.1765, stratify=y_tmp, random_state=42)
```
(0.1765 of the remaining 85% is about 15% of the total.)

### Example
10,000 orders, 70-15-15: 7,000 train, 1,500 validation, 1,500 test. For 24 months of sales, train on months 1–18, validate on 19–21, test on 22–24.

### In the news
See news box. With 78% of firms using AI, a clean held-out test set is what separates a credible pilot result from an inflated one.

### Interview angle
> [!question] How it is asked
> "Why do we need a validation set as well as a test set?"

> [!tip] Strong answer includes
> - Distinct roles: fit, tune, final evaluation
> - Test set touched once, otherwise it becomes another tuning set
> - Stratify for imbalance, chronological split for time series
> - Split before preprocessing

---

## 8. Cross Validation (k-fold)
> 🔴 Tier 1 · _Tracker hint:_ Split data into k folds; train on k-1, test on 1; repeat k times; average score

### Definition
**k-fold cross-validation** splits the training data into $k$ equal folds. Each fold serves once as the validation set while the model trains on the other $k-1$ folds. The $k$ scores are averaged:

$$CV = \frac{1}{k}\sum_{i=1}^{k} \text{score}_i$$

and the standard deviation shows stability. Typical $k=5$ or 10. Variants: **stratified** k-fold (keeps class ratio), **leave-one-out** (k = n, expensive), **TimeSeriesSplit** (expanding window, no future in train), **group k-fold** (all rows of one customer in one fold).

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print(scores.mean(), scores.std())
```

Trade-off: more folds means less bias in the estimate but more compute.

### Example
5-fold scores: 0.82, 0.80, 0.85, 0.78, 0.80. Sum = 4.05, mean = 4.05/5 = **0.81**. Deviations from the mean are small, so the model is stable.

### In the news
See news box. When deployment spreads quickly (23 banks using MuleHunter.AI), estimates must hold across different banks, which is why grouped or per-bank validation matters.

### Interview angle
> [!question] How it is asked
> "What is k-fold cross-validation and when would you not use it?"

> [!tip] Strong answer includes
> - The procedure and the averaged score plus spread
> - Why better than a single split on small data
> - Stratified, grouped and time-series variants
> - Not for ordered data with plain random folds, and compute cost

---

## 9. Feature Engineering
> 🔴 Tier 1 · _Tracker hint:_ Creating/transforming features; one-hot encoding, scaling, imputation, interaction terms

### Definition
**Feature engineering** is turning raw data into inputs that expose the signal to the model. It often improves results more than switching algorithms.

- **Encoding:** one-hot for nominal categories, ordinal/label for ordered ones, target encoding for high cardinality (with leakage care).
- **Scaling:** standardise or min-max for distance- and gradient-based models.
- **Imputation:** mean/median/mode, or a missing-indicator flag.
- **Transformations:** log of skewed values, binning, polynomial terms.
- **Interactions:** price × promo flag, distance / speed.
- **Date features:** day of week, month, festival, lag and rolling means.
- **Domain features:** days since last purchase, order value / items.

Tree models need less scaling but still benefit from good derived features.

### Example
From raw timestamp and pincode a delivery-time model gets: hour, is_weekend, is_festival, distance_km, rolling 7-day average delay for the pincode. A single "rolling average delay" feature often outperforms adding five more raw columns.

### In the news
See news box. MuleHunter.AI's design rested on engineering 19 behavioural patterns of mule accounts from raw transaction data, as the Business Standard explainer describes it.

### Interview angle
> [!question] How it is asked
> "What features would you build to predict late deliveries / customer churn?"

> [!tip] Strong answer includes
> - Features grouped: customer, product, time, location, behaviour
> - Lag and rolling features for time series
> - Encoding and scaling choices linked to the model
> - A warning about leakage (features unavailable at prediction time)

---

## 10. Data Preprocessing
> 🔴 Tier 1 · _Tracker hint:_ Handle missing values, outliers, skewness; StandardScaler, MinMaxScaler; label encoding

### Definition
Preprocessing prepares raw data for modelling.

- **Missing values:** drop (if few and random), impute (median for skewed), model-based imputation, add an indicator.
- **Outliers:** detect by IQR rule (outside $Q_1-1.5\,IQR$, $Q_3+1.5\,IQR$) or z-score; cap (winsorise), transform or keep if genuine.
- **Skewness:** log or Box-Cox transform.
- **Scaling:** $z=\dfrac{x-\mu}{\sigma}$ (StandardScaler); $x'=\dfrac{x-x_{min}}{x_{max}-x_{min}}$ (MinMaxScaler).
- **Encoding:** LabelEncoder is for targets or ordinal; one-hot for nominal features.

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)       # fit on train only
X_train_s, X_test_s = scaler.transform(X_train), scaler.transform(X_test)
```

### Example
Values 10, 20, 30, 40, 50: mean 30, population sd = $\sqrt{(400+100+0+100+400)/5}=\sqrt{200}=14.14$. The z-score of 50 is $20/14.14=1.41$. Min-max of 20 is $(20-10)/(50-10)=0.25$.

### In the news
See news box. Fraud and transaction data is messy and heavily skewed; RBI's push to standardise how banks use the tool depends on consistent data preparation.

### Interview angle
> [!question] How it is asked
> "How would you handle missing values and outliers in this dataset?"

> [!tip] Strong answer includes
> - Understand why data is missing (random or informative) before choosing a fix
> - Outlier: error versus genuine rare event
> - Fit scalers on train only
> - Which models need scaling (KNN, SVM, NN, regularised linear) and which do not (trees)

---

## 11. Overfitting Prevention
> 🔴 Tier 1 · _Tracker hint:_ Regularization (L1/L2), more data, simpler model, dropout (neural nets), cross-validation

### Definition
**Overfitting** is when a model fits noise in the training data and fails on new data (high variance). Remedies:

| Lever | How it helps |
|---|---|
| More / better data, augmentation | Noise averages out |
| Simpler model, fewer features | Less capacity to memorise |
| Regularisation L1/L2 | Penalises large coefficients |
| Early stopping | Stops training when validation loss rises |
| Dropout (neural nets) | Randomly drops units, prevents co-adaptation |
| Pruning, max_depth, min_samples_leaf (trees) | Limits tree growth |
| Ensembling (bagging) | Averages out variance |
| Cross-validation | Detects it early |

Regularised loss: $L + \lambda\sum|\beta_j|$ (L1) or $L+\lambda\sum\beta_j^2$ (L2).

### Example
A churn tree of unlimited depth scores 100% on train and 68% on test. Setting `max_depth=5` and `min_samples_leaf=50` gives 79% train and 76% test: lower training score, better real performance. (Illustrative.)

### In the news
See news box. Because model access is getting cheap (280-fold lower inference cost), the scarce skill is not building a model but proving it will generalise.

### Interview angle
> [!question] How it is asked
> "Your model performs very well in training but poorly in production. What do you do?"

> [!tip] Strong answer includes
> - Diagnose: compare train and validation error, check leakage and distribution shift
> - A list of remedies matched to model type
> - Cross-validation and a clean test set
> - Mention monitoring after deployment

---

## 12. ML Evaluation Metrics Overview
> 🔴 Tier 1 · _Tracker hint:_ Regression: RMSE, MAE, R²; Classification: Accuracy, Precision, Recall, F1, AUC-ROC

### Definition
**Regression:** MAE $=\frac1n\sum|y-\hat y|$; MSE $=\frac1n\sum(y-\hat y)^2$; RMSE $=\sqrt{MSE}$; $R^2=1-\frac{SS_{res}}{SS_{tot}}$.

**Classification** (from the confusion matrix): Accuracy $=\frac{TP+TN}{N}$; Precision $=\frac{TP}{TP+FP}$; Recall $=\frac{TP}{TP+FN}$; $F_1=\frac{2PR}{P+R}$; AUC-ROC = probability a random positive is scored above a random negative.

Choose by **cost of errors**: fraud (miss is costly) means recall; spam folder (false alarm is costly) means precision; imbalanced data means F1, PR-AUC, not accuracy. Details: [[095 Regression Algorithms]] and [[096 Classification Algorithms]].

### Example
Actual demand 100, 120, 80, 140; forecast 110, 115, 90, 100. Errors: 10, -5, 10, -40. MAE = (10+5+10+40)/4 = **16.25**. MSE = (100+25+100+1600)/4 = 456.25, RMSE = **21.36**. RMSE is higher because the single 40-unit miss is penalised more.

### In the news
See news box. For mule-account detection, RBI cited false positives of rule-based systems as the problem, which is a precision issue; missed mules are a recall issue.

### Interview angle
> [!question] How it is asked
> "Which metric would you use for this problem and why?"

> [!tip] Strong answer includes
> - Ties the metric to the cost of each error type
> - Distinguishes regression and classification metrics
> - Warns that accuracy misleads with imbalance
> - Mentions comparing against a naive baseline

---

## 13. ⭐ Advanced: Data Leakage and Time-Aware Validation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Data leakage** is when information unavailable at prediction time slips into training, giving great validation scores and a failed deployment.

- **Target leakage:** a feature that is a consequence of the label (e.g. "refund issued" when predicting cancellation).
- **Train-test contamination:** fitting scalers or imputers on the full data, or duplicates across splits.
- **Temporal leakage:** random splits on time series, so the model "sees" the future.

Defences: split first, wrap preprocessing in a `Pipeline`, use `TimeSeriesSplit` or a forward-chaining split, audit each feature with "would I know this at prediction time?", and be suspicious of near-perfect scores.

### Example
A model predicting whether a shipment will be delayed uses the feature "actual_delivery_date minus promised_date". It scores AUC 0.99 offline, but that feature only exists after delivery. In production the AUC falls to 0.7. Removing it is the fix.

### In the news
Not a single dated headline; as ML spreads to 78% of organisations (see news box), leakage is one of the most common reasons pilots look better than production.

### Interview angle
> [!question] How it is asked
> "Your model has 98% accuracy in testing. Are you happy? What could be wrong?"

> [!tip] Strong answer includes
> - Suspicion first: too good to be true
> - Names target, contamination and temporal leakage
> - Checks per feature for availability at prediction time
> - Remedy: pipeline, time-based split, holdout from the future

---

## 14. ⭐ Advanced: Framing ML Problems for the Business (PM lens)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Product and consulting interviews test whether you can decide **if and how** to use ML.

1. **Decision:** what action will change because of the prediction?
2. **Baseline:** rules or simple average; ML must beat it by enough to justify cost.
3. **Metric hierarchy:** business KPI (fill rate, revenue) → model metric (RMSE, recall) → guardrails (fairness, latency).
4. **Error costs:** cost-matrix of false positive versus false negative.
5. **Data readiness:** volume, labels, history, privacy.
6. **Value:** $\text{Expected value} = (\text{benefit per correct action} \times TP) - (\text{cost per wrong action} \times FP) - \text{running cost}$.
7. **Human in the loop and monitoring.**

### Example
A model flags 1,000 orders a day as likely RTO (return-to-origin). Calling each flagged customer costs Rs 10. Precision is 40%, so 400 are truly risky; saving an RTO is worth Rs 150. Value = 400 x 150 - 1,000 x 10 = 60,000 - 10,000 = Rs 50,000/day before model running costs. If precision fell to 5%: 50 x 150 - 10,000 = -Rs 2,500, a loss.

### In the news
See news box: RBI's MuleHunter.AI was framed around a concrete problem (fraud via mule accounts) with a pilot before scale-up, the pattern interviewers want to hear.

### Interview angle
> [!question] How it is asked
> "A client wants to use AI to improve operations. How do you decide where to start?"

> [!tip] Strong answer includes
> - Starts with the decision and KPI, not the technology
> - Baseline and expected value calculation
> - Data readiness and pilot-then-scale plan
> - Risks: bias, drift, adoption by frontline staff

---
## 🔗 Go deeper: expansion notes
- [[218 Forecasting with ML & Foundation Models|Forecasting with ML & Foundation Models]]
- [[220 Responsible AI, Explainability & Model Governance|Responsible AI, Explainability & Model Governance]]
