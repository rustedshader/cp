from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split(' ')))
    max_count  = max(Counter(arr).values())
    k = len(set(arr))
    print(max(min(max_count-1,k),min(max_count,k-1)))
