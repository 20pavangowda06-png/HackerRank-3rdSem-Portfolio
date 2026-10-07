"""
HackerRank - Sparse Arrays (Easy)
https://www.hackerrank.com/challenges/sparse-arrays/

Given a list of strings and a list of queries, return for each query how
many times it appears in the strings list.

Local test harness included below. On HackerRank, submit only the
sparseArrays function.
"""
from collections import Counter


def sparseArrays(strings, queries):
    freq = Counter(strings)  # one pass: O(N)
    return [freq[q] for q in queries]  # Counter returns 0 for missing keys


# Local tests: sample case plus edge cases.
if __name__ == "__main__":
    cases = [
        (["ab", "ab", "abc"], ["ab", "abc", "bc"], [2, 1, 0], "1 sample"),
        ([], ["a"], [0], "2 edge (no strings)"),
        (["x", "x", "x"], ["x", "y"], [3, 0], "3 edge (all identical)"),
        (["a", "b"], [], [], "4 edge (no queries)"),
    ]
    passed = True
    for strings, queries, expected, label in cases:
        got = sparseArrays(strings, queries)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
