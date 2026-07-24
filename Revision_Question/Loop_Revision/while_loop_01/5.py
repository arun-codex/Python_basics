# 5. Find the sum of the first n natural numbers using a while loop.

'''
n = 5

sum_of_n = 1 + 2 + 3 + 4 + 5 = 15

'''

n = int(input("Enter n number to get sum: "))
i = 1
total = 0
while i <=n:
    total = total + i
    i +=1
print(total)


