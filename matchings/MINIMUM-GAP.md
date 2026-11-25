# The smallest spectral gap in the perfect matching association scheme

**Theorem.** Let \(n\ge5\). Among nonidentity relations of the perfect matching association scheme on \(2n\) vertices, the minimum unnormalized adjacency spectral gap is \(2n-1\). Only the relation \(\sigma=(2,1^{n-2})\), which switches two edges of a matching, attains it. This proves Conjecture 6.1 of the arXiv version of Gupta, Herman, Lacaze-Masmonteil, Maleki and Meagher. [Source, §6](https://arxiv.org/html/2510.17135v2#S6)

Write \(\Omega\) for the perfect matchings. The relation type of two matchings is the partition formed by the half-lengths of their alternating cycles, with a shared edge contributing a part of size one. Write \(A_\mu,d_\mu\) for the adjacency matrix and degree of the relation graph, and define its gap \(\Delta_\mu\) by the smallest Rayleigh quotient of \(d_\mu I-A_\mu\) on the orthogonal complement of constants. This definition also gives zero if the graph is disconnected.

## Comparing each relation to a switch

Take a pair \(M,L\) of the given nonidentity type \(\mu\). Select two edges of \(M\) in a nontrivial alternating cycle of \(M\cup L\), and delete them. The cycle becomes two paths whose endpoints are the four endpoints of the deleted edges. There are exactly three pairings of those endpoints. Connecting the endpoints within each path makes two alternating cycles. Each of the other two pairings joins the paths into one alternating cycle of the original length. One is the original pairing. Use the other to obtain a matching \(N\). The types of \((M,L),(L,N),(M,N)\) are then \(\mu,\mu,\sigma\). This construction also works on a cycle of length four, where the two paths each consist of a single edge of \(L\).

Relabel this triple using a uniform permutation of the \(2n\) vertices. For any fixed type, the symmetric group acts transitively on ordered pairs of that type, by matching their alternating cycles and preserving the two edge colors. Hence the relabeling gives the uniform ordered pair law of type \(\mu\) on each leg and the uniform ordered pair law of type \(\sigma\) on the endpoints.

For \(f\colon\Omega\to\mathbb R\), let \(D_\tau(f)\) denote the mean of \((f(P)-f(Q))^2\) over uniform ordered pairs of type \(\tau\). The square inequality \((u+v)^2\le 2(u^2+v^2)\) on the relabeled triple yields

\[
D_\sigma(f)\le4D_\mu(f).
\]

Under the uniform inner product, \(\langle f,(d_\tau I-A_\tau)f\rangle=d_\tau D_\tau(f)/2\). The known switch degree and gap are \(d_\sigma=n(n-1)\) and \(\Delta_\sigma=2n-1\). Applying the Rayleigh inequality to every \(f\) perpendicular to constants now gives

\[
\Delta_\mu\ \ge\ \frac{d_\mu}{4n(n-1)}(2n-1).
\]

In particular, the gap is positive for every nonidentity type at these sizes. [Switch eigenvalue and gap, Gupta et al., §4](https://arxiv.org/html/2510.17135v2#S4)

The comparison is strict for any nonconstant \(f\). Equality in the averaged square inequality would force \(f(L)=(f(M)+f(N))/2\) on the entire orbit. The three vertex marginals are uniform. Therefore the mean square of \(f(L)\) equals that of \(f(M)\), while the mean square of \((f(M)+f(N))/2\) is the mean square of \(f(M)\) minus \(D_\sigma(f)/4\). This would force \(D_\sigma(f)=0\). The switch gap is positive, so \(D_\sigma(f)=0\) implies \(f\) is constant. Applying strictness to a nonzero minimizing eigenvector perpendicular to constants makes the gap bound strict.

## Degrees and the small exception

Delete the singleton parts of \(\mu\) to get a core \(\nu\) of weight \(s\). Then \(d_\mu=\binom{n}{s}d_\nu\), since there are \(\binom{n}{s}\) ways to choose the reference edges in the nontrivial components. For a component of half-length \(a\) on prescribed reference edges the degree is \(2^{a-1}(a-1)!\), by the valency formula for a single cycle. Fix one of the \(s\) reference edges. Choosing an \(a\)-component containing it gives at least \(\binom{s-1}{a-1}2^{a-1}(a-1)!\) arrangements, multiplied by the degree of the remaining core. The chosen component is uniquely identifiable from the resulting matching as the component containing the fixed edge. Count an empty remaining core with degree one. [Valency formula, Gupta et al., Lemma 2.1](https://arxiv.org/html/2510.17135v2#S2.SS1)

Suppose \(s\ge5\), and take \(a\) to be the largest part of the core.

- If \(a\ge4\), the count is at least \(8(s-1)(s-2)(s-3)\). Since \(2(s-2)(s-3)\ge s\) for \(s\ge5\), this is at least \(4s(s-1)\).
- If \(a=3\), the residual core has at least one nontrivial component, so its degree is at least two. The count is at least \(8(s-1)(s-2)\), which is at least \(4s(s-1)\).
- If \(a=2\), all parts are two. For even \(s\ge6\), the degrees \(d_s\) satisfy \(d_s=2(s-1)d_{s-2}\), by choosing the partner of the fixed reference edge and one of the two possible switches. The base is \(d_6=2\cdot5\cdot12=120=4\cdot6\cdot5\). The recurrence preserves the bound \(d_s\ge4s(s-1)\), since \(2(s-2)(s-3)\ge s\).

Thus \(d_\mu\ge4n(n-1)\) for \(s\ge5\), as \(\binom ns s(s-1)=n(n-1)\binom{n-2}{s-2}\). For \(s=3\) the degree is \(8\binom{n}{3}\), which meets the same bound at \(n\ge5\). For \(s=4\) the two possible core degrees are \(48\) and \(12\), for \((4)\) and \((2,2)\) respectively. Both meet the bound at \(n\ge6\), and at \(n=5\) only \(\mu=(2,2,1)\) falls below it. The published \(n=5\) eigenmatrix gives that relation valency 60 and largest nonconstant eigenvalue 15, for a gap of \(45>9\). The core of weight two is precisely the switch relation. These cases establish the minimum. [Exact \(n=5\) table](https://arxiv.org/html/2510.17135v2#A1)

## Scope

The argument applies to the unnormalized adjacency gap in Conjecture 6.1. The normalized gaps satisfy the factor-four comparison above. The proof uses a two-step walk for every switch, which by itself yields only the diameter bound \(2(n-1)\). Conjecture 6.2 asks for \(n-1\). The separate finite calculation checks that sharper bound over its stated range.

The lower limit \(n\ge5\) is sharp. At \(n=4\), the \((2,2)\) relation has gap \(12-7=5\), while the switch relation has gap \(12-5=7\). These values follow from the published \(n=4\) table. [Source, Table 5](https://arxiv.org/html/2510.17135v2#A1)
