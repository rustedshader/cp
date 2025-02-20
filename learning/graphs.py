## BFS 

input_data: list = {1: [4,6] ,4: [3,2] , 6: [5] , 3: None , 2: None , 5: None }

visited = set()
def dfs_rec(node):
    print(node)
    if input_data[node] is not None:
        for num in input_data[node]:
            if num not in visited and not None:
                visited.add(num)
                dfs_rec(num)

# dfs_rec(1)

## BFS
def bfs(node):
    visited = set()
    queue = []
    queue.append(node)
    visited.add(node)
    while queue:
        s = queue.pop(0)
        print(s)
        if input_data[s] is not None:
            for num in input_data[s]:
                if num not in visited:
                    queue.append(num)
                    visited.add(num)

bfs(1)