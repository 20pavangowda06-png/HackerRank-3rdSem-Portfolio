# Day of the Programmer

**HackerRank:** https://www.hackerrank.com/challenges/day-of-the-programmer/ ·
**Topic:** Implementation

## Problem
Return the date of the 256th day of `year` as `dd.mm.yyyy`, accounting for
the Julian→Gregorian calendar switch (Russia, 1918).

## Approach
1918 is special-cased (Feb 14 followed Jan 31 → day 256 is 26.09.1918).
Otherwise: Julian leap iff divisible by 4 (before 1918); Gregorian leap iff
divisible by 400, or by 4 but not 100. Leap years → 12.09, else 13.09.

## Complexity
- Time: **O(1)**
- Space: **O(1)**
