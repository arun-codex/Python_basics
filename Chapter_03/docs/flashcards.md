---
title: Strings Flashcards
chapter: 03
difficulty: ⭐⭐☆☆☆
study_time: 10 Minutes
revision_time: 5 Minutes
interview_importance: Extremely High
exam_importance: High
---

← [Projects](./projects.md) | 🏠 [Home](../../README.md) | [Resources](./resources.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🧠 Active Recall Flashcards

Use these for your 5-Minute Revision. Cover the answer, read the question, and force yourself to recall the answer before checking.

---

<details>
<summary><b>Question:</b> Does string slicing include the stop index? (e.g. `word[0:4]`)</summary>
<br>
<b>Answer:</b> No. It stops *before* the stop index. `word[0:4]` gets indexes 0, 1, 2, and 3.
</details>

<details>
<summary><b>Question:</b> What is the easiest way to reverse a string in Python?</summary>
<br>
<b>Answer:</b> Using slicing with a step of -1: `word[::-1]`
</details>

<details>
<summary><b>Question:</b> Are strings mutable or immutable?</summary>
<br>
<b>Answer:</b> Immutable. Once created, you cannot change a character at a specific index. You must create a new string.
</details>

<details>
<summary><b>Question:</b> What does the string method `.find("xyz")` return if "xyz" is not in the string?</summary>
<br>
<b>Answer:</b> It returns `-1`.
</details>

<details>
<summary><b>Question:</b> What is an escape sequence? Give an example.</summary>
<br>
<b>Answer:</b> A way to insert characters that are illegal or have special meaning in a string. Example: `\n` for a new line, or `\t` for a tab.
</details>

---
### Next Recommended Step
Check out the **[Resources](./resources.md)** if you want to explore the massive list of built-in string methods available in Python!
