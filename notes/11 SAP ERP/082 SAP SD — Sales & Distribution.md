---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP SD — Sales & Distribution"
tier: Tier 2
roles: Operations
status: complete
subtopics: 13
---
# SAP SD — Sales & Distribution

⬅ [[081 SAP PP — Production Planning]] · [[_Index - SAP ERP|SAP ERP]] · [[083 SAP WM-EWM — Warehouse]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. SD Organizational Structure]]
2. [[#2. Customer Master (XD01/VD01)]]
3. [[#3. Sales Order (VA01/VA02/VA03)]]
4. [[#4. Pricing in SAP]]
5. [[#5. Delivery (VL01N)]]
6. [[#6. Billing / Invoice (VF01)]]
7. [[#7. Order-to-Cash Process]]
8. [[#8. Credit Management]]
9. [[#9. Availability Check (ATP)]]
10. [[#10. Returns Process (VA01 with return order)]]
11. [[#11. SD Reports]]
12. [[#12. ⭐ Advanced: Third-Party & Intercompany Sales]]
13. [[#13. ⭐ Advanced: GST e-Invoicing & E-Way Bill in SD]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): order-to-cash moves to S/4HANA as the ECC deadline nears
> **ECC clock is ticking (Gartner figures, end-2024).** Mainstream maintenance for SAP ERP 6.0 (ECC, EHP 6–8) ends on **31 Dec 2027**, extended maintenance runs to **31 Dec 2030**. Gartner estimated only **39% of SAP's ~35,000 ECC customers (~14,000)** had bought S/4HANA transition licences by end-2024, projecting ~17,000 holdouts by 2027. ([SoftwareSeni summary](https://www.softwareseni.com/what-sap-ecc-end-of-support-actually-means-and-why-17000-companies-are-not-ready/); secondary source quoting Gartner)
> 
> **GAIL goes live on RISE with SAP (formal launch 25 Jun 2025).** GAIL, which sells gas and petrochemicals to industrial customers, described itself as the first Maharatna PSU to move from legacy ECC to S/4HANA on cloud ("Navodaya"), delivered within one year. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
> 
> **SAP Q4 2025 (29 Jan 2026).** Current cloud backlog +25% constant currency (+16% reported); 2026 guidance 23–25% cloud revenue growth; SAP said Business AI featured in about two-thirds of Q4 cloud orders. ([Constellation Research](https://www.constellationr.com/insights/news/saps-q4-cloud-backlog-spurs-concerns))
> 
> Sub-topics that say **"See news box"** reuse these items. Related: [[080 SAP MM — Materials Management]], [[083 SAP WM-EWM — Warehouse]].

---
## 1. SD Organizational Structure
> 🟠 Tier 2 · _Tracker hint:_ Sales Org → Distribution Channel → Division → Sales Office → Sales Group

### Definition
SD structure is built around the **sales area**.
- **Sales organisation:** selling unit responsible for sales and conditions; assigned to one company code.
- **Distribution channel:** route to the customer (retail, wholesale, direct, e-commerce).
- **Division:** product line grouping (e.g. consumer, industrial). Cross-division sales are possible.
- **Sales area** = sales org + distribution channel + division. Every sales document is entered for a sales area; customer and material must be extended to it.
- **Sales office:** physical office of the sales team (assigned to a sales area).
- **Sales group:** team within a sales office (sales reps), used for reporting and responsibility.
- **Shipping point:** place where deliveries are processed (assigned to plant), **loading point**, **plant** (delivering plant determined by customer-material or shipping point).

Assignments to remember: sales org → company code; distribution channel → sales org; division → sales org; plant → sales org + distribution channel (for delivery); shipping point → plant. Mnemonic: "Who sells (sales org), through what route (channel), what products (division)".

### Example
FMCG company: Sales org 1000 (India), channels 10 (general trade), 20 (modern trade), 30 (e-commerce); divisions 01 (foods), 02 (personal care). Sales area 1000/20/01 = foods to modern trade; sales offices Mumbai and Delhi; sales groups per key account manager.

### In the news
See news box. For companies with several channels (quick commerce, modern trade), sales area design is what keeps pricing and credit rules separate.

### Interview angle
> [!question] How it is asked
> "Explain the SD organisation structure" or "What is a sales area?"

> [!tip] Strong answer includes
> - Sales org, channel, division and the sales area combination
> - Sales office and sales group as organisational responsibility
> - Link to plant and shipping point for delivery
> - Example with channels from an Indian FMCG or auto firm

---

## 2. Customer Master (XD01/VD01)
> 🟠 Tier 2 · _Tracker hint:_ General data, Sales area data, Company code data; payment terms; shipping conditions

### Definition
The customer master has three data levels:
1. **General data (client):** name, address, tax numbers (GSTIN, PAN), contact persons, bank. Same across all company codes and sales areas.
2. **Company code data:** reconciliation account (receivables), payment terms, dunning, credit data in FI (`FD32` credit master).
3. **Sales area data:** **customer group, pricing procedure determination, price group, shipping conditions, delivering plant, incoterms, payment terms, partner functions (sold-to, ship-to, bill-to, payer)**, shipping and billing data.

ECC T-codes: `XD01` create centrally, `XD02`, `XD03`, `VD01` sales view only, `FD01` accounting only. In **S/4HANA** the customer is created via **Business Partner** (`BP`) with the customer role (FLCU00 for FI, FLCU01 for sales).

**Partner functions:** SP (sold-to), SH (ship-to), BP (bill-to), PY (payer). One sold-to can have many ship-to's and one payer. **Account assignment group** (customer) combined with the material's account assignment group and sales document type decides revenue accounts in billing.

### Example
Retail chain "Fresh Basket" (sold-to 100234): ship-to for each store DC, payer = head office. Payment terms Net 30, shipping condition "standard", incoterms CIF Pune. Credit limit ₹2 crore stored in credit management.

### In the news
See news box. Merging customers and vendors into Business Partner is a data-migration item for ECC customers moving to S/4HANA.

### Interview angle
> [!question] How it is asked
> "What are the levels of the customer master?" or "Difference between sold-to, ship-to, bill-to, payer?"

> [!tip] Strong answer includes
> - Three levels and what each contains
> - Partner functions with an example
> - Business Partner in S/4HANA
> - How customer data defaults into the sales order

---

## 3. Sales Order (VA01/VA02/VA03)
> 🟠 Tier 2 · _Tracker hint:_ Order type; item category; schedule lines; pricing procedure; availability check

### Definition
A **sales order** is the customer's binding request for goods or services. Create `VA01`, change `VA02`, display `VA03`.

**Document structure:**
- **Header:** order type (OR standard order, QT quotation, IN inquiry, RE returns, CR credit memo request, DR debit memo request, KB consignment fill-up), sales area, partners, payment terms, incoterms, pricing date, credit status.
- **Item:** material, quantity, **item category** (e.g. TAN standard item, TAD service, TAS third-party), pricing, plant, storage location, **requested delivery date**.
- **Schedule line:** confirmed quantity and date after the availability check (category CP for MRP-relevant lines).

Determination: **order type + item category group (from material master) + usage + higher-level item category → item category**; item category + MRP type → schedule line category.

Order-entry checks: **credit**, **availability (ATP)**, **pricing** (via the pricing procedure), **incompletion** log, **partner determination**, **text and output determination**. Copy control manages data flow between documents (quotation → order → delivery → billing).

### Example
Order for 1,000 cartons: item 10, category TAN, requested delivery 20 Oct. ATP confirms 800 on 20 Oct (stock) and 200 on 25 Oct (planned production), creating two schedule lines. The customer's complete-delivery indicator, if set, would push all 1,000 to 25 Oct.

### In the news
See news box. S/4HANA introduces Fiori apps ("Create Sales Orders") and advanced ATP (aATP) options but keeps VA01 logic.

### Interview angle
> [!question] How it is asked
> "What happens when you save a sales order?" or "Explain the structure of a sales document."

> [!tip] Strong answer includes
> - Header/item/schedule line structure and key fields
> - Item category and schedule line category determination
> - Checks: credit, availability, pricing, incompletion
> - Document flow and copy control

---

## 4. Pricing in SAP
> 🟠 Tier 2 · _Tracker hint:_ Condition technique; condition types (PR00=price, K004=discount); pricing procedure

### Definition
SAP pricing uses the **condition technique**:
- **Condition type:** a pricing element, e.g. **PR00** (base price), **K004** (material discount), **K005** (customer/material discount), **K007** (customer discount), **KF00** (freight), **MWST** or in India GST types (JOIG/JOCG/JOSG, etc.).
- **Condition table:** key combination (e.g. customer/material).
- **Access sequence:** ordered search through condition tables, stopping at the first record found (most specific first).
- **Condition record:** the actual value, valid dates, scale (quantity breaks) (`VK11` create, `VK12`, `VK13`).
- **Pricing procedure:** ordered list of condition types with **steps, subtotals, requirements and calculation types** (standard `RVAA01`), determined by **sales area + customer pricing procedure + document pricing procedure**.

Each line: step, counter, condition type, from/to references, **subtotal**, **statistical** flag, **account key** for FI. Condition classes: A discount, B price, D tax. Amounts can be absolute, percentage or per unit.

Net price calculation example: $\text{Net} = \text{Gross} - \text{discounts} + \text{surcharges}$, then tax is added to get invoice value.

### Example
100 units, PR00 ₹1,000 each = ₹1,00,000. K004 −5% = −₹5,000 → ₹95,000. Freight KF00 ₹2,000 → ₹97,000. GST 18% on ₹97,000 = ₹17,460 → invoice total **₹1,14,460**. For an intra-state sale, CGST 9% + SGST 9% = ₹8,730 + ₹8,730; inter-state uses IGST 18%.

### In the news
See news box. Complex tax and e-invoicing rules in India make accurate pricing procedure and tax determination a standard consulting deliverable in every SD rollout.

### Interview angle
> [!question] How it is asked
> "Explain how SAP determines the price for a sales order."

> [!tip] Strong answer includes
> - Condition type, table, access sequence, record, procedure chain
> - Examples PR00, K004, tax
> - How the pricing procedure is determined
> - Why access sequences prioritise specific over general prices

---

## 5. Delivery (VL01N)
> 🟠 Tier 2 · _Tracker hint:_ Picking; goods issue (GI) from warehouse; delivery type; shipping point

### Definition
An **outbound delivery** is the document that triggers physical shipment: picking, packing and goods issue. Create `VL01N` (with reference to sales order), `VL02N` change/post goods issue, `VL03N` display; collective processing `VL10` (delivery due list), monitor `VL06O`.

Steps:
1. **Delivery creation:** shipping point, delivery type (LF standard delivery, LR returns delivery), route determination, weight/volume.
2. **Picking:** generates a transfer order in WM/EWM or a pick list; picked quantity confirmed in the delivery (`VL02N` picking tab) or `LT12`.
3. **Packing:** handling units.
4. **Post goods issue (PGI):** movement type **601**; stock reduces, **Dr COGS, Cr Inventory**; delivery status becomes "goods issue completed" and the order becomes billing-relevant.
5. Reversal: `VL09` cancels PGI (movement 602).

Determination: **shipping point = shipping condition + loading group + plant**. Delivery blocks and **incoterms** affect process.

### Example
Order 1,000 cartons; picking confirms 800 (partial). PGI for 800 at standard cost ₹120 → COGS Dr ₹96,000, Inventory Cr ₹96,000. Remaining 200 is delivered in a second delivery after the production receipt.

### In the news
See news box. Faster, real-time stock updates in S/4HANA help avoid over-promising and shorten pick-to-ship cycle.

### Interview angle
> [!question] How it is asked
> "What happens during post goods issue?" or "How is the shipping point determined?"

> [!tip] Strong answer includes
> - Delivery steps: create, pick, pack, PGI
> - Movement type 601 and its accounting
> - Shipping point determination logic
> - Reversal and partial delivery handling

---

## 6. Billing / Invoice (VF01)
> 🟠 Tier 2 · _Tracker hint:_ Billing type; account determination; posting to FI; credit memo

### Definition
**Billing** creates the customer invoice and posts revenue to FI. `VF01` create, `VF02` change, `VF03` display, `VF04` billing due list, `VF11` cancel billing document.

Key features:
- **Billing types:** F2 invoice, F5 pro forma (order-related), G2 credit memo, L2 debit memo, S1 cancellation of invoice, IV intercompany invoice.
- **Billing relevance** is set at item category level (delivery-related or order-related).
- **Account determination (VKOA):** revenue accounts chosen by **chart of accounts + sales org + customer account assignment group + material account assignment group + account key**.
- **Posting to FI:** Dr Customer receivable (reconciliation account), Cr Revenue, Cr Output tax (GST). A **accounting document** is created and **document flow** is updated.
- **Billing block** and **billing plans** (milestone, periodic) for contracts or projects.

In India the billing document is also the base for **e-invoicing** (IRN, QR code) and **e-way bill**, integrated via GST add-ons.

### Example
Invoice for ₹97,000 + 18% GST (₹17,460) = ₹1,14,460: Dr Customer ₹1,14,460, Cr Revenue ₹97,000 (via VKOA), Cr Output GST ₹17,460. A credit memo (G2) for ₹5,000 + GST ₹900 reverses part: Dr Revenue ₹5,000, Dr Output GST ₹900, Cr Customer ₹5,900.

### In the news
See news box. As India's GST e-invoicing thresholds expand, billing documents must integrate with the government portal in real time.

### Interview angle
> [!question] How it is asked
> "What is account determination in billing?" or "Difference between F2 and G2?"

> [!tip] Strong answer includes
> - Billing types and relevance
> - Account determination keys (VKOA)
> - FI posting entry
> - Cancel with S1 or VF11, and credit memo flow

---

## 7. Order-to-Cash Process
> 🟠 Tier 2 · _Tracker hint:_ Sales Order → Delivery → Post GI → Invoice → Payment — end-to-end flow

### Definition
**Order-to-Cash (O2C)** is the end-to-end cycle from customer inquiry to cash collection.

| Step | SAP | Output / effect |
|---|---|---|
| Pre-sales | Inquiry (VA11), quotation (VA21) | Document with prices |
| Sales order | VA01 | Checks: credit, ATP, pricing; creates demand for MRP |
| Delivery | VL01N | Picking, packing |
| Post goods issue | VL02N | Stock down (601), COGS posted |
| Billing | VF01 | Invoice, revenue, receivable |
| Payment | F-28 (incoming payment) or automatic | Clears receivable, updates credit exposure |

Key controls: credit limit, availability, **delivery and billing blocks**, **document flow** for traceability. KPIs: **order cycle time**, **DSO** (days sales outstanding) = receivables / revenue × days, **OTIF**, **perfect order rate**, **billing accuracy**, **credit memo rate**.

Integration: SD with MM (stock, procurement), PP (make-to-order), FI (revenue, cash), CO (profitability analysis, COPA), QM and WM.

### Example
Order ₹10 lakh on day 0; delivery on day 3; invoice on day 3; customer pays on day 38 (Net 30 + 5 days late). Order-to-cash time = 38 days. DSO for a company with ₹5 crore receivables and ₹40 crore annual revenue: $5/40 \times 365 \approx 45.6$ days.

### In the news
See news box. Faster, AI-assisted collections and dispute management are among SAP's cloud push areas.

### Interview angle
> [!question] How it is asked
> "Walk me through order-to-cash in SAP and where it can break."

> [!tip] Strong answer includes
> - Sequence with documents and T-codes
> - Accounting entries at GI and billing
> - Typical failure points: credit block, no stock, wrong pricing, missing master data
> - KPIs: cycle time, DSO, OTIF

---

## 8. Credit Management
> 🟠 Tier 2 · _Tracker hint:_ Credit limit check; credit exposure; release blocked orders (VKM1)

### Definition
**Credit management** limits the risk of selling to customers who cannot pay. In classic SD:
- **Credit limit** per customer or credit control area (`FD32` maintain credit master).
- **Credit exposure** = open orders + open deliveries + open billing documents + open items (receivables) + special liabilities (e.g. bills of exchange).
- **Credit check types:** simple check (static: compares exposure with limit), automatic check (dynamic over horizon), by risk category and credit group. Checks occur at order save, delivery creation and post goods issue as configured (`OVA8`).
- **Credit block:** order is saved with a block; credit manager reviews and releases in `VKM1` (blocked SD documents), `VKM3` (list of sales orders).

$\text{Available credit} = \text{credit limit} - \text{credit exposure}$.

In **S/4HANA**, FI-AR credit management is replaced by **SAP Credit Management (FIN-FSCM-CR)** with the business partner as credit account, scoring and rules.

### Example
Customer limit ₹50 lakh; open receivables ₹30 lakh, open deliveries ₹5 lakh, open orders ₹10 lakh → exposure ₹45 lakh. New order ₹8 lakh → exposure ₹53 lakh > ₹50 lakh, order blocked. Credit manager releases partially in VKM1 after receipt of a ₹5 lakh payment.

### In the news
See news box. Working-capital pressure raises the importance of automated credit scoring and dispute management in cloud ERP.

### Interview angle
> [!question] How it is asked
> "How do you prevent bad debt in an O2C process?"

> [!tip] Strong answer includes
> - Credit exposure components and formula
> - Check points and block/release process
> - Credit master and risk categories; S/4HANA Credit Management
> - Balance: sales growth vs credit risk, with KPIs (DSO, bad-debt %)

---

## 9. Availability Check (ATP)
> 🟠 Tier 2 · _Tracker hint:_ Check against stock, inbound deliveries, planned orders; confirmed quantities

### Definition
**Available-to-promise (ATP)** checks, at order entry, whether the requested quantity can be delivered by the requested date and confirms quantities in schedule lines.

$\text{ATP quantity} = \text{warehouse stock} + \text{planned receipts} - \text{planned issues}$.

Elements counted are controlled by the **checking group** (material master, MRP 3) and **checking rule** (per transaction, e.g. sales order = A) plus the **requirements class**. Typical inclusions: unrestricted stock, safety stock (optional), purchase orders, planned orders, production orders, **reservations and other requirements** (as issues), and the **replenishment lead time (RLT)** (if no supply is known). Options: **check without RLT, with RLT**, **availability overview** (`CO09`), **backorder processing** (`V_RA`) to redistribute stock.

Delivery proposals: **one-time delivery**, **complete delivery**, **delivery proposal**. In S/4HANA **advanced ATP (aATP)** adds product allocation, alternative-based confirmation and supply protection.

### Example
Stock 80 units today; planned production receipt 50 units on Friday. Customer requests 100 on Wednesday. ATP confirms 80 on Wednesday; 20 on Friday (two schedule lines). If the customer insisted on complete delivery, the single line would be confirmed 100 on Friday.

### In the news
See news box. Faster real-time stock visibility and aATP in S/4HANA improve delivery promises, especially for high-demand allocation.

### Interview angle
> [!question] How it is asked
> "How does SAP confirm delivery dates in a sales order?"

> [!tip] Strong answer includes
> - ATP formula and what supply and demand elements count
> - Checking group and checking rule
> - Partial vs complete delivery trade-off
> - aATP and allocation in constrained supply

---

## 10. Returns Process (VA01 with return order)
> 🟠 Tier 2 · _Tracker hint:_ Return order → Return delivery → Credit memo; movement type 651

### Definition
Customer returns are handled via a **returns order** (order type **RE**), created in `VA01`, often with reference to the original invoice. Sequence:
1. **Return order** (RE): reason, quantity, price reference; may be **blocked** for approval (billing block / delivery block).
2. **Return delivery** (delivery type **LR**, via `VL01N`): customer goods physically received. Posting **goods receipt** into stock: movement type **651** is the standard returns movement for the return delivery (the stock may land in blocked or returns stock depending on configuration; variants 653/655/657 exist).
3. **Credit memo** (billing type **G2**, via `VF01`) reverses revenue and tax: Dr Revenue, Dr Output tax, Cr Customer.
4. Inspection and decision: restock, rework, scrap, vendor return.

Related: **credit memo request (CR)** for price adjustments without goods; **replacement delivery**; **free-of-charge delivery**. Reason codes and **returns authorization** limit abuse. For retailers returns can be 20–30% in online fashion, so process cost matters.

### Example
Customer returns 100 defective units sold at ₹500 + 18% GST. Return order RE for 100 units; return delivery with GR into blocked stock (651); credit memo ₹50,000 + ₹9,000 GST = ₹59,000. After inspection, 60 are reworked and returned to unrestricted stock, 40 scrapped (movement 551, cost 40 × ₹300 standard cost = ₹12,000 expensed, assuming a ₹300 standard cost).

### In the news
See news box. High returns in e-commerce make returns automation (RMA, refunds) a cost lever for retailers on S/4HANA.

### Interview angle
> [!question] How it is asked
> "Describe the returns process in SAP SD with accounting impact."

> [!tip] Strong answer includes
> - RE, LR, G2 document sequence
> - Stock movement (651) and the credit memo's FI effect
> - Quality decision and disposition
> - Controls: approval, reason codes, time limits

---

## 11. SD Reports
> 🟠 Tier 2 · _Tracker hint:_ VA05 (list of sales orders), VF05 (list of billing documents), VA35 (scheduling agreements list)

### Definition
Standard SD lists (selection by customer, material, date, status):

| T-code | Report |
|---|---|
| `VA05` | List of sales orders |
| `VA15 / VA25` | List of inquiries / quotations |
| `VA35` | List of scheduling agreements |
| `VA45` | List of contracts |
| `VF05` | List of billing documents |
| `VF04` | Billing due list |
| `VL06O` | Outbound delivery monitor |
| `VL10` | Delivery due list |
| `VKM1` | Blocked SD documents (credit) |

Fiori and embedded analytics in S/4HANA provide analytical apps (sales volume, open orders, billing blocks) built on CDS. Typical KPIs: **order backlog**, **fill rate**, **on-time delivery**, **sales by customer/material**, **blocked order value**, **average days to invoice**.

### Example
Month-end check: `VA05` for orders with "open" status shows ₹3.2 crore not delivered; `VF04` shows ₹1.1 crore of delivered but not invoiced items (a revenue leakage risk); `VKM1` shows ₹40 lakh blocked for credit. Together they give the sales finance team a to-do list.

### In the news
See news box. Embedded analytics in S/4HANA reduces dependence on offline Excel extracts for these lists.

### Interview angle
> [!question] How it is asked
> "How would you find all delivered but unbilled orders?"

> [!tip] Strong answer includes
> - Right T-code per question (VA05, VF04, VF05, VKM1)
> - Concept of billing due list and revenue leakage
> - Fiori and analytics alternatives
> - Turning report output into action (follow-ups, blocks)

---

## 12. ⭐ Advanced: Third-Party & Intercompany Sales
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Third-party order processing:** the company sells an item it does not stock; item category **TAS** generates a **purchase requisition** automatically on order save; the vendor ships directly to the customer. Flow: sales order → PR → PO (`ME21N`) → vendor delivers → **GR/invoice receipt** at the company (MIRO) → billing to the customer (VF01). Billing is triggered by invoice receipt, so the **margin** is the difference between sales price and purchase price.

**Intercompany sales:** one company code (selling) sells to a customer; another company code (delivering plant) ships. After delivery, the delivering company bills the selling company at the **transfer price** (intercompany billing type IV, condition PI01), and the selling company bills the customer (F2). Needs: correct company-code to plant assignment, **transfer pricing** and GST handling (inter-state, different GSTINs).

Both flows test integration across SD, MM and FI and appear in consulting case studies on **drop-ship** and **group sales** structures.

### Example
Third party: customer price ₹12,000, vendor price ₹9,500; margin ₹2,500 (20.8%). Intercompany: Company A (sales) sells for ₹12,000; delivering company B bills A at ₹10,000 (transfer price); A bills customer ₹12,000. A's margin is ₹12,000 − ₹10,000 = ₹2,000, i.e. $2000/12000 = 16.7\%$; B earns its own margin on the ₹10,000 transfer price over its cost.

### In the news
See news box. Group structures (e.g. PSUs with subsidiaries) on S/4HANA need robust intercompany processes and eliminations.

### Interview angle
> [!question] How it is asked
> "A distributor does not hold stock for a rare item. How would you model that in SAP?"

> [!tip] Strong answer includes
> - TAS flow with PR/PO and invoice-triggered billing
> - Margin calculation and risk (supplier delays, quality)
> - Intercompany billing with transfer price and tax
> - Drop-ship vs stocking decision (service level vs working capital)

---

## 13. ⭐ Advanced: GST e-Invoicing & E-Way Bill in SD
> ⭐ Advanced · _Added beyond the tracker_

### Definition
In India, B2B invoices of eligible taxpayers must be registered on the **Invoice Registration Portal (IRP)** to receive an **Invoice Reference Number (IRN)** and a signed QR code; this is **e-invoicing**. It applies to businesses above an aggregate annual turnover threshold (it was lowered in stages, reaching ₹5 crore from 1 Aug 2023; verify the current threshold on the GST portal). The **e-way bill** is required for movement of goods above ₹50,000 consignment value (with exemptions and state rules).

SAP implementation: after billing (VF01), the system calls the IRP via **SAP Document and Reporting Compliance (e-Document framework)** or add-on, stores IRN and QR in the billing document, and prints it on the invoice. Failures (invalid GSTIN, HSN missing) block or delay billing. Credit notes also need IRN; cancellation allowed within a limited time window.

Data prerequisites: customer GSTIN in master data, material **HSN codes**, correct tax code determination (intra-state CGST+SGST vs inter-state IGST), place of supply.

### Example
Invoice ₹1,00,000 for a product with an 18% GST rate: GST = ₹18,000 (the HSN code decides the rate). IRN is generated within seconds; if the customer's GSTIN is invalid, VF01 shows an error status, and billing posts but the e-document stays "rejected" until corrected.

### In the news
See news box. For Indian rollouts like GAIL's, statutory compliance (GST, e-invoicing) is a non-negotiable scope item in design.

### Interview angle
> [!question] How it is asked
> "What master data and process steps are needed for GST e-invoicing in SAP SD?"

> [!tip] Strong answer includes
> - IRN, IRP, QR code, e-way bill basics
> - Data quality: GSTIN, HSN, place of supply
> - Error handling and reconciliation (GSTR-1/2B)
> - State thresholds as assumptions to verify

---
## 🔗 Go deeper: expansion notes
- [[195 SAP SD Advanced - Pricing, Output & Document Flow|SAP SD Advanced - Pricing, Output & Document Flow]]
- [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)|SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]]
- [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows|SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]
