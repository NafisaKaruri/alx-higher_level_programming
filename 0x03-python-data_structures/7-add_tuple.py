#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = []
    length = max(len(tuple_a), len(tuple_b))

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    for i in range(length):
        a = tuple_a[i] if i < len(tuple_a) else 0
        b = tuple_b[i] if i < len(tuple_b) else 0
        new_tuple.append(a + b)
    return tuple(new_tuple)
