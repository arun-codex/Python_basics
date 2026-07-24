# 7. Print the multiplication table of a given number using a while loop. 

n = int(input("Enter a Number: ")) 
i = 1

while i < 11:
    print(f"{n} x {i} = {n*i}")
    i +=1
