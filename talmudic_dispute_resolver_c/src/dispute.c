#include <stdio.h>
#include <stdlib.h>
#include "dispute.h"
#include "distribution.h"

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

void destroyDispute(Dispute *dispute)
{
    if (dispute != NULL)
    {
        free(dispute->claimants.claimants);
        dispute->claimants.claimants = NULL;
    }
}

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

void splitRemainderEqually(Dispute *dispute)
{
    Fraction dividedRemainder = divideByInt(dispute->remainder, dispute->claimants.size);
    for (int i = 0; i < dispute->claimants.size; i++)
    {
        dispute->claimants.claimants[i].collects = add(dispute->claimants.claimants[i].collects, dividedRemainder);
    }
    dispute->remainder = (Fraction){0, 1};
}