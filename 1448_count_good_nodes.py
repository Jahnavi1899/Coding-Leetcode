# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = [0]
        self.dfs(root, root.val, cnt)
        return cnt

    def dfs(self, node, pathMax, cnt):
        if pathMax <= node.val:
            cnt[0] += 1
        
        if node.left:
            self.dfs(node.left, max(pathMax, node.val), cnt)

        if node.right:
            self.dfs(node.right, max(pathMax, node.val), cnt)

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)

obj = Solution()
print(obj.goodNodes(root))
        