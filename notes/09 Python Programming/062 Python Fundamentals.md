---
tags: [python-programming, tier1]
area: Python Programming
topic: "Python Fundamentals"
tier: Tier 1
roles: All Roles
status: complete
subtopics: 14
---
# Python Fundamentals

[[_Index - Python Programming|Python Programming]] · [[063 NumPy]] ➡

> **Area:** Python Programming · **Priority:** 🔴 Tier 1 · **Target roles:** All Roles

## Sub-topics in this note
1. [[#1. Data Types]]
2. [[#2. Variables & Naming]]
3. [[#3. Lists]]
4. [[#4. Tuples]]
5. [[#5. Dictionaries]]
6. [[#6. Sets]]
7. [[#7. String Operations]]
8. [[#8. Control Flow]]
9. [[#9. Functions]]
10. [[#10. List Comprehensions]]
11. [[#11. Error Handling]]
12. [[#12. File I/O]]
13. [[#13. ⭐ Advanced: Copying, Mutable Defaults & Generators]]
14. [[#14. ⭐ Advanced: Pythonic Code, Complexity & Testing]]

## 📰 News box
> [!news] Shared news hook for this topic (2024–2026): Python keeps growing as the default analytics language
> **Python adoption jumps (Stack Overflow Developer Survey 2025).** Python is used by **57.9%** of respondents, a **7 percentage point increase from 2024 to 2025**, which the survey ties to its role in AI and data work. ([Source](https://survey.stackoverflow.co/2025/technology))
> 
> **pandas 3.0 released (21 Jan 2026).** The release makes Copy-on-Write the only mode (removing `SettingWithCopyWarning` and chained assignment) and infers text columns as a dedicated `str` dtype instead of `object`. ([Source](https://pandas.pydata.org/community/blog/pandas-3.0.html), [release notes](https://pandas.pydata.org/docs/whatsnew/v3.0.0.html))
> 
> Sub-topics that say **"See news box"** reuse these items.

---
## 1. Data Types
> 🔴 Tier 1 · _Tracker hint:_ int, float, str, bool, NoneType; type(), isinstance(); type coercion

### Definition
Python is **dynamically typed**: a variable holds a reference to an object, and the *object* carries the type. Core built-in scalar types:

| Type | Example | Notes |
|---|---|---|
| `int` | `42` | Arbitrary precision, no overflow |
| `float` | `3.14` | 64-bit IEEE 754, so `0.1 + 0.2 != 0.3` exactly |
| `str` | `"SIOM"` | Immutable text |
| `bool` | `True` | Subclass of `int` (`True + 1 == 2`) |
| `NoneType` | `None` | "No value"; test with `is None` |

```python
type(5)                  # <class 'int'>
isinstance(5, (int, float))   # True; preferred over type(x) == int
int("12") + 3            # explicit coercion -> 15
float("3.5"); str(10); bool(0)  # False
"5" + 3                  # TypeError: Python does not implicitly coerce str and int
5 + 2.0                  # 7.0, int is implicitly widened to float
```
Falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `None`. For money use `decimal.Decimal` to avoid float rounding.

### Example
A raw sales CSV gives quantity as `"120"` (string). `qty = int("120"); revenue = qty * 49.5` gives `5940.0`. Without the cast, `"120" * 49.5` raises `TypeError`, and `"120" * 2` silently gives `"120120"`, a classic data bug.

### In the news
See news box. With Python used by 57.9% of developers surveyed, type-handling basics are table stakes for any analyst role.

### Interview angle
> [!question] How it is asked
> "What is the difference between `==` and `is`?" or "What does `type(True)` return and why?" or a quick screen asking you to predict `0.1 + 0.2 == 0.3`.

> [!tip] Strong answer includes
> - Names the built-in types and notes dynamic typing
> - Uses `isinstance` rather than `type() ==`
> - Explains float precision and when to use `Decimal` or `round`
> - Distinguishes implicit vs explicit coercion and the `None` check with `is`

---

## 2. Variables & Naming
> 🔴 Tier 1 · _Tracker hint:_ snake_case convention; mutable vs immutable; variable unpacking a,b = 1,2

### Definition
A variable is a **name bound to an object**; assignment never copies the object. PEP 8 recommends `snake_case` for variables/functions, `PascalCase` for classes and `UPPER_CASE` for constants. Names cannot start with a digit or be keywords.

**Immutable** objects cannot change in place: `int`, `float`, `str`, `bool`, `tuple`, `frozenset`. **Mutable** objects can: `list`, `dict`, `set`.

```python
a, b = 1, 2          # unpacking
a, b = b, a          # swap without temp
first, *rest = [10, 20, 30]   # first=10, rest=[20, 30]
x = [1, 2]; y = x; y.append(3)   # x is now [1, 2, 3] (same object)
z = x.copy()         # independent shallow copy
```
`id(obj)` shows identity; `==` compares value, `is` compares identity.

### Example
`total_sales = 0` then `total_sales += 500` rebinds the name to a new int (ints are immutable). But `orders = []; backup = orders; orders.append("PO-1")` also changes `backup`, which is why you copy lists before modifying them in a function.

### In the news
See news box. pandas 3.0's Copy-on-Write exists precisely to remove this class of "did my change leak into another object?" surprise in DataFrames.

### Interview angle
> [!question] How it is asked
> "What is the difference between mutable and immutable types? Give examples." or "What does this code print?" (a shared-list aliasing snippet).

> [!tip] Strong answer includes
> - Variables as references/names, not boxes
> - Lists of mutable vs immutable types with one consequence of each
> - `is` vs `==` and aliasing vs copying
> - PEP 8 naming used correctly in code you write live

---

## 3. Lists
> 🔴 Tier 1 · _Tracker hint:_ Ordered, mutable; list[0], list[-1], list[1:3]; .append(), .extend(), .sort(), list comprehension

### Definition
A **list** is an ordered, mutable, heterogeneous sequence. Indexing starts at 0; negative indices count from the end; slices `a[start:stop:step]` exclude `stop`.

```python
a = [10, 20, 30, 40, 50]
a[0], a[-1], a[1:3]      # 10, 50, [20, 30]
a[::-1]                  # reversed copy
a.append(60)             # add one item, O(1) amortised
a.extend([70, 80])       # add many items
a.insert(0, 5)           # O(n)
a.pop(); a.remove(20)    # remove last / first match
a.sort(reverse=True)     # in place, returns None
sorted(a)                # new list
squares = [x**2 for x in a if x > 20]
```
`append([1,2])` adds a nested list; `extend([1,2])` adds two items. Membership `x in a` is O(n), so use a set for large lookups.

### Example
Daily demand `d = [120, 135, 128, 150, 142]`. Total `sum(d) = 675`, average `sum(d)/len(d) = 135.0`, last 3 days `d[-3:] = [128, 150, 142]`, and days above average `[x for x in d if x > 135] = [150, 142]`.

### In the news
See news box. Lists remain the workhorse structure for small data before moving to NumPy arrays or pandas Series, which now underpin the 57.9% Python usage figure's analytics side.

### Interview angle
> [!question] How it is asked
> "Difference between `append` and `extend`?" "How do you reverse a list?" "What is the time complexity of `in` on a list?"

> [!tip] Strong answer includes
> - Slicing rules including negative and step
> - In-place `sort()` returns `None` vs `sorted()`
> - Complexity awareness (append O(1), insert/in O(n))
> - Switches to set/dict when lookups dominate

---

## 4. Tuples
> 🔴 Tier 1 · _Tracker hint:_ Ordered, immutable; (a,b,c); unpacking; used as dict keys; namedtuple

### Definition
A **tuple** is an ordered, **immutable** sequence. Because it is immutable and hashable (if its contents are), it can be a **dictionary key** or set member, which lists cannot. A single-item tuple needs a trailing comma: `(5,)`.

```python
point = (28.6, 77.2)
lat, lon = point                 # unpacking
def stats(x): return min(x), max(x)   # returns a tuple
lo, hi = stats([3, 9, 5])

from collections import namedtuple
Order = namedtuple("Order", ["sku", "qty"])
o = Order("A1", 40)
o.sku, o.qty                      # readable field access
route_cost = {("Pune", "Nashik"): 210}   # tuple as dict key
```
Use tuples for fixed records and function returns; lists for collections that change.

### Example
Distance lookup: `dist = {("Mumbai","Pune"): 150, ("Pune","Nashik"): 210}`. Then `dist[("Pune","Nashik")]` gives 210. A list as key would raise `TypeError: unhashable type`.

### In the news
See news box. Typed, structured data is also why modern libraries lean on named fields (`NamedTuple`, dataclasses) in production analytics code.

### Interview angle
> [!question] How it is asked
> "List vs tuple?" or "Why can a tuple be a dict key but a list cannot?"

> [!tip] Strong answer includes
> - Immutability and hashability link
> - Use cases: fixed records, multiple return values, keys
> - `namedtuple` for readability
> - Caveat: a tuple holding a list is not fully immutable

---

## 5. Dictionaries
> 🔴 Tier 1 · _Tracker hint:_ Key-value pairs; dict.get(key, default); dict comprehension; .items(), .keys(), .values()

### Definition
A **dict** maps unique, hashable keys to values with average **O(1)** lookup. Since Python 3.7 it preserves insertion order.

```python
stock = {"A1": 40, "B2": 15}
stock["C3"] = 8                    # add/update
stock.get("Z9", 0)                 # 0, no KeyError
stock["Z9"]                        # KeyError
for sku, qty in stock.items(): ...
stock.keys(); stock.values()
low = {k: v for k, v in stock.items() if v < 20}   # comprehension
from collections import Counter, defaultdict
Counter(["A", "B", "A"])           # Counter({'A': 2, 'B': 1})
d = defaultdict(list); d["x"].append(1)
stock.update({"A1": 50}); stock.pop("B2")
```
Merge with `a | b` (3.9+).

### Example
Count orders per region: `orders = ["N","S","N","E","N"]`; `Counter(orders)` gives N=3, S=1, E=1. Revenue by region: `rev = {}` then `rev[r] = rev.get(r, 0) + amount` for each row.

### In the news
See news box. JSON from APIs maps directly to Python dicts, which is how most real-time data feeds reach analysts.

### Interview angle
> [!question] How it is asked
> "How would you count word frequency?" or "What happens when you access a missing key, and how do you avoid it?"

> [!tip] Strong answer includes
> - `get`, `setdefault`, `defaultdict`, `Counter`
> - Hash table, O(1) average lookup, keys must be hashable
> - Iteration with `.items()`
> - Comprehensions for filtering/transforming

---

## 6. Sets
> 🔴 Tier 1 · _Tracker hint:_ Unordered, unique; set operations: union |, intersection &, difference -; .add(), .discard()

### Definition
A **set** is an unordered collection of unique, hashable items with average O(1) membership tests. Ideal for deduplication and comparing groups.

```python
a = {1, 2, 3}; b = {3, 4}
a | b      # union {1,2,3,4}
a & b      # intersection {3}
a - b      # difference {1,2}
a ^ b      # symmetric difference {1,2,4}
a.add(9); a.discard(100)   # discard: no error if absent
a.remove(100)              # KeyError if absent
set([1,1,2])               # {1, 2}
empty = set()              # {} creates an empty dict
```
`a <= b` tests subset. `frozenset` is the immutable, hashable version.

### Example
Customers last month `A = {101,102,103,104}`, this month `B = {103,104,105}`. Retained `A & B = {103,104}`; churned `A - B = {101,102}`; new `B - A = {105}`.

### In the news
See news box. Sets are the quick tool for data-quality checks (missing IDs between two extracts) before loading into pandas.

### Interview angle
> [!question] How it is asked
> "Remove duplicates from a list preserving order" or "Find customers present in list A but not in B."

> [!tip] Strong answer includes
> - Set operations with the operator forms
> - Why membership is fast (hashing)
> - `discard` vs `remove`; `{}` is a dict
> - Order-preserving dedupe: `list(dict.fromkeys(x))`

---

## 7. String Operations
> 🔴 Tier 1 · _Tracker hint:_ f-strings: f'{name}: {value:.2f}'; .split(), .join(), .strip(), .replace(), .format()

### Definition
Strings are **immutable** sequences of Unicode characters. Methods return new strings.

```python
name, value = "Revenue", 1234.5678
f"{name}: {value:.2f}"        # 'Revenue: 1234.57'
f"{value:,.0f}"               # '1,235' thousands separator
f"{0.256:.1%}"                # '25.6%'
"  hi  ".strip()              # 'hi'
"a,b,c".split(",")            # ['a','b','c']
"-".join(["2026","01","15"])  # '2026-01-15'
"Pune".replace("P", "p"); "x".upper(); "pune".title()
"{} costs {}".format("Item", 5)
"abc".startswith("a"); "b" in "abc"
```
Use `join` rather than repeated `+=` in loops (O(n) vs O(n²)).

### Example
Clean SKU `raw = "  sku-0042 "`: `raw.strip().upper().replace("-", "_")` gives `'SKU_0042'`. Parse `"Pune|Nashik|210"` with `city_a, city_b, km = "Pune|Nashik|210".split("|")` and `int(km)`.

### In the news
See news box. pandas 3.0 now infers a dedicated `str` dtype for text columns, making string-heavy cleaning faster and more consistent.

### Interview angle
> [!question] How it is asked
> "Check if a string is a palindrome" or "Format a float to 2 decimals in a message."

> [!tip] Strong answer includes
> - f-strings with format specs
> - Immutability and method chaining
> - `split`/`join` as inverses
> - Slicing `s[::-1]` for reversal

---

## 8. Control Flow
> 🔴 Tier 1 · _Tracker hint:_ if/elif/else; for loop with enumerate(); while loop; break/continue/pass

### Definition
Python uses indentation for blocks.

```python
if qty > 100: tier = "A"
elif qty > 50: tier = "B"
else: tier = "C"

for i, sku in enumerate(["A1", "B2"], start=1):
    print(i, sku)
for a, b in zip([1,2,3], ["x","y","z"]): ...

n = 0
while n < 5:
    n += 1
    if n == 2: continue    # skip rest of this pass
    if n == 4: break       # exit loop
for x in range(3): pass    # placeholder
```
`for...else`: the `else` runs if the loop did not `break`. Conditional expression: `"hi" if x else "lo"`. `range(a, b, step)` excludes `b`.

### Example
ABC classification by cumulative value: loop through items sorted by value, keep a running total, `if cum <= 0.8*total: cls="A" elif cum <= 0.95*total: cls="B" else: cls="C"`.

### In the news
See news box. Loop-heavy code over large tables is what vectorised pandas/NumPy replaces (see [[063 NumPy]]).

### Interview angle
> [!question] How it is asked
> "Write FizzBuzz" or "Find the first number divisible by 7 in a list; what happens if none exists?"

> [!tip] Strong answer includes
> - Correct `enumerate`/`zip`/`range` use
> - Understands `break`/`continue`/`pass` and loop `else`
> - Avoids infinite `while` loops
> - Notes when vectorisation beats loops

---

## 9. Functions
> 🔴 Tier 1 · _Tracker hint:_ def, *args, **kwargs; default params; return multiple values; lambda x: x*2

### Definition
Functions are first-class objects: assignable, passable and returnable.

```python
def eoq(demand, order_cost, hold_cost=2.0, *args, **kwargs):
    """Return (EOQ, orders per year)."""
    q = (2 * demand * order_cost / hold_cost) ** 0.5
    return q, demand / q        # returns a tuple

q, n = eoq(12000, 100, hold_cost=3)
double = lambda x: x * 2
sorted(items, key=lambda r: r["qty"])
def f(*args, **kwargs): ...     # args tuple, kwargs dict
def bad(x, acc=[]): ...         # mutable default is shared: avoid
```
Scope follows LEGB (Local, Enclosing, Global, Built-in). Add type hints (`def f(x: int) -> float`) and docstrings.

### Example
`eoq(12000, 100, hold_cost=3)`: $\sqrt{2 \times 12000 \times 100 / 3} = \sqrt{800000} \approx 894.4$ units, orders per year $12000/894.4 \approx 13.4$.

### In the news
See news box. As analytics code moves into shared repositories, reusable, typed, documented functions are the entry point to maintainable pipelines.

### Interview angle
> [!question] How it is asked
> "What are `*args` and `**kwargs`?" "Why is a mutable default argument dangerous?"

> [!tip] Strong answer includes
> - Positional, keyword, default, variadic parameters
> - Multiple returns as a tuple
> - Lambda for short, throwaway functions only
> - The default-argument gotcha and LEGB scope

---

## 10. List Comprehensions
> 🔴 Tier 1 · _Tracker hint:_ [x**2 for x in range(10) if x%2==0] — concise, Pythonic iteration

### Definition
A comprehension builds a collection from an iterable in one expression: `[expr for item in iterable if condition]`. Same idea for dicts, sets and generators.

```python
[x**2 for x in range(10) if x % 2 == 0]     # [0, 4, 16, 36, 64]
[("hi" if x > 0 else "lo") for x in vals]   # if/else goes BEFORE for
{k: v*2 for k, v in d.items()}              # dict comp
{x % 3 for x in range(10)}                  # set comp
sum(x*x for x in range(10))                 # generator, lazy
[(i, j) for i in range(2) for j in range(2)]  # nested
```
Use a plain loop when logic is complex; readability beats brevity. Typically faster than an equivalent `append` loop.

### Example
Convert prices with 18% GST: `prices = [100, 250, 400]`; `[round(p*1.18, 2) for p in prices]` = `[118.0, 295.0, 472.0]`. Keep only orders above 200: `[p for p in prices if p > 200]` = `[250, 400]`.

### In the news
See news box. Comprehensions are the pure-Python cousin of pandas filtering; both express "transform and filter" declaratively.

### Interview angle
> [!question] How it is asked
> "Rewrite this loop as a comprehension" or "Flatten a list of lists."

> [!tip] Strong answer includes
> - Correct syntax with filter vs conditional expression placement
> - Dict/set/generator variants
> - Memory trade-off: generator vs list
> - Judgement: don't nest three levels deep

---

## 11. Error Handling
> 🔴 Tier 1 · _Tracker hint:_ try/except/finally; raise; specific exceptions (ValueError, KeyError, FileNotFoundError)

### Definition
Exceptions signal runtime problems. Catch the **specific** exception you can handle, never a bare `except:`.

```python
try:
    qty = int(row["qty"])
    price = prices[row["sku"]]
except ValueError:
    qty = 0                      # bad number
except KeyError as e:
    print("Unknown SKU", e)
else:
    total = qty * price          # runs only if no exception
finally:
    log.close()                  # always runs

def check(x):
    if x < 0:
        raise ValueError("demand cannot be negative")
```
Common: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `FileNotFoundError`, `ZeroDivisionError`. Custom errors subclass `Exception`. Python style is EAFP (easier to ask forgiveness than permission).

### Example
Loading a monthly file: `try: df = pd.read_csv(path) except FileNotFoundError: df = pd.DataFrame()` lets a batch job continue when one month's file is missing, while a `ValueError` from a corrupt value is logged and re-raised.

### In the news
See news box. pandas 3.0 removing chained-assignment behaviour turns silent logic bugs into explicit patterns, the same philosophy as raising errors early.

### Interview angle
> [!question] How it is asked
> "What is the difference between `except Exception` and a bare `except`?" or "When does `finally` run?"

> [!tip] Strong answer includes
> - Specific exceptions first, general last
> - `else` and `finally` roles
> - `raise` and custom exceptions
> - Do not swallow errors silently; log them

---

## 12. File I/O
> 🔴 Tier 1 · _Tracker hint:_ open(file,'r') with context manager; read(), readlines(); CSV, JSON handling

### Definition
Always open files with a **context manager** so they close automatically.

```python
with open("orders.txt", "r", encoding="utf-8") as f:
    text = f.read()              # whole file
    # or: lines = f.readlines()  # list of lines
    # or: for line in f: ...     # memory-friendly
with open("out.txt", "w") as f:  # 'a' append, 'w' overwrites
    f.write("hello\n")

import csv, json
with open("o.csv", newline="") as f:
    for row in csv.DictReader(f): print(row["sku"])
with open("cfg.json") as f:
    cfg = json.load(f)           # file -> dict
json.dumps(cfg, indent=2)        # dict -> string
```
For tables prefer `pd.read_csv`. Use `pathlib.Path` for paths.

### Example
Read a 5 GB log without loading it: `with open("log.txt") as f: errors = sum(1 for line in f if "ERROR" in line)` keeps memory flat because the file is iterated line by line.

### In the news
See news box. pandas 3.0's string dtype and CoW mainly speed up what you do *after* loading files, so reading with the right dtypes still matters.

### Interview angle
> [!question] How it is asked
> "How do you read a very large file?" or "Why use `with open`?"

> [!tip] Strong answer includes
> - Context manager guarantees closing
> - Modes `r`, `w`, `a` and encoding
> - Line iteration for big files; `csv`/`json` modules or pandas for structure
> - Handles `FileNotFoundError`

---

## 13. ⭐ Advanced: Copying, Mutable Defaults & Generators
> ⭐ Advanced · _Added beyond the tracker_

### Definition
**Shallow vs deep copy.** `b = a.copy()` or `copy.copy(a)` duplicates the outer container but shares inner objects; `copy.deepcopy(a)` clones recursively.

```python
import copy
a = [[1, 2], [3]]
b = copy.copy(a);  b[0].append(9)    # a[0] is now [1, 2, 9]
c = copy.deepcopy(a); c[0].append(7) # a unchanged
```

**Mutable default argument bug:** `def add(x, acc=[])` reuses one list across calls. Use `acc=None` and create the list inside.

**Generators** yield values lazily and keep one item in memory:

```python
def read_chunks(path):
    with open(path) as f:
        for line in f:
            yield line.strip()
gen = (x * 2 for x in range(10**7))   # no list built
```
Related tools: `itertools`, `functools.lru_cache`, decorators, `dataclasses`, and `if __name__ == "__main__":` guards.

### Example
Summing a 10-million-number stream: `sum(x for x in range(10**7))` uses constant memory, while `sum([x for x in range(10**7)])` builds a list of 10 million ints first.

### In the news
See news box. Copy semantics are exactly what pandas 3.0 Copy-on-Write standardises: every derived DataFrame behaves as an independent copy while sharing memory until modified.

### Interview angle
> [!question] How it is asked
> "Shallow vs deep copy?" "What is a generator and why use it?" "What is wrong with `def f(x, l=[])`?"

> [!tip] Strong answer includes
> - Concrete shallow-copy surprise with nested lists
> - Generator = lazy iterator, saves memory
> - Fix for the mutable default
> - Mention of `lru_cache` for memoising expensive pure functions

---

## 14. ⭐ Advanced: Pythonic Code, Complexity & Testing
> ⭐ Advanced · _Added beyond the tracker_

### Definition
Interviewers probe whether you write **clean, efficient** Python.

- **Complexity cheatsheet:** list index O(1), list `in` O(n), dict/set lookup O(1) average, sort O(n log n), `list.insert(0, x)` O(n) (use `collections.deque` for O(1) at both ends).
- **Idioms:** `enumerate`, `zip`, unpacking, `any()`/`all()`, `dict.get`, `with`, `sorted(key=...)`, `collections.Counter`.
- **Type hints and docstrings:** `def forecast(x: list[float]) -> float:`.
- **Virtual environments** (`python -m venv .venv`) and `requirements.txt` for reproducibility.
- **Testing:** a minimal `pytest` function `def test_eoq(): assert round(eoq(12000,100,3)[0]) == 894`.
- **Common coding-round tasks:** two-sum with a dict, anagram check with `Counter`, reversing, de-duplication, string parsing.

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return seen[target - n], i
        seen[n] = i
```

### Example
`two_sum([2, 7, 11, 15], 9)`: i=0, n=2, store {2:0}; i=1, n=7, target-n=2 is in seen so return `(0, 1)`. Complexity O(n) time, O(n) space versus O(n²) for the nested-loop version.

### In the news
See news box. As Python moves deeper into business roles (57.9% usage), recruiters increasingly expect clean, tested code even from non-engineers.

### Interview angle
> [!question] How it is asked
> "Solve two-sum and state the complexity" or "How would you speed up this slow loop?"

> [!tip] Strong answer includes
> - Brute force first, then the hash-map optimisation
> - Big-O stated for time and space
> - Readable names, docstring, edge cases (empty list, duplicates)
> - Mentions testing and environment hygiene

---
## 🔗 Go deeper: expansion notes
- [[184 Python OOP, Modules & Project Structure|Python OOP, Modules & Project Structure]]
- [[185 Python Interview Problem Bank|Python Interview Problem Bank]]
- [[186 Python Data Cleaning & EDA Playbook|Python Data Cleaning & EDA Playbook]]
