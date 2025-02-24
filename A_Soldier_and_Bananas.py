def solve(k,n,w):
    cost = 0
    for i in range(1,w+1):
        cost += k * i
    if cost < n:
        return 0
    return cost - n
        
k,n,w = map(int,input().split(" "))
print(solve(k,n,w))