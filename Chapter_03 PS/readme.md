# Chapter 03 PS - Strings (Practice Set)

---

# Introduction

**What is this topic?**
This is the Practice Set companion to Chapter 3. Here, you will apply your theoretical knowledge of strings, string slicing, formatting, and built-in methods (like `.replace()` and `.find()`).

**Why is it important?**
Text manipulation is a daily requirement for developers. Learning to slice strings correctly and format them for UI displays is non-negotiable.

---

# Learning Objectives

After completing this practice set, students should be able to:
- Dynamically format strings using `f-strings` or concatenation.
- Use string methods to sanitize and modify text data.
- Utilize escape sequences (`\n`, `\t`) to format console output beautifully.

---

# Practice Questions (Core Set)

### Problem 1: Greeting User
Write a Python program to display a user-entered name followed by "Good Afternoon" using the `input()` function.

### Problem 2: Template Replacement
Write a program to fill in a letter template given below with a name and date.
```text
letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''
```

### Problem 3: Detect Double Spaces
Write a program to detect if there are any double spaces in a string.

### Problem 4: Replace Double Spaces
Replace the double spaces from Problem 3 with single spaces.

### Problem 5: Format with Escape Sequences
Write a program to format the following letter using escape sequence characters.
`letter = "Dear Arun, This Python course is nice. Thanks!"`

---

# Solutions

**Solution to Problem 1:**
```python
name = input("Enter your name: ")
print(f"Good Afternoon, {name}")
# Or using concatenation: print("Good Afternoon, " + name)
```

**Solution to Problem 2:**
```python
letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

name = input("Enter your name: ")
date = input("Enter date: ")

# Strings are immutable, so we MUST reassign the result to the variable
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)
```

**Solution to Problem 3 & 4:**
```python
text = "This is a string with double  spaces."

# Problem 3: Detection
double_spaces_exist = text.find("  ")
print("Double space at index:", double_spaces_exist) # Returns -1 if not found

# Problem 4: Replacement
clean_text = text.replace("  ", " ")
print(clean_text)
```

**Solution to Problem 5:**
```python
# Using \n for newline and \t for tab indent
formatted_letter = "Dear Arun,\n\tThis Python course is nice.\nThanks!"
print(formatted_letter)
```

---

# Mini Projects

1. **Email Slicer**
   - **Difficulty:** Intermediate
   - **Task:** Ask the user for their email. Slice the string at the `@` symbol to print their username and domain separately.
2. **Mad Libs**
   - **Difficulty:** Beginner
   - **Task:** Use an f-string to inject 5 user-provided words into a funny story template.

---

# Common Errors

### `AttributeError: 'str' object has no attribute 'replacee'`
- **Why:** Typo in the method name.
- **How to Fix:** Ensure you spell built-in methods exactly (`.replace()`).

### `TypeError: 'str' object does not support item assignment`
- **Why:** You tried to fix a typo in a string using `text[0] = "A"`.
- **How to Fix:** Use `.replace()` or slicing. Strings are immutable!

---

# Interview Questions

### 10 Practice Interview Questions
1. How do you replace a substring within a string?
2. Does the `.replace()` method modify the original string? Why or why not?
3. What method finds the index of a substring?
4. Write code to format a string dynamically with a variable.
5. What does the `\n` escape sequence do?
6. How do you convert a string to uppercase?
7. What happens if `.find()` does not find the substring?
8. Write a function to check if a string contains double spaces.
9. How do you print a literal backslash `\` in a string?
10. What is an f-string and why is it preferred over concatenation?

---

# Folder Structure

```text
Chapter_03 PS/
│
├── readme.md         <-- (You are here)
├── problem_01.py
├── problem_02.py
├── problem_03.py
├── problem_04.py
└── problem_05.py
```
*(Proceed to Chapter 4 to continue the course!)*
