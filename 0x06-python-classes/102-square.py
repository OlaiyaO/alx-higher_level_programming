#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Check if two squares are equal in area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of the first square is less than the second."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the first square is less than or equal to the second."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of the first square is greater than the second."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the first square is greater than or equal to the second."""
        return self.area() >= other.area()
