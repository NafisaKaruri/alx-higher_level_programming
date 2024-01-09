#!/usr/bin/python3
"""Defines write_file method"""


def write_file(filename="", text=""):
    """
    write_file: writes a string to a text file (UTF8)
    args:
        filename: the name of the text file to be written in
        text: the string to be added to the text file
    returns: the number of characters written
    """
    with open(filename, 'w', encoding="utf_8") as f:
        n = f.write(text)
    f.close
    return n
