#!/usr/bin/python3
"""Extends BaseGeometry with a method integer_validator(self, name, value)"""


class BaseGeometry:
    """A class with an area method and an integer_validator method."""

    def area(self):
        """Raises an Exception with the message 'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
