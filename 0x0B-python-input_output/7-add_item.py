#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Try to load the existing list from the file, if it exists
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Add the arguments passed to the script to the list
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
