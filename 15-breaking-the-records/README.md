# Breaking the Records

**HackerRank:** https://www.hackerrank.com/challenges/breaking-best-and-worst-records/ ·
**Topic:** Implementation

## Problem
Count how many times the season's highest and lowest scores are broken.
Return `[high_breaks, low_breaks]`.

## Approach
Track running max/min from the first score; each new extreme increments its
counter. Single pass.

## Complexity
- Time: **O(n)**
- Space: **O(1)**
