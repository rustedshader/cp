import sys
x = sys.stdin.read()
lines = x.splitlines()
t = int(lines[0])
for i in range(1,t+1):
    x= [int(num) for num in lines[i]]
    sum = 0
    for values in x:
        sum+=values
    print(sum)
