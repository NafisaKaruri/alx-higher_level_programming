#!/usr/bin/python3
"""Defines to_json_string method"""


import json


def to_json_string(my_obj):
    """
    to_json_string: returns the JSON representation of an object
    args:
        my_obj: the object
    """
    return json.dumps(my_obj)
