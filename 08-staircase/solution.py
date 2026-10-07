"""
HackerRank - Staircase (Easy)
https://www.hackerrank.com/challenges/staircase/

Print a right-aligned staircase of '#' of height n. This function prints
directly (HackerRank's driver just calls it).
"""
import io
from contextlib import redirect_stdout


def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)


if __name__ == "__main__":
    cases = [
        (4, "   #\n  ##\n ###\n####\n", "1 sample"),
        (1, "#\n", "2 edge (n=1)"),
        (2, " #\n##\n", "3 edge (n=2)"),
    ]
    passed = True
    for n, expected, label in cases:
        buf = io.StringIO()
        with redirect_stdout(buf):
            staircase(n)
        got = buf.getvalue()
        ok = got == expected
        print(f"Test {label}: {'PASS' if ok else 'FAIL'}")
        if not ok:
            print("got:     " + repr(got))
            print("expected:" + repr(expected))
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
