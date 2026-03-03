class CalculatorError(Exception):
    """Base exception for all calculator-related errors."""
    pass


class OperationError(CalculatorError):
    """Raised when an invalid operation is requested or fails."""
    pass


class ValidationError(CalculatorError):
    """Raised when user input fails validation checks."""
    pass


class HistoryError(CalculatorError):
    """Raised when there is an issue with history management."""
    pass


class ConfigurationError(CalculatorError):
    """Raised when configuration loading fails."""
    pass