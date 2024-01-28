"שנים אוחזין בטלית זה אומר אני מצאתיה וזה אומר אני מצאתיה זה אומר כולה שלי וזה אומר כולה שלי זה ישבע שאין לו בה פחות מחציה וזה ישבע שאין לו בה פחות מחציה ויחלוקו

זה אומר כולה שלי וזה אומר חציה שלי האומר כולה שלי ישבע שאין לו בה פחות משלשה חלקים והאומר חציה שלי ישבע שאין לו בה פחות מרביע זה נוטל שלשה חלקים וזה נוטל רביע"

## Introduction.
This document delves into the captivating world of Talmudic jurisprudence, focusing on a particular case study involving a dispute over a singular garment, known as a talit. It explores the application of Talmudic principles in resolving disputes over shared property, especially when the claims of the involved parties differ.

## Abstract

The analysis presented in this document centers on the Talmudic division algorithm. Although this algorithm is not exclusive to the talit problem and is referenced in various contexts of resource distribution, it is notably discussed on the very first page of a tractate commonly used as an introductory study text in Yeshiva education worldwide. For centuries, this problem, initially comprising a few passages focused on judicial details pertinent to Talmudic law (such as the oath (Shevua) a claimant must take to secure their claimed portion, or cases involving witnesses), has evolved into a subject of extensive analysis. Numerous commentators have explored its game-theoretical aspects, particularly in scenarios where multiple parties claim different portions of a single item, such as a garment (talit).

## The Talmudic Case of the Talit

### Scenario Overview
The Talmud discusses a scenario where two or more parties lay claim to a single talit, each asserting that they have found it. The guidelines for equitable distribution are outlined in two primary scenarios:

1. **Equal Claim Scenario**: When both parties claim the entire garment, it is divided equally.
2. **Unequal Claim Scenario**: If one party claims the entire garment and the other only half, the first receives three-quarters, while the latter receives one-quarter.

This allocation strategy has intrigued many. Given that the claims revolve around the discovery of the talit, and considering that the Talmud specifies the claimants are holding or grabbing the talit (a method of asserting ownership by possession in Talmudic law), the rationale behind such distribution seems counterintuitive. Why should the party claiming only half, perhaps appearing more honest, lose a quarter of their claim?

### Rationale from Talmudic Commentators

The Rishonim, early Talmudic commentators, provide a rationale for these rules:

- Claiming only a portion of a garment is tantamount to conceding the remainder to the other party.
- Thus, a claim for half instantly awards the other party a half share.
- The disputed remainder is then divided equally, as both claimants have an equal stake in it.

#### Application to Multiple Claimants

In applying Talmudic principles as an algorithm for dispute resolution involving multiple claimants, the following steps are considered:

- **Application of Concessions:** Initially, any explicit concessions by the parties are directly applied, which involves allocating the conceded fraction to the non-conceding parties.
- **Even Division of Remainders:** In the absence of further concessions, the remaining part of the item (in this case, the talit) is evenly split among all claimants.

However, the Talmudic framework is primarily designed for disputes involving two parties, where concessions are absolute and directly involve a single other party. This framework does not explicitly guide handling situations with concessions involving multiple parties, adding a layer of complexity.

The complexity is notably amplified when applying these rules to scenarios with more than two claimants. The concessions and claims become multi-dimensional, requiring a more sophisticated approach. This complexity becomes especially pronounced with the addition of even one more conceding party.

I recall first grappling with this problem as a teenager, introduced to me by my grandfather during his visit to the Yeshiva I attended. At that time, we were studying this specific part of the Talmud. The scenario he presented, which I later discovered had been discussed in various other sources, unfolds as follows:

### Case Studies

**Case 1:** 'A' claims the entire talit, while 'B' and 'C' each claim half.

2.1. **Initial Consideration**:
   - **a.** 'B' and 'C' concede half to 'A', effectively granting 'A' half of the talit.
   - **b.** The remaining half is then divided between 'B' and 'C', with each receiving `1/4`.

   This approach, however, deviates from the principle of evenly splitting the disputed portion. Even if we accept that 'B' and 'C' resolved their concessions by granting half to 'A', 'A' still asserts a claim on the remainder without any concession.

   This distribution also contrasts with the Talmudic scenario (3/4 - 1/4 split). While 'B' (claiming 1/2) retains the same portion (`1/4`) in both cases, 'A's share is reduced to account for 'C', the additional claimant.
 
2.2. **Alternative Approach**:
   - **a.** 'B' and 'C' each concede half to 'A', resulting in 'A' receiving half of the talit.
   - **b.** The remaining half is divided among all three, yielding a `4/6, 1/6, 1/6` split.

   This division appears to align with the principle of evenly splitting what remains. It symmetrically reduces the shares of 'A' and 'B' by `1/12`: 'A' from `3/4` to `4/6` and 'B' from `1/4` to `1/6`.

   However, this distribution is still not proportionate, as it does not fully consider the mutual concessions of 'B' and 'C'. The concessions by 'B' and 'C' are not exclusively to 'A', but are also implicitly to each other. Consequently, an even split of the remainder cannot be equitable and consistent with the Talmudic principle since granting half to 'A' does not capture and resolve the full dynamics of the concessions by the others.

   Furthermore, as 'A' maintains their full claim, including on the fractions conceded between 'B' and 'C', the symmetry in reduction appears unjustified considering 'A's unchanged claim in the portion disputed between 'B' and 'C'. The symmetry in reduction (when allocating a portion to 'C') fails to account for 'A's greater claim.

2.3. **Resolution**:
   - **a.** Unless they are unanimous (if every other claimant concedes), concessions are made to the remaining claimants, not to specific individuals.
   - **b.** Therefore, divide that concession by the number of others (as we would have done if all the others had equal stakes to it).
   - **c.** This unanimous net concession to 'A' is `1/4`, as both 'B' and 'C' concede at least a quarter each directly to 'A'.
   - **d.** The disputed part of the concessions (`1/4` from each) is evenly divided between 'A' and each of the others since their respective stakes to it are equal once their concessions have been distributed and resolved.
   - **e.** 'A' ends up with `1/4 + 1/8` (from 'B') + `1/8` (from 'C') + `1/12` (even split of the remaining `1/4`), totaling `7/12`.
   - **f.** 'B' and 'C' each receive `1/8` from their dispute with 'A' + `1/12`, totaling `5/24` each.

**Final Distribution**:
- 'A': `7/12` (or `14/24`)
- 'B': `5/24`
- 'C': `5/24`


### Case 2: 'A' and 'B' each claim the entire talit, while 'C' claims half.

- **Step a**: 'C' concedes half to 'A' and 'B', but not to either specifically. This conceded half is equally divided between 'A' and 'B', so each gets `1/4` of the talit.
- **Step b**: The other half, disputed by all three, is split evenly, resulting in `1/6` each.
- **Step c**: Final distribution calculation:
  - 'A' receives `1/4 + 1/6 = 5/12`.
  - 'B' receives `1/4 + 1/6 = 5/12`.
  - 'C' receives `1/6`.

### Case 3: 'A' and 'B' each claim the entire talit, while 'C' and 'D' claim hlaf.

- **Step a**: 'C' and 'D' concede `1/2` each, which becomes `1/6` to each of the 3 other claimants. This results in 'A' and 'B' each receiving a concession of `1/6` from 'C' and 'D' respectively.
- **Step b**: The unanimous net concession of `2/6` (or `1/3`) from 'C' and 'D' to 'A' and 'B'.
- **Step c**: 'A' and 'B' split this unanimous concession, collecting `1/6` each.
- **Step d**: The `1/6` conceded by 'C' to 'D', and vice versa, remains disputed among the three others. Each `1/6` is split between its 3 claimants, each collecting `1/18`.
- **Step e**: Division so far:
  - 'A' and 'B' receive `1/6 + 1/18 = 5/18` each.
  - 'C' and 'D' receive `1/18` each. (Total distributed: `2/3`)
- **Step f**: The remaining `1/3`, with no concessions, is evenly split, adding `1/12` to each claimant.

**Final Distribution**:
- 'A': `5/18 + 1/12 = 11/36`
- 'B': `5/18 + 1/12 = 11/36`
- 'C': `1/18 + 1/12 = 5/36`
- 'D': `1/18 + 1/12 = 5/36`

