from functools import reduce
a = [1, 2,345, 33, 56565, 10, 125, 873,8739]



def greater(a,b):
    if a > b: 
        return a
    return b

print(reduce(greater,a ))