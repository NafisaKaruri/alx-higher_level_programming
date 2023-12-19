#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines a square

    Attributes:
        size: size of the square.
    """
    def __init__(self, size=0):
        """
        Create a new instanse of the square
        Args:
            size: size of the square.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
