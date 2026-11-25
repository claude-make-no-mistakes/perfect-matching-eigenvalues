import Init

namespace Matching

/-! Arithmetic and induction used after the Rayleigh comparison is established. -/

theorem extend_one (previous current target : Rat)
    (rising : previous < target)
    (lower : target ≤ current)
    (upper : current ≤ max target previous) :
    current = target := by
  have max_eq : max target previous = target := by
    rw [Rat.max_def, if_neg (Rat.not_le.mpr rising)]
  rw [max_eq] at upper
  exact Rat.le_antisymm upper lower

theorem extend_all (base : Nat) (eigenvalue target : Nat → Rat)
    (base_eq : eigenvalue base = target base)
    (rising : ∀ n, base ≤ n → target n < target (n + 1))
    (lower : ∀ n, base ≤ n → target n ≤ eigenvalue n)
    (upper : ∀ n, base ≤ n →
      eigenvalue (n + 1) ≤ max (target (n + 1)) (eigenvalue n)) :
    ∀ n, base ≤ n → eigenvalue n = target n := by
  have aux : ∀ offset : Nat, eigenvalue (base + offset) = target (base + offset) := by
    intro offset
    induction offset with
    | zero => exact base_eq
    | succ k ih =>
      have bound : base ≤ base + k := by omega
      have above : base ≤ (base + k) + 1 := by omega
      have step := extend_one (eigenvalue (base + k))
        (eigenvalue ((base + k) + 1)) (target ((base + k) + 1))
        (by rw [ih]; exact rising _ bound)
        (lower _ above) (upper _ bound)
      simpa [Nat.add_assoc] using step
  intro n bound
  have address : base + (n - base) = n := by omega
  simpa only [address] using aux (n - base)

end Matching

#print axioms Matching.extend_all
