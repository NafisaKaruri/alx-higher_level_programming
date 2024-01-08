#!/usr/bin/python3
"""Defines is_same_class method"""


def is_same_class(obj, a_class):
    """Returns bool, checks if obj is exactly an instance of a_class"""

    return type(obj) == a_class
