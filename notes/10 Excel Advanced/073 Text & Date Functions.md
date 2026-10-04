---
tags: [excel-advanced, tier1]
area: Excel Advanced
topic: "Text & Date Functions"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Text & Date Functions

⬅ [[072 Logical & Statistical Functions]] · [[_Index - Excel Advanced|Excel Advanced]] · [[074 Array & Dynamic Array Functions]] ➡

> **Area:** Excel Advanced · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. LEFT / RIGHT / MID]]
2. [[#2. LEN / FIND / SEARCH]]
3. [[#3. TRIM / CLEAN]]
4. [[#4. CONCATENATE / CONCAT / &]]
5. [[#5. TEXT Function]]
6. [[#6. UPPER / LOWER / PROPER]]
7. [[#7. SUBSTITUTE / REPLACE]]
8. [[#8. VALUE / NUMBERVALUE]]
9. [[#9. TODAY / NOW]]
10. [[#10. DATEDIF / NETWORKDAYS]]
11. [[#11. ⭐ Advanced: TEXTSPLIT, TEXTBEFORE and TEXTAFTER (365)]]
12. [[#12. ⭐ Advanced: Date Engineering: EDATE, EOMONTH and Indian Fiscal Year]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI arrives inside the Excel cell, then retreats
> **COPILOT() function (Aug 2025).** On 19 Aug 2025 Microsoft announced a `=COPILOT("prompt", range)` worksheet function, rolled out first to Beta Channel users with Microsoft 365 Copilot licences on Windows and Mac. Example from the launch: `=COPILOT("What is the sentiment of the comment in cell A2?")`; demos included cleaning messy text by extracting names and phone numbers. ([GeekWire](https://www.geekwire.com/2025/excel-formula-meets-ai-prompt-microsoft-brings-new-copilot-function-to-spreadsheet-cells/))
> 
> **Retirement (Aug 2026).** The Register reports Microsoft decided not to move forward with the function; it stays in preview and retires on **14 Sep 2026**, with the Copilot side pane as the alternative. Lesson: deterministic text functions (LEFT, TRIM, TEXTSPLIT) remain the auditable way to clean data; AI output "should be reviewed and validated". ([The Register](https://www.theregister.com/ai-and-ml/2026/08/17/excels-copilot-function-is-headed-for-the-recycle-bin/5288327))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. LEFT / RIGHT / MID
> 🔴 Tier 1 · _Tracker hint:_ =LEFT(A1,3); =RIGHT(A1,4); =MID(A1,3,5); extract substrings

### Definition
These three functions slice a text string by position.

```excel
=LEFT(text, [num_chars])        -- first n characters (default 1)
=RIGHT(text, [num_chars])       -- last n characters
=MID(text, start_num, num_chars) -- n characters starting at position start_num (1-based)
```

Results are always **text**, even if they look like numbers (so `=LEFT("2025-26",4)` returns "2025" as text; wrap in `VALUE()` or `--` to use it in maths). Typical uses in operations: pulling a plant code, state code or year out of a structured ID. Example: SKU `MUM-FG-00452`, `=LEFT(A2,3)` gives `MUM`, `=MID(A2,5,2)` gives `FG`, `=RIGHT(A2,5)` gives `00452`. A GSTIN's first two characters are the state code, so `=LEFT(B2,2)` gives `27` for Maharashtra. Fixed positions work only if the structure is fixed; for variable-length parts combine with FIND (next sub-topic).

### Example
Material code `RM-STL-2025-0731`. Quarter sheet needs the year and serial:
- Year: `=MID(A2,8,4)` returns `2025` (characters 8 to 11: R=1, M=2, "-"=3, S=4, T=5, L=6, "-"=7, then 2025 starts at 8).
- Serial: `=RIGHT(A2,4)` returns `0731`.
- Numeric serial: `=VALUE(RIGHT(A2,4))` returns 731.

### In the news
See news box. The COPILOT function was pitched for the same extraction jobs (names, phone numbers); LEFT/MID are the free, deterministic way when the pattern is fixed.

### Interview angle
> [!question] How it is asked
> "You have 10,000 SKU codes like MUM-FG-00452. How do you split out the warehouse code?" or a live Excel test on extracting substrings.

> [!tip] Strong answer includes
> - Syntax of all three and that MID needs a start position
> - Remember outputs are text; convert with VALUE when needed
> - Say fixed-position vs variable-length: switch to FIND/SEARCH or TEXTSPLIT
> - Mention Flash Fill/Text to Columns as quick alternatives, formulas for repeatable work

---

## 2. LEN / FIND / SEARCH
> 🔴 Tier 1 · _Tracker hint:_ =LEN(A1); =FIND('_',A1) case-sensitive; =SEARCH('_',A1) case-insensitive

### Definition
```excel
=LEN(text)                              -- number of characters (spaces included)
=FIND(find_text, within_text, [start])  -- position, case-sensitive, no wildcards
=SEARCH(find_text, within_text, [start])-- position, case-insensitive, allows ? and * wildcards
```
Both FIND and SEARCH return `#VALUE!` if not found, so wrap with `IFERROR`. Their real power is feeding LEFT/MID/RIGHT for variable-length text:

- Text before the first underscore: `=LEFT(A1, FIND("_",A1)-1)`
- Text after it: `=MID(A1, FIND("_",A1)+1, LEN(A1))`
- Count of a character: `=LEN(A1)-LEN(SUBSTITUTE(A1,"-",""))`

Use FIND when case matters (`"a"` differs from `"A"`), SEARCH when it does not or when you need wildcards.

### Example
`A1 = "Pune_Plant2_Line7"`.
- `FIND("_",A1)` = 5, so `=LEFT(A1,5-1)` = `Pune`.
- Second underscore: `=FIND("_",A1,FIND("_",A1)+1)` = 12 (P-u-n-e=4, "_"=5, Plant2 = 6 to 11, "_"=12).
- `LEN(A1)` = 17, so line code = `=RIGHT(A1,17-12)` = `Line7`.

### In the news
See news box. AI formula helpers can generate such nested formulas, but you still need to understand FIND positions to verify them.

### Interview angle
> [!question] How it is asked
> "Extract the first name from 'Basu, Samriddha'" or "What is the difference between FIND and SEARCH?"

> [!tip] Strong answer includes
> - Case-sensitive vs case-insensitive, wildcard support only in SEARCH
> - Using FIND inside LEFT/MID for variable length
> - IFERROR wrapper for missing delimiters
> - LEN trick to count occurrences of a character

---

## 3. TRIM / CLEAN
> 🔴 Tier 1 · _Tracker hint:_ =TRIM(A1) removes extra spaces; =CLEAN(A1) removes non-printable characters

### Definition
```excel
=TRIM(text)   -- removes leading/trailing spaces and collapses internal runs of spaces to one
=CLEAN(text)  -- removes non-printable ASCII characters (codes 0 to 31), e.g. line breaks from system exports
```
Data exported from SAP, ERP or web pages often has invisible junk that makes `VLOOKUP`/`XLOOKUP` return `#N/A` even though two cells "look identical". Two gotchas: TRIM does not remove the **non-breaking space** (character 160) common in web data, fix with `=TRIM(SUBSTITUTE(A1,CHAR(160)," "))`; CLEAN does not remove CHAR(160) either. Standard cleaning pattern: `=TRIM(CLEAN(A1))`. After cleaning, copy and Paste Special > Values to replace the raw column.

### Example
Vendor master has `"Tata Steel "` (trailing space) while the PO sheet has `"Tata Steel"`. `=XLOOKUP(B2, Vendors!A:A, Vendors!B:B)` fails. Check: `LEN("Tata Steel ")` = 11 vs `LEN("Tata Steel")` = 10. `=TRIM(A2)` gives 10 and the lookup works.

### In the news
See news box. Messy-text clean-up was a headline use case of the COPILOT function; TRIM/CLEAN are the deterministic, auditable version.

### Interview angle
> [!question] How it is asked
> "Your VLOOKUP returns #N/A though the values look identical. What do you check?"

> [!tip] Strong answer includes
> - Hidden spaces, non-printing characters, text vs number mismatch
> - Diagnose with LEN comparison
> - TRIM(CLEAN()) and the CHAR(160) caveat
> - Fix at source (Power Query Trim/Clean) for repeatable refreshes

---

## 4. CONCATENATE / CONCAT / &
> 🔴 Tier 1 · _Tracker hint:_ =A1&' '&B1; =concat(A1:C1); =textjoin(', ',TRUE(),A1:A10)

### Definition
Joining text from several cells.

| Method | Syntax | Notes |
|---|---|---|
| Ampersand | `=A1&" "&B1` | Fastest to type, most used |
| CONCATENATE | `=CONCATENATE(A1," ",B1)` | Legacy; no ranges |
| CONCAT | `=CONCAT(A1:C1)` | Accepts ranges, no delimiter |
| TEXTJOIN | `=TEXTJOIN(", ",TRUE,A1:A10)` | Delimiter plus ignore-empty flag; best for lists |

Numbers and dates join as raw serial values unless wrapped in `TEXT()`: `="Due: "&TEXT(B2,"dd-mmm-yyyy")`. TEXTJOIN with `FILTER` creates conditional lists: `=TEXTJOIN(", ",TRUE,FILTER(A2:A100,B2:B100="Late"))` lists all late suppliers in one cell. Build lookup keys with `=A2&"|"&B2` (a composite key) when matching on two columns.

### Example
Mailing label from columns First, Last, City: `=PROPER(A2&" "&B2)&", "&C2` returns `Samriddha Basu, Nashik`. TEXTJOIN example: A2:A5 = Pune, blank, Nashik, Mumbai gives `=TEXTJOIN(", ",TRUE,A2:A5)` = `Pune, Nashik, Mumbai` (blank skipped because the second argument is TRUE).

### In the news
See news box. Natural-language prompts are replacing some manual string assembly, but TEXTJOIN remains the reliable way to build lists.

### Interview angle
> [!question] How it is asked
> "How do you combine first and last names?" or "How do you list all items that meet a condition in one cell?"

> [!tip] Strong answer includes
> - Ampersand vs CONCAT vs TEXTJOIN with trade-offs
> - Wrap dates and numbers in TEXT()
> - TEXTJOIN + FILTER for conditional lists
> - Composite keys for two-column lookups

---

## 5. TEXT Function
> 🔴 Tier 1 · _Tracker hint:_ =TEXT(A1,'dd-mmm-yyyy'); =TEXT(A1,'#,##0.00'); number/date formatting for display

### Definition
```excel
=TEXT(value, format_text)
```
Converts a number or date to **text** with a chosen display format. Common codes:

| Format | Meaning | 45200 / 1234567.8 becomes |
|---|---|---|
| `dd-mmm-yyyy` | day-month-year | 01-Oct-2023 |
| `mmmm` | full month name | October |
| `ddd` | weekday short | Sun |
| `#,##0.00` | thousands separator, 2 decimals | 1,234,567.80 |
| `0.0%` | percentage | (0.256 gives 25.6%) |
| `000000` | zero-pad | 000731 for 731 |

Because the result is text, you cannot sum it; keep the original numeric cell for calculation and use TEXT only for labels, dashboard titles and keys. Indian-style lakh grouping cannot be done by `#,##0` alone (it groups in thousands); use a custom cell format `[>=10000000]##\,##\,##\,##0;[>=100000]##\,##\,##0;##,##0` for display. Format codes are locale-dependent in some regional settings.

### Example
Dashboard title: `="Sales as of "&TEXT(TODAY(),"dd-mmm-yyyy")` shows `Sales as of 02-Oct-2026` on 2 Oct 2026. Leading zeros: PO number 731 shown as `=TEXT(731,"PO-00000")` = `PO-00731`.

### In the news
See news box. COPILOT output was returned as plain text too; for finance-grade labels TEXT with an explicit format is predictable.

### Interview angle
> [!question] How it is asked
> "How do you show a date as 'Oct-2026' in a formula result?" or "Why can't I sum cells created with TEXT?"

> [!tip] Strong answer includes
> - Syntax and 3 or 4 format codes from memory
> - Output is text, not numeric
> - Use for dynamic labels and zero-padded IDs
> - Know the difference from cell Number Formatting (display only, value unchanged)

---

## 6. UPPER / LOWER / PROPER
> 🔴 Tier 1 · _Tracker hint:_ =PROPER(A1) — Title Case; useful for name/address standardization

### Definition
```excel
=UPPER(A1)   -- ALL CAPS
=LOWER(A1)   -- all lowercase
=PROPER(A1)  -- Capitalises The First Letter Of Each Word
```
Used to standardise names, cities and codes before matching or de-duplication; `"mumbai"`, `"MUMBAI"` and `"Mumbai"` are equal in Excel lookups but not in Power Query or SQL, so standardise anyway. PROPER capitalises after any non-letter, which breaks some strings: `"o'neil"` becomes `"O'Neil"` (fine) but `"mcdonald"` becomes `"Mcdonald"`, and `"gst number 27ABC"` capitalises letters after digits. Abbreviations like `"HUL"` become `"Hul"`; use UPPER for codes. Combine: `=PROPER(TRIM(A1))`. Case-sensitive comparison uses `EXACT(A1,B1)` since `=` ignores case.

### Example
Address field `"  flat 4, sai  nagar, nashik "`. `=PROPER(TRIM(A1))` gives `Flat 4, Sai Nagar, Nashik`. Email key: `=LOWER(TRIM(B1))` ensures `Sam@Gmail.com` matches `sam@gmail.com`.

### In the news
See news box. Standardising case is a basic data-quality step that AI helpers also automate, but you must verify exceptions like acronyms.

### Interview angle
> [!question] How it is asked
> "How would you clean a customer list with inconsistent capitalisation before de-duplicating?"

> [!tip] Strong answer includes
> - The three functions and when each applies (names vs codes)
> - Combine with TRIM first
> - PROPER pitfalls (acronyms, McDonald)
> - EXACT for case-sensitive comparison; Power Query for large refreshable data

---

## 7. SUBSTITUTE / REPLACE
> 🔴 Tier 1 · _Tracker hint:_ =SUBSTITUTE(A1,'old','new'); =REPLACE(A1,start,len,'new'); text cleaning

### Definition
```excel
=SUBSTITUTE(text, old_text, new_text, [instance_num])  -- replaces by matching text (case-sensitive)
=REPLACE(old_text, start_num, num_chars, new_text)      -- replaces by position
```
SUBSTITUTE swaps every occurrence unless you give `instance_num` (replace only the nth). REPLACE overwrites a fixed block of characters. Use SUBSTITUTE to strip symbols: `=SUBSTITUTE(A1,"₹","")`, remove commas, or turn a line break into a space `SUBSTITUTE(A1,CHAR(10)," ")`. Nest to remove several characters. Counting trick: `=LEN(A1)-LEN(SUBSTITUTE(A1,"x",""))` counts "x". Use REPLACE for masking or format changes: `=REPLACE(A1,5,4,"XXXX")` masks characters 5 to 8. Neither modifies the source; they return new text.

### Example
Amount stored as text `"₹1,25,000"`. `=VALUE(SUBSTITUTE(SUBSTITUTE(A1,"₹",""),",",""))` removes the symbol then the commas, giving 125000. Phone `9876543210` masked: `=REPLACE(A1,3,6,"******")` gives `98******10`.

### In the news
See news box. COPILOT was demoed on cleaning messy data; for repeatable pipelines SUBSTITUTE or Power Query Replace Values is the auditable method.

### Interview angle
> [!question] How it is asked
> "Numbers imported with rupee symbols and commas won't sum. How do you fix them?"

> [!tip] Strong answer includes
> - SUBSTITUTE for matching text, REPLACE for position
> - Nested SUBSTITUTE then VALUE
> - instance_num option
> - Mention Find & Replace for one-offs, formulas/Power Query for repeatable cleaning

---

## 8. VALUE / NUMBERVALUE
> 🔴 Tier 1 · _Tracker hint:_ =VALUE('1,234') → 1234; convert text-stored numbers to numeric

### Definition
```excel
=VALUE(text)                                   -- converts a number-looking text to a number (locale dependent)
=NUMBERVALUE(text, [decimal_sep], [group_sep]) -- locale-independent conversion
```
Numbers stored as text (left-aligned, green triangle, SUM returns 0) are a top cause of wrong totals and failed lookups. Fixes: `VALUE`, double unary `=--A1`, multiply by 1, Text to Columns, or Paste Special > Multiply by 1. NUMBERVALUE helps when the source uses a different separator: `=NUMBERVALUE("1.234,56",",",".")` returns 1234.56. It also handles percentages: `=NUMBERVALUE("12%")` gives 0.12. VALUE also converts date-like text to a date serial: `=VALUE("15-Aug-2025")`. Failing conversions return `#VALUE!`.

### Example
Cells hold text `"1,234"`, `"2,500"`, `"750"`. `=SUM(A1:A3)` returns 0. `=SUMPRODUCT(--SUBSTITUTE(A1:A3,",",""))` strips commas, converts each to 1234, 2500, 750 and returns 4484. `=VALUE(RIGHT("PO-731",3))` returns 731.

### In the news
See news box. AI-based extraction returns text too, so a VALUE step is needed before the numbers feed a model.

### Interview angle
> [!question] How it is asked
> "A column of numbers sums to zero. What is wrong and how do you fix it?"

> [!tip] Strong answer includes
> - Diagnose: text-stored numbers (alignment, ISNUMBER)
> - Several fixes: VALUE, --, Paste Special multiply, Text to Columns
> - NUMBERVALUE for different separators
> - Prevent at source with Power Query data types

---

## 9. TODAY / NOW
> 🔴 Tier 1 · _Tracker hint:_ =TODAY() current date; =NOW() date+time; volatile — recalculates every open

### Definition
```excel
=TODAY()  -- current date (serial number, no time)
=NOW()    -- current date and time
```
Both are **volatile**: they recalculate whenever the workbook calculates or opens, so values change daily and can slow big models. They suit ageing and countdowns: days to delivery `=B2-TODAY()`, invoice age `=TODAY()-C2`, overdue flag `=IF(TODAY()>B2,"Overdue","OK")`. To freeze a timestamp (e.g. when a record was entered) use Ctrl+; for the date, Ctrl+Shift+; for the time, or a VBA/iterative approach, never a formula. Date arithmetic works in days because dates are serial numbers (1 = 1 Jan 1900). Format the cell as Date, otherwise you see a number. For reproducible reports store an "As of" date input and reference it instead of TODAY().

### Example
PO due 15-Oct-2026, today 2-Oct-2026: `=B2-TODAY()` = 13 days. Ageing bucket: `=IF(TODAY()-C2<=30,"0-30",IF(TODAY()-C2<=60,"31-60","60+"))`. An invoice dated 1-Aug-2026 is 62 days old on 2-Oct-2026 (Aug 1 to Sep 1 = 31, to Oct 1 = 61, to Oct 2 = 62), so it falls in "60+".

### In the news
See news box. Volatile live formulas and AI calls both change output between opens, which is why a fixed "As of" date matters for audit.

### Interview angle
> [!question] How it is asked
> "What does volatile mean? How would you build an ageing report?"

> [!tip] Strong answer includes
> - TODAY vs NOW and volatility with performance impact
> - Ageing buckets via nested IF/IFS or LOOKUP
> - Static timestamp shortcuts
> - Use an As-of cell for reproducible reports

---

## 10. DATEDIF / NETWORKDAYS
> 🔴 Tier 1 · _Tracker hint:_ =DATEDIF(start,end,'d') for days, 'm' months, 'y' years; =NETWORKDAYS(start,end,holidays)

### Definition
```excel
=DATEDIF(start, end, unit)     -- unit: "d" days, "m" complete months, "y" complete years,
                               -- "ym" months ignoring years, "md" days ignoring months, "yd" days ignoring years
=NETWORKDAYS(start, end, [holidays])           -- working days, Mon-Fri, inclusive of both ends
=NETWORKDAYS.INTL(start, end, [weekend], [holidays])  -- custom weekends
=WORKDAY(start, days, [holidays])              -- date after n working days
```
DATEDIF is a legacy undocumented function (not in the function wizard) but works; `start` must be earlier than `end` or it returns `#NUM!`; the `"md"` unit can give wrong results, avoid it. NETWORKDAYS counts both start and end days if they are working days. For Indian operations, put plant holidays (Diwali, Republic Day, etc.) in a named range and pass it, and use NETWORKDAYS.INTL when plants run six-day weeks (weekend code `11` = Sunday only).

### Example
Start 1-Jan-2020, end 2-Oct-2026: `DATEDIF(...,"y")` = 6 complete years; `"ym"` = 9 months; `"md"` = 1 day. Lead time: PO 1-Oct-2026 (Thu) to GRN 9-Oct-2026 (Fri): calendar days = 8; `NETWORKDAYS` = 7 (Oct 1, 2, 5, 6, 7, 8, 9; weekend 3-4 excluded), minus 1 if Oct 2 (Gandhi Jayanti) is in the holiday list = 6.

### In the news
See news box. Date logic is deterministic and auditable, unlike an AI-generated answer that "should be reviewed and validated".

### Interview angle
> [!question] How it is asked
> "How would you compute supplier lead time in working days?" or "Calculate an employee's tenure in years and months."

> [!tip] Strong answer includes
> - DATEDIF units and its undocumented status
> - NETWORKDAYS with a holiday range; INTL for custom weekends
> - Inclusive counting and its off-by-one risk
> - WORKDAY to project due dates

---

## 11. ⭐ Advanced: TEXTSPLIT, TEXTBEFORE and TEXTAFTER (365)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Microsoft 365 added dynamic text functions that replace most LEFT/MID/FIND gymnastics:

```excel
=TEXTBEFORE(text, delimiter, [instance_num], ...)  -- text before nth delimiter
=TEXTAFTER(text, delimiter, [instance_num], ...)   -- text after nth delimiter
=TEXTSPLIT(text, col_delimiter, [row_delimiter], [ignore_empty], [match_mode], [pad_with])
```
TEXTSPLIT spills results across cells; a negative `instance_num` counts from the end, so `=TEXTAFTER(A1,"_",-1)` returns the last segment however many underscores exist. Wrap with `IFERROR` or use the `if_not_found` argument. Combine: `=TAKE(TEXTSPLIT(A1,"-"),,-1)` returns the last piece; `=VALUE(TEXTAFTER(A1,"-"))` returns a number.

### Example
`A1 = "Pune_Plant2_Line7"`: `=TEXTSPLIT(A1,"_")` spills `Pune`, `Plant2`, `Line7` into three cells. `=TEXTBEFORE(A1,"_")` = `Pune`; `=TEXTAFTER(A1,"_",2)` = `Line7`. Compare the old `=MID(A1,FIND("_",A1,FIND("_",A1)+1)+1,99)`, which is longer and error-prone.

### In the news
See news box. Microsoft invests in new native functions and AI helpers alike; knowing TEXTSPLIT shows you track the current toolset.

### Interview angle
> [!question] How it is asked
> "Split a full address into columns using formulas" or "What newer Excel functions have you used?"

> [!tip] Strong answer includes
> - TEXTSPLIT/TEXTBEFORE/TEXTAFTER and the negative-instance trick
> - Mention 365-only availability and fallback for older versions
> - Compare with Text to Columns (static) and Power Query (refreshable)

---

## 12. ⭐ Advanced: Date Engineering: EDATE, EOMONTH and Indian Fiscal Year
> ⭐ Advanced · _Added beyond the tracker_

### Definition
```excel
=EDATE(start, months)      -- same day, n months later (negative = earlier)
=EOMONTH(start, months)    -- last day of the month n months away
=YEAR(A1)  =MONTH(A1)  =DAY(A1)  =WEEKDAY(A1,2)  =WEEKNUM(A1)
=DATE(y,m,d)
```
India's financial year runs **April to March**. Fiscal year label: `="FY"&IF(MONTH(A1)>=4,YEAR(A1)+1,YEAR(A1))` gives FY2027 for any date from 1-Apr-2026 to 31-Mar-2027. Fiscal quarter: `=INT(MOD(MONTH(A1)-4,12)/3)+1`. Payment terms: due date = `=A1+45` for net-45, or month-end terms `=EOMONTH(A1,1)+15`. EOMONTH(date,0) gives the month end; `EOMONTH(date,-1)+1` gives the month start. Avoid text dates: use `DATE` or `DATEVALUE`.

### Example
Invoice date 20-Oct-2026, terms "month-end + 30": `=EOMONTH(A1,0)+30` = 31-Oct + 30 = 30-Nov-2026. Fiscal quarter for 20-Oct-2026: MONTH=10, MOD(10-4,12)=6, INT(6/3)=2, +1 = Q3 (Oct to Dec is Q3 of an Apr-Mar year). Correct.

### In the news
See news box. Date logic like fiscal calendars encodes business rules that an AI prompt can easily get wrong; build it with explicit formulas.

### Interview angle
> [!question] How it is asked
> "Group transactions by Indian fiscal quarter" or "Compute the due date for 'EOM + 45' payment terms."

> [!tip] Strong answer includes
> - EDATE/EOMONTH and the fiscal-year offset formula
> - Test edge dates (31 March, 1 April)
> - Mention helper columns or Power Query date table for reuse
> - Connect to working-capital (DPO/DSO) calculations

---
## 🔗 Go deeper: expansion notes
- [[187 Excel Interview Problem Bank & Case Exercises|Excel Interview Problem Bank & Case Exercises]]
- [[188 Financial Modelling in Excel|Financial Modelling in Excel]]
- [[189 VBA, Macros & Office Scripts Basics|VBA, Macros & Office Scripts Basics]]
