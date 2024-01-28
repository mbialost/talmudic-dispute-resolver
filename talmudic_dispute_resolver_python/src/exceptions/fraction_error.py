"""
Module: fraction_error.py

Description:
- A custom exception class created to handle cases of invalid fractions in a dispute, 
  particularly those outside the range of 0 to 1.
"""

from fractions import Fraction


class FractionError(ValueError):
    """
    Base-class for errors related to fraction processing.
    """

    def __init__(self, fraction: Fraction, message: str = "Fraction error occurred"):
        super().__init__(message)
        self.fraction = fraction

    def __str__(self):
        return f"{super().__str__()} - Fraction: {self.fraction}"


class FractionRangeError(FractionError):
    """
    Exception for fractions outside the valid range [0, 1].
    """

    def __init__(self, fraction: Fraction):
        message = f"Invalid fraction {fraction}. Must be within [0, 1]."
        super().__init__(fraction, message)

    def __str__(self):
        return f"{super().__str__()}"


class FractionOperationError(FractionError):
    """
    Exception for generic fraction operation errors.
    """

    def __init__(self, fraction: Fraction, target: Fraction, message: str):
        super().__init__(fraction, message)
        self.target = target

    def __str__(self):
        return f"{super().__str__()} - Operand: {self.target}"
