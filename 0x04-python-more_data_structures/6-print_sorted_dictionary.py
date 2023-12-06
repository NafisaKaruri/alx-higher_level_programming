#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sd = sorted(a_dictionary)
    for key in sd:
        print("{} : {}".format(key, a_dictionary.get(key)))
