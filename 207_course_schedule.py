class Solution:
    def canFinish(self, numCourses, prerequisites):
        adjList = [[] for _ in range(numCourses)]
        for i, j in prerequisites:
            adjList[j].append(i)

        visited = [0 for _ in range(numCourses)]
        pathvisited = [0 for _ in range(numCourses)]
        for n in range(numCourses):
            if visited[n] == 0:
                res = self.isCycle(n, adjList, visited, pathvisited)
                if res:
                    return False
        return True

    def isCycle(self, node, adjList, visited, pathvisited):
        visited[node] = 1
        pathvisited[node] = 1

        for adj in adjList[node]:
            if visited[adj] == 0:
                ans = self.isCycle(adj, adjList, visited, pathvisited)
                if ans:
                    return True
            elif pathvisited[adj] == 1:
                return True
        pathvisited[node] = 0
        return False
    
numCourses = 2
prerequisites = [[1,0],[0,1]]

obj = Solution()
print(obj.canFinish())
