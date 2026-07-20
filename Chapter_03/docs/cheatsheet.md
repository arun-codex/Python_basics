---
title: Strings Cheat Sheet
chapter: 03
difficulty: ⭐⭐☆☆☆
study_time: 15 Minutes
revision_time: 5 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Notes](./notes.md) | 🏠 [Home](../../README.md) | [Practice](./practice.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# ⚡ Chapter 03 Cheat Sheet: Strings

Use this page for rapid 5-minute and 15-minute revisions right before an exam.

## 📌 1. String Slicing Visualizer
```text
String:   P   Y   T   H   O   N
Index:    0   1   2   3   4   5
Negative:-6  -5  -4  -3  -2  -1
```
*Remember: The STOP index is never included!*

## 📌 2. Slicing Syntax (`string[start:stop:step]`)
| Code | Explanation | Output (using "PYTHON") |
| :--- | :--- | :--- |
| `word[0:3]` | From index 0 up to (but not including) 3 | `"PYT"` |
| `word[:3]` | Same as above (starts at 0 implicitly) | `"PYT"` |
| `word[2:]` | From index 2 to the very end | `"THON"` |
| `word[-1]` | The last character | `"N"` |
| `word[::-1]`| **Reverses the string!** | `"NOHTYP"` |

## 📌 3. Essential String Methods
Assume `s = "hello world"`

| Method | What it does | Example Output |
| :--- | :--- | :--- |
| `len(s)` | Returns length of string | `11` |
| `s.capitalize()` | Capitalizes first letter | `"Hello world"` |
| `s.count("o")` | Counts occurrences of "o" | `2` |
| `s.find("world")` | Returns starting index of "world" | `6` |
| `s.replace("h", "j")`| Replaces characters | `"jello world"` |

## 📌 4. Escape Sequences
| Sequence | Output |
| :--- | :--- |
| `\n` | New Line |
| `\t` | Tab (Indent) |
| `\'` | Single Quote `'` |
| `\\` | Backslash `\` |

## 🚨 Things I Always Forget
1. Strings are **Immutable**. You cannot do `word[0] = "X"`. You must create a new string: `new_word = "X" + word[1:]`.
2. F-strings need the `f` prefix: `print(f"Name: {name}")`.

---
### Next Recommended Step
Test your syntax retention by solving the **[Practice Problems](./practice.md)**.
