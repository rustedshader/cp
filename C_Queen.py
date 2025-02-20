# def solve(tree_arr):
#     for _ in tree_arr:
#         pi,ci = _
#         if ci == 1:
#             x`xxxxx`
#     pass




# tree_arr = []
# for _ in range(int(input())):
#     x,y = map(int,input().split(" "))
#     tree_arr.append((x,y))
# class newNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = self.right = None

# def insertLevelOrder(arr,i,n):
#     root = None
#     if i < n:
#         root = newNode(arr[i])
#         root.left = insertLevelOrder(arr,2*i + 1 , n)
#         root.right = insertLevelOrder(arr,2*i+ 2 , n)
#     return root

# def inOrder(root):
#     if root != None:
#         inOrder(root.left)
#         print(root.data,end=' ')
#         inOrder(root.right)

# x = [5,3,6,2,4,None,7]
# key = 3

# def traverse_tree():
#     for i in range(len(x)-2):
#         print(x[i])
#         print(x[i+1],print(i+2))


# root = None
# root = insertLevelOrder(x,0,len(x))
# inOrder(root)


class Tree:
    def __init__(self,val=0,Left=None,right=None):
        self.val = val
        self.Left = self.Left 
        self.Right = self.Right

def sortedArray(self, nums):
    def helper(l,r):
        if l > r:
            return None
        m = (l+r) // 2
        root = Tree(nums[m])
        root.left = helper(1,m-1)
        root.right = helper(1,m)