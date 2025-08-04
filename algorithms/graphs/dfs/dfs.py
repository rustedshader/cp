graph = {"A": ["B", "C", "D"], "B": ["E"], "C": ["D", "E"], "D": [], "E": []}
visited = set()


def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neigbour in graph[root]:
            dfs(visited, graph, neigbour)


if __name__ == "__main__":
    dfs(visited, graph, "A")
