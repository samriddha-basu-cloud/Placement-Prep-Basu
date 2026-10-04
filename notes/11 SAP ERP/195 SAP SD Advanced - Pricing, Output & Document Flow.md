---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP SD Advanced - Pricing, Output & Document Flow"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP SD Advanced - Pricing, Output & Document Flow

⬅ [[194 SAP Production Execution, Confirmation & Product Costing]] · [[_Index - SAP ERP|SAP ERP]] · [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Condition Technique: Building Blocks]]
2. [[#2. Access Sequences, Condition Records & Scales]]
3. [[#3. Pricing Procedure: Worked Calculation with GST]]
4. [[#4. Item Categories & Schedule Line Categories]]
5. [[#5. Copy Control]]
6. [[#6. Partner Functions & Text Determination]]
7. [[#7. Output Determination (NAST to Output Management)]]
8. [[#8. Billing Plans]]
9. [[#9. Rebates, Condition Contracts & Free Goods]]
10. [[#10. Incompletion Procedure]]
11. [[#11. Credit Management (SAP FSCM)]]
12. [[#12. Delivery Scheduling & Route Determination]]
13. [[#13. S/4HANA Advanced ATP (aATP)]]
14. [[#14. ⭐ Advanced: Document Flow, VBFA & S/4HANA Data Model]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Indian tax rule changes land directly in SD pricing, billing and e-invoicing configuration
> **GSTN 30-day e-invoice reporting window extended to AATO ₹10 crore and above (effective 1 April 2025).** Taxpayers with aggregate annual turnover of ₹10 crore or more can no longer report e-invoices older than 30 days from the invoice date; the Invoice Registration Portal rejects them. The rule covers invoices, credit notes and debit notes, and an earlier advisory (13 September 2023) had set the threshold at ₹100 crore. Mandatory e-invoicing itself applies above ₹5 crore turnover. For SD teams this means billing documents must be released to the IRP promptly and failed IRN generation must be monitored daily. ([CAclubindia report on the GSTN advisory](https://www.caclubindia.com/news/gstn-advisory-new-e-invoice-reporting-limit-set-for-businesses-with-aato-of-rs-10-crore-and-above-24084.asp); the thresholds are also summarised by [GSTIN API](https://gstinapi.com/blog/e-invoice-30-day-reporting-limit))
>
> **GST rate restructuring effective 22 September 2025.** After the GST Council's 56th meeting (3 September 2025), the four-slab structure (5/12/18/28%) was consolidated into mainly a 5% merit rate and an 18% standard rate, with a 40% special rate for luxury and sin goods. Every ERP had to change tax condition records (JOIG/JOCG/JOSG/JOUG), material tax classification and, for price-sensitive FMCG items, the **gross-to-net price** logic in pricing procedures. ([PIB press release](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2164586&reg=48&lang=2))
>
> **S/4HANA simplified the SD data model.** SAP's S/4HANA sales course describes the removal of the status tables VBUK/VBUP (status fields now sit in VBAK/VBAP and LIKP/LIPS), replacement of the pricing cluster table KONV by the transparent table PRCD_ELEMENTS, the extension of the document category field VBTYP to VBTYPL, and the retirement of the rebate index VBOX. ([SAP Learning](https://learning.sap.com/courses/functions-innovations-in-sap-s-4hana-sales/identifying-data-model-simplifications-in-sap-s-4hana_fd1c3867-7016-40f1-9e98-3d44a5e81f25))
>
> Sub-topics that say **"See news box"** reuse these items. Basics of the sales cycle are in [[082 SAP SD — Sales & Distribution]]; tax mechanics are in [[227 GST & Indirect Tax for Supply Chains]].

---
## 1. Condition Technique: Building Blocks
> 🔴 Tier 1 · _Key points:_ Condition table, access sequence, condition type, pricing procedure, condition record; same engine for output, text, partner and batch determination

### Definition
The **condition technique** is SAP's generic rule engine: "given these field values in the document, find the matching record and return a value or a decision". Pricing is its best-known use, but output determination, material determination, free goods, batch determination, account determination and text determination all use the same pattern.

Chain of objects (bottom to top):
1. **Condition table:** a key combination of fields, for example *Customer / Material* or *Price list / Material*. Tables are numbered (A304 and so on), created in `V/03`.
2. **Access sequence:** an ordered list of condition tables searched from most specific to most general; the search **stops at the first hit** (unless the exclusive flag is off) (`V/07`).
3. **Condition type:** one pricing element, with a **condition class** (A discount/surcharge, B price, D tax), **calculation type** (percentage, fixed amount, quantity-dependent) and an access sequence (`V/06`).
4. **Pricing procedure:** the ordered recipe that lists condition types with step numbers, subtotals, requirements and account keys (`V/08`).
5. **Condition record:** the actual price/discount with validity dates and scales, maintained in `VK11/VK12/VK13`.

Procedure determination uses four keys: **sales area + customer pricing procedure (customer master) + document pricing procedure (sales document type)**; the result is the pricing procedure used for the document.

### Example
Condition type **K007** (customer discount, percentage) has access sequence K007 → one table keyed on *Customer*. The pricing procedure lists K007 at step 120. At order entry SAP reads the customer number from the order, searches condition records for K007, finds −3% and writes it into the pricing result at step 120.

### In the news
See news box. Each GST rate change forces updates in condition records and, occasionally, in the access sequence for tax conditions (HSN-based rather than material-based).

### Interview angle
> [!question] How it is asked
> "Explain how SAP finds the price in a sales order, from condition table to pricing procedure."

> [!tip] Strong answer includes
> - The five objects in the right order, with one example for each
> - Access sequence stops at first valid record and goes most specific to most general
> - How the pricing procedure itself is determined (sales area, customer and document pricing procedure)
> - Mention that the same technique drives output, text and batch determination, linking it to [[082 SAP SD — Sales & Distribution|the SD overview]]

---
## 2. Access Sequences, Condition Records & Scales
> 🔴 Tier 1 · _Key points:_ Access sequence order, exclusive flag, scales, validity, condition exclusion groups, group conditions

### Definition
- **Access sequence line (access):** table + order number + *exclusive* indicator. Fields in the table must be present in a **field catalogue** and each field is linked to a communication-structure field (KOMK header, KOMP item) via the **field mapping** in the access.
- **Condition record validity:** valid-from and valid-to dates; the system picks the record valid on the **pricing date**.
- **Scales:** a record can hold a *from-scale* (price changes at quantity breaks, e.g. 1–99, 100–499, 500+) or *to-scale* (the whole quantity gets the rate that matches the total). The **scale basis** can be quantity, value or weight, and the scale can be defined as **from-scale** (lower limits) or **to-scale** (upper limits).
- **Condition supplements:** a record can carry extra conditions such as delivery-quantity-based freight.
- **Condition exclusion groups:** two conditions in a group are alternatives and only the best is kept (for example, customer discount vs promotional discount: the customer gets the lower price, never both).
- **Group conditions:** quantity or value across several items in the order is added up before the scale is read (items of one material group share the discount scale).
- **Manual conditions:** the *Manual entry* indicator lets sales reps type a value (for example price override), subject to authorisation.

### Example
Access sequence for **PR00** in one company: (10) customer/material, (20) price list/material, (30) material. A customer without a specific record falls through to a price list, then to the general material price. Scale for the general record of material FG-210: 1–99 units ₹1,300; 100–499 ₹1,250; 500 and above ₹1,200. An order for 50 units is priced at ₹1,300 → ₹65,000; 200 units at ₹1,250 → ₹2,50,000; 600 units at ₹1,200 → ₹7,20,000. In this example the whole order quantity is priced at the rate of the band it reaches, not band by band.

### In the news
See news box. Price lists in FMCG were re-issued across thousands of SKUs after the 22 September 2025 GST rate cuts, so teams that mass-maintained records through BAPIs or the Fiori "Manage Prices" app reduced the effort.

### Interview angle
> [!question] How it is asked
> "A customer says he got the wrong price. How do you trace which condition record was used?"

> [!tip] Strong answer includes
> - Open the pricing screen of the document item and use the condition analysis (the analysis icon shows which table and access hit)
> - Check validity dates versus pricing date, scales, exclusion groups and manual overrides
> - Explain access order and the exclusive flag
> - Mention the preventive control: mass maintenance with approval, plus [[175 Data Quality, Master Data & Data Governance|master data governance]] for price lists

---
## 3. Pricing Procedure: Worked Calculation with GST
> 🔴 Tier 1 · _Key points:_ Step, counter, condition type, from/to, subtotal, requirement, calculation type, statistical, account key; India tax conditions

### Definition
Each line of a pricing procedure has: **step** and **counter** (order of calculation), **condition type**, **from/to** (the base: which earlier steps are summed to form the base for a percentage), **manual** and **mandatory** flags, **statistical** flag (shown but not added to the value, for example cost or pocket price), **subtotal** (stores an intermediate value in a field such as net value, used for statistics and cost), **requirement** (an ABAP routine that decides whether the line runs), **alternative calculation type** and **alternative base value** routines, and **account key** (to FI revenue, discount or freight accounts, see [[190 SAP FI-CO Essentials for Operations Professionals]]).

Sample India procedure (simplified, illustrative):

| Step | Cond. type | Description | Base | Calc |
|---|---|---|---|---|
| 10 | PR00 | Base price | per unit × qty | quantity-dependent |
| 20 | K005 | Customer/material discount | per unit × qty | fixed amount per unit, minus |
| 30 | — | Subtotal 1 | sum 10 to 20 | |
| 40 | K007 | Customer discount | from step 30 | percentage, minus |
| 50 | — | Net value | sum 30 and 40 | subtotal |
| 60 | KF00 | Freight | per shipment | fixed amount |
| 70 | — | Tax base | sum 50 and 60 | |
| 80 | JOIG / JOCG+JOSG | GST on step 70 | from 70 | percentage |
| 90 | — | Total incl. tax | sum 70 and 80 | |

$$\text{Tax} = \text{Tax rate} \times (\text{Net value} + \text{Freight}) \qquad \text{Invoice total} = \text{Tax base} + \text{Tax}$$

### Example
Order: 200 units of FG-210. PR00 = ₹1,250 per unit (100–499 band) → **₹2,50,000**. K005 = −₹40 per unit → −₹8,000, subtotal 1 = **₹2,42,000**. K007 = −3% of 2,42,000 = −₹7,260, net value **₹2,34,740**. Freight KF00 ₹3,000 → tax base **₹2,37,740**. Inter-state sale: IGST 18% = **₹42,793.20**, total **₹2,80,533.20**. For an intra-state sale CGST 9% (₹21,396.60) + SGST 9% (₹21,396.60) gives the same total. With a standard cost of ₹1,000 per unit (₹2,00,000), gross margin on net value = 2,34,740 − 2,00,000 = ₹34,740, i.e. **14.8%**; the statistical cost condition (VPRS) is the usual way to see this in the pricing screen.

### In the news
See news box. After GST 2.0, the same procedure often needed a **new tax condition record at 5% or 40%** per HSN and a re-run of price-list uplift/rollback; a pricing procedure with a clean tax block avoids touching discounts.

### Interview angle
> [!question] How it is asked
> "Here is a price, a discount, freight and GST. Build the pricing procedure and give the invoice value." (Often a whiteboard exercise.)

> [!tip] Strong answer includes
> - The order: gross price, discounts, net value subtotal, freight, tax base, tax, total
> - Correct base for each percentage (from/to), and why tax comes last
> - Statistical lines for cost and margin, account keys for FI, requirements for conditional lines
> - Tax variants: IGST vs CGST+SGST by place of supply (see [[227 GST & Indirect Tax for Supply Chains]])

---
## 4. Item Categories & Schedule Line Categories
> 🔴 Tier 1 · _Key points:_ TAN, TAD, TAS, TATX, TANN; schedule line CP, CN; item category determination; ATP and MRP relevance

### Definition
The **item category** controls how a line behaves: delivery-relevant, billing-relevant, pricing, stock/requirements, whether it is a text item, a free-goods item or a service. **Item category determination** (`VOV4`) combines four keys:

$$\text{Item category} = f(\text{sales document type},\ \text{item category group},\ \text{usage},\ \text{higher-level item category})$$

The **item category group** comes from the material master sales org view (NORM standard item, DIEN service, LEIS non-stock service, BANS third-party), the *usage* is system-set (for example free goods) and the *higher-level item category* is used for sub-items (BOM components, free goods).

Common item categories (standard SAP): **TAN** standard item (delivery and billing relevant, pricing on), **TAD** service (billing only, no delivery), **TAS** third-party item (creates a purchase requisition, billing against invoice), **TATX** text item (no value), **TANN** free of charge item (delivery relevant, not billing relevant), **REN** return item.

**Schedule line category** (`VOV6`) is assigned per item category and MRP type (material master) by schedule line category determination. It controls whether the line is **delivery-relevant**, whether an **availability check** runs, whether a **requirement transfer** occurs to MRP and which movement type is used for goods issue. Standard: **CP** (MRP + ATP check) and **CN** (no MRP, so no requirements); **CS** is used for third-party schedule lines. Each item has one or more schedule lines (confirmed quantity and date).

### Example
Sales order OR for a laptop (NORM) and an AMC service (DIEN). The laptop gets item category TAN with schedule line CP: ATP confirms 50 units on 10 November. The AMC is TAD: no delivery and no schedule lines, billed through the billing plan (see sub-topic 8). If the same customer gets 2 free laptops with 20 purchased, the free ones sit under the main item with TANN and are shipped but not billed.

### In the news
See news box. In S/4HANA the same configuration is retained, but fields moved from status tables into the item table, so reports on item status read VBAP directly.

### Interview angle
> [!question] How it is asked
> "Why is one order line delivered but not billed? Where would you look?"

> [!tip] Strong answer includes
> - Item category flags: delivery relevant, billing relevant, pricing, schedule line allowed
> - Determination keys (document type, item category group, usage, higher item)
> - Schedule line category effect on MRP and ATP
> - Concrete examples TAN, TAD, TAS, TANN and a realistic problem, such as a mis-set item category group

---
## 5. Copy Control
> 🔴 Tier 1 · _Key points:_ VTAA, VTLA, VTFL, VTFA; copying requirements; data transfer routines; pricing type; header, item and schedule-line levels

### Definition
**Copy control** defines what moves from a **source document** to a **target document** when one sales document is created with reference to another. It is configured per pair of document types and item categories at three levels: **header**, **item**, **schedule line** (where relevant).

| Transaction | Copies |
|---|---|
| `VTAA` | Sales document → sales document (quotation → order, order → returns) |
| `VTLA` | Sales document → delivery |
| `VTFA` | Sales document → billing document (order-related billing) |
| `VTFL` | Delivery → billing document (delivery-related billing) |

At each level the settings include: **copying requirements** (a routine that blocks the copy if the source is not in a valid state, for example "quotation must be complete"), **data transfer routines** (what fields are copied or recalculated), **copy quantities** (open quantity, delivered quantity), **document flow update** and, at item level, the **pricing type**:

| Pricing type | Effect on pricing in the target document |
|---|---|
| **B** | Carry out new pricing |
| **C** | Copy manual pricing elements and redetermine the others |
| **D** | Copy pricing elements unchanged |
| **G** | Copy pricing elements unchanged and redetermine taxes |

Billing documents are normally created with **G** or **D**, so that a price agreed at order is not repriced at invoice (a price change after order confirmation never silently changes the customer's bill); for a quotation-to-order step, **B** is common if the price list may have moved.

### Example
A quotation QT at ₹1,250 per unit is valid till 31 October. The customer orders on 20 October: order type OR is created with reference to QT using copy control (VTAA entry QT → OR). With pricing type B the order reprices at today's list; with D the quoted price is protected. The delivery copies the schedule-line confirmed quantity, and the invoice (VTFL, delivery → F2) uses G so that GST is re-determined correctly if the ship-to state is changed by the credit team before billing.

### In the news
See news box. The 22 September 2025 rate change illustrates why pricing type matters: invoices for deliveries made before and billed after the change need explicit tax treatment (tax point rules), not a blind re-pricing.

### Interview angle
> [!question] How it is asked
> "A customer was invoiced at a price different from the order. How can this happen and how do you prevent it?"

> [!tip] Strong answer includes
> - Copy control levels and the four transactions
> - Pricing type (B/C/D/G) and what each does to manual conditions and taxes
> - Copying requirements and data transfer routines for validation
> - Document flow, so that quantities cannot be over-delivered or over-billed

---
## 6. Partner Functions & Text Determination
> 🟠 Tier 2 · _Key points:_ Sold-to, ship-to, bill-to, payer; partner determination procedure; text types; text determination procedure and access sequence

### Definition
**Partner functions** describe who plays which role in a transaction. The four mandatory SD functions are **SP sold-to**, **SH ship-to**, **BP bill-to** and **PY payer**; others include **forwarding agent/carrier** and **sales employee**. Each function belongs to a **partner type** (customer KU, vendor LI, personnel PE, contact person AP).

Determination works through a **partner determination procedure** assigned (a) to the customer account group (master data), (b) to the document header per document type, (c) to the item per item category. Partners are copied from the customer master (sales area data → *Partner functions* tab) into the sales document, and a changed ship-to in the order is a header partner change that may redo pricing and tax. In S/4HANA customers are **business partners**; roles and partner functions are maintained in BP.

**Text determination** uses the condition technique on text objects. Text types (e.g. `0001` material sales text, `0002` header note 1, `Z001` special packing instruction) are grouped in a **text procedure** for a text object (customer header, material, sales document header, item, billing). An **access sequence** tells the system where the text comes from (customer master, material master, copy from previous document). Texts can be copied to delivery and billing and can be printed on forms.

### Example
Customer "Apex Retail": sold-to and payer in Mumbai (corporate); ship-to is the Pune DC; bill-to is the regional office Thane for GST invoices. Because the bill-to GSTIN determines place of supply, a wrong bill-to means wrong IGST vs CGST+SGST. The customer master carries a text "Deliver only between 9 and 5" (customer text), which is copied into the order header and printed on the delivery note.

### In the news
See news box. Place-of-supply accuracy under e-invoicing makes **partner data quality** (GSTIN, state) a first-line control, since the IRP validates the buyer GSTIN.

### Interview angle
> [!question] How it is asked
> "Why do we need ship-to and bill-to separately, and how does SAP decide them in the order?"

> [!tip] Strong answer includes
> - The four functions with a real example involving GST invoicing
> - Procedure assignment at account group, header and item
> - Business partner concept in S/4HANA
> - Text determination as the same technique (text type, procedure, access sequence)

---
## 7. Output Determination (NAST to Output Management)
> 🟠 Tier 2 · _Key points:_ Output type, condition record, medium, partner, dispatch time, NAST; BRF+ output management in S/4HANA

### Definition
**Output** is a document sent to a party: order confirmation, delivery note, invoice, pro-forma. In classic SAP it uses the condition technique with an **output type** (for example `BA00` order confirmation, `LD00` delivery note, `RD00` invoice), an **access sequence** (e.g. sales org + customer), an **output procedure** per document type and **condition records** that store, per partner, the **transmission medium** (1 print, 5 external send e.g. email, 6 EDI, 7 distribution, 8 special function) and the **dispatch time** (send with periodically scheduled job, immediately, or at save). Output items are written to table **NAST** and processed at save or by the output-processing program (RSNAST00); the processing log shows status and errors.

In **S/4HANA** the **output management** framework is the strategic approach: output types are determined by **BRF+** rules and sent through the **Output Control** (Fiori apps such as "Manage Output Items" and "Output Parameter Determination"); forms use **Adobe Forms**. On-premise S/4HANA can still run NAST for compatibility; the cloud editions are built around the new framework. Cross-border India requires an **IRN and QR code** on invoices, which the form must show. Delivery of e-invoices through SAP Business Network or an integration (see [[199 SAP Ariba, SRM & Business Network]]) is another output channel.

### Example
Customer A wants invoice PDFs by email; customer B wants EDI (`INVOIC02`). Both use output type RD00: condition records with medium 5 for A (email address from the partner contact) and medium 6 for B with its EDI partner profile. Delivery notes are printed at the warehouse printer via a condition record for shipping point 1000.

### In the news
See news box. Output must now show the **IRN and QR** after IRP clearance, so the invoice output is triggered only after e-invoice success.

### Interview angle
> [!question] How it is asked
> "A customer did not receive the invoice. How do you troubleshoot output?"

> [!tip] Strong answer includes
> - Check output status (processed, not processed, error), condition record found, output procedure assigned to doc type
> - Partner and medium (email address, EDI profile, printer)
> - Difference between NAST-based and S/4HANA output management with BRF+
> - Link to e-invoicing dependency and a re-issue approach

---
## 8. Billing Plans
> 🔴 Tier 1 · _Key points:_ Periodic vs milestone billing plan; billing dates; billing block; revenue recognition; service and project sales

### Definition
A **billing plan** splits the billing of one order item into **several dates** instead of one invoice per delivery. Two types:
- **Periodic billing:** equal amounts at regular intervals (monthly rent, annual maintenance contract, subscription). The plan type fixes the start/end date, billing rule and calendar.
- **Milestone billing:** the value is split into **partial amounts or percentages**, each tied to a milestone date (for example a project network or a manual date). Dates can be linked to project milestones, each with a **billing block** that lifts when the milestone is complete.

A billing plan is created at the item (item category with billing plan type; typical for TAD) and the **billing index/due list** (`VF04`) creates invoices when the dates arrive. Under **IFRS 15/Ind AS 115**, billing does not equal revenue; the sales/billing dates feed **deferred revenue and unbilled receivable** postings (see [[190 SAP FI-CO Essentials for Operations Professionals]]). S/4HANA's **Revenue Accounting and Reporting (RAR)** automates performance-obligation allocation for contracts that need it.

### Example
Factory automation project ₹60,00,000 (milestone plan): 30% advance on order, 40% on delivery of equipment, 30% on acceptance. Invoices: ₹18,00,000 + GST ₹3,24,000 = **₹21,24,000**; ₹24,00,000 + ₹4,32,000 = **₹28,32,000**; ₹18,00,000 + ₹3,24,000 = **₹21,24,000**. Total GST ₹10,80,000 (18% of ₹60 lakh). AMC example: ₹12,00,000 a year billed monthly gives **₹1,00,000** plus ₹18,000 GST = ₹1,18,000 a month.

### In the news
See news box. Each periodic invoice needs its own IRN within 30 days, so recurring billing runs have to be scheduled with failure handling.

### Interview angle
> [!question] How it is asked
> "How would you bill a project in instalments in SAP, and how do you protect cash flow?"

> [!tip] Strong answer includes
> - Periodic vs milestone plans and the VF04 billing due list
> - Billing blocks tied to milestone completion, and advance billing
> - Revenue recognition difference from billing
> - GST on each instalment and e-invoicing per invoice

---
## 9. Rebates, Condition Contracts & Free Goods
> 🟠 Tier 2 · _Key points:_ Retroactive volume rebate, accruals, settlement; VBO1 vs condition contract management (S/4HANA); inclusive and exclusive free goods

### Definition
**Rebate:** a retroactive discount paid to a customer on the sales volume of a period, with accruals posted at each invoice and settled by a **credit memo** after the period. Classic ECC: **rebate agreement** (`VBO1`), condition type (e.g. `BO01` group rebate), accrual key and the rebate index **VBOX**. **S/4HANA:** the classic rebate processing is replaced by **condition contract management** (part of Settlement Management), which keeps agreements for customer and supplier together, calculates the business volume directly from billing documents without an index, and supports final, partial, delta settlement and delta accruals (create with `WCOCO`, settle with `WB2R_SC`).

**Retroactive scale types:** a scale may apply to the whole volume once a threshold is crossed (retroactive) or only to the volume above the threshold (marginal).

**Free goods:** bonus quantities given with a purchase, determined by the condition technique (condition type `NA00`). **Inclusive:** free quantity is part of the ordered quantity (customer orders 100 and 10 of these are free, so only 90 are billed). **Exclusive:** free quantity is delivered in addition (customer orders 100, pays 100, receives 110). Free goods lines use a free-of-charge item category (see sub-topic 4).

### Example
Distributor sells ₹6.5 crore a year. Agreement: 1% on sales up to ₹5 crore, and **2% on the whole** volume if sales exceed ₹5 crore (retroactive). Rebate = 2% × ₹6.5 crore = **₹13,00,000**; a marginal version (1% on the first ₹5 crore, 2% only on the ₹1.5 crore above) gives ₹5,00,000 + ₹3,00,000 = **₹8,00,000**. Monthly accrual at the average pace is about ₹1,08,333 (₹13 lakh / 12). Free goods: "10 plus 1" rule with 100 ordered, exclusive gives 10 free (ships 110); inclusive: 10 of the 100 are free (bills 90).

### In the news
See news box. The SAP Press overview of condition contract management stresses real-time access to business volume (billing tables VBRK/VBRP) and the end of the VBOX rebuild problem; migration teams must decide which open rebate agreements to settle before cut-over and which to convert (see [[200 SAP S-4HANA Migration, Data Migration & Testing]]). ([SAP PRESS blog](https://blog.sap-press.com/condition-contract-management-with-sap-s4hana))

### Interview angle
> [!question] How it is asked
> "How would you handle a year-end volume rebate in SAP, and what changes in S/4HANA?"

> [!tip] Strong answer includes
> - Accrual at each billing, settlement by credit memo, retroactive vs marginal scales with arithmetic
> - Classic VBO1/VBOX versus condition contract management and Settlement Management
> - Free goods inclusive vs exclusive and the item category
> - Governance: P&L effect of rebate accruals, cut-off at period end, link to [[138 Order Management, Customer Service & Cost-to-Serve]]

---
## 10. Incompletion Procedure
> 🟠 Tier 2 · _Key points:_ Mandatory fields, incompletion log, VOV7, status groups, delivery/billing blocks

### Definition
An **incompletion procedure** defines which fields must be filled before a document may proceed. Each procedure lists fields per **status group** (header, item, schedule line, partner, delivery, billing) and each field has a **warning/error** behaviour and the process step affected (for example "delivery block", "billing block"). A procedure is assigned per sales document type, item category, schedule line category and delivery type in `VOV7` (item category) and related configuration. The **incompletion log** (`Edit → Incompletion log` in `VA02`) lists missing data. The report `V.02` lists incomplete sales orders; incomplete deliveries and invoices have similar reports.

In practice incompletion protects the downstream process: an order without a payment term or incoterms can be saved but not delivered or invoiced until corrected. It is also a data-quality control (see [[175 Data Quality, Master Data & Data Governance]]).

### Example
Export orders must have incoterms and port of loading; the incompletion procedure for order type "export" lists them as mandatory at header level and as a **delivery block** if missing. A sales coordinator saves the order, the log shows "Incoterms missing", the customer service runs `V.02` each morning and clears the list before 2 pm, so shipments are not held at the dock.

### In the news
See news box. IRN generation also needs complete tax data (buyer GSTIN, HSN), so the incompletion check is a cheap early gate before billing.

### Interview angle
> [!question] How it is asked
> "An order cannot be delivered. What blocks do you check?"

> [!tip] Strong answer includes
> - Incompletion log, delivery block, credit block, schedule-line confirmation, shipping point/route determination
> - How incompletion is configured and which reports list incomplete documents
> - Prevention by master-data defaults and mandatory fields
> - Escalation: weekly KPI on incomplete orders

---
## 11. Credit Management (SAP FSCM)
> 🟠 Tier 2 · _Key points:_ Credit segment, exposure, score and rules, automatic check, documented credit decisions; replaced FD32

### Definition
In S/4HANA, classic credit management in FI-AR is replaced by **SAP Credit Management (FIN-FSCM-CR)**, which treats the customer as a **business partner** with a **credit profile**. Main elements:
- **Credit segment:** the unit for which a credit limit is set (a division, region or company-code cluster). A customer can have a different limit per segment. Credit segments are assigned to company codes and linked to the SD credit check configuration.
- **Credit exposure:** open orders + open deliveries + open billing documents + open receivables + special liabilities, updated from SD and FI.
- **Score and rules:** a score from internal rules (payment history, overdue days) or external agencies (for example Dun & Bradstreet) sets the credit limit and a **risk class**; rules define automatic limit proposals.
- **Credit checks in SD:** static or dynamic, **maximum document value**, **critical fields** (payment terms changed), **overdue open items**. They run at order save, delivery creation and goods issue as configured in `OVA8`.
- **Documented credit decisions:** blocked documents create decision records that analysts process in the "Manage Documented Credit Decisions" app, with approval steps; `VKM1` still releases blocks directly. `UKM_BP` replaces `FD32` for maintaining credit data.

$$\text{Available credit} = \text{Credit limit} - \text{Credit exposure} \qquad \text{Utilisation} = \frac{\text{Exposure}}{\text{Limit}}$$

### Example
Customer limit ₹2 crore. Open receivables ₹1.1 crore, open deliveries ₹35 lakh, open orders ₹40 lakh: exposure **₹1.85 crore**, available **₹15 lakh**. New order ₹20 lakh pushes exposure to **₹2.05 crore** (utilisation **102.5%**), so the order is blocked; the credit analyst checks overdue items, takes a ₹10 lakh part payment into account and releases after approval. The same customer in another segment (for example a different division) may still have headroom.

### In the news
See news box. As e-invoicing exposes invoices to tax authorities in near real time, collections and credit controls are tightened by finance teams to keep working capital in check; the technique is explained further in [[136 Supply Chain Finance & Working Capital]]. (SD credit check configuration summary: [SD Vault](https://thesdvault.com/sap-sd-credit-management), a practitioner blog.)

### Interview angle
> [!question] How it is asked
> "How do you prevent bad debt without slowing sales? What changed in S/4HANA?"

> [!tip] Strong answer includes
> - Exposure formula components with the arithmetic and the check points
> - Credit segment, scoring and documented credit decision workflow
> - Release governance, ageing review and DSO, bad-debt KPIs
> - Balancing service levels: partial release, security deposits, advance payment

---
## 12. Delivery Scheduling & Route Determination
> 🔴 Tier 1 · _Key points:_ Backward scheduling; transit time, loading time, pick/pack time, transportation lead time; departure zone, shipping condition, transportation group

### Definition
**Shipping point determination** uses *delivering plant + shipping condition (customer) + loading group (material)*. **Route determination** then finds the route from *country and departure zone of the shipping point + shipping condition + transportation group (material) + country and transportation zone of the ship-to (+ optional weight group)*. The route carries **transit time**, **transportation lead time**, fixed or distance data and the carrier.

**Delivery scheduling** (backward scheduling by default) starts from the **requested delivery date** and subtracts times, using the **shipping point calendar** (factory calendar):
1. **Goods issue date** = delivery date − transit time (route).
2. **Loading date** = goods issue date − loading time (shipping point).
3. **Material availability date** = loading date − pick/pack time (shipping point).
4. **Transportation planning date** = loading date − transportation lead time (route).

If the material availability date is in the past, **forward scheduling** starts from today and moves the delivery date later. The ATP check is made on the material availability date (see sub-topic 13 and [[119 Supply Planning, DRP & Available-to-Promise]]).

### Example
Customer wants delivery on Thursday 5 November 2026. Route: transit time 3 working days, loading time 1 day, pick/pack 1 day, transportation lead time 2 days (all working days). Goods issue: Monday 2 November; loading: Friday 30 October; material availability: Thursday 29 October; transportation planning: Wednesday 28 October. If the plant can supply only from 2 November, forward scheduling moves the loading date and the confirmed delivery date correspondingly.

### In the news
See news box. Quick-commerce and e-commerce promise windows depend on this scheduling logic, adapted to hours rather than days, see [[129 E-commerce & Quick-Commerce Fulfilment]].

### Interview angle
> [!question] How it is asked
> "The customer wants delivery on the 5th; how does SAP decide when to pick and ship?"

> [!tip] Strong answer includes
> - Determination keys for shipping point and route
> - Backward scheduling with the four dates and the calendar
> - Forward scheduling fallback and ATP on the material availability date
> - Linking to transportation planning, see [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]]

---
## 13. S/4HANA Advanced ATP (aATP)
> 🟠 Tier 2 · _Key points:_ Product allocation, backorder processing, alternative-based confirmation, supply protection; performance for mass checks

### Definition
**Advanced available-to-promise (aATP)** is the S/4HANA availability check, running in memory on HANA for sales orders, stock transport orders, production orders, and in other processes. SAP's learning content lists these features:
- **Product allocation (PAL):** distributes scarce products among regions or customers so no single order takes all stock.
- **Backorder processing (BOP):** re-assesses confirmations when supply changes, for example when a high-priority order arrives, an order is cancelled or production is delayed, and redistributes stock by rules.
- **Alternative-based confirmation (ABC):** proposes a substitute product or delivery plant if the requested one cannot be confirmed.
- **Supply protection (SuP):** reserves supply for defined customers or segments so concurrent orders cannot consume it.
- **Optimised mass processing:** checks orders with many items, or production orders with many components, efficiently.

Licensing and scope notes (SAP Learning): advanced ATP is part of standard S/4HANA Cloud licences; the enterprise (on-premise) edition needs a dedicated aATP licence; it cannot be combined with check against planning, catch-weight or active ingredient management.

$$\text{Confirmed qty} = \min(\text{Requested qty},\ \text{ATP qty} - \text{Allocated to others})$$

### Example
Demand for a new smartphone exceeds supply: 10,000 units available this week. Product allocation: 4,000 to e-commerce, 3,000 to modern trade, 3,000 to distributors. An e-commerce order for 5,000 gets only 4,000 confirmed, even though total stock is greater. Later a distributor cancels 500: backorder processing re-runs and confirms 500 more units to waiting e-commerce orders by priority.

### In the news
SAP Learning describes aATP's feature set and its licensing constraints on-premise; teams planning a migration must check the licence and the restrictions before promising aATP functions to the business. ([SAP Learning](https://learning.sap.com/courses/exploring-aatp-in-sap-s-4hana/outlining-advanced-available-to-promise-aatp-in-sap-s-4hana))

### Interview angle
> [!question] How it is asked
> "How would you allocate scarce stock between key accounts and e-commerce in SAP?"

> [!tip] Strong answer includes
> - Product allocation vs supply protection vs BOP, each with its purpose
> - Alternative-based confirmation (substitute product/plant)
> - Business rules and priorities (strategic accounts, contracts), and a monitoring cadence
> - Limits: licence, incompatibilities, link to [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]] and S&OP

---
## 14. ⭐ Advanced: Document Flow, VBFA & S/4HANA Data Model
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Document flow** links every follow-on document to its predecessor. The central table is **VBFA** (sales document flow): each row stores preceding document (**VBELV/POSNV**), subsequent document (**VBELN/POSNN**), document categories (**VBTYP_V, VBTYP_N**), quantities (RFMNG) and values (RFWRT). The standard order-to-cash chain reads: quotation (B) → order (C) → delivery (J) → picking/transfer order → goods issue (R) → invoice (M) → accounting document (FI). Other categories: returns H, credit memo request K, debit memo request L, credit memo O, debit memo P, returns delivery T, scheduling agreement E, contract G, shipment 8.

Header tables: **VBAK/VBAP** (sales order header/item), **LIKP/LIPS** (delivery), **VBRK/VBRP** (billing), **VBKD** (business data), **VBPA** (partners), **VBEP** (schedule lines), **PRCD_ELEMENTS** (pricing results; was KONV), **KONH/KONP/KONM** (condition header/item/scales), **NAST** (output). In S/4HANA: status tables **VBUK/VBUP** are merged into the header/item tables, index tables (VAKPA, VAPMA and others) and **VBOX** are dropped, and **VBTYP** becomes **VBTYPL**. A new **Process Overview** combines document flow and status.

Tracing a quantity difference: start with the sales order, open the *Document flow* button, then drill into the delivery and the invoice; query VBFA for quantities that have been delivered but not billed (open billing), for example with `VA05N`, `VF04` or custom SQL (see [[061 SQL for SCM & Business Analytics]]).

### Example
Order 5000012345 item 10 for 200 units: delivery 80012345 (200), PGI posted, invoice 90012345 (200), accounting document 100012345. A customer claims 180 units received; the VBFA chain shows a return delivery (T) of 20 and a credit memo (O) of 20 units × ₹2,500 = ₹50,000 pending approval. Net billed quantity = 200 − 20 = 180.

### In the news
See news box. The S/4HANA data model simplification reduces joins in reports and makes custom code that read KONV or VBUK need rework in migration projects, see [[200 SAP S-4HANA Migration, Data Migration & Testing]] and [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]].

### Interview angle
> [!question] How it is asked
> "How do you trace a customer's invoice back to the sales order and delivery, and which tables hold this link?"

> [!tip] Strong answer includes
> - Document flow chain with the categories and VBFA key fields
> - Standard tables for header, item, delivery, billing, partners and pricing results
> - S/4HANA changes: status fields merged, KONV to PRCD_ELEMENTS, VBTYPL, no VBOX
> - Practical use: open items reports, delivered-not-billed, reconciliation to FI
