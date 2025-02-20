# class Node:
#     def __init__(self,key):
#         self.key = key
#         self.left = None
#         self.right = None

# def insert(root,key):
#     if root is None:
#         return Node(key)
#     if key < root.key:
#         root.left = insert(root.left,key)
#     else:
#         root.right = insert(root.right, key)
#     return root

# def create_bst_from_array(arr):
#     root = None
#     for key in arr:
#         root = insert(root,key)
#     return root

# print(create_bst_from_array([5,4,3,2,1]).key)
# print(chr(ord("a") - 32) )

# string = "pratham jain"

# ord(' ')
# for character in input(): print((chr(ord(character) - 32)), end="")


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# def add_to_graph(arr):
#     root = Node()
#     n = len(arr)

# arr = [3,1,4,2,5]
# arr.sort()

# root = sorted_array_to_bst(arr)
# print("INORDER traversal of BST:")
# inorder_traversal(root)


# def insert(root,value):
#     if root is None:
#         return Node(value)
#     if value < root.value:
#         root.left = insert(root.left ,value)
#     else:
#         root.right = insert(root.right , value)
#     return root

# # Left -> Root -> Right

# def inorder_traversel(node):
#     if node:
#         inorder_traversel(node.left)
#         print(node.value)
#         inorder_traversel(node.right)

# root = Node(5)

# insert(root,2)
# insert(root,7)
# insert(root,1)
# insert(root,8)

# inorder_traversel(root)

print(sum([i  for i in range(101) if i % 10 == 0]))

