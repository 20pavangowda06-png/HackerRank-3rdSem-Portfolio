"""
HackerRank - Compare the Triplets (Easy)
https://www.hackerrank.com/challenges/compare-the-triplets/

Alice and Bob each have 3 ratings. For each category, the higher rating
earns its owner a point (ties earn nothing). Return [alice_points, bob_points].

Local test harness included below. On HackerRank, submit only the
compareTriplets function.
"""


def compareTriplets(a, b):
    alice = sum(1 for x, y in zip(a, b) if x > y)
    bob = sum(1 for x, y in zip(a, b) if x < y)
    return [alice, bob]


# Local tests: sample case plus edge cases.
if __name__ == "__main__":
    cases = [
        ([5, 6, 7], [3, 6, 10], [1, 1], "1 sample"),
        ([1, 1, 1], [1, 1, 1], [0, 0], "2 edge (all ties)"),
        ([10, 10, 10], [1, 1, 1], [3, 0], "3 edge (clean sweep)"),
        ([1, 2, 3], [3, 2, 1], [1, 1], "4 edge (mixed with a tie)"),
    ]
    passed = True
    for a, b, expected, label in cases:
        got = compareTriplets(a, b)
        ok = got == expected
        print(f"Test {label}: {a} vs {b} -> {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
