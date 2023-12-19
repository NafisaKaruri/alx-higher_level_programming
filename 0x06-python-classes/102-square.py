#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
    Class that defines a square.

    Attributes:
        size: size of the square.
    """
    def __init__(self, size=0):
        """
        Create a new instanse of the square.
        Args:
            size: size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size.

        Args:
            value (int): size of the square.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def ___lt__(self, other):
        """Compares if square's area is less than another square.

        Args:
            other (Square): square to be compared with this square.

        Returns: bool (True or False)
        """
        return self.__size < other.__size

    def __le__(self, other):
        """Compares if square's area is less than or equal another square.

        Args:
            other (Square): square to be compared with this square.

        Returns: bool (True or False)
        """
        return self.__size <= other.__size

    def __eq__(self, other):
        """Compares if square's area equal to another square.

        Args:
            other (Square): square to be compared with this square.

        Returns: bool (True or False)
        """
        return self.__size == other.__size

    def __ne__(self, other):
        """Compares if square's area is not equal to another square.

        Args:
            other (Square): square to be compared with this square.

        Returns: bool (True or False)
        """
        return self.__size != other.__size

    def __gt__(self, other):
        """Compares if square's area is greater than another square.

        Args:
            other (Square): square to be compared with this square.

        Returns: bool (True or False)
        """
        return self.__size > other.__size

    def __ge__(self, other):
        """Compares if square's area is greater than or equal another square.

        Args:
            other (Square): square to be compared with this square.

        Returns: bool (True or False)
        """
        return self.__size >= other.__size
