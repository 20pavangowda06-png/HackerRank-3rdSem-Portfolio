"""
HackerRank - Migratory Birds (Easy)
https://www.hackerrank.com/challenges/migratory-birds/

Return the id of the most frequently sighted bird type; on ties, the
smallest id wins.
"""
from collections import Counter


def migratoryBirds(arr):
    counts = Counter(arr)
    return min(counts, key=lambda t: (-counts[t], t))


if __name__ == "__main__":
    cases = [
        ([1, 4, 4, 4, 5, 3], 4, "1 sample"),
        ([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4], 3, "2 sample (tie -> smaller id)"),
        ([2, 2, 2], 2, "3 edge (single type)"),
    ]
    passed = True
    for arr, expected, label in cases:
        got = migratoryBirds(arr)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
