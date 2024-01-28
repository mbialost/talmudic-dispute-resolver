"""
Module: dispute_fraction.py

Description:
    This module is specifically designed for managing fractions in dispute scenarios. It includes:

    - 'DisputeFraction': 
        A subclass of Python's standard 'Fraction' class. This subclass ensures that fractions are restricted 
        to the permissible range throughout a resolution process. It incorporates custom arithmetic operations to preserve 
        this characteristic of DisputeFraction instances.
        
    - `validate_claim`:
        A helper function that validates a single claim, or converts it to a DisputeFraction, prior to its inclusion in a dispute.

    Note: 
    Within the project, 'DisputeFraction' is imported as 'Fraction' for enhanced clarity and ease of integration.
"""
from fractions import Fraction
from ..exceptions.fraction_error import FractionRangeError


class DisputeFraction(Fraction):
    """
    A specialized Fraction class for disputes, ensuring fractions remain within the 0 to 1 range.

    Inherits from the standard 'Fraction' class.

    Raises:
        FractionError: When a fraction is not within the 0 to 1 range.
    """
    
    def __new__(cls, numerator, denominator=None) -> "DisputeFraction":
        if denominator is not None:
            instance = super().__new__(cls, numerator, denominator)
        else:
            instance = super().__new__(cls, numerator)
        instance._validate()
        return instance

    def _validate(self) -> None:
        if not (0 <= self <= 1):
            raise FractionRangeError(self)

        
    def _operate(self, other, operation) -> "DisputeFraction":
        if not isinstance(other, Fraction):
            other = Fraction(other)
        result = operation(self, other)
        return DisputeFraction(result.numerator, result.denominator)

    # Overriding arithmetic operations to ensure the result is a DisputeFraction
    def __add__(self, other) -> "DisputeFraction":
        return self._operate(other, Fraction.__add__)

    def __sub__(self, other) -> "DisputeFraction":
        return self._operate(other, Fraction.__sub__)

    def __mul__(self, other) -> "DisputeFraction":
        return self._operate(other, Fraction.__mul__)

    def __truediv__(self, other) -> "DisputeFraction":
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self._operate(other, Fraction.__truediv__)

    # Ensure reflected operations also return DisputeFractions
    def __radd__(self, other) -> "DisputeFraction":
        return self._operate(other, Fraction.__radd__)

    def __rsub__(self, other) -> "DisputeFraction":
        return self._operate(other, Fraction.__rsub__)

    def __rmul__(self, other) -> "DisputeFraction":
        return self._operate(other, Fraction.__rmul__)

    def __rtruediv__(self, other) -> "DisputeFraction":
        if self == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self._operate(other, Fraction.__rtruediv__)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.numerator}, {self.denominator})"
    
    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"


def validate_claim(claim) -> DisputeFraction:
    """
    Converts the input to a DisputeFraction if it's not already one, ensuring it's within the valid range [0, 1].

    Args:
        claim: The value to convert to DisputeFraction. Can be an int, float, Fraction, or DisputeFraction.

    Returns:
        A DisputeFraction instance representing the claim.

    Raises:
        TypeError: If the claim cannot be converted to a DisputeFraction.
        FractionRangeError: If the resulting DisputeFraction is out of the valid range [0, 1].
    """
    if not isinstance(claim, Fraction):
        try:
            claim = DisputeFraction(claim)
        except ValueError as e:
            raise TypeError(f"Cannot convert {claim} to DisputeFraction: {e}")
    if isinstance(claim, DisputeFraction):
        return claim
    return DisputeFraction(claim.numerator, claim.denominator)

print(Fraction(1, 2) + Fraction(1, 2))