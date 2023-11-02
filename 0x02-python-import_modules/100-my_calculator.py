#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3)

    operators = {'+': add, '-': sub, '*': mul, '/': div}

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    if operator == '/' and b == 0:
        print("Error: Division by zero is not allowed.")
        exit(1)

    result = operators[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))

