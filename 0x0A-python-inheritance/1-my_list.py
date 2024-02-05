#!/usr/bin/python3
"""Defines a class that inherits from list."""


class MyList(list):
    """A class that inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order."""
        print(sorted(self))
