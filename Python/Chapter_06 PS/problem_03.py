# A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams

spams = ["Make a lot of money", "buy now", "subscribe this", "click this"]
text = input("Enter your text: ")

if text in spams:
    print("This is a spam comment")
else:
    print("This is not a spam comment")

# end

