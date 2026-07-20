---
title: Dictionaries and Sets Interview Prep
chapter: 05
difficulty: ⭐⭐⭐⭐☆
study_time: 1 Hour
revision_time: 20 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Practice](./practice.md) | 🏠 [Home](../../README.md) | [Projects](./projects.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🎤 Chapter 05 Interview Preparation

Dictionaries (Hash Maps) are the single most important data structure for technical interviews. If you don't know dictionaries, you will not pass a coding interview.

---

## ❓ Theory Questions

**Q1: What is the time complexity of searching for a key in a dictionary?**
> **Answer:** $O(1)$ on average. This is because dictionaries use Hash Tables. The key is hashed to calculate the exact memory location, meaning Python doesn't have to scan through the dictionary to find it.

**Q2: What is the difference between `.get(key)` and `[key]`?**
> **Answer:** If the key does not exist, `[key]` will throw a `KeyError` and crash the program. `.get(key)` will safely return `None` (or a default value if you provide one, e.g., `.get(key, 0)`). 

**Q3: Can you use a list as a dictionary key?**
> **Answer:** No. Dictionary keys must be *hashable* (immutable). Since lists can be changed after they are created, they cannot be hashed. You must use a tuple instead if you want to store multiple values as a key.

---

## 🛑 Interview Traps & Tricky Questions

**Trap 1: The "Remove Duplicates" Trap**
*Interviewer: "How would you remove duplicates from a list in one line of code?"*
> **Trap:** They want to see if you understand sets.
> **Answer:** `list(set(my_list))`

**Trap 2: The Two-Sum Problem**
*Interviewer: "Given an array of integers, find two numbers that add up to a specific target. Try to do it faster than $O(n^2)$."*
> **Trap:** Nested loops take $O(n^2)$. 
> **Answer:** You must use a dictionary to store the numbers you have already seen. As you loop through the array, you calculate `target - current_number`. If that result is already a key in your dictionary, you found the pair in $O(n)$ time!

---

## 👔 HR / Scenario Questions

*Scenario: "Arun, we are building a login system. We need to store user emails and their passwords to verify logins quickly. We have 10 million users. Should we use two lists or a dictionary?"*

**Your Answer:** "Definitely a dictionary. If we use a list of emails, searching for a specific email takes $O(n)$ time, which would be terrible for 10 million users. A dictionary maps the email (key) directly to the password (value) in $O(1)$ time, making logins instantaneous."

---
### Next Recommended Step
Put this interview theory into practice by building something real. Head over to **[Projects](./projects.md)**.
