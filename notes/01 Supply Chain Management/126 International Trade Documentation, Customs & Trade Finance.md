---
tags: [supply-chain-management, tier1]
area: Supply Chain Management
topic: "International Trade Documentation, Customs & Trade Finance"
tier: Tier 1
roles: Operations / Consulting
status: complete
subtopics: 14
---
# International Trade Documentation, Customs & Trade Finance

⬅ [[125 Transportation Management Deep Dive]] · [[_Index - Supply Chain Management|Supply Chain Management]] · [[127 Warehouse Engineering - Racking, Sizing & Material Handling]] ➡

> **Area:** Supply Chain Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Export-Import Process and Registrations in India]]
2. [[#2. Customs Clearance: Shipping Bill and Bill of Entry]]
3. [[#3. HS Classification and the Customs Tariff]]
4. [[#4. Customs Valuation]]
5. [[#5. Duty Stack and Landed Cost]]
6. [[#6. Core Shipping and Trade Documents]]
7. [[#7. Incoterms 2020 in Contracts]]
8. [[#8. Payment Terms and Trade Finance Instruments]]
9. [[#9. FTAs and Rules of Origin]]
10. [[#10. Export Incentives: Drawback, RoDTEP, RoSCTL, EPCG and Advance Authorisation]]
11. [[#11. SEZ, EOU, FTWZ, Bonded Warehouse and AEO]]
12. [[#12. Container Logistics: FCL vs LCL, Demurrage and Detention]]
13. [[#13. Trade Policy: DGFT, Anti-Dumping and Trade Remedies]]
14. [[#14. ⭐ Advanced: Build-vs-Import Landed-Cost Model with Incentives and FX]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): FTAs go live, export incentives wobble, tariff structure simplified
> **India–UK CETA enters into force (15 Jul 2026).** The agreement and its Double Contribution Convention took effect on 15 July 2026, with three implementing notifications issued on 14–15 July. CBIC notified the origin rules on 3 July 2026: a product can qualify if wholly obtained, made only from originating materials, or made from non-originating inputs that meet product-specific rules; the qualifying value content test is 40% of ex-works price (or 45% of FOB) under build-down and 35% under build-up; de minimis tolerance is 7.5% for agri/fishery chapters and 12.5% for most other goods. ([Legal500](https://www.legal500.com/intelligence/india/international-law/india-uk-ceta-enters-into-force-compliance-and-operational-considerations-for-indian-and-uk-businesses), [India Briefing](https://www.india-briefing.com/news/india-uk-ceta-rules-of-origin-explained-45924.html/))
>
> **EU–India FTA concluded (26 Jan 2026).** Negotiations were concluded on 26 January 2026; India agreed to cut car tariffs from 110% to a minimum of 10% in phases and to remove duty on auto parts within 5–10 years, with machinery, chemicals and pharma duties also cut. Legal review, translation and ratification were still pending in the source reviewed, so it is a concluded deal, not yet a working tariff schedule. ([KPMG](https://kpmg.com/us/en/taxnewsflash/news/2026/01/eu-india-conclude-negotiations-fta.html))
>
> **RoDTEP: halved, restored, extended (Feb–Sep 2026).** DGFT Notification 60/2025-26 of 23 Feb 2026 limited RoDTEP rates and value caps to 50% of existing levels (agri and food Chapters 01–24 excluded). Notification 66/2025-26 restored the earlier rates and caps with effect from 23 Mar 2026. On 30 Sep 2026 the scheme was extended to 31 Dec 2026 with rates and caps unchanged. ([TaxGuru – cut](https://taxguru.in/dgft/dgft-cuts-rodtep-rates-50-percent-rationalisation-notification.html), [TaxGuru – restoration](https://taxguru.in/dgft/rodtep-rates-restored-government-withdraws-50-percent-restriction.html), [Fibre2Fashion](https://www.fibre2fashion.com/news/textiles-policy-news/india-extends-rodtep-scheme-till-december-31-rates-unchanged-313906-newsdetails.htm))
>
> **Export Promotion Mission, ₹25,060 crore (approved 12 Nov 2025).** For FY2025-26 to FY2030-31, with *Niryat Protsahan* (trade finance: interest subvention, factoring, collateral support) and *Niryat Disha* (market access, quality compliance, logistics support), replacing the Interest Equalisation Scheme and Market Access Initiative. ([PIB](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=2189381&reg=3&lang=2))
>
> **Tariff simplification.** Budget 2025-26 removed seven more rates for industrial goods, leaving eight rates including zero, and exempted Social Welfare Surcharge on 82 tariff lines that carry a cess ([PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2098364&reg=48&lang=2)). Budget 2026-27 cut the duty on dutiable personal imports from 20% to 10% and raised the duty-free input limit for seafood exporters from 1% to 3% of previous-year FOB ([Tribune](https://www.tribuneindia.com/news/business/budget-2026-customs-duty-rationalised-on-key-items-with-focus-on-domestic-manufacturing-ease-of-living/)).
>
> Sub-topics that say **"See news box"** reuse these items. Rates and scheme dates change often; the above were checked in early Oct 2026.

---
## 1. Export-Import Process and Registrations in India
> 🔴 Tier 1 · _Key points:_ IEC, ICEGATE, CHA, AD code, RCMC

### Definition
Cross-border trade in India runs on a small set of registrations and actors.
- **IEC (Importer-Exporter Code):** a 10-character code issued by **DGFT**, linked to PAN, needed to import or export goods and most services for business. It is lifetime, with an annual update requirement.
- **ICEGATE:** the CBIC e-commerce portal where Bills of Entry and Shipping Bills are filed, duties paid and status tracked. Most ports run on **ICES** (Indian Customs EDI System).
- **CHA/CB (Customs Broker):** licensed by CBIC to file declarations and handle examination and clearance for a fee.
- **AD Code:** authorised dealer bank code registered with customs for the exporter's port, so export proceeds and drawback flow through the right bank.
- **RCMC:** registration-cum-membership certificate from an Export Promotion Council (e.g., EEPC, FIEO, APEDA) needed for scheme benefits.
- Others: freight forwarder or NVOCC, shipping line or airline, terminal or ICD/CFS operator, marine insurer, authorised dealer (AD) bank.

End-to-end flow: contract and Incoterm → payment instrument → production and pre-shipment inspection → booking and stuffing → customs filing and clearance → carriage → documents to bank → arrival, import clearance and delivery → payment realisation and incentive claims.

### Example
A Pune auto-parts maker with ₹4 crore annual exports. Steps: IEC from DGFT, AD code registered at the port, RCMC from EEPC, a CHA appointed for Nhava Sheva (JNPT), and a freight forwarder booking a 20 ft container. Each shipment needs a commercial invoice, packing list, shipping bill and bill of lading; after realisation the bank issues an e-BRC (electronic bank realisation certificate) that supports incentive claims. The same firm importing steel bars files a bill of entry via the CHA, pays duties on ICEGATE and takes out-of-charge from customs.

### In the news
See news box. The Export Promotion Mission routes trade-finance support through DGFT's digital platform, which only works for firms with IEC, AD code and clean ICEGATE records.

### Interview angle
> [!question] How it is asked
> "A first-time exporter in Nashik wants to ship grapes to Europe. Walk me through what they need before the first container leaves."

> [!tip] Strong answer includes
> - IEC, AD code, RCMC/APEDA registration and phyto-sanitary requirements for agri
> - The actor map: CHA, forwarder, line, terminal, bank, insurer
> - The document-and-money flow in sequence, not a loose list
> - A mention of the 3PL/forwarder choice and cold chain (link to [[133 Food, Agri & Perishables Supply Chain - India]])

---
## 2. Customs Clearance: Shipping Bill and Bill of Entry
> 🔴 Tier 1 · _Key points:_ Shipping bill, LEO, bill of entry, out-of-charge

### Definition
**Export (Shipping Bill):** the exporter or CHA files a **Shipping Bill** on ICEGATE (free, dutiable or drawback type). Many bills are processed by EDI without human intervention; goods are presented at the port or examined at the factory, and the officer grants a **Let Export Order (LEO)**, after which containers are loaded under customs supervision and "shipped on board" is recorded. Drawback and incentives are then processed through the system.

**Import (Bill of Entry):** the importer or CHA files a **Bill of Entry (BoE)**, which can be filed before the vessel arrives. Customs assesses duty (self-assessment since 2011, with risk-based verification through the Risk Management System), the importer pays, the cargo may be examined, and customs gives **out-of-charge** so the goods can leave the port or CFS. Where goods are not cleared in time, port/CFS storage and shipping-line charges rise (see sub-topic 12). A **warehousing BoE** allows duty deferral in a bonded warehouse; an **ex-bond BoE** clears goods from it.

| Step | Export | Import |
|---|---|---|
| Declaration | Shipping Bill | Bill of Entry (often before arrival) |
| Duty | Normally nil; incentives claimed | BCD, SWS, IGST, AIDC/cess, ADD as applicable |
| Gate decision | LEO | Out-of-charge |
| Proof of completion | Shipped-on-board, EGM filed by carrier | Duty-paid challan, BoE copy for ITC |

### Example
A BoE for ₹10 lakh of components is picked by the risk engine for examination. Two days of delay at the CFS beyond the free period adds storage plus line detention, easily a five-figure cost. The importer who filed the BoE before vessel arrival and pre-paid duty avoided this. For the consequences of GST on imported goods, see [[227 GST & Indirect Tax for Supply Chains]].

### In the news
See news box. Budget 2026-27 also eased procedures for personal imports and trimmed rates (20% to 10%), part of the long push to cut clearance friction under the National Logistics Policy ([[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]]).

### Interview angle
> [!question] How it is asked
> "Where does a shipment typically lose time between landing at JNPT and reaching your plant?"

> [!tip] Strong answer includes
> - Pre-arrival filing, duty payment, RMS examination, out-of-charge, then CFS/ICD and inland leg
> - Dwell-time KPI and its link to demurrage and detention
> - Mentions ICEGATE, EDI and paperless processing, not manual submission
> - Offers levers: pre-filing, AEO status, bonded warehouse, clean documentation

---
## 3. HS Classification and the Customs Tariff
> 🔴 Tier 1 · _Key points:_ HS code, 8-digit ITC-HS, Chapter, mis-classification

### Definition
The **Harmonised System (HS)** is the WCO's international goods nomenclature: 6 digits are common worldwide (chapter, heading, subheading); India extends it to **8 digits** for the Customs Tariff and ITC-HS (policy). The code decides **duty rate, export-import policy status (free, restricted, prohibited), GST rate (HSN), FTA eligibility, quality-control order coverage and anti-dumping coverage.**

Classification follows the **General Rules of Interpretation (GRI 1-6)**: classify by the heading terms and section/chapter notes first; then for mixtures, sets and incomplete or unassembled goods, apply the rules in order; finally the most specific description wins.

Why classification errors are costly: wrong code can mean short-paid duty, penalty and interest, loss of FTA benefit, a held consignment, and a mismatch with the GST return. Importers use a **classification ruling** (advance ruling or a past assessed order) for repeat items.

### Example
A smart watch with a built-in phone function and a plain fitness band may sit under different headings; the BCD may differ by several percentage points. If a 10-lakh consignment is declared at a code with 10% BCD but customs reclassifies it to a heading carrying 20%, the demand is the difference on assessable value: ₹10,00,000 x 10% = ₹1,00,000 extra BCD, plus SWS on it, IGST on the higher base, interest and a possible penalty.

### In the news
See news box. With Budget 2025-26 reducing the industrial slabs to eight, the stakes of a code are lower in rate-spread terms but remain high for FTA claims and QCO/anti-dumping coverage.

### Interview angle
> [!question] How it is asked
> "Why does an HS code matter to a supply chain manager? Give a case where a mis-classification hurt."

> [!tip] Strong answer includes
> - Lists everything the code drives: duty, policy, GST, FTA, trade remedies
> - Mentions product master data discipline (link to [[175 Data Quality, Master Data & Data Governance]])
> - Mentions GRI, advance ruling, and a documented classification file
> - Cites the cost: penalty, interest, detention, lost preference

---
## 4. Customs Valuation
> 🔴 Tier 1 · _Key points:_ Transaction value, CIF, adjustments, related parties

### Definition
Valuation follows Section 14 of the Customs Act and the **Customs Valuation (Determination of Value of Imported Goods) Rules, 2007**, aligned with the WTO valuation agreement. The primary method is **transaction value**: the price actually paid or payable for the goods when sold for export to India, adjusted by additions:
- cost of transport, loading, handling and **insurance** up to the place of importation (assessable value is effectively **CIF**; where not ascertainable, rules specify defaults, e.g. insurance 1.125% of FOB, air freight capped at 20% of FOB);
- **landing charges** at 1% of CIF (Rule 10(2));
- selling commission, royalties and licence fees related to the goods and payable as a condition of sale, packing, and **assists** (materials, tooling, design supplied free by the buyer);
- **excluded:** buying commission, post-importation costs, and duties payable in India.

If transaction value is rejected (relationship influenced price, doubts on declared value), valuation falls back in sequence: identical goods, similar goods, deductive, computed, then the residual method. The **exchange rate** used is the one notified by CBIC (fortnightly, separate rates for import and export) under Section 14.

$$AV = \text{FOB} + \text{freight} + \text{insurance} + \text{landing (1\% of CIF)} + \text{royalty/assists/selling commission} + \text{packing}$$

### Example
Invoice price ₹1,00,000; buyer pays a royalty of ₹5,000 as a condition of sale; selling commission ₹3,000; buyer supplies a die worth ₹4,000 (assist); packing ₹1,500; buying commission ₹2,000 (excluded). Transaction value = 1,00,000 + 5,000 + 3,000 + 4,000 + 1,500 = **₹1,13,500**; the ₹2,000 buying commission is not added. Freight, insurance and landing charges then go on top for AV.

### In the news
See news box. Higher-duty goods such as passenger vehicles (110% in the EU-India deal context) show why valuation and classification disputes concentrate where duty rates are steep.

### Interview angle
> [!question] How it is asked
> "A supplier invoices you at $100 but wires $80 in a separate side arrangement. What is customs value and what is the risk?"

> [!tip] Strong answer includes
> - Transaction value is price actually paid or payable, so undervaluation is an offence
> - Additions and exclusions with at least three examples (royalty, assists, buying commission)
> - Related-party pricing and transfer-pricing consistency
> - Fallback valuation methods and the notified exchange rate

---
## 5. Duty Stack and Landed Cost
> 🔴 Tier 1 · _Key points:_ BCD, SWS, IGST, AIDC, ADD, landed cost

### Definition
Import duty in India is cumulative, in this order:
1. **BCD** on assessable value.
2. **SWS** (Social Welfare Surcharge) = 10% of BCD; Budget 2025-26 exempted it on 82 tariff lines that carry a cess, and no more than one cess or surcharge applies per line.
3. **IGST** on (AV + BCD + SWS), usually 5/12/18/28%; the rate set was reformed in 2025, so confirm the current rate ([[227 GST & Indirect Tax for Supply Chains]]). IGST paid on imports for business use is generally creditable as ITC.
4. **Other levies:** AIDC on some items, compensation cess on a few, anti-dumping/safeguard/CVD where notified.

$$\text{Duty} = BCD + SWS + IGST,\quad BCD = r\cdot AV,\; SWS = 0.1\cdot BCD,\; IGST = g\,(AV+BCD+SWS)$$

True **landed cost** = AV + BCD + SWS + (non-creditable taxes) + CHA, port, CFS, inland freight, insurance and handling + finance cost of inventory in transit. Creditable IGST is a working-capital cost, not a product cost.

### Example
FOB USD 10,000, freight USD 1,200, insurance 1.125% of FOB (USD 112.50), so CIF = USD 11,312.50. At ₹88/USD (assumed) CIF = ₹9,95,500. Landing charge 1% = ₹9,955, so AV = **₹10,05,455**. BCD 7.5% (illustrative rate) = ₹75,409; SWS = ₹7,541; IGST base = ₹10,88,405; IGST at 18% = ₹1,95,913. Total duty = ₹2,78,863; cash needed at clearance = ₹12,84,318. Because the IGST is creditable, the product cost excluding IGST = 10,05,455 + 75,409 + 7,541 = ₹10,88,405. Add inland freight ₹45,000, CHA ₹12,000 and port/CFS ₹30,000 = **₹11,75,405**; for 500 units this is about **₹2,351 per unit**. If a FTA brought BCD to nil (below), the saving is ₹75,409 + ₹7,541 = **₹82,950** (about 7.1% of the non-IGST cost).

```python
fx, fob, fr = 88.0, 10000, 1200
cif = (fob + fr + 0.01125*fob) * fx
av = cif * 1.01
bcd = 0.075*av; sws = 0.1*bcd
igst = 0.18*(av + bcd + sws)
print(round(av), round(bcd), round(sws), round(igst))  # 1005455 75409 7541 195913
```

### In the news
See news box. The trimming to eight industrial tariff rates and SWS exemptions on cess-bearing lines changed the arithmetic of the duty stack; always recompute with the live tariff for the HS code.

### Interview angle
> [!question] How it is asked
> "Should we import this component from Vietnam or source locally? Walk me through a landed-cost comparison."

> [!tip] Strong answer includes
> - Full stack including SWS on BCD and IGST on the cascaded base
> - Distinguishes creditable IGST (cash-flow) from true cost
> - Adds lead-time inventory, safety stock and FX hedging cost, not just unit price
> - Tests the result against FTA preference and drawback/duty exemption schemes
> - Links to total cost of ownership ([[002 Procurement & Strategic Sourcing]], [[110 Cost Accounting for Operations]])

---
## 6. Core Shipping and Trade Documents
> 🔴 Tier 1 · _Key points:_ Commercial invoice, packing list, B/L, AWB, certificate of origin

### Definition
| Document | Issued by | Purpose |
|---|---|---|
| **Commercial invoice** | Seller | Value, terms, goods; basis of customs value and payment |
| **Packing list** | Seller | Packages, weights, dimensions; used for stuffing and examination |
| **Bill of Lading (B/L)** | Shipping line/NVOCC | Receipt for goods, contract of carriage, and **document of title** if negotiable ("to order") |
| **Sea waybill** | Carrier | Receipt and contract, not a title document; faster release, no original needed |
| **Airway Bill (AWB)** | Airline/forwarder | Receipt and contract, **non-negotiable** |
| **Certificate of origin (CoO)** | Chamber/EPC or self-declaration | Nationality of goods; preferential CoO supports FTA duty cut |
| **Insurance certificate** | Insurer | Needed under CIF/CIP and often under LC |
| **Inspection, phyto, health certificates** | Agencies | Regulatory approval to ship or import |

B/L types: **Master B/L** (line to forwarder) vs **House B/L** (forwarder to shipper); **clean** (no adverse remarks on goods) vs **claused**; **shipped on board** vs received for shipment; **straight** (named consignee) vs **order** (negotiable); **telex release / sea waybill** for original-free delivery. A bank under an LC needs documents that **comply strictly** with the credit terms.

### Example
An LC calls for a "clean shipped-on-board B/L, invoice of USD 98,000, CoO" but the invoice shows USD 98,500. The bank can refuse the documents as discrepant, and the buyer may use that leverage to renegotiate price or delay payment. A transposed letter in the consignee name causes the same problem, which is why exporters run a document checklist before presenting.

### In the news
See news box. Under the India-UK CETA the importer must hold valid origin proof and carries the burden of proof, so the CoO file is a risk document, not paperwork.

### Interview angle
> [!question] How it is asked
> "What is the difference between a bill of lading and an airway bill, and why does it matter for payment terms?"

> [!tip] Strong answer includes
> - B/L as title document, AWB non-negotiable
> - Why banks prefer B/L-backed credit and how that affects financing
> - Document discrepancies and fixing them early
> - E-B/L and digitisation as a trend (relevant to [[016 Digital Supply Chain & Industry 4.0]])

---
## 7. Incoterms 2020 in Contracts
> 🔴 Tier 1 · _Key points:_ Risk transfer, cost split, named place, EXW to DDP

### Definition
**Incoterms 2020** (ICC) are 11 standard terms that fix **where risk passes, who pays carriage, insurance and export/import clearance**. They do not transfer title, define payment or govern dispute remedies, and the contract should name the place and the Incoterms edition.

- **Any mode:** EXW, FCA, CPT, CIP, DAP, DPU (renamed from DAT, can be any place), DDP.
- **Sea and inland waterway only:** FAS, FOB, CFR, CIF.
- Risk passes: at seller's premises for EXW; on loading on the vessel for FOB; at the named destination for DAP/DPU/DDP.
- **Insurance:** CIF needs minimum cover (Institute Cargo Clauses C); **CIP needs Clauses (A)**, a notable change from 2010.
- **FCA** allows the buyer to instruct the carrier to issue an on-board B/L to the seller, solving an old FOB-in-container problem.
- Containerised cargo is usually handed to the line at a terminal or ICD, not "over the rail", so ICC recommends FCA/CPT/CIP rather than FOB/CFR/CIF for containers.

### Example
An Indian exporter quotes USD 10,000 FOB Mundra and the Dubai buyer asks for CIF Jebel Ali. Freight USD 700 and insurance 0.3% of CIF: CIF = (10,000 + 700) / (1 − 0.003 x 1.1), with insurance on 110% of CIF value, which gives about USD 10,735. The quote rose 7.4%, but the seller carries cost and the contract of carriage while risk still passes at loading, so the buyer still bears loss in transit. Insurance should therefore cover the buyer's interest, and a claims route must be agreed.

### In the news
See news box. FTA duty cuts apply on customs value, and CIF-based valuation means the Incoterm chosen alters dutiable value; shifting freight to the buyer on FOB terms can still leave freight added at import.

### Interview angle
> [!question] How it is asked
> "Why would an Indian exporter prefer FCA over FOB for containers, and when does selling DDP backfire?"

> [!tip] Strong answer includes
> - The risk/cost transfer point and who controls the freight and insurance
> - FCA over FOB for containers; CIP vs CIF insurance level
> - DDP risks: unlimited import duty, VAT/GST exposure, destination clearance control
> - Freight leverage: exporters selling CIF capture freight margin, importers choosing FOB can negotiate better rates ([[125 Transportation Management Deep Dive]])

---
## 8. Payment Terms and Trade Finance Instruments
> 🔴 Tier 1 · _Key points:_ LC (UCP 600), documentary collection, advance, open account

### Definition
Ordering by seller risk, from safest to riskiest for the seller:

| Term | How it works | Seller risk | Buyer risk |
|---|---|---|---|
| **Advance payment** | Buyer pays before shipment | None | High |
| **Confirmed LC** | Issuing bank promises payment against compliant documents, a second bank confirms | Very low | Moderate (documents, not goods, are checked) |
| **Unconfirmed LC** | Issuing bank promises | Low, bank/country risk | Moderate |
| **Documentary collection (D/P, D/A)** | Banks hand documents against payment (D/P) or acceptance of a draft (D/A) under **URC 522** | Moderate to high | Low |
| **Open account** | Shipment first, pay later | High | Low |

**Letter of Credit (LC)** under **UCP 600**: a bank's irrevocable undertaking to pay if compliant documents are presented. Practical rules: documents to be presented within **21 calendar days** after shipment but within validity; banks have a maximum of **5 banking days** to examine. LC variants: sight vs usance, **confirmed**, transferable, back-to-back, red clause (advance), **standby LC** (ISP98, guarantee-like). Financing tools: packing credit (pre-shipment) and post-shipment finance in rupee or foreign currency, **bill discounting**, **export factoring and forfaiting**, and credit insurance (ECGC in India). Trade finance rate support is now channelled through *Niryat Protsahan* under the Export Promotion Mission.

### Example
A ₹50 lakh export is offered on 90-day usance terms. If the exporter's cost of funds is 9% p.a., financing the 90 days costs 5,000,000 x 9% x 90/360 = **₹1,12,500** (2.25% of invoice value). That is the price the seller should embed in a 90-day open-account quote, plus the cost of ECGC credit-insurance cover. Compare: an LC with confirmation might add 0.5-1.5% in fees but removes buyer-bank risk.

### In the news
See news box. The ₹25,060 crore Export Promotion Mission explicitly targets affordable trade finance for MSMEs (interest subvention, export factoring, collateral cover). See also [[136 Supply Chain Finance & Working Capital]].

### Interview angle
> [!question] How it is asked
> "A new Bangladeshi buyer wants 90-day open account on a ₹2 crore order. What would you do?"

> [!tip] Strong answer includes
> - Risk ladder with the instruments named correctly
> - Cost of financing the credit period priced into the quote
> - Mitigants: credit insurance (ECGC), confirmed LC, partial advance, factoring
> - Note that an LC finances documents, so shipping errors can void payment

---
## 9. FTAs and Rules of Origin
> 🔴 Tier 1 · _Key points:_ Preferential duty, origin criteria, regional value content, CoO

### Definition
A **Free Trade Agreement (FTA)** or **CEPA/CETA** cuts or removes duty between partners on negotiated tariff lines. To claim the benefit goods must satisfy **Rules of Origin (RoO)**, which stop third-country goods from entering via a partner.

Common origin criteria:
- **Wholly obtained** (grown, mined, born, caught);
- **Change in tariff classification (CTC):** inputs change heading, subheading or chapter;
- **Regional/qualifying value content (RVC/QVC):** minimum local content percentage;
- **Specific process rule** (typical in chemicals, textiles);
- **Cumulation** (counting inputs from partner countries as local) and **de minimis** tolerance for small non-originating content.

$$RVC_{\text{build-down}} = \frac{\text{FOB} - \text{VNM}}{\text{FOB}}\times 100$$

where VNM is the value of non-originating materials.

Operationally the exporter secures a preferential CoO or an origin declaration, the importer claims preference on the Bill of Entry, and customs can verify and recover duty if origin fails. India's FTA network includes ASEAN, Japan, Korea, UAE (CEPA), Australia (ECTA), the UK (CETA) and more under negotiation.

### Example
An Indian electronics assembler exports a product valued FOB ₹10,00,000 to the UK. Imported (non-originating) components are ₹5,50,000. Build-down RVC = (10,00,000 − 5,50,000)/10,00,000 = **45%**. Against a 45%-of-FOB build-down threshold in the UK deal (as reported), it just qualifies; a ₹10,000 input price rise to ₹5,60,000 gives 44% and fails, losing the duty-free entry. Hence exporters track input origin and pricing continuously.

### In the news
See news box. The CETA took effect on 15 Jul 2026 with 40%/45% build-down and 35% build-up thresholds and 7.5%/12.5% de minimis tolerances; the EU deal (concluded 26 Jan 2026) would add a larger market once ratified. Link to [[014 Global SCM & Sustainability]] for China+1 and trade risk.

### Interview angle
> [!question] How it is asked
> "India has signed an FTA with the UK. How should a textile exporter decide whether to restructure its sourcing?"

> [!tip] Strong answer includes
> - The origin test and which input sourcing breaks it
> - Duty saved vs compliance cost, with a quantified example
> - Preference utilisation (many firms leave FTA benefit unclaimed)
> - Competitors' positions and rival countries' FTAs

---
## 10. Export Incentives: Drawback, RoDTEP, RoSCTL, EPCG and Advance Authorisation
> 🔴 Tier 1 · _Key points:_ Zero-rating, duty remission, EO, input duty exemption

### Definition
Exports should leave India without embedded taxes. Schemes:
- **Duty drawback (AIR / brand rate):** refund of customs/central excise duties on inputs used in exports; the **All Industry Rate** is notified as a percentage of FOB, with value caps. Drawback is not for IGST/GST refunded separately.
- **RoDTEP:** remission of embedded central/state levies not otherwise refunded (e.g., fuel, electricity duty, mandi tax), paid as a **% of FOB**, with caps, via transferable duty credit/refund. **RoSCTL** does the same for apparel, made-ups and some textiles.
- **GST on exports:** zero-rated; exporters claim a **refund of IGST** paid on exports or of unutilised ITC (details in [[227 GST & Indirect Tax for Supply Chains]]).
- **Advance Authorisation (AA):** duty-free import of inputs physically incorporated in an export product (with SION norms), usually for exports with a minimum **value addition** and an export obligation period.
- **EPCG (Export Promotion Capital Goods):** import capital goods at reduced/zero duty against an **export obligation of 6 times the duty, taxes and cess saved**, to be fulfilled in **6 years** from authorisation; domestically sourced capital goods carry an obligation 25% lower; meeting 75% of specific plus 100% of average EO in half the time can trigger early redemption (FTP 2023, Chapter 5).
- **Export promotion mission** support for finance and market access.

### Example
FOB ₹10,00,000 shipment. Illustrative RoDTEP at 1.5% = ₹15,000; drawback AIR at 2% = ₹20,000 (assumed rates, not actual). If the margin on the order was ₹60,000, the incentives add 58% to margin, which shows why the February 2026 halving of RoDTEP (before restoration on 23 Mar 2026) mattered to thin-margin exporters. EPCG: capital goods import saves ₹30 lakh in duty and taxes, so EO = 6 x 30 = **₹1.8 crore** over 6 years (about ₹30 lakh a year); for domestic purchase the EO is 25% less, **₹1.35 crore**. Missing EO triggers recovery of the duty with interest and possible penalty.

### In the news
See news box. RoDTEP was halved on 23 Feb 2026, restored on 23 Mar 2026, then extended to 31 Dec 2026 on rates unchanged; the Export Promotion Mission (₹25,060 crore) is the structural support layered on top. Budget 2026-27 also raised the duty-free input limit for seafood exporters from 1% to 3% of previous-year FOB.

### Interview angle
> [!question] How it is asked
> "Your client, a garment exporter, has 6% net margin. How much do RoDTEP/RoSCTL, drawback and EPCG matter, and what is the risk in planning around them?"

> [!tip] Strong answer includes
> - Scheme-by-scheme purpose: input duty, embedded tax, capital goods, GST
> - Quantified effect on margin, with caveat that rates are administrative and can change (RoDTEP cut and restoration in 2026)
> - EPCG obligation mechanics and the penalty for shortfall
> - Recommends not building pricing that depends entirely on incentives

---
## 11. SEZ, EOU, FTWZ, Bonded Warehouse and AEO
> 🔴 Tier 1 · _Key points:_ Duty-free enclaves, bonded storage, trusted trader

### Definition
| Regime | What it is | Key benefit |
|---|---|---|
| **SEZ** | Duty-free enclave treated as foreign territory for trade | Duty-free inputs and capital goods, GST/IGST zero-rated supplies, export obligation through positive net foreign exchange |
| **EOU/EHTP/STP** | Unit anywhere that exports its output | Duty-free inputs, exemption from BCD; must export 100% (subject to DTA sale rules) |
| **FTWZ (Free Trade Warehousing Zone)** | SEZ-type zone for warehousing and trading | Duty-free import, storage, re-export, value-added services |
| **Bonded warehouse** | Licensed warehouse where goods are stored without duty until clearance | Duty deferral (pay on ex-bond clearance), re-export without duty |
| **AEO (Authorised Economic Operator)** | CBIC trusted-trader status in tiers (T1, T2, T3; LO for logistics operators) | Faster clearance, lower examination, deferred duty payment at higher tiers, mutual-recognition benefits abroad |

SEZs in India are anchored on the SEZ Act 2005. AEO status rests on compliance records, financial solvency and supply-chain security, and is beneficial for companies running just-in-time lines because dwell time falls ([[007 Lean Manufacturing]]).

### Example
A European brand holds slow-moving spares in an FTWZ near JNPT. Parts are imported duty-free into the zone, held for 4 months and shipped to Gulf customers, with duty payable only if a unit enters the domestic market. For a ₹10 crore stock with 7.5% BCD plus SWS, deferring ₹83 lakh of duty (10,00,00,000 x 8.25%) for four months at 10% p.a. saves about **₹2.75 lakh** in finance cost and removes duty on goods that are re-exported.

### In the news
See news box. The Export Promotion Mission and budget measures (tariff simplification, input duty relief for seafood, aircraft MRO parts) show how policy shifts the value of these regimes. Expect enclave-based incentives to be reshaped over time.

### Interview angle
> [!question] How it is asked
> "A global electronics firm wants a regional spares hub for South Asia. Compare SEZ, FTWZ and bonded warehouse in India."

> [!tip] Strong answer includes
> - Differences in duty treatment, domestic sale rules and compliance
> - Rough economics: duty deferral, avoidance of duty on re-exports, rent and cost
> - AEO for cleared goods and lower dwell time
> - Links to network design ([[113 Network Design & Facility Location Modelling]]) and 3PL options

---
## 12. Container Logistics: FCL vs LCL, Demurrage and Detention
> 🔴 Tier 1 · _Key points:_ TEU, cube vs weight, break-even, free days, demurrage

### Definition
- **Container types:** 20 ft (about 33 m³, practical payload around 26-28 t), 40 ft (about 67 m³), 40 ft high cube (about 76 m³), reefers and open-tops. Capacity is counted in **TEU**.
- **FCL:** full container for one shipper; **LCL:** consolidated by a CFS with others, charged per m³ or tonne (whichever greater, "W/M"); LCL has higher per-unit rate, extra handling and often more transit time and damage risk.
- **Cube vs weight:** a container is either full by volume or by weight. FMCG and apparel are cube-bound; steel and chemicals are weight-bound.
- **Demurrage:** charge levied by the shipping line (and port or CFS storage) when a container stays in the terminal beyond free days. **Detention:** charge when the container is held outside the port beyond free days. Both create a strong incentive for pre-filing, documents ready and prompt return of empties. Disputes hinge on free-time clauses in the B/L or tariff.

$$\text{Break-even volume} = \frac{\text{FCL rate}}{\text{LCL rate per m}^3}$$

### Example
FCL 20 ft at ₹85,000 versus LCL at ₹4,500/m³ (assumed). Break-even = 85,000/4,500 = **18.9 m³**. At 15 m³, LCL costs ₹67,500 (cheaper than FCL by ₹17,500); at 19 m³ it costs ₹85,500 and FCL is cheaper, plus lower handling. A 40 ft container taking 0.06 m³ cartons of 9 kg each at 85% cube use holds int(0.85 x 67 / 0.06) = **949 cartons**, weighing 8.5 t, so it is cube-limited and weight is no issue. Demurrage: 7 free days, container cleared on day 12 with a slab of ₹2,000 per day for the first five days after free time: 5 x ₹2,000 = **₹10,000**, with ₹4,000 per day from the sixth day thereafter. Also see [[140 Packaging, Unitisation & Load Optimisation]] and [[009 Logistics & Distribution]].

### In the news
See news box. Budget measures such as longer export periods for garments and footwear inputs, and the push on clearance reform, aim at reducing the dwell time that causes these charges.

### Interview angle
> [!question] How it is asked
> "Your 12 m³ monthly export is shipped LCL. At what volume would moving to FCL pay for itself?"

> [!tip] Strong answer includes
> - Break-even computation and the qualitative factors (damage, lead time, inventory held to fill the box)
> - Cube vs weight constraint and container selection
> - Demurrage vs detention definitions and how to avoid them
> - Consolidation options (buyer's consolidation, shared FCL)

---
## 13. Trade Policy: DGFT, Anti-Dumping and Trade Remedies
> 🔴 Tier 1 · _Key points:_ FTP, ITC(HS), DGTR, ADD, safeguard, QCO

### Definition
- **DGFT** (Directorate General of Foreign Trade, Ministry of Commerce) issues the **Foreign Trade Policy** (FTP 2023) and notifications under the FT(D&R) Act 1992; it classifies goods in **ITC(HS)** as **free, restricted** (licence or authorisation needed) or **prohibited**.
- **Trade remedies** are run by **DGTR** (Directorate General of Trade Remedies): **anti-dumping duty (ADD)** when imports are sold below normal value and injure domestic industry; **countervailing duty (CVD)** against subsidised imports; **safeguard duty** against a sudden surge of imports regardless of fairness. DGTR recommends; the Department of Revenue notifies duties, normally for five years.
- **Quality Control Orders (QCOs)** under BIS require standard marks for specified products, affecting import eligibility.
- **Non-tariff barriers abroad:** SPS/TBT measures, labelling, and carbon rules such as the EU's CBAM, covered in [[014 Global SCM & Sustainability]].
- **FEMA** and RBI govern realisation of export proceeds and import payments; the period for realising export proceeds is set by RBI (historically 9 months; verify the current rule).

### Example
A buyer sources a chemical at ₹100 per kg from a Chinese supplier. ADD of 20% is notified: landed cost rises by ₹20 on the AV, and for 200 tonnes a year the extra cost is 200,000 kg x ₹20 = **₹40 lakh**, before BCD/IGST on the higher base. The buyer's options: switch to a supplier or country not covered by the notification (many ADDs name specific producers with different rates), qualify an Indian vendor, renegotiate price, or absorb the cost. The question to ask is whether the notification covers the exact HS code and producer.

### In the news
See news box. Frequent tweaks in RoDTEP and the move to simpler tariff slabs show that trade policy is a moving variable: monitor DGFT and CBIC notifications as part of procurement risk ([[015 Supply Chain Risk & Resilience]]).

### Interview angle
> [!question] How it is asked
> "India imposes anti-dumping duty on a key input of your client. What are the options and how do you decide?"

> [!tip] Strong answer includes
> - Differentiates ADD, CVD, safeguard and QCO
> - Looks at the exact product scope and which suppliers carry which rate
> - Quantifies cost impact and compares alternate sources, including domestic
> - Considers hedging via contracts and inventory build before the duty date

---
## 14. ⭐ Advanced: Build-vs-Import Landed-Cost Model with Incentives and FX
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A proper sourcing decision compares **delivered, risk-adjusted cost** across locations:

$$C_{\text{import}} = AV + BCD + SWS + \text{logistics} + \text{inventory carrying cost} + \text{FX hedge cost} + \text{compliance cost} - \text{FTA saving}$$

versus the domestic price including GST (with credit) and inventory. Add the **pipeline inventory** from transit time: 45 days in transit holds capital at the firm's cost of capital. Add **safety stock** rising with lead-time variability (see [[003 Inventory Management]]). Add **FX volatility** (a 2% adverse rupee move on USD 10,000 is ₹17,600 at ₹88).

For exports the corresponding calculation is **net export realisation = FOB value − input cost − logistics + incentives (drawback, RoDTEP, IGST refund) − financing cost**, converted at the realised rate.

### Example
Import option: unit price USD 20, 1,000 units, ₹88/USD (assumed), so product value = ₹17,60,000. BCD plus SWS at 8.25% of AV (AV taken equal to the invoice for simplicity) = ₹1,45,200; freight, CHA and port = ₹95,000; landed value excluding creditable IGST = ₹20,00,200. Carrying cost for 60 days in the pipeline at 12% p.a. = ₹39,456; a hedge cost of 1% of product value = ₹17,600. Total = **₹20,57,256**, or about **₹2,057 per unit**. Domestic option: ₹2,150 per unit ex-GST (GST creditable), with 15 days of pipeline at 12% adding ₹10,603 on ₹21.5 lakh, so about **₹2,161 per unit**. Import wins by roughly 4.8% before risk. Sensitivity: the advantage vanishes at about **₹92.6/USD**, a 5.3% rupee depreciation; at ₹92.4 the import cost rises to about ₹2,155 per unit, almost level. Consultants should present a sensitivity table and the break-even exchange rate, not a single number.

### In the news
See news box. As FTAs open the UK and potentially the EU, and duty slabs fall, more categories will shift toward imports or exports on landed cost, so structured models matter.

### Interview angle
> [!question] How it is asked
> "Build a quick landed-cost comparison between a China, Vietnam and domestic supplier, and tell me when you'd choose the more expensive one."

> [!tip] Strong answer includes
> - A structured cost buildup with taxes treated correctly (creditable GST not a cost)
> - Risk adjustments: lead time, quality, geopolitical, FX, duty change
> - A sensitivity or break-even, not just a point estimate
> - Strategic criteria: dual sourcing, China+1, resilience ([[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]])
