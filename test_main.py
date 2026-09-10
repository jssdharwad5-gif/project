import math
from main import A, B, C


def test_addition():
    assert A(5, 3) == 8


def test_subtraction():
    assert B(5, 3) == 2


def test_multiplication():
    assert C(5, 3) == 15


def test_math_square_root_of_addition():
    result = A(9, 7)
    assert math.isclose(math.sqrt(result), 4, rel_tol=1e-9)
    # math.sqrt(16) = 4.0
