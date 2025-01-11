import sys
x = sys.stdin.read()
k = x.splitlines()[1].split(" ")[int(x.splitlines()[0].split(" ")[1]) - 1]
num_arr = x.splitlines()[1].split(" ")
sel_num = [num for num in num_arr if int(num) >= int(k) and int(num)>0]
print(len(sel_num))
