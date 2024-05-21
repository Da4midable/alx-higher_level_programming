#!/usr/bin/python3
"""
Module: file_writer

A module providing a function for writing text to a file.

Functions:
- write_file(filename="", text=""): Write the specified text to specified file
and returns number of characters written

"""


def write_file(filename="", text=""):
    """
    Write the specified text to the specified file.

    Parameters:
    - filename (str, optional): path to the file where text will be written.
      If not provided, an empty string is used, and the user can specify file
      when calling the function.
    - text (str, optional): The text to be written to the file.
      If not provided, an empty string is used.

    Usage:
    >>> write_file('output.txt', 'Hello, World!')
    Writes 'Hello, World!' to the 'output.txt' file.

    >>> write_file(text='Lorem ipsum')
    Prompts user to enter file path and writes 'Lorem ipsum' to specified file
    """
    with open(filename, 'w') as file:
        return file.write(text)
