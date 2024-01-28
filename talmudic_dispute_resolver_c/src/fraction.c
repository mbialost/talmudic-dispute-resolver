/**
 * @file fraction.c
 * @brief Implementation of the Fraction manipulation library for C.
 *
 * This module contains the definitions of functions declared in fraction.h.
 * It includes the implementation of arithmetic operations, utility functions,
 * and other functionalities related to fractions.
 *
 * @author [mbialost]
 * @version [0.1]
 * @date [28-01-2024]
 */

#include <stdlib.h>
#include "fraction.h"

// Euclid's algorithm for finding the GCD of two numbers. The loop iteratively replaces
// the larger number with the remainder of the larger number divided by the smaller one.
// This process repeats until the smaller number becomes 0, leaving the GCD in the other variable.
int greatestCommonDivisor(int num1, int num2)
{
    while (num2 != 0)
    {
        int temp = num2;
        num2 = num1 % num2;
        num1 = temp;
    }
    return num1;
}

// Computes LCM using the relationship between GCD and LCM, important for adding or subtracting fractions.
int lowestCommonMultiple(int num1, int num2)
{
    return (num1 / greatestCommonDivisor(num1, num2)) * num2;
}

// Simplifies fractions, crucial for maintaining accuracy and reducing complexity in operations.
Fraction simplify(Fraction fraction)
{
    int gcd = greatestCommonDivisor(fraction.numerator, fraction.denominator);
    return (Fraction){fraction.numerator / gcd, fraction.denominator / gcd, fraction.isValid};
}

// Creates a fraction, returning an error code if the fraction is invalid.
Fraction createFraction(int numerator, int denominator)
{
    bool isValid = denominator > 0 && numerator <= denominator;
    Fraction fraction = {numerator, denominator, isValid};
    return simplify(fraction);
}

// Adjusts fractions to have the same denominator, ensuring exact division since
// the least common denominator (lcd) is by definition a multiple of both denominators.
FractionAdjustments adjustForOperation(Fraction fraction1, Fraction fraction2)
{
    int lcd = lowestCommonMultiple(fraction1.denominator, fraction2.denominator);
    int adjustedNumerator1 = fraction1.numerator * (lcd / fraction1.denominator);
    int adjustedNumerator2 = fraction2.numerator * (lcd / fraction2.denominator);
    return (FractionAdjustments){adjustedNumerator1, adjustedNumerator2, lcd};
}

// Each arithmetic function below ensures the results are simplified and valid, which is crucial for accuracy and usability.

Fraction add(Fraction fraction1, Fraction fraction2)
{
    FractionAdjustments adj = adjustForOperation(fraction1, fraction2);
    return createFraction(adj.numerator1 + adj.numerator2, adj.lcd);
}

Fraction subtract(Fraction fraction1, Fraction fraction2)
{
    FractionAdjustments adj = adjustForOperation(fraction1, fraction2);
    return createFraction(adj.numerator1 - adj.numerator2, adj.lcd);
}

Fraction multiply(Fraction fraction1, Fraction fraction2)
{
    return createFraction(fraction1.numerator * fraction2.numerator, fraction1.denominator * fraction2.denominator);
}

Fraction multiplyByInt(Fraction fraction1, int factor)
{
    return createFraction(fraction1.numerator * factor, fraction1.denominator);
}

Fraction divide(Fraction fraction1, Fraction fraction2)
{
    return createFraction(fraction1.numerator * fraction2.denominator, fraction1.denominator * fraction2.numerator);
}

Fraction divideByInt(Fraction fraction1, int divisor)
{
    return createFraction(fraction1.numerator, fraction1.denominator * divisor);
}

// Conversions and comparisons are implemented to avoid floating-point errors and ensure accurate results.

double toFloat(Fraction fraction)
{
    return (double)fraction.numerator / fraction.denominator;
}

bool areEqual(Fraction fraction1, Fraction fraction2)
{
    return fraction1.numerator * fraction2.denominator == fraction2.numerator * fraction1.denominator;
}

bool isGreaterThan(Fraction fraction1, Fraction fraction2)
{
    return fraction1.numerator * fraction2.denominator > fraction2.numerator * fraction1.denominator;
}

void printFraction(Fraction fraction)
{
    printf("%d/%d\n", fraction.numerator, fraction.denominator);
}
