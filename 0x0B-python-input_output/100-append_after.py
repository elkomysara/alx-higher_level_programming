#!/usr/bin/python3
"""Defines a function that inserts text after lines containing a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specific string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert after each occurrence of search_string.
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
