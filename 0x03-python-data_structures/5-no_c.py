#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)
    new_string = ''
    for i in range(length):
        if my_string[i] in "cC":
            continue
        new_string = new_string + my_string[i]
    return new_string
