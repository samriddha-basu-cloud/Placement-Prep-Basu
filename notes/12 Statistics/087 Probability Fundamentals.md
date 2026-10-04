---
tags: [statistics, tier1]
area: Statistics
topic: "Probability Fundamentals"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Probability Fundamentals

⬅ [[086 Descriptive Statistics]] · [[_Index - Statistics|Statistics]] · [[088 Probability Distributions]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Probability Rules]]
2. [[#2. Conditional Probability]]
3. [[#3. Bayes' Theorem]]
4. [[#4. Independent Events]]
5. [[#5. Mutually Exclusive Events]]
6. [[#6. Permutations & Combinations]]
7. [[#7. Expected Value]]
8. [[#8. Variance of Random Variable]]
9. [[#9. Law of Large Numbers]]
10. [[#10. Central Limit Theorem (CLT)]]
11. [[#11. ⭐ Advanced: Monte Carlo Simulation]]
12. [[#12. ⭐ Advanced: Bayesian Updating with Beta-Binomial (Defect Rate Learning)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): FDA formally embraces Bayesian methods
> **FDA draft guidance on Bayesian methods in clinical trials (9 Jan 2026).** The FDA issued draft guidance clarifying how Bayesian approaches can be used for regulatory decisions; the guidance says Bayesian methodology "combines prior knowledge with new data as it becomes available", in a continuous learning process that lets trial designs adapt as evidence accumulates. It covers INDs, NDAs and BLAs and addresses Bayesian methods for primary inference in Phase III settings. Prior x likelihood, updated with data, is Bayes' theorem applied at regulatory scale. ([Alston and Bird summary](https://www.alston.com/en/insights/publications/2026/01/fda-bayesian-guidance-drug-trials))
>
> **India's new CPI series (12 Feb 2026).** Based on a 2023-24 household survey; shows how sample data and probability-based weights are turned into a national inflation number (Jan 2026 reading 2.75% on the new base). ([Upstox explainer](https://upstox.com/learning-center/personal-finance/what-changed-in-indias-new-cpi-series-and-how-it-impacts-the-economy-and-inflation/article-1518/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Probability Rules
> 🔴 Tier 1 · _Tracker hint:_ P(A) ∈ [0,1]; P(S)=1; P(A∪B)=P(A)+P(B)-P(A∩B); P(Ac)=1-P(A)

### Definition
Kolmogorov's axioms: (1) $0\le P(A)\le1$; (2) $P(S)=1$ for the sample space $S$; (3) for mutually exclusive events probabilities add. Derived rules:
- **Complement:** $P(A^c)=1-P(A)$. Very useful for "at least one" questions.
- **Addition (union):** $P(A\cup B)=P(A)+P(B)-P(A\cap B)$ (subtract the overlap, else it is double counted).
- **Multiplication:** $P(A\cap B)=P(A)\,P(B\mid A)$.

Classical probability = favourable/total outcomes (equally likely); empirical = relative frequency; subjective = degree of belief.

### Example
30% of orders are delayed by supplier delay (A), 40% by transport delay (B), 10% by both. $P(A\cup B)=0.30+0.40-0.10=\mathbf{0.60}$; so $P(\text{neither})=1-0.60=\mathbf{0.40}$.

### In the news
See news box. Regulatory frameworks build on these basic rules of combining probabilities of events.

### Interview angle
> [!question] How it is asked
> "40% of customers buy A, 30% buy B, 10% buy both. What fraction buy neither?"

> [!tip] Strong answer includes
> - Use the addition rule with the overlap subtracted
> - Then complement: 1 − 0.60 = 0.40
> - Draw a Venn diagram to avoid double counting
> - State the answer in words

---

## 2. Conditional Probability
> 🔴 Tier 1 · _Tracker hint:_ P(A|B) = P(A∩B)/P(B); intuition: probability of A given B already occurred

### Definition
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0$$
Restrict the sample space to $B$ and ask what share of it also lies in $A$. $P(A\mid B)\ne P(B\mid A)$ in general (the "prosecutor's fallacy"). Rearranged: multiplication rule $P(A\cap B)=P(B)P(A\mid B)$. **Law of total probability:** $P(A)=\sum P(A\mid B_i)P(B_i)$ for a partition $\{B_i\}$. A contingency table (row/column percentages) is the easiest way to see it.

### Example
1,000 orders; 200 from Supplier X; 30 of X's orders were defective; 80 orders in all were defective. $P(\text{defective}\mid X)=30/200=\mathbf{0.15}$, while $P(X\mid\text{defective})=30/80=\mathbf{0.375}$. Different questions, different answers.

### In the news
See news box. A clinical trial interim result is a conditional statement: probability of benefit given the data so far.

### Interview angle
> [!question] How it is asked
> "Of customers who open the email, 20% buy. Does that mean 20% of buyers opened the email?"

> [!tip] Strong answer includes
> - No: P(A|B) ≠ P(B|A)
> - Define the conditioning event clearly
> - Use a table or tree with counts
> - Business meaning: targeting changes the denominator

---

## 3. Bayes' Theorem
> 🔴 Tier 1 · _Tracker hint:_ P(A|B) = P(B|A)×P(A) / P(B); prior × likelihood / evidence; Bayesian updating

### Definition
$$P(A\mid B)=\frac{P(B\mid A)\,P(A)}{P(B)}=\frac{P(B\mid A)P(A)}{\sum_i P(B\mid A_i)P(A_i)}$$
**Posterior = prior × likelihood / evidence.** It revises belief when evidence arrives. The most common mistake is ignoring the **base rate** (the prior): a rare condition with a decent test still gives many false positives. Updating can be repeated: today's posterior is tomorrow's prior.

### Example
Machine A makes 60% of items with 2% defects; Machine B makes 40% with 5% defects. $P(D)=0.6(0.02)+0.4(0.05)=0.012+0.020=0.032$. A found item is defective: $P(A\mid D)=0.012/0.032=\mathbf{0.375}$, $P(B\mid D)=\mathbf{0.625}$. Even though B makes fewer items, a defect points more to B.

### In the news
See news box. The FDA's Bayesian draft guidance (Jan 2026) is exactly prior knowledge plus new trial data combined by Bayes' rule.

### Interview angle
> [!question] How it is asked
> "A fraud test catches 90% of frauds, wrongly flags 5% of genuine transactions, and 1% of transactions are fraud. If a transaction is flagged, what is the chance it is fraud?"

> [!tip] Strong answer includes
> - Set up tree: P(F)=0.01, P(flag|F)=0.9, P(flag|not F)=0.05
> - P(flag)=0.009+0.0495=0.0585; posterior = 0.009/0.0585 = **15.4%**
> - Explain base-rate effect in plain words
> - Business implication: precision matters, so review flagged cases

---

## 4. Independent Events
> 🔴 Tier 1 · _Tracker hint:_ P(A∩B) = P(A)×P(B); knowing B gives no info about A

### Definition
$A$ and $B$ are **independent** if $P(A\cap B)=P(A)P(B)$, equivalently $P(A\mid B)=P(A)$. For several independent events, probabilities multiply; "at least one" = $1-\prod(1-p_i)$. Independence is an *assumption* to be justified (shared causes such as a common power supply break it). Independence is not the same as being mutually exclusive.

Reliability: a **series** system works only if all parts work ($R=\prod R_i$); a **parallel** system works if at least one does ($R=1-\prod(1-R_i)$).

### Example
Two machines fail on a given day independently with probabilities 0.05 and 0.10. Both fail: 0.05×0.10 = **0.005**. At least one fails: $1-0.95\times0.90=1-0.855=\mathbf{0.145}$. A line needing both machines has reliability 0.855; with a parallel backup it is 0.995.

### In the news
See news box. Supply chain risk models assume independence of supplier failures; the 2024–25 disruptions show common-cause correlations (same region, same sub-supplier) which violate it.

### Interview angle
> [!question] How it is asked
> "Each of 3 suppliers delivers on time with probability 0.9. What is the probability all three are on time? At least one?"

> [!tip] Strong answer includes
> - Assume independence and state it as an assumption
> - All three: 0.729; at least one: 1 − 0.001 = 0.999
> - Caveat: common causes break independence
> - Link to dual sourcing and redundancy

---

## 5. Mutually Exclusive Events
> 🔴 Tier 1 · _Tracker hint:_ P(A∩B)=0; cannot both occur; P(A∪B) = P(A)+P(B)

### Definition
Events are **mutually exclusive (disjoint)** if they cannot occur together: $P(A\cap B)=0$, so $P(A\cup B)=P(A)+P(B)$. **Collectively exhaustive** events cover the whole sample space; a partition is both. Key distinction:

| | Mutually exclusive | Independent |
|---|---|---|
| Definition | $P(A\cap B)=0$ | $P(A\cap B)=P(A)P(B)$ |
| Knowing B | tells you A did **not** happen | tells you nothing |
| Both possible if P>0? | exclusive events with positive probability are **dependent** | yes |

### Example
A single order is either "on time", "late by 1–2 days" or "late by 3+ days" (mutually exclusive, exhaustive): probabilities 0.80, 0.15, 0.05 sum to 1. Probability of "late" = 0.15+0.05 = 0.20. By contrast "order from Supplier X" and "order is late" are not exclusive.

### In the news
See news box. Trial outcomes classified as "success", "failure" or "inconclusive" form such a partition.

### Interview angle
> [!question] How it is asked
> "Are mutually exclusive events independent?"

> [!tip] Strong answer includes
> - No: if one occurs the other cannot, so they are dependent (when probabilities > 0)
> - Contrast formulas: P(A∩B) = 0 vs = P(A)P(B)
> - Example with 0.3 and 0.4: union 0.7 if exclusive; intersection 0.12 if independent
> - Mention partitions for total probability

---

## 6. Permutations & Combinations
> 🔴 Tier 1 · _Tracker hint:_ nPr = n!/(n-r)!; nCr = n!/[r!(n-r)!]; when order matters vs doesn't

### Definition
- **Factorial:** $n!=n(n-1)\cdots1$; $0!=1$.
- **Permutations** (order matters): $_nP_r=\frac{n!}{(n-r)!}$.
- **Combinations** (order does not matter): $_nC_r=\frac{n!}{r!(n-r)!}=\binom{n}{r}$.
- **Arrangements with repeats:** $\frac{n!}{n_1!n_2!\cdots}$; **circular arrangements:** $(n-1)!$.
- Test: "Does swapping two chosen items give a different outcome?" yes means permutation.

Counting is the basis of classical probability (favourable/total) and of binomial coefficients.

### Example
Rank the top 3 of 5 vendors: $_5P_3=5!/2!=\mathbf{60}$. Pick a 3-member review panel from 5 managers: $_5C_3=\mathbf{10}$ (60/3! = 10). Chance that a random panel includes a specific manager: $\binom{4}{2}/\binom{5}{3}=6/10=\mathbf{0.6}$.

### In the news
See news box. Not tied to a specific recent event; counting underlies sampling plans, such as choosing survey households.

### Interview angle
> [!question] How it is asked
> "In how many ways can a team of 4 be chosen from 9 people, and in how many ways can they be assigned 4 distinct roles?"

> [!tip] Strong answer includes
> - Team: $_9C_4=126$; roles: $_9P_4=3024$
> - The reasoning on order
> - Check with factorial cancellation
> - Link: 3,024 = 126 × 4!

---

## 7. Expected Value
> 🔴 Tier 1 · _Tracker hint:_ E(X) = Σ[x × P(x)]; weighted average of outcomes by probability

### Definition
$$E(X)=\sum x\,P(x)\quad(\text{discrete}),\qquad E(X)=\int x f(x)\,dx\quad(\text{continuous})$$
It is the long-run average, not necessarily a possible outcome. **Linearity:** $E(aX+b)=aE(X)+b$; $E(X+Y)=E(X)+E(Y)$ always (independent or not). Decision rule: choose the option with the highest expected profit (risk-neutral), then adjust for risk. Expected monetary value (EMV) trees extend it to sequential decisions.

### Example
Daily demand: 10 units (p=0.2), 20 (0.5), 30 (0.3). $E(X)=10(0.2)+20(0.5)+30(0.3)=2+10+9=\mathbf{21}$ units. Unit margin ₹50, stocking 20 units: profit if demand ≥ 20 is 20×50 = ₹1,000; if demand 10, sell 10 and lose cost on 10 leftover (cost ₹30 each): 500 − 300 = ₹200. Expected = 0.2×200 + 0.8×1,000 = 40 + 800 = **₹840**.

### In the news
See news box. Regulatory decisions weigh the expected benefit and risk of treatments, an EMV logic.

### Interview angle
> [!question] How it is asked
> "A project has a 60% chance of earning ₹10 crore and a 40% chance of losing ₹4 crore. Do you take it?"

> [!tip] Strong answer includes
> - E = 0.6×10 − 0.4×4 = ₹4.4 crore
> - Note variance and downside tolerance
> - Consider staging, hedging or pilot
> - State assumptions on probabilities

---

## 8. Variance of Random Variable
> 🔴 Tier 1 · _Tracker hint:_ Var(X) = E[(X-μ)²] = E(X²) - [E(X)]²

### Definition
$$\text{Var}(X)=E[(X-\mu)^2]=E(X^2)-[E(X)]^2,\qquad \sigma=\sqrt{\text{Var}(X)}$$
Properties: $\text{Var}(aX+b)=a^2\text{Var}(X)$; for **independent** $X,Y$: $\text{Var}(X+Y)=\text{Var}(X)+\text{Var}(Y)$ (in general add $2\,\text{Cov}(X,Y)$). Variance of a sum of $n$ independent identical items is $n\sigma^2$, so sd grows with $\sqrt{n}$: the root of risk pooling. Standard error of a mean: $\sigma/\sqrt{n}$.

### Example
Same demand distribution as before (mean 21). $E(X^2)=100(0.2)+400(0.5)+900(0.3)=20+200+270=490$. $\text{Var}=490-21^2=490-441=\mathbf{49}$, $\sigma=\mathbf{7}$. Pooling 4 independent identical regions: total variance 4×49 = 196, sd = 14 (not 28); per-region sd falls from 7 to 3.5.

### In the news
See news box. Interim looks in Bayesian trials explicitly quantify the uncertainty (variance) of effect estimates.

### Interview angle
> [!question] How it is asked
> "Why does centralising inventory reduce safety stock?"

> [!tip] Strong answer includes
> - Variances add for independent demands, sd grows with √n
> - Numeric example (4 regions → sd ×2 not ×4)
> - Condition: demands not perfectly correlated
> - Trade-off: longer delivery distance

---

## 9. Law of Large Numbers
> 🔴 Tier 1 · _Tracker hint:_ Sample mean → population mean as n→∞; basis for statistical inference

### Definition
As the sample size $n$ grows, the sample mean $\bar{X}_n$ converges to the population mean $\mu$ (weak law: in probability; strong law: almost surely). It justifies using sample averages as estimates and insurance/casino economics. It does **not** say short-run deviations will be "corrected" (gambler's fallacy): the *proportion* converges, while the absolute difference can keep growing. Convergence speed is governed by the standard error $\sigma/\sqrt{n}$.

### Example
A fair die has mean 3.5. After 10 rolls the average might be 4.1 or 2.9; after 10,000 rolls it will be within about $3\times1.708/\sqrt{10000}\approx0.05$ of 3.5 (σ of a die = 1.708). A manager with 20 deliveries should not trust an on-time rate of 95% as precisely as one from 2,000 deliveries.

### In the news
See news box. Large surveys (household expenditure surveys behind CPI weights) rely on this law: more households, a more reliable average.

### Interview angle
> [!question] How it is asked
> "A coin landed heads 5 times in a row. Is tails 'due'?"

> [!tip] Strong answer includes
> - No: independent trials, LLN is about long-run proportions
> - Difference between expected value and short-run luck
> - Sample size and standard error
> - Business application: do not over-react to small samples

---

## 10. Central Limit Theorem (CLT)
> 🔴 Tier 1 · _Tracker hint:_ Sample means are normally distributed regardless of population distribution (n≥30)

### Definition
For independent samples of size $n$ from **any** population with mean $\mu$ and finite variance $\sigma^2$, the distribution of $\bar{X}$ approaches
$$\bar{X}\sim N\!\left(\mu,\ \frac{\sigma^2}{n}\right)$$
as $n$ increases. Standard error $=\sigma/\sqrt{n}$. The rule $n\ge30$ is a guideline: heavily skewed populations may need more, and near-normal ones need fewer. CLT underpins confidence intervals and most hypothesis tests ([[089 Hypothesis Testing]]). It applies to sums and means, not to single observations.

### Example
Order size is skewed with $\mu=50$ and $\sigma=30$. For samples of $n=36$: SE = 30/6 = **5**. $P(\bar{X}>58)$: $z=(58-50)/5=1.6$, so probability = 1 − 0.9452 = **0.0548**, about 5.5%. Doubling the sample to 144 cuts SE to 2.5, so $z=3.2$ and the probability is ~0.07%.

### In the news
See news box. The CLT is why survey-based statistics (CPI) can attach margins of error to national averages.

### Interview angle
> [!question] How it is asked
> "Why can we use normal-based tests on skewed data?"

> [!tip] Strong answer includes
> - CLT: the sampling distribution of the mean is normal for adequate n
> - SE = σ/√n and its role in intervals/tests
> - n ≥ 30 as a rule of thumb, with caveats on skew/outliers
> - Distinguish data distribution from sampling distribution

---

## 11. ⭐ Advanced: Monte Carlo Simulation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
When closed-form probability is intractable (many uncertain inputs), **simulate**: draw random inputs from assumed distributions, compute the outcome, repeat thousands of times, and read the distribution of results. By the LLN the average of simulated results converges to the expectation; the error shrinks like $1/\sqrt{N}$. Uses: project schedule risk (PERT with random durations), inventory policy testing, financial risk (VaR), capacity planning.

Steps: model → distributions (from data) → correlations → run N≥10,000 → analyse percentiles (P50, P90) → sensitivity.

```python
import numpy as np
rng = np.random.default_rng(1)
demand = rng.normal(100, 20, 100000).clip(0)     # daily demand
lead = rng.integers(3, 8, 100000)                # lead time 3-7 days
lt_demand = demand * lead                        # simplified
print(np.percentile(lt_demand, 95))
```

### Example
Project with two sequential tasks: A uniform 4–6 weeks (mean 5), B uniform 3–7 weeks (mean 5). Mean total = 10 weeks; simulation gives the chance of finishing within 11 weeks (about 0.8) and P90 duration (about 11.7 weeks, using a normal approximation with sd 1.29) for a buffer, which a deterministic plan of "10 weeks" hides.

### In the news
See news box. Bayesian and simulation-based designs allow trials to be tested under many scenarios before they run.

### Interview angle
> [!question] How it is asked
> "How would you estimate the probability that a project finishes on time when task durations are uncertain?"

> [!tip] Strong answer includes
> - Model task durations as distributions, simulate many runs
> - Report percentile (P80/P90) rather than only the mean
> - Mention correlation and critical-path switching
> - Validate against past projects

---

## 12. ⭐ Advanced: Bayesian Updating with Beta-Binomial (Defect Rate Learning)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
To learn an unknown rate $p$ (defect or conversion), use a **Beta prior** $\text{Beta}(\alpha,\beta)$. After observing $k$ successes in $n$ trials, the posterior is $\text{Beta}(\alpha+k,\ \beta+n-k)$ with mean
$$E[p\mid\text{data}]=\frac{\alpha+k}{\alpha+\beta+n}.$$
The prior acts like $\alpha+\beta$ pseudo-observations; as $n$ grows, data dominates. This avoids over-reading small samples (e.g. 1 defect in 5 items is not "20%").

### Example
Prior belief about a new supplier's defect rate: Beta(2, 98), mean 2%. Inspect 200 units, 8 defective. Posterior Beta(10, 290): mean = 10/300 = **3.33%**. The sample alone says 4%; the prior pulls it toward 2%. With 2,000 units and 80 defects, posterior mean 82/2100 = 3.9%, closer to the data.

### In the news
See news box. The FDA guidance legitimises exactly this style of using prior information alongside new data.

### Interview angle
> [!question] How it is asked
> "How would you estimate the conversion rate of a new feature after only 50 visitors?"

> [!tip] Strong answer includes
> - Small sample is noisy; use a prior from similar features
> - Posterior updates as data arrives; report interval, not a point
> - Mention Beta-Binomial or a simple shrinkage
> - Decision rule: act when posterior probability of beating control exceeds a threshold

---

---
## 🔗 Go deeper: expansion notes
- [[217 Probability Puzzles & Applied Problem Solving|Probability Puzzles & Applied Problem Solving]]
- [[210 Bayesian Statistics for Decisions|Bayesian Statistics for Decisions]]
