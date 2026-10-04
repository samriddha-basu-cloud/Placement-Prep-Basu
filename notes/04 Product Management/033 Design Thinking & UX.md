---
tags: [product-management, tier2]
area: Product Management
topic: "Design Thinking & UX"
tier: Tier 2
roles: PM
status: complete
subtopics: 12
---
# Design Thinking & UX

⬅ [[032 Agile & Scrum Framework]] · [[_Index - Product Management|Product Management]] · [[034 Prioritization Frameworks]] ➡

> **Area:** Product Management · **Priority:** 🟠 Tier 2 · **Target roles:** PM

## Sub-topics in this note
1. [[#1. Design Thinking Stages]]
2. [[#2. Empathy Mapping]]
3. [[#3. Pain Point Identification]]
4. [[#4. Wireframing Basics]]
5. [[#5. Usability Testing]]
6. [[#6. Accessibility in Design]]
7. [[#7. UX Research Methods]]
8. [[#8. Prototype Fidelity]]
9. [[#9. Visual Design Basics]]
10. [[#10. Responsive Design]]
11. [[#11. ⭐ Advanced: UX Laws and Heuristic Evaluation]]
12. [[#12. ⭐ Advanced: Measuring UX at Scale (HEART, Task Success, Design Metrics)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): The European Accessibility Act takes effect (28 June 2025)
> The **European Accessibility Act (EAA)** became applicable on **28 June 2025**, requiring many consumer-facing digital products and services sold in the EU (e-commerce, banking services, e-books, ticketing and self-service terminals) to be accessible. A first-year enforcement summary reports that the technical reference standard is **EN 301 549 v3.2.1, which incorporates WCAG 2.1 Level AA**, and that penalties differ widely between EU member states (set nationally). I have not relied on that page's compliance statistics, as I could not cross-check them. For Indian product teams selling into Europe, accessibility has moved from "nice to have" to a legal requirement. ([Disability World summary](https://www.disabilityworld.org/articles/eaa-first-year-enforcement-report/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Design Thinking Stages
> 🟠 Tier 2 · _Tracker hint:_ Empathize → Define → Ideate → Prototype → Test

### Definition
**Design thinking** is a human-centred, iterative problem-solving approach (popularised by IDEO and Stanford d.school). Five stages:

| Stage | Aim | Typical methods | Output |
|---|---|---|---|
| **Empathize** | Understand users | Interviews, observation, immersion | Insights, empathy map |
| **Define** | Frame the right problem | Synthesis, affinity maps, "How might we" | Problem statement / POV |
| **Ideate** | Generate many options | Brainstorm, SCAMPER, Crazy 8s | Shortlisted ideas |
| **Prototype** | Make ideas tangible cheaply | Sketches, mock-ups, storyboards | Low-fidelity prototype |
| **Test** | Learn from users | Usability tests, A/B, feedback | Learnings, iterate |

Stages are **non-linear**: loop back as you learn. Mindsets: empathy, curiosity, bias to action, collaboration, "fail early and cheaply". **Double Diamond** (UK Design Council): Discover → Define → Develop → Deliver, alternating divergent and convergent thinking. A good **problem statement**: "[User] needs [need] because [insight]."

### Example
Reducing no-shows at a diagnostic lab: Empathize (interview patients: hard to fast, unclear instructions) → Define ("How might we make preparation instructions effortless?") → Ideate (WhatsApp reminders, pictorial guide) → Prototype (mock message flow) → Test with 10 patients, then iterate.

### In the news
See news box. Accessibility requirements sit inside Empathize and Test: include users with disabilities in research rather than retrofitting later.

### Interview angle
> [!question] How it is asked
> "Walk me through how you would design a solution for [problem] using design thinking."

> [!tip] Strong answer includes
> - The five stages with a concrete method for each
> - A sharp problem statement before ideation
> - Iterative and user-tested, not linear
> - A measurable outcome to confirm success

---

## 2. Empathy Mapping
> 🟠 Tier 2 · _Tracker hint:_ Says, thinks, does, feels — user empathy tool

### Definition
An **empathy map** (Dave Gray, XPLANE) is a one-page visual that captures what we know about a user to build shared understanding. Four quadrants around the user:

- **Says:** direct quotes from interviews.
- **Thinks:** beliefs and worries they may not voice.
- **Does:** observed behaviours and actions.
- **Feels:** emotions (frustrations, fears, hopes).

Extended versions add **Hears**, **Sees**, plus **Pains** and **Gains**. Method: pick one persona and context, gather research data, put sticky notes in each quadrant, look for **contradictions** (says vs does) and **insights**, then derive needs and "How might we" questions. Empathy maps summarise research; they do not replace it, and they differ from personas (a profile) and journey maps (a sequence over time).

### Example
Gig delivery partner using a payouts app. Says: "Why is my payout delayed?" Thinks: "If I lose a day's pay I cannot cover rent." Does: checks the app 10 times a day, screenshots earnings. Feels: anxious, distrustful. Insight: needs real-time payout transparency; opportunity: live earnings tracker and payout ETA.

### In the news
See news box. For accessibility, empathy maps for users with low vision or motor impairments reveal needs that majority-user research misses.

### Interview angle
> [!question] How it is asked
> "How would you build empathy with users of a rural health app?"

> [!tip] Strong answer includes
> - Four quadrants with real research inputs
> - Says vs does contradiction as insight
> - Derives needs and opportunities
> - Differentiates from persona and journey map

---

## 3. Pain Point Identification
> 🟠 Tier 2 · _Tracker hint:_ Primary research, surveys, interviews, usability tests

### Definition
A **pain point** is a specific friction or unmet need that users face. Types: **financial** (too costly), **productivity** (time-consuming), **process** (confusing steps), **support** (no help available). Sources:

- **Primary research:** interviews, observation/contextual inquiry, surveys, usability tests.
- **Secondary / behavioural data:** funnel drop-offs, support tickets, app reviews, search queries, session recordings, NPS verbatims.

Method: gather → code themes (affinity diagramming) → rate by **frequency × severity** (and reach) → validate quantitatively → turn the top ones into problem statements. Ask about **past behaviour** ("tell me about the last time you ...") rather than hypotheticals; avoid leading questions (the Mom Test); look for workarounds, since a workaround signals a real pain. Interview 5–8 users per segment for qualitative patterns.

### Example
A banking app has 40% drop-off at e-KYC. Interviews and recordings show that users fail to upload a clear photo in low light and don't know why the app rejects it. Pain point: unclear error and no guidance. Fix: live framing guide and specific error text; measure completion rate afterwards.

### In the news
See news box. Accessibility complaints (unlabeled buttons, low contrast) are pain points that now carry legal as well as UX risk for products sold in Europe.

### Interview angle
> [!question] How it is asked
> "How would you discover the biggest problems users face with our app?"

> [!tip] Strong answer includes
> - Mix of qualitative and quantitative sources
> - Prioritisation by frequency, severity and reach
> - Past-behaviour interviewing and avoiding leading questions
> - Converting pain into a testable hypothesis

---

## 4. Wireframing Basics
> 🟠 Tier 2 · _Tracker hint:_ Low/high fidelity; Figma/Balsamiq basics; information architecture

### Definition
A **wireframe** is a skeletal, mostly grayscale layout showing structure, content hierarchy and functionality of a screen without detailed styling.

- **Low-fidelity:** quick sketches or boxes (paper, Balsamiq) to explore layout and flow cheaply.
- **High-fidelity:** pixel-accurate designs with real content, spacing and components (Figma, Sketch, Adobe XD), often with design systems.
- **Information architecture (IA):** how content is organised, labelled and navigated: sitemaps, navigation structure, hierarchy, labelling; validated through card sorting and tree testing.

Figma basics: frames per screen, auto layout, components and variants, constraints, shared styles, prototyping links, comments, dev mode. Principles: clear hierarchy, consistent patterns, one primary action per screen, realistic content, annotate behaviour and states (empty, loading, error). **User flow** diagrams show the path across screens.

### Example
Checkout flow wireframes: Cart → Address → Payment → Confirmation. In low fidelity, test whether users find "Apply coupon"; in high fidelity, define states: coupon invalid, payment pending, payment failed. Keep one primary button ("Pay Rs 1,299") per screen.

### In the news
See news box. Annotating wireframes with accessibility notes (heading order, alt text, focus order, labels) is cheaper than fixing built products.

### Interview angle
> [!question] How it is asked
> "Sketch the home screen for a grocery delivery app and explain your choices."

> [!tip] Strong answer includes
> - Goal and primary action first, then layout
> - Hierarchy, navigation and key states
> - Fidelity chosen to match the decision to be made
> - Plan to validate with users

---

## 5. Usability Testing
> 🟠 Tier 2 · _Tracker hint:_ Task completion rate, time-on-task, error rate, SUS score

### Definition
**Usability testing** observes representative users attempting realistic tasks to find problems. Types: moderated vs unmoderated, remote vs in-person, formative (find issues) vs summative (measure).

Metrics:
- **Task completion (success) rate** $=\frac{\text{successful tasks}}{\text{attempts}}\times100$.
- **Time on task**, **error rate**, number of clicks, **satisfaction** (post-task SEQ, post-test SUS).
- **System Usability Scale (SUS):** 10 statements on a 1–5 scale; odd items score $=x-1$, even items $=5-x$; sum the scores and multiply by **2.5** to get 0–100. The average SUS is about **68**; above 80 is excellent.

Nielsen: about 5 users uncover roughly 85% of usability problems: $1-(1-0.31)^5\approx 0.84$. Use several small rounds. Prepare a script with tasks and success criteria; "think aloud"; observe, don't help; rate issue severity.

### Example
SUS answers: 4,2,4,2,5,1,4,2,4,2. Odd items (1,3,5,7,9): 4,4,5,4,4 → 3+3+4+3+3 = 16. Even items (2,4,6,8,10): 2,2,1,2,2 → (5−x) = 3+3+4+3+3 = 16. Total 32 × 2.5 = **80**. Task data: 18 of 20 participants found "Reorder", completion = **90%**.

### In the news
See news box. Include participants who use screen readers and keyboard-only navigation in usability tests; automated checks catch only part of the issues.

### Interview angle
> [!question] How it is asked
> "How would you test whether the new onboarding is usable?"

> [!tip] Strong answer includes
> - Representative users, realistic tasks, success criteria
> - Behavioural metrics (completion, time, errors) plus SUS
> - Small iterative rounds and severity ranking
> - Turning findings into prioritised design changes

---

## 6. Accessibility in Design
> 🟠 Tier 2 · _Tracker hint:_ WCAG standards; inclusive design principles

### Definition
**Accessibility (a11y)** means people with disabilities (visual, hearing, motor, cognitive) can perceive, understand, navigate and interact with your product. **WCAG** (W3C Web Content Accessibility Guidelines; 2.1 in 2018, **2.2 in Oct 2023**) is organised by **POUR** principles: **Perceivable, Operable, Understandable, Robust**. Conformance levels: **A, AA, AAA**; AA is the usual legal target.

Key AA requirements:
- **Colour contrast:** at least **4.5:1** for normal text and **3:1** for large text and UI components.
- Text alternatives (alt text) for images; captions for video.
- Full keyboard operability and visible focus; no keyboard traps.
- Don't use colour alone to convey meaning; resizable text; clear labels, errors and form instructions.
- Semantic HTML and ARIA for screen readers; sensible touch targets.

**Inclusive design** (Microsoft): recognise exclusion, learn from diversity, solve for one, extend to many (permanent, temporary, situational limits, e.g., a broken arm or a glare-filled screen). Universal design benefits everyone (captions, curb cuts).

### Example
Button text #777777 on white has contrast about 4.48:1, which just fails the 4.5:1 AA requirement for normal text; darkening to #767676 passes at about 4.54:1. Also add a text label to an icon-only "Pay" button for screen readers.

### In the news
See news box. The EAA applies from 28 June 2025 and points to EN 301 549 (WCAG 2.1 AA) as the technical standard for covered products and services in the EU.

### Interview angle
> [!question] How it is asked
> "How would you make a payments app accessible?" or "What is WCAG?"

> [!tip] Strong answer includes
> - POUR principles and AA contrast ratios
> - Examples: keyboard, screen reader, captions, not colour-only
> - Inclusive design: permanent, temporary, situational
> - Testing with assistive tech and users, plus regulatory context

---

## 7. UX Research Methods
> 🟠 Tier 2 · _Tracker hint:_ Interviews, surveys, card sorting, tree testing, diary studies

### Definition
Methods sit on two axes: **qualitative vs quantitative** (why vs how many) and **attitudinal vs behavioural** (say vs do).

| Method | Answers | Type |
|---|---|---|
| **User interviews** | Motivations, context, language | Qualitative, attitudinal |
| **Surveys** | Prevalence, satisfaction, segmentation | Quantitative, attitudinal |
| **Contextual inquiry / ethnography** | Real-world behaviour | Qualitative, behavioural |
| **Card sorting** | How users group and label content (open vs closed) | IA, qualitative or quantitative |
| **Tree testing** | Can users find items in a proposed menu hierarchy? | IA validation, quantitative |
| **Diary studies** | Behaviour and feelings over days or weeks | Longitudinal, qualitative |
| **Usability testing** | Can users complete tasks | Behavioural |
| **A/B tests, analytics** | What happens at scale | Quantitative, behavioural |
| **Concept testing, Kano** | Value and priority of ideas | Mixed |

Choose by question and stage: discovery (interviews, field studies, diary), design (card sort, tree test, concept test), validation (usability, A/B). Triangulate methods.

### Example
Redesigning a bank's app menu: open card sort with 30 users shows "Cards" and "Limits" cluster together; a tree test of the new structure shows that only 55% find "Raise card limit"; after relabelling, the next test reaches 82%.

### In the news
See news box. Research panels must include disability-inclusive recruitment to meet the intent of accessibility regulation.

### Interview angle
> [!question] How it is asked
> "Which research method would you use to decide the navigation structure of an app?"

> [!tip] Strong answer includes
> - Matching method to question (why vs how many, say vs do)
> - Card sort then tree test for IA
> - Sample size and bias awareness
> - Triangulation of qualitative and quantitative data

---

## 8. Prototype Fidelity
> 🟠 Tier 2 · _Tracker hint:_ Paper → digital wireframe → interactive prototype → pilot

### Definition
**Fidelity** is how closely a prototype resembles the final product in visuals, interaction and content. Spectrum:

1. **Paper / sketch (low):** minutes, test concepts and flows.
2. **Digital wireframe (low-mid):** layout and hierarchy, click-through.
3. **Interactive prototype (high):** Figma/ProtoPie with realistic UI, transitions, content; tests usability details.
4. **Coded prototype / beta:** real data and performance.
5. **Pilot:** limited real-world release to a small group, measuring behaviour.

Rule: **use the lowest fidelity that answers the question**. Low fidelity invites structural feedback and is cheap to change; high fidelity yields precise feedback on visual and interaction detail but costs more and can anchor teams ("it looks finished"). Match to risk: desirability (concept), usability (interactive), feasibility (coded), viability (pilot). Also "Wizard of Oz" prototypes simulate back-end behaviour with humans.

### Example
New cash-flow dashboard for small businesses: week 1, paper sketches with 5 shop owners (does the chart idea make sense?); week 2, clickable Figma prototype tested on task completion; week 4, pilot to 200 users in one city, measuring weekly active use and support tickets.

### In the news
See news box. Fidelity choices should include accessibility behaviours (focus order, keyboard use) once prototypes are interactive.

### Interview angle
> [!question] How it is asked
> "How would you validate a new product idea before engineering effort?"

> [!tip] Strong answer includes
> - Fidelity ladder tied to the question being tested
> - Cost vs learning trade-off
> - Risks of premature high fidelity
> - Pilot design with success metrics

---

## 9. Visual Design Basics
> 🟠 Tier 2 · _Tracker hint:_ Typography, color theory, hierarchy, negative space

### Definition
- **Typography:** choose 1–2 typefaces; use a scale (e.g., 12/14/16/20/24/32 px); body text at least 16px on mobile for readability; line height about 1.4–1.6; limit line length to ~50–75 characters; weight and size signal hierarchy.
- **Colour theory:** colour wheel (complementary, analogous, triadic); 60-30-10 rule (dominant, secondary, accent); brand colour for primary actions; semantic colours (green success, red error, amber warning); cultural meanings; ensure contrast and do not rely on colour alone.
- **Visual hierarchy:** size, contrast, position, whitespace and proximity direct attention; one primary call-to-action per view.
- **Negative space (whitespace):** space around elements improves comprehension and focus.
- **Layout and grid:** 8-point spacing system, alignment, consistency.
- Gestalt principles: proximity, similarity, closure, continuity.
- **Design systems** (Material, Apple HIG, internal libraries) ensure consistency.

### Example
A pricing page cluttered with five equally bold buttons. Redesign: single high-contrast primary button ("Start free trial"), secondary actions as text links, 24px spacing between plan cards, body text 16px with 1.5 line height, headline 32px bold. The result: clear hierarchy and fewer decisions.

### In the news
See news box. Compliance with WCAG 2.1 AA affects visual design directly through contrast, text size and non-colour cues.

### Interview angle
> [!question] How it is asked
> "What makes a good interface visually? Critique this screen."

> [!tip] Strong answer includes
> - Hierarchy, contrast, spacing and consistency
> - One primary action and clear typography scale
> - Colour use with accessibility and meaning
> - Links design choices to user goals and metrics

---

## 10. Responsive Design
> 🟠 Tier 2 · _Tracker hint:_ Mobile-first; breakpoints; touch vs cursor interaction

### Definition
**Responsive design** adapts layout to screen size and capability using fluid grids, flexible images and CSS media queries.

- **Mobile-first:** design and build for the smallest screen first, then progressively enhance for larger screens (focuses on core content and performance; most Indian users are mobile-first).
- **Breakpoints (typical):** ~360–480 px (phones), ~768 px (tablets), ~1024 px (small laptops), ~1280 px+ (desktops); choose them by content, not devices.

```css
.card { width: 100%; }
@media (min-width: 768px) { .card { width: 50%; } }
```

- **Touch vs cursor:** touch targets at least ~44×44 px (Apple) or 48×48 dp (Material); no hover-only interactions; thumb-reach zones; gestures need visible alternatives. Cursor: hover states, precise small targets, keyboard shortcuts.
- Other: responsive images, performance on slow networks, orientation, text reflow at 400% zoom (WCAG reflow), safe areas, dark mode, internationalisation (Indic scripts, longer text).

### Example
E-commerce product page: on a 360 px phone, one column with a sticky "Add to cart" button at the thumb zone; at 768 px, image left and details right; at 1280 px, adds a side filter panel. Test on low-end Android devices over 4G.

### In the news
See news box. WCAG's reflow and target-size criteria make responsive behaviour an accessibility topic, not just a layout one.

### Interview angle
> [!question] How it is asked
> "How would you design this for mobile and desktop?" or "What is mobile-first and why?"

> [!tip] Strong answer includes
> - Mobile-first rationale with content prioritisation
> - Breakpoint logic and layout changes
> - Touch target size, thumb zone and no hover dependence
> - Performance and accessibility considerations

---

## 11. ⭐ Advanced: UX Laws and Heuristic Evaluation
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Nielsen's 10 usability heuristics:** visibility of system status; match between system and the real world; user control and freedom; consistency and standards; error prevention; recognition rather than recall; flexibility and efficiency of use; aesthetic and minimalist design; help users recognise, diagnose and recover from errors; help and documentation. A **heuristic evaluation** has 3–5 experts inspect an interface against them, then rate each issue's **severity** (0–4) by frequency, impact and persistence: fast and cheap, but it finds expert-predicted issues, not real user behaviour.

**UX laws:**
- **Hick's law:** decision time rises with the number of choices, $T=b\log_2(n+1)$; reduce options.
- **Fitts's law:** time to hit a target $T=a+b\log_2(D/W+1)$ falls with larger, closer targets (make primary buttons big and reachable).
- **Jakob's law:** users expect your site to work like others they use.
- **Miller's law:** working memory about 7 ± 2 chunks; chunk information.
- **Peak-end rule:** experiences are judged by the peak and the end.

### Example
A form shows 12 payment options in one flat list. Applying Hick's law: show the 3 most used (UPI, card, netbanking) and group the rest under "More". Heuristic: "error prevention", since an incorrect UPI ID is validated live before submission.

### In the news
See news box. Accessibility audits often combine automated scanning, heuristic review and assistive-technology testing, because no single method finds everything.

### Interview angle
> [!question] How it is asked
> "Critique this app's UX" or "What UX principles guide your decisions?"

> [!tip] Strong answer includes
> - Named heuristics/laws tied to concrete screen issues
> - Severity ranking and prioritisation
> - Pairs expert review with user testing
> - Proposed changes and how to measure improvement

---

## 12. ⭐ Advanced: Measuring UX at Scale (HEART, Task Success, Design Metrics)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
PMs must link design to metrics. **Google's HEART framework** gives categories, each with Goals → Signals → Metrics:

| Dimension | Example metric |
|---|---|
| **H**appiness | CSAT, NPS, SUS |
| **E**ngagement | Sessions per user per week |
| **A**doption | New users of a feature |
| **R**etention | D30 retention, repeat rate |
| **T**ask success | Completion rate, time on task, error rate |

Other measures: **conversion funnel**, **Customer Effort Score**, support-ticket volume, rage clicks and dead clicks, form abandonment, accessibility audit pass rate. Combine **attitudinal** (surveys) and **behavioural** (analytics) data. Validate design changes by **A/B test** with a guardrail (e.g., support contacts) and a time-bounded **usability benchmark** to track improvement version to version.

Design-system ROI: reuse of components reduces build time and inconsistency.

### Example
Redesign of KYC flow. Before: completion 60%, median time 6 min, support tickets 8 per 1,000 users. After A/B test with 10,000 users per arm: completion 72%, median 4 min, tickets 6 per 1,000. Completion lift = +12 points (+20% relative: 72/60 − 1 = 0.20).

### In the news
See news box. A regulatory requirement like the EAA gives accessibility a measurable compliance metric (audit pass rate) that sits alongside HEART metrics.

### Interview angle
> [!question] How it is asked
> "How would you measure whether a redesign was successful?"

> [!tip] Strong answer includes
> - HEART or similar structure with 3–5 metrics
> - Baseline, target and an experiment or benchmark
> - Guardrails and qualitative follow-up
> - Decision rule for ship, iterate or roll back

---
## 🔗 Go deeper: expansion notes
- [[164 Product Discovery & User Research|Product Discovery & User Research]]
