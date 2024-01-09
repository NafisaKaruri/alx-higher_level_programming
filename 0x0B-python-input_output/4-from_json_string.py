#!/usr/bin/python3
"""Defines from_json_string method"""


import json


def from_json_string(my_str):
    """
    from_json_string: returns an object represented by JSON string
    args:
        my_str: the JSON representation of the object
    """
    return json.loads(my_str)
