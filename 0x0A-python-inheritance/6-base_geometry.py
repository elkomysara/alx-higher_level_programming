#!/usr/bin/python3
"""
Module 6-base_geometry
Defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")
