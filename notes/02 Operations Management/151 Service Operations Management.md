---
tags: [operations-management, tier1]
area: Operations Management
topic: "Service Operations Management"
tier: Tier 1
roles: Operations / Consulting / PM
status: complete
subtopics: 13
---
# Service Operations Management

⬅ [[150 Decision Analysis & Simulation]] · [[_Index - Operations Management|Operations Management]] · [[152 Learning Curves, Work Measurement & Productivity]] ➡

> **Area:** Operations Management · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / Consulting / PM

## Sub-topics in this note
1. [[#1. Service Characteristics (IHIP) and the Service Package]]
2. [[#2. Service Process Matrix (Schmenner) and Service Classification]]
3. [[#3. Service Blueprinting, Front Office and Back Office]]
4. [[#4. The Service-Profit Chain]]
5. [[#5. SERVQUAL and the Gaps Model of Service Quality]]
6. [[#6. Capacity Management in Services: Chase, Level and Demand Shaping]]
7. [[#7. Yield and Revenue Management: Littlewood's Rule and RevPAR]]
8. [[#8. Overbooking: Worked Numbers]]
9. [[#9. Self-Service, Digitisation and the Service Factory Shift]]
10. [[#10. Healthcare and Hospital Operations]]
11. [[#11. Service Failure, Recovery and the Service Recovery Paradox]]
12. [[#12. Service KPIs, SLAs and Net Promoter Score]]
13. [[#13. ⭐ Advanced: Frei's Five Variabilities and Managing Customer-Induced Variability]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): when a service runs with no slack, one shock breaks it
> **IndiGo December 2025 meltdown and the ₹22.20 crore penalty (reported January 2026).** Between 3 and 5 December 2025, IndiGo cancelled **2,507 flights** and delayed **1,852**, affecting **over 3 lakh passengers**. DGCA's order blamed "excessive operational optimisation": crew, aircraft and network were stretched to the limit, rosters had minimal recovery margins, and the new flight-duty-time rules were not implemented well. The penalty was **₹22.20 crore** (₹1.80 crore for CAR violations plus ₹20.40 crore at ₹30 lakh a day for 68 days of duty-time non-compliance), with a **₹50 crore bank guarantee** tied to reforms. A textbook case of a capacity cushion removed to raise utilisation. ([The Tribune](https://www.tribuneindia.com/news/airline-operations/dgca-imposes-rs-22-20-crore-penalty-on-indigo-over-december-2025-flight-disruption))
>
> **Max Healthcare Q1 FY27 (reported August 2026).** Operating beds **5,379**, occupancy held at about **75%** despite adding capacity, **ARPOB ₹81,900** (+5% YoY), **91,326** inpatient discharges and **10.5 lakh** outpatient consultations; gross revenue **₹2,982 crore** (+16%). Hospital economics are a capacity-and-yield game: beds are perishable inventory, ARPOB is the yield metric. ([Investing.com](https://www.investing.com/news/company-news/max-healthcare-q1-fy27-slides-revenue-jumps-16-amid-expansion-93CH-4859836))
>
> **IRCTC Tatkal rules (effective 15 July 2025).** Online Tatkal booking through the IRCTC site or app requires Aadhaar OTP authentication, and authorised agents are barred from booking opening-day Tatkal tickets in the first 30 minutes of the window (10:00-10:30 AC, 11:00-11:30 non-AC). A rule designed to ration a scarce, perishable seat inventory fairly against bots and touts. ([All India Radio News](https://www.newsonair.gov.in/aadhaar-authentication-made-mandatory-for-online-tatkal-ticket-booking-from-july-15)) For scale, IRCTC reported a daily average of about **7.31 lakh tickets** in December 2023 (as quoted on [Wikipedia](https://en.wikipedia.org/wiki/Indian_Railway_Catering_and_Tourism_Corporation)).
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Service Characteristics (IHIP) and the Service Package
> 🔴 Tier 1 · _Key points:_ Intangibility, heterogeneity, inseparability, perishability; goods-services continuum

### Definition
Services are deeds, processes and performances rather than stored objects. Four classic characteristics (the **IHIP** set):
- **Intangibility:** cannot be touched or inventoried; quality is judged on **experience and credence attributes** (search attributes are rare), so evidence management (uniforms, reports, receipts, branded environment) matters.
- **Heterogeneity:** the output varies by employee, customer and day, which makes standardisation, scripts and training the main quality levers.
- **Inseparability (simultaneity):** production and consumption happen together, the customer is **present in and co-produces** the process, so there is no finished-goods buffer between you and the customer.
- **Perishability:** an empty seat, hotel room or doctor-hour cannot be stored, so capacity is lost if unused. This is why **capacity management and yield management** are the core of service operations.

The **service package** (Fitzsimmons) bundles four elements: **supporting facility**, **facilitating goods**, **explicit services** (core benefit) and **implicit services** (psychological benefit, courtesy). Most offers sit on a **goods-services continuum**: a restaurant is part goods (food) and part service (ambience, speed). Operations differ from manufacturing in three consequences: no inventory buffer, customer participation in the process, and time-sensitive demand.

### Example
A diagnostic lab sells a blood test. Intangible: the customer cannot inspect the result before buying, so NABL accreditation and the printed report act as evidence. Heterogeneous: two phlebotomists differ in comfort and speed, so a standard sample-collection protocol is used. Inseparable: the patient must be present at collection. Perishable: a phlebotomist idle from 2 to 3 pm cannot be "stocked up" for the 9 am rush, so slots are priced and booked (₹100 off for afternoon appointments is a demand-shifting lever).

### In the news
See news box. The IndiGo case is perishability plus inseparability: a cancelled flight's seats are gone, and the passenger is physically stranded in the process.

### Interview angle
> [!question] How it is asked
> "How is managing a service operation different from managing a factory?"

> [!tip] Strong answer includes
> - IHIP with one concrete implication of each for operations
> - Customer is part of the process, so demand variability and customer behaviour are inputs you cannot buffer
> - Capacity is the substitute for inventory (link to [[018 Capacity Management & OEE]])
> - Quality judged on process as well as outcome; measure both

---

## 2. Service Process Matrix (Schmenner) and Service Classification
> 🔴 Tier 1 · _Key points:_ Labour intensity vs interaction and customisation; four service types; swift, even flow

### Definition
Schmenner's **Service Process Matrix** (1986) classifies services on two axes: **degree of labour intensity** (labour cost vs capital cost, vertical) and **degree of customer interaction and customisation** (horizontal). Four quadrants:

| | Low interaction and customisation | High interaction and customisation |
|---|---|---|
| **Low labour intensity** | **Service factory:** airlines, trucking, hotels, rail | **Service shop:** hospitals, auto repair, restaurants |
| **High labour intensity** | **Mass service:** retail banking, schools, retail stores | **Professional service:** consultants, lawyers, doctors, architects |

Managerial challenges shift with the quadrant. Factories and shops are capital-heavy: the problems are **scheduling, capacity timing, demand smoothing and capital decisions**. Mass and professional services are labour-heavy: the problems are **hiring, training, motivation, workforce scheduling and, for professional services, delivery of customisation without losing control of cost**. Moving **right** raises customisation and cost; moving **down** to mass service pushes standardisation. Schmenner's later work (2004) argued that productivity in all quadrants follows the **"swift, even flow"** principle: the faster and more evenly materials or customers flow through the process, the higher the productivity, so remove variability and bottlenecks.

### Example
A diagnostic chain wants to scale. A single-doctor clinic is a professional service. Standardising tests into protocols and adding appointment slots turns it toward a service shop, and a collection-centre network with automated analysers behaves like a service factory. Each step down and left cuts cost per patient but also removes the physician's discretion; the strategic question is where on the matrix the brand wants to sit and whether the customer will accept it.

### In the news
See news box. IndiGo is a service factory run for maximum utilisation; the penalty order shows what happens when "even flow" is attempted with no buffer to absorb a rule change.

### Interview angle
> [!question] How it is asked
> "Where would you place a private hospital and a bank branch on the service process matrix, and what does it imply?"

> [!tip] Strong answer includes
> - Both axes and the four labels placed correctly (hospital: service shop; branch: mass service)
> - Different management problems per quadrant (capital and scheduling vs workforce)
> - A concrete shift: digitising a branch pushes it towards a service factory
> - Mention that productivity improvement means reducing variability, linking to [[017 Process Management & Optimization]]

---

## 3. Service Blueprinting, Front Office and Back Office
> 🔴 Tier 1 · _Key points:_ Shostack; lines of interaction/visibility; fail points; decoupling

### Definition
A **service blueprint** (Shostack, 1984; extended by Bitner) is a process map that shows the customer journey and the organisation's actions behind it. Its lanes, from top to bottom:
1. **Physical evidence** the customer sees.
2. **Customer actions.**
3. *Line of interaction*
4. **Onstage (front-office) employee actions.**
5. *Line of visibility*
6. **Backstage (back-office) actions.**
7. *Line of internal interaction*
8. **Support processes** (IT, supply, HR, systems).

Blueprints expose **fail points**, **wait points** and **customer-induced variability**, and let the designer attach timings and tolerances to each step. **Front office** is where the customer is present (high contact, harder to standardise); **back office** is hidden (can run like a factory, batch, centralise or offshore). **Decoupling** (Chase's customer-contact model) means isolating the back office from customer variability to raise efficiency, e.g. cheque clearing centralised in one hub. The classic Chase result: potential efficiency falls as customer contact rises, so push work backstage or to self-service wherever the experience allows.

### Example
Blueprint of an online Tatkal booking. Customer actions: log in, choose train, enter passengers, pay. Onstage: web interface and payment page. Backstage: seat allocation engine, payment gateway, SMS gateway. Support: reservation database and Aadhaar OTP authentication (since July 2025). Fail points: payment timeout after the seat is locked, and the 10:00 login spike. A 60-second target for the payment step gives a measurable standard, and a retry path (re-use of locked seat for 5 minutes) is designed in.

### In the news
See news box. Aadhaar OTP and the agent exclusion window are changes to the "line of internal interaction": a control inserted into the support layer to protect the front-end experience.

### Interview angle
> [!question] How it is asked
> "A hospital's discharge process takes 5 hours. How would you analyse it?"

> [!tip] Strong answer includes
> - Draw the blueprint: patient, ward, billing, pharmacy, insurer TPA, with time at each step
> - Identify wait points and the line of visibility (what the family sees)
> - Separate customer-dependent delays from internal hand-off delays; move billing and medicines backstage in parallel
> - Quantify with a time target per step and a pilot, using tools from [[007 Lean Manufacturing]] (value stream thinking)

---

## 4. The Service-Profit Chain
> 🔴 Tier 1 · _Key points:_ Heskett et al. 1994; internal quality to loyalty to profit

### Definition
The **Service-Profit Chain** (Heskett, Jones, Loveman, Sasser, Schlesinger, *Harvard Business Review*, 1994) links internal practices to financial results in a chain of cause and effect:

**Internal service quality** (workplace, tools, selection and training, rewards) → **employee satisfaction** → **employee retention and productivity** → **external service value** → **customer satisfaction** → **customer loyalty** → **revenue growth and profitability**.

Implications for operations: frontline turnover is a cost driver, not just an HR statistic; loyalty economics (retention is cheaper than acquisition, loyal customers buy more and refer) justify investment in service capacity and empowerment; and metrics should be balanced across the chain, which is the spirit of the balanced scorecard in [[225 Budgeting, Variance Analysis & Balanced Scorecard]]. Caveat: empirical support is strongest for the employee-to-customer links and weaker for the "satisfaction to profit" step, because satisfied customers may not be loyal and loyal customers may not be profitable (hence cost-to-serve analysis, see [[138 Order Management, Customer Service & Cost-to-Serve]]).

### Example
A call centre of 200 agents has 60% annual attrition and replacement cost of ₹60,000 per agent: $200 \times 0.60 \times 60{,}000 = ₹72$ lakh a year. Cutting attrition to 40% through better tools and scheduling saves $200 \times 0.20 \times 60{,}000 = ₹24$ lakh in hiring cost alone, before counting higher first-call resolution from experienced agents.

### In the news
See news box. IndiGo's order cited management-structure shortcomings and crew rosters with no recovery margin; the internal side of the chain (crew fatigue, rostering) showed up as external service failure.

### Interview angle
> [!question] How it is asked
> "Why should a bank invest in better working conditions for branch staff? Show the business case."

> [!tip] Strong answer includes
> - Walk the chain link by link, in the order above
> - Put a number on attrition cost and the effect on customer metrics
> - Acknowledge the weak link (satisfaction does not guarantee profit)
> - Name the metrics: eNPS, attrition, first-contact resolution, customer NPS, cost-to-serve

---

## 5. SERVQUAL and the Gaps Model of Service Quality
> 🔴 Tier 1 · _Key points:_ Parasuraman-Zeithaml-Berry; five dimensions (RATER); five gaps

### Definition
Service quality is the difference between **expectations** and **perceptions**. SERVQUAL (Parasuraman, Zeithaml, Berry, 1988) uses 22 paired items rated on a 7-point scale across five dimensions, remembered as **RATER**:
- **R**eliability: perform the promised service dependably and accurately (usually the most important in studies).
- **A**ssurance: knowledge, courtesy, ability to inspire trust.
- **T**angibles: facilities, equipment, appearance.
- **E**mpathy: caring, individual attention.
- **R**esponsiveness: willingness to help, promptness.

$$\text{Gap score}_i = P_i - E_i, \qquad \text{SERVQUAL} = \frac{1}{n}\sum_{i}(P_i - E_i)$$
Negative scores mean perceptions fall short. The **Gaps Model** explains why:
1. **Gap 1 (knowledge):** management does not know customer expectations.
2. **Gap 2 (standards):** expectations are known but not translated into design and standards.
3. **Gap 3 (delivery):** standards exist but service performance falls short (people, systems, capacity).
4. **Gap 4 (communication):** promises made in marketing exceed what operations can deliver.
5. **Gap 5 (customer gap):** perceived minus expected service, the result of gaps 1 to 4.

Criticisms: the difference-score method is statistically problematic; **SERVPERF** (Cronin and Taylor) uses perceptions only and often predicts better; the five dimensions may not be stable across industries and cultures.

### Example
A bank survey gives mean expected and perceived scores (7-point) for the five dimensions: Reliability 6.5 vs 5.4, Responsiveness 6.8 vs 6.0, Assurance 6.2 vs 6.3, Empathy 6.0 vs 5.1, Tangibles 6.4 vs 6.0. Gaps: $-1.1, -0.8, +0.1, -0.9, -0.4$; mean SERVQUAL $= -0.62$. Priority is reliability (largest gap, and most valued), then empathy. If reliability issues stem from core-banking downtime, the root cause is a Gap 3 (delivery/systems) rather than a Gap 1 knowledge problem.

### In the news
See news box. IndiGo's cancellations hit reliability, the heaviest-weighted dimension; the compensation and communication debate was a responsiveness and Gap 4 issue (promised schedule vs delivered).

### Interview angle
> [!question] How it is asked
> "Customers rate our hospital's care high but complain about waiting and billing. Diagnose using a service quality model."

> [!tip] Strong answer includes
> - Five dimensions and five gaps, mapped to the symptom (waiting: responsiveness and Gap 3 capacity; billing: reliability and Gap 2 standards)
> - How to measure: SERVQUAL or SERVPERF survey plus operational data (waits, error rates)
> - Prioritise by importance times gap size
> - Link fixes to capacity, process and communication, and mention the limitations of the model

---

## 6. Capacity Management in Services: Chase, Level and Demand Shaping
> 🔴 Tier 1 · _Key points:_ Perishable capacity; utilisation vs waiting; levers on supply and demand

### Definition
Because services cannot be stocked, capacity must be matched to demand in time. Levers:
- **Supply side (chase):** part-time and flex staff, cross-training, split shifts, overtime, customer co-production, shared capacity (peak-day rentals), and technology.
- **Demand side (shape):** reservations and appointments, differential pricing (happy hour, off-peak tariff), complementary services (bar for restaurant queue), queue-management tactics, and communicating expected waits.
- **Level strategy** (constant staffing) is rare; services typically use chase or hybrid (see [[153 Aggregate Planning Models & Workforce Strategy]] for the cost table method, and [[005 Production & Operations Planning]]).

**Link to queueing:** waiting time rises non-linearly with utilisation. For a single server $W_q \propto \rho/(1-\rho)$, so a 95% utilised counter has far longer queues than a 80% one; services therefore hold a **capacity cushion** (see [[018 Capacity Management & OEE]]) and use pooled queues and triage. Psychology matters too: unoccupied time feels longer, uncertain waits feel longer than known ones, unfair waits feel longer (Maister's propositions).

### Example
A bank branch sees 30 customers/hour with an average service time of 10 minutes ($\mu = 6$ per hour per teller, offered load $a = 5$). Erlang-C results for $c$ tellers:

| Tellers $c$ | Utilisation | P(wait) | Avg wait $W_q$ |
|---|---|---|---|
| 6 | 83.3% | 58.8% | 5.9 min |
| 7 | 71.4% | 32.4% | 1.6 min |
| 8 | 62.5% | 16.7% | 0.6 min |
| 9 | 55.6% | 8.1% | 0.2 min |

Going from 6 to 7 tellers (+17% capacity) cuts the wait by about 72%. With a 2-minute wait target, 7 tellers is the answer; the 8th teller buys only 1 further minute for a full extra salary. Full formulas are in [[149 Queueing Theory & Waiting-Line Analysis]].

### In the news
See news box. IndiGo removed buffers to push utilisation up; the Dec 2025 failure is the queueing curve at $\rho \to 1$, where a small shock produces a very large backlog.

### Interview angle
> [!question] How it is asked
> "Queues at our service centre are long but staff look idle between peaks. What do you do?"

> [!tip] Strong answer includes
> - Average utilisation hides peak-hour overload: measure arrivals by 30-minute interval
> - Supply levers (flex shifts, cross-training, pooling) and demand levers (appointments, off-peak incentive)
> - Quantify with a queueing or staffing table and an explicit wait target
> - Perceived wait management (info, occupied time, fairness) as a low-cost add-on

---

## 7. Yield and Revenue Management: Littlewood's Rule and RevPAR
> 🔴 Tier 1 · _Key points:_ Perishable capacity; fare classes; protection level; RevPAR

### Definition
**Revenue (yield) management** sells the right capacity to the right customer at the right price at the right time. It works best when capacity is **fixed and perishable**, demand is **variable and segmentable**, bookings can be taken in advance, marginal cost is low and fixed cost is high (airlines, hotels, rail, cinemas, cloud capacity).

**Littlewood's rule** (two fare classes, low-fare demand arrives first): protect $y^*$ seats for the high fare $f_H$ so that

$$P(D_H > y^*) = \frac{f_L}{f_H}$$

Accept a discount booking only while the expected revenue from holding that seat for a late high-fare customer is lower than the discount fare. The generalisation to many fare classes is **EMSR** (expected marginal seat revenue). Related metrics:
- Hotels: $\text{RevPAR} = \text{Occupancy} \times \text{ADR} = \dfrac{\text{Room revenue}}{\text{Rooms available}}$
- Airlines: load factor, **RASK** (revenue per available seat-km), yield per revenue passenger km.
- Hospitals: **ARPOB** (average revenue per occupied bed per day).

### Example
Flight with 180 seats; full fare $f_H = ₹12{,}000$, discount $f_L = ₹5{,}000$; high-fare demand ~ Normal with mean 40, standard deviation 12. Critical ratio $= 5{,}000/12{,}000 = 0.4167$, so protect for the $(1 - 0.4167) = 58.3$rd percentile of $D_H$: $y^* = 40 + 0.21 \times 12 \approx 42.5$, so protect about **43 seats** for full-fare customers and sell at most $180 - 43 = 137$ seats at the discount fare. Hotel check: 120 rooms, 75% occupancy, ADR ₹4,800 gives RevPAR $= 0.75 \times 4{,}800 = ₹3{,}600$ and daily room revenue $= 120 \times 3{,}600 = ₹4.32$ lakh.

### In the news
See news box. IRCTC's Tatkal and premium-Tatkal pricing, and Max Healthcare's ARPOB discipline, are revenue management of a fixed perishable capacity; the Aadhaar and agent rules police who gets access to the premium quota.

### Interview angle
> [!question] How it is asked
> "How would you price and allocate seats on a 180-seat flight, and what is the risk of protecting too many seats?"

> [!tip] Strong answer includes
> - Fixed perishable capacity plus segmented demand as the conditions for RM
> - Littlewood's ratio with a numeric protection level
> - Cost of spill (empty protected seats) vs cost of dilution (selling cheap seats that high-fare customers would have bought)
> - Fairness and brand risk (surge pricing complaints), and data needs: booking curves, cancellations, forecasts per [[004 Demand Forecasting & Planning]]

---

## 8. Overbooking: Worked Numbers
> 🔴 Tier 1 · _Key points:_ No-show rate; binomial; critical ratio; denied-boarding cost

### Definition
Overbooking sells more reservations than capacity to offset no-shows and late cancellations. Let capacity $C$, bookings $n$, show-up probability $p$ per booking, so shows $S \sim \text{Binomial}(n, p)$. Let $F$ be the revenue per flown customer and $D$ the full cost per bumped customer (compensation, rebooking, goodwill). Adding one more booking is worth it while

$$P(S_n \ge C) < \frac{F}{F + D}$$

where $S_n$ is the number of shows among the current bookings. The rule is a newsvendor in disguise (see [[003 Inventory Management]] for the critical-ratio logic): too few bookings leave empty seats; too many create bumped customers.

In India, DGCA's rules require airlines to seek volunteers first and compensate involuntarily denied passengers; as reported by [Wego](https://blog.wego.com/dgca-passenger-rights/) and [HappyFares](https://www.happyfares.in/blog/denied-boarding-overbooking-rights-india-2026/) the caps are about **₹10,000 if an alternative flight is within 24 hours and ₹20,000 beyond that** (200% and 400% of the one-way base fare plus fuel charge). Check the current DGCA Civil Aviation Requirement (CAR) before quoting rates in an interview.

### Example
180 seats, show-up probability $p = 0.92$, $F = ₹6{,}000$, $D = ₹15{,}000$ (cash compensation plus goodwill). Critical ratio $= 6{,}000/21{,}000 = 0.286$. Expected values (binomial):

| Bookings $n$ | Expected flown | Expected bumped | Expected profit (₹) |
|---|---|---|---|
| 180 | 165.60 | 0.000 | 9,93,600 |
| 188 | 172.94 | 0.023 | 10,37,277 |
| 190 | 174.69 | 0.106 | 10,46,581 |
| 192 | 176.30 | 0.341 | 10,52,686 |
| **193** | **177.01** | **0.551** | **10,53,799** |
| 194 | 177.64 | 0.839 | 10,53,267 |
| 196 | 178.64 | 1.677 | 10,46,697 |
| 199 | 179.52 | 3.562 | 10,23,679 |

The optimum is to book **193** passengers: expected profit rises by about ₹60,200 (+6.1%) over no overbooking, with about 0.55 expected bumped passengers per flight. If compensation $D$ doubles to ₹30,000 the ratio falls to $6{,}000/36{,}000 = 0.167$ and the optimal overbooking shrinks, which is why airlines overbook more on routes with frequent alternatives.

### In the news
See news box. After the December 2025 disruption, DGCA's order signalled that regulators will price service failure heavily; denied-boarding and cancellation compensation raise $D$ and reduce optimal overbooking.

### Interview angle
> [!question] How it is asked
> "An airline sees 8% no-shows on a 180-seat aircraft. How many tickets should it sell?"

> [!tip] Strong answer includes
> - Naive answer: $180/0.92 \approx 196$; why that is too aggressive (it ignores the asymmetric cost of bumping)
> - Marginal logic: compare cost of an empty seat (lost fare) vs cost of a bumped passenger
> - Binomial or normal approximation for shows, and sensitivity to $p$ and $D$
> - Ethics and regulation: volunteers first, compensation rules, brand damage

---

## 9. Self-Service, Digitisation and the Service Factory Shift
> 🔴 Tier 1 · _Key points:_ Customer as co-producer; cost-to-serve; digital failure modes

### Definition
**Self-service** transfers work to the customer (ATMs, web check-in, UPI, kiosks, quick commerce apps). Operations logic:
- **Decoupling and standardisation:** repetitive transactions move to a low-variability, low-cost channel; human capacity is reserved for exceptions.
- **Cost-to-serve:** a digital transaction costs a fraction of an assisted one, but the saving only materialises if the channel works and customers adopt it.
- **Co-production risks:** customer error, abandonment, and loss of the recovery opportunity that human contact provides. Digital channels also fail **in bulk**: one outage affects everyone at once, so resilience, load testing and graceful degradation (queues, waiting rooms, fallback to counters) are design requirements.
- **Omnichannel integration:** same data across app, branch and call centre; one customer, one history.

Technology levers: automation and bots, workflow engines, appointment systems, real-time dashboards (see [[047 MIS & Dashboard Design]]), and process mining (see [[173 Process Mining & Operations Intelligence]]).

### Example
A bank branch handles 1,200 assisted transactions a day at ₹45 each (staff, premises) and an ATM or app transaction costs ₹8. Shifting 60% of volume digital saves $1{,}200 \times 0.60 \times (45 - 8) = ₹26{,}640$ a day, about ₹80 lakh a year on 300 working days ($26{,}640 \times 300 = ₹79.9$ lakh). Counter-check: if a 2% failed-transaction rate sends 5% of those users back to a counter at a cost of ₹60 per recovery, the annual leakage is a small fraction of the saving, so the business case holds; the risk is the reputational tail, not the average.

### In the news
See news box. IRCTC runs a very large concurrent-demand digital service; the Tatkal rule changes are service-design changes to control who competes for scarce inventory in the opening minutes.

### Interview angle
> [!question] How it is asked
> "A bank wants to move 70% of branch transactions to digital. What are the operational risks?"

> [!tip] Strong answer includes
> - Savings logic (cost per transaction by channel) with numbers
> - Adoption barriers, accessibility and the need for assisted channels
> - Concentration risk: peak load, outages, fraud; fallback design
> - Metrics: digital adoption, failure rate, first-contact resolution, cost-to-serve

---

## 10. Healthcare and Hospital Operations
> 🔴 Tier 1 · _Key points:_ Bed capacity, ALOS, occupancy, ARPOB, OPD flow, triage

### Definition
A hospital is a **service shop** with several linked flows: outpatient (OPD) clinics, emergency, inpatient wards and ICU, operation theatres (OT), diagnostics, pharmacy and billing. Key operational metrics:
- **Occupancy:** $\text{Occupancy} = \dfrac{\text{Occupied bed-days}}{\text{Available bed-days}}$
- **ALOS:** average length of stay, $= \dfrac{\text{Total bed-days}}{\text{Discharges}}$
- **Bed turnover rate** $= \text{Discharges}/\text{Beds}$ per period
- **ARPOB:** revenue per occupied bed per day, the headline yield measure of Indian listed hospitals; **ARPP** is revenue per patient. Because $\text{Revenue} \approx \text{Occupied bed-days} \times \text{ARPOB}$, growth comes from higher occupancy, a richer case mix or higher tariffs; shorter ALOS raises throughput but lowers occupied bed-days per patient.

Little's Law links flows to stock: $L = \lambda W$, so average census $=$ admissions per day $\times$ ALOS. Operational levers: OT scheduling, discharge-before-noon, bed management (control tower), triage and fast-track in emergency, appointment smoothing in OPD, and the **bottleneck** (often OT, ICU beds or radiology). Pushing occupancy beyond roughly 85% raises the risk of blocked emergency admissions (the queueing effect again).

### Example
A hospital admits 50 patients a day with ALOS 4.2 days. Census $= 50 \times 4.2 = 210$ occupied beds. To run at 85% occupancy it needs $210/0.85 = 247$ beds; at 95% only 221 beds, but with little cushion for surges. Reality check with Max Healthcare's figures: $5{,}379 \times 0.75 \approx 4{,}034$ occupied beds; over a 91-day quarter at ARPOB ₹81,900 that gives $4{,}034 \times 91 \times 81{,}900 \approx ₹3{,}007$ crore, close to reported gross revenue of ₹2,982 crore (the gap is rounding in occupancy and the fact that some revenue is OPD). Implied ALOS $= 4{,}034 \times 91/91{,}326 \approx 4.0$ days (an estimate, not a disclosed figure).

### In the news
See news box. Max's occupancy held at about 75% while beds expanded, a sign that new capacity is being filled; ARPOB growth of 5% is the yield side of the same story.

### Interview angle
> [!question] How it is asked
> "How would you reduce OT idle time and patient waiting at a 500-bed hospital?"

> [!tip] Strong answer includes
> - Find the bottleneck (OT, ICU, diagnostics) with data on utilisation and queues
> - Levers: block scheduling by specialty, turnaround time reduction (SMED-style, see [[007 Lean Manufacturing]]), discharge planning, pre-admission testing
> - Numbers: occupancy, ALOS, ARPOB, and the trade-off of running above 85% occupancy
> - Patient safety and clinical quality as constraints, not afterthoughts

---

## 11. Service Failure, Recovery and the Service Recovery Paradox
> 🔴 Tier 1 · _Key points:_ Recovery as a second chance; paradox is conditional; fairness; recovery cost

### Definition
A **service failure** is inevitable in heterogeneous, inseparable services; **service recovery** is the organisation's response. Effective recovery has: a clear way to complain, speed (acknowledge fast), empathy and apology, fair outcome (distributive, procedural and interactional justice), and **root-cause correction** so the same failure does not recur.

The **service recovery paradox** (McCollough and Bharadwaj, 1992) is the claim that customers who experienced a failure and a **very good recovery** can be more satisfied or loyal than customers who never had a failure. The research evidence is mixed: reviews (for example Magnini, Ford, Markowski and Honeycutt, 2007) find it appears only under conditions: low severity of failure, first failure (not repeated), failure not caused by controllable or stable factors, and an outstanding recovery. Do not plan to fail deliberately; the paradox is an upside, not a strategy.

**Recovery economics:** if the cost of recovery per failure is $c_r$ and the lifetime value of a retained customer is $LTV$, recovery pays when retention probability gain $\times\, LTV > c_r$.

### Example
An airline cancels 1,000 bookings. Compensation and rebooking cost ₹4,500 per passenger ($4.5$ million total). Without good recovery 30% of affected customers defect; with good recovery 12% defect. Customer lifetime value is ₹40,000. Customers retained by recovery $= 1{,}000 \times (0.30 - 0.12) = 180$, worth $180 \times 40{,}000 = ₹72$ lakh versus ₹45 lakh cost, a net gain of ₹27 lakh. Break-even defect reduction $= 4{,}500/40{,}000 = 11.25$ percentage points.

### In the news
See news box. IndiGo's penalty included a bank guarantee released in phases against verified reforms: regulators now require evidence of root-cause recovery, not only refunds.

### Interview angle
> [!question] How it is asked
> "A key customer received a faulty delivery and is angry. How do you recover, and is it worth the cost?"

> [!tip] Strong answer includes
> - Sequence: apologise, fix, compensate fairly, prevent recurrence
> - Mention the service recovery paradox and its conditions, without relying on it
> - Compare recovery cost with customer lifetime value
> - Capture failure data and feed it into the process (Gap analysis from SERVQUAL, [[011 Quality Management (TQM)]])

---

## 12. Service KPIs, SLAs and Net Promoter Score
> 🔴 Tier 1 · _Key points:_ Operational + perception metrics; NPS, CSAT, CES; SLA design

### Definition
Service performance needs both **process metrics** and **perception metrics**:
- **Operational:** service level (% calls answered within 20 seconds), average speed of answer, abandonment rate, average handle time, first-contact resolution (FCR), on-time performance, turnaround time, right-first-time, utilisation, cost per transaction.
- **Perception:** **CSAT** (satisfaction with an interaction), **CES** (customer effort score), and **NPS**.
- **NPS** (Reichheld, 2003): "How likely are you to recommend us?" on a 0-10 scale. Promoters 9-10, passives 7-8, detractors 0-6.

$$NPS = \%\text{Promoters} - \%\text{Detractors} \quad (\text{range } -100 \text{ to } +100)$$

An **SLA** (service level agreement) converts expectations into measurable targets (e.g. 90% of tickets resolved in 24 hours) with credits or penalties. Pitfalls: gaming (closing tickets early), measuring the average rather than the tail (95th percentile), and optimising a metric against the customer's real goal (low AHT but low FCR). See [[031 Product Metrics & Analytics]] for how product teams use NPS and CSAT, and [[012 Supply Chain Analytics & KPIs]] for operational KPIs.

### Example
A survey of 400 customers: 208 score 9-10, 120 score 7-8, 72 score 0-6. Promoters $= 52\%$, detractors $= 18\%$, so $NPS = 52 - 18 = +34$. Call centre: 12,000 calls in a month, 9,480 answered within 20 seconds, 600 abandoned: service level $= 9{,}480/12{,}000 = 79\%$, abandonment $= 600/12{,}000 = 5\%$. If the target is 80/20 service level, the centre is 1 point short; each added agent-hour on the peak interval is the lever.

### In the news
See news box. After the December 2025 disruption, DGCA's order tied reform bank guarantees to verified performance, a regulator-imposed SLA with a financial penalty.

### Interview angle
> [!question] How it is asked
> "Which KPIs would you track for a hospital outpatient department, and why NPS alone is not enough?"

> [!tip] Strong answer includes
> - A balanced set: wait time (95th percentile), consult time, no-show rate, FCR or repeat visits, CSAT and NPS
> - NPS formula, thresholds and its limits (cultural bias, no root cause; pair with driver analysis)
> - Targets with tails, not only averages
> - Link each KPI to a lever and an owner

---

## 13. ⭐ Advanced: Frei's Five Variabilities and Managing Customer-Induced Variability
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Frances Frei (*Harvard Business Review*, 2006) argued that service operations differ from manufacturing mainly because **customers introduce variability** that cannot be removed upstream. She identified five types:
1. **Arrival variability:** when customers show up (peaks).
2. **Request variability:** what they ask for.
3. **Capability variability:** how well they can perform their part.
4. **Effort variability:** how much work they are willing to do.
5. **Subjective preference variability:** what each regards as good service.

Two broad responses: **accommodation** (absorb the variability with flexible capacity, at higher cost) or **reduction** (steer customers: reservations, menus, training, defaults, price incentives). Firms choose a point on the cost-quality trade-off consistently with their strategy: a low-cost carrier reduces variability (fixed menu, self-check-in), a premium hotel accommodates it.

This links to the service process matrix: the further right on customisation, the more variability must be accommodated. It also connects to [[017 Process Management & Optimization]]: variability is the root cause of waiting and buffer needs in every process.

### Example
A hospital OPD sees patients arrive mostly at 9-11 am (arrival variability). Reduction: appointment slots with a 15-minute stagger and a ₹100 discount on afternoon diagnostics. Accommodation: two floating nurses and a fast-track desk 9-11 am. Suppose peak-hour demand is 60 patients against a 40-patient capacity per hour. Moving 25% of peak patients (15) to off-peak slots brings peak demand to 45, and adding a floating nurse who raises capacity to 48/hour closes the gap with a cost far below running that nurse all day.

### In the news
See news box. Tatkal opening is an extreme case of arrival variability: all demand arrives at 10:00 and 11:00, so policy tools (authentication, agent windows) reduce variability by limiting who can arrive.

### Interview angle
> [!question] How it is asked
> "Why is it harder to improve efficiency in a service than a factory, and what can you do about it?"

> [!tip] Strong answer includes
> - Customer-induced variability with the five types and an example of each
> - Accommodation vs reduction as an explicit choice tied to strategy
> - Quantified example showing a demand-shifting lever vs adding capacity
> - Caution about customer fairness and experience when reducing variability
