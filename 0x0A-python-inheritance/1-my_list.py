#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList that inherits from list
"""


class MyList(list):
    """Inherits from list and has a method to print sorted list"""

    def print_sorted(self):
        """Prints the list, sorted in ascending order"""
        print(sorted(self))


