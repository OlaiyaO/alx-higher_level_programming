#!/usr/bin/python3
"""
Module to add two integers
"""


def add_integer(a, b=98):
    """Function to add two integers

    Args:
        a (int): First integer
        b (int): Second integer (default is 98)

    Returns:
        int: Sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
