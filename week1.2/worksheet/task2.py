# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers()

if len(numbers) == 0:
    sys.exit("Error: no numbers provided")

numbers.sort()
count = len(numbers)
middle = count // 2
if count % 2 != 0:
    median = numbers[middle]
else:
    median = (numbers[middle - 1] + numbers[middle]) / 2

print("Minimum =" , min(numbers))
print("Maximum =" , max(numbers))
print("Median =" , median)
print("Mean =" , sum(numbers) / count)
