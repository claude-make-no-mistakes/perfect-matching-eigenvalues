# An edge-star reduction for the perfect matching spectral-gap conjecture

For a fixed nonempty partition \(\nu\vdash s\) with parts at least two, the signed second-eigenvalue conjecture for \((\nu,1^{n-s})\) at all \(n\ge s+2\) is equivalent to its single instance at \(n=s+2\). When the target attains the signed maximum at the base, at each later size it is strictly above every competing eigenvalue on a different nontrivial representation. Exact orbit quotients settle the four bases of size \(s=6\) at \(n=8\), which proves the conjecture for all four families at every \(n\ge8\).

## Definitions and the signed target

Write \(\Omega_n\) for the perfect matchings of a complete graph on \(2n\) vertices. The relation type of \((M,N)\) records the half-lengths of the alternating cycles of the two matchings, counting a shared edge as a doubled cycle of half-length one. Fix \(\nu\) as above and put \(\mu_n=(\nu,1^{n-s})\) for \(n\ge s\). Let \(A_n\) be its adjacency operator, \(d_n\) its valency, and \(P_n=A_n/d_n\). Write \(b_n\) for the largest eigenvalue of \(P_n\) on the orthogonal complement of constants. This is the second eigenvalue in decreasing signed order with multiplicities. All inner products on matching spaces below use uniform measure.

The matching permutation module is the multiplicity-free sum of the Specht modules \(V_{2\lambda}\), for \(\lambda\vdash n\). In the authors' notation the target row is \(\lambda=(n-1,1)\), and the subscript of \(A\) is the relation, not the module. Their formal Conjecture 1.3 also covers the one-singleton hook \((n-1,1)\) except at \(n=4\). Their Corollary 3.5 handles those hooks for \(n\ge6\), and Appendix A handles \(n=3,5\). [Gupta et al., Conjecture 1.3, Section 2 and Corollary 3.5](https://arxiv.org/html/2510.17135v2).

For an edge \(e\) of the complete graph let \(g_e(M)=\mathbf1_{e\in M}\) and let \(U_n=\operatorname{span}\{g_e\}\). The incidence map from the permutation module on two-element sets to the matching module is equivariant. By Young's rule the domain has constituents \(V_{(2n)},V_{(2n-1,1)},V_{(2n-2,2)}\) for \(n\ge2\). The target permutation module contains no \(V_{(2n-1,1)}\) because its constituents have even row lengths. Constants lie in the image since \(\sum_e g_e=n\), and \(g_e\) is nonconstant for \(n\ge2\). Consequently

\[
U_n=\mathbf R\mathbf1\oplus V_{(2n-2,2)}.
\]

Conditional on \(M\), a uniform \(\mu_n\)-neighbor \(N\) shares exactly \(n-s\) of the \(n\) edges of \(M\). Its marginal probability of containing \(e\in M\) is \(a=(n-s)/n\) by symmetry. The stabilizer of \(M\) is also transitive on the \(\binom{2n}{2}-n=2n(n-1)\) edges outside \(M\), so the marginal there is \(c=s/[2n(n-1)]\). Thus \(P_ng_e=c+(a-c)g_e\), and subtracting the mean \(1/(2n-1)\) gives the normalized target eigenvalue

\[
\rho_n=a-c=1-\frac{s}{2}\left(\frac1n+\frac1{n-1}\right).
\]

The valency is the number of ways to select the \(s\) matching edges to change times the valency on those \(2s\) vertices. In symbols, \(d_n=\binom ns d_s\) and \(d_s=2^{s-\ell(\nu)}s!/\prod_i i^{m_i}m_i!\), where \(m_i\) is the multiplicity of \(i\) in \(\nu\). The target spectral gap is \(d_n(1-\rho_n)\) wherever the conjecture holds. [Gupta et al., Lemmas 2.1–2.2](https://arxiv.org/html/2510.17135v2#S2.SS1).

## Restriction to a shared edge

Suppose \(n>s\). For any edge \(e\), let \(\Omega_e=\{M:e\in M\}\) and let \(f_e=f|_{\Omega_e}\). Removing the endpoints of \(e\) identifies \(\Omega_e\) with \(\Omega_{n-1}\). The induced relation is \(\mu_{n-1}\), and its normalized adjacency is \(P_{n-1}\) after this identification.

Consider the following sampling rule. Choose \(e\) uniformly among all edges of the complete graph, then choose \(M\) uniformly in \(\Omega_e\), then choose \(N\) uniformly among its induced neighbors in \(\Omega_e\). Every matching contains exactly \(n\) edges and all stars have the same size, so \(M\) is uniform and \(e\) given \(M\) is uniform among its \(n\) edges. For a fixed \(\mu_n\)-neighbor \(N\), there are exactly \(n-s\) eligible choices of \(e\in M\cap N\). The conditional probability of that \(N\) given \(M\) is \((n-s)/(nd_{n-1})=1/d_n\). This proves the exact identities

\[
\langle f,P_nf\rangle=\mathbb E_e\langle f_e,P_{n-1}f_e\rangle_{\Omega_e},
\qquad
\|f\|^2=\mathbb E_e\|f_e\|^2_{\Omega_e}.
\]

Take \(f\in W_n=U_n^\perp\). For every edge \(e\), orthogonality to \(g_e\) says that \(f_e\) has mean zero. The local signed Rayleigh bound yields

\[
\langle f,P_nf\rangle\le b_{n-1}\|f\|^2.
\]

Both \(U_n\) and \(W_n\) are invariant. The target row gives \(b_n\ge\rho_n\) and the Rayleigh inequality gives \(b_n\le\max(\rho_n,b_{n-1})\). For every \(n>s\) in range, \(\rho_n-\rho_{n-1}=s/[n(n-2)]>0\). If \(b_{n-1}\le\rho_n\), the conjectured row attains \(b_n\). If \(b_{n-1}<\rho_n\), the top nonconstant eigenspace is exactly \(V_{(2n-2,2)}\). In particular, starting from \(b_{s+2}=\rho_{s+2}\), even with a tie at the base, proves the result and removes any tie across modules at every later size. The converse is immediate by taking \(n=s+2\). Since \(\rho_n<1\) for a nonempty core, any size certified this way also has a connected relation graph.

This argument requires at least one shared edge for a restriction step. The identity relation has \(s=0\) and every eigenvalue is 1. For \(n=1\) the space has dimension one and the second-eigenvalue target has no meaning. The one-singleton relation \((3,1)\) at \(n=4\) has target 4 and actual second eigenvalue 8 on \(V_{(2,2,2,2)}\). Even outside hooks, the example \((2,2,1)\) at \(n=5\) has target 6 and second eigenvalue 15. A signed inequality can hold when the absolute-value version fails. At \((n,\mu)=(4,(2,1,1))\) the target is 5, and one competing eigenvalue is \(-6\). [Gupta et al., Appendix A, Tables 5–6](https://arxiv.org/html/2510.17135v2#A1).

### A corollary with unbounded core size

For every pair of integers \(s\ge2\) and \(n\ge s+2\), the relation \((s,1^{n-s})\) has its largest nonconstant eigenvalue on \(V_{(2n-2,2)}\). For \(s\ge5\), start from the published Corollary 3.5 at size \(s+1\ge6\). It gives \(b_{s+1}=\rho_{s+1}\) for the one-singleton relation \((s,1)\). Since \(\rho_{s+1}<\rho_{s+2}\), the preceding argument applies at every size from \(s+2\) onward. For \(s=2,3,4\), use the exact two-singleton bases at \(n=4,5,6\) in the [computed table](../verification/two-singleton-bases.json). Both the size of the changed alternating cycle and the number of shared edges can therefore vary without bound. [Gupta et al., Corollary 3.5](https://arxiv.org/html/2510.17135v2#S3).

## Exact bases for the weight-six families

Use the adjacent-pair matching \(M_0\) and let \(H_n\) be its stabilizer. Its orbits on \(\Omega_n\) are indexed by the relation type with \(M_0\). To see transitivity for a given type, match up alternating cycles of the same length, then relabel corresponding vertices around each cycle, preserving the \(M_0\)-edges. For each relation \(\mu\), orbit row \(\sigma\), and orbit column \(\tau\), the quotient entry is the number of \(N\) with pair types \(\operatorname{type}(M_\sigma,N)=\mu\) and \(\operatorname{type}(M_0,N)=\tau\), where \(M_\sigma\) is any representative. These quotients act on the \(H_n\)-fixed subspace. Every matching-module constituent has a one-dimensional fixed subspace by Frobenius reciprocity and the multiplicity-free decomposition. Thus the quotient sees every constituent once, including constituents that tie for a particular relation. [Srinivasan, The perfect matching association scheme](https://doi.org/10.5802/alco.104).

The native enumerator accumulated all the counts from 2,027,025 matchings at \(n=8\). It enumerates each matching by pairing the least remaining vertex with each available partner in turn. A walk around the alternating cycles gives the relation types. It stores the 22 quotients of size \(22\times22\) in integer counters. The Python implementation computes the same quotients separately for \(n=3,4\) and verifies the complete published spectra at those sizes. The checks at all three sizes include the diagonal relation, row sums, detailed balance with orbit sizes, commutativity, and exact joint eigenvectors over the rationals.

The joint eigenvectors were labeled independently of the workbook. If \(u\) is the spherical vector scaled so that \(u(M_0)=1\), its uniform squared norm is \(1/\dim V_{2\lambda}\). Indeed, if \(Q\) is the orthogonal projector onto the constituent, then \(Q\delta_{M_0}\) is fixed by \(H_n\), its squared counting norm is \(Q_{M_0,M_0}\), and transitivity gives \(Q_{M_0,M_0}=\dim V_{2\lambda}/|\Omega_n|\). The central transposition sum contributes \(n\) copies of the original matching and reaches each switch-neighbor twice, so its action is \(nI+2A_{(2,1^{n-2})}\). Its scalar on \(V_{2\lambda}\) is the sum of the Young diagram contents. The pair of hook-length dimension and content sum separates the labels at these sizes. [Gupta et al., Table 1 and Proposition 4.1](https://arxiv.org/html/2510.17135v2#S4).

| Base relation | Valency | Target on \(V_{(14,2)}\) | Largest other nonconstant eigenvalue |
|---|---:|---:|---:|
| \((6,1,1)\) | 107520 | 21120 | 960 |
| \((4,2,1,1)\) | 40320 | 7920 | 2520 |
| \((3,3,1,1)\) | 17920 | 3520 | 1504 |
| \((2,2,2,1,1)\) | 3360 | 660 | 396 |

The normalized target is \(11/56\) in each case. The full exact matrix and both shape orders are in [certificate_n8.json](certificate_n8.json). All 484 adjacency eigenvalues and all 22 dimensions agree with the pinned authors' workbook. The worksheet rows use doubled Specht labels and the columns use doubled relation partitions. Worksheet row 27 finds the first signed maximum after excluding the trivial row, so ties select the first matching row. The workbook's per-column test row applies to relations with at least two doubled parts equal to 2. The Sage function `main_conjecture` uses the same signed maximum and scope and excludes the identity column. These automated checks do not include the formal conjecture's one-singleton hooks. The exact comparison above reads the integer values in the spectrum table and independently determines all maximizers. [Authors' workbook](https://github.com/Himanshugupta23/Perfect-Matching-Association-Scheme/blob/9bfd0192a04b1c271b305ee3c8146b356ac41603/Excel_format_Evals_of_PM_Schm_upto_n%3D15.xlsx), [authors' Sage code](https://github.com/Himanshugupta23/Perfect-Matching-Association-Scheme/blob/9bfd0192a04b1c271b305ee3c8146b356ac41603/Evals_of_PM_scheme_via_Srinivasan_algorithm.sage.py#L245-L274).

A separate exact calculation using Jack polynomials certifies all 230 bases for \(2\le s\le16\) and checks 72,035 workbook entries. The same propagation argument therefore settles every one of those core families at all admissible sizes. [Jack calculation](../verification/ZONAL-SPEC.md), [base certificate](../verification/two-singleton-bases.json).

## A lower-order sufficient condition

The same Rayleigh identity applies at \(n=s+2\) before any conjecture is known for one-singleton relations. It suffices to show, for each core, that

\[
b_{s+1}(\nu,1)\le\rho_{s+2}=\frac{3s+4}{2(s+1)(s+2)}.
\]

This requires only the largest signed nonconstant eigenvalue, regardless of its label. Exact rational checks of the pinned workbook satisfy the strict inequality for all 134 cores with \(2\le s\le14\). Iterating once gives another sufficient condition, \(b_s(\nu)\le\rho_{s+2}\), because \(\rho_{s+1}<\rho_{s+2}\). That stronger condition fails for \((2,2)\), \((2,2,2)\), \((3,3)\), and \((2,2,2,2)\) in this range. For example \(b_4(2,2)=7/12>4/15=\rho_6\). The failures concern the sufficient bound. The corresponding two-singleton bases still hold. The universal one-singleton bound and arbitrary two-singleton bases remain open here.

For a shape-specific version, let \(f\) lie in \(V_{2\lambda}\). Under restriction to the subgroup fixing the endpoints of \(e\) pointwise, the only even constituents have shapes \(2\kappa\) obtained by removing a corner of \(\lambda\) and doubling row lengths. This follows by applying the symmetric-group branching rule twice, since reaching another even shape requires both removals from the same row. The restriction map \(f\mapsto f_e\) is equivariant for that subgroup, so the projections of \(f_e\) lie only in these constituents of the smaller matching module. The projected squared norms, averaged over \(e\) and divided by \(\|f\|^2\), are nonnegative and sum to 1. The exact Rayleigh identity writes the eigenvalue at \(\lambda\) as their convex combination of the corresponding predecessor eigenvalues. This restricts which lower-order rows can contribute to a particular competitor. The argument still requires a bound on the relevant lower-order spectra.

## Reproduction

The scripts were checked with Python 3.12.14, SymPy 1.14.0 and GNU C++17. With the compiler and its runtime on `PATH`, run from this directory.

```powershell
python -B check_baseline.py
python -B check_n8.py --output certificate_n8.replay.json
python -B check_stretch.py
```

Use `--cxx C:/msys64/ucrt64/bin/g++.exe` to select that compiler when needed, and add `C:/msys64/ucrt64/bin` to `PATH` for its runtime. Both workbook checks accept `--workbook PATH` for a local copy and verify the same SHA-256 as the default pinned download. The pre-computation baseline files and checksums are in [baseline/SHA256SUMS](baseline/SHA256SUMS). The stretch calculation uses the authors' tabulated integer spectra. The independent native quotient calculation is confined to \(n\le8\).
