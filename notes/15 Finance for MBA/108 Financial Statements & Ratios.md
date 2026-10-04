---
tags: [finance-for-mba, tier1]
area: Finance for MBA
topic: "Financial Statements & Ratios"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 12
---
# Financial Statements & Ratios

[[_Index - Finance for MBA|Finance for MBA]] · [[109 Valuation Basics (NPV, IRR, DCF)]] ➡

> **Area:** Finance for MBA · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. Income Statement (P&L)]]
2. [[#2. Balance Sheet]]
3. [[#3. Cash Flow Statement]]
4. [[#4. EBITDA]]
5. [[#5. Financial Ratios — Profitability]]
6. [[#6. Financial Ratios — Liquidity]]
7. [[#7. Financial Ratios — Leverage]]
8. [[#8. Financial Ratios — Efficiency]]
9. [[#9. DuPont Analysis]]
10. [[#10. Working Capital Cycle]]
11. [[#11. ⭐ Advanced: ROIC and EVA (economic value added)]]
12. [[#12. ⭐ Advanced: Earnings quality and red flags]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Two Indian retailers, two very different financial profiles
> **Eternal (Zomato + Blinkit), Q2 FY26 (reported Oct 2025).** Revenue tripled: **₹13,590 crore (+183% YoY)**, with Blinkit at **₹9,891 crore (+756%)**, yet profit after tax fell 63% to **₹65 crore** and adjusted EBITDA margin was **1.75%** (6.4% a year earlier). About **80% of Blinkit's order value** now comes from inventory the company owns, a move from marketplace to inventory-led. Revenue jumps when you book goods sold rather than a commission, but margin percentage falls: the same business reads very differently on the P&L (my interpretation of the accounting effect). ([INDmoney](https://www.indmoney.com/blog/stocks/eternal-zomato-q2-results))
> 
> **D-Mart (Avenue Supermarts), Q2 FY26 (quarter ended 30 Sep 2025).** Revenue **₹16,676 crore (+15%)**, EBITDA **₹1,230 crore**, EBITDA margin **7.3%** (7.6% a year earlier), PAT **₹685 crore** (PAT margin 4.1% vs 4.6%), **432 stores**. A low-margin, high-turn retailer where small margin changes and inventory efficiency drive returns. ([Torus Digital](https://www.torusdigital.com/toruscope/quarterly-results/avenue-supermarts-q2-fy26-results-dmarts-profit-rises-4-yoy-revenue-up-15/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
> **Running example used below (illustrative "Sample Foods Ltd", ₹ crore):** Revenue 1,000; COGS 600; Opex excluding D&A 150; D&A 50; Interest 40; Tax rate 25%. Balance sheet: Cash 80, Receivables 150, Inventory 220, Other current assets 50, Non-current assets 700; Payables 100, other current liabilities 150 (CL = 250); Long-term debt 350 (total debt 400, including 50 short-term inside CL); Equity 600.

## 1. Income Statement (P&L)
> 🔴 Tier 1 · _Tracker hint:_ Revenue – COGS = Gross Profit; – OPEX = EBIT; – Interest = EBT; – Tax = PAT

### Definition
The income statement reports performance **over a period** on an accrual basis.

| Line | Formula |
|---|---|
| Revenue (net sales) | Price × volume, net of GST and returns |
| Gross profit | Revenue − COGS |
| EBITDA | Gross profit − operating expenses (excl. D&A) |
| EBIT (operating profit) | EBITDA − Depreciation & Amortisation |
| EBT (PBT) | EBIT − Interest (+ other income) |
| PAT | EBT − Tax |

Accrual basis means revenue is recognised when earned (not when cash arrives). In India, Ind AS and Schedule III set the format. Look at margins and growth, and separate **recurring** from **exceptional** items.

### Example
Sample Foods: Gross profit = 1,000 − 600 = **400** (40%); EBITDA = 400 − 150 = **250** (25%); EBIT = 250 − 50 = **200**; EBT = 200 − 40 = **160**; Tax = 25% × 160 = 40; **PAT = 120** (net margin 12%).

### In the news
See news box. Eternal: revenue up 183% but PAT down 63% shows why you read the whole P&L, not the top line. D-Mart: stable margins at lower levels.

### Interview angle
> [!question] How it is asked
> "Walk me through the P&L" or "Revenue is up 20% but profit is down; why?"

> [!tip] Strong answer includes
> - Each line with its formula, top to bottom
> - Margins at each level (gross, EBITDA, net)
> - Reading the cause of a profit decline (gross margin, opex, interest, tax)
> - Operating vs non-operating and one-offs

---

## 2. Balance Sheet
> 🔴 Tier 1 · _Tracker hint:_ Assets = Liabilities + Equity; Current vs Non-current; Working capital = CA – CL

### Definition
A **snapshot** at a date of what the firm owns (assets), owes (liabilities) and what belongs to shareholders (equity).

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

**Current** items are realised or due within 12 months (cash, receivables, inventory; payables, short-term debt). **Non-current**: fixed assets, long-term investments, long-term debt. **Net working capital** = Current assets − Current liabilities (operating NWC excludes cash and debt). Equity = share capital + reserves.

### Example
Sample Foods: CA = 80 + 150 + 220 + 50 = **500**; total assets = 500 + 700 = **1,200**. CL = 250; LT debt 350; equity 600 → 250 + 350 + 600 = **1,200** ✓. NWC = 500 − 250 = **250**.

### In the news
See news box. Eternal's shift to owning inventory moves assets onto the balance sheet (inventory, working capital); an asset-light marketplace had none.

### Interview angle
> [!question] How it is asked
> "What happens to the balance sheet if the company buys machinery on credit?" or "What is working capital?"

> [!tip] Strong answer includes
> - Identity A = L + E and the double effect of any transaction
> - Current vs non-current split and NWC
> - What a heavy-inventory or heavy-debt balance sheet signals
> - Link to cash flow (changes in balance sheet items drive cash)

---

## 3. Cash Flow Statement
> 🔴 Tier 1 · _Tracker hint:_ Operating + Investing + Financing activities; Free Cash Flow = OCF – CapEx

### Definition
Reconciles profit with the **change in cash** over a period, in three sections: **Operating (CFO)**, **Investing (CFI)**, **Financing (CFF)**.

Indirect method for CFO:

$$CFO = PAT + D\&A \pm \Delta\text{Working capital} \pm \text{other non-cash items}$$

Increase in receivables or inventory *reduces* cash; increase in payables *increases* it.

$$FCF = CFO - \text{CapEx}$$

Profit is an opinion, cash is a fact: a profitable firm can still run out of cash (growth eats working capital).

### Example
Sample Foods: PAT 120 + D&A 50 = 170; working capital build-up of 30 → **CFO = 140**. CapEx 90 → **FCF = 50**. If it repays 20 of debt and pays 15 dividend: CFF = −35; net change in cash = 140 − 90 − 35 = **+15**. CFO/PAT = 1.17, which is healthy.

### In the news
See news box. Low-margin retail needs the cash conversion to match: rising inventory in an inventory-led model absorbs cash even when P&L improves.

### Interview angle
> [!question] How it is asked
> "A company is profitable but running out of cash. Why?"

> [!tip] Strong answer includes
> - Three sections and the indirect-method bridge from PAT
> - Working-capital build-up, capex and debt repayment as usual culprits
> - FCF definition and why it matters for valuation ([[109 Valuation Basics (NPV, IRR, DCF)]])
> - Quality check: CFO/PAT over time

---

## 4. EBITDA
> 🔴 Tier 1 · _Tracker hint:_ Earnings Before Interest, Tax, Depreciation & Amortization; proxy for operating cash flow

### Definition
$$EBITDA = \text{Revenue} - \text{COGS} - \text{Opex (excl. D\&A)} = EBIT + D\&A$$

It strips out financing (interest), tax and non-cash charges, so it compares operating performance across firms with different capital structures. **Limits:** ignores capex (a capital-heavy business needs to reinvest), working-capital needs, and can be flattered by capitalising costs. "EBITDA minus capex" is a better cash proxy. **EBITDA margin** = EBITDA/Revenue. Companies often report **adjusted EBITDA**: check what is excluded (ESOP costs, one-offs). Under Ind AS 116, lease costs move below EBITDA, which raises EBITDA for lease-heavy retailers; compare on a like-for-like basis.

### Example
Sample Foods: EBIT 200 + D&A 50 = **250**; margin 25%. If capex is 90, EBITDA − capex = 160. Two firms with EBITDA of 250 can differ greatly: one needs 30 of capex, the other 150.

### In the news
See news box. Eternal's **adjusted EBITDA** margin of 1.75% (down from 6.4%) and D-Mart's 7.3% show that scale does not equal margin; check what is adjusted.

### Interview angle
> [!question] How it is asked
> "Why do investors use EBITDA? What are its drawbacks?"

> [!tip] Strong answer includes
> - Formula and the EBIT + D&A link
> - Use: comparability and EV/EBITDA multiples
> - Limits: capex, working capital, adjustments, Ind AS 116 leases
> - Suggest EBITDA − capex or FCF as complement

---

## 5. Financial Ratios — Profitability
> 🔴 Tier 1 · _Tracker hint:_ Gross margin = GP/Revenue; EBITDA margin; ROE = PAT/Equity; ROCE

### Definition
| Ratio | Formula |
|---|---|
| Gross margin | Gross profit / Revenue |
| EBITDA margin | EBITDA / Revenue |
| Net margin | PAT / Revenue |
| ROE | PAT / Average shareholders' equity |
| ROCE | EBIT / Capital employed, where Capital employed = Total assets − Current liabilities |
| ROA | PAT / Total assets |

Margins measure how much profit each rupee of sales yields; return ratios measure how well capital is used. ROCE is capital-structure neutral; ROE is boosted by leverage. Compare to peers, the cost of capital and the firm's own history.

### Example
Sample Foods: gross margin 400/1,000 = **40%**; EBITDA margin **25%**; net margin **12%**; ROE = 120/600 = **20%**; capital employed = 1,200 − 250 = 950 → ROCE = 200/950 = **21.1%**; ROA = 120/1,200 = **10%**.

### In the news
See news box. D-Mart's PAT margin of 4.1% is thin, but fast inventory turns lift returns; Eternal's 1.75% adjusted EBITDA margin reflects investment in quick commerce.

### Interview angle
> [!question] How it is asked
> "Company A has a 10% margin and Company B 4%; which is better?" (answer: depends on turnover; see DuPont)

> [!tip] Strong answer includes
> - Right formulas and the denominator definitions (average vs closing)
> - Margin vs return distinction
> - ROCE vs cost of capital
> - Use of peers and trend

---

## 6. Financial Ratios — Liquidity
> 🔴 Tier 1 · _Tracker hint:_ Current Ratio = CA/CL (>2 ideal); Quick Ratio = (CA-Inventory)/CL (>1 ideal)

### Definition
Liquidity ratios assess the ability to meet short-term obligations.

$$\text{Current ratio} = \frac{CA}{CL}, \quad \text{Quick ratio} = \frac{CA - \text{Inventory}}{CL}, \quad \text{Cash ratio} = \frac{\text{Cash}}{CL}$$

Rules of thumb (2 and 1) vary by industry: retailers and FMCG with fast cash cycles run below 1.5 because payables fund inventory; a project business needs more. Very high ratios can signal idle cash or bloated inventory. Quick ratio excludes inventory because it can take time to sell and may be sold below book value.

### Example
Sample Foods: current ratio = 500/250 = **2.0**; quick ratio = (500 − 220)/250 = 280/250 = **1.12**; cash ratio = 80/250 = **0.32**. Healthy by the textbook rules; inventory is 44% of CA, so check inventory days (see Working Capital Cycle).

### In the news
See news box. A retailer like D-Mart funds inventory through supplier credit, so a current ratio below 2 is normal for it; the guidance is to compare with the sector, not the rule of thumb.

### Interview angle
> [!question] How it is asked
> "Is a current ratio of 1.2 bad?"

> [!tip] Strong answer includes
> - Formulas for current, quick and cash
> - Industry context (FMCG/retail vs capital goods)
> - What drives the ratio (payables, inventory, short-term debt)
> - Pair with cash conversion cycle

---

## 7. Financial Ratios — Leverage
> 🔴 Tier 1 · _Tracker hint:_ Debt/Equity ratio; Interest Coverage = EBIT/Interest (>3 ideal)

### Definition
$$\frac{D}{E} = \frac{\text{Total debt}}{\text{Shareholders' equity}}, \quad ICR = \frac{EBIT}{\text{Interest}}, \quad \text{Net debt/EBITDA} = \frac{\text{Debt} - \text{Cash}}{EBITDA}$$

Leverage magnifies both returns and risk. Higher D/E raises ROE when ROCE > cost of debt, but increases bankruptcy risk. ICR below ~2–3 is a red flag; Net debt/EBITDA of 3x or more is high for most sectors. Define debt precisely (include lease liabilities?) and note that financial firms use different norms.

### Example
Sample Foods: debt 400, equity 600 → D/E = **0.67**; ICR = 200/40 = **5.0x**; Net debt/EBITDA = (400 − 80)/250 = **1.28x**. Comfortable. If EBIT fell 60% to 80, ICR drops to 2.0x, which would trigger covenant concerns.

### In the news
See news box. The news box gives profit and EBITDA but not debt, so for Eternal or D-Mart you would pull debt and interest from the latest balance sheet before judging leverage; with Eternal's PAT at just ₹65 crore in Q2 FY26, interest cover would be the first ratio to check in any debt-funded expansion.

### Interview angle
> [!question] How it is asked
> "How much debt can this company take on?"

> [!tip] Strong answer includes
> - D/E, ICR and Net debt/EBITDA with thresholds
> - Link to risk and covenants
> - Stability of cash flows decides capacity
> - Trade-off: tax shield vs distress cost

---

## 8. Financial Ratios — Efficiency
> 🔴 Tier 1 · _Tracker hint:_ Asset Turnover = Revenue/Total Assets; Receivables Days = AR/(Revenue/365)

### Definition
Efficiency (activity) ratios measure how well assets are turned into sales.

| Ratio | Formula |
|---|---|
| Asset turnover | Revenue / Total assets |
| Fixed asset turnover | Revenue / Net fixed assets |
| Inventory turnover | COGS / Average inventory |
| Days inventory (DIO) | Inventory / (COGS/365) |
| Receivable days (DSO) | Receivables / (Revenue/365) |
| Payable days (DPO) | Payables / (COGS/365) |

Use average balances when possible. A high turnover offsets a low margin (D-Mart model); a low turnover requires a high margin (luxury, capital goods).

### Example
Sample Foods: asset turnover = 1,000/1,200 = **0.83x**; DSO = 150/(1,000/365) = **54.8 days**; inventory turns = 600/220 = **2.7x** (DIO = 220 × 365/600 = **133.8 days**); DPO = 100 × 365/600 = **60.8 days**.

### In the news
See news box. D-Mart's model is high turns on a thin margin; with its EBITDA margin slipping from 7.6% to 7.3%, asset and inventory turns matter even more.

### Interview angle
> [!question] How it is asked
> "Receivable days have gone from 40 to 60; what could be the reasons and what do you do?"

> [!tip] Strong answer includes
> - Formula, with 365 days convention
> - Interpreting a trend (collection, credit policy, mix)
> - Link to cash and working capital
> - Operational remedies (invoicing discipline, early-payment discounts)

---

## 9. DuPont Analysis
> 🔴 Tier 1 · _Tracker hint:_ ROE = Net Margin × Asset Turnover × Financial Leverage; decompose performance

### Definition
$$ROE = \frac{PAT}{Revenue} \times \frac{Revenue}{Assets} \times \frac{Assets}{Equity}$$

Three levers: **profitability** (net margin), **efficiency** (asset turnover) and **leverage** (equity multiplier). Extended five-step version splits margin into tax burden (PAT/EBT), interest burden (EBT/EBIT) and operating margin (EBIT/Revenue). Used to explain *why* ROE differs between firms or years, and whether high ROE is quality (margin/turns) or financial engineering (leverage).

### Example
Sample Foods: net margin 12% × turnover 0.8333 × leverage (1,200/600 = 2.0) = **20%** = ROE ✓.
Compare **D-Mart-style** (margin 4%, turnover 2.5, leverage 1.2 → ROE 12%) with a **branded FMCG-style** (margin 12%, turnover 1.0, leverage 1.5 → ROE 18%): same business logic, different mix of levers (illustrative numbers).

### In the news
See news box. Eternal's margin fell sharply while turnover (revenue/assets) rose with inventory-led revenue: a pure DuPont story.

### Interview angle
> [!question] How it is asked
> "ROE has dropped from 20% to 15%. Which lever moved?"

> [!tip] Strong answer includes
> - Three-factor decomposition, correct formula
> - Diagnosis using each factor
> - Distinguish leverage-driven ROE as riskier
> - Recommendation tied to the weak lever

---

## 10. Working Capital Cycle
> 🔴 Tier 1 · _Tracker hint:_ Days Inventory + Days Receivable – Days Payable = Cash Conversion Cycle

### Definition
$$CCC = DIO + DSO - DPO$$

The **Cash Conversion Cycle** is the number of days cash is tied up between paying suppliers and collecting from customers. Shorter (or negative) is better. Levers: reduce DIO (forecasting, SKU rationalisation, lean), reduce DSO (credit terms, collections, factoring), extend DPO (supplier terms, supply-chain finance, mindful of supplier health). Working capital investment ≈ Revenue/365 × CCC (using consistent bases). In India, MSME payment rules (45-day limit under the MSMED Act) constrain DPO extension.

### Example
Sample Foods: DIO 133.8 + DSO 54.8 − DPO 60.8 = **127.8 days**. Cutting DIO by 20 days releases about 600/365 × 20 = **₹32.9 crore** of cash. A retailer such as D-Mart tends to have a very short or even negative CCC because it collects at the till and pays suppliers on credit (qualitative; check reported figures).

### In the news
See news box. Eternal's inventory-led model lengthens the cycle (it now owns stock); D-Mart's efficiency depends on turning inventory faster than suppliers are paid.

### Interview angle
> [!question] How it is asked
> "How would you free up cash in this business?" or "Which component of the cash cycle would you attack first?"

> [!tip] Strong answer includes
> - Formula, correct components and units
> - Quantify the cash released per day of improvement
> - Sequence the levers (inventory first for manufacturers)
> - Caution about supplier stress and service levels (links with [[110 Cost Accounting for Operations]])

---

## 11. ⭐ Advanced: ROIC and EVA (economic value added)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
$$NOPAT = EBIT \times (1 - t), \quad ROIC = \frac{NOPAT}{\text{Invested capital}}, \quad EVA = NOPAT - WACC \times \text{Invested capital}$$

Invested capital = Equity + Debt − Excess cash. A firm creates value only if **ROIC > WACC**. ROIC is cleaner than ROE (ignores leverage) and ROCE (uses after-tax operating profit). EVA expresses the spread in rupees. Operations managers use it to justify capital projects and working-capital cuts.

### Example
Sample Foods: NOPAT = 200 × 0.75 = **150**. Invested capital = 600 + 400 − 80 = **920**; ROIC = 150/920 = **16.3%**. If WACC = 11%, spread = 5.3%; EVA = 150 − 0.11 × 920 = 150 − 101.2 = **₹48.8 crore** positive.

### In the news
See news box. Fast growth with thin margins (Eternal) invites the question: does ROIC exceed WACC once the network matures?

### Interview angle
> [!question] How it is asked
> "How do you know if growth is creating value?"

> [!tip] Strong answer includes
> - ROIC vs WACC test, with formulas
> - Distinction from ROE
> - Margin × invested-capital turnover as the drivers
> - Growth destroys value if ROIC < WACC

---

## 12. ⭐ Advanced: Earnings quality and red flags
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Consultants and analysts test whether reported profit is **backed by cash** and sustainable. Key checks:
- **CFO/PAT** persistently below 0.8–1.0.
- **Receivables growing faster than revenue** (aggressive recognition).
- **Inventory growing faster than sales** (obsolescence).
- **Accruals ratio** = (PAT − CFO)/Average assets: high means low quality.
- **Capitalised costs**, rising "other income", frequent exceptional items, auditor changes, related-party transactions.
- **Adjusted** metrics that grow apart from reported ones.

Use common-size and trend (3–5 years) analysis.

### Example
Sample Foods: CFO/PAT = 140/120 = **1.17** (good). Accruals ratio = (120 − 140)/1,200 = **−1.7%** (negative is good). Now suppose receivables rose 40% while revenue rose 10%: DSO would climb from 54.8 to about 71 days (150 × 1.4 = 210; 210/(1,000 × 1.1/365) = 69.7 days), a flag even if profits looked fine.

### In the news
See news box. When a company's *adjusted* EBITDA diverges from reported profit (as with high-growth consumer internet firms), cross-check cash flow.

### Interview angle
> [!question] How it is asked
> "Profit is growing 25% a year; what would you check before believing it?"

> [!tip] Strong answer includes
> - CFO/PAT and accruals
> - Receivables and inventory vs sales
> - Adjusted vs reported earnings, one-offs
> - Cash flow tied to P&L; peer comparison

---
## 🔗 Go deeper: expansion notes
- [[225 Budgeting, Variance Analysis & Balanced Scorecard|Budgeting, Variance Analysis & Balanced Scorecard]]
- [[226 Corporate Finance Essentials - Capital Structure & Cost of Capital|Corporate Finance Essentials - Capital Structure & Cost of Capital]]
