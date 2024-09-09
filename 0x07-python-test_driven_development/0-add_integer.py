#!/usr/bin/python3
"""
This module provides a function `add_integer` to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casting floats to integers).
    
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add (default is 98).
    
    Returns:
        int: The sum of a and b, both cast to integers if necessary.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    
    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
        >>> add_integer("4", 2)
        Traceback (most recent call last):
            ...
        TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast both a and b to int before performing the addition
    return int(a) + int(b)
