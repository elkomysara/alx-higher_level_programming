#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Returns the addition of two integers or floats casted to integers.

    Args:
        a: The first number to add (integer or float).
        b: The second number to add (integer or float, defaults to 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b are not integers or floats.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
