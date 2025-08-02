for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    max_val = 0
    for i in range(n - 1):
        max_val = max(min(arr[i:i+2]),max_val)
    for i in range(n - 2):
        max_val = max(sorted(arr[i:i+3])[1],max_val)
    print(max_val)
