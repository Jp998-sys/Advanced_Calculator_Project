from app.calculator_memento import CalculatorMemento
from app.history import Observer
from app.calculation import Calculation
from app.operations import OperationFactory 
import pandas as pd

class Calculator:
    def __init__(self):
        self.history = []
        self.undo_stack = []
        self.redo_stack = []
        self.observers = []
        self._auto_save_triggered = False  # for testing

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation)

    def add_calculation(self, calculation):
        self.undo_stack.append(CalculatorMemento(self.history))
        self.history.append(calculation)
        self.redo_stack.clear()

        self.notify_observers(calculation)

    def undo(self):
        if not self.undo_stack:
            return False

        self.redo_stack.append(CalculatorMemento(self.history))
        memento = self.undo_stack.pop()
        self.history = memento.get_state()
        return True

    def redo(self):
        if not self.redo_stack:
            return False

        self.undo_stack.append(CalculatorMemento(self.history))
        memento = self.redo_stack.pop()
        self.history = memento.get_state()
        return True
    def calculate(self, operation_name, a, b):
        # Create operation using Factory
        operation = OperationFactory.create(operation_name)

        result = operation.execute(a, b)

        # Create Calculation object
        calculation = Calculation(operation_name, a, b, result)

        #Save current state for undo
        self.undo_stack.append(CalculatorMemento(self.history))

        # Add to history 
        self.history.append(calculation)

        #Clear redo stack
        self.redo_stack.clear()

        # Notify Observer
        self.notify_observers(calculation)
        return result
    def save_history(self, filename= "history.csv"):
        if not self.history:
            return False
        data = []

        for calc in self.history:
            data.append({
                "operation": calc.operation,
                "a": calc.a,
                "b": calc.b,
                "result": calc.result,
                "timestamp": calc.timestamp
            })
        df = pd.DataFrame(data)
        df.to_csv(filename, index = False)

        return True
    def load_history(self, filename = "history.csv"):
        try:
            df = pd.read_csv(filename)

            self.history.clear()

            for _, row in df.iterrows():
                calculation = Calculation(
                    row["operation"],
                    row["a"],
                    row["b"],
                    row["result"]
                )
                self.history.append(calculation)

            return True
        except FileNotFoundError:
            return False