x = """4
10 10 1
0 0 3
-5 -8 8
4 -5 3"""

lines = x.splitlines()
t = int(lines[0])


for i in  range(1,t+1):
    x_m = int(lines[i].split(" ")[0])
    y_m = int(lines[i].split(" ")[1])
    k = int(lines[i].split(" ")[2])
    if k == 1:
        print(x_m,y_m)
    else:
        print(x_m-1,y_m-1)
