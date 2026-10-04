---
tags: [statistics, tier2]
area: Statistics
topic: "Generalised Linear Models & Categorical Data Analysis"
tier: Tier 2
roles: Analytics / PM
status: complete
subtopics: 13
---
# Generalised Linear Models & Categorical Data Analysis

⬅ [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]] · [[_Index - Statistics|Statistics]] · [[210 Bayesian Statistics for Decisions]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** Analytics / PM

## Sub-topics in this note
1. [[#1. Contingency Tables: Joint, Marginal and Conditional Distributions]]
2. [[#2. Risk Difference, Relative Risk and Odds Ratio (Worked)]]
3. [[#3. Chi-square Test of Independence and Residuals]]
4. [[#4. Simpson's Paradox and the Cochran-Mantel-Haenszel Test]]
5. [[#5. The GLM Framework: Family, Link, Linear Predictor and Deviance]]
6. [[#6. Logistic Regression: Fitting and Interpreting Odds]]
7. [[#7. Marginal Effects and Predicted Probabilities]]
8. [[#8. Probit and Other Binary Links]]
9. [[#9. Poisson Regression for Counts, Rates and Offsets]]
10. [[#10. Overdispersion: Quasi-Poisson, Negative Binomial and Zero-Inflation]]
11. [[#11. Ordinal Logistic Regression (Proportional Odds)]]
12. [[#12. Goodness of Fit and Model Comparison: Deviance, Hosmer-Lemeshow, AIC, LR Tests]]
13. [[#13. ⭐ Advanced: Gamma GLMs, Separation, Rare Events and a Recipe Book]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Dengue counts, a textbook case for count-data GLMs
> **India's dengue counts swing year to year.** The National Centre for Vector Borne Diseases Control (NCVBDC) lists 2,33,251 cases and 303 deaths in 2022; 2,89,235 cases and 485 deaths in 2023; 2,33,519 cases and 297 deaths in 2024; and 1,21,824 cases and 131 deaths in 2025 (provisional). In 2025 the highest burdens were Tamil Nadu (23,407), Maharashtra (14,168) and Kerala (10,923). Counts of events across states of very different population are modelled with Poisson or negative-binomial regression with a population offset, and the year-to-year swings are the overdispersion that forces the move from Poisson to negative binomial (sub-topics 9 and 10). ([NCVBDC dengue situation page](https://ncvbdc.mohfw.gov.in/index4.php?lang=1&level=0&linkid=431&lid=3715), figures as shown on the page when checked on 3 October 2026)
>
> **Dengue is at record levels globally.** WHO reports 2024 as a historic peak with over 14.6 million cases, and, for January to July 2025, over 4 million cases and more than 3,000 deaths across 97 countries, with spread into previously unaffected regions. Case counts rarely follow a clean Poisson pattern; seasonality, clustering and reporting differences generate extra variance. ([WHO dengue fact sheet](https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Contingency Tables: Joint, Marginal and Conditional Distributions
> 🟠 Tier 2 · _Key points:_ r x c table of counts; row/column totals; conditional proportions; independence means equal conditional distributions

### Definition
A **contingency table** cross-classifies units by two categorical variables (offer received by repeat purchase, supplier by defect/no defect). Cell counts $n_{ij}$; **marginals** are row and column totals; **joint** proportions divide by the grand total; **conditional** proportions divide by a row (or column) total. Variables are **independent** if the conditional distribution of one is the same across levels of the other, i.e. $E_{ij}=\frac{(\text{row total}_i)(\text{column total}_j)}{n}$. The sampling design decides which proportions are meaningful: cohort or experiment (fix groups, compare outcome rates), case-control (fix outcome groups, so only odds ratios are estimable), cross-sectional (all margins random). Always percent in the direction of the explanatory variable. Probability background in [[087 Probability Fundamentals]].

### Example
A retailer sends a ₹50 offer to 400 customers and nothing to 400 comparable customers (random assignment). Repeat purchase within 30 days: offer 120 repeat and 280 not; no offer 90 repeat and 310 not. Conditional repeat rates: 30.0% with offer, 22.5% without. Expected counts under independence for "offer and repeat": $400\times210/800=105$ against 120 observed. Row percentages, not column percentages, answer "does the offer work?".

### In the news
See news box. State-by-year dengue tables are r x c tables of counts; the first step is always to look at rates per population, not raw counts.

### Interview angle
> [!question] How it is asked
> "Of customers who got the coupon, 30% repurchased. Does that prove the coupon works?"

> [!tip] Strong answer includes
> - Need the comparison group (22.5% without), randomisation or adjustment for confounding
> - Percent within exposure groups; distinguish experiment, cohort, case-control designs
> - Next step: effect size (difference, ratio, odds ratio) with a confidence interval, then significance

---
## 2. Risk Difference, Relative Risk and Odds Ratio (Worked)
> 🟠 Tier 2 · _Key points:_ RD $=p_1-p_2$; RR $=p_1/p_2$; OR $=\frac{ad}{bc}$; CI for OR via $\log$; OR approximates RR only for rare outcomes

### Definition
For a 2x2 table with exposure rows and outcome columns ($a$ exposed with outcome, $b$ exposed without, $c$ unexposed with, $d$ unexposed without):

$$\text{RD}=p_1-p_2,\ \ p_1=\tfrac{a}{a+b},\ p_2=\tfrac{c}{c+d},\qquad \text{RR}=\frac{p_1}{p_2},\qquad \text{OR}=\frac{a/b}{c/d}=\frac{ad}{bc},\qquad SE(\ln\text{OR})=\sqrt{\tfrac1a+\tfrac1b+\tfrac1c+\tfrac1d}$$

The 95% CI for OR is $\exp(\ln\text{OR}\pm1.96\,SE)$; likewise $SE(\ln RR)=\sqrt{\frac1a-\frac1{n_1}+\frac1c-\frac1{n_2}}$. RD answers "how many extra repeats per 100 customers" and gives the **number needed to treat** $=1/\text{RD}$; RR answers "how many times as likely"; OR is the natural scale of logistic regression and the only measure valid in case-control studies. OR exaggerates RR when the outcome is common: 60% vs 40% gives RR = 1.5 but OR = 2.25. OR = 1 (or RR = 1, RD = 0) means no association.

### Example
Offer vs no offer: $p_1=0.300$, $p_2=0.225$. RD $=7.5$ pp (95% CI 1.4 to 13.6 pp); NNT $=13.3$, so about 14 offers per extra repeat purchase; RR $=1.333$ (CI 1.054 to 1.688); OR $=\frac{120\times310}{280\times90}=1.476$, $SE(\ln OR)=\sqrt{1/120+1/280+1/90+1/310}=0.1678$ and CI **(1.075, 2.028)**. At ₹50 per offer, the cost per incremental repeat purchase is $50\times13.33=$ **₹667**, so the offer pays only if a repeat purchase is worth well above that. Rare-outcome contrast: 3 vs 2 events per 1,000 gives RR = 1.50 and OR = 1.502.

### In the news
See news box. Public-health reports use RR and OR on counts such as dengue cases between districts; reading which measure was reported prevents overstating effects.

### Interview angle
> [!question] How it is asked
> "What is the difference between relative risk and odds ratio, and which would you report to the business?"

> [!tip] Strong answer includes
> - Definitions; OR approximates RR only for rare events; OR for case-control and logistic regression
> - Report absolute difference (RD, NNT) alongside relative measures; show the CI
> - Translate into money: cost per incremental conversion

---
## 3. Chi-square Test of Independence and Residuals
> 🟠 Tier 2 · _Key points:_ $\chi^2=\sum\frac{(O-E)^2}{E}$, d.f. $(r-1)(c-1)$; expected counts large enough; standardised residuals show which cells drive it

### Definition
$\chi^2=\sum_{i,j}\frac{(O_{ij}-E_{ij})^2}{E_{ij}}$ with $(r-1)(c-1)$ d.f. under independence. It tests whether an association exists, not how strong it is: report an effect size (Cramer's $V=\sqrt{\chi^2/(n\min(r-1,c-1))}$, or the odds ratio). Rule: expected counts at least 5 (otherwise Fisher exact or Monte Carlo, see [[206 Non-Parametric Tests]]). **Adjusted standardised residuals** $\frac{O-E}{\sqrt{E(1-r_i/n)(1-c_j/n)}}$ beyond $\pm2$ flag the cells responsible. The likelihood-ratio statistic $G^2=2\sum O\ln(O/E)$ is the GLM analogue. Chi-square assumes independent observations; repeated measures on the same customers require McNemar's test instead. General framework in [[089 Hypothesis Testing]].

### Example
Same offer table: $\chi^2=5.81$, d.f. 1, $p=0.0159$ (uncorrected); Yates-corrected $\chi^2=5.43$, $p=0.0198$; Fisher exact $p=0.0197$. All three agree at 5%. For $2\times2$, $\chi^2=z^2$ for the difference in proportions: $z=2.41$. Cramer's $V$ (here $\phi$) $=\sqrt{5.81/800}=0.085$: statistically significant but a small association, so significance is not size.

### In the news
See news box. State-versus-year tables of dengue counts could be tested for independence but are dominated by population size; GLMs with offsets handle that properly.

### Interview angle
> [!question] How it is asked
> "p = 0.016 on the chi-square test. Is the effect big?"

> [!tip] Strong answer includes
> - p-value does not measure effect size; report OR, difference and Cramer's V
> - Check expected counts and independence; paired data need McNemar
> - Note large $n$ makes tiny effects significant

---
## 4. Simpson's Paradox and the Cochran-Mantel-Haenszel Test
> 🟠 Tier 2 · _Key points:_ Aggregate vs stratified association can reverse; CMH pools stratum 2x2 tables under common odds ratio; Breslow-Day tests homogeneity

### Definition
**Simpson's paradox:** an association in aggregated data can reverse once a lurking variable (confounder) is used to stratify, because group sizes differ across strata. **Cochran-Mantel-Haenszel (CMH)** tests the null of conditional independence (common OR = 1) across $K$ strata, and gives the **Mantel-Haenszel pooled odds ratio**

$$\widehat{OR}_{MH}=\frac{\sum_k a_kd_k/n_k}{\sum_k b_kc_k/n_k}$$

Check homogeneity with the Breslow-Day (or Tarone) test; if odds ratios genuinely differ across strata, report them separately (effect modification). CMH is the stratified analogue of chi-square, and a logistic regression with a stratum covariate is the model-based version. Causal reading needs a causal diagram; stratifying on a collider or mediator can create bias, see [[214 Causal Inference & Experimentation Beyond A-B Tests]].

### Example
The offer is sent by channel. App users: with offer 210 of 300 repeat (70%), without offer 585 of 900 repeat (65%). Web users: with offer 180 of 900 repeat (20%), without 45 of 300 repeat (15%). Pooled: with offer 390/1,200 = **32.5%**, without 630/1,200 = **52.5%**, pooled OR $=0.44$: the offer looks harmful. Why: offers went mostly to low-propensity web users while the no-offer group is mostly high-propensity app users. Within each channel the offer helps (stratum ORs 1.26 and 1.42, homogeneity Breslow-Day $p=0.60$). CMH: $\chi^2=5.98$, $p=0.0145$ (0.0168 with continuity correction); $\widehat{OR}_{MH}=1.317$ (95% CI 1.056 to 1.643). Neither stratum alone is significant ($p=0.11$ and $0.055$) but pooling within strata is.

```python
from statsmodels.stats.contingency_tables import StratifiedTable
st = StratifiedTable([[[210,90],[585,315]], [[180,720],[45,255]]])
print(st.oddsratio_pooled, st.test_null_odds(correction=False).pvalue, st.test_equal_odds().pvalue)
```

### In the news
See news box. Comparing dengue burden between states or years without adjusting for population and reporting intensity invites the same reversal.

### Interview angle
> [!question] How it is asked
> "Overall conversion is lower for the promoted group, yet every segment looks better with the promotion. How can that be?"

> [!tip] Strong answer includes
> - Simpson's paradox: unequal allocation across a segment that drives conversion
> - Stratify or use regression; randomise to prevent it; CMH for stratified 2x2 tables
> - Decide by the causal question: which comparison is the fair one

---
## 5. The GLM Framework: Family, Link, Linear Predictor and Deviance
> 🟠 Tier 2 · _Key points:_ Random component (exponential family) + linear predictor + link $g(\mu)=\eta$; MLE by IRLS; deviance replaces sum of squares

### Definition
A **generalised linear model** has three parts: (1) a **random component**: $y_i$ from an exponential-family distribution (normal, binomial, Poisson, gamma, inverse Gaussian, negative binomial with fixed dispersion, Tweedie) with mean $\mu_i$; (2) a **systematic component** $\eta_i=\mathbf x_i^\top\boldsymbol\beta$; (3) a **link** $g(\mu_i)=\eta_i$. Coefficients are estimated by maximum likelihood via iteratively reweighted least squares ([[205 Sampling Distributions & Estimation]] on MLE).

| Outcome | Family | Canonical link | Interpretation of $e^\beta$ |
|---|---|---|---|
| Continuous | Gaussian | identity | (linear regression, [[090 Regression Analysis]]) |
| Binary 0/1 | Binomial | logit | odds ratio |
| Count (rate with offset) | Poisson | log | incidence rate ratio |
| Positive skewed (cost, time) | Gamma | inverse (log is common) | multiplicative effect on mean |

**Deviance** $D=2\left[\ell(\text{saturated})-\ell(\text{model})\right]$ measures lack of fit (for Gaussian it is the residual sum of squares). Nested models are compared by the drop in deviance, which is chi-square with d.f. equal to the number of added parameters (likelihood-ratio test). **Null deviance** is that of the intercept-only model; $1-D/D_0$ is a (McFadden-type) pseudo-$R^2$. Dispersion $\phi=1$ for binomial and Poisson; $\hat\phi=X^2/(n-p)$ (Pearson) checks that assumption. ML equivalents: [[095 Regression Algorithms]], [[096 Classification Algorithms]].

### Example
Poisson model for breakdown counts of 120 machines (sub-topic 9): null deviance 382.7, residual deviance 271.6 on 117 d.f. The drop of 111.2 on 2 d.f. is hugely significant, but residual deviance far exceeds its d.f. (117), a symptom of overdispersion, not of a good fit.

### In the news
See news box. Counts (dengue), proportions (case fatality) and costs sit in different GLM families; choosing the family from the outcome's nature is the first modelling decision.

### Interview angle
> [!question] How it is asked
> "What is a generalised linear model and how is it different from linear regression?"

> [!tip] Strong answer includes
> - Three components: distribution, linear predictor, link; mean transformed, not data
> - Examples: logistic (binomial/logit), Poisson (log), gamma (positive skewed)
> - Fitted by ML, assessed with deviance, AIC, residual diagnostics; overdispersion check

---
## 6. Logistic Regression: Fitting and Interpreting Odds
> 🟠 Tier 2 · _Key points:_ $\ln\frac{p}{1-p}=\beta_0+\beta_1x_1+\dots$; $e^{\beta}$ = odds ratio per unit; probability effects are not constant

### Definition
Logistic regression models a binary outcome: $\text{logit}(p)=\ln\frac p{1-p}=\mathbf x^\top\boldsymbol\beta$, so $p=\frac1{1+e^{-\mathbf x^\top\boldsymbol\beta}}$. Coefficient $\beta_j$ is the change in log-odds per unit of $x_j$ holding others fixed; **$e^{\beta_j}$ is the odds ratio** (OR above 1 raises the odds). Interpretation with odds: OR 1.6 does not mean 60% higher probability. Fitted by ML; Wald z-tests per coefficient, likelihood-ratio tests for blocks. Needs enough events (rule of thumb of about 10 events per predictor), no perfect separation, and no strong multicollinearity. Classification threshold choice and ROC are covered in [[096 Classification Algorithms]] and [[098 Model Selection & Optimization]].

### Example
Churn model on 2,000 simulated customers (statsmodels `logit`): churn rate 25.9%. Estimates:

| Predictor | $\hat\beta$ | SE | OR | 95% CI for OR |
|---|---|---|---|---|
| Intercept | 0.136 | 0.150 | 1.15 | 0.85 to 1.54 |
| Tenure (months) | -0.0706 | 0.0060 | **0.932** | 0.921 to 0.943 |
| Complaints (per year) | 0.472 | 0.050 | **1.604** | 1.454 to 1.768 |
| Premium plan (1/0) | -0.803 | 0.125 | **0.448** | 0.351 to 0.572 |

Reading: each extra month of tenure cuts the odds of churn by 6.8%; each complaint multiplies odds by 1.60; premium plan cuts odds by 55%. Prediction for a non-premium customer with 12 months tenure: zero complaints gives odds $e^{0.136-0.0706\times12}=0.491$, $p=33.0\%$; three complaints multiply odds by $1.604^3=4.12$ to 2.03, so $p=67.0\%$. Overall fit: LR $\chi^2=307.8$ (3 d.f., $p<10^{-60}$), deviance 1,978.2 (null 2,285.9), McFadden pseudo-$R^2=0.135$, AIC 1,986.2, AUC 0.744. Dropping complaints raises AIC to 2,077.9 (LR test 93.8, $p\approx10^{-22}$).

### In the news
See news box. Case-fatality or hospitalisation rates among dengue patients (binary outcomes per patient) are modelled with logistic regression and reported as odds ratios.

### Interview angle
> [!question] How it is asked
> "A logistic model gives a coefficient of 0.47 for complaints. How do you explain it to a manager?"

> [!tip] Strong answer includes
> - $e^{0.47}=1.60$: each complaint raises the odds of churn by about 60%
> - Convert to probabilities at realistic profiles (33% to 67% in the example) because odds are not probabilities
> - Mention model checks (calibration, AUC) and the business action: retention triggers at 2+ complaints

---
## 7. Marginal Effects and Predicted Probabilities
> 🟠 Tier 2 · _Key points:_ $\partial p/\partial x_j=\beta_jp(1-p)$; varies with $x$; AME vs MEM; discrete change for dummies

### Definition
In a logit model the effect of $x_j$ on the **probability** is $\frac{\partial p}{\partial x_j}=\beta_j\,p(1-p)$, largest at $p=0.5$ (where it is $\beta_j/4$, the "divide by 4 rule") and small at extreme probabilities. **Average marginal effect (AME)** averages this over every observation; **marginal effect at the mean (MEM)** evaluates at average covariates; for dummies use the discrete change in predicted probability. AMEs are comparable across models (logit and probit) and are what a business audience usually wants ("percentage points"). Standard errors by the delta method; statsmodels `get_margeff()`.

### Example
Churn model: AMEs are **-0.0115** for tenure (each extra month cuts churn probability by about 1.15 pp), **+0.0770** for each complaint (+7.7 pp) and **-0.1308** for premium (-13.1 pp). Check: at the mean churn probability $0.2585$, $\beta p(1-p)=0.4723\times0.2585\times0.7415=0.0905$ for complaints, which differs from the AME of 0.077 because the AME averages over customers whose probabilities range from very low to high. For the non-premium 12-month profile, the first complaint raises churn from 33.0% to about 44% (odds ratio 1.60 on odds 0.49) and moving to 3 complaints reaches 67%. Marginal effects are bigger for customers in the middle of the risk range, which is where retention efforts have most leverage.

### In the news
See news box. Public-health communication prefers percentage-point differences in risk to odds ratios for exactly this reason.

### Interview angle
> [!question] How it is asked
> "Odds ratios confuse our executives. How do you present logistic regression results?"

> [!tip] Strong answer includes
> - Average marginal effects in percentage points, and predicted probabilities for named customer profiles
> - Note effects vary with the baseline risk
> - Pair with decision metrics (lift, cost of intervention)

---
## 8. Probit and Other Binary Links
> 🟠 Tier 2 · _Key points:_ $\Phi^{-1}(p)=\mathbf x^\top\boldsymbol\beta$; latent-variable view; coefficients about logit divided by 1.6-1.8; complementary log-log for asymmetric/rare events

### Definition
**Probit** uses the normal CDF link: $p=\Phi(\mathbf x^\top\boldsymbol\beta)$, from a latent variable $y^*=\mathbf x^\top\boldsymbol\beta+\varepsilon$ with $\varepsilon\sim N(0,1)$ and $y=1$ if $y^*>0$. Logit assumes a logistic error (heavier tails); both give S-shaped curves and nearly identical fits. Probit coefficients are roughly logit coefficients divided by about 1.6-1.8 (the logistic variance is $\pi^2/3$), and there is no odds-ratio interpretation: coefficients are in z-score units, so report marginal effects. **Complementary log-log** is asymmetric and natural for discrete-time survival or rare events ([[211 Reliability & Survival Analysis]]). Probit is conventional in economics (ordered probit, bivariate probit); logit dominates in analytics because of odds ratios.

### Example
Same churn data: probit coefficients tenure $-0.0398$, complaints $0.274$, premium $-0.453$. Ratios logit/probit: 1.77, 1.72, 1.77. AMEs are almost identical: tenure -0.0112, complaints +0.0768, premium -0.1268 (logit: -0.0115, +0.0770, -0.1308). AIC: logit 1,986.2, probit 1,990.6, a marginal preference for logit here. Conclusion: the link rarely changes decisions; the choice should follow interpretation needs.

### In the news
See news box. Whichever link is used, communicating to non-specialists means translating to probabilities or marginal effects.

### Interview angle
> [!question] How it is asked
> "Logit or probit: does it matter?"

> [!tip] Strong answer includes
> - Almost always the same predictions and AMEs; logit gives odds ratios, probit assumes normal latent errors
> - Compare via AIC or just choose by interpretability
> - Mention cloglog for asymmetric/rare event modelling

---
## 9. Poisson Regression for Counts, Rates and Offsets
> 🟠 Tier 2 · _Key points:_ $\ln\mu_i=\mathbf x_i^\top\boldsymbol\beta+\ln(t_i)$; offset $\ln(\text{exposure})$ with coefficient fixed at 1; $e^{\beta}$ = incidence rate ratio

### Definition
For non-negative integer counts $y_i\sim\text{Poisson}(\mu_i)$ with $\ln\mu_i=\mathbf x_i^\top\boldsymbol\beta$. If observations differ in **exposure** $t_i$ (machine-hours, population, days at risk), model the rate with an **offset**: $\ln\mu_i=\ln t_i+\mathbf x_i^\top\boldsymbol\beta$, i.e. $\mu_i/t_i=e^{\mathbf x_i^\top\boldsymbol\beta}$. The offset has coefficient exactly 1 (not estimated). $e^{\beta_j}$ is the **incidence rate ratio (IRR)**, the multiplicative change in the rate per unit of $x_j$. Assumptions: events independent, mean equals variance (equidispersion), log-linear effects. Use for defects per unit, calls per hour, breakdowns per machine-hour, claims per policy-year; see reliability in [[155 Reliability Engineering & Maintenance Optimisation]] and queues in [[149 Queueing Theory & Waiting-Line Analysis]].

### Example
Breakdowns at 120 machines (simulated), exposure 800 to 4,000 machine-hours, predictors age (years) and a preventive-maintenance (PM) flag. Poisson GLM with $\ln(\text{hours}/1000)$ offset:

| Term | $\hat\beta$ | SE | IRR | 95% CI |
|---|---|---|---|---|
| Intercept | -0.064 | 0.127 | 0.94 | 0.73 to 1.20 |
| Age (per year) | 0.0894 | 0.0121 | **1.094** | 1.068 to 1.120 |
| PM program | -0.767 | 0.103 | **0.465** | 0.379 to 0.569 |

Reading: each extra year of machine age raises the breakdown rate by 9.4%; preventive maintenance cuts it by 53.5%. Without the offset the model would confuse long-running machines with unreliable ones. Residual deviance 271.6 on 117 d.f., Pearson $X^2/\text{d.f.}=2.41$: the equidispersion assumption fails (next sub-topic), so these SEs are too small.

```python
import statsmodels.api as sm, statsmodels.formula.api as smf, numpy as np
m = smf.glm('y ~ age + pm', df, family=sm.families.Poisson(), offset=np.log(df.hours/1000)).fit()
print(np.exp(m.params))
```

### In the news
See news box. Dengue counts per state use population as the exposure; the same offset logic converts counts into incidence rates.

### Interview angle
> [!question] How it is asked
> "You want to compare accident counts across plants with very different hours worked. How do you model it?"

> [!tip] Strong answer includes
> - Poisson (or negative binomial) regression with log(hours) as an offset; interpret as rate ratios
> - Check overdispersion and excess zeros
> - Do not divide counts by exposure and run OLS blindly: heteroskedasticity and small counts

---
## 10. Overdispersion: Quasi-Poisson, Negative Binomial and Zero-Inflation
> 🟠 Tier 2 · _Key points:_ Pearson $X^2/\text{d.f.}$ well above 1; fix with robust/quasi SEs or negative binomial ($\text{Var}=\mu+\alpha\mu^2$); zero-inflated/hurdle for excess zeros

### Definition
**Overdispersion** means variance exceeds the mean (unobserved heterogeneity, clustering, contagion). Poisson coefficients stay consistent but SEs are too small and p-values too optimistic. Diagnose with Pearson $X^2/(n-p)$ (above about 1.5 is a concern) or a score/LR test of $\alpha=0$. Remedies: (1) **quasi-Poisson / robust (sandwich) SEs**, scaling SEs by $\sqrt{\hat\phi}$; (2) **negative binomial (NB2)** with $\text{Var}(y)=\mu+\alpha\mu^2$, a gamma-mixed Poisson, which models extra variance and gives a likelihood for AIC; (3) **zero-inflated Poisson/NB** or **hurdle models** when zeros are excess (structural zeros, such as machines that never run). Underdispersion is rare (use Conway-Maxwell-Poisson or quasi models).

### Example
Same machine data. Pearson dispersion $\hat\phi=2.41$, so quasi-Poisson SEs are $\sqrt{2.41}=1.55$ times larger: age SE rises from 0.0121 to 0.0188 and PM from 0.103 to 0.160. **Negative binomial** fit: $\hat\alpha=0.365$ (SE 0.100; LR test of $\alpha=0$: 44.8, $p<0.001$), age IRR **1.102** (1.062 to 1.143), PM IRR **0.457** (0.335 to 0.624). AIC: Poisson 573.0, NB **530.2**, a drop of 42.8, decisive for NB. Predicted breakdown rate per 1,000 machine-hours for an 8-year-old machine: 1.95 without PM and 0.89 with PM. Conclusions about direction are unchanged, but the intervals are about 50% wider than Poisson's, as they should be.

### In the news
See news box. The yearly swings in dengue counts (2,89,235 in 2023 to 2,33,519 in 2024) are far larger than Poisson variation around a stable mean would allow; overdispersion is the norm for epidemic counts.

### Interview angle
> [!question] How it is asked
> "Your Poisson model has a dispersion statistic of 2.4. What do you do?"

> [!tip] Strong answer includes
> - Overdispersion: SEs understated; use quasi-Poisson/robust SEs or negative binomial
> - Check for excess zeros (zero-inflated or hurdle), omitted covariates, clustering
> - Compare by AIC and by predictive checks; keep the offset

---
## 11. Ordinal Logistic Regression (Proportional Odds)
> 🟠 Tier 2 · _Key points:_ $\text{logit}\,P(Y\le j)=\theta_j-\mathbf x^\top\boldsymbol\beta$; one slope per predictor; test proportional-odds assumption

### Definition
For an ordered outcome (rating low/medium/high, Likert 1-5, severity) the **proportional-odds (cumulative logit) model** is $\ln\frac{P(Y\le j)}{P(Y>j)}=\theta_j-\mathbf x^\top\boldsymbol\beta$, $j=1,\dots,J-1$. The thresholds $\theta_j$ increase with $j$; $\boldsymbol\beta$ is common to all cut-offs, so $e^{\beta}$ is the odds ratio of being in a higher category for a one-unit increase in $x$. The proportional-odds assumption (same $\beta$ for every cut) can be checked with the Brant test or by comparing with a partial-proportional model. Treating a 3 to 5-point ordinal scale as a numeric outcome in OLS is common but loses information; use multinomial logistic if the categories are unordered. Related: non-parametric ordinal methods in [[206 Non-Parametric Tests]].

### Example
900 simulated customers rate a delivery experience Low/Medium/High (22.6%, 30.3%, 47.1%), predictors days of delay and premium membership. `OrderedModel` (statsmodels, logit): delay $\hat\beta=-0.350$ (SE 0.034), OR **0.704** per extra day of delay; premium $\hat\beta=0.550$ (SE 0.132), OR **1.734**. Reading: each day of delay cuts the odds of a higher rating by about 30%; premium customers have about 1.7 times the odds of a higher rating. Thresholds: $\hat\theta_1=-1.871$ and $\hat\theta_2=-1.871+e^{0.428}=-0.337$ (statsmodels reports the second as the log of the increment).

### In the news
See news box. Disease severity grades (for example mild, moderate, severe) are ordered outcomes of the kind this model handles.

### Interview angle
> [!question] How it is asked
> "Satisfaction is on a 1-5 scale. Linear regression or something else?"

> [!tip] Strong answer includes
> - Ordinal logistic (proportional odds) respects ordering without assuming equal spacing
> - Interpret $e^\beta$ as odds of a higher category; test the proportional-odds assumption
> - Linear regression acceptable only as a quick approximation for 5+ categories; report both if needed

---
## 12. Goodness of Fit and Model Comparison: Deviance, Hosmer-Lemeshow, AIC, LR Tests
> 🟠 Tier 2 · _Key points:_ Deviance and Pearson $X^2$ (grouped data); Hosmer-Lemeshow for binary; AIC/BIC; LR test for nested; calibration and AUC

### Definition
- **Likelihood-ratio test** for nested models: $2(\ell_{full}-\ell_{reduced})\sim\chi^2_{\text{extra parameters}}$. **AIC** $=2k-2\ell$ and **BIC** $=k\ln n-2\ell$ for non-nested comparison on the same data.
- **Deviance and Pearson $X^2$** as goodness-of-fit tests are valid only for grouped data with large expected counts (they are not chi-square for individual binary data); for counts, compare to the residual d.f. as a dispersion check.
- **Hosmer-Lemeshow (HL):** sort by predicted probability, split into $g$ (usually 10) groups, compare observed and expected events $\sum\frac{(O_g-E_g)^2}{E_g(1-E_g/n_g)}\sim\chi^2_{g-2}$. A small p-value means poor calibration; the test has low power for small $n$ and is oversensitive for huge $n$, so also plot a calibration curve.
- **Discrimination:** AUC/ROC (the ability to rank), distinct from calibration. Also check influential points (Cook's distance, leverage), residual plots (deviance/Pearson/quantile residuals) and multicollinearity (VIF).

### Example
Churn model: HL $\chi^2=8.89$ on 8 d.f., $p=0.35$: no evidence of miscalibration; AUC = 0.744 (moderate discrimination; calibration and discrimination are separate properties). Model comparison by AIC: with complaints 1,986.2, without 2,077.9; logit 1,986.2 vs probit 1,990.6. Poisson vs NB for counts: AIC 573.0 vs 530.2 and LR for dispersion 44.8: the GLM family choice is itself testable. In production, monitor calibration drift as customers' behaviour changes (see [[220 Responsible AI, Explainability & Model Governance]]).

### In the news
See news box. A modeller fitting the NCVBDC state-year counts would compare Poisson, negative binomial and zero-inflated alternatives by AIC and out-of-sample forecasts.

### Interview angle
> [!question] How it is asked
> "How do you validate a logistic regression model beyond accuracy?"

> [!tip] Strong answer includes
> - Discrimination (AUC, KS, lift) and calibration (HL, calibration plot, Brier score), on a hold-out or cross-validated sample
> - LR tests/AIC for model selection; residual and influence diagnostics
> - Business metric: expected profit at the chosen threshold; ongoing monitoring

---
## 13. ⭐ Advanced: Gamma GLMs, Separation, Rare Events and a Recipe Book
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Gamma GLM with log link** models positive skewed outcomes (claim amounts, repair cost, lead time) with variance proportional to mean squared, so effects are multiplicative on the mean and no log-transform bias correction is needed (compare OLS on $\ln y$). **Perfect or quasi-complete separation** (a predictor splits the outcome perfectly) makes ML coefficients diverge: use Firth's penalised likelihood, ridge/lasso penalties, or merge categories. **Rare events** (very few 1s) need Firth/exact methods or case-control sampling with intercept correction. **Multinomial logit** handles unordered categories (brand choice; links to conjoint in [[207 Multivariate Statistics - PCA, Factor Analysis & Cluster Analysis]]). **Mixed-effects GLMs/GEE** handle repeated measures and clustered data (stores, patients). **Tweedie** GLMs model insurance pure premium with many zeros plus skewed positives. Software notes in [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]]; Python workflow basics in [[067 Statistical Analysis in Python]].

### Example
Repair cost for 900 simulated service tickets (₹, gamma distributed) with predictors days of delay and premium flag. `smf.glm('cost ~ delay + prem', family=Gamma(link=Log()))`: exponentiated coefficients 140 (baseline mean cost ₹140), 1.058 per delay day (+5.8% cost per extra day), 1.355 for premium (+35.5%); dispersion about 0.33. The multiplicative reading matches how costs behave. Executed one-line recipes:

```python
import statsmodels.api as sm, statsmodels.formula.api as smf
smf.logit('y ~ x1 + x2', df).fit()                                   # logistic
smf.glm('y ~ x', df, family=sm.families.Poisson(), offset=off).fit()  # Poisson with offset
smf.glm('c ~ x', df, family=sm.families.Gamma(sm.families.links.Log())).fit()
from statsmodels.miscmodels.ordinal_model import OrderedModel         # ordinal logit
from statsmodels.stats.contingency_tables import StratifiedTable      # CMH
```

### In the news
See news box. Case counts, case-fatality and treatment cost for dengue are respectively Poisson/NB, binomial and gamma outcomes; one public-health dataset can need all three GLM families.

### Interview angle
> [!question] How it is asked
> "Your outcome is claim cost, always positive and right-skewed. How would you model it?"

> [!tip] Strong answer includes
> - Gamma GLM with log link (or lognormal on log scale with smearing correction); effects are percentages of mean cost
> - If many zeros: two-part (frequency x severity) or Tweedie
> - Diagnose with deviance residuals, calibration by decile, and compare using out-of-sample metrics
