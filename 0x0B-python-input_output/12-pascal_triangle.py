#!/usr/bin/python3
"""Defines pascal_triangle method"""


def pascal_triangle(n):
    """
    DISCLAIMER: this function can be more efficient when using :
                C(n, k) = C(n, k-1) * (n-k+1) / k,
                but, unfortunately im too lazy right now.

    This function generates a Pascal's Triangle with n rows.
    Arguments:
    n (int): number of rows.
    Returns:
    tri (list): a matrix representing the Pascal's Triangle.
    """

    if n <= 0:
        return []

    # initialized a triangle matrix with n rows
    tri = [[0 for x in range(y+1)] for y in range(n)]

    # iterating throught matrix
    for i in range(n):
        # iterating throught the matrix's rows
        for j in range(i + 1):
            # the first and last are always 1
            if (j == 0 or j == i):
                tri[i][j] = 1
            # else it is the sum of the two elements above it
            else:
                tri[i][j] = tri[i - 1][j - 1] + tri[i - 1][j]

    # voila, return the Pascal's triangle
    return tri
