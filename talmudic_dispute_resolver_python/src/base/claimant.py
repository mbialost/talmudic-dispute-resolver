"""
Module: claimant.py

Description:
- This module introduces the Claimant abstract base class, designed for representing claimants in dispute scenarios.
  The class provides a generic template for claimant operations, which can be specialized in subclasses.

Dependencies:
- Utilizes the DisputeFraction class (aliased as Fraction) to ensure that all claims and allocations are represented 
  as fractions in range 0-1 throughout the resolution process.
"""

from dataclasses import dataclass
from abc import ABC, abstractmethod

from ..models.dispute_fraction import DisputeFraction as Fraction


@dataclass
class Claimant(ABC):
    """
    Abstract base class for a claimant in a dispute.

    This class acts as a template for creating specific types of claimant objects (e.g., TalitClaimant) 
    in the context of dispute resolution. It defines essential attributes and abstract methods that all 
    claimant subclasses should implement.

    Attributes:
        identifier (str): Unique identifier for the claimant.
        claim (Fraction): The initial claim of the disputed object by the claimant.
        concession (Fraction): The concession implied by the claim (i.e., the remainder minus the claim)
        collected (Fraction): Total fraction of the disputed object received by the claimant.

    Abstract Methods:
        collect(fraction: Fraction) -> None:
            Collects a specified portion of the disputed object.

        concede(fraction: Fraction) -> None:
            Decrements the claimant's concession once a portion has been resolved. 
    """

    identifier: str
    claim: Fraction
    concession: Fraction
    collected: Fraction
    
    @abstractmethod
    def collect(self, fraction: Fraction) -> None:
        """
        Abstract method for collecting a portion of the disputed object.

        Args:
            fraction (Fraction): The fraction of the disputed object to be collected.

        This method must be implemented in subclasses.
        """
        pass

    @abstractmethod
    def concede(self, fraction: Fraction) -> None:
        """
        Abstract method for decrementing a portion of the claimant's concession.

        Args:
            fraction (Fraction): The resolved fraction to subtract from the claimant's concession.

        This method must be implemented in subclasses.
        """
        pass
