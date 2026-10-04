---
tags: [excel-advanced, tier1]
area: Excel Advanced
topic: "Logical & Statistical Functions"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Logical & Statistical Functions

⬅ [[071 Lookup & Reference Functions]] · [[_Index - Excel Advanced|Excel Advanced]] · [[073 Text & Date Functions]] ➡

> **Area:** Excel Advanced · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. IF & Nested IF]]
2. [[#2. IFS Function]]
3. [[#3. AND / OR / NOT]]
4. [[#4. COUNTIF / COUNTIFS]]
5. [[#5. SUMIF / SUMIFS]]
6. [[#6. AVERAGEIF / AVERAGEIFS]]
7. [[#7. MAXIFS / MINIFS]]
8. [[#8. LARGE / SMALL]]
9. [[#9. RANK / RANK.EQ]]
10. [[#10. PERCENTILE / QUARTILE]]
11. [[#11. ⭐ Advanced: SUMPRODUCT and Array Logic (OR conditions)]]
12. [[#12. ⭐ Advanced: SUBTOTAL, AGGREGATE and Summaries on Filtered Data]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI arrives in the formula bar, and Microsoft itself says do not use it for the numbers
> **The Excel COPILOT function (announced August 2025).** It let a cell formula send a natural-language prompt to AI (summarising, classifying, formatting text). Microsoft explicitly advised against using it for numerical calculations, for retrieving information already in the workbook, or for legally sensitive content, which is exactly the territory of IF/COUNTIFS/SUMIFS. TechRadar reports it is being discontinued from 14 September 2026 in favour of the Copilot side panel, without having reached a full public launch. ([Microsoft Tech Community, Aug 2025](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-ai-to-your-formulas-with-the-copilot-function-in-excel/4443487); [TechRadar](https://www.techradar.com/pro/microsoft-is-dropping-its-excel-copilot-function-after-only-a-year-and-without-ever-getting-a-full-public-launch))
>
> **Python in Excel is generally available** (Microsoft: "now generally available" for Windows users of Microsoft 365 Business and Enterprise, built with Anaconda; Excel for the web was slated for early 2025). It brings pandas and statistical libraries into cells (`=PY(...)`), complementing, not replacing, native logical and statistical functions. ([Microsoft Tech Community](https://techcommunity.microsoft.com/blog/excelblog/python-in-excel-%E2%80%93-available-now/4240212); [Petri M365 changelog, Dec 2024](https://petri.com/microsoft-changelog/m365-changelog-microsoft-excel-for-the-web-python-in-excel-will-be-generally-available-starting-in-early-2025-dec-19-2024/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
**Sample data used in the examples below** (Region in `A2:A7`, Product in `B2:B7`, Sales in `C2:C7`): East A 100; East B 150; West A 200; West A 120; West B 80; East A 130. Total sales 780, mean 130.

## 1. IF & Nested IF
> 🔴 Tier 1 · _Tracker hint:_ =IF(A1>90,'a',IF(A1>75,'b','c')); max 7 levels; prefer ifs() in excel 365

### Definition
`=IF(logical_test, value_if_true, [value_if_false])` evaluates a condition and returns one of two results. Nest IFs for more than two outcomes: `=IF(A1>90,"A",IF(A1>75,"B","C"))`. Excel evaluates conditions **in order** and stops at the first true, so order thresholds from most to least restrictive.

Correction to the tracker hint: the limit was 7 nested levels in Excel 2003 and earlier; **Excel 2007 onwards allows 64**. Deep nesting is unreadable, so prefer `IFS`, `SWITCH`, a lookup table with approximate match (`XLOOKUP`/`VLOOKUP(...,TRUE)`) or `LET`. Omitting `value_if_false` returns `FALSE`; use `""` for blank. Comparison operators: `=`, `<>`, `>`, `>=`, `<`, `<=`. Text comparisons are case-insensitive. Combine with `AND`, `OR`, `NOT` for compound tests. IF returns a value; combine with conditional formatting for visual flags.

### Example
Score in `A1` = 82. `=IF(A1>90,"A",IF(A1>75,"B","C"))`: 82 is not above 90, but is above 75, so the result is "B". A supplier flag: `=IF(D2>0.95,"Preferred",IF(D2>=0.85,"Approved","Review"))` where `D2` is on-time delivery (0.91 returns "Approved").

### In the news
See news box. Logical tests are deterministic and auditable; Microsoft warned that its AI COPILOT function should not be used for numerical calculations, so grading or flagging rules belong in IF/IFS.

### Interview angle
> [!question] How it is asked
> "Write a formula that assigns a grade or rating based on a score. How do you keep it maintainable?"

> [!tip] Strong answer includes
> - Correct ordering of conditions; nested logic shown clearly
> - Know the 64-level limit and why you should not reach it
> - Alternatives: IFS, lookup table with approximate match, SWITCH
> - Guard for blanks and text (`IF(A1="","",...)`)

---

## 2. IFS Function
> 🔴 Tier 1 · _Tracker hint:_ =ifs(A1>=90,'a',A1>=75,'b',A1>=60,'c',TRUE(),'f'); cleaner than nested if

### Definition
`=IFS(test1, value1, test2, value2, ..., [testN, valueN])` checks tests in order and returns the value for the **first TRUE**. Available in Excel 2019 and Microsoft 365 (not Excel 2016 or earlier). If no test is true it returns `#N/A`, so end with a catch-all: `TRUE, "default"`.

Advantages: flat and readable, no closing parenthesis pile-up. Limits: up to 127 pairs; all tests must be written out (no shared left side, unlike `SWITCH`), and evaluation is in order, so order matters. For equality on one expression use `SWITCH(expr, val1, res1, ..., default)`. For many bands, a small table plus `XLOOKUP(...,-1)` is easier to maintain, since business users can edit the table without touching formulas.

### Example
`=IFS(A1>=90,"A",A1>=75,"B",A1>=60,"C",TRUE,"F")`. For 58: the first three tests are false and `TRUE` catches it, so the result is "F". For 82: second test is the first true, so "B". Delivery tiers: `=IFS(B2<=2,"Express",B2<=5,"Standard",TRUE,"Economy")` where `B2` = delivery days (4 returns "Standard").

### In the news
See news box. IFS is a plain deterministic function, consistent with Microsoft's advice to keep exact rule-based logic out of AI-generated formulas.

### Interview angle
> [!question] How it is asked
> "Rewrite this nested IF using a cleaner function. What happens if no condition is true?"

> [!tip] Strong answer includes
> - IFS syntax and first-true behaviour; `TRUE` as the default branch
> - `#N/A` if no match; version availability
> - SWITCH for equality, lookup table for many bands
> - Readability and maintainability argument

---

## 3. AND / OR / NOT
> 🔴 Tier 1 · _Tracker hint:_ =IF(AND(A1>0,B1>0),'both positive',''); combine with if for compound conditions

### Definition
Logical functions combine conditions and return TRUE or FALSE:

| Function | Returns TRUE when |
|---|---|
| `AND(c1, c2, ...)` | All conditions are TRUE |
| `OR(c1, c2, ...)` | At least one is TRUE |
| `NOT(c)` | The condition is FALSE |
| `XOR(c1, c2)` | An odd number are TRUE |

They are usually wrapped in IF: `=IF(AND(B2<=ROP,C2="No"),"Reorder","OK")`. Inside array-style formulas (`SUMPRODUCT`, `FILTER`), the operators `*` (AND) and `+` (OR) are used instead, because `AND`/`OR` collapse an array to one result. Excel does not short-circuit `AND`/`OR`: all arguments are evaluated, so `AND(A1<>0,10/A1>2)` still errors when `A1 = 0`; use nested IF to guard. Text and blank handling: comparisons with `""` check empty cells; booleans coerce to 1/0 in arithmetic (`--(A1>5)`).

### Example
Inventory rule: reorder when stock is at or below the reorder point and no order is already open. Stock = 40, ROP = 50, open order = "No": `=IF(AND(B2<=C2,D2="No"),"Reorder","OK")` returns "Reorder". If an order is open (`D2="Yes"`), AND is FALSE and the result is "OK". Eligibility: `=IF(OR(E2>=60,F2="Waiver"),"Eligible","Not eligible")`.

### In the news
See news box. Compound business rules like these are the deterministic logic Microsoft says should not be delegated to the AI function.

### Interview angle
> [!question] How it is asked
> "Flag orders that are both overdue and above Rs 1 lakh. How would you write this?"

> [!tip] Strong answer includes
> - IF wrapping AND/OR with clear thresholds in cells, not hard-coded
> - Understand no short-circuiting and the array alternatives (`*`, `+`)
> - Operator precedence handled with brackets
> - Test edge cases (blank cells, equality)

---

## 4. COUNTIF / COUNTIFS
> 🔴 Tier 1 · _Tracker hint:_ =COUNTIFS(range1,criteria1,range2,criteria2); count with multiple conditions

### Definition
`=COUNTIF(range, criteria)` counts cells meeting one condition; `=COUNTIFS(range1, criteria1, range2, criteria2, ...)` counts rows meeting **all** conditions (AND logic; up to 127 pairs). All ranges must have the same size.

Criteria forms:

- Exact: `"West"` or a cell reference `E2`
- Comparison: `">100"`, `"<=50"`, `"<>0"`; with a cell: `">"&E2`
- Wildcards: `"Pr*"` (starts with Pr), `"?at"`; escape with `~`
- Blank / non-blank: `""` / `"<>"`
- Dates: `">="&DATE(2026,4,1)`

For **OR** logic add counts: `=COUNTIF(A:A,"East")+COUNTIF(A:A,"West")` or `=SUM(COUNTIF(A:A,{"East","West"}))`. Duplicates test: `=COUNTIF($A$2:$A$100,A2)>1`. Count unique values: `=SUM(1/COUNTIF(range,range))` (older) or `=COUNTA(UNIQUE(range))` (365). COUNTIFS is not case-sensitive and has trouble with text-numbers stored as text and strings over 255 characters.

### Example
Sample data: `=COUNTIFS(A2:A7,"East",B2:B7,"A")` counts rows where Region = East and Product = A: rows 1 and 6 qualify (sales 100 and 130), so the result is **2**. `=COUNTIF(C2:C7,">=120")` counts 150, 200, 120, 130, so **4**. `=COUNTIFS(C2:C7,">100",C2:C7,"<200")` counts 150, 120, 130, so **3**.

### In the news
See news box. Counting by criteria is a deterministic task where native functions beat AI; Python in Excel offers `value_counts` for larger summaries.

### Interview angle
> [!question] How it is asked
> "How many orders from the West region were above Rs 50,000 and delivered late? Which function?"

> [!tip] Strong answer includes
> - COUNTIFS with AND logic, criteria syntax (`">"&cell`), wildcards
> - OR logic via addition or array constants
> - Duplicate detection and unique counts
> - PivotTable as an alternative for many cross-tabs

---

## 5. SUMIF / SUMIFS
> 🔴 Tier 1 · _Tracker hint:_ =SUMIFS(sum_range,criteria_range1,criteria1,...); conditional summing

### Definition
`=SUMIF(range, criteria, [sum_range])` sums cells that meet one condition. `=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2, ...)` sums values meeting **all** conditions.

**Watch the argument order**: in `SUMIF` the sum range is *last* and optional; in `SUMIFS` the sum range comes *first* and is required. Criteria syntax is the same as COUNTIFS (operators in quotes, `">"&cell`, wildcards, dates). All ranges must be the same size. For OR logic add several SUMIFS or use `SUM(SUMIFS(sum,range,{"East","West"}))`.

Common patterns: monthly totals using date bounds (`">="&start`, `"<"&EDATE(start,1)`), top-down category rollups, and reconciliation of subtotals to the grand total. A PivotTable is faster to build for many dimensions, but SUMIFS is live, formula-driven and good for fixed-layout reports. Avoid full-column references on huge workbooks; use Tables or exact ranges.

### Example
Sample data: `=SUMIFS(C2:C7,A2:A7,"East",B2:B7,"A")` sums East and A: 100 + 130 = **230**. `=SUMIF(A2:A7,"West",C2:C7)` sums West: 200 + 120 + 80 = **400**. Check: East total 100 + 150 + 130 = 380, West 400, sum 780 equals the grand total, a reconciliation check you should always build.

### In the news
See news box. For financial or operational totals, Microsoft's guidance against AI formulas for numerics makes SUMIFS the safe, auditable choice.

### Interview angle
> [!question] How it is asked
> "Build a monthly sales summary by region and product without a PivotTable."

> [!tip] Strong answer includes
> - Correct SUMIFS argument order and anchored ranges (`$`)
> - Date-range criteria and cell-referenced thresholds
> - Reconciliation check to the grand total
> - When to prefer PivotTable or Power Query

---

## 6. AVERAGEIF / AVERAGEIFS
> 🔴 Tier 1 · _Tracker hint:_ =AVERAGEIFS(avg_range, criteria_range, criteria); conditional average

### Definition
`=AVERAGEIF(range, criteria, [average_range])` and `=AVERAGEIFS(average_range, criteria_range1, criteria1, ...)` average the cells that meet the conditions. As with SUMIFS, the **average range comes first** in `AVERAGEIFS`.

Behaviour: blank and text cells in the average range are ignored; if **no cell matches** the result is `#DIV/0!` (wrap in `IFERROR` or `IF(COUNTIFS(...)=0,...)`). A conditional average is *not* the same as the average of group averages: groups of different sizes need a **weighted average** (`SUMPRODUCT(values,weights)/SUM(weights)`) when combining. Conditional average of means hides dispersion; add `COUNTIFS` and median/percentile (via `AGGREGATE` or `FILTER`) for context. Excel has no `MEDIANIFS`: use `=MEDIAN(FILTER(range,cond))` in 365 or an array `MEDIAN(IF(...))`.

### Example
Sample data: average sales for East and A: `=AVERAGEIFS(C2:C7,A2:A7,"East",B2:B7,"A")` = (100 + 130) / 2 = **115**. Average for West: `=AVERAGEIF(A2:A7,"West",C2:C7)` = (200 + 120 + 80) / 3 = **133.3**. Overall mean = 780 / 6 = 130, while the average of the two regional means (East 126.7, West 133.3) is 130 only because both regions have 3 rows; with unequal counts the two differ.

### In the news
See news box. Python in Excel (`groupby().mean()`) handles bigger group-wise averages; native AVERAGEIFS is best for live small reports.

### Interview angle
> [!question] How it is asked
> "What is the average order value for repeat customers in Q2? How do you handle no matching rows?"

> [!tip] Strong answer includes
> - AVERAGEIFS syntax and argument order; ignoring blanks/text
> - `#DIV/0!` handling when no match
> - Weighted vs simple average of averages
> - Pair with count and spread so the average is not misleading

---

## 7. MAXIFS / MINIFS
> 🔴 Tier 1 · _Tracker hint:_ =maxifs(max_range, criteria_range, criteria); max with conditions (excel 2019+)

### Definition
`=MAXIFS(max_range, criteria_range1, criteria1, ...)` and `=MINIFS(min_range, criteria_range1, criteria1, ...)` return the largest/smallest value among rows meeting all conditions. Available in Excel 2019 and Microsoft 365. If no row matches, they return **0** (not an error), which can mislead, so check with `COUNTIFS` first.

Before 2019 you needed an array formula: `=MAX(IF(A2:A7="West",C2:C7))` (Ctrl+Shift+Enter in older Excel; works normally in 365). For the **row** of the maximum, combine with lookup: `=XLOOKUP(MAXIFS(...),C2:C7,B2:B7)` (ties return the first). Use for latest date per customer (`MAXIFS(date, customer, id)`), cheapest quote per item (`MINIFS(price, item, x)`), peak load per plant. Criteria rules are the same as COUNTIFS.

### Example
Sample data: highest sale in the West region: `=MAXIFS(C2:C7,A2:A7,"West")` considers 200, 120, 80, so **200**. Lowest West sale for product A: `=MINIFS(C2:C7,A2:A7,"West",B2:B7,"A")` considers 200, 120, so **120**. Pre-2019 equivalent for the first: `=MAX(IF(A2:A7="West",C2:C7))`.

### In the news
See news box. Native conditional extremes are exact and auditable; AI-generated lookups were discouraged by Microsoft for retrieving data already in the workbook.

### Interview angle
> [!question] How it is asked
> "Find the most recent order date for each customer without a PivotTable."

> [!tip] Strong answer includes
> - MAXIFS/MINIFS syntax; version requirement and the array-formula fallback
> - Zero returned when no match: guard with COUNTIFS
> - Combine with XLOOKUP to retrieve the row details
> - Use cases: latest date, best price, peak value

---

## 8. LARGE / SMALL
> 🔴 Tier 1 · _Tracker hint:_ =LARGE(array,1) for max, =LARGE(array,2) for 2nd largest; useful for top-n

### Definition
`=LARGE(array, k)` returns the k-th largest value; `=SMALL(array, k)` returns the k-th smallest. `LARGE(array,1)` equals `MAX`, `SMALL(array,1)` equals `MIN`. They ignore text and blanks; k beyond the count gives `#NUM!`. Ties are repeated (two equal values count as two positions).

Top-N patterns: **sum of top 3** `=SUMPRODUCT(LARGE(range,{1,2,3}))`; top-N list `=LARGE(range,ROWS($A$1:A1))` filled down; retrieve the associated label with `INDEX/MATCH` (beware duplicates: use a tie-breaker helper such as `value + ROW()/1E9`). In 365, `=TAKE(SORT(range,,-1),3)` or `=LARGE(range,SEQUENCE(3))` are simpler. For conditional k-th values: `=LARGE(IF(A2:A7="West",C2:C7),2)` (array formula) or `=AGGREGATE(14,6,C2:C7/(A2:A7="West"),2)`.

### Example
Sample sales: 100, 150, 200, 120, 80, 130. `=LARGE(C2:C7,1)` = 200; `=LARGE(C2:C7,2)` = 150; `=LARGE(C2:C7,3)` = 130. Top 3 sum: 200 + 150 + 130 = **480** (61.5% of the 780 total, since $480/780\approx0.615$). Second-smallest: `=SMALL(C2:C7,2)` = 100.

### In the news
See news box. Top-N ranking on exact numbers is again a deterministic task for native functions.

### Interview angle
> [!question] How it is asked
> "Show the top 5 suppliers by spend and their share of total spend."

> [!tip] Strong answer includes
> - LARGE with k, INDEX/MATCH to return names, tie handling
> - Share of total = top-N sum / total (Pareto link)
> - Modern alternatives: SORT/TAKE
> - Conditional top-N via AGGREGATE or array formulas

---

## 9. RANK / RANK.EQ
> 🔴 Tier 1 · _Tracker hint:_ =RANK(value, array, 0) descending; useful for supplier ranking, abc analysis

### Definition
`=RANK.EQ(number, ref, [order])` returns the rank of a number within a list: `order = 0` or omitted ranks **descending** (largest = 1), non-zero ranks ascending. `RANK` is the older compatibility name; `RANK.EQ` is the current one. **Ties** receive the same rank and the next rank is skipped (two firsts, then 3). `RANK.AVG` gives tied values the average of their ranks (1.5, 1.5, 3).

Unique ranking (break ties by order of appearance): `=RANK.EQ(C2,$C$2:$C$7)+COUNTIF($C$2:C2,C2)-1`. Rank within a group: `=COUNTIFS($A$2:$A$7,A2,$C$2:$C$7,">"&C2)+1`. In 365: `=XMATCH(C2,SORT($C$2:$C$7,,-1))`. Applications: supplier scorecards, sales leaderboards, ABC analysis (rank by value, then cumulative % to assign A/B/C), percentile of an item.

### Example
Sample sales: 200, 150, 130, 120, 100, 80 (sorted). Rank of 130 (descending): `=RANK.EQ(130,C2:C7,0)` = **3**. Rank of 100 is 5; rank of 80 is 6. If two items both had 150, each would be rank 2 and the next would be rank 4. ABC check: cumulative share of top two = (200 + 150) / 780 = 44.9%, of top three = 480/780 = 61.5%; assign classes by cumulative share thresholds.

### In the news
See news box. Rankings drive scorecards; keep them formula-based so they refresh and can be audited.

### Interview angle
> [!question] How it is asked
> "Rank 200 suppliers by composite score, handling ties, and show their quartile."

> [!tip] Strong answer includes
> - RANK.EQ vs RANK.AVG; tie behaviour and the tie-breaker formula
> - Ranking within groups (COUNTIFS) and cumulative % for ABC
> - Percent rank / quartile for banding
> - Sorting vs ranking: rank keeps the original order

---

## 10. PERCENTILE / QUARTILE
> 🔴 Tier 1 · _Tracker hint:_ =PERCENTILE(array,0.75) for 75th percentile; quartile analysis for outliers

### Definition
`=PERCENTILE.INC(array, k)` returns the k-th percentile (k between 0 and 1) using inclusive interpolation; `=PERCENTILE.EXC` excludes the 0 and 1 endpoints (needs $1/(n+1)\le k\le n/(n+1)$). `=QUARTILE.INC(array, quart)` with quart 0-4 gives min, Q1, median, Q3, max. `PERCENTILE` and `QUARTILE` are older equivalents of the `.INC` versions. `PERCENTRANK.INC(array, x)` goes the other way.

Inclusive position: $pos=1+k(n-1)$ on the sorted data, interpolating between neighbours. Outlier rule (Tukey): $IQR=Q_3-Q_1$; lower fence $=Q_1-1.5\,IQR$, upper fence $=Q_3+1.5\,IQR$; values outside are flagged. Percentiles are robust to outliers and suit skewed data (lead times, delivery SLAs: "95% delivered within X days" is `PERCENTILE.INC(times,0.95)`). Conditional percentile: `=PERCENTILE.INC(IF(A2:A7="West",C2:C7),0.9)` (array) or with `FILTER` in 365.

### Example
Sorted sample sales: 80, 100, 120, 130, 150, 200 (n = 6). Median `=MEDIAN` = (120 + 130)/2 = 125. Q1: position $1+0.25\times5=2.25$, so $100+0.25\times(120-100)=105$. Q3: position $1+0.75\times5=4.75$, so $130+0.75\times(150-130)=145$. $IQR=145-105=40$. Fences: $105-60=45$ and $145+60=205$. No value is outside (80 to 200), so no outliers; a sale of 260 would be flagged.

### In the news
See news box. Python in Excel (`describe()`, `quantile()`) can compute the same statistics on bigger tables, but the native functions are enough for lead-time and SLA percentile reporting.

### Interview angle
> [!question] How it is asked
> "How would you identify outlier orders, or report the 90th percentile delivery time?"

> [!tip] Strong answer includes
> - PERCENTILE.INC/EXC difference and interpolation
> - IQR fences (1.5 x IQR) for outliers; mention boxplot
> - Why percentiles suit skewed operations data (SLA reporting)
> - Treat outliers (investigate, not auto-delete)

---

## 11. ⭐ Advanced: SUMPRODUCT and Array Logic (OR conditions)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
`SUMIFS` and `COUNTIFS` only do AND logic across criteria ranges. `SUMPRODUCT` multiplies and sums arrays, so Boolean arrays can express any logic without Ctrl+Shift+Enter:

- AND: multiply (`*`); OR: add (`+`) then test `>0`; NOT: `1-` or `<>`.
- Convert TRUE/FALSE to 1/0 with `--` or by multiplying.
- Weighted averages: `=SUMPRODUCT(values,weights)/SUM(weights)`.
- Cross-range comparisons and dates: `=SUMPRODUCT((MONTH(dates)=4)*(amounts))`.

Pattern: `=SUMPRODUCT(--(((cond1)+(cond2))>0), sum_range)`. Mind range sizes (must match) and avoid whole-column references (very slow). In 365, `FILTER` plus `SUM` gives equally readable alternatives: `=SUM(FILTER(C2:C7,(A2:A7="East")+(B2:B7="B")))`. Note that `SUMPRODUCT` with text in the value arrays returns zeros unless converted.

### Example
Sample data: sum of sales where Region is East **or** Product is B. Matching rows: East A 100, East B 150, West B 80, East A 130. Formula: `=SUMPRODUCT(--(((A2:A7="East")+(B2:B7="B"))>0),C2:C7)` returns 100 + 150 + 80 + 130 = **460**. Note East-and-B (150) satisfies both conditions, so the `>0` test prevents double-counting it (without it, 150 would be counted twice for 610).

### In the news
See news box. Complex multi-condition logic is where native array logic is verifiable, unlike a prompt-based AI function.

### Interview angle
> [!question] How it is asked
> "SUMIFS handles AND. How do you sum with OR conditions, or compute a weighted average?"

> [!tip] Strong answer includes
> - `*` as AND, `+` as OR, `>0` to avoid double counting
> - Weighted average pattern
> - Performance caution on big ranges; FILTER/SUM alternative in 365
> - Test the formula on a small hand-checked sample

---

## 12. ⭐ Advanced: SUBTOTAL, AGGREGATE and Summaries on Filtered Data
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Normal `SUM`, `AVERAGE`, `COUNT` include hidden/filtered rows, which misleads when a user filters a table.

- `=SUBTOTAL(function_num, ref1, ...)`: codes 1-11 include manually hidden rows; **101-111 ignore hidden rows**; both ignore rows hidden by a filter and ignore other SUBTOTALs inside the range. Examples: `109` = SUM, `101` = AVERAGE, `102` = COUNT, `103` = COUNTA, `104` = MAX, `105` = MIN. The Table "Total Row" uses SUBTOTAL.
- `=AGGREGATE(function_num, options, array, [k])`: 19 functions (1-13 for references, 14-19 for arrays with k such as LARGE=14, SMALL=15, PERCENTILE.INC=16, QUARTILE.INC=17); **options** choose what to ignore: `6` = errors, `5` = hidden rows, `7` = hidden rows and errors. It can do conditional calculations via division trick: `=AGGREGATE(14,6,C2:C7/(A2:A7="West"),1)` returns the largest West value (division by zero errors are ignored).
- Use `OPTIONS 6` to sum a column that contains errors: `=AGGREGATE(9,6,range)`.

### Example
Table of 6 sales (100, 150, 200, 120, 80, 130). Filter to Region = West: visible rows 200, 120, 80. `=SUM(C2:C7)` still shows 780, but `=SUBTOTAL(109,C2:C7)` shows **400**. `=AGGREGATE(14,6,C2:C7/(A2:A7="West"),1)` returns **200**, the highest West value, without MAXIFS or an array entry.

### In the news
See news box. A filter-aware total is another case where a deterministic function must be trusted over AI-written summaries.

### Interview angle
> [!question] How it is asked
> "My total does not change when I filter the table. Why, and how do I fix it?"

> [!tip] Strong answer includes
> - SUM includes hidden rows; use SUBTOTAL(109) (or 9) for filtered data
> - Difference between 1-11 and 101-111 function numbers
> - AGGREGATE for ignoring errors and conditional k-th values
> - Table Total Row uses SUBTOTAL automatically

---
## 🔗 Go deeper: expansion notes
- [[187 Excel Interview Problem Bank & Case Exercises|Excel Interview Problem Bank & Case Exercises]]
- [[188 Financial Modelling in Excel|Financial Modelling in Excel]]
- [[189 VBA, Macros & Office Scripts Basics|VBA, Macros & Office Scripts Basics]]
