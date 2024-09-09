#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """
    Return the addition of two numbers.

    Args:
        a (int, float): The first number.
        b (int, float): The second number (default is 98).

    Returns:
        int: The sum of a and b, after casting to integers if necessary.

    Raises:
        TypeError: If a or b is not an integer or float.
        ValueError: If float NaN or infinity is passed.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float) and (a != a or a in [float('inf'), -float('inf')]):
        raise ValueError("cannot convert float NaN or infinity to integer")
    if isinstance(b, float) and (b != b or b in [float('inf'), -float('inf')]):
        raise ValueError("cannot convert float NaN or infinity to integer")

    # Cast both a and b to int before performing the addition
    return int(a) + int(b)
