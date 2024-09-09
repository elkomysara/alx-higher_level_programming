#!/usr/bin/python3
"""
This module contains a function to add two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, casting floats to integers.
    
    Args:
        a (int, float): The first number.
        b (int, float): The second number, default is 98.
    
    Returns:
        int: The sum of a and b, cast to integers if necessary.
    
    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast to int before adding
    return int(a) + int(b)
