class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def leafSimilar(root1, root2):
    leaf_root1 = []
    leaf_root2 = []
    get_leaf_node(root1, leaf_root1)
    get_leaf_node(root2, leaf_root2)

    if leaf_root1 == leaf_root2:
        return True
    else:
        return False

def get_leaf_node(root_node, leaf_lst):
    if root_node == None:
        return
    elif root_node.left == None and root_node.right == None:
        leaf_lst.append(root_node.val)
    else:
        get_leaf_node(root_node.left, leaf_lst)
        get_leaf_node(root_node.right, leaf_lst)

root1 = TreeNode(1, TreeNode(2, None, None), TreeNode(3, None, None))
root2 = TreeNode(1, TreeNode(3, None, None), TreeNode(2, None, None))
print(leafSimilar(root1, root2))
