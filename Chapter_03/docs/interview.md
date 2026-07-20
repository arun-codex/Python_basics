---
title: Strings Interview Prep
chapter: 03
difficulty: ⭐⭐⭐☆☆
study_time: 45 Minutes
revision_time: 20 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Practice](./practice.md) | 🏠 [Home](../../README.md) | [Projects](./projects.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🎤 Chapter 03 Interview & Exam Preparation

String manipulation is one of the most tested topics in coding interviews (especially on platforms like LeetCode or HackerRank).

---

## ❓ Theory Questions (Exam Prep)

**Q1: Explain what it means when we say "Strings are immutable in Python".**
> **Answer:** Immutability means that once a string object is created in memory, its contents cannot be altered. If you try to do `word[0] = 'X'`, Python throws a `TypeError`. To "modify" a string, you must actually create a brand new string and reassign it to the variable (e.g., `word = 'X' + word[1:]`).

**Q2: What is the syntax to reverse a string using slicing?**
> **Answer:** `string[::-1]`. This tells Python to start from the end, go to the beginning, and take steps of `-1` (backwards).

**Q3: How do you format a string to inject variables dynamically?**
> **Answer:** By using F-strings (introduced in Python 3.6). You prefix the string with `f` and place the variables inside curly braces: `f"Hello {name}"`.

---

## 🛑 Interview Traps & Tricky Questions

**Trap 1: Out of Bounds Slicing**
*Interviewer: "If `word = 'PYTHON'`, what happens if I run `print(word[2:100])`? Will it crash?"*
> **Trap:** You might assume it throws an `IndexError` because there is no index 100.
> **Answer:** It will NOT crash! Python slicing is very forgiving. If the stop index is out of bounds, Python just stops at the end of the string. The output will be `"THON"`.

**Trap 2: `replace()` doesn't modify the original string!**
*Interviewer: "What is the output of the following code?"*
```python
word = "Hello"
word.replace("H", "J")
print(word)
```
> **Trap:** You might assume the output is `"Jello"`.
> **Answer:** The output is `"Hello"`. Because strings are immutable, `.replace()` returns a *new* string. The code didn't assign the new string back to the variable. It should have been `word = word.replace("H", "J")`.

---
### Next Recommended Step
Put this theory into practice by building a mini-project. Head over to **[Projects](./projects.md)**.
