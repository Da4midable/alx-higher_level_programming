#!/usr/bin/python3
"""
Module: my_module
~~~~~~~~~~~~~~~~~

A module containing a base class for geometry-related functionality.

Classes:
- BaseGeometry: A base class for geometry-related functionality.

Usage:
>>> from my_module import BaseGeometry

>>> geometry_instance = BaseGeometry()
>>> geometry_instance.area()
Traceback (most recent call last):
  ...
Exception: area() is not implemented
"""


class BaseGeometry:
    """
    A base class for geometry-related functionality.

    This class provides a foundation for building geometry-related classes.
    It defines a placeholder method 'area()' that raises an exception,
    indicating that the method needs to be implemented by derived classes.

    Methods:
    - area(): Placeholder method for calculating the area of a geometry.
    Must be implemented by derived classes.

    - integer_validator(name, value): Validate that a value is an integer
    greater than 0, raising appropriate errors if conditions are not met.

    Usage:
    >>> from my_module import BaseGeometry

    >>> geometry_instance = BaseGeometry()
    >>> geometry_instance.area()
    Traceback (most recent call last):
      ...
    Exception: area() is not implemented
    """

    def area(self):
        """
        Placeholder method for calculating the area of a geometry.

        This method should be implemented by derived classes to provide
        specific functionality for calculating the area of a geometry.

        Raises:
        - Exception: Indicates that the method is not implemented
        in the base class.

        Example:
        >>> from my_module import BaseGeometry

        >>> geometry_instance = BaseGeometry()
        >>> geometry_instance.area()
        Traceback (most recent call last):
          ...
        Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is an integer greater than 0.

        Parameters:
        - name (str): The name of the value for error messages.
        - value: The value to be validated.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.

        Example:
        >>> from my_module import BaseGeometry

        >>> geometry_instance = BaseGeometry()
        >>> geometry_instance.integer_validator("side_length", 5)
        >>> geometry_instance.integer_validator("side_length", "invalid")
        Traceback (most recent call last):
          ...
        TypeError: side_length must be an integer
        >>> geometry_instance.integer_validator("side_length", -3)
        Traceback (most recent call last):
          ...
        ValueError: side_length must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
