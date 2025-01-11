from collections import deque

# use deque as its more pythony way of doing things

data = {"1": ["2", "3"], "2": ["4", "5"], "3": [], "4": [], "5": []}


visited = set()


def bfs(data: dict, visited: set, node: str):
    queue = deque()
    visited.add(node)
    queue.append(node)
    while queue:
        m = queue.popleft()
        print(m)
        for n in data[m]:
            if n not in visited:
                visited.add(n)
                queue.append(n)


if __name__ == "__main__":
    bfs(data, visited, "1")
