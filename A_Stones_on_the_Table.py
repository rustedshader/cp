def solve(s: str):
    l_s = len(s)
    count = 0
    for i in range(l_s - 2):
        if s[i] == s[i+2] and s[i] != s[i+1] and s[i+2] != s[i+1] :
            count+=1
    return count



n = int(input())
s = input()
print(solve(s))


