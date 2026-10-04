---
tags: [statistics, tier2]
area: Statistics
topic: "Non-Parametric Tests"
tier: Tier 2
roles: Analytics / Consulting / Operations
status: complete
subtopics: 14
---
# Non-Parametric Tests

⬅ [[205 Sampling Distributions & Estimation]] · [[_Index - Statistics|Statistics]] · [[207 Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** Analytics / Consulting / Operations

## Sub-topics in this note
1. [[#1. When to Use Non-Parametric Methods]]
2. [[#2. Sign Test]]
3. [[#3. Wilcoxon Signed-Rank Test]]
4. [[#4. Mann-Whitney U (Wilcoxon Rank-Sum) with Worked Ranks]]
5. [[#5. Kruskal-Wallis Test (and Post-hoc Dunn)]]
6. [[#6. Friedman Test (Repeated Measures / Blocked Designs)]]
7. [[#7. Spearman and Kendall Rank Correlation]]
8. [[#8. Goodness-of-Fit and Normality: Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk]]
9. [[#9. Runs (Wald-Wolfowitz) Test for Randomness]]
10. [[#10. Chi-square vs Fisher's Exact Test]]
11. [[#11. Permutation (Randomisation) Tests]]
12. [[#12. Power Trade-offs: When Rank Tests Win and Lose]]
13. [[#13. Decision Flowchart for Choosing a Test]]
14. [[#14. ⭐ Advanced: Python and Excel Recipes]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Mann-Whitney in A/B testing is under scrutiny
> **"Stop AbUsing the Mann-Whitney U Test" (Analytics-Toolkit, 9 January 2024).** The article argues that the test is routinely applied to skewed business metrics such as revenue per user although it tests a stochastic difference or shift in ranks, not the difference in means a business decision needs. Its simulations report the t-test reaching about 80% power against about 73% for MWU in one scenario (a 3.76% true difference), MWU power of 0.6% against 44% for the t-test in another (a 1.84% difference), and false-positive rates near 28% for MWU when the true mean difference was about zero (nominal 5%). Treat these as one vendor's simulations, but they show why the choice of test must match the question. ([Analytics-Toolkit](https://blog.analytics-toolkit.com/2024/stop-abusing-the-mann-whitney-u-test-mwu/))
>
> **The opposite practitioner view.** Experimentation-platform guidance (Statsig) recommends Mann-Whitney for heavily skewed metrics, outliers, small samples (under about 30 per group) and ordinal data such as ratings, noting that it does not compare means or medians as such, needs similar distribution shapes, and struggles with many ties; it advises running parametric and rank tests side by side as a sanity check. ([Statsig](https://www.statsig.com/perspectives/mannwhitney-nonparametric-abtesting))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. When to Use Non-Parametric Methods
> 🟠 Tier 2 · _Key points:_ Few distribution assumptions; ranks/signs; ordinal data, outliers, small $n$; trade-off is some power and a different hypothesis

### Definition
**Parametric** tests (z, t, ANOVA, Pearson) assume a distributional form (usually normal errors) and test parameters such as the mean. **Non-parametric** (distribution-free) tests rely on signs, ranks or resampling and need weaker assumptions. Use them when:
- data are **ordinal** (Likert 1-5, rankings, severity grades);
- **small $n$** with clear non-normality, or heavy outliers/skew (waiting times, claim sizes, revenue);
- the metric has **detection limits or ties** (counts, scores);
- you want results robust to outliers.

Costs: the null and alternative are about ranks or distributions (stochastic dominance, location shift), not always the mean; some loss of power when the normal model is true (the Wilcoxon-type tests keep about $3/\pi\approx95.5\%$ asymptotic relative efficiency versus the t-test under normality and can be more powerful under heavy tails); ties need corrections. With large samples the CLT ([[205 Sampling Distributions & Estimation]]) often lets the t-test survive moderate skew, so the case for rank tests is strongest for small, ordinal or outlier-prone data.

| Parametric | Non-parametric analogue |
|---|---|
| One-sample / paired t | Sign test, Wilcoxon signed-rank |
| Two-sample t | Mann-Whitney U (Wilcoxon rank-sum) |
| One-way ANOVA | Kruskal-Wallis |
| Repeated-measures ANOVA | Friedman |
| Pearson r | Spearman rho, Kendall tau |
| Normality (Shapiro) | Kolmogorov-Smirnov, Anderson-Darling |

### Example
Ten call-centre agents rate a new tool on a 1-5 scale before and after training. Ratings are ordinal, so means are questionable; a paired sign or Wilcoxon test is appropriate where the paired t-test is not.

### In the news
See news box. The live debate (rank test or mean test for skewed revenue?) is exactly the "what hypothesis do you really care about" question at the start of this note.

### Interview angle
> [!question] How it is asked
> "Your data are heavily skewed. What test would you use and why?"

> [!tip] Strong answer includes
> - First ask what you want to compare (means vs distributions); then check sample size and skew
> - Rank tests for ordinal or outlier-prone data; bootstrap or log-transform when the mean is the target
> - Know the trade-off: robust, slightly less powerful under normality, different hypothesis
> - Mention reporting an effect size, not only p

---
## 2. Sign Test
> 🟠 Tier 2 · _Key points:_ Count + vs -; $X\sim\text{Bin}(n,0.5)$ under H0; ignores magnitudes; ties dropped

### Definition
Tests whether the median of paired differences (or of a single sample against a hypothesised median) is zero. Drop zero differences, count $k$ positive signs among $n$ non-zero pairs. Under H0, $k\sim\text{Binomial}(n,\tfrac12)$, giving an exact p-value. It uses only direction, so it is the most assumption-light and least powerful of the paired tests, and works for ordinal data (better or worse) where differences cannot be measured. Normal approximation for $n>20$: $z=(k-n/2)/(\sqrt n/2)$.

### Example
Twelve customers compare the old and new packaging: 9 prefer new, 2 prefer old, 1 is indifferent. Drop the tie: $n=11$, $k=9$. Two-sided $p=2\times P(X\le2)=0.0654$ (one-sided 0.0327). At $\alpha=0.05$ two-sided, not significant; if the question was only "is new better?" the one-sided p of 0.033 would be. State the direction hypothesis before looking.

### In the news
See news box. Sign-type logic ("did more people prefer B?") is also the basis of simple win-rate comparisons in product experiments.

### Interview angle
> [!question] How it is asked
> "Nine of eleven customers prefer the new design. Is that enough?"

> [!tip] Strong answer includes
> - Binomial test with ties removed, exact p about 0.065 two-sided
> - Pre-register one-sided vs two-sided, small $n$ caveat
> - Upgrade to Wilcoxon signed-rank if magnitudes are meaningful

---
## 3. Wilcoxon Signed-Rank Test
> 🟠 Tier 2 · _Key points:_ Rank $|d_i|$, sum ranks of positive and negative differences; assumes symmetric differences; ties/zeros need care

### Definition
For paired data: compute $d_i=x_i-y_i$, drop zeros, rank $|d_i|$ (average ranks for ties), then $W^+=$ sum of ranks of positive $d$ and $W^-$ for negative $d$. Test statistic is $\min(W^+,W^-)$. Under H0, $E(W)=n(n+1)/4$ and $Var(W)=n(n+1)(2n+1)/24$, with a normal approximation for larger $n$ (exact tables for small $n$). It assumes differences are roughly symmetric around the median, and uses magnitudes through ranks, so it is more powerful than the sign test.

### Example
Cycle time (minutes) at 10 workstations before and after a layout change:

| Before | 38 | 42 | 35 | 51 | 47 | 40 | 44 | 39 | 53 | 36 |
|---|---|---|---|---|---|---|---|---|---|---|
| After | 35 | 40 | 36 | 44 | 41 | 40 | 39 | 37 | 45 | 34 |
| d | 3 | 2 | -1 | 7 | 6 | 0 | 5 | 2 | 8 | 2 |

Drop the zero ($n=9$). $|d|$ ranks: 1 gets rank 1; the three 2s share ranks 2,3,4 so each gets 3; 3 gets 5; 5 gets 6; 6 gets 7; 7 gets 8; 8 gets 9. $W^+=44$, $W^-=1$ (only the d = -1 pair). Statistic $=1$. SciPy: exact p $=0.0078$ (normal approximation without continuity correction: 0.0106; because of ties the approximate value is the safer one to quote). Paired t-test on the same data: $t=3.60$, $p=0.0058$, the same conclusion. Cycle times fell significantly.

### In the news
See news box. Paired before/after designs (same stores, same sites) are common in operations pilots and can use this test when the difference distribution is skewed.

### Interview angle
> [!question] How it is asked
> "You ran a pilot on 10 plants. Differences are skewed. What test and what do you report?"

> [!tip] Strong answer includes
> - Wilcoxon signed-rank (paired); mention symmetry assumption, else sign test
> - Report median difference (Hodges-Lehmann estimate) with CI
> - Handle zero differences and ties; exact vs approximate p

---
## 4. Mann-Whitney U (Wilcoxon Rank-Sum) with Worked Ranks
> 🟠 Tier 2 · _Key points:_ Pool, rank, sum ranks; $U_1=R_1-n_1(n_1+1)/2$; tests whether one group tends to be larger

### Definition
For two independent groups of sizes $n_1,n_2$: pool all values, rank from smallest (ties get the average rank), find rank sums $R_1,R_2$ and

$$U_1=R_1-\frac{n_1(n_1+1)}{2},\qquad U_2=n_1n_2-U_1,\qquad z=\frac{U-n_1n_2/2}{\sqrt{n_1n_2(n_1+n_2+1)/12}}$$

$U_1/(n_1n_2)$ equals $P(X_1>X_2)+\tfrac12P(X_1=X_2)$, the **probability of superiority** (common-language effect size). The test is a test of **location shift only if the two distributions have the same shape**; otherwise it tests stochastic dominance, which is not the same as equal means or medians.

### Example
Time to resolve tickets (minutes), team A ($n_1=5$): 12, 15, 11, 18, 14; team B ($n_2=7$): 16, 19, 22, 17, 21, 20, 25.

Sorted pooled: 11(A) 12(A) 14(A) 15(A) 16(B) 17(B) 18(A) 19(B) 20(B) 21(B) 22(B) 25(B). Ranks of A: 11 to rank 1, 12 to 2, 14 to 3, 15 to 4, 18 to 7. $R_A=1+2+3+4+7=17$, $R_B=78-17=61$ (total $12\cdot13/2=78$). $U_A=17-15=2$, $U_B=61-28=33$ (check: $2+33=35=5\times7$). Exact two-sided $p=0.0101$; normal approximation $z=-2.52$, $p=0.0118$ (0.0149 with continuity correction). Probability of superiority that a random B ticket takes longer than a random A ticket $=33/35=0.94$. Welch t gives $t=-3.56$, $p=0.0057$, consistent. The permutation test on the mean difference in sub-topic 11 returns the same exact p of 0.0101, because with no ties the rank-sum permutation distribution matches.

### In the news
See news box. This is the test at the centre of the Analytics-Toolkit critique and the Statsig defence; both agree the result is about ranks and probability of superiority, not a revenue difference.

### Interview angle
> [!question] How it is asked
> "Revenue per user is heavily skewed, so we used Mann-Whitney and it's significant. Can we say mean revenue went up?"

> [!tip] Strong answer includes
> - No: MWU supports "B tends to be larger", not a difference in means
> - If means matter, use Welch t with robust SEs, a bootstrap on the mean, or a log-scale analysis
> - Mention shape assumption, ties, and reporting probability of superiority with a CI
> - Connect to experimentation in [[214 Causal Inference & Experimentation Beyond A-B Tests]]

---
## 5. Kruskal-Wallis Test (and Post-hoc Dunn)
> 🟠 Tier 2 · _Key points:_ Rank all groups together; $H=\frac{12}{N(N+1)}\sum\frac{R_i^2}{n_i}-3(N+1)\sim\chi^2_{k-1}$; post hoc Dunn with correction

### Definition
The rank analogue of one-way ANOVA ([[089 Hypothesis Testing]]) for $k\ge3$ independent groups. Rank all $N$ observations jointly; with rank sums $R_i$:

$$H=\frac{12}{N(N+1)}\sum_{i=1}^k\frac{R_i^2}{n_i}-3(N+1)$$

compared with $\chi^2_{k-1}$ (needs roughly $n_i\ge5$). Software applies a tie correction. A significant H says at least one group differs; locate differences with **Dunn's test** (or pairwise Mann-Whitney) with Holm or Bonferroni adjustment.

### Example
Delivery delay (hours) for three suppliers, five deliveries each. S1: 4, 6, 5, 7, 3; S2: 8, 9, 7, 10, 11; S3: 5, 12, 13, 9, 14. Rank sums: $R_1=18$, $R_2=47$, $R_3=55$ (total 120 for $N=15$). $H=\frac{12}{15\cdot16}(18^2/5+47^2/5+55^2/5)-48=7.58$; with the tie correction SciPy reports $H=7.62$, $p=0.0221$. One-way ANOVA on the raw data: $F=6.82$, $p=0.0105$. Pairwise Mann-Whitney p-values (unadjusted): S1 vs S2 0.016, S1 vs S3 0.047, S2 vs S3 0.35; after Bonferroni (x3): 0.048, 0.14, 1.0. So the evidence is mainly that S1 is faster than S2; S3 differs from S1 only before correction. Use `scikit_posthocs.posthoc_dunn` in practice.

### In the news
See news box. When more than two variants run (A/B/C tests), rank-based omnibus tests need the same scrutiny as the two-group version.

### Interview angle
> [!question] How it is asked
> "Three DCs report different dwell times and the data are skewed. How do you test it?"

> [!tip] Strong answer includes
> - Kruskal-Wallis omnibus, then Dunn or pairwise MWU with multiplicity correction
> - Report effect size (epsilon-squared) and medians per group
> - Assumes similar shapes and independent groups; ANOVA vs KW consistency check

---
## 6. Friedman Test (Repeated Measures / Blocked Designs)
> 🟠 Tier 2 · _Key points:_ Rank within each block; $Q=\frac{12}{nk(k+1)}\sum R_j^2-3n(k+1)\sim\chi^2_{k-1}$

### Definition
Non-parametric analogue of repeated-measures or randomized-block ANOVA: $k$ treatments measured on each of $n$ blocks (stores, patients, days). Rank the $k$ values **within each block**, sum ranks per treatment $R_j$, and

$$Q=\frac{12}{nk(k+1)}\sum_{j=1}^kR_j^2-3n(k+1)\ \sim\ \chi^2_{k-1}\ (\text{approx})$$

Post hoc: Nemenyi or Wilcoxon with correction. Blocking removes store-to-store differences, the same idea as paired designs in [[092 Sampling & Experimental Design]] and [[213 Design of Experiments - Factorial, Fractional & Taguchi]]. With two treatments it reduces to the sign test.

### Example
Daily sales index at 8 stores under three shelf layouts (A, B, C): 7/9/8, 6/8/9, 8/9/7, 5/7/9, 6/6/8, 7/8/9, 4/6/7, 8/7/9. Within-store ranks give rank sums A = 10.5, B = 16.5, C = 21.0 (total 48 = 8x6). $Q=\frac{12}{8\cdot3\cdot4}(10.5^2+16.5^2+21^2)-3\cdot8\cdot4=0.125\times823.5-96=6.94$ ($p=0.031$) by hand; SciPy's tie-corrected value is 7.16 ($p=0.028$). Layout C is ranked best, A worst.

### In the news
See news box. Blocked comparisons guard against store/site effects, a design choice that matters more than the choice of test.

### Interview angle
> [!question] How it is asked
> "We tried three layouts in the same stores. Which analysis do you use?"

> [!tip] Strong answer includes
> - Treat stores as blocks; Friedman (or repeated-measures ANOVA if approximately normal)
> - Post hoc pairwise comparisons with correction
> - Note the practical limit: carryover/order effects need randomised or counterbalanced order

---
## 7. Spearman and Kendall Rank Correlation
> 🟠 Tier 2 · _Key points:_ Monotone association, robust to outliers; $\rho_s=1-\frac{6\sum d_i^2}{n(n^2-1)}$; Kendall $\tau=\frac{C-D}{n(n-1)/2}$

### Definition
**Spearman's $\rho_s$** is Pearson's correlation computed on ranks; with no ties $\rho_s=1-\frac{6\sum d_i^2}{n(n^2-1)}$ where $d_i$ is the rank difference. **Kendall's $\tau$** counts concordant ($C$) and discordant ($D$) pairs: $\tau=\frac{C-D}{n(n-1)/2}$ (tau-b adjusts for ties). Both detect **monotonic** (not only linear) relationships, resist outliers, and suit ordinal data. Kendall is preferred for small samples with many ties and has a more direct probabilistic meaning; its values are typically smaller in magnitude than Spearman's. Pearson ([[090 Regression Analysis]]) measures only linear association.

### Example
Eight suppliers: price index 10, 12, 15, 18, 20, 25, 28, 30 and quality score 62, 70, 65, 78, 74, 90, 82, 95. Price ranks 1 to 8; quality ranks 1, 3, 2, 5, 4, 7, 6, 8. $\sum d^2=0+1+1+1+1+1+1+0=6$, so $\rho_s=1-\frac{6\cdot6}{8\cdot63}=0.929$ ($p=0.0009$). Pairs: $C=25$, $D=3$ of 28, so $\tau=22/28=0.786$ ($p=0.0055$). Pearson $r=0.914$. Monotone-but-nonlinear case: $y=x^3$ for $x=1..10$ gives Pearson $r=0.928$ but Spearman exactly $1.0$.

### In the news
See news box. Rank correlations are standard in checking whether a model's ranking (risk scores, demand ranks) agrees with outcomes.

### Interview angle
> [!question] How it is asked
> "When would you use Spearman instead of Pearson?"

> [!tip] Strong answer includes
> - Ordinal data, outliers, monotone non-linear relationship
> - Interpretation: strength of monotone association, not causal or linear slope
> - Kendall for small $n$/ties; correlation is not causation, see [[214 Causal Inference & Experimentation Beyond A-B Tests]]

---
## 8. Goodness-of-Fit and Normality: Kolmogorov-Smirnov, Anderson-Darling, Shapiro-Wilk
> 🟠 Tier 2 · _Key points:_ KS = max gap between CDFs; AD weights tails; estimated parameters need Lilliefors/AD tables; low power at small $n$

### Definition
**One-sample KS:** $D=\sup_x|F_n(x)-F_0(x)|$ compares the empirical CDF to a fully specified distribution $F_0$. **Two-sample KS** compares two empirical CDFs (any difference in shape, location or spread). Critical caution: if you estimate parameters from the same data (mean and s.d. for a normality check), the standard KS p-values are too large (too conservative); use **Lilliefors**. **Anderson-Darling (AD)** squares the gap with extra weight on the tails and is generally more powerful against tail departures; **Shapiro-Wilk** is the usual powerful normality test for $n<5000$. No normality test replaces a Q-Q plot, because large samples reject trivial departures and small ones miss big ones.

### Example
25 delivery times (minutes, simulated from a gamma): mean 14.4, s.d. 9.7, max 36.8. SciPy `kstest` against a normal with fitted mean/s.d. gives $D=0.137$, $p=0.69$ (misleading as parameters were estimated); Lilliefors gives $p=0.26$; Shapiro-Wilk gives $W=0.894$, $p=0.013$; Anderson-Darling gives $A^2=0.856$, above the 2.5% critical value (0.845) but below the 1% value (1.001). The tail-sensitive tests detect the right skew that plain KS misses. Two-sample KS between these times and a slower route (22 times): $D=0.476$, $p=0.006$.

### In the news
See news box. Whether to use rank tests is often decided by a normality check; the KS pitfall above is why many analytics teams prefer Q-Q plots plus Shapiro or AD.

### Interview angle
> [!question] How it is asked
> "How do you check whether your data are normal, and does it matter?"

> [!tip] Strong answer includes
> - Q-Q plot and histogram first; Shapiro or AD second; Lilliefors correction for KS with estimated parameters
> - Matters for small-sample t-tests and for residuals in regression, less for large $n$ means
> - Two-sample KS for comparing whole distributions (for example model score drift in [[098 Model Selection & Optimization]])

---
## 9. Runs (Wald-Wolfowitz) Test for Randomness
> 🟠 Tier 2 · _Key points:_ Count runs of like symbols; too few = clustering/trend, too many = alternation; $\mu_R=1+\frac{2n_1n_2}{n_1+n_2}$

### Definition
A **run** is an unbroken sequence of the same symbol. Dichotomise the series (above/below median, up/down, pass/fail). With $n_1$ and $n_2$ symbols of each type and $R$ runs:

$$\mu_R=1+\frac{2n_1n_2}{n_1+n_2},\qquad \sigma_R^2=\frac{2n_1n_2(2n_1n_2-n_1-n_2)}{(n_1+n_2)^2(n_1+n_2-1)},\qquad z=\frac{R-\mu_R}{\sigma_R}$$

Too few runs means clustering (trend, shifts); too many means over-alternation (over-adjustment). Used to test randomness of residuals or of control-chart points ([[091 Statistical Quality Control (SQC)]], [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]).

### Example
20 days of defect counts coded 1 if above median, else 0: 1 1 1 0 0 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1. Here $n_1=11$, $n_2=9$, runs $R=7$. $\mu_R=1+2\cdot99/20=10.9$, $\sigma_R^2=4.64$, $z=-1.81$, two-sided $p=0.070$. Mild evidence of clustering (a drifting process), not conclusive at 5%.

### In the news
See news box. Run rules in control charts (many consecutive points on one side of the centre line) are the industrial version of this test.

### Interview angle
> [!question] How it is asked
> "How would you check if a process's output is random or has patterns?"

> [!tip] Strong answer includes
> - Runs chart/test about the median; compare actual runs to expected
> - Complement with autocorrelation (ACF) and control chart run rules
> - Explain what too few or too many runs signal

---
## 10. Chi-square vs Fisher's Exact Test
> 🟠 Tier 2 · _Key points:_ Fisher for small expected counts (<5) in 2x2; chi-square is an approximation; Yates correction conservative

### Definition
For a 2x2 table, **Pearson's chi-square** compares observed with expected counts using an asymptotic $\chi^2_1$ approximation, valid when expected counts are not small (rule: all above 5, some say above 1 with at most 20% below 5). **Fisher's exact test** computes the exact hypergeometric probability of tables as or more extreme given the margins, so it needs no large-sample approximation (conditioning on margins makes it slightly conservative). Yates' continuity correction is conservative; many statisticians now prefer Fisher or the Barnard test for small tables. For larger tables use the Freeman-Halton extension or Monte Carlo p-values. Chi-square basics are in [[089 Hypothesis Testing]]; odds ratios in [[209 Generalised Linear Models & Categorical Data Analysis]].

### Example
A pilot of 20 deliveries tests a new route planner: late deliveries with old method 8 of 10, with new 3 of 10. Table [[8,2],[3,7]] (late/on time). Expected counts are 5.5 and 4.5 (two cells just under 5). Uncorrected chi-square: $\chi^2=5.05$, $p=0.0246$. Yates-corrected: $\chi^2=3.23$, $p=0.072$. Fisher's exact (hypergeometric sum of tables as unlikely as observed): $p=0.0698$; sample odds ratio $=(8\cdot7)/(2\cdot3)=9.33$. The uncorrected chi-square rejects while the exact test does not: borderline results at small $n$ depend on the method, so report Fisher, the odds ratio and its wide CI.

### In the news
See news box. Small-pilot decisions are where the choice between exact and approximate tests changes the headline.

### Interview angle
> [!question] How it is asked
> "In a 2x2 with small counts, why not just use chi-square?"

> [!tip] Strong answer includes
> - Chi-square p-values rely on large expected counts; use Fisher (exact) when expected counts are small
> - Report odds ratio with CI; note Yates is conservative
> - Pilot decisions should be framed in terms of effect size and cost, not p alone

---
## 11. Permutation (Randomisation) Tests
> 🟠 Tier 2 · _Key points:_ Shuffle labels under H0; compute statistic on every (or many) permutations; exact, any statistic

### Definition
If the group labels are exchangeable under H0, then every re-assignment of labels is equally likely. Compute the statistic for the observed labelling and for all (or a random 10,000) permutations; the p-value is the share of permuted statistics at least as extreme. It works for any statistic (difference in means, medians, trimmed means, correlation), needs few assumptions, and is exact under randomisation. It differs from the bootstrap (which resamples with replacement to get intervals). Exchangeability fails for dependent data and for tests of equality of means when variances differ strongly.

### Example
Take the tickets from sub-topic 4 and use the mean difference (mean of B minus mean of A $=20.0-14.0=6.0$ minutes). All $\binom{12}{5}=792$ ways to assign five observations to "team A" were enumerated: 8 give an absolute mean difference at least as large as observed, so $p=8/792=0.0101$ (SciPy's `permutation_test` with 9,999 resamples also gave 0.0101). With no ties this coincides with the exact Mann-Whitney result.

```python
from scipy import stats
import numpy as np
A=[12,15,11,18,14]; B=[16,19,22,17,21,20,25]
res=stats.permutation_test((A,B), lambda x,y: np.mean(y)-np.mean(x),
                           permutation_type='independent', n_resamples=9999, random_state=1)
print(res.pvalue)   # 0.0101
```

### In the news
See news box. Because a permutation test can target the mean, it answers the "did average revenue change?" question that a rank test cannot, while still avoiding normality assumptions.

### Interview angle
> [!question] How it is asked
> "How would you test a difference in medians without assuming a distribution?"

> [!tip] Strong answer includes
> - Shuffle labels many times, recompute the median difference, get an empirical p-value
> - Contrast with bootstrap for CIs; mention exchangeability assumption
> - Use for odd statistics (ratios, percentiles); mention compute is cheap

---
## 12. Power Trade-offs: When Rank Tests Win and Lose
> 🟠 Tier 2 · _Key points:_ ARE 0.955 under normality; much higher under heavy tails; MWU can lose power or be miscalibrated for mean shifts in skewed data

### Definition
Asymptotic relative efficiency (ARE) of the Wilcoxon/Mann-Whitney versus the t-test is $3/\pi\approx0.955$ for normal data, at least 0.864 for any continuous distribution, and can be well above 1 for heavy-tailed or contaminated data. So rank tests lose little under normality and can gain a lot with outliers. But the hypothesis differs: with unequal variances or shapes, MWU can reject when means are equal and can miss differences in means. The sign test has ARE $2/\pi\approx0.64$ against the t-test under normality.

### Example
Simulation ($n=30$ per group, 4,000 runs, $\alpha=0.05$, shift added to group B):

| Population | Shift | Welch t power | Mann-Whitney power |
|---|---|---|---|
| Normal | 0.7 | 75.7% | 73.3% |
| Student t, 3 d.f. | 1.0 | 67.1% | 83.0% |
| Lognormal ($\sigma=1$) | 1.0 (additive) | 55.6% | 95.5% |

Under normality the loss is small (about 2 points); with heavy tails or skew the rank test is much more powerful at detecting a location shift. This simulation is a pure location shift; if instead the two groups differ in spread or the business cares about means, the news-box critique applies. Null check: for lognormal data with no shift, rejection rates were 3.7% (t) and 4.7% (MWU), both near 5%.

### In the news
See news box. The reported 80% versus 73% power gap and the Statsig recommendation describe the two sides of this trade-off in the context of skewed revenue.

### Interview angle
> [!question] How it is asked
> "Is a non-parametric test always safer?"

> [!tip] Strong answer includes
> - No: it answers a different question and can have lower power or miscalibrated error rates for mean differences when shapes differ
> - Under normality ARE 95%, under heavy tails often better
> - Decide by hypothesis of interest, data type and diagnostics; simulate if unsure

---
## 13. Decision Flowchart for Choosing a Test
> 🟠 Tier 2 · _Key points:_ Outcome type, number of groups, paired or independent, assumptions, sample size

### Definition
Work through four questions: (1) **Outcome type**: continuous, ordinal, binary/count, time-to-event. (2) **Groups**: one sample vs a value, two groups, 3+ groups. (3) **Design**: paired/blocked vs independent. (4) **Assumptions**: normal enough (or large $n$) and equal variance; if not, go rank/resampling.

```text
Outcome continuous or ordinal?
 |-- One sample vs value:  normal? -> one-sample t      | no -> sign / Wilcoxon signed-rank
 |-- Two groups
 |     paired      : normal diffs? -> paired t          | no -> Wilcoxon signed-rank (or sign)
 |     independent : normal/large n? -> Welch t         | no -> Mann-Whitney U / permutation
 |-- 3+ groups
 |     independent : normal, equal var? -> ANOVA        | no -> Kruskal-Wallis (+ Dunn)
 |     repeated    : normal? -> RM-ANOVA                | no -> Friedman (+ Nemenyi)
 |-- Association    : linear/normal -> Pearson           | monotone/ordinal -> Spearman / Kendall
Outcome binary/categorical:
 |-- 2x2 : expected counts >=5 -> chi-square (or z for proportions) | small -> Fisher exact
 |-- r x c: chi-square (Monte Carlo / Freeman-Halton if sparse)
Distribution shape: Q-Q plot, Shapiro / Anderson-Darling; KS two-sample for whole-distribution comparison
Randomness of a sequence: runs test, ACF
Anything awkward: permutation test or bootstrap on the statistic you care about
```

### Example
A retailer compares basket values across 4 regions (skewed, 40 baskets per region). Independent, 3+ groups, skewed: Kruskal-Wallis then Dunn with Holm; but since the CFO wants *mean* basket value, also run a bootstrap or Welch ANOVA on logs and report both. Customer satisfaction scores (1-5) for 3 chatbot versions in the same users: Friedman.

### In the news
See news box. The debate over MWU on revenue illustrates why step (1) (what is the estimand?) comes before the flowchart.

### Interview angle
> [!question] How it is asked
> "Walk me through how you decide which statistical test to use."

> [!tip] Strong answer includes
> - Structured decision: outcome, groups, pairing, assumptions, then diagnostics
> - Mention effect size, multiple comparisons, and checking robustness with a second method
> - Mention the business estimand (mean, median, proportion) before the test name

---
## 14. ⭐ Advanced: Python and Excel Recipes
> ⭐ Advanced · _Added beyond the tracker_

### Definition
SciPy covers all tests in this note; Excel needs formula work (ToolPak has t-tests, ANOVA and correlation, but no Wilcoxon, Mann-Whitney, Kruskal-Wallis or Friedman; add-ins such as Real Statistics fill the gap). See [[067 Statistical Analysis in Python]] and [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]].

### Example
Python (executed with SciPy 1.17; results quoted in earlier sub-topics):

```python
from scipy import stats
stats.binomtest(9, 11, 0.5)                              # sign test (p = 0.0654)
stats.wilcoxon(before, after)                            # signed-rank, paired
stats.mannwhitneyu(A, B, alternative='two-sided')        # U for the FIRST sample
stats.kruskal(g1, g2, g3)                                # Kruskal-Wallis
stats.friedmanchisquare(x1, x2, x3)                      # Friedman (columns = treatments)
stats.spearmanr(x, y); stats.kendalltau(x, y)            # rank correlation
stats.shapiro(x); stats.anderson(x, 'norm', method='interpolate')
stats.ks_2samp(x, y)                                     # two-sample KS
stats.fisher_exact([[8, 2], [3, 7]])                     # odds ratio 9.33, p = 0.0698
stats.permutation_test((A, B), statistic, permutation_type='independent')
```

Excel Mann-Whitney recipe (data in A2:A13, group label in B2:B13): `=RANK.AVG(A2,$A$2:$A$13,1)` for ranks; `R1 =SUMIF(B2:B13,"A",C2:C13)`; `U1 = R1 - n1*(n1+1)/2`; `z =(U1-n1*n2/2)/SQRT(n1*n2*(n1+n2+1)/12)`; `p =2*(1-NORM.S.DIST(ABS(z),TRUE))`. For the tickets example: $U=2$, $z=-2.52$, $p=0.0118$. Spearman: `=CORREL(rank_x_range, rank_y_range)`. Kruskal-Wallis p: `=CHISQ.DIST.RT(H, k-1)` (for $H=7.58$, $k=3$ this returns 0.0226). Fisher exact for [[8,2],[3,7]]: sum `HYPGEOM.DIST` over the tables at most as likely as observed, which gives 0.0698.

### In the news
See news box. Experimentation platforms ship Mann-Whitney as a default option for skewed metrics, which is why knowing the underlying calculation (not just the button) matters.

### Interview angle
> [!question] How it is asked
> "Can you run a Mann-Whitney in Excel, or would you use Python?"

> [!tip] Strong answer includes
> - Excel by ranks and the z formula (RANK.AVG, SUMIF, NORM.S.DIST) and caveats with ties and small $n$
> - Python/SciPy for exact p-values and permutation tests; document version and the `method` argument
> - Know to verify a result with two methods and report effect size
