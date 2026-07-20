---
title: Lists and Tuples Cheat Sheet
chapter: 04
difficulty: ⭐⭐⭐☆☆
study_time: 15 Minutes
revision_time: 5 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Notes](./notes.md) | 🏠 [Home](../../README.md) | [Practice](./practice.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# ⚡ Chapter 04 Cheat Sheet: Lists & Tuples

Use this page for rapid 5-minute and 15-minute revisions right before an exam.

## 📌 1. List vs Tuple at a Glance

| Feature | List `[]` | Tuple `()` |
| :--- | :--- | :--- |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` |
| **Mutability** | Mutable (Can be changed) | Immutable (Cannot be changed) |
| **Speed** | Slower | Faster |
| **Use Case** | Data that changes over time (e.g. user list). | Constant data (e.g. days of week). |

## 📌 2. Accessing & Slicing
*(Applies to BOTH Lists and Tuples)*
Assume `l = [10, 20, 30, 40, 50]`
- **First item:** `l[0]` 
- **Last item:** `l[-1]`
- **Slice first three:** `l[:3]`  *(Returns `[10, 20, 30]`)*
- **Reverse:** `l[::-1]`

## 📌 3. List Methods (MUTATES the original list)
Assume `l = [5, 1, 9]`

| Method | What it does | Resulting List |
| :--- | :--- | :--- |
| `l.append(4)` | Adds to end | `[5, 1, 9, 4]` |
| `l.insert(1, 8)` | Inserts 8 at index 1 | `[5, 8, 1, 9]` |
| `l.pop(0)` | Removes & returns index 0 | `[1, 9]` |
| `l.remove(9)` | Removes the value 9 | `[5, 1]` |
| `l.sort()` | Sorts ascending | `[1, 5, 9]` |
| `l.reverse()` | Reverses order | `[9, 1, 5]` |

## 📌 4. Tuple Methods (Does NOT mutate)
Assume `t = (5, 5, 1)`
| Method | What it does | Result |
| :--- | :--- | :--- |
| `t.count(5)` | Occurrences of 5 | `2` |
| `t.index(1)` | Index of first 1 | `2` |

## 🚨 Things I Always Forget
1. `l.sort()` returns `None`. You cannot do `new_list = l.sort()`. It modifies `l` directly!
2. Creating a one-item tuple requires a comma: `t = (1,)`. Without it, it's just an integer wrapped in parentheses.

---
### Next Recommended Step
Test your syntax retention by solving the **[Practice Problems](./practice.md)**.
