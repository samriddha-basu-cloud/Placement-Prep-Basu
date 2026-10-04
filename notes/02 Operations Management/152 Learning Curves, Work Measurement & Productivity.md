---
tags: [operations-management, tier2]
area: Operations Management
topic: "Learning Curves, Work Measurement & Productivity"
tier: Tier 2
roles: Operations
status: complete
subtopics: 13
---
# Learning Curves, Work Measurement & Productivity

⬅ [[151 Service Operations Management]] · [[_Index - Operations Management|Operations Management]] · [[153 Aggregate Planning Models & Workforce Strategy]] ➡

> **Area:** Operations Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. Productivity: Partial, Multifactor and Total]]
2. [[#2. Method Study and the SREDIM Sequence]]
3. [[#3. Work Measurement: Techniques and Purpose]]
4. [[#4. Stopwatch Time Study: Normal Time and Standard Time]]
5. [[#5. Allowances: Personal, Fatigue, Delay and Contingency]]
6. [[#6. Work Sampling]]
7. [[#7. Predetermined Motion Time Systems (MTM, MOST)]]
8. [[#8. Learning Curve I: Wright's Cumulative-Average Model]]
9. [[#9. Learning Curve II: Crawford's Unit Model, Comparison and Cost Estimation]]
10. [[#10. Learning Applications: Ramp-up, Pricing, Forgetting and Limits]]
11. [[#11. Incentive Wage Plans: Halsey, Rowan, Taylor, Gantt and Group Plans]]
12. [[#12. Ergonomics, Standard Work and Linking Measurement to Lean]]
13. [[#13. ⭐ Advanced: Experience Curve vs Learning Curve, Plateau Models and Estimating from Data]]

## 📰 News box
> [!news] Why this matters now (2024–2026): learning curves explain why clean-energy costs keep falling, and why ramp-up plans matter
> **Solar PV is the textbook learning curve.** Our World in Data reports that for more than four decades (1976-2019) the price of solar modules fell by about **20% with every doubling of global cumulative capacity**, from roughly **$106 per watt to $0.38 per watt (a 99.6% fall)**. That is a Wright's-law curve at industry scale: the "learning rate" here is 20%, equivalent to an 80% curve. ([Our World in Data](https://ourworldindata.org/learning-curve)) The same logic, applied inside a single plant or a single operator's first 100 units, drives every new-line ramp-up plan, PLI-scheme capacity addition and contract-price quote in this note.
>
> Sub-topics that say **"See news box"** reuse this item. Work measurement and incentive plans have no news hook; their "In the news" lines tie them to the learning-curve story or say so plainly.

---
## 1. Productivity: Partial, Multifactor and Total
> 🟠 Tier 2 · _Key points:_ Output/input; partial vs multifactor vs total; productivity vs efficiency vs effectiveness

### Definition
**Productivity** is the ratio of output to the inputs used to make it. Measure in consistent units (physical units or constant-price rupees) so that price inflation does not masquerade as improvement.

$$\text{Partial productivity} = \frac{\text{Output}}{\text{One input}} \quad (\text{e.g. units per labour-hour})$$
$$\text{Multifactor productivity} = \frac{\text{Output}}{\text{Labour} + \text{Material} + \text{Energy}} , \qquad \text{Total productivity} = \frac{\text{Output}}{\text{All inputs incl. capital}}$$
Related terms: **efficiency** compares actual output with the standard or expected output (see [[018 Capacity Management & OEE]]); **effectiveness** is doing the right thing (meeting the goal). Partial measures mislead when inputs are substituted: automating a line raises labour productivity but may lower capital productivity. Hence analysts compare partial, multifactor and total measures together. **Productivity growth** is the main long-run source of wage growth without inflation; in services, measuring output quality is the practical difficulty (see [[151 Service Operations Management]]).

### Example
Year 1: 50,000 units sold at ₹480, labour 2,500 hours at ₹350, material ₹300 per unit, energy ₹2.0 lakh, capital charge ₹10 lakh. Year 2: 56,000 units, labour 2,550 hours, material ₹295 per unit, energy ₹2.2 lakh, capital charge ₹11.5 lakh (new machine). All in constant Year 1 prices.

| Measure | Year 1 | Year 2 | Change |
|---|---|---|---|
| Labour productivity (units/hr) | 20.0 | 21.96 | +9.8% |
| Multifactor (output / labour + material + energy) | 1.493 | 1.524 | +2.1% |
| Total (output / all inputs) | 1.406 | 1.431 | +1.8% |

Labour productivity jumped 9.8%, but once material, energy and the new machine are counted, total productivity rose only 1.8%. A strong answer says which measure the claim is based on.

### In the news
See news box. The solar curve is a total-cost productivity story: the price fall comes from scale, process learning and material efficiency together, not labour alone.

### Interview angle
> [!question] How it is asked
> "A plant says productivity rose 10%. How would you check whether that is real improvement?"

> [!tip] Strong answer includes
> - Ask which measure (partial vs total) and in constant prices
> - Check input substitution: did capital, outsourcing or overtime replace labour?
> - Compute multifactor and total productivity from the same data
> - Tie to value: output of the right quality, not just volume

---

## 2. Method Study and the SREDIM Sequence
> 🟠 Tier 2 · _Key points:_ Select-Record-Examine-Develop-Install-Maintain; process charts; 5W1H; ECRS

### Definition
**Method study** is the systematic recording and critical examination of existing and proposed ways of doing work, to find easier and more effective methods. It comes before work measurement: there is no point timing a bad method. The standard sequence is **SREDIM**:
1. **Select** the job (high volume, bottleneck, high cost, safety issue).
2. **Record** the facts with charts: outline process chart, flow process chart, flow diagram, **multiple-activity chart**, **two-handed (left-hand/right-hand) chart**, SIMO chart, string diagram.
3. **Examine** critically with the primary questions (what, where, when, who, how) and secondary questions (why; what else could be done; what should be done), plus the **ECRS** principle: Eliminate, Combine, Rearrange, Simplify.
4. **Develop** the best practical method (economy of motion, cost, safety).
5. **Install** the method: train workers, pilot, document standard work.
6. **Maintain** it: audit for drift.

**Principles of motion economy** (Gilbreth, Barnes): use both hands simultaneously, avoid unnecessary motions, minimise distances, keep materials in the normal work area, use gravity and jigs. The 17 **therbligs** are the basic elements of motion.

### Example
Flow process chart for an inspection step: 18 events, of which 5 are operations, 4 inspections, 6 transports and 3 delays; total distance 46 metres. After re-layout (move inspection bench next to machine, combine two inspections): 3 operations, 2 inspections, 2 transports, 1 delay, 14 metres. Events fall from 18 to 8 (−56%) and distance by 70%, before any change to machine speed.

### In the news
See news box. Gains from method improvement are the "learning" that happens by design rather than by repetition, and they often reset the curve to a lower starting point.

### Interview angle
> [!question] How it is asked
> "How would you improve a manual packing line before investing in automation?"

> [!tip] Strong answer includes
> - SREDIM, starting with a recorded baseline (video, flow chart)
> - ECRS and motion economy ideas applied to this line
> - Timing only after the method is fixed, then standard work (see [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]])
> - Operator involvement and safety, linking to [[007 Lean Manufacturing]]

---

## 3. Work Measurement: Techniques and Purpose
> 🟠 Tier 2 · _Key points:_ Time study, work sampling, PMTS, standard data; uses of standard time

### Definition
**Work measurement** determines the time a **qualified, trained worker** needs to complete a task at a **defined level of performance** using a specified method. Techniques:
- **Stopwatch time study:** direct timing of cycles with performance rating.
- **Work sampling (ratio-delay):** random instantaneous observations to estimate the proportion of time in each activity.
- **Predetermined motion time systems (PMTS):** MTM, MOST, MODAPTS, Work-Factor: times built up from tabulated basic motions.
- **Standard data and synthesis:** reuse of elemental times from earlier studies.
- **Historical or estimated times:** quick but unreliable.

Uses of the **standard time**: capacity and load planning, scheduling, costing and pricing, labour planning and headcount, line balancing, incentive wage plans, and performance control (see [[021 Scheduling & Sequencing]], [[110 Cost Accounting for Operations]]). Ethical and industrial-relations point: standards must be explained, documented and agreed, because time standards affect pay and workloads.

### Example
A line needs 360 units a shift on 480 minutes of available time. If the standard time is 1.45 min/unit, required workstation-time $= 360 \times 1.45 = 522$ min, so more than one operator is needed: $522/480 = 1.09$, hence 2 operators (or a method change to cut about 10%). Without a measured standard time, the headcount decision is a guess.

### In the news
See news box. Standard time is the first point on the plan; the learning curve describes how the actual time falls towards it over the first units.

### Interview angle
> [!question] How it is asked
> "When would you use work sampling instead of a stopwatch study?"

> [!tip] Strong answer includes
> - Stopwatch for short, repetitive cycles; work sampling for long, irregular or multi-person activities
> - PMTS when the job does not yet exist (new line design)
> - What each technique yields and its accuracy and cost
> - Standard time as an input to staffing and costing

---

## 4. Stopwatch Time Study: Normal Time and Standard Time
> 🟠 Tier 2 · _Key points:_ Observed time, rating, normal time, allowances, standard time, sample size

### Definition
Steps: break the job into **elements**, time each element over several cycles with a stopwatch (continuous or snap-back), discard abnormal readings, apply **performance rating**, then add allowances.

$$\text{Normal time} = \text{Average observed time} \times \frac{\text{Rating}}{100}$$
$$\text{Standard time} = \text{Normal time} \times (1 + \text{Allowance}) \quad \text{or} \quad \frac{\text{Normal time}}{1 - \text{Allowance fraction of total time}}$$
Use the first form when the allowance percentage is given on **work time**, and the second when it is given on **total (shift) time**. State which one you use. **Rating** compares the observed pace with a concept of normal pace (100% = a qualified worker, motivated, working neither fast nor slow). Rating methods: speed rating, Westinghouse (skill, effort, conditions, consistency), synthetic rating.

**Sample size** for the cycle time at 95% confidence and accuracy $\pm k$ of the mean:
$$n = \left(\frac{z\, s}{k\, \bar{x}}\right)^2 , \quad z = 1.96$$
where $s$ is the sample standard deviation (see [[092 Sampling & Experimental Design]]). Barnes's range method gives the same estimate from the range of readings.

### Example
Ten observed cycle times (minutes): 1.00, 1.12, 0.95, 1.08, 1.20, 0.98, 1.05, 1.15, 0.92, 1.10. Mean $\bar x = 1.055$, $s = 0.0912$. For $\pm 5\%$ at 95%: $n = (1.96 \times 0.0912/(0.05 \times 1.055))^2 = 11.5$, so about **12 cycles**: take 2 more readings. Rating 110%: normal time $= 1.055 \times 1.10 = 1.1605$ min. Allowances 15% of the shift: standard time $= 1.1605/(1 - 0.15) = 1.365$ min. Output per 480-minute shift $= 480/1.365 = 351.6$, so about 351 units.

Multi-element example (minutes): element observed time × rating: pick blank $0.30 \times 1.05 = 0.315$; load fixture $0.25 \times 1.10 = 0.275$; drill $0.55 \times 0.95 = 0.5225$; unload $0.20 \times 1.10 = 0.220$. Normal time $= 1.3325$ min. Allowances (personal 5%, fatigue 6%, delay 5% $= 16\%$ of total time): standard time $= 1.3325/0.84 = 1.586$ min; units per shift $= 480/1.586 = 302.6$.

### In the news
See news box. Standard times are the target the learning curve approaches; plant ramp-up plans compare actual hours per unit against the standard each week.

### Interview angle
> [!question] How it is asked
> "A time study gives 1.2 minutes average with 115% rating and 12% allowance. What is the standard time and daily output?"

> [!tip] Strong answer includes
> - Normal time $= 1.2 \times 1.15 = 1.38$ min, then allowance (state which formula): $1.38 \times 1.12 = 1.546$ min, or $1.38/0.88 = 1.568$ min
> - Output per shift $= 480/\text{ST}$ (about 306 to 311 units)
> - Check sample size, abnormal readings and operator selection
> - Acknowledge rating subjectivity and mitigations (training, benchmark films)

---

## 5. Allowances: Personal, Fatigue, Delay and Contingency
> 🟠 Tier 2 · _Key points:_ PF&D; basic vs variable fatigue; total vs work-time basis

### Definition
Allowances compensate for time that is a necessary part of the job but not captured in the observed pace:
- **Personal needs** (rest room, water): typically 5% of an 8-hour shift (about 24 minutes) in many standards.
- **Fatigue:** a basic fatigue allowance (around 4%) plus a **variable** component for heavy work, poor posture, heat, noise, repetitiveness and mental strain. Ergonomic design cuts the variable part: seated work, adjustable height, balanced loads (see [[022 Maintenance Management (TPM-RCM)]] for autonomous care and [[007 Lean Manufacturing]] for standard work and workplace organisation).
- **Delay allowance:** unavoidable delays (machine waiting, supervisor instructions, material arrival).
- **Special allowances:** tool changes, setup, policy allowances (e.g. safety breaks), contingency.

The typical total ranges from about 10% (light, comfortable work) to 25% or more (heavy, hot). Indian statutory framing: the Factories Act 1948 limits working hours and requires a rest interval of at least half an hour after five hours of work (its provisions are being subsumed by the Occupational Safety, Health and Working Conditions Code; verify current status), so allowances should never be used to compress legal rest. Shop-floor practice and company standards vary; do not quote one number as universal.

### Example
Operator allowance sheet: personal 5%, basic fatigue 4%, variable fatigue (standing, moderate lift) 3%, delay 3%, total 15%. Normal time 2.00 min per piece. Standard time (on total time) $= 2.00/0.85 = 2.353$ min; (on work time) $= 2.00 \times 1.15 = 2.30$ min. Over 480 min, output is 204 pieces versus 208.7: a 2.3% difference, which is why the basis must be stated in the standard.

### In the news
See news box. In a ramp-up, early hours per unit include learning losses that must not be hidden inside "allowances"; keep learning allowances separate and time-limited.

### Interview angle
> [!question] How it is asked
> "Why not set standard time equal to the observed average time?"

> [!tip] Strong answer includes
> - Observed time reflects one person's pace on that day, hence rating
> - Allowances for personal, fatigue and delay time make the standard attainable all shift
> - Explain the two allowance formulas and their small numeric difference
> - Mention union and legal context, and review of standards after method change

---

## 6. Work Sampling
> 🟠 Tier 2 · _Key points:_ Random observations; binomial sample size; activity ratios

### Definition
**Work sampling** (activity sampling, ratio-delay study; Tippett, 1930s) records at random instants what each person or machine is doing. If $p$ is the true proportion of time in an activity, observations $n$ give $\hat p$ with standard error $\sqrt{p(1-p)/n}$.

$$n = \frac{z^2\, p(1-p)}{e^2} \quad (\text{absolute accuracy } e), \qquad n = \frac{z^2 (1-p)}{k^2 p} \quad (\text{relative accuracy } k)$$
At 95% confidence $z = 1.96$. Observation instants should be random (random-number tables) over the whole period, covering all shifts. Advantages: cheaper than continuous observation, can study groups, tolerates interruptions, no stopwatch needed, less intrusive. Disadvantages: gives no detail on method, needs large samples for rare activities, and observer bias in classification.

**Standard time by work sampling:**
$$\text{Normal time per unit} = \frac{\text{Total time} \times \text{Fraction working} \times \text{Average rating}}{\text{Units produced}}$$
then add allowances as before.

### Example
Guess 30% idle time for warehouse pickers; want $\pm 5$ percentage points at 95%: $n = 1.96^2 \times 0.30 \times 0.70/0.05^2 = 322.7$, so about **323 observations**. With a tighter $\pm 3$ points: $n = 896$. After 600 observations, 150 are "idle": $\hat p = 25\%$, half-width $= 1.96\sqrt{0.25 \times 0.75/600} = 3.46$ points, so idle time is between about 21.5% and 28.5%.

Standard-time case: one operator observed over 10 days (4,800 minutes), working 82% of the time at average rating 100%, producing 2,000 units: normal time $= 4{,}800 \times 0.82 \times 1.00/2{,}000 = 1.968$ min; with 15% allowance on total time, standard time $= 1.968/0.85 = 2.315$ min.

### In the news
No separate news hook. Activity sampling is the usual way to size staffing in service settings such as nursing wards or ticket counters (see [[151 Service Operations Management]]); it is a standard technique, not a claim about any named company.

### Interview angle
> [!question] How it is asked
> "How would you measure how much time warehouse staff actually spend on productive work?"

> [!tip] Strong answer includes
> - Work sampling with random times, defined activity categories and stratification by shift
> - Sample size formula and a numeric answer
> - Confidence interval on the result
> - Follow-ups: turn the idle categories into action (see [[127 Warehouse Engineering - Racking, Sizing & Material Handling]], [[128 Warehouse Labour, WES-WCS & Yard Management]])

---

## 7. Predetermined Motion Time Systems (MTM, MOST)
> 🟠 Tier 2 · _Key points:_ TMU; synthetic times before the job exists; MTM-1, MTM-2, MOST

### Definition
**PMTS** build the time for a job from tabulated times for basic motions (reach, move, grasp, position, release, turn, disengage), already levelled to a normal pace, so no performance rating is needed. **MTM-1** (Methods-Time Measurement, 1948) uses the **TMU**:

$$1\ \text{TMU} = 0.00001\ \text{hour} = 0.0006\ \text{min} = 0.036\ \text{s}, \qquad 100{,}000\ \text{TMU} = 1\ \text{hour}$$
Faster derivatives: **MTM-2**, **MTM-3**, **MOST** (Maynard Operation Sequence Technique, which uses index-value sequences for general move, controlled move, tool use) and **MODAPTS**. Use them for short-cycle repetitive assembly, planning new lines before any worker exists, comparing methods on paper, and building standard data.

Limitations: need analyst training and certification, not suited to mental tasks or long process-controlled cycles, and table values reflect the original manufacturing conditions; companies often calibrate with their own time studies.

### Example
Illustrative (not taken from the MTM-1 tables): an assembly step comprises motions of 12.9, 8.0, 15.0, 9.5 and 20.0 TMU. Total $= 65.4$ TMU $= 65.4 \times 0.036 = 2.354$ seconds. At normal pace a worker can do $3600/2.354 = 1{,}529$ such steps an hour before allowances. With 15% allowance on total time: $3600 \times 0.85/2.354 = 1{,}300$ per hour.

### In the news
No separate news hook. For lines being set up under India's manufacturing incentive schemes (see [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]), PMTS is the standard way to set line-balance targets before the first worker is hired.

### Interview angle
> [!question] How it is asked
> "We are designing a new assembly line. How do you estimate cycle times before it exists?"

> [!tip] Strong answer includes
> - PMTS (MTM or MOST) from drawings and method sketches
> - Value of TMU and basic arithmetic
> - Validate with a pilot line and update standards; link to line balancing and takt time
> - Caveat on suitability and analyst skill

---

## 8. Learning Curve I: Wright's Cumulative-Average Model
> 🟠 Tier 2 · _Key points:_ Doubling output cuts cumulative average time by a fixed percentage; $Y_n = a n^b$

### Definition
The **learning (experience) curve** says that as cumulative output doubles, the time or cost per unit falls by a constant percentage. T. P. Wright (1936) observed this in aircraft production: each doubling of cumulative units cut the **cumulative average** labour hours to about 80% (an "80% curve", learning rate 20%).

**Wright's cumulative-average model:**
$$Y_n = a\, n^{b}, \qquad b = \frac{\ln r}{\ln 2}$$
where $Y_n$ is the **cumulative average** time per unit over the first $n$ units, $a$ is the time for the first unit, and $r$ is the learning rate (e.g. $r = 0.80$, so $b = -0.3219$). Total time for $n$ units: $T_n = n\, Y_n = a\, n^{1+b}$. Time of the $n$th unit alone: $T_n - T_{n-1}$. Estimate $r$ from data by regression: $\ln Y_n = \ln a + b \ln n$ (see [[090 Regression Analysis]]).

Typical learning rates: 70-80% for assembly-heavy, labour-intensive work (aircraft, shipbuilding); 85-90% for mixed work; 90-95% for machine-paced work. A lower percentage means faster learning.

### Example
First unit takes $a = 1{,}000$ hours; 80% curve.

| Units $n$ | Cumulative average $Y_n$ (hrs) | Total time $T_n$ (hrs) |
|---|---|---|
| 1 | 1,000.0 | 1,000 |
| 2 | 800.0 | 1,600 |
| 4 | 640.0 | 2,560 |
| 8 | 512.0 | 4,096 |
| 16 | 409.6 | 6,554 |
| 20 | 381.2 | 7,624 |

Units 11-20: $T_{20} - T_{10} = 7{,}624 - 4{,}765 = 2{,}859$ hours, an average of 285.9 hours each. The 20th unit alone takes $T_{20} - T_{19} = 260.6$ hours. At ₹600 per labour-hour, 20 units cost $7{,}624 \times 600 = ₹45.7$ lakh in labour. If the observed cumulative average at 4 units is 72 hours against a 100-hour first unit, $r^2 = 0.72$, so $r = 84.9\%$.

### In the news
See news box. Solar's 20% learning rate per doubling of global capacity is the same 80% curve measured on price rather than hours.

### Interview angle
> [!question] How it is asked
> "First unit took 1,000 hours with an 80% learning curve. How long will the first 20 units take and what will unit 20 cost?"

> [!tip] Strong answer includes
> - State which model (cumulative average) and the formula $Y_n = a n^b$
> - Total hours 7,624; average 381; marginal 20th unit about 261 hours
> - Learning rate vs curve percentage (20% rate = 80% curve)
> - Caveat: curve flattens, and cost includes more than labour

---

## 9. Learning Curve II: Crawford's Unit Model, Comparison and Cost Estimation
> 🟠 Tier 2 · _Key points:_ Unit time $Y_n = a n^b$; total hours as a sum; model choice changes the answer

### Definition
**Crawford's unit model** (Lockheed, 1940s) applies the same equation to the **time of the individual $n$th unit** rather than to the cumulative average:
$$t_n = a\, n^{b}, \qquad T_n = \sum_{i=1}^{n} a\, i^{b} \approx \frac{a\,(n + 0.5)^{b+1} - a\,(0.5)^{b+1}}{b+1}$$
Doubling cumulative output cuts the **unit** time to $r$ times its previous level (e.g. unit 2 takes 80% of unit 1, unit 4 takes 80% of unit 2). Cumulative average time falls more slowly than unit time. Choice of model:
- Wright cumulative-average: popular in US aerospace pricing and defence contracting; smoother early curve.
- Crawford unit: common in operations and cost estimation; easier to link to the time of a specific unit and to labour standards.

Always state the model; the two give very different totals for the same $a$ and $r$. Use **learning tables** (multipliers) or Excel `=a*n^b`. For costing, apply the curve to **labour (and learning-sensitive overhead)**, not to purchased material.

### Example
Same data: $a = 1{,}000$ hours, $r = 80\%$, 20 units.

| Quantity | Wright (cumulative average) | Crawford (unit) |
|---|---|---|
| Total hours, 20 units | 7,624 | 10,485 |
| Average hours per unit | 381.2 | 524.2 |
| Time of unit 20 | 260.6 | 381.2 |
| Time of unit 10 | 328.6 | 476.5 |

(Crawford totals are the sum of $1000 \times i^{-0.3219}$ for $i = 1,\dots,20$; the integral approximation gives 10,512.) The Wright model gives 27% less total labour for the same inputs. For a fixed-price contract of 20 units at ₹600 per hour, labour cost is ₹45.7 lakh (Wright) vs ₹62.9 lakh (Crawford): a ₹17.2 lakh difference. Use observed early-unit data to decide which model fits.

How many units until a unit takes 400 hours (Crawford)? $n = (400/1000)^{1/(-0.3219)} = 17.2$, so unit 18 (unit 17 takes 401.7 hours, unit 18 takes 394.4).

### In the news
See news box. For solar and batteries the experience curve is calibrated on price per unit capacity against cumulative global output, a unit-type curve at industry level.

### Interview angle
> [!question] How it is asked
> "Wright vs Crawford: what is the difference and which one would you use for a bid?"

> [!tip] Strong answer includes
> - Cumulative-average vs unit-time definitions
> - Show the numeric difference in total hours for the same $a$ and $r$
> - Fit both to actual early data with regression and choose the better fit
> - Bid with a margin for the risk that learning is slower than modelled

---

## 10. Learning Applications: Ramp-up, Pricing, Forgetting and Limits
> 🟠 Tier 2 · _Key points:_ New-line ramp-up; experience curve pricing; forgetting; plateau; make-or-buy

### Definition
Applications:
- **Production ramp-up and staffing:** forecast hours per unit for the first weeks of a new model or line; plan trainers, overtime and yield.
- **Quoting and negotiation:** buyers expect price cuts as cumulative volume rises (learning-based price reductions in supplier contracts, see [[122 Spend Analysis, Savings & Procurement Maturity]]).
- **Make-or-buy and capacity decisions:** early volumes in-house can be costlier than the vendor's mature cost.
- **Strategy:** experience-curve pricing (BCG, 1960s): price ahead of cost to build share and drive down cost; works only if the curve is real and competitors cannot copy it.
- **Healthcare and services:** surgeon volume, call-centre onboarding.

Limits: learning flattens (plateau) when method and equipment stop changing; **forgetting** appears after breaks (a rule of thumb is to restart part-way back up the curve, depending on the break); a change of product, shift pattern or high labour turnover resets learning; machine-paced work has less learning; learning in **organisation** (tooling, layout, supplier quality) is as important as individual learning. The experience curve covers total cost (including design and material), not only labour.

### Example
New-model assembly: first unit takes 6.0 hours; unit-model learning rate 85% ($b = -0.2345$). Unit times: unit 2 = 5.10, unit 4 = 4.33, unit 8 = 3.68, unit 16 = 3.13, unit 32 = 2.66, unit 64 = 2.26 hours. The standard is 2.0 hours: unit number reaching it is $(2/6)^{1/-0.2345} = 108$. Cumulative hours of the first 50 units $= 153.1$, whereas at the standard 2.0 h/unit those 50 units would take 100 hours: 53 hours of learning loss, which the plan should fund (extra staff, trainers, lower first-month output) rather than blame on operators.

### In the news
See news box. The same logic applies to any new plant: expect hours and cost per unit to fall along a curve with cumulative volume, and plan the early months accordingly.

### Interview angle
> [!question] How it is asked
> "A new line is meeting only 60% of target output in week 2. Is it a problem?"

> [!tip] Strong answer includes
> - Compare with expected learning curve and cumulative output, not the steady-state target
> - Separate learning (operators, method) from equipment (OEE) and material issues, linking [[018 Capacity Management & OEE]]
> - Plan: structured training, standard work, quick feedback, staged targets
> - Warn about forgetting, turnover and shift changes

---

## 11. Incentive Wage Plans: Halsey, Rowan, Taylor, Gantt and Group Plans
> 🟠 Tier 2 · _Key points:_ Time-saved bonuses; piece-rate; standard time as the basis

### Definition
Incentive plans pay for output above a **standard**, using standard times from work measurement. Classic individual plans:
- **Halsey 50-50:** worker shares a fraction (usually 50%) of time saved. $\text{Wage} = R\, T_a + \tfrac12 R (T_s - T_a)$.
- **Rowan:** bonus proportional to the fraction of standard time saved, so the bonus falls as savings become very large (an in-built cap). $\text{Wage} = R\, T_a + \dfrac{T_s - T_a}{T_s}\, T_a R$.
- **Taylor's differential piece rate:** two piece rates, a low one (about 83% of normal) below standard and a high one (about 125%) at or above standard.
- **Gantt task and bonus:** guaranteed day rate; at or above standard, the worker gets a bonus (typically 20%) plus pay for time.
- **Emerson efficiency plan:** a graduated bonus starting at about two-thirds efficiency.
- **Group plans:** Scanlon, Rucker, gainsharing, and profit-sharing, which reward team productivity and cut internal conflict.

Design principles: standards must be fair and accurate; payment must be simple and prompt; quality must be protected (pay on good units); guaranteed minimum wage; safety not compromised. In India, wage-plan changes interact with minimum wage law, bonus law, and settlements with unions; confirm current coverage under the new labour codes (see [[153 Aggregate Planning Models & Workforce Strategy]]).

### Example
Job standard $T_s = 10$ hours, rate $R = ₹150$ per hour, actual $T_a = 8$ hours.
- Time wage $= 8 \times 150 = ₹1{,}200$.
- Halsey: $1{,}200 + 0.5 \times 150 \times 2 = ₹1{,}350$ (₹168.75 per hour).
- Rowan: $1{,}200 + (2/10) \times 8 \times 150 = ₹1{,}440$ (₹180 per hour).
If the worker finishes in 5 hours, Halsey gives $750 + 375 = ₹1{,}125$ and Rowan gives $750 + 0.5 \times 5 \times 150 = ₹1{,}125$; if 2 hours, Halsey $300 + 600 = ₹900$, Rowan $300 + 0.8 \times 2 \times 150 = ₹540$: Rowan protects the firm from loose standards.

Taylor's differential with standard 40 pieces and a base ₹5 per piece: at 35 pieces the rate is $0.83 \times 5 = ₹4.15$ and pay is ₹145.25; at 40 pieces pay is $40 \times 6.25 = ₹250$; at 48 pieces ₹300. The cliff at 40 shows why such plans are harsh.

### In the news
No dedicated news hook here. See news box for the productivity story that incentive design should be aligned to: gains are shared when learning and method gains are real.

### Interview angle
> [!question] How it is asked
> "How would you design an incentive for pickers in a distribution centre without hurting quality?"

> [!tip] Strong answer includes
> - Base on measured standard times (engineered standards)
> - Individual or team plan, with quality gate (pay on error-free lines) and safety limits
> - Compare Halsey and Rowan style sharing; avoid cliffs and ratchet effects
> - Pilot, communicate standards, review with the union or workforce representatives

---

## 12. Ergonomics, Standard Work and Linking Measurement to Lean
> 🟠 Tier 2 · _Key points:_ Human factors; standard work; takt; line balancing

### Definition
**Ergonomics** (human factors engineering) fits the job to the worker: workstation height and reach envelope, force and repetition limits (NIOSH lifting equation, RULA/REBA posture scoring), lighting, noise, heat. Poor ergonomics adds fatigue allowance, injuries, absenteeism and error. Good method study and ergonomics reduce standard time and variable fatigue allowance together.

**Standard work** (Lean) documents the best known sequence, cycle time and standard WIP, using time-study data. Link to **takt time** $= \dfrac{\text{Available time}}{\text{Demand}}$ and **line balancing**: assign elements so that no station's time exceeds the takt, with balance efficiency $= \dfrac{\sum t_i}{N \times \text{cycle time}}$ (see [[156 Lean Management Systems - A3, Hoshin Kanri & Standard Work]], [[017 Process Management & Optimization]]).

### Example
Demand 360 units in 480 minutes, takt $= 480/360 = 1.33$ min. Work content 6.4 min requires at least $6.4/1.33 = 4.8$, so 5 stations. With five stations at takt 1.33 min the balance efficiency is $6.4/(5 \times 1.33) = 96\%$. If standard times are mis-set by +10% (7.04 min), the same layout requires 5.3, so 6 stations and balance efficiency falls to $7.04/(6 \times 1.33) = 88\%$.

### In the news
See news box. Learning curves, ergonomics and standard work are the human side of line ramp-up; the equipment side is OEE.

### Interview angle
> [!question] How it is asked
> "How do time study and Lean's standard work fit together?"

> [!tip] Strong answer includes
> - Time study gives element times; standard work documents sequence, takt and WIP
> - Takt vs cycle time vs standard time; line balancing efficiency
> - Ergonomic limits are constraints on pace
> - Continuous improvement means standards are revisited after each kaizen

---

## 13. ⭐ Advanced: Experience Curve vs Learning Curve, Plateau Models and Estimating from Data
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Learning curve:** labour hours per unit fall with repetition (a worker or a line). **Experience curve** (Boston Consulting Group, 1960s): total **cost per unit (in constant money)** falls by a constant percentage per doubling of cumulative volume across the whole value chain, including scale, design, process and material. Important differences: experience curves are measured on cost or price, apply to an industry or product, and are strategy tools; learning curves are measured on hours for a task and are planning tools.

Extensions: **Stanford-B** $Y_n = a (n + B)^b$ (units of prior experience $B$), **DeJong** (incompressible share $M$ of machine-paced time: $Y_n = a\,[M + (1-M) n^b]$), **S-curves** with a start-up plateau, and learning with forgetting.

**Estimating $r$ from data:** take logs, $\ln Y_n = \ln a + b \ln n$; OLS slope is $b$; $r = 2^{b}$. Check fit with $R^2$ and residual patterns; a curve that bends flat suggests the plateau models.

### Example
DeJong model with $a = 100$ minutes, $M = 0.30$ (machine-paced), $r = 0.80$ ($b = -0.3219$). At $n = 8$: $Y_8 = 100\,[0.30 + 0.70 \times 8^{-0.3219}] = 100\,[0.30 + 0.70 \times 0.512] = 65.8$ minutes, versus 51.2 for pure Wright. The incompressible share limits the achievable gain: the asymptote is 30 minutes.

Experience-curve strategy: price falls 20% per doubling. A company at 1 lakh cumulative units and ₹1,000 unit cost expects ₹800 at 2 lakh, ₹640 at 4 lakh, ₹512 at 8 lakh. A rival entering at 10,000 units faces unit cost ₹1,000 × $(10/100)^{-0.3219}$, about ₹2,100, an entry barrier unless it buys experience (licensing, acquisition) or uses new technology.

### In the news
See news box. Solar's 99.6% price decline is the standard exhibit for experience-curve strategy; new entrants succeeded by accelerating cumulative volume through subsidies and scale.

### Interview angle
> [!question] How it is asked
> "How would you estimate the learning rate from the first 12 units of a new product and use it to forecast?"

> [!tip] Strong answer includes
> - Log-log regression, check $R^2$, extract $r = 2^b$
> - Decide cumulative-average vs unit model by fit
> - Forecast with prediction intervals, adding a plateau or incompressible-time floor
> - Strategic caveats: experience curves do not continue automatically; they need deliberate process improvement
