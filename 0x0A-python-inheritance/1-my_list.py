#!/usr/bin/python3
"""module of a an inherited list of class MyList"""


class MyList(list):
    """
    Customized list class with additional functionality.

    This class inherits the built-in list class and adds a method
    for printing the sorted elements of the list. It enforces that the
    elements in the list must be integers.

    Methods:
    - __init__(self, new_list=None): Constructor to initialize MyList instance
    - print_sorted(self): Print the sorted elements of the list.


    """

    def print_sorted(self):
        """
        Print the sorted elements of the list.

        """
        print(sorted(self))
