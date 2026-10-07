# Migratory Birds

**HackerRank:** https://www.hackerrank.com/challenges/migratory-birds/ ·
**Topic:** Implementation

## Problem
Return the most frequently sighted bird type id; ties go to the smallest id.

## Approach
`Counter` for frequencies, then `min` with key `(-count, id)` — maximises
count, breaks ties toward the smaller id.

## Complexity
- Time: **O(n)**
- Space: **O(k)** for k distinct types
