"""
Module: disputed_object.py

Description:
- This module introduces the DisputedResource abstract base class, designed for representing objects within a dispute context. 
  It offers a a generic template for tracking and managing the allocation of such objects through fractional claims.

Dependencies:
- Utilizes the DisputeFraction class (aliased as Fraction) to ensure that all claims and allocations are represented 
  as fractions in range 0-1 throughout the resolution process.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod

from ..models.dispute_fraction import DisputeFraction as Fraction


@dataclass
class DisputedResource(ABC):
    """
    An abstract base class for objects involved in disputes, DisputedResource provides a template for tracking 
    the unallocated portion of such objects. It defines a framework for subclasses to implement specific allocation behaviors 
    tailored to the nature of the disputed object.

    Attributes:
        remainder (Fraction): The unallocated fraction of the object.

    Methods:
        allocate(fraction: Fraction) -> None: An abstract method intended for allocation of a portion of the object. 
        Implementing subclasses will define the allocation logic specific to the disputed object's context.
    
    Example Usage:
      class TalitDispute(DisputedResource):
          def allocate(self, fraction: Fraction) -> None:
              self.remainder -= fraction  # Update the remainder
    """

    remainder: Fraction = Fraction(1)

    @abstractmethod
    def allocate(self, fraction: Fraction) -> None:
        """
        Abstract method for allocating a specified fraction from the object's remainder.

        Args:
            fraction (Fraction): The fraction of the object to be allocated.

        This method should be implemented by subclasses to define specific allocation behavior.
        """
        pass

