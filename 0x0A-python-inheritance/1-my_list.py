#!/usr/bin/python3
"""Defines a class MyList"""


class MyList(list):
    """Class with a print_sorted method"""

    def print_sorted(self):
        """Sorts and prints a list"""
        print(sorted(self))
