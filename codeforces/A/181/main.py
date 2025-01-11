import sys
v = sys.stdin.read()
n = v.splitlines()[0].split(" ")[0]
m = v.splitlines()[0].split(" ")[1]

arr = []
x_cords = []
y_cords = []
for i in range(1,len(v.splitlines())):
    z = (v.splitlines()[i])
    for k in range(0,len(z)):
        if z[k] == "*":
            # print(z[k],i,k+1)
            x_cords.append(i)
            y_cords.append(k+1)

for num in x_cords:
    if x_cords.count(num) == 1:
        arr.append(str(num))
for num in y_cords:
    if y_cords.count(num) == 1:
        arr.append(str(num))

print(' '.join(arr))

# Answer for codeforces https://codeforces.com/problemset/problem/181/A
