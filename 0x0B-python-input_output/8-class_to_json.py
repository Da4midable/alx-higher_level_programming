#!/usr/bin/python3
"""Module for converting a class instance to a JSON representation.
"""


def class_to_json(obj):
    """
    Convert a class instance to a JSON representation.

    Parameters:
    - obj: The instance of a class to be converted.

    Returns:
    - dict: A dictionary representing the attributes of the class instance.

    Example:
    >>> class MyClass:
    ...     def __init__(self, name, age):
    ...         self.name = name
    ...         self.age = age
    ...
    >>> obj = MyClass("John", 25)
    >>> json_representation = class_to_json(obj)
    >>> print(json_representation)
    {'name': 'John', 'age': 25}
    """
    return obj.__dict__
