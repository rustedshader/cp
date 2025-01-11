for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split(" ")))
    arb_arr = [x for x in range(1,n+1)]
    # print(arb_arr)
    for i in range(0,n):
        print(arb_arr[i:n])
    print()
