from itertools import accumulate
from bisect import bisect_right

for _ in range(int(input())):
    n, q = map(int, input().split())
    n_arr = list(map(int, input().split()))
    q_arr = list(map(int, input().split()))
    prefix_sums = list(accumulate(n_arr, initial=0))
    cumulative_max = list(accumulate(n_arr, max, initial=0))
    print(prefix_sums, cumulative_max) 
    result = []
    for query in q_arr:
        idx = bisect_right(cumulative_max, query) - 1
        result.append(prefix_sums[idx])
    print(*result)
