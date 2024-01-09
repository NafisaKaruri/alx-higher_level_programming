#!/usr/bin/python3
"""Defines the text_indentation method"""


def text_indentation(text):
    """prints a text with 2 \n after each .?:"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for d in ".:?":
        text = (d + "\n\n").join([i.strip(" ") for i in text.split(d)])

    print("{}".format(text), end="")
