---
tags: [guesstimates, tier1]
area: Guesstimates
topic: "Common Mistakes & How to Avoid"
tier: Tier 1
roles: Consulting
status: complete
subtopics: 10
---
# Common Mistakes & How to Avoid

⬅ [[106 Product & Tech Guesstimates]] · [[_Index - Guesstimates|Guesstimates]] · [[221 Retail, FMCG & Consumer Guesstimates - Practice Set]] ➡
> **Area:** Guesstimates · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting

## Sub-topics in this note
1. [[#1. Jumping to Answer]]
2. [[#2. Missing Population Filter]]
3. [[#3. Forgetting Frequency]]
4. [[#4. Not Checking Answer]]
5. [[#5. Paralysis on Assumptions]]
6. [[#6. Ignoring Units]]
7. [[#7. Presenting Only Final Number]]
8. [[#8. Not Structuring Creatively]]
9. [[#9. ⭐ Advanced: Reference numbers to memorise]]
10. [[#10. ⭐ Advanced: Mental maths, rounding and error propagation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Real company numbers are the best sanity checks for your estimates
> **D-Mart, Q2 FY26 (quarter ended 30 Sep 2025).** Revenue **₹16,676 crore** (+15% YoY) across **432 stores**, i.e. about ₹38.6 crore per store per quarter (≈ ₹154 crore a year). If your guesstimate for a D-Mart store's annual revenue is ₹5 crore, this one number tells you that you are off by about 30x. ([Torus Digital](https://www.torusdigital.com/toruscope/quarterly-results/avenue-supermarts-q2-fy26-results-dmarts-profit-rises-4-yoy-revenue-up-15/))
> 
> **IPL 2025 final on JioStar (reported 19 Jun 2025).** **55 million** peak concurrent viewers, **31.7 billion** minutes of watch time in the final and **840 billion** minutes across the tournament. Quoting such figures lets you test whether a bandwidth or viewership estimate is plausible. ([Business Standard](https://www.business-standard.com/industry/news/ipl-2025-breaks-viewership-records-rcb-final-draws-840-billion-minutes-125061900901_1.html))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Jumping to Answer
> 🔴 Tier 1 · _Tracker hint:_ Never blurt out a number; always structure first; interviewer wants to see your thinking

### Definition
The most common failure: stating a number in the first 10 seconds. A guesstimate is graded on **structure, assumptions, arithmetic and sanity check**, in roughly that order; the final number matters least. Standard sequence:

1. **Clarify** (scope, geography, definition, time frame).
2. **Structure** (state the formula or tree aloud: e.g. Market = Users × Frequency × Price).
3. **Ask for 30–60 seconds** to think, if needed.
4. **Assume** (with logic for each).
5. **Calculate** (round numbers, narrate).
6. **Sanity check** and conclude.

Silence for 30 seconds while structuring is acceptable; saying "one second, let me structure this" is a positive signal.

### Example
Question: "How many ATMs are there in Mumbai?" Weak: "About 10,000." Strong: "Let me clarify: bank ATMs including off-site? Then I'll go supply-side: ATMs = population / people per ATM, and cross-check on the demand side: transactions per day / transactions per ATM per day. Let me set that structure on paper first."

### In the news
See news box. Both D-Mart revenue and the IPL peak are numbers you could blurt out incorrectly; a structure forces you to build them from drivers.

### Interview angle
> [!question] How it is asked
> It is rarely asked; interviewers watch for it. The prompt is any guesstimate, such as "How many trucks cross the Mumbai-Pune highway?" ([[105 Operations & SCM Guesstimates]]).

> [!tip] Strong answer includes
> - A visible pause and a stated approach before any number
> - A tree or formula with 3–5 drivers
> - Clarifying questions that narrow scope
> - Calling out each step as you go

---

## 2. Missing Population Filter
> 🔴 Tier 1 · _Tracker hint:_ Always ask: WHO in the total population is relevant? Age, income, geography, behavior

### Definition
Starting with the **whole population** (1.4 billion) when only a subset uses the product inflates the answer by 5–50x. Apply a filter funnel: **Total population → Geography (urban/rural) → Age → Income → Behaviour/need → Share choosing this brand**. Document each filter with a rough percentage. Equivalent in B2B: total firms → size band → sector → function that buys.

$$\text{Relevant users} = N \times f_{\text{geo}} \times f_{\text{age}} \times f_{\text{income}} \times f_{\text{need}}$$

### Example
Premium baby diapers in India. Births about 23M/year (approximate) → children under 2.5 years ≈ 57M (23 × 2.5). Filters: urban 35% → 20M; income to afford premium 20% → 4M; use daily 70% → **~2.8M children**. Skipping the income filter gives 20M and an overestimate of 5x.

### In the news
See news box. D-Mart's formats serve specific urban middle-income catchments; its 432 stores show the population filter in the real world (stores sit where the target households are).

### Interview angle
> [!question] How it is asked
> "How many people buy [product] in India?" or "What is the market for [premium/niche product]?"

> [!tip] Strong answer includes
> - An explicit funnel of filters with rationale
> - Segmentation by income or location where behaviour differs
> - Using round, memorable base numbers (India: ~1.4 bn people, ~300 M households, ~35% urban; approximate)
> - Noting what is excluded and why

---

## 3. Forgetting Frequency
> 🔴 Tier 1 · _Tracker hint:_ Market size = people × per-person-per-year spend; forgetting frequency = wrong by 12x

### Definition
Market value is **volume × price**, and volume is **users × frequency × quantity per occasion**. Forgetting the time dimension gives errors of 12x (monthly vs annual), 52x (weekly) or 365x (daily). Always convert to a **per-year** figure at the end, and write the unit chain.

$$\text{Market (₹/yr)} = \text{Users} \times \frac{\text{occasions}}{\text{year}} \times \frac{\text{units}}{\text{occasion}} \times \frac{₹}{\text{unit}}$$

### Example
Coffee market (out-of-home): 10M daily drinkers × 1 cup × ₹30 × 365 = ₹1.095 × 10¹¹ = **₹10,950 crore/year** ($1.095\times10^{11}/10^7$). Without the ×365 you get ₹30 crore, 365 times too small. For a monthly purchase (e.g. phone recharge) the error is 12x.

### In the news
See news box. D-Mart's quarterly revenue ×4 is an example of annualising correctly; if you used one quarter as the year, you would underestimate by 4x.

### Interview angle
> [!question] How it is asked
> "What is the annual market for [X]?" The word "annual" is the trap.

> [!tip] Strong answer includes
> - A frequency assumption for each segment (daily, weekly, occasional)
> - Annualisation as an explicit last step
> - Units shown at each step
> - A sensitivity note: what if frequency halves?

---

## 4. Not Checking Answer
> 🔴 Tier 1 · _Tracker hint:_ Too high? Too low? Compare to publicly known reference; say 'does this pass sanity check?'

### Definition
A **sanity check** compares the result with an independent anchor: a known market size, per-capita figure, share of GDP, capacity of a facility, or a second method. Useful tests:
- **Per-capita:** answer ÷ population; is ₹ per person plausible?
- **Share of GDP/market:** must not exceed the parent market.
- **Physical limits:** can that many trucks fit on the road? Can one person do that many tasks?
- **Second route:** top-down vs bottom-up ([[105 Operations & SCM Guesstimates]] triangulation).

If it fails, find the assumption that moved it, fix it aloud, and re-state the answer.

### Example
You estimate annual revenue of a D-Mart store as ₹5 crore. Sanity anchor from the news box: ₹16,676 crore / 432 stores × 4 ≈ **₹154 crore** per store per year. You are 30x low, so revisit: store size (35,000 sq ft), footfall (say 3,000 bills/day), basket (₹1,500) → 3,000 × 1,500 × 365 = ₹164 crore ✓. (Footfall and basket are assumptions; the result lines up with the reported figure.)

### In the news
See news box. IPL's reported 55 million concurrent viewers tells you YouTube-India-scale bandwidth cannot be a few Tbps; it must be tens to hundreds of Tbps.

### Interview angle
> [!question] How it is asked
> "Does that sound reasonable?" after your answer.

> [!tip] Strong answer includes
> - A specific benchmark (per capita, known company figure)
> - Willingness to say "that looks too high" and revise
> - Explaining which assumption caused the miss
> - Final answer given as a range

---

## 5. Paralysis on Assumptions
> 🔴 Tier 1 · _Tracker hint:_ State your assumption confidently; say 'I'll assume X for now and can revisit'; keep moving

### Definition
Candidates stall when they lack data ("I don't know how many people use coffee"). The interviewer expects **reasoned guesses**, not facts. Techniques:
- **Anchor on a known number**, then adjust (e.g. 1.4 bn population, 4.5 people per household).
- **Bracket** (it is more than 1M and less than 100M, so geometric mean ≈ 10M).
- **Segment** and assume per segment.
- **Park** an assumption: "I'll assume X for now and revisit if time permits."
- Prefer round numbers that make arithmetic easy.

### Example
"Share of Mumbai households ordering food online on a given day?" Weak: "I don't know." Strong: "Mumbai has about 5M households. I'll assume 8% order on any day, since higher-income households order weekly and others rarely. We can sensitivity-test at 5% and 12%." Result 400,000 orders, with a range of 250,000–600,000.

### In the news
See news box. Even companies publish only partial numbers; analysts rely on reasoned estimates around disclosed anchors such as D-Mart's store count.

### Interview angle
> [!question] How it is asked
> Not asked directly; it appears when you do not know a number. The interviewer may say "Take any reasonable number."

> [!tip] Strong answer includes
> - Confident phrasing: "I'll assume…"
> - A one-line justification
> - Flagging sensitivity of the answer to that assumption
> - Moving on rather than debating the number

---

## 6. Ignoring Units
> 🔴 Tier 1 · _Tracker hint:_ Always write units: ₹/day, units/month, people/km²; dimensional analysis prevents errors

### Definition
**Dimensional analysis**: carry units through every step; the final unit must match the question (₹/year, trucks/day, Tbps). Typical traps: lakh/crore vs million/billion (1 lakh = $10^5$, 1 crore = $10^7$, 1 million = $10^6$, 1 billion = $10^9$), bits vs bytes (1 byte = 8 bits), rate vs volume (Mbps vs MB), per day vs per hour, tonnes vs kg, sq ft vs sq m (1 m² = 10.764 sq ft).

### Example
Streaming: 500M views × 300 s × 5 Mbps = $7.5\times10^{11}$ Mb. The unit is **megabits (a volume)**, not Mbps. Divide by 86,400 s to get a rate: 8.68 Tbps. Calling the volume "750 Tbps" is a 86,400-fold error ([[106 Product & Tech Guesstimates]]). Another one: 1.5 lakh orders × ₹400 = ₹6 crore (not ₹60 crore): 150,000 × 400 = 60,000,000 = ₹6 crore.

### In the news
See news box. Revenue is reported in ₹ crore and viewership in billions of minutes; mixing the systems is the classic slip when you cite them.

### Interview angle
> [!question] How it is asked
> Not asked; it is a hidden scoring item. Interviewers catch "lakh vs million" slips.

> [!tip] Strong answer includes
> - Units written in every line
> - One convention (Indian or international) used consistently
> - Cancelling units to verify the formula
> - Converting to a sensible final unit (₹ crore, million)

---

## 7. Presenting Only Final Number
> 🔴 Tier 1 · _Tracker hint:_ Show all steps; interviewer grades the process, not just the answer

### Definition
The interviewer cannot give credit for steps they cannot see. Write a **visible tree** on paper, narrate each branch, and **recap** in a single line at the end: "So Users × Frequency × Price = ₹X crore, which is about Y% of the market; here is my sanity check." A good layout: assumptions on the left, formula in the middle, result on the right; circle the final number with its unit.

### Example
Skeleton answer for "market for premium running shoes in India": (1) population 1.4 bn → urban 35% = 490M; (2) age 18–45 = 40% = 196M; (3) income top 10% = ~20M; (4) 30% run regularly = 6M; (5) 1 pair/year × ₹6,000: 6M × 6,000 = 36,000M = $3.6\times10^{10}$ = **₹3,600 crore**. Quick mental maths might have said "₹36,000 crore"; writing the step with units (₹ and the crore conversion) catches that 10x slip.

### In the news
See news box. Companies disclose revenue, store counts and watch-time as stepwise drivers; consulting-style answers mirror that build.

### Interview angle
> [!question] How it is asked
> Implicit in every guesstimate; sometimes "walk me through your thinking."

> [!tip] Strong answer includes
> - Visual structure and a final recap
> - Naming the key driver and the key assumption
> - Rounded numbers with units
> - A one-line "so what" after the number

---

## 8. Not Structuring Creatively
> 🔴 Tier 1 · _Tracker hint:_ Avoid formulaic repetition; sometimes segment by urban/rural, income level, or use case

### Definition
Interviewers see hundreds of "population × share × price" answers. Stand out by choosing the **cut that fits the problem**: urban/rural, income tier, use case (commute vs leisure), channel (modern trade vs kirana), supply-side (capacity of providers) vs demand-side (users), or **time-of-day**. Two structuring rules: **MECE** (mutually exclusive, collectively exhaustive) segments, and **materiality** (spend time on the 2 segments that make 80% of the answer).

### Example
Cabs in Bengaluru. Demand-side: commuters × share using cabs × trips. Supply-side: registered cabs × trips per cab per day × utilisation. Segmenting use cases: airport (fixed, high ticket), office commute (peaky), leisure. Then reconcile the two. This gives a richer discussion than a single formula, and the reconciliation doubles as a sanity check.

### In the news
See news box. Quick commerce and traditional retail have very different structures: stores (D-Mart) vs dark stores; segmenting by format is the creative cut.

### Interview angle
> [!question] How it is asked
> Any guesstimate; strong candidates introduce a segmentation that reflects real behaviour.

> [!tip] Strong answer includes
> - A MECE segmentation with a business logic
> - Focus on the largest segment
> - Both supply- and demand-side views
> - Linking the cut to the decision (e.g. which segment to enter)

---

## 9. ⭐ Advanced: Reference numbers to memorise
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Fast sanity checks need a **bank of anchors** (approximate; refresh before interviews):

| Anchor | Approx. value |
|---|---|
| India population | ~1.4 billion |
| Households (4.5 persons each) | ~300 million |
| Urban share | ~35% |
| Working-age (15–64) share | ~65–67% |
| 1 lakh / 1 crore / 1 million | $10^5$ / $10^7$ / $10^6$ |
| Seconds in a day / year | 86,400 / ~31.5M |
| Working days per year | ~300 |
| Truck payload (typical) | 10 t (heavy: 20–25 t) |

Add a handful of company anchors from news (e.g. D-Mart ₹154 crore per store per year; IPL final peak 55M concurrent viewers) and update them regularly.

### Example
Household-based estimate of toothpaste: 300M households × 1 tube/month × ₹80 × 12 = 300M × 960 = ₹2.88 × 10¹¹ = **₹28,800 crore** (upper bound, assuming all households buy). Compare with reported market sizes to calibrate.

### In the news
See news box. Both anchors (₹154 crore per D-Mart store; 55M concurrent viewers) are derived from reports, which is the habit: convert headlines into reusable reference points.

### Interview angle
> [!question] How it is asked
> Implicit: "What assumption are you making for the number of households?"

> [!tip] Strong answer includes
> - Quoting anchors without hesitation
> - Showing the derivation (people ÷ 4.5)
> - Labelling them approximate
> - Updating them when you know better

---

## 10. ⭐ Advanced: Mental maths, rounding and error propagation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Speed and accuracy under pressure come from: (1) **powers of ten** (write numbers as $a\times10^n$); (2) **round to friendly numbers** (1.4 → 1.5 if the other number is 2, since 3 is easier than 2.8); (3) **round in opposite directions** so errors cancel (one up, one down); (4) know **error propagation**: for products, relative errors add roughly: a 20% error in each of 3 multiplied inputs gives up to ~60% in the answer (about 35% if independent: $\sqrt{3}\times20\%$). So focus effort on the **largest-uncertainty driver**.

### Example
1.4M × 38 × 0.6 ≈ ? Round 1.4 up to 1.5 and 38 down to 35 (opposite directions): 1.5M × 35 = 52.5M, × 0.6 = 31.5M. Exact: 1.4M × 38 = 53.2M × 0.6 = 31.9M, so the rounded result is only about 1% low. Had both been rounded up (1.5 × 40 × 0.6 = 36M) the answer would be 13% high. Tip: if a driver has a 3x range, put your time on that.

### In the news
See news box. Reported figures such as ₹16,676 crore / 432 stores are best rounded to ₹17,000 crore / 430 ≈ ₹40 crore per quarter, quick enough for a live check.

### Interview angle
> [!question] How it is asked
> "Can you do the calculation roughly?" Many interviews forbid calculators.

> [!tip] Strong answer includes
> - Rounding stated openly
> - Errors that cancel
> - Time spent on the key assumptions, not on decimals
> - A final answer expressed as a range

---
## 🔗 Go deeper: expansion notes
- [[221 Retail, FMCG & Consumer Guesstimates - Practice Set|Retail, FMCG & Consumer Guesstimates - Practice Set]]
- [[222 Infrastructure, Energy, Healthcare & Public-Sector Guesstimates|Infrastructure, Energy, Healthcare & Public-Sector Guesstimates]]
