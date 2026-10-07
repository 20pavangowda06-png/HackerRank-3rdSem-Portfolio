"""
HackerRank - Divisible Sum Pairs (Easy)
https://www.hackerrank.com/challenges/divisible-sum-pairs/

Count pairs (i, j) with i < j such that (ar[i] + ar[j]) is divisible by k.
"""


def divisibleSumPairs(n, k, ar):
    return sum(1 for i in range(n)
               for j in range(i + 1, n)
               if (ar[i] + ar[j]) % k == 0)


if __name__ == "__main__":
    cases = [
        ((6, 3, [1, 3, 2, 6, 1, 2]), 5, "1 sample"),
        ((2, 2, [1, 1]), 1, "2 edge (single pair)"),
        ((3, 5, [1, 1, 1]), 0, "3 edge (no divisible pair)"),
    ]
    passed = True
    for args, expected, label in cases:
        got = divisibleSumPairs(*args)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
