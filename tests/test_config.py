from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError

def validate_number(value):
    if abs(value) > CalculatorConfig.MAX_INPUT_VALUE:
        raise ValidationError("Input exceeds maximum allowed value")