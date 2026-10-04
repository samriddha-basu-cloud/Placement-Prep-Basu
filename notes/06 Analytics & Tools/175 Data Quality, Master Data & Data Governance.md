---
tags: [analytics-tools, tier2]
area: Analytics & Tools
topic: "Data Quality, Master Data & Data Governance"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# Data Quality, Master Data & Data Governance

⬅ [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]] · [[_Index - Analytics & Tools|Analytics & Tools]]

> **Area:** Analytics & Tools · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Why Data Quality Matters in Operations and Supply Chains]]
2. [[#2. Data Quality Dimensions: Accuracy, Completeness, Consistency, Timeliness, Uniqueness, Validity]]
3. [[#3. Master, Transactional and Reference Data in Supply Chains]]
4. [[#4. Impact of Bad Master Data on MRP, Safety Stock and Shipping]]
5. [[#5. Vendor and Customer Master: Duplicates, Fraud Risk and Payments]]
6. [[#6. Master Data Management (MDM): Architectures and the Golden Record]]
7. [[#7. Matching, Deduplication and Survivorship]]
8. [[#8. Data Governance: Council, Owners, Stewards and Policies]]
9. [[#9. Data Lineage, Catalog, Glossary and Metadata]]
10. [[#10. Data Quality KPIs, Scorecards and the Cost of Poor Quality]]
11. [[#11. India Focus: DPDP Act Basics and Statutory Master Data (GSTIN, PAN, HSN)]]
12. [[#12. Worked Data-Cleaning Checklist for an Item or Vendor Master]]
13. [[#13. ⭐ Advanced: SAP Master Data Governance and Data Migration Quality Gates]]
14. [[#14. ⭐ Advanced: Data Governance for AI and Analytics]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI projects and India's new privacy law both raise the price of bad data
> **Gartner on AI-ready data (26 February 2025).** Gartner predicted that **60% of AI projects will be abandoned through 2026** if they are not supported by AI-ready data, and reported that **63% of organisations** either do not have or are unsure they have the right data-management practices for AI. Its five recommended steps include assuring data quality through testing and monitoring and evolving metadata management. ([Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk))
>
> **Cost of poor data quality (Gartner, 2020 research).** Gartner's data-quality page still cites that poor data quality costs organisations **at least US$12.9 million a year on average**, and defines nine quality dimensions: accessibility, accuracy, completeness, consistency, precision, relevancy, timeliness, uniqueness and validity. The figure is a survey-based average from 2020, not a measurement for any one firm. ([Gartner: data quality](https://www.gartner.com/en/data-analytics/topics/data-quality))
>
> **India's DPDP Rules, 2025 (notified mid-November 2025).** The Rules operationalise the Digital Personal Data Protection Act, 2023 with an **18-month phased compliance period**: the Data Protection Board provisions took effect immediately, consent-manager provisions follow after 12 months (about 13 November 2026), and the core obligations apply from about **13 May 2027**. The Act's penalty tiers run up to **₹250 crore** for failing to keep reasonable security safeguards, ₹200 crore for breach-notification failures or violations on children's data, and ₹50 crore for other violations. In early 2026 MeitY consulted on shortening the timeline for Significant Data Fiduciaries to about 12 months; trade-law commentary (February 2026) described that as still a proposal. Check the latest gazette notification before quoting dates. ([PIB: DPDP Rules, 2025](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf), [Consent.in timeline](https://www.consent.in/blog/dpdp-rules), [Chambers: proposed shortening](https://chambers.com/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Why Data Quality Matters in Operations and Supply Chains
> 🟠 Tier 2 · _Key points:_ garbage in, garbage out; cost of poor data; decisions, automation and AI all depend on data; data as an asset

### Definition
**Data quality (DQ)** is the degree to which data is fit for its intended use: it must describe the real world correctly, be present when needed and be consistent across systems. In a supply chain, data feeds every planning and execution decision: [[004 Demand Forecasting & Planning|forecasts]], [[119 Supply Planning, DRP & Available-to-Promise|MRP and DRP runs]], [[003 Inventory Management|safety stock]], [[125 Transportation Management Deep Dive|freight costing]], supplier payments and customer service promises.

Why it is an operations issue, not an IT issue:
- **Automation amplifies errors.** A wrong lead time in one record becomes wrong planned orders for thousands of MRP runs.
- **Errors compound across systems.** The same material may exist with different units in ERP, WMS and TMS ([[013 ERP & Enterprise Systems (SAP-Oracle)]]).
- **Analytics trust.** If users distrust the dashboard, they revert to Excel ([[047 MIS & Dashboard Design]]).
- **Compliance.** Wrong GSTIN, HSN or address data causes tax mismatches and failed e-invoices ([[227 GST & Indirect Tax for Supply Chains]]).

The classic prevention hierarchy is the **1-10-100 heuristic**: roughly ₹1 to prevent a bad record at entry, ₹10 to detect and correct it later, ₹100 once it has caused a business failure. Treat it as a teaching heuristic, not a measured law.

### Example
A distributor loads 500 new SKUs a quarter and 8% (40 SKUs) have wrong case-pack quantities. Using the heuristic with an illustrative ₹50 base cost per record: catching the 40 errors at entry costs $40\times50=₹2{,}000$; finding and correcting them later costs $40\times500=₹20{,}000$; and if each reaches a customer as a mis-ship or return it costs $40\times5000=₹2{,}00{,}000$. The practical point is the ordering: a mandatory-field or case-pack validation at creation is the cheapest control.

### In the news
See news box. Gartner's AI-readiness finding means data quality now decides whether AI investments ([[099 ML for Operations & SCM]]) pay back at all.

### Interview angle
> [!question] How it is asked
> "Why do many supply chain analytics and ERP projects fail, and what has data to do with it?"

> [!tip] Strong answer includes
> - Link bad master data to concrete failures (wrong lead time to late orders; wrong dimensions to freight overcharge)
> - Prevention is cheaper than correction (validation at entry, ownership)
> - Quality is fit-for-purpose and measurable, not a one-time clean-up
> - Ownership sits with the business, supported by IT
> - A quantified example from an internship or case

---
## 2. Data Quality Dimensions: Accuracy, Completeness, Consistency, Timeliness, Uniqueness, Validity
> 🟠 Tier 2 · _Key points:_ six core dimensions; how each is measured; additional dimensions (precision, relevancy, accessibility)

### Definition
| Dimension | Question | Typical measure | Supply chain example |
|---|---|---|---|
| **Accuracy** | Does the value match reality? | % values matching a trusted source or physical check | Recorded pallet weight 480 kg vs measured 520 kg |
| **Completeness** | Is everything required present? | % non-null in mandatory fields | Missing HSN code or lead time on items |
| **Consistency** | Is it the same across systems and fields? | % records matching across sources | Material unit "EA" in ERP, "PC" in WMS |
| **Timeliness** | Is it current enough for the use? | Age since last update; latency | Supplier lead time last reviewed 3 years ago |
| **Uniqueness** | Is each entity stored once? | Duplicate rate | Same vendor under three vendor codes |
| **Validity** | Does it follow format and business rules? | % passing rules | GSTIN format, pincode six digits, lead time greater than 0 |

Gartner lists nine dimensions (adding accessibility, precision and relevancy); other frameworks (DAMA) use similar sets with "integrity" and "reasonableness". In an interview, give the six, then add one or two others with an example.

Measure each as a percentage: $$\text{Completeness}=\frac{\text{records with all mandatory fields populated}}{\text{total records}}\times100$$ and $$\text{Uniqueness}=1-\frac{\text{duplicate records}}{\text{total records}}$$

### Example
A 10,000-item material master audit finds 420 items without HSN code, 180 duplicate items, 60 items with an invalid unit of measure and 900 items whose lead times are older than 24 months. Completeness for HSN is $1-420/10000=95.8\%$, uniqueness is $98.2\%$, validity of UoM is $99.4\%$ and timeliness of lead times is $91.0\%$. Weighting these 30%, 20%, 30%, 20% gives a composite score of $0.3\times0.958+0.2\times0.982+0.3\times0.994+0.2\times0.91 = 96.4\%$. A composite hides the problem: the 91% timeliness may matter far more for A-class items, so also score by item class.

### In the news
See news box. Gartner's nine-dimension list shows that a "dimension" list differs by source: stick to a definition and examples rather than memorising a number.

### Interview angle
> [!question] How it is asked
> "What are the dimensions of data quality? Give a supply chain example for each."

> [!tip] Strong answer includes
> - The six with a one-line definition and a concrete example each
> - How each is measured (percentages, thresholds, rules)
> - Which dimension matters most for which decision (timeliness for lead times, accuracy for dimensions)
> - Mention that dimensions overlap (validity vs accuracy: a valid GSTIN can still be the wrong supplier)
> - Prioritise by business impact and class of item

---
## 3. Master, Transactional and Reference Data in Supply Chains
> 🟠 Tier 2 · _Key points:_ master data defines entities; transactional records events; reference data are code lists; domains: material, vendor, customer, BOM, routing, location

### Definition
- **Master data:** slowly changing core business entities shared across processes: materials/products, vendors/suppliers, customers, plants and warehouses, BOMs, routings, work centres, pricing conditions, employees, chart of accounts.
- **Transactional data:** events that reference master data: purchase orders, goods receipts, sales orders, shipments, invoices.
- **Reference data:** standardised code lists: units of measure, currencies, country and state codes, HSN/SAC codes, Incoterms, payment terms.
- **Metadata:** data about data (definitions, owners, formats, lineage).

Why master data deserves special treatment: it is **created once but used thousands of times**. A wrong record is multiplied by every transaction that points to it ([[080 SAP MM — Materials Management]], [[191 SAP MM Advanced - Inventory, Batches & Special Stocks]]).

| Domain | Critical attributes in operations |
|---|---|
| **Material/product** | UoM and conversions, dimensions, weight, shelf life, MRP type, lot size, lead time, safety stock, HSN, serialisation, hazardous class |
| **Vendor** | Legal name, PAN, GSTIN, bank account, payment terms, address, lead time, minimum order quantity, certification |
| **Customer** | Legal entity, ship-to vs bill-to, GSTIN, delivery windows, credit limit, price group |
| **BOM and routing** | Components, quantities, scrap, operations, standard times ([[081 SAP PP — Production Planning]]) |
| **Location** | Plant, storage location, address, pincode, dock constraints |

### Example
A single material "Brake Pad Set" appears in the ERP with a base UoM of "PC", the WMS counts it in "BOX" of 4, and the TMS ships it as "KG". When a customer orders 100 pieces, the WMS picks 100 boxes (400 pieces), the TMS books freight for 100 kg, and the invoice is for 100 pieces: three systems, three truths, one shipment dispute. The fix is one governed material record with approved conversion factors synchronised to all systems.

### In the news
See news box. The DPDP Act treats customer, driver and employee-contact data as personal data, so customer master records now carry legal obligations as well as operational value.

### Interview angle
> [!question] How it is asked
> "What is the difference between master data and transactional data? Why does it matter for MRP?"

> [!tip] Strong answer includes
> - Definitions and examples; reference data as a third type
> - Master data errors multiply across transactions
> - Domain-specific critical attributes (lead time, lot size, UoM)
> - Ownership: business owns, IT provides tooling
> - Link to a real planning failure caused by a master data field

---
## 4. Impact of Bad Master Data on MRP, Safety Stock and Shipping
> 🟠 Tier 2 · _Key points:_ lead time, lot size, UoM, BOM errors; late orders; wrong safety stock; freight mis-billing and truck-fill errors

### Definition
Planning logic converts master-data parameters directly into actions ([[193 SAP MRP Deep Dive - Planning Strategies & Parameters]], [[005 Production & Operations Planning]]):
- **Lead time (planned delivery time):** sets order release date. Too short means late arrivals and stockouts; too long means excess inventory.
- **Safety stock formula:** $SS = z\,\sigma_d\sqrt{L}$, so an understated $L$ gives a proportionally smaller buffer (see [[003 Inventory Management]]).
- **Lot size and rounding value:** affect order quantities and cash tied up.
- **BOM quantities and scrap:** drive component requirements.
- **Dimensions, weight and stacking data:** drive truck loading, volumetric freight and warehouse slotting ([[140 Packaging, Unitisation & Load Optimisation]], [[009 Logistics & Distribution]]).
- **UoM conversions:** drive purchase quantities and invoices.

### Example
**Lead-time error in MRP.** An item has recorded lead time 4 days, actual 9 days, daily demand mean 200 units, daily standard deviation 40, service z = 1.65.
- Recorded safety stock: $1.65\times40\times\sqrt4 = 132$ units; actual need $1.65\times40\times\sqrt9 = 198$ units, a shortfall of 66 units (one-third).
- Reorder point recorded: $200\times4+132 = 932$; actual: $200\times9+198 = 1998$, a gap of 1,066 units.
- If the material is needed on 1 November, MRP releases the order on 28 October (1 Nov minus 4 days) but the goods arrive on 6 November: five days late, so production waits or expedites.

**Dimension error in freight.** Carton recorded as 40 x 30 x 25 cm, actual 60 x 40 x 30 cm, dead weight 8 kg, volumetric divisor 5,000 cm³/kg. Recorded volumetric weight is $40\times30\times25/5000 = 6$ kg (chargeable 8 kg); actual is $60\times40\times30/5000 = 14.4$ kg (chargeable 14.4 kg). At 1,200 cartons a month and ₹18 per kg, the planned cost is $1200\times8\times18 = ₹1,72,800$ against actual $1200\times14.4\times18 = ₹3,11,040$, a monthly surprise of ₹1,38,240 and a truck that fills much earlier than the plan.

### In the news
See news box. As AI planning and agents ([[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]) take more decisions automatically, these master-data parameters become the silent drivers of automated errors.

### Interview angle
> [!question] How it is asked
> "Your safety stock numbers look low and stockouts are rising. Where do you look first?"

> [!tip] Strong answer includes
> - Check master data first: lead time, lot size, MRP type, review period
> - Compare recorded vs actual lead time (receipt dates) and demand variability
> - Quantify the gap with $SS=z\sigma\sqrt{L}$
> - Fix at the source with an owner and a review cycle, not one-off overrides
> - Track a KPI such as % items with lead time updated in last 12 months

---
## 5. Vendor and Customer Master: Duplicates, Fraud Risk and Payments
> 🟠 Tier 2 · _Key points:_ duplicate vendors, bank-detail changes, PAN/GSTIN checks, ship-to vs bill-to; segregation of duties

### Definition
Vendor master data touches cash. Typical problems:
- **Duplicate vendors** (different spellings, multiple codes) causing duplicate payments, missed volume discounts and distorted spend analysis ([[122 Spend Analysis, Savings & Procurement Maturity]]).
- **Weak bank-detail change control**, a common route for payment fraud (a "vendor" requests a new account by email).
- **Missing or invalid statutory IDs** (PAN, GSTIN, MSME registration), leading to input-tax-credit problems and payment-timing breaches under MSME rules ([[136 Supply Chain Finance & Working Capital]]).
- **Inactive vendors** left open, an unnecessary risk.

Customer master problems: wrong ship-to addresses, mixed bill-to and ship-to, duplicate accounts (credit limit split), invalid GSTIN (failed e-invoice), outdated delivery windows ([[138 Order Management, Customer Service & Cost-to-Serve]], [[082 SAP SD — Sales & Distribution]]).

Controls: **maker-checker** (separate creator and approver), **mandatory fields**, **GSTIN/PAN validation** against official services, **duplicate check at creation**, periodic **block-and-review** of dormant vendors, and audit logs of changes. See [[199 SAP Ariba, SRM & Business Network]] and [[192 SAP Sourcing & Procurement Deep Dive]] for supplier onboarding workflows.

### Example
A company finds that "Sharma Traders Pvt Ltd" and "Sharma Trader Pvt. Ltd." exist as two vendor codes with the same PAN. An invoice of ₹4.2 lakh was entered once under each code and paid twice. Recovery needs a credit note, and the audit trail shows the duplicate was created because the creation screen had no PAN-based duplicate check. Fix: make PAN mandatory, block creation if the PAN already exists, and run a monthly duplicate-payment report (same amount, same invoice number, similar vendor name).

### In the news
See news box. Under the DPDP framework, customer and supplier-contact personal data must be accurate, secured and erased when no longer needed, which strengthens the case for cleaning dormant records.

### Interview angle
> [!question] How it is asked
> "How would you reduce duplicate payments and vendor fraud?"

> [!tip] Strong answer includes
> - Preventive controls: mandatory PAN/GSTIN, duplicate check, maker-checker, bank-change verification by call-back
> - Detective controls: duplicate payment analytics, dormant vendor review
> - Ownership between procurement, finance and master data team
> - KPI: duplicate rate, % vendors validated, time to onboard
> - Quantified example

---
## 6. Master Data Management (MDM): Architectures and the Golden Record
> 🟠 Tier 2 · _Key points:_ golden record, single source of truth, registry vs consolidation vs coexistence vs centralised, hub, survivorship

### Definition
**Master data management (MDM)** is the discipline, process and technology that creates and maintains a consistent, accurate "single version of the truth" for key entities. The result for each entity is a **golden record**: the best consolidated record, built from multiple sources by matching and **survivorship rules** (which source wins for which attribute).

Common MDM implementation styles:
| Style | How it works | Pros | Cons |
|---|---|---|---|
| **Registry** | Hub stores only index/keys linking source records; sources keep their data | Fast, light, low disruption | No cleansed master to push back; reads need federation |
| **Consolidation** | Hub merges data for reporting, analytics | Good for BI; source systems unchanged | Read-only; sources stay dirty |
| **Coexistence** | Golden record maintained in hub and synchronised back to sources | Balances flexibility and control | Complex synchronisation |
| **Centralised/transaction** | All creation and change happens in the hub first | Strongest control and quality | Highest change effort; process redesign |

Typical MDM process: **collect → standardise and cleanse → match → merge (golden record) → govern (workflow and approvals) → distribute** to consuming systems. In SAP landscapes, central master data creation is often supported by SAP Master Data Governance (see sub-topic 13).

### Example
Vendor "ABC Logistics" exists in three systems: ERP (address A, GSTIN valid, bank account 1), TMS (address B, no GSTIN) and the procurement portal (address A, updated email). Survivorship rules: GSTIN and bank account come from ERP (finance-validated), address from the most recently updated record, email from the portal. The golden record combines these; the hub then pushes the merged attributes back to the TMS (coexistence), and the TMS stops creating its own vendor code.

### In the news
See news box. AI-readiness advice from Gartner (align data to use cases, evolve metadata) is effectively a modern restatement of MDM: define what a "customer" or "material" means once, then govern it.

### Interview angle
> [!question] How it is asked
> "What is a golden record and how would you build one for suppliers?"

> [!tip] Strong answer includes
> - Define golden record and survivorship rules per attribute
> - MDM styles (registry to centralised) and when each fits
> - Process: standardise, match, merge, approve, distribute
> - Governance: data owner, stewards, workflows
> - Tool-agnostic approach plus mention of SAP MDG or similar

---
## 7. Matching, Deduplication and Survivorship
> 🟠 Tier 2 · _Key points:_ standardisation, exact vs fuzzy matching, similarity scores, blocking, thresholds, human review, merge rules

### Definition
**Deduplication** (record linkage) proceeds in steps:
1. **Standardise:** lower-case, trim spaces, remove punctuation, expand abbreviations, drop legal suffixes (Ltd, Pvt, Limited).
2. **Block:** compare only records that share a key (first letters, pincode, PAN) to avoid comparing every pair.
3. **Match:** exact match on strong identifiers (PAN, GSTIN, email), fuzzy match on names and addresses using edit distance (Levenshtein), token-based or phonetic algorithms.
4. **Score and decide:** auto-merge above a high threshold, send to a data steward in a middle band, treat as distinct below it.
5. **Survivorship:** choose which attribute value survives (most recent, most complete, most trusted source).
6. **Audit:** log merges and allow unmerge.

Levenshtein-based similarity: $$\text{similarity}=1-\frac{\text{edit distance}}{\max(|a|,|b|)}$$

Strong identifiers beat fuzzy names: the PAN occupies characters 3 to 12 of a GSTIN, so two GSTINs with the same PAN belong to the same legal entity (different states or branches).

### Example
After normalising names (lower-case, punctuation removed, legal suffixes dropped):
- "Tata Steel Ltd" and "TATA STEEL LIMITED" both become "tata steel": distance 0, similarity 1.00, so auto-merge.
- "Sharma Traders Pvt Ltd" and "Sharma Trader Pvt. Ltd." become "sharma traders" and "sharma trader": distance 1, similarity $1-1/14 = 0.929$, so merge candidate or steward review depending on the threshold.
- "ABC Logistics" and "ABC Logistic Services" become "abc logistics" and "abc logistic services": distance 8, similarity 0.619, so fuzzy matching alone would call them distinct. Only a shared PAN or address would reveal they may be the same entity, which shows why name similarity needs support from identifiers.

```python
def lev(a, b):
    d = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        prev, d[0] = d[:], i
        for j, cb in enumerate(b, 1):
            d[j] = min(prev[j] + 1, d[j - 1] + 1, prev[j - 1] + (ca != cb))
    return d[-1]

sim = lambda a, b: 1 - lev(a, b) / max(len(a), len(b))
print(round(sim("sharma traders", "sharma trader"), 3))  # 0.929
```

### In the news
See news box. As data volumes grow, firms use ML-based entity resolution, but Gartner's note on continuous monitoring means that thresholds and false-merge rates still need human oversight.

### Interview angle
> [!question] How it is asked
> "How would you find and merge duplicate vendors in 50,000 records?"

> [!tip] Strong answer includes
> - Standardise then block then match (exact on PAN/GSTIN, fuzzy on names and addresses)
> - Thresholds: auto-merge, steward review, distinct
> - Survivorship rules and audit/unmerge capability
> - Avoid false merges (two legal entities with similar names)
> - Prevent re-creation with duplicate checks at entry; pandas or SQL for the prototype ([[064 Pandas — Data Manipulation]], [[056 JOINs — All Types]])

---
## 8. Data Governance: Council, Owners, Stewards and Policies
> 🟠 Tier 2 · _Key points:_ governance council, data owner, data steward, custodian; policies, standards, RACI; operating model

### Definition
**Data governance** is the set of decision rights, roles, policies and processes that ensure data is managed as an asset: who may create, change and use which data, to what standard. It is different from **data management** (the execution) and from **data quality** (the outcome).

Typical roles:
| Role | Responsibility |
|---|---|
| **Data governance council / steering committee** | Senior cross-functional body; sets policy, priorities, resolves disputes, funds initiatives |
| **Data owner** | Business executive accountable for a domain (e.g. Head of Procurement owns vendor data) |
| **Data steward** | Day-to-day guardian: defines rules, monitors quality, resolves issues |
| **Data custodian** | IT/technical owner of systems and security |
| **Data producer and consumer** | Create and use data; follow the rules and report issues |

Building blocks: a **data glossary** (agreed definitions, e.g. what counts as an "active customer"), **standards** (naming, formats, mandatory fields), **policies** (retention, access, privacy), **a RACI**, **issue management** and **KPIs**. Start small: pick two or three high-value domains (material and vendor), appoint owners, define the top 10 quality rules, publish a scorecard, and extend.

### Example
A manufacturer forms a council chaired by the COO with heads of procurement, planning, finance, sales and IT. Rules agreed: a material may be created only via a workflow with planning approval of lead time and lot size; a vendor may be created only with valid PAN, GSTIN and bank proof verified by finance. The stewards publish a monthly scorecard (see sub-topic 10); in this illustrative case the duplicate vendor rate falls from 3.1% to 0.8% after six months, and MRP exception messages drop. Governance succeeded because ownership sat with the business and the council removed blockers.

### In the news
See news box. The DPDP Rules create statutory duties (breach notice, erasure, accountability) that need exactly these roles: a named contact for data queries, owners for personal data domains and logged processes.

### Interview angle
> [!question] How it is asked
> "How would you set up data governance in a company that has none?"

> [!tip] Strong answer includes
> - Start with business pain and 2-3 domains, not a grand programme
> - Roles: council, owners, stewards, custodians, with decision rights
> - Policies and glossary, issue process, KPIs reviewed regularly
> - Quick wins to build credibility (e.g. duplicate vendor clean-up)
> - Link to change management and incentives (stewards need time and recognition)

---
## 9. Data Lineage, Catalog, Glossary and Metadata
> 🟠 Tier 2 · _Key points:_ metadata types, lineage (source to report), data catalog, business glossary, impact analysis

### Definition
- **Metadata:** technical (table, column, type), business (definition, owner, sensitivity) and operational (refresh time, row counts, quality score).
- **Data lineage:** the traceable path of data from source through transformations to reports and models. **Upstream** lineage answers "where did this number come from?"; **downstream** lineage answers "what breaks if I change this field?" (impact analysis).
- **Data catalog:** a searchable inventory of datasets with metadata, owners, usage, quality scores and access requests.
- **Business glossary:** agreed definitions of terms (OTIF, fill rate, active customer) linked to the data fields that implement them ([[012 Supply Chain Analytics & KPIs]]).
- **Data contracts / SLAs:** agreements between producers and consumers on schema and freshness.

Why it matters: in a modern stack (ERP to data lake to warehouse to dashboard) numbers pass through many transformations ([[182 Data Modelling for Analytics - Star Schema, SCD & Warehouses]], [[045 SQL for Operations Analytics]]). Without lineage, reconciling a mismatch takes days and trust erodes.

### Example
The CFO's dashboard shows OTIF of 91%; the supply chain head's report shows 86%. A catalog and lineage view reveals that the CFO's view counts delivery date at dispatch, while the supply chain report counts at proof of delivery, and one applies a 2-day tolerance. The business glossary then fixes one definition (on-time means delivered within the agreed window by the carrier POD), and both reports are rebuilt from the same governed table.

### In the news
See news box. Gartner's recommendation to "evolve metadata management" for AI shows that catalogs and lineage are moving from compliance tooling to prerequisites for trusted AI.

### Interview angle
> [!question] How it is asked
> "Two reports show different OTIF numbers. How would you resolve it?"

> [!tip] Strong answer includes
> - Trace lineage: source tables, filters, date logic, tolerance, exclusions
> - Agree a single definition in the glossary and one governed dataset
> - Add data tests and a catalog entry with owner
> - Communicate the change and retire duplicate reports
> - Mention process mining or SQL reconciliation as tools ([[173 Process Mining & Operations Intelligence]])

---
## 10. Data Quality KPIs, Scorecards and the Cost of Poor Quality
> 🟠 Tier 2 · _Key points:_ completeness, uniqueness, validity, timeliness rates; thresholds, trend, root cause; link to Six Sigma and cost of poor quality

### Definition
A **data quality scorecard** reports each critical data element's rule, measured score, target and trend by domain and owner. Common KPIs:
- % mandatory fields populated (completeness)
- Duplicate rate (uniqueness)
- % records passing validation rules (validity)
- % records reviewed or updated within a period (timeliness)
- Cross-system match rate (consistency)
- Defect rate and **time to fix** (DQ incidents closed within SLA)
- **Business-impact KPIs:** expedites due to data errors, rework hours, failed e-invoices, mis-shipments caused by master data, MRP exception volume

Use the [[008 Six Sigma & Quality Tools|Six Sigma]] mindset: define the critical-to-quality data element, measure the defect rate, analyse root causes (Pareto, 5 Whys), improve (validation, training), and control (monitoring). A defect rate converts to DPMO: $$\text{DPMO}=\frac{\text{defects}}{\text{records}\times\text{opportunities per record}}\times10^6$$

### Example
Vendor master audit: 2,000 vendors, 5 mandatory critical fields each (10,000 opportunities), 150 defects found. $\text{DPMO}=150/10000\times10^6=15{,}000$. Pareto of the 150 defects: bank proof missing 60 (40%), invalid GSTIN 45 (30%), payment terms blank 30 (20%), other 15 (10%). Fixing the top two removes 70% of defects. A control is added: GSTIN validation at entry and a mandatory bank-proof upload; the next audit finds 38 defects, so DPMO falls to 3,800, a 74.7% reduction (check: $1-38/150 = 0.7467$).

### In the news
See news box. Gartner's per-company cost estimate is large but generic; build your own cost-of-poor-quality view from rework hours, expedited freight and write-offs, which is more persuasive to a CFO.

### Interview angle
> [!question] How it is asked
> "How would you measure and report data quality to leadership?"

> [!tip] Strong answer includes
> - Scorecard by domain and critical data element with owner, target, trend
> - Mix of technical rates and business-impact measures
> - Pareto and root causes, then controls
> - Reporting cadence and escalation to the council
> - Convert quality improvement into rupees (rework, expedites, write-offs)

---
## 11. India Focus: DPDP Act Basics and Statutory Master Data (GSTIN, PAN, HSN)
> 🟠 Tier 2 · _Key points:_ Data Fiduciary and Data Principal, consent, notice, purpose limitation, accuracy duty, security, breach, erasure, penalties; GSTIN structure and checksum

### Definition
**Digital Personal Data Protection Act, 2023 (DPDP Act):** India's general personal data law, operationalised by the DPDP Rules, 2025 (see news box for dates and penalties). Core terms and duties (verify against the bare Act and Rules):
- **Data Principal:** the individual the data is about (customer, employee, driver). **Data Fiduciary:** the entity deciding purpose and means of processing. **Data Processor:** processes on the fiduciary's behalf. **Significant Data Fiduciary:** a notified entity with larger risk (extra duties such as audits and impact assessments).
- Processing needs **consent** or a listed legitimate use, with a clear **notice** of purpose.
- **Purpose limitation and minimisation:** collect only what is needed.
- **Accuracy duty:** where personal data is used to decide something affecting the individual or is shared with another fiduciary, the fiduciary must make reasonable efforts to keep it complete, accurate and consistent (Section 8(3), check the bare Act). This is a direct data quality obligation.
- **Security safeguards, breach notification** (to the Board and affected persons), **retention limits and erasure** when the purpose ends or consent is withdrawn.
- **Rights:** access, correction and erasure, grievance redress, nomination.
- Special rules for children's data (verifiable parental consent).
- Penalties up to ₹250 crore for security-safeguard failure (per the Act's schedule, via PIB summary).

**Statutory identifiers in supply chain master data:**
- **GSTIN (15 characters):** 2-digit state code + 10-character PAN + 1 entity number + "Z" + 1 check character. The check character is computed with a modulus-36 algorithm.
- **PAN:** 10 characters (5 letters, 4 digits, 1 letter).
- **HSN:** 4/6/8-digit commodity codes driving GST rate and customs ([[126 International Trade Documentation, Customs & Trade Finance]]).
- **Pincode:** 6 digits; first digit region.

### Example
**GSTIN checksum.** Take a commonly used sample GSTIN "27AAPFU0939F1ZV". Convert each of the first 14 characters to a value (0-9 as digits, A=10 to Z=35), multiply alternate positions by 1 and 2, add the quotient and remainder after dividing each product by 36, sum, and the check character is the value of $(36-(S \bmod 36)) \bmod 36$. The calculation gives "V", matching the last character, so the number is structurally valid. (A structurally valid GSTIN may still be cancelled or belong to someone else, so confirm status on the GST portal.)

```python
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def gst_check(first14):
    s = 0
    for i, c in enumerate(first14):
        v = chars.index(c) * (1 if i % 2 == 0 else 2)
        s += v // 36 + v % 36
    return chars[(36 - s % 36) % 36]

print(gst_check("27AAPFU0939F1Z"))  # V
```

**DPDP angle.** A logistics firm keeps driver Aadhaar scans and phone numbers in a shared folder forever. Under the Act it needs a purpose, security, a retention period and an erasure process: governance, not just IT, must own this.

### In the news
See news box. The two dates to remember are November 2026 (consent managers) and May 2027 (core obligations), with a proposal to bring forward some duties for Significant Data Fiduciaries; track the notification status.

### Interview angle
> [!question] How it is asked
> "What is the DPDP Act and what would it change for a supply chain team?"

> [!tip] Strong answer includes
> - Key terms (Data Principal, Data Fiduciary) and the principles (consent, purpose, minimisation, accuracy, security, erasure)
> - Practical impact: customer and driver data, vendor contact details, CCTV, tracking and apps; vendor contracts as processors
> - Penalty scale (up to ₹250 crore) and the phased timeline, with a caution that dates are being refined
> - The accuracy duty as a link to data quality
> - Governance steps: data inventory, notices, retention schedule, breach playbook

---
## 12. Worked Data-Cleaning Checklist for an Item or Vendor Master
> 🟠 Tier 2 · _Key points:_ profile, standardise, validate, deduplicate, enrich, correct at source, monitor; document every step

### Definition
A repeatable checklist (also see [[186 Python Data Cleaning & EDA Playbook]], [[064 Pandas — Data Manipulation]], [[075 Pivot Tables & Power Query]]):
1. **Scope and owner:** which table, which decision it supports, who approves changes.
2. **Backup and profile:** keep an untouched copy; count rows; null rate per column; distinct values; min/max.
3. **Standardise:** trim, case, dates, units, legal suffixes, code lists.
4. **Validate rules:** formats (GSTIN, PAN, pincode), ranges (lead time 1-180 days), cross-field (shelf life greater than 0 for batch items).
5. **Deduplicate:** exact on keys, fuzzy on names, review band.
6. **Resolve outliers and nulls:** fix from source, impute only if defensible, or flag.
7. **Enrich:** HSN from description, geocode addresses.
8. **Correct at source (system of record)**, not only in the extract; load via governed process ([[200 SAP S-4HANA Migration, Data Migration & Testing]]).
9. **Re-measure and report:** before-after DQ scores; keep a change log.
10. **Prevent:** entry validation, workflow, periodic review.

### Example
```python
import pandas as pd, re
df = pd.read_csv("material_master.csv")
df["desc_clean"] = df["desc"].str.strip().str.lower()

null_rate = df.isna().mean().round(3)                       # completeness
dup_keys  = df[df.duplicated("matnr", keep=False)]          # uniqueness
bad_lt    = df[(df.lead_time_days <= 0) | (df.lead_time_days > 180)]  # validity
gst_re = re.compile(r"^\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]$")
df["gstin_ok"] = df.gstin.fillna("").apply(lambda s: bool(gst_re.match(s)))
```
On a 5-row test table with one duplicate material number, three out-of-range lead times (-2, 0 and 400 days), one malformed GSTIN and one missing GSTIN, the checks flag exactly those rows. The format check alone passes a GSTIN whose check character is wrong ("...F1ZX"), which is why the checksum from sub-topic 11 is added as a second rule. Output goes to a steward-review sheet with columns for proposed correction and approver, not directly to the system.

### In the news
See news box. Gartner's advice to assure data quality "through testing and monitoring" maps to automating these checks as scheduled rules, not one-off clean-ups.

### Interview angle
> [!question] How it is asked
> "You receive a messy vendor master from a client. How would you clean it?"

> [!tip] Strong answer includes
> - Profile before changing; keep raw data and a log
> - Rule-based checks, deduplication with thresholds, steward approval
> - Fix at the source and prevent recurrence
> - Before-after metrics and business impact
> - Communicate assumptions and what could not be verified

---
## 13. ⭐ Advanced: SAP Master Data Governance and Data Migration Quality Gates
> ⭐ Advanced · _Added beyond the tracker_

### Definition
In SAP landscapes the **material master** is organised into views (basic data, purchasing, MRP, work scheduling, storage, accounting, sales) maintained by different departments ([[080 SAP MM — Materials Management]], [[079 SAP Fundamentals & Architecture]]). Without a controlled process, each department edits its own view and inconsistencies appear. **SAP Master Data Governance (MDG)** adds central creation and change workflows, validation rules, duplicate checks and audit trails for material, business partner (customer and vendor), finance and other domains.

During an **S/4HANA migration**, data quality becomes a project critical path ([[200 SAP S-4HANA Migration, Data Migration & Testing]], [[201 SAP Landscape, Transports, Security & GRC Basics]]): the **Business Partner** model unifies vendor and customer masters, duplicates must be resolved before loading, and legacy codes need mapping. Good practice: **quality gates** with pass thresholds (for example 98% valid on critical fields) before each mock load, owner sign-off by domain, and reconciliation reports comparing legacy and target counts and values.

### Example
For a plant migration: 30,000 materials in legacy; profiling finds 3,200 obsolete (no movement in 5 years), 1,100 duplicates and 900 with invalid UoM conversion. The team decides to migrate only active items ($30000-3200=26{,}800$), merge the 1,100 duplicates found among them (assuming each is one surplus copy, leaving $26800-1100=25{,}700$ unique active materials), and fix the 900 conversions before the second mock load. Gate: at least 98% of critical fields valid, otherwise cutover is postponed. The business benefit is a smaller, cleaner master and a faster MRP run after go-live.

### In the news
See news box. The AI-readiness and compliance drivers have made data migration programmes one of the main moments when companies actually invest in master data governance.

### Interview angle
> [!question] How it is asked
> "How would you ensure data quality in an SAP S/4HANA migration?"

> [!tip] Strong answer includes
> - Profile and cleanse before migration; scope only active data
> - Business owners for each domain, with sign-off
> - Mock loads with quality gates and reconciliation reports
> - Central creation workflow (MDG or equivalent) post go-live
> - KPIs: error rate by load, duplicates removed, post-go-live exceptions

---
## 14. ⭐ Advanced: Data Governance for AI and Analytics
> ⭐ Advanced · _Added beyond the tracker_

### Definition
AI and machine-learning products add new data-quality concerns ([[094 ML Fundamentals & Workflow]], [[220 Responsible AI, Explainability & Model Governance]]):
- **Representativeness and bias:** training data must reflect the operating conditions (all regions, seasons, customer segments).
- **Label quality:** wrong labels (for example mis-coded demand history or stock-outs recorded as zero demand) mislead forecasting models ([[218 Forecasting with ML & Foundation Models]]).
- **Drift and freshness:** inputs change; monitor distribution shift and latency.
- **Lineage and reproducibility:** be able to say which data version trained which model.
- **Privacy and consent:** personal data used for modelling needs a lawful basis, minimisation and, where required, anonymisation.
- **Unstructured data (documents, emails) for LLM applications:** retrieval quality depends on clean, current, permissioned content ([[219 NLP, Embeddings & LLM Applications for Analysts]]).

**AI-ready data** means: fit for the use case, documented (metadata and lineage), monitored (tests for quality and drift) and governed (access, ethics, compliance). A pragmatic order of work: pick a use case, define the data requirements, assess gaps, fix the top few quality issues, then scale.

### Example
A demand-forecasting model trained on three years of sales shows poor accuracy for 15% of SKUs. Investigation finds that stock-out days were recorded as zero sales, teaching the model that demand is low when product was simply unavailable. Remedy: flag stock-out periods using inventory snapshots, treat those days as censored (or impute using in-stock demand), retrain, and add a data test that checks for runs of zero sales alongside zero stock. Forecast accuracy for the affected SKUs improves because the label now represents demand, not sales.

### In the news
See news box. Gartner's 60% abandonment prediction concerns precisely these data readiness gaps, not algorithms.

### Interview angle
> [!question] How it is asked
> "A data scientist says the demand model is underperforming. What data checks would you run before changing the algorithm?"

> [!tip] Strong answer includes
> - Check target definition (sales vs true demand), stock-outs, promotions, outliers, missing dates
> - Data splits, leakage, drift and freshness
> - Lineage: which source tables feed features and who owns them
> - Monitoring and tests as part of the pipeline
> - Governance and privacy review for personal data
