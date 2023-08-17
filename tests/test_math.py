from src.math import add, subtract, multiply


def test_add():
    assert add(3, 2) == 5


def test_subtract():
    assert subtract(3, 2) == 0


def test_multiply():
    assert multiply(3, 2) == 6
