# 3. Return the factorial (using a normal loop, not recursion).
def factorial_of_num(n):
    facto = 0
    for i in range(1,n):
        facto += i
    return facto

n = 6 
f = factorial_of_num(n)
print(f)