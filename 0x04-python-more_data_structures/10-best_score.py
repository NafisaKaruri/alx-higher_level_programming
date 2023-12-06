#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        mv = 0
        mk = None
        for key, value in a_dictionary.items():
            if value > mv:
                mv = value
                mk = key
        return mk
