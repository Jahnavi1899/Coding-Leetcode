# class Solution:
#     def findCircleNum(self, isConnected) -> int:
#         n = len(isConnected)
#         isVisited = [0 for _ in range(n+1)]
#         cnt = 0
#         adjList = [[] for _ in range(n+1)]

#         for i in range(n):
#             for j in range(n):
#                 if i != j and isConnected[i][j]:
#                     adjList[i+1].append(j+1)
#         print(adjList)

#         for i in range(1, n+1):
#             if isVisited[i] == 0:
#                 cnt += 1
#                 self.dfs(i, isVisited, adjList)

#         return cnt

#     def dfs(self, node, isVisited, adjList):
#         isVisited[node] = 1
#         for n in adjList[node]:
#             if isVisited[n] == 0:
#                 self.dfs(n, isVisited, adjList)

class DisjointSet:
    def __init__(self, n):
        self.rank = [0 for _ in range(n+1)]
        self.parent = [i for i in range(n+1)]

    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, node1, node2):
        ult_p_node1 = self.findParent(node1)
        ult_p_node2 = self.findParent(node2)

        if ult_p_node1 == ult_p_node2:
            return

        if self.rank[ult_p_node1] > self.rank[ult_p_node2]:
            self.parent[ult_p_node2] = ult_p_node1
        elif self.rank[ult_p_node2] > self.rank[ult_p_node1]:
            self.parent[ult_p_node1] = ult_p_node2
        else:
            self.parent[ult_p_node1] = ult_p_node2
            self.rank[ult_p_node2] += 1

class Solution:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        disjointSet = DisjointSet(n)
        res = 0
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    disjointSet.unionByRank(i+1, j+1)
                    # adjList[i+1].append(j+1)
                    # adjList[j+1].append(i+1)
        print(disjointSet.parent)
        for i in range(1, n+1):
            if disjointSet.parent[i] == i:
                res += 1
        return res
        


        

isConnected = [[1,1,0],[1,1,0],[0,0,1]]

obj = Solution()
print(obj.findCircleNum(isConnected))

        