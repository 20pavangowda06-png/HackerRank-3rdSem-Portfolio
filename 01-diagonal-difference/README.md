# Diagonal Difference

**HackerRank:** https://www.hackerrank.com/challenges/diagonal-difference/ ·
**Topic:** 2D Arrays / Matrices

## Problem
Given an `n × n` matrix, compute the absolute difference between the sums of
its primary diagonal (top-left → bottom-right) and secondary diagonal
(top-right → bottom-left).

## Approach
Single pass over the row index `i`: accumulate `arr[i][i]` for the primary
diagonal and `arr[i][n-1-i]` for the secondary diagonal, then take the
absolute difference. No extra data structures needed.

## Complexity
- Time: **O(n)** — one pass over n rows
- Space: **O(1)** — two running sums

## Notes
- Works for negative values and 1×1 matrices without special-casing.
- `solution.py` contains a local test harness (`python3 solution.py`);
  submit only the `diagonalDifference` function on HackerRank.
