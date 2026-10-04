---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP MM Advanced - Inventory, Batches & Special Stocks"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP MM Advanced - Inventory, Batches & Special Stocks

⬅ [[190 SAP FI-CO Essentials for Operations Professionals]] · [[_Index - SAP ERP|SAP ERP]] · [[192 SAP Sourcing & Procurement Deep Dive]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Movement Types: Anatomy and the Core Set]]
2. [[#2. Accounting of Key Movements: Worked Postings]]
3. [[#3. Transfer Postings and Plant-to-Plant Transfers]]
4. [[#4. Stock Transport Orders (Intra- and Inter-Company)]]
5. [[#5. Reservations]]
6. [[#6. Physical Inventory (MI01, MI04, MI07)]]
7. [[#7. Batch Management and Classification]]
8. [[#8. Serial Numbers]]
9. [[#9. Special Stocks: Overview]]
10. [[#10. Consignment and Pipeline Procurement]]
11. [[#11. Subcontracting (Provision of Components) and Returnable Packaging]]
12. [[#12. Split Valuation]]
13. [[#13. Key T-codes, Reports and Fiori Apps]]
14. [[#14. ⭐ Advanced: S/4HANA Inventory Management Changes (MATDOC, Negative Stock)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): inventory logic moves onto S/4HANA's single material-document model
> **S/4HANA 2025 on-premise release (8 Oct 2025).** IDES24's release overview lists, under sourcing and procurement, **advanced ATP (aATP) with an automated stock-transport-order (STO) function**, and under warehouse management **batch-specific units of measure in EWM**, plus a manufacturing rework enhancement. These are vendor-described features; the underlying movement-type and stock logic taught here is unchanged. ([IDES24](https://www.ides24.de/en/knowledge/what-s-new-in-s4hana-2025))
>
> **ECC deadline (SAP announcement, 4–5 Feb 2025).** Standard maintenance for ECC ends **31 Dec 2027**, extended maintenance for on-premise SAP ERP at the **end of 2030**; a paid "SAP ERP, private edition, transition option" for very large ECC estates is purchasable from **2028** and usable **2031–2033**, bundled with a RISE contract and requiring SAP HANA. Every ECC stock process (MIGO, special stocks, MB52 reports) therefore has to be re-tested on S/4HANA's MATDOC model. ([CIO.com](https://www.cio.com/article/3816887/sap-throws-a-lifeline-to-large-organizations-with-new-ecc-offering.html); [TechTarget](https://www.techtarget.com/searchsap/news/366618912/Rise-With-SAP-will-extend-support-deadline-for-some))
>
> **SAP Q2 2026 (23 Jul 2026).** Current cloud backlog **€22.9 billion (+27%; +26% constant currency)**, cloud revenue +24% at constant currency, 2026 cloud revenue outlook **€25.8–26.2 billion**; Cloud ERP Suite revenue was €5.5 billion, about 88% of cloud revenue, per Investing.com. ([PR Newswire](https://www.prnewswire.com/news-releases/sap-quarterly-statement-q2-2026-302833633.html); [Investing.com](https://www.investing.com/news/company-news/sap-q2-2026-slides-cloud-backlog-surges-27-amid-margin-pressure-93CH-4810220))
>
> Sub-topics that say **"See news box"** reuse these items. Basics of MM are in [[080 SAP MM — Materials Management]].

---
## 1. Movement Types: Anatomy and the Core Set
> 🔴 Tier 1 · _Key points:_ Movement type controls stock type, accounts, screens; reversal pairs

### Definition
A **movement type** (three digits, table `T156`, maintained in `OMJJ`) is the single most important control in inventory management. It decides: which **stock types** are debited/credited (unrestricted, QI, blocked, special stock), whether the movement is **value-updating** (account postings through `OBYC` transaction keys), which **fields are mandatory** (cost centre, order, reason code), and its **reversal movement type**. Movement types sit under a **transaction type** (WE goods receipt, WA goods issue, UM transfer posting) and are processed in `MIGO`.

Remember them in groups: 1xx receipts, 2xx issues to consumption, 3xx transfers, 4xx special-stock transfers, 5xx other receipts/issues and subcontracting, 6xx deliveries/transit, 7xx inventory differences. An even-numbered reversal usually follows the odd one (101/102, 201/202, 261/262).

| Group | Type | Use |
|---|---|---|
| Receipt | 101 / 102 | GR for PO or production order / reversal |
| Receipt | 103 / 105 | GR into GR-blocked stock / release from it |
| Receipt | 501 / 561 | Receipt without PO / initial stock upload |
| Return | 122 / 161 | Return to vendor / return PO |
| Issue | 201 / 261 / 281 | To cost centre / production order / network |
| Issue | 551 / 552 | Scrapping / reversal |
| Transfer | 301 / 303 + 305 | Plant-to-plant 1-step / 2-step (in-transit) |
| Transfer | 311 / 313 + 315 | Storage location 1-step / 2-step |
| Transfer | 321 / 322 | QI to unrestricted / unrestricted to QI |
| Transfer | 343 / 344 | Blocked to unrestricted / unrestricted to blocked |
| Special stock | 411 / 412 | E.g. unrestricted to sales-order stock (E), consignment K to own stock |
| STO | 351 / 641 / 643 | Issue for STO to in-transit / delivery intra-company / cross-company |
| Subcontract | 541 / 543 | Provide components to vendor / consumption at GR |
| Delivery | 601 / 602 | GI for outbound delivery / cancel |
| Count | 701 / 702 | Inventory gain / loss, unrestricted |

### Example
A user posts 261 without a production order number: `MIGO` refuses because the movement type makes the order a required entry. Switching the movement type to 201 asks for a cost centre instead, and the debit lands on a cost-centre expense account rather than WIP. One field on `T156`, different accounting.

### In the news
See news box. Movement types survive the S/4HANA move, but IDES24's note on aATP with automated STOs shows how new apps still ride on 351/641 style movements.

### Interview angle
> [!question] How it is asked
> "What is a movement type and what does it control?" or "Name five movement types and their use."

> [!tip] Strong answer includes
> - Control functions: stock type, value update, mandatory fields, reversal
> - Grouping logic (1xx to 7xx) and reversal pairs
> - Five accurate examples with business context
> - Link to account determination (movement type to transaction key in `OBYC`, see [[190 SAP FI-CO Essentials for Operations Professionals]])

---

## 2. Accounting of Key Movements: Worked Postings
> 🔴 Tier 1 · _Key points:_ BSX, WRX, GBB; value-updating vs quantity-only movements

### Definition
A movement is **value-updating** when stock value changes (receipts, issues, scrap, deliveries) and **quantity-only** when value stays inside the same valuation level (sloc-to-sloc 311, QI to unrestricted 321, blocked 344). Value-updating movements create an FI document through `OBYC` keys: **BSX** (stock), **WRX** (GR/IR), **GBB** with modifier (VBR consumption, AUF order, VNG scrap, VAX COGS, INV inventory difference, BSA initial entry), **PRD** (standard-price difference) and **UMB** (revaluation/transfer differences).

Valuation rules: issues are posted at the current **MAP** (price control V) or **standard price** (price control S). Receipts against a PO are posted at the PO price (GR/IR), and the invoice then settles any difference ([[190 SAP FI-CO Essentials for Operations Professionals]]).

### Example
Steel coil, MAP ₹95 per kg, 1,000 kg on hand.

| Movement | Qty | Debit | Credit | ₹ |
|---|---|---|---|---|
| 101 GR from PO at ₹95 | 500 kg | Stock (BSX) | GR/IR (WRX) | 47,500 |
| 261 to production order | 50 kg | Order consumption (GBB/AUF) | Stock (BSX) | 4,750 |
| 201 to maintenance cost centre | 20 kg | Consumption expense (GBB/VBR) | Stock (BSX) | 1,900 |
| 551 scrap (rusted) | 5 kg | Scrap expense (GBB/VNG) | Stock (BSX) | 475 |
| 311 sloc RM to sloc line-side | 100 kg | no FI document | no FI document | 0 |
| 122 return to vendor | 10 kg | GR/IR (WRX) | Stock (BSX) | 950 |

The 311 transfer changes quantities only: both slocs belong to the same plant, so the plant-level value does not move.

### In the news
See news box. In S/4HANA each of these movements writes a row to the single material-document table MATDOC and journal lines to the Universal Journal in one transaction.

### Interview angle
> [!question] How it is asked
> "What is the accounting for 261, 201, 551 and 601?" or "Which movements create no accounting document?"

> [!tip] Strong answer includes
> - BSX versus GBB offsets and the modifiers VBR, AUF, VNG, VAX
> - A table with quantities and rupee values using MAP
> - Quantity-only movements (311, 321, 344)
> - Reversal rather than delete

---

## 3. Transfer Postings and Plant-to-Plant Transfers
> 🔴 Tier 1 · _Key points:_ 301 vs 303/305, 311, 321/322, valuation at issuing plant

### Definition
**Transfer postings** move stock without consuming it. Within a plant: 311 (one-step sloc to sloc) or 313 + 315 (remove, then place, with in-transit stock); status changes (321 QI to unrestricted, 343 blocked to unrestricted); and **material-to-material** (309). Between plants (stock transfer without a PO): **301** (one-step) or **303 + 305** (two-step, goods sit in **stock in transit** of the receiving plant between the two). Between company codes the move is a sale: it needs an inter-company clearing posting and, in India, a tax invoice and e-way bill when the GSTINs differ.

**Valuation rule:** the receiving plant takes the stock in at the **issuing plant's valuation price**. If the receiving plant uses MAP, its price is recalculated; if it uses standard price, the difference is a price-difference posting. The plants must belong to the same company code for a plain 301 to need no sales document.

T-codes: `MIGO` (transfer posting, 301/311), `MB1B` (legacy transfer posting), `MB5T` (stock in transit).

### Example
Pune holds MAP ₹95; Nashik holds 200 units at MAP ₹98 (value ₹19,600). A 301 transfer of 50 units: issue from Pune 50 × 95 = ₹4,750 (Cr Pune stock), receipt in Nashik at ₹4,750. Nashik new MAP = (19,600 + 4,750) / 250 = **₹97.40**. With a two-step 303/305 posting the 50 units would sit in transit for transport days and would not be usable by Nashik MRP until the 305 placement.

### In the news
See news box. SAP's aATP with automated STOs aims to fix shortages by transferring between plants; the stock posting under the hood remains 301/351 style.

### Interview angle
> [!question] How it is asked
> "What is the difference between 301 and 303/305?" or "At which price does the receiving plant value a transferred material?"

> [!tip] Strong answer includes
> - One-step vs two-step and when to prefer two-step (transit visibility, goods damaged in transit)
> - Valuation at issuing plant price; MAP recalculation with a number
> - Cross-company transfer implications (clearing, GST invoice and e-way bill)
> - Reports to track in-transit (`MB5T`)

---

## 4. Stock Transport Orders (Intra- and Inter-Company)
> 🔴 Tier 1 · _Key points:_ UB PO, 351 in-transit, delivery 641/643, GR 101, billing IV

### Definition
An **STO** is a PO to your own plant (the supplying plant) instead of a vendor; PO type **UB**, item category **U**. It supports planning (the receiving plant's MRP creates the STO), tracking and, with a delivery, shipping documents.

**Without delivery (one-step/two-step by movement 351):**
1. Receiving plant raises STO (supplying plant on the item).
2. Supplying plant posts GI in `MIGO` against the STO with **351**: stock moves into the receiving plant's **stock in transit**.
3. Receiving plant posts GR **101** against the PO: stock in transit becomes unrestricted.

**With delivery (needed for shipping and e-way bills):** STO → **outbound delivery** (`VL10B` due-list or `VL01N` with PO reference, delivery type NL) → picking → **post goods issue (641)** → GR 101 at receiving plant. **Inter-company** (different company codes): delivery type NLCC, PGI uses **643**, then **billing document (type IV)** at an inter-company price (condition PI01) creates a customer invoice for the supplying company and (through EDI or a standard process) a vendor invoice for the receiving company. Pricing and tax of the billing document come from SD ([[082 SAP SD — Sales & Distribution]]).

| Variant | Delivery | Billing | GI movement |
|---|---|---|---|
| Intra-company, no delivery | No | No | 351 |
| Intra-company with delivery | Yes (NL) | No | 641 |
| Inter-company | Yes (NLCC) | Yes (IV) | 643 |

### Example
Pune (company code 1000) transfers 500 units to a Nashik plant that sits in company code 2000. Stock at cost 500 × ₹95 = ₹47,500 leaves Pune on PGI (643). Inter-company price ₹120 gives billing value 500 × 120 = ₹60,000; IGST 18% = ₹10,800; invoice ₹70,800. Pune books ₹12,500 internal profit (60,000 − 47,500) which is eliminated on consolidation. When Nashik posts GR 101, its stock is valued at ₹60,000 and its payable to Pune is ₹70,800. In India an STO between plants with different state GSTINs is a taxable supply, so the invoice and e-way bill are mandatory; inside one GSTIN a delivery challan suffices (see [[227 GST & Indirect Tax for Supply Chains]]).

### In the news
See news box. IDES24 specifically lists an automated STO function in aATP in the 2025 on-premise release.

### Interview angle
> [!question] How it is asked
> "Explain the stock transport order process, with and without delivery." or "How is inter-company stock transfer billed?"

> [!tip] Strong answer includes
> - PO type UB, item category U, supplying plant
> - 351 vs 641 vs 643 and when each is used
> - Inter-company billing (IV), PI01 price and consolidation elimination
> - GST and e-way bill awareness for India

---

## 5. Reservations
> 🔴 Tier 1 · _Key points:_ MB21, planned issue, effect on availability, deletion

### Definition
A **reservation** is a request to the warehouse to keep stock ready for a future goods issue to a cost centre, order, project or another plant. Manual reservations: `MB21` create (movement type, cost centre/order, material, quantity, date), `MB22` change, `MB23` display, `MB24`/`MB25` lists. Reservations are also generated automatically by production orders (component reservations), maintenance orders, networks and stock-transfer needs.

Key points:
- Reservations **reduce available stock** in availability check and MRP (shown as "Rsrv" in `MD04`), but do not change stock until the goods issue.
- The **requirements date** drives MRP's timing; the **final issue** indicator closes a partly issued reservation.
- Each item has the "movement allowed" flag, a movement type and an account assignment; goods issue with reference to a reservation in `MIGO` pre-fills the data and keeps control.
- Old reservations are cleaned with `MBVR` (reorganisation), based on the "reservation retention period" in the configuration.
- Table `RESB` holds reservation items.

### Example
Maintenance plans a shutdown on 20 Oct and raises `MB21` for 20 kg of gasket material to cost centre Maintenance (type 201). Unrestricted stock is 60 kg, reservation 20 kg reduces ATP to 40 kg for other users. On 20 Oct the store issues against the reservation in `MIGO` (201), clearing the reservation; if only 15 kg is issued and the final-issue flag is set, the remaining 5 kg is released automatically.

### In the news
See news box. Reservation visibility feeds the planners' "material coverage" views that S/4HANA Fiori apps present.

### Interview angle
> [!question] How it is asked
> "What is a reservation and how is it different from a purchase requisition?"

> [!tip] Strong answer includes
> - Internal stock reservation vs PR (procure externally)
> - Effect on ATP/MRP without moving stock
> - Created manually (`MB21`) or automatically from orders
> - Reservation clean-up and final-issue handling

---

## 6. Physical Inventory (MI01, MI04, MI07)
> 🔴 Tier 1 · _Key points:_ Create document, count, post differences; posting block; cycle counting

### Definition
**Physical inventory (PI)** reconciles book stock with the physical count. Procedures:
- **Periodic (annual) inventory:** whole warehouse counted at year-end, with posting block on all materials.
- **Continuous inventory:** counts spread through the year; every material at least once.
- **Cycle counting:** frequency by ABC class (e.g. A counted 4 times, B twice, C once), driven by a **CC indicator** and run with `MICN`.
- **Inventory sampling:** random sample of materials, extrapolated; allowed under statutory conditions.

**Process:**
1. `MI01` **create PI document** (list of materials, batch, storage location, special stock); optional **posting block** (no goods movements while counting) and **freeze book inventory** (system stock frozen at that moment for fair comparison). Print with `MI21`.
2. `MI04` **enter count** (counted quantity; zero count flag). `MI11` recount if difference exceeds tolerance.
3. `MI20` **list of inventory differences** (qty and value) for approval.
4. `MI07` **post differences**: movement type **701** (gain) or **702** (loss) for unrestricted stock; accounting Dr/Cr GBB/INV.
5. `MI02` change, `MI03` display; `MI09` count without reference doc.

See the governance and ABC logic in [[116 Inventory Valuation, Cycle Counting & Inventory Governance]].

### Example
System shows 500 kg of HDPE; count is 488 kg. Difference −12 kg at MAP ₹95 = **₹1,140** loss, posted with 702: Dr Inventory difference ₹1,140, Cr Stock ₹1,140. If the tolerance is ₹1,000 per item for the approving clerk, this posting needs a recount (`MI11`) or manager approval. Inventory accuracy = items counted correctly / total items counted; 95 of 100 correct = 95%.

### In the news
See news box. Count tools and Fiori apps change with each release; the document logic (create, count, post differences) does not.

### Interview angle
> [!question] How it is asked
> "Describe the physical inventory process in SAP, step by step with T-codes." or "What does freezing the book inventory do?"

> [!tip] Strong answer includes
> - `MI01` to `MI04` to `MI07` and the 701/702 accounting
> - Posting block and freeze book inventory
> - Cycle counting by ABC class; recount on tolerance breach
> - Root-cause follow-up (`MB51` history, receiving errors) rather than just adjusting

---

## 7. Batch Management and Classification
> 🔴 Tier 1 · _Key points:_ Batch master, classification, shelf life, batch determination, where-used list

### Definition
A **batch** is a homogeneous subset of a material produced or procured together, with its own specifications and stock. It is switched on in the material master (**batch management requirement** indicator, Purchasing or Plant data/storage view). Features:
- **Batch master** (`MSC1N` create, `MSC2N` change, `MSC3N` display): batch number, manufacture date, **shelf-life expiry date (SLED)**, status (restricted/unrestricted), vendor batch.
- **Batch classification:** characteristics (`CT04`) grouped in classes of class type **023** (`CL02`), e.g. potency, moisture, colour; values recorded from QM results or entered. Used for searching and for selection.
- **Shelf-life data:** total shelf life and **minimum remaining shelf life** in the material master; GR can derive SLED from the manufacture date; `MB5M` lists materials near expiry; in SD, a customer may demand a minimum remaining shelf life at delivery.
- **Batch determination:** the system proposes batches through a **strategy** (search procedure + strategy types with sort rules such as FEFO: first-expired-first-out) in MM (`MBC1`), PP (`COB1`) or SD (`VCH1`).
- **Where-used list** (`MB56`): all customers/orders where a batch ended up, essential for recalls.
- **Valuation:** a batch can also be a valuation type (batch-level split valuation).

### Example
A dairy-drink batch B2603-01 is produced on 1 Mar 2026 with 365 days of shelf life, so SLED = 1 Mar 2027. A key-account customer requires at least 180 days of remaining shelf life at delivery, so the last day to dispatch from that batch is 2 Sep 2026 (1 Mar 2027 minus 180 days). On 15 Aug 2026 the batch has 198 days left. A contamination alert triggers `MB56`, which lists every delivery and customer that received B2603-01.

### In the news
See news box. IDES24's 2025 notes mention batch-specific units of measure in EWM, aimed at catch-weight products such as meat and dairy.

### Interview angle
> [!question] How it is asked
> "What is batch management and how would you implement FEFO in SAP?" or "How do you trace a batch in a product recall?"

> [!tip] Strong answer includes
> - Batch master, classification (class type 023), SLED
> - Batch determination strategy with FEFO sorting in MM/PP/SD
> - `MB56` where-used and recall process; link to QM ([[084 SAP QM & PM]])
> - Industry use: pharma, food, chemicals, FMCG

---

## 8. Serial Numbers
> 🔴 Tier 1 · _Key points:_ Serial number profile, equipment master, serialisation procedures

### Definition
A **serial number** identifies a single unit of a material (an item with warranty or maintenance history). In SAP each serial number is stored in an **equipment master record** (category S) linked to the material. Set-up:
1. **Serial number profile** (`OIS2`) with serialisation procedures that control when numbers are mandatory (e.g. at goods receipt, goods issue, delivery).
2. Assign the profile in the material master (Plant data / Sales: general).
3. Create or enter serial numbers at the movement (automatic assignment or manual list), with an **obligation** setting (mandatory, optional, automatic).

Reports: `IQ03` display a serial number, `IQ09` stock list by serial number, `IQ01` create. Serial numbers also feed warranty tracking in PM and service. Difference from batch: **batch** = a lot with common properties (quantity many), **serial** = one unit, unique, quantity one.

### Example
An electronics distributor receives 200 smart meters. The profile requires serialisation at GR and delivery: 200 numbers are recorded at GR; when 40 meters are delivered, the delivery needs exactly 40 serial numbers selected from stock. If a meter fails within warranty, its serial history shows vendor, GR date, customer and delivery. A batch would only tell which lot of 200 it came from.

### In the news
See news box. In regulated or electronics supply chains, unit-level traceability is the practical use of serial numbers on S/4HANA.

### Interview angle
> [!question] How it is asked
> "Batch vs serial number in SAP: when do you use each?"

> [!tip] Strong answer includes
> - Batch (group) vs serial (unit), equipment master link
> - Profile with obligation and procedures (`OIS2`)
> - Reports (`IQ09`) and use in warranty/PM
> - Cost: more data entry; use only where unit traceability pays

---

## 9. Special Stocks: Overview
> 🔴 Tier 1 · _Key points:_ Special stock indicators E, K, M, O, P, Q, V, W; ownership vs location

### Definition
**Special stocks** are stocks managed separately from the plant's own unrestricted stock because of **ownership** (vendor or customer) or **assignment** (to a sales order or project). They are managed with a **special stock indicator** and are shown in `MMBE` and `MB52`.

| Indicator | Name | Ownership / assignment | Valuated at your company? |
|---|---|---|---|
| **K** | Vendor consignment | Vendor owns, stored at your site | No, until consumed |
| **O** | Parts provided to vendor (subcontracting) | You own, stored at vendor | Yes (your balance sheet) |
| **E** | Sales order stock (make-to-order) | Yours, tied to a sales order item | Yes, usually valuated per order |
| **Q** | Project stock | Yours, tied to a WBS element | Yes, per project |
| **M** | Returnable packaging (vendor) | Vendor-owned, at your site | No |
| **V / W** | Customer returnable packaging / customer consignment | Yours, at the customer | Yes |
| **P** | Pipeline | Vendor-owned material in a pipeline | No, liability on withdrawal |

Special stock appears under the movement, e.g. 101K (GR into consignment) or 411 E (transfer to sales order stock). It has separate MRP planning segments (e.g. sales-order stock covers only that order).

### Example
A machinery maker sells a customised turbine under a make-to-order sales order. Planned production creates stock in **E** (sales order 5000123/10), not in the plant's general pool: only that order can use it, and valuation is carried per order. A spare steel plate in plant stock cannot be allocated to it unless transferred by 411 E. Project stock **Q** works the same with the WBS element for capex projects.

### In the news
See news box. Special stocks must be mapped one by one during S/4HANA conversion because their ownership logic affects balance-sheet inventory.

### Interview angle
> [!question] How it is asked
> "What are the special stock types and who owns the stock in each?"

> [!tip] Strong answer includes
> - Indicators and ownership: K vendor, O own at vendor, E/Q tied to order/project
> - Valuation consequence (K not valuated until consumed)
> - How MRP treats them (separate segments)
> - Business case for each

---

## 10. Consignment and Pipeline Procurement
> 🔴 Tier 1 · _Key points:_ Info record K, 101K, withdrawal liability, MRKO settlement

### Definition
In **consignment**, the vendor places stock at your site and keeps ownership until you use it. Process:
1. **Consignment info record** (`ME11`, info category *Consignment*) holds the price; **PO item category K** carries no price of its own.
2. **GR 101 (consignment)** posts to vendor consignment stock (special stock K): **no FI posting**, quantity only.
3. **Consumption** (`201`/`261` from consignment stock) or **transfer to own stock** (`411 K`) creates a **liability**: Dr Consumption, Cr Consignment liability (**KON**).
4. **Settlement:** `MRKO` creates the vendor invoice: Dr Consignment liability, Dr Input GST, Cr Vendor. Frequency (weekly or monthly) is a commercial agreement.
5. **Return:** unused stock returned with 122K or via a return PO.

**Pipeline** (materials like gas, water, power) works similarly but with no goods receipt: withdrawal of a quantity creates the liability, settled through `MRKO`.

Benefits: lower working capital, no inventory ownership risk; risk: obsolete stock lingers at the vendor's discretion unless contract limits it. Link to [[136 Supply Chain Finance & Working Capital]] for the cash effect.

### Example
A vendor stores 10,000 bolts valued at ₹2 each at your plant. Stock value on your books: **₹0**; vendor's own inventory ₹20,000. In March 2,500 bolts are consumed: liability = 2,500 × ₹2 = **₹5,000** (Dr Consumption ₹5,000, Cr KON ₹5,000). `MRKO` at month-end invoices ₹5,000 plus 18% GST ₹900 = **₹5,900** (Dr KON ₹5,000, Dr Input GST ₹900, Cr Vendor ₹5,900). The other 7,500 bolts (₹15,000) remain the vendor's asset.

### In the news
See news box. Consignment and VMI flows are a standard test scenario in any ECC-to-S/4HANA migration; the movement logic stays the same.

### Interview angle
> [!question] How it is asked
> "How does consignment procurement work in SAP and what is the accounting?"

> [!tip] Strong answer includes
> - Consignment info record and 101K with no FI posting
> - Liability at consumption (KON) and `MRKO` settlement
> - Working-capital advantage with numbers
> - Risk: obsolescence and contract caps

---

## 11. Subcontracting (Provision of Components) and Returnable Packaging
> 🔴 Tier 1 · _Key points:_ PO item L, 541 provision, 543 consumption, fee-only liability, GST job work

### Definition
In **subcontracting** you buy a processed item and send the components to the vendor. Process:
1. **PO** with item category **L** for the finished item; the **BOM** supplies components (a subcontracting BOM or plant BOM).
2. **Provide components** with **541** (stock moves to special stock **O**, still valued on your books, no FI posting) via `MIGO` or `ME2O` (subcontracting cockpit).
3. **GR 101 of the finished item** against the PO: the finished material enters stock, **543** automatically consumes the provided components, and the service fee is posted to GR/IR.
4. **Invoice** the fee only: Dr GR/IR, Dr Input GST, Cr Vendor.
5. Monitoring: `MBLB` (stock with subcontractor), `ME2O`.

Price of finished item = components consumed + service fee. In India the principal sends goods under a **delivery challan** (job work, section 143 of the CGST Act); inputs are returned or supplied within one year, and capital goods within three, or GST becomes payable; periodic (quarterly or half-yearly, depending on turnover) **ITC-04** reporting applies. Returnable packaging: **M** (vendor-owned crates at your site) and **V** (yours at the customer) track containers by quantity with deposit pricing.

### Example
1,000 castings, MAP ₹200 each (₹2,00,000), are provided to a machining vendor. The fee is ₹30 per piece (₹30,000). On GR of 1,000 machined parts: Dr Finished stock ₹2,30,000 (₹230 per piece), Cr GR/IR ₹30,000 (fee), Cr Component stock (543 consumption) ₹2,00,000. If only 980 pieces come back and 20 castings are scrapped, the components of the 20 consumed castings can be consumed via 543 and become a cost, or recovered from the vendor as per contract. See deeper process in [[192 SAP Sourcing & Procurement Deep Dive]].

### In the news
See news box. Subcontracting flows are among the processes in India under tight GST job-work compliance, an ECC-to-S/4HANA test scenario.

### Interview angle
> [!question] How it is asked
> "Walk me through the subcontracting process and its accounting in SAP."

> [!tip] Strong answer includes
> - PO item L, 541 to O stock, GR 101 with 543, fee in GR/IR
> - Who owns components (you) and how value builds in the finished item
> - Monitoring and reconciliation (`MBLB`, `ME2O`)
> - GST challan and ITC-04 in India

---

## 12. Split Valuation
> 🔴 Tier 1 · _Key points:_ Valuation category, valuation type, separate MAP per type

### Definition
**Split valuation** values one material in the same plant as several partial stocks, each with its own price and quantity, instead of one average. Use it when stocks differ in origin, quality or status, or per batch.
- **Valuation category** (e.g. origin, batch, status): classification in the material master; activated globally (`OMW0`) and defined with valuation types (`OMWC`).
- **Valuation types** (e.g. DOMESTIC, IMPORTED): each has own quantity, value, price control and account assignment through valuation class.
- **Procurement:** POs and goods movements must name the valuation type; transfers between types (309/ "split valuation transfer") change the valuation.
- Reporting: `MMBE` and `MB52` show each type; `MB5B` shows value by type.

Benefits: transparent cost for imported versus local supply; batch-level costing in pharma and chemicals; avoids "blended" MAP hiding cost differences.

### Example
Plant holds 500 kg domestic steel at ₹60 (₹30,000) and 300 kg imported at ₹68 (₹20,400). Blended MAP would be 50,400 / 800 = **₹63**. With split valuation, issuing 100 kg domestic costs ₹6,000 vs ₹6,300 blended; issuing 100 kg imported costs ₹6,800. A product that requires imported steel carries ₹6,800 per 100 kg, so margin analysis reflects real sourcing.

### In the news
See news box. Imported inputs with different landed costs are the classic split-valuation case, so it is on every migration checklist.

### Interview angle
> [!question] How it is asked
> "What is split valuation and when would you use it?"

> [!tip] Strong answer includes
> - Valuation category and types; separate MAP per type
> - Cases: origin (domestic/import), batch, quality status
> - Posting needs valuation type on PO/movement
> - Numeric comparison blended vs split MAP

---

## 13. Key T-codes, Reports and Fiori Apps
> 🔴 Tier 1 · _Key points:_ MIGO, MB52, MMBE, MB51, MB5B, MB5L, MBLB, Fiori equivalents

### Definition
`MIGO` (goods receipt, issue, transfer, return) is the one transaction behind nearly all movements (older `MB01`, `MB1A`, `MB1B`, `MB1C` exist). Reports:

| T-code | Use |
|---|---|
| `MMBE` | Stock overview per material by plant, sloc, stock type, special stock, batch |
| `MB52` | Warehouse stocks with value per sloc, one line per material |
| `MB51` | Material documents (movement history) |
| `MB5B` | Stocks on posting date (e.g. month-end balance) |
| `MB5L` | Stock value balances to reconcile to FI |
| `MB5T` / `MB5S` | Stock in transit / GR-IR analysis by PO |
| `MBLB` | Stock at subcontractor |
| `MB54` / `MB58` | Vendor consignment stock / customer consignment stock |
| `MB5M` | Shelf-life expiry list |
| `MB25` | Reservation list |
| `MB56` | Batch where-used |
| `MD04` | Stock/requirements list |

**Fiori equivalents** in S/4HANA include Stock Overview apps (single and multiple material), Material Documents Overview, Post Goods Movement, Manage Batches and Slow or Non-Moving Materials. KPIs: **inventory turns** = COGS / average inventory; **days of inventory** = 365 / turns.

### Example
COGS ₹240 crore, average inventory ₹30 crore: turns = 8, days of inventory = 365 / 8 ≈ **46 days**. A 5-day reduction in a ₹30 crore stock at 11% cost of capital frees ₹30 crore × 5/46 ≈ ₹3.26 crore of cash and saves about ₹36 lakh a year in carrying cost.

### In the news
See news box. Reports read directly from MATDOC in S/4HANA, so stock-by-posting-date reports no longer need separate aggregate tables.

### Interview angle
> [!question] How it is asked
> "Which T-code shows stock per storage location with value, and which shows movement history?"

> [!tip] Strong answer includes
> - Right report for each question (MMBE/MB52/MB51/MB5B)
> - Reconciliation path to FI (`MB5L`)
> - Fiori counterparts
> - KPIs from the data (turns, days of inventory, ABC)

---

## 14. ⭐ Advanced: S/4HANA Inventory Management Changes (MATDOC, Negative Stock)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
S/4HANA redesigned inventory management for speed:
- **MATDOC** is a single table for material document header and items; `MKPF` and `MSEG` remain as compatibility views. Stock quantities in the old aggregate tables (`MARD`, `MCHB`, `MSKA`, `MKOL` and so on) are no longer stored; compatibility views (e.g. `NSDM_V_MARD`) compute them from MATDOC on the fly. Result: fewer database locks, higher throughput for goods movements (backflush, handheld scans), and stock "as of any date" without separate history tables.
- **Material Ledger always on:** valuation postings flow into ML tables and the Universal Journal.
- **Negative stocks:** allowed only if enabled at plant, storage location and material level; values are posted at the current price and corrected when later receipts cover the negative quantity (price differences result). Use sparingly: negative stock indicates late GR posting.
- **Material number** length up to 40 characters; MIGO is gradually replaced by the Fiori "Post Goods Movement" app in the cloud edition.
- **Simplified interfaces:** custom code reading `MARD` or `MSEG` has to be checked in the custom-code analysis ([[200 SAP S-4HANA Migration, Data Migration & Testing]]).

### Example
A warehouse posts thousands of goods movements in a peak hour (backflush, handheld scans). In ECC each movement updated the document tables and the aggregate stock rows, creating lock contention on popular materials; in S/4HANA each movement inserts a MATDOC row and stock is aggregated when queried, so there is no row-lock queue. A negative-stock case: a store issues 10 units while only 4 are booked because GR is late; the book stock is −6 until the GR posts, and the price difference (GR price vs MAP) on the covered 6 units goes to a difference account.

### In the news
See news box. As ECC extended maintenance ends in 2030 (standard in 2027), custom stock reports reading old tables are a common migration finding.

### Interview angle
> [!question] How it is asked
> "What changes in inventory management in S/4HANA compared to ECC?"

> [!tip] Strong answer includes
> - MATDOC, compatibility views and removal of aggregates
> - ML always on, Universal Journal integration
> - Negative-stock policy and its valuation effect
> - Impact on custom code, reports and testing; see [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]] for rapid recall
