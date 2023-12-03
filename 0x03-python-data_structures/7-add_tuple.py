#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    length = max(len(tuple_a), len(tuple_b))
    for i in range(length):
        if i >= len(tuple_b):
            new_tuple.append(tuple_a[i])
        elif i >= len(tuple_a):
            new_tuple.append(tuple_b[i])
        else:
            new_tuple.append(tuple_a[i] + tuple_b[i])
    return tuple(new_tuple)
