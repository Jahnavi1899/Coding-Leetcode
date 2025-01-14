# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root):
        return self.rootToLeaf(root, 0)


    def rootToLeaf(self, root, pathSum):
        if not root:
            return 0
    
        pathSum = pathSum * 10 + root.val
        if not root.left and not root.right:
            return pathSum
        return self.rootToLeaf(root.left, pathSum) + self.rootToLeaf(root.right, pathSum)

root = TreeNode(1)
root.left = TreeNode(9)
root.right = TreeNode(0)
root.left.left = TreeNode(5)    
root.left.right = TreeNode(1)

sol = Solution()
print(sol.sumNumbers(root))