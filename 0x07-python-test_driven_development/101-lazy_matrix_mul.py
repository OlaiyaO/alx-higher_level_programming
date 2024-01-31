#!/usr/bin/python3
"""Module to perform matrix multiplication using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiply two matrices using NumPy

    Args:
    m_a (list): First matrix
    m_b (list): Second matrix

    Returns:
    list: The resulting matrix
    """

    return np.dot(m_a, m_b).tolist()
