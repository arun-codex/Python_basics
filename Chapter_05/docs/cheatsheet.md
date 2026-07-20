---
title: Dictionaries and Sets Cheat Sheet
chapter: 05
difficulty: ⭐⭐⭐☆☆
study_time: 15 Minutes
revision_time: 5 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Notes](./notes.md) | 🏠 [Home](../../README.md) | [Practice](./practice.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# ⚡ Chapter 05 Cheat Sheet: Dictionary and Sets

Use this page for rapid 5-minute and 15-minute revisions right before an exam or interview.

## 📌 1. Dictionaries at a Glance

| Operation | Syntax | Example |
| :--- | :--- | :--- |
| **Initialize Empty** | `d = {}` | `my_dict = {}` |
| **Initialize Data** | `d = {k: v}` | `user = {"name": "Arun", "age": 20}` |
| **Access (Safe)** | `d.get(k)` | `user.get("name")` *(Returns None if key missing)* |
| **Access (Unsafe)** | `d[k]` | `user["name"]` *(Throws KeyError if missing)* |
| **Add/Update** | `d[k] = v` | `user["city"] = "NY"` |
| **Delete** | `del d[k]` or `d.pop(k)` | `user.pop("age")` |

### Dictionary Iteration
```python
d = {"a": 1, "b": 2}

for key in d.keys():           # Iterates over keys
for value in d.values():       # Iterates over values
for key, value in d.items():   # Iterates over both
```

## 📌 2. Sets at a Glance

| Operation | Syntax | Example |
| :--- | :--- | :--- |
| **Initialize Empty** | `s = set()` | `my_set = set()` *(Do NOT use `{}`)* |
| **Initialize Data** | `s = {e1, e2}` | `my_set = {1, 2, 3}` |
| **Add Element** | `s.add(e)` | `my_set.add(4)` |
| **Remove Element** | `s.remove(e)` | `my_set.remove(4)` *(Throws error if missing)* |
| **Discard Element** | `s.discard(e)` | `my_set.discard(4)` *(Safe removal)* |

### Set Math Operations
```python
A = {1, 2, 3}
B = {3, 4, 5}

A | B   # Union: {1, 2, 3, 4, 5}
A & B   # Intersection: {3}
A - B   # Difference: {1, 2}
```

## 🚨 Things I Always Forget
1. **Dictionary Keys MUST be immutable!** (Strings, ints, tuples). You cannot use a list as a dictionary key.
2. **Sets are unordered.** You cannot index them. `my_set[0]` is an instant crash.
3. `d = {}` creates an empty dictionary. `s = set()` creates an empty set.

---
### Next Recommended Step
Test your syntax retention by solving the **[Practice Problems](./practice.md)**.
