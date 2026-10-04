---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Demand Forecasting & Planning"
tier: Tier 1
roles: Operations / Consulting / PM
status: complete
subtopics: 14
---
# Demand Forecasting & Planning

⬅ [[003 Inventory Management]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[005 Production & Operations Planning]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting / PM

## Sub-topics in this note
1. [[#1. Qualitative Methods]]
2. [[#2. Simple Moving Average (SMA)]]
3. [[#3. Weighted Moving Average (WMA)]]
4. [[#4. Exponential Smoothing]]
5. [[#5. Holt-Winters (Triple Exp. Smoothing)]]
6. [[#6. Regression Forecasting]]
7. [[#7. Seasonality & Trend Analysis]]
8. [[#8. Forecast Error Metrics]]
9. [[#9. Demand Planning Process]]
10. [[#10. S&OP (Sales & Operations Planning)]]
11. [[#11. Collaborative Forecasting (CPFR)]]
12. [[#12. AI/ML in Demand Forecasting]]
13. [[#13. ⭐ Advanced: Intermittent Demand & Croston's Method]]
14. [[#14. ⭐ Advanced: Forecast Value Added (FVA), Bias & Hierarchical Reconciliation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI forecasting goes mainstream, and policy shocks break the old models
> **Amazon's foundation forecasting model (announced 11 Jun 2025).** Amazon said its new AI forecasting model, deployed in the US, Canada, Mexico and Brazil, improved **long-term national forecasts for deal events by 10%** and **regional forecasts for millions of popular items by 20%**. Earlier systems relied on sales history alone; the new model also uses regional and seasonal patterns (the example given was ski-goggle demand in Boulder, Colorado). ([Supply Chain Dive](https://www.supplychaindive.com/news/amazon-ai-supply-chain-usage-upgrades/750713/))
> 
> **Tariff front-loading distorts demand signals (early 2025).** The NRF / Hackett Global Port Tracker reported loaded US imports up **13.4% year on year in January 2025** and projected +6.1% in February and +10.8% in March as retailers pulled orders ahead of tariffs, with the first year-on-year decline since September 2023 expected in June-July. Orders driven by policy, not consumer demand, are a classic forecasting trap. ([Supply Chain Dive](https://www.supplychaindive.com/news/loaded-import-volume-forecast-national-retail-federation-tariffs-trump/742071/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Qualitative Methods
> 🔴 Tier 1 · _Tracker hint:_ Market survey, Delphi method, expert judgment, sales force composite

### Definition
Used when historical data is scarce or irrelevant (new products, launches, structural change), or to overlay judgement on statistics.
- **Market research / survey**: questionnaires, test markets, conjoint analysis; costly but captures intent.
- **Delphi method**: a panel of experts answers anonymously over several rounds; a facilitator shares summarised feedback until opinions converge; reduces dominance and groupthink.
- **Executive/expert judgment (jury of executive opinion)**: quick, but biased by seniority.
- **Sales-force composite**: reps estimate their territories; close to customers but biased by quotas.
- **Customer/channel input** and **analogy** (use a similar past launch's curve).

Risks: optimism bias, anchoring, sandbagging (reps lowball when paid against quota). Best used with statistical forecast, with **FVA** checks (see section 14).

### Example
A Pune-based EV start-up has no sales history. It surveys 2,000 target buyers (12% say "likely to buy"), applies a haircut (stated intent overstates actual purchases; a common rule is to discount heavily), triangulates with a Delphi panel of 8 dealers/analysts across two rounds, and arrives at a launch-year range rather than a point.

### In the news
See news box. Policy shocks (tariffs) are exactly when history fails and qualitative judgement (customer/channel input) must supplement models.

### Interview angle
> [!question] How it is asked
> "How would you forecast demand for a new product with no history?"

> [!tip] Strong answer includes
> - Analogy to similar products, surveys/test markets, Delphi
> - Combining sources (triangulation) and giving a range with scenarios
> - Bias controls: anonymity (Delphi), separating forecast from targets
> - Revisit weekly after launch with actuals (Bayesian updating)

---

## 2. Simple Moving Average (SMA)
> 🔴 Tier 1 · _Tracker hint:_ Avg of last N periods; formula, pros/cons, lag issue

### Definition
$$F_{t+1} = \frac{A_t + A_{t-1} + \dots + A_{t-N+1}}{N}$$

Averages the last $N$ actuals with equal weights. **Pros:** simple, smooths noise, transparent. **Cons:** lags a trend (forecast trails by about $(N-1)/2$ periods), ignores older data completely, treats all $N$ periods equally, needs $N$ data points, cannot handle seasonality. **Choice of N:** larger N = smoother but slower; smaller N = responsive but noisy. Best for stable, level demand.

### Example
Demand weeks 1-5: 120, 130, 125, 140, 135. 3-week SMA forecast for week 6 = (125 + 140 + 135)/3 = **133.3**. For a rising series 100, 110, 120, 130 the 3-period SMA gives 120 for the next period vs a trend-based value of ~140; that gap is the lag.

### In the news
See news box. With front-loaded orders, a moving average would read the temporary surge as a new level and over-forecast the following months.

### Interview angle
> [!question] How it is asked
> "Compute the 3-period moving average. What are its limitations?"

> [!tip] Strong answer includes
> - Correct arithmetic and window choice trade-off
> - Lag with trend, no seasonality handling
> - When it is fine (stable demand, short horizon)
> - Better alternatives: exponential smoothing, Holt

---

## 3. Weighted Moving Average (WMA)
> 🔴 Tier 1 · _Tracker hint:_ Higher weights to recent data; weight selection

### Definition
$$F_{t+1} = \sum_{i=1}^{N} w_i A_{t-i+1}, \qquad \sum w_i = 1$$

Recent periods get larger weights, so the forecast responds faster than SMA. **Choosing weights:** judgement, or choose weights that minimise historical error (MAD/MSE) on a hold-out set; weights must sum to 1. Still limited to N points and lags trends, though less. Generalisation: exponential smoothing uses geometrically declining weights over all history.

### Example
Same data (most recent first): 135, 140, 125. Weights 0.5, 0.3, 0.2:
F = 0.5×135 + 0.3×140 + 0.2×125 = 67.5 + 42 + 25 = **134.5** (vs SMA 133.3, because the latest value 135 counts more than the 125).

### In the news
See news box. When demand regime changes (tariffs, policy), heavier recent weights adapt faster, but also chase noise: a front-loaded spike gets over-trusted.

### Interview angle
> [!question] How it is asked
> "When would you use weighted over simple moving average and how would you choose the weights?"

> [!tip] Strong answer includes
> - Weights sum to 1, recent heavier
> - Choose by minimising error on back-test, not by gut alone
> - Trade-off: responsiveness vs noise
> - Mention exponential smoothing as the systematic version

---

## 4. Exponential Smoothing
> 🔴 Tier 1 · _Tracker hint:_ Ft = α·At-1 + (1-α)·Ft-1; α selection, single vs double

### Definition
**Single (simple) exponential smoothing:**
$$F_{t+1} = \alpha A_t + (1-\alpha)F_t$$
(the tracker writes it as $F_t = \alpha A_{t-1} + (1-\alpha)F_{t-1}$, same idea.) Equivalent to weights $\alpha(1-\alpha)^k$ on past data. Needs only last forecast and actual. **α in (0,1):** high α (0.3-0.5) = responsive, noisy; low α (0.05-0.2) = stable, slow. Pick α minimising MAD/MSE on history. Start value: first actual or mean of first few. For level-only demand.

**Double (Holt's linear) exponential smoothing** adds a trend:
$$L_t = \alpha A_t + (1-\alpha)(L_{t-1} + T_{t-1}), \quad T_t = \beta(L_t - L_{t-1}) + (1-\beta)T_{t-1}, \quad F_{t+m} = L_t + mT_t$$

### Example
α = 0.3, F₁ = 100, A₁ = 110: F₂ = 0.3×110 + 0.7×100 = **103**. A₂ = 120: F₃ = 0.3×120 + 0.7×103 = 36 + 72.1 = **108.1**. Note the forecast keeps lagging a rising series; Holt's trend term would fix that.

### In the news
See news box. Many demand-planning tools (SAP IBP, Kinaxis, o9) still use exponential-smoothing families as baseline models, with ML as overlays (general statement).

### Interview angle
> [!question] How it is asked
> "Forecast next month using exponential smoothing with α = 0.3. What does α mean?"

> [!tip] Strong answer includes
> - Formula, arithmetic done cleanly
> - α trade-off and how to select (minimise error)
> - Single vs double (trend) vs triple (season)
> - Initialisation and tracking-signal monitoring

---

## 5. Holt-Winters (Triple Exp. Smoothing)
> 🔴 Tier 1 · _Tracker hint:_ Trend + seasonality components; additive vs multiplicative

### Definition
Holt-Winters smooths **three** components: level $L$, trend $T$, and seasonal $S$ (season length $s$, e.g. 12 months, 7 days), with parameters $\alpha, \beta, \gamma$.

**Additive** (seasonal swing roughly constant in size): $F_{t+m} = L_t + mT_t + S_{t+m-s}$.
**Multiplicative** (seasonal swing grows with level, common in retail): $F_{t+m} = (L_t + mT_t)\times S_{t+m-s}$.

Multiplicative level update: $L_t = \alpha\,\frac{A_t}{S_{t-s}} + (1-\alpha)(L_{t-1}+T_{t-1})$; $T_t = \beta(L_t-L_{t-1}) + (1-\beta)T_{t-1}$; $S_t = \gamma\,\frac{A_t}{L_t} + (1-\gamma)S_{t-s}$. Needs at least 2 full seasons of history. In Python: `statsmodels.tsa.holtwinters.ExponentialSmoothing`.

### Example
Level 200, trend 5 units/month, seasonal index for target month 1.2 (e.g. festive month), forecast 2 months ahead: multiplicative = (200 + 2×5) × 1.2 = 210 × 1.2 = **252**. Additive with seasonal +30: 200 + 10 + 30 = 240.

### In the news
See news box. Seasonality models are the baseline Amazon-type systems build on; the reported 10-20% gains came from adding richer regional and event features beyond sales history.

### Interview angle
> [!question] How it is asked
> "Demand has trend and seasonality. Which method would you use?"

> [!tip] Strong answer includes
> - Three components and three parameters
> - Additive vs multiplicative choice (does seasonal amplitude scale with level?)
> - Data requirement (2+ seasons) and limits (festival dates shift, such as Diwali, Eid)
> - Alternatives: regression with dummies, ARIMA/SARIMA, Prophet, ML

---

## 6. Regression Forecasting
> 🔴 Tier 1 · _Tracker hint:_ Time-series regression, causal factors, R²

### Definition
**Linear regression** fits $y = a + bx$ by least squares: $b = \dfrac{\sum (x-\bar x)(y-\bar y)}{\sum (x-\bar x)^2}$, $a = \bar y - b\bar x$.
- **Time-series (trend) regression**: $x$ = time period.
- **Causal / multiple regression**: $y = \beta_0 + \beta_1 x_1 + \dots$ with drivers such as price, promotion, weather, GDP, festival dummies.

**R²** = proportion of variance explained = $1 - SSE/SST$; also check adjusted R², p-values, residual plots (autocorrelation, heteroscedasticity), multicollinearity, out-of-sample error. Causal models need forecasts of the drivers themselves. Beware spurious correlation and extrapolation beyond the data range.

### Example
Periods 1-5, demand 10, 12, 13, 15, 18. $\bar x = 3$, $\bar y = 13.6$. $\sum(x-\bar x)(y-\bar y) = 7.2 + 1.6 + 0 + 1.4 + 8.8 = 19$; $\sum(x-\bar x)^2 = 10$. $b = 1.9$; $a = 13.6 - 1.9 \times 3 = 7.9$. Forecast period 6: 7.9 + 1.9×6 = **19.3**. SST = 37.2, SSR = $b^2 \times 10$ = 36.1, so R² = **0.97**.

### In the news
See news box. Causal models can include policy variables (tariff dates) as dummies, but only if the dates are known; this is where Amazon-style models add event and regional features.

### Interview angle
> [!question] How it is asked
> "How would you build a model to forecast demand using price and promotion?"

> [!tip] Strong answer includes
> - Explanatory variables, functional form (log-log gives elasticities)
> - Diagnostics (R², residuals, multicollinearity) and out-of-sample test
> - Need future values of drivers
> - Interpretation: price elasticity, promo uplift

---

## 7. Seasonality & Trend Analysis
> 🔴 Tier 1 · _Tracker hint:_ Seasonal indices, trend decomposition, STL method

### Definition
Demand = **Trend (T) + Seasonality (S) + Cyclical (C) + Irregular/noise (I)**: multiplicative $D = T \times S \times C \times I$ or additive.

**Seasonal index** = average demand for the period (e.g. quarter) / overall average. Steps: (1) compute averages by period over several years; (2) divide by the grand average; (3) **deseasonalise** = actual / index; (4) fit trend to deseasonalised data; (5) reseasonalise = trend forecast × index. Indices should average 1.

**Classical decomposition**: centred moving average to estimate trend. **STL** (Seasonal-Trend decomposition using LOESS): robust to outliers, allows seasonal shape to change over time; in Python `statsmodels.tsa.seasonal.STL`.

### Example
Quarterly average demand: Q1 80, Q2 100, Q3 140, Q4 80; grand average 100. Indices: 0.8, 1.0, 1.4, 0.8 (sum = 4.0). Next year's deseasonalised trend forecast 110 per quarter: Q3 forecast = 110 × 1.4 = **154**; Q1 = 110 × 0.8 = 88.

### In the news
See news box. Front-loaded tariff volumes are an **irregular** component; they must be flagged/cleansed before computing seasonal indices, or next year's forecast will carry a phantom peak.

### Interview angle
> [!question] How it is asked
> "How do you handle seasonal demand like Diwali for an Indian retailer?"

> [!tip] Strong answer includes
> - Decompose into trend, seasonality, noise; compute indices
> - Handle moving festival dates and promotions with dummies/event calendar
> - Cleanse outliers (stock-outs, one-offs); STL for evolving seasonality
> - Plan capacity/inventory build-up ahead of peak

---

## 8. Forecast Error Metrics
> 🔴 Tier 1 · _Tracker hint:_ MAD, MSE, MAPE, RMSE — formulas and interpretation

### Definition
With error $e_t = A_t - F_t$ over $n$ periods:

| Metric | Formula | Notes |
|---|---|---|
| **Bias / ME** | $\sum e_t / n$ | Sign shows over-/under-forecasting |
| **MAD / MAE** | $\sum \lvert e_t \rvert / n$ | Same units as demand; robust |
| **MSE** | $\sum e_t^2 / n$ | Penalises large errors |
| **RMSE** | $\sqrt{MSE}$ | Same units, outlier-sensitive |
| **MAPE** | $\frac{100}{n}\sum \lvert e_t \rvert / A_t$ | Scale-free; blows up when $A_t$ near 0 |
| **WAPE** | $\sum\lvert e_t\rvert / \sum A_t$ | Volume-weighted, popular in retail |
| **Tracking signal** | $\sum e_t / MAD$ | Alarm if outside ±4 (some use ±3 to ±6) |

### Example
Actual 100, 110, 90; forecast 95, 115, 100. Errors: +5, −5, −10. MAD = (5+5+10)/3 = **6.67**. MSE = (25+25+100)/3 = 50; RMSE = **7.07**. MAPE = (5/100 + 5/110 + 10/90)/3 = (0.0500 + 0.0455 + 0.1111)/3 = **6.9%**. Bias = −10/3 = −3.3 (over-forecast). Tracking signal = −10/6.67 = **−1.5**, within limits.

### In the news
See news box. Amazon's reported "20% improvement" in regional forecasts would be measured with an error metric like WAPE or MAPE at region-item level; always ask which metric and level of aggregation.

### Interview angle
> [!question] How it is asked
> "Calculate MAPE and tell me which metric you'd use for intermittent demand."

> [!tip] Strong answer includes
> - Correct formulas and arithmetic
> - Pros/cons: MAPE fails on zeros; RMSE penalises large misses
> - Bias vs accuracy distinction; tracking signal
> - Aggregation level matters (error falls when aggregating SKUs)

---

## 9. Demand Planning Process
> 🔴 Tier 1 · _Tracker hint:_ S&OP, consensus forecasting, rolling forecast horizon

### Definition
A monthly/weekly cycle that turns data into an agreed demand number:
1. **Data collection and cleansing**: sales history, remove stockout-censored and one-off events.
2. **Statistical baseline forecast** (best-fit model per SKU-location).
3. **Overlays**: promotions, price changes, launches, market intelligence.
4. **Consensus review** among sales, marketing, planning, finance: agree one number.
5. **Approve and hand to supply planning**; compare against targets and capacity (S&OP).
6. **Measure accuracy and bias**; feed back.

**Rolling forecast horizon:** each period, drop the elapsed period and add a new one at the end (e.g. a 12- or 18-month rolling plan), so forecasts are always refreshed. Planning hierarchy: product family vs SKU; region vs store; forecast at higher level, disaggregate. Separate **forecast** (unbiased expectation) from **plan/target** (what we want).

### Example
A beverage firm forecasts 1.0 million cases for July. Marketing adds a 10% promotion uplift on 40% of volume (+4% overall: 1.04m); the heat-wave overlay adds 3% (≈1.07m); Finance's target is 1.2m. The planning team documents the gap (forecast 1.07m vs target 1.2m) and takes a decision: either close the gap with actions or plan supply to the forecast.

### In the news
See news box. AI forecasting changes step 2 (the baseline), not the need for consensus; Amazon still pairs model output with planners.

### Interview angle
> [!question] How it is asked
> "Describe how you would set up a demand planning process for a FMCG firm."

> [!tip] Strong answer includes
> - Data → baseline → overlay → consensus → approval → measurement
> - Separate forecast from target; measure bias
> - Rolling horizon and frequency by category
> - Roles and ownership (demand planner, sales, finance)

---

## 10. S&OP (Sales & Operations Planning)
> 🔴 Tier 1 · _Tracker hint:_ Cross-functional alignment: sales, ops, finance, supply

### Definition
**S&OP** is the monthly executive process that balances demand and supply and aligns the operating plan with the financial plan. Typical 5-step cycle:
1. **Data gathering / product review**
2. **Demand review**: consensus demand plan
3. **Supply review**: capacity and material feasibility, constraints, scenarios
4. **Pre-S&OP (reconciliation)**: resolve gaps, financial impact
5. **Executive S&OP meeting**: decisions, approve plan, assign actions.

Time horizon 12-24 months, aggregated (families). **IBP** (Integrated Business Planning) extends to financial and strategy. Outputs: one set of numbers, frozen near-term plan, risks and opportunities. Maturity: reactive, standard, advanced, proactive. Failure causes: sales and ops working separately, no executive ownership, too detailed, ignoring finance. Tools: SAP IBP, o9, Kinaxis, Anaplan.

### Example
Sales plans 120,000 units in Q3, plant capacity is 100,000 on normal time; overtime can add 10,000 at ₹40 more per unit. S&OP options: overtime (10,000 × 40 = ₹4 lakh), outsource 10,000, shift some demand to Q4 through promotions, or accept a shortfall. Executive meeting selects the lowest-cost option consistent with service targets.

### In the news
See news box. Tariff and policy swings forced faster S&OP cycles and scenario planning (best/worst case), as the NRF projections themselves show quickly changing import expectations.

### Interview angle
> [!question] How it is asked
> "What is S&OP and why do companies struggle with it?"

> [!tip] Strong answer includes
> - The cycle and the single set of numbers
> - Cross-functional (sales, ops, finance, supply) with executive decision-making
> - Scenario planning and trade-off with cost and service
> - Pitfalls: siloed targets, sandbagging, lack of discipline

---

## 11. Collaborative Forecasting (CPFR)
> 🔴 Tier 1 · _Tracker hint:_ Shared forecasts with retail partners; VMI link

### Definition
**CPFR** (Collaborative Planning, Forecasting and Replenishment, VICS standard) is a process where a supplier and retailer build a **joint business plan** and a **shared forecast**, then manage exceptions together. Stages: strategy and planning (partnership, joint business plan), demand and supply management (sales and order forecast), execution (order generation, delivery), analysis (exception management, performance). Compared with **VMI**: VMI hands replenishment to the vendor using the customer's stock data; CPFR is a *two-way* planning collaboration (both parties jointly create forecasts). Benefits: less bullwhip, higher availability, lower stocks. Barriers: trust, IT integration, partner readiness, fragmented retail base in India.

### Example
Walmart and Warner-Lambert (1990s) piloted CPFR on Listerine, improving in-stock and sales; today Indian FMCG companies share secondary-sales and POS data with modern trade and distributors. Illustration: if a retailer plans a 3-week promotion, joint planning lets the supplier build stock ahead rather than react to a spike.

### In the news
See news box. Shared forecasts and signal visibility are the antidote to policy-driven order spikes becoming upstream noise (bullwhip).

### Interview angle
> [!question] How it is asked
> "How would you reduce forecast error with a large retailer customer?"

> [!tip] Strong answer includes
> - Joint business plan, share POS and promotion calendar, exception management
> - Difference from VMI
> - Prerequisites: data, trust, incentives
> - Pilot on top SKUs/partner, measure forecast accuracy and in-stock

---

## 12. AI/ML in Demand Forecasting
> 🔴 Tier 1 · _Tracker hint:_ Gradient boosting, LSTM, causal AI; vs traditional methods

### Definition
ML models learn patterns from many series and many features (price, promo, weather, events, holidays, store attributes), unlike classical per-series statistics.
- **Gradient boosting** (LightGBM, XGBoost): tabular features with lags; fast, strong, the workhorse for retail.
- **Deep learning** (LSTM, DeepAR, Temporal Fusion Transformer): sequence models, global models across thousands of SKUs, probabilistic outputs.
- **Foundation / pretrained time-series models** (e.g. Amazon Chronos, Google TimesFM): zero-shot forecasting.
- **Causal ML**: estimates promo/price effect (uplift) rather than correlation.
- **Demand sensing**: short-term signal use (POS, weather).

Pros: handles many drivers and cold-start (by attributes); cons: data hungry, less interpretable, risk of overfitting, still needs good data and bias control. Always benchmark against a simple baseline (seasonal naive) with time-based cross-validation (no random splits).

```python
import lightgbm as lgb
df["lag_7"] = df.groupby("sku")["units"].shift(7)
df["roll_28"] = df.groupby("sku")["units"].transform(lambda s: s.shift(1).rolling(28).mean())
train = df[df.date < "2025-01-01"].dropna()
X = ["lag_7", "roll_28", "price", "promo", "dow"]
model = lgb.LGBMRegressor(n_estimators=500, learning_rate=0.05).fit(train[X], train["units"])
```

### Example
A grocery chain forecasts 50,000 SKU-store series. A global LightGBM with price, promo, weather and festival features cut WAPE from 32% to 27% against a Holt-Winters baseline (illustrative figures). Amazon's reported 20% gain in regional item forecasts is a published real-world comparison (see news box).

### In the news
See news box. Amazon's foundation forecasting model reflects the industry move from per-series statistics to one large model that learns across items and regions.

### Interview angle
> [!question] How it is asked
> "Would you replace statistical forecasts with machine learning?"

> [!tip] Strong answer includes
> - Where ML wins (many features, promotions, cold start) and where simple methods suffice (stable, low-volume)
> - Backtesting, baseline comparison, forecast value added
> - Governance: explainability, planner overrides, drift monitoring
> - Data quality first: clean history, stock-out correction

---

## 13. ⭐ Advanced: Intermittent Demand & Croston's Method
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Intermittent (lumpy) demand**, common for spare parts and slow movers, has many zero-demand periods. Standard smoothing is biased and MAPE is undefined. **Croston's method** smooths separately (a) the **size** of non-zero demands $z$ and (b) the **interval** between them $p$, updating only when demand occurs:

$$\hat z_t = \alpha z_t + (1-\alpha)\hat z_{t-1}, \quad \hat p_t = \alpha p_t + (1-\alpha)\hat p_{t-1}, \quad F = \hat z/\hat p$$

The **SBA** correction multiplies by $(1 - \alpha/2)$ to remove bias. Classify patterns by **ADI** (average demand interval) and **CV²**: smooth, erratic, intermittent, lumpy (cut-offs ADI = 1.32, CV² = 0.49). Evaluate with MASE or scaled bias, not MAPE; for inventory use lead-time demand distributions (Poisson, negative binomial) rather than normal.

### Example
Smoothed demand size 20 units, smoothed interval 4 periods: forecast = 20/4 = **5 units per period**. With α = 0.1, SBA factor = 1 − 0.05 = 0.95, so 4.75.

### In the news
See news box. As AI models handle fast movers, spare parts and long tails remain a place where purpose-built intermittent methods and probabilistic forecasts still matter (analytical remark).

### Interview angle
> [!question] How it is asked
> "How would you forecast spare parts that sell once or twice a year?"

> [!tip] Strong answer includes
> - Why standard methods fail; ADI/CV² classification
> - Croston/SBA or probabilistic approaches; service-level-driven stocking
> - Use installed base, failure rates and criticality (VED)
> - Pool across locations; right error metrics

---

## 14. ⭐ Advanced: Forecast Value Added (FVA), Bias & Hierarchical Reconciliation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**FVA** measures whether each step in the forecasting process improves accuracy versus the previous step (naive → statistical → planner override → consensus):

$$FVA = \text{Error}_{\text{before step}} - \text{Error}_{\text{after step}}$$

A positive FVA means the step added value; negative means it destroyed it (common with sales overrides driven by optimism). Pair with **bias** tracking: persistent over-forecast creates excess inventory; under-forecast creates stock-outs.

**Hierarchical forecasting:** forecast at SKU-store, family and national levels. Independent forecasts are inconsistent; **reconcile** them (bottom-up, top-down, middle-out or optimal MinT reconciliation) so lower levels sum to higher levels. Aggregating reduces error (risk pooling), so judge accuracy at the level where decisions are made.

### Example
Naive forecast WAPE 40%, statistical model 30%, planner overrides 33%, consensus 31%. FVA of statistical = +10 points; FVA of planner override = −3 points (worse), so the overrides should be restricted to events the model cannot know (promotions, launches).

### In the news
See news box. Amazon's quoted 10% and 20% gains are improvements against a prior baseline: that is FVA at scale, and the right question to ask of any AI forecasting claim.

### Interview angle
> [!question] How it is asked
> "Our forecast accuracy is 70%. How do you improve it?"

> [!tip] Strong answer includes
> - Define accuracy metric and level first; measure bias
> - FVA to find which steps help or hurt
> - Fix data (stock-out censoring), segment SKUs (ABC-XYZ), tune models per segment
> - Governance on overrides and incentives (separate forecast from sales target)

---
## 🔗 Go deeper: expansion notes
- [[118 New-Product Forecasting, Demand Sensing & Demand Shaping|New-Product Forecasting, Demand Sensing & Demand Shaping]]
- [[120 Integrated Business Planning (IBP) & S&OP Maturity|Integrated Business Planning (IBP) & S&OP Maturity]]
- [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory|Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]
- [[218 Forecasting with ML & Foundation Models|Forecasting with ML & Foundation Models]]
