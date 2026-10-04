---
tags: [finance-for-mba, tier2]
area: Finance for MBA
topic: "Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement

⬅ [[110 Cost Accounting for Operations]] · [[_Index - Finance for MBA|Finance for MBA]] · [[225 Budgeting, Variance Analysis & Balanced Scorecard]] ➡

> **Area:** Finance for MBA · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Capex Decision Framework and Incremental Cash Flows]]
2. [[#2. Appraisal Metrics on a Plant Expansion: NPV, IRR, PI and Payback]]
3. [[#3. Depreciation Tax Shield and the Indian Block of Assets]]
4. [[#4. Working Capital in Projects]]
5. [[#5. Building the Automation Business Case]]
6. [[#6. Equipment Replacement and Equivalent Annual Cost]]
7. [[#7. Choosing between Machines of Unequal Lives]]
8. [[#8. Lease vs Buy]]
9. [[#9. Hurdle Rates and Cost of Capital for Capex]]
10. [[#10. Sensitivity, Scenario and Break-Even Analysis]]
11. [[#11. Capital Rationing and Project Portfolios]]
12. [[#12. Real Options Intuition]]
13. [[#13. ⭐ Advanced: Real vs Nominal Flows and the Inflation Trap]]
14. [[#14. ⭐ Advanced: Own vs Outsource a Warehouse (Utilisation Break-Even)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India's capex wave puts appraisal discipline in the spotlight
> **Steel needs about ₹10 lakh crore of new capex to reach 300 MT (IBEF, 2025).** India's steel plan of **300 million tonnes a year of capacity by 2030** is described as needing roughly **₹10 lakh crore (US$156 billion) of additional investment by 2030-31**; April-July 2025 crude steel output was **54.19 MT**. ([IBEF steel](https://www.ibef.org/industry/steel))
>
> **Cement capacity race (IBEF, FY25).** Production rose to about **453 million tonnes** in FY25 (from 426.29 MT, +6.3%) against **668 MT of installed capacity** (March 2025), with **150-160 MT** of further capacity planned between FY25 and FY28. ([IBEF cement](https://www.ibef.org/industry/cement-india))
>
> **PLI schemes turn capex into cash incentives (IBEF, 2025).** Production-linked incentive schemes had disbursed **₹21,534 crore across 12 sectors**, with PLI-linked investment of **₹1.76 lakh crore**; manufacturing FDI totalled ₹14,45,781 crore. ([IBEF manufacturing](https://www.ibef.org/industry/manufacturing-sector-india)). Incentives belong in the project cash flows, see [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].
>
> **New Income-tax Act in force (from 1 April 2026).** The Income-tax Act, 2025 replaced the 1961 Act; it uses a single "Tax Year" instead of previous year/assessment year and cuts the text from over 800 provisions to **536 sections, 23 chapters and 16 schedules**. Depreciation and block-of-assets rules should be re-read in the new text before a live model. ([Wikipedia summary](https://en.wikipedia.org/wiki/Income-tax_Act,_2025))
>
> Sub-topics that say **"See news box"** reuse these items. Tax rates and depreciation percentages below are the long-standing 1961-Act values; they are flagged where a re-check against the 2025 Act's schedules is needed (checked October 2026). All project numbers are illustrative.

---
## 1. Capex Decision Framework and Incremental Cash Flows
> 🟠 Tier 2 · _Key points:_ incremental after-tax cash flows; ignore sunk costs; include working capital, salvage, opportunity costs and cannibalisation

### Definition
A capital-budgeting decision compares the firm **with the project** against the firm **without it**. Only **incremental, after-tax, cash** flows count:

$$FCF_t=(EBITDA_t-Dep_t)(1-T)+Dep_t-\Delta NWC_t-Capex_t$$

where $T$ is the tax rate and $Dep_t$ is tax depreciation. Rules:
- **Ignore sunk costs** (feasibility study already paid) and financing flows (interest sits in the discount rate).
- **Include opportunity costs** (land or a line the project uses), **cannibalisation** and **side effects** (lower sales of an existing product), **working capital** and **end-of-life salvage**.
- Use **nominal flows with a nominal rate** or **real flows with a real rate** (see sub-topic 12).
- **Tax**: Indian corporates choosing the concessional regime (section 115BAA) pay 22% plus 10% surcharge and 4% cess, an effective **25.17%** (22% × 1.10 × 1.04 = 25.168%; section numbers change under the 2025 Act, so cite the rate, not the clause); hand calculations below round to 25%.

Capex types to recognise in operations: **expansion** (new line), **replacement** (equipment at end of life), **cost-saving** (automation), **regulatory/safety** (must-do) and **strategic** (option-like). Link: [[109 Valuation Basics (NPV, IRR, DCF)]] for the core formulas, [[110 Cost Accounting for Operations]] for cost behaviour, [[188 Financial Modelling in Excel]] for the spreadsheet build.

### Example
A plant manager says: "We spent ₹40 lakh last year on a study; with that, this ₹6 crore line is a bargain." The study is **sunk** and irrelevant. If the line uses an idle shed that could be rented for ₹30 lakh a year, that rent is an **opportunity cost** and must be a cash outflow of the project (₹30 lakh × (1 − 0.25) = ₹22.5 lakh after tax a year).

### In the news
See news box. Steel's ₹10 lakh crore and cement's 150-160 MT additions are expansion capex at industry scale; each project inside those totals is judged by the same incremental-cash-flow test.

### Interview angle
> [!question] How it is asked
> "A company is considering a new ₹50 crore line. Which cash flows would you include?"

> [!tip] Strong answer includes
> - Incremental, after-tax, cash-based flows; sunk costs excluded
> - Working capital, salvage, opportunity cost and cannibalisation
> - Financing flows left to the discount rate
> - Consistency of real vs nominal; a mention of tax shield on depreciation

---
## 2. Appraisal Metrics on a Plant Expansion: NPV, IRR, PI and Payback
> 🟠 Tier 2 · _Key points:_ full cash-flow table; NPV at WACC; IRR; profitability index; simple and discounted payback

### Definition
$$NPV=\sum_{t=0}^{n}\frac{FCF_t}{(1+r)^t},\qquad PI=\frac{PV(\text{future cash inflows})}{\text{initial outlay}},\qquad NPV=0\ \text{at}\ r=IRR$$

- **NPV > 0** accept; PI > 1 is the same decision restated per rupee invested (useful under budget limits).
- **IRR** is a return, not a rupee amount; compare it with the hurdle rate; prefer NPV for mutually exclusive projects ([[109 Valuation Basics (NPV, IRR, DCF)]]).
- **Payback** shows liquidity risk, not value.

### Example
**Pune line expansion.** Capex ₹50 crore on plant and machinery (15% WDV block); sales volume 6 lakh units a year at ₹1,500 (₹90 crore at full run); variable cost 62% of sales; fixed cash cost ₹16 crore; volume ramps 70%, 90%, then 100%; net working capital 12% of sales, recovered in Year 6; sale of machine at ₹5 crore at the end of Year 6; tax 25%; WACC 12%. (Half-year depreciation rule ignored for simplicity.)

| ₹ crore | Y0 | Y1 | Y2 | Y3 | Y4 | Y5 | Y6 |
|---|---|---|---|---|---|---|---|
| Sales | | 63.0 | 81.0 | 90.0 | 90.0 | 90.0 | 90.0 |
| EBITDA | | 7.94 | 14.78 | 18.20 | 18.20 | 18.20 | 18.20 |
| Tax depreciation | | 7.50 | 6.38 | 5.42 | 4.61 | 3.92 | 3.33 |
| EBIT | | 0.44 | 8.41 | 12.78 | 13.59 | 14.28 | 14.87 |
| Tax at 25% | | 0.11 | 2.10 | 3.20 | 3.40 | 3.57 | 3.72 |
| EBITDA − tax | | 7.83 | 12.68 | 15.00 | 14.80 | 14.63 | 14.48 |
| Change in NWC | | −7.56 | −2.16 | −1.08 | 0 | 0 | +10.80 |
| Salvage plus tax shield on remaining block | | | | | | | 6.92 |
| **Free cash flow** | **−50.00** | **0.27** | **10.52** | **13.92** | **14.80** | **14.63** | **32.21** |
| Discount factor at 12% | 1.000 | 0.893 | 0.797 | 0.712 | 0.636 | 0.567 | 0.507 |
| Present value | −50.00 | 0.24 | 8.39 | 9.91 | 9.41 | 8.30 | 16.32 |

- Contribution at full run = 90 × 0.38 = ₹34.2 crore; EBITDA = 34.2 − 16 = ₹18.2 crore. The Year 6 shield term is explained in sub-topic 3: ₹1.92 crore.
- **NPV** = ₹2.56 crore (the rounded table sums to ₹2.57 crore). **IRR = 13.3%**. **PI** = 52.56 ÷ 50 = **1.05**.
- **Cumulative cash flow**: −50, −49.73, −39.21, −25.29, −10.49, +4.14, so simple **payback = 4 + 10.49 ÷ 14.63 = 4.72 years**. Discounted payback: cumulative PV −13.75 at Y5, +2.56 at Y6, so **5.84 years**.
- **NPV profile**: 36.35 at 0%; 19.50 at 5%; 6.77 at 10%; 2.56 at 12%; about 0 at 13.3%; −3.00 at 15%.

Verdict: accept on paper but **thin**: a ₹2.56 crore NPV on ₹60.8 crore of peak funding (₹50 crore capex plus ₹10.8 crore working capital) is about 4%; sub-topic 10 shows why this needs a scenario test.

### In the news
See news box. PLI-type incentives would be added as extra cash inflows and could lift this NPV; an incentive of 2% of incremental sales on ₹63-90 crore of sales would add about ₹1.3-1.8 crore a year before tax (an illustration, not an actual scheme term).

### Interview angle
> [!question] How it is asked
> "A plant costs ₹50 crore and yields ₹12 crore a year for six years. Should we build it at a 12% cost of capital?"

> [!tip] Strong answer includes
> - NPV first, with IRR and PI as cross-checks
> - Payback as a liquidity and risk screen, with the discounted version
> - Working capital recovery and salvage in the last year
> - A comment on how thin the margin of safety is

---
## 3. Depreciation Tax Shield and the Indian Block of Assets
> 🟠 Tier 2 · _Key points:_ WDV block system; 15% plant and machinery, 40% computers; PV of shield = t·d·C/(r+d)

### Definition
Depreciation is non-cash but cuts tax, so each rupee of depreciation is worth $T$ rupees of cash: **shield = depreciation × T**.

Indian income-tax depreciation is computed on a **block of assets** (assets of the same class and rate) by the **written-down-value (WDV) method**:

$$Dep_t=d\times WDV_{t-1}^{\text{block}},\qquad WDV_t=WDV_{t-1}+\text{additions}-\text{sale proceeds}-Dep_t$$

Under the 1961 Act the commonly used rates (Appendix I to the Income-tax Rules; re-check the schedules under the Income-tax Act, 2025) are: **plant and machinery (general) 15%**, **computers and software 40%**, **buildings other than residential 10%**, **furniture 10%**, **motor cars 15%**, **pollution-control and energy-saving equipment 40%**. Points to remember:
- Assets put to use for under 180 days in the year get only **half** the rate in that year.
- Selling an asset **reduces the block's WDV**; the block continues. Only if the block has no assets left is the shortfall a short-term capital loss (usable against capital gains, not business income).
- **Additional depreciation** of 20% on new plant in manufacturing exists in the 1961 Act, but it is not available to companies that choose the concessional 22% regime (confirm for the current year).
- The concessional 15% regime for new manufacturers (section 115BAB) applied only to units starting production by 31 March 2024; do not assume it for a new project without checking.
- Book depreciation (Companies Act Schedule II, straight line) differs from tax depreciation; the difference creates deferred tax but **cash flows use tax depreciation**.

**Present value of the shield.** For a declining-balance block run indefinitely:

$$PV(\text{shield})=\frac{T\,d\,C}{r+d}$$

Fraction of cost recovered in PV terms, $T=25.17\%$, $r=12\%$: 5% block 7.4%; 10% block 11.4%; **15% block 14.0%**; 40% block **19.4%**; immediate write-off 25.2%. Faster write-off means higher value.

### Example
₹10 crore machine, 15% block, $T=25.168\%$, $r=12\%$.

| Year | Opening WDV | Depreciation | Tax shield |
|---|---|---|---|
| 1 | 10.000 | 1.500 | 0.3775 |
| 2 | 8.500 | 1.275 | 0.3209 |
| 3 | 7.225 | 1.084 | 0.2728 |
| 4 | 6.141 | 0.921 | 0.2318 |
| 5 | 5.220 | 0.783 | 0.1971 |

- PV of the first five years of shield at 12% = **₹1.046 crore**; WDV left after five years = ₹4.437 crore.
- PV of the whole perpetual stream = 0.25168 × 0.15 × 10 ÷ 0.27 = **₹1.398 crore** (14.0% of cost).
- Compare straight-line over 5 years (₹2 crore a year): PV of shield = 0.5034 × 3.6048 = **₹1.815 crore**. The WDV block system is slower because depreciation shrinks each year.
- In the Pune line, the block's WDV after Year 6 is 50 × 0.85⁶ = ₹18.86 crore; after the ₹5 crore sale it is ₹13.86 crore; the shield on that remainder, at 25% and 12%, is 0.25 × 0.15 × 13.86 ÷ 0.27 = **₹1.92 crore**, counted as part of terminal value.

### In the news
See news box. The Income-tax Act, 2025 came into force on 1 April 2026 with a new section and schedule structure, so models built on 1961-Act clause numbers need re-mapping; also see how GST input credit on capital goods affects the true capex outlay in [[227 GST & Indirect Tax for Supply Chains]].

### Interview angle
> [!question] How it is asked
> "Why does depreciation matter in a cash-flow model if it is non-cash?" or "How does the block-of-assets system affect the tax shield?"

> [!tip] Strong answer includes
> - Shield = depreciation × tax rate, and why faster write-off is worth more
> - Block / WDV mechanics: sale proceeds reduce the block; half-year rule
> - The perpetuity shortcut $\frac{TdC}{r+d}$
> - Flag that rates and clauses must be checked against the current Act

---
## 4. Working Capital in Projects
> 🟠 Tier 2 · _Key points:_ NWC is an investment, recovered at the end; days-based build; releases lift NPV

### Definition
A project that raises sales also raises receivables and inventory, partly offset by payables:

$$NWC=\text{Receivables}+\text{Inventory}-\text{Payables},\qquad \Delta NWC_t=NWC_t-NWC_{t-1}$$

Receivables = sales × DSO ÷ 365; inventory and payables = COGS × days ÷ 365. $\Delta NWC$ is a **cash outflow** when positive, and the balance is **recovered** when the project ends (or is carried into terminal value for a going concern). Working-capital terms are an operational lever: see [[136 Supply Chain Finance & Working Capital]] and [[003 Inventory Management]].

### Example
For the Pune line at full sales of ₹90 crore and COGS of ₹55.8 crore (variable cost): receivables 45 days = 90 × 45 ÷ 365 = **₹11.10 crore**; inventory 50 days of COGS = 55.8 × 50 ÷ 365 = **₹7.64 crore**; payables 50 days = **₹7.64 crore**; NWC = **₹11.10 crore (12.3% of sales)**; the model uses 12% = ₹10.8 crore.
- **Impact on value**: dropping the working-capital line gives an NPV of ₹6.33 crore instead of ₹2.56 crore, so ignoring it overstates value by **₹3.77 crore**.
- **Lever**: cutting receivable days by 10 releases 90 × 10 ÷ 365 = **₹2.47 crore** of cash once.

### In the news
See news box. For the capacity additions in steel and cement, the capex bill gets the headline, but the working capital that the new volume ties up sits outside it and still has to be funded (analytical reading).

### Interview angle
> [!question] How it is asked
> "Does working capital belong in a capex appraisal? How do you treat it?"

> [!tip] Strong answer includes
> - NWC as a build-up and recovery with $\Delta NWC$ in the flow
> - Days-based calculation (DSO, DIO, DPO)
> - Quantified effect on NPV and on payback
> - Operational levers (terms, inventory policy)

---
## 5. Building the Automation Business Case
> 🟠 Tier 2 · _Key points:_ capex split by tax block; labour savings with wage growth; ramp-up; break-even savings

### Definition
A cost-saving project (warehouse conveyors/sorters, AS/RS, cobots, a new WMS) has no revenue line: the **cash flow is the cost avoided**. Build it as: **benefits** (labour, error and damage reduction, throughput) − **new costs** (annual maintenance contract, power, software subscriptions) = pre-tax savings; apply tax with depreciation by block; add a **ramp-up** and a **terminal value**. Link: [[127 Warehouse Engineering - Racking, Sizing & Material Handling]], [[128 Warehouse Labour, WES-WCS & Yard Management]], [[016 Digital Supply Chain & Industry 4.0]].

### Example
**Sortation automation at a fulfilment centre.** Capex ₹30 crore: ₹24 crore equipment (15% block) and ₹6 crore software and controls (40% block). Labour: 200 FTE × ₹4.5 lakh = ₹9 crore a year, wages growing 6% a year; throughput and damage savings ₹2.4 crore; maintenance contract −₹1.9 crore growing 4% a year; power −₹0.6 crore; benefits ramp 60% in Year 1; 10-year horizon; salvage ₹3 crore; tax 25% (losses in Year 1 shield other income); WACC 12%.

| ₹ crore | Y1 | Y2 | Y3 | Y5 | Y8 | Y10 |
|---|---|---|---|---|---|---|
| Pre-tax savings | 4.34 | 9.36 | 9.86 | 10.94 | 12.83 | 14.30 |
| Tax depreciation | 6.00 | 4.50 | 3.46 | 2.19 | 1.22 | 0.86 |
| After-tax cash flow | 4.75 | 8.15 | 8.26 | 8.75 | 9.93 | 10.94 (+3.25 terminal) |

Year 1 check: labour 9 × 0.6 = 5.40; throughput 2.4 × 0.6 = 1.44; maintenance −1.90; power −0.60; savings = **4.34**.

- **NPV = ₹18.20 crore; IRR = 23.6%; payback about 4.05 years.**
- **Break-even**: NPV falls to about zero if labour savings are **60% of the plan (about 120 FTE displaced, not 200)**.
- **Stress tests**: labour savings −20% → NPV ₹9.16 crore; capex +25% → ₹12.03 crore; wage growth 3% instead of 6% → ₹13.12 crore; a one-year delay in benefits → ₹10.77 crore.

Business-case lesson: the project survives every single stress but fails if **two or three** go wrong together, and the largest driver is how many FTE are actually removed (not capex), so the operational plan for redeploying staff drives value.

### In the news
See news box. Government PLI support and the cost of labour in India's warehouse belt make automation economics a live question; the same analysis applies to capacity decisions covered in [[018 Capacity Management & OEE]].

### Interview angle
> [!question] How it is asked
> "A warehouse wants to spend ₹30 crore on automation. How would you evaluate it?"

> [!tip] Strong answer includes
> - Savings built bottom-up (FTE × cost, errors, throughput) net of new run costs
> - Ramp-up, wage inflation and terminal value
> - Break-even savings and one or two stress tests
> - Non-financial factors: service level, safety, scalability, vendor lock-in

---
## 6. Equipment Replacement and Equivalent Annual Cost
> 🟠 Tier 2 · _Key points:_ EAC converts unequal-life costs into a yearly figure; replace when EAC of new < cost of keeping old one more year

### Definition
For cost-only comparisons (same output either way), compute the **present value of all costs** and convert to an equal annual figure:

$$EAC=\frac{PV(\text{costs})}{A_{n,r}},\qquad A_{n,r}=\frac{1-(1+r)^{-n}}{r}$$

Capital cost, discounted operating costs and salvage go into the PV; the old machine's **current market value is an opportunity cost** (not its book value, which is sunk). **Decision rules:** (1) compare EAC of the new machine with EAC of continuing the old machine for its remaining life; (2) a sharper test is to compare the **cost of running the old machine one more year** with the new machine's EAC, and replace when old exceeds new. Related reliability thinking: [[155 Reliability Engineering & Maintenance Optimisation]] and [[022 Maintenance Management (TPM-RCM)]].

### Example
**CNC machine, ₹ lakh, 12% rate, pre-tax.** Old machine: market value now 12, four years of life left, running cost 9, 10, 11, 12 in Years 1-4, salvage 2 at the end of Year 4. New machine: cost 36, life 8 years, running cost 4.0 rising by 0.5 a year (4.0 to 7.5), salvage 4 at the end of Year 8.
- PV old = 12 + (9/1.12 + 10/1.12² + 11/1.12³ + 12/1.12⁴) − 2/1.12⁴ = **42.19**; annuity factor (4 years) = 3.0373; **EAC old = 13.89**.
- PV new = 36 + PV of running costs − 4/1.12⁸ = **61.49**; annuity factor (8 years) = 4.9676; **EAC new = 12.38**.
- Cost of keeping old one more year, with market values 12, 9, 6.5, 4, 2 at the end of Years 0-4: Year 1 = 9 + (12 × 1.12 − 9) = **13.44**; Year 2 = 13.58; Year 3 = 14.28; Year 4 = 14.48. Every figure exceeds the new machine's 12.38, so **replace now**, saving about ₹1.1-2.1 lakh a year depending on how long the old machine would otherwise be kept.
- Tax refinement: add depreciation shields to both and the proceeds-reduce-the-block rule from sub-topic 3.

### In the news
See news box. In sectors adding capacity at scale (cement, steel), a new plant often displaces older, costlier units, so expansion and replacement capex overlap; the EAC test isolates the cost side (analytical reading).

### Interview angle
> [!question] How it is asked
> "Our 5-year-old machine still works. When should we replace it?"

> [!tip] Strong answer includes
> - Market value as an opportunity cost; book value as sunk
> - EAC for old and new, or the one-more-year cost
> - Rising maintenance and downtime on the old asset
> - Technology, quality and energy benefits outside the cost model

---
## 7. Choosing between Machines of Unequal Lives
> 🟠 Tier 2 · _Key points:_ do not compare raw PVs; use EAC or a common replication horizon

### Definition
A cheaper machine with a short life is not automatically better. Compare on a common basis: either **EAC** or the **replication chain** (repeat each option until the lowest common multiple of lives). They give the same ranking. EAC assumes each option can be renewed at the same cost, which is a modelling assumption to state aloud.

### Example
**Machine X**: cost ₹20 lakh, life 3 years, running cost ₹6 lakh a year. **Machine Y**: cost ₹30 lakh, life 5 years, running cost ₹4.5 lakh a year. Zero salvage; 12%.
- PV X = 20 + 6 × 2.4018 = **34.41**; EAC X = 34.41 ÷ 2.4018 = **₹14.33 lakh**.
- PV Y = 30 + 4.5 × 3.6048 = **46.22**; EAC Y = 46.22 ÷ 3.6048 = **₹12.82 lakh**.
- Raw PVs (34.41 vs 46.22) wrongly favour X. **Replication check**: over the 15-year common horizon X is bought five times and Y three times, giving chain PVs of **97.58** and **87.33**. Dividing by the 15-year annuity factor $A_{15,12\%}=6.8109$ returns the same EACs: 97.58 ÷ 6.8109 = 14.33 and 87.33 ÷ 6.8109 = 12.82. **Choose Y.**

### In the news
See news box. A shorter-lived, cheaper asset looks attractive when financing is tight; the EAC view shows the hidden cost of re-buying more often.

### Interview angle
> [!question] How it is asked
> "Machine A costs less but lasts 3 years; machine B costs more and lasts 5. How do you choose?"

> [!tip] Strong answer includes
> - Why raw NPV or PV comparison is misleading
> - EAC or LCM replication, with the assumption of like-for-like renewal
> - Inflation, technology change and salvage as caveats
> - A sensitivity on the discount rate

---
## 8. Lease vs Buy
> 🟠 Tier 2 · _Key points:_ discount at after-tax cost of debt; compare PV cost of buying and leasing; break-even rental

### Definition
Leasing is a financing choice, so the **discount rate is the after-tax cost of debt**, $k_d(1-T)$. Compare the **PV of after-tax cost of owning** (outlay − PV of depreciation shield − PV of salvage) with the **PV of after-tax lease rentals**:

$$PV_{\text{buy}}=C-\sum\frac{T\cdot Dep_t}{(1+k)^t}-\frac{S_n+\text{shield on residual block}}{(1+k)^n},\qquad PV_{\text{lease}}=L(1-T)A_{n,k}$$

$$NAL=PV_{\text{buy}}-PV_{\text{lease}}\quad(\text{lease if }NAL>0)$$

Other points: under **Ind AS 116** a lessee recognises a right-of-use asset and lease liability for most leases (exceptions: 12 months or less and low-value assets), so leasing no longer hides debt; GST on rentals and capital-goods input credit should be checked ([[227 GST & Indirect Tax for Supply Chains]]); the lessor's residual value, maintenance bundling and flexibility are real benefits of leasing (forklifts, trucks, MHE).

### Example
**₹10 crore material-handling fleet.** Buy with a loan at 10% (after-tax 7.5%); 15% block; sale after 5 years at ₹3 crore; lease rental ₹2.5 crore a year for 5 years (in arrears); tax 25%.
- Depreciation shields (₹ crore): 0.375, 0.319, 0.271, 0.230, 0.196; PV at 7.5% = **1.152**.
- WDV after five years = 10 × 0.85⁵ = 4.437; after the ₹3 crore sale, 1.437 stays in the block; its shield value = 0.25 × 0.15 × 1.437 ÷ (0.075 + 0.15) = 0.240 at Year 5, PV **0.167**.
- PV of salvage = 3 ÷ 1.075⁵ = **2.090**.
- **PV cost of buying** = 10 − 1.152 − 2.090 − 0.167 = **₹6.59 crore**.
- **PV cost of leasing** = 2.5 × 0.75 × 4.0459 = **₹7.59 crore**.
- NAL = 6.59 − 7.59 = **−₹0.99 crore**: buy. The **break-even rental** is 6.59 ÷ (0.75 × 4.0459) = **₹2.17 crore a year**; if the lessor offers below that, lease.

### In the news
See news box. With steel needing about ₹10 lakh crore of new capex, leasing peripheral assets (fleets, MHE, IT) to save capital for core plant is a natural question (analytical reading).

### Interview angle
> [!question] How it is asked
> "Should we lease or buy a fleet of trucks or forklifts?"

> [!tip] Strong answer includes
> - After-tax cost of debt as the discount rate and the reason
> - PV cost of buying vs leasing, and the break-even rental
> - Residual value risk, maintenance bundling and flexibility
> - Balance-sheet and covenant effects under Ind AS 116

---
## 9. Hurdle Rates and Cost of Capital for Capex
> 🟠 Tier 2 · _Key points:_ WACC as base; adjust for project risk; do not use the company WACC for every project

### Definition
The **hurdle rate** is the minimum acceptable return. A common starting point is **WACC**:

$$WACC=\frac{E}{V}k_e+\frac{D}{V}k_d(1-T),\qquad k_e=R_f+\beta\,(ERP)$$

Use a **project-specific rate** when the project's risk differs from the firm's: add a premium for a new technology or new geography, or use a pure-play beta. Companies commonly set hurdle rates above WACC (for example WACC plus 2-4 percentage points) to cover estimation bias. Do not raise the rate to be "safe" and also build pessimistic cash flows: that double-counts risk. Details in [[226 Corporate Finance Essentials - Capital Structure & Cost of Capital]].

### Example
Illustrative inputs (refresh the risk-free rate from the current 10-year G-sec yield): $R_f$ 6.5%, equity risk premium 6.5%, beta 1.1; pre-tax cost of debt 9.5%; target 70% equity and 30% debt; tax 25%.
- $k_e$ = 6.5 + 1.1 × 6.5 = **13.65%**; after-tax $k_d$ = 9.5 × 0.75 = **7.125%**.
- WACC = 0.7 × 13.65 + 0.3 × 7.125 = **11.69%, about 12%** (the rate used in the Pune line).
- An automation project judged riskier by 2 points is evaluated at 14%. The automation case stays strongly positive (NPV ₹12.13 crore even at 15%), while the Pune line's IRR of 13.3% falls below a 14% hurdle: the same risk adjustment kills the thin project and leaves the strong one standing.

### In the news
See news box. With steel needing about ₹10 lakh crore of new capex, even a one-point change in the hurdle rate shifts the NPV of every project in the pipeline through $r$ (analytical reading).

### Interview angle
> [!question] How it is asked
> "What discount rate would you use for a project in a new business line?"

> [!tip] Strong answer includes
> - WACC derivation with CAPM and after-tax debt
> - Adjustment for project risk, not just company risk
> - Avoiding double counting of risk in rate and cash flows
> - IRR vs hurdle comparison and the sensitivity of NPV to the rate

---
## 10. Sensitivity, Scenario and Break-Even Analysis
> 🟠 Tier 2 · _Key points:_ one-variable tornado; combined scenarios; break-even volume and price

### Definition
- **Sensitivity**: change one driver at a time and record the NPV (tornado chart).
- **Scenario analysis**: change several drivers together into pessimistic, base and optimistic cases and weight them by probability.
- **Break-even (NPV = 0)**: the driver value at which the project just earns the hurdle rate; the gap to base is the **margin of safety**.
- Simulation ([[150 Decision Analysis & Simulation]]) is the next step for correlated risks.

### Example
Pune line (base NPV ₹2.56 crore):

| Change | NPV (₹ crore) |
|---|---|
| Volume −10% | −6.72 |
| Volume +10% | +11.84 |
| Price −5% | −9.95 |
| Price +5% | +15.08 |
| Variable cost +5% | −5.31 |
| Fixed cost +10% | −2.37 |
| Capex +20% | −6.05 |

- **Break-even volume** is 97.2% of plan, i.e. 5.83 lakh units against 6.0 lakh (−2.8%); **break-even price** is 1.0% below plan. Price is the dominant driver: a 5% change moves NPV by about ₹12.5 crore each way, versus ₹9.3 crore for 10% on volume.
- **Scenarios** (pessimistic: volume −15%, price −3%, variable cost +4%; optimistic: volume +10%, price +2%; tax losses usable elsewhere): pessimistic NPV **−₹23.09 crore (IRR −1.1%)**, base **₹2.56 crore**, optimistic **+₹17.35 crore (IRR 20.6%)**. With probabilities 25%/50%/25%, expected NPV = −5.77 + 1.28 + 4.34 = **−₹0.16 crore**, so a project that looked acceptable on the base case is **marginal** on a risk-weighted basis.

### In the news
See news box. When 150-160 MT of cement capacity is planned against 668 MT already installed, utilisation and price are the obvious risks, so wide scenario ranges on both are reasonable (analytical reading).

### Interview angle
> [!question] How it is asked
> "The NPV is positive. What could make this project fail?"

> [!tip] Strong answer includes
> - One-way sensitivity to find the dominant driver
> - Scenarios with probabilities and an expected NPV
> - Break-even volume or price with the margin of safety
> - Mitigations: contracts, phasing, hedging, pricing power

---
## 11. Capital Rationing and Project Portfolios
> 🟠 Tier 2 · _Key points:_ budget limit; rank by PI; check combinations; integer programming for large sets

### Definition
When capital is limited (**capital rationing**), the goal is to choose the **combination of projects with the highest total NPV within the budget**, not simply the highest-NPV or highest-IRR projects. Ranking by **profitability index** works when projects are divisible; with indivisible projects the greedy PI rule can miss the best combination and an integer-programming (knapsack) model is exact ([[148 Operations Research - Network Models & Integer Programming]], [[146 Operations Research - Linear Programming]]). Soft rationing (management limit) and hard rationing (market limit) differ in how binding the budget is.

### Example
Budget ₹50 crore; outlay and NPV (₹ crore):

| Project | Outlay | NPV | PI (NPV/outlay) |
|---|---|---|---|
| A | 30 | 11.7 | 0.39 |
| B | 20 | 9.0 | 0.45 |
| C | 25 | 10.0 | 0.40 |
| D | 15 | 5.0 | 0.33 |

- **Greedy by PI**: take B (20), then C (25) = 45 outlay, NPV **19.0**; A needs 30 but only 5 is left.
- **Best combination** (enumerate all feasible sets): **A + B** = 50 outlay, NPV **20.7**. Other feasible sets: B + C 19.0; A + D 16.7; C + D 15.0; B + D 14.0.
- Lesson: the PI rule left ₹5 crore unused; the exact answer is worth ₹1.7 crore more. Also consider a funding-cost view: borrow more if the project IRR exceeds the marginal cost of funds.

### In the news
See news box. Groups with several expansion projects in the cement and steel pipelines must fit them inside a board-approved capex envelope, which is a rationing problem in practice (analytical reading).

### Interview angle
> [!question] How it is asked
> "You have ₹50 crore and four projects. How do you decide?"

> [!tip] Strong answer includes
> - Maximise total NPV under the budget, not rank by IRR
> - PI as a first screen and exact combination for indivisible projects
> - Interdependence (mutually exclusive, contingent projects)
> - Questioning whether the budget constraint is real

---
## 12. Real Options Intuition
> 🟠 Tier 2 · _Key points:_ option to expand, delay or abandon; flexibility has value that static NPV misses

### Definition
Static NPV assumes a fixed plan. Real options recognise that management can **expand** if demand is strong, **delay** until uncertainty resolves, **switch** inputs or **abandon** and recover salvage. Value of a project with flexibility:

$$\text{Expanded NPV}=\text{Static NPV}+\text{Value of options}$$

The value of an option rises with **uncertainty** (volatility), unlike NPV which usually falls with risk. Use a simple decision tree ([[150 Decision Analysis & Simulation]]) or a binomial lattice for numbers; use the intuition when exact option models are not defensible. Typical operations examples: a modular warehouse that can add a second phase, a plant built with shell space for a second line, a pilot before roll-out.

### Example
**Phase 1 pilot line** has a static NPV of **−₹2 crore**. If demand proves high in Year 2 (probability 50%), the company can spend ₹20 crore on Phase 2, whose present value at that date is ₹30 crore (NPV +₹10 crore); if demand is low it does not expand (value 0).
- Value of the expansion option today = 0.5 × 10 ÷ 1.12² = **₹3.99 crore**.
- **Total value** = −2 + 3.99 = **+₹1.99 crore**: the project is worth doing for its option, even though its static NPV is negative.
- If the option instead costs ₹3 crore to hold (for example, extra shell space), the net value is −2 + 3.99 − 3 = −₹1.01 crore, so pay for flexibility only when the option value exceeds its cost.

### In the news
See news box. Capacity plans such as the 150-160 MT of cement additions over FY25-28 are naturally phased, which is where the option to speed up, slow down or stop a later phase has value (analytical reading).

### Interview angle
> [!question] How it is asked
> "A pilot has negative NPV. Why might we still do it?"

> [!tip] Strong answer includes
> - Option to expand, delay or abandon, and why uncertainty raises its value
> - A simple tree with probabilities and discounting
> - Cost of keeping the option open
> - Caveat that options must be real (rights actually held and exercisable)

---
## 13. ⭐ Advanced: Real vs Nominal Flows and the Inflation Trap
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Cash flows and discount rates must be in the same terms:

$$1+r_{nominal}=(1+r_{real})(1+\pi)$$

If flows are in today's rupees (real), use the real rate; if they include inflation (nominal), use the nominal rate. Depreciation tax shields are **fixed in nominal rupees** (based on historical cost), so inflation makes them worth less in real terms; working capital grows with nominal sales; and different cost lines inflate at different rates (wages, power, steel).

### Example
Outlay ₹100 crore; real cash inflow ₹30 crore for 5 years; real rate 8%; inflation 5%.
- Nominal rate = 1.08 × 1.05 − 1 = **13.4%**.
- Correct, real flows at 8%: NPV = **₹19.78 crore**; correct, nominal flows (30 × 1.05ᵗ) at 13.4%: **₹19.78 crore** (same).
- **Mismatch 1**: real flows at the nominal 13.4% gives ₹4.50 crore, understating value by 77%.
- **Mismatch 2**: nominal flows at the real 8% gives ₹37.95 crore, overstating value by 92%.
- In India, wage inflation of 6% in the automation case (sub-topic 5) against a 4% maintenance escalator is a deliberate mix of nominal rates by line.

### In the news
See news box. On the long horizons typical of steel and cement capex, a small inflation-treatment error compounds into a large valuation gap; the tax-law change in the news box is another reason to re-check assumptions each year (analytical reading).

### Interview angle
> [!question] How it is asked
> "Your cash flows are in constant prices but the rate is nominal. What is wrong?"

> [!tip] Strong answer includes
> - The Fisher relationship and matching terms
> - Why depreciation shields do not inflate
> - Different inflation rates by cost line
> - A numerical illustration of the error

---
## 14. ⭐ Advanced: Own vs Outsource a Warehouse (Utilisation Break-Even)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Owning (or long-leasing) a facility turns variable 3PL charges into **fixed** costs. The key variable is **utilisation**:

$$\text{Cost per used position}=\frac{\text{Annualised capex}+\text{fixed opex}}{\text{positions}\times 12\times u},\qquad \text{Annualised capex}=Capex\times\frac{r}{1-(1+r)^{-n}}$$

The ratio $\frac{r}{1-(1+r)^{-n}}$ is the **capital recovery factor (CRF)**. Own wins above a break-even utilisation; below it, 3PL's pay-per-use flexibility wins. Strategic factors: control, service level, seasonality, network design ([[113 Network Design & Facility Location Modelling]], [[019 Facility Layout & Location]], [[010 Warehouse Management]], [[129 E-commerce & Quick-Commerce Fulfilment]]).

### Example
Own warehouse: capex ₹40 crore (racking, MHE, WMS, fit-out; land leased), 15-year life, 12% hurdle; fixed opex ₹4.5 crore a year; 20,000 pallet positions (240,000 position-months a year); 3PL quote ₹520 per used pallet-month. (Illustrative; ignores tax and variable handling.)
- CRF(12%, 15) = 0.12 ÷ (1 − 1.12⁻¹⁵) = **0.1468**; annualised capex = 40 × 0.1468 = **₹5.87 crore**; total annual cost = ₹10.37 crore.
- Cost per position-month at 100% fill = 10.37 × 10⁷ ÷ 240,000 = **₹432**; at 70% fill = ₹432 ÷ 0.7 = **₹617**.
- **Break-even utilisation** = 432 ÷ 520 = **83%**: own below 83% is more expensive than 3PL; above it, cheaper.
- Decision: if demand is seasonal with a 60-90% fill swing, a hybrid (own the base load, 3PL the peak) beats either extreme.

### In the news
See news box. If the policy push on logistics infrastructure described in [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]] widens 3PL supply and lowers quotes, the break-even utilisation an owner must clear rises (analytical reading; no 3PL price data was verified).

### Interview angle
> [!question] How it is asked
> "Should the client build its own warehouse or use a 3PL?"

> [!tip] Strong answer includes
> - Annualised capex via CRF plus fixed opex vs 3PL variable price
> - Break-even utilisation and demand variability
> - Hybrid and phased options (real-options thinking from sub-topic 12)
> - Non-cost factors: control, service, scalability and exit cost
