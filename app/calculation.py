from datetime import datetime


class Calculation:
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = datetime.now()

    def __str__(self):
        symbol_map = {
            "add": "+",
            "subtract": "-",
            "multiply": "*",
            "divide": "/",
            "power": "^",
            "root": "√",
            "modulus": "%",
            "int_divide": "//",
            "percent": "%",
            "abs_diff": "|-|"
        }

        symbol = symbol_map.get(self.operation, self.operation)

        return f"{self.a} {symbol} {self.b} = {self.result}"