import pytest
from decimal import Decimal
from app.operations import (
    add, subtract, multiply, divide,
    power, root, modulus,
    int_divide, percent, abs_diff
)

def test_add():
    assert add(2, 3) == Decimal("5")

def test_subtract():
    assert subtract(5, 2) == Decimal("3")

def test_multiply():
    assert multiply(3, 4) == Decimal("12")

def test_divide():
    assert divide(10, 2) == Decimal("5")

def test_power():
    assert power(2, 3) == Decimal("8")

def test_root():
    assert root(9, 2) == Decimal("3")

def test_modulus():
    assert modulus(10, 3) == Decimal("1")

def test_int_divide():
    assert int_divide(7, 2) == Decimal("3")

def test_percent():
    assert percent(50, 200) == Decimal("25")

def test_abs_diff():
    assert abs_diff(10, 4) == Decimal("6")



