---
title: Modules, Comments & pip Interview Prep
chapter: 01
difficulty: ⭐☆☆☆☆
study_time: 20 Minutes
revision_time: 10 Minutes
interview_importance: Low
exam_importance: Medium
---

← [Practice](./practice.md) | 🏠 [Home](../../README.md) | [Projects](./projects.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🎤 Chapter 01 Interview & Exam Preparation

You likely won't get coding interview questions on this chapter, but university exams love to test your understanding of Python's architecture (like the interpreter and modules).

---

## ❓ Theory Questions (Exam Prep)

**Q1: What is pip?**
> **Answer:** `pip` stands for "Pip Installs Packages" (or Preferred Installer Program). It is the standard package manager for Python that allows you to install and manage external libraries that do not come with the standard Python installation.

**Q2: What is the difference between an Interpreter and a Compiler?**
> **Answer:** Python is an interpreted language. The Python interpreter reads and executes the code line by line from top to bottom. If it hits an error on line 5, the first 4 lines will still run. A compiler (like in C++) translates the entire program into machine code *before* running it. If there is an error anywhere, the program won't run at all.

**Q3: How are multi-line comments technically handled in Python?**
> **Answer:** Python doesn't actually have a dedicated syntax for multi-line comments. When we use `'''` or `"""`, we are actually creating a multi-line *string*. However, because we don't assign that string to a variable, the Python interpreter reads it, evaluates it, and then instantly throws it away (garbage collects it), effectively making it a comment!

---

## 🛑 Exam Traps

**Trap 1: The Print Parentheses**
*Exam Question: Which of the following is correct in Python 3?*
A) `print "Hello"`
B) `print("Hello")`
> **Trap:** Many old tutorials use Python 2. In Python 2, `print "Hello"` was valid. In Python 3, it is an error.
> **Answer:** B

---
### Next Recommended Step
Want to play with some cool external modules? Head over to **[Projects](./projects.md)**.
