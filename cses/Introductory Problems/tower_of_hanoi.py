n = int(input())
x1 = [k for k in range(n+1,1,-1)]
x2 = [0]
x3 = [0]

if x2[-1] < x1[-1]:
    break
else:
    x2.append(x1[-1])
    x1.pop(-1)
if x3[-1] < x1[-1]:
    break
else:
    x3.append(x1[-1])
    x1.pop(-1)
if x2[-1] > x1[-1] and x3[-1] > x1[-1]:
    if x3[-1] > x2[-1]:
        x3.append(x2[-1])
        x2.pop(-1)
    else:
        x2.append(x3[-1]) 
        x3.pop(-1)