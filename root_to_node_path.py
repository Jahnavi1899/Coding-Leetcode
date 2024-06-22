class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rootToNodePath(root, val, res):
    if root:
        res.append(root.val)
        if root.val == val:
            return True
        left = rootToNodePath(root.left, val, res)
        right = rootToNodePath(root.right, val, res)
        if left or right:
            return True
        res.pop()
        return False


    else:
        return False
    

    
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(6)
root.left.right = Node(2)
root.right.left = Node(0)
root.right.right = Node(8)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

res = []
rootToNodePath(root, 8, res)
print(res)
    