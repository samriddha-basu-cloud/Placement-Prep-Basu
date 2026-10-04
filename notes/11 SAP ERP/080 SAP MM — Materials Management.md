---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP MM — Materials Management"
tier: Tier 1
roles: Operations
status: complete
subtopics: 15
---
# SAP MM — Materials Management

⬅ [[079 SAP Fundamentals & Architecture]] · [[_Index - SAP ERP|SAP ERP]] · [[081 SAP PP — Production Planning]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations

## Sub-topics in this note
1. [[#1. MM Organizational Structure]]
2. [[#2. Material Master (MM01/MM60)]]
3. [[#3. Vendor Master (XK01/MK01)]]
4. [[#4. Purchase Requisition (ME51N)]]
5. [[#5. Request for Quotation (ME41)]]
6. [[#6. Purchase Order (ME21N)]]
7. [[#7. Goods Receipt (MIGO — GR)]]
8. [[#8. Invoice Verification (MIRO)]]
9. [[#9. Goods Issue (MIGO — GI)]]
10. [[#10. Stock Types]]
11. [[#11. Inventory Management Reports]]
12. [[#12. Special Procurement Types]]
13. [[#13. Material Requirements Planning (MD01/MD02)]]
14. [[#14. ⭐ Advanced: Release Strategy (PO Approval) in SAP]]
15. [[#15. ⭐ Advanced: Valuation & Price Control (Standard Price vs Moving Average)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): ECC deadline pushes procure-to-pay onto S/4HANA
> **ECC clock is ticking (Gartner figures, end-2024).** Mainstream maintenance for SAP ERP 6.0 (ECC, EHP 6–8) ends on **31 Dec 2027**, extended maintenance runs to **31 Dec 2030**. Gartner estimated only **39% of SAP's ~35,000 ECC customers (~14,000)** had bought S/4HANA transition licences by end-2024; a Horváth study of 200 SAP companies found only **8% of migrations finished on schedule**. ([SoftwareSeni summary](https://www.softwareseni.com/what-sap-ecc-end-of-support-actually-means-and-why-17000-companies-are-not-ready/); secondary source quoting Gartner and Horváth)
> 
> **GAIL goes live on RISE with SAP (formal launch 25 Jun 2025).** GAIL described itself as the first Maharatna PSU to move from legacy ECC to S/4HANA on cloud ("Navodaya"), done within one year. Procurement and materials are core scope of such programmes. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
> 
> **SAP Q4 2025 (29 Jan 2026).** Current cloud backlog +25% constant currency (+16% reported); 2026 guidance of 23–25% cloud revenue growth; SAP said Business AI featured in about two-thirds of Q4 cloud orders. ([Constellation Research](https://www.constellationr.com/insights/news/saps-q4-cloud-backlog-spurs-concerns))
> 
> Sub-topics that say **"See news box"** reuse these items. Foundations are in [[079 SAP Fundamentals & Architecture]].

---
## 1. MM Organizational Structure
> 🔴 Tier 1 · _Tracker hint:_ Company Code → Plant → Storage Location; Purchasing Org → Purchasing Group

### Definition
MM's org units determine where stock lives and who buys.
- **Company code:** legal entity, FI balance sheet.
- **Plant:** valuation area for inventory (material valuation is normally at plant level), MRP area, and location of stock. A plant is assigned to one company code.
- **Storage location:** quantity-based subdivision within a plant (raw material store, FG store, scrap yard). Stock value is not held per sloc.
- **Purchasing organisation:** negotiates with vendors, owns conditions and contracts; assigned to company code and plants. Variants: **enterprise-level** (for all company codes), **company-code-specific**, **plant-specific**, or **reference purchasing org** (shares conditions).
- **Purchasing group:** buyer or buying team; not an organisational unit assigned to others.

Config path (SPRO, Enterprise Structure): define plant `OX10`, storage location `OX09`, purchasing org `OX08`, assign plant to company code `OX18`, assign purchasing org to company code `OX01`, assign purchasing org to plant `OX17`. If you cannot recall codes, say the principle and the SPRO path.

### Example
Company code 1000; plants 1100 Pune and 1200 Nashik; each has slocs 0001 (RM), 0002 (FG). Purchasing org 1000 buys for both plants. Stock of steel coil in plant 1100/0001 = 500 kg valued at plant 1100's moving average price; 300 kg in 1200/0001 may carry a different price.

### In the news
See news box. In a PSU like GAIL, with many plants and pipelines, a clean plant/purchasing org structure is the base for central procurement.

### Interview angle
> [!question] How it is asked
> "Walk me through the organisational structure used in procurement" or "Where is stock valued, at plant or storage location?"

> [!tip] Strong answer includes
> - Correct order and the assignment rules (plant to one company code)
> - Valuation at plant level, quantity at sloc level
> - Purchasing org variants and central purchasing idea
> - Business example with named plants

---

## 2. Material Master (MM01/MM60)
> 🔴 Tier 1 · _Tracker hint:_ Views: Basic Data, Purchasing, MRP, Storage, Accounting; material type; industry sector

### Definition
The **material master** is the central repository of all data about a material a company buys, makes, stores or sells. It is split into **views**, each maintained by the department that owns it, and at different **organisational levels**.

| View | Typical content | Level |
|---|---|---|
| Basic Data 1/2 | Description, base UoM, material group, weights | Client |
| Sales Org 1/2 | Sales UoM, delivery plant, tax classification | Sales org / distribution channel |
| Purchasing | Purchasing group, order unit, GR processing time | Plant |
| MRP 1–4 | MRP type, lot size, safety stock, planned delivery time, procurement type | Plant |
| Storage 1/2 | Storage conditions, shelf life, batch management | Plant / sloc |
| Quality Mgmt | Inspection type | Plant |
| Accounting 1/2 | Valuation class, price control (S or V), standard price or MAP | Valuation area |

Key control fields: **material type** (ROH raw material, HALB semi-finished, FERT finished goods, HAWA trading goods, VERP packaging, DIEN service) decides which views, number range, and whether the material has a stock account. **Industry sector** (e.g. M mechanical engineering, C chemical, P pharma) decides screen sequence and fields (e.g. batch management for pharma).

T-codes: `MM01` create, `MM02` change, `MM03` display, `MM06` flag for deletion, `MM60` material list (report), `MMBE` stock overview, `MM50` extend (view completeness).

### Example
Creating raw material "HDPE granules" ROH with industry sector M: Basic Data (UoM KG, group RM01), Purchasing (group 002, order unit KG), MRP 1 (MRP type PD, lot size EX), MRP 2 (planned delivery time 7 days, GR processing 1 day), Accounting 1 (valuation class 3000, price control V, MAP initial ₹95). Skipping the MRP view means MRP will never plan it.

### In the news
See news box. Large migrations such as GAIL's rely on migration cockpits to load cleansed material masters; in S/4HANA the product number can be up to 40 characters.

### Interview angle
> [!question] How it is asked
> "What is a material master and what does the MRP view control?" or "What is the effect of material type?"

> [!tip] Strong answer includes
> - Views and which department maintains each
> - Material type effects (ROH/FERT/HAWA) and industry sector
> - Level of data: client, plant, sloc, valuation area
> - Impact of wrong data on MRP and valuation

---

## 3. Vendor Master (XK01/MK01)
> 🔴 Tier 1 · _Tracker hint:_ General data, Company code data, Purchasing org data; payment terms

### Definition
The vendor master holds data about suppliers in three levels:
1. **General data (client level):** name, address, tax numbers (in India GSTIN, PAN), bank details. Same for all company codes.
2. **Company code data (accounting view):** reconciliation account (e.g. payables control), payment terms, payment methods, withholding tax (TDS) info, clearing with customer.
3. **Purchasing organisation data:** order currency, purchase terms, incoterms, **schedule-agreement relevance**, GR-based invoice verification flag, partner functions.

ECC T-codes: `XK01` create centrally, `XK02` change, `XK03` display; `MK01` creates purchasing view only; `FK01` creates accounting view only. In **S/4HANA**, vendors are created as **Business Partners** via `BP` with vendor roles (FLVN00 for FI, FLVN01 for purchasing); the old T-codes are redirected.

**Payment terms** such as "Net 45" or "2/10 net 30" (2% discount if paid in 10 days, else 30) drive cash discount and due dates. The **vendor account group** controls number range and field status; **info records** link vendor-material prices.

### Example
Vendor "Shree Packaging Pvt Ltd": general data with GSTIN and bank; company code 1000 with reconciliation account 160000 and payment terms Net 45; purchasing org 1000 with currency INR, incoterms FCA Pune. Cash discount "2/10 net 30" on a ₹1,00,000 invoice: paying within 10 days costs ₹98,000, saving ₹2,000, equal to roughly 37% annualised return ($2/98 \times 365/20 \approx 37\%$).

### In the news
See news box. Moving to Business Partner is one of the visible changes ECC customers must prepare for during migration.

### Interview angle
> [!question] How it is asked
> "What are the levels of the vendor master?" or "Why would a purchasing org not be able to buy from a vendor?"

> [!tip] Strong answer includes
> - Three levels and what sits in each
> - Reconciliation account and payment terms in the company code view
> - Business Partner in S/4HANA
> - Governance: duplicate checks, bank-detail change approvals (fraud risk)

---

## 4. Purchase Requisition (ME51N)
> 🔴 Tier 1 · _Tracker hint:_ Internal document; created by MRP or manually; not legally binding

### Definition
A **purchase requisition (PR)** is an internal request to purchasing to procure a material or service in a given quantity by a given date. It is **not** an external commitment. It can be created:
- **Automatically** by MRP (`MD01N` or `MD02`), by plant maintenance or production orders (for non-stock components), or by a network.
- **Manually** by users (`ME51N` create, `ME52N` change, `ME53N` display); list via `ME5A` or `ME2N` for PO tracking.

Important fields: material, quantity, delivery date, plant, purchasing group, **account assignment category** (K cost centre, F production order, blank for stock, A asset), and optionally a desired vendor and source list. PRs can have a **release strategy** (approval) if configured. After sourcing, a PR is converted into an RFQ or PO (`ME21N` using the PR selection list, or `ME59N` automatic PO creation).

A **PR status** changes from open (not yet converted) to ordered; an unprocessed PR does not commit money, but may reserve budget if budget control is active.

### Example
MRP finds a shortfall of 500 kg of HDPE for 15 Oct and creates PR 10000456 (plant 1100, group 002). The buyer takes 400 kg from contract vendor A and 100 kg from vendor B: two POs from one PR, with the PR quantities updated accordingly.

### In the news
See news box. Public-sector migrations (GAIL) combine PR approval workflows with e-procurement integration.

### Interview angle
> [!question] How it is asked
> "Difference between PR and PO?" "Who creates a PR and how does it get converted?"

> [!tip] Strong answer includes
> - Internal, non-binding, versus PO as legal commitment
> - Automatic (MRP) and manual creation
> - Account assignment categories and release strategy
> - PR to RFQ/PO and how to track open PRs (ME5A)

---

## 5. Request for Quotation (ME41)
> 🔴 Tier 1 · _Tracker hint:_ Sent to vendors; collect quotations; compare with ME49

### Definition
An **RFQ** is a request sent to potential vendors asking for price and terms for given materials or services. It is part of **sourcing** and does not commit the buyer.
Process:
1. `ME41` create RFQ (can reference PR, a source list, or a previous RFQ); `ME42` change, `ME43` display.
2. Print or send via output control (email/EDI/Ariba).
3. `ME47` maintain the vendor's **quotation** (price conditions, delivery dates, validity).
4. `ME49` **price comparison list** compares quotations by net price, with options such as best price, delivery time.
5. `ME48` display quotation; **rejection letters** are generated to losing vendors; the winning quotation is converted into a PO (`ME21N`) or an info record.

Quotation information can be stored as an **info record** so that later POs get the price automatically. Competitive bidding practice requires at least 3 quotes above a defined value in most firms and PSUs.

### Example
RFQ for 10,000 kg HDPE to three vendors. Quotes: A ₹96/kg, 10 days; B ₹94/kg, 15 days; C ₹95/kg, 7 days. ME49 ranks by price: B lowest (₹9,40,000). If the plant stock-out risk is high, the buyer may award to C (₹9,50,000, 7 days), paying ₹10,000 extra for 8 days earlier delivery. The comparison supports a documented decision.

### In the news
See news box. Large buyers increasingly run RFQs through cloud sourcing tools (SAP Ariba) integrated with S/4HANA, but the basic flow stays the same.

### Interview angle
> [!question] How it is asked
> "How do you choose a vendor in SAP?" or "What is the sequence PR, RFQ, quotation, PO?"

> [!tip] Strong answer includes
> - Full flow with T-codes ME41, ME47, ME49
> - Evaluation criteria beyond price (lead time, quality, payment terms)
> - Info record update and audit trail of the decision
> - When RFQ is skipped (contracts, source list, framework agreement)

---

## 6. Purchase Order (ME21N)
> 🔴 Tier 1 · _Tracker hint:_ Legal contract with vendor; PO types: Standard, Subcontracting, Consignment, Stock Transfer

### Definition
A **purchase order** is a formal, legally binding request to a vendor to supply goods or services under stated conditions. It has a **header** (vendor, purchasing org, group, company code, payment terms, currency), **items** (material, quantity, price, plant, delivery date, account assignment, **item category**), and **confirmations** (vendor acknowledgements).

PO **item categories** (blank = standard):
- **Standard:** normal procurement of stocked material.
- **Subcontracting (L):** components sent to the vendor.
- **Consignment (K):** vendor-owned stock at your site.
- **Stock transfer (U):** between plants of the same company (intra-company), with stock transport orders (STO).
- **Third-party (S):** vendor ships to your customer.
- **Services (D)** and **Limit (B)**.

T-codes: `ME21N` create, `ME22N` change, `ME23N` display, `ME2N/ME2M` reports, `ME28/ME29N` release. Output via NAST (print, email, EDI). **Account assignment** (K, F, A) determines whether the item is expense, stock or asset. The **PO history** logs GR and IR, so open quantity and open value are visible.

### Example
PO 4500001201 to Shree Packaging: 5,000 cartons at ₹40, delivery 20 Oct, plant 1100, payment Net 45. Value ₹2,00,000 plus 12% GST = ₹2,24,000 (the tax code determines input GST posting at invoice verification).

### In the news
See news box. In migration projects, open POs are usually carried over as open items; PO history needs cleaning before the cut-over.

### Interview angle
> [!question] How it is asked
> "What are the different types of PO and when would you use each?"

> [!tip] Strong answer includes
> - PO as a legal document with header/item structure
> - Item categories with a real-life use for each
> - Account assignment and tax determination
> - Release strategy and PO history

---

## 7. Goods Receipt (MIGO — GR)
> 🔴 Tier 1 · _Tracker hint:_ Movement type 101; GR against PO; partial GR; quality inspection stock (movement type 503)

### Definition
A **goods receipt (GR)** records physical receipt of goods, increasing stock and creating a **material document** and an **accounting document**. Done in `MIGO` (action *Goods Receipt*, reference *Purchase Order*).

Key **movement types** (they control stock updates and accounts):

| Mvt type | Use |
|---|---|
| 101 | GR for PO into warehouse (unrestricted, QI, or blocked, depending on inspection and item setup) |
| 102 | Reversal of 101 |
| 103 / 105 | GR into GR-blocked stock / release from it |
| 122 / 161 | Return delivery to vendor (122) and returns for purchase orders (161) |
| 501 / 503 | Receipt without PO into unrestricted (501) or quality inspection stock (503) |
| 321 | Release from QI stock to unrestricted |

Accounting for a valuated GR: **Dr Inventory (BSX), Cr GR/IR clearing (WRX)**. **Partial GR** is allowed; the PO shows delivered quantity and open quantity, and tolerance limits (under/over-delivery) apply. If the material master has an **inspection type 01** active, 101 posts into **quality inspection stock** until the usage decision (QA11) moves it to unrestricted (321) or blocked.

### Example
PO for 1,000 units at ₹50. GR 600 units: material doc updates stock by 600 and posts Dr Inventory ₹30,000 / Cr GR/IR ₹30,000. Next week GR 400 units: another ₹20,000. Total GR/IR credit ₹50,000 awaits the invoice.

### In the news
See news box. Real-time stock updates in S/4HANA (MATDOC) mean a GR is visible to MRP and ATP immediately.

### Interview angle
> [!question] How it is asked
> "What happens in SAP when you post a goods receipt?" or "What is the use of movement type 101 vs 103?"

> [!tip] Strong answer includes
> - Stock update plus accounting entry (Dr Inventory, Cr GR/IR)
> - Movement type concept (101, 102, 122, 321, 501)
> - Partial GR, tolerances and quality inspection stock
> - Reversal rather than deletion

---

## 8. Invoice Verification (MIRO)
> 🔴 Tier 1 · _Tracker hint:_ 3-way match: PO + GR + Invoice; tolerance checks; automatic blocking

### Definition
**Logistics invoice verification (LIV)** matches the vendor invoice to the PO and GR before posting to accounts payable. Done in `MIRO` (enter invoice), blocked invoices released with `MRBR`.

**3-way match:** invoice quantity and price must agree with (a) PO price, (b) quantity received in GR. SAP compares the invoice with the PO price and quantity delivered less quantity already invoiced.

**Tolerance keys** (set in config, e.g. OMR6) define allowed variances: **PP** price variance, **BD** form small differences, **AP** amount for item without order reference, **DQ** quantity variance, **ST** date variance, **PS** price variance (estimated price). If outside tolerance the invoice posts but is **blocked for payment** (reason R for quantity, P for price) until released.

Postings: **Dr GR/IR clearing, Dr Input tax, Cr Vendor payable.** Price differences go to price-difference accounts (PRD for standard price) or adjust inventory under MAP. Other important T-codes: `MR8M` cancel invoice, `MIR4` display, `MR11` GR/IR account maintenance, `MIR7` park invoice.

### Example
PO 100 units at ₹250. GR 90 units. Vendor invoices 100 units at ₹250 = ₹25,000. Invoice quantity (100) exceeds GR (90). Value of GR = 90 × 250 = ₹22,500. SAP posts the invoice with a quantity variance of 10 units (₹2,500). If the DQ tolerance is 5%, 10% is outside, so the invoice is blocked until the remaining 10 units are received or the finance team overrides.

### In the news
See news box. Invoice automation (OCR, e-invoicing IRN under GST) feeds MIRO; the 3-way match is still the control.

### Interview angle
> [!question] How it is asked
> "What is a 3-way match and what happens if it fails?" or "Why is the invoice blocked?"

> [!tip] Strong answer includes
> - PO, GR and invoice compared on quantity and price
> - Tolerances and blocking reasons
> - GR/IR clearing and the accounting entry
> - 2-way match and GR-based IV exceptions (services, evaluated receipt settlement)

---

## 9. Goods Issue (MIGO — GI)
> 🔴 Tier 1 · _Tracker hint:_ Movement type 261 (to production order); 201 (to cost center); 551 (scrapping)

### Definition
A **goods issue (GI)** reduces stock when material leaves the warehouse for consumption, production, scrapping or sale. The movement type fixes the account debited.

| Mvt type | Use | Typical FI posting |
|---|---|---|
| 261 | GI to production order | Dr Consumption / WIP of order, Cr Inventory |
| 262 | Reversal of 261 | opposite |
| 201 | GI to cost centre | Dr Cost centre expense, Cr Inventory |
| 202 | Reversal of 201 | opposite |
| 551 | Scrapping from unrestricted | Dr Scrapping expense, Cr Inventory |
| 311 / 301 | Transfer sloc to sloc, plant to plant (1-step) | no P&L effect |
| 601 | GI for outbound delivery (SD) | Dr COGS, Cr Inventory |

In `MIGO`, action *Goods Issue*, choose reference (order, reservation) or none; a **reservation** (`MB21`) planned in advance supports stock availability. In production, issues can be **backflushed** automatically at order confirmation. Stock rule: GI cannot exceed unrestricted stock unless negative stocks are allowed.

### Example
Issue 50 kg of HDPE (MAP ₹95/kg) to production order 1000450 with 261: stock falls by 50 kg, and ₹4,750 (50 × 95) is debited to the order's material cost. Scrapping 5 kg with 551 posts ₹475 to the scrapping expense account.

### In the news
See news box. In S/4HANA, goods movements read and write to one material document table, which speeds up high-volume issues such as backflushing.

### Interview angle
> [!question] How it is asked
> "Which movement type do you use for issuing material to a production order, and what is the accounting?"

> [!tip] Strong answer includes
> - 261, 201, 551, 601 with the correct purpose
> - Accounting entry per type
> - Reservation concept and backflush
> - Reversal movement types (262, 202)

---

## 10. Stock Types
> 🔴 Tier 1 · _Tracker hint:_ Unrestricted, Quality inspection, Blocked, In-transit, Consignment; movement types

### Definition
Stock is classified by **availability and ownership**:

| Stock type | Meaning | Available for MRP / ATP? |
|---|---|---|
| Unrestricted-use | Free for any use | Yes |
| Quality inspection | Awaiting inspection | Optional (setting) |
| Blocked | Held back (damaged, under investigation) | No |
| Returns | Stock from customer returns | No |
| Stock in transfer / in-transit | Posted out of one plant, not yet received | Shown separately |
| Consignment (vendor-owned) | Located at your site, owned by the vendor until consumed | Yes (as vendor stock) |
| Special stocks | Sales order stock (E), project stock (Q), subcontracting stock at vendor (O) | Yes, for the owner |

Stock changes between types via movement types: 321 QI to unrestricted, 322 unrestricted to QI, 343/344 blocked ↔ unrestricted. Plant-to-plant: 301 (one-step), or 303 then 305 (two-step through in-transit). `MMBE` shows all stock types, `MB52` warehouse stock.

### Example
A pharma plant receives 1,000 boxes. They land in QI stock (101 with inspection). After sampling, 950 pass (321 to unrestricted) and 50 fail (344 to blocked), later scrapped with 551. Only 950 are available to production.

### In the news
See news box. Stock-type logic becomes critical in regulated, high-value flows where traceability and batch status must be accurate.

### Interview angle
> [!question] How it is asked
> "What stock types exist in SAP and how do you move between them?"

> [!tip] Strong answer includes
> - Unrestricted, QI, blocked, in-transit, consignment, special stocks
> - Movement types between them (321/322, 343/344, 301-305)
> - Availability in MRP and ATP per stock type
> - Example showing a quality failure

---

## 11. Inventory Management Reports
> 🔴 Tier 1 · _Tracker hint:_ MB52 (warehouse stocks), MB51 (material documents), MMBE (stock overview)

### Definition
Common reports:

| T-code | Report | Typical question |
|---|---|---|
| `MMBE` | Stock overview (per material, by plant/sloc, batch) | How much stock do we have in each stock type? |
| `MB52` | Warehouse stocks of material (list per plant/sloc with value) | What is the stock value per storage location? |
| `MB51` | Material document list | Who moved this material, when and why? |
| `MB5B` | Stock on posting date | What was stock at month-end? |
| `MB5L` | List of stock values: balances | Reconcile with FI |
| `MD04` | Stock/requirements list | What supply and demand elements exist for this material? |
| `ME2M / ME2N` | PO by material / PO number | What's still open? |
| `MB5T` | Stock in transit | Items shipped but not received |

In S/4HANA Fiori apps replace several (e.g. "Stock – Multiple Materials", "Material Documents Overview", "Slow or Non-Moving Materials"). KPIs derived: **inventory turns** = COGS / average inventory; **days of inventory** = 365 / turns.

### Example
COGS ₹120 crore, average inventory ₹20 crore. Turns = 120 / 20 = 6 times; days of inventory = 365 / 6 ≈ 61 days. `MB5B` gives inventory on 31 March to compute the closing figure; `MB51` traces an unexplained difference of 40 units by listing movements by date.

### In the news
See news box. Real-time reporting on HANA reduces dependence on overnight batch reports, but the report logic is the same.

### Interview angle
> [!question] How it is asked
> "How would you find out why stock is wrong for a material?" "Which T-code shows stock per storage location?"

> [!tip] Strong answer includes
> - MMBE for overview, MB52 for stock list with value, MB51 for movement history
> - Investigation steps: MB51 then document flow to the source transaction
> - KPIs from the data (turns, days of inventory)
> - Mention Fiori equivalents

---

## 12. Special Procurement Types
> 🔴 Tier 1 · _Tracker hint:_ Consignment (pay when consumed), Subcontracting (give material, get back processed), Third-party

### Definition
Standard procurement is "buy and stock". Special types support other flows:
- **Consignment:** vendor owns stock stored at your plant (**PO item category K**, no price on PO line; the info record holds the consignment price). Stock is posted with 101K as vendor consignment stock; liability arises only when you consume or transfer it to own stock, settled in `MRKO`. Benefit: lower working capital and fewer stock-outs.
- **Subcontracting:** you send components to a vendor (provision, movement 541 to subcontracting stock) who processes and returns the finished/semi-finished item (GR 101 for PO item category L). Your liability is only for the **service fee**; you keep ownership of components. The BOM for the subcontracted material supplies component list.
- **Third-party:** you place a PO with a vendor who ships directly to your customer (item category S); no stock in your warehouse; used with SD third-party order (TAS) and a goods receipt/invoice sequence.
- **Stock transfer:** between plants (STO, item category U) with delivery in SD if needed.
- **Pipeline** and **external service** are other variants.

### Example
Tata-style auto plant, consignment of fasteners: vendor stocks 10,000 bolts at your plant; the plant consumes 2,500 in a month at ₹2 each. Liability = 2,500 × 2 = ₹5,000 settled that month via MRKO, while the remaining 7,500 stay on the vendor's balance sheet. Subcontracting: you send 1,000 castings to a machining vendor (541) and pay ₹30 per piece for machining on receipt (₹30,000).

### In the news
See news box. Procurement redesigns during S/4HANA moves often rationalise subcontracting and consignment flows to reduce stock held on the books.

### Interview angle
> [!question] How it is asked
> "Explain consignment vs subcontracting" or "When would you use a third-party order?"

> [!tip] Strong answer includes
> - Ownership and when liability arises
> - Movement types (101K, 541) and item categories (K, L, S, U)
> - Working-capital effect of consignment
> - Real example from automotive or FMCG

---

## 13. Material Requirements Planning (MD01/MD02)
> 🔴 Tier 1 · _Tracker hint:_ Run MRP; planned orders; purchase requisitions auto-created; exception messages

### Definition
**MRP** (Material Requirements Planning) calculates **what to procure or produce, how much and when**, from demand (sales orders, forecasts, planned independent requirements), current stock and open supply.

**Net requirement** = gross requirement + safety stock − available stock − scheduled receipts (open POs/PRs/planned orders). **Procurement proposal** (planned order or PR) is created for the net shortage; the **lot-size procedure** (EX exact, FX fixed, HB replenish to maximum) shapes the quantity and **lead time scheduling** sets the dates (backward from need date).

T-codes: `MD01` (classic total planning), `MD02` (single-item multi-level), `MD03` (single-item single-level), `MD01N` (MRP Live in S/4HANA), **`MD04`** stock/requirements list, **`MD05`** MRP list, **`MD07`** current stock/requirements list, **`MD06`** collective display.

Procurement type in the material master (E in-house, F external) decides whether a planned order (production) or PR (purchase) results. **Exception messages** (reschedule in, reschedule out, cancel, stock below safety stock and others; the numeric codes differ by message and release, so confirm them in MD04 and see [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]]) guide planners; the **planning horizon** and **time fences** control how far MRP plans and when it stops changing firm orders.

### Example
Material HDPE: requirement 500 kg, stock 120 kg, safety stock 50 kg, open PO 200 kg. Net = 500 + 50 − 120 − 200 = **230 kg**. Lot size fixed at 100 kg → PR for 3 × 100 = **300 kg**. Planned delivery time 7 days: PR date = need date − 7 days − GR processing days.

### In the news
See news box. The move to MRP Live on HANA is among the top S/4HANA planning improvements: ECC users move from `MD01` to `MD01N`.

### Interview angle
> [!question] How it is asked
> "How does MRP work?" or "What outputs does an MRP run create and how do planners use them?"

> [!tip] Strong answer includes
> - Net requirement formula with the arithmetic
> - Planned order vs PR by procurement type
> - Lot-size procedure, lead time scheduling and safety stock
> - Exception messages and MD04 as the planner's tool

---

## 14. ⭐ Advanced: Release Strategy (PO Approval) in SAP
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A **release strategy** makes a PO or PR need approval before it can be ordered. It is built on:
- **Release group:** object being released (PR or PO).
- **Release code:** an approver role (e.g. 01 section head, 02 plant head, 03 CFO).
- **Release indicator:** document status (blocked, released).
- **Classification:** characteristic values such as document type, plant, purchasing group, **net order value**. If a document matches the characteristics, the strategy applies.

Approval paths are sequential or parallel via **release prerequisites**. Users approve in `ME28` (collective) or `ME29N` (individual). Config sits in SPRO, Materials Management → Purchasing → Purchase Order → Release Procedure. In S/4HANA Fiori, "Manage Purchase Orders" and flexible workflow replace some of this.

Governance relevance: it supports delegation of authority (DoA), prevents split orders (watch for POs split to dodge thresholds), and creates an approval audit trail.

### Example
PO value thresholds: up to ₹1,00,000 no release (auto); ₹1–10 lakh: purchasing head (code 01); above ₹10 lakh: code 01 then plant head (02) then CFO (03) above ₹50 lakh. A ₹12 lakh PO needs 01 and 02 before the vendor receives it.

### In the news
See news box. Public-sector and listed firms moving to cloud ERP (GAIL) tighten approval and audit controls as part of standardisation.

### Interview angle
> [!question] How it is asked
> "How would you control high-value purchases in SAP?"

> [!tip] Strong answer includes
> - Release strategy structure (group, code, indicator, classification)
> - Thresholds by value and plant with sequential approvals
> - Control against split ordering
> - Link to audit and delegation-of-authority policies

---

## 15. ⭐ Advanced: Valuation & Price Control (Standard Price vs Moving Average)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
In the Accounting view the **price control indicator** decides how stock is valued.
- **S (standard price):** a fixed price (set via costing, e.g. `CK11N/CK24`); every GR and GI posts at the standard price; differences between actual and standard go to **price difference accounts (PRD)**. Typical for manufactured goods (FERT, HALB).
- **V (moving average price, MAP):** the price is recalculated at each GR/IR: $MAP = \frac{\text{total stock value}}{\text{total stock quantity}}$. Typical for purchased raw materials and trading goods.

Account determination uses **valuation class** + **transaction/event keys** (BSX stock, WRX GR/IR, GBB offsetting entries, PRD price differences) configured in `OBYC`. In S/4HANA, the **Material Ledger** is active, enabling actual costing with multiple currencies.

Rule: with S, price difference is not moved into stock; with V, an invoice price difference changes MAP if stock is available, else goes to a price difference account.

### Example
Stock 100 kg at MAP ₹50 (value ₹5,000). GR 50 kg at ₹56 (₹2,800). New MAP = (5,000 + 2,800) / 150 = **₹52**. Under standard price ₹50 the 50 kg would be valued at ₹2,500 and the extra ₹300 (50 × 6) goes to PRD as a price variance, a useful signal for procurement cost.

### In the news
See news box. With inflation and commodity volatility, actual costing in the Material Ledger is a frequent S/4HANA benefit cited by finance teams.

### Interview angle
> [!question] How it is asked
> "Difference between standard price and moving average price? Which would you use for a bolt and a car?"

> [!tip] Strong answer includes
> - S vs V definitions with the MAP formula and a numeric example
> - Price variance accounts under S
> - Which material types use which
> - Link to account determination (OBYC) and Material Ledger

---
## 🔗 Go deeper: expansion notes
- [[191 SAP MM Advanced - Inventory, Batches & Special Stocks|SAP MM Advanced - Inventory, Batches & Special Stocks]]
- [[192 SAP Sourcing & Procurement Deep Dive|SAP Sourcing & Procurement Deep Dive]]
- [[193 SAP MRP Deep Dive - Planning Strategies & Parameters|SAP MRP Deep Dive - Planning Strategies & Parameters]]
- [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows|SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]
