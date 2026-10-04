---
tags: [excel-advanced, tier1]
area: Excel Advanced
topic: "Array & Dynamic Array Functions"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Array & Dynamic Array Functions

⬅ [[073 Text & Date Functions]] · [[_Index - Excel Advanced|Excel Advanced]] · [[075 Pivot Tables & Power Query]] ➡

> **Area:** Excel Advanced · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. SUMPRODUCT]]
2. [[#2. Legacy Array Formula (Ctrl+Shift+Enter)]]
3. [[#3. FILTER Function (365)]]
4. [[#4. SORT / SORTBY]]
5. [[#5. UNIQUE Function]]
6. [[#6. SEQUENCE]]
7. [[#7. XLOOKUP with Arrays]]
8. [[#8. VSTACK / HSTACK (365)]]
9. [[#9. BYROW / BYCOL]]
10. [[#10. LAMBDA Function]]
11. [[#11. ⭐ Advanced: LET, MAP, REDUCE and the Spill-Range Operator]]
12. [[#12. ⭐ Advanced: Performance and Audit of Array Models]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Excel adds AI agents on top of the formula engine
> **Agent Mode in Excel (GA Jan 2026).** Microsoft announced that Agent Mode in Excel, part of Microsoft 365 Copilot, became generally available on Windows on 27 Jan 2026, with Mac rolling out over the following days. It builds and edits spreadsheets from natural-language goals, so reviewing the formulas it writes (often dynamic-array formulas) is now a core skill. ([Microsoft Tech Community](https://techcommunity.microsoft.com/blog/excelblog/agent-mode-in-excel-is-now-generally-available-on-desktop/4457408))
> 
> **COPILOT() function (Aug 2025, retiring Sep 2026).** A `=COPILOT("prompt", range)` function was announced on 19 Aug 2025 for Beta Channel users and, per The Register, retires on 14 Sep 2026 while still in preview; Microsoft points users to the Copilot side pane. Dynamic arrays (FILTER, LAMBDA) remain the deterministic, auditable route. ([GeekWire](https://www.geekwire.com/2025/excel-formula-meets-ai-prompt-microsoft-brings-new-copilot-function-to-spreadsheet-cells/), [The Register](https://www.theregister.com/ai-and-ml/2026/08/17/excels-copilot-function-is-headed-for-the-recycle-bin/5288327))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. SUMPRODUCT
> 🔴 Tier 1 · _Tracker hint:_ =SUMPRODUCT(A1:A10,B1:B10); weighted avg: =SUMPRODUCT(wts,vals)/SUM(wts); multi-criteria sum

### Definition
`SUMPRODUCT` multiplies corresponding elements of equal-sized arrays and sums the products, evaluating arrays natively without Ctrl+Shift+Enter.

$$\text{SUMPRODUCT}(a,b)=\sum_i a_i b_i$$

Three workhorse uses:
- **Total value:** `=SUMPRODUCT(Qty, Price)` avoids a helper column.
- **Weighted average:** `=SUMPRODUCT(wts, vals)/SUM(wts)`.
- **Multi-criteria sum/count:** boolean tests become 1/0 when multiplied: `=SUMPRODUCT((Region="North")*(Month="Jan")*Sales)`. Count: `=SUMPRODUCT((Region="North")*(Sales>1000))`. OR logic uses `+`. Use `--` to coerce booleans when passing a single array: `=SUMPRODUCT(--(A2:A100>50))`.

Arrays must have the same dimensions or you get `#VALUE!`. It handles OR conditions and wildcard-free partial logic that SUMIFS cannot, but is slower on very large ranges. Text cells in numeric arrays are treated as 0.

### Example
Supplier scorecard: scores 90, 80, 70 with weights 0.5, 0.3, 0.2. $\text{SUMPRODUCT}=0.5\times90+0.3\times80+0.2\times70=45+24+14=83$; weights sum to 1.0, so weighted score = 83. Stock value: Qty {10, 20, 5}, Price {100, 50, 200}: $1000+1000+1000=3000$.

### In the news
See news box. Agent-generated spreadsheets frequently rely on SUMPRODUCT for weighted metrics; you must be able to audit it.

### Interview angle
> [!question] How it is asked
> "Compute a weighted average without helper columns" or "SUMIFS vs SUMPRODUCT: when do you use each?"

> [!tip] Strong answer includes
> - Definition and the weighted average formula
> - Boolean array multiplication for multi-criteria (AND with `*`, OR with `+`)
> - Dimension match and the `--` coercion
> - SUMIFS is faster and clearer for simple AND criteria; SUMPRODUCT for OR/complex logic

---

## 2. Legacy Array Formula (Ctrl+Shift+Enter)
> 🔴 Tier 1 · _Tracker hint:_ {=SUM(IF(range='X',values,0))}; now replaced by dynamic arrays

### Definition
Before Excel 365, formulas that process arrays element-by-element (e.g. `IF` over a range) had to be confirmed with **Ctrl+Shift+Enter (CSE)**, shown with curly braces `{=...}` (typed braces do not work). Such formulas return a single value or fill a pre-selected range.

```excel
{=SUM(IF(A2:A100="North", B2:B100, 0))}      -- sum for North
{=MAX(IF(A2:A100="North", B2:B100))}          -- MAXIFS substitute
{=INDEX(C:C, MATCH(1, (A:A="X")*(B:B="Y"), 0))} -- two-criteria lookup
{=AVERAGE(IF(ISNUMBER(B2:B100), B2:B100))}
```
In Excel 365/2021 the engine evaluates arrays natively: the same formula entered with plain Enter works and can **spill**. Legacy CSE formulas still open and work; you will meet them in older company models. Weaknesses: easy to forget CSE, hard to audit, cannot be edited without re-confirming, slower on large ranges. Modern equivalents: SUMIFS, MAXIFS, FILTER, XLOOKUP.

### Example
Sales: A = region (North, South, North), B = value (100, 200, 300). `{=SUM(IF(A2:A4="North",B2:B4,0))}`: IF returns {100, 0, 300}; SUM = 400. In 365 enter the same without braces, or use `=SUMIFS(B2:B4,A2:A4,"North")` = 400.

### In the news
See news box. Many legacy models audited by agents or consultants still contain CSE formulas; recognising them avoids breaking them.

### Interview angle
> [!question] How it is asked
> "What is an array formula and what does Ctrl+Shift+Enter do?"

> [!tip] Strong answer includes
> - Array vs scalar evaluation
> - Curly braces and legacy CSE; native evaluation in 365
> - A concrete two-criteria lookup example
> - Prefer SUMIFS/MAXIFS/FILTER now, but be able to read legacy formulas

---

## 3. FILTER Function (365)
> 🔴 Tier 1 · _Tracker hint:_ =filter(data, condition, [if_empty]); =filter(A:C, B:B='north')

### Definition
```excel
=FILTER(array, include, [if_empty])
```
Returns the rows (or columns) of `array` where `include` is TRUE, as a **spilled** dynamic array. Combine conditions with `*` (AND) and `+` (OR):

```excel
=FILTER(A2:D100, (B2:B100="North")*(D2:D100>1000), "No match")
=FILTER(A2:D100, (B2:B100="North")+(B2:B100="West"))
```
The result updates automatically when data changes; reference the spill range with `F2#`. Wrap in other functions: `=SUM(FILTER(D2:D100,B2:B100="North"))`, `=SORT(FILTER(...))`, `=COUNTA(UNIQUE(FILTER(...)))`. Avoid whole-column references inside arrays (slow); use Tables (`Sales[Region]`). Errors: `#CALC!` when empty and no `if_empty`; `#SPILL!` when output cells are blocked. Available in Microsoft 365 and Excel 2021+.

### Example
Table of orders: rows (Pune, 500), (Nashik, 1200), (Pune, 1500). `=FILTER(A2:B4, B2:B4>1000)` returns rows 2 and 3 (Nashik 1200, Pune 1500). `=SUM(FILTER(B2:B4, A2:A4="Pune"))` = 500 + 1500 = 2000.

### In the news
See news box. Agent Mode relies on such dynamic functions to build live reports, so reading FILTER logic matters for review.

### Interview angle
> [!question] How it is asked
> "Without a pivot, how do you get a live list of overdue orders for one supplier?"

> [!tip] Strong answer includes
> - Syntax and the `if_empty` argument
> - AND with `*`, OR with `+`
> - Spill behaviour, `#SPILL!` and the `#` operator
> - Compare with AutoFilter (manual) and Power Query (heavier)

---

## 4. SORT / SORTBY
> 🔴 Tier 1 · _Tracker hint:_ =sort(array,[sort_index],[sort_order]); =sortby(data,COL1,1,COL2,-1)

### Definition
```excel
=SORT(array, [sort_index], [sort_order], [by_col])   -- order: 1 ascending (default), -1 descending
=SORTBY(array, by_array1, [order1], by_array2, [order2], ...)
```
`SORT` sorts by a column number inside the array. `SORTBY` sorts by any range, even one not included in the output, and supports multiple keys. Examples: top-down ranking `=SORT(A2:C100,3,-1)`; sort by region ascending then sales descending `=SORTBY(A2:C100, B2:B100, 1, C2:C100, -1)`. Combine: `=TAKE(SORT(A2:C100,3,-1),5)` gives a live top-5 list; `=SORT(FILTER(...))`. Results spill and update automatically, unlike Data > Sort which is a one-time action.

### Example
Data (Item, Revenue): A 40, B 90, C 60. `=SORT(A2:B4,2,-1)` returns B 90, C 60, A 40. Top-2: `=TAKE(SORT(A2:B4,2,-1),2)` returns B 90, C 60. This is the first step of an ABC analysis.

### In the news
See news box. Live-sorted outputs are typical in AI-built dashboards.

### Interview angle
> [!question] How it is asked
> "How do you build a dynamic top-10 customer list that updates itself?"

> [!tip] Strong answer includes
> - SORT vs SORTBY and multi-key sort
> - Descending is `-1`
> - Combine with FILTER and TAKE
> - Contrast with static Data > Sort

---

## 5. UNIQUE Function
> 🔴 Tier 1 · _Tracker hint:_ =unique(range, [by_col], [exactly_once]); dynamic unique list

### Definition
```excel
=UNIQUE(array, [by_col], [exactly_once])
```
Returns distinct values (or rows). `by_col` TRUE compares columns; `exactly_once` TRUE returns only values that appear **once** (not merely distinct). Replaces the old Remove Duplicates and complex `INDEX/MATCH/COUNTIF` formulas. Useful patterns:

- Distinct count: `=COUNTA(UNIQUE(A2:A100))` (or `ROWS(UNIQUE(...))`)
- Sorted list for a dropdown: `=SORT(UNIQUE(A2:A100))`, then Data Validation list source `=F2#`
- Unique combos: `=UNIQUE(A2:B100)` (compares both columns per row)
- Sum per unique: `=SUMIFS(C:C, A:A, F2#)` spills per-item totals

Blank cells appear as 0; wrap with `FILTER(range, range<>"")`. Case-insensitive.

### Example
Supplier column: Tata, Bharat, Tata, Mahindra, Bharat. `=UNIQUE(A2:A6)` returns Tata, Bharat, Mahindra (3 distinct). `=UNIQUE(A2:A6,,TRUE)` returns only Mahindra (appears exactly once). Distinct supplier count = 3.

### In the news
See news box. Dynamic lists feed AI-assisted summaries; UNIQUE is the natural source for category lists.

### Interview angle
> [!question] How it is asked
> "How do you count distinct customers in a transaction list?"

> [!tip] Strong answer includes
> - `COUNTA(UNIQUE())` or `ROWS`
> - Difference between distinct and exactly-once
> - Dropdown from a spill range via `#`
> - Alternatives: Pivot (distinct count via data model), Remove Duplicates (static)

---

## 6. SEQUENCE
> 🔴 Tier 1 · _Tracker hint:_ =sequence(rows,cols,start,step); generate number sequences dynamically

### Definition
```excel
=SEQUENCE(rows, [columns], [start], [step])
```
Generates a spilled grid of numbers. `=SEQUENCE(5)` gives 1 to 5; `=SEQUENCE(3,4)` fills a 3x4 grid with 1 to 12; `=SEQUENCE(12,1,0,5)` gives 0, 5, 10... Typical uses: row numbers, calendars, and building date series with `EDATE`: `=EDATE(DATE(2026,4,1), SEQUENCE(12,1,0))` yields the 12 fiscal-year month starts. Combine with `INDEX` to reshape or pick every nth row: `=INDEX(A2:A100, SEQUENCE(10,,1,3))` returns rows 1, 4, 7, ... Combine with `LAMBDA`/`BYROW` for loops. Use `ROWS(range)` to size dynamically: `=SEQUENCE(ROWS(A2:A100))`. Replaces dragging fill handles and `ROW()-1` hacks.

### Example
Rolling 6-month forecast headers: `=EOMONTH(TODAY(), SEQUENCE(1,6,0))` returns 6 consecutive month-ends across a row. Amortisation periods: `=SEQUENCE(60)` for a 5-year monthly loan.

### In the news
See news box. Agent Mode-style tools generate such helper arrays routinely.

### Interview angle
> [!question] How it is asked
> "Generate a list of the next 12 month-ends with one formula."

> [!tip] Strong answer includes
> - All four arguments
> - Combine with EDATE/EOMONTH/INDEX
> - Spills, no manual drag
> - Mention volatility if TODAY() is used

---

## 7. XLOOKUP with Arrays
> 🔴 Tier 1 · _Tracker hint:_ =xlookup(A2,lookup,choosecols(return,1,3)) — return multiple columns

### Definition
```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```
Because `return_array` can be multi-column, one XLOOKUP spills several fields: `=XLOOKUP(A2, Items[SKU], B2:C50)`. Use `CHOOSECOLS(array, 1, 3)` to pick non-adjacent columns. XLOOKUP also accepts **array lookup values**: `=XLOOKUP(F2:F10, A:A, B:B)` looks up many values at once. Two-criteria lookup: `=XLOOKUP(1, (A:A="X")*(B:B="Y"), C:C)` or concatenated keys. `match_mode` options: 0 exact, -1 exact or next smaller, 1 exact or next larger, 2 wildcard. `search_mode -1` finds the **last** match. Unlike `VLOOKUP`, it looks left, defaults to exact match and has `if_not_found`. Available in Excel 2021 and 365.

### Example
Price table columns: SKU, Description, Price. `=XLOOKUP("S102", A2:A50, B2:C50)` returns Description and Price side by side. Tiered freight: `=XLOOKUP(weight, Slab[Min], Slab[Rate], , -1)` returns the rate for the highest slab minimum not above the weight (e.g. 42 kg with slabs 0, 25, 50 returns the 25 kg rate).

### In the news
See news box. Agent Mode often produces XLOOKUP/XMATCH lookups; knowing their match modes helps catch silent errors.

### Interview angle
> [!question] How it is asked
> "VLOOKUP vs XLOOKUP: why switch? How do you return multiple columns?"

> [!tip] Strong answer includes
> - Left lookup, default exact, `if_not_found`, search/match modes
> - Multi-column spill and CHOOSECOLS
> - Approximate tier lookup with `-1`
> - Version caveat; INDEX/MATCH fallback

---

## 8. VSTACK / HSTACK (365)
> 🔴 Tier 1 · _Tracker hint:_ =vstack(table1,table2) — vertical combine; replaces complex array formulas

### Definition
```excel
=VSTACK(array1, [array2], ...)   -- stack vertically, appending rows
=HSTACK(array1, [array2], ...)   -- stack horizontally, appending columns
```
Mismatched widths are padded with `#N/A` (wrap in `IFERROR`, or use `TAKE/DROP`). Consolidate monthly sheets without Power Query: `=VSTACK(Jan!A2:D100, Feb!A2:D100, Mar!A2:D100)`; remove blanks with `FILTER(result, INDEX(result,,1)<>"")`. Add a header: `=VSTACK({"SKU","Qty"}, data)`. Build a table with computed columns: `=HSTACK(A2:A10, B2:B10*C2:C10)`. Related: `TOCOL`, `TOROW`, `WRAPROWS`, `TAKE`, `DROP`, `EXPAND`. For many files or refresh-from-folder, Power Query Append is more robust; VSTACK suits a handful of in-workbook ranges.

### Example
Q1 sheets have 3 rows each (Jan 3, Feb 3, Mar 3) with identical columns. `=VSTACK(Jan!A2:C4, Feb!A2:C4, Mar!A2:C4)` spills 9 rows. Then `=SUM(INDEX(result,,3))` totals column 3 across all months.

### In the news
See news box. Consolidation of many sheets is a common agent task; VSTACK is the formula route, Power Query the scalable one.

### Interview angle
> [!question] How it is asked
> "How would you combine 12 monthly sheets into one table?"

> [!tip] Strong answer includes
> - VSTACK/HSTACK and padding with #N/A
> - Compare with Power Query Append (scales, refreshes) and manual copy-paste (error-prone)
> - Handling headers and blank rows
> - Mention version dependence

---

## 9. BYROW / BYCOL
> 🔴 Tier 1 · _Tracker hint:_ =byrow(range,lambda(row,SUM(row))); apply function row-by-row

### Definition
```excel
=BYROW(array, LAMBDA(row, calculation))   -- returns one result per row
=BYCOL(array, LAMBDA(col, calculation))   -- returns one result per column
```
They apply a LAMBDA to each row or column and spill the results, making per-row aggregates that require a single scalar output (so `MAP`, `REDUCE`, `SCAN` handle other shapes). Example: row max `=BYROW(B2:E10, LAMBDA(r, MAX(r)))`; rows with any stock-out `=BYROW(B2:E10, LAMBDA(r, COUNTIF(r,0)>0))`; per-column average `=BYCOL(B2:E10, LAMBDA(c, AVERAGE(c)))`. The LAMBDA must return a single value per row/column. Related: `MAP(array, LAMBDA(x, ...))` applies element by element; `SCAN` returns running totals; `REDUCE` collapses to one value. Use these to avoid helper columns and fragile `Ctrl+Shift+Enter` constructs.

### Example
Weekly demand for 3 SKUs over 4 weeks: rows (10,20,30,40), (5,5,5,5), (0,10,0,10). `=BYROW(B2:E4, LAMBDA(r, SUM(r)))` returns 100, 20, 20. Running total with `=SCAN(0, B2:E2, LAMBDA(a,v, a+v))` on row 1 gives 10, 30, 60, 100.

### In the news
See news box. LAMBDA-family functions are what agent-built models call when logic must be reused across rows.

### Interview angle
> [!question] How it is asked
> "How can you compute a per-row result like the max of several columns without helper columns?"

> [!tip] Strong answer includes
> - Syntax of BYROW with LAMBDA
> - Single-value output rule; MAP/SCAN/REDUCE alternatives
> - Readability trade-off versus a helper column
> - Version note (365)

---

## 10. LAMBDA Function
> 🔴 Tier 1 · _Tracker hint:_ =lambda(x,y,x^2+y^2)(3,4); create custom reusable functions in excel

### Definition
`LAMBDA` lets you define custom functions using Excel formulas, with no VBA.

```excel
=LAMBDA(x, y, x^2 + y^2)(3, 4)    -- inline call returns 25
```
For reuse, save it in **Formulas > Name Manager** with a name, e.g. `HYP` = `=LAMBDA(x,y,SQRT(x^2+y^2))`; then `=HYP(3,4)` returns 5. Optional parameters go in square brackets. Use `LET` to name intermediate results inside formulas and speed them up:

```excel
=LET(rev, SUM(B2:B10), cost, SUM(C2:C10), (rev-cost)/rev)
```
LAMBDA supports recursion (a named LAMBDA can call itself) and combines with MAP/BYROW/REDUCE. Benefits: central logic, easier updates, readable names. Risks: shared workbooks depend on the name definition; test thoroughly; 365-only.

### Example
Define `EOQ` = `=LAMBDA(D,S,H,SQRT(2*D*S/H))`. For annual demand D = 12,000, order cost S = ₹500, holding cost H = ₹10: $\sqrt{2\times12000\times500/10}=\sqrt{1{,}200{,}000}\approx1095$ units. `=EOQ(12000,500,10)` returns about 1095.4.

### In the news
See news box. As AI generates formulas, reusable named LAMBDAs give teams controlled, auditable logic.

### Interview angle
> [!question] How it is asked
> "Have you used LAMBDA or LET? Why would you?"

> [!tip] Strong answer includes
> - Syntax and the immediate-call test
> - Naming in Name Manager for reuse
> - LET for readability and speed
> - A business example (EOQ, weighted score) and the maintenance caveat

---

## 11. ⭐ Advanced: LET, MAP, REDUCE and the Spill-Range Operator
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Advanced dynamic-array patterns used in modelling interviews:

```excel
=LET(name1, value1, [name2, value2...], calculation)
=MAP(array, LAMBDA(x, ...))             -- element-wise, same shape output
=REDUCE(initial, array, LAMBDA(acc, x, ...))
=SCAN(initial, array, LAMBDA(acc, x, ...))  -- running results
```
`F2#` refers to the whole spill range from F2, so downstream formulas resize automatically. `LET` evaluates a repeated sub-expression once, making formulas faster and readable. Typical pattern: LET holds a FILTERed table, then computes several metrics. Also `GROUPBY` and `PIVOTBY` (newer 365 functions) create pivot-style summaries by formula. `#SPILL!` appears when a spill range is blocked or in a Table (spills are not allowed inside Tables). `@` forces implicit intersection.

### Example
Running stock balance: opening 100, daily net movements in B2:B6 = {+50, -30, -80, +20, -10}. `=SCAN(100, B2:B6, LAMBDA(a,v, a+v))` returns 150, 120, 40, 60, 50. The third day dips to 40, which would trigger a reorder if ROP = 50.

### In the news
See news box. Agent Mode writes such constructs; interviewers increasingly ask candidates to explain or fix AI-generated formulas.

### Interview angle
> [!question] How it is asked
> "Explain what this LET/MAP formula does" or "How do you compute a running balance without dragging formulas?"

> [!tip] Strong answer includes
> - What LET buys (naming, single evaluation)
> - SCAN/REDUCE/MAP distinctions
> - Spill operator `#` and typical errors
> - Honesty about 365-only features and a fallback

---

## 12. ⭐ Advanced: Performance and Audit of Array Models
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Large array formulas can slow a workbook. Good practice:
- Use **Tables** and structured references rather than whole-column references (`A:A`) inside `SUMPRODUCT`, `FILTER`, `XLOOKUP` arrays.
- Prefer `SUMIFS/COUNTIFS` for simple criteria (they are optimised); reserve `SUMPRODUCT` for OR logic.
- Avoid volatile functions (`OFFSET`, `INDIRECT`, `TODAY`) inside big arrays.
- Use `LET` to avoid recomputing the same sub-array.
- Check calculation mode (Automatic except Data Tables) and use **Formulas > Evaluate Formula** and **Trace Precedents** to audit.
- Document spill outputs with labels and keep space beneath them.
- Replace long chains with Power Query for 100k+ rows or multiple files.

Interviewers value the judgment to choose the right tool, not only the newest function.

### Example
A model uses `=SUMPRODUCT((A:A="North")*(B:B>0)*C:C)` over whole columns, about 1,048,576 rows x 3 arrays. Rewriting as `=SUMIFS(C:C,A:A,"North",B:B,">0")` computes the same total much faster, because SUMIFS stops at the used range. Better still, use `Sales[Value]` with the Table.

### In the news
See news box. AI tools make complex formulas cheap to generate, so formula review and performance hygiene become more valuable.

### Interview angle
> [!question] How it is asked
> "Your Excel model takes two minutes to recalculate. What do you do?"

> [!tip] Strong answer includes
> - Identify volatile and whole-column formulas
> - Replace with SUMIFS, Tables, LET
> - Manual calc mode while editing; Evaluate Formula to debug
> - Move heavy transformation to Power Query or a database

---
## 🔗 Go deeper: expansion notes
- [[187 Excel Interview Problem Bank & Case Exercises|Excel Interview Problem Bank & Case Exercises]]
- [[188 Financial Modelling in Excel|Financial Modelling in Excel]]
- [[189 VBA, Macros & Office Scripts Basics|VBA, Macros & Office Scripts Basics]]
