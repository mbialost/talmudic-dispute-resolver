/**
 * @file dispute.h
 * @brief Dispute resolution module for handling disputes involving claimants.
 *
 * This module provides structures and functions for managing disputes, 
 * which involve claimants with fractional claims. It includes utilities for 
 * creating disputes, finding the lowest concession, distributing concessions,
 * and splitting remainders.
 *
 * Structures:
 * - Dispute: Manages the details of a dispute including claimants and remaining fractions.
 *
 * Functions:
 * - createDispute: Initializes a Dispute object with a given list of claims.
 * - destroyDispute: Frees resources associated with a Dispute object.
 * - findLowestConcession: Identifies the lowest concession in a dispute.
 * - distributeLowestConcession: Distributes the lowest concession among claimants.
 * - splitRemainderEqually: Splits any remaining fractions equally among claimants.
 *
 * @author [Your Name]
 * @version [0.1]
 * @date [Date]
 */

#ifndef DISPUTE_H
#define DISPUTE_H

#include "claimant.h"

// Manages the details of a dispute including claimants and remaining fractions.
typedef struct {
    Fraction remainder;    // The remaining fraction after distributions.
    ClaimantList claimants; // A list of claimants involved in the dispute.
    int partialsCount;     // Number of partial claimants in the dispute.
} Dispute;

// Function declarations
Dispute createDispute(Fractionlist* claims); // Initializes a Dispute object with given claims.
void destroyDispute(Dispute* dispute);       // Frees resources associated with a Dispute.
Fraction findLowestConcession(Dispute* dispute); // Identifies the lowest concession in a dispute.
void distributeLowestConcession(Dispute* dispute); // Distributes the lowest concession among claimants.
void splitRemainderEqually(Dispute* dispute); // Splits remaining fractions equally among claimants.

#endif // DISPUTE_H
