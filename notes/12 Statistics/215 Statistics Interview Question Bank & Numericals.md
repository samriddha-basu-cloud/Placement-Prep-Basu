---
tags: [statistics, tier1]
area: Statistics
topic: "Statistics Interview Question Bank & Numericals"
tier: Tier 1
roles: All roles
status: complete
subtopics: 14
---
# Statistics Interview Question Bank & Numericals

⬅ [[214 Causal Inference & Experimentation Beyond A-B Tests]] · [[_Index - Statistics|Statistics]] · [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** All roles

## Sub-topics in this note
1. [[#1. How to Use This Bank: Answer Structure and Numerical Protocol]]
2. [[#2. Descriptive Statistics: Questions and Numericals]]
3. [[#3. Probability and Bayes: Questions and Numericals]]
4. [[#4. Distributions: Questions and Numericals]]
5. [[#5. Sampling, CLT and Confidence Intervals]]
6. [[#6. Hypothesis Testing and p-values: Questions and Numericals]]
7. [[#7. Chi-Square, ANOVA and Non-Parametric Questions]]
8. [[#8. Regression and Correlation: Questions and Numericals]]
9. [[#9. Quality and SPC: Questions and Numericals]]
10. [[#10. Experimentation and Sampling Design Questions]]
11. [[#11. Brain-Teasers with Short Solutions]]
12. [[#12. Explain It to a Non-Technical Manager]]
13. [[#13. Common Misconceptions Table]]
14. [[#14. ⭐ Advanced: Which-Test Decision Table and Rapid-Fire Formulas]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): regulators and benchmarks now demand statistical rigour in the open
> **FDA draft guidance on Bayesian methodology (9 Jan 2026; Federal Register notice 12 Jan 2026).** The US FDA set out how Bayesian methods can support regulatory decisions in clinical trials, including interim adaptations, dose selection and end-of-trial conclusions, across INDs, NDAs and BLAs. Interviewers increasingly ask both the classical (p-value, confidence interval) and the Bayesian (prior, posterior, credible interval) reading of the same result, so know both. ([Alston and Bird summary](https://www.alston.com/en/insights/publications/2026/01/fda-bayesian-guidance-drug-trials); [Federal Register notice](https://www.federalregister.gov/documents/2026/01/12/2026-00325/use-of-bayesian-methodology-in-clinical-trials-of-drug-and-biological-products-draft-guidance-for))
>
> **fev-bench for forecasting models (arXiv, 2025).** A benchmark of 100 forecasting tasks across seven domains (46 with covariates) was built because earlier benchmarks lacked statistical rigour: it reports win rates and skill scores with bootstrapped confidence intervals so that readers can tell real improvement from random variation. This is the "is the difference more than noise?" question at the centre of every statistics interview. ([arXiv 2509.26468](https://arxiv.org/abs/2509.26468))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. How to Use This Bank: Answer Structure and Numerical Protocol
> 🔴 Tier 1 · _Key points:_ Definition, intuition, example, caveat; set up, compute, interpret in words

### Definition
This note holds **64 conceptual questions (Q1 to Q64)** with model answers, **21 worked numericals (N1 to N21)**, brain-teasers, manager-friendly explanations and a misconceptions table. Each topic section links to the teaching note to revise first: [[086 Descriptive Statistics]], [[087 Probability Fundamentals]], [[088 Probability Distributions]], [[089 Hypothesis Testing]], [[090 Regression Analysis]], [[091 Statistical Quality Control (SQC)]], [[092 Sampling & Experimental Design]], [[093 Business Statistics Applications]], and the extension notes [[205 Sampling Distributions & Estimation]], [[206 Non-Parametric Tests]], [[209 Generalised Linear Models & Categorical Data Analysis]], [[210 Bayesian Statistics for Decisions]].

**Conceptual answer structure (30 to 60 seconds):** (1) one-line definition, (2) the intuition or formula, (3) a business example, (4) the common trap or assumption. Stop; let the interviewer probe.

**Numerical protocol (say it aloud):**
1. Name the quantity and the method ("one-sample t-test for a mean, σ unknown").
2. Write the formula and identify every symbol from the data.
3. Compute with units; keep 3 to 4 significant figures.
4. Compare with the critical value or give the p-value.
5. **Interpret in one business sentence**, with the decision and a caveat.

Table of standard critical values to memorise: $z_{0.95}=1.645$ (one-tail 5%), $z_{0.975}=1.96$, $z_{0.995}=2.576$; $t_{0.975,10}=2.228$, $t_{0.975,30}=2.042$, $t_{0.975,100}=1.984$.

### Example
Asked "A sample of 36 has mean 52 and SD 9; give a 95% CI", a strong spoken answer: "Unknown σ, n = 36, so a t interval with 35 df. Standard error is 9/√36 = 1.5, t critical 2.03, margin 3.05, so (48.95, 55.05). We are 95% confident, by this procedure, that the true mean lies there; the interval does not say 95% of observations fall in it." That is N8 below.

### In the news
See news box. Both items reward candidates who state uncertainty (interval, error rate) next to every number.

### Interview angle
> [!question] How it is asked
> "Walk me through your statistics background and one analysis where it changed a decision."

> [!tip] Strong answer includes
> - A real example with a decision, a test or model, and the size of the effect
> - Naming assumptions and how they were checked
> - Plain-language interpretation first, jargon second
> - Practice habit: do the numericals below aloud with a timer

---
## 2. Descriptive Statistics: Questions and Numericals
> 🔴 Tier 1 · _Key points:_ Mean vs median, n-1, SD vs SE, outliers, CV

### Definition
**Q1. When do you use mean, median or mode?** Mean for symmetric data and when totals matter (cost per unit); median for skewed data (salaries, lead times, order values) because it resists outliers; mode for categorical data or most common size/SKU.

**Q2. Why divide by n − 1 for sample variance?** The sample mean is fitted from the same data, so deviations around it are slightly too small; dividing by $n-1$ (Bessel's correction) makes $s^2$ an unbiased estimator of $\sigma^2$. Equivalent statement: only $n-1$ deviations are free (degrees of freedom).

**Q3. Standard deviation vs standard error?** SD describes spread of individual observations; SE $=s/\sqrt n$ describes how much a **sample statistic** (the mean) would vary across repeated samples. SE shrinks with $n$; SD does not.

**Q4. A distribution is right-skewed. Where do mean and median sit?** Mean above median (the tail pulls the mean); report median and IQR; consider a log transform.

**Q5. How do you detect and treat outliers?** Rule: outside $Q_1-1.5\,IQR$ or $Q_3+1.5\,IQR$, or $|z|>3$. Investigate cause (data error, real extreme, different population) before any action; options are correct, keep with a robust method, winsorise, or analyse with and without. Never delete silently.

**Q6. What is the coefficient of variation and when is it useful?** $CV=s/\bar x$; unit-free, so it compares variability across different units or scales (₹ price vs kg weight; two suppliers with different mean lead times).

**Q7. What do percentiles, quartiles and a boxplot show?** Position within the distribution; the box spans $Q_1$ to $Q_3$ (IQR), the line is the median, whiskers extend to the last point within 1.5 IQR, dots beyond are potential outliers. Good for comparing groups side by side.

### Example
**N1.** Lead times (days) for 8 orders: 4, 6, 6, 7, 9, 10, 12, 18. Mean $=72/8=9$. Median $=(7+9)/2=8$. Mode = 6. Sample variance $=\frac{\sum(x-9)^2}{7}=\frac{138}{7}=19.71$, SD $=4.44$, $CV=4.44/9=49.3\%$. $Q_1=6$, $Q_3=10.5$ (linear interpolation, the Excel `QUARTILE.INC` rule), IQR = 4.5; upper fence $10.5+1.5(4.5)=17.25$, so **18 is an outlier**. Mean (9) above median (8) confirms right skew.

**N2.** Purchases: 500 kg at ₹40, 300 kg at ₹44, 200 kg at ₹52. Weighted mean price $=\frac{20{,}000+13{,}200+10{,}400}{1{,}000}=\mathbf{₹43.60}$ (a simple average would wrongly give ₹45.33). A truck drives 60 km/h out and 40 km/h back: average speed is the harmonic mean $\frac{2}{1/60+1/40}=\mathbf{48}$ km/h, not 50.

```python
import numpy as np
x = np.array([4,6,6,7,9,10,12,18])
print(x.mean(), np.median(x), x.std(ddof=1), np.percentile(x, [25, 75]))   # 9.0 8.0 4.44 [ 6. 10.5]
```

### In the news
See news box. Reporting a mean without its spread or interval is the most common error benchmarks such as fev-bench were designed to avoid.

### Interview angle
> [!question] How it is asked
> "Average delivery time is 3 days but customers complain. What might be going on?"

> [!tip] Strong answer includes
> - Mean hides the tail: check median, 90th/95th percentile and SD
> - Segment by route, supplier, day of week (mix effects)
> - Percentile-based service KPIs, not averages alone
> - Mentions skew and outliers with a rule for each

---
## 3. Probability and Bayes: Questions and Numericals
> 🔴 Tier 1 · _Key points:_ Independence, conditional, Bayes, base rates, Simpson's paradox, Bayesian vs frequentist

### Definition
**Q8. Independent vs mutually exclusive events?** Independent: $P(A\cap B)=P(A)P(B)$; knowing one tells nothing about the other. Mutually exclusive: $P(A\cap B)=0$. Two events with positive probabilities cannot be both; mutually exclusive events are strongly dependent.

**Q9. State Bayes' theorem and say what each term means.** $P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$: posterior = likelihood × prior / evidence. See [[087 Probability Fundamentals]].

**Q10. What is the base-rate fallacy?** Ignoring prevalence when interpreting a positive result. A 90%-sensitive test for a 1% condition with 9% false positives has $P(D\mid+)\approx9.2\%$ (worked in [[217 Probability Puzzles & Applied Problem Solving]]).

**Q11. State the law of total probability.** $P(B)=\sum_i P(B\mid A_i)P(A_i)$ for a partition $A_i$; used as the denominator of Bayes.

**Q12. Properties of expectation and variance?** $E[aX+b]=aE[X]+b$; $Var(aX+b)=a^2Var(X)$; $E[X+Y]=E[X]+E[Y]$ always; $Var(X+Y)=Var(X)+Var(Y)$ only if uncorrelated.

**Q13. Gambler's fallacy?** After 9 heads in a row, the next toss is still 50-50 for a fair coin; independent trials have no memory. The opposite error (hot-hand) assumes streaks persist.

**Q14. Frequentist vs Bayesian?** Frequentist: probability is long-run frequency; parameters are fixed; inference via p-values and CIs. Bayesian: probability expresses belief; parameters have distributions; prior × likelihood gives posterior and **credible intervals**. See [[210 Bayesian Statistics for Decisions]].

**Q15. Credible interval vs confidence interval?** A 95% credible interval says "given data and prior, there is a 95% probability the parameter is in here". A 95% CI says the **procedure** captures the true value in 95% of repeated samples; any single interval either contains it or does not.

**Q16. What is Simpson's paradox?** A trend in each subgroup reverses when groups are pooled. Kidney-stone data: treatment A succeeds 93.1% (81/87) on small stones and 73.0% (192/263) on large; B succeeds 86.7% (234/270) and 68.8% (55/80). A wins in both groups, yet overall A is 78.0% (273/350) vs B 82.6% (289/350), because A was given more of the hard (large-stone) cases. Fix: stratify or adjust for the confounder.

**Q17. What is conditional independence and why does it matter in naive Bayes?** Naive Bayes assumes features are independent given the class; it often works despite violations because only the ranking of class probabilities matters ([[096 Classification Algorithms]]).

### Example
**N3 (Bayes).** Machine A makes 60% of output with 2% defective; machine B makes 40% with 5% defective. $P(\text{defect})=0.6(0.02)+0.4(0.05)=0.012+0.020=\mathbf{0.032}$. A randomly chosen defective part came from A with probability $\frac{0.012}{0.032}=\mathbf{37.5\%}$, from B $62.5\%$: B is the main source despite lower volume.

**N4 (independence).** $P(A)=0.5$, $P(B)=0.4$, $P(A\cup B)=0.7$. Then $P(A\cap B)=0.5+0.4-0.7=0.2=0.5\times0.4$, so **A and B are independent**.

**N20 (Bayesian update).** Prior for a conversion rate: Beta(2, 8) (mean 0.20). Data: 18 conversions in 100 visitors. Posterior = Beta(2+18, 8+82) = **Beta(20, 90)**, mean $20/110=0.182$, 95% credible interval **(0.116, 0.259)**. The data pulled the mean from 0.20 to 0.182; with more data the prior fades.

```python
from scipy import stats
print(stats.beta.ppf([0.025, 0.975], 20, 90))    # [0.1158 0.2587]
```

### In the news
See news box. The FDA guidance is the formal version of N20: a prior, data, a posterior and a decision rule.

### Interview angle
> [!question] How it is asked
> "A fraud model flags a transaction. Fraud prevalence is 0.5%. How worried should you be?"

> [!tip] Strong answer includes
> - Ask for prevalence, sensitivity, false-positive rate; apply Bayes
> - Natural frequencies ("out of 10,000 transactions...")
> - Business translation: alert precision, review cost, threshold choice
> - Contrast frequentist and Bayesian readings if asked

---
## 4. Distributions: Questions and Numericals
> 🔴 Tier 1 · _Key points:_ Normal, binomial, Poisson, exponential, t; z-scores; safety stock

### Definition
**Q18. Properties of the normal distribution?** Symmetric bell; mean = median = mode; 68%, 95%, 99.7% within 1, 2, 3 SD; $z=(x-\mu)/\sigma$. Sums of independent normals are normal.

**Q19. Binomial vs Poisson?** Binomial: number of successes in $n$ fixed independent trials with probability $p$; mean $np$, variance $np(1-p)$. Poisson: count of events in an interval at rate $\lambda$; mean = variance = $\lambda$. Poisson approximates binomial when $n$ is large and $p$ small ($n=1000$, $p=0.002$: exact $P(3)=0.1806$, Poisson(2) gives $0.1804$).

**Q20. What is special about the exponential distribution?** Time between Poisson events; **memoryless**: $P(T>s+t\mid T>s)=P(T>t)$; mean $1/\lambda$. Used for arrivals and failure times ([[149 Queueing Theory & Waiting-Line Analysis]], [[211 Reliability & Survival Analysis]]).

**Q21. When do you use t rather than z?** Mean inference with unknown $\sigma$ estimated by $s$; t has heavier tails (df = n − 1) and converges to z as $n$ grows (critical 2.042 at 30 df vs 1.96).

**Q22. Why does the normal appear everywhere?** Central limit theorem: sums and averages of many independent small effects are approximately normal.

**Q23. Which distribution would you use for (a) defects per metre, (b) number of defective units in a batch of 50, (c) time until next machine failure, (d) order values?** (a) Poisson, (b) binomial (or hypergeometric if sampling without replacement from a small lot), (c) exponential or Weibull, (d) often log-normal (right-skewed, positive).

**Q24. What is a z-score and what is it used for?** Number of SDs from the mean; compares values on different scales, flags outliers ($|z|>3$), and converts a service level into safety-stock factor ($z=1.645$ for 95%).

### Example
**N5 (normal).** Fill weight $\sim N(500,\,4^2)$ g. (a) $P(X<492)=P(Z<-2)=\mathbf{2.28\%}$. (b) $P(494<X<506)=P(-1.5<Z<1.5)=\mathbf{86.64\%}$. (c) 95th percentile $=500+1.645\times4=\mathbf{506.58}$ g. (d) Safety stock: daily demand SD 20 units, lead time 4 days, service level 95%: $1.645\times20\times\sqrt4=\mathbf{65.8\approx66}$ units ([[003 Inventory Management]]).

**N6 (binomial).** 10 items, defect rate 5%. $P(X=1)=10(0.05)(0.95)^9=\mathbf{0.3151}$; $P(X\ge2)=1-P(0)-P(1)=1-0.5987-0.3151=\mathbf{0.0861}$; mean 0.5, SD 0.689.

**N7 (Poisson).** Calls arrive at 4 per hour. $P(0\text{ in 30 min})=e^{-2}=\mathbf{0.1353}$. $P(\ge8\text{ in an hour})=1-P(X\le7)=\mathbf{0.0511}$.

```python
from scipy import stats
print(stats.norm.cdf(-2), stats.binom.pmf(1, 10, .05), stats.poisson.sf(7, 4))   # 0.0228 0.3151 0.0511
```

### In the news
See news box. Probabilistic forecasts (quantiles of a predictive distribution) are replacing single-number forecasts; this section's distributions are what they summarise.

### Interview angle
> [!question] How it is asked
> "Demand is roughly normal, mean 200, SD 30, lead time 4 days. How much stock for 98% service?"

> [!tip] Strong answer includes
> - Convert to lead-time demand (mean 800, SD $30\sqrt4=60$)
> - $z_{0.98}=2.054$, so safety stock $=123$, reorder point about 923
> - Mention normality assumption and fat-tailed alternatives
> - Link to cycle service level vs fill rate

---
## 5. Sampling, CLT and Confidence Intervals
> 🔴 Tier 1 · _Key points:_ CLT, standard error, interpreting CI, margin of error, sampling bias, bootstrap

### Definition
**Q25. State the central limit theorem.** For independent observations with finite variance, the sampling distribution of $\bar X$ approaches $N(\mu,\sigma^2/n)$ as $n$ grows, whatever the shape of the population; $n\ge30$ is a rough guide, more for heavy skew. See [[205 Sampling Distributions & Estimation]].

**Q26. What is the standard error of the mean and how do you halve it?** $SE=\sigma/\sqrt n$; to halve it, **quadruple** the sample size.

**Q27. How do you interpret a 95% CI correctly?** If we repeated the sampling and building of intervals many times, about 95% would contain the true parameter. For one interval, we say "we are 95% confident"; it is not a probability statement about this interval, nor a range containing 95% of the data.

**Q28. What makes a CI narrower?** Larger $n$, lower variability, lower confidence level (90% is narrower than 99%). Margin $=t^*\,s/\sqrt n$.

**Q29. Name four sampling methods and a bias for each.** Simple random (needs a frame), stratified (reduces variance; proportional allocation), cluster (cheaper but higher variance; design effect), systematic (periodicity risk). Non-probability (convenience, quota) cannot give valid CIs. See [[092 Sampling & Experimental Design]].

**Q30. What is selection or survivorship bias?** The sample systematically excludes part of the population: surveying only current customers ignores those who left; reviewing only successful projects overstates success. Fix with the right sampling frame and by tracing non-responders.

**Q31. What is the bootstrap?** Resample the data with replacement many times, compute the statistic each time, and use the spread (percentiles) as an interval; useful for medians, ratios and when formulas are messy.

### Example
**N8 (CI for a mean).** $n=36$, $\bar x=52$, $s=9$: $SE=9/6=1.5$; $t_{0.975,35}=2.030$; margin $=3.045$; 95% CI **(48.95, 55.05)**.

**N9 (sample size).** Proportion with margin ±3% at 95% (worst case $p=0.5$): $n=\frac{1.96^2(0.25)}{0.03^2}=1{,}067.1\Rightarrow\mathbf{1{,}068}$. Mean with $\sigma=15$, margin $E=3$: $n=(1.96\times15/3)^2=96.04\Rightarrow\mathbf{97}$. A survey of India's 1.4 billion people needs about the same n as one of a city, because $n$ depends on precision, not population size (unless the sample is a large fraction of a small population).

```python
from scipy import stats
print(stats.t.interval(0.95, 35, loc=52, scale=9/6))     # (48.95, 55.05)
```

### In the news
See news box. Bootstrapped intervals are exactly how fev-bench reports forecast-model rankings.

### Interview angle
> [!question] How it is asked
> "Why is a poll of 1,000 enough for a country of a billion?"

> [!tip] Strong answer includes
> - Precision depends on $n$ via $1/\sqrt n$, not on population size
> - Margin of error about ±3% at 95%
> - Condition: random sample, not a biased frame (non-response matters more than size)
> - Cluster or stratified designs change the effective sample size

---
## 6. Hypothesis Testing and p-values: Questions and Numericals
> 🔴 Tier 1 · _Key points:_ Errors, power, p-value, practical vs statistical significance, multiple testing, one-tailed

### Definition
**Q32. Explain H0 and H1 with a business example.** H0 is the status quo (new packaging does not change mean sales); H1 is what you want evidence for. We never "prove" H0; we fail to reject it.

**Q33. Type I and Type II errors?** Type I ($\alpha$): reject a true H0 (false alarm, launching a useless feature). Type II ($\beta$): fail to reject a false H0 (missing a real improvement). Power $=1-\beta$. Lowering $\alpha$ raises $\beta$ for fixed $n$.

**Q34. What is a p-value?** The probability, computed assuming H0 is true, of a test statistic at least as extreme as observed. It is not the probability H0 is true.

**Q35. How can you increase power?** Larger $n$, larger effect, larger $\alpha$, lower variance (blocking, paired design, covariate adjustment).

**Q36. Statistical vs practical significance?** With huge $n$, tiny effects are "significant"; always report effect size and CI. A 0.05-point lift in conversion may be significant yet worth nothing.

**Q37. One-tailed or two-tailed?** One-tailed only when a difference in the other direction is impossible or irrelevant and this was decided before seeing data; otherwise two-tailed. Switching after the data is p-hacking.

**Q38. What is the multiple-testing problem and how do you handle it?** With $m$ independent tests at 5%, $P(\text{at least one false positive})=1-0.95^m$; for 20 tests, **64.2%**. Use Bonferroni ($\alpha/m$, so 0.0025 for 20), Holm, or control the false discovery rate (Benjamini-Hochberg).

**Q39. z-test vs t-test vs proportion test?** z: mean with known $\sigma$ or very large $n$; t: mean with estimated $s$; z for proportions with $np$ and $n(1-p)$ at least 10.

**Q40. What is wrong with stopping an A/B test as soon as p < 0.05?** Repeated peeking inflates the false-positive rate well above 5%. Fix the sample size in advance or use sequential methods (alpha spending, always-valid p-values, Bayesian monitoring).

### Example
**N10 (z-test).** Claimed mean 250 g, $\sigma=12$, $n=49$, $\bar x=253.5$. $z=\frac{3.5}{12/7}=\mathbf{2.04}$; two-sided $p=\mathbf{0.0412}$; reject H0 at 5%: the mean differs from 250 g (about 3.5 g heavy; 95% CI 250.1 to 256.9).

**N11 (t-test).** $n=16$, $\bar x=18.2$, $s=2.4$, H0: $\mu=17$. $t=\frac{1.2}{2.4/4}=\mathbf{2.00}$, df 15, critical $\pm2.131$, $p=\mathbf{0.064}$: **fail to reject** at 5% (not "no difference"; the evidence is suggestive and the test may be underpowered).

**N12 (two proportions).** Defect rates 120/1,000 (12%) vs 150/1,000 (15%). Pooled $\hat p=0.135$; $SE=\sqrt{0.135\times0.865\times\frac{2}{1000}}=0.01528$; $z=0.03/0.01528=\mathbf{1.96}$; $p=\mathbf{0.0496}$. Borderline: significant at 5% by a hair; report the interval (difference 3 points, 95% CI about 0.0 to 6.0 points) and the cost of acting.

```python
from scipy import stats
print(2*(1-stats.norm.cdf(2.0417)), 2*stats.t.sf(2.0, 15))   # 0.0412 0.0639
```

### In the news
See news box. The FDA guidance reflects the same discussion about how much evidence is enough; classical error control remains the baseline.

### Interview angle
> [!question] How it is asked
> "p = 0.03. Does that mean there is a 97% chance our change works?"

> [!tip] Strong answer includes
> - No: it is P(data this extreme | H0), not P(effect is real)
> - Report effect size and CI; mention power and prior plausibility
> - Multiple tests and peeking inflate false positives
> - Decision framed by cost of Type I vs Type II errors

---
## 7. Chi-Square, ANOVA and Non-Parametric Questions
> 🔴 Tier 1 · _Key points:_ Independence test, expected counts, why ANOVA, post-hoc, rank tests

### Definition
**Q41. What does a chi-square test of independence do?** Compares observed counts with those expected if two categorical variables were independent: $\chi^2=\sum\frac{(O-E)^2}{E}$, $df=(r-1)(c-1)$. Expected counts should be at least 5 (else Fisher's exact test). See [[209 Generalised Linear Models & Categorical Data Analysis]].

**Q42. Why use ANOVA instead of several t-tests?** Three t-tests at 5% give a family-wise error of $1-0.95^3=14.3\%$. ANOVA tests all means at once with $F=MS_{between}/MS_{within}$.

**Q43. ANOVA is significant. What next?** It only says at least one mean differs; use Tukey HSD (or Bonferroni) for pairwise differences; report effect size $\eta^2=SS_B/SS_T$. Check equal variances and residual normality.

**Q44. When do you prefer non-parametric tests?** Small samples with non-normal data, ordinal data, or heavy outliers: Mann-Whitney (instead of independent t), Wilcoxon signed-rank (paired), Kruskal-Wallis (ANOVA), Spearman (correlation). Cost: some power when normality actually holds. See [[206 Non-Parametric Tests]].

**Q45. How do you check normality, and does it always matter?** Q-Q plot, Shapiro-Wilk. For means, the CLT makes the t-test robust with moderate $n$; strong skew and small $n$ are the problem. Normality is an assumption about residuals/the sampling distribution, not about raw data per se.

### Example
**N13 (chi-square).** Complaint (yes/no) by shift: Day 40 yes, 60 no; Night 30 yes, 70 no. Expected under independence: 35 yes and 65 no in each row. $\chi^2=\frac{(40-35)^2}{35}+\frac{(60-65)^2}{65}+\frac{(30-35)^2}{35}+\frac{(70-65)^2}{65}=0.714+0.385+0.714+0.385=\mathbf{2.20}$; $df=1$; critical value 3.84; $p=\mathbf{0.138}$. **Not significant**: no evidence the complaint rate differs by shift.

**N14 (ANOVA from summary).** Three groups of 5; means 20, 24, 28; pooled within-group variance $MS_W=16$. Grand mean 24, $SS_B=5(16+0+16)=160$, $MS_B=160/2=80$; $F=80/16=\mathbf{5.0}$ on (2, 12) df; critical 3.885; $p=\mathbf{0.026}$: reject; at least one mean differs.

```python
from scipy import stats
print(stats.chi2_contingency([[40,60],[30,70]], correction=False)[:2])   # (2.198, 0.138)
print(stats.f.sf(5.0, 2, 12))                                            # 0.0263
```

### In the news
See news box. Comparing many models or groups needs multiple-comparison control, the point of Q42 and Q38.

### Interview angle
> [!question] How it is asked
> "Three plants, one quality metric. How do you decide if they differ?"

> [!tip] Strong answer includes
> - ANOVA after plotting; assumptions (independence, similar variances, residuals)
> - Tukey for which pairs; effect size
> - Non-parametric fallback (Kruskal-Wallis) if assumptions fail
> - Practical significance and cost, not only p

---
## 8. Regression and Correlation: Questions and Numericals
> 🔴 Tier 1 · _Key points:_ Slope meaning, R-squared, assumptions, multicollinearity, causation, extrapolation

### Definition
**Q46. How do you interpret a regression slope?** Expected change in $y$ for a one-unit increase in $x$, holding other predictors fixed; the intercept is $y$ at $x=0$ (often not meaningful). State units.

**Q47. R² vs adjusted R²?** $R^2$ is the fraction of variance explained and never falls when variables are added; adjusted $R^2$ penalises extra predictors. A high $R^2$ does not mean a correct model (check residuals; beware overfitting).

**Q48. List the linear regression assumptions.** Linearity, independence of errors, constant variance (homoscedasticity), normal residuals (for small-sample inference), no perfect multicollinearity. Diagnose with residual plots, Q-Q plot, Durbin-Watson, VIF. See [[090 Regression Analysis]].

**Q49. What is multicollinearity and why is it a problem?** Predictors strongly correlated with each other; coefficients become unstable with inflated standard errors (VIF above 5 to 10), though predictions may stay fine. Remedy: drop or combine variables, regularise (ridge), use PCA ([[207 Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis]]).

**Q50. Correlation vs causation?** Correlation measures linear association; causation needs a design (randomisation) or assumptions (see [[214 Causal Inference & Experimentation Beyond A-B Tests]]). Confounders, reverse causality and coincidence all produce correlation (ice-cream sales and drownings share a hot-weather driver).

**Q51. What is overfitting?** A model captures noise: excellent training fit, poor out-of-sample accuracy. Prevent with a train/test split, cross-validation, simpler models, regularisation ([[098 Model Selection & Optimization]]).

**Q52. What is heteroscedasticity and what do you do?** Residual variance changes with the level of $x$ (a funnel); standard errors are biased. Use robust (White) standard errors, a log transform or weighted least squares.

**Q53. Linear vs logistic regression?** Linear for a continuous outcome; logistic for a binary outcome, modelling log-odds $\ln\frac{p}{1-p}$; coefficients are log-odds ratios, so $e^{\beta}$ is an odds ratio ([[096 Classification Algorithms]]). Also mention **regression to the mean**: extreme values tend to be followed by less extreme ones with no intervention, a classic false-effect trap.

### Example
**N15 (fit a line).** Advertising spend $x$ (₹ lakh) 1, 2, 3, 4, 5 and sales $y$ (₹ lakh) 2.1, 3.9, 6.2, 7.8, 10.0. $\bar x=3$, $\bar y=6$; $S_{xy}=19.7$, $S_{xx}=10$. Slope $b=19.7/10=\mathbf{1.97}$; intercept $a=6-1.97\times3=\mathbf{0.09}$; $\hat y=0.09+1.97x$. Correlation $r=0.9988$, $R^2=\mathbf{0.9977}$. Residuals 0.04, −0.13, 0.20, −0.17, 0.06; $SSE=0.091$; $s=\sqrt{0.091/3}=0.174$; $SE(b)=0.174/\sqrt{10}=0.0551$; $t=1.97/0.0551=35.8$ (df 3), $p<0.001$.

**N16 (prediction).** At $x=3$: $\hat y=6.0$ (the line passes through $(\bar x,\bar y)$). At $x=6$: $\hat y=0.09+11.82=\mathbf{11.91}$, but 6 is **outside the observed range 1 to 5**, so it is an extrapolation and should be flagged. Interpretation: each extra ₹1 lakh of advertising is associated with about ₹1.97 lakh of extra sales in this range (association, not proof of causation).

```python
import numpy as np
x = np.array([1,2,3,4,5]); y = np.array([2.1,3.9,6.2,7.8,10.0])
b, a = np.polyfit(x, y, 1); print(b, a, np.corrcoef(x, y)[0, 1]**2)   # 1.97 0.09 0.9977
```

### In the news
See news box. Regression with calendar, price and promotion covariates underlies the forecasting benchmarks discussed in [[218 Forecasting with ML & Foundation Models]].

### Interview angle
> [!question] How it is asked
> "Your model has R² = 0.95. Is it a good model?"

> [!tip] Strong answer includes
> - Not necessarily: check out-of-sample error, residual patterns, overfitting
> - R² depends on the variance of y; compare with a baseline model
> - Interpretability, stability of coefficients, VIF
> - Business usefulness: error in ₹ or units

---
## 9. Quality and SPC: Questions and Numericals
> 🔴 Tier 1 · _Key points:_ Common vs special cause, control vs spec limits, Cp vs Cpk, sigma level, chart choice

### Definition
**Q54. Common-cause vs special-cause variation?** Common: inherent random variation of a stable process; special: assignable, unusual events. Control charts signal special causes; reducing common-cause variation needs process redesign (Deming). See [[091 Statistical Quality Control (SQC)]].

**Q55. Control limits vs specification limits?** Control limits ($\bar X\pm3\sigma$ of the plotted statistic) come from the process (voice of the process); specification limits come from the customer (voice of the customer). They are unrelated; a stable process can still be out of spec.

**Q56. Cp vs Cpk?** $C_p=\frac{USL-LSL}{6\sigma}$ is potential capability if centred; $C_{pk}=\min\left(\frac{USL-\mu}{3\sigma},\frac{\mu-LSL}{3\sigma}\right)$ accounts for centring. $C_{pk}\le C_p$, with equality when centred. Typical target 1.33.

**Q57. What does six sigma mean quantitatively?** 3.4 defects per million opportunities, assuming the conventional 1.5σ long-term shift of the mean; without the shift, six-sigma capability is about 2 parts per billion. See [[008 Six Sigma & Quality Tools]].

**Q58. Which chart for which data?** Variables: X-bar/R (subgroups of 2 to 10), X-bar/S (larger subgroups), I-MR (individual values). Attributes: p or np (fraction/number defective), c or u (defects per unit). The p-chart handles variable sample sizes.

**Q59. What are producer's and consumer's risk in acceptance sampling?** Producer's risk $\alpha$: rejecting a good lot (at AQL); consumer's risk $\beta$: accepting a bad lot (at LTPD). The OC curve shows the acceptance probability by quality level ([[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]]).

### Example
**N17 (X-bar and R limits).** Subgroups of $n=4$; $\bar{\bar X}=100$, $\bar R=6$. Factors for $n=4$: $A_2=0.729$, $D_3=0$, $D_4=2.282$. X-bar chart: $100\pm0.729\times6=\mathbf{104.37}$ and $\mathbf{95.63}$. R chart: UCL $=2.282\times6=\mathbf{13.69}$, LCL $=0$.

**N18 (capability).** Specification 9.95 to 10.10 mm; process mean 10.02, $\sigma=0.02$. $C_p=\frac{0.15}{0.12}=\mathbf{1.25}$; $C_{pk}=\min\left(\frac{0.08}{0.06},\frac{0.07}{0.06}\right)=\min(1.333,\,1.167)=\mathbf{1.167}$ (limited by the lower side: the mean is closer to LSL). Fraction out of spec: below LSL $z=-3.5$ gives 232.6 ppm; above USL $z=+4.0$ gives 31.7 ppm; total about **264 ppm**. Re-centring at 10.025 would raise $C_{pk}$ to 1.25.

**N21 (p-chart).** $n=200$ per sample, $\bar p=0.04$: $\sigma_p=\sqrt{0.04\times0.96/200}=0.01386$; $UCL=0.04+3(0.01386)=\mathbf{0.0816}$; $LCL=0.04-0.0416<0$, so **LCL = 0**.

```python
from scipy import stats
print(stats.norm.cdf(-3.5)*1e6 + stats.norm.sf(4)*1e6)   # ~264 ppm
```

### In the news
See news box. Control-chart thinking carries over to monitoring model error and data drift in production ([[220 Responsible AI, Explainability & Model Governance]]).

### Interview angle
> [!question] How it is asked
> "A process is in control but customers are unhappy. How is that possible?"

> [!tip] Strong answer includes
> - In control means stable, not capable of meeting specification
> - Compute Cp and Cpk, check centring
> - Reduce variation (common cause) or re-centre; do not tamper with a stable process
> - Add measurement-system check (Gauge R&R)

---
## 10. Experimentation and Sampling Design Questions
> 🔴 Tier 1 · _Key points:_ A/B test design, randomisation, blocking, sample size, SRM, factorial designs

### Definition
**Q60. How do you design an A/B test?** Define one primary metric and guardrails, a minimum detectable effect, $\alpha$ and power; compute sample size; randomise at the right unit (user, not session); run for whole weekly cycles; check balance and sample-ratio mismatch; analyse once at the planned end.

**Q61. Why randomise, and what is blocking?** Randomisation balances known and unknown confounders on average, supporting causal claims. Blocking (stratifying) groups similar units (store size, region) to remove their variation from the comparison and raise power.

**Q62. What is sample-ratio mismatch?** A 50/50 split that yields, say, 50.8/49.2 with large $n$ signals a bug in assignment or logging; results from such a test are untrustworthy until explained.

**Q63. What are novelty effects, interference and network effects?** Users react to something new then revert; in marketplaces and social products treatment spills over to controls, biasing estimates; use cluster or geo-randomisation, switchbacks. See [[214 Causal Inference & Experimentation Beyond A-B Tests]].

**Q64. Factorial design vs one-factor-at-a-time?** Factorial varies all factors together, estimating main effects and interactions from fewer runs; OFAT misses interactions. See [[213 Design of Experiments - Factorial, Fractional & Taguchi]] and [[092 Sampling & Experimental Design]].

### Example
**N19 (A/B sample size).** Baseline conversion 4.0%; want to detect 4.8% (a 20% relative lift) with $\alpha=0.05$ two-sided and 80% power:
$$n=\frac{\left(z_{\alpha/2}\sqrt{2\bar p(1-\bar p)}+z_{\beta}\sqrt{p_1(1-p_1)+p_2(1-p_2)}\right)^2}{(p_2-p_1)^2},\quad \bar p=0.044$$
$n=\mathbf{10{,}317}$ per arm, so about **20,600 users in total**. Halving the detectable lift to 0.4 points needs about 4 times as many (n scales with $1/\delta^2$). At 5,000 visitors a day split evenly, the test needs about 4.1 days of traffic at minimum; round up to a full week (7 days) to cover weekly seasonality.

```python
from math import sqrt
from scipy.stats import norm
p1, p2 = .04, .048; pb = (p1+p2)/2; za, zb = norm.ppf(.975), norm.ppf(.8)
n = (za*sqrt(2*pb*(1-pb)) + zb*sqrt(p1*(1-p1)+p2*(1-p2)))**2 / (p2-p1)**2
print(round(n))    # 10316 (10,317 after rounding up)
```

### In the news
See news box. Bootstrapped intervals and pre-specified evaluation protocols in benchmarks echo good A/B practice: fix the analysis plan before looking.

### Interview angle
> [!question] How it is asked
> "Design an experiment to test a new checkout flow."

> [!tip] Strong answer includes
> - Hypothesis, primary metric, guardrails, unit of randomisation
> - Sample size and duration with MDE, alpha, power
> - Validity checks (SRM, A/A test), no peeking
> - Decision rule including cost and the practical size of lift

---
## 11. Brain-Teasers with Short Solutions
> 🔴 Tier 1 · _Key points:_ Give the answer, the reasoning and a simulation; full treatment in the puzzles note

### Definition
Five that appear repeatedly; each is solved and simulated in [[217 Probability Puzzles & Applied Problem Solving]].

**B1. Monty Hall:** switching wins 2/3 because the host's reveal carries information (his first pick was right with 1/3).
**B2. Birthday:** 23 people give a 50.7% chance of a shared birthday (253 pairs); 50 people 97%.
**B3. Two children, at least one boy:** P(both boys) = 1/3, but if "the older is a boy" it is 1/2.
**B4. Lost boarding pass:** 100 passengers; the first sits in a random seat, others take their own seat if free, else a random free one. P(last passenger gets own seat) = **1/2** (simulation 0.499).
**B5. Ants on a triangle:** three ants start on the three corners and each picks a direction at random; P(at least one collision) = $1-2/2^3=\mathbf{3/4}$ (simulation 0.751).
Pigeonhole bonus: a drawer has black and white socks; 3 socks guarantee a matching pair.

### Example
Spoken solution for B4: "By symmetry, the process comes down to whether seat 1 or seat 100 is taken first by a displaced passenger; each is equally likely, so 1/2. For n = 2 it is trivially 1/2, and a simulation of 100 passengers over 40,000 runs gave 0.499." Show the structure: small case, symmetry, simulation.

```python
import numpy as np
rng = np.random.default_rng(3)
d = rng.integers(0, 2, (200000, 3))
print(1 - np.mean((d.sum(1) == 0) | (d.sum(1) == 3)))     # ~0.75 (ants)
```

### In the news
See news box. Puzzle reasoning (conditioning, symmetry, simulation) is the same toolkit as Bayesian analysis of trial data.

### Interview angle
> [!question] How it is asked
> "Here is a puzzle; talk me through it."

> [!tip] Strong answer includes
> - Restate, small case, method name, answer, sanity check
> - Offer to verify by simulation
> - Do not rush to a memorised answer; reason it out
> - Stay composed when stuck: try the complement or symmetry

---
## 12. Explain It to a Non-Technical Manager
> 🔴 Tier 1 · _Key points:_ Lead with the decision, one number plus its uncertainty, one caveat

### Definition
Models answers for the eight most common "explain" requests.

| Concept | Manager-friendly answer |
|---|---|
| **p-value** | "If nothing had really changed, we would see a difference this big only about 3 times in 100. That is unusual enough that we treat the change as real, though not certain." |
| **Confidence interval** | "Our best estimate is 52, and given the sample size the true value is probably between 49 and 55." |
| **Standard deviation** | "A typical order lands about 4 days either side of the average; the bigger this number, the less predictable delivery is." |
| **Regression coefficient** | "Every extra ₹1 lakh of advertising has been associated with about ₹2 lakh more sales in the range we have seen." |
| **R-squared** | "The model explains about 90% of the ups and downs in sales; the remaining 10% is driven by things we have not captured." |
| **Correlation vs causation** | "These two move together, but that does not prove one causes the other; something else, like season, could drive both. A controlled test would settle it." |
| **Not significant** | "We could not rule out luck with this much data. That is not proof there is no effect; we may need a bigger test." |
| **Sample size** | "To spot a 0.8-point lift reliably we need about 10,000 customers per version; fewer than that and we might miss it or be fooled by noise." |

Bonus lines: **Cpk** "how comfortably the process fits inside the customer's tolerance (1.33 or more is comfortable)"; **Type I vs II** "false alarm vs missed opportunity".

### Example
Result: A/B test of a new checkout, 4.0% vs 4.8% conversion, $p=0.051$. Manager version: "The new checkout looks about 0.8 points better (4.8% vs 4.0%). The test is just short of our usual evidence bar: if the two versions were truly identical, a gap this big would appear about 1 time in 20. Given the low cost of rollout, I recommend a 2-week extension rather than a full launch." Includes decision, size, uncertainty, caveat and next step.

### In the news
See news box. Both Bayesian and frequentist readings can be translated into the same plain statements: how likely, how large, how sure.

### Interview angle
> [!question] How it is asked
> "Explain a p-value to someone who has never taken statistics."

> [!tip] Strong answer includes
> - An everyday analogy (a coin or a jury) in one sentence
> - No jargon without a gloss
> - The practical consequence (what to do next)
> - A check for understanding: "does that make sense?"

---
## 13. Common Misconceptions Table
> 🔴 Tier 1 · _Key points:_ p-value, CI, not significant, correlation, normality, outliers

### Definition

| Misconception | Correction |
|---|---|
| "p = 0.03 means a 3% chance H0 is true" | p is P(data this extreme or more \| H0 true), not P(H0 true); that needs a prior (Bayes) |
| "p > 0.05 proves no effect" | Absence of evidence is not evidence of absence; check power and the CI |
| "A 95% CI contains 95% of the data" | It is about the **mean** (parameter); prediction or tolerance intervals describe individual values |
| "95% probability the true mean is in this interval" | Frequentist: the **procedure** has 95% coverage; Bayesian credible intervals give the probability statement |
| "Statistically significant means important" | Significance depends on $n$; judge by effect size and cost |
| "Correlation implies causation" | Needs design or assumptions; beware confounders, reverse causality |
| "R² of 0.9 means a good model" | Check residuals, out-of-sample error, overfitting |
| "Data must be normal for a t-test" | Residuals or the sampling distribution; CLT helps for moderate $n$ |
| "Remove outliers to get a cleaner result" | Investigate first; deletion without cause is data tampering |
| "A coin that landed heads 5 times is due for tails" | Independent trials have no memory (gambler's fallacy) |
| "Averages describe everyone" | Segment; Simpson's paradox can reverse the story |
| "A bigger sample fixes a biased sample" | Bias does not shrink with $n$; fix the sampling design |
| "Failing to reject H0 means accepting H0" | It means the data are insufficient to reject |
| "Peek until p < 0.05, then stop" | Inflates the false-positive rate |

### Example
Quote check: "Our test showed the new supplier is no different (p = 0.12), so quality is the same." Correction: "With 15 samples per supplier the test could only reliably detect a difference of about 1 SD, so the result is inconclusive; for example, an observed gap of 1.2 units (SD 2) has a 95% CI of roughly −0.3 to +2.7, compatible with both no effect and a meaningful one."

### In the news
See news box. Misreading intervals and p-values is why benchmark authors insist on bootstrapped CIs and why regulators spell out prior and error-rate requirements.

### Interview angle
> [!question] How it is asked
> "What are the most common mistakes you see in how people use p-values and confidence intervals?"

> [!tip] Strong answer includes
> - At least three misconceptions with the correct reading
> - An example of consequences (a missed improvement or a false launch)
> - Remedy: effect sizes, intervals, pre-specified analysis
> - Humility: acknowledge Bayesian alternatives

---
## 14. ⭐ Advanced: Which-Test Decision Table and Rapid-Fire Formulas
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Which test? (decision table)**

| Question | Data | Test |
|---|---|---|
| One mean vs a value | numeric, $\sigma$ unknown | one-sample t |
| Two independent means | numeric | Welch t (Mann-Whitney if non-normal, small $n$) |
| Before/after, same units | numeric pairs | paired t (Wilcoxon signed-rank) |
| 3+ means | numeric | one-way ANOVA (Kruskal-Wallis); Tukey after |
| Two proportions | binary | two-proportion z (Fisher if small) |
| Association of two categoricals | counts | chi-square (Fisher exact for small counts) |
| Two numeric variables | numeric | Pearson (Spearman for ranks), regression |
| Variances | numeric | F-test, Levene |
| Many tests | p-values | Bonferroni, Holm, Benjamini-Hochberg |

**Rapid-fire formulas**

| Item | Formula |
|---|---|
| SE of mean | $s/\sqrt n$ |
| CI for mean | $\bar x\pm t^*\,s/\sqrt n$ |
| CI for proportion | $\hat p\pm z^*\sqrt{\hat p(1-\hat p)/n}$ |
| Sample size, mean | $n=(z\sigma/E)^2$ |
| Sample size, proportion | $n=z^2p(1-p)/E^2$ |
| Welch SE | $\sqrt{s_1^2/n_1+s_2^2/n_2}$ |
| Pooled proportion SE | $\sqrt{\hat p(1-\hat p)(1/n_1+1/n_2)}$ |
| Chi-square | $\sum(O-E)^2/E$ |
| Correlation | $r=S_{xy}/\sqrt{S_{xx}S_{yy}}$ |
| Slope | $b=S_{xy}/S_{xx}$ |
| Adjusted $R^2$ | $1-(1-R^2)\frac{n-1}{n-k-1}$ |
| Cohen's $d$ | $(\bar x_1-\bar x_2)/s_p$ |
| Bonferroni | $\alpha/m$ |
| Poisson | $P(k)=e^{-\lambda}\lambda^k/k!$ |
| Safety stock | $z\,\sigma_d\sqrt{L}$ |

For hands-on versions of these in Excel, Python and Minitab see [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]].

### Example
Case style: "Conversion on mobile is 3.1% and on desktop 5.2%; the CEO wants to cut mobile spend." Structure: (1) is the difference real (two-proportion test, CI)? (2) Simpson's paradox: is the device mix confounded with traffic source or product? (3) Practical significance: revenue per visit, not only conversion. (4) Experiment before deciding. Quick adjusted $R^2$ check: $R^2=0.80$, $n=30$, $k=5$: $1-0.2\times\frac{29}{24}=\mathbf{0.758}$.

### In the news
See news box. The decision table is what regulators and benchmark authors codify when they require a pre-specified analysis plan.

### Interview angle
> [!question] How it is asked
> "I give you a dataset and a business question. How do you choose the method?"

> [!tip] Strong answer includes
> - Clarify the question and the data types, then use a decision table like the one above
> - State assumptions, check them, and name a fallback
> - Quantify effect and uncertainty, not only a verdict
> - Close with the business recommendation and next experiment
