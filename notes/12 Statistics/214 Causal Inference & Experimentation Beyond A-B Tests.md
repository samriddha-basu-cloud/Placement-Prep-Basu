---
tags: [statistics, tier1]
area: Statistics
topic: "Causal Inference & Experimentation Beyond A-B Tests"
tier: Tier 1
roles: PM / Analytics / Consulting
status: complete
subtopics: 13
---
# Causal Inference & Experimentation Beyond A-B Tests

⬅ [[213 Design of Experiments - Factorial, Fractional & Taguchi]] · [[_Index - Statistics|Statistics]] · [[215 Statistics Interview Question Bank & Numericals]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** PM / Analytics / Consulting

## Sub-topics in this note
1. [[#1. Correlation vs Causation and the Confounding Problem]]
2. [[#2. Potential Outcomes, ATE and Selection Bias]]
3. [[#3. Randomised Controlled Trials: Design and the Randomisation Unit]]
4. [[#4. Interference, Network Effects, Switchbacks and Geo Experiments]]
5. [[#5. Difference-in-Differences (with Worked Table)]]
6. [[#6. Regression Discontinuity]]
7. [[#7. Instrumental Variables and LATE]]
8. [[#8. Propensity Score Matching and Weighting]]
9. [[#9. Synthetic Control]]
10. [[#10. Uplift Modelling and Heterogeneous Treatment Effects]]
11. [[#11. Pitfalls: Selection Bias, Simpson's Paradox and Other Traps]]
12. [[#12. Answering "How Would You Measure the Impact of X?"]]
13. [[#13. ⭐ Advanced: DAGs, Sensitivity Analysis and Triangulation]]

## 📰 News box
> [!news] Shared news hook for this topic (2018–2026): marketplaces, marketing budgets and policy all run on quasi-experiments
> **Switchback tests at DoorDash (company engineering blog, 14 February 2018).** DoorDash explains that simple A/B tests are often ineffective in its marketplace because treatment and control customers share the same pool of delivery drivers ("Dashers"), so the arms interfere with each other. Its answer is a **switchback test**: randomise treatment over time-and-region units, typically **30-minute periods at city level**, which keeps randomisation (the key to causal claims) while avoiding network contamination. The post also notes that before/after comparisons cannot establish causation because "the outside world often has a much larger effect on metrics than product changes do". In its A/A tests, adjusting standard errors for correlated time-region units changed variance by less than 10%. ([DoorDash Engineering](https://careersatdoordash.com/blog/switchback-tests-and-randomized-experimentation-under-network-effects-at-doordash/))
>
> **Google open-sources Meridian, a Bayesian marketing mix model (29 January 2025).** Meridian is described as using Bayesian causal inference to reveal the incremental impact of marketing, with results of incrementality experiments usable as priors; over 20 measurement partners were trained and certified on it. Observational media-mix models are calibrated by randomised tests, a pattern worth knowing. ([Google blog](https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/))
>
> **A recall-based "impact" study of Karnataka's Shakti free-bus scheme (Ideas for India article).** Researchers surveyed about 250 women in four districts, asking them to compare work and travel before and after the scheme's June 2023 launch; 61% reported travelling more often for work and only 10.5% entered paid work for the first time, with wages not rising. The article itself describes the design as recall-based, not a randomised trial. Treat such pre/post self-reports as descriptive, and ask what a comparison group would add. ([Ideas for India](https://www.ideasforindia.in/topics/social-identity/fare-play-how-karnatakas-shakti-is-changing-womens-work))
>
> **Natural experiments won the 2021 Economics Nobel (11 October 2021).** David Card, Joshua Angrist and Guido Imbens were honoured for work on labour economics and natural experiments; the Academy said natural experiments are "a rich source of knowledge". DiD, IV and RD, covered below, are the tools that grew from this agenda. ([NBER](https://www.nber.org/news/joshua-angrist-david-card-and-guido-imbens-awarded-2021-nobel-prize))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Correlation vs Causation and the Confounding Problem
> 🔴 Tier 1 · _Key points:_ Association is not effect; confounders, reverse causality, selection; causal question needs a counterfactual

### Definition
**Correlation** says two variables move together; **causation** says changing one changes the other. Three reasons a correlation can mislead:
- **Confounding:** a third variable drives both (high-intent customers both join the loyalty programme and spend more).
- **Reverse causality:** the outcome causes the "treatment" (stores in trouble get more supervision visits, so visits correlate with poor performance).
- **Selection/ collider bias:** the data were filtered on a variable affected by both (analysing only survivors, or only buyers).
Also coincidence (spurious trends, multiple testing) and measurement error. A **causal question** asks "what would the outcome have been under the other action?", which is a counterfactual that can never be observed for the same unit. The solutions are design (randomisation, quasi-experiments) or assumptions (adjustment for confounders, which need subject knowledge). The causal ladder: association (seeing), intervention (doing), counterfactual (imagining). Link to statistical foundations in [[090 Regression Analysis]] (a regression coefficient is not automatically causal) and [[089 Hypothesis Testing]].

### Example
Suppose (illustrative numbers) customers who use a food-delivery app's in-app wallet order 3.1 times a month versus 1.8 for non-users. Does wallet cause more orders? Alternatives: heavy users adopt wallets (reverse causality); high-income users do both (confounding); the wallet was offered first to loyal users (selection). A causal design is needed before "push wallet adoption" becomes a strategy: randomise the nudge, or use a rollout discontinuity.

### In the news
See news box. The Shakti study is descriptive: women's own before/after recall cannot separate the scheme's effect from other changes since June 2023.

### Interview angle
> [!question] How it is asked
> "Users who watch a tutorial retain better. Should we force everyone to watch it?"

> [!tip] Strong answer includes
> - Correlation could be due to motivation (confounding); the tutorial may be a marker, not a cause
> - Propose a randomised test of showing the tutorial, or an encouragement design
> - Specify the metric, population and the harm of forcing (drop-off)
> - Say what you would conclude under each outcome

---
## 2. Potential Outcomes, ATE and Selection Bias
> 🔴 Tier 1 · _Key points:_ Y(1), Y(0); ATE, ATT; observed difference = ATT + selection bias; fundamental problem of causal inference

### Definition
In the **Rubin potential-outcomes framework**, each unit $i$ has two potential outcomes: $Y_i(1)$ under treatment and $Y_i(0)$ under control. The individual effect $\tau_i=Y_i(1)-Y_i(0)$ is never observed (the **fundamental problem of causal inference**). Estimands:

$$\text{ATE}=E[Y(1)-Y(0)],\qquad \text{ATT}=E[Y(1)-Y(0)\mid T=1]$$

The naive difference in observed means decomposes:

$$E[Y\mid T=1]-E[Y\mid T=0]=\underbrace{E[Y(1)-Y(0)\mid T=1]}_{\text{ATT}}+\underbrace{E[Y(0)\mid T=1]-E[Y(0)\mid T=0]}_{\text{selection bias}}$$

**Randomisation** makes treated and control comparable ($T\perp(Y(0),Y(1))$), so selection bias is zero in expectation. Core assumptions for observational work: **SUTVA** (no interference between units; one version of the treatment), **ignorability/unconfoundedness** ($Y(0),Y(1)\perp T\mid X$), **positivity/overlap** (every covariate profile can be treated or untreated). Special estimands: **LATE** (effect for compliers in IV) and **CATE** (effect conditional on covariates, for uplift).

### Example
Four customers: A (Y0=10, Y1=14), B (8, 8), C (12, 16), D (6, 9). True ATE $=(4+0+4+3)/4=2.75$. If the programme is joined by A and C (the high-spenders) and not by B and D: observed treated mean $=(14+16)/2=15$, control mean $=(8+6)/2=7$, naive difference $=8$. ATT $=(4+4)/2=4$ and selection bias $=E[Y(0)\mid T=1]-E[Y(0)\mid T=0]=11-7=4$, so $8=4+4$. The naive estimate is 3x the true ATE. Scaled-up version: 40% heavy buyers (baseline ₹2,000/month), 60% light (₹800); heavy join with probability 0.7, light with 0.2; true effect ₹150 for all. Joiners are 70% heavy, non-joiners 20% heavy, so naive difference $=(0.7-0.2)\times1200+150=\mathbf{₹750}$ against the true ₹150 (selection bias ₹600). Adjusting for buyer type (stratifying) recovers about ₹151 in a simulation of 100,000 customers.

### In the news
See news box. DoorDash's remark that the outside world moves metrics more than product changes is the same point: observed differences contain selection and time effects, not just treatment.

### Interview angle
> [!question] How it is asked
> "Explain ATE vs ATT, and why a naive comparison of users vs non-users is biased."

> [!tip] Strong answer includes
> - Potential outcomes; observed difference = ATT + selection bias
> - Randomisation removes selection bias in expectation
> - State SUTVA, ignorability and overlap for observational claims
> - Give a numeric or business example (loyal members are already high spenders)

---
## 3. Randomised Controlled Trials: Design and the Randomisation Unit
> 🔴 Tier 1 · _Key points:_ Pick the unit (user, session, cluster, geo, time); power and ICC; pre-register metric; guardrails; check SRM and balance

### Definition
An **RCT / online controlled experiment** randomly assigns units to arms and compares outcomes. Design choices:
- **Randomisation unit:** user (most common; consistent experience), device/cookie, session, order, store/city/geo (cluster), time block (switchback). The **analysis unit** should match the randomisation unit (or use cluster-robust SEs).
- **Hypothesis, primary metric, guardrails** (revenue, latency, complaints, cancellation) and **minimum detectable effect**, set before launch. Sample size and power formulas are in [[089 Hypothesis Testing]] and [[092 Sampling & Experimental Design]]; a typical Bernoulli sample size per arm is $n\approx16\,p(1-p)/\delta^2$ for 80% power.
- **Cluster randomisation:** observations in a cluster are correlated; design effect $\text{deff}=1+(m-1)\rho$ for cluster size $m$ and intraclass correlation $\rho$; effective sample size $=N/\text{deff}$.
- **Checks:** **sample ratio mismatch (SRM)** test (chi-square on arm counts), covariate balance, A/A tests, no peeking (see sequential testing in [[210 Bayesian Statistics for Decisions]]).
- **Variance reduction:** stratification, blocking, CUPED/regression adjustment using pre-period data.
- **Intention-to-treat (ITT)** analysis: analyse as randomised, not as treated; handles non-compliance honestly.
- **Pitfalls:** novelty/primacy effects (run full weekly cycles), Hawthorne effect, **SUTVA violations** (interference), carryover, multiple metrics (false positives), learning effects.

### Example
A delivery platform tests a new dispatch algorithm by randomising **cities** (20 cities) for a week, 5,000 orders per city per day: 35,000 orders per city, 700,000 in all. Order-level delivery times in a city are correlated with $\rho=0.01$ (shared weather, traffic, rider supply). Design effect $=1+(35{,}000-1)\times0.01=\mathbf{351}$; effective sample size $=700{,}000/351\approx\mathbf{1{,}995}$. The huge order count is an illusion; precision is governed by 20 clusters. Remedies: more clusters (shorter/more units, as in switchbacks), pre-period covariates, matched pairs of cities, or randomise at a level where interference is manageable (rider zone).

### In the news
See news box. DoorDash's 30-minute city-level periods are the compromise between interference and effective sample size.

### Interview angle
> [!question] How it is asked
> "You can randomise by user, by session or by city. How do you choose?"

> [!tip] Strong answer includes
> - Match unit to where interference occurs (shared resource, social spillover) and to the metric's level
> - Trade-off: finer unit = more power but contamination; coarser = cleaner but fewer effective units (design effect)
> - Metrics, guardrails, MDE, duration with full weekly cycles
> - SRM check, ITT analysis, A/A test

---
## 4. Interference, Network Effects, Switchbacks and Geo Experiments
> 🔴 Tier 1 · _Key points:_ SUTVA fails with shared supply/social links; switchback, cluster/geo randomisation, budget-split designs

### Definition
**Interference (spillover)** means one unit's treatment affects another's outcome, violating SUTVA, so the simple treatment-minus-control comparison no longer equals the global effect. Sources: two-sided marketplaces (shared drivers, inventory, pricing), social networks (friends' exposure), shared capacity (warehouse, call centre), and auction/budget competition in ads. Typical bias: with a shared supply pool, treated users who consume more capacity make control look worse (overstating effect), or the reverse with competition. Tools:
- **Switchback (time-split) tests:** the whole market flips between treatment and control across time windows, randomised and analysed as time-region units. Needs a window long enough for effects to materialise and short enough to give many windows; handle **carryover** (washout periods, discard transition) and time trends (block by hour/day-of-week); use cluster-robust or randomisation inference.
- **Cluster / geo randomisation:** cities, zones, social clusters; matched-pair geo experiments for marketing incrementality.
- **Ego-cluster/graph cluster randomisation** for social networks; **budget-split** designs for ad marketplaces; **holdout markets** for launches.
- **Two-sided designs** randomise both sides when needed. Always compare estimates against the fully-rolled-out effect when possible.

### Example
A quick-commerce firm tests a "free delivery above ₹199" rule. Randomising customers 50/50 inside a city: treated customers place more orders, using up rider supply, so control customers wait longer and order less, making the observed gap larger than the true effect of launching to everyone. Switchback design: city-level treatment alternates in 2-hour windows over four weeks (14 days × 12 windows × 5 cities = 840 city-windows), randomised within day-part. Analysis: regression of metric on treatment with day-part and city fixed effects and cluster-robust SEs by city-day; discard the first 15 minutes of every window as transition. The estimate is the effect of the policy on the whole system, at the price of much wider intervals than a naive user-level test.

### In the news
See news box. DoorDash states that treatment/control splits within a market share a driver fleet and that its switchbacks use 30-minute periods at city level, with a standard-error adjustment for correlated time-region units that moved variance by less than 10% in A/A tests.

### Interview angle
> [!question] How it is asked
> "How would you test a new pricing or dispatch algorithm on a marketplace where riders are shared?"

> [!tip] Strong answer includes
> - Spot interference (shared supply) and explain the bias direction
> - Switchback or geo-cluster design; window length, carryover, time trends
> - Accept lower power; use covariates, pairing, more windows
> - Validate with A/A runs and compare with a small user-level test

---
## 5. Difference-in-Differences (with Worked Table)
> 🔴 Tier 1 · _Key points:_ (Treated post − pre) − (Control post − pre); parallel trends; event-study; clustered SEs

### Definition
**Difference-in-differences (DiD)** estimates a treatment effect when a policy hits some units and not others at a given time, using a control group to remove common time trends:

$$\hat\tau_{DiD}=(\bar Y_{T,post}-\bar Y_{T,pre})-(\bar Y_{C,post}-\bar Y_{C,pre})$$

Regression form: $Y_{it}=\alpha+\beta\,\text{Treated}_i+\gamma\,\text{Post}_t+\delta\,(\text{Treated}_i\times\text{Post}_t)+\varepsilon_{it}$; $\delta$ is the effect. The key assumption is **parallel trends**: absent treatment, treated and control would have changed by the same amount. Check with pre-period trends and an **event-study** plot (leads should be near zero, lags show effect dynamics). Also needed: no anticipation, stable composition, no spillover from treated to control. Use **cluster-robust standard errors** at the unit (or treatment-assignment) level. Modern issues: **staggered adoption** with heterogeneous effects makes simple two-way fixed effects biased; use Callaway-Sant'Anna or Sun-Abraham estimators. Variants: triple differences, synthetic DiD. Classic case: Card and Krueger's study of New Jersey's 1992 minimum-wage increase using Pennsylvania restaurants as the control group.

### Example
A quick-commerce firm launches 10-minute delivery in 20 dark stores (treated) while 20 comparable stores keep 30-minute service. Weekly orders per store (simulated panel: 8 weeks pre, 8 weeks post, common trend of +1 order a week, true effect +15):

| Group | Pre | Post | Change |
|---|---|---|---|
| Treated stores | 104.5 | 127.3 | +22.8 |
| Control stores | 96.3 | 103.1 | +6.8 |
| **Difference-in-differences** | | | **+16.05** |

- Pre/post for treated alone (+22.8) overstates because the market trend added about 6.8 orders; post-only comparison (+24.2) is polluted by the baseline gap (treated stores were already 8 orders higher).
- Regression with store-clustered SEs: $\hat\delta=16.05$, SE $=0.75$, 95% CI $[14.6,\,17.5]$ (true effect 15 inside).
- Event study: coefficients for pre-weeks are about 0 (average 1.0 on a base of 100), post-weeks average about 17, supporting parallel trends.
- Business sentence: "10-minute delivery added about 16 orders per store per week (about 15% of the treated stores' pre-launch level of 104.5), assuming treated stores would have followed the control stores' trend."

```python
import pandas as pd, statsmodels.formula.api as smf
# df columns: store, treated (0/1), post (0/1), orders
m = smf.ols("orders ~ treated * post", data=df).fit(cov_type="cluster", cov_kwds={"groups": df["store"]})
print(m.params["treated:post"], m.bse["treated:post"])
```

### In the news
See news box. The Nobel-recognised natural-experiment tradition is largely DiD: Card's minimum-wage work compared neighbouring states with different policies. A Shakti-type scheme could be assessed by DiD against similar districts or states without free travel, if parallel pre-trends can be shown.

### Interview angle
> [!question] How it is asked
> "We launched a new loyalty programme in Bengaluru only. How do you measure its impact on orders?"

> [!tip] Strong answer includes
> - DiD with comparable cities as control; the (post−pre) difference formula
> - Parallel trends: check pre-trends, event-study, choose controls by pre-period similarity
> - Risks: spillover, concurrent events, composition change, clustered SEs; synthetic control as alternative
> - Translate result to a business number with a confidence interval

---
## 6. Regression Discontinuity
> 🔴 Tier 1 · _Key points:_ Treatment assigned by a cutoff on a running variable; compare units just above and below; bandwidth; local effect

### Definition
In a **regression discontinuity (RD) design**, treatment is assigned (sharp RD) or its probability jumps (fuzzy RD) at a cutoff $c$ of a continuous **running variable** $X$ (credit score, exam mark, age, order value, ranking). Units just either side are alike, so the jump in outcome at $c$ identifies the **local** effect:

$$\tau_{RD}=\lim_{x\downarrow c}E[Y\mid X=x]-\lim_{x\uparrow c}E[Y\mid X=x]$$

Estimate with **local linear regression** within a bandwidth $h$ on each side: $Y=\alpha+\tau D+\beta(X-c)+\gamma D(X-c)+\varepsilon$ for $|X-c|\le h$, with $D=\mathbf 1[X\ge c]$; choose $h$ by data-driven rules (Imbens-Kalyanaraman, Calonico-Cattaneo-Titiunik) and check sensitivity. Checks: **no manipulation** of the running variable (density test, McCrary), covariate balance at the cutoff, placebo cutoffs, donut RD. Limits: the effect is local to the cutoff (external validity); fuzzy RD needs an IV (the cutoff as instrument); sparse data near the cutoff widens intervals. Product uses: eligibility thresholds, rank-based exposure (top 10 results), credit/limit policies, "free shipping above ₹499" thresholds.

### Example
A lender raises credit limits for customers with bureau score $\ge700$. Simulated data: 6,000 customers around 700, true jump in monthly spend of ₹5,000. Naive comparison of all above vs all below gives +₹10,060 (it picks up the steady relationship between score and spend). Local linear RD:

| Bandwidth | Customers used | Estimated jump | SE |
|---|---|---|---|
| ±10 points | 1,254 | ₹4,960 | 660 |
| ±20 points | 2,362 | ₹4,960 | 470 |
| ±40 points | 4,048 | ₹4,690 | 350 |

All near the true ₹5,000; the naive gap is double. Reporting: "At the 700 cutoff, a limit increase raises monthly spend by about ₹5,000 (95% CI about ₹4,000 to ₹6,000) for customers near 700; do not extrapolate to score-800 customers without further evidence."

### In the news
See news box. RD is among the quasi-experimental designs highlighted by the natural-experiments tradition behind the 2021 Nobel Prize; any business rule with a cutoff creates RD opportunities.

### Interview angle
> [!question] How it is asked
> "Customers with order value just above ₹499 get free delivery. How do you estimate its effect on retention?"

> [!tip] Strong answer includes
> - Compare customers just above and below the threshold; local linear regression with bandwidth
> - Check for manipulation (people padding carts to ₹499): density test, covariate balance
> - Effect is local; mention fuzzy RD when compliance is imperfect
> - Sensitivity to bandwidth and functional form

---
## 7. Instrumental Variables and LATE
> 🔴 Tier 1 · _Key points:_ Instrument Z shifts treatment, affects Y only through D; Wald = ITT / first stage; relevance, exclusion, monotonicity

### Definition
When unobserved confounding makes OLS biased, an **instrument** $Z$ can still identify an effect if: (1) **relevance** $Z$ moves treatment $D$ (first-stage F well above 10); (2) **independence** $Z$ is as-good-as-randomly assigned; (3) **exclusion** $Z$ affects $Y$ only through $D$; (4) **monotonicity** no "defiers". With a binary instrument, the **Wald estimator** is

$$\hat\beta_{IV}=\frac{E[Y\mid Z=1]-E[Y\mid Z=0]}{E[D\mid Z=1]-E[D\mid Z=0]}=\frac{\text{ITT}}{\text{first stage}}$$

and it identifies the **LATE**: the effect for **compliers**, those whose treatment status changes with $Z$ (not for always-takers or never-takers). 2SLS generalises to many instruments and covariates. Sources: randomised encouragement (nudges, invitations), lotteries (draft lottery), geographic distance to a facility, rollout timing, staggered policy. Weak instruments inflate bias and variance; testing exclusion is impossible, only argued. Practical use: an RCT with imperfect compliance gives the effect of **using** the feature, not just **being offered** it.

### Example
An app randomly sends a push notification (Z) encouraging users to subscribe to a premium plan (D); outcome Y is 90-day spend (₹). Highly motivated users subscribe anyway and spend more, so OLS of Y on D is badly biased. Simulated data (40,000 users, true effect ₹80, motivation unobserved, seed 1):
- Subscription rate: 57.1% with the nudge vs 23.6% without; first stage $=33.5$ pp (F about 5,300).
- Spend: ITT $=\text{₹}27.4$ higher among nudged users.
- Wald/2SLS: $27.4/0.335=\mathbf{₹81.8}$ per subscriber (95% CI about ₹71 to ₹92), compared with the naive OLS "effect" of **₹177**.
Interpretation: ₹82 is the effect of subscribing for **compliers** (users who subscribe only when nudged); if promotions go to a different type of user, effects may differ. Always report ITT too: ₹27 per nudged user is what the campaign delivers.

### In the news
See news box. Instrumental variables (with RD and DiD) are the other half of the natural-experiment toolkit recognised by the 2021 Nobel Prize; the LATE concept came from Angrist and Imbens' work.

### Interview angle
> [!question] How it is asked
> "A feature's users spend more. Randomised invitations exist but only some invitees adopt. How do you get the effect of adoption?"

> [!tip] Strong answer includes
> - Use the randomised invitation as an instrument: ITT divided by first stage = LATE
> - State relevance, exclusion, monotonicity; weak instrument check
> - Interpret as effect for compliers only
> - Contrast with naive adopters vs non-adopters (selection bias)

---
## 8. Propensity Score Matching and Weighting
> 🔴 Tier 1 · _Key points:_ P(T=1|X); match or reweight; check overlap and balance; only fixes observed confounders

### Definition
When treatment was not randomised but you believe covariates $X$ capture all confounding (ignorability), the **propensity score** $e(X)=P(T=1\mid X)$ summarises $X$: conditional on $e(X)$, treatment is as good as random (Rosenbaum-Rubin). Methods:
- **Matching:** pair each treated unit with the control(s) with the nearest score (with caliper, often 0.2 sd of the logit of the score); estimates ATT; check balance with standardised mean differences (SMD below 0.1).
- **Inverse probability weighting (IPW):** weight $1/e$ for treated and $1/(1-e)$ for controls to estimate ATE; trim extreme weights; **stabilised or overlap weights** help.
- **Stratification** on score; **doubly robust** estimators (AIPW, targeted learning/ TMLE) combine outcome regression and weighting and are consistent if either model is right; **double ML** with ML nuisance models.
- **Diagnostics:** overlap/common support plots, balance tables before vs after, sensitivity analysis to hidden bias (E-value, Rosenbaum bounds).
Matching on pre-treatment covariates only (never post-treatment). It cannot fix **unobserved** confounders (motivation), and a perfect-prediction propensity model (no overlap) means the comparison is invalid. Models in [[096 Classification Algorithms]] (logistic regression, gradient boosting) estimate the score.

### Example
Simulated data: 20,000 customers; premium-membership opt-in depends on tenure and prior orders, true effect on monthly spend = ₹100. 47.9% opted in.
- Naive difference: **₹189** (members are heavier buyers).
- OLS adjusting for tenure and orders: ₹98.9.
- Propensity score (logistic) overlap: treated 1st to 99th percentile 0.22 to 0.89; controls 0.19 to 0.79: good overlap.
- 1:1 caliper matching: 9,549 of 9,572 treated matched; **ATT ₹102.4**; SMD of tenure fell from 0.457 to 0.002 and of orders from 0.444 to −0.002.
- IPW ATE: ₹99.4.
Everything lands near the true ₹100 because the simulated confounders were all observed. In real data the unmeasured part (motivation, intent) remains, so call the result "adjusted association" unless the ignorability argument is strong.

### In the news
See news box. Meridian lets incrementality-experiment results enter as priors, reflecting that modelling observed data alone leaves confounding open.

### Interview angle
> [!question] How it is asked
> "Premium members spend more. How would you estimate the true effect without an experiment?"

> [!tip] Strong answer includes
> - Propensity score matching/IPW or doubly robust estimation using pre-treatment covariates
> - Check overlap and covariate balance (SMD)
> - Limitation: unobserved confounders; sensitivity analysis; prefer experiment or quasi-experiment if available
> - Report ATT vs ATE and what population it applies to

---
## 9. Synthetic Control
> 🔴 Tier 1 · _Key points:_ One treated unit; weighted donor pool reproduces its pre-period path; gap after = effect; placebo tests for inference

### Definition
**Synthetic control (Abadie)** estimates the effect of an intervention on a single (or few) treated aggregate unit (a city, state, country, a market launch) when a good single control does not exist. Build a **weighted average of donor units** (weights non-negative, summing to 1) that matches the treated unit's pre-intervention outcomes (and covariates). The post-period gap between treated and synthetic is the estimated effect: $\hat\tau_t=Y_{1t}-\sum_j w_j^*Y_{jt}$. Inference by **placebo tests**: apply the same method to every donor, compare the post/pre RMSPE ratio of the treated unit with the donors' (permutation p-value is at least $1/(J+1)$). Requirements: long pre-period, donors unaffected by the intervention (no spillover), treated unit inside the convex hull of donors, no big shocks specific to the treated unit. Extensions: synthetic DiD, augmented synthetic control, Bayesian structural time series (CausalImpact) for marketing geo-lifts.

### Example
A policy (say congestion pricing) starts in one city at month 16 of 24, with 11 donor cities. Simulated outcome index with a true effect of +8:
- Weights: four donors take 97% of the weight (0.372, 0.241, 0.215, 0.142), the rest near zero.
- Pre-period fit RMSPE $=0.36$; post-period average gap $=\mathbf{+7.67}$ (true 8).
- Naive pre/post change in the treated city $=+12.4$ (includes the common trend of about +5.6 seen in donors); DiD against the average donor $=+6.8$.
- Placebo permutation: the treated city's post/pre RMSPE ratio is 21.6 vs 0.4 to 3.3 for the 11 donors, so it ranks 1st of 12: permutation $p=1/12=0.083$ (the smallest possible with 12 units).
Report with the pre-fit chart and placebo plot; a poor pre-fit (large RMSPE) means do not trust the estimate.

### In the news
See news box. Marketing incrementality tests often compare treated and untreated markets, the same logic as a synthetic control; such experiment results can feed Meridian-type models as priors.

### Interview angle
> [!question] How it is asked
> "We launched in Pune only. How do you measure the effect when no other city is similar?"

> [!tip] Strong answer includes
> - Build a synthetic Pune from a weighted mix of other cities that tracks it pre-launch
> - Placebo/permutation inference; pre-fit quality
> - Assumptions: no spillover, no concurrent local shocks, long pre-period
> - Compare with DiD and note the benefits when parallel trends fail for single controls

---
## 10. Uplift Modelling and Heterogeneous Treatment Effects
> 🔴 Tier 1 · _Key points:_ Target the persuadables; effect = P(buy|treat) − P(buy|control); sleeping dogs; Qini curve

### Definition
**Uplift (incremental response) modelling** predicts the **conditional average treatment effect** $\tau(x)=E[Y\mid T=1,x]-E[Y\mid T=0,x]$ so that treatments (coupons, calls, messages) go where they change behaviour. Four customer types: **persuadables** (act only if treated), **sure things** (act anyway), **lost causes** (never act), **sleeping dogs** (treatment backfires: unsubscribes, churn). Propensity-to-buy models target sure things and waste money. Methods: two-model (T-learner), single model with interactions (S-learner), **X/R-learners, causal forests, uplift trees**, class-transformation methods. They need **randomised data** (or strong unconfoundedness). Evaluate with **Qini / uplift curves** (cumulative incremental conversions as you target top-scored users) and uplift at k, ideally on a randomised holdout; avoid evaluating with accuracy. Decision rule: treat if $\tau(x)\times\text{value}>\text{cost}$. Heterogeneity discovery risks false positives: use pre-specified subgroups or honest splitting, and correct for multiple comparisons. Linked topics: [[100 ML for Product Management]], [[096 Classification Algorithms]].

### Example
A retention SMS test, 100,000 users randomised 50/50 into four equal behavioural segments (simulated). Conversion without vs with the offer:

| Segment | Control | Treated | Uplift |
|---|---|---|---|
| Persuadables | 4.2% | 12.2% | **+8.1 pp** |
| Sure things | 30.6% | 29.6% | about 0 (−1.0 pp noise) |
| Lost causes | 1.0% | 1.0% | 0 |
| Sleeping dogs | 19.8% | 13.9% | **−5.9 pp** |

Overall effect is only about +0.2 pp (true +0.5 pp) because gains and losses cancel, and the average hides who should be messaged. Targeting only persuadables (25,000 users) yields about 2,000 incremental conversions (25,000 × 8 pp), versus about 500 from messaging all 100,000, with a quarter of the messages and none of the sleeping-dog harm. If each message costs ₹3 and a conversion is worth ₹400 margin, the persuadable-only campaign earns $2{,}000\times400-25{,}000\times3=₹7.25$ lakh; messaging all earns $500\times400-100{,}000\times3=-₹1$ lakh.

### In the news
See news box. Uplift needs randomised or quasi-experimental ground truth; marketing-mix and incrementality efforts such as Meridian's experiment-as-prior design aim at the same incremental, not average, question.

### Interview angle
> [!question] How it is asked
> "Why not just target the customers most likely to convert?"

> [!tip] Strong answer includes
> - Likely to convert is not likely to be influenced; target persuadables, avoid sleeping dogs
> - Uplift = difference in conversion between treated and control, needs randomised data
> - Evaluate on a holdout with Qini curve and ₹ value minus cost
> - Warn about noisy subgroups and multiple testing

---
## 11. Pitfalls: Selection Bias, Simpson's Paradox and Other Traps
> 🔴 Tier 1 · _Key points:_ Selection, survivorship, Simpson, regression to the mean, post-treatment control, novelty, SUTVA, p-hacking

### Definition
Common traps in impact measurement:
- **Selection bias:** compared groups differ before treatment (self-selected users, opt-in pilots, volunteers).
- **Survivorship bias:** analysing only units that remained (active users, surviving stores).
- **Simpson's paradox:** a trend in aggregates reverses in sub-groups because group sizes differ; resolve by deciding which variable is a confounder (adjust) vs a mediator/collider (do not adjust), using the causal story, not the data alone.
- **Regression to the mean:** units picked for extreme values drift back (worst-performing stores improve anyway); control groups or pre-period baselines must be matched on that selection.
- **Post-treatment/collider adjustment:** controlling for a variable affected by treatment biases the result.
- **Interference, novelty and primacy effects**, **Hawthorne effect**, **seasonality and concurrent events**, **attrition**, **p-hacking/multiple comparisons**, **peeking**, **ecological fallacy** (group-level patterns assigned to individuals), **external validity** (a local effect does not generalise).
- **Metric traps:** surrogate metrics (clicks) that do not track value; Goodhart's law.

### Example
Simpson's paradox in delivery performance. Two carriers, two route types, on-time deliveries:

| | Metro | Rural | Overall |
|---|---|---|---|
| Carrier A | 95/100 (95%) | 150/300 (50%) | 245/400 (**61.3%**) |
| Carrier B | 270/300 (90%) | 40/100 (40%) | 310/400 (**77.5%**) |

A is better in **both** route types, yet B looks better overall because A is assigned more difficult rural routes. Comparing overall rates would reward the carrier with easy routes; route type is a pre-treatment confounder, so compare within route type, or standardise to a common route mix (50/50: A $=(95+50)/2=72.5\%$, B $=(90+40)/2=65\%$). In contrast, adjusting for a variable like "delivery delay" that carrier choice itself changes would be a post-treatment error.

### In the news
See news box. A recall-based pre/post study is vulnerable to selection (who answered), recall error and concurrent changes, which is why DiD or a comparison group is the minimum for a causal claim.

### Interview angle
> [!question] How it is asked
> "Conversion is higher on iOS than Android in aggregate but lower on both within each country. What is happening?"

> [!tip] Strong answer includes
> - Simpson's paradox: mix differs across groups; compare within strata or standardise
> - Decide using causal reasoning which variables to condition on (confounder vs mediator/collider)
> - Mention other biases (selection, survivorship, regression to the mean)
> - Recommend design (randomise) over post-hoc slicing

---
## 12. Answering "How Would You Measure the Impact of X?"
> 🔴 Tier 1 · _Key points:_ Clarify decision & metric → counterfactual → feasible design ladder → analysis plan → risks → recommendation

### Definition
A reusable interview structure:
1. **Clarify the decision and the metric:** what will change if the answer is "positive"? Primary metric (orders, retention, margin), guardrails, time horizon, unit.
2. **State the counterfactual:** "what would have happened without X?"
3. **Choose the strongest feasible design (ladder):** (a) randomised experiment (user-level; cluster/switchback if interference); (b) staggered rollout or phased launch randomised by time/geo; (c) quasi-experiment: DiD, RD, IV, synthetic control; (d) observational adjustment: matching/IPW/regression with sensitivity analysis; (e) last resort: pre/post with caveats.
4. **Design details:** unit, sample size and duration (full weekly cycles), SRM/balance checks, guardrails, novelty effects.
5. **Analysis plan:** ITT vs treated, heterogeneity, CI, correction for multiple metrics.
6. **Threats and mitigations:** interference, selection, concurrent events, seasonality, attrition.
7. **Translate to a decision:** effect size in ₹, uncertainty, rollout/hold, follow-ups.
Prefer randomisation; when impossible (a policy imposed on one city, historic data, ethical limits) say which assumption each alternative needs (parallel trends, no manipulation at cutoff, exclusion, ignorability). Tie to product metrics in [[031 Product Metrics & Analytics]] and the A/B basics in [[092 Sampling & Experimental Design]].

### Example
Prompt: "A food-delivery company introduces a 10-minute delivery tier in 5 of 40 cities. How do you measure impact on order frequency and cannibalisation?" Answer skeleton:
- Metric: weekly orders per active customer (primary), margin per order and rider utilisation (guardrails), cannibalisation of the 30-minute tier.
- Design: if the rollout order is still open, randomise the 5 launch cities from matched pairs (stratify by size/growth); otherwise DiD with remaining cities as controls plus a synthetic control for the biggest city.
- Checks: parallel pre-trends (12 weeks), event study, no demand spillover across neighbouring cities, concurrent festival or pricing changes.
- Interference: within-city customer-level tests are contaminated by shared riders, so use city-level or switchback tests.
- Output: "+X% orders per customer (95% CI), margin impact in ₹ lakh per month; recommend roll-out to cities of type Y".

### In the news
See news box. The DoorDash post and the Shakti article are two ends of the ladder: a design built around interference, and a recall-based pre/post that stops short of a causal estimate.

### Interview angle
> [!question] How it is asked
> "How would you measure the impact of our new recommendation feature / a government scheme / a marketing campaign?"

> [!tip] Strong answer includes
> - Clarify decision, metric and counterfactual first
> - Rank designs from randomised to observational and justify the choice
> - State assumptions and checks for the chosen quasi-experiment
> - Close with a decision in business units, plus risks and next steps

---
## 13. ⭐ Advanced: DAGs, Sensitivity Analysis and Triangulation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Causal DAGs (directed acyclic graphs):** draw arrows for assumed causal links. Adjust for **confounders** (common causes), do not adjust for **mediators** (on the causal path, unless estimating direct effects) or **colliders** (common effects: conditioning opens a spurious path). The **backdoor criterion** states which sets of covariates block all non-causal paths.
- **Sensitivity analysis for unmeasured confounding:** the **E-value** is the minimum strength (on the risk-ratio scale) an unmeasured confounder must have with both treatment and outcome to explain away an observed risk ratio: $E=RR+\sqrt{RR(RR-1)}$. For an observed $RR=1.8$, $E=1.8+\sqrt{1.8\times0.8}=\mathbf{3.0}$: a confounder would need a risk ratio of 3.0 with both treatment and outcome to nullify the result. Compare with the strength of known confounders to judge plausibility.
- **Negative controls and placebo outcomes** (an outcome that should not be affected) detect hidden bias.
- **Triangulation:** agree across methods with different assumptions (RCT, DiD, synthetic control, IV); calibrate observational models (marketing mix, attribution) with randomised lift tests or geo experiments, which is the design of Bayesian MMMs that take experiment results as priors (see [[210 Bayesian Statistics for Decisions]]).
- **Heterogeneity and transportability:** will the estimate apply to new cities, customers or time? **Long-term effects:** use surrogates carefully; run holdouts for months.
- **Sequential/adaptive experimentation** and bandits when decisions are repeated.

### Example
A DiD shows a new loyalty programme raises weekly orders 6% (observational rollout, not randomised). A sceptic says "stores chosen for the pilot were already improving". Responses: (1) event-study shows flat pre-trends for 12 weeks; (2) placebo test on an outcome the programme cannot affect (store footfall from walk-ins) shows no change; (3) E-value (strictly defined for risk ratios; for a continuous outcome like orders, convert via a standardised effect size, so treat this as illustration): if the uplift were a risk ratio of 1.06 the E-value is $1.06+\sqrt{1.06\times0.06}=1.31$, meaning a modest confounder (RR about 1.3 with both pilot selection and orders) could erase it, so the conclusion is **fragile** and a randomised holdout in the next wave is advisable. Weak evidence, honestly graded, is a strong interview answer.

### In the news
See news box. Meridian's use of experiment results as priors is triangulation in product form: an observational model constrained by randomised evidence.

### Interview angle
> [!question] How it is asked
> "You cannot randomise. How confident are you in an observational estimate, and what would change your mind?"

> [!tip] Strong answer includes
> - Draw the causal graph; adjust for confounders, not colliders/mediators
> - Sensitivity analysis (E-value), placebo/negative controls
> - Triangulate across methods and calibrate with randomised tests
> - State confidence honestly and propose the next experiment
