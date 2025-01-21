# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {}
        for i, num in enumerate(inorder):
            inorder_map[num] = i

        return self.buildBinaryTree(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1, inorder_map)

        
    def buildBinaryTree(self, inorder, in_start, in_end, postorder, post_start, post_end, inorder_map):
        if (in_start > in_end) or (post_start > post_end):
            return None

        root = TreeNode(postorder[post_end])
        rootIdx = inorder_map[root.val]
        numLeft = rootIdx - post_start
        
        print(inorder[in_start:in_end+1])
        print(postorder[post_start:post_end+1])

        left = self.buildBinaryTree(inorder, in_start, rootIdx - 1, postorder, post_start, post_start + numLeft - 1, inorder_map)

        right = self.buildBinaryTree(inorder, rootIdx+1, in_end, postorder, post_start + numLeft, post_end-1, inorder_map)

        root.left = left
        root.right = right

        return root
        
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

sol = Solution()
root = sol.buildTree(inorder, postorder)
print(root)