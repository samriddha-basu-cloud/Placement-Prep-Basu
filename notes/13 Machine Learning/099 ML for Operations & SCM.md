---
tags: [machine-learning, tier1]
area: Machine Learning
topic: "ML for Operations & SCM"
tier: Tier 1
roles: Operations / PM
status: complete
subtopics: 12
---
# ML for Operations & SCM

⬅ [[098 Model Selection & Optimization]] · [[_Index - Machine Learning|Machine Learning]] · [[100 ML for Product Management]] ➡

> **Area:** Machine Learning · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / PM

## Sub-topics in this note
1. [[#1. Demand Forecasting with ML]]
2. [[#2. Predictive Maintenance]]
3. [[#3. Inventory Optimization with RL]]
4. [[#4. Supplier Risk Prediction]]
5. [[#5. Anomaly Detection in Supply Chain]]
6. [[#6. Price Optimization]]
7. [[#7. Route Optimization with ML]]
8. [[#8. NLP for Procurement]]
9. [[#9. Image Recognition in Warehouse]]
10. [[#10. Time Series with ML]]
11. [[#11. ⭐ Advanced: Forecast Value Added, Hierarchical Reconciliation and MLOps for Ops]]
12. [[#12. ⭐ Advanced: Prescriptive Analytics: Predict-then-Optimize]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Amazon's foundation forecasting model, and ML in Indian banking fraud control
> **Amazon forecasting model (11 Jun 2025).** Amazon announced a foundational AI forecasting model that predicts what customers will want, where and when, for hundreds of millions of products a day, using weather and holiday signals on top of sales history. Amazon reported a **10% improvement in long-term national forecasts for deal events and a 20% improvement in regional forecasts for millions of popular items**; it was already used in the US, Canada, Mexico and Brazil. ([About Amazon](https://www.aboutamazon.com/news/operations/amazon-ai-innovations-delivery-forecasting-robotics))
> 
> **RBI's MuleHunter.AI (2024–2026).** The Reserve Bank Innovation Hub built an AI/ML tool that spots "mule accounts" (accounts used to move fraud proceeds) by detecting unusual transaction patterns; a Sept 2026 industry write-up reports it deployed across **31 banks**. ([RMA India](https://rmaindia.org/mulehunter-ai-rbis-ai-fraud-detection-system-now-live-across-31-banks/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Demand Forecasting with ML
> 🔴 Tier 1 · _Tracker hint:_ XGBoost on lag features, rolling stats, calendar features; vs ARIMA; probabilistic forecast

### Definition
Classical statistical models (moving average, exponential smoothing, ARIMA) fit **one series at a time**. ML forecasting instead treats forecasting as **supervised regression on a feature table**, so one model can learn across thousands of SKU-store series and absorb external drivers.

Typical features per row (SKU, store, day *t*):
- **Lag features:** sales at $t-1, t-7, t-14, t-364.
- **Rolling statistics:** 7/28-day mean, std, min, max (computed only from past data).
- **Calendar:** day of week, month, festival flags (Diwali, Eid), payday.
- **Exogenous:** price, promotion, weather, competitor price, stock-out flag.

Models: gradient boosting (XGBoost, LightGBM) is the workhorse; deep models (DeepAR, N-BEATS, Temporal Fusion Transformer) for large panels.

**ML vs ARIMA:** ARIMA is strong for a single stable series with few data; ML wins with many related series, promotions, and cold-start via features. Always compare to a naive/seasonal-naive baseline.

**Probabilistic forecast:** instead of one number, predict quantiles (P10/P50/P90) via quantile loss $L_\tau = \max(\tau e, (\tau-1)e)$, so safety stock can be set from the P90 rather than an assumed normal.

Metrics: MAPE, WAPE $=\sum|A-F|/\sum A$, bias $=\sum(F-A)/\sum A$, pinball loss. Validate with **time-based splits** (never random).

```python
import lightgbm as lgb
m = lgb.LGBMRegressor(objective="quantile", alpha=0.9, n_estimators=400)
m.fit(X_train, y_train)          # X has lag/rolling/calendar columns
p90 = m.predict(X_test)
```

### Example
A kirana-focused FMCG distributor forecasts weekly units of one SKU. Last 4 weeks: 120, 130, 110, 140. Simple 4-week average = (120+130+110+140)/4 = **125**. An ML model also sees "Diwali in 2 weeks" and "promo ON" and predicts 170. If actuals are 168, MAPE for ML = |168−170|/168 ≈ **1.2%** vs 25.6% for the moving average (|168−125|/168).

### In the news
See news box. Amazon's 20% regional-forecast gain came from adding weather/holiday/regional signals, which is the feature-engineering idea in this sub-topic at scale.

### Interview angle
> [!question] How it is asked
> "How would you forecast demand for 10,000 SKUs across 500 stores?" or "ARIMA vs XGBoost, which and why?"

> [!tip] Strong answer includes
> - Baseline first (seasonal naive), then ML with lag/rolling/calendar/price/promo features
> - Time-series cross-validation and leakage avoidance (no future info in rolling features)
> - WAPE/bias as business metrics, not just RMSE
> - Probabilistic output feeding safety stock and service level
> - Hierarchical forecasting and intermittent demand as known limits

---

## 2. Predictive Maintenance
> 🔴 Tier 1 · _Tracker hint:_ Sensor data (vibration, temp) → binary classification (fail/no-fail); MTBF prediction

### Definition
Use sensor and log data to predict equipment failure **before** it happens, moving from reactive ("fix when broken") and preventive ("fix every N hours") to **condition-based/predictive** maintenance.

**Framing options**
- **Classification:** will the machine fail in the next *k* days? (label = 1 if failure within horizon).
- **Regression:** Remaining Useful Life (RUL).
- **Anomaly detection** when failures are rare/unlabelled.

Features: vibration RMS, FFT peaks, temperature, current, pressure, operating hours, rolling means/slopes over windows. **Class imbalance** is the norm (failures <1–2%), so use precision/recall, PR-AUC, class weights; accuracy is misleading.

**Key reliability formulas**
$$MTBF=\frac{\text{operating time}}{\text{number of failures}},\qquad Availability=\frac{MTBF}{MTBF+MTTR}$$

Business trade-off: a false alarm costs an unnecessary stoppage; a missed failure costs unplanned downtime. Choose the probability threshold by expected cost, not 0.5.

### Example
A plant's press runs 2,000 h with 4 failures: MTBF = 2000/4 = **500 h**. With MTTR = 10 h, availability = 500/510 ≈ **98.0%**. If the model cuts failures to 3 (MTBF = 667 h), availability = 667/677 ≈ **98.5%**, plus fewer emergency repairs.

### In the news
See news box. The same "learn normal patterns, flag deviations" logic is used by RBI's MuleHunter.AI on transactions; in plants, it is applied to sensor streams.

### Interview angle
> [!question] How it is asked
> "A factory has frequent unplanned downtime. How can data science help?"

> [!tip] Strong answer includes
> - Maintenance maturity ladder: reactive → preventive → predictive
> - Labelling strategy (failure within next k days) and imbalance handling
> - Cost-based threshold (downtime cost vs false-alarm cost)
> - Pilot on critical assets, sensors/data readiness, change management with maintenance crew
> - KPIs: unplanned downtime %, OEE, MTBF, maintenance cost

---

## 3. Inventory Optimization with RL
> 🔴 Tier 1 · _Tracker hint:_ Reinforcement learning agent; state=inventory level; action=order qty; reward=minimize cost

### Definition
Reinforcement learning (RL) learns a **policy** by trial and reward, a natural fit for sequential replenishment decisions.

- **State:** on-hand + on-order inventory, recent demand, day of week, lead-time status.
- **Action:** order quantity (or order-up-to level).
- **Reward:** $-(\text{ordering} + \text{holding} + \text{stock-out penalty})$ each period.
- **Goal:** maximise expected discounted return $\sum \gamma^t r_t$.

Algorithms: Q-learning/DQN for small discrete problems; PPO/actor-critic for continuous actions and many SKUs. Training happens in a **simulator** of demand and lead times (never on live stock).

Why use it: classical $(s,S)$ or newsvendor policies are optimal only under simple assumptions (stationary demand, one echelon). RL helps with multi-echelon networks, non-stationary demand, perishability, and complex costs. Weaknesses: sample hungry, needs a trustworthy simulator, harder to explain; so benchmark against $(s,S)$ and deploy as a recommendation first.

Bellman update (tabular): $Q(s,a)\leftarrow Q(s,a)+\alpha\,[r+\gamma\max_{a'}Q(s',a')-Q(s,a)]$.

### Example
Single item, holding cost ₹2/unit/period, stock-out cost ₹10/unit, fixed order cost ₹50. State: stock 5; demand turns out 8. Action A (no order): shortage 3 × 10 = ₹30, reward = **−30**. Action B (order 4, assuming it arrives in time): stock 9 − demand 8 = 1 left, holding ₹2 + order ₹50 = ₹52, reward = **−52**. Here not ordering is cheaper for this single draw; across many simulated episodes with higher demand, the agent learns when a fixed order cost is worth paying. That is exactly the (s,S)-like trade-off RL discovers from rewards.

### In the news
See news box. Amazon's forecast model supplies the demand input; RL/optimisation policies then decide how much to stock against that forecast.

### Interview angle
> [!question] How it is asked
> "Could RL replace our reorder-point rules? When would you use it?"

> [!tip] Strong answer includes
> - Clear MDP framing (state, action, reward)
> - Why a simulator is needed and the sim-to-real gap
> - Benchmark vs $(s,S)$/newsvendor; start where classical policies are weak (multi-echelon, perishable)
> - Safe deployment: guardrails, human override, shadow mode
> - Honest limits: explainability and data requirements

---

## 4. Supplier Risk Prediction
> 🔴 Tier 1 · _Tracker hint:_ Features: financial ratios, geo-risk, delivery history; Logistic Regression/XGBoost

### Definition
Predict the probability that a supplier will fail (late delivery, quality escape, insolvency) using a supervised model.

**Features:** financial (current ratio, debt/equity, interest cover, Altman Z), operational (OTIF history, defect ppm, lead-time variance), geographic/geopolitical (country risk, port/flood exposure), concentration (share of spend, sole-source flag), news sentiment, ESG flags.

**Models:** logistic regression (interpretable, odds ratios, regulators like it) → gradient boosting (more accuracy). Output a **risk score** (0–100) and tier (High/Med/Low).

$$P(\text{fail})=\frac{1}{1+e^{-(\beta_0+\beta_1x_1+\dots)}}$$

Evaluation: AUC-ROC, recall at a chosen precision, **calibration** (does a 20% score mean ~20% fail?). Labels are scarce, so combine with expert-rated scores. Risk score × spend/criticality (Kraljic position) gives a **prioritised watchlist** and mitigation (dual source, safety stock, audit).

### Example
Logistic model: log-odds = −3 + 0.8×(late-delivery rate in tens of %) + 1.2×(sole-source flag). Supplier with 20% late (=2) and sole-source (=1): z = −3 + 1.6 + 1.2 = −0.2; P = 1/(1+e^{0.2}) = **45%** high risk. A supplier with 0% late, multi-sourced: z = −3, P = **4.7%**.

### In the news
See news box. MuleHunter.AI scores accounts by risky behaviour patterns, the same logic as scoring suppliers on delivery and financial behaviour; note that supplier-risk models also need tier-2/3 and geopolitical features, not only supplier financials (analytical point, not from the news box).

### Interview angle
> [!question] How it is asked
> "How would you build an early-warning system for supplier disruption?"

> [!tip] Strong answer includes
> - Feature families (financial, operational, geo, concentration)
> - Interpretable baseline, then boosting; calibration and thresholds
> - Combine score with criticality/spend to prioritise
> - Actions linked to score (audit, dual sourcing, buffer)
> - Data issues: few labelled failures, tier-n visibility

---

## 5. Anomaly Detection in Supply Chain
> 🔴 Tier 1 · _Tracker hint:_ Isolation Forest on order patterns; detect unusual demand spikes or fraud

### Definition
Anomaly detection finds points that deviate from normal behaviour, usually **without labels**.

**Isolation Forest:** builds random trees that split features at random; anomalies are few and different so they get isolated in **fewer splits**. Anomaly score $s(x,n)=2^{-E[h(x)]/c(n)}$; scores near 1 are anomalous, near 0.5 or below are normal. Other methods: z-score/IQR, DBSCAN, Local Outlier Factor, autoencoders, STL-residual thresholds for time series.

Use cases: sudden order spikes (genuine demand vs error vs panic buying), duplicate/inflated invoices, ghost vendors, abnormal return patterns, sensor drift, shipment-route deviations.

```python
from sklearn.ensemble import IsolationForest
iso = IsolationForest(n_estimators=200, contamination=0.01, random_state=42)
df["flag"] = iso.fit_predict(df[["qty","unit_price","orders_per_day"]]) == -1
```

`contamination` is the assumed outlier share; tune with business review. Flags go to a human queue, not auto-blocked.

### Example
Daily orders for a distributor: mean 100, std 10. Order of 160 gives z = (160−100)/10 = **6**, far beyond 3, so flagged. Investigation shows a duplicate PO entry; blocking it saved ₹4.8 lakh of excess stock.

### In the news
See news box. MuleHunter.AI is anomaly detection on transaction patterns at national scale; procurement teams use the same idea on POs and invoices.

### Interview angle
> [!question] How it is asked
> "How would you detect fraud or errors in purchase orders with no labelled fraud data?"

> [!tip] Strong answer includes
> - Unsupervised approach (Isolation Forest/autoencoder), features chosen well
> - Handling seasonality so festivals are not flagged
> - Human-in-the-loop review and feedback to improve precision
> - Cost of false positives vs misses
> - Distinguish anomaly types: error, fraud, real demand shift

---

## 6. Price Optimization
> 🔴 Tier 1 · _Tracker hint:_ Regression on demand elasticity; A/B test price changes; dynamic pricing models

### Definition
Pricing analytics sets prices to maximise profit given how demand reacts.

**Price elasticity:** $E=\frac{\%\Delta Q}{\%\Delta P}$; estimated with a log-log regression $\ln Q=\alpha+\beta\ln P+\gamma X+\varepsilon$, where $\beta$ is the elasticity. $|E|>1$ means elastic (price cut raises revenue).

**Profit-max price** (constant elasticity): markup rule $P^*=\frac{c\,E}{1+E}$ (with $E<-1$). Example form: $P^*=c\cdot\frac{|E|}{|E|-1}$.

**Dynamic pricing:** prices updated by time, inventory, competitor or demand signals (airlines, ride-hailing, e-commerce). ML models (GBM, bandits) predict demand at candidate prices. Always **A/B test** price changes and watch for confounders (promotions, seasonality), cannibalisation and fairness/regulatory limits.

### Example
Unit cost ₹60, elasticity −3. Optimal price = 60 × 3/(3−1) = **₹90** (50% markup). If elasticity is −1.5: 60 × 1.5/0.5 = **₹180**. Lower elasticity means customers are less price-sensitive, so you price higher.

### In the news
See news box. Better regional demand forecasts (Amazon) are the input that lets dynamic pricing and markdown models react by location and event.

### Interview angle
> [!question] How it is asked
> "How would you decide whether to raise the price of our product by 10%?"

> [!tip] Strong answer includes
> - Elasticity concept and how to estimate it (regression, experiment)
> - Profit, not revenue, as the target; include cost and cannibalisation
> - Test design (geo/time split) and guardrails
> - Segment by customer/channel; competitor and brand effects

---

## 7. Route Optimization with ML
> 🔴 Tier 1 · _Tracker hint:_ Reinforcement learning for VRP; graph neural networks; Google OR-Tools

### Definition
The **Vehicle Routing Problem (VRP)**: given a depot, vehicles with capacity, and customers with demand (and time windows), choose routes minimising total distance/time/cost. It is NP-hard, so large instances use heuristics.

- **Exact/classical:** MILP, branch-and-cut for small cases.
- **Heuristics/metaheuristics:** savings algorithm, local search, tabu search, genetic algorithms. **Google OR-Tools** provides a production-grade routing solver.
- **ML-based:** RL policies and attention/GNN models learn to construct routes quickly (good for real-time re-routing); ML also **predicts travel times/ETAs** and service times that feed the optimiser. In practice, "ML predicts the inputs, OR optimises the routes" is the robust hybrid.

```python
from ortools.constraint_solver import pywrapcp, routing_enums_pb2
manager = pywrapcp.RoutingIndexManager(n_locations, n_vehicles, depot)
routing = pywrapcp.RoutingModel(manager)
# register transit callback + capacity dimension, then:
params = pywrapcp.DefaultRoutingSearchParameters()
params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
sol = routing.SolveWithParameters(params)
```

### Example
10 drops, 2 vans. Manual routes: 90 km and 80 km = 170 km. Optimised routes: 70 + 68 = 138 km. Saving = 32/170 = **18.8%**. At ₹12/km and 26 days, saving = 32 × 12 × 26 = **₹9,984/month**.

### In the news
See news box. Amazon's June 2025 announcement placed AI forecasting alongside delivery and robotics upgrades; forecasts decide where stock sits, which shortens routes.

### Interview angle
> [!question] How it is asked
> "How would you reduce last-mile delivery cost for an e-commerce hub?"

> [!tip] Strong answer includes
> - VRP definition with constraints (capacity, time windows)
> - Heuristic solver (OR-Tools) plus ML for ETA prediction
> - Batching, zoning, delivery-density levers, not just algorithms
> - KPIs: cost per drop, drops per route, on-time %, km per drop

---

## 8. NLP for Procurement
> 🔴 Tier 1 · _Tracker hint:_ Contract analysis; vendor review sentiment; RFQ classification using BERT

### Definition
Natural Language Processing turns unstructured procurement text (contracts, emails, RFQs, invoices, reviews) into data.

Tasks and methods:
- **Contract analysis:** clause extraction, obligation/risk flagging (named-entity recognition, question answering).
- **RFQ/spend classification:** map line items to UNSPSC/category taxonomy (text classification).
- **Vendor/news sentiment:** early risk signals from news and reviews.
- **Invoice/PO matching:** OCR plus entity extraction.

**BERT** is a pre-trained transformer encoder that is fine-tuned on a small labelled set; now large language models (LLMs) also do extraction via prompting. Metrics: precision/recall/F1 per class; human review for high-value clauses.

```python
from transformers import pipeline
clf = pipeline("zero-shot-classification")
clf("100 pcs M8 hex bolts, zinc coated", candidate_labels=["fasteners","packaging","electricals"])
```

### Example
A firm has 5,000 vendor contracts. Manual review at 45 min each = 3,750 hours. If NLP extracts clauses and humans verify at 10 min each = 833 hours, saving about **78%** of effort (2,917 h).

### In the news
See news box. Banks' MuleHunter.AI shows regulated industries accepting ML for text- and pattern-heavy compliance; procurement contract review is a similar low-risk-to-start use of NLP.

### Interview angle
> [!question] How it is asked
> "Where would you use AI in the procurement function?"

> [!tip] Strong answer includes
> - 2–3 concrete use cases (spend classification, contract risk, supplier news)
> - Human-in-the-loop for legal risk, data security/confidentiality
> - Pilot, metric (hours saved, leakage found), then scale
> - Mention of LLM vs fine-tuned BERT trade-off (cost, privacy, accuracy)

---

## 9. Image Recognition in Warehouse
> 🔴 Tier 1 · _Tracker hint:_ Defect detection (CNNs); barcode/QR scanning; shelf occupancy monitoring

### Definition
Computer vision uses **convolutional neural networks (CNNs)** and detection models (YOLO, Faster R-CNN) on camera feeds.

Use cases:
- **Defect/damage detection** at inbound and packing (classification or object detection).
- **Barcode/QR/label reading** and OCR on pallets and parcels.
- **Shelf/bin occupancy and slot utilisation**, planogram compliance in stores.
- **Safety:** PPE checks, forklift/people proximity.
- **Dimensioning and counting** boxes on pallets.

Pipeline: collect images → label → augment (flip, brightness) → fine-tune a pre-trained model (transfer learning) → deploy on edge device for latency. Metrics: precision, recall, mAP; the cost of a missed defect usually exceeds a false alarm. Lighting, occlusion and new SKUs cause drift, so retrain periodically.

### Example
Inspection of 10,000 parcels/day, true damage rate 2% = 200 damaged. Model recall 90%, precision 80%: catches 180, false alarms = 180/0.8 − 180 = 45. Missed = 20. Manual review of 225 flagged parcels instead of 10,000.

### In the news
See news box. Amazon's June 2025 announcement also covered a new agentic-AI team in Amazon Robotics to make robots (e.g. the Proteus mobile robot) understand natural-language commands, showing vision and AI moving deeper into warehouses.

### Interview angle
> [!question] How it is asked
> "How could a warehouse use AI to cut damages and errors?"

> [!tip] Strong answer includes
> - Specific vision use cases tied to a KPI (damage rate, pick accuracy)
> - Edge deployment, data labelling effort, drift
> - Cost-benefit: camera/hardware cost vs error savings
> - Precision/recall trade-off and human fallback

---

## 10. Time Series with ML
> 🔴 Tier 1 · _Tracker hint:_ Feature engineering from TS (lag, rolling mean, fourier terms); feed to XGBoost/LightGBM

### Definition
Convert a time series into a **tabular supervised problem**, then use tree models.

- **Lags:** `y.shift(k)`.
- **Rolling windows:** `y.shift(1).rolling(7).mean()` (shift first to avoid leakage).
- **Fourier terms** for seasonality with period $m$: $\sin(2\pi k t/m),\ \cos(2\pi k t/m)$, $k=1..K$.
- **Calendar and event flags**, trend index, price/promo.

Forecast horizon strategies: **recursive** (feed predictions back), **direct** (a model per horizon), or multi-output.

**Validation:** expanding/rolling-origin splits (`TimeSeriesSplit`); never shuffle. Trees cannot extrapolate trend, so de-trend/difference or model ratios to a baseline.

```python
import numpy as np, pandas as pd
df["lag7"] = df["y"].shift(7)
df["roll7"] = df["y"].shift(1).rolling(7).mean()
df["s1"] = np.sin(2*np.pi*df["dayofyear"]/365.25)
df["c1"] = np.cos(2*np.pi*df["dayofyear"]/365.25)
```

### Example
Sales (units): 100, 110, 120, 130, 140. For the row at t=5 (value 140): lag1 = 130, and the 3-period rolling mean of the three previous values (110, 120, 130) = **120**. A tree model cannot predict above its training max (140) without trend handling, so add a differenced target (y_t − y_{t-1} = 10).

### In the news
See news box. Amazon's model uses weather and holiday signals as extra inputs; Fourier/calendar/exogenous features are the standard way to encode them.

### Interview angle
> [!question] How it is asked
> "How do you prepare time-series data for XGBoost? What can go wrong?"

> [!tip] Strong answer includes
> - Lags, rolling stats (shifted), Fourier/calendar features
> - Time-based validation and leakage avoidance
> - Trees' inability to extrapolate trend, and the fix
> - Direct vs recursive multi-step forecasting

---

## 11. ⭐ Advanced: Forecast Value Added, Hierarchical Reconciliation and MLOps for Ops
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Forecast Value Added (FVA)** = accuracy of a step (e.g., planner override) minus accuracy of the naive forecast. If a manual override has negative FVA, remove it.
- **Hierarchical forecasting:** forecasts at SKU, category, region and national level must add up. **Reconciliation** (bottom-up, top-down, MinT) makes them coherent.
- **Intermittent demand** (many zeros, spare parts): Croston/SBA, or probabilistic count models.
- **MLOps:** monitor data and concept drift, retrain schedule, feature store, backtesting, and **champion-challenger** rollout. Tie to the cost of error: asymmetric loss (stock-out costs more than holding).
- **Explainability:** SHAP values show which features drive a forecast or risk score, vital to win planner trust.

### Example
Naive WAPE = 30%, statistical model = 24%, planner-adjusted = 26%. FVA of the statistical model vs naive = +6 pp; planner override vs statistical = −2 pp (hurts). Decision: freeze overrides except for known events.

### In the news
See news box. Amazon quoted improvements by horizon and level (national vs regional), consistent with measuring forecast value at each level of the hierarchy.

### Interview angle
> [!question] How it is asked
> "Your ML forecast is more accurate but planners ignore it. What do you do?"

> [!tip] Strong answer includes
> - Trust building: explainability, FVA tracking, pilot on a few categories
> - Measure in business terms (inventory, service level), not only MAPE
> - Process change: S&OP integration, override governance
> - Monitoring and retraining plan

---

## 12. ⭐ Advanced: Prescriptive Analytics: Predict-then-Optimize
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Most ops value comes when predictions feed a decision model: **predict → optimise → act**.

- Predict demand/lead time/failure probability (ML).
- Optimise decisions (LP/MILP, stochastic programming): how much to order, where to ship, which machine to service first.
- Simulate (Monte Carlo/digital twin) to test policies before roll-out.

Caution: the most accurate predictor is not always the best decision-maker (decision-focused learning); errors that matter are those that change the decision. For inventory, plug quantile forecasts into the newsvendor critical ratio $CR=\frac{C_u}{C_u+C_o}$ and stock to the CR-quantile of demand.

### Example
Unit cost ₹60, price ₹100, salvage ₹40. $C_u=100-60=40$, $C_o=60-40=20$, CR = 40/60 = **0.667**. Stock to the 66.7th percentile of the forecast demand distribution, not the mean.

### In the news
See news box. Amazon's forecasts exist to drive inventory placement and delivery speed, a predict-then-optimise loop.

### Interview angle
> [!question] How it is asked
> "You have a good demand forecast. How do you turn it into an ordering decision?"

> [!tip] Strong answer includes
> - Critical-ratio/newsvendor logic with quantile forecast
> - Constraints (MOQ, capacity, shelf life) in the optimiser
> - Simulation before deployment and A/B or pilot after
> - Cost asymmetry between shortage and excess

---
## 🔗 Go deeper: expansion notes
- [[218 Forecasting with ML & Foundation Models|Forecasting with ML & Foundation Models]]
- [[120 Integrated Business Planning (IBP) & S&OP Maturity|Integrated Business Planning (IBP) & S&OP Maturity]]
