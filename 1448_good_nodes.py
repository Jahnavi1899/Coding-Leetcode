# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []
        queue = [root]
        while queue:
            path = []
            top = queue.pop(0)
            self.findPath(root, top, path)
            if len(path) == 0:
                res.append(top)
            if top.left:
                queue.append(top.left)
            if top.right:
                queue.append(top.right)
        return len(res)
            
            

    def findPath(self, root, target, res):
        if root:
            if root.val > target.val:
                res.append(root.val)
            if root == target:
                return True
            left = self.findPath(root.left, target, res)
            if left:
                return True
            right = self.findPath(root.right, target, res)
            if left and right:
                res.pop()
                return False
            else:
                return True
        else:
            return False
            
    
root = TreeNode(3)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

obj = Solution()
print(obj.goodNodes(root))

          
        