---
tags: [machine-learning, tier2]
area: Machine Learning
topic: "Forecasting with ML & Foundation Models"
tier: Tier 2
roles: Analytics / Operations
status: complete
subtopics: 13
---
# Forecasting with ML & Foundation Models

⬅ [[101 Deep Learning Basics]] · [[_Index - Machine Learning|Machine Learning]] · [[219 NLP, Embeddings & LLM Applications for Analysts]] ➡

> **Area:** Machine Learning · **Priority:** 🟠 Tier 2 · **Target roles:** Analytics / Operations

## Sub-topics in this note
1. [[#1. Why Machine-Learning Forecasting: Local vs Global Models]]
2. [[#2. Feature Engineering for Demand: Lags, Calendars, Price and Promotion]]
3. [[#3. Gradient-Boosted Global Models (LightGBM) vs Local Statistical Models]]
4. [[#4. Executed Experiment: Global LightGBM vs Baselines (Simulated Retail Panel)]]
5. [[#5. Deep Forecasting Models: DeepAR, N-BEATS, Temporal Fusion Transformer]]
6. [[#6. Time-Series Foundation Models: Chronos, TimesFM, Moirai]]
7. [[#7. Probabilistic Forecasts: Quantile Loss and the Pinball Function]]
8. [[#8. Hierarchical and Grouped Forecasting: Reconciliation]]
9. [[#9. Evaluation: Rolling Origin, WAPE, Bias, MASE and Forecast Value Added]]
10. [[#10. Intermittent Demand and New-Product Cold Start]]
11. [[#11. M5 Competition: Lessons for Practitioners]]
12. [[#12. When Simple Beats Complex: A Decision Framework]]
13. [[#13. ⭐ Advanced: Productionising Forecasts, Monitoring and Ensembles]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): time-series foundation models went from research demos to products
> **TimesFM 3.0 (Google Research, 31 Aug 2026).** Google released TimesFM-3, a 330-million-parameter decoder-only model trained on more than 1 trillion time points, with native multivariate forecasting and support for past and future covariates, and reports rank 1 among pretrained models on the GIFT-Eval, fev-bench and TIME leaderboards. The repository notes a licensing split: code and weights up to version 2.5 are Apache-2.0, while the downloadable 3.0 weights are non-commercial; commercial and production use runs through Google Cloud services such as BigQuery ML (rollout finished in September 2026). ([Google Research blog](https://research.google/blog/timesfm-3-a-zero-shot-foundation-model-for-multivariate-forecasting/); [TimesFM repository](https://github.com/google-research/timesfm))
>
> **Chronos-2 (Amazon, 20 Oct 2025).** Amazon released Chronos-2, a 120M-parameter encoder-only model that forecasts univariate, multivariate and covariate-informed tasks in one architecture, zero-shot, and ranked first among pretrained models on GIFT-Eval; it is Apache-2.0 and runs at over 300 forecasts per second on a single A10G GPU. ([Amazon Science](https://www.amazon.science/blog/introducing-chronos-2-from-univariate-to-universal-forecasting); [model card](https://huggingface.co/amazon/chronos-2))
>
> **Moirai 2.0 (Salesforce, 8 Aug 2025).** Salesforce switched Moirai from a masked-encoder to a decoder-only design and trained it with quantile loss; the company reports it is about 96% smaller than Moirai-large, 44% faster, and first by MASE on GIFT-Eval among models without test-data leakage. ([Salesforce blog](https://www.salesforce.com/blog/moirai-2-0/))
>
> **Benchmarks got stricter (2025).** fev-bench (100 tasks, 7 domains, 46 with covariates) reports win rates and skill scores with bootstrapped confidence intervals, because earlier leaderboards often could not distinguish real gains from noise. ([arXiv 2509.26468](https://arxiv.org/abs/2509.26468))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Why Machine-Learning Forecasting: Local vs Global Models
> 🟠 Tier 2 · _Key points:_ One model per series vs one model for thousands of series; cross-learning; covariates

### Definition
A **local** model (ETS, ARIMA, Theta; see [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]) is fitted separately to each series using only that series' history. A **global** model is a single model trained on **all** series stacked together, with series identity, calendar and driver variables as features. Global models can **cross-learn**: a new SKU with 8 weeks of history borrows seasonality and promotion response from thousands of similar SKUs.

When each approach wins:
- Few series, long clean history, stable seasonality: local statistical models are hard to beat and easy to explain.
- Many related series, short or intermittent histories, strong external drivers (price, promo, weather, festivals, stock-outs): global ML wins.
- Hierarchies, cold-start and new products ([[118 New-Product Forecasting, Demand Sensing & Demand Shaping]]) favour global models because features, not history, carry the signal.

Typical pipeline: tidy panel (SKU × location × date), feature table, global model, time-based validation, forecast with intervals, reconcile across the hierarchy, then feed planning ([[004 Demand Forecasting & Planning]], [[119 Supply Planning, DRP & Available-to-Promise]], [[120 Integrated Business Planning (IBP) & S&OP Maturity]]). Earlier coverage of the basics sits in [[099 ML for Operations & SCM]] and [[066 Demand Forecasting & Time Series]].

### Example
A beverage company has 40 SKUs; each SKU alone has about 3 years of daily data and an 8%-of-days promotion calendar, roughly 88 promo days per SKU, too few to learn the uplift reliably. A single global model sees $40\times0.08\times1{,}095\approx3{,}500$ promo observations and learns one shared uplift curve, with a SKU-level adjustment. The experiment in sub-topic 4 reproduces this effect with simulated data.

### In the news
See news box. Foundation models extend "global" to the extreme: one pretrained model for every series, zero-shot, with no per-series training.

### Interview angle
> [!question] How it is asked
> "You have 10,000 SKUs across 500 stores. Do you fit 5 million ARIMA models?"

> [!tip] Strong answer includes
> - Global model with SKU, store and hierarchy features, plus a statistical baseline for the stable head
> - Cross-learning benefits for short and intermittent series
> - Compute and maintenance cost of per-series models
> - Validation by rolling origin and segmentation by volume and variability

---
## 2. Feature Engineering for Demand: Lags, Calendars, Price and Promotion
> 🟠 Tier 2 · _Key points:_ Lag at least the horizon; rolling stats from lagged data; known-future covariates; no leakage

### Definition
Forecasting becomes supervised regression once each row (SKU, day $t$) carries features known **at the forecast origin**.

| Feature family | Examples | Notes |
|---|---|---|
| **Lags** | $y_{t-14},y_{t-21},y_{t-28},y_{t-364}$ | For a horizon of $H$ days use lags **at least $H$** (or recurse); lag 7 or 364 captures weekly and annual season |
| **Rolling statistics** | mean, std, min, max of the last 7/28/90 days, computed on data shifted by $H$ | Shift **before** rolling or the window peeks into the future |
| **Calendar** | day of week, month, week of year, payday, month-end | Cyclical encoding (sin/cos) helps linear models; trees take integers |
| **Events** | Diwali, Eid, IPL season, monsoon onset, GST-rate change day | Add lead and lag flags (demand builds before a festival, drops after) |
| **Price and promotion** | price index vs base, discount depth, promo flag, competitor price | Known in the future (planned), so legal for any horizon |
| **Availability** | stock-out flag, days since last stock-out | Sales are censored demand; mark or impute stock-outs |
| **Static attributes** | SKU category, pack size, store format, city tier | Enable cold-start |
| **Weather and macro** | temperature, rainfall, CPI | Use **forecasts** of weather, not actuals, at training time to avoid optimism |

**Leakage rules:** (1) never use information dated after the origin; (2) fit encoders and scalers on training data only; (3) cross-validate by time, never by random rows; (4) beware of features that are consequences of the target (for example "returns" in the same week).

**Target handling:** counts are non-negative and skewed, so use an objective such as Poisson or **Tweedie** rather than squared error, or forecast $\log(1+y)$; scale each series (divide by its recent mean) to compare across SKUs.

### Example
Forecast horizon $H=14$ days. Features for SKU 7 on 20 Sep (origin 6 Sep): `lag14` = sales on 6 Sep, `lag28` = 23 Aug, `rm28` = mean of the 28 days ending 6 Sep, `dow` = Saturday, `promo` = 1 (planned), `price` = 0.85 of base. Every value is known on 6 Sep, so the same trained model can score all 14 future days without recursion. If `rm28` were computed up to 19 Sep it would leak the answer and the offline accuracy would be falsely good.

```python
import pandas as pd
# df: long panel with columns sku, date, y (built in the next sub-topic)
df = df.sort_values(["sku", "date"])
g = df.groupby("sku")["y"]
for L in (14, 21, 28, 364):
    df[f"lag{L}"] = g.shift(L)                 # every lag >= horizon (14)
df["rm28"] = g.shift(14).groupby(df.sku).transform(lambda x: x.rolling(28).mean())   # shift first, then roll
df["dow"], df["month"] = df.date.dt.dayofweek, df.date.dt.month
```

### In the news
See news box. Newer models such as Chronos-2 and TimesFM 3.0 accept past and future covariates natively, which replaces some hand-built lag features but not the thinking about what is known at the origin.

### Interview angle
> [!question] How it is asked
> "What features would you use to forecast daily demand for a packaged-food SKU in India?"

> [!tip] Strong answer includes
> - Lags and rolling stats with the horizon rule, calendar, festival and payday flags
> - Price, promo and distribution (weighted availability)
> - Stock-out handling and leakage controls
> - Static attributes for cold start; weather forecasts rather than actuals

---
## 3. Gradient-Boosted Global Models (LightGBM) vs Local Statistical Models
> 🟠 Tier 2 · _Key points:_ Trees on lag features; Tweedie/Poisson objectives; strong baselines; maintainability

### Definition
**Gradient boosting** builds many shallow trees sequentially, each fitted to the residual gradient of the previous ensemble. **LightGBM**, XGBoost and CatBoost are the workhorses of tabular forecasting; LightGBM trains quickly on millions of rows, supports categorical features and custom objectives (Poisson, Tweedie, quantile). Tree models cannot extrapolate beyond the target range seen in training, so trending series need a **detrending** step (model the ratio to a recent level) or a hybrid with a statistical trend.

| | Local ETS/ARIMA | Global LightGBM |
|---|---|---|
| Data per model | one series | all series |
| Strength | smooth, stable, few series; explainable | covariates, promotions, cross-learning, cold start |
| Weakness | cannot use drivers easily; fragile on short or intermittent data | trend extrapolation; needs feature work; can leak |
| Intermittent demand | Croston, SBA, TSB | Tweedie or Poisson loss handles zeros |
| Ops burden | thousands of fits | one model, one retrain job |

Good practice: always include a **seasonal naive** and a **moving average** baseline, report the **gain over the best baseline**, and keep a statistical model for the stable "A-class" head where it is tough to beat. Related: [[095 Regression Algorithms]], [[098 Model Selection & Optimization]].

### Example
Tweedie with variance power 1.2 sits between Poisson (1) and gamma (2), suiting daily unit sales with many zeros and occasional spikes. Configuration used in the next sub-topic's experiment:

```python
import lightgbm as lgb
m = lgb.LGBMRegressor(objective="tweedie", tweedie_variance_power=1.2,
                      n_estimators=300, learning_rate=0.05, num_leaves=31,
                      min_child_samples=40, subsample=0.8, subsample_freq=1, colsample_bytree=0.8)
m.fit(train[feats], train.y)
```

### In the news
See news box. In the M5 competition (sub-topic 11) LightGBM variants dominated; the new foundation models are now compared with such tuned global models on benchmarks such as fev-bench.

### Interview angle
> [!question] How it is asked
> "Why would you choose LightGBM over ARIMA for retail demand? When would you not?"

> [!tip] Strong answer includes
> - Covariates, cross-learning, scale, count objectives
> - Not for few stable series or when explainability and trend extrapolation dominate
> - Baselines and rolling-origin validation prove the gain
> - Retraining cadence and monitoring cost

---
## 4. Executed Experiment: Global LightGBM vs Baselines (Simulated Retail Panel)
> 🟠 Tier 2 · _Key points:_ Rolling-origin WAPE; promo and price features matter; irreducible noise floor; quantile coverage

### Definition
A reproducible comparison on **simulated** data (not a real retailer): 40 SKUs, 3 years of daily Poisson demand with weekday effects, annual seasonality, trend, 8% promotion days (uplift +60%) and price elasticity −1.2. A 14-day horizon is evaluated at three **rolling origins** (4 Aug, 15 Sep, 27 Oct 2025), with the model retrained on data before each origin. Because the data are simulated, the **true mean** is known, which gives an "oracle" error floor created by pure Poisson noise.

### Example
```python
import numpy as np, pandas as pd, lightgbm as lgb
rng = np.random.default_rng(42)
S, T, H = 40, 3*365, 14
dates = pd.date_range("2023-01-02", periods=T, freq="D")
dow_eff = np.array([0.9, 0.85, 0.9, 0.95, 1.1, 1.3, 1.2])
frames = []
for s in range(S):
    base, price0 = rng.lognormal(2.3, 0.6), rng.uniform(80, 200)
    promo = (rng.random(T) < 0.08).astype(int)
    price = price0 * (1 - 0.15*promo) * (1 + rng.normal(0, 0.01, T))
    t = np.arange(T)
    mu = (base * dow_eff[dates.dayofweek] * (1 + 0.25*np.sin(2*np.pi*(t % 365)/365 + s))
          * (1 + 0.0004*t) * (1 + 0.6*promo) * (price/price0)**-1.2)
    frames.append(pd.DataFrame(dict(sku=s, date=dates, y=rng.poisson(mu), mu=mu, price=price/price0, promo=promo)))
df = pd.concat(frames, ignore_index=True)
df["dow"], df["month"] = df.date.dt.dayofweek, df.date.dt.month
g = df.groupby("sku")["y"]
for L in (14, 21, 28, 35, 364):
    df[f"lag{L}"] = g.shift(L)
sh = g.shift(H).groupby(df.sku)
df["rm28"], df["rm7"], df["rs28"] = (sh.transform(lambda x: x.rolling(28).mean()),
                                      sh.transform(lambda x: x.rolling(7).mean()),
                                      sh.transform(lambda x: x.rolling(28).std()))
feats = ["price","promo","dow","month","lag14","lag21","lag28","lag35","rm28","rm7","rs28","sku"]
wape = lambda a, f: np.abs(a - f).sum() / a.sum()
P = dict(n_estimators=300, learning_rate=0.05, num_leaves=31, min_child_samples=40,
         subsample=0.8, subsample_freq=1, colsample_bytree=0.8, verbose=-1, random_state=1)
out = {"seasonal naive (lag 14)": [], "28-day mean": [], "global LightGBM": [], "LightGBM without price/promo": [], "oracle (true mean)": []}
cov = []
for o in pd.to_datetime(["2025-08-04", "2025-09-15", "2025-10-27"]):
    train = df[(df.date < o)].dropna(subset=["lag364", "rs28"])
    test = df[(df.date >= o) & (df.date < o + pd.Timedelta(days=H))]
    a = test.y.values
    ma = df[df.date < o].groupby("sku").y.apply(lambda x: x.tail(28).mean())
    m1 = lgb.LGBMRegressor(objective="tweedie", tweedie_variance_power=1.2, **P).fit(train[feats], train.y)
    f2 = [f for f in feats if f not in ("price", "promo")]
    m2 = lgb.LGBMRegressor(objective="tweedie", tweedie_variance_power=1.2, **P).fit(train[f2], train.y)
    for k, f in zip(out, [test.lag14.values, test.sku.map(ma).values, m1.predict(test[feats]), m2.predict(test[f2]), test.mu.values]):
        out[k].append(wape(a, f))
    q10 = lgb.LGBMRegressor(objective="quantile", alpha=0.1, **P).fit(train[feats], train.y).predict(test[feats])
    q90 = lgb.LGBMRegressor(objective="quantile", alpha=0.9, **P).fit(train[feats], train.y).predict(test[feats])
    cov.append(np.mean((a >= q10) & (a <= q90)))
for k, v in out.items():
    print(f"{k:30s} WAPE {np.mean(v)*100:5.1f}%")
print("P10-P90 coverage", round(float(np.mean(cov)), 3))
```

Results (mean of three origins, 14-day windows, 560 SKU-days each):

| Method | WAPE |
|---|---|
| Seasonal naive (same weekday, 14 days ago) | 34.0% |
| 28-day moving average | 27.0% |
| Global LightGBM without price and promo features | 24.2% |
| **Global LightGBM with all features** | **19.0%** |
| Oracle (the true expected demand) | 17.6% |

What to read: (1) the global model cuts WAPE from 27.0% (best baseline) to 19.0%, a **30% relative reduction**; (2) **price and promotion features alone are worth 5.2 points** (24.2% to 19.0%), because promotions are planned in advance and hence known covariates; (3) even a perfect model scores 17.6% on this data, since Poisson noise at about 16 units a day is irreducible; LightGBM is within 1.4 points of the floor, so more modelling effort has little room to pay off; (4) the nominal 80% interval (P10 to P90) covered **77.3%** of actuals, slightly under-confident-width, a typical calibration shortfall to monitor. Numbers come from simulated data and will differ on real data; the **procedure** (baselines, rolling origin, oracle floor, calibration) is the transferable part.

### In the news
See news box. Benchmarks like fev-bench formalise this practice: many tasks, several origins, bootstrapped intervals, and strong baselines in the comparison.

### Interview angle
> [!question] How it is asked
> "Your ML model beats last year's forecast by 2 points of WAPE. Is that worth deploying?"

> [!tip] Strong answer includes
> - Compare with the best baseline (not just the old process), across several origins
> - Estimate the noise floor so you know the maximum possible gain
> - Show where the gain comes from (promo/price, cold-start SKUs, high-volume vs tail)
> - Translate to inventory or service-level impact in ₹

---
## 5. Deep Forecasting Models: DeepAR, N-BEATS, Temporal Fusion Transformer
> 🟠 Tier 2 · _Key points:_ Probabilistic RNN; pure-MLP stacks; attention with variable selection; when deep learning pays

### Definition
**DeepAR** (Amazon; Salinas, Flunkert, Gasthaus and Januschowski, published in the International Journal of Forecasting, 2020): an autoregressive recurrent network trained on many related series; it outputs the parameters of a distribution at each step (for example negative binomial for counts) and produces probabilistic forecasts by sampling paths. Strong for large panels of count-like series with covariates.

**N-BEATS** (Oreshkin et al., ICLR 2020): a deep stack of fully connected blocks with backward (backcast) and forward (forecast) residual links; univariate, no feature engineering, with an interpretable variant that fits trend and seasonality bases. It was introduced as a pure deep-learning model reported to outperform established statistical approaches on the M3, M4 and tourism benchmarks.

**Temporal Fusion Transformer, TFT** (Lim, Arik, Loeff and Pfister, Google, IJF 2021): combines LSTM encoding, multi-head attention, **variable-selection networks** and gating, takes static, past and known-future inputs, and outputs **quantiles** directly, with interpretable variable importance and attention over time.

**Caution:** Zeng et al. ("Are Transformers Effective for Time Series Forecasting?", AAAI 2023) showed that a one-layer linear model (DLinear) beat several Transformer forecasters on common long-horizon benchmarks, a reminder that depth is not accuracy. Deep models earn their cost when you have **many series, long histories, rich covariates, and need multi-horizon quantiles**; they carry heavier tuning, GPU and MLOps overhead ([[101 Deep Learning Basics]]).

### Example
Rule of thumb for a mid-size retailer: 5,000 SKU-store series with 3 years of data, promotions and weather. Options by cost: (1) seasonal naive and ETS baseline (hours); (2) LightGBM global model with features (days); (3) TFT or DeepAR with GluonTS or PyTorch Forecasting (weeks, GPU). Adopt the next tier only if it beats the previous by a margin that matters in ₹ of inventory.

```python
# GluonTS-style sketch (illustrative, not run here)
# from gluonts.torch import DeepAREstimator
# est = DeepAREstimator(freq="D", prediction_length=14, num_layers=2,
#                       distr_output=NegativeBinomialOutput(), trainer_kwargs={"max_epochs": 20})
# predictor = est.train(train_ds); forecasts = list(predictor.predict(test_ds))
```

### In the news
See news box. Pretrained foundation models (TimesFM, Chronos-2, Moirai 2.0) are the latest step in the deep-learning line that began with DeepAR and N-BEATS.

### Interview angle
> [!question] How it is asked
> "Would you use a Transformer for demand forecasting?"

> [!tip] Strong answer includes
> - Only if baseline and GBM leave measurable error and there is scale and covariates
> - Name a model (TFT for covariates and quantiles, DeepAR for count distributions, N-BEATS for univariate)
> - Evidence from rolling-origin tests, not leaderboard claims
> - Cost, latency, explainability, retraining burden

---
## 6. Time-Series Foundation Models: Chronos, TimesFM, Moirai
> 🟠 Tier 2 · _Key points:_ Pretrained on huge corpora; zero-shot forecasting; quantile outputs; covariate support; licences

### Definition
A **time-series foundation model (TSFM)** is pretrained once on a very large and diverse collection of series (real and synthetic) and then asked to forecast **new series zero-shot**: you supply the history (and optionally covariates) and receive point and quantile forecasts without per-series training. Optional **fine-tuning** (for example LoRA) adapts it to your data. Verified state of the main open families, as of October 2026:

| Model | Developer | Key verified facts |
|---|---|---|
| **Chronos-2** | Amazon | 20 Oct 2025; 120M parameters; encoder-only; univariate, multivariate and covariate-informed forecasting in one model; context up to 8,192; prediction length up to 1,024; Apache-2.0; `pip install chronos-forecasting`; first among pretrained models on GIFT-Eval at release |
| **TimesFM 2.5** | Google Research | 15 Sep 2025; 200M parameters (down from 500M in 2.0); 16k context (up from 2,048); optional 30M quantile head for horizons to 1k; covariates restored through XReg in Oct 2025; Apache-2.0 weights |
| **TimesFM 3.0** | Google Research | 31 Aug 2026; 330M parameters; trained on more than 1 trillion time points; native multivariate and covariates; downloadable weights are **non-commercial**; commercial use through Google Cloud (BigQuery ML). TimesFM is also offered inside Google Sheets via Connected Sheets (README, Feb 2026 update) |
| **Moirai 2.0** | Salesforce | 8 Aug 2025; decoder-only (Moirai 1 was a masked encoder); quantile loss and multi-token prediction; about 96% smaller and 44% faster than Moirai-large (company-reported) |

Earlier lineage: the original Chronos (2024) scaled and tokenised values and used language-model architectures; TimesFM (ICML 2024) introduced the patched decoder-only design; Moirai 1 (2024) introduced a masked encoder for any-variate forecasting. Commercial APIs also exist (for example Nixtla's TimeGPT). Evaluation suites: **GIFT-Eval**, **fev-bench**, **TIME**.

**How to use them sensibly:** (1) start from a seasonal-naive and LightGBM baseline; (2) run the TSFM zero-shot on the same rolling origins; (3) compare WAPE, bias and **quantile calibration**; (4) pass known covariates (promotion, price) if the model supports them, because a model blind to known promotions gives up exactly the gain that the price/promo ablation above shows (about 5 WAPE points in that simulation); (5) consider an **ensemble** (average of TSFM and GBM) which often beats both; (6) check licence and data-residency before production. Leaderboard ranks are measured on public benchmarks and may not transfer to your series; always run your own test.

### Example
Illustrative pseudo-workflow with Chronos-2 (API as per the model card; not executed here because it needs a model download):

```python
# pip install chronos-forecasting
# from chronos import Chronos2Pipeline
# pipe = Chronos2Pipeline.from_pretrained("amazon/chronos-2")
# pred = pipe.predict_df(context_df, future_df=future_covariates_df,   # promo, price known ahead
#                        prediction_length=14, quantile_levels=[0.1, 0.5, 0.9],
#                        id_column="sku", timestamp_column="date", target="y")
```

Decision table: zero-shot TSFM for the **long tail** (tens of thousands of low-volume series, no time to tune), tuned LightGBM or TFT for the **head** (high-value SKUs with promotions), seasonal naive as the control.

### In the news
See news box for all three launches. The licence split on TimesFM 3.0 is a practical lesson: a model that tops a leaderboard may not be usable in production on your own infrastructure.

### Interview angle
> [!question] How it is asked
> "Would you replace our forecasting stack with a foundation model?"

> [!tip] Strong answer includes
> - Benchmark on your data with rolling origins against current methods and a seasonal-naive control
> - Zero-shot for the long tail and cold start; tuned or ensembled models where covariates matter
> - Check covariate support, quantile quality, latency, cost and licence (non-commercial vs Apache-2.0)
> - Governance: monitoring, fallback to the baseline, versioning of model weights

---
## 7. Probabilistic Forecasts: Quantile Loss and the Pinball Function
> 🟠 Tier 2 · _Key points:_ Predict quantiles not just the mean; pinball loss; calibration and sharpness; newsvendor link

### Definition
A **probabilistic forecast** gives a distribution (or quantiles) for future demand, which is what inventory and capacity decisions require. The **pinball (quantile) loss** for quantile level $\tau$, forecast $\hat y$ and actual $y$ with error $e=y-\hat y$:

$$L_\tau(y,\hat y)=\max\big(\tau\,e,\;(\tau-1)\,e\big)$$

It penalises under-forecasts with weight $\tau$ and over-forecasts with weight $1-\tau$; the minimiser is the $\tau$-quantile of the predictive distribution. At $\tau=0.5$ it is half the absolute error. Averaging pinball loss over several quantiles approximates the **CRPS**; the M5 uncertainty track scored forecasts with a scaled pinball loss. Judge probabilistic forecasts on two properties: **calibration** (the P90 should exceed actuals about 90% of the time) and **sharpness** (narrow intervals).

**Link to inventory (newsvendor):** with underage cost $c_u$ and overage cost $c_o$, the optimal stock is the **critical-ratio quantile** $\frac{c_u}{c_u+c_o}$ of demand ([[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]], [[003 Inventory Management]]).

### Example
Pinball loss at $\tau=0.9$ with forecast 100: if actual is 120, $e=20$, loss $=0.9\times20=\mathbf{18}$; if actual is 80, $e=-20$, loss $=(0.9-1)(-20)=\mathbf{2}$. Under-forecasting costs 9 times more, which pushes the optimum toward a high quantile. At $\tau=0.5$ both cases cost 10.

Newsvendor: a bakery loses ₹40 margin per unsold-demand unit ($c_u$) and ₹10 per leftover unit ($c_o$); critical ratio $=40/(40+10)=0.80$, so bake to the **P80** of the demand forecast. If demand is normal with mean 100 and SD 30, that quantile is $100+0.8416\times30=125.2$ units.

```python
import numpy as np
pinball = lambda y, f, q: np.mean(np.maximum(q*(y-f), (q-1)*(y-f)))
print(pinball(np.array([120]), np.array([100]), 0.9), pinball(np.array([80]), np.array([100]), 0.9))  # 18.0 2.0
# LightGBM quantile model: lgb.LGBMRegressor(objective="quantile", alpha=0.9)
```

### In the news
See news box. TimesFM 2.5 offers an optional quantile head and Moirai 2.0 switched to quantile loss, both for probabilistic output; the executed experiment above showed an 80% interval covering 77.3% of actuals.

### Interview angle
> [!question] How it is asked
> "Why forecast quantiles instead of the mean for inventory?"

> [!tip] Strong answer includes
> - Costs are asymmetric: the optimal stock is a quantile (critical ratio)
> - Pinball loss defines and evaluates quantile forecasts
> - Calibration and sharpness checks (coverage of P10-P90)
> - Link to safety stock and service-level targets

---
## 8. Hierarchical and Grouped Forecasting: Reconciliation
> 🟠 Tier 2 · _Key points:_ Forecasts at SKU, region and total must add up; bottom-up, top-down, OLS and MinT reconciliation

### Definition
Demand data form **hierarchies** (SKU → category → total; store → city → region) or **groupings** (product × geography). Independent forecasts at each level generally **do not add up** (incoherent). Reconciliation adjusts them to be coherent. Using the summing matrix $S$ (maps bottom-level series $b$ to all series $y=Sb$):

- **Bottom-up:** forecast the bottom level and sum. Unbiased but noisy at low volumes.
- **Top-down:** forecast the total and split by historical proportions. Smooth but loses local detail.
- **Middle-out:** forecast at a middle level then go both ways.
- **Optimal reconciliation:** $\tilde y=S(S'W^{-1}S)^{-1}S'W^{-1}\hat y$; $W=I$ is OLS, and **MinT** (Wickramasuriya, Athanasopoulos and Hyndman, JASA 2019) sets $W$ to the covariance of base forecast errors, giving the minimum-variance coherent forecast. Software: Nixtla `hierarchicalforecast`, R `fabletools`/`hts`.

Coherence matters because planners aggregate: the S&OP total must match the sum of the regional plans ([[120 Integrated Business Planning (IBP) & S&OP Maturity]], [[198 SAP IBP, APO & Demand-Driven Planning]]).

### Example
Total = A + B. Base forecasts: total 100, A 60, B 45 (A + B = 105, incoherent). Bottom-up gives total 105. OLS reconciliation: $S=\begin{pmatrix}1&1\\1&0\\0&1\end{pmatrix}$, $\hat\beta=(S'S)^{-1}S'\hat y=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\begin{pmatrix}160\\145\end{pmatrix}=\begin{pmatrix}58.33\\43.33\end{pmatrix}$, so reconciled forecasts are **A 58.33, B 43.33, total 101.67**: the 5-unit gap is spread across all three forecasts.

```python
import numpy as np
S = np.array([[1,1],[1,0],[0,1]]); yh = np.array([100, 60, 45.])
b = np.linalg.solve(S.T @ S, S.T @ yh); print(b.round(2), (S @ b).round(2))   # [58.33 43.33] [101.67 58.33 43.33]
```

### In the news
See news box. Foundation models forecast each series independently, so a reconciliation step is still needed to make their outputs coherent across the hierarchy.

### Interview angle
> [!question] How it is asked
> "Regional forecasts do not add up to the national forecast. What do you do?"

> [!tip] Strong answer includes
> - Name the options (bottom-up, top-down, MinT) and their trade-offs
> - Reconciliation can improve accuracy, not only coherence
> - Probabilistic reconciliation for quantiles
> - Who owns the number in S&OP (one version of the truth)

---
## 9. Evaluation: Rolling Origin, WAPE, Bias, MASE and Forecast Value Added
> 🟠 Tier 2 · _Key points:_ Time-ordered validation; WAPE instead of MAPE for low volumes; bias; scaled errors; FVA

### Definition
**Rolling-origin (time-series) cross-validation:** repeatedly choose an origin, train on data before it, forecast the next $H$ periods, advance the origin, and average errors. Never shuffle rows. Use at least 3 to 5 origins, covering seasons and promotion periods.

Metrics:
- **WAPE** $=\frac{\sum|A-F|}{\sum A}$: volume-weighted; robust to small denominators.
- **Bias** $=\frac{\sum(F-A)}{\sum A}$: systematic over- (positive) or under-forecast. Planners often track WAPE and bias together.
- **MAPE** $=\frac1n\sum\frac{|A-F|}{A}$: breaks for zeros and overweights tiny volumes.
- **MASE:** MAE divided by the in-sample MAE of the naive (or seasonal-naive) method; unit-free, below 1 means better than naive.
- **RMSE:** penalises large misses; sensitive to outliers.
- **Pinball loss / CRPS** for quantiles; **coverage** for intervals.
- **Forecast Value Added (FVA):** accuracy of each process step relative to the naive forecast; a step with negative FVA should be removed ([[099 ML for Operations & SCM]], [[012 Supply Chain Analytics & KPIs]]).

Aggregate separately by **volume class and variability (ABC/XYZ)**; a single global WAPE hides that the tail is unforecastable.

### Example
Three SKUs, actual 100, 10, 2 and forecast 90, 15, 1. APEs: 10%, 50%, 50%, so **MAPE = 36.7%**; **WAPE** $=\frac{10+5+1}{112}=\mathbf{14.3\%}$; bias $=\frac{(90+15+1)-112}{112}=\mathbf{-5.4\%}$. MAPE is dominated by the two small SKUs that hardly matter in volume; WAPE reflects the business impact.

### In the news
See news box. Good benchmarks now report scaled errors and skill scores with intervals; internal forecast reviews should do the same instead of a single MAPE figure.

### Interview angle
> [!question] How it is asked
> "How do you validate a forecasting model and which metric do you report?"

> [!tip] Strong answer includes
> - Rolling-origin validation, several origins, no leakage
> - WAPE plus bias, MASE for comparisons, pinball for quantiles
> - Segment by volume and intermittency
> - Compare with seasonal naive and report FVA

---
## 10. Intermittent Demand and New-Product Cold Start
> 🟠 Tier 2 · _Key points:_ Croston, SBA and TSB; Tweedie objective; attribute-based forecasts for new SKUs

### Definition
**Intermittent demand** (many zero periods, as for spare parts and slow movers) breaks standard accuracy metrics and smoothing methods. Options: **Croston** (separately smooths demand size and inter-demand interval), **SBA** (a bias-corrected Croston), **TSB** (updates the demand probability each period so obsolescence decays the forecast), or global models with **Tweedie/Poisson/negative-binomial** losses. Evaluate with WAPE aggregated over time, MASE, pinball loss at the stocking quantile, and **service level achieved**, not period-level MAPE.

**Cold start:** for a new SKU use a global model with attributes (category, price, pack size, brand, launch promotion) and similar-item analogues; blend toward the item's own history as data accumulate ([[118 New-Product Forecasting, Demand Sensing & Demand Shaping]]). Foundation models help here as well: zero-shot forecasts from 4 to 8 weeks of history.

### Example
A spare part sells 0, 0, 3, 0, 0, 0, 4, 0 units per week (mean 0.875). A moving-average forecast of 0.875 units will never match any actual week; the stocking decision is better framed with a Poisson or negative-binomial **quantile**: for Poisson with mean 0.875, the P95 of weekly demand is 3 units ($P(X\le2)=0.941$, $P(X\le3)=0.988$), so stock to the 3-unit target for a 95%-ish service level over a one-week lead time.

```python
from scipy import stats
print(stats.poisson.cdf([2, 3], 0.875).round(3))      # [0.941 0.988]
```

### In the news
See news box. Zero-shot models are marketed for cold-start and long-tail series, but intermittent series are exactly where you must verify calibration before trusting them.

### Interview angle
> [!question] How it is asked
> "How would you forecast demand for a spare part that sells twice a year?"

> [!tip] Strong answer includes
> - Do not use MAPE; use a count-based or Croston-family approach and stocking quantiles
> - Pool information across similar parts (global model, analogues)
> - Link to service-level trade-offs and obsolescence risk
> - Criticality-based policy (low-volume, high-impact parts)

---
## 11. M5 Competition: Lessons for Practitioners
> 🟠 Tier 2 · _Key points:_ Walmart data, LightGBM dominance, cross-learning, external variables, ensembles

### Definition
The **M5 competition** (Makridakis Open Forecasting Center, 2020, Kaggle) used **30,490** hierarchical unit-sales series from Walmart (10 stores in California, Texas and Wisconsin) with a 28-day horizon, price, calendar and SNAP-benefit information; **5,507 teams** from 101 countries submitted. Accuracy was scored with a scaled RMSE (WRMSSE), and a separate uncertainty track with scaled pinball loss. Findings reported in the organisers' paper (International Journal of Forecasting, 2022):
- All of the **top 50** submissions were "pure" machine-learning methods; the winner combined many LightGBM models and was **22.4% better** than the best statistical benchmark.
- Only **7.5% of teams (415)** beat the best statistical benchmark: ML is not automatically better.
- **Cross-learning** (one model across many series) outperformed series-by-series modelling.
- **External variables**, especially price and promotion-type information, added value.
- **Simple ensembles** (equal-weight combinations) were highly effective.
- Gains shrank at the finest level: about **40%** better at the total level but only **3%** at the product-store level, because disaggregated demand is noisier.
Source: [M5 accuracy competition paper](https://statmodeling.stat.columbia.edu/wp-content/uploads/2021/10/M5_accuracy_competition.pdf).

### Example
Practical translation: (1) build a good global GBM with price and promo features; (2) combine a few diverse models; (3) always beat the benchmark in a hold-out before celebrating; (4) expect the biggest accuracy gains at aggregate levels and the smallest at the store-SKU-day tail, where inventory policy and safety stock must absorb the noise ([[003 Inventory Management]]).

### In the news
See news box. Foundation-model leaderboards (GIFT-Eval, fev-bench) are the new M-competitions; the M5 lesson to demand strong baselines and honest holdouts applies unchanged.

### Interview angle
> [!question] How it is asked
> "What did we learn from the M5 forecasting competition?"

> [!tip] Strong answer includes
> - ML (LightGBM) won, via cross-learning and external variables
> - Most entrants still lost to statistical benchmarks (7.5% won)
> - Ensembling helps; gains are largest at aggregate levels
> - Caveat: Walmart data, 28-day horizon, a simulated-rich environment; test on your own

---
## 12. When Simple Beats Complex: A Decision Framework
> 🟠 Tier 2 · _Key points:_ Baseline discipline; cost-benefit; model governance; segment before you choose

### Definition
Complex models win when there is signal that simple models cannot use (covariates, cross-series patterns, long-horizon quantiles). They lose when data are short, noisy or stable, when the process is limited by planning latency rather than accuracy, or when explainability matters to planners and auditors. A practical ladder:

1. **Seasonal naive / moving average** (minutes). Always the control.
2. **ETS / Theta / ARIMA** (hours; [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]).
3. **Global LightGBM with features** (days).
4. **Deep model (TFT/DeepAR) or foundation model** (days to weeks; heavier ops).
5. **Ensembles and reconciliation** across all of the above.

Step up only if it adds enough **FVA in ₹**: forecast improvement converts to inventory via safety stock roughly proportional to forecast-error standard deviation, so a 10% cut in error SD gives about a 10% cut in safety stock ([[003 Inventory Management]]). Segment first: stable A-items with long histories (simple models), promoted items (global GBM with promo features), long-tail and new items (zero-shot or global models), intermittent parts (count models).

### Example
Inventory value tied to safety stock: ₹50 crore. A model that reduces forecast-error SD by 8% could free about ₹4 crore (8% of ₹50 crore, a rule-of-thumb estimate assuming safety stock scales linearly with error SD and holding all else constant). If it needs three data scientists and a GPU team costing ₹1.5 crore a year, the net benefit is positive but must be re-checked after the first-year monitoring; if the gain is 1%, stay with the simpler model.

### In the news
See news box. The existence of free zero-shot models shifts the question from "can we build a forecaster?" to "is ours better than a pretrained baseline on our own data?"

### Interview angle
> [!question] How it is asked
> "When would you NOT use machine learning for forecasting?"

> [!tip] Strong answer includes
> - Short or very stable series, few series, no covariates, strict explainability
> - Forecast accuracy is not the bottleneck (lead times, MOQs, policy)
> - Baseline ladder and cost-benefit in ₹
> - Governance: monitoring, fallback, human override

---
## 13. ⭐ Advanced: Productionising Forecasts, Monitoring and Ensembles
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A forecast in production is a **pipeline**, not a model: data validation, feature store, scheduled retraining, forecast generation, reconciliation, publishing to planning systems, and monitoring.
- **Monitoring:** track WAPE and bias by segment against the baseline, interval coverage (P10-P90 should cover about 80%), feature drift (distribution shift of price and promo), and **volume-weighted exception reports**; alert on bias because systematic over-forecasting builds inventory.
- **Retraining cadence:** weekly or monthly for GBMs; zero-shot models need no retraining but should be re-benchmarked when new versions appear (TimesFM 2.5 to 3.0 changed size, licence and capabilities within a year).
- **Ensembles:** averaging a GBM and a foundation model usually reduces error because their mistakes differ; weights can be chosen on rolling origins by segment.
- **Human-in-the-loop:** planners override for known events; log overrides and measure their FVA.
- **Governance:** model registry, versioned weights and licences, data lineage, and fallback to the baseline on failure; see [[220 Responsible AI, Explainability & Model Governance]] for drift metrics (PSI, KS) and documentation, and [[099 ML for Operations & SCM]] for MLOps for operations.
- **Decision link:** pass quantiles (not means) to inventory and capacity optimisers ([[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]).

### Example
Monitoring rule for the simulated retailer: weekly volume-weighted bias beyond ±5% for two consecutive weeks triggers a review; P10-P90 coverage below 70% or above 90% triggers recalibration (conformal adjustment or quantile re-fit); PSI above 0.25 on the price feature triggers retraining. A simple **conformal** fix for coverage: compute residuals on a recent calibration window and widen the interval by the empirical 90th-percentile residual.

```python
import numpy as np
# split-conformal widening: calib_resid = actual - median_forecast on a recent window
def conformal_interval(median_fc, calib_resid, alpha=0.2):
    lo, hi = np.quantile(calib_resid, [alpha/2, 1 - alpha/2])
    return median_fc + lo, median_fc + hi
```

### In the news
See news box. As zero-shot models proliferate, versioning, licensing and re-benchmarking become part of the forecasting team's routine.

### Interview angle
> [!question] How it is asked
> "Your forecast was accurate in testing but the business says it is wrong now. How do you investigate?"

> [!tip] Strong answer includes
> - Check data pipeline and drift first, then bias by segment, then model
> - Compare with the baseline in production (FVA) and look at override behaviour
> - Interval coverage and recalibration
> - Process fixes: monitoring dashboard, retraining policy, fallback and ownership
> - Practice questions in [[215 Statistics Interview Question Bank & Numericals]] and tooling in [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]]
