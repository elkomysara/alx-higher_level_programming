#!/usr/bin/python3
"""Defines a function for converting an object to its JSON representation."""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to convert to JSON.
    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
