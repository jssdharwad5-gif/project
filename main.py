import math


def A(a, b):
    return a + b


def B(a, b):
    return a - b


def C(a, b):
    return a * b


def read_two_numbers():
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        return first, second
    except ValueError:
        print("Please enter valid numeric values.")
        return 0, 0


if __name__ == '__main__':
    x, y = read_two_numbers()
    print("Addition:", A(x, y))
    print("Subtraction:", B(x, y))
    print("Multiplication:", C(x, y))
    print("Square root of Addition:", math.sqrt(A(x, y)))
