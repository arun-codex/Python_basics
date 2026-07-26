# 🚀 Mini Projects: File I/O

← [Back to Chapter Dashboard](../README.md)

## Project 1: High Score Tracker

- **Goal:** Create a simple script that saves the user's high score. If the user enters a higher score, update the file.
- **Difficulty:** ⭐⭐⭐☆☆
- **Time:** 30 minutes
- **Concepts Used:** File Reading, File Writing, Type Conversion, Conditionals
- **Skills Learned:** Persisting data between script executions.

**Expected Workflow:**
1. Check if `highscore.txt` exists (or just try to read it).
2. If it doesn't exist, assume the high score is 0.
3. Ask the user for a new score.
4. If the new score is greater than the saved high score, write the new score to `highscore.txt`.

## Project 2: Simple Diary application

- **Goal:** Build an application where the user can write a diary entry, and it gets appended to a `diary.txt` file with the current date/time.
- **Difficulty:** ⭐⭐⭐☆☆
- **Time:** 20 minutes
- **Concepts Used:** File Appending, `datetime` module (optional).
- **Skills Learned:** Logging and appending data sequentially.

**Expected Workflow:**
1. Prompt the user: "Write your diary entry for today:"
2. Take the user's input.
3. Open `diary.txt` in append mode (`"a"`).
4. Write the input to the file along with a newline `\n`.
