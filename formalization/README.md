# Uniqueness of a rational crossing

For positive rational A and B and every positive integer exponent d, the reduced beta kernels A·pᵈ and B·(1−p)ᵈ have at most one crossing in rational 0<p<1. The proof uses strict power monotonicity on both sides.

The reduced kernels arise by canceling their common positive factor. The rational certificate does not assert existence of a rational crossing. The real crossing, moving-trial interpolation and sharp height lower bound remain in the manuscript.

[Lean source](Q950Crossing.lean) · [Mathematical source](../paper/manuscript.tex) · [Expected axiom report](expected-axioms.txt)

Replay from this directory with Lean 4.30.0 and its standard library.

```sh
lean -DwarningAsError=true Q950Crossing.lean > axioms.actual
diff -u expected-axioms.txt axioms.actual
```
