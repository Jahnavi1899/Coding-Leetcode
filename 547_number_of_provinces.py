class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        isVisited = [0 for _ in range(n+1)]
        cnt = 0
        adjList = [[] for _ in range(n+1)]

        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j]:
                    adjList[i+1].append(j+1)
        print(adjList)

        for i in range(1, n+1):
            if isVisited[i] == 0:
                cnt += 1
                self.dfs(i, isVisited, adjList)

        return cnt

    def dfs(self, node, isVisited, adjList):
        isVisited[node] = 1
        for n in adjList[node]:
            if isVisited[n] == 0:
                self.dfs(n, isVisited, adjList)

isConnected = [[1,1,0],[1,1,0],[0,0,1]]

obj = Solution()
print(obj.findCircleNum(isConnected))

        