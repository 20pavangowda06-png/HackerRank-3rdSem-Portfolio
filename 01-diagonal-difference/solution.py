"""
HackerRank - Diagonal Difference (Easy)
https://www.hackerrank.com/challenges/diagonal-difference/

Given a square matrix, calculate the absolute difference between the sums
of its two diagonals (primary: top-left to bottom-right, secondary:
top-right to bottom-left).

Local test harness included below. On HackerRank, submit only the
diagonalDifference function.
"""


def diagonalDifference(arr):
    n = len(arr)
    primary = sum(arr[i][i] for i in range(n))
    secondary = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)


# Local tests: sample case plus edge cases.
if __name__ == "__main__":
    cases = [
        ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15, "1 sample"),
        ([[1]], 0, "2 edge (1x1 matrix)"),
        ([[1, 2], [3, 4]], 0, "3 edge (2x2, equal diagonals)"),
        ([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], 0,
         "4 edge (all negative, symmetric)"),
    ]
    passed = True
    for arr, expected, label in cases:
        got = diagonalDifference(arr)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
