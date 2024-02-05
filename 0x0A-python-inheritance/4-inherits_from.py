#!/usr/bin/python3
"""Returns True if the object is an instance, otherwise False."""


def inherits_from(obj, a_class):
    """An instance of a class that inherited (directly or indirectly)."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
