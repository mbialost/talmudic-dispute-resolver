#ifndef FRACTION_H
#define FRACTION_H

#include <stdbool.h>
#include <stdio.h>

// Defines a fraction with numerator, denominator, and a validity flag.
typedef struct {
    int numerator;
    int denominator;
    bool isValid; // Indicates if the fraction's denominator is non-zero and valid.
} Fraction;

// Structure used for adjusting fractions to perform arithmetic operations with a common denominator.
typedef struct {
    int numerator1; // Adjusted numerator for the first fraction.
    int numerator2; // Adjusted numerator for the second fraction.
    int lcd;        // Least common denominator for the two fractions.
} FractionAdjustments;

typedef struct {
    Fraction* fractions;
    int size;
} Fractionlist;

// Mathematical utility functions.
int greatestCommonDivisor(int num1, int num2); // Uses Euclid's algorithm for finding GCD.
int lowestCommonMultiple(int num1, int num2);  // Utilizes GCD for calculating LCM.

// Fraction operations.
Fraction simplify(Fraction fraction); // Reduces fraction to simplest form by dividing both parts by their GCD.
Fraction createFraction(int numerator, int denominator); // Constructs a fraction, ensuring it's simplified and valid.

// Arithmetic operations for fractions, ensuring result simplification and validity.
Fraction add(Fraction fraction1, Fraction fraction2);
Fraction subtract(Fraction fraction1, Fraction fraction2);
Fraction multiply(Fraction fraction1, Fraction fraction2);
Fraction multiplyByInt(Fraction fraction1, int factor);
Fraction divide(Fraction fraction1, Fraction fraction2);
Fraction divideByInt(Fraction fraction1, int divisor);

// Conversion and comparison utilities.
double toFloat(Fraction fraction); // Converts fraction to double for comparison or other operations.
bool areEqual(Fraction fraction1, Fraction fraction2); // Compares fractions by cross-multiplication to avoid floating-point errors.
bool isGreaterThan(Fraction fraction1, Fraction fraction2); // Determines if first fraction is larger using cross-multiplication.
void printFraction(Fraction fraction); // Displays fraction in human-readable format.

#endif // FRACTION_H
