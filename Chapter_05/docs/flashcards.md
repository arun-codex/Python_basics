---
title: Dictionaries and Sets Flashcards
chapter: 05
difficulty: ⭐⭐☆☆☆
study_time: 10 Minutes
revision_time: 5 Minutes
interview_importance: High
exam_importance: High
---

← [Projects](./projects.md) | 🏠 [Home](../../README.md) | [Resources](./resources.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🧠 Active Recall Flashcards

Use these for your 5-Minute Revision. Cover the answer, read the question, and force yourself to recall the answer before checking.

---

<details>
<summary><b>Question:</b> What is the time complexity of searching a dictionary?</summary>
<br>
<b>Answer:</b> $O(1)$ (Instantaneous), because dictionaries use Hash Tables to calculate the exact location of the key in memory.
</details>

<details>
<summary><b>Question:</b> What happens if you try to use `my_dict["wrong_key"]`?</summary>
<br>
<b>Answer:</b> The program crashes with a `KeyError`.
</details>

<details>
<summary><b>Question:</b> How do you safely access a dictionary key without crashing?</summary>
<br>
<b>Answer:</b> Use the `.get()` method. Example: `my_dict.get("wrong_key")` returns `None`.
</details>

<details>
<summary><b>Question:</b> Can a list be used as a dictionary key?</summary>
<br>
<b>Answer:</b> No. Dictionary keys must be immutable (unhashable type error). Use a tuple instead.
</details>

<details>
<summary><b>Question:</b> How do you create an empty set?</summary>
<br>
<b>Answer:</b> `my_set = set()`. If you use `{}`, you create an empty dictionary!
</details>

<details>
<summary><b>Question:</b> Are sets ordered? Can I do `my_set[0]`?</summary>
<br>
<b>Answer:</b> No. Sets are completely unordered. Attempting to index a set will throw a TypeError.
</details>

<details>
<summary><b>Question:</b> What is the fastest way to remove all duplicates from a list?</summary>
<br>
<b>Answer:</b> Convert it to a set. `list(set(my_list))`
</details>

---
### Next Recommended Step
Check out the **[Resources](./resources.md)** if you are still feeling confused about Hash Tables!
