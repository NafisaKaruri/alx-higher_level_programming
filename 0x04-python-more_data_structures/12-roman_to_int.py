#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    num = 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    s = 0
    for digit in reversed(roman_string):
        num = rom[digit]
        if s < num * 5:
            s += num
        else:
            s += -num
    return s
