#!/usr/bin/python3
"""Defines find_peak function"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
