# An Edge-Conditioning Reduction for Perfect-Matching Eigenvalues

Conditioning on a shared edge reduces the signed second-eigenvalue inequality for each fixed core to the case of exactly two shared edges. We prove the reduction and verify the bases for 230 cores of weight at most sixteen. A separate argument settles the single-cycle family for arbitrary cycle size.

[Paper PDF](paper/paper.pdf) · [LaTeX source](paper/paper.tex) · [Proof notes](matchings/REPORT.md) · [Orbit quotient certificate](matchings/certificate_n8.json) · [230 base certificates](verification/two-singleton-bases.json)

## Replay the certificates

Use Python 3.12, SymPy 1.14.0 and a GNU C++17 compiler.

```sh
python -m pip install -r requirements.txt
python -B replay.py
```

The replay downloads the authors' pinned workbook and checks its SHA-256. Use --workbook PATH for an offline copy or --cxx PATH to select the compiler.

The general conjecture remains open in this work. See [formal verification status](FORMALIZATION.md).

[Verification record](REVIEW.md) · [Draft post for X](POST.md)
