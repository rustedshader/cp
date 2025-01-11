import sys
x = sys.stdin.read()
lines = x.splitlines()
n = int(lines[0])
a = lines[1].split(" ")
a = [int(num) for num in a]
count=0
for i in range(1,len(a)):
    if a[i] < min(a[:i]):
        count+=1
    if a[i] > max(a[:i]):
        count+=1

print(count)

# Answer for https://codeforces.com/problemset/problem/155/A
