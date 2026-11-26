# Edge-Conditioning and Minimum Spectral Gaps for Perfect-Matching Eigenvalues

This repository contains proofs, exact computational certificates, and Lean 4 checks for two structural results on the perfect matching association scheme on $2n$ vertices:

1. **Fixed-core edge-conditioning reduction (Conjecture 1.3 of Gupta et al.):** Conditioning on a shared edge reduces the signed second-eigenvalue inequality for each fixed core $\nu \vdash s$ (with all parts at least $2$) to the single two-singleton base $n = s+2$. Whenever the base holds, the target eigenspace $V_{(2n-2,2)}$ strictly dominates all competing nontrivial representations for every $n \ge s+3$. Exact Jack-polynomial (zonal) certificates settle all $230$ cores of weight $2 \le s \le 16$ at every $n \ge s+2$, independent orbit-quotient enumeration verifies all four weight-$6$ cores at $n = 8$, and the published one-singleton hook theorem settles the single-cycle family $(s, 1^{n-s})$ for arbitrary $s \ge 2$ and $n \ge s+2$.
2. **Minimum unnormalized spectral gap (Conjecture 6.1 of Gupta et al.):** For every $n \ge 5$, among all nonidentity relations of the perfect matching association scheme on $2n$ vertices, the minimum unnormalized adjacency spectral gap is $2n - 1$, attained uniquely by the two-edge switch relation $\sigma = (2, 1^{n-2})$. The proof averages a strict two-step walk comparison against $\sigma$. The threshold $n \ge 5$ is sharp.

## Documents and certificates

- **Paper:** [paper/paper.pdf](paper/paper.pdf) ([LaTeX source](paper/paper.tex))
- **Proof notes:** [Edge-conditioning reduction](matchings/REPORT.md) · [Minimum spectral gap](matchings/MINIMUM-GAP.md)
- **Verification & literature:** [Verification summary](REVIEW.md) · [Formal verification status](FORMALIZATION.md) · [Related work](PRIOR-WORK.md) · [Zonal specification](verification/ZONAL-SPEC.md)
- **Archived certificates:** [Orbit quotient certificate ($n=8$)](matchings/certificate_n8.json) · [230 base certificates ($2 \le s \le 16$)](verification/two-singleton-bases.json) · [Conjecture search output ($5 \le n \le 21$)](verification/conjecture-search-through-21.jsonl)

## Reproducing the certificates

Requirements: Python 3.12+, SymPy 1.14.0 (`requirements.txt`), and a GNU C++17 compiler (`g++`).

```sh
python3 -m pip install -r requirements.txt
python3 -B replay.py
```

`replay.py` verifies the SHA-256 digests of the frozen baseline scripts and $n = 3, 4$ controls, compiles and executes `matchings/orbit_quotients.cpp` to verify all $484$ labeled eigenvalues and $22$ dimensions at $n = 8$, checks all $134$ one-singleton sufficient-condition bounds ($2 \le s \le 14$), and regenerates all $230$ two-singleton bases ($2 \le s \le 16$) via `verification/zonal.py` while matching all $72{,}035$ eigenvalues in the authors' pinned workbook ($4 \le n \le 15$). Pass `--workbook PATH` to use a local copy of the hash-pinned workbook, or `--cxx PATH` to select the C++17 compiler.

### Extended conjecture search

`verification/search_conjectures.py` checks Conjecture 1.3 and Conjecture 6.1 through $n = 21$ ($3{,}477$ nonidentity relation graphs) and Conjecture 6.2 (diameter at most $n - 1$) through $n = 17$ ($1{,}187$ relation graphs) via the exact weighted trace pairing for $(I + A_\mu)^{n-1}$:

```sh
python3 -B verification/search_conjectures.py --through 21 --diameters-through 17
```

No counterexample was found in these ranges; the exact output is archived in [verification/conjecture-search-through-21.jsonl](verification/conjecture-search-through-21.jsonl).

### Lean 4 verification

Using Lean 4.34.1 (specified in `lean-toolchain`), check the abstract arithmetic and induction lemmas from the repository root:

```sh
lean formalization/Propagation.lean
lean formalization/EnergyComparison.lean
```

See [FORMALIZATION.md](FORMALIZATION.md) for the exact scope of the Lean formalization. The general signed second-eigenvalue conjecture for arbitrary cores remains open.
