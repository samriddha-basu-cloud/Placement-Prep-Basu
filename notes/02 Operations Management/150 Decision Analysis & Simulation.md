---
tags: [operations-management, tier2]
area: Operations Management
topic: "Decision Analysis & Simulation"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Decision Analysis & Simulation

⬅ [[149 Queueing Theory & Waiting-Line Analysis]] · [[_Index - Operations Management|Operations Management]] · [[151 Service Operations Management]] ➡

> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Decision Environments and Payoff Tables]]
2. [[#2. Decisions Under Uncertainty: Maximax, Maximin, Laplace, Hurwicz, Regret]]
3. [[#3. Decisions Under Risk: EMV and Expected Opportunity Loss]]
4. [[#4. Expected Value of Perfect Information (EVPI)]]
5. [[#5. Decision Trees and Rollback]]
6. [[#6. Bayesian Revision and the Expected Value of Sample Information (EVSI)]]
7. [[#7. Utility Theory and Risk Attitude]]
8. [[#8. Markov Chains: Brand Switching and Market Share]]
9. [[#9. Markov Chains for Machine States and Absorbing Chains]]
10. [[#10. Monte Carlo Simulation: Steps and a Newsvendor Case]]
11. [[#11. Discrete-Event Simulation: An Inventory Case]]
12. [[#12. Sensitivity Analysis and Tornado Diagrams]]
13. [[#13. Communicating Risk to Executives]]
14. [[#14. ⭐ Advanced: Real Options, Stochastic Programming and Scenario Planning]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Regulators decide on scenarios, not forecasts
> **RBI Financial Stability Report, 30 June 2026.** Reported figures: the gross NPA ratio of banks stood at 1.8% in March 2026 (net NPA 0.4%, capital adequacy ratio 17.7%, CET1 15.3%). In the RBI's stress tests of 46 banks, the baseline scenario sees GNPA edging up to 1.9% by March 2028 with CET1 falling to 13.9%, while two adverse scenarios (geopolitical risks, energy-price pressure and exchange-rate volatility) push GNPA to 3.8% and 4.1%. The report presents a base case and adverse cases side by side, instead of a single prediction: scenario analysis is decision analysis under uncertainty. ([Business Standard, 30 June 2026](https://www.business-standard.com/amp/finance/news/bank-npas-fall-further-in-march-may-rise-under-baseline-scenario-rbi-126063001072_1.html))
>
> **US Federal Reserve 2026 stress-test scenarios (final, 4 February 2026).** The severely adverse scenario has unemployment peaking at 10% in Q3 2027, house prices falling about 30%, equity prices falling about 58% and real GDP contracting 4.6% to its trough, applied to 30 banks. The Fed states explicitly that the scenarios "are not forecasts" and exist to test resilience under hypothetical conditions. ([Federal Reserve](https://www.federalreserve.gov/publications/2026-stress-test-scenarios.htm))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Decision Environments and Payoff Tables
> 🟠 Tier 2 · _Key points:_ Certainty, risk, uncertainty; alternatives, states of nature, payoffs

### Definition
A decision problem has **alternatives** (actions the manager controls), **states of nature** (uncontrollable future conditions), and **payoffs** (outcomes, such as NPV in ₹ crore, for each alternative–state pair), arranged in a **payoff table**. Three environments:

| Environment | What is known | Method |
|---|---|---|
| Certainty | The state | Choose the best payoff (LP and optimisation: [[146 Operations Research - Linear Programming]]) |
| **Risk** | Probabilities of states | Expected monetary value (EMV), decision tree, utility |
| **Uncertainty** | States, not probabilities | Maximax, maximin, Laplace, Hurwicz, minimax regret |

A good decision is not the same as a good outcome: judge decisions by the information and logic at the time, not by luck.

### Example
Running example (NPV in ₹ crore). A firm must choose plant capacity before knowing demand:

| Alternative | Low demand | Medium demand | High demand |
|---|---|---|---|
| Small plant | 40 | 50 | 55 |
| Medium plant | 20 | 80 | 90 |
| Large plant | −40 | 60 | 140 |

Forecast probabilities (for the "risk" sub-topics): Low 0.3, Medium 0.5, High 0.2. The large plant has the highest upside (140) and the worst downside (−40), the small plant the opposite, and the medium plant is a compromise.

### In the news
See news box. A bank stress test is a payoff table: alternatives (capital buffers, lending policies) against scenarios (baseline, adverse 1, adverse 2); the regulator reports outcomes (GNPA, CET1) per scenario and does not claim a single probability.

### Interview angle
> [!question] How it is asked
> "How would you structure a capacity-expansion decision when demand is uncertain?"

> [!tip] Strong answer includes
> - Lay out alternatives, states of nature, payoffs (a table or tree) and the objective (expected value, risk)
> - Say whether probabilities are available; if not, use scenario analysis and robust criteria
> - Include option-like alternatives: phased build, flexible capacity, outsourcing
> - Separate decision quality from outcome

---
## 2. Decisions Under Uncertainty: Maximax, Maximin, Laplace, Hurwicz, Regret
> 🟠 Tier 2 · _Key points:_ Optimist, pessimist, equal-likelihood, coefficient of optimism, minimax regret

### Definition
When probabilities are unknown, criteria express the decision-maker's attitude:

| Criterion | Rule | Attitude |
|---|---|---|
| **Maximax** | Choose the alternative with the largest best-case payoff | Optimist |
| **Maximin** | Choose the alternative with the largest worst-case payoff | Pessimist (conservative) |
| **Laplace** (equal likelihood) | Maximise the average payoff | Treat states as equally likely |
| **Hurwicz** | Maximise $\alpha\,(\text{best})+(1-\alpha)(\text{worst})$, $0\le\alpha\le1$ | Between optimism and pessimism |
| **Minimax regret (Savage)** | Minimise the maximum **regret** (opportunity loss) = best payoff in the state − payoff obtained | Avoids the biggest "I should have chosen differently" |

### Example
Using the payoff table (₹ crore):
- **Maximax:** best cases 55, 90, 140: **Large**.
- **Maximin:** worst cases 40, 20, −40: **Small**.
- **Laplace:** averages 48.3, 63.3, 53.3: **Medium**.
- **Hurwicz** with $\alpha=0.6$: Small $0.6(55)+0.4(40)=49$; Medium $0.6(90)+0.4(20)=62$; Large $0.6(140)+0.4(-40)=68$: **Large**. With $\alpha=0.4$: 46, 48, 32: **Medium**. The answer flips with the optimism coefficient: always state $\alpha$.
- **Minimax regret:** column maxima are 40 (Low), 80 (Medium), 140 (High). Regret table: Small (0, 30, 85), Medium (20, 0, 50), Large (80, 20, 0). Maximum regrets: 85, **50**, 80: **Medium**.

Different criteria give different answers (Large, Small, Medium, Large/Medium, Medium); the interview skill is to explain why and to pick the one that fits the firm's risk appetite.

### In the news
See news box. The RBI's adverse scenarios are a maximin-style view of the system (how bad can it get, and are banks still adequately capitalised?), while the baseline is closer to an expected case.

### Interview angle
> [!question] How it is asked
> "You do not know the probabilities of demand. Which plant do you build, and which criterion are you using?"

> [!tip] Strong answer includes
> - Compute at least maximin, maximax, regret and say they disagree
> - Recommend by firm context: a cash-constrained start-up leans maximin; a cash-rich incumbent in a growth market may be maximax
> - Try to get probabilities (even rough ones) or run scenario analysis, rather than leaning on a pure criterion
> - Note that regret measures the cost of being wrong, which many executives find more natural

---
## 3. Decisions Under Risk: EMV and Expected Opportunity Loss
> 🟠 Tier 2 · _Key points:_ EMV = Σ p × payoff; EOL; EMV can ignore risk appetite

### Definition
With probabilities $p_j$ for states, the **expected monetary value** of alternative $i$ is

$$\text{EMV}_i=\sum_j p_j\,v_{ij}$$

Choose the highest EMV. **Expected opportunity loss (EOL)** = $\sum_j p_j\,r_{ij}$ (expected regret); the alternative with the lowest EOL is the same as the one with the highest EMV. EMV is appropriate for repeated decisions, or when the stakes are small relative to the firm's capital; for large one-off bets, use utility (sub-topic 7).

### Example
Probabilities 0.3, 0.5, 0.2:
- Small: $0.3(40)+0.5(50)+0.2(55)=12+25+11=48$.
- **Medium:** $0.3(20)+0.5(80)+0.2(90)=6+40+18=\mathbf{64}$.
- Large: $0.3(-40)+0.5(60)+0.2(140)=-12+30+28=46$.

**Medium plant: EMV ₹64 crore.** EOL: Small $0.3(0)+0.5(30)+0.2(85)=32$; Medium $0.3(20)+0+0.2(50)=\mathbf{16}$; Large $0.3(80)+0.5(20)+0=34$; the minimum EOL is again Medium. Check the identity: EMV + EOL = expected value under perfect information: $64+16=80$ ✓.

### In the news
See news box. Banks weigh expected losses (probability-weighted) against tail losses (adverse scenarios): EMV-type provisioning in the base case, stress-test capital for the tail.

### Interview angle
> [!question] How it is asked
> "Calculate the EMV of each option. Should we just pick the highest?"

> [!tip] Strong answer includes
> - Compute EMV for each alternative in a clear table
> - Compare the downside as well: Medium also has a limited loss (+20 worst case) while Large has −40
> - Say that EMV treats ₹1 crore gain and loss symmetrically: it fits repeated decisions, not bet-the-company decisions
> - Check how sensitive the decision is to the probability estimates

---
## 4. Expected Value of Perfect Information (EVPI)
> 🟠 Tier 2 · _Key points:_ Upper bound on what any forecast/survey can be worth

### Definition
**Expected value with perfect information (EVwPI):** if a clairvoyant told you the state before you chose, you would choose the best action in each state. 

$$\text{EVwPI}=\sum_j p_j\max_i v_{ij},\qquad \text{EVPI}=\text{EVwPI}-\max_i\text{EMV}_i=\min_i\text{EOL}_i$$

EVPI is the maximum price worth paying for *any* information about the state, however good. It sets a ceiling for market research, pilots, forecasting systems and sensors.

### Example
Best payoff per state: Low 40 (Small), Medium 80 (Medium), High 140 (Large). $\text{EVwPI}=0.3(40)+0.5(80)+0.2(140)=12+40+28=80$. $\text{EVPI}=80-64=\mathbf{₹16\ crore}$, which equals the minimum EOL (16). No survey costing more than ₹16 crore can be worthwhile; a survey is only worth its cost if its EVSI (sub-topic 6) exceeds the price.

### In the news
See news box. Regulators' stress tests are costly; EVPI-style logic asks what it is worth to know the true macro scenario in advance: a high number explains why banks hold capital buffers instead.

### Interview angle
> [!question] How it is asked
> "How much should we pay to eliminate uncertainty about demand?"

> [!tip] Strong answer includes
> - EVPI = EV with perfect information − best EMV (₹80 − ₹64 = ₹16 crore)
> - Equal to minimum expected regret; a ceiling on the value of any study
> - Practical studies give imperfect information: value them with EVSI (next topics)
> - Use EVPI to reject expensive studies quickly

---
## 5. Decision Trees and Rollback
> 🟠 Tier 2 · _Key points:_ Decision nodes (squares), chance nodes (circles), fold back from the right

### Definition
A **decision tree** shows sequential decisions and uncertainties in time order. **Decision nodes** (squares) are choices; **chance nodes** (circles) are uncertain events with branch probabilities; terminal nodes hold payoffs (net of costs along the path). **Rollback (backward induction):** start at the right; at a chance node compute the expected value; at a decision node take the best branch (and prune the others with "//"). The value at the root is the EMV of the optimal strategy, and the path of chosen branches is the **optimal policy**, which can condition later decisions on earlier outcomes.

### Example
Decision: *commission a market survey (cost ₹2 crore) before choosing a plant, or decide now.* From sub-topics 3 and 6:
- **Decide now:** Medium plant, EMV 64.
- **Survey:** with probability 0.47 the result is Favourable, and the best plant then is Large (EMV 85.96); with probability 0.53 it is Unfavourable, and the best plant is Medium (EMV 49.62). EMV of the survey branch before its cost: $0.47(85.96)+0.53(49.62)=66.7$; after the ₹2 crore fee: **64.7**.

Rollback result: survey (64.7) beats deciding now (64.0) by a mere ₹0.7 crore: worth doing only if the survey's assumed reliability is credible, because its value (EVSI = 2.7) barely exceeds its cost. The tree shows the *policy*: build Large if favourable, Medium if unfavourable.

### In the news
See news box. Staged decisions are the heart of scenario planning: wait for the next set of data (like each FSR) and revise the policy, rather than committing to a single path.

### Interview angle
> [!question] How it is asked
> "Draw the decision tree for: launch now, run a pilot first, or abandon. What does it tell you?"

> [!tip] Strong answer includes
> - Square/circle nodes, probabilities that sum to 1, payoffs net of costs along each path
> - Roll back to the root; state the optimal policy, not just the number
> - Compare the value of the pilot (EVSI) with its cost and time delay
> - Test sensitivity of the decision to the key probabilities

---
## 6. Bayesian Revision and the Expected Value of Sample Information (EVSI)
> 🟠 Tier 2 · _Key points:_ Prior × likelihood → posterior; EVSI ≤ EVPI; efficiency

### Definition
Imperfect information (a survey, pilot, test marketing, expert forecast) updates the prior with Bayes' rule:

$$P(\theta_j\mid x)=\frac{P(x\mid\theta_j)\,P(\theta_j)}{\sum_k P(x\mid\theta_k)\,P(\theta_k)}$$

Compute, for each possible message $x$, its probability $P(x)$ and the posterior; choose the best action using posterior EMV; then:

$$\text{EVSI}=\sum_x P(x)\max_i\text{EMV}_i(x)-\max_i\text{EMV}_i^{\text{prior}}$$

**Efficiency of information** $=\text{EVSI}/\text{EVPI}$. See [[210 Bayesian Statistics for Decisions]] and [[087 Probability Fundamentals]] for Bayes' rule and its pitfalls (base rates).

### Example
Survey reliability (likelihood of a Favourable result): $P(F\mid\text{Low})=0.1$, $P(F\mid\text{Medium})=0.5$, $P(F\mid\text{High})=0.95$.

| Result | Joint with (Low, Med, High) | $P(x)$ | Posterior (Low, Med, High) |
|---|---|---|---|
| Favourable | 0.03, 0.25, 0.19 | 0.47 | 0.064, 0.532, 0.404 |
| Unfavourable | 0.27, 0.25, 0.01 | 0.53 | 0.509, 0.472, 0.019 |

Posterior EMVs: after *Favourable*: Small 51.4, Medium 80.2, **Large 86.0**. After *Unfavourable*: Small 45.0, **Medium 49.6**, Large 10.6.
EV with survey $=0.47(85.96)+0.53(49.62)=66.7$. **EVSI** $=66.7-64=\mathbf{₹2.7\ crore}$, and efficiency $=2.7/16=16.9\%$. A survey costing ₹2 crore is worth commissioning (net +0.7); one costing ₹3 crore is not. Note the value arises only because the information *changes the decision* (Large vs Medium); a survey that cannot change the action has EVSI = 0 (an earlier, weaker survey with likelihoods 0.2/0.6/0.9 always left Medium optimal, so its EVSI was exactly zero).

### In the news
See news box. Each FSR and each new stress-test round revises beliefs with new data; the Fed publishes scenarios in advance so banks can plan, which is a structural use of information value.

### Interview angle
> [!question] How it is asked
> "A pilot launch costs ₹1 crore and is 'fairly reliable'. How do you decide if it is worth it?"

> [!tip] Strong answer includes
> - Quantify reliability with likelihoods; apply Bayes to get posteriors and decisions per result
> - Compute EVSI and compare with cost; bound it by EVPI
> - Observe that information has value only if it can change the decision
> - Consider delay (time value, competitor moves) as part of the cost

---
## 7. Utility Theory and Risk Attitude
> 🟠 Tier 2 · _Key points:_ Utility, certainty equivalent, risk premium, exponential utility

### Definition
EMV assumes risk neutrality. **Utility theory** (von Neumann–Morgenstern) converts payoffs into utilities $u(x)$ capturing risk attitude: **risk averse** (concave $u$), **risk neutral** (linear), **risk seeking** (convex). Decide by **expected utility**. The **certainty equivalent (CE)** of a gamble is the sure amount with the same utility; **risk premium** = EMV − CE. A practical form is the **exponential utility** with risk tolerance $R$ (a rough "size of gamble the firm can stomach"):

$$u(x)=1-e^{-x/R},\qquad \text{CE}=-R\ln\!\Big(\sum_jp_je^{-x_j/R}\Big)$$

Utility can be assessed by lottery questions (standard gamble): ask for the probability $p$ at which the manager is indifferent between a sure amount and a gamble between the best and worst outcome.

### Example
A 50:50 gamble of +₹100 crore or −₹40 crore has EMV ₹30 crore. With $R=100$: $\text{CE}=-100\ln(0.5e^{-1}+0.5e^{0.4})=\mathbf{7.3}$ (risk premium ₹22.7 crore); with $R=50$ (a more cautious firm): CE = **−8.3**: the firm would pay ₹8.3 crore to avoid it.

Apply to the plant decision (CE in ₹ crore, computed): $R=100$: Small 47.8, **Medium 59.5**, Large 26.0; $R=50$: 47.7, **54.7**, 9.3; $R=1000$ (nearly risk neutral): 48.0, 63.6, 44.0. The large plant looks poor to a risk-averse firm even though its EMV (46) is close to the small plant's (48), because the −40 downside is heavily penalised. In all three cases Medium still wins, but the *margin* of Medium over Large grows from about ₹20 crore (R = 1000) to ₹33 crore (R = 100) and ₹45 crore (R = 50) as risk aversion rises.

### In the news
See news box. Regulators force risk aversion on banks via capital buffers: the severely adverse scenario (equities −58%, house prices −30%) deliberately weights the downside tail more than an EMV view would.

### Interview angle
> [!question] How it is asked
> "Why might a CFO reject the highest-EMV project?"

> [!tip] Strong answer includes
> - EMV ignores risk attitude and the size of the bet relative to capital (ruin risk)
> - Introduce utility/CE: the risk-adjusted value; risk premium as the cost of volatility
> - Practical tools: limits on downside (max loss), hurdle-rate adjustments, staging
> - Distinguish firm-level risk neutrality (diversified shareholders) from decision-maker risk aversion

---
## 8. Markov Chains: Brand Switching and Market Share
> 🟠 Tier 2 · _Key points:_ Transition matrix, n-step probabilities, steady state πP = π

### Definition
A **Markov chain** models a system moving among states, where the next state depends only on the current one (the **Markov property**). The **transition matrix** $P$ has $P_{ij}=\Pr(\text{next}=j\mid\text{now}=i)$, each row summing to 1. If $\pi^{(0)}$ is the initial state distribution (row vector), then $\pi^{(n)}=\pi^{(0)}P^n$. For a regular chain, $\pi^{(n)}$ converges to the **steady-state** distribution $\pi$ independent of the start:

$$\pi P=\pi,\qquad \sum_j\pi_j=1$$

Uses: market share and customer churn, loyalty and retention, brand switching, credit-rating migration, machine and patient states ([[088 Probability Distributions]], [[031 Product Metrics & Analytics]] for retention/cohort thinking).

### Example
Three quick-commerce apps A, B, C (hypothetical data). Monthly switching: from A: 80% stay, 10% to B, 10% to C; from B: 15% to A, 70% stay, 15% to C; from C: 20% to A, 20% to B, 60% stay. Current shares (0.40, 0.35, 0.25).
- Next month: $0.40(0.8)+0.35(0.15)+0.25(0.2)=0.4225$ for A; B 0.335; C 0.2425.
- Month 2: (0.4368, 0.3252, 0.2380); month 3: (0.4458, 0.3189, 0.2353).
- **Steady state:** solve $\pi P=\pi$ with $\sum\pi=1$: $\pi=(6/13,\ 4/13,\ 3/13)=(46.2\%,\ 30.8\%,\ 23.1\%)$ (verified numerically).
A's long-run share (46.2%) exceeds its current 40% because its retention (80%) beats its rivals'. Strategic levers: retention (diagonal) matters more than acquisition: raising C's retention from 60% to 70% (its row becomes 0.15, 0.15, 0.70) lifts C's long-run share from 23.1% to 28.6% and cuts A's from 46.2% to 42.9% (steady states re-computed). Caveat: the model assumes constant switching probabilities and no market growth; re-estimate regularly.

### In the news
See news box. Loan-status migration (performing → stressed → NPA) can be modelled as a Markov chain; projections such as "GNPA edges up from 1.8% to 1.9% by March 2028" rest on migration assumptions of this kind under macro scenarios (the RBI's actual framework is more elaborate than a single transition matrix).

### Interview angle
> [!question] How it is asked
> "Customers switch between three brands with these probabilities. What happens to market share in the long run?"

> [!tip] Strong answer includes
> - Set up the transition matrix correctly; check rows sum to 1
> - Steady state by solving $\pi P=\pi$ plus normalisation; show a short-run projection too
> - Interpret: retention drives long-run share; compute impact of retention improvements
> - State assumptions (stationary probabilities, no new entrants) and how to relax them

---
## 9. Markov Chains for Machine States and Absorbing Chains
> 🟠 Tier 2 · _Key points:_ Availability from steady state; time to failure via fundamental matrix

### Definition
Machines move among states (Good, Degraded, Failed). The long-run **availability** is the sum of steady-state probabilities of operating states. If a chain has **absorbing** states (e.g., Failed with no repair), write $P=\begin{pmatrix}Q&R\\0&I\end{pmatrix}$; the **fundamental matrix** $N=(I-Q)^{-1}$ gives expected visits to each transient state, and $N\mathbf 1$ gives the **expected number of periods until absorption** from each state. Links: maintenance planning and condition-based maintenance ([[022 Maintenance Management (TPM-RCM)]], [[155 Reliability Engineering & Maintenance Optimisation]]).

### Example
Weekly states with repair: Good → Good 0.85, Worn 0.10, Failed 0.05; Worn → Worn 0.70, Failed 0.30; Failed → Good 1.0 (repair takes one week and restores as-new).

**Steady state:** $\pi=(60/89,\ 20/89,\ 9/89)=(0.674,\ 0.225,\ 0.101)$. **Availability** (Good or Worn) $=89.9\%$; the machine is down 10.1% of weeks. If an unplanned failure week costs ₹80,000 in lost output and repair, the expected cost is $0.101\times80{,}000\approx₹8{,}090$ per week. Preventive intervention (replacing a Worn machine at ₹20,000 during a planned stop) can be tested by changing the Worn row.

**Absorbing version** (failure terminal, no repair): $Q=\begin{pmatrix}0.85&0.10\\0&0.70\end{pmatrix}$: $N=\begin{pmatrix}6.67&2.22\\0&3.33\end{pmatrix}$, so the **expected time to failure is 8.9 weeks from Good** and 3.3 weeks from Worn (computed with NumPy). The Worn state shortens remaining life by 63%, a quantified case for condition monitoring.

### In the news
See news box. The same state-and-migration logic is used for loans (performing, stressed, NPA) in credit-risk stress testing, though real bank models are far richer.

### Interview angle
> [!question] How it is asked
> "How would you estimate the availability of a machine that cycles through Good, Worn and Failed states?"

> [!tip] Strong answer includes
> - Define states and transition probabilities from maintenance records
> - Solve the steady state; availability = sum of operating-state probabilities
> - Convert to ₹: downtime cost per period times the failure probability, compare with preventive actions
> - Mention limits: the Markov property (age not remembered), data needs, and semi-Markov extensions

---
## 10. Monte Carlo Simulation: Steps and a Newsvendor Case
> 🟠 Tier 2 · _Key points:_ Model, distributions, random draws, many trials, summarise

### Definition
**Monte Carlo simulation** samples uncertain inputs from probability distributions, computes the output for each sample, and summarises the distribution of outputs. Steps: (1) define the output metric (profit, NPV, completion date); (2) build the deterministic model; (3) assign distributions to uncertain inputs (from data or expert ranges: triangular, normal, lognormal, PERT); (4) model correlations; (5) run thousands of trials with random draws (Excel RAND/NORM.INV, `@RISK`, Python NumPy: [[046 Python for Operations]], [[074 Array & Dynamic Array Functions]]); (6) report mean, percentiles (P10/P50/P90), probability of a threshold event; (7) check convergence (standard error $\sigma/\sqrt n$); (8) test sensitivity. Monte Carlo handles distributions and non-linear models that closed-form formulas cannot.

### Example
**Newsvendor.** A seasonal item: selling price ₹50, cost ₹30, salvage ₹0; demand normal with mean 100 and standard deviation 20. Underage cost $C_u=20$, overage cost $C_o=30$, critical ratio $=C_u/(C_u+C_o)=0.40$, so $Q^*=100+z_{0.40}\times20=100-0.2533\times20=\mathbf{94.9\approx95}$. Monte Carlo with 200,000 demand draws (Python, seed 2026) against the closed-form expected profit:

| Order $Q$ | MC mean profit (₹) | Exact (₹) | P10 profit | Std dev | P(profit < 0) |
|---|---|---|---|---|---|
| 80 | 1,517 | 1,517 | 1,320 | 261 | 0.5% |
| 90 | 1,603 | 1,602 | 1,020 | 412 | 1.1% |
| **95** | **1,614** | 1,614 | 870 | 497 | 1.6% |
| 100 | 1,602 | 1,601 | 720 | 583 | 2.3% |
| 110 | 1,504 | 1,502 | 420 | 743 | 4.5% |

The profit curve is flat near the optimum (₹1,602 to ₹1,614 between 90 and 100) but the risk (spread and downside) rises quickly with $Q$: choosing 90 instead of 95 gives up about ₹12 of mean profit and cuts the standard deviation by 17%. This is the "mean versus risk" conversation executives need. Inventory theory of the same structure: [[003 Inventory Management]], [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]].

### In the news
See news box. Stress-testing and scenario engines at banks use Monte Carlo and scenario paths to produce loss distributions; regulators prescribe the scenarios, banks supply the models.

### Interview angle
> [!question] How it is asked
> "How would you quantify the risk in a project's NPV, and how is that better than a base-case estimate?"

> [!tip] Strong answer includes
> - Replace point estimates with distributions for the key uncertain inputs; run thousands of trials
> - Report percentiles and probability of loss, not just the mean
> - Check convergence and test input assumptions; mention correlations
> - Compare with an analytic result when available to validate the code (e.g., newsvendor critical ratio)

---
## 11. Discrete-Event Simulation: An Inventory Case
> 🟠 Tier 2 · _Key points:_ Events, state, clock, KPIs; compare policies; replications

### Definition
**Discrete-event simulation (DES)** models a system as a sequence of events (demand arrival, order arrival, machine breakdown) that change the state at discrete times. Components: **state variables** (inventory, orders outstanding), **event list**, **clock**, **random-input generators**, and **statistics counters**. Use it when interactions and timing matter (inventory with lead-time variability, queues with priorities: [[149 Queueing Theory & Waiting-Line Analysis]], supply-chain networks). Tools: SimPy ([[068 Operations-Specific Python (PuLP, SimPy)]]), AnyLogic, Arena, Simio, FlexSim. Good practice: warm-up, common random numbers when comparing policies, multiple replications, confidence intervals, validation.

### Example
Continuous-review $(r,Q)$ policy: daily demand Poisson with mean 20; supplier lead time equally likely 2, 3 or 4 days (mean 3, so mean lead-time demand = 60); order quantity $Q=200$; start with inventory $r+Q$; unmet demand is lost. Simulating 365 days, 300 replications (seed 0):

| Reorder point $r$ | Fill rate | Avg on-hand | Orders/yr | Stock-out days/yr |
|---|---|---|---|---|
| 40 | 93.7% | 89 | 33.7 | 33.8 |
| 60 (= mean LTD) | 98.2% | 104 | 35.3 | 12.5 |
| 80 | 99.85% | 122 | 35.9 | 1.7 |
| 100 | 100% | 142 | 36.0 | 0.0 |

Reading: reordering at the *mean* lead-time demand still leaves 12.5 stock-out days a year; moving $r$ from 60 to 80 buys about 1.7 points of fill rate (98.2% to 99.85%) for roughly 18 more units of average stock (104 to 122). The manager picks $r$ by comparing the cost of the extra stock with the cost of lost sales. Closed-form safety-stock formulas ([[003 Inventory Management]]) give the same direction; simulation handles lost sales, mixed lead times and other messy rules.

```python
import numpy as np
def sim(r, Q, days=365, reps=300, seed=0):
    rng = np.random.default_rng(seed); fills = []
    for _ in range(reps):
        inv, pipe, dem_tot, short = r + Q, [], 0, 0
        for _d in range(days):
            pipe = [(t - 1, q) for t, q in pipe]
            inv += sum(q for t, q in pipe if t <= 0); pipe = [(t, q) for t, q in pipe if t > 0]
            dem = rng.poisson(20); sold = min(inv, dem); inv -= sold
            dem_tot += dem; short += dem - sold
            if inv + sum(q for _, q in pipe) <= r: pipe.append((rng.choice([2, 3, 4]), Q))
        fills.append(1 - short / dem_tot)
    return np.mean(fills)
```

### In the news
See news box. Regulatory stress tests are scenario-based simulations at industry scale; firms mirror them internally (what if a port closes, a supplier fails, demand drops 20%?) using DES and Monte Carlo.

### Interview angle
> [!question] How it is asked
> "How would you compare two inventory policies when demand and lead time are uncertain?"

> [!tip] Strong answer includes
> - Build a simulation with realistic demand and lead-time distributions; same random numbers for both policies
> - KPIs: fill rate, stock-out days, average inventory, orders per year, total cost
> - Replications and confidence intervals; warm-up when needed
> - Validate against a simple formula or past data

---
## 12. Sensitivity Analysis and Tornado Diagrams
> 🟠 Tier 2 · _Key points:_ One-at-a-time swings; break-even; scenario vs Monte Carlo

### Definition
**Sensitivity analysis** shows which inputs most affect the output. **One-way (tornado) analysis:** vary each input across a plausible low-high range with the others at base, record the output swing, and sort bars from largest to smallest; the shape resembles a tornado. Complements: **break-even analysis** (value at which the decision flips), **two-way tables** (data tables in Excel: [[077 Solver, Goal Seek & What-If Analysis]]), **scenario analysis** (coherent bundles of inputs), and **probabilistic sensitivity** (Monte Carlo with rank correlation or variance contribution). Tornado diagrams are one-at-a-time and miss interactions; ranges must be justified, not equal percentages by habit.

### Example
Profit $=(p-v)\,q-F$ with price $p=₹120$, variable cost $v=₹70$, volume $q=10{,}000$, fixed cost $F=₹3{,}00{,}000$: base profit **₹2,00,000**. Ranges: price ±10%, variable cost ±10%, volume ±20%, fixed cost ±10%.

| Input | Low case | High case | Profit at low | Profit at high | Swing |
|---|---|---|---|---|---|
| Price | ₹108 | ₹132 | ₹80,000 | ₹3,20,000 | **₹2,40,000** |
| Volume | 8,000 | 12,000 | ₹1,00,000 | ₹3,00,000 | ₹2,00,000 |
| Variable cost | ₹77 | ₹63 | ₹1,30,000 (at ₹77) | ₹2,70,000 (at ₹63) | ₹1,40,000 |
| Fixed cost | ₹3,30,000 | ₹2,70,000 | ₹1,70,000 | ₹2,30,000 | ₹60,000 |

Tornado order: price, volume, variable cost, fixed cost. Break-even price (profit zero): $p=70+300{,}000/10{,}000=₹100$, i.e., a 16.7% fall from ₹120. **Monte Carlo** with triangular distributions over the same ranges (200,000 trials): mean ₹2.00 lakh, standard deviation ₹71,000, P10 ₹1.09 lakh, P50 ₹1.98 lakh, P90 ₹2.94 lakh, probability of loss about 0.04%: the one-at-a-time extremes (₹80,000 profit in the worst single-input case) overstate the risk because all four inputs rarely hit their extremes together. The managerial message: pricing discipline matters more than fixed-cost trimming (see [[110 Cost Accounting for Operations]] for the CVP logic).

### In the news
See news box. The RBI's two adverse scenarios and the Fed's severely adverse scenario are *joint* shocks (energy prices, FX and growth together, or unemployment, housing and equity together): scenario analysis rather than one-at-a-time sensitivity, because the shocks are correlated.

### Interview angle
> [!question] How it is asked
> "Which assumptions should the board worry about most in this business case?"

> [!tip] Strong answer includes
> - One-way tornado with defensible ranges, sorted by swing; name the top two drivers
> - Break-even values for the key drivers (price down 16.7% wipes out profit)
> - Use scenarios for correlated shocks and Monte Carlo for a probability of loss
> - Focus management attention and risk mitigation on the top drivers

---
## 13. Communicating Risk to Executives
> 🟠 Tier 2 · _Key points:_ Ranges not points; P10/P50/P90; decision first; visual choices

### Definition
Executives need a decision, the reasoning, and the risk, in that order. Practices:
- **Lead with the recommendation** and the decision rule ("build Medium; switch to Large only if a favourable pilot result arrives").
- **Give ranges and percentiles:** P10/P50/P90 and probability of loss, not just a mean; say what the ranges assume.
- **Use the right visuals:** tornado (what drives the answer), histogram or cumulative curve (the distribution), fan chart (time), payoff or regret table (alternatives), decision tree (policy). See [[047 MIS & Dashboard Design]] and [[029 Data Interpretation & Charts]].
- **Frame downside in business terms** (₹ crore, months of runway, covenant breach), and name early-warning triggers and mitigations.
- **Separate facts, estimates and judgement;** show what would change the recommendation.
- **Avoid false precision** (₹64.0 crore EMV from guessed probabilities is not 64.0): round, and state confidence.
- Structure the story with the storyline methods in [[162 Structured Communication - SCQA, Storylines & Case Delivery]].

### Example
Board summary for the plant decision: "**Recommend the Medium plant: expected NPV ₹64 crore, a 70% chance of at least ₹80 crore, and a worst case of +₹20 crore.** The Large plant has higher upside (₹140 crore) but a 30% chance of losing ₹40 crore, and a lower risk-adjusted value (certainty equivalent ₹26 crore against ₹59 crore for Medium at a risk tolerance of ₹100 crore). A ₹2 crore market survey is marginally worthwhile (value ₹2.7 crore): if favourable, upgrade to Large (EMV ₹86 crore). Key sensitivity: Large overtakes Medium only if the probability of High demand rises above about 46%."

How the 46% is derived (always compute the flip point rather than guess it): holding Low demand at 0.3, let $p_H$ be High and $0.7-p_H$ be Medium. Large minus Medium EMV $=(-40-20)(0.3)+(60-80)(0.7-p_H)+(140-90)p_H=-18-14+20p_H+50p_H=-32+70p_H$, which is positive when $p_H>0.457$. At $p_H=0.457$ both plants have an EMV of about ₹66.6 crore.

### In the news
See news box. The RBI and Fed present their risk as scenarios with explicit assumptions, headline numbers and "not a forecast" language: a good model of communicating uncertainty to non-technical audiences.

### Interview angle
> [!question] How it is asked
> "How would you explain the uncertainty in your forecast and recommendation to the CEO in two minutes?"

> [!tip] Strong answer includes
> - Recommendation first, then the 2–3 numbers that matter (expected value, range, probability of loss)
> - One visual (tornado or distribution), plain language, the assumption that would flip the decision
> - Triggers and contingency plans, not just risk descriptions
> - Honesty about model limits and data quality

---
## 14. ⭐ Advanced: Real Options, Stochastic Programming and Scenario Planning
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Value of flexibility / real options:** the ability to delay, expand, switch or abandon has value because decisions can be conditioned on information. A decision tree with options (rolling back with the best choice at each node) automatically values them; the option's value is the difference between the tree with and without the flexible branch ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]], [[109 Valuation Basics (NPV, IRR, DCF)]]).
- **Two-stage stochastic programming:** choose first-stage decisions now (capacity, inventory) and recourse decisions after uncertainty resolves (production, shipping), minimising expected total cost. **Value of the stochastic solution (VSS)** = cost of using the mean-value solution minus the stochastic optimum; **EVPI** carries over (wait-and-see versus here-and-now).
- **Robust optimisation / minimax regret planning:** protect against the worst case in an uncertainty set; a mathematical form of the maximin and regret criteria of sub-topic 2.
- **Scenario planning:** narrative, internally consistent futures used when probabilities are unknowable; pair with indicators that signal which scenario is unfolding. Regulators' stress tests are a formal version.
- **Markov decision processes (MDPs):** sequential decisions with Markov transitions; the language of dynamic pricing, replacement, and reinforcement learning ([[218 Forecasting with ML & Foundation Models]] for forecast inputs).

### Example
Flexibility value with the running example. Suppose the firm builds the Medium plant now and holds an option to add a ₹30 crore expansion once demand is known. The expansion lifts the High-demand gross payoff of Medium from 90 to 135, so after its cost the High payoff is $135-30=105$; it is exercised only in the High state, where it adds 15 net (in the other states it would not pay for itself). Medium with the option has payoffs 20, 80, 105 and $\text{EMV}=0.3(20)+0.5(80)+0.2(105)=6+40+21=67$, against 64 without the option: the **option is worth ₹3 crore**. It also beats the survey strategy (64.7 net of the ₹2 crore fee) under these illustrative numbers, because staging pays only where the expansion is worth exercising. Change the expansion cost to ₹50 crore and the option has no value (net High payoff 85, below 90), which shows how sensitive such conclusions are to the cost assumption.

### In the news
See news box. Stress-test scenarios are explicitly not forecasts, and banks must hold capital that works across them: robust planning in practice.

### Interview angle
> [!question] How it is asked
> "How do you value the flexibility to expand later versus committing to a larger plant now?"

> [!tip] Strong answer includes
> - Model the option in a decision tree: later decision conditioned on revealed demand
> - The value of the option = EMV with option − EMV without; compare to its upfront premium
> - Link to real options and stochastic programming (VSS, EVPI) in more advanced settings
> - Caution: assumptions on expansion cost and timing drive the answer, so stress-test them
