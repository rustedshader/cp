from math import prod

def solve(n,k,arr):
    even = 0 
    if prod(arr) % k == 0:
        return 0
    if k == 4:
        for i in arr:
            if i % 2 == 0:
                even+=1
    diff_arr = []
    for i  in arr:
        diff_arr.append(k - (i % k))
    if k == 4:
        if even >= 2:
            op = 0
        if even == 1:
            op  = 1
        if even == 0:
            op  = 2
        return min(op,min(diff_arr))
    return(min(diff_arr))

for _ in range(int(input())):
    n,k = map(int,input().split())
    arr  = list(map(int,input().split()))
    print(solve(n,k,arr))