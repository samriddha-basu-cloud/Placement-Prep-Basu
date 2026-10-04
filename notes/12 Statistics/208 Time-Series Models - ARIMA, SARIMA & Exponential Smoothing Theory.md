---
tags: [statistics, tier1]
area: Statistics
topic: "Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory"
tier: Tier 1
roles: Operations / Analytics / Consulting
status: complete
subtopics: 14
---
# Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory

⬅ [[207 Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis]] · [[_Index - Statistics|Statistics]] · [[209 Generalised Linear Models & Categorical Data Analysis]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Analytics / Consulting

## Sub-topics in this note
1. [[#1. Time-Series Components and Stationarity]]
2. [[#2. Unit-Root Tests: ADF and KPSS]]
3. [[#3. Differencing and Transformations]]
4. [[#4. AR, MA, ARMA and ARIMA Models]]
5. [[#5. Identification with ACF and PACF (Worked)]]
6. [[#6. Box-Jenkins Methodology]]
7. [[#7. SARIMA: Seasonal ARIMA (Worked Example)]]
8. [[#8. Residual Diagnostics and the Ljung-Box Test]]
9. [[#9. Exponential Smoothing and the ETS Framework]]
10. [[#10. Holt-Winters: Additive vs Multiplicative]]
11. [[#11. Forecast Intervals and Uncertainty]]
12. [[#12. Model Comparison: AIC/BIC, Time-Series Cross-Validation and Accuracy Metrics]]
13. [[#13. ARIMAX and Regression with ARIMA Errors]]
14. [[#14. ⭐ Advanced: GARCH and Volatility Models (Overview)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Foundation models challenge ARIMA, and India rebases its inflation series
> **Amazon's Chronos tokenises time series (arXiv March 2024).** Chronos scales and quantises values into tokens and trains T5-family language models (20M to 710M parameters) with a cross-entropy loss. Evaluated on 42 datasets against classical statistical and deep-learning methods, it beat competitors on datasets seen in pretraining and showed "comparable and occasionally superior" zero-shot performance on new datasets. The classical baselines in these benchmarks are ARIMA and exponential smoothing, so you need to know them well enough to say when they still win. ([arXiv 2403.07815](https://arxiv.org/abs/2403.07815))
>
> **Google's TimesFM (arXiv October 2023, final version April 2024).** A decoder-only, patch-based attention model pretrained on a large time-series corpus; the authors report out-of-the-box zero-shot accuracy approaching that of supervised models trained on each individual dataset, across varying history lengths, horizons and granularities. ([arXiv 2310.10688](https://arxiv.org/abs/2310.10688))
>
> **India's CPI moves to base 2024 (February 2026).** MoSPI's revised series shifts the base from 2012 to 2024 using the 2023-24 Household Consumption Expenditure Survey; food and beverages weight falls from 45.86% to 36.75%. January 2026 inflation on the new series was 2.75% against 1.3% for December 2025 on the old series, a reminder that a base revision creates a structural break that must be handled (linking factors, level shift dummies) before fitting any ARIMA. ([Upstox explainer of the MoSPI release](https://upstox.com/learning-center/personal-finance/what-changed-in-indias-new-cpi-series-and-how-it-impacts-the-economy-and-inflation/article-1518/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Time-Series Components and Stationarity
> 🔴 Tier 1 · _Key points:_ Trend, seasonality, cycle, noise; weak stationarity (constant mean, variance, autocovariance depends only on lag); random walk is non-stationary

### Definition
A time series is a sequence of observations ordered in time, usually modelled as trend + seasonality + irregular components (additive $y_t=T_t+S_t+e_t$ or multiplicative $y_t=T_t\times S_t\times e_t$; logs turn multiplicative into additive). Classical decomposition and moving averages are in [[066 Demand Forecasting & Time Series]] and [[004 Demand Forecasting & Planning]]; this note covers the model-based theory.

**Weak stationarity:** constant mean, constant variance, and autocovariance $\gamma(k)=\text{Cov}(y_t,y_{t+k})$ that depends only on the lag $k$. ARMA theory needs stationarity. A **random walk** $y_t=y_{t-1}+e_t$ is non-stationary (variance grows like $t\sigma^2$), but its first difference is white noise: it has a **unit root**, is "integrated of order 1", I(1). Shocks to a stationary series fade; shocks to an I(1) series are permanent. Regressing one trending series on another produces spurious regression (high $R^2$, meaningless) unless the series are cointegrated. See also [[090 Regression Analysis]].

### Example
Monthly demand rising from 1,000 by 8 units a month with a December peak is non-stationary in the mean (trend) and in seasonal pattern. After taking one regular and one seasonal difference the series fluctuates around a stable level, which is what ARMA machinery can model. A white-noise forecast error series is stationary by construction and is the target for model residuals.

### In the news
See news box. A CPI base revision is a structural break that violates constant-mean stationarity in the spliced series; splice with official linking factors or model the break explicitly.

### Interview angle
> [!question] How it is asked
> "Why does stationarity matter for time-series models, and how do you check it?"

> [!tip] Strong answer includes
> - Constant mean, variance and lag-dependent autocovariance; models estimate stable relationships only if they exist
> - Check by plotting, ACF decay, and ADF/KPSS tests; fix by differencing, log, seasonal differencing
> - Spurious regression risk with trending series

---
## 2. Unit-Root Tests: ADF and KPSS
> 🔴 Tier 1 · _Key points:_ ADF H0 = unit root (non-stationary); KPSS H0 = stationary; use both; trend/constant specification matters

### Definition
**Augmented Dickey-Fuller (ADF):** regress $\Delta y_t=\alpha+\beta t+\gamma y_{t-1}+\sum\delta_i\Delta y_{t-i}+e_t$. H0: $\gamma=0$ (unit root, non-stationary). A small p-value rejects H0 and supports stationarity. The test has low power against near-unit-root series, so a "fail to reject" is weak evidence of a unit root. **KPSS** reverses the roles: H0 stationary (around a constant or trend), H1 unit root. Combining: ADF rejects and KPSS does not reject, then stationary; ADF does not reject and KPSS rejects, then non-stationary, difference; both reject or neither rejects is ambiguous (try trend-stationarity, structural break tests, Phillips-Perron). Choose the deterministic term (constant, or constant and trend) to match the plot, and the lag length by AIC.

### Example
Executed in statsmodels on 200 simulated points (seed 2024):

| Series | ADF stat | ADF p | KPSS stat | KPSS p | Verdict |
|---|---|---|---|---|---|
| AR(1), $\phi=0.7$ | -5.37 | 0.000004 | 0.145 | above 0.10 | stationary |
| Random walk | -1.32 | 0.62 | 0.589 | 0.024 | unit root |
| Differenced random walk | -13.42 | about 0 | | | stationary |

For 84 months of trending seasonal demand, ADF on the level gives p = 0.895 (unit root not rejected); after one regular plus one seasonal difference p = 0.022. Code: `adfuller(x, autolag='AIC')`, `kpss(x, regression='c', nlags='auto')`.

### In the news
See news box. Inflation indices and prices are classic I(1) series; analysts usually model inflation rates (differences of logs) rather than levels.

### Interview angle
> [!question] How it is asked
> "ADF p-value is 0.3. What does that tell you and what next?"

> [!tip] Strong answer includes
> - Cannot reject a unit root; series likely non-stationary or the test lacks power
> - Confirm with KPSS and a plot, then difference (and re-test), considering trend-stationary alternatives
> - Warn against over-differencing, which inflates variance and induces negative autocorrelation

---
## 3. Differencing and Transformations
> 🔴 Tier 1 · _Key points:_ $\nabla y_t=y_t-y_{t-1}$; seasonal difference $y_t-y_{t-m}$; log/Box-Cox to stabilise variance; back-transform forecasts

### Definition
**First difference** $\nabla y_t=y_t-y_{t-1}$ removes a stochastic (or linear) trend; a second difference removes a quadratic trend (rarely needed). **Seasonal difference** $\nabla_my_t=y_t-y_{t-m}$ ($m=12$ for monthly, 7 for daily-with-weekday, 52 for weekly) removes stable seasonality. The backshift operator $B y_t=y_{t-1}$ gives $\nabla=1-B$, $\nabla_m=1-B^m$. **Variance-stabilising transforms:** log (when variance grows with level, as in multiplicative seasonality) or Box-Cox with $\lambda$; forecasts must be back-transformed, with a small bias correction for means. Typical order: transform, then seasonal difference, then regular difference if still needed; difference as little as possible. After differencing a series $d$ times the model is $\text{ARIMA}(p,d,q)$.

### Example
Seasonal demand (monthly) trending up: level ADF p = 0.895. One regular difference gives p about $4\times10^{-12}$ but the seasonal pattern remains in the ACF; adding a seasonal difference yields a series whose ACF shows only two clear spikes (lag 1 about -0.42 and lag 12 about -0.32), which points at a $(0,1,1)(0,1,1)_{12}$ model (see sub-topic 7). Working in logs makes the December peak a constant percentage rather than a growing absolute amount.

### In the news
See news box. Foundation models like Chronos and TimesFM internally scale each series (a form of normalisation), but for ARIMA the analyst must do the transformation explicitly.

### Interview angle
> [!question] How it is asked
> "How do you handle trend and seasonality before ARIMA?"

> [!tip] Strong answer includes
> - Log if variance grows with level; seasonal difference for stable seasonality; regular difference for trend
> - Confirm with ADF/KPSS and ACF; avoid over-differencing
> - Remember to invert the transformation for business-unit forecasts

---
## 4. AR, MA, ARMA and ARIMA Models
> 🔴 Tier 1 · _Key points:_ AR(p): regress on own lags; MA(q): on past shocks; ARIMA(p,d,q) = ARMA on d-differenced series; stationarity and invertibility

### Definition
$$\text{AR}(p):\ y_t=c+\phi_1y_{t-1}+\dots+\phi_py_{t-p}+e_t,\qquad \text{MA}(q):\ y_t=\mu+e_t+\theta_1e_{t-1}+\dots+\theta_qe_{t-q}$$

**ARMA(p,q)** combines both; **ARIMA(p,d,q)** applies ARMA to the $d$-times differenced series. Conditions: AR roots outside the unit circle (for AR(1), $|\phi|<1$) for stationarity; MA roots outside the unit circle for invertibility. Key properties: AR(1) has mean $c/(1-\phi)$, variance $\sigma^2/(1-\phi^2)$ and $\rho_k=\phi^k$. MA(1) has $\rho_1=\theta/(1+\theta^2)$ and $\rho_k=0$ for $k\ge2$. ARIMA(0,1,1) is equivalent to simple exponential smoothing with $\alpha=1+\theta$; ARIMA(0,2,2) corresponds to Holt's method. Special cases: ARIMA(0,1,0) is the random walk (the naive forecast); with drift it is the "drift" forecast.

### Example
AR(1) with $\phi=0.7$, mean 100, last observation 110: the forecasts revert to the mean geometrically, $\hat y_{T+h}=100+0.7^h\times10$, giving 107.0, 104.9, 103.4 for $h=1,2,3$ and 100.3 for $h=10$. For MA(1) with $\theta=0.6$: $\rho_1=0.6/1.36=0.441$ and zero beyond lag 1; the forecast beyond one step is just the mean. Hence AR forecasts decay gradually, MA forecasts cut off after $q$ steps.

### In the news
See news box. ARIMA remains the baseline that newer foundation models are benchmarked against, in part because its few parameters are transparent and auditable.

### Interview angle
> [!question] How it is asked
> "Explain AR, MA and ARIMA(1,1,1) in plain words."

> [!tip] Strong answer includes
> - AR: today depends on recent values; MA: today depends on recent forecast errors; I: difference to get stationarity
> - ARIMA(1,1,1): difference once, then AR(1) plus MA(1) on the changes
> - Stationarity and invertibility conditions; relationship to exponential smoothing
> - Link to forecasting for supply chains: [[119 Supply Planning, DRP & Available-to-Promise]]

---
## 5. Identification with ACF and PACF (Worked)
> 🔴 Tier 1 · _Key points:_ AR(p): PACF cuts off at p, ACF tails off; MA(q): ACF cuts off at q, PACF tails off; ARMA: both tail off; bands $\pm1.96/\sqrt n$

### Definition
The **autocorrelation function (ACF)** $\rho_k$ is the correlation of $y_t$ and $y_{t-k}$. The **partial ACF (PACF)** is the correlation at lag $k$ after removing the effect of the intermediate lags. Approximate 95% bands for white noise: $\pm1.96/\sqrt n$.

| Model | ACF | PACF |
|---|---|---|
| AR(p) | tails off (exponential/sinusoidal decay) | cuts off after lag $p$ |
| MA(q) | cuts off after lag $q$ | tails off |
| ARMA(p,q) | tails off | tails off |
| Non-stationary | decays very slowly, near 1 | big spike at lag 1 |
| Seasonal (period $m$) | spikes at $m, 2m,\dots$ | spikes at $m, 2m,\dots$ |

Identification is a starting point; confirm by comparing a few candidate orders with AIC/BIC and checking residuals.

### Example
200 points simulated from AR(1) with $\phi=0.7$: sample ACF at lags 1-5 is 0.737, 0.535, 0.375, 0.242, 0.136 (theory 0.70, 0.49, 0.34, 0.24, 0.17), a smooth decay; PACF is 0.741 then -0.018, -0.029, -0.045, -0.037, all inside $\pm0.139$: cut-off after lag 1, so AR(1). Fit: $\hat\phi=0.738$ (SE 0.052). 200 points from MA(1) with $\theta=0.6$: ACF is 0.49 at lag 1 then 0.08, 0.06, 0.02, -0.05 (inside the band): cut-off after lag 1; PACF 0.49, -0.21, 0.16, -0.10 decays. Fit: $\hat\theta=0.631$ (SE 0.058). AIC for the AR(1) data: ARIMA(1,0,0) 567.9; (2,0,0) 569.9; (1,0,1) 569.9; the wrong MA(1) model 622.8. Extra terms do not pay for themselves, and AIC picks the true AR(1).

### In the news
See news box. Automated ARIMA search (auto-ARIMA, pmdarima, R's forecast::auto.arima) uses AIC to choose among such orders, but reading ACF/PACF plots is still the expected interview skill.

### Interview angle
> [!question] How it is asked
> "The PACF cuts off after lag 2 and the ACF decays. Which model?"

> [!tip] Strong answer includes
> - AR(2); explain why (PACF cut-off, ACF tail-off)
> - Mention the confidence band and that one or two marginal spikes are noise
> - Verify with AIC and residual ACF; consider differencing if the ACF decays too slowly

---
## 6. Box-Jenkins Methodology
> 🔴 Tier 1 · _Key points:_ Identify, estimate, diagnose, forecast; parsimony; iterate

### Definition
Box-Jenkins is the iterative workflow for ARIMA modelling:
1. **Plot and prepare:** outliers, missing values, structural breaks, variance transform (log).
2. **Stationarise:** differencing (regular and seasonal); test with ADF/KPSS.
3. **Identify** tentative $(p,q)$ and $(P,Q)$ from ACF/PACF; prefer parsimonious models.
4. **Estimate** by maximum likelihood (or conditional least squares); check coefficient significance and stationarity/invertibility.
5. **Diagnose:** residuals should be white noise (no ACF spikes, Ljung-Box not significant), approximately normal and constant variance.
6. **Compare** candidates (AIC/BIC, out-of-sample error), choose, **forecast** with intervals; **monitor** and re-fit as data arrive.

Parsimony matters because every extra parameter costs data and degrades forecasts; models with common AR and MA factors are redundant (parameter redundancy).

### Example
The 84-month simulated demand series of sub-topic 7: step 1 log-transform (variance grows with level); step 2 one regular plus one seasonal difference (ADF p falls from 0.895 on the level to 0.022); step 3 the ACF of the differenced series has spikes at lag 1 (about -0.42) and lag 12 (about -0.32), so tentative MA(1) and seasonal MA(1); step 4 estimates $\hat\theta_1=-0.85$, $\hat\Theta_1=-0.83$, both significant; step 5 Ljung-Box p = 0.124 at lag 12 (clean); step 6 forecast 12 months with 95% intervals, test MAPE 3.5%. The full numbers are in sub-topic 7.

### In the news
See news box. Benchmarks of foundation models run an automatic version of this loop (fit candidate statistical models, pick by validation error), so the manual workflow explains what those baselines are doing.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would build an ARIMA model for monthly sales."

> [!tip] Strong answer includes
> - Plot, transform, stationarise (ADF/KPSS), identify (ACF/PACF), estimate, diagnose (Ljung-Box), validate out of sample, forecast with intervals
> - Mention seasonal terms and parsimony
> - Say how often you would retrain and how you handle promotions and outliers (see ARIMAX below)

---
## 7. SARIMA: Seasonal ARIMA (Worked Example)
> 🔴 Tier 1 · _Key points:_ $\text{SARIMA}(p,d,q)(P,D,Q)_m$; "airline model" $(0,1,1)(0,1,1)_{12}$; seasonal terms at lag $m$

### Definition
SARIMA adds seasonal AR and MA terms at multiples of the period $m$ and seasonal differencing:

$$\Phi_P(B^m)\,\phi_p(B)\,(1-B)^d(1-B^m)^D\,y_t=c+\Theta_Q(B^m)\,\theta_q(B)\,e_t$$

The **airline model** $(0,1,1)(0,1,1)_{12}$ (on logs) is a strong default for monthly data with multiplicative seasonality: one regular and one seasonal difference with one MA term at lag 1 and one at lag 12. Seasonal spikes in the ACF at lags $m$, $2m$ guide $Q$; in the PACF they guide $P$. Multiple seasonality (weekday and annual) needs TBATS, Fourier terms or regression with ARIMA errors.

### Example
96 months of simulated demand (trend +8 units per month from 1,000 and a multiplicative seasonal profile whose November peak is about 25% above the annual average), first 84 months for training, last 12 for testing, all fitted on logs with `SARIMAX`:

| Model | AIC | BIC |
|---|---|---|
| (0,1,1)(0,1,1)$_{12}$ | -259.6 | -252.8 |
| (1,1,1)(0,1,1)$_{12}$ | -257.6 | -248.5 |
| (0,1,1)(1,1,1)$_{12}$ | -258.0 | -248.9 |
| (2,1,0)(0,1,1)$_{12}$ | -248.4 | -239.4 |
| (1,1,0)(1,1,0)$_{12}$ | -228.6 | -221.8 |

The airline model wins on both criteria. Estimates: $\hat\theta_1=-0.850$ (SE 0.073), $\hat\Theta_1=-0.834$ (SE 0.275). Ljung-Box on residuals: lag 12 p = 0.124, lag 24 p = 0.447 (no leftover autocorrelation). Test-set MAPE on the 12 held-out months: **3.5%** against 5.6% for the seasonal-naive forecast (repeat last year). Forecasts for Jan to Dec of the test year (units): 1,459, 1,376, 1,613, 1,678, 1,766, 1,869, 1,684, 1,680, 1,818, 1,989, 2,291, 2,092. These run above the actuals in all 12 months. A likely reason is that the differenced log model extrapolates the recent percentage growth, while the simulated trend is linear in units so percentage growth slows: a trend-type mismatch that the Holt-Winters comparison below helps expose.

```python
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
m = SARIMAX(np.log(train), order=(0,1,1), seasonal_order=(0,1,1,12)).fit(disp=False)
fc = m.get_forecast(12); pred = np.exp(fc.predicted_mean); ci = np.exp(fc.conf_int(0.05))
```

### In the news
See news box. Seasonal ARIMA and ETS are still the workhorses against which Chronos and TimesFM are scored on retail and demand series.

### Interview angle
> [!question] How it is asked
> "What does SARIMA(0,1,1)(0,1,1)12 mean?"

> [!tip] Strong answer includes
> - One regular and one seasonal difference, MA(1) on shocks and MA(1) at lag 12, usually on log data
> - When to use (stable multiplicative seasonality), and what residual checks to run
> - Beat the seasonal-naive benchmark or do not deploy; see [[004 Demand Forecasting & Planning|demand forecasting]] for business use

---
## 8. Residual Diagnostics and the Ljung-Box Test
> 🔴 Tier 1 · _Key points:_ Residuals should be white noise; $Q=n(n+2)\sum\frac{\hat\rho_k^2}{n-k}\sim\chi^2_{h-\text{params}}$; plot ACF, QQ, variance

### Definition
A good model leaves residuals with no pattern. **Ljung-Box:** H0: residuals are independently distributed (no autocorrelation up to lag $h$):

$$Q=n(n+2)\sum_{k=1}^{h}\frac{\hat\rho_k^2}{n-k}\ \sim\ \chi^2_{h-p-q}$$

(degrees of freedom reduced by the number of fitted ARMA parameters). Choose $h$ around $\min(10,n/5)$ for non-seasonal data, $2m$ for seasonal. A **small p-value means leftover structure**, so the model is inadequate; a large p-value means no evidence of autocorrelation (not proof of a good model). Also check: residual ACF within bands, histogram/QQ (for interval validity), stable variance over time (ARCH effects via Ljung-Box on squared residuals), and no pattern against fitted values. Durbin-Watson is a lag-1 check used in regression.

### Example
SARIMA airline model above: Ljung-Box lag 12 $Q=15.2$, $p=0.124$; lag 24 $Q=22.2$, $p=0.447$ (with 2 fitted MA parameters subtracted from d.f.). Conclusion: no significant leftover autocorrelation. Contrast: fitting an MA(1) to the AR(1) data in sub-topic 5 leaves strongly autocorrelated residuals (its AIC was 55 points worse). Regression residuals with Durbin-Watson 0.78 (sub-topic 13) signal positive autocorrelation.

### In the news
See news box. Model-risk reviews for forecasting models (including ML ones, see [[218 Forecasting with ML & Foundation Models]]) ask for exactly these residual checks.

### Interview angle
> [!question] How it is asked
> "How do you know your forecasting model is adequate?"

> [!tip] Strong answer includes
> - Residual diagnostics (Ljung-Box, ACF plot, normality) plus out-of-sample accuracy against a naive benchmark
> - A passing Ljung-Box is necessary, not sufficient
> - Adjust Ljung-Box degrees of freedom for fitted parameters

---
## 9. Exponential Smoothing and the ETS Framework
> 🔴 Tier 1 · _Key points:_ SES, Holt (trend), damped trend, Holt-Winters (season); ETS(Error, Trend, Seasonal) taxonomy; weights decay geometrically

### Definition
**Simple exponential smoothing (SES)** for level-only data: $\ell_t=\alpha y_t+(1-\alpha)\ell_{t-1}$, forecast $\hat y_{t+h}=\ell_t$. Equivalent to weights $\alpha(1-\alpha)^j$ on past observations. **Holt:** adds a trend $b_t=\beta^*(\ell_t-\ell_{t-1})+(1-\beta^*)b_{t-1}$, forecast $\ell_t+hb_t$. **Damped trend:** $\ell_t+(\phi+\phi^2+\dots+\phi^h)b_t$ with $0<\phi<1$, often the best-performing in M-competition style evaluations. **Holt-Winters** adds seasonal indices. The **ETS state-space** taxonomy labels models ETS(Error, Trend, Seasonal) with Error in {A, M}, Trend in {N, A, Ad}, Seasonal in {N, A, M}; it supplies likelihoods, AIC and prediction intervals. SES is ETS(A,N,N) and is the same model as ARIMA(0,1,1). Smoothing parameters are estimated by minimising squared error or maximising likelihood; higher $\alpha$ means faster reaction and a noisier forecast. Initial values matter for short series.

### Example
Demand 100, 110, 104, 115, 120 with $\alpha=0.3$ and $\ell_0=100$: levels after each new observation are 103.0, 103.3, 106.81, 110.77, so the next-period forecast is 110.8 (the latest 120 is only 30% weighted, damping noise). With $\alpha=0.8$ the forecast would hug the last values more closely. For a trending series SES lags behind, so use Holt; for seasonality use Holt-Winters or ETS with seasonal terms. Compare with moving averages in [[066 Demand Forecasting & Time Series]].

### In the news
See news box. Exponential smoothing remains a standard benchmark in the Chronos evaluation family; the new models must beat it to justify their cost.

### Interview angle
> [!question] How it is asked
> "How is exponential smoothing different from a moving average, and how do you choose alpha?"

> [!tip] Strong answer includes
> - Geometric weights vs equal weights; one parameter to tune by minimising out-of-sample error or likelihood
> - Trend and seasonal extensions (Holt, Holt-Winters), damping for long horizons
> - ETS gives prediction intervals and AIC; SES equals ARIMA(0,1,1)

---
## 10. Holt-Winters: Additive vs Multiplicative
> 🔴 Tier 1 · _Key points:_ Additive: constant seasonal swing in units; multiplicative: swing proportional to level; pick by plot and AIC/validation

### Definition
**Additive seasonality:** $y_t\approx\ell+tb+s_t$; the seasonal amplitude stays the same as the level grows. **Multiplicative:** $y_t\approx(\ell+tb)\,s_t$ with indices around 1; amplitude grows with level (typical for sales, passenger counts). Choose by plotting: if the seasonal swings widen as the series rises, use multiplicative (or log, then additive). The trend can be additive (linear growth), multiplicative (exponential) or damped. A mismatched structure is a common source of forecast bias.

### Example
Same 84-month training data, 12-month test, statsmodels `ExponentialSmoothing(train, trend=..., seasonal=..., seasonal_periods=12)`:

| Trend / seasonal | AIC | Test MAPE |
|---|---|---|
| additive / additive | 681.8 | 3.00% |
| additive / **multiplicative** | **636.5** | **1.69%** |
| multiplicative / multiplicative | 647.1 | 2.15% |

Additive trend with multiplicative seasonality wins on both AIC and test error, matching how the data were built (linear trend, multiplicative seasonal profile), and beats the SARIMA of sub-topic 7 (3.5% MAPE) and seasonal naive (5.6%). ETS state-space versions: ETS(M,A,M) AIC 872.3 (MAPE 1.77%), ETS(A,A,M) 878.9 (1.69%), ETS(A,A,A) 924.3 (2.75%), ETS(M,Ad,M) 948.0 (2.18%). Compare AIC only among models fitted to the same series on the same scale: the SARIMA (fitted on logs) and these level-scale models have incomparable AIC values, which is why the table uses test error across families.

### In the news
See news box. This is the comparison that matters in the foundation-model era: a well-chosen Holt-Winters is a strong baseline for seasonal demand.

### Interview angle
> [!question] How it is asked
> "How do you decide between additive and multiplicative seasonality?"

> [!tip] Strong answer includes
> - Plot: do seasonal swings grow with the level? If yes, multiplicative or log-transform
> - Compare by AIC (same scale) and rolling-origin error
> - Mention trend choice and damping; ties to inventory and S&OP forecasts in [[120 Integrated Business Planning (IBP) & S&OP Maturity]]

---
## 11. Forecast Intervals and Uncertainty
> 🔴 Tier 1 · _Key points:_ Interval widens with horizon; random walk $\pm z\sigma\sqrt h$; model-based intervals understate uncertainty (parameter, model and structural-break risk)

### Definition
A **point forecast** is the conditional mean; a **prediction interval** says where the future observation will fall with stated probability, $\hat y_{T+h}\pm z_{\alpha/2}\,\hat\sigma_h$. $\sigma_h$ grows with horizon: it is constant for pure MA beyond $q$ steps, converges to the series s.d. for stationary AR, and grows like $\sqrt h$ for a random walk (and faster with extra differencing). Intervals assume normal, uncorrelated residuals and a correct model; they ignore parameter and model uncertainty and regime shifts, so actual coverage is often below nominal. Check calibration on holdout data. Business use: set safety stock with forecast-error s.d. in [[003 Inventory Management]].

### Example
Random walk with $\sigma=10$: 95% half-widths at horizons 1, 2, 3 are $1.96\times10\times\sqrt h=19.6,\ 27.7,\ 34.0$: the interval at $h=3$ is 1.7 times as wide as at $h=1$. SARIMA airline model: 95% intervals for the test year are about $\pm7\%$ of the forecast (January: 1,365 to 1,560 around 1,459). Only 10 of the 12 actuals (83%) fell inside the nominal 95% intervals, because the forecasts were biased upward: intervals are only as good as the point forecast and the model. Use rolling-origin evaluation to measure real coverage before promising a service level.

### In the news
See news box. Probabilistic forecasting (quantile forecasts) is a headline feature of the foundation models such as Chronos, precisely because decisions need intervals, not just points.

### Interview angle
> [!question] How it is asked
> "Why not just give the business the point forecast?"

> [!tip] Strong answer includes
> - Decisions (safety stock, capacity, budgets) depend on uncertainty; widths grow with horizon
> - Intervals are conditional on the model; validate coverage on holdout; prefer quantile forecasts or conformal methods for robustness
> - Link to safety stock formula and service levels

---
## 12. Model Comparison: AIC/BIC, Time-Series Cross-Validation and Accuracy Metrics
> 🔴 Tier 1 · _Key points:_ AIC $=2k-2\ln L$; BIC penalises more; rolling-origin CV; MAPE/MASE/RMSE; always beat the naive benchmark

### Definition
**AIC** $=2k-2\ln\hat L$ and **BIC** $=k\ln n-2\ln\hat L$ trade fit against complexity (lower is better). BIC picks simpler models for large $n$. They are valid only for models on the same data and same dependent variable (not for different differencing orders or a log vs level model). **Time-series cross-validation** (rolling or expanding origin) trains on data up to $t$, forecasts the next $h$ periods, then moves the origin forward; never shuffle time series. Metrics: **RMSE/MAE** (scale-dependent), **MAPE** $=\frac{100}{n}\sum|e_t/y_t|$ (undefined near zero, favours under-forecasting), **sMAPE**, **MASE** (error scaled by in-sample naive error; below 1 beats naive), and pinball loss for quantiles. Compare to naive and seasonal-naive benchmarks. Detailed accuracy KPIs are in [[012 Supply Chain Analytics & KPIs]].

### Example
Rolling-origin evaluation of the airline SARIMA on the demand series with forecast origins after month 60, 72 and 84 (12-month horizon each): MAPE 2.45%, 3.21%, 3.53%; mean **3.06%**. A single holdout (the last fold, 3.5%) therefore overstated the average error, and the error rose with later origins in this run (consistent with the trend-type mismatch noted above). The seasonal-naive benchmark scored 5.6% on the last holdout, so SARIMA clears the benchmark but Holt-Winters (additive trend, multiplicative season, 1.69%) is better still.

### In the news
See news box. Foundation-model papers evaluate with exactly this kind of rolling-origin, benchmark-relative scoring across dozens of datasets.

### Interview angle
> [!question] How it is asked
> "Two models have similar AIC. How do you choose, and how do you prove it will work in production?"

> [!tip] Strong answer includes
> - Prefer simpler (BIC), compare on rolling-origin out-of-sample error vs seasonal naive, check bias and interval coverage
> - Explain AIC comparability limits and that cross-validation must respect time order
> - Business metric: cost of over- vs under-forecast, not only MAPE

---
## 13. ARIMAX and Regression with ARIMA Errors
> 🔴 Tier 1 · _Key points:_ Add external regressors (promotions, price, holidays); model residual autocorrelation with ARMA; future values of regressors required

### Definition
**Regression with ARIMA errors:** $y_t=\beta_0+\beta_1x_{1t}+\dots+\eta_t$, where $\eta_t$ follows an ARIMA process. It estimates covariate effects while correctly handling autocorrelated errors (ordinary regression has invalid SEs when errors are autocorrelated; check Durbin-Watson and the residual ACF). "ARIMAX" is often loosely used for this model (some texts mean a model with lagged $x$ terms, so state the form). In `SARIMAX`, `exog=` gives the regressors, and the intercept is the regression intercept, not the process mean of an AR model. Forecasting needs future values of $x$ (planned promotions, calendar events, or forecasts of the drivers). Dynamic regression with lagged effects (distributed lags) handles carry-over and pull-forward.

### Example
Weekly demand, 156 weeks (simulated): baseline 500, promotion weeks (about 25%) add 120, AR(1) noise with $\phi=0.6$. SARIMAX with the promo flag as exog and AR(1) errors: promo effect $\hat\beta=118.5$ (SE 4.2; true 120), $\hat\phi=0.51$; AIC 1,438 against 1,740 for ARIMA(1,0,0) without the promo variable. Plain OLS gives promo $=117.1$ with Durbin-Watson 0.78 (strong positive autocorrelation), so its SE cannot be trusted. Forecast for four planned weeks with promos in weeks 1 and 4: 608, 495, 497, 617 with 95% ranges about $\pm50$ to $\pm58$. Use this to plan inventory in [[119 Supply Planning, DRP & Available-to-Promise]] and to measure promotion uplift for [[093 Business Statistics Applications]].

### In the news
See news box. After a CPI base change, a level-shift dummy in a regression with ARIMA errors is one clean way to keep the series modelled across the break.

### Interview angle
> [!question] How it is asked
> "How would you include promotions and holidays in a time-series forecast?"

> [!tip] Strong answer includes
> - Dummy/exogenous regressors with ARIMA (or ETS plus regression) errors; need future values of promotion calendars
> - Check residual autocorrelation; avoid leakage from using actual future covariates
> - Estimate uplift and cannibalisation; consider ML alternatives in [[218 Forecasting with ML & Foundation Models]]

---
## 14. ⭐ Advanced: GARCH and Volatility Models (Overview)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
ARIMA models the conditional mean; **ARCH/GARCH** model the conditional **variance**, which clusters in financial and commodity series (calm periods, then turbulent ones). **GARCH(1,1):**

$$r_t=\sigma_te_t,\qquad \sigma_t^2=\omega+\alpha\,r_{t-1}^2+\beta\,\sigma_{t-1}^2$$

Stationary if $\alpha+\beta<1$; long-run variance $\omega/(1-\alpha-\beta)$; persistence $\alpha+\beta$ (close to 1 means volatility shocks decay slowly); half-life $=\ln0.5/\ln(\alpha+\beta)$. Extensions: EGARCH and GJR-GARCH (leverage effect: bad news raises volatility more), GARCH-in-mean, multivariate DCC. Applications: Value-at-Risk, option pricing, commodity-price hedging ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]), time-varying prediction intervals. Detect ARCH effects with Ljung-Box on squared residuals or Engle's LM test.

### Example
1,500 simulated returns from a GARCH(1,1) (true $\omega=0.05$, $\alpha=0.10$, $\beta=0.85$); `arch_model(r, mean='Zero', vol='GARCH', p=1, q=1)` estimates $\hat\omega=0.059$, $\hat\alpha=0.116$ (SE 0.020), $\hat\beta=0.828$ (SE 0.032). Persistence 0.944, half-life $\ln0.5/\ln0.944=12.1$ days; long-run variance $0.0587/(1-0.944)=1.05$. Ljung-Box on returns: $p=0.78$ (no mean dynamics), on squared returns: $p\approx10^{-68}$ (strong ARCH effect). The 10-day variance forecast rises from 0.633 to 0.803, mean-reverting towards 1.05 from a calm starting point.

### In the news
See news box. Probabilistic foundation models are judged on how well they capture uncertainty; GARCH is the classical explicit model of time-varying uncertainty.

### Interview angle
> [!question] How it is asked
> "Our commodity price series has calm and wild periods. ARIMA intervals look too narrow in the wild periods. What do you do?"

> [!tip] Strong answer includes
> - Constant-variance residual assumption is violated; test squared residuals for ARCH effects
> - ARIMA for the mean plus GARCH (or EGARCH/GJR) for the variance; time-varying intervals
> - Use forecast variance for hedging and risk limits; validate by backtesting VaR exceedances
