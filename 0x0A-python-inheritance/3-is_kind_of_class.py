#!/usr/bin/python3
"""
A module for checking if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class.

Funciton:
- is_kind_of_class: checks if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    checks if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class.

    Parameters:
    - obj: Any Python object to check.
    - a_class: class to compare the object type with

    Returns:
    True if object type is an instance of the specified class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
