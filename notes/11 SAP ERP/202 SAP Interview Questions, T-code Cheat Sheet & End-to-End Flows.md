---
tags: [sap-erp, tier1]
area: SAP ERP
topic: "SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows

⬅ [[201 SAP Landscape, Transports, Security & GRC Basics]] · [[_Index - SAP ERP|SAP ERP]] · [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]] ➡

> **Area:** SAP ERP · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Procure-to-Pay: Flow, T-codes, Tables and Postings]]
2. [[#2. Order-to-Cash: Flow, T-codes, Tables and Postings]]
3. [[#3. Plan-to-Produce: Flow, T-codes, Tables and Costing]]
4. [[#4. Record-to-Report: FI Integration and Account Determination]]
5. [[#5. Quality and Maintenance Flows: Inspect-to-Release and Notify-to-Settle]]
6. [[#6. Key Tables Cheat Sheet (ECC and S/4HANA)]]
7. [[#7. T-code Cheat Sheet: MM, Inventory, WM and EWM]]
8. [[#8. T-code Cheat Sheet: PP, SD, QM, PM, FI/CO and General]]
9. [[#9. Interview Questions: MM and Procurement (Q1–Q18)]]
10. [[#10. Interview Questions: PP and SD (Q19–Q36)]]
11. [[#11. Interview Questions: WM, QM and PM (Q37–Q50)]]
12. [[#12. Interview Questions: FI Integration and S/4HANA (Q51–Q66)]]
13. [[#13. Scenario Questions and Troubleshooting Playbooks]]
14. [[#14. ⭐ Advanced: How to Answer SAP Questions and What to Avoid]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Cloud ERP momentum and the ECC deadline keep SAP skills in demand
> **SAP Q2 2026 results (23 Jul 2026).** Current cloud backlog reached **€22.9 billion**, up **27%** (26% at constant currencies); cloud revenue grew 22% (24% constant currency); **Cloud ERP Suite revenue grew 25%** (27% constant currency); total revenue rose 9% (11% constant currency). SAP's CEO attributed the momentum to its "Autonomous Enterprise" strategy and customer interest in AI grounded in business processes. ([SAP News Center](https://news.sap.com/2026/07/sap-announces-q2-and-half-year-2026-results/))
>
> **The ECC clock (SAP, 4 Feb 2025; e3mag, 23 Oct 2025).** Standard maintenance for SAP ERP/ECC runs to end-2027 (mainstream) and end-2030 (extended). SAP's paid "private edition, transition option" is purchasable from 2028 and usable 2031–2033, but SAP says it is not a maintenance prolongation. ([SAP News Center](https://news.sap.com/2025/02/sap-erp-private-edition-transition-option-navigate-complex-rise-with-sap-transformations/); [e3mag](https://e3mag.com/en/deadline-extension-for-ecc-6-0-until-2033/))
>
> **Three real migration routes (Computer Weekly, 6 Jan 2026).** Twinings Ovaltine (greenfield on RISE, two customisations), QD Group (brownfield, "on time, on budget, no incidents") and Imperial Brands (selective migration, about 50 ERPs into one S/4HANA instance). ([Computer Weekly](https://www.computerweekly.com/news/366636765/S4Hana-in-2026-Three-ways-to-move-off-SAP-ECC))
>
> Sub-topics that say **"See news box"** reuse these items. Module deep dives: [[080 SAP MM — Materials Management]], [[081 SAP PP — Production Planning]], [[082 SAP SD — Sales & Distribution]], [[083 SAP WM-EWM — Warehouse]], [[084 SAP QM & PM]].

---
## 1. Procure-to-Pay: Flow, T-codes, Tables and Postings
> 🔴 Tier 1 · _Key points:_ PR, RFQ, PO, GR, IR, payment; GR/IR; EKKO/EKPO/EKBE

### Definition
**Flow:** need identified (MRP or user) → **PR** `ME51N` → **RFQ** `ME41` → quotation `ME47` → comparison `ME49` → **PO** `ME21N` (release `ME29N` if release strategy) → **GR** `MIGO` (movement 101) → **IR** `MIRO` → payment `F110` (run) or `F-53` (manual).

**Tables:** `EBAN` PR; `EKKO` PO header; `EKPO` PO item; `EKET` schedule lines; `EKKN` account assignment; `EKBE` PO history (GR/IR documents); `RBKP/RSEG` invoice header/items; `LFA1/LFB1/LFM1` vendor general/company/purchasing; `MKPF/MSEG` material documents in ECC, **MATDOC** in S/4HANA.

**Postings (valuated stock item, GST ignored):**
| Step | Debit | Credit |
|---|---|---|
| GR (101) | Inventory (BSX) | GR/IR clearing (WRX) |
| IR | GR/IR clearing; price difference (PRD) if price differs under standard price | Vendor (payables) |
| Payment | Vendor | Bank |

Related depth: [[192 SAP Sourcing & Procurement Deep Dive]], [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]].

### Example
PO for 1,000 kg at ₹95/kg. GR of 600 kg: Dr Inventory 57,000 / Cr GR/IR 57,000 (600 × 95). Vendor invoice for those 600 kg at ₹97: invoice value 58,200 (600 × 97). Clear GR/IR 57,000 and, with standard price control, book the 1,200 difference to price difference account. With 18% GST intra-state: input CGST 5,238 and SGST 5,238, vendor credited 68,676 (58,200 × 1.18). Remaining 400 kg stays open on the PO.

### In the news
See news box. Procure-to-pay is the most common first process in S/4HANA programmes; the Twinings and QD Group projects both had to move this chain.

### Interview angle
> [!question] How it is asked
> "Explain procure-to-pay in SAP with T-codes, documents created and accounting entries."

> [!tip] Strong answer includes
> - Sequence with documents (PR, PO, material document, accounting document, invoice document)
> - GR/IR logic and what happens on a price difference
> - Where the process can be blocked (release strategy, invoice blocks, tolerances)
> - Mention that S/4HANA keeps T-codes but changes tables (MATDOC, BP)

---
## 2. Order-to-Cash: Flow, T-codes, Tables and Postings
> 🔴 Tier 1 · _Key points:_ Inquiry to payment; delivery and billing; VBAK/VBAP/LIKP/VBRK

### Definition
**Flow:** inquiry `VA11` → quotation `VA21` → **sales order** `VA01` → availability check/credit check → **outbound delivery** `VL01N` → picking (and WM transfer order) → **post goods issue** (PGI) `VL02N` (movement 601) → **billing** `VF01` → incoming payment `F-28`, customer items `FBL5N`.

**Document types (defaults):** order OR, quotation QT, inquiry IN, returns RE, credit memo request CR, debit memo request DR; delivery LF; billing F2 invoice, G2 credit memo, L2 debit memo, S1 cancellation.

**Tables:** `VBAK` sales header, `VBAP` item, `VBEP` schedule lines, `VBKD` business data, `VBPA` partners, `LIKP/LIPS` delivery, `VBRK/VBRP` billing, `VBFA` document flow, `KNA1/KNB1/KNVV` customer; pricing in `KONV` (ECC) / `PRCD_ELEMENTS` (S/4HANA); status tables `VBUK/VBUP` were removed in S/4HANA (status fields moved into header/item tables).

**Postings:** PGI: Dr COGS (GBB/VAX) / Cr Inventory (BSX). Billing: Dr Customer receivable / Cr Revenue (VKOA) / Cr output GST. Payment: Dr Bank / Cr Customer. See [[195 SAP SD Advanced - Pricing, Output & Document Flow]].

### Example
500 units at ₹1,200 list = 6,00,000; 5% customer discount = 30,000; net 5,70,000; 18% GST = 1,02,600; invoice 6,72,600. Standard cost ₹800/unit gives COGS 4,00,000 at PGI. Gross margin = 5,70,000 − 4,00,000 = 1,70,000, which is 29.8% of net revenue. Intra-state sale splits GST into CGST and SGST (JOCG, JOSG); inter-state uses IGST (JOIG).

### In the news
See news box. The cloud ERP suite growth SAP reports includes order-to-cash modules, where e-invoicing and credit management are common reasons to modernise.

### Interview angle
> [!question] How it is asked
> "Walk through order-to-cash and say where revenue and COGS are recognised."

> [!tip] Strong answer includes
> - Order, delivery, PGI, billing, payment, with documents and tables
> - Stock reduces and COGS is booked at PGI; revenue at billing
> - Blocks: credit, delivery, billing, incompletion, no stock
> - Document flow `VBFA` to trace and GST determination in India

---
## 3. Plan-to-Produce: Flow, T-codes, Tables and Costing
> 🔴 Tier 1 · _Key points:_ MRP, planned order, production order, confirmation, GR, settlement

### Definition
**Master data:** material master with MRP view, BOM (`CS01`), work centre (`CR01`), routing (`CA01`), production version. **Flow:** demand (sales orders, forecast, planned independent requirement `MD61`) → **MRP** `MD01N` (or `MD02` multi-level) → review `MD04` → **planned order** → convert `CO40`/`MD04` or create **production order** `CO01` → release `CO02` (status REL) with material availability check `CO24` → goods issue/backflush `MIGO` movement 261 → confirmation `CO11N` (status CNF) → GR of finished goods `MIGO` movement 101 → technical completion (TECO) → variance calculation `KKS1` → settlement `CO88` → CLSD.

**Order statuses:** CRTD created, REL released, PCNF partially confirmed, CNF confirmed, DLV delivered, TECO technically completed, CLSD closed.

**Tables:** `AUFK` order master, `AFKO` order header (PP), `AFPO` order item, `AFVC/AFVV` operations, `RESB` reservations/components, `AFRU` confirmations, `PLAF` planned orders, `STKO/STPO` BOM header/items, `MAST` material-BOM link, `PLKO/PLPO` routing header/operations, `CRHD` work centre, `MDKP/MDTB` MRP header/lines. Depth: [[193 SAP MRP Deep Dive - Planning Strategies & Parameters]], [[194 SAP Production Execution, Confirmation & Product Costing]].

### Example
Order for 1,000 kg. Standard cost ₹250/kg, so standard value 2,50,000. Actual order costs (components + activities + overheads) total 2,62,500. Variance = 12,500 unfavourable. At settlement the order debits stock at standard (2,50,000, via GR) and the variance goes to a price/production variance account; the order balance becomes zero and the order is closed.

### In the news
See news box. MRP Live on HANA (a headline change in S/4HANA) shortens planning runs, which is why manufacturers target planning for early wins.

### Interview angle
> [!question] How it is asked
> "Describe the end-to-end flow from demand to finished goods receipt in SAP PP, including costing."

> [!tip] Strong answer includes
> - Master data prerequisites (BOM, routing, work centre) and MRP controller view
> - Planned order vs production order; release and availability check
> - 261 issue, confirmation, 101 receipt, TECO, variance, settlement
> - Costing: planned vs actual, variance categories

---
## 4. Record-to-Report: FI Integration and Account Determination
> 🔴 Tier 1 · _Key points:_ OBYC, valuation class, GR/IR, period close, universal journal

### Definition
Logistics postings create FI documents automatically through **account determination**: for materials, a movement type points to a **transaction key** (BSX inventory, WRX GR/IR, GBB offsetting entry with account modifiers such as VBR for consumption or VAX for sales, PRD price differences), and the material's **valuation class** (material master, accounting view) selects the GL account via `OBYC` configuration. For SD revenue the analogue is `VKOA`. See [[190 SAP FI-CO Essentials for Operations Professionals]].

**Period-end (R2R) logistics steps:** `MMPV` period close for MM, `MR11` GR/IR maintenance/clearing, `MRBR` release blocked invoices, `CKMLCP` actual costing run (if material ledger actual costing is used), `KKS1`/`CO88` production variances and settlement, `AFAB` depreciation, `F.13` automatic clearing, `FAGLL03`/`FBL3N` line item review, `F.01` financial statements, and carry forward balances.

**S/4HANA:** **Universal Journal `ACDOCA`** holds FI, CO, asset and material-ledger line items in one table; compatibility views replace `BSIS/BSAS/BSID/BSAD/BSIK/BSAK` index tables; the material ledger is mandatory.

### Example
Movement 261 (issue to production): Dr Consumption/WIP (via GBB with modifier) / Cr Inventory (BSX) at the material's valuation. Month-end: GR/IR balance 3,20,000 relates to deliveries not invoiced; finance accrues it using `MR11` only for items confirmed as no longer expected, and the rest stays open as a liability for goods received not invoiced.

### In the news
See news box. In the Computer Weekly cases, finance and data teams drive scope: record-to-report is where ECC to S/4HANA differences (ACDOCA, ML) are most visible.

### Interview angle
> [!question] How it is asked
> "How does a goods movement end up in FI, and what changes in S/4HANA?"

> [!tip] Strong answer includes
> - Movement type to transaction key to valuation class to GL account
> - Examples: 101 uses BSX and WRX; 261 uses BSX and GBB
> - Period-end clean-up tasks and who owns them
> - Universal journal and mandatory material ledger in S/4HANA

---
## 5. Quality and Maintenance Flows: Inspect-to-Release and Notify-to-Settle
> 🔴 Tier 1 · _Key points:_ GR creates inspection lot; UD posts stock; notification, order, confirm, TECO, settle

### Definition
**Quality (inbound):** material with QM inspection type active; PO placed (QM info record `QI01` may be needed); GR in `MIGO` (101) puts stock in **quality inspection stock** and creates an **inspection lot** (`QA32` list); results recorded `QE51N`/`QE01`; **usage decision** `QA11` posts stock to unrestricted, blocked, scrap, or returns; rejection can create a **quality notification** `QM01` and a return delivery (122). Depth: [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]].

**Maintenance:** **notification** `IW21` (M1 request, M2 malfunction, M3 activity) → **order** `IW31` (planned operations, components, costs) → release → issue spares (261 against reservation) → **confirmation** `IW41` → **TECO** (`IW32`) → **settlement** `KO88` to the cost centre/asset. Preventive path: maintenance plan `IP01` scheduled by `IP10`. Depth: [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]].

**Tables:** `QALS` inspection lot, `QAVE` usage decision, `QAMV/QAMR` characteristic specs/results, `QMEL` notification (QM and PM), `AFIH` maintenance order header, `EQUI` equipment, `IFLOT` functional location, `MPLA/MPOS` maintenance plan/item.

### Example
GR of 5,000 valves creates lot with 125 pieces sampled; 3 defective with acceptance number 3 → UD "A": 5,000 pieces move from inspection stock to unrestricted. If 4 had failed (reject number 4), UD "R" would block stock, create a vendor complaint, and trigger return delivery. For PM: a pump seal leak (M2) takes 4 hours; the order shows labour 4 h × ₹450 × 2 technicians = ₹3,600 and a seal kit ₹1,850; settlement debits the cost centre ₹5,450.

### In the news
See news box. Quality and maintenance are where SAP's intelligent asset management and automotive quality exchange initiatives sit; the underlying notifications and orders remain the backbone.

### Interview angle
> [!question] How it is asked
> "What happens in SAP when a goods receipt is posted for a QM-relevant material?"

> [!tip] Strong answer includes
> - Stock goes to inspection stock; lot is created; sample, results, UD
> - UD posts to unrestricted/blocked/scrap; notification and returns on reject
> - PM chain: notification, order, confirm, TECO, settle
> - Link to vendor rating and MTBF reporting

---
## 6. Key Tables Cheat Sheet (ECC and S/4HANA)
> 🔴 Tier 1 · _Key points:_ Master data, documents, status, history; S/4HANA replacements

### Definition
| Domain | Table | Content |
|---|---|---|
| Material | `MARA` / `MAKT` | General data / descriptions |
| Material | `MARC` / `MARD` / `MBEW` | Plant data / storage location stock / valuation |
| Material | `MVKE`, `MLGN`, `MLGT`, `MARM` | Sales org data, WM data, units of measure |
| Batch, special stock | `MCH1/MCHA`, `MKOL`, `MSLB`, `MSKA`, `MARC` | Batches (client/plant), consignment at vendor, special stock at vendor, sales order stock |
| Material documents | `MKPF` + `MSEG` (ECC); `MATDOC` (S/4HANA) | Header and items |
| Reservations | `RKPF` / `RESB` | Header / items |
| Vendor | `LFA1`, `LFB1`, `LFM1`; BP: `BUT000` | General, company code, purchasing org |
| Customer | `KNA1`, `KNB1`, `KNVV` | General, company code, sales area |
| Purchasing | `EBAN`, `EKKO`, `EKPO`, `EKET`, `EKKN`, `EKBE`, `EINA/EINE`, `EORD` | PR, PO header/item, schedule, account assignment, history, info record, source list |
| Invoice | `RBKP`, `RSEG` | Invoice header, items |
| Sales | `VBAK`, `VBAP`, `VBEP`, `VBKD`, `VBPA`, `VBFA` | Header, item, schedule, business data, partners, document flow |
| Delivery, billing | `LIKP`, `LIPS`, `VBRK`, `VBRP` | Delivery and billing |
| Pricing | `KONH`, `KONP`, `KONV` (ECC) / `PRCD_ELEMENTS` (S/4) | Condition header/items, document conditions |
| Production | `AUFK`, `AFKO`, `AFPO`, `AFVC`, `AFRU`, `PLAF` | Order master, header, item, operations, confirmations, planned orders |
| BOM, routing | `STKO`, `STPO`, `MAST`, `PLKO`, `PLPO`, `MAPL`, `CRHD` | BOM, material-BOM link, routing, material-task list, work centre |
| MRP | `MDKP`, `MDTB` | MRP header and elements |
| Quality | `QALS`, `QAVE`, `QAMV`, `QAMR`, `QMEL`, `QPMK`, `QINF` | Lot, UD, characteristics, results, notification, master characteristic, QM info record |
| Maintenance | `EQUI`, `IFLOT`, `ILOA`, `AFIH`, `MPLA`, `MPOS`, `IMPTT`, `IMRG` | Equipment, functional location, location data, order header, plan, item, measuring point, measurement document |
| Org | `T001`, `T001W`, `T001L` | Company code, plant, storage location |
| FI | `BKPF`, `BSEG`, `ACDOCA` (S/4HANA), `BSIK/BSAK/BSID/BSAD` | Document header, items, universal journal, open and cleared items |

**S/4HANA to remember:** `MKPF/MSEG` and stock aggregate tables become compatibility views over `MATDOC`; `VBUK/VBUP` removed; `KONV` replaced by `PRCD_ELEMENTS`; open-item index tables become views on `ACDOCA`; customer/vendor master tables are kept in sync from Business Partner.

### Example
Find all open POs for vendor 100245 with delivery pending: join `EKKO` (LIFNR) with `EKPO` (ELIKZ not set) and `EKET`; pull received quantity from `EKBE` (VGABE = 1 GR). For stock by plant and storage location in ECC read `MARD`; in S/4HANA use the stock apps or `MATDOC`-based views rather than assuming the old aggregate update.

### In the news
See news box. Table-level knowledge is checked in migration interviews because Z reports reading `MSEG` directly are the most common custom-code finding in conversions (see [[200 SAP S-4HANA Migration, Data Migration & Testing]]).

### Interview angle
> [!question] How it is asked
> "Name the tables for PO header and item, material documents, and sales document flow. What changed in S/4HANA?"

> [!tip] Strong answer includes
> - EKKO/EKPO, MKPF/MSEG (MATDOC), VBFA, with one-line meanings
> - Use of the tables to answer a real question (open PO, delivered quantity)
> - Honest about S/4HANA replacements instead of reciting old names
> - Mention `SE16N` for display only, not for data fixes

---
## 7. T-code Cheat Sheet: MM, Inventory, WM and EWM
> 🔴 Tier 1 · _Key points:_ Master data, purchasing, inventory movements, warehouse

### Definition
| T-code | Purpose | T-code | Purpose |
|---|---|---|---|
| `MM01` | Create material | `MM02` | Change material |
| `MM03` | Display material | `MM06` | Flag for deletion |
| `MM60` | Material list | `MMBE` | Stock overview |
| `MM50` | Extend material views | `MMPV` | Close posting period |
| `BP` | Business partner (S/4) | `XK01` | Create vendor (ECC) |
| `XK02` | Change vendor (ECC) | `XK03` | Display vendor (ECC) |
| `MK01` | Create vendor, purchasing view | `FK01` | Create vendor, accounting view |
| `ME51N` | Create PR | `ME52N` | Change PR |
| `ME53N` | Display PR | `ME5A` | PR list |
| `ME41` | Create RFQ | `ME47` | Maintain quotation |
| `ME49` | Price comparison | `ME21N` | Create PO |
| `ME22N` | Change PO | `ME23N` | Display PO |
| `ME2N` | PO by number | `ME2L` | POs by vendor |
| `ME2M` | POs by material | `ME29N` | Release PO |
| `ME28` | Release PO (collective) | `ME31K` | Create contract |
| `ME31L` | Create scheduling agreement | `ME11` | Create info record |
| `ME01` | Maintain source list | `MEQ1` | Maintain quota arrangement |
| `ME9F` | Output messages for PO | `ME61` | Vendor evaluation |
| `MIGO` | Goods movement (GR, GI, transfer) | `MB51` | Material document list |
| `MB52` | Stock by plant / storage location | `MB5B` | Stock on posting date |
| `MB03` | Display material document | `MB21` | Create reservation |
| `MB1A` | Goods issue (obsolete in S/4) | `MIRO` | Enter invoice |
| `MIR4` | Display invoice | `MIR7` | Park invoice |
| `MRBR` | Release blocked invoices | `MR11` | GR/IR maintenance |
| `MR8M` | Cancel invoice | `MRKO` | Consignment settlement |
| `MI01` | Create physical inventory document | `MI04` | Enter count (with document) |
| `MI07` | Post differences | `MICN` | Cycle count documents |
| `MD01N` | MRP run (S/4HANA MRP Live) | `MD04` | Stock/requirements list |
| `MD05` | MRP list | `MD07` | Current stock/requirements list |
| `MMBE` | Stock overview | `ME03` | Display source list |
| `OBYC` | Automatic account determination | `OMJJ` | Customise movement types |
| `LT01` | Create WM transfer order | `LT03` | TO from transfer requirement |
| `LT12` | Confirm TO | `LS01N` | Create storage bin |
| `LS03N` | Display storage bin | `LX02` | Stock per bin |
| `LX03` | Bin status report | `LI01N` | Create WM inventory document |
| `LI11N` | Enter WM count | `LI20` | Clear WM differences |
| `/SCWM/MON` | EWM warehouse monitor | `/SCWM/PRDI` | EWM inbound delivery |
| `/SCWM/PRDO` | EWM outbound delivery | `/SCWM/RFUI` | EWM RF user interface |

### Example
A buyer finds out why a PO shows "delivery date past": `ME23N` (status) → `ME2N` (open items) → `MB51` (any GR posted?) → `MMBE` (stock) → `ME2L` (all POs for the vendor) → `ME61` (vendor performance). Six T-codes, one story; interviewers like this chained use.

### In the news
See news box. Many of these classic transactions survive in S/4HANA, but Fiori apps are the strategic UI; know both names.

### Interview angle
> [!question] How it is asked
> "Which T-code would you use to … (create PO, post GR, see stock, release PO, clear GR/IR)?"

> [!tip] Strong answer includes
> - The T-code plus what you check after (document number, status)
> - Notes on obsolete codes in S/4HANA (MB1A, XK01 replaced by MIGO, BP)
> - A short chain of T-codes for troubleshooting rather than isolated codes
> - Honesty: do not invent T-codes; say the menu path if unsure

---
## 8. T-code Cheat Sheet: PP, SD, QM, PM, FI/CO and General
> 🔴 Tier 1 · _Key points:_ Production, sales, quality, maintenance, finance, system tools

### Definition
| T-code | Purpose | T-code | Purpose |
|---|---|---|---|
| `CS01` | Create BOM | `CS02` | Change BOM |
| `CS03` | Display BOM | `CS11` | BOM level-by-level |
| `CR01` | Create work centre | `CR02` | Change work centre |
| `CA01` | Create routing | `CA02` | Change routing |
| `C201` | Create master recipe | `MD61` | Planned independent requirements |
| `MD40` | MPS run | `MD11` | Create planned order |
| `CO01` | Create production order | `CO02` | Change / release production order |
| `CO03` | Display production order | `CO40` | Convert planned to production order |
| `CO24` | Missing parts info | `CO11N` | Production order confirmation |
| `COOIS` | Order information system | `KKS1` | Variance calculation for orders |
| `CO88` | Settle production order | `CM01` | Work centre load |
| `CM21` | Capacity leveling | `MF50` | Planning table (repetitive) |
| `MFBF` | Repetitive backflush | `COR1` | Create process order |
| `VA01` | Create sales order | `VA02` | Change sales order |
| `VA03` | Display sales order | `VA05` | List of sales orders |
| `VA11` | Create inquiry | `VA21` | Create quotation |
| `VL01N` | Create outbound delivery | `VL02N` | Change delivery / post goods issue |
| `VL03N` | Display delivery | `VL06O` | Outbound delivery monitor |
| `VF01` | Create billing document | `VF02` | Change billing |
| `VF03` | Display billing | `VF04` | Billing due list |
| `VF11` | Cancel billing | `VK11` | Create condition record |
| `VK12` | Change condition record | `V/08` | Pricing procedure config |
| `VOFM` | Routines (requirements, formulas) | `VKOA` | Revenue account determination |
| `CO09` | ATP availability overview | `V.15` | Backorders |
| `VA14L` | Sales orders blocked for delivery | `FD32` | Customer credit (classic) |
| `UKM_BP` | Credit master data (FSCM) | `VKM1` | Blocked SD documents (classic) |
| `QP01` | Create inspection plan | `QP02` | Change inspection plan |
| `QP03` | Display inspection plan | `QS21` | Create master inspection characteristic |
| `QDV1` | Create sampling procedure | `QDP1` | Create sampling scheme |
| `QDR1` | Create dynamic modification rule | `QA01` | Create inspection lot manually |
| `QA32` | Inspection lot list | `QE51N` | Results recording worklist |
| `QE01` | Record results | `QA11` | Record usage decision |
| `QI01` | Create QM info record | `QM01` | Create quality notification |
| `QM02` | Change quality notification | `QM03` | Display quality notification |
| `IL01` | Create functional location | `IL03` | Display functional location |
| `IE01` | Create equipment | `IE03` | Display equipment |
| `IH01` | Functional location structure | `IH08` | Equipment list |
| `IB01` | Create equipment BOM | `IA05` | Create general task list |
| `IP01` | Create maintenance plan | `IP10` | Schedule maintenance plan |
| `IP30` | Deadline monitoring | `IP41` | Single-cycle plan |
| `IP42` | Strategy plan | `IK01` | Create measuring point |
| `IK11` | Create measurement document | `IW21` | Create PM notification |
| `IW28` | Notification list (change) | `IW29` | Notification list (display) |
| `IW31` | Create maintenance order | `IW32` | Change maintenance order |
| `IW38` | Order list (change) | `IW39` | Order list (display) |
| `IW41` | Time confirmation | `KO88` | Settle internal/PM order |
| `FB50` | Post G/L document | `FB60` | Enter vendor invoice (FI) |
| `FB70` | Enter customer invoice | `F-28` | Incoming payment |
| `F-53` | Outgoing payment | `F110` | Automatic payment run |
| `FB03` | Display FI document | `FB08` | Reverse FI document |
| `FBL1N` | Vendor line items | `FBL5N` | Customer line items |
| `FBL3N` | G/L line items | `FS00` | G/L account master |
| `F.01` | Financial statements | `F.13` | Automatic clearing |
| `AS01` | Create asset master | `AFAB` | Depreciation run |
| `ABZON` | Asset acquisition without vendor | `OB52` | Open and close posting periods |
| `KS01` | Create cost centre | `KSB1` | Cost centre line items |
| `KO01` | Create internal order | `KOB1` | Order line items |
| `CK11N` | Create product cost estimate | `CK24` | Mark and release cost estimate |
| `CKMLCP` | Actual costing run | `KE21N` | CO-PA posting |
| `SE16N` | Table display | `SE11` | Dictionary |
| `SE38` | ABAP editor / run report | `SM37` | Job overview |
| `SU01` | User maintenance | `PFCG` | Role maintenance |
| `SU53` | Last authorisation failure | `ST22` | ABAP dumps |
| `SM50` | Process overview | `SM12` | Lock entries |
| `SM21` | System log | `STMS` | Transport management |
| `SE09` | Transport organizer | `SPRO` | Configuration (IMG) |
| `SBWP` | Business workplace inbox | `SLG1` | Application log |
| `SM30` | Table maintenance | `SM36` | Schedule job |

### Example
A plant manager asks "why can't I confirm this order?" Chain: `COOIS` (status) → `CO03` (components, status REL?) → `CO24` (missing parts) → `MB52` (stock) → `CO02` (release) → `CO11N` (confirm). Matching each question to a code is the quickest way to show hands-on practice.

### In the news
See news box. Fiori launchpad tiles map to many of these codes; migration teams publish a mapping from classic T-codes to apps (consult SAP's Fiori apps reference library for the current list).

### Interview angle
> [!question] How it is asked
> "Name the T-codes you use daily in your module" or "Which T-code would you use to settle a production order?"

> [!tip] Strong answer includes
> - Cluster by process step instead of reciting a list
> - Mention a related report or status to check after the action
> - Correct handling of unknowns: describe path and purpose
> - Know which codes changed in S/4HANA (BP, MIGO replacing MB1x, MD01N)

---
## 9. Interview Questions: MM and Procurement (Q1–Q18)
> 🔴 Tier 1 · _Key points:_ Org, material and vendor master, valuation, GR/IR, release, special procurement

### Definition
**Q1. What does the material type control?** A: Which views exist, number range, price control default, whether quantity and value are updated (for example ROH raw material, HALB semi-finished, FERT finished, HAWA trading goods, DIEN service).

**Q2. At which level is stock valued?** A: Valuation area, normally the plant (or company code). Storage locations hold quantity only.

**Q3. Standard price (S) vs moving average (V)?** A: S fixes the price; differences post to price-difference accounts. V recalculates on each receipt or invoice: new price = total value / total quantity.

**Q4. What is GR/IR clearing?** A: A liability-like clearing account credited at GR and debited at invoice, so goods received but not invoiced remain visible; cleared by invoice or via `MR11`.

**Q5. What is three-way match and tolerance?** A: PO, GR and invoice must agree on quantity and price; tolerance keys (price, quantity, date) set allowed deviation, beyond which the invoice is blocked.

**Q6. Can a PO exist without a PR?** A: Yes; PR is optional, but PR gives approval, MRP traceability and budget control.

**Q7. What are source determination tools?** A: Source list (`ME01`), info record (`ME11`), quota arrangement (`MEQ1`), contracts and scheduling agreements; they pick vendor and price at PR/PO.

**Q8. Difference between consignment, subcontracting and stock transfer order?** A: Consignment: vendor owns stock until withdrawal. Subcontracting: components sent to vendor who returns finished goods. STO: movement between plants with PO, delivery, GR.

**Q9. Item categories in a PO?** A: Standard (blank), K consignment, L subcontracting, B limit, D service, U stock transfer.

**Q10. Account assignment categories?** A: K cost centre, A asset, F internal order, P project/WBS; they decide where consumption cost posts instead of inventory.

**Q11. How does a release strategy work?** A: Classification of PO values (release group, code, indicator, strategy) triggers approval; `ME28`/`ME29N` release. See [[080 SAP MM — Materials Management]].

**Q12. Why is an invoice blocked?** A: Price, quantity, date, project or manual blocks; release in `MRBR`.

**Q13. What are movement types 101, 102, 122, 201, 261, 301, 311, 321, 551, 561?** A: GR for PO, reversal, return to vendor, issue to cost centre, issue to production order, plant-to-plant transfer, sloc-to-sloc transfer, QI to unrestricted, scrap, initial stock.

**Q14. Which MRP types exist?** A: PD MRP, VB manual reorder point, VM automatic reorder point, ND no planning; lot sizes EX (lot for lot), FX fixed, HB replenish to maximum.

**Q15. How do you handle returns to vendor?** A: Movement 122 against the GR (or return PO item), then credit memo through invoice verification (`MIRO` credit memo).

**Q16. How do you manage batches and shelf life?** A: Batch management in the material master; shelf life expiration date (SLED); picking by FEFO/FIFO. See [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]].

**Q17. What is the physical inventory process?** A: Create document `MI01`, count `MI04`, post differences `MI07` (701 gain, 702 loss); block posting during the count.

**Q18. What is the difference between reservation and PR?** A: Reservation (`MB21`) reserves stock internally for consumption; PR triggers external procurement.

### Example
Moving average example for Q3: stock 100 kg at ₹90 (value 9,000); GR 50 kg at ₹96 (4,800). New MAP = 13,800 / 150 = ₹92.00. If an invoice later shows ₹99 for the 50 kg while all 150 kg are still in stock, the extra 150 (3 × 50) is capitalised, raising MAP to 13,950/150 = ₹93.00. If most of the goods had already been consumed, the portion relating to consumed quantity goes to the price-difference account instead.

### In the news
See news box. Procurement was the first process moved in the QD Group and Twinings programmes; expect migration-related follow-ups to these basics.

### Interview angle
> [!question] How it is asked
> Short, rapid-fire: "What is GR/IR?", "Standard vs MAP?", "Tell me the P2P flow."

> [!tip] Strong answer includes
> - A definition in one sentence, then an example with numbers
> - The accounting effect, not just the screen
> - The T-code or table you would look at
> - Awareness of S/4HANA differences when relevant

---
## 10. Interview Questions: PP and SD (Q19–Q36)
> 🔴 Tier 1 · _Key points:_ BOM, routing, MRP, order status, pricing, document flow, credit

### Definition
**Q19. Master data for a production order?** A: Material master (MRP and work scheduling views), BOM, routing/recipe, work centre, production version.

**Q20. Planned order vs production order?** A: Planned order is an MRP proposal with no costs collected; production order is the executable document with costing, reservations and confirmations.

**Q21. What happens when a production order is released?** A: Status REL; goods issue and confirmation are allowed; availability checks run (as configured); order can be printed.

**Q22. BOM usage?** A: Usage 1 production, 3 universal, 5 sales and distribution; BOM status controls release.

**Q23. Routing vs work centre?** A: Routing lists operations and standard values; the work centre provides capacity and cost-centre/activity link for costing.

**Q24. Common lot-sizing rules?** A: EX lot-for-lot, FX fixed, HB replenish to maximum, WB weekly, MB monthly.

**Q25. Planning strategies 10, 20, 40, 50?** A: 10 make-to-stock, 20 make-to-order, 40 planning with final assembly, 50 planning without final assembly.

**Q26. Backflushing?** A: Components are issued automatically (movement 261) at confirmation; set in work centre or component; saves manual issue.

**Q27. Order status flow?** A: CRTD, REL, PCNF, CNF, DLV, TECO, CLSD.

**Q28. How is production cost calculated?** A: Planned cost at order creation from BOM/routing; actual cost from issues and confirmations; variances at `KKS1`; settlement `CO88`.

**Q29. Discrete vs repetitive vs process manufacturing?** A: Discrete uses orders (`CO01`); repetitive uses run schedule quantities (`MFBF`); process uses process orders and recipes (`COR1`).

**Q30. SD organisational structure?** A: Sales organisation, distribution channel, division form the sales area; shipping point and plant handle delivery; company code handles accounting.

**Q31. Pricing condition technique?** A: Condition table, access sequence, condition type, pricing procedure (steps such as PR00 price, discounts, taxes). See [[195 SAP SD Advanced - Pricing, Output & Document Flow]].

**Q32. Item category vs schedule line category?** A: Item category controls pricing, billing and delivery relevance of the item (TAN); schedule line category controls MRP, availability check, delivery relevance (CP).

**Q33. How does the availability check work?** A: Checks ATP against stock plus planned receipts within replenishment lead time; result gives schedule lines; S/4HANA offers advanced ATP.

**Q34. How is credit management done?** A: Classic credit checks use credit control areas; modern S/4HANA uses SAP Credit Management with scores and credit limits (`UKM_BP`).

**Q35. Returns process?** A: Return order (RE), return delivery, goods receipt to returns/blocked stock, credit memo (CR) and billing.

**Q36. Third-party and intercompany sales?** A: Third-party: sales order creates PR/PO and vendor ships to customer; intercompany: billing between plants of different company codes with internal billing (IV).

### Example
Planning strategy example for Q25: a tyre maker holds 10,000 radial tyres; MTS (10) plans finished goods directly from forecast. For a customised mould (MTO, 20), nothing is produced until a sales order exists and the requirement is pegged to that order. A hybrid planning without final assembly (50) holds sub-assemblies (treads and belts) at forecast and finishes only when orders come.

### In the news
See news box. MRP Live and advanced ATP are specific S/4HANA improvements that planners cite in migration business cases.

### Interview angle
> [!question] How it is asked
> "Explain how a sales order flows into production and what documents are created."

> [!tip] Strong answer includes
> - Sales order requirement, MRP, planned order, production order, GR, delivery
> - Planning strategy and its effect on when production starts
> - Pricing, ATP and credit as SD controls
> - Document flow and tracing

---
## 11. Interview Questions: WM, QM and PM (Q37–Q50)
> 🔴 Tier 1 · _Key points:_ Bins and TOs, inspection lot and UD, notification and orders

### Definition
**Q37. WM structure?** A: Warehouse number, storage type, storage section, storage bin, quant; linked to plant/sloc in IM.

**Q38. TR vs TO?** A: A transfer requirement states what needs moving; a transfer order instructs the warehouse worker (source bin to destination bin) and is confirmed.

**Q39. Putaway and picking strategies?** A: Putaway: fixed bin, open storage, near picking bin, next empty bin; picking: FIFO, LIFO, partial pallets, shelf-life based. See [[083 SAP WM-EWM — Warehouse]].

**Q40. How do WM and IM stay reconciled?** A: Each IM posting has a WM transfer order trail; differences are cleared with inventory processes (`LI20`), interim storage types for GR/GI areas.

**Q41. WM vs EWM?** A: WM is the legacy module; EWM is process-oriented, with wave management and RF; embedded EWM runs inside S/4HANA. Check SAP's compatibility scope for dates before advising a client. See [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]].

**Q42. What inputs does QM need to inspect a GR?** A: Inspection type active in material master, an inspection plan or default characteristics, and (for vendors) QM control in the info record.

**Q43. What is an inspection lot?** A: The record to inspect a quantity under a plan; created on triggers like GR, production, delivery.

**Q44. What does the usage decision do?** A: Final accept/reject and stock posting; records quality score and may start follow-up actions.

**Q45. Quality notification types?** A: Q1 customer complaint, Q2 vendor complaint, Q3 internal problem, with tasks and activities. See [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]].

**Q46. Functional location vs equipment?** A: Location is where something works (persists); equipment is the physical object that can move and carries history.

**Q47. PM notification types?** A: M1 maintenance request, M2 malfunction report, M3 activity report.

**Q48. Maintenance plan types?** A: Single cycle, strategy plan, multiple counter plan; time-based, performance-based or condition-based.

**Q49. How do you compute MTBF/MTTR?** A: MTBF = operating time / failures, MTTR = repair time / repairs; availability = MTBF/(MTBF + MTTR). See [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]].

**Q50. How does PM integrate with MM and FI/CO?** A: Spare parts reservation and issue (MM), purchase requisitions for non-stock parts, order costs settled to cost centres or assets (FI/CO).

### Example
Q38 example: GR of 24 pallets posts to GR interim area; a TR is created; `LT03` makes a TO moving each pallet to a bin chosen by strategy; confirming the TO (`LT12`) clears interim stock, and the WM stock equals IM stock. If a worker places a pallet in a different bin, the TO confirmation records the actual bin.

### In the news
See news box. Equipment and quality data are the two areas where SAP is attaching AI and analytics (see [[203 SAP QM Deep Dive - Inspection, Usage Decision & Quality Notifications]] and [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]]).

### Interview angle
> [!question] How it is asked
> "Explain the warehouse putaway process in WM" or "What is an inspection lot and how is it closed?"

> [!tip] Strong answer includes
> - Object names in order (TR, TO, confirmation; lot, results, UD)
> - What stock type changes at each step
> - Triggers and the integration points to MM/PP/SD
> - Practical failure scenarios (no bin found, lot cannot close, order not releasable)

---
## 12. Interview Questions: FI Integration and S/4HANA (Q51–Q66)
> 🔴 Tier 1 · _Key points:_ Account determination, GR/IR, ML, ACDOCA, BP, MATDOC, Fiori

### Definition
**Q51. How does MM post to FI?** A: Movement type selects a transaction key; valuation class selects the GL account in `OBYC`; posting creates an FI document automatically.

**Q52. How does SD post to FI?** A: Billing creates revenue and receivable via condition type and `VKOA`; PGI posts COGS/inventory.

**Q53. How do intercompany stock transfers work?** A: Cross-company STO with GI (351) and GR, plus intercompany billing and clearing accounts. See [[190 SAP FI-CO Essentials for Operations Professionals]].

**Q54. What is the material ledger?** A: A parallel valuation ledger enabling actual costing, multiple currencies/valuations; mandatory in S/4HANA.

**Q55. How is withholding tax (TDS) handled?** A: Vendor master carries withholding tax type and section; tax is deducted at invoice or payment and credited to a TDS payable account; PAN is required.

**Q56. What is MMPV and why close periods?** A: It moves MM posting period so postings go to the correct month; closing prevents back-dated stock movements.

**Q57. What is document splitting / segment reporting?** A: A new GL feature that splits documents by characteristics (profit centre, segment) to enable balance sheets by dimension.

**Q58. What is the Universal Journal?** A: ACDOCA table holding all line items for FI, CO, assets and ML with one source of truth.

**Q59. What replaces vendor and customer masters?** A: Business Partner (`BP`) with roles (FLVN00/FLVN01 for vendor, FLCU00/FLCU01 for customer); CVI synchronises legacy tables.

**Q60. What is MATDOC?** A: New material document table merging MKPF/MSEG and stock aggregates, with stock computed from line items; compatibility views keep old code running.

**Q61. What is MRP Live?** A: HANA-optimised MRP (`MD01N`), runs in database; classic `MD01` is for compatibility.

**Q62. How long can a material number be?** A: Up to 40 characters if extended length is activated; was 18.

**Q63. What is Fiori and what is a launchpad?** A: A role-based web UI built from apps and tiles; SAP GUI remains available for classic transactions.

**Q64. What is advanced ATP?** A: HANA-based availability with product allocation and alternative-based confirmation (aATP).

**Q65. What is the Simplification List?** A: SAP's published list of removals and changes between ECC and S/4HANA, with required actions. See [[200 SAP S-4HANA Migration, Data Migration & Testing]].

**Q66. What is clean core?** A: Keeping the ERP standard and putting extensions in-app or side-by-side so upgrades are easy.

### Example
Q55 example: vendor invoice ₹1,00,000 for contractor services; TDS at 2% (as an illustrative rate; use the rate and section applicable to the vendor): TDS = 2,000; vendor payable = 98,000 (excluding GST), TDS payable = 2,000 until deposit to the government by the due date. Check section and rates against the current Income Tax provisions before quoting.

### In the news
See news box. SAP's Cloud ERP Suite growth (25% reported in Q2 2026, constant currency 27%) indicates more S/4HANA-related interview questions will cover cloud editions and clean core.

### Interview angle
> [!question] How it is asked
> "What are the biggest differences between ECC and S/4HANA that an MM/SD consultant should know?"

> [!tip] Strong answer includes
> - Five items: BP, MATDOC, ACDOCA, MRP Live, Fiori; plus clean-core and extensibility
> - Impact on custom code and reports
> - How you would test regression in a migration
> - Honest about versions (on-premise vs public cloud features differ)

---
## 13. Scenario Questions and Troubleshooting Playbooks
> 🔴 Tier 1 · _Key points:_ Symptom, hypothesis, T-code check, fix

### Definition
**S1. GR posted but invoice cannot be entered.** Check `ME23N` PO history: delivery completed? GR-based IV flag? `EKBE` for GR; look for invoice block; check tolerance keys and whether GR was reversed.

**S2. System stock differs from physical stock.** `MMBE` and `MB52` for IM; `LX02` for WM bin stock; `MB51` for last movements; consider unposted GI, batch/special stock, QI or blocked stock; run physical inventory and post differences (701/702) with approval.

**S3. Sales order cannot be delivered.** Check delivery block and billing block on `VA03`; credit block (`VKM1`/`UKM`); incompletion log; availability and schedule lines; shipping point and route determination; stock in plant/sloc; picking location.

**S4. Production order cannot be confirmed or released.** Check status (`CO03`), missing parts (`CO24`), component stock, operation status, capacity, and whether TECO or a deletion flag is set; negative stock settings and backflush flags.

**S5. MRP did not create a PR for a material.** Check MRP type and controller (MARC), planning run (`MD04`: net requirements), lot size, planning time fence, stock, open POs, deletion flag at plant, MRP group and strategy; run single-item planning (`MD03`).

**S6. Price in the PO is ₹95 but valuation shows ₹97.** Check the price control: standard (difference to PRD), MAP (invoice price change updates MAP only if stock is available); look at the invoice document and the material price history (`MR21` for price change).

**S7. Vendor payment is not released.** Check payment block in vendor/invoice, payment method, due date, `F110` proposal log, bank details and exceptions.

**S8. Incoming lot rejected, line stops.** UD reject, notification Q2, return delivery 122, request replacement, assess alternate source (source list/quotas); communicate to production planning.

**S9. A critical machine fails repeatedly.** Pull M2 notification history (`IW29`), damage and cause codes, MTBF/MTTR, order costs; Pareto the causes; revise the maintenance plan or spare parts stocking.

### Example
S6 worked: PO 1,000 kg at ₹95; MAP initially ₹90 with 1,000 kg; invoice at ₹97 for 600 kg when 1,600 kg stock exists (not enough consumption): the invoice difference (2 × 600 = 1,200) is capitalised to inventory, MAP becomes (value + 1,200)/quantity; if stock had been consumed first, the portion for consumed goods goes to the price-difference account instead.

### In the news
See news box. Post-go-live hypercare tickets in conversions mostly look like these scenarios (blocked invoices, stock mismatch, MRP behaviour); see [[200 SAP S-4HANA Migration, Data Migration & Testing]].

### Interview angle
> [!question] How it is asked
> "Users complain that MRP is not planning a critical material. Walk me through your analysis."

> [!tip] Strong answer includes
> - A structured hypothesis list from master data to run parameters to transactions
> - T-codes at each step
> - Fix, test, and prevention (master data checks, reports)
> - Communication with business while resolving

---
## 14. ⭐ Advanced: How to Answer SAP Questions and What to Avoid
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Answer pattern for any SAP question:** (1) one-sentence definition, (2) place in the process, (3) key T-code or table, (4) accounting or stock effect, (5) one practical example with numbers, (6) risk or control, (7) S/4HANA note.

**Common mistakes:**
- Reciting T-codes without explaining the document or posting that results.
- Confusing PR with PO, TR with TO, notification with order, planned order with production order.
- Quoting ECC-only tables (`MSEG`, `VBUK`, `KONV`, `BSEG` as the single source) without noting S/4HANA changes.
- Saying a configuration "is in SPRO" without a path or example; give `OBYC`, `OVKK`-type names only if sure.
- Claiming hands-on experience you do not have. Interviewers test a depth question next. Say "I know the process and used these reports; I have not configured it."
- Ignoring India context: GST, TDS, e-invoice, HSN, e-way bill, MSME payment terms.

**When you do not remember a T-code:** name the object and the menu path (Logistics > Materials Management > Purchasing > Purchase Order > Create), then say what you would verify.

**How to practise:** pick one end-to-end flow, draw it with documents and postings, and speak it in 90 seconds; then take two variants (a return, a block). Pair with [[143 SCM Interview Question Bank]] and [[158 Operations Management Interview Question Bank & Numericals]].

### Example
Q: "What is a GR/IR account?" Weak answer: "A clearing account." Strong: "It is a clearing account that sits between goods receipt and invoice. At GR, inventory is debited and GR/IR credited; at invoice verification GR/IR is debited and the vendor credited. A balance on GR/IR means goods received not yet invoiced, so I would review it monthly with `MR11` and `MB5S` to find stale items." (`MB5S` is the GR/IR balance report.)

### In the news
See news box. As cloud ERP adoption grows, interviewers increasingly ask how an SAP consultant works within standard and clean-core limits, so keep one example of a process you would not customise.

### Interview angle
> [!question] How it is asked
> "You said you know SAP MM. What is the last problem you solved and how?"

> [!tip] Strong answer includes
> - A real or simulated project episode with symptom, cause and fix
> - T-codes and tables used and what you learned
> - Control and compliance angle
> - Honest scope of your experience

Related: [[201 SAP Landscape, Transports, Security & GRC Basics]] and [[085 SAP Reporting & Analytics]].
