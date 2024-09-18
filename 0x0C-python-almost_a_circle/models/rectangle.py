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

    # Getters and Setters for each attribute (Same as previous tasks)
    # (Code omitted for brevity - include same getter/setters from previous tasks)

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

    def update(self, *args):
        """Update attributes with non-keyword arguments."""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
