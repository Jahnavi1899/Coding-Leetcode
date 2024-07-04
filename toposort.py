class Toposort:

    def topoSortDFS(self, n, adjList):
        '''
            TC : O(V+E)
            SC : O(V)
        '''
        visited = [0 for _ in range(n)]
        stack = []
        for i in range(n):
            if visited[i] == 0:
                self.dfs(i, visited, stack, adjList)

        res = []
        while stack:
            node = stack.pop()
            res.append(node)

        return res

    def dfs(self, node, visited, stack, adjList):
        visited[node] = 1
        for i in adjList[node]:
            if visited[i] == 0:
                self.dfs(i, visited, stack, adjList)

        stack.append(node)

    def topoSortBFS(self, n, adjList):
        indegree = [0 for _ in range(n)]
        res = []

        for adj in adjList:
            for node in adj:
                indegree[node] += 1

        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            front = queue.pop(0)
            res.append(front)

            for neigh in adjList[front]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        return res

adjList = [[],[],[3],[1],[0,1],[0,2]]
n = 6

obj = Toposort()
#print(obj.topoSortDFS(n, adjList))
print(obj.topoSortBFS(n, adjList))