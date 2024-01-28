/**
 * @file dispute.c
 * @brief Implementation of the Dispute management library for C.
 *
 * This module contains the definitions of functions declared in dispute.h.
 * It provides functionality for creating and managing Dispute structures, including allocation
 * and deallocation of resources, finding the lowest concession, and distributing claims among
 * claimants. Functions in this module leverage the Fraction and Distribution libraries to handle
 * fractional values and distributions accurately.
 *
 * @author [mbialost]
 * @version [0.1]
 * @date [28-01-2024]
 */

#include <stdio.h>
#include <stdlib.h>
#include "dispute.h"
#include "distribution.h"


/**
 * Constructs a new Dispute object based on a list of claims.
 * Initializes Claimants within the dispute, calculating partial and full claims.
 * It handles memory allocation for the claimants and exits with an error if allocation fails.
 *
 * @param claims A pointer to a list of fractions representing individual claims.
 * @return A Dispute structure with initialized claimants and their respective claims.
 */
Dispute createDispute(Fractionlist *claims)
{
    ClaimantList claimants;
    claimants.claimants = malloc(sizeof(Claimant) * claims->size);

    if (claimants.claimants == NULL)
    {
        fprintf(stderr, "Failed to allocate memory for claimants.\n");
        exit(EXIT_FAILURE);
    }

    claimants.size = claims->size;

    int partialsCount = 0;
    for (int i = 0; i < claims->size; i++)
    {

        claimants.claimants[i] = newClaimant(i, claims->fractions[i]);
        if (claimants.claimants[i].isPartial)
        {
            partialsCount++;
        }
    }
    Dispute dispute = {(Fraction){1, 1}, claimants, partialsCount};
    return dispute;
}

/**
 * Frees allocated memory associated with a Dispute object.
 * This function is crucial for preventing memory leaks in the application.
 *
 * @param dispute A pointer to the Dispute object to be destroyed.
 */
void destroyDispute(Dispute *dispute)
{
    if (dispute != NULL)
    {
        free(dispute->claimants.claimants);
        dispute->claimants.claimants = NULL;
    }
}

/**
 * Determines the lowest concession among partial claimants in a dispute.
 * This function is key in the distribution process to ensure fair allocation.
 *
 * @param dispute A pointer to the Dispute object.
 * @return A Fraction representing the lowest concession found.
 */
Fraction findLowestConcession(Dispute *dispute)
{
    Fraction currentLowest = {1, 1};

    for (int i = 0; i < dispute->claimants.size; i++)
    {
        Claimant currentClaimant = dispute->claimants.claimants[i];
        if (currentClaimant.isPartial && isGreaterThan(currentLowest, currentClaimant.concession))
        {
            currentLowest = currentClaimant.concession;
        }
    }
    return currentLowest;
}


/**
 * Distributes the lowest concession found among all claimants in the dispute.
 * This function adjusts claims and concessions of each claimant based on the distribution.
 *
 * @param dispute A pointer to the Dispute object.
 */
void distributeLowestConcession(Dispute *dispute)
{
    Fraction currentLowest = findLowestConcession(dispute);
    Distribution distribution = newDistribution(currentLowest, dispute->partialsCount, dispute->claimants.size);

    for (int i = 0; i < dispute->claimants.size; i++)
    {
        Claimant currentClaimant = dispute->claimants.claimants[i];
        if (currentClaimant.isPartial)
        {
            currentClaimant.collects = add(currentClaimant.collects, distribution.splitWithFulls);
            currentClaimant.concession = subtract(currentClaimant.concession, currentLowest);
            if (areEqual(currentClaimant.concession, (Fraction){0, 1}))
            {
                currentClaimant.isPartial = false;
                dispute->partialsCount -= 1;
            }
        }
        else
        {
            currentClaimant.collects = add(currentClaimant.collects, distribution.totalForFulls);
        }
        dispute->claimants.claimants[i] = currentClaimant;
    }
    dispute->remainder = subtract(
        dispute->remainder,
        multiplyByInt(distribution.perClaimantFraction, dispute->claimants.size));
}

/**
 * Splits the remainder evenly among all claimants in the dispute.
 * This function is used once all concessions in the dispute have been resolved.
 *
 * @param dispute A pointer to the Dispute object.
 */
void splitRemainderEqually(Dispute *dispute)
{
    Fraction dividedRemainder = divideByInt(dispute->remainder, dispute->claimants.size);
    for (int i = 0; i < dispute->claimants.size; i++)
    {
        dispute->claimants.claimants[i].collects = add(dispute->claimants.claimants[i].collects, dividedRemainder);
    }
    dispute->remainder = (Fraction){0, 1};
}