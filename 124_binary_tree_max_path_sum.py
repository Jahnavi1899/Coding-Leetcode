# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root) -> int:
        pathsum = [0]
        self.findMaxPathSum(root, pathsum)
        return pathsum[0]

    def findMaxPathSum(self, root, pathsum):
        if not root:
            return pathsum[0]
        print(pathsum)
        pathsum[0] = pathsum[0]+root.val
        lh = self.findMaxPathSum(root.left, pathsum)
        rh = self.findMaxPathSum(root.right, pathsum)
        pathsum[0] = max(pathsum[0], lh + rh)
        return max(lh, rh)
    
root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(3)
sol = Solution()
print(sol.maxPathSum(root)) # 6
        