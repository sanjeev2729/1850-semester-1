# Worksheet 1.2: Task 1 Solution
import sys
grade = input("Enter your grade (0-100): ")
if not grade.isdigit():
    sys.exit("Invalid input. Please enter a number between 0 and 100.")

grades = int(grade)
if grades >= 70:
    result = " Distinction"
elif grades >= 40:
    result = " Pass"
else:
    result = " Fail"
print(grades, "is a", result)


