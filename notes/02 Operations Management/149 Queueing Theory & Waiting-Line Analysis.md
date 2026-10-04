---
tags: [operations-management, tier1]
area: Operations Management
topic: "Queueing Theory & Waiting-Line Analysis"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Queueing Theory & Waiting-Line Analysis

⬅ [[148 Operations Research - Network Models & Integer Programming]] · [[_Index - Operations Management|Operations Management]] · [[150 Decision Analysis & Simulation]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Anatomy of a Queueing System and Kendall Notation]]
2. [[#2. Little's Law and Core Performance Measures]]
3. [[#3. M/M/1 Queue]]
4. [[#4. M/M/c and Erlang C]]
5. [[#5. Staffing for a Service Level and the Square-Root Rule]]
6. [[#6. The Pooling Effect: One Queue vs Many]]
7. [[#7. The Hockey-Stick Curve, Variability and Kingman's Formula]]
8. [[#8. M/G/1 and the Pollaczek–Khinchine Formula]]
9. [[#9. Finite-Source Queues (Machine Repair Model)]]
10. [[#10. Priority Queues and Triage]]
11. [[#11. Simulation of Queues]]
12. [[#12. The Psychology of Waiting and Design Levers]]
13. [[#13. ⭐ Advanced: Erlang B, Abandonment, Queueing Networks and Approximations]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): England's A&E queue shows what happens when utilisation stays too high
> **NHS England A&E, March 2026.** NHS England's statistical commentary reports that 77.1% of A&E patients were admitted, transferred or discharged within four hours in March 2026, against a long-standing operational standard of 95% and an interim goal of 78% by March 2026 set in the June 2025 Urgent and Emergency Care Plan; 46,665 patients waited more than 12 hours from decision to admit to actual admission. ([NHS England statistical commentary, March 2026](https://www.england.nhs.uk/statistics/wp-content/uploads/sites/2/2026/04/Statistical-commentary-March-2026-G4dal2.pdf); [The King's Fund](https://www.kingsfund.org.uk/insight-and-analysis/data-and-charts/accident-emergency-waiting-times))
>
> **Why occupancy matters.** The King's Fund notes that hospitals, particularly in winter, routinely run bed occupancy above 92%, the level at which the Department of Health and Social Care suggests hospitals will struggle to cope with emergency admissions; blocked beds create "trolley waits" for patients in A&E. Queueing theory explains why: delay explodes as utilisation nears 100%. ([The King's Fund](https://www.kingsfund.org.uk/insight-and-analysis/long-reads/whats-going-on-with-ae-waiting-times))
>
> **Live wait-time estimates at Delhi airport.** Delhi Airport publishes security-check wait times that are collected by sensors and cameras at checkpoints and updated every few minutes, with the caveat that the estimates are indicative only: a queue-measurement system built to manage and announce waits. ([Delhi Airport](https://www.newdelhiairport.in/wait-time/departure/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Anatomy of a Queueing System and Kendall Notation
> 🔴 Tier 1 · _Key points:_ Arrival process, service process, servers, discipline; A/S/c/K/N

### Definition
Every waiting line has: an **arrival process** (rate $\lambda$, inter-arrival distribution), a **service process** (rate $\mu$ per server, so mean service time $1/\mu$), $c$ **servers**, a **queue discipline** (FCFS, priority, SIRO, LIFO), and a **capacity** limit and **source population** (infinite or finite). Behavioural features: **balking** (not joining), **reneging/abandonment** (leaving), **jockeying** (switching lines).

**Kendall notation** $A/S/c/K/N/D$: $A$ = arrival distribution, $S$ = service distribution, $c$ = servers, $K$ = system capacity (default ∞), $N$ = population (default ∞), $D$ = discipline (default FCFS). Symbols: **M** = Markovian (Poisson arrivals; exponential service), **D** = deterministic, **G** = general, $E_k$ = Erlang-$k$.

| Notation | Meaning | Typical use |
|---|---|---|
| M/M/1 | Poisson arrivals, exponential service, one server | Single counter, single machine |
| M/M/c | $c$ identical servers, one shared queue | Call centre, bank with a token system |
| M/G/1 | General service-time distribution | Repair shop, ER doctor (service variability matters) |
| M/M/c/c | No waiting room (Erlang B) | Telephone trunk lines, parking |
| M/M/1//N | Finite population | Machine-repair (operators and machines) |

**Stability condition:** utilisation $\rho=\lambda/(c\mu)<1$. If $\rho\ge1$ the queue grows without bound. The exponential/Poisson assumptions come from probability ([[087 Probability Fundamentals]], [[088 Probability Distributions]]).

### Example
Classify: "A repair shop receives about 8 breakdowns an hour (random), one mechanic, repair times vary from 2 minutes to 40 minutes with mean 6 minutes": M/G/1 with $\lambda=8$, $\mu=10$ per hour, $\rho=0.8$. "A call centre with 11 agents and no limit on the number of waiting callers": M/M/11. "Five machines served by one repair crew": M/M/1//5.

### In the news
See news box. A&E is a multi-server queue with priority classes, blocked downstream beds and abandonment (patients who leave without being seen): a system whose utilisation is policy-driven by bed occupancy.

### Interview angle
> [!question] How it is asked
> "Describe M/M/1 and M/M/c. What do the letters mean, and when do the formulas fail?"

> [!tip] Strong answer includes
> - Decode the notation and give a real example for each
> - State the stability condition $\rho<1$
> - Formulas fail when arrivals are not Poisson (batches, schedules), service times are not exponential (use M/G/1), or there is abandonment and priority
> - Mention that you would measure λ and service-time distribution from data before choosing a model

---
## 2. Little's Law and Core Performance Measures
> 🔴 Tier 1 · _Key points:_ L = λW holds for any stable system; the four measures

### Definition
**Little's Law** (1961): for any stable system in steady state, long-run average number in system equals arrival rate times average time in system:

$$L=\lambda W\qquad L_q=\lambda W_q\qquad W=W_q+\tfrac{1}{\mu}\qquad L=L_q+\tfrac{\lambda}{\mu}$$

It needs no assumption about the arrival or service distribution or the discipline. Measures to report: **utilisation** $\rho$; **$L_q$** (average number waiting); **$L$** (number in system); **$W_q$** (average wait before service); **$W$** (time in system); **$P_0$** (probability the system is empty); **P(wait > t)**; and **service level** (share of customers served within a target). The average number of busy servers is $\lambda/\mu$ (the **offered load** in Erlangs).

### Example
A store has on average 12 customers inside, and customers arrive at 30 per hour. Time in store: $W=L/\lambda=12/30=0.4$ hours = 24 minutes. The same law links inventory to flow time in operations ([[003 Inventory Management]]: $I=\text{throughput}\times\text{flow time}$) and WIP in lean systems ([[007 Lean Manufacturing]]).

### In the news
See news box. Little's Law applied to A&E: if arrivals are roughly fixed and boarded patients stay longer because there are no free beds, the number of people in the department rises in proportion to their time there: 12-hour waits of tens of thousands per month are the law at work.

### Interview angle
> [!question] How it is asked
> "A hospital ward has 40 patients on average and 10 admissions a day. What is the average length of stay?"

> [!tip] Strong answer includes
> - $W=L/\lambda=40/10=4$ days; units must match (per day)
> - State that the law is distribution-free and holds for systems, subsystems and queues alone
> - Use it as a sanity check on any simulation or dashboard
> - Link to inventory and WIP: lead time = WIP ÷ throughput

---
## 3. M/M/1 Queue
> 🔴 Tier 1 · _Key points:_ ρ = λ/μ; L = ρ/(1−ρ); Wq = ρ/(μ−λ)

### Definition
Single server, Poisson arrivals ($\lambda$), exponential service ($\mu$), infinite FCFS queue, $\rho=\lambda/\mu<1$:

$$P_n=(1-\rho)\rho^n,\quad L=\frac{\rho}{1-\rho},\quad L_q=\frac{\rho^2}{1-\rho},\quad W=\frac{1}{\mu-\lambda},\quad W_q=\frac{\rho}{\mu-\lambda}$$

Also $P(W_q>t)=\rho e^{-(\mu-\lambda)t}$ (for $t\ge0$) and $P(\text{system empty})=1-\rho$.

### Example
Bank counter: $\lambda=8$ customers/hour, $\mu=10$ per hour. $\rho=0.8$; $L=0.8/0.2=4$; $L_q=0.64/0.2=3.2$; $W=1/(10-8)=0.5$ h = **30 min**; $W_q=0.8/2=0.4$ h = **24 min** (check $L_q=\lambda W_q=8\times0.4=3.2$ ✓). Probability a customer waits more than 10 minutes: $0.8e^{-2/6}=0.573$. Probability the server is idle: 20%. A server that looks "20% idle" still produces 24-minute waits, which is why managers must judge utilisation by waiting, not by idle time. If arrivals rise 12.5% to 9/hour: $\rho=0.9$, $W_q=0.9/(10-9)=0.9$ h = **54 min**: a 12.5% rise in demand more than doubles the wait.

### In the news
See news box. Delhi airport's wait estimate is a measured $W_q$; the NHS situation is the same arithmetic with ρ near 1: small changes in load or length of stay create large changes in waits.

### Interview angle
> [!question] How it is asked
> "Customers arrive at 8 an hour and a clerk serves 10 an hour. Why is there still a long queue, and what happens if demand grows 10%?"

> [!tip] Strong answer includes
> - Compute ρ = 0.8, $W_q=24$ min; explain randomness as the cause of waiting even with spare capacity
> - Demand +10% (8.8/h): ρ = 0.88, $W_q=0.88/1.2=0.733$ h ≈ 44 min (+83%)
> - Offer levers: raise μ (faster service, parallel prep), add a server, smooth arrivals (appointments)
> - Mention the nonlinear (hockey-stick) relation, not a linear one

---
## 4. M/M/c and Erlang C
> 🔴 Tier 1 · _Key points:_ Offered load a = λ/μ; probability of waiting (Erlang C); Wq = Pw/(cμ−λ)

### Definition
$c$ identical servers share one queue. Offered load $a=\lambda/\mu$ (Erlangs); utilisation $\rho=a/c<1$. The **Erlang C** formula gives the probability that an arriving customer must wait:

$$P_w=C(c,a)=\frac{\dfrac{a^c}{c!}\cdot\dfrac{c}{c-a}}{\displaystyle\sum_{k=0}^{c-1}\frac{a^k}{k!}+\frac{a^c}{c!}\cdot\frac{c}{c-a}}$$

$$W_q=\frac{P_w}{c\mu-\lambda},\quad L_q=\lambda W_q,\quad W=W_q+\frac1\mu,\quad L=L_q+a$$

**Service level** (share answered within $t$): $SL(t)=1-P_w\,e^{-(c\mu-\lambda)t}$. Because the wait, given that one must wait, is exponential with rate $c\mu-\lambda$, average wait *of those who wait* is $1/(c\mu-\lambda)$.

### Example
Call centre: 120 calls/hour, average handling time 4 minutes ($\mu=15$ calls/hour/agent), so $a=8$ Erlangs. With **10 agents**: $\rho=0.8$, $P_w=0.409$, $W_q=0.409/(150-120)=0.01364$ h = **49 s**, $L_q=1.64$, 20-second service level $=1-0.409e^{-30\times(20/3600)}=65.4\%$. Compare **11 agents**: $\rho=0.727$, $P_w=0.245$, $W_q=19.6$ s, SL(20 s) = **80.9%**. So one extra agent (10%) lifts the 20-second service level from 65% to 81% and cuts the average wait by 60% (all numbers computed in Python).

### In the news
See news box. Emergency departments are M/M/c-like systems where the "servers" are treatment bays and clinicians; the $\rho$ near 0.9+ regime is where waits reach hours.

### Interview angle
> [!question] How it is asked
> "A call centre with 120 calls an hour and 4-minute calls wants 80% answered in 20 seconds. How many agents?"

> [!tip] Strong answer includes
> - Offered load = 120 × 4/60 = 8 Erlangs; start at c = 9 and iterate Erlang C (11 agents gives 81%)
> - Show shrinkage: scheduled headcount ≈ agents ÷ (1 − shrinkage, say 30%)
> - State the sensitivity: going from 10 to 11 agents changes service from 65% to 81%
> - Note limitations: no abandonment in Erlang C (use Erlang A if callers hang up)

---
## 5. Staffing for a Service Level and the Square-Root Rule
> 🔴 Tier 1 · _Key points:_ Minimum c meeting SL; offered load + β√a; shrinkage; occupancy vs service

### Definition
**Capacity planning for queues:** choose the smallest $c$ such that the service-level or waiting-time target is met. Rule of thumb for large systems, the **square-root staffing rule** (Halfin–Whitt regime):

$$c\approx a+\beta\sqrt{a}$$

where $\beta$ (the "safety staffing" factor, around 0.5 to 2) controls quality: larger $\beta$ means better service. Implication: **economies of scale**: as offered load grows, you need less *proportional* excess capacity, so big pooled centres run at higher occupancy for the same service level. Practical steps: forecast arrivals by 15–30 minute interval; choose AHT; compute $c$ per interval; add **shrinkage** (breaks, training, leave, absenteeism) to get rostered headcount.

### Example
Same call centre ($a=8$): the table gives service level for 20 seconds as agents vary (computed):

| Agents $c$ | Occupancy | $P_w$ | Avg wait | SL(20 s) |
|---|---|---|---|---|
| 9 | 88.9% | 65.3% | 157 s | 39.9% |
| 10 | 80.0% | 40.9% | 49 s | 65.4% |
| **11** | 72.7% | 24.5% | 20 s | **80.9%** |
| 12 | 66.7% | 14.0% | 8 s | 90.0% |
| 13 | 61.5% | 7.6% | 4 s | 95.0% |

Square-root rule with $\beta=1$: $c\approx8+\sqrt8=10.8\to11$, matching. Scaling up: for $a=80$ Erlangs (ten times the load), $\beta=1$ gives $c\approx80+8.9\approx89$, occupancy 90%, and Erlang C (with the same 4-minute calls) confirms a 20-second service level of about **89%**: the larger pooled centre beats the small centre's 81% while running at 90% occupancy instead of 73%. Rostering: with 30% shrinkage, 11 agents on the phones need about $11/0.7\approx16$ rostered.

### In the news
See news box. Delhi airport's use of live waiting-time data is the demand-side of the same planning: staffing lanes in line with measured waits. Staffing to a service level, not to an average load, is the key discipline behind the NHS 4-hour standard.

### Interview angle
> [!question] How it is asked
> "How would you decide the number of check-in counters or support agents for each hour of the day?"

> [!tip] Strong answer includes
> - Forecast arrivals per interval; estimate service time; compute offered load
> - Find the minimum $c$ for the service target via Erlang C or the square-root rule
> - Add shrinkage and a buffer for forecast error; compare against cost per agent-hour
> - Mention cross-training and flexible/floating staff as the cheaper way to buffer variability

---
## 6. The Pooling Effect: One Queue vs Many
> 🔴 Tier 1 · _Key points:_ Single shared queue beats parallel queues; but fast single server also wins

### Definition
**Pooling** combines separate demand streams or servers into one shared system. With the same total capacity, a **single queue feeding $c$ servers** (M/M/c) has much lower waiting than $c$ separate M/M/1 queues, because no server idles while customers wait elsewhere and the line cannot be "bad luck" in one lane. The same logic underlies safety-stock pooling in supply chains ([[003 Inventory Management]], [[113 Network Design & Facility Location Modelling]]) and cross-trained labour pools.

### Example
Two counters, each serving $\mu=5$ customers/hour. Total arrival rate 8/hour.
- **Separate lines** (4/hour each, each M/M/1): $\rho=0.8$, $W_q=0.8/(5-4)=0.8$ h = **48 min**; $W=1$ h.
- **One shared line (M/M/2)**, $a=1.6$, $\rho=0.8$: $P_w=0.711$, $W_q=0.711/(10-8)=0.3556$ h = **21.3 min**; $W=0.556$ h = 33.3 min.
Pooling cuts the wait in queue by **56%** at identical utilisation and total capacity.
- **Counter-intuition:** one *fast* server at $\mu=10$ with $\lambda=8$: $W_q=0.4$ h = 24 min but $W=0.5$ h = 30 min, which beats pooled slow servers on total time (33.3 min) because the service time itself is shorter, though $W_q$ is slightly higher (24 vs 21.3 min). Pooling reduces waiting, not service time.

**Caveats:** pooling fails when the streams need different skills, the pooled system adds travel/handover or switching costs, or customers value continuity (relationship banking, personal doctors). Real-world cases: single "snake" queues in banks and airports; shared call-centre routing; pooled ICU beds across wards.

### In the news
See news box. England's bed occupancy problem is partly a pooling problem: ring-fencing capacity by ward or specialty prevents the system from using spare capacity where the queue is, so pooled "flow" beds and discharge lounges are standard levers.

### Interview angle
> [!question] How it is asked
> "A bank has three tellers, each with their own line. A consultant suggests one common line. Why, and what could go wrong?"

> [!tip] Strong answer includes
> - Same capacity, same utilisation, but less variance: average wait drops (numbers: 48 → 21 min in a two-teller example)
> - Fairness (FCFS) and psychological benefits; remove the "wrong lane" regret
> - Caveats: specialisation, space, handover costs, jockeying already approximating pooling
> - Pooling reduces waiting, not service time: speed-up and pooling are complements

---
## 7. The Hockey-Stick Curve, Variability and Kingman's Formula
> 🔴 Tier 1 · _Key points:_ Waiting explodes as ρ→1; variability multiplies it

### Definition
In M/M/1, $W_q/E[S]=\rho/(1-\rho)$: waiting time in units of mean service times. It is convex and rises steeply above ~80–85% utilisation. **Kingman's approximation** (VUT equation) for a single server with general arrival and service variability:

$$W_q\approx\underbrace{\frac{c_a^2+c_s^2}{2}}_{V\ (\text{variability})}\times\underbrace{\frac{\rho}{1-\rho}}_{U\ (\text{utilisation})}\times\underbrace{E[S]}_{T\ (\text{time})}$$

where $c_a$ and $c_s$ are the coefficients of variation of inter-arrival and service times (for M/M/1 both are 1, so $V=1$). Levers on waiting: reduce **utilisation**, reduce **variability** (standard work, appointments, smoothing arrivals), reduce **mean service time**.

### Example
$W_q/E[S]$ in M/M/1 by utilisation (computed):

| ρ | 50% | 70% | 80% | 90% | 95% | 99% |
|---|---|---|---|---|---|---|
| $W_q/E[S]$ | 1 | 2.3 | 4 | 9 | 19 | 99 |

With a 6-minute service, waits at 50%, 80%, 90%, 95% are 6, 24, 54 and 114 minutes. **Variability:** with $c_a=1$ and $c_s^2=0.25$ (very consistent service), at ρ = 0.9 and $E[S]=6$: $W_q\approx\frac{1+0.25}{2}\times9\times6=33.75$ min, versus 54 min for $c_s^2=1$: cutting service variability by 75% cuts waiting by 37.5%, with no new capacity. Appointment systems drive $c_a$ toward 0, the biggest lever of all.

### In the news
See news box. A hospital at 92%+ bed occupancy sits on the steep part of the curve: a few extra emergency admissions or a few more delayed discharges cause disproportionate increases in waits. The same reasoning applies to a factory at 95% utilisation ([[018 Capacity Management & OEE]]) or a warehouse in peak season.

### Interview angle
> [!question] How it is asked
> "Why shouldn't we run our shared service centre at 95% utilisation, and what would you target?"

> [!tip] Strong answer includes
> - Convex waiting curve: at 95% the queue is about 19 service times, versus 4 at 80%
> - Variability matters as much as utilisation (Kingman: V × U × T)
> - Targets: 75–85% for high-variability service systems with significant waiting cost, higher for pooled or predictable systems
> - Alternatives to adding servers: smoothing demand, reducing variability, flexible capacity

---
## 8. M/G/1 and the Pollaczek–Khinchine Formula
> 🔴 Tier 1 · _Key points:_ Service-time variance inflates waiting; deterministic service halves Wq

### Definition
Poisson arrivals ($\lambda$), **general** service time $S$ with mean $E[S]=1/\mu$ and variance $\sigma^2$, one server, $\rho=\lambda E[S]<1$. The **Pollaczek–Khinchine (P–K) formula**:

$$L_q=\frac{\lambda^2\sigma^2+\rho^2}{2(1-\rho)},\qquad W_q=\frac{L_q}{\lambda}=\frac{\lambda\,E[S^2]}{2(1-\rho)}=\frac{1+c_s^2}{2}\cdot\frac{\rho}{\mu(1-\rho)}$$

with $c_s^2=\sigma^2/E[S]^2$ (squared coefficient of variation), $E[S^2]=\sigma^2+E[S]^2$. $W=W_q+E[S]$, $L=\lambda W$. For exponential service $c_s^2=1$ (M/M/1 formulas); for deterministic service $c_s^2=0$ (**M/D/1**), waiting is exactly **half** of M/M/1.

### Example
$\lambda=8$/hour, $E[S]=6$ minutes (0.1 h), $\rho=0.8$ (computed):

| Service-time pattern | $c_s^2$ | $W_q$ | $L_q$ |
|---|---|---|---|
| Deterministic (M/D/1) | 0 | 12 min | 1.6 |
| Exponential (M/M/1) | 1 | 24 min | 3.2 |
| Highly variable ($c_s=2$, $c_s^2=4$) | 4 | 60 min | 8.0 |

The same average service time and utilisation produce a five-fold range of waits. A repair shop whose job times range from 2 to 40 minutes ($c_s$ above 1) therefore suffers far longer waits than a standardised process. Levers: standard work, triage into fast and slow lanes, pre-processing (forms completed before arrival), splitting big jobs.

### In the news
See news box. Clinical complexity makes A&E service times highly variable (a sprained ankle versus a stroke): a high $c_s^2$ means the same occupancy yields much longer waits, which is why streaming low-acuity patients into separate lanes (fast-track, urgent treatment centres) cuts overall waiting.

### Interview angle
> [!question] How it is asked
> "Two service desks have the same average handling time and demand. One has very consistent handling times, the other has high variance. Which has the longer queue and by how much?"

> [!tip] Strong answer includes
> - P–K formula: waiting scales with $(1+c_s^2)/2$, so higher variance means longer waits; deterministic is half of M/M/1, $c_s=2$ is 2.5 times M/M/1
> - Numerical illustration with the same ρ
> - Operational levers: standardise, separate fast and slow jobs, reduce rework
> - Be ready to name the assumption (Poisson arrivals)

---
## 9. Finite-Source Queues (Machine Repair Model)
> 🔴 Tier 1 · _Key points:_ Arrivals depend on how many are up; M/M/1//N; machine downtime

### Definition
When the calling population is small, arrivals depend on the state: each of $N$ units in operation fails at rate $\lambda$ (per unit); the repair facility with $c$ servers repairs at rate $\mu$. For one repairer (M/M/1//N), with $\rho=\lambda/\mu$:

$$P_0=\left[\sum_{n=0}^{N}\frac{N!}{(N-n)!}\rho^n\right]^{-1},\quad P_n=\frac{N!}{(N-n)!}\rho^nP_0,\quad L=N-\frac{1-P_0}{\rho},\quad \lambda_{\text{eff}}=\lambda(N-L)=\mu(1-P_0)$$

$W=L/\lambda_{\text{eff}}$ (time from failure to repair completion); $L_q=L-(1-P_0)$; $W_q=L_q/\lambda_{\text{eff}}$. Applications: machine downtime and maintenance crews ([[022 Maintenance Management (TPM-RCM)]], [[155 Reliability Engineering & Maintenance Optimisation]]), IT desks for a limited fleet, forklift pools. The question: how many repairers/spares minimise downtime plus labour cost?

### Example
Five machines each fail on average once per 4 operating hours ($\lambda=0.25$/hour); one technician repairs at $\mu=1$ per hour ($\rho=0.25$). State probabilities $P_0..P_5$ = 0.199, 0.249, 0.249, 0.187, 0.093, 0.023 (sum 1). Technician utilisation $1-P_0=\mathbf{80.1\%}$; expected machines down $L=1.80$ (so about **3.2 machines running** on average); effective failure rate $\lambda_{\text{eff}}=0.80$/hour; time from failure to restart $W=1.80/0.80=2.24$ h, of which waiting for the technician $W_q=1.24$ h. Adding a second technician (M/M/2//5) cuts the waiting for repair, at the price of lower utilisation; compare the extra labour cost with the production value of each additional running machine-hour. (Computed in Python.)

### In the news
See news box. Where the "population" is bounded (a hospital's limited ventilators, a fleet of ambulances), the infinite-population formulas overstate arrivals; finite-source models are used for ambulance fleets and equipment pools.

### Interview angle
> [!question] How it is asked
> "A plant has 5 CNC machines and one maintenance technician. How do you decide whether to hire a second one?"

> [!tip] Strong answer includes
> - Use a finite-source model (or simulation); measure failure and repair rates from CMMS data
> - Compute expected machines down and lost production value per hour vs the technician's cost
> - Note the alternative levers: faster repair (spares, tooling), preventive maintenance, spare machine
> - Warn that infinite-source M/M/1 over-predicts congestion for small populations

---
## 10. Priority Queues and Triage
> 🔴 Tier 1 · _Key points:_ Non-preemptive vs preemptive; conservation law; protect urgent, delay non-urgent

### Definition
Customers are served by **class priority** instead of arrival order. **Non-preemptive priority:** a job in service is never interrupted. **Preemptive-resume:** a higher class interrupts service and the interrupted job resumes later. For non-preemptive M/G/1 with classes $1..K$ (1 = highest), service moments $E[S_i^2]$, $\rho_i=\lambda_iE[S_i]$ and cumulative load $\sigma_k=\sum_{i\le k}\rho_i$, **Cobham's formula**:

$$W_q^{(k)}=\frac{W_0}{(1-\sigma_{k-1})(1-\sigma_k)},\qquad W_0=\sum_{i}\frac{\lambda_iE[S_i^2]}{2}$$

($W_0$ is the mean residual work found by an arrival.) **Conservation law:** a work-conserving discipline changes *who* waits, but the weighted-average wait (weighted by load) is the same as under FCFS when service times are equally distributed across classes.

### Example
ER triage: urgent patients $\lambda_1=2$/hour, non-urgent $\lambda_2=6$/hour, one doctor, exponential service with mean 6 minutes ($\mu=10$/hour) for both: $\rho_1=0.2$, $\rho_2=0.6$, total $\rho=0.8$.
- **FCFS:** $W_q=0.8/(10-8)=0.4$ h = **24 min** for everyone.
- **Non-preemptive priority:** $W_0=\dfrac{8\times(2/100)}{2}=0.08$ h. Urgent: $W_q^{(1)}=0.08/(1-0.2)=0.1$ h = **6 min**. Non-urgent: $W_q^{(2)}=0.08/[(1-0.2)(1-0.8)]=0.5$ h = **30 min**. Load-weighted average: $(2\times6+6\times30)/8=24$ min (the conservation law).
Triage cuts the urgent wait by 75% at a 25% longer wait for the non-urgent: acceptable when urgency reflects clinical risk. Danger: if the high class has most of the load, the low class **starves** (as $\sigma\to1$, $W_q^{(2)}\to\infty$), so add aging or a maximum-wait escalation.

### In the news
See news box. NHS four-hour and 12-hour waiting metrics are exactly the blend of urgency classes and waiting-time targets; "breaches" cluster in the low-priority classes when overall utilisation is high.

### Interview angle
> [!question] How it is asked
> "How would you prioritise customers in a queue, and what's the downside?"

> [!tip] Strong answer includes
> - Priority by urgency/value (triage, SLAs), or shortest-job-first to cut average wait
> - Quantify: urgent 6 min versus FCFS 24 min; non-urgent 30 min; conservation law
> - Starvation risk: add aging, caps, or separate lanes (fast-track)
> - Preemption costs: set-ups and loss of work; fairness and perception issues

---
## 11. Simulation of Queues
> 🔴 Tier 1 · _Key points:_ Lindley recursion; discrete-event simulation; when formulas break

### Definition
Simulation estimates queue performance when formulas do not apply (non-Poisson arrivals, abandonment, priorities, time-varying demand, networks of queues, blocking). **Single-server FCFS recursion (Lindley):**

$$W_{n+1}=\max\{0,\ W_n+S_n-A_{n+1}\}$$

with $W_n$ the wait of customer $n$, $S_n$ its service time and $A_{n+1}$ the inter-arrival time to the next. **Discrete-event simulation (DES)** keeps an event list (arrivals, service completions), advances the clock to the next event, updates state and statistics ([[150 Decision Analysis & Simulation]] covers Monte Carlo and simulation steps; [[068 Operations-Specific Python (PuLP, SimPy)]] for SimPy). Steps: model → input distributions fitted to data → warm-up deletion → multiple replications → confidence intervals → validation against theory/history.

### Example
**Hand simulation** (single server, minutes): inter-arrival times 2, 1, 4, 3, 1, 5, 2, 3; service times 3, 4, 2, 3, 4, 2, 3, 2.

| Cust | Arrives | Service | Starts | Wait | Departs |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 2 | 0 | 5 |
| 2 | 3 | 4 | 5 | 2 | 9 |
| 3 | 7 | 2 | 9 | 2 | 11 |
| 4 | 10 | 3 | 11 | 1 | 14 |
| 5 | 11 | 4 | 14 | 3 | 18 |
| 6 | 16 | 2 | 18 | 2 | 20 |
| 7 | 18 | 3 | 20 | 2 | 23 |
| 8 | 21 | 2 | 23 | 2 | 25 |

Total wait 14, **average wait 1.75 min**; server busy 23 of 25 minutes (92%). Eight customers are too few to trust: replicate.

**Computer check** (Python; 400,000 customers, 10,000 discarded as warm-up, seed 42): $\lambda=8$, $\mu=10$ per hour gave a mean wait of **23.8 minutes** versus the analytical 24 minutes, confirming the model and the recursion. Use simulation for the situations the formulas do not cover, and use the formulas as a validation test for the simulator.

### In the news
See news box. Hospitals and airports use simulation to test staffing and layout changes before implementing; data from sensors (as at Delhi airport) feed arrival-rate and service-time distributions.

### Interview angle
> [!question] How it is asked
> "How would you simulate a queue and know it is correct?"

> [!tip] Strong answer includes
> - Inputs from data; event-driven logic or Lindley recursion; run length, warm-up, replications
> - Validate against a case with a known answer (M/M/1: $W_q=\rho/(\mu-\lambda)$) and against history
> - Report confidence intervals, not point estimates; run sensitivity on demand
> - Use for what-if scenarios (add a server, split queues, change schedules)

---
## 12. The Psychology of Waiting and Design Levers
> 🔴 Tier 1 · _Key points:_ Perceived vs actual wait; Maister's principles; virtual queues

### Definition
Satisfaction depends on **perceived** wait, not just actual wait. Maister's classic principles (1985): **occupied time feels shorter than unoccupied time**; **pre-process waits feel longer than in-process waits**; **anxiety makes waits seem longer**; **uncertain waits feel longer than known, finite waits**; **unexplained waits feel longer than explained**; **unfair waits (queue jumping) feel longer**; **solo waits feel longer than group waits**; and people will wait longer for services they value more. Practical levers: give **information** (estimated wait displays, "you are number 5"), **occupy** customers (mirrors, content, forms), **start service early** (menus, triage nurse), **provide fairness** (single FCFS line, tokens), **virtual queues** (callback, app tokens, appointment slots), **redistribute demand** (off-peak pricing, pre-booking).

Operational levers beside psychology: reduce arrival variability, reduce service time and variability, pool servers, add flexible capacity at peaks, offer self-service (UPI, kiosks, DigiYatra-type automation).

### Example
Hypothetical numeric case: in the 10-agent call centre of sub-topic 4, about 41% of callers wait, and *given* that they wait the mean wait is $1/(c\mu-\lambda)=1/30$ hour = 2 minutes, with a long tail (10% of waiters wait more than about 4.6 minutes). Playing an honest "your estimated wait is 2 minutes" message removes uncertainty; offering a callback to callers who would otherwise wait removes the unoccupied time altogether and also shortens the live queue for those who stay. Neither changes the agents' workload; both change how the wait is experienced. (The 4.6-minute figure is $\ln(10)/30$ hours.)

### In the news
See news box. A live wait-time display, as at Delhi airport, addresses two of Maister's principles at once: it reduces uncertainty and shows fairness; NHS-style targets on four-hour and 12-hour waits try to cap the worst experiences, not only the average.

### Interview angle
> [!question] How it is asked
> "A restaurant, clinic or e-commerce help desk has long waits and no budget for more staff. What do you do?"

> [!tip] Strong answer includes
> - Distinguish actual and perceived wait; tell customers the wait and keep them occupied
> - Cut variability: appointments, triage, standard work, pre-processing
> - Pool or flex capacity at peak; use virtual queues and callbacks
> - Measure: abandonment rate, service level, percentiles, not just averages

---
## 13. ⭐ Advanced: Erlang B, Abandonment, Queueing Networks and Approximations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Erlang B (M/M/c/c, blocked calls cleared):** probability that all $c$ servers are busy and an arrival is lost: $B(c,a)=\dfrac{a^c/c!}{\sum_{k=0}^{c}a^k/k!}$, computed by recursion $B(0)=1$, $B(k)=\dfrac{aB(k-1)}{k+aB(k-1)}$. Used for trunk lines, parking, bed or ventilator capacity without waiting rooms. **Erlang C relation:** $C=\dfrac{B}{1-\rho(1-B)}$.
- **Erlang A (M/M/c+M):** adds abandonment with rate $\theta$ per waiting customer; more realistic for call centres since impatient customers leave.
- **Jackson networks:** a network of M/M/c nodes with Poisson external arrivals and probabilistic routing decomposes into independent M/M/c queues (product-form solution); the building block for analysing hospital pathways or multi-stage service flows.
- **Heavy-traffic and fluid approximations**, G/G/c (Allen–Cunneen) for non-Poisson systems; **time-varying arrivals**: use the pointwise stationary approximation or simulation.
- **Priority with preemption, vacations, batch arrivals** extend the models. **Optimising $c$:** minimise $c\cdot C_s + \lambda W_q\cdot C_w$ (server cost plus waiting cost).

### Example
**Erlang B:** 8 Erlangs offered to 10 lines: $B=12.2\%$ of calls blocked; with 12 lines $B=5.1\%$. **Optimal servers:** ER with $\lambda=5$ patients/hour and 90-minute treatment ($a=7.5$): waiting before a bay is available by number of bays, from Erlang C: 8 bays 145 min, **9 bays 30 min**, 10 bays 11 min, 11 bays 4.5 min, 12 bays 1.9 min. If waiting costs ₹1,500 per patient-hour and a bay costs ₹4,000 per hour: cost of waiting per hour $=\lambda W_q\times1500$: 9 bays: $5\times0.509\times1500\approx₹3{,}819$ of waiting plus bay cost $9\times4000=36{,}000$, total ≈ ₹39,819; 10 bays: waiting ≈ ₹1,380 plus $40{,}000$, total ≈ ₹41,380; so **9 bays minimises the total** on these assumed costs (8 bays: waiting ≈ ₹18,163 plus 32,000 = ₹50,163, worse; 11 bays: ₹44,565), and a higher waiting cost would justify a tenth bay. The break-even logic is the point; real costs are clinical and reputational.

### In the news
See news box. Real-world queue targets (NHS 4-hour, airport wait times) are service-level constraints; the model picks the cheapest capacity that satisfies them.

### Interview angle
> [!question] How it is asked
> "How would you determine the right number of beds, counters or lines taking the cost of waiting into account?"

> [!tip] Strong answer includes
> - Choose Erlang B for lost-calls systems, Erlang C/A for waiting systems
> - Total cost = capacity cost + waiting/blocking cost; find the minimum, or capacity meeting a service constraint
> - Point out the diminishing returns beyond the knee of the curve
> - Mention simulation for time-varying demand and networks
