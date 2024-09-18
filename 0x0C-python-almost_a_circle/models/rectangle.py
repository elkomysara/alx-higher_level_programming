#!/usr/bin/python3
"""Defines a Rectangle class that inherits from Base."""
from models.base import Base

class Rectangle(Base):
    """Represents a rectangle, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getters and Setters for each attribute (Code omitted for brevity)

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with the character `#` taking care of x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Override the __str__ method to return a specific string format."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update attributes using *args and **kwargs."""
        if args and len(args) > 0:
            attr_names = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attr_names):
                    setattr(self, attr_names[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
