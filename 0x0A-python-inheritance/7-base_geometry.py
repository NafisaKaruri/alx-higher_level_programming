#!/usr/bin/python3
"""Defines BaseGeometry class"""


class BaseGeometry:
    """Defines public instance methods area, integer_validator"""

    def area(self):
        """
        raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates <value>
        raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
