#!/usr/bin/python3
"""Defines read_file method"""


def read_file(filename=""):
    """
    read_file: reads a text file (UTF8) and prints it to stdout
    args:
        filename: the file to be opened
    """
    with open(filename, encoding="utf_8") as f:
        read_data = f.read()
        print("{}".format(read_data), end='')
    f.close()
