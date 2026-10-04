---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "FMCG & Retail Distribution - India Route-to-Market"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# FMCG & Retail Distribution - India Route-to-Market

⬅ [[129 E-commerce & Quick-Commerce Fulfilment]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[131 Automotive Supply Chain - JIT, Tiers & EVs]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. India's FMCG Distribution Structure]]
2. [[#2. C&F Agents, Super Stockists and Distributors: Roles and Economics]]
3. [[#3. Primary, Secondary and Tertiary Sales; Sell-In vs Sell-Out]]
4. [[#4. Distributor ROI and Working Capital: Worked P&L]]
5. [[#5. Distributor Management Systems (DMS), SFA and Retailer Apps]]
6. [[#6. Trade Promotions and Trade Terms]]
7. [[#7. Modern Trade and Key-Account Supply Chain]]
8. [[#8. E-commerce, Quick Commerce and Channel Conflict]]
9. [[#9. Retail Replenishment: Store-Level Min-Max, Assortment and Planograms]]
10. [[#10. Direct Store Delivery (DSD) and Fresh/Perishable Distribution]]
11. [[#11. Category Supply Chains: Staples, Personal Care, Foods and Beverages]]
12. [[#12. Forward Integration: Direct Reach, Shakti and D2C]]
13. [[#13. Rural Reach and Cost-to-Serve]]
14. [[#14. ⭐ Advanced: Redesigning Route-to-Market, a Consulting Case]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): GST 2.0, rural-led demand and quick commerce reshape route-to-market
> **GST rate overhaul effective 22 Sep 2025.** Following a 3 Sep 2025 announcement, India moved from six to four slabs: **0%, 5%, 18% and 40%**, eliminating the 12% and 28% slabs. For FMCG, a rate change on live stock means re-pricing, relabelling and claim processing across the C&F-distributor-retailer chain (the operational consequence is an inference; the slab change itself is as stated by the source). The same source reports an estimated net revenue loss of about ₹480 billion and an expected direct consumption boost of about ₹700 billion (government/estimate figures). ([Wikipedia: GST India](https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)))
>
> **Rural India and quick commerce, as reported by IBEF.** IBEF's FMCG page says that rural India overtook cities in affordable-premium FMCG consumption, with **51% of volume share in 2025 (a ₹98,000 crore market)**; Dabur is cited as deriving **45-50% of revenue from rural markets across about 1,31,000 villages**; **rural was 38% of 2024 FMCG sales**; and quick commerce accounts for **70-75% of e-grocery orders**, up from 35% in 2022, with FMCG companies reporting 50-100% sales growth on that channel in FY25. ([IBEF](https://www.ibef.org/industry/fmcg))
>
> **Organised retail is still a minority.** IBEF's retail page puts India's retail market at **₹81.58 lakh crore (US$952 billion) in 2024**, of which **organised retail is ₹11.31 lakh crore (about 14%)**, projected to reach ₹19.71 lakh crore by 2030. ([IBEF Retail](https://www.ibef.org/industry/retail-india))
>
> Sub-topics that say **"See news box"** reuse these items. Market-size figures are third-party estimates; confirm before quoting.

---
## 1. India's FMCG Distribution Structure
> 🔴 Tier 1 · _Key points:_ Company, C&F, super stockist, distributor, wholesaler, kirana

### Definition
Indian FMCG companies reach millions of small outlets through a **multi-tier general-trade chain**:

**Manufacturer → Carrying & Forwarding (C&F) agent / depot → (Super stockist) → Distributor → (Sub-distributor / wholesaler) → Retailer (kirana, chemist, paan shop) → Consumer**

- **Factory/Central warehouse** feeds regional depots by full-truck loads.
- **C&F agent:** operates the company's depot on a service fee; holds the company's stock on consignment (no ownership), handles inbound, storage, and dispatch to distributors, and bills on the company's behalf.
- **Super stockist (SS):** buys stock and supplies many distributors in a region; offers credit to them and reduces the company's number of billing points.
- **Distributor/stockist:** an independent trader who buys from the company or SS, holds stock, employs salesmen and delivery vans, extends credit to retailers, and earns a margin and scheme income; usually has an exclusive territory or beat plan.
- **Wholesaler/sub-stockist:** serves the smaller outlets or a rural cluster.
- **Retailer:** over-the-counter kirana and specialty outlets (chemists, cosmetics, paan); the unit that actually serves the consumer. Widely cited estimates put the number of kirana stores at roughly 12-13 million (industry estimates; verify with the latest NielsenIQ or other studies).

The structure persists because small outlets need **small orders, credit, frequent visits and last-metre delivery**, which the intermediaries finance. Each tier adds a margin, so the company's price ladder (ex-factory, distributor price, retailer price, MRP) has to fit.

### Example
Illustrative price ladder for a ₹100 MRP soap (assumed margins, not company data, and ignoring the GST component inside MRP): the retailer takes 15%, so the retailer buys at ₹85.0; the wholesaler takes 4%, so the wholesaler buys at ₹81.6; the distributor takes 5%, so the distributor buys from the company at ₹77.5. The channel therefore absorbs about **₹22.5 of every ₹100 MRP** (₹15.0 retailer, ₹3.4 wholesaler, ₹4.1 distributor) before the company's own discounts and taxes.

```python
mrp = 100
retailer_buy = mrp*(1-0.15)
wholesaler_buy = retailer_buy*(1-0.04)
distributor_buy = wholesaler_buy*(1-0.05)
print(retailer_buy, round(wholesaler_buy,1), round(distributor_buy,1))   # 85.0 81.6 77.5
```

### In the news
See news box. Organised retail is about 14% of the ₹81.58 lakh crore market (IBEF), so general trade through distributors remains the volume channel for most FMCG firms, even as quick commerce grows.

### Interview angle
> [!question] How it is asked
> "Walk me through how a bar of soap gets from a Pune factory to a village kirana. Where would you cut cost?"

> [!tip] Strong answer includes
> - The tier chain and the role of each tier (C&F as service, distributor as trader with credit)
> - Where cost and delay accumulate: handling, credit, small drops, returns and claims
> - Options: consolidate tiers, DMS, direct reach, wholesale hubs, rural redistribution
> - A numeric price ladder to show channel margin

---
## 2. C&F Agents, Super Stockists and Distributors: Roles and Economics
> 🔴 Tier 1 · _Key points:_ Consignment vs trading, margin structure, credit, territory

### Definition
| Role | Ownership of stock | Revenue model | Risk | Typical coverage |
|---|---|---|---|---|
| **C&F agent** | None (consignment) | Fixed fee per case or commission | Low: operational (shrinkage, accuracy) | State/region depot |
| **Super stockist** | Owns stock | Margin (low, often 1-3%) | Credit and inventory | Many distributors |
| **Distributor** | Owns stock | Margin (higher, often 3-8% depending on category) plus schemes | Credit to retailers, expiry, claim leakage | A town or a beat of outlets |
| **Wholesaler** | Owns stock | Trade margin | Credit, price volatility | Small outlets, rural |

Margins vary by company and category (indicative). The distributor's economics depend on **margin on sales, annual turnover, working capital days, cost of delivery and sales force, and scheme claim leakage** (see sub-topic 4). The company's choice of tiers is a trade-off: more tiers give reach with less capital; fewer tiers give better control, fresher stock and lower channel cost. Companies also run **modern trade, e-commerce and institutional (canteen, CSD) channels** directly or through specialised distributors.

Common problems: **overlapping territories**, **stock-outs at the retailer despite stock at the distributor**, **expiry and near-expiry stock**, **claim delays**, **price parity breaches**, **slow-moving SKUs ignored** by the distributor's salesmen, and **distributor ROI too low to reinvest**.

### Example
A company sells ₹600 crore a year through 200 distributors (average ₹3 crore each, ₹25 lakh a month). An analysis shows 60 distributors below the ROI hurdle because their sales average only ₹20 lakh a month. The sales head considers merging them into 30 distributors at about ₹40 lakh a month each. Billing points fall from 200 to 170 and each remaining distributor's cost-to-serve per rupee falls, but the decision depends on whether the merged distributors can still **cover every retailer** that the 60 served; a coverage gap costs more than the ROI gain.

### In the news
See news box. With rural at 51% of volume in affordable-premium FMCG (IBEF) and Dabur reaching about 1.31 lakh villages, companies need distribution models that reach small markets economically, not only large towns.

### Interview angle
> [!question] How it is asked
> "A distributor with ₹30 lakh monthly sales wants a higher margin. How do you decide?"

> [!tip] Strong answer includes
> - Computes distributor ROI and compares to a hurdle rate
> - Separates margin from working-capital terms and claim speed (often a bigger lever)
> - Considers coverage and service obligations in return
> - Considers consolidation, sub-distributors or DMS-based monitoring

---
## 3. Primary, Secondary and Tertiary Sales; Sell-In vs Sell-Out
> 🔴 Tier 1 · _Key points:_ Primary = company to distributor; secondary = distributor to retailer; tertiary = retailer to consumer

### Definition
- **Primary sales:** company invoices to its distributors/C&F; this is what the company books as revenue.
- **Secondary sales:** distributor invoices to retailers; shows channel offtake.
- **Tertiary sales:** retailer to consumer (measured by retail audit or POS data).
- **Sell-in vs sell-out:** sell-in is primary; sell-out is secondary or tertiary.

If primary exceeds secondary for a period, **channel inventory has increased**. Persistent gaps indicate **channel stuffing** (pushing stock to meet targets), which causes expiry, discounting and weak distributor ROI, and later a primary-sales cliff. Monitor **distributor inventory days** (stock / average daily secondary sales), **secondary-to-primary ratio**, **fill rate**, and **stock ageing**.

$$\text{Distributor days of stock} = \frac{\text{Closing stock at cost}}{\text{Average daily secondary sales at cost}}$$

### Example
In a quarter, primary sales are ₹100 crore and secondary sales ₹82 crore, so the channel has absorbed ₹18 crore of extra stock. That equals about 18/82 x 90 = **19.8 additional days** of stock at distributors. If their normal level is 15 days, they are now at about 35 days, with expiry risk on short-life SKUs. The company may be forced to cut next quarter's primary sales, taking a hit to reported growth, or to fund returns and discounts.

### In the news
See news box. GST rate changes make channel-inventory visibility more valuable: when rates change, stock at old tax rates and old MRPs must be tracked and claimed correctly, which needs secondary-sales and stock data.

### Interview angle
> [!question] How it is asked
> "A company reports 10% primary growth but secondary sales are flat. What do you worry about and what do you do?"

> [!tip] Strong answer includes
> - Channel inventory build and days of stock at the distributor
> - Why it matters: expiry, ROI, discounting, next-quarter primary cliff
> - Data sources: DMS, retail audits, e-B2B orders
> - Actions: align targets to secondary or sell-out, cap distributor days, align incentives

---
## 4. Distributor ROI and Working Capital: Worked P&L
> 🔴 Tier 1 · _Key points:_ Margin, opex, inventory days, receivable days, ROCE, break-even margin

### Definition
A distributor's return depends on **gross margin**, **operating cost to serve**, and **capital tied in stock and receivables**.

$$\text{Capital employed} = \text{Inventory} + \text{Receivables} + \text{Fixed assets} - \text{Payables}$$

$$\text{ROCE} = \frac{\text{Annual EBITDA}}{\text{Capital employed}},\qquad \text{Inventory} = \text{COGS}\times\frac{\text{Days}}{30}$$

(See [[136 Supply Chain Finance & Working Capital]] for cash-conversion logic and [[108 Financial Statements & Ratios]] for ratios.)

### Example
Monthly secondary sales ₹100 lakh (illustrative distributor, assumed data):

| Item | ₹ lakh per month |
|---|---|
| Gross margin (6.0% of sales) | 6.00 |
| Scheme and incentive income retained | 0.80 |
| **Income** | **6.80** |
| Salesmen (5 x ₹0.20 lakh) | 1.00 |
| Delivery vans and drivers | 1.70 |
| Godown rent and utilities | 0.70 |
| Office, accounts, DMS | 0.70 |
| Expiry, damage and claim leakage | 0.50 |
| Other | 0.30 |
| **Operating cost** | **4.90** |
| **EBITDA** | **1.90 (1.9% of sales)** |

Working capital: inventory 10 days at cost (COGS ₹94 lakh) = ₹31.3 lakh; receivables 20 days = ₹66.7 lakh; payables 4 days = ₹12.5 lakh; fixed assets ₹14 lakh. **Capital employed = ₹99.5 lakh**. Annual EBITDA = 1.9 x 12 = ₹22.8 lakh, so **ROCE = 22.9%**. Interest at 11.5% on 60% debt = ₹0.57 lakh a month, depreciation ₹0.18 lakh, so profit before tax = ₹1.15 lakh a month (₹13.8 lakh a year) and return on the owner's 40% equity of ₹39.8 lakh is about 35%.

Sensitivity:
- **Margin 5.0%:** EBITDA ₹0.9 lakh a month, ROCE **10.8%**, PBT ₹1.8 lakh a year; the distributor's break-even margin is about **4.9%**.
- **Receivable days 32:** capital rises to ₹139.5 lakh, ROCE falls to **16.3%**.
- **Inventory days 15:** capital ₹115.1 lakh, ROCE **19.8%**.

A distributor's life is a **thin-margin, working-capital game**: a one-point fall in margin or a 12-day rise in receivables can erase much of the return, which explains pressure for price parity with quick commerce and demand for faster claim settlement.

### In the news
See news box. With quick commerce growing 70-75% of e-grocery orders (IBEF), distributors fear loss of volume and margin parity; the company must protect distributor ROI to keep rural and small-town reach.

### Interview angle
> [!question] How it is asked
> "Distributors are threatening to stop lifting stock because margins are 'too low'. Evaluate."

> [!tip] Strong answer includes
> - Builds the distributor P&L and ROCE from margin, cost to serve and working capital
> - Identifies levers: margin, credit days, claim settlement, DMS and delivery productivity
> - Quantifies the break-even margin and the risk to coverage
> - Balances company economics with channel health

---
## 5. Distributor Management Systems (DMS), SFA and Retailer Apps
> 🔴 Tier 1 · _Key points:_ DMS, sales force automation, secondary visibility, e-B2B ordering

### Definition
- **DMS (Distributor Management System):** software at the distributor for orders, invoicing, stock, schemes, claims, GST and credit control, connected to the company's ERP or data lake. It gives the company **secondary sales, closing stock, ageing and outlet-level data** without waiting for audits.
- **SFA (Sales Force Automation):** mobile app for salesmen with beat plans, outlet visit logging, order capture, photo audit and scheme display.
- **Retailer ordering apps (e-B2B):** apps through which retailers order directly (the company's own app or marketplaces such as Udaan or Jumbotail), usually fulfilled by distributors or hubs.
- **Integration:** DMS ↔ company ERP ([[013 ERP & Enterprise Systems (SAP-Oracle)]], [[082 SAP SD — Sales & Distribution]]) ↔ trade promotion management ↔ analytics.

Benefits: **faster claim validation**, lower claim leakage, accurate **days of stock**, **fill rate**, **productive-call %**, **lines per call**, and the ability to give **suggested orders** based on outlet history. Barriers: distributor reluctance, data quality, connectivity in rural areas, and cost.

### Example
A company pays ₹120 crore of scheme claims a year. Manual validation leaks 1.5% (₹1.8 crore) through duplicate and invalid claims; DMS-based auto-validation cuts leakage to 0.5%, saving ₹1.2 crore a year. If the DMS costs ₹1,000 per distributor per month for 1,000 distributors = ₹1.2 crore a year, the claims saving alone just pays for the system; the further gains in forecasting, stock visibility and distributor ROI make the case.

### In the news
See news box. The GST changes in Sep 2025 are an example where DMS data on stock at old rates and MRPs lets companies compute credit-note and relabelling claims faster.

### Interview angle
> [!question] How it is asked
> "How would you convince 1,000 distributors to adopt a DMS?"

> [!tip] Strong answer includes
> - Benefits for the distributor (faster claims, less paperwork, working-capital visibility)
> - Incentives, simple UX, training and a phased rollout
> - Data standards and integration with ERP
> - Measuring adoption and impact: claim cycle, stock days, fill rate

---
## 6. Trade Promotions and Trade Terms
> 🔴 Tier 1 · _Key points:_ Schemes, on-invoice vs off-invoice, lift, pull-forward, promo ROI

### Definition
**Trade promotions** are incentives to the trade (distributors, wholesalers, retailers) to buy, stock, display or push products: **price-off/on-invoice discounts, volume-slab schemes, buy-X-get-Y, display and visibility payments, listing fees, cash discounts and retailer loyalty programmes**. Consumer promotions (price packs, coupons) work alongside. Trade spend is typically a large share of a company's gross-to-net waterfall (indicative range varies by company).

Evaluate promotion on **incremental profit**, not volume:

$$\text{Promo profit} = \text{Promo units}\times\text{Unit margin after discount} - \text{Baseline units}\times\text{Baseline unit margin} - \text{Post-promotion dip loss}$$

Effects to account for: **lift**, **pull-forward (forward buying)** and post-promo dip, **cannibalisation** of other SKUs, and **channel stocking** that is not sold through.

### Example
Baseline 10,000 units a week; price ₹100; unit margin 35%. A 3-week, **10% discount** promotion: price ₹90, unit margin after discount = ₹25 (cost ₹65). Baseline contribution over 3 weeks = 30,000 x ₹35 = **₹10.5 lakh**. A lift of 40% gives 42,000 units x ₹25 = ₹10.5 lakh; a two-week post-promo dip of 15% costs 10,000 x 0.15 x 2 x ₹35 = **₹1.05 lakh**. Net = 10.5 − 10.5 − 1.05 = **−₹1.05 lakh (loss)**. The **break-even lift** is (10.5 + 1.05) / 7.5 − 1 = **54%**; at 60% lift (48,000 units x ₹25 = ₹12.0 lakh) the promotion earns +₹0.45 lakh. A **20% discount** needs a lift of about 157% to break even, so deep discounts are rarely profitable unless they win new customers or shelf space.

### In the news
See news box. Faster quick-commerce growth (50-100% FMCG sales growth reported on that channel in FY25 per IBEF) means brands must set promotion rules by channel to avoid price conflicts with general trade.

### Interview angle
> [!question] How it is asked
> "A brand manager proposes a 20% price-off for a festival promotion. How would you evaluate it?"

> [!tip] Strong answer includes
> - Incremental-profit formula, break-even lift and post-promo dip
> - Pull-forward, cannibalisation and channel stocking
> - Alternatives: bundle, loyalty, display payments, smaller discount
> - Supply readiness: stock, fill rate and distribution coverage during the promo

---
## 7. Modern Trade and Key-Account Supply Chain
> 🔴 Tier 1 · _Key points:_ Retail DCs, fill rate, OTIF fines, listing, trade terms

### Definition
**Modern trade (MT)** includes hypermarkets, supermarkets and chains (for example D-Mart, Reliance Retail and regional chains) and uses **retailer DCs** and centralised procurement. Key-account supply chain features: **direct billing to the chain**, **delivery to retailer DCs or stores**, **EDI/portal orders and ASN**, **OTIF (on-time in-full) targets with penalties**, **appointment windows**, **fill-rate and shelf-availability metrics**, **trade terms (margin, listing fees, display allowances, return rights)** and **payment terms** (30-45 days or more). MT demands **barcode/GS1 compliance**, accurate master data ([[175 Data Quality, Master Data & Data Governance]]) and **promotions planned jointly**.

Company vs distributor-served: some chains are served directly by the company (large format), others through MT-specialised distributors. The supply-chain challenge is service level (OTIF 95%+ is common) with lower margins and longer credit.

### Example
A retailer's DC demands 98% OTIF and fines 2% of invoice value on a short-shipped line. The company's OTIF is 94% because 6% of lines are short (stock-outs and late truck arrival). On monthly sales of ₹5 crore to this account, if half of the 6% failures carry a fine at 2% of the affected value: fines ≈ ₹5 crore x 6% x 50% x 2% = **₹30,000 a month**, small relative to the lost sales on stock-outs; a lost sale of the same lines at 25% margin costs ₹5 crore x 6% x 25% = **₹7.5 lakh** in margin. The cost of service failure is therefore mostly lost sales, not fines.

### In the news
See news box. Organised retail is about 14% of retail by value (IBEF) but growing, so MT service standards increasingly shape the whole supply chain's performance targets.

### Interview angle
> [!question] How it is asked
> "Your OTIF with a large retailer is 91% against a target of 97%. How do you diagnose and fix it?"

> [!tip] Strong answer includes
> - Splits OTIF failures: on-time vs in-full, root causes (stock, picking, transport, paperwork)
> - Plans: safety stock for the account, appointment slots, ASN accuracy, packaging standards
> - Quantifies lost sales, penalty and relationship cost
> - Aligns planning with the retailer's promotion calendar

---
## 8. E-commerce, Quick Commerce and Channel Conflict
> 🔴 Tier 1 · _Key points:_ Channel strategy, price parity, assortment, pack-size, distributor impact

### Definition
Channels beyond general trade: **e-commerce marketplaces**, **quick commerce**, **B2B e-commerce (kirana ordering)** and **D2C**. For FMCG, the issues are: **price parity** (online discounts versus kirana prices), **assortment and pack-size** (online-exclusive packs, larger packs), **service level (fill rate) and lead time to dark stores**, **trade margin and ad spend** on platforms, **conflict with distributors** (platform volume bypasses them or is served by dedicated distributors) and **data ownership**. Companies respond with **channel-specific SKUs and price corridors**, **dedicated e-commerce distribution teams or hubs**, and **margin structures that keep traditional distributors viable**. See [[129 E-commerce & Quick-Commerce Fulfilment]] and [[036 Go-To-Market Strategy]].

Share of channels is changing fast: IBEF reports that quick commerce is 70-75% of e-grocery orders and that FMCG companies saw 50-100% sales growth on the channel in FY25 (see news box). General trade is still much larger in volume.

### Example
A beauty brand sells ₹100 crore a year, 70% general trade, 15% marketplace, 15% quick commerce. Gross margins to the brand: GT 38% after distributor margin, marketplace 30% (after commission and ads), Q-commerce 33%. Blended = 0.7 x 38 + 0.15 x 30 + 0.15 x 33 = **26.6 + 4.5 + 4.95 = 36.05%**. If quick commerce grows to 30% at the expense of GT (GT 55%): 0.55 x 38 + 0.15 x 30 + 0.30 x 33 = 20.9 + 4.5 + 9.9 = **35.3%**, a fall of 0.75 points or ₹0.75 crore on the same sales, plus a shift in working capital (Q-commerce pays faster, GT carries distributor credit). The mix shift is therefore a mild margin concern but a bigger supply-chain complexity issue.

### In the news
See news box. The same IBEF data show channel growth rates far apart, which is why supply-chain planners must plan GT, MT and Q-commerce supply separately, with different SLAs and pack configurations.

### Interview angle
> [!question] How it is asked
> "Quick commerce is 25% of a brand's sales and distributors are upset. What do you do?"

> [!tip] Strong answer includes
> - Maps channel economics (margin, working capital, service) and conflict points
> - Price corridor, channel SKUs, protect distributors with fair margin or role in serving the channel
> - Supply planning by channel and a mother-hub strategy
> - Data sharing and promotion governance

---
## 9. Retail Replenishment: Store-Level Min-Max, Assortment and Planograms
> 🔴 Tier 1 · _Key points:_ Min-max, review period, planogram, assortment, GMROI

### Definition
For modern retail and chain stores, **replenishment** uses a **min-max (reorder point, order-up-to)** policy per SKU per store, driven by forecast and lead time:

$$\text{Max} = d(R+L) + z\sigma_d\sqrt{R+L},\qquad \text{Min (reorder point)} = dL + z\sigma_d\sqrt{L}$$

where $d$ is mean daily demand, $\sigma_d$ its standard deviation, $R$ review period and $L$ lead time (days); see [[003 Inventory Management]] and [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]. **Planograms** (shelf layouts by SKU, facings and position) turn space into sales: facings should match expected sales and pack size, and **the minimum shelf quantity (presentation stock)** must be added to the formula. **Assortment** decisions rank SKUs by sales, margin and substitutability; low-productivity SKUs are cut and space is reallocated. Productivity is measured by **GMROI** and sales per square foot:

$$\text{GMROI} = \frac{\text{Gross margin}}{\text{Average inventory at cost}}$$

### Example
A store sells a shampoo at 6 units a day (standard deviation 2); a daily review (R = 1 day) and a 2-day lead time. Max = 6 x 3 + 1.65 x 2 x $\sqrt{3}$ = 18 + 5.7 = **23.7, so 24 units**; Min = 6 x 2 + 1.65 x 2 x $\sqrt{2}$ = 12 + 4.7 = **16.7, so 17 units**. When stock plus on-order falls to 17 the system orders up to 24. For the category: sales ₹1.2 crore a year at 22% gross margin on average inventory at cost of ₹15 lakh gives **GMROI = 0.22 x 1.2 crore / 15 lakh = 1.76** (each ₹1 invested in inventory returns ₹1.76 of gross margin a year). Cutting the slowest 10% of SKUs (which carry 15% of inventory and 3% of sales) lifts GMROI.

### In the news
See news box. As organised retail and quick commerce grow, store-level replenishment shifts from weekly distributor visits to daily or twice-daily system-driven replenishment, calling for better forecasting at store-SKU level ([[004 Demand Forecasting & Planning]]).

### Interview angle
> [!question] How it is asked
> "A supermarket chain has 12% out-of-stocks on fast sellers and too much stock on slow ones. What do you change?"

> [!tip] Strong answer includes
> - Segment SKUs (ABC/XYZ) and set service levels by segment
> - Min-max with correct lead time and review period; planogram and presentation stock
> - Fix forecasts, store-level data and DC fill rate
> - Cut tail SKUs; track GMROI and availability

---
## 10. Direct Store Delivery (DSD) and Fresh/Perishable Distribution
> 🔴 Tier 1 · _Key points:_ DSD, shelf life, cold chain, route sales, returns

### Definition
**DSD** means the supplier delivers directly to the store or outlet (bypassing the retailer's DC), with the driver or salesman often handling the shelf: used for **bread, dairy, ice cream, beverages, snacks and biscuits** where shelf life is short, volumes are high or the supplier wants control of shelf and freshness. Features: **van sales or pre-sell routes**, a **handheld invoicing device**, **stock rotation**, **returns/expiry write-offs**, **route optimisation** and **cash/credit collection**. Fresh and perishable chains (milk, fruit and vegetables, meat) add **cold chain**, short lead times and high wastage. See [[133 Food, Agri & Perishables Supply Chain - India]].

Trade-offs: **DSD** gives control and freshness but has high cost per drop and complex route management; **DC-based replenishment** is cheaper per case but is less fresh and gives less control.

### Example
A beverage company delivers to 400 outlets a day with 10 vans. Cost per van per day is ₹3,200 (driver, fuel, depreciation) = ₹32,000; each outlet drop is 12 cases at ₹450 per case, so daily sales are ₹21.6 lakh. Logistics cost = 32,000 / 21.6 lakh = **1.5% of sales**; if the same outlets were served through a wholesaler with twice-a-week visits, outlet availability would be lower (out-of-stock at 8% instead of 3%), and a 5-point improvement in availability on ₹21.6 lakh x 5% = **₹1.08 lakh a day** of recovered sales offsets DSD's extra cost.

### In the news
See news box. For perishables, quick commerce changes the maths of fresh supply: dark stores increase daily frequency, so supplier DSD routes are being re-planned around dark-store receiving windows.

### Interview angle
> [!question] How it is asked
> "Should a dairy company use DSD or a distributor for its curd and paneer in a metro?"

> [!tip] Strong answer includes
> - Shelf life, cold-chain control, volumes per outlet and density
> - Cost per drop versus lost sales from stock-outs and expiry
> - Handheld, route optimisation, returns policy, and credit control
> - Hybrid option: DSD to top outlets, distributor for the long tail

---
## 11. Category Supply Chains: Staples, Personal Care, Foods and Beverages
> 🔴 Tier 1 · _Key points:_ Category characteristics, SKU proliferation, shelf-life, seasonality

### Definition
Different categories need different supply chain designs ([[112 Supply Chain Strategy - Fit, Segmentation & Maturity]]):

| Category | Characteristics | Supply chain focus |
|---|---|---|
| **Staples (atta, rice, oil, salt)** | High volume, low margin, price-sensitive, commodity-driven | Procurement and hedging ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]), bulk logistics, low cost |
| **Personal and home care** | Many SKUs, price-pack architecture, promotions, premiumisation | SKU rationalisation, forecasting, fill rate, secondary visibility |
| **Packaged foods and snacks** | Shelf life 3-12 months, seasonality, plant specialisation | FEFO, plant-to-depot, expiry control |
| **Beverages and dairy** | Short life, cold chain, high weight | DSD, returns of packaging, route design |
| **Impulse and sachet products** | Low unit value, huge outlet count | Rural reach, redistribution, small drops |

**SKU proliferation** (many variants and pack sizes) lifts inventory and complexity; link to [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]]. **Price-pack architecture** (small packs at fixed price points such as ₹5 and ₹10) is an Indian reach strategy that makes supply chain costs per unit high and requires efficient secondary packaging.

### Example
A company with ₹2,000 crore of sales and 1,200 active SKUs finds that the top 300 SKUs deliver 80% of sales and the bottom 400 only 1.5% (₹30 crore). Cutting the bottom 400 releases inventory of ₹14 crore, worth 11% = **₹1.5 crore a year** of carrying cost, plus lower changeover and expiry losses. Against that, the lost margin is ₹30 crore x 30% = ₹9 crore if no volume is recovered, or **₹2.7 crore** if substitution recovers 70% of the volume. The net is about −₹1.2 crore before changeover, expiry and complexity savings, so a rank-only cut can destroy value; the right approach is to cut SKUs that are substitutable and keep those with unique consumers or retailer-listing importance.

### In the news
See news box. The reported rural growth in affordable-premium consumption (51% of volume share in 2025, IBEF) favours small-pack and mid-priced SKUs, which changes category supply planning toward higher unit volume per rupee of sales.

### Interview angle
> [!question] How it is asked
> "How would you design the supply chain differently for staples and for a premium skincare line?"

> [!tip] Strong answer includes
> - Cost vs responsiveness, using fit logic and product characteristics
> - Inventory policy, service level, distribution channel and packaging by category
> - SKU rationalisation with substitution analysis
> - Examples of Indian category differences

---
## 12. Forward Integration: Direct Reach, Shakti and D2C
> 🔴 Tier 1 · _Key points:_ Direct distribution, rural micro-entrepreneurs, D2C, B2B apps

### Definition
**Forward integration** means the company controls more of the route to the consumer. Forms:
- **Direct distribution (direct reach):** company-run sales and delivery to retailers, bypassing sub-tiers, supported by SFA and DMS; typical for high-density outlets.
- **Rural micro-entrepreneur models:** **Hindustan Unilever's Project Shakti** (launched in 2000) recruits women from self-help groups as direct sellers in small villages, supplied from the redistribution stockist, giving the company last-mile reach where conventional distribution is uneconomical (current counts: see HUL's annual report). Other companies use similar rural salesforces or "rural sub-stockist" models.
- **Retailer ordering apps** (company apps or B2B marketplaces).
- **D2C websites and subscriptions:** direct to consumer, with the company handling fulfilment (3PL), returns and data.
- **Company-owned or franchise stores** for specific categories.

Trade-offs: **control and data** versus **fixed cost and service complexity**. Forward integration pays where outlet density, order value and repeat frequency are high.

### Example
A direct-reach programme serves 5,000 outlets in a city, each ordering ₹4,500 a week on average, and the company earns 8% more margin than through the distributor (it keeps the 5% distributor margin and 3% in avoided scheme leakage, but incurs cost). Weekly sales = 5,000 x 4,500 = ₹2.25 crore; extra margin = 8% = ₹18 lakh a week, ₹9.4 crore a year. Direct costs: 40 salesmen at ₹30,000 per month, delivery cost 2.2% of sales, credit cost 1% = (40 x 30,000 x 12 = ₹1.44 crore) + (3.2% x ₹117 crore = ₹3.74 crore) = **₹5.2 crore**, leaving a net gain of **about ₹4.2 crore a year**, if the service level and credit control are maintained. In smaller towns with lower density, the same model loses money.

### In the news
See news box. Rural volume share at 51% (IBEF) is why micro-entrepreneur and sub-stockist reach models remain important even as quick commerce grows in cities.

### Interview angle
> [!question] How it is asked
> "Should an FMCG company move to direct distribution in the top 50 cities?"

> [!tip] Strong answer includes
> - Density, order value and service economics by town class
> - Net gain compared with distributor model, including credit and delivery costs
> - Impact on distributors, coverage and rural reach
> - Pilot design, success metrics and exit rules

---
## 13. Rural Reach and Cost-to-Serve
> 🔴 Tier 1 · _Key points:_ Rural market, redistribution, small drops, cost-to-serve, hub-and-spoke

### Definition
Rural India is large by volume but costly to serve: **small order sizes, scattered outlets, poor roads, higher credit risk**. Typical designs: **hub-and-spoke with a redistribution stockist (RS) in a feeder town**, **van sales** on fixed days (rural van or "haat" models), **sub-stockists/wholesalers** and **micro-entrepreneur networks**. **Cost-to-serve** (CTS) analysis by outlet cluster combines **delivery cost per drop, salesman time per call, margin, credit cost and expiry** to decide visit frequency and which tier serves which outlet ([[138 Order Management, Customer Service & Cost-to-Serve]]). Key metrics: **numeric distribution** (share of outlets stocking the brand), **weighted distribution**, **productive calls**, **lines per call**, **cost per outlet served**.

$$\text{CTS per drop} = \frac{\text{Van and driver cost} + \text{Salesman cost} + \text{Credit and loss cost}}{\text{Drops served}}$$

### Example
A van with driver costs ₹3,000 a day (van cost only, excluding salesman time) and serves 45 rural outlets at an average ₹1,100 per drop (₹49,500 of sales). CTS per drop = 3,000 / 45 = **₹66.7**, which is 6.1% of the drop value. A town van making 70 drops of ₹1,600 has a CTS of 3,000 / 70 = **₹42.9** (2.7% of drop value). For the smallest rural outlets at ₹800 per drop, ₹66.7 is **8.3%** of the drop, so a weekly visit is uneconomic: fortnightly visits, wholesaler or redistribution-stockist supply, or digital ordering with consolidated drops would bring the cost per sales rupee down. Hence segment outlets by size and potential instead of treating all outlets equally.

### In the news
See news box. IBEF notes the rural segment as 38% of 2024 FMCG sales and rising in affordable-premium volumes; Dabur's 1,31,000-village reach highlights how large the rural CTS challenge is.

### Interview angle
> [!question] How it is asked
> "A company wants to double rural outlet coverage without raising distribution cost. How?"

> [!tip] Strong answer includes
> - Outlet segmentation and CTS by cluster; frequency by potential
> - Hub-and-spoke via RS, sub-stockists, micro-entrepreneurs, van sales, digital ordering
> - Product and pack choices (small packs) for rural
> - Credit control and monitoring through DMS/SFA

---
## 14. ⭐ Advanced: Redesigning Route-to-Market, a Consulting Case
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **route-to-market (RTM) redesign** asks: for each **outlet segment (class and geography)**, what is the most profitable and effective **channel and service model**? Steps: (1) **segment outlets** by type, size, location and potential; (2) calculate **cost-to-serve and margin by segment and route**; (3) identify **overlaps and gaps** (outlets served by multiple distributors or none); (4) set **tier roles** (direct, distributor, wholesaler, RS, e-B2B) and **service standards** (visit frequency, delivery lead time, credit); (5) design **distributor ROI** and **incentives** with a hurdle rate; (6) enable with **DMS/SFA and data**; (7) **pilot, measure, scale**. Frameworks: [[024 Consulting Frameworks]], [[112 Supply Chain Strategy - Fit, Segmentation & Maturity]]. Network aspects after GST: **fewer depots and larger consolidated warehouses**, as discussed in [[227 GST & Indirect Tax for Supply Chains]] and [[113 Network Design & Facility Location Modelling]].

### Example
A company with ₹800 crore of sales across 100,000 outlets segments them: Segment A (10,000 large outlets, 45% of sales = ₹360 crore), B (30,000 medium, 35% = ₹280 crore) and C (60,000 small, 20% = ₹160 crore). A cost-to-serve analysis finds A at 2.5%, B at 4.0% and C at 8.5% of sales: A = ₹9.0 crore, B = ₹11.2 crore, C = ₹13.6 crore, a total of **₹33.8 crore (4.2%)**, hidden by a single company-wide average. Proposal: serve C outlets fortnightly via wholesalers and e-B2B ordering, cutting their cost to serve from 8.5% to 5.5% (a saving of 3 points x ₹160 crore = **₹4.8 crore**), at the risk of losing 5% of C's volume (₹8 crore of sales at 25% margin = **₹2 crore**). The **net benefit is ₹2.8 crore a year**, plus lower distributor workload. The case structure interviewers expect: segment, cost-to-serve, options, risk, pilot.

### In the news
See news box. Organised retail (14% of market) and quick commerce (70-75% of e-grocery orders) are new RTM routes: the redesign question is how to allocate outlets across GT, MT, Q-commerce and direct models after the GST reform and the shift in consumption toward rural and affordable-premium segments.

### Interview angle
> [!question] How it is asked
> "A ₹5,000 crore FMCG company asks you to reduce distribution cost by 100 bps without losing reach. Structure your approach."

> [!tip] Strong answer includes
> - Segmentation and cost-to-serve baseline; identify where the 100 bps will come from
> - Options by segment with quantified savings and risk (reach, service, distributor ROI)
> - Enablers: DMS/SFA, route rationalisation, depot consolidation, digital ordering
> - Pilot plan, KPIs (distribution, fill rate, ROI) and change management
