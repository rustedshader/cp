import sys
x = sys.stdin.read()
lines = x.splitlines()
test_cases = lines[0]
i = 1
initial = 1
while i < len(lines):
    n = int(lines[i].split(" ")[0])
    m = int(lines[i].split(" ")[1])
    change = 0
    for k in range(1,n+1):
        for j in range(1,m+1):
            if str(lines[i+k][j-1]) == 'R':
                if j+1 > m:
                    change+=1
            if str(lines[i+k][j-1]) == 'D':
                if k+1 > n:
                    change+=1
    print(change)
    i += n+1

# Solution for codeforces problem https://codeforces.com/contest/1391/problem/B
