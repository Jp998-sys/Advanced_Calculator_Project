from abc import ABC, abstractmethod
from decimal import Decimal

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

    def _to_decimal(self, value):
        return Decimal(str(value))


class Add(Operation):
    def execute(self, a, b):
        return self._to_decimal(a) + self._to_decimal(b)


class Subtract(Operation):
    def execute(self, a, b):
        return self._to_decimal(a) - self._to_decimal(b)


class Multiply(Operation):
    def execute(self, a, b):
        return self._to_decimal(a) * self._to_decimal(b)


class Divide(Operation):
    def execute(self, a, b):
        b = self._to_decimal(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self._to_decimal(a) / b


class Power(Operation):
    def execute(self, a, b):
        return self._to_decimal(a) ** self._to_decimal(b)


class Root(Operation):
    def execute(self, a, b):
        b = self._to_decimal(b)
        if b == 0:
            raise ValueError("Root degree cannot be zero")
        return self._to_decimal(a) ** (Decimal(1) / b)


class Modulus(Operation):
    def execute(self, a, b):
        b = self._to_decimal(b)
        if b == 0:
            raise ZeroDivisionError("Cannot mod by zero")
        return self._to_decimal(a) % b


class IntDivide(Operation):
    def execute(self, a, b):
        b = self._to_decimal(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self._to_decimal(a) // b


class Percent(Operation):
    def execute(self, a, b):
        b = self._to_decimal(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return (self._to_decimal(a) / b) * Decimal(100)


class AbsDiff(Operation):
    def execute(self, a, b):
        return abs(self._to_decimal(a) - self._to_decimal(b))