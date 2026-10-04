---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "Order Management, Customer Service & Cost-to-Serve"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 13
---
# Order Management, Customer Service & Cost-to-Serve

⬅ [[137 Supply Chain Contracts & Game Theory]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[139 Product Design & Supply Chain - DFSC, Postponement & Complexity]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. The Order-to-Cash (O2C) and Order Fulfilment Process]]
2. [[#2. Order Promising, Allocation and Backorders]]
3. [[#3. Customer Service Levels and SLAs]]
4. [[#4. Perfect Order Index and Its Composition]]
5. [[#5. Order Cycle Time and Its Components]]
6. [[#6. The Service-Cost Trade-Off Curve]]
7. [[#7. Cost-to-Serve and the Customer Profitability Waterfall]]
8. [[#8. The Whale Curve and Customer Segmentation by Service]]
9. [[#9. Customer-Centric Supply Chain Design]]
10. [[#10. Returns, Credit and Deductions]]
11. [[#11. Retail OTIF Fines and Vendor Compliance]]
12. [[#12. ⭐ Advanced: Time-Driven Activity-Based Costing for Cost-to-Serve]]
13. [[#13. ⭐ Advanced: Recovering Cost-to-Serve Through Pricing, Terms and Service Menus]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): faster promises meet higher delivery costs, so cost-to-serve is back on the agenda
> **Nordstrom pushes delivery speed (Sept 2026).** Nordstrom said it is pursuing consistent **seven-day-a-week delivery** across its carrier mix, already offers next-day and two-day delivery in some areas, and piloted **same-day delivery of beauty products in Los Angeles (order by 3 p.m., delivered by 9 p.m.)** with plans to extend to further markets in fall 2026. Faster service tiers carry a cost that must be priced or segmented. ([Supply Chain Dive](https://www.supplychaindive.com/news/nordstrom-eyes-weekend-delivery-faster-shipping/831511/))
>
> **Carrier costs rise into peak season (Sept 2026).** Supply Chain Dive reported US diesel at **$6.53 per gallon on 21 September 2026, up 24 cents in a week**, and new peak-season fees from USPS, FedEx, UPS and Amazon running from September through January. One shipper quoted (People's Choice Beef Jerky) uses three to four carriers, accepting slightly higher postage as protection against peak-season disruption, and a carrier executive said saving two to three dollars or more per order on shipping fees frees up meaningful capital. ([Supply Chain Dive](https://www.supplychaindive.com/news/carrier-diversity-key-to-holiday-success-in-a-high-cost-environment/831027/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. The Order-to-Cash (O2C) and Order Fulfilment Process
> 🔴 Tier 1 · _Key points:_ Order capture to cash collection, hand-offs, where errors and delay arise

### Definition
**Order-to-cash (O2C)** is the end-to-end process from a customer's order to cash in the bank. Typical stages:

1. **Order capture**: EDI, portal, app, salesperson, phone/WhatsApp; validate customer, price, terms, MOQ.
2. **Order entry and validation**: master-data checks, pricing and discounts, tax (GST) determination, **credit check**.
3. **Order promising**: availability-to-promise (ATP), delivery date commitment, allocation.
4. **Fulfilment**: pick, pack, quality check, load, dispatch; shipping documents and e-way bill ([[227 GST & Indirect Tax for Supply Chains]], [[010 Warehouse Management]]).
5. **Delivery and proof of delivery (POD)**.
6. **Invoicing and billing**: accurate, e-invoice generated.
7. **Collections, cash application and dispute resolution**.
8. **Returns, claims and credit notes**.

Owned by different functions (sales, customer service, supply planning, warehouse, logistics, finance), so most failures happen at **hand-offs**. Systems: ERP order and billing modules ([[082 SAP SD — Sales & Distribution]], [[195 SAP SD Advanced - Pricing, Output & Document Flow]]), WMS/TMS, e-invoicing portals. In SCOR ([[111 SCOR Model & Supply Chain Process Frameworks]]) this is the **Deliver** process (order management is a core element of D1/D2/D3).

### Example
A Nashik FMCG company processes 1,20,000 distributor orders a year. Audit finds 8% need manual correction (wrong price list, missing GST number, credit block). At ₹400 per exception handled, that is 9,600 × ₹400 = **₹38.4 lakh a year**, plus a 1.5-day delay per exception. Cleaning price and customer master data ([[175 Data Quality, Master Data & Data Governance]]) is the cheapest route to a faster O2C.

### In the news
See news box. Speed promises (same-day, seven-day delivery) depend on order capture, picking and carrier hand-off all being in order, not only on the last mile.

### Interview angle
> [!question] How it is asked
> "Walk me through order-to-cash and tell me where you would look first if customers complain about late and wrong deliveries."

> [!tip] Strong answer includes
> - The stages from capture to cash, and ownership of each
> - Measuring each stage (order entry time, order accuracy, pick accuracy, POD time, invoice accuracy, dispute rate)
> - Hand-off failures: master data, credit holds, allocation rules, warehouse cut-offs
> - Link to DSO: billing and delivery errors delay payment

---
## 2. Order Promising, Allocation and Backorders
> 🔴 Tier 1 · _Key points:_ ATP/CTP, promise date, allocation rules, backorder vs lost sale

### Definition
**Order promising** commits a quantity and date to the customer:

- **ATP (available-to-promise)**: uncommitted stock plus planned receipts, net of committed orders, until the next planned supply. Discrete ATP in the first period = on hand + scheduled receipt − customer orders up to the next receipt ([[119 Supply Planning, DRP & Available-to-Promise]]).
- **CTP (capable-to-promise)**: ATP plus the uncommitted production capacity and materials that could be used to make the product.
- **Global ATP / multi-location ATP**: sources the order from the best node (service vs cost).

When supply is short, **allocation rules** decide who gets stock: pro-rata to forecast, to historic share, by customer priority or segment, or first-come-first-served. Rules based on past sales (not on orders) discourage order inflation ([[114 Bullwhip Effect, Beer Game & Information Sharing]]).

**Backorder vs lost sale**: a backorder keeps the order and ships later (cost: expediting, split shipments, customer irritation); a lost sale loses the margin and may lose the customer. Policies: **ship-complete** (hold until all lines available), **ship-available** (partial shipments), **substitution** (offer a compatible SKU), **cancel**.

### Example
On hand 200 units, with receipts of 500 in week 2 and 500 in week 4. Customer orders already promised: week 1: 150, week 2: 120, week 3: 200, week 4: 180.

- Week 1 ATP = 200 − 150 = **50** (until the next receipt in week 2)
- Week 2 ATP = 500 − (120 + 200) = **180** (covers weeks 2-3, until the receipt in week 4)
- Week 4 ATP = 500 − 180 = **320**

A new order for 200 units for week 2 cannot be met in full: week 2 ATP is 180, so the options are a split promise (180 in week 2 and the remaining 20 from week 4's ATP of 320) or a full promise for week 4.

### In the news
See news box. Same-day and next-day promises make promise dates visible to the customer, so the quality of the ATP logic is now a customer-facing metric.

### Interview angle
> [!question] How it is asked
> "A key customer orders 1,000 units but you can ship only 600 this week. What do you do?"

> [!tip] Strong answer includes
> - Check allocation policy, customer segment and contractual penalty exposure
> - Options: partial ship, substitute, expedite production or transfer, split delivery, offer a date
> - Cost comparison (expediting cost vs penalty vs lost margin)
> - Communicate early with a firm new date; fix the root cause in the S&OP or inventory plan

---
## 3. Customer Service Levels and SLAs
> 🔴 Tier 1 · _Key points:_ Cycle service level vs fill rate; line/unit/case fill; SLA metrics and penalties

### Definition
Customer service is measured on **availability, timeliness, accuracy and responsiveness**. Common metrics:

- **Cycle service level (CSL)**: probability of no stock-out in a replenishment cycle (a planning parameter linked to safety stock, see [[003 Inventory Management]]).
- **Fill rate**: fraction of demand met from stock. Variants: **unit fill**, **line fill**, **order fill** (complete orders), **case fill** (retail).
- **On-time (OT), in-full (IF), OTIF**: delivery on the promised date and quantity; define the **window** (for example the appointment slot) and the **basis** (customer request date vs promise date).
- **Order accuracy, damage rate, response time, claims resolution time**.

A **service level agreement (SLA)** formalises metric, measurement method, target, reporting frequency, exclusions (force majeure, customer-caused delays) and remedies (credits, fines, termination rights). Fill rate and CSL differ: with lot size $Q$ and expected shortage per cycle $ESC = \sigma_L \cdot L(z)$,

$$\text{Fill rate} = 1 - \frac{ESC}{Q}$$

### Example
Lead-time demand standard deviation $\sigma_L$ = 100 units, order quantity $Q$ = 500.

| CSL | $z$ | Safety stock | Expected shortage per cycle | Fill rate |
|---|---|---|---|---|
| 90% | 1.28 | 128 | 4.73 | 99.05% |
| 95% | 1.64 | 164 | 2.09 | 99.58% |
| 99% | 2.33 | 233 | 0.34 | 99.93% |

A "95% service" promise by CSL corresponds to a **99.6% unit fill rate** here, so check which one the customer means. Case fill and line fill will be lower than unit fill because shortages concentrate on a few lines.

### In the news
See news box. Faster delivery promises are service levels on the timeliness dimension; they must be written into SLAs with realistic measurement windows.

### Interview angle
> [!question] How it is asked
> "A customer demands 99% service. What do you ask before agreeing?"

> [!tip] Strong answer includes
> - Clarify the definition: CSL vs fill rate vs OTIF, window, measurement basis, and which SKUs
> - Cost of the target (extra safety stock, capacity, premium transport) and who pays
> - Exclusions and remedies in the SLA, plus review cadence
> - Segment by customer and SKU: not everyone needs 99%

---
## 4. Perfect Order Index and Its Composition
> 🔴 Tier 1 · _Key points:_ Product of component rates; compounding effect; diagnosis by component

### Definition
The **perfect order** is an order delivered **on time, in full, damage-free and with accurate documentation** (SCOR Reliability attribute RL.1.1 "perfect order fulfilment" uses the same logic: all items, quantities, date, documents and condition right). The **perfect order index** is the product of the component rates:

$$POI = \text{On-time} \times \text{In-full} \times \text{Damage-free} \times \text{Documentation-accurate}$$

If components are independent the index compounds downwards quickly: four components at 97% each give 88.5%, not 97%. Variants add "correct invoice" and "correct channel/label". Use it to track end-to-end reliability across functions and to find the weakest component; see KPIs in [[012 Supply Chain Analytics & KPIs]].

### Example
Monthly measures: on-time 96%, in-full 97%, damage-free 99%, documentation accurate 98%.

POI = 0.96 × 0.97 × 0.99 × 0.98 = **90.3%**. So out of 10,000 orders, about **965 are imperfect** even though no single component is below 96%.

Improvement scenario: raise in-full from 97% to 99%, giving 0.96 × 0.99 × 0.99 × 0.98 = 92.2%. Rank projects by component gap multiplied by cost per failure (a late delivery vs a damaged delivery vs a wrong invoice delaying payment by weeks).

### In the news
See news box. Higher peak surcharges and speed promises raise the cost of every imperfect order, because re-delivery is a second delivery at peak rates.

### Interview angle
> [!question] How it is asked
> "What is the perfect order rate and why can it be low when each KPI looks fine?"

> [!tip] Strong answer includes
> - Definition and the multiplicative structure with a number (90.3% from four 96-99% rates)
> - Root causes by component and the owning function
> - Cost of imperfection: re-delivery, credit notes, disputes, lost customer
> - Caveat: measure orders (not lines) consistently and agree the definition with the customer

---
## 5. Order Cycle Time and Its Components
> 🔴 Tier 1 · _Key points:_ Elapsed time from order to delivery; variability matters more than the mean

### Definition
**Order cycle time (OCT)** or order-to-delivery lead time is the elapsed time from customer order to receipt. Components:

- **Order transmission** (customer to supplier)
- **Order entry, validation and credit approval**
- **Order processing and release** (allocation, wave planning)
- **Picking, packing, staging and loading**
- **Transit** (line-haul, cross-dock, last mile)
- **Delivery, unloading and receipt, POD**

OCT should be tracked as **mean and variability**: customers hold safety stock against variability, so a 6-day cycle that varies between 4 and 9 days is worse than a steady 7-day cycle. Compress by parallel processing (credit check and allocation together), cut-off time extension, order-batching rules, pre-positioning stock closer to demand ([[113 Network Design & Facility Location Modelling]], [[009 Logistics & Distribution]]), and eliminating hand-offs. Contrast **customer order decoupling point**: the later the point where orders trigger activity, the longer the OCT (make-to-order vs make-to-stock; see [[005 Production & Operations Planning]]).

### Example
A distributor's OCT, in days: transmission 0.5, entry and credit check 0.5, pick and pack 1.0, loading and dispatch 0.5, transit 3.0, receipt 0.5 = **6.0 days**.

- Assume moving the daily dispatch cut-off from 12 noon to 4 p.m. converts about half the orders from next-day to same-day dispatch, saving 0.5 day on average.
- Assume automated credit approval cuts the entry and credit step by 0.4 days.
- New OCT about **5.1 days**, a 15% reduction without touching transit. The customer's required safety stock falls roughly with the lead-time variation, so the benefit shows up in the customer's inventory, a selling point.

### In the news
See news box. Seven-day and same-day delivery attack the processing and transit components; the dispatch cut-off is the cheapest lever.

### Interview angle
> [!question] How it is asked
> "A customer says our delivery takes too long. How do you break down and shorten the order cycle?"

> [!tip] Strong answer includes
> - The component list with measured times, mean and variability
> - Quick wins in order processing, cut-offs and parallelisation before expensive transit upgrades
> - Segmenting by customer need (not everyone values speed)
> - Link between lead-time variability and safety stock

---
## 6. The Service-Cost Trade-Off Curve
> 🔴 Tier 1 · _Key points:_ Diminishing returns, rising cost at the top end, find the economic level by segment

### Definition
Logistics cost rises **more than proportionally** with service level, while revenue benefit flattens: the last few points of availability cost far more than the first. The economic service level is where the **marginal cost of service equals marginal benefit** (retained margin, avoided penalties, loyalty). With normal demand, safety stock is $SS = z\sigma_L$, and $z$ grows ever more slowly with each extra point of CSL: 90%→95% adds 0.36 sigma, 95%→99% adds 0.68, 99%→99.9% adds 0.76. Other cost drivers: expedited freight, standby capacity, higher warehouse density of stock, more nodes.

Different customers deserve different points on the curve: **differentiated service** by segment ([[112 Supply Chain Strategy - Fit, Segmentation & Maturity]]). A common mistake is a blanket 98-99% target "because the competitor does".

### Example
$\sigma_L$ = 100 units, holding cost ₹25 per unit-year (SKU unit cost ₹100).

| CSL | $z$ | Safety stock | Annual holding cost |
|---|---|---|---|
| 90% | 1.28 | 128 | ₹3,204 |
| 95% | 1.64 | 164 | ₹4,112 |
| 98% | 2.05 | 205 | ₹5,134 |
| 99% | 2.33 | 233 | ₹5,816 |
| 99.9% | 3.09 | 309 | ₹7,726 |

Going from 95% to 99% adds 68 units and **₹1,703 a year (+41%)** per SKU for 4 more points of CSL. On 5,000 such SKUs that is about **₹85 lakh a year**. If the incremental 4 points of CSL are worth only ₹12 per SKU in avoided lost margin, the move does not pay, unless the SKU belongs to a critical customer.

### In the news
See news box. As delivery speed and peak-season surcharges rise, customers tolerate fewer promises that cost more than they are worth.

### Interview angle
> [!question] How it is asked
> "Should we raise our service level from 95% to 99%?"

> [!tip] Strong answer includes
> - Show diminishing returns with numbers (safety stock and cost)
> - Compare marginal cost to marginal value (lost margin, penalties, retention)
> - Differentiate by segment and SKU role (A items and critical customers vs tail)
> - Offer non-inventory routes: faster replenishment, better forecasts, postponement

---
## 7. Cost-to-Serve and the Customer Profitability Waterfall
> 🔴 Tier 1 · _Key points:_ Revenue to net profit after service-driven costs; activity-based drivers; price vs gross margin illusion

### Definition
**Cost-to-serve (CTS)** measures the full cost of serving a given customer, channel or product, beyond COGS, using **activity drivers** (orders, lines, cases, drops, kilometres, returns, calls, days of credit). Gross margin hides this: two customers with the same gross margin can differ widely in profit once order handling, picking, freight, returns, payment terms and account management are loaded ([[110 Cost Accounting for Operations]]). The **waterfall** goes: gross sales, less discounts and trade spend, = net sales, less COGS = gross margin, less order processing, handling, freight, compliance fines, returns, credit cost, key-account cost = **customer net profit**.

Cost of credit uses the working-capital link: $\text{Credit cost} = \text{Revenue} \times r \times \frac{DSO}{365}$ ([[136 Supply Chain Finance & Working Capital]]).

### Example
Illustrative rate card: order processing ₹1,500 per order, handling ₹8 per case, credit cost 11% a year. ₹ lakh unless stated.

| | A: Modern-trade chain | B: Wholesaler | C: Direct small retailers |
|---|---|---|---|
| Revenue | 500 | 300 | 100 |
| COGS | 350 | 225 | 70 |
| **Gross margin** | 150 (30%) | 75 (25%) | 30 (30%) |
| Trade spend / rebates | 40 | 15 | 6 |
| Order processing | 3.6 (240 orders) | 1.8 (120) | 12.0 (800 orders) |
| Handling | 4.8 (60,000 cases) | 3.2 (40,000) | 0.64 (8,000) |
| Freight | 3.0 (₹5 per case) | 1.6 (₹4) | 1.76 (₹22) |
| Retailer fines and chargebacks | 5.0 | 0 | 0 |
| Returns and credit notes | 10.0 (2%) | 3.0 (1%) | 4.0 (4%) |
| Credit cost | 9.0 (60 days) | 4.1 (45 days) | 0.9 (30 days) |
| Key-account cost | 6.0 | 2.0 | 3.0 |
| **Net profit** | **68.6 (13.7%)** | **44.3 (14.8%)** | **1.7 (1.7%)** |

Customer C earns the same 30% gross margin as A but only **1.7% net**, because ₹1,500 per order on 800 small orders swamps it. Actions: minimum order value or case-multiple pricing, drop-size surcharge, move to a distributor or e-B2B app, one delivery day a week. Total across the three customers: ₹900 lakh revenue, ₹114.6 lakh net profit (12.7%).

### In the news
See news box. Nordstrom's push to faster delivery and the peak surcharge story are cost-to-serve increases that a customer-level analysis lets a firm price or segment rather than absorb.

### Interview angle
> [!question] How it is asked
> "Our biggest customer is also our least profitable. How do you prove it and what do you do?"

> [!tip] Strong answer includes
> - Build the waterfall by customer with activity drivers (orders, lines, cases, drops, returns, credit days)
> - Distinguish avoidable and unavoidable cost; avoid arbitrary allocation
> - Actions: pricing and terms, service-level menu, minimum orders, channel shifts, fix root-cause errors
> - Handle the relationship risk: share the data with the customer and offer a path to better terms

---
## 8. The Whale Curve and Customer Segmentation by Service
> 🔴 Tier 1 · _Key points:_ Cumulative profit by ranked customer peaks above 100%, tail destroys value; segment, then act

### Definition
The **whale curve** (profit concentration curve) ranks customers from most to least profitable and plots **cumulative profit as % of total profit** against % of customers. The curve rises above 100%, peaks, and falls back to 100% because unprofitable customers erode profit. The height above 100% shows how much profit is lost to the tail; humps well above 100% are often reported for businesses with many small accounts (an empirical pattern, not a law).

Use: **segment** customers by profit and strategic value, and pick the action:

| Segment | Profile | Action |
|---|---|---|
| **Protect and grow** | High profit, high potential | Priority service, joint planning |
| **Fix** | Large revenue, low profit | Re-price, change terms, reduce service cost |
| **Migrate** | Small, costly to serve direct | Move to distributor, digital channel, self-serve |
| **Exit or reprice** | Negative, no strategic value | Raise price, minimum order or exit |

Check the strategic value before exit (reference customers, volume that absorbs fixed cost, adjacencies).

### Example
Ten customers ranked by profit (₹ lakh): 60, 45, 30, 20, 10, 5, 0, −5, −15, −25. Total = ₹125 lakh.

| Customers | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Cumulative profit | 60 | 105 | 135 | 155 | 165 | 170 | 170 | 165 | 150 | 125 |
| As % of total | 48% | 84% | 108% | 124% | 132% | 136% | 136% | 132% | 120% | 100% |

The curve peaks at **136%** with the top 6 customers: the bottom 3 customers destroy ₹45 lakh (36% of the final profit). Fixing them to break-even (or repricing) raises total profit from ₹125 lakh to ₹170 lakh, about +36%.

### In the news
See news box. Higher carrier costs make the tail of small, scattered deliveries more costly, widening the whale curve's hump.

### Interview angle
> [!question] How it is asked
> "What is a whale curve and how would you use it with a client?"

> [!tip] Strong answer includes
> - Describe the plot and why it exceeds 100%
> - Link to cost-to-serve data as the input
> - Segment-based actions rather than blanket exits
> - Cautions: allocation assumptions, strategic customers, one-year snapshot

---
## 9. Customer-Centric Supply Chain Design
> 🔴 Tier 1 · _Key points:_ Design service by customer needs; Indian channels; service menu; fit

### Definition
A **customer-centric** supply chain starts from what each segment values (speed, availability, order flexibility, information, price, sustainability) and designs fulfilment, inventory, network and terms to match, instead of one uniform service. Steps: **segment** customers by needs and profit; **define the service menu** (standard, premium, economy) with price signals; **design the physical flow** (forward stock locations, direct-to-store, cross-dock, e-fulfilment); **set inventory policy by segment**; **align metrics and incentives** ([[112 Supply Chain Strategy - Fit, Segmentation & Maturity]]). Technology: order orchestration, distributed order management, visibility, control towers ([[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]).

Indian context: a manufacturer may serve **modern trade** (DC deliveries, appointment slots, OTIF compliance), **general trade** (distributor-led, credit-based, small drops), **e-commerce marketplaces** (strict ASN and packaging rules), **quick commerce** (frequent small replenishments to dark stores) and **institutional or export** customers, each with a different service-cost profile ([[130 FMCG & Retail Distribution - India Route-to-Market]], [[129 E-commerce & Quick-Commerce Fulfilment]]).

### Example
A paint company serves dealers with one service model: 48-hour delivery from a regional depot, free freight above ₹25,000. Analysis shows 20% of dealers order below ₹10,000 and generate 4% of revenue but 30% of delivery cost. New design: three tiers: **Gold** (top dealers, 24-hour delivery, vendor-managed replenishment), **Standard** (48 hours, free freight above ₹40,000), **Basic** (weekly route delivery or via sub-dealers, freight charged under ₹10,000). Outcome: delivery cost per order falls, large dealers get faster service and small ones still buy, via a lower-cost path.

### In the news
See news box. Nordstrom's carrier mix (national plus regional carriers) is an example of matching delivery capability to local market needs rather than a single network.

### Interview angle
> [!question] How it is asked
> "How would you redesign a supply chain around customer segments?"

> [!tip] Strong answer includes
> - Segment by needs and profit, not by size alone
> - A service menu with prices, so customers choose and pay for premium service
> - Matching inventory and network to each segment
> - Change management: sales incentives and customer communication

---
## 10. Returns, Credit and Deductions
> 🔴 Tier 1 · _Key points:_ RMA, returns cost, credit limits, disputes and short payments, link to DSO

### Definition
**Returns management**: authorisation (RMA), reason codes (damage, wrong item, expired, overstock, customer remorse), inspection and disposition (restock, refurbish, liquidate, scrap) and credit-note issuance. Returns costs include reverse freight, handling, inspection, markdown and the lost sale; link [[135 Reverse Logistics, Remanufacturing & EPR in India]]. Control by return policies (time windows, caps, restocking fees) and root-cause fixes upstream (packaging, picking accuracy).

**Credit management**: credit limit set by customer risk (financials, payment history, bureau score), credit holds, security (bank guarantee, letter of credit), insurance, dunning. The cost is **working capital**: DSO × revenue × cost of money. For India, the **MSME payment rule** applies when the *buyer* is you and the *supplier* is an MSE (see [[136 Supply Chain Finance & Working Capital]]); if you are an MSME selling to a corporate buyer, tools like TReDS shorten your DSO.

**Deductions and short payments**: customers (especially retailers) pay less than the invoice for claimed shortages, damages, fines or promotions; a large share is invalid. Deduction management (root cause, dispute, recover) is a profit lever.

### Example
A firm with ₹400 crore turnover has 3% of invoice value disputed or short paid: **₹12 crore a year**. Assume 40% of that (₹4.8 crore) is invalid and recoverable, and a dedicated deductions desk wins 75% of those disputes: ₹3.6 crore recovered. Desk cost is ₹40 lakh a year, so the net gain is **₹3.2 crore**. Faster resolution adds cash: cutting average dispute resolution from 40 to 25 days on ₹12 crore frees ₹12 × 15/365 = **₹0.49 crore**.

### In the news
See news box. Peak-season delivery failures and surcharge disputes add to short pays and returns, and the cost of reverse and re-delivery trips rises with fuel.

### Interview angle
> [!question] How it is asked
> "Returns and short payments are eating margin. Where do you start?"

> [!tip] Strong answer includes
> - Quantify by reason code and customer (Pareto)
> - Root-cause upstream (picking errors, packaging damage, wrong pricing)
> - Policy levers: windows, restocking fees, authorisation, inspection at source
> - Process levers: deductions desk, POD evidence, quick dispute resolution

---
## 11. Retail OTIF Fines and Vendor Compliance
> 🔴 Tier 1 · _Key points:_ Retailer scorecards, percentage fines on non-compliant cases, appointment windows, supplier response

### Definition
Large retailers run **vendor compliance programmes** (Walmart's OTIF programme is the best-known US example; modern-trade chains and e-commerce marketplaces in India run similar scorecards): suppliers must deliver the right cases, **on time within an appointment window** and with accurate labels, ASNs and packaging. Misses attract **fines or chargebacks**, typically a **percentage of the cost of goods of the non-compliant order or case**, with a target OTIF threshold and sometimes a grace band. The retailer's logic: stock-outs and receiving disruption at its DCs are costly. The supplier's challenge: OTIF is computed by the retailer, windows are narrow, and root causes can sit on either side (retailer-caused delays, carrier issues).

Supplier response: baseline OTIF by customer and reason code; fix root causes (order accuracy, ASN/label compliance, transport planning, appointment adherence); **dispute invalid fines** with POD, timestamps and retailer-caused delays; **buffer stock** for tight-target customers; negotiate windows and measurement rules; price the compliance cost into terms. Link to perfect order (sub-topic 4) and cost-to-serve (sub-topic 7). Specific rates, targets and windows change by retailer and year, so confirm in the current vendor manual before quoting.

### Example
Stylised programme: fine = 3% of the cost of goods of non-compliant cases; supplier ships ₹20 crore of COGS a month to the retailer with **9% non-compliant**.

- Monthly fine = 20 crore × 9% × 3% = **₹5.4 lakh**; annual **₹64.8 lakh**.
- A root-cause programme cuts non-compliance to 4%: fine = 20 × 4% × 3% = ₹2.4 lakh a month, saving **₹36 lakh a year**.
- If 30% of fines are invalid and 70% of those get recovered, the recovery is a further ₹64.8 × 30% × 70% ≈ ₹13.6 lakh on the baseline.
- Extra safety stock to hit the target (₹50 lakh at 20% carrying cost = ₹10 lakh a year) is cheaper than the fines it prevents.

### In the news
See news box. Tighter delivery windows and higher peak fees raise both the likelihood of misses and the cost per miss, so compliance performance needs executive attention before peak season.

### Interview angle
> [!question] How it is asked
> "A retailer is fining us 3% of COGS for OTIF misses. How would you respond?"

> [!tip] Strong answer includes
> - Quantify fine exposure and baseline OTIF by reason code and DC
> - Root-cause fixes plus dispute process for invalid fines
> - Compare cost of compliance (stock, planning, transport) with cost of fines and lost business
> - Negotiate measurement rules and windows; consider customer-specific service models

---
## 12. ⭐ Advanced: Time-Driven Activity-Based Costing for Cost-to-Serve
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Traditional activity-based costing (ABC) needs surveys of how people spend time. **Time-driven ABC (TDABC)**, introduced by Kaplan and Anderson, simplifies it using two parameters:

$$\text{Capacity cost rate} = \frac{\text{Cost of capacity supplied}}{\text{Practical capacity (minutes or hours)}}$$

$$\text{Activity cost} = \text{Capacity cost rate} \times \text{Time per unit of activity}$$

Time equations capture complexity: handling time = base time + extra time for each special feature (phone vs EDI, expedite, custom label, manual credit check). The approach gives **order-level and customer-level cost**, is easy to update, and exposes idle capacity (unused practical capacity is a cost of capacity, not allocated to customers). Pitfalls: poor time estimates, inconsistent capacity definition, and treating fixed cost as avoidable. TDABC links to [[110 Cost Accounting for Operations]] and budgeting variances in [[225 Budgeting, Variance Analysis & Balanced Scorecard]].

### Example
A customer service department costs ₹60 lakh a year (salaries, systems, space), with 8 agents at 1,600 productive hours each = 12,800 hours.

- Capacity cost rate = 60,00,000 / 12,800 = **₹468.75 per hour** = **₹7.81 per minute**.
- EDI order: 2 minutes = **₹15.63**; phone order: 12 minutes = **₹93.75**; expedite request: 30 minutes = **₹234.38**.
- Customer X places 600 phone orders and 40 expedite requests a year: 600 × 93.75 + 40 × 234.375 = 56,250 + 9,375 = **₹65,625**.
- If all orders move to EDI: 600 × 15.625 + 9,375 = 9,375 + 9,375 = **₹18,750**; saving about **₹46,900** a year, a basis for an EDI-only price tier.

### In the news
See news box. Where carrier and fuel costs jump quickly, rate-card style driver costing (cost per drop, per case, per minute) lets firms reprice service tiers in weeks.

### Interview angle
> [!question] How it is asked
> "How would you cost a customer's service-related activities without a year-long ABC project?"

> [!tip] Strong answer includes
> - Capacity cost rate and a few time equations per activity
> - Use available data (order system, WMS, TMS) as drivers
> - Separate cost of used capacity from idle capacity
> - Pilot on the top and bottom customers, then scale

---
## 13. ⭐ Advanced: Recovering Cost-to-Serve Through Pricing, Terms and Service Menus
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Once cost-to-serve is known, the commercial levers are (1) **price**: list price adjustments, order-handling fees, drop-size surcharges, rush fees; (2) **terms**: minimum order values, case or pallet multiples, order cut-offs, delivery frequency, payment terms (including early-payment discount versus credit cost), return caps; (3) **service menu**: a priced choice among service tiers; (4) **channel shift**: route low-volume customers via distributors or digital self-serve; (5) **cost reduction**: consolidate deliveries, standard routes, pick-and-pack improvements, EDI adoption.

Good practice: **pocket price waterfall** (list price to pocket price after discounts, rebates and CTS); transparent rate cards; phased implementation and communication; guard against competitor poaching; legal checks (Competition Act on discriminatory pricing and trade-practice rules). Make sure the service menu is **self-selecting**: customers who value speed pay for it. Link to pricing in cases ([[160 Case Interview - Cost Reduction, Turnaround & Pricing]]) and profitability case technique ([[025 Case Interview — Profitability]]).

### Example
Using Customer C from sub-topic 7 (revenue ₹100 lakh, net profit ₹1.7 lakh): 800 orders a year at an average ₹12,500 each.

- Introduce a **₹1,000 fee on orders below ₹10,000** (assume 40% of orders, 320 orders, and half of them consolidate into larger or fewer orders): 160 orders pay the fee = ₹1.6 lakh; 160 orders are consolidated, saving 160 × ₹1,500 = ₹2.4 lakh of order cost.
- Move delivery from daily to twice a week for the same customers: freight falls 20% (₹0.35 lakh).
- Net profit improves from ₹1.7 lakh to about **₹6.1 lakh** (1.7 + 1.6 + 2.4 + 0.35), a margin of about 6%. Risk: some customers leave; check that lost contribution (30% gross margin on the volume lost) stays below the gains.

### In the news
See news box. As delivery costs increase, retailers and brands are moving towards fee-based or tiered delivery offers, the retail version of a service menu.

### Interview angle
> [!question] How it is asked
> "Having shown customer C is unprofitable, what would you recommend and what is the risk?"

> [!tip] Strong answer includes
> - A ranked set of levers: price, terms, channel, cost, with expected rupee impact
> - Estimating customer response (volume lost, competitor reaction) and the break-even volume loss
> - Sequencing and communication, pilots by region
> - Governance: owners, tracking of realised pocket margin
