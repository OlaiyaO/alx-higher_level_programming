#!/usr/bin/python3
"""
This module contains a function that finds a peak in a lists.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in list_of_integers

    Args:
        list_of_integers (list): List of integers.

    Returns:
        int: A peak integer in the list.
    """
    if list_of_integers is None or list_of_integers == []:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    lo = 0
    hi = length
    while lo < hi:
        mid = (lo + hi) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and \
           (mid == length - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return None
