"""
HackerRank - Dynamic Array (Easy)
https://www.hackerrank.com/challenges/dynamic-array/

Maintain N sequences. Queries are [type, x, y]:
  type 1: append y to sequence ((x ^ lastAnswer) % N)
  type 2: set lastAnswer to seq[((x ^ lastAnswer) % N)][y % size], record it.
Return all recorded answers.

Local test harness included below. On HackerRank, submit only the
dynamicArray function.
"""


def dynamicArray(n, queries):
    seqs = [[] for _ in range(n)]
    last_answer = 0
    result = []
    for q, x, y in queries:
        idx = (x ^ last_answer) % n
        if q == 1:
            seqs[idx].append(y)
        else:  # q == 2
            last_answer = seqs[idx][y % len(seqs[idx])]
            result.append(last_answer)
    return result


# Local tests: sample case plus edge cases.
if __name__ == "__main__":
    cases = [
        (2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]],
         [7, 3], "1 sample"),
        (1, [[1, 0, 42], [2, 0, 0]], [42], "2 edge (single sequence)"),
        (3, [[1, 5, 9], [1, 5, 9], [2, 5, 1]], [9],
         "3 edge (xor wraps index around)"),
    ]
    passed = True
    for n, queries, expected, label in cases:
        got = dynamicArray(n, queries)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
