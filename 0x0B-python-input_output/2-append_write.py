#!/usr/bin/python3
"""Defines append_write method"""


def append_write(filename="", text=""):
    """
    append_write: appends a string at the end of a text file
    args:
        filename: the name of the text file to modify
        text: the string to be appended to the text file
    returns: the number of characters added
    """
    with open(filename, 'a', encoding="utf_8") as f:
        n = f.write(text)
    f.close()
    return n
