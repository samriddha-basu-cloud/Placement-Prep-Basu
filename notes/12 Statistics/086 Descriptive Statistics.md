---
tags: [statistics, tier1]
area: Statistics
topic: "Descriptive Statistics"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Descriptive Statistics

[[_Index - Statistics|Statistics]] · [[087 Probability Fundamentals]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Measures of Central Tendency]]
2. [[#2. Measures of Spread / Dispersion]]
3. [[#3. Skewness]]
4. [[#4. Kurtosis]]
5. [[#5. Percentiles & Quartiles]]
6. [[#6. Box Plot Interpretation]]
7. [[#7. Frequency Distribution]]
8. [[#8. Covariance & Correlation]]
9. [[#9. Scatter Plot & Correlation]]
10. [[#10. Z-Score (Standardization)]]
11. [[#11. ⭐ Advanced: Robust Statistics (MAD, Trimmed Mean) for Messy Operations Data]]
12. [[#12. ⭐ Advanced: Simpson's Paradox and Aggregation Traps]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India re-bases its inflation and GDP statistics
> **New CPI series (launched 12 Feb 2026, base year 2024 replacing 2012).** Built on the Household Consumption Expenditure Survey 2023-24 and the COICOP 2018 classification; the weight of food and beverages falls from **45.86% to 36.75%**, housing/utilities/fuel rises to **17.67%**. The first reading, for January 2026, was **2.75%** (urban plus rural), against **1.3%** for December 2025 on the old series. Same economy, different weights, different number. ([Upstox explainer of the MoSPI release](https://upstox.com/learning-center/personal-finance/what-changed-in-indias-new-cpi-series-and-how-it-impacts-the-economy-and-inflation/article-1518/))
>
> **New GDP series (base year 2022-23, released 27 Feb 2026).** Replaces the 2011-12 base. Reported: FY2025-26 second advance estimate real growth **7.6%**; FY2024-25 revised real growth **7.1%** (nominal 9.7%); new data sources include GST data, e-Vahan and Ministry of Corporate Affairs filings, with double deflation in manufacturing and agriculture. ([PIB release as read via fetch](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2233518&reg=48&lang=2))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Measures of Central Tendency
> 🔴 Tier 1 · _Tracker hint:_ Mean (arithmetic/geometric/harmonic); Median (middle value); Mode (most frequent); when to use each

### Definition
| Measure | Formula | Use when |
|---|---|---|
| Arithmetic mean | $\bar{x}=\frac{1}{n}\sum x_i$ | Symmetric data, additive quantities |
| Geometric mean | $GM=(\prod x_i)^{1/n}$ | Growth rates, ratios, indices |
| Harmonic mean | $HM=\frac{n}{\sum 1/x_i}$ | Rates over equal distance/cost (speeds, price per unit) |
| Median | middle value of sorted data | Skewed data, outliers (income, lead time) |
| Mode | most frequent value | Categorical data, most common size/SKU |

Mean is pulled by outliers; median is **robust**. For positive data, $HM \le GM \le AM$.

### Example
Lead times (days): 4, 5, 5, 6, 7, 8, 20. Mean = 55/7 = **7.86**, median = **6**, mode = **5**. The one 20-day delay drags the mean above 6 of 7 observations; quote the median for the typical case and report the tail separately.
Growth factors 1.10, 1.20, 0.90: GM = (1.188)^(1/3) = **1.059**, i.e. 5.9% a year, not the arithmetic 6.7%. Truck going 60 km/h out and 40 km/h back: HM = 2/(1/60+1/40) = **48 km/h**.

### In the news
See news box. The CPI is a *weighted* mean of item price changes, so changing the weights changes the answer.

### Interview angle
> [!question] How it is asked
> "Average salary in a company is ₹12 L but most people earn less. Why? Which average would you report?"

> [!tip] Strong answer includes
> - Outlier sensitivity of the mean; use median for skew
> - Geometric mean for growth (CAGR), harmonic for rates
> - State which measure you report and why
> - Show both when they differ a lot

---

## 2. Measures of Spread / Dispersion
> 🔴 Tier 1 · _Tracker hint:_ Range, IQR, Variance (σ²), Standard Deviation (σ); Coefficient of Variation = σ/μ

### Definition
- **Range** = max − min (sensitive to outliers).
- **IQR** = Q3 − Q1 (middle 50%).
- **Population variance** $\sigma^2=\frac{\sum(x_i-\mu)^2}{N}$; **sample variance** $s^2=\frac{\sum(x_i-\bar{x})^2}{n-1}$ (the $n-1$ makes it unbiased).
- **Standard deviation** = √variance, same units as data.
- **Coefficient of variation** $CV=\sigma/\mu$ (unitless) compares variability across different scales.

In supply chain, $\sigma$ of demand during lead time drives safety stock: $SS = Z \times \sigma_{LT}$.

### Example
Data 2, 4, 4, 4, 5, 5, 7, 9: mean = 40/8 = 5. Squared deviations: 9+1+1+1+0+0+4+16 = 32. Population variance = 32/8 = **4**, σ = **2**; sample variance = 32/7 = **4.57**, s = 2.14. CV = 2/5 = **0.40**. A product with mean demand 1,000 and σ=100 (CV 0.10) is far more predictable than one with mean 50 and σ=25 (CV 0.50) even though its σ is larger.

### In the news
See news box. Revisions of base year change not only the level but the volatility of series; analysts compare spread before and after.

### Interview angle
> [!question] How it is asked
> "Two suppliers both average 10 days lead time. How do you choose?"

> [!tip] Strong answer includes
> - Mean is not enough; compare σ or CV
> - Link spread to safety stock and cost
> - Sample vs population ($n-1$)
> - Use CV to compare unlike scales

---

## 3. Skewness
> 🔴 Tier 1 · _Tracker hint:_ Positive skew (tail right, mean > median); Negative skew (tail left); Symmetric (normal)

### Definition
**Skewness** measures asymmetry:
$$\text{Skew}=\frac{1}{n}\sum\left(\frac{x_i-\bar{x}}{s}\right)^3$$
Pearson's second coefficient: $3(\text{mean}-\text{median})/s$.

| Shape | Tail | Order |
|---|---|---|
| Positive (right) skew | long right tail | mean > median > mode |
| Symmetric | none | mean = median = mode |
| Negative (left) skew | long left tail | mean < median < mode |

Rule of thumb: |skew| < 0.5 roughly symmetric; > 1 strongly skewed. Lead times, incomes, order values, delivery delays are usually right-skewed.

### Example
Lead times 4, 5, 5, 6, 7, 8, 20: mean 7.86 > median 6; s = 5.52; Pearson skew = 3(7.86−6)/5.52 = **1.01**, strongly right-skewed. Planning to the mean under-protects against the long tail; plan on a high percentile.

### In the news
See news box. Income and price distributions are right-skewed, which is why median and weighted measures matter in official statistics.

### Interview angle
> [!question] How it is asked
> "Mean delivery time is 5 days but customers complain. What might be happening?"

> [!tip] Strong answer includes
> - Right skew: long tail of late deliveries
> - Median, 90th/95th percentile, and on-time % instead of mean
> - Segment the tail by lane/supplier
> - Plan safety stock for the tail

---

## 4. Kurtosis
> 🔴 Tier 1 · _Tracker hint:_ Leptokurtic (fat tails, kurtosis>3); Platykurtic (thin tails); Mesokurtic (normal, =3)

### Definition
**Kurtosis** measures tail weight (and peakedness):
$$\text{Kurt}=\frac{1}{n}\sum\left(\frac{x_i-\bar{x}}{s}\right)^4$$
Normal = 3. **Excess kurtosis** = Kurt − 3 (many software packages report this, so check which one).

| Type | Kurtosis | Meaning |
|---|---|---|
| Leptokurtic | > 3 | fat tails, more extreme events |
| Mesokurtic | = 3 | normal-like |
| Platykurtic | < 3 | thin tails, fewer extremes |

Fat tails mean that "3-sigma events" happen more often than the normal predicts; risk models assuming normality understate risk.

### Example
Daily demand shocks for a commodity: normal predicts |z|>3 about 0.27% of days (about 1 day in 370). A leptokurtic series might show it on 1–2% of days, so safety stock sized by a normal Z-value would be breached several times more often than planned.

### In the news
See news box. Supply shocks (such as 2024 shipping and 2025 chip disruptions) are fat-tail events that normal-based plans miss.

### Interview angle
> [!question] How it is asked
> "What does high kurtosis tell you and why does it matter for risk?"

> [!tip] Strong answer includes
> - Kurtosis = tail heaviness; 3 for normal; excess = −3
> - Consequence: more extreme outcomes than the normal predicts
> - Business example (demand spikes, returns, losses)
> - Response: percentile-based or scenario-based buffers

---

## 5. Percentiles & Quartiles
> 🔴 Tier 1 · _Tracker hint:_ Q1=25th, Q2=50th(median), Q3=75th; IQR = Q3-Q1; outlier: < Q1-1.5×IQR or > Q3+1.5×IQR

### Definition
The **p-th percentile** is the value below which p% of observations fall. Quartiles split data into four parts: Q1 (25th), Q2 (median), Q3 (75th). $IQR=Q_3-Q_1$.

**Tukey fences:** lower = $Q_1-1.5\,IQR$, upper = $Q_3+1.5\,IQR$; points outside are flagged as outliers (3×IQR for "extreme"). Software uses different interpolation rules, so Q1/Q3 can differ slightly between Excel (`QUARTILE.INC` / `QUARTILE.EXC`), Python and textbook "median of halves" methods.

### Example
Order values (₹ thousand): 12, 15, 16, 18, 20, 21, 23, 25, 28, 60. Median = (20+21)/2 = **20.5**. Lower half 12–20: Q1 = **16**; upper half 21–60: Q3 = **25**. IQR = 9. Upper fence = 25 + 13.5 = **38.5**; lower = 16 − 13.5 = 2.5. So **60 is an outlier**; investigate whether it is an error or a bulk order.

### In the news
See news box. Official releases increasingly report medians and percentiles in addition to averages for this reason.

### Interview angle
> [!question] How it is asked
> "How would you detect outliers in a dataset of delivery times?"

> [!tip] Strong answer includes
> - IQR/Tukey fences (robust) vs z-score (assumes normal)
> - Decide: error, genuine rare event, or different segment
> - Do not delete automatically; document treatment
> - Percentiles (P90, P95) for service-level reporting

---

## 6. Box Plot Interpretation
> 🔴 Tier 1 · _Tracker hint:_ Whiskers = 1.5×IQR; median line; mean vs median position shows skew

### Definition
A **box plot** (box-and-whisker) shows five numbers: minimum (non-outlier), Q1, median, Q3, maximum (non-outlier). The box spans Q1–Q3 (IQR), the line is the median, whiskers extend to the most extreme points within 1.5×IQR of the box, and dots beyond are outliers.

Reading it:
- **Median not centred in the box** → skew (closer to Q1 with long upper whisker = right skew).
- **Box height** = spread; **side-by-side boxes** compare groups (plants, suppliers, shifts).
- If the mean marker sits above the median → right skew.
- Compare boxes' overlap to judge if groups differ, before a formal test.

### Example
Delivery times by carrier: Carrier A box 2–4 days with median 3, no outliers; Carrier B box 2–7, median 3, two outliers at 15 days. Same median, but B is far less reliable; choose A for time-critical lanes.

### In the news
See news box. Distribution plots (not only averages) are now common in published economic comparisons.

### Interview angle
> [!question] How it is asked
> "What can you tell from this box plot?" (a chart is shown)

> [!tip] Strong answer includes
> - Read median, IQR, whiskers, outliers in that order
> - Comment on skew and comparison between groups
> - Translate into a business message
> - Mention next step (test, root cause on outliers)

---

## 7. Frequency Distribution
> 🔴 Tier 1 · _Tracker hint:_ Class intervals, frequency table, histogram, ogive (cumulative frequency curve)

### Definition
Grouping data into **class intervals** with **frequency** (count), **relative frequency** (count/total) and **cumulative frequency**. Number of classes roughly $k\approx1+3.322\log_{10}n$ (Sturges) with equal widths. A **histogram** plots frequency as adjacent bars (area proportional to frequency); an **ogive** plots cumulative frequency against upper class limits and lets you read the median and percentiles graphically.

Grouped median: $\text{Median}=L+\frac{n/2-F}{f}\times w$ ($L$ lower limit of median class, $F$ cumulative before it, $f$ its frequency, $w$ width).

### Example
40 deliveries, delay in days: 0–2: 8; 2–4: 14; 4–6: 10; 6–8: 6; 8–10: 2. Cumulative: 8, 22, 32, 38, 40. Median class is 2–4 (cumulative passes 20): median = 2 + (20−8)/14 × 2 = **3.71 days**. Share delayed under 6 days = 32/40 = **80%**.

### In the news
See news box. Survey data, such as the household expenditure survey behind the new CPI, is first summarised into frequency tables before weights are derived.

### Interview angle
> [!question] How it is asked
> "Here are 500 transaction values. How would you summarise them for a manager?"

> [!tip] Strong answer includes
> - Histogram with sensible bins, plus median and spread
> - Cumulative view for service-level questions ("% within 3 days")
> - Comment on shape (skew, multimodality)
> - Beware of bin width changing the story

---

## 8. Covariance & Correlation
> 🔴 Tier 1 · _Tracker hint:_ Cov(X,Y) = Σ(xi-x̄)(yi-ȳ)/n; Pearson r = Cov/σxσy; r ∈ [-1,1]

### Definition
**Covariance** measures how two variables move together: $\text{Cov}(X,Y)=\frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{n}$ (use $n-1$ for a sample). Its size depends on units. **Pearson correlation** standardises it:
$$r=\frac{\text{Cov}(X,Y)}{\sigma_X\sigma_Y}\in[-1,1]$$
$r^2$ is the share of variance in one linearly explained by the other. Pearson captures **linear** association only and is sensitive to outliers; use Spearman rank correlation for monotonic, non-linear relations.

### Example
Ad spend x = 1, 2, 3, 4, 5 (₹ lakh); sales y = 2, 4, 5, 4, 5 (units '000). x̄ = 3, ȳ = 4. Products of deviations: (−2)(−2)=4, (−1)(0)=0, 0×1=0, 1×0=0, 2×1=2; sum = 6. Cov = 6/5 = **1.2**. σx = √2 = 1.414, σy = √1.2 = 1.095. r = 1.2/(1.414×1.095) = **0.775**; r² = 0.60.

### In the news
See news box. Official series built from overlapping data (for example price indices used to deflate GDP) are not independent, so be careful about counting them as separate evidence.

### Interview angle
> [!question] How it is asked
> "What is the difference between covariance and correlation?"

> [!tip] Strong answer includes
> - Cov has units; r is standardised in [−1, 1]
> - r measures linear association only
> - r² interpretation
> - Mention of diversification (portfolio / demand pooling) as a use

---

## 9. Scatter Plot & Correlation
> 🔴 Tier 1 · _Tracker hint:_ Strong/weak/no correlation; positive/negative; correlation ≠ causation

### Definition
A **scatter plot** shows paired observations; direction (positive/negative), form (linear/curved), strength (tight/loose) and outliers. Rough guide for |r|: 0.7–1 strong, 0.3–0.7 moderate, below 0.3 weak. Always **plot before computing r**: Anscombe's quartet gives four datasets with the same r (≈0.816) and very different shapes.

**Correlation ≠ causation:** reasons for association without causation are confounding (a third variable), reverse causality, selection and coincidence. Demonstrating causation needs experiments (A/B tests) or careful design.

### Example
Ice-cream sales and drowning incidents correlate positively; the confounder is temperature (summer). In operations: forecast error and promotion frequency correlate (r = 0.6) but both are driven by category; cutting promotions alone may not fix accuracy.

### In the news
See news box. When two official series disagree (old vs new CPI), one should look for the structural (weight) reason rather than infer a cause.

### Interview angle
> [!question] How it is asked
> "Sales and marketing spend are highly correlated. Does marketing drive sales?"

> [!tip] Strong answer includes
> - Plot first, check outliers and non-linearity
> - Name the confounder/reverse causality possibilities
> - Propose a test (geo A/B, holdout) or regression with controls
> - Avoid claiming causation from r alone

---

## 10. Z-Score (Standardization)
> 🔴 Tier 1 · _Tracker hint:_ Z = (X - μ) / σ; measures standard deviations from mean; used in comparisons

### Definition
$$Z=\frac{X-\mu}{\sigma}$$ (sample: $z=(x-\bar{x})/s$). It re-expresses a value as the number of standard deviations from the mean: mean 0, sd 1. Uses: **compare** values on different scales, flag **outliers** (|z|>3), compute normal probabilities, set **safety stock** ($SS=Z\sigma_{LT}$), and standardise features for machine learning. Normal rule: |z|<1 → 68%, <2 → 95%, <3 → 99.7%. Caveat: z-scores assume roughly symmetric data; extreme outliers inflate σ and hide themselves.

### Example
Supplier A delivers in 12 days where the benchmark is μ = 10, σ = 2: z = **1.00**. Supplier B takes 30 days where μ = 25, σ = 4: z = **1.25**. B is relatively worse even though A looks "earlier". Safety stock: demand σ over lead time = 80 units, 95% service → Z = 1.645, SS = 1.645 × 80 = **131.6 ≈ 132 units**.

### In the news
See news box. Standardising makes different indices comparable; the re-based series are compared via changes, not raw levels.

### Interview angle
> [!question] How it is asked
> "A student scored 78 in Maths (mean 70, sd 8) and 82 in English (mean 75, sd 10). Which is better relative to peers?"

> [!tip] Strong answer includes
> - Compute both: 1.00 vs 0.70, so Maths is relatively better
> - Interpret in sd units and percentile
> - Link to business use (safety stock, anomaly detection)
> - Note the normality assumption

---

## 11. ⭐ Advanced: Robust Statistics (MAD, Trimmed Mean) for Messy Operations Data
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Operations data has outliers (data-entry errors, one-off bulk orders). **Robust** measures resist them:
- **Median Absolute Deviation:** $MAD=\text{median}(|x_i-\text{median}(x)|)$. A robust z: $z_{robust}=0.6745\,(x_i-\tilde{x})/MAD$; flag $|z_{robust}|>3.5$ (Iglewicz–Hoaglin).
- **Trimmed mean:** drop a fixed % from each tail (for example 10%) before averaging.
- **Winsorising:** cap extremes at a percentile instead of removing them.
- Forecast accuracy can use **MAPE** or **WAPE** = Σ|actual−forecast| / Σ actual, which is stable when some SKUs are small.

### Example
Lead times 4, 5, 5, 6, 7, 8, 20: median 6; absolute deviations 2, 1, 1, 0, 1, 2, 14; MAD = **1**. Robust z for 20 = 0.6745×14/1 = **9.4** → clear outlier, whereas the ordinary z-score of 20 is only (20−7.86)/5.52 = **2.2**, i.e. the outlier masks itself.

### In the news
See news box. Statistical agencies use robust methods and careful outlier treatment when re-basing series.

### Interview angle
> [!question] How it is asked
> "Your dataset has a few extreme values. How do you decide what to do with them?"

> [!tip] Strong answer includes
> - Investigate cause first (error vs real)
> - Use robust statistics (median, MAD, trimmed mean)
> - Report with and without outliers for sensitivity
> - Document the rule applied

---

## 12. ⭐ Advanced: Simpson's Paradox and Aggregation Traps
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Simpson's paradox**: a trend present in several groups reverses when the groups are combined, because group sizes (weights) differ. It is a warning that **aggregate averages can mislead**; the cure is stratification and understanding the confounder. Related traps: averaging averages (use weighted mean), ecological fallacy, survivorship bias.

Weighted mean: $\bar{x}_w=\frac{\sum w_i x_i}{\sum w_i}$.

### Example
Two plants' on-time deliveries (on-time lines / total lines). **Plant X:** domestic 9/10 = 90%, X export 30/100 = 30%, overall 39/110 = **35.5%**. **Plant Y:** domestic 80/100 = 80%, export 2/10 = 20%, overall 82/110 = **74.5%**. In each segment X beats Y (90 vs 80, 30 vs 20), yet overall Y beats X, because X ships mostly the hard export mix.

### In the news
See news box. Changing the basket weights moved the headline inflation: a real-world case of "same prices, different mix, different aggregate".

### Interview angle
> [!question] How it is asked
> "Plant X beats Plant Y in every segment but Y looks better overall. How?"

> [!tip] Strong answer includes
> - Name the paradox and the mix/confounder cause
> - Compute weighted averages to show it
> - Recommend segment-level comparison
> - Warn against headline averages in performance reviews

---

---
## 🔗 Go deeper: expansion notes
- [[205 Sampling Distributions & Estimation|Sampling Distributions & Estimation]]
- [[215 Statistics Interview Question Bank & Numericals|Statistics Interview Question Bank & Numericals]]
- [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab|Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]]
