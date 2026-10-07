# Compare the Triplets

**HackerRank:** https://www.hackerrank.com/challenges/compare-the-triplets/ ·
**Topic:** Basic Implementation

## Problem
Alice and Bob each have 3 challenge ratings. Compare them pairwise: the
higher rating in a category earns its owner one point; ties earn nothing.
Return `[alice_points, bob_points]`.

## Approach
Zip the two triplets and count pairwise wins for each side with generator
expressions — one pass, no indexing bugs.

## Complexity
- Time: **O(1)** — always exactly 3 comparisons
- Space: **O(1)**

## Notes
- Trivially generalises to any number of categories (still O(k)).
- `solution.py` contains a local test harness (`python3 solution.py`);
  submit only the `compareTriplets` function on HackerRank.
