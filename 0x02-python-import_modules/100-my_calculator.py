#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, mul, sub, div
    from sys import argv, exit
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    a = int(argv[1])
    operation = argv[2]
    b = int(argv[3])
    if operation == '+':
        print('{} {} {} = {}'.format(a, operation, b, add(a, b)))
    elif operation == '-':
        print('{} {} {} = {}'.format(a, operation, b, sub(a, b)))
    elif operation == '*':
        print('{} {} {} = {}'.format(a, operation, b, mul(a, b)))
    else:
        print('{} {} {} = {}'.format(a, operation, b, div(a, b)))
