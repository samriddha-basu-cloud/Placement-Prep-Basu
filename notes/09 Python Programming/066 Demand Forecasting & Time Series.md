---
tags: [python-programming, tier1]
area: Python Programming
topic: "Demand Forecasting & Time Series"
tier: Tier 1
roles: Operations / PM
status: complete
subtopics: 12
---
# Demand Forecasting & Time Series

⬅ [[065 Data Visualization (Matplotlib-Seaborn-Plotly)]] · [[_Index - Python Programming|Python Programming]] · [[067 Statistical Analysis in Python]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / PM

## Sub-topics in this note
1. [[#1. Time Series Components]]
2. [[#2. pandas resample()]]
3. [[#3. Rolling Average in Python]]
4. [[#4. Exponential Smoothing (statsmodels)]]
5. [[#5. ARIMA Model]]
6. [[#6. Facebook Prophet]]
7. [[#7. Train-Test Split for TS]]
8. [[#8. Forecast Error Calculation]]
9. [[#9. ACF & PACF Plots]]
10. [[#10. Seasonal Decompose]]
11. [[#11. ⭐ Advanced: Stationarity, SARIMA & Model Selection]]
12. [[#12. ⭐ Advanced: Bias, Tracking Signal, Intermittent Demand & S&OP Link]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Foundation models arrive in forecasting
> **Google's TimesFM.** Google Research's time-series foundation model is a decoder-only model with about **200 million parameters**, pretrained on **100 billion real-world time points** (Google Trends, Wikipedia page views and synthetic ARMA data). It is reported to beat other state-of-the-art models in **zero-shot** forecasting (no training on the target series), supporting the claim that scaling laws apply to Transformer forecasters. It follows Nixtla's **TimeGPT** (debuted August 2023), which Nixtla has since followed with TimeGPT-2 and 2.1 announcements. (The source does not give an exact TimesFM announcement date.) ([Source](https://aihorizonforecast.substack.com/p/timesfm-googles-foundation-model), [Nixtla](https://www.nixtla.io/blog/timegpt-2-announcement))
> 
> **The classical toolkit is still the baseline.** pandas 3.0 (21 Jan 2026) changed the default datetime resolution away from nanoseconds, widening the date range time-series code can represent, and NumPy 2.5.0 shipped on 21 Jun 2026. ([pandas](https://pandas.pydata.org/community/blog/pandas-3.0.html), [NumPy](https://numpy.org/news/))
> 
> Sub-topics that say **"See news box"** reuse these items. I could not verify benchmark numbers for foundation models beyond what is stated above, so treat their accuracy claims as vendor/paper claims.

---
## 1. Time Series Components
> 🔴 Tier 1 · _Tracker hint:_ Trend, Seasonality, Cyclical, Irregular/Noise — decomposition

### Definition
A **time series** is a sequence of observations ordered in time at regular intervals. It is usually modelled as a combination of:

| Component | Meaning | Typical example |
|---|---|---|
| **Trend (T)** | Long-run upward/downward movement | Rising smartphone demand |
| **Seasonality (S)** | Fixed-period repeating pattern (week, month, year) | Diwali peak, summer beverages |
| **Cyclical (C)** | Irregular multi-year swings tied to economy/business cycles | Auto demand through the cycle |
| **Irregular / noise (R)** | Random, unpredictable residual | Weather event, one-off order |

**Additive:** $y_t = T_t + S_t + R_t$ (seasonal swing roughly constant in size).
**Multiplicative:** $y_t = T_t \times S_t \times R_t$ (seasonal swing grows with the level; common in sales).
Seasonality has a *fixed, known* period; cycles do not. Log-transforming a multiplicative series makes it additive. Forecasting works by estimating the predictable components (T, S) and treating R as uncertainty.

### Example
Trend level 200 units, December seasonal index 1.10. Multiplicative: 200 x 1.10 = 220. Additive equivalent: seasonal effect +20, so 200 + 20 = 220. If the trend grows to 300 the multiplicative December value is 330 (a +30 swing) but the additive one stays 320, which is why sales with growth need the multiplicative form.

### In the news
See news box. Foundation models like TimesFM claim to learn trend and seasonality patterns from pretraining across many series rather than fitting each series separately.

### Interview angle
> [!question] How it is asked
> "What patterns do you look for in demand data before choosing a forecast method?"

> [!tip] Strong answer includes
> - All four components with business examples
> - Additive vs multiplicative and how to tell (seasonal amplitude grows with level)
> - Seasonality (fixed period) vs cycle (irregular length)
> - Method choice follows components: no trend/seasonality, then SES; trend, then Holt; both, then Holt-Winters/SARIMA

---

## 2. pandas resample()
> 🔴 Tier 1 · _Tracker hint:_ df.resample('M').sum() — aggregate to monthly; 'Q'=quarterly, 'W'=weekly

### Definition
`resample` is a time-based `groupby`: it changes the **frequency** of a series with a `DatetimeIndex` (or `on="date"`). **Downsampling** aggregates (daily to monthly); **upsampling** creates new timestamps that need filling.

```python
df["date"] = pd.to_datetime(df["date"])
s = df.set_index("date")["sales"]
s.resample("W").sum()           # weekly (week ending Sunday)
s.resample("MS").sum()          # month-start; 'ME' = month-end
s.resample("QS").sum()          # quarterly; 'YS' yearly
s.resample("ME").agg(["sum", "mean", "max"])
s.resample("D").asfreq().fillna(0)   # reveal missing days
s.resample("h").interpolate()        # upsample + interpolate
```
Older code uses `'M'`, `'Q'`; recent pandas versions deprecated those aliases in favour of `'ME'`, `'QE'`. Use `sum` for flows (sales), `mean`/`last` for levels (price, inventory). Missing dates should be filled (often with 0 for sales) before modelling so the series is regular.

### Example
Daily sales for 90 days (Jan to Mar) with `resample("ME").sum()` produces 3 rows. If 31 days sum to 12,400 in January, 28 in February to 11,200, and 31 in March to 13,950, then average per day is 400, 400 and 450 respectively: using sums alone would understate February because it has fewer days, so compare per-day averages too.

### In the news
See news box. pandas 3.0's datetime changes affect how frequencies and resolutions are inferred, so pin versions and check date dtypes after upgrading.

### Interview angle
> [!question] How it is asked
> "Your data is daily but S&OP plans monthly. How do you prepare it?"

> [!tip] Strong answer includes
> - Aggregation rule matches the metric (sum vs mean vs last)
> - Handles missing dates and unequal month lengths
> - Chooses the planning bucket to match decision horizon
> - Mentions fiscal calendar (India FY starts April)

---

## 3. Rolling Average in Python
> 🔴 Tier 1 · _Tracker hint:_ df['ma3'] = df['sales'].rolling(3).mean() — 3-period moving average

### Definition
A **simple moving average (SMA)** of window $w$ averages the last $w$ observations; as a forecast: $\hat{y}_{t+1} = \frac{1}{w}\sum_{i=0}^{w-1} y_{t-i}$.

```python
df["ma3"] = df["sales"].rolling(3).mean()           # first 2 rows NaN
df["ma3_fc"] = df["ma3"].shift(1)                    # forecast for t uses data to t-1
df["wma"] = df["sales"].rolling(3).apply(lambda x: (x * [1, 2, 3]).sum() / 6)  # weighted
df["ewm"] = df["sales"].ewm(alpha=0.3, adjust=False).mean()
```
Larger window = smoother but slower to react; smaller window = responsive but noisy. SMA lags trends and cannot model seasonality. Use `shift(1)` so a "forecast" for period $t$ never contains $y_t$ (look-ahead leakage).

### Example
Sales 100, 110, 120, 130. 3-period MAs: (100+110+120)/3 = 110 and (110+120+130)/3 = 120. Forecast for next period = 120, while the series is actually rising by 10 per period, so the SMA lags (the true trend would predict 140), showing why SMA underforecasts a trend.

### In the news
See news box. Moving averages are still the sanity-check baseline that any model, including foundation models, must beat.

### Interview angle
> [!question] How it is asked
> "How would you build a simple baseline forecast?" or "What are the weaknesses of a moving average?"

> [!tip] Strong answer includes
> - Formula and trade-off of window length
> - Lag with trend; no seasonality handling
> - `shift` to avoid leakage when evaluating
> - Compares against naive and seasonal-naive baselines

---

## 4. Exponential Smoothing (statsmodels)
> 🔴 Tier 1 · _Tracker hint:_ from statsmodels.tsa.holtwinters import ExponentialSmoothing; fit model; forecast

### Definition
Exponential smoothing weights recent data more with geometrically decaying weights.

- **Simple (SES):** $\hat{y}_{t+1} = \alpha y_t + (1-\alpha)\hat{y}_t$, for series with no trend/seasonality; $0<\alpha<1$ (high = reactive).
- **Holt (trend):** adds a level and trend equation (parameters $\alpha, \beta$).
- **Holt-Winters (seasonal):** adds seasonal factors ($\alpha,\beta,\gamma$), additive or multiplicative.

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing
fit = ExponentialSmoothing(train, trend="add", seasonal="mul",
                           seasonal_periods=12).fit()
fc = fit.forecast(6)                  # next 6 periods
print(fit.params, fit.aic)
ses = SimpleExpSmoothing(train).fit(smoothing_level=0.3, optimized=False)
```
The index should have a regular frequency (`train.index.freq = "MS"`). Use `seasonal="mul"` when seasonal amplitude grows with level (requires positive data). Parameters are estimated by minimising SSE.

### Example
SES with $\alpha=0.3$, actuals 100, 110, 120, initial forecast 100. F2 = 0.3(100)+0.7(100) = 100; F3 = 0.3(110)+0.7(100) = 103; F4 = 0.3(120)+0.7(103) = 36+72.1 = 108.1. Note the lag behind the rising actuals, which is why Holt (with trend) is needed here.

### In the news
See news box. Exponential smoothing and ARIMA remain strong baselines that foundation models are benchmarked against.

### Interview angle
> [!question] How it is asked
> "Which exponential smoothing variant would you use for monthly sales with growth and seasonality?"

> [!tip] Strong answer includes
> - SES vs Holt vs Holt-Winters by components present
> - Role of alpha (reactivity) and additive vs multiplicative choice
> - Code skeleton with fit/forecast on a train set
> - Evaluates on a holdout, compares to a naive baseline

---

## 5. ARIMA Model
> 🔴 Tier 1 · _Tracker hint:_ from statsmodels.tsa.arima.model import ARIMA; model = ARIMA(data,order=(p,d,q)).fit()

### Definition
**ARIMA(p, d, q)** models a series with:
- **AR(p):** current value depends on its past $p$ values: $y_t = c + \phi_1 y_{t-1}+\dots+\phi_p y_{t-p}+\varepsilon_t$
- **I(d):** differencing $d$ times to make the series **stationary** (constant mean/variance, no trend)
- **MA(q):** depends on past $q$ forecast errors: $\varepsilon_t + \theta_1\varepsilon_{t-1}+\dots$

```python
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(train, order=(1, 1, 1)).fit()
print(model.summary())            # coefficients, AIC, diagnostics
fc = model.get_forecast(steps=6)
mean = fc.predicted_mean
ci = fc.conf_int()                # prediction interval
model.forecast(6)                 # quick point forecast
```
Seasonal version: `SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12))`. Pick orders from ACF/PACF plots and compare **AIC/BIC** (lower is better); check residuals look like white noise (Ljung-Box test). Requires a stationary series after differencing.

### Example
ARIMA(0,1,0) is a random walk: $y_t = y_{t-1}+\varepsilon_t$, so the forecast is the last value (the naive forecast). If the last observation is 150, every future point forecast is 150 but the prediction interval widens with horizon. A (1,1,0) model adds an autoregressive term on the differences.

### In the news
See news box. Even with foundation models available, ARIMA/ETS remain the explainable baseline expected in a business setting.

### Interview angle
> [!question] How it is asked
> "Explain ARIMA in simple terms and how you pick p, d, q."

> [!tip] Strong answer includes
> - Plain-language meaning of AR, I, MA
> - Stationarity and differencing; ADF test
> - Order selection by ACF/PACF and AIC; residual diagnostics
> - Limitations: single series, linear, needs seasonal extension; compare with ETS/Prophet

---

## 6. Facebook Prophet
> 🔴 Tier 1 · _Tracker hint:_ from prophet import Prophet; m.fit(df); future = m.make_future_dataframe(30); m.predict(future)

### Definition
**Prophet** (developed at Facebook/Meta, now the open-source `prophet` package) is an additive regression model: $y(t) = g(t) + s(t) + h(t) + \varepsilon_t$, i.e. piecewise **trend**, multiple **seasonalities** (yearly, weekly via Fourier terms) and **holiday** effects. It handles missing data and outliers fairly robustly and needs little tuning.

```python
from prophet import Prophet
df = df.rename(columns={"date": "ds", "sales": "y"})      # required column names
m = Prophet(yearly_seasonality=True, weekly_seasonality=True,
            seasonality_mode="multiplicative")
m.add_country_holidays(country_name="IN")
m.add_regressor("promo")                                  # optional extra variable
m.fit(df)
future = m.make_future_dataframe(periods=30)              # +30 days (freq="D")
fc = m.predict(future)
fc[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail()
m.plot(fc); m.plot_components(fc)
```
Good for daily business data with strong seasonality and holidays (festivals). It is less suited to short series or when sophisticated dynamics matter. Validate with `prophet.diagnostics.cross_validation`.

### Example
For 2 years of daily sales with weekly and annual patterns, `make_future_dataframe(30)` extends the dates by 30 days and `predict` returns `yhat` (forecast) with 80% interval by default (`yhat_lower`, `yhat_upper`). Adding Indian holidays (Diwali) as events typically captures spikes that a plain ARIMA misses.

### In the news
See news box. Prophet represents the "practitioner-friendly" approach; foundation models aim to be even more plug-and-play, zero-shot.

### Interview angle
> [!question] How it is asked
> "When would you choose Prophet over ARIMA?"

> [!tip] Strong answer includes
> - Decomposable model: trend + seasonality + holidays
> - `ds`/`y` format and `make_future_dataframe`
> - Strengths (holidays, missing data, ease) and weaknesses (not for short or highly autocorrelated series)
> - Still evaluates on a time-based holdout against a baseline

---

## 7. Train-Test Split for TS
> 🔴 Tier 1 · _Tracker hint:_ Split by time (not random); last N periods = test; no shuffle

### Definition
Time series have temporal dependence, so a random split lets the model "see the future" (**data leakage**) and gives falsely good scores. Always split **chronologically**, with the test set after the training set.

```python
n_test = 6
train, test = df.iloc[:-n_test], df.iloc[-n_test:]       # last 6 periods = test
# better: rolling-origin validation
from sklearn.model_selection import TimeSeriesSplit
tscv = TimeSeriesSplit(n_splits=5)
for tr_idx, te_idx in tscv.split(X):
    ...                                                  # train always before test
```
Test length should equal the **forecast horizon** you care about. Rolling-origin (walk-forward) cross-validation repeats the process over several cut-offs for a more reliable estimate. Fit scalers/feature engineering only on training data. After choosing the model, **refit on all data** before the real forecast.

### Example
36 months of data (Jan 2023 to Dec 2025) and a 6-month planning horizon: train on months 1-30, test on months 31-36. A random 80/20 split would put some of 2025 in training and test on 2024 months, making the model look much better than it will be in production.

### In the news
See news box. Benchmarks of foundation models stress that they were evaluated on data after the training period to avoid leakage, the same principle.

### Interview angle
> [!question] How it is asked
> "Why can't you use `train_test_split` with shuffle on time series?"

> [!tip] Strong answer includes
> - Leakage explanation and temporal order
> - Test window equals business horizon
> - Walk-forward / `TimeSeriesSplit` for robustness
> - Refit on full data for the final forecast

---

## 8. Forecast Error Calculation
> 🔴 Tier 1 · _Tracker hint:_ from sklearn.metrics import mean_absolute_error, mean_squared_error; np.sqrt(mse) for RMSE

### Definition
With actuals $A_t$, forecasts $F_t$, error $e_t = A_t - F_t$:

| Metric | Formula | Notes |
|---|---|---|
| Bias (ME) | $\frac{1}{n}\sum e_t$ | Sign shows over/under-forecasting |
| MAE | $\frac{1}{n}\sum \lvert e_t\rvert$ | Same units, robust |
| MSE / RMSE | $\frac{1}{n}\sum e_t^2$, $\sqrt{MSE}$ | Penalises big misses |
| MAPE | $\frac{100}{n}\sum \frac{\lvert e_t\rvert}{A_t}$ | Fails when $A_t$ is 0 |
| WAPE | $\frac{\sum \lvert e_t\rvert}{\sum A_t}$ | Volume-weighted; handles zeros |

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_true, y_pred)
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
```
Compare to a naive benchmark (MASE < 1 means better than naive).

### Example
Actual 100, 120, 110; forecast 90, 125, 100. Errors +10, -5, +10. MAE = 25/3 = 8.33. MSE = (100+25+100)/3 = 75, RMSE = 8.66. MAPE = (10/100 + 5/120 + 10/110)/3 = (0.1000+0.0417+0.0909)/3 = 7.75%. Bias = 15/3 = +5 (under-forecasting on average).

### In the news
See news box. Foundation-model claims are always stated on an error metric over specific benchmarks, so know which metric a claim uses.

### Interview angle
> [!question] How it is asked
> "Which error metric would you report to the business, and why?"

> [!tip] Strong answer includes
> - MAE/WAPE for interpretability, RMSE when big misses are costly
> - MAPE pitfalls with zeros and asymmetric penalties
> - Bias reported separately from accuracy
> - Benchmarks vs naive; ties error to safety stock and service level

---

## 9. ACF & PACF Plots
> 🔴 Tier 1 · _Tracker hint:_ from statsmodels.graphics.tsaplots import plot_acf, plot_pacf — for ARIMA order selection

### Definition
- **ACF (autocorrelation function):** correlation of the series with its own lag $k$ (direct plus indirect effects).
- **PACF (partial ACF):** correlation at lag $k$ after removing the effect of intermediate lags (the direct effect).

```python
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
fig, ax = plt.subplots(2, 1, figsize=(10, 6))
plot_acf(diffed, lags=24, ax=ax[0])
plot_pacf(diffed, lags=24, ax=ax[1], method="ywm")
plt.show()
```
Bars outside the shaded band (approximately $\pm 1.96/\sqrt{n}$) are significant.

| Pattern | Suggests |
|---|---|
| PACF cuts off after lag p, ACF decays | AR(p) |
| ACF cuts off after lag q, PACF decays | MA(q) |
| Both decay | ARMA (mixed) |
| Slowly decaying ACF | Non-stationary; difference it |
| Spikes at 12, 24 (monthly) | Seasonality; use seasonal terms |

### Example
After first differencing, the PACF has a single significant spike at lag 1 and the ACF decays gradually, so try ARIMA(1,1,0). If instead the ACF has one spike at lag 1 and the PACF decays, try ARIMA(0,1,1). Choose among candidates by AIC and residual checks.

### In the news
See news box. Automated order search (`pmdarima`'s `auto_arima`, statsforecast) is common, but interviewers still ask you to read ACF/PACF by hand.

### Interview angle
> [!question] How it is asked
> "How do you decide the AR and MA order from these plots?"

> [!tip] Strong answer includes
> - Definitions of ACF vs PACF
> - The cut-off vs decay rules
> - Plot after differencing and check seasonal lags
> - Treat as a guide; confirm with AIC and residuals

---

## 10. Seasonal Decompose
> 🔴 Tier 1 · _Tracker hint:_ from statsmodels.tsa.seasonal import seasonal_decompose; plot trend/seasonal/residual

### Definition
`seasonal_decompose` splits a series into **trend**, **seasonal** and **residual** by classical moving-average decomposition.

```python
from statsmodels.tsa.seasonal import seasonal_decompose, STL
res = seasonal_decompose(s, model="multiplicative", period=12)
res.plot()                       # observed, trend, seasonal, resid
res.trend; res.seasonal; res.resid
stl = STL(s, period=12, robust=True).fit()    # more flexible, robust to outliers
seasonal_index = res.seasonal[:12]           # monthly seasonal factors
deseasonalised = s / res.seasonal            # multiplicative
```
Needs at least two full seasonal cycles and a regular index. Trend values are NaN at the ends (centred moving average). Choose `additive` or `multiplicative`; multiplicative requires positive data. STL handles changing seasonality and outliers better.

### Example
Monthly sales: trend 200, seasonal index for December 1.25 (multiplicative). Expected December = 200 x 1.25 = 250. Deseasonalising an actual December of 275 gives 275/1.25 = 220, which shows the underlying level has risen above 200 once the festive effect is removed.

### In the news
See news box. Decomposition is the interpretable step that makes forecasts defensible to a business audience, even when black-box models do the final prediction.

### Interview angle
> [!question] How it is asked
> "How would you separate festival seasonality from the underlying growth in sales?"

> [!tip] Strong answer includes
> - Additive vs multiplicative choice and reason
> - Reads seasonal indices as business insight
> - Needs enough cycles; mentions STL for robustness
> - Uses deseasonalised data to judge true performance

---

## 11. ⭐ Advanced: Stationarity, SARIMA & Model Selection
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A series is **(weakly) stationary** if its mean, variance and autocovariance do not change over time. ARIMA requires it.

- **ADF test** (Augmented Dickey-Fuller): null = unit root (non-stationary). p < 0.05 rejects the null, so treat as stationary. **KPSS** has the reverse null.
- **Remedies:** first difference (trend), seasonal difference $y_t - y_{t-m}$, log transform (variance).
- **SARIMA** $(p,d,q)(P,D,Q)_m$ handles seasonality; $m=12$ monthly, 7 daily-weekly.
- **Selection:** AIC/BIC, rolling-origin CV; **residuals** should be white noise (Ljung-Box).

```python
from statsmodels.tsa.stattools import adfuller
stat, p, *_ = adfuller(s.dropna())
if p > 0.05: s_d = s.diff().dropna()
from statsmodels.tsa.statespace.sarimax import SARIMAX
fit = SARIMAX(train, order=(1,1,1), seasonal_order=(0,1,1,12)).fit(disp=False)
fit.forecast(6)
```
Model families to compare: naive, seasonal naive, ETS, ARIMA/SARIMA, Prophet, gradient boosting on lag features, and foundation models.

### Example
Monthly sales trending upward with ADF p = 0.78: not stationary. After first differencing p = 0.01: stationary, so d = 1. The seasonal naive baseline (forecast = value 12 months ago) must be beaten; if SARIMA's RMSE is 8.5 versus 12.0 for seasonal naive, it improves error by about 29% (3.5/12).

### In the news
See news box. Zero-shot foundation models claim to skip this stationarity and tuning workflow, but are judged against exactly these classical baselines.

### Interview angle
> [!question] How it is asked
> "How do you know if your series is stationary and what do you do if not?"

> [!tip] Strong answer includes
> - Visual check plus ADF/KPSS with null hypotheses stated correctly
> - Differencing, seasonal differencing, log
> - SARIMA notation and residual checks
> - Always benchmarks against naive/seasonal naive

---

## 12. ⭐ Advanced: Bias, Tracking Signal, Intermittent Demand & S&OP Link
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Forecasting in operations is judged by decisions, not just error scores.

- **Tracking signal** = RSFE / MAD, where RSFE = cumulative sum of errors and MAD = mean absolute deviation. Persistently beyond about $\pm 4$ (a common rule of thumb) signals bias and a model needing review.
- **Forecast Value Added (FVA):** does each step (statistical forecast, planner override) improve on the naive forecast?
- **Intermittent / lumpy demand** (spare parts, slow movers): use **Croston's method** or SBA, which smooth demand size and interval separately; MAPE is meaningless with many zeros, so use WAPE/MASE.
- **Safety stock from forecast error:** $SS = z \cdot \sigma_e \sqrt{L}$ where $\sigma_e$ is the forecast-error standard deviation per period (RMSE) and L is the lead time in periods.
- **Hierarchies:** forecast at SKU-store, aggregate to SKU-region; top-down vs bottom-up vs reconciliation.
- **Exogenous drivers:** price, promotions, weather, festival dates.
- **Forecast at the right level:** aggregate forecasts are more accurate than item-level (risk pooling).

### Example
Monthly RMSE 40 units, lead time 4 months, service level 95% (z = 1.65): $SS = 1.65 \times 40 \times \sqrt{4} = 132$ units. Cutting RMSE to 30 through better forecasting gives $1.65 \times 30 \times 2 = 99$ units, a 25% reduction in safety stock (33/132), which is the business case for forecasting improvement.

### In the news
See news box. As accuracy claims from new models compete, ops leaders ask for FVA and inventory impact, not just lower RMSE.

### Interview angle
> [!question] How it is asked
> "Our forecast accuracy is 70%. How do you improve it, and what is it worth?"

> [!tip] Strong answer includes
> - Diagnose by segment (SKU class, horizon, bias vs noise) before changing models
> - Baseline, FVA and tracking signal
> - Right method per demand pattern (Croston for intermittent)
> - Translate improvement into safety stock, service level and working capital

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
