import pytest
from decimal import Decimal
from app.operations import (
    Add, Subtract, Multiply, Divide,
    Power, Root, Modulus,
    IntDivide, Percent, AbsDiff
)
from app.operations import OperationFactory

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