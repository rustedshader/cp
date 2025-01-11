data = {"1": ["2", "3"], "2": ["4", "5"], "3": [], "4": [], "5": []}

visited = set()


def dfs(data: dict, visited: set, node: str) -> None:
    if node not in visited:
        visited.add(node)
        print(node)
        for n in data[node]:
            dfs(data, visited, n)


if __name__ == "__main__":
    dfs(data, visited, "1")
