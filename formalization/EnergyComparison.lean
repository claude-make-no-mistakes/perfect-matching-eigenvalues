import Init

namespace Matching

def square (q : Rat) : Rat := q * q

theorem square_nonneg (q : Rat) : 0 ≤ square q := by
  unfold square
  rcases (Rat.le_total (a := 0) (b := q)) with positive | negative
  · exact Rat.mul_nonneg positive positive
  · have nonnegative : 0 ≤ -q := by grind
    have bound := Rat.mul_nonneg nonnegative nonnegative
    have identity : (-q) * (-q) = q * q := by grind
    simpa only [identity] using bound

theorem two_step_square (left middle right : Rat) :
    square (left - right) ≤ 2 * (square (left - middle) + square (middle - right)) := by
  have h := square_nonneg (left - 2 * middle + right)
  have decomposition :
      square (left - right) + square (left - 2 * middle + right) =
      2 * (square (left - middle) + square (middle - right)) := by
    unfold square
    grind
  rw [← decomposition]
  have ordered := (Rat.add_le_add_left (c := square (left - right))).mpr h
  simpa only [Rat.add_zero] using ordered

theorem energy_compare (endpoint firstLeg secondLeg reference : Rat)
    (triangle : endpoint ≤ 2 * (firstLeg + secondLeg))
    (firstMarginal : firstLeg = reference) (secondMarginal : secondLeg = reference) :
    endpoint ≤ 4 * reference := by
  rw [firstMarginal, secondMarginal] at triangle
  have identity : 2 * (reference + reference) = 4 * reference := by grind
  simpa only [identity] using triangle

end Matching

#print axioms Matching.two_step_square
#print axioms Matching.energy_compare
