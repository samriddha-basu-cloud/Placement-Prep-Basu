---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Supply Chain Finance & Working Capital"
tier: Tier 1
roles: Consulting / Operations / Finance
status: complete
subtopics: 14
---
# Supply Chain Finance & Working Capital

⬅ [[135 Reverse Logistics, Remanufacturing & EPR in India]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[137 Supply Chain Contracts & Game Theory]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Consulting / Operations / Finance

## Sub-topics in this note
1. [[#1. Working Capital and the Cash-to-Cash Cycle]]
2. [[#2. Levers on DIO, DSO and DPO]]
3. [[#3. Cost of Capital, the Value of a Day and Discount Rates]]
4. [[#4. Trade Credit Terms: 2/10 Net 30]]
5. [[#5. The Supply Chain Finance Landscape]]
6. [[#6. Reverse Factoring (Approved Payables Finance)]]
7. [[#7. Dynamic Discounting]]
8. [[#8. Inventory Finance and PO Finance]]
9. [[#9. TReDS in India (RXIL, M1xchange, Invoicemart)]]
10. [[#10. The MSME 45-Day Payment Rule and Section 43B(h)]]
11. [[#11. Releasing Cash by Reducing Inventory]]
12. [[#12. Supplier Financial Health]]
13. [[#13. ⭐ Advanced: Greensill and the Failure Modes of Supply Chain Finance]]
14. [[#14. ⭐ Advanced: A Working-Capital Diagnostic in a Consulting Case]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): invoice discounting scaled up in India while global companies still hold trillions in idle working capital
> **TReDS crosses ₹2 lakh crore (July 2025).** The Receivables Exchange of India (RXIL), one of India's RBI-authorised TReDS platforms, announced that it had crossed **₹2 trillion (₹2 lakh crore)** of cumulative MSME invoice financing on 2 July 2025, with **₹80,500 crore financed in FY25 alone**, over 44,000 MSMEs registered and over 88.5 lakh invoices discounted. ([Business Standard](https://www.business-standard.com/economy/news/treds-platform-rxil-crosses-2-trn-msme-invoice-financing-milestone-125070200578_1.html))
>
> **Wider TReDS net (Nov 2024).** The MSME Ministry notified that companies with turnover above **₹250 crore (down from ₹500 crore)** and all central public sector enterprises must onboard to TReDS by **31 March 2025**. M1xchange's CEO said small firms can get invoices discounted on TReDS at roughly **7-10% a year against 15-24%** outside it. ([M1xchange](https://www.m1xchange.com/treds-govt-reduces-turnover-threshold-to-rs-250-cr-to-get-more-companies-on-invoice-discounting-platform/); [Business Standard](https://www.business-standard.com/finance/news/rbi-s-treds-platform-bridging-600-bn-funding-gap-for-smaller-firms-124102201091_1.html))
>
> **RBI consolidates TReDS rules (June 2026).** According to M1xchange's summary, RBI issued a single TReDS Master Direction on **23 June 2026** that replaced the earlier guidelines and the June 2023 circular. Reported changes: re-discounting of factoring units, access to government credit-guarantee funds, no insurance premium on the seller, no buyer set-off against accepted units, and a **₹25 crore minimum net worth** for operators by 31 March 2028. Check the RBI text before quoting details. ([M1xchange](https://www.m1xchange.com/thought-xchange/rbi-rationalises-treds-rules-in-2026-one-master-direction-a-complete-overhaul/))
>
> **$1.7 trillion still trapped (Aug 2025).** The Hackett Group's 2025 Working Capital Survey of the 1,000 largest US public companies (2024 data) found the cash conversion cycle improved 4% to **37 days**, with DPO up 3% to **59 days**, yet **$1.7 trillion (35% of gross working capital)** remained excess; receivables alone were about $600 billion of it. ([Hackett Group](https://www.thehackettgroup.com/2025-working-capital-survey-payables-rebound-receivables-inventory-lag/))
>
> **Supplier finance must now be disclosed.** The IASB's amendments to IAS 7 and IFRS 7 require companies to disclose the terms, liability amounts, payment-due ranges and liquidity risk of supplier finance arrangements, effective for annual periods beginning on or after **1 January 2024**. ([IFRS Foundation](https://www.ifrs.org/news-and-events/news/2023/05/iasb-increases-transparency-of-companies-supplier-finance/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Working Capital and the Cash-to-Cash Cycle
> 🔴 Tier 1 · _Key points:_ Net working capital, CCC = DIO + DSO − DPO, why cash is a supply chain KPI

### Definition
**Working capital** is the cash tied up in running the operating cycle. **Net trade working capital (NTWC)** = inventory + trade receivables − trade payables. The **cash-to-cash (cash conversion) cycle** measures how many days cash is locked up between paying suppliers and collecting from customers:

$$CCC = DIO + DSO - DPO$$

$$DIO = \frac{\text{Inventory}}{\text{COGS}} \times 365, \quad DSO = \frac{\text{Receivables}}{\text{Sales}} \times 365, \quad DPO = \frac{\text{Payables}}{\text{COGS}} \times 365$$

Use average balances for rigour and COGS (not sales) for DIO and DPO because inventory and payables are carried at cost. A negative CCC means suppliers fund the business (Amazon-style marketplaces, FMCG giants with fast stock turns and long creditor terms). Link: DIO is the inverse of [[003 Inventory Management|inventory turnover]]; the ratio definitions sit in [[108 Financial Statements & Ratios]]; the KPI is the "cash-to-cash cycle time" metric in the [[111 SCOR Model & Supply Chain Process Frameworks|SCOR]] asset-management attribute.

### Example
A Pune auto-component maker: sales ₹1,200 crore, COGS ₹900 crore, inventory ₹150 crore, receivables ₹200 crore, payables ₹120 crore.

- DIO = 150/900 × 365 = **60.8 days**
- DSO = 200/1,200 × 365 = **60.8 days**
- DPO = 120/900 × 365 = **48.7 days**
- CCC = 60.8 + 60.8 − 48.7 = **73.0 days**

NTWC = 150 + 200 − 120 = ₹230 crore, i.e. 19% of sales. Every extra day of CCC costs roughly one day of sales or COGS in cash (₹2.5-3.3 crore here).

### In the news
See news box. The Hackett survey is the standard benchmark: top-quartile firms beat the median by about 18 days of DSO, and the large "trapped" figure is why CFOs now push supply chain teams on cash, not only cost.

### Interview angle
> [!question] How it is asked
> "A client's EBITDA is fine but they keep drawing more bank debt. How do you diagnose it?"

> [!tip] Strong answer includes
> - Compute DIO, DSO, DPO and CCC, then trend and benchmark against peers (same sector)
> - Translate days into rupees: one day of sales or COGS = cash
> - Split inventory into RM/WIP/FG, receivables into overdue vs not-yet-due
> - Name growth as a cause: a growing firm needs more working capital even when profitable

---
## 2. Levers on DIO, DSO and DPO
> 🔴 Tier 1 · _Key points:_ Inventory, receivables, payables levers; trade-offs; cash release worked example

### Definition
Each component has operational levers, and each lever has a trade-off.

| Lever | Typical actions | Trade-off / watch-out |
|---|---|---|
| **DIO down** | Right-size safety stock ([[003 Inventory Management]]), SKU rationalisation, better forecasts ([[004 Demand Forecasting & Planning]]), lower lot sizes via setup reduction, DDMRP buffers ([[117 Demand-Driven MRP (DDMRP) & Buffer Management|DDMRP]]), consignment/VMI, clear obsolete stock | Service level and stock-outs; supply risk |
| **DSO down** | Clean invoicing and fewer disputes, credit scoring, dunning, e-invoicing, early-payment discounts, TReDS, factoring | Customer relationships; price concessions |
| **DPO up** | Negotiated terms, payment-run discipline (pay on due date, not early), reverse factoring, dynamic discounting ([[122 Spend Analysis, Savings & Procurement Maturity|procurement]] levers) | Supplier health, price increases, **MSME 45-day rule**, reputation |

The trap is **optimising one lever at one firm's expense**: stretching payables simply moves working capital onto weaker suppliers' balance sheets, whose cost of capital is higher, so total supply chain cost rises and risk rises ([[015 Supply Chain Risk & Resilience]]). The end-to-end view treats the *chain's* cash cycle as the thing to minimise, which is the logic of supply chain finance.

### Example
For the maker above, a programme delivers DIO −10, DSO −10, DPO +10 days.

- DIO −10 days frees 10 × 900/365 = **₹24.7 crore**
- DSO −10 days frees 10 × 1,200/365 = **₹32.9 crore**
- DPO +10 days frees 10 × 900/365 = **₹24.7 crore**
- Total one-time cash release = **₹82.2 crore**; CCC falls from 73.0 to 43.0 days

At a 10% cost of debt the recurring interest saving is about **₹8.2 crore a year**. Note that this is a one-time cash release plus a recurring finance-cost saving, not a recurring cash flow.

### In the news
See news box. The Hackett finding that payables improved while receivables and inventory lagged shows companies reach first for the easiest lever (DPO), which is exactly what the Indian MSME payment rule now restricts.

### Interview angle
> [!question] How it is asked
> "Which of DIO, DSO and DPO would you attack first for a mid-sized manufacturer and why?"

> [!tip] Strong answer includes
> - Rank by size of rupee prize and ease, not by habit; use value per day (COGS/365 vs sales/365)
> - Name the trade-off for each lever (service, relationship, supplier stress)
> - Prefer root-cause fixes (forecast accuracy, dispute-free invoicing) over pure term stretching
> - Quantify cash release and the finance-cost saving separately

---
## 3. Cost of Capital, the Value of a Day and Discount Rates
> 🔴 Tier 1 · _Key points:_ Compare the return on cash vs the cost of money; WACC vs short-term rate; whose cost of capital?

### Definition
Working-capital decisions are rate comparisons. The **value of a day** of cash is $\text{cash per day} \times \text{cost of capital}/365$. Which rate to use depends on the cash in question:

- **Buyer with surplus cash**: the opportunity cost is the treasury yield (for example 6-7% on liquid funds). Paying early for a 1.5% discount over 30 days (about 18-19% annualised) beats it.
- **Buyer drawing working-capital loans**: the marginal short-term borrowing rate (say 9-10%).
- **Long-lived investments** (capex, network design): WACC, because funding is mixed and permanent ([[226 Corporate Finance Essentials - Capital Structure & Cost of Capital]], [[109 Valuation Basics (NPV, IRR, DCF)]]).
- **Supplier**: its own borrowing rate, often 12-24% for a small Indian MSME, against a large corporate's 7-9%. This **spread in cost of capital** is the economic engine of supply chain finance: the anchor buyer's credit rating lends cheap money to its weaker suppliers.

An **annualised discount rate** for early payment: $r = \frac{d}{1-d} \times \frac{365}{t}$ where $d$ is the discount fraction and $t$ the days accelerated (simple); the compound equivalent is $(1+\frac{d}{1-d})^{365/t}-1$.

### Example
A buyer has ₹10 crore idle cash earning 7%. A supplier offers 1% off if paid 20 days early instead of day 30.

- Annualised simple return = 1/99 × 365/20 = **18.4%** (compound 20.1%), well above 7%, so take it.
- On a ₹10 crore invoice, paying on day 10 costs ₹9.9 crore instead of ₹10 crore on day 30. The ₹10 lakh gain on ₹9.9 crore for 20 days annualises to 18.4%. Holding the ₹9.9 crore at 7% instead would earn only 9.9 crore × 7% × 20/365 = ₹3.8 lakh.
- If the same buyer instead borrows at 11%, the discount is still worth taking since 18.4% > 11%.

A **hurdle comparison for extending terms**: stretching DPO by 45 days on ₹1,000 crore of annual purchases frees ₹123.3 crore (1,000 × 45/365) and saves ₹12.3 crore a year at 10%. If the suppliers' own cost of money is 15%, carrying the same ₹123.3 crore costs them ₹18.5 crore a year, so the chain as a whole is worse off by about ₹6.2 crore unless the buyer shares the saving or funds it through a programme.

### In the news
See news box. TReDS discounting at about 7-10% against 15-24% outside the platform is the same buyer-credit-versus-supplier-credit spread in action.

### Interview angle
> [!question] How it is asked
> "Should we accept the supplier's early-payment discount, or hold the cash for 30 more days?"

> [!tip] Strong answer includes
> - Convert the discount into an annualised rate and compare with the relevant cost of money
> - Choose the right comparator (surplus yield vs borrowing rate), not blanket WACC
> - Mention supplier-side value (their cost of capital is higher, so a shared saving exists)
> - Tax shield and covenants are second-order; liquidity risk is first-order

---
## 4. Trade Credit Terms: 2/10 Net 30
> 🔴 Tier 1 · _Key points:_ Implied interest rate, simple vs effective annual rate, early-payment discount logic

### Definition
**Trade credit** is supplier financing: goods delivered now, payment later. Terms are written "$d$/$t_d$ net $T$": a discount of $d\%$ if paid within $t_d$ days, otherwise full payment at day $T$. Skipping the discount means borrowing the discounted price for $T - t_d$ days at an implicit rate:

$$\text{Simple annual rate} = \frac{d}{1-d} \times \frac{365}{T - t_d}$$

$$\text{Effective annual rate (EAR)} = \left(1 + \frac{d}{1-d}\right)^{365/(T-t_d)} - 1$$

Trade credit is often "free" only if the discount is taken; otherwise it is among the most expensive finance a firm uses, and most firms that miss the discount do so unknowingly. Indian practice: payment terms of 30, 45, 60, 90 days or more in retail and heavy engineering, with the MSME statutory cap of 45 days when the supplier is a micro or small enterprise ([[227 GST & Indirect Tax for Supply Chains]] explains the invoice trail that proves dates).

### Example
Terms **2/10 net 30** on a ₹5 lakh invoice.

- Pay on day 10: ₹5,00,000 × 0.98 = **₹4,90,000**.
- Pay on day 30: ₹5,00,000. Extra ₹10,000 for 20 days on ₹4,90,000 → 2.04% for 20 days.
- Simple annual rate = 2/98 × 365/20 = **37.2%**; EAR = (1.0204)^(18.25) − 1 = **44.6%**.

Variants: 1/10 net 30 gives 18.4% simple (20.1% EAR); 2/10 net 60 gives 14.9% simple (15.9% EAR), which is why stretching the net date dilutes the discount's attractiveness.

Decision rule: **take the discount if the implicit rate exceeds your best alternative cost of funds**; if cash is short, borrow from the bank at 12-14% to pay on day 10 and save the difference.

### In the news
See news box. With 43B(h) in force, buyers face a 45-day ceiling on payments to micro and small suppliers, so a buyer with spare cash can still use an early-payment discount (for example 1% for payment inside 15 days) as a negotiation lever, provided the discount is the supplier's free choice.

### Interview angle
> [!question] How it is asked
> "Supplier offers 2/10 net 30. Our bank cost is 12%. What do you do and what is the effective cost of not taking it?"

> [!tip] Strong answer includes
> - The formula and the number (about 37% simple, about 45% EAR)
> - Decision: take the discount, even by borrowing
> - Caveat: a supplier offering a very large discount may be signalling its own liquidity stress
> - Stretching beyond day 30 ("stacking" payables) harms the relationship and credit terms

---
## 5. The Supply Chain Finance Landscape
> 🔴 Tier 1 · _Key points:_ Buyer-led vs seller-led, receivables vs payables vs inventory finance, who funds and who takes the risk

### Definition
**Supply chain finance (SCF)** is a family of techniques that use the **credit strength of the anchor** (usually the buyer) to release cash across the chain at lower cost, while the physical flow is untouched. Map the tools by the asset financed and the party initiating:

| Tool | Asset financed | Initiated by | Who bears credit risk | Typical use |
|---|---|---|---|---|
| **Reverse factoring (approved payables finance)** | Approved invoice | Buyer | Buyer (the anchor) | Big buyer, many small suppliers |
| **Dynamic discounting** | Approved invoice | Buyer | Buyer pays from own cash | Cash-rich buyer |
| **Factoring / invoice discounting** | Receivable | Seller | Seller's customers (non-recourse) or seller (recourse) | Seller needs cash |
| **TReDS** | Accepted invoice (factoring unit) | Seller (MSME) | Buyer (non-recourse to MSME) | India, MSME suppliers to larger buyers |
| **Inventory / warehouse-receipt finance** | Stock | Owner | Owner and collateral value | Commodities, agri, dealers |
| **PO finance** | Confirmed purchase order | Supplier | Buyer's order plus supplier's performance | Traders, exporters, start-ups |
| **Trade finance (LC, bank guarantees, pre-shipment credit)** | Shipment / contract | Either | Bank | International trade ([[126 International Trade Documentation, Customs & Trade Finance]]) |

Three design questions for any scheme: **who is the credit anchor, is the financing off the supplier's recourse, and does it change how the buyer's accountants classify the payable** (trade payable vs financial debt: the topic that triggered disclosure rules).

### Example
Anchor buyer: AAA-rated, borrows at 7.5%. Fifty MSME suppliers: 14-18% own borrowing. A programme lets suppliers discount approved invoices at the buyer's rate plus a spread (about 8.5%). The 6-9 percentage-point cost saving per supplier is shared: suppliers keep most of it, the buyer takes DPO extension, and the funder earns a spread on a near-bank-risk asset.

### In the news
See news box. TReDS is India's regulated, exchange-style version of buyer-anchored receivables financing, and the IFRS 7 disclosure amendments address the reverse-factoring side.

### Interview angle
> [!question] How it is asked
> "What is supply chain finance and how is it different from a normal bank loan to a supplier?"

> [!tip] Strong answer includes
> - The anchor-credit idea: price the risk on the buyer, not the weak supplier
> - A clear taxonomy (receivables-, payables-, inventory-based; buyer-led vs seller-led)
> - Win-win logic and the catch (buyer may use it to extend terms; supplier dependence)
> - Link to procurement strategy: use for tail suppliers, not for strategic ones

---
## 6. Reverse Factoring (Approved Payables Finance)
> 🔴 Tier 1 · _Key points:_ Mechanics, buyer extends DPO, supplier gets early cash at buyer's rate, accounting risk

### Definition
In **reverse factoring**, the buyer approves an invoice on the platform of a bank or fintech. The supplier may take payment immediately (less a discount priced off the **buyer's** credit rating) or wait until the due date. At maturity the buyer pays the funder. Flow:

1. Supplier ships and invoices; buyer approves the invoice (irrevocable payment undertaking).
2. Funder pays the supplier on request at a discount: $\text{Price} = F\left(1 - r \times \frac{\text{days remaining}}{365}\right)$.
3. Buyer pays the funder the full amount on the original (often extended) due date.

Benefits: supplier cash at a lower rate; buyer extends terms (DPO) without harming supplier liquidity; funder gets low-risk short-tenor assets. Risks: **concentration** (all suppliers depend on one programme), **covenant and rating risk** if the funding line is withdrawn, **disclosure** (rating agencies and IAS 7/IFRS 7 treat large programmes as debt-like exposure), and **"payables reclassification"**.

### Example
Buyer purchases ₹1,000 crore a year; terms extended from 45 to 90 days under the programme. Invoice of ₹100 lakh due on day 90; supplier draws funds on day 15 (75 days early) at 8.5%.

- Discount = 100 × 0.085 × 75/365 = **₹1.75 lakh**; supplier receives **₹98.25 lakh** on day 15.
- Supplier's own borrowing at 15% for the same 75 days would cost ₹3.08 lakh, so it saves about **₹1.33 lakh** per invoice.
- Buyer: 45 extra days × ₹1,000 crore/365 = **₹123.3 crore** cash released; saves about ₹12.3 crore a year at 10%.

Without the programme the supplier would wait 90 days for cash; with it, the supplier chooses between waiting and paying about 1.75% for 75 days of cash.

### In the news
See news box. IASB (IAS 7 and IFRS 7) and US GAAP (ASU 2022-04) now require disclosure of terms, outstanding amounts and payment ranges, because analysts could not see how much debt-like funding sat inside trade payables.

### Interview angle
> [!question] How it is asked
> "A client wants to extend supplier payment terms from 45 to 90 days using reverse factoring. Walk me through the economics and risks."

> [!tip] Strong answer includes
> - Cash released = purchases × extra days/365, and the finance-cost saving
> - Supplier-side benefit only if the programme rate beats their own cost of money
> - Risks: concentration, programme withdrawal, disclosure/rating treatment, MSME law
> - Governance: written terms, caps by supplier, funder diversification

---
## 7. Dynamic Discounting
> 🔴 Tier 1 · _Key points:_ Buyer pays early from own cash for a sliding discount; APR logic; vs reverse factoring

### Definition
In **dynamic discounting** the buyer uses its **own cash** to pay approved invoices early in return for a discount that **slides with time**: the earlier the payment, the larger the discount. The discount is set as an annualised rate (APR) applied to the days accelerated:

$$\text{Discount} = \text{Invoice} \times \text{APR} \times \frac{\text{days early}}{360 \text{ (or 365)}}$$

Contrast with a fixed "2/10 net 30" static discount and with reverse factoring (third-party funding). Dynamic discounting suits **cash-rich buyers** whose treasury yield is below the supplier's cost of funds; it generates a return, not a DPO extension. It is also **supplier-optional**, can be run invoice-by-invoice, and avoids debt classification issues. Many ERPs and e-invoicing platforms support it ([[199 SAP Ariba, SRM & Business Network]], [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]).

### Example
Invoice ₹100 lakh due in 60 days. The buyer offers an 18% APR (360-day basis); the supplier chooses payment 30 days early.

- Discount = 100 × 0.18 × 30/360 = **₹1.5 lakh**; buyer pays **₹98.5 lakh**.
- Buyer's annualised return = 1.5/98.5 × 365/30 = **18.5%**, against, say, a 7% treasury yield.
- Over ₹500 crore of eligible annual spend with 30% adoption and an average 30-day acceleration, the buyer earns about ₹500 × 0.30 × 1.5% = ₹2.25 crore a year on cash otherwise earning 7% (₹1.3 crore on the same deployed amount).

### In the news
See news box. Where buyers have strong cash but suppliers are MSMEs facing the 45-day limit, early-payment programmes are a compliant way to turn cash into both supplier loyalty and yield.

### Interview angle
> [!question] How it is asked
> "When would you choose dynamic discounting over reverse factoring?"

> [!tip] Strong answer includes
> - Cash-rich buyer vs a buyer wanting to preserve cash (reverse factoring) or extend terms
> - Return framing: APR earned vs treasury yield
> - Supplier voluntariness and fairness (avoid coercive discount demands)
> - Hybrid use: dynamic discounting first, then third-party funding when buyer cash runs out

---
## 8. Inventory Finance and PO Finance
> 🔴 Tier 1 · _Key points:_ Stock as collateral, warehouse receipts, channel/floor-plan finance, PO finance risks

### Definition
**Inventory finance** lends against stock: the lender takes a pledge or hypothecation over goods held in a controlled location, with a haircut (advance rate) of typically 60-80% of value depending on commodity volatility and liquidity. Variants:

- **Warehouse-receipt finance**: goods sit in an accredited warehouse and a receipt is pledged; in India, electronic negotiable warehouse receipts (e-NWR) under the Warehousing Development and Regulatory Authority are used for agri-commodities.
- **Collateral-management arrangements**: a third-party collateral manager guards and reports stock for the bank.
- **Channel (dealer) finance / floor-plan finance**: funds a distributor's or dealer's stock, with the manufacturer as anchor (autos, consumer durables, tractors).
- **Vendor-managed and consignment stock** ([[003 Inventory Management]]) are the non-financing cousins: the supplier funds the stock.

**Purchase-order (PO) finance** advances funds to a supplier against a confirmed PO from a creditworthy buyer so it can buy inputs and produce. It is riskier than invoice finance because the *performance* risk (can the supplier deliver and pass quality?) sits with the funder, hence higher pricing and strict controls (direct payments to input suppliers, assignment of proceeds).

Key risks: collateral fraud (double pledging, phantom stock), price volatility ([[123 Commodity Price Risk, Hedging & Contract Pricing Mechanisms]]), quality deterioration, and legal enforceability.

### Example
A rice exporter holds ₹20 crore of paddy-milled rice in an accredited warehouse. A bank advances 70% = **₹14 crore** against warehouse receipts at 10%. Holding it for 90 days costs 14 × 0.10 × 90/365 = **₹0.345 crore** interest. The firm avoids selling in the harvest-glut price trough. If market price falls 20%, collateral becomes ₹16 crore and the 70% advance (₹14 crore) is now 87.5% of value: a margin call looms.

PO finance example: a trader holds a confirmed ₹50 lakh PO from a creditworthy buyer; input cost is ₹37.5 lakh. The funder pays the input supplier directly for 80% of cost (₹30 lakh) and collects from the buyer on delivery; the trader's margin (₹12.5 lakh) is only realised if delivery and quality pass.

### In the news
See news box. As TReDS and invoice finance scale for post-delivery receivables, the open gap for MSMEs is **pre-delivery** finance (inventory and PO), which remains mostly bilateral bank or NBFC lending.

### Interview angle
> [!question] How it is asked
> "A seasonal agri-processor is cash-constrained at harvest. What financing solutions would you design?"

> [!tip] Strong answer includes
> - Warehouse-receipt or stock finance with advance rate and haircuts
> - Controls: accredited warehouses, insurance, collateral manager, periodic audits
> - Match tenor to the stock-holding cycle; avoid short-term debt for permanent stock
> - Price risk hedging and margin-call mechanics

---
## 9. TReDS in India (RXIL, M1xchange, Invoicemart)
> 🔴 Tier 1 · _Key points:_ RBI-regulated e-platform, buyer-accepted invoices, competitive bidding, without recourse

### Definition
The **Trade Receivables Discounting System (TReDS)** is an RBI-regulated electronic platform, operating under the Payment and Settlement Systems Act, where MSME sellers upload invoices, corporate or government buyers accept them, and financiers (banks, NBFC-factors, other RBI-permitted institutions) bid to discount them. RBI's FAQ describes the flow: invoice becomes a **factoring unit**, the buyer accepts, financiers bid competitively, the best bid is selected, the seller is paid, and the buyer repays the financier on the due date. The facility is **without recourse** to the MSME seller if the buyer defaults, and default handling sits with the financier, not the platform.

Why it is powerful: the lender prices the **buyer's** risk, so rates are lower than MSME working-capital loans, auctions compress spreads, and payment dates are visible and enforceable. Platforms: **RXIL, M1xchange and Invoicemart** are the established three; the MSME Ministry's November 2024 notification, as reported by M1xchange, refers to four authorised platforms including C2treds. Platform details such as number of banks, fees and eligibility change frequently, so check current figures before quoting.

Policy tailwind: the 2024 notification lowered the onboarding threshold for buyers to ₹250 crore turnover and covers all CPSEs. Link to the next sub-topic: TReDS gives buyers a way to meet the 45-day rule at a lower cash cost.

Limits: penetration remains low (a Data Diaries analysis of FY2025-26 data put it near 1.2% of GST-registered MSMEs, with about 2.46 lakh sellers and ₹3.47 lakh crore financed; treat it as a third-party estimate), many buyers onboarded "for form", and low-ticket or informal suppliers are underserved.

### Example
An MSME sells ₹25 lakh of fabricated parts to a large OEM on 60-day terms. On day 5 the OEM accepts the invoice on TReDS; a bank wins the bid at 8.4% discount.

- Days to maturity: 55. Discount = 25 lakh × 0.084 × 55/365 = **₹31,644**.
- MSME receives about **₹24.68 lakh** on day 5 instead of waiting to day 60.
- Bank loan at 16% for 55 days would have cost **₹60,274**; saving about ₹28,600.
- If the OEM defaults, the financier absorbs the loss; the MSME owes nothing.

### In the news
See news box. RXIL's ₹2 lakh crore cumulative milestone, the lowered buyer threshold and the 2026 consolidated Master Direction show TReDS shifting from pilot to core infrastructure.

### Interview angle
> [!question] How it is asked
> "How does TReDS help MSMEs and why has adoption been slower than expected?"

> [!tip] Strong answer includes
> - Participants and flow: seller, buyer, financier; factoring unit; bidding; without recourse
> - Why rates are low: buyer risk, competition, transparency
> - Adoption barriers: buyer reluctance, onboarding, limited MSME awareness, small invoice sizes
> - Policy levers: turnover thresholds, CPSE mandates, guarantees, insurance

---
## 10. The MSME 45-Day Payment Rule and Section 43B(h)
> 🔴 Tier 1 · _Key points:_ MSMED Act s.15-16 (45 days), 43B(h) tax disallowance, micro/small only, effect on DPO

### Definition
The **MSMED Act, 2006** (Section 15) sets the maximum credit period for goods or services bought from micro and small enterprises: **15 days** from acceptance or deemed acceptance if there is no written agreement, and no more than **45 days** even with one. Delayed payment attracts compound interest, with monthly rests, at **three times the RBI bank rate** (Section 16); this interest is not tax-deductible.

**Section 43B(h)** of the Income-tax Act, 1961 (inserted by the Finance Act 2023, effective 1 April 2024, i.e. AY 2024-25, so first tested on FY 2023-24 accounts) bites on taxes: an amount owed to a micro or small enterprise **beyond the Section 15 time limit** is allowed as a deduction **only in the year it is actually paid**. So an unpaid, overdue MSE payable at 31 March is added back to taxable income for that year. Key scope points (check the date you read them: interpretation continues to evolve):

- Applies to **micro and small** enterprises registered under MSMED Act (Udyam); **medium enterprises and unregistered suppliers are outside it**.
- Covers purchases of goods and services; traders' status has been debated, so check supplier classification.
- No "pay by the return filing date" relief; late payment simply shifts the deduction.
- Reported to be carried into the Income-tax Act 2025 (in force from 1 April 2026) with the same effect; verify the section number in the new Act before citing it.

### Example
A company buys ₹10 lakh of components from a small enterprise on 1 April 2025 under a written 45-day agreement, so it is due by 16 May. It pays on 20 June.

- **Case A:** paid 20 June 2025, 35 days late, but within the same financial year, so the deduction stays in FY 2025-26; the exposure is the MSMED Act interest, not the tax add-back.
- **Case B:** invoice dated 15 February 2026, due 1 April 2026, unpaid on 31 March 2026: not yet overdue, so still deductible in FY 2025-26.
- **Case C:** invoice dated 10 January 2026, due 24 February 2026, still unpaid on 31 March 2026: **disallowed in FY 2025-26** and deductible only in FY 2026-27 when paid.
- Tax effect on a ₹10 lakh item at the 25.17% effective company rate (22% + 10% surcharge + 4% cess) is **₹2.52 lakh** of tax pulled forward by one year; at 10% cost of money, the real timing cost is about ₹0.25 lakh, but the MSMED interest at 3 times bank rate, compounded monthly and non-deductible, is the larger penalty.

The Clothing Manufacturers Association of India anticipated losses of ₹5,000-7,000 crore because retail pays on 90-120 day cycles (as reported by Business Standard in 2024), which illustrates the real operational impact.

### In the news
See news box. The 45-day cap is a main reason buyers have to either pay MSMEs earlier, shorten terms contractually, or provide TReDS and reverse factoring so that the supplier is paid early while the buyer's cash date still meets the rule.

### Interview angle
> [!question] How it is asked
> "A retail client pays suppliers at 90 days. How does 43B(h) change their working capital strategy?"

> [!tip] Strong answer includes
> - The rule: 15/45-day limit, micro and small only, deduction on payment basis
> - Cash impact: DPO for this supplier segment falls from 90 to 45 days; compute the cash needed
> - Responses: segment suppliers by Udyam status, renegotiate, use TReDS or dynamic discounting, pass costs into price, tighten procure-to-pay controls ([[190 SAP FI-CO Essentials for Operations Professionals]])
> - Governance: Udyam certificate capture and master-data hygiene

---
## 11. Releasing Cash by Reducing Inventory
> 🔴 Tier 1 · _Key points:_ One-time release + carrying-cost saving; where to cut; service risk; EBITDA vs cash

### Definition
Cutting inventory is the biggest cash lever in most manufacturers and distributors. The **one-time cash release** is:

$$\Delta \text{Cash} = \Delta \text{Days} \times \frac{\text{COGS}}{365} = \text{Inventory} \times \text{\% reduction}$$

and the **recurring annual saving** is the **carrying-cost rate × inventory removed** (capital cost + storage + insurance + obsolescence, typically 15-30% of value, see [[003 Inventory Management]]). Practical sources of release: slow/obsolete stock write-down and liquidation ([[116 Inventory Valuation, Cycle Counting & Inventory Governance]]), SKU pruning, lower safety stock via better forecasts and lead-time variability reduction, smaller lots and EPQ re-optimisation ([[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]]), shifting to a pull replenishment, multi-echelon rebalancing, pushing consignment stock to suppliers (careful: it may simply raise prices).

Distinguish **cash** from **P&L**: releasing inventory raises operating cash flow once; the P&L gains only through the carrying-cost saving; a write-down hits profit immediately.

### Example
Inventory ₹150 crore; COGS ₹900 crore (6.0 turns, DIO 60.8 days). Target: cut 20% through SKU rationalisation and safety-stock reset.

- One-time release = 150 × 0.20 = **₹30 crore**; new DIO = 48.7 days; turns = 7.5.
- Recurring carrying-cost saving at 25% = **₹7.5 crore a year** (of which capital cost at 10% is ₹3.0 crore and the remaining ₹4.5 crore is storage, insurance and obsolescence).
- Cost: if fill rate drops from 97% to 96% on a ₹1,200 crore business, lost margin of 1% × 1,200 × 25% gross margin = ₹3 crore: the net gain is still positive but now is a service-versus-cash call.

### In the news
See news box. The Hackett survey flagged inventory as lagging in 2024; in the cases of tariff front-loading and chip-shortage buffers, companies raised stock deliberately, showing that inventory decisions are strategic, not just financial ([[015 Supply Chain Risk & Resilience]]).

### Interview angle
> [!question] How it is asked
> "The CFO wants a 20% inventory cut. How do you decide where to cut and what could go wrong?"

> [!tip] Strong answer includes
> - Segment first (ABC/XYZ, aged stock, SKU contribution) before cutting across the board
> - Quantify release and recurring saving, with carrying-cost components
> - Service-level and supply-risk guardrails; stage-gate the target
> - Distinguish one-time cash from recurring savings; avoid cutting buffers on critical, long lead-time items

---
## 12. Supplier Financial Health
> 🔴 Tier 1 · _Key points:_ Early-warning signs, Altman Z-score, concentration, mitigation

### Definition
A supplier's insolvency can halt a line more surely than a quality problem. Supplier financial-health monitoring combines:

- **Quantitative models**: the **Altman Z-score** for listed manufacturers

$$Z = 1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + 1.0X_5$$

with $X_1$ = working capital/total assets, $X_2$ = retained earnings/total assets, $X_3$ = EBIT/total assets, $X_4$ = market value of equity/total liabilities, $X_5$ = sales/total assets. Zones (listed manufacturers): above 2.99 safe, 1.81-2.99 grey, below 1.81 distress. Variants exist for private and non-manufacturing firms with different coefficients and cut-offs.
- **Ratios**: current ratio, interest coverage, debt/EBITDA, DSO creeping up, DPO to its own vendors stretching, covenant breaches.
- **External signals**: credit-rating downgrades (CRISIL, ICRA, CARE), bureau reports, litigation, GST filing delays, bank-account irregularities, late payments to labour, key-person exits.
- **Operational signals**: rising defects, missed deliveries, deferred maintenance, requests for advances or price rises.

Mitigations ([[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]], [[015 Supply Chain Risk & Resilience]]): dual sourcing for critical parts, step-in rights and tooling ownership, supplier development, supply chain finance for healthy but under-financed suppliers, and **contingency inventory** for those showing stress.

### Example
Supplier ratios: $X_1 = 0.12$, $X_2 = 0.10$, $X_3 = 0.08$, $X_4 = 0.9$, $X_5 = 1.1$.
Z = 1.2(0.12) + 1.4(0.10) + 3.3(0.08) + 0.6(0.9) + 1.0(1.1) = 0.144 + 0.14 + 0.264 + 0.54 + 1.1 = **2.19**: grey zone. Action: quarterly review, check order-book concentration, create a second-source qualification plan rather than cancelling business.

### In the news
See news box. The Hackett data on DPO stretching (59 days average) means many suppliers carry more of the chain's cash; combined with 43B(h), buyer treasury and procurement should jointly track supplier liquidity.

### Interview angle
> [!question] How it is asked
> "How would you tell that a tier-1 supplier is about to fail, and what would you do?"

> [!tip] Strong answer includes
> - A blend of quantitative (Z-score, coverage, ratings) and qualitative signals
> - Prioritise by criticality (Kraljic, single-source, switching time) so effort goes where failure hurts most
> - Actions ladder: monitor, support (finance, forecast sharing), de-risk (dual source, buffer), exit
> - Avoid starving a recovering supplier: stretched terms can cause the failure you are trying to prevent

---
## 13. ⭐ Advanced: Greensill and the Failure Modes of Supply Chain Finance
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Greensill Capital** (UK, founded 2011) grew as a leading SCF provider: it bought supplier invoices, packaged them and sold them to investors, notably **Credit Suisse's roughly $10 billion of supply chain finance funds**. It collapsed in March 2021. The sequence, as set out in the UK Parliament's Treasury Committee review: Greensill lost about **$4.6 billion of insurance cover** when the insurer, Tokio Marine, declined renewal (effective 1 March 2021); Credit Suisse suspended the funds; **administrators were appointed on 8 March 2021**.

Failure modes (the lessons):

1. **Not really SCF.** Growth came in **"future receivables"**, invoices for sales not yet made, from 2% to 11% of asset flow by 2020, and in heavy concentration with a single group (GFG Alliance). Financing a hope of future trade is lending, not payables finance.
2. **Insurance dependence.** The investor product assumed credit insurance on weak-credit exposures; withdrawal triggered a run.
3. **Liquidity mismatch.** Daily-liquid funds held assets that could not be sold quickly.
4. **Opacity and regulation gaps.** Programmes sat outside prudential supervision; buyers' liabilities were disguised as trade payables, so analysts could not see debt-like exposure, the origin of the IAS 7/IFRS 7 and ASU 2022-04 disclosure rules.
5. **Reputation.** A buyer whose programme collapses faces a sudden supplier liquidity crisis.

India's TReDS has structural mitigants: regulated platforms, buyer acceptance of each specific invoice, settlement through payment systems, without recourse to the MSME, but financier concentration to big buyers is still a risk.

### Example
A buyer's reverse-factoring programme is ₹400 crore of drawn supplier invoices at year end and its reported trade payables are ₹1,000 crore. The programme lets the buyer pay on day 120 instead of the original day 45, a 75-day extension. If the funder withdraws and suppliers demand the old terms, the cash call is about ₹400 crore × 75/365 ≈ **₹82 crore**. With a ₹100 crore cash buffer the buyer copes; with ₹40 crore it must borrow or delay payments, which then triggers MSME-rule penalties. Stress test = drawn programme balance × days of extension/365.

### In the news
See news box. Disclosure of supplier-finance liabilities is now mandatory under IFRS from 2024; the Greensill story is the standard case behind it.

### Interview angle
> [!question] How it is asked
> "What went wrong at Greensill and how would you design a safe SCF programme?"

> [!tip] Strong answer includes
> - Facts: insurance withdrawal, Credit Suisse funds, administration in March 2021
> - Core point: real SCF finances real, approved, short-tenor trade; Greensill drifted into unsecured future-receivable lending
> - Controls: diversify funders, cap programme size vs buyer liquidity, no uninsured long-tenor exposures, transparency, stress tests
> - Separate lessons for buyer, supplier and investor

---
## 14. ⭐ Advanced: A Working-Capital Diagnostic in a Consulting Case
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A structured approach for a "free up cash" or "reduce working capital" case ([[024 Consulting Frameworks]], [[160 Case Interview - Cost Reduction, Turnaround & Pricing]]):

1. **Baseline**: compute DIO, DSO, DPO, CCC and NTWC as % of sales, by business unit; check seasonality and year-end window dressing.
2. **Benchmark**: against best-in-class peers; the gap in days × value per day gives the **size of the prize**.
3. **Root causes**: forecast bias, over-ordering, long lead times, long setup, product proliferation, billing errors, disputes, poor credit control, weak supplier terms, process fragmentation ([[111 SCOR Model & Supply Chain Process Frameworks]]).
4. **Levers** with value, timing, ease and risk; sequence quick wins (collections, obsolete stock) before structural fixes (S&OP, network).
5. **Financing options** (TReDS, reverse factoring, dynamic discounting, stock finance) after operational fixes, never instead of them.
6. **Sustain**: link to S&OP ([[120 Integrated Business Planning (IBP) & S&OP Maturity]]), set CCC targets in incentives, review monthly.

Always separate one-time release from recurring benefits and check that cash was not simply moved to a supplier or customer.

### Example
Client (FMCG distributor-focused manufacturer): sales ₹2,400 crore, COGS ₹1,800 crore. Current DIO 55, DSO 38, DPO 42 (CCC 51). Peer best-in-class: DIO 42, DSO 30, DPO 55.

- DIO gap 13 days × 1,800/365 = ₹64.1 crore
- DSO gap 8 days × 2,400/365 = ₹52.6 crore
- DPO gap 13 days × 1,800/365 = ₹64.1 crore, but the 45-day rule limits the share of micro and small suppliers, so haircut by say one third → ₹42.7 crore
- Realistic prize ≈ ₹159 crore (64.1 + 52.6 + 42.7) at 70% capture ≈ ₹111 crore, or about 4.6% of sales; interest saving at 10% ≈ ₹11 crore a year.

### In the news
See news box. Regulated invoice platforms and tax rules on MSME payments now sit inside the realistic solution space for any Indian working-capital engagement.

### Interview angle
> [!question] How it is asked
> "A manufacturer's CFO wants ₹100 crore of cash released within 12 months. What is your plan?"

> [!tip] Strong answer includes
> - Size the prize from benchmarks in rupees, then prioritise and phase the levers
> - Operational root causes before financial engineering; costs and risks of each lever
> - Ownership: CCC KPIs for sales, supply chain and procurement, not only for finance
> - One-time vs recurring benefits, and an owner and tracking cadence
