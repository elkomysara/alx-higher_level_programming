#!/usr/bin/python3
"""Function that returns the dictionary description for JSON serialization."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure.

    Args:
        obj: The object instance to serialize.

    Returns:
        Dictionary representation of the object for JSON serialization.
    """
    return obj.__dict__
