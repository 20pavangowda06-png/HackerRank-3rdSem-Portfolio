"""
HackerRank - Day of the Programmer (Easy)
https://www.hackerrank.com/challenges/day-of-the-programmer/

Return the date of the 256th day of `year` as "dd.mm.yyyy".
Julian calendar (leap if divisible by 4) up to 1917, Gregorian after 1918;
1918 is the transition year (Feb had 15 days -> day 256 is 26.09.1918).
"""


def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"
    if year < 1918:
        leap = (year % 4 == 0)
    else:
        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return f"12.09.{year}" if leap else f"13.09.{year}"


if __name__ == "__main__":
    cases = [
        (2017, "13.09.2017", "1 sample"),
        (2016, "12.09.2016", "2 sample (Gregorian leap)"),
        (1800, "12.09.1800", "3 edge (Julian leap: 1800 % 4 == 0)"),
        (1918, "26.09.1918", "4 edge (transition year)"),
        (2100, "13.09.2100", "5 edge (Gregorian non-leap century)"),
    ]
    passed = True
    for year, expected, label in cases:
        got = dayOfProgrammer(year)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
