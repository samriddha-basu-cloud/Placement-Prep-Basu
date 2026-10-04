---
tags: [excel-advanced, tier1]
area: Excel Advanced
topic: "Lookup & Reference Functions"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Lookup & Reference Functions

⬅ [[070 Foundations & Navigation]] · [[_Index - Excel Advanced|Excel Advanced]] · [[072 Logical & Statistical Functions]] ➡

> **Area:** Excel Advanced · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. VLOOKUP]]
2. [[#2. HLOOKUP]]
3. [[#3. INDEX + MATCH]]
4. [[#4. XLOOKUP (Excel 365)]]
5. [[#5. Two-Way Lookup]]
6. [[#6. MATCH Function]]
7. [[#7. OFFSET Function]]
8. [[#8. CHOOSE Function]]
9. [[#9. INDIRECT]]
10. [[#10. IFERROR / IFNA]]
11. [[#11. ⭐ Advanced: Dynamic Array Functions (FILTER, SORT, UNIQUE, XMATCH)]]
12. [[#12. ⭐ Advanced: Lookup Performance and Approximate-Match Binary Search]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Excel's lookup layer is being reshaped by Python and AI, but XLOOKUP/INDEX-MATCH logic still underpins both
> **Python in Excel became generally available** (Microsoft: "now generally available" for Windows users of Microsoft 365 Business and Enterprise, built with Anaconda; a December 2024 changelog entry said Excel for the web would follow from early 2025). Python merges and lookups (`pandas.merge`) are the code-based cousins of VLOOKUP/XLOOKUP, and `=PY()` cells can read the same tables. ([Microsoft Tech Community](https://techcommunity.microsoft.com/blog/excelblog/python-in-excel-%E2%80%93-available-now/4240212); [Petri M365 changelog, Dec 2024](https://petri.com/microsoft-changelog/m365-changelog-microsoft-excel-for-the-web-python-in-excel-will-be-generally-available-starting-in-early-2025-dec-19-2024/))
>
> **The COPILOT function (announced August 2025) was short-lived.** It let a formula call AI with a prompt. Microsoft advised against using it for numerical calculations or for retrieving information already in the workbook, and TechRadar reports it is being discontinued from 14 September 2026. For lookups, the lesson is that deterministic functions (exact-match XLOOKUP, INDEX/MATCH) remain the reliable way to retrieve data. ([Microsoft Tech Community, Aug 2025](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/bring-ai-to-your-formulas-with-the-copilot-function-in-excel/4443487); [TechRadar](https://www.techradar.com/pro/microsoft-is-dropping-its-excel-copilot-function-after-only-a-year-and-without-ever-getting-a-full-public-launch))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. VLOOKUP
> 🔴 Tier 1 · _Tracker hint:_ =VLOOKUP(value, table, col_index, 0); FALSE()=exact match; limitations: left-only, slow on large data

### Definition
`=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])` searches the **first column** of `table_array` for `lookup_value` and returns the value in column number `col_index_num` of the same row.

- `range_lookup = FALSE` (or `0`): **exact match**. Use this almost always.
- `TRUE` (or omitted): **approximate match**, requires the first column sorted ascending, returns the largest value less than or equal to the lookup. Used for slabs (tax, commission, grade bands). Omitting the argument is the classic bug: wrong results without any error.

Limitations: (1) lookup column must be leftmost; (2) the column index is a hard-coded number, so inserting a column breaks it (use `MATCH` to compute it, or XLOOKUP); (3) returns the first match only; (4) slower on large data with exact match (linear scan); (5) text-vs-number mismatches and trailing spaces give `#N/A`; (6) default is case-insensitive; (7) wildcards `*` and `?` work with text.

Lock the table with absolute references: `=VLOOKUP(E2,$A$2:$C$100,3,FALSE)`.

### Example
Product table `A2:C6`: S101 Bolt 12; S102 Nut 8; S103 Washer 3; S104 Screw 5; S105 Rivet 7 (SKU, Name, Price). `=VLOOKUP("S103",A2:C6,3,FALSE)` returns 3. Approximate match: commission bands `0 to 0%`, `50,000 to 2%`, `1,00,000 to 5%`, `2,00,000 to 8%`; sales of Rs 1,25,000: `=VLOOKUP(125000,band_table,2,TRUE)` returns 5%, so commission $=125000\times0.05=$ Rs 6,250.

### In the news
See news box. VLOOKUP remains everywhere in legacy workbooks, but new work should use XLOOKUP, and `pandas.merge` is the equivalent when the data moves into Python in Excel.

### Interview angle
> [!question] How it is asked
> "Explain VLOOKUP and its limitations. How would you look up a value to the left?"

> [!tip] Strong answer includes
> - Four arguments, exact vs approximate match and the sorted-data requirement
> - Limitations (leftmost key, hard-coded column index, first match, performance)
> - Alternatives: INDEX+MATCH (any direction), XLOOKUP (modern)
> - Error handling (`IFNA`) and data cleaning (TRIM, consistent types)

---

## 2. HLOOKUP
> 🔴 Tier 1 · _Tracker hint:_ =HLOOKUP(value, table, row_index, 0); horizontal version of vlookup

### Definition
`=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])` is VLOOKUP rotated: it searches the **first row** of `table_array` and returns a value from the specified row of the matching column. Use when data is laid out with periods or categories across columns (months across the top, KPI rows below). The same rules apply: `FALSE` for exact match; `TRUE` requires the first row sorted ascending.

Limits are the same as VLOOKUP (top-row key, hard-coded row index, first match). Because most analysis data should be in columns (tidy format), HLOOKUP is relatively rare; in modern Excel `XLOOKUP` works horizontally or vertically with the same syntax, and `INDEX/MATCH` can also handle either direction. Transposing the data (Paste Special, Transpose, or the `TRANSPOSE` function) is another approach.

### Example
Months across row 1 (`B1:D1` = Jan, Feb, Mar), Sales in row 2 (`B2:D2` = 120, 135, 150), Cost in row 3 (`B3:D3` = 80, 90, 95), table `A1:D3`. `=HLOOKUP("Feb",B1:D3,2,FALSE)` returns 135 (row 2 of the table). The equivalent XLOOKUP: `=XLOOKUP("Feb",B1:D1,B2:D2)`. Margin for February: `=HLOOKUP("Feb",B1:D3,2,0)-HLOOKUP("Feb",B1:D3,3,0)` gives $135-90=45$.

### In the news
Not tied to a specific news item. See news box: the direction-agnostic XLOOKUP largely replaces HLOOKUP in new workbooks.

### Interview angle
> [!question] How it is asked
> "When would you use HLOOKUP instead of VLOOKUP?"

> [!tip] Strong answer includes
> - Data oriented horizontally (keys in the first row); row_index instead of col_index
> - Same exact/approximate rules and limits
> - Prefer XLOOKUP or INDEX/MATCH; tidy data is better arranged vertically
> - Mention the TRANSPOSE alternative

---

## 3. INDEX + MATCH
> 🔴 Tier 1 · _Tracker hint:_ =INDEX(return_col, MATCH(lookup_val, lookup_col, 0)); left lookup; two-way lookup

### Definition
Two functions combined:

- `MATCH(lookup_value, lookup_array, 0)` returns the **position** of the value in a one-dimensional range.
- `INDEX(array, row_num, [column_num])` returns the value at that position.

`=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))`

Advantages over VLOOKUP: lookup column can be **left or right** of the return column; no hard-coded column index (insert columns safely, references adjust); separate ranges are lighter than a whole table; the same MATCH can feed several INDEX calls (helper column of positions, faster); works in any direction; can do **two-way** lookups. Compared with XLOOKUP, it works in all Excel versions (2007 onward).

Multi-criteria lookup (older Excel): `=INDEX(C2:C100,MATCH(1,(A2:A100=E1)*(B2:B100=F1),0))` evaluates arrays (Ctrl+Shift+Enter in pre-365 Excel; spills natively in 365). Or concatenate a helper key column.

### Example
Same product table (`A2:A6` SKU, `B2:B6` Name, `C2:C6` Price). Find the SKU for the name "Nut" (a leftward lookup VLOOKUP cannot do): `=INDEX(A2:A6,MATCH("Nut",B2:B6,0))` returns "S102", because MATCH returns 2 (Nut is second) and INDEX returns the second item of `A2:A6`. Price of Screw: `=INDEX(C2:C6,MATCH("Screw",B2:B6,0))` returns 5.

### In the news
See news box. Because Microsoft's own AI formula function was withdrawn and Python in Excel is cell-based, INDEX/MATCH knowledge remains a safe, portable foundation across every Excel version.

### Interview angle
> [!question] How it is asked
> "Why do many analysts prefer INDEX-MATCH over VLOOKUP? Write a left lookup."

> [!tip] Strong answer includes
> - Formula structure and what each part returns
> - Four advantages (any direction, robust to column insertion, performance, two-way)
> - Compare with XLOOKUP and when each is available
> - Handling duplicates and `#N/A` with IFNA

---

## 4. XLOOKUP (Excel 365)
> 🔴 Tier 1 · _Tracker hint:_ =xlookup(value, lookup_array, return_array, [if_not_found]); replaces vlookup

### Definition
`=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`

- **Default is exact match** (no more forgetting `FALSE`).
- `if_not_found`: built-in error handling, e.g. `"Not found"`.
- `match_mode`: `0` exact (default), `-1` exact or next smaller, `1` exact or next larger, `2` wildcard.
- `search_mode`: `1` first to last (default), `-1` last to first (find the **latest** entry), `2` binary search ascending, `-2` binary descending.
- Looks **left or right**, vertical or horizontal, uses separate ranges (insert-column safe).
- **Returns arrays**: `return_array` can be several columns, and the result spills: `=XLOOKUP(E2,A2:A100,B2:D100)`.
- Available in Excel 2021, Microsoft 365 and Excel for the web; not in Excel 2019 or earlier (use INDEX/MATCH if files must work there).

Combine two XLOOKUPs to get a range: `=SUM(XLOOKUP(start,dates,vals):XLOOKUP(end,dates,vals))`. Multi-criteria: `=XLOOKUP(1,(A2:A100=E1)*(B2:B100=F1),C2:C100)`.

### Example
Using the product table: `=XLOOKUP("S104",A2:A6,C2:C6,"Not found")` returns 5; `=XLOOKUP("S999",A2:A6,C2:C6,"Not found")` returns "Not found". Commission band with approximate match: `=XLOOKUP(125000,band_min,band_pct,0,-1)` returns the 5% row (exact or next smaller threshold 1,00,000), even if the table is unsorted. Last occurrence: `=XLOOKUP(E2,A:A,C:C,,0,-1)` retrieves the most recent price for repeated SKUs.

### In the news
See news box. XLOOKUP is the modern default Microsoft documents for lookups; with Python in Excel, `pandas.merge` plays the same role for table joins.

### Interview angle
> [!question] How it is asked
> "What are the advantages of XLOOKUP over VLOOKUP?"

> [!tip] Strong answer includes
> - Exact match by default, left/right/horizontal lookup, `if_not_found`
> - match_mode and search_mode (last-to-first, binary search)
> - Spilling multi-column returns
> - Version availability and the INDEX/MATCH fallback

---

## 5. Two-Way Lookup
> 🔴 Tier 1 · _Tracker hint:_ =INDEX(data, MATCH(row_val, row_labels,0), MATCH(col_val, col_labels,0))

### Definition
A **two-way (matrix) lookup** finds the intersection of a row label and a column label in a grid such as a freight rate card, price matrix or SLA table.

`=INDEX(data_grid, MATCH(row_value, row_labels, 0), MATCH(col_value, col_labels, 0))`

- First `MATCH` finds the row position, second finds the column position, and INDEX returns the cell at that intersection.
- Use `MATCH(...,0)` for text labels and `MATCH(...,1)` on ascending numeric headers for bands (weight slabs, distance slabs).
- XLOOKUP version: `=XLOOKUP(row_val,row_labels,XLOOKUP(col_val,col_labels,data_grid))` (the inner XLOOKUP returns a column that the outer one searches).
- Data validation dropdowns for row and column inputs make an interactive rate calculator.

### Example
Rate card (Rs): zones in `A2:A4` (Z1, Z2, Z3), weight slab lower bounds in `B1:D1` (0, 5, 10 kg), data in `B2:D4`:

| | 0 | 5 | 10 |
|---|---|---|---|
| Z1 | 40 | 60 | 90 |
| Z2 | 55 | 80 | 120 |
| Z3 | 70 | 100 | 150 |

For Zone Z2 and a 7.5 kg parcel: `=INDEX(B2:D4,MATCH("Z2",A2:A4,0),MATCH(7.5,B1:D1,1))`. `MATCH("Z2",...,0)` = 2; `MATCH(7.5,B1:D1,1)` = 2 (largest slab bound not above 7.5 is 5); INDEX returns row 2, column 2 = **Rs 80**.

### In the news
See news box. Rate-card lookups are exactly where deterministic formulas beat AI functions; Microsoft advised against the COPILOT function for retrieving data already in the workbook.

### Interview angle
> [!question] How it is asked
> "Given a rate matrix by zone and weight, how do you auto-pick the freight cost?"

> [!tip] Strong answer includes
> - INDEX with two MATCH calls; exact for labels, approximate for numeric slabs
> - Sorted headers requirement for approximate match
> - Dropdowns for inputs and `IFERROR/IFNA` guards for out-of-range weights
> - XLOOKUP nested alternative

---

## 6. MATCH Function
> 🔴 Tier 1 · _Tracker hint:_ =MATCH(value, array, 0); returns position; combine with index; 0=exact,-1=less,1=greater

### Definition
`=MATCH(lookup_value, lookup_array, [match_type])` returns the **relative position** (not the value) of an item in a one-row or one-column range.

| match_type | Meaning | Data order needed |
|---|---|---|
| `0` | Exact match (wildcards `*`, `?` allowed for text) | Any |
| `1` (default) | Largest value **less than or equal to** the lookup | Ascending |
| `-1` | Smallest value **greater than or equal to** the lookup | Descending |

(Note: the tracker hint's "-1 = less, 1 = greater" is reversed: `1` finds the largest value not exceeding the lookup, `-1` the smallest value not below it.) The default of `1` when you omit the argument is a common trap, so always type `0` for exact matching. MATCH is case-insensitive; it returns `#N/A` if nothing matches.

Uses: feed INDEX, find the last numeric row (`=MATCH(9.99E+307,A:A)`), check existence (`=ISNUMBER(MATCH(x,list,0))`), find the column of a header, and drive dynamic ranges. XMATCH (365) adds `match_mode` and `search_mode` like XLOOKUP and defaults to exact.

### Example
List `A2:A6` = Bolt, Nut, Washer, Screw, Rivet. `=MATCH("Washer",A2:A6,0)` returns 3. Sorted bands `{0,50000,100000,200000}`: `=MATCH(125000,band_min,1)` returns 3 (1,00,000 is the largest threshold not above 1,25,000); `=MATCH(125000,band_min,0)` returns `#N/A` because there is no exact 125000. Existence test: `=IF(ISNUMBER(MATCH("Nut",A2:A6,0)),"In list","Missing")` returns "In list".

### In the news
See news box. For new files, `XMATCH` is the 365 successor with exact-match default.

### Interview angle
> [!question] How it is asked
> "What does MATCH return, and what do match types 0, 1 and -1 do?"

> [!tip] Strong answer includes
> - Returns position, not value; pairs with INDEX
> - Correct meaning of 1 / 0 / -1 and sort requirements
> - Warn about the default of 1
> - Use cases: existence checks, slab lookups, last-row detection

---

## 7. OFFSET Function
> 🔴 Tier 1 · _Tracker hint:_ =OFFSET(ref, rows, cols, [height], [width]); dynamic ranges; use in dashboards

### Definition
`=OFFSET(reference, rows, cols, [height], [width])` returns a reference that is `rows` down and `cols` right of the starting cell (negative = up/left), optionally resized to `height` x `width`. It returns a **reference**, so it can be wrapped in SUM, AVERAGE, charts or named ranges.

It is **volatile**: Excel recalculates it on every change anywhere in the workbook, which slows large models. Alternatives that are non-volatile: INDEX-based ranges (`$A$2:INDEX($A:$A,n)`), Excel Tables, dynamic arrays (`TAKE`, `DROP` in 365).

Typical uses: rolling windows (last 3 months), dynamic chart ranges, dependent selection by position, scenario shifting. Prefer other tools when the same result can be obtained non-volatilely.

### Example
`=OFFSET(A1,2,1,3,1)` starts at `A1`, goes 2 rows down and 1 column right (cell `B3`) and returns 3 rows x 1 column: the range `B3:B5`. Rolling 3-month sum when data is in `B2:B13` and the count of filled months is in `n = COUNT(B2:B13)`: `=SUM(OFFSET(B1,COUNT(B2:B13)-2,0,3,1))`. With 8 months of data, OFFSET moves 6 rows down from `B1` to `B7` and takes 3 cells, `B7:B9`, which are months 6, 7 and 8 (rows 2 to 9 hold the data). Non-volatile equivalent: `=SUM(INDEX(B2:B13,COUNT(B2:B13)-2):INDEX(B2:B13,COUNT(B2:B13)))`.

### In the news
Not tied to a specific news item. See news box: modern spilled-array functions are reducing the need for volatile OFFSET tricks.

### Interview angle
> [!question] How it is asked
> "How do you build a chart or sum that automatically follows the last 12 months of data?"

> [!tip] Strong answer includes
> - OFFSET syntax and that it returns a reference
> - Volatility and the performance trade-off
> - Non-volatile alternatives (INDEX range, Tables, TAKE)
> - Specific use case (rolling window or dashboard dropdown)

---

## 8. CHOOSE Function
> 🔴 Tier 1 · _Tracker hint:_ =CHOOSE(index,VAL1,VAL2,...); scenario selector; combine with match

### Definition
`=CHOOSE(index_num, value1, [value2], ...)` returns the item at position `index_num` (1 to 254 values). Values can be numbers, text, cell references or even ranges. Index must be a whole number 1 or more (decimals are truncated); out-of-range gives `#VALUE!`.

Uses: **scenario selector** for models (`1=Low, 2=Base, 3=High` drives growth, price, cost), converting codes to labels (`CHOOSE(WEEKDAY(A1,2),"Mon","Tue",...)`), picking which range to aggregate (`=SUM(CHOOSE(B1,Q1_Sales,Q2_Sales))`), and combining with `MATCH` to map text to an index: `=CHOOSE(MATCH(B1,{"Low","Base","High"},0),5%,8%,12%)`. Compared with nested IF, CHOOSE is shorter when the selector is numeric. For ranges of values, `INDEX` can do the same job on a table and is easier to maintain; `SWITCH` and `XLOOKUP` are the modern alternatives.

### Example
Scenario cell `B1` = 2. `=CHOOSE(B1,0.05,0.08,0.12)` returns 8% (base case growth). Revenue next year = `=B2*(1+CHOOSE($B$1,0.05,0.08,0.12))`; with current revenue Rs 100 crore, base case gives $100\times1.08=$ Rs 108 crore, high case (3) gives Rs 112 crore. Switching `B1` flips the whole model, typically via a dropdown.

### In the news
Not tied to a specific news item. See news box: scenario selectors remain a deterministic way to let non-technical users flex a model, unlike AI-generated outputs.

### Interview angle
> [!question] How it is asked
> "How would you build a model where the user picks Optimistic, Base or Pessimistic and everything updates?"

> [!tip] Strong answer includes
> - A single scenario cell (dropdown) feeding CHOOSE/INDEX for each assumption
> - Assumptions table with one column per scenario
> - Labelled outputs and a check on the chosen scenario
> - Alternatives: SWITCH, XLOOKUP, Data Tables for sensitivity

---

## 9. INDIRECT
> 🔴 Tier 1 · _Tracker hint:_ =INDIRECT('sheet2!a1'); dynamic sheet/range references; useful but volatile

### Definition
`=INDIRECT(ref_text, [a1])` converts a **text string** into a live reference. The text can be built from cell contents, so sheet names, ranges and even named ranges can be chosen dynamically.

`=INDIRECT("Sheet2!A1")` or, with a sheet name that has spaces or comes from a cell, `=INDIRECT("'"&A1&"'!B2")`.

Uses: consolidate identical monthly sheets, dependent dropdowns (`INDIRECT(B2)` where `B2` is a named range), build references from row/column numbers (`INDIRECT("R"&r&"C"&c,FALSE)`).

Drawbacks: **volatile** (slows large files); references are text, so they do not update when you rename or move sheets or insert rows, and Trace Precedents cannot follow them; fails if the target workbook is closed. Prefer INDEX/CHOOSE, structured references, `XLOOKUP`, Power Query or `VSTACK` (365) where possible.

### Example
Sheets named Jan, Feb, Mar each hold totals in `B10`. Put the sheet name in `A2` (e.g., "Feb"): `=INDIRECT("'"&A2&"'!B10")` returns Feb's total. If Jan = 120, Feb = 135, Mar = 150, changing `A2` among the three returns each value, and `=SUM(INDIRECT("'"&A2&"'!B2:B9"))` totals a range on the selected sheet. A dependent dropdown: list of states in named ranges `Maharashtra`, `Gujarat`; the second dropdown's source is `=INDIRECT($B$2)`.

### In the news
See news box. As workbooks add Python and AI features, volatile text-built references such as INDIRECT are harder to audit; Power Query is increasingly preferred for consolidating sheets.

### Interview angle
> [!question] How it is asked
> "How would you pull the same cell from 12 monthly sheets into a summary, and what are the risks?"

> [!tip] Strong answer includes
> - INDIRECT with a sheet name in a cell; alternative of 3D references or Power Query append
> - Volatility, auditing and rename risks
> - Dependent dropdown use case
> - Safer alternatives and when INDIRECT is still acceptable

---

## 10. IFERROR / IFNA
> 🔴 Tier 1 · _Tracker hint:_ =IFERROR(VLOOKUP(...),'not found'); clean error handling in lookup chains

### Definition
`=IFERROR(value, value_if_error)` returns a fallback if `value` is any error (`#N/A`, `#DIV/0!`, `#VALUE!`, `#REF!`, `#NAME?`, `#NUM!`, `#NULL!`). `=IFNA(value, value_if_na)` catches **only `#N/A`** (the "not found" error from lookups).

Best practice: use **IFNA** for lookups so genuine mistakes (a broken reference `#REF!`, a typo `#NAME?`) still surface; blanket IFERROR can mask bugs and wrong totals. For division, test the cause: `=IF(B2=0,0,A2/B2)`. Fallbacks should be meaningful (`"Not found"`, 0, or blank `""`), and note that text fallbacks inside numeric columns break sums.

Chain lookups across sources: `=IFNA(VLOOKUP(A2,Table1,2,0),IFNA(VLOOKUP(A2,Table2,2,0),"Not found"))`. With XLOOKUP use its `if_not_found` argument instead. `AGGREGATE` can ignore errors in aggregations (e.g. `=AGGREGATE(9,6,range)` sums ignoring errors).

### Example
`=VLOOKUP("S999",A2:C6,3,FALSE)` returns `#N/A`. `=IFNA(VLOOKUP("S999",A2:C6,3,FALSE),"Not found")` shows "Not found". If the price column is typed `Rs 12` (text) and arithmetic gives `#VALUE!`, IFNA lets it show through and exposes the data error, whereas IFERROR would hide it and a downstream total could silently be too low (e.g., 4 of 5 prices summed: 12+8+3+5=28 instead of 35 with Rivet = 7).

### In the news
See news box. Microsoft's guidance that AI-formula output should not be used for exact numerical work reinforces explicit, auditable error handling.

### Interview angle
> [!question] How it is asked
> "What is the difference between IFERROR and IFNA, and which would you use around a lookup?"

> [!tip] Strong answer includes
> - IFNA targets only `#N/A`; IFERROR swallows everything
> - Risk of masking real errors; meaningful fallback values
> - Chained lookups across multiple sources
> - Prefer XLOOKUP's `if_not_found` or fix the root cause (clean data)

---

## 11. ⭐ Advanced: Dynamic Array Functions (FILTER, SORT, UNIQUE, XMATCH)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
In Excel 365 and 2021, formulas can return **arrays that spill** into neighbouring cells; a reference to a spill uses `A2#`.

- `FILTER(array, include, [if_empty])` returns rows meeting conditions; multiply conditions for AND, add for OR.
- `UNIQUE(array, [by_col], [exactly_once])` returns distinct values.
- `SORT(array, [sort_index], [order])` and `SORTBY`.
- `XMATCH`, `TAKE`, `DROP`, `VSTACK`, `HSTACK`, `TEXTSPLIT` (newer).
- `LET(name, value, ..., calculation)` stores intermediate results; `LAMBDA` makes custom functions.

Together they replace many helper columns and array formulas: a dependent dropdown source is `=UNIQUE(FILTER(...))`, a top-5 list is `=TAKE(SORT(...),5)`. Spill errors (`#SPILL!`) occur when the output range is blocked.

### Example
Table `A2:C7` (Region, Product, Sales): East A 100; East B 150; West A 200; West A 120; West B 80; East A 130. `=UNIQUE(A2:A7)` returns East, West. `=FILTER(A2:C7,(A2:A7="West")*(B2:B7="A"),"None")` returns the two rows West A 200 and West A 120. `=SORT(C2:C7,1,-1)` returns 200, 150, 130, 120, 100, 80. `=LET(t,SUM(C2:C7),n,COUNT(C2:C7),t/n)` returns $780/6=130$.

### In the news
See news box. Dynamic arrays are the formula-side counterpart to Python in Excel and are part of the 365 feature set Microsoft keeps extending.

### Interview angle
> [!question] How it is asked
> "Without a PivotTable, how do you get a live, sorted list of unique customers with their total sales?"

> [!tip] Strong answer includes
> - `UNIQUE` plus `SUMIFS` referencing the spill (`A2#`) or `GROUPBY` where available
> - FILTER with AND/OR logic and `if_empty`
> - Knowledge of `#SPILL!` and version availability (365/2021 vs 2019)
> - Fallback for older Excel: PivotTable or helper columns

---

## 12. ⭐ Advanced: Lookup Performance and Approximate-Match Binary Search
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Lookups on large data can make a workbook crawl, so know the performance rules:

- **Exact-match** VLOOKUP/MATCH scans linearly: roughly $n$ comparisons per lookup, so $m$ lookups on $n$ rows cost about $m\times n$ operations.
- **Approximate match on sorted data** uses binary search: about $\log_2 n$ comparisons. For 100,000 rows, $\log_2 100000\approx17$ vs up to 100,000.
- Trick for fast exact match on sorted data: `=IF(INDEX(keys,MATCH(x,keys,1))=x, INDEX(vals,MATCH(x,keys,1)),"Not found")` (binary search plus an equality check). XLOOKUP's `search_mode` `2` or `-2` offers binary search directly.
- Compute `MATCH` once in a helper column and reuse it in many `INDEX` formulas.
- Reference only needed ranges, not entire columns, in VLOOKUP with huge tables; Tables handle this.
- Avoid volatile functions (OFFSET, INDIRECT, TODAY) in heavy sheets; set calculation to manual while building.
- Beyond roughly a million rows or many joins: Power Query merge, Power Pivot relationships, or SQL/pandas.

### Example
A model has 50,000 SKUs and performs 50,000 exact VLOOKUPs against a 100,000-row master. Worst case about $50{,}000\times100{,}000=5\times10^9$ comparisons. With sorted keys and binary search, about $50{,}000\times17=850{,}000$ comparisons (thousands of times less). In practice, Excel's exact-match engine has internal optimisations, but the order-of-magnitude difference is why sorting plus approximate search or a helper MATCH column is recommended for very large lookups.

### In the news
See news box. Python in Excel offloads heavy merges to pandas in the cloud, an alternative when lookup-heavy workbooks become slow.

### Interview angle
> [!question] How it is asked
> "Your workbook with 200,000 lookups takes minutes to recalculate. What do you do?"

> [!tip] Strong answer includes
> - Diagnose: volatile functions, whole-column references, exact-match scans
> - Binary-search approach, helper MATCH column, Tables
> - Move joins to Power Query / Power Pivot / SQL
> - Calculation mode and documenting trade-offs

---
## 🔗 Go deeper: expansion notes
- [[187 Excel Interview Problem Bank & Case Exercises|Excel Interview Problem Bank & Case Exercises]]
- [[188 Financial Modelling in Excel|Financial Modelling in Excel]]
- [[189 VBA, Macros & Office Scripts Basics|VBA, Macros & Office Scripts Basics]]
