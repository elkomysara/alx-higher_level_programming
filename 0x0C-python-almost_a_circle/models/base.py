#!/usr/bin/python3
"""Defines a base class for all other classes in this project."""
import json


class Base:
    """Represents the base model.

    This class will be the “base” of all other classes in this project.
    Manages the id attribute to avoid duplicating the same code.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation.

        Args:
            json_string (str): A string representing a list of dictionaries.
        
        Returns:
            list: A list represented by json_string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))
