def solve(n,m,a):
    length = (n + a - 1) // a
    width = (m + a - 1) // a
    return length * width

n,m,a = map(int,input().split(" "))
print(solve(n,m,a))