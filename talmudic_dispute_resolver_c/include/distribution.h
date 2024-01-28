#ifndef DISTRIBUTION_H
#define DISTRIBUTION_H

#include "fraction.h"

typedef struct {
    Fraction currentConcession;
    Fraction perClaimantFraction;
    Fraction splitWithFulls;
    Fraction totalForFulls;
} Distribution;

Distribution newDistribution(Fraction concession, int partialsCount, int totalClaimants);
void printDistribution(Distribution* distribution);
#endif // DISTRIBUTION_H
