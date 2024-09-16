#!/usr/bin/python3
"""
Module 10-square
Inherits from Rectangle and initializes size with validation.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Defines a square using Rectangle"""

    def __init__(self, size):
        """Initialize size after validation"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
