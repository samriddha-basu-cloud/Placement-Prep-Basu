---
tags: [sap-erp, tier2]
area: SAP ERP
topic: "SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)"
tier: Tier 2
roles: Operations / Consulting
status: complete
subtopics: 14
---
# SAP Transportation & Logistics Execution (LE-TRA, TM, GTS)

⬅ [[195 SAP SD Advanced - Pricing, Output & Document Flow]] · [[_Index - SAP ERP|SAP ERP]] · [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]] ➡

> **Area:** SAP ERP · **Priority:** 🟠 Tier 2 · **Target roles:** Operations / Consulting

## Sub-topics in this note
1. [[#1. Logistics Execution Landscape: SD, LE, TM, EWM and GTS]]
2. [[#2. Outbound Delivery Processing and Goods Issue]]
3. [[#3. Handling Units and Packing]]
4. [[#4. Shipping Point, Route and Transportation Planning Point]]
5. [[#5. Shipment Document (VT01N) and Shipment Processing]]
6. [[#6. Transportation Planning and Consolidation in LE-TRA]]
7. [[#7. Freight Cost Calculation and Shipment Cost Settlement]]
8. [[#8. SAP TM: Embedded vs Standalone, Freight Orders and Documents]]
9. [[#9. Carrier Tendering and Freight Order Management: Worked Example]]
10. [[#10. SAP Global Trade Services (GTS): Compliance, Customs and Preference]]
11. [[#11. 3PL and Carrier Integration]]
12. [[#12. Worked Outbound Flow: Order to Delivery to Freight to Billing]]
13. [[#13. ⭐ Advanced: E-Way Bill, GST and Transport Compliance in India]]
14. [[#14. ⭐ Advanced: Transportation KPIs and Cost-to-Serve]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): SAP bundles transportation, warehouse, yard and network into one logistics suite
> **SAP Transportation Management named a Gartner Magic Quadrant Leader for the 11th consecutive year (SAP report, 1 April 2025).** SAP's announcement cites generative AI in the transportation cockpit for conversational planning, AI-assisted goods receipt analysis, freight planning that minimises CO2 emissions down to item level, expanded 3D load planning, shipping and receiving orchestration with Extended Warehouse Management, and integration of SAP TM, SAP EWM, SAP Yard Logistics and SAP Business Network for Logistics. It also lists regulatory compliance modelling for customs and environmental rules. (Vendor report of an analyst result: [SAP News Center, 1 Apr 2025](https://news.sap.com/2025/04/sap-a-leader-gartner-magic-quadrant-transportation-management-systems/))
>
> **SAP Logistics Management and Supply Chain Orchestration (7 October 2025).** At SAP Connect SAP announced SAP Logistics Management, a cloud-native solution for multi-tier distribution networks (general availability planned Q1 2026), and SAP Supply Chain Orchestration for disruption detection (H1 2026). It said SAP Business Network now runs on SAP BTP and facilitates "over US$6.3 trillion in annual commerce across 190 countries". ([SAP News Center, 7 Oct 2025](https://news.sap.com/2025/10/sap-connect-innovative-updates-supply-chain-management/))
>
> **SAP named a Leader in the first Gartner Magic Quadrant for Supply Chain Management Suites (13 August 2026).** SAP's report lists SAP Transportation Management, SAP Extended Warehouse Management, SAP Business Network, SAP Integrated Business Planning and SAP Ariba among the suite components and describes new Joule assistants for logistics through 2026. ([SAP News Center, 13 Aug 2026](https://news.sap.com/2026/08/sap-a-leader-inaugural-gartner-magic-quadrant-scm-suites/))
>
> Sub-topics that say **"See news box"** reuse these items. Concept notes: [[009 Logistics & Distribution]], [[125 Transportation Management Deep Dive]], [[126 International Trade Documentation, Customs & Trade Finance]].

---
## 1. Logistics Execution Landscape: SD, LE, TM, EWM and GTS
> 🟠 Tier 2 · _Key points:_ Where LE-SHP, LE-TRA, SAP TM, EWM and GTS sit in the order-to-delivery chain

### Definition
**Logistics Execution (LE)** in SAP ERP has three main parts: **LE-WM** (warehouse, see [[083 SAP WM-EWM — Warehouse]]), **LE-SHP** (shipping: deliveries, picking, packing, goods issue) and **LE-TRA** (transportation: shipments, routes, freight costs). Beyond LE:
- **SAP TM (Transportation Management):** advanced planning, carrier selection, tendering, freight settlement; embedded in S/4HANA or standalone.
- **SAP EWM:** warehouse execution ([[197 SAP EWM Deep Dive - Process-Oriented Warehousing]]).
- **SAP GTS (Global Trade Services):** trade compliance, customs and preference.
- **SAP Business Network for Logistics:** collaboration with carriers.

Chain: **sales order → delivery (LE-SHP) → warehouse pick → pack (HU) → shipment (LE-TRA) / freight order (TM) → goods issue → billing → freight settlement**. Each hand-off is a document in the document flow (see [[195 SAP SD Advanced - Pricing, Output & Document Flow]]).

### Example
Delivery 80012345 (4,000 kg), 80012346 (3,500 kg) and 80012347 (2,300 kg) for customers on the Pune to Delhi lane: LE-SHP creates the three deliveries; LE-TRA consolidates them into shipment 3000123 (9,800 kg) with a contracted road carrier as service agent; freight is calculated and settled to the carrier. In TM the same step creates a freight order from a transportation requirement.

### In the news
See news box. SAP's 2026 Gartner suites report names TM and EWM as components of an integrated supply chain suite.

### Interview angle
> [!question] How it is asked
> "Where does SAP SD end and logistics execution begin, and where would you use TM instead of LE-TRA?"

> [!tip] Strong answer includes
> - Boundary: sales order and pricing in SD, delivery and shipment in LE
> - Capabilities: LE-TRA basic planning and freight cost; TM optimisation and tendering
> - GTS for compliance on cross-border flows
> - Document flow and integration points to FI and MM

---
## 2. Outbound Delivery Processing and Goods Issue
> 🟠 Tier 2 · _Key points:_ VL01N/VL10, picking, packing, PGI (601), delivery split, delivery block, partial delivery

### Definition
**Outbound delivery** (`VL01N` single, `VL10` collective due list) confirms what leaves the warehouse and when. Steps:
1. **Create delivery** from sales order schedule lines due for delivery (shipping point determination, delivery scheduling, route).
2. **Picking:** creates a transfer order (WM) or warehouse task (EWM); or pick quantity directly in the delivery (`VL02N`, no WM) with storage location determination.
3. **Packing:** HU creation (sub-topic 3).
4. **Post goods issue (PGI)** (`VL02N`, or `VL06G`): stock decrease with **movement type 601**, accounting entry **Dr COGS, Cr Inventory**, document flow updated; delivery becomes billing-relevant; PGI reversal with `VL09`.
Delivery splits (by warehouse, route, weight limit, partner) and **delivery blocks** (credit, billing) control exceptions. **Delivery types** (LF standard, LO delivery without order reference, NL replenishment/stock transfer delivery) control behaviour; delivery output (delivery note, packing list) is covered in [[195 SAP SD Advanced - Pricing, Output & Document Flow]].

$$\text{COGS at PGI} = \text{quantity issued} \times \text{valuation price}$$

### Example
Delivery of 1,000 cartons at moving average ₹320 per carton: PGI posts COGS ₹3,20,000 (Dr COGS, Cr Inventory). If only 900 are available, partial delivery posts ₹2,88,000 and the remaining 100 stay open as a back-order for later delivery, unless the customer requires complete delivery.

### In the news
See news box. In S/4HANA PGI posts to one material document table, so stock is visible immediately for ATP and planning.

### Interview angle
> [!question] How it is asked
> "What happens in SAP when you post goods issue on a delivery?"

> [!tip] Strong answer includes
> - Stock reduction (601), accounting entry, document flow, billing due list update
> - Pre-conditions: picking complete, packing, no blocks
> - Reversal path and what cannot be reversed (invoiced)
> - Link to ATP, COGS and inventory valuation ([[080 SAP MM — Materials Management]])

---
## 3. Handling Units and Packing
> 🟠 Tier 2 · _Key points:_ Packaging materials, packing instructions, HU, SSCC, nested HU, delivery-level packing, shipment-level packing

### Definition
A **handling unit (HU)** is a physical unit (pallet, carton, drum, container) made of **packaging material** plus its contents, identified by a unique number (the **SSCC/NVE**). **Packaging materials** are material master records of type VERP, grouped by **packaging material type** (box, pallet, container) with allowed weight and volume. **Packing instructions** define what goes where, such as "max 60 cartons per pallet, 1,000 kg". HUs can be **nested** (cartons on pallet in container) and **packed at delivery level** (`VL02N`) or **at shipment level** (`VT02N`, consolidated packing).
Auto-packing (via packing instruction) and manual packing (scan or drag and drop) are both supported; HU data prints on labels and is passed to ASN/EDI to customers and to 3PLs. In EWM the HU is the main unit of movement (see [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]]).

Weight and volume totals of HUs update the **delivery gross weight, volume** and the **shipment's loading utilisation**, which in turn drive freight.

$$\text{Pallets needed} = \left\lceil \frac{\text{cartons}}{\text{cartons per pallet}} \right\rceil$$

### Example
Eight store deliveries total 960 cartons; one pallet holds 60 cartons. Loose arithmetic gives 960 / 60 = 16 pallets, but every delivery needs its own labelled HUs. If the stores order 120, 120, 120, 120, 120, 120, 100 and 140 cartons, the pallet counts per delivery are 2, 2, 2, 2, 2, 2, 2 (100 cartons: 1 full pallet plus a 40-carton partial pallet) and 3 (140 cartons: 2 full plus 20 loose) = **17 pallets**, one more than the 16 from the total, because pallets are not shared between stores. Freight planners therefore count HUs by delivery, not by total cartons.

### In the news
See news box. TM's expanded 3D load planning uses HU dimensions and weights from this master data.

### Interview angle
> [!question] How it is asked
> "Why does SAP need HUs in shipping, and what does packing do to freight?"

> [!tip] Strong answer includes
> - HU, packaging materials, packing instructions, SSCC
> - Delivery-level versus shipment-level packing
> - Impact on weight, volume, load planning, freight and ASN content
> - Data governance for packaging dimensions

---
## 4. Shipping Point, Route and Transportation Planning Point
> 🟠 Tier 2 · _Key points:_ Shipping point determination, route determination, transit time, transportation planning point, service agent

### Definition
- **Shipping point:** determined from plant + shipping condition + loading group; defines pick/pack and loading times, working calendar and shipping output.
- **Route:** determined from departure zone (shipping point) + shipping condition + transportation group + ship-to transportation zone (+ weight group); stores transit time, transportation lead time, **service agent** (carrier), **stages** (legs).
- **Transportation planning point:** the organisational unit (an individual or team) responsible for planning and processing shipments; assigned to a company code. Delivery scheduling logic is explained in [[195 SAP SD Advanced - Pricing, Output & Document Flow]] (sub-topic 12).
- **Means of transport** (truck type 32 ft, 20 ft container) and **transportation group/loading group** inform load capacity checks.

Cross-border shipments add **incoterms**, **customs documents** and **leg determination** (pre-carriage, main carriage, on-carriage) with ports and airports as transportation connection points.

### Example
Plant Pune, customer in Delhi: route R-PUN-DEL with transit time 3 days, service agent a contracted carrier, stages: Pune plant to Delhi DC (1 leg). Cross-border: Nhava Sheva port as transportation connection point: leg 1 Pune to JNPT (pre-carriage), leg 2 JNPT to Jebel Ali (main carriage), leg 3 customer delivery (on-carriage).

### In the news
See news box. Gartner and SAP both highlight cross-border compliance and multimodal planning as growth areas for TM.

### Interview angle
> [!question] How it is asked
> "How does SAP know which carrier and transit time to use for an order?"

> [!tip] Strong answer includes
> - Determination keys for shipping point and route
> - Route attributes: transit time, service agent, stages
> - Planning point as ownership and authorisation unit
> - Cross-border legs and incoterms

---
## 5. Shipment Document (VT01N) and Shipment Processing
> 🟠 Tier 2 · _Key points:_ Shipment types, stages and legs, processing statuses, VT04 due list, shipment completion

### Definition
The **shipment document** (`VT01N` create, `VT02N` change, `VT03N` display, `VT04` shipment due list for automatic creation, `VT11` shipment list) groups one or more deliveries (inbound or outbound) into one transport movement.

Structure:
- **Header:** shipment type (for example individual or collective shipment), transportation planning point, carrier (service agent), means of transport, route, dates (planning, check-in, loading start/end, shipment completion, start, end), total weight and volume.
- **Stages/legs:** pre-carriage, main carriage, on-carriage, return leg; each stage has start and end points and its own service agent.
- **Items:** deliveries or HUs assigned.
- **Statuses** (processing control): planning, check-in, loading start, loading end, shipment completion, shipment start, shipment end; each is a milestone date and may trigger output (shipping documents, **bill of lading**, **e-way bill**), a goods issue, or tendering.
- **Shipment completion:** step that checks that all deliveries are packed and loaded; it triggers freight calculation and outputs.

**Collective shipment** processing combines deliveries from several shipping points; **direct shipment** combines delivery to many ship-to's on one run (milk-run). Output on shipment: shipping instructions, packing list, transport label.

### Example
Three deliveries (4,000, 3,500, 2,300 kg) are combined in shipment 3000123: truck of 10,000 kg capacity: **98%** weight utilisation; volume 31 m³ of 32 m³ (**96.9%**). Shipment completion at 16:00 triggers freight calculation and prints the bill of lading; shipment start at 18:30 marks departure.

### In the news
See news box. In TM, the equivalent steps use freight orders and execution events for tracking.

### Interview angle
> [!question] How it is asked
> "Walk me through shipment creation and what each processing status triggers."

> [!tip] Strong answer includes
> - Header, stage, item structure
> - Statuses and their downstream triggers
> - Collective vs direct shipment and capacity utilisation
> - Documents: bill of lading, e-way bill, shipping instructions

---
## 6. Transportation Planning and Consolidation in LE-TRA
> 🟠 Tier 2 · _Key points:_ Manual and automatic shipment creation, consolidation rules, capacity, limits of LE-TRA vs TM

### Definition
LE-TRA planning uses **shipment types, route and rules** to group deliveries:
- **Shipment planning:** from the **shipment due list** (`VT04`) select deliveries and create shipments; **collective processing** applies **consolidation criteria** (route, ship-to, weight limits) to build many shipments in one run.
- **Capacity and checks:** weight and volume limits of the means of transport; **loading-point scheduling**; transportation dates by backward scheduling from delivery date.
- **Carrier assignment:** the **service agent** from the route or manual selection.
Limitations: LE-TRA has **limited optimisation** (no automatic cost-based carrier selection or multi-pick multi-drop routing) and basic tendering; that is the field of **SAP TM** (vehicle scheduling and routing optimiser, carrier selection by cost/service, load planning).

Planning objective: minimise cost subject to service windows: minimise
$$\sum_{k} (\text{freight cost}_k) \quad \text{subject to capacity}_k \ge \text{load}_k,\ \text{pickup}\ \le\ \text{latest dispatch}$$
which is a vehicle routing problem when many stops exist (see [[148 Operations Research - Network Models & Integer Programming]]).

### Example
Delhi NCR lane volume of 24,500 kg, trucks of 10,000 kg: minimum trucks = ceil(24,500 / 10,000) = **3** (average utilisation 81.7%); a fourth truck would drop it to 61.3% and add a full trip cost. If deliveries can be grouped as 9,800 + 9,800 + 4,900 kg, the third load fits a 5-tonne vehicle at 98% utilisation, which is cheaper than a full 10-tonne truck at 49%.

### In the news
See news box. Gartner-recognised TM capabilities such as multi-constraint optimisation (cost, time, emissions) are the step beyond LE-TRA.

### Interview angle
> [!question] How it is asked
> "When is LE-TRA enough and when should you move to TM?"

> [!tip] Strong answer includes
> - LE-TRA: simple shipments, fixed carriers, low complexity
> - TM triggers: multi-modal, carrier tendering, optimisation, multiple legs, 3PL/LSP business
> - Cost/benefit and integration effort
> - Quick wins: consolidation rules, utilisation KPI

---
## 7. Freight Cost Calculation and Shipment Cost Settlement
> 🟠 Tier 2 · _Key points:_ Shipment cost document, pricing procedure for freight, scales by weight/distance, accruals, service entry sheet, invoice verification

### Definition
**Shipment costs** are calculated per shipment stage using the **condition technique** with a dedicated shipment-cost pricing procedure (see [[195 SAP SD Advanced - Pricing, Output & Document Flow]]): conditions such as base freight by weight or distance scale, **fuel surcharge** (percentage), **loading/unloading**, **detention/waiting**, **toll** and **minimum charge**; **tariff zones**, **freight codes** and **service agent** feed the condition record.

Settlement chain:
1. **Shipment cost document** (`VI01` create, `VI02` change; shipment cost list `VI04`) created from the shipment after completion; items per stage.
2. **Settlement:** posts an **accrual** or the service via an automatically generated **service purchase order and service entry sheet** against the carrier (vendor).
3. **Invoice verification** (`MIRO`) of the carrier invoice against the service entry sheet; differences are investigated (see [[080 SAP MM — Materials Management]]).
4. **Controlling/FI:** account assignment to cost centre, order or profitability segment, so freight appears in **cost-to-serve** ([[138 Order Management, Customer Service & Cost-to-Serve]]).
Freight to the customer is charged on the SD side via a freight condition (KF00 in pricing, which can be estimated from the shipment cost).

$$\text{Freight cost} = \text{base} + \text{fuel surcharge} + \text{loading} + \text{detention} + \text{toll}$$

### Example
Pune to Delhi, 1,420 km: base ₹46 per km × 1,420 = **₹65,320**; fuel surcharge 8% of base = ₹5,225.60; loading and unloading fixed ₹2,500; detention 6 hours × ₹400 = ₹2,400; toll at actual ₹7,800. Total **₹83,245.60**, or **₹8.49 per kg** for 9,800 kg. Allocation to deliveries by weight: 4,000 kg = ₹33,977.78; 3,500 kg = ₹29,730.57; 2,300 kg = ₹19,537.23 (sum ₹83,245.58 before rounding). (GST on freight depends on the carrier's registration and the applicable rate; check with tax.)

### In the news
See news box. TM's CO2-minimising freight planning adds an environmental cost line next to the monetary one.

### Interview angle
> [!question] How it is asked
> "How is freight cost calculated and paid in SAP, and how does it reach the P&L?"

> [!tip] Strong answer includes
> - Condition technique for freight with scales and surcharges
> - Shipment cost document, service PO/SES, MIRO and accruals
> - Allocation to deliveries and customers; cost-to-serve use
> - Controls: rate-card governance, invoice audit, detention

---
## 8. SAP TM: Embedded vs Standalone, Freight Orders and Documents
> 🟠 Tier 2 · _Key points:_ Embedded TM in S/4HANA vs standalone TM; transportation requirement, freight unit, freight order, freight booking, forwarding order, settlement

### Definition
**SAP Transportation Management** exists as:
- **Embedded TM in S/4HANA:** runs in the S/4HANA system, shares master data, creates documents from sales orders, deliveries and purchase orders without distribution; **basic shipping** covers simpler scope, advanced functions (optimisation, tendering, charge management) need licences. Lower integration effort.
- **Standalone SAP TM:** a separate system connected to ERP (S/4HANA or ECC); decoupled planning, easier to serve multiple ERPs or an LSP with many customers.

Document model: **order-based transportation requirement (OTR)** and **delivery-based transportation requirement (DTR)** from ERP; **freight units** (planning objects: what must move), **freight orders** (road: a carrier's job), **freight bookings** (ocean/air) and **forwarding orders** (an LSP's customer order); **charge calculation** via calculation sheets and agreements; **freight settlement** (freight settlement documents to the carrier, **forwarding settlement** to the customer) integrated with FI.

Capabilities: **planning cockpit** (map, Gantt), **VSR optimiser** for routing and scheduling, **carrier selection** (cost, priority, business share), **tendering**, **load planning**, **incident management**, **event handling/track and trace**, **carrier collaboration** via Business Network for Logistics (news box).

Selection: embedded for single S/4HANA landscapes and moderate volume; standalone for multi-ERP or LSP use cases (parallel to embedded vs decentralised EWM in [[197 SAP EWM Deep Dive - Process-Oriented Warehousing]]).

### Example
A manufacturer (S/4HANA) ships 600 deliveries a day. Embedded TM turns deliveries into freight units; the optimiser builds 70 freight orders on 6 lanes; carriers are selected by cost and acceptance; the settlement creates freight settlement documents that post accruals to FI.

### In the news
See news box. SAP's 2025 Leader announcement lists generative AI conversational planning in the TM cockpit and CO2-minimising planning down to item level.

### Interview angle
> [!question] How it is asked
> "Embedded or standalone TM for a client, and how do freight orders flow?"

> [!tip] Strong answer includes
> - Documents: requirement, freight unit, freight order/booking, settlement
> - Embedded vs standalone criteria (landscape, volume, 3PL)
> - Optimiser, carrier selection, tendering
> - Integration with EWM for shipping and receiving, and with Business Network for carriers

---
## 9. Carrier Tendering and Freight Order Management: Worked Example
> 🟠 Tier 2 · _Key points:_ Broadcast and sequential tendering, carrier acceptance, auto-award, spot vs contract, freight order execution

### Definition
**Tendering** offers freight orders to carriers. Types: **peer-to-peer** (sequential; one carrier at a time by rank), **broadcast** (several at once; best response wins), **open** (by portal; first to accept). Carrier **ranking** uses contract rates, quality score (on-time, damage), capacity and **business share** targets. Responses: accept, reject, or quote; **auto-award** rules decide. **Execution**: dispatch, **track and trace events** (departure, arrival, delay), proof of delivery, claim handling. Order of precedence: contract carrier first, spot market only when contract capacity or service fails.

Evaluation: price alone is not enough; use **total cost** = freight + expected failure cost (missed delivery) and measure **tender acceptance rate** and **on-time performance**.

### Example
A lane freight order is tendered by broadcast to three carriers: A quotes ₹64,500, B ₹61,200 and C ₹66,800 (all-in). B is cheapest, saving ₹3,300 vs A and ₹5,600 vs C. Suppose carrier B's historical on-time rate is 82% and a late delivery costs ₹15,000 in penalties and service recovery: expected failure cost = 0.18 × 15,000 = ₹2,700 → adjusted B = ₹63,900. A has 95% on time: expected failure = 0.05 × 15,000 = ₹750 → adjusted A = ₹65,250. B still wins by ₹1,350. If B's on-time rate were 70%, expected cost ₹4,500 → ₹65,700 and A would win. Sequential tendering with probabilities of acceptance (A 60%, B 80%, C 50%) means the chance that at least one accepts is 1 − 0.4 × 0.2 × 0.5 = **96%**.

### In the news
See news box. Carrier collaboration in the network and AI-based planning aim at higher tender acceptance and faster re-planning.

### Interview angle
> [!question] How it is asked
> "How would you design the carrier selection and tendering rules for a lane network?"

> [!tip] Strong answer includes
> - Contract vs spot, ranking criteria, business share and capacity
> - Total cost including service failure
> - Metrics: acceptance rate, OTIF, cost per kg, spot share
> - Governance of rate cards, escalation, claims

---
## 10. SAP Global Trade Services (GTS): Compliance, Customs and Preference
> 🟠 Tier 2 · _Key points:_ Compliance Management, Customs Management, Preference Management; feeder system blocks; sanctioned party list screening

### Definition
**SAP GTS** supports cross-border trade through three areas:
- **Compliance Management:** **sanctioned party list (SPL) screening** of business partners, **embargo checks**, **legal control** (export licences, import control, product classification such as HS/ECCN against control lists). In the integrated process, SD or MM documents are **sent to GTS as the feeder system**; if a check fails the document is **blocked** (for example delivery or goods issue blocked) until cleared.
- **Customs Management:** creation and filing of **export and import declarations**, transit procedures, **customs warehouse** and **inward processing** management, with country-specific customs systems connected by messages; local filing (in India via the national customs systems, usually with the customs broker or local tools) is part of the design.
- **Preference Management:** determination of **preferential origin** under **free trade agreements** (FTAs) using rules of origin, **vendor/long-term supplier declarations** and **proofs** (certificate of origin) so exports can claim lower duty and imports can use FTA benefits.
Classification, master data of **customs tariff numbers (HSN/HS)** and **partner master quality** drive accuracy (see [[126 International Trade Documentation, Customs & Trade Finance]] and [[175 Data Quality, Master Data & Data Governance]]). SAP's product positioning for trade compliance changes over time; confirm the current product and licence with SAP.

### Example
Exporter ships medical devices to the UAE under an FTA: GTS screens the consignee against sanction lists, checks the HS code against export control, creates the customs declaration data and determines preferential origin if the regional value content threshold is met. Duty saving, assumed: 5% duty on ₹1 crore of goods = ₹5,00,000; on a ₹10 crore annual volume saving ₹50 lakh, which justifies maintaining origin data.

### In the news
See news box. SAP's TM Leader announcement lists customs and environmental compliance modelling as part of its logistics offering.

### Interview angle
> [!question] How it is asked
> "What does GTS do for an exporter, and how does it integrate with SD?"

> [!tip] Strong answer includes
> - Three pillars: compliance, customs, preference
> - Feeder system integration and document blocks
> - Master data: classification, partner, origin rules
> - India-specific: export documents, LUT/GST, drawback schemes handled with local processes

---
## 11. 3PL and Carrier Integration
> 🟠 Tier 2 · _Key points:_ EDI/IDoc, shipping order and confirmation, ASN, APIs, Business Network for Logistics, track and trace, 3PL KPIs

### Definition
Outsourced logistics usually runs through messages between the ERP and the provider's systems:
- **Outbound shipping orders to a 3PL warehouse:** delivery data sent as a **shipping order** (message type SHPORD), **shipping confirmation** back (SHPCON) with actual quantities, batch, HU data; goods issue is then posted from the confirmation.
- **Inbound:** ASN (DESADV) or purchase order data; **goods receipt confirmation** from the 3PL.
- **Carrier:** tender, load tender, **shipment status** and **proof of delivery** by EDI, API or **SAP Business Network for Logistics** (news box).
- **Invoices:** carrier and 3PL invoices (freight, storage, handling) matched to shipment cost documents or service entry sheets.
Governance: **SLA and KPI** (order cycle time, on-time dispatch, inventory accuracy, damage), **audit rights**, **data ownership**, and **fallback** for message failures with monitoring (IDoc status, queue backlog). Strategic context in [[124 Outsourcing, Supplier Partnerships & Kraljic Strategies]].

### Example
FMCG company outsources a 40,000-pallet DC to a 3PL: ERP sends 1,200 shipping orders daily; 3PL confirms by 20:00; 12 confirmations fail daily due to batch mismatches (1%), delaying goods issue and billing. Fix by validating batch master data before sending: failure rate target below 0.2%, cutting delayed invoices from 12 to about 2 a day.

### In the news
See news box. SAP says Business Network (running on BTP) facilitates "over US$6.3 trillion in annual commerce" and offers Logistics collaboration with carriers.

### Interview angle
> [!question] How it is asked
> "How would you integrate a 3PL warehouse and a carrier with SAP and make the process reliable?"

> [!tip] Strong answer includes
> - Message flows: shipping order, confirmation, ASN, shipment status, invoice
> - Monitoring, error handling, reconciliation of stock
> - SLAs and KPIs with penalties
> - Master data alignment (product, batch, partner, UoM)

---
## 12. Worked Outbound Flow: Order to Delivery to Freight to Billing
> 🟠 Tier 2 · _Key points:_ End-to-end numbers across SD, LE-SHP, LE-TRA, FI/MM

### Definition
Reference flow for a Pune plant shipping to a Delhi customer (all figures illustrative):
1. **Sales order** `VA01`: 9,800 kg total in three items; pricing as in [[195 SAP SD Advanced - Pricing, Output & Document Flow]]; ATP confirms for 3 November; credit check passes.
2. **Delivery** `VL01N`: three deliveries created from the due list; picking in WM/EWM; packing into 16 HUs.
3. **Shipment** `VT01N`: three deliveries on one shipment; route R-PUN-DEL; carrier assigned; shipment completion.
4. **Freight** `VI01`: ₹83,245.60 calculated; accrued on completion.
5. **PGI** at loading end: COGS booked at moving average; **e-way bill** generated (consignment value above ₹50,000).
6. **Billing** `VF01`: invoice with IRN and QR (e-invoicing).
7. **Carrier invoice** matched to service entry sheet; payment per terms.
8. **Proof of delivery** → billing/collection triggers.

Costs and margin: $\text{Contribution} = \text{Net sales} - \text{COGS} - \text{freight}$.

### Example
Sales value (all three deliveries, assumed) ₹7,20,000; COGS ₹5,00,000; freight ₹83,245.60. Contribution = 7,20,000 − 5,00,000 − 83,245.60 = **₹1,36,754.40** or **19.0%** of sales (136,754.4 / 720,000). Freight is 11.6% of sales, large for a ₹7.2 lakh load: the pricing team asks whether the freight condition (KF00) in the sales order recovers it (if freight is charged at ₹3,000 per shipment, as in the 195 pricing example, the company absorbs about ₹80,246 on this shipment).

### In the news
See news box. Planning tools (TM, EWM) move freight and warehouse costs into the same planning cockpit; the e-invoicing rule applies at step 6 (see [[195 SAP SD Advanced - Pricing, Output & Document Flow]]).

### Interview angle
> [!question] How it is asked
> "Walk me through order-to-delivery in SAP with the documents created, and tell me where freight is recognised."

> [!tip] Strong answer includes
> - Sequence of documents with T-codes: VA01, VL01N, VT01N, VI01, VF01
> - Accounting entries: PGI (COGS), freight accrual, billing (revenue)
> - Compliance documents: e-invoice, e-way bill
> - Contribution analysis and corrective actions

---
## 13. ⭐ Advanced: E-Way Bill, GST and Transport Compliance in India
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Under GST rules an **e-way bill** is needed for movement of goods when the consignment value exceeds ₹50,000 (certain exemptions apply; state rules for intra-state movement vary). It is generated on the GST e-way bill portal or through API from the ERP, with **Part A** (supplier, recipient, invoice, HSN, value) and **Part B** (vehicle number or transport document). **Validity:** one day for each 200 km (or part) for normal cargo, counted from generation. **Transporters** can update Part B and consolidate bills. Generating it from **shipment completion** with the invoice's **IRN** avoids manual entry. **GTA services** attract GST under specific provisions and rates (forward or reverse charge); finance should confirm the current rate and ITC position, especially after the September 2025 rate changes (see [[227 GST & Indirect Tax for Supply Chains]]). Logistics policy context (NLP, Gati Shakti, ULIP) is in [[145 India Manufacturing & Supply Chain Policy - PLI, Gati Shakti & NLP]].

Verification of current limits and rules is needed before quoting them in a client engagement (thresholds and validity rules are amended from time to time; not re-verified for this note beyond the textbook rules).

### Example
Delhi consignment of ₹7.2 lakh (above ₹50,000) over 1,420 km: validity = ceil(1,420 / 200) = **8 days** (7.1 rounded up). If the truck leaves Pune on 4 November, the e-way bill generated on 4 November is valid until the end of the 8th day. A breakdown that causes a 10-day transit means the transporter must extend validity before expiry, otherwise penalties may apply.

### In the news
See news box for SAP's logistics suite; the India-specific compliance rule is a design requirement for every shipment process rollout.

### Interview angle
> [!question] How it is asked
> "How would you automate e-way bill generation in an SAP dispatch process?"

> [!tip] Strong answer includes
> - Trigger point (shipment completion or PGI), data sources (invoice, HSN, vehicle)
> - Integration through API or GSP, error monitoring, extension/validity handling
> - Controls: value thresholds, exemptions, transporter responsibility
> - Linking to e-invoice IRN and audit trail

---
## 14. ⭐ Advanced: Transportation KPIs and Cost-to-Serve
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Core transportation KPIs and formulas (see [[012 Supply Chain Analytics & KPIs]]):
$$\text{Cost per kg} = \frac{\text{Total freight}}{\text{Weight shipped}} \qquad \text{Utilisation} = \frac{\text{Load weight}}{\text{Vehicle capacity}}$$
$$\text{OTIF} = \frac{\text{Deliveries on time and in full}}{\text{Total deliveries}} \qquad \text{Freight as \% of sales} = \frac{\text{Freight}}{\text{Net sales}}$$
Other KPIs: **empty running** (empty km share), **detention hours**, **tender acceptance rate**, **claims rate**, **CO2 per tonne-km**, **cost per delivery**. In S/4HANA and TM these come from shipment, freight order and settlement data; BI tools aggregate them ([[085 SAP Reporting & Analytics]]). Cost-to-serve analysis assigns freight to customers, products and channels to see unprofitable drops.

### Example
Month: 400 shipments, total freight ₹3.2 crore, weight 3,600 tonnes, net sales ₹38 crore, 340 delivered OTIF. Cost per kg = 3,20,00,000 / 36,00,000 kg = **₹8.89/kg**; freight % of sales = 3.2 / 38 = **8.4%**; OTIF = 340 / 400 = **85%**. Raising average utilisation from 82% to 90% at the same volume reduces trips by 1 − 82/90 = **8.9%**, so freight saves about ₹28.4 lakh a month if cost scales with trips (assumption).

### In the news
See news box. SAP's TM suite cites emissions minimisation and multi-constraint optimisation alongside cost.

### Interview angle
> [!question] How it is asked
> "Freight is 9% of sales and rising; how do you diagnose and fix it?"

> [!tip] Strong answer includes
> - Decompose: rate, volume, utilisation, mix (FTL/LTL), expedites, detention
> - Use data from shipment and settlement documents; compare lanes and carriers
> - Levers: consolidation, tendering, mode shift, slotting and packing to raise density
> - Estimate impact with arithmetic and agree actions with owners
