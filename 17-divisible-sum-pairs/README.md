# Divisible Sum Pairs

**HackerRank:** https://www.hackerrank.com/challenges/divisible-sum-pairs/ ·
**Topic:** Implementation

## Problem
Count pairs `(i, j)`, `i < j`, with `(ar[i] + ar[j])` divisible by `k`.

## Approach
Direct double loop over pairs (n ≤ 100, so O(n²) is fine).

## Complexity
- Time: **O(n²)**
- Space: **O(1)**

## Notes
- An O(n) follow-up exists using remainder frequencies (`rem` pairs with
  `k - rem`), worth knowing for interviews.
