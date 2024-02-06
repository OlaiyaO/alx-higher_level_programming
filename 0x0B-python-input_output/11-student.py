#!/usr/bin/python3
"""
Module for Student class
"""


class Student:
    """
    Defines a Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance
        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): list of strings, only attributes names
                          contained in this list must be retrieved
        Returns:
            dict: dictionary representation of the Student instance
        """

        if attrs is None:
            return self.__dict__
        else:
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):

        """
        Replaces all attributes of the Student instance
        Args:
            json (dict): dictionary representation of a Student instance
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(f"Ignoring unknown attribute: {key}")
