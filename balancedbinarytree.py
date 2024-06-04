class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balancedBinaryTree(root):
    leftHeight = Height(root, 'left')
    rightHeight = Height(root, 'right')

    diff = abs(leftHeight - rightHeight)
    if diff != 1:
        return False
    else:
        balancedBinaryTree(root.left)
        balancedBinaryTree(root.right)
        


def Height(root, side):
    if root is None:
        return 0
    if side == 'left':
        return 1 + Height(root.left, side)
    else:
        return 1 + Height(root.right, side)
    