from main import A, B, C


def test_addition():
    assert A(5, 3) == 8


def test_subtraction():
    assert B(5, 3) == 2


def test_multiplication():
    assert C(5, 3) == 15
