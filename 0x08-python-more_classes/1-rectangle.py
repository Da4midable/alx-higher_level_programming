#!/usr/bin/python3
"""A module for square"""


class Rectangle:
    """Rectangle class with a method to print a square."""
    def __init__(self, width=0, height=0):
        """Constructor.
        Args:
            width: width of the rectangle.
            height: height of rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter method."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setter method."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setter method."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
