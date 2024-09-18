#!/usr/bin/python3
"""Defines a base class for all other classes in this project."""
import json
import csv
import os


class Base:
    """Represents the base model."""

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
        """Return an instance with all attributes set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Dummy instance for Rectangle
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Dummy instance for Square
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as f:
            json_data = f.read()
            list_dicts = cls.from_json_string(json_data)
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV string representation of list_objs to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if list_objs is None or len(list_objs) == 0:
                writer.writerow([])
            else:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            instances = []
            for row in reader:
                if cls.__name__ == "Rectangle":
                    obj_dict = {
                        'id': int(row[0]),
                        'width': int(row[1]),
                        'height': int(row[2]),
                        'x': int(row[3]),
                        'y': int(row[4])
                    }
                elif cls.__name__ == "Square":
                    obj_dict = {
                        'id': int(row[0]),
                        'size': int(row[1]),
                        'x': int(row[2]),
                        'y': int(row[3])
                    }
                instance = cls.create(**obj_dict)
                instances.append(instance)
            return instances
