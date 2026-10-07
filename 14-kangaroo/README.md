# Number Line Jumps (Kangaroo)

**HackerRank:** https://www.hackerrank.com/challenges/kangaroo/ ·
**Topic:** Implementation

## Problem
Kangaroos start at `x1 < x2` jumping `v1`, `v2` per step. Return "YES" if
they ever land together, else "NO".

## Approach
Math, not simulation: if `v1 <= v2` the one behind never catches up → "NO".
Otherwise they meet iff `(x2 - x1)` is divisible by `(v1 - v2)`.

## Complexity
- Time: **O(1)**
- Space: **O(1)**

## Notes
- Simulating jump-by-jump would be O(answer) — unbounded; the divisibility
  test is constant time.
