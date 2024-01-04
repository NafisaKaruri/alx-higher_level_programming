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

    def __str__(self):
        """
        Returns an empty string if the width or the height == 0
        Returns the Rectangle as a string of #
        """
        rec = ""
        if self.__height == 0 or self.__width == 0:
            return rec
        for i in range(self.__height):
            rec += ("#" * self.__width)
            if i is not self.__height - 1:
                rec += "\n"
        return rec

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be able
        to recreate a new instancle by using eval()
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

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

    def area(self):
        """
        Calculates the Rectangle area.

        Returns: the current Rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the Rectangle perimeter.

        Returns: the current Rectangle perimeter.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
