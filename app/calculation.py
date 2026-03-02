from datetime import datetime

class Calculation: 
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.a} {self.operation} {self.b} = {self.result}"