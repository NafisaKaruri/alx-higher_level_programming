#!/usr/bin/python3
"""defines the matrix_divided method"""


def matrix_divided(matrix, div):
    """divided matrix by div"""
    err = "matrix must be a matrix (list of lists) of integers/floats"

    # division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # div isn't a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # matrix isn't a matrix
    if not matrix or not isinstance(matrix, list):
        raise TypeError(err)
    # matrix isn't a list of list of ints or floats
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(err)

    # matrix rows aren't of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in row] for row in matrix]
