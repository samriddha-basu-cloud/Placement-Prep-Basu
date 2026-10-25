---
tags: [machine-learning, tier2, ai, tools]
area: Machine Learning
topic: "AI Productivity Toolkit for MBA Work - Excel, SQL, Decks & Research"
tier: Tier 2
roles: All roles
status: complete
subtopics: 12
---
# AI Productivity Toolkit for MBA Work - Excel, SQL, Decks & Research

⬅ [[231 AI Industry Landscape, Economics & India AI Ecosystem]] · [[_Index - Machine Learning|Machine Learning]] · [[233 AI & ML Interview Question Bank for MBA Roles]] ➡

> **Area:** Machine Learning · **Priority:** 🟠 Tier 2 · **Target roles:** All roles

**Why this matters:** interviewers now ask "How do you use AI in your work?" and expect a concrete, responsible answer. New joiners who use AI well (and verify it) are visibly faster in their first months. This note is a practical playbook; tools change monthly, so it focuses on habits that transfer across ChatGPT, Claude, Gemini, Microsoft Copilot and similar assistants.

## Sub-topics in this note
1. [[#1. Ground Rules: Confidentiality, Verification and Disclosure]]
2. [[#2. Prompting for Business Work: The CRAFT Template]]
3. [[#3. AI for Excel: Formulas, Debugging, Agent Mode and Python]]
4. [[#4. AI for SQL and Python: Text-to-Query with Tests]]
5. [[#5. AI for Data Analysis and EDA]]
6. [[#6. AI for Slides: Storyline First, Then Pages]]
7. [[#7. AI for Research and Company Preparation]]
8. [[#8. AI as a Case and Guesstimate Sparring Partner]]
9. [[#9. AI for Behavioural and HR Interview Practice]]
10. [[#10. AI for Professional Writing: Emails, Outreach and Reports]]
11. [[#11. No-Code and Low-Code AI Analytics]]
12. [[#12. ⭐ Advanced: A Personal AI Workflow and a Portfolio Project]]

## 📰 News box
> [!news] Shared news hook for this topic (2025–2026): AI moves inside everyday office tools
> **Agent Mode in Excel generally available (early 2026).** Microsoft made Agent Mode in Excel generally available on web and Windows (Mac following), able to build workbooks, repair formulas and create charts and PivotTables, with a choice of OpenAI and Anthropic models; at that time it was not yet available in the EU or UK. ([SumProduct](https://sumproduct.com/news/agent-mode-in-excel-is-now-generally-available-on-the-desktop/))
>
> **"Shadow AI" is widespread.** MIT NANDA's 2025 *GenAI Divide* report found employees using personal AI tools without approval, which makes productivity hard to measure and creates data-leak risk. ([Computing](https://computing.co.uk/news/2025/ai/mit-report-95pc-corporate-generative-ai-pilots-fail))
>
> **India's data law applies to what you paste.** The DPDP Rules were notified on 14 Nov 2025 with phased obligations; personal data in prompts is personal data processing ([[220 Responsible AI, Explainability & Model Governance]]).
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Ground Rules: Confidentiality, Verification and Disclosure
> 🔴 Tier 1 · _Key points:_ Never paste confidential or personal data into unapproved tools; verify every number; disclose AI use where it matters; never use AI in proctored tests

### Definition
Five rules:
1. **Confidentiality:** use only company-approved tools for company data; no client names, financials, personal data or internship documents in personal accounts. Anonymise or use synthetic data for practice.
2. **Verification:** treat AI output as a draft from a fast but unreliable junior. Recompute numbers, check sources exist and say what you cite, test code and formulas on known cases.
3. **Ownership:** you are accountable for what you submit, as Air Canada found for its chatbot ([[220 Responsible AI, Explainability & Model Governance]]).
4. **Disclosure:** follow your institute's and employer's policies; disclose substantive AI help where asked (assignments, reports).
5. **Assessment integrity:** using AI during proctored online tests, coding rounds or live interviews is cheating; firms detect it (tab switches, typing patterns, follow-up questioning) and it leads to disqualification ([[234 Aptitude & Online Assessment Prep - Quant, Logical, Verbal & DI]], [[238 Placement Season Playbook - Process, Calendar, Day-of Strategy & Mock Drills]]).

### Example
During a summer internship you want help building a supplier-scorecard model. Safe: describe the structure with dummy supplier names and fake numbers in a personal tool, or use the company's approved Copilot on the real file. Unsafe: uploading the client's actual spend cube with supplier names and prices to a personal account.

### In the news
See news box. Shadow AI is exactly the unsafe pattern above at company scale.

### Interview angle
> [!question] How it is asked
> "How do you use tools like ChatGPT in your work?"

> [!tip] Strong answer includes
> - One or two specific uses with a time-saving result
> - How you verify outputs
> - Your confidentiality rule; shows judgement, not just enthusiasm

---
## 2. Prompting for Business Work: The CRAFT Template
> 🔴 Tier 1 · _Key points:_ Context, Role, Ask, Format, Tests; give examples; iterate; ask the AI to ask you questions

### Definition
**CRAFT** prompt structure:
- **C**ontext: situation, audience, data available, constraints.
- **R**ole: the expert perspective ("act as a supply chain consultant reviewing…").
- **A**sk: the specific task and the decision it supports.
- **F**ormat: length, structure (table, bullets, SCQA), tone.
- **T**ests: criteria the output must meet ("every number must come from the table I gave"; "flag assumptions"; "list what you are unsure of").

Habits: give a good example of the output you want; break big tasks into steps; ask the model to **ask clarifying questions first**; ask it to **critique its own draft against the tests**; keep a library of prompts that worked.

### Example
Weak: "Write about inventory reduction."
Strong: "**Context:** I'm an MBA intern at a tyre company; finished-goods inventory is 52 days against a 40-day target; 30% of SKUs are C-class with 70 days of cover. **Role:** act as an operations consultant. **Ask:** give five levers to reduce inventory to 40 days without hurting the 95% fill rate, with expected impact ranges. **Format:** a table with lever, mechanism, impact (days), effort, risk; then a 3-line recommendation. **Tests:** use only the numbers above, mark any assumption with 'ASSUMPTION', and tell me what data would sharpen the estimate." The second prompt gets an answer you can actually check against [[003 Inventory Management]] and [[115 Advanced Inventory Policies - EPQ, Discounts & (s,S) Systems]].

### In the news
See news box. As models improve, the quality gap between users comes more from context and verification than from prompt tricks.

### Interview angle
> [!question] How it is asked
> "How do you get good results from AI tools?"

> [!tip] Strong answer includes
> - A structure like CRAFT with a real example
> - Iteration and self-critique
> - Verification as part of the workflow

---
## 3. AI for Excel: Formulas, Debugging, Agent Mode and Python
> 🔴 Tier 1 · _Key points:_ Describe the table and the goal; test on known rows; ask for explanation; agentic features build whole sheets but still need checking

### Definition
Uses:
- **Write formulas** from plain-English specs (XLOOKUP, SUMIFS, LET, LAMBDA, dynamic arrays; [[071 Lookup & Reference Functions]], [[074 Array & Dynamic Array Functions]]).
- **Debug and explain** inherited formulas ("explain what this nested IF does, step by step").
- **Build models:** in-app agents can now create workbooks, PivotTables and charts from instructions; Python in Excel enables pandas-style analysis in the grid.
- **Power Query and VBA/Office Scripts** generation ([[075 Pivot Tables & Power Query]], [[189 VBA, Macros & Office Scripts Basics]]).

**Verification routine:** (1) specify column letters and sample rows; (2) test the formula on 3-5 rows you can compute by hand, including an edge case (blank, zero, duplicate); (3) cross-check totals with a PivotTable; (4) look for hard-coded numbers.

### Example
Prompt: "Sheet `PO` has columns A PO_No, B Vendor, C Material, D Qty, E Unit_Price, F GRN_Date, G Promised_Date. Write one formula for column H that returns 'Late' if GRN_Date > Promised_Date, 'Pending' if GRN_Date is blank and today is past Promised_Date, else 'On time'." Typical answer: `=IF(F2="",IF(TODAY()>G2,"Pending","On time"),IF(F2>G2,"Late","On time"))`. Test: row with GRN 12-Oct, promised 10-Oct → "Late" ✓; blank GRN, promised last week → "Pending" ✓; blank GRN, promised next week → "On time" ✓ (you might rename this "Open"; AI follows your spec literally, so fix the spec).

### In the news
See news box. Agent Mode makes building faster but not checking; firms still expect analysts to own the numbers.

### Interview angle
> [!question] How it is asked
> Excel round: "You may use any tools later at work, but walk me through how you'd check this model."

> [!tip] Strong answer includes
> - A testing routine (hand-computed rows, edge cases, totals reconciliation)
> - Awareness of common AI errors (wrong ranges, absolute/relative references)
> - Clear documentation of assumptions

---
## 4. AI for SQL and Python: Text-to-Query with Tests
> 🟠 Tier 2 · _Key points:_ Provide schema and sample rows; ask for comments; run on a small dataset with a known answer; watch joins and NULLs

### Definition
LLMs are strong at writing SQL and pandas code if you give the **schema** (table and column names, keys, data types) and **business definitions** ("active customer = ordered in last 90 days"). Common AI errors: wrong join keys or join type creating duplicates, mishandled NULLs, date-boundary errors, window functions without proper partitioning, and plausible column names that do not exist. See [[056 JOINs — All Types]], [[058 Window Functions]], [[181 SQL Interview Problem Bank]].

**Test protocol:** create 5-10 rows of toy data where you know the answer; run the query; check row counts before and after each join; compare totals with a trusted report.

### Example
Prompt: "Tables: `orders(order_id, customer_id, order_date, amount)`, `customers(customer_id, region)`. Write SQL for each region's revenue in Q3 2026 and the top customer by revenue in each region." A typical correct answer uses a CTE with `SUM(amount)` grouped by region and customer, then `RANK() OVER (PARTITION BY region ORDER BY revenue DESC)` and filters rank = 1. Check: does it filter `order_date >= '2026-07-01' AND order_date < '2026-10-01'` (not `<= '2026-09-30'`, which can miss same-day timestamps)? Does it return ties? Did it use INNER JOIN, silently dropping orders from customers missing in `customers`?

### In the news
See news box. Text-to-SQL inside BI tools is spreading, so the analyst's value shifts to definitions and validation.

### Interview angle
> [!question] How it is asked
> "If AI can write SQL, why should we test you on it?"

> [!tip] Strong answer includes
> - You need to read, debug and validate SQL; AI makes subtle join and date errors
> - Business definitions are the hard part
> - Show the testing habit

---
## 5. AI for Data Analysis and EDA
> 🟠 Tier 2 · _Key points:_ Use AI to generate hypotheses and code, not conclusions; recompute key statistics; beware invented patterns

### Definition
Workflow ([[186 Python Data Cleaning & EDA Playbook]]):
1. Describe the dataset and the business question.
2. Ask for an EDA plan: data quality checks, distributions, segment cuts, outliers.
3. Run the analysis (AI writes code; you run it, or an in-tool code interpreter runs it).
4. Ask for **hypotheses** explaining patterns, then **test** them with data.
5. Write conclusions yourself, with numbers you have verified.

Pitfalls: correlation presented as causation ([[214 Causal Inference & Experimentation Beyond A-B Tests]]); summary statistics hallucinated without running code; ignoring data-quality issues; overfitting a story to noise.

### Example
Dataset: 18 months of delivery data for 4,000 shipments. AI-generated EDA shows on-time delivery fell from 92% to 84% in the last quarter, and suggests "carrier B performance decline". Your check: carrier B's share of volume rose from 20% to 45% after a rate renegotiation, and its OTD was flat at 78%; the overall decline is a **mix effect**, not a performance decline. The right recommendation is about allocation, not carrier B's operations ([[125 Transportation Management Deep Dive]]).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> Analytics case: "Here is a dataset; on-time delivery fell. Why?"

> [!tip] Strong answer includes
> - Segment before concluding (mix vs rate effects)
> - Hypothesis-test loop
> - Clear separation of what data shows vs what you infer

---
## 6. AI for Slides: Storyline First, Then Pages
> 🔴 Tier 1 · _Key points:_ Answer first; action titles; one message per slide; AI drafts structure, you own the logic and numbers

### Definition
Consulting-style deck discipline ([[162 Structured Communication - SCQA, Storylines & Case Delivery]]):
1. Write the **governing thought** (the one-sentence answer).
2. Build the **storyline**: SCQA, then 3-5 key supporting messages (pyramid principle).
3. Turn messages into **action titles** (full-sentence takeaways, not topic labels).
4. Decide the evidence per slide (chart, table, framework).
5. Only then generate or format slides.

AI is useful for: turning notes into a storyline, rewriting topic titles into action titles, suggesting chart types ([[076 Charts, Dashboards & Form Controls]], [[047 MIS & Dashboard Design]]), tightening wording, and creating a speaker script. AI-generated decks tend to be generic and over-bulleted; edit hard.

### Example
Topic titles → action titles:
- "Inventory analysis" → "Finished-goods inventory is 12 days above target, driven by C-class SKUs"
- "Supplier performance" → "Three suppliers cause 60% of late deliveries; all are single-sourced"
- "Recommendations" → "Three levers cut inventory to 40 days within two quarters at no service risk"
Read only the titles in order: they should tell the whole story.

### In the news
See news box. Slide-generation features are now built into office suites; storyline quality is what still separates good analysts.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would build a deck for the CXO from this analysis."

> [!tip] Strong answer includes
> - Answer-first storyline and action titles
> - Evidence per message
> - Where AI helps and where you would not trust it

---
## 7. AI for Research and Company Preparation
> 🔴 Tier 1 · _Key points:_ Use search-grounded tools; open the sources; triangulate figures; date every fact; annual reports and earnings calls

### Definition
Company prep in about 45 minutes with AI help ([[050 Why Consulting - PM - Operations-]], sub-topic 8; [[237 Recruiter Sector Primers - FMCG, Auto, E-commerce, Manufacturing, IT-GCC & Consulting]]):
1. **Business snapshot:** segments, revenue mix, geography, key numbers from the latest annual report and investor presentation.
2. **Strategy and news:** last 12 months of announcements, capex, acquisitions, management commentary from earnings calls.
3. **Operations angle:** plants, supply chain model, distribution reach, recent disruptions or initiatives.
4. **Industry context:** growth, competitors, regulation.
5. **Your questions:** 3 smart questions for the interviewer.

Rules: prefer tools that cite sources; open and read the cited pages; triangulate figures across two sources; **record the date** of each figure; note anything unverified as "to check".

### Example
Prompt: "Using only the attached FY26 annual report and Q1 FY27 investor presentation of [company], extract: revenue by segment, EBITDA margin trend for 3 years, capex plans, number of plants and capacity, and three operations initiatives mentioned by management. Quote the page number for each figure." Then verify three random figures against the PDF.

### In the news
See news box. Search-grounded assistants reduce but do not remove hallucinated facts; page-cited extraction from primary documents is the safest pattern.

### Interview angle
> [!question] How it is asked
> "What do you know about us?" / "What is our biggest challenge right now?"

> [!tip] Strong answer includes
> - Two or three specific, dated facts from primary sources
> - An operations-relevant insight, not a Wikipedia summary
> - A thoughtful question back

---
## 8. AI as a Case and Guesstimate Sparring Partner
> 🟠 Tier 2 · _Key points:_ Interviewer prompt; force it to withhold data; rubric-based feedback; check its maths; complement, not replace, human mocks

### Definition
AI can act as a case interviewer at any hour. Set it up well:
- Give a role and rules: "You are a consulting interviewer. Give me a case prompt in [industry]. Do not reveal data until I ask for specific information. After I finish, score me 1-5 on structure, hypothesis, maths, synthesis and communication, with one improvement for each."
- Use voice mode for realistic delivery practice.
- Ask for **variants** of the same case type to practise structuring ([[025 Case Interview — Profitability]], [[027 Case Interview — Market Entry]]).
- For guesstimates, ask it to challenge your assumptions ([[102 Guesstimate Framework]]).

Limits: AI's own case data may be internally inconsistent; its numbers for India can be outdated or wrong (use [[103 Key India Data Points to Memorize]]); it is often too lenient. Human mocks with seniors remain essential for pressure and body language.

### Example
After a profitability case, the AI scores "structure 4/5: good revenue-cost split but you skipped the customer-mix branch; maths 3/5: you computed contribution margin as 22% instead of 28% (₹2.8 on ₹10)". You check its arithmetic: ₹2.8 / ₹10 = 28% ✓, so the feedback stands. Log the error type in your mock tracker ([[238 Placement Season Playbook - Process, Calendar, Day-of Strategy & Mock Drills]]).

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> Rarely asked directly; it shows up as better-structured cases. If asked "How did you prepare?", describe a mixed system: AI drills plus peer and senior mocks with tracked feedback.

> [!tip] Strong answer includes
> - Volume plus deliberate practice on weak areas
> - Feedback logs and measurable improvement
> - Human mocks for realism

---
## 9. AI for Behavioural and HR Interview Practice
> 🟠 Tier 2 · _Key points:_ Sharpen your stories, never invent them; probe-style follow-ups; authenticity check

### Definition
Uses: turn rough notes into STAR structure ([[049 STAR Stories — Leadership & Conflict]]); generate likely follow-up probes ("what would you do differently?", "what was your specific contribution?"); map stories to company values ([[176 Company-Specific Behavioural Rounds & Leadership Principles]]); tighten TMAY to 90 seconds ([[048 Tell Me About Yourself]]); practise HR and salary questions ([[178 HR Round, Offers & Salary Negotiation in India]]).

**Red lines:** never let AI invent achievements, numbers or experiences; interviewers probe two or three levels deep and fabricated detail collapses. AI-polished language that does not sound like you also hurts; read answers aloud and rewrite in your own words.

### Example
Prompt: "Here is my rough story about reducing MIS report time at my internship [notes]. Restructure it as STAR in under 150 words, keep only facts I gave you, and then ask me the five hardest follow-up questions an Amazon interviewer would ask about it." Then answer the follow-ups aloud and refine.

### In the news
See news box. Recruiters increasingly ask follow-ups designed to detect scripted, AI-generated answers.

### Interview angle
> [!question] How it is asked
> Any behavioural question, plus "Tell me more about your role in that" probes.

> [!tip] Strong answer includes
> - Specific, verifiable details only you would know
> - Your own decisions and what you learned
> - Natural delivery, not memorised AI prose

---
## 10. AI for Professional Writing: Emails, Outreach and Reports
> 🟠 Tier 2 · _Key points:_ Purpose and reader first; personalise; short; check tone and facts; never mass-send generic AI text

### Definition
Use AI to draft and edit: cold emails to alumni ([[179 Resume, LinkedIn & Cold Outreach for Placements]]), follow-ups after interviews, internship weekly updates, executive summaries. A good writing prompt states **reader, purpose, desired action, length, tone** and gives the facts. Then personalise (specific reference to the person's work), cut 30%, and check every fact. Generic AI-sounding outreach is easy to spot and often ignored.

### Example
Prompt: "Draft a 90-word LinkedIn message to a SIOM alumnus who is a category manager at a quick-commerce firm. Purpose: ask for a 15-minute call about how category managers use dark-store data. Mention that I read her post on assortment planning for Tier-2 cities. Tone: respectful, specific, no flattery. End with two time options." Then edit to sound like you.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> Indirectly: written assignments, email exercises in assessment centres, or "Draft a response to this angry customer" tasks.

> [!tip] Strong answer includes
> - Clear purpose, structure and call to action
> - Appropriate tone for the reader
> - Accurate facts and no filler

---
## 11. No-Code and Low-Code AI Analytics
> 🟡 Tier 3 · _Key points:_ AutoML, BI copilots, spreadsheet insights; fast prototypes; still need validation and leakage checks

### Definition
Tools that let non-programmers build models or insights: BI copilots that create visuals and DAX from questions ([[044 Power BI & DAX]]), spreadsheet "analyse data" features, cloud AutoML services that train and compare models automatically, and no-code workflow builders for simple agents. They are good for **quick prototypes and baselines**; the classic ML pitfalls still apply: data leakage, time-aware validation, class imbalance, metric choice ([[094 ML Fundamentals & Workflow]], [[096 Classification Algorithms]]).

### Example
An intern uses AutoML to predict late supplier deliveries and gets 94% accuracy. Checks: only 6% of deliveries are late, so predicting "never late" also scores 94%; recall on late deliveries is what matters. A feature "days_delayed" leaked the answer. After removing leakage and evaluating recall and precision, the honest model catches 61% of late deliveries at 40% precision, still useful for expediting priority, and an honest number to present.

### In the news
See news box.

### Interview angle
> [!question] How it is asked
> "You built a model with 94% accuracy. Is it good?"

> [!tip] Strong answer includes
> - Baseline comparison and class imbalance
> - Leakage and validation checks
> - Business metric and threshold choice

---
## 12. ⭐ Advanced: A Personal AI Workflow and a Portfolio Project
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Personal workflow:** keep a prompt library (CRAFT prompts for research, Excel, SQL, decks, writing); a verification checklist; a "decision log" of where AI helped or misled you. This becomes a strong interview story.

**Portfolio project (2-3 weekends)** for operations/consulting/PM profiles ([[179 Resume, LinkedIn & Cold Outreach for Placements]], sub-topic 10):
- *Option A:* "GenAI spend classifier": classify 5,000 public procurement line items (government e-procurement data) into categories using an LLM with a validation set; report accuracy, cost per 1,000 items and an error analysis ([[122 Spend Analysis, Savings & Procurement Maturity]]).
- *Option B:* "Supplier-risk news monitor": weekly digest from news headlines for 20 listed suppliers, with risk tags and human-verified examples ([[015 Supply Chain Risk & Resilience]]).
- *Option C:* "Demand forecast + agentic exception summary": public retail dataset, LightGBM forecast ([[218 Forecasting with ML & Foundation Models]]) plus an LLM-written planner summary of top exceptions.
Write it up as problem → approach → results (with numbers) → limitations → business impact; host on GitHub with a one-page README.

### Example
Resume bullet: "Built an LLM-based spend classifier for 5,000 public procurement lines (91% accuracy vs 74% keyword baseline; about ₹3 per 1,000 lines on a low-cost model); documented error analysis and human-review design." In the interview, be ready to explain the validation set, the errors, and what you would change for production.

### In the news
See news box. With AI use near-universal, demonstrated judgement (evaluation, cost, limits) differentiates candidates more than "I know ChatGPT".

### Interview angle
> [!question] How it is asked
> "Tell me about a project where you used AI." / "What's an AI tool you built or used that changed how you work?"

> [!tip] Strong answer includes
> - Problem, approach, measured result, limitations
> - Cost and evaluation, not just the demo
> - What you learned about where AI fails
