#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method to return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
