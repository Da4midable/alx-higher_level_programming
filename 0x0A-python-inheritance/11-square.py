#!/usr/bin/python3
"""

A module containing the `Square` class, which inherits
the `Rectangle` class.

Classes:
- Square: A class representing a square with equal sides.

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class representing a square with equal sides,
    inheriting the `Rectangle` class.

    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size): Constructor method to initialize a Square object
    with a given size.

    """

    def __init__(self, size):
        """
        Initialize a Square object with a given size.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than or equal to 0.

        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

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
        formatted as "[ClassName] size/size".

        Example:
        >>> square = Square(6, 6)
        >>> print(square)
        [Square] 6/6
        """
        string = "[" + (self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
