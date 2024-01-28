#ifndef CLAIMANT_H
#define CLAIMANT_H

#include <stdbool.h>
#include "fraction.h"

typedef struct {
    int identifier;
    Fraction claim;
    Fraction concession;
    Fraction collects;
    bool isPartial;
} Claimant;

typedef struct {
    int size;
    Claimant* claimants;
} ClaimantList;


Claimant newClaimant(int identifier, Fraction claim);
void printClaimant(Claimant claimant);

#endif // CLAIMANT_H

