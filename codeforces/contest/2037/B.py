for _ in range(int(input())):
    k = int(input())
    k_arr = list(map(int, input().split()))
    k -= 2
    if k == 1:
        print(1, 1)
    else:
        factors = []
        i = 1
        while i * i <= k:
            if k % i == 0:
                factors += [(i, k // i)]
            i += 1
        for j, k in factors:
            if j in k_arr and k in k_arr:
                print(j, k)
                break