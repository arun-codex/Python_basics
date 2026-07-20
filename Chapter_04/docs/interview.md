---
title: Lists and Tuples Interview Prep
chapter: 04
difficulty: ⭐⭐⭐☆☆
study_time: 45 Minutes
revision_time: 20 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Practice](./practice.md) | 🏠 [Home](../../README.md) | [Projects](./projects.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🎤 Chapter 04 Interview & Exam Preparation

Lists (often called Arrays in other languages) are the most tested data structure in technical interviews. If you don't understand Lists, you cannot pass a software engineering interview.

---

## ❓ Theory Questions (Exam Prep)

**Q1: What is the primary difference between a List and a Tuple?**
> **Answer:** Lists are mutable (can be changed after creation), whereas Tuples are immutable (cannot be changed after creation). Lists use square brackets `[]`, Tuples use parentheses `()`.

**Q2: Why does Python have Tuples if Lists can do everything a Tuple can do?**
> **Answer:** Because Tuples are immutable, they are faster and use less memory. They also provide safety; if you have data that should *never* change during the runtime of an application, storing it in a Tuple guarantees that it won't be accidentally modified by a rogue function.

**Q3: Can a List contain different data types?**
> **Answer:** Yes, Python lists are heterogeneous. They can contain integers, strings, floats, booleans, and even other lists, all at the same time.

---

## 🛑 Interview Traps & Tricky Questions

**Trap 1: Sorting a List**
*Interviewer: "What is the output of the following code?"*
```python
my_list = [5, 1, 9]
print(my_list.sort())
```
> **Trap:** You might assume the output is `[1, 5, 9]`.
> **Answer:** The output is `None`. The `.sort()` method sorts the list *in-place* and does not return the sorted list. To fix this, you must do `my_list.sort()` on one line, and `print(my_list)` on the next.

**Trap 2: The Single Item Tuple**
*Interviewer: "I want to create a tuple with a single item, the number 5. Is `t = (5)` correct?"*
> **Trap:** It looks correct, but parentheses are also used for math!
> **Answer:** No. `t = (5)` creates an integer. To create a single item tuple, you must include a trailing comma: `t = (5,)`.

---
### Next Recommended Step
Put this theory into practice by building a mini-project. Head over to **[Projects](./projects.md)**.
