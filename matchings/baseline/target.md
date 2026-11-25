# Frozen matching-scheme target

Source: Gupta, Herman, Lacaze-Masmonteil, Maleki, Meagher, Conjecture 1.3, Lemmas 2.1–2.2, Appendix A Tables 4–5, [arXiv:2510.17135v2](https://arxiv.org/html/2510.17135v2).

For every nonempty partition `nu` of `s >= 2` whose parts are all at least 2, and every `n >= s+2`, the largest eigenvalue of `A_mu` on the subspace perpendicular to constants equals its eigenvalue on `V[2n-2,2]`, where `mu=(nu,1^(n-s))`. This compares signed eigenvalues and allows equality across modules. Normalizing by the positive valency gives `rho = 1 - (s/2)*(1/n+1/(n-1))`. The paper separately includes the one-singleton hook case `mu=(n-1,1)`, except `n=4`. For the identity relation `mu=(1^n)`, every eigenspace has eigenvalue 1 and the signed statement is tautological for `n>=2`.

The propagation target is the inequality on functions perpendicular to every edge indicator, and the implication from the exact base at `n=s+2` to every larger `n`. The finite extension requires all 22 quotient eigenvalues for each of `[6,1,1]`, `[4,2,1,1]`, `[3,3,1,1]`, and `[2,2,2,1,1]` at `n=8`, computed independently of the authors' workbook.

The checker must certify exact joint quotient eigenvalues, compare every entry with the published small matrices, accept a known positive case, reject a known false case, and keep signed and absolute order distinct. The frozen positive control is `(n,mu)=(4,(2,1,1))`: degree 12, target 5, greatest competing signed eigenvalue 2 and greatest competing absolute eigenvalue 6. The frozen negative control is `(4,(3,1))`: degree 32, target 4, competing signed eigenvalue 8 on `V[2,2,2,2]`.
