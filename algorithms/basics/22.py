N = int(input())
k = (N*2)-1
s = 1
e = k-1

arr = [N]*k
for _ in range(k):
    print(*arr,sep='')
    if(e-s > 0):
        for i in range(s,e):
            arr[i]-=1
        s+=1
        e-=1
    else:
        for i in range(e,s):
            arr[i]+=1
        s+=1
        e-=1
