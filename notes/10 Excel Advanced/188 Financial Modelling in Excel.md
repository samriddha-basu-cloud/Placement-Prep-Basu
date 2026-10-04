---
tags: [excel-advanced, tier2]
area: Excel Advanced
topic: "Financial Modelling in Excel"
tier: Tier 2
roles: Consulting / Finance / Operations
status: complete
subtopics: 14
---
# Financial Modelling in Excel

⬅ [[187 Excel Interview Problem Bank & Case Exercises]] · [[_Index - Excel Advanced|Excel Advanced]] · [[189 VBA, Macros & Office Scripts Basics]] ➡

> **Area:** Excel Advanced · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / Finance / Operations

## Sub-topics in this note
1. [[#1. Modelling Best Practice: FAST, Colours & One-Formula-Per-Row]]
2. [[#2. Model Architecture: Sheets, Timeline & Flags]]
3. [[#3. Three-Statement Model Skeleton]]
4. [[#4. Forecast Drivers & Working-Capital Schedules]]
5. [[#5. DCF in Excel: Worked Example]]
6. [[#6. WACC & Terminal Value Choices (India)]]
7. [[#7. Scenario Switch with CHOOSE and INDEX]]
8. [[#8. Sensitivity Tables]]
9. [[#9. Circularity & Iterative Calculation]]
10. [[#10. Checks & Error Flags]]
11. [[#11. Unit-Economics Model]]
12. [[#12. Break-Even & Operating Leverage Model]]
13. [[#13. Model Review Checklist]]
14. [[#14. ⭐ Advanced: Monte Carlo Simulation & Model Risk]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): standards, spreadsheet-risk lessons and live Indian inputs for a DCF
> **FAST Standard remains the reference for spreadsheet design.** The FAST Standard Organisation (a UK not-for-profit) publishes the free standard under a Creative Commons Attribution 4.0 licence; its latest version is dated July 2019 (FAST-Standard-02c). Its four principles are Flexible, Appropriate, Structured and Transparent. Checked 4 October 2026. ([FAST Standard](https://fast-standard.org/the-fast-standard/))
>
> **A formula slip inside a risk model: JPMorgan's "London Whale" (2012).** A secondary summary of the episode states that a spreadsheet formula divided by the sum instead of the average when computing relative changes in hazard rates and correlations, inside a Value-at-Risk model for credit-derivative positions, and that the bank lost at least $6.2 billion on the trades; the error involved copy-and-paste across spreadsheets. This is a cautionary example for the review checklist below, not a 2024-26 event, and the figure comes from that secondary source. ([Qashqade](https://www.qashqade.com/insights/the-worst-financial-services-excel-errors-of-all-time/))
>
> **Live inputs for a rupee DCF (checked 4 October 2026).** Trading Economics reports the India 10-year government bond yield at 7.21% on 1 October 2026, a two-year high, with the RBI policy rate at 5.25% (August 2026), US 10-year yields at 5.30% and markets pricing sizeable rate rises over the next 12 months. A rising risk-free rate pushes up the cost of equity and WACC and lowers present values, which is why the sensitivity tables below matter. Treat quoted market levels as time-sensitive. ([Trading Economics](https://tradingeconomics.com/india/government-bond-yield))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Modelling Best Practice: FAST, Colours & One-Formula-Per-Row
> 🟠 Tier 2 · _Key points:_ Flexible, Appropriate, Structured, Transparent; colour code; no hard-codes; consistent formulas

### Definition
A financial model is a **calculation engine with a clear audit trail**, not a big spreadsheet. The FAST Standard summarises good practice in four words: **Flexible** (can change scenarios and structure without rebuilding), **Appropriate** (a good representation of reality, not reality itself; no spurious precision), **Structured** (consistent layout so another person can take over), **Transparent** (simple formulas that modellers and non-modellers can follow). Core rules:

- **Separate inputs, calculations and outputs.** Inputs once, in one place; calculations never typed over; outputs read-only.
- **One formula per row** (consistent across the timeline): copy the first formula across all periods; any exception is a flag, not an edit.
- **No hard-coded numbers inside formulas** (`*1.18`, `/365`): put them in labelled cells (tax rate, days in year).
- **Colour code**: blue font for inputs (hard-coded numbers), black for formulas, green for links to other sheets, red for checks or flags. Optionally shade input cells light yellow.
- **Units and signs**: label units (₹ crore, % of revenue), keep one sign convention (outflows negative in cash flow), keep one currency and scale.
- **Time**: one timeline row across all sheets, same columns for the same period, flags for actual vs forecast.
- **Short formulas**: split long nested `IF`s into steps; avoid `OFFSET`/`INDIRECT` (volatile, hard to audit); avoid merged cells; use named ranges sparingly and consistently.
- **Documentation**: a cover sheet (purpose, version, author, date, change log), assumptions list with sources, a checks summary.

### Example
Bad: `=B12*(1+0.12)-B13*0.2517` repeated with different constants. Good: `=C12*(1+C$5)` where `C$5` is the growth input and `=-C14*Tax_rate` for tax, with both inputs on the Inputs sheet in blue. When growth changes from 12% to 10% in one cell, every dependent figure updates, and a reviewer can click one cell to see where the number comes from. Related layout habits for operations workbooks are in [[078 Excel for Operations & SCM]] and shortcuts in [[070 Foundations & Navigation]].

### In the news
See news box. The FAST Standard (July 2019 version, free under CC BY 4.0) is the document to cite when asked "what standard do you follow?"; the 2012 London Whale case is the story of what happens when review discipline fails.

### Interview angle
> [!question] How it is asked
> "How do you structure a financial model so that someone else can use and audit it?"

> [!tip] Strong answer includes
> - Input / calculation / output separation and one timeline
> - Colour conventions and no hard-codes in formulas
> - Consistent formulas across rows, checks sheet, documentation and version control
> - Name a standard (FAST) and say what "appropriate" detail means

---
## 2. Model Architecture: Sheets, Timeline & Flags
> 🟠 Tier 2 · _Key points:_ sheet map, time flags, named inputs, sign conventions, dashboard

### Definition
A typical structure: `Cover` (purpose, version, change log) > `Inputs` (all assumptions, scenario switch) > `Calc` sheets (Revenue, Costs, Capex, Working capital, Debt, Tax) > `Statements` (IS, BS, CF) > `Valuation` (DCF, ratios) > `Outputs` (dashboard, charts) > `Checks`. Principles:

- **Timeline row** at the top of every calc sheet linked to a single master (`=Inputs!E$4`); period flags such as `Forecast flag = 1 if period > last actual date`, so formulas can be written once and switch behaviour with the flag.
- **Names** for key scalars only (`Tax_rate`, `WACC`, `Scenario`); ranges and structured references for tables.
- **Direction of flow**: left to right (time) and top to bottom (inputs to results); avoid back-references that jump around sheets.
- **Granularity**: monthly for operations and cash, annual for valuation; roll up with `SUMIFS` on a period key rather than retyping.
- **Protection** of calc and output sheets (unlocked inputs only); data validation on inputs (lists, ranges).

```excel
' Period flag (row 6), master timeline in Inputs!E4:AI4
=IF(E$4>Inputs!$C$3, 1, 0)                         ' 1 = forecast period
' Annual from monthly
=SUMIFS(Calc!$E12:$AI12, Calc!$E$5:$AI$5, G$5)     ' G5 holds the fiscal-year key
' Fiscal year key for an Indian April-March year (ending year)
=YEAR(E4)+(MONTH(E4)>=4)
```

### Example
A 5-year plan model has 40 columns (months) on the calc sheets and 5 on the valuation sheet. The fiscal-year key lets `SUMIFS` aggregate the 12 months of each April-March year; changing the model start date in `Inputs` moves every sheet. Checks on the `Checks` sheet confirm that monthly totals equal annual totals.

### In the news
See news box. Interest-rate moves (10-year G-sec at 7.21% on 1 October 2026) mean the discount rate on the Inputs sheet is a live input; a clean architecture lets you update one cell and re-run the valuation.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would lay out a model for a new plant investment."

> [!tip] Strong answer includes
> - Sheet map with flow of information and a master timeline
> - Flags and consistent formulas across columns
> - Scenario and sensitivity capability planned from day one
> - Checks sheet and a dashboard for decision makers

---
## 3. Three-Statement Model Skeleton
> 🟠 Tier 2 · _Key points:_ IS to CF to BS links, balance check, cash as the result, working-capital schedule

### Definition
The **integrated model** links the income statement (IS), balance sheet (BS) and cash flow statement (CF) so that the balance sheet balances by construction. Background on statements and ratios: [[108 Financial Statements & Ratios]]. Link logic:

1. **IS**: revenue, COGS, opex, EBITDA, depreciation, EBIT, interest, PBT, tax, PAT.
2. **Schedules**: working capital (receivable, inventory, payable days), fixed assets (opening + capex - depreciation), debt (opening - repayment), equity (opening + PAT - dividends).
3. **CF (indirect)**: CFO = PAT + depreciation - increase in NWC; CFI = - capex; CFF = - debt repaid - dividends; net change in cash.
4. **BS**: cash = opening cash + net change from CF; other lines from schedules; the **balance check** = total assets - (liabilities + equity) must be zero. Cash must come from the cash flow statement, never from a plug.

Worked mini-model for "Nashik Components Ltd" (illustrative, ₹ crore). Opening balance sheet (FY26A): cash 30, receivables 82, inventory 80, net PP&E 200 (assets 392); payables 36, debt 120, equity 236. Drivers: revenue growth 12%, 10%, 8%, 8%, 6%; gross margin 35%; opex 17% of revenue (EBITDA margin 18%); depreciation 10% of opening PP&E; capex 6% of revenue; receivable days 60 (on revenue), inventory days 90 and payable days 40 (on COGS); interest 9% on opening debt; debt repayment ₹20 crore a year; tax 25.17%; dividend 20% of PAT.

| ₹ crore | FY27 | FY28 | FY29 | FY30 | FY31 |
|---|---|---|---|---|---|
| Revenue | 560.0 | 616.0 | 665.3 | 718.5 | 761.6 |
| EBITDA | 100.8 | 110.9 | 119.8 | 129.3 | 137.1 |
| Depreciation | 20.0 | 21.4 | 22.9 | 24.6 | 26.5 |
| EBIT | 80.8 | 89.5 | 96.8 | 104.7 | 110.6 |
| Interest | 10.8 | 9.0 | 7.2 | 5.4 | 3.6 |
| PAT | 52.4 | 60.3 | 67.1 | 74.3 | 80.1 |
| Increase in NWC | 15.9 | 14.2 | 12.5 | 13.5 | 10.9 |
| CFO | 56.5 | 67.4 | 77.5 | 85.5 | 95.6 |
| Capex | 33.6 | 37.0 | 39.9 | 43.1 | 45.7 |
| Closing cash | 22.4 | 20.8 | 25.0 | 32.4 | 46.4 |
| Closing debt | 100.0 | 80.0 | 60.0 | 40.0 | 20.0 |
| Closing equity | 277.9 | 326.1 | 379.8 | 439.2 | 503.3 |
| Total assets | 417.8 | 450.0 | 487.2 | 530.4 | 577.5 |
| Balance check | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

Key formulas (column E = FY27, D = FY26):

```excel
Revenue         =D10*(1+E$5)                         ' growth input in row 5
COGS            =E10*(1-GM)                          ' GM = gross margin input
Depreciation    =Dep_rate*D40                        ' opening net PP&E (D40)
Interest        =Int_rate*D55                        ' opening debt, avoids circularity
Tax             =MAX(0,E28)*Tax_rate                 ' PBT in E28
Receivables     =AR_days/365*E10
Inventory       =Inv_days/365*E11
Payables        =AP_days/365*E11
Closing cash    =D60+E70+E71+E72                     ' prior cash + CFO + CFI + CFF
Balance check   =ROUND(E45-(E52+E55+E58),3)          ' assets - (payables + debt + equity)
```

### Example
FY27 by hand: revenue 500 x 1.12 = 560; COGS 560 x 0.65 = 364; opex 95.2; EBITDA 100.8; depreciation 10% x 200 = 20; EBIT 80.8; interest 9% x 120 = 10.8; PBT 70.0; tax 25.17% = 17.62; PAT 52.38. Receivables 60/365 x 560 = 92.05; inventory 90/365 x 364 = 89.75; payables 40/365 x 364 = 39.89; NWC 141.92 against 126.0 opening, so ΔNWC = 15.92. CFO = 52.38 + 20 - 15.92 = 56.46; capex 33.6; dividends 10.48; debt repaid 20, so closing cash = 30 + 56.46 - 33.6 - 20 - 10.48 = 22.39. Assets = 22.39 + 92.05 + 89.75 + 213.6 = 417.80; payables 39.89 + debt 100 + equity (236 + 52.38 - 10.48 = 277.90) = 417.80, so the check is 0. Figures reproduced in Python from the same drivers.

### In the news
See news box. Interest cost in the model uses the opening debt balance; in a higher-rate environment (10-year yield 7.21%), changing the interest-rate input should flow through PAT, cash and the balance check with no manual patching.

### Interview angle
> [!question] How it is asked
> "Walk me through how the three statements link. If you increase depreciation by 10, what happens?"

> [!tip] Strong answer includes
> - IS to CF (PAT plus non-cash and working-capital changes) to BS (cash and schedules); equity roll-forward
> - Depreciation +10: EBIT -10, tax shield +10 x t, PAT lower by 10(1-t), CFO higher by 10t net (non-cash add-back), PP&E down by 10, cash up by 10t, equity down by 10(1-t): the BS still balances
> - Cash never a plug; balance check built in
> - Working-capital days drive receivables, inventory, payables (link [[110 Cost Accounting for Operations]])

---
## 4. Forecast Drivers & Working-Capital Schedules
> 🟠 Tier 2 · _Key points:_ driver-based forecasting, days metrics, capex and depreciation schedules, NWC change

### Definition
Forecast from **drivers**, not from trends of the line items. Revenue = volume x price (or customers x ARPU, or capacity x utilisation); costs split into variable (% of revenue or per unit) and fixed (₹ per period, inflated); working capital by **days**: receivable days = receivables / revenue x 365, inventory days = inventory / COGS x 365, payable days = payables / COGS x 365; **cash conversion cycle** = DIO + DSO - DPO. Capex from capacity needs (or % of revenue); depreciation by asset class, straight line (`=SLN(cost, salvage, life)`) or % of opening net block. Cross-check forecasts against history and peers (growth, margins, days).

Working-capital arithmetic from the mini-model: opening NWC = 82 + 80 - 36 = ₹126 crore (25.2% of FY26 revenue). With 60/90/40 days the NWC is 141.9 at FY27, so growth consumes cash: ΔNWC 15.9 in FY27. Cash conversion cycle = 90 + 60 - 40 = 110 days (with DSO on revenue and DIO/DPO on COGS, a convention to state).

```excel
DSO / DIO / DPO (history)   =Receivables/Revenue*365 ;  =Inventory/COGS*365 ;  =Payables/COGS*365
Cash conversion cycle       =DIO+DSO-DPO
Net block roll-forward      =Opening + Capex - Depreciation
Straight-line depreciation  =SLN(1000, 100, 10)       ' = 90 per year (cost 1000, salvage 100, life 10)
```

### Example
If the plant negotiates payable days from 40 to 50 on COGS of ₹364 crore (FY27), payables rise by 10/365 x 364 = ₹9.97 crore, releasing about ₹10 crore of cash once: a working-capital lever with the same effect as ₹10 crore of extra funding. Supply-chain finance programmes work this way (see [[136 Supply Chain Finance & Working Capital]]).

### In the news
See news box. With policy rates and bond yields rising (10-year G-sec at 7.21%), the carrying cost of inventory and receivables increases, so days assumptions matter more.

### Interview angle
> [!question] How it is asked
> "How would you forecast working capital and what happens to cash if sales grow 20%?"

> [!tip] Strong answer includes
> - Days-based drivers on the correct base (revenue or COGS)
> - Growth consumes cash even when profitable (NWC and capex build)
> - Cash conversion cycle and levers (collections, inventory, supplier terms)
> - Sanity checks against history and peers

---
## 5. DCF in Excel: Worked Example
> 🟠 Tier 2 · _Key points:_ FCFF, discounting, terminal value, EV to equity bridge, NPV vs SUMPRODUCT

### Definition
A **discounted cash flow** values a business as the present value of its **free cash flow to the firm (FCFF)** plus a terminal value, at the weighted average cost of capital (WACC). Theory is in [[109 Valuation Basics (NPV, IRR, DCF)]].

$$FCFF = EBIT(1-t) + D\&A - Capex - \Delta NWC$$

$$EV=\sum_{t=1}^{N}\frac{FCFF_t}{(1+WACC)^t}+\frac{TV_N}{(1+WACC)^N},\qquad TV_N=\frac{FCFF_N(1+g)}{WACC-g}$$

Equity value = EV - net debt (debt - cash); value per share = equity value / shares. Using the mini-model: WACC = 12.07% (derived in the next sub-topic), g = 5%, net debt at FY26 = 120 - 30 = ₹90 crore, 10 crore shares (illustrative).

| ₹ crore | FY27 | FY28 | FY29 | FY30 | FY31 |
|---|---|---|---|---|---|
| EBIT x (1 - 25.17%) | 60.5 | 67.0 | 72.4 | 78.3 | 82.8 |
| + Depreciation | 20.0 | 21.4 | 22.9 | 24.6 | 26.5 |
| - Capex | 33.6 | 37.0 | 39.9 | 43.1 | 45.7 |
| - Increase in NWC | 15.9 | 14.2 | 12.5 | 13.5 | 10.9 |
| **FCFF** | 30.9 | 37.2 | 43.0 | 46.4 | 52.6 |
| Discount factor at 12.07% | 0.8923 | 0.7962 | 0.7104 | 0.6339 | 0.5657 |
| PV of FCFF | 27.6 | 29.6 | 30.5 | 29.4 | 29.8 |

Sum of PVs = ₹146.9 crore. Terminal value = 52.62 x 1.05 / (0.1207 - 0.05) = ₹781.6 crore; PV of TV = 781.6 x 0.5657 = ₹442.1 crore. **EV = 146.9 + 442.1 = ₹589.0 crore**; equity = 589.0 - 90 = ₹499.0 crore; per share ₹49.90. The terminal value is 75.1% of EV.

```excel
' FCFF in row 3 (B3:F3), period numbers 1..5 in row 2, WACC in I1, g in I2
PV of FCFF   =NPV($I$1, B3:F3)                          ' = 146.92 (end-year flows)
PV (explicit)=SUMPRODUCT(B3:F3/(1+$I$1)^B2:F2)          ' same result, shows the mechanics
TV           =F3*(1+$I$2)/($I$1-$I$2)                   ' = 781.56
PV of TV     =B7/(1+$I$1)^F2                            ' = 442.09
EV           =B5+B8                                     ' = 589.02
Equity       =B9-NetDebt                                ' = 499.02
Mid-year PV  =SUMPRODUCT(B3:F3/(1+$I$1)^(B2:F2-0.5))    ' = 155.54 (cash arrives through the year)
```
Pitfall: `NPV` assumes the first flow is at the end of period 1 and the range excludes the time-0 flow; a time-0 investment is added outside: `=-Invest + NPV(r, flows)`. For dated flows use `XNPV(rate, values, dates)` (its first value is at the first date).

```python
fcff = [30.94, 37.20, 42.97, 46.38, 52.62]            # rounded copy of the FCFF row
wacc, g, net_debt, shares = 0.1207, 0.05, 90, 10
pv = sum(f / (1 + wacc) ** t for t, f in enumerate(fcff, start=1))
tv = fcff[-1] * (1 + g) / (wacc - g)
ev = pv + tv / (1 + wacc) ** len(fcff)
print(round(pv, 1), round(tv, 1), round(ev, 1), round((ev - net_debt) / shares, 2))
assert round(ev) == 589 and round((ev - net_debt) / shares, 1) == 49.9
```
Output: `146.9 781.6 589.0 49.9` (the Excel formulas above were recalculated in a spreadsheet engine and match to the rupee-crore decimal shown).

### Example
Implied multiples sanity check: EV 589.0 over FY27 EBITDA 100.8 = 5.8x; the terminal value 781.6 over FY31 EBITDA 137.1 = 5.7x. If listed peers trade at 9 to 10 times, either the assumptions are conservative (12% WACC, 5% growth, 18% margin) or the company is cheap; saying so is part of the answer. A DCF is only as good as these inputs: moving WACC by 1 point moves EV by 10% to 15% (next sub-topics).

### In the news
See news box. With the India 10-year yield at 7.21% (1 October 2026), the risk-free input is higher than a year earlier and compresses value; note the date of your market inputs on the Inputs sheet.

### Interview angle
> [!question] How it is asked
> "Walk me through a DCF. What are the most sensitive assumptions, and how do you sanity-check the answer?"

> [!tip] Strong answer includes
> - FCFF build, discount rate, terminal value, EV to equity bridge, per-share value
> - TV share of EV (75% here) and implied exit multiple as cross-checks
> - Timing conventions (end-year vs mid-year) and the `NPV` first-period trap
> - Sensitivity to WACC and g; consistency (growth <= long-run nominal GDP growth, capex vs depreciation in the terminal year)

---
## 6. WACC & Terminal Value Choices (India)
> 🟠 Tier 2 · _Key points:_ CAPM, cost of debt after tax, target weights, Gordon growth vs exit multiple

### Definition
$$WACC=\frac{E}{E+D}K_e+\frac{D}{E+D}K_d(1-t),\qquad K_e=r_f+\beta\,(ERP)$$

Inputs: **risk-free rate** (10-year G-sec yield; 7.21% on 1 October 2026), **beta** (levered, from peers re-levered to target structure), **equity risk premium** (an assumption, commonly in the range of 5-7% for India in practice; state your source), **pre-tax cost of debt** (company borrowing rate), **tax rate** (India's base corporate rate for companies that have not opted for the concessional regime is 25.17% including surcharge and cess; verify the regime applicable to your company), **target weights** at market values.

Worked: $K_e$ = 7.21% + 1.1 x 6.5% = 14.36%; after-tax $K_d$ = 9% x (1 - 0.2517) = 6.73%; weights 70/30: WACC = 0.7 x 14.36% + 0.3 x 6.73% = 10.05% + 2.02% = 12.07%. The ERP and beta are illustrative assumptions, not market data.

```excel
Ke    =Rf + Beta*ERP                    ' = 0.0721 + 1.1*0.065 = 0.1436
Kd_at =Kd*(1-Tax)                       ' = 0.09*(1-0.2517) = 0.0673
WACC  =E_w*Ke + D_w*Kd_at               ' = 0.1207
```
**Terminal value methods.** (1) **Gordon growth**: $TV=FCFF_N(1+g)/(WACC-g)$; keep $g$ at or below long-run nominal growth (5% is a high-end assumption for India; many analysts use 3-5%). (2) **Exit multiple**: $TV=\text{EBITDA}_N\times$ multiple, cross-checked against the implied $g$. Under the mid-year convention the treatment of TV discounting differs between textbooks (N or N - 0.5 for the perpetuity method): state your convention. In the terminal year normalise capex relative to depreciation and the NWC build to the terminal growth.

### Example
Exit-multiple cross-check: at 6x FY31 EBITDA of 137.1, TV = 822.5 (against 781.6 by Gordon growth), PV at 12.07% for 5 years = 465.3, so EV = 146.9 + 465.3 = ₹612.2 crore, 4% above the Gordon result. The two methods agree when the multiple matches the implied one (5.7x here). Also: using the book or target debt weight of 30% when the company's actual market-value debt ratio is lower understates WACC; use target structure and say so.

### In the news
See news box. Rising government yields (7.21%) and US yields at 5.30% put upward pressure on $r_f$; an interviewer in 2026 may well ask how a 50 bp move in the risk-free rate changes WACC and value (about 0.35 percentage points of WACC at 70% equity weight and beta 1.1: 0.7 x 0.5%).

### Interview angle
> [!question] How it is asked
> "How do you estimate WACC for an Indian manufacturing company? Which terminal growth rate would you use and why?"

> [!tip] Strong answer includes
> - CAPM for equity, after-tax debt cost, target weights; beta unlevered from peers and re-levered
> - Source and date for the risk-free rate and ERP; consistent currency (rupee flows with rupee rates)
> - Terminal growth below nominal GDP growth; cross-check with exit multiple and implied growth
> - TV share of value and sensitivity to WACC and g

---
## 7. Scenario Switch with CHOOSE and INDEX
> 🟠 Tier 2 · _Key points:_ one switch cell, live case, scenario table, avoid duplicating the model

### Definition
Build **one model** driven by a **scenario selector** (a cell with data validation: 1 Base, 2 Upside, 3 Downside) and a scenario table on the Inputs sheet. The live case is picked with `CHOOSE` or `INDEX`; downstream formulas read only the live column. Avoid copying the model for each scenario; avoid `OFFSET`. Store results of each scenario (a pasted-values table or a data table) to compare side by side.

```excel
' Inputs sheet: Scenario in C3 (1, 2 or 3); cases in D10:F10 (Base, Upside, Downside)
Live growth shift   =CHOOSE(Scenario, D10, E10, F10)
Live (INDEX form)   =INDEX($D10:$F10, 1, Scenario)
Scenario name       =INDEX({"Base","Upside","Downside"}, Scenario)
Safe guard          =IF(OR(Scenario<1, Scenario>3), NA(), Scenario)
```
Scenario inputs for the mini-model (growth shift in each year; gross-margin shift): Base 0 / 0; Upside +2 points / +1 point; Downside -3 points / -1.5 points. Results (WACC 12.07%, g 5%):

| Scenario | FY31 revenue (₹ crore) | FY31 EBITDA margin | Minimum cash (₹ crore) | EV (₹ crore) | Equity value (₹ crore) |
|---|---|---|---|---|---|
| Base | 761.6 | 18.0% | 20.8 | 589.0 | 499.0 |
| Upside | 834.3 | 19.0% | 24.5 | 665.9 | 575.9 |
| Downside | 662.2 | 16.5% | 15.5 | 490.9 | 400.9 |

The downside lowers EV by 16.7% and equity value by 19.7% (leverage amplifies); minimum cash stays positive so no extra funding is needed in these cases.

### Example
The recommended presentation to a decision maker is the table above plus one sentence: "Value ranges from ₹491 crore to ₹666 crore; even the downside keeps cash positive, so the debt repayment schedule is safe." The model itself has one live case and the table is produced by a data table or by running each case and pasting values with a macro ([[189 VBA, Macros & Office Scripts Basics]]).

### In the news
See news box. Scenario thinking is routine when rate paths are uncertain: the same switch can carry a "higher-for-longer" case with a higher WACC input.

### Interview angle
> [!question] How it is asked
> "How do you build scenarios into a model without copying it three times?"

> [!tip] Strong answer includes
> - Single model, selector cell with validation, `CHOOSE`/`INDEX` to pick the live case
> - Scenario table on the Inputs sheet; outputs table comparing cases
> - Discipline: scenarios change inputs only, never formulas
> - Distinguish scenarios (coherent stories) from sensitivities (one variable at a time)

---
## 8. Sensitivity Tables
> 🟠 Tier 2 · _Key points:_ two-way data table, formula-based grid, WACC vs g, what to show

### Definition
A **sensitivity table** recalculates one output (EV) over ranges of two inputs. Excel's **Data Table** (Data > What-If Analysis > Data Table) uses a row input cell and a column input cell on the same sheet as the table; results appear as `{=TABLE(row_input, col_input)}`. Data tables recalculate the whole model for each cell (slow on big models; set calculation to "Automatic except data tables" when needed). A **formula-based grid** avoids data tables: write the closed-form EV formula in each cell referencing the row and column headers.

```excel
' WACC down the rows (A20:A22), g across the columns (B19:D19), FCFF in B3:F3, periods in B2:F2
=SUMPRODUCT($B$3:$F$3/(1+$A20)^$B$2:$F$2) + $F$3*(1+B$19)/($A20-B$19)/(1+$A20)^$F$2
```
Enterprise value (₹ crore) from the mini-model's FCFF:

| WACC \ g | 4% | 5% | 6% |
|---|---|---|---|
| 11% | 615.3 | 697.8 | 813.4 |
| 12% | 535.4 | 595.1 | 674.7 |
| 13% | 473.4 | 518.2 | 575.8 |

The 11% / 4% cell (615.3) was reproduced by the Excel formula above in a spreadsheet engine; all nine values come from the same calculation in Python.

### Example
Reading the grid: one point of WACC (12% to 13% at g = 5%) takes EV from 595.1 to 518.2, a 12.9% fall; one point of g (5% to 6% at 12%) adds 13.4%. The table's shape is the message: value is far more sensitive to the terminal assumptions than to a year of forecast error, so spend interview time defending WACC and g. Conditional formatting (colour scale) and highlighting the base case make the table decision-ready; show a second table with equity value per share if the audience thinks in share price.

### In the news
See news box. In 2026 interest-rate conditions, an interviewer may ask for the table to be re-centred on a higher WACC; building it from headers lets you shift the centre in seconds.

### Interview angle
> [!question] How it is asked
> "Show how sensitive enterprise value is to WACC and terminal growth. How would you build it in Excel?"

> [!tip] Strong answer includes
> - Data table mechanics (row/column input cells, same sheet) and the formula-grid alternative
> - Centre on base case; sensible step sizes; show EV and per-share
> - Interpretation: TV dominates; which assumption to defend first
> - Calculation setting and speed trade-off

---
## 9. Circularity & Iterative Calculation
> 🟠 Tier 2 · _Key points:_ why circular, average-balance interest, iteration settings, circuit breaker, algebraic alternative

### Definition
A **circular reference** occurs when a formula depends on its own result, directly or through a chain. In models it arises when **interest is calculated on average debt** while debt repayment depends on cash flow after interest (cash sweep), or when fees are a percentage of a total that includes the fee. Excel warns by default; you can allow it with File > Options > Formulas > Enable iterative calculation (maximum iterations, maximum change). Better practice: **avoid** (use opening balances), **solve algebraically**, or keep it with a **circuit breaker** switch and checks, because circularity can blow up with `#VALUE!` and then persist.

Example: opening debt 120, rate 9%, cash available for debt service before interest 50, no tax. Sweep = 50 - interest; closing debt = 120 - sweep; interest = 9% x average(opening, closing).

Iteration: interest 0 gives closing debt 70, then interest 8.55; next 78.55 and 8.935; then 8.952, 8.9528, 8.9529: converged in about 6 steps.

Algebra: let $i$ be interest; closing debt $D_1 = 120 - 50 + i = 70 + i$; $i = 0.09\cdot(120+D_1)/2 = 0.045(190+i)$, so $i = 8.55/0.955 = 8.9529$ and $D_1 = 78.9529$.

```excel
' Circular (needs iterative calculation ON)
Interest   =Rate*AVERAGE(Opening, Closing)
Closing    =Opening - (CashAvail - Interest)
' Circuit breaker: switch cell Circ (1 = on, 0 = off)
Interest   =IF(Circ=1, Rate*AVERAGE(Opening, Closing), Rate*Opening)
' Closed-form alternative (no circularity)
Interest   =Rate*(2*Opening - CashAvail)/2/(1 - Rate/2)    ' = 0.09*(240-50)/2/(0.955) = 8.9529
```
Reset procedure if errors lock in: set `Circ` to 0, let the model recalculate, then set back to 1. Recommended settings: maximum iterations 100, maximum change 0.001; always add a check that the iterated interest equals `Rate*AVERAGE(...)` to within tolerance.

### Example
Circular and closed-form answers agree: interest ₹8.9529 crore, closing debt ₹78.9529 crore. In the main mini-model interest is on opening debt (₹10.8 crore in FY27 vs ₹10.35 on average balance), which keeps the model non-circular at the cost of overstating interest by a small amount when debt is falling. Interview point: say you would use the opening-balance approach unless the client specifically needs average-balance interest, and then use a breaker.

### In the news
See news box. As rates rise, the gap between opening-balance and average-balance interest grows with the size of the repayment, so reviewers pay more attention to this simplification.

### Interview angle
> [!question] How it is asked
> "What is a circular reference in a financial model and how do you handle it?"

> [!tip] Strong answer includes
> - Cause (interest on average balances with cash sweep) and risk (instability, hidden errors)
> - Options: avoid, solve algebraically, or iterate with a circuit breaker and checks
> - Excel settings (iterations, max change) and the reset procedure
> - Documenting the circularity on the cover sheet

---
## 10. Checks & Error Flags
> 🟠 Tier 2 · _Key points:_ balance, cash, sums, sign and range checks, master check, conditional formats

### Definition
Checks are formulas that return 0 (or FALSE) when the model is healthy and are summarised in one **master check** shown on every output page. Typical set:

| Check | Formula idea |
|---|---|
| Balance sheet balances | `=ROUND(Assets-Liabilities-Equity,3)` equals 0 every period |
| Cash ties | Closing cash on BS equals closing cash on CF |
| Sources equal uses | In a funding table, total sources minus total uses is 0 |
| Roll-forwards | Opening + movement = closing for PP&E, debt, equity, NWC |
| Sums tie | Annual totals equal the sum of months; segment totals equal group total |
| Sign and range | Days between 0 and 365; margins between -50% and 100%; no negative debt or inventory |
| Error scan | `=SUMPRODUCT(--ISERROR(range))` equals 0 |
| Circularity | Iterated value equals recomputed value within tolerance |
| Inputs complete | No blank required inputs: `=COUNTBLANK(Inputs!C5:C40)` equals 0 |

```excel
Check (per period)  =ABS(E45-(E52+E55+E58))>0.001            ' TRUE = error
Master check        =IF(SUM(Checks!E5:E30)=0, "OK", "CHECK MODEL")
Error scan          =SUMPRODUCT(--ISERROR(Calc!E5:AI120))
Conditional format  red fill when master check <> "OK"; show it in the title bar cell of every sheet
```
Behaviour of a good check: it **fails** when you break something (test it by deliberately mis-linking a cell). `IFERROR` should not hide errors in the calculation chain: use it only at the presentation layer, and only with a visible count of errors trapped.

### Example
In the mini-model, change closing cash to a hard-coded 20 in FY27: the balance check shows 2.4 (22.4 - 20) and the master check turns red; without the check the model would still print a plausible but wrong balance sheet. Another quick test: set depreciation to 0 and confirm the balance still holds. Data-quality parallels (control totals, reconciliation) are covered in [[175 Data Quality, Master Data & Data Governance]].

### In the news
See news box. The London Whale episode is cited in model-risk training because a single mis-specified formula went unchecked; automated checks and independent review are the control.

### Interview angle
> [!question] How it is asked
> "How do you know your model is right?"

> [!tip] Strong answer includes
> - Built-in checks (balance, cash, roll-forwards, sums) with a master flag
> - Testing the checks by breaking the model; extreme-value tests (zero growth, zero debt)
> - Independent review or parallel calculation (for example in Python)
> - Documented assumptions and a change log

---
## 11. Unit-Economics Model
> 🟠 Tier 2 · _Key points:_ contribution per order, CAC, LTV, payback, LTV/CAC, sensitivity

### Definition
Unit economics models profit for **one unit** of the business (an order, a customer, a vehicle, a delivery) before scale effects. Layout: revenue per unit (AOV) - variable costs per unit = **contribution margin per unit** (CM); then customer-level metrics: **CAC** (customer acquisition cost), **orders per month**, **lifetime** = 1 / monthly churn, **LTV** = CM per order x orders per month x lifetime, **LTV/CAC**, **payback** = CAC / monthly contribution. Contribution is before fixed overhead; fully-loaded profit needs scale and allocation. Related: [[110 Cost Accounting for Operations]], [[031 Product Metrics & Analytics]].

Illustrative quick-commerce order (numbers are assumptions, not company data): AOV ₹550; gross margin 20% = ₹110; advertising income ₹10; delivery cost ₹45; picking and packing ₹25; dark-store cost per order ₹20; payment and packaging ₹12.

CM = 110 + 10 - 45 - 25 - 20 - 12 = **₹18 per order (3.3% of AOV)**. Customer: 3 orders a month, monthly churn 8% (lifetime 12.5 months), CAC ₹250.

LTV = 18 x 3 x 12.5 = **₹675**; LTV/CAC = 2.7; payback = 250 / (18 x 3) = **4.6 months**.

```excel
CM per order     =AOV*Gross_margin + Ad_income - Delivery - Pick_pack - Dark_store - Payment_pack   ' = 18
Lifetime         =1/Churn                                                                          ' = 12.5 months
LTV              =CM*Orders_per_month*Lifetime                                                     ' = 675
LTV/CAC          =LTV/CAC                                                                          ' = 2.7
Payback (months) =CAC/(CM*Orders_per_month)                                                        ' = 4.63
Break-even orders per store per day  =Store_fixed_cost_per_day/CM
```

### Example
Sensitivity: delivery cost down by ₹5 to ₹40 lifts CM from 18 to 23 (+28%), LTV to 862.5 and LTV/CAC to 3.45; a 10-point higher churn (18%) cuts lifetime to 5.6 months and LTV to 300 (LTV/CAC 1.2). Tiny margins make the model highly sensitive to delivery cost and basket size, which is the point to make in an interview about quick commerce ([[129 E-commerce & Quick-Commerce Fulfilment]]). Rule of thumb often quoted: LTV/CAC of 3 or more and payback under 12 months for subscription-type businesses; treat as heuristics, not laws.

### In the news
See news box. Unit economics changes with interest rates through the cost of funding working capital and inventory; keep the funding cost as an explicit input if the business is inventory-heavy.

### Interview angle
> [!question] How it is asked
> "A quick-commerce company earns ₹18 per order contribution. Is the business viable? What would you check?"

> [!tip] Strong answer includes
> - Contribution per order, variable vs fixed split, CAC, retention and frequency
> - LTV and payback arithmetic, with sensitivity to delivery cost, basket size, churn
> - Store-level break-even (fixed cost / contribution) and ramp-up of orders per store
> - Cohort evidence rather than averages, and caution about heuristics

---
## 12. Break-Even & Operating Leverage Model
> 🟠 Tier 2 · _Key points:_ contribution margin, break-even volume, margin of safety, DOL, target-profit pricing

### Definition
Cost-volume-profit: contribution per unit = price - variable cost. **Break-even volume** = fixed cost / contribution per unit. **Margin of safety** = (actual - break-even) / actual. **Degree of operating leverage (DOL)** = contribution / EBIT = % change in EBIT per % change in volume. Target profit volume = (fixed cost + target profit) / contribution per unit.

Example (₹ crore, volumes in lakh units): price ₹500, variable cost ₹300, so contribution ₹200 per unit; fixed costs ₹40 crore.
- Break-even = 4,000 lakh rupees / 200 = **20 lakh units** (₹40 crore / ₹200 per unit = 20 lakh).
- At 30 lakh units: contribution = 30 x 200 = ₹60 crore; EBIT = 60 - 40 = **₹20 crore**; margin of safety = (30 - 20)/30 = **33.3%**; DOL = 60/20 = **3.0**.
- Volume +10% (33 lakh units): contribution 66, EBIT 26, **+30%**, which equals DOL x 10%.
- Volume -10% (27 lakh): EBIT 14, **-30%**: leverage cuts both ways.

```excel
Break-even units      =Fixed/(Price-Variable)                 ' 4000 lakh Rs / 200 = 20 lakh units
Margin of safety      =(Volume-BE)/Volume                     ' 33.3%
DOL                   =Contribution/EBIT                      ' 60/20 = 3.0
Target-profit volume  =(Fixed+Target_profit)/(Price-Variable) ' (40+30)*100/200 = 35 lakh units for Rs 30 crore
Data table            volume across, price down -> EBIT grid
```
Unit conversion: ₹40 crore = 4,000 lakh rupees, and 4,000 / 200 = 20 lakh units; the lakh-versus-crore conversion is the usual error source.

### Example
Two plants: A has fixed ₹40 crore and variable ₹300; B automates, raising fixed to ₹60 crore and cutting variable to ₹250. Contribution is 200 vs 250; break-even 20 vs 24 lakh units. At 30 lakh units, EBIT is A 20 and B 15; at 40 lakh units A 40 and B 40; at 50 lakh units A 60 and B 65. B has higher operating leverage: worse at low volume, better at high volume (the volumes where they are equal: 40 + 200(V-30)/100... computed as 40 crore = (200 - 250)... equal at V = 40 lakh units). See [[110 Cost Accounting for Operations]] and the capacity decision in [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]].

### In the news
See news box. Higher rates raise the fixed charge of capital-heavy plants (interest is a fixed cost), increasing operating and financial leverage together.

### Interview angle
> [!question] How it is asked
> "At what volume does this plant break even, and how risky is it if demand falls 10%?"

> [!tip] Strong answer includes
> - Contribution per unit, break-even volume and margin of safety with correct units (lakh and crore)
> - DOL as the amplifier of volume changes, and the link to financial leverage
> - Sensitivity table of EBIT by price and volume
> - Decision relevance: automation, outsourcing, make vs buy

---
## 13. Model Review Checklist
> 🟠 Tier 2 · _Key points:_ structure, inputs, formulas, logic, outputs, documentation

### Definition
Use this list to review your own or someone else's model. Report findings with severity (critical, major, minor) and fix location.

1. **Purpose and scope**: question the model answers; users; version; date; owner.
2. **Structure**: inputs, calculations, outputs separated; one timeline; flow left to right; no hidden sheets or rows unexplained.
3. **Inputs**: all in blue on one sheet; sources and dates; units; data validation; no hard-coded numbers in formulas.
4. **Formulas**: consistent across each row (Go To Special > Row differences); no `#REF!`, no links to external files without documentation; no merged cells; volatile functions minimal; absolute/relative references correct; no formulas overwritten by values.
5. **Logic**: three statements integrated; balance check; cash from the CF; signs consistent; tax on positive PBT only (or loss carry-forward modelled); working-capital bases correct; terminal year normalised; WACC consistent with currency and capital structure.
6. **Checks**: balance, cash, roll-forwards, sums, error scan, master flag; tested by breaking the model.
7. **Stress tests**: zero and extreme values; negative growth; interest rate shock; switch to downside.
8. **Outputs**: ties to the model; units and labels; charts with axis titles; sensitivities and scenarios present; key messages stated.
9. **Documentation and control**: cover sheet, change log, file naming and versioning, protection, backups; reviewer sign-off.
10. **Independent cross-check**: re-compute headline results in a second tool (Python, calculator) or compare with a simple benchmark (EV/EBITDA, margins, growth versus history and peers).

### Example
Applying the checklist to the mini-model finds: (a) interest on opening balance overstates cost slightly (documented simplification); (b) tax is applied to PBT without a loss carry-forward, acceptable here because PBT is positive in all years; (c) the terminal year capex (45.7) exceeds depreciation (26.5) which is consistent with 5% growth but should be justified; (d) the TV is 75% of EV, so the valuation is mostly a terminal assumption. Each is reported with severity and a recommended fix, rather than being silently corrected.

### In the news
See news box. The FAST Standard and professional model-audit practice formalise this review; the London Whale case is the argument for independent review of any model that drives large decisions.

### Interview angle
> [!question] How it is asked
> "You are handed a model from a colleague and must sign it off in an hour. What do you do?"

> [!tip] Strong answer includes
> - Start with structure and checks (does it balance, are inputs separated), then formulas, then logic and outputs
> - Use tools: Trace Precedents, Go To Special, Evaluate Formula, error scan
> - Stress tests and an independent cross-check; report findings by severity
> - Do not rebuild silently: log changes and agree them with the owner

---
## 14. ⭐ Advanced: Monte Carlo Simulation & Model Risk
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A scenario table shows three stories; a **Monte Carlo simulation** shows a distribution. Replace point inputs with random draws, recalculate the model many times and read percentiles of the output. In Excel: draw inputs with `=NORM.INV(RAND(), mean, sd)` (or `RANDARRAY` in 365), link them to the live assumptions, and use a **one-variable data table** with a blank column input cell to recalculate 1,000 or more trials; then summarise with `PERCENTILE.INC`, `AVERAGE` and `COUNTIF`. Press F9 to resample; freeze a run by pasting values. Add-ins (@RISK, Crystal Ball) or Python are used for larger work. **Model risk** is the risk of wrong decisions from model errors or misuse; controls are independent validation, version control, input governance and documented limitations.

```excel
Growth shift   =NORM.INV(RAND(), 0, 0.02)
Margin shift   =NORM.INV(RAND(), 0, 0.01)
WACC draw      =MAX(0.08, NORM.INV(RAND(), 0.1207, 0.008))
Trial output   =EV                                  ' linked to the live model
P5, P50, P95   =PERCENTILE.INC(Results, 0.05) ; 0.5 ; 0.95
P(EV below 500) =COUNTIF(Results, "<500")/COUNT(Results)
```
Results on the mini-model (5,000 trials, seed 11, in Python with the same engine; Excel with `RAND()` will differ slightly each run): mean EV ₹599 crore, P5 ₹451 crore, median ₹590 crore, P95 ₹776 crore, standard deviation about ₹101 crore, and a 15.3% probability that EV falls below ₹500 crore.

### Example
Reporting: "The base case is ₹589 crore; with plausible uncertainty in growth (sd 2 points), gross margin (sd 1 point) and WACC (sd 0.8 points) the 90% range is ₹451 to ₹776 crore and there is roughly a one-in-seven chance of value below ₹500 crore." The assumptions behind the distribution (independent normal draws) are themselves judgments and should be stated; correlated inputs (growth and margin often move together) would widen or narrow the range. Statistical background: [[092 Sampling & Experimental Design]] and [[150 Decision Analysis & Simulation]].

### In the news
See news box. The 2012 London Whale loss is the textbook model-risk case: an unreviewed formula in a risk model understated risk; simulation does not fix a wrong formula, so validation of the model comes first.

### Interview angle
> [!question] How it is asked
> "How would you show the uncertainty in this valuation instead of a single number?"

> [!tip] Strong answer includes
> - Distributions for the key drivers, repeated recalculation (data table or tool), percentiles and probability of loss
> - Caveats: assumed distributions, ignored correlations, false precision
> - Compare with scenario analysis and sensitivity tables (when each is enough)
> - Model-risk controls: validation, version control, documentation
