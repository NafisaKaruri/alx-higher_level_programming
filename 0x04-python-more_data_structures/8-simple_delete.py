#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key and a_dictionary.get(key):
        del a_dictionary[key]
    return a_dictionary
