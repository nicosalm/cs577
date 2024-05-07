# Subset Sum

Given n integers A = {a1, ... an} and target sum t, is there a subset
S of A s.t. the sum of S = T

Weakly NP-Hard (pseudopolynomial)

Process:
    * View numbers in base 1 + max n_xi
    * triple (xi, xj, xk) -> 0000100001001000 (1's are i, j, k) 
    * t = 1111111111            = bi + bj + bk

# Partition

Given A = {a1, ... an} is there a subset S in A s.t.
the sum of S = sum A \ S = sum A / 2?

Reduction from Subset Sum to Partition:
    * Let sigma = sum A
    * add a_n+1 = sigma + t & add a_n+2 = 2 * sigma - t
    *       + sigma - t                  + t
    * Need to construct a subset which adds up to t by solving subset sum!

Weakly NP-Hard

# Rectangle Packing

Given rectangles R1 ... Ri ... Rn (with total area T),
can you pack them into a rectangle of exactly T space?

Reduction from Partition
    * ai -> 3ai
    * T = 2 * (3t or 3/2 sum A)
