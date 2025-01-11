def solve(n: int):
    if n <= 4:
        return [-1]

    even_arr = []
    odd_arr = []
    ans = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
    ans = even_arr + odd_arr
    if ans:
        return ans
    else:
        return [-1]

for _ in range(int(input())):
    print(*solve(int(input())))