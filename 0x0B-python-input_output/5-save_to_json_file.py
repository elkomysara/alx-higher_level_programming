#!/usr/bin/python3
"""Defines a function for saving an object to a file using JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using its JSON representation.

    Args:
        my_obj (object): The object to save.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
