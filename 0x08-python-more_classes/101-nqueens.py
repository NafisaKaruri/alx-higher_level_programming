#!/usr/bin/python3
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if not argv[1].isdigit():
    print("N must be a number")
    exit(1)

N = int(argv[1])
if N < 4:
    print("N must be at least 4")
    exit(1)
