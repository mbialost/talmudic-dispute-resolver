"""
This module provides the core functionalities for managing a Talit dispute resolution process.

It includes the 'Talit' class, representing the disputed object, and the 'DisputeManager' class, 
which oversees the entire dispute resolution process including the allocation 
and distribution of the Talit according to various claims.

Key Classes:
    DisputeManager: Manages the dispute resolution process, 
        handling the allocation of the Talit and tracking the status of various claimants.

Overview:.
    The 'DisputeManager' class orchestrates the resolution process. 
    It manages claimants, both full and partial, and directs the distribution of the Talit's fractions
    based on the claims and resolutions reached.

Note: 
    The module utilizes the 'TalitFraction' class (aliased as 'Fraction') for managing fractional claims and concessions.
"""

import logging
from dataclasses import dataclass
from ..models.dispute_fraction import DisputeFraction as Fraction
from ..base.disputed_resource import DisputedResource
from ..controllers.claimant_manager import ClaimantManager


logger = logging.getLogger(__name__)


@dataclass
class Distribution:
    concession: Fraction
    claimant_count: int
    fulls_count: int

    def __post_init__(self):
        self.full_share = self.concession / (self.claimant_count - 1)
        self.partial_share = self.full_share / (self.fulls_count + 1)


class Dispute:
    """Manages the resolution process for disputes involving a Talit.

    This class is responsible for overseeing the entire dispute resolution process,
    including tracking and updating dispute data, managing allocations based on claimant concessions,
    and distributing the Talit.

    Attributes:
        talit (DisputedObject): The disputed Talit object.
        claimant_manager (ClaimantManager): Manages claimant-related operations.
        full_claimants (list[Claimant]): List of claimants with full claims.
        partial_claimants (list[Claimant]): List of claimants with partial claims.
        claimant_count (int): Total number of claimants.

    Methods:
        __init__: Initializes the DisputeManager with the Talit object and ClaimantManager.
        split_remainder_equally: Distributes the remaining Talit fraction equally among full claimants.
        calculate_per_claimant_fraction: Calculates the Talit fraction for each claimant based on the lowest concession.
        calculate_allocation_for_claimant_groups: Calculates Talit fractions for full and partial claimants.
        calculate_allocations: Determines distributions for full and partial claimants, including total distribution.
        distribute_lowest_concession: Manages the distribution of concessions among claimants in a single cycle.
    """

    def __init__(
        self, talit: DisputedResource, claims: list[Fraction], claimant_manager: ClaimantManager
    ) -> None:
        """Initializes the DisputeManager with a Talit object and a ClaimantManager.

        Args:
            talit (Talit): The Talit object representing the disputed item.
            claimant_manager (ClaimantManager): Manager responsible for creating and handling claimants.
        """
        self.talit = talit
        self.claimant_manager = claimant_manager
        
        self.claimant_count = len(claims)
        self.partial_claimants = self.claimant_manager.create_claimants(sorted(claims, reverse=True))
        self.full_claimants = []
        
        self.update_claimant_statuses()        
        logger.info("Dispute setup complete.")

    def split_remainder_equally(self) -> None:
        remainder_share = self.talit.remainder / self.claimant_count
        self.talit.allocate(self.talit.remainder)
        self.claimant_manager.distribute_to_claimants(
            remainder_share, self.full_claimants
        )

    def distribute_concession(self, distribution: Distribution) -> None:  
        self.claimant_manager.concede_from_claimants(distribution.concession, self.partial_claimants)      
        self.claimant_manager.distribute_to_claimants(
            distribution.full_share, self.full_claimants
        )
        self.claimant_manager.distribute_to_claimants(
            distribution.partial_share, self.partial_claimants
        )
        self.claimant_manager.distribute_to_claimants(
            distribution.partial_share * len(self.partial_claimants), self.full_claimants
        )
        
    def update_claimant_statuses(self) -> None:
        status_updates = self.claimant_manager.update_partial_claimants(self.partial_claimants)
        self.partial_claimants = status_updates[0]
        self.full_claimants.extend(status_updates[1])
        
    def handle_distribution(self, concession: Fraction) -> None:
        distribution = Distribution(concession, self.claimant_count, len(self.full_claimants))
        self.talit.allocate(distribution.full_share * self.claimant_count)
        self.distribute_concession(distribution)
        self.update_claimant_statuses()

        