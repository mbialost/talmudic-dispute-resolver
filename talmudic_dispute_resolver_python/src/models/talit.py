"""
Module: talit.py

Description:
- Defines the 'Talit' class as a concrete implementation of 'DisputedResource' for managing disputes over a Talit,
  a traditional Jewish prayer shawl. It extends 'DisputedResource' for the Talmudic Talit-dispute scenario,
  adding validation and logging functionality.

Dependencies:
- Utilizes the DisputeFraction class (aliased as Fraction) to ensure that all claims and allocations are represented 
  as fractions in range 0-1 throughout the resolution process.
"""

from dataclasses import dataclass
import logging

from ..models.dispute_fraction import DisputeFraction as Fraction
from ..exceptions.fraction_error import FractionOperationError
from ..base.disputed_resource import DisputedResource


logger = logging.getLogger(__name__)


@dataclass
class Talit(DisputedResource):
    """
    Concrete subclass of DisputedResource for overseeing the Allocation process in Talir disputes.
    Uses a custom exception `AllocationError` for error-handling, and provides tracking and logging
    functionality for auditability.

    Inherited Attributes:
        remainder (Fraction): Unallocated fraction of the Talit, initially set to 1 (the whole Talit).

    Methods:
        allocate(fraction: Fraction) -> None:
            Implements specific logic for validating and logging each allocation for transparency and clarity.

    Example:
        >>> talit = Talit()
        >>> talit.allocate(Fraction(1, 4))
        >>> print(talit.remainder)
        Fraction(3, 4)
    """
    
    def allocate(self, fraction: Fraction) -> None:
        """
        Allocates a given fraction of the Talit, adjusting the 'remainder' and logs the operation, 
        ensuring transparency and traceability in the resolution of the dispute.

        Args:
            fraction (Fraction): The fraction of the Talit to be allocated.
            
        Raises:
            AllocationError: If the allocation fraction is greater than the remainder.
        """
        if self.remainder < fraction:
            raise FractionOperationError(
                fraction,
                self.remainder,
                f"Talit cannot allocate more than the remainder.",
            )
        
        logger.info("Allocating %s of the Talit", fraction)
        self.remainder -= fraction
