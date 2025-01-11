import sys

x = sys.stdin.read()

n = int(x.splitlines()[0])
matrix_element = []
sum = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            sum+=int(x.splitlines()[i].split(" ")[j-1])
        elif (n+1)/2 == i:
            sum+=int(x.splitlines()[i].split(" ")[j-1])
        elif (n+1)/2 == j:
            sum+=int(x.splitlines()[i].split(" ")[j-1])
        elif i+j == n+1:
            sum+=int(x.splitlines()[i].split(" ")[j-1])
print(sum)
