for _ in range(0,int(input())):
    n = int(input())
    s = input()
    if s[0] == s[-1]:
        print("NO")
    if s[0] != s[-1]:
        print("YES")
