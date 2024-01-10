#!/usr/bin/python3
"""Defines append_after method"""


def append_after(filename="", search_string="", new_string=""):
    """
    This function inserts a line of text to a file,
    after each line containing a specific string.

    Arguments:
        filename: the file to be modified
        search_string: the specific string to insert new_string after
        new_string: the new string to be appended
    """
    with open(filename, 'r', encoding="utf_8") as f:
        lines = f.readlines()
    with open(filename, 'w', encoding="utf_8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
    f.close
