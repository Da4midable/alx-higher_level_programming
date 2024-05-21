#!/usr/bin/python3
"""
Module: json_utils
~~~~~~~~~~~~~~~~~~
A utility module for handling JSON data in Python.

Functions:
- save_to_json_file(my_obj, filename): Serialize a Python object
and save it to a JSON file.

"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serialize a Python object and save it to a JSON file.

    Parameters:
    - my_obj (object): The Python object to be serialized.
    - filename (str): The name of the JSON file to save the serialized data.

    Returns:
    - None

    Example:
    >>> import json_utils
    >>> data_to_save = {"key": "value", "number": 42}
    >>> json_utils.save_to_json_file(data_to_save, "output.json")
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
