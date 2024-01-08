#!/usr/bin/python3
"""Defines inherits_from method"""


def inherits_from(obj, a_class):
    """Returns if obj is instance of a_class that inherited from a a_class"""

    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
