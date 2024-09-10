#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The module provides one function: text_indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_spaces = False

    for char in text:
        if skip_spaces and char == " ":
            continue
        result += char
        if char in ".:?":
            result += "\n\n"
            skip_spaces = True
        else:
            skip_spaces = False
    
    print(result.strip(), end="")
