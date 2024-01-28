/**
 * @file claimant.c
 * @brief Implementation of the Claimant management library for C.
 *
 * This module contains the definitions of functions declared in claimant.h.
 * It includes the implementation of functions for creating and managing Claimant structures.
 * These functions leverage the Fraction manipulation library for operations involving claims
 * and concessions, ensuring accuracy in the representation and calculations of fractional values.
 *
 * @author [mbialost]
 * @version [0.1]
 * @date [28-01-2024]
 */

#include <stdio.h>
#include <stdlib.h>
#include "claimant.h"

// Constructs a new Claimant object with the given identifier and claim.
// The function computes the concession, which is the remainder of the claim subtracted from 1,
// and checks if the concession is greater than zero to determine if the claim is partial.
Claimant newClaimant(int identifier, Fraction claim)
{
    Fraction concession = subtract(createFraction(1, 1), claim);
    bool isPartial = isGreaterThan(concession, (Fraction){0, 1});
    return (Claimant){identifier, claim, concession, (Fraction){0, 1}, isPartial};
}

// Prints the details of a Claimant, including the identifier and the fractions representing
// the claim and the amount the claimant collects. This function uses the printFraction function
// from the Fraction manipulation library to display the fractional values.
void printClaimant(Claimant claimant)
{
    printf("\nClaimant %i:\n  - Claim: ", claimant.identifier);
    printFraction(claimant.claim);
    printf("  - Collects: ");
    printFraction(claimant.collects);
}
