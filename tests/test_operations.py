import pytest
import os
from decimal import Decimal
from app.operations import (
    Add, Subtract, Multiply, Divide,
    Power, Root, Modulus,
    IntDivide, Percent, AbsDiff
)
from app.operations import OperationFactory



def test_save_history_creates_file(tmp_path):
    file_path = tmp_path / "history.csv"

    calc = Calculator()
    calc.calculate("add", 2, 3)

    result = calc.save_history(str(file_path))

    assert result is True
    assert os.path.exists(file_path)

def test_load_history(tmp_path):
    file_path = tmp_path / "history.csv"

    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.save_history(str(file_path))

    new_calc = Calculator()
    result = new_calc.load_history(str(file_path))

    assert result is True
    assert len(new_calc.history) == 1

def test_load_history_file_not_found():
    calc = Calculator()
    result = calc.load_history("nonexistent.csv")
    assert result is False
    
def test_divide_by_zero():
    op = Divide()
    with pytest.raises(ZeroDivisionError):
        op.execute(5, 0)

def test_root_zero_degree():
    op = Root()
    with pytest.raises(ValueError):
        op.execute(9, 0)

def test_percent_divide_zero():
    op = Percent()
    with pytest.raises(ZeroDivisionError):
        op.execute(5, 0)

def test_factory_returns_add():
    op = OperationFactory.create("add")
    assert isinstance(op, Add)

def test_factory_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.create("unknown")

from app.calculator import Calculator

def test_add_calculation():
    calc = Calculator()
    calc.add_calculation("2 + 3 = 5")
    assert len(calc.history) == 1

def test_undo():
    calc = Calculator()
    calc.add_calculation("2 + 3 = 5")
    result = calc.undo()
    assert result is True
    assert calc.history == []

def test_redo():
    calc = Calculator()
    calc.add_calculation("2 + 3 = 5")
    calc.undo()
    result = calc.redo()
    assert result is True
    assert len(calc.history) == 1

def test_undo_empty():
    calc = Calculator()
    assert calc.undo() is False

def test_redo_empty():
    calc = Calculator()
    assert calc.redo() is False

def test_calculate_add():
    calc = Calculator()
    result = calc.calculate("add", 2, 3)
    assert result == 5
    assert len(calc.history) == 1

@pytest.mark.parametrize("operation,a,b,expected", [
    ("power", 2, 3, 8),
    ("root", 9, 2, 3),
    ("modulus", 10, 3, 1),
    ("int_divide", 10, 3, 3),
    ("percent", 50, 200, 25),
    ("abs_diff", 10, 4, 6),
])
def test_advanced_operations(operation, a, b, expected):
    op = OperationFactory.create(operation)
    result = op.execute(a, b)
    assert result == expected