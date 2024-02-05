#!/usr/bin/python3
"""A definition for a function that looks up object attribute"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
