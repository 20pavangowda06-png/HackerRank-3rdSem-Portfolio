"""
HackerRank - A Very Big Sum (Easy)
https://www.hackerrank.com/challenges/a-very-big-sum/

Return the sum of very large integers (Python ints are unbounded, so this
is the same as a plain sum — the challenge is a nod to fixed-width
languages).
"""


def aVeryBigSum(ar):
    return sum(ar)


if __name__ == "__main__":
    cases = [
        ([1000000001, 1000000002, 1000000003, 1000000004, 1000000005],
         5000000015, "1 sample"),
        ([2**63, 2**63], 2**64, "2 edge (beyond 64-bit)"),
    ]
    passed = True
    for ar, expected, label in cases:
        got = aVeryBigSum(ar)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
