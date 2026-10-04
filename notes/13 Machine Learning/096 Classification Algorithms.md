---
tags: [machine-learning, tier1]
area: Machine Learning
topic: "Classification Algorithms"
tier: Tier 1
roles: PM / Operations
status: complete
subtopics: 14
---
# Classification Algorithms

⬅ [[095 Regression Algorithms]] · [[_Index - Machine Learning|Machine Learning]] · [[097 Unsupervised Learning]] ➡

> **Area:** Machine Learning · **Priority:** 🔴 Tier 1 · **Target roles:** PM / Operations

## Sub-topics in this note
1. [[#1. Logistic Regression]]
2. [[#2. Decision Tree Classifier]]
3. [[#3. Random Forest Classifier]]
4. [[#4. Gradient Boosting (XGBoost/LightGBM)]]
5. [[#5. K-Nearest Neighbors (KNN)]]
6. [[#6. Naive Bayes]]
7. [[#7. Support Vector Machine (SVM)]]
8. [[#8. Neural Network (MLP)]]
9. [[#9. Evaluation: Classification Metrics]]
10. [[#10. Confusion Matrix]]
11. [[#11. ROC Curve & AUC]]
12. [[#12. Class Imbalance Handling]]
13. [[#13. ⭐ Advanced: Cost-Sensitive Thresholds and Precision-Recall Trade-off]]
14. [[#14. ⭐ Advanced: Multi-class, Multi-label Metrics and Probability Scoring]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Classification at national scale, fraud detection in Indian banking
> **RBI's MuleHunter.AI (announced Dec 2024).** The Reserve Bank Innovation Hub's ML tool flags "mule" accounts (accounts used to move illicit funds) by analysing transaction and account data, built after studying 19 distinct behaviour patterns with banks. It was piloted with two public sector banks, which found more mule accounts than traditional rule-based methods. By 10 Dec 2025, 23 banks had implemented it (about 15 reported in Aug 2025). RBI declined to disclose the number of mule accounts found. The sources describe the problem as flagging accounts but do not name the algorithm. ([Business Standard](https://www.business-standard.com/finance/personal-finance/explained-rbi-has-a-new-ai-tool-mulehunter-ai-to-reduce-digital-frauds-124120900250_1.html), [MediaNama](https://www.medianama.com/2025/12/223-rti-23-banks-mulehunter-mule-accounts/))
>
> **Stanford AI Index 2025 (April 2025).** 78% of organisations reported using AI in 2024 (55% in 2023); inference cost for GPT-3.5-level performance fell over 280-fold from Nov 2022 to Oct 2024. ([Business Wire summary of the Stanford HAI report](https://www.businesswire.com/news/home/20250407539812/en/Stanford-HAIs-2025-AI-Index-Reveals-Record-Growth-in-AI-Capabilities-Investment-and-Regulation))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Logistic Regression
> 🔴 Tier 1 · _Tracker hint:_ Binary/multi-class; sigmoid function; output = probability; threshold for class assignment

### Definition
Despite the name, logistic regression is a **classifier**. It models the log-odds as linear:

$$\ln\frac{p}{1-p}=z=\beta_0+\beta_1x_1+\dots+\beta_px_p,\qquad p=\sigma(z)=\frac{1}{1+e^{-z}}$$

Fitted by maximum likelihood (minimising log-loss). The output is a **probability**; assign class 1 if $p\ge t$ (default $t=0.5$, but tune $t$ to costs). Each $e^{\beta_j}$ is an **odds ratio**: the multiplicative change in odds per unit rise in $x_j$. Multi-class: one-vs-rest or softmax. Add L1/L2 regularisation (`C` is the inverse strength). Scale features for regularised fits. Decision boundary is linear; add interactions or polynomial terms for curves.

```python
from sklearn.linear_model import LogisticRegression
m = LogisticRegression(C=1.0, class_weight="balanced", max_iter=1000).fit(X_train_s, y_train)
p = m.predict_proba(X_test_s)[:, 1]
```

### Example
$z=1.5$: $p=1/(1+e^{-1.5})=1/(1+0.2231)=$ **0.818**; odds = $e^{1.5}=4.48$. With threshold 0.5, class = 1. If $\beta_1=0.7$, a one-unit rise in $x_1$ multiplies odds by $e^{0.7}=2.01$.

### In the news
See news box. Interpretable baselines like logistic regression are what banks usually benchmark newer fraud models against.

### Interview angle
> [!question] How it is asked
> "Why not use linear regression for a yes/no outcome?" or "How do you interpret logistic regression coefficients?"

> [!tip] Strong answer includes
> - Sigmoid maps to (0,1); log-odds linear
> - Odds ratio interpretation
> - Threshold chosen by cost, not fixed 0.5
> - MLE and log-loss; regularisation

---

## 2. Decision Tree Classifier
> 🔴 Tier 1 · _Tracker hint:_ Splits on Gini impurity or Information Gain (entropy); easy to interpret

### Definition
A tree repeatedly splits data to make child nodes purer. Impurity measures for class proportions $p_k$:

$$\text{Gini}=1-\sum_k p_k^2,\qquad \text{Entropy}=-\sum_k p_k\log_2 p_k$$

**Information gain** = parent entropy minus weighted child entropy. The split with the largest gain (or Gini decrease) is chosen; leaves predict the majority class (or class proportions). Pros: readable rules, no scaling, handles mixed data. Cons: overfits, unstable to small data changes, axis-aligned splits. Control via `max_depth`, `min_samples_leaf`, pruning.

```python
from sklearn.tree import DecisionTreeClassifier, export_text
t = DecisionTreeClassifier(criterion="gini", max_depth=4, min_samples_leaf=30).fit(X_train, y_train)
print(export_text(t, feature_names=list(X.columns)))
```

### Example
A node with 6 positives and 4 negatives: $p=0.6,0.4$. Gini = 1-(0.36+0.16) = **0.48**. Entropy = -(0.6 log₂0.6 + 0.4 log₂0.4) = 0.6(0.737)+0.4(1.322) = **0.971** bits. A pure node has 0 for both; a 50/50 node has Gini 0.5, entropy 1.

### In the news
See news box. Regulated settings favour rule-like, explainable models, which keeps shallow trees relevant.

### Interview angle
> [!question] How it is asked
> "How does a decision tree choose splits? Gini versus entropy?"

> [!tip] Strong answer includes
> - Impurity formulas and a worked computation
> - Greedy, recursive splitting and stopping rules
> - Overfitting and pruning
> - Gini and entropy usually give similar trees

---

## 3. Random Forest Classifier
> 🔴 Tier 1 · _Tracker hint:_ Bagging of decision trees; majority vote; handles missing data; robust

### Definition
Many decorrelated trees, each trained on a bootstrap sample with a random subset of features at each split (typically $\sqrt p$ for classification). The forest predicts by **majority vote** (or averaged probabilities). Averaging cuts variance, so it is robust to noise and overfits less than one tree. Features: out-of-bag error estimate, feature importances, little tuning, works with mixed features and non-linearity. Key parameters: `n_estimators`, `max_features`, `max_depth`, `min_samples_leaf`, `class_weight`. Note: scikit-learn's forest historically needed imputed data (newer versions support NaN in some trees), so state that missing values are usually imputed first. Probabilities are often not well calibrated ([[098 Model Selection & Optimization]]).

```python
from sklearn.ensemble import RandomForestClassifier
m = RandomForestClassifier(n_estimators=300, class_weight="balanced_subsample", oob_score=True, n_jobs=-1)
```

### Example
100 trees; 62 vote "default". Predicted class = default; probability estimate 62/100 = **0.62**. If a high-recall policy sets the threshold at 0.4, it is flagged even at 45 votes.

### In the news
See news box. Ensembles of trees are a common production choice for fraud and risk scoring on tabular data (general practice; the RBI sources do not name an algorithm).

### Interview angle
> [!question] How it is asked
> "Why does a random forest outperform a single decision tree?"

> [!tip] Strong answer includes
> - Bootstrap plus random features means decorrelated trees; vote reduces variance
> - OOB score as free validation
> - Strengths: robust, minimal preprocessing; weaknesses: less interpretable, calibration
> - Feature importance caveat (bias towards high-cardinality features)

---

## 4. Gradient Boosting (XGBoost/LightGBM)
> 🔴 Tier 1 · _Tracker hint:_ State-of-art for tabular data; hyperparams: n_estimators, max_depth, learning_rate

### Definition
Boosting builds trees **sequentially**, each fitting the errors (gradient of log-loss) of the current ensemble: $F_m=F_{m-1}+\nu h_m$; the final probability is $\sigma(F_M)$. It usually tops other methods on **tabular** data.

| Hyperparameter | Effect |
|---|---|
| `n_estimators` | Number of rounds; use early stopping |
| `learning_rate` | Shrinkage; small plus many trees is better |
| `max_depth` / `num_leaves` | Complexity of each tree (3 to 8) |
| `subsample`, `colsample_bytree` | Row/column sampling, reduce variance |
| `reg_lambda`, `reg_alpha`, `min_child_weight` | Regularisation |
| `scale_pos_weight` | Imbalance handling in XGBoost |

LightGBM is fast (histogram, leaf-wise); CatBoost handles categories natively.

```python
import lightgbm as lgb
m = lgb.LGBMClassifier(n_estimators=1000, learning_rate=0.03, num_leaves=31)
m.fit(X_tr, y_tr, eval_set=[(X_va, y_va)], callbacks=[lgb.early_stopping(50)])
```

### Example
With learning_rate 0.1 and 200 rounds versus 0.02 and 1,000 rounds, the second usually generalises a little better but trains 5x longer. A fraud team picks the second for the nightly batch and the first for quick experiments.

### In the news
See news box. For high-volume transaction classification, fast boosted models are practical because inference is cheap (280-fold cost drop in the AI Index for LLM-class inference; tree models are far cheaper still).

### Interview angle
> [!question] How it is asked
> "Why is XGBoost popular? How would you tune it?"

> [!tip] Strong answer includes
> - Sequential error correction, regularised, handles missing values
> - Key hyperparameters and the learning-rate versus trees trade-off
> - Early stopping on a validation set
> - When not to use: tiny data, images/text, need for simple explanations

---

## 5. K-Nearest Neighbors (KNN)
> 🔴 Tier 1 · _Tracker hint:_ Classify based on k nearest training points; distance metric (Euclidean); scale features first

### Definition
KNN is a **lazy learner**: no training; at prediction it finds the $k$ closest training points and takes a majority vote (optionally distance-weighted). Euclidean distance $d=\sqrt{\sum(x_i-x_i')^2}$ (also Manhattan, cosine). Small $k$ means high variance, large $k$ means high bias; choose $k$ by CV (odd $k$ for binary). **Scale features** or the large-range feature dominates; it suffers in high dimensions ("curse of dimensionality") and is slow at prediction on big data (use KD-trees, approximate nearest neighbours). Good for recommenders and as a baseline.

```python
from sklearn.neighbors import KNeighborsClassifier
m = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=7, weights="distance"))
```

### Example
Query (2,3). Training points: A(3,3) class 1, d=1; B(2,5) class 0, d=2; C(6,3) class 1, d=4; D(5,7) class 0, d=$\sqrt{9+16}=5$. With k=3 neighbours A, B, C: votes 1,0,1 so class **1**. Scale issue: age (20 to 60) and income (20,000 to 200,000): without scaling income decides everything.

### In the news
See news box. Similar-behaviour matching, the core intuition of KNN, underlies pattern-based flagging, although MuleHunter.AI's actual method is not described in the sources.

### Interview angle
> [!question] How it is asked
> "Why must you scale features for KNN, and how do you choose k?"

> [!tip] Strong answer includes
> - Distance-based, so scale matters
> - k trades bias and variance; pick by cross-validation
> - Curse of dimensionality and slow inference
> - Handling ties and weighted voting

---

## 6. Naive Bayes
> 🔴 Tier 1 · _Tracker hint:_ P(class|features) via Bayes; assumes feature independence; fast; good for text/NLP

### Definition
Applies Bayes' theorem with a "naive" assumption that features are **conditionally independent given the class**:

$$P(C\mid x_1..x_n)\propto P(C)\prod_{i}P(x_i\mid C)$$

Pick the class with the highest posterior. Variants: **Gaussian** (continuous), **Multinomial** (word counts), **Bernoulli** (binary). Use **Laplace smoothing** to avoid zero probabilities. Very fast, works with little data and many features (text), but the independence assumption is wrong in practice and probabilities are poorly calibrated though rankings are often good.

```python
from sklearn.naive_bayes import MultinomialNB
m = MultinomialNB(alpha=1.0).fit(X_counts, y)
```

### Example
Spam prior $P(S)=0.4$; word "lottery" appears in 50% of spam, 5% of ham. $P(S\mid w)=\dfrac{0.4\times0.5}{0.4\times0.5+0.6\times0.05}=\dfrac{0.20}{0.23}=$ **0.870**.

### In the news
See news box. Text classification of complaints and messages still uses Naive Bayes as a fast baseline, though the RBI tool works on transaction behaviour.

### Interview angle
> [!question] How it is asked
> "Why is Naive Bayes called naive, and why does it still work?"

> [!tip] Strong answer includes
> - Independence assumption and the formula
> - Needs only class-wise counts, so fast and data-efficient
> - Laplace smoothing
> - Ranking good, probabilities not calibrated

---

## 7. Support Vector Machine (SVM)
> 🔴 Tier 1 · _Tracker hint:_ Maximize margin between classes; kernel trick (RBF, polynomial); works in high dimensions

### Definition
SVM finds the hyperplane $w\cdot x+b=0$ that **maximises the margin** (distance between classes), where margin $=\dfrac{2}{\|w\|}$. Soft-margin objective: $\min\ \tfrac12\|w\|^2+C\sum\xi_i$. Only **support vectors** (points on or inside the margin) define the boundary. **Kernel trick** computes similarity in a higher-dimensional space without constructing it: linear, polynomial, **RBF** $K(x,x')=e^{-\gamma\|x-x'\|^2}$. $C$ high means fewer violations, more overfit; $\gamma$ high means narrow, wiggly boundary. Needs scaling; probability outputs require extra calibration; slow on large datasets (more than about 100k rows); strong for high-dimensional, small-to-medium data.

```python
from sklearn.svm import SVC
m = make_pipeline(StandardScaler(), SVC(kernel="rbf", C=1, gamma="scale", probability=True))
```

### Example
If $w=(3,4)$ then $\|w\|=5$ and margin = 2/5 = **0.4** units. Shrinking $\|w\|$ to 2.5 would double the margin to 0.8, which is what the optimiser seeks subject to classifying points correctly.

### In the news
See news box. Boosted trees and neural networks have largely displaced SVMs in production, so expect SVM mainly as a concept question.

### Interview angle
> [!question] How it is asked
> "What is the kernel trick and what do C and gamma do in SVM?"

> [!tip] Strong answer includes
> - Maximum-margin idea and support vectors
> - Kernel intuition: separate in a higher dimension without computing it
> - C and $\gamma$ effects on bias-variance
> - Scale features; limits on big data

---

## 8. Neural Network (MLP)
> 🔴 Tier 1 · _Tracker hint:_ Input → Hidden layers → Output; activation functions; backpropagation; use for complex patterns

### Definition
A **multi-layer perceptron** stacks layers: each neuron computes $a=\phi(w\cdot x+b)$. Activation functions add non-linearity: **ReLU** $\max(0,z)$ in hidden layers, **sigmoid** for binary output, **softmax** for multi-class. Training: forward pass computes loss (cross-entropy); **backpropagation** applies the chain rule to get gradients; an optimiser (SGD, Adam) updates weights; repeat over mini-batches and epochs. Regularise with dropout, weight decay, early stopping. Needs scaled inputs and usually lots of data; on tabular data it often does not beat gradient boosting. Good for images, text, audio, and very large datasets.

```python
from sklearn.neural_network import MLPClassifier
m = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(64,32), early_stopping=True))
```

### Example
One neuron: inputs x=(1,2), weights w=(0.5,0.25), bias 0.1: $z=0.5+0.5+0.1=1.1$. ReLU output 1.1. With sigmoid: $1/(1+e^{-1.1})=1/(1+0.3329)=$ **0.750**.

### In the news
See news box. Deep models are advancing fastest, but for tabular fraud-type problems simpler models often remain competitive.

### Interview angle
> [!question] How it is asked
> "Explain how a neural network learns. When would you not use one?"

> [!tip] Strong answer includes
> - Layers, activations, loss, backpropagation, optimiser
> - Why non-linear activations are needed
> - Overfitting controls
> - Not for small tabular data where boosting is simpler and more explainable

---

## 9. Evaluation: Classification Metrics
> 🔴 Tier 1 · _Tracker hint:_ Accuracy=(TP+TN)/total; Precision=TP/(TP+FP); Recall=TP/(TP+FN); F1=2×P×R/(P+R)

### Definition
$$Acc=\frac{TP+TN}{N},\quad Precision=\frac{TP}{TP+FP},\quad Recall=\frac{TP}{TP+FN},\quad F_1=\frac{2PR}{P+R}$$

Also: **Specificity** $=TN/(TN+FP)$; $F_\beta$ weights recall more when $\beta>1$; **log-loss** scores probabilities; **MCC** is robust to imbalance.

- **Precision** answers "of those flagged, how many are real?" (cost of false alarms).
- **Recall** answers "of the real ones, how many did we catch?" (cost of misses).
- They trade off through the threshold. Report the metric that matches the business cost; use macro/weighted averaging for multi-class.

### Example
1,000 accounts: TP=40, FP=10, FN=20, TN=930. Accuracy = 970/1000 = 0.97. Precision = 40/50 = **0.80**. Recall = 40/60 = **0.667**. F1 = 2(0.8)(0.667)/(1.467) = **0.727**. A model that flags nobody scores 940/1000 = **94% accuracy** with zero recall, which is why accuracy misleads.

### In the news
See news box. RBI framed rule-based fraud detection as generating false positives (hurting precision) and missing evolving tactics (hurting recall); both matter, and banks must pick the balance.

### Interview angle
> [!question] How it is asked
> "Your fraud model has 99% accuracy. Is it good?"

> [!tip] Strong answer includes
> - Not by itself: check the base rate and a do-nothing baseline
> - Precision, recall, F1 and what each error costs
> - Threshold selection
> - Possibly PR-AUC for rare events

---

## 10. Confusion Matrix
> 🔴 Tier 1 · _Tracker hint:_ 2×2 table: TP, FP, FN, TN; class imbalance affects accuracy; use F1, AUC for imbalanced

### Definition
The confusion matrix tabulates predictions versus actuals:

| | Predicted positive | Predicted negative |
|---|---|---|
| **Actual positive** | TP (hit) | FN (miss, Type II) |
| **Actual negative** | FP (false alarm, Type I) | TN (correct rejection) |

All classification metrics derive from it. Row-normalised values give recall and specificity; column-normalised give precision. For multi-class it becomes $K\times K$, showing which classes get confused. Always read it alongside the class counts. Changing the threshold moves counts between cells: lower threshold means more TP and more FP.

```python
from sklearn.metrics import confusion_matrix, classification_report
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
```

### Example
Using TP=40, FP=10, FN=20, TN=930: the cell FN=20 means 20 mule accounts were missed; FP=10 means 10 genuine customers were wrongly flagged. FPR = 10/940 = **0.0106**; TPR = 40/60 = 0.667. Lowering the threshold might give TP=50, FP=40, FN=10, TN=900: recall 0.833, precision 0.556.

### In the news
See news box. An FP here is a genuine customer facing a frozen account; an FN is laundered money moving: the matrix makes that trade-off explicit for policymakers.

### Interview angle
> [!question] How it is asked
> "Draw a confusion matrix and tell me which cells matter for this business problem."

> [!tip] Strong answer includes
> - Correct layout with Type I and II errors
> - Maps cells to rupee or customer cost
> - How the threshold shifts cells
> - Imbalance: prefer precision, recall, F1, PR/ROC curves

---

## 11. ROC Curve & AUC
> 🔴 Tier 1 · _Tracker hint:_ TPR vs FPR at different thresholds; AUC=area under curve; AUC=1 perfect, 0.5=random

### Definition
The **ROC curve** plots **TPR (recall)** against **FPR** $=FP/(FP+TN)$ as the decision threshold sweeps from 1 to 0. The diagonal is random guessing. **AUC** is the area under the curve: the probability that a randomly chosen positive gets a higher score than a randomly chosen negative. 1.0 is perfect, 0.5 random, below 0.5 worse than random (flip the labels). AUC is threshold-independent and insensitive to class prior, but with **severe imbalance** the **precision-recall curve (PR-AUC)** is more informative because FPR stays small when negatives are huge. Pick the operating point using costs (e.g. Youden's J = TPR - FPR).

```python
from sklearn.metrics import roc_auc_score, roc_curve
auc = roc_auc_score(y_test, p)
fpr, tpr, thr = roc_curve(y_test, p)
```

### Example
ROC points (FPR, TPR): (0,0), (0.1,0.6), (0.3,0.85), (1,1). Trapezoid area: 0.1×(0+0.6)/2 = 0.03; 0.2×(0.6+0.85)/2 = 0.145; 0.7×(0.85+1)/2 = 0.6475. Total AUC = **0.8225**.

### In the news
See news box. For rare-event problems such as mule accounts, a high AUC can still hide poor precision at useful thresholds, so check PR curves too.

### Interview angle
> [!question] How it is asked
> "What does AUC of 0.8 mean? When is ROC-AUC misleading?"

> [!tip] Strong answer includes
> - Ranking interpretation (probability a positive outranks a negative)
> - Threshold-free versus a single operating point
> - Misleading under heavy imbalance: use PR-AUC
> - Choosing the threshold by cost

---

## 12. Class Imbalance Handling
> 🔴 Tier 1 · _Tracker hint:_ SMOTE (oversample minority), class_weight='balanced', threshold tuning, F1/AUC metrics

### Definition
When one class is rare (fraud, churn, defects), models favour the majority class. Options:

- **Metrics first:** precision, recall, F1, PR-AUC, not accuracy.
- **Class weights:** `class_weight="balanced"` gives weight $w_c=\dfrac{N}{K\cdot n_c}$.
- **Resampling:** random under-sampling (loses data), over-sampling, or **SMOTE** (synthetic minority points interpolated between neighbours).
- **Threshold tuning:** move the cut-off from 0.5 using costs.
- **Algorithms:** boosted trees with `scale_pos_weight`, anomaly detection for extreme rarity.
- **Rule:** resample **only the training folds** (use `imblearn.pipeline`), never validation or test data, and use stratified splits.

```python
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
pipe = Pipeline([("smote", SMOTE(random_state=0)), ("clf", LogisticRegression(max_iter=1000))])
```

### Example
10,000 rows, 100 positives (1%). Balanced weights: negatives $10000/(2\times9900)=$ **0.505**; positives $10000/(2\times100)=$ **50**. Each missed positive is penalised about 99 times as much as a missed negative.

### In the news
See news box. Mule accounts are a tiny fraction of all accounts, so such systems live with severe imbalance and must be judged on precision and recall rather than accuracy.

### Interview angle
> [!question] How it is asked
> "You have 1% fraud in the data. How do you build the model?"

> [!tip] Strong answer includes
> - Metric choice (PR-AUC, recall at fixed precision)
> - Class weights or SMOTE applied only inside training folds
> - Threshold tuning with a cost matrix
> - Stratified validation and monitoring after launch

---

## 13. ⭐ Advanced: Cost-Sensitive Thresholds and Precision-Recall Trade-off
> ⭐ Advanced · _Added beyond the tracker_

### Definition
The default 0.5 threshold is rarely optimal. With cost of a false positive $c_{FP}$ and false negative $c_{FN}$, and a **calibrated** probability $p$, predict positive when

$$p>\frac{c_{FP}}{c_{FP}+c_{FN}}$$

Alternatively compute total expected cost across thresholds and choose the minimum, or pick the threshold meeting an operational constraint ("recall at least 90%" or "review capacity of 500 cases a day"). Show the **precision-recall curve** and **gain/lift** charts to stakeholders; capacity-constrained settings use **precision at top-K**.

### Example
Missing a fraud costs Rs 5,000; reviewing a false alarm costs Rs 100. Threshold = 100/(100+5000) = **0.0196**, so flag anything above about 2% probability. If reviewers can only handle 500 cases a day, take the top 500 scores instead and report precision@500.

### In the news
See news box. RBI's problem statement (too many false positives from rules versus missed mules) is exactly a cost-trade-off setting.

### Interview angle
> [!question] How it is asked
> "How would you decide the cut-off for flagging transactions?"

> [!tip] Strong answer includes
> - Costs of FP versus FN and the threshold formula
> - Need for calibrated probabilities
> - Operational constraint (review capacity) and precision@K
> - Revisit threshold as base rates drift

---

## 14. ⭐ Advanced: Multi-class, Multi-label Metrics and Probability Scoring
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **Multi-class (one label among K):** use softmax; report per-class precision and recall; **macro-average** (each class equal, exposes poor minority classes), **micro-average** (pools counts, equals accuracy for single-label), **weighted** (by support).
- **Multi-label (several labels per item):** one binary classifier per label; metrics like Hamming loss, per-label F1.
- **Probability quality:** **log-loss** $=-\frac1n\sum[y\ln p+(1-y)\ln(1-p)]$ and **Brier score** $=\frac1n\sum(p-y)^2$ penalise overconfident errors.
- **Ordinal targets** (ratings 1 to 5): consider ordinal models or MAE rather than plain accuracy.

### Example
Three classes with F1 = 0.90 (80% of data), 0.60 and 0.30 (10% each). Macro-F1 = (0.90+0.60+0.30)/3 = **0.60**. Weighted-F1 = 0.8(0.9)+0.1(0.6)+0.1(0.3) = 0.72+0.06+0.03 = **0.81**. The weighted figure hides the poor minority classes. Log-loss for a confident wrong prediction p=0.01 when y=1: $-\ln 0.01=4.6$, versus 0.69 for p=0.5.

### In the news
See news box. In national-scale systems, the minority patterns are exactly what matters, so macro-level views are more informative than headline accuracy.

### Interview angle
> [!question] How it is asked
> "Your 5-class classifier has 85% accuracy but the client is unhappy. Why?"

> [!tip] Strong answer includes
> - Look at per-class metrics and the confusion matrix
> - Macro versus weighted averaging, and why they differ
> - Probability-based metrics for confidence
> - Link errors to which class the business cares about

---
## 🔗 Go deeper: expansion notes
- [[220 Responsible AI, Explainability & Model Governance|Responsible AI, Explainability & Model Governance]]
