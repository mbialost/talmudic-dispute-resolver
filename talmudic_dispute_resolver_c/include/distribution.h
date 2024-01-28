/**
 * @file distribution.h
 * @brief Distribution management library for C.
 *
 * This library provides structures and functions for managing distributions 
 * in a system that involves concession, claimants, and distributions. 
 * It relies on the fraction library for precise arithmetic operations.
 *
 * Structures:
 * - Distribution: Manages the distribution details involving various fractions.
 *
 * Functions:
 * - newDistribution: Creates a new Distribution object.
 * - printDistribution: Outputs the details of a Distribution object.
 *
 * @author [Your Name]
 * @version [0.1]
 * @date [Date]
 */

#ifndef DISTRIBUTION_H
#define DISTRIBUTION_H

#include "fraction.h"

// Represents the distribution of concessions and claims.
typedef struct {
    Fraction currentConcession;    // The current concession as a fraction.
    Fraction perClaimantFraction;  // Fraction of distribution per claimant.
    Fraction splitWithFulls;       // Fraction to be split among full claimants.
    Fraction totalForFulls;        // Total fraction allocated for full claimants.
} Distribution;

// Constructs a new Distribution object given a concession and claimant count.
// concession - the initial concession as a fraction.
// partialsCount - number of partial claimants.
// totalClaimants - total number of claimants.
Distribution newDistribution(Fraction concession, int partialsCount, int totalClaimants);

// Displays the distribution in a human-readable format.
// distribution - pointer to the Distribution object to be printed.
void printDistribution(Distribution* distribution);

#endif // DISTRIBUTION_H
