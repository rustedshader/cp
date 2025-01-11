from collections import defaultdict

s = set()

s.add(1)
s.add(2)

print(s)

k = {"greg": 1, "steve": 2}
print(k["steve"])


default = defaultdict(int)
print(default[2])

default = defaultdict(list)  # Common in leetcode problems
print(default[2])

from collections import Counter

string_ = "aaababbbbabababab"


print(Counter(string_))
