#!/usr/bin/python3
"""Module defining MyInt class"""


class MyInt(int):
    """Class MyInt inherits from int"""

    def __eq__(self, other):
        """Inverted equality check"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted inequality check"""
        return super().__eq__(other)
