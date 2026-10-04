---
tags: [product-management, tier2]
area: Product Management
topic: "Technical Understanding (APIs, SDLC)"
tier: Tier 2
roles: PM
status: complete
subtopics: 12
---
# Technical Understanding (APIs, SDLC)

⬅ [[034 Prioritization Frameworks]] · [[_Index - Product Management|Product Management]] · [[036 Go-To-Market Strategy]] ➡

> **Area:** Product Management · **Priority:** 🟠 Tier 2 · **Target roles:** PM

## Sub-topics in this note
1. [[#1. SDLC]]
2. [[#2. APIs (REST/GraphQL)]]
3. [[#3. Database Basics]]
4. [[#4. Cloud Computing Basics]]
5. [[#5. System Design Basics]]
6. [[#6. DevOps & CI/CD]]
7. [[#7. Data Pipeline Basics]]
8. [[#8. Security Basics]]
9. [[#9. Mobile Development Concepts]]
10. [[#10. AI/ML Product Concepts]]
11. [[#11. ⭐ Advanced: SLIs, SLOs and Error Budgets]]
12. [[#12. ⭐ Advanced: Build vs Buy and Technical Debt]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): two outages that explain modern software delivery and cloud risk
> **CrowdStrike (19 Jul 2024).** A faulty Falcon sensor content update (channel file 291; the validator missed a 21-vs-20 input-field mismatch) crashed about **8.5 million Windows devices**; a fix shipped in **79 minutes** but ~99% of sensors recovered only by 29 Jul. CrowdStrike then adopted a **staged "concentric rings" rollout** with customer choice (early adopter, general availability, delay) and code-release-grade testing for content. ([TechTarget](https://www.techtarget.com/whatis/feature/Explaining-the-largest-IT-outage-in-history-and-whats-next))
> 
> **AWS US-EAST-1 (19–20 Oct 2025).** A **race condition in DynamoDB's automated DNS management** produced an empty DNS record for the regional endpoint and the automation could not repair it. EC2 launches, Lambda, Fargate and Network Load Balancer were hit; AWS cited 2–3 hour impact windows but customer effects ran up to about **15 hours**. AWS disabled the DNS automation globally and added protections and rate controls. ([InfoQ](https://www.infoq.com/news/2025/11/aws-dynamodb-outage-postmortem))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. SDLC
> 🟠 Tier 2 · _Tracker hint:_ Requirements → Design → Development → Testing → Deployment → Maintenance

### Definition
The **Software Development Life Cycle** is the sequence of stages by which software moves from idea to retirement:
1. **Requirements:** business needs, user stories, acceptance criteria (PM owns the "why/what").
2. **Design:** architecture, data model, UX, API contracts.
3. **Development:** coding, code review, version control (Git).
4. **Testing:** unit, integration, system, UAT; regression; performance and security tests.
5. **Deployment:** release to production (ideally automated).
6. **Maintenance:** bugs, monitoring, upgrades, eventual sunset.

**Models:** *Waterfall* (sequential, good for fixed, regulated scope), *V-model* (tests mapped to each stage), *Iterative/Spiral* (risk-driven loops), *Agile* (Scrum/Kanban: short sprints, working software each cycle) and *DevOps* (continuous delivery with operations feedback). Cost of change rises sharply the later a defect is found, hence "shift left" (test earlier).

### Example
A bank building a loan-origination app: Waterfall for the core regulatory ledger (fixed RBI-driven specs), Scrum with 2-week sprints for the customer app, with a CI/CD pipeline pushing weekly releases.

### In the news
See news box. Both outages were failures in the *testing and deployment* stages (an unvalidated content update; an automation race condition), which is why modern SDLCs add staged rollout, canary releases and post-incident reviews.

### Interview angle
> [!question] How it is asked
> "Explain SDLC to a non-technical stakeholder" or "Waterfall vs Agile: which would you choose for this project?"

> [!tip] Strong answer includes
> - Six stages with the PM's role in each
> - Waterfall vs Agile trade-offs (certainty of scope vs adaptability)
> - Where defects are cheapest to fix (early)
> - Release strategy: staged rollout and rollback plan

---

## 2. APIs (REST/GraphQL)
> 🟠 Tier 2 · _Tracker hint:_ Request/response; endpoints; GET/POST/PUT/DELETE; JSON

### Definition
An **API (Application Programming Interface)** is a contract that lets one piece of software request data or actions from another. In **REST** over HTTP, resources are URLs (endpoints) and verbs express intent:

| Method | Purpose | Idempotent? |
|---|---|---|
| GET | Read | Yes |
| POST | Create | No |
| PUT | Replace/update fully | Yes |
| PATCH | Partial update | Usually not guaranteed |
| DELETE | Remove | Yes |

Responses carry **status codes**: 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized (not authenticated), 403 Forbidden, 404 Not Found, 429 Too Many Requests, 500 Server Error. Data is usually **JSON**.

```http
GET /api/v1/orders/1042 HTTP/1.1
Authorization: Bearer <token>

200 OK
{ "id": 1042, "status": "SHIPPED", "total": 1499.00 }
```

**GraphQL** has a single endpoint where the client specifies exactly the fields needed, avoiding over-fetching and many round trips; the trade-off is harder caching and query-cost control. Other concepts: versioning (/v1), rate limiting, pagination, webhooks (server calls you), API keys.

### Example
Razorpay or Paytm payment APIs: your app POSTs an order, receives an order ID, the customer pays, and a webhook confirms payment. A PM decides what to expose, how to version it and what rate limits apply.

### In the news
See news box. AWS's outage began at a DNS record for an API endpoint (the DynamoDB regional endpoint): when the endpoint name stopped resolving, every service calling that API failed, an example of a hidden dependency.

### Interview angle
> [!question] How it is asked
> "What is an API and how would you explain REST to a business user?" or "What happens when you tap Pay?"

> [!tip] Strong answer includes
> - Plain-language analogy (restaurant waiter: menu, order, kitchen)
> - Verbs, status codes and JSON
> - REST vs GraphQL trade-off
> - PM concerns: versioning, backward compatibility, rate limits, documentation, developer experience

---

## 3. Database Basics
> 🟠 Tier 2 · _Tracker hint:_ Relational vs NoSQL; CRUD operations; SQL join types

### Definition
**Relational (SQL) databases** (MySQL, PostgreSQL, Oracle) store data in tables with a fixed schema, keys and relationships, and guarantee **ACID** transactions (Atomicity, Consistency, Isolation, Durability): ideal for payments and inventory. **NoSQL** stores include document (MongoDB), key-value (Redis, DynamoDB), wide-column (Cassandra) and graph (Neo4j): flexible schema and horizontal scale, often with *eventual consistency* (the CAP theorem trade-off).

**CRUD** = Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).

```sql
INSERT INTO customers (id, name, city) VALUES (1, 'Asha', 'Pune');
SELECT name FROM customers WHERE city = 'Pune';
UPDATE customers SET city = 'Nashik' WHERE id = 1;
DELETE FROM customers WHERE id = 1;

-- Join: orders with customer names
SELECT c.name, o.order_id, o.amount
FROM customers c
INNER JOIN orders o ON o.customer_id = c.id;
```

| Join | Returns |
|---|---|
| INNER | Only matching rows in both tables |
| LEFT | All left rows plus matches (NULL if none) |
| RIGHT | All right rows plus matches |
| FULL OUTER | All rows from both |
| CROSS | Every combination (Cartesian product) |

Also: primary/foreign keys, indexes (faster reads, slower writes), normalisation.

### Example
Customers with no orders: `SELECT c.name FROM customers c LEFT JOIN orders o ON o.customer_id = c.id WHERE o.order_id IS NULL;`. With 100 customers and 70 having orders, INNER JOIN returns only order rows (many per customer), while this query returns the 30 inactive customers: a typical PM analytics ask.

### In the news
See news box. AWS's incident was in DynamoDB, a managed NoSQL store used as a foundational dependency by many other AWS services and customer apps: choice of data store becomes a resilience decision as well as a performance one.

### Interview angle
> [!question] How it is asked
> "SQL or NoSQL for this product?" or "Write a query to find customers who haven't ordered in 90 days."

> [!tip] Strong answer includes
> - ACID vs eventual consistency and the use case for each
> - CRUD mapping to SQL and the join types, with LEFT JOIN anti-join pattern
> - Indexes and why they matter for scale
> - Choosing by access pattern, consistency need and scale, not fashion

---

## 4. Cloud Computing Basics
> 🟠 Tier 2 · _Tracker hint:_ IaaS, PaaS, SaaS; AWS/Azure/GCP services overview

### Definition
Cloud computing delivers compute, storage and services on demand with pay-as-you-go pricing (OpEx instead of CapEx), elasticity and global reach.

| Model | You manage | Provider manages | Examples |
|---|---|---|---|
| **IaaS** | OS, runtime, apps, data | Servers, storage, network | AWS EC2, Azure VMs, Google Compute Engine |
| **PaaS** | Apps and data | Everything below | Heroku, Google App Engine, AWS Elastic Beanstalk |
| **SaaS** | Just configuration and use | Everything | Salesforce, Gmail, Zoho, Freshworks |

Core services: compute (EC2/VMs, Lambda/serverless), storage (S3, Blob), databases (RDS, DynamoDB), networking (VPC, load balancers), analytics (BigQuery, Redshift). Deployment: public, private, hybrid, multi-cloud. **Shared responsibility model:** the provider secures the cloud; you secure what you put in it (identity, data, configuration). Cost levers: right-sizing, reserved/spot instances, autoscaling, egress charges.

### Example
A D2C startup runs its web app on AWS EC2 behind a load balancer, stores images in S3, uses RDS for orders and CloudFront as CDN; scale-out on festival sale days, scale-in afterwards, paying only for what ran.

### In the news
See news box. The AWS US-EAST-1 incident showed that "the cloud" is concentrated: one region's failure affected many unrelated apps, which is why designs use multiple Availability Zones and, for critical apps, multi-region failover.

### Interview angle
> [!question] How it is asked
> "Explain IaaS/PaaS/SaaS with examples" or "Should we go multi-cloud?"

> [!tip] Strong answer includes
> - Pizza-as-a-service style analogy, correct examples
> - Cost model shift CapEx to OpEx and elasticity
> - Shared responsibility and vendor lock-in
> - Resilience patterns (multi-AZ, multi-region) vs their cost

---

## 5. System Design Basics
> 🟠 Tier 2 · _Tracker hint:_ Load balancing, caching, CDN, microservices vs monolith

### Definition
- **Load balancer:** spreads requests across servers (round-robin, least-connections); removes single points of failure via health checks.
- **Caching:** keep frequently read data in fast memory (Redis, Memcached, browser cache). Average latency $= h \cdot t_{cache} + (1-h)\cdot t_{db}$ where *h* is the hit ratio.
- **CDN:** edge servers near users serve static content (images, video, JS), cutting latency and origin load (CloudFront, Akamai, Cloudflare).
- **Monolith vs microservices:** monolith = one deployable unit (simple, fast to start, scaling is all-or-nothing); microservices = many small independently deployable services (team autonomy, independent scaling; costs: network latency, distributed debugging, data consistency).
- **Scaling:** vertical (bigger machine) vs horizontal (more machines); database replicas and sharding; message queues (Kafka, SQS) decouple producers and consumers.
- **Availability:** 99.9% allows 0.001 × 8,760 h ≈ 8.76 hours downtime per year; 99.99% ≈ 52.6 minutes per year.

### Example
A quick-commerce app serves a product catalog: with 90% cache hit, 5 ms cache and 100 ms database read, average read = 0.9×5 + 0.1×100 = **14.5 ms** instead of 100 ms; images come from a CDN; checkout is a separate service that scales during a sale.

### In the news
See news box. AWS's cascading failure (DNS, then EC2 launches, then load balancers) is the textbook "failure propagates across tightly coupled services" story, and the reason for bulkheads, rate limits and graceful degradation.

### Interview angle
> [!question] How it is asked
> "How would you design a system for 1 million users on a flash sale?" or "Monolith or microservices for our startup?"

> [!tip] Strong answer includes
> - Clarify requirements (users, read/write ratio, latency, consistency)
> - Layers: CDN, load balancer, cache, services, DB with replicas, queue
> - Honest trade-off: start monolith, split when team or scale demands
> - Failure modes and the cost of each added component

---

## 6. DevOps & CI/CD
> 🟠 Tier 2 · _Tracker hint:_ Continuous integration, continuous deployment; pipeline stages

### Definition
**DevOps** merges development and operations practices so software ships frequently and reliably. **CI (Continuous Integration):** developers merge small changes to a shared branch many times a day; each merge triggers automated build and tests. **CD:** *Continuous Delivery* = every passing build is deployable with a manual approval; *Continuous Deployment* = it goes to production automatically.

Pipeline: commit → build → unit tests → static analysis/security scan → integration tests → package (container image) → deploy to staging → smoke tests → **canary / blue-green** release → monitoring with auto-rollback. Tools: Git, Jenkins, GitHub Actions, GitLab CI, Docker, Kubernetes, Terraform (infrastructure as code).

**DORA metrics** measure delivery performance: deployment frequency, lead time for changes, change failure rate, and time to restore service. Elite teams are both fast *and* stable: speed and safety are not a trade-off when automated.

### Example
A fintech with weekly manual releases moves to CI/CD: deployments rise from 4 per month to 20 per week, change failure rate falls from 15% to 5% because each change is small and auto-tested, and rollback takes minutes using blue-green.

### In the news
See news box. CrowdStrike's fix was essentially a **delivery-pipeline change**: content updates now pass through staged rings and code-grade testing; AWS added velocity controls and protection checks to its automation.

### Interview angle
> [!question] How it is asked
> "What is CI/CD and why does a PM care?" or "How do you reduce release risk?"

> [!tip] Strong answer includes
> - CI vs continuous delivery vs deployment, accurately distinguished
> - Pipeline stages with automated gates
> - Canary/blue-green and feature flags (see [[034 Prioritization Frameworks]])
> - DORA metrics as outcome measures

---

## 7. Data Pipeline Basics
> 🟠 Tier 2 · _Tracker hint:_ ETL process; data warehouse vs data lake; batch vs streaming

### Definition
A **data pipeline** moves data from sources (app DBs, logs, SaaS tools) to where it is analysed. **ETL** = Extract, Transform, Load (transform before loading; classic warehouses); **ELT** = load raw first, transform inside the warehouse (modern cloud approach, e.g. BigQuery/Snowflake with dbt).

| | Data warehouse | Data lake |
|---|---|---|
| Data | Structured, modelled (schema-on-write) | Raw, any format (schema-on-read) |
| Users | Analysts, BI | Data scientists, ML |
| Examples | BigQuery, Redshift, Snowflake | S3/ADLS with Spark |

A **lakehouse** combines both. **Batch** processes data in scheduled chunks (nightly sales report); **streaming** processes events continuously (Kafka, Flink: fraud detection, live dashboards). Data quality needs: schema checks, deduplication, freshness SLAs, lineage, and governance (PII masking).

### Example
An e-commerce company extracts orders each night (batch), loads to BigQuery, models a daily GMV table. For fraud, payments events stream via Kafka and are scored within seconds. A PM defines "what freshness do users need": hourly is enough for revenue dashboards, seconds for fraud.

### In the news
See news box. Pipelines also fail on bad input: CrowdStrike's incident traced to a validator that missed a malformed content file, so data/config validation deserves the same rigour as code tests.

### Interview angle
> [!question] How it is asked
> "Explain ETL and the difference between a warehouse and a lake" or "Batch or streaming for this use case?"

> [!tip] Strong answer includes
> - ETL vs ELT and why ELT is common now
> - Warehouse vs lake with who uses each
> - Pick batch vs streaming by required latency and cost
> - Data quality, ownership and privacy as PM responsibilities

---

## 8. Security Basics
> 🟠 Tier 2 · _Tracker hint:_ Authentication vs authorization; OAuth; HTTPS; data encryption

### Definition
- **Authentication (AuthN):** who are you? (password, OTP, biometrics, MFA). **Authorization (AuthZ):** what may you do? (roles/permissions, least privilege). Remember: 401 = not authenticated, 403 = not authorised.
- **OAuth 2.0:** a delegation protocol that lets an app access your data on another service via a limited **access token** without sharing your password ("Sign in with Google" use of OAuth plus **OpenID Connect** for identity). Tokens often are **JWTs** with expiry and scopes.
- **HTTPS = HTTP over TLS:** encrypts data in transit and verifies the server via certificates.
- **Encryption at rest** (e.g. AES-256) protects stored data; **hashing with salt** (bcrypt/argon2) is used for passwords, never reversible encryption.
- Common threats: phishing, SQL injection, XSS, broken access control, leaked API keys, supply-chain attacks. Principles: defence in depth, least privilege, zero trust.
- Privacy and compliance: India's Digital Personal Data Protection Act, 2023 (consent, purpose limitation), RBI data-localisation norms for payments data, PCI-DSS for card data.

### Example
A fintech app: OTP plus device binding for login (AuthN), role-based limits so a support agent can view but not move money (AuthZ), card data tokenised, TLS everywhere, secrets in a vault, an access log for audits.

### In the news
See news box. CrowdStrike is a security vendor, and the outage showed that security tooling with kernel-level access is itself a risk surface: privileged software needs the strictest change control.

### Interview angle
> [!question] How it is asked
> "Difference between authentication and authorization?" or "How would you secure a payments feature?"

> [!tip] Strong answer includes
> - Crisp AuthN vs AuthZ with 401/403
> - OAuth as delegated access, tokens not passwords
> - Encryption in transit and at rest, hashing passwords
> - Privacy regulation (DPDP, RBI) and least privilege; security built in at design time

---

## 9. Mobile Development Concepts
> 🟠 Tier 2 · _Tracker hint:_ Native vs hybrid; app store submission; push notifications

### Definition
| Approach | Tech | Pros | Cons |
|---|---|---|---|
| **Native** | Kotlin/Java (Android), Swift (iOS) | Best performance, full device APIs | Two codebases |
| **Cross-platform/hybrid** | React Native, Flutter, Ionic | One codebase, faster, cheaper | Some performance and native-feature limits |
| **PWA / mobile web** | Web tech | No install, instant updates | Limited hardware access, discoverability |

**App store release:** build and sign, submit to Google Play or Apple App Store, review (Apple's review is stricter and slower; Play is faster), staged rollout percentage, then monitor crash rate and ratings. Because users update slowly, **old versions persist**, so APIs must be backward compatible and a **force-update** mechanism and **remote config/feature flags** are needed. **Push notifications** use FCM (Android) and APNs (iOS); they need user opt-in, and over-use drives uninstalls. Other concepts: offline-first, app size, low-end Android devices and patchy networks (very relevant in India), deep links.

### Example
A tier-2-city lending app trims APK size and supports offline form-saving because many users have low-end phones and weak connectivity; it uses staged rollout on Play (5%, 20%, 100%) and a feature flag to disable a failing KYC step without a store release.

### In the news
See news box. Staged rollout is built into app stores (percentage rollouts), the same ring logic CrowdStrike adopted after its outage.

### Interview angle
> [!question] How it is asked
> "Native or hybrid for our first app?" or "How do you handle a bad release on mobile?"

> [!tip] Strong answer includes
> - Trade-off table with a clear recommendation tied to stage and team
> - Store review lead time and staged rollout
> - Backward-compatible APIs, force update, kill switch
> - Push notification strategy (opt-in, relevance, frequency)

---

## 10. AI/ML Product Concepts
> 🟠 Tier 2 · _Tracker hint:_ Model training, inference, accuracy vs recall; bias in AI

### Definition
**Training** fits a model to labelled data (offline, compute-heavy); **inference** uses the trained model to predict on new inputs (online, latency- and cost-sensitive). Split data into train/validation/test to detect **overfitting** (great on training data, poor on new data). Concepts: features, labels, drift (data or concept drift degrades a model over time, so monitor and retrain).

**Classification metrics** from the confusion matrix (TP, FP, FN, TN):
- Accuracy = (TP+TN)/all
- Precision = TP/(TP+FP) ("when I flag, am I right?")
- Recall = TP/(TP+FN) ("how many real cases did I catch?")
- F1 = 2PR/(P+R)

**Accuracy misleads on imbalanced data.** Threshold choice trades precision against recall; set by cost of each error. **Bias in AI:** unrepresentative training data, proxy variables, label bias; mitigate via audits by subgroup, diverse data and human oversight. For LLMs: hallucination, prompt design, RAG (retrieval-augmented generation), evaluation sets, guardrails, cost per query.

### Example
Fraud model: 1,000 transactions, 10 fraudulent. A model that flags nothing has accuracy 990/1000 = **99%** but recall **0%**. A real model flags 12: TP = 8, FP = 4, FN = 2 → precision 8/12 = **0.667**, recall 8/10 = **0.80**, F1 = 2×0.667×0.8/(0.667+0.8) ≈ **0.727**. For fraud, a PM may favour recall; for blocking customer accounts, precision.

### In the news
> [!news] ChatGPT Go free for a year in India (announced Oct 2025, from 4 Nov 2025)
> OpenAI made its sub-$5-per-month ChatGPT Go plan free for 12 months for users in India from 4 Nov 2025; TechCrunch noted India is OpenAI's second-largest market and had 29 million ChatGPT app downloads in the 90 days before Aug 2025. Serving that many users means inference cost and latency, not training, dominate the economics. ([TechCrunch](https://techcrunch.com/2025/10/27/openai-offers-free-chatgpt-go-for-one-year-to-all-users-in-india))

### Interview angle
> [!question] How it is asked
> "Your fraud model has 99% accuracy. Is it good?" or "How would you launch an AI feature responsibly?"

> [!tip] Strong answer includes
> - Precision, recall and the imbalanced-class trap with numbers
> - Threshold decided by business cost of FP vs FN
> - Training vs inference cost, latency, monitoring for drift
> - Bias audit, human-in-the-loop, fallback when the model is unsure

---

## 11. ⭐ Advanced: SLIs, SLOs and Error Budgets
> ⭐ Advanced · _Added beyond the tracker_

### Definition
From Google's Site Reliability Engineering practice: **SLI** (indicator) = a measured quantity (request success rate, p95 latency); **SLO** (objective) = the internal target (99.9% success over 30 days); **SLA** = the customer contract with penalties (usually looser than the SLO). The **error budget** = 1 − SLO, the amount of unreliability you may "spend" on releases and experiments.

$$\text{Allowed downtime} = (1 - \text{SLO}) \times \text{period}$$

For 99.9% over 30 days: 0.001 × 43,200 min = **43.2 minutes**. If the budget is exhausted, feature releases pause and effort goes to reliability; if lots remains, ship faster. This turns the PM-vs-engineering argument (features vs stability) into a data-driven rule. Each extra "nine" is roughly 10× harder and costlier.

### Example
SLO 99.95% monthly availability for a checkout API: budget = 0.0005 × 43,200 = **21.6 minutes**. A 15-minute incident in week 1 consumes 69% of the budget; the PM defers risky launches until week 3, and prioritises a fix for the root cause.

### In the news
See news box. After a 15-hour customer impact, AWS added throttling and protection against bad DNS plans; budget-based thinking would have flagged how much reliability each dependency consumes.

### Interview angle
> [!question] How it is asked
> "How do you balance new features against reliability?"

> [!tip] Strong answer includes
> - SLI, SLO, SLA distinctions and the error-budget formula
> - Policy: freeze launches when budget is gone
> - Customer-centric SLIs (checkout success), not server uptime
> - Choosing the SLO by cost of the next nine vs business value

---

## 12. ⭐ Advanced: Build vs Buy and Technical Debt
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Build vs buy (vs partner/open source):** build when the capability is a core differentiator and you have the skills; buy when it is commodity (auth, payments, email, analytics) or time-to-market dominates. Compare **total cost of ownership** over 3–5 years: licence/usage fees, integration, maintenance, talent, switching cost and vendor risk; $\text{TCO} = \text{build cost} + \sum \text{run costs}$ vs $\text{subscription} \times \text{years} + \text{integration}$.

**Technical debt** is the future cost of shortcuts taken now (Ward Cunningham's metaphor). It carries "interest": slower delivery, more bugs. Manage it by allocating a fixed capacity share (commonly 15–20% per sprint, a rule of thumb), tracking it visibly, and tying paydown to business outcomes (cycle time, incident count). Never assume zero debt is the goal; intentional, short-lived debt can be rational.

### Example
A startup needs in-app chat: build in-house ≈ 4 engineers × 6 months (~24 person-months) plus ongoing support; buy a chat SDK at ₹X per month with 2 weeks of integration. If chat is not the core product, buy and spend the 24 person-months on the differentiating feature.

### In the news
See news box. Reliance on a few foundational cloud services and security vendors is a buy decision with concentration risk; mature teams document the failure mode of each bought dependency.

### Interview angle
> [!question] How it is asked
> "Should we build our own payments stack or use a gateway?" or "Engineering wants a sprint to pay down tech debt. Your response?"

> [!tip] Strong answer includes
> - Core vs commodity test, then TCO and time-to-market
> - Lock-in and exit plan, vendor risk
> - Treat tech debt as a visible, budgeted backlog tied to metrics
> - Decision made jointly with engineering, with a review date

---
## 🔗 Go deeper: expansion notes
- [[166 AI Product Management - LLM Products, Evals & Economics|AI Product Management - LLM Products, Evals & Economics]]
