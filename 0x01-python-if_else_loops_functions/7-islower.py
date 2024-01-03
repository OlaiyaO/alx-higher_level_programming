#!/usr/bin/python3

def islower(c):
    """
    Checks if a character is lowercase.

    Args:
    - c: a character (string of length 1)

    Returns:
    - True if the character is lowercase, False otherwise
    """
    return ord('a') <= ord(c) <= ord('z')
