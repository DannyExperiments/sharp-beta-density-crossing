"""Exact arithmetic checks for the trial bound and worked rational crossings."""

from fractions import Fraction as F
from math import comb, factorial


def density(t, k, point):
    return (t + 1) * comb(t, k) * point**k * (1 - point)**(t - k)


def grid():
    count = 0
    for a in range(1, 34):
        for b in range(a):
            c = a + b
            baseline = density(c, a, F(1, 2))
            assert baseline == density(c, b, F(1, 2))
            for f in (*range(20), 37, 99, 201):
                t = c + f
                x = t + 1
                p = F(c + 1, 2 * x)
                factor = F(x * x, (c + 1) * (2 * x - c - 1))
                for k in (a, b):
                    assert density(t, k, p) >= baseline * factor
                    assert (density(t, k, p) == baseline) == (f == 0)
                g = F(factorial(a) * factorial(t - a), factorial(b) * factorial(t - b))
                assert F(b + 1, t - b)**(a - b) <= g <= F(a, t - a + 1)**(a - b)
                count += 1
    return count


def rational_crossings():
    fixtures = [(2, 2, 0, F(1, 2)), (9, 2, 0, F(1, 7)), (50, 2, 0, F(1, 36))]
    fixtures.extend((t, a, a - 1, F(a, t + 1)) for a in range(1, 12) for t in range(2 * a - 1, 30))
    for t, a, b, theta in fixtures:
        c = a + b
        h = density(t, a, theta)
        assert h == density(t, b, theta)
        assert h >= density(c, a, F(1, 2))
        assert (h == density(c, a, F(1, 2))) == (t == c)
        for j in range(51):
            p = F(j, 50)
            assert min(density(t, a, p), density(t, b, p)) <= h
    assert density(2, 2, F(1, 2)) == F(3, 4)
    assert density(9, 0, F(1, 7)) == 10 * F(6, 7)**9
    return len(fixtures)


if __name__ == "__main__":
    print(grid(), "exact trial controls, crossing-odds brackets, and equality checks.")
    print(rational_crossings(), "exact rational crossings, each checked at 51 grid points.")
    print("Worked fixture: H0=3/4; for a=2, b=0, f=7, theta=1/7 and H=10*(6/7)^9.")
