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

    def area(self):
        """Returns the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """
        Return the string representation of the object for printing
        and conversion to a string.

        This method is called when using the print() function or str() function
        on an instance of the class. It provides a human-readable string
        that includes the class name in square brackets followed by the width
        and height values separated by a forward slash.

        Returns:
        - str: A string representation of the object,
        formatted as "[ClassName] width/height".

        Example:
        >>> rectangle = Rectangle(4, 6)
        >>> print(rectangle)
        [Rectangle] 4/6
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
