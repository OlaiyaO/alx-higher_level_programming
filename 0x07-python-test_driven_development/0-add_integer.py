#!/usr/bin/python3
"""Module to add two integers"""


def add_integer(a, b=98):
    """Function that returns addition of:wq two integers

    Arguments of type Float are casted to integers before addition is done.

    Returns:
        TypeError: If a or b is not an integer or not a float respectively.
    """ 
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
