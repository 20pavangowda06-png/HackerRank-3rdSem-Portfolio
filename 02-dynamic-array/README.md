# Dynamic Array

**HackerRank:** https://www.hackerrank.com/challenges/dynamic-array/ ·
**Topic:** Data Structures / Vectors

## Problem
Maintain `n` sequences under `q` queries of the form `[type, x, y]`:
- type 1: append `y` to sequence `((x ^ lastAnswer) % n)`
- type 2: set `lastAnswer = seq[((x ^ lastAnswer) % n)][y % size]` and record it.

Return all recorded answers.

## Approach
Keep a list of `n` lists plus a `lastAnswer` variable. Each query is handled
in O(1): the XOR-plus-modulo picks the target sequence, then it's either an
append or an indexed read whose result is collected.

## Complexity
- Time: **O(n + q)** — n sequence initialisation + one O(1) step per query
- Space: **O(n + total appended elements)** — the sequences themselves

## Notes
- The XOR with `lastAnswer` makes query routing depend on previous answers,
  so queries can't be trivially parallelised — that's the intended trap.
- `solution.py` contains a local test harness (`python3 solution.py`);
  submit only the `dynamicArray` function on HackerRank.
