#!/usr/bin/python3
"""module of a function that looks up an object's attribute"""


def lookup(obj):
    """
    Retrieve the list of attributes and methods of an object.

    This function takes an object as an argument and returns a list
    containing the names of attributes and methods associated with the object.

    Parameters:
    - obj: Any Python object whose attributes and methods are to be retrieved.

    Returns:
    A list containing the names of attributes and methods of the given object.

    """
    return dir(obj)
