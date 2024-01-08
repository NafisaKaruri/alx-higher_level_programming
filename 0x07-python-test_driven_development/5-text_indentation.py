#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for d in ".:?":
        text = (d + "\n\n").join([i.strip(" ") for i in text.split(d)])

    print("{}".format(text), end="")
