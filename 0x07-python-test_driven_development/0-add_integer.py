#!/usr/bin/python3
"""Define the function to sum two integers."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int, float): First number.
        b (int, float): Second number, defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or cannot be cast to int.

    Returns:
        int: Sum of a and b.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")

    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, TypeError):
        raise TypeError("b must be an integer")

    return a + b
