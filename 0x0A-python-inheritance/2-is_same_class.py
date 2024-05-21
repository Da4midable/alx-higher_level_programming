#!/usr/bin/python3
"""

A module containing a function to check if an object is of a specific class.

Functions:
- is_same_class(obj, a_class): Check if object type is same as specified class

Usage:
>>> from my_module import is_same_class

>>> obj_instance = MyClass()
>>> is_same_class(obj_instance, MyClass)
True

>>> other_instance = OtherClass()
>>> is_same_class(other_instance, MyClass)
False
"""


def is_same_class(obj, a_class):

    """
    Check if the type of an object is the same as a specified class.

    Parameters:
    - obj: Any Python object to check.
    - a_class: class to compare the object type with

    Returns:
    True if object type is the same as the specified class, False otherwise.

    Example:
    >>> from my_module import is_same_class

    >>> obj_instance = MyClass()
    >>> is_same_class(obj_instance, MyClass)
    True

    >>> other_instance = OtherClass()
    >>> is_same_class(other_instance, MyClass)
    False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
