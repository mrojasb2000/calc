from calc.calc import Calc
import pytest

def test_add_many_numbers():
    c = Calc()
    s = range(100)
    expected = 4950
    actual = c.add(*s)

    assert actual == expected

def test_substract_two_numbers():
    c = Calc()
    expected = 7
    actual = c.sub(10, 3)

    assert actual == expected

def test_mul_two_numbers():
    c = Calc()
    expected = 24
    actual = c.mul(6, 4)

    assert actual == expected

def test_mul_many_numbers():
    c = Calc()
    s = range(1, 10)
    expected = 362880
    actual = c.mul(*s)

    assert actual == expected

def test_div_two_numbers():
    c = Calc()
    expected = 6.5
    actual = c.div(13, 2)

    assert actual == expected

def test_div_by_zero_returns_inf():
    c = Calc()
    expected = "inf"
    actual = c.div(5, 0)

    assert actual == expected

def test_mul_by_zero_raises_exception():
    c = Calc()

    with pytest.raises(ValueError):
        c.mul(3, 0)    