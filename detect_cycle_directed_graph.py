# on the same path the node should not be revisited

def detectCycle(n, adjList):
    visited = [0 for _ in range(n)]
    pathVisited = [0 for _ in range(n)]

    for i in range(n):
        if visited[i] == 0:
            res = dfs(i, visited, pathVisited, adjList)
            if res:
                return True
    
    return False
            
def dfs(node, visited, pathvisited, adjList):
    visited[node] = 1
    pathvisited[node] = 1
    for adj in adjList[node]:
        if visited[adj] == 0 and pathvisited[adj] == 0:
            if dfs(adj, visited, pathvisited, adjList):
                return True
        elif visited[adj] == 1 and pathvisited[adj] == 1:
            return True
    pathvisited[node] = 0
    return False

adjList = [[5],[4],[3],[1],[0],[2]]
n = 6

print(detectCycle(n, adjList))

