---
tags: [python-programming, tier1]
area: Python Programming
topic: "NumPy"
tier: Tier 1
roles: Operations / PM
status: complete
subtopics: 12
---
# NumPy

⬅ [[062 Python Fundamentals]] · [[_Index - Python Programming|Python Programming]] · [[064 Pandas — Data Manipulation]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** Operations / PM

## Sub-topics in this note
1. [[#1. Array Creation]]
2. [[#2. Array Operations]]
3. [[#3. Indexing & Slicing]]
4. [[#4. Shape Operations]]
5. [[#5. Statistical Functions]]
6. [[#6. Random Module]]
7. [[#7. Linear Algebra]]
8. [[#8. Vectorization vs Loops]]
9. [[#9. np.where()]]
10. [[#10. Sorting & Searching]]
11. [[#11. ⭐ Advanced: Memory, dtypes & Performance Pitfalls]]
12. [[#12. ⭐ Advanced: Monte Carlo & Matrix Methods for Operations]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): NumPy's first major release in years, and steady modernisation since
> **NumPy 2.0.0 (16 Jun 2024).** The first major release since 2006 (the NumPy news page calls it the first major release in 20 years): 212 contributors and 1,078 pull requests, with ABI/API breaking changes and new type-promotion rules that downstream packages had to migrate to. ([Source](https://numpy.org/news/))
> 
> **Steady cadence since.** 2.1.0 (Aug 2024) added Python 3.13 support; 2.2.0 (Dec 2024) added `matvec`/`vecmat` and StringDType improvements; 2.3.0 (Jun 2025) improved free-threading support; 2.4.0 (Dec 2025); and **2.5.0 (21 Jun 2026)** removed distutils, dropped Python 3.11 and made sorting compliant with the array-api standard for descending sorts. ([Source](https://numpy.org/news/))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Array Creation
> 🔴 Tier 1 · _Tracker hint:_ np.array([1,2,3]), np.zeros((3,4)), np.ones(), np.arange(0,10,2), np.linspace(0,1,100)

### Definition
A NumPy **ndarray** is a fixed-type, contiguous, N-dimensional array. It stores raw values (not Python objects), which is why it is compact and fast.

```python
import numpy as np
np.array([1, 2, 3])            # from list, dtype int64
np.array([[1, 2], [3, 4]])     # 2-D
np.zeros((3, 4))               # 3x4 of 0.0
np.ones(5, dtype=int)
np.full((2, 2), 7)
np.eye(3)                      # identity
np.arange(0, 10, 2)            # [0 2 4 6 8], stop excluded
np.linspace(0, 1, 5)           # [0. 0.25 0.5 0.75 1.], stop included
np.empty(3)                    # uninitialised
arr.dtype, arr.ndim, arr.size
```
`arange` takes a *step*; `linspace` takes the *number of points* (and includes the endpoint by default). Specify `dtype` (`float32`) to save memory.

### Example
Demand for 12 months starts as a list; `d = np.array([120,135,128,150,142,160,155,170,165,180,175,190])` lets you write `d.mean()` = 155.83 instead of looping. A time axis for 12 months: `np.arange(1, 13)`.

### In the news
See news box. NumPy 2.x changed default integer and promotion behaviour, so explicit `dtype` in creation calls makes code portable across versions.

### Interview angle
> [!question] How it is asked
> "Difference between `arange` and `linspace`?" or "How is a NumPy array different from a Python list?"

> [!tip] Strong answer includes
> - Homogeneous, contiguous memory vs list of object pointers
> - `arange` (step, excludes stop) vs `linspace` (count, includes stop)
> - dtype control and memory impact
> - Knows `zeros`, `ones`, `full`, `eye`

---

## 2. Array Operations
> 🔴 Tier 1 · _Tracker hint:_ Element-wise: +,-,*,/,**; np.dot() for matrix mult; broadcasting rules

### Definition
Arithmetic operators work **element-wise**. `*` is NOT matrix multiplication; use `@` or `np.dot`.

```python
a = np.array([1, 2, 3]); b = np.array([10, 20, 30])
a + b, a * b, a ** 2, b / a     # element-wise
A = np.array([[1, 2], [3, 4]]); B = np.array([[5, 6], [7, 8]])
A @ B                            # matrix product [[19 22],[43 50]]
np.dot(a, b)                     # 140 (dot product)
```
**Broadcasting rules:** compare shapes from the right; two dimensions are compatible if they are equal or one is 1; the size-1 axis is "stretched". Shapes `(3,4)` and `(4,)` work; `(3,4)` and `(3,)` fail, while `(3,4)` and `(3,1)` work.

```python
X = np.arange(12).reshape(3, 4)
X - X.mean(axis=0)               # subtract column means: (3,4)-(4,)
```

### Example
Revenue = price x quantity: `price = np.array([50, 120, 80]); qty = np.array([10, 4, 25])`; `price*qty = [500, 480, 2000]`, total 2,980 (`np.dot(price, qty)` gives the same 2,980 in one step).

### In the news
See news box. NumPy 2.2 added dedicated `matvec`/`vecmat` functions, showing continued investment in linear-algebra primitives.

### Interview angle
> [!question] How it is asked
> "What is broadcasting?" "What does `*` do on two 2-D arrays?"

> [!tip] Strong answer includes
> - Element-wise vs matrix multiplication (`@`)
> - The right-to-left shape rule with an example
> - Typical use: standardising columns (subtract mean, divide by std)
> - Knows a shape mismatch error and how to fix with `reshape` or `[:, None]`

---

## 3. Indexing & Slicing
> 🔴 Tier 1 · _Tracker hint:_ arr[0], arr[1:3], arr[arr>5] (boolean indexing), arr[[0,2,4]] (fancy indexing)

### Definition
```python
a = np.array([10, 20, 30, 40, 50, 60])
a[0], a[-1]          # 10, 60
a[1:3]               # [20 30]  -- a VIEW (shares memory)
a[a > 25]            # boolean mask -> [30 40 50 60]  -- a COPY
a[[0, 2, 4]]         # fancy indexing -> [10 30 50]   -- a COPY
M = np.arange(12).reshape(3, 4)
M[1, 2]              # row 1, col 2
M[:, 1]              # column 1
M[M[:, 0] > 0, :]    # filter rows
a[(a > 20) & (a < 60)]   # combine with & | ~ and parentheses
```
Slices return **views**: modifying them changes the original; use `.copy()` to detach. Boolean and fancy indexing return copies. Use `&`, `|`, `~` (not `and`, `or`, `not`).

### Example
Daily demand `d = np.array([120, 135, 128, 150, 142])`. Days above the mean 135: `d[d > d.mean()]` = `[150, 142]` (the mean is 135, so 135 itself is excluded). Set outliers: `d[d > 145] = 145` caps values in place.

### In the news
See news box. pandas 3.0 Copy-on-Write brings DataFrames closer to a clear copy-vs-view story, an area where NumPy users already need care.

### Interview angle
> [!question] How it is asked
> "Does slicing copy the array?" "How do you filter an array by condition?"

> [!tip] Strong answer includes
> - View vs copy distinction and the consequence
> - Boolean masks with `&`/`|` and parentheses
> - 2-D indexing `[row, col]`, `:` for all
> - Fancy indexing and when it copies

---

## 4. Shape Operations
> 🔴 Tier 1 · _Tracker hint:_ arr.shape, arr.reshape(3,4), arr.flatten(), arr.T (transpose)

### Definition
```python
a = np.arange(12)
a.shape                 # (12,)
b = a.reshape(3, 4)     # 3 rows, 4 cols
a.reshape(2, -1)        # -1 infers 6 -> (2, 6)
b.T                     # transpose (4, 3), a view
b.flatten()             # 1-D COPY
b.ravel()               # 1-D view when possible
a[:, None]              # add axis -> (12, 1)
np.concatenate([x, y], axis=0)
np.vstack([x, y]); np.hstack([x, y])
np.squeeze(arr); arr.swapaxes(0, 1)
```
The total number of elements must stay the same: reshaping 12 into `(5, 3)` raises `ValueError`. `axis=0` runs down rows (column-wise result), `axis=1` runs across columns.

### Example
Hourly demand for 3 days in a flat array of 72 values: `h = demand.reshape(3, 24)` gives one row per day; `h.mean(axis=0)` gives the average demand profile for each hour of the day (24 values).

### In the news
See news box. Shape errors were a typical migration headache in NumPy 2.0, where some function behaviours and defaults changed.

### Interview angle
> [!question] How it is asked
> "What does `reshape(-1, 1)` do?" or "Difference between `flatten` and `ravel`?"

> [!tip] Strong answer includes
> - `-1` inference and the element-count constraint
> - `flatten` copies, `ravel` can return a view
> - Understanding `axis` semantics
> - Why sklearn needs `X.reshape(-1, 1)` for a single feature

---

## 5. Statistical Functions
> 🔴 Tier 1 · _Tracker hint:_ np.mean(), np.median(), np.std(), np.var(), np.percentile(arr,75)

### Definition
```python
x = np.array([4, 8, 6, 5, 3, 7])
np.mean(x)            # 5.5
np.median(x)          # 5.5
np.var(x)             # population variance (ddof=0)
np.std(x, ddof=1)     # sample standard deviation
np.percentile(x, 75)  # 75th percentile
np.corrcoef(a, b)     # correlation matrix
M.mean(axis=0)        # per column; axis=1 per row
np.nanmean(x)         # ignore NaN
np.cumsum(x); np.max(x); np.ptp(x)   # ptp = max - min
```
Key trap: NumPy's default `ddof=0` (population), whereas pandas `.std()` defaults to `ddof=1` (sample). Formulas: $\sigma^2 = \frac{1}{n}\sum (x_i-\mu)^2$ (population) and $s^2=\frac{1}{n-1}\sum (x_i-\bar{x})^2$ (sample).

### Example
`x = [4,8,6,5,3,7]`: mean = 33/6 = 5.5. Deviations squared: 2.25, 6.25, 0.25, 0.25, 6.25, 2.25 sum to 17.5. Population variance = 17.5/6 = 2.917; sample variance = 17.5/5 = 3.5, sample std = 1.871. Used for safety stock: $SS = z \cdot \sigma_d \cdot \sqrt{L}$.

### In the news
See news box. The ddof difference between NumPy and pandas is a perennial source of mismatched numbers when analysts port code between them.

### Interview angle
> [!question] How it is asked
> "Why do `np.std` and `df.std()` give different answers?" or "How would you compute demand variability for safety stock?"

> [!tip] Strong answer includes
> - `ddof` explanation
> - `axis` handling and `nan`-versions
> - Median robust to outliers vs mean
> - Links stats to an ops use (safety stock, control limits)

---

## 6. Random Module
> 🔴 Tier 1 · _Tracker hint:_ np.random.seed(42), np.random.rand(), np.random.randn(), np.random.choice()

### Definition
```python
np.random.seed(42)               # legacy global seed
np.random.rand(3)                # uniform [0,1)
np.random.randn(3)               # standard normal N(0,1)
np.random.randint(1, 7, size=5)  # dice, high excluded
np.random.choice(["A","B","C"], size=10, p=[.5,.3,.2])
np.random.normal(100, 15, 1000)  # mean 100, sd 15

rng = np.random.default_rng(42)  # modern recommended API
rng.normal(100, 15, 1000); rng.integers(1, 7, 5); rng.choice(a, 3, replace=False)
```
A **seed** makes results reproducible. NumPy recommends the `Generator` API (`default_rng`) over the legacy global `np.random.*` functions. Used for simulation, bootstrapping and Monte Carlo.

### Example
Monte Carlo of stock-out risk: demand over lead time ~ Normal(mean 500, sd 80), reorder point 600. `d = rng.normal(500, 80, 100000); (d > 600).mean()` is about 0.106, matching theory: $P(Z > 1.25) \approx 0.1056$.

### In the news
See news box. Reproducibility (fixed seeds, pinned NumPy versions) matters more as NumPy's major and minor releases alter some defaults.

### Interview angle
> [!question] How it is asked
> "How would you simulate demand uncertainty?" or "Why set a seed?"

> [!tip] Strong answer includes
> - Seed for reproducibility; `default_rng` as modern API
> - Chooses a distribution suited to the data
> - Many runs and reads the probability from the fraction exceeding a threshold
> - Notes sampling error shrinks with more draws

---

## 7. Linear Algebra
> 🔴 Tier 1 · _Tracker hint:_ np.linalg.inv(), np.linalg.det(), np.linalg.eig(), np.linalg.solve()

### Definition
```python
A = np.array([[2, 1], [1, 3]]); b = np.array([8, 13])
np.linalg.det(A)            # 5.0
np.linalg.inv(A)            # inverse (needs det != 0)
np.linalg.solve(A, b)       # solves A x = b -> [2.2 3.6]
vals, vecs = np.linalg.eig(A)   # eigenvalues / eigenvectors
np.linalg.norm(v)
np.linalg.lstsq(X, y, rcond=None)   # least-squares regression
```
Prefer `solve(A, b)` over `inv(A) @ b`: it is faster and numerically more stable. Eigen-decomposition underpins PCA and Markov-chain steady states.

### Example
Two products share a machine: 2x + y = 8 hours and x + 3y = 13 hours. `solve` gives x = 2.2, y = 3.6. Check: 2(2.2)+3.6 = 8.0 and 2.2+3(3.6) = 13.0. Determinant 2x3 - 1x1 = 5.

### In the news
See news box. NumPy 2.2's `matvec`/`vecmat` additions reflect demand for clean matrix-vector primitives in ML workloads.

### Interview angle
> [!question] How it is asked
> "Solve a system of equations in Python" or "Why prefer `solve` to `inv`?"

> [!tip] Strong answer includes
> - `solve` over explicit inverse, with reasons
> - What a zero determinant means (singular)
> - Eigen-decomposition use in PCA/Markov chains
> - Least squares for regression

---

## 8. Vectorization vs Loops
> 🔴 Tier 1 · _Tracker hint:_ Vectorized ops 10-100x faster; avoid Python loops on arrays

### Definition
**Vectorization** pushes the loop into compiled C code, operating on whole arrays with contiguous memory and SIMD, avoiding per-element Python interpreter overhead and type checks.

```python
import numpy as np, time
x = np.random.rand(1_000_000)
# loop
out = [v * 2 + 1 for v in x]
# vectorised
out = x * 2 + 1
# time it
%timeit x * 2 + 1          # in Jupyter
```
Typical speed-ups run from about 10x to 100x or more depending on the operation (the tracker's range). Memory trade-off: vectorised code creates temporaries. Tools when you cannot vectorise: `np.vectorize` (a convenience wrapper, not faster), `numba`, `pandas.apply` (still slow), or rewriting using `np.where`/boolean masks.

### Example
Price with 18% GST for 1 million items: the loop `[p*1.18 for p in prices]` takes on the order of 100 ms in pure Python while `prices*1.18` takes a few ms. Exact times depend on the machine, so say "roughly an order of magnitude or more faster" rather than a precise figure.

### In the news
See news box. NumPy's free-threading support (2.1 onward) targets making multi-core parallel Python more practical, a complement to vectorisation.

### Interview angle
> [!question] How it is asked
> "Why is NumPy faster than lists?" or "How would you speed up this loop over a DataFrame?"

> [!tip] Strong answer includes
> - Contiguous typed memory, C loops, SIMD
> - Replace loops with vector ops, masks, `np.where`
> - Honest note: `np.vectorize` is not true vectorisation
> - Profile first (`%timeit`) before optimising

---

## 9. np.where()
> 🔴 Tier 1 · _Tracker hint:_ np.where(condition, value_if_true, value_if_false) — vectorized if-else

### Definition
`np.where(cond, x, y)` returns elements from `x` where `cond` is True and from `y` otherwise, for the whole array at once. With only the condition, it returns the **indices** where it is True.

```python
a = np.array([5, 12, 8, 20])
np.where(a > 10, "high", "low")     # ['low' 'high' 'low' 'high']
np.where(a > 10, a, 0)              # [0 12 0 20]
np.where(a > 10)                    # (array([1, 3]),) indices
np.select([a < 6, a < 15], ["L", "M"], default="H")   # multi-branch
np.clip(a, 6, 15)
```
Nested `np.where` handles three outcomes; `np.select` is cleaner for many. In pandas the equivalent is `np.where` on a column or `Series.where`/`mask`.

### Example
Flag SKUs for reorder: stock `[40, 5, 18, 0]`, reorder point 10. `np.where(stock <= 10, "REORDER", "OK")` gives `['OK','REORDER','OK','REORDER']`. Count to reorder: `(stock <= 10).sum()` = 2.

### In the news
See news box. As NumPy and pandas evolve, vectorised conditionals remain the idiomatic alternative to row-by-row `apply`.

### Interview angle
> [!question] How it is asked
> "Add a column that labels rows high/medium/low without a loop."

> [!tip] Strong answer includes
> - Three-argument form for if-else, one-argument form for indices
> - `np.select` for several conditions
> - Avoids `apply` with `if` inside
> - Handles NaN explicitly (comparisons with NaN are False)

---

## 10. Sorting & Searching
> 🔴 Tier 1 · _Tracker hint:_ np.sort(), np.argsort(), np.argmax(), np.argmin(), np.unique()

### Definition
```python
a = np.array([30, 10, 50, 20])
np.sort(a)                 # [10 20 30 50] (copy); a.sort() in place
np.argsort(a)              # [1 3 0 2] indices that sort a
a[np.argsort(a)[::-1]]     # descending [50 30 20 10]
np.argmax(a), np.argmin(a) # 2, 1
np.unique([1, 2, 2, 3], return_counts=True)   # (array([1,2,3]), array([1,2,1]))
np.searchsorted(sorted_a, 25)   # binary search insertion point
np.cumsum(a); np.partition(a, -2)   # top-k without full sort
```
`argsort` is key for ranking one array by another (e.g. sort SKUs by revenue). Note that NumPy 2.5 made descending sorts compliant with the array-api standard.

### Example
`sku = np.array(["A","B","C","D"]); rev = np.array([300, 500, 100, 100])`. `order = np.argsort(rev)[::-1]` gives `[1, 0, ...]`, so `sku[order][:2]` = `["B","A"]` (top 2). Cumulative share: 500/1000 = 50%, then 300 more gives 80% for ABC analysis.

### In the news
See news box. NumPy 2.5.0 (Jun 2026) updated sorting for the array-api standard, which matters for code that needs descending sorts consistent across libraries.

### Interview angle
> [!question] How it is asked
> "Get the top 5 products by sales from arrays" or "What does `argsort` return?"

> [!tip] Strong answer includes
> - `sort` vs `argsort` and when to use indices
> - `argmax`/`argmin` return the index, not the value
> - `unique` with counts for frequency
> - `partition` for top-k efficiency

---

## 11. ⭐ Advanced: Memory, dtypes & Performance Pitfalls
> ⭐ Advanced · _Added beyond the tracker_

### Definition
- **dtype matters:** `int8` holds -128 to 127 and overflows silently; `float32` halves memory vs `float64`. NumPy 2.0 changed scalar type-promotion rules (NEP 50), so mixed scalar and array operations can give different dtypes than in 1.x.
- **Views, strides, copies:** `a.base` shows whether an array owns its data; `np.shares_memory(a, b)` checks overlap. Transpose and slices are views with different strides.
- **Memory:** `a.nbytes`; one million float64 = 8 MB.
- **Avoid temporaries:** `np.add(a, b, out=a)` or in-place `a += b`.
- **`einsum`:** compact tensor operations, e.g. `np.einsum("ij,j->i", A, v)` equals `A @ v`.
- **Masked/NaN handling:** `np.isnan`, `np.nan_to_num`, `np.ma`.
- **Beyond NumPy:** `numba` JIT, `dask` for out-of-core arrays, `cupy` for GPU, `scipy.sparse` for sparse matrices.

```python
np.array([100], dtype=np.int8) + np.int8(100)   # overflow wraps to -56
```

### Example
A 50,000 x 2,000 float64 demand matrix needs 50,000 x 2,000 x 8 bytes = 800,000,000 bytes (about 0.8 GB). Using float32 halves this to about 0.4 GB with usually negligible loss for forecasting features.

### In the news
See news box. NumPy 2.0's promotion-rule changes are the headline example of why you test numerical pipelines after upgrading.

### Interview angle
> [!question] How it is asked
> "Your script runs out of memory on a large array. What do you do?"

> [!tip] Strong answer includes
> - Check dtype and downcast; compute `nbytes`
> - Chunk or use memory-mapped files (`np.memmap`) or dask
> - Avoid unnecessary copies; in-place ops
> - Sparse structures when most entries are zero

---

## 12. ⭐ Advanced: Monte Carlo & Matrix Methods for Operations
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Applied NumPy patterns that show up in ops and consulting case work.

- **Monte Carlo inventory simulation:** draw demand and lead time from distributions, compute service level and cost across thousands of runs.
- **Markov chains:** transition matrix $P$; steady state $\pi$ solves $\pi P = \pi$ (eigenvector of $P^T$ for eigenvalue 1).
- **Linear regression via normal equations:** $\hat\beta = (X^TX)^{-1}X^Ty$, or `np.linalg.lstsq`.
- **Weighted averages / scoring models:** `np.dot(weights, scores)` for vendor selection.
- **Distance matrices** for routing heuristics with broadcasting: `np.sqrt(((P[:,None,:]-P[None,:,:])**2).sum(-1))`.

```python
P = np.array([[0.9, 0.1], [0.5, 0.5]])
w, v = np.linalg.eig(P.T)
pi = v[:, np.argmax(w.real)].real; pi = pi / pi.sum()   # [0.8333 0.1667]
```

### Example
Customer states (Active, Lapsed) with P above: steady state solves pi1 = 0.9 pi1 + 0.5 pi2 with pi1 + pi2 = 1, so 0.1 pi1 = 0.5 pi2, pi1 = 5 pi2, giving pi = (5/6, 1/6) = (0.833, 0.167). About 83% of customers are active in the long run.

### In the news
See news box. As NumPy continues to be the base of the scientific stack (2.x releases every six months), simulation code written today stays portable.

### Interview angle
> [!question] How it is asked
> "How would you estimate the probability of a stock-out under uncertain demand and lead time?"

> [!tip] Strong answer includes
> - Model inputs as distributions, simulate 10,000+ runs
> - Report the metric (service level, expected shortage) with a confidence band
> - Cross-check against an analytical result where available
> - Fix a seed and document assumptions

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
