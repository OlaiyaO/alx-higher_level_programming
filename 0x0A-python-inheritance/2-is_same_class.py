#!/usr/bin/python3
"""Returns an instance of the specified class"""


def is_same_class(obj, a_class):
    """Returns an instance of the specified class; otherwise False."""
    return type(obj) == a_class
