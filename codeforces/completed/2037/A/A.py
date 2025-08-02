for _ in range(int(input())):
    n = int(input())
    n_arr = list(map(int, input().split()))
    n_set = set(n_arr)
    t = 0
    for i in n_set:
        if n_arr.count(i) > 1:
            max_score = n_arr.count(i) // 2
            t+=max_score
    print(t)