"""
# Definition for a Node.
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root:
            queue = [root]
            while queue:
                n = len(queue)
                for i in range(n):
                    top = queue.pop(0)
                    print(i)
                    if i < n-1:
                        top.next = queue[0]
                    if top.left:
                        queue.append(top.left)
                    if top.right:
                        queue.append(top.right)

        return root
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

sol = Solution()
sol.connect(root)
print(root)



        