#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Checks if an object is an instance of a class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of, or if obj is an instance of a class
    that inherited from, the specified class; False otherwise.
    """
    return isinstance(obj, a_class)
