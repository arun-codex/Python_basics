# Chapter 01 PS - Modules & Comments (Practice Set)

---

# Introduction

**What is this topic?**
This is the Practice Set companion to Chapter 1. While the main chapter taught you the theory behind importing modules, using `pip`, and writing comments, this directory focuses exclusively on applying those concepts through code.

**Why is it important?**
Programming is not a spectator sport. Solving practice sets is the only way to build muscle memory for syntax. 

**Where is it used in real-world projects?**
The exact scripts you write here (using `os` to scan directories, or `pyttsx3` to output audio) are fundamental versions of real-world server scripts and accessibility tools.

---

# Learning Objectives

After completing this practice set, students should be able to:
- Write and execute Python scripts independently.
- Confidently use `pip` to install third-party packages.
- Implement the `os` module for basic filesystem interaction.
- Troubleshoot basic `ImportError` exceptions.

---

# Practice Questions (Core Set)

### Problem 1: Multi-line Printing
Write a program to print a multi-line poem (e.g., Twinkle Twinkle Little Star). Use the correct string formatting to ensure the newlines are respected in the output.

### Problem 2: Using Built-in Modules
Use the REPL (Read, Evaluate, Print, Loop) interactive prompt to import the `math` module and calculate the square root of 64. (Note: Just practice in terminal, no file needed).

### Problem 3: External Modules (Text-to-Speech)
Install the external module `pyttsx3` using pip. Write a script that uses this module to make your computer say "Hello, Python is amazing!" out loud.

### Problem 4: OS Directory Listing
Write a program using the built-in `os` module to list all the contents (files and folders) of a specific directory (like the directory your script is in). Add comments explaining what the code is doing.

---

# Solutions

**Solution to Problem 1:**
```python
# Using triple quotes to span multiple lines without needing \n
poem = '''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.'''

print(poem)
```

**Solution to Problem 3:**
```python
# Problem_3.py
# Make sure to run `pip install pyttsx3` in your terminal first!

import pyttsx3 # Import the external module

engine = pyttsx3.init() # Initialize the engine
engine.say("Hello, Python is amazing!") # Queue the speech
engine.runAndWait() # Execute
```

**Solution to Problem 4:**
```python
# Problem_4.py
import os # Import the built-in Operating System module

# os.listdir() takes a path. '.' means current directory.
# We store the result in a variable called 'contents'
contents = os.listdir('.')

print("Contents of this directory:")
print(contents)
```

---

# Mini Projects

1. **Audiobook Reader (Basic)**
   - **Difficulty:** Intermediate
   - **Concepts:** `pyttsx3`, File reading (preview).
   - **Task:** Make the computer read a long string of text.
2. **Directory Scanner Tool**
   - **Difficulty:** Beginner
   - **Concepts:** `os` module.
   - **Task:** Print the contents of a user's Desktop directory.

---

# Common Errors

### `ModuleNotFoundError: No module named 'pyttsx3'`
- **Why:** Python cannot find the package. It either isn't installed, or is installed in a different Python environment.
- **How to Fix:** Open terminal and run `pip install pyttsx3`. 

---

# Interview Questions

### 10 Practice Interview Questions
1. How do you print a string that spans multiple lines?
2. What command do you run in the terminal to install a package?
3. What built-in module allows you to interact with the file system?
4. How do you list the contents of a directory programmatically?
5. What does the `#` symbol do in Python?
6. Why are triple quotes `'''` sometimes used as comments?
7. What is the difference between `import os` and `pip install pyttsx3`?
8. Explain what the Python REPL is.
9. Write a script on the whiteboard to print the current working directory.
10. How do you add an inline comment?

---

# Summary

This practice set solidified your understanding of the Python environment. By writing scripts that interact with your operating system (`os`) and external libraries (`pyttsx3`), you have taken your first real steps as a Python developer.

---

# Folder Structure

```text
Chapter_01 PS/
│
├── readme.md         <-- (You are here)
├── Problem_1.py
├── Problem_3.py
└── Problem_4.py
```
*(Proceed to Chapter 2 to continue the course!)*
