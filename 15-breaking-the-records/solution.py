"""
HackerRank - Breaking the Records (Easy)
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/

Given season scores, count how many times the highest and lowest records
are broken. Return [high_breaks, low_breaks].
"""


def breakingRecords(scores):
    hi = lo = scores[0]
    high_breaks = low_breaks = 0
    for s in scores[1:]:
        if s > hi:
            hi, high_breaks = s, high_breaks + 1
        elif s < lo:
            lo, low_breaks = s, low_breaks + 1
    return [high_breaks, low_breaks]


if __name__ == "__main__":
    cases = [
        ([10, 5, 20, 20, 4, 5, 2, 25, 1], [2, 4], "1 sample"),
        ([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], [4, 0], "2 sample"),
        ([5], [0, 0], "3 edge (single game)"),
        ([1, 2, 3, 4], [3, 0], "4 edge (always improving)"),
    ]
    passed = True
    for scores, expected, label in cases:
        got = breakingRecords(scores)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
