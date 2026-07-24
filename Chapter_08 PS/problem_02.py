# 2. Write a python program using function to convert Celsius to Fahrenheit



c = int(input("Enter the temperature in Celsius: "))

def conv(c):
    f = (c * 9/5) + 32 
    return f

print(conv(c))