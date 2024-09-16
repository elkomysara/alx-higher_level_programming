#!/usr/bin/python3
"""
Module 101-add_attribute
Defines a function that adds a new attribute to an object if it's possible
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible

    Args:
        obj: The object to add the attribute to
        attr: The name of the attribute
        value: The value of the attribute

    Raises:
        TypeError: If the object cannot have new attributes
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
