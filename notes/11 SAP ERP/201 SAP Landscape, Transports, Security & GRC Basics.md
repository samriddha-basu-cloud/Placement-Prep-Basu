---
tags: [sap-erp, tier3]
area: SAP ERP
topic: "SAP Landscape, Transports, Security & GRC Basics"
tier: Tier 3
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP Landscape, Transports, Security & GRC Basics

⬅ [[200 SAP S-4HANA Migration, Data Migration & Testing]] · [[_Index - SAP ERP|SAP ERP]] · [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]] ➡

> **Area:** SAP ERP · **Priority:** 🟡 Tier 3 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. The Three-Tier Architecture and the DEV-QAS-PRD Landscape]]
2. [[#2. Clients: Client-Dependent vs Cross-Client Data]]
3. [[#3. Transport Management: Requests, Tasks and STMS]]
4. [[#4. Change Governance: ChaRM, Cloud ALM and gCTS]]
5. [[#5. Users, Roles and Profiles: SU01 and PFCG]]
6. [[#6. Authorisation Objects and How a Check Works]]
7. [[#7. Segregation of Duties (SoD) and Critical Access]]
8. [[#8. SAP GRC Access Control and Cloud Identity Access Governance]]
9. [[#9. Audit Trails: Change Documents, Table Logs, Security Audit Log]]
10. [[#10. BASIS Tasks Overview and the Monitoring T-codes]]
11. [[#11. Job Scheduling and Background Processing]]
12. [[#12. Performance Basics for Business Users]]
13. [[#13. SOX, ITGC and the India Control Framework]]
14. [[#14. ⭐ Advanced: What Business Users and Consultants Should Know]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Core ERP and NetWeaver security flaws make access, patching and change control board-level topics
> **Maximum-severity NetWeaver flaw exploited before disclosure (April 2025).** CVE-2025-31324 in SAP NetWeaver Visual Composer scored **CVSS 10.0**: a missing authorisation check in the Metadata Uploader let **unauthenticated** attackers upload files and run code. Rapid7 reported exploitation observed since **at least 27 Mar 2025**, ahead of public disclosure on **24 Apr 2025**, mainly against manufacturing companies, with webshells dropped on affected servers; all NetWeaver 7.xx versions were in scope. ([Rapid7](https://www.rapid7.com/blog/post/2025/04/28/etr-active-exploitation-of-sap-netweaver-visual-composer-cve-2025-31324/))
>
> **Monthly SAP Security Patch Day, September 2026.** A Pathlock summary of the 8 Sep 2026 patch day counts **33 security notes (19 new, 14 updated)**, **7 HotNews** (CVSS 9.0 or higher) of which **2 scored 10.0**, touching NetWeaver AS ABAP/Java kernels, Web Dispatcher, Commerce Cloud, BTP and S/4HANA finance components. (Vendor-blog tally; the notes themselves are on SAP's support portal.) ([Pathlock](https://pathlock.com/blog/sap-security-patch-day-september-2026/))
>
> **What SAP Access Control is designed to do (SAP Learning).** Access risk analysis with segregation-of-duties and critical-access checks, emergency (firefighter) access with logged actions, business role management, and self-service access requests with embedded risk analysis. ([SAP Learning](https://learning.sap.com/learning-journeys/exploring-the-fundamentals-of-sap-system-security/describing-sap-access-control))
>
> Sub-topics that say **"See news box"** reuse these items. Migration context for the landscape: [[200 SAP S-4HANA Migration, Data Migration & Testing]].

---
## 1. The Three-Tier Architecture and the DEV-QAS-PRD Landscape
> 🟡 Tier 3 · _Key points:_ Presentation, application, database; DEV, QAS (test), PRD; sandbox and training

### Definition
SAP runs as a **three-tier architecture**: **presentation** (SAP GUI, Fiori launchpad in a browser), **application servers** (ABAP work processes: dialog, background, update, enqueue, spool, gateway) and the **database** (SAP HANA for S/4HANA, older ECC could run on Oracle, DB2, SQL Server, MaxDB). Details in [[079 SAP Fundamentals & Architecture]].

A **system landscape** is the set of SAP systems a company runs so that change is built, tested and released safely. The classic **three-system landscape** is:
- **DEV** (development): configuration and ABAP development.
- **QAS** (quality assurance, test): integration and user acceptance testing with production-like data.
- **PRD** (production): live business; no direct changes.

Variations: a **sandbox (SBX)** for experiments, **training (TRN)** system or client, **two-system** landscapes for small firms (not recommended: no test buffer), **four-system** landscapes with a separate **pre-production/performance** or project track in parallel with a maintenance track so that urgent fixes and long projects do not collide. Each system has a **SID** (three-character system ID such as `DEV`, `QAS`, `PRD`), one or more **instances**, and each application server shares the **message server** and **enqueue server** of the central services instance.

### Example
A mid-size Pune auto-parts company runs ECC: DEV (SID ED1, clients 100 config, 200 unit test), QAS (EQ1, client 300 integration test and 400 UAT), PRD (EP1, client 500 live) and a separate sandbox. A new GST e-invoice change is built in ED1/100, tested in EQ1/300, accepted by finance in EQ1/400 and only then moved to EP1/500. A bug found in PRD is fixed in DEV and transported; it is never patched live.

### In the news
See news box. NetWeaver-level vulnerabilities such as CVE-2025-31324 sit below the business layer, which is why the technical landscape (internet-facing components, patch levels) is a governance topic and not only a Basis topic.

### Interview angle
> [!question] How it is asked
> "Why does SAP have DEV, QAS and PRD, and what would go wrong with only one system?"

> [!tip] Strong answer includes
> - Separation of build, test and live; risk of untested changes hitting live data
> - Role of each system and who may change what
> - Why a project track and a maintenance track may run in parallel
> - Audit relevance: change control evidence per system

---
## 2. Clients: Client-Dependent vs Cross-Client Data
> 🟡 Tier 3 · _Key points:_ Client = business unit in a system; SCC4; customising vs repository

### Definition
A **client** is a self-contained unit inside one SAP system, with its own master data, transaction data and user master. Logon is always to a **client** (three digits). Standard clients: **000** (SAP reference/ setup and maintenance client), **001** (a template copy of 000), **066** (EarlyWatch service client in older systems).

- **Client-dependent (client-specific)** data: most customising tables (plant, company code, pricing), master data, transaction data, user master, authorisation roles' assignments.
- **Cross-client (client-independent)** data: the **ABAP Repository** (programs, table definitions, dictionary objects), some customising (for example, global settings, clients table `T000`), system-wide parameters.

**SCC4** maintains client settings: **client role** (Production, Test, Customizing, Demo, Training/Education, SAP reference), **changes and transports for client-specific objects** ("automatic recording of changes", "changes without automatic recording", "no changes allowed"), **cross-client object changes** (allowed or not), and protection against client copy and comparison tools. Production clients are normally set to **no changes allowed** for customising and repository.

Client tools: **SCC4** settings, **SCCL** local client copy, **SCC9** remote client copy, **SCC8** client export, **SCC7** import post-processing, **SCC1** copy of specific transport requests between clients in the same system (for example, from the customising client to the test client), **SCC5** delete client.

### Example
Moving company-code settings (client-specific) from client 100 into client 300 in the same DEV system is done with SCC1 (transport request copy). A new ABAP report (cross-client) is visible in all clients of DEV the moment it is activated; but its variants and any customising it reads still differ per client.

### In the news
See news box. A cross-client change or a mis-set production client is exactly what ITGC auditors test: they check SCC4 settings in PRD as evidence that nobody can change live configuration.

### Interview angle
> [!question] How it is asked
> "What is a client in SAP and which data is client-dependent?"

> [!tip] Strong answer includes
> - Client as separation of business data and user master inside one system
> - Examples of client-dependent (master data, customising) vs cross-client (programs, dictionary)
> - SCC4 client role and change options; why PRD is locked
> - Typical use: one DEV with config client and unit-test client

---
## 3. Transport Management: Requests, Tasks and STMS
> 🟡 Tier 3 · _Key points:_ Workbench vs customising requests, release, import queue, return codes

### Definition
Changes made in DEV are recorded in **change requests** (also called transport requests) so they can be moved to QAS and PRD with the **Change and Transport System (CTS)**.
- **Workbench request** (type K): repository objects, cross-client (programs, dictionary objects, screens, enhancements). Created in SE09/SE10 or when you save an object.
- **Customizing request** (type W): client-specific configuration done in SPRO/SM30.
- A request has **tasks**, one per developer or configurator; **release the task first**, then the request. Request number format: `<SID>K9<nnnnn>` (example `DEVK900123`).
- **Transport of copies** and **relocation** requests are special types for moving objects without changing ownership.
- Objects in requests are listed in tables `E070` (header) and `E071` (objects); object directory in `TADIR`.

**STMS** (Transport Management System) configures and runs transports:
- **Transport domain** with a **domain controller**; **transport routes** with a **consolidation route** (DEV to QAS) and **delivery route** (QAS to PRD).
- Released requests land in the **import queue** of the target system; an administrator imports **all** requests or a **single** request (**import single** can break dependencies). Optional **QA approval** step before import into PRD.
- **Return codes** after import: **0** success, **4** warning (usually fine), **8** error (investigate), **12** severe error.
- Related T-codes: `SE09`/`SE10` transport organizer, `SE01` extended view, `SCC1` copy request between clients, `STMS_IMPORT` import queue.

### Example
A consultant adds a new "Q3 inspection type" in SPRO (customising request `DEVK900451`), a developer creates a Z-report (workbench request `DEVK900452`). The report depends on a new database field in request `DEVK900440`. If the team imports `...452` into QAS before `...440`, the import returns code 8 because the field does not exist: sequence and dependencies matter. Both are tested in QAS, approved and then imported into PRD in the same order during a change window.

### In the news
See news box. Controlled import into PRD with approvals and logs is the evidence that regulators and auditors expect for "authorised change".

### Interview angle
> [!question] How it is asked
> "What is the difference between a workbench and a customising request, and how does STMS move them?"

> [!tip] Strong answer includes
> - What each request type carries (cross-client repository vs client-specific customising)
> - Task, release, request sequence and the import queue
> - Consolidation vs delivery route; return codes 0/4/8/12
> - Dependency and sequence risk, plus approval before PRD

---
## 4. Change Governance: ChaRM, Cloud ALM and gCTS
> 🟡 Tier 3 · _Key points:_ Change request approval workflow, emergency changes, git-based CTS

### Definition
Plain STMS lets any authorised administrator import anything; mature organisations add a **change process** on top:
- **ChaRM (Change Request Management in SAP Solution Manager)**: a workflow with change document, approval, development, test, release, import to PRD, and a log. Types: normal change, urgent (hotfix) change, general change, administrative change.
- **SAP Cloud ALM**: the cloud-based application lifecycle tool aimed at RISE and cloud customers, with project, test and change management elements. (Check current product capability with SAP when advising.)
- **gCTS (git-enabled CTS)**: in S/4HANA, ABAP repository objects can be kept in git repositories with branches, giving version history across systems; used with CTS-based import mechanisms.
- **CTS+** moves non-ABAP content (for example Java or BTP artefacts) with the same transport route.
- **Process controls:** segregation of the developer from the person who imports into PRD, **emergency change procedure** with after-the-fact review, **transport freeze** around month-end, and **change documentation** linking each transport to a business ticket and test evidence.

### Example
A month-end issue breaks the GST report. Normal change takes two weeks, so the team raises an **urgent change**: fix in DEV, quick test in QAS with a copy of last month's data, release approved by the finance controller and IT head, imported into PRD by the Basis admin (not the developer), and a post-implementation review the next week. All steps are logged under a ticket number.

### In the news
See news box. A monthly patch day (second Tuesday) adds regular, scheduled change on top of project transports, so patching also needs a change window and rollback plan.

### Interview angle
> [!question] How it is asked
> "How would you control changes in a SAP landscape for audit purposes?"

> [!tip] Strong answer includes
> - Ticket-to-transport traceability; approvals; test evidence
> - Separation between developer and importer
> - Emergency change path with retrospective approval
> - Tools (ChaRM, Cloud ALM, gCTS) named as examples, not the heart of the answer

---
## 5. Users, Roles and Profiles: SU01 and PFCG
> 🟡 Tier 3 · _Key points:_ User types, single/composite/derived roles, profile generation

### Definition
- **User master (SU01):** user ID, name, password rules, validity dates, **user type** (A Dialog, B System, C Communication, L Reference, S Service), assigned roles, parameters, defaults (such as decimal format). Display `SU01D`, mass maintenance `SU10`. Locked users: `SU01` or `SU10`; logon table `USR02`.
- **Role (PFCG):** a collection of **menu entries** (transactions, reports, Fiori apps) and **authorisations**. Saving generates an **authorisation profile** that is assigned to users via the role (`AGR_USERS` table). User comparison (**Utilities > Mass comparison**) refreshes user buffers.
- **Single role:** one job function.
- **Composite role:** a bundle of single roles for a job position (for example "Purchasing Executive Pune").
- **Derived role:** inherits the menu and authorisation proposal from a **master role** but has **different organisational values** (plant, company code, purchasing org); used to scale one role design to many plants.
- **Reference users** share a base set of authorisations; **system/communication users** run interfaces and must not log on interactively.
- **Dangerous profiles:** `SAP_ALL` (all authorisations) and `SAP_NEW`; never assign to dialog users in production except as a logged emergency measure.

### Example
A role "MM_BUYER" includes menu ME21N, ME22N, ME23N, ME2N, MIGO display. The master role is built once. Derived roles "MM_BUYER_1100" (Pune plants and purchasing org 1000) and "MM_BUYER_1200" (Nashik plant) differ only in organisation values. A composite role "PURCHASING_EXEC" combines MM_BUYER_1100 with "MM_REPORTS_DISPLAY".

### In the news
See news box. The SAP Access Control capabilities (role design, access requests) are all built on the role objects described here.

### Interview angle
> [!question] How it is asked
> "What are single, composite and derived roles, and why use derived roles?"

> [!tip] Strong answer includes
> - Role as menu plus authorisations, generating a profile
> - Composite for job bundling; derived to vary organisational levels
> - User types and why system users are separate
> - Danger of SAP_ALL and need for periodic role clean-up

---
## 6. Authorisation Objects and How a Check Works
> 🟡 Tier 3 · _Key points:_ Object, fields, ACTVT, AND/OR logic, SU53, SU24, trace

### Definition
An **authorisation object** (class-grouped, display in `SU21`) is a template with up to ten **fields**; an **authorisation** is an instance with concrete field values stored in a role. Typical field **ACTVT** (activity): 01 create, 02 change, 03 display, 06 delete, 10 post, 16 execute. Examples: `S_TCODE` (start a transaction), `M_BEST_BSA` (PO document type), `M_BEST_EKO` (purchasing org), `M_BEST_WRK` (plant), `F_BKPF_BUK` (company code in FI posting), `S_TABU_DIS` (table maintenance by authorisation group).

**Check logic:** inside an authorisation, **all fields must pass (AND)**; across several authorisations of the same object, **any one may satisfy it (OR)**; a transaction usually triggers **several objects, all of which must pass (AND)**.

Troubleshooting for business users and admins:
- `SU53` shows the **last failed authorisation check** of the user: screenshot it to the security team.
- `SU24` maintains which objects are proposed for each transaction (check indicator and default values); `SU25` handles upgrade adjustment.
- `ST01` / `STAUTHTRACE` records authority checks while reproducing an issue; `SUIM` reports who has which authorisation or role; `SU56` shows the user buffer.

### Example
Meena tries `ME21N` for plant 1200 and gets "no authorisation". SU53 shows `M_BEST_WRK` with ACTVT 01 and WERKS 1200 missing; her role only contains WERKS 1100. The role owner adds 1200 via the derived role for Nashik after approval; no one lends her another ID. Time to resolution depends on a clear request process, not on technology.

### In the news
See news box. Missing-authorisation checks are also the vulnerability class in CVE-2025-31324 ("missing authorization check"), which shows why checks must be present in custom and standard code.

### Interview angle
> [!question] How it is asked
> "A user cannot post a goods receipt. How do you find out why and fix it?"

> [!tip] Strong answer includes
> - SU53 first, then trace if needed
> - AND/OR logic of fields and objects
> - Fix via role owner and approval, test in QAS, transport the role
> - Never share IDs or grant SAP_ALL as a shortcut

---
## 7. Segregation of Duties (SoD) and Critical Access
> 🟡 Tier 3 · _Key points:_ Conflicting functions, risk rules, mitigating controls

### Definition
**Segregation of duties** means no single person can complete a risky end-to-end transaction alone, which would allow error or fraud. In SAP, a **function** is a set of transactions/authorisations (for example "Create Vendor"), a **risk** pairs two or more conflicting functions, and **rules** are the technical checks. Typical conflicts:

| Conflict | Risk |
|---|---|
| Maintain vendor master (BP/XK01) and post vendor payments (F110/F-53) | Fictitious vendor paid |
| Create PO (ME21N) and release PO (ME29N) | Self-approved purchase |
| Post goods receipt (MIGO) and invoice verification (MIRO) | Pay for goods not received |
| Maintain material/price and adjust inventory counts | Stock manipulation |
| Create customer and post incoming payment or credit memo | Misappropriated cash |
| Develop code and import transports into PRD | Unreviewed change to live system |
| User admin (SU01) and role admin (PFCG) | Self-granted access |

**Critical access** is single-person risk (for example SAP_ALL, debug-with-replace, table maintenance of sensitive tables). Where separation is impossible (small teams), use **mitigating controls**: independent review of a report, approval workflow, monitoring, and documented sign-off.

### Example
An access review of 1,200 users with a 120-risk rule set finds **340 users (28.3%)** with at least one conflict. After role redesign (splitting "AP clerk" from "vendor master" roles) and mitigating controls for the small plant teams, **85 users (7.1%)** remain, each with a documented control owner and periodic review. The metric tracked is "users with unmitigated SoD conflicts", not the raw number of conflicts.

### In the news
See news box. SAP Access Control's access risk analysis automates exactly this rule-based detection, in real time or offline with simulation before roles are assigned.

### Interview angle
> [!question] How it is asked
> "Give three SoD conflicts in procure-to-pay and how you would handle a small team that cannot separate them."

> [!tip] Strong answer includes
> - Examples from vendor master, PO release, GR/IR
> - Preventive (role design, workflow) vs detective (reports) controls
> - Mitigating controls for unavoidable overlap, with owner and frequency
> - Link to ITGC and external audit evidence; refer to [[080 SAP MM — Materials Management]] for P2P documents

---
## 8. SAP GRC Access Control and Cloud Identity Access Governance
> 🟡 Tier 3 · _Key points:_ ARA, EAM/firefighter, BRM, ARM, user access review

### Definition
**SAP GRC (Governance, Risk and Compliance)** is a suite; the access-related product is **SAP Access Control** with four main capabilities (per SAP Learning):
1. **Access Risk Analysis (ARA):** SoD and critical-access analysis with delivered rule sets, simulation before granting access, remediation workflows and mitigation controls.
2. **Emergency Access Management (EAM, "firefighter"):** a privileged ID is checked out for a stated reason and period; all actions are logged and sent to a **controller** for review.
3. **Business Role Management (BRM):** a repository and workflow for role definition, approval and risk analysis, plus periodic role certification.
4. **Access Request Management (ARM):** self-service requests with approval workflow, embedded risk check and auto-provisioning.

Related: **user access review** (managers certify who has what), **SAP Process Control** (control testing and monitoring for SOX-style programmes) and **SAP Risk Management**. The cloud counterpart for new and RISE customers is **SAP Cloud Identity Access Governance (IAG)**, which covers access analysis, role design, access requests and privileged access in a SaaS model; check SAP's roadmap for product status when advising.

Implementation sequence consultants use: define rule set and business functions, clean roles, run baseline analysis, remediate, switch on ARM workflow, run first review, then ongoing monitoring.

### Example
At month-end a finance manager needs to correct postings in PRD. Instead of receiving a permanent powerful role, she requests firefighter ID `FF_FIN_01` through EAM with the ticket number, uses it for two hours, and the controller receives a log of every transaction and table change to approve. After approval the ID is checked back in.

### In the news
See news box. SAP's description of EAM (temporary elevated access with a detailed action log) is the control point that regulators look for in privileged access.

### Interview angle
> [!question] How it is asked
> "How would you give a manager one-time elevated access in production without breaking controls?"

> [!tip] Strong answer includes
> - Firefighter/EAM concept: reason, time limit, full log, controller review
> - ARA before granting access, with mitigation
> - Differences between preventive and detective controls
> - Awareness of the move to cloud IAG for new landscapes

---
## 9. Audit Trails: Change Documents, Table Logs, Security Audit Log
> 🟡 Tier 3 · _Key points:_ CDHDR/CDPOS, SCDO, SM19/SM20, rec/client, SM21

### Definition
Different logs answer different questions:
- **Change documents** record who changed master and document data: header `CDHDR` (object class, object ID, user, date, time, transaction) and items `CDPOS` (table, field, old and new value). Display via the object's transaction (for example in MM03 or FK03/BP: "Environment > Changes"), or reports like `RSSCD100`. Object definitions in `SCDO`. Typical use: who changed a vendor's bank account or a price.
- **Table logging:** database-level logging of selected tables when the technical setting "log data changes" is on (SE13) and profile parameter `rec/client` is set; evaluated with `SCU3`; stored in `DBTABLOG`. Use for configuration tables.
- **Security Audit Log:** configured in `SM19` (newer systems via `RSAU_CONFIG`), evaluated in `SM20` (or `RSAU_READ_LOG`): logons, failed logons, RFC calls, transaction starts, user master changes.
- **System log** `SM21`, **ABAP short dumps** `ST22`, **application logs** `SLG1`, **statistical records** `STAD`.
- **Document trail for users:** SUIM change documents show role and user changes.

Indian context: under the Companies (Accounts) Rules, accounting software used by a company must have an **audit trail (edit log)** of each change to books of account, enabled throughout the year and not capable of being disabled, applicable from financial years starting on or after **1 April 2023** (verify the current wording and auditor-reporting requirements with the ICAI and MCA text before quoting in an interview). SAP's change documents and table logs are common evidence for this.

### Example
A vendor's bank account changed two days before a large payment. The auditor uses the vendor's change documents: user `RAVI.P`, changed field `BANKN` (bank account) at 22:14 on the previous Sunday; the SoD report shows RAVI.P is also in the payment-run role. The conflict, not the change itself, is the finding; the evidence comes from CDHDR/CDPOS.

### In the news
See news box. The CVE-2025-31324 incident is a reminder that detective logs at the server level (new files on the application server, unusual RFC calls) complement business-level change documents.

### Interview angle
> [!question] How it is asked
> "How can you find out who changed a vendor's bank details, and for how long is that data available?"

> [!tip] Strong answer includes
> - Change documents (CDHDR/CDPOS) and the display path in the master data transaction
> - Table logging for config tables, Security Audit Log for system events
> - Retention and archiving policy for logs
> - Link to audit trail requirements and ITGC

---
## 10. BASIS Tasks Overview and the Monitoring T-codes
> 🟡 Tier 3 · _Key points:_ SM50, SM37, ST22, SM21, SM12, SM13, SM59, ST03N

### Definition
**BASIS** (the SAP technical administration function) keeps the system running. Business and functional consultants should recognise these tools:

| Area | T-code | Use |
|---|---|---|
| Work processes | `SM50` (local), `SM66` (global) | See running dialog, background, update processes; spot long-running or stuck |
| Background jobs | `SM37`, `SM36` | Monitor and schedule jobs; job log and spool |
| ABAP short dumps | `ST22` | Runtime errors with cause and reference |
| System log | `SM21` | Kernel and system events |
| Locks | `SM12` | Enqueue entries; document locked by another user |
| Update requests | `SM13` | Failed update tasks (document did not post fully) |
| Users logged on | `SM04`, `AL08` | Who is on, which terminal |
| Workload | `ST03N` | Response-time analysis per transaction and user |
| SQL trace | `ST05` | Database performance, with `ST02` for buffers |
| RFC / interfaces | `SM59`, `SM58`, `SMQ1`, `SMQ2` | Destinations, transactional and queued RFC errors |
| Output | `SPAD`, `SP01`, `SOST` | Printers and spool; mail send status |
| Parameters | `RZ10`, `RZ11` | Profile parameters |
| Application log | `SLG1` | Logs from interfaces and migrations |

Routine tasks: patching and support packages, kernel updates, system copies (refresh QAS from PRD), backups and restore tests, user administration support, transport imports, capacity and database monitoring.

### Example
Finance reports that "payment run F110 stopped". The team checks `SM37` and finds job `F110-PAYRUN` cancelled; the job log shows a short dump reference. In `ST22` the dump is "TSV_TNEW_PAGE_ALLOC_FAILED" (memory), so Basis raises memory limits; the job is rerun and completes. Business users should note the dump timestamp and ID rather than only saying "system error".

### In the news
See news box. Monthly patching and kernel updates are routine Basis tasks that now carry security urgency (HotNews notes with CVSS above 9).

### Interview angle
> [!question] How it is asked
> "A month-end job failed overnight. What do you check and in what order?"

> [!tip] Strong answer includes
> - SM37 job log and spool, then ST22 dump, SM21 system log, SM12/SM13 for locks and updates
> - Re-run safely (variants, restart point), communicate to business
> - Preventive monitoring and alerting
> - Escalation path to Basis and application owner

---
## 11. Job Scheduling and Background Processing
> 🟡 Tier 3 · _Key points:_ SM36, variants, periodic jobs, statuses, job chains

### Definition
**Background jobs** run without a user session, using **background work processes**. A job (`SM36` or SM36 wizard) has: **steps** (ABAP report with a **variant**, external command, or external program), **start condition** (immediate, date/time, after another job or event, periodic), **job class** (A high, B medium, C low) and **target server**. Job **statuses**: scheduled, released, ready, active, finished, cancelled. Evaluate in `SM37` (filter by user, name, date, status); job log and spool show results.

Common business jobs: nightly **MRP** (`MD01N`), **availability** and replenishment runs, **billing due list**, **payment run**, **GR/IR clearing**, **depreciation**, interface file imports, report mailings, archiving.

Good practice: dedicated **batch user IDs** (system type), **variants** with dates relative to run date, **job chains** with dependencies (use event-based or external schedulers such as SAP Solution Manager job scheduling or third-party schedulers for complex chains), failure alerts, documented restart procedures, and no heavy dialogue-time reports in business hours.

### Example
Nightly chain (hours): 22:00 stock/consumption data extract (0.5), 22:30 MRP Live for plants 1100 and 1200 (1.5), 00:00 convert planned orders (0.5), 00:30 purchase requisition release workflow (0.5), 01:00 refresh reports and dashboards (1.0), finish 02:00. A delay in step 2 delays everything after it; if MRP takes 3.0 hours the chain finishes 03:30, and a monitoring alert on step 2 allows planners to start the day knowing the plan is not ready.

### In the news
See news box. In S/4HANA, MRP Live and HANA-based reports shorten nightly chains, so schedules often tighten after migration; see [[200 SAP S-4HANA Migration, Data Migration & Testing]].

### Interview angle
> [!question] How it is asked
> "How would you schedule and monitor the nightly planning and billing runs?"

> [!tip] Strong answer includes
> - Job definition elements (steps, variant, start condition, class)
> - Chain dependencies and restart procedure
> - Monitoring (SM37, alerts) and ownership of failure response
> - Avoid user-ID-based jobs; use controlled batch users

---
## 12. Performance Basics for Business Users
> 🟡 Tier 3 · _Key points:_ Response time components, ST03N, selection criteria, background reports, HANA

### Definition
Dialog **response time** (as in `ST03N`) is the sum of: **wait time** (waiting for a free work process), **roll-in/roll-out and load/generation time**, **CPU time**, **database request time** and sometimes **GUI/network time**. Rules of thumb: average dialog response below about one second, database share below roughly half, and wait time near zero; treat these as indicative thresholds to compare against your own baseline.

What users can do:
- Use **narrow selection criteria** (plant, date range) rather than blank selection on large tables.
- Run heavy reports **in background** with a variant, off peak.
- Avoid `SE16N` on large tables in PRD without filters; use standard reports or embedded analytics (see [[085 SAP Reporting & Analytics]]).
- Save **variants** and layouts instead of re-downloading large lists to Excel.

What Basis and developers do: index and SQL tuning (`ST05`), buffer tuning (`ST02`), memory and work-process sizing, **code pushdown** to HANA, retiring slow custom reports.

### Example
Average dialog response of 1,450 ms is made of wait 60, roll/load 90, CPU 280, database 820 and GUI/other 200 ms (sum 1,450). The database share is 820/1,450 = **56.6%**, which points to SQL or missing index tuning rather than adding application servers. After tuning two custom reports the database part falls to 430 ms and total response to 1,060 ms (a 27% improvement).

### In the news
See news box. Faster HANA-based processing is one of the benefits that [[200 SAP S-4HANA Migration, Data Migration & Testing]] promises, but unmodified custom code can still be slow.

### Interview angle
> [!question] How it is asked
> "Users say SAP is slow. How do you structure the investigation?"

> [!tip] Strong answer includes
> - Scope the problem: one transaction/user/time vs system-wide
> - Check response time breakdown in ST03N; find which component dominates
> - Isolate with trace (ST05) for DB problems; check jobs competing for resources
> - Quick user-side mitigations plus the permanent fix

---
## 13. SOX, ITGC and the India Control Framework
> 🟡 Tier 3 · _Key points:_ Four ITGC domains, key controls, ICFR in India, evidence

### Definition
**IT general controls (ITGC)** are the controls over the environment in which applications run; they support reliance on automated application controls (like three-way match) for financial reporting. Four classic domains and SAP evidence:

| Domain | Example controls | SAP evidence |
|---|---|---|
| Access to programs and data | Joiner-mover-leaver, SoD, privileged access, password policy | SU01/USR02, SUIM, GRC reports, SAP_ALL assignment list |
| Program change management | Approved, tested, segregated changes | Transport logs (E070), ChaRM tickets, SCC4 settings |
| Program development / implementation | Controlled build, data migration reconciliations | Test evidence, sign-offs (see [[200 SAP S-4HANA Migration, Data Migration & Testing]]) |
| Computer operations | Job scheduling, backup, incident management | SM37 history, backup logs, ticket data |

**SOX Section 404** (US) requires management assessment and auditor attestation of internal control over financial reporting; it applies to US-listed companies, which includes some Indian companies listed on US exchanges and Indian subsidiaries of US parents. In **India**, the **Companies Act 2013** requires directors to confirm adequate internal financial controls (Section 134(5)(e) for listed companies) and the statutory auditor to report on **internal financial controls over financial reporting** (Section 143(3)(i)); confirm wording and applicability before quoting. The ICAI guidance note on audit of ICFR is the practical reference. Application controls (for example three-way match, tolerance limits, automatic account determination) are tested alongside ITGC.

Testing method: **design** effectiveness (is the control well designed?) and **operating** effectiveness (does it work through the period?), using population extracts and samples.

### Example
The auditor tests "all production transports are approved". The Basis team extracts all transports imported to PRD in the year from transport logs: 640. A sample of 25 is checked for ticket, approval and test evidence; 24 comply and one emergency change lacks retrospective approval, which is reported as a control deviation, documented, and remediated by tightening the urgent-change procedure. Sample sizes depend on the auditor's method; the numbers here are illustrative.

### In the news
See news box. Patching evidence (which HotNews notes were applied, and when) is increasingly requested in ITGC testing.

### Interview angle
> [!question] How it is asked
> "What are ITGCs, and what would an auditor ask you for in a SAP environment?"

> [!tip] Strong answer includes
> - Four ITGC domains with SAP examples
> - Difference between ITGC and application controls
> - Indian ICFR framing and, where relevant, SOX 404
> - Evidence is system-generated and time-stamped, not a spreadsheet created later

---
## 14. ⭐ Advanced: What Business Users and Consultants Should Know
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A practical checklist that links technical governance to everyday behaviour:
1. **Never share IDs.** Every posting is traceable to a person; shared IDs break the audit trail and SoD.
2. **Request, do not borrow.** A missing authorisation goes to the role owner with an SU53 screenshot and business justification.
3. **Test in QAS**, never in PRD. Test data should be created for the purpose or masked.
4. **Know your transaction and your document numbers.** Quote document numbers, T-codes, dump IDs and times when raising incidents; they save hours.
5. **Understand change windows.** Month-end, quarter-end and year-end freeze transports; plan changes around the finance calendar.
6. **Master data discipline.** Bank account, tax number and payment term changes need a second-person check ([[175 Data Quality, Master Data & Data Governance]]).
7. **Respect segregation.** Do not ask a colleague to "just approve" a document you created.
8. **Spot phishing.** SAP logon screen lookalikes, fake "role request" mails.
9. **Interfaces and RFC users** are privileged technical identities; they need owners, secrets rotation and least privilege.
10. **Consultant conduct:** use named IDs, no production access without a ticket, no hard-coded passwords in code, document every config change with a transport and ticket.

### Example
During UAT a tester discovers that the "AP clerk" role can also run F110 payments. Instead of simply removing the transaction, the consultant raises a ticket with the role owner, runs a before/after SoD simulation, retests the clerk's end-to-end invoice processing in QAS, and transports the corrected role through the standard path, leaving evidence for the audit file.

### In the news
See news box. Security incidents like CVE-2025-31324 begin below the level at which business users work, but the checklist above shows the user-side behaviours that keep stolen credentials and misuse from spreading.

### Interview angle
> [!question] How it is asked
> "You are the functional lead and a director asks you to give a junior colleague his ID for a week. What do you do?"

> [!tip] Strong answer includes
> - Refuse politely, offer the correct route (role request, temporary role with approval)
> - Explain the audit and SoD reasons in business terms
> - Offer a faster route (urgent access request, firefighter if truly needed)
> - Document and escalate if pressure continues

Related notes: end-to-end flows and T-codes in [[202 SAP Interview Questions, T-code Cheat Sheet & End-to-End Flows]], FI-side controls in [[190 SAP FI-CO Essentials for Operations Professionals]], general ERP governance in [[013 ERP & Enterprise Systems (SAP-Oracle)]], and risk frameworks in [[040 Risk & Stakeholder Management]].
