#!/usr/bin/python3
"""
Creates an Object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
