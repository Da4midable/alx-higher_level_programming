#!/usr/bin/python3
"""
Module: my_module
~~~~~~~~~~~~~~~~~

Module providing a function to convert a Python object to JSON representation

Functions:
- to_json_string(my_obj): Return the JSON representation of a Python object.

"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of a Python object.

    This function uses `json.dumps` method to serialize given Python object
    to its JSON representation.

    Args:
    - my_obj: The Python object to be serialized.

    Returns:
    - str: The JSON representation of the object.

    Example:
    >>> from my_module import to_json_string

    >>> my_list = [1, 2, 3]
    >>> json_list = to_json_string(my_list)
    >>> print(json_list)
    "[1, 2, 3]"

    >>> my_dict = {'key': 'value', 'number': 42}
    >>> json_dict = to_json_string(my_dict)
    >>> print(json_dict)
    '{"key": "value", "number": 42}'

    """
    json_rep = json.dumps(my_obj)
    return json_rep
