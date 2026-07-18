a = int(input("Enter your age: "))

# If elif else ladder is used to check multiple conditions

if(a>=18):
    print("You are above the age of consent")

elif(a<0):
    print("You are not born yet!")

elif(a==0):
    print("You are just born!")

else:
    print("you are below the age of consent")

print("Thanks for using the app")
