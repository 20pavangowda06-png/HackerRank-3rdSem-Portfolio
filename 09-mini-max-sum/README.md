# Mini-Max Sum

**HackerRank:** https://www.hackerrank.com/challenges/mini-max-sum/ ·
**Topic:** Warmup

## Problem
Given 5 positive integers, print the minimum and maximum sums of any 4.

## Approach
`min_sum = total - max(arr)`, `max_sum = total - min(arr)` — excluding the
largest (smallest) element gives the extreme 4-element sums. Prints directly.

## Complexity
- Time: **O(n)**
- Space: **O(1)**
