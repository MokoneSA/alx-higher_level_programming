#!/usr/bin/python3
"""Define a rectangle class"""
from base import Base


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

    @property
    def width(self):
        """set/get the width of the Rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self):
        """set/get the height of the Rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @property
    def x(self):
        """set/get the x of the Rectangle"""
        return self._x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
            self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height
