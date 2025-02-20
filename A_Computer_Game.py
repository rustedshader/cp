# count = 0
# def check_if_move_possible(col,combined_matrix: list , x: int , y: int) -> bool:
#     global count
#     if x == 1 and y == col - 1:
#         count += 1
#         return True 
#     if x < 2 and y < col and x >= 0  and y >= 0:
#         if combined_matrix[x][y] == 1 :
#             return
#         if combined_matrix[x][y] == 0 :
#             return check_if_move_possible(col,combined_matrix,x-1,y), check_if_move_possible(col,combined_matrix,x,y-1),check_if_move_possible(col,combined_matrix,x+1,y-1), check_if_move_possible(col,combined_matrix,x+1,y+1), check_if_move_possible(col,combined_matrix,x,y+1) , check_if_move_possible(col,combined_matrix,x+1,y)

# def solve(col: int ,combined_matrix: list ):
#     global count
#     x: int = 0
#     y: int = 0
#     combined_matrix[1][col-1] == 0
#     print(check_if_move_possible(col,combined_matrix,x,y))
#     print(count)
# k = {}
# print(max(k.values))

# for _ in range(int(input())):
#     n = int(input())
#     level_one = list(map(int,input()))
#     level_two = list(map(int,input()))
#     combined_matrix = [level_one,level_two]
#     count = 0
#     level_one
#     solve(n,combined_matrix)

from collections import deque


def bfs(root):
    queue = []
    queue.append(root)

    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.pop(0)
            print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)










possible_moves = [1,-1]

def solve(start_x, start_y, dest_x, dest_y):
    if start_x == dest_x:
        return 0
    if start_y == dest_y:
        return 0
    queue = deque()
    queue.append(((start_x, start_y), 0))
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        node, count = queue.popleft()
        x, y = node

        if node == (dest_x, dest_y):
            return count - 1

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 1000 and 0 <= ny <= 1000 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), count + 1))

    return -1  

# print(solve(2, 1, 4, 1)) 


def solve(combined_matrix,x,y):
    queue = deque()
    count = 0 
    queue.append(((0,0),count))
    visited = set()
    visited.add((0,0))
    while queue:
        node,count =queue.popleft()
        x,y = node
        if node == (x,y):
            return count
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),(1,1),(-1,1),(1,-1),(-1,-1)]:
            nx,ny = x + dx , y+dy
            if 0 <= nx <= x and 0 <= ny <= 1 and (nx,ny) not in visited and combined_matrix[nx][ny] == 0:
                visited.add((nx,ny))
                queue.popleft((nx,ny),count + 1)
    return count

for _ in range(int(input())):
    n = int(input())
    level_one = list(map(int,input()))
    level_two = list(map(int,input()))
    combined_matrix = [level_one,level_two]
    count = 0
    print(solve(combined_matrix,n-1,1))