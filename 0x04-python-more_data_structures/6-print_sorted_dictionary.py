#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    sd = sorted(a_dictionary.keys())
    for key in sd:
        print("{}: {}".format(key, a_dictionary.get(key)))
