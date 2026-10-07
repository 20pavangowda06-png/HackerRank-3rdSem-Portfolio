"""
HackerRank - Simple Array Sum (Easy)
https://www.hackerrank.com/challenges/simple-array-sum/

Return the sum of an array's elements.
"""


def simpleArraySum(ar):
    return sum(ar)


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 10, 11], 31, "1 sample"),
        ([-5], -5, "2 edge (single negative)"),
        ([1000000000, 1000000000], 2000000000, "3 edge (large values)"),
    ]
    passed = True
    for ar, expected, label in cases:
        got = simpleArraySum(ar)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
