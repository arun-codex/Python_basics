# Write a program to detect double space in a string

word = "Hello  My Name is Arun.  How are you?"

# using count function
count = word.count("  ")
print(count)

# using find function
print(word.find("  "))
