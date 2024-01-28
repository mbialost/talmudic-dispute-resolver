"""
Module: talit_claimant.py

Description:
- Defines the 'TalitClaimant' class as a concrete implementation of 'Claimant' for the Talmudic dispute scenario.

Dependencies:
- Utilizes the DisputeFraction class (aliased as Fraction) to ensure that all claims and allocations are represented 
  as fractions in range 0-1 throughout the resolution process.
"""

from dataclasses import dataclass
import logging

from talmudic_dispute_resolver.src.models.dispute_fraction import (
    DisputeFraction as Fraction,
)
from ..exceptions.fraction_error import FractionOperationError
from ..base.claimant import Claimant


logger = logging.getLogger(__name__)


@dataclass
class TalitClaimant(Claimant):
    """
    Represents a claimant in a Talit dispute, extending the 'Claimant' base class.


    It initializes the concession based on the claim, tracks the collected and
    conceded fractions adjusting the claimant's share in the dispute.

    Attributes Inherited from the Claimant base class (and redefined for clarity):
        identifier (str): Unique identifier for the claimant.
        claim (Fraction): The initial claim of the disputed Talit by the claimant.
        concession (Fraction): Fraction of the Talit conceded by the claimant, initially set to zero.
        collected (Fraction): Total fraction of the Talit collected by the claimant, initially set to zero.

    Methods:
        collect(fraction: Fraction) -> None:
            Collects a specified fraction of the Talit. This method updates the 'collected' attribute
            to reflect the fraction of the Talit received by the claimant.

        decrement_concession(fraction: Fraction) -> None:
            Decrements the claimant's concession by a specified fraction. This method updates the 'concession'
            attribute, reducing it by the given fraction once a the fraction of it has been resolved.
    """

    identifier: str
    claim: Fraction
    concession: Fraction = Fraction(0)
    collected: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        """
        Initializes the 'concession' attribute to the difference between the full object (1) and
        the 'claim', and logs the creation of the claimant.
        """
        self.concession = 1 - self.claim
        logger.debug("Creating Claimant: '%s' Claim: %s", self.identifier, self.claim)

    def collect(self, fraction: Fraction) -> None:
        """
        Collects a specified fraction of the Talit.

        Args:
            fraction (Fraction): The fraction of the Talit to be collected.

        Updates the 'collected' attribute by adding the specified fraction and logs the collection action.
        """
        if fraction > self.claim:
            raise FractionOperationError(
                fraction,
                self.claim,
                f"Claimant {self.identifier} attempted to collect more than their claim.",
            )

        self.collected += fraction
        logger.info("Claimant %s collected %s of Talit", self.identifier, fraction)

    def concede(self, fraction: Fraction) -> None:
        """
        Subtracts a specified fraction from the claimant's concession once it has been resolved.

        Args:
            fraction (Fraction): Fraction to subtract from the concession.

        Reduces the 'concession' attribute by the specified fraction and logs the action.
        """
        if fraction > self.concession:
            raise FractionOperationError(
                fraction,
                self.concession,
                f"Claimant {self.identifier} attempted to concede more than their concession.",
            )

        self.concession -= fraction
        logger.info(
            "Concession of claimant %s decremented by %s to %s",
            self.identifier,
            fraction,
            self.concession,
        )

    def __repr__(self) -> str:
        return f"TalitClaimant({self.identifier}, {self.claim})"

    def __str__(self) -> str:
        return f"Claimant {self.identifier} with claim {self.claim}\n    - Collected: {self.collected}\n"
