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
    def __init__(self, calculator):
        self.calculator = calculator

    def update(self, calculation):
        # Placeholder – real pandas save comes later
        self.calculator._auto_save_triggered = True