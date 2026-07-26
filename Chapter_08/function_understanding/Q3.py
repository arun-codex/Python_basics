n = int(input("Enter a number to get factorial: "))
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)

factorial(n)