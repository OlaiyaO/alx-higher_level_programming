#!/usr/bin/python3
"""Define a class MagicClass."""


class MagicClass:
    """Represent a class that mimics a given Python bytecode."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int): The radius of the MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return self.__radius ** 2 * 3.14159265359

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return 2 * 3.14159265359 * self.__radius
