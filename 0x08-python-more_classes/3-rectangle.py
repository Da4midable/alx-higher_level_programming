#!/usr/bin/python3
"""A module for square"""


class Rectangle:
    """Rectangle class with a method to print a rectangle."""
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

    def area(self):
        """ returns the area of a rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """ returns the area of a rectangle"""
        result = self.__height + self.__width
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (2 * result)

    def __str__(self):
        """prints the rectangle with the character #"""
        result = ""
        for x in range(0, self.height):
            result += "#" * self.width
            if x < self.height - 1:
                result += "\n"
        if self.height == 0:
            result += "\n"
        if self.__height == 0 or self.__width == 0:
            return ""
        return result
