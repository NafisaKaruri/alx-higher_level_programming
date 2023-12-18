#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            n = n + 1
        except (ValueError, IndexError, NameError, TypeError):
            continue
    print()
    return n
