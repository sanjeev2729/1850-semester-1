# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from point import Point
from shapes import Circle

c = Circle(Point(0, 0), "red", 5)
print(c)
print(f"Area = {c.area():.3f}")
print(f"Perimeter = {c.perimeter():.3f}")

print("moving circle to (3, 4)")
c.set_position(Point(3, 4))
print(c)

print("changing circle colour to blue")
c.set_colour("blue")
print(c)