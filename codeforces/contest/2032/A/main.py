from itertools import permutations 

for _ in range(int(input())):
    n = int(input())
    s = list(map(int,input().split(" ")))
    perm = permutations(s,2)
    max_c = 0 
    for p in list(perm):
        c = 0
        for k in range(n):
            if p[0] ^ p[1] > 0:
                c+=1
        if c > max_c:
            max_c = c
        
    print(max_c)