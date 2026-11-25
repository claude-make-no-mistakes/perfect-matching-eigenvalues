# An Edge-Conditioning Reduction for Perfect-Matching Eigenvalues

Conditioning on a shared edge reduces the signed second-eigenvalue inequality for each fixed core to the case of exactly two shared edges. We prove the reduction and verify the bases for 230 cores of weight at most sixteen. A separate argument settles the single-cycle family for arbitrary cycle size.

[Paper PDF](paper/paper.pdf) · [LaTeX source](paper/paper.tex) · [Proof notes](matchings/REPORT.md) · [Orbit quotient certificate](matchings/certificate_n8.json) · [230 base certificates](verification/two-singleton-bases.json)

## The minimum-gap conjecture

The relation that switches two edges uniquely minimizes the unnormalized spectral gap for \(n\ge5\). Its gap is \(2n-1\). This proves Conjecture 6.1 of Gupta et al.'s arXiv v2. The proof compares each relation to the switch graph by averaging a two-step walk. [Proof](matchings/MINIMUM-GAP.md)

## Replay the certificates

Use Python 3.12, SymPy 1.14.0 and a GNU C++17 compiler.

```sh
python -m pip install -r requirements.txt
python -B replay.py
```

The replay downloads the authors' pinned workbook and checks its SHA-256. Use --workbook PATH for an offline copy or --cxx PATH to select the compiler.

The general conjecture remains open in this work. See [formal verification status](FORMALIZATION.md).

[Verification record](REVIEW.md) · [Draft post for X](POST.md)

The [counterexample search](verification/search_conjectures.py) checks the signed eigenvalue conjecture through \(n=21\) and the diameter conjecture through \(n=17\). [Exact output](verification/conjecture-search-through-21.jsonl) · [Prior-work check](PRIOR-WORK.md)

~~~sh
python -B verification/search_conjectures.py --through 21 --diameters-through 17
~~~

The search computes the integer eigenmatrix and checks the valencies and weighted trace identities. It compares the signed eigenvalue ordering and smallest gap across the indicated sizes. For the diameter test, it recovers coefficients of \((I+A_\mu)^{n-1}\) in the orbital basis using the weighted trace pairing. Every nonzero coefficient represents walks to every pair in its orbital. The run covered 3,477 nonidentity relation graphs, including 1,187 diameter bounds, and found no violation of the published conjectures in those ranges.
