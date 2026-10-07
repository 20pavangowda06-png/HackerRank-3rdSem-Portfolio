"""
HackerRank - Plus Minus (Easy)
https://www.hackerrank.com/challenges/plus-minus/

Print the ratios of positive, negative, and zero values in the array,
each on its own line with 6 decimal places.
"""
import io
from contextlib import redirect_stdout


def plusMinus(arr):
    n = len(arr)
    print(f"{sum(1 for x in arr if x > 0) / n:.6f}")
    print(f"{sum(1 for x in arr if x < 0) / n:.6f}")
    print(f"{sum(1 for x in arr if x == 0) / n:.6f}")


if __name__ == "__main__":
    cases = [
        ([-4, 3, -9, 0, 4, 1], "0.500000\n0.333333\n0.166667\n", "1 sample"),
        ([0, 0], "0.000000\n0.000000\n1.000000\n", "2 edge (all zero)"),
        ([1, 2, 3], "1.000000\n0.000000\n0.000000\n", "3 edge (all positive)"),
    ]
    passed = True
    for arr, expected, label in cases:
        buf = io.StringIO()
        with redirect_stdout(buf):
            plusMinus(arr)
        got = buf.getvalue()
        ok = got == expected
        print(f"Test {label}: {'PASS' if ok else 'FAIL'}")
        if not ok:
            print("got:     " + repr(got))
            print("expected:" + repr(expected))
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
