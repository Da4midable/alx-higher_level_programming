#!/usr/bin/python3
"""

A module for checking if an object inherits from a specific class.

Functions:
- inherits_from(obj, a_class): Checks if object inherits from a specific class.

Usage:
>>> from my_module import inherits_from

>>> obj_instance = MyClass()
>>> inherits_from(obj_instance, Animal)
True

>>> fish_instance = Fish()
>>> inherits_from(fish_instance, Animal)
False
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specific class.

    Parameters:
    - obj: Any Python object to check.
    - a_class: The class to check if the object inherits from.

    Returns:
    True if the object is an instance of a subclass of the specified class,
    False otherwise.

    Example:
    >>> from my_module import inherits_from

    >>> obj_instance = MyClass()
    >>> inherits_from(obj_instance, Animal)
    True

    >>> fish_instance = Fish()
    >>> inherits_from(fish_instance, Animal)
    False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
