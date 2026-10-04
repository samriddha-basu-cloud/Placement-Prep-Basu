---
tags: [statistics, tier2]
area: Statistics
topic: "Sampling & Experimental Design"
tier: Tier 2
roles: All Roles
status: complete
subtopics: 10
---
# Sampling & Experimental Design

⬅ [[091 Statistical Quality Control (SQC)]] · [[_Index - Statistics|Statistics]] · [[093 Business Statistics Applications]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Sampling Methods]]
2. [[#2. Sample Size Determination]]
3. [[#3. Confidence Intervals]]
4. [[#4. Design of Experiments (DOE)]]
5. [[#5. Randomized Block Design]]
6. [[#6. Latin Square Design]]
7. [[#7. Response Surface Methodology]]
8. [[#8. A/B Testing Statistics]]
9. [[#9. ⭐ Advanced: Design Effect, Non-Response Bias and Weighting]]
10. [[#10. ⭐ Advanced: Pitfalls in A/B Testing: Peeking, Multiple Comparisons, Variance Reduction]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's Census 2027 and the new CPI, sampling and enumeration at national scale
> **Census 2027 (houselisting began April 2026).** India's first digital census runs in two phases: Houselisting and Housing Census from **April to September 2026** (30 days per State/UT, with an optional 15-day self-enumeration window), and Population Enumeration in **February 2027** (reference date 1 March 2027). It uses about **31 lakh enumerators and supervisors**, mobile apps in 16 languages, a budget of **₹11,718.24 crore**, and for the first time a full caste enumeration. A census is a complete enumeration (no sampling error), but it still faces non-sampling errors such as non-response. ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2255461&reg=3&lang=1))
> 
> **New CPI price sampling (Feb 2026).** The 2024-base CPI collects prices from **1,465 rural and 1,395 urban markets across 434 towns**, plus weekly data from **12 e-commerce platforms**; the basket was designed from the 2023-24 Household Consumption Expenditure Survey (a sample survey). (The article does not describe the formal sampling scheme; treat it as an illustration of large-scale price sampling.) ([Business Standard](https://www.business-standard.com/amp/economy/news/economy-inflation-weight-food-beverages-cut-new-cpi-series-2024-base-126012901838_1.html))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Sampling Methods
> 🟠 Tier 2 · _Tracker hint:_ Simple Random, Systematic (every kth), Stratified (by subgroup), Cluster, Convenience

### Definition
A **sample** is a subset of a **population** drawn through a **sampling frame** (the list). **Probability sampling** gives every unit a known non-zero chance, so sampling error can be quantified; **non-probability sampling** does not.

| Method | How | Best when | Watch out |
|---|---|---|---|
| Simple random | Every unit equally likely (random numbers) | Homogeneous population, full frame | Needs a list; can miss small groups |
| Systematic | Every $k$th unit, $k=N/n$, random start | Ordered lists, production line | Hidden periodicity bias |
| Stratified | Split into homogeneous strata, sample each (proportional or optimal) | Distinct subgroups; want precision | Needs strata info |
| Cluster | Randomly pick whole groups (villages, stores), survey all or a sub-sample | No frame, dispersed population, cost | Higher variance (design effect) |
| Multistage | Cluster at several levels | National surveys | Complex weights |
| Convenience / judgement / quota / snowball | Easy access or expert choice | Pilots, exploration | Selection bias, no error estimate |

**Sampling error** is chance variation; **non-sampling error** (coverage, non-response, measurement, bias) can be larger and does not fall with $n$. A bigger biased sample is still biased.

### Example
A packaged-snack firm wants shopper feedback across 5,000 kirana stores in four zones. Stratified by zone (North 1,000, South 1,500, West 1,500, East 1,000) with a total sample of 400: proportional allocation gives 80, 120, 120, 80. Systematic: with $N=5{,}000$ and $n=400$, $k=12.5$, so pick every 12th or 13th store from a random start.

### In the news
See news box. The CPI market coverage (urban and rural markets, 434 towns) illustrates the stratification idea (separate rural and urban strata); adding e-commerce price feeds is a response to a changing sampling frame as consumers shift online.

### Interview angle
> [!question] How it is asked
> "How would you survey customers of a quick-commerce app across India?" or "Stratified vs cluster: what is the difference?"

> [!tip] Strong answer includes
> - Probability vs non-probability sampling and why it matters for inference
> - Stratified (within-group homogeneous) vs cluster (within-group heterogeneous)
> - The frame, and the biases from convenience samples
> - Non-response and weighting for representativeness

---

## 2. Sample Size Determination
> 🟠 Tier 2 · _Tracker hint:_ n = (Z×σ/E)² for means; n = Z²×p(1-p)/E² for proportions; E=margin of error

### Definition
Sample size balances precision (margin of error $E$), confidence (via $Z$), and variability.

$$n=\left(\frac{Z_{\alpha/2}\,\sigma}{E}\right)^2\ \text{(mean)},\qquad n=\frac{Z_{\alpha/2}^2\,p(1-p)}{E^2}\ \text{(proportion)}$$

- Use $p=0.5$ if unknown (maximises $p(1-p)=0.25$, the conservative choice).
- Z values: 90% is 1.645, 95% is 1.96, 99% is 2.576.
- Round **up**.
- **Finite population correction:** $n_{adj}=\dfrac{n}{1+(n-1)/N}$, relevant when $n$ exceeds about 5% of $N$.
- Halving $E$ needs **4x** the sample. Cluster samples need $n\times$ design effect; allow for expected non-response (divide by response rate).
- Two-group tests: sample size depends on effect size, $\alpha$, and power (see A/B testing, sub-topic 8).

### Example
Mean: $\sigma=15$ minutes of delivery time, $E=3$, 95%: $n=(1.96\times15/3)^2=9.8^2=96.04\to97$.
Proportion: $p=0.5$, $E=0.05$, 95%: $n=1.96^2\times0.25/0.05^2=3.8416\times0.25/0.0025=384.16\to385$.
Finite population $N=2{,}000$: $385/(1+384/2000)=385/1.192=323$.

### In the news
See news box. The CPI's price-collection design is a sample-size decision at scale: more markets and e-commerce feeds reduce sampling error but cost more; the cost-precision trade-off is the same as $n\propto1/E^2$.

### Interview angle
> [!question] How it is asked
> "How many customers should we survey to estimate satisfaction within ±5%?"

> [!tip] Strong answer includes
> - Formula for a proportion with $p=0.5$ and $Z=1.96$, giving about 385
> - Inverse-square relation between margin of error and $n$
> - Adjust for finite population, non-response and design effect
> - Variance known from a pilot or past data

---

## 3. Confidence Intervals
> 🟠 Tier 2 · _Tracker hint:_ CI = x̄ ± Z×(σ/√n); or ± t×(s/√n); interpret as: 95% of such intervals contain μ

### Definition
A confidence interval gives a range of plausible values for a population parameter.

$$\bar x\pm z_{\alpha/2}\frac{\sigma}{\sqrt n}\ (\sigma\text{ known}),\qquad \bar x\pm t_{\alpha/2,\,n-1}\frac{s}{\sqrt n}\ (\sigma\text{ unknown}),\qquad \hat p\pm z\sqrt{\frac{\hat p(1-\hat p)}{n}}$$

**Correct interpretation (frequentist):** if we repeated the sampling many times, about 95% of the intervals so built would contain the true parameter. It is **not** "a 95% probability that $\mu$ lies in this particular interval" (the interval is random, $\mu$ is fixed). Width shrinks with larger $n$ ($\propto1/\sqrt n$), grows with higher confidence and variability. Use $t$ for small samples (it has fatter tails). A CI also does a hypothesis test: if 0 (or the null value) is outside the 95% CI, reject at 5%. Bootstrap CIs handle awkward statistics (see [[093 Business Statistics Applications]]).

### Example
Sample of 36 orders: mean basket ₹250, $s=30$. SE $=30/\sqrt{36}=5$; $t_{0.025,35}\approx2.030$; margin $=10.15$; 95% CI = ₹239.85 to ₹260.15. If $n$ were 144 (4x), SE = 2.5 and the margin ~5.0: double the precision for four times the data.

### In the news
See news box. Published headline statistics, for example CPI inflation of 2.75% for Jan 2026, are point estimates from sampled prices; any survey-based figure carries uncertainty, which is why interpretation should include a range or the revision history.

### Interview angle
> [!question] How it is asked
> "What does a 95% confidence interval actually mean?" or "Compute the CI for this sample."

> [!tip] Strong answer includes
> - Correct repeated-sampling interpretation, not "95% probability"
> - z vs t choice, and the formula with the standard error
> - Effects of $n$, variability and confidence on the width
> - Link between CI and hypothesis test

---

## 4. Design of Experiments (DOE)
> 🟠 Tier 2 · _Tracker hint:_ Factorial designs; 2^k full factorial; fractional factorial; Taguchi methods

### Definition
**DOE** (Fisher) deliberately varies **factors** at chosen **levels** to measure their effects on a **response**, using **randomisation**, **replication** and **blocking** to get valid, efficient conclusions. One-factor-at-a-time testing misses **interactions** and wastes runs.

- **$2^k$ full factorial:** $k$ factors at 2 levels (coded -1/+1), $2^k$ runs. Main effect $=$ mean response at high $-$ mean at low. Interaction effect measures whether one factor's effect depends on another.
- **Fractional factorial** $2^{k-p}$: a fraction of runs (e.g. $2^{5-1}=16$ instead of 32) at the price of **aliasing** (confounding) of effects; resolution III/IV/V tells what is confounded. Use for screening many factors.
- **Taguchi methods:** orthogonal arrays (e.g. L8, L9) and signal-to-noise ratios to find robust settings insensitive to noise.
- Analysis: ANOVA, effect plots, interaction plots, normal probability plot of effects.
- Then refine with **response surface** designs (sub-topic 7).

### Example
2x2 factorial: Temperature (A) and Pressure (B), response = yield.
Runs: (-,-)=20, (+,-)=30, (-,+)=25, (+,+)=45.
$A=\frac{(30+45)-(20+25)}{2}=15$; $B=\frac{(25+45)-(20+30)}{2}=10$; $AB=\frac{(20+45)-(30+25)}{2}=5$.
Raising temperature adds 15 units on average; the positive interaction means the pressure benefit is larger at high temperature. A $2^3$ design needs 8 runs; $2^{3-1}$ needs 4.

### In the news
See news box. Not directly applicable to DOE; experimental design in public statistics shows up in how pilots test collection methods. Industrially, DOE is the standard tool for the Improve phase of Six Sigma ([[091 Statistical Quality Control (SQC)]]).

### Interview angle
> [!question] How it is asked
> "How would you find the best combination of settings for a process with several factors?"

> [!tip] Strong answer includes
> - Why not one-factor-at-a-time (interactions, efficiency)
> - Factorial design, randomisation, replication, blocking
> - Fractional factorial for screening, with the aliasing trade-off
> - Taguchi for robust design; ANOVA for analysis

---

## 5. Randomized Block Design
> 🟠 Tier 2 · _Tracker hint:_ Block nuisance variables; rows=blocks, columns=treatments; reduce error variance

### Definition
When experimental units differ in a known way (store size, machine, day), **group similar units into blocks** and assign every treatment randomly **within each block**. Variation between blocks is removed from the error term, increasing power.

Model: $y_{ij}=\mu+\tau_i+\beta_j+\varepsilon_{ij}$ (treatment $\tau_i$, block $\beta_j$). With $a$ treatments and $b$ blocks:

$$SST=SS_{treat}+SS_{block}+SSE,\qquad df:\ (ab-1)=(a-1)+(b-1)+(a-1)(b-1)$$

$$F=\frac{MS_{treat}}{MSE},\quad MSE=\frac{SSE}{(a-1)(b-1)}$$

Compared with a completely randomised design, blocking helps only if blocks differ materially (otherwise you lose error degrees of freedom). Block what you can, randomise what you cannot. Paired t-test is a randomised block with two treatments.

### Example
3 pack designs tested across 4 stores (blocks). $SS_{treat}=60$, $SS_{block}=90$, $SSE=30$ (total 180). $df$: treatments 2, blocks 3, error 6. $MS_{treat}=30$, $MSE=30/6=5$, $F=6.0$ versus $F_{0.05;2,6}=5.14$, so pack design matters. Without blocking, SSE would be $30+90=120$ on 9 df, $MSE=13.3$, $F=2.25$ and the effect would be missed.

### In the news
See news box. Stratification in survey sampling is the observational cousin of blocking: both use known groupings to cut variance, as the CPI does by separating urban and rural markets.

### Interview angle
> [!question] How it is asked
> "You are testing three store layouts across 12 stores of different sizes. How do you design the test?"

> [!tip] Strong answer includes
> - Block by the nuisance variable (store size, region), randomise within block
> - Variance-partition logic: why error shrinks
> - ANOVA table with the correct degrees of freedom
> - When blocking does not help

---

## 6. Latin Square Design
> 🟠 Tier 2 · _Tracker hint:_ Two blocking factors; efficient for 3+ factor experiments

### Definition
A **Latin square** of order $p$ is a $p\times p$ grid where each treatment (letter) appears **exactly once in every row and every column**. Rows and columns are two blocking factors (e.g. day and machine/operator); treatments are the third factor. It needs only $p^2$ runs instead of $p^3$.

Model: $y_{ijk}=\mu+\alpha_i+\beta_j+\tau_k+\varepsilon$. Degrees of freedom: rows $p-1$, columns $p-1$, treatments $p-1$, error $(p-1)(p-2)$, total $p^2-1$.

Assumptions: **no interaction** between blocking factors and treatments; treatments randomly assigned within the square; $p$ at least 4 to give reasonable error df ($p=3$ gives only 2). Variants: **Graeco-Latin** squares add a third blocking factor. Used in agriculture, manufacturing trials, and marketing tests (e.g. day-of-week by store by promotion).

### Example
Testing 4 promotions (A to D) across 4 stores (rows) and 4 weeks (columns), 16 observations rather than 64:

| | W1 | W2 | W3 | W4 |
|---|---|---|---|---|
| Store 1 | A | B | C | D |
| Store 2 | B | C | D | A |
| Store 3 | C | D | A | B |
| Store 4 | D | A | B | C |

Error df = $(4-1)(4-2)=6$. Each promotion runs once in every store and every week, so store and week effects cancel.

### In the news
See news box. Not directly applicable; Latin squares matter in rotated-treatment tests such as testing price points across stores and days in retail pilots.

### Interview angle
> [!question] How it is asked
> "You can run only 16 trials. How would you test 4 treatments while controlling for two sources of variation?"

> [!tip] Strong answer includes
> - Each treatment once per row and column, with $p^2$ runs
> - The no-interaction assumption
> - Degrees of freedom (error $=(p-1)(p-2)$)
> - Extension: Graeco-Latin; limitation for small $p$

---

## 7. Response Surface Methodology
> 🟠 Tier 2 · _Tracker hint:_ Optimize response; Box-Behnken, Central Composite Design; contour plots

### Definition
**RSM** (Box and Wilson) uses designed experiments plus regression to model the relationship between several inputs and a response and find the **optimum**. Sequence: screening, **steepest ascent** with a first-order model, then a **second-order model** near the optimum:

$$y=\beta_0+\sum\beta_ix_i+\sum\beta_{ii}x_i^2+\sum\sum\beta_{ij}x_ix_j+\varepsilon$$

- **Central Composite Design (CCD):** factorial points + axial (star) points at $\pm\alpha$ + centre points. $\alpha=\sqrt2$ for a rotatable 2-factor design ($\alpha=2^{k/4}$ for a full factorial base). Runs for $k=2$: $4+4+n_c$.
- **Box-Behnken:** 3 levels, no corner points (safer when extreme corners are unsafe or infeasible); for $k=3$: 12 edge-midpoint runs + centre runs.
- **Analysis:** fit, check lack of fit, locate **stationary point** (maximum, minimum or saddle) with contour and 3-D surface plots; confirm by a run at the optimum. **Desirability functions** handle multiple responses.

### Example
One factor for simplicity: fitted yield $y=50+4x-2x^2$. $dy/dx=4-4x=0$ gives $x^*=1$, $y^*=50+4-2=52$; since $\beta_{11}<0$ it is a maximum. For a 2-factor CCD with 5 centre points: $4+4+5=13$ runs. Box-Behnken for 3 factors with 3 centre points: $12+3=15$ runs.

### In the news
See news box. Not directly applicable; RSM is how process industries tune settings (pharma, chemicals, food) after the screening stage.

### Interview angle
> [!question] How it is asked
> "How would you find the optimal setting for temperature and time that maximise yield?"

> [!tip] Strong answer includes
> - Sequential approach: screen, climb, fit the second-order model
> - CCD vs Box-Behnken and when each is preferable
> - Stationary point and contour plot reading
> - Validate with confirmation runs

---

## 8. A/B Testing Statistics
> 🟠 Tier 2 · _Tracker hint:_ Control vs treatment; randomization; minimum detectable effect; sample size calc

### Definition
An **A/B test** is a randomised controlled experiment: users are randomly split into **control (A)** and **treatment (B)**, and a pre-defined **primary metric** (conversion, revenue per user) is compared. Randomisation makes groups comparable, so the difference can be read causally.

Two-proportion test: $z=\dfrac{\hat p_B-\hat p_A}{\sqrt{\hat p(1-\hat p)(1/n_A+1/n_B)}}$.

**Sample size per arm** for baseline $p_1$, target $p_2$, $MDE=|p_2-p_1|$:

$$n=\frac{(z_{\alpha/2}+z_{\beta})^2\,[p_1(1-p_1)+p_2(1-p_2)]}{(p_2-p_1)^2}$$

with $\alpha=0.05$ ($z=1.96$) and power 80% ($z_\beta=0.84$). **Minimum detectable effect (MDE)** is the smallest lift worth detecting; smaller MDE needs much more traffic ($n\propto1/MDE^2$). Fix sample size and duration in advance (include full weekly cycles); define guardrail metrics; check **sample ratio mismatch**.

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize
es = proportion_effectsize(0.11, 0.10)
n = NormalIndPower().solve_power(es, power=0.8, alpha=0.05)
```

### Example
Baseline conversion 10%, aim to detect 11% (MDE = 1 percentage point). $(1.96+0.84)^2=7.84$; $0.10\times0.90+0.11\times0.89=0.09+0.0979=0.1879$. $n=7.84\times0.1879/0.01^2=1.4731/0.0001\approx14{,}731$ per arm, about 29,500 users in total. For a 2-point MDE, the need falls to roughly a quarter.

### In the news
No verified, specific A/B-testing news item was found for this note; see news box for the sampling context. A/B tests are the standard way Indian e-commerce and fintech apps decide interface and pricing changes, and the news box's emphasis on representative sampling applies equally to who gets assigned to treatment.

### Interview angle
> [!question] How it is asked
> "Design an A/B test for a new checkout page." or "The test is significant after 3 days; do we ship?"

> [!tip] Strong answer includes
> - Hypothesis, primary metric, guardrails, randomisation unit
> - Sample size from baseline, MDE, $\alpha$ and power (with the formula)
> - Run to the planned size; avoid peeking and many metrics
> - Interpret statistical vs practical significance; consider novelty effects and seasonality

---

## 9. ⭐ Advanced: Design Effect, Non-Response Bias and Weighting
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Design effect** compares a complex design's variance with simple random sampling: $deff=\dfrac{Var_{complex}}{Var_{SRS}}$. For cluster samples with cluster size $m$ and intra-cluster correlation $\rho$:

$$deff=1+(m-1)\rho,\qquad n_{eff}=\frac{n}{deff}$$

- **Non-response bias:** if non-responders differ from responders, estimates are biased no matter how large $n$ is. Remedies: follow-ups, incentives, **post-stratification / raking weights** to match known population margins, imputation.
- **Weighting:** design weight $=1/\text{inclusion probability}$; adjust for non-response; trim extreme weights.
- **Sampling from big data / online panels:** self-selected samples are not probability samples.
- **Other biases:** coverage (frame omits groups), survivorship, measurement and social-desirability bias.
- **Total survey error** thinking: sampling error plus all non-sampling errors.

### Example
Cluster survey: 20 customers per store, $\rho=0.05$: $deff=1+19\times0.05=1.95$. A sample of 1,000 customers has an effective size $1000/1.95\approx513$. If 385 effective respondents are required, you need $385\times1.95\approx751$ respondents; with a 60% response rate, contact $751/0.6\approx1{,}252$ people.

### In the news
See news box. Census 2027's self-enumeration option and digital forms aim to reduce non-response and coverage errors, the same issues survey designers manage with weighting.

### Interview angle
> [!question] How it is asked
> "Your survey got a 20% response rate. Can you trust the results?"

> [!tip] Strong answer includes
> - Non-response bias vs sampling error; larger $n$ does not fix bias
> - Compare responders with known population margins; weight or raking
> - Design effect for clustered samples
> - Triangulate with an independent data source

---

## 10. ⭐ Advanced: Pitfalls in A/B Testing: Peeking, Multiple Comparisons, Variance Reduction
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Peeking / optional stopping:** checking a fixed-horizon test repeatedly and stopping when $p<0.05$ inflates the false-positive rate well above 5%. Use sequential methods (alpha-spending, always-valid p-values) or commit to the sample size.
- **Multiple comparisons:** testing $m$ metrics or variants: family-wise error is about $1-(1-\alpha)^m$ (for 10 independent tests at 5% that is $1-0.95^{10}=40.1\%$). Control with **Bonferroni** ($\alpha/m$) or **Benjamini-Hochberg** FDR.
- **Sample ratio mismatch (SRM):** a 50/50 split that arrives as 51/49 on large traffic signals a randomisation or logging bug; test with a chi-square.
- **Variance reduction:** **CUPED** adjusts the metric with pre-experiment data ($Y'=Y-\theta(X-\bar X)$), cutting needed sample size; stratification and blocking help similarly.
- **Interference / network effects:** in marketplaces, treatment spills over; randomise by cluster, region or time.
- **Novelty and primacy effects, Simpson's paradox**, and ratio-metric variance (delta method).
- **Bayesian A/B:** report the probability that B beats A and expected loss.

### Example
You track 10 metrics at $\alpha=0.05$ and ship because one is "significant". Chance of at least one false positive when all effects are zero is $1-0.95^{10}=40.1\%$. With Bonferroni, the threshold per metric is $0.05/10=0.005$. For SRM: expected 50,000 / 50,000 but observed 50,900 / 49,100 gives $\chi^2=(900^2/50000)\times2=32.4$, far above 3.84, so the split is broken.

### In the news
See news box. A representative, properly randomised assignment is the experimental analogue of a good sampling frame; SRM checks are quality control for that assignment.

### Interview angle
> [!question] How it is asked
> "Your A/B test shows a 2% lift with p = 0.04 after you checked daily for two weeks. What is wrong?"

> [!tip] Strong answer includes
> - Peeking inflates false positives; pre-register sample size or use sequential tests
> - Multiple metrics need correction
> - SRM check and CUPED mention
> - Practical vs statistical significance; replicate before a big rollout

---
## 🔗 Go deeper: expansion notes
- [[213 Design of Experiments - Factorial, Fractional & Taguchi|Design of Experiments - Factorial, Fractional & Taguchi]]
- [[214 Causal Inference & Experimentation Beyond A-B Tests|Causal Inference & Experimentation Beyond A-B Tests]]
