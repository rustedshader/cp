x = [1,2,3]
ans = []

for i in range(len(x)):
    for k in range(i+1,len(x)+1):
        ans.append(x[i:k])
print(ans)


s = 'shubhang'
ans2 = set()
for i in range(len(s)):
    for k in range(i+1,len(s)+1):
        ans2.add(s[i:k])

print(ans2)
