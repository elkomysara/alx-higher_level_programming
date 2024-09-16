#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with an unimplemented area method
and an integer validator method.
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
