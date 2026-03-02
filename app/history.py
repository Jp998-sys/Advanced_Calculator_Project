from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, calculation):
        pass

import logging

class LoggingObserver(Observer):
    def update(self, calculation):
        logging.info(f"New calculation performed: {calculation}")


class AutoSaveObserver(Observer):
    def __init__(self, calculator, filename = "history.csv"):
        self.calculator = calculator
        self.filename = filename

    def update(self, calculation):
        self.calculator.save_history(self.filename)