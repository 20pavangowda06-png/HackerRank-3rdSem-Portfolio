"""
HackerRank - Apple and Orange (Easy)
https://www.hackerrank.com/challenges/apple-and-orange/

Count how many apples and oranges land on Sam's house [s, t].
Apples fall from tree at `a` (position a + d), oranges from `b`.
Prints the apple count then the orange count, one per line.
"""
import io
from contextlib import redirect_stdout


def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(1 for d in apples if s <= a + d <= t))
    print(sum(1 for d in oranges if s <= b + d <= t))


if __name__ == "__main__":
    cases = [
        ((7, 11, 5, 15, [-2, 2, 1], [5, -6]), "1\n1\n", "1 sample"),
        ((0, 10, 0, 10, [], []), "0\n0\n", "2 edge (no fruit)"),
        ((5, 5, 0, 10, [5], [-5]), "1\n1\n", "3 edge (boundary hits)"),
    ]
    passed = True
    for args, expected, label in cases:
        buf = io.StringIO()
        with redirect_stdout(buf):
            countApplesAndOranges(*args)
        got = buf.getvalue()
        ok = got == expected
        print(f"Test {label}: got {got!r} (expected {expected!r}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
