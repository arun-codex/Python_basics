---
title: Variables & Data Types Cheat Sheet
chapter: 02
difficulty: ⭐☆☆☆☆
study_time: 15 Minutes
revision_time: 5 Minutes
interview_importance: Medium
exam_importance: High
---

← [Notes](./notes.md) | 🏠 [Home](../../README.md) | [Practice](./practice.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# ⚡ Chapter 02 Cheat Sheet: Variables & Data Types

Use this page for rapid 5-minute and 15-minute revisions right before an exam.

## 📌 1. Variable Rules
- ✅ Valid: `name`, `name1`, `my_name`, `_name`
- ❌ Invalid: `1name`, `my name`, `my-name`, `print`

## 📌 2. Data Types Summary

| Type | Example | What is it? |
| :--- | :--- | :--- |
| `int` | `5`, `-10` | Whole numbers |
| `float`| `3.14`, `-0.5` | Decimal numbers |
| `str` | `"Hello"` | Text data |
| `bool` | `True`, `False`| Logical values (MUST be Capitalized) |
| `None` | `None` | Empty value |

## 📌 3. Essential Operators

| Category | Symbols | Example |
| :--- | :--- | :--- |
| **Arithmetic** | `+`, `-`, `*`, `/`, `%`, `//` | `5 % 2 = 1` (Remainder) |
| **Assignment** | `=`, `+=`, `-=` | `x += 5` (Same as `x = x + 5`) |
| **Comparison** | `==`, `!=`, `<`, `>` | `5 == 5` (Returns True) |
| **Logical** | `and`, `or`, `not` | `True and False` (Returns False) |

## 📌 4. Critical Syntax

| Action | Code |
| :--- | :--- |
| **Check Type** | `type(my_variable)` |
| **Get Input** | `name = input("Enter name: ")` |
| **Typecast (Str -> Int)** | `num = int("5")` |
| **Typecast (Int -> Str)** | `text = str(5)` |

## 🚨 Things I Always Forget
1. `input()` **ALWAYS** returns a string. If you want a number, you must cast it: `int(input("Enter number: "))`.
2. `a = b` means assign the value of `b` to `a`. `a == b` means ask if `a` is equal to `b`.

---
### Next Recommended Step
Test your syntax retention by solving the **[Practice Problems](./practice.md)**.
