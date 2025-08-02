from cmath import inf


for i in range(int(input())):
    n = int(input())
    n_arr = list(map(int,input().split(" ")))
    
    if n == 1:
        print(1)
        continue
    if n % 2 == 0:
        ans = n_arr[1] - n_arr[0]
        for t in range(2,n,2):
            ans = max(ans,(n_arr[t+1] - n_arr[t]))
        print(ans)
    else:
        ans = inf
        for p in range(n):
            temp_arr = n_arr[:p] + n_arr[p + 1:]
            mx = temp_arr[1] - temp_arr[0]
            for t in range(2,n-1,2):
                mx = max(mx,(temp_arr[t+1] - temp_arr[t]))
            ans = min(ans,mx)
        print(ans)