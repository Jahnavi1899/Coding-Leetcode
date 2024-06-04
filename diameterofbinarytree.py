class Node:
     def __init__(self, val, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

def diameterOfBinaryTree(root):
     max_height = 0
     

# def diameterOfBinaryTree(root):
#     max_path = 0
#     dfs(root, max_path)
#     return max_path

# def dfs(root, max_path):
#     if not root:
#         return 0
#     left = dfs(root.left, max_path)
#     right = dfs(root.right, max_path)
#     max_path = max(max_path, left+right)
#     return 1 + max(left, right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(diameterOfBinaryTree(root))