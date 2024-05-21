#!/usr/bin/python3
"""

A module containing the `Rectangle` class, which inherits from `BaseGeometry`.

Classes:
- Rectangle: A class representing a rectangle with width and height.

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class representing a rectangle with width and height.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.

    Methods:
    - __init__(self, width, height): Constructor method to initialize
    a Rectangle object with a given width and height.

    Usage:
    >>> from my_module import Rectangle

    >>> rectangle_instance = Rectangle(10, 5)
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle object with a given width and height.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.

        Raises:
        - TypeError: If width or height is not an integer.
        - ValueError: If width or height is less than or equal to 0.

        Usage:
        >>> from my_module import Rectangle

        >>> rectangle_instance = Rectangle(10, 5)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
