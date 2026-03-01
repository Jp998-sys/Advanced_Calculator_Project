from decimal import Decimal

def add(a, b):
    return Decimal(a) + Decimal(b)

def subtract(a, b):
    return Decimal(a) - Decimal(b)

def multiply(a, b):
    return Decimal(a) * Decimal(b)

def divide(a, b):
    if Decimal(b) == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return Decimal(a) / Decimal(b)

def power(a, b):
    return Decimal(a) ** Decimal(b)

def root(a, b):
    if Decimal(b) == 0:
        raise ValueError("Root degree cannot be zero")
    return Decimal(a) ** (Decimal(1) / Decimal(b))

def modulus(a, b):
    if Decimal(b) == 0:
        raise ZeroDivisionError("Cannot mod by zero")
    return Decimal(a) % Decimal(b)

def int_divide(a, b):
    if Decimal(b) == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return Decimal(a) // Decimal(b)

def percent(a, b):
    if Decimal(b) == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return (Decimal(a) / Decimal(b)) * Decimal(100)

def abs_diff(a, b):
    return abs(Decimal(a) - Decimal(b))

