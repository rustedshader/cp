def solve(n):
    if (n + 1) % 3 == 0 or (n - 1) % 3 == 0:
        return "First"
    return "Second"


# 1
# 0


for _ in range(int(input())):
    n = int(input())
    print(solve(n))
