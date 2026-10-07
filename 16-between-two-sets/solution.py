"""
HackerRank - Between Two Sets (Easy)
https://www.hackerrank.com/challenges/between-two-sets/

Count integers x such that every element of `a` divides x and x divides
every element of `b`. Such x are exactly the multiples of lcm(a) that
also divide gcd(b).
"""
import math


def getTotalX(a, b):
    l = 1
    for x in a:
        l = l * x // math.gcd(l, x)
    g = 0
    for x in b:
        g = math.gcd(g, x)
    return sum(1 for m in range(l, g + 1, l) if g % m == 0)


if __name__ == "__main__":
    cases = [
        (([2, 4], [16, 32, 96]), 3, "1 sample"),
        (([3, 4], [24, 48]), 2, "2 sample"),
        (([2], [3]), 0, "3 edge (no valid integer)"),
        (([1], [100]), 9, "4 edge (divisors of 100)"),
    ]
    passed = True
    for args, expected, label in cases:
        got = getTotalX(*args)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
