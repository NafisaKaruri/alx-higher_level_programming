#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """
    Class that defines a MagicClass "circle".
    Attributes:
        radius: the radius of a circle.
    """
    def __init__(self, radius=0):
        """
        Creates a new MagicClass instance.
        Args:
            radius: the radius of a circle.
        Raises:
            TypeError: radius must be a number
        """
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self, radius):
        """
        Returns: the area of a circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self, radius):
        """
        Returns: the circuference of a circle.
        """
        return (2 * math.pi) * self.__radius
