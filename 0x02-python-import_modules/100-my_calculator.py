#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{:d} {:s} {:d}".format(a, argv[2], b), end=" = ")
    if (argv[2] == '+'):
        print("{:d}".format(add(a, b)))
    elif (argv[2] == '-'):
        print("{:d}".format(sub(a, b)))
    elif (argv[2] == '*'):
        print("{:d}".format(mul(a, b)))
    elif (argv[2] == '/'):
        print("{:d}".format(div(a, b)))
