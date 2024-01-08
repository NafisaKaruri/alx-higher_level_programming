#!/usr/bin/python3
"""Defines Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class: child of Rectangle with
    __init__ and area methods"""

    def __init__(self, size):
        """
        initializes the attributes
        attribute:
            size (int): private +ve int, defines the size of square
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        The implementation of the area method
        Returns: the area of the Square
        """
        return super().area()

    def __str__(self):
        """The string representation of Square"""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
