# 9. Create a function that prints the larger of two numbers.

a = 5
b = 6

def largerof(a,b):
    if(a==b):
        print("Both are equal.")
    elif(a > b):
        print(f"{a} is larger than {b}.")
    elif(a < b):
        print(f"{b} is larger than {a}")
    else:
        print("Something Wrong!")
        

largerof(a,b)