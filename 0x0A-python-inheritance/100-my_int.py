#!/usr/bin/python3
"""

A module containing the `MyInt` class, a custom integer class with modified
equality and inequality behavior.

Classes:
- MyInt: custom integer class with overridden equality and inequality methods.

"""


class MyInt(int):
    """
    MyInt class, a custom integer class with modified equality
    and inequality behavior.

    This class inherits from the built-in `int` class in Python but provides
    a different behavior for equality and inequality comparisons
    by considering only the real part.

    Methods:
    - __eq__(self, value): Override of the equality comparison operator (`==`).
      Returns True if the real part of the MyInt object is not equal to
      the given value; False otherwise.

    - __ne__(self, value): Override of inequality comparison operator (`!=`).
      Returns True if the real part of the MyInt object is equal to the given
      value; False otherwise.

    Usage:
    >>> from my_module import MyInt

    >>> custom_int = MyInt(5)
    >>> result = custom_int == 5
    >>> print(result)
    False

    >>> result = custom_int != 5
    >>> print(result)
    True
    """

    def __eq__(self, value):
        """
        Override of the equality comparison operator (`==`).

        Returns True if the real part of the MyInt object is not equal to
        the given value; False otherwise.

        Parameters:
        - value: The value to compare with the real part of the MyInt object.

        Returns:
        - bool: True if the real part is not equal to the value;
        False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override of the inequality comparison operator (`!=`).

        Returns True if the real part of the MyInt object is equal to
        the given value; False otherwise.

        Parameters:
        - value: The value to compare with the real part of the MyInt object.

        Returns:
        - bool: True if the real part is equal to the value; False otherwise.
        """
        return self.real == value
