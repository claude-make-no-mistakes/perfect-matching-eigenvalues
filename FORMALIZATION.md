# Formal verification status

Two standalone Lean 4 files (checked under Lean 4.34.1, as pinned in `lean-toolchain`) formalize the abstract arithmetic and induction steps underlying the main arguments:

- [formalization/Propagation.lean](formalization/Propagation.lean): models the second-eigenvalue sequence and target sequence as rational-valued functions `Nat → Rat` and proves that the Rayleigh sandwich inequality together with strict monotonicity of the target propagates equality from any base $b_{n_0} = \rho_{n_0}$ to all $n \ge n_0$ (`Matching.extend_all`).
- [formalization/EnergyComparison.lean](formalization/EnergyComparison.lean): proves the pointwise two-step square inequality $(x - z)^2 \le 2\bigl((x - y)^2 + (y - z)^2\bigr)$ (`Matching.two_step_square`) and the resulting factor-four energy comparison once both leg marginals agree (`Matching.energy_compare`).

## Running the Lean checks

From the repository root with Lean 4.34.1 on `PATH`:

```sh
lean formalization/Propagation.lean
lean formalization/EnergyComparison.lean
```

Both files type-check with zero errors, zero warnings, no `sorry`, and depend only on the standard Lean axioms (`propext`, `Classical.choice`, `Quot.sound`).

## Scope outside Lean

The graph-specific representation theory, edge-conditioning Rayleigh comparison, cycle-reconnection triple, strictness of the energy comparison, degree lower bounds, and passage to the spectral gap are proved in [paper/paper.tex](paper/paper.tex). The finite base spectra and workbook comparisons are verified in exact integer and rational arithmetic by `replay.py`.
