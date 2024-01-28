/**
 * @file main.c
 * @brief This file contains the main function to apply Talmudic principle to a given dispute.
 * 
 * The main function in this file is `applyTalmudicPrincipal()`, which applies a Talmudic principle to a given dispute.
 * The Talmudic principle is applied as long as the remainder of the dispute is greater than 0.
 * If there are no partials in the dispute, the remainder is split equally among the disputants.
 * If there are partials in the dispute, the lowest concession is distributed among the disputants.
 * 
 * This file includes "dispute.h" for the definition of the Dispute structure and "distribution.h" for the distribution functions.
 * It also includes standard libraries stdio.h and stdlib.h for standard input/output and general purpose functions respectively.
 * 
 * @author Your Name
 * @version 1.0
 * @date 2022-01-01
 */

#include "dispute.h"

#include "distribution.h"

#include <stdio.h>
#include <stdlib.h>


/**
 * This function applies a Talmudic principle to a given dispute.
 * 
 * The Talmudic principle is applied as long as the remainder of the dispute is greater than 0.
 * 
 * If there are no partials in the dispute, the remainder is split equally among the disputants.
 * 
 * If there are partials in the dispute, the lowest concession is distributed among the disputants.
 * 
 * @param dispute - A pointer to the Dispute structure which contains the details of the dispute.
 */
void applyTalmudicPrincipal(Dispute *dispute)
{

    while (isGreaterThan(dispute->remainder, (Fraction){0, 1}))
    {

        if (!dispute->partialsCount)
        {

            splitRemainderEqually(dispute);
        }
        else
        {

            distributeLowestConcession(dispute);
        }
    }
}

int main()
{
    // Hardcoded because this is an early draft.
    Fraction fractions[6] = {{1, 1}, {1, 2}, {1, 2}, {1, 3}, {1, 4}, {1, 1}};
    Fractionlist claims = {fractions, 6};

    Dispute dispute = createDispute(&claims);
    applyTalmudicPrincipal(&dispute);

    Fraction totalDistributed = {0, 1};

    for (int i = 0; i < 6; i++)
    {
        totalDistributed = add(totalDistributed, dispute.claimants.claimants[i].collects);
        printClaimant(dispute.claimants.claimants[i]);
    }

    printf("\nTotal distributed: ");
    printFraction(totalDistributed);

    destroyDispute(&dispute);

    return 0;
}
