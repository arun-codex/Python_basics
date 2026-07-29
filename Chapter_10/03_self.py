class Employee:
    language = "python"   # This is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

arun = Employee()
arun.language = "JavaScript"       # This is an instance attribute 
print(arun.language, arun.salary)
arun.getInfo()
# Employee.getInfo(arun)
