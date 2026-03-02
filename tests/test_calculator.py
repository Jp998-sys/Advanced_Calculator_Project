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

def test_autosave_observer_trigger():
    calc = Calculator()
    observer = AutoSaveObserver(calc)
    calc.add_observer(observer)

    calc.add_calculation("2 + 3 = 5")

    assert calc._auto_save_triggered is True

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

