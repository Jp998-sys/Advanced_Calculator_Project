from app.calculator import Calculator
from app.history import LoggingObserver, AutoSaveObserver

def test_add_observer():
    calc = Calculator()
    observer = LoggingObserver()
    calc.add_observer(observer)
    assert observer in calc.observers

def test_remove_observer():
    calc = Calculator()
    observer = LoggingObserver()
    calc.add_observer(observer)
    calc.remove_observer(observer)
    assert observer not in calc.observers

import os 
def test_autosave_observer_trigger():
    filename = "test_auto.csv"
    calc = Calculator()
    observer = AutoSaveObserver(calc, filename)
    calc.add_observer(observer)
    calc.calculate("add", 2, 3)
    assert os.path.exists(filename)
    os.remove(filename)

def test_calculate_add():
    calc = Calculator()
    result = calc.calculate("add", 2, 3)
    assert result == 5
    assert len(calc.history) == 1

def test_undo_after_calculate_add():
    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.undo()
    assert len(calc.history) == 0

def test_redo_after_calculate_add():
    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.undo()
    calc.redo()
    assert len(calc.history) == 1

