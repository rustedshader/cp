def solve(a, b, n):
    arr1 = []
    arr2 = []
    a1 = 0
    a2 = 0
    for i in range(n):
        if i % 2 == 0:
            arr1.append(b[i])
            arr2.append(a[i])
            a2 += 1
        else:
            arr1.append(a[i])
            arr2.append(b[i])
            a1 += 1
    if arr1.count("0") >= a1 and arr2.count("0") >= a2:
        return True
    else:
        return False


for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    if solve(a, b, n):
        print("YES")
    else:
        print("NO")
