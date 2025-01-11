from cmath import inf

def solve(n: int):
    pairs = (1,n)
    min = inf
    for k in range(1,n//2 + 1):
        if (k) % (n-k) == 0:
            if k // (n-k) < min:
                min = k // (n-k)
                pairs = (k,n-k)
        elif (n-k) % k == 0:
            if (n-k) // k  < min:
                min = (n-k) // k
                pairs = (n-k,k)
    return pairs


for _ in range(int(input())):
    n = int(input())
    print(*solve(n))