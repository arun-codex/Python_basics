# Write a program which finds out whether a given name is present in a list or not.

# List of names
name_list = ["Arun", "Adarsh", "Aarav", "Aarushi", "Aisha", "Aman", "Aarav", "Amina"]

# Ask user for name
name = input("Enter your name: ")

# Check if name is in list or not
if name in name_list:
    print("Name is present in the list")
else:
    print("Name is not present in the list")

# End