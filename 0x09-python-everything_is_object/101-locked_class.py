#!/usr/bin/python3
"""Module containing LockedClass."""


class LockedClass:
    """
    A class that prevents the dynamic creation of new instance attributes,
    except for 'first_name'.

    Attributes:
        first_name (str): The allowed instance attribute.
    """

    __slots__ = ('first_name',)
