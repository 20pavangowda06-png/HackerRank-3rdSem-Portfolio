# Staircase

**HackerRank:** https://www.hackerrank.com/challenges/staircase/ ·
**Topic:** Warmup

## Problem
Print a right-aligned staircase of `#` of height `n`.

## Approach
Row `i` (1-based) prints `n - i` spaces followed by `i` hashes.
The function prints directly, as HackerRank's driver expects.

## Complexity
- Time: **O(n²)** — n rows of up to n characters
- Space: **O(1)**
