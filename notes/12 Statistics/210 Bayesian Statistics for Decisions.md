---
tags: [statistics, tier2]
area: Statistics
topic: "Bayesian Statistics for Decisions"
tier: Tier 2
roles: Analytics / PM / Consulting
status: complete
subtopics: 14
---
# Bayesian Statistics for Decisions

⬅ [[209 Generalised Linear Models & Categorical Data Analysis]] · [[_Index - Statistics|Statistics]] · [[211 Reliability & Survival Analysis]] ➡

> **Area:** Statistics · **Priority:** 🟠 Tier 2 · **Target roles:** Analytics / PM / Consulting

## Sub-topics in this note
1. [[#1. Bayes' Rule for Distributions]]
2. [[#2. Priors: Informative, Weak and Non-informative]]
3. [[#3. Beta-Binomial: Updating a Conversion or Defect Rate]]
4. [[#4. Gamma-Poisson: Updating a Rate of Events]]
5. [[#5. Normal-Normal: Updating a Mean]]
6. [[#6. Credible Interval vs Confidence Interval]]
7. [[#7. Posterior Predictive Distribution]]
8. [[#8. Bayesian A/B Testing: Probability to Beat Control and Expected Loss]]
9. [[#9. Thompson Sampling and Multi-Armed Bandits]]
10. [[#10. Hierarchical Models and Shrinkage]]
11. [[#11. MCMC Overview and PyMC]]
12. [[#12. Bayesian vs Frequentist: The Interview Comparison]]
13. [[#13. ⭐ Advanced: Expected-Loss Launch Decisions in Rupees]]
14. [[#14. ⭐ Advanced: Prior Sensitivity, Peeking and Bayesian Stopping Rules]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Bayesian methods move from academic to regulatory and marketing-budget practice
> **FDA draft guidance on Bayesian methodology in drug trials (January 2026).** The US FDA issued a draft guidance, reported as "Use of Bayesian Methodology in Clinical Trials of Drug and Biological Products", on how Bayesian designs can support approval, including primary inference in Phase III. Secondary summaries describe three themes: priors must be justified and pre-specified, borrowing from historical data needs safeguards such as discounting and sensitivity analysis, and success is declared when a posterior probability (for example, that the effect exceeds a clinically meaningful threshold) reaches a pre-agreed level. Operating characteristics are evaluated by simulation. Summaries differ by a few days on the exact release date (9 vs 12 January 2026), so quote it as "January 2026". ([Alston and Bird summary](https://www.alston.com/en/insights/publications/2026/01/fda-bayesian-guidance-drug-trials); [arXiv practitioner review](https://arxiv.org/html/2601.14701v1))
>
> **Google open-sources Meridian, a Bayesian marketing mix model (29 January 2025).** Google made Meridian available to everyone, describing it as built on Bayesian causal inference that lets marketers blend prior knowledge with data. Its announcement says over 20 measurement partners were trained and certified, that it was tested with hundreds of brands, and that results of incrementality experiments can be fed in as priors. This is the "informative prior from an experiment" idea of this note applied to budget allocation across media channels. ([Google blog](https://blog.google/products/ads-commerce/meridian-marketing-mix-model-open-to-everyone/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Bayes' Rule for Distributions
> 🟠 Tier 2 · _Key points:_ Posterior ∝ likelihood × prior; parameters are random variables; update as data arrives

### Definition
Bayesian inference treats an unknown parameter $\theta$ (a conversion rate, a defect rate, a mean lead time) as a quantity with a probability distribution that expresses current knowledge. Bayes' rule, extended from events (see [[087 Probability Fundamentals]]) to distributions, updates the **prior** $p(\theta)$ with the **likelihood** $p(\text{data}\mid\theta)$ to give the **posterior**:

$$p(\theta\mid \text{data})=\frac{p(\text{data}\mid\theta)\,p(\theta)}{p(\text{data})}\;\propto\;p(\text{data}\mid\theta)\,p(\theta)$$

The denominator $p(\text{data})=\int p(\text{data}\mid\theta)p(\theta)\,d\theta$ is a normalising constant (the "evidence"). It is hard to compute for complex models, which is why MCMC exists (sub-topic 11). Three properties to remember:
- **Sequential updating:** today's posterior is tomorrow's prior; the final posterior is the same whether data arrive in one batch or one point at a time.
- **Data dominate eventually:** as $n$ grows the likelihood overwhelms any reasonable prior, and Bayesian and frequentist answers converge.
- **Output is a distribution**, so questions like "what is the probability variant B beats A?" have a direct answer, which a p-value does not give (see [[089 Hypothesis Testing]]).

### Example
A discrete warm-up. A supplier's lots are "good" (2% defective) or "bad" (10% defective). Prior belief from history: P(bad) = 20%. A sample of 20 units shows 3 defectives. Likelihoods: $\binom{20}{3}0.02^3 0.98^{17}=0.0065$ (good) and $\binom{20}{3}0.10^3 0.90^{17}=0.1901$ (bad). Posterior P(bad) $=\frac{0.1901\times0.2}{0.1901\times0.2+0.0065\times0.8}=\mathbf{0.880}$. One sample moved belief from 20% to 88%, which is the logic behind a lot-by-lot decision in [[212 Acceptance Sampling & Measurement System Analysis (Gauge R&R)]].

### In the news
See news box. The FDA guidance is essentially "prior x likelihood = posterior", with rules about how the prior may be built and how the final posterior probability is judged.

### Interview angle
> [!question] How it is asked
> "Explain Bayes' rule in the context of a parameter, not an event. What are the prior, likelihood and posterior?"

> [!tip] Strong answer includes
> - Posterior is proportional to likelihood times prior; denominator is just a normaliser
> - Concrete business parameter (conversion rate) with a prior from past launches
> - Sequential updating and convergence of Bayesian and frequentist answers with big data
> - Mention that the output is a full distribution, which supports decisions directly

---
## 2. Priors: Informative, Weak and Non-informative
> 🟠 Tier 2 · _Key points:_ Prior = encoded knowledge; strength measured in pseudo-observations; always check sensitivity

### Definition
A **prior** is the distribution of $\theta$ before seeing the current data. Types:
- **Informative prior:** built from historical data, earlier experiments or expert judgement (for example, "past checkout tests gave conversion near 4%, give or take 1 pp"). Powerful with small samples, risky if wrong.
- **Weakly informative prior:** rules out absurd values while letting data speak (for example, a conversion rate prior that puts almost no mass above 50%). This is the recommended default in modern practice.
- **Non-informative / flat prior:** Beta(1,1) or a very wide Normal. Reproduces frequentist-like answers but can allow silly values and is not truly "objective" (a flat prior on $p$ is not flat on odds).
- **Conjugate prior:** a family where prior and posterior have the same form (sub-topics 3 to 5), giving closed-form updates.

For conjugate models, prior strength is easy to read: a Beta($a$,$b$) prior behaves like $a+b$ earlier observations. Beta(4,96) says "equivalent to 100 past visitors with 4 conversions". How to build one: fit a Beta to the historical spread of conversion rates across past tests, or use an external experiment (as Google Meridian does with incrementality tests). Pre-specify the prior before the test, and report how conclusions change under sceptical and enthusiastic priors.

### Example
Same data (48 conversions in 1,000 sessions, raw 4.8%) under three priors centred near 4%:
- Flat Beta(1,1): posterior mean $\frac{1+48}{2+1000}=4.89\%$.
- Beta(4,96), weight 100: $\frac{4+48}{100+1000}=4.73\%$.
- Strong Beta(40,960), weight 1,000: $\frac{40+48}{1000+1000}=4.40\%$, pulled well toward 4%.
With 5,000 sessions per arm the choice among weak priors barely matters, but a very heavy prior (weight 10,000) still pulls noticeably (see sub-topic 14).

### In the news
See news box. Both the FDA guidance and Meridian turn on how a prior is justified; the FDA asks sponsors to document rationale and run sensitivity analysis, Meridian lets teams set priors from experiments.

### Interview angle
> [!question] How it is asked
> "Isn't choosing a prior subjective? How do you defend it to a sceptical stakeholder?"

> [!tip] Strong answer includes
> - Every method has assumptions; the Bayesian prior is explicit and inspectable
> - Weakly informative default, informative only with documented evidence
> - Express prior strength as pseudo-observations; pre-register it
> - Show sensitivity: results under sceptical, neutral and optimistic priors

---
## 3. Beta-Binomial: Updating a Conversion or Defect Rate
> 🟠 Tier 2 · _Key points:_ Beta(a,b) prior + x successes in n trials → Beta(a+x, b+n−x); mean = (a+x)/(a+b+n)

### Definition
For a proportion $p$ with prior $p\sim\text{Beta}(a,b)$ and data $x\sim\text{Binomial}(n,p)$, the posterior is again Beta:

$$p\mid x\sim\text{Beta}(a+x,\;b+n-x),\qquad E[p\mid x]=\frac{a+x}{a+b+n}$$

The posterior mean is a **weighted average** of prior mean $a/(a+b)$ and sample proportion $x/n$, with weights $\frac{a+b}{a+b+n}$ and $\frac{n}{a+b+n}$. Beta($a$,$b$) has variance $\frac{ab}{(a+b)^2(a+b+1)}$ and mode $\frac{a-1}{a+b-2}$ for $a,b>1$. Use it for conversion, click-through, defect proportion, on-time delivery (see [[088 Probability Distributions]] for the Binomial).

### Example
A food-delivery app's past checkout tests suggest conversion around 4%. Encode as Beta(4,96) (mean 4%, weight 100). A new flow gets 48 conversions from 1,000 sessions (4.8%). Posterior: Beta(52,1048).
- Posterior mean $=52/1100=\mathbf{4.73\%}$ (between prior 4.0% and sample 4.8%; prior weight $100/1100=9\%$).
- Posterior sd $=0.64$ pp; 95% credible interval $=\mathbf{[3.55\%,\,6.06\%]}$.
- $P(p>4\%)=\mathbf{87.6\%}$: "88% sure the new flow beats today's 4%".
- Compare a Wald confidence interval from the same data: $4.8\%\pm1.96\sqrt{0.048\times0.952/1000}=[3.48\%,\,6.12\%]$, slightly wider because the prior adds information.

### In the news
See news box. Posterior probabilities of exactly this form ("probability the effect exceeds a threshold") are the success criterion the FDA draft guidance describes.

### Interview angle
> [!question] How it is asked
> "We saw 12 conversions out of 150 visits on a new landing page. Prior from other pages is about 6%. What is your estimate?"

> [!tip] Strong answer includes
> - Convert prior to Beta pseudo-counts, add successes and failures, quote posterior mean and interval
> - Interpret weight: prior contributes $a+b$ observations, data $n$
> - State a decision-ready probability such as P(rate > 6%)
> - Note that with large $n$ the prior washes out

---
## 4. Gamma-Poisson: Updating a Rate of Events
> 🟠 Tier 2 · _Key points:_ Gamma(α,β) prior + Poisson counts → Gamma(α+Σx, β+n); predictive is negative binomial

### Definition
For an event rate $\lambda$ (defects per shift, breakdowns per month, support tickets per day) with Poisson counts $x_1,\dots,x_n$ and prior $\lambda\sim\text{Gamma}(\alpha,\beta)$ (shape, rate), the posterior is

$$\lambda\mid x\sim\text{Gamma}\!\left(\alpha+\sum x_i,\;\beta+n\right),\qquad E[\lambda\mid x]=\frac{\alpha+\sum x_i}{\beta+n}$$

Interpretation: $\alpha$ is prior "event count" and $\beta$ is prior "exposure periods". The posterior mean is a weighted average of prior mean $\alpha/\beta$ and sample mean $\bar x$. Pair with exposure: if exposure differs by period, use $\beta+\sum t_i$. The Poisson model is covered in [[088 Probability Distributions]] and the regression version in [[209 Generalised Linear Models & Categorical Data Analysis]].

### Example
A press line has historically averaged 3 stoppages per day. Prior Gamma(6,2): mean 3, equal to 2 days of experience. Over 5 days the counts are 3, 5, 4, 6, 3 (total 21, sample mean 4.2). Posterior: Gamma(27, 7).
- Mean $=27/7=\mathbf{3.86}$ per day (prior 3.0, data 4.2, pulled toward data by weight $5/7$).
- 95% credible interval for $\lambda$: **[2.54, 5.44]**.
- Predictive distribution for tomorrow is negative binomial with mean 3.86 and $P(\text{at least 8 stoppages})=\mathbf{5.5\%}$, wider than a Poisson(3.86) because uncertainty about $\lambda$ is carried through.

### In the news
See news box. Count-rate updating like this is the simplest member of the family of models that Bayesian tools such as Meridian generalise.

### Interview angle
> [!question] How it is asked
> "Machines at a new plant failed 2 times in 4 months. How would you estimate the monthly failure rate and quantify uncertainty?"

> [!tip] Strong answer includes
> - Poisson likelihood with a Gamma prior, show the update rule
> - Prior from similar machines; weak prior if none
> - Report interval and probability of exceeding a service threshold
> - Link to reliability work in [[211 Reliability & Survival Analysis]] when exposure times matter

---
## 5. Normal-Normal: Updating a Mean
> 🟠 Tier 2 · _Key points:_ Precision-weighted average; posterior precision = prior precision + data precision

### Definition
For a mean $\mu$ with known data standard deviation $\sigma$, prior $\mu\sim N(\mu_0,\tau_0^2)$ and sample mean $\bar x$ from $n$ observations, the posterior is Normal. Working in **precision** ($1/\text{variance}$) makes it simple:

$$\frac{1}{\tau_n^2}=\frac{1}{\tau_0^2}+\frac{n}{\sigma^2},\qquad \mu_n=\frac{\mu_0/\tau_0^2+n\bar x/\sigma^2}{1/\tau_0^2+n/\sigma^2}$$

So the posterior mean is a **precision-weighted average** and uncertainty always shrinks after seeing data. With unknown $\sigma$ the exact result uses a Normal-Inverse-Gamma prior and a $t$ posterior, but the known-$\sigma$ case shows the mechanics (compare the sampling-distribution logic in [[205 Sampling Distributions & Estimation]]).

### Example
A new vendor's mean delivery lead time (hours). Procurement's prior from similar vendors: $N(100,15^2)$. Nine deliveries average 112 hours with $\sigma=12$ known.
- Prior precision $=1/225=0.00444$; data precision $=9/144=0.0625$; posterior precision $=0.06694$.
- Posterior sd $=3.86$ h. Posterior mean $=\mathbf{111.2}$ h; weights: prior 6.6%, data 93.4%.
- 95% credible interval $=[103.6,\;118.8]$. Frequentist 95% CI: $112\pm1.96\times4=[104.2,\;119.8]$.
- Predictive sd for the next single delivery $=\sqrt{3.86^2+12^2}=12.6$ h.

### In the news
See news box. Normal-Normal blending of an earlier estimate with new data is exactly how experiment results become priors in media-mix models.

### Interview angle
> [!question] How it is asked
> "You have a prior estimate and a new sample, both with uncertainty. How do you combine them?"

> [!tip] Strong answer includes
> - Precision-weighted average, inverse-variance logic
> - Posterior variance smaller than both inputs
> - Prior weight shrinks as $n$ grows
> - Distinguish uncertainty in the mean (posterior) from spread of a single new observation (predictive)

---
## 6. Credible Interval vs Confidence Interval
> 🟠 Tier 2 · _Key points:_ Credible = probability statement about θ given data; CI = long-run coverage of the procedure

### Definition
A **95% credible interval** is a range that contains $\theta$ with 95% posterior probability: "given the data and prior, there is a 95% probability the true rate lies here". It can be **equal-tailed** (2.5% and 97.5% quantiles) or the **highest density interval (HDI)**, the shortest interval holding 95% mass (better for skewed posteriors). A **95% confidence interval** (see [[092 Sampling & Experimental Design]]) is a statement about the procedure: if the experiment were repeated many times, 95% of such intervals would cover the fixed true $\theta$. For any one realised interval, a frequentist says "it either covers or not".

Bayesian add-ons: **ROPE** (region of practical equivalence) says "treat differences smaller than 0.1 pp as no change" and reports the posterior mass inside it. The two intervals are numerically close with weak priors and large samples, but differ with small samples, strong priors, or boundaries (for example, a rate near 0).

### Example
48 conversions in 1,000 sessions. Wald CI: [3.48%, 6.12%]. Bayesian with flat prior: [3.64%, 6.31%] (mean 4.89%). Informative Beta(4,96): [3.55%, 6.06%]. Nearly identical here. With 2 conversions in 20 sessions, the Wald interval $10\%\pm13\%$ spans [-3%, 23%], a negative rate, while the flat-prior Beta(3,19) credible interval is [3.0%, 30.4%] (mean 13.6%), always inside 0 to 1 and honest about the huge uncertainty.

### In the news
See news box. Regulators and marketers who adopt Bayesian methods report posterior intervals and probabilities rather than p-values, because they answer the question managers actually ask.

### Interview angle
> [!question] How it is asked
> "What is the difference between a 95% confidence interval and a 95% credible interval? Which would you give a business stakeholder?"

> [!tip] Strong answer includes
> - Credible = probability of θ in the interval given data and prior; CI = long-run coverage
> - Say that stakeholders read CIs as credible intervals anyway, which is a point for Bayesian reporting
> - Mention HDI vs equal-tailed and ROPE
> - Agree they converge with big data and weak priors

---
## 7. Posterior Predictive Distribution
> 🟠 Tier 2 · _Key points:_ Average the likelihood over the posterior; predictions carry parameter uncertainty

### Definition
The **posterior predictive distribution** gives the probability of a future observation $\tilde y$ after integrating over everything still unknown about $\theta$:

$$p(\tilde y\mid\text{data})=\int p(\tilde y\mid\theta)\,p(\theta\mid\text{data})\,d\theta$$

Plugging in a single point estimate (for example, $\hat p=4.8\%$) ignores parameter uncertainty and gives intervals that are too narrow. For conjugate models the predictive is known: Beta-Binomial for future successes, Negative Binomial for Gamma-Poisson counts, Normal with variance $\tau_n^2+\sigma^2$ for Normal-Normal. In practice it is simulated: draw $\theta$ from the posterior, then draw data from the likelihood. It also powers **posterior predictive checks**: simulate replicated datasets and compare with the real one to test model fit.

### Example
Posterior Beta(52,1048) for conversion. Next 200 sessions: predictive is Beta-Binomial with mean $200\times4.727\%=9.45$ conversions and sd 3.26, with a central 90% interval of **4 to 15 conversions**. A plug-in Binomial(200, 4.8%) has sd 3.02, so it understates the spread by about 7%. Planning a daily forecast and safety stock needs the wider band (compare [[004 Demand Forecasting & Planning]]).

### In the news
See news box. Predictive simulation is also how FDA-style Bayesian designs compute operating characteristics: simulate many future trials under assumed truths and count how often the success criterion is met.

### Interview angle
> [!question] How it is asked
> "Difference between the posterior and the posterior predictive? Why does it matter for forecasting?"

> [!tip] Strong answer includes
> - Posterior is about the parameter; predictive is about future data
> - Predictive variance = parameter uncertainty + sampling noise
> - Plug-in estimates give overconfident forecasts
> - Mention simulation-based predictive checks for model validation

---
## 8. Bayesian A/B Testing: Probability to Beat Control and Expected Loss
> 🟠 Tier 2 · _Key points:_ P(B>A), expected loss, credible interval of lift; decide on risk, not on p<0.05

### Definition
Model each arm's conversion with a Beta posterior and compare the posteriors by simulation. Three decision metrics:
- **Probability to beat control:** $P(p_B>p_A\mid\text{data})$.
- **Expected loss** of choosing B: $E[\max(p_A-p_B,\,0)]$, the average conversion points you would give up if B is actually worse. Choose when expected loss is below a **threshold of caring** (for example, 0.05 pp).
- **Credible interval of lift** $(p_B-p_A)/p_A$, optionally with a ROPE.

Expected loss weighs both how likely a mistake is and how costly it would be, which a bare P(B>A) misses. Compared with frequentist testing (see [[089 Hypothesis Testing]] and the A/B section of [[092 Sampling & Experimental Design]]), there is no fixed sample size, but peeking still inflates false decisions unless rules are pre-set (sub-topic 14). For funnel metrics see [[031 Product Metrics & Analytics]].

### Example
Control A: 200/5,000 (4.0%). Variant B: 240/5,000 (4.8%). This is the same data whose z-test gives two-sided p = 0.051 in the hypothesis-testing note. With flat Beta(1,1) priors, posteriors are Beta(201,4801) and Beta(241,4761).
- $P(p_B>p_A)=\mathbf{97.4\%}$ (matches the one-sided p of about 0.026).
- Mean difference 0.80 pp; 95% credible interval $[-0.005,\;1.60]$ pp.
- Expected loss if you ship B: **0.004 pp**; if you keep A: **0.80 pp**.
- $P(\text{lift}>0.5\text{ pp})=76.7\%$; mean relative lift +20%, credible interval about $[-0.1\%,\,+44\%]$.
- Money: at 10 lakh sessions a month, ₹1,200 order value and 15% contribution margin, shipping B has expected gain $10^6\times0.008\times1200\times0.15=$ **₹14.4 lakh a month**, and expected loss from being wrong of about ₹7,000 a month. Ship B and keep monitoring.

```python
import numpy as np
rng = np.random.default_rng(42)
a = rng.beta(1+200, 1+4800, 2_000_000)
b = rng.beta(1+240, 1+4760, 2_000_000)
print((b > a).mean())                # 0.974
print(np.maximum(a - b, 0).mean())   # 4.0e-05 expected loss of shipping B
```

### In the news
See news box. Google Meridian reports incremental effects as posterior distributions with credible intervals, so budget decisions can be framed as probability of a minimum return, the same grammar as "probability to beat control".

### Interview angle
> [!question] How it is asked
> "Test shows p = 0.051. Your PM asks whether to ship. What do you say?"

> [!tip] Strong answer includes
> - Frame as decision under uncertainty: P(B>A), expected loss, rupee impact
> - 5% is a convention; the cost of a wrong launch and of delay matters
> - Compute from Beta posteriors by simulation
> - Warn that Bayesian stopping rules still need pre-registration against peeking

---
## 9. Thompson Sampling and Multi-Armed Bandits
> 🟠 Tier 2 · _Key points:_ Sample each arm's posterior, play the best draw; explore-exploit by probability matching

### Definition
A **multi-armed bandit** allocates traffic among options while learning, trading **exploration** (learning which is best) against **exploitation** (using the current best). **Thompson sampling** does this with Bayesian posteriors: each round, draw one sample $\tilde p_k$ from every arm's posterior, play the arm with the largest draw, observe the result, update that arm's posterior. Each arm is played with probability equal to the posterior probability that it is best (probability matching), so uncertain arms still get tried, and clearly inferior arms are starved. For binary rewards each arm is a Beta-Binomial model (sub-topic 3). It has strong regret guarantees, is simple to implement and handles delayed updates well. Contrast: A/B test = fixed split, then decide; bandit = adaptive allocation, lower regret, but weaker clean inference and trouble with non-stationarity (time effects need discounting).

### Example
Three banner variants with true rates 4%, 5%, 6% (unknown to the algorithm), 20,000 impressions, 20 simulated runs per policy.
- Equal split: about 6,667 impressions each, average regret (conversions lost against always showing the 6% banner) **200**.
- Thompson sampling with Beta(1,1) priors: about 665 / 2,227 / 17,108 impressions, average regret **36**, an 82% reduction.
- Trade-off: the bandit gives a less clean estimate of the losing arms, so use it for continuous optimisation (recommendations, banners, push-notification copy) rather than one-off launch decisions that need an unbiased effect size.

```python
import numpy as np
true = [0.04, 0.05, 0.06]; a = np.ones(3); b = np.ones(3); rng = np.random.default_rng(0)
for t in range(20000):
    k = int(np.argmax(rng.beta(a, b)))      # sample each posterior, play the best draw
    y = rng.random() < true[k]
    a[k] += y; b[k] += 1 - y                # Bayesian update of the chosen arm
```

### In the news
See news box. Meridian's use of experiments as priors and the FDA's interest in adaptive designs are two ends of the same idea: let accumulating evidence change what you do next.

### Interview angle
> [!question] How it is asked
> "When would you use a multi-armed bandit instead of an A/B test, and how does Thompson sampling work?"

> [!tip] Strong answer includes
> - Explore-exploit and regret; sample posteriors, play the best draw, update
> - Use when opportunity cost is high or content is short-lived
> - Downsides: biased/weaker inference on losing arms, non-stationarity, harder to read secondary metrics
> - Mention contextual bandits and link to [[100 ML for Product Management]]

---
## 10. Hierarchical Models and Shrinkage
> 🟠 Tier 2 · _Key points:_ Partial pooling; small groups shrink toward the overall mean; borrow strength

### Definition
Suppose you estimate a rate for many groups (stores, pin codes, drivers, SKUs). **No pooling** estimates each group alone: noisy for small groups. **Complete pooling** uses one overall rate: ignores real differences. A **hierarchical (multilevel) model** is the compromise: group rates $p_j$ are drawn from a common distribution, $p_j\sim\text{Beta}(a,b)$ or $\theta_j\sim N(\mu,\tau^2)$, whose hyperparameters are themselves learned from data. The result is **partial pooling** or **shrinkage**: each group's estimate is a weighted average of its own rate and the overall mean, with the weight on its own data rising with its sample size. This is the Bayesian form of random effects, and of "empirical Bayes" when hyperparameters are fitted and then fixed.

### Example
Six stores, conversions/sessions: 5/100, 30/1,000, 2/40, 60/1,200, 8/300, 18/500. Using a common prior Beta(4,96) (mean 4%, weight 100) the posterior mean is $(x+4)/(n+100)$:

| Store | Raw rate | Own-data weight $n/(n+100)$ | Shrunk estimate |
|---|---|---|---|
| 1 (n=100) | 5.00% | 0.50 | 4.50% |
| 2 (n=1,000) | 3.00% | 0.91 | 3.09% |
| 3 (n=40) | 5.00% | 0.29 | 4.29% |
| 4 (n=1,200) | 5.00% | 0.92 | 4.92% |
| 5 (n=300) | 2.67% | 0.75 | 3.00% |
| 6 (n=500) | 3.60% | 0.83 | 3.67% |

Stores 1 and 3 both show 5%, but store 3 (40 sessions) is pulled much harder toward 4%; store 4 with 1,200 sessions barely moves. A full hierarchical fit would estimate the prior weight from the six stores instead of fixing 100. This is why a "top-performing store" list sorted by raw rate is dominated by tiny stores (the small-sample trap), and is the idea behind ranking restaurants or sellers by shrunk ratings.

### In the news
See news box. Partial pooling is how sparse segments (small regions, new SKUs) borrow strength from dense ones in Bayesian marketing and demand models.

### Interview angle
> [!question] How it is asked
> "You have conversion rates for 500 pin codes, many with few orders. How do you rank them fairly?"

> [!tip] Strong answer includes
> - Raw rates are noisy for small $n$; rank by shrunk (posterior) estimates or lower credible bound
> - Describe partial pooling and hyperparameters learned from data
> - Mention empirical Bayes as the simple version, random effects as the frequentist cousin
> - Call out the winner's curse in raw top-N lists

---
## 11. MCMC Overview and PyMC
> 🟠 Tier 2 · _Key points:_ Sample from posterior when no closed form; check R-hat, ESS, divergences, trace plots

### Definition
Outside conjugate pairs the posterior has no closed form because $p(\text{data})$ is an intractable integral. **Markov chain Monte Carlo (MCMC)** builds a chain whose long-run distribution is the posterior, so draws from the chain approximate it. Basic **Metropolis**: propose $\theta'$ near $\theta$, accept with probability $\min\!\big(1,\frac{p(\theta'\mid\text{data})}{p(\theta\mid\text{data})}\big)$ (the unknown constant cancels). Modern tools such as **PyMC** and **Stan** use **Hamiltonian Monte Carlo/NUTS**, which uses gradients to move efficiently. Alternatives: variational inference (fast, approximate) and Laplace approximation.

Workflow: specify priors and likelihood, sample several chains, **diagnose**, then summarise.
- **R-hat** near 1.00 (below about 1.01) means chains agree; **effective sample size (ESS)** in the hundreds or more per parameter; no divergences; trace plots look like "fuzzy caterpillars".
- Discard **warm-up/burn-in** draws; compare priors with **prior predictive checks** and fit with **posterior predictive checks**.

### Example
Posterior for the conversion model of sub-topic 3, Beta(52,1048). A hand-written Metropolis sampler (20,000 steps, proposal sd 0.01, first 2,000 discarded, acceptance rate 58%) gave mean **4.72%** and 95% interval **[3.55%, 6.06%]**, matching the exact result 4.73% and [3.55%, 6.06%]. The same A/B model of sub-topic 8 in PyMC (executed with 4 chains, 2,000 draws) reports $P(B>A)=0.974$, R-hat 1.0 and ESS about 8,000:

```python
import pymc as pm, numpy as np
with pm.Model():
    p_a = pm.Beta("p_a", 1, 1); p_b = pm.Beta("p_b", 1, 1)
    pm.Binomial("obs_a", n=5000, p=p_a, observed=200)
    pm.Binomial("obs_b", n=5000, p=p_b, observed=240)
    diff = pm.Deterministic("diff", p_b - p_a)
    idata = pm.sample(2000, tune=1000, chains=4, random_seed=7)
d = idata.posterior["diff"].values.ravel()
print((d > 0).mean())      # about 0.974
```

For a conjugate model like this one MCMC is unnecessary; use PyMC when you add covariates, hierarchies or non-standard likelihoods (see [[067 Statistical Analysis in Python]] for the classical Python toolkit).

### In the news
See news box. As reported, the FDA guidance expects sponsors to document simulation code and computational methods, so Bayesian analyses must be reproducible, whatever sampler is used.

### Interview angle
> [!question] How it is asked
> "What is MCMC and how do you know the sampler worked?"

> [!tip] Strong answer includes
> - Reason: posterior intractable; chain converges to it; Metropolis acceptance idea
> - Diagnostics: R-hat, ESS, divergences, trace plots, multiple chains
> - Prior and posterior predictive checks
> - Know when closed-form conjugate updates are enough

---
## 12. Bayesian vs Frequentist: The Interview Comparison
> 🟠 Tier 2 · _Key points:_ Probability of hypotheses vs long-run error rates; both valid; choose by question

### Definition
| Aspect | Frequentist | Bayesian |
|---|---|---|
| Parameter | Fixed unknown constant | Random variable with distribution |
| Probability means | Long-run frequency | Degree of belief |
| Main output | Estimate, CI, p-value | Posterior, credible interval, P(hypothesis) |
| Prior information | Not formally used | Explicit prior |
| Error control | Type I and II error by design | Via simulation of operating characteristics |
| Stopping rules | Fixed sample or alpha-spending | Posterior-based, but peeking still needs rules |
| Small data | Weak, relies on asymptotics | Prior helps, but prior matters |
| Computation | Closed forms | MCMC for complex models |
| Direct answer to "is B better?" | p-value (indirect) | P(B>A) (direct) |

Neither is "right". Frequentist tests give guaranteed long-run error rates, which is vital for regulators, repeated programme-level decisions and audits. Bayesian methods give directly interpretable probabilities, incorporate prior evidence, and handle sequential decisions and hierarchical data naturally. In practice many teams calibrate Bayesian decision rules so that frequentist error rates are acceptable, which is exactly the option the FDA draft guidance gives sponsors.

### Example
Same A/B data: frequentist says z = 1.95, p = 0.051 ("fail to reject at 5%"). Bayesian says P(B>A) = 97.4% and expected loss of shipping B is 0.004 pp. Neither is wrong; they answer different questions. The decision depends on the cost of a wrong launch, reversibility (a button colour vs a pricing change), and prior evidence from similar tests.

### In the news
See news box. The FDA's willingness to accept Bayesian primary analysis, provided error-rate behaviour is understood, is a practical sign that the two schools are being combined, not set against each other.

### Interview angle
> [!question] How it is asked
> "Are you a Bayesian or a frequentist? When would you use each?"

> [!tip] Strong answer includes
> - Pragmatic: pick by question, constraints and audience
> - Bayesian for small data, sequential decisions, prior evidence, hierarchies, probabilities for managers
> - Frequentist for regulatory settings, simple large-sample tests, no credible prior
> - Mention the common ground: both agree with lots of data; both can be gamed (peeking, p-hacking, cherry-picked priors)

---
## 13. ⭐ Advanced: Expected-Loss Launch Decisions in Rupees
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Bayesian decision theory turns posteriors into actions by attaching a **loss** (or utility) to each action and state, then choosing the action with the lowest posterior expected loss (see [[150 Decision Analysis & Simulation]]). For a launch decision, define the value per period $V(\delta)=N\cdot\delta\cdot m$, where $\delta=p_B-p_A$ is the conversion difference, $N$ the volume and $m$ the contribution per conversion. Then:

$$\text{EV(ship B)}=E[V(\delta)],\qquad \text{Expected loss(ship B)}=E[\max(-V(\delta),0)]$$

Add one-time launch cost $C$ and ship if $E[V]\times\text{horizon}>C$ and the expected loss is tolerable. Also compute the **expected value of perfect information (EVPI)** $=E[\max(V,0)]-\max(E[V],0)$, which caps what extra testing is worth: if EVPI is smaller than the cost of running the test longer, stop and decide.

### Example
Using the sub-topic 8 posteriors with 10 lakh sessions a month and ₹180 contribution per order (₹1,200 × 15%): $E[V]=\text{₹}14.4$ lakh a month; expected loss of shipping B is about ₹7,200 a month (0.004 pp × 10 lakh × ₹180). If B costs ₹30 lakh in engineering and the payback horizon is 12 months, EV over 12 months is ₹172.8 lakh, so ship. For a tiny change worth ₹2 lakh a month with ₹30 lakh cost, the same posterior would not justify shipping despite 97% probability of being better: probability is not value. This "P(better) vs ₹ value" distinction is what separates a PM answer from a statistician's.

### In the news
See news box. Meridian outputs are built for exactly this: posterior return-on-ad-spend distributions that feed budget optimisation under risk.

### Interview angle
> [!question] How it is asked
> "The test says 94% probability B is better but lift is small. How do you decide?"

> [!tip] Strong answer includes
> - Translate to expected value and expected loss in rupees, include launch and maintenance cost
> - Reversibility and risk appetite set the threshold
> - EVPI: is more data worth its cost?
> - Segment and guardrail checks before the final call

---
## 14. ⭐ Advanced: Prior Sensitivity, Peeking and Bayesian Stopping Rules
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Two traps survive in Bayesian testing. **(1) Prior influence:** a prior of weight $w$ pseudo-observations matters if $w$ is not small relative to $n$; always rerun with sceptical, neutral and optimistic priors and report the range. **(2) Optional stopping:** it is often claimed that Bayesian answers are unaffected by stopping rules (the likelihood principle), true for the posterior as a mathematical object, but the long-run **false-decision rate** of "stop when P(B>A) crosses 95%" still rises with the number of looks. Controls: pre-register minimum sample and maximum duration, use a stricter threshold plus expected-loss cut-off, and **simulate the operating characteristics** of the whole decision rule under no-effect and real-effect scenarios, which is what the FDA guidance asks of sponsors.

### Example
Prior sensitivity, A/B data of sub-topic 8 (A 200/5,000, B 240/5,000):

| Prior on each arm | P(B>A) | Mean difference |
|---|---|---|
| Flat Beta(1,1) | 97.4% | 0.80 pp |
| Beta(4,96), weight 100 | 97.3% | 0.78 pp |
| Beta(40,960), weight 1,000 | 96.4% | 0.67 pp |
| Beta(400,9600), weight 10,000 | 87.7% | 0.27 pp |

Only an extremely strong prior (twice the data volume per arm) changes the story. Peeking: simulate A/A tests (true rate 4% in both arms, up to 10,000 per arm), declare a winner if $P(B>A)>95\%$ or $<5\%$. Checking at one final look gives a false-decision rate of **8.6%**; checking after every 1,000 visitors (10 looks) gives **33.6%**. The Bayesian posterior at every look is "correct", but the decision procedure is not safe, so calibrate thresholds by simulation or use a pre-set minimum runtime. See also [[214 Causal Inference & Experimentation Beyond A-B Tests]] for design issues that no prior can fix.

### In the news
See news box. The FDA draft guidance's insistence on simulated operating characteristics and sensitivity analyses addresses exactly these two traps.

### Interview angle
> [!question] How it is asked
> "Does a Bayesian approach let me stop an experiment whenever I like?"

> [!tip] Strong answer includes
> - Posterior stays valid, but decision rules have error rates that grow with looks
> - Pre-register thresholds, minimum sample and duration; simulate the rule
> - Prior sensitivity analysis with sceptical and optimistic priors
> - Also mention novelty effects and weekly cycles as reasons to run full weeks
