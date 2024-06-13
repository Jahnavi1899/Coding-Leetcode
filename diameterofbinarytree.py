# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        max_path = [0]
        self.calculateHeight(root, max_path)
        return max_path
        

    def calculateHeight(self, root, max_path):
        if root:
            lh = self.calculateHeight(root.left, max_path)
            rh = self.calculateHeight(root.right, max_path)
            max_path[0] = max(max_path[0], lh+rh)
            return max(lh, rh) + 1
        else:
            return 0
        
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
        
obj = Solution()
print(obj.diameterOfBinaryTree(tree))