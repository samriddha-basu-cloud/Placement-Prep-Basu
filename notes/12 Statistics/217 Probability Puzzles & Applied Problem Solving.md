---
tags: [statistics, tier3]
area: Statistics
topic: "Probability Puzzles & Applied Problem Solving"
tier: Tier 3
roles: All roles
status: complete
subtopics: 13
---
# Probability Puzzles & Applied Problem Solving

⬅ [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]] · [[_Index - Statistics|Statistics]]

> **Area:** Statistics · **Priority:** 🟡 Tier 3 · **Target roles:** All roles

## Sub-topics in this note
1. [[#1. Thinking-Aloud Template for Any Probability Puzzle]]
2. [[#2. Counting Techniques]]
3. [[#3. The Birthday Problem]]
4. [[#4. Monty Hall and Conditional-Probability Traps]]
5. [[#5. Bayes and the Medical-Test Puzzle]]
6. [[#6. Coin Puzzles and Waiting Times]]
7. [[#7. Dice and Expected-Value Games]]
8. [[#8. Gambler's Ruin]]
9. [[#9. The Matching (Derangement) Problem]]
10. [[#10. Reliability Systems: Series, Parallel and k-out-of-n]]
11. [[#11. The Secretary (Optimal Stopping) Problem]]
12. [[#12. Monte Carlo as a Verification Habit]]
13. [[#13. ⭐ Advanced: First-Step Analysis, Indicators and Markov Chains]]

## 📰 News box
> [!news] Why this matters now (2024–2026): Bayes' theorem is now written into regulator guidance
> **FDA draft guidance on Bayesian methodology (9 Jan 2026; Federal Register notice 12 Jan 2026).** The US FDA published draft guidance on how Bayesian methods can support regulatory decisions in clinical trials, covering interim adaptations and dose selection as well as end-of-trial conclusions, across INDs, NDAs and BLAs. The same conditional-probability machinery that interviewers test with a "positive medical test" puzzle (prior, likelihood, posterior) is what a regulator now expects trial teams to use explicitly. ([Alston and Bird summary](https://www.alston.com/en/insights/publications/2026/01/fda-bayesian-guidance-drug-trials); [Federal Register notice](https://www.federalregister.gov/documents/2026/01/12/2026-00325/use-of-bayesian-methodology-in-clinical-trials-of-drug-and-biological-products-draft-guidance-for))
>
> Sub-topics that say **"See news box"** reuse this item.

---
## 1. Thinking-Aloud Template for Any Probability Puzzle
> 🟡 Tier 3 · _Key points:_ Restate, define the sample space, pick a method, sanity-check, then verify by simulation

### Definition
Interviewers rarely care whether you remember the answer to a puzzle; they score **how you structure an unfamiliar problem**. A reliable seven-step spoken template:

1. **Restate** the problem in your own words and confirm the rules ("Each draw is without replacement, correct?").
2. **Define the experiment and the event** precisely: what is random, what is being asked.
3. **Choose the tool**: counting (equally likely outcomes), conditioning/Bayes, complement ("at least one" is $1-P(\text{none})$), symmetry, linearity of expectation, or first-step analysis (recursion on the first move).
4. **Compute on a small case** (n = 2 or 3) to check your formula.
5. **State the answer with units** and a one-line intuition.
6. **Sanity-check**: limits, bounds ($0\le p\le1$), symmetry, comparison with a rough estimate.
7. **Offer a simulation** ("I would confirm with 100,000 Monte Carlo trials") and say what the code would do.

Three habits that win marks: say assumptions out loud (fair coin, independent rolls), prefer the complement for "at least one" questions, and distinguish **"what I know"** from **"what I am conditioning on"**. Most famous puzzles are traps in conditioning: the information is revealed by a *process* (a host who knows), not just a *fact*.

### Example
Question: "A family has two children; at least one is a boy. P(both boys)?" Spoken answer: "Sample space (older, younger): BB, BG, GB, GG, equally likely. Conditioning on 'at least one boy' removes GG, leaving three outcomes, one of which is BB. So 1/3. If the statement were 'the older child is a boy' the space is BB, BG, so 1/2: the wording of the information changes the answer. I would check with a quick simulation." (A simulation of 200,000 families gave 0.3333 and 0.5003.)

### In the news
See news box. Regulatory Bayesian reasoning is this template applied at scale: state the prior, update on data, report the posterior probability.

### Interview angle
> [!question] How it is asked
> "Here is a brain-teaser. Take your time and think out loud."

> [!tip] Strong answer includes
> - Restating the problem and the assumptions before computing
> - A named method (complement, Bayes, symmetry, linearity, recursion)
> - A small-case check and a sanity bound
> - Offering a Monte Carlo check and reading the result honestly
> - Staying calm if the first approach fails: say "let me try conditioning instead"

---
## 2. Counting Techniques
> 🟡 Tier 3 · _Key points:_ Multiplication rule, permutations, combinations, repeated letters, stars and bars, complement

### Definition
When outcomes are equally likely, $P(A)=\frac{\#A}{\#\Omega}$ and the work is counting.

- **Multiplication rule:** independent stages with $n_1,n_2,\dots$ options give $n_1n_2\cdots$ outcomes.
- **Permutations** (order matters, no repeats): $P(n,r)=\frac{n!}{(n-r)!}$.
- **Combinations** (order ignored): $\binom{n}{r}=\frac{n!}{r!(n-r)!}$.
- **Arrangements with repeated items:** $\frac{n!}{n_1!\,n_2!\cdots}$.
- **Circular arrangements** of $n$ distinct people: $(n-1)!$.
- **Stars and bars:** the number of ways to distribute $n$ identical items into $k$ bins is $\binom{n+k-1}{k-1}$.
- **Inclusion-exclusion** and the **complement trick** for "at least one".

Hypergeometric draws (without replacement) use $\binom{K}{k}\binom{N-K}{n-k}/\binom{N}{n}$; the full treatment of distributions is in [[088 Probability Distributions]] and the basic rules in [[087 Probability Fundamentals]].

### Example
- Distinct arrangements of the letters in MISSISSIPPI: $\frac{11!}{4!\,4!\,2!}=\mathbf{34{,}650}$.
- Distribute 10 identical cartons among 4 retailers (zero allowed): $\binom{13}{3}=\mathbf{286}$.
- A committee of 3 men and 2 women from 6 men and 5 women: $\binom{6}{3}\binom{5}{2}=20\times10=\mathbf{200}$.
- Poker one-pair hand: $13\binom{4}{2}\binom{12}{3}4^3=1{,}098{,}240$ out of $\binom{52}{5}=2{,}598{,}960$, so $P=\mathbf{42.26\%}$.
- Seating 6 people at a round table: $5!=\mathbf{120}$.

```python
from math import comb, factorial
print(factorial(11)//(factorial(4)*factorial(4)*factorial(2)))   # 34650
print(comb(13,3), comb(6,3)*comb(5,2))                           # 286 200
print(13*comb(4,2)*comb(12,3)*4**3/comb(52,5))                   # 0.42257
```

### In the news
See news box. Counting underlies the combinatorial design of clinical-trial simulations and, in operations, the number of SKU-route-vehicle assignments a solver must search ([[146 Operations Research - Linear Programming]]).

### Interview angle
> [!question] How it is asked
> "How many ways can 5 identical pallets be placed in 3 bays?" or "Probability a random 5-card hand is a flush?"

> [!tip] Strong answer includes
> - Naming the structure: ordered or unordered, with or without repeats, identical or distinct
> - Using complement for "at least one"
> - A tiny case (2 pallets, 2 bays) to confirm the formula
> - Not over-counting symmetric cases (divide by the repeats)

---
## 3. The Birthday Problem
> 🟡 Tier 3 · _Key points:_ P(shared birthday) in a group; complement; 23 people gives about 50%; approximation 1 - exp(-n(n-1)/730)

### Definition
In a group of $n$ people, assuming 365 equally likely birthdays and independence, the probability that **no two share** a birthday is

$$P(\text{all different})=\prod_{i=0}^{n-1}\frac{365-i}{365}\qquad P(\text{match})=1-\prod_{i=0}^{n-1}\frac{365-i}{365}$$

Why it surprises: the number of **pairs** grows as $\binom{n}{2}$, not $n$. A useful approximation is $P(\text{match})\approx1-e^{-n(n-1)/(2\cdot365)}$. The same logic governs **hash collisions** and duplicate-ID risk in databases.

### Example
| n | P(at least one shared birthday) |
|---|---|
| 10 | 11.7% |
| 23 | **50.7%** |
| 30 | 70.6% |
| 40 | 89.1% |
| 50 | 97.0% |
| 70 | 99.92% |

For $n=23$: pairs $=\binom{23}{2}=253$; approximation gives $1-e^{-253/365}=50.0\%$ (exact 50.73%). A class of 60 MBA students almost surely has a shared birthday; a team of 10 has about 1 chance in 9.

```python
import numpy as np
rng = np.random.default_rng(1)
b = rng.integers(0, 365, (100000, 23))
print(np.mean([len(set(r)) < 23 for r in b]))   # ~0.507
```

### In the news
See news box. Collision probabilities of this form are why identifiers and hashes need far more distinct values than the number of records.

### Interview angle
> [!question] How it is asked
> "How many people do you need in a room for a better-than-even chance two share a birthday?"

> [!tip] Strong answer includes
> - Compute the complement (all different), not the match directly
> - Explain the pairs intuition (253 pairs among 23 people)
> - Quote 23 and the 1 - e^(-n(n-1)/730) approximation
> - Mention assumptions (uniform birthdays, ignoring 29 February; real birthdays are slightly non-uniform, which makes matches a bit more likely)
> - Apply it: probability of duplicate order numbers or hash collisions

---
## 4. Monty Hall and Conditional-Probability Traps
> 🟡 Tier 3 · _Key points:_ Switch wins 2/3; host knowledge matters; two-children problem; Bertrand's box

### Definition
**Monty Hall.** Three doors, one car. You pick a door; the host, who **knows** where the car is, opens a different door showing a goat and offers a switch. Your first pick was right with probability 1/3, and this does not change when a goat is revealed; the remaining 2/3 concentrates on the other closed door. So **switching wins with probability 2/3**.

Generalisation: with $n$ doors and the host opening $n-2$ goat doors, switching wins $\frac{n-1}{n}$ (99% for 100 doors). If the host opens a door **at random** and happens to show a goat, the posterior for staying becomes 1/2: the host's knowledge is the whole puzzle.

**Related traps**
- **Two children.** "At least one is a boy" gives P(two boys) $=1/3$; "the older is a boy" gives $1/2$. Adding "born on a Tuesday" to the first statement moves the answer to $13/27\approx48.1\%$ because it makes the information more specific.
- **Bertrand's box.** Three boxes: gold-gold, gold-silver, silver-silver. A random coin drawn is gold. P(the other coin is gold) $=\frac{1\cdot\frac13}{1\cdot\frac13+\frac12\cdot\frac13}=\mathbf{2/3}$, not 1/2: a gold coin is twice as likely to come from the GG box.

The cure for every one of these is to **list the equally likely elementary outcomes** and delete those contradicting the information, or to write Bayes' rule explicitly ([[087 Probability Fundamentals]], [[210 Bayesian Statistics for Decisions]]).

### Example
Simulation of 200,000 games: staying wins 33.4%, switching wins 66.6%. Two-children simulation: P(both boys | at least one boy) = 0.3333; P(both | older is boy) = 0.5003; P(both | a boy born on Tuesday) = 0.479 (theory 0.4815).

```python
import numpy as np
rng = np.random.default_rng(0)
car = rng.integers(0, 3, 200000); pick = rng.integers(0, 3, 200000)
print("stay", np.mean(car == pick), "switch", np.mean(car != pick))
```

### In the news
See news box. The posterior-updating logic of Monty Hall (new information changes the odds only through the process that generated it) is exactly the point regulators make about prior specification and trial design.

### Interview angle
> [!question] How it is asked
> "In Monty Hall, why does switching help? What if the host did not know where the car was?"

> [!tip] Strong answer includes
> - 1/3 vs 2/3 reasoning ("the host's action carries information")
> - The 100-door intuition
> - The host-ignorance variant giving 1/2
> - Willingness to simulate rather than argue
> - Linking to Bayes: prior 1/3 each, likelihood of the host's choice

---
## 5. Bayes and the Medical-Test Puzzle
> 🟡 Tier 3 · _Key points:_ Base rates, sensitivity, specificity, PPV, natural frequencies, repeated tests

### Definition
With prevalence $\pi$, sensitivity $Se=P(+\mid D)$ and false-positive rate $\alpha=1-Sp=P(+\mid \bar D)$:

$$P(D\mid +)=\frac{\pi\,Se}{\pi\,Se+(1-\pi)\,\alpha}\qquad P(\bar D\mid -)=\frac{(1-\pi)\,Sp}{(1-\pi)\,Sp+\pi\,(1-Se)}$$

$P(D\mid+)$ is the **positive predictive value (PPV)**. For rare conditions PPV is low even when the test is accurate, because false positives from the large healthy group swamp true positives. This is the **base-rate fallacy**. The easiest way to explain it aloud is with **natural frequencies**: "Out of 1,000 people..." The same maths drives fraud-alert precision, defect detection and quality inspection ([[091 Statistical Quality Control (SQC)]]).

### Example
Prevalence 1%, sensitivity 90%, false-positive rate 9%.

Per 1,000 people: 10 diseased, of whom $10\times0.9=9$ test positive; 990 healthy, of whom $990\times0.09=89.1$ test positive. So $P(D\mid+)=\frac{9}{9+89.1}=\mathbf{9.17\%}$ (exact: $0.009/0.0981$). A positive result is about 1 in 11 likely to be real.

A **second independent positive** test: $\frac{0.01(0.9)^2}{0.01(0.9)^2+0.99(0.09)^2}=\mathbf{50.3\%}$.

TB-screening variant: prevalence 2%, sensitivity 95%, specificity 98%: $PPV=\frac{0.019}{0.019+0.0196}=\mathbf{49.2\%}$ and $NPV=\mathbf{99.9\%}$. Screening works for ruling out, not for confirming.

```python
prev, se, fpr = 0.01, 0.90, 0.09
ppv = prev*se / (prev*se + (1-prev)*fpr)
print(round(ppv, 4))                                    # 0.0917
ppv2 = prev*se**2 / (prev*se**2 + (1-prev)*fpr**2)
print(round(ppv2, 4))                                   # 0.5025
```

### In the news
See news box. The FDA's Bayesian guidance formalises this prior-likelihood-posterior chain for drug trials; the screening-test version is the version most people meet first.

### Interview angle
> [!question] How it is asked
> "A test is 90% accurate and you test positive. What is the chance you have the disease?" Or "A fraud model flags a transaction; how likely is it truly fraud?"

> [!tip] Strong answer includes
> - Asking for the prevalence (base rate) before answering
> - Natural-frequency walk-through in under a minute
> - Distinguishing sensitivity, specificity, PPV and NPV
> - Noting that 90% accuracy is ambiguous without sensitivity and specificity
> - Business translation: alert precision, review workload, cost of false positives

---
## 6. Coin Puzzles and Waiting Times
> 🟡 Tier 3 · _Key points:_ Expected tosses for HH and HT, Penney's game, geometric waiting times, first-step analysis

### Definition
- **Geometric waiting time.** The number of fair tosses to the first head has mean 2; the number of rolls of a fair die to the first six has mean 6. For success probability $p$, $E[N]=1/p$.
- **Expected tosses for a pattern.** Using first-step analysis: $E[\text{HT}]=4$, $E[\text{HH}]=6$, $E[\text{HHH}]=14$, $E[\text{HTH}]=10$. A pattern that can overlap with itself takes longer (HH overlaps itself; HT cannot). A quick rule: $E=\sum 2^{k}$ over each prefix length $k$ that equals a suffix (HH: $2^1+2^2=6$; HT: $2^2=4$; HTH: $2^1+2^3=10$).
- **Penney's game.** Despite equal expected frequency, patterns are **not transitive**: against HTH, the pattern HHT wins with probability 2/3. The second player can always choose a pattern that beats the first player's choice.

**First-step analysis for HH.** Let $E$ be the expected tosses. After the first toss: with prob 1/2 it is T (back to start, cost 1+E); with prob 1/2 it is H, and then next toss gives H (done, total 2) or T (restart, 2+E). So $E=\frac12(1+E)+\frac14(2)+\frac14(2+E)\Rightarrow E=6$.

### Example
Game: you and a friend each pick a three-toss pattern; the first to appear wins. If the friend picks HTH, you pick HHT and win 66.6% of the time (simulation: 0.666). Expected waiting times from 50,000-sequence simulations: HH 5.98, HT 4.00, HHH 14.01, HTH 9.98.

```python
import numpy as np
rng = np.random.default_rng(0)
def wait(pat):
    s, c = "", 0
    while not s.endswith(pat):
        s += "H" if rng.random() < .5 else "T"; c += 1
    return c
print(np.mean([wait("HH") for _ in range(50000)]))   # ~6
print(np.mean([wait("HT") for _ in range(50000)]))   # ~4
```

### In the news
See news box. Waiting-time and run-length results also underlie sequential monitoring in trials and control-chart run rules ([[091 Statistical Quality Control (SQC)]]).

### Interview angle
> [!question] How it is asked
> "On average how many tosses until you see two heads in a row? Why is it more than for a head followed by a tail?"

> [!tip] Strong answer includes
> - First-step (recursive) equation for E with the algebra
> - Intuition: after HH-failure you lose all progress; after HT-failure you keep a T but not an H
> - The answer 6 vs 4, and Penney's non-transitivity as a bonus
> - A simulation check

---
## 7. Dice and Expected-Value Games
> 🟡 Tier 3 · _Key points:_ Linearity of expectation, optimal stopping, re-roll strategy, pricing a game fairly

### Definition
**Expected value** $E[X]=\sum x\,P(x)$. **Linearity of expectation** says $E[X+Y]=E[X]+E[Y]$ even when $X$ and $Y$ are dependent, which makes many "hard-looking" counts easy by writing them as sums of indicator variables. A game is **fair** at entry price $E[\text{payoff}]$. Optimal-stopping games are solved **backwards** by comparing the value in hand with the expected value of continuing ([[150 Decision Analysis & Simulation]]).

Standard results for fair dice:
- One die: $E=3.5$, variance $35/12$.
- Maximum of two dice: $E[\max]=\frac{161}{36}=4.472$.
- Rolls to see **all six faces** (coupon collector): $6\left(1+\tfrac12+\tfrac13+\tfrac14+\tfrac15+\tfrac16\right)=\mathbf{14.7}$.
- Rolls until **two consecutive sixes**: $6+36=\mathbf{42}$.

### Example
**Re-roll game.** You roll a die and may keep the face (paid ₹ equal to the face value ×100) or re-roll once, taking the second result. Re-roll only if the first is 1, 2 or 3 (below the continuation value 3.5). Value:
$$\tfrac{4+5+6}{6}+\tfrac{3}{6}\times3.5=2.5+1.75=\mathbf{4.25}$$
so the game is worth ₹425, better than ₹350 from a single roll. With **two** allowed re-rolls the threshold for the first roll becomes 4.25, so you re-roll on 1-4.

**Fair price.** A stall pays ₹10 × face on one roll: fair entry price ₹35. If it charges ₹40 the house expects ₹5 per play.

**Coupon collector check.** Simulation of 100,000 runs gives 14.68 rolls to see all faces (theory 14.7). The sum is 7 before a 6 in a craps-style race with probability $6/(6+5)=54.5\%$ (7 has 6 ways, 6 has 5).

```python
import numpy as np
rng = np.random.default_rng(0)
def coupon():
    seen, k = set(), 0
    while len(seen) < 6:
        seen.add(rng.integers(1, 7)); k += 1
    return k
print(np.mean([coupon() for _ in range(100000)]))   # ~14.7
```

### In the news
See news box. Expected-value pricing is the same idea as weighing a trial design's expected benefit against its risk.

### Interview angle
> [!question] How it is asked
> "You can roll a die once more after the first roll. What would you pay to play and what is your strategy?"

> [!tip] Strong answer includes
> - Backward induction (compare face with expected continuation value 3.5)
> - The exact answer 4.25 with arithmetic
> - Awareness that EV is not the whole story when stakes are large (risk aversion)
> - Using linearity of expectation rather than enumerating

---
## 8. Gambler's Ruin
> 🟡 Tier 3 · _Key points:_ Random walk with absorbing barriers; k/N for a fair game; negative drift destroys the bankroll

### Definition
A gambler with ₹$k$ bets ₹1 per round, winning with probability $p$ (losing $q=1-p$), and stops on reaching ₹$N$ or ₹0.

$$P(\text{reach }N)=\begin{cases}\dfrac{k}{N}&p=\tfrac12\\[2mm]\dfrac{1-(q/p)^{k}}{1-(q/p)^{N}}&p\ne\tfrac12\end{cases}$$

For a fair game the expected number of rounds is $k(N-k)$. Even a **small house edge** compounds: the longer you play, the closer ruin probability approaches 1. With $p<\tfrac12$ and no upper target, ruin is certain. This is the core logic behind **bankroll management, safety capital and why a business needs reserves** (also a model for a random-demand inventory hitting zero; see [[149 Queueing Theory & Waiting-Line Analysis]]).

### Example
- Fair game, start ₹10, target ₹20: P(reach target) = 10/20 = **50%**, expected duration $10\times10=100$ rounds (simulation: 97.7 rounds for the roulette variant below).
- European roulette bet on red ($p=18/37=0.4865$), start ₹10, target ₹20: $q/p=19/18=1.0556$; $P=\frac{1-1.0556^{10}}{1-1.0556^{20}}=\mathbf{36.8\%}$ (simulation 37.0%).
- American roulette ($p=18/38$): same target gives **25.9%**. Start ₹100, target ₹200: only **0.0027%**, while a fair game would give 50%. The edge, not the bets, destroys you.
- Fair game start ₹5, target ₹20: $5/20=25\%$, duration $5\times15=75$ rounds (simulation 25.3%, 74.8).

```python
def ruin(k, N, p):
    q = 1 - p
    return k / N if p == .5 else (1 - (q/p)**k) / (1 - (q/p)**N)
print(ruin(10, 20, 18/37))     # 0.368
print(ruin(100, 200, 18/38))   # 2.7e-05
```

### In the news
See news box. Sequential (interim-analysis) designs use the same random-walk-with-barriers mathematics, which is why Bayesian and group-sequential rules must control error rates.

### Interview angle
> [!question] How it is asked
> "You have ₹1 lakh and a slightly unfavourable bet. Why do you almost surely go broke if you keep playing?"

> [!tip] Strong answer includes
> - The k/N result for fair bets and the formula for biased bets
> - Why bankroll size matters more than bet cleverness
> - Link to business: cash reserves, safety stock as a buffer against random walk of demand
> - A numeric example and a simulation

---
## 9. The Matching (Derangement) Problem
> 🟡 Tier 3 · _Key points:_ Hat-check problem; P(no match) tends to 1/e; expected matches = 1

### Definition
Randomly assign $n$ items (hats, letters, purchase orders) to $n$ owners. A **derangement** is a permutation with no fixed point:

$$D_n=n!\sum_{i=0}^{n}\frac{(-1)^i}{i!}\qquad P(\text{no match})=\frac{D_n}{n!}\to e^{-1}\approx0.3679$$

The **expected number of matches is exactly 1 for every $n$**, via linearity of expectation: each item matches with probability $1/n$, and there are $n$ items: $n\times\frac1n=1$. The number of matches is approximately Poisson(1), so $P(\text{exactly }k)\approx\frac{e^{-1}}{k!}$ ([[088 Probability Distributions]]). Note that the result barely depends on $n$: for $n=5$ it is already 36.7%.

### Example
| n | Derangements $D_n$ | P(no match) |
|---|---|---|
| 3 | 2 | 33.3% |
| 4 | 9 | 37.5% |
| 5 | 44 | 36.67% |
| 10 | 1,334,961 | 36.788% |

Simulation for $n=10$ over 100,000 shuffles: P(no match) = 0.370, mean matches = 0.998. Business reading: if 10 labelled parcels are put into 10 labelled bins completely at random, expect one correctly placed, and about a 63% chance of at least one right.

```python
import numpy as np
rng = np.random.default_rng(0)
m = np.array([(rng.permutation(10) == np.arange(10)).sum() for _ in range(100000)])
print(np.mean(m == 0), m.mean())   # ~0.368, ~1.0
```

### In the news
See news box. Fixed-point counts are a standard null model when testing whether a prediction or matching system does better than random pairing.

### Interview angle
> [!question] How it is asked
> "10 people throw their hats in a pile and take one at random. What is the expected number who get their own hat? Probability nobody does?"

> [!tip] Strong answer includes
> - Linearity of expectation gives 1 instantly, independent of n
> - Inclusion-exclusion for P(no match), limit 1/e
> - The Poisson(1) shape
> - A realistic analogy (mis-sorted parcels, random roster assignment)

---
## 10. Reliability Systems: Series, Parallel and k-out-of-n
> 🟡 Tier 3 · _Key points:_ Series multiplies, parallel uses the complement, k-of-n via binomial, redundancy placement

### Definition
For independent components with reliability $R_i$ (probability of working over the mission):
- **Series** (all must work): $R_s=\prod R_i$.
- **Parallel** (at least one must work): $R_p=1-\prod(1-R_i)$.
- **k-out-of-n** with equal $R$: $\sum_{j=k}^{n}\binom{n}{j}R^j(1-R)^{n-j}$.
- Redundancy **at the component level** beats redundancy **at the system level**.

This is the maths behind dual sourcing, backup machines and redundant servers; deeper treatment (hazard rates, Weibull, MTBF) is in [[211 Reliability & Survival Analysis]] and [[155 Reliability Engineering & Maintenance Optimisation]], and supply-chain risk framing in [[015 Supply Chain Risk & Resilience]].

### Example
With $R=0.9$ per component:
- Three in series: $0.9^3=\mathbf{0.729}$.
- Three in parallel: $1-0.1^3=\mathbf{0.999}$.
- 2-out-of-3: $3(0.9)^2(0.1)+0.9^3=0.243+0.729=\mathbf{0.972}$.
- 2-out-of-4: $\mathbf{0.9963}$; 3-out-of-5 at $R=0.8$: $\mathbf{0.942}$.
- Two parallel pairs **in series** (component-level redundancy): $(1-0.01)^2=\mathbf{0.9801}$ vs two series pairs **in parallel** (system-level): $1-(1-0.81)^2=\mathbf{0.9639}$.

Long chains are fragile: a 10-step process at 95% per step yields $0.95^{10}=\mathbf{59.9\%}$ end-to-end; a 50-step chain at 99% per step gives $\mathbf{60.5\%}$. This is the same reason a supply chain with many tiers needs buffers.

```python
from scipy.stats import binom
R = 0.9
print(R**3, 1-(1-R)**3, 1-binom.cdf(1, 3, R))   # 0.729 0.999 0.972
print((1-(1-R)**2)**2, 1-(1-R**2)**2)            # 0.9801 0.9639
```

### In the news
See news box. Chained-system reasoning (probabilities multiplying along a pipeline) is also how analysts reason about end-to-end error in multi-step data and decision pipelines.

### Interview angle
> [!question] How it is asked
> "Each of three servers is up 99% of the time. What is the uptime of one that needs any single server vs all three? Where would you add redundancy?"

> [!tip] Strong answer includes
> - Series = product, parallel = complement of product of failures
> - k-of-n by binomial
> - Redundancy at the weakest and at component level
> - Independence caveat: common-cause failures (shared power, one supplier region) break the formula

---
## 11. The Secretary (Optimal Stopping) Problem
> 🟡 Tier 3 · _Key points:_ Reject the first n/e, then take the first candidate better than all so far; success about 37%

### Definition
$n$ candidates arrive in random order; you see each once and must accept or reject on the spot, without recall; you want the single best. **Optimal strategy:** observe (reject) the first $r$ candidates, then accept the first candidate better than everyone seen so far. Success probability:

$$P(r,n)=\frac{r}{n}\sum_{j=r+1}^{n}\frac{1}{j-1}\;\xrightarrow{n\to\infty}\; -x\ln x\quad(x=r/n)$$

maximised at $x=1/e\approx0.368$ with success probability $1/e\approx36.8\%$. For small $n$ the best $r$ is: $n=5\to r=2$ (43.3%), $n=10\to r=3$ (39.9%), $n=20\to r=7$ (38.4%), $n=100\to r=37$ (37.1%). It is a model for hiring, apartment hunting and supplier selection under time pressure ([[150 Decision Analysis & Simulation]]).

### Example
Interviewing 10 applicants in sequence: reject the first 3, then hire the first one who beats all previous. Exact success = 39.87%; a simulation of 100,000 trials gave 39.5%. Compare with picking at random: 10%. For $n=100$, $r=37$ gives 37.1% (simulation 37.2%).

```python
def sec(n, r):
    return 1/n if r == 0 else (r/n) * sum(1/(j-1) for j in range(r+1, n+1))
best = max(range(10), key=lambda r: sec(10, r))
print(best, round(sec(10, best), 4))      # 3 0.3987
```

### In the news
See news box. Optimal-stopping logic also appears in sequential trial designs, where a study stops early when evidence crosses a boundary.

### Interview angle
> [!question] How it is asked
> "You are interviewing 50 vendors one by one and cannot return to a rejected one. What is your rule?"

> [!tip] Strong answer includes
> - Explore-then-exploit: skip about 37% of candidates, then take the first record-breaker
> - Success about 37%, versus 2% (1/50) for a random pick
> - Assumptions: random order, no recall, only relative rank known, goal is the single best
> - Real-world adjustments (partial recall, cost of search, thresholds on absolute quality)

---
## 12. Monte Carlo as a Verification Habit
> 🟡 Tier 3 · _Key points:_ Simulate to check an analytic answer; standard error of a proportion; seed, vectorise, report uncertainty

### Definition
**Monte Carlo** estimates a probability by simulating the experiment many times and taking the observed fraction. Because each trial is a Bernoulli outcome, the standard error is $\sqrt{p(1-p)/N}$. To get about ±1 percentage point at $p\approx0.5$ (95%) needs $N\approx\left(\frac{1.96\times0.5}{0.01}\right)^2\approx9{,}600$ trials; ±0.3 pp needs about 107,000. Always: **fix a seed**, **vectorise** with NumPy, report the estimate with its standard error, and compare with the exact answer. The simulation is also the fallback when no closed form exists ([[150 Decision Analysis & Simulation]], [[205 Sampling Distributions & Estimation]]).

Variance-reduction ideas worth naming: antithetic variates, common random numbers (compare two policies on the same random draws), and importance sampling for rare events.

### Example
Birthday problem, 23 people, 100,000 trials: observed $\hat p=0.5093$; $SE=\sqrt{0.5093\times0.4907/100000}=0.0016$; 95% interval $0.5093\pm0.0031=(0.506,0.512)$, which contains the exact 0.5073. A simulation with only 100 trials would give $SE\approx0.05$, an interval about 20 points wide: too noisy to verify anything.

```python
import numpy as np
rng = np.random.default_rng(7)

def mc(trial, n=100000):
    x = np.array([trial() for _ in range(n)], dtype=float)
    p = x.mean(); se = x.std(ddof=1) / np.sqrt(n)
    return p, se, (p - 1.96*se, p + 1.96*se)

print(mc(lambda: len(set(rng.integers(0, 365, 23))) < 23))
```

### In the news
See news box. Bayesian trial designs are typically checked by simulating their error rates and power, so this habit is a working skill and not only a classroom trick.

### Interview angle
> [!question] How it is asked
> "How would you check your answer by simulation, and how many runs do you need?"

> [!tip] Strong answer includes
> - Pseudocode: loop, indicator, average
> - Standard error and how it shrinks with $1/\sqrt N$
> - Seed for reproducibility, vectorised code
> - Using simulation for problems with no closed form (inventory with random lead time, queues)

---
## 13. ⭐ Advanced: First-Step Analysis, Indicators and Markov Chains
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Three methods solve most "hard" puzzles quickly.

1. **Indicator variables and linearity.** To find an expected count (matches, distinct birthdays, runs), write $X=\sum I_k$ and use $E[X]=\sum P(I_k=1)$, no independence needed. Example: expected number of distinct values in $n$ draws from $m$ equally likely values is $m\left[1-\left(1-\tfrac1m\right)^n\right]$; for 23 draws from 365 days this is **22.32** distinct birthdays.
2. **First-step analysis.** Condition on the first move and write a linear equation for the unknown expectation or probability (Section 6).
3. **Markov chains.** When the future depends only on the current state, put transition probabilities in a matrix; absorbing chains give ruin and waiting-time answers ([[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]] for a different Markov-flavoured use, and [[149 Queueing Theory & Waiting-Line Analysis]]).

### Example
A machine is Up or Down each day. If Up it stays Up with probability 0.9; if Down it is repaired (becomes Up) with probability 0.6. Long-run Up fraction $\pi$ solves $\pi=0.9\pi+0.6(1-\pi)\Rightarrow0.7\pi=0.6\Rightarrow\pi=\mathbf{0.857}$ (about 85.7% availability). Expected days to the first breakdown from Up: $1/0.1=10$; expected repair time $1/0.6=1.67$ days; these give the same availability $10/(10+1.67)=85.7\%$.

```python
import numpy as np
P = np.array([[0.9, 0.1], [0.6, 0.4]])   # states: Up, Down
w, v = np.linalg.eig(P.T)
pi = np.real(v[:, np.argmax(np.real(w))]); print(pi / pi.sum())   # [0.857 0.143]
print(365 * (1 - (1 - 1/365)**23))                                  # 22.32
```

### In the news
See news box. Markov and Bayesian models are the mathematical core of the posterior-updating machinery regulators are now accepting.

### Interview angle
> [!question] How it is asked
> "A machine is up 90% of days and the repair crew fixes it the next day 60% of the time. What is its long-run availability?"

> [!tip] Strong answer includes
> - Recognise a two-state Markov chain and write the balance equation
> - Cross-check with MTBF/(MTBF + MTTR)
> - Mention the Markov assumption (memoryless) and when it fails (wear-out)
> - Link to [[215 Statistics Interview Question Bank & Numericals]] for follow-ups
