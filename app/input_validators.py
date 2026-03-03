from app.calculator_config import CalculatorConfig

class AutoSaveObserver(Observer):
    def __init__(self, calculator):
        self.calculator = calculator

    def update(self, calculation):
        if CalculatorConfig.AUTO_SAVE:
            self.calculator.save_history()