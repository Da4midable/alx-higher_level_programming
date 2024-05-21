#!/usr/bin/python3
"""
Module: file_reader
~~~~~~~~~~~~~~~~~~

A module containing a function to read and print the content of a file.

Functions:
- read_file(filename=""): Reads and prints the content of a file.

"""


def read_file(filename=""):
    """
    Read and print the content of a file.

    Parameters:
    - filename (str, optional): The path to the file to be read.
      If not provided, an empty string is used, and the user can specify file
      when calling the function.

    Raises:
    - FileNotFoundError: If the specified file is not found.

    Usage:
    >>> read_file('example.txt')
    Reads and prints the content of the 'example.txt' file.

    >>> read_file()
    Prompts the user to enter a file path and reads and prints
    the content of the specified file.
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        file_content = file.read()
        print(file_content[:-1])
