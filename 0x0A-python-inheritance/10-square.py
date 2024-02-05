#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle with validated props"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that inherits from Rectangle and represents a square."""

    def __init__(self, size):
        """Initializes a Square instance with size."""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
