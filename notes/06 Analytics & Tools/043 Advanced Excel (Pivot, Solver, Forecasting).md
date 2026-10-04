---
tags: [analytics-tools, tier1]
area: Analytics & Tools
topic: "Advanced Excel (Pivot, Solver, Forecasting)"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 13
---
# Advanced Excel (Pivot, Solver, Forecasting)

[[_Index - Analytics & Tools|Analytics & Tools]] · [[044 Power BI & DAX]] ➡

> **Area:** Analytics & Tools · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Pivot Tables]]
2. [[#2. XLOOKUP / VLOOKUP / HLOOKUP]]
3. [[#3. INDEX + MATCH]]
4. [[#4. Logical Functions]]
5. [[#5. Text Functions]]
6. [[#6. Date & Time Functions]]
7. [[#7. Statistical Functions]]
8. [[#8. Array Formulas & SUMPRODUCT]]
9. [[#9. Named Ranges & Dynamic Arrays]]
10. [[#10. Solver & Goal Seek]]
11. [[#11. Forecasting Tools]]
12. [[#12. Dashboard Design]]
13. [[#13. ⭐ Advanced: LET, LAMBDA, XMATCH and Power Query in Excel]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI arrives in the Excel cell, then retreats to the side pane
> **COPILOT() function (announced 19 Aug 2025).** Microsoft introduced `=COPILOT("prompt", range)` in Excel for Windows and Mac Beta Channel users with a Microsoft 365 Copilot licence, letting users classify, summarise and generate text from within a cell (example in the announcement coverage: `=COPILOT("What is the sentiment of the comment in cell A2?")`). Web access was to follow via the Frontier programme. ([GeekWire](https://www.geekwire.com/2025/excel-formula-meets-ai-prompt-microsoft-brings-new-copilot-function-to-spreadsheet-cells/))
>
> **Retirement of the function (reported Aug 2026, effective 14 Sep 2026).** The Register reports Microsoft is dropping the COPILOT() function, which stayed in preview throughout (general availability had been planned for 2027), saying the Copilot side pane "should be enough"; equivalent AI help (summarise, classify, generate, web retrieval) remains in the side pane. Google Sheets has had a similar AI function since June 2025. ([The Register](https://www.theregister.com/ai-and-ml/2026/08/17/excels-copilot-function-is-headed-for-the-recycle-bin/5288327))
>
> Lesson for placements: core formulas (lookups, pivots, Solver) are stable, while AI features come and go; build skills in the stable layer and treat AI output as a draft to verify.
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Pivot Tables
> 🔴 Tier 1 · _Tracker hint:_ Row/column/value fields; grouping; calculated fields; slicers

### Definition
A **PivotTable** summarises a flat table by dragging fields into four areas: **Rows**, **Columns**, **Values** (aggregate: sum, count, average, % of total, distinct count via the Data Model) and **Filters**. Source data must be tabular: one header row, no blanks, one record per row (best as an Excel Table, `Ctrl+T`, so ranges grow automatically).

Key features:
- **Grouping:** dates into months, quarters, years; numbers into bins (for example 0-100, 100-200).
- **Calculated field:** a formula across fields, for example `=Revenue-Cost` (works on sums, not row by row).
- **Show Values As:** % of grand total, % of row, running total, difference from previous.
- **Slicers and timelines:** click filters shared across pivots.
- **PivotCharts**, **GETPIVOTDATA**, **Refresh** (Data, Refresh All; pivots do not update automatically).
- Shortcut: Insert, PivotTable (Alt+N+V).

### Example
Sales table with columns Date, Region, SKU, Units, Revenue. Drag Region to Rows, Date (grouped by Month) to Columns, Revenue to Values (Sum) and show as "% of Column Total". Add a calculated field `Margin = Revenue - Cost`. Insert a Region slicer connected to two pivots, so one click filters both the sales and returns pivots.

### In the news
See news box. AI formulas aside, summarising with a PivotTable stays deterministic and auditable, which is why it is still the default first step when a manager sends a raw data dump.

### Interview angle
> [!question] How it is asked
> "Given this order dump, how would you find the top 5 customers by revenue and their return rate?" (usually a live Excel test)

> [!tip] Strong answer includes
> - Convert to Table first; clean data (no merged cells, consistent dates)
> - Choose the fields into the four areas aloud
> - Calculated fields and Show Values As (percent of total)
> - Slicers for the user; refresh after data changes
> - Sanity check: pivot total equals source total

---

## 2. XLOOKUP / VLOOKUP / HLOOKUP
> 🔴 Tier 1 · _Tracker hint:_ XLOOKUP syntax; exact vs approximate; error handling with IFERROR

### Definition
Lookups fetch a value from a table by a key.

```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```
- `range_lookup` FALSE (or 0) = **exact**; TRUE = approximate (needs sorted ascending first column). Forgetting FALSE is the classic bug.
- VLOOKUP only looks **right** of the key and breaks if columns are inserted (hard-coded index).
- **XLOOKUP** (Microsoft 365 / Excel 2021+): looks left or right, defaults to exact, has built-in `if_not_found`, `match_mode` (0 exact, -1 exact or next smaller, 1 exact or next larger, 2 wildcard) and `search_mode` (1 first-to-last, -1 last-to-first, 2/-2 binary). It can return multiple columns (spill).
- **Error handling:** `=IFERROR(VLOOKUP(...),"Not found")` hides all errors (even real ones); prefer `IFNA` or XLOOKUP's `if_not_found`.

### Example
Freight slabs: weights 0, 10, 25, 50 in A2:A5; rates 40, 35, 30, 25 in B2:B5. For 32 kg:
`=XLOOKUP(32, A2:A5, B2:B5, "n/a", -1)` returns the rate for the 25 kg slab = 30 (exact or next smaller).
Same with VLOOKUP: `=VLOOKUP(32, A2:B5, 2, TRUE)` = 30. SKU master: `=XLOOKUP(A2, Master[SKU], Master[Description], "Unknown SKU")`.

### In the news
See news box. Lookups remain the backbone of data prep; XLOOKUP and friends are formulas Copilot suggestions often generate, so you should be able to read and debug them.

### Interview angle
> [!question] How it is asked
> "Why is XLOOKUP better than VLOOKUP?" "Your VLOOKUP returns #N/A for a value you can see. Why?"

> [!tip] Strong answer includes
> - Left-lookup, default exact match, if_not_found, no column index
> - Common #N/A causes: trailing spaces, text vs number, wrong match type
> - IFERROR vs IFNA (do not mask real errors)
> - Approximate match requires sorted data (VLOOKUP) and suits slabs and tax brackets

---

## 3. INDEX + MATCH
> 🔴 Tier 1 · _Tracker hint:_ Two-way lookup; more flexible than VLOOKUP; array context

### Definition
`INDEX(array, row_num, [col_num])` returns the value at a position; `MATCH(lookup_value, lookup_array, [match_type])` returns the position (0 exact, 1 largest value less or equal in ascending data, -1 smallest value greater or equal in descending data).

```
=INDEX(C2:C100, MATCH(F1, A2:A100, 0))                    // one-way lookup, any direction
=INDEX(B2:M20, MATCH(G1, A2:A20, 0), MATCH(G2, B1:M1, 0)) // two-way (row and column)
```
Advantages: works left of the key, not broken by inserted columns, faster than VLOOKUP over huge ranges, two-dimensional lookup, can return a whole row or column (`INDEX(B2:M20, MATCH(...), 0)`). With multiple criteria use an array: `=INDEX(C2:C100, MATCH(1, (A2:A100=F1)*(B2:B100=F2), 0))` (array-evaluated; entered with Ctrl+Shift+Enter in older Excel). XLOOKUP now covers many cases, but INDEX/MATCH remains universal, including in older Excel and Google Sheets.

### Example
Rate card: rows = origin city (A2:A6), columns = destination zone (B1:E1). Rate from Nashik to Zone C:
`=INDEX(B2:E6, MATCH("Nashik", A2:A6, 0), MATCH("C", B1:E1, 0))`. If Nashik is the 3rd origin (A4) and C is the 3rd zone (column D), the formula returns cell D4, say Rs 18 per kg.

### In the news
See news box. Many corporate files still run on Excel 2016/2019 where XLOOKUP and dynamic arrays are unavailable, so INDEX/MATCH is the safe, portable choice.

### Interview angle
> [!question] How it is asked
> "How would you do a two-way lookup in Excel?" "When would you use INDEX-MATCH over XLOOKUP?"

> [!tip] Strong answer includes
> - The two functions, with MATCH type 0 for exact
> - Two-way example with both MATCHes
> - Why more robust than VLOOKUP
> - Multiple criteria via a boolean array or helper column

---

## 4. Logical Functions
> 🔴 Tier 1 · _Tracker hint:_ IF, IFS, AND, OR, NOT, IFERROR — nested logic

### Definition
```
=IF(logical_test, value_if_true, value_if_false)
=IFS(test1, value1, test2, value2, ..., TRUE, default)
=AND(c1, c2, ...)   =OR(c1, c2, ...)   =NOT(c)
=IFERROR(value, value_if_error)   =IFNA(value, value_if_na)
=SWITCH(expr, val1, result1, ..., default)
```
Nested IFs are evaluated in order, so put the most restrictive test first. `IFS` is cleaner; it returns #N/A if no test is TRUE, so end with `TRUE, "default"`. Combine: `=IF(AND(B2>=90, C2="Y"), "A", "B")`. Boolean arithmetic: TRUE=1, FALSE=0, so `=SUMPRODUCT((A2:A9="N")*(B2:B9>5))` counts. Avoid deep nesting beyond 3 levels: use IFS, lookup tables, or SWITCH. `IFERROR` is for presentation, not to hide data problems.

### Example
Vendor rating: score in B2, on-time % in C2.
`=IFS(AND(B2>=90, C2>=0.95), "Preferred", AND(B2>=75, C2>=0.90), "Approved", TRUE, "Review")`.
Score 92 and OTD 96% gives "Preferred"; 80 and 92% gives "Approved"; 80 and 85% falls through to "Review".

### In the news
See news box. AI helpers can draft nested logic, but a manager will still ask you to explain each branch; you must be able to trace the test order.

### Interview angle
> [!question] How it is asked
> "Write a formula to classify vendors into three tiers based on two metrics." or "What does IFERROR do and what is the danger?"

> [!tip] Strong answer includes
> - Correct order of conditions and a default branch
> - IFS or lookup table instead of deep nesting
> - AND/OR combos with parentheses
> - IFERROR can hide real bugs; use IFNA or test inputs

---

## 5. Text Functions
> 🔴 Tier 1 · _Tracker hint:_ LEFT, RIGHT, MID, TRIM, CONCATENATE, TEXT, SUBSTITUTE

### Definition
```
=LEFT(text, n)   =RIGHT(text, n)   =MID(text, start, n)
=LEN(text)   =FIND(find, within, [start])   =SEARCH(...)   // SEARCH: not case sensitive, allows wildcards
=TRIM(text)   =CLEAN(text)   =UPPER/LOWER/PROPER(text)
=SUBSTITUTE(text, old, new, [instance])   =REPLACE(text, start, n, new)
=CONCAT(a, b, ...)   =TEXTJOIN(delimiter, ignore_empty, range)   =A2&"-"&B2
=TEXT(value, "format")   =VALUE(text)
=TEXTSPLIT(text, col_delim, [row_delim])   // Microsoft 365
```
`CONCATENATE` is legacy; use `CONCAT` or `&`. `TRIM` removes extra spaces (not non-breaking spaces CHAR(160): combine `SUBSTITUTE(A2, CHAR(160), " ")`). `TEXT(0.256, "0.0%")` gives "25.6%"; `TEXT(A2, "dd-mmm-yyyy")` formats a date. Text-to-number mismatches are the main cause of failed lookups. Flash Fill (Ctrl+E) and Text to Columns are quick non-formula options.

### Example
SKU code "MH-NSK-00123 " in A2 (trailing space). State = `=LEFT(TRIM(A2), 2)` gives "MH"; city = `=MID(TRIM(A2), 4, 3)` gives "NSK"; number = `=VALUE(RIGHT(TRIM(A2), 5))` gives 123. Replace hyphens: `=SUBSTITUTE(A2, "-", "/")` gives "MH/NSK/00123 ".

### In the news
See news box. COPILOT() was marketed for "clean messy data by extracting names and phone numbers"; classical text functions do the same deterministically and are free.

### Interview angle
> [!question] How it is asked
> "You have a column with 'City - State - Pin' in one cell. How do you split it?"

> [!tip] Strong answer includes
> - TRIM first, then FIND/MID or TEXTSPLIT or Text to Columns
> - Convert text to numbers with VALUE before lookup
> - Know TEXTJOIN and TEXT for reporting labels
> - Mention Flash Fill for one-offs but formulas for repeatable work

---

## 6. Date & Time Functions
> 🔴 Tier 1 · _Tracker hint:_ TODAY, NOW, DATEDIF, WORKDAY, EOMONTH, NETWORKDAYS

### Definition
Excel stores dates as serial numbers (days since 1900-01-00) and times as fractions of a day, so date arithmetic is plain subtraction.
```
=TODAY()   =NOW()                        // volatile: recalculate each time
=DATE(y, m, d)   =YEAR/MONTH/DAY(date)   =WEEKDAY(date, [type])
=DATEDIF(start, end, "Y"/"M"/"D"/"YM"/"MD")   // undocumented but works
=EOMONTH(start, months)   =EDATE(start, months)
=WORKDAY(start, days, [holidays])   =NETWORKDAYS(start, end, [holidays])
=WORKDAY.INTL(...)  =NETWORKDAYS.INTL(...)  // custom weekends
=WEEKNUM(date)   =TEXT(date, "mmm-yy")
```
Use for SCM: lead times, ageing buckets, due dates excluding weekends/holidays, month-end cut-offs.

### Example
PO date 2 Oct 2026 (Friday). Delivery promised in 5 working days: `=WORKDAY(DATE(2026,10,2), 5)` returns Fri 9 Oct 2026. Month end: `=EOMONTH(DATE(2026,10,2), 0)` returns 31 Oct 2026. Working days from 2 to 30 Oct (weekends excluded, no holiday list): `=NETWORKDAYS(DATE(2026,10,2), DATE(2026,10,30))` = 21 (pass a holiday range such as Gandhi Jayanti and Dussehra to reduce it). Age of invoice: `=TODAY()-B2`.

### In the news
See news box. Time-based calculations are where AI-written formulas most often go wrong (inclusive vs exclusive counts, holidays), so verify with a hand check.

### Interview angle
> [!question] How it is asked
> "Calculate the ageing of invoices in 0-30, 31-60, 61-90 and 90+ buckets." or "How many working days between two dates?"

> [!tip] Strong answer includes
> - NETWORKDAYS/WORKDAY with a holiday list
> - Date as a number; subtraction gives days
> - Ageing buckets via IFS or LOOKUP on days
> - Volatile function caution (TODAY) for reproducible reports

---

## 7. Statistical Functions
> 🔴 Tier 1 · _Tracker hint:_ AVERAGE, MEDIAN, STDEV, PERCENTILE, CORREL, FORECAST

### Definition
```
=AVERAGE(r)  =MEDIAN(r)  =MODE.SNGL(r)
=STDEV.S(r)  (sample)   =STDEV.P(r) (population)   =VAR.S(r)
=PERCENTILE.INC(r, k)  =QUARTILE.INC(r, q)  =PERCENTRANK.INC(r, x)
=CORREL(x, y)   =RSQ(y, x)   =SLOPE(y, x)   =INTERCEPT(y, x)
=FORECAST.LINEAR(x, known_y, known_x)   (FORECAST is the legacy name)
=COUNTIFS  SUMIFS  AVERAGEIFS  LARGE  SMALL  RANK.EQ
```
Mean is sensitive to outliers; median is robust. **Coefficient of variation** CV = $\sigma/\mu$ compares variability across items (used for demand variability and ABC-XYZ classification). $CORREL$ ranges from -1 to +1 and shows association, not causation. Sample standard deviation divides by $n-1$:
$$s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}$$
Data Analysis ToolPak (Descriptive Statistics, Regression) is an add-in.

### Example
Daily dispatch times (hours): 10, 12, 12, 14, 40. Mean = 88/5 = **17.6**; median = **12** (the outlier 40 pulls the mean up). Squared deviations: 57.76 + 31.36 + 31.36 + 12.96 + 501.76 = 635.2; variance = 635.2/4 = 158.8; `STDEV.S` = **12.60**. `PERCENTILE.INC(r, 0.9)`: position = 0.9 × (5 - 1) = 3.6 (zero-based), so interpolate between the 4th value (14) and 5th value (40): 14 + 0.6 × (40 - 14) = **29.6** hours.

### In the news
See news box. Statistical functions are deterministic, and the AI function was positioned for text work, not numeric analysis: for numbers, use these.

### Interview angle
> [!question] How it is asked
> "Average delivery time is 3 days but customers complain. What would you check?" (answer: percentile and spread)

> [!tip] Strong answer includes
> - Mean vs median; spread via STDEV and percentiles (P90/P95 for service)
> - Sample vs population standard deviation
> - CORREL gives strength of linear relation, not cause
> - CV for comparing variability across SKUs

---

## 8. Array Formulas & SUMPRODUCT
> 🔴 Tier 1 · _Tracker hint:_ Multi-criteria summing; {CSE} arrays; SUMPRODUCT for weighted avg

### Definition
An **array formula** operates on ranges and returns one or many values. In legacy Excel, enter with **Ctrl+Shift+Enter** to get braces `{=...}` (CSE). In Microsoft 365 formulas calculate arrays natively (no CSE) and can spill.

**SUMPRODUCT(array1, array2, ...)** multiplies corresponding elements and sums; it handles arrays without CSE.
```
=SUMPRODUCT(weights, scores)/SUM(weights)                      // weighted average
=SUMPRODUCT((Region="North")*(Qtr="Q1")*Sales)                 // multi-criteria sum (AND)
=SUMPRODUCT(((Region="North")+(Region="East"))*Sales)          // OR via +
=SUMPRODUCT(--(A2:A100>100))                                    // count with condition
```
`--` converts TRUE/FALSE to 1/0. `SUMIFS/COUNTIFS` are faster for simple multi-criteria; SUMPRODUCT is needed for OR logic, calculated criteria, or weights. Arrays of unequal size give #VALUE!. Large SUMPRODUCT over entire columns is slow.

### Example
Supplier scorecard: scores 8 (quality), 6 (cost), 9 (delivery) with weights 0.5, 0.3, 0.2. `=SUMPRODUCT(B2:B4, C2:C4)` = 8×0.5 + 6×0.3 + 9×0.2 = 4 + 1.8 + 1.8 = **7.6** (weights sum to 1). Weighted average lead time: orders of 100, 300, 200 units with lead times 5, 7, 4 days: (500 + 2,100 + 800)/600 = **5.67 days**.

### In the news
See news box. As dynamic arrays and AI features spread, SUMPRODUCT knowledge matters for compatibility with older files and for transparent weighting.

### Interview angle
> [!question] How it is asked
> "How do you compute a weighted average in Excel?" "Sum sales where region is North AND month is Q1."

> [!tip] Strong answer includes
> - SUMPRODUCT form with a weight sum check
> - Boolean multiplication for AND, addition for OR
> - SUMIFS when it is enough; SUMPRODUCT when it is not
> - CSE history vs dynamic arrays

---

## 9. Named Ranges & Dynamic Arrays
> 🔴 Tier 1 · _Tracker hint:_ SPILL functions: FILTER, SORT, UNIQUE, SEQUENCE

### Definition
**Named ranges** (Formulas, Name Manager, `Ctrl+F3`) give a readable name to a cell, range, constant or formula (`=SUM(Sales)` vs `=SUM(C2:C500)`). Convert data to **Tables** to use structured references that expand automatically, e.g. `=SUM(Orders[Revenue])`.

**Dynamic array functions** (Microsoft 365, Excel 2021+) return many values that **spill** into neighbouring cells; `A2#` refers to the whole spill range.
```
=UNIQUE(range, [by_col], [exactly_once])
=SORT(range, [sort_index], [order], [by_col])    =SORTBY(range, by_range, order)
=FILTER(range, include, [if_empty])
=SEQUENCE(rows, [cols], [start], [step])
=XLOOKUP / XMATCH, =TAKE / DROP / CHOOSECOLS, =LET(name, value, calc)
```
A #SPILL! error means something blocks the spill area. Spill formulas chain: `=SORT(UNIQUE(FILTER(...)))`.

### Example
Region list: `=UNIQUE(Orders[Region])`. Top 5 SKUs by revenue from a summary in A2:B50: `=TAKE(SORT(A2:B50, 2, -1), 5)`. Delayed orders: `=FILTER(Orders, Orders[Days_Late]>0, "None")`. Dates for a 12-month calendar: `=EDATE(DATE(2026,4,1), SEQUENCE(12,1,0,1))` gives Apr 2026 to Mar 2027.

### In the news
See news box. Dynamic arrays are the formula-level feature that replaced much repetitive pivot and helper-column work, and they are what Excel kept while the COPILOT() function was retired.

### Interview angle
> [!question] How it is asked
> "Extract a list of unique customers and sort them by revenue. How?"

> [!tip] Strong answer includes
> - Names and Tables for readability and auto-expansion
> - UNIQUE, FILTER, SORT, SEQUENCE, with a chained example
> - Spill range reference (`#`) and #SPILL! causes
> - Compatibility warning for older Excel versions

---

## 10. Solver & Goal Seek
> 🔴 Tier 1 · _Tracker hint:_ LP optimization; target cell; changing cells; constraints

### Definition
**Goal Seek** (Data, What-If Analysis) changes **one input** to make **one formula** hit a target value (single variable, root finding). **Solver** (add-in: File, Options, Add-ins, Solver) optimises a **target cell** (Max, Min or Value Of) by changing **multiple variable cells** subject to **constraints**.

Solving methods: **Simplex LP** (linear model; gives sensitivity report; use whenever linear), **GRG Nonlinear** (smooth nonlinear), **Evolutionary** (non-smooth, e.g. IF logic). Set "Make Unconstrained Variables Non-Negative" and tick **Assume Linear Model** for LP. Reports: Answer, Sensitivity (shadow prices, reduced costs), Limits.

LP form: maximise $c^T x$ subject to $Ax \le b$, $x \ge 0$. Integer or binary constraints (`int`, `bin`) turn it into integer programming (slower). Typical uses: product mix, blending, transport cost minimisation, staff scheduling, network flows (see the wider LP topics in the vault).

### Example
Max profit = 40x + 30y; machine hours 2x + y ≤ 100; labour x + y ≤ 80; demand x ≤ 40; x, y ≥ 0. Corner points: (0, 80) gives 2,400; (40, 20) gives 2,200; (40, 0) gives 1,600; intersection of both resources 2x + y = 100 and x + y = 80 gives x = 20, y = 60 with profit 40×20 + 30×60 = **2,600** (feasible: x ≤ 40). So the optimum is **x = 20, y = 60, profit Rs 2,600**. In Solver: target = profit cell, Max; changing cells = x, y; add the three constraints. Goal Seek example: set the profit cell to 0 by changing the price cell to find the break-even price.

### In the news
See news box. Solver is deterministic, auditable optimisation, which suits decisions that need defensible numbers; AI cell functions are not designed for that role.

### Interview angle
> [!question] How it is asked
> "How would you decide the product mix with limited machine hours in Excel?" "Difference between Goal Seek and Solver?"

> [!tip] Strong answer includes
> - Decision variables, objective and constraints defined before opening Solver
> - Simplex LP vs GRG vs Evolutionary and why
> - Reading shadow prices from the sensitivity report
> - Goal Seek: one input one output; Solver: many inputs, constraints

---

## 11. Forecasting Tools
> 🔴 Tier 1 · _Tracker hint:_ FORECAST.ETS; seasonality; confidence intervals in Excel

### Definition
Excel offers:
- **Forecast Sheet** (Data, Forecast Sheet): one click builds a table and chart with lower/upper confidence bounds from a timeline and values.
- **FORECAST.ETS(target_date, values, timeline, [seasonality], [data_completion], [aggregation])**: Exponential Triple Smoothing (AAA version of Holt-Winters) with additive trend and seasonality.
- **FORECAST.ETS.CONFINT(target_date, values, timeline, [confidence_level], [seasonality], ...)**: the half-width of the confidence interval (default 95%).
- **FORECAST.ETS.SEASONALITY(values, timeline)**: auto-detected season length.
- **FORECAST.LINEAR**, **TREND**, **GROWTH** for linear and exponential trends; moving averages via Data Analysis ToolPak.

Requirements: timeline with **constant step** (monthly, daily); up to 30% missing points handled by interpolation. Seasonality `1` = auto, `0` = none, or a number of periods (12 for monthly data). Accuracy: compute MAPE, MAD, bias on a hold-out.
$$MAPE = \frac{1}{n}\sum \frac{|A_t - F_t|}{A_t} \times 100$$

### Example
Monthly demand Jan 2024 to Dec 2025 in B2:B25, dates in A2:A25. Forecast Jan 2026: `=FORECAST.ETS(DATE(2026,1,1), B2:B25, A2:A25, 12)`; interval half-width: `=FORECAST.ETS.CONFINT(DATE(2026,1,1), B2:B25, A2:A25, 0.95, 12)`. If forecast = 1,200 units and CONFINT = 150, range = 1,050 to 1,350. MAPE check: actual 1,100 vs forecast 1,200 gives |1,100 - 1,200|/1,100 = 9.1%.

### In the news
See news box. The ETS functions are a statistical, reproducible method; AI-in-a-cell outputs vary with prompt and model version, which is why planners should still validate with MAPE.

### Interview angle
> [!question] How it is asked
> "How would you forecast next quarter's demand in Excel and tell me how reliable it is?"

> [!tip] Strong answer includes
> - FORECAST.ETS with seasonality and a confidence interval
> - Data requirements: regular intervals, enough history (at least 2 seasons)
> - Hold-out test and MAPE/bias
> - Judgmental overlays (promotions) beyond the statistical forecast

---

## 12. Dashboard Design
> 🔴 Tier 1 · _Tracker hint:_ Linked charts, form controls, slicers, conditional formatting

### Definition
An Excel dashboard communicates the few KPIs a decision-maker needs on one screen. Build in layers: **Data** (Tables or Power Query output) → **Calculations** (pivots, formulas) → **Dashboard sheet** (charts, KPI cards).

Components: PivotCharts and charts linked to pivots; **slicers/timelines** connected to multiple pivots (Slicer, Report Connections); **form controls** (combo box, option button, scroll bar linked to a cell, driving `INDEX` or `CHOOSE`); **conditional formatting** (data bars, icon sets, colour scales, formula-based RAG); **sparklines**; KPI cards using `TEXT` formulas; named ranges; dynamic titles `="Sales: "&Region`.

Design rules: put the headline KPI top left, 4 to 6 KPIs, one chart for one message, consistent colours (RAG sparingly), minimal gridlines and 3D, label directly, show targets and variance, protect the sheet, document the refresh steps. Use Power Query for repeatable refresh; for larger data use the Data Model or Power BI (see [[044 Power BI & DAX]]).

### Example
Distribution dashboard: KPI cards (OTIF %, fill rate, inventory days, cost per case) with arrows against target; a pivot chart of OTIF by region with a Region slicer; a month timeline; a conditional-formatting table of depots where OTIF < 90% in red. Form-control dropdown chooses "Cost per case" or "OTIF" for one chart via `=INDEX(KPI_range, 1, $B$1)`.

### In the news
See news box. The feature that survived is the interactive side pane and the analytics layer, while the cell function was retired; dashboards still need human-defined KPIs and thresholds.

### Interview angle
> [!question] How it is asked
> "Design a one-page dashboard for a warehouse manager." "What makes a dashboard bad?"

> [!tip] Strong answer includes
> - Audience and decisions first, KPIs second, charts last
> - Layered build with refreshable data
> - Interactivity: slicers, form controls; RAG logic with thresholds
> - Pitfalls: clutter, too many colours, no targets, stale data

---

## 13. ⭐ Advanced: LET, LAMBDA, XMATCH and Power Query in Excel
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**LET** names intermediate results inside one formula (readability and speed): 
```
=LET(sales, SUMIFS(Rev, Reg, A2), cost, SUMIFS(Cost, Reg, A2), (sales-cost)/sales)
```
**LAMBDA** creates reusable custom functions without VBA: `=LAMBDA(x, y, x/y)`; save via Name Manager (for example `MARGIN(rev, cost)`); with helper functions `MAP`, `REDUCE`, `SCAN`, `BYROW`, `BYCOL`, `MAKEARRAY`. **XMATCH** is the modern MATCH (supports exact/next, wildcard, reverse search). 

**Power Query** (Data, Get Data) is the repeatable ETL layer: import from CSV, folder, web, SQL; steps recorded in the M language (merge, append, pivot/unpivot, split, group by, fill down); refresh in one click. Best practice: never manually clean data that will arrive again; build a query. **Power Pivot / Data Model** adds relationships and DAX measures inside Excel. Shortcuts to know: Ctrl+T (table), F4 (absolute reference), Alt+= (autosum), Ctrl+Shift+L (filters).

### Example
Combine 12 monthly CSV files from a folder: Data, Get Data, From Folder, Combine and Transform, remove duplicates, change types, load to a Table, Refresh each month. Margin as LAMBDA: `=LAMBDA(rev, cost, (rev-cost)/rev)`; named `MARGIN`; then `=MARGIN(B2, C2)` where B2 = 500 and C2 = 380 gives 0.24 (24%).

### In the news
See news box. The experimental AI cell function was retired a year after its preview, while the formula language (LET, LAMBDA, dynamic arrays) and Power Query are what you can rely on; treat AI output as a draft.

### Interview angle
> [!question] How it is asked
> "You receive the same messy report every month. How do you automate it without macros?"

> [!tip] Strong answer includes
> - Power Query for repeatable cleaning and merging
> - LET/LAMBDA to make complex formulas readable and reusable
> - Data Model/DAX when data exceeds a worksheet or needs relationships
> - Document the steps; protect against schema changes

---
## 🔗 Go deeper: expansion notes
- [[187 Excel Interview Problem Bank & Case Exercises|Excel Interview Problem Bank & Case Exercises]]
- [[188 Financial Modelling in Excel|Financial Modelling in Excel]]
- [[189 VBA, Macros & Office Scripts Basics|VBA, Macros & Office Scripts Basics]]
