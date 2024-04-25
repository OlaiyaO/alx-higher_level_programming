#!/usr/bin/python3
"""
This module contains a function that finds a peak in a lists.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of integers.

    Returns:
        int: A peak integer in the list.
    """
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    mid = length // 2
    peak = list_of_integers[mid]
    if (mid == length - 1 or peak >= list_of_integers[mid + 1]) and \
       (mid == 0 or peak >= list_of_integers[mid - 1]):
        return peak
    elif mid != length - 1 and list_of_integers[mid + 1] > peak:
        return find_peak(list_of_integers[mid + 1:])
    else:
        return find_peak(list_of_integers[:mid])
