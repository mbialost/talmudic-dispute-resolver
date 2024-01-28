
"""
This module implements a fair-division algorithm  inspired by the Talmudic scenario known as: 
        "Two who are grasping a (disputed) garment (שניים אוחזין בטלית)". 

Note:
    This version of the fair-division algorithm is streamlined to highlight its core principles 
    rather than practical application. Consequently, it omits comprehensive error handling to maintain simplicity. 
    For a more robust and detailed implementation, refer to the official documentation.
    
Use:
    The example provided in the 'main' block demonstrates the function's usage, including formatting and printing the outcomes.
"""
from fractions import Fraction


def distribute_based_on_concessions(claims: list[Fraction]) -> Fraction:
    """
    Distributes a disputed resource based on fractional claims using a concession-based approach.

    This algorithm resolves disputes over shared resources by distributing them according to the concessions
    implied by each claim (1 - claim = concession). This provides a dynamic and fair allocation, reflecting 
    the relative size of each claim.

    Algorithm Process:
        1. Concession Distribution:
        - Orders claims in descending order to ensure that the division of each conceded fraction is applicable 
          to all subsequent claims.
        - For each claim, calculates the remaining concession by subtracting already resolved concessions.
        - Allocates shares of this concession to partial and full claims, with partial claims receiving a share 
          that is further divided among each partial and all full claims (at that point).

        3. Cumulative Allocation:
        - Cumulatively calculates the allocation for each claim based on the index at which they became full.
        - This is the sum of allocations for partials up to that point, and allocations for fulls from that point onwards.

        4. Final Distribution: 
        - Calculates any remaining resource not yet allocated and divides it evenly.
        - Combines the cumulative allocations and the remainder share to determine the final allocation for each claim.
        
    Args:
        claims (list[Fraction]): Fractional claims to the resource, where each Fraction represents a part of the whole.

    Returns:
        (list[tuple]): Each tuple contains (claimant index, original claim, final allocation), where both claim and allocation
        are represented as Fractions.
        
    Example:
        >>> claims = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]
        >>> distribute_based_on_concessions(claims)
        [
            (1, Fraction(1, 2), Fraction(31, 72)),
            (2, Fraction(1, 3), Fraction(11, 36)),
            (3, Fraction(1, 4), Fraction(19, 72))
        ]
    """
    # Immediately sort from largest to smallest to ensure the index for each claim never changes.
    claims = sorted(claims, reverse=True)

    # Check if there is no dispute.
    if sum(claims) <= 1:
        return [(i + 1, claim, claim) for i, claim in enumerate(claims)]
            
    # Tracks the statuses of claims throughout the iteration.
    full_claims, partial_claims = 0, len(claims)
    other_claims = partial_claims - 1  # Excludes the conceding party from their own concession division.

    # Tracks the portions of each concession allocated for each status. 
    allocations_partials, allocations_fulls = [], []
    resolved_concessions = Fraction(0)  # Tracks cumulative accounted concessions.

    for claim in claims:
        remaining_concession = (1 - claim) - resolved_concessions
        resolved_concessions += remaining_concession
        
        per_claim_share = remaining_concession / other_claims

        # Allocate portions for each status.
        allocations_partials.append(per_claim_share / (full_claims + 1))
        allocations_fulls.append(per_claim_share + (partial_claims * allocations_partials[-1]))

        partial_claims -= 1
        full_claims += 1

    # Accumulate shares for each claim based on index.
    cumulative_for_fulls = [sum(allocations_fulls[i + 1 :]) for i in range(len(claims))]
    cumulative_for_partials = [sum(allocations_partials[: i + 1]) for i in range(len(claims))]

    remainder = 1 - sum(cumulative_for_partials + cumulative_for_fulls)
    remainder_share = remainder / len(claims)

    final_distribution = [
        (i, claim, cumulative_for_fulls[i] + cumulative_for_partials[i] + remainder_share)
        for i, claim in enumerate(claims)
    ]

    return final_distribution


def solve_and_print(name, claims):
    results = distribute_based_on_concessions(claims)
    total = 0

    print(f'\nResults for {name}:')
    for i, claim, outcome in results:
        print(f"  Claimant {i+1}\n   - Claim: {claim}\n   - Outcome: {outcome}\n")
        total += outcome

    # Must be equal to 1.
    print(f"Total distributed: {total}")



def main():
    cases = {
        # Talmudic scenarios:
        'Scenario 1': [Fraction(1), Fraction(1)],
        'Scenario 2': [Fraction(1), Fraction(1, 2)],

        'No dispute': [Fraction(1, 2), Fraction(1, 4), Fraction(1, 4)],

        # From `once_upon_a_talit.md`
        'Case 1': [Fraction(1), Fraction(1, 2), Fraction(1, 2)],
        'Case 2': [Fraction(1), Fraction(1), Fraction(1, 2)],
        'Case 3': [Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2)]
    }
    for name, claims in cases.items():
        solve_and_print(name, claims)

if __name__ == "__main__":
    main()


