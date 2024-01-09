#!/usr/bin/python3
"""Defines save_to_json_file method"""


import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json_file: writes an object to a text file using JSON representation
    args:
        my_obj: the object
        filename: the text file
    """
    with open(filename, 'w', encoding="utf_8") as f:
        json.dump(my_obj, f)
    f.close()
