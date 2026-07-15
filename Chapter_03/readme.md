# Chapter 03 - Python Strings

---

# Introduction

**What is this topic?**
A String is a fundamental data type in Python used to represent and store text data. It is an ordered sequence of characters enclosed within single, double, or triple quotes. Crucially, strings in Python are **immutable**, meaning once a string is created, it cannot be changed in place.

**Why is it important?**
Text processing is one of the most common tasks in programming. From rendering UI text and reading files, to parsing API responses and generating reports, strings are everywhere.

**Why should every Python developer learn it?**
Python is renowned for its incredible text-processing capabilities. Understanding how to slice strings, format them dynamically, and use built-in string methods (like `.replace()` or `.split()`) allows you to write clean and efficient code without relying on complex, manual loops.

**Where is it used in real-world projects?**
- Parsing and cleaning raw text data.
- Building URLs dynamically for Web Scraping or API calls.
- Formatting console outputs and generating logs.

**Industry use cases:**
- **Web Development:** HTML/JSON generation and parsing.
- **Data Science / NLP:** Pre-processing text data (lowercasing, removing punctuation) before feeding it to machine learning models.
- **Cybersecurity:** Analyzing network packet payloads or searching for malicious signatures in text.

---

# Learning Objectives

After completing this chapter, students should be able to:
- Understand what a String is and the concept of immutability.
- Perform string indexing and slicing (both positive and negative).
- Utilize Escape Sequences to format output.
- Apply Python's vast array of built-in string methods.
- Solve text-based algorithmic interview questions.

---

# Theory

### Immutability
A string is immutable. This means if you have `name = "Arun"`, you cannot change the 'A' to a 'T' by doing `name[0] = "T"`. Python will throw a `TypeError`. Instead, you must create a *new* string.

### Indexing
Because strings are ordered sequences, every character has a specific address, called an **index**. Python uses zero-based indexing.
`"P y t h o n"`
` 0 1 2 3 4 5 `

### Slicing
Slicing allows you to extract a substring from a string. It uses the syntax `string[start : stop : step]`. The `stop` index is *exclusive* (it goes up to, but does not include, the stop index).

---

# Syntax

```python
name = "Arun"
greeting = 'Hello'
paragraph = """This is a
multi-line string"""
```
- `"Arun"`: Double quotes are standard.
- `'Hello'`: Single quotes work exactly the same.
- `"""..."""`: Triple quotes allow strings to span multiple lines.

---

# Concepts Covered

- [x] String Definition & Quotes
- [x] String Concatenation & Repetition
- [x] Indexing (Positive and Negative)
- [x] Slicing
- [x] String Immutability
- [x] String Methods (`lower`, `upper`, `replace`, etc.)
- [x] Escape Sequences
- [x] f-strings (String Formatting)

---

# Important Functions

*(Note: Strings have methods, but few global functions apply only to them. `len()` is the most common).*

### 1. `len()`
- **Purpose:** Returns the number of characters in the string, including spaces.
- **Syntax:** `len(string_name)`
- **Parameters:** A string.
- **Return Value:** Integer.
- **Example:** `len("Hello")`
- **Output:** `5`
- **Common Mistakes:** Forgetting that spaces and punctuation count towards the length.
- **Interview Tips:** Often used to find the middle index of a string: `mid = len(s) // 2`.

---

# Methods

String methods belong to the string object and return a *new* string (because strings are immutable).

### 1. `upper()` and `lower()`
- **Explanation:** Converts the string to all uppercase or all lowercase.
- **Example:** `"Arun".upper()`
- **Output:** `"ARUN"`

### 2. `capitalize()`
- **Explanation:** Converts only the first character to uppercase.
- **Example:** `"hello world".capitalize()`
- **Output:** `"Hello world"`

### 3. `title()`
- **Explanation:** Converts the first letter of *every word* to uppercase.
- **Example:** `"hello world".title()`
- **Output:** `"Hello World"`

### 4. `replace(old, new)`
- **Explanation:** Replaces occurrences of a substring with a new substring.
- **Example:** `"Hello World".replace("World", "Arun")`
- **Output:** `"Hello Arun"`

### 5. `find(substring)`
- **Explanation:** Returns the lowest index where the substring is found. Returns `-1` if not found.
- **Example:** `"Python".find("th")`
- **Output:** `2`

### 6. `split(separator)`
- **Explanation:** Splits the string into a list of strings based on the separator (default is space).
- **Example:** `"A B C".split()`
- **Output:** `['A', 'B', 'C']`

---

# Memory Visualization

Strings in Python are immutable arrays of Unicode characters. 

```python
name = "Cat"
```
In memory:
```text
name -----> [ 'C' | 'a' | 't' ] (Immutable block)
```

If you do `name = name + "s"`:
Python does *not* expand the existing block. It creates a brand new block `[ 'C' | 'a' | 't' | 's' ]` and updates the `name` pointer to point to the new block. The old block is eventually garbage collected.

---

# Internal Working

In CPython, strings are highly optimized. Because they are immutable, Python uses **String Interning** for short, common strings. If you create `a = "hello"` and `b = "hello"`, Python might point both variables to the exact same string object in memory to save space. 
Furthermore, string concatenation (`+`) in a loop is traditionally slow in Python because a new memory block must be allocated every iteration. (Though CPython 3.x has heavily optimized this, using `.join()` is still the preferred internal method for joining many strings).

---

# Code Examples

### 20 Beginner Examples

```python
# 1. Single quotes
str1 = 'Hello'

# 2. Double quotes (Useful if string contains an apostrophe)
str2 = "It's a good day"

# 3. Triple quotes for multiline
str3 = '''Line 1
Line 2'''

# 4. String concatenation (+)
greeting = "Hello" + " " + "World"

# 5. String repetition (*)
echo = "Hello! " * 3

# 6. Accessing first character
print(str1[0]) # 'H'

# 7. Accessing last character (Negative indexing)
print(str1[-1]) # 'o'

# 8. Slicing (First 3 chars)
print(str1[0:3]) # 'Hel'

# 9. Slicing with defaults
print(str1[:3]) # 'Hel'

# 10. Finding length
print(len(str1)) # 5

# 11. Escape sequence (Newline)
print("Hello\nWorld")

# 12. Escape sequence (Tab)
print("Hello\tWorld")

# 13. f-string formatting
name = "Arun"
print(f"My name is {name}")

# 14. Convert to uppercase
print(str1.upper())

# 15. Convert to lowercase
print(str1.lower())

# 16. Check if string ends with suffix
print(str1.endswith("lo")) # True

# 17. Check if string starts with prefix
print(str1.startswith("He")) # True

# 18. Count occurrences
print("banana".count("a")) # 3

# 19. Capitalize first letter
print("apple".capitalize()) # 'Apple'

# 20. Find a substring
print("banana".find("na")) # 2
```

### 10 Intermediate Examples

```python
# 1. Slicing with a step
print("Python"[0:6:2]) # 'Pto'

# 2. Reversing a string using slicing trick
print("Python"[::-1]) # 'nohtyP'

# 3. Replacing substrings
text = "I like apples"
print(text.replace("apples", "bananas"))

# 4. Splitting a string into a list
words = "Python is fun".split() # ['Python', 'is', 'fun']

# 5. Joining a list into a string
list_of_words = ['Python', 'is', 'fun']
sentence = " ".join(list_of_words)

# 6. Removing whitespace from ends
dirty_str = "   hello   "
print(dirty_str.strip()) # 'hello'

# 7. Formatting using .format() (Older method)
print("My name is {}".format("Arun"))

# 8. Checking if string is alphanumeric
print("Python3".isalnum()) # True

# 9. Checking if string is all digits
print("12345".isdigit()) # True

# 10. Chaining string methods
dirty_text = "   HELLO world  "
clean_text = dirty_text.strip().lower().capitalize() # 'Hello world'
```

### 5 Advanced Examples

```python
# 1. Using raw strings (r"...") for regular expressions or file paths
path = r"C:\new_folder\test.txt" # The \n and \t won't trigger escape sequences

# 2. Advanced f-string formatting (Padding and alignment)
num = 42
print(f"{num:05d}") # '00042'
print(f"{name:>10}") # Right-aligned in 10 spaces

# 3. Using translation tables (maketrans / translate)
table = str.maketrans("aeiou", "12345")
print("hello".translate(table)) # 'h2ll4'

# 4. Multiline f-strings
query = (
    f"SELECT * "
    f"FROM users "
    f"WHERE name = '{name}'"
)

# 5. Evaluating variables dynamically via f-string debugging (Python 3.8+)
x = 10
print(f"{x=}") # 'x=10'
```

---

# Practice Questions

### 10 Beginner Problems
1. Create a string with your name and print its length.
2. Concatenate your first name and last name with a space in between.
3. Extract the 3rd character of the string `"Python"`.
4. Extract the last character of `"Python"` using negative indexing.
5. Slice `"Programming"` to get the word `"Gram"`.
6. Print the string `"Hello World"` entirely in uppercase.
7. Print the string `"Hello World"` entirely in lowercase.
8. Use an f-string to print `"My name is [name] and I am [age] years old"`.
9. Write a program to find if the word `"apple"` is inside `"I like apple pie"`.
10. Use an escape sequence to print a word wrapped in double quotes (e.g., He said "Hi").

### 10 Intermediate Problems
1. Write a program to reverse a string entered by the user.
2. Check if a given string is a palindrome (reads the same forwards and backwards).
3. Write a program to remove all leading and trailing spaces from a user input.
4. Replace all spaces in a string with hyphens `-`.
5. Count how many vowels (a, e, i, o, u) are in a given string.
6. Split a sentence into a list of words and print the list.
7. Join the list `['a', 'b', 'c']` into a string `"a-b-c"`.
8. Write a program to extract the domain name from an email address (e.g., `user@gmail.com` -> `gmail.com`).
9. Capitalize every word in a sentence (convert to title case).
10. Check if a string contains only numbers without using a `for` loop.

### 10 Advanced Problems
1. Write a program to compress a string (e.g., `"aaabbc"` -> `"a3b2c1"`).
2. Write a program to find the first non-repeating character in a string.
3. Write a program to check if two strings are anagrams of each other.
4. Implement a simple Caesar Cipher encryption program.
5. Write a program to find the longest word in a sentence.
6. Write a program to remove all punctuation from a string.
7. Format a large integer with commas as thousands separators (e.g., `1000000` -> `1,000,000`).
8. Write a custom function that acts like `.split()` without using the built-in method.
9. Extract all hashtags from a tweet (string) using string methods.
10. Reverse the order of *words* in a sentence, but keep the words themselves spelled correctly.

---

# Solutions

**Intermediate Problem 2 (Palindrome):**
```python
text = input("Enter a word: ")
# Clean the text: remove spaces and lowercase it for accurate comparison
clean_text = text.replace(" ", "").lower()

# Check if the string is identical to its reversed self
if clean_text == clean_text[::-1]:
    print("It is a palindrome!")
else:
    print("Not a palindrome.")
```

**Advanced Problem 10 (Reverse Words):**
```python
sentence = "Python is awesome"
# 1. Split into words: ['Python', 'is', 'awesome']
words = sentence.split()
# 2. Reverse the list: ['awesome', 'is', 'Python']
words.reverse()
# 3. Join back with spaces
reversed_sentence = " ".join(words)
print(reversed_sentence) # Output: awesome is Python
```

---

# Mini Projects

1. **Vowel Counter:**
   - **Difficulty:** Beginner
   - **Concepts:** Iteration, `.count()`.
2. **Mad Libs Generator:**
   - **Difficulty:** Beginner
   - **Concepts:** User input, f-strings.
3. **Email Slicer:**
   - **Difficulty:** Intermediate
   - **Concepts:** `.find()`, slicing to extract username and domain.
4. **Palindrome Checker:**
   - **Difficulty:** Intermediate
   - **Concepts:** String slicing step `[::-1]`.
5. **Acronym Generator:**
   - **Difficulty:** Intermediate
   - **Concepts:** `.split()`, `.upper()`, indexing first letters.
6. **Word Count Tool:**
   - **Difficulty:** Beginner
   - **Concepts:** `.split()`, `len()`.
7. **Password Strength Checker:**
   - **Difficulty:** Advanced
   - **Concepts:** Iteration, `.isupper()`, `.isdigit()`, string lengths.
8. **Caesar Cipher Encoder:**
   - **Difficulty:** Advanced
   - **Concepts:** ASCII values (`ord()`, `chr()`), string concatenation.
9. **Text Analyzer:**
   - **Difficulty:** Advanced
   - **Concepts:** Counting words, vowels, consonants, and punctuation.
10. **Profanity Filter:**
    - **Difficulty:** Intermediate
    - **Concepts:** `.replace()` to censor bad words with `***`.

---

# Common Errors

### `TypeError: 'str' object does not support item assignment`
- **Why:** You tried to change a character inside a string by its index. Strings are immutable.
- **When:** `name = "Arun"; name[0] = "T"`
- **How to Fix:** Create a new string: `name = "T" + name[1:]`

### `IndexError: string index out of range`
- **Why:** You tried to access an index that doesn't exist.
- **When:** `text = "Hi"; print(text[5])`
- **How to Fix:** Ensure index is `< len(text)`.

### `AttributeError: 'NoneType' object has no attribute 'lower'`
- **Why:** You called a string method on a variable that is `None` (often from a failed regex match or API call).
- **How to Fix:** Check if the variable is not None before calling string methods.

---

# Best Practices

- **Formatting:** Use **f-strings** (Python 3.6+) over `%s` or `.format()`. They are faster and far more readable.
- **Concatenation:** When joining many strings in a loop, do not use `+=`. Append them to a list and use `"".join(list)`. It is much faster due to how memory works.
- **Quotes:** Pick a style (single or double quotes) and stick to it. PEP 8 does not mandate one over the other, but consistency is key.
- **Immutability:** Remember that string methods return a *new* string. `text.lower()` does nothing to `text` unless you reassign it: `text = text.lower()`.

---

# Performance Tips

- **Fast Methods:** `f-strings` are evaluated at runtime directly in C, making them extremely fast.
- **Slow Methods:** Repeated string concatenation using `+` in a massive `for` loop is notoriously slow.
- **Optimization Tips:** If you need to search a massive block of text for complex patterns, do not use basic string methods. Compile a Regular Expression using the `re` module.

---

# Real World Applications

- **Data Cleaning:** Converting all user emails to `.lower()` before saving to a database to prevent duplicate accounts (`User@email.com` vs `user@email.com`).
- **File Paths:** Using raw strings (`r"C:\..."`) to manage Windows file paths in scripts.
- **Web Scraping:** Using `.find()` and slicing to extract pricing text from raw HTML strings.
- **Security:** Hashing strings (passwords) before storing them.

---

# Interview Questions

### 20 Beginner Questions
1. What is a string?
2. How do you create a string?
3. What is the difference between single and double quotes?
4. What does it mean that strings are immutable?
5. How do you find the length of a string?
6. How do you access the first character?
7. What is negative indexing?
8. What is string slicing?
9. How do you convert a string to uppercase?
10. How do you convert a string to lowercase?
11. What does `strip()` do?
12. How do you replace a word in a string?
13. How do you split a sentence into words?
14. What are escape sequences?
15. What does `\n` do?
16. What does `\t` do?
17. How do you concatenate two strings?
18. How do you repeat a string 5 times?
19. What is an f-string?
20. How do you check if a string contains another string?

### 20 Intermediate Questions
1. How do you reverse a string?
2. What happens if you try `text[0] = "A"`?
3. What is the difference between `find()` and `index()`?
4. How do you join a list of strings into one string?
5. Explain `isalnum()`, `isalpha()`, and `isdigit()`.
6. How do you format a float to 2 decimal places using f-strings?
7. What is a raw string?
8. How do you check if a string is a palindrome?
9. Why is `.join()` preferred over `+` for concatenating a list of strings?
10. What does `splitlines()` do?
11. How do you count the occurrences of a substring?
12. Explain `startswith()` and `endswith()`.
13. What is the output of `"Python"[1:5:2]`?
14. How do you convert an integer to a string?
15. How do you remove only trailing spaces? (`rstrip()`)
16. How do you capitalize every word in a string? (`title()`)
17. What is the difference between `title()` and `capitalize()`?
18. How do you center-align a string with padding? (`center()`)
19. What does the `partition()` method do?
20. How does Python compare two strings? (Lexicographical order based on ASCII values).

### 20 Advanced Questions
1. Explain String Interning in Python.
2. How does the immutable nature of strings affect memory management?
3. What is the time complexity of the `in` operator for strings? (Boyer-Moore-Horspool algorithm).
4. Explain the difference between `bytes` and `str` in Python 3.
5. How do you encode a string to bytes and decode bytes to a string?
6. What is Unicode and how does Python 3 handle it?
7. How do you use the `maketrans()` and `translate()` methods?
8. Explain the `format_map()` method.
9. How would you implement a custom string class inheriting from `UserString`?
10. How do you extract variables locally into an f-string using `locals()`?
11. Compare the performance of `%` formatting, `.format()`, and f-strings.
12. Explain how to detect anagrams optimally.
13. Write an algorithm to find the longest palindromic substring.
14. What is the `re` module and when should you use it over string methods?
15. How do you handle string interpolation securely to prevent injection attacks?
16. Explain the KMP (Knuth-Morris-Pratt) algorithm for pattern matching.
17. How do you remove specific characters from a string optimally?
18. What is the memory overhead of a string in Python?
19. How do you align text columns in terminal outputs using string methods?
20. Explain the `ascii()` built-in function vs `repr()`.

---

# Interview Answers (Selected)

**Q: What is the difference between `find()` and `index()`?**
**A:** Both return the lowest index of a substring. However, if the substring is *not found*, `find()` returns `-1`, whereas `index()` raises a `ValueError`.

**Q: Why is `.join()` preferred over `+` for concatenating a list of strings?**
**A:** Strings are immutable. Using `+` in a loop creates a new string object in memory on every iteration, leading to O(N^2) time complexity. `.join()` calculates the total memory needed once and creates the final string in O(N) time.

**Q: Explain String Interning.**
**A:** To save memory, Python caches (interns) short, identifier-like strings (like variable names or dictionary keys). If you assign `"abc"` to two variables, Python only creates one string object in memory and points both variables to it.

---

# Cheat Sheet

| Operation | Syntax | Example | Output | Notes |
| :--- | :--- | :--- | :--- | :--- |
| **Length** | `len(s)` | `len("Hi")` | `2` | Returns integer |
| **Concatenate** | `s1 + s2` | `"A" + "B"` | `"AB"` | |
| **Repeat** | `s * n` | `"A" * 3` | `"AAA"` | |
| **Access** | `s[i]` | `"Py"[0]` | `"P"` | |
| **Slice** | `s[start:stop]`| `"Py"[0:1]` | `"P"` | Stop is exclusive |
| **Lowercase** | `s.lower()` | `"A".lower()`| `"a"` | Returns new string |
| **Uppercase** | `s.upper()` | `"a".upper()`| `"A"` | Returns new string |
| **Replace** | `s.replace(o, n)`|`"a".replace("a","b")`|`"b"`| Replaces all |
| **Split** | `s.split()` | `"a b".split()`|`['a', 'b']`| Returns a list |
| **Join** | `"sep".join(lst)`|`",".join(['a','b'])`|`"a,b"` | Opposite of split |

---

# Mind Map

```text
Chapter 3: Strings
├── Immutability (Cannot be changed in place)
├── Indexing & Slicing
│   ├── Positive (0 to n)
│   ├── Negative (-1 to -n)
│   └── Slicing [start:stop:step]
├── Formatting
│   ├── Escape Sequences (\n, \t)
│   └── f-strings (f"Hello {name}")
└── Common Methods
    ├── Case: upper(), lower(), title()
    ├── Search: find(), count(), startswith()
    ├── Modify: replace(), strip()
    └── List Conv: split(), join()
```

---

# Summary

Strings are an immutable sequence of characters. Mastering string manipulation (slicing, indexing, formatting, and methods) is mandatory for any Python developer, as text processing is ubiquitous in programming. Remember that modifying a string always results in a new string object being created.

---

# Key Takeaways

- Strings are immutable.
- Indexes start at `0`. Negative indexes start at `-1`.
- `stop` indexes in slicing are exclusive.
- `f-strings` are the modern, fast way to format text.
- Use `.join()` to merge lists of strings efficiently.

---

# Resources

- **Official Python Documentation:** [docs.python.org/3/library/stdtypes.html#text-sequence-type-str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
- **Relevant PEPs:** PEP 498 (Literal String Interpolation - f-strings)
- **Practice Websites:** CodingBat (String challenges)

---

# Folder Structure

```text
Chapter_03/
│
├── readme.md               <-- (You are here)
├── 01_intro_to_String.py   
├── 02_negative_slicing.py  
├── 03_string_function.py   
├── 04_escape_seq.py        
└── string.py               
```

---

# Progress Tracker

- [x] Theory
- [x] Examples
- [x] Exercises
- [x] Mini Project
- [x] Interview Questions
- [x] Cheat Sheet
- [x] Mind Map

---

# Revision Notes

- **Quotes:** Single `'`, double `"`, triple `'''` for multiline.
- **Slice:** `string[start:stop:step]`. Default start is 0, default stop is end.
- **Reverse trick:** `string[::-1]`.
- **f-string:** `f"Value is {x}"`.
- **Strip:** `strip()` removes edge spaces.
- **Split/Join:** `.split()` makes a string a list. `.join()` makes a list a string.

---

# Cheat Sheet Table

*(Refer to the comprehensive table in the Cheat Sheet section above)*

---

# Common Interview Programs

**1. Palindrome Check**
```python
def is_palindrome(s):
    # Reverse string and compare
    return s == s[::-1]
```
*Explanation:* Slicing `[::-1]` returns a reversed copy of the string.

**2. Count Vowels**
```python
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
```
*Explanation:* Iterates through every character checking membership in a string of vowels.

---

# Challenge Problems

1. Implement `.replace()` manually using loops and slicing.
2. Given a string, compress it (e.g., `AABBC` -> `A2B2C1`).
3. Check if two strings are valid anagrams.
4. Convert a string from `snake_case` to `camelCase`.
5. Find the longest substring without repeating characters.

---

# Assignments

1. Write a program that takes a user's full name and prints their initials (e.g., Arun Codex -> A.C.).
2. Write a script that checks if a string ends with `.txt` or `.py`.
3. Create a program that censors the word "darn" by replacing it with "****".
4. Prompt the user for a sentence and print how many words are in it.
5. Create a formatted receipt using f-string alignment (`>10` and `<10`).

---

# Frequently Asked Questions (FAQs)

**Q: Can I put double quotes inside double quotes?**
A: No, it will cause a Syntax Error. Use single quotes on the outside: `'He said "Hi"'`, or use an escape sequence: `"He said \"Hi\""`.

**Q: Why does `text.replace()` not change my string?**
A: Because strings are immutable. You must assign the result back: `text = text.replace()`.

---

# Keywords

- **Immutable:** Unchangeable after creation.
- **Sequence:** An ordered collection of items.
- **Substring:** A continuous sequence of characters within a string.
- **Index:** A numeric position in a sequence.

---

# Glossary

- **f-string:** Formatted string literals, prefixed with `f`.
- **Escape Sequence:** Characters starting with `\` that invoke an alternative interpretation (like newline).
- **String Interning:** Caching identical strings to save memory.

---

# Notes

- **Warning:** Beware of `IndexError` when looping through strings manually via indexing.
- **Best Practice:** Use `.lower()` when comparing user inputs to make your program case-insensitive.

---

# Do's and Don'ts

| ✅ Do | ❌ Don't |
| :--- | :--- |
| Use f-strings for formatting | Use the outdated `%s` formatting |
| Use `.join()` for lists of strings| Use `+=` in a large loop to build strings |
| Keep quotes consistent | Mix single and double quotes randomly |

---

# Revision Checklist

- [ ] I understand string immutability.
- [ ] I can slice strings forwards and backwards.
- [ ] I can use f-strings.
- [ ] I know `.replace()`, `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`.

---

# Quick Quiz

1. What is the output of `"ABC"[1]`?
   - A) A
   - B) B
   - C) C
2. Are strings mutable in Python?
   - A) Yes
   - B) No
3. Which method splits a string into a list?
   - A) `slice()`
   - B) `split()`
   - C) `join()`

*(Answers: 1: B, 2: B, 3: B)*

---

# Flash Cards

**Q:** How do you reverse a string?
**A:** `string[::-1]`

**Q:** What method converts a list of strings into one string?
**A:** `"".join(list)`

**Q:** What does `len(" A ")` return?
**A:** `3` (Spaces count as characters).

---

# Next Chapter

In the next chapter, we will explore **Lists**. You will learn how to create dynamic, mutable arrays that can hold multiple different data types at once!
