# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        mapping = self.nodeMap(root)
        targetNode = self.dfs(root, target)
        #nodeList = self.radialDistance(target, k, mapping)

        isVisited = []
        queue = [targetNode]
        dist = 0
        while dist < k:
            for _ in range(len(queue)):
                top = queue.pop(0)
                if top not in isVisited:
                    isVisited.append(top)
                if top.left and top.left not in isVisited:
                    queue.append(top.left)
                    isVisited.append(top.left)
                if top.right and top.right not in isVisited:
                    queue.append(top.right)
                    isVisited.append(top.right)
                if mapping[top] and mapping[top] not in isVisited:
                    queue.append(mapping[top])
                    isVisited.append(mapping[top])
            dist += 1
        print(queue)
        return []

    def nodeMap(self, root):
        # store the parent-child mapping for each node
        parent_child_mapping = {root: None}
        queue = [root]
        while queue:
            top = queue.pop(0)
            if top.left:
                parent_child_mapping[top.left] = top
                queue.append(top.left)
            if top.right:
                parent_child_mapping[top.right] = top
                queue.append(top.right)

        return parent_child_mapping
            
    def dfs(self, root, target):
        if root:
            if root.val == target.val:
                return root
            return self.dfs(root.left, target) or self.dfs(root.right, target)
        else:
            return 

    # calculating the radial distance from the target
    def radialDistance(self, target, k, mapping):
        isVisited = []
        queue = [target]
        dist = 0
        while dist < k:
            for _ in range(len(queue)):
                top = queue.pop(0)
                if top not in isVisited:
                    isVisited.append(top)
                if top.left and top.left not in isVisited:
                    queue.append(top.left)
                    isVisited.append(top.left)
                if top.right and top.right not in isVisited:
                    queue.append(top.right)
                    isVisited.append(top.right)
                if mapping[top] and mapping[top] not in isVisited:
                    queue.append(mapping[top])
                    isVisited.append(mapping[top])
            dist += 1
        print(queue)
        return queue




root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

target = TreeNode(5)
k = 2

obj = Solution()
print(obj.distanceK(root, target, k))
