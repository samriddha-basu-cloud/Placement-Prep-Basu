---
tags: [consulting-preparation, tier2]
area: Consulting Preparation
topic: "Data Interpretation & Charts"
tier: Tier 2
roles: Consulting / PM
status: complete
subtopics: 10
---
# Data Interpretation & Charts

⬅ [[028 Guesstimates & Market Sizing]] · [[_Index - Consulting Preparation|Consulting Preparation]] · [[159 Case Interview - M&A & Due Diligence]] ➡
> **Area:** Consulting Preparation · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / PM

## Sub-topics in this note
1. [[#1. Chart Reading]]
2. [[#2. Index Numbers]]
3. [[#3. Business Dashboard Analysis]]
4. [[#4. Table Data Extraction]]
5. [[#5. Graph Anomalies]]
6. [[#6. Excel-Based Data Analysis]]
7. [[#7. Drawing Insights]]
8. [[#8. Presenting Findings]]
9. [[#9. ⭐ Advanced: Variance, Mix and Decomposition Analysis]]
10. [[#10. ⭐ Advanced: Statistical Thinking in Data Interpretation]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India re-bases its GDP series (Feb 2026)
> On **27 February 2026** India's National Statistics Office released a **new GDP series with base year 2022-23**, replacing the 2011-12 base that had been used for over a decade. India Briefing's summary reports real GDP growth of **7.2% for 2023-24 and 7.1% for 2024-25** under the new series, with a real GDP base of about **Rs 261.18 trillion**, and a methodology shift toward administrative data (GST, corporate filings, e-Vahan, annual household surveys) and away from proxy indicators. A new CPI series was also scheduled for release on 12 February 2026. ([India Briefing](https://www.india-briefing.com/news/indias-new-gdp-series-base-year-2022-23-explained-43112.html/); schedule: [PIB](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2226269&reg=3&lang=2))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Chart Reading
> 🟠 Tier 2 · _Tracker hint:_ Bar, line, pie, scatter, waterfall — what each shows

### Definition
Pick the chart by the question it answers.

| Chart | Best for | Watch out for |
|---|---|---|
| Bar / column | Comparing categories | Axis not starting at zero |
| Line | Trend over time | Too many series; dual axes |
| Pie / donut | Share of a whole (2–5 slices) | Hard to compare similar slices |
| Stacked bar | Composition and total together | Only the bottom segment is comparable |
| Scatter | Relationship between two variables, outliers | Correlation is not causation |
| Waterfall | Bridge from one value to another (profit bridge) | Confirm start and end totals |
| Histogram | Distribution of one variable | Bin width choice |

Reading routine: (1) title and units, (2) axes and scale, (3) legend, (4) the big pattern, (5) the exception, (6) the "so what".

### Example
A profit bridge (waterfall) for a retailer: last year Rs 100 crore, volume +18, price +6, input costs -14, wages -5, other -3 = this year Rs 102 crore (100 + 18 + 6 - 14 - 5 - 3 = 102). Reading: volume growth did the work; cost inflation took away 19 crore of it.

### In the news
See news box. Newspapers plotted old vs new GDP growth as line charts; always check that both series use the same base before reading the gap as real.

### Interview angle
> [!question] How it is asked
> "Here is a chart of revenue by region. What do you see?"

> [!tip] Strong answer includes
> - Starts with title, units and axes before describing
> - States the main pattern in one sentence, then an exception
> - Quantifies (change in %, share, rank)
> - Ends with an implication and a question for more data

---

## 2. Index Numbers
> 🟠 Tier 2 · _Tracker hint:_ Base year = 100; reading relative changes correctly

### Definition
An **index number** expresses a value relative to a base period set to 100.

$$\text{Index}_t = \frac{X_t}{X_{\text{base}}} \times 100$$

Reading rules:
- Index 125 means 25% above the base, **not** 25 percentage points of anything else.
- Change between two non-base years: $\frac{I_2 - I_1}{I_1} \times 100$ is a **percentage change**; $I_2 - I_1$ is **index points**. They differ unless $I_1=100$.
- Two series with the same base can be compared for *growth*, never for *level* (an index of 150 for A and 120 for B does not mean A is bigger than B).
- Rebasing: new index = old index / old index of the new base × 100.
- Real vs nominal: deflate with a price index, $\text{Real} = \text{Nominal}/\text{Price index} \times 100$.

### Example
Sales index (2022 = 100): 2023 = 110, 2024 = 132. Growth 2023 to 2024 = (132 - 110)/110 = 20% (but 22 index points). Rebase to 2023 = 100: 2024 = 132/110 × 100 = **120**, 2022 = 100/110 × 100 = 90.9.

### In the news
See news box. Moving the GDP and CPI base to 2022-23 means every index was reset to 100 in that year; growth *rates* are comparable, index levels are not.

### Interview angle
> [!question] How it is asked
> "The index rose from 120 to 150. By how much did it grow?" (Trap: 25%, not 30.)

> [!tip] Strong answer includes
> - Separates percentage change from index points
> - Rebases correctly if needed
> - Warns against comparing levels across different bases
> - Mentions real vs nominal when money values are involved

---

## 3. Business Dashboard Analysis
> 🟠 Tier 2 · _Tracker hint:_ KPI red/amber/green logic; trend vs snapshot

### Definition
A **dashboard** summarises KPIs against targets. **RAG status** (red/amber/green) is rule-based, e.g. green: at or above target; amber: within 5–10% below; red: worse than that. Good dashboards show:

- **Snapshot** (this month vs target) *and* **trend** (last 6–12 months). A green KPI that has fallen five months running is a warning; a red one that is rising may be recovering.
- **Leading vs lagging indicators:** pipeline and on-time dispatch lead; revenue and customer churn lag.
- **Drill-down:** from total to region, product and customer.
- **Few, balanced KPIs** (financial, customer, process, people), each with a definition and owner.

Analysis flow: headline, biggest variance, root-cause hypothesis, action.

### Example
Ops dashboard, month vs target: OTIF 91% (target 95%, amber); inventory days 48 (target 45, amber); cost per order Rs 112 (target Rs 110, amber); but OTIF trend 96, 95, 93, 92, 91 shows a steady slide. All three are only amber, yet the *trend* is the story: investigate supplier delays rather than waiting for red.

### In the news
See news box. Macro dashboards like GDP face the same lesson: a headline growth figure needs the revision and base context before judging.

### Interview angle
> [!question] How it is asked
> "Here is a dashboard for a delivery startup. What are your top three observations?"

> [!tip] Strong answer includes
> - Prioritises by business impact, not by order on the page
> - Uses trend and target together
> - Links KPIs causally (late deliveries → refunds → churn)
> - Proposes next analysis or action with owner

---

## 4. Table Data Extraction
> 🟠 Tier 2 · _Tracker hint:_ Row/column intersection reading; percentage change

### Definition
Tables test accuracy under time pressure. Habits:

1. Read the **title, units** (Rs crore vs lakh, %, mn) and footnotes first.
2. Locate the exact **row/column intersection**; underline both.
3. Compute only what is asked; approximate with round numbers when options are far apart.
4. Percentage change $=\frac{\text{New}-\text{Old}}{\text{Old}}\times100$; percentage-point change is a simple difference of two percentages.
5. **CAGR** $=\left(\frac{V_n}{V_0}\right)^{1/n}-1$.
6. Share $=\text{part}/\text{total}$; mix shifts can happen even if every part grows.

Shortcut: 5% = half of 10%; 15% = 10% + 5%; to compare ratios, cross-multiply.

### Example
Revenue (Rs crore): 2021 = 800, 2024 = 1,080. Change = 280/800 = 35%. CAGR over 3 years = $(1080/800)^{1/3}-1 = 1.35^{0.333}-1 \approx 10.5\%$ (since $1.105^3 \approx 1.349$). Margin rising from 12% to 15% is a 3 percentage-point (25% relative) increase.

### In the news
See news box. Revised GDP tables: a figure like "7.1% for 2024-25" must be read against which series and base year the column belongs to.

### Interview angle
> [!question] How it is asked
> "From the table, which region grew fastest and what is its share now?"

> [!tip] Strong answer includes
> - Confirms units and period before calculating
> - Distinguishes percentage change from percentage points
> - Uses approximation sensibly and states it
> - Notes what the table cannot tell you

---

## 5. Graph Anomalies
> 🟠 Tier 2 · _Tracker hint:_ Inflection points, outliers, truncated axes — red flags

### Definition
Spot what distorts or deserves explanation:

- **Truncated axis:** a bar chart starting at 90 makes 95 vs 100 look like a 2x gap.
- **Dual axes** that create fake correlation.
- **Inconsistent time intervals** or missing periods.
- **Inflection points:** where trend changes (a launch, policy, price rise, one-off event).
- **Outliers:** one huge value skewing averages; check data errors, then one-offs.
- **Cherry-picked window:** start date chosen to show growth.
- **Area/3D effects** exaggerating size; pie slices not summing to 100%.
- **Survivorship and denominator changes:** percentages without the base.

Always ask: is this a data issue, a seasonal effect, or a real change?

### Example
A bar chart shows quarterly sales Rs 96, 98, 100, 102 crore with the y-axis starting at 94, so the last bar looks four times the first (8 vs 2 units of height); real growth is 102/96 - 1 = 6.25%. Another case: sales spike in March every year, so a Feb-to-Mar jump is seasonality, not momentum.

### In the news
See news box. A new base year creates a visible "break" in long GDP charts; analysts add a series-break marker so the discontinuity is not mistaken for an economic shock.

### Interview angle
> [!question] How it is asked
> "What is odd about this chart?" or "The CEO says sales have tripled. Do you agree?"

> [!tip] Strong answer includes
> - Checks axis start, scale, time window and units
> - Distinguishes data artefact from business event
> - Proposes what extra data would confirm
> - Recomputes the real change from raw values

---

## 6. Excel-Based Data Analysis
> 🟠 Tier 2 · _Tracker hint:_ Pivot tables, VLOOKUP, conditional formatting for analysis

### Definition
Core Excel toolkit for analysis:

```excel
=VLOOKUP(A2, Prices!$A:$C, 3, FALSE)          // exact match, return 3rd column
=XLOOKUP(A2, Prices!A:A, Prices!C:C, "NA")     // modern, any direction
=INDEX(C:C, MATCH(A2, A:A, 0))                 // flexible lookup
=SUMIFS(Sales, Region, "West", Month, "Mar")   // conditional sum
=COUNTIFS(Status, "Late", Region, "North")
=IFERROR(B2/C2, 0)
```

- **Pivot table:** drag fields into Rows, Columns, Values (sum, count, average), Filters; use "Show values as % of total" and group dates by month.
- **Conditional formatting:** colour scales, data bars, icon sets (RAG), rules like `=B2<C2`.
- **Cleaning:** Remove Duplicates, Text to Columns, TRIM, Data Validation.
- Pitfalls: VLOOKUP needs `FALSE` for exact match, lookup value must be in the first column, and ranges should be locked with `$`.

### Example
Sales sheet with columns Region, Product, Month, Revenue. Insert pivot: Rows = Region, Columns = Month, Values = Sum of Revenue, then right-click Show Values As > % of Row Total to see each region's monthly mix; apply a 3-colour scale to find weak months in seconds. To pull product margin from a master: `=VLOOKUP(B2, Master!A:D, 4, FALSE)`.

### In the news
See news box. Statistics offices now merge GST, e-Vahan and survey data, which is exactly a large lookup-and-pivot exercise at national scale; the same skills on a smaller scale are asked in case tests.

### Interview angle
> [!question] How it is asked
> "How would you find the top 5 customers by revenue for each region?" or an Excel test in a Product/Consulting round.

> [!tip] Strong answer includes
> - Pivot table for aggregation, with a sensible layout
> - Lookups with exact match and error handling
> - Cleans data before analysing
> - Sanity checks totals against source

---

## 7. Drawing Insights
> 🟠 Tier 2 · _Tracker hint:_ So-what? thinking; business implication of data point

### Definition
An **insight** is an observation + reason + implication; data alone is not one.

- **What:** the fact ("repeat rate fell from 32% to 25%").
- **Why:** the likely driver, from segmenting the data (by cohort, channel, region).
- **So what:** the decision it supports ("fix onboarding for the paid-ads cohort first").

Techniques: compare to benchmark/target/previous; segment and find the mix effect; decompose a change (volume × price × mix); size the prize (Rs value); keep to 2–3 insights; flag the caveats. Ask "so what?" three times until you reach an action. Beware confusing correlation with causation and drawing conclusions from small samples.

### Example
Total revenue grew 10% (Rs 500 to Rs 550 crore). Decomposition: volume +12%, price -3%, mix +1%. Insight: growth is purely volume bought with discounting; margins likely fell. So what: test whether price cuts are driving volume, and protect price on top SKUs.

### In the news
See news box. "Growth is 7.1%" is an observation; the insight is whether the new series changes the ranking of sectors and what that means for investment decisions.

### Interview angle
> [!question] How it is asked
> "What would you tell the CEO based on this data?"

> [!tip] Strong answer includes
> - Observation, cause and implication in one line each
> - Quantified size of the issue
> - A recommended action and the next analysis
> - Honesty about limits of the data

---

## 8. Presenting Findings
> 🟠 Tier 2 · _Tracker hint:_ Pyramid principle; lead with conclusion; support with data

### Definition
**Pyramid principle (Barbara Minto):** answer first, then 2–4 grouped supporting arguments, each backed by data. Structure: **Situation – Complication – Question – Answer (SCQA)** for the opening. Rules: one message per slide (action title as a full sentence), MECE grouping, logical order (time, structure or importance), and "so what" at the end. For charts: one chart, one message; highlight the key bar; remove clutter; label directly. Tailor depth to the audience (executive: 30 seconds; analyst: backup).

Template: "Recommendation → three reasons → evidence → risks and next steps".

### Example
Slide title (action title): "Cutting 20% of low-velocity SKUs would free Rs 40 crore of working capital without hurting service." Support: (1) 20% of SKUs = 3% of sales, (2) holding cost saved Rs 6 crore, (3) fill rate impact under 0.5 points. Next steps and risks follow.

### In the news
See news box. Statistical agencies publish a press note leading with the headline growth number, then methodology, an answer-first structure.

### Interview angle
> [!question] How it is asked
> "Present your recommendation in two minutes" or "How would you structure the final deck?"

> [!tip] Strong answer includes
> - Conclusion first, then three supports
> - Numbers and chart titles that state the message
> - Anticipates the hardest question
> - Closes with decision needed and next steps

---

## 9. ⭐ Advanced: Variance, Mix and Decomposition Analysis
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Consulting data questions often ask "why did profit change?" Break the change into drivers.

**Price-volume-mix:** $\Delta\text{Revenue} = (\Delta Q)\,P_0 + Q_1\,(\Delta P)$ (volume effect at old price plus price effect at new volume). **Mix** arises when sales shift between products with different margins. **Variance vs plan:** favourable/unfavourable by driver. **Simpson's paradox:** a trend in each group can reverse in the aggregate because group sizes change, so always segment before concluding.

### Example
Q0 = 100, P0 = Rs 50 → revenue 5,000. Q1 = 120, P1 = Rs 48 → revenue 5,760. Volume effect = 20 × 50 = +1,000; price effect = 120 × (-2) = -240. Total = +760 ✓ (5,760 - 5,000).

### In the news
See news box. Re-basing GDP is partly a mix effect: the economy's composition (services, digital) has shifted since 2011-12, which a newer base captures.

### Interview angle
> [!question] How it is asked
> "Revenue is up but profit is down. Why?"

> [!tip] Strong answer includes
> - Splits into price, volume and mix and calculates each
> - Checks segment-level data for Simpson's paradox
> - Links drivers to operational causes
> - Proposes a targeted action

---

## 10. ⭐ Advanced: Statistical Thinking in Data Interpretation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Interpreting data well requires a few statistical habits:

- **Mean vs median:** skewed data (incomes, order values) makes the mean misleading; report the median and spread.
- **Variability:** standard deviation and range; a stable 4.0 average with huge swings is not the same as a steady 4.0.
- **Sample size and significance:** small samples produce noisy percentages; ask for n.
- **Correlation vs causation:** confounders, reverse causality.
- **Base-rate neglect:** "10% rise" on a tiny base is still tiny in absolute terms.
- **Seasonality and trend:** compare year over year, or seasonally adjusted.

### Example
Order values (Rs): 200, 220, 250, 260, 280, 6,000. Mean = 7,210/6 = 1,201.7 (7,210 sum: 200+220+250+260+280+6,000 = 7,210); median = (250+260)/2 = 255. The one big order drags the mean to five times the typical order; report the median and treat the large order separately.

### In the news
See news box. Revised growth estimates carry measurement uncertainty; mature analysts quote them with the revision history rather than as exact facts.

### Interview angle
> [!question] How it is asked
> "The average order value jumped 20%. Is that good news?"

> [!tip] Strong answer includes
> - Checks distribution (mean vs median) and outliers
> - Asks for sample size and period
> - Considers seasonality and mix
> - Separates correlation from cause before recommending

---
## 🔗 Go deeper: expansion notes
- [[162 Structured Communication - SCQA, Storylines & Case Delivery|Structured Communication - SCQA, Storylines & Case Delivery]]
- [[214 Causal Inference & Experimentation Beyond A-B Tests|Causal Inference & Experimentation Beyond A-B Tests]]
