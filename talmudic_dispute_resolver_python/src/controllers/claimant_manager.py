"""
Module: claimant_manager.py

Description:
- This module defines the 'ClaimantManager' class, which plays a central role in managing the operations related to claimants in dispute scenarios, specifically tailored for Talit disputes. 
- The ClaimantManager is responsible for creating claimants based on their claims, categorizing them as full or partial claimants, and handling the distribution of concessions and resolution of claims effectively.
- It provides a structured approach to managing the different phases of dispute resolution, from the initial categorization of claimants to the final allocation of the disputed object.

Classes:
    ClaimantManager: Manages the creation and handling of claimants in a dispute scenario. It includes key methods for categorizing claimants, distributing concessions, and resolving claims.

Key Functionalities:
- Creation of claimants from claims and categorization into full and partial claimants.
- Distribution of concessions to claimants, ensuring fair and efficient allocation.
- Dynamic management of claimants' statuses as their claims are resolved.

Usage:
- This class is intended to be used in conjunction with the 'Claimant' class and its subclasses, providing a streamlined process for managing the various aspects of dispute resolution involving claimants.

Note:
- The class makes use of the 'TalitFraction' class (imported as 'Fraction') for precise handling of fractional claims and concessions in the context of Talit disputes.
"""

from typing import Callable

from talmudic_dispute_resolver.src.models.dispute_fraction import (
    DisputeFraction as Fraction,
)
from talmudic_dispute_resolver.src.base.claimant import Claimant


class ClaimantManager:
    def __init__(self, claimant_factory: Callable[[str, Fraction], Claimant]) -> None:
        self.claimant_factory = claimant_factory

    def create_claimants(self, claims: list[Fraction]) -> list[Claimant]:
        return [
            self.claimant_factory(str(i + 1), claim) for i, claim in enumerate(claims)
        ]

    def distribute_to_claimants(
        self, fraction: Fraction, claimants: list[Claimant]
    ) -> list[Claimant]:
        for claimant in claimants:
            claimant.collect(fraction)
        return claimants

    def concede_from_claimants(
        self, fraction: Fraction, claimants: list[Claimant]
    ) -> list[Claimant]:
        for claimant in claimants:
            claimant.concede(fraction)
        return claimants

    def update_partial_claimants(self, claimants: list[Claimant]) -> tuple[list[Claimant]]:
        partial_claimants = [
            claimant for claimant in claimants if claimant.concession
        ]
        full_claimants = [
            claimant for claimant in claimants if not claimant.concession
        ]
        return partial_claimants, full_claimants
