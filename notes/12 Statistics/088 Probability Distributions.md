---
tags: [statistics, tier1]
area: Statistics
topic: "Probability Distributions"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Probability Distributions

⬅ [[087 Probability Fundamentals]] · [[_Index - Statistics|Statistics]] · [[089 Hypothesis Testing]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Normal Distribution]]
2. [[#2. Standard Normal (Z)]]
3. [[#3. Binomial Distribution]]
4. [[#4. Poisson Distribution]]
5. [[#5. Uniform Distribution]]
6. [[#6. Exponential Distribution]]
7. [[#7. t-Distribution]]
8. [[#8. Chi-Square Distribution]]
9. [[#9. F-Distribution]]
10. [[#10. Log-Normal Distribution]]
11. [[#11. ⭐ Advanced: Newsvendor Model with Normal Demand]]
12. [[#12. ⭐ Advanced: Poisson-Exponential Link and the M/M/1 Queue]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's statistical overhaul and the FDA's Bayesian turn
> **India's new GDP series (released 27 Feb 2026, base year 2022-23).** Real GDP growth for FY2025-26 (second advance estimate) was reported at **7.6%** and FY2024-25 revised to **7.1%** (nominal 9.7%); the series adds GST, e-Vahan and company-filing data and uses double deflation in manufacturing and agriculture. Estimates like these are random variables with uncertainty; revisions are the realised error. ([PIB release as read via fetch](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2233518&reg=48&lang=2))
>
> **FDA draft guidance on Bayesian methods (9 Jan 2026).** Describes Bayesian methods for primary inference in Phase III trials, combining prior knowledge with new data. Posterior distributions (often Beta or Normal) replace a single p-value as the basis of decision. ([Alston and Bird summary](https://www.alston.com/en/insights/publications/2026/01/fda-bayesian-guidance-drug-trials))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Normal Distribution
> 🔴 Tier 1 · _Tracker hint:_ Bell curve; μ±σ=68%, μ±2σ=95%, μ±3σ=99.7%; Z-table; N(μ,σ²)

### Definition
$$f(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
Symmetric, bell-shaped, fully described by mean $\mu$ and variance $\sigma^2$; mean = median = mode. **Empirical rule:** $\mu\pm1\sigma$ = 68.3%, $\pm2\sigma$ = 95.4%, $\pm3\sigma$ = 99.7%. Sums and averages of many small independent effects are approximately normal (CLT, see [[087 Probability Fundamentals]]). A linear combination of independent normals is normal, with means and variances adding. Use for measurement errors, process dimensions, aggregated demand; avoid for strictly positive heavily skewed data.

### Example
Delivery time is $N(40,\,5^2)$ minutes. P(35–45 min) ≈ 68%. P(X>50): $z=(50-40)/5=2$, so **2.28%**. P(X<32): $z=-1.6$, so **5.48%**. The time within which 95% arrive: $40+1.645\times5=\mathbf{48.2}$ min.

### In the news
See news box. Growth estimates are reported as point numbers, but their sampling error is typically modelled as approximately normal.

### Interview angle
> [!question] How it is asked
> "Demand is normally distributed with mean 500 and sd 80. What is the probability demand exceeds 600?"

> [!tip] Strong answer includes
> - z = 100/80 = 1.25 → P = 1 − 0.8944 = 10.6%
> - Empirical rule as a sanity check
> - Mention the assumption and when it fails (negative demand, skew)
> - Link to safety stock

---

## 2. Standard Normal (Z)
> 🔴 Tier 1 · _Tracker hint:_ N(0,1); Z=(X-μ)/σ; used for hypothesis testing, confidence intervals

### Definition
The **standard normal** is $N(0,1)$. Any $X\sim N(\mu,\sigma^2)$ converts by $Z=(X-\mu)/\sigma$, so one table $\Phi(z)=P(Z\le z)$ serves all. Symmetry: $\Phi(-z)=1-\Phi(z)$.

Key critical values:
| Confidence / service level | One-tail Z | Two-tail Z |
|---|---|---|
| 90% | 1.282 | 1.645 |
| 95% | 1.645 | 1.960 |
| 99% | 2.326 | 2.576 |

Uses: confidence interval $\bar{x}\pm Z\,\sigma/\sqrt{n}$, z-test, and **safety stock** $SS=Z\sigma_{LT}$ with $Z=\Phi^{-1}(\text{service level})$. Excel: `=NORM.S.INV(0.95)` and `=NORM.S.DIST(1.645,TRUE)`.

### Example
Lead-time demand $N(500,\ 80^2)$; 95% cycle service level: $Z=1.645$, SS = 1.645×80 = **131.6 ≈ 132**, reorder point = 500 + 132 = **632 units**. For 99%: Z = 2.326, SS = 186, an extra 54 units to cut stock-out probability from 5% to 1%.

### In the news
See news box. Interval estimates for statistics (such as growth) use these critical values.

### Interview angle
> [!question] How it is asked
> "How do you set safety stock for a 98% service level?"

> [!tip] Strong answer includes
> - Z for 98% = 2.054, SS = Z × σ over lead time
> - σ over lead time = σ_d × √L (if demand independent)
> - Cycle service level vs fill rate distinction
> - Cost of each extra percentage point of service

---

## 3. Binomial Distribution
> 🔴 Tier 1 · _Tracker hint:_ n trials, p=prob of success; P(X=k) = nCk × p^k × (1-p)^(n-k); mean=np

### Definition
$$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},\ k=0,\dots,n$$
Conditions: fixed $n$, two outcomes, constant $p$, independent trials. Mean $np$; variance $np(1-p)$. For large $n$ it is approx normal when $np\ge10$ and $n(1-p)\ge10$ (with continuity correction). Excel: `=BINOM.DIST(k,n,p,FALSE)` (exact), `TRUE` (cumulative). Sampling without replacement from a small population is hypergeometric instead.

### Example
Sample 10 items; true defect rate 10%. $P(X=2)=\binom{10}{2}(0.1)^2(0.9)^8=45\times0.01\times0.4305=\mathbf{0.194}$. Mean = 1, variance = 0.9. $P(X=0)=0.9^{10}=0.349$; so there is a 65% chance of at least one defect in the sample.

### In the news
See news box. A trial's success count out of n patients is binomial; Bayesian designs put a Beta prior on p (conjugate).

### Interview angle
> [!question] How it is asked
> "A call-centre agent resolves 80% of calls first time. Out of 5 calls, what is the probability exactly 4 are resolved?"

> [!tip] Strong answer includes
> - $\binom{5}{4}(0.8)^4(0.2)=5\times0.4096\times0.2=0.4096$
> - State the independence and constant-p assumptions
> - Mean and variance for planning
> - When to approximate with normal or Poisson

---

## 4. Poisson Distribution
> 🔴 Tier 1 · _Tracker hint:_ Count of events in fixed interval; P(X=k) = e^(-λ)λ^k/k!; mean=λ; defects, arrivals

### Definition
$$P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!},\quad k=0,1,2,\dots$$
Counts of rare, independent events in a fixed interval (time, area, length) at constant average rate $\lambda$. **Mean = variance = $\lambda$** (check this: if variance greatly exceeds the mean, the data is over-dispersed, so consider negative binomial). Poisson approximates binomial when $n$ is large and $p$ small ($\lambda=np$). Rate scales with interval: $\lambda_{2h}=2\lambda_{1h}$. Excel: `=POISSON.DIST(k,λ,FALSE)`.

### Example
A helpline receives on average $\lambda=3$ calls per hour. $P(0)=e^{-3}=\mathbf{0.0498}$. $P(2)=e^{-3}\cdot9/2=\mathbf{0.2240}$. $P(X\le2)=e^{-3}(1+3+4.5)=\mathbf{0.4232}$, so $P(X\ge3)=0.577$. Spare-parts demand of 0.5 per month: P(zero demand in a month) = $e^{-0.5}=0.607$.

### In the news
See news box. Not tied to a specific recent event; count data (defects, breakdowns, arrivals) is a standard Poisson case.

### Interview angle
> [!question] How it is asked
> "A bank branch gets 6 customers per 10 minutes on average. What is the probability of more than 8 in a 10-minute window?"

> [!tip] Strong answer includes
> - Identify as Poisson with λ=6; compute complement of P(X≤8)
> - State assumptions (independence, constant rate)
> - Check the mean-variance equality
> - Link to queueing/staffing and spare parts

---

## 5. Uniform Distribution
> 🔴 Tier 1 · _Tracker hint:_ All outcomes equally likely; U(a,b); mean=(a+b)/2; useful in simulations

### Definition
Continuous $U(a,b)$: $f(x)=\frac{1}{b-a}$ for $a\le x\le b$; $P(c\le X\le d)=\frac{d-c}{b-a}$. Mean $\frac{a+b}{2}$, variance $\frac{(b-a)^2}{12}$. Discrete uniform: each of $k$ outcomes has probability $1/k$ (die). Random number generators draw $U(0,1)$; **inverse transform** turns them into any other distribution. Used when only min and max are known (maximum ignorance) in simulations and PERT-like estimates.

### Example
Supplier lead time $U(4,10)$ days: mean = **7**, variance = 36/12 = **3**, sd = 1.73. P(lead time > 8) = (10−8)/6 = **0.333**. Excel simulation: `=4+RAND()*6`.

### In the news
See news box. Not tied to a specific recent event; simulation models of supply disruption often use uniform inputs for unknown durations.

### Interview angle
> [!question] How it is asked
> "A delivery slot is anywhere between 2 and 6 pm. What is the chance it arrives before 3:30?"

> [!tip] Strong answer includes
> - (3.5−2)/4 = 0.375
> - Mean 4 pm, sd = 4/√12 ≈ 1.15 h
> - Recognise that it models total uncertainty within bounds
> - Mention RAND() for simulation

---

## 6. Exponential Distribution
> 🔴 Tier 1 · _Tracker hint:_ Time between Poisson events; P(X>x) = e^(-λx); memoryless property

### Definition
Time between events of a Poisson process with rate $\lambda$: $f(x)=\lambda e^{-\lambda x}$, $x\ge0$; $P(X>x)=e^{-\lambda x}$; mean $1/\lambda$, variance $1/\lambda^2$. **Memoryless:** $P(X>s+t\mid X>s)=P(X>t)$: the elapsed waiting time tells you nothing. Used for inter-arrival times, service times in M/M/1 queues, time to failure for random failures (constant hazard rate; MTBF = $1/\lambda$). Not suitable for wear-out failures (increasing hazard; use Weibull).

### Example
Mean service time 5 min, so $\lambda=0.2$/min. $P(X>10)=e^{-2}=\mathbf{0.135}$. Given a customer has already waited 5 min being served, the chance the service lasts more than 10 further minutes is still 0.135. A machine with MTBF of 500 h: P(survives 100 h) = $e^{-0.2}=0.819$.

### In the news
See news box. Not tied to a specific recent event; used in reliability models for equipment under predictive maintenance programmes.

### Interview angle
> [!question] How it is asked
> "What does 'memoryless' mean, and for which processes is it realistic?"

> [!tip] Strong answer includes
> - The conditional-probability statement
> - Constant failure rate / random arrivals as the realistic cases
> - Where it fails (ageing components)
> - Relation to Poisson (counts vs gaps)

---

## 7. t-Distribution
> 🔴 Tier 1 · _Tracker hint:_ Used when n<30 or σ unknown; heavier tails than normal; df=n-1

### Definition
When σ is estimated by sample sd $s$, the statistic $t=\frac{\bar{x}-\mu}{s/\sqrt{n}}$ follows a **Student t-distribution** with $df=n-1$. Bell-shaped and symmetric like the normal but with **heavier tails**, reflecting extra uncertainty from estimating σ. As df grows it converges to $N(0,1)$ (roughly equal above df ≈ 30). Variance $df/(df-2)$ for df>2.

| df | t critical (95%, two-tailed) |
|---|---|
| 5 | 2.571 |
| 9 | 2.262 |
| 15 | 2.131 |
| 20 | 2.086 |
| ∞ | 1.960 |

Excel: `=T.INV.2T(0.05,9)`.

### Example
Sample of 10 lead times: $\bar{x}=12$, $s=3$. 95% CI = $12\pm2.262\times3/\sqrt{10}=12\pm2.146$ = **(9.85, 14.15)**. Using Z=1.96 would give ±1.86, too narrow, and overstate confidence.

### In the news
See news box. Small samples (early trial phases) are why t-based and Bayesian methods are used rather than normal approximations.

### Interview angle
> [!question] How it is asked
> "When do you use a t-test rather than a z-test?"

> [!tip] Strong answer includes
> - σ unknown (always in practice) and small n
> - Heavier tails; df = n − 1
> - Convergence to normal for large n
> - Assumption: data approx normal for small n

---

## 8. Chi-Square Distribution
> 🔴 Tier 1 · _Tracker hint:_ Sum of squared standard normals; used in chi-square tests, goodness of fit

### Definition
If $Z_1,\dots,Z_k$ are independent standard normals, $\chi^2_k=\sum Z_i^2$ has a **chi-square distribution** with $k$ degrees of freedom. Mean $k$, variance $2k$, right-skewed (becoming normal as $k$ grows), non-negative. Uses: tests of independence and goodness of fit ([[089 Hypothesis Testing]]), and inference on a variance: $(n-1)s^2/\sigma^2\sim\chi^2_{n-1}$.

| df | Critical value (α = 0.05, right tail) |
|---|---|
| 1 | 3.841 |
| 2 | 5.991 |
| 4 | 9.488 |
| 5 | 11.070 |

Excel: `=CHISQ.INV.RT(0.05,4)`.

### Example
A process variance claim σ² = 4. Sample n = 15 gives $s^2=9$. Statistic = 14×9/4 = **31.5**; critical value for df=14 at 5% is 23.68, so the process is more variable than claimed.

### In the news
See news box. Not tied to a specific recent event; categorical survey data (preferences, categories) is analysed with chi-square.

### Interview angle
> [!question] How it is asked
> "Where does the chi-square distribution come from, and what is it used for?"

> [!tip] Strong answer includes
> - Sum of squared standard normals, df = number of terms
> - Right-skewed, non-negative
> - Tests on categorical data and variance
> - Mean = df, so a value far above df signals poor fit

---

## 9. F-Distribution
> 🔴 Tier 1 · _Tracker hint:_ Ratio of chi-square distributions; used in ANOVA and regression F-test

### Definition
$F=\dfrac{\chi^2_{d_1}/d_1}{\chi^2_{d_2}/d_2}$ with numerator df $d_1$ and denominator df $d_2$. Right-skewed, non-negative; an F near 1 means the two variance estimates agree. Uses: **ANOVA** (variance between groups / variance within), **regression overall significance** ($F=MSR/MSE$), and **comparing two variances** ($s_1^2/s_2^2$). The upper critical value depends on both df: for example $F_{0.05}(2,12)=3.885$, $F_{0.05}(3,20)=3.098$. Excel: `=F.INV.RT(0.05,2,12)`. Note $t_{df}^2=F_{1,df}$.

### Example
Regression with 3 predictors and n = 24: df = (3, 20); suppose F = 8.4 > 3.10, so at least one predictor matters (overall model significant). Comparing two machines: $s_1^2=16$, $s_2^2=9$, $F=1.78$, below the critical value for 10, 10 df (2.98), so no evidence of different variability.

### In the news
See news box. Not tied to a specific recent event; F-tests are the backbone of comparing many groups in experiments.

### Interview angle
> [!question] How it is asked
> "What does the F statistic in a regression output tell you?"

> [!tip] Strong answer includes
> - Tests whether all slope coefficients are zero
> - Ratio of explained to unexplained variance per df
> - Look at p-value for F, then individual t-tests
> - Distinguish from R² (strength) vs F (significance)

---

## 10. Log-Normal Distribution
> 🔴 Tier 1 · _Tracker hint:_ Right-skewed; log(X)~Normal; used for stock prices, income, lead times

### Definition
$X$ is **log-normal** if $\ln X\sim N(\mu,\sigma^2)$. Always positive, right-skewed, the product of many small positive random factors (multiplicative effects), by the CLT applied to logs. Properties: median = $e^{\mu}$; mean = $e^{\mu+\sigma^2/2}$ (greater than the median); variance $(e^{\sigma^2}-1)e^{2\mu+\sigma^2}$. Used for asset prices, incomes, claim sizes, repair and lead times. Fit: take logs of data and check normality.

### Example
Lead time in days is log-normal with $\mu=1.5$, $\sigma=0.4$ on the log scale. Median = $e^{1.5}=\mathbf{4.48}$ days; mean = $e^{1.58}=\mathbf{4.85}$ days. P(lead time > 8): $\ln8=2.079$, $z=(2.079-1.5)/0.4=1.45$, so probability about **7.4%**. A normal fit would put symmetric mass on either side of the mean.

### In the news
See news box. GDP and incomes are multiplicative growth processes, hence log-scale analysis (growth rates).

### Interview angle
> [!question] How it is asked
> "Why model project cost overruns or lead times with a log-normal instead of a normal?"

> [!tip] Strong answer includes
> - Positive and right-skewed; multiplicative effects
> - Median < mean; use percentile planning
> - Fit by log transform and normality check
> - Implication for buffers (tail risk)

---

## 11. ⭐ Advanced: Newsvendor Model with Normal Demand
> ⭐ Advanced · _Added beyond the tracker_

### Definition
For a single-period perishable item with unit cost $c$, price $p$, salvage $s$: **underage cost** $C_u=p-c$, **overage cost** $C_o=c-s$. Optimal service level (critical ratio):
$$CR=\frac{C_u}{C_u+C_o},\qquad Q^*=\mu+z_{CR}\,\sigma\ \ (\text{demand} \sim N(\mu,\sigma^2))$$
Order more when the margin is high relative to the loss on leftovers. Excel: `=NORM.INV(CR, μ, σ)`.

### Example
Festival sweets: $p=100$, $c=40$, $s=10$. $C_u=60$, $C_o=30$, $CR=60/90=0.667$, $z=0.431$. Demand $N(500,80^2)$: $Q^*=500+0.431\times80=\mathbf{534.5\approx535}$ boxes. Ordering the mean (500) would under-stock; the optimal order is above the mean because underage costs twice as much.

### In the news
See news box. Fashion, e-commerce festival sales and vaccines all use critical-ratio logic with probabilistic demand.

### Interview angle
> [!question] How it is asked
> "How many units of a seasonal item should the retailer order?"

> [!tip] Strong answer includes
> - Underage and overage costs, critical ratio
> - Normal inverse for quantity
> - Intuition: stock above mean when margin exceeds markdown loss
> - Sensitivity to forecast σ

---

## 12. ⭐ Advanced: Poisson-Exponential Link and the M/M/1 Queue
> ⭐ Advanced · _Added beyond the tracker_

### Definition
If arrivals are Poisson with rate $\lambda$, inter-arrival times are exponential with mean $1/\lambda$. With exponential service at rate $\mu$ and one server (**M/M/1**), utilisation $\rho=\lambda/\mu<1$ and:
$$L_q=\frac{\rho^2}{1-\rho},\quad W=\frac{1}{\mu-\lambda},\quad W_q=\frac{\rho}{\mu-\lambda},\quad L=\lambda W\ \text{(Little's law)}$$
Waiting time rises non-linearly as utilisation approaches 100%, the reason for slack capacity.

### Example
A packing bench: arrivals $\lambda=8$/h, service $\mu=10$/h. $\rho=0.8$; $L_q=0.64/0.2=\mathbf{3.2}$ jobs waiting; $W=1/2=\mathbf{0.5}$ h (30 min) in system; $W_q=0.8/2=0.4$ h (24 min). Raising arrivals to 9/h gives $\rho=0.9$, $W=1$ h: a 12% load increase doubles the time in system.

### In the news
See news box. Not tied to a specific recent event; quick-commerce and warehouse queues are modelled this way.

### Interview angle
> [!question] How it is asked
> "Why does the queue explode when the system is almost fully utilised?"

> [!tip] Strong answer includes
> - Waiting time ∝ 1/(1−ρ)
> - Variability in arrivals and service drives waiting
> - Numeric example (80% → 90% utilisation)
> - Remedies: capacity buffer, variability reduction, pooling

---

---
## 🔗 Go deeper: expansion notes
- [[205 Sampling Distributions & Estimation|Sampling Distributions & Estimation]]
- [[217 Probability Puzzles & Applied Problem Solving|Probability Puzzles & Applied Problem Solving]]
