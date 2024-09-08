#!/usr/bin/python3
"""
This module defines a Square class that represents a square shape.

The Square class includes a private instance attribute `size` for its dimensions.
"""
class Square:
    """
    A class used to represent a square.

    Attributes:
        __size (int): The size of one side of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with a given size.

        Args:
            size (int): The size of one side of the square.
        """
        self.__size = size
