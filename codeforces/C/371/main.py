from collections import Counter
def binary_search(arr,N,to_find):
    low = 0
    high = N-1
    m = N//2
    while(high - low > 1):
        if (to_find > arr[m]):
            low = m+1
            m = (high + low) // 2
        else:
            high = m
            m = (high + low) // 2
    if arr[high] == to_find:
        return high
    elif arr[low] == to_find:
        return low
    else:
        return "Number not found !"

s = [k for k in input()]
nb,ns,nc = map(int,input().split(" "))
pb,ps,pc = map(int,input().split(" "))
r = int(input())
count = 0

c  = Counter(s)




print(s)
print(c)
print(count)
