#!/usr/bin/python3
"""
Module: my_module
~~~~~~~~~~~~~~~~~

A module containing a class and a function for working with student data.

Classes:
- Student: A class representing a student with first name, last name, and age.

Functions:
- to_json(obj): Convert an object to a JSON representation.

"""


class Student:
    """
    Student class representing a student with first name, last name, and age.

    Attributes:
    - first_name (str): The first name of the student.
    - last_name (str): The last name of the student.
    - age (int): The age of the student.

    Methods:
    - to_json(): Convert the student object to a JSON representation.

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

    def to_json(self):
        """
        Convert the student object to a JSON representation.

        Returns:
        - dict: A dictionary representing the attributes of the student.

        Example:
        >>> student_instance = Student("John", "Doe", 20)
        >>> json_representation = student_instance.to_json()
        >>> print(json_representation)
        {'first_name': 'John', 'last_name': 'Doe', 'age': 20}
        """
        return self.__dict__
