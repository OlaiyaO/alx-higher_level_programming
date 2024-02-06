#!/usr/bin/python3
"""
Defines a student class and retrieves a dictionary of a student instance.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a student instance.

        Returns:
            dict: A dictionary representation of the student instance.
        """
        return self.__dict__
