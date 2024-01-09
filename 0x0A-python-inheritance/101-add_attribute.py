#!/usr/bin/python3
"""Defines the add_attribute method"""


def add_attribute(obj, name, value):
    """
    add a new attribute to an object if possible
    raises:
        TypeError: can't add new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
