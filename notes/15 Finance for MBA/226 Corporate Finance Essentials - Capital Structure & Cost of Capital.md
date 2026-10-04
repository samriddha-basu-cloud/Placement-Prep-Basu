---
tags: [finance-for-mba, tier2]
area: Finance for MBA
topic: "Corporate Finance Essentials - Capital Structure & Cost of Capital"
tier: Tier 2
roles: Consulting / Finance
status: complete
subtopics: 14
---
# Corporate Finance Essentials - Capital Structure & Cost of Capital

⬅ [[225 Budgeting, Variance Analysis & Balanced Scorecard]] · [[_Index - Finance for MBA|Finance for MBA]] · [[227 GST & Indirect Tax for Supply Chains]] ➡

> **Area:** Finance for MBA · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / Finance

## Sub-topics in this note
1. [[#1. Capital Structure and Sources of Funds]]
2. [[#2. Cost of Equity: CAPM, Beta and the Equity Risk Premium]]
3. [[#3. Cost of Debt, Preference Capital and the Tax Shield]]
4. [[#4. WACC: Worked Calculation]]
5. [[#5. Modigliani-Miller: Capital Structure Irrelevance and the Tax Shield]]
6. [[#6. Trade-off, Pecking-Order and Agency/Signalling Theories]]
7. [[#7. Operating, Financial and Combined Leverage]]
8. [[#8. EBIT-EPS Analysis and the Indifference Point]]
9. [[#9. Dividend Policy: Irrelevance, Lintner and Payout Choices]]
10. [[#10. Share Buybacks: Mechanics, EPS Effect and Indian Rules]]
11. [[#11. Enterprise Value Bridge and Valuation Multiples]]
12. [[#12. M&A: Accretion/Dilution and Synergies]]
13. [[#13. Credit Ratings, Coverage Ratios and the Indian Regulatory Context]]
14. [[#14. ⭐ Advanced: Project-Specific Discount Rates, Beta Relevering and Adjusted Present Value]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Rates, buybacks and credit quality in India, October 2026
> **Policy rate and risk-free rate (checked 4 October 2026).** The RBI repo rate stands at **5.25%** (held in August 2026, neutral stance; SDF 5.00%, MSF and Bank Rate 5.50%). The MPC meets **5-7 October 2026** with the decision due on 7 October; in a Reuters poll of 61 economists (mid-to-late September), **35 expected a 25 bp hike to 5.50%**, which would be the first increase since February 2023. The benchmark 10-year G-sec yield was about **7.21% on 1 October 2026**, a two-and-a-half-year high. That 7.21% is the risk-free input for CAPM and WACC below. ([Outlook Money](https://www.outlookmoney.com/banking/rbi-mpc-october-2026-key-things-to-know-ahead-of-policy-decision); [Trading Economics](https://tradingeconomics.com/india/government-bond-yield))
>
> **Buyback taxation reset (from 1 April 2026).** Under the Income-tax Act, 2025 as amended by Finance Act 2026, share-buyback proceeds are taxed as **capital gains** in shareholders' hands, replacing the earlier deemed-dividend treatment. As enacted, an additional tax applies to **promoter** shareholders only for buybacks under section 68 of the Companies Act, 2013, making the aggregate burden about **22% for domestic-company promoters and 30% for others**. ([DPNC summary of Finance Act 2026](https://www.dpncindia.com/wp-content/uploads/2026/04/Finance-Act-2026-Some-Key-Amendments.pdf); [TaxGuru on the Finance Bill](https://taxguru.in/income-tax/buyback-taxation-shifted-dividend-capital-gains-1st-april-2026.html))
>
> **Credit health is strong (CRISIL, H1 FY27 reported 30 September 2026).** CRISIL's credit ratio for April-September 2026 was **2.18x** (464 upgrades against 213 downgrades; about 81% of ratings reaffirmed), up from 1.5x in H2 FY26; about 40% of upgrades came from infrastructure and allied sectors, median debt-to-equity near **0.5x**. For FY26, ICRA reported 388 upgrades against 124 downgrades (credit ratio 3.1x). ([IPA Newspack](https://ipanewspack.com/healthier-balance-sheets-drive-credit-upgrades-across-sectors-in-h1fy27/); [Business Standard](https://www.business-standard.com/industry/news/rating-agencies-see-moderation-in-credit-ratios-amid-global-risks-126040101287_1.html))
>
> **India's equity risk premium (Damodaran, 5 January 2026).** India is rated Baa3 (Moody's) with a **country risk premium of 2.85%** and a **total equity risk premium of 7.08%** on a 4.23% mature-market premium. ([Damodaran country risk table](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ctryprem.html))
>
> Sub-topics that say **"See news box"** reuse these items. Rates and tax rules were checked on 4 October 2026; the RBI decision of 7 October 2026 may change the repo rate. Company numbers in worked examples are illustrative.

---
## 1. Capital Structure and Sources of Funds
> 🟠 Tier 2 · _Key points:_ debt vs equity; instruments; D/E and D/(D+E); target structure

### Definition
**Capital structure** is the mix of long-term debt, preference capital and equity funding the firm's assets. Measures: **debt-to-equity** $D/E$, **debt ratio** $D/(D+E)$ (book or, better, market values), net debt/EBITDA.

| Source | Cost features | India examples |
|---|---|---|
| Equity (retained earnings, IPO, QIP, rights) | Highest required return, no mandatory payout | IPOs, QIPs, promoter infusion |
| Term loans, working-capital limits | Floating or fixed; security and covenants | Banks, NBFCs; repo-linked external-benchmark loans |
| NCDs, commercial paper, bonds | Priced off G-sec plus rating spread | Listed NCDs under SEBI rules |
| ECBs, trade credit | FX risk, RBI guidelines | External commercial borrowings |
| Hybrids (preference, convertibles) | Between debt and equity | CCPS, CCDs |

Debt is cheaper (lenders have priority and interest is tax deductible) but adds **fixed obligations** and bankruptcy risk. Operating firms must also fund **working capital** ([[136 Supply Chain Finance & Working Capital]]) and capex ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]). Ratios: [[108 Financial Statements & Ratios]].

### Example
Firm with debt ₹3,000 crore and equity (market) ₹7,000 crore: $D/(D+E)=30\%$, $D/E=0.43$. Book equity ₹3,500 crore would show $D/E=0.86$; market value is the right basis for cost of capital.

### In the news
See news box. With a repo rate of 5.25% and a 10-year G-sec at 7.21%, corporate borrowing costs are set by a rating spread over G-secs and are sensitive to the MPC outcome.

### Interview angle
> [!question] How it is asked
> "How would you decide whether a company should fund a ₹500 crore capex with debt or equity?"

> [!tip] Strong answer includes
> - Compare cost, risk, control dilution and flexibility
> - Look at current leverage, cash-flow stability, coverage and covenants
> - Match tenor of funding to asset life
> - Mention rating impact and target capital structure

---
## 2. Cost of Equity: CAPM, Beta and the Equity Risk Premium
> 🟠 Tier 2 · _Key points:_ ke = rf + β × ERP; levered vs unlevered beta; India inputs

### Definition
$$k_e=r_f+\beta\,(R_m-r_f)=r_f+\beta\times ERP$$
- $r_f$: yield on a government security of matching currency and horizon (India: 10-year G-sec).
- $\beta$: sensitivity of the stock to the market, from a regression of stock returns on index returns; **business risk** plus **financial leverage**.
- $ERP$: premium over the risk-free rate for holding equity.
Unlever and relever with the Hamada relation (assumes debt beta of zero):
$$\beta_L=\beta_U\left[1+(1-T)\frac{D}{E}\right]$$
Use **industry (peer) betas**, unlever each, average, then relever at the target structure; raw regression betas are noisy. Alternatives to CAPM: dividend-growth, build-up (rf + premiums), Fama-French factors.

### Example
Peer unlevered beta 0.80; target $D/E=3000/7000$; tax 25.17%. $\beta_L=0.80\times[1+0.7483\times0.4286]=1.057$. With $r_f=7.21\%$ and ERP 7.08% (Damodaran India total premium): $k_e=7.21\%+1.057\times7.08\%=\mathbf{14.69\%}$. Caution: Damodaran's premium is built from a USD mature-market premium plus a country premium, so pairing it with an INR risk-free rate is a practitioner shortcut; Indian practice often uses an ERP of 5-7% with the INR G-sec yield. With ERP 6%, $k_e=13.55\%$. Always state the choice.

### In the news
See news box. A higher 10-year yield lifts $r_f$ one-for-one into $k_e$ and WACC, so a 25 bp policy surprise can shift hurdle rates for capex across the economy.

### Interview angle
> [!question] How it is asked
> "How do you estimate the cost of equity of an unlisted Indian company?"

> [!tip] Strong answer includes
> - CAPM with peer betas unlevered and relevered at target D/E
> - Choice of rf (10-year G-sec) and ERP, with the currency consistency point
> - Size or illiquidity premium for small or unlisted firms
> - Cross-check with build-up or dividend-growth estimates

---
## 3. Cost of Debt, Preference Capital and the Tax Shield
> 🟠 Tier 2 · _Key points:_ use current marginal borrowing cost, not coupon history; after-tax = kd(1 − T)

### Definition
$$k_d^{\,after\text{-}tax}=k_d(1-T)$$
$k_d$ is the **current market yield** on the firm's long-term debt (yield to maturity on traded bonds, or risk-free rate plus rating-based spread, or a recent bank quote), not the coupon on old debt. The tax shield on interest is worth $T\times\text{Interest}$ a year, provided the firm earns enough taxable profit. Indian corporates choosing the concessional regime pay 22% plus surcharge and cess, an effective **25.17%** (22% × 1.10 × 1.04), checked as a standing rate; use the firm's marginal rate. **Preference capital:** $k_p=D_p/P_p$ with no tax shield (dividends are not deductible). Link: [[109 Valuation Basics (NPV, IRR, DCF)]].

### Example
Firm borrows at 9.5% pre-tax: $k_d=9.5\%\times(1-0.2517)=\mathbf{7.11\%}$. On ₹1,000 crore of debt, interest ₹95 crore saves tax of ₹23.9 crore (0.2517 × 95). A firm with accumulated losses and no taxable profit gets no shield, so its after-tax cost is the full 9.5%.

### In the news
See news box. A hike in the repo rate feeds through external-benchmark-linked loans quickly; fixed-rate NCDs reprice only at refinancing.

### Interview angle
> [!question] How it is asked
> "Why do we use the after-tax cost of debt in WACC?"

> [!tip] Strong answer includes
> - Interest is deductible, so the shareholders' net cost is lower
> - Use today's marginal rate, not historical coupon
> - Shield needs taxable profit; loss-making firms get none
> - Do not apply the shield to preference dividends

---
## 4. WACC: Worked Calculation
> 🟠 Tier 2 · _Key points:_ market-value weights; target structure; use as hurdle rate for average-risk projects

### Definition
$$WACC=\frac{E}{D+E}\,k_e+\frac{D}{D+E}\,k_d(1-T)\;(+\;\tfrac{P}{V}k_p)$$
Use **market-value** weights at the **target** structure. WACC is the discount rate for **average-risk projects financed in the firm's usual mix**; it is the minimum return the firm must earn to satisfy capital providers. Do not use it blindly for projects with different risk (see sub-topic 14). Applications: capex hurdle rate ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]), DCF valuation ([[109 Valuation Basics (NPV, IRR, DCF)]]), EVA ([[225 Budgeting, Variance Analysis & Balanced Scorecard]]), lease-vs-buy.

### Example
Using sub-topics 2-3: $E/V=70\%$, $k_e=14.69\%$, $D/V=30\%$, $k_d(1-T)=7.11\%$.
$$WACC=0.70\times14.69\%+0.30\times7.11\%=10.28\%+2.13\%=\mathbf{12.42\%}$$
Sensitivity: with ERP 6% ($k_e=13.55\%$), WACC = **11.62%**. A ₹400 crore plant earning ₹52 crore of NOPAT a year in perpetuity has a return of 13%, which beats 12.42% (NPV positive) but not a 13.5% hurdle. A 25 bp rise in $r_f$ raises WACC by roughly $0.70\times0.25\%=0.175\%$ (equity part only if debt is fixed-rate).

### In the news
See news box. At a 7.21% risk-free rate, even an AAA-rated Indian issuer has a base cost of capital above 10%; plan hurdle rates accordingly and re-check them when the MPC moves.

### Interview angle
> [!question] How it is asked
> "Calculate WACC given debt ₹300 crore at 9.5%, equity ₹700 crore, beta 1.1, rf 7.2%, ERP 6%, tax 25%."

> [!tip] Strong answer includes
> - $k_e=7.2+1.1\times6=13.8\%$, $k_d=7.125\%$, WACC = 0.7 × 13.8 + 0.3 × 7.125 = 11.80%
> - Market weights, target structure, after-tax debt
> - What WACC is and is not (project risk matters)
> - Sensitivity to beta, rf and leverage

---
## 5. Modigliani-Miller: Capital Structure Irrelevance and the Tax Shield
> 🟠 Tier 2 · _Key points:_ MM I (no tax): V is independent of leverage; MM II: ke rises with D/E; with tax V_L = V_U + T·D

### Definition
**No taxes, perfect markets:**
- **Proposition I:** $V_L=V_U$; WACC is constant at $k_u$.
- **Proposition II:** $k_e=k_u+(k_u-k_d)\dfrac{D}{E}$. Cheaper debt is exactly offset by costlier equity.

**With corporate tax (T), permanent debt:**
- $V_L=V_U+T\,D$ (the PV of the tax shield).
- $k_e=k_u+(k_u-k_d)(1-T)\dfrac{D}{E}$ and $WACC=k_u\left(1-T\dfrac{D}{V_L}\right)$ falls as debt rises.
Taken literally, 100% debt is optimal, which is why later theories add bankruptcy and agency costs.

### Example
Unlevered firm: EBIT ₹300 crore, $k_u=12\%$, $V_U=2{,}500$. Borrow ₹1,000 crore at 8% (no tax): $E=1{,}500$; $k_e=12\%+(12\%-8\%)\times\tfrac{1000}{1500}=14.67\%$; check: equity earnings (300 − 80) / 1,500 = 14.67%. WACC = 0.6 × 14.67% + 0.4 × 8% = **12%** (unchanged).
With tax 25%: $V_U=300\times0.75/0.12=1{,}875$; $V_L=1{,}875+0.25\times1{,}000=\mathbf{2{,}125}$; $E=1{,}125$; $k_e=14.67\%$ (check: (300 − 80) × 0.75 / 1,125); WACC = 0.5294 × 14.67% + 0.4706 × 8% × 0.75 = **10.59%**, below $k_u=12\%$. The value gain of ₹250 crore equals the PV of tax saved.

### In the news
See news box. The buyback-tax reset and moves in corporate tax regimes change the effective value of debt shields and payout channels, which is the MM tax logic in practice.

### Interview angle
> [!question] How it is asked
> "If debt is cheaper than equity, why not finance everything with debt?"

> [!tip] Strong answer includes
> - MM I and II: leverage raises the risk of equity so the blended cost does not fall (no tax)
> - With tax, the shield adds value $T\times D$
> - Counterforce: distress costs, agency costs, covenants, rating loss
> - Conclusion: an interior optimum, which the trade-off theory describes

---
## 6. Trade-off, Pecking-Order and Agency/Signalling Theories
> 🟠 Tier 2 · _Key points:_ trade-off: V = V_U + PV(shield) − PV(distress); pecking order: retained earnings → debt → equity; signalling

### Definition
- **Static trade-off:** $V_L=V_U+PV(\text{tax shield})-PV(\text{financial distress \& agency costs})$. WACC is U-shaped; the optimum is where marginal shield equals marginal distress cost. Asset-heavy, stable-cash-flow firms (utilities, infra) carry more debt than intangible-heavy or volatile firms.
- **Pecking order (Myers-Majluf):** because managers know more than investors, new equity is read as a signal that shares are overvalued; firms prefer **internal funds, then debt, then equity**. Explains why profitable firms often have low debt.
- **Agency theory (Jensen-Meckling):** debt disciplines managers (free cash flow) but creates shareholder-bondholder conflict (risk shifting, underinvestment).
- **Market timing and signalling:** equity is issued when valuations are high; higher payout or debt can signal confidence.

### Example
Illustrative U-shape (peer unlevered beta 0.873, $r_f=7.21\%$, ERP 7.08%, tax 25.17%, borrowing cost rising with leverage):

| D/V | Pre-tax $k_d$ | Relevered β | $k_e$ | WACC |
|---|---|---|---|---|
| 0% | 9.50% | 0.873 | 13.39% | 13.39% |
| 20% | 9.25% | 1.037 | 14.55% | 13.02% |
| 30% | 9.50% | 1.153 | 15.38% | **12.90%** |
| 40% | 10.50% | 1.309 | 16.48% | 13.03% |
| 50% | 12.00% | 1.527 | 18.02% | 13.50% |

WACC bottoms near 30% debt. (Borrowing costs are assumed for the illustration; real rating-based spreads must be used in a live analysis.)

### In the news
See news box. CRISIL's finding that median debt-to-equity of rated Indian firms is near 0.5x and that upgrades cluster in infrastructure fits the trade-off logic: stable, asset-backed cash flows carry more debt without a rating penalty.

### Interview angle
> [!question] How it is asked
> "Why does Infosys have almost no debt while L&T carries a lot?"

> [!tip] Strong answer includes
> - Business risk and cash-flow stability, asset tangibility
> - Pecking order: cash-rich firms need no external funds
> - Trade-off: distress costs differ by industry
> - Qualify with company specifics: ask for current balance sheets

---
## 7. Operating, Financial and Combined Leverage
> 🟠 Tier 2 · _Key points:_ DOL = CM/EBIT; DFL = EBIT/EBT; DCL = DOL × DFL

### Definition
$$DOL=\frac{CM}{EBIT},\qquad DFL=\frac{EBIT}{EBIT-I}=\frac{EBIT}{EBT},\qquad DCL=DOL\times DFL=\frac{CM}{EBT}$$
- **Operating leverage** arises from fixed operating costs: a given % change in sales produces a larger % change in EBIT.
- **Financial leverage** arises from fixed interest: a % change in EBIT produces a larger % change in EPS.
- **Combined leverage** is the total sensitivity of EPS to sales. High DCL with volatile demand is dangerous. Break-even and cost behaviour: [[110 Cost Accounting for Operations]].
- Plants with high fixed cost per unit ([[019 Facility Layout & Location]], capacity decisions) have high DOL.

### Example
Price ₹120, variable cost ₹70, 1,00,000 units, fixed cost ₹20,00,000, interest ₹5,00,000.
CM = 50 × 1,00,000 = ₹50,00,000; EBIT = ₹30,00,000; EBT = ₹25,00,000.
DOL = 50/30 = **1.67**; DFL = 30/25 = **1.20**; DCL = **2.0**.
A 10% volume rise to 1,10,000 units: EBIT = 55 − 20 = ₹35,00,000 (+16.7% = 10 × 1.67); EBT = ₹30,00,000 (+20% = 16.7 × 1.2); a 10% sales rise gives about +20% earnings. The same logic reverses on a 10% fall.

### In the news
See news box. A rate hike raises interest $I$ on floating-rate loans, pushing DFL up and squeezing EBT for highly levered firms.

### Interview angle
> [!question] How it is asked
> "Which would you rather own in a downturn: high operating leverage or high financial leverage?"

> [!tip] Strong answer includes
> - Both amplify swings; DCL multiplies them
> - Operating leverage depends on cost structure (fixed vs variable, make vs outsource)
> - Financial leverage is a choice that can be changed; operating leverage is harder to change
> - Link to flexibility via outsourcing and variable-cost contracts

---
## 8. EBIT-EPS Analysis and the Indifference Point
> 🟠 Tier 2 · _Key points:_ compare financing plans by EPS at various EBIT; indifference EBIT; EPS is not value

### Definition
$$EPS=\frac{(EBIT-I)(1-T)-D_p}{N}$$
The **indifference EBIT** is where two financing plans give the same EPS. Above it, the plan with more debt gives higher EPS; below it, the equity plan is better. EPS analysis ignores risk, so pair it with coverage ratios and the effect on the share price.

### Example
A firm has 10,00,000 shares, no debt and needs ₹5 crore. Plan A: issue 2,00,000 shares at ₹250. Plan B: ₹5 crore of 10% debt (interest ₹50 lakh). Tax 25%. Setting EPS equal: $\frac{X}{12\text{ lakh}}=\frac{X-50\text{ lakh}}{10\text{ lakh}}$ gives $X=\mathbf{₹3\text{ crore}}$.

| EBIT | EPS Plan A | EPS Plan B |
|---|---|---|
| ₹2 crore | 12.50 | 11.25 |
| ₹3 crore | 18.75 | 18.75 |
| ₹4 crore | 25.00 | 26.25 |

If EBIT is expected at ₹4 crore and is stable, debt lifts EPS by 5%; if demand is cyclical, the downside is larger.

### In the news
See news box. Stronger credit ratios (CRISIL 2.18x credit ratio) make debt-funded expansion cheaper, but higher policy rates would move indifference points upward.

### Interview angle
> [!question] How it is asked
> "A company wants to raise ₹500 crore. How would you compare debt and equity financing on EPS?"

> [!tip] Strong answer includes
> - EPS under each plan at expected and downside EBIT, and the indifference point
> - Interest coverage and rating impact, not just EPS
> - Dilution, control, and signalling effects of issuing equity
> - Conclusion linked to earnings stability

---
## 9. Dividend Policy: Irrelevance, Lintner and Payout Choices
> 🟠 Tier 2 · _Key points:_ MM irrelevance; bird-in-hand; Gordon model; Lintner smoothing; signalling; clientele

### Definition
- **MM dividend irrelevance:** with perfect markets and a fixed investment policy, value depends on earnings power, not payout; a dividend just moves value from share price to cash.
- **Bird-in-hand (Gordon/Lintner):** investors prefer certain dividends; **Gordon model** $P_0=\dfrac{E(1-b)}{k-br}$ for retention $b$ and return on retained funds $r$.
- **Tax and clientele effects:** in India, dividends are taxed in the hands of shareholders at slab rates (the dividend distribution tax was abolished from FY 2020-21), so low-slab investors prefer dividends and high-slab investors prefer buybacks or growth.
- **Signalling:** a dividend rise signals confidence in sustained earnings; a cut signals trouble.
- **Lintner:** firms smooth dividends, adjusting only partly toward a target payout: $D_t=D_{t-1}+s\,(p\,E_t-D_{t-1})$.
- **Residual policy:** pay only what is left after funding all positive-NPV projects ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]]).

### Example
EPS ₹50, required return $k=12\%$. If $r=15\%$ (reinvestment beats $k$): retention 0% → $P=50/0.12=₹417$; 40% → $g=6\%$, $P=30/(0.12-0.06)=₹500$; 60% → $g=9\%$, $P=20/(0.12-0.09)=₹667$. Retention adds value when $r>k$. If $r=10\%<k$, price falls with retention (₹417, ₹375, ₹333), so pay out. Lintner: previous DPS ₹10, target payout 50%, EPS ₹30, speed 0.3: DPS = 10 + 0.3 × (15 − 10) = **₹11.5**.

### In the news
See news box. The buyback tax reset from 1 April 2026 changes the relative appeal of dividends and buybacks for different shareholder groups and sets a distinct additional tax for promoters.

### Interview angle
> [!question] How it is asked
> "Should a profitable company with limited investment opportunities pay dividends or hold cash?"

> [!tip] Strong answer includes
> - Residual policy: return cash if returns on reinvestment < cost of capital
> - Signalling and smoothing; avoid frequent cuts
> - Tax clientele; options of dividend vs buyback
> - Ensure liquidity and covenants are respected

---
## 10. Share Buybacks: Mechanics, EPS Effect and Indian Rules
> 🟠 Tier 2 · _Key points:_ return of cash; EPS accretion needs earnings yield > after-tax yield on cash; Companies Act s.68 limits

### Definition
A **buyback** retires shares using surplus cash (or debt), shrinking the equity base. Compared with a dividend: flexible, tax treated as capital gains for shareholders from 1 April 2026, supports the share price. EPS rises when the **earnings yield** ($EPS/P$) exceeds the **after-tax return on the cash used**. Value per remaining share is unchanged if the repurchase is at fair value (it is a transfer, not value creation).

**Indian rules (Companies Act 2013, section 68, and SEBI Buy-back Regulations):**
- Maximum **25%** of aggregate paid-up capital and free reserves in a year (equity shares: 25% of paid-up equity capital).
- Board resolution suffices up to **10%**; above that a special resolution is needed.
- Post-buyback debt cannot exceed **2:1** to paid-up capital and free reserves.
- No fresh buyback offer within **one year** of closing the previous offer; funded from free reserves, securities premium or proceeds of a different kind of issue.
- Tender-offer buybacks reserve **15%** for small shareholders.
(These limits come from a law-firm summary read in this session; confirm against the current Act before relying on them.)

### Example
Net profit ₹2,000 crore, 40 crore shares (EPS ₹50), price ₹800 (P/E 16, earnings yield 6.25%). Buyback of ₹1,000 crore retires 1.25 crore shares at ₹800. Cash earned 7% pre-tax, so lost post-tax income = 1,000 × 7% × (1 − 0.2517) = ₹52.4 crore. New profit = ₹1,947.6 crore on 38.75 crore shares: EPS **₹50.26 (+0.5%)**. Because earnings yield 6.25% only slightly exceeds the 5.24% after-tax cash yield, accretion is small. At P/E 10 (price ₹500), accretion would be about +2.5%.

### In the news
See news box. After 1 April 2026, buyback proceeds are capital gains in shareholders' hands, and promoters face an additional levy for section 68 buybacks, so promoter participation is now less attractive.

### Interview angle
> [!question] How it is asked
> "Does a buyback create value for shareholders?"

> [!tip] Strong answer includes
> - Transfer, not creation, at fair value; it signals undervaluation and raises EPS mechanically
> - Compare earnings yield with after-tax return on cash
> - Compare with dividend: flexibility, tax treatment, signalling
> - Check leverage and growth opportunities foregone

---
## 11. Enterprise Value Bridge and Valuation Multiples
> 🟠 Tier 2 · _Key points:_ EV = equity + debt + minorities + prefs − cash − associates; EV/EBITDA, P/E, EV/Sales; consistency rules

### Definition
$$EV=\text{Market cap}+\text{Debt}+\text{Preference}+\text{Minority interest}-\text{Cash}-\text{Associates/non-operating investments}$$
$$\text{Equity value}=EV-\text{Net debt}-\text{Preference}-\text{Minorities}+\text{Associates}$$
**Match numerator and denominator:** EV multiples (EV/EBITDA, EV/EBIT, EV/Sales) pair with pre-financing metrics; equity multiples (P/E, P/B) pair with post-interest metrics. Choose comparables by business model, growth and margin, then use medians. Typical use: **trading comps** (listed peers), **precedent transactions** (control premium), and DCF as cross-check ([[109 Valuation Basics (NPV, IRR, DCF)]]). EV/EBITDA is popular for capital-intensive businesses; P/E for stable financials; EV/Sales for loss-making growth businesses. Debt for EV should include lease liabilities (Ind AS 116) consistently with EBITDA.

### Example
Market cap ₹5,000 crore, debt ₹1,500 crore, cash ₹300 crore, minority interest ₹100 crore, associates ₹150 crore: EV = 5,000 + 1,500 + 100 − 300 − 150 = **₹6,150 crore**; with EBITDA ₹700 crore, EV/EBITDA = **8.8x**.
Valuing a target: peer EV/EBITDA multiples 10.5, 12.0, 13.5, 11.0, 9.5 (median 11.0x; mean 11.3x). Target EBITDA ₹240 crore → EV = **₹2,640 crore**; net debt ₹800 crore → equity ₹1,840 crore; with 20 crore shares ≈ ₹92 per share.

### In the news
See news box. Higher G-sec yields compress multiples because the discount rate rises; a rate decision is also a valuation event.

### Interview angle
> [!question] How it is asked
> "Why use EV/EBITDA rather than P/E to compare two companies with different leverage?"

> [!tip] Strong answer includes
> - EV is capital-structure neutral; P/E is distorted by leverage
> - Include leases, minorities, pensions; subtract cash and associates consistently
> - Peers must match growth, margin and risk
> - Cross-check with DCF and precedent transactions

---
## 12. M&A: Accretion/Dilution and Synergies
> 🟠 Tier 2 · _Key points:_ pro forma EPS; stock vs cash; P/E rule; synergies needed to break even

### Definition
Pro forma EPS after an acquisition:
$$EPS_{pf}=\frac{NI_{acq}+NI_{tgt}+\text{Synergies}(1-T)-\text{After-tax financing cost}}{\text{Acquirer shares}+\text{New shares issued}}$$
A deal is **accretive** if $EPS_{pf}>EPS_{acq}$. Rules of thumb: a **stock deal** is accretive when the acquirer's P/E exceeds the price-paid P/E of the target; a **cash/debt deal** is accretive when the target's earnings yield (NI/price) exceeds the after-tax cost of debt. EPS accretion is not value creation: the deal must clear the cost of capital, and synergies must exceed the premium paid. More: [[159 Case Interview - M&A & Due Diligence]].

### Example
Acquirer: net profit ₹500 crore, 100 crore shares, EPS ₹5, P/E 20 → share price ₹100. Target: net profit ₹100 crore; price paid ₹2,400 crore (P/E 24). Debt cost 9.5% pre-tax, tax 25.17% (after-tax 7.11%).

| Structure | New shares / interest | Pro forma EPS | vs ₹5 |
|---|---|---|---|
| All stock | 24 crore shares | 600 / 124 = ₹4.84 | **−3.2%** dilutive |
| All cash (debt) | interest after tax ₹170.6 crore | (600 − 170.6)/100 = ₹4.29 | **−14.1%** dilutive |
| 50:50 | 12 crore shares; ₹1,200 crore debt | (600 − 85.3)/112 = ₹4.60 | **−8.1%** dilutive |

Why: stock P/E 20 < price P/E 24, and target earnings yield 4.17% < after-tax debt cost 7.11%. **Synergies needed to break even (all stock):** EPS 5 × 124 = ₹620 crore needed, so ₹20 crore post-tax, i.e., ₹26.7 crore pre-tax (20/0.7483), about 1.1% of the ₹2,400 crore price a year in cost or revenue synergy.

### In the news
See news box. Strong ratings (CRISIL credit ratio 2.18x) and a still-moderate cost of debt support leveraged deals, but with an after-tax debt cost of about 7.1% (9.5% pre-tax), a debt-funded deal needs a target earnings yield above that level to be accretive.

### Interview angle
> [!question] How it is asked
> "A company with P/E of 20 acquires a target at P/E of 24. Is it accretive?"

> [!tip] Strong answer includes
> - Stock deal dilutive (buying higher P/E with lower P/E paper)
> - Debt deal: compare earnings yield to after-tax debt cost
> - Quantify synergies required; mention integration costs and dis-synergies
> - Accretion is not value: premium vs NPV of synergies

---
## 13. Credit Ratings, Coverage Ratios and the Indian Regulatory Context
> 🟠 Tier 2 · _Key points:_ rating scales; interest coverage; net debt/EBITDA; SEBI-regulated CRAs; RBI roles

### Definition
**Credit ratings** (CRISIL, ICRA, CARE, India Ratings, Acuité, Brickwork; regulated by SEBI) give an ordinal view of default risk, from AAA (highest safety) to D (default); AAA-BBB is **investment grade**, BB and below speculative. Spread over G-secs widens down the scale. Drivers: business risk, financial profile, liquidity, promoter support. Key ratios:
$$\text{Interest coverage}=\frac{EBIT}{\text{Interest}},\quad \frac{\text{Net debt}}{EBITDA},\quad DSCR=\frac{\text{Cash flow available}}{\text{Interest}+\text{Principal}}$$
**RBI and SEBI basics:** the RBI sets the repo rate (through the MPC), regulates banks and NBFCs and the ECB framework; SEBI regulates listed securities, public issues, buybacks, bond disclosures and rating agencies; the Companies Act (MCA) governs dividends and buybacks. Floating-rate bank loans are linked to external benchmarks (repo), so policy moves pass through quickly. A **credit ratio** is upgrades divided by downgrades over a period. Link: [[012 Supply Chain Analytics & KPIs]] for cash-conversion metrics and [[136 Supply Chain Finance & Working Capital]].

### Example
EBIT ₹900 crore, interest ₹300 crore: coverage 3.0x. Net debt ₹1,200 crore (debt 1,500 − cash 300), EBITDA ₹700 crore: net debt/EBITDA = **1.71x**. Lenders often cap net debt/EBITDA near 3x and demand coverage above 2.5-3x, but thresholds vary by sector. A one-notch downgrade can add 25-50 bp to borrowing cost (illustrative); on ₹2,000 crore of debt, 40 bp costs ₹8 crore a year before tax.

### In the news
See news box. CRISIL's H1 FY27 ratio of 2.18x (464 upgrades, 213 downgrades) and a median debt-to-equity near 0.5x show healthy balance sheets, with downgrades concentrated in textiles and ceramics facing import competition.

### Interview angle
> [!question] How it is asked
> "What happens to a firm's cost of capital if its rating is downgraded?"

> [!tip] Strong answer includes
> - Higher spread on new borrowing, covenant and refinancing risk
> - WACC effect depends on weights and equity risk response
> - Ratios lenders watch (coverage, net debt/EBITDA, DSCR)
> - Mitigation: deleveraging, asset sales, equity infusion

---
## 14. ⭐ Advanced: Project-Specific Discount Rates, Beta Relevering and Adjusted Present Value
> ⭐ Advanced · _Added beyond the tracker_

### Definition
WACC at the firm level misprices projects whose risk or financing differs from the firm's. Better practice:
- **Project/division hurdle rates:** use pure-play peer betas, unlever, then relever at the target structure for that business.
- **Adjusted present value (APV):** $APV=\text{NPV at }k_u+PV(\text{financing side effects})$, mainly tax shields (minus distress and issue costs). Best when leverage changes over time (LBOs, project finance), because WACC then needs a changing weight.
- **Equity-vs-asset beta:** observed equity beta embeds the firm's own leverage; asset beta is the business risk alone.
- **Pitfalls:** one company-wide WACC overinvests in risky divisions and underinvests in safe ones; using book weights; mixing nominal flows with real rates; double-counting tax shields (in both WACC and cash flows).

### Example
Observed beta 1.2 at $D/E=0.5$, $T=25.17\%$: $\beta_U=1.2/(1+0.7483\times0.5)=\mathbf{0.873}$. Relevered at $D/E=0.25$: 1.037; at $D/E=1.0$: 1.527.
APV: unlevered cash flow ₹100 crore a year forever, $k_u=12\%$: $V_U=833.3$. Permanent debt ₹400 crore, tax 25%: shield PV = 0.25 × 400 = ₹100 crore; **APV = ₹933.3 crore**. If the project costs ₹900 crore, NPV is +₹33.3 crore, whereas at $k_u$ alone the project would show −₹66.7 crore: financing, not operations, makes it viable, so a banker should state that explicitly.

### In the news
See news box. With the 10-year G-sec rising to 7.21%, hurdle rates must be refreshed division by division, not just at group level; CRISIL's finding that infrastructure-linked sectors lead upgrades implies lower distress cost and so more debt capacity there.

### Interview angle
> [!question] How it is asked
> "A group has an IT services arm and a steel plant. Would you use one WACC for both?"

> [!tip] Strong answer includes
> - No; unlever peer betas for each business and relever at its target structure
> - Different capital structures and risk imply different hurdle rates
> - APV when debt is project-specific or changing
> - Sanity check against the group WACC and execution risk
