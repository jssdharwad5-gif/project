import math
import sys


def A(a, b):
    return a + b


def B(a, b):
    return a - b


def C(a, b):
    return a * b


def read_two_numbers():
    # Accept CLI numbers if provided, so CI/CD can run without input.
    if len(sys.argv) >= 3:
        try:
            return float(sys.argv[1]), float(sys.argv[2])
        except ValueError:
            return 5.0, 3.0

    # Only ask interactively if a real terminal is available.
    if sys.stdin.isatty():
        try:
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            return first, second
        except (EOFError, ValueError):
            print("Please enter valid numeric values.")
            return 5.0, 3.0

    # Non-interactive environments such as GitHub Actions should not block.
    return 5.0, 3.0


if __name__ == '__main__':
    x, y = read_two_numbers()
    print("Addition:", A(x, y))
    print("Subtraction:", B(x, y))
    print("Multiplication:", C(x, y))
    print("Square root of Addition:", math.sqrt(A(x, y)))
