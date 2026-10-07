"""
HackerRank - Birthday Cake Candles (Easy)
https://www.hackerrank.com/challenges/birthday-cake-candles/

Count how many candles have the maximum height.
"""


def birthdayCakeCandles(candles):
    return candles.count(max(candles))


if __name__ == "__main__":
    cases = [
        ([3, 2, 1, 3], 2, "1 sample"),
        ([10], 1, "2 edge (single candle)"),
        ([4, 4, 4, 4], 4, "3 edge (all tallest)"),
    ]
    passed = True
    for candles, expected, label in cases:
        got = birthdayCakeCandles(candles)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
