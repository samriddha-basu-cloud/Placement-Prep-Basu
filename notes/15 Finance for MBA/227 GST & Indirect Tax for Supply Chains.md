---
tags: [finance-for-mba, tier1]
area: Finance for MBA
topic: "GST & Indirect Tax for Supply Chains"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# GST & Indirect Tax for Supply Chains

⬅ [[226 Corporate Finance Essentials - Capital Structure & Cost of Capital]] · [[_Index - Finance for MBA|Finance for MBA]]

> **Area:** Finance for MBA · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. GST Architecture: CGST, SGST, IGST and Scope]]
2. [[#2. Rate Structure After GST 2.0 and HSN Classification]]
3. [[#3. Supply, Time of Supply and Value of Supply]]
4. [[#4. Place of Supply and Inter-State vs Intra-State]]
5. [[#5. Input Tax Credit: Conditions, Time Limits and Utilisation]]
6. [[#6. Blocked Credits (Section 17(5)) and Apportionment]]
7. [[#7. Reverse Charge Mechanism (RCM)]]
8. [[#8. E-Invoicing and E-Way Bill]]
9. [[#9. Stock Transfers and Branch Transfers]]
10. [[#10. Landed Cost: How GST Enters the Cost of a Purchase]]
11. [[#11. GST and Warehouse Network Design]]
12. [[#12. Customs Duty Interplay: Imports, Exports and IGST]]
13. [[#13. Anti-Profiteering, Transitions and Compliance KPIs]]
14. [[#14. ⭐ Advanced: Inverted Duty Structures, ITC Lock-Up and Refunds]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): GST 2.0 reset the rate structure; collections keep climbing
> **GST 2.0 took effect on 22 September 2025.** On the 56th GST Council's 3 September 2025 decisions, the four-slab structure (5/12/18/28%) became a **two-rate system of 5% and 18%**, plus a **40% "de-merit" rate** for sin and luxury goods (pan masala, tobacco, aerated drinks, high-end cars, yachts, private aircraft). Cement and small cars/two-wheelers moved from 28% to **18%**; trucks, buses, three-wheelers and auto parts from 28% to 18%; GTA freight stays at **5% without ITC, or 18% with full ITC at the transporter's option**. Registration thresholds for goods were unchanged. ([PIB: GST reforms 2025](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/sep/doc202594628401.pdf); [PIB FAQs on the 56th Council](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2163560&reg=48&lang=2); [EY alert](https://www.ey.com/en_in/technical/alerts-hub/2025/09/gst-council-announces-major-rate-rationalization-and-trade-facilitation-measures))
>
> **Trade-facilitation measures that matter to operations (September 2025).** Risk-based **provisional refunds** were extended to zero-rated exports and to **inverted-duty structures** (reported as a 90% provisional refund), and the **place of supply for intermediary services** shifts from the supplier's to the recipient's location. This second change was later legislated: Finance Act 2026 omitted section 13(8)(b) of the IGST Act with effect from **30 March 2026**, so qualifying intermediary services can be zero-rated exports. ([EY alert](https://www.ey.com/en_in/technical/alerts-hub/2025/09/gst-council-announces-major-rate-rationalization-and-trade-facilitation-measures); [DMI Finance GST tracker](https://www.dmifinance.in/gst/gst-updates-amendments/); [TaxGuru on section 13(8)(b)](https://taxguru.in/goods-and-service-tax/intermediary-conundrum-omission-section-13-8-b-igst-act-finance-act-2026.html))
>
> **Collections after the reform (September 2026).** Gross GST collection was **₹2,03,521 crore** (+14.7% on ₹1,77,365 crore a year earlier); net revenue **₹1.77 lakh crore** (+18.1%); import-linked GST **₹65,525 crore** (+25.9%) against domestic GST of **₹1.38 lakh crore** (+10.1%); April-September 2026 gross collections were **₹12.46 lakh crore** (+11.6%). The source offers no commentary on how much of the growth is due to the rate cuts. ([The Indian Eye](https://theindianeye.com/2026/10/02/gst-collections-rise-14-7-to-%E2%82%B92-04-lakh-crore-in-september/))
>
> **Anti-profiteering after the cut (2025).** The National Anti-Profiteering Authority had a sunset of 31 March 2025; cases now sit with the GST Appellate Tribunal. Even so, section 171 still requires rate-cut benefits to be passed on, the Consumer Affairs ministry allowed revised MRP stickers on unsold stock until 31 December 2025, and finance ministry instructions asked tax commissioners for monthly price-change reports after 22 September 2025. ([TaxGuru](https://taxguru.in/goods-and-service-tax/anti-profiteering-gst-2-0-law-practice.html))
>
> Sub-topics that say **"See news box"** reuse these items. Rates, thresholds and dates were checked on 4 October 2026 from the sources above plus standard CGST/IGST provisions; GST law changes frequently through notifications, so confirm against the latest CBIC notification before a live decision. Worked examples are illustrative.

---
## 1. GST Architecture: CGST, SGST, IGST and Scope
> 🔴 Tier 1 · _Key points:_ destination-based; dual GST; intra-state = CGST + SGST; inter-state = IGST; what is outside GST

### Definition
GST (from 1 July 2017) is a **destination-based, multi-stage tax on the supply of goods and services** with credit for tax paid on inputs, so tax falls on value addition and ultimately on the consumer. It is **dual**: the Centre and the State both levy it on the same supply.

| Tax | Applies when | Revenue goes to |
|---|---|---|
| **CGST** + **SGST/UTGST** | Intra-state supply (supplier and place of supply in the same state) | Centre and that State, equal halves |
| **IGST** | Inter-state supply, imports, supplies to SEZ, exports (zero-rated) | Centre; apportioned to the destination state through settlement |
| **Compensation cess** | Wound down for most goods in 2025-26; tobacco-linked goods follow a separate path (check status) | — |

Subsumed taxes: central excise (mostly), service tax, VAT/CST, entry tax, octroi, purchase tax. **Outside GST (as of last check):** petroleum crude, high-speed diesel, motor spirit, natural gas and aviation turbine fuel, alcohol for human consumption and electricity, which still bear VAT/excise, a reason fuel costs remain outside the credit chain in logistics. **Registration:** mandatory above ₹40 lakh turnover for goods suppliers (₹20 lakh services; lower for special-category states and some states), with no change in the goods threshold after GST 2.0. Composition scheme (up to ₹1.5 crore) gives a low flat rate but **no ITC** and no inter-state outward supply. Registration is **state-wise per PAN**: a company storing goods in five states needs five GSTINs. Link: [[009 Logistics & Distribution]], [[001 SCM Introduction & Fundamentals]].

### Example
A Pune plant sells ₹1,00,000 of goods to a dealer in Pune at 18%: CGST ₹9,000 + SGST ₹9,000. The same goods sold to a dealer in Bengaluru carry IGST ₹18,000. The total tax is the same, but the **credit track differs**: credit is held registration-wise (state-wise), CGST and SGST credits cannot be set off against each other, whereas IGST credit can be used against IGST, CGST and SGST.

### In the news
See news box. After GST 2.0 the 5%/18% core rates apply the same way across CGST/SGST/IGST (for example, 18% = 9% + 9% or 18% IGST); the rate cut also changed the tax embedded in every purchase and sale invoice in a supply chain.

### Interview angle
> [!question] How it is asked
> "How does GST differ from the earlier indirect tax regime, and why does it matter for a supply chain?"

> [!tip] Strong answer includes
> - Subsumed many taxes, with seamless credit across goods and services
> - Destination principle: tax goes to the consuming state; inter-state trade is not a cascading cost
> - Removed state border check posts and CST; consolidated warehouse networks
> - Residual gaps: fuel and electricity outside, blocked credits, state-wise registration

---
## 2. Rate Structure After GST 2.0 and HSN Classification
> 🔴 Tier 1 · _Key points:_ 0/5/18/40 slabs from 22 Sep 2025; HSN drives rate; HSN digits by turnover; special rates

### Definition
Since **22 September 2025** the principal rates are **0%** (exempt/nil), **5%** (merit: essentials, many agri and healthcare items, three-wheelers, tractors and farm equipment), **18%** (standard: most goods and services, now including cement, small cars, buses, trucks, air-conditioners, refrigerators, washing machines) and **40%** (sin and luxury goods: pan masala, tobacco, aerated beverages, large cars, motorcycles above 350cc, yachts, private aircraft, betting). Special rates continue for items such as gold and silver (3%) and rough diamonds; check the notification for the HSN. **Examples of consequence for operations:** man-made fibre and yarn dropped to 5% (inverted-duty fix); hotel rooms below ₹7,500 a day at 5% (no ITC); GTA 5% (no ITC) or 18% (ITC).

**Classification:** goods are classified under the **HSN (Harmonized System of Nomenclature)**; services under **SAC**. Rate, ITC, e-invoice and e-way bill all key off the HSN/SAC. Mandatory HSN digits on invoices: **4 digits** up to ₹5 crore annual turnover, **6 digits** above (8 digits for imports/exports). Misclassification means the wrong rate and rate disputes; after the reform the main boundary is 5% vs 18%. Master data discipline matters ([[175 Data Quality, Master Data & Data Governance]]); SAP holds HSN in material master/tax condition records ([[195 SAP SD Advanced - Pricing, Output & Document Flow]], [[190 SAP FI-CO Essentials for Operations Professionals]]).

### Example
A trader holds 10,000 bags of cement bought at ₹300 base + 28% (₹384 gross). After 22 September 2025 new supplies carry 18%: ₹354 at the same base. The unsold stock bought at 28% still has a valid ITC of ₹84 a bag in the ledger; **ITC already credited remains usable** (section 49(4) per the PIB FAQs), but the shelf price must now reflect 18% (see sub-topic 13).

### In the news
See news box. Cement, trucks, auto parts, consumer durables and fibre moved down; sin goods moved to 40%. Network planners should recompute landed costs and customer prices from 22 September 2025 invoices onward.

### Interview angle
> [!question] How it is asked
> "GST rates on cement fell from 28% to 18%. What does that do to a cement company's supply chain?"

> [!tip] Strong answer includes
> - Price to customer falls (or margin rises) depending on pass-through; demand elasticity
> - Input credits remain; transitional stock; invoice and ERP rate master updates
> - Freight (GTA) rate options and ITC chain for logistics
> - Check HSN classification and rate in the master data before go-live

---
## 3. Supply, Time of Supply and Value of Supply
> 🔴 Tier 1 · _Key points:_ taxable event = supply; time of supply sets the tax point; value includes incidentals, excludes pre-supply discounts

### Definition
**Supply** (section 7 CGST) covers sale, transfer, barter, exchange, licence, rental and disposal made for consideration in the course or furtherance of business, plus **deemed supplies** such as supplies between **distinct persons** (Schedule I) and gifts to employees above ₹50,000 in a year. **Time of supply of goods** (the tax point) is the **earliest** of invoice date (or the last date on which the invoice should have been issued, i.e., removal of goods or delivery), and date of receiving payment. For services, where the invoice is issued within the prescribed period (30 days), it is the earlier of invoice date and payment; otherwise the earlier of completion of service and payment.

**Value of supply** (section 15) is the **transaction value** if the parties are unrelated and price is the sole consideration. It includes incidental charges (packing, commission, freight charged by the supplier), taxes other than GST, subsidies linked to price and interest or late fee on delayed payment; it excludes **discounts given before or at the time of supply** shown on the invoice (and post-supply discounts only if agreed in advance and the recipient reverses the related ITC).
$$GST=\text{Taxable value}\times\text{Rate},\qquad \text{Taxable value}=\frac{\text{Gross price}}{1+\text{Rate}}\ \text{(for tax-inclusive MRP)}$$

### Example
List price ₹10,00,000; trade discount 5% on invoice (₹50,000); packing charged ₹20,000; freight charged and arranged by supplier ₹30,000 (incidental, part of the composite supply). Taxable value = 10,00,000 − 50,000 + 20,000 + 30,000 = **₹10,00,000**; GST at 18% = **₹1,80,000**; invoice total ₹11,80,000. An MRP of ₹1,180 (tax-inclusive, 18%) gives taxable value 1,180/1.18 = ₹1,000.

### In the news
See news box. After the rate cut, tax-inclusive MRPs fall by the change in rate, which is why the ministry allowed revised MRP declarations on old stock to 31 December 2025.

### Interview angle
> [!question] How it is asked
> "A supplier gives a year-end volume rebate. How is GST treated?"

> [!tip] Strong answer includes
> - Pre-agreed discounts linked to invoices reduce taxable value; others do not unless conditions are met
> - Credit note and ITC reversal by the recipient
> - Time of supply and tax point; value includes freight arranged by supplier
> - Show control: contract terms must describe the rebate at inception

---
## 4. Place of Supply and Inter-State vs Intra-State
> 🔴 Tier 1 · _Key points:_ goods: where movement ends; bill-to-ship-to; services: recipient location (B2B); IGST vs CGST+SGST decision

### Definition
Whether tax is **IGST or CGST + SGST** depends on the **location of supplier** and the **place of supply (POS)** (IGST Act sections 10-13). Different states = inter-state = IGST.
- **Goods with movement (s.10):** POS is where movement ends (delivery state). **Bill-to-ship-to:** if goods are delivered on the buyer's direction to a third party, POS is the **principal buyer's (bill-to) state**.
- **Goods without movement:** where delivered; **imports:** IGST under the Customs Tariff Act; exports and SEZ supplies are **zero-rated**.
- **Services (s.12, domestic):** general rule B2B = **recipient's location**; B2C = recipient's address on record, otherwise supplier's location. Specific rules: immovable property → location of the property; transport of goods B2B → recipient's location; B2C → where goods are handed over.
- **Cross-border services (s.13):** generally recipient's location; **intermediary services** were deemed supplier-located until section 13(8)(b) was omitted from 30 March 2026.
Zero-rated supplies (exports, SEZ) can be made under a Letter of Undertaking (LUT) without paying IGST and then refund of accumulated ITC claimed, or with IGST paid and refund claimed.

### Example
Bill-to ship-to: a Mumbai distributor (bill-to) buys from a Gujarat plant and directs delivery to its customer in Hyderabad. The POS of the first supply is **Maharashtra** (the bill-to buyer's state), so the Gujarat plant charges **IGST** (Gujarat to Maharashtra is inter-state). The distributor's onward sale to its customer, with Maharashtra as supplier location and Telangana as delivery, is also **IGST**. Without the bill-to-ship-to rule, the first sale would be misread as Gujarat to Telangana.

### In the news
See news box. The POS change for intermediary services makes Indian agents and sourcing offices serving foreign principals potentially export services, which refunds ITC instead of adding 18% tax.

### Interview angle
> [!question] How it is asked
> "A buyer in Delhi asks you to ship to its warehouse in Jaipur. Which GST applies?"

> [!tip] Strong answer includes
> - Under bill-to-ship-to the POS is the bill-to buyer's state (Delhi), not the delivery state (Rajasthan)
> - So a Delhi supplier charges CGST + SGST, while a supplier in another state charges IGST; the Jaipur delivery then needs the buyer's own onward invoice if it resells
> - Registration implications for holding stock in a new state
> - Exports and SEZ as zero-rated with LUT

---
## 5. Input Tax Credit: Conditions, Time Limits and Utilisation
> 🔴 Tier 1 · _Key points:_ s.16 conditions; GSTR-2B matching; 180-day payment rule; credit utilisation order

### Definition
**ITC** lets a registered person set off GST paid on inputs, input services and capital goods against output GST. Conditions (section 16):
1. Holding a valid **tax invoice** (or debit note).
2. **Receipt** of goods/services.
3. Supplier has actually **paid the tax** and the invoice appears in the recipient's **GSTR-2B** (auto-drafted statement).
4. Recipient has filed **GSTR-3B**.
5. Claimed by **30 November following the financial year** (or annual-return date, whichever is earlier).
6. Payment to the supplier within **180 days** of the invoice, or ITC is reversed with interest (re-claimable on payment).
**Utilisation order (Rule 88A):** IGST credit is used first for IGST, then CGST and SGST (in any order or proportion); CGST credit for CGST, then IGST; SGST credit for SGST, then IGST. **CGST and SGST credits cannot be set off against each other.** ITC cannot be used to pay **reverse-charge** tax (paid in cash first, then claimed as ITC) or interest/penalty. Since the 2025 portal changes, GSTR-3B has hard validations on negative ledger balances and excess ITC reclaim (introduced in December 2025 per a compliance tracker).

### Example (monthly return, ₹)
A Nashik manufacturer buys raw material ₹10,00,000 from Gujarat (IGST 18% = 1,80,000) and GTA freight ₹50,000 (RCM at 5% = IGST 2,500, claimable after cash payment). It sells ₹14,00,000 within Maharashtra (CGST 1,26,000 + SGST 1,26,000) and ₹6,00,000 to Karnataka (IGST 1,08,000).
- **ITC available:** IGST 1,80,000 on the supplier invoice, plus 2,500 on the freight once the RCM tax is paid in cash.
- **Output tax:** CGST 1,26,000; SGST 1,26,000; IGST 1,08,000 (total 3,60,000).
- Apply IGST credit: 1,08,000 against IGST; remaining 74,500 against CGST → CGST payable in cash 51,500; SGST payable in cash 1,26,000.
- Net payable on outward supplies = 3,60,000 − 1,82,500 = **₹1,77,500** in cash, plus the ₹2,500 RCM cash paid earlier, so total cash for the month is **₹1,80,000** (check: 3,60,000 − 1,80,000 of supplier-invoice ITC).
If the supplier's invoice is missing from GSTR-2B, the ₹1,80,000 credit is not claimable that month and the cash outflow jumps by that amount.

### In the news
See news box. In September 2026 the Centre reported refunds of ₹27,001 crore against gross collection ₹2.04 lakh crore; the claim discipline in GSTR-2B and returns filing determines how much of the tax paid is recovered as credit instead of cost.

### Interview angle
> [!question] How it is asked
> "Your supplier does not file returns. What is the impact and what do you do?"

> [!tip] Strong answer includes
> - ITC at risk if the invoice is not in GSTR-2B; recipient bears the loss
> - Vendor compliance scoring, payment holds (hold the tax portion until the invoice appears), contract indemnity
> - The 180-day payment rule and the reversal with interest
> - Reconcile books vs GSTR-2B monthly before filing

---
## 6. Blocked Credits (Section 17(5)) and Apportionment
> 🔴 Tier 1 · _Key points:_ vehicles, food, club, works contract for immovable property; exempt-supply apportionment

### Definition
Section 17(5) **blocks** ITC on specified items, so the GST paid becomes **part of the cost**. Main blocks:
- **Motor vehicles** for carrying up to 13 persons (and related insurance, repair, fuel), except when used for resale, passenger transport, driver training or goods transport (trucks are eligible).
- **Food and beverages, outdoor catering**, beauty treatment, health services, club and fitness memberships, and life/health insurance, unless the supply is mandated by law or forms part of an outward supply of the same category.
- **Works contract and construction of immovable property** (other than plant and machinery) for own account, with the 2025-26 Budget amendment replacing "plant or machinery" with "plant and machinery" in 17(5)(d) to align the wording.
- **Goods lost, stolen, destroyed, written off or gifted** (free samples); personal consumption; tax demanded or paid on fraud, detention or confiscation cases (sections 74, 129, 130).
**Apportionment (Rules 42-43):** where inputs serve both taxable and exempt supplies, ITC is limited to the proportion attributable to taxable (and zero-rated) supplies:
$$\text{Eligible ITC}=\text{Common ITC}\times\frac{\text{Taxable + zero-rated turnover}}{\text{Total turnover}}$$
Reversals appear in **GSTR-3B Table 4(B)**; wrongly availed credit attracts interest at **24% a year** from the claim date to the reversal date.

### Example
A distribution company buys an ₹8,00,000 sedan for senior managers (GST 18% = ₹1,44,000, blocked): the asset cost is **₹9,44,000**. A ₹8,00,000 delivery truck is ITC-eligible: cost **₹8,00,000**. A warehouse building constructed by contractors (works contract) with ₹50 lakh of GST is blocked, whereas the racking inside (plant and machinery) may be eligible, so **classification of capex as building vs plant** has a direct tax consequence ([[127 Warehouse Engineering - Racking, Sizing & Material Handling]]).
Mixed use: common ITC ₹10 lakh; taxable turnover ₹90 crore; exempt turnover ₹10 crore: eligible = 10 × 90/100 = ₹9 lakh; ₹1 lakh is reversed.

### In the news
See news box. Vehicles now sit at 18% (small cars) or 40% (large cars); where credit is blocked, that GST is a real cost of the vehicle.

### Interview angle
> [!question] How it is asked
> "A company wants to build a warehouse. How does GST affect the decision to build, lease or rent?"

> [!tip] Strong answer includes
> - ITC blocked on construction of immovable property; renting generally allows ITC on rent (18% tax) to a registered lessee who makes taxable supplies
> - Plant and machinery vs building classification of racking, conveyors, mezzanines
> - Effect on total cost of ownership and lease-vs-buy ([[224 Capital Budgeting for Operations - Capex, Lease vs Buy & Replacement]])
> - Mixed-use apportionment

---
## 7. Reverse Charge Mechanism (RCM)
> 🔴 Tier 1 · _Key points:_ recipient pays tax; GTA freight; imports of services; cash payment then ITC

### Definition
Under **reverse charge**, the **recipient** (not the supplier) pays GST on notified supplies (section 9(3)) and on a limited set of supplies from unregistered persons (section 9(4)), and on **import of services** (IGST Act 5(3)). Common supply-chain RCM items:
- **Goods Transport Agency (GTA) services** (road freight, with consignment note) to a registered business, factory, society, partnership or similar: recipient pays **5%**. GTA may instead opt for forward charge at **18% with full ITC** (and charge GST in its invoice).
- **Legal services** from advocates, **sponsorship**, **security services** from non-corporate suppliers, and **import of services** from abroad (for example, software, freight by foreign carrier).
RCM tax is paid **in cash** (not from the credit ledger) in GSTR-3B; the recipient then claims **ITC** in the same or later return if eligible. The recipient self-invoices (and, for unregistered suppliers, issues a payment voucher).

### Example
A GTA issues a ₹20,000 consignment note and charges no GST. The shipper pays **5% RCM = ₹1,000** in cash and claims ₹1,000 back as ITC; the net cost is ₹20,000. If the GTA instead opts for 18% with ITC, the invoice is ₹20,000 + ₹3,600 = ₹23,600, again recoverable by a registered shipper. A GTA at the 5% rate cannot take ITC on its own fuel or vehicle costs, whereas one choosing 18% recovers them and may quote a lower base, so compare quotes on a **net-of-ITC** basis.

### In the news
See news box. GTA continues to be the main logistics service with a 5% or 18% option after GST 2.0 and the RCM mechanism remained in place for registered recipients.

### Interview angle
> [!question] How it is asked
> "Why does reverse charge matter in logistics procurement and how should we budget it?"

> [!tip] Strong answer includes
> - GTA RCM 5% vs forward charge 18%, who pays and cash vs credit
> - ITC on RCM is eligible only for taxable supplies and after cash payment
> - Compare transporter quotes net of ITC; make the model consistent across vendors
> - Self-invoicing, GSTR-3B reporting and audit trails

---
## 8. E-Invoicing and E-Way Bill
> 🔴 Tier 1 · _Key points:_ e-invoice for B2B above ₹5 crore AATO; IRN and QR; 30-day reporting for ≥ ₹10 crore; e-way bill above ₹50,000

### Definition
**E-invoicing:** B2B, export and credit/debit-note invoices of registrants with **aggregate annual turnover (AATO) above ₹5 crore (PAN-wise)** must be reported to the **Invoice Registration Portal (IRP)**, which returns an **Invoice Reference Number (IRN)**, digital signature and **QR code**. Exempt classes include banks, financial institutions, insurers, GTAs and passenger transport. For taxpayers with AATO of **₹10 crore or more**, invoices must be reported **within 30 days** of the invoice date or the IRP rejects them (this 30-day limit is reported for AATO of ₹10 crore and above; it is understood to apply from 1 April 2025, a date not confirmed in the sources read). An invoice without an IRN (where mandatory) is not valid for the recipient's ITC.

**E-way bill:** needed for movement of goods of **consignment value above ₹50,000** (inter-state and, with state variations, intra-state). The consignor, consignee or transporter generates it (Part A: invoice details, Part B: vehicle). **Validity:** about **one day per 200 km** for regular cargo (longer for over-dimensional cargo). Goods in transit without a valid e-way bill risk **detention and penalty** (200% of tax on taxable goods under section 129, check current rules). Stock transfers and branch transfers also require e-way bills above the value limit.
The e-way bill details integrate with the **transport management system (TMS)** and ERP, so the dispatch process cannot release a truck until the e-invoice (IRN) and e-way bill exist ([[125 Transportation Management Deep Dive]], [[196 SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)]], [[082 SAP SD — Sales & Distribution]]).

### Example
A dispatch of 8 pallets ₹6,40,000 + 18% from Pune to Indore (about 600 km) needs an IRN (if AATO > ₹5 crore) and an e-way bill; validity is about 3 days (600/200). If the truck breaks down after day 3, the transporter must update Part B or extend validity before expiry. A dispatch of ₹40,000 of goods is below the ₹50,000 limit and needs no e-way bill, though the supplier may still generate one voluntarily.

### In the news
See news box. The reforms reaffirmed the digital trail: e-invoice reporting window, provisional refunds and ITC matching all depend on structured invoice data; December 2025 added hard validations in GSTR-3B returns.

### Interview angle
> [!question] How it is asked
> "How would you design the dispatch process so no truck leaves without compliant paperwork?"

> [!tip] Strong answer includes
> - ERP/WMS gate: IRN and e-way bill must exist before gate-out
> - Pre-checks: GSTIN validity, HSN, value, distance and vehicle number
> - Exception handling for breakdowns, transshipment and multi-vehicle loads
> - KPIs: e-way bill expiry incidents, IRN failures, detention cases

---
## 9. Stock Transfers and Branch Transfers
> 🔴 Tier 1 · _Key points:_ distinct persons; Schedule I deemed supply; IGST on inter-state transfer; valuation under Rule 28

### Definition
Under GST, **establishments of the same legal entity in different states are "distinct persons"** (section 25), each registered separately. A transfer of goods between them, **even without consideration, is a taxable supply** (Schedule I) and needs a **tax invoice, IGST and an e-way bill**. The receiving branch claims the IGST as ITC; the tax is therefore usually a **cash-flow timing cost**, not a final cost, provided the receiving state has output tax to absorb the credit. **Valuation (Rule 28 for related/distinct persons):** open market value, else value of goods of like kind and quality, else cost-based (cost plus 10% under Rule 30); where the recipient is eligible for **full ITC**, the value declared on the invoice is deemed the open-market value. Transfers within the **same state and same GSTIN** (between additional places of business) are not supplies; they move on a **delivery challan** with an e-way bill if the value limit is exceeded. **Job work** sends (section 143) are not supplies if inputs return within 1 year (capital goods 3 years). **Services** between a head office and branches (shared HR, IT) are also supplies; **Input Service Distributor (ISD)** mechanism distributes ITC on common services and has been mandatory for cross-state distribution from 1 April 2025 (confirm).

### Example
Pune plant transfers goods with cost ₹10,00,000 to its Delhi DC: IGST at 18% on invoice value ₹10,00,000 = **₹1,80,000** paid by Pune. Delhi sells the stock locally for ₹13,00,000 + CGST/SGST 18% (₹2,34,000). Delhi's net payable = 2,34,000 − 1,80,000 (IGST ITC) = **₹54,000**. The interest cost of the cash tied up in IGST for 45 days at 10% = 1,80,000 × 10% × 45/365 = **₹2,219**. If the cost-plus value of Rule 30 (cost + 10%) applied, the invoice value would be ₹11,00,000 and IGST ₹1,98,000; Delhi would then claim ₹1,98,000, so the extra float is ₹18,000.

### In the news
See news box. The shift of intermediary services to recipient-location and provisional refunds for inverted duty reduce, but do not remove, tax cash-flow friction for multi-state networks.

### Interview angle
> [!question] How it is asked
> "We have a plant in Gujarat and DCs in six states. How do inter-state stock transfers affect cost?"

> [!tip] Strong answer includes
> - Each state is a separate registration; transfers are taxable supplies at IGST
> - Mostly a timing cost: tax paid by sender, ITC to receiver; quantify the float
> - Valuation rules and invoice vs challan distinctions
> - Option: direct-to-customer shipments from plant to reduce IGST float and handling

---
## 10. Landed Cost: How GST Enters the Cost of a Purchase
> 🔴 Tier 1 · _Key points:_ recoverable GST is not cost; blocked or non-claimable GST is cost; compare suppliers on net-of-ITC basis

### Definition
**Landed cost** is the full cost of getting an item into inventory. Under GST:
$$\text{Inventory cost}=\text{Price}+\text{Freight}+\text{Duties}+\text{Handling}+\text{Non-recoverable GST}$$
**Recoverable GST (ITC) is excluded**: it is a receivable from the government. It becomes cost when the buyer cannot claim it: composition-scheme purchasers, blocked items, exempt-supply makers, or when the supplier's invoice does not reach GSTR-2B. Compare quotations on **net-of-ITC** landed cost, not gross price. A supplier under the composition scheme or unregistered supplier gives no ITC (for B2B, a costlier option unless the base price is lower by about the full GST).

### Example (domestic purchase)
1,000 units: goods ₹10,00,000 + IGST ₹1,80,000; GTA freight ₹50,000 (RCM 5% = ₹2,500); warehouse handling ₹1,00,000 + 18% (₹18,000). Total ITC = 1,80,000 + 2,500 + 18,000 = **₹2,00,500**.
- **Inventory cost (eligible ITC)** = 10,00,000 + 50,000 + 1,00,000 = **₹11,50,000 = ₹1,150/unit**.
- **If ITC were blocked** (e.g., the buyer cannot claim): cost = 11,50,000 + 2,00,500 = ₹13,50,500 = **₹1,350.5/unit**, 17.4% higher.
- **Supplier comparison:** a registered supplier at ₹10,00,000 + ₹1,80,000 GST costs ₹10,00,000 net of ITC. A composition-scheme supplier quoting ₹10,50,000 with no GST looks cheaper on the gross invoice (₹10,50,000 vs ₹11,80,000) but is ₹50,000 dearer in real cost, because the buyer gets no credit.

### In the news
See news box. For cement, trucks and fibre the lower rate reduces the cash tied up in tax per purchase, but the landed-cost logic is unchanged.

### Interview angle
> [!question] How it is asked
> "Supplier A quotes ₹100 + 18% GST; Supplier B (composition dealer) quotes ₹108 with no GST. Who do you choose?"

> [!tip] Strong answer includes
> - A: ₹100 net of ITC (GST recovered); B: ₹108 with no credit, so A is cheaper
> - Check supplier compliance and the ITC risk (GSTR-2B)
> - Add freight and handling on a comparable basis
> - Consider working capital: GST is paid up-front and recovered later

---
## 11. GST and Warehouse Network Design
> 🔴 Tier 1 · _Key points:_ removal of tax-driven state warehouses; consolidation vs service level; state-wise registration; stranded ITC and IGST float

### Definition
Before 2017, state VAT, the 2% CST on inter-state sales, entry taxes and check posts rewarded **state-level warehouses**. GST removed most of this tax friction, so networks can be designed on **logistics economics**: inventory pooling, transport cost and service time ([[113 Network Design & Facility Location Modelling]], [[010 Warehouse Management]]). Residual GST factors in the design:
- **State-wise registration:** each state with stock needs a GSTIN, returns and ITC management (compliance cost per node).
- **IGST on stock transfers:** an inter-state transfer is a taxable supply, creating a cash float (sub-topic 9); direct shipping or fewer hops reduces it.
- **Stranded ITC:** CGST/SGST credit cannot cross states. A DC state with heavy local purchases of services but mostly IGST outward supplies can accumulate unused credit.
- **Blocked credit on construction** nudges toward leased or third-party warehouses (see sub-topic 6 above).
- **Transport:** e-way bill validity at 200 km/day affects planning of long hauls.
Inventory pooling follows the **square-root law**: inventory needed varies with $\sqrt{n}$ for $n$ stocking points.

### Example
Total inventory at one national DC ₹40 crore (illustrative). With 4 DCs: 40 × √4 = ₹80 crore; with 8 DCs: 40 × √8 = ₹113.1 crore. At a 20% carrying cost, holding cost is ₹16 crore with 4 DCs and ₹22.6 crore with 8, a saving of **₹6.6 crore a year** from consolidation, before the added outbound freight. Add tax float: if ₹50 crore a month moves by inter-state transfers (IGST ₹9 crore), a 10-day average lock-up at 10% costs 9 × 10% × 10/365 × 12 = **₹0.30 crore a year**; each additional state node also needs registration and returns.

### In the news
See news box. A national tax with a lower 18% base and structured e-invoicing makes consolidated hub-and-spoke networks easier to run; quick-commerce and e-commerce dark-store models still need state registrations ([[129 E-commerce & Quick-Commerce Fulfilment]]).

### Interview angle
> [!question] How it is asked
> "A retailer has 12 state warehouses. Should it consolidate under GST?"

> [!tip] Strong answer includes
> - Tax friction no longer forces state-wise warehouses; model inventory pooling vs freight and service-level trade-offs
> - Quantify GST friction: registration cost, IGST float, stranded ITC
> - Customer promise (delivery time) and perishable or heavy products limit consolidation
> - Phased pilot and a total-cost model

---
## 12. Customs Duty Interplay: Imports, Exports and IGST
> 🔴 Tier 1 · _Key points:_ BCD + SWS + IGST on imports; IGST creditable; zero-rated exports; duty schemes

### Definition
Imports bear **customs duty** (Basic Customs Duty, Social Welfare Surcharge, possibly anti-dumping, safeguard or countervailing duties) and **IGST** on top:
$$IGST=\text{Rate}\times\left(\text{Assessable value}+BCD+SWS+\text{other duties}\right)$$
Assessable value is generally CIF (cost + insurance + freight, plus a loading for landing charges). **SWS** is 10% of BCD where applicable (many lines exempted, check the tariff entry). **IGST paid on import is eligible as ITC** (shown through the Bill of Entry in GSTR-2B), but **BCD and SWS are costs** (unless duty-free via schemes). **Exports are zero-rated:** exported with LUT without IGST, with refund of accumulated ITC, or with IGST paid and refund claimed; separate export incentives (duty drawback, RoDTEP, RoSCTL) may apply. **Duty-saving schemes:** EPCG, Advance Authorisation, SEZ and EOU, plus warehousing/bonded duty deferral ([[126 International Trade Documentation, Customs & Trade Finance]], [[014 Global SCM & Sustainability]], [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]). Customs duty rates are changed by each Budget and by notification; a trade blog summary of Union Budget 2026 reports lower BCD on personal imports from 1 April 2026 and wider duty-free allowances for select inputs ([EximPe](https://eximpe.com/blog/b2b/import-duty-changes-in-budget-2026-complete-guide-for-importers-exporters-travelers)), so check the live tariff.

### Example
Imported components: assessable value ₹10,00,000; BCD 7.5% (illustrative) = ₹75,000; SWS 10% of BCD = ₹7,500; IGST base = ₹10,82,500; IGST 18% = **₹1,94,850**. Add customs-broker charges ₹30,000 (+18% GST ₹5,400) and inland GTA freight ₹40,000 (RCM ₹2,000).
- **Inventory cost** = 10,82,500 + 30,000 + 40,000 = **₹11,52,500** (₹1,152.5 a unit on 1,000 units).
- **ITC** = 1,94,850 + 5,400 + 2,000 = ₹2,02,250; cash outlay at the port = 13,54,750.
- Customs cost is 8.25% of assessable value (82,500/10,00,000); the IGST (₹1,94,850) needs funding for the clearance-to-credit period: at 10% for 30 days ≈ ₹1,602 of finance cost.
If the importer cannot claim ITC (for example, it makes exempt supplies), the cost rises by the full ₹2,02,250.

### In the news
See news box. In September 2026 import-linked GST rose 25.9% to ₹65,525 crore against 10.1% growth in domestic GST, reflecting higher import values and the importance of customs-plus-IGST in total landed cost.

### Interview angle
> [!question] How it is asked
> "Compare the landed cost of importing a component from China with buying domestically."

> [!tip] Strong answer includes
> - Import: CIF + BCD + SWS + clearing + inland; IGST recoverable, BCD not
> - Domestic: price + freight; GST recoverable; supplier compliance risk
> - Working capital: IGST paid at the port, longer lead times and safety stock
> - Duty schemes and trade-agreement rates; FX and supply risk

---
## 13. Anti-Profiteering, Transitions and Compliance KPIs
> 🔴 Tier 1 · _Key points:_ section 171; pass-through of rate cuts; compliance KPI set; interest and penalty exposure

### Definition
**Anti-profiteering (section 171, CGST Act):** any reduction in the GST rate or benefit of ITC must be **passed on to recipients through a commensurate price reduction**. The National Anti-Profiteering Authority (NAA) investigated complaints and could order refund with interest or deposit in the Consumer Welfare Fund; its sunset was 31 March 2025 and its remaining matters now sit with the GST Appellate Tribunal (per the source read), but the legal obligation continues and the government has used price-monitoring instructions after GST 2.0. Benefits are assessed at **SKU level**.

**Compliance KPIs for an operations/finance team:**
| KPI | Why |
|---|---|
| **ITC match rate** (books vs GSTR-2B) | Credit at risk; target above 98% |
| % of vendors compliant on returns | Source of mismatches |
| E-invoice/IRN coverage and rejection rate | Validity of the invoice |
| E-way bill generated before dispatch; expiry incidents | Detention exposure |
| Blocked ITC as % of purchases | Cost leakage |
| ITC lock-up days (balance ÷ monthly ITC × 30) | Working capital |
| Refund cycle time (inverted duty, exports) | Cash recovery |
| Notices, interest and late fee paid | Compliance cost |
**Interest:** **18% a year** on delayed payment of tax; **24%** on undue or excess ITC claimed and utilised.

### Example
Cement bag base price ₹300: at 28% the MRP was ₹384; at 18% it should be ₹354 (a ₹30 cut). If the manufacturer kept the shelf price at ₹384, the implied base becomes 384/1.18 = ₹325.42, an extra ₹25.42 of base price, and the buyer loses ₹30 of benefit. ITC match: books show ₹1,80,000 of eligible supplier-invoice credit but GSTR-2B shows ₹1,70,000, so match = 1,70,000/1,80,000 = **94.4%**, ₹10,000 at risk. If ₹1,00,000 of tax is paid 45 days late: interest = 1,00,000 × 18% × 45/365 = **₹2,219**; wrongly utilised ITC of the same size for 45 days costs 24% = **₹2,959**.

### In the news
See news box. The ministry's instruction to report monthly price changes after 22 September 2025 and the extended MRP relabelling window are anti-profiteering enforcement in practice.

### Interview angle
> [!question] How it is asked
> "What KPIs would you track to be sure the company is GST-compliant and not leaking credit?"

> [!tip] Strong answer includes
> - ITC reconciliation rate, vendor compliance, IRN/e-way bill coverage, blocked-ITC share
> - Controls: master-data HSN/rate checks, vendor onboarding checks, monthly close checklist
> - Financial exposure: interest 18%/24%, penalties, ITC loss
> - Pass-through documentation for rate changes (SKU-level price evidence)

---
## 14. ⭐ Advanced: Inverted Duty Structures, ITC Lock-Up and Refunds
> ⭐ Advanced · _Added beyond the tracker_

### Definition
An **inverted duty structure** arises when the tax on **inputs exceeds the tax on outputs**, so credit accumulates and cannot be fully used. Refunds under section 54(3) are available for accumulated ITC on **inputs** (and, for goods, not input services or capital goods) in inverted-rate cases, subject to the refund formula; exporters under LUT can also claim refunds of accumulated ITC. GST 2.0 targeted known inversions (for example, man-made fibre and yarn to 5%) and extended **risk-based provisional refunds** to inverted-duty claims (reported as 90%). Remaining operational issues: **ITC lock-up** (working capital), **state-wise ledgers**, **blocked credits** and slow refund cycles. Mitigations: restructure sourcing, switch to forward-charge vendors, optimise inventory and purchase timing, apply for provisional refunds, and model **after-tax cost of funds on blocked ITC**. Link: [[136 Supply Chain Finance & Working Capital]], [[012 Supply Chain Analytics & KPIs]].

### Example
A fabric converter buys inputs of ₹200 crore a year at 18% (GST ₹36 crore) and sells output of ₹260 crore at 5% (GST ₹13 crore). Annual excess ITC = **₹23 crore**. If the credit builds evenly and is not refunded until year-end, the average locked balance is about ₹11.5 crore; at a 10% cost of funds the carrying cost is about **₹1.15 crore** a year. After a rate correction (inputs and outputs aligned at 5%), input GST is ₹10 crore and output GST ₹13 crore, so the firm turns into a net cash payer of ₹3 crore a year and the lock-up disappears. Note: the refund formula limits what can actually be reclaimed.

### In the news
See news box. The 2025 reforms fixed several inverted duty chains (textiles, some fertiliser inputs) and enabled faster provisional refunds, which shows how rate design directly affects working capital in manufacturing supply chains.

### Interview angle
> [!question] How it is asked
> "A manufacturer's GST credit keeps piling up although it is profitable. What would you investigate?"

> [!tip] Strong answer includes
> - Input vs output rate gap (inversion), exempt or zero-rated outward share, state-wise imbalance
> - Remedies: refund claim (inverted duty/exports), vendor/product re-mapping, timing of purchases
> - Quantify the lock-up in ₹ and days and the cost of funds
> - Verify ITC eligibility and vendor compliance before claiming refunds
