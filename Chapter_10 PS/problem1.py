''' 
1. Create a class
“Programmer” for storing information of few programmers working at
Microsoft 

'''



class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Arun", 120000, 844112)
print(p.name, p.salary, p.pin, p.company)


r = programmer("Rohan", 120000, 844112)
print(r.name, r.salary, r.pin, r.company)

