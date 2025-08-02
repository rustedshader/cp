import graphviz


class GraphNode:
    def __init__(self, value, right=None, left=None):
        self.right = right
        self.left = left
        self.value = value


def print_graph(root: GraphNode):
    if root is None:
        return
    print(root.value)
    print_graph(root.left)
    print_graph(root.right)


def draw_graph(dot: graphviz.Digraph, root: GraphNode):
    if root is None:
        return
    dot.node(str(root.value))
    if root.left is not None:
        dot.node(str(root.left.value))
        dot.edge(str(root.value), str(root.left.value))
    if root.right is not None:
        dot.node(str(root.right.value))
        dot.edge(str(root.value), str(root.right.value))
    draw_graph(dot, root.left)
    draw_graph(dot, root.right)


visited = set()


def dfs(root: GraphNode):
    if root is None:
        return
    visited.add(root)
    print(root.value)
    if root.left not in visited and root.left:
        dfs(root.left)
    if root.right not in visited and root.right:
        dfs(root.right)


def bfs(root: GraphNode):
    pass


if __name__ == "__main__":
    root = GraphNode(1)
    root.left = GraphNode(6, right=GraphNode(value=5), left=GraphNode(value=4))
    root.right = GraphNode(
        7, right=GraphNode(value=9, right=GraphNode(11)), left=GraphNode(value=10)
    )
    # print_graph(root)
    # dot = graphviz.Digraph()
    # draw_graph(dot, root)
    # dot.view()
    dfs(root)
    # print(visited)
