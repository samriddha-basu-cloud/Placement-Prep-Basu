---
tags: [machine-learning, tier3]
area: Machine Learning
topic: "Responsible AI, Explainability & Model Governance"
tier: Tier 3
roles: PM / Analytics / Consulting
status: complete
subtopics: 14
---
# Responsible AI, Explainability & Model Governance

⬅ [[219 NLP, Embeddings & LLM Applications for Analysts]] · [[_Index - Machine Learning|Machine Learning]]

> **Area:** Machine Learning · **Priority:** 🟡 Tier 3 · **Target roles:** PM / Analytics / Consulting

## Sub-topics in this note
1. [[#1. Responsible AI: Principles and Why It Is an Interview Topic]]
2. [[#2. Where Bias Comes From, and Real Incidents]]
3. [[#3. Fairness Metrics: Demographic Parity, Equalised Odds and Calibration]]
4. [[#4. Executed Example: A Fairness Audit of a Loan Model]]
5. [[#5. Explainability: Global vs Local, Intrinsic vs Post-hoc]]
6. [[#6. SHAP and LIME]]
7. [[#7. Partial Dependence, Permutation Importance and Counterfactual Explanations]]
8. [[#8. Model Documentation: Model Cards, Datasheets and the Audit Trail]]
9. [[#9. Monitoring and Drift: PSI, KS and Performance Decay]]
10. [[#10. Human-in-the-Loop, LLM Risks and the Air Canada Ruling]]
11. [[#11. EU AI Act: Risk Tiers and Timeline]]
12. [[#12. India: DPDP Act 2023, DPDP Rules 2025 and the Emerging AI Rules]]
13. [[#13. AI Risk Register and Governance Operating Model]]
14. [[#14. ⭐ Advanced: Interview Framing for Responsible-AI Questions]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): the rules for AI are being written, delayed and phased in
> **EU AI Act: high-risk deadlines pushed back (Digital Omnibus, agreed May 2026, adopted mid-2026).** After a provisional political agreement on 6 May 2026 (confirmed by Member States on 13 May), the EU adopted the "Digital Omnibus" amendments. Obligations for stand-alone high-risk systems (Annex III uses such as employment, creditworthiness, education and essential services) moved from 2 August 2026 to **2 December 2027**; high-risk AI embedded in regulated products (Annex I) moved to **2 August 2028**. Most Article 50 transparency duties (telling users they are talking to an AI, marking synthetic content, disclosing deepfakes) still apply from **2 August 2026**, with a grace period to 2 December 2026 for watermarking existing systems; a new prohibition on AI that generates non-consensual intimate imagery and child sexual abuse material was added. Fines for Article 50 breaches reach EUR 15 million or 3% of worldwide turnover. ([Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); [Jones Walker](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon); [Orrick, July 2026](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes))
>
> **India notifies the DPDP Rules, 2025 (14 Nov 2025).** The Government of India notified the Digital Personal Data Protection Rules, operationalising the 2023 Act with an **18-month phased compliance timeline**, standalone consent notices, prompt breach notification to individuals, verifiable consent for children's data, and rights to access, correct, update and erase personal data, with responses due within a maximum of 90 days; the Data Protection Board works as a digital office. ([PIB release, 14 Nov 2025](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014))
>
> **India labels synthetic content (Feb 2026).** The IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021 were amended by a notification of 10 February 2026, effective 20 February 2026, adding obligations for intermediaries on AI-generated and synthetic content, including labelling with embedded metadata where feasible. ([Wikipedia, Regulation of artificial intelligence](https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence))
>
> Sub-topics that say **"See news box"** reuse these items. Regulatory dates change quickly; checked October 2026.

---
## 1. Responsible AI: Principles and Why It Is an Interview Topic
> 🟡 Tier 3 · _Key points:_ Fairness, transparency, accountability, privacy, safety, human oversight; risk-based thinking

### Definition
**Responsible AI** is the set of practices that make an AI system lawful, fair, explainable, safe, secure, privacy-preserving and accountable across its life cycle. Common principles (OECD, NIST, EU, India's emerging guidance): **fairness and non-discrimination; transparency and explainability; accountability and human oversight; robustness, safety and security; privacy and data governance; societal and environmental well-being.**

Two organising frameworks worth naming:
- **NIST AI Risk Management Framework 1.0 (January 2023):** four functions, **Govern, Map, Measure, Manage**.
- **ISO/IEC 42001:2023:** a certifiable AI **management-system** standard (policies, roles, risk processes), similar in spirit to ISO 9001 for quality ([[011 Quality Management (TQM)]]).

Why it matters for placements: Product Managers own launch decisions and user harm ([[166 AI Product Management - LLM Products, Evals & Economics]]); consultants advise clients on AI risk; analysts build the models ([[098 Model Selection & Optimization]], [[096 Classification Algorithms]]). Interviewers test whether you can **spot a risk, quantify it, and propose controls**, not recite principles. Prerequisites: [[094 ML Fundamentals & Workflow]], [[100 ML for Product Management]].

### Example
A bank wants to use ML to pre-approve personal loans. Responsible-AI questions to ask: Is the data representative (rural applicants, women, thin-file borrowers)? Can an applicant be told why they were declined? Who can override? What is monitored monthly? Which regulation applies (RBI guidance, DPDP, and for an EU product the AI Act's high-risk rules for creditworthiness)?

### In the news
See news box. Both the EU and India are moving from principles to enforceable duties with dates and penalties.

### Interview angle
> [!question] How it is asked
> "What does responsible AI mean to you, and how would you apply it on a project?"

> [!tip] Strong answer includes
> - Principles tied to concrete controls (fairness test, explanation, human override, monitoring, documentation)
> - A risk-based approach: higher stakes mean more controls
> - A named framework (NIST AI RMF, ISO 42001) and relevant law (EU AI Act, DPDP)
> - One example from a project or case

---
## 2. Where Bias Comes From, and Real Incidents
> 🟡 Tier 3 · _Key points:_ Data, labels, proxies, feedback loops; COMPAS, Optum, Gender Shades, Amazon recruiting, Dutch benefits scandal

### Definition
Bias enters at every stage:
- **Historical/representation bias:** training data reflect past discrimination or miss groups.
- **Measurement/label bias:** the label is a poor proxy for the real target (cost used as a proxy for health need).
- **Proxy variables:** a feature correlated with a protected attribute (pin code, college, income) reintroduces it even if the attribute is removed ("fairness through unawareness" fails).
- **Sampling and survivorship bias:** only approved loans have repayment labels (reject inference problem).
- **Aggregation and evaluation bias:** one model for heterogeneous groups; test sets that under-represent minorities.
- **Feedback loops:** predictions change future data (predictive policing sends patrols where crime was recorded).
- **Deployment bias:** the model is used in a context it was not designed for.

Documented cases (each verified from a reference page checked October 2026):
- **COMPAS recidivism tool (ProPublica, 2016):** ProPublica found the tool biased against Black defendants on error rates; the vendor replied that it predicted recidivism equally accurately across races. Both claims can be true because **calibration and error-rate balance cannot both hold** when base rates differ (sub-topic 3).
- **Health-risk algorithm (Optum-type, study published 2019):** the algorithm used past healthcare cost as a proxy for need; Black patients incurred about $1,800 less in costs per year than white patients with similar need, so equally scored patients were not equally sick.
- **Gender Shades (2018):** commercial facial analysis had error rates of up to 35% for darker-skinned women versus under 1% for lighter-skinned men.
- **Amazon recruiting tool:** deactivated after it was found to penalise résumés containing the word "women's" and graduates of all-women's colleges.
- **Dutch childcare-benefits scandal:** roughly 26,000 parents were wrongly accused of fraud between 2005 and 2019 and the Rutte cabinet resigned on 15 January 2021; the data-protection authority found nationality and dual citizenship had been used in a discriminatory way. Source: [Wikipedia summary](https://en.wikipedia.org/wiki/Dutch_childcare_benefits_scandal); [COMPAS](https://en.wikipedia.org/wiki/COMPAS_(software)); [Algorithmic bias](https://en.wikipedia.org/wiki/Algorithmic_bias).

### Example
Proxy audit on the loan model in sub-topic 4: the protected attribute is **not** a model input, yet group B is approved at 49.8% versus 59.8% for group A, because average income differs between groups and income drives the score. Removing the attribute did not remove the disparity; the disparity came through a legitimate-looking feature. The audit question is then "is the gap explained by a business-necessary factor, and is there a less discriminatory alternative?"

### In the news
See news box. The EU omnibus added a legal basis to process special-category data for bias detection, because you cannot measure fairness without the attribute. (Reported in the Orrick summary.)

### Interview angle
> [!question] How it is asked
> "Your hiring model never sees gender. Can it still be biased?"

> [!tip] Strong answer includes
> - Yes: proxies, historical labels, uneven error rates
> - Test outcomes by group even if the attribute is excluded from training
> - Remedies: better data and labels, feature review, constraints or threshold adjustment, human review
> - Documented trade-offs and who signed off

---
## 3. Fairness Metrics: Demographic Parity, Equalised Odds and Calibration
> 🟡 Tier 3 · _Key points:_ Demographic parity, equal opportunity, equalised odds, predictive parity, disparate-impact ratio; impossibility result

### Definition
Let $\hat Y$ be the decision, $Y$ the true outcome and $A$ the protected group.

| Criterion | Requirement | Reads as |
|---|---|---|
| **Demographic (statistical) parity** | $P(\hat Y=1\mid A=a)$ equal across groups | same selection rate |
| **Disparate-impact ratio** | $\dfrac{P(\hat Y=1\mid A=\text{protected})}{P(\hat Y=1\mid A=\text{reference})}$ | the US "four-fifths rule" flags ratios below 0.8 (a screening rule of thumb from US employment guidance, not an Indian legal test) |
| **Equal opportunity** | equal true-positive rate $P(\hat Y=1\mid Y=1,A)$ | qualified people are accepted equally often |
| **Equalised odds** | equal TPR **and** equal FPR | error rates match across groups |
| **Predictive parity / calibration** | equal $P(Y=1\mid \hat Y=1,A)$ (PPV) or calibration by score | a given score means the same risk in each group |
| **Individual fairness** | similar individuals get similar outcomes | needs a similarity metric |
| **Counterfactual fairness** | decision unchanged if only the protected attribute changed (in a causal model) | needs a causal graph |

**Impossibility result** (Kleinberg et al., 2016; Chouldechova, 2017): when base rates differ between groups and the classifier is imperfect, calibration (predictive parity) and equalised odds cannot both hold. Choosing a metric is therefore a **policy and context decision**, not a purely technical one: lending often emphasises equal opportunity and calibration; hiring screens emphasise selection-rate ratios; medical triage emphasises error rates for the vulnerable group.

Mitigation families: **pre-processing** (reweighing, resampling), **in-processing** (fairness constraints or penalties), **post-processing** (group-specific thresholds). Each trades some accuracy or another fairness metric for the one targeted.

### Example
Small worked case. Group A: 100 applicants, 60 repay; the model approves 55 of those who repay and 10 of the 40 who would default. Group B: 100 applicants, 40 repay; approves 32 and 6 of the 60 who default.
- Selection rate A $=\frac{55+10}{100}=65\%$; B $=\frac{32+6}{100}=38\%$; ratio $=0.38/0.65=\mathbf{0.585}$ (below 0.8, fails the screening rule).
- TPR A $=55/60=91.7\%$; B $=32/40=80.0\%$ (gap 11.7 points).
- FPR A $=10/40=25\%$; B $=6/60=10\%$.
- PPV A $=55/65=84.6\%$; B $=32/38=84.2\%$: the model is **calibrated** across groups (about equal PPV) yet fails demographic parity and equalised odds because the groups have different base rates (60% vs 40% repaying). That is the impossibility result in miniature.

### In the news
See news box. High-risk credit scoring is named in the EU rules, and which metric you choose becomes part of the documentation regulators will ask for.

### Interview angle
> [!question] How it is asked
> "Demographic parity and equalised odds conflict. Which would you choose for a loan model and why?"

> [!tip] Strong answer includes
> - Define each metric precisely and show they can conflict
> - Choose by context: harm of false negatives vs false positives, legal exposure, stakeholder input
> - Report several metrics, document the choice and the trade-off
> - Propose monitoring by group after launch

---
## 4. Executed Example: A Fairness Audit of a Loan Model
> 🟡 Tier 3 · _Key points:_ Train without the protected attribute; audit by group; see what forced parity costs

### Definition
Simulated data (20,000 applicants, not real people). True repayment depends on income, debt and tenure only. Group A has higher average income (by 6 thousand on the scale used), so group A repays more often by construction. The protected attribute is **not** a model input. A gradient-boosting classifier is trained, and outcomes are audited by group on a held-out 40%.

### Example
```python
import numpy as np, pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
rng = np.random.default_rng(7)
n = 20000
group = rng.integers(0, 2, n)                                  # 0 = group A, 1 = group B (NOT a model input)
income = rng.normal(60 + 6*(group == 0), 18, n).clip(10)       # income differs by group (a proxy path)
tenure = rng.exponential(5, n); debt = rng.normal(30, 10, n).clip(0)
z = 0.045*(income-60) - 0.06*(debt-30) + 0.08*(tenure-5) + rng.normal(0, 0.8, n)
df = pd.DataFrame(dict(group=group, income=income, tenure=tenure, debt=debt, repay=(z > 0).astype(int)))
X, y = df.loc[:, ["income", "tenure", "debt"]], df.repay
Xtr, Xte, ytr, yte, gtr, gte = train_test_split(X, y, df.group, test_size=0.4, random_state=0)
m = GradientBoostingClassifier(random_state=0).fit(Xtr, ytr)
p = m.predict_proba(Xte)[:, 1]; pred = (p >= 0.5).astype(int)
print("AUC", round(roc_auc_score(yte, p), 3))
res = pd.DataFrame(dict(g=gte.values, y=yte.values, pred=pred, p=p))
def rates(r, pr):
    tpr = ((pr == 1) & (r.y == 1)).sum() / (r.y == 1).sum(); fpr = ((pr == 1) & (r.y == 0)).sum() / (r.y == 0).sum()
    ppv = ((pr == 1) & (r.y == 1)).sum() / (pr == 1).sum()
    return pr.mean(), tpr, fpr, ppv
for g in (0, 1):
    r = res[res.g == g]; a, t, f, pv = rates(r, r.pred)
    print(f"group {g}: approval {a:.3f} TPR {t:.3f} FPR {f:.3f} PPV {pv:.3f}")
a0, a1 = res[res.g == 0].pred.mean(), res[res.g == 1].pred.mean()
print("demographic parity diff", round(a1 - a0, 3), "disparate-impact ratio", round(a1 / a0, 3))
r1 = res[res.g == 1]; t1 = np.quantile(r1.p, 1 - a0); pr1 = (r1.p >= t1).astype(int)
print("group-B threshold for parity", round(t1, 3), [round(float(v), 3) for v in rates(r1, pr1)])
```

Output (AUC 0.884):

| Metric | Group A | Group B | Gap |
|---|---|---|---|
| Approval rate | 59.8% | 49.8% | −10.0 points; ratio 0.833 |
| True-positive rate | 84.9% | 80.2% | 4.7 points |
| False-positive rate | 25.6% | 21.2% | 4.4 points |
| Precision (PPV) | 81.9% | 78.0% | 3.9 points |

Reading it: the disparate-impact ratio of 0.833 passes the four-fifths screen narrowly, error rates are within about 5 points, and precision is close, so the model behaves similarly by group; the 10-point approval gap mirrors the underlying repayment gap (57.7% vs 48.5% base rates in the test data). **Forcing parity** by lowering group B's threshold from 0.5 to 0.348 lifts B's approval to 59.8% and TPR to 88.8%, but also raises its **FPR to 32.5%** and cuts PPV to 72.0%: more group-B approvals that default. That is the cost of choosing demographic parity over calibration here. Whether it is acceptable is a policy decision (and may be limited by law, since group-specific thresholds can be unlawful disparate treatment in some jurisdictions).

### In the news
See news box. The omnibus's new legal basis for processing special-category data for bias detection is exactly what makes an audit like this lawful in the EU.

### Interview angle
> [!question] How it is asked
> "How would you audit a model for bias if the protected attribute is not in the data?"

> [!tip] Strong answer includes
> - Obtain the attribute (or a lawful proxy such as surname/geography with caveats) only for auditing
> - Compare selection, TPR, FPR, PPV by group with confidence intervals
> - Explain the trade-offs of mitigation (parity vs calibration, accuracy cost)
> - Involve legal, risk and business owners in the choice

---
## 5. Explainability: Global vs Local, Intrinsic vs Post-hoc
> 🟡 Tier 3 · _Key points:_ Interpretable models first; post-hoc explanations are approximations; audiences differ

### Definition
**Explainability** answers "why did the model decide this?" for different audiences: the customer (reasons for adverse action), the regulator (model logic and controls), the data scientist (debugging), and the business owner (trust).

- **Intrinsic (interpretable) models:** linear/logistic regression, scorecards, shallow trees, GAMs, monotonic gradient boosting. Best when stakes are high and accuracy loss is small ([[090 Regression Analysis]], [[095 Regression Algorithms]]).
- **Post-hoc methods** for black boxes: **global** (what matters overall: permutation importance, partial dependence, mean absolute SHAP) and **local** (why this case: SHAP values, LIME, counterfactuals).
- **Caveats:** explanations describe the model, not reality; correlated features split credit unpredictably; explanations can be unstable and, if misused, **fairwash** a biased model; they do not replace testing.

Choosing: if a simple model gets within about 1 to 2 points of the black box, use it; otherwise pair a complex model with documented post-hoc explanations and limits.

### Example
Credit decision explanation for a customer must be short and actionable: "Your application was declined mainly because (1) your existing debt is high relative to income, (2) credit history is short." This is a top-reasons list (reason codes), which a scorecard produces natively and a black box produces through SHAP or counterfactual summaries.

### In the news
See news box. High-risk classes in the EU rules require transparency and human oversight; "explainable enough to be overseen" is the practical standard.

### Interview angle
> [!question] How it is asked
> "Would you use a black-box model for credit scoring? How would you explain its decisions?"

> [!tip] Strong answer includes
> - Benchmark an interpretable model first
> - If using a complex model: SHAP reason codes, monotonic constraints, stability checks
> - Separate audiences and needs (customer vs regulator vs developer)
> - Limits of explanations and a validation process independent of the developer

---
## 6. SHAP and LIME
> 🟡 Tier 3 · _Key points:_ Shapley-value attributions that sum to the prediction; LIME local surrogate; cautions

### Definition
**SHAP** (Lundberg and Lee, 2017) assigns each feature a Shapley value from cooperative game theory: the average marginal contribution of the feature over all orderings of features. Properties: **local accuracy** (base value plus all SHAP values equals the model output), missingness and consistency. For tree models, **TreeSHAP** computes exact values quickly. Global importance is the mean absolute SHAP value; plots include summary (beeswarm), dependence, force/waterfall.

For a tree classifier the output is in **log-odds**; apply the logistic function to convert: $p=\frac{1}{1+e^{-(\text{base}+\sum\phi_j)}}$.

**LIME** (Ribeiro et al., 2016) explains one prediction by sampling perturbed points around it, weighting them by proximity, and fitting a simple (sparse linear) **local surrogate**; the surrogate's coefficients are the explanation. It is model-agnostic and fast but sensitive to the sampling and kernel width, so explanations can vary between runs.

| | SHAP | LIME |
|---|---|---|
| Basis | Shapley values (axiomatic) | local linear surrogate |
| Additive to prediction | yes | no |
| Stability | high for TreeSHAP | can vary with sampling |
| Cost | cheap for trees, expensive for generic models | cheap per instance |

### Example
Executed on the loan model (sub-topic 4) with a gradient-boosting classifier. An applicant with income 50.3, tenure 3.2 years and debt 32.4 is predicted to repay with $p=0.151$ (declined). The base value is 0.26 log-odds; SHAP values are income −1.26, tenure −0.33, debt −0.41; the sum is $0.26-1.26-0.33-0.41=-1.72$ log-odds, and $\frac{1}{1+e^{1.72}}=0.152$, matching the model. **Reason codes:** (1) income is low relative to approved applicants, (2) debt is high, (3) tenure is short. Global mean |SHAP|: income 1.23, debt 0.95, tenure 0.52.

```python
import shap
# continues from sub-topic 4: m, Xte, X are defined there
ex = shap.TreeExplainer(m)                                   # m = fitted GradientBoostingClassifier
sv = ex.shap_values(Xte.iloc[:2000])                         # log-odds contributions
print(dict(zip(X.columns, abs(sv).mean(0).round(2))))        # income 1.23, tenure 0.52, debt 0.95
```

### In the news
See news box. As transparency duties spread, explanation artefacts such as SHAP reason codes become part of the evidence regulators and customers may request.

### Interview angle
> [!question] How it is asked
> "What is a SHAP value and what are its limitations?"

> [!tip] Strong answer includes
> - Average marginal contribution; contributions add up to prediction minus base
> - Local (one decision) and global (mean absolute) uses
> - Limits: correlated features, depends on the background data, explains the model not causality
> - Contrast with LIME's local surrogate and its instability

---
## 7. Partial Dependence, Permutation Importance and Counterfactual Explanations
> 🟡 Tier 3 · _Key points:_ Average effect curves; importance by shuffling; "what would need to change" explanations

### Definition
- **Partial dependence plot (PDP; Friedman, 2001):** average model output as a feature is varied over a grid while the others keep their observed values; shows the direction and shape of the average effect. **ICE** curves show one line per instance and reveal heterogeneity that the average hides. PDPs mislead when features are strongly correlated (they evaluate unrealistic combinations); **ALE plots** are an alternative.
- **Permutation importance:** the drop in a score (AUC) after randomly shuffling one feature on held-out data; model-agnostic, but split across correlated features.
- **Counterfactual explanations** (Wachter et al., 2017): the smallest change to the input that flips the decision ("if debt were ₹X lower, you would be approved"). They are actionable and intuitive, but must respect feasibility (do not suggest changing age or nationality) and legal limits.

### Example
On the loan model: permutation importance (AUC drop) income 0.224, debt 0.134, tenure 0.049, which agrees with the SHAP ranking. PDP of debt (log-odds, average) over debt 13.1, 21.5, 30.0, 38.4, 46.9: **1.93, 1.11, 0.18, −0.85, −1.80**, monotonically decreasing, as business logic expects. Counterfactual for the declined applicant (income 50.3, tenure 3.2, debt 32.4): cutting debt by **14.5** (to 17.9) lifts the repayment probability to **0.565**, so the actionable advice is "reduce outstanding debt by about 14.5 units".

```python
# continues from sub-topic 4 (m, Xte, yte, X) and the declined applicant x0
from sklearn.inspection import permutation_importance, partial_dependence
pi = permutation_importance(m, Xte, yte, n_repeats=5, random_state=0, scoring="roc_auc")
pdp = partial_dependence(m, Xte, ["debt"], grid_resolution=5)
x1 = x0.copy()                                   # x0 = the declined applicant (one-row DataFrame)
for d in np.arange(0, 40, 0.5):
    x1["debt"] = x0["debt"].values[0] - d
    if m.predict_proba(x1)[0, 1] >= 0.5: print("cut debt by", d); break
```

### In the news
See news box. Counterfactual reasons are the plain-language form closest to what a customer-facing transparency duty requires.

### Interview angle
> [!question] How it is asked
> "A customer asks what they can do to get approved. How would you answer from the model?"

> [!tip] Strong answer includes
> - Counterfactual: the smallest feasible change that flips the decision
> - Only mutable, legitimate features; no protected attributes
> - Caveat: the model changes over time and the quote is indicative
> - Combine with reason codes and a human channel

---
## 8. Model Documentation: Model Cards, Datasheets and the Audit Trail
> 🟡 Tier 3 · _Key points:_ Model card sections; datasheets for datasets; versioning and approvals

### Definition
**Model cards** (Mitchell et al., 2019, Google) are short structured documents accompanying a model. **Datasheets for datasets** (Gebru et al.) do the same for data. A practical model card:

| Section | Contents |
|---|---|
| Overview | name, version, owner, date, intended use and users |
| Out-of-scope uses | what it must not be used for |
| Data | sources, period, size, known gaps, labelling process |
| Method | algorithm, features, key hyperparameters, constraints |
| Performance | metrics overall and **by subgroup**, with confidence intervals |
| Fairness | metrics chosen, results, mitigation, rationale |
| Explainability | global importance, example reasons |
| Limitations and risks | failure modes, drift sensitivity, human-oversight points |
| Monitoring | metrics, thresholds, review cadence, rollback plan |
| Approvals | validation sign-off, risk owner, change log |

Governance basics: a **model inventory** (every model, owner, risk tier), independent **validation** of high-risk models, change control, and **audit trails** of data, code, parameters and decisions. Under the EU AI Act, high-risk systems need technical documentation, logging, human oversight and a risk-management system; the NIST AI RMF "Govern" function covers policies and accountability. Related practices: [[175 Data Quality, Master Data & Data Governance]].

### Example
A one-page model card for the loan model would state: "Intended use: pre-screen personal-loan applications for human review; not for final rejection without review. Data: 20,000 simulated applicants (illustrative). Performance: AUC 0.884; approval rates 59.8% (A) vs 49.8% (B); TPR 84.9% vs 80.2%; FPR 25.6% vs 21.2%. Limitations: protected attribute unavailable at inference; income is a proxy path; retrain if PSI on income exceeds 0.25."

### In the news
See news box. Documentation duties (technical file, logs, instructions for use) are a core part of the high-risk requirements, now due from December 2027 for stand-alone systems under the revised timetable.

### Interview angle
> [!question] How it is asked
> "What documentation would you want before approving a model for production?"

> [!tip] Strong answer includes
> - Intended use and limits, data lineage, performance by subgroup, fairness results
> - Validation by an independent party; approval and change log
> - Monitoring plan and rollback
> - Model inventory and risk tiering

---
## 9. Monitoring and Drift: PSI, KS and Performance Decay
> 🟡 Tier 3 · _Key points:_ Data drift vs concept drift; PSI thresholds; KS statistic; label delay

### Definition
Models degrade because the world changes. **Data (covariate) drift:** input distribution shifts. **Concept drift:** the relationship between inputs and outcome changes (a new regulation, a pandemic). **Label shift:** the outcome rate changes. **Upstream data issues:** schema changes, units, missing feeds.

**Population Stability Index (PSI)** compares a baseline (expected) distribution with a current (actual) one across $B$ bins:

$$PSI=\sum_{i=1}^{B}(a_i-e_i)\ln\frac{a_i}{e_i}$$

Common industry rule of thumb (from credit-risk practice, not a statutory standard): **below 0.10 stable; 0.10 to 0.25 moderate shift, investigate; above 0.25 significant shift, act**. **Kolmogorov-Smirnov (KS) statistic** is the maximum gap between two cumulative distributions, $D=\sup_x|F_1(x)-F_2(x)|$, with a p-value from `scipy.stats.ks_2samp`; with large samples tiny shifts become "significant", so judge **size** (D, PSI) not only p ([[205 Sampling Distributions & Estimation]], [[206 Non-Parametric Tests]]). For accuracy monitoring, labels arrive late (loan default takes months), so track proxies: input drift, score distribution, approval rate, and early-delinquency indicators; **control charts** work well for rate metrics ([[091 Statistical Quality Control (SQC)]]).

### Example
Hand PSI with 5 bins: expected shares 10%, 20%, 30%, 25%, 15%; actual 5%, 15%, 30%, 30%, 20%. Terms: $(−0.05)\ln0.5=0.0347$; $(−0.05)\ln0.75=0.0144$; $0$; $(0.05)\ln1.2=0.0091$; $(0.05)\ln1.333=0.0144$. **PSI = 0.0725**, stable. Simulated checks (10,000 draws each; baseline Normal(60, 18)):

```python
import numpy as np
from scipy import stats
rng = np.random.default_rng(7)
def psi(expected, actual, bins=10):
    edges = np.quantile(expected, np.linspace(0, 1, bins + 1)); edges[0], edges[-1] = -np.inf, np.inf
    pe = np.clip(np.histogram(expected, edges)[0] / len(expected), 1e-6, None)
    pa = np.clip(np.histogram(actual, edges)[0] / len(actual), 1e-6, None)
    return float(np.sum((pa - pe) * np.log(pa / pe)))
base = rng.normal(60, 18, 10000)
for name, new in [("no change", rng.normal(60, 18, 10000)), ("mean +6", rng.normal(66, 18, 10000)), ("SD 18 -> 26", rng.normal(60, 26, 10000))]:
    print(f"{name:12s} PSI {psi(base, new):.3f}  KS {stats.ks_2samp(base, new).statistic:.3f}")
```

| Scenario | PSI | KS | Verdict |
|---|---|---|---|
| No change | 0.001 | 0.009 | stable |
| Mean up by 6 (a third of an SD) | 0.121 | 0.145 | moderate, investigate |
| SD from 18 to 26 | 0.170 | 0.095 | moderate, investigate |

### In the news
See news box. Post-market monitoring and incident reporting are central obligations in the EU high-risk regime, so drift metrics become compliance evidence as well as engineering hygiene.

### Interview angle
> [!question] How it is asked
> "How do you know your model is still working six months after launch?"

> [!tip] Strong answer includes
> - Input drift (PSI/KS), score distribution, outcome metrics when labels arrive, by segment
> - Thresholds and owners; alert, investigate, retrain, rollback
> - Label delay and proxy metrics
> - Distinguish data drift from concept drift

---
## 10. Human-in-the-Loop, LLM Risks and the Air Canada Ruling
> 🟡 Tier 3 · _Key points:_ Oversight design; automation bias; hallucination liability; escalation paths

### Definition
**Human-in-the-loop (HITL)** places a person in the decision (approve each case); **human-on-the-loop** has the person supervising and intervening; **human-in-command** keeps overall control. Good design needs: meaningful authority to override, enough information and time, **training on automation bias** (over-trusting the machine), escalation paths, and logging of overrides (override rate and reasons are a monitoring signal: ~0% overrides may mean rubber-stamping, very high may mean a poor model).

**Routing by confidence and stakes:** auto-approve clear low-risk cases, send uncertain or high-impact cases to people. This is the practical basis for "human oversight" duties.

**LLM-specific risks:** hallucinated facts, prompt injection, data leakage, toxic output, over-reliance. Controls: grounding on approved sources, refusal and escalation, output filtering, rate limits, red-teaming, and clear disclosure ([[219 NLP, Embeddings & LLM Applications for Analysts]], [[166 AI Product Management - LLM Products, Evals & Economics]]).

**Case, Moffatt v. Air Canada (14 Feb 2024):** a customer relied on the airline's website chatbot, which said he could buy full-price tickets and claim a bereavement refund within 90 days. The British Columbia Civil Resolution Tribunal held Air Canada responsible for what its chatbot said, rejected the argument that the chatbot was a separate legal entity, found negligent misrepresentation, and awarded CA$812 plus costs and interest. The amount is small; the principle is not: **the company owns its AI's statements.** Source: [Wikipedia, Moffatt v. Air Canada](https://en.wikipedia.org/wiki/Moffatt_v._Air_Canada).

### Example
Loan pre-screening with routing: $p\ge0.80$ auto-approve to a human spot-check (5% sampled); $0.35\le p<0.80$ mandatory human review with SHAP reason codes; $p<0.35$ decline with reasons and an appeal route. If analysts override 2% of approvals and 40% of mid-band cases, review resources go to the mid-band; if overrides drop to 0% after a month, investigate rubber-stamping.

### In the news
See news box. EU Article 50 requires telling users when they interact with an AI system (chatbots) from August 2026; the Air Canada case shows the liability that exists even without that rule.

### Interview angle
> [!question] How it is asked
> "How would you deploy a customer-service chatbot responsibly?"

> [!tip] Strong answer includes
> - Grounded answers from approved content, citations, refusal when unsure
> - Disclosure that it is an AI, escalation to a human, logging
> - Evaluation set, red-teaming, and monitoring of complaints and overrides
> - Accountability: the company owns the outputs (Air Canada)

---
## 11. EU AI Act: Risk Tiers and Timeline
> 🟡 Tier 3 · _Key points:_ Unacceptable, high, limited, minimal; GPAI; penalties; dates checked October 2026

### Definition
The **EU AI Act (Regulation (EU) 2024/1689)** entered into force on **1 August 2024** and regulates by **risk tier**:

| Tier | Examples | Obligation |
|---|---|---|
| **Unacceptable (prohibited)** | social scoring, certain manipulative or exploitative AI, some real-time remote biometric identification in public, untargeted face-image scraping; since the omnibus, AI generating non-consensual intimate imagery and child sexual abuse material | banned; prohibitions applied from 2 February 2025 (the new ones from 2 December 2026) |
| **High risk** | Annex III uses: employment and worker management, creditworthiness and essential services, education, law enforcement, migration, justice, critical infrastructure; Annex I: AI as a safety component of regulated products | risk management, data governance, technical documentation, logging, transparency, human oversight, accuracy and robustness, conformity assessment, post-market monitoring |
| **Limited risk (transparency)** | chatbots, deepfakes, synthetic content, emotion recognition | disclosure and machine-readable marking (Article 50) |
| **Minimal risk** | spam filters, most recommenders | no specific obligation |
| **General-purpose AI (GPAI)** | foundation and LLMs | transparency and documentation duties since 2 August 2025; extra obligations for models with systemic risk (training compute above $10^{25}$ FLOPs) |

**Penalties:** up to EUR 35 million or 7% of worldwide turnover for prohibited practices; EUR 15 million or 3% for other obligations; EUR 7.5 million or 1% for supplying incorrect information (SMEs get lower caps). **Revised timetable:** Annex III high-risk obligations now **2 December 2027**, Annex I **2 August 2028**, Article 50 transparency **2 August 2026** (watermarking grace to 2 December 2026 for existing systems). **Extraterritorial:** applies to non-EU providers whose output is used in the EU, so Indian IT and SaaS firms serving European clients are in scope. Sources: Wikipedia overview and the law-firm summaries in the news box.

### Example
Classify five systems for an Indian bank's European arm: (1) a CV-screening tool for hiring: **high risk** (employment); (2) a credit-scoring model for retail loans: **high risk** (creditworthiness); (3) a customer chatbot: **limited risk**, must disclose it is AI; (4) a fraud-detection model on card transactions: fraud detection is carved out of the creditworthiness category in the Act's text, so typically not high-risk (confirm with counsel); (5) an internal spell-check assistant: **minimal risk**.

### In the news
See news box for the revised dates and the new prohibition. The timetable slid by 16 months for stand-alone high-risk systems, which gives a longer runway but does not remove the requirement.

### Interview angle
> [!question] How it is asked
> "Our client sells an HR analytics tool in Europe. What does the AI Act mean for them?"

> [!tip] Strong answer includes
> - It is likely high risk (employment); list obligations (risk management, documentation, human oversight, monitoring)
> - Timeline (Dec 2027 after the omnibus) and penalties
> - Extraterritorial scope; role of provider vs deployer
> - A practical plan: inventory, classify, gap assessment, controls, documentation

---
## 12. India: DPDP Act 2023, DPDP Rules 2025 and the Emerging AI Rules
> 🟡 Tier 3 · _Key points:_ Consent, data fiduciary duties, children, breach notification, penalties up to ₹250 crore, no standalone AI law

### Definition
**Digital Personal Data Protection Act, 2023** (Presidential assent 11 August 2023): governs processing of digital personal data in India (and offline data that is digitised; also processing abroad when offering goods or services in India). Key concepts:
- **Data Principal** (individual) and **Data Fiduciary** (the organisation deciding purpose and means); **Significant Data Fiduciaries** (by volume and sensitivity) carry extra duties such as an India-based Data Protection Officer, an independent data auditor and periodic impact assessments.
- **Consent** must be free, specific, informed and unambiguous with a clear notice; legitimate-use exceptions exist (for example voluntary sharing, government benefits, medical emergencies, employment).
- **Rights:** access to information, correction and erasure, consent withdrawal, grievance redressal, nomination of another person; no right to data portability or "right to be forgotten" in the final text.
- **Children:** verifiable parental consent; processing that is detrimental to a child's well-being, including tracking, behavioural monitoring and targeted advertising, is barred.
- **Security and breach:** reasonable security safeguards and breach intimation to the Board and affected individuals.
- **Enforcement:** the **Data Protection Board of India** adjudicates; appeals go to TDSAT. Maximum penalties in the Schedule reach **₹250 crore** (failure to take security safeguards) and **₹200 crore** (children's data obligations, breach notification).
- **DPDP Rules, 2025** were notified on 14 November 2025 with an 18-month phased compliance period; consent managers must be Indian companies. By the Wikipedia summary, the Board provisions commenced at notification, a further tranche follows in November 2026 and the remaining substantive duties around May 2027 (verify exact dates against the Gazette).

**AI specifics:** India has no standalone binding AI statute as of this check. AI deployment sits under existing law (DPDP for personal data used in training or prompts, sectoral regulators such as RBI and SEBI, consumer-protection and IT law, and the February 2026 amendment on synthetic content). Practical implications for ML teams: purpose limitation (do not reuse customer data for a new model without a lawful basis), data minimisation, erasure and retention rules for training data and logs, breach readiness, and vendor/processor contracts when sending personal data to external LLM APIs ([[175 Data Quality, Master Data & Data Governance]]). The IndiaAI Mission (₹10,371.92 crore allocation over 2024-2029 per Wikipedia) funds compute and datasets but is not a compliance regime.

### Example
A retailer wants to fine-tune a customer-support model on 2 million past chat transcripts containing names, phone numbers and order details. Controls: confirm lawful basis and notice cover the purpose; strip or pseudonymise identifiers; restrict access; set retention; check whether the vendor is a processor under contract; plan for erasure requests (can you remove an individual's data from training sets?); log access; prepare a breach playbook. Exposure if safeguards fail: up to ₹250 crore per the Act's Schedule.

### In the news
See news box for the Rules notification and the synthetic-content amendment. Obligations are phased, so build compliance now rather than waiting for the final date.

### Interview angle
> [!question] How it is asked
> "We want to use customer data to train a model. What do we need to consider under Indian law?"

> [!tip] Strong answer includes
> - Lawful basis and notice, purpose limitation, minimisation
> - Security safeguards, breach notification, retention and erasure
> - Children's data and Significant Data Fiduciary duties if applicable
> - Vendor contracts for external LLM APIs; penalty exposure (up to ₹250 crore)
> - Honest limits: the AI-specific rules are still evolving; consult counsel

---
## 13. AI Risk Register and Governance Operating Model
> 🟡 Tier 3 · _Key points:_ Likelihood-impact scoring; owners and controls; three lines of defence; tiering

### Definition
An **AI risk register** lists risks per model or use case with likelihood, impact, controls, owner, residual risk and review date. Score likelihood and impact on 1 to 5, rating = likelihood × impact (1 to 25), with bands such as 1 to 6 low, 7 to 14 medium, 15 to 25 high. Categories: data quality and bias, model performance and drift, explainability, security (adversarial inputs, data poisoning, prompt injection), privacy and legal, operational resilience, third-party/vendor, reputational and ethical, misuse.

**Operating model (three lines of defence):** (1) business and model owners build and run with controls; (2) independent risk, compliance and model-validation teams set policy and challenge; (3) internal audit provides assurance. An **AI governance committee** approves high-risk use cases; tiering (high/medium/low) decides the depth of review. Link risk management practice to [[040 Risk & Stakeholder Management]] and enterprise risk thinking in [[015 Supply Chain Risk & Resilience]].

### Example
| Risk | L | I | Score | Control | Owner |
|---|---|---|---|---|---|
| Disparate approval rates by group | 3 | 5 | **15** (high) | quarterly fairness audit, thresholds, human review of mid-band | Chief Risk Officer |
| Input drift (income PSI above 0.25) | 4 | 3 | **12** (medium) | weekly PSI dashboard, retrain trigger | Model owner |
| Personal data leak via external LLM API | 2 | 5 | **10** (medium) | no PII in prompts, vendor DPA, redaction | CISO and DPO |
| Chatbot states a wrong policy | 3 | 4 | **12** (medium) | grounded answers, escalation, disclosure | Product owner |
| Model unavailable (vendor outage) | 2 | 4 | **8** (medium) | fallback to rules-based scoring | Operations |

Rank by score, assign owners, set review dates, and track residual risk after controls.

### In the news
See news box. Registers and inventories are the evidence that regulators and auditors ask for, under both the EU rules and Indian data-protection duties.

### Interview angle
> [!question] How it is asked
> "Build a risk register for an AI claim-triage system."

> [!tip] Strong answer includes
> - Risk categories, likelihood-impact scores, controls, owners and review cadence
> - Ranking by severity and focus on top risks
> - Link to monitoring metrics and thresholds
> - Governance: tiering, independent validation, escalation, incident process

---
## 14. ⭐ Advanced: Interview Framing for Responsible-AI Questions
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A reusable structure for any responsible-AI case or opinion question, in about two minutes:

1. **Stakes and stakeholders:** who is affected, how badly, reversibly?
2. **Risks:** bias, error, privacy, security, misuse, over-reliance (name the top two or three for this case).
3. **Measures:** how you would test (subgroup metrics, drift, red-team) and the metric choice with trade-off.
4. **Controls:** human oversight, explanations, documentation, monitoring, rollback.
5. **Law and policy:** EU AI Act tier, DPDP duties, sector regulators.
6. **Decision:** ship, ship with guardrails, pilot, or stop; with criteria and a review date.

Pitfalls to avoid: treating fairness as a single number; claiming a model is "unbiased"; ignoring business value (a safe model nobody uses is not a success); vague answers without metrics; absolutist rejection of AI. Show **judgement**: "I would launch in a pilot to 5% of applications with human review of the mid-band, monitor approval-rate parity and drift weekly, and expand if PSI stays under 0.10 and the disparate-impact ratio stays above 0.8, subject to legal review." Connect to monitoring tools in [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]] and statistical reasoning in [[215 Statistics Interview Question Bank & Numericals]].

### Example
Prompt: "An Indian health-tech startup wants an AI that prioritises patients for teleconsultation by predicted severity. Thoughts?" Model answer: stakes are high (delayed care); main risks are label bias (past utilisation as proxy for need, as in the cost-proxy case), poor performance for under-served groups, and over-reliance by triage staff. Measures: sensitivity by group for severe cases (equal opportunity), calibration, drift by region. Controls: never auto-deny, clinician override, explanation of drivers, consent and data minimisation under DPDP, incident log. Decision: pilot with clinician review, stop criteria if sensitivity for any group falls more than 5 points below the average.

### In the news
See news box. Employers and regulators are asking candidates for a defensible view on AI risk, not only technical skill.

### Interview angle
> [!question] How it is asked
> "Is it ethical to use AI for hiring or lending decisions?"

> [!tip] Strong answer includes
> - It depends on stakes, design and controls, and can be better or worse than human decisions
> - Specific safeguards: audits by group, explanations, human review, appeals
> - Regulatory awareness (high-risk tier, DPDP)
> - A clear recommendation with conditions, not a lecture
