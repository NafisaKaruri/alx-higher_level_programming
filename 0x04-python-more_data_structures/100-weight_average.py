#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0
    denominator = 0
    for i, j in my_list:
        numerator += i * j
        denominator += j
    return numerator/denominator
