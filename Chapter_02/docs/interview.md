---
title: Variables & Data Types Interview Prep
chapter: 02
difficulty: ⭐⭐☆☆☆
study_time: 30 Minutes
revision_time: 15 Minutes
interview_importance: Medium
exam_importance: High
---

← [Practice](./practice.md) | 🏠 [Home](../../README.md) | [Projects](./projects.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🎤 Chapter 02 Interview & Exam Preparation

You will heavily rely on variables and data types in every single technical interview. Understanding how Python handles memory allocation for variables is often a key differentiator between a junior and an intermediate developer.

---

## ❓ Theory Questions (Exam Prep)

**Q1: Is Python strongly typed or dynamically typed?**
> **Answer:** Python is **dynamically typed**. In languages like Java or C++, you have to explicitly declare what type of data a variable will hold (e.g., `int age = 20;`). In Python, you just write `age = 20`, and Python automatically figures out it is an integer at runtime.

**Q2: What is the difference between `/` and `//` in Python?**
> **Answer:** `/` is standard division and *always* returns a float (e.g., `5 / 2 = 2.5`). `//` is floor division; it divides and rounds down to the nearest integer, returning an `int` (e.g., `5 // 2 = 2`).

**Q3: What does the `%` (modulo) operator do and when is it useful?**
> **Answer:** Modulo returns the remainder of a division. It is heavily used in coding interviews to check if a number is even or odd (`num % 2 == 0`).

---

## 🛑 Interview Traps & Tricky Questions

**Trap 1: String Multiplication**
*Interviewer: "What is the output of `"3" * 3` in Python?"*
> **Trap:** You might assume it's `9` or an error.
> **Answer:** `"333"`. When you multiply a string by an integer, Python simply repeats the string that many times!

**Trap 2: Floating Point Precision**
*Interviewer: "Does `0.1 + 0.2 == 0.3`?"*
> **Trap:** In pure math, yes. In Python (and almost all programming languages), NO! 
> **Answer:** It returns `False`. Because of how computers store floating-point numbers in binary, `0.1 + 0.2` actually evaluates to `0.30000000000000004`.

---

## 👔 HR / Scenario Questions

*Scenario: "Arun, we have a script that is asking the user for their birth year and calculating their current age. However, the program keeps crashing with a TypeError. What is the most likely cause?"*

**Your Answer:** "The most likely cause is that the programmer forgot to typecast the user input. The `input()` function in Python always returns a string. If they tried to do `2024 - birth_year` without converting `birth_year` to an integer using `int()`, Python will throw a TypeError for trying to subtract a string from an integer."

---
### Next Recommended Step
Put this theory into practice by building a mini-project. Head over to **[Projects](./projects.md)**.
