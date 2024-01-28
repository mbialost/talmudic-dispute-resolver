/**
 * @file fraction.h
 * @brief Fraction manipulation library for C.
 *
 * Provides structures and functions for representing and performing arithmetic
 * operations on fractions. Includes utilities for creating, simplifying, and
 * manipulating fractions, as well as performing arithmetic operations and comparisons.
 *
 * Structures:
 * - Fraction: Represents a fraction with numerator, denominator, and a validity flag.
 * - FractionAdjustments: Adjusts fractions for operations with a common denominator.
 * - Fractionlist: Manages a list of Fraction objects.
 *
 * Functions:
 * - greatestCommonDivisor: Computes the greatest common divisor of two integers.
 * - lowestCommonMultiple: Determines the least common multiple of two integers.
 * - simplify: Reduces a fraction to its simplest form.
 * - createFraction: Creates a valid, simplified fraction.
 * - Arithmetic operations (add, subtract, multiply, divide, multiplyByInt, divideByInt)
 * - toFloat: Converts a fraction to a double.
 * - Comparison functions (areEqual, isGreaterThan)
 * - printFraction: Outputs a fraction in readable format.
 *
 *
 * @author [mbialost]
 * @version [0.1]
 * @date [28-01-2024]
 */

#ifndef FRACTION_H
#define FRACTION_H

#include <stdbool.h>
#include <stdio.h>

// Defines a fraction with numerator, denominator, and a validity flag.
typedef struct
{
    int numerator;
    int denominator;
    bool isValid; // Indicates if the fraction's denominator is non-zero and valid.
} Fraction;

// Structure used for adjusting fractions to perform arithmetic operations with a common denominator.
typedef struct
{
    int numerator1; // Adjusted numerator for the first fraction.
    int numerator2; // Adjusted numerator for the second fraction.
    int lcd;        // Least common denominator for the two fractions.
} FractionAdjustments;

typedef struct
{
    Fraction *fractions;
    int size;
} Fractionlist;

// Mathematical utility functions.
int greatestCommonDivisor(int num1, int num2); // Uses Euclid's algorithm for finding GCD.
int lowestCommonMultiple(int num1, int num2);  // Utilizes GCD for calculating LCM.

// Fraction operations.
Fraction simplify(Fraction fraction);                    // Reduces fraction to simplest form by dividing both parts by their GCD.
Fraction createFraction(int numerator, int denominator); // Constructs a fraction, ensuring it's simplified and valid.

// Arithmetic operations for fractions, ensuring result simplification and validity.
Fraction add(Fraction fraction1, Fraction fraction2);
Fraction subtract(Fraction fraction1, Fraction fraction2);
Fraction multiply(Fraction fraction1, Fraction fraction2);
Fraction multiplyByInt(Fraction fraction1, int factor);
Fraction divide(Fraction fraction1, Fraction fraction2);
Fraction divideByInt(Fraction fraction1, int divisor);

// Conversion and comparison utilities.
double toFloat(Fraction fraction);                          // Converts fraction to double for comparison or other operations.
bool areEqual(Fraction fraction1, Fraction fraction2);      // Compares fractions by cross-multiplication to avoid floating-point errors.
bool isGreaterThan(Fraction fraction1, Fraction fraction2); // Determines if first fraction is larger using cross-multiplication.
void printFraction(Fraction fraction);                      // Displays fraction in human-readable format.

#endif // FRACTION_H
