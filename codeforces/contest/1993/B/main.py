x =  """7
5
1 3 5 7 9
4
4 4 4 4
3
2 3 4
4
3 2 2 8
6
4 3 6 1 2 1
6
3 6 1 2 1 2
5
999999996 999999997 999999998 999999999 1000000000"""


lines = x.splitlines()
t = int(lines[0])

for i in range(1,t*2+1,2):
    n = lines[i]
    a = lines[i+1].split(" ")
    a = [int(num) for num in a]
    for p in range(0,len(a)):
        for k in range(0,len(a)):
            print(p,k)
