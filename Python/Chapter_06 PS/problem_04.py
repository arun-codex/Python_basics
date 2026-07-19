# Write a program to find whether a given username contains less than 10 characters or not

# Ask user for username
username = input("Enter your username: ")

# Find length of username
username_len = len(username)

# Check if username is less than 10 characters or not
if username_len < 10: 
    print("Username is valid")
else:
    print("Username is greater than 10 characters")
    print("Make it shorter than 10 characters or use this one")
    print(f"Username is {username[:10]}")

