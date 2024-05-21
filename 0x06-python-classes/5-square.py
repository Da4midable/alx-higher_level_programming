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
        """Constructor to initialize a new square.

        Args:
            size (int): Length of new square.
        """

        self.size = size

    @property
    def size(self):
        """Getter method."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of size (int)."""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #."""
        for x in range(0, self.size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
