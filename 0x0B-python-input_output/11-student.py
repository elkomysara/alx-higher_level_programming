#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.
        
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.
        
        If attrs is a list of strings, only attributes included in this
        list will be retrieved. Otherwise, all attributes will be retrieved.
        """
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        
        Args:
            json (dict): A dictionary containing new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
