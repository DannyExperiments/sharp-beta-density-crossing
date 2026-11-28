import Std
namespace Crossing
/-- Strict monotonicity at each positive integral exponent. -/
theorem pow_strict (x y : Rat) (hx : 0 < x) (hxy : x < y) (n : Nat) : x^(n+1) < y^(n+1) := by
  induction n with
  | zero => simp [hxy]
  | succ n ih =>
    have hp : 0 < x^(n+1) := Rat.pow_pos hx
    have u := Rat.mul_pos hp (show 0 < y-x by grind)
    have v := Rat.mul_pos (show 0 < y by grind) (show 0 < y^(n+1)-x^(n+1) by grind)
    rw [Rat.pow_succ x (n+1), Rat.pow_succ y (n+1)]
    grind
/-- After removing the common positive factor x^b(1-x)^(t-a), the two
beta kernels are A*x^(a-b) and B*(1-x)^(a-b). They meet at most once. -/
theorem unique_cross (A B p q : Rat) (d : Nat) (hA : 0 < A) (hB : 0 < B)
    (hp : 0 < p ∧ p < 1) (hq : 0 < q ∧ q < 1)
    (cp : A*p^(d+1)=B*(1-p)^(d+1)) (cq : A*q^(d+1)=B*(1-q)^(d+1)) : p=q := by
  have order (x y : Rat) (hx : 0 < x) (hy : y < 1) (lt : x < y) :
      A*x^(d+1) < A*y^(d+1) ∧ B*(1-y)^(d+1) < B*(1-x)^(d+1) := by
    have h := pow_strict x y hx lt d
    have h' := pow_strict (1-y) (1-x) (by grind) (by grind) d
    have u := Rat.mul_pos hA (show 0 < y^(d+1) - x^(d+1) by grind)
    have v := Rat.mul_pos hB (show 0 < (1-x)^(d+1) - (1-y)^(d+1) by grind)
    grind
  by_cases l : p < q
  · have := order p q hp.1 hq.2 l; grind
  · by_cases r : q < p
    · have := order q p hq.1 hp.2 r; grind
    · grind
#print axioms unique_cross
end Crossing
