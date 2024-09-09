#!/usr/bin/python3
"""Define a class MagicClass to calculate area and circumference."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize the MagicClass.

        Args:
            radius (int, float): The radius of the circle. Defaults to 0.

        Raises:
            TypeError: If radius is not an integer or float.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the circle."""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Return the circumference of the circle."""
        return 2 * math.pi * self.__radius
