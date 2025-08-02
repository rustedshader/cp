import graphviz


class TreeNode:
    def __init__(self,val,right=None,left=None):
        self.val =val
        self.right = right
        self.left =left 


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    for i in range(4, 10):
        root.left.left = TreeNode(i)
    for i in range(10, 15):
        root.right.right = TreeNode(i)
    dot = graphviz.Digraph()
    dot.node(str(root.val))
    dot.node(str(root.left.val))
    dot.node(str(root.right.val))
    dot.node(str(root.left.left.val))
    dot.node(str(root.right.right.val))
    dot.edge(str(root.val), str(root.left.val))
    dot.edge(str(root.val), str(root.right.val))
    dot.edge(str(root.left.val), str(root.left.left.val))
    dot.edge(str(root.right.val), str(root.right.right.val))
    dot.render('test-output/round-table.gv', view=True)


