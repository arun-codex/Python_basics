class Employee:
    language = "python"   # This is a class attribute
    salary = 120000


arun = Employee()
arun.language = "JavaScript"       # This is an instance attribute 
arun.language = "Java"
print(arun.language, arun.salary)
