class DisjointSet :

    rank, parent = [], []

    def __init__(self, n):
        self.rank = [0 for _ in range(n)]
        self.parent = [0 for _ in range(n)]
        for i in range(0, n):
            self.parent[i] = i

    # path compression 
    '''
        Path compression is done while finding the parent. It updates parent of each node
        to its ultimate parent.
    '''
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.findParent(self.parent[node])
    
    def unionByRank(self, u, v):
        up_u = self.findParent(u)
        up_v = self.findParent(v)

        if up_u == up_v:
            return
        if self.rank[up_u] < self.rank[up_v]:
            self.parent[up_u] = up_v
        elif self.rank[up_v] < self.rank[up_u]:
            self.parent[up_v] = up_u
        else:
            self.parent[up_u] = self.parent[up_v]
            self.rank[up_u] += 1

def KruskalAlgo(adjList):
    # create a list of (weight, node1, node2)
    edges = []
    n = len(adjList)
    # O(V+E)
    for node1 in range(n):
        for node2, weight in adjList[node1]:
            edges.append([weight, node1, node2])

    disjointSet = DisjointSet(n)
    edges.sort() # O(log(V))
    mstWeight = 0
    res = []
    # V * 4 * alpha
    for weight, node1, node2 in edges:
        if disjointSet.findParent(node1) != disjointSet.findParent(node2):
            disjointSet.unionByRank(node1, node2)
            mstWeight += weight
            res.append([node1, node2])

    return mstWeight, res

        

# obj = DisjointSet(7)
# obj.unionByRank(1, 2)
# obj.unionByRank(2, 3)
# obj.unionByRank(4, 5)
# obj.unionByRank(6, 7)
# obj.unionByRank(5, 6)
# print(obj.findParent(3))
# print(obj.findParent(7))
# obj.unionByRank(3, 7)

# print(obj.findParent(3))
# print(obj.findParent(7))

adjList = [[[1,2],[3,1],[4,4]], [[0,2],[2,3],[3,3],[5,7]], [[1,3],[3,5],[5,8]], [[0,1],[1,3],[2,5],[4,9]], [[0,4],[3,9]], [[1,7], [2,8]]]
weight, mst = KruskalAlgo(adjList)

print(weight)
print(mst)

        


