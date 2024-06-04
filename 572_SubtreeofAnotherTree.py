# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        if root is None:
            return False
        if root.val == subRoot.val:
            return self.checkSimilar(root, subRoot)
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def checkSimilar(self, root, subRoot):
        if root is None or subRoot is None:
            return True
        if root is None or subRoot is None or root.val != subRoot.val:
            return False
        left = self.checkSimilar(root.left, subRoot.left)
        right = self.checkSimilar(root.right, subRoot.right)

        return left and right
    
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))

obj = Solution().isSubtree(root, subRoot)
print(obj)
        