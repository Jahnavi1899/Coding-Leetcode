class DisjointSet :

    rank, parent = [], []

    def __init__(self, n):
        self.rank = [0 for _ in range(n+1)]
        self.parent = [0 for _ in range(n+1)]
        for i in range(1, n+1):
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

obj = DisjointSet(7)
obj.unionByRank(1, 2)
obj.unionByRank(2, 3)
obj.unionByRank(4, 5)
obj.unionByRank(6, 7)
obj.unionByRank(5, 6)
print(obj.findParent(3))
print(obj.findParent(7))
obj.unionByRank(3, 7)

print(obj.findParent(3))
print(obj.findParent(7))

        


