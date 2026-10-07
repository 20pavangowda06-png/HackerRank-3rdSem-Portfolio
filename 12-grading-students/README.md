# Grading Students

**HackerRank:** https://www.hackerrank.com/challenges/grading-students/ ·
**Topic:** Implementation

## Problem
Round each grade up to the next multiple of 5 if it's within 2 of it and
the grade is ≥ 38; otherwise leave unchanged.

## Approach
For each grade: if `g >= 38` and `g % 5 >= 3`, add `5 - (g % 5)`.
The `% 5 >= 3` test is exactly "less than 3 away from the next multiple".

## Complexity
- Time: **O(n)**
- Space: **O(n)** for the result list

## Notes
- Edge cases: 38 → 40 (boundary rounds up), 37 stays (below 38 never rounds).
