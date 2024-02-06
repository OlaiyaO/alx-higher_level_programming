#!/usr/bin/python3
"""
Reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
