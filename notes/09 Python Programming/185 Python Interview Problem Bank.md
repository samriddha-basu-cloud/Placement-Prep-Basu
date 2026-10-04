---
tags: [python-programming, tier1]
area: Python Programming
topic: "Python Interview Problem Bank"
tier: Tier 1
roles: Analytics / Operations / PM
status: complete
subtopics: 12
---
# Python Interview Problem Bank

⬅ [[184 Python OOP, Modules & Project Structure]] · [[_Index - Python Programming|Python Programming]] · [[186 Python Data Cleaning & EDA Playbook]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** Analytics / Operations / PM

## Sub-topics in this note
1. [[#1. How Coding Rounds Work & Complexity Cheat-Sheet]]
2. [[#2. Strings]]
3. [[#3. Lists, Dicts & Sets]]
4. [[#4. Two-Pointer & Sliding Window]]
5. [[#5. Sorting, Searching & Heaps]]
6. [[#6. Recursion & Dynamic Programming]]
7. [[#7. Pandas: GroupBy, Merge & Filter]]
8. [[#8. Pandas: Window Equivalents, Pivot & Cleaning]]
9. [[#9. Ops-Flavoured Functions]]
10. [[#10. Simulation & Performance]]
11. [[#11. Common Mistakes & Python Puzzlers]]
12. [[#12. ⭐ Advanced: Streaming, Generators & Windows Without Loading Everything]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): pandas 3.0 and Python 3.15 change what "correct" looks like in a coding round
> **pandas 3.0.0 (21 January 2026).** The release notes list a dedicated `str` dtype inferred by default for text columns (replacing `object`; missing values stay `NaN`), Copy-on-Write semantics under which chained assignment never works and `SettingWithCopyWarning` is removed, a new `pd.col()` expression syntax for `assign`, `left_anti` and `right_anti` join types in `merge()`, and a minimum of Python 3.11. Candidates who still write `df[mask]["col"] = x` will now get silently wrong code. ([pandas 3.0.0 release notes](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html), [pandas 3.0 blog](https://pandas.pydata.org/community/blog/pandas-3.0.html))
>
> **Python 3.15 release candidate (2 October 2026).** python.org lists 3.15.0rc3 as the final release candidate, with the final release scheduled for 9 October 2026 after a one-week slip for lazy-import fixes; headline features are explicit lazy imports (PEP 810), `frozendict` and `sentinel` built-ins, unpacking in comprehensions, and UTF-8 as the default encoding. Checked 4 October 2026. ([python.org](https://www.python.org/downloads/latest/python3.15/)) Python 3.14 (7 October 2025) made deferred annotation evaluation the default. ([What's New in 3.14](https://docs.python.org/3/whatsnew/3.14.html))
>
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. How Coding Rounds Work & Complexity Cheat-Sheet
> 🔴 Tier 1 · _Key points:_ 6-step routine, Big-O of Python structures, what interviewers score

### Definition
Analytics, operations and PM-tech rounds rarely ask hard algorithms; they ask **small, clean problems** (string/list/dict manipulation, a pandas transformation, an ops formula as a function) and watch how you work. A reliable routine: (1) restate and ask about edge cases (empty input, duplicates, negatives, NaN, types); (2) give a tiny example; (3) state the brute force and its cost; (4) improve with the right structure (dict, set, sort, two pointers, heap); (5) code cleanly with good names; (6) test with 2-3 cases and state time and space complexity.

| Operation | Cost | Note |
|---|---|---|
| `list[i]`, `list.append(x)` | O(1) (append amortised) | `insert(0, x)`, `pop(0)` are O(n); use `deque` |
| `x in list`, `list.index(x)` | O(n) | the commonest hidden slowdown |
| `x in set`, `d[key]`, `d[key] = v` | O(1) average | keys must be hashable |
| `sorted(a)`, `a.sort()` | O(n log n) | stable; `key=` for custom order |
| `heapq.heappush/heappop` | O(log n) | `nlargest(k, a)` is O(n log k) |
| `bisect` on sorted list | O(log n) | insertion into a list is still O(n) |
| `"".join(parts)` | O(total length) | repeated `s += x` can be quadratic |
| pandas `groupby`, `merge` (hash) | O(n) to O(n + m) | vectorised; avoid `iterrows`/`apply(axis=1)` on big data |

### Example
Two-sum on 100,000 numbers: nested loops check about $n^2/2 = 5\times10^9$ pairs; a dict of seen values does 100,000 lookups. The code for this is problem P7 below. Everything in this note was executed; the assertions after each solution are its test cases.

### In the news
See news box. pandas 3.0 and Python 3.15 are current, so show modern idioms (`.loc` assignment, `str` dtype, `X | None` hints) rather than patterns that newer versions break.

### Interview angle
> [!question] How it is asked
> "Solve this on a shared screen and talk me through your thinking."

> [!tip] Strong answer includes
> - Clarifying questions and edge cases before typing
> - Brute force first, then the optimisation with complexity stated in Big-O
> - Readable names, small functions, tests on edge cases (empty, one element, duplicates)
> - Using built-ins well (`Counter`, `defaultdict`, `sorted(key=)`, `heapq`) rather than reinventing them
> - Language basics in [[062 Python Fundamentals]] and class design in [[184 Python OOP, Modules & Project Structure]]

---
## 2. Strings
> 🔴 Tier 1 · _Key points:_ P1-P6: reverse words, palindrome, anagram, first unique, run-length, brackets

### Definition
String problems test indexing, hashing characters (`Counter`), two pointers and stacks. Strings are immutable in Python; build results with lists and `"".join`.

```python
from collections import Counter
from itertools import groupby

# P1  Reverse the words in a sentence (collapse extra spaces)
def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])
assert reverse_words("  ship   from Nashik  ") == "Nashik from ship"

# P2  Palindrome ignoring case and non-alphanumerics (two pointers, O(n) time, O(1) extra)
def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i, j = i + 1, j - 1
    return True
assert is_palindrome("A man, a plan, a canal: Panama") and not is_palindrome("SKU-101")

# P3  Are two strings anagrams? (Counter equality, O(n))
def is_anagram(a: str, b: str) -> bool:
    return Counter(a.lower()) == Counter(b.lower())
assert is_anagram("Listen", "Silent") and not is_anagram("abc", "abd")

# P4  First non-repeating character (index), -1 if none
def first_unique(s: str) -> int:
    c = Counter(s)
    return next((i for i, ch in enumerate(s) if c[ch] == 1), -1)
assert first_unique("leetcode") == 0 and first_unique("aabb") == -1 and first_unique("loveleetcode") == 2

# P5  Run-length encode: "aaabbc" -> "a3b2c1"
def rle(s: str) -> str:
    return "".join(f"{k}{len(list(g))}" for k, g in groupby(s))
assert rle("aaabbc") == "a3b2c1" and rle("") == ""

# P6  Balanced brackets using a stack
def balanced(s: str) -> bool:
    pairs, stack = {")": "(", "]": "[", "}": "{"}, []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
assert balanced("{[()]}") and not balanced("([)]") and not balanced("((")
print("strings ok")
```

### Example
`rle("aaabbc")` returns `a3b2c1`; `first_unique("loveleetcode")` returns 2 (the letter `v`); `balanced("([)]")` is `False` because `)` meets `[` on the stack. Complexities: P1 O(n); P2 O(n) time, O(1) space; P3 and P4 O(n) with O(k) space for k distinct characters; P5 O(n); P6 O(n) time, O(n) stack.

### In the news
See news box. Python 3.15 makes UTF-8 the default text encoding, which removes a class of "wrong characters when reading a CSV on Windows" bugs, but still pass `encoding=` explicitly in interview code.

### Interview angle
> [!question] How it is asked
> "Check whether a string is a valid sequence of brackets." or "Find the first non-repeating character."

> [!tip] Strong answer includes
> - Stack for matching problems; `Counter` for frequency problems
> - Two-pointer palindrome without building a reversed copy
> - Mention case, spaces, punctuation and Unicode
> - Complexity in time and space

---
## 3. Lists, Dicts & Sets
> 🔴 Tier 1 · _Key points:_ P7-P12: two-sum, top-k, group anagrams, dedupe, merge intervals, flatten

### Definition
Dicts and sets turn "search the list again" into one pass. `Counter` counts, `defaultdict(list)` groups, `dict.fromkeys(seq)` de-duplicates while keeping order (dicts keep insertion order), and sorting first often simplifies interval and ordering problems.

```python
from collections import Counter, defaultdict

# P7  Two-sum: indices of two numbers adding to target (hash map, O(n))
def two_sum(nums, target):
    seen = {}
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
assert two_sum([2, 7, 11, 15], 9) == [0, 1] and two_sum([3, 2, 4], 6) == [1, 2]

# P8  k most frequent SKUs in an order log
def top_k(items, k):
    return [x for x, _ in Counter(items).most_common(k)]
log = ["A", "B", "A", "C", "B", "A", "D", "B", "A"]
assert top_k(log, 2) == ["A", "B"]

# P9  Group words that are anagrams of each other
def group_anagrams(words):
    d = defaultdict(list)
    for w in words:
        d["".join(sorted(w))].append(w)
    return list(d.values())
assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

# P10 Remove duplicates but keep first-seen order
def dedupe(seq):
    return list(dict.fromkeys(seq))
assert dedupe(["S2", "S1", "S2", "S3", "S1"]) == ["S2", "S1", "S3"]

# P11 Merge overlapping intervals (sort, then sweep), O(n log n)
def merge_intervals(iv):
    out = []
    for s, e in sorted(iv):
        if out and s <= out[-1][1]:
            out[-1][1] = max(out[-1][1], e)
        else:
            out.append([s, e])
    return out
assert merge_intervals([(8, 10), (1, 3), (2, 6), (15, 18), (17, 20)]) == [[1, 6], [8, 10], [15, 20]]

# P12 Flatten an arbitrarily nested list
def flatten(x):
    for el in x:
        if isinstance(el, list):
            yield from flatten(el)
        else:
            yield el
assert list(flatten([1, [2, [3, 4]], 5])) == [1, 2, 3, 4, 5]
print("lists/dicts ok")
```

### Example
`merge_intervals` on `[(8,10),(1,3),(2,6),(15,18),(17,20)]` sorts to `(1,3),(2,6),(8,10),(15,18),(17,20)` and returns `[[1,6],[8,10],[15,20]]`: the same logic merges overlapping machine-booking or shift slots. `top_k(log, 2)` on nine order lines returns `["A", "B"]` (A appears 4 times, B 3 times).

### In the news
See news box. In pandas the same grouping is `df.groupby(...)`, and the new `left_anti` join answers "which keys are missing" without the `isin` workaround.

### Interview angle
> [!question] How it is asked
> "Given a list of transactions, find two that sum to a target." or "Merge overlapping delivery windows."

> [!tip] Strong answer includes
> - Hash map for O(n) lookups; say what you store (value to index)
> - Sort-then-sweep for intervals; sort key correctness
> - Order preservation (`dict.fromkeys`) and stability
> - Why `x in list` inside a loop is O(n^2)

---
## 4. Two-Pointer & Sliding Window
> 🔴 Tier 1 · _Key points:_ P13-P18: sorted two-sum, in-place dedupe, move zeroes, windows, Kadane

### Definition
**Two pointers** scan a sorted array from both ends or use a read/write pair to modify in place in O(n) time and O(1) space. A **sliding window** keeps a running summary of a contiguous range: fixed length k (add the new element, drop the old) or variable length (grow the right edge, shrink the left when a rule breaks). **Kadane's algorithm** keeps the best sum ending here: $cur = \max(x, cur + x)$.

```python
# P13 Sorted array two-sum with two pointers (O(n), O(1) space)
def two_sum_sorted(a, target):
    i, j = 0, len(a) - 1
    while i < j:
        s = a[i] + a[j]
        if s == target:
            return [i, j]
        i, j = (i + 1, j) if s < target else (i, j - 1)
    return []
assert two_sum_sorted([1, 3, 4, 6, 9], 10) == [0, 4] and two_sum_sorted([1, 2], 9) == []

# P14 In-place de-duplication of a sorted list; return the new length
def dedupe_sorted(a):
    if not a:
        return 0
    w = 1
    for r in range(1, len(a)):
        if a[r] != a[w - 1]:
            a[w] = a[r]
            w += 1
    return w
arr = [1, 1, 2, 2, 2, 3]
n = dedupe_sorted(arr)
assert n == 3 and arr[:n] == [1, 2, 3]

# P15 Move zeroes to the end, keeping order, in place
def move_zeroes(a):
    w = 0
    for r in range(len(a)):
        if a[r] != 0:
            a[w], a[r] = a[r], a[w]
            w += 1
    return a
assert move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]

# P16 Highest total demand in any k consecutive days (fixed sliding window)
def best_window(a, k):
    cur = best = sum(a[:k])
    for i in range(k, len(a)):
        cur += a[i] - a[i - k]
        best = max(best, cur)
    return best
assert best_window([5, 2, 9, 1, 7, 3, 8], 3) == 18        # 7 + 3 + 8

# P17 Longest substring without repeating characters (variable window, O(n))
def longest_unique(s):
    last, start, best = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        best = max(best, i - start + 1)
    return best
assert longest_unique("abcabcbb") == 3 and longest_unique("bbbb") == 1 and longest_unique("") == 0

# P18 Maximum subarray sum (Kadane): best consecutive stretch of net cash flow
def max_subarray(a):
    cur = best = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6 and max_subarray([-3, -1, -2]) == -1
print("two-pointer ok")
```

### Example
Daily demand `[5, 2, 9, 1, 7, 3, 8]`, best 3-day window: sums are 16, 12, 17, 11, 18, so the answer is 18 (days 5-7: 7 + 3 + 8). Kadane on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]` returns 6 from the stretch `4, -1, 2, 1`: the best consecutive run of net cash flow.

### In the news
See news box. NumPy and pandas replace many windows with `rolling(k).sum()`; interviewers still ask for the manual version to test reasoning.

### Interview angle
> [!question] How it is asked
> "Find the maximum total sales in any 7 consecutive days." or "Longest stretch with no repeated SKU."

> [!tip] Strong answer includes
> - Recognise the pattern (sorted input, contiguous range, in place) and name it
> - Update the window in O(1) instead of re-summing
> - State O(n) time and O(1) space, plus edge cases such as k larger than the array and all-negative input
> - Cross-check with a brute force on a small case

---
## 5. Sorting, Searching & Heaps
> 🔴 Tier 1 · _Key points:_ P19-P23: multi-key sort, binary search, bisect, k-th largest, merge sorted

### Definition
`sorted(iterable, key=..., reverse=...)` is stable and O(n log n); negate numeric keys to sort descending on one field and ascending on another. **Binary search** needs sorted data and runs in O(log n); `bisect` gives the insertion point and is the clean way to look up slabs, tax brackets and price breaks. A **heap** (`heapq`) returns the smallest item in O(log n), so k-th largest costs O(n log k) with a size-k min-heap.

```python
import bisect, heapq

# P19 Sort orders by value descending, ties by customer name ascending
orders = [("Tata", 500), ("Bajaj", 900), ("Mahindra", 500), ("Ashok", 900)]
assert sorted(orders, key=lambda o: (-o[1], o[0])) == [("Ashok", 900), ("Bajaj", 900), ("Mahindra", 500), ("Tata", 500)]

# P20 Binary search (iterative), and the bisect version used for price slabs
def binary_search(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == x:
            return mid
        lo, hi = (mid + 1, hi) if a[mid] < x else (lo, mid - 1)
    return -1
assert binary_search([1, 3, 5, 7, 9], 7) == 3 and binary_search([1, 3], 4) == -1

slab_starts = [0, 100, 500, 1000]          # quantity breaks
slab_price  = [50, 47, 44, 40]             # Rs per unit
def unit_price(qty):
    return slab_price[bisect.bisect_right(slab_starts, qty) - 1]
assert [unit_price(q) for q in (99, 100, 499, 500, 5000)] == [50, 47, 47, 44, 40]

# P21 k-th largest element: min-heap of size k, O(n log k)
def kth_largest(a, k):
    h = a[:k]
    heapq.heapify(h)
    for x in a[k:]:
        if x > h[0]:
            heapq.heapreplace(h, x)
    return h[0]
assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5 and heapq.nlargest(3, [3, 2, 1, 5, 6, 4]) == [6, 5, 4]

# P22 Merge two sorted lists in O(n + m)
def merge_sorted(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    return out + a[i:] + b[j:]
assert merge_sorted([1, 4, 9], [2, 3, 10, 11]) == [1, 2, 3, 4, 9, 10, 11] == list(heapq.merge([1, 4, 9], [2, 3, 10, 11]))

# P23 Top 3 suppliers by spend from a dict
spend = {"S1": 120, "S2": 340, "S3": 90, "S4": 340, "S5": 10}
top3 = sorted(spend.items(), key=lambda kv: (-kv[1], kv[0]))[:3]
assert top3 == [("S2", 340), ("S4", 340), ("S1", 120)]
print("sorting ok")
```

### Example
Price slabs: breaks at 0, 100, 500, 1,000 units with prices ₹50, 47, 44, 40. `bisect_right(starts, qty) - 1` maps quantity 99 to ₹50, 100 and 499 to ₹47, 500 to ₹44 and 5,000 to ₹40. In SQL terms this is a range lookup; in Excel it is approximate-match `XLOOKUP` (see [[187 Excel Interview Problem Bank & Case Exercises]]).

### In the news
See news box. `sorted()` and `heapq` are built in and unchanged across 3.14 and 3.15, which is why these remain safe interview defaults.

### Interview angle
> [!question] How it is asked
> "Return the top 3 suppliers by spend, breaking ties alphabetically." or "Find the discount slab for a quantity."

> [!tip] Strong answer includes
> - Multi-key sort via a tuple key and negation
> - Binary search invariants (`lo`, `hi`, mid) and off-by-one care; mention `bisect_left` vs `bisect_right`
> - Heap for top-k when n is large and k is small; `nlargest` as the one-liner
> - Stability of Python's sort

---
## 6. Recursion & Dynamic Programming
> 🔴 Tier 1 · _Key points:_ P24-P28: memoised Fibonacci, subsets, coin change, knapsack, grid paths

### Definition
**Recursion** solves a problem through smaller copies of itself and needs a base case. When sub-problems repeat, **memoise** (`functools.lru_cache`) or build a table bottom-up: **dynamic programming**. Recipe: define the state (what the table index means), the recurrence, the base cases and the order of filling. Python's default recursion limit is about 1,000 frames, so deep recursion needs an iterative version.

```python
from functools import lru_cache
from itertools import combinations

# P24 Fibonacci: memoised recursion vs iterative
@lru_cache(maxsize=None)
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
assert fib(50) == fib_iter(50) == 12586269025

# P25 All subsets (power set) by recursion, and permutations via itertools
def subsets(a):
    if not a:
        return [[]]
    rest = subsets(a[1:])
    return rest + [a[:1] + r for r in rest]
assert len(subsets([1, 2, 3])) == 8 and sorted(subsets([1, 2])) == [[], [1], [1, 2], [2]]
from itertools import permutations
assert len(list(permutations("ABC"))) == 6 and len(list(combinations(range(5), 2))) == 10

# P26 Fewest cartons to make an exact count (coin-change DP, O(amount * len(sizes)))
def min_cartons(sizes, amount):
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for s in sizes:
            if s <= a and dp[a - s] + 1 < dp[a]:
                dp[a] = dp[a - s] + 1
    return -1 if dp[amount] == INF else dp[amount]
assert min_cartons([1, 5, 6, 9], 11) == 2          # 5 + 6; greedy 9+1+1 would use 3
assert min_cartons([5, 10], 3) == -1

# P27 0/1 knapsack: best total benefit of projects within a budget
def knapsack(costs, benefits, budget):
    dp = [0] * (budget + 1)
    for c, b in zip(costs, benefits):
        for w in range(budget, c - 1, -1):         # backwards so each project is used once
            dp[w] = max(dp[w], dp[w - c] + b)
    return dp[budget]
assert knapsack([10, 20, 30], [60, 100, 120], 50) == 220

# P28 Count the monotone paths in an r x c grid (DP) = C(r+c-2, r-1)
def grid_paths(r, c):
    dp = [1] * c
    for _ in range(1, r):
        for j in range(1, c):
            dp[j] += dp[j - 1]
    return dp[-1]
from math import comb
assert grid_paths(3, 7) == 28 == comb(8, 2)
print("recursion/dp ok")
```

### Example
Cartons of 1, 5, 6 and 9 units to pack exactly 11 units: greedy takes 9 + 1 + 1 = 3 cartons, DP finds 5 + 6 = 2 cartons. Knapsack with costs 10, 20, 30, benefits 60, 100, 120 and budget 50 selects the 20 and 30 projects for a benefit of 220 (not the first two, 160). The grid count for 3 x 7 is $\binom{8}{2}=28$. Budget-constrained project selection links to [[146 Operations Research - Linear Programming]] and integer programming in [[148 Operations Research - Network Models & Integer Programming]].

### In the news
See news box. Python 3.14 and 3.15 keep `functools.cache` and `lru_cache` unchanged; the free-threaded build is the one place caching behaviour under threads deserves a mention.

### Interview angle
> [!question] How it is asked
> "Compute the minimum number of pack sizes to ship exactly N units." or "Pick projects to maximise benefit within a budget."

> [!tip] Strong answer includes
> - Show why greedy fails with a counter-example
> - State the DP state, recurrence and base case before coding
> - Complexity: coin change O(amount x sizes), knapsack O(n x budget)
> - Iterate the budget backwards in 0/1 knapsack so each item is used once

---
## 7. Pandas: GroupBy, Merge & Filter
> 🔴 Tier 1 · _Key points:_ P29-P32: named aggregation, top-N per group, left join checks, groupby.filter

### Definition
The pandas questions that recur: aggregate by a key (`groupby().agg(name=(col, func))`), top-N per group (sort, then `groupby().head(n)`), joins that must not change row counts (`merge(..., how="left", indicator=True)` plus a length assertion) and group-level filters (`groupby().filter`). Chained assignment (`df[mask]["x"] = v`) is not allowed in pandas 3.0; use `df.loc[mask, "x"] = v`. See [[064 Pandas — Data Manipulation]] for the full tour. The practice data used in sub-topics 7 and 8:

```python
import pandas as pd
import numpy as np

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "customer": ["Tata", "Bajaj", "Tata", "Mahindra", "Bajaj", "Tata", "Ashok", "Mahindra", "Bajaj", "Tata"],
    "region":   ["West", "West", "West", "West", "North", "North", "South", "South", "North", "West"],
    "month":    ["2026-01", "2026-01", "2026-02", "2026-02", "2026-01", "2026-02", "2026-01", "2026-03", "2026-03", "2026-03"],
    "qty":      [10, 4, 6, 8, 5, 7, 3, 9, 6, 12],
    "amount":   [5000, 2400, 3300, 4800, 2750, 3850, 1800, 5400, 3300, 6600],
})
customers = pd.DataFrame({"customer": ["Tata", "Bajaj", "Mahindra", "Eicher"], "tier": ["A", "B", "A", "C"]})

# P29 Revenue, order count and distinct customers per region (named aggregation)
g = orders.groupby("region").agg(revenue=("amount", "sum"), orders=("order_id", "count"),
                                 customers=("customer", "nunique")).sort_values("revenue", ascending=False)
assert g.loc["West", "revenue"] == 22100 and g.loc["South", "customers"] == 2

# P30 Top 2 orders by amount in each region
top2 = (orders.sort_values("amount", ascending=False).groupby("region").head(2)
        .sort_values(["region", "amount"], ascending=[True, False]))
assert top2.query("region == 'West'")["order_id"].tolist() == [10, 1]

# P31 Left join to the customer master and list customers with no master record
m = orders.merge(customers, on="customer", how="left", indicator=True)
unmatched = m.loc[m["_merge"] == "left_only", "customer"].unique().tolist()
assert unmatched == ["Ashok"] and len(m) == len(orders)           # left join must not multiply rows
anti = orders.merge(customers, on="customer", how="left_anti")      # pandas 3.0+: rows with no match, in one step
assert anti["customer"].tolist() == ["Ashok"]
never_ordered = customers[~customers["customer"].isin(orders["customer"])]["customer"].tolist()
assert never_ordered == ["Eicher"]

# P32 Customers with more than 1 order AND total spend above 9,000 (groupby.filter)
big = orders.groupby("customer").filter(lambda d: len(d) > 1 and d["amount"].sum() > 9000)
assert sorted(big["customer"].unique()) == ["Mahindra", "Tata"]      # Bajaj: 8,450 total
```

### Example
Revenue by region on the sample data: West ₹22,100 (5 orders, 3 customers), North ₹9,900 (3, 2), South ₹7,200 (2, 2); total ₹39,200. Top-2 West orders are 10 (₹6,600) and 1 (₹5,000). Ashok has orders but no master record (found by both `indicator=True` and `left_anti`); Eicher is in the master but never ordered. Only Tata (₹18,750) and Mahindra (₹10,200) have more than one order and spend above ₹9,000; Bajaj has 3 orders but only ₹8,450.

### In the news
See news box. `left_anti` in pandas 3.0 replaces the `indicator` plus filter recipe for "rows with no match", and Copy-on-Write guarantees that filtered frames never silently modify the original.

### Interview angle
> [!question] How it is asked
> "Show the top 2 orders per region." or "After the merge there are more rows than before. Why?"

> [!tip] Strong answer includes
> - Named aggregation and `as_index=False` or `reset_index` for flat output
> - Join-key uniqueness check (duplicates in the right table multiply rows); `validate="m:1"` in `merge`
> - Anti-join patterns and `indicator`
> - Awareness of pandas 3.0 (Copy-on-Write, `str` dtype)

---
## 8. Pandas: Window Equivalents, Pivot & Cleaning
> 🔴 Tier 1 · _Key points:_ P33-P38: cumsum, shift, rank, transform, pct_change, pivot_table, melt, drop_duplicates

### Definition
SQL window functions ([[058 Window Functions]]) map to pandas as follows: `SUM() OVER (PARTITION BY k ORDER BY t)` is `groupby(k)[col].cumsum()`; `LAG` is `groupby(k)[col].shift(1)`; `RANK` is `groupby(k)[col].rank(method="min")`; `SUM() OVER (PARTITION BY k)` without ordering is `groupby(k)[col].transform("sum")`; moving average is `rolling(k).mean()`. `pivot_table` reshapes long to wide (with `margins` for totals); `melt` goes back. `drop_duplicates(keep="last")` after sorting keeps the latest record.

```python
# P33 SQL window-function equivalents on the orders table (sorted by order_id within customer)
o = orders.sort_values(["customer", "order_id"]).copy()
o["running_total"] = o.groupby("customer")["amount"].cumsum()               # SUM() OVER (PARTITION BY ... ORDER BY ...)
o["prev_amount"]   = o.groupby("customer")["amount"].shift(1)               # LAG(amount, 1)
o["rank_in_cust"]  = o.groupby("customer")["amount"].rank(ascending=False, method="min")   # RANK()
o["share_of_cust"] = o["amount"] / o.groupby("customer")["amount"].transform("sum")         # amount / SUM() OVER (PARTITION BY)
tata = o[o["customer"] == "Tata"]
assert tata["running_total"].tolist() == [5000, 8300, 12150, 18750]
assert np.isnan(tata["prev_amount"].iloc[0]) and tata["prev_amount"].iloc[1] == 5000
assert tata["rank_in_cust"].tolist() == [2, 4, 3, 1]
assert round(tata["share_of_cust"].iloc[0], 4) == 0.2667

# P34 Month-over-month growth of total revenue, and a 2-month rolling mean
monthly = orders.groupby("month")["amount"].sum()
growth = monthly.pct_change().round(4)
assert monthly.tolist() == [11950, 11950, 15300] and growth.tolist()[1:] == [0.0, 0.2803]
roll = monthly.rolling(2).mean()
assert roll.tolist()[1:] == [11950.0, 13625.0]

# P35 Pivot: customers as rows, months as columns, sum of amount, with totals; and back with melt
pv = orders.pivot_table(index="customer", columns="month", values="amount", aggfunc="sum",
                        fill_value=0, margins=True, margins_name="Total")
assert pv.loc["Tata", "Total"] == 18750 and pv.loc["Total", "Total"] == 39200
long = pv.drop(index="Total", columns="Total").reset_index().melt(id_vars="customer", var_name="month", value_name="amount")
assert len(long) == 4 * 3 and long["amount"].sum() == 39200

# P36 Keep the most recent record per key (typical master-data clean-up)
raw = pd.DataFrame({"sku": ["A", "B", "A", "C", "B"], "price": [10, 20, 12, 30, 22],
                    "updated": pd.to_datetime(["2026-01-01", "2026-01-05", "2026-02-01", "2026-01-09", "2026-03-01"])})
latest = raw.sort_values("updated").drop_duplicates("sku", keep="last").sort_values("sku")
assert latest["price"].tolist() == [12, 22, 30]

# P37 Fill missing lead times with the median of the supplier's own history (group-wise imputation)
lt = pd.DataFrame({"supplier": ["S1", "S1", "S1", "S2", "S2"], "lead_days": [5, np.nan, 7, 10, np.nan]})
lt["lead_days"] = lt["lead_days"].fillna(lt.groupby("supplier")["lead_days"].transform("median"))
assert lt["lead_days"].tolist() == [5.0, 6.0, 7.0, 10.0, 10.0]

# P38 Share of revenue and cumulative share by region, in one chain
reg = (orders.groupby("region", as_index=False)["amount"].sum().sort_values("amount", ascending=False)
       .assign(share=lambda d: d["amount"] / d["amount"].sum()).assign(cum_share=lambda d: d["share"].cumsum()))
assert reg["region"].tolist() == ["West", "North", "South"] and round(reg["cum_share"].iloc[1], 3) == 0.816
```

### Example
Tata's four orders (₹5,000, 3,300, 3,850, 6,600) give running totals 5,000, 8,300, 12,150, 18,750; the first order is ranked 2 by amount and is 5,000/18,750 = 26.67% of Tata's spend. Monthly revenue is ₹11,950, 11,950, 15,300, so month-on-month growth is 0% then +28.03%, and the 2-month rolling mean is 11,950 then 13,625. Region shares are 56.4%, 25.3%, 18.4% (cumulative 56.4%, 81.6%, 100%). The same ideas power the SQL set in [[181 SQL Interview Problem Bank]].

### In the news
See news box. pandas 3.0 adds `pd.col()` for `assign`, so a column calculation can be written `df.assign(total=pd.col("qty") * pd.col("price"))` instead of a lambda.

### Interview angle
> [!question] How it is asked
> "Give me each customer's running total and previous order amount." or "Keep only the latest price per SKU."

> [!tip] Strong answer includes
> - The SQL-to-pandas mapping above, including `transform` vs `agg` (same length vs one row per group)
> - Sorting before `cumsum`, `shift` and `drop_duplicates`
> - `pivot_table` parameters (`index`, `columns`, `values`, `aggfunc`, `fill_value`, `margins`)
> - Group-wise imputation instead of one global mean

---
## 9. Ops-Flavoured Functions
> 🔴 Tier 1 · _Key points:_ P39-P46: EOQ, safety stock, ROP, ABC, fill rate, OEE, newsvendor, FIFO, smoothing

### Definition
Operations interviews turn textbook formulas into functions. Keep formulas explicit and testable. $EOQ=\sqrt{2DS/H}$; $SS=z\,\sigma_d\sqrt{L}$; $ROP=\bar d L+SS$; $OEE=A\times P\times Q$; newsvendor critical ratio $CR=C_u/(C_u+C_o)$ and $Q^*=\mu+z_{CR}\sigma$; simple exponential smoothing $F_{t+1}=\alpha A_t+(1-\alpha)F_t$; $MAPE=\frac1n\sum|A_t-F_t|/A_t$. Theory is in [[003 Inventory Management]], [[018 Capacity Management & OEE]], [[012 Supply Chain Analytics & KPIs]] and [[066 Demand Forecasting & Time Series]].

```python
from math import sqrt
from statistics import NormalDist
from collections import deque
import pandas as pd

# P39 EOQ and total annual cost at a given order quantity
def eoq(D, S, H):
    return sqrt(2 * D * S / H)
def annual_cost(D, S, H, Q, price=0.0):
    return D / Q * S + Q / 2 * H + D * price
D, S, H = 12000, 500, 50                      # units/year, Rs/order, Rs/unit/year
q = eoq(D, S, H)
assert round(q, 1) == 489.9
assert round(annual_cost(D, S, H, q)) == 24495 and annual_cost(D, S, H, 1000) == 31000

# P40 Safety stock and reorder point for a service level
def safety_stock(z_or_sl, sigma_d, L):
    z = NormalDist().inv_cdf(z_or_sl) if z_or_sl < 1 else z_or_sl
    return z * sigma_d * sqrt(L)
def reorder_point(d_bar, L, sigma_d, sl):
    return d_bar * L + safety_stock(sl, sigma_d, L)
assert round(safety_stock(0.95, 6, 7), 1) == 26.1
assert round(reorder_point(12000 / 365, 7, 6, 0.95), 1) == 256.2

# P41 ABC classification: A = items making the first 80% of value, B = next 15%, C = last 5%
sku = pd.DataFrame({"sku": list("ABCDEFGH"), "value": [500, 300, 90, 40, 30, 20, 12, 8]})
sku = sku.sort_values("value", ascending=False)
sku["cum_share"] = sku["value"].cumsum() / sku["value"].sum()
sku["class"] = pd.cut(sku["cum_share"].round(6), [0, 0.80, 0.95, 1.0], labels=["A", "B", "C"])
assert sku["cum_share"].round(2).tolist() == [0.5, 0.8, 0.89, 0.93, 0.96, 0.98, 0.99, 1.0]
assert sku["class"].tolist() == ["A", "A", "B", "B", "C", "C", "C", "C"]

# P42 Fill rate vs cycle service level from simulated demand and a stock level
demand = [90, 120, 100, 150, 80, 110, 130, 95]
stock = 110
cycle_sl = sum(d <= stock for d in demand) / len(demand)          # share of cycles with no stockout
fill_rate = 1 - sum(max(d - stock, 0) for d in demand) / sum(demand)   # share of units served
assert cycle_sl == 0.625 and round(fill_rate, 4) == 0.92

# P43 OEE = Availability x Performance x Quality
def oee(planned_min, downtime_min, ideal_cycle_min, total_units, good_units):
    run = planned_min - downtime_min
    a = run / planned_min
    p = ideal_cycle_min * total_units / run
    q = good_units / total_units
    return a, p, q, a * p * q
a, p, q_, o = oee(480, 60, 0.5, 700, 665)
assert round(a, 4) == 0.875 and round(p, 4) == 0.8333 and q_ == 0.95 and round(o, 4) == 0.6927

# P44 Newsvendor: optimal order quantity for normal demand
def newsvendor(mu, sigma, price, cost, salvage):
    cu, co = price - cost, cost - salvage
    cr = cu / (cu + co)
    return cr, mu + NormalDist().inv_cdf(cr) * sigma
cr, qopt = newsvendor(mu=200, sigma=40, price=100, cost=60, salvage=20)
assert cr == 0.5 and qopt == 200
cr2, q2 = newsvendor(200, 40, 100, 40, 20)
assert round(cr2, 4) == 0.7500 and round(q2, 1) == 227.0

# P45 FIFO issue from batches (oldest first): return the cost of goods issued
def fifo_issue(batches, qty):
    """batches: deque of [qty, unit_cost], oldest on the left. Mutates batches."""
    cost = 0.0
    while qty > 0:
        if not batches:
            raise ValueError("insufficient stock")
        b = batches[0]
        take = min(qty, b[0])
        cost += take * b[1]
        b[0] -= take
        qty -= take
        if b[0] == 0:
            batches.popleft()
    return cost
bt = deque([[100, 10.0], [200, 12.0], [150, 15.0]])
assert fifo_issue(bt, 250) == 100 * 10 + 150 * 12 and list(bt) == [[50, 12.0], [150, 15.0]]

# P46 Simple exponential smoothing forecast and MAPE
def ses(series, alpha):
    f = [series[0]]
    for x in series[:-1]:
        f.append(alpha * x + (1 - alpha) * f[-1])
    return f                                   # f[t] is the forecast for period t
def mape(actual, forecast):
    return sum(abs(a - f) / a for a, f in zip(actual, forecast)) / len(actual)
act = [100, 110, 105, 120, 115]
fc = ses(act, 0.3)
assert [round(x, 2) for x in fc] == [100, 100, 103.0, 103.6, 108.52]
assert round(mape(act[1:], fc[1:]), 4) == 0.0757
print("ops ok")
```

### Example
EOQ for D = 12,000, S = ₹500, H = ₹50: 489.9 units, annual cost ₹24,495 against ₹31,000 for lots of 1,000. Safety stock at 95% for sigma 6/day and 7-day lead time: 1.645 x 6 x 2.646 = 26.1; ROP = 230.1 + 26.1 = 256.2. ABC on eight SKUs worth 500, 300, 90, 40, 30, 20, 12, 8: cumulative shares 50, 80, 89, 93, 96, 98, 99, 100% give A = {A, B}, B = {C, D}, C = the rest (a boundary item is assigned by its cumulative share; state your convention). With stock 110 against the eight demands, cycle service level is 5/8 = 62.5% but fill rate is 1 - 70/875 = 92%. OEE: availability 420/480 = 87.5%, performance 0.5 x 700/420 = 83.3%, quality 665/700 = 95%, so OEE = 69.3%. Newsvendor: price 100, cost 40, salvage 20 gives CR = 60/80 = 0.75 and Q* = 200 + 0.6745 x 40 = 227. FIFO issue of 250 from batches 100 @ 10, 200 @ 12, 150 @ 15 costs 1,000 + 1,800 = ₹2,800. Exponential smoothing with alpha 0.3 on 100, 110, 105, 120, 115 forecasts 100, 100, 103.0, 103.6, 108.52 with MAPE 7.57% over the last four periods.

### In the news
See news box. `statistics.NormalDist` (standard library) supplies `inv_cdf` for z-values, so these functions need no SciPy.

### Interview angle
> [!question] How it is asked
> "Write a function that returns the reorder point for a SKU, given demand history and service level." or "Classify SKUs into A, B, C."

> [!tip] Strong answer includes
> - Formula stated first, then code; units consistent (daily sigma with days of lead time)
> - Sensible handling of edge cases (zero demand, service level of 1, missing history)
> - Explains cycle service level vs fill rate and why ABC cut-offs are conventions
> - Tests with a hand-checked number

---
## 10. Simulation & Performance
> 🔴 Tier 1 · _Key points:_ P47-P49: Monte Carlo stock-out probability, vectorising, set vs list

### Definition
**Monte Carlo** estimates a probability by simulating many random trials; seed the generator for reproducibility (`np.random.default_rng(seed)`). **Vectorisation** moves loops into compiled NumPy/pandas code; typical speed-ups are one to two orders of magnitude. **Data-structure choice** is the other big lever: membership tests on a `set` are O(1) on average versus O(n) on a list. When asked "how would you speed this up", measure with `timeit`, then change the algorithm or structure before reaching for parallelism.

```python
import numpy as np
import timeit

# P47 Monte Carlo: probability of a stock-out during lead time
rng = np.random.default_rng(42)
daily = rng.normal(loc=33, scale=6, size=(100_000, 7))      # 7-day lead time, demand per day
lt_demand = daily.sum(axis=1)
rop = 256
p_stockout = (lt_demand > rop).mean()
print(round(p_stockout, 3))                                  # analytic: P(Z > (256-231)/(6*sqrt(7)))
from statistics import NormalDist
analytic = 1 - NormalDist(mu=33 * 7, sigma=6 * 7 ** 0.5).cdf(rop)
assert abs(p_stockout - analytic) < 0.01
print(round(analytic, 3))

# P48 Vectorise: Loop vs NumPy for 1 million order values
vals = list(range(1_000_000))
arr = np.arange(1_000_000)
t_loop = timeit.timeit(lambda: sum(v * 1.18 for v in vals), number=3)
t_np = timeit.timeit(lambda: (arr * 1.18).sum(), number=3)
assert abs(sum(v * 1.18 for v in vals) - (arr * 1.18).sum()) < 1e-3 * (arr * 1.18).sum()
print("numpy faster:", t_np < t_loop)

# P49 Membership test: list is O(n), set is O(1) on average
ids = list(range(200_000)); idset = set(ids)
t_list = timeit.timeit(lambda: 199_999 in ids, number=200)
t_set = timeit.timeit(lambda: 199_999 in idset, number=200)
print("set faster:", t_set < t_list)
```

### Example
Lead-time demand for 7 days with mean 33 and standard deviation 6 per day is normal with mean 231 and standard deviation $6\sqrt7=15.87$. The chance it exceeds a reorder point of 256 is $P(Z>1.575)\approx5.8\%$; the 100,000-run simulation gives 5.7%. The analytic answer and the simulation agreeing is the check. The timing asserts only compare the two methods; actual speed-ups vary by machine, so quote them as measured, not as fixed numbers. More simulation recipes are in [[068 Operations-Specific Python (PuLP, SimPy)]] and [[067 Statistical Analysis in Python]].

### In the news
See news box. Python 3.15's lazy imports and improved experimental JIT target start-up and interpreter speed, but the large gains still come from vectorisation and better data structures.

### Interview angle
> [!question] How it is asked
> "How would you estimate the probability of a stock-out if demand and lead time are both random?" or "This loop over 5 million rows is slow. What do you do?"

> [!tip] Strong answer includes
> - Simulate demand over lead time, count exceedances, check against the normal approximation
> - Seed the generator and state the number of trials and its error (about $\sqrt{p(1-p)/n}$)
> - Profile first, vectorise, use `set`/`dict`, avoid `iterrows`/row-wise `apply`, read in chunks
> - Complexity language, not just "it feels faster"

---
## 11. Common Mistakes & Python Puzzlers
> 🔴 Tier 1 · _Key points:_ mutable defaults, late-binding closures, shallow copy, removal during iteration, floats

### Definition
Interviewers use short snippets to see whether you know the language's sharp edges. The usual suspects, with the behaviour shown in the comments:

```python
import copy

# 1 Mutable default argument
def add_sku(sku, bucket=[]):
    bucket.append(sku)
    return bucket
add_sku("A"); print(add_sku("B"))                          # ['A', 'B'], not ['B']

# 2 Late binding in closures
fns = [lambda: i for i in range(3)]
print([f() for f in fns])                                 # [2, 2, 2]
fixed = [lambda i=i: i for i in range(3)]
print([f() for f in fixed])                               # [0, 1, 2]

# 3 Shallow vs deep copy
a = [[1, 2], [3]]
b, c = a.copy(), copy.deepcopy(a)
a[0].append(99)
print(b[0], c[0])                                         # [1, 2, 99] [1, 2]

# 4 == compares values, `is` compares identity
x, y = [1, 2], [1, 2]
print(x == y, x is y)                                     # True False

# 5 Removing items while iterating skips elements
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)                                               # [1, 2, 3]
print([n for n in [1, 2, 2, 3] if n != 2])                # [1, 3]

# 6 Floats, rounding, division
print(0.1 + 0.2 == 0.3, round(2.5), round(3.5), -7 // 2, -7 % 2, 7 / 2)   # False 2 4 -4 1 3.5

# 7 sort() returns None; sorted() returns a new list
data = [3, 1, 2]
print(data.sort(), data, sorted([3, 1, 2], reverse=True))  # None [1, 2, 3] [3, 2, 1]

# 8 String += in a loop is quadratic in the worst case; join is linear
parts = [str(i) for i in range(5)]
print("-".join(parts))                                    # 0-1-2-3-4
```
Other classic mistakes: writing `if x == None` instead of `if x is None`; bare `except:` that hides bugs; using `and`/`or` between pandas Series instead of `&`/`|`; chained assignment in pandas (a no-op under pandas 3.0 Copy-on-Write); comparing floats with `==`; forgetting that `df.sort_values` returns a new frame; merging on a key with duplicates and silently multiplying rows; reading IDs as integers and losing leading zeros (`dtype=str`).

### Example
`add_sku("B")` returns `['A', 'B']` because both calls share the default list. `[lambda: i for i in range(3)]` returns `[2, 2, 2]` as every lambda looks up the same `i` when called; the fix `lambda i=i: i` freezes the value. `round(2.5)` is 2 and `round(3.5)` is 4 because Python rounds halves to even; `-7 // 2` is -4 (floor division) and `-7 % 2` is 1.

### In the news
See news box. The pandas 3.0 `str` dtype and Copy-on-Write turn two former "gotchas" (object-dtype strings, `SettingWithCopyWarning`) into settled behaviour, so answers should describe the new rules and mention old versions only for legacy code.

### Interview angle
> [!question] How it is asked
> "What does this code print?" followed by a snippet with a mutable default, a closure or a copy.

> [!tip] Strong answer includes
> - Predict the output, explain the mechanism (evaluated once at definition, late binding, shared references), then give the fix
> - Use `copy.deepcopy`, `None` defaults, list comprehensions instead of mutating while iterating
> - Know `is` vs `==`, `sort` vs `sorted`, integer vs float division
> - Link to testing and defensive design in [[184 Python OOP, Modules & Project Structure]]

---
## 12. ⭐ Advanced: Streaming, Generators & Windows Without Loading Everything
> ⭐ Advanced · _Added beyond the tracker_

### Definition
When data does not fit in memory, or arrives as a stream (scanner events, IoT readings, ERP exports of millions of rows), process it incrementally: **generators** (`yield`) produce one item at a time; `pd.read_csv(..., chunksize=n)` yields DataFrames; a `deque(maxlen=k)` keeps a rolling window with O(1) updates. Aggregations that can be combined across chunks (sum, count, min, max; mean via sum and count) work chunk by chunk; medians and distinct counts need other techniques (sketches, two passes).

```python
import pandas as pd
from collections import deque
import io

# Stream a big CSV in chunks and aggregate without loading it all
csv = io.StringIO("sku,qty\n" + "\n".join(f"{'AB'[i % 2]},{i}" for i in range(1000)))
totals = {}
for chunk in pd.read_csv(csv, chunksize=300):
    for k, v in chunk.groupby("sku")["qty"].sum().items():
        totals[k] = totals.get(k, 0) + v
assert totals == {"A": 249500, "B": 250000}

# Generator pipeline: constant memory, lazy evaluation
def read_lines(lines):
    for ln in lines:
        yield ln.strip()
def parse(rows):
    for r in rows:
        sku, qty = r.split(",")
        yield sku, int(qty)
rows = parse(read_lines(["A,5\n", "B,7\n", "A,3\n"]))
agg = {}
for sku, q in rows:
    agg[sku] = agg.get(sku, 0) + q
assert agg == {"A": 8, "B": 7}

# Moving average over a stream using a deque (fixed-size window)
def moving_avg(stream, k):
    w, s = deque(maxlen=k), 0
    for x in stream:
        if len(w) == k:
            s -= w[0]
        w.append(x); s += x
        if len(w) == k:
            yield s / k
assert list(moving_avg([10, 20, 30, 40, 50], 3)) == [20.0, 30.0, 40.0]
print("toolbox ok")
```

### Example
A 1,000-row file read in chunks of 300 yields four chunks; combining per-chunk sums gives A = 249,500 and B = 250,000, equal to the whole-file result. The moving average over `[10, 20, 30, 40, 50]` with window 3 yields 20, 30, 40, using one running sum rather than re-adding three numbers each time. Data-quality checks on the same exports are in [[186 Python Data Cleaning & EDA Playbook]] and [[175 Data Quality, Master Data & Data Governance]].

### In the news
See news box. Python 3.15's lazy imports reduce start-up cost of scripts that import heavy libraries; for the data itself, chunking and generators remain the portable technique.

### Interview angle
> [!question] How it is asked
> "You have a 20 GB CSV of order lines and 8 GB of RAM. How do you compute revenue per SKU?"

> [!tip] Strong answer includes
> - Chunked reading with `usecols`, narrow dtypes (`category`, `float32`), and combinable aggregates
> - Generators for lazy pipelines; stating memory is O(chunk) rather than O(file)
> - Alternatives: DuckDB or a database for SQL on large files, Polars lazy mode, Parquet instead of CSV
> - Validation: compare chunked totals with a control total from the source system
