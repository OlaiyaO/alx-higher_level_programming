#!/usr/bin/python3
"""
Appends at the end of a file (UTF8), returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
