# Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the user

# taking marks from user
python_marks = int(input("Enter your marks in Python: "))
java_marks = int(input("Enter your marks in java: "))
c_marks = int(input("Enter your marks in C: "))

percentage = (python_marks+java_marks+c_marks)/3
# checking the pass or fail status of student 
if percentage >= 40 and python_marks >= 33 and java_marks >= 33 and c_marks >= 33:
    print(f"Your overall percentage: {percentage:.2f}%")
    print("Pass")
else:
    print(f"Your overall percentage: {percentage:.2f}%")
    print("Fail")
    print("Better luck next time")
# end
