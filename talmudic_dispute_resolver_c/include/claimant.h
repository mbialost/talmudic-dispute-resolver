/**
 * @file claimant.h
 * @brief Claimant management module for handling claim-related data.
 *
 * This module provides structures and functions for managing claimants and their associated claims,
 * represented as fractions. It includes utilities for creating claimants and managing a list of them.
 *
 * Structures:
 * - Claimant: Represents a claimant with an identifier and fractions for claim, concession, and collects. 
 *             Includes a flag indicating if the claim is partial.
 * - ClaimantList: Manages a list of Claimant objects.
 *
 * Functions:
 * - newClaimant: Creates a new Claimant object with given identifier and claim.
 * - printClaimant: Outputs the details of a Claimant object in a readable format.
 *
 * @author [mbialost]
 * @version [0.1]
 * @date [28-01-2024]
 */

#ifndef CLAIMANT_H
#define CLAIMANT_H

#include <stdbool.h>
#include "fraction.h"

// Represents a claimant with various fractional claims and a partiality flag.
typedef struct {
    int identifier;      // Unique identifier for the claimant.
    Fraction claim;      // The fraction representing the claim.
    Fraction concession; // The fraction representing the concession.
    Fraction collects;   // The fraction representing the collection amount.
    bool isPartial;      // Flag indicating if the claim is partial.
} Claimant;

// Manages a list of Claimant objects.
typedef struct {
    int size;         // Number of Claimants in the list.
    Claimant* claimants; // Pointer to array of Claimant objects.
} ClaimantList;

// Creates a new Claimant object .
Claimant newClaimant(int identifier, Fraction claim);

// Displays the details of a Claimant object in a readable format.
void printClaimant(Claimant claimant);

#endif // CLAIMANT_H
