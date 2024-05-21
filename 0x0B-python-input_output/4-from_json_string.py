#!/usr/bin/python3
"""
Module: json_utils
~~~~~~~~~~~~~~~~~~
A utility module for handling JSON data in Python.

Functions:
- from_json_string(my_str): Deserialize JSON-formatted string to Python object

"""

import json


def from_json_string(my_str):
    """
    Deserialize a JSON-formatted string to a Python object.

    Parameters:
    - my_str (str): The JSON-formatted string to be deserialized.

    Returns:
    - object: The Python object resulting from deserialization.

    Example:
    >>> import json_utils
    >>> json_string = '{"key": "value", "number": 42}'
    >>> python_obj = json_utils.from_json_string(json_string)
    >>> print(python_obj)
    {'key': 'value', 'number': 42}
    """
    return json.loads(my_str)
