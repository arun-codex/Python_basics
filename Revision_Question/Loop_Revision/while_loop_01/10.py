
# 10. Keep asking the user to enter the correct password.
# Password: python123
# Stop only when the correct password is entered.

password = input("Enter password: ")

while password != "python123":
    print("Wrong password. Try again.")
    password = input("Enter password: ")
print("Password Matched!")

