#!/usr/bin/python3
"""Defines load_from_json_file method"""


import json


def load_from_json_file(filename):
    """
    load_from_json_file: creates an object from JSON file
    args:
        filename: the json file
    """
    with open(filename, 'r', encoding="utf_8") as f:
        x = json.load(f)
    f.close()
    return x
