def solve(n, x, arr: list):
    if n > 1:
        max_diff = float("-inf")
        for i in range(n - 1):
            if arr[i + 1] - arr[i] > max_diff:
                max_diff = arr[i + 1] - arr[i]
        return max(max(max_diff, 2 * (x - max(arr))), arr[0])
    else:
        return max(arr[0], 2 * (x - arr[0]))


for _ in range(int(input())):
    n, x = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    print(solve(n, x, arr))
