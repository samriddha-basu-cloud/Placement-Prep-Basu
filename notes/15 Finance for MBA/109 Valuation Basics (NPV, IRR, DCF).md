---
tags: [finance-for-mba, tier1]
area: Finance for MBA
topic: "Valuation Basics (NPV, IRR, DCF)"
tier: Tier 1
roles: Consulting / Operations
status: complete
subtopics: 12
---
# Valuation Basics (NPV, IRR, DCF)

⬅ [[108 Financial Statements & Ratios]] · [[_Index - Finance for MBA|Finance for MBA]] · [[110 Cost Accounting for Operations]] ➡

> **Area:** Finance for MBA · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. Time Value of Money]]
2. [[#2. NPV (Net Present Value)]]
3. [[#3. IRR (Internal Rate of Return)]]
4. [[#4. Payback Period]]
5. [[#5. DCF Valuation]]
6. [[#6. Comparable Transactions (EV/EBITDA)]]
7. [[#7. WACC]]
8. [[#8. Break-Even Point]]
9. [[#9. Sensitivity Analysis]]
10. [[#10. Scenario Analysis]]
11. [[#11. ⭐ Advanced: NPV vs IRR conflicts and MIRR]]
12. [[#12. ⭐ Advanced: Terminal value pitfalls and sanity checks]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's big IPOs put valuation maths in the headlines
> **Hyundai Motor India IPO (opened 15–17 Oct 2024).** An issue of **₹27,870 crore** at a price band of **₹1,865–1,960**; **225 anchor investors** put in **₹8,315.3 crore** before the issue opened. Forbes India described the offer as "richly valued", i.e. leaving little on the table for new investors: the practical question is whether the price is justified by expected cash flows and peer multiples. ([Forbes India](https://www.forbesindia.com/article/take-one-big-story-of-the-day/hyundai-motor-ipo-do-valuations-justify-the-price/94379/1))
> 
> **Swiggy IPO (anchor bidding 5 Nov, issue 6–8 Nov 2024, listing expected 13 Nov).** Total issue size **₹11,300 crore**: a fresh issue raised to **₹4,499 crore** (from ₹3,750 crore) and an offer for sale of 175.1 million shares, in a price band of **₹371–390**. A loss-making growth company is valued on future cash flows and revenue multiples rather than current earnings. ([Business Standard](https://www.business-standard.com/companies/news/swiggy-raises-primary-issuance-to-rs-4-499-cr-cuts-ofs-to-175-1-mn-shares-124102900834_1.html))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Time Value of Money
> 🔴 Tier 1 · _Tracker hint:_ ₹100 today > ₹100 tomorrow; FV = PV×(1+r)^n; PV = FV/(1+r)^n

### Definition
A rupee today is worth more than a rupee later because it can be invested (opportunity cost), inflation erodes purchasing power, and the future is uncertain (risk).

$$FV = PV(1+r)^n, \qquad PV = \frac{FV}{(1+r)^n}$$

- **Annuity** (equal payment $C$ for $n$ periods): $PV = C \cdot \frac{1-(1+r)^{-n}}{r}$.
- **Perpetuity:** $PV = C/r$; **growing perpetuity:** $PV = C_1/(r-g)$, valid for $r>g$.
- Match the rate and period (monthly cash flows need a monthly rate); EMIs are annuities. **Effective annual rate** = $(1+r/m)^m - 1$.

Discounting is the foundation of NPV, IRR and DCF.

### Example
₹1,00,000 invested at 8% for 5 years: $1.08^5 = 1.4693$ → FV = **₹1,46,933**. Reverse: ₹1,00,000 due in 5 years at 8% is worth 1,00,000/1.4693 = **₹68,058** today. Annuity: ₹20,000/year for 5 years at 10%: factor = (1 − 1.1⁻⁵)/0.1 = 3.7908 → PV = **₹75,816**.

### In the news
See news box. An IPO price is today's value of expected future cash flows; a ₹390 offer price for Swiggy is a bet on far-off profits being worth that much now.

### Interview angle
> [!question] How it is asked
> "Would you take ₹1 lakh today or ₹1.2 lakh in a year?" or "What is the PV of a perpetuity growing at 5%?"

> [!tip] Strong answer includes
> - Three reasons for time value
> - The right formula, consistent rate and period
> - The comparison: implied return 20% vs your alternative
> - Quick mental rule: rule of 72 (doubling time ≈ 72/r%)

---

## 2. NPV (Net Present Value)
> 🔴 Tier 1 · _Tracker hint:_ Σ[CF_t/(1+r)^t] – Initial Investment; NPV>0 = value creating; r=hurdle rate

### Definition
$$NPV = \sum_{t=1}^{n}\frac{CF_t}{(1+r)^t} - I_0$$

Where $r$ is the project's risk-adjusted discount rate (hurdle rate, often WACC). **Decision rule:** accept if NPV > 0; for mutually exclusive projects choose the highest NPV. NPV measures value added in rupees and is additive across projects. Use **incremental after-tax cash flows** (not accounting profit), include working-capital changes and terminal or salvage value, and ignore sunk costs and financing flows (they are in $r$).

### Example
Invest ₹1,000 lakh; cash flows ₹400, ₹500, ₹600 lakh in Years 1–3; $r$ = 10%.
PV = 400/1.1 + 500/1.21 + 600/1.331 = 363.64 + 413.22 + 450.79 = **1,227.65**. NPV = 1,227.65 − 1,000 = **₹227.65 lakh** > 0, accept.

### In the news
See news box. Investors in Hyundai Motor India or Swiggy are in effect computing NPV: pay ₹X now for a stream of future cash flows; "richly valued" means the NPV at the offer price is thin.

### Interview angle
> [!question] How it is asked
> "A plant costs ₹50 crore and yields ₹12 crore for 6 years. Should we build it?" (cost of capital 12%)

> [!tip] Strong answer includes
> - Formula and rule with the correct discount rate
> - Incremental cash flows, taxes, working capital
> - Sensitivity to $r$ and volumes (see sub-topic on sensitivity)
> - NPV as the primary criterion over IRR for ranking

---

## 3. IRR (Internal Rate of Return)
> 🔴 Tier 1 · _Tracker hint:_ Discount rate where NPV=0; compare to WACC; higher IRR = better project

### Definition
IRR is the rate $r^*$ that solves

$$0 = \sum_{t=1}^{n}\frac{CF_t}{(1+r^*)^t} - I_0$$

It is the project's compound annual return. Accept if IRR > hurdle rate (WACC). Found by trial and error, interpolation or Excel (`=IRR(range)`). **Limitations:** multiple IRRs when cash flows change sign more than once; assumes reinvestment at IRR itself (unrealistic for high IRR); can mislead on mutually exclusive projects of different scale or timing (NPV wins). The **Modified IRR (MIRR)** fixes the reinvestment problem.

### Example
Same cash flows as the NPV example. NPV at 21% = +10.77; NPV at 22% = −5.77 (e.g. at 22%: 327.87 + 335.93 + 330.43 = 994.23). Linear interpolation: 21 + 10.77/(10.77 + 5.77) = **≈ 21.7%**. Since 21.7% > 10%, accept. Excel: cash flows in A1:A4 (−1000, 400, 500, 600) → `=IRR(A1:A4)`.

### In the news
See news box. Private-equity or anchor investors in IPOs state targets as IRRs; a ₹8,315 crore anchor book must expect returns above its cost of capital after the listing price.

### Interview angle
> [!question] How it is asked
> "NPV says Project A, IRR says Project B. Which one do you choose?"

> [!tip] Strong answer includes
> - Definition and the comparison to hurdle rate
> - NPV is better for mutually exclusive projects (scale, timing, reinvestment)
> - Multiple IRRs for unconventional cash flows
> - MIRR as a fix

---

## 4. Payback Period
> 🔴 Tier 1 · _Tracker hint:_ Years to recover initial investment; simple (undiscounted) vs discounted payback

### Definition
**Simple payback** = time for cumulative (undiscounted) cash inflows to equal the initial outlay. For even cash flows: $I_0 / CF$. **Discounted payback** uses discounted cash flows (accounts for time value). Payback is simple, liquidity-focused and useful when risk or obsolescence is high (tech, fashion), but it **ignores cash flows after the cut-off** and (if simple) the time value. Use it as a screening tool next to NPV, never alone.

### Example
Same project (−1,000; 400, 500, 600). Cumulative: 400, 900, 1,500 → payback = 2 + (1,000 − 900)/600 = **2.17 years**. Discounted: PVs 363.64, 413.22, 450.79; cumulative 363.64, 776.86, 1,227.65 → 2 + (1,000 − 776.86)/450.79 = 2 + 0.495 = **2.49 years**.

### In the news
See news box. Loss-making growth firms such as Swiggy are judged on long-run economics, not payback; a payback test would fail them, which shows its short-sightedness.

### Interview angle
> [!question] How it is asked
> "A project pays back in 3 years; is it good?"

> [!tip] Strong answer includes
> - Both versions with formulas
> - Strengths: simple, liquidity, risk-aware
> - Weaknesses: ignores later cash flows, time value
> - Recommend NPV together with payback

---

## 5. DCF Valuation
> 🔴 Tier 1 · _Tracker hint:_ Forecast FCFs → discount at WACC → Terminal value → Enterprise Value → Equity Value

### Definition
Value of the firm = present value of future free cash flows.

$$EV = \sum_{t=1}^{N}\frac{FCFF_t}{(1+WACC)^t} + \frac{TV_N}{(1+WACC)^N}$$

$$FCFF = EBIT(1-t) + D\&A - \text{CapEx} - \Delta NWC$$
$$TV_N = \frac{FCFF_N (1+g)}{WACC - g} \quad (\text{Gordon growth}) \quad \text{or}\quad EBITDA_N \times \text{exit multiple}$$

**Equity value = EV − Net debt (debt − cash)** (and minorities/preference); per share = equity ÷ shares. Typical steps: explicit forecast of 5–10 years, WACC, terminal value, bridge to equity. TV is often 60–80% of EV, so test the growth ($g$ below long-run nominal GDP) and WACC assumptions.

### Example
FCFF: Year 1: 100, Year 2: 120, Year 3: 140; WACC 10%; $g$ = 4%.
PVs: 90.91 + 99.17 + 105.19 = 295.27. TV = 140 × 1.04 / (0.10 − 0.04) = 145.6/0.06 = **2,426.67**; PV(TV) = 2,426.67/1.331 = **1,823.2**. EV = 295.27 + 1,823.2 ≈ **2,118**. Net debt 300 → equity ≈ **1,818**. TV is 86% of EV: any small change to $g$ or WACC moves value a lot.

### In the news
See news box. IPO pricing of Hyundai India or Swiggy cross-checks DCF with peer multiples; DCF is highly sensitive for growth firms with long-dated cash flows.

### Interview angle
> [!question] How it is asked
> "How would you value a company?" or "Walk me through a DCF."

> [!tip] Strong answer includes
> - FCFF definition and the steps to equity value
> - Terminal value method and its dominant share
> - Net debt bridge and share count
> - Cross-check with multiples; sensitivity on WACC and $g$

---

## 6. Comparable Transactions (EV/EBITDA)
> 🔴 Tier 1 · _Tracker hint:_ EV = Market Cap + Debt – Cash; EV/EBITDA multiple vs industry peers

### Definition
**Relative valuation:** value a company by applying peers' multiples. Enterprise value is the value of operations to all capital providers:

$$EV = \text{Market cap} + \text{Debt} + \text{Minorities/Preference} - \text{Cash}$$

$$\text{Implied EV} = \text{EBITDA}_{target} \times \text{Peer EV/EBITDA}$$

Then subtract net debt to get equity value. **Trading comps** use listed peers' current multiples; **transaction comps** use multiples paid in past acquisitions (include a control premium). EV/EBITDA is capital-structure neutral. Other multiples: P/E, EV/Sales (for loss-makers), EV/EBIT. Choose peers by sector, size, growth, margins, and use the median.

### Example
Company: market cap ₹5,000 crore, debt ₹1,200 crore, cash ₹200 crore → EV = **₹6,000 crore**. EBITDA ₹500 crore → **12.0x**. Peers trade at 10x median → implied EV = ₹5,000 crore → equity = 5,000 − 1,000 (net debt) = **₹4,000 crore**, i.e. it trades at a 20% EV premium (market cap 25% above the peer-implied ₹4,000 crore), which needs justification (higher growth or margins).

### In the news
See news box. IPO pricing relies on peer multiples; for Hyundai, comparing its multiples with listed auto peers is the standard way to test whether the price is rich (I did not retrieve specific multiples, so none are quoted here).

### Interview angle
> [!question] How it is asked
> "A target has EBITDA of ₹100 crore; peers trade at 8x. What is it worth?" (then: and the equity value?)

> [!tip] Strong answer includes
> - EV bridge and why EV rather than market cap
> - Peer selection and adjustments (growth, margin, size)
> - Trading vs transaction comps (control premium)
> - Limits: multiples embed market sentiment; combine with DCF

---

## 7. WACC
> 🔴 Tier 1 · _Tracker hint:_ Weighted Average Cost of Capital = Ke×E/V + Kd×D/V×(1-tax); used as discount rate

### Definition
$$WACC = K_e\frac{E}{V} + K_d(1-t)\frac{D}{V}$$

- **Cost of equity** from CAPM: $K_e = r_f + \beta (E[R_m] - r_f)$. In India, $r_f$ is the 10-year G-Sec yield.
- **Cost of debt** $K_d$ = current borrowing rate (pre-tax); interest is tax-deductible, hence $(1-t)$.
- Weights use **market values** (or target capital structure), not book.

WACC is the minimum return required by capital providers, used to discount FCFF and as the project hurdle (adjust for project risk). Raising debt cheapens WACC only up to the point where distress costs rise.

### Example
E = ₹600 crore, D = ₹400 crore (V = 1,000). $r_f$ = 7%, $\beta$ = 1.0, market premium 7% → $K_e$ = 7 + 1.0 × 7 = **14%**. $K_d$ = 9%, tax 25% → after-tax 6.75%. WACC = 0.6 × 14% + 0.4 × 6.75% = 8.4% + 2.7% = **11.1%**.

### In the news
See news box. The discount rate used by IPO investors for a loss-making growth firm such as Swiggy is higher than for a mature auto maker such as Hyundai India; the same cash flow is worth less at a higher WACC.

### Interview angle
> [!question] How it is asked
> "How would you calculate the discount rate for this project?" or "Does more debt always lower WACC?"

> [!tip] Strong answer includes
> - Formula with market-value weights
> - CAPM for equity, after-tax debt cost
> - Project-specific risk adjustment
> - Trade-off of the tax shield vs distress costs

---

## 8. Break-Even Point
> 🔴 Tier 1 · _Tracker hint:_ Fixed Costs / (Selling Price – Variable Cost per unit); where profit = 0

### Definition
$$BEP_{units} = \frac{\text{Fixed costs}}{P - V}, \qquad BEP_{₹} = \frac{\text{Fixed costs}}{CM\ ratio}$$

where $P - V$ is the contribution margin per unit and $CM\ ratio = (P-V)/P$. Target profit: units $= (FC + \text{Target profit})/(P-V)$. **Margin of safety** = (Actual − BEP)/Actual. **Operating leverage** = Contribution / EBIT: the higher the fixed cost share, the more profit swings with volume. Assumptions: linear costs and revenue, constant mix, within relevant range. Cash break-even excludes non-cash costs (depreciation).

### Example
A cloud kitchen: fixed costs ₹6,00,000 per month; price ₹50; variable cost ₹30 → CM ₹20. BEP = 6,00,000/20 = **30,000 units** (revenue ₹15,00,000). At 36,000 units: profit = 6,000 × 20 = ₹1,20,000; margin of safety = 6,000/36,000 = 16.7%.

### In the news
See news box. For high-fixed-cost platforms like Swiggy (dark stores, tech), the break-even is the volume needed per store/city before contribution covers fixed cost.

### Interview angle
> [!question] How it is asked
> "How many units must we sell to break even?" or "What happens to break-even if the price drops 10%?"

> [!tip] Strong answer includes
> - Correct formula, fixed/variable classification
> - Target-profit variant, margin of safety
> - Sensitivity (price, VC, FC) and operating leverage
> - Limitations: linearity, multi-product mix (see [[110 Cost Accounting for Operations]])

---

## 9. Sensitivity Analysis
> 🔴 Tier 1 · _Tracker hint:_ Change one variable (price, volume, cost) and see impact on NPV/profit

### Definition
Vary one input at a time (others fixed) and record the change in the output (NPV, IRR, profit). Present as a **table**, **tornado chart** (variables ranked by impact) or **break-even / switching value** (the input value at which NPV = 0). Purpose: identify **key value drivers** and the margin for error. Limitation: one-at-a-time ignores correlations (price and volume usually move together) and does not assign probabilities (that is scenario analysis).

### Example
The project (NPV = ₹227.65 lakh at 10%). All cash flows −10%: PV = 1,104.88 → NPV = **₹104.88 lakh**. Switching value: NPV = 0 when cash flows fall by 227.65/1,227.65 = **18.5%**. Discount rate: at 15% PV = 347.83 + 378.07 + 394.51 = 1,120.41 → NPV = **₹120.4 lakh**. Conclusion: the project is more sensitive to cash flows than to the discount rate in this range.

### In the news
See news box. IPO valuations are very sensitive to growth and WACC; a small change in the terminal growth rate can swing the DCF value of growth firms by a lot.

### Interview angle
> [!question] How it is asked
> "Which assumption in your model worries you most?"

> [!tip] Strong answer includes
> - One-variable-at-a-time and the tornado idea
> - Switching value for decision relevance
> - Name the key driver and how to de-risk it
> - Limits and the move to scenarios

---

## 10. Scenario Analysis
> 🔴 Tier 1 · _Tracker hint:_ Best/Base/Worst case; range of outcomes; probability-weighted expected value

### Definition
Change **several variables together** to define coherent states of the world (best, base, worst), compute the output in each and weight by probability:

$$E[NPV] = \sum_i p_i \cdot NPV_i, \qquad \sigma = \sqrt{\sum_i p_i (NPV_i - E[NPV])^2}$$

Unlike sensitivity analysis, it captures correlated moves (e.g. low demand with price cuts). **Monte Carlo simulation** extends this using distributions for inputs. Good scenarios have narratives (e.g. "a competitor enters") rather than arbitrary ±10%.

### Example
Bear: NPV −150 (p = 25%); Base: +228 (50%); Bull: +500 (25%). Expected NPV = 0.25 × (−150) + 0.5 × 228 + 0.25 × 500 = −37.5 + 114 + 125 = **₹201.5 lakh**. Probability of loss = 25%. The decision needs the range as well as the mean.

### In the news
See news box. Analysts pricing IPOs use scenarios for market share and margin outcomes; the "richly valued" label for the Hyundai IPO means the bear case already gets the investor little room.

### Interview angle
> [!question] How it is asked
> "What are the risks to this investment and how would you quantify them?"

> [!tip] Strong answer includes
> - Three coherent scenarios with narratives
> - Probability-weighted NPV, and range / downside
> - Difference from sensitivity analysis
> - Decision: mitigation, staging, or real options

---

## 11. ⭐ Advanced: NPV vs IRR conflicts and MIRR
> ⭐ Advanced · _Added beyond the tracker_

### Definition
NPV and IRR can disagree for **mutually exclusive** projects because of scale or timing (the crossover rate). When they conflict, NPV prevails since it assumes reinvestment at the cost of capital, not at the IRR. **MIRR** reinvests inflows at the cost of capital and discounts outflows at the financing rate:

$$MIRR = \left(\frac{FV_{\text{inflows at }r}}{PV_{\text{outflows at }k}}\right)^{1/n} - 1$$

Also the **profitability index** $PI = PV(\text{inflows})/I_0$ helps rank projects under capital rationing.

### Example
Project (−1,000; 400, 500, 600), reinvestment and finance at 10%: FV of inflows = 400 × 1.21 + 500 × 1.1 + 600 = 484 + 550 + 600 = 1,634. MIRR = $(1{,}634/1{,}000)^{1/3} - 1$ = **17.8%** (vs IRR 21.7%). PI = 1,227.65/1,000 = **1.23**.

### In the news
See news box. A growth investor quoting a 30% IRR may rely on exit at a rich IPO price; MIRR with realistic reinvestment would be lower.

### Interview angle
> [!question] How it is asked
> "Why is NPV preferred over IRR?"

> [!tip] Strong answer includes
> - Scale and timing conflicts, reinvestment assumption
> - Multiple IRRs
> - MIRR and PI as corrections or rationing tools
> - Final rule: choose the highest NPV

---

## 12. ⭐ Advanced: Terminal value pitfalls and sanity checks
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Terminal value (TV) dominates DCF output, so test it: (1) **growth $g$** should not exceed long-run nominal GDP growth (and normally sits well below it); (2) in the terminal year, **capex ≈ depreciation × (1 + growth)** and reinvestment must support $g$: $g = \text{Reinvestment rate} \times ROIC$; (3) cross-check the **implied exit multiple** $TV/EBITDA_N$ against peers; (4) use **mid-year discounting** if cash flows arrive evenly; (5) never discount TV at the wrong year.

### Example
From the DCF example: TV = ₹2,426.67 crore with FCFF₃ = 140. Suppose EBITDA₃ is 220 → implied TV/EBITDA = 2,426.67/220 = **11.0x**. If peers trade at 8x, the Gordon assumptions ($g$ = 4%, WACC 10%) are generous. Re-running with $g$ = 3%: TV = 140 × 1.03/0.07 = **2,060**; PV = 2,060/1.331 = 1,547.7; EV = 295.27 + 1,547.7 = **1,843**, a 13% drop in EV for a 1 point change in $g$.

### In the news
See news box. For loss-making platforms, TV carries almost all the value, so a "richly valued" label is mostly a statement about terminal assumptions.

### Interview angle
> [!question] How it is asked
> "Your DCF has 85% of value in the terminal value. Is that a problem?"

> [!tip] Strong answer includes
> - Acknowledging the risk and showing a cross-check (implied multiple)
> - Sensible $g$ and reinvestment consistency
> - Sensitivity table for WACC and $g$
> - Longer explicit forecast for firms not yet at steady state

---
## 🔗 Go deeper: expansion notes
- [[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement|Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]
- [[226 Corporate Finance Essentials - Capital Structure & Cost of Capital|Corporate Finance Essentials - Capital Structure & Cost of Capital]]
