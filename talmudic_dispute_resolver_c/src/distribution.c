/**
 * @file distribution.c
 * @brief Implementation of the Distribution calculation library for C.
 *
 * This module contains the definitions of functions declared in distribution.h.
 * It focuses on calculating and managing the distribution of concessions among claimants.
 * The functions in this module utilize the Fraction manipulation library to accurately handle
 * fractional values during the distribution process, ensuring precise allocation of resources
 * among different parties.
 *
 * @author [mbialost]
 * @version [0.1]
 * @date [28-01-2024]
 */

#include "distribution.h"

/**
 * Creates a new Distribution object based on the provided concession, partialsCount, and totalClaimants.
 * The function calculates the distribution of a concession among claimants, considering both partial
 * and full claimants. It determines the fraction of the concession that each type of claimant receives.
 *
 * @param concession The fraction of the total value being conceded.
 * @param partialsCount The count of claimants with partial claims.
 * @param totalClaimants The total number of claimants.
 * @return A Distribution structure representing the calculated distribution of the concession.
 */
Distribution newDistribution(Fraction concession, int partialsCount, int totalClaimants)
{
    // Calculate the count of full claimants.
    int fullsCount = totalClaimants - partialsCount;

    // Calculate the fraction of the concession allocated to each claimant excluding the conceder.
    Fraction perClaimantFraction = divideByInt(concession, totalClaimants - 1);

    // Determine the fraction of the concession that partial claimants share with full claimants.
    Fraction splitWithFulls = divideByInt(perClaimantFraction, fullsCount + 1);

    // Calculate the total fraction of the concession received by full claimants.
    Fraction totalForFulls = add(perClaimantFraction, multiplyByInt(splitWithFulls, partialsCount));
    return (Distribution){concession, perClaimantFraction, splitWithFulls, totalForFulls};
}

/**
 * Prints the details of a Distribution object.
 * 
 * @param distribution A pointer to the Distribution object to be printed.
 */
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
