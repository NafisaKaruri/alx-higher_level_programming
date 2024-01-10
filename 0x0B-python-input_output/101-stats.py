#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""


from sys import stdin

# the possible status codes
status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

# the file read size counter
read_size = 0
# lines read counter
count = 0


def printer():
    """
    Prints the metrics so far
    """
    print('File size: {}'.format(read_size))
    for key in sorted(status_codes):
        if status_codes[key] > 0:
            print('{}: {}'.format(key, status_codes[key]))


try:
    for line in stdin:
        s_line = line.split()
        if len(s_line) >= 2:
            status = s_line[-2]
            read_size += int(s_line[-1])
            if status in status_codes:
                status_codes[status] += 1

        count += 1

        if count % 10 == 0:
            printer()
    printer()

except KeyboardInterrupt as e:
    printer()
