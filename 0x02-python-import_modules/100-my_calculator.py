#!/usr/bin/python3
if __name__ == '__main__':
    # Import required functions
    from calculator_1 import add, sub, mul, div
    from sys import argv

    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Define a dictionary to map operators to functions
    operator_functions = {"+": add, "-": sub, "*": mul, "/": div}

    # Check if the operator is valid
    operator = argv[2]
    if operator not in operator_functions:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    # Parse input numbers
    try:
        a = int(argv[1])
        b = int(argv[3])
    except ValueError:
        print("Invalid input. Both <a> and <b> should be integers.")
        exit(1)

    # Perform the calculation and handle division by zero
    result = None
    if operator == "/" and b == 0:
        print("Error: Division by zero is not allowed.")
        exit(1)
    else:
        result = operator_functions[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))

