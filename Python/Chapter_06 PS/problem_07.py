# Write a program to find out whether a given post is talking about “Arun” or not.

articles = "hii Arun , how are you doing today, Arun is your full name or Arun kumar is your full name"

# Get name from user
name = input("Enter key word you want to search in article: ")

# Check if name is present in the article
if name in articles:
    print("Yes the article is talking about", name)
else:
    print("Name is not present in the article")
