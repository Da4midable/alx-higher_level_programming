#!/usr/bin/python3
"""Module for dynamically adds a new attribute to an object."""


def add_attribute(obj, att, value):
    """
    Dynamically adds a new attribute to an object.

    Parameters:
    - obj: The object to which the attribute will be added.
    - att: The name of the new attribute.
    - value: The value to assign to the new attribute.

    Raises:
    - TypeError: If the object does not have a '__dict__' attribute,
    indicating that it does not support the addition of new attributes.

    Usage:
    >>> my_object = MyCustomClass()
    >>> add_attribute(my_object, 'new_attribute', 42)
    >>> print(my_object.new_attribute)
    42
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
