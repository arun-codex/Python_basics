a = int(input("Enter you age: "))

# if statement no : 1
if(a%2 == 0):
    print("a is even")
# End of if statement no : 1

# if statement no : 2
if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are not born yet!")

elif(a==0):
    print("You are just born!")

else:
    print("you are below the age of consent")
# End of if statement no : 2

print("Thanks for using the app")