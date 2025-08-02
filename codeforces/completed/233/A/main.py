n = int(input())
lst = [0] * n
if n % 2 != 0:
    print("-1")
else:
    for i in range(0, n):
        if i % 2 == 0:
            lst[i+1] = i + 1
        else:
            lst[i-1] = i + 1
    finLst = [str(x) for x in lst]
    print(" ".join(finLst))
# Solution for https://codeforces.com/problemset/problem/233/A
