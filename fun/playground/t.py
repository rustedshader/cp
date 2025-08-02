n,s,m = map(int,input().split(" "))
ll = list(map(int,input().split(" ")))
count = 0
visited = set()
for num in ll:
    if s == m:
        print('magic')
        print(count)
        break
    if s > n:
        print('right')
        print(count)
        break
    if s < -1 * n:
        print('left')
        print(count)
        break
    if s in visited:
        print('cycle')
        print(count)
        break
    if num > 0:
        visited.add(s)
        s+=num
        count+=1
    if num < 0:
        visited.add(s)
        s-=abs(num)
        count+=1
