#!/usr/bin/python3


def add_integer(a, b=98):
    """Adds two intrgers and returns value

    Args:
        a (int): first unteger
        b (int, optional): second integer. Defaults to 98.

    Raises:
        TypeError: if either a or b is neither an interger or float

    Returns:
        int: addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
       
    
