#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    maxx = my_list[0]
    for i in my_list[1:]:
        if i > maxx:
            maxx = i
    return maxx
    # return sorted(my_list)[len(my_list) - 1]
