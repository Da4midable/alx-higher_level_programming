#!/usr/bin/python3
"""
Module: my_module
~~~~~~~~~~~~~~~~~

A module containing a class and a function for working with student data.

Classes:
- Student: A class representing a student with first name, last name, and age.

Functions:
- to_json(obj, attrs=None): Convert an object to a JSON representation.

"""


class Student:
    """
    Student class representing a student with first name, last name, and age.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.

    Methods:
    - to_json(attrs=None): Convert the student object to a JSON representation.

    Example:
    >>> student_instance = Student("John", "Doe", 20)
    >>> json_representation = student_instance.to_json()
    >>> print(json_representation)
    {'first_name': 'John', 'last_name': 'Doe', 'age': 20}
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student object with first name, last name, and age.

        Parameters:
        - first_name (str): The first name of the student.
        - last_name (str): The last name of the student.
        - age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Convert the student object to a JSON representation.

        Parameters:
        - attrs (list, optional): A list of attribute names to include
          in the JSON representation. If not provided, include all attributes.

        Returns:
        - dict: A dictionary representing specified attributes of the student.


        """
        if (type(attrs) == list and
                all(type(elmnt) == str for elmnt in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__
