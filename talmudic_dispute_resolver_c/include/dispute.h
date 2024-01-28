#include "claimant.h"

typedef struct {
    Fraction remainder;
    ClaimantList claimants;
    int partialsCount;
} Dispute;


Dispute createDispute(Fractionlist* claims);
void destroyDispute(Dispute* dispute);
Fraction findLowestConcession(Dispute* dispute);
void distributeLowestConcession(Dispute* dispute);
void splitRemainderEqually(Dispute* dispute);
