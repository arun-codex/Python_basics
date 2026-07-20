# Write a python program to find an average of two numbers entered by the user.


a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))

average = (a+b) / 2

print ("The average value of a and b is : ", average)

#this is another way to write this program 
# print("The average value of a and b is : ", (a+b)/2)


# This will give <class 'int'>
print(type(a))

# This will give <class 'int'>
print(type(b))

# This will give <class 'float'> because / always give float value 
print(type(average))


