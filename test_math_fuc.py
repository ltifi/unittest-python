from unittest import result
import math_func
import pytest
import sys


@pytest.mark.skip(reason='Do not run number add test')
def test_add():
    assert math_func .add(7, 3) == 10
    assert math_func.add(7) == 8


@pytest.mark.skipif(sys.version_info < (3, 3), reason='Do not run number add test')
def test_prod():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14


@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Hello' in result


@pytest.mark.string
def test_product_strings():
    assert math_func.product('Hello ', 3)[:-1] == 'Hello Hello Hello'
    result = math_func.product('Hello')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
