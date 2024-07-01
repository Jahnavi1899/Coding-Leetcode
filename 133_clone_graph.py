# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node:
            nodeMap = {}
            return self.dfs(node, nodeMap)
        
        return None

    def dfs(self, node, nodeMap):
        if node in nodeMap:
            return nodeMap[node]
        
        copy = Node(node.val)
        nodeMap[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor, nodeMap))
        return copy
    
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

root.neighbors.append(node2)
root.neighbors.append(node4)

node2.neighbors.append(root)
node2.neighbors.append(node3)

node3.neighbors.append(node2)
node3.neighbors.append(node4)

node4.neighbors.append(root)
node4.neighbors.append(node3)

obj = Solution()
print(obj.cloneGraph(root))