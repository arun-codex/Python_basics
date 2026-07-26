# ⚡ Cheat Sheet: File I/O

← [Back to Chapter Dashboard](../README.md)

## Basic Syntax

### Opening and Closing
```python
# Don't do this (easy to forget to close)
f = open("data.txt", "r")
f.close()

# Do this instead! (Auto-closes)
with open("data.txt", "r") as f:
    # do something with f
    pass
```

### File Modes
- `"r"` - Read (Default)
- `"w"` - Write (Overwrites existing!)
- `"a"` - Append (Adds to the end)

### Reading Methods
```python
with open("data.txt", "r") as f:
    text = f.read()       # Reads entire file as a single string
    line = f.readline()   # Reads one line as a string
    lines = f.readlines() # Reads all lines into a list of strings
```

### Writing Methods
```python
with open("data.txt", "w") as f:
    f.write("Hello World\n")  # Writes a string
    
    lines = ["Line 1\n", "Line 2\n"]
    f.writelines(lines)       # Writes a list of strings
```

## ⚠️ Things People Forget
- `write()` does **not** automatically add a newline character (`\n`). You have to add it yourself.
- Using `"w"` mode on an existing file will completely wipe its contents before writing.
- `readlines()` keeps the `\n` character at the end of each line in the list. You might need to use `.strip()` to clean it up.
