#include "dispute.h"

#include "distribution.h"

#include <stdio.h>
#include <stdlib.h>

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
