#!/usr/bin/python3
"""
Module 9-rectangle
Inherits from BaseGeometry and initializes width and height with validation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Defines a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize width and height after validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
