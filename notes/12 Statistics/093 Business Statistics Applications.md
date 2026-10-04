---
tags: [statistics, tier2]
area: Statistics
topic: "Business Statistics Applications"
tier: Tier 2
roles: All Roles
status: complete
subtopics: 10
---
# Business Statistics Applications

⬅ [[092 Sampling & Experimental Design]] · [[_Index - Statistics|Statistics]] · [[205 Sampling Distributions & Estimation]] ➡
> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Index Numbers]]
2. [[#2. Time Series Decomposition]]
3. [[#3. Seasonal Adjustment]]
4. [[#4. Moving Averages for Trend]]
5. [[#5. Weighted Index Numbers]]
6. [[#6. Statistical Decision Theory]]
7. [[#7. Simulation-Based Statistics]]
8. [[#8. Bayesian vs Frequentist]]
9. [[#9. ⭐ Advanced: Deflating Series, Base Shifting and Splicing]]
10. [[#10. ⭐ Advanced: Simpson's Paradox, Correlation vs Causation and Misleading Statistics]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's CPI gets a new base year (2024), a live lesson in index numbers
> **What changed (launched Feb 2026).** MoSPI re-based the Consumer Price Index from 2011-12 to **2024**, drawing weights from the 2023-24 Household Consumption Expenditure Survey and adopting the **COICOP 2018** classification (12 divisions). *Food and Beverages* weight fell from **45.86% to 36.75%**; *housing, utilities and fuel* rose from **10.07% to 17.67%**; *health* is weighted at **6.10%** and *transport* **8.80%**. The basket has **358 weighted items** (seven new items such as streaming services; six obsolete ones such as VCRs and cassettes dropped), with prices from **434 towns** and weekly data from **12 e-commerce platforms**. SBI Research estimated the new weights could lift headline CPI by about **20 to 30 basis points** on unchanged indices. ([Business Standard](https://www.business-standard.com/amp/economy/news/economy-inflation-weight-food-beverages-cut-new-cpi-series-2024-base-126012901838_1.html), [Upstox](https://upstox.com/learning-center/personal-finance/what-changed-in-indias-new-cpi-series-and-how-it-impacts-the-economy-and-inflation/article-1518/))
> 
> **First reading.** January 2026 inflation under the new series was **2.75%**, against **1.3%** for December 2025 on the old series; the gap reflects the methodology change, not just a price spike. ([Upstox](https://upstox.com/learning-center/personal-finance/what-changed-in-indias-new-cpi-series-and-how-it-impacts-the-economy-and-inflation/article-1518/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Index Numbers
> 🟠 Tier 2 · _Tracker hint:_ Price index: (P1/P0)×100; Laspeyres vs Paasche; CPI and WPI construction

### Definition
An **index number** expresses the change in a variable (price, quantity, value) relative to a **base period** set to 100.

- **Simple price relative:** $I=\dfrac{P_1}{P_0}\times100$.
- **Laspeyres (base-year quantities):** $L=\dfrac{\sum P_1Q_0}{\sum P_0Q_0}\times100$. Easy (weights fixed), but overstates inflation because consumers substitute away from items that become dearer (substitution bias).
- **Paasche (current-year quantities):** $P=\dfrac{\sum P_1Q_1}{\sum P_0Q_1}\times100$. Needs new quantities every period; tends to understate.
- **Fisher ideal:** $F=\sqrt{L\times P}$, and satisfies the time-reversal and factor-reversal tests. Also Marshall-Edgeworth, and chain-linked indices.
- **Value index** $=\sum P_1Q_1/\sum P_0Q_0$.

**CPI** (consumer price index) measures retail prices for a household basket; India's CPI (Combined) feeds the RBI's 4% (±2%) inflation target. **WPI** (wholesale price index) tracks wholesale goods prices (no services) and has a different basket. Inflation rate $=\dfrac{CPI_t-CPI_{t-1}}{CPI_{t-1}}\times100$.

### Example
Two goods. Base: rice ₹40 and oil ₹120, quantities 10 and 5. Current: rice ₹50, oil ₹144, quantities 8 and 6.
Laspeyres $=\dfrac{50(10)+144(5)}{40(10)+120(5)}=\dfrac{500+720}{1000}=122.0$.
Paasche $=\dfrac{50(8)+144(6)}{40(8)+120(6)}=\dfrac{400+864}{320+720}=\dfrac{1264}{1040}=121.5$.
Fisher $=\sqrt{122.0\times121.54}\approx121.8$. Laspeyres is higher than Paasche, consistent with substitution bias.

### In the news
See news box. The new CPI changes the base year and the weights, effectively re-running the Laspeyres exercise with quantities from 2023-24 consumption data; its start of 2.75% against 1.3% on the old series shows how basket choice moves the number.

### Interview angle
> [!question] How it is asked
> "Why is Laspeyres biased upward?" or "How is CPI different from WPI?" or "How is inflation computed?"

> [!tip] Strong answer includes
> - Formulas with base-year vs current-year weights
> - Substitution bias and the Fisher compromise
> - CPI (consumers, includes services) vs WPI (wholesale, goods only)
> - Why re-basing is needed (changed consumption patterns, new products)

---

## 2. Time Series Decomposition
> 🟠 Tier 2 · _Tracker hint:_ Trend (T) × Seasonal (S) × Cyclical (C) × Irregular (I) — multiplicative model

### Definition
A time series is split into components:
- **Trend (T):** long-run direction.
- **Seasonal (S):** regular pattern within a year (festivals, weather).
- **Cyclical (C):** multi-year business-cycle swings (irregular period).
- **Irregular (I):** random noise and shocks.

**Multiplicative model:** $Y_t=T_t\times S_t\times C_t\times I_t$ (seasonal swings grow with the level). **Additive model:** $Y_t=T_t+S_t+C_t+I_t$ (constant swing size). Choose multiplicative when seasonal amplitude rises with the trend; taking logs turns it into additive.

**Classical decomposition steps (multiplicative):** (1) centred moving average over the season length to estimate $T\times C$; (2) ratio $Y/(T\times C)$ gives $S\times I$; (3) average by month/quarter to get the seasonal index, normalised to average 1 (sum 12 for months, 4 for quarters); (4) deseasonalise, fit the trend by regression, and forecast as $T\times S$. Modern tools: STL, X-13ARIMA-SEATS.

```python
from statsmodels.tsa.seasonal import seasonal_decompose
res = seasonal_decompose(series, model="multiplicative", period=12)
res.trend, res.seasonal, res.resid
```

### Example
December sales: trend estimate ₹500 lakh, seasonal index 1.20, cyclical 1.00, irregular 1.00. Forecast $=500\times1.20\times1.00\times1.00=₹600$ lakh. Forecast for the next month with trend 510 and seasonal 0.90 is $510\times0.90=459$.

### In the news
See news box. Headline CPI inflation is seasonal (vegetable prices peak in the monsoon), which is why analysts compare year-on-year changes and look at core inflation that strips the volatile components, a decomposition idea.

### Interview angle
> [!question] How it is asked
> "Sales jump every October. How would you separate festival effects from underlying growth?"

> [!tip] Strong answer includes
> - The four components and the multiplicative vs additive choice
> - Steps: moving average, ratio, seasonal index, deseasonalise, trend
> - Using the decomposed model to forecast
> - Awareness of structural breaks, outliers and tools (STL)

---

## 3. Seasonal Adjustment
> 🟠 Tier 2 · _Tracker hint:_ Divide by seasonal index to get trend; seasonal index = avg monthly ratio

### Definition
**Seasonal adjustment** removes the recurring seasonal pattern so you can see underlying movement (trend and cycle) and compare adjacent periods fairly.

$$\text{Deseasonalised value}=\frac{Y_t}{S_t}\quad(\text{multiplicative}),\qquad Y_t-S_t\ (\text{additive})$$

**Seasonal index** by ratio-to-moving-average: for each month, average the ratios $Y/CMA$ across years, then **normalise** so the indices average 1.00 (100%). An index of 1.20 means that month is typically 20% above the annual average; 0.80 means 20% below. After adjusting, fit a trend line (regression on time) and re-seasonalise for forecasts: $\hat Y=\text{trend}\times S$.

Use year-on-year comparison as a simple alternative when no adjustment is available.

### Example
Quarterly seasonal indices: Q1 0.90, Q2 1.10, Q3 0.80, Q4 1.20 (sum 4.0, average 1 ✓). Q4 actual sales 480 deseasonalised: $480/1.20=400$. Q3 actual 340: $340/0.80=425$. In raw terms Q4 looks stronger (480 vs 340); after adjustment Q3's underlying level (425) is actually higher than Q4's (400).
Forecast: trend for next Q1 = 410, so forecast $=410\times0.90=369$.

### In the news
See news box. After the re-base, official and private economists comparing the new and old series have to adjust for the level difference (2.75% vs 1.3%) before drawing conclusions about the trend, the same logic as removing a known component before comparison.

### Interview angle
> [!question] How it is asked
> "Q4 sales are 20% higher than Q3. Is the business growing?"

> [!tip] Strong answer includes
> - Divide by the seasonal index to compare like with like
> - How the index is built and normalised
> - Year-on-year as a quick check
> - Caution on festival shifts (Diwali date moves) and trading-day effects

---

## 4. Moving Averages for Trend
> 🟠 Tier 2 · _Tracker hint:_ 3-period, 5-period CMA; odd-period MA centered automatically

### Definition
A **simple moving average (SMA)** of period $m$ averages $m$ consecutive observations and slides forward, smoothing out short-term noise so the trend shows.

- **Odd $m$** (3, 5): the average sits exactly at the middle period, so it is **centred automatically**: $MA_t=\dfrac{Y_{t-1}+Y_t+Y_{t+1}}{3}$.
- **Even $m$** (4 for quarters, 12 for months): the average falls between two periods, so a second 2-period average **centres** it (CMA).
- A period equal to the seasonal length removes the seasonality, leaving $T\times C$.
- Larger $m$ gives smoother series but more lag and loses $m-1$ points (for $m=3$ you lose first and last).
- Weighted MA and **exponential smoothing** give more weight to recent data. Trailing MA is used for forecasting, centred MA for trend estimation.

Moving averages smooth, they do not forecast beyond the data without further modelling; they lag turning points.

### Example
Series: 20, 22, 24, 23, 25, 27. 3-period MA: $(20+22+24)/3=22$; $(22+24+23)/3=23$; $(24+23+25)/3=24$; $(23+25+27)/3=25$ → 22, 23, 24, 25 (a rising trend of about 1 per period).
4-period CMA for 100, 120, 90, 130, 110: first 4-MA $=440/4=110$ (between t2 and t3); second $=450/4=112.5$ (between t3 and t4); centred at t3 $=(110+112.5)/2=111.25$.

### In the news
See news box. Analysts often quote 3-month moving averages of monthly CPI to look past noise from vegetables, a practical use of the smoothing method.

### Interview angle
> [!question] How it is asked
> "Calculate a 3-month moving average" or "Why use a centred moving average?"

> [!tip] Strong answer includes
> - Compute correctly and state where the average is placed
> - Why even-length windows need a 2x MA to centre
> - Trade-off between smoothness and lag
> - Choosing window = seasonal length to remove seasonality

---

## 5. Weighted Index Numbers
> 🟠 Tier 2 · _Tracker hint:_ Weighted average of component indices; sectoral weights in composite index

### Definition
Composite indices (CPI, WPI, IIP, Sensex-type indices) combine component indices using **weights** that reflect relative importance (expenditure share, output value, market cap).

$$I_{composite}=\frac{\sum w_iI_i}{\sum w_i}$$

- **Weighted aggregative indices:** Laspeyres, Paasche, Fisher from sub-topic 1.
- **Weighted average of relatives:** $\dfrac{\sum w\,(P_1/P_0)\times100}{\sum w}$ with $w=P_0Q_0$ (equals Laspeyres).
- Weights should reflect the base period; updating them (re-basing) corrects drift as spending patterns change.
- **Contribution to change** of component $i$ $=w_i\times\Delta I_i/\sum w$; useful to find which sector drives movement.
- Sensitivity: a component's influence on the composite depends on both **weight and volatility**.

### Example
Mini-CPI with weights Food 36.75 (index 110) and Others 63.25 (index 104):
$I=\dfrac{36.75\times110+63.25\times104}{100}=\dfrac{4042.5+6578}{100}=106.2$.
Under the old food weight 45.86 (others 54.14): $\dfrac{45.86\times110+54.14\times104}{100}=\dfrac{5044.6+5630.6}{100}=106.75$. A lower food weight reduces the headline when food is the high-inflation component, one reason weights matter.

### In the news
See news box. The explicit weight changes are the story: food 45.86% to 36.75%, housing/utilities/fuel 10.07% to 17.67%, health 6.10%, transport 8.80%. SBI Research estimated the new weights could raise headline CPI by 20 to 30 bp on unchanged indices (when food inflation is low), and could reverse when food inflation is high.

### Interview angle
> [!question] How it is asked
> "How is the CPI weighted and what happens when the weights change?"

> [!tip] Strong answer includes
> - Formula for a weighted composite
> - Source of weights (household expenditure survey) and why re-basing happens
> - Computation of a worked mini-CPI
> - Interpretation: weight times component movement drives the headline

---

## 6. Statistical Decision Theory
> 🟠 Tier 2 · _Tracker hint:_ Decision under uncertainty; maximin, maximax, minimax regret, expected value

### Definition
A decision problem has **actions**, **states of nature**, and **payoffs**. Criteria:
- **Maximax** (optimist): pick the action with the best best-case payoff.
- **Maximin** (Wald, pessimist): pick the best of the worst cases.
- **Minimax regret** (Savage): regret = best payoff in that state minus your payoff; choose the action whose maximum regret is smallest.
- **Hurwicz:** weighted mix of best and worst with optimism index $\alpha$. **Laplace:** equal probabilities.
- **Expected Monetary Value (EMV)** when probabilities are known: $EMV=\sum p_jV_{ij}$. **EVPI** $=EV_{\text{perfect info}}-\max EMV$ (upper bound on what information is worth).
- **Decision trees**, utility functions for risk aversion, and **Bayesian updating** with sample information (EVSI).

### Example
Capacity decision, payoffs (₹ crore) in Good / Fair / Poor demand:

| | Good | Fair | Poor |
|---|---|---|---|
| Big plant | 80 | 30 | -40 |
| Medium | 50 | 35 | 0 |
| Small | 20 | 15 | 10 |

Maximax: Big (80). Maximin: Small (worst cases -40, 0, 10, so 10). Regret table (column maxima 80, 35, 10): Big 0, 5, 50 (max 50); Medium 30, 0, 10 (max 30); Small 60, 20, 0 (max 60), so minimax regret picks **Medium**.
With probabilities 0.3, 0.5, 0.2: EMV Big $=24+15-8=31$; Medium $=15+17.5+0=32.5$; Small $=6+7.5+2=15.5$. Choose Medium. EVPI $=(0.3\times80+0.5\times35+0.2\times10)-32.5=43.5-32.5=₹11$ crore.

### In the news
See news box. Revised statistics change decision inputs; a central bank or firm facing a new inflation series with a different level treats the base-year uncertainty as a state of nature, picking robust actions (minimax regret) until the new series stabilises.

### Interview angle
> [!question] How it is asked
> "Which option would you choose if you cannot estimate the probabilities?"

> [!tip] Strong answer includes
> - Name each criterion and its attitude to risk
> - Regret table done correctly
> - EMV and EVPI when probabilities exist
> - Mention utility/risk appetite and sensitivity to the probabilities

---

## 7. Simulation-Based Statistics
> 🟠 Tier 2 · _Tracker hint:_ Bootstrap resampling; Monte Carlo for confidence intervals

### Definition
When formulas are hard or assumptions are shaky, use the computer to simulate.

- **Bootstrap (Efron):** resample your data **with replacement** (same size $n$) many times (say 5,000 to 10,000), compute the statistic each time, and use the distribution of results for standard errors and **percentile confidence intervals** (2.5th and 97.5th percentiles). Works for medians, ratios, percentiles and other statistics lacking simple formulas. Poor for extremes (max) and very small samples.
- **Monte Carlo simulation:** draw random inputs from assumed distributions, compute the output many times, and summarise the distribution (project completion time, NPV risk, inventory shortfall, queue waits). Accuracy improves as $1/\sqrt{N}$.
- **Permutation tests** shuffle labels to build a null distribution.

```python
import numpy as np
rng = np.random.default_rng(42)
x = np.array([3, 4, 4, 5, 9, 6, 4, 7])
boots = [rng.choice(x, size=len(x), replace=True).mean() for _ in range(10_000)]
print(np.percentile(boots, [2.5, 97.5]))   # 95% bootstrap CI for the mean
```

### Example
Project with three sequential tasks, durations triangular (min, mode, max) in days: A (4, 5, 8), B (6, 8, 12), C (3, 4, 7). Simulate 10,000 times, sum durations, and read the 90th percentile as a planning date. The sum of the three modes is 17 days, but because the distributions are right-skewed the mean is higher than 17: the triangular mean is $(a+m+b)/3$, so $(17/3)+(26/3)+(14/3)=57/3=19$ days.

### In the news
See news box. Agencies cannot re-survey a whole country; uncertainty in survey-based indices such as the CPI can be assessed by resampling methods (bootstrap or replicate weights), though the article does not state which method MoSPI uses.

### Interview angle
> [!question] How it is asked
> "How would you estimate the risk that a project finishes late?" or "What is bootstrapping?"

> [!tip] Strong answer includes
> - Bootstrap steps: resample with replacement, compute statistic, take percentiles
> - Monte Carlo steps: distributions, many runs, summarise output
> - When it beats formulas; limits (garbage in, garbage out)
> - Number of iterations and reproducibility (seed)

---

## 8. Bayesian vs Frequentist
> 🟠 Tier 2 · _Tracker hint:_ Prior belief + data → posterior (Bayesian) vs repeated sampling inference (Frequentist)

### Definition
**Frequentist:** probability is long-run frequency; parameters are fixed unknowns; inference via sampling distributions: p-values, confidence intervals, hypothesis tests. A 95% CI means that 95% of intervals from repeated samples would cover the truth.

**Bayesian:** probability expresses degrees of belief; parameters have distributions. Update a **prior** with data through Bayes' theorem:

$$P(\theta\mid D)=\frac{P(D\mid\theta)\,P(\theta)}{P(D)}\ \Longrightarrow\ \text{posterior}\propto\text{likelihood}\times\text{prior}$$

Results are direct statements: "probability that conversion exceeds 12% is 80%", with **credible intervals**. Conjugate example: Beta prior + binomial data gives a Beta posterior. Strengths: uses prior knowledge, works with small samples, gives decision-ready probabilities; weaknesses: prior choice is subjective, computation (MCMC). With lots of data the two usually agree.

### Example
Prior belief: conversion about 10%, expressed as Beta(2, 18) (mean $2/20=10\%$). Data: 30 conversions in 200 visitors. Posterior = Beta(2+30, 18+170) = Beta(32, 188), mean $=32/220=14.5\%$. Frequentist estimate $30/200=15\%$. The prior pulls the estimate slightly toward 10%. Rare-event disease testing is the classic Bayes' theorem case: with 1% prevalence, 95% sensitivity and 95% specificity, $P(\text{disease}\mid+)=\dfrac{0.95\times0.01}{0.95\times0.01+0.05\times0.99}=\dfrac{0.0095}{0.0590}=16.1\%$.

### In the news
See news box. Revised statistics are an updating problem: when a new CPI series arrives, a Bayesian forecaster treats the old model's output as a prior and updates it with the new data; frequentist practice is to re-estimate.

### Interview angle
> [!question] How it is asked
> "Explain the difference between Bayesian and frequentist approaches to a business person." or "A test is 95% accurate and says positive. What is the chance you actually have the condition?"

> [!tip] Strong answer includes
> - One-line contrast: fixed parameter and long-run frequency vs belief updated by data
> - Bayes' theorem with a worked base-rate example
> - Practical uses: Bayesian A/B testing, spam filters, demand forecasting with little data
> - Weigh prior subjectivity against interpretability

---

## 9. ⭐ Advanced: Deflating Series, Base Shifting and Splicing
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Deflating (real vs nominal):** convert nominal values to constant prices: $\text{Real}=\dfrac{\text{Nominal}}{\text{Price index}}\times100$. Needed for real wages, real GDP, real sales growth.
- **Base shifting:** move an index to a new base period: $I_{new\,base}=\dfrac{I_{old}}{I_{old\ at\ new\ base\ year}}\times100$.
- **Splicing (linking):** join an old series and a new re-based series using the overlap period: multiply the old series by the **linking factor** $=\dfrac{\text{new at overlap}}{\text{old at overlap}}$ to get one continuous series.
- **Real wage** $=$ nominal wage deflated by CPI; **purchasing power** of money $=100/CPI$.
- **Dearness allowance and escalation clauses** use CPI to adjust pay and contracts: choose the right index (CPI-IW for industrial workers, CPI-Combined, WPI for supplier contracts).
- Index tests: time-reversal, factor-reversal, circular test.

### Example
Nominal sales ₹1,200 crore in 2024; price index 120 (base 2020 = 100). Real sales $=1200/120\times100=₹1{,}000$ crore (at 2020 prices). Base shift: index in 2024 is 150, in 2022 is 125 (base 2020 = 100): re-based to 2022, the 2024 index $=150/125\times100=120$. Splice: if old index is 160 and new index is 100 in the overlap year, the linking factor is $100/160=0.625$; an old value of 144 becomes $144\times0.625=90$ on the new base.

### In the news
See news box. The new 2024-base CPI and the old 2011-12 series cannot simply be compared; users of CPI-linked contracts, wage agreements and economic time series need linking factors to splice them.

### Interview angle
> [!question] How it is asked
> "Revenue grew 12% but inflation was 6%. What is the real growth?"

> [!tip] Strong answer includes
> - Real growth $\approx\dfrac{1.12}{1.06}-1\approx5.7\%$ (not 6% by subtraction)
> - Deflating formula and choice of the appropriate index
> - Splicing when a series is re-based
> - Mention CPI-linked contracts or escalation clauses

---

## 10. ⭐ Advanced: Simpson's Paradox, Correlation vs Causation and Misleading Statistics
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Simpson's paradox:** a trend that appears in several groups reverses when the groups are combined, because group sizes differ (a **lurking/confounding variable**).
- **Correlation is not causation:** a third variable, reverse causality, or chance can produce correlation; **randomised experiments** (A/B tests) or causal methods (difference-in-differences, instrumental variables, matching) support causal claims.
- **Common traps:** survivorship bias, selection bias, base-rate neglect, cherry-picking time windows, misleading axes, averaging averages, **ecological fallacy**, p-hacking, regression to the mean, and mixing up percentage change with percentage-point change.
- **Always ask:** What is the denominator? What is the comparison group? Who is missing from the data? What is the sample size and uncertainty?
- Present with context: ranges, base rates, and absolute as well as relative changes.

### Example
Classic kidney-stone study (Charig et al., 1986): Treatment A succeeded in 273/350 = 78% of cases, B in 289/350 = 82.6%, so B looks better overall. But within small stones A is 81/87 = 93.1% vs B 234/270 = 86.7%, and within large stones A is 192/263 = 73.0% vs B 55/80 = 68.8%. A wins in both groups; B looks better overall because it was used mostly on easier (small stone) cases. Business analogue: a channel's conversion looks worse overall only because it is used more on harder segments.

### In the news
See news box. Headline comparisons such as "inflation was 2.75% against 1.3% last month" mix two different baskets and bases: a like-for-like trap of the same family. Always check that two numbers are comparable before reading change.

### Interview angle
> [!question] How it is asked
> "Region A has a higher conversion rate than region B in every segment, yet B's overall rate is higher. How?"

> [!tip] Strong answer includes
> - Name Simpson's paradox and explain it by mix shift or weights
> - Recommend analysing by segment and thinking about confounders
> - Distinguish correlation from causation; propose a randomised test
> - Mention percentage vs percentage point, and base-rate clarity

---
## 🔗 Go deeper: expansion notes
- [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory|Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]
- [[211 Reliability & Survival Analysis|Reliability & Survival Analysis]]
