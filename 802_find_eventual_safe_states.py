class Solution:
    # def eventualSafeNodes(self, graph):
    #     n = len(graph)
    #     isSafeNode = [0 for _ in range(n)]
    #     visited = [0 for _ in range(n)]
    #     pathvisited = [0 for _ in range(n)]

    #     for i in range(n):
    #         if visited[i] == 0:
    #             self.isCycle(i, graph, visited, pathvisited, isSafeNode)

    #     res = []
    #     for node in range(n):
    #         if isSafeNode[node] == 1:
    #             res.append(node)
    #     return res



    # def isCycle(self, node, graph, visited, pathvisited, isSafeNode):
    #     visited[node] = 1
    #     pathvisited[node] = 1
    #     for adj in graph[node]:
    #         if visited[adj] == 0:
    #             check = self.isCycle(adj, graph, visited, pathvisited, isSafeNode)
    #             if check:
    #                 isSafeNode[node] = 0
    #                 return True
    #         elif pathvisited[adj] == 1:
    #             isSafeNode[adj] = 0
    #             return True

    #     isSafeNode[node] = 1
    #     pathvisited[node] = 0
    #     return False


    def eventualSafeNodes(self, graph):
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        res = []

        for i in range(n):
            for e in graph[i]:
                reverse_graph[e].append(i)
                indegree[i] += 1

        queue = []
        for j in range(n):
            if indegree[j] == 0:
                queue.append(j)

        while queue:
            front = queue.pop(0)
            res.append(front)

            for adj in reverse_graph[front]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)
            

        return sorted(res)

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
obj = Solution()

print(obj.eventualSafeNodes(graph))