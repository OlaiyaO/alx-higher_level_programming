#!/usr/bin/python3
"""Definition for a function that divides matrices."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The number to divide the matrix by.

    Returns:
        list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If matrix contains non-numeric elements, div is not a number,
                   or div is equal to 0.
        ValueError: If rows of the matrix have different sizes.
    """
    if (not all(isinstance(row, list) and all(isinstance(el, (int, float))
        for el in row) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")
    return [[round(el / div, 2) for el in row] for row in matrix]
