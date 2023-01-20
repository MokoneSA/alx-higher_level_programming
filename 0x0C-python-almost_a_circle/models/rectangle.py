#!/usr/bin/python3
"""Define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new rectangle

        Args:
            width (int):  width of the new rectangle.
            height (int): height of the nw rectangle.
            x (int): x coordinate of the new rectangle.
            y (int): y coordinate of the new rectangle.
            id (int): identity of the new rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height is <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y is <= 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
