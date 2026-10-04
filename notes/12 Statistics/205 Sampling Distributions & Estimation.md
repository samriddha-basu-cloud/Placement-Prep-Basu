---
tags: [statistics, tier1]
area: Statistics
topic: "Sampling Distributions & Estimation"
tier: Tier 1
roles: All roles
status: complete
subtopics: 14
---
# Sampling Distributions & Estimation

⬅ [[093 Business Statistics Applications]] · [[_Index - Statistics|Statistics]] · [[206 Non-Parametric Tests]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** All roles

## Sub-topics in this note
1. [[#1. Population, Sample, Parameter and Statistic]]
2. [[#2. Sampling Distribution of the Mean, Standard Error and Finite-Population Correction]]
3. [[#3. Sampling Distribution of a Proportion]]
4. [[#4. Sampling Distribution of the Variance (Chi-square)]]
5. [[#5. The Central Limit Theorem: Demonstration and Failure Modes]]
6. [[#6. Point Estimators and Their Properties]]
7. [[#7. Maximum Likelihood Estimation (Bernoulli, Exponential, Normal)]]
8. [[#8. Method of Moments]]
9. [[#9. Confidence Interval for a Mean (z and t)]]
10. [[#10. Confidence Interval for a Proportion (Wald, Wilson, Clopper-Pearson)]]
11. [[#11. Confidence Intervals for Differences of Means and Proportions]]
12. [[#12. Confidence Interval for a Variance or Standard Deviation (Chi-square)]]
13. [[#13. Bootstrap Confidence Intervals]]
14. [[#14. ⭐ Advanced: Sample Size for Estimation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Sample size, sampling frames and the cost of getting estimates wrong
> **India re-engineers its labour survey for precision (2025).** From January 2025 the PLFS sample rose from 12,800 to 22,692 first-stage units (12,504 rural, 10,188 urban) and from 8 to 12 households per unit, about 2,72,304 households or 2.65 times the old sample. The point was monthly national estimates (first bulletin May 2025: April LFPR 55.6%, unemployment rate 5.1%) and quarterly estimates for rural plus urban India. More households shrink the standard error, which is the whole logic of this note. ([PIB: Changes in PLFS from 2025](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2128662&reg=48&lang=2); [AIR News on the first monthly report](https://www.newsonair.gov.in/indias-april-lfpr-at-55-6-unemployment-rate-at-5-1-first-monthly-plfs-report))
>
> **2024 Lok Sabha exit polls missed (June 2024).** Pollsters projected roughly 350-400 seats for the NDA; the result was 293 (BJP 240). Commentators pointed to state-level over-estimation (Uttar Pradesh, Maharashtra) and thin coverage of some voter groups, for example women in Bengal. A reminder that a confidence interval only covers random sampling error, not a biased or unrepresentative sample. ([Down To Earth, 5 June 2024](https://www.downtoearth.org.in/governance/why-did-2024-lok-sabha-predictions-miss-the-mark-heres-the-science-behind-exit-polls))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Population, Sample, Parameter and Statistic
> 🔴 Tier 1 · _Key points:_ Parameter (population, fixed, unknown) vs statistic (sample, random); frame; sampling error vs bias

### Definition
A **population** is the full set of units you care about; a **sample** is the subset you observe. A **parameter** ($\mu,\sigma,p$) is a fixed, usually unknown, number describing the population; a **statistic** ($\bar x, s, \hat p$) is computed from the sample and changes from sample to sample. The **sampling frame** is the list from which units are drawn (all SKUs, all customers on the CRM, all households in the census list). **Estimation** uses a statistic to infer a parameter and attaches a measure of uncertainty.

Two different errors: **sampling error** is random, shrinks as $n$ grows and is what standard errors and confidence intervals describe; **bias** (frame gaps, non-response, self-selection, leading questions) does not shrink with $n$ and is invisible to any formula. See [[092 Sampling & Experimental Design]] for probability sampling designs (SRS, stratified, cluster, systematic) and [[086 Descriptive Statistics]] for $\bar x$ and $s$.

### Example
A kirana-distribution firm wants the mean order value across its 12,000 retailers. Population = 12,000 retailers, parameter $\mu$ = mean order value (unknown). It samples 150 retailers at random; $\bar x$ = ₹8,450 is a statistic. A second sample of 150 gives ₹8,210: the statistic varies, the parameter does not. If the 150 were picked only from retailers who answered the sales rep's call, the estimate is biased towards active retailers and no interval fixes that.

### In the news
See news box. The PLFS redesign shows sampling error being cut by design, while the exit-poll miss shows bias that no formula repairs.

### Interview angle
> [!question] How it is asked
> "We surveyed 500 customers and 70% are satisfied. Can we say 70% of all customers are satisfied?"

> [!tip] Strong answer includes
> - Distinguish statistic (70% of sample) from parameter (true share), and give an interval, not a single number
> - Ask how the 500 were chosen: frame, randomisation, non-response
> - Separate sampling error (quantifiable) from bias (not quantifiable by n)
> - Propose a fix: stratify, reweight, follow up non-responders

---
## 2. Sampling Distribution of the Mean, Standard Error and Finite-Population Correction
> 🔴 Tier 1 · _Key points:_ $E(\bar X)=\mu$; $SE=\sigma/\sqrt n$; FPC $\sqrt{(N-n)/(N-1)}$ when $n/N>5\%$

### Definition
The **sampling distribution** of a statistic is its distribution over all possible samples of size $n$. For the mean of an iid sample from a population with mean $\mu$ and s.d. $\sigma$:

$$E(\bar X)=\mu,\qquad SE(\bar X)=\sigma_{\bar X}=\frac{\sigma}{\sqrt n}$$

The **standard error** (SE) is the standard deviation of the statistic, so it measures how far $\bar x$ typically lands from $\mu$. Quadrupling $n$ halves the SE (the square-root law), which is why precision gets expensive. When $\sigma$ is unknown, the estimated SE is $s/\sqrt n$.

When sampling **without replacement** from a small finite population ($n/N$ above about 5%), multiply by the **finite-population correction**:

$$SE=\frac{\sigma}{\sqrt n}\sqrt{\frac{N-n}{N-1}}$$

The FPC is about 1 when $n\ll N$, so a poll of 1,000 voters is just as precise for a state as for a country. It matters for audits and surveys of small lists.

### Example
Lead times for 500 vendors have $\sigma$ = 12 days. A sample of $n$ = 100: $SE=12/\sqrt{100}=1.20$ days. Since $n/N$ = 20%, FPC $=\sqrt{400/499}=0.895$, so corrected $SE=1.074$ days (about 10% smaller). To halve the SE to 0.60 days you need $n=400$ (ignoring FPC), not 200.

### In the news
See news box. PLFS's 2.65x households cut the nominal SE by a factor $1/\sqrt{2.65}\approx0.61$ (about 39% smaller) if the design were simple random; clustering makes the real gain smaller, which is why designers talk about the design effect.

### Interview angle
> [!question] How it is asked
> "If we double the sample size, does the margin of error halve?"

> [!tip] Strong answer includes
> - No: margin scales with $1/\sqrt n$, so it falls by $1/\sqrt2\approx0.71$; halving needs 4x the sample
> - SE vs standard deviation: SE describes the statistic, SD describes the data
> - FPC for samples above about 5% of a small population
> - Diminishing returns, so fix bias and non-response before buying more n

---
## 3. Sampling Distribution of a Proportion
> 🔴 Tier 1 · _Key points:_ $SE(\hat p)=\sqrt{p(1-p)/n}$; normal if $np\ge10$ and $n(1-p)\ge10$

### Definition
For a yes/no attribute with true share $p$, the sample proportion $\hat p=X/n$ with $X\sim\text{Binomial}(n,p)$ has

$$E(\hat p)=p,\qquad SE(\hat p)=\sqrt{\frac{p(1-p)}{n}}$$

The normal approximation works when $np\ge10$ and $n(1-p)\ge10$ (some books use 5). The SE is largest at $p=0.5$, so $p=0.5$ is the conservative planning value. In practice the SE is estimated by plugging in $\hat p$. For a difference $\hat p_1-\hat p_2$ the variances add (see sub-topic 11). See [[088 Probability Distributions]] for the binomial and its normal approximation.

### Example
A plant has a historical defect rate $p$ = 8%. Inspect $n$ = 400 units. $SE=\sqrt{0.08\times0.92/400}=0.0136$ (1.36 percentage points). Check: $np$ = 32 and $n(1-p)$ = 368, both above 10. Probability the sample shows more than 11% defective: $z=(0.11-0.08)/0.0136=2.21$, so $P\approx0.0135$ (about 1.3%). A reading of 12% would justify stopping to investigate; this is the logic of a p-chart in [[091 Statistical Quality Control (SQC)]].

### In the news
See news box. Exit polls and PLFS indicators such as the unemployment rate (5.1% in April 2025) are sample proportions, and their precision follows this formula.

### Interview angle
> [!question] How it is asked
> "A poll of 1,000 people shows 52% for A. Is A winning?"

> [!tip] Strong answer includes
> - SE $=\sqrt{0.52\times0.48/1000}=1.58$ pp, margin about 3.1 pp, so the interval 48.9% to 55.1% includes 50%
> - Not a statistical lead; add undecideds and non-response bias
> - Conservative $p=0.5$ explains the "plus or minus 3%" headline for $n$ around 1,000

---
## 4. Sampling Distribution of the Variance (Chi-square)
> 🔴 Tier 1 · _Key points:_ $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$ for normal data; sensitive to non-normality

### Definition
If the data are normal, the scaled sample variance follows a chi-square distribution:

$$\frac{(n-1)s^2}{\sigma^2}\sim\chi^2_{n-1},\qquad E(s^2)=\sigma^2,\qquad Var(s^2)=\frac{2\sigma^4}{n-1}$$

The distribution of $s^2$ is right-skewed for small $n$, so symmetric "estimate $\pm$ margin" intervals are wrong for variances. The result is very sensitive to non-normal tails; for heavy-tailed data the variance of $s^2$ depends on the kurtosis and the chi-square result is unreliable. The ratio of two independent sample variances from normal populations follows an F distribution, used in ANOVA ([[089 Hypothesis Testing]]) and Levene-type variance checks.

### Example
A filling machine has true $\sigma^2=16$ ($\sigma$ = 4 ml). With $n=16$: $Var(s^2)=2\cdot16^2/15=34.1$, so the s.d. of $s^2$ is 5.8. The probability the sample variance exceeds 28: $\chi^2=15\times28/16=26.25$ on 15 d.f., so $P=0.035$. A sample variance of 28 happens about 3.5% of the time by chance when the process is in control.

### In the news
See news box. Variability estimates (not only means) drive process-capability claims, so small-sample variance uncertainty is a standing risk in quality reporting.

### Interview angle
> [!question] How it is asked
> "We measured 10 parts and the s.d. is 0.8 mm against a spec of 1.0. Are we capable?"

> [!tip] Strong answer includes
> - A sample s.d. is itself random: build a chi-square interval before claiming capability
> - Chi-square interval assumes normality; check with a histogram or normal probability plot
> - Ten points give very wide variance intervals; collect more before a capability sign-off

---
## 5. The Central Limit Theorem: Demonstration and Failure Modes
> 🔴 Tier 1 · _Key points:_ $\bar X$ is approx normal for large $n$ whatever the population; needs finite variance and independence

### Definition
**CLT:** for iid draws with finite mean $\mu$ and finite variance $\sigma^2$, the standardised mean converges to a standard normal:

$$\frac{\bar X-\mu}{\sigma/\sqrt n}\ \xrightarrow{d}\ N(0,1)$$

Rule of thumb: $n\ge30$ is enough for mild skew; strongly skewed or heavy-tailed data need far more. The skewness of $\bar X$ falls like $\gamma/\sqrt n$, where $\gamma$ is the population skewness (for the exponential $\gamma=2$).

**When it fails or crawls:** (1) infinite variance (Cauchy, some power-law tails): averages do not settle; (2) extreme skew or outlier-prone data (lognormal with large $\sigma$, insurance claims, order values): needs thousands of points; (3) dependent data (autocorrelation, clusters) where the effective sample size is much smaller than $n$, see [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]; (4) non-identical distributions with a few dominant terms; (5) the "$n$" that matters is the number of independent units.

### Example
Executed simulation (NumPy, 100,000 replications):

```python
import numpy as np
from scipy import stats
rng = np.random.default_rng(7)
for n in (2, 5, 30, 100):
    m = rng.exponential(1, (100_000, n)).mean(1)          # true mean = 1
    print(n, round(stats.skew(m), 3), round(2/np.sqrt(n), 3),
          np.mean(abs(m - 1) <= 1.96/np.sqrt(n)))
```

| n | skewness of $\bar x$ | theory $2/\sqrt n$ | actual coverage of $\bar x\pm1.96\,SE$ |
|---|---|---|---|
| 2 | 1.43 | 1.41 | 95.1% |
| 5 | 0.91 | 0.89 | 95.7% |
| 30 | 0.37 | 0.37 | 95.3% |
| 100 | 0.21 | 0.20 | 95.0% |

Failure: the mean of Cauchy draws is itself Cauchy, so the interquartile range stays at about 2.0 for n = 1, 10 or 1000 (simulated). For lognormal data with $\sigma=1.5$, the nominal 95% t-interval for the mean covered the true mean only 78.7% of the time at n = 30, 87.9% at n = 200 and 92.9% at n = 2000. Heavy-tailed revenue data therefore break "n above 30" folklore.

(The table is the output of the code shown. The Cauchy and lognormal figures come from separate simulations of 20,000 replications each and move by under a percentage point with the seed.)

### In the news
See news box. Monthly survey indicators rely on CLT-based intervals; the PLFS enlarged its sample partly so those intervals stay narrow at monthly frequency.

### Interview angle
> [!question] How it is asked
> "Why is n = 30 the magic number, and when would you not trust it?"

> [!tip] Strong answer includes
> - CLT is about the distribution of the mean, not the data; 30 is a convention for mild skew
> - Failure cases: heavy tails (revenue per user, claims), outliers, autocorrelation, tiny clusters
> - Remedies: bootstrap, log transform and report geometric mean, trimmed means, bigger n, [[206 Non-Parametric Tests|non-parametric methods]]

---
## 6. Point Estimators and Their Properties
> 🔴 Tier 1 · _Key points:_ Bias, variance, MSE; unbiased, consistent, efficient, sufficient

### Definition
A **point estimator** $\hat\theta$ is a rule that gives one number for parameter $\theta$. Quality criteria:

- **Bias** $=E(\hat\theta)-\theta$. **Unbiased** if zero.
- **Variance** of the estimator: how much it scatters across samples.
- **Mean squared error:** $MSE=Var(\hat\theta)+\text{Bias}^2$. A little bias can pay for a lot less variance (shrinkage, ridge regression).
- **Consistent:** $\hat\theta\to\theta$ in probability as $n\to\infty$ (the sample mean is, by the law of large numbers).
- **Efficient:** lowest variance among unbiased estimators; the Cramer-Rao bound $Var(\hat\theta)\ge 1/I(\theta)$ sets the floor ($I$ = Fisher information of the sample).
- **Sufficient:** captures all the information the sample holds about $\theta$ (for the normal mean, $\bar x$).

Key facts: $\bar x$ is unbiased for $\mu$; $s^2$ with divisor $n-1$ is unbiased for $\sigma^2$ while divisor $n$ is biased low by factor $(n-1)/n$; $s$ is slightly biased low for $\sigma$ even with $n-1$. For a normal population the sample median is unbiased for $\mu$ but about 64% as efficient as $\bar x$ (variance about $\pi/2$ times larger).

### Example
Simulation: $n=5$ draws from $N(0,1)$, 200,000 samples. Mean of the divisor-$n$ variance = 0.801 (theory $4/5=0.80$); divisor $n-1$ gives 1.002, unbiased. Yet by MSE, for normal data dividing by $n+1$ is best: MSE factors (in units of $\sigma^4$) are 0.500 for $n-1=4$, 0.360 for $n=5$ and 0.333 for $n+1=6$. "Unbiased" is not the same as "best".

### In the news
See news box. Survey agencies publish weighted estimators that are deliberately design-based and approximately unbiased, then report SEs; a headline number is only half the result.

### Interview angle
> [!question] How it is asked
> "Why do we divide by n-1 in the sample variance?"

> [!tip] Strong answer includes
> - Deviations are measured from $\bar x$, which sits closer to the data than $\mu$, so $\sum(x_i-\bar x)^2$ underestimates; dividing by $n-1$ removes the bias (one degree of freedom used)
> - Bias vs variance: MSE is the combined criterion; ties to the bias-variance trade-off in [[098 Model Selection & Optimization]]
> - Consistency matters more than unbiasedness for large samples

---
## 7. Maximum Likelihood Estimation (Bernoulli, Exponential, Normal)
> 🔴 Tier 1 · _Key points:_ Maximise $L(\theta)=\prod f(x_i;\theta)$; solve score equation; invariance; asymptotically efficient

### Definition
The **likelihood** $L(\theta)=\prod_i f(x_i;\theta)$ treats the observed data as fixed and the parameter as variable; the **MLE** $\hat\theta$ maximises it (in practice the log-likelihood $\ell(\theta)=\sum\ln f(x_i;\theta)$). Set $\partial\ell/\partial\theta=0$ (the score equation) and check it is a maximum. MLEs are consistent, asymptotically normal with variance $1/I(\theta)$ (so asymptotically efficient), and invariant: the MLE of $g(\theta)$ is $g(\hat\theta)$. MLE is the engine behind logistic regression ([[209 Generalised Linear Models & Categorical Data Analysis]]) and many ML losses ([[095 Regression Algorithms]], [[096 Classification Algorithms]]).

**Bernoulli:** $\ell=\sum x_i\ln p+(n-\sum x_i)\ln(1-p)$, so $\hat p=\bar x$. **Exponential (rate $\lambda$):** $f=\lambda e^{-\lambda x}$, $\ell=n\ln\lambda-\lambda\sum x_i$, so $\hat\lambda=n/\sum x_i=1/\bar x$ and $SE(\hat\lambda)\approx\hat\lambda/\sqrt n$ (since $I=n/\lambda^2$). **Normal:** $\hat\mu=\bar x$ and $\hat\sigma^2=\frac1n\sum(x_i-\bar x)^2$, which is biased: MLE need not be unbiased.

### Example
Ten inspected parts, 1 = defective: 1,0,0,1,0,0,0,1,0,0. $\hat p=3/10=0.30$.

Eight times between breakdowns (hours): 12, 45, 7, 30, 22, 64, 15, 9. $\sum=204$, $\bar x=25.5$ h, so $\hat\lambda=8/204=0.0392$ per hour and the MLE of the mean time between failures is 25.5 h. Approx SE of $\hat\lambda$: $0.0392/\sqrt8=0.0139$ (a wide interval for n = 8). Normal sensors reading 48, 52, 50, 47, 53, 51: $\hat\mu=50.17$, MLE variance $=4.47$ against the unbiased $s^2=5.37$. Link to reliability in [[155 Reliability Engineering & Maintenance Optimisation]] and queue inter-arrival rates in [[149 Queueing Theory & Waiting-Line Analysis]].

### In the news
See news box. Large-scale survey weighting and modelled estimates (small-area estimation) are likelihood based; MLE is the default estimation workhorse in analytics tools.

### Interview angle
> [!question] How it is asked
> "Derive the MLE for the failure rate of an exponential lifetime and say what it tells you."

> [!tip] Strong answer includes
> - Write the likelihood, take the log, differentiate, get $\hat\lambda=1/\bar x$
> - Interpret: reciprocal of average lifetime; mention censored data change the likelihood
> - Mention asymptotic properties and that MLE of $\sigma^2$ is biased but consistent
> - Explain MLE vs least squares: identical for normal errors

---
## 8. Method of Moments
> 🔴 Tier 1 · _Key points:_ Equate sample moments to population moments; simple, consistent, often less efficient than MLE

### Definition
The **method of moments (MoM)** sets population moments (functions of the parameters) equal to the corresponding sample moments and solves. For one parameter use $E(X)=\bar x$; for two use $E(X)$ and $E(X^2)$ (or the variance). MoM is easy, gives consistent estimators and often serves as starting values for iterative MLE; it can be less efficient and can return impossible values (a negative variance estimate, a parameter outside its range).

### Example
**Uniform(0, $\theta$):** $E(X)=\theta/2$, so $\hat\theta_{MoM}=2\bar x$. Data 3.1, 7.4, 5.2, 9.0, 1.8, 6.5: $\bar x=5.5$, so $\hat\theta=11.0$, whereas the MLE is the sample maximum, 9.0. MoM can fall below the observed maximum for other samples, an impossible value for this model. **Gamma(shape $k$, scale $\theta$)** for task durations: mean $k\theta$, variance $k\theta^2$. Data 4.2, 6.1, 3.3, 8.9, 5.0, 7.4, 2.8, 5.5: $\bar x=5.4$, population-style variance $=3.69$, so $\hat\theta=3.69/5.4=0.683$ and $\hat k=5.4^2/3.69=7.90$. These feed a PERT-style duration model in [[039 Scheduling Tools (CPM-PERT-Gantt)]].

### In the news
See news box. Simple moment-based estimators underpin fast dashboard metrics; fuller likelihood models are used when decisions are costly.

### Interview angle
> [!question] How it is asked
> "What is the difference between MoM and MLE and when would you use each?"

> [!tip] Strong answer includes
> - MoM: match moments, closed form, quick; MLE: maximise likelihood, more efficient asymptotically, needs optimisation
> - MoM can give out-of-range values; MLE respects the parameter space
> - Practical use of MoM as initial values for numerical MLE

---
## 9. Confidence Interval for a Mean (z and t)
> 🔴 Tier 1 · _Key points:_ $\bar x\pm z\,\sigma/\sqrt n$ if $\sigma$ known; $\bar x\pm t_{n-1}\,s/\sqrt n$ otherwise

### Definition
A $(1-\alpha)$ **confidence interval** is built by a procedure that captures the true parameter in $(1-\alpha)$ of repeated samples. Once computed, a given interval either contains $\mu$ or it does not; the 95% describes the method, not this one interval.

$$\bar x\pm z_{\alpha/2}\frac{\sigma}{\sqrt n}\ \ (\sigma\text{ known}),\qquad \bar x\pm t_{\alpha/2,\,n-1}\frac{s}{\sqrt n}\ \ (\sigma\text{ unknown})$$

The $t$ distribution has fatter tails than the normal (heavier for small d.f.), compensating for estimating $\sigma$ with $s$; it needs approximately normal data for small $n$ and converges to $z$ as $n$ grows. The margin of error $E=\text{critical value}\times SE$ is wider for higher confidence and narrower for larger $n$. Interval width is not a probability statement about $\mu$ (the Bayesian credible interval in [[210 Bayesian Statistics for Decisions]] makes that kind of statement).

### Example
$n=25$ deliveries, $\bar x=48.2$ minutes, $s=6.4$. $SE=6.4/5=1.28$; $t_{0.025,24}=2.064$; margin $=2.64$. 95% CI: **(45.56, 50.84) minutes**. Wrongly using $z=1.96$ gives (45.69, 50.71), too narrow. If $\sigma=6$ were truly known: (45.85, 50.55). To test a promise of "under 45 minutes", note 45 lies outside the interval, matching a two-sided t-test at 5% in [[089 Hypothesis Testing]].

### In the news
See news box. Survey releases such as PLFS and consumption surveys publish estimates with relative standard errors; analysts reading them should build the interval, not quote only the point value.

### Interview angle
> [!question] How it is asked
> "What does a 95% confidence interval actually mean?"

> [!tip] Strong answer includes
> - Long-run coverage of the procedure; not "95% probability the mean is in this interval"
> - Width drivers: confidence level, variability, sample size
> - t vs z and the normality assumption for small samples
> - Link to hypothesis tests: a value outside the interval is rejected at the matching $\alpha$

---
## 10. Confidence Interval for a Proportion (Wald, Wilson, Clopper-Pearson)
> 🔴 Tier 1 · _Key points:_ Wald $\hat p\pm z\sqrt{\hat p(1-\hat p)/n}$ fails for small $n$ or extreme $p$; prefer Wilson

### Definition
**Wald:** $\hat p\pm z_{\alpha/2}\sqrt{\hat p(1-\hat p)/n}$. Easy but its true coverage can fall well below nominal for small $n$ or $\hat p$ near 0 or 1, and it can give limits below 0 or above 1. **Wilson score** interval (preferred default):

$$\frac{\hat p+\frac{z^2}{2n}\ \pm\ z\sqrt{\frac{\hat p(1-\hat p)}{n}+\frac{z^2}{4n^2}}}{1+\frac{z^2}{n}}$$

**Clopper-Pearson** ("exact") inverts the binomial and is conservative (coverage at least nominal). Agresti-Coull adds about 2 successes and 2 failures. For zero events in $n$ trials the "rule of three" gives an approximate 95% upper bound of $3/n$.

### Example
18 of 150 customers returned a product: $\hat p=0.12$. Wald: (6.80%, 17.20%). Wilson: (7.73%, 18.17%). Clopper-Pearson: (7.27%, 18.30%). They differ only mildly at this $n$. Now 2 defects in 40: $\hat p=5\%$. Wald gives (-1.75%, 11.75%), an impossible lower limit; Wilson gives (1.38%, 16.50%); Clopper-Pearson (0.61%, 16.92%). In Python: `statsmodels.stats.proportion.proportion_confint(2, 40, method='wilson')`. Rule of three: 0 defects in 60 gives an upper bound about 5%.

### In the news
See news box. Poll margins of error and PLFS rates are proportion intervals; small subgroup cells in survey tables need Wilson or exact intervals, not Wald.

### Interview angle
> [!question] How it is asked
> "Our A/B test has 2 conversions out of 40 in the pilot. What is the conversion rate range?"

> [!tip] Strong answer includes
> - Point estimate 5% but a Wald interval goes negative: use Wilson or exact
> - Report (1.4%, 16.5%) and say the pilot is too small to decide
> - Mention rule of three for zero events and the conservative $p=0.5$ for planning

---
## 11. Confidence Intervals for Differences of Means and Proportions
> 🔴 Tier 1 · _Key points:_ Variances add; Welch for unequal variances; CI containing 0 means no significant difference

### Definition
**Two independent means (Welch, the safe default):**

$$(\bar x_1-\bar x_2)\pm t_{\alpha/2,\nu}\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}},\qquad \nu=\frac{(s_1^2/n_1+s_2^2/n_2)^2}{\frac{(s_1^2/n_1)^2}{n_1-1}+\frac{(s_2^2/n_2)^2}{n_2-1}}$$

Pooled-variance $t$ is valid only if $\sigma_1^2\approx\sigma_2^2$. **Paired data** (same unit before and after): form differences $d_i$ and use the one-sample interval on $\bar d$, which removes between-unit noise. **Two proportions:**

$$(\hat p_1-\hat p_2)\pm z_{\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}$$

An interval excluding 0 is equivalent to a significant two-sided test; but the interval also reports effect size and its uncertainty, which is what a business decision needs.

### Example
Cycle times: line A, $n_1=40$, mean 52.4, $s_1=8.1$; line B, $n_2=35$, mean 48.9, $s_2=10.3$. Difference 3.5; $SE=\sqrt{8.1^2/40+10.3^2/35}=2.161$; Welch $\nu=64.3$; $t=1.998$; 95% CI **(-0.82, 7.82)**. Pooled $t$ gives (-0.74, 7.74), nearly identical. The interval includes 0, so no proof that A is slower, though a 7.8-unit gap is not ruled out.

Conversion: new checkout 156/1200 = 13.0%; old 119/1100 = 10.8%. Difference 2.18 pp, $SE=1.35$ pp, 95% CI **(-0.46, 4.83) pp**. Not significant at 5%; the plausible uplift ranges from slightly negative to nearly 5 pp, so the next step is a bigger test (see sample size below and [[214 Causal Inference & Experimentation Beyond A-B Tests]]).

### In the news
See news box. Comparing survey estimates across rounds (for example monthly PLFS readings) needs difference intervals with correlated panels in mind; rotation panels induce overlap that changes the SE.

### Interview angle
> [!question] How it is asked
> "Version B shows 2.2 points higher conversion. Do we ship it?"

> [!tip] Strong answer includes
> - Compute the interval for the difference; here it spans zero
> - Weigh cost of a wrong ship vs cost of waiting; extend the test or check power
> - Mention practical significance and multiple looks (peeking inflates false positives)

---
## 12. Confidence Interval for a Variance or Standard Deviation (Chi-square)
> 🔴 Tier 1 · _Key points:_ $\left[\frac{(n-1)s^2}{\chi^2_{1-\alpha/2}},\ \frac{(n-1)s^2}{\chi^2_{\alpha/2}}\right]$; asymmetric; normality assumed

### Definition
From $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$ (normal data):

$$\frac{(n-1)s^2}{\chi^2_{\alpha/2,\,n-1}\ (\text{upper tail})}\ \le\ \sigma^2\ \le\ \frac{(n-1)s^2}{\chi^2_{1-\alpha/2,\,n-1}\ (\text{lower tail})}$$

Take square roots for $\sigma$. The interval is asymmetric: the upper limit is much farther from $s^2$ than the lower. It is not robust to non-normality. Ratio of variances uses the F distribution.

### Example
$n=20$ measurements, $s=3.2$ mm: $s^2=10.24$, $(n-1)s^2=194.56$. The $\chi^2_{19}$ 2.5% and 97.5% points are 8.907 and 32.852. Variance CI: $194.56/32.852=5.92$ to $194.56/8.907=21.84$, so **$\sigma\in(2.43, 4.67)$ mm**. The upper limit is 46% above $s$, whereas the lower is 24% below: asymmetric. If the specification demands $\sigma\le 3$, the data cannot confirm it. This is the interval to use before quoting a process capability in [[008 Six Sigma & Quality Tools]].

### In the news
See news box. Variance-based claims (capability indices, volatility) carry wide intervals at small $n$; always show them.

### Interview angle
> [!question] How it is asked
> "Process s.d. from 20 samples is 3.2. How sure are you that true s.d. is under 4?"

> [!tip] Strong answer includes
> - Chi-square interval with $n-1$ d.f.; upper limit 4.67 so cannot claim under 4
> - Asymmetry and normality assumption
> - Remedy: bigger sample or bootstrap

---
## 13. Bootstrap Confidence Intervals
> 🔴 Tier 1 · _Key points:_ Resample with replacement B times; percentile or BCa interval; works for medians, ratios, any statistic

### Definition
The **bootstrap** treats the sample as a stand-in for the population: draw $B$ (typically 5,000-10,000) resamples of size $n$ **with replacement**, compute the statistic on each, and use the resulting distribution for inference. **Percentile CI:** the 2.5th and 97.5th percentiles of the bootstrap statistics. **BCa** corrects bias and skew and is preferred (`scipy.stats.bootstrap(..., method='BCa')`). It needs only the data, no formula, so it handles medians, trimmed means, percentiles, ratios, correlation and model metrics. Limits: poor for tiny samples, extreme-value statistics (maximum), and dependent data unless a block bootstrap is used.

### Example
Executed on 20 order-to-delivery times in days (NumPy seed 11, $B$ = 10,000): the data have mean 3.65, median 2.85 and two extreme values (9.6, 12.2).

```python
import numpy as np
x = np.array([2.1,2.4,2.2,3.8,2.9,2.3,9.6,2.7,3.1,2.5,4.4,2.6,3.3,2.8,12.2,3.0,2.2,2.9,3.6,2.4])
rng = np.random.default_rng(0); idx = rng.integers(0, len(x), (10_000, len(x)))
print(np.percentile(np.median(x[idx], 1), [2.5, 97.5]))
```

Output: median percentile CI **(2.45, 3.20)** days (a BCa run in SciPy gave 2.45 to 3.26); mean percentile CI about (2.7, 4.8) against the t-interval (2.44, 4.86), while the BCa mean interval stretched to about (2.87, 5.41), reflecting the right skew that the symmetric t-interval ignores. With two outliers the mean is unstable and the median is a better summary of typical delivery. Exact limits vary slightly with the random seed.

### In the news
See news box. Survey agencies and analytics teams increasingly use resampling or replicate weights for variance estimates of complex statistics where no simple formula exists.

### Interview angle
> [!question] How it is asked
> "How would you put a confidence interval around the median delivery time?"

> [!tip] Strong answer includes
> - Bootstrap: resample with replacement, compute median each time, take percentiles
> - State B, seed, and that BCa corrects skew
> - Warn about dependence (use block bootstrap for time series) and tiny samples

---
## 14. ⭐ Advanced: Sample Size for Estimation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Choose $n$ so that the margin of error is at most $E$ at confidence $1-\alpha$.

$$n=\left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2\ \ (\text{mean}),\qquad n=\frac{z_{\alpha/2}^2\,p(1-p)}{E^2}\ \ (\text{proportion}),\qquad n_{\text{each group}}=2\left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2\ \ (\text{difference of means})$$

Use $p=0.5$ when unknown. Round **up**. With a finite population, $n=\dfrac{n_0}{1+(n_0-1)/N}$. If $\sigma$ must be estimated by $s$, use a pilot and iterate with $t$ (adds a few units). Add inflation for non-response, and a design effect for clustered designs. This is *estimation* precision; sample size for a hypothesis test with power is covered in [[089 Hypothesis Testing]] (power, effect size) and [[092 Sampling & Experimental Design]].

### Example
Mean order value, $\sigma\approx$ ₹15, margin ±₹2, 95%: $n=(1.96\times15/2)^2=216.1$, so **217**; the iterative t version converges to 219. At 90% confidence ($z=1.645$): $n=152.2$, so 153. A satisfaction survey with ±3 pp at 95%, worst case $p=0.5$: $n=1.96^2\times0.25/0.03^2=1067.1$, so **1,068**. If $p$ is believed near 10%: 384.2, so 385. For a population of $N=2000$: $1068/(1+1067/2000)=696.4$, so 697. Expecting 60% response means mailing $697/0.6\approx1{,}162$. Difference of two means with $\sigma=10$ and $E=2$: 192.1 per group, so 193 each (386 total).

### In the news
See news box. PLFS's 2.65x sample was a sample-size decision to deliver monthly, not just annual, precision; larger surveys cost more but buy narrower intervals roughly as $1/\sqrt n$.

### Interview angle
> [!question] How it is asked
> "How many customers should we survey to estimate satisfaction within 3 points?"

> [!tip] Strong answer includes
> - Formula with $p=0.5$, $z=1.96$, $E=0.03$ giving about 1,070
> - Adjust for finite population, non-response, and segments (need that many per segment for segment-level claims)
> - Note the precision/cost curve ($1/\sqrt n$) and that bias control matters more than a bigger n
> - Cross-reference tools in [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]]
