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

    new_text = ""
    i = 0
    while i < len(text):
        new_text += text[i]
        if text[i] in ".:?":
            new_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    print(new_text, end="")
