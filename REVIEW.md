# Verification summary

This note summarizes the mathematical and computational checks verifying the results in [paper/paper.tex](paper/paper.tex).

## Edge-conditioning reduction and single-cycle family

- **Conditional transition probability:** Sampling a uniform edge $e$, a uniform matching $M \in \Omega_e$, and a uniform $\mu_{n-1}$-neighbor $N \in \Omega_e$ yields $(M, N)$ with conditional probability $(n - s) / (n d_{n-1}) = 1 / d_n$, matching the uniform $\mu_n$-neighbor law.
- **Zero-mean restriction:** For any $f \perp \operatorname{span}\{g_e\}$, each restriction $f_e = f|_{\Omega_e}$ has mean zero on $\Omega_e \cong \Omega_{n-1}$, yielding the Rayleigh bound $\langle f, P_n f \rangle \le b_{n-1} \|f\|^2$.
- **Strict monotonicity and induction:** For $n > s \ge 2$, $\rho_n - \rho_{n-1} = s / [n(n-2)] > 0$, so any base $b_{s+2} = \rho_{s+2}$ propagates to all $n \ge s+2$ and strictly separates $V_{(2n-2,2)}$ from $W_n$ for all $n \ge s+3$.
- **Single-cycle starting cases:** For $s \ge 5$, Corollary 3.5 of [Gupta et al.](https://arxiv.org/html/2510.17135v2#S3) gives $b_{s+1}(s, 1) = \rho_{s+1}$, starting the induction at $n = s+2$; for $s \in \{2, 3, 4\}$, the two-singleton bases at $n = 4, 5, 6$ are certified directly.

## Finite-base and spectrum certificates

- **Core count:** There are exactly $230$ partitions $\nu \vdash s$ with all parts at least $2$ across $2 \le s \le 16$ (and $134$ across $2 \le s \le 14$).
- **Orbit-quotient enumeration ($n = 8$):** `matchings/orbit_quotients.cpp` enumerates all $15!! = 2{,}027{,}025$ matchings of $K_{16}$ and computes all $22$ exact $22 \times 22$ orbit quotient matrices; `matchings/exact_quotient.py` labels all $22$ joint eigenvectors independently by hook-length dimension and central transposition content sum, reproducing all $484$ eigenvalues and $22$ dimensions in the authors' pinned workbook.
- **Jack-polynomial / zonal verification ($4 \le n \le 18$):** `verification/zonal.py` computes exact integer zonal polynomials ($\alpha = 2$) in the power-sum basis, identifying the normalized coefficients with adjacency eigenvalues via Theorem 2.2.1 of [Lindzey, Chapter 2](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/9d33772f-c7dc-409f-a4ed-521da8d87890/content). All $72{,}035 = \sum_{n=4}^{15} p(n)^2$ compared workbook entries agree identically, and all $230$ two-singleton base gaps ($2 \le s \le 16$) are strictly positive; the smallest normalized base gap is $1/60$, attained for core $(2, 2)$ at $n = 6$ ($d_6 = 180$, target $48$, largest competitor $45$).
- **Extended conjecture search:** `verification/search_conjectures.py` checks all $3{,}477$ nonidentity relations for $5 \le n \le 21$ (Conjectures 1.3 and 6.1) and all $1{,}187$ diameter bounds for $5 \le n \le 17$ (Conjecture 6.2), with zero violations.

## Minimum-gap proof and Lean 4 checks

- **Minimum spectral gap ($n \ge 5$):** Every step of the cycle-reconnection triple $(M, L, N)$, strict inequality $D_\sigma(f) < 4 D_\mu(f)$ for nonconstant $f$, combinatorial degree lower bounds $d_\mu \ge 4n(n-1)$ for all nonidentity $\mu \neq \sigma$ except $(2, 2, 1)$ at $n = 5$, and the exact exception check $\Delta_{(2,2,1)} = 60 - 15 = 45 > 9$ have been verified analytically and cross-checked against exact spectra.
- **Lean 4.34.1:** Both `formalization/Propagation.lean` and `formalization/EnergyComparison.lean` type-check with zero errors, zero warnings, no `sorry`, and only the standard axioms (`propext`, `Classical.choice`, `Quot.sound`).
