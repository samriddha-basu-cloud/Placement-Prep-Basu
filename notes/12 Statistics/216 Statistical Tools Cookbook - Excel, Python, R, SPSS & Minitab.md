---
tags: [statistics, tier3]
area: Statistics
topic: "Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab"
tier: Tier 3
roles: All roles
status: complete
subtopics: 14
---
# Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab

⬅ [[215 Statistics Interview Question Bank & Numericals]] · [[_Index - Statistics|Statistics]] · [[217 Probability Puzzles & Applied Problem Solving]] ➡

> **Area:** Statistics · **Priority:** 🟡 Tier 3 · **Target roles:** All roles

## Sub-topics in this note
1. [[#1. Choosing the Right Tool for the Job]]
2. [[#2. Excel: Functions versus the Analysis ToolPak]]
3. [[#3. Descriptive Statistics Across Tools]]
4. [[#4. t-Tests and Non-Parametric Alternatives]]
5. [[#5. ANOVA and Post-hoc Tests]]
6. [[#6. Chi-Square, Correlation and Association]]
7. [[#7. Regression: Tools and How to Read the Table]]
8. [[#8. Regression Diagnostics and Prediction]]
9. [[#9. Control Charts and Process Capability]]
10. [[#10. Design of Experiments in Software]]
11. [[#11. Time Series and Forecasting Tools]]
12. [[#12. Power, Sample Size and A/B Test Calculations]]
13. [[#13. Reporting Results in Plain English]]
14. [[#14. ⭐ Advanced: Reproducible Analysis and Common Tool Pitfalls]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): forecasting and statistics are moving into the spreadsheet and one `pip install`
> **TimesFM reaches Google Sheets and BigQuery ML (README updates, 2026).** Google Research's open TimesFM forecasting model is now listed as available inside BigQuery ML (SQL), in Google Sheets through Connected Sheets (a Workspace update dated February 2026), and in Vertex AI Model Garden. In the repository's September 2026 update, TimesFM 3.0 is described as finishing its rollout in BigQuery ML for commercial and production use, while the downloadable 3.0 weights carry a non-commercial licence. Analysts can therefore reach a modern forecaster from a spreadsheet without writing Python. ([TimesFM repository README](https://github.com/google-research/timesfm))
>
> **Chronos-2 is one `pip install` away (October 2025).** Amazon's Chronos-2 forecaster (120M parameters, Apache 2.0, context up to 8,192 points) loads through the `chronos-forecasting` package and takes pandas DataFrames, with optional covariates; the model card reports state-of-the-art zero-shot accuracy on the fev-bench, GIFT-Eval and Chronos Benchmark II suites. ([Hugging Face model card](https://huggingface.co/amazon/chronos-2); [Amazon Science announcement](https://www.amazon.science/blog/introducing-chronos-2-from-univariate-to-universal-forecasting))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Choosing the Right Tool for the Job
> 🟡 Tier 3 · _Key points:_ Excel for quick answers and stakeholders, Python/R for reproducible work, SPSS/Minitab for menu-driven classroom and shop-floor use

### Definition
The same statistical procedure exists in five common tools; the skill is **matching the tool to the audience and the repeatability needed**.

| Tool | Strength | Weakness | Typical user |
|---|---|---|---|
| **Excel** (functions + Analysis ToolPak) | Everyone has it; quick; shareable | Manual, error-prone, static ToolPak output, limited diagnostics | Managers, finance, ops analysts |
| **Python** (pandas, scipy, statsmodels) | Reproducible, scalable, full diagnostics, ML integration | Coding needed | Data/analytics roles |
| **R** | Best statistical library coverage (tests, DOE, SPC, forecasting) | Less general-purpose than Python | Statisticians, researchers |
| **SPSS** | Point-and-click, readable output, strong in surveys and social science | Licence cost, weaker automation | Market research, academia |
| **Minitab** | Built-in Six Sigma tools: control charts, capability, Gage R&R, DOE | Licence cost, niche | Quality, Lean Six Sigma Black Belts |

Rule of thumb: **one-off answer for a meeting** use Excel; **a number that will be re-computed monthly** write Python/R; **a Six Sigma project report** use Minitab; **a survey cross-tab for a client** use SPSS or Python. Whatever the tool, the workflow is unchanged: check the data, check assumptions, run the test, read the output, report in plain words. The statistical ideas live in [[086 Descriptive Statistics]], [[089 Hypothesis Testing]], [[090 Regression Analysis]] and [[091 Statistical Quality Control (SQC)]]; the Python basics are in [[067 Statistical Analysis in Python]] and the Excel basics in [[072 Logical & Statistical Functions]].

### Example
A plant manager asks, "Is the new supplier slower?" You have 10 deliveries from each supplier. In Excel, `=T.TEST(A2:A11,B2:B11,2,3)` gives the answer in one cell. If the same question must be answered every week for 40 suppliers, a 6-line pandas loop calling `scipy.stats.ttest_ind(..., equal_var=False)` is the right tool. If the CEO wants a signed-off six-sigma deck, Minitab's 2-Sample t dialog produces the graphs.

### In the news
See news box. As forecasting models become callable from SQL and spreadsheets, the choice of tool increasingly depends on governance and repeatability, not on capability.

### Interview angle
> [!question] How it is asked
> "Which tools have you used for statistical analysis, and how do you choose between them?"

> [!tip] Strong answer includes
> - Naming at least one spreadsheet tool and one scripting tool, with a project for each
> - Choosing by audience, repeatability and auditability, not by habit
> - Mentioning that the assumptions and interpretation stay the same across tools
> - Honesty about limits (for example, Excel's static ToolPak output)

---
## 2. Excel: Functions versus the Analysis ToolPak
> 🟡 Tier 3 · _Key points:_ Enable ToolPak; functions are live, ToolPak output is static; T.TEST type argument; read the two-tail p

### Definition
Excel offers two routes. **Worksheet functions** are live formulas that recalculate. The **Analysis ToolPak** is an add-in that writes a static block of results.

**Enable the ToolPak (Windows):** File > Options > Add-ins > Manage: Excel Add-ins > Go > tick *Analysis ToolPak*. It then appears as **Data > Data Analysis**. On Mac use Tools > Excel Add-ins. It is not available in Excel for the web.

**Key functions:**

| Task | Function |
|---|---|
| Mean, median, mode | `AVERAGE`, `MEDIAN`, `MODE.SNGL` |
| Sample SD, variance | `STDEV.S`, `VAR.S` (population: `STDEV.P`, `VAR.P`) |
| Quartiles, percentiles | `QUARTILE.INC`, `PERCENTILE.INC` (the `.EXC` versions differ) |
| Skewness, kurtosis (excess) | `SKEW`, `KURT` |
| 95% CI half-width for a mean | `CONFIDENCE.T(0.05, s, n)` |
| z and t critical values | `NORM.S.INV(0.975)`, `T.INV.2T(0.05, df)` |
| t-test p-value | `T.TEST(range1, range2, tails, type)` where type 1 = paired, 2 = equal variance, **3 = unequal variance (Welch)** |
| F-test for variances | `F.TEST(range1, range2)` (two-tailed) |
| Chi-square p-value | `CHISQ.TEST(actual_range, expected_range)` |
| Correlation, slope, intercept, R² | `CORREL`, `SLOPE`, `INTERCEPT`, `RSQ` |
| Multiple regression array | `LINEST(y, X, TRUE, TRUE)` (enter as dynamic array) |
| Forecasting | `FORECAST.LINEAR`, `FORECAST.ETS`, `FORECAST.ETS.CONFINT` |

**ToolPak menu items:** Descriptive Statistics, t-Test (three versions), z-Test, F-Test, Anova: Single Factor, Anova: Two-Factor (with and without replication), Regression, Correlation, Covariance, Histogram, Moving Average, Exponential Smoothing, Random Number Generation, Rank and Percentile, Sampling. Pitfall: ToolPak outputs **do not update** when the data change, so re-run them; keep them away from reports that must stay live. More Excel material: [[072 Logical & Statistical Functions]], [[043 Advanced Excel (Pivot, Solver, Forecasting)]].

### Example
Supplier A and B lead times (10 deliveries each):

A = 12.1, 13.4, 11.8, 12.9, 14.2, 13.1, 12.6, 13.8, 12.2, 13.5; B = 13.9, 14.8, 13.2, 15.1, 14.4, 13.7, 15.3, 14.1, 14.9, 13.6.

`=T.TEST(A2:A11,B2:B11,2,3)` returns **0.0008** (two-tailed Welch). The ToolPak "t-Test: Two-Sample Assuming Unequal Variances" prints both "P(T<=t) one-tail" and "P(T<=t) two-tail"; for "is B different from A?" read the **two-tail** value, 0.0008, with t Stat −4.007 and a Welch df of about 18 (exact value 17.8).

### In the news
See news box. Spreadsheet-based forecasting (`FORECAST.ETS`, Connected Sheets) is the on-ramp that analysts reach first, which is why knowing what the function assumes matters.

### Interview angle
> [!question] How it is asked
> "How would you run a t-test in Excel, and what would you check first?"

> [!tip] Strong answer includes
> - `T.TEST` with the right type argument, or ToolPak with the right variant
> - Checking equal-variance choice (default to Welch, type 3)
> - Reading the two-tail p-value for a non-directional question
> - Reporting an effect size and CI, not only p
> - Noting that ToolPak output is static and not auditable like a formula

---
## 3. Descriptive Statistics Across Tools
> 🟡 Tier 3 · _Key points:_ Describe, skew, outliers by 1.5 IQR fence, CI of the mean

### Definition
Always summarise before testing: count, mean, SD, five-number summary, skewness, outliers.

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| Summary table | Data > Data Analysis > Descriptive Statistics (tick Summary statistics, Confidence Level) | `df.describe()` | `summary(x)`; `sd(x)` | Analyze > Descriptive Statistics > Descriptives or Explore | Stat > Basic Statistics > Display Descriptive Statistics |
| Histogram | Insert > Histogram | `df.hist()` | `hist(x)` | Graphs > Chart Builder > Histogram | Graph > Histogram |
| Boxplot | Insert > Box and Whisker | `df.boxplot()` | `boxplot(x)` | Analyze > Descriptive Statistics > Explore > Plots | Graph > Boxplot |
| Normality check | Q-Q plot (manual) | `scipy.stats.shapiro(x)` | `shapiro.test(x)` | Explore > Plots > Normality plots with tests | Stat > Basic Statistics > Normality Test |
| 95% CI of mean | `CONFIDENCE.T` | `stats.t.interval(...)` | `t.test(x)$conf.int` | Explore > Statistics | Stat > Basic Statistics > Graphical Summary |

Interpretation cues: a **mean far above the median** signals right skew; the **1.5 × IQR rule** flags outliers (below $Q_1-1.5\,IQR$ or above $Q_3+1.5\,IQR$); **CV** $=s/\bar x$ compares variability across units.

### Example
Lead times (days) of 20 purchase orders: 12, 15, 11, 14, 18, 13, 16, 12, 15, 41, 14, 13, 17, 15, 12, 16, 14, 13, 15, 14.

```python
import pandas as pd
from scipy import stats
s = pd.Series([12,15,11,14,18,13,16,12,15,41,14,13,17,15,12,16,14,13,15,14])
print(s.describe().round(2))
q1, q3 = s.quantile([.25, .75]); iqr = q3 - q1
print("skew", round(s.skew(), 2), "fences", q1 - 1.5*iqr, q3 + 1.5*iqr)
print(stats.t.interval(0.95, len(s)-1, loc=s.mean(), scale=stats.sem(s)))
```

Output: mean 15.50, SD 6.26, median 14, Q1 13, Q3 15.25, IQR 2.25, skewness 3.89, outlier fences 9.63 and 18.63, so the **41-day order** is an outlier and the mean (15.5) is dragged above the median (14). 95% CI for the mean: (12.57, 18.43). Report the **median and IQR** for such skewed data, and investigate the 41-day order rather than deleting it.

### In the news
See news box. Basic descriptive checks remain the first step before feeding data to any pretrained forecaster.

### Interview angle
> [!question] How it is asked
> "You get a dataset; what do you do in the first 15 minutes?"

> [!tip] Strong answer includes
> - Shape, missing values, units, duplicates
> - Mean vs median, SD vs IQR, outliers with a rule, not by eye
> - A plot before a test
> - Decision on treating outliers (investigate, do not silently delete)

---
## 4. t-Tests and Non-Parametric Alternatives
> 🟡 Tier 3 · _Key points:_ Welch by default; paired when the same units are measured twice; read t, df, p and CI together

### Definition

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| One-sample t | no direct function: `=(AVERAGE(x)-mu)/(STDEV.S(x)/SQRT(COUNT(x)))`, then `T.DIST.2T(ABS(t), n-1)` | `stats.ttest_1samp(x, mu)` | `t.test(x, mu=)` | Analyze > Compare Means > One-Sample T Test | Stat > Basic Statistics > 1-Sample t |
| Two-sample (Welch) | `T.TEST(a,b,2,3)`; ToolPak "Unequal Variances" | `stats.ttest_ind(a, b, equal_var=False)` | `t.test(a, b)` (Welch by default) | Analyze > Compare Means > Independent-Samples T Test | Stat > Basic Statistics > 2-Sample t |
| Paired | `T.TEST(a,b,2,1)`; ToolPak "Paired Two Sample" | `stats.ttest_rel(a, b)` | `t.test(a, b, paired=TRUE)` | Analyze > Compare Means > Paired-Samples T Test | Stat > Basic Statistics > Paired t |
| Mann-Whitney (non-parametric) | no built-in (rank manually) | `stats.mannwhitneyu(a, b)` | `wilcox.test(a, b)` | Analyze > Nonparametric Tests > Independent Samples | Stat > Nonparametrics > Mann-Whitney |
| Two proportions | manual z formula | `proportions_ztest` (statsmodels) | `prop.test(x, n)` | Crosstabs or Compare Means | Stat > Basic Statistics > 2 Proportions |

SPSS Independent-Samples output prints two rows (equal variances assumed or not); read the "not assumed" row unless Levene's test says variances are similar. Theory in [[089 Hypothesis Testing]] and [[206 Non-Parametric Tests]].

### Example
Using the supplier data of sub-topic 2:

```python
import numpy as np
from scipy import stats
a = np.array([12.1,13.4,11.8,12.9,14.2,13.1,12.6,13.8,12.2,13.5])
b = np.array([13.9,14.8,13.2,15.1,14.4,13.7,15.3,14.1,14.9,13.6])
print(stats.ttest_ind(a, b, equal_var=False))      # t=-4.007, p=0.0008
print(stats.mannwhitneyu(a, b).pvalue)             # 0.0028
before = np.array([52,48,55,60,47,51,58,49]); after = np.array([49,47,50,57,46,48,55,48])
print(stats.ttest_rel(before, after))              # t=5.0, p=0.0016, df=7
```

Reading it: mean A 12.96 vs mean B 14.30 (difference −1.34 days), Welch $t=-4.01$, df 17.8, $p=0.0008$, 95% CI for the difference (−2.04, −0.64) days, Cohen's $d=-1.79$ (very large). The rank test agrees ($p=0.003$). **Plain English:** "Supplier B delivers on average 1.3 days later than A (95% CI 0.6 to 2.0 days), too large to be chance." Paired example: a process change cut mean cycle time by 2.5 minutes in the same 8 workstations ($t=5.0$, df 7, $p=0.0016$).

### In the news
See news box. Benchmarking forecasters against baselines on the same series is a paired comparison, the same logic as the paired t-test above.

### Interview angle
> [!question] How it is asked
> "When do you use a paired t-test and what happens if you wrongly use an independent test?"

> [!tip] Strong answer includes
> - Paired = same units measured twice (before/after), tests the mean difference
> - Wrong independent test throws away the pairing and loses power
> - Welch as the safe default, check normality or n large
> - Report effect size and CI along with p

---
## 5. ANOVA and Post-hoc Tests
> 🟡 Tier 3 · _Key points:_ F = MSB/MSW; one significant F then pairwise (Tukey); check variance equality

### Definition
One-way ANOVA tests whether $k$ group means differ: $F=\dfrac{MS_{between}}{MS_{within}}$ with $df=(k-1,\;N-k)$. A significant F says "at least one mean differs" and does not say which, so follow with **Tukey HSD** (controls the family-wise error).

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| One-way ANOVA | Data Analysis > Anova: Single Factor | `stats.f_oneway(g1, g2, g3)` or `anova_lm(ols(...))` | `summary(aov(y ~ g, d))` | Analyze > Compare Means > One-Way ANOVA | Stat > ANOVA > One-Way |
| Post-hoc | none built in (manual) | `pairwise_tukeyhsd(y, g)` | `TukeyHSD(aov(...))` | One-Way ANOVA > Post Hoc > Tukey | One-Way > Comparisons > Tukey |
| Two-way / factorial | Anova: Two-Factor | `ols('y ~ C(a)*C(b)')` + `anova_lm` | `aov(y ~ a*b)` | Analyze > General Linear Model > Univariate | Stat > ANOVA > General Linear Model |
| Equal-variance check | `F.TEST` (two groups only) | `stats.levene(...)` | `bartlett.test` / `car::leveneTest` | One-Way > Options > Homogeneity of variance | One-Way > Test for equal variances |

### Example
Tensile strength (MPa) from three plants, six samples each: A = 22.1, 23.4, 21.8, 22.9, 23.0, 22.4; B = 24.5, 25.1, 23.9, 24.8, 25.6, 24.2; C = 22.8, 23.9, 23.1, 24.0, 22.7, 23.5.

```python
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from statsmodels.stats.multicomp import pairwise_tukeyhsd
g1=[22.1,23.4,21.8,22.9,23.0,22.4]; g2=[24.5,25.1,23.9,24.8,25.6,24.2]; g3=[22.8,23.9,23.1,24.0,22.7,23.5]
df = pd.DataFrame({'y': g1+g2+g3, 'plant': ['A']*6+['B']*6+['C']*6})
print(anova_lm(smf.ols('y ~ C(plant)', df).fit()).round(4))
print(pairwise_tukeyhsd(df.y, df.plant))
print(stats.levene(g1, g2, g3))
```

**ANOVA table:**

| Source | df | SS | MS | F | p |
|---|---|---|---|---|---|
| Between plants | 2 | 13.401 | 6.701 | **19.10** | 0.0001 |
| Within (error) | 15 | 5.262 | 0.351 | | |

Reading it: $F=6.701/0.351=19.10$ on (2, 15) df, $p<0.001$; Levene $p=0.98$ so equal variances are plausible. Effect size $\eta^2=13.401/18.663=0.72$ (72% of variation is between plants). Tukey: B is higher than A by 2.08 MPa (p = 0.0001) and than C by 1.35 (p = 0.0035); A and C do not differ (p = 0.114). **Plain English:** "Plant B produces stronger material than both others; A and C are statistically indistinguishable."

### In the news
See news box. Comparing many models across many datasets (as the fev-bench evaluation does) faces the same multiple-comparison issue that Tukey addresses for group means.

### Interview angle
> [!question] How it is asked
> "Why not run three separate t-tests instead of ANOVA?"

> [!tip] Strong answer includes
> - Inflated Type I error: three tests at 5% give about 14% family-wise error
> - ANOVA first, then Tukey for which pairs
> - Assumptions: independence, roughly normal residuals, similar variances
> - Effect size ($\eta^2$) and practical meaning

---
## 6. Chi-Square, Correlation and Association
> 🟡 Tier 3 · _Key points:_ Expected counts at least 5; Cramer's V for strength; correlation is not causation

### Definition

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| Chi-square test of independence | `CHISQ.TEST(obs, exp)` (build expected table with row total × column total / N) | `stats.chi2_contingency(table)` | `chisq.test(table)` | Analyze > Descriptive Statistics > Crosstabs > Statistics > Chi-square | Stat > Tables > Chi-Square Test for Association |
| Goodness of fit | `CHISQ.TEST` | `stats.chisquare(obs, exp)` | `chisq.test(obs, p=)` | Analyze > Nonparametric Tests > One Sample (Chi-square) | Stat > Tables > Chi-Square Goodness-of-Fit Test |
| Pearson correlation | `CORREL` | `df.corr()`, `stats.pearsonr` | `cor.test(x, y)` | Analyze > Correlate > Bivariate | Stat > Basic Statistics > Correlation |
| Spearman rank | `CORREL` on ranks | `stats.spearmanr` | `cor.test(method="spearman")` | Correlate > Bivariate > Spearman | Correlation > Spearman |

### Example
Defect class by shift (rows: Day, Night; columns: Minor, Major, Critical): [[30, 45, 25], [20, 55, 45]].

```python
import numpy as np
from scipy import stats
tab = np.array([[30,45,25],[20,55,45]])
chi2, p, dof, exp = stats.chi2_contingency(tab)
print(round(chi2, 2), round(p, 4), dof)             # 6.95 0.0309 2
print(exp.round(1))
print(round(np.sqrt(chi2 / tab.sum() / (min(tab.shape) - 1)), 3))   # Cramer's V 0.178
```

$\chi^2=6.95$, df = 2, $p=0.031$: the defect mix differs by shift. The smallest expected count is 22.7 (all above 5, so the test is valid). Cramer's V = 0.18, a **small-to-moderate** association: statistically significant but not dramatic. **Plain English:** "Night shift produces proportionally more major and critical defects than day shift; the gap is real but modest." See [[209 Generalised Linear Models & Categorical Data Analysis]] for models beyond the 2×3 table.

### In the news
See news box. Categorical association tests remain the default for audit and compliance checks on counts.

### Interview angle
> [!question] How it is asked
> "p is 0.03 on a chi-square test; is the relationship strong?"

> [!tip] Strong answer includes
> - p-value tells existence, Cramer's V or odds ratio tells strength
> - Expected counts at least 5 (else Fisher's exact)
> - Association is not causation; check confounders such as product mix by shift
> - Plain-language summary of which cells drive the result

---
## 7. Regression: Tools and How to Read the Table
> 🟡 Tier 3 · _Key points:_ Coefficient, SE, t, p, CI; F-test; R-squared vs adjusted; condition number

### Definition

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| Simple/multiple regression | Data Analysis > Regression; or `LINEST` | `smf.ols('y ~ x1 + x2', df).fit()` | `lm(y ~ x1 + x2, d)` then `summary()` | Analyze > Regression > Linear | Stat > Regression > Regression > Fit Regression Model |
| Prediction interval | manual with `STEYX` | `m.get_prediction(new).summary_frame()` | `predict(m, new, interval="prediction")` | Linear > Save > Prediction intervals | Fit model > Options > Prediction |
| Multicollinearity | Correlation matrix | `variance_inflation_factor` | `car::vif(m)` | Linear > Statistics > Collinearity diagnostics | Fit Regression Model > Results (VIF) |
| Residual plots | Regression > Residual Plots | `m.resid`, `sm.qqplot` | `plot(m)` | Linear > Plots | Fit model > Graphs > Four in one |

**How to read a regression table (the checklist):**
1. **F-statistic and Prob(F):** is the model as a whole better than the intercept-only model?
2. **R² and adjusted R²:** share of variation explained; adjusted R² penalises useless variables.
3. **Coefficient:** change in $y$ per one-unit change in that $x$, holding the others fixed.
4. **Std err, t = coef / SE, P>|t|:** is the coefficient distinguishable from zero?
5. **95% CI:** plausible range; if it spans zero the variable is not significant at 5%.
6. **Diagnostics:** Durbin-Watson (about 2 means no autocorrelation), Omnibus/JB (residual normality), Condition number (multicollinearity warning).
Theory in [[090 Regression Analysis]] and [[095 Regression Algorithms]].

### Example
60 weeks of data: units sold of a beverage vs price (₹), promotion flag, and temperature (°C). Data generated with a fixed seed so that anyone can reproduce it.

```python
import numpy as np, pandas as pd
import statsmodels.formula.api as smf
rng = np.random.default_rng(11); n = 60
price = rng.uniform(80, 120, n).round(1); promo = rng.integers(0, 2, n); temp = rng.uniform(20, 40, n).round(1)
units = (900 - 4.2*price + 85*promo + 3.0*temp + rng.normal(0, 25, n)).round(0)
df = pd.DataFrame(dict(units=units, price=price, promo=promo, temp=temp))
m = smf.ols('units ~ price + promo + temp', df).fit()
print(m.summary())
```

Key lines of the output:

| Term | Coef | Std err | t | P>\|t\| | 95% CI |
|---|---|---|---|---|---|
| Intercept | 877.71 | 26.75 | 32.81 | 0.000 | 824.1 to 931.3 |
| price | −4.257 | 0.232 | −18.35 | 0.000 | −4.72 to −3.79 |
| promo | 90.93 | 5.504 | 16.52 | 0.000 | 79.9 to 102.0 |
| temp | 3.919 | 0.457 | 8.57 | 0.000 | 3.00 to 4.84 |

Model: $R^2=0.925$, adjusted $R^2=0.921$, $F(3,56)=231.2$, $p=1.7\times10^{-31}$, Durbin-Watson 2.12, Jarque-Bera $p=0.947$. **Plain English:** "Each ₹1 price rise cuts weekly sales by about 4.3 units (95% CI 3.8 to 4.7); a promotion adds about 91 units; each extra degree adds about 4 units; together these explain 92% of the weekly variation." The warning "condition number 1.01e+03" is due to unscaled price and temperature levels, not collinearity: VIFs are all about 1.0.

### In the news
See news box. Regression-style models with calendar, price and promotion covariates are exactly the structure that newer forecasting models accept as covariates.

### Interview angle
> [!question] How it is asked
> "Here is a regression output. Tell me what it says."

> [!tip] Strong answer includes
> - Start with overall F and R-squared, then coefficients with units
> - Interpret one coefficient in a sentence with "holding other variables constant"
> - Check p, CI and practical size, not only stars
> - Diagnostics: residual plot, VIF, autocorrelation
> - Caution: association, extrapolation limits (do not predict price outside the range 80 to 120)

---
## 8. Regression Diagnostics and Prediction
> 🟡 Tier 3 · _Key points:_ Residual checks, VIF, Breusch-Pagan, prediction versus confidence interval

### Definition
After fitting, verify the assumptions (LINE: Linearity, Independence, Normal residuals, Equal variance).

| Check | Python | Excel | Rule of thumb |
|---|---|---|---|
| Residual vs fitted plot | `plt.scatter(m.fittedvalues, m.resid)` | Regression > Residual Plots | Random cloud, no funnel or curve |
| Normality of residuals | `stats.shapiro(m.resid)`, Q-Q plot | histogram of residuals | $p>0.05$ and straight Q-Q line |
| Heteroscedasticity | `het_breuschpagan(m.resid, m.model.exog)` | residual-vs-fitted funnel | $p>0.05$ |
| Autocorrelation | `durbin_watson(m.resid)` | residual lag-1 correlation | about 2 (below 1.5 or above 2.5 is a concern) |
| Multicollinearity | `variance_inflation_factor` | `CORREL` matrix | VIF below 5 (some use 10) |
| Influential points | `m.get_influence().cooks_distance` | manual | Cook's $D>4/n$ worth a look |

**Confidence interval vs prediction interval:** the CI is for the **mean** response at given $x$; the prediction interval is for a **single new** observation and is always wider.

### Example
Continuing the sales model: Breusch-Pagan $p=0.43$ (no evidence of unequal variance), Shapiro-Wilk $p=0.54$, Durbin-Watson 2.12, VIFs 1.00, 1.01, 1.00. For a week with price ₹100, promotion on and 30 °C:

```python
# continues from the fitted model m above
new = pd.DataFrame(dict(price=[100], promo=[1], temp=[30]))
print(m.get_prediction(new).summary_frame(alpha=0.05).round(1))
```

Output: predicted mean **660.5** units; 95% CI for the mean 652.2 to 668.8; 95% **prediction** interval 617.3 to 703.7. For stock planning, use the prediction interval (or its upper quantile) because a single week's demand varies far more than the average does. Safety stock from that spread: [[003 Inventory Management]].

### In the news
See news box. Prediction intervals are the classical cousin of the quantile forecasts that foundation models output (for example the quantile head in TimesFM 2.5).

### Interview angle
> [!question] How it is asked
> "What is the difference between a confidence interval and a prediction interval in regression?"

> [!tip] Strong answer includes
> - CI for the mean at x; PI for one new observation; PI wider
> - Which one matters for planning (PI)
> - The four assumptions and one diagnostic for each
> - What to do on failure: transform, add variables, robust SEs, different model

---
## 9. Control Charts and Process Capability
> 🟡 Tier 3 · _Key points:_ X-bar and R limits with A2, D3, D4; sigma-hat = Rbar/d2; Cp versus Cpk

### Definition
Subgroup data (size $n$) gives centre lines $\bar{\bar X}$ and $\bar R$; limits are $\bar{\bar X}\pm A_2\bar R$ and $D_3\bar R,\;D_4\bar R$. For $n=5$: $A_2=0.577$, $D_3=0$, $D_4=2.114$, $d_2=2.326$. Individuals chart: $\bar X\pm2.66\,\overline{MR}$. Capability: $C_p=\dfrac{USL-LSL}{6\hat\sigma}$, $C_{pk}=\min\!\left(\dfrac{USL-\bar X}{3\hat\sigma},\dfrac{\bar X-LSL}{3\hat\sigma}\right)$, with $\hat\sigma=\bar R/d_2$ (within-subgroup).

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| X-bar/R | build with `AVERAGE`, `MAX-MIN`, lines | compute by hand (a few lines of NumPy) | `qcc::qcc(data, type="xbar")` | Analyze > Quality Control > Control Charts | Stat > Control Charts > Variables Charts for Subgroups > Xbar-R |
| Individuals (I-MR) | formulas | compute by hand | `qcc(type="xbar.one")` | Control Charts > Individuals, Moving Range | Variables Charts for Individuals > I-MR |
| Attribute (p, np, c, u) | formulas | by hand | `qcc(type="p")` | Control Charts > p, np, c, u | Stat > Control Charts > Attributes Charts |
| Capability | formulas | by hand | `qcc::process.capability` | not standard | Stat > Quality Tools > Capability Analysis > Normal |
| Gage R&R | ToolPak ANOVA two-factor | statsmodels two-way ANOVA | `SixSigma::ss.rr` | not standard | Stat > Quality Tools > Gage Study > Gage R&R Study (Crossed) |

Theory in [[091 Statistical Quality Control (SQC)]] and measurement systems in [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]].

### Example
Twenty subgroups of 5 measurements (target 50, specification 44 to 56; simulated with a fixed seed).

```python
import numpy as np
rng = np.random.default_rng(5)
data = rng.normal(50, 2, (20, 5)).round(2)
xb, R = data.mean(1), data.max(1) - data.min(1)
A2, D3, D4, d2 = 0.577, 0, 2.114, 2.326
xbb, Rb = xb.mean(), R.mean()
print(round(xbb, 3), round(Rb, 3))                       # 49.552 4.10
print("Xbar UCL/LCL", round(xbb + A2*Rb, 3), round(xbb - A2*Rb, 3))   # 51.919 47.186
print("R UCL/LCL", round(D4*Rb, 3), D3*Rb)               # 8.671 0.0
sig = Rb / d2; USL, LSL = 56, 44
print("Cp", round((USL-LSL)/(6*sig), 2), "Cpk", round(min(USL-xbb, xbb-LSL)/(3*sig), 2))   # 1.13 1.05
```

$\bar{\bar X}=49.55$, $\bar R=4.10$; X-bar limits 47.19 to 51.92; R-chart UCL 8.67; $\hat\sigma=4.101/2.326=1.76$; $C_p=12/(6\times1.763)=1.13$ and $C_{pk}=1.05$. No subgroup falls outside the limits, so the process is stable; $C_{pk}$ just above 1 means it is capable but with little margin (many customers require at least 1.33). **Plain English:** "The process is in statistical control and barely capable; about 1 part in 1,000 would fall outside specification if the data are normal."

### In the news
See news box. Monitoring a model's forecast error with a control chart is a practical use of the same limits.

### Interview angle
> [!question] How it is asked
> "What is the difference between Cp and Cpk, and what does a Cpk of 1.05 tell you?"

> [!tip] Strong answer includes
> - Cp = spread vs tolerance; Cpk also penalises off-centre
> - Control (stable) comes before capability (meets spec)
> - Constants A2, D4 depend on subgroup size
> - Cpk 1.05 means marginal; target 1.33 or higher for most customers

---
## 10. Design of Experiments in Software
> 🟡 Tier 3 · _Key points:_ Code factors as -1 and +1; effect = 2 x coefficient; read interaction; Minitab and R automate the design

### Definition
A **full factorial** tests all combinations of factor levels, estimating main effects and interactions with fewer runs than one-factor-at-a-time. Code each factor as −1 (low) and +1 (high); the **effect** is the difference between the mean response at high and at low, which equals **twice** the regression coefficient in the coded model. Theory in [[213 Design of Experiments - Factorial, Fractional & Taguchi]] and [[092 Sampling & Experimental Design]].

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| Create design | build table by hand | `itertools.product`, `pyDOE2` | `FrF2`, `DoE.base` | Data > Orthogonal Design > Generate | Stat > DOE > Factorial > Create Factorial Design |
| Analyse | Regression ToolPak on coded columns | `ols('y ~ A*B')` + `anova_lm` | `lm(y ~ A*B)` | General Linear Model > Univariate | Stat > DOE > Factorial > Analyze Factorial Design |
| Plots | chart means by hand | `sm.graphics.interaction_plot` | `interaction.plot` | Profile plots | Factorial Plots (main effects, interaction) and Pareto of effects |

### Example
A 2² design with two replicates: A = oven temperature (−1 = 160, +1 = 180 °C), B = cure time (−1 = 20, +1 = 30 min); response y = strength.

| A | B | Replicates | Mean |
|---|---|---|---|
| −1 | −1 | 28, 30 | 29 |
| +1 | −1 | 36, 38 | 37 |
| −1 | +1 | 18, 20 | 19 |
| +1 | +1 | 31, 33 | 32 |

```python
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
rows = []
for A, B, ys in [(-1,-1,[28,30]), (1,-1,[36,38]), (-1,1,[18,20]), (1,1,[31,33])]:
    rows += [dict(A=A, B=B, y=y) for y in ys]
m = smf.ols('y ~ A*B', pd.DataFrame(rows)).fit()
print(m.params.round(2).to_dict())          # Intercept 29.25, A 5.25, B -3.75, A:B 1.25
print(anova_lm(m, typ=2).round(3))
```

Effects: A = 2 × 5.25 = **+10.5**, B = 2 × (−3.75) = **−7.5**, AB = 2 × 1.25 = **+2.5**. ANOVA: A $F=110.25$, $p<0.001$; B $F=56.25$, $p=0.002$; AB $F=6.25$, $p=0.067$ (error df 4, MSE 2.0). **Plain English:** "Higher temperature raises strength by about 10.5 units; a longer cure time lowers it by about 7.5; there is a hint of interaction, not conclusive with so few runs." Check by hand: mean at A+ = (37+32)/2 = 34.5, at A− = (29+19)/2 = 24, difference 10.5.

### In the news
See news box. Automated experimentation platforms and spreadsheet-based design tools make factorial thinking accessible to analysts.

### Interview angle
> [!question] How it is asked
> "Why use a factorial experiment rather than changing one factor at a time?"

> [!tip] Strong answer includes
> - Efficiency: all factors estimated from the same runs
> - Interactions are visible only when factors vary together
> - Replication gives error estimate and p-values
> - Coded units and effect = 2 × coefficient

---
## 11. Time Series and Forecasting Tools
> 🟡 Tier 3 · _Key points:_ Holt-Winters and SARIMA; hold-out MAPE and WAPE; Excel FORECAST.ETS

### Definition

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| Linear trend | `FORECAST.LINEAR`, Trendline | `LinearRegression`, `ols` | `lm`, `forecast::tslm` | Analyze > Regression > Curve Estimation | Stat > Time Series > Trend Analysis |
| Exponential smoothing with trend and seasonality | `FORECAST.ETS` (AAA ETS), Data > Forecast Sheet | `ExponentialSmoothing(...).fit()` | `forecast::ets()` | Analyze > Forecasting > Create Traditional Models (Exponential Smoothing) | Stat > Time Series > Winters' Method |
| ARIMA/SARIMA | none | `SARIMAX(order=, seasonal_order=)` | `forecast::auto.arima` | Time Series Modeler (ARIMA / Expert Modeler) | Stat > Time Series > ARIMA |
| Decomposition | manual | `seasonal_decompose` | `stl()` | Analyze > Forecasting > Seasonal Decomposition | Stat > Time Series > Decomposition |
| Accuracy | `ABS`, `SUMPRODUCT` | manual | `accuracy()` | model fit table | model summary |

Excel's `FORECAST.ETS` needs a **regular, evenly spaced timeline**; use `FORECAST.ETS.CONFINT` for a confidence band and `FORECAST.ETS.SEASONALITY` to see the detected season length. Models in theory: [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]], [[066 Demand Forecasting & Time Series]], [[004 Demand Forecasting & Planning]]; ML approaches in [[218 Forecasting with ML & Foundation Models]].

### Example
48 months of simulated demand (trend 0.8 per month, 12-month seasonality, noise SD 2; seed 5 after the control-chart draws). Hold out the last 6 months.

```python
import numpy as np, pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
rng = np.random.default_rng(5)
_ = rng.normal(50, 2, (20, 5))                      # same stream as the control-chart example
t = np.arange(48); season = np.tile([0,-6,-3,2,5,9,12,8,3,-1,-4,-8], 4)
y = (100 + 0.8*t + season + rng.normal(0, 2, 48)).round(1)
ser = pd.Series(y, index=pd.date_range('2022-01-01', periods=48, freq='MS'))
tr, te = ser[:42], ser[42:]
fit = ExponentialSmoothing(tr, trend='add', seasonal='add', seasonal_periods=12).fit()
f = fit.forecast(6)
print("WAPE %", round(float(np.abs(te - f).sum() / te.sum() * 100), 2))   # about 1.7
```

Result: the Holt-Winters model forecasts the held-out six months with **MAPE 1.68% and WAPE 1.68%** (these coincide here because the series is far from zero and errors are similar in size); SARIMA(1,1,1)(0,1,1)₁₂ on the full series forecasts the next three months as 138.8, 133.0, 138.0, close to a full-sample Holt-Winters fit (138.4, 132.7, 137.6 for the same three months). With only four years of data statsmodels warns that it had too few observations to estimate seasonal starting values; in practice use at least 3 to 4 full seasons, and compare against a seasonal-naive baseline. **Plain English:** "Holt-Winters tracks the last half-year to within about 1.7% of volume."

### In the news
See news box. Foundation models such as Chronos-2 and TimesFM are called with the same "history in, quantiles out" pattern as the statsmodels code above.

### Interview angle
> [!question] How it is asked
> "How would you build and validate a quick forecast in Excel or Python?"

> [!tip] Strong answer includes
> - Plot, decompose, choose model family (ETS or ARIMA), fit
> - Hold-out or rolling-origin validation, WAPE and bias, compared with seasonal naive
> - Warning on too-short history
> - Intervals, not only point forecasts

---
## 12. Power, Sample Size and A/B Test Calculations
> 🟡 Tier 3 · _Key points:_ Plan n before data; effect size; solve_power; two-proportion z

### Definition
Power analysis links four quantities: effect size, $\alpha$, power ($1-\beta$) and sample size; fix three and solve for the fourth.

| Task | Excel | Python | R | SPSS | Minitab |
|---|---|---|---|---|---|
| n for two-sample t | `NORM.S.INV`-based formula | `TTestIndPower().solve_power(...)` | `power.t.test(delta=, sd=, power=)` | Analyze > Power Analysis > Means > Independent-Samples T Test | Stat > Power and Sample Size > 2-Sample t |
| Two proportions | formula | `proportions_ztest`, `NormalIndPower` | `prop.test`, `power.prop.test` | Power Analysis > Proportions | Stat > Power and Sample Size > 2 Proportions |

For two means: $n\approx\dfrac{2(z_{1-\alpha/2}+z_{1-\beta})^2}{d^2}$ per group, where $d$ is Cohen's effect size. See [[089 Hypothesis Testing]] and [[214 Causal Inference & Experimentation Beyond A-B Tests]].

### Example
To detect a medium effect $d=0.5$ with $\alpha=0.05$ (two-sided) and 80% power: formula gives $2(1.96+0.8416)^2/0.25=62.8$, so **63 per group**; exact t-based calculation gives 63.77, round up to **64 per group**.

```python
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.proportion import proportions_ztest
print(TTestIndPower().solve_power(effect_size=0.5, alpha=0.05, power=0.8))   # 63.77
print(proportions_ztest([200, 240], [5000, 5000]))                           # z=-1.95, p=0.051
```

A/B check from the hypothesis-testing note: 4.0% (200 of 5,000) versus 4.8% (240 of 5,000) gives $z=-1.95$, $p=0.051$: just short of the 5% threshold, so the experiment is underpowered for a 0.8-point lift.

### In the news
See news box. Benchmarks like fev-bench report bootstrapped confidence intervals for win rates, the same discipline of reporting uncertainty rather than a bare ranking.

### Interview angle
> [!question] How it is asked
> "How many users do you need for this A/B test?"

> [!tip] Strong answer includes
> - Baseline rate, minimum detectable effect, alpha, power
> - Formula or tool, then rounding up
> - Trade-off: smaller effect needs far more users (n scales with 1/d²)
> - Pre-register the stopping rule to avoid peeking

---
## 13. Reporting Results in Plain English
> 🟡 Tier 3 · _Key points:_ Answer first, then effect size, interval, evidence, caveat

### Definition
Managers need a decision, not a printout. A reusable four-part sentence:

1. **Answer** ("Supplier B is slower").
2. **Size with uncertainty** ("by 1.3 days, 95% CI 0.6 to 2.0").
3. **Evidence** ("p < 0.001 on 10 deliveries each").
4. **Caveat and next step** ("small sample; confirm over next quarter").

| Output | Say this |
|---|---|
| $p=0.0008$ | "If the suppliers were really equal, a gap this large would appear in under 1 in 1,000 samples" |
| 95% CI (−2.04, −0.64) | "We are 95% confident, by the method used, that the true gap lies between 0.6 and 2.0 days" |
| $R^2=0.92$ | "The model explains 92% of week-to-week variation in sales" |
| Coefficient −4.26 | "Each ₹1 price rise is associated with about 4 fewer units, other factors constant" |
| $C_{pk}=1.05$ | "Capable, but with little safety margin" |
| ANOVA $F$ significant | "At least one plant differs; Tukey shows B is the different one" |

Avoid: "proves", "the probability the hypothesis is true", "significant" without size, and unlabelled axes. Put the formula in an appendix.

### Example
Raw: "t(17.8) = −4.01, p = 0.0008, d = −1.79." Manager version: "Supplier B's deliveries average 14.3 days against 13.0 for Supplier A, a gap of about 1.3 days that is very unlikely to be chance (10 deliveries each). Moving the volume to A would cut average lead time by around 9%." (1.34/14.30 = 9.4%, an arithmetic illustration only.)

### In the news
See news box. As model-based tools spread, the analyst's value moves from running the test to explaining it.

### Interview angle
> [!question] How it is asked
> "Explain this regression to a non-technical manager in one minute."

> [!tip] Strong answer includes
> - Lead with the decision relevance, not the method
> - Use units and ranges; one number plus one uncertainty
> - One caveat that matters, not five
> - Offer the detail on request

---
## 14. ⭐ Advanced: Reproducible Analysis and Common Tool Pitfalls
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Professional practice means any colleague can re-run your analysis. Tool-specific traps to know:

| Tool | Pitfall |
|---|---|
| Excel | `T.TEST` type argument (1, 2, 3) silently changes the test; `STDEV.P` vs `STDEV.S`; ToolPak output is static; `FORECAST.ETS` fails on irregular dates; `QUARTILE.INC` vs `.EXC` give different quartiles; rounding in displayed cells hides precision |
| Python | `ttest_ind` defaults to **equal variances** (`equal_var=True`); `pandas.std` uses ddof=1 but `numpy.std` uses ddof=0; `skew` and `kurt` conventions differ from Excel's; always set `rng` seeds |
| R | `t.test` is Welch by default (opposite to Python's default); factors versus numerics change what `aov` does |
| SPSS | Independent t-test prints two rows; read the right one; pasted syntax saves the analysis |
| Minitab | Dialog defaults (e.g., Welch vs pooled, Tukey vs Fisher) vary by version; save the project (.mpx) and the session window output |

Reproducibility checklist: raw data file untouched, a script or documented steps, versions of libraries recorded, random seeds fixed, outputs saved with the code, and a one-line data dictionary. A notebook (Jupyter or Quarto) puts code, tables and narrative together; see [[186 Python Data Cleaning & EDA Playbook]] and [[185 Python Interview Problem Bank]].

### Example
The same two groups can yield different p-values depending on the variant: Excel `=T.TEST(A,B,2,2)` (pooled) vs `=T.TEST(A,B,2,3)` (Welch), and Python `ttest_ind(a, b)` (pooled by default) vs `equal_var=False`. With the supplier data the two p-values are 0.000826 and 0.000841, nearly identical because the group sizes are equal and the sample SDs close (0.78 and 0.71); with unequal sizes and SDs the gap can change a decision. A one-line habit: write down which variant you ran.

```python
from scipy import stats
import numpy as np
a = np.array([12.1,13.4,11.8,12.9,14.2,13.1,12.6,13.8,12.2,13.5]); b = np.array([13.9,14.8,13.2,15.1,14.4,13.7,15.3,14.1,14.9,13.6])
print(stats.ttest_ind(a, b).pvalue, stats.ttest_ind(a, b, equal_var=False).pvalue)
```

### In the news
See news box. Licence terms matter too: the TimesFM 3.0 downloadable weights are non-commercial while Chronos-2 is Apache 2.0, so a production decision depends on the licence as well as accuracy.

### Interview angle
> [!question] How it is asked
> "Your colleague gets a different p-value from yours on the same data. How do you debug?"

> [!tip] Strong answer includes
> - Compare test variants (pooled vs Welch, one- vs two-tailed, ddof)
> - Compare data cleaning steps and exclusions
> - Re-run from raw data with a script and a seed
> - Document the variant in the report
> - Link to [[215 Statistics Interview Question Bank & Numericals]] for practice
