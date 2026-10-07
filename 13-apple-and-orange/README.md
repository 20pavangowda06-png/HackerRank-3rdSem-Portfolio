# Apple and Orange

**HackerRank:** https://www.hackerrank.com/challenges/apple-and-orange/ ·
**Topic:** Implementation

## Problem
Count apples landing in `[s, t]` from tree at `a` (position `a + d`) and
oranges from tree at `b`. Print the two counts.

## Approach
Two generator counts with chained comparisons `s <= a + d <= t`.
Prints directly, one count per line.

## Complexity
- Time: **O(m + n)** (m apples, n oranges)
- Space: **O(1)**
