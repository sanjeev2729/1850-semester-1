# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
class Circle(Shape):
    """
    A Circle shape.
    """

    def __init__(self, position, colour, radius):
        """
        Creates a Circle with the specified position, colour & radius.
        """
        super().__init__(position, colour)
        self.set_radius(radius)

    def set_radius(self, radius):
        """
        Sets this Circle's radius to the given value.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        if radius <= 0:
            raise ValueError("radius must be positive")

        self.radius = radius

# Make sure that it inherits properly from Shape!
    def __str__(self):
        return f"Circle(position={self.position}, colour={self.colour}, radius={self.radius})"

    def area(self):
        """
        Returns the area of this Circle.
        """
        return math.pi * self.radius ** 2
    def perimeter(self):
        """
        Returns the perimeter of this Circle.
        """
        return 2 * math.pi * self.radius