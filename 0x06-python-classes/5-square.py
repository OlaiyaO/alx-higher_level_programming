#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
