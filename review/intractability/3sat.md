# Complexity, NP-Completeness, Reductions

Recall:

P = {Problems solvable in polynomial time}
NP = {Decision problems (yes or no) solvable in non-deterministic polynomial time }

Non-deterministic:
    * Guess one out of polynomially many options in O(1) time
    * If any guess leads to a yes answer, then we get such a guess
    * Asymmetric and bias towards yes

## 3-SAT
Given Boolean formula of form:

> (x_1 or x_3 or !x_6) and (!x_2 or x_3 or !x_7) and ...

Each or clause only has **3** literals in it. 

Decision question (Yes/No): Can you set the variables x1, x2, ... -> {T, F}
such that formula = T (Satisfying assignment)

This problem is in NP:
    * Guess whether x1 = T or F, x2 = T or F ...
    * Check whether formula is satisfied -> { Yes: True, No: False }

## Definitions

NP = { Decision problems with polynomial-size certificates &
        polynomial-time verifiers for YES inputs } 

X is NP-Complete if X in NP & X is NP-Hard

X is NP-Hard if every problem Y in NP reduces to X

Reduction from problem A -> problem B = polynomial time algorithm converting
A inputs -> equivalent B inputs

If B in P -> A in P
If B in NP -> A in NP

## Proving X is NP-Complete
1. Prove X in NP (nondeterministic algorithm, certificate & verifier) 
2. Prove X in NP-Hard by reducing from known NP-complete problem Y to X
    * Z in NP -> Y -> X
