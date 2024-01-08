#!/usr/bin/python3
"""Defines is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """Returns bool, if obj is an instance of a_class or subclass"""

    return isinstance(obj, a_class)
