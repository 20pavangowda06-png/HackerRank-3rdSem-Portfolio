"""
HackerRank - Number Line Jumps / Kangaroo (Easy)
https://www.hackerrank.com/challenges/kangaroo/

Two kangaroos start at x1, x2 (x1 < x2) jumping v1, v2 per step.
Return "YES" if they ever land on the same spot, else "NO".
"""


def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"  # starts behind and never faster: can never catch up
    # need n >= 0 with x1 + n*v1 = x2 + n*v2  ->  (x2-x1) divisible by (v1-v2)
    return "YES" if (x2 - x1) % (v1 - v2) == 0 else "NO"


if __name__ == "__main__":
    cases = [
        ((0, 3, 4, 2), "YES", "1 sample"),
        ((0, 2, 5, 3), "NO", "2 sample (slower, behind)"),
        ((0, 5, 10, 5), "NO", "3 edge (same speed)"),
        ((0, 4, 8, 2), "YES", "4 edge (meets exactly)"),
        ((0, 4, 7, 2), "NO", "5 edge (never aligns)"),
    ]
    passed = True
    for args, expected, label in cases:
        got = kangaroo(*args)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
