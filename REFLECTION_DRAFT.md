# Reflective summary (draft, ~200 words) — Activity 8

Solving these five problems taught me that optimization is mostly about
choosing the right structure before writing a single line of logic. In Sparse
Arrays, the naive nested loop compares every query against every string —
O(n·q) — while a single frequency-map pass answers each query in O(1),
dropping the total to O(n+q). That one change, from scanning to hashing, was
the clearest lesson of the set: whenever a problem asks "how many times does
X occur", a hash map is almost always the answer. Diagonal Difference showed
the opposite virtue — restraint. With only two running sums and one pass over
n rows, the solution is O(n) time and O(1) space, and reaching for anything
heavier would be pure overhead. Dynamic Array demonstrated how a tiny bit of
bitwise arithmetic (XOR with the last answer) can route queries without any
search, and Time Conversion was a reminder that edge cases — midnight and
noon — deserve explicit tests, not assumptions. Writing local test harnesses
before submitting caught these early and made the HackerRank submissions pass
first try. The broader takeaway for my portfolio: I now analyse time and
space complexity as a habit, not an afterthought, and I document the
trade-off next to every solution so a reviewer can see the reasoning, not
just the code.
