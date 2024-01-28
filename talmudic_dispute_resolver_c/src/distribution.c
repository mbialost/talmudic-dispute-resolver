#include "distribution.h"

Distribution newDistribution(Fraction concession, int partialsCount, int totalClaimants)
{
    int fullsCount = totalClaimants - partialsCount;

    // Divide the concession between all claimants other than the conceder.
    Fraction perClaimantFraction = divideByInt(concession, totalClaimants - 1);

    // Partial claimants each split their perClaimantFraction with all full claimants.
    Fraction splitWithFulls = divideByInt(perClaimantFraction, fullsCount + 1);

    // Fulls recieve both the perClaimantFraction, and a splitWithFulls portion from each partial.
    Fraction totalForFulls = add(perClaimantFraction, multiplyByInt(splitWithFulls, partialsCount));
    return (Distribution){concession, perClaimantFraction, splitWithFulls, totalForFulls};
}

void printDistribution(Distribution *distribution)
{
    printf("\nDistribution for concession of ");
    printFraction(distribution->currentConcession);
    printf("  - Per claimant fraction: ");
    printFraction(distribution->perClaimantFraction);
    printf("  - Split with fulls: ");
    printFraction(distribution->splitWithFulls);
    printf("  - Total for fulls: ");
    printFraction(distribution->totalForFulls);
}

// Python implementation:

// @dataclass
// class Distribution:
//     concession: Fraction
//     partials_count: int
//     total_claimant_count: int

//     def __post_init__(self) -> None:
//         fulls_count = self.total_claimant_count- self.partials_count
//         self.per_claimant_fraction = self.concession / (self.total_claimant_count - 1)
//         self.split_with_fulls = self.per_claimant_fraction / (fulls_count + 1)
//         self.for_fulls = self.per_claimant_fraction + (self.partials_count * self.split_with_fulls)
