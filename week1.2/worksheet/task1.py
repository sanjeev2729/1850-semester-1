# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter the grade (range from 0 to 100): ")
if not grade.isdigit():
        sys.exit("Error: Grade must be an integer between 0 and 100.")

grades = int(grade)
if 0 > grades or grades > 100:
    sys.exit("Error: Grade must be an integer between 0 and 100.")

if  grades >= 70:
    print(grades, "is a Distinction")
elif grades >= 40:
    print(grades, "is a Pass")
else:
    print(grades, "is a Fail")



