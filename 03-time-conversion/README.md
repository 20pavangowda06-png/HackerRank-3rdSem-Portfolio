# Time Conversion

**HackerRank:** https://www.hackerrank.com/challenges/time-conversion/ ·
**Topic:** Strings & Logic

## Problem
Convert a 12-hour clock time string like `"07:05:45PM"` to 24-hour format
(`"19:05:45"`).

## Approach
Split off the `AM`/`PM` suffix and the `hh:mm:ss` parts. Adjust the hour:
12 AM → 0, 12 PM stays 12, other PM hours get +12, AM hours are unchanged.
Reassemble with zero-padded hour.

## Complexity
- Time: **O(1)** — fixed-size string
- Space: **O(1)**

## Notes
- The only tricky cases are the 12 o'clock boundaries (midnight/noon) —
  covered by explicit edge-case tests.
- `solution.py` contains a local test harness (`python3 solution.py`);
  submit only the `timeConversion` function on HackerRank.
