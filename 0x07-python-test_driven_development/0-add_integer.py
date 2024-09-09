#!/usr/bin/python3
"""
This is the "0-add_integer" module.
It provides one function: add_integer(a, b).
This function adds two integers or floats.
"""
def add_integer(a, b=98):
    """
    Return the sum of two integers or floats as integers.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
