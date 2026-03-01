import pytest
from decimal import Decimal
from app.operations import (add, subtract, multiply, divide,
                             power, root, modulus, int_divide,
                               percent, abs_diff)
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

def test_root_zero_degree():
    with pytest.raises(ValueError):
        root(9, 0)

def test_percent_divide_zero():
    with pytest.raises(ZeroDivisionError):
        percent(5, 0)