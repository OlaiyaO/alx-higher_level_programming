#!/usr/bin/python3
"""
Script to demonstrate serialization and deserialization of a Student object.
"""

import os
import sys

class Student:
    """
    Class defining a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

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
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): Strings specifying the attributes added to the dictionary.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
        return result


    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance using a dictionary.

        Args:
            json (dict): A dictionary containing the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
