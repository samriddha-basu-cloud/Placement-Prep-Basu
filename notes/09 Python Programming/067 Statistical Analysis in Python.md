---
tags: [python-programming, tier1]
area: Python Programming
topic: "Statistical Analysis in Python"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Statistical Analysis in Python

⬅ [[066 Demand Forecasting & Time Series]] · [[_Index - Python Programming|Python Programming]] · [[068 Operations-Specific Python (PuLP, SimPy)]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Descriptive Stats]]
2. [[#2. Hypothesis Testing]]
3. [[#3. Correlation]]
4. [[#4. Linear Regression]]
5. [[#5. Distribution Testing]]
6. [[#6. Confidence Intervals]]
7. [[#7. ANOVA]]
8. [[#8. Monte Carlo Simulation]]
9. [[#9. Optimization with SciPy]]
10. [[#10. A/B Test in Python]]
11. [[#11. ⭐ Advanced: Power, Effect Size and Multiple Testing]]
12. [[#12. ⭐ Advanced: Bootstrap and Permutation Tests]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the Python data stack keeps moving, so know the versions you quote
> **SciPy 1.16.0 (released 22 June 2025).** Adds an `equal_var` keyword to `scipy.stats.f_oneway` (enabling Welch's ANOVA when variances are unequal) and to `tukey_hsd` (enabling Games-Howell), a new `quantile` function, and a rewritten COBYLA optimiser in `scipy.optimize` based on the PRIMA package. Requires Python 3.11-3.13. ([SciPy 1.16.0 release notes](https://docs.scipy.org/doc/scipy-1.16.0/release/1.16.0-notes.html))
>
> **pandas 3.0.0 (21 January 2026).** Strings now default to a dedicated `str` dtype, Copy-on-Write becomes the default (chained assignment such as `df[df['a'] > 5]['b'] = 1` no longer works and `SettingWithCopyWarning` is removed), a new `pd.col()` expression syntax is added, and the minimum Python is 3.11. ([pandas 3.0.0 what's new](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Descriptive Stats
> 🔴 Tier 1 · _Tracker hint:_ df.describe(), df.skew(), df.kurt(), scipy.stats.describe()

### Definition
Descriptive statistics summarise a dataset without inferring anything about a wider population. Three families matter:

- **Centre:** mean $\bar{x}=\frac{1}{n}\sum x_i$, median (robust to outliers), mode.
- **Spread:** variance, standard deviation (sample uses $n-1$, so `ddof=1`, the pandas default; NumPy defaults to `ddof=0`), IQR $=Q_3-Q_1$, range, coefficient of variation $CV=s/\bar{x}$.
- **Shape:** skewness (asymmetry; positive means a long right tail) and excess kurtosis (tail heaviness; 0 for a normal, positive means fat tails).

```python
import pandas as pd
from scipy import stats

df = pd.read_csv("orders.csv")
print(df["lead_time"].describe())        # count, mean, std, min, quartiles, max
print(df["lead_time"].skew(), df["lead_time"].kurt())   # kurt() is excess kurtosis
print(stats.describe(df["lead_time"]))   # n, minmax, mean, variance, skewness, kurtosis
print(df.groupby("supplier")["lead_time"].agg(["mean", "median", "std"]))
```

When mean > median the distribution is usually right-skewed (lead times, order values, salaries), so report the median and IQR, not just the mean.

### Example
Delivery times (days) for 8 orders: 2, 3, 3, 4, 5, 5, 6, 20.
Mean = 48/8 = **6.0**; median = (4+5)/2 = **4.5**. The single 20-day order drags the mean above the median, so the data are right-skewed; "typical" delivery is closer to 4.5 days. A good analyst reports both and flags the outlier for root-cause checking.

### In the news
See news box. pandas 3.0 and SciPy 1.16 are the versions you will meet in 2026 notebooks; `describe()` itself is unchanged, but string columns now carry the `str` dtype so `describe(include='object')` style code needs a check.

### Interview angle
> [!question] How it is asked
> "You get a dataset of order delivery times. How would you summarise it before building anything?" or "Mean is 6, median is 4.5. What does that tell you?"

> [!tip] Strong answer includes
> - Mean vs median gap signals skew; recommend median/IQR and a histogram or box plot
> - Mention `describe()`, skewness/kurtosis, missing values and outlier checks before modelling
> - Sample vs population standard deviation (`ddof`)
> - Segment the summary (`groupby`) because overall averages hide supplier/region differences

---

## 2. Hypothesis Testing
> 🔴 Tier 1 · _Tracker hint:_ from scipy import stats; stats.ttest_1samp(), stats.ttest_ind(), stats.chi2_contingency()

### Definition
Hypothesis testing asks whether an observed difference is plausibly just sampling noise. Steps: state $H_0$ (no effect) and $H_1$; pick significance level $\alpha$ (usually 0.05); compute a test statistic; get the **p-value** = probability of seeing a result at least this extreme if $H_0$ were true. If $p<\alpha$, reject $H_0$.

| Question | Test | SciPy call |
|---|---|---|
| Is the mean different from a target? | One-sample t | `stats.ttest_1samp(x, popmean)` |
| Do two independent groups differ in mean? | Welch / Student t | `stats.ttest_ind(a, b, equal_var=False)` |
| Same units measured before and after? | Paired t | `stats.ttest_rel(before, after)` |
| Are two categorical variables associated? | Chi-square | `stats.chi2_contingency(table)` |
| Non-normal two-group comparison | Mann-Whitney U | `stats.mannwhitneyu(a, b)` |

Test statistic for one-sample t: $t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}$ with $n-1$ degrees of freedom. A p-value is **not** the probability that $H_0$ is true, and "not significant" is not "no effect" (it may be low power). Type I error = false positive ($\alpha$); Type II = false negative ($\beta$); power $=1-\beta$.

### Example
A vendor promises a mean lead time of 7 days. You sample n = 25 orders: $\bar{x}=8.2$, $s=3$.
$t=(8.2-7)/(3/\sqrt{25})=1.2/0.6=2.0$, df = 24. Two-sided critical value at 5% is about 2.064, so $p\approx0.057$: not significant at 5%, though suggestive; collect more data rather than declare the vendor compliant.

Chi-square example: supplier A has 10 defects in 200 units, supplier B 30 in 300. Overall defect rate 40/500 = 8%, so expected defects are 16 (A) and 24 (B). $\chi^2=\frac{(10-16)^2}{16}+\frac{(190-184)^2}{184}+\frac{(30-24)^2}{24}+\frac{(270-276)^2}{276}\approx2.25+0.20+1.50+0.13=4.08$, df = 1, above 3.84, so $p\approx0.043$ (this is without continuity correction, `correction=False`; SciPy applies Yates' correction to 2x2 tables by default, giving a somewhat larger p).

### In the news
See news box. SciPy 1.16's `equal_var` option and Welch-by-default habits (`equal_var=False`) matter whenever two suppliers or variants have unequal variances.

### Interview angle
> [!question] How it is asked
> "How would you check whether a new packaging line really reduced damage rates?" or "Explain p-value to a non-technical manager."

> [!tip] Strong answer includes
> - Clear $H_0$/$H_1$, choice of test justified by data type (means vs proportions, paired vs independent)
> - Correct p-value meaning, plus effect size and confidence interval, not p alone
> - Assumptions: independence, rough normality or large n, Welch if variances differ
> - Practical vs statistical significance; type I/II errors and power

---

## 3. Correlation
> 🔴 Tier 1 · _Tracker hint:_ df.corr() — Pearson; df.corr(method='spearman'); sns.heatmap(df.corr(), annot=True)

### Definition
Correlation measures the strength and direction of association, from −1 to +1.

- **Pearson** $r=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i-\bar{x})^2\sum(y_i-\bar{y})^2}}$ measures *linear* association; sensitive to outliers.
- **Spearman** is Pearson on the ranks: captures any monotonic relationship, robust to outliers and works for ordinal data.
- **Kendall tau** is another rank measure, better for small samples with ties.

```python
import seaborn as sns, matplotlib.pyplot as plt
num = df.select_dtypes("number")
corr = num.corr()                          # Pearson by default
rho = num.corr(method="spearman")
sns.heatmap(corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.show()

from scipy import stats
r, p = stats.pearsonr(df["ad_spend"], df["sales"])   # r and its p-value
```

Cautions: correlation is not causation; a confounder (festival season drives both ad spend and sales) can create it; $r\approx0$ does not rule out a non-linear relationship; always plot a scatter. Multicollinearity (high $r$ between predictors) destabilises regression coefficients.

### Example
Monthly ad spend and sales for a D2C brand give $r=0.92$. Both rise in Diwali months, so the true effect of ads may be much smaller. Checking Spearman and a partial correlation controlling for a festival-month dummy tests this. (Illustrative scenario.)

### In the news
Not tied to a specific development; applies the same way after the pandas 3.0 release (see news box for version context): `df.corr(numeric_only=True)` remains the safe call when string columns are present.

### Interview angle
> [!question] How it is asked
> "Sales and ad spend have 0.9 correlation. Should we double the ad budget?"

> [!tip] Strong answer includes
> - "Correlation is not causation"; name a confounder and propose an experiment or regression with controls
> - Pearson (linear, outlier-sensitive) vs Spearman (monotonic, rank-based)
> - Always visualise (scatter, heatmap) and check for outliers
> - Multicollinearity warning when selecting features

---

## 4. Linear Regression
> 🔴 Tier 1 · _Tracker hint:_ from sklearn.linear_model import LinearRegression; model.fit(X,y); model.coef_, model.intercept_

### Definition
Linear regression models $y=\beta_0+\beta_1x_1+\dots+\beta_kx_k+\varepsilon$, estimating coefficients by **ordinary least squares** (minimise $\sum(y_i-\hat{y}_i)^2$). In simple regression $\beta_1=\frac{S_{xy}}{S_{xx}}$ and $\beta_0=\bar{y}-\beta_1\bar{x}$. Fit quality: $R^2=1-\frac{SS_{res}}{SS_{tot}}$ (share of variance explained); adjusted $R^2$ penalises extra predictors; RMSE/MAE measure error in the unit of $y$.

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
X = df.loc[:, ["ad_spend", "price"]]; y = df["sales"]
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression().fit(Xtr, ytr)
print(model.coef_, model.intercept_, model.score(Xte, yte))   # score = R^2

import statsmodels.api as sm                  # for p-values and CIs
res = sm.OLS(y, sm.add_constant(X)).fit(); print(res.summary())
```

scikit-learn gives predictions; **statsmodels** gives inference (p-values, confidence intervals). Assumptions (LINE): linearity, independence, normal residuals, equal variance. Check residual plots; watch for multicollinearity (VIF) and outliers.

### Example
Ad spend (Rs lakh) x = 1, 2, 3, 4, 5 and sales (Rs lakh) y = 12, 15, 19, 24, 25.
$\bar{x}=3$, $\bar{y}=19$; $S_{xy}=(-2)(-7)+(-1)(-4)+0+(1)(5)+(2)(6)=35$; $S_{xx}=10$.
Slope $=3.5$; intercept $=19-3.5\times3=8.5$. So $\hat{y}=8.5+3.5x$: each extra Rs 1 lakh of ads is associated with Rs 3.5 lakh more sales. $S_{yy}=126$, $SS_{reg}=3.5^2\times10=122.5$, so $R^2=122.5/126\approx0.97$.

### In the news
See news box. In pandas 3.0 chained assignment (`df[mask]['col'] = v`) no longer modifies the original, so feature engineering code should use `df.loc[mask, 'col'] = v`.

### Interview angle
> [!question] How it is asked
> "How do you interpret regression coefficients and how do you know the model is good?"

> [!tip] Strong answer includes
> - Coefficient meaning ("holding others constant"), $R^2$ vs out-of-sample error
> - Train/test split, residual diagnostics, multicollinearity (VIF)
> - Difference between prediction (sklearn) and inference (statsmodels)
> - Warn against extrapolation and omitted-variable bias

---

## 5. Distribution Testing
> 🔴 Tier 1 · _Tracker hint:_ stats.shapiro(data) for normality; stats.kstest() for goodness of fit

### Definition
Many methods (t-tests, control charts, safety-stock formulas, process capability) assume normality, so we test it.

- **Shapiro-Wilk** `stats.shapiro(x)`: best power for small to medium samples (n up to a few thousand). $H_0$: data come from a normal distribution; small $p$ means reject normality.
- **Kolmogorov-Smirnov** `stats.kstest(x, 'norm', args=(mu, sigma))`: compares the empirical CDF with a fully specified theoretical CDF; estimating parameters from the same data makes the p-value too lenient (use Lilliefors via statsmodels). `stats.ks_2samp` compares two samples.
- **Anderson-Darling** `stats.anderson`, **D'Agostino** `stats.normaltest`.
- Visual checks: histogram, Q-Q plot (`stats.probplot`).

```python
stat, p = stats.shapiro(df["daily_demand"])
print("normal-looking" if p > 0.05 else "not normal", p)
stats.kstest(df["daily_demand"], "norm", args=(df["daily_demand"].mean(), df["daily_demand"].std()))
```

With large n tests reject for trivial deviations, and with small n they lack power, so always pair with a Q-Q plot. If not normal: transform (log, Box-Cox `stats.boxcox`) or use non-parametric tests.

### Example
Daily demand for 40 days gives Shapiro W = 0.97, p = 0.35 (illustrative numbers): $p>0.05$, so no evidence against normality and the safety stock formula $z\sigma\sqrt{L}$ is reasonable. If instead p = 0.001 and the Q-Q plot bends upward at the right end, demand is right-skewed (lumpy B2B orders) and a normal-based safety stock under-protects against spikes.

### In the news
See news box. Not a headline topic; use SciPy 1.16 as the current stable reference when you cite function names.

### Interview angle
> [!question] How it is asked
> "How do you check that demand is normally distributed before computing safety stock?"

> [!tip] Strong answer includes
> - Q-Q plot plus Shapiro-Wilk; state $H_0$ correctly
> - Limits: sensitivity to sample size; KS needs known parameters
> - Remedies: transformation, empirical or bootstrap percentiles, non-parametric tests
> - Link to business impact (service level at the tail)

---

## 6. Confidence Intervals
> 🔴 Tier 1 · _Tracker hint:_ stats.t.interval(0.95, df=n-1, loc=mean, scale=sem) — t-distribution CI

### Definition
A **95% confidence interval** is a range constructed by a procedure that captures the true parameter in 95% of repeated samples. It is *not* "95% probability the parameter lies in this particular interval". For a mean with unknown $\sigma$: $\bar{x}\pm t_{\alpha/2,\,n-1}\cdot\frac{s}{\sqrt{n}}$, where $s/\sqrt{n}$ is the standard error (SEM). For a proportion (large n): $\hat{p}\pm z\sqrt{\hat{p}(1-\hat{p})/n}$.

```python
import numpy as np
from scipy import stats
x = df["lead_time"].to_numpy()
n, m, sem = len(x), x.mean(), stats.sem(x)          # sem uses ddof=1
lo, hi = stats.t.interval(0.95, df=n-1, loc=m, scale=sem)
```

(Older SciPy versions used the argument name `alpha` for the confidence level; recent releases use `confidence`, so pass it positionally as above.) Wider interval means less precision; width shrinks with $1/\sqrt{n}$, so quadrupling the sample halves the width. For skewed data or medians, use `stats.bootstrap`.

### Example
n = 16 orders, mean lead time 50 hours, s = 8. SEM $=8/\sqrt{16}=2$. $t_{0.975,15}=2.131$. Margin $=2.131\times2=4.26$, so the 95% CI is **(45.74, 54.26)** hours. A promise of "48 hours average" is plausible; a promise of 40 is not.

### In the news
See news box. SciPy's `scipy.stats.bootstrap` (long available, actively maintained in the 1.16 line) is the go-to when a closed-form CI does not exist.

### Interview angle
> [!question] How it is asked
> "What does a 95% confidence interval mean?" or "Your A/B uplift is 2% with CI of -0.5% to 4.5%. Do you ship?"

> [!tip] Strong answer includes
> - Correct frequentist interpretation (procedure, not a probability about the parameter)
> - Formula with t vs z and the role of sample size
> - Using CI to judge practical significance, and that it spans zero here
> - Mention bootstrap for non-standard statistics

---

## 7. ANOVA
> 🔴 Tier 1 · _Tracker hint:_ stats.f_oneway(group1, group2, group3) — one-way ANOVA; p-value interpretation

### Definition
One-way **ANOVA** tests whether three or more group means are equal ($H_0:\mu_1=\mu_2=\dots=\mu_k$). Running many t-tests inflates the false-positive rate, so ANOVA uses one F-test:
$F=\frac{MS_{between}}{MS_{within}}=\frac{SS_B/(k-1)}{SS_W/(N-k)}$.
A large $F$ (small $p$) means at least one mean differs; it does not say which. Follow with a post-hoc test: `stats.tukey_hsd(a, b, c)` or statsmodels `pairwise_tukeyhsd`.

```python
from scipy import stats
F, p = stats.f_oneway(plant_a, plant_b, plant_c)
res = stats.tukey_hsd(plant_a, plant_b, plant_c)
print(F, p); print(res)
```

Assumptions: independent observations, roughly normal residuals, equal variances (check Levene: `stats.levene`). If variances differ, use Welch's ANOVA (`f_oneway(..., equal_var=False)` in SciPy 1.16+) or Kruskal-Wallis (`stats.kruskal`) for non-normal data. Two-way ANOVA (statsmodels `anova_lm`) adds a second factor and interaction.

### Example
Defect counts per batch for three plants: A = 4, 5, 6; B = 6, 7, 8; C = 8, 9, 10. Group means 5, 7, 9; grand mean 7.
$SS_B=3(4+0+4)=24$; $SS_W=2+2+2=6$; $df_B=2$, $df_W=6$.
$MS_B=12$, $MS_W=1$, so $F=12$. The 5% critical value for F(2, 6) is 5.14, so reject $H_0$: plants differ. Tukey then shows A vs C is the largest gap.

### In the news
See news box. SciPy 1.16 added `equal_var` to `f_oneway` (Welch ANOVA) and `tukey_hsd` (Games-Howell), which directly addresses the unequal-variance problem common in plant or vendor comparisons.

### Interview angle
> [!question] How it is asked
> "Three warehouses report different pick rates. How do you test whether the difference is real?"

> [!tip] Strong answer includes
> - Why not multiple t-tests (familywise error)
> - F-statistic as between-group over within-group variance
> - Post-hoc test to locate the difference; assumptions and Welch/Kruskal fallbacks
> - Report effect size (eta-squared) as well as p

---

## 8. Monte Carlo Simulation
> 🔴 Tier 1 · _Tracker hint:_ np.random.normal(mean, std, n_simulations) — inventory/project risk simulation

### Definition
Monte Carlo simulation estimates the distribution of an outcome by drawing many random samples of the uncertain inputs and computing the outcome each time. By the law of large numbers, the sample statistic converges to the true value; the error shrinks as $1/\sqrt{N}$.

```python
import numpy as np
rng = np.random.default_rng(42)                 # modern, reproducible generator
N = 100_000
demand = rng.normal(500, 80, N)                 # demand during lead time
stockout_prob = (demand > 600).mean()
p95 = np.percentile(demand, 95)                 # stock needed for 95% service

# project duration: sum of triangular task times
t1 = rng.triangular(4, 6, 10, N); t2 = rng.triangular(3, 5, 9, N)
total = t1 + t2
print(np.percentile(total, [50, 80, 90]))
```

Use it when closed-form maths is hard: correlated inputs, non-normal distributions, multi-stage systems (inventory with random demand and lead time, PERT projects, financial risk). Always fix a seed, justify input distributions with data, and report percentiles (P50/P80/P90), not just the mean.

### Example
Demand during lead time ~ Normal(mean 500, sd 80) and you hold 600 units. Analytical: $z=(600-500)/80=1.25$, $P(D>600)=1-\Phi(1.25)\approx10.6\%$. A 100,000-draw simulation returns about 10.6% too. For 95% service you need $500+1.645\times80\approx632$ units.

### In the news
See news box. NumPy's `default_rng` plus SciPy's `stats.qmc` (quasi-Monte Carlo) are the modern reproducible tools; pandas 3.0's Copy-on-Write helps keep simulation result frames free of accidental mutation.

### Interview angle
> [!question] How it is asked
> "How would you estimate the probability our project finishes on time when task durations are uncertain?"

> [!tip] Strong answer includes
> - Define input distributions from data (triangular/PERT/normal), simulate N runs, read percentiles
> - Explain why it beats using averages (flaw of averages)
> - Mention seed, convergence check and correlated inputs
> - Translate output to a decision (buffer, safety stock, contingency)

---

## 9. Optimization with SciPy
> 🔴 Tier 1 · _Tracker hint:_ from scipy.optimize import minimize, linprog; supply chain cost minimization

### Definition
`scipy.optimize` solves two big classes:

- **Linear programs:** `linprog(c, A_ub, b_ub, A_eq, b_eq, bounds)` minimises $c^Tx$ subject to $A_{ub}x\le b_{ub}$, $A_{eq}x=b_{eq}$. Default method is HiGHS. It always *minimises*, so negate the objective to maximise, and write $\ge$ constraints as $\le$ by multiplying by −1. Variable bounds default to $x\ge0$.
- **Nonlinear problems:** `minimize(fun, x0, method='SLSQP', bounds=..., constraints=...)`. Good for smooth cost curves such as EOQ with quantity discounts.

For integer decisions (open or close a warehouse) SciPy has `milp`; for modelling large LPs, PuLP or OR-Tools are friendlier (see [[068 Operations-Specific Python (PuLP, SimPy)]]).

```python
from scipy.optimize import linprog, minimize
# min 2x + 3y  s.t. x + y >= 100, x <= 60, x,y >= 0
res = linprog(c=[2, 3], A_ub=[(-1, -1)], b_ub=[-100], bounds=[(0, 60), (0, None)])
print(res.x, res.fun)

# EOQ by minimisation: total cost = D*S/Q + H*Q/2
D, S, H = 12000, 500, 24
f = lambda q: D*S/q[0] + H*q[0]/2
print(minimize(f, x0=[100], bounds=[(1, None)]).x)
```

### Example
Two plants ship 100 units: plant X costs Rs 2/unit with capacity 60, plant Y costs Rs 3/unit. Optimal: ship 60 from X and 40 from Y; cost $=60\times2+40\times3=$ Rs 240. The solver's `res.x = [60, 40]`, `res.fun = 240`. EOQ check: $\sqrt{2\times12000\times500/24}\approx707$ units, which `minimize` should reproduce.

### In the news
See news box. SciPy 1.16 swapped COBYLA for a PRIMA-based implementation with fewer function evaluations; the LP route (`linprog`/HiGHS) is unchanged and remains the right tool for linear supply chain models.

### Interview angle
> [!question] How it is asked
> "How would you decide shipment quantities from plants to DCs to minimise cost?"

> [!tip] Strong answer includes
> - Decision variables, objective, constraints (capacity, demand) stated before any code
> - LP vs nonlinear vs integer programming and the right library
> - Sensitivity analysis (shadow prices, `res.ineqlin.marginals`)
> - Sanity-check the solution against a simple heuristic

---

## 10. A/B Test in Python
> 🔴 Tier 1 · _Tracker hint:_ stats.proportions_ztest([conversions],[total]) — test significance of A/B results

### Definition
An A/B test randomly assigns users to control (A) and variant (B), then tests whether the metric differs more than chance allows. For conversion rates use a two-proportion z-test:
$z=\frac{\hat{p}_B-\hat{p}_A}{\sqrt{\hat{p}(1-\hat{p})(1/n_A+1/n_B)}}$, with pooled $\hat{p}=\frac{x_A+x_B}{n_A+n_B}$.

```python
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
count = [250, 200]      # conversions: B first, then A
nobs  = [2000, 2000]
z, p = proportions_ztest(count, nobs)           # two-sided by default
print(z, p)

# sample size BEFORE the test
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
es = proportion_effectsize(0.12, 0.10)
n = NormalIndPower().solve_power(es, power=0.8, alpha=0.05, ratio=1)
```

Good practice: fix sample size and duration in advance (do not peek and stop on the first significant reading), pre-register one primary metric, randomise at the right unit, run whole weeks to cover weekly cycles, check sample-ratio mismatch, and correct for multiple metrics/variants. For continuous metrics use `stats.ttest_ind(..., equal_var=False)`. Note `proportions_ztest` lives in `statsmodels`, not SciPy.

### Example
A: 200 of 2000 convert (10.0%); B: 250 of 2000 (12.5%). Pooled $\hat{p}=450/4000=0.1125$; SE $=\sqrt{0.1125\times0.8875\times(1/2000+1/2000)}=\sqrt{0.0000998}\approx0.00999$; $z=0.025/0.00999\approx2.50$; $p\approx0.012$. Significant at 5%. Planning check: detecting 10% to 12% at 80% power needs about 3,834 users per arm ($n=\frac{(1.96+0.84)^2\,(0.09+0.1056)}{0.02^2}$; equivalently $n=2\left(\frac{1.96+0.84}{h}\right)^2$ with Cohen's $h\approx0.064$), so 2,000 per arm is under-powered for a 2-point lift (a true 10% to 12.5% lift needs about 2,500 per arm); a significant result from an under-powered test tends to overstate the effect.

### In the news
See news box. Welch-style options added to SciPy's ANOVA help when you compare more than two variants (A/B/C tests) with unequal variances.

### Interview angle
> [!question] How it is asked
> "Variant B has a higher conversion rate after 3 days. Should we launch it?"

> [!tip] Strong answer includes
> - No: check pre-planned sample size, significance, practical lift and guardrail metrics
> - Peeking inflates false positives; use sequential methods only if designed for it
> - Novelty effects, sample-ratio mismatch, multiple-comparison correction
> - State the decision rule and business cost of a wrong call

---

## 11. ⭐ Advanced: Power, Effect Size and Multiple Testing
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A result needs more than $p<0.05$:

- **Effect size** quantifies magnitude: Cohen's $d=\frac{\bar{x}_1-\bar{x}_2}{s_p}$ for means (0.2 small, 0.5 medium, 0.8 large by convention), Cohen's $h$ for proportions, eta-squared for ANOVA.
- **Power** $=1-\beta$: the chance of detecting a real effect. Sample size per group for two means: $n\approx\frac{2(z_{1-\alpha/2}+z_{1-\beta})^2\sigma^2}{\Delta^2}$.
- **Multiple testing:** with $m$ independent tests at $\alpha=0.05$, the chance of at least one false positive is $1-0.95^m$. Corrections: **Bonferroni** (use $\alpha/m$, conservative), **Holm**, **Benjamini-Hochberg** (controls false discovery rate).

```python
from statsmodels.stats.multitest import multipletests
reject, p_adj, _, _ = multipletests(pvals, alpha=0.05, method="fdr_bh")
```

Non-parametric and resampling alternatives: `stats.mannwhitneyu`, `stats.kruskal`, `stats.bootstrap`, `stats.permutation_test`.

### Example
You test 20 metrics in one experiment at $\alpha=0.05$. P(at least one false positive) $=1-0.95^{20}\approx64\%$. Bonferroni threshold $=0.05/20=0.0025$. A "winning" metric with $p=0.03$ should not be celebrated.

### In the news
See news box. SciPy 1.16's added Games-Howell and Welch ANOVA options are examples of the library catching up with robust post-hoc practice.

### Interview angle
> [!question] How it is asked
> "We checked 15 KPIs and one improved significantly. Is the experiment a success?"

> [!tip] Strong answer includes
> - Compute the false-positive probability across many tests; propose one primary metric
> - Bonferroni/Holm vs Benjamini-Hochberg trade-off
> - Power analysis up front; minimum detectable effect tied to business value
> - Report effect size with CI, not only p

---

## 12. ⭐ Advanced: Bootstrap and Permutation Tests
> ⭐ Advanced · _Added beyond the tracker_

### Definition
When distributions are unknown or the statistic is awkward (median, ratio, 90th percentile, Gini), resample instead of using formulas.

- **Bootstrap:** resample the data *with replacement* many times, compute the statistic each time, and use the spread (percentile or BCa interval) as its sampling distribution.
- **Permutation test:** shuffle group labels many times to build the null distribution of the difference; $p$ = fraction of shuffles at least as extreme as observed.

```python
import numpy as np
from scipy import stats
x = np.array(lead_times)
ci = stats.bootstrap((x,), np.median, confidence_level=0.95, n_resamples=9999, method="BCa")
print(ci.confidence_interval)

res = stats.permutation_test((a, b), lambda u, v: np.mean(u) - np.mean(v),
                             permutation_type="independent", n_resamples=9999)
print(res.pvalue)
```

Assumes the sample is representative and observations are independent (use block bootstrap for time series). Few assumptions, but computationally heavier and cannot fix a biased sample.

### Example
Median delivery time from 30 orders is 4.5 days. A bootstrap with 9,999 resamples gives a 95% interval such as (3.5, 6.0) days (illustrative): you can tell the customer "median delivery is 4-6 days" without assuming normality.

### In the news
See news box. `scipy.stats.bootstrap` and `permutation_test` are part of the maintained 1.16 API, so they run on current Python 3.11-3.13 stacks.

### Interview angle
> [!question] How it is asked
> "How would you put an error bar on a median when you have only 30 data points and a skewed distribution?"

> [!tip] Strong answer includes
> - Describe resampling with replacement and percentile/BCa interval
> - Compare with t-interval assumptions
> - Mention time-series dependence (block bootstrap) and the limits (biased sample)
> - Permutation test as an assumption-light alternative to a t-test

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
