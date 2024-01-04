#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """
    Class that defines a Rectangle

    Attributes:
        width: the width of the rectangle.
        height: the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Creates a new instance of class Rectangle
        Args:
            height (int): the height of the Rectangle.
            width (int): the width of the Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.
        Args:
            value (int): the height of the Rectangle.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.
        Args:
            value (int): the width of the Rectangle.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
