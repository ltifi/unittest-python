import math_func


def test_add():
    assert math_func .add(7, 3) == 10
    assert math_func.add(7) == 8


def test_prod():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 15