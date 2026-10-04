---
tags: [statistics, tier1]
area: Statistics
topic: "Regression Analysis"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 12
---
# Regression Analysis

⬅ [[089 Hypothesis Testing]] · [[_Index - Statistics|Statistics]] · [[091 Statistical Quality Control (SQC)]] ➡

> **Area:** Statistics · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Simple Linear Regression]]
2. [[#2. Coefficient Interpretation]]
3. [[#3. R² (Coefficient of Determination)]]
4. [[#4. Adjusted R²]]
5. [[#5. Residual Analysis]]
6. [[#6. Multiple Linear Regression]]
7. [[#7. Multicollinearity]]
8. [[#8. Heteroscedasticity]]
9. [[#9. Logistic Regression]]
10. [[#10. Regression in Business]]
11. [[#11. ⭐ Advanced: Dummy Variables, Interactions and Log Transformations]]
12. [[#12. ⭐ Advanced: Overfitting, Validation and Regularisation (Ridge and Lasso)]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): India re-bases its inflation index, and every fitted model built on the old series now has a structural break
> **New CPI series (launched Feb 2026).** MoSPI moved the Consumer Price Index base from 2011-12 to **2024**, using the 2023-24 Household Consumption Expenditure Survey. The weight of *Food and Beverages* falls from **45.86% to 36.75%**, housing/utilities/fuel rises from **10.07% to 17.67%**; the basket has **358 weighted items** under the COICOP 2018 classification, with price collection across **434 towns** plus weekly data from **12 e-commerce platforms**. The first reading under the new series (Jan 2026) was **2.75%**, versus **1.3%** for Dec 2025 on the old series, which reflects the methodology change and not only a price move. ([Business Standard](https://www.business-standard.com/amp/economy/news/economy-inflation-weight-food-beverages-cut-new-cpi-series-2024-base-126012901838_1.html), [Upstox](https://upstox.com/learning-center/personal-finance/what-changed-in-indias-new-cpi-series-and-how-it-impacts-the-economy-and-inflation/article-1518/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Simple Linear Regression
> 🔴 Tier 1 · _Tracker hint:_ Y = β0 + β1X + ε; β1=slope=Cov(X,Y)/Var(X); β0=intercept; OLS method

### Definition
Simple linear regression models one response $Y$ as a straight-line function of one predictor $X$ plus random error:

$$Y_i = \beta_0 + \beta_1 X_i + \varepsilon_i$$

**Ordinary Least Squares (OLS)** chooses $\hat\beta_0,\hat\beta_1$ to minimise the sum of squared residuals $\sum (Y_i-\hat Y_i)^2$. The closed-form solution is:

$$\hat\beta_1 = \frac{\sum (X_i-\bar X)(Y_i-\bar Y)}{\sum (X_i-\bar X)^2} = \frac{Cov(X,Y)}{Var(X)} = r\,\frac{s_Y}{s_X}, \qquad \hat\beta_0 = \bar Y - \hat\beta_1 \bar X$$

The fitted line always passes through $(\bar X,\bar Y)$. The classical (Gauss-Markov) assumptions are: linearity, errors with mean zero, constant variance (homoscedasticity), independent errors, and no perfect collinearity (multiple regression). Under these, OLS is the Best Linear Unbiased Estimator (BLUE). Normality of errors is needed only for exact small-sample t and F tests.

Regression shows **association**; causation needs design (experiment) or strong assumptions.

### Example
Ad spend $X$ (₹ lakh): 1, 2, 3, 4, 5. Sales $Y$ (₹ crore): 3, 5, 4, 6, 7.
$\bar X=3,\ \bar Y=5$. $S_{xy}=(-2)(-2)+(-1)(0)+(0)(-1)+(1)(1)+(2)(2)=9$; $S_{xx}=4+1+0+1+4=10$.
$\hat\beta_1=9/10=0.9$; $\hat\beta_0=5-0.9\times3=2.3$. Fitted line: $\hat Y=2.3+0.9X$. Spending ₹6 lakh predicts $2.3+5.4=7.7$ crore (extrapolation beyond the data, so treat with caution).

### In the news
See news box. Any regression fitted on the old CPI series (for example inflation on repo rate) must be re-estimated or the series spliced, because the new base changes weights and levels: a textbook structural break.

### Interview angle
> [!question] How it is asked
> "Explain simple linear regression to a non-technical manager." or "How is the slope calculated and what does the line represent?"

> [!tip] Strong answer includes
> - Plain-language picture: the best-fit line that minimises squared vertical gaps
> - Formula $\beta_1=Cov(X,Y)/Var(X)$ and that the line passes through the means
> - The OLS assumptions, and that it is BLUE under them
> - Correlation is not causation, and do not extrapolate far outside the data range

---

## 2. Coefficient Interpretation
> 🔴 Tier 1 · _Tracker hint:_ β1 = one unit increase in X → β1 units change in Y, holding others constant

### Definition
Each coefficient is a **marginal effect**: the expected change in $Y$ for a one-unit increase in that predictor, **holding the other predictors constant** (ceteris paribus). The intercept $\beta_0$ is the predicted $Y$ when all $X=0$ (often not meaningful in business data).

Functional forms change the reading:

| Model | Interpretation of $\beta_1$ |
|---|---|
| Level-level: $Y=\beta_0+\beta_1X$ | 1 unit of X changes Y by $\beta_1$ units |
| Log-log: $\ln Y=\beta_0+\beta_1\ln X$ | 1% rise in X changes Y by about $\beta_1$% (an **elasticity**) |
| Log-level: $\ln Y=\beta_0+\beta_1X$ | 1 unit of X changes Y by about $100\beta_1$% |
| Level-log: $Y=\beta_0+\beta_1\ln X$ | 1% rise in X changes Y by about $\beta_1/100$ units |
| Dummy variable | Average difference in Y between that category and the base category |

Significance: test $H_0:\beta_j=0$ with $t=\hat\beta_j/SE(\hat\beta_j)$; the **p-value** and the **95% confidence interval** $\hat\beta\pm t_{\alpha/2}\,SE$ tell you whether the effect is distinguishable from zero. Statistical significance is not practical significance: look at effect size.

### Example
Fitted: $\text{Sales (units)} = 500 - 8\,\text{Price (₹)} + 40\,\text{Promo}$ (Promo = 1 if on promotion). Holding promo status fixed, each ₹1 price rise lowers sales by 8 units. A promotion week sells 40 more units than a non-promotion week at the same price. If the 95% CI for the price coefficient is $-8\pm3$, i.e. $[-11,-5]$, price is clearly significant.

### In the news
See news box. With the new CPI weights, the coefficient on "food inflation" in a headline-inflation regression will differ: food now carries 36.75% weight, not 45.86%, so the same food price shock moves headline CPI less.

### Interview angle
> [!question] How it is asked
> "Your model says β for price is -8. What does that mean?" or "The coefficient is positive but the p-value is 0.3; what do you tell the client?"

> [!tip] Strong answer includes
> - "Per unit change, holding other variables constant" in the units of the data
> - The correct reading for log and dummy variables
> - Use of p-value and confidence interval, plus practical size of the effect
> - Caveat: association not causation; omitted variables bias the coefficient

---

## 3. R² (Coefficient of Determination)
> 🔴 Tier 1 · _Tracker hint:_ Proportion of variance in Y explained by X(s); R²=0 to 1; higher is better

### Definition
$R^2$ is the share of total variation in $Y$ explained by the model:

$$R^2=\frac{SSR}{SST}=1-\frac{SSE}{SST},\qquad SST=\sum(Y_i-\bar Y)^2 = SSR+SSE$$

where $SSR=\sum(\hat Y_i-\bar Y)^2$ (explained) and $SSE=\sum(Y_i-\hat Y_i)^2$ (unexplained). In simple regression $R^2=r^2$ (the squared correlation).

Cautions: $R^2$ **never decreases** when a variable is added, so it rewards overfitting; a high $R^2$ does not prove the model is correct (trending series give spurious high $R^2$); a low $R^2$ can still be useful when the signal is real but noisy (e.g. human behaviour). It says nothing about bias, and cannot be compared across models with different dependent variables (e.g. $Y$ vs $\ln Y$).

### Example
Using the earlier data ($\hat Y=2.3+0.9X$): fitted values 3.2, 4.1, 5.0, 5.9, 6.8; residuals -0.2, 0.9, -1.0, 0.1, 0.2. $SSE=0.04+0.81+1.00+0.01+0.04=1.90$; $SST=4+0+1+1+4=10$. $R^2=1-1.90/10=0.81$: ad spend explains 81% of the variation in sales; $r=\sqrt{0.81}=0.90$. Check: $SSR=0.9^2\times10=8.1$, and $8.1/10=0.81$.

### In the news
See news box. A high $R^2$ in a model of inflation fitted on 2011-12-base data does not guarantee a good fit once the basket changes: fit must be re-checked out of sample on the new series.

### Interview angle
> [!question] How it is asked
> "Your model has R² of 0.95. Is it a good model?" or "What does R² of 0.3 mean, and is that bad?"

> [!tip] Strong answer includes
> - Definition as explained variance with the SSR/SST formula
> - "Good" depends on context and domain (0.3 may be fine in consumer behaviour)
> - R² always rises with more variables, so use adjusted R² and out-of-sample error
> - High R² can hide spurious regression, overfitting or non-random residuals

---

## 4. Adjusted R²
> 🔴 Tier 1 · _Tracker hint:_ Penalizes for adding non-significant variables; always use in multiple regression

### Definition
Adjusted $R^2$ corrects $R^2$ for the number of predictors $k$ and sample size $n$:

$$\bar R^2 = 1-\frac{SSE/(n-k-1)}{SST/(n-1)} = 1-(1-R^2)\frac{n-1}{n-k-1}$$

Adding a variable always raises $R^2$, but $\bar R^2$ rises **only if the variable's t-statistic exceeds 1 in absolute value** (i.e. it reduces the error mean square). It can fall, and can even be negative for poor models. Use it to compare nested or non-nested models with the same $Y$ and different numbers of predictors. Better selection tools: AIC, BIC, cross-validated RMSE.

### Example
n = 30. Model A has k = 2, $R^2=0.80$: $\bar R^2=1-0.20\times29/27=0.785$. Model B adds 3 weak variables (k = 5) and $R^2$ edges up to 0.81: $\bar R^2=1-0.19\times29/24=1-0.2296=0.770$. $R^2$ rose, but adjusted $R^2$ fell from 0.785 to 0.770, so the extra variables are not worth keeping.

### In the news
See news box. The new CPI series carries more components (12 COICOP divisions, 358 items); an analyst adding many sub-indices as predictors must watch adjusted $R^2$ and not just $R^2$ to avoid overfitting a short post-2024 history.

### Interview angle
> [!question] How it is asked
> "Why not just use R² to choose between models?" or "R² went up when we added a variable. Should we keep it?"

> [!tip] Strong answer includes
> - Formula with $n$ and $k$ and why it penalises complexity
> - Rises only if $|t|>1$ for the added variable
> - Prefer parsimonious models; mention AIC/BIC or hold-out validation
> - A worked mini-example showing R² up and adjusted R² down

---

## 5. Residual Analysis
> 🔴 Tier 1 · _Tracker hint:_ Residuals should be: normally distributed, mean=0, constant variance, independent

### Definition
Residuals $e_i=Y_i-\hat Y_i$ are the model's diagnostic window. Check:

| Assumption | Diagnostic plot / test | Violation looks like |
|---|---|---|
| Linearity, mean zero | Residuals vs fitted | Curved pattern, U-shape |
| Constant variance | Residuals vs fitted; Breusch-Pagan | Funnel / fan shape |
| Independence | Residuals vs time; Durbin-Watson (≈2 is good) | Runs of same sign, autocorrelation |
| Normality | Q-Q plot; Shapiro-Wilk | Points leave the diagonal, heavy tails |
| Influence / outliers | Standardised residuals (>3), Cook's distance, leverage | Single points that drive the line |

With OLS and an intercept, residuals sum to zero by construction, so "mean = 0" is automatic; the real question is whether they have **no structure**. Fixes: add a missing variable or a quadratic term, transform ($\ln Y$), use robust standard errors, add lags (autocorrelation), or investigate outliers before removing them.

### Example
Weekly sales regressed on temperature gives a residual plot with a clear U-shape: under-prediction at low and high temperatures. Adding $\text{Temp}^2$ removes the pattern and lifts adjusted $R^2$ from 0.55 to 0.72 (illustrative). For time series, Durbin-Watson of 0.8 flags positive autocorrelation: standard errors are understated and t-values inflated.

### In the news
See news box. After a base-year revision, residuals of old models on new data tend to show a level shift: a run of same-signed errors is the practical signal that the relationship has changed.

### Interview angle
> [!question] How it is asked
> "You have fitted a regression. How do you check that it is valid?"

> [!tip] Strong answer includes
> - List of assumptions (linearity, homoscedasticity, independence, normality) with a plot or test for each
> - Specific remedies (transform, add term, robust SE, lags)
> - Outliers and influential points: investigate, do not just delete
> - Distinguish prediction accuracy from valid inference

---

## 6. Multiple Linear Regression
> 🔴 Tier 1 · _Tracker hint:_ Y = β0+β1X1+β2X2+...+βkXk; F-test for overall model significance

### Definition
$$Y=\beta_0+\beta_1X_1+\beta_2X_2+\dots+\beta_kX_k+\varepsilon$$

In matrix form $\hat{\boldsymbol\beta}=(X^\top X)^{-1}X^\top Y$. Each $\beta_j$ is a partial effect holding the others constant.

**Overall F-test** ($H_0:\beta_1=\dots=\beta_k=0$):

$$F=\frac{SSR/k}{SSE/(n-k-1)}=\frac{R^2/k}{(1-R^2)/(n-k-1)}\sim F_{k,\,n-k-1}$$

A small p-value means at least one predictor matters. Then use **t-tests** for individual coefficients. Important: the overall F can be significant while individual t-tests are not (symptom of multicollinearity). Include categorical predictors as **dummy variables** (k-1 dummies for k categories to avoid the dummy trap), and interaction terms $X_1X_2$ when the effect of one variable depends on another.

```python
import statsmodels.formula.api as smf
m = smf.ols("sales ~ price + ad_spend + C(region)", data=df).fit()
print(m.summary())   # coefficients, t, p, R2, adj R2, F-stat
```

### Example
Sales on price, ad spend and number of outlets with $n=40$, $k=3$, $R^2=0.85$:
$F=\dfrac{0.85/3}{0.15/36}=\dfrac{0.2833}{0.004167}=68.0$. The 5% critical value of $F_{3,36}$ is about 2.87, so the model is overwhelmingly significant.

### In the news
See news box. A headline-CPI model with several component inflations (food, fuel, core) as predictors is a multiple regression; the new weights alter the dependent variable and must be reflected in the specification.

### Interview angle
> [!question] How it is asked
> "How do you read a regression output table?" Often in a case with an Excel or Python summary printed.

> [!tip] Strong answer includes
> - Read order: F-test and adjusted R² first, then each coefficient's sign, size and p-value
> - Partial-effect interpretation (holding others constant)
> - Dummy variables for categories; interactions where effects depend on each other
> - Flag multicollinearity and check residual diagnostics before trusting it

---

## 7. Multicollinearity
> 🔴 Tier 1 · _Tracker hint:_ High correlation between predictors; inflates SE; detect with VIF>10

### Definition
Multicollinearity means predictors are strongly correlated with each other, so the model cannot separate their individual effects. Coefficients stay unbiased but their **standard errors inflate**, giving unstable estimates, wrong signs, and insignificant t-values despite a high $R^2$ and significant F.

**Variance Inflation Factor:** regress predictor $X_j$ on the other predictors; with that regression's $R_j^2$,

$$VIF_j=\frac{1}{1-R_j^2},\qquad Tolerance=1-R_j^2$$

Rules of thumb: VIF above 5 is a concern and above 10 is serious. Also check the correlation matrix and the condition number.

**Remedies:** drop or combine redundant variables (e.g. average, index), collect more data, centre variables (for polynomial/interaction terms), use **ridge regression** or PCA. If the goal is only prediction, multicollinearity is less harmful; for explaining each driver's effect it is a major problem. "Perfect" collinearity (including the dummy trap) makes OLS impossible.

### Example
Predicting store revenue with both "floor area in sq ft" and "floor area in sq m": perfect collinearity. A subtler case: "ad spend" and "number of promotions" correlated at 0.95: $R_j^2\approx0.90$, so $VIF=1/(1-0.90)=10$ and the standard errors are inflated by $\sqrt{10}\approx3.2$ times.

### In the news
See news box. Food, fuel and core inflation components are correlated, so regressing headline CPI on all of them invites high VIFs; the re-weighted basket changes those correlations.

### Interview angle
> [!question] How it is asked
> "Two of your variables are highly correlated. What happens to the model and what do you do?"

> [!tip] Strong answer includes
> - Effect: unbiased but high-variance estimates; unstable signs
> - Detection: VIF (and its formula), correlation matrix, high R² with insignificant t's
> - Remedies: drop/merge variables, ridge/PCA, more data
> - Distinguish prediction goal (mild) from interpretation goal (serious)

---

## 8. Heteroscedasticity
> 🔴 Tier 1 · _Tracker hint:_ Non-constant residual variance; Breusch-Pagan test; use WLS or transform

### Definition
Heteroscedasticity means $Var(\varepsilon_i)$ is not constant, typically growing with a predictor or with the level of $Y$ (e.g. spending variance rises with income). OLS coefficients remain unbiased, but **standard errors are wrong** (usually understated), so t-tests, p-values and confidence intervals mislead; OLS is also no longer the most efficient estimator.

**Detect:** funnel shape in residuals vs fitted; **Breusch-Pagan** (regress squared residuals on predictors; $LM=nR^2_{aux}\sim\chi^2_k$), White test, Goldfeld-Quandt. A p-value below 0.05 rejects constant variance.

**Fix:** (1) heteroscedasticity-robust (White/HC) standard errors, the easiest; (2) **Weighted Least Squares** with weights $1/\sigma_i^2$; (3) transform the dependent variable (log or square root); (4) re-specify the model (missing variable or wrong functional form).

```python
from statsmodels.stats.diagnostic import het_breuschpagan
lm, lm_p, f, f_p = het_breuschpagan(m.resid, m.model.exog)
m_rob = m.get_robustcov_results(cov_type="HC3")
```

### Example
Regressing monthly spend on income for 200 households: low-income households cluster tightly around the line, high-income households scatter widely. Breusch-Pagan gives $p=0.001$. Re-fitting with $\ln(\text{spend})$ or HC3 standard errors restores valid inference; the point estimates barely change but the standard error of income may be 30% larger (illustrative).

### In the news
See news box. Price indices pooled across many items and cities (434 towns in the new CPI) combine very different variances; regressions on such cross-sectional price data are classic candidates for robust standard errors.

### Interview angle
> [!question] How it is asked
> "What is heteroscedasticity, why does it matter and how do you handle it?"

> [!tip] Strong answer includes
> - Definition and the consequence: unbiased coefficients but invalid SEs
> - Detection: residual plot plus Breusch-Pagan or White test
> - Remedies in order of ease: robust SE, WLS, log transform
> - Business example (variance rises with firm size or income)

---

## 9. Logistic Regression
> 🔴 Tier 1 · _Tracker hint:_ Binary outcome; log-odds = β0+β1X; interpret as odds ratio; sigmoid function

### Definition
When $Y\in\{0,1\}$ (churn, default, purchase), OLS can predict outside [0,1] and violates variance assumptions. **Logistic regression** models the probability through the log-odds (logit):

$$\ln\frac{p}{1-p}=\beta_0+\beta_1X_1+\dots+\beta_kX_k \quad\Longleftrightarrow\quad p=\frac{1}{1+e^{-(\beta_0+\beta_1X_1+\dots)}}$$

The right-hand form is the **sigmoid** (S-curve). Estimation is by **maximum likelihood**, not OLS. Interpretation: $e^{\beta_j}$ is the **odds ratio**: the multiplicative change in the odds for a one-unit rise in $X_j$ (odds ratio above 1 raises the odds). Classify with a threshold (default 0.5, tuned to costs). Evaluate with the confusion matrix, precision/recall, ROC-AUC, KS statistic (credit scoring), not $R^2$ (pseudo-$R^2$ exists). Multi-class: multinomial/softmax; ordered outcomes: ordinal logit.

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression().fit(X_train, y_train)
p = clf.predict_proba(X_test)[:, 1]
```

### Example
Loan default: $\text{logit}=-2+0.5X$, with $X$ = number of missed payments. At $X=4$: logit = 0, so $p=0.50$. At $X=6$: logit = 1, so $p=1/(1+e^{-1})=0.731$. Odds ratio per extra missed payment $=e^{0.5}=1.65$: the odds of default rise by about 65%.

### In the news
See news box. Not directly applicable: the new CPI series is a continuous measure. The logistic link appears when a bank models "inflation above RBI's 4% target (yes/no)" as a binary outcome.

### Interview angle
> [!question] How it is asked
> "How would you predict customer churn?" or "Interpret a coefficient of 0.7 in a logistic model."

> [!tip] Strong answer includes
> - Why not OLS for a binary outcome; logit link and sigmoid
> - Odds ratio interpretation ($e^{0.7}\approx2.01$, i.e. odds roughly double)
> - Metrics: confusion matrix, ROC-AUC, precision-recall, threshold choice based on costs
> - Class imbalance handling and avoiding leakage

---

## 10. Regression in Business
> 🔴 Tier 1 · _Tracker hint:_ Demand forecasting, price elasticity, cost driver analysis, sales forecasting

### Definition
Common applications:
- **Demand and sales forecasting:** regress sales on price, promotion, seasonality dummies, trend, weather, festivals.
- **Price elasticity:** log-log model $\ln Q=\alpha+\beta\ln P$; $\beta$ is the elasticity (e.g. -1.8 means a 1% price rise cuts demand about 1.8%, so demand is elastic and a price rise cuts revenue).
- **Cost driver analysis:** regress total cost on activity drivers (machine hours, orders) to split fixed cost (intercept) and variable cost (slope).
- **Marketing mix modelling:** contribution of channels to sales, with adstock effects.
- **Operations:** lead-time prediction, defect rate vs process settings, productivity vs training.
- **Finance/HR:** credit scoring (logistic), attrition, salary benchmarking.

Workflow: define the question, clean data, explore, specify, estimate, diagnose, validate out-of-sample, and communicate effects in business units. Always report prediction intervals, not just point forecasts.

### Example
Warehouse cost vs lines picked: $\text{Cost}=₹2{,}00{,}000+₹12\times\text{Lines}$. Fixed cost is ₹2 lakh per month; each extra line costs ₹12. At 50,000 lines: $2{,}00{,}000+12\times50{,}000=₹8{,}00{,}000$. Price elasticity: with $\beta=-1.8$, a 5% price cut raises volume about 9%.

### In the news
See news box. Businesses indexing contracts to CPI, or forecasting demand from inflation, now need to model on the new 2024-base series; Jan 2026 reads 2.75% on the new series against 1.3% on the old for Dec 2025, a methodological gap forecasters must not read as a spike.

### Interview angle
> [!question] How it is asked
> "How would you estimate the effect of a price change on demand?" or "A client wants to forecast sales next quarter. What model do you build?"

> [!tip] Strong answer includes
> - Clear framing: dependent variable, predictors, expected signs
> - Log-log for elasticity and the business reading of the coefficient
> - Diagnostics, out-of-sample validation and prediction intervals
> - Caveat on causality (price set endogenously) and the data you would request

---

## 11. ⭐ Advanced: Dummy Variables, Interactions and Log Transformations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Real data are not neat straight lines, so analysts extend OLS while keeping it linear in the parameters.
- **Dummy variables** encode categories; use $k-1$ dummies for $k$ levels. Coefficients are differences from the base level.
- **Interaction terms** let the slope depend on another variable: $Y=\beta_0+\beta_1X+\beta_2D+\beta_3(X\cdot D)$. Here $\beta_3$ is the difference in slope between groups.
- **Polynomial terms** ($X^2$) capture curvature, such as diminishing returns to ad spend.
- **Log transforms** tame skew and give elasticities.
- **Endogeneity**: if $X$ is correlated with the error (reverse causality, omitted variable), OLS is biased. Remedies include instrumental variables, fixed effects, or experiments.
- **Time-series cautions:** regressions of trending series produce **spurious regression** (high $R^2$, tiny Durbin-Watson); difference the data or test for cointegration.

### Example
Sales $=100+5\,\text{Ads}+30\,\text{Metro}+2\,(\text{Ads}\times\text{Metro})$. In non-metro towns each extra ₹1 lakh of ads adds 5 units; in metro towns it adds $5+2=7$ units. Metro towns also start 30 units higher at zero ads.

### In the news
See news box. A regime change like a CPI re-base is usually handled by adding a **structural-break dummy** (0 before, 1 after) and its interaction with the key regressors, or by splicing the series.

### Interview angle
> [!question] How it is asked
> "Does the effect of price differ between metro and rural customers? How would you test it?"

> [!tip] Strong answer includes
> - Interaction term, and the test on its coefficient
> - Dummy-variable trap and base category
> - Endogeneity caveat when prices respond to demand
> - Spurious regression warning for trending time series

---

## 12. ⭐ Advanced: Overfitting, Validation and Regularisation (Ridge and Lasso)
> ⭐ Advanced · _Added beyond the tracker_

### Definition
A model that fits the training data too closely (too many predictors for the sample) predicts new data badly. Guard against it with:
- **Train/test split or k-fold cross-validation**, reporting RMSE/MAE/MAPE on held-out data.
- **Regularisation:** add a penalty to the OLS loss.

$$\text{Ridge: } \min \sum(Y_i-\hat Y_i)^2+\lambda\sum\beta_j^2 \qquad \text{Lasso: } \min \sum(Y_i-\hat Y_i)^2+\lambda\sum|\beta_j|$$

Ridge shrinks coefficients (good for multicollinearity); **Lasso** can set some to exactly zero (variable selection). Scale predictors first and choose $\lambda$ by cross-validation.
- **Bias-variance trade-off:** simple models have high bias, complex ones high variance.
- For time series use **walk-forward** validation, never random shuffling.

```python
from sklearn.linear_model import LassoCV
lasso = LassoCV(cv=5).fit(X_scaled, y)
print(lasso.coef_)   # zeros = dropped variables
```

### Example
With 40 stores and 30 candidate predictors, OLS shows $R^2=0.98$ but a hold-out RMSE twice that of a model with 5 predictors; Lasso keeps 6 predictors and gives the best hold-out RMSE (illustrative).

### In the news
See news box. With only months of data on the new 2024-base series, flexible models overfit easily; regularisation and rolling validation matter.

### Interview angle
> [!question] How it is asked
> "How do you make sure your model will work on new data?"

> [!tip] Strong answer includes
> - Hold-out or cross-validation, and the gap between train and test error
> - Ridge vs Lasso, and what each does to coefficients
> - Time-ordered validation for forecasting
> - Simplicity and interpretability as a business requirement

---
## 🔗 Go deeper: expansion notes
- [[209 Generalised Linear Models & Categorical Data Analysis|Generalised Linear Models & Categorical Data Analysis]]
- [[208 Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory|Time-Series Models - ARIMA, SARIMA & Exponential Smoothing Theory]]
- [[216 Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab|Statistical Tools Cookbook - Excel, Python, R, SPSS & Minitab]]
