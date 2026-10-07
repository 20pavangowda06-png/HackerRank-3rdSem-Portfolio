"""
HackerRank - Mini-Max Sum (Easy)
https://www.hackerrank.com/challenges/mini-max-sum/

Given 5 positive integers, print the minimum and maximum sums obtainable
by summing exactly 4 of them. Prints "min max".
"""
import io
from contextlib import redirect_stdout


def miniMaxSum(arr):
    total = sum(arr)
    print(total - max(arr), total - min(arr))


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], "10 14\n", "1 sample"),
        ([7, 69, 2, 221, 8974], "299 9271\n", "2 sample"),
        ([5, 5, 5, 5, 5], "20 20\n", "3 edge (all equal)"),
    ]
    passed = True
    for arr, expected, label in cases:
        buf = io.StringIO()
        with redirect_stdout(buf):
            miniMaxSum(arr)
        got = buf.getvalue()
        ok = got == expected
        print(f"Test {label}: got {got!r} (expected {expected!r}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
