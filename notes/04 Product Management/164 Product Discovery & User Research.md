---
tags: [product-management, tier2]
area: Product Management
topic: "Product Discovery & User Research"
tier: Tier 2
roles: Product Manager
status: complete
subtopics: 13
---
# Product Discovery & User Research

⬅ [[163 PM Interview Types & Answer Frameworks]] · [[_Index - Product Management|Product Management]] · [[165 Platform & Marketplace Product Strategy]] ➡

> **Area:** Product Management · **Priority:** 🟠 Tier 2 · **Target roles:** Product Manager

## Sub-topics in this note
1. [[#1. Discovery vs Delivery and Dual-Track Agile]]
2. [[#2. Continuous Discovery Habits (Teresa Torres)]]
3. [[#3. Opportunity Solution Trees]]
4. [[#4. Customer Interview Technique and the Mom Test]]
5. [[#5. Story-Based Interviewing and JTBD (Switch) Interviews]]
6. [[#6. Surveys and Bias]]
7. [[#7. Sample Sizes in Discovery]]
8. [[#8. Usability Testing vs Concept Testing]]
9. [[#9. Assumption Mapping and Prioritising What to Test]]
10. [[#10. Discovery Experiments: Fake Door, Concierge, Wizard of Oz]]
11. [[#11. Synthesising Insights: Affinity Maps and Evidence]]
12. [[#12. Discovery for B2B and Operations Products]]
13. [[#13. ⭐ Advanced: Decision Rules, Evidence Quality and Discovery Debt]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI is entering the research workflow faster than trust in it
> **State of User Research 2025 (User Interviews, survey fielded 25 July – 9 August 2025).** Of **485 researchers** surveyed, **80% now use AI tools**, a 24-point rise on the previous year, yet **91% worry about accuracy and hallucinations** and 41% say AI's current effect on UX research is negative (32% positive). The same report notes a median output of 2 mixed-method, 3 qualitative and 1 quantitative study per six months, i.e. research capacity is thin, which is exactly why PMs are expected to run their own weekly discovery. ([User Interviews](https://www.userinterviews.com/state-of-user-research-report))
>
> **The Future of User Research 2025 (Maze, 800 product professionals, Dec 2024 – Jan 2025).** **55%** reported rising demand for research over the previous year and **63%** named time and bandwidth as the top constraint; **58%** reported using AI tools, commonly for analysing research data and transcription. Only about 7% of respondents were product managers, so PM-led discovery still leans on the researchers and designers around the PM. ([Maze](https://maze.co/resources/user-research-report-2025/))
>
> **Evergreen anchor: the "5 users" rule is from the year 2000.** Nielsen Norman Group's classic article (18 March 2000) argued that 5 test users surface about 85% of usability problems and that three small rounds beat one large study; its later guidance still recommends 5 for most qualitative studies and about 20+ for quantitative ones. ([NN/g](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/), [NN/g how many users](https://www.nngroup.com/articles/how-many-test-users/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Discovery vs Delivery and Dual-Track Agile
> 🟠 Tier 2 · _Key points:_ Build the right thing vs build the thing right; two parallel tracks; product trio

### Definition
**Product discovery** is the work of deciding *what* to build: finding customer problems worth solving and checking that a solution is **valuable** (customers want it), **usable**, **feasible** (engineering can build it) and **viable** (the business can sustain it). These are Marty Cagan's four product risks. **Delivery** is building, testing and shipping the chosen solution well. The classic failure is "build trap": a roadmap of outputs (features shipped) with no evidence of outcomes (behaviour changed).

**Dual-track agile** (popularised by Jeff Patton and Marty Cagan) runs two tracks at once, sharing one team:

| | Discovery track | Delivery track |
|---|---|---|
| Question | Should we build it? What exactly? | How do we build it well? |
| Output | Validated learning, prototypes, ranked opportunities | Working, shipped, measured software |
| Cadence | Continuous, small experiments each week | Sprints / releases, see [[032 Agile & Scrum Framework]] |
| Risk reduced | Value, usability, viability | Feasibility, quality, delivery |

Discovery runs **ahead of** delivery by one to two sprints: items enter the sprint backlog only after the key assumptions are tested. It is not a separate "research team" handing over a spec; engineers participate in discovery because they spot feasibility traps early. Discovery effort is scaled to risk: a button colour change needs no discovery, a new product line needs a lot.

### Example
A freight-aggregator app team wants to add "instant truck booking". Discovery track (2 weeks): 8 transporter interviews, 3 prototype tests, a fake-door button measuring tap rate. Delivery track meanwhile ships last sprint's validated "document upload" improvement. Only after prototypes show transporters accept a fixed price will "instant booking" enter a sprint. If the fake door gets under 1% taps, the feature is dropped at a cost of two weeks, not two quarters (compare [[030 Product Fundamentals & Strategy]]).

### In the news
See news box. The Maze and User Interviews data show research demand outrunning capacity, which is why discovery is becoming a daily PM habit rather than a specialist project.

### Interview angle
> [!question] How it is asked
> "How do you decide what to build, and how do you avoid shipping features nobody uses?"

> [!tip] Strong answer includes
> - The four risks (value, usability, feasibility, viability) and which one you test first
> - Dual track: discovery stays 1-2 sprints ahead of delivery, with engineers in the loop
> - Scaling effort to risk and cost, not "research everything"
> - An outcome metric you commit to, with a kill decision if experiments fail

---

## 2. Continuous Discovery Habits (Teresa Torres)
> 🟠 Tier 2 · _Key points:_ Weekly touchpoints, product trio, outcome-led, small research activities

### Definition
Teresa Torres's *Continuous Discovery Habits* defines **continuous discovery** as: at a minimum, **weekly touchpoints with customers, by the team that is building the product, where they run small research activities in pursuit of a desired outcome**. Core ideas:

- **Product trio:** the PM, a designer and a software engineer make discovery decisions together, replacing hand-offs.
- **Outcome over output:** the team is given a measurable **product outcome** (a behaviour change such as "increase weekly repeat orders from kirana retailers"), not a feature list. See [[031 Product Metrics & Analytics]] and [[225 Budgeting, Variance Analysis & Balanced Scorecard|balanced scorecard]] for linking outcomes to business results.
- **Habits not projects:** interview every week (ideally automated recruiting), map what you learn on an opportunity solution tree, test assumptions in days, not months.
- **Compare and contrast:** never evaluate a single idea (whether-or-not decisions are made badly); generate at least three solutions per opportunity and choose among them.
- **Interview snapshots:** a one-page record per interview (key quote, opportunities heard, insight) so learning is shareable and not trapped in one head.

Torres's weekly rhythm: one or two customer interviews, one assumption test in flight, the tree updated, and a decision recorded. The smallest unit of discovery is a **touchpoint**, not a study.

### Example
A B2B logistics SaaS team (outcome: reduce average invoice-dispute resolution time from 9 to 5 days). Their automated recruiting pipeline books 2 customer calls per week. Over 6 weeks: 12 interviews, 4 assumption tests, two solutions killed, one shipped behind a flag. Cost: roughly 2 hours per team member per week, far less than a quarterly research project.

### In the news
See news box. Tooling for transcription and clustering lowers the cost of weekly touchpoints, but the human discipline of interviewing remains the bottleneck.

### Interview angle
> [!question] How it is asked
> "How do you stay in touch with customers while shipping every sprint?"

> [!tip] Strong answer includes
> - Weekly cadence by the whole trio, not by an outsourced research team
> - Starting from an outcome, then opportunities, not from a feature
> - Generating multiple solutions and testing assumptions, not ideas
> - Honest limits: some products (B2B, regulated) need creative recruiting

---

## 3. Opportunity Solution Trees
> 🟠 Tier 2 · _Key points:_ Outcome → opportunities → solutions → assumption tests; one target at a time

### Definition
An **opportunity solution tree (OST)** is a visual map that connects the outcome to the customer needs that could move it, to solutions, to the experiments that test them. Four layers:

1. **Outcome** (top): one measurable product outcome the team owns.
2. **Opportunities:** customer needs, pain points and desires, phrased from the customer's view ("I cannot tell if my truck will reach on time"), never as solutions ("add tracking"). Large opportunities are broken into smaller, child opportunities.
3. **Solutions:** several ideas per chosen opportunity.
4. **Assumption tests:** the smallest experiments that test the riskiest assumptions behind each solution.

Rules of the tree: opportunities come **from interviews and data** not brainstorms; each opportunity should be distinct (no overlap) so the tree can be pruned; the team **picks one target opportunity** at a time, comparing a few using a simple criterion such as market size, customer importance, company fit and differentiation; solutions are only discussed after the opportunity is chosen. Compare with the [[034 Prioritization Frameworks]] (RICE, MoSCoW), which rank *solutions*: the tree first ranks *problems*.

### Example
Outcome: increase weekly active suppliers on a procurement portal from 4,000 to 5,500 in two quarters.

| Opportunity (interview-sourced) | Interviews citing | Severity (1-5) | Frequency × severity |
|---|---|---|---|
| Cannot see PO status without phoning buyer | 7 of 12 | 4 | 28 |
| Invoice rejections unexplained | 4 of 12 | 5 | 20 |
| Rate-card updates via WhatsApp, lost | 9 of 12 | 2 | 18 |
| Manual proof-of-delivery upload | 5 of 12 | 3 | 15 |

The frequency × severity score is ranked: PO status (7 × 4 = 28) wins and becomes the target opportunity. Three solutions are generated: PO status tracker, WhatsApp bot, weekly email digest. Riskiest assumption of the tracker: "suppliers will log in to check", tested with a fake door.

### In the news
See news box. AI clustering of interview transcripts can propose opportunity candidates, but the PM must still validate they trace back to real customer quotes.

### Interview angle
> [!question] How it is asked
> "You are the PM for [app]. Our goal is to improve retention. Where do you start?"

> [!tip] Strong answer includes
> - Restating the goal as a measurable outcome, then mapping opportunities (not solutions)
> - Evidence for each opportunity (interviews, funnel data, support tickets)
> - Choosing one target by explicit criteria, then 3+ solutions
> - An assumption test per solution before building

---

## 4. Customer Interview Technique and the Mom Test
> 🟠 Tier 2 · _Key points:_ Past behaviour, specifics, no pitching; compliments, fluff and ideas are bad data

### Definition
Rob Fitzpatrick's *The Mom Test* is built on the idea that even your mother will lie to protect your feelings; the fix is to ask questions that cannot be answered politely. Rules:

1. **Talk about their life, not your idea.**
2. **Ask about specifics in the past, not generics or opinions about the future.**
3. **Talk less, listen more.**

Three kinds of **bad data**: **compliments** ("great idea!"), **fluff** (generics "I usually...", future promises "I would definitely buy", hypotheticals "I might"), and **ideas** (feature requests, which hide the underlying problem). Good data is **facts and commitments**: money, time or reputation put at stake (a pilot, an introduction, a signed letter of intent, a pre-order).

| Bad question | Why bad | Better question |
|---|---|---|
| "Would you use an app that tracks your trucks?" | Hypothetical, leading | "Talk me through the last time a delivery was late. What did you do?" |
| "How much would you pay?" | Opinion, unreliable | "What are you spending now on this problem (money, hours)?" |
| "Do you think this is a good idea?" | Invites compliments | "What else have you tried? Why did that not work?" |
| "We will add a dashboard, right?" (feature request) | Solution-first | "Why do you want that? What would it let you do?" |

Interview mechanics: 30-45 minutes, one interviewer plus one note-taker, recorded with consent, open the call with context not pitch, follow the story with "what happened next?", close with "who else should I talk to?" and ask for a next step (commitment). Watch for **confirmation bias**: you hear what you hoped to hear.

### Example
A founder pitches "WhatsApp-based ordering for kirana owners". Weak: "Would you use it?" → "Sure, sounds useful" (compliment). Strong: "Tell me about the last time you ran out of stock of a fast-moving item." → "Last Tuesday, I phoned my distributor's salesman three times; he did not pick up; I lost about ₹2,000 of sales." The second answer gives a specific, a cost and a current workaround (phoning), all of which are evidence of a real problem. A **commitment** test follows: "Can I come to your shop Saturday and watch you place the order?"

### In the news
See news box. Researchers' top worry (hallucinated or misread transcripts) is why raw quotes and recordings, not AI summaries, should anchor discovery decisions.

### Interview angle
> [!question] How it is asked
> "Role-play: interview me as a small-shop owner to find out if a stock-ordering app is a good idea."

> [!tip] Strong answer includes
> - Opens with their routine and last-time stories, never pitches
> - Digs for cost, frequency, workaround and who decides
> - Distinguishes compliments/fluff from commitments
> - Ends with a next step, referral and a clear learning goal

---

## 5. Story-Based Interviewing and JTBD (Switch) Interviews
> 🟠 Tier 2 · _Key points:_ Jobs to be done; push, pull, anxiety, habit; timeline of the switch

### Definition
**Jobs to be Done (JTBD)** treats a purchase as "hiring" a product to make progress in a circumstance: people do not want a quarter-inch drill, they want a hole. The job has functional, emotional and social dimensions. **Switch interviews** (Bob Moesta, Chris Spiek and the Re-Wired Group, building on Clayton Christensen's work) reconstruct a recent real purchase or switch on a **timeline**:

First thought → passive looking → active looking → deciding → first use → ongoing use.

At each step identify the **four forces** of progress:

| Force | Direction | Question to probe |
|---|---|---|
| **Push** of the situation | Toward change | What was going wrong with the old way? |
| **Pull** of the new solution | Toward change | What attracted you to the new product? |
| **Anxiety** about the new | Against change | What worried you about switching? |
| **Habit** of the present | Against change | What kept you with the old way? |

Switch happens when push plus pull exceed anxiety plus habit. Torres's **story-based interviewing** is the same discipline in discovery: "Tell me about the last time you ..." and collect the whole story, the context and the alternatives, instead of asking about preferences. Recruit people who **switched recently** (memory is fresh) and also those who considered but did not switch.

### Example
Interviewing 10 small businesses that moved from Excel/Tally billing to a cloud GST invoicing app. Push: GST return mismatches at month-end. Pull: automatic GSTR-1 data entry (see [[227 GST & Indirect Tax for Supply Chains]]). Anxiety: "Will my accountant accept it? Is my data safe?" Habit: accountant and staff already trained on Tally. Insight: the barrier is not features but the accountant's buy-in, so the product adds an **accountant invite with read-only access** and an import from Tally. Onboarding messaging targets the accountant, not just the owner.

### In the news
See news box. JTBD interviews are labour-intensive; AI-moderated interviews can scale volume but struggle with probing the emotional "anxiety" forces, so many teams keep the key switch interviews human-led.

### Interview angle
> [!question] How it is asked
> "Why do users choose our product over a competitor, and how would you find out?"

> [!tip] Strong answer includes
> - Job framed as progress in a circumstance, not a demographic
> - Timeline plus the four forces (push, pull, anxiety, habit)
> - Interviewing recent switchers and non-switchers
> - A concrete product or messaging change driven by anxiety or habit

---

## 6. Surveys and Bias
> 🟠 Tier 2 · _Key points:_ Surveys size patterns, interviews find them; sampling, wording, non-response bias

### Definition
**Interviews discover** (what problems exist); **surveys quantify** (how many people have each problem, how severe). Use surveys *after* qualitative work, once you can write closed questions that match the customer's own language. Common biases:

| Bias | What goes wrong | Mitigation |
|---|---|---|
| **Selection / sampling bias** | Respondents differ from the target population (only active users answer) | Random sample, quota by segment, include churned users |
| **Non-response bias** | Those who reply differ from those who do not | Short survey, reminders, compare responders to the base |
| **Leading / loaded questions** | Wording nudges the answer | Neutral wording, test with pilot respondents |
| **Double-barrelled** | "Is the app fast and easy?" asks two things | One idea per question |
| **Acquiescence** | People agree with statements | Mix positive and negative items; avoid agree/disagree scales |
| **Social desirability** | Answers that look good | Anonymity, behaviour-based questions |
| **Order / anchoring effects** | Earlier questions shape later ones | Randomise options, general before specific |
| **Stated vs revealed preference** | People say they would pay but do not | Prefer behavioural data or commitments |

Metrics: **CSAT** (satisfaction with an interaction), **NPS** (0-10 likelihood to recommend; % promoters 9-10 minus % detractors 0-6), **CES** (effort). Specialised methods: **Kano** (must-have vs delighter), **Van Westendorp** (price sensitivity), **MaxDiff** (forced trade-offs).

$$n = \frac{z^2\, p(1-p)}{e^2}$$

With 95% confidence ($z = 1.96$), worst-case $p = 0.5$ and margin of error $e = 0.05$: $n = 384$ responses. For a finite population $N$: $n_{adj} = \frac{n}{1 + (n-1)/N}$.

### Example
A survey for 2,000 registered distributors: required $n = 1.96^2 \times 0.25 / 0.05^2 = 384.2 \approx 385$. Finite-population correction: $385/(1 + 384/2000) \approx 323$ responses. At a 20% response rate you must invite about 1,615 distributors. Tightening to ±3% would need about 1,067 responses for an infinite population. Check non-response: if responders skew toward the top 20% of distributors by volume, weight the results. See [[092 Sampling & Experimental Design]] and [[205 Sampling Distributions & Estimation]].

### In the news
See news box. Survey fraud and AI-generated open-text responses are a growing quality issue, so add attention checks and verify respondents against customer records where possible.

### Interview angle
> [!question] How it is asked
> "Your NPS is 42. Can you trust it and what would you do with it?"

> [!tip] Strong answer includes
> - NPS as a lagging, coarse signal: who responded, sample size, trend by segment
> - Linking verbatims to behaviours (retention, repeat orders)
> - Naming at least three biases and a mitigation for each
> - Sample-size reasoning rather than "we surveyed a lot of people"

---

## 7. Sample Sizes in Discovery
> 🟠 Tier 2 · _Key points:_ 5 users per round, saturation, qualitative is not statistics; when 20+ is needed

### Definition
Sample size depends on **what question** you ask:

- **Qualitative usability testing:** Nielsen and Landauer's model says the share of problems found by $n$ users is
$$1 - (1 - L)^n$$
where $L \approx 0.31$ is the average share a single user finds. So 5 users ≈ 84.4%. NN/g recommends **several rounds of about 5** rather than one large round, only **2-3 users per distinct audience** where budgets are tight, **20+** for quantitative usability metrics, **15+ per group for card sorting**, about **39** for stable eyetracking heatmaps.
- **Qualitative interviews:** run until **thematic saturation**: new interviews stop producing new themes. Typically 5-8 per segment for a focused question; more if segments differ.
- **Surveys / quantitative:** use the margin-of-error formula in the surveys section above.
- **A/B experiments:** power calculation, see [[089 Hypothesis Testing]] and [[214 Causal Inference & Experimentation Beyond A-B Tests]].

Caveats: the 31% figure varies with product complexity and tester skill; **"5 users" does not mean 5 users total** (several rounds, several segments); and 5 successes out of 5 do not prove a 100% success rate.

### Example
Probability that a theme held by a share $p$ of users appears at least once in $n$ interviews is $1-(1-p)^n$:

| Theme prevalence | 5 interviews | 8 | 10 | 15 |
|---|---|---|---|---|
| 10% of users | 41% | 57% | 65% | 79% |
| 20% | 67% | 83% | 89% | 96% |
| 30% | 83% | 94% | 97% | 100% |

To see a 20% theme at least once with 90% confidence you need $\ln(0.1)/\ln(0.8) \to 11$ interviews; for a 10% theme, 22. Rare but severe issues (for example payment failure for one bank) need targeted recruiting. Quantitatively: 5 of 5 tasks successful gives a 95% Wilson interval of 57-100%; 24 of 30 gives 63-91%, which is why small tests detect big problems but cannot estimate rates.

### In the news
See news box. Nielsen's article is now 25 years old, yet its core logic (iterate with small rounds) is what enables weekly discovery.

### Interview angle
> [!question] How it is asked
> "How many users would you test with before deciding to launch?"

> [!tip] Strong answer includes
> - "It depends on the question": qualitative problem-finding vs quantitative estimation
> - The $1-(1-L)^n$ logic with several small rounds
> - Segments change the count; saturation as stopping rule
> - Pairing small-sample qualitative insight with a quantitative follow-up

---

## 8. Usability Testing vs Concept Testing
> 🟠 Tier 2 · _Key points:_ Can they use it vs do they want it; task success, SUS; prototype fidelity

### Definition
| | **Usability testing** | **Concept testing** |
|---|---|---|
| Question | Can users complete tasks with the design? | Do users understand, want and value the idea? |
| Stage | Prototype or live product, after the problem is chosen | Before building: idea, positioning, storyboard, landing page |
| Stimulus | Clickable prototype, tasks | Concept card, mock-ups, pitch or price |
| Metrics | Task success rate, time on task, error count, **SUS** score, severity of issues | Comprehension, appeal, relevance, purchase intent, preference, MaxDiff |
| Typical n | 5 per round (qualitative) | 5-8 interviews, or 100-300 for quantitative concept survey |
| Main risk | Fixing usability of something nobody wants | Stated intent overstates real demand |

**System Usability Scale (SUS):** 10 items, 1-5 scale; for odd items subtract 1, for even items subtract the response from 5, add and multiply by 2.5, giving 0-100; average across the industry is about 68. Moderated methods: think-aloud, 5 tasks, one facilitator. Unmoderated remote tests scale cheaply. Combine with [[033 Design Thinking & UX]] for prototype fidelity and heuristics. Concept tests should anchor intent with **commitment** (pre-order, waitlist sign-up) because intent claims typically overstate behaviour.

### Example
Respondent 1 answers the ten items 4,2,4,2,5,1,4,2,4,2. Odd-numbered items (4,4,5,4,4) minus 1 give 3,3,4,3,3 = 16; even-numbered items (2,2,1,2,2) subtracted from 5 give 3,3,4,3,3 = 16; total 32 × 2.5 = **80**. Two more respondents score 90 and 55, so the mean of the three is 75, above the 68 benchmark. With n = 3 the spread (55 to 90) is the real finding: one user struggled badly, and the session recording of that user shows which screen to fix first.

### In the news
See news box. AI "synthetic users" are offered as cheap concept testers; the survey's 91% accuracy worry suggests treating them as brainstorming aids, not evidence of demand.

### Interview angle
> [!question] How it is asked
> "You have a prototype of a new feature. How do you test it before engineering starts?"

> [!tip] Strong answer includes
> - Separating "is it wanted" (concept) from "is it usable" (usability) and testing them in that order
> - Task-based protocol with success criteria agreed up front
> - 5 users per round, iterate, then measure with SUS or task success
> - Behavioural commitment as the strongest concept evidence

---

## 9. Assumption Mapping and Prioritising What to Test
> 🟠 Tier 2 · _Key points:_ List assumptions, plot importance vs evidence, test the riskiest first

### Definition
Every solution hides assumptions. **Assumption mapping** (Torres; David Bland's *Testing Business Ideas*) surfaces and ranks them:

1. **Story-map** how the solution creates value, step by step.
2. List each assumption in the form "We believe that ...". Categories: **desirability** (do they want it), **viability** (will it make money), **feasibility** (can we build it), **usability** (can they use it), **ethical** (could it cause harm).
3. Plot on a 2 × 2: **importance** (how much does the idea fail if wrong?) vs **evidence** (how much do we already know?).
4. Test **important with weak evidence** assumptions first: the "leap-of-faith" assumptions.
5. Write an experiment with a **falsifiable success threshold fixed before the test** ("at least 10% of visitors click"; "6 of 8 managers complete the task unaided").

| | Weak evidence | Strong evidence |
|---|---|---|
| **High importance** | **Test now** | Monitor |
| **Low importance** | Test later / ignore | Ignore |

A good experiment states: assumption, hypothesis, method, sample, metric, **threshold** (pass/fail), and the decision each outcome triggers.

### Example
Solution: "driver app shows live fuel price at nearby pumps." Assumptions: (1) drivers care about price more than distance (desirability, high importance, weak evidence) → test first with 8 driver interviews; (2) pump data available via API (feasibility, high, weak) → engineer spike of 2 days; (3) UI clear (usability, low) → later. Threshold: at least 6 of 8 drivers name fuel price as a top-3 concern in a last-fill-up story. If only 2 of 8 do, kill or reshape before building anything.

### In the news
See news box. The thin research capacity reported means assumption mapping is how PMs choose the one or two experiments they can afford this week.

### Interview angle
> [!question] How it is asked
> "How do you validate a new product idea cheaply before investing in it?"

> [!tip] Strong answer includes
> - Listing assumptions by risk type, ranking by importance and evidence
> - A pre-committed, falsifiable threshold and a decision rule
> - Choosing the cheapest experiment that tests the riskiest assumption
> - Willingness to kill or pivot on the data

---

## 10. Discovery Experiments: Fake Door, Concierge, Wizard of Oz
> 🟠 Tier 2 · _Key points:_ Fake door, concierge, Wizard of Oz, explainer video, prototypes; ethics

### Definition
Experiments are ordered from cheapest/weakest to costliest/strongest evidence.

| Method | What it is | Tests | Weakness |
|---|---|---|---|
| **Fake door / painted door** | A button, link or landing page for a feature that does not exist; measure clicks or sign-ups, then reveal "coming soon" | Desirability, demand | Clicks are not payment; may annoy users |
| **Explainer video / landing page** | Describes the product and collects emails or pre-orders | Value proposition | Self-selected audience |
| **Concierge MVP** | You deliver the service manually and visibly to a few customers | Whether the outcome is valued; what the process really needs | Does not scale; high touch |
| **Wizard of Oz** | The customer sees a working product, but humans operate the back end in secret | Usability and demand of the full experience | Hidden cost; can mislead on feasibility |
| **Prototype test** | Clickable mock-up | Usability | Not real behaviour |
| **Pre-order / pilot with payment** | Real money or signed pilot | Willingness to pay | Needs a credible offer |
| **A/B or feature-flag rollout** | Real feature to a slice of users, see [[214 Causal Inference & Experimentation Beyond A-B Tests]] | Impact on the outcome metric | Needs build and traffic |

A famous demand test: Drew Houston's 2008 Dropbox demo video; he said the beta waiting list went from 5,000 to 75,000 "literally overnight" (TechCrunch, 2011). Eric Ries's *Lean Startup* popularised concierge and Wizard-of-Oz style MVPs. **Ethics:** do not collect payment for products you cannot deliver; tell participants afterwards; avoid fake doors on critical flows (health, finance).

### Example
Fake door on a freight app: 20,000 shippers see a new "Instant quote" button; 600 tap it (3.0%, 95% interval 2.8-3.2%); of the 600, 90 (15%) join a pilot waitlist, i.e. 0.45% of all viewers. Pre-set thresholds: proceed if tap-rate above 2% and waitlist conversion above 10%. Both pass, so a **concierge** pilot follows: ops staff quote manually for 30 shippers; each quote takes 4 hours at ₹250 per hour, a total of 30 × 4 × 250 = ₹30,000 per round, cheap relative to a quarter of engineering time. The concierge also reveals which 6 data fields staff always had to ask for, which become the product's input form.

### In the news
See news box. AI makes Wizard-of-Oz cheaper: a human-in-the-loop prototype can now be an LLM, but label it honestly to participants.

### Interview angle
> [!question] How it is asked
> "You want to launch a B2B subscription feature but are unsure anyone will pay. What is the cheapest test?"

> [!tip] Strong answer includes
> - A ladder of experiments from fake door to concierge to paid pilot
> - Pre-set thresholds, sample and duration, and the follow-up decision
> - Awareness that clicks are weak evidence and payment/commitment is strong
> - Ethical handling of fake doors and deception

---

## 11. Synthesising Insights: Affinity Maps and Evidence
> 🟠 Tier 2 · _Key points:_ Affinity diagram, themes, insight statements, evidence strength, avoiding confirmation bias

### Definition
**Synthesis** converts raw notes into decisions. Steps: (1) **capture** each observation as an atomic note with a source ID (P4: "phoned distributor three times"); (2) **cluster** similar notes bottom-up into an **affinity map** (themes emerge from data, not from predefined buckets); (3) **name** the clusters as customer needs (opportunities); (4) write **insight statements**: "[User] needs [need] because [reason], evidenced by [n of N]"; (5) **rate evidence strength**: number of independent sources, recency, behaviour vs opinion, and triangulation with quantitative data; (6) **act**: update the opportunity solution tree and record the decision.

Tools: sticky notes (Miro, FigJam), spreadsheet coding, Dovetail-type repositories, AI-assisted clustering (see [[219 NLP, Embeddings & LLM Applications for Analysts]]). Related artefacts: **personas** (profile of a segment), **journey maps** (stages and emotions over time), **empathy maps** (see [[033 Design Thinking & UX]]).

| Evidence level | Example | Weight |
|---|---|---|
| Strong | Observed behaviour, payments, usage logs, signed pilot | High |
| Medium | Specific past-story from several interviewees; support ticket patterns | Medium |
| Weak | Opinions, hypotheticals, one-off requests | Low |

Guards against **confirmation bias**: have two people cluster independently; actively look for disconfirming quotes; count only independent sources; separate observation from interpretation.

### Example
Twelve interviews with plant maintenance managers produce 96 notes. Clustering gives 7 themes, the largest being "spares availability unknown at breakdown" (31 notes from 9 of 12 managers). Insight: "Maintenance managers need real-time spares visibility because they lose breakdown hours searching stores, evidenced by 9 of 12, with logged downtime of 3-6 hours per event (behavioural data from 2 plants)". Two other themes had only 2 sources each and are parked. Link to [[022 Maintenance Management (TPM-RCM)]] and [[204 SAP PM Deep Dive - Maintenance Orders, Plans & Strategies]] for the system-of-record side.

### In the news
See news box. With 80% of researchers using AI, a good habit is to ask AI for candidate clusters but to verify every theme against the quotes.

### Interview angle
> [!question] How it is asked
> "You have 20 interview transcripts. How do you get from them to a product decision?"

> [!tip] Strong answer includes
> - Atomic notes, bottom-up clustering and counting independent sources
> - Insight statements with evidence strength, not just themes
> - Triangulating with quantitative data
> - Naming bias controls and the decision the synthesis fed

---

## 12. Discovery for B2B and Operations Products
> 🟠 Tier 2 · _Key points:_ Buyer vs user vs payer; shadowing; process mapping; small N; compliance and legacy ERP

### Definition
B2B and operations products differ from consumer ones:

- **Multiple stakeholders:** the **buyer** (budget), **user** (daily work), **influencer/IT** (integration, security) and **champion**. Discover each separately; the user's pain does not equal the buyer's ROI case.
- **Small, concentrated customer base:** 30 enterprise accounts means each interview is a large share of the market; recruit through account managers and customer success, and watch for bias toward friendly customers.
- **Context matters:** shadow users on the shop floor, warehouse or dispatch desk (**contextual inquiry**), because workflows live in WhatsApp, Excel and paper, and workers omit steps they consider obvious.
- **Process and data first:** map the as-is process (see [[017 Process Management & Optimization]], [[173 Process Mining & Operations Intelligence]]) and quantify the pain in time, rupees and errors (cost-to-serve, see [[138 Order Management, Customer Service & Cost-to-Serve]]).
- **Integration and change costs:** ERP, WMS or TMS integration (see [[174 Supply Chain Technology Landscape - Planning, Execution & Procure Tech]]) and user training are often the real adoption barrier, so test feasibility and onboarding early.
- **Long cycles, few data points:** rely on qualitative evidence, pilots with success criteria, and **design partners** instead of A/B tests with thousands of users.

Typical B2B evidence ladder: user interviews → shadowing → data pull of current process metrics → prototype walkthrough with buyer → paid pilot with exit criteria → expansion.

### Example
A warehouse WMS add-on to reduce mis-picks. Discovery: shadow 4 pickers over 2 shifts at 2 sites and observe that most mis-picks involve similar-looking SKU labels in adjacent bins. Pull the WMS data: 30,000 picks per day with a recorded error rate of 0.5% = 150 mis-picks per day. Ask the warehouse head for the cost per mis-pick (₹180 including return and re-ship): 150 × ₹180 = ₹27,000 per day, or about ₹81 lakh per year at 300 working days (150 × 180 × 300 = ₹81,00,000). A paid pilot at one site targets a 40% reduction, success criterion agreed with the buyer. The users and the buyer therefore see value in different terms (fewer errors and less rework vs ₹ saved), and both are covered. See [[128 Warehouse Labour, WES-WCS & Yard Management]].

### In the news
See news box. Low PM share among research practitioners (7% of Maze respondents) reinforces that in B2B the PM must partner with customer success and sales for access rather than rely on a research team.

### Interview angle
> [!question] How it is asked
> "How would you do product discovery for a TMS used by transport planners at a 3PL?"

> [!tip] Strong answer includes
> - Mapping buyer, user, IT and champion; separate interviews for each
> - Shadowing and process data to quantify pain in ₹ and hours
> - Early integration and change-management risk tests
> - Pilot with success criteria and design partners instead of large A/B tests

---

## 13. ⭐ Advanced: Decision Rules, Evidence Quality and Discovery Debt
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Senior PMs formalise **when evidence is enough**:

- **Confidence scoring:** score each solution on Impact, Confidence, Ease (ICE) or reach/impact/confidence/effort (RICE, see [[034 Prioritization Frameworks]]); confidence should be driven only by the **evidence level** (strong/medium/weak above), not by enthusiasm. Raise confidence by running a cheaper experiment, not by debating.
- **Pre-registered thresholds:** decide pass/fail before seeing data, reducing **HARKing** (hypothesising after results are known) and motivated reading of noisy results.
- **Reversibility test (Bezos "one-way vs two-way doors"):** reversible changes need light evidence and fast shipping; irreversible ones (pricing model, data migration, regulated features) need deeper discovery.
- **Triangulation:** three independent signals (qualitative stories, behavioural data, commercial commitment) before a big bet.
- **Discovery debt:** the gap since you last spoke with the customer segment; reduce it with a standing interview programme. Symptoms: roadmap items with no linked customer evidence and surprise churn.
- **Bias checklist:** confirmation, survivorship (only talking to retained users), recency, HiPPO (highest paid person's opinion), and the "loudest customer" trap.
- **Responsible discovery:** consent for recordings, anonymisation, and data minimisation. In India the Digital Personal Data Protection Act, 2023 and its Rules apply to personal data collected in research, see [[166 AI Product Management - LLM Products, Evals & Economics]] for the DPDP timeline.

### Example
Two candidate bets with evidence audits. Bet A "bulk order upload": 9 of 12 interviewees cite it, 4 pilot customers shared sample files, a fake door got a 4.1% tap rate: three independent signals, **high** confidence. Bet B "AI route suggestions": enthusiastic quotes from 3 prospects, no behavioural data, no pilot: **low** confidence, so the next step is a Wizard-of-Oz test rather than a build. With equal impact scores, RICE using confidence 100% for A and 50% for B ranks A at twice the score of B for the same reach, impact and effort, purely on evidence.

### In the news
See news box. As AI tools produce plausible-looking synthesis in minutes, evidence quality (traceable quotes, behavioural data) becomes the scarce skill.

### Interview angle
> [!question] How it is asked
> "Your CEO is certain about a feature; the data is mixed. What do you do?"

> [!tip] Strong answer includes
> - Treating the CEO's belief as a hypothesis with a stated test and threshold
> - Evidence audit with strong/medium/weak sources
> - Reversibility and cost of being wrong
> - Offering a time-boxed experiment and a pre-agreed decision rule (see [[163 PM Interview Types & Answer Frameworks]])
