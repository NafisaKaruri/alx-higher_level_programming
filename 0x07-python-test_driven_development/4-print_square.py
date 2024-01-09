#!/usr/bin/python3
"""Defines the print_square method"""


def print_square(size):
    """prints a square with #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
