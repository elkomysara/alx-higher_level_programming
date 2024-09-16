#!/usr/bin/python3
"""
Module 100-my_int
Defines a rebel class MyInt that inherits from int
"""


class MyInt(int):
    """
    MyInt is a rebel class that inverts == and != operators
    """
    def __eq__(self, other):
        """
        Override the == operator with != behavior
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator with == behavior
        """
        return super().__eq__(other)
