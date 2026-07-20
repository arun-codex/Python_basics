---
title: Strings Projects
chapter: 03
difficulty: ⭐⭐☆☆☆
study_time: 45 Minutes
revision_time: N/A
interview_importance: Low
exam_importance: Low
---

← [Interview](./interview.md) | 🏠 [Home](../../README.md) | [Flashcards](./flashcards.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🚀 Chapter 03 Projects

String manipulation is incredibly fun. Build this project to solidify your understanding of string methods and slicing.

## ✉️ Project 1: The Automated Letter Generator

**Goal:** Build a script that automatically generates a customized formal letter by replacing placeholder tags in a string template.
**Difficulty:** ⭐⭐☆☆☆
**Estimated Time:** 20 Mins

### Concepts Practiced
- Multi-line strings (`'''`)
- `str.replace()`
- `input()`
- F-strings

### Project Requirements
1. Create a multi-line string variable called `template`. It should look exactly like this:
```text
Dear <|NAME|>,
You are selected for the <|ROLE|> position!
Please report to the office on <|DATE|>.
Regards,
HR Department
```
2. Ask the user to input a Name, a Role, and a Date using `input()`.
3. Use the `.replace()` string method to replace `<|NAME|>` with the user's name, `<|ROLE|>` with the user's role, and `<|DATE|>` with the user's date.
4. Print the final customized letter to the screen!

*Hint: Remember that `.replace()` returns a NEW string. You have to save it back into a variable (e.g., `template = template.replace(...)`).*

---
### Next Recommended Step
Projects finished? Let's do some Active Recall to lock in the theory. Go to **[Flashcards](./flashcards.md)**.
