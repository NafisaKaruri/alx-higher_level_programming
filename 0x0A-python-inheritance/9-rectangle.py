#!/usr/bin/python3
"""Defines Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class: child of BaseGeomtry with:
        __init__, __str__, area methods
    """

    def __init__(self, width, height):
        """
        initializes the attributes
        attributes:
            width (int): private +ve int, defines the width of Rectangle
            height (int): private +ve int, defines the height of Rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """string representation of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        The implementation of the area method
        Returns: the area of the Rectangle
        """
        return self.__width * self.__height
