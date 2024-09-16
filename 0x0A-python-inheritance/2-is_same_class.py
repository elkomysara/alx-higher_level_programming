#!/usr/bin/python3
"""
Module 2-is_same_class
Checks if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) == a_class
