---
tags: [excel-advanced, tier1]
area: Excel Advanced
topic: "Excel Interview Problem Bank & Case Exercises"
tier: Tier 1
roles: Analytics / Operations / Consulting
status: complete
subtopics: 14
---
# Excel Interview Problem Bank & Case Exercises

⬅ [[078 Excel for Operations & SCM]] · [[_Index - Excel Advanced|Excel Advanced]] · [[188 Financial Modelling in Excel]] ➡

> **Area:** Excel Advanced · **Priority:** 🔴 Tier 1 · **Target roles:** Analytics / Operations / Consulting

## Sub-topics in this note
1. [[#1. The Practice Dataset & How to Use This Bank]]
2. [[#2. Lookup Tasks]]
3. [[#3. Dynamic Array Tasks]]
4. [[#4. SUMPRODUCT & Multi-Condition Aggregation]]
5. [[#5. Date & Time Logic]]
6. [[#6. ABC Analysis & Pareto]]
7. [[#7. Running Totals, Ranking & Percent of Total]]
8. [[#8. Deduplication & Text Clean-up]]
9. [[#9. Pivot-Table Questions]]
10. [[#10. What-If, Goal Seek & Break-Even]]
11. [[#11. Timed Case Exercises]]
12. [[#12. Formula-Audit Questions & Common Mistakes]]
13. [[#13. Keyboard-Speed List & Drills]]
14. [[#14. ⭐ Advanced: LET, LAMBDA, Power Query & Python Hand-offs]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Excel's formula toolbox keeps growing while the AI shortcut for it was pulled back
> **The COPILOT function is retired (announced 17 August 2026, stops 14 September 2026).** The Register reports that Microsoft is withdrawing the `=COPILOT` worksheet function, introduced in August 2025 and never out of preview, with the Copilot side pane as the supported alternative. Microsoft's own caution at launch was that output should be validated before use in critical decisions. Interview takeaway: show you can build the answer with formulas you can audit, not by prompting a cell. ([The Register](https://www.theregister.com/ai-and-ml/2026/08/17/excels-copilot-function-is-headed-for-the-recycle-bin/5288327), [Windows Central](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-is-ditching-the-copilot-function-in-excel-before-it-even-launches))
>
> **New aggregation and text functions.** Microsoft's Insider blog describes `GROUPBY` and `PIVOTBY`, which summarise data with a formula and, in its words, need just 3 arguments, the same number as a simple `XLOOKUP`; the page was last modified on 31 January 2025 ([Microsoft 365 Insider blog](https://techcommunity.microsoft.com/blog/microsoft365insiderblog/new-aggregation-functions-in-excel-groupby-and-pivotby/4222707)). A Microsoft Q&A thread (January 2026) lists `REGEXTEST`, `REGEXEXTRACT` and `REGEXREPLACE` as available in Current and Monthly Enterprise Channels, with the Semi-Annual Enterprise Channel expected around July 2026 (not guaranteed) ([Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5727787/when-are-the-regex-functions-coming-to-excel-365-u)). Function availability depends on the update channel, so check `File > Account` before relying on a new function in an interview test or a shared model.
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The Practice Dataset & How to Use This Bank
> 🔴 Tier 1 · _Key points:_ one ops dataset reused for every task, Excel 365 and legacy formulas, expected answers

### Definition
Every task below uses the same small **order-to-delivery dataset**, so each answer can be checked. Type or paste it into a new workbook. Sheet `Orders` holds 20 sales orders in `A1:K21` (header in row 1; `H` = `F*G`; blank `J` means not delivered). Sheet `SKU` is the item master, `Slabs` a quantity-discount table and `Freight` a rate card.

| A OrderID | B OrderDate | C Customer | D Region | E SKU | F Qty | G UnitPrice | H Value | I Promised | J Delivered | K Status |
|---|---|---|---|---|---|---|---|---|---|---|
| SO-1001 | 05-Jan-26 | Tata Motors | West | BRG-6205 | 400 | 250 | 100,000 | 12-Jan-26 | 11-Jan-26 | Delivered |
| SO-1002 | 07-Jan-26 | Bajaj Auto | West | SEAL-3552 | 1,200 | 40 | 48,000 | 14-Jan-26 | 16-Jan-26 | Delivered |
| SO-1003 | 09-Jan-26 | Mahindra | West | BOLT-M12 | 5,000 | 3 | 15,000 | 16-Jan-26 | 16-Jan-26 | Delivered |
| SO-1004 | 12-Jan-26 | Ashok Leyland | South | HOSE-12 | 150 | 900 | 135,000 | 22-Jan-26 | 27-Jan-26 | Delivered |
| SO-1005 | 15-Jan-26 | Eicher | North | ROD-16 | 800 | 70 | 56,000 | 23-Jan-26 | 22-Jan-26 | Delivered |
| SO-1006 | 19-Jan-26 | Tata Motors | West | SEAL-3552 | 600 | 40 | 24,000 | 27-Jan-26 | 27-Jan-26 | Delivered |
| SO-1007 | 22-Jan-26 | Bajaj Auto | West | BRG-6205 | 300 | 250 | 75,000 | 30-Jan-26 | 02-Feb-26 | Delivered |
| SO-1008 | 28-Jan-26 | Mahindra | West | ROD-16 | 1,500 | 70 | 105,000 | 05-Feb-26 | 04-Feb-26 | Delivered |
| SO-1009 | 02-Feb-26 | Ashok Leyland | South | BOLT-M12 | 8,000 | 3 | 24,000 | 09-Feb-26 | 09-Feb-26 | Delivered |
| SO-1010 | 04-Feb-26 | Eicher | North | GASK-90 | 500 | 55 | 27,500 | 11-Feb-26 | 13-Feb-26 | Delivered |
| SO-1011 | 09-Feb-26 | Tata Motors | West | HOSE-12 | 100 | 900 | 90,000 | 17-Feb-26 | 16-Feb-26 | Delivered |
| SO-1012 | 11-Feb-26 | Bajaj Auto | West | BOLT-M12 | 6,000 | 3 | 18,000 | 18-Feb-26 | 18-Feb-26 | Delivered |
| SO-1013 | 16-Feb-26 | Mahindra | West | BRG-6205 | 250 | 250 | 62,500 | 24-Feb-26 | 27-Feb-26 | Delivered |
| SO-1014 | 19-Feb-26 | Eicher | North | SEAL-3552 | 900 | 40 | 36,000 | 26-Feb-26 | 25-Feb-26 | Delivered |
| SO-1015 | 24-Feb-26 | Ashok Leyland | South | ROD-16 | 600 | 70 | 42,000 | 04-Mar-26 | 04-Mar-26 | Delivered |
| SO-1016 | 02-Mar-26 | Tata Motors | West | GASK-90 | 700 | 55 | 38,500 | 09-Mar-26 | 12-Mar-26 | Delivered |
| SO-1017 | 05-Mar-26 | Bajaj Auto | West | HOSE-12 | 120 | 900 | 108,000 | 13-Mar-26 |  | Open |
| SO-1018 | 10-Mar-26 | Eicher | North | BRG-6205 | 200 | 250 | 50,000 | 18-Mar-26 |  | Open |
| SO-1019 | 12-Mar-26 | Mahindra | West | SEAL-3552 | 1,000 | 40 | 40,000 | 20-Mar-26 |  | Open |
| SO-1020 | 16-Mar-26 | Ashok Leyland | South | BRG-6205 | 350 | 250 | 87,500 | 25-Mar-26 |  | Open |

`SKU` sheet (A1:E7): BRG-6205 Bearings 150 (cost) 7 (lead days) Pune Bearings; SEAL-3552 Seals 22, 5; BOLT-M12 Fasteners 1.8, 10; HOSE-12 Hydraulics 620, 14; ROD-16 Steel 48, 6; GASK-90 Seals 31, 5. `Slabs` (A1:B5): MinQty/Discount rows 0/0%, 500/2%, 1,000/4%, 5,000/6%. `Freight` (A1:F4): regions West, North, South by category Bearings, Seals, Fasteners, Hydraulics, Steel; South x Hydraulics is 2.5%.

Control totals: sum of `Value` = ₹11,82,000; Delivered ₹8,96,500; Open ₹2,85,500. **Rules of the bank.** Formulas assume they are typed on the `Orders` sheet with ranges `2:21`; in a real model convert the data to an Excel Table and use structured references (`tblOrders[Value]`) so ranges grow automatically. Each task lists an Excel 365 formula and, where it differs, a legacy formula for Excel 2016 to 2019. The legacy formulas below were recalculated in a spreadsheet engine (LibreOffice Calc) against this dataset and matched the stated results, except the `AGGREGATE` array idiom in Q41, which that engine cannot evaluate (its answer was checked in pandas). The 365-only formulas (`XLOOKUP`, `XMATCH`, `FILTER`, `UNIQUE`, `SORTBY`, `TAKE`, `LET`, `SCAN`, `HSTACK`, `TEXTBEFORE`, `GROUPBY`) could not be evaluated by that engine and were checked against an independent pandas calculation of the expected result, so confirm them in Excel before an interview. Dates and numbers were typed as real dates and numbers, never text.

### Example
How to practise: cover the "Answer" column, write the formula in under two minutes, compare. Tasks Q1 to Q50 are numbered through the sub-topics; the timed cases in sub-topic 11 combine them. Background reading: [[071 Lookup & Reference Functions]], [[072 Logical & Statistical Functions]], [[073 Text & Date Functions]], [[074 Array & Dynamic Array Functions]] and [[078 Excel for Operations & SCM]].

### In the news
See news box. In a timed test, confirm which functions your Excel version supports before choosing between `XLOOKUP` and `INDEX/MATCH`; use whichever you can defend.

### Interview angle
> [!question] How it is asked
> "Here is a sales extract. In 30 minutes, answer these ten questions in Excel and explain your approach."

> [!tip] Strong answer includes
> - Check the data first (types, blanks, duplicates, totals) before writing formulas
> - Absolute and relative references used deliberately; ranges as Tables or named ranges
> - State assumptions (as-of date, definition of on-time) and verify with a control total
> - Mention the alternative (pivot, Power Query) and why you chose the formula

---
## 2. Lookup Tasks
> 🔴 Tier 1 · _Key points:_ XLOOKUP vs INDEX/MATCH, approximate match, last match, two-way, multi-criteria

### Definition
| Q | Task | Excel 365 | Legacy | Answer |
|---|---|---|---|---|
| 1 | Unit cost of the SKU in E2 from `SKU` sheet | `=XLOOKUP(E2,SKU!$A$2:$A$7,SKU!$C$2:$C$7,"Not found")` | `=INDEX(SKU!$C$2:$C$7,MATCH(E2,SKU!$A$2:$A$7,0))` | 150 |
| 2 | Same, but return "Not found" for bad SKUs | built in (4th argument) | `=IFERROR(INDEX(SKU!$C$2:$C$7,MATCH("XYZ-1",SKU!$A$2:$A$7,0)),"Not found")` | Not found |
| 3 | Customer name for order SO-1010 (lookup key to the right of the answer) | `=XLOOKUP("SO-1010",A2:A21,C2:C21)` | `=INDEX(C2:C21,MATCH("SO-1010",A2:A21,0))` | Eicher |
| 4 | Discount slab for the quantity in F3 (1,200) | `=XLOOKUP(F3,Slabs!$A$2:$A$5,Slabs!$B$2:$B$5,,-1)` | `=LOOKUP(F3,Slabs!$A$2:$A$5,Slabs!$B$2:$B$5)` or `=VLOOKUP(F3,Slabs!$A$2:$B$5,2,TRUE)` | 4% |
| 5 | Freight % for region of D5 (South) and category Hydraulics (two-way) | `=INDEX(Freight!$B$2:$F$4,XMATCH(D5,Freight!$A$2:$A$4),XMATCH("Hydraulics",Freight!$B$1:$F$1))` | `=INDEX(Freight!$B$2:$F$4,MATCH(D5,Freight!$A$2:$A$4,0),MATCH("Hydraulics",Freight!$B$1:$F$1,0))` | 2.5% |
| 6 | Date of Eicher's most recent order (last match) | `=XLOOKUP("Eicher",C2:C21,B2:B21,,0,-1)` | `=LOOKUP(2,1/(C2:C21="Eicher"),B2:B21)` | 10-Mar-26 |
| 7 | Order ID for Tata Motors and HOSE-12 (two criteria) | `=XLOOKUP(1,(C2:C21="Tata Motors")*(E2:E21="HOSE-12"),A2:A21)` | `=INDEX(A2:A21,MATCH(1,INDEX((C2:C21="Tata Motors")*(E2:E21="HOSE-12"),0),0))` | SO-1011 |
| 8 | Total quantity for Tata Motors and SEAL-3552 (numeric: use SUMIFS) | `=SUMIFS(F2:F21,C2:C21,"Tata Motors",E2:E21,"SEAL-3552")` | same | 600 |

Why `LOOKUP(2,1/(...),...)` works: the division yields 1 for matches and `#DIV/0!` for non-matches; `LOOKUP` ignores errors and, with a lookup value (2) larger than anything in the array, returns the last numeric entry. `XLOOKUP`'s `-1` in the search-mode argument (6th) searches last to first; its 5th argument `0` means exact match; `-1` in the 5th argument means exact or next smaller (approximate on sorted data).

### Example
Q4 in detail: quantity 1,200 sits between the slab starts 1,000 and 5,000, so the "exact or next smaller" logic returns the 1,000 row's 4%. If the table were unsorted, approximate `VLOOKUP`/`LOOKUP` would return garbage silently; `XLOOKUP` with `-1` does not need a sorted table. For Q5, `MATCH` supplies row 3 (South) and column 4 (Hydraulics) of the 3 x 5 rate card, giving 0.025.

### In the news
See news box. `XLOOKUP`, `XMATCH` and dynamic arrays are in Microsoft 365 and Excel 2021 and later; shared workbooks that must open in Excel 2016 or 2019 should keep `INDEX/MATCH`.

### Interview angle
> [!question] How it is asked
> "Why prefer `XLOOKUP` over `VLOOKUP`? When does `INDEX/MATCH` still win?"

> [!tip] Strong answer includes
> - `VLOOKUP` cannot look left, breaks when columns are inserted (hard-coded index number), and defaults to approximate match
> - `XLOOKUP`: separate arrays, built-in not-found text, search direction, match modes, returns arrays
> - `INDEX/MATCH` for backwards compatibility and for two-way lookups
> - Exact match (0 or FALSE) by default in analysis; approximate only for sorted bands

---
## 3. Dynamic Array Tasks
> 🔴 Tier 1 · _Key points:_ UNIQUE, FILTER, SORTBY, TAKE, LET, SCAN, GROUPBY, spill behaviour

### Definition
Dynamic array formulas **spill** their results into neighbouring cells; reference the whole spill with the `#` operator (`E2#`). They need Microsoft 365 (and `TAKE`, `HSTACK`, `GROUPBY` need a recent build); legacy alternatives are given.

| Q | Task | Excel 365 | Legacy | Answer |
|---|---|---|---|---|
| 9 | List the customers once | `=UNIQUE(C2:C21)` | Remove Duplicates on a copy, or `INDEX/MATCH/COUNTIF` helper | 5 names |
| 10 | Count distinct customers | `=COUNTA(UNIQUE(C2:C21))` | `=SUMPRODUCT(1/COUNTIF(C2:C21,C2:C21))` | 5 |
| 11 | Distinct customers in the West | `=COUNTA(UNIQUE(FILTER(C2:C21,D2:D21="West")))` | `=SUMPRODUCT((D2:D21="West")/COUNTIFS(C2:C21,C2:C21,D2:D21,D2:D21))` | 3 |
| 12 | All open orders for Eicher | `=FILTER(A2:A21,(C2:C21="Eicher")*(K2:K21="Open"),"None")` | helper column with `AGGREGATE` or filter | SO-1018 |
| 13 | Top 3 orders by value (whole rows) | `=TAKE(SORTBY(A2:K21,H2:H21,-1),3)` | `=INDEX(A2:A21,MATCH(LARGE(H2:H21,k),H2:H21,0))` for k=1,2,3 | SO-1004, SO-1017, SO-1008 |
| 14 | Tata Motors share of total value, one named step | `=LET(tm,SUMIFS(H2:H21,C2:C21,"Tata Motors"),tm/SUM(H2:H21))` | `=SUMIFS(H2:H21,C2:C21,"Tata Motors")/SUM(H2:H21)` | 21.36% |
| 15 | Running total of Value as one spilled column | `=SCAN(0,H2:H21,LAMBDA(a,b,a+b))` | `=SUM($H$2:H2)` filled down | last = 11,82,000 |
| 16 | Revenue by customer, sorted descending | `=GROUPBY(C2:C21,H2:H21,SUM,,,-2)` (or `=SORTBY(UNIQUE(C2:C21),SUMIFS(H2:H21,C2:C21,UNIQUE(C2:C21)),-1)` for names) | PivotTable | Ashok 2,88,500; Tata 2,52,500; Bajaj 2,49,000; Mahindra 2,22,500; Eicher 1,69,500 |

Notes: for Q13 the second-largest in the legacy version is `LARGE(H2:H21,2)` = 1,08,000 (SO-1017). `LET` names intermediate results so the formula is shorter, faster (each name is computed once) and readable. In `GROUPBY`, a negative `sort_order` sorts descending by the numbered column (column 2 here is the summed values); confirm argument details with `F1` help in your build, since the function is new.

### Example
Q11 by hand: West customers are Tata Motors, Bajaj Auto and Mahindra (Ashok Leyland is South, Eicher North), so 3. The legacy `SUMPRODUCT` works by giving each West row the weight $1/n$, where $n$ is how many rows share that customer-and-region pair, so each distinct customer sums to 1. Dynamic arrays do the same with `UNIQUE`/`FILTER`.

### In the news
See news box. New functions such as `GROUPBY` and `REGEX*` are rolling out by update channel, so a spill formula that works on your laptop may show `#NAME?` on a colleague's older build.

### Interview angle
> [!question] How it is asked
> "Without a PivotTable, produce a live sorted list of customers with their total revenue."

> [!tip] Strong answer includes
> - `UNIQUE` plus `SUMIFS` with spill range, `SORTBY` for order, or `GROUPBY` where available
> - The `#` spill reference and `#SPILL!` causes (blocked cells, tables cannot hold spills)
> - Legacy alternative for older Excel and for sharing
> - When a PivotTable is better (huge data, interactive slicing, refresh)

---
## 4. SUMPRODUCT & Multi-Condition Aggregation
> 🔴 Tier 1 · _Key points:_ boolean arrays, AND as multiply, OR as add, weighted averages, SUMIFS limits

### Definition
`SUMPRODUCT` multiplies arrays element by element and sums the products, so it evaluates conditions without Ctrl+Shift+Enter. TRUE/FALSE become 1/0 when multiplied or when preceded by `--`. **AND** is multiplication, **OR** is addition (then test `>0`). It is the answer when `SUMIFS` cannot express the test (comparing two columns, functions of dates, OR logic).

| Q | Task | Formula | Answer |
|---|---|---|---|
| 17 | Weighted average selling price | `=SUMPRODUCT(F2:F21,G2:G21)/SUM(F2:F21)` | ₹41.23 per unit |
| 18 | Value of open West orders | `=SUMPRODUCT((D2:D21="West")*(K2:K21="Open")*H2:H21)` | 1,48,000 |
| 19 | Orders placed by Eicher or Mahindra | `=SUMPRODUCT(--((C2:C21="Eicher")+(C2:C21="Mahindra")>0))` | 8 |
| 20 | Number of late deliveries (delivered after promised) | `=SUMPRODUCT(--(J2:J21>I2:I21))` | 6 |
| 21 | Value of late deliveries | `=SUMPRODUCT((J2:J21>I2:I21)*H2:H21)` | 3,86,500 |
| 22 | Average days late among late orders | `=SUMPRODUCT((J2:J21>I2:I21)*(J2:J21-I2:I21))/SUMPRODUCT(--(J2:J21>I2:I21))` | 3.0 days |
| 23 | Open orders already overdue at 20-Mar-26 | `=SUMPRODUCT((K2:K21="Open")*(I2:I21<DATE(2026,3,20)))` | 2 |
| 24 | Gross margin % using SKU unit costs | `=SUMPRODUCT(F2:F21,G2:G21-SUMIF(SKU!$A$2:$A$7,E2:E21,SKU!$C$2:$C$7))/SUM(H2:H21)` | 36.85% |

Why Q20 works: undelivered orders have an empty `J`, which Excel treats as 0, so `0>I` is FALSE and they are not counted as late. Q24 uses `SUMIF` with an array of criteria (E2:E21) to fetch each row's unit cost inside `SUMPRODUCT`.

### Example
Q24 by hand: revenue is ₹11,82,000 and cost of goods is ₹7,46,400 (sum of qty x unit cost), so margin is 4,35,600 / 11,82,000 = 36.85%. Per SKU: Seals 45.0%, Gaskets 43.6%, Bearings 40.0%, Fasteners 40.0%, Steel 31.4%, Hydraulics 31.1%: the biggest-revenue lines are not the most profitable ones, which is the consulting-style insight to speak aloud.

### In the news
See news box. `SUMPRODUCT` remains the compatibility choice for models shared with older Excel versions or other tools where dynamic arrays and `COPILOT` are unavailable.

### Interview angle
> [!question] How it is asked
> "Calculate on-time delivery percentage and average delay without helper columns."

> [!tip] Strong answer includes
> - Boolean arithmetic: `*` for AND, `+` for OR, `--` to coerce
> - Handling blanks (undelivered rows) explicitly
> - `SUMIFS/COUNTIFS` when criteria are simple (faster, clearer), `SUMPRODUCT` for column-to-column comparisons
> - Cross-check with a pivot or a manual count

---
## 5. Date & Time Logic
> 🔴 Tier 1 · _Key points:_ delays, NETWORKDAYS/WORKDAY, EOMONTH, fiscal year (April-March), aging buckets

### Definition
Excel stores dates as serial numbers (1 = 1-Jan-1900 in the 1900 system; 46,023 is 1-Jan-2026), so subtraction gives days. Key functions: `NETWORKDAYS(start,end,[holidays])`, `WORKDAY(start,days,[holidays])`, `EOMONTH`, `EDATE`, `DATEDIF`, `TEXT(date,"mmm-yy")`, `WEEKNUM`, `ISOWEEKNUM`. Indian fiscal year runs April to March.

| Q | Task | Formula | Answer |
|---|---|---|---|
| 25 | Days late for row 3 (SO-1002) | `=MAX(0,J3-I3)` | 2 |
| 26 | On-time % of delivered orders | `=1-SUMPRODUCT(--(J2:J21>I2:I21))/COUNT(J2:J21)` | 62.5% (10 of 16) |
| 27 | Working days from order to delivery for SO-1001 | `=NETWORKDAYS(B2,J2)-1` | 4 |
| 28 | Promise date = order date + 7 working days (SO-1001) | `=WORKDAY(B2,7)` | 14-Jan-26 |
| 29 | Month-end of the order date | `=EOMONTH(B2,0)` | 31-Jan-26 |
| 30 | Fiscal year (ending year) of the order date | `=YEAR(B2)+(MONTH(B2)>=4)` | 2026 (FY 2025-26) |
| 31 | Fiscal quarter (Q1 = Apr-Jun) | `=INT(MOD(MONTH(B2)-4,12)/3)+1` | 4 (Jan-Mar) |
| 32 | Revenue in February 2026 | `=SUMIFS(H2:H21,B2:B21,">="&DATE(2026,2,1),B2:B21,"<"&DATE(2026,3,1))` | 3,00,000 |
| 33 | Days overdue at 20-Mar-26 for SO-1017 (row 18) | `=MAX(0,DATE(2026,3,20)-I18)` | 7 |
| 34 | Aging bucket from days overdue `x` | `=IF(x<=0,"Not due",IF(x<=7,"1-7",IF(x<=30,"8-30",">30")))` | 1-7 (for 7) |
| 35 | Show order date as text "Jan-26" | `=TEXT(B2,"mmm-yy")` | Jan-26 |

Traps: `NETWORKDAYS` counts both end dates, hence the `-1` for elapsed working days; SO-1001 was delivered on Sunday 11-Jan-26, so the 5 working days Mon 5 to Fri 9 count as 5 including the start day, minus 1 gives 4. `TEXT` format codes depend on the language of Excel. Use `DATE(y,m,d)` rather than typing text dates; use `">="&date` to concatenate a date into a criterion. Use a holiday list in `NETWORKDAYS`/`WORKDAY`; `NETWORKDAYS.INTL` and `WORKDAY.INTL` change the weekend pattern (important for six-day plants).

### Example
Aging report at 20-Mar-26: open orders are SO-1017 (promised 13-Mar, 7 days overdue, ₹1,08,000), SO-1018 (18-Mar, 2 days, ₹50,000), SO-1019 (20-Mar, due today, 0) and SO-1020 (25-Mar, not due). Overdue value = ₹1,58,000; in the buckets that is 1-7 days: two orders. A FY pivot grouping needs a helper column because default date grouping uses the calendar year.

### In the news
See news box. `TEXT` and date formats are locale-dependent, so avoid them in keys that must work across country settings; the new `REGEX*` functions, where available, help parse date strings in messy exports.

### Interview angle
> [!question] How it is asked
> "Calculate the on-time delivery rate, the average delay and the number of working days between order and delivery."

> [!tip] Strong answer includes
> - Dates are numbers; subtraction gives days; use `NETWORKDAYS` with a holiday list
> - Treat blanks (undelivered) explicitly; define "on time" (<= promised) up front
> - Fiscal-year and week conventions stated; `EOMONTH` for month bucketing
> - Validate that dates are real dates (not text) with `ISNUMBER`

---
## 6. ABC Analysis & Pareto
> 🔴 Tier 1 · _Key points:_ value by SKU, sort, cumulative share, class cut-offs, Pareto chart

### Definition
ABC analysis ranks items by annual (or period) usage value and splits them at cumulative-share cut-offs, commonly **A: first 80%, B: next 15%, C: last 5%** of value. (Conventions differ on the item that crosses a boundary; state yours.) Steps: aggregate value by SKU, sort descending, compute each share and cumulative share, assign the class. Theory and policies per class are in [[003 Inventory Management]] and [[078 Excel for Operations & SCM]].

| Step | Legacy formula (SKUs typed in `ABC!A2:A7`) |
|---|---|
| Value by SKU (B) | `=SUMIF(Orders!$E$2:$E$21,A2,Orders!$H$2:$H$21)` |
| k-th largest value (D) | `=LARGE($B$2:$B$7,ROWS(D$2:D2))` |
| SKU for that value (E) | `=INDEX($A$2:$A$7,MATCH(D2,$B$2:$B$7,0))` |
| Cumulative share (F) | `=SUM($D$2:D2)/SUM($D$2:$D$7)` |
| Class (G) | `=IF(F2<=0.8,"A",IF(F2<=0.95,"B","C"))` |

Excel 365 in one formula (spills a 4-column table):

```excel
=LET(sku, UNIQUE(E2:E21),
     val, SUMIFS(H2:H21, E2:E21, sku),
     s,   SORTBY(sku, val, -1),
     v,   SORTBY(val, val, -1),
     cum, SCAN(0, v, LAMBDA(a, b, a + b)) / SUM(v),
     HSTACK(s, v, cum, IF(cum <= 0.8, "A", IF(cum <= 0.95, "B", "C"))))
```
Result (both versions): BRG-6205 ₹3,75,000 (31.7%, cumulative 31.7%) A; HOSE-12 ₹3,33,000 (28.2%, 59.9%) A; ROD-16 ₹2,03,000 (17.2%, 77.1%) A; SEAL-3552 ₹1,48,000 (12.5%, 89.6%) B; GASK-90 ₹66,000 (5.6%, 95.2%) C; BOLT-M12 ₹57,000 (4.8%, 100%) C. (The legacy chain was recalculated in a spreadsheet engine; the 365 formula was cross-checked against pandas.)

### Example
Three of six SKUs (50%) make 77.1% of value, and the top four reach 89.6%: the usual "vital few". GASK-90 lands in C because 95.18% is above the 95% cut-off; under the "include the item that crosses the line" convention it would be B. For the chart, build a Pareto: columns for value, a line for cumulative % on a secondary axis (see [[076 Charts, Dashboards & Form Controls]]). Note that 80/20 is a pattern, not a law: ABC by value hides low-value, critical parts, so add criticality or lead-time (XYZ or VED) as a second dimension.

### In the news
See news box. `LET`, `SCAN` and `HSTACK` collapse a five-column helper table into one formula but need a current Microsoft 365 build; keep the helper-column version if the file is shared widely.

### Interview angle
> [!question] How it is asked
> "Classify these SKUs into A, B and C in Excel and tell me what you would do differently for each class."

> [!tip] Strong answer includes
> - Value = quantity x price (or unit cost) for the period; sort, cumulative %, cut-offs 80/95
> - Boundary convention and why `<=` is used; XYZ/VED as a second lens
> - Policy by class: A tight control and frequent review, C simple rules and larger buffers
> - Re-run periodically; ABC changes as demand changes

---
## 7. Running Totals, Ranking & Percent of Total
> 🔴 Tier 1 · _Key points:_ expanding ranges, running total by group, RANK.EQ, share, MoM change

### Definition
A **running total** uses an expanding range with a fixed start: `=SUM($H$2:H2)`. A running total **by group** uses `SUMIFS` on the expanding range with the group key. `RANK.EQ(x, range, [order])` returns rank (1 = largest by default); ties get the same rank. Percent of total divides by an absolute reference: `=H2/SUM($H$2:$H$21)`.

| Q | Task | Formula | Answer |
|---|---|---|---|
| 36 | Cumulative value to row 6 | `=SUM($H$2:H6)` | 3,54,000 |
| 37 | Running total for the row's customer (row 8, Bajaj Auto) | `=SUMIFS($H$2:H8,$C$2:C8,C8)` | 1,23,000 (SO-1002 + SO-1007) |
| 38 | Rank of SO-1004 by value | `=RANK.EQ(H5,$H$2:$H$21)` | 1 |
| 39 | SO-1004 share of total | `=H5/SUM($H$2:$H$21)` | 11.42% |
| 40 | Largest order of Tata Motors | `=MAXIFS(H2:H21,C2:C21,"Tata Motors")` | 1,00,000 |
| 41 | Largest order of Eicher (legacy array-style) | `=AGGREGATE(14,6,H2:H21/(C2:C21="Eicher"),1)` | 56,000 |
| 42 | January to February change in revenue | `=SUMPRODUCT((MONTH(B2:B21)=2)*H2:H21)/SUMPRODUCT((MONTH(B2:B21)=1)*H2:H21)-1` | -46.2% |

Q41 is an Excel idiom (the `6` option ignores the `#DIV/0!` errors created by non-matching rows); on current Excel `MAXIFS` is simpler. `MAXIFS` and `MINIFS` need Excel 2019 or later. The monthly totals are ₹5,58,000 (January), ₹3,00,000 (February) and ₹3,24,000 (March to 16-Mar, so a partial month): the -46.2% is real in the data but March must not be compared as a full month.

### Example
Running total by customer is how a credit controller sees exposure building over time; the same logic with an `Open` status filter gives open exposure. To rank within a group, `=COUNTIFS($C$2:$C$21,C2,$H$2:$H$21,">"&H2)+1` returns 1 for each customer's largest order. In 365 use `SORTBY`/`TAKE` or `GROUPBY` for top-N per group.

### In the news
See news box. In models that must survive older Excel versions, keep `SUMIFS`/`COUNTIFS` rank logic instead of `SCAN` or `GROUPBY`.

### Interview angle
> [!question] How it is asked
> "Add a column that shows each customer's cumulative spend, and another that ranks customers within region."

> [!tip] Strong answer includes
> - Anchoring the start of the range (`$H$2`), relative end
> - `SUMIFS` with expanding ranges for grouped running totals; `COUNTIFS(...,">"&x)+1` for group rank
> - Percent of total with an absolute denominator; avoiding division by zero with `IFERROR` or `IF`
> - Mention PivotTable "Running Total In" and "% of Column Total" as the no-formula route

---
## 8. Deduplication & Text Clean-up
> 🔴 Tier 1 · _Key points:_ flag duplicates, keep first or last, UNIQUE, TRIM/CLEAN, split text

### Definition
Always **flag before you delete**. `=COUNTIF($C$2:C2,C2)>1` is TRUE from the second occurrence of a value on (keeps the first); `=COUNTIFS(C2:$C$21,C2)=1` is TRUE only for the last occurrence (keeps the latest if rows are in date order). For whole-row duplicates use `UNIQUE(A2:K21)` (365) or Data > Remove Duplicates (destructive, so copy first). Clean text with `TRIM` (spaces), `CLEAN` (non-printing), `SUBSTITUTE(x,CHAR(160)," ")` (non-breaking space), `VALUE`, `PROPER`. Convert text numbers with `VALUE` or `--`.

| Q | Task | Formula | Answer |
|---|---|---|---|
| 43 | Is C8 a repeat of an earlier customer? | `=COUNTIF($C$2:C8,C8)>1` | TRUE (Bajaj Auto first appears in row 3) |
| 44 | Is C2 the last order of that customer? | `=COUNTIFS(C2:$C$21,C2)=1` | FALSE |
| 45 | SKU family (text before the dash) | 365: `=TEXTBEFORE(E2,"-")`; legacy: `=LEFT(E2,FIND("-",E2)-1)` | BRG |
| 46 | Count SKUs ending in "-M12" | `=COUNTIF(E2:E21,"*-M12")` | 3 |
| 47 | Number of SKUs in the "Seals" category of the master | `=SUMPRODUCT((SKU!$B$2:$B$7="Seals")*1)` | 2 |
| 48 | Median order value for the West (legacy needs Ctrl+Shift+Enter) | `=MEDIAN(IF(D2:D21="West",H2:H21))` | 55,250 |

`COUNTIF` wildcards: `*` any text, `?` one character, `~*` a literal star. A common trap: `COUNTIF` treats long numbers as 15-digit numbers and text IDs that differ after 15 characters can match falsely; use `SUMPRODUCT(--(range=cell))` for exact comparison of long IDs. A second trap is trailing spaces ("Tata Motors ") that make `UNIQUE` and pivots list one customer twice.

### Example
Duplicate-invoice check on an AP extract: a helper `=COUNTIFS(Vendor,B2,InvoiceNo,C2,Amount,D2)>1` flags suspected double payments; sort the flags to the top and review. Data cleaning at larger scale moves to Power Query (Remove Duplicates, Trim, Split Column, Change Type with locale) or to Python, see [[075 Pivot Tables & Power Query]] and [[186 Python Data Cleaning & EDA Playbook]].

### In the news
See news box. Where the `REGEX*` functions are available they replace long `LEFT/MID/FIND` chains for patterns such as extracting a PO number from free text; where they are not, keep Power Query.

### Interview angle
> [!question] How it is asked
> "This vendor list has duplicates and extra spaces. How do you clean it and keep an audit trail?"

> [!tip] Strong answer includes
> - Copy raw data, never overwrite; add flag columns first
> - `TRIM`/`CLEAN`/non-breaking-space fix before de-duplicating
> - Keep-first vs keep-latest logic with `COUNTIF` expanding ranges or `UNIQUE`
> - Power Query for repeatable clean-ups; report rows removed

---
## 9. Pivot-Table Questions
> 🔴 Tier 1 · _Key points:_ layout, value field settings, grouping, slicers, GETPIVOTDATA, pivot vs formula

### Definition
Expected pivot results on the dataset (insert PivotTable from the `Orders` range):

| Pivot (Rows, Columns, Values) | Result |
|---|---|
| Region x Status, Sum of Value | West 5,76,000 delivered / 1,48,000 open = 7,24,000; South 2,01,000 / 87,500 = 2,88,500; North 1,19,500 / 50,000 = 1,69,500; Grand total 11,82,000 |
| Customer, Sum of Value, sorted descending | Ashok Leyland 2,88,500; Tata Motors 2,52,500; Bajaj Auto 2,49,000; Mahindra 2,22,500; Eicher 1,69,500 |
| Region, Sum of Value, shown as % of Grand Total | West 61.3%; South 24.4%; North 14.3% |
| Order Date grouped by Months, Sum of Value | Jan 5,58,000; Feb 3,00,000; Mar 3,24,000 |
| Customer, Count of OrderID | 4 each |

Typical questions: (Q49) create the pivot and show value as a percent of column total; (Q50) group dates by month and quarter; add a **slicer** and a **timeline**; add a **calculated field** (a formula on summed fields; it cannot use `IF` on rows and sums before it divides, so a ratio such as average price must be built as a calculated field `=Value/Qty`, not by averaging row prices) and a **calculated item**; use `GETPIVOTDATA("Value",$A$3,"Region","West")` to pull a pivot cell into a report (auto-created when you click a pivot cell while typing `=`); refresh after source changes (convert the source to a Table, or use the Data Model/Power Pivot for multi-table relationships and `DISTINCTCOUNT`).

### Example
Pivot vs formulas: a pivot answers "what does the data say" in seconds and is easy to slice, but it does not refresh by itself, cannot be nested in other formulas as easily and breaks if headers change. Formulas (`SUMIFS`, `GROUPBY`) are live and traceable but need more building. In interviews, say which you would use and why: pivots for exploration and managerial views, formulas for models and templates. More on the mechanics is in [[075 Pivot Tables & Power Query]].

### In the news
See news box. `GROUPBY` and `PIVOTBY` bring pivot-style summaries into live formulas (with the update-channel caveat), but PivotTables keep interactive features such as slicers and drill-down.

### Interview angle
> [!question] How it is asked
> "Create a summary of revenue by region and status, show each region's share, and make it update when new data is added."

> [!tip] Strong answer includes
> - Source as a Table so the pivot range grows; refresh (or refresh on open)
> - Show Values As (% of total, running total), grouping dates, slicers
> - Calculated fields for ratios; avoid averaging averages
> - Data Model/DAX for multi-table or distinct counts; know when to move to Power BI ([[044 Power BI & DAX]])

---
## 10. What-If, Goal Seek & Break-Even
> 🔴 Tier 1 · _Key points:_ Goal Seek, data tables, Scenario Manager, break-even, sensitivity

### Definition
- **Goal Seek** (Data > What-If Analysis): change one input cell until a formula cell hits a target value.
- **Data Table**: recalculates a formula for a range of one or two inputs (row and column input cells); results use `{=TABLE(...)}`.
- **Scenario Manager** stores named sets of inputs; better practice is a scenario switch cell with `CHOOSE`/`INDEX` (see [[188 Financial Modelling in Excel]]).
- **Solver** optimises with constraints ([[077 Solver, Goal Seek & What-If Analysis]]).

Worked numbers for BRG-6205 (price ₹250, unit cost ₹150, fixed cost ₹5,00,000 for the period):

| Question | Answer | Formula or method |
|---|---|---|
| Contribution per unit | ₹100 | `=250-150` |
| Break-even quantity | 5,000 units | `=500000/(250-150)` |
| Result at the 1,500 units sold in the dataset | loss of ₹3,50,000 | `=1500*100-500000` |
| Price for a 45% gross margin | ₹272.73 | Goal Seek on price so that `(price-150)/price` = 45%, or algebra `=150/(1-0.45)` |
| Revenue given up if orders of 1,000 units or more get 2 extra points of discount | ₹5,000 (2% of ₹2,50,000 on six orders) | `=0.02*SUMIFS(H2:H21,F2:F21,">=1000")` |

### Example
Data table for break-even quantity versus price: put prices 240, 250, 260, 270 down a column and the formula `=500000/(price-150)` at the top; with column input cell = price you get 5,556; 5,000; 4,545; 4,167 units. Each ₹10 price rise lowers break-even by about 10% at ₹250. Goal Seek returns 272.73 because 122.73/272.73 = 45%. Say aloud that Goal Seek gives one number for one target, a data table gives the sensitivity, and Solver handles constraints.

### In the news
See news box. Interview tests increasingly forbid AI help; the `COPILOT` function's retirement is a reminder that what-if work should rest on explicit, auditable inputs.

### Interview angle
> [!question] How it is asked
> "At what selling price does this product reach a 45% margin, and how sensitive is break-even to price?"

> [!tip] Strong answer includes
> - Names the tool for the question: Goal Seek (one target), Data Table (sensitivity), Scenario switch (cases), Solver (constraints)
> - Inputs on a separate, labelled assumptions area; no hard-coded numbers in formulas
> - Break-even = fixed cost / contribution per unit; operating-leverage intuition
> - Interprets results in business terms (₹ impact, volume needed)

---
## 11. Timed Case Exercises
> 🔴 Tier 1 · _Key points:_ four 15-20 minute cases on the practice dataset with answer keys

### Definition
Set a timer; produce the numbers, one chart and a one-line "so what". Answer keys follow the case lists.

**Case A: Delivery performance (15 min).** (1) On-time rate of delivered orders. (2) Number and value of late orders. (3) Average delay of late orders. (4) Which customer suffers most? (5) Overdue open orders at 20-Mar-26.

**Case B: Revenue and mix (20 min).** (1) Revenue by region, customer and month. (2) Top customer and its share. (3) Gross margin overall and by SKU. (4) One chart and a recommendation.

**Case C: Inventory policy for BRG-6205 (20 min).** Assume the 1,500 units sold over 90 days (1 Jan to 31 Mar) are the demand, daily demand standard deviation 6 units, lead time 7 days (SKU sheet), order cost ₹500, holding cost 20% of unit cost, 95% service level. Compute daily and annual demand, EOQ, safety stock and reorder point.

**Case D: Discount what-if (15 min).** Orders of 1,000 units or more get 2 extra discount points. Revenue given up? Margin effect? Is it worth it if it lifts those customers' volume by 10%?

### Example
**Answer key.** Case A: 10 of 16 on time = 62.5%; 6 late orders (SO-1002, 1004, 1007, 1010, 1013, 1016) worth ₹3,86,500 (43.1% of delivered value ₹8,96,500); average delay 18/6 = 3.0 days (maximum 5 days, SO-1004); Bajaj Auto worst with 2 of 3 delivered orders late; overdue open orders at 20-Mar: SO-1017 (7 days) and SO-1018 (2 days), value ₹1,58,000. Average order-to-delivery time of delivered orders is 8.4 calendar days.
Case B: West ₹7,24,000 (61.3%), South ₹2,88,500 (24.4%), North ₹1,69,500 (14.3%); top customer Ashok Leyland ₹2,88,500 (24.4%) with Tata Motors second at 21.4%; months ₹5,58,000, ₹3,00,000, ₹3,24,000 (March partial); gross margin 36.85% (₹4,35,600) with Seals 45% and Hydraulics 31.1%. Recommendation: protect Hydraulics margin (largest low-margin line, ₹3,33,000 revenue) through price or cost action, and fix the single dominant West region dependency.
Case C: daily demand 1,500/90 = 16.67; annual 16.67 x 365 = 6,083; holding cost 0.2 x 150 = ₹30; EOQ = $\sqrt{2\cdot6083\cdot500/30}$ = 450.3 units; safety stock = 1.645 x 6 x $\sqrt7$ = 26.1; ROP = 16.67 x 7 + 26.1 = 142.8. Excel: `=SQRT(2*6083.33*500/30)`, `=NORM.S.INV(0.95)*6*SQRT(7)`.
Case D: six orders qualify (SO-1002, 1003, 1008, 1009, 1012, 1019) worth ₹2,50,000; two extra discount points cost ₹5,000 at current volume. A 10% volume lift adds ₹25,000 revenue before discount; those six orders (seals, fasteners, steel) have a blended gross margin of 38.2% (cost ₹1,54,600 on ₹2,50,000), so the lift adds about ₹9,500 gross margin. Subtracting the ₹5,000 giveaway and the discount on the extra volume (about ₹500) leaves roughly +₹4,000: marginally positive, small, and sensitive to the volume assumption (at a 5% lift the net is about -₹500).

### In the news
See news box. In a live case, structure beats speed: state your plan, build one clear table or chart, and quote the "so what" before the number of decimals.

### Interview angle
> [!question] How it is asked
> "Here is a month of orders. Tell me what is going on with delivery and where the money is made."

> [!tip] Strong answer includes
> - Plan first (metrics, definitions, checks), then build; label units and as-of date
> - Control totals ties out (₹11,82,000) and a sanity check on each answer
> - Insight and action, not just numbers (late orders concentrate in two customers; Hydraulics margin; West dependency)
> - Links operations metrics ([[012 Supply Chain Analytics & KPIs]]) to financial impact

---
## 12. Formula-Audit Questions & Common Mistakes
> 🔴 Tier 1 · _Key points:_ spot the bug, reference types, hidden hard-codes, approximate-match traps, circularity

### Definition
Audit questions give a formula or a sheet and ask "what is wrong?" Tools: Trace Precedents/Dependents (Ctrl+[ and Ctrl+]), Evaluate Formula, Show Formulas (Ctrl + grave accent), Error Checking, Go To Special (formulas, constants, blanks, differences), the Inquire add-in, and `ISFORMULA`/`FORMULATEXT`.

| # | Flawed formula or sheet | Problem | Fix |
|---|---|---|---|
| A1 | `=VLOOKUP(E2,SKU!A:E,3)` | Missing 4th argument: approximate match on an unsorted list; hard-coded column 3 | `=VLOOKUP(E2,SKU!A:E,3,FALSE)` or `XLOOKUP` |
| A2 | `=H2/SUM(H2:H21)` filled down | Denominator range moves (no `$`) | `=H2/SUM($H$2:$H$21)` |
| A3 | `=SUM(H2:H20)` while data runs to row 21 | Range stops short; new rows missed | Use a Table `SUM(tblOrders[Value])` |
| A4 | `=SUMIF(C2:C21,"Tata*",H2:H21)` | Wildcard also matches "Tata Steel" etc. | Exact criterion, or a unique customer ID |
| A5 | `=IF(F2>1000,0.04,IF(F2>500,0.02,0))` | Hard-coded slabs and boundary (>=1,000 qualifies for 4% in the table) | Lookup table with `LOOKUP/XLOOKUP`; `>=` semantics |
| A6 | `=B2+30` where B2 contains the text "05-Jan-26" | Date stored as text; result `#VALUE!` or wrong | Convert with `DATEVALUE` or Text to Columns; check `ISNUMBER` |
| A7 | `=A2*1.18` | Hard-coded GST rate buried in the formula | Input cell `Tax_Rate`, referenced absolutely |
| A8 | Total row inside the SUMIF range; pivot built on a range containing a total row | Double counting | Keep totals outside the data block |
| A9 | `=H2*G3` pattern drifting across rows | Inconsistent formulas down a column | Consistent formula per column; use `Go To Special > Row differences` |
| A10 | Circular reference warning after adding interest on average balance | Formula depends on its own result | Redesign, or enable iterative calculation deliberately with a circuit breaker |

**Common mistakes in tests:** typing numbers instead of referencing cells; merged cells that block sorting and pivots; blank rows inside data; mixing units (units, kg, cartons); not freezing panes; no labels or units; volatile functions (`OFFSET`, `INDIRECT`, `TODAY`) in big models; pasting values over formulas without noting it; presenting unformatted results (no thousands separators or ₹ symbol); not testing with an edge case (empty cell, zero, text).

### Example
A1 on SKU "BOLT-M12" with an unsorted master: approximate match returns whichever row the binary search lands on, so a plausible but wrong cost, and no error. The audit habit is to test the formula with a value you know the answer to (150 for BRG-6205) and with a value that must fail ("XYZ"). For A5, a quantity of exactly 1,000 gets 4% in the slab table (min 1,000) but 2% in the hard-coded `IF` because of `>1000`: a boundary mismatch like this is a classic source of reconciliation breaks. The model-review side of this is in [[188 Financial Modelling in Excel]].

### In the news
See news box. AI-generated formulas make audit skills more valuable: the retired `COPILOT` function carried an explicit validation caveat, and generated formulas have the same failure modes as A1 to A10.

### Interview angle
> [!question] How it is asked
> "Review this workbook before it goes to the CFO. What would you check?"

> [!tip] Strong answer includes
> - Structure first (inputs, calculations, outputs, version, units), then formulas (consistency, hard-codes, ranges), then results (totals tie out, sign and magnitude checks)
> - Named tools: Trace Precedents, Evaluate Formula, Go To Special, error checking
> - Specific bug classes (reference drift, approximate match, text-numbers, double counting)
> - Reporting findings with severity and fixes, not silently changing the file

---
## 13. Keyboard-Speed List & Drills
> 🔴 Tier 1 · _Key points:_ ten shortcuts that save minutes, mouse-free workflow, timed drills

### Definition
Windows shortcuts that matter in timed tests (Mac equivalents differ; Cmd often replaces Ctrl, and some Alt sequences do not exist).

| Goal | Keys |
|---|---|
| Jump to the edge of data / select to the edge | `Ctrl+Arrow` / `Ctrl+Shift+Arrow` |
| Select the data region / whole sheet | `Ctrl+A` (press again for the sheet) |
| Insert an Excel Table | `Ctrl+T` |
| AutoSum | `Alt+=` |
| Cycle absolute/relative reference | `F4` while editing a reference |
| Edit cell / evaluate part of a formula | `F2` / `F9` (undo with Esc) |
| Fill the same entry into a selection | `Ctrl+Enter` |
| Fill down / right | `Ctrl+D` / `Ctrl+R` |
| Toggle filters | `Ctrl+Shift+L` |
| Paste Special (values) | `Ctrl+Alt+V`, then `V`, Enter |
| Format cells / number, currency, percent formats | `Ctrl+1` / `Ctrl+Shift+1`, `Ctrl+Shift+4`, `Ctrl+Shift+5` |
| Show formulas / trace precedents | `Ctrl` + grave-accent key / `Ctrl+[` |
| Insert PivotTable | `Alt, N, V` |
| Go To Special | `F5` then `Alt+S` (or `Ctrl+G`) |
| Today's date / current time | `Ctrl+;` / `Ctrl+Shift+;` |
| New line inside a cell | `Alt+Enter` |
| Autofit column width | `Alt, H, O, I` |
| Move between sheets | `Ctrl+PgUp` / `Ctrl+PgDn` |
| Remove Duplicates dialog | `Alt, A, M` |
| Evaluate Formula dialog | `Alt, M, V` |

**Drills (5 minutes each).** (1) From a blank sheet: paste the dataset, `Ctrl+T`, name the table, add a `Value` column, total with `Alt+=`; target under 90 seconds. (2) Fill a calculated column for 20 rows with `Ctrl+Enter` and convert to values with `Ctrl+Alt+V`. (3) Build the Region x Status pivot with `Alt, N, V` and format as ₹ with `Ctrl+1`; target under 2 minutes.

### Example
Speed comes from not leaving the keyboard: `Ctrl+Shift+Down` to select a column of data, `Alt+=` to total it, `F4` to lock a reference while typing, `Ctrl+Enter` to apply one formula to a pre-selected range. In a 30-minute test the saving is typically several minutes, which buys time for checks. Practising these on the foundations in [[070 Foundations & Navigation]] is enough.

### In the news
See news box. Excel's ribbon and Alt key sequences can differ across builds and languages; confirm the sequences on the machine you will use in the interview.

### Interview angle
> [!question] How it is asked
> "Share your screen and build this summary while I watch." (Navigation speed is observed.)

> [!tip] Strong answer includes
> - Fluent use of Tables, `F4`, `Ctrl+Arrow`, `Alt+=`, filters and pivots without hunting through menus
> - Narrating while working (what and why)
> - Checking totals before presenting
> - Calm recovery from errors (Ctrl+Z, Evaluate Formula)

---
## 14. ⭐ Advanced: LET, LAMBDA, Power Query & Python Hand-offs
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Advanced rounds ask when a formula is the wrong tool. **`LET`** names sub-expressions; **`LAMBDA`** creates reusable custom functions saved in Name Manager (for example `=LAMBDA(x, y, x/y-1)` as `GROWTH`); helpers `MAP`, `BYROW`, `BYCOL`, `REDUCE`, `SCAN` apply them across arrays. Use **Power Query** when the job is repeatable data preparation (import, merge, unpivot, clean), **PivotTables/Data Model** for exploration and measures, **VBA/Office Scripts** for UI automation ([[189 VBA, Macros & Office Scripts Basics]]), and **Python** (including Python in Excel) when logic is complex, data large or the work needs testing ([[185 Python Interview Problem Bank]]).

```excel
=LET(late, J2:J21 > I2:I21,
     n,    COUNT(J2:J21),
     HSTACK(1 - SUM(--late) / n,
            SUM(late * (J2:J21 - I2:I21)) / SUM(--late)))
```
Result: 62.5% and 3.0 days, the same as the earlier `SUMPRODUCT` versions (cross-checked in pandas). `late` and `n` are computed once and reused.

A reusable function via Name Manager: name `OTIF_RATE`, refers to `=LAMBDA(promised, delivered, 1 - SUM(--(delivered > promised)) / COUNT(delivered))`; call it as `=OTIF_RATE(I2:I21, J2:J21)`, which returns 62.5%.

### Example
Decision rule to state in the interview: a one-off number from a small sheet is a formula; a weekly report from changing SAP exports is Power Query (documented steps, refresh); a model with branching logic, tests or millions of rows is Python; a button for non-technical users is a macro or Office Script. Equivalent SQL for the same questions is in [[181 SQL Interview Problem Bank]].

### In the news
See news box. Because functions such as `GROUPBY`, `REGEX*` and `TAKE` arrive by channel and `COPILOT()` was withdrawn, build interview answers on durable functions (`SUMIFS`, `INDEX/MATCH`, `SUMPRODUCT`) and mention the new ones as upgrades.

### Interview angle
> [!question] How it is asked
> "When would you use LET or LAMBDA, and when would you stop using formulas altogether?"

> [!tip] Strong answer includes
> - `LET` for readability and speed; `LAMBDA` for reuse and consistency; the compatibility cost
> - Power Query for ETL, Python for complex or large analysis, VBA/Scripts for UI tasks
> - Maintainability: documentation, named inputs, tests on known answers
> - Awareness of version and channel availability
