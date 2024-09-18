#!/usr/bin/python3
"""Defines a base class for all other classes in this project."""
import json
import csv
import turtle

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
    def draw(list_rectangles, list_squares):
        """Draws all Rectangles and Squares using the turtle module."""
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        pen = turtle.Turtle()
        pen.speed(1)  # Set the drawing speed (1 is slow, 10 is fast)

        # Draw rectangles
        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, -rect.y)  # Adjusting the position
            pen.pendown()
            pen.begin_fill()
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)
            pen.end_fill()

        # Draw squares
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, -square.y)
            pen.pendown()
            pen.begin_fill()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)
            pen.end_fill()

        turtle.done()

    # Other methods of the Base class...

