#!/usr/bin/python3
"""prints all possible solutions to the N queens puzzle

Attributes:
    N (int): the number of queens
"""


from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

N = int(argv[1])
if N < 4:
    print("N must be at least 4")
    sys.exit(1)
