---
tags: [statistics, tier1]
area: Statistics
topic: "Hypothesis Testing"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 15
---
# Hypothesis Testing

⬅ [[088 Probability Distributions]] · [[_Index - Statistics|Statistics]] · [[090 Regression Analysis]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Framework]]
2. [[#2. Type I Error (α)]]
3. [[#3. Type II Error (β)]]
4. [[#4. p-value Interpretation]]
5. [[#5. One-tailed vs Two-tailed]]
6. [[#6. One-Sample Z-test]]
7. [[#7. One-Sample t-test]]
8. [[#8. Two-Sample t-test (Independent)]]
9. [[#9. Paired t-test]]
10. [[#10. Chi-Square Test (Independence)]]
11. [[#11. Chi-Square Goodness of Fit]]
12. [[#12. ANOVA (One-Way)]]
13. [[#13. Two-Way ANOVA]]
14. [[#14. ⭐ Advanced: Sample Size, Effect Size and Power for A/B Tests]]
15. [[#15. ⭐ Advanced: Multiple Testing, Bonferroni and p-hacking]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Two re-based statistics, one regulator going Bayesian
> **FDA draft guidance on Bayesian methods (9 Jan 2026).** The FDA clarified how Bayesian approaches can support regulatory decisions in clinical trials, including primary inference in Phase III, by combining prior knowledge with accumulating data. The classical frequentist approach starts from a null hypothesis and controls error rates (the topic of this note); Bayesian methods instead estimate the probability that a treatment works. Know both framings. ([Alston and Bird summary](https://www.alston.com/en/insights/publications/2026/01/fda-bayesian-guidance-drug-trials))
>
> **New CPI base (Feb 2026).** The January 2026 inflation reading on the new base (2024=100) was 2.75%, versus 1.3% for December 2025 on the old series, a gap driven by new weights (food share down from 45.86% to 36.75%). A reminder that measurement choices, not only real change, can move a headline number. ([Upstox explainer of the MoSPI release](https://upstox.com/learning-center/personal-finance/what-changed-in-indias-new-cpi-series-and-how-it-impacts-the-economy-and-inflation/article-1518/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Framework
> 🔴 Tier 1 · _Tracker hint:_ State H0 & H1 → Choose test → Collect data → Calculate test stat → Compare to critical value/p-value → Decision

### Definition
Hypothesis testing uses sample data to decide between a **null hypothesis H0** (status quo, "no effect", always contains equality) and an **alternative H1** (what you want evidence for). Steps:
1. State H0 and H1 (before seeing data).
2. Choose significance level $\alpha$ (usually 0.05) and the right test (data type, number of groups, σ known, paired?).
3. Collect data (check assumptions: random sample, normality or large n, independence).
4. Compute the test statistic: $\frac{\text{estimate}-\text{hypothesised value}}{\text{standard error}}$.
5. Compare to the critical value, or compute the p-value.
6. Decide and state in business words. "Fail to reject H0" is not "H0 is true".

Choosing a test: one mean (z or t), two means (independent t or paired t), 3+ means (ANOVA), categorical relationships (chi-square), proportions (z for proportions).

### Example
Claim: bags contain 500 g. H0: μ = 500; H1: μ ≠ 500; α = 0.05. n = 36, x̄ = 496.5, σ = 10 known. $z=(496.5-500)/(10/6)=-2.10$; critical ±1.96, so reject H0: evidence the mean differs (p = 0.036).

### In the news
See news box. Frequentist testing (this note) and Bayesian updating are the two accepted frameworks; the FDA now describes both.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would test whether a new process reduces defects."

> [!tip] Strong answer includes
> - H0/H1 stated clearly, chosen test with justification
> - α, sample size/power planned in advance
> - Test statistic, p-value, decision in plain business language
> - Check assumptions and practical significance (effect size), not only p

---

## 2. Type I Error (α)
> 🔴 Tier 1 · _Tracker hint:_ Reject true H0; False Positive; α = significance level (usually 0.05)

### Definition
A **Type I error** is rejecting H0 when H0 is true (a false alarm). Its probability is the **significance level** $\alpha=P(\text{reject }H_0\mid H_0\text{ true})$. You choose α in advance; lower α means fewer false positives but more false negatives (for the same n). Business equivalents: launching a feature that does not work, accusing an innocent supplier of poor quality, stopping a healthy process (producer's risk in quality control).

**Multiple testing:** with $m$ independent tests at α, $P(\text{at least one false positive})=1-(1-\alpha)^m$.

### Example
Run 20 independent A/B tests at α = 0.05 where none has a real effect. Expected false positives = 20×0.05 = **1**; probability at least one = $1-0.95^{20}=\mathbf{64.2\%}$. Hence one "significant" result among 20 should not be celebrated.

### In the news
See news box. Regulators set stringent α-control rules because a Type I error means approving an ineffective treatment.

### Interview angle
> [!question] How it is asked
> "What is a Type I error and give a business example?"

> [!tip] Strong answer includes
> - Reject a true H0 (false positive); probability = α
> - Concrete example (launch a useless feature, scrap good batch)
> - Cost of this error vs the other
> - Multiple-testing caution (Bonferroni)

---

## 3. Type II Error (β)
> 🔴 Tier 1 · _Tracker hint:_ Fail to reject false H0; False Negative; Power = 1-β

### Definition
A **Type II error** is failing to reject H0 when H1 is true (a miss), with probability $\beta$. **Power** $=1-\beta$ is the probability of detecting a real effect. Power rises with: larger sample size, larger true effect, larger α, smaller variability. Planning for 80% (or 90%) power is standard.

| | H0 true | H0 false |
|---|---|---|
| Reject H0 | Type I error (α) | Correct (power) |
| Fail to reject | Correct | Type II error (β) |

For a one-sided z-test, $\beta=\Phi\!\left(z_{\alpha}-\frac{\delta}{\sigma/\sqrt{n}}\right)$ where $\delta=\mu_1-\mu_0$.

### Example
H0: μ = 100; σ = 10; n = 25 (SE = 2); α = 0.05 one-sided. Reject if $\bar{x}>100+1.645\times2=103.29$. If the true mean is 105: β = P(x̄ < 103.29 | μ=105) = Φ((103.29−105)/2) = Φ(−0.855) = **0.196**, power = **0.804** (about 80%). With n = 9 (SE = 3.33) power drops to roughly 44% (β = Φ(1.645 − 5/3.33) = 0.56).

### In the news
See news box. Underpowered studies miss real effects; the Bayesian approach is partly pitched as a way to use data more efficiently.

### Interview angle
> [!question] How it is asked
> "What is the power of a test and how can you increase it?"

> [!tip] Strong answer includes
> - Power = 1 − β = detecting a true effect
> - Levers: n, effect size, α, variance reduction
> - Trade-off between Type I and II errors
> - Pre-test sample size calculation

---

## 4. p-value Interpretation
> 🔴 Tier 1 · _Tracker hint:_ P(observing result | H0 is true); p < α → reject H0; p > α → fail to reject

### Definition
The **p-value** is the probability, assuming H0 is true, of obtaining a test statistic at least as extreme as the one observed. Decision: $p<\alpha\Rightarrow$ reject H0. Smaller p = stronger evidence against H0.

Common misreadings (all wrong): p is *not* the probability H0 is true; *not* the probability the result is due to chance alone; *not* the size or importance of the effect; p > 0.05 does *not* prove no effect. Always report effect size and a confidence interval alongside.

### Example
A/B test: Variant A converts 200/5,000 = 4.0%; B converts 240/5,000 = 4.8%. Pooled p̂ = 440/10,000 = 0.044; SE = √(0.044×0.956×(2/5000)) = 0.0041. z = 0.008/0.0041 = **1.95**; two-sided p = **0.051**. Not below 0.05, so formally fail to reject, though it is close, so collect more data or consider the cost of a wrong decision before dropping B.

### In the news
See news box. The shift toward posterior probabilities (Bayesian) is partly a response to p-value misinterpretation.

### Interview angle
> [!question] How it is asked
> "p = 0.03. What does it mean?"

> [!tip] Strong answer includes
> - If H0 were true, a result this extreme would occur about 3% of the time
> - Not the probability that H0 is true
> - Compare with α; add effect size and CI
> - Practical vs statistical significance

---

## 5. One-tailed vs Two-tailed
> 🔴 Tier 1 · _Tracker hint:_ Two-tailed: H1: μ ≠ μ0; One-tailed: H1: μ > μ0 or H1: μ < μ0

### Definition
- **Two-tailed:** H1: μ ≠ μ0; rejection region split α/2 in each tail. Detects change in either direction.
- **Right-tailed:** H1: μ > μ0; **left-tailed:** H1: μ < μ0; all α in one tail. More power in the specified direction, but cannot detect an effect in the opposite direction.

| α | One-tailed Z | Two-tailed Z |
|---|---|---|
| 0.05 | 1.645 | ±1.960 |
| 0.01 | 2.326 | ±2.576 |

Choose direction **before** seeing data and on logic (a safety claim "at least" is one-tailed; "different from standard" is two-tailed). One-sided p = half of two-sided p when the effect is in the predicted direction.

### Example
New process claimed to cut cycle time (μ0 = 20 min). Left-tailed H1: μ < 20. z = −1.8: one-tailed p = 0.036 (reject at 5%); two-tailed p = 0.072 (fail). The test choice changes the verdict, so it must be justified up front, not after the data.

### In the news
See news box. Not tied to a specific recent event; in practice, directional claims about safety or harm deserve a two-sided look because an effect in the unexpected direction still matters.

### Interview angle
> [!question] How it is asked
> "When would you use a one-tailed test, and what is the risk?"

> [!tip] Strong answer includes
> - Direction pre-specified with business logic
> - Higher power in that direction, blind to the opposite effect
> - Critical value difference (1.645 vs 1.96)
> - Do not switch after seeing data (p-hacking)

---

## 6. One-Sample Z-test
> 🔴 Tier 1 · _Tracker hint:_ Z = (x̄ - μ0) / (σ/√n); σ known, large sample; test if mean = claimed value

### Definition
$$Z=\frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}\sim N(0,1)\text{ under }H_0$$
Use when σ is known (or n large, ≥30, with $s$ as a good estimate) and data are approximately normal or n large (CLT). Reject (two-tailed, α = 0.05) if $|Z|>1.96$. Confidence interval: $\bar{x}\pm1.96\,\sigma/\sqrt{n}$. Proportion version: $Z=\frac{\hat{p}-p_0}{\sqrt{p_0(1-p_0)/n}}$. Excel: `=Z.TEST(array, μ0, σ)` (gives one-tailed p).

### Example
A filling machine should deliver 500 g, σ = 10 g known. Sample n = 36, x̄ = 496.5. SE = 10/6 = 1.667. $Z=-3.5/1.667=\mathbf{-2.10}$; two-tailed p = 0.036 < 0.05, so reject H0. 95% CI: 496.5 ± 3.27 = (493.2, 499.8), which excludes 500.

### In the news
See news box. Large-sample z-tests are the workhorse for comparing survey-based national figures.

### Interview angle
> [!question] How it is asked
> "A supplier claims average delivery of 4 days. How would you check this with 50 deliveries?"

> [!tip] Strong answer includes
> - H0: μ = 4, H1: μ ≠ 4 (or > 4 if testing for lateness)
> - Z vs t (σ known? n large)
> - Compute statistic, interpret p and CI
> - Check outliers/skew in the data

---

## 7. One-Sample t-test
> 🔴 Tier 1 · _Tracker hint:_ t = (x̄ - μ0) / (s/√n); σ unknown; df=n-1; compare to t-critical

### Definition
$$t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}},\quad df=n-1$$
Used when σ is unknown (the usual case), especially for small n; requires roughly normal data (robust for moderate n). Reject if $|t|>t_{\alpha/2,\,n-1}$ or if p < α. Python: `scipy.stats.ttest_1samp(x, popmean=50)`; Excel: `=T.TEST` (for two samples) or compute with `T.DIST.2T`.

### Example
n = 16, x̄ = 52, s = 8, μ0 = 50. SE = 8/4 = 2; $t=2/2=\mathbf{1.00}$, df = 15; critical value 2.131, so **fail to reject** (p ≈ 0.33). The 2-unit difference is not distinguishable from sampling noise with this sample. With n = 64, SE = 1 and t = 2.0 (df 63, crit ≈ 2.00, borderline).

### In the news
See news box. Small-sample evidence early in a study is assessed with t-based intervals before large trials.

### Interview angle
> [!question] How it is asked
> "A pilot with 12 stores raised average sales by ₹2,000. Is it real?"

> [!tip] Strong answer includes
> - t-test on the lift against 0 (or paired by store vs baseline)
> - df = n − 1, critical value, p-value
> - Assumptions (approx. normal differences) and sample size
> - Report effect with confidence interval

---

## 8. Two-Sample t-test (Independent)
> 🔴 Tier 1 · _Tracker hint:_ Test difference between two group means; pooled vs Welch's t-test

### Definition
Tests H0: μ1 = μ2 for two independent groups.
- **Pooled (equal variance):** $s_p^2=\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}$, $t=\frac{\bar{x}_1-\bar{x}_2}{s_p\sqrt{1/n_1+1/n_2}}$, $df=n_1+n_2-2$.
- **Welch (unequal variance):** $t=\frac{\bar{x}_1-\bar{x}_2}{\sqrt{s_1^2/n_1+s_2^2/n_2}}$ with Welch–Satterthwaite df. Safer default; software: `ttest_ind(a, b, equal_var=False)`.

Check variances (Levene or F-test), normality, independence. For skewed data use Mann-Whitney.

### Example
Line A: n = 10, x̄ = 42, s = 4; Line B: n = 12, x̄ = 38, s = 5. $s_p^2=(9\times16+11\times25)/20=20.95$, $s_p=4.577$; SE = 4.577×√(1/10+1/12) = 4.577×0.4282 = **1.960**. $t=4/1.96=\mathbf{2.04}$, df = 20; critical 2.086, so fail to reject at 5% (p ≈ 0.055). Borderline; get more data.

### In the news
See news box. A/B tests on websites and plants are comparisons of two independent groups.

### Interview angle
> [!question] How it is asked
> "Two plants have different average defect rates. How do you know the difference is real?"

> [!tip] Strong answer includes
> - Two-sample test; pooled vs Welch choice
> - Assumptions and checks
> - Effect size and confidence interval for the difference
> - Practical significance and confounders (product mix)

---

## 9. Paired t-test
> 🔴 Tier 1 · _Tracker hint:_ Before-after; same subjects; d = x1-x2; t = d̄ / (sd/√n)

### Definition
For **dependent** (matched) observations, such as before and after on the same unit. Work with differences $d_i=x_{1i}-x_{2i}$:
$$t=\frac{\bar{d}}{s_d/\sqrt{n}},\quad df=n-1$$
H0: mean difference = 0. Pairing removes between-subject variability, giving more power than an independent test. Requires differences roughly normal. Python: `ttest_rel(before, after)`. If the same subjects are measured twice, using the independent test is a classic error.

### Example
Cycle time (min) of 5 workstations before vs after training; reductions d = 3, 5, 2, 4, 6. $\bar{d}=4$; deviations −1, 1, −2, 0, 2 → sum of squares 10; $s_d=\sqrt{10/4}=1.581$; SE = 1.581/√5 = 0.707; $t=4/0.707=\mathbf{5.66}$, df = 4, critical 2.776, so **reject H0** (p ≈ 0.005): the training reduced cycle time.

### In the news
See news box. Before/after pilots (new base vs old base statistics) are paired comparisons by construction.

### Interview angle
> [!question] How it is asked
> "You measured productivity of the same 30 employees before and after a new tool. Which test?"

> [!tip] Strong answer includes
> - Paired t-test on differences; why not independent
> - Assumption on differences; Wilcoxon if non-normal
> - Beware time effects/no control group
> - Report mean change with CI

---

## 10. Chi-Square Test (Independence)
> 🔴 Tier 1 · _Tracker hint:_ Test if two categorical variables are related; χ² = Σ(O-E)²/E

### Definition
Tests H0: two categorical variables are independent. Build a contingency table; expected count $E_{ij}=\frac{\text{row total}\times\text{column total}}{\text{grand total}}$; 
$$\chi^2=\sum\frac{(O-E)^2}{E},\quad df=(r-1)(c-1)$$
Right-tailed. Conditions: counts (not percentages), independent observations, expected count ≥ 5 in most cells (else Fisher's exact). A significant result shows association, not its strength (use Cramér's V) or causation.

### Example
Defects by shift. Shift A: 20 defective, 180 OK; Shift B: 40 defective, 160 OK. Totals: 200, 200; defective 60, OK 340; N = 400. Expected: defective 30 each shift, OK 170 each. $\chi^2=\frac{(20-30)^2}{30}+\frac{(40-30)^2}{30}+\frac{(180-170)^2}{170}+\frac{(160-170)^2}{170}=3.33+3.33+0.59+0.59=\mathbf{7.84}$; df = 1, critical 3.841, so **reject**: defects depend on shift (p ≈ 0.005).

### In the news
See news box. Categorical survey outcomes (for example household expenditure categories) are analysed with such tests.

### Interview angle
> [!question] How it is asked
> "Is customer segment related to product preference?" (given a table)

> [!tip] Strong answer includes
> - Expected counts, χ² formula, df
> - Conditions (expected ≥ 5, counts)
> - Interpret: association not causation; look at which cells contribute
> - Effect size (Cramér's V)

---

## 11. Chi-Square Goodness of Fit
> 🔴 Tier 1 · _Tracker hint:_ Test if observed distribution matches expected; df=k-1

### Definition
Tests H0: the data follow a specified distribution (for example uniform, or given proportions). 
$$\chi^2=\sum_{i=1}^{k}\frac{(O_i-E_i)^2}{E_i},\quad df=k-1-m$$
where $m$ is the number of parameters estimated from data (0 if the distribution is fully specified). Conditions: expected counts ≥ 5. Used to check a die, a demand pattern across weekdays, or whether data are Poisson/normal before using a model.

### Example
A die rolled 60 times gives faces 1–6: 5, 8, 9, 8, 10, 20. Expected = 10 each. $\chi^2=(25+4+1+4+0+100)/10=\mathbf{13.4}$; df = 5, critical 11.07, so **reject** fairness (p ≈ 0.020): the die over-produces 6. Another use: orders expected evenly across 5 weekdays, but Monday gets double the share, which breaks the staffing plan.

### In the news
See news box. Checking that data follow assumed distributions underlies model validation in official statistics.

### Interview angle
> [!question] How it is asked
> "How would you test whether arrivals per hour follow a Poisson distribution?"

> [!tip] Strong answer includes
> - Bin counts, compute Poisson expected counts using estimated λ
> - χ² with df = k − 1 − 1
> - Merge sparse bins (expected < 5)
> - Interpretation and next step if rejected

---

## 12. ANOVA (One-Way)
> 🔴 Tier 1 · _Tracker hint:_ Compare means of 3+ groups; F = variance between/variance within; post-hoc tests

### Definition
Tests H0: μ1 = μ2 = ... = μk against "at least one differs". Why not repeated t-tests: error inflates ($1-0.95^m$).

| Source | SS | df | MS | F |
|---|---|---|---|---|
| Between | SSB | k − 1 | SSB/(k−1) | MSB/MSW |
| Within | SSW | N − k | SSW/(N−k) | |

$F=\frac{MSB}{MSW}\sim F_{k-1,\,N-k}$ under H0. Assumptions: independence, normal residuals, equal variances. Significant F says only that some difference exists; **post-hoc tests** (Tukey HSD, Bonferroni) find which pairs. Python: `scipy.stats.f_oneway(a,b,c)`.

### Example
Three suppliers, 3 deliveries each (days): A 20, 22, 21; B 24, 25, 23; C 30, 29, 31. Means 21, 24, 30; grand mean 25. SSB = 3(16+1+25) = 126; SSW = 2+2+2 = 6. MSB = 126/2 = 63; MSW = 6/6 = 1; **F = 63**, critical $F_{0.05}(2,6)=5.14$, so reject: suppliers differ. Tukey then shows C is slower than A and B.

### In the news
See news box. Multi-arm trials (several doses versus control) are analysed with ANOVA-type methods.

### Interview angle
> [!question] How it is asked
> "You tested 4 packaging designs on sales. How do you decide which one is best?"

> [!tip] Strong answer includes
> - ANOVA first (not many t-tests), then post-hoc
> - Assumptions check; non-parametric alternative (Kruskal-Wallis)
> - Effect size ($\eta^2=SSB/SST$)
> - Business interpretation and cost

---

## 13. Two-Way ANOVA
> 🔴 Tier 1 · _Tracker hint:_ Two factors + interaction effect; factorial design; main effects vs interaction

### Definition
Studies the effect of **two factors** on a numeric outcome in a **factorial design** (every combination of levels). It tests three hypotheses: main effect of factor A, main effect of factor B, and the **A×B interaction** (the effect of one factor depends on the level of the other). Decomposition: $SST=SS_A+SS_B+SS_{AB}+SSE$, each tested with an F ratio against MSE. **Interpret the interaction first**; if it is significant, main effects can be misleading. Replicates per cell are needed to estimate interaction. A profile plot with non-parallel lines suggests interaction.

### Example
Output (units) by Machine and Shift, cell means: A-Day 50, A-Night 52; B-Day 60, B-Night 50. Machine means: A = 51, B = 55; shift means: Day = 55, Night = 51. B beats A by 10 on day shift but loses by 2 at night: lines cross, so **interaction** exists. Recommending "use Machine B" would be wrong without specifying the shift.

### In the news
See news box. Experiments in operations and marketing increasingly use factorial designs to test several levers at once.

### Interview angle
> [!question] How it is asked
> "How would you test price and packaging together on sales?"

> [!tip] Strong answer includes
> - Factorial design with replication
> - Main effects vs interaction; examine interaction first
> - Check assumptions, then post-hoc/simple-effects analysis
> - Efficiency compared with one-factor-at-a-time

---

## 14. ⭐ Advanced: Sample Size, Effect Size and Power for A/B Tests
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Before an experiment decide the **minimum detectable effect (MDE)** and size the sample. For comparing two means (equal groups, two-sided):
$$n\ \text{per group}=\frac{2\,(z_{1-\alpha/2}+z_{1-\beta})^2\,\sigma^2}{\delta^2}$$
With α = 0.05 and power 80%: $(1.96+0.84)^2=7.84$. For two proportions use $n=\frac{(z_{1-\alpha/2}+z_{1-\beta})^2\,[p_1(1-p_1)+p_2(1-p_2)]}{(p_1-p_2)^2}$. **Effect size** (Cohen's d = δ/σ): 0.2 small, 0.5 medium, 0.8 large. Halving the MDE quadruples n. Avoid peeking and stopping early without sequential corrections.

### Example
Average order value σ = ₹10 (illustrative); want to detect δ = ₹2: n = 2×7.84×100/4 = **392 per group**. To detect δ = ₹1: 1,568 per group (4×). For conversion 4.0% vs 4.8%: $[0.04\times0.96+0.048\times0.952]=0.0384+0.0457=0.0841$; $n=7.84\times0.0841/0.008^2=\mathbf{10{,}302}$ per group, so the 5,000-per-arm test above was underpowered.

### In the news
See news box. Trial guidance (Bayesian or frequentist) puts heavy weight on pre-specifying design and sample size.

### Interview angle
> [!question] How it is asked
> "How long should we run this A/B test?"

> [!tip] Strong answer includes
> - MDE, baseline rate, α, power → n; divide by traffic for days
> - Run full weeks to cover seasonality
> - No peeking, or use sequential methods
> - Decide on business significance, not only statistical

---

## 15. ⭐ Advanced: Multiple Testing, Bonferroni and p-hacking
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Testing many hypotheses inflates false positives. **Family-wise error rate** $=1-(1-\alpha)^m$. Corrections:
- **Bonferroni:** use $\alpha/m$ per test (conservative).
- **Holm:** step-down, uniformly more powerful than Bonferroni.
- **Benjamini–Hochberg:** controls the **false discovery rate**, used when screening many metrics.

**p-hacking** (slicing data until something is "significant", optional stopping, switching one/two-tailed) invalidates p-values. Defences: pre-registration of hypotheses and metrics, a single primary metric, holdout validation, and reporting all tests run.

### Example
20 metrics tested at α = 0.05: chance of ≥ 1 false positive is 64%. Bonferroni threshold = 0.05/20 = **0.0025**; a p of 0.03 on one metric is not significant after correction. Slicing one flat experiment into 10 customer segments gives about 40% chance of at least one "significant" segment by luck ($1-0.95^{10}=0.40$).

### In the news
See news box. Regulatory guidance stresses prespecified analyses and error control for the same reason.

### Interview angle
> [!question] How it is asked
> "Your A/B test showed no overall effect, but one segment shows a big win. Do you ship it?"

> [!tip] Strong answer includes
> - Segment finding is exploratory; multiple-comparison problem
> - Correct (Bonferroni/BH) or treat as hypothesis for a follow-up test
> - Pre-specified primary metric and segments
> - Replicate before rolling out

---

---
## 🔗 Go deeper: expansion notes
- [[206 Non-Parametric Tests|Non-Parametric Tests]]
- [[205 Sampling Distributions & Estimation|Sampling Distributions & Estimation]]
- [[214 Causal Inference & Experimentation Beyond A-B Tests|Causal Inference & Experimentation Beyond A-B Tests]]
