---
tags: [machine-learning, tier1]
area: Machine Learning
topic: "Regression Algorithms"
tier: Tier 1
roles: Operations / PM
status: complete
subtopics: 12
---
# Regression Algorithms

⬅ [[094 ML Fundamentals & Workflow]] · [[_Index - Machine Learning|Machine Learning]] · [[096 Classification Algorithms]] ➡

> **Area:** Machine Learning · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / PM

## Sub-topics in this note
1. [[#1. Linear Regression]]
2. [[#2. Ridge Regression (L2)]]
3. [[#3. Lasso Regression (L1)]]
4. [[#4. Elastic Net]]
5. [[#5. Polynomial Regression]]
6. [[#6. Decision Tree Regressor]]
7. [[#7. Random Forest Regressor]]
8. [[#8. Gradient Boosting Regressor]]
9. [[#9. Support Vector Regression (SVR)]]
10. [[#10. Evaluation: Regression]]
11. [[#11. ⭐ Advanced: Multicollinearity, VIF and Regression Diagnostics]]
12. [[#12. ⭐ Advanced: Demand Forecasting with Regression and Prediction Intervals]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Cheaper, wider ML adoption means regression-style forecasting is everywhere
> **Stanford AI Index 2025 (April 2025).** 78% of organisations reported using AI in 2024 (55% the year before), and the inference cost of GPT-3.5-level performance fell over 280-fold between Nov 2022 and Oct 2024. The report does not single out regression, but numeric prediction (demand, price, ETA) is among the commonest business uses. ([Business Wire summary of the Stanford HAI report](https://www.businesswire.com/news/home/20250407539812/en/Stanford-HAIs-2025-AI-Index-Reveals-Record-Growth-in-AI-Capabilities-Investment-and-Regulation))
>
> **RBI's MuleHunter.AI (Dec 2024, 23 banks by Dec 2025).** An RBI Innovation Hub ML tool analysing 19 behaviour patterns of mule accounts, piloted at two public sector banks; the sources do not state the algorithm used. Useful as an Indian example of ML replacing fixed rules. ([Business Standard](https://www.business-standard.com/finance/personal-finance/explained-rbi-has-a-new-ai-tool-mulehunter-ai-to-reduce-digital-frauds-124120900250_1.html), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Linear Regression
> 🔴 Tier 1 · _Tracker hint:_ y=β0+β1x; OLS; assumptions: linearity, normality, homoscedasticity, independence

### Definition
Linear regression models a continuous target as a weighted sum of features:

$$y=\beta_0+\beta_1x_1+\dots+\beta_px_p+\varepsilon$$

**OLS (ordinary least squares)** chooses $\beta$ to minimise the residual sum of squares: $\hat\beta=(X^TX)^{-1}X^Ty$. For one feature: $\beta_1=\dfrac{S_{xy}}{S_{xx}}$, $\beta_0=\bar y-\beta_1\bar x$.

**Assumptions (LINE + no multicollinearity):** Linearity of the relationship; Independence of errors; Normality of residuals (matters for inference, not for fitting); Equal variance (homoscedasticity). Violations: curved residual plot (non-linear), funnel shape (heteroscedasticity), autocorrelation (Durbin-Watson), high VIF (multicollinearity).

Coefficients are interpretable: $\beta_j$ is the change in $y$ per unit change in $x_j$ holding others constant.

```python
from sklearn.linear_model import LinearRegression
m = LinearRegression().fit(X_train, y_train)
```

### Example
x = 1,2,3,4,5 (ad spend), y = 2,4,5,4,5. Means: x̄=3, ȳ=4. $S_{xy}=(-2)(-2)+(-1)(0)+0(1)+1(0)+2(1)=6$; $S_{xx}=4+1+0+1+4=10$. So $\beta_1=0.6$, $\beta_0=4-0.6\times3=2.2$. Prediction at x=6: 2.2+3.6=**5.8**. Fitted values 2.8, 3.4, 4.0, 4.6, 5.2; SSE=2.4, SST=6, so $R^2=1-2.4/6=0.6$.

### In the news
See news box. As prediction becomes cheap, linear regression stays the interpretable baseline that regulators and business owners can audit.

### Interview angle
> [!question] How it is asked
> "Explain linear regression and its assumptions. How do you check them?"

> [!tip] Strong answer includes
> - The equation, OLS objective, coefficient meaning
> - The four assumptions and one diagnostic each (residual plots, Q-Q plot, Durbin-Watson, VIF)
> - Consequence of violation and a fix (transform, robust errors, drop correlated features)
> - R² versus adjusted R² and out-of-sample error

---

## 2. Ridge Regression (L2)
> 🔴 Tier 1 · _Tracker hint:_ Adds λΣβ² penalty; shrinks coefficients; handles multicollinearity; never zero

### Definition
Ridge minimises

$$\sum_i (y_i-\hat y_i)^2+\lambda\sum_j\beta_j^2,\qquad \hat\beta_{ridge}=(X^TX+\lambda I)^{-1}X^Ty$$

The penalty shrinks coefficients towards zero but **never exactly to zero**. Adding $\lambda I$ makes $X^TX$ invertible and stabilises estimates when features are highly correlated (multicollinearity), trading a little bias for much lower variance. $\lambda=0$ is OLS; large $\lambda$ gives a flat model. **Scale features first** (the penalty depends on magnitude) and do not penalise the intercept. Choose $\lambda$ by cross-validation.

```python
from sklearn.linear_model import RidgeCV
m = RidgeCV(alphas=[0.1, 1, 10, 100]).fit(X_train_scaled, y_train)
```

### Example
With orthonormal features, $\hat\beta_{ridge}=\hat\beta_{OLS}/(1+\lambda)$. If OLS gives 3 and $\lambda=0.5$: ridge = 3/1.5 = **2.0**. A weak coefficient 0.4 becomes 0.4/1.5 = 0.267, smaller but not zero.

### In the news
See news box. Wider ML use on correlated business features (price, discount, promo spend) makes regularised regression a safe default.

### Interview angle
> [!question] How it is asked
> "What happens when two features are highly correlated in linear regression, and how does ridge help?"

> [!tip] Strong answer includes
> - Unstable, huge-variance coefficients under multicollinearity
> - The penalty term and the shrinkage intuition
> - Never exactly zero, so no feature selection
> - Scaling and choosing $\lambda$ via CV

---

## 3. Lasso Regression (L1)
> 🔴 Tier 1 · _Tracker hint:_ Adds λΣ|β| penalty; can shrink coefficients to zero = feature selection

### Definition
Lasso minimises

$$\sum_i (y_i-\hat y_i)^2+\lambda\sum_j|\beta_j|$$

The L1 penalty has "corners" on the axes, so the optimum often lands exactly at $\beta_j=0$: **built-in feature selection** and sparse, interpretable models. With orthonormal features the solution is **soft-thresholding**: $\hat\beta_j=\text{sign}(\hat\beta^{OLS}_j)\max(|\hat\beta^{OLS}_j|-\lambda,0)$.

Weaknesses: among a group of correlated features it picks one arbitrarily; it can select at most $n$ features when $p>n$. Scale features; tune $\lambda$ by CV.

```python
from sklearn.linear_model import LassoCV
m = LassoCV(cv=5).fit(X_train_scaled, y_train)
selected = X.columns[m.coef_ != 0]
```

### Example
OLS coefficients 3.0 and 0.4, $\lambda=0.5$ (soft-threshold convention): first becomes 3.0-0.5=**2.5**, second becomes max(0.4-0.5,0)=**0**. The weak feature is dropped.

### In the news
See news box. Where banks and firms must explain models, sparse L1 models with few retained features are easier to defend than opaque ones.

### Interview angle
> [!question] How it is asked
> "Ridge versus Lasso: when would you use each?"

> [!tip] Strong answer includes
> - L1 gives sparsity and selection; L2 shrinks but keeps all
> - Lasso for many irrelevant features; ridge for many small correlated effects
> - Geometry or soft-threshold intuition
> - Standardise features and choose $\lambda$ by CV

---

## 4. Elastic Net
> 🔴 Tier 1 · _Tracker hint:_ Combines L1 + L2; best of both; use when features > observations

### Definition
Elastic Net blends both penalties:

$$\sum_i (y_i-\hat y_i)^2+\lambda\Big[\alpha\sum|\beta_j|+(1-\alpha)\sum\beta_j^2\Big]$$

(sklearn names: `alpha` is the overall strength and `l1_ratio` is the L1 share.) It keeps lasso's sparsity but the L2 part makes it **select or drop groups of correlated features together** rather than picking one at random, and it is stable when $p>n$ (lasso picks at most $n$). Two hyperparameters tuned by CV.

```python
from sklearn.linear_model import ElasticNetCV
m = ElasticNetCV(l1_ratio=[.1,.5,.9], cv=5).fit(X_train_scaled, y_train)
```

### Example
Gene-like or text data: 200 samples, 5,000 features, many correlated. Lasso keeps at most 200 and flips between correlated twins; Elastic Net with `l1_ratio=0.5` keeps correlated twins with shared weights and still zeroes most of the 5,000.

### In the news
See news box. Wide behavioural datasets (like the 19 mule-account patterns in RBI's work) are where penalised models are natural candidates, though the sources do not say Elastic Net was used.

### Interview angle
> [!question] How it is asked
> "When would you prefer Elastic Net over Lasso?"

> [!tip] Strong answer includes
> - Correlated features and $p>n$
> - Two parameters: strength and L1 ratio
> - Grouping effect versus lasso's arbitrary choice
> - Tune with CV on scaled data

---

## 5. Polynomial Regression
> 🔴 Tier 1 · _Tracker hint:_ Add polynomial features (X²,X³); captures non-linear relationships

### Definition
Polynomial regression adds powers of features and still fits a **linear model in the coefficients**:

$$y=\beta_0+\beta_1x+\beta_2x^2+\dots+\beta_dx^d$$

Use `PolynomialFeatures(degree=d)` then LinearRegression. Higher degree reduces bias but sharply increases variance, with wild behaviour at the edges (Runge phenomenon) and explosive extrapolation. Pick $d$ by cross-validation, scale features, and combine with ridge. Interaction terms ($x_1x_2$) come with it for multiple features. Splines or tree models are often safer for flexible curves.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge
m = make_pipeline(PolynomialFeatures(2), StandardScaler(), Ridge(1.0))
```

### Example
Fitted model: $\hat y=1+2x+0.5x^2$. At x=4: 1+8+8 = **17**. A straight line cannot capture a curve like a cost that rises faster at higher volume (diseconomies of scale).

### In the news
See news box. Cheap compute lets teams try polynomial and tree models quickly, but validation discipline decides which is trusted.

### Interview angle
> [!question] How it is asked
> "Your scatter plot is curved. What do you do before moving to a complex model?"

> [!tip] Strong answer includes
> - Add squared or interaction terms, still linear in parameters
> - Choose degree by CV and watch overfitting
> - Danger of extrapolation
> - Alternatives: log transform, splines, trees

---

## 6. Decision Tree Regressor
> 🔴 Tier 1 · _Tracker hint:_ Splits data on features; RMSE minimization; prone to overfitting; need pruning

### Definition
A regression tree recursively splits feature space into regions; each leaf predicts the **mean** of its training targets. At each node the split (feature, threshold) is chosen to maximise the reduction in squared error (variance):

$$\Delta = SSE_{parent}-\big(SSE_{left}+SSE_{right}\big)$$

Pros: handles non-linearity and interactions, no scaling, interpretable, works with mixed data. Cons: high variance, piecewise-constant predictions, cannot extrapolate beyond training range. Control with `max_depth`, `min_samples_leaf`, or cost-complexity pruning (`ccp_alpha`).

```python
from sklearn.tree import DecisionTreeRegressor
m = DecisionTreeRegressor(max_depth=5, min_samples_leaf=20).fit(X_train, y_train)
```

### Example
Sales = 10, 12, 30, 32. Before splitting: mean 21, SSE = 121+81+81+121 = 404. Split between 12 and 30: left mean 11 (SSE 1+1=2), right mean 31 (SSE 1+1=2). SSE after = 4, reduction = **400**.

### In the news
See news box. Tree-based models remain the workhorse for tabular business data; the single tree is mostly used as an explainer.

### Interview angle
> [!question] How it is asked
> "How does a decision tree decide where to split in regression, and why does it overfit?"

> [!tip] Strong answer includes
> - Variance reduction / SSE criterion, leaf = mean
> - Deep trees memorise noise
> - Pruning and limits (depth, leaf size)
> - Cannot extrapolate; piecewise-constant output

---

## 7. Random Forest Regressor
> 🔴 Tier 1 · _Tracker hint:_ Ensemble of decision trees; bagging; reduces variance; feature importance

### Definition
A **random forest** trains $B$ trees on **bootstrap samples** (bagging) and, at each split, considers only a random subset of features (`max_features`). Prediction = **average** of the trees. Variance of an average of $B$ trees with variance $\sigma^2$ and pairwise correlation $\rho$:

$$Var=\rho\sigma^2+\frac{1-\rho}{B}\sigma^2$$

More trees shrink the second term; random feature selection reduces $\rho$. Out-of-bag (OOB) samples give a free validation estimate. Provides feature importance (impurity-based, or better permutation importance). Little tuning needed; weaker at extrapolation and less interpretable than one tree.

```python
from sklearn.ensemble import RandomForestRegressor
m = RandomForestRegressor(n_estimators=300, oob_score=True, n_jobs=-1).fit(X_train, y_train)
```

### Example
σ²=100, ρ=0.3, B=100: variance = 30 + 0.7×100/100 = **30.7**, versus 100 for a single tree. Raising B to 1,000 gives 30.07: gains flatten because of the correlation floor.

### In the news
See news box. Random forests are a common first model in business ML because they perform well with little tuning.

### Interview angle
> [!question] How it is asked
> "Why does a random forest generalise better than a single decision tree?"

> [!tip] Strong answer includes
> - Bagging plus random feature subsets decorrelate trees
> - Averaging reduces variance, bias roughly unchanged
> - OOB error and feature importance
> - Limits: cannot extrapolate, large and slow to explain

---

## 8. Gradient Boosting Regressor
> 🔴 Tier 1 · _Tracker hint:_ Sequential trees; each corrects errors of previous; XGBoost, LightGBM, CatBoost

### Definition
**Gradient boosting** builds shallow trees sequentially; each new tree fits the **negative gradient of the loss** (for squared error, the residuals) of the current ensemble:

$$F_m(x)=F_{m-1}(x)+\nu\,h_m(x)$$

with learning rate $\nu$. It reduces **bias** (and with subsampling, variance). Key hyperparameters: `n_estimators`, `learning_rate`, `max_depth` (3–8), `subsample`, regularisation; lower learning rate plus more trees generalises better; use early stopping. XGBoost adds second-order gradients and regularisation; LightGBM is histogram-based and leaf-wise (fast); CatBoost handles categoricals natively. Often best on tabular data, but easier to overfit than random forest.

```python
import xgboost as xgb
m = xgb.XGBRegressor(n_estimators=500, learning_rate=0.05, max_depth=4, subsample=0.8)
m.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
```

### Example
Actual 100; $F_0$ = mean = 80; residual 20. Tree 1 predicts 20; with $\nu=0.1$: $F_1=80+0.1\times20=82$, new residual 18. Tree 2 predicts about 18: $F_2=82+1.8=83.8$. Slowly approaching 100 over many rounds.

### In the news
See news box. Boosted trees (XGBoost, LightGBM) remain the usual choice for tabular business problems such as demand and ETA prediction.

### Interview angle
> [!question] How it is asked
> "Random forest versus gradient boosting: difference and when to use each?"

> [!tip] Strong answer includes
> - Parallel bagging (variance) versus sequential boosting (bias)
> - Learning rate versus number of trees trade-off
> - Early stopping for overfit control
> - Name XGBoost, LightGBM, CatBoost strengths

---

## 9. Support Vector Regression (SVR)
> 🔴 Tier 1 · _Tracker hint:_ Fits hyperplane within ε-tube; kernel trick for non-linearity

### Definition
SVR fits a function so that most points lie within an **ε-tube** around it; errors smaller than $\varepsilon$ cost nothing. Loss is the **ε-insensitive loss**:

$$L_\varepsilon=\max(0,\,|y-\hat y|-\varepsilon)$$

Objective: minimise $\tfrac12\|w\|^2+C\sum(\xi_i+\xi_i^*)$ where slack $\xi$ covers points outside the tube. $C$ is the penalty for violations (large $C$ = less tolerance, more overfit); $\varepsilon$ is tube width; the **kernel** (RBF, polynomial) lets it fit curves without explicit features, with $\gamma$ controlling RBF reach. Only **support vectors** (points on or outside the tube) define the model. Needs feature scaling; slow beyond ~50k rows.

```python
from sklearn.svm import SVR
m = make_pipeline(StandardScaler(), SVR(kernel="rbf", C=10, epsilon=0.1))
```

### Example
ε = 5. Point with error 3: loss 0. Point with error 8: loss 8-5 = **3**. Compare squared loss, which would charge 9 and 64.

### In the news
See news box. SVR is now less common in industry than boosted trees, but is still asked in interviews as a kernel-methods example.

### Interview angle
> [!question] How it is asked
> "What is the ε-tube in SVR and what do C and ε control?"

> [!tip] Strong answer includes
> - Insensitive loss and support vectors
> - Role of C, ε, γ and the kernel trick
> - Scale features first
> - Limits: scales poorly with data, less interpretable

---

## 10. Evaluation: Regression
> 🔴 Tier 1 · _Tracker hint:_ RMSE = √MSE (penalizes large errors); MAE (robust to outliers); R² (explanatory power)

### Definition
| Metric | Formula | Notes |
|---|---|---|
| MAE | $\frac1n\sum\lvert y-\hat y\rvert$ | Same units, robust to outliers, easy to explain |
| MSE | $\frac1n\sum(y-\hat y)^2$ | Squared units; punishes large errors |
| RMSE | $\sqrt{MSE}$ | Same units, outlier-sensitive |
| MAPE | $\frac{100}{n}\sum\lvert\frac{y-\hat y}{y}\rvert$ (in percent) | Breaks when $y$ near 0; biased towards under-forecast |
| R² | $1-\frac{SS_{res}}{SS_{tot}}$ | Share of variance explained; can be negative on test data |
| Adj. R² | $1-(1-R^2)\frac{n-1}{n-p-1}$ | Penalises useless features |

Always compare with a **naive baseline** (last value, mean). For skewed or multiplicative targets consider RMSLE. Always evaluate on held-out data, and look at residual plots.

### Example
Actual 100, 120, 80, 140; forecast 110, 115, 90, 100; errors 10, -5, 10, -40. MAE = 65/4 = **16.25**; MSE = 1825/4 = 456.25; RMSE = **21.36**. Mean actual = 110, SS_tot = 100+100+900+900 = 2000, so $R^2=1-1825/2000=0.0875$: the one big miss ruins explanatory power even though three of four are close.

### In the news
See news box. As adoption grows, firms need a plain business translation of error: "average miss is 16 units per SKU" (MAE) is easier to act on than R².

### Interview angle
> [!question] How it is asked
> "RMSE or MAE: which would you report to the business?"

> [!tip] Strong answer includes
> - Link to the cost of errors (large misses costly means RMSE)
> - Outlier robustness of MAE
> - R² limits and adjusted R²
> - Benchmark against a naive forecast

---

## 11. ⭐ Advanced: Multicollinearity, VIF and Regression Diagnostics
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Multicollinearity** means predictors are strongly correlated, giving unstable, hard-to-interpret coefficients (prediction can still be fine). Detect with the **variance inflation factor**:

$$VIF_j=\frac{1}{1-R_j^2}$$

where $R_j^2$ comes from regressing feature $j$ on all the others. Rule of thumb: VIF above 5 to 10 is a concern. Fixes: drop or combine features, PCA, ridge. Other diagnostics: residual vs fitted plot (non-linearity, funnel), Q-Q plot (normality), Cook's distance (influential points), Durbin-Watson (autocorrelation, essential for time-series regressions).

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
```

### Example
If regressing "discount %" on the other features gives $R^2=0.90$, then VIF = 1/(1-0.90) = **10**, so the coefficient's variance is inflated 10x (standard error about 3.2x). Price and discount move together, so their separate effects are not identifiable.

### In the news
Not a dated news item; as 78% of firms use AI (see news box), explaining coefficients to stakeholders makes these diagnostics a practical, regulator-friendly skill.

### Interview angle
> [!question] How it is asked
> "A regression shows that increasing price increases sales. Do you trust it?"

> [!tip] Strong answer includes
> - Suspects collinearity, omitted variables or confounding (promotions, season)
> - Checks VIF and residuals
> - Distinguishes prediction from causal interpretation
> - Suggests a controlled test or including control variables

---

## 12. ⭐ Advanced: Demand Forecasting with Regression and Prediction Intervals
> ⭐ Advanced · _Added beyond the tracker_

### Definition
For supply chains, a point forecast is not enough: safety stock needs the **uncertainty**. Approaches:

- **Regression with calendar features:** lags, rolling means, promotion, price, festival and weather variables; gradient boosting across many SKUs ("global model").
- **Quantile regression:** minimise pinball loss to predict the 50th, 90th percentile directly (`GradientBoostingRegressor(loss="quantile", alpha=0.9)`).
- **Safety stock link:** $SS=z\cdot\sigma_{error}\cdot\sqrt{L}$ using the forecast error standard deviation.
- **Validation:** rolling-origin (walk-forward) evaluation, not random splits; track bias (mean error) as well as MAE.
- **Hierarchy:** forecast at SKU-store level and reconcile to totals.

### Example
Weekly forecast error SD = 40 units, lead time 4 weeks, service level 95% (z = 1.65): SS = 1.65 × 40 × √4 = 1.65 × 40 × 2 = **132 units**. If a better model cuts error SD to 30, SS = 99 units, a 25% cut in safety stock.

### In the news
See news box. Cheaper ML (280-fold lower inference cost) makes SKU-level forecasting with uncertainty bands feasible even for mid-size Indian retailers.

### Interview angle
> [!question] How it is asked
> "How would you improve forecast accuracy for a retailer, and how does it affect inventory?"

> [!tip] Strong answer includes
> - Better features and global gradient-boosting model with a baseline comparison
> - Walk-forward validation and bias tracking
> - Quantile or error-SD driven safety stock
> - Quantified inventory and service impact

---
## 🔗 Go deeper: expansion notes
- [[218 Forecasting with ML & Foundation Models|Forecasting with ML & Foundation Models]]
