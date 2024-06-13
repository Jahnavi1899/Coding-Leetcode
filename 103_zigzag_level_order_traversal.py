# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if root:
            queue = [root]
            flag = 0
       
            while queue:
                temp = []
                n = len(queue)
                for _ in range(n):
                    top_element = queue.pop(0)
                    temp.append(top_element.val)

                    if top_element.left:
                        queue.append(top_element.left)
                    if top_element.right: 
                        queue.append(top_element.right)
                if flag:
                    res.append(temp[::-1])
                else:
                    res.append(temp[::])
                flag = not flag
                
            print(res)
        return res

        