#!/usr/bin/python3
"""
This module defines a class `Square` with a private instance attribute `size`.
"""
class Square:
    """
    A class that defines a square.
    
    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """
        Initializes the square with the given size.
        
        Args:
            size (int): The size of the square.
        """
        self.__size = size
