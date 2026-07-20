---
title: Dictionaries and Sets Projects
chapter: 05
difficulty: ⭐⭐⭐☆☆
study_time: 1 Hour
revision_time: N/A
interview_importance: High
exam_importance: Low
---

← [Interview](./interview.md) | 🏠 [Home](../../README.md) | [Flashcards](./flashcards.md) →
[README](../README.md) | [Notes](./notes.md) | [Practice](./practice.md) | [Interview](./interview.md) | [Cheat Sheet](./cheatsheet.md) | [Projects](./projects.md)

# 🚀 Chapter 05 Projects

Build these to solidify your understanding of dictionaries and sets. This is how professionals actually use these data structures.

## 📱 Project 1: Contact Book Application

**Goal:** Build a command-line program that stores names and phone numbers.
**Difficulty:** ⭐⭐☆☆☆
**Estimated Time:** 30 Mins

### Concepts Practiced
- Dictionary initialization.
- Dictionary `.update()` and `.pop()`.
- Error handling with `.get()`.

### Project Requirements
1. Create an empty dictionary called `contacts`.
2. Write a `while` loop that asks the user what they want to do:
   - Type "add" to add a new contact.
   - Type "search" to look up a phone number.
   - Type "delete" to remove a contact.
   - Type "exit" to quit.
3. If the user searches for a name that doesn't exist, print "Contact not found" instead of crashing.

### 🌟 Bonus Feature (Portfolio Value)
Update the program so that one person (key) can have *multiple* phone numbers. 
*Hint: The value in your dictionary should be a list!* `{"Arun": ["555-1234", "555-9876"]}`

---

## 🔒 Project 2: Unique Password Analyzer

**Goal:** Analyze a list of compromised passwords to find unique entries.
**Difficulty:** ⭐⭐⭐☆☆
**Estimated Time:** 20 Mins

### Concepts Practiced
- Converting lists to sets.
- Set mathematical operations (Intersection).

### Project Requirements
1. Create a list of 10 passwords (include duplicates like "password123", "admin", "admin").
2. Convert that list into a set to find out how many *unique* passwords were used.
3. Create a second set of "Banned Passwords".
4. Use the **Intersection** operator `&` to print out which user passwords are in the banned list.

---
### Next Recommended Step
Projects finished? Excellent! Let's do some Active Recall to lock this into long-term memory. Go to **[Flashcards](./flashcards.md)**.
