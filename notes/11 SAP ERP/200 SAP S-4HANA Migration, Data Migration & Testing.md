---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP S-4HANA Migration, Data Migration & Testing"
tier: Tier 2
roles: Consulting / Operations
status: complete
subtopics: 14
---
# SAP S-4HANA Migration, Data Migration & Testing

⬅ [[199 SAP Ariba, SRM & Business Network]] · [[_Index - SAP ERP|SAP ERP]] · [[201 SAP Landscape, Transports, Security & GRC Basics]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Consulting / Operations

## Sub-topics in this note
1. [[#1. Why Migrate: ECC Deadlines and What S/4HANA Changes]]
2. [[#2. Migration Paths: Greenfield, Brownfield, Bluefield]]
3. [[#3. SAP Activate and Programme Phases]]
4. [[#4. SAP Readiness Check and Scoping]]
5. [[#5. Simplification List and Custom Code Remediation]]
6. [[#6. Technical Conversion: Maintenance Planner, SUM and DMO]]
7. [[#7. Data Migration: Migration Cockpit, Staging Tables and Direct Transfer]]
8. [[#8. Data Cleansing, Mapping and Reconciliation]]
9. [[#9. Cutover Plan, Rehearsals and Go/No-Go]]
10. [[#10. Testing Strategy: Unit, Integration, UAT, Regression]]
11. [[#11. Hypercare and Stabilisation]]
12. [[#12. Change Management, Training and Adoption]]
13. [[#13. Business Case, Risks and the Consulting Case Angle]]
14. [[#14. ⭐ Advanced: Clean Core, RISE vs GROW, and Cloud Editions]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): The ECC deadline turns S/4HANA migration into a dated programme
> **SAP creates a paid bridge beyond 2030 (announced 4 Feb 2025).** SAP introduced the "SAP ERP, private edition, transition option": available to buy from **2028**, usable **2031–2033**, aimed at large, complex ECC estates, and only on SAP HANA. SAP states it is an additional, non-mandatory offering and **not a maintenance prolongation**: customers who finish by end-2030 do not need it, and on-premise ECC still ends extended maintenance in 2030. ([SAP News Center](https://news.sap.com/2025/02/sap-erp-private-edition-transition-option-navigate-complex-rise-with-sap-transformations/); trade-press view in [e3mag, 23 Oct 2025](https://e3mag.com/en/deadline-extension-for-ecc-6-0-until-2033/), which also records the standard dates: mainstream maintenance to end-2027, chargeable extended maintenance to end-2030 at a two-percentage-point surcharge.)
>
> **Progress is slower than the calendar (Basis Technologies model, 30 Jun 2024).** Using SAP and Gartner data, the author estimated that only about **28%** of the original ~35,000 ECC customers were live on S/4HANA at end-2023, with a projection of about **57% by end-2027** and roughly **80% by end-2030**, and a peak resource crunch 3–4 years out. These are modelled estimates, not audited counts. ([Basis Technologies](https://www.basistechnologies.com/blog/the-true-state-of-s4hana/))
>
> **Three real routes, three real firms (Computer Weekly, 6 Jan 2026).** Twinings Ovaltine ran a near-vanilla greenfield on RISE (two customisations in the whole environment); retailer QD Group did a like-for-like brownfield "on time, on budget, no incidents"; Imperial Brands used a selective (bluefield) route to consolidate about 50 legacy ERP systems into one S/4HANA instance, and its data lead noted that data ownership is hard without a data culture. ([Computer Weekly](https://www.computerweekly.com/news/366636765/S4Hana-in-2026-Three-ways-to-move-off-SAP-ECC))
>
> **Old data-loading tool is gone (SAP documentation, via KeyUserTraining).** The LTMC migration cockpit is deprecated since S/4HANA 2020 and read-only since 2021; the Fiori app "Migrate Your Data" replaces it, and old LTMC projects cannot be imported. ([KeyUserTraining](https://keyusertraining.com/en/sap-ltmc-legacy-transfer-migration-cockpit/); secondary source for SAP's deprecation notice)
>
> Sub-topics that say **"See news box"** reuse these items. Module background: [[079 SAP Fundamentals & Architecture]].

---
## 1. Why Migrate: ECC Deadlines and What S/4HANA Changes
> 🟠 Tier 2 · _Key points:_ 2027 mainstream / 2030 extended, HANA-only, simplified data model, Fiori

### Definition
**SAP ECC 6.0** (the SAP ERP 6.0 core, enhancement packs 0–8) is the 2006-vintage ERP most Indian manufacturers still run. **S/4HANA** is the rewrite of the ERP core for the in-memory SAP HANA database. Dates to quote (checked against SAP and trade press, Oct 2026): **mainstream maintenance ends 31 Dec 2027; extended maintenance (chargeable) ends 31 Dec 2030**; the 2031–2033 transition option is a paid cloud subscription, not an extension.

What actually changes in the data model and applications (the content of the "Simplification List"):

| Area | ECC | S/4HANA |
|---|---|---|
| Accounting | BSEG, BKPF plus separate CO and ML tables | **Universal Journal ACDOCA**: one line-item table for FI, CO, asset accounting and material ledger |
| Material documents | MKPF header + MSEG items, aggregate tables MARD/MBEW updated | **MATDOC** one table; stock computed on the fly; old tables become compatibility views |
| Customers and vendors | KNA1/LFA1 maintained with XD01/XK01 | **Business Partner (BP)** is the single master; CVI keeps old tables in sync |
| MRP | MD01 batch run | **MRP Live** (MD01N) runs in HANA, much faster |
| Material number | 18 characters | up to **40 characters** (optional extended length) |
| Credit management | FI-AR credit | SAP Credit Management (FSCM) |
| UI | SAP GUI | **Fiori launchpad** (SAP GUI still available) |
| Analytics | BW extracts | embedded analytics on live data |

Why the business cares: end of vendor patches and legal updates (GST and e-invoicing changes arrive as SAP notes only for supported releases), a shrinking ECC talent pool, and HANA-only innovation (AI, Fiori, real-time).

### Example
Today is 3 Oct 2026. Months left to the standard dates: to 31 Dec 2027 ≈ **15 months**; to 31 Dec 2030 ≈ **51 months**. A mid-size manufacturer's brownfield programme typically takes 12–24 months from kick-off, so a firm that has not started is already inside the window where mainstream maintenance may lapse before go-live; from 2028 it would pay the extended-maintenance surcharge on its maintenance base (two percentage points per the trade-press report above, so a 22% fee becomes 24%).

### In the news
See news box. The Basis Technologies projection that only ~57% of ECC customers will be live by end-2027 is why advisory firms are busy: demand for consultants peaks before the deadline.

### Interview angle
> [!question] How it is asked
> "A client says ECC works fine, so why spend ₹80 crore moving to S/4HANA?"

> [!tip] Strong answer includes
> - Dates stated precisely (2027 mainstream, 2030 extended, 2033 only via the paid private-edition option)
> - Cost of staying: surcharge, no innovation, rising support risk, compliance patches
> - Cost of waiting: resource crunch, rushed project, higher mistake risk
> - Concrete benefits tied to the client's pain (close time, MRP runtime, single BP master), not generic "digital"

---
## 2. Migration Paths: Greenfield, Brownfield, Bluefield
> 🟠 Tier 2 · _Key points:_ New implementation vs system conversion vs selective data transition

### Definition
- **Greenfield (new implementation):** install a fresh S/4HANA system, redesign processes to SAP best practice, and **load only chosen master data and open items** with the migration cockpit. The old system is archived or kept read-only.
- **Brownfield (system conversion):** convert the **existing ECC system in place** using Software Update Manager (SUM) with the Database Migration Option (DMO) when the database is not yet HANA. All configuration, custom code and history come along.
- **Bluefield (selective data transition):** a hybrid, usually tool-based (SNP, Datavard and similar partners, or SAP's own selective transition services) that builds a new system but **brings selected company codes, plants, or time slices of history**, or merges several ECC systems into one. A "shell conversion" converts a copy of the system with data removed, then loads the chosen data.

| Criterion | Greenfield | Brownfield | Bluefield |
|---|---|---|---|
| Process redesign | Full | Minimal | Targeted |
| Custom code | Rebuilt or dropped | Carried, must be remediated | Selected |
| History | Only what is loaded | All | Chosen scope |
| Duration | Longest | Shortest | Medium |
| Business disruption | High (change) | Low | Medium |
| Typical fit | Heavily customised, M&A, process reset | Stable, standard, deadline-driven | Carve-outs, consolidation of many ERPs |

### Example
Weighted scoring for a client (weights out of 100: process redesign need 25, customisation level 20, history need 15, time and cost 25, disruption tolerance 15; scores 1–5, higher means better fit):
- Greenfield: 5, 5, 2, 2, 2 gives (125 + 100 + 30 + 50 + 30)/100 = **3.35**
- Brownfield: 2, 2, 5, 5, 4 gives (50 + 40 + 75 + 125 + 60)/100 = **3.50**
- Bluefield: 4, 4, 4, 3, 3 gives (100 + 80 + 60 + 75 + 45)/100 = **3.60**

The totals are close, so the real answer is to test the weights with the client. A firm that merges three ERPs after an acquisition scores "process redesign" higher and the ranking flips towards greenfield or bluefield.

### In the news
See news box. Computer Weekly's three cases map one-to-one onto the three paths: Twinings (greenfield), QD Group (brownfield), Imperial Brands (bluefield, about 50 ERPs into one).

### Interview angle
> [!question] How it is asked
> "Greenfield or brownfield for a 30-year-old Indian auto-component maker with 5,000 custom objects?"

> [!tip] Strong answer includes
> - Decision criteria stated first (customisation, data history, time, appetite for change, number of ERPs)
> - Honest trade-offs: brownfield carries technical debt; greenfield loses history and needs strong change management
> - Mention bluefield for consolidation or carve-out
> - A recommendation plus what would change it (for example, process mining showing 70% non-standard variants, see [[173 Process Mining & Operations Intelligence]])

---
## 3. SAP Activate and Programme Phases
> 🟠 Tier 2 · _Key points:_ Discover, Prepare, Explore, Realize, Deploy, Run; fit-to-standard

### Definition
**SAP Activate** is SAP's implementation methodology: agile delivery inside a phase-gate structure, applied to new implementations and conversions. Six phases:
1. **Discover:** value case, scope, choose cloud edition or on-premise, trial system.
2. **Prepare:** project charter, team, governance, system provisioning, **Readiness Check** for conversions.
3. **Explore:** **fit-to-standard workshops** on a pre-configured best-practice system; output is a backlog of gaps (configuration, extension, process change).
4. **Realize:** iterative build and test in sprints; data migration mock loads; integration build.
5. **Deploy:** final testing, cutover rehearsals, training, go-live, **hypercare**.
6. **Run:** steady-state support, continuous improvement, quarterly cloud releases.

Fit-to-standard replaces the older "blueprint" document: instead of asking users what they want, show the standard process and record only deviations. It ties to project governance in [[038 PMBOK Knowledge Areas]] and iterative delivery in [[032 Agile & Scrum Framework]].

### Example
A 14-month brownfield for an Indian pharma company: Discover and Prepare 2 months (Readiness Check, scoping), Explore 2 months (fit-to-standard on finance, MM, QM, batch management), Realize 6 months (custom code remediation, three data mocks, regression build), Deploy 3 months (two cutover rehearsals, UAT, training), then a further month of hypercare reported separately. Fiscal year-end (31 March) is usually avoided as a go-live window, so the plan works back from a go-live in April–June or another quiet period.

### In the news
See news box. With the 2027 deadline close, programme offices compress Explore by using pre-configured best-practice content rather than writing custom blueprints.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would structure a 12-month S/4HANA conversion."

> [!tip] Strong answer includes
> - The six phases with the key deliverable and quality gate of each
> - Fit-to-standard as the scoping method
> - Calendar logic: avoid year-end close and festival peaks; plan mocks and rehearsals before go-live
> - Governance: steering committee, business process owners, data owners named early

---
## 4. SAP Readiness Check and Scoping
> 🟠 Tier 2 · _Key points:_ Cloud-based analysis of ECC; simplification items, custom code, add-ons, sizing, Fiori

### Definition
**SAP Readiness Check for SAP S/4HANA** is a self-service analysis run on your productive (or a copy of) ECC system. Data is collected by a small program, uploaded to SAP, and a dashboard returns findings:
- **Simplification items:** which of the hundreds of simplification-list entries apply to your system, with relevance (for example, "you use SD credit management, which is replaced").
- **Custom code analysis:** how much of your Z code touches changed or removed objects (ABAP Test Cockpit based).
- **Add-on compatibility:** which partner or SAP add-ons are supported on the target release.
- **Sizing:** estimated HANA memory and disk based on current data volumes.
- **Recommended Fiori apps** based on transaction usage.
- **Business functions, data volume management, integration** (interfaces, RFCs) and **Business Process Discovery** (which processes are actually used).

Distinguish it from the technical **Simplification Item Check** (framework in SAP Note 2399707), which runs inside the system and must be run in client 000 as part of the SUM pre-checks. The Readiness Check is for **scoping and budgeting**; the Simplification Item Check is a **blocking technical gate** before conversion.

### Example
For a ₹3,500 crore auto-parts maker the Readiness Check reports (illustrative figures): 112 relevant simplification items (of which 14 need business action such as Business Partner conversion), 4,000 custom objects, 6 add-ons (2 unsupported), HANA sizing 1.2 TB. The programme manager converts these into a work breakdown: 14 business-action items become epics with owners, 2 add-ons become a vendor-upgrade workstream, and the custom code number feeds the next sub-topic.

### In the news
See news box. As adoption reaches the late majority, scoping discipline matters more than technology: late movers can learn from the roughly 28% who were live by end-2023.

### Interview angle
> [!question] How it is asked
> "What do you do in the first four weeks of an S/4HANA conversion?"

> [!tip] Strong answer includes
> - Readiness Check output and how each section becomes a workstream
> - Difference between Readiness Check (planning) and Simplification Item Check (technical gate)
> - Stakeholder interviews to confirm which processes are really used
> - Outcome: scope, effort estimate, risk list, go/no-go for the path decision

---
## 5. Simplification List and Custom Code Remediation
> 🟠 Tier 2 · _Key points:_ ABAP Test Cockpit, usage data (SCMON/UPL), delete unused, clean core

### Definition
The **Simplification List** (published per release) states, by functional area, what was removed, replaced, or changed and what the customer must do (for example, "MRP: classic MRP tables changed, MRP Live is used", "Credit management replaced", "Customer/vendor replaced by Business Partner"). The **Simplification Item Catalog** tool lets you filter by relevance.

**Custom code** (Z/Y programs, enhancements, user exits, custom tables) is the largest source of effort in a brownfield. Process:
1. **Collect usage:** switch on the ABAP Call Monitor (SCMON) and/or Usage Procedure Logging (UPL) in production for 3–12 months to see which objects actually run.
2. **Delete the unused** before analysis: typically a third or more of custom code.
3. **Run ABAP Test Cockpit (ATC) with the S/4HANA readiness checks** (via a central check system) to find syntax and semantic incompatibilities.
4. **Fix:** automatic quick fixes where available; manual adaptation for the rest; **replace with standard** where S/4HANA now covers the need.
5. **Re-home extensions** to clean-core options: in-app (key-user) extensibility, developer extensibility, or side-by-side on SAP BTP.

Typical findings: direct reads on removed tables (for example MKPF/MSEG), `SELECT *` on changed tables, sorting assumptions that HANA no longer guarantees, and use of obsolete function modules.

### Example
4,000 custom objects. SCMON shows 35% unused (1,400), leaving 2,600 used. ATC flags 20% of those for change: 520 objects. At 0.75 person-day each: 390 person-days; at an assumed blended rate of ₹25,000 per day the effort is **₹97.5 lakh** (390 × 25,000 = 97,50,000), before testing. Deleting the unused 1,400 saved analysis and testing of 35% of the estate.

### In the news
See news box. SAP's clean-core message is why the Readiness Check's custom-code section is treated as a design decision, not a clean-up chore.

### Interview angle
> [!question] How it is asked
> "The client has 8,000 custom programs. How do you size and de-risk the custom code work?"

> [!tip] Strong answer includes
> - Usage data before analysis; delete unused first
> - ATC findings categorised (auto-fix, manual, replace by standard)
> - Test effort follows changed objects, so risk-based regression
> - Governance: freeze on new Z development during the project, extension policy for the future

---
## 6. Technical Conversion: Maintenance Planner, SUM and DMO
> 🟠 Tier 2 · _Key points:_ Stack XML, SUM with DMO, shadow instance, uptime vs downtime, rollback

### Definition
Brownfield mechanics:
- **Maintenance Planner** (a cloud tool) validates the target release, checks add-on and product-version compatibility and produces the **stack file** (`stack.xml`) with the downloads.
- **Software Update Manager (SUM)** performs the conversion: it applies the new software, converts data (for example into the MATDOC and ACDOCA structures), and runs the pre-checks, including the simplification item check.
- **DMO (Database Migration Option) of SUM** combines the **database migration to HANA** with the **software conversion in one run and one downtime**. The source database stays consistent, so a **rollback** by re-activating the source is possible until the cutover point.
- During **uptime**, SUM builds a **shadow instance** to prepare the new repository while users keep working; during **downtime** the system moves to HANA, application data is migrated and converted, and remaining post-processing runs.
- Options to cut downtime: **downtime-optimised conversion (DoC)**, **near-zero downtime maintenance (nZDM)**, and parallel data transfer. **DMOVE2S4** is DMO combined with a system move, for example to a hyperscaler or RISE environment.
- Two-step alternative: first migrate the database to HANA (Suite on HANA), then convert. One step is the default recommendation.

### Example
Downtime budget (illustrative assumptions, not benchmarks): after archiving the database shrinks from 6.0 TB to 4.5 TB; measured transfer of 750 GB/hour gives 4,500 / 750 = **6 hours**; software and data conversion 3 hours; post-processing and smoke test 2 hours. Total **11 hours**, so a Saturday 8 pm to Sunday 7 am window fits. If the same migration ran at 400 GB/hour, transfer alone would take 11.25 hours, which breaks the window and triggers a downtime-optimised approach or more parallel processes.

### In the news
See news box. Because the transition option applies only to HANA systems, a Suite-on-HANA first step is no longer just a technical stepping-stone but also a prerequisite for that bridge.

### Interview angle
> [!question] How it is asked
> "How do you keep production downtime for a conversion within a weekend?"

> [!tip] Strong answer includes
> - SUM/DMO one-step logic, shadow instance, uptime vs downtime
> - Data volume reduction and archiving before conversion
> - Multiple technical rehearsals with timed runs on a production-size copy
> - Rollback plan and the point after which rollback is no longer possible

---
## 7. Data Migration: Migration Cockpit, Staging Tables and Direct Transfer
> 🟠 Tier 2 · _Key points:_ "Migrate Your Data" app, migration objects, files vs staging vs direct transfer

### Definition
In greenfield and bluefield the data is **loaded**, not converted. SAP's tool is the **SAP S/4HANA migration cockpit**, now the Fiori app **Migrate Your Data**. It works with **migration objects** (predefined business objects such as Material, Business Partner, Open Purchase Order, Fixed Asset, Open AP items) that know the target APIs and the mandatory fields.
- **Staging tables approach:** source data is prepared (spreadsheet templates or ETL) into **staging tables** created by the cockpit; the cockpit then validates, converts values (mapping), simulates and posts. Files are now simply one way of filling staging tables.
- **Direct transfer approach:** the cockpit reads **directly from the source SAP system** (ECC) over an RFC connection, selecting data per object, mapping values, then posting. It fits SAP-to-SAP migration without extract files; later releases allow staging tables as intermediate storage for adjustment (per the KeyUserTraining summary of SAP documentation).
- **LTMC** (the older cockpit) is deprecated; the **Legacy System Migration Workbench (LSMW)** is not recommended for S/4HANA objects because it can bypass the new data model checks.
- Steps in the app: create project, select objects, fill or select source, **map values** (for example old plant codes to new), **simulate**, **migrate**, review messages, correct, repeat.
- Large or complex loads often use **SAP Data Services** or third-party ETL tools; custom migration objects can be added.

### Example
Loading customers as Business Partners from ECC with direct transfer: select the Business Partner (Customer) object, filter company code 1000 and customers active in the last 24 months, map payment terms, simulate (3,200 records; 41 errors, mostly missing tax numbers), fix in the source, simulate again with 0 errors, then migrate. The same cycle is repeated for each mock load so the final cutover load is a known quantity.

### In the news
See news box: LTMC projects cannot be imported into Migrate Your Data, so any plan that relied on old LTMC templates must be rebuilt.

### Interview angle
> [!question] How it is asked
> "Which tool and approach would you use to load open purchase orders and why?"

> [!tip] Strong answer includes
> - Migration cockpit with the right migration object, not LSMW
> - Staging tables vs direct transfer with the reason (non-SAP source vs SAP source)
> - Simulate before migrate, repeated mocks, error loop with business owners
> - Open items only (not full history) and reconciliation after load

---
## 8. Data Cleansing, Mapping and Reconciliation
> 🟠 Tier 2 · _Key points:_ Scope/archive, deduplicate, mapping tables, control totals, owner sign-off

### Definition
Poor data is a leading cause of slipped go-lives. The data workstream has five jobs:
1. **Scope:** what to migrate. Rules such as "materials with a movement in the last 24 months or open stock", "vendors with transactions in 3 years", "open items only for FI". Everything else is archived or left in the legacy system.
2. **Cleanse:** remove duplicates, fix addresses, GSTIN and PAN formats, units of measure, obsolete materials; validate bank details.
3. **Map:** value mapping tables (old to new) for plant, material group, payment terms, GL accounts; **key mapping** for IDs that change (for example vendor 100245 becomes BP 1000245).
4. **Load and reconcile:** compare counts and control totals before and after: number of records, sum of stock value, sum of open AP/AR, sum of GL balances per account.
5. **Own:** each object has a business data owner who signs off each mock; see governance ideas in [[175 Data Quality, Master Data & Data Governance]].

India-specific checks: GSTIN validity per state, PAN against vendor type for TDS, HSN/SAC codes on materials and services, e-way bill and e-invoice master data, MSME vendor flag for payment timelines. Finance reconciliation logic is in [[190 SAP FI-CO Essentials for Operations Professionals]].

### Example
Vendor master of 48,000 records: duplicate detection finds 6.5% = **3,120** duplicates; after merge **44,880** remain. Material master of 1,25,000: 30% have had no movement for 3 years (37,500), so **87,500** are migrated. Load success across three mock loads of those 87,500 materials: mock 1 at 91.2% (79,800 loaded, 7,700 errors), mock 2 at 96.8% (84,700 loaded, 2,800 errors), mock 3 at 99.6% (87,150 loaded, 350 errors). The target for the dress rehearsal is zero unexplained errors and 100% reconciliation of stock value to FI.

### In the news
See news box. Imperial Brands' data lead says data ownership is difficult without a data culture; the practical answer is to name business owners and measure quality per mock.

### Interview angle
> [!question] How it is asked
> "How do you make sure the data loaded into S/4HANA is correct?"

> [!tip] Strong answer includes
> - Scope rules to reduce volume, then cleansing with named owners
> - Mapping tables under change control
> - Control totals and sample-based business validation at each mock
> - Error trend across mock loads as a go-live gate (for example under 0.5% unexplained)

---
## 9. Cutover Plan, Rehearsals and Go/No-Go
> 🟠 Tier 2 · _Key points:_ Runbook, critical path, mock cutovers, freeze, rollback, go/no-go

### Definition
**Cutover** is the controlled transition from the old system to the new one. The **cutover plan (runbook)** lists every task with owner, duration, predecessor, time slot and a check. Components:
- **Freeze rules:** transport freeze, master data freeze, period-end timing.
- **Technical tasks:** final backup, SUM downtime (brownfield), interface switch, user and authorisation checks.
- **Data tasks:** delta master data, open items, stock quantities (physical count aligned), balance carry-forward.
- **Business tasks:** stop postings, close open documents, communicate to customers and vendors.
- **Verification and Go/No-Go:** reconciliation, smoke tests, a formal decision with criteria, and a **rollback plan** with a stated point of no return.
- **Rehearsals:** at least one full **dress rehearsal** (timed, on production-sized data) plus earlier technical mocks; each updates the runbook with real durations.

### Example
Runbook tasks (hours): Freeze 2, Final backup 1, SUM downtime 11, Interface switch 3, Master data delta 6 (starts after freeze), Open items 5, Reconciliation 4 (needs both open items and interfaces), Smoke test 3, Go/No-Go 1. Earliest finish times: backup 3, SUM 14, interfaces 17, delta 8, open items 13, reconciliation 21, smoke test 24, decision **25 hours**. The critical path is Freeze, Backup, SUM, Interfaces, Reconciliation, Smoke test, Go/No-Go. Shortening master-data loads does nothing; shortening SUM or interface switching shortens the window. See [[039 Scheduling Tools (CPM-PERT-Gantt)]].

### In the news
See news box. QD Group's "no incidents" brownfield is the type of outcome rehearsed cutovers aim at.

### Interview angle
> [!question] How it is asked
> "What goes into a cutover plan and how do you decide to go live?"

> [!tip] Strong answer includes
> - Runbook structure with owners, durations, dependencies, critical path
> - Number of rehearsals and what each proves
> - Explicit go/no-go criteria (open P1/P2 defects, data reconciliation, user readiness)
> - Rollback criteria and the last safe rollback point

---
## 10. Testing Strategy: Unit, Integration, UAT, Regression
> 🟠 Tier 2 · _Key points:_ Test layers, entry/exit criteria, regression automation, data and performance tests

### Definition
| Layer | Purpose | Who | Typical scope |
|---|---|---|---|
| Unit test | One function or configuration works | Consultant | Single transaction or custom object |
| String or scenario test | A chain within a module | Consultant plus key user | Create PR, PO, GR |
| Integration test (SIT) | Cross-module and cross-system end to end | Cross-functional team | Order-to-cash with FI, interfaces to GST portal, banks, WMS |
| User acceptance test (UAT) | Business confirms it meets need | Key users, process owners | Real scenarios, signed off |
| Regression test | Existing processes still work after change | Test team, automation | Core flows after each transport or release |
| Data migration test | Loaded data is complete and correct | Data owners | Reconciliations per mock |
| Performance and security | Speed and authorisation | Basis, security | Batch runtimes (MRP, billing), role tests |
| Cutover or dress-rehearsal test | The plan works | All | Timed |

Controls: **test strategy and plan**, **entry and exit criteria**, **defect severity** (P1 blocker to P4 cosmetic), **traceability** (requirement to test case to defect), and **test automation** for regression (tools such as SAP Solution Manager or Cloud ALM test suites, Tricentis, Worksoft). In conversions, test effort is **risk-based**: weight it to processes touched by simplification items and changed custom code. Cloud ERP also needs regression each quarterly release. Security and authorisation testing links to [[201 SAP Landscape, Transports, Security & GRC Basics]].

### Example
2,400 planned test cases; 2,280 executed (95%); 95% of executed pass = **2,166 passed** (90.25% of planned), 114 failed. Exit criteria: 100% of P1 and P2 cases executed, zero open P1, at most 5 open P2 with workaround, 95% pass rate on critical business scenarios. With 114 failures including 2 P1, the cycle cannot exit; a fix-and-retest cycle follows, and go-live readiness is reviewed after it.

### In the news
See news box. As companies rush before 2027, compressed test windows are a recurring cause of defects in the first weeks after go-live (a practitioner pattern, not a figure from the sources above).

### Interview angle
> [!question] How it is asked
> "How would you design the test strategy for an S/4HANA conversion with limited time?"

> [!tip] Strong answer includes
> - Layered strategy and who owns each layer
> - Risk-based regression focused on changed objects and revenue-critical flows
> - Automation for repeatable regression
> - Defect triage rules and measurable exit criteria, plus test data and environment readiness

---
## 11. Hypercare and Stabilisation
> 🟠 Tier 2 · _Key points:_ 4–8 weeks, war room, ticket burn-down, exit criteria, transition to AMS

### Definition
**Hypercare** is the intensive post-go-live support period (commonly 4 to 8 weeks, longer if a period-end close falls inside) in which the project team, not the regular support desk, fixes issues quickly. Elements:
- **War room** and a daily stand-up with business leads, functional and technical teams.
- **Ticket triage** with severity targets (for example P1 response 30 minutes, fix or workaround 4 hours).
- **Floor-walkers or super-users** at plants and finance teams.
- **Monitoring** of batch jobs (MRP, billing, interfaces), postings, and the first financial close.
- **KPIs:** open tickets by severity, ageing, first-time-right, order-to-invoice cycle, stock accuracy, payment run success, user adoption.
- **Exit criteria:** no open P1/P2, backlog under agreed size, stable for two consecutive weeks, first month-end close completed, knowledge transferred to the **application management services (AMS)** team.

### Example
Week 1 after go-live: 420 tickets raised, 38 P1/P2. Week 4: 60 new tickets per week, 0 P1, 3 P2 with workarounds, GST return preparation completed on time. The steering committee approves exit at week 6 after the first month-end close and hands over to AMS with a known-issue list (illustrative numbers).

### In the news
See news box. Twinings' near-vanilla design (two customisations) is a design choice that shortens hypercare because there is less to break.

### Interview angle
> [!question] How it is asked
> "The go-live happened but invoicing is delayed. What do you do in the first week?"

> [!tip] Strong answer includes
> - Triage by business impact (cash and compliance first: invoicing, e-invoice, payments)
> - War room, clear owner per issue, daily communication to leadership
> - Temporary workarounds with a plan to retire manual steps
> - Root-cause fix into the regression suite; exit criteria and handover to AMS

---
## 12. Change Management, Training and Adoption
> 🟠 Tier 2 · _Key points:_ Stakeholder map, ADKAR, super-users, training before UAT, adoption metrics

### Definition
Technology rarely fails first; adoption does. Change management in an ERP programme includes:
- **Stakeholder and impact analysis:** who loses an Excel, a manual approval, a local report; role-by-role impact.
- **Communication plan:** sponsor messages, town halls, plant visits.
- **Training:** role-based, hands-on in a training client; a **super-user** network (one per 30–50 users is a common rule of thumb); train before UAT and again close to go-live; Fiori launchpad and new tile layouts matter.
- **Readiness surveys** and a formal **readiness gate** before go-live.
- **Models:** **ADKAR** (Awareness, Desire, Knowledge, Ability, Reinforcement) or Kotter. See [[040 Risk & Stakeholder Management]].
- **Adoption metrics:** login and transaction counts, shadow-Excel use, ticket types ("how do I" tickets signal training gaps).
- **Process ownership and data ownership** assigned to named line managers.

### Example
A plant of 600 users: at 1 super-user per 40, **15 super-users** are trained first. Training attendance target is 95% before go-live; actual is 91% at T-2 weeks, so a catch-up batch is scheduled and go-live is conditional on reaching 95%. After go-live "how-to" tickets fall from 45% to 15% of volume in six weeks, read as adoption improving (illustrative).

### In the news
See news box. Imperial Brands' remark on data culture is a change-management finding: ownership and behaviour decide data quality.

### Interview angle
> [!question] How it is asked
> "Users are resisting the new system. How do you handle it?"

> [!tip] Strong answer includes
> - Diagnose why: capability, motivation, or process change (ADKAR gaps)
> - Super-users and line-manager sponsorship, not only classroom training
> - Visible quick wins and listening mechanisms
> - Metrics for adoption and a go-live readiness gate

---
## 13. Business Case, Risks and the Consulting Case Angle
> 🟠 Tier 2 · _Key points:_ NPV of migration, cost drivers, top risks, structured case answer

### Definition
**Cost drivers:** licences or subscription (RISE bundles infrastructure and software), implementation services (typically the largest line), custom code remediation, data migration, testing, training, internal backfill, contingency (10–20%). **Benefits:** lower IT run cost (decommissioning, archiving), faster close, working capital from better planning, compliance, and the avoided extended-maintenance surcharge. Evaluate with NPV and payback ([[109 Valuation Basics (NPV, IRR, DCF)]], [[042 Cost & Budget Management]]).

**Top risks:** scope creep; custom code and interface underestimation; poor data quality; insufficient business involvement; compressed testing; key-person dependency in a tight talent market; cutover failure at period end; adoption. Mitigate with the risk-register approach from [[040 Risk & Stakeholder Management]].

**Case structure (a good frame):** (1) objectives and constraints (deadline, budget, tolerance for change), (2) current-state assessment (Readiness Check, process mining), (3) options (greenfield, brownfield, bluefield, RISE vs on-premise), (4) business case, (5) roadmap with phases and risks, (6) governance and change plan. See [[024 Consulting Frameworks]] and [[026 Case Interview — Operations Cases]].

### Example
Seven-year cash flows in ₹ crore (year 0 to 6) at 11% discount. Brownfield: −45, −35, then +28 a year for 5 years gives **NPV = ₹16.7 crore**, IRR about 17.8%, cumulative cash turns positive in year 4. Greenfield: −80, −70, then +55 a year gives **NPV = ₹40.1 crore**, IRR about 19.7%, cumulative cash positive in year 4. Greenfield costs more up front but, if the process-redesign benefits are real, creates more value. The recommendation depends on whether the extra ₹27 crore a year of benefit is credible: test it with a sensitivity case (for example 60% of the forecast benefit) before choosing. All figures here are illustrative.

### In the news
See news box. The modelled progress rates (about 28% live at end-2023, a projected 57% by end-2027) support the argument for starting early rather than waiting for the deadline.

### Interview angle
> [!question] How it is asked
> "A mid-size Indian chemicals company has ECC, 2,000 users and a 2028 target. Advise them." (case)

> [!tip] Strong answer includes
> - Clarify scope, entities, data volumes, customisation, and any M&A plans
> - Option comparison with criteria and a recommendation
> - A rough business case with NPV and a sensitivity
> - Top five risks with mitigations, a phased timeline, and next steps (Readiness Check, steering committee)

---
## 14. ⭐ Advanced: Clean Core, RISE vs GROW, and Cloud Editions
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Clean core** means keeping the ERP standard and putting differentiation outside it (key-user extensions, side-by-side apps on SAP BTP, and APIs) so upgrades do not break custom code. SAP treats it as the design principle for its cloud ERP and for brownfield customers who want painless upgrades.

Deployment choices:
- **RISE with SAP** (from 2021): a subscription bundle (S/4HANA Cloud private edition, infrastructure, technical services, tools) that lets existing customers do **brownfield or greenfield** with high customisation freedom.
- **GROW with SAP** (public cloud): multi-tenant S/4HANA Cloud public edition with standardised best-practice processes, **greenfield only**, and limited modification; quarterly releases.
- **On-premise** S/4HANA: full control, own infrastructure and upgrade effort.
- **SAP Cloud ERP** is the newer branding of SAP's cloud suite (2025 per Wikipedia's SAP ERP page; confirm current product names with SAP when advising a client).

Trade-off: private edition keeps flexibility (and technical debt); public edition forces fit-to-standard discipline but minimises upgrade cost. A common compromise for large groups: public cloud for subsidiaries, private for the core manufacturer.

### Example
A group with a pharma plant (batch genealogy, heavily regulated) and three distribution subsidiaries chooses private cloud for the plant (needs validated, stable releases) and public cloud for the subsidiaries (standard order-to-cash and finance, onboarded one at a time), with intercompany integration through standard APIs. This is a design illustration, not a reported case.

### In the news
See news box. SAP's position that the transition option is not a maintenance extension underlines its message: the destination is RISE-style cloud ERP, not another on-premise decade.

### Interview angle
> [!question] How it is asked
> "What is clean core, and does it matter to a manufacturer with plant-specific processes?"

> [!tip] Strong answer includes
> - Definition and the reason: upgradeability and lower remediation cost
> - Options for extension that preserve the core (in-app, side-by-side)
> - Matching edition to process variability, regulatory validation and speed
> - Honest note: some industry-specific needs still require private-edition flexibility

Related notes: end-to-end ERP flows in [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]], procure-to-pay in [[080 SAP MM — Materials Management]], general ERP context in [[013 ERP & Enterprise Systems (SAP-Oracle)]], and reporting in [[085 SAP Reporting & Analytics]].
