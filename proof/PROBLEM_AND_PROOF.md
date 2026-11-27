# Problem and proof outline

Keep the two compared counts a>b≥0 fixed, and add f other observations to the total t. At the interior crossing of their two beta densities, compare the common height to the binary density at 1/2. [Published question](https://proceedings.mlr.press/v151/anand-jain22a/anand-jain22a.pdf#page=19)

## Moving trial point

Use x=t+1 and m=(a+b+1)/2 and evaluate both densities at p=m/x. Interpolate the total by a real parameter using a finite falling-factorial product. Bound the sum in the logarithmic derivative by the right-endpoint sum estimate. The resulting nonnegative bound integrates to log[x²/(4m(x−m))]. Both densities start at the same binary baseline when x=2m.

## The crossing and stopping

The geometric-mean formula for the crossing odds puts the crossing between the two density modes. The smaller density increases toward the crossing from the left and decreases from it to the right. Its maximum therefore dominates the smaller density at the common trial point. At f=0 the crossing is 1/2 and the comparison is exact. At positive f the integrated factor is strictly greater than one.

Under the original 1vr rule, disjoint confidence interval interiors imply crossing height at most δ/K. The binary baseline is at most that height, and hence strictly below the original 1v1 threshold δ/(K−1). Each possible leader-versus-competitor pair passes when the 1vr rule stops.

[Complete argument](../paper/manuscript.pdf)
