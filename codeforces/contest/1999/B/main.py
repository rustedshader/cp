import sys
x = """5
3 8 2 6
1 1 1 1
10 10 2 2
1 1 10 10
3 8 7 2"""
lines = x.splitlines()
t = int(lines[0])
for i in range(1,t+1):
    numbers_arr = lines[i].split(" ")
    numbers_arr = [int(num) for num in numbers_arr]
    a1 = numbers_arr[0]
    a2 = numbers_arr[1]
    b1 = numbers_arr[2]
    b2 = numbers_arr[3]
    sum = 0
    if a1>b1:
        sum+=1
    if a2>b2:
        sum+=1
    if a1>b2:
        sum+=1
    if a2>b1:
        sum+=1
