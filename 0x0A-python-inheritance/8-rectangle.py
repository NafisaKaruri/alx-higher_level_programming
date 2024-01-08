#!/usr/bin/python3
"""Defines Rectangle class that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class: child of BaseGeomtry with an __init__ method"""

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
