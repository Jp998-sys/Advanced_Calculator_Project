class CalculatorMemento:
    def __init__(self, history_snapshot):
        self._history_snapshot = history_snapshot.copy()

    def get_state(self):
        return self._history_snapshot.copy()