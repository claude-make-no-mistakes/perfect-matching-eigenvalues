# Formal verification status

Lean 4.34.1 checks [the fixed-core propagation step](formalization/Propagation.lean). It models the two eigenvalue sequences as rational-valued functions and takes the spectral inequalities as hypotheses. Given the Rayleigh comparison and the increase of the target eigenvalue, a successful base implies the same eigenvalue at every larger size.

Run this command from the repository root with the toolchain specified in the toolchain file.

~~~sh
lean formalization/Propagation.lean
lean formalization/EnergyComparison.lean
~~~

The paper proves the graph-specific Rayleigh comparison and identifies the target representation. The exact Python and C++ replay checks the finite bases. Those steps remain outside Lean.

The second file checks the square inequality behind the two-step Dirichlet comparison and the factor-four bound once both leg marginals agree. The cycle reconnection argument, identification of the graph marginals, degree counts, and passage to the spectral gap remain in the written proof.
