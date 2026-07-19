


# Ask user for marks
marks = int(input("Enter your marks: "))

# Checking the conditon of marks

if marks > 100:
    print("Marks cannot be greater than 100")
elif marks >= 90:
    print("Grade : Excellent")
elif marks >= 80:
    print("Grade : A")
elif marks >= 70:
    print("Grade : B")
elif marks >= 60:
    print("Grade : C")
elif marks >= 50:
    print("Grade : D")
elif marks < 0:
    print("Marks cannot be negative")

else:
    print("Fail")