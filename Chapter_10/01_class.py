class Employee:
    language = "python"   # This is a class attribute
    salary = 120000


arun = Employee()
arun.name = "Arun"       # This is an instance attribute 
print(arun.name, arun.language, arun.salary)

rohan = Employee()
rohan.name = "rohan"
print(rohan.salary, rohan.language, rohan.name)


# here name is instance attribute and salary and language are class attributes as they directly belong to the class 