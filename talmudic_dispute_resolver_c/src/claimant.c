#include <stdio.h>
#include <stdlib.h>
#include "claimant.h"

Claimant newClaimant(int identifier, Fraction claim)
{
    Fraction concession = subtract(createFraction(1, 1), claim);
    bool isPartial = isGreaterThan(concession, (Fraction){0, 1});
    return (Claimant){identifier, claim, concession, (Fraction){0, 1}, isPartial};
}

void printClaimant(Claimant claimant)
{
    printf("\nClaimant %i:\n  - Claim: ", claimant.identifier);
    printFraction(claimant.claim);
    printf("  - Collects: ");
    printFraction(claimant.collects);
}
