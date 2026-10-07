"""
HackerRank - Grading Students (Easy)
https://www.hackerrank.com/challenges/grading-students/

Round each grade up to the next multiple of 5 if the difference is less
than 3 AND the grade is at least 38. Otherwise leave it unchanged.
"""


def gradingStudents(grades):
    result = []
    for g in grades:
        if g >= 38 and g % 5 >= 3:
            g += 5 - (g % 5)
        result.append(g)
    return result


if __name__ == "__main__":
    cases = [
        ([73, 67, 38, 33], [75, 67, 40, 33], "1 sample"),
        ([38], [40], "2 edge (boundary rounds up)"),
        ([37], [37], "3 edge (below 38 never rounds)"),
        ([100, 0], [100, 0], "4 edge (extremes)"),
    ]
    passed = True
    for grades, expected, label in cases:
        got = gradingStudents(grades)
        ok = got == expected
        print(f"Test {label}: got {got} (expected {expected}): "
              f"{'PASS' if ok else 'FAIL'}")
        passed &= ok
    print("ALL TESTS PASSED" if passed else "SOME TESTS FAILED")
