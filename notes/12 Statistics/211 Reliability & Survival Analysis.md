---
tags: [statistics, tier2]
area: Statistics
topic: "Reliability & Survival Analysis"
tier: Tier 2
roles: Operations / Analytics
status: complete
subtopics: 14
---
# Reliability & Survival Analysis

⬅ [[210 Bayesian Statistics for Decisions]] · [[_Index - Statistics|Statistics]] · [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Analytics

## Sub-topics in this note
1. [[#1. Time-to-Event Data, Censoring and Truncation]]
2. [[#2. Survival, Hazard and Cumulative Hazard Functions]]
3. [[#3. Kaplan-Meier Estimator: Worked Table]]
4. [[#4. Log-Rank Test: Comparing Survival Curves]]
5. [[#5. Cox Proportional Hazards: Interpretation]]
6. [[#6. Exponential Model and MTTF Estimation]]
7. [[#7. Weibull Model, Parameter Estimation and the Bathtub Curve]]
8. [[#8. Warranty and Field Failure Data Analysis]]
9. [[#9. Customer Churn and Time-to-Event Applications]]
10. [[#10. Competing Risks]]
11. [[#11. Repairable Systems: Renewal, NHPP and Crow-AMSAA]]
12. [[#12. Executed Python Workflow with lifelines]]
13. [[#13. ⭐ Advanced: AFT Models, PH Diagnostics and Time-Varying Covariates]]
14. [[#14. ⭐ Advanced: Bayesian and Sample-Size Considerations for Reliability Tests]]

## 📰 News box
> [!news] Why this matters now: age-dependent failure is still driving the world's biggest recalls
> **Takata airbag inflators: roughly 67 million air bags under recall (NHTSA page, accessed 2026).** The US safety regulator's Takata page says about 67 million air bags across 19 manufacturers are under recall, with 28 confirmed deaths in the US and at least 400 alleged injuries. The cause is propellant that degrades with long exposure to heat and humidity, so risk rises with vehicle age and hot-humid location, and NHTSA prioritised repairs by age and region ("Zone A"). A failure probability that depends on age and environment, with most cars still unfailed, is the textbook case for hazard functions, censored field data and Weibull-type wear-out models. ([NHTSA Takata recall spotlight](https://www.nhtsa.gov/equipment/takata-recall-spotlight))
>
> **Open-source tooling (lifelines documentation).** The Python `lifelines` library defines survival analysis as the study of time until an event and shows Kaplan-Meier, Cox and parametric fitters on right-censored data (cases where the event had not happened when observation ended). The same code runs customer-churn, machine-life and warranty analyses. ([lifelines docs](https://lifelines.readthedocs.io/en/latest/Survival%20analysis%20with%20lifelines.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Time-to-Event Data, Censoring and Truncation
> 🟠 Tier 2 · _Key points:_ Duration + event flag; right-censoring; left-truncation; why ordinary averages and regression mislead

### Definition
**Survival (time-to-event) analysis** models the time $T$ until an event: machine failure, customer churn, loan default, delivery completion, employee exit. Each unit contributes a **duration** and an **event indicator** (1 = event seen, 0 = censored). Ignoring censoring biases results: dropping censored units throws away the long survivors; treating censored times as failure times understates life.

Key types of incomplete observation:
- **Right-censoring** (most common): observation ends before the event (study ends, customer still active, unit withdrawn for another reason). We know $T>c$.
- **Left-censoring:** event happened before observation began (known only that $T<c$).
- **Interval-censoring:** event known to lie between two inspections (for example, a failure found at a monthly maintenance check).
- **Left truncation (delayed entry):** units enter the dataset only if they have already survived to some age, such as customers who joined before the data warehouse started. They must enter the risk set at their entry age, not at time 0, or survival is overstated.
- **Type I vs Type II censoring:** test stopped at a fixed time vs stopped after a fixed number of failures; **random censoring** covers everything else. Standard methods assume censoring is **non-informative** (independent of future failure risk). If customers leave the observation window because they are about to churn, that assumption fails.

Always build the dataset from entry date, exit date and exit reason. See [[022 Maintenance Management (TPM-RCM)]] and [[155 Reliability Engineering & Maintenance Optimisation]] for where failure data come from.

### Example
A fleet analyst has 5 pumps. Hours in service: 1,200 (failed), 2,000 (still running when the dataset was cut), 800 (failed), 2,000 (still running), 1,500 (removed for an unrelated upgrade). Naive mean of the five numbers is 1,500 h. But only 2 events were seen and three durations are lower bounds, so 1,500 h is not "mean life". The exponential estimate $\hat\lambda=\text{events}/\text{total exposure}=2/7{,}500=0.000267$ per hour gives MTTF $=3{,}750$ h, using every unit's exposure and counting only observed failures.

### In the news
See news box. In recall data most vehicles have not failed (they are right-censored at their current age), which is why regulators track failure rates by age and region instead of simple averages.

### Interview angle
> [!question] How it is asked
> "Your churn dataset has customers who are still active. How do you compute average customer lifetime without bias?"

> [!tip] Strong answer includes
> - Duration and event flag; active customers are right-censored, not zero-lifetime and not dropped
> - Use Kaplan-Meier or a parametric model, and restricted mean survival time if tail not observed
> - Mention delayed entry (left truncation) and informative censoring risks
> - Know the difference between censoring (partial info) and truncation (selection)

---
## 2. Survival, Hazard and Cumulative Hazard Functions
> 🟠 Tier 2 · _Key points:_ S(t)=P(T>t); h(t)=instantaneous failure rate given survival; H(t)=∫h; S=exp(−H)

### Definition
For a non-negative lifetime $T$ with density $f(t)$ and CDF $F(t)$:

$$S(t)=P(T>t)=1-F(t),\qquad h(t)=\lim_{\Delta t\to0}\frac{P(t\le T<t+\Delta t\mid T\ge t)}{\Delta t}=\frac{f(t)}{S(t)}$$

$$H(t)=\int_0^t h(u)\,du,\qquad S(t)=e^{-H(t)},\qquad \text{MTTF}=E[T]=\int_0^\infty S(t)\,dt$$

- **Hazard** $h(t)$ is the failure rate among those still alive at $t$; it is a rate, not a probability, and can exceed 1.
- **Hazard shapes (bathtub):** decreasing (infant mortality, burn-in), constant (random failures), increasing (wear-out). The reliability-engineering name for $S(t)$ is **reliability** $R(t)$ and for $h(t)$ the **failure rate**.
- **Median life** satisfies $S(t_{0.5})=0.5$. **B10 life** is the age by which 10% have failed, $S=0.90$ (common in bearings and tyres).
- **Mean residual life** and **conditional reliability** $R(t+x\mid t)=R(t+x)/R(t)$ matter for used equipment and warranty extensions.

Relationship to the distributions in [[088 Probability Distributions]]: exponential = constant hazard, Weibull = power-law hazard, lognormal = hump-shaped hazard.

### Example
Weibull with scale $\eta=1{,}000$ h and shape $\beta$ (hazard $h(t)=\frac{\beta}{\eta}(t/\eta)^{\beta-1}$), hazard per 1,000 h:

| Shape | At 200 h | At 800 h | Interpretation |
|---|---|---|---|
| 0.5 | 1.12 | 0.56 | Falling: infant mortality |
| 1.0 | 1.00 | 1.00 | Constant: random failures |
| 3.0 | 0.12 | 1.92 | Rising: wear-out |

With $\beta=1$ the component is "memoryless": the chance a pump survives the next 100 h is the same at any age. With $\beta=3$ a 800-h-old pump is 16 times as likely to fail next as a 200-h-old pump, which is why preventive replacement only makes sense when the hazard rises.

### In the news
See news box. Takata inflators are a rising-hazard case: risk climbs with years of heat and humidity exposure, justifying replacement campaigns ordered by age.

### Interview angle
> [!question] How it is asked
> "What is the difference between a failure probability and a hazard rate? When does preventive replacement make sense?"

> [!tip] Strong answer includes
> - Hazard is conditional on survival so far; relate $f$, $S$, $h$, $H$
> - Bathtub shapes and the Weibull shape parameter meaning
> - Replacement only pays if hazard rises (and replacement cost is below failure cost)
> - Constant hazard means age-based maintenance is pointless; use condition monitoring instead

---
## 3. Kaplan-Meier Estimator: Worked Table
> 🟠 Tier 2 · _Key points:_ S(t)=Π(1−dᵢ/nᵢ) at event times; censored units leave the risk set; median = first S ≤ 0.5

### Definition
The **Kaplan-Meier (product-limit) estimator** is the standard non-parametric estimate of $S(t)$ with censored data:

$$\hat S(t)=\prod_{t_i\le t}\left(1-\frac{d_i}{n_i}\right)$$

where $d_i$ is the number of events at time $t_i$ and $n_i$ the number still **at risk** just before $t_i$ (not yet failed or censored). The curve is a step function that only drops at event times. Censored observations cause no drop, but they reduce the risk set afterwards. By convention a censoring at the same time as an event is treated as occurring just after it. **Greenwood's formula** gives variance: $\widehat{\text{Var}}[\hat S(t)]=\hat S(t)^2\sum \frac{d_i}{n_i(n_i-d_i)}$. The **median survival time** is the smallest $t$ with $\hat S(t)\le0.5$; if the curve never falls to 0.5 the median is undefined, and restricted mean survival time up to a horizon is reported instead.

### Example
Tenure in months for 12 subscribers (1 = churned, 0 = censored/still active): 2, 3, 3+, 5, 6+, 7, 7, 8+, 9, 11+, 12, 12+ (the "+" marks censored).

| Time $t_i$ | At risk $n_i$ | Events $d_i$ | Censored | $1-d_i/n_i$ | $\hat S(t_i)$ |
|---|---|---|---|---|---|
| 2 | 12 | 1 | 0 | 0.9167 | 0.9167 |
| 3 | 11 | 1 | 1 | 0.9091 | 0.8333 |
| 5 | 9 | 1 | 0 | 0.8889 | 0.7407 |
| 6 | 8 | 0 | 1 | 1 | 0.7407 |
| 7 | 7 | 2 | 0 | 0.7143 | 0.5291 |
| 8 | 5 | 0 | 1 | 1 | 0.5291 |
| 9 | 4 | 1 | 0 | 0.75 | 0.3968 |
| 11 | 3 | 0 | 1 | 1 | 0.3968 |
| 12 | 2 | 1 | 1 | 0.5 | 0.1984 |

- Median survival $=9$ months (first time $\hat S\le0.5$).
- At $t=9$, Greenwood gives SE $=0.164$ and a 95% interval of about $[0.08,\,0.72]$, very wide with 12 customers (lifelines uses a log-log transform and reports $[0.11,\,0.68]$). Wide bands are the honest message of small samples.
- 12-month retention estimate: 19.8%. A naive count of customers observed to reach month 12 (2 of 12 = 16.7%) understates retention, because customers censored earlier are counted as if they had left.

### In the news
See news box. Field recall and warranty datasets are dominated by right-censored units, so Kaplan-Meier style estimators (or their parametric cousins) are the first thing an analyst runs.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would estimate 12-month retention when many customers joined only recently."

> [!tip] Strong answer includes
> - Kaplan-Meier: at each churn time multiply survival by (1 − events/at risk); censored customers leave the risk set
> - Why a simple ratio of churners to joiners is biased low (recent joiners cannot have churned yet)
> - Report confidence band and median/restricted mean
> - Compare groups with the log-rank test

---
## 4. Log-Rank Test: Comparing Survival Curves
> 🟠 Tier 2 · _Key points:_ Compares observed vs expected events across groups at each event time; chi-square, 1 df for 2 groups

### Definition
The **log-rank test** tests $H_0$: the survival curves of two (or more) groups are identical, using all event times. At each distinct event time $t_j$ with $N_j$ at risk in total, $d_j$ events overall and $n_{Aj}$ at risk in group A, the expected events in A under $H_0$ are $E_{Aj}=d_j\,n_{Aj}/N_j$, and the hypergeometric variance is $V_j=d_j\frac{n_{Aj}}{N_j}\frac{n_{Bj}}{N_j}\frac{N_j-d_j}{N_j-1}$. Then

$$\chi^2=\frac{\left(\sum_j (d_{Aj}-E_{Aj})\right)^2}{\sum_j V_j}\;\sim\;\chi^2_{1}$$

It is the most powerful test when hazards are proportional (curves do not cross); if curves cross, use Wilcoxon/Gehan or Fleming-Harrington weights, or restricted mean survival time. It is a **test, not an effect size**: pair it with a hazard ratio from Cox. Compare with the tests of [[089 Hypothesis Testing]] and rank-based logic in [[206 Non-Parametric Tests]].

### Example
Months to churn, two plans, + = censored:
Plan A (8 customers): 3, 5, 7, 9, 12+, 14, 16+, 18+. Plan B (8 customers): 1, 2, 3, 4, 6, 8, 10+, 13.

Event times and expected events in A (partial table):

| $t$ | At risk A / B | Events A / B | $E_A$ | $V$ |
|---|---|---|---|---|
| 1 | 8 / 8 | 0 / 1 | 0.500 | 0.250 |
| 2 | 8 / 7 | 0 / 1 | 0.533 | 0.249 |
| 3 | 8 / 6 | 1 / 1 | 1.143 | 0.452 |
| 4 | 7 / 5 | 0 / 1 | 0.583 | 0.243 |
| 5 | 7 / 4 | 1 / 0 | 0.636 | 0.231 |
| ... | | | | |
| 14 | 3 / 0 | 1 / 0 | 1.000 | 0.000 |

Totals over all 11 event times: observed in A $O_A=5$, expected $E_A=7.75$, $\sum V=2.514$. $\chi^2=(5-7.75)^2/2.514=\mathbf{3.01}$, $p=\mathbf{0.083}$. Plan A had fewer churns than expected, but with 16 customers the evidence is not significant at 5%; this is a power problem, not proof of no difference. (Verified with `lifelines.statistics.logrank_test`.)

### In the news
See news box. Regulators comparing failure experience across vehicle batches, model years or regions rely on the same logic of comparing observed and expected failures at each age.

### Interview angle
> [!question] How it is asked
> "Two onboarding flows; how do you test whether customers stay longer with the new one?"

> [!tip] Strong answer includes
> - Kaplan-Meier curves by arm and a log-rank test; Cox model for the hazard ratio with CI
> - Proportional hazards assumption: check for crossing curves
> - Handle censoring (users still active) instead of comparing average days so far
> - Plan sample size by number of events, not number of users

---
## 5. Cox Proportional Hazards: Interpretation
> 🟠 Tier 2 · _Key points:_ h(t|x)=h₀(t)·exp(βx); exp(β)=hazard ratio; semi-parametric; check PH assumption

### Definition
The **Cox model** relates covariates to the hazard without specifying the baseline shape:

$$h(t\mid x)=h_0(t)\,\exp(\beta_1x_1+\dots+\beta_px_p)$$

Estimation uses the **partial likelihood** (only the ordering of events matters), so $h_0(t)$ is left unspecified. Interpretation:
- $e^{\beta_j}$ is the **hazard ratio (HR)** for a one-unit increase in $x_j$, holding others fixed. HR = 2 means twice the instantaneous risk at every point in time; HR < 1 is protective.
- It is **not** "twice as likely to ever churn" and not "half the lifetime"; it is a rate ratio at each moment. For a binary $x$, $\text{HR}=e^\beta$; for a $k$-unit change, $e^{k\beta}$.
- **Proportional hazards (PH) assumption:** HR is constant over time. Check with Schoenfeld-residual tests/plots and log-log plots; if violated, stratify on the variable, add time interaction, or use AFT models (sub-topic 13).
- **Concordance index** measures ranking quality (0.5 random, 1 perfect). **Predicted survival** for any profile $=S_0(t)^{\exp(\beta x)}$.
- Like regression (see [[090 Regression Analysis]]) it needs enough events per covariate (a rough rule is about 10 events per predictor), watch collinearity and report CIs.

### Example
Executed `lifelines` fit on a **simulated** telecom dataset (600 customers, 24-month window, 260 churn events; true hazard ratios set to 2.0 for month-to-month and 1.3 per early complaint):

| Covariate | Coef | HR $=e^{\text{coef}}$ | 95% CI for HR |
|---|---|---|---|
| Month-to-month plan | 0.811 | **2.25** | 1.73 to 2.92 |
| Complaints (per complaint) | 0.262 | **1.30** | 1.16 to 1.45 |

- Reading: at any tenure, a month-to-month customer churns at 2.25 times the rate of a contract customer with the same complaints; each complaint adds 30% to the rate (two complaints: $1.30^2=1.69$).
- Concordance 0.63 (modest ranking power, typical for churn); PH test p-values 0.54 and 0.98, so no evidence against proportional hazards.
- Predicted 12-month survival: month-to-month with 2 complaints **64.3%**; contract with none **89.0%**. The plain KM at 12 months is 69.9% for month-to-month and 85.8% for contract.
- Our CI contains the true value 2.0, as it should about 95% of the time.

### In the news
See news box. Age and environment (heat, humidity) act as covariates on a hazard in recall risk models; Cox-type models are the standard way to quantify such effects.

### Interview angle
> [!question] How it is asked
> "A Cox model gives HR = 1.8 for customers acquired through discount coupons. How do you explain this to the marketing head?"

> [!tip] Strong answer includes
> - At any point in time, coupon customers leave at 1.8 times the rate of comparable others (with CI)
> - It is not a probability of eventually churning; translate to survival curves at 6/12 months
> - Mention proportional hazards check and confounding (observational data)
> - Suggest retention actions or a test; link to [[214 Causal Inference & Experimentation Beyond A-B Tests]] for causal claims

---
## 6. Exponential Model and MTTF Estimation
> 🟠 Tier 2 · _Key points:_ Constant hazard λ; MLE λ̂=r/T_total; MTTF=1/λ; chi-square confidence interval

### Definition
The **exponential model** has $h(t)=\lambda$, $S(t)=e^{-\lambda t}$, $\text{MTTF}=1/\lambda$ and is memoryless. It fits electronic parts in their useful life and events in a Poisson process (see [[088 Probability Distributions]]). With $r$ observed failures and **total time on test** $T_{tot}=\sum$ (all durations, failed and censored), the maximum-likelihood estimate is

$$\hat\lambda=\frac{r}{T_{tot}},\qquad \widehat{\text{MTTF}}=\frac{T_{tot}}{r}$$

An exact two-sided $100(1-\alpha)\%$ interval for MTTF in a time-terminated test is $\left[\frac{2T_{tot}}{\chi^2_{\alpha/2,\,2r+2}},\;\frac{2T_{tot}}{\chi^2_{1-\alpha/2,\,2r}}\right]$ (with chi-square upper-tail percentage points). Zero-failure tests give only a one-sided lower bound: $\text{MTTF}_{L}=2T_{tot}/\chi^2_{\alpha,2}$, which is the logic of "demonstration" tests. Distinguish **MTTF** (non-repairable) from **MTBF** (repairable, between failures). Use [[155 Reliability Engineering & Maintenance Optimisation]] for system-level reliability (series, parallel).

### Example
20 identical sensors are tested for 1,000 h. 10 fail at 120, 210, 260, 340, 420, 515, 600, 720, 810 and 950 h; 10 survive (censored at 1,000 h).
- Total time on test $=\text{sum of failure times}+10\times1000=4{,}945+10{,}000=14{,}945$ h.
- $\hat\lambda=10/14{,}945=6.69\times10^{-4}$ per hour, MTTF $=\mathbf{1{,}494.5}$ h.
- 95% CI for MTTF: $[813,\;3{,}117]$ h, wide because only 10 failures.
- $R(500)=e^{-500/1494.5}=71.6\%$. (The data show a hint of wear-out, so see the Weibull fit next.)
- Wrong shortcut: averaging failure times alone gives 494.5 h, which understates life by a factor of 3.

### In the news
See news box. Where hazard is not constant (inflators aging with humidity) the exponential assumption fails; this is why analysts test the shape parameter before using MTTF.

### Interview angle
> [!question] How it is asked
> "15 of 40 units failed in a 2,000-hour test. How do you estimate MTBF and what does it mean?"

> [!tip] Strong answer includes
> - Total time on test (failed plus survivor hours) divided by number of failures, not average failure time
> - Valid only if hazard is constant; confirm with a Weibull shape near 1
> - Give a confidence interval (chi-square) and note MTBF is not "expected life" for units that wear out
> - Use for repairable-system availability: $A=\text{MTBF}/(\text{MTBF}+\text{MTTR})$

---
## 7. Weibull Model, Parameter Estimation and the Bathtub Curve
> 🟠 Tier 2 · _Key points:_ S(t)=exp(−(t/η)^β); β<1 infant, =1 random, >1 wear-out; MLE or Weibull plot; B10 life

### Definition
The **Weibull distribution** with scale (characteristic life) $\eta$ and shape $\beta$:

$$S(t)=\exp\!\left[-\left(\frac{t}{\eta}\right)^{\beta}\right],\quad h(t)=\frac{\beta}{\eta}\left(\frac{t}{\eta}\right)^{\beta-1},\quad \text{MTTF}=\eta\,\Gamma\!\left(1+\frac1\beta\right)$$

At $t=\eta$ survival is $e^{-1}=36.8\%$ regardless of $\beta$ (63.2% fail). $\beta$ in the field: bearings 1.5 to 2 or more, corrosion/fatigue 2 to 4, electronics near 1, early defects below 1.
**Estimation:**
- **Maximum likelihood** with censoring (what software like `lifelines`, Minitab, Reliasoft reports); needs numerical optimisation.
- **Weibull probability plot / median-rank regression:** plot $\ln(-\ln(1-F))$ vs $\ln t$; slope $=\beta$, intercept gives $\eta$ (classic exam method, with Bernard's median ranks $F_i=(i-0.3)/(n+0.4)$). Straight line = Weibull fits.
- **Three-parameter Weibull** adds a failure-free location shift $\gamma$. Mixed populations (batches/failure modes) show as bends; fit separate modes.
- The **bathtub curve** is the sum of decreasing (early life), constant (random) and increasing (wear-out) hazards; burn-in screening cuts the first part, preventive replacement the last.

### Example
Same 20-sensor test as sub-topic 6. Weibull MLE with censoring gives $\hat\beta=1.36$ (SE 0.39) and $\hat\eta=1{,}287$ h:
- Mean life $=\eta\Gamma(1+1/\beta)=1{,}178$ h (below the exponential 1,495 h, since failures bunch up late).
- $R(500)=75.9\%$, $R(1000)=49.2\%$ (observed: 10 of 20 = 50% still running at 1,000 h, consistent).
- B10 life $=\eta(-\ln0.9)^{1/\beta}=\mathbf{247}$ h.
- Median-rank regression on the 10 failures gives $\beta\approx1.39$, $\eta\approx1{,}189$ h, close to MLE.
- The approximate 95% CI for $\beta$ ($1.36\pm1.96\times0.39$, about 0.59 to 2.14) includes 1, and the AIC (168.2 exponential vs 169.2 Weibull) does not favour the extra parameter, so there is only weak evidence of wear-out with 10 failures. State this honestly; do not claim wear-out from this sample.

### In the news
See news box. Takata-type degradation is a wear-out mechanism: modelling the hazard with $\beta>1$ and an environment covariate is how repair priorities by age are justified.

### Interview angle
> [!question] How it is asked
> "What does the Weibull shape parameter tell you and how would you use it to choose a maintenance policy?"

> [!tip] Strong answer includes
> - $\beta<1$, $=1$, $>1$ meanings and the bathtub curve
> - Preventive replacement only if $\beta>1$; burn-in if $\beta<1$
> - Estimation by MLE with censoring, or a Weibull plot; B10 life and characteristic life
> - Uncertainty: with few failures the CI on $\beta$ is wide; check fit before deciding

---
## 8. Warranty and Field Failure Data Analysis
> 🟠 Tier 2 · _Key points:_ Age-at-failure + age of non-failures; time-in-service vs calendar time; reporting delay; expected claims and cost

### Definition
Warranty data record claims, but the population at risk is the full fleet. Good practice:
- **Use time-in-service** (months since sale or hours of use), not calendar month of claim. Units sold at different dates have different exposure; units without claims are **right-censored at their current age** (cut-off date minus sale date).
- Build the dataset from **sales (population)** plus **claims**, not claims alone; claims-only data suffers from "sales mix" confusion and look like failure rates rising when more units were simply sold.
- **Reporting delay** means recent claims are undercounted: apply delay-adjusted (IBNR-like) corrections.
- **Usage vs age:** two-dimensional warranties (12 months or 15,000 km, whichever first) need usage-rate models; many cars run well below the km limit.
- **Failure modes:** analyse each mode separately (competing risks, sub-topic 10); a mixed-mode Weibull plot shows bends.
- **Outputs:** cumulative claim rate by age, forecast of expected claims, **cost of warranty per unit**, early-warning detection of a bad batch (use 8D and containment; see [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]).

Expected claims in the warranty window $W$: $N\,F(W)$, cost $=N\,F(W)\,c$ if each unit fails at most once and each claim costs $c$ (with repairable items, count renewals).

### Example
10,000 units sold; component life assumed Weibull with $\beta=2.0$ and $\eta=60$ months (assumed values for illustration; estimate from data in practice). 12-month warranty, ₹8,000 average claim cost:
- $F(12)=1-\exp[-(12/60)^2]=3.92\%$, so $392$ expected claims.
- Cost $=392\times\text{₹}8{,}000=$ **₹31.4 lakh** (about ₹314 per unit sold, to be accrued as a warranty provision).
- B5 life $=60\times(-\ln0.95)^{1/2}=13.6$ months: 5% fail by about month 14, a design target an OEM can compare with competitors.
- If a supplier change moved $\eta$ to 45 months, $F(12)=1-\exp[-(12/45)^2]=6.9\%$, and cost rises to ₹55 lakh; this is the quantitative case for supplier quality.

### In the news
See news box. Takata shows the end state of a field failure that appears only after years: warranties expired, the population heavily censored, and regulators using age-and-region analysis to rank repair urgency.

### Interview angle
> [!question] How it is asked
> "Warranty claims on a new model rose 40% last quarter. How do you tell whether quality has deteriorated?"

> [!tip] Strong answer includes
> - Normalise by units at risk and time-in-service; cumulative claim rates by sales-month cohort
> - Adjust for reporting delay and sales-mix changes; compare cohorts at the same age
> - Break down by failure mode, supplier lot, plant, region
> - Convert to rupee cost and trigger containment/8D if a cohort is worse

---
## 9. Customer Churn and Time-to-Event Applications
> 🟠 Tier 2 · _Key points:_ Survival beats binary churn classifier for "when" and for censored data; CLV from S(t); time-varying covariates

### Definition
Churn is naturally a time-to-event problem. Compared with a logistic model that predicts "churn within 90 days" (see [[096 Classification Algorithms]]), survival analysis:
- uses **all customers**, including recent joiners (censored), without arbitrary label windows;
- gives a **survival curve per customer**, so retention at any horizon and **expected remaining lifetime** are available;
- shows **when** risk peaks (for example, at contract renewal or at 30 days), which guides intervention timing;
- supports **time-varying covariates** (usage last month, a new complaint) via counting-process data.

**Customer lifetime value** from survival: $\text{CLV}=\sum_{t=1}^{H} m\,\frac{\hat S(t)}{(1+d)^{t}}$ for monthly margin $m$ and discount rate $d$. Applications beyond telecom: subscription and OTT retention, loan default and prepayment, employee attrition, time-to-first-purchase, delivery-time modelling, equipment remaining useful life, time-to-fill job vacancies, stockout time.

### Example
From the simulated churn fit of sub-topic 5: 12-month retention is 69.9% for month-to-month customers and 85.8% for contract customers. The area under each KM curve up to 12 months (restricted mean survival time) is 10.16 months for month-to-month and 11.05 months for contract, a gap of 0.90 months of paying tenure in year one. At ₹300 monthly margin that is about **₹270 of extra margin per customer in year one**, less than a ₹600 conversion incentive. A year-one view says no; but the retention gap persists, so a two-to-three-year CLV horizon (if a similar gap recurred each year, break-even takes about 2.2 years) may say yes. The survival model puts the trade-off in numbers, which a one-off churn flag cannot. (The comparison is observational; whether converting a customer would actually produce the contract-customer curve is a causal question, see [[214 Causal Inference & Experimentation Beyond A-B Tests]].)

```python
from lifelines import KaplanMeierFitter, CoxPHFitter
# df: tenure (months), churned (0/1), covariates
cph = CoxPHFitter().fit(df, "tenure", "churned")
cph.predict_survival_function(df.iloc[:5], times=[3, 6, 12])
cph.predict_expectation(df.iloc[:5])   # restricted expected lifetime
```

### In the news
See news box. The `lifelines` documentation covers the same tooling for churn as for medical and mechanical lifetimes, one reason data teams adopt it for subscription analytics.

### Interview angle
> [!question] How it is asked
> "Why would you use survival analysis instead of a churn classifier?"

> [!tip] Strong answer includes
> - Censoring, timing of risk, expected lifetime and CLV, time-varying covariates
> - Mention hazard-based targeting: act where hazard peaks
> - Honest about limits: observational, non-informative censoring, need for enough events
> - Link to [[031 Product Metrics & Analytics]] retention curves and [[100 ML for Product Management]]

---
## 10. Competing Risks
> 🟠 Tier 2 · _Key points:_ Several event types preclude each other; 1−KM overstates; use cumulative incidence (Aalen-Johansen); cause-specific vs Fine-Gray

### Definition
In **competing risks** a unit can end in one of several mutually exclusive ways: churn by choice vs non-payment, failure by mode A vs B, death vs relapse, loan default vs prepayment. Treating other causes as censored and computing $1-\text{KM}$ for the event of interest **overstates** its probability, because KM pretends the competing-event units could still have had the event of interest.

Correct tools:
- **Cumulative incidence function (CIF)** $F_k(t)=P(T\le t,\text{cause}=k)$, estimated by **Aalen-Johansen**; CIFs across causes plus survival sum to 1.
- **Cause-specific hazard** $h_k(t)$: models the rate of cause $k$ among those still event-free; fit a Cox model per cause (right for etiology and "what drives churn type").
- **Fine-Gray subdistribution hazard**: models the CIF directly (right for predicting the absolute probability of cause $k$).

### Example
A subscription business: voluntary churn hazard 1/30 per month, involuntary (payment failure) 1/60 per month (simulated, 500 customers, followed up to 24 months; 222 voluntary, 126 involuntary, 152 censored).
- Naive $1-\text{KM}$ for voluntary churn at 24 months: **53.5%** (theory 55.1%).
- Correct Aalen-Johansen CIF for voluntary churn at 24 months: **44.4%** (theory 46.6%; sample noise explains the gap) and 25.2% for involuntary.
- Exact formula for constant hazards: $\text{CIF}_v(24)=\frac{\lambda_v}{\lambda_v+\lambda_i}\left(1-e^{-(\lambda_v+\lambda_i)24}\right)=\frac{1/30}{1/20}\left(1-e^{-24/20}\right)=0.667\times0.699=46.6\%$.
Fixing the payment failures (reducing involuntary churn) would raise the share of customers who reach the voluntary-churn decision, a trade-off invisible in a one-cause model.

### In the news
See news box. In recalls, a car can leave the population by being scrapped, sold abroad or repaired (competing exits), so analysts must model who is still at risk.

### Interview angle
> [!question] How it is asked
> "You report that 55% of customers eventually churn voluntarily, but finance sees only 45%. What could explain it?"

> [!tip] Strong answer includes
> - Competing events (involuntary churn) were censored in KM; use CIF
> - Cause-specific hazard for drivers; Fine-Gray or CIF for absolute probabilities
> - Show the sum of all causes plus survival equals one
> - Apply to failure modes, default vs prepayment

---
## 11. Repairable Systems: Renewal, NHPP and Crow-AMSAA
> 🟠 Tier 2 · _Key points:_ Repairable = count failures in time; HPP constant rate; NHPP power law N(t)=λtᵝ; β>1 deteriorating; trend tests

### Definition
For a **repairable system** (machine, truck, ATM) the same unit fails repeatedly, so we model the **count** of failures $N(t)$, not a single lifetime.
- **HPP (homogeneous Poisson process):** constant intensity $\lambda$, independent identically distributed exponential gaps ($\beta=1$); equivalent to "as good as new" or random failures. MTBF $=1/\lambda$.
- **Renewal process:** repair restores to as-good-as-new; gaps iid with any distribution.
- **NHPP (non-homogeneous Poisson process):** intensity changes with age, repair is "minimal" ("as bad as old"). **Power-law NHPP (Crow-AMSAA):** expected failures $\Lambda(t)=\lambda t^\beta$, intensity $u(t)=\lambda\beta t^{\beta-1}$. $\beta>1$ deterioration, $\beta<1$ reliability growth (design fixes work), $\beta=1$ stable.
- For time-truncated data observed to $T$ with failure times $t_1,\dots,t_n$: $\hat\beta=\dfrac{n}{\sum\ln(T/t_i)}$, $\hat\lambda=n/T^{\hat\beta}$ (a bias-corrected $\hat\beta$ is $\frac{n-1}{n}\hat\beta$). **Laplace trend test:** $U=\dfrac{\bar t-T/2}{T\sqrt{1/(12n)}}$, approximately $N(0,1)$ under HPP; $U>1.96$ signals deterioration.
- Use the intensity, not the average gap, to plan spares, overhaul timing and replace-or-repair decisions (see [[022 Maintenance Management (TPM-RCM)]] and [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]] for the data trail).

### Example
A truck's engine failures (hours) over a 2,000-h observation: 410, 820, 1,100, 1,290, 1,440, 1,560, 1,670, 1,760, 1,830, 1,890, 1,940, 1,980 ($n=12$). Gaps shrink from 410 h to about 40 h.
- $\sum\ln(T/t_i)=4.584$; $\hat\beta=12/4.584=\mathbf{2.62}$ (bias-corrected 2.40), $\hat\lambda=2.74\times10^{-8}$.
- Current intensity $u(2000)=0.0157$ per hour, so **instantaneous MTBF $\approx64$ h**, versus the naive $T/n=167$ h.
- Expected failures in the next 500 h: $\hat\lambda(2500^{\hat\beta}-2000^{\hat\beta})=\mathbf{9.5}$, versus 3.0 if one wrongly assumed a constant rate.
- Laplace $U=2.85$ ($p=0.004$): strong evidence of deterioration. Action: overhaul or replace the engine instead of repairing again. Compare repair cost per failure with replacement cost amortised over remaining life.

### In the news
See news box. Fleet and aircraft operators track failure intensity versus age per unit for exactly this reason; the pattern of shrinking gaps is the signal to retire an asset.

### Interview angle
> [!question] How it is asked
> "A machine's breakdowns are becoming more frequent. How do you decide whether to keep repairing or replace it?"

> [!tip] Strong answer includes
> - Count-based model, not lifetime: NHPP power law, β>1 means deterioration
> - Trend test (Laplace), instantaneous MTBF, expected failures and repair cost forecast
> - Compare cumulative repair cost with replacement; consider downtime cost
> - Warn that average MTBF hides trends

---
## 12. Executed Python Workflow with lifelines
> 🟠 Tier 2 · _Key points:_ KaplanMeierFitter, logrank_test, CoxPHFitter, WeibullFitter; check PH; report HR with CI and survival curves

### Definition
Library `lifelines` (pip install lifelines) covers the standard pipeline: `KaplanMeierFitter` (non-parametric), `logrank_test` / `multivariate_logrank_test`, `CoxPHFitter` (+ `check_assumptions`, `proportional_hazard_test`), `WeibullFitter`, `ExponentialFitter`, `LogNormalFitter`, `WeibullAFTFitter`, `AalenJohansenFitter`. Data needs two columns: duration and event (1 = observed, 0 = censored), plus covariates. Workflow: (1) clean and define entry/exit and reason; (2) KM by key segments; (3) log-rank; (4) Cox with CIs and PH check; (5) parametric fit for extrapolation (compare AIC); (6) translate to business (retention at 3/6/12 months, expected cost). Pair with [[067 Statistical Analysis in Python]] and [[064 Pandas — Data Manipulation]].

### Example
Executed code (seeded simulated churn data) and its output:

```python
import numpy as np, pandas as pd
from lifelines import KaplanMeierFitter, CoxPHFitter
from lifelines.statistics import logrank_test, proportional_hazard_test

rng = np.random.default_rng(2026)
n = 600
mtm = rng.binomial(1, 0.55, n)            # 1 = month-to-month plan
comp = rng.poisson(1.0, n)                # complaints in first 3 months
xb = np.log(2.0) * mtm + np.log(1.3) * comp
t_true = (-np.log(rng.random(n)) / (0.008 * np.exp(xb))) ** (1 / 1.1)   # Weibull PH
df = pd.DataFrame({"tenure": np.minimum(t_true, 24).round(2),
                   "churned": (t_true <= 24).astype(int),
                   "month_to_month": mtm, "complaints": comp})

cph = CoxPHFitter().fit(df, "tenure", "churned")
cols = ["exp(coef)", "exp(coef) lower 95%", "exp(coef) upper 95%", "p"]
print(cph.summary[cols].round(3))
print(round(cph.concordance_index_, 3))
print(proportional_hazard_test(cph, df, time_transform="rank").summary.round(3))
```

Output: HR month-to-month **2.25** (1.73 to 2.92), complaints **1.30** (1.16 to 1.45), concordance **0.629**, PH-test p = 0.975 and 0.540 (assumption holds), KM 12-month retention 85.8% (contract) vs 69.9% (month-to-month), log-rank $\chi^2=35.9$ (p far below 0.001). Because the data are simulated with known HRs of 2.0 and 1.3, the fit recovers them. On real data, never expect such clean recovery; expect messier PH checks and report assumptions.

### In the news
See news box. The `lifelines` docs show the same fitters across medicine, politics and engineering, which is why one workflow serves reliability and churn teams.

### Interview angle
> [!question] How it is asked
> "Describe the steps you would follow to analyse customer retention with survival analysis in Python."

> [!tip] Strong answer includes
> - Data layout (duration, event, covariates), censoring definition, delayed entry
> - KM → log-rank → Cox (HR with CI, PH check) → parametric extrapolation
> - Business translation: retention at horizons, CLV, intervention timing
> - Pitfalls: informative censoring, immortal time bias, too few events

---
## 13. ⭐ Advanced: AFT Models, PH Diagnostics and Time-Varying Covariates
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Accelerated failure time (AFT)** models say covariates stretch or shrink time: $\ln T=\mu+\gamma x+\sigma\varepsilon$. $e^{\gamma}$ is a **time ratio** (acceleration factor): 0.5 means lifetimes are half as long. For the Weibull distribution only, PH and AFT coincide, with $\text{HR}=e^{-\beta_{shape}\gamma}$ (shape $\rho$). AFT gives interpretable time effects, full parametric predictions and extrapolation, and avoids the PH assumption (log-normal and log-logistic AFT can have non-monotone hazards). **Arrhenius/Eyring and power-law acceleration** in reliability testing are AFT models: raising temperature to age parts faster and extrapolating to use conditions.

**PH diagnostics:** scaled Schoenfeld residuals vs time (flat line = OK), log-minus-log curves (parallel = OK), the statistical test (weak in small samples, overpowered in big ones). Remedies: stratify; add $x\times\log t$ interaction; split follow-up into periods; AFT; restricted mean survival time difference (no PH needed).
**Time-varying covariates** (lifelines `CoxTimeVaryingFitter`): data are in "long" format with start-stop rows per customer. Beware **immortal-time bias** (classifying someone as "treated" using future information). Also: **frailty/shared-frailty** models for clusters (machines in a plant), and **cure models** for populations in which some never fail.

### Example
Weibull AFT on the same simulated churn data gives time ratios **0.486** for month-to-month (their expected tenure is about half) and **0.792** per complaint, with shape $\hat\rho=1.12$. Convert to Cox-style HR: $e^{-1.12\times(-0.721)}=2.24$ and $e^{-1.12\times(-0.233)}=1.30$, matching Cox (2.25 and 1.30). Two languages, one fit: "churn rate is 2.25 times higher" equals "time to churn is about half as long".

### In the news
See news box. Accelerated life tests (heat, vibration, humidity) used to qualify components for recall-prone environments are AFT models in practice.

### Interview angle
> [!question] How it is asked
> "What do you do if the proportional hazards assumption fails in your Cox model?"

> [!tip] Strong answer includes
> - Diagnose with Schoenfeld residuals and plots; avoid relying only on p-values
> - Stratify, time interaction, split follow-up, or AFT/RMST alternatives
> - Know HR vs time ratio and when the Weibull makes them equivalent
> - Mention time-varying covariates and immortal-time bias

---
## 14. ⭐ Advanced: Bayesian and Sample-Size Considerations for Reliability Tests
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Reliability testing is expensive and failures are rare, so planning matters.
- **Zero-failure (success-run) test:** to demonstrate reliability $R$ at confidence $C$ with no failures, the needed number of units is $n=\dfrac{\ln(1-C)}{\ln R}$. For 90% reliability at 90% confidence, $n=22$; for 95% at 90%, $n=45$; for 99% at 95%, $n=299$.
- **Weibayes:** assume a plausible shape $\beta$ from past data and estimate $\eta$ even with zero or few failures: $\hat\eta=\left(\frac{\sum t_i^{\beta}}{r}\right)^{1/\beta}$ for $r\ge1$ (lower bound with $r=0$ using a chi-square factor). Useful in warranty early warnings.
- **Events, not subjects, drive power:** for a log-rank/Cox comparison the required number of events is about $d=\frac{4(z_{\alpha/2}+z_{\beta})^2}{(\ln \text{HR})^2}$ for equal groups (Schoenfeld). For HR = 0.7, 80% power, two-sided 5%: $d=4(1.96+0.84)^2/(\ln0.7)^2\approx 247$ events.
- **Bayesian reliability:** conjugate Gamma-Exponential updates (rate $\lambda$ with Gamma prior; see [[210 Bayesian Statistics for Decisions]]) let engineers combine a prior from similar products with a few test failures and report probability that MTBF exceeds a contractual level.
- **Accelerated tests** extend limited time by stress levels, but the acceleration model must be validated.

### Example
Success-run: to show 95% reliability with 90% confidence over a 1,000-h mission, $n=\ln(0.10)/\ln(0.95)=44.9\to45$ units, all surviving 1,000 h. Test cost 45 units × ₹40,000 = ₹18 lakh. If the OEM instead runs 20 units to 1,000 h and sees 10 failures, the Weibull analysis of sub-topic 7 applies, but the lower confidence bound is far weaker. The Bayesian alternative with a Gamma prior equivalent to 3 failures in 6,000 h (from a previous design) and the same data (10 failures in 14,945 h) gives posterior $\text{Gamma}(13,\,20{,}945)$ for $\lambda$ (shape $3+10$, rate $6{,}000+14{,}945$), posterior mean $\lambda=13/20945=6.2\times10^{-4}$ per hour, equivalent to an MTBF of about 1,611 h (the reciprocal of the mean rate), a little above the 1,495 h likelihood-only estimate because the prior was optimistic.

### In the news
See news box. Recall costs on the scale of tens of millions of units are the commercial argument for investing in better test design before launch.

### Interview angle
> [!question] How it is asked
> "How many units must we test, and for how long, to prove a 95% reliability claim?"

> [!tip] Strong answer includes
> - Success-run formula with confidence level, effect of allowing failures
> - Events drive power; use Weibayes or Bayesian priors if data are scarce
> - Accelerated testing with validated acceleration model
> - Trade-off: test cost vs expected recall/warranty cost
