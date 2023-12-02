#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    length = len(my_list)
    new_list = []
    for i in range(length):
        if i == idx:
            new_list.append(element)
        else:
            new_list.append(my_list[i])
    return new_list
