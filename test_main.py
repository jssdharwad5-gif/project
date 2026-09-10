import math
import sys
from main import A, B, C, read_two_numbers


def test_addition():
    assert A(5, 3) == 8


def test_subtraction():
    assert B(5, 3) == 2


def test_multiplication():
    assert C(5, 3) == 15


def test_math_square_root_of_addition():
    result = A(9, 7)
    assert math.isclose(math.sqrt(result), 4, rel_tol=1e-9)


def test_read_two_numbers_from_command_line():
    original_argv = sys.argv[:]
    try:
        sys.argv = ['main.py', '7', '4']
        assert read_two_numbers() == (7.0, 4.0)
    finally:
        sys.argv = original_argv
