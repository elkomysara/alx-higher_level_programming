#!/usr/bin/python3
"""Defines a base class for all other classes in this project."""
import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set.

        Args:
            **dictionary (dict): Key/value pairs of attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Create a dummy Rectangle
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Create a dummy Square
        dummy.update(**dictionary)  # Update the dummy instance
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file.

        Reads from a file named <Class name>.json.
        Returns:
            - A list of instances (Rectangle/Square).
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as f:
            json_data = f.read()
            list_dicts = cls.from_json_string(json_data)
            return [cls.create(**d) for d in list_dicts]
