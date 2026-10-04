---
tags: [supply-chain-management, tier2]
area: Supply Chain Management
topic: "Commodity Price Risk, Hedging & Contract Pricing Mechanisms"
tier: Tier 2
roles: Operations / Finance / Consulting
status: complete
subtopics: 13
---
# Commodity Price Risk, Hedging & Contract Pricing Mechanisms

⬅ [[122 Spend Analysis, Savings & Procurement Maturity]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]] ➡

> **Area:** Supply Chain Management · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Finance / Consulting

## Sub-topics in this note
1. [[#1. Commodity Exposure Mapping (Direct, Indirect, Embedded)]]
2. [[#2. Price Drivers, Benchmarks and Volatility]]
3. [[#3. Forwards, Futures, Options and Swaps: The Basics]]
4. [[#4. Hedge Ratio and Basis Risk (Worked Example)]]
5. [[#5. Hedging Policy, Governance and Accounting]]
6. [[#6. Index-Linked Contracts and Pass-Through Clauses]]
7. [[#7. Price Escalation Formulas (Worked)]]
8. [[#8. Fixed vs Floating Pricing: The Cost of Certainty]]
9. [[#9. Forward Buying, Strategic Stock and Timing Purchases]]
10. [[#10. Dual Sourcing, Substitution and Supply-Side Risk]]
11. [[#11. Tyre Industry Case: Rubber and Crude Basket]]
12. [[#12. India Specifics: MCX, LME Parity, SEBI and RBI]]
13. [[#13. ⭐ Advanced: Cost-at-Risk and a Portfolio View of Commodity Exposure]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): raw-material baskets, oil and rubber swing faster than price lists
> **JK Tyre on the raw-material squeeze (Autocar Professional, 21 September 2026).** Management said raw materials are roughly **67% of total costs**; the company had taken price increases of about **12.5%** overall (4-5% in the replacement market, 5-7% in exports) and saw "still an 8-9% gap" to offset in the second half. It also flagged that the raw-material basket could rise **18-20% sequentially in Q1 FY27**, citing geopolitical factors and currency weakness. ([Autocar Professional](https://www.autocarpro.in/feature/inside-jk-tyres-growth-bet-134810))
>
> **Crude oil swings (1 October 2026).** Brent traded at about **$98.15 a barrel** and WTI at **$90.35**, after Brent gained roughly **14% in September**, with US-Iran talks and recovering West Asian exports driving the market. (Crude is the feedstock chain for synthetic rubber, carbon black and polymers, and sets diesel and freight costs.) ([Business Standard](https://www.business-standard.com/markets/commodities/oil-prices-steady-as-investors-assess-us-iran-peace-talks-supply-outlook-126100100084_1.html))
>
> **Rubber futures (29 September 2026).** The Singapore-listed TSR20 rubber future (5-tonne contract) closed at 245.30 on the page quoted, within a 52-week range of **168.10 to 262.90** and about **44% higher over the year**: a swing that a tyre maker cannot ignore. ([Investing.com](https://www.investing.com/commodities/rubber-tsr20-futures))
>
> **Market plumbing is not risk-free.** The London Metal Exchange (owned by HKEX, which bought it for £1.4 billion in 2012) cancelled nickel trades during the March 2022 spike; the UK FCA fined LME **£9.2 million in March 2025** for failing to prevent the volatility. In India, MCX has been regulated by SEBI since the Forward Markets Commission merged into it in September 2015. ([Wikipedia: London Metal Exchange](https://en.wikipedia.org/wiki/London_Metal_Exchange); [Wikipedia: MCX](https://en.wikipedia.org/wiki/Multi_Commodity_Exchange))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Commodity Exposure Mapping (Direct, Indirect, Embedded)
> 🟠 Tier 2 · _Key points:_ Natural rubber, crude, steel, aluminium, copper, cotton; share of COGS; who bears the risk

### Definition
**Commodity price risk** is the risk that input (or output) prices move against the firm, hitting margin or budget. Mapping starts from the **bill of materials and cost sheet**: which inputs are (a) **direct** (the commodity itself: natural rubber for a tyre, steel coil for a stamping), (b) **indirect/derived** (carbon black, synthetic rubber and polyester cord track crude oil chains; freight tracks diesel), and (c) **embedded** in bought-in components (a supplier's price includes its own copper or aluminium). For each: annual quantity, ₹ value, % of COGS, price volatility, contract terms (fixed, index-linked, spot), and pass-through ability to customers.

| Commodity | Typical Indian users | Price discovery (reference) |
|---|---|---|
| Natural rubber | Tyres, gloves, belts | SGX/Osaka/Shanghai futures, Rubber Board domestic grades |
| Crude oil and derivatives | Petrochemicals, synthetic rubber, polymers, freight | Brent/WTI; MCX crude futures |
| Steel (HRC, long, wire rod) | Auto components, construction, capital goods | Domestic trade prices and published indices; thin futures |
| Aluminium, copper, zinc | Wheels, wires, cables, electrical, EV | LME; MCX base-metal futures |
| Cotton | Textiles, apparel | ICE cotton; domestic quotes |

The exposure is not only the **price level**: also **FX** (most benchmarks are in US dollars), **freight**, **duties** and **availability**. Combine with [[110 Cost Accounting for Operations|cost sheets]] to compute margin sensitivity.

### Example
Tyre maker, sales ₹100 (index), total costs ₹86, EBITDA ₹14 (14%). Raw materials are 67% of costs: 0.67 × 86 = **₹57.6**. A 10% rise in the raw-material basket adds ₹5.76, so costs become ₹91.76 and EBITDA falls to ₹8.24 (**8.2%**). To restore the original EBITDA rupees, price must rise **5.76%**; to restore the 14% margin, price must rise **6.7%** (solve $(100+x-91.76)/(100+x) = 0.14$). A hedge or pass-through clause is worth exactly this much.

### In the news
See news box. JK Tyre's 67% raw-material share and a 12.5% price rise with a remaining 8-9% gap are the same arithmetic in real figures.

### Interview angle
> [!question] How it is asked
> "Raw-material prices rose 10%. How does that hit this company's margin and what would you do?"

> [!tip] Strong answer includes
> - Cost-structure arithmetic (share of COGS x price change)
> - Map direct, derived and embedded exposure (including FX)
> - Levers: pass-through, hedging, sourcing, formulation or design, inventory timing
> - Check price elasticity, competitor behaviour and contract lags before raising prices

---
## 2. Price Drivers, Benchmarks and Volatility
> 🟠 Tier 2 · _Key points:_ Supply shocks, demand, FX, speculation; reference prices; volatility measurement

### Definition
Commodity prices respond to **supply** (weather, mine and plantation output, OPEC+ decisions, export bans), **demand** (industrial cycles, China), **stocks** (inventory-to-use ratios), **substitution** (synthetic vs natural rubber, aluminium vs steel), **currency** (USD strength), **policy** (duties, quotas, sanctions) and **financial flows**. Natural rubber is grown mostly in Asia (Thailand, Indonesia and Vietnam together about 61% of output in 2022) and competes with petroleum-based synthetic rubber, which links it to crude oil; India ranks third as a producer and fourth as a consumer ([Wikipedia: Natural rubber](https://en.wikipedia.org/wiki/Natural_rubber)). Regulatory shifts such as the EU deforestation rules (EUDR) add compliance cost to the rubber chain.

**Volatility** = standard deviation of returns, annualised (monthly $\sigma \times \sqrt{12}$). A "price risk budget" uses volatility to translate exposure into **cost at risk** (see the advanced section). Volatility clusters: it rises after shocks, so hedge policy should not assume a stable $\sigma$.

### Example
Monthly percentage changes in natural rubber have a standard deviation of 6.0%. Annualised volatility = 6.0% × √12 = **20.8%**. On an annual purchase of ₹400 crore, a one-standard-deviation adverse move costs about ₹83 crore (0.208 × 400) before any pass-through or hedge, and about **₹137 crore at 95%** (1.645 × 83) if returns are roughly normal (a simplification: commodity returns have fat tails).

### In the news
See news box. Brent's 14% September gain and the TSR20 range of 168.10 to 262.90 show volatility on both the crude and rubber legs of a tyre cost sheet at once.

### Interview angle
> [!question] How it is asked
> "What drives natural-rubber prices and how would you track them for a tyre company?"

> [!tip] Strong answer includes
> - Supply, demand, stocks, FX, substitution, policy as driver buckets
> - Which benchmarks and indices a buyer monitors (and the weekly review cadence)
> - Volatility to quantify exposure, with caveats on tails
> - Early-warning links: crude to synthetic rubber, USD/INR to import parity

---
## 3. Forwards, Futures, Options and Swaps: The Basics
> 🟠 Tier 2 · _Key points:_ OTC vs exchange, margining, call/put, cap/collar, commodity swap

### Definition
| Instrument | Mechanics | Locks in | Notes |
|---|---|---|---|
| **Forward** | OTC agreement to buy at a fixed price on a future date | Price | Tailor-made; counterparty credit risk; no margin or daily settlement |
| **Futures** | Standardised exchange contract; daily mark-to-market, initial and variation margin | Price | Liquid; basis risk since contract may differ in grade, location, month; margin calls hit cash |
| **Call option** | Right (not obligation) to buy at strike; premium paid | A **maximum** price (cap) | Keeps downside benefit; costs premium |
| **Put option** | Right to sell at strike | A minimum price | Used by producers/sellers |
| **Collar** | Buy a call, sell a put | A price **band** | Can be zero-premium; gives up gains below the put strike |
| **Swap** | Exchange floating price for fixed over a period, settled in cash | Average price | OTC, with banks/traders; suits monthly consumption |

A **buyer** (tyre maker) hedges by going **long** futures or buying calls (gains if prices rise, offsetting higher physical cost). A **seller** (plantation, aluminium smelter) goes short. Physical purchase and hedge are **separate transactions**: the hedge pays off in cash even if no commodity is delivered.

### Example
Buy a call on rubber with a strike of ₹190 per kg and a premium of ₹6. Effective cost = spot + premium − call payoff:

| Spot at expiry (₹/kg) | Call payoff | Effective cost |
|---|---|---|
| 171 | 0 | 177 |
| 190 | 0 | 196 |
| 196 | 6 − 6 = 0 net | 196 |
| 209 | 19 − 6 = 13 net | **196** |

The cost is capped at ₹196 (strike plus premium) while a fall to ₹171 still benefits the buyer (cost 177). A **zero-cost collar** (buy ₹190 call, sell ₹170 put): effective cost stays between **170 and 190** whatever the market does; below ₹170 the buyer gives the gain away.

### In the news
See news box. LME's 2022 nickel episode (trades cancelled, later litigation, FCA fine of £9.2 million in March 2025) is a reminder of exchange and liquidity risks hidden in a "simple" hedge.

### Interview angle
> [!question] How it is asked
> "Futures vs options for hedging raw-material price: when would you choose each?"

> [!tip] Strong answer includes
> - Futures: cheap, symmetric, margin calls; options: insurance with premium, keep upside
> - Collar for budget certainty with limited cost
> - Matching hedge quantity and timing with the physical purchase
> - Option premiums rise with volatility, so buying protection after a spike is expensive (see [[109 Valuation Basics (NPV, IRR, DCF)|valuation basics]] for time-value ideas)

---
## 4. Hedge Ratio and Basis Risk (Worked Example)
> 🟠 Tier 2 · _Key points:_ Minimum-variance hedge ratio; basis = spot minus futures; effective price

### Definition
A hedge is rarely perfect because the futures price $F$ and the price actually paid $S$ do not move one-for-one. **Basis** $b = S - F$ (spot minus futures). With a hedge ratio of 1 the effective purchase price is $S_1 - (F_1 - F_0) = F_0 + b_1$: the hedge fixes the futures price and leaves the **basis at the end** as the risk. The **minimum-variance hedge ratio**:

$$h^* = \rho \, \frac{\sigma_S}{\sigma_F}, \qquad N^* = \frac{h^* \, Q_A}{Q_F}$$

where $\rho$ is the correlation of spot and futures price changes, $\sigma_S$ and $\sigma_F$ their standard deviations, $Q_A$ the quantity exposed and $Q_F$ the contract size. Basis risk grows with **grade mismatch** (RSS4 in Kerala vs TSR20 in Singapore), **location**, **maturity mismatch**, and **currency** (INR spot vs USD futures).

### Example
A tyre maker will buy **500 tonnes** of natural rubber in three months at an expected ₹190/kg and hedges on a 5-tonne futures contract. Correlation $\rho = 0.85$, $\sigma_S = 6.0\%$, $\sigma_F = 6.5\%$: $h^* = 0.85 \times 6.0/6.5 =$ **0.785**; contracts = 0.785 × 500 / 5 = 78.5, so **78 contracts** (390 tonnes, 78% hedged). Futures price today (converted to ₹/kg) is ₹176: basis = 190 − 176 = **₹14**.

**Prices rise:** spot ₹209, futures ₹192.5. Unhedged cost = 209 × 5,00,000 kg = ₹10.45 crore. Futures gain = (192.5 − 176) × 3,90,000 = ₹64.35 lakh. Net cost **₹9.81 crore**, an effective **₹196.13/kg**. (A 100% hedge would give 192.5.) Basis widened from 14 to 16.5.

**Prices fall:** spot ₹171, futures ₹158.5. Unhedged cost = ₹8.55 crore. Futures loss = (158.5 − 176) × 3,90,000 = −₹68.25 lakh. Net cost **₹9.23 crore**, effective **₹184.65/kg**: the hedge removed the benefit of a price fall. That is the cost of certainty, and why a **hedge policy** must be agreed with the board in advance.

### In the news
See news box. With TSR20 up about 44% in a year, a buyer who left exposure open carried a large unhedged cost; but the 168 to 263 range also shows how a hedge placed at the wrong time locks in a high price.

### Interview angle
> [!question] How it is asked
> "You hedged 100% of the exposure and prices fell. Was the hedge a mistake?"

> [!tip] Strong answer includes
> - A hedge is insurance for budget certainty, not a profit centre
> - Minimum-variance ratio and why a ratio below 1 is common
> - Basis risk sources and how to reduce them (closer grade, matching maturity)
> - Cash-flow and margin-call planning; hedge-effectiveness testing

---
## 5. Hedging Policy, Governance and Accounting
> 🟠 Tier 2 · _Key points:_ Board-approved policy, layered hedging, limits, Ind AS 109 hedge accounting

### Definition
A **commodity hedging policy** states: purpose (protect margin, not speculate), **exposures in scope**, permitted **instruments and counterparties**, **hedge cover limits by horizon** (e.g. 75% for 0-3 months, 50% for 3-6, 25% for 6-12), **layered (rolling) hedging** (add cover in tranches to average the entry price), **limits** on position, loss triggers, **segregation of duties** (front office, middle-office risk, back-office confirmation) and **reporting** to a risk committee. Governance avoids the classic failures: unhedged "hedges" sized above physical needs (speculation), concentration with one counterparty, and no mark-to-market reporting.

**Accounting (Ind AS 109, Financial Instruments):** derivatives are measured at fair value; **cash flow hedge accounting** lets the effective portion of the gain or loss sit in the cash-flow hedge reserve (in other comprehensive income) until the hedged purchase affects profit. Needs formal documentation at inception and effectiveness assessment (economic relationship; hedge ratio consistent with actual hedging). Without hedge accounting, mark-to-market swings hit profit before the purchase occurs. Link to [[225 Budgeting, Variance Analysis & Balanced Scorecard|budgeting and variance]] and [[108 Financial Statements & Ratios|financial statements]].

### Example
Annual rubber need ₹400 crore; policy cover 75% / 50% / 25% for the next 3 / 3-6 / 6-12 months, applied to quarterly needs of ₹100 crore each: hedged = 0.75×100 + 0.50×100 + 0.25×200 = 75 + 50 + 50 = **₹175 crore (43.8%)** of 12-month exposure. Layering by buying a third of each tranche monthly avoids locking the whole book on one bad day.

### In the news
See news box. After a 44% one-year rubber move and a 14% monthly crude gain, risk committees review whether cover limits and layering rules still match volatility.

### Interview angle
> [!question] How it is asked
> "How would you set up a commodity hedging programme at a manufacturer?"

> [!tip] Strong answer includes
> - Exposure identification first, hedge only what is physical and forecast
> - Policy: cover ratios by horizon, instruments, limits, governance
> - Accounting treatment (hedge accounting) and cash-margin planning
> - KPIs: hedge effectiveness, average hedged price vs spot, budget variance

---
## 6. Index-Linked Contracts and Pass-Through Clauses
> 🟠 Tier 2 · _Key points:_ Price tied to a published index; lag; collar; share of price indexed

### Definition
Instead of the buyer hedging, **the contract price floats with a published index** (an agreed formula). Design choices:
- **Index choice**: transparent and not manipulable, correlated with the supplier's real cost (e.g. a feedstock index for carbon black, a published HRC steel price for stampings, LME aluminium for castings). Public price sources: exchanges, Platts, Argus, government, trade bodies.
- **Share indexed**: only the commodity portion of cost is indexed; conversion cost stays fixed.
- **Reset frequency and lag**: monthly or quarterly, using the average of the previous month to reduce noise.
- **Dead band / threshold**: no change if the index moves less than ±3-5%.
- **Cap and floor / collar**: limit the pass-through.
- **Symmetry**: price falls must also pass through (a common negotiating point).
- **Currency**: index in USD converted at an agreed FX rate.
- **Audit and dispute terms**, and a **review right** if the index is discontinued.
Pass-through works both ways: **upstream** (supplier to buyer) and **downstream** (buyer to its customers). OEM-tier contracts in autos often have material-escalation annexures.

### Example
Supplier's price depends on feedstock (55%), power (20%), labour (10%) and a fixed portion (15%). Base price ₹110/kg. Feedstock index +12%, power +4%, labour +3%: new price = 110 × (0.15 + 0.55×1.12 + 0.20×1.04 + 0.10×1.03) = 110 × 1.077 = **₹118.47/kg** (+7.7%). With a ±3% dead band, a feedstock rise of only 2.5% would trigger no change that period; a monthly reset with the one-month lag means the buyer sees the rise only after a month: lag helps budgeting but defers recovery.

### In the news
See news box. JK Tyre needed 12.5% in price increases against input inflation: a downstream pass-through that lags upstream cost moves is exactly where margin leaks.

### Interview angle
> [!question] How it is asked
> "A supplier wants a raw-material escalation clause. What terms would you insist on?"

> [!tip] Strong answer includes
> - Transparent, public index; only the commodity share indexed
> - Symmetric pass-through, dead band, caps, reset and lag
> - Right to audit supplier cost basis; FX treatment
> - Compare with a fixed price and hedge: who is best placed to carry the risk

---
## 7. Price Escalation Formulas (Worked)
> 🟠 Tier 2 · _Key points:_ Base price x weighted index ratios; fixed element; project and long-term contracts

### Definition
Long-term supply, EPC and infrastructure contracts use an **escalation (price variation) formula**:

$$P_t = P_0 \left[a + b\,\frac{M_t}{M_0} + c\,\frac{L_t}{L_0} + d\,\frac{E_t}{E_0}\right], \qquad a + b + c + d = 1$$

$a$ = fixed element (not escalated; margin and overhead), $b, c, d$ = weights on material, labour and energy indices. The base indices $M_0$, $L_0$, $E_0$ are those at the base date (usually bid submission). Government and PSU contracts, and EPC contracts (see [[168 Project Procurement, Contracts & EPC Delivery]]) often use published indices, e.g. wholesale price index components. Good practice: **cap total escalation**, specify **rate base dates**, clarify which period's index applies (delivery date vs billing date), and cover **price falls**.

### Example
Contract for 2,000 tonnes of fabricated steel at base ₹80,000 per tonne. Weights: fixed 20%, steel 55%, labour 15%, energy 10%. Index ratios at delivery: steel 1.08, labour 1.04, energy 1.06. Factor = 0.20 + 0.55×1.08 + 0.15×1.04 + 0.10×1.06 = 0.20 + 0.594 + 0.156 + 0.106 = **1.056**. Escalated price = ₹80,000 × 1.056 = **₹84,480/t**; extra cost = 2,000 × 4,480 = **₹89.6 lakh**. A 5% overall cap would limit the factor to 1.05, price ₹84,000, a difference of ₹9.6 lakh to the buyer.

### In the news
See news box. In a quarter where the raw-material basket swings by double digits, escalation formulas and caps decide who carries the shock: supplier, buyer or the end customer.

### Interview angle
> [!question] How it is asked
> "Calculate the escalated price and discuss whether the clause is balanced."

> [!tip] Strong answer includes
> - Correct weights summing to 1 and base-date indices
> - Fixed element and cap; symmetric treatment
> - Who verifies the index and how disputes are resolved
> - Interaction with fixed-price and lump-sum risk transfer

---
## 8. Fixed vs Floating Pricing: The Cost of Certainty
> 🟠 Tier 2 · _Key points:_ Who bears volatility; risk premium; duration; budget vs margin

### Definition
A **fixed-price contract** transfers price risk to the supplier, who prices it in as a **risk premium**; a **floating (index-linked) price** passes volatility through and removes the premium. The choice depends on: the buyer's ability to pass costs on, the supplier's ability to hedge, the contract tenor, the commodity's volatility, and the relationship. Hybrids: **fixed for the quarter, reset quarterly**; **band pricing** (fixed within a collar, floating outside); **cost-plus with an open book**; **partial indexing**. Under accounting and budgeting, fixed prices give a predictable budget; floating gives margin protection only if the downstream price is also floating.

**Risk-sharing logic:** put the risk with the party who can manage it cheapest (the one with a natural offset, scale or hedging access). Game-theoretic view of long-term contracts is in [[137 Supply Chain Contracts & Game Theory]].

### Example
Aluminium castings: floating price expected ₹220/kg with a standard deviation of ₹18; fixed 12-month price quoted ₹228/kg. The ₹8/kg difference is the **risk premium** (3.6%). On 3,000 tonnes (30 lakh kg) a year, the premium is ₹2.4 crore. Is it worth it? If the buyer cannot pass on a ₹18 move (≈ ₹5.4 crore, 1 sd on 30 lakh kg) and a 95% adverse move is ₹29.6 per kg × 30 lakh = ₹8.9 crore, paying ₹2.4 crore for certainty is justified when margins are thin; if customer contracts already index aluminium, floating is cheaper and equally safe.

### In the news
See news box. Where raw materials are about two-thirds of costs (JK Tyre), the question "fixed or floating?" is a margin decision, not a procurement preference.

### Interview angle
> [!question] How it is asked
> "A supplier offers a fixed price for 12 months at 4% above current index. Take it?"

> [!tip] Strong answer includes
> - Compare premium with expected volatility cost and ability to pass through
> - Consider supplier's credit strength (can it honour a fixed price in a spike?)
> - Hybrid structures and shorter fixed windows
> - Scenario table: price up, flat, down

---
## 9. Forward Buying, Strategic Stock and Timing Purchases
> 🟠 Tier 2 · _Key points:_ Buy ahead of expected price rise; holding cost threshold; strategic reserves

### Definition
**Forward buying** is purchasing more than current needs to lock a low price, funded by holding cost (capital, storage, shrinkage, obsolescence ~15-30% a year, as in [[003 Inventory Management]]). It is a **physical hedge**. Rule of thumb: forward buy only if **expected price rise > holding cost for the period** (plus a margin of safety), and storage capacity, shelf life and cash are available. **Strategic stock** is held for supply disruption rather than price (see [[015 Supply Chain Risk & Resilience]]). Both interact with EOQ logic ([[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems|EPQ and discounts]]), working capital ([[136 Supply Chain Finance & Working Capital]]) and the buyer's view of price cycles. Risks: price falls after buying; speculative stock is not a hedge if price direction is guessed.

### Example
Rubber at ₹190/kg; the buyer expects ₹205/kg in two months and holds stock at 18% a year. Holding cost for 2 months = 190 × 0.18 × 2/12 = **₹5.70/kg (3.0%)**, so the break-even price rise is 3.0%. Expected rise = 15/190 = 7.9%, net benefit = 205 − 190 − 5.7 = **₹9.30/kg**. On 500 tonnes: ₹46.5 lakh, with cash tied up of 190 × 5,00,000 = ₹9.5 crore for two months. If the price instead falls to ₹180: loss = (190 − 180) + 5.7 = ₹15.7/kg, ₹78.5 lakh. So size the forward buy by risk appetite, not only by expected value.

### In the news
See news box. The 12.5% price rise and 18-20% basket increase flagged by JK Tyre show the payoff to anyone who bought ahead, and TSR20's 168 to 263 range shows how costly the opposite error can be.

### Interview angle
> [!question] How it is asked
> "Prices are expected to rise 8% next quarter. Should we build 3 months of stock?"

> [!tip] Strong answer includes
> - Compare expected rise to holding cost; consider downside scenario
> - Cash, storage and shelf-life constraints
> - Alternatives: hedge with futures, fix-price contract, partial buy
> - Distinguish speculation from policy-based cover

---
## 10. Dual Sourcing, Substitution and Supply-Side Risk
> 🟠 Tier 2 · _Key points:_ Price risk vs availability risk; split awards; spec flexibility

### Definition
Price risk is only part of commodity risk; **availability** (export bans, plantation disease, smelter outage, shipping disruption) matters as much. Non-financial tools: **dual or multi-sourcing** (e.g. 70/30 split to keep competitive tension and a qualified backup), **geographic diversification**, **material substitution** (synthetic vs natural rubber blends, aluminium vs steel in lightweighting, recycled content), **spec flexibility** (approved alternate grades), **design changes** (thrifting copper content), **recycling and reclaim**, **long-term supply agreements** with volume commitments, and **vertical or captive supply** (plantation or recycling stakes). Costs: duplicated qualification (PPAP, audits; see [[121 Supplier Quality & Automotive Core Tools (APQP, PPAP, 8D)]]), lower volume leverage, complexity. Detailed supply-risk strategies are in [[002 Procurement & Strategic Sourcing|the multi-sourcing section]] of the procurement note.

### Example
Annual rubber demand 6,000 tonnes at ₹190/kg (₹114 crore). Single sourcing earns a 2% volume discount, ₹2.28 crore. With a 70/30 split only the 70% share earns it (0.7 × 2% = 1.4%, ₹1.60 crore), so the leverage cost is ₹2.28 − 1.60 = **₹0.68 crore a year**. Disruption side (illustrative): a 10% annual chance of a 4-week outage at the single source, with line stoppage costing ₹3 crore a week, gives an expected loss of 0.10 × 12 = **₹1.2 crore**. If the qualified backup can scale up to cover the full need after one week, the outage costs 1 week (₹3 crore) and the expected loss falls to ₹0.3 crore: a saving of ₹0.9 crore against a ₹0.68 crore premium, so the split is marginally worth it. The exercise is to compare **premium vs expected loss**, with honest assumptions on ramp-up time.

### In the news
See news box. Crude-linked inputs (synthetic rubber, carbon black) and natural rubber move differently, which is why tyre formulations and sourcing use both.

### Interview angle
> [!question] How it is asked
> "Is dual sourcing worth the extra cost for a commodity input?"

> [!tip] Strong answer includes
> - Compare premium with expected disruption cost
> - Split ratios, qualification cost, switching time
> - Substitution and spec flexibility as cheaper tools
> - Combine with inventory and contract terms

---
## 11. Tyre Industry Case: Rubber and Crude Basket
> 🟠 Tier 2 · _Key points:_ Natural vs synthetic rubber, carbon black, cord; price pass-through lags; CEAT-type analysis

### Definition
A tyre's raw-material basket: **natural rubber** (a large share by weight for truck tyres; passenger tyres use more synthetic), **synthetic rubber** (SBR, BR; butadiene and styrene from crude derivatives), **carbon black** (made from carbon-black feedstock oil), **steel cord and bead wire**, **textile cord** (nylon, polyester) and **chemicals**. Much of the basket is **crude-linked** and **USD-priced** (imports of natural rubber, synthetic rubber, carbon black and cord), so rupee depreciation hits costs. Pricing: OEM contracts reset slowly with escalation clauses; **replacement-market** price increases are announced by manufacturers and lag cost increases by 1-3 months; exports reprice quickly. Hence margins squeeze when inputs rise fast and expand when they fall. Tools: **inventory timing**, **import sourcing mix**, **partial hedging** of USD (forwards) and, where possible, commodity, **formulation changes** and **price/mix actions**. (CEAT's specialty tyre business with CAMSO adds off-highway exposure; see [[142 Company Supply Chain Case Library]].)

### Example
Quarterly raw-material spend ₹1,000 crore: natural rubber 30%, synthetic rubber 20%, carbon black 15%, cords 20%, chemicals and others 15%. Scenario: natural rubber +15%, synthetic and carbon black +10% each (crude), cord +3%, others flat. Increase = 300×0.15 + 200×0.10 + 150×0.10 + 200×0.03 = 45 + 20 + 15 + 6 = **₹86 crore (+8.6%)**. If rupee depreciation adds 3% to USD-linked 70% of the basket: 0.03 × 0.70 × 1,086 ≈ ₹22.8 crore extra. Total hit ≈ ₹108.8 crore a quarter. Against sales of ₹3,000 crore, that is 3.6% of sales; with a price increase of 4% recovering 0.04 × 3,000 = ₹120 crore **after** a lag of one to two months, the first month's gap is unrecovered (≈ ₹36 crore at one month's lag).

### In the news
See news box. JK Tyre's comments on a remaining 8-9% price gap, and its claim that raw materials are about 67% of costs, are the real-world version of this exercise.

### Interview angle
> [!question] How it is asked
> "A tyre maker's EBITDA margin fell 400 bps. Natural rubber and crude are both up. Diagnose and recommend."

> [!tip] Strong answer includes
> - Cost-structure maths and basket decomposition, including FX
> - Price-pass-through lag and market structure (OEM vs replacement vs exports)
> - Levers: pricing, mix, hedging (FX and commodity), sourcing, design-to-cost
> - Link to [[160 Case Interview - Cost Reduction, Turnaround & Pricing]]

---
## 12. India Specifics: MCX, LME Parity, SEBI and RBI
> 🟠 Tier 2 · _Key points:_ Domestic price = import parity; MCX contracts; SEBI oversight; hedging abroad

### Definition
**Market structure.** **MCX** (Multi Commodity Exchange, set up in 2003, listed 2012) trades energy (crude oil, natural gas), base metals and bullion futures and some agri contracts; **NCDEX** focuses on agri. Commodity derivatives have been regulated by **SEBI since September 2015**, when the Forward Markets Commission merged into it. SEBI has at times suspended derivatives in specified agricultural commodities (check the current list and dates directly from SEBI circulars; this changes). India does not have a deep, liquid domestic futures market for every input: **natural rubber** hedging is largely referenced to overseas contracts (SGX, Osaka, Shanghai) and **steel** relies on published indices and contract formulas, so basis and FX risk are bigger.

**Domestic vs international price.** For imported metals the domestic price tracks **import parity**:

$$P_{India} \approx \big(P_{LME} \times \text{USD/INR}\big) \times (1 + \text{duty}) + \text{premium, freight, insurance, local charges}$$

so MCX or domestic prices follow **LME and the rupee**; a weaker rupee raises domestic prices even if LME is flat. Duty and safeguard measures change the parity.

**Overseas hedging.** Indian companies hedge on overseas exchanges or OTC under RBI's foreign-exchange regulations (FEMA), board-approved policy and reporting rules. Rules have been liberalised over time but remain conditional (check the current RBI master direction before advising a client).

### Example
Illustrative import parity for copper: LME at $10,000 per tonne and USD/INR at 88 give ₹8,80,000 per tonne. With a 2.5% customs duty assumed for illustration, parity = 8,80,000 × 1.025 = **₹9,02,000 per tonne**, before premiums, freight and local charges. If the rupee weakens by 2% to 89.76 with LME unchanged, the base converts to ₹8,97,600 and parity to ₹9,20,040 (**+₹18,040 per tonne**, +2%). A buyer with a USD hedge sees the rupee move offset; a buyer without it absorbs it.

### In the news
See news box. MCX's SEBI oversight since 2015 and LME's HKEX ownership frame where Indian industrial buyers actually find benchmark prices; JK Tyre cited currency weakness as a driver of its raw-material increase.

### Interview angle
> [!question] How it is asked
> "Why did domestic copper or aluminium prices rise when LME was flat?"

> [!tip] Strong answer includes
> - Import-parity formula: LME x FX x (1 + duty) + premium
> - Roles of MCX, LME, SEBI (domestic) and RBI/FEMA (overseas hedging)
> - FX hedging as a separate decision
> - Check duty, safeguard and regulatory changes before quoting numbers

---
## 13. ⭐ Advanced: Cost-at-Risk and a Portfolio View of Commodity Exposure
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Cost-at-Risk (CaR)** or **Earnings-at-Risk** estimates how much extra cost the exposure portfolio could suffer at a given confidence level over a horizon:

$$\sigma_P = \sqrt{\mathbf{e}^{\top}\Sigma\,\mathbf{e}}, \qquad CaR_{95\%} = 1.645\,\sigma_P$$

$\mathbf{e}$ = vector of ₹ exposures, $\Sigma$ = covariance matrix of price returns (volatilities and correlations). Diversification across commodities lowers $\sigma_P$ below the simple sum; hedging reduces exposures in $\mathbf{e}$. Limits: assumes normal returns and stable correlation; correlations rise in crises. Complement with **scenario and stress tests** (crude +30%, rupee −8%, rubber +40%). Used for hedging policy, budget contingency, and board risk appetite.

### Example
Annual exposures: natural rubber ₹400 crore (volatility 25%), crude-linked inputs ₹250 crore (30%), steel ₹150 crore (20%). Correlations: rubber-crude 0.5, rubber-steel 0.3, crude-steel 0.4. Portfolio standard deviation = **₹166.2 crore**; 95% CaR = 1.645 × 166.2 = **₹273.4 crore** (the undiversified sum is 1.645 × (100 + 75 + 30) = ₹337.2 crore, so diversification saves ₹63.8 crore). Hedge half the rubber and crude exposures (exposures become 200, 125, 150): $\sigma_P$ = ₹92.1 crore and 95% CaR = **₹151.5 crore**, a **45% reduction** (₹121.9 crore lower). Compare with hedge cost and margin-call liquidity, and set the cover ratio so CaR stays inside the board's risk appetite (for example, no more than 3% of EBITDA).

### In the news
See news box. Simultaneous moves in rubber (+44% a year), crude (+14% in September) and the rupee are what cost-at-risk models try to capture, and why correlation assumptions deserve a stress test.

### Interview angle
> [!question] How it is asked
> "How would you quantify the commodity risk of a multi-commodity manufacturer for the board?"

> [!tip] Strong answer includes
> - Exposure vector, volatilities, correlations and confidence level
> - Diversification effect and hedging impact on CaR
> - Limitations: fat tails, correlation breakdown; add stress scenarios
> - Tie to risk appetite and hedge-policy limits; see also [[090 Regression Analysis|regression methods]] for estimating hedge ratios
