# Between Two Sets

**HackerRank:** https://www.hackerrank.com/challenges/between-two-sets/ ·
**Topic:** Implementation

## Problem
Count integers `x` such that every element of `a` divides `x` and `x`
divides every element of `b`.

## Approach
Such `x` are exactly the multiples of `lcm(a)` that divide `gcd(b)`.
Compute both with `math.gcd`, then count multiples of the LCM up to the GCD
that divide it.

## Complexity
- Time: **O(n log M + m log M + g/l)** — gcd/lcm work plus the multiple scan
- Space: **O(1)**

## Notes
- Brute-forcing 1..100 for each candidate pair would also pass the limits,
  but the lcm/gcd formulation is the intended insight.
