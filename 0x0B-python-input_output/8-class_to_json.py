#!/usr/bin/python3
"""
Returns the description with data structure for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the description with data structure for JSON serialization.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
