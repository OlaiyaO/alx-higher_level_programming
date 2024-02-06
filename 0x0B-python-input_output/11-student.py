#!/usr/bin/python3
"""
Defines a student class with methods to save to and reload from a JSON file.
"""


import json


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

    def reload_from_json(self, json):
        """
        Replaces attributes of Student with the values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute values to reload.

        Returns:
            None
        """
        for key, value in json.items():
            setattr(self, key, value)
