#!/usr/bin/python3
"""Extends BaseGeometry with a method area(self)"""


class BaseGeometry:
    """A class with an area method that raises an Exception."""

    def area(self):
        """Raises an Exception with the message area() is not implemented."""
        raise Exception("area() is not implemented")
