#!/usr/bin/python3
"""Defines matrix_mul method"""



def matrix_mul(m_a, m_b):
    """multiplies two matrices"""
    # check if m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if row == []:
            raise ValueError("m_a can't be empty")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if row == []:
            raise ValueError("m_b can't be empty")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # check if all row are of the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    product = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for x in range(len(m_a)):
        for y in range(len(m_b[0])):
            for z in range(len(m_b)):
                product[x][y] += m_a[x][z] * m_b[z][y]

    return product
