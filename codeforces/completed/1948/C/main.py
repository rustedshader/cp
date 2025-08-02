from collections import deque
for _ in range(int(input())):
    n = int(input())
    s = list(map(str.strip, [input() for _ in range(2)]))
    visited = [[0] * n for _ in range(2)]
    visited[0][0] = 1
    queue = deque()
    queue.append([0,0])
    while queue:
        x,y = queue.popleft()
        if x-1 >= 0:
            if s[x-1][y] == '>' and y+1<n and visited[x-1][y+1] != 1:
                queue.append([x-1,y+1])
                visited[x-1][y+1] = 1
        if x-1 >= 0:
            if s[x-1][y] == '<' and  y-1>=0 and visited[x-1][y-1] != 1:
                queue.append([x-1,y-1])
                visited[x-1][y-1] = 1
        if x+1 <= 1:
            if s[x+1][y] == '>' and  y+1 <n and visited[x+1][y+1] != 1:
                queue.append([x+1,y+1])
                visited[x+1][y+1] = 1
        if x+1 <= 1:
            if s[x+1][y] == '<' and  y-1 >= 0 and visited[x+1][y-1] != 1:
                queue.append([x+1,y-1])
                visited[x+1][y-1] = 1
        if y-1 >= 0:
            if s[x][y-1] == '<' and  y-2>=0 and  visited[x][y-2] != 1:
                queue.append([x,y-2])
                visited[x][y-2] = 1
        if y+1 < n:
            if s[x][y+1] == '>' and  y+2 < n and  visited[x][y+2] != 1:
                queue.append([x,y+2])
                visited[x][y+2] = 1
    if visited[1][n-1] == 1:
        print('YES')
    else:
        print('NO')

# == initialisation error in line which caused more moemory to be used and caused tle  