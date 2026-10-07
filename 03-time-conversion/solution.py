"""
HackerRank - Time Conversion (Easy)
https://www.hackerrank.com/challenges/time-conversion/

Convert a 12-hour AM/PM time string (e.g. "07:05:45PM") to 24-hour format
(e.g. "19:05:45").

Local test harness included below. On HackerRank, submit only the
timeConversion function.
"""


def timeConversion(s):
    period = s[-2:]            # "AM" or "PM"
    hh, mm, ss = s[:-2].split(":")
    h = int(hh)
    if period == "AM":
        h = 0 if h == 12 else h      # 12 AM -> 00
    else:  # PM
        h = h if h == 12 else h + 12  # 12 PM stays 12
    return f"{h:02d}:{mm}:{ss}"


# Local tests: sample case plus edge cases (midnight / noon boundaries).
if __name__ == "__main__":
    cases = [
        ("07:05:45PM", "19:05:45", "1 sample"),
        ("12:01:00AM", "00:01:00", "2 edge (midnight)"),
        ("12:01:00PM", "12:01:00", "3 edge (noon)"),
        ("01:00:00AM", "01:00:00", "4 edge (plain AM)"),
        ("11:59:59PM", "23:59:59", "5 edge (end of day)"),
    ]
    passed = True
    for s, expected, label in cases:
        got = timeConversion(s)
        ok = got == expected
        print(f"Test {label}: '{s}' -> '{got}' (expected '{expected}'): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
