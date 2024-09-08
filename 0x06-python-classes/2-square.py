#!/usr/bin/python3
"""
This module defines a Square class that represents a square shape with
size validation.
"""
class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of one side of the square.
    """
    def __init__(self, size=0):
        """
        Initializes the square with the given size.
        Args:
            size (int): The size of one side of the square, defaults to 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
