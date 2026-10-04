---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP FI-CO Essentials for Operations Professionals"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP FI-CO Essentials for Operations Professionals

⬅ [[085 SAP Reporting & Analytics]] · [[_Index - SAP ERP|SAP ERP]] · [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. FI Organisational Structure & Chart of Accounts]]
2. [[#2. General Ledger Posting & the Document Principle]]
3. [[#3. Accounts Payable (AP) and TDS/GST]]
4. [[#4. Accounts Receivable (AR) and Credit Control]]
5. [[#5. Asset Accounting (FI-AA)]]
6. [[#6. Controlling Basics: Cost Centres, Cost Elements & Allocations]]
7. [[#7. Profit Centres and Internal Orders]]
8. [[#8. CO-PA: Profitability Analysis]]
9. [[#9. Automatic Account Determination for Goods Movements (OBYC)]]
10. [[#10. GR/IR Clearing and Price Variances]]
11. [[#11. Material Ledger and Actual Costing]]
12. [[#12. Period-End Closing: FI, MM, CO and ML Sequence]]
13. [[#13. Integration of MM, SD and PP with FI-CO: Worked Journal Entries]]
14. [[#14. ⭐ Advanced: S/4HANA Universal Journal (ACDOCA)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): finance is where the S/4HANA move bites hardest
> **SAP Q2 2026 results (23 Jul 2026).** Current cloud backlog reached **€22.9 billion, up 27% (+26% at constant currency)**; cloud revenue rose 22% reported (+24% constant currency); SAP guided 2026 cloud revenue to **€25.8–26.2 billion**. Investing.com's summary adds that **Cloud ERP Suite revenue was €5.5 billion (+27%), about 88% of cloud revenue**, i.e. the finance-plus-logistics core this note teaches is the engine of SAP's growth. ([PR Newswire: SAP Quarterly Statement Q2 2026](https://www.prnewswire.com/news-releases/sap-quarterly-statement-q2-2026-302833633.html); [Investing.com](https://www.investing.com/news/company-news/sap-q2-2026-slides-cloud-backlog-surges-27-amid-margin-pressure-93CH-4810220))
>
> **ECC deadline and the 2033 "transition option" (announced 4–5 Feb 2025).** Standard maintenance for ECC ends **31 Dec 2027** and extended maintenance for on-premise SAP ERP ends at the **end of 2030**. For very large ECC estates SAP introduced "SAP ERP, private edition, transition option": purchasable from **2028**, usable **2031–2033**, tied to a RISE with SAP contract, with SAP HANA as the only database and systems to be moved to the private edition before end-2030. ([CIO.com](https://www.cio.com/article/3816887/sap-throws-a-lifeline-to-large-organizations-with-new-ecc-offering.html); [TechTarget](https://www.techtarget.com/searchsap/news/366618912/Rise-With-SAP-will-extend-support-deadline-for-some))
>
> **S/4HANA 2025 on-premise release (8 Oct 2025).** IDES24's release overview lists under Finance faster period-end closing and automated reconciliations on the Universal Journal, simplified asset accounting and predictive accounting. Per Wikipedia, since Oct 2023 the on-premise edition follows a two-year release cycle with seven-year mainstream maintenance. (Vendor-described features; check release notes before promising them to a client.) ([IDES24](https://www.ides24.de/en/knowledge/what-s-new-in-s4hana-2025); [Wikipedia: SAP S/4HANA](https://en.wikipedia.org/wiki/SAP_S/4HANA))
>
> **GAIL goes live on S/4HANA Cloud (25 Jun 2025).** GAIL called itself the first Maharatna PSU to move from legacy ECC to S/4HANA on cloud ("Navodaya"), delivered in one year; its Director (Finance) framed it as building a smarter, more agile enterprise rather than a technology change. ([Indian Chemical News](https://www.indianchemicalnews.com/digitization/gail-goes-live-with-rise-with-sap-s4hana-on-cloud-26605))
>
> Sub-topics that say **"See news box"** reuse these items. Related: [[080 SAP MM — Materials Management]], [[200 SAP S-4HANA Migration, Data Migration & Testing]].

---
## 1. FI Organisational Structure & Chart of Accounts
> 🔴 Tier 1 · _Key points:_ Company code, chart of accounts, fiscal year variant, GL master at two levels

### Definition
**FI (Financial Accounting)** records the legal books of a company. Its building blocks:
- **Company code:** the smallest unit for which a complete, self-contained set of books (balance sheet, P&L) is produced; one legal entity or GSTIN-bearing unit in practice. Carries currency (INR), fiscal year variant and posting period variant.
- **Chart of accounts (CoA):** the list of GL accounts shared by one or more company codes. Types: **operating CoA** (used for daily posting), **group CoA** (for consolidation) and **country CoA** (statutory, e.g. for local reporting).
- **Fiscal year variant:** defines periods; India uses an **April to March** year with 12 periods plus special periods (variant V3 in the standard delivery) versus K4 for a calendar year.
- **Posting period variant** (`OB52`): which periods are open for which account types (+ assets, D customers, K vendors, S GL).
- **Other dimensions:** segment (statutory segment reporting, Ind AS 108), profit centre, functional area, and the older business area.

**GL account master** has two levels: **chart-of-accounts level** (number, group, balance-sheet or P&L type, short text, group account number) and **company-code level** (currency, open-item management, line-item display, tax category, field status group, reconciliation account flag). In S/4HANA the account master also decides whether an account is a **cost element** (primary or secondary), because the separate cost-element master is gone.

T-codes: `FS00` maintain GL account, `FSP0` CoA level, `FSS0` company-code level, `OB52` open/close periods, `OBY6` company-code global parameters.

### Example
Company "Shakti Auto Components Pvt Ltd", company code 1000, currency INR, fiscal year variant V3 (Apr–Mar). Plants 1100 Pune and 1200 Nashik both belong to company code 1000, so one balance sheet covers both. Account 140000 "Raw material stock" is a CoA-level balance-sheet account; at company-code level it is flagged "reconciling: no, line items: yes". Account 160000 "Sundry creditors" is a **reconciliation account**: it is blocked for direct posting and updates only through vendor postings.

### In the news
See news box. GAIL's finance director framed S/4HANA as an enterprise redesign; in practice that starts with agreeing one chart of accounts and company-code structure.

### Interview angle
> [!question] How it is asked
> "Walk me through the FI organisational structure and what a chart of accounts is." or "Why can't I post directly to the vendor reconciliation account?"

> [!tip] Strong answer includes
> - Company code as the legal reporting unit; CoA shared across codes; plant assigned to one company code
> - Two-level GL master (CoA vs company code) and the reconciliation-account concept
> - Fiscal year variant for April–March and posting period control
> - Link to MM: plant to company code assignment decides which books a stock movement hits ([[079 SAP Fundamentals & Architecture]])

---

## 2. General Ledger Posting & the Document Principle
> 🔴 Tier 1 · _Key points:_ Dr = Cr, document types, posting keys, parking, reversal

### Definition
Every FI posting creates an **accounting document** with a header (company code, document type, posting date, document date, currency, reference) and **line items** (account, debit/credit, amount, tax code, cost object). A document must balance (total debits = total credits) before it can be saved. Documents are never deleted; errors are corrected by **reversal** (`FB08`, or `FBRA` for cleared items) which posts an equal and opposite document.

| Item | Examples |
|---|---|
| **Document type** (number range, allowed accounts) | SA GL document, KR vendor invoice, KZ vendor payment, RE invoice from MM (MIRO), WE goods receipt, WA goods issue, DR customer invoice, DZ customer payment, RV billing from SD, AF depreciation |
| **Posting key** (debit/credit, account type) | 40 GL debit, 50 GL credit, 31 vendor invoice (credit), 25 vendor payment (debit), 01 customer invoice (debit), 15 customer payment (credit), 89 stock receipt, 99 stock issue, 86 GR/IR credit, 96 GR/IR debit |

T-codes: `FB50` (enter GL document), `FB01` (classic), `F-02`, `FB03` display, `FB08` reverse, `FBV1` park, `FS10N` (ECC balances; `FAGLB03` in S/4), `FBL3N` line items. **Parked documents** need no balance and no immediate effect on ledgers and are posted later after approval, a common control for high-value journals. **Tolerance groups** limit how large a posting each user can make. In S/4HANA the GL line itself carries the extra dimensions (cost centre, profit centre, segment) because of the Universal Journal.

### Example
Month-end accrual for electricity: `FB50`, document type SA, Dr 450100 Power & fuel ₹2,40,000 (cost centre Pune Plant), Cr 230100 Accrued expenses ₹2,40,000. Next month a reversal date is entered so the accrual cancels automatically when the actual vendor invoice arrives.

### In the news
See news box. IDES24 lists automated reconciliations and faster closing for the 2025 release, which target exactly this journal-posting and accrual workload.

### Interview angle
> [!question] How it is asked
> "What is a document type and a posting key? How do you correct a wrongly posted FI document?"

> [!tip] Strong answer includes
> - Balanced document principle; no deletion, only reversal (`FB08`)
> - Document type controls number range; posting key controls debit/credit and account type
> - Parking and approval workflow for control
> - India point: the Companies Act accounting-software audit-trail (edit log) requirement means reversals and changes must stay traceable

---

## 3. Accounts Payable (AP) and TDS/GST
> 🔴 Tier 1 · _Key points:_ Vendor sub-ledger, reconciliation account, invoice, payment run F110, TDS

### Definition
**AP** manages vendor sub-ledger accounts. Each vendor posting automatically updates a **reconciliation account** (e.g. Sundry creditors) in the GL. Flows:
1. **Invoice:** with PO reference through MIRO (`MIRO` creates an FI document, type RE), or without PO through `FB60`.
2. **Payment:** automatic payment program `F110` (parameters, proposal, payment run, printing/bank file); manual `F-53`. Payment terms and **cash discount** decide the due date.
3. **Controls:** payment blocks, duplicate-invoice check on reference number/amount/date, bank-detail change approval, down payments (`F-48`).
4. **India overlay:** **TDS** deducted on vendor payments (e.g. s.194J 10% on professional fees, s.194C on contractors; rates change, check the current Finance Act); **GST input tax** posted to input CGST/SGST/IGST accounts for claiming credit; **MSME vendors** must be paid within 45 days (15 days if no written agreement) or the buyer loses the tax deduction until payment under s.43B(h).

Standard FI entry for a service invoice: Dr Expense, Dr Input GST, Cr Vendor (reconciliation account), Cr TDS payable. In S/4HANA vendors are **Business Partners** (`BP`).

### Example
Consultancy fee ₹1,00,000 plus 18% GST (₹18,000) = invoice ₹1,18,000. TDS 10% is computed on the base fee (₹10,000) because GST is shown separately. Entry: Dr Consulting expense ₹1,00,000; Dr Input GST ₹18,000; Cr Vendor ₹1,08,000; Cr TDS payable ₹10,000. When `F110` pays the vendor, Dr Vendor ₹1,08,000, Cr Bank ₹1,08,000; the ₹10,000 is deposited to the government separately. See [[227 GST & Indirect Tax for Supply Chains]].

### In the news
See news box. The jump to RISE/S/4HANA moves vendors to Business Partner and often adds automated payment and bank-communication cloud services.

### Interview angle
> [!question] How it is asked
> "Explain the AP process from invoice to payment and what controls you would put in." or "What is a reconciliation account?"

> [!tip] Strong answer includes
> - Sub-ledger to GL link via reconciliation account
> - PO-based (MIRO) vs non-PO (FB60) invoices and the 3-way match
> - `F110` stages: parameters, proposal, run, bank file
> - TDS, GST input credit and MSME 45-day rule as India specifics; duplicate-invoice and bank-change controls

---

## 4. Accounts Receivable (AR) and Credit Control
> 🔴 Tier 1 · _Key points:_ Billing creates FI document, incoming payment, dunning, credit management

### Definition
**AR** manages customer sub-ledgers. In order-to-cash the **billing document** (SD, `VF01`) automatically creates the FI invoice: **Dr Customer (reconciliation account: Sundry debtors), Cr Revenue, Cr Output GST**. Revenue accounts come from SD account determination (`VKOA`) using account keys such as ERL (revenue), ERS (sales deductions) and MWS (output tax). Incoming payments are posted with `F-28` (or via bank statement `FF67`/electronic bank statement) and **cleared** against open items. Process items:
- **Dunning** (`F150`): reminder letters by overdue days (level 1, 2, 3).
- **Credit management:** limit check at sales order, delivery and goods issue; in S/4HANA through SAP Credit Management.
- **Down payment and advance** (`F-29`), **credit memos**, **bad debt provisions** (age-based).
- **Special GL:** bills of exchange, guarantees, down payments are posted through special GL indicators and shown separately in the reconciliation account.

Key KPI: **DSO** = (average receivables ÷ credit sales) × days. Link to the order-to-cash flow in [[082 SAP SD — Sales & Distribution]].

### Example
Billing 1,000 units at ₹250 = ₹2,50,000 plus 18% GST ₹45,000. FI document: Dr Customer ₹2,95,000; Cr Revenue ₹2,50,000; Cr Output GST ₹45,000. On receipt (`F-28`), Dr Bank ₹2,95,000, Cr Customer ₹2,95,000, and the invoice clears. If receivables average ₹3.5 crore on annual credit sales of ₹36.5 crore, DSO = 3.5 / 36.5 × 365 = **35 days**.

### In the news
See news box. As cloud ERP revenue grows (Cloud ERP Suite €5.5 billion in Q2 2026), credit and collections modules are a standard part of finance scope.

### Interview angle
> [!question] How it is asked
> "What posting happens when a customer invoice is created in SAP?" or "How would you reduce DSO using SAP?"

> [!tip] Strong answer includes
> - Billing to FI integration with the three-line entry incl. output GST
> - Clearing of open items; dunning and credit limit checks
> - DSO formula with a number
> - Reconciliation account, special GL (advance, down payment)

---

## 5. Asset Accounting (FI-AA)
> 🔴 Tier 1 · _Key points:_ Asset class, depreciation areas, capitalisation, retirement, Schedule II

### Definition
**FI-AA** is the sub-ledger for fixed assets. Key objects:
- **Asset class:** groups assets (machinery, vehicles, IT) and carries default accounts, depreciation keys and number range.
- **Asset master:** `AS01` create; has **depreciation areas** (book depreciation under the Companies Act, tax depreciation under the Income-tax Act, management, group). In S/4HANA the new Asset Accounting posts into the Universal Journal; each area maps to a ledger.
- **Acquisition:** via PO with account assignment **A** (GR posts Dr Asset, Cr GR/IR), via `F-90` for vendor invoice or `ABZON` for asset without PO. **Asset under construction (AuC)** collects capex and is settled to the final asset when ready.
- **Depreciation run:** `AFAB` monthly: Dr Depreciation expense (cost centre), Cr Accumulated depreciation. **Retirement:** `F-92` (sale to a customer, with revenue) or `ABAVN` (scrapping, no revenue). **Year-end:** `AJAB`.

Depreciation methods: **SLM** (straight line) $=\frac{\text{Cost}-\text{Residual}}{\text{Life}}$ and **WDV** (written-down value) $=\text{Rate}\times\text{Opening book value}$.

### Example
Plant & machinery cost ₹30,00,000, useful life 15 years under Schedule II of the Companies Act, residual value 5% (₹1,50,000). SLM depreciation = (30,00,000 − 1,50,000) / 15 = **₹1,90,000 a year (₹15,833 a month)**. For tax, WDV at 15% gives ₹4,50,000 in year 1 and ₹3,82,500 in year 2 (15% of ₹25,50,000); the gap between book and tax depreciation creates **deferred tax**, which is why two depreciation areas are kept. (Rates and lives are as per standard Schedule II and Income-tax block rates; verify current provisions.)

### In the news
See news box. IDES24 lists simplified fixed-asset accounting in the 2025 on-premise release; ECC customers moving to S/4HANA must convert to the new Asset Accounting.

### Interview angle
> [!question] How it is asked
> "How does an asset get capitalised in SAP from a PO? What is AuC?" or "SLM vs WDV: which does SAP support?"

> [!tip] Strong answer includes
> - Asset class, master, depreciation areas (book vs tax)
> - Acquisition path (account assignment A, AuC settlement)
> - `AFAB` run and the Dr/Cr entry
> - Numeric SLM example and Schedule II link

---

## 6. Controlling Basics: Cost Centres, Cost Elements & Allocations
> 🔴 Tier 1 · _Key points:_ Controlling area, cost centre, activity type, assessment vs distribution

### Definition
**CO (Controlling)** is internal management accounting, used to plan, monitor and allocate costs inside the firm (see [[110 Cost Accounting for Operations]]). Elements:
- **Controlling area:** the organisational unit for cost accounting; one controlling area can span several company codes. Fiscal year variant must be consistent.
- **Cost element:** classifies costs. **Primary cost elements** exist as GL accounts (raw material consumption, salaries); **secondary cost elements** (category 42 assessment, 43 internal activity allocation, 21 internal settlement) exist only in CO. In S/4HANA both are created as GL accounts with an account type.
- **Cost centre:** a place where costs arise (department, machine group). `KS01` create, `KSB1` actual line items, `S_ALR_87013611` cost centre report in ECC, `KP06` plan costs.
- **Activity type:** measures output of a cost centre (machine hour, labour hour) with a planned **activity price** (`KP26`) used to charge orders: $\text{price}=\frac{\text{planned cost}}{\text{planned activity}}$.
- **Allocation:** **Assessment** (`KSU5`) uses a secondary cost element and hides the original cost types; **Distribution** (`KSV5`) keeps primary cost elements visible; **Activity allocation** charges orders for activity consumed.

### Example
HR cost centre has actual cost ₹6,00,000 and is assessed to production, stores and quality using headcount 40 : 35 : 25 = ₹2,40,000 / ₹2,10,000 / ₹1,50,000. A machining cost centre has planned cost ₹48,00,000 for 8,000 machine hours, so the activity price is ₹48,00,000 / 8,000 = **₹600 per machine hour**. A production order using 8 hours is charged ₹4,800.

### In the news
See news box. In S/4HANA the cost element is just a GL account type, one of the simplifications that make the ECC-to-S/4HANA conversion a finance project first.

### Interview angle
> [!question] How it is asked
> "What is the difference between FI and CO?" or "Assessment vs distribution?"

> [!tip] Strong answer includes
> - FI external, legal; CO internal, management reporting
> - Controlling area, cost centre, cost element, activity type with the price formula
> - Assessment (secondary cost element) vs distribution (primary retained)
> - How an order is charged through activity price (bridge to production costing in [[194 SAP Production Execution, Confirmation & Product Costing]])

---

## 7. Profit Centres and Internal Orders
> 🔴 Tier 1 · _Key points:_ Profit centre accounting, segment, internal order types, settlement

### Definition
**Profit centre (PCA):** a management unit for which a P&L (and, with document splitting, a balance sheet) is prepared, e.g. a plant, business line or region. It is assigned to cost centres, materials (plant data) and orders. In ECC it was a separate ledger (GLPCA); in S/4HANA it is a field in the Universal Journal, so profit-centre reports always reconcile with the GL. **Segment** is derived from the profit centre and supports statutory segment reporting.

**Internal order:** a temporary cost object for a specific job, event or project, created with `KO01`:
| Order type | Purpose | Settles to |
|---|---|---|
| Overhead (marketing, maintenance, R&D) | Collect costs of a short-term activity | Cost centre or GL |
| Investment | Collect capex | Asset under construction, then asset |
| Accrual | Compute accruals for provisions | Cost centre |
| With revenue | Events with income | Profitability segment |

Orders have **budget and availability control** (`KO22`), **commitments** from PRs and POs, and **settlement** (`KO88`) at period end. Production orders and maintenance orders are special order categories settled the same way ([[084 SAP QM & PM]]).

### Example
A trade-show internal order has a budget of ₹6,00,000. Booth fabrication ₹3,50,000 (PO), travel ₹1,10,000 and giveaways ₹90,000 are posted, so actual = ₹5,50,000, leaving ₹50,000 (availability control warns at, say, 90% usage). At period end `KO88` settles ₹5,50,000: Dr Marketing cost centre, Cr Internal order (settlement secondary cost element). For an investment order of ₹25 lakh, settlement goes to an AuC asset instead.

### In the news
See news box. GAIL's project-heavy, multi-plant structure is the kind of business that relies on orders and WBS elements to track capex.

### Interview angle
> [!question] How it is asked
> "When would you use an internal order instead of a cost centre?" or "What happens at order settlement?"

> [!tip] Strong answer includes
> - Cost centre permanent vs internal order temporary
> - Order types and where each settles
> - Budget, commitment and availability control
> - Profit centre as a field in the Universal Journal in S/4HANA

---

## 8. CO-PA: Profitability Analysis
> 🔴 Tier 1 · _Key points:_ Operating concern, costing-based vs account-based, value fields, billing flow

### Definition
**CO-PA** analyses profit by market segments: customer, product, region, sales organisation, channel. The **operating concern** (`KEA0`) defines the characteristics (what you slice by) and value fields (what you measure: revenue, discounts, COGS, freight).
- **Costing-based CO-PA:** value fields hold revenue and cost components from valuation (standard cost, activity cost); can use alternative valuation (e.g. plan cost); not tied to GL accounts line by line, so reconciliation to FI is by totals.
- **Account-based CO-PA (Margin Analysis in S/4HANA):** posts by account, same as FI, so it reconciles automatically; in S/4HANA the **Universal Journal** carries the profitability characteristics, so account-based CO-PA is the default and costing-based is an optional add-on.

Flow: sales order and billing (SD) pass revenue, discounts and freight to CO-PA at billing; COGS flows at goods issue (cost from the material valuation). Reports: `KE30` (ECC), Fiori "Margin Analysis"; manual line item `KE21N`; line-item report `KE24`.

$$\text{Contribution margin}=\text{Net revenue}-\text{COGS}-\text{variable selling cost}$$

### Example
Region West sells 10,000 units at ₹500: gross revenue ₹50,00,000, 5% discount ₹2,50,000, net revenue ₹47,50,000, COGS (std ₹320) ₹32,00,000, freight ₹2,50,000. Contribution = 47,50,000 − 32,00,000 − 2,50,000 = **₹13,00,000, a margin of 27.4% of net revenue**. If another region sells at ₹430 with the same cost, CO-PA exposes the negative effect of discounting by customer and product.

### In the news
See news box. In S/4HANA, margin analysis inside the Universal Journal replaces nightly CO-PA reconciliations that used to dominate ECC month-ends.

### Interview angle
> [!question] How it is asked
> "What is CO-PA and what is the difference between costing-based and account-based?"

> [!tip] Strong answer includes
> - Operating concern, characteristics, value fields
> - Both flavours and why account-based reconciles with FI
> - How billing and goods issue feed CO-PA
> - Business use: customer or product profitability, discount analysis (consulting angle: [[025 Case Interview — Profitability]])

---

## 9. Automatic Account Determination for Goods Movements (OBYC)
> 🔴 Tier 1 · _Key points:_ Valuation class, transaction/event key, account modifier, BSX, WRX, GBB, PRD

### Definition
When a goods movement is posted in MM, SAP finds the GL account without user input. The chain:
1. **Movement type** (T156) fixes the **transaction/event key** (and the account modifier).
2. **Material** gives **valuation class** (material master, Accounting 1), fixed via material type and account category reference (`OMSK`).
3. In `OBYC`, the key (+ modifier + valuation class + chart of accounts / valuation grouping code) points to a **GL account**. `OMWB` simulates the determination.

| Key | Meaning | Typical use |
|---|---|---|
| **BSX** | Inventory posting | Stock account Dr on receipt, Cr on issue |
| **WRX** | GR/IR clearing | Cr at GR, Dr at invoice |
| **GBB** (with modifier) | Offsetting entry for goods issue | VBR consumption (201), AUF order (261), VNG scrap, VAX COGS (601), BSA initial stock (561), INV inventory differences (701/702) |
| **PRD / PRF** | Price difference (standard price) | Invoice price variance |
| **UMB** | Revaluation / transfer price differences | Plant-to-plant transfers, price change |
| **KON** | Consignment liability | Consumption of vendor stock |
| **BSV** | Change in stock value | Where stock change is shown in P&L |

Each combination is stored once for a CoA, so a **single change in OBYC affects all materials of that class**. Wrong valuation class is a classic reason for reconciliation breaks between inventory and GL.

### Example
HDPE is valued at moving average ₹95 (valuation class 3000). Postings:

| Movement | Quantity | Debit | Credit | Amount (₹) |
|---|---|---|---|---|
| 101 GR from PO | 1,000 kg | Raw material stock (BSX) | GR/IR (WRX) | 95,000 |
| 261 to production order | 50 kg | Production order (GBB/AUF) | Raw material stock (BSX) | 4,750 |
| 201 to cost centre | 50 kg | Cost centre expense (GBB/VBR) | Raw material stock (BSX) | 4,750 |
| 551 scrap | 5 kg | Scrapping expense (GBB/VNG) | Raw material stock (BSX) | 475 |
| 702 inventory loss (count 12 kg short) | 12 kg | Inventory difference (GBB/INV) | Raw material stock (BSX) | 1,140 |
| 601 delivery of FG, standard ₹160 | 1,000 pcs | COGS (GBB/VAX) | Finished goods stock (BSX) | 1,60,000 |

The 601 line is a finished-goods material (valuation class for FERT), so the same keys point to different accounts; the key is identical, the class differs. Details of movements in [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]].

### In the news
See news box. Account-determination tables are the first thing validated in a migration test cycle ([[200 SAP S-4HANA Migration, Data Migration & Testing]]).

### Interview angle
> [!question] How it is asked
> "How does SAP know which GL account to post when I do a goods receipt?" or "What are BSX, WRX and GBB?"

> [!tip] Strong answer includes
> - The chain: movement type to transaction key to valuation class to GL (OBYC)
> - BSX, WRX, GBB, PRD, UMB with a one-line use each
> - A posted example with amounts
> - Where it breaks: wrong valuation class, missing account modifier; test with `OMWB`

---

## 10. GR/IR Clearing and Price Variances
> 🔴 Tier 1 · _Key points:_ Dr Stock/Cr GR-IR at GR; Dr GR-IR at invoice; MAP vs standard; MR11

### Definition
**GR/IR (goods receipt / invoice receipt) clearing** is a balance-sheet account that holds the liability for goods received but not yet invoiced (credit balance) or invoiced but not yet received (debit balance). Flow:
- **GR (101):** Dr Inventory (BSX), Cr GR/IR (WRX), at the PO price.
- **IR (MIRO):** Dr GR/IR (WRX), Dr Input GST, Cr Vendor; any price difference goes to the stock (MAP) or to **PRD** (standard price).
- When balances remain on the GR/IR account for long (short invoice, price difference), they are cleared with `MR11` (GR/IR account maintenance, write-off), `F.13` automatic clearing, and reconciled with `MB5S` (GR/IR balance by PO). Open balances at year-end are shown under accruals or other liabilities, often with a reclassification.

**Price differences:** **Price control V (MAP):** the invoice difference changes stock value and MAP if stock is still on hand, otherwise it goes to a price difference account. **Price control S (standard):** stock stays at standard; the difference is expensed to PRD immediately.

### Example
PO 500 units at ₹120. GR: Dr Stock ₹60,000, Cr GR/IR ₹60,000. Vendor invoices ₹126 per unit: IR value ₹63,000 plus 18% GST ₹11,340 = ₹74,340.
- **Standard price ₹120:** Dr GR/IR ₹60,000; Dr PRD ₹3,000; Dr Input GST ₹11,340; Cr Vendor ₹74,340.
- **MAP, 300 units earlier at ₹118 (MAP before GR), all stock on hand:** MAP after GR = (35,400 + 60,000) / 800 = ₹119.25; the ₹3,000 invoice difference is added to stock, giving ₹98,400 / 800 = **₹123 new MAP**.
Because ₹126 is the actual price, MAP "catches up" with reality, whereas standard cost shows the difference as a procurement variance for the buyer to explain.

### In the news
See news box. A stale GR/IR balance is one of the first things auditors and S/4HANA migration teams clean up before cut-over.

### Interview angle
> [!question] How it is asked
> "What is GR/IR and why does it have a balance at month-end?" or "How is price difference handled in SAP for standard and MAP?"

> [!tip] Strong answer includes
> - Entry at GR and at IR, with accounts
> - What causes residual balances; `MR11`, `MB5S`, `F.13`
> - MAP vs standard treatment, with the numeric example
> - Control action: age the GR/IR items and chase vendors/receiving

---

## 11. Material Ledger and Actual Costing
> 🔴 Tier 1 · _Key points:_ Periodic unit price, multilevel actual costing, revaluation of consumption, CKMLCP

### Definition
The **Material Ledger (ML)** keeps quantity and value of a material by period in several currencies and valuation types. It is **always active in S/4HANA** (stock valuation runs through it and it feeds the Universal Journal), while **actual costing** (the use of a calculated actual price) is a switch you activate per plant.

With **price control S**, ML collects **price differences and exchange-rate differences** during the period. At closing the **Periodic Unit Price (PUP)** is calculated:
$$PUP=\frac{\text{Opening value}+\text{Receipts at actual value (incl. differences)}}{\text{Opening qty}+\text{Receipt qty}}$$
Steps in the **actual costing run** `CKMLCP`: selection, sorting by low-level code, **single-level price determination** (PUP per material), **single-level settlement**, **multilevel price determination** (the actual cost of components rolls into semi-finished and finished goods through the BOM structure), **multilevel settlement** (revalues consumption and closing stock), and **closing entries** (posting to FI). Only closing entries create FI documents.

Result: **consumption is revalued** at actual cost (variances posted from stock to COGS/WIP) and the remaining stock is revalued to PUP. Multilevel costing is what transfers variances from raw material to finished goods up the BOM.

### Example
Opening stock 100 units at standard ₹50 (value ₹5,000). Receipt of 100 units at ₹56: price difference 100 × 6 = ₹600 collected in ML, stock stays at standard ₹5,000 + ₹5,000 = ₹10,000. PUP = (5,000 + 5,600) / 200 = **₹53**. 120 units were consumed at ₹50, so consumption is revalued by 120 × (53 − 50) = **₹360** (to COGS/WIP), and closing stock of 80 units is revalued by 80 × 3 = **₹240** (to inventory, value now ₹4,240 = 80 × 53). Total ₹600 = ₹360 + ₹240. 

### In the news
See news box. IDES24's 2025 notes list predictive accounting and faster closing, but actual costing remains the main route to true product costs when commodity prices swing.

### Interview angle
> [!question] How it is asked
> "What is the Material Ledger? How is actual costing different from standard costing?"

> [!tip] Strong answer includes
> - ML as multi-currency, multi-valuation stock ledger; always on in S/4HANA, actual costing optional
> - PUP formula and the 600 = 360 + 240 split example
> - Single-level vs multilevel and `CKMLCP` steps
> - Business case: true cost of goods, variance pass-through, transfer pricing

---

## 12. Period-End Closing: FI, MM, CO and ML Sequence
> 🔴 Tier 1 · _Key points:_ Open/close periods, accruals, depreciation, CO allocation, WIP, variances, ML run

### Definition
A **period-end close** follows a dependency order: materials first, then costs, then financials.

| Step | What | T-code |
|---|---|---|
| 1 | Freeze MM: close the previous period, open the new one; GR/IR check | `MMPV`, `MR11`, `MB5S` |
| 2 | Open-PO and inventory counts, accruals for received-not-invoiced goods and services | `FBS1`, `ML81N` |
| 3 | Foreign currency valuation of open items and balances | `F.05` / `FAGL_FCV` |
| 4 | Depreciation | `AFAB` |
| 5 | CO allocations: assessment, distribution, periodic activity price | `KSU5`, `KSV5`, `KSII` |
| 6 | Production: WIP, variance, settlement | `KKAO`, `KKS1`, `KO88` |
| 7 | Material ledger actual costing run | `CKMLCP` |
| 8 | Reconcile: stock list vs GL, sub-ledgers vs reconciliation accounts, GST ITC vs GSTR-2B | `MB5L`, `FAGLB03` |
| 9 | Close FI periods; year-end balance carry forward; reports | `OB52`, `S_ALR_87012284` |

In S/4HANA the **Universal Journal** removes the need for the FI-CO reconciliation ledger run, and SAP's **Advanced Financial Closing** or task-list tools sequence the steps with owners, dependencies and sign-offs.

### Example
Plant controller's close calendar: working day 1 close MM period 9, GR/IR review and accruals; day 2 depreciation and FX valuation; day 3 allocations and WIP; day 4 variance calculation and settlement of production orders; day 5 `CKMLCP`; day 6 reconciliation and trial balance to the CFO. Settling after the ML run would be wrong because actual price differences must be in the order costs first.

### In the news
See news box. IDES24 describes automated reconciliations and faster closing as the 2025 finance theme; closing calendars are rebuilt around such tools during migration.

### Interview angle
> [!question] How it is asked
> "Walk me through month-end close in SAP for a manufacturing company" or "In what order do you run settlement and the material ledger?"

> [!tip] Strong answer includes
> - Dependency logic: sub-ledgers and stock first, then CO allocation, WIP and variance, then ML, then FI close
> - Named T-codes at each stage
> - India controls: TDS/GST reconciliation and audit-trail evidence
> - Mention of a closing cockpit and KPIs such as days to close

---

## 13. Integration of MM, SD and PP with FI-CO: Worked Journal Entries
> 🔴 Tier 1 · _Key points:_ Procure-to-pay, order-to-cash, make-to-stock entries

### Definition
Logistics events create financial documents automatically (the **document principle**: one material document, one or more accounting documents, linked in the document flow). The three cycles:

**Procure-to-pay (MM):** PO (no FI posting), GR 101 (Dr Stock, Cr GR/IR), MIRO (Dr GR/IR, Dr Input GST, Cr Vendor), payment `F110` (Dr Vendor, Cr Bank).

**Order-to-cash (SD):** Sales order (none), goods issue 601 (Dr COGS, Cr Stock), billing (Dr Customer, Cr Revenue, Cr Output GST), payment `F-28` (Dr Bank, Cr Customer).

**Plan-to-produce (PP):** issue 261 (Dr Production order, Cr Raw material), confirmation of activity (Dr Production order, Cr Cost centre via activity type), GR 101 from order (Dr Finished goods at standard, Cr Production order), settlement of variance (Dr Price difference/Production variance, Cr Production order).

### Example
**Procure-to-pay:** 1,000 kg steel at ₹100 = ₹1,00,000 plus 18% GST ₹18,000.

| Event | Dr | Cr |
|---|---|---|
| GR | Stock 1,00,000 | GR/IR 1,00,000 |
| MIRO | GR/IR 1,00,000; Input GST 18,000 | Vendor 1,18,000 |
| Payment | Vendor 1,18,000 | Bank 1,18,000 |

**Order-to-cash:** 1,000 units, price ₹250, standard cost ₹160.

| Event | Dr | Cr |
|---|---|---|
| Goods issue | COGS 1,60,000 | Finished goods 1,60,000 |
| Billing | Customer 2,95,000 | Revenue 2,50,000; Output GST 45,000 |
| Receipt | Bank 2,95,000 | Customer 2,95,000 |

Gross margin = 2,50,000 − 1,60,000 = **₹90,000 (36% of revenue)**. **Production:** 1,000 kg of ₹95 raw material issued = ₹95,000; machine time 8 h × ₹600 = ₹4,800 charged to the order. A full variance walk-through is in [[194 SAP Production Execution, Confirmation & Product Costing]]; sales entries come from [[082 SAP SD — Sales & Distribution]].

### In the news
See news box. In the Universal Journal each of these entries is a set of ACDOCA lines carrying cost centre, profit centre and segment at posting time.

### Interview angle
> [!question] How it is asked
> "Give the accounting entries in the procure-to-pay and order-to-cash cycles" or "Where do SD and MM touch FI?"

> [!tip] Strong answer includes
> - The three entries per cycle with the right accounts and GST
> - Which events have no accounting (PO, sales order)
> - Account determination keys behind them (BSX, WRX, GBB for MM; `VKOA` account keys for SD)
> - Margin or cost number to show that the entries tie together

---

## 14. ⭐ Advanced: S/4HANA Universal Journal (ACDOCA)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
In ECC, FI (`BKPF`/`BSEG`), CO (`COEP`), asset accounting (`ANEP`), the New GL (`FAGLFLEXA`), CO-PA and the material ledger each stored their own line items, and a reconciliation ledger kept FI and CO in agreement. In S/4HANA the **Universal Journal** is the table **`ACDOCA`**, a single line-item store for GL, CO, Asset Accounting, ML and account-based CO-PA. Facts worth knowing:
- **Key fields:** ledger (`RLDNR`, e.g. leading ledger 0L), company code, fiscal year, document number and a six-digit line item, so the old 999-line limit of `BSEG` does not apply to ACDOCA.
- **Ledgers:** the leading ledger follows the statutory view; **non-leading (parallel) ledgers** support other GAAPs; **extension ledgers** store only adjustments on top of a base ledger.
- **Compatibility views:** old tables (`COEP`, `GLT0`, `FAGLFLEXA`, `BSIS`, `BSID`, `BSIK` and others) exist as views that read ACDOCA, so legacy reports and custom code keep working; `BKPF` stays as the document header and `BSEG` keeps the FI document items. Inventory documents follow the same idea: `MATDOC` replaces `MKPF/MSEG`.
- **Benefits:** one source of truth with no reconciliation, drill-down from balance to line item with cost centre, profit centre and segment, no aggregate tables (totals are computed on the fly in HANA), and real-time period-end reports.
- **Impact on consultants:** Business Partner replaces vendor and customer masters; cost elements become GL accounts; profit centre and segment are on each line; Fiori apps (e.g. Trial Balance, Display Line Items in General Ledger) replace many classic reports.

Source for table-level facts: QueryViz and SkillsTek summaries, and Eursap's UJ explainer (secondary sources); confirm against SAP Notes before client work.

### Example
A goods issue of ₹4,750 to a cost centre writes two ACDOCA lines (Dr consumption GL with cost centre and profit centre, Cr stock GL) while MATDOC holds the quantity. A cost-centre report for the month sums line items of the consumption account where cost centre = X, and a balance sheet report sums the stock account for the same ledger, with no job between them. Moving to ECC-based reports would have required FI, CO and ML to be reconciled first.

### In the news
See news box. Because SAP says Cloud ERP Suite is about 88% of its cloud revenue (Q2 2026), the Universal Journal is the default data model that nearly every new SAP finance project lands on.

### Interview angle
> [!question] How it is asked
> "What is the Universal Journal and why does it matter?" or "How does S/4HANA change FI-CO compared to ECC?"

> [!tip] Strong answer includes
> - Single table ACDOCA replacing separate FI, CO, AA, ML and CO-PA stores; compatibility views
> - No reconciliation ledger, six-digit line items, parallel and extension ledgers
> - Business effects: faster close, real-time profitability by segment, cost element as GL account
> - Consulting lens: impact on custom reports, migration effort ([[200 SAP S-4HANA Migration, Data Migration & Testing]]) and training; quick-reference T-codes in [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]]
