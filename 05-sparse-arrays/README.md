# Sparse Arrays

**HackerRank:** https://www.hackerrank.com/challenges/sparse-arrays/ ·
**Topic:** Hash Maps / Strings

## Problem
Given `n` strings and `q` query strings, report for each query how many
times it occurs among the strings.

## Approach
Build a frequency map (`collections.Counter`) over the strings in one pass,
then answer each query with a single dict lookup. `Counter` returns 0 for
missing keys, so no existence checks are needed.

## Complexity
- Time: **O(n + q)** — one pass to count, O(1) per query
- Space: **O(n)** — the frequency map (bounded by distinct strings)

## Notes
- The naive nested-loop version is O(n·q); the hash map is what makes this
  efficient — the key lesson of the problem.
- `solution.py` contains a local test harness (`python3 solution.py`);
  submit only the `sparseArrays` function on HackerRank.
