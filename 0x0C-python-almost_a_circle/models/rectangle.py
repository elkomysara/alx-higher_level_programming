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
    # (Code omitted for brevity - include same getter/setters from previous task)

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance with the character `#` taking care of x and y."""
        print("\n" * self.y, end="")  # Print the y number of newlines for vertical padding
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)  # Print the x spaces for horizontal padding, followed by # for the rectangle

    def __str__(self):
        """Override the __str__ method to return a specific string format."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
