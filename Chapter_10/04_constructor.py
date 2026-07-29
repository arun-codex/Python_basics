class Employee:
    language = "python"   # This is a class attribute
    salary = 120000

    def __init__(self, name, salary, language):       # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

arun = Employee("Arun", 130000, "JavaScripy")
# arun.name = "Arun"
print(arun.name, arun.salary, arun.language)


