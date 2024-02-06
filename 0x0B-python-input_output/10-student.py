#!/usr/bin/python3
"""
Defines and retrieves a dictionary ofa student instance with filtering.
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

    def to_json(self, attrs=None):
        """
        Retrieves a student instance with optional filtering.

        Args:
            attrs (list, optional): A list of attribute in the dictionary.
            Defaults to None, which includes all attributes.

        Returns:
            dict: A student instance with filtered attributes.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
