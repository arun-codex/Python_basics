# Write a program to find the greatest of four numbers entered by the user.

# Taking inputs form users
n1 = int(input("Enter a number1: "))
n2 = int(input("Enter a number2: "))
n3 = int(input("Enter a number3: "))
n4 = int(input("Enter a number4: "))

# Checking the greater number using if and elif else ladder
if(n1>=n2 and n1>=n3 and n1>=n4):
    print("number1 is greater ")
elif(n2>=n1 and n2>=n3 and n2>=n4):
    print("number2 is greater")
elif(n3>=n1 and n3>=n2 and n3>=n4):
    print("number3 is greater")
else:
    print("number4 is greater")
