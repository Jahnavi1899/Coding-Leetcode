# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        res = []
        if root:
            queue = [root]
            while queue:
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if i == 0:
                        res.append(node.val)
                    
                    if node.right:
                        queue.append(node.right)

                    if node.left:
                        queue.append(node.left)
        return res
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

obj = Solution()
print(obj.rightSideView(root))