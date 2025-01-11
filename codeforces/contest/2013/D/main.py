for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    for i in range(n-1):
        arr[i] -= 1
        arr[i+1] += 1
    print(arr)
