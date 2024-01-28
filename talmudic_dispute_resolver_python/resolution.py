"""
Module: resolution.py

This module serves as the interface for applying Talmudic principles to resolve Talit disputes. 

It integrates components from other modules including
`dispute_fraction`, `talit_claimant`, `claimant_manager`, `dispute`, and `talit`.
Using classes including `DisputeFraction`, `ClaimantManager`, `TalitClaimant` `Dispute`, and `Talit` 
to execute the dispute resolution process. The main function, `apply_the_talmudic_principles`, 
implements the logic for recursively applying concessions and distributing the remainder until the dispute is resolved.

Functions:
    apply_the_talmudic_principles: Applies Talmudic principles to resolve a given dispute.
    create_dispute: Creates a dispute object from a list of claims.
"""

import logging

from src.models.dispute_fraction import DisputeFraction as Fraction
from src.models.talit_claimant import TalitClaimant 
from src.controllers.claimant_manager import ClaimantManager
from src.controllers.dispute import Dispute
from src.models.talit import Talit


logging.basicConfig(
    filename="שלושה_אוחזין_בטלית.log",
    filemode="a",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
)


def apply_the_talmudic_principles(dispute: Dispute) -> None:
    """Applies Talmudic principles to resolve a Talit dispute.

    This function iteratively applies concessions and distributes the remainder of the Talit
    until all disputes are resolved. It ensures that the dispute resolution process continues
    until no further concessions are possible, and the Talit's remainder is evenly split.

    Args:
        dispute (Dispute): The dispute object representing the ongoing Talit dispute.

    Returns:
        List[Claimant]: A list of claimants with their final allocations after the dispute is resolved.
    """
        
    while dispute.partial_claimants:
        concession = dispute.partial_claimants[0].concession
        dispute.handle_distribution(concession)
        
    dispute.split_remainder_equally()
    return dispute.full_claimants


def create_dispute(claims: list[Fraction]):
    """
    Creates a dispute object from a list of claims.

    Creates a Talit object from the list of claims, Instantiates a ClaimantManager object
    with the TalitClaimant class initializer as the claimant factory function, and
    initializes a dispute object with it.

    Args:
        claims (list[Fraction]): List of claims on the Talit.

    Returns:
        Dispute: A dispute object representing the ongoing Talit dispute.
    """
    talit = Talit()
    claimant_manager = ClaimantManager(TalitClaimant)
    dispute = Dispute(talit, claims, claimant_manager)
    return dispute

def print_resolution(resolution: list[TalitClaimant]):
    """
    Prints the resolution of a dispute.

    Prints the final allocations of the claimants in a dispute, and the total number of cycles
    required to resolve the dispute.

    Args:
        dispute (Dispute): The dispute object representing the ongoing Talit dispute.
    """
    total_sum = Fraction(0)
    print("   Claimant | Claim |  Collected")
    for claimant in resolution:
        total_sum += claimant.collected
        formatted = f"\n       {claimant.identifier}    |  {claimant.claim}  |  {claimant.collected}"
        print(' ', '-' * 31, formatted)
    print(f"\n    Total Distributed: {total_sum}\n")


# Resolves examples from `once_upon_a_talit.md`
def resolve_examples():
    examples = {
    'Classic': [Fraction(1), Fraction(1, 2)],
    'Example1': [Fraction(1), Fraction(1, 2), Fraction(1, 2)],
    'Example2': [Fraction(1), Fraction(1), Fraction(1, 2)],
    'Example3': [Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2)]
    }
    for name, example in examples.items():
        print(f"            {name}:\n")
        dispute = create_dispute(example)
        resolution = apply_the_talmudic_principles(dispute)
        print_resolution(resolution)
    
# Example Usage
if __name__ == "__main__":
    claims = [
        Fraction(1),
        Fraction(1, 2),
        Fraction(1, 2),
        Fraction(1, 3),
        Fraction(1, 4),
        Fraction(1),
    ]
    dispute = create_dispute(claims)
    resolution = apply_the_talmudic_principles(dispute)
    print_resolution(resolution)
    resolve_examples()
