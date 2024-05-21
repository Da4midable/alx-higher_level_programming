#!/usr/bin/python3
"""A module for square"""


class Square:
    """Square class with a method to print a square.

    Attributes:
        __size (int): The length of the side of the square.

    Methods:
        __init__(self, size=0): Constructor to initialize the Square instance.
    """

    def __init__(self, size=0):
        """Constructor.

        Args:
            size (int): Length of side of the square.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
