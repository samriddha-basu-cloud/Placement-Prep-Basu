---
tags: [machine-learning, tier2]
area: Machine Learning
topic: "Model Selection & Optimization"
tier: Tier 2
roles: PM / Operations
status: complete
subtopics: 12
---
# Model Selection & Optimization

⬅ [[097 Unsupervised Learning]] · [[_Index - Machine Learning|Machine Learning]] · [[099 ML for Operations & SCM]] ➡

> **Area:** Machine Learning · **Priority:** 🟠 Tier 2 · **Target roles:** PM / Operations

## Sub-topics in this note
1. [[#1. Hyperparameter Tuning]]
2. [[#2. GridSearchCV]]
3. [[#3. Learning Curves]]
4. [[#4. Feature Importance]]
5. [[#5. SHAP Values]]
6. [[#6. Ensemble Methods]]
7. [[#7. Model Calibration]]
8. [[#8. Regularization Comparison]]
9. [[#9. Pipeline in sklearn]]
10. [[#10. MLOps Basics]]
11. [[#11. ⭐ Advanced: Bayesian Optimization and Optuna]]
12. [[#12. ⭐ Advanced: Nested Cross-Validation and Honest Model Selection]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): AI scales fast, so tuning, explainability and MLOps become the bottleneck
> **Stanford AI Index 2025 (April 2025).** 78% of organisations reported using AI in 2024, up from 55% in 2023; the inference cost of a system at GPT-3.5 level fell over 280-fold between Nov 2022 and Oct 2024; US private AI investment was $109.1 bn in 2024. As deployment widens, the challenge shifts from building one model to selecting, explaining and maintaining many. ([Business Wire summary of the Stanford HAI report](https://www.businesswire.com/news/home/20250407539812/en/Stanford-HAIs-2025-AI-Index-Reveals-Record-Growth-in-AI-Capabilities-Investment-and-Regulation))
>
> **RBI's MuleHunter.AI (Dec 2024 to Dec 2025).** An ML tool from the RBI Innovation Hub, developed from 19 mule-account behaviour patterns, piloted at two public sector banks and implemented by 23 banks by 10 Dec 2025. RBI declined to disclose how many mule accounts it found citing fiduciary and competitive concerns, an illustration of the monitoring and transparency questions around deployed models. The sources do not describe its algorithm. ([Business Standard](https://www.business-standard.com/finance/personal-finance/explained-rbi-has-a-new-ai-tool-mulehunter-ai-to-reduce-digital-frauds-124120900250_1.html), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Hyperparameter Tuning
> 🟠 Tier 2 · _Tracker hint:_ Grid Search (exhaustive), Random Search (faster), Bayesian Optimization (smarter)

### Definition
**Parameters** are learned from data (coefficients, tree splits); **hyperparameters** are set before training (learning rate, `max_depth`, `C`, $\lambda$, number of trees). Tuning searches for the best values using validation performance (cross-validation).

| Method | Idea | Pros / cons |
|---|---|---|
| Grid search | Try every combination | Simple, exhaustive; cost explodes with parameters |
| Random search | Sample combinations at random | Often as good with far fewer trials (Bergstra and Bengio); explores important parameters better |
| Bayesian optimisation | Build a surrogate (e.g. Gaussian process, TPE) of score vs parameters, pick the next promising point | Fewer trials; harder to parallelise (Optuna, Hyperopt) |
| Successive halving / Hyperband | Drop poor candidates early | Saves compute |

Rules: tune on validation folds only, keep the test set untouched, fix a budget, use sensible ranges (log-scale for learning rate, $C$, $\lambda$).

### Example
Grid over `n_estimators` in {100, 300, 500} × `max_depth` in {3, 5, 7, 9} = 12 combinations; with 5-fold CV = **60 fits**. Random search with 20 samples from continuous ranges = 100 fits, covering more distinct values per parameter.

### In the news
See news box. With 78% of firms using AI and compute getting cheaper, automated tuning is increasingly default, but unchecked tuning on the same data inflates reported performance.

### Interview angle
> [!question] How it is asked
> "How would you tune hyperparameters for a gradient boosting model on a limited budget?"

> [!tip] Strong answer includes
> - Parameters versus hyperparameters
> - Random or Bayesian search over grid for many parameters, log-scale ranges
> - Cross-validation and keeping the test set untouched
> - Early stopping and budget awareness

---

## 2. GridSearchCV
> 🟠 Tier 2 · _Tracker hint:_ sklearn.model_selection.GridSearchCV; param_grid dict; cv folds; scoring metric

### Definition
`GridSearchCV` runs cross-validation for every combination in a `param_grid` and refits the best model on all training data (`refit=True`).

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = {"n_estimators": [100, 300], "max_depth": [5, 10, None], "min_samples_leaf": [1, 5]}
gs = GridSearchCV(RandomForestClassifier(random_state=0), param_grid,
                  cv=5, scoring="f1", n_jobs=-1, refit=True)
gs.fit(X_train, y_train)
print(gs.best_params_, gs.best_score_)
best = gs.best_estimator_          # evaluate once on X_test
```

Key arguments: `cv` (int or splitter such as `StratifiedKFold`, `TimeSeriesSplit`), `scoring` (`"roc_auc"`, `"neg_root_mean_squared_error"`, `"f1"`...; sklearn maximises scores, so errors are negated), `n_jobs`, `cv_results_`. Related: `RandomizedSearchCV(n_iter=...)`, `HalvingGridSearchCV`. To tune preprocessing too, pass a `Pipeline` and use `step__param` names.

### Example
Grid above: 2 × 3 × 2 = 12 combinations × 5 folds = **60 fits**, plus 1 final refit. If `gs.best_score_` = 0.81 (CV F1) but the test F1 = 0.80, the estimate is consistent; if the test F1 were 0.70, suspect leakage or overfitting to the CV folds.

### In the news
See news box. Cheaper compute makes brute-force grids affordable, but reproducibility (fixed seeds, logged parameters) matters once models are audited.

### Interview angle
> [!question] How it is asked
> "Write or explain GridSearchCV. How many model fits will it run?"

> [!tip] Strong answer includes
> - Combinations × folds (+ refit) arithmetic
> - Scoring metric matched to the business (not default accuracy)
> - Wrap preprocessing in a Pipeline to avoid leakage
> - Evaluate best model once on the untouched test set

---

## 3. Learning Curves
> 🟠 Tier 2 · _Tracker hint:_ Train vs validation error, training size; diagnose bias/variance; when to get more data

### Definition
A **learning curve** plots training and validation performance versus training-set size (or versus epochs/complexity for validation curves).

| Pattern | Diagnosis | What to do |
|---|---|---|
| Both errors high and converged close together | **High bias** (underfit) | Richer model/features, less regularisation; more data will **not** help |
| Large gap: train error low, validation high | **High variance** (overfit) | More data, regularise, simplify, ensemble |
| Validation error still falling at max size | Data-limited | Collect more data |
| Both low and close | Good fit | Ship |

It tells you where to invest: data, features or model capacity.

```python
from sklearn.model_selection import learning_curve
sizes, tr, va = learning_curve(model, X, y, cv=5, train_sizes=[0.1,0.3,0.5,0.7,1.0], scoring="neg_root_mean_squared_error")
```

### Example
At 10,000 rows: train RMSE 4, validation RMSE 9 (gap 5). At 40,000 rows: train 5, validation 7 (gap 2). Gap shrinking and validation still improving means more data helps. If instead both stuck near 8, the model is underfit and a more expressive model or new features is needed. (Illustrative numbers.)

### In the news
See news box. With AI investment high ($109.1 bn in the US in 2024), "should we collect more data or fix the model?" is a real budgeting question that learning curves answer cheaply.

### Interview angle
> [!question] How it is asked
> "Your model underperforms. Would more data help?"

> [!tip] Strong answer includes
> - Plot train and validation curves versus data size
> - Reads gap (variance) and level (bias)
> - Clear actions for each diagnosis
> - Links to cost of data collection

---

## 4. Feature Importance
> 🟠 Tier 2 · _Tracker hint:_ Random Forest: impurity-based; XGBoost: gain-based; SHAP values: model-agnostic

### Definition
Feature importance ranks how much each input drives predictions.

- **Impurity-based (Gini/MDI)** in random forests: total impurity reduction from splits on a feature. Fast but **biased** towards high-cardinality and continuous features, and computed on training data.
- **Gain / cover / weight** in XGBoost: gain (average loss improvement per split on the feature) is most meaningful; weight (split count) is misleading.
- **Permutation importance:** shuffle one feature on held-out data and measure the score drop; model-agnostic, but understated for correlated features.
- **Coefficients** (scaled) for linear models.
- **SHAP:** consistent, local plus global attribution (next topic).

Importance is not causality, and correlated features share or hide importance.

```python
from sklearn.inspection import permutation_importance
r = permutation_importance(model, X_val, y_val, n_repeats=10, scoring="roc_auc", random_state=0)
```

### Example
A churn model's permutation importance: shuffling `tenure` drops AUC by 0.08, `support_calls` by 0.05, `city` by 0.00. So tenure matters most, city adds nothing (candidate to drop). (Illustrative.)

### In the news
See news box. As models spread across regulated sectors, being able to say which features drive decisions is increasingly expected, though RBI declined to disclose mule-account results, so transparency has limits in practice.

### Interview angle
> [!question] How it is asked
> "How do you find out which features drive your model? Can you trust impurity importance?"

> [!tip] Strong answer includes
> - Methods and when each is used
> - Impurity bias and the permutation or SHAP alternative
> - Correlated features caveat
> - Importance is not causation

---

## 5. SHAP Values
> 🟠 Tier 2 · _Tracker hint:_ SHapley Additive exPlanations; feature contribution per prediction; explainable AI

### Definition
**SHAP** applies **Shapley values** from cooperative game theory: a feature's contribution is its average marginal effect on the prediction over all feature orderings. Properties: **additivity** and consistency.

$$f(x)=\phi_0+\sum_{j=1}^{M}\phi_j,\qquad \phi_0=E[f(X)]\ (\text{base value})$$

Positive $\phi_j$ pushes the prediction up from the average, negative pushes down. `TreeExplainer` is exact and fast for tree models; `KernelExplainer`/`DeepExplainer` for others. Plots: **force/waterfall** (one prediction), **beeswarm/summary** (global: mean $|\phi|$ gives importance and shows direction), **dependence** plots. Caveats: explains the model, not causality; correlated features; compute cost for non-tree models.

```python
import shap
explainer = shap.TreeExplainer(model)
sv = explainer.shap_values(X_val)
shap.summary_plot(sv, X_val)
```

### Example
Churn model with average predicted probability 0.30. For one customer: tenure +0.25, support calls +0.10, discount received -0.05. Prediction = 0.30 + 0.25 + 0.10 - 0.05 = **0.60**. The contributions sum exactly to the gap from the base value, so the account manager sees why this customer is flagged.

### In the news
See news box. Explainability is a practical need when AI decisions affect customers' accounts, as with fraud flags on bank accounts. The sources on MuleHunter.AI do not state what explanation methods it provides.

### Interview angle
> [!question] How it is asked
> "How would you explain an individual model prediction to a business user or regulator?"

> [!tip] Strong answer includes
> - Shapley intuition and the additive decomposition
> - Local (waterfall) versus global (summary) use
> - Limits: association not causation; correlated features
> - Practical: show top 3 reasons per decision

---

## 6. Ensemble Methods
> 🟠 Tier 2 · _Tracker hint:_ Bagging (Random Forest), Boosting (XGBoost), Stacking (meta-model on base models)

### Definition
Ensembles combine many models for better accuracy and stability.

| Method | How | Reduces | Example |
|---|---|---|---|
| **Bagging** | Train models in parallel on bootstrap samples; average/vote | Variance | Random Forest |
| **Boosting** | Train sequentially, each focusing on previous errors | Bias (and some variance) | AdaBoost, XGBoost, LightGBM |
| **Stacking** | Base models' out-of-fold predictions feed a **meta-model** | Both, through diversity | Logistic regression on RF + GBM + SVM outputs |
| **Voting / blending** | Average or weighted vote | Variance | Simple averaging |

Works when models are **diverse** and individually better than chance. Costs: complexity, latency, explainability. Stacking must use out-of-fold predictions to avoid leakage.

```python
from sklearn.ensemble import StackingClassifier
st = StackingClassifier(estimators=[("rf", rf), ("gb", gb)], final_estimator=LogisticRegression(), cv=5)
```

### Example
Three **independent** classifiers each 70% accurate, majority vote: P(correct) = 3(0.7²)(0.3) + 0.7³ = 3(0.49)(0.3)+0.343 = 0.441+0.343 = **0.784**. In practice errors are correlated, so gains are smaller, which is why diversity matters.

### In the news
See news box. Competition-style stacking gets headlines, but production teams weigh the small accuracy gains against latency and maintenance cost.

### Interview angle
> [!question] How it is asked
> "Bagging versus boosting versus stacking?"

> [!tip] Strong answer includes
> - Parallel/variance versus sequential/bias versus meta-learner
> - Diversity requirement
> - Overfitting risk of boosting and leakage risk of stacking
> - Production trade-off: accuracy versus complexity

---

## 7. Model Calibration
> 🟠 Tier 2 · _Tracker hint:_ Platt scaling, isotonic regression; align predicted probabilities with actual outcomes

### Definition
A model is **calibrated** if, among cases predicted at probability $p$, about a fraction $p$ are actually positive. Many models (random forest, boosting, SVM, Naive Bayes, neural nets) rank well but give distorted probabilities. Calibration matters whenever you use the **probability value**: expected-cost decisions, thresholds, pricing, risk.

- **Reliability diagram:** predicted probability bins versus observed frequency (diagonal is ideal).
- **Metrics:** Brier score $=\frac1n\sum(p-y)^2$, expected calibration error, log-loss.
- **Platt scaling:** fit $P(y=1\mid f)=\frac{1}{1+e^{Af+B}}$ on held-out scores (parametric; works for S-shaped distortion, small data).
- **Isotonic regression:** non-parametric monotonic mapping (flexible; needs more data, can overfit).
Calibrate on a separate set or by cross-validation.

```python
from sklearn.calibration import CalibratedClassifierCV
cal = CalibratedClassifierCV(model, method="isotonic", cv=5).fit(X_train, y_train)
```

### Example
Customers scored 0.80 by the model repay on time only 60% of the time (over-confident). Brier contribution for a positive case scored 0.8: $(0.8-1)^2=0.04$; for a negative scored 0.8: $(0.8-0)^2=0.64$. After calibration the 0.80 bucket maps to about 0.60, so expected-loss calculations become correct.

### In the news
See news box. Where decisions turn on probability thresholds (freeze or not, lend or not), miscalibration translates directly into mis-sized false positives.

### Interview angle
> [!question] How it is asked
> "Your model has AUC 0.9 but the business says the probabilities look off. What do you check?"

> [!tip] Strong answer includes
> - Ranking (AUC) versus calibration are different
> - Reliability diagram and Brier score
> - Platt versus isotonic and when each applies
> - Calibrate on held-out data

---

## 8. Regularization Comparison
> 🟠 Tier 2 · _Tracker hint:_ L1→sparsity+feature selection; L2→weight shrinkage; Dropout (neural nets)→co-adaptation

### Definition
Regularisation adds a complexity cost to reduce overfitting (variance).

| Technique | Penalty / mechanism | Effect |
|---|---|---|
| **L1 (Lasso)** | $\lambda\sum\lvert w\rvert$ | Sparse weights, feature selection |
| **L2 (Ridge / weight decay)** | $\lambda\sum w^2$ | Shrinks all weights smoothly, handles collinearity |
| **Elastic Net** | Both | Sparse plus grouped |
| **Dropout** | Randomly zero units (rate $p$) during training | Prevents co-adaptation; ensemble-like effect |
| **Early stopping** | Stop when validation loss rises | Implicit regularisation |
| **Tree controls** | `max_depth`, `min_samples_leaf`, pruning, `subsample` | Limits capacity |
| **Data augmentation** | More varied examples | Less memorisation |

In logistic regression and SVM, sklearn's `C` is the **inverse** of $\lambda$ (small $C$ = strong regularisation). Tune strength by CV; scale features first.

### Example
Weights (3.0, 0.4), $\lambda=0.5$: L2 (orthonormal) divides by $1+\lambda$: (2.0, 0.267), nothing zero. L1 soft-threshold subtracts $\lambda$: (2.5, **0**), the weak feature is removed. Dropout with $p=0.5$ on a hidden layer of 100 units randomly switches off about 50 units each training step.

### In the news
See news box. As models grow (and become cheap to run), regularisation is what keeps them from memorising noise.

### Interview angle
> [!question] How it is asked
> "Compare L1, L2 and dropout."

> [!tip] Strong answer includes
> - Penalty forms and geometry
> - Sparsity versus shrinkage versus co-adaptation
> - Which model class each belongs to
> - Hyperparameter tuned by CV, features scaled

---

## 9. Pipeline in sklearn
> 🟠 Tier 2 · _Tracker hint:_ Chain preprocessing + model; prevent data leakage; GridSearch over entire pipeline

### Definition
A `Pipeline` chains transformers and a final estimator so that **fit** on training data learns all steps from the training portion only; inside cross-validation each fold refits preprocessing on its own training part, preventing **leakage**. `ColumnTransformer` applies different preprocessing to numeric and categorical columns. Parameters of any step are tuned together with the `step__param` syntax. A single saved pipeline object also guarantees identical preprocessing in production.

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV

pre = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")), ("sc", StandardScaler())]), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)])
pipe = Pipeline([("pre", pre), ("clf", GradientBoostingClassifier())])
gs = GridSearchCV(pipe, {"clf__learning_rate": [0.05, 0.1], "clf__max_depth": [2, 3]}, cv=5, scoring="roc_auc")
gs.fit(X_train, y_train)
```

### Example
Leaky way: scale the full dataset, then cross-validate; each validation fold's mean and variance have influenced the scaler, giving optimistic scores (a small effect for scalers, but severe for target encoding or feature selection). Pipeline way: scaler refit inside each fold, honest scores.

### In the news
See news box. Scaling ML across 23 banks requires identical, versioned preprocessing at each site, which a packaged pipeline provides (general practice; implementation details of MuleHunter.AI are not public in the sources).

### Interview angle
> [!question] How it is asked
> "How do you prevent data leakage when doing cross-validation and tuning?"

> [!tip] Strong answer includes
> - Fit transformers on training folds only, using Pipeline
> - ColumnTransformer for mixed types
> - Tune pipeline parameters with `step__param`
> - Pickle the whole pipeline for deployment consistency

---

## 10. MLOps Basics
> 🟠 Tier 2 · _Tracker hint:_ Model versioning (MLflow), reproducibility, CI/CD for models, monitoring drift

### Definition
**MLOps** applies DevOps discipline to the ML lifecycle: build, deploy, monitor, retrain.

- **Versioning and tracking:** code (Git), data (DVC, lakehouse snapshots), models and experiments (MLflow: params, metrics, artefacts, model registry with stages).
- **Reproducibility:** fixed seeds, pinned environments/containers, logged data versions.
- **CI/CD for ML:** automated tests (data validation, unit tests, performance gates), automated training pipelines, staged rollout (shadow, canary, A/B).
- **Serving:** batch or real-time API, latency and cost budgets, feature store for consistent features.
- **Monitoring:** data drift (inputs change), concept drift (relationship changes), performance with delayed labels, data quality, fairness. Population Stability Index $PSI=\sum(a_i-e_i)\ln\frac{a_i}{e_i}$ (below 0.1 stable, 0.1 to 0.25 watch, above 0.25 significant shift: rule of thumb).
- **Retraining triggers:** schedule, drift alert, performance drop.

```python
import mlflow
with mlflow.start_run():
    mlflow.log_params({"max_depth": 4}); mlflow.log_metric("auc", 0.87)
    mlflow.sklearn.log_model(model, "model")
```

### Example
Expected distribution of a feature: 50%/50% across two bins; this month 60%/40%. PSI = (0.6-0.5)ln(0.6/0.5) + (0.4-0.5)ln(0.4/0.5) = 0.1(0.1823) + (-0.1)(-0.2231) = 0.0182+0.0223 = **0.0405**, below 0.1, so stable.

### In the news
See news box. With 78% of organisations using AI and tools like MuleHunter.AI rolling out to 23 banks, operating models safely at scale (monitoring, versioning, transparency) is now the main challenge. RBI's reluctance to disclose mule counts also shows governance trade-offs.

### Interview angle
> [!question] How it is asked
> "Your model was great at launch but is degrading. What do you do?" or "What is MLOps?"

> [!tip] Strong answer includes
> - Distinguish data drift from concept drift; monitor inputs and outcomes
> - Tools: MLflow tracking/registry, CI/CD gates, shadow or canary rollout
> - Retraining triggers and rollback plan
> - Ownership: who responds to alerts, and business KPI monitoring

---

## 11. ⭐ Advanced: Bayesian Optimization and Optuna
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Bayesian optimisation treats the validation score as an expensive black-box function. It keeps a **surrogate model** (Gaussian process or Tree-structured Parzen Estimator, TPE) of score versus hyperparameters and an **acquisition function** (Expected Improvement, UCB) that balances **exploration** (uncertain regions) and **exploitation** (promising regions) to choose the next trial. Optuna (default TPE sampler) adds **pruning** of unpromising trials, conditional search spaces and parallel studies.

```python
import optuna
from sklearn.model_selection import cross_val_score
def objective(trial):
    m = lgb.LGBMClassifier(num_leaves=trial.suggest_int("num_leaves", 15, 127),
                           learning_rate=trial.suggest_float("lr", 1e-3, 0.3, log=True),
                           n_estimators=300)
    return cross_val_score(m, X_train, y_train, cv=5, scoring="roc_auc").mean()
study = optuna.create_study(direction="maximize"); study.optimize(objective, n_trials=50)
```

### Example
Grid of 5 values for each of 4 hyperparameters = 5⁴ = 625 combinations (3,125 fits with 5-fold CV). A 50-trial Bayesian search uses 250 fits, about 8% of the cost, and typically lands near the best region.

### In the news
See news box. Cheaper compute lowers the cost of each trial, but smarter search still saves time and energy when models are retrained regularly.

### Interview angle
> [!question] How it is asked
> "Why is Bayesian optimisation more efficient than grid search?"

> [!tip] Strong answer includes
> - Surrogate model and acquisition function; learns from past trials
> - Exploration versus exploitation
> - Pruning poor trials early
> - Caveat: still validate the final model on an untouched test set

---

## 12. ⭐ Advanced: Nested Cross-Validation and Honest Model Selection
> ⭐ Advanced · _Added beyond the tracker_

### Definition
If you tune hyperparameters with CV and then report that same CV score, the estimate is **optimistically biased** (selection bias). **Nested CV** fixes this: an **inner loop** selects hyperparameters, an **outer loop** evaluates the whole selection procedure on data never used for tuning.

```python
inner = GridSearchCV(pipe, param_grid, cv=3, scoring="roc_auc")
outer_scores = cross_val_score(inner, X, y, cv=5, scoring="roc_auc")
print(outer_scores.mean(), outer_scores.std())
```

Cost: outer folds × inner folds × grid size fits. Use it to **compare algorithms** fairly on small datasets; for large data a simple train/validation/test split is enough. Also report variability (std across folds), compare against baselines, and use time-based splits for temporal data. For model choice also weigh latency, interpretability, maintenance and fairness, not only the score.

### Example
5 outer × 3 inner folds × 12 grid points = 5 × 3 × 12 = **180 fits** (plus refits). Typical result: plain tuned-CV AUC 0.86 versus nested-CV AUC 0.84, the 0.02 gap being the optimism from tuning on the same folds. (Illustrative.)

### In the news
See news box. With AI adoption near 78% of organisations, over-optimistic pilot numbers are a common cause of production disappointment; honest estimates protect credibility.

### Interview angle
> [!question] How it is asked
> "How do you choose between two models fairly, and how do you report the performance you expect in production?"

> [!tip] Strong answer includes
> - Selection bias when tuning and evaluating on the same folds
> - Nested CV or a locked test set
> - Report mean ± std and compare to a baseline
> - Include non-accuracy criteria: latency, cost, explainability, maintenance

---
## 🔗 Go deeper: expansion notes
- [[220 Responsible AI, Explainability & Model Governance|Responsible AI, Explainability & Model Governance]]
- [[218 Forecasting with ML & Foundation Models|Forecasting with ML & Foundation Models]]
